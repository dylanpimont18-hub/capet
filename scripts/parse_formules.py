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


_HEADING = re.compile(r"^###\s+(?:\d+\.\d+\s+)?(?P<titre>.+?)\s*$")

# Certaines formules ne sont pas précédées d'un heading `###` mais d'une
# ligne en gras qui joue le même rôle d'intitulé :
#   **Modèle électrique de la MCC à excitation séparée :**
#   $$U = R_a I_a + ...$$
# Sans cela, ces cartes affichent « Énoncez la relation : (sans titre) ».
_INTITULE_GRAS = re.compile(r"^\*\*(?P<titre>[^*]{6,120}?)\s*:?\*\*\s*:?\s*$")

# « pour » est VOLONTAIREMENT absent : mesuré sur le corpus, il capture à lui
# seul 97 lignes de prose sur 138 (« Pour une installation comportant… »,
# « pour $f = 50$ Hz », « pour diminuer le courant ») et fait passer le bruit
# de 7 à 35 captures. Ne pas le rajouter.
_MARQUEURS = (
    "si ", "valable", "à condition", "hypothèse", "hypothèses",
    "uniquement", "lorsque", "en régime", "condition",
)

# Une « condition » qui cite une source ou se termine par « : » est en fait
# une métadonnée ou une amorce de paragraphe, pas une condition.
_REJETS = ("source :", "source directe", "exemple", "résultat imposé")
_LONGUEUR_MAX = 200


def _nettoyer(ligne: str) -> str:
    """Retire puces et marques de gras d'une condition.

    `lstrip("*- ")` seul laisse le `**` FERMANT : sur « **Attention** : … »
    il produit « Attention** : … », affiché tel quel par echapper(). On retire
    donc la puce par regex, puis les paires de gras.
    """
    s = re.sub(r"^\s*[-*]+\s*", "", ligne.strip())
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    return s.replace("**", "").strip()


def _est_condition(ligne: str) -> bool:
    """Vrai si la ligne énonce une condition d'application exploitable."""
    s = _nettoyer(ligne)
    bas = s.lower()

    if len(s) > _LONGUEUR_MAX:
        return False                      # paragraphe entier, pas une condition
    if s.rstrip().endswith(":"):
        return False                      # amorce de paragraphe
    if any(r in bas for r in _REJETS):
        return False                      # métadonnée de source

    return any(bas.startswith(m) or f" {m}" in bas for m in _MARQUEURS)


def parse_block_formulas(section_text: str, theme_id: str) -> list[dict]:
    """Extrait les formules écrites en blocs $$ ... $$.

    Le label provient du heading `###` courant, privé de sa numérotation.
    Les conditions proviennent des lignes suivant le bloc qui portent un
    marqueur de condition ; la prose descriptive est écartée.
    """
    lignes = section_text.splitlines()
    cards = []
    label_courant = ""

    i = 0
    while i < len(lignes):
        ligne = lignes[i].rstrip()

        h = _HEADING.match(ligne)
        if h:
            label_courant = h.group("titre").strip()
            i += 1
            continue

        # Un intitulé en gras précise le label sans remplacer la section :
        # il vaut pour les blocs qui le suivent immédiatement.
        g = _INTITULE_GRAS.match(ligne.strip())
        if g:
            label_courant = g.group("titre").strip().rstrip(":").strip()
            i += 1
            continue

        if ligne.startswith("$$"):
            # Bloc sur une ligne, ou multi-lignes jusqu'au $$ fermant.
            if ligne.endswith("$$") and len(ligne) > 4:
                latex = ligne[2:-2].strip()
                j = i + 1
            else:
                buf = [ligne[2:]]
                j = i + 1
                while j < len(lignes) and not lignes[j].rstrip().endswith("$$"):
                    buf.append(lignes[j])
                    j += 1
                if j < len(lignes):
                    buf.append(lignes[j].rstrip()[:-2])
                    j += 1
                latex = "\n".join(buf).strip()

            # Conditions : lignes suivantes jusqu'au prochain heading ou bloc.
            conditions = []
            k = j
            while k < len(lignes):
                suite = lignes[k].rstrip()
                if suite.startswith("###") or suite.startswith("$$") or suite.startswith("## "):
                    break
                if suite.strip() and _est_condition(suite):
                    conditions.append(_nettoyer(suite))
                k += 1

            if latex:
                cards.append({
                    "type": "formule",
                    "theme": theme_id,
                    "label": label_courant or "(sans titre)",
                    "latex": latex,
                    "unites": "",
                    "frequence": "",
                    "conditions": " ".join(conditions),
                    "source_format": "bloc",
                })
            i = j
            continue

        i += 1

    return cards
