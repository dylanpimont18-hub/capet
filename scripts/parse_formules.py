"""Extraction des cartes formule depuis les fichiers T{nn}_contenu.md."""

import re

_SEP = re.compile(r"^[\s|:\-]+$")

# Mots-clés de reconnaissance des colonnes, testés sur la ligne d'en-tête.
_CLE_LABEL = ("grandeur", "loi", "contexte", "paramètre", "parametre", "nom")
_CLE_UNITE = ("unité", "unite")
_CLE_FREQ = ("fréquence", "frequence")


def _cellules(ligne: str) -> list[str]:
    """Découpe une ligne de tableau en respectant les segments math.

    Un `split("|")` naïf casse `$|\\underline{Z}| = \\sqrt{R^2}$` (module
    d'une impédance, T03) : les barres verticales de la notation « module »
    sont prises pour des séparateurs de colonnes. Résultat sans cette garde :
    une carte dont le verso est le seul caractère `$`.
    """
    contenu = ligne.strip().strip("|")
    parts: list[str] = []
    buf: list[str] = []
    dans_math = False
    for ch in contenu:
        if ch == "$":
            dans_math = not dans_math
            buf.append(ch)
        elif ch == "|" and not dans_math:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf))
    return [p.strip() for p in parts]


def _strip_math(s: str) -> str:
    """Retire les délimiteurs $...$ autour d'une formule.

    Uniquement quand la cellule est UN seul segment math. Une cellule comme
    `$R = U^2/P$ (charge purement résistive)` en contient deux morceaux :
    retirer le premier et le dernier `$` produirait du LaTeX invalide.
    """
    s = s.strip()
    if s.count("$") == 2 and s.startswith("$") and s.endswith("$"):
        return s[1:-1].strip()
    return s


def _clean_unit(s: str) -> str:
    """Le tiret cadratin signifie 'sans unité'."""
    s = s.strip()
    return "" if s in {"—", "-", "–", "", "sans unité"} else s


def _indices(entete: list[str]) -> dict | None:
    """Déduit la position de chaque colonne depuis la ligne d'en-tête.

    Retourne None si le tableau n'a pas de colonne « Formule » : ce n'est
    alors pas un tableau de formules (tableau de technologies, de quadrants,
    de caractéristiques…) et il doit être ignoré entièrement.
    """
    bas = [c.lower() for c in entete]
    i_formule = next((i for i, c in enumerate(bas) if "formule" in c), None)
    if i_formule is None:
        return None

    def cherche(cles, exclure):
        return next(
            (i for i, c in enumerate(bas)
             if i != exclure and any(k in c for k in cles)),
            None,
        )

    i_label = cherche(_CLE_LABEL, i_formule)
    if i_label is None:
        # Pas de colonne descriptive nommée : on prend la colonne voisine.
        i_label = 1 if i_formule == 0 and len(bas) > 1 else (0 if i_formule > 0 else None)

    return {
        "formule": i_formule,
        "label": i_label,
        "unite": cherche(_CLE_UNITE, i_formule),
        "freq": cherche(_CLE_FREQ, i_formule),
    }


def parse_table_formulas(section_text: str, theme_id: str) -> list[dict]:
    """Extrait les formules écrites sous forme de tableau Markdown.

    Les colonnes sont localisées par la ligne d'en-tête, JAMAIS par position
    fixe : le corpus mélange `| Grandeur | Formule | Unité |` (formule en
    colonne 2) et `| Formule LaTeX | Contexte | Fréquence | Source |`
    (formule en colonne 1). Supposer une position fixe corrompt 58 % du
    corpus sans lever d'erreur.
    """
    cards = []
    idx = None

    for ligne in section_text.splitlines():
        ligne = ligne.rstrip()
        if not ligne.startswith("|") or _SEP.match(ligne):
            continue

        cells = _cellules(ligne)

        # Une ligne sans $ est une ligne d'en-tête : elle (re)définit le schéma.
        if "$" not in ligne:
            idx = _indices(cells)
            continue

        if idx is None:
            continue  # tableau sans colonne Formule : ignoré

        def col(nom: str) -> str:
            i = idx[nom]
            return cells[i] if i is not None and i < len(cells) else ""

        latex = col("formule")
        if "$" not in latex:
            continue

        cards.append({
            "type": "formule",
            "theme": theme_id,
            "label": col("label"),
            "latex": _strip_math(latex),
            "unites": _clean_unit(col("unite")),
            "frequence": col("freq"),
            "conditions": "",
            "source_format": "table",
        })
    return cards
