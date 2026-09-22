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

from scripts.parse_formules import parse_block_formulas

BLOCS = r"""## 1. FORMULES ET COURS

### 1.2 Montage inverseur
$$\frac{V_s}{V_e} = -\frac{R_2}{R_1}$$

Gain en tension : inversion de phase.

### 1.5 Montage soustracteur
$$V_s = \frac{R_2}{R_1}(V_2 - V_1)$$

Valable si les quatre résistances sont appariées.

Utilisé pour un capteur de température.
"""

def test_extrait_deux_blocs():
    assert len(parse_block_formulas(BLOCS, "T19")) == 2

def test_label_vient_du_heading_sans_numerotation():
    c = parse_block_formulas(BLOCS, "T19")[0]
    assert c["label"] == "Montage inverseur"
    assert c["source_format"] == "bloc"

def test_latex_sans_delimiteurs():
    c = parse_block_formulas(BLOCS, "T19")[0]
    assert c["latex"] == r"\frac{V_s}{V_e} = -\frac{R_2}{R_1}"

def test_condition_capturee_quand_marqueur_present():
    c = parse_block_formulas(BLOCS, "T19")[1]
    assert "quatre résistances sont appariées" in c["conditions"]

def test_prose_descriptive_ignoree():
    # Cas réel T19 : « Utilisé pour amplifier… issue d'un capteur de
    # température » NE doit pas être capturé. C'est précisément la raison
    # pour laquelle « pour » est absent des marqueurs.
    c = parse_block_formulas(BLOCS, "T19")[1]
    assert "capteur de température" not in c["conditions"]

PROSE_POUR = """## 1. FORMULES ET COURS

### 1.5 Montage soustracteur
$$V_s = R_2 (V_2 - V_1)$$

Utilisé pour amplifier une tension différentielle issue d'un capteur de température.
"""

def test_le_marqueur_pour_ne_capture_rien():
    assert parse_block_formulas(PROSE_POUR, "T19")[0]["conditions"] == ""

AMORCE = r"""## 1. FORMULES ET COURS

### 1.1 AOP idéal
$$\varepsilon = 0$$

Un AOP parfait en régime linéaire vérifie les trois hypothèses :
"""

def test_amorce_de_paragraphe_rejetee():
    # Se termine par « : » : c'est une introduction, pas une condition.
    assert parse_block_formulas(AMORCE, "T19")[0]["conditions"] == ""

METADONNEE = """## 1. FORMULES ET COURS

### 1.2 Énergie
$$E = P t$$

Source : E2_Sujet_2021 (Q5) : « déterminer l'énergie lorsque le niveau est bas ».
"""

def test_ligne_de_source_rejetee():
    assert parse_block_formulas(METADONNEE, "T19")[0]["conditions"] == ""

def test_bloc_sans_condition_a_conditions_vide():
    c = parse_block_formulas(BLOCS, "T19")[0]
    assert c["conditions"] == ""

GRAS = r"""## 1. FORMULES ET COURS

### 1.1 AOP idéal
$$\varepsilon = 0$$

**Condition de fonctionnement linéaire :** la sortie est rebouclée sur l'entrée.
"""

def test_marques_de_gras_retirees_des_conditions():
    c = parse_block_formulas(GRAS, "T19")[0]
    assert "**" not in c["conditions"]
    assert "rebouclée" in c["conditions"]

def test_frequence_vide_pour_les_blocs():
    assert parse_block_formulas(BLOCS, "T19")[0]["frequence"] == ""
