# tests/test_extract_tikz.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from scripts.extract_tikz import extract_tikz_envs

TEX = r"""
\begin{document}
Du texte.
\begin{tikzpicture}[scale=0.9]
  \draw (0,0) -- (1,1);
\end{tikzpicture}
Encore du texte.
\begin{circuitikz}[european]
  \draw (0,0) to[R, l=$R_1$] (2,0);
\end{circuitikz}
\end{document}
"""

def test_extrait_deux_environnements():
    assert len(extract_tikz_envs(TEX)) == 2

def test_types_environnements():
    envs = extract_tikz_envs(TEX)
    assert envs[0]["env"] == "tikzpicture"
    assert envs[1]["env"] == "circuitikz"

def test_code_contient_les_delimiteurs():
    e = extract_tikz_envs(TEX)[0]
    assert e["code"].startswith(r"\begin{tikzpicture}")
    assert e["code"].endswith(r"\end{tikzpicture}")

def test_hash_stable_et_court():
    a = extract_tikz_envs(TEX)[0]["hash"]
    b = extract_tikz_envs(TEX)[0]["hash"]
    assert a == b
    assert len(a) == 12

def test_hash_differe_entre_schemas():
    envs = extract_tikz_envs(TEX)
    assert envs[0]["hash"] != envs[1]["hash"]

def test_aucun_environnement_renvoie_liste_vide():
    assert extract_tikz_envs(r"\begin{document}rien\end{document}") == []
