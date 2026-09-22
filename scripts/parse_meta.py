"""Extraction des métadonnées de thème depuis les fiches .tex."""

import re

_MACRO = "\\ficheEntete"
_PRESENCE = re.compile(
    r"Présence\s*:\}\s*\\textbf\{(?P<n>\d+)\s*/\s*(?P<sur>\d+)\}"
)


def _arguments(texte: str, depart: int, combien: int) -> list[str]:
    """Lit `combien` arguments {…} consécutifs à partir de `depart`.

    Équilibre les accolades : le titre de T20 contient
    `1\\textsuperscript{er}`, qu'un motif `[^}]*` tronquerait, décalant
    silencieusement tous les arguments suivants.
    """
    args: list[str] = []
    i = depart
    n = len(texte)
    while len(args) < combien and i < n:
        while i < n and texte[i] != "{":
            # Entre deux arguments on ne tolère que des blancs, % et sauts.
            if texte[i] not in " \t\r\n%":
                return args
            i += 1
        if i >= n:
            break
        profondeur = 1
        i += 1
        debut = i
        while i < n and profondeur:
            if texte[i] == "{":
                profondeur += 1
            elif texte[i] == "}":
                profondeur -= 1
            i += 1
        args.append(texte[debut:i - 1])
    return args


_BALISE = re.compile(r"\\[a-zA-Z]+\s*")


def _detex(s: str) -> str:
    """Transforme un fragment LaTeX en texte affichable.

    Le titre de T20 vaut `Filtres RC/RL - 1\\textsuperscript{er} et
    2\\textsuperscript{e} ordre` : sans nettoyage, l'app afficherait la
    commande telle quelle. On retire la commande et on garde son argument.
    """
    s = _BALISE.sub("", s)
    s = s.replace("{", "").replace("}", "")
    s = s.replace("~", " ").replace("\\", "")
    return re.sub(r"\s+", " ", s).strip()


def parse_meta(texte_tex: str) -> dict:
    """Extrait code, titre, domaine et fréquence d'apparition d'une fiche.

    Lève ValueError si la fiche n'a pas de \\ficheEntete — c'est un défaut
    de la source, pas un cas à ignorer silencieusement.
    """
    pos = texte_tex.find(_MACRO)
    if pos == -1:
        raise ValueError("aucun \\ficheEntete trouvé dans la fiche")

    # 0 = code, 1 = titre, 2 = couleur, 3 = domaine, 4 = ligne de présence
    args = _arguments(texte_tex, pos + len(_MACRO), 5)
    if len(args) < 2:
        raise ValueError("\\ficheEntete incomplet (moins de 2 arguments)")

    code = args[0].strip()
    titre = _detex(args[1])
    domaine = _detex(args[3]) if len(args) > 3 else ""

    p = _PRESENCE.search(args[4] if len(args) > 4 else texte_tex)
    n = int(p.group("n")) if p else 0
    sur = int(p.group("sur")) if p else 13
    poids = round(n / sur, 3) if sur else 0.0

    return {
        "code": code,
        "titre": titre,
        "domaine": domaine,
        "presence_n": n,
        "presence_sur": sur,
        "poids": poids,
    }
