"""Contrôles sur les questions rédigées des cartes formule.

Ces questions sont le seul contenu de l'app qui ne provienne pas des fiches
(cf. scripts/questions.json). Elles méritent donc leurs propres garde-fous :
une question qui livrerait sa réponse détruirait l'intérêt du rappel actif,
et une question orpheline signalerait une désynchronisation avec le corpus.
"""

import json
import pathlib
import re

RACINE = pathlib.Path(__file__).resolve().parents[1]
QUESTIONS = RACINE / "scripts" / "questions.json"
CARTES = RACINE / "app" / "cards.json"


def charger():
    q = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    d = json.loads(CARTES.read_text(encoding="utf-8"))
    return q, {c["id"]: c for c in d["cards"]}


def test_json_valide_et_non_vide():
    q, _ = charger()
    assert q, "aucune question rédigée"
    assert all(isinstance(v, str) and v.strip() for v in q.values())


def test_aucune_question_orpheline():
    """Chaque question doit correspondre à une carte existante."""
    q, cartes = charger()
    orphelines = sorted(set(q) - set(cartes))
    assert not orphelines, f"questions sans carte : {orphelines[:5]}"


def test_questions_sur_cartes_formule_seulement():
    q, cartes = charger()
    mauvais = [k for k in q if cartes[k]["type"] != "formule"]
    assert not mauvais, f"questions sur des cartes non-formule : {mauvais[:5]}"


def test_forme_interrogative():
    """Une question se termine par « ? », sauf les impératifs « Énoncez… »."""
    q, _ = charger()
    fautifs = [
        k for k, v in q.items()
        if not v.rstrip().endswith("?")
        and not re.match(r"^(Énoncez|Enoncez|Donnez|Citez|Exprimez)", v.strip())
    ]
    assert not fautifs, f"ni interrogatives ni impératives : {fautifs[:5]}"


def test_longueur_lisible_sur_telephone():
    """Au-delà de ~170 caractères, la question mange l'écran."""
    q, _ = charger()
    trop = [(k, len(v)) for k, v in q.items() if len(v) > 170]
    assert not trop, f"questions trop longues : {trop[:5]}"


def test_la_question_ne_livre_pas_sa_reponse():
    """Règle absolue du rappel actif : le recto ne contient pas la formule.

    On compare les symboles du MEMBRE DE DROITE de la formule (la réponse
    cherchée) aux symboles présents dans la question. Nommer la grandeur
    demandée est légitime ; reproduire la structure de la relation ne l'est
    pas. On détecte donc la présence d'un opérateur LaTeX de la formule dans
    la question, ce qui ne peut pas être accidentel.
    """
    q, cartes = charger()
    operateurs = re.compile(
        r"\\(frac|dfrac|sqrt|sum|int|prod|cdot|times|log|ln|exp)\b"
    )
    # Un « \cdot » dans une notation d'unité (tr·min⁻¹, A·h, W·h) n'est pas
    # une fuite : il écrit l'unité, pas la structure de la relation.
    unite = re.compile(
        r"(?:tr|min|rad|s|A|V|W|N|m|kg|h|Hz|K)\s*\$?\\cdot\$?\s*"
        r"(?:tr|min|rad|s|A|V|W|N|m|kg|h|Hz|K)"
    )

    fuites = []
    for k, question in q.items():
        latex = cartes[k].get("latex", "")
        ops_formule = set(operateurs.findall(latex))
        ops_question = set(operateurs.findall(unite.sub(" ", question)))
        communs = ops_formule & ops_question
        if communs:
            fuites.append((k, sorted(communs)))
    assert not fuites, f"la question reproduit la structure de sa formule : {fuites[:5]}"


def test_couverture_complete_des_formules():
    """Toute carte formule doit avoir sa question rédigée."""
    q, cartes = charger()
    formules = {i for i, c in cartes.items() if c["type"] == "formule"}
    sans = sorted(formules - set(q))
    assert not sans, f"{len(sans)} cartes formule sans question : {sans[:5]}"
