"""Extraction des cartes piège depuis la section 5 des fiches.

La section 5 « LACUNES ET PIÈGES RÉCURRENTS » contient les conditions
d'application des formules, sous forme d'erreurs à éviter. C'est le
matériau des cartes de type « piege ».
"""

import re

_SECTION_5 = re.compile(r"^## 5\..*?(?=^## 6\.|\Z)", re.S | re.M)

# Format A : sous-titre ### (T02)
_H3 = re.compile(r"^###\s+(?:\d+\.\d+\s+)?(?P<titre>.+?)\s*$", re.M)
# Formats B et C : « 1. **Titre** : corps » ou « - **Titre** : corps »
_PUCE = re.compile(r"^(?:\d+\.|[-*])\s+\*\*(?P<titre>.+?)\*\*\s*:?\s*(?P<corps>.*)$")

# « Formule correcte » est un libellé réel de T02, absent d'une première
# lecture rapide : sans lui, la règle de ce piège reste vide.
_ALIAS_REGLE = ("La distinction", "Règle", "Correction", "Méthode correcte",
                "Formule correcte")

# Le lookahead de _champ doit s'arrêter sur un LIBELLÉ de champ, pas sur
# n'importe quel gras : sinon « ...valeur efficace du **fondamental** $I_1$ »
# tronque le champ au milieu d'une phrase (cas réel T02).
_LIBELLES = (
    r"(?:Le piège|La distinction|Règle|Correction|Méthode correcte"
    r"|Erreur type|Formule correcte)"
)

# Fin de première phrase : un point suivi d'un espace et d'une majuscule.
_FIN_PHRASE = re.compile(r"(?<=\.)\s+(?=[A-ZÀÉÈÊÎÔÛÇ])")


def _demarquer(s: str) -> str:
    """Retire le gras Markdown résiduel d'un texte de carte.

    Les corps de pièges contiennent du gras d'emphase en milieu de phrase
    (« confondre les deux colonnes **FP** et **cos φ** »). Sans ce
    nettoyage, `echapper()` afficherait les astérisques littéralement.
    """
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    return s.replace("**", "").strip()


def _champ(bloc: str, libelle: str) -> str:
    """Récupère le texte d'un champ `**Libellé** : ...` jusqu'au champ suivant.

    La borne est `\\n**` (gras en début de ligne), et non `**` : un gras en
    milieu de phrase (« Confondre **F_P** et cos φ ») ne doit pas tronquer
    le champ.
    """
    motif = re.compile(
        r"\*\*" + re.escape(libelle) + r"\*\*\s*:?\s*(?P<val>.*?)"
        r"(?=\n\s*\*\*" + _LIBELLES + r"\*\*|\Z)",
        re.S,
    )
    m = motif.search(bloc)
    if not m:
        return ""
    val = m.group("val").strip()
    val = re.sub(r"\n\s*[-*]\s*", " ", val)   # aplatit les sous-listes
    val = re.sub(r"\s*\n\s*", " ", val)
    return _demarquer(val)


def _couper(corps: str) -> tuple[str, str]:
    """Sépare le corps en (première phrase, reste)."""
    corps = corps.strip()
    parties = _FIN_PHRASE.split(corps, maxsplit=1)
    if len(parties) == 2:
        return parties[0].strip(), parties[1].strip()
    return corps, ""


def _parse_format_h3(section: str, theme_id: str) -> list[dict]:
    positions = [(m.start(), m.group("titre")) for m in _H3.finditer(section)]
    cartes = []
    for i, (debut, titre) in enumerate(positions):
        fin = positions[i + 1][0] if i + 1 < len(positions) else len(section)
        bloc = section[debut:fin]
        regle = ""
        for alias in _ALIAS_REGLE:
            regle = _champ(bloc, alias)
            if regle:
                break
        cartes.append({
            "type": "piege", "theme": theme_id, "titre": _demarquer(titre),
            "piege": _champ(bloc, "Le piège"), "regle": regle,
            "erreur_type": _champ(bloc, "Erreur type"),
        })
    return cartes


def _parse_format_liste(section: str, theme_id: str) -> list[dict]:
    """Formats B et C : item sur une ligne, éventuellement continué.

    Une ligne qui ne commence pas par une puce ni un chiffre prolonge l'item
    courant (les sources coupent parfois un item sur deux lignes).
    """
    cartes: list[dict] = []
    courant: list[str] = []
    titre_courant = ""

    def cloturer():
        if not titre_courant:
            return
        piege, regle = _couper(_demarquer(" ".join(courant)))
        cartes.append({
            "type": "piege", "theme": theme_id, "titre": _demarquer(titre_courant),
            "piege": piege, "regle": regle, "erreur_type": "",
        })

    for ligne in section.splitlines():
        nue = ligne.strip()
        if not nue or nue.startswith("#") or nue.startswith("---"):
            continue
        m = _PUCE.match(nue)
        if m:
            cloturer()
            titre_courant = m.group("titre").strip()
            courant = [m.group("corps").strip()]
        elif titre_courant:
            courant.append(nue)
    cloturer()
    return cartes


def parse_pieges(texte_fiche: str, theme_id: str) -> list[dict]:
    """Extrait les items de la section 5 en cartes piège.

    La section 5 a trois formats dans le corpus : sous-titres ### (T02),
    liste numérotée (T01-T17) et liste à puces (T18-T30). Les trois sont
    gérés ; ne traiter que le premier ne ramènerait que 8 items sur 199.
    """
    m = _SECTION_5.search(texte_fiche)
    if not m:
        return []
    section = m.group(0)

    cartes = _parse_format_h3(section, theme_id)
    if cartes:
        return cartes
    return _parse_format_liste(section, theme_id)
