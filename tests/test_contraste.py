"""Contrôle de non-régression des contrastes WCAG de la feuille de style.

Le point n°1 de la grille UI/UX est l'accessibilité, et le contraste en est
la part la plus facile à casser sans s'en apercevoir : un jeton retouché à
la main dans `app/css/style.css` peut faire passer un texte sous le seuil
sans qu'aucun test existant ne bronche. Ce fichier ferme ce trou.
"""

import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parents[1]
CSS = RACINE / "app" / "css" / "style.css"


def luminance(hexa: str) -> float:
    """Luminance relative d'une couleur hexadécimale (formule WCAG)."""
    h = hexa.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    canaux = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    lin = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in canaux)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    haut, bas = max(la, lb), min(la, lb)
    return (haut + 0.05) / (bas + 0.05)


def jetons(entete: str) -> dict[str, str]:
    """Collecte les `--var: #hex` d'un bloc, jusqu'à son accolade fermante."""
    trouves: dict[str, str] = {}
    dedans = False
    for ligne in CSS.read_text(encoding="utf-8").splitlines():
        nue = ligne.strip()
        if nue.startswith(entete):
            dedans = True
            continue
        if dedans and nue == "}":
            break
        if dedans:
            m = re.match(r"--([a-z0-9-]+):\s*(#[0-9a-fA-F]{3,8})", nue)
            if m:
                trouves["--" + m.group(1)] = m.group(2)
    return trouves


# (premier plan, arrière-plan, seuil, description)
PAIRES = [
    ("--ink", "--bg", 4.5, "texte courant sur fond"),
    ("--ink", "--surface", 4.5, "texte sur carte"),
    ("--ink-doux", "--surface", 4.5, "texte secondaire sur carte"),
    ("--ink-faible", "--surface", 4.5, "consigne sur carte"),
    ("--ink-faible", "--bg", 4.5, "libellé de navigation sur fond"),
    ("--accent", "--surface", 4.5, "accent sur carte"),
    ("--accent", "--bg", 3.0, "onglet actif sur fond (non-texte)"),
    ("--su", "--surface", 4.5, "bouton Su"),
    ("--hesite", "--surface", 4.5, "bouton Hésité"),
    ("--rate", "--surface", 4.5, "bouton Raté"),
    ("--sur-accent", "--accent", 4.5, "texte du bouton Révéler"),
    # WCAG 1.4.11 vise les composants d'interface (champs, boutons), pas un
    # liseré décoratif entre deux surfaces déjà distinctes par leur fond.
    # On vérifie seulement qu'il reste perceptible.
    ("--rule", "--surface", 1.2, "bordure de carte (décorative)"),
    ("--surface", "--bg", 1.05, "carte détachée du fond"),
]

THEMES = {
    "sombre (défaut)": ":root {",
    "clair": ':root[data-theme="clair"]',
}


def evaluer(verbeux: bool = False) -> list[tuple]:
    """Retourne la liste des couples passant sous leur seuil."""
    echecs = []
    for nom, entete in THEMES.items():
        t = jetons(entete)
        if verbeux:
            print(f"\n=== {nom} ({len(t)} jetons) ===")
        for fg, bg, seuil, desc in PAIRES:
            if fg not in t or bg not in t:
                echecs.append((nom, desc, "jeton absent", seuil))
                continue
            r = ratio(t[fg], t[bg])
            if r < seuil:
                echecs.append((nom, desc, round(r, 2), seuil))
            if verbeux:
                marque = "OK   " if r >= seuil else "ÉCHEC"
                print(f"  {marque} {r:5.2f}:1 (min {seuil})  {desc}")
    return echecs


def test_contrastes_wcag():
    """Aucun couple texte/fond ne doit passer sous son seuil WCAG."""
    echecs = evaluer()
    assert not echecs, f"{len(echecs)} contraste(s) insuffisant(s) : {echecs}"


if __name__ == "__main__":
    ech = evaluer(verbeux=True)
    print(f"\nTOTAL ÉCHECS : {len(ech)}")
    for e in ech:
        print("  ", e)
    sys.exit(1 if ech else 0)
