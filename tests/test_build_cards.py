import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from scripts.build_cards import assembler, faire_id

def test_id_format():
    assert faire_id("T19", "formule", 3) == "T19-f-003"
    assert faire_id("T02", "piege", 12) == "T02-p-012"
    assert faire_id("T30", "schema", 1) == "T30-s-001"

def test_assembler_produit_la_structure():
    themes = [{"code": "T19", "titre": "AOP", "domaine": "élec",
               "poids": 0.3, "presence_n": 4, "presence_sur": 13}]
    cartes = [{"type": "formule", "theme": "T19", "label": "x",
               "latex": "a=b", "unites": "", "conditions": ""}]
    out = assembler(themes, cartes)
    assert out["version"] == 1
    assert out["themes"][0]["code"] == "T19"
    assert out["cards"][0]["id"] == "T19-f-001"

def test_poids_propage_depuis_le_theme():
    themes = [{"code": "T19", "titre": "AOP", "domaine": "élec",
               "poids": 0.308, "presence_n": 4, "presence_sur": 13}]
    cartes = [{"type": "piege", "theme": "T19", "titre": "t",
               "piege": "p", "regle": "r", "erreur_type": ""}]
    out = assembler(themes, cartes)
    assert out["cards"][0]["poids"] == 0.308

def test_ids_uniques():
    themes = [{"code": "T19", "titre": "AOP", "domaine": "e",
               "poids": 0.3, "presence_n": 4, "presence_sur": 13}]
    cartes = [{"type": "formule", "theme": "T19", "label": f"f{i}",
               "latex": "x", "unites": "", "conditions": ""} for i in range(5)]
    ids = [c["id"] for c in assembler(themes, cartes)["cards"]]
    assert len(ids) == len(set(ids))

def test_poids_affine_par_la_frequence():
    from scripts.build_cards import _poids_final
    assert _poids_final(1.0, "") == 1.0
    assert _poids_final(1.0, "Très fréquent") == 1.2
    assert _poids_final(1.0, "Systématique") == 1.3
    assert _poids_final(1.0, "Présent") == 0.9

def test_poids_accepte_les_accords_feminins():
    from scripts.build_cards import _poids_final
    assert _poids_final(1.0, "Fréquente") == 1.1
    assert _poids_final(1.0, "Très fréquente (donnée ou calculée)") == 1.2

def test_frequence_inconnue_laisse_le_poids_intact():
    from scripts.build_cards import _poids_final
    assert _poids_final(0.5, "2017 (réchauffeur 3 kW)") == 0.5

def test_carte_de_theme_inconnu_est_rejetee():
    import pytest
    with pytest.raises(ValueError, match="T99"):
        assembler([{"code": "T19", "titre": "A", "domaine": "e", "poids": 0.3,
                    "presence_n": 4, "presence_sur": 13}],
                  [{"type": "formule", "theme": "T99", "label": "x",
                    "latex": "y", "unites": "", "conditions": ""}])
