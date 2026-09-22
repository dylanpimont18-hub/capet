import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from scripts.parse_pieges import parse_pieges

FICHE_A = r"""# T02 — Puissance

## 1. FORMULES ET COURS
| a | $b$ | c |

## 5. LACUNES ET PIÈGES RÉCURRENTS

### 5.1 Confusion entre $F_P$ et $\cos\varphi$

**Le piège** : Confondre le facteur de puissance et le facteur de déplacement.

**La distinction** :
- Si le signal est purement sinusoïdal : $F_P = \cos\varphi$.

**Erreur type** : Dans le sujet 2018, des candidats confondaient les colonnes.

### 5.2 Oubli du rendement

**Le piège** : Calculer sans diviser par le rendement.

**Correction** : La formule correcte inclut $\eta$ au dénominateur.

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

Rien ici.
"""

FICHE_B = r"""# T01

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Signe dans la loi des mailles** : oublier de changer le signe d'une tension. Toujours définir un sens de parcours avant d'écrire.

2. **Valeur efficace vs crête** : $V_{eff} = V_{max}/\sqrt{2}$ seulement pour un sinusoïdal pur.

## 6. CONNEXIONS
Rien.
"""

FICHE_C = r"""# T19

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **Appliquer $V_+ = V_-$ sans vérifier la contre-réaction** : en mode comparateur, cette égalité est fausse. Vérifier le bouclage avant tout calcul.
- **Signe du gain inverseur** : oublier le signe négatif.

## 6. CONNEXIONS
Rien.
"""

# --- Format A : sous-titres ### ---

def test_A_extrait_deux_pieges():
    assert len(parse_pieges(FICHE_A, "T02")) == 2

def test_A_titre_sans_numerotation():
    p = parse_pieges(FICHE_A, "T02")[0]
    assert p["titre"].startswith("Confusion entre")
    assert not p["titre"].startswith("5.1")

def test_A_champ_piege():
    assert "Confondre le facteur" in parse_pieges(FICHE_A, "T02")[0]["piege"]

def test_A_regle_depuis_la_distinction():
    assert "purement sinusoïdal" in parse_pieges(FICHE_A, "T02")[0]["regle"]

def test_A_regle_depuis_correction():
    assert "dénominateur" in parse_pieges(FICHE_A, "T02")[1]["regle"]

def test_A_erreur_type():
    assert "sujet 2018" in parse_pieges(FICHE_A, "T02")[0]["erreur_type"]

# --- Format B : liste numérotée ---

def test_B_extrait_deux_pieges():
    assert len(parse_pieges(FICHE_B, "T01")) == 2

def test_B_titre_depuis_le_gras():
    assert parse_pieges(FICHE_B, "T01")[0]["titre"] == "Signe dans la loi des mailles"

def test_B_piege_est_la_premiere_phrase():
    p = parse_pieges(FICHE_B, "T01")[0]
    assert "oublier de changer le signe" in p["piege"]
    assert "Toujours définir" not in p["piege"]

def test_B_regle_est_le_reste():
    assert "Toujours définir un sens" in parse_pieges(FICHE_B, "T01")[0]["regle"]

def test_B_corps_monophrase_laisse_regle_vide():
    assert parse_pieges(FICHE_B, "T01")[1]["regle"] == ""

# --- Format C : liste à puces ---

def test_C_extrait_deux_pieges():
    assert len(parse_pieges(FICHE_C, "T19")) == 2

def test_C_titre_avec_latex_conserve():
    assert "$V_+ = V_-$" in parse_pieges(FICHE_C, "T19")[0]["titre"]

def test_C_decoupage_piege_regle():
    p = parse_pieges(FICHE_C, "T19")[0]
    assert "égalité est fausse" in p["piege"]
    assert "Vérifier le bouclage" in p["regle"]

# --- Communs ---

def test_section_6_non_capturee():
    for p in parse_pieges(FICHE_A, "T02") + parse_pieges(FICHE_B, "T01"):
        assert "Rien" not in p["regle"] and "Rien" not in p["piege"]

def test_type_et_theme():
    p = parse_pieges(FICHE_A, "T02")[0]
    assert p["type"] == "piege" and p["theme"] == "T02"

def test_fiche_sans_section_5_renvoie_liste_vide():
    assert parse_pieges("# T99\n\n## 1. FORMULES\n\nrien\n", "T99") == []

def test_tous_les_pieges_ont_un_titre_non_vide():
    for f, t in ((FICHE_A, "T02"), (FICHE_B, "T01"), (FICHE_C, "T19")):
        for p in parse_pieges(f, t):
            assert p["titre"].strip()
