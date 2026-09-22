"""Orchestrateur : assemble app/cards.json depuis les sources LaTeX/Markdown.

Usage : python scripts/build_cards.py [--sans-svg]
"""

import argparse
import datetime
import json
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE))

from scripts.parse_formules import parse_table_formulas, parse_block_formulas
from scripts.parse_pieges import parse_pieges
from scripts.parse_meta import parse_meta
from scripts.extract_tikz import extract_tikz_envs
from scripts.build_svg import compile_tikz

_PREFIXE = {"formule": "f", "piege": "p", "schema": "s"}
_SECTION_1 = re.compile(r"^## 1\..*?(?=^## 2\.|\Z)", re.S | re.M)


def faire_id(theme: str, type_carte: str, n: int) -> str:
    return f"{theme}-{_PREFIXE[type_carte]}-{n:03d}"


# Vocabulaire réel de la colonne « Fréquence » des fiches, relevé sur le
# corpus au 2026-09-21. Multiplie le poids de thème pour les 114 formules
# qui le portent ; une valeur inconnue laisse le poids inchangé (1.0).
_BONUS_FREQUENCE = {
    "systématique": 1.30,
    "à connaître par cœur": 1.30,
    "très fréquent": 1.20,
    "fréquent": 1.10,
    "base": 1.10,
    "courant": 1.00,
    "présent": 0.90,
}


def _poids_final(poids_theme: float, frequence: str) -> float:
    """Affine le poids de thème par la fréquence propre à la formule.

    Le texte est normalisé (minuscules, accords féminins, parenthèses
    retirées) puis cherché par préfixe : « Très fréquente (donnée ou
    calculée) » doit valoir autant que « Très fréquent ».
    """
    if not frequence:
        return round(poids_theme, 4)
    f = frequence.lower().split("(")[0].strip().rstrip("es").strip()
    for cle, bonus in _BONUS_FREQUENCE.items():
        base = cle.rstrip("es")
        if f.startswith(base):
            return round(poids_theme * bonus, 4)
    return round(poids_theme, 4)


def assembler(themes: list[dict], cartes: list[dict]) -> dict:
    """Assemble la structure finale, en attribuant ids et poids."""
    poids_par_theme = {t["code"]: t["poids"] for t in themes}
    compteurs: dict[tuple[str, str], int] = {}
    sorties = []

    for c in cartes:
        theme = c["theme"]
        if theme not in poids_par_theme:
            raise ValueError(f"carte rattachée à un thème inconnu : {theme}")
        cle = (theme, c["type"])
        compteurs[cle] = compteurs.get(cle, 0) + 1
        carte = dict(c)
        carte["id"] = faire_id(theme, c["type"], compteurs[cle])
        carte["poids"] = _poids_final(poids_par_theme[theme], c.get("frequence", ""))
        sorties.append(carte)

    return {
        "version": 1,
        "genere_le": datetime.date.today().isoformat(),
        "themes": themes,
        "cards": sorties,
    }


def construire(sans_svg: bool = False) -> dict:
    fiches = RACINE / "fiches"
    niveaux_path = RACINE / "scripts" / "niveaux_schemas.json"
    niveaux = json.loads(niveaux_path.read_text(encoding="utf-8")) if niveaux_path.exists() else {}

    themes, cartes = [], []

    for tex in sorted(fiches.glob("T[0-9][0-9]_[A-Z]*.tex")):
        if "contenu" in tex.name or "pilote" in tex.name:
            continue
        texte_tex = tex.read_text(encoding="utf-8")
        meta = parse_meta(texte_tex)
        code = meta["code"]
        themes.append(meta)

        md = fiches / f"{code}_contenu.md"
        if md.exists():
            texte_md = md.read_text(encoding="utf-8")
            m1 = _SECTION_1.search(texte_md)
            if m1:
                section1 = m1.group(0)
                cartes += parse_table_formulas(section1, code)
                cartes += parse_block_formulas(section1, code)
            cartes += parse_pieges(texte_md, code)

        for i, env in enumerate(extract_tikz_envs(texte_tex), start=1):
            rel = f"svg/{env['hash']}.svg"
            dest = RACINE / "app" / rel
            if not sans_svg and not dest.exists():
                if not compile_tikz(env["code"], env["env"], dest):
                    print(f"  ! schema non compile : {code} n°{i}", file=sys.stderr)
                    continue
            # Une carte schéma sans son image n'a aucun sens : en mode
            # --sans-svg, on ne l'émet pas plutôt que de produire une carte
            # dont le recto est une image cassée.
            if not dest.exists():
                continue
            cartes.append({
                "type": "schema",
                "theme": code,
                "svg": rel,
                "niveau": niveaux.get(env["hash"], "reconnaissance"),
                "label": f"Schéma {code} n°{i}",
            })

    return assembler(themes, cartes)


def ecrire_sw_assets(app_dir: pathlib.Path) -> int:
    """Génère app/sw-assets.js : la liste des fichiers à précacher.

    Le service worker doit connaître les SVG de schémas et les polices
    KaTeX. Sans cela, un schéma jamais affiché avant la coupure réseau
    donne une image cassée, et les formules tombent sur une police de
    substitution au premier lancement hors-ligne.
    """
    chemins: list[str] = []

    svg_dir = app_dir / "svg"
    if svg_dir.exists():
        chemins += sorted(f"./svg/{p.name}" for p in svg_dir.glob("*.svg"))

    fonts = app_dir / "vendor" / "katex" / "fonts"
    if fonts.exists():
        # Les .woff2 suffisent : tous les navigateurs cibles les gèrent.
        chemins += sorted(f"./vendor/katex/fonts/{p.name}"
                          for p in fonts.glob("*.woff2"))

    contenu = (
        "// Généré par build_cards.py — ne pas modifier à la main.\n"
        "self.ASSETS = " + json.dumps(chemins, indent=1) + ";\n"
    )
    (app_dir / "sw-assets.js").write_text(contenu, encoding="utf-8")
    return len(chemins)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sans-svg", action="store_true",
                    help="n'appelle pas LaTeX : itération rapide sur le texte. "
                         "Les cartes schéma dont le SVG n'existe pas encore "
                         "sont alors OMISES (pas d'image cassée).")
    args = ap.parse_args()

    data = construire(sans_svg=args.sans_svg)
    sortie = RACINE / "app" / "cards.json"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(
        json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    ecrire_sw_assets(RACINE / "app")
    par_type: dict[str, int] = {}
    for c in data["cards"]:
        par_type[c["type"]] = par_type.get(c["type"], 0) + 1
    print(f"{len(data['themes'])} themes, {len(data['cards'])} cartes -> {sortie}")
    print("  detail :", par_type)


if __name__ == "__main__":
    main()
