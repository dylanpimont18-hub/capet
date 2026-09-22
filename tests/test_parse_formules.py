import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from scripts.parse_formules import parse_table_formulas

# Schéma A : formule en colonne 2 (T01, T02...)
SECTION_A = """## 1. FORMULES ET COURS

| Grandeur / Loi | Formule | Unité |
|----------------|---------|-------|
| Loi d'Ohm (résistif) | $u = R \\cdot i$ | V, Ω, A |
| Diviseur de tension | $V_s = V_e \\cdot \\dfrac{R_B}{R_A + R_B}$ | V |
| Facteur de puissance | $\\cos\\varphi = P / S$ | — |
"""

# Schéma B : formule en colonne 1 (T06 à T13)
SECTION_B = """## 1. FORMULES ET COURS

| Formule LaTeX | Contexte | Fréquence | Source |
|---------------|----------|-----------|--------|
| $\\bar{U} = \\dfrac{2\\sqrt{2}V}{\\pi}$ | Redresseur PD2 | Très fréquent | 2019 |
| $P = U \\cdot I$ | Puissance continue | Systématique | 2021 |
"""

# Tableau qui n'est pas un tableau de formules : doit être ignoré
SECTION_C = """## 1. FORMULES ET COURS

| Technologie | Tension nominale | Énergie massique |
|-------------|------------------|------------------|
| Li-ion | $3{,}7$ V | 150 W·h/kg |
"""

def test_schema_A_extrait_trois_formules():
    assert len(parse_table_formulas(SECTION_A, "T01")) == 3

def test_schema_A_champs():
    c = parse_table_formulas(SECTION_A, "T01")[0]
    assert c["type"] == "formule"
    assert c["theme"] == "T01"
    assert c["label"] == "Loi d'Ohm (résistif)"
    assert c["latex"] == r"u = R \cdot i"
    assert c["unites"] == "V, Ω, A"
    assert c["source_format"] == "table"

def test_schema_B_formule_en_colonne_1():
    cards = parse_table_formulas(SECTION_B, "T08")
    assert len(cards) == 2
    assert cards[0]["latex"] == r"\bar{U} = \dfrac{2\sqrt{2}V}{\pi}"

def test_schema_B_label_depuis_contexte():
    c = parse_table_formulas(SECTION_B, "T08")[0]
    assert c["label"] == "Redresseur PD2"

def test_schema_B_frequence_capturee():
    c = parse_table_formulas(SECTION_B, "T08")[0]
    assert c["frequence"] == "Très fréquent"

def test_schema_B_sans_colonne_unite():
    assert parse_table_formulas(SECTION_B, "T08")[0]["unites"] == ""

def test_tableau_sans_colonne_formule_ignore():
    assert parse_table_formulas(SECTION_C, "T15") == []

def test_ignore_la_ligne_de_separation():
    assert all("---" not in c["label"] for c in parse_table_formulas(SECTION_A, "T01"))

def test_unite_tiret_cadratin_devient_vide():
    assert parse_table_formulas(SECTION_A, "T01")[2]["unites"] == ""

def test_delimiteurs_math_retires():
    for c in parse_table_formulas(SECTION_A, "T01") + parse_table_formulas(SECTION_B, "T08"):
        assert not c["latex"].startswith("$")
        assert not c["latex"].endswith("$")

def test_frequence_absente_vaut_chaine_vide():
    assert parse_table_formulas(SECTION_A, "T01")[0]["frequence"] == ""

# Cas réel T03 : les barres du module |Z| ne sont pas des séparateurs
SECTION_PIPE = """## 1. FORMULES ET COURS

| Grandeur / Loi | Formule | Unité |
|----------------|---------|-------|
| Module impédance RC | $|\\underline{Z}| = \\sqrt{R^2 + (1/C\\omega)^2}$ | Ω |
| Gain Bode | $G_{dB} = 20\\log_{10}|H(j\\omega)|$ | dB |
"""

def test_barres_dans_les_maths_ne_cassent_pas_les_colonnes():
    cards = parse_table_formulas(SECTION_PIPE, "T03")
    assert len(cards) == 2
    assert cards[0]["label"] == "Module impédance RC"
    assert cards[0]["unites"] == "Ω"

def test_module_conserve_ses_barres():
    c = parse_table_formulas(SECTION_PIPE, "T03")[0]
    assert c["latex"].startswith(r"|\underline{Z}|")
    assert c["latex"] != "$"

def test_cellule_a_segments_math_multiples_non_tronquee():
    from scripts.parse_formules import _strip_math
    s = r"$R = U^2/P$ (charge purement résistive)"
    assert _strip_math(s) == s
