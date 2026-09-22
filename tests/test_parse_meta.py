import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from scripts.parse_meta import parse_meta

TEX = r"""
\input{preamble}
\ficheHeaders{T19}{AOP}{colElec}
\begin{document}
\ficheEntete{T19}{AOP (amplificateur opérationnel)}{colElec}%
  {électronique - Conditionnement du signal}%
  {\textbf{Présence :} \textbf{4/13} sujets (2013-2026) - thème \emph{régulier depuis 2019}}%
  {montages inverseur - suiveur}
\end{document}
"""

TEX_IMPLICITE = r"""
\ficheEntete{T28}{Logique combinatoire}{colElec}%
  {électronique - Logique}%
  {\textbf{Présence :} \textbf{3/13} sujets (implicite) - thème de \emph{culture}}%
  {sous-themes}
"""

def test_code_et_titre():
    m = parse_meta(TEX)
    assert m["code"] == "T19"
    assert m["titre"] == "AOP (amplificateur opérationnel)"

def test_domaine():
    assert parse_meta(TEX)["domaine"] == "électronique - Conditionnement du signal"

def test_presence():
    m = parse_meta(TEX)
    assert m["presence_n"] == 4
    assert m["presence_sur"] == 13

def test_poids_calcule():
    assert parse_meta(TEX)["poids"] == 0.308

def test_presence_implicite_parsee():
    m = parse_meta(TEX_IMPLICITE)
    assert m["presence_n"] == 3
    assert m["code"] == "T28"

TEX_ACCOLADES = r"""
\ficheEntete{T20}{Filtres RC/RL - 1\textsuperscript{er} et 2\textsuperscript{e} ordre}{colElec}%
  {électronique - Traitement analogique du signal}%
  {\textbf{Présence :} \textbf{5/13} sujets (2013-2026) - thème \emph{régulier}}%
  {sous-themes}
"""

def test_titre_avec_accolades_imbriquees():
    m = parse_meta(TEX_ACCOLADES)
    assert m["code"] == "T20"
    assert m["titre"] == "Filtres RC/RL - 1er et 2e ordre"

def test_domaine_non_decale_par_les_accolades_imbriquees():
    # Le vrai piège : un motif [^}]* renverrait un domaine vide ici.
    assert parse_meta(TEX_ACCOLADES)["domaine"] == "électronique - Traitement analogique du signal"

def test_presence_lue_malgre_les_accolades_imbriquees():
    assert parse_meta(TEX_ACCOLADES)["presence_n"] == 5

def test_aucune_commande_latex_ne_subsiste():
    for champ in ("titre", "domaine"):
        assert "\\" not in parse_meta(TEX_ACCOLADES)[champ]

def test_tex_sans_entete_leve_valueerror():
    import pytest
    with pytest.raises(ValueError):
        parse_meta(r"\documentclass{article}\begin{document}\end{document}")
