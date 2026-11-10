"""Compilation des environnements TikZ en SVG thémables.

Chaîne : latex -> .dvi -> dvisvgm --no-fonts -> .svg, puis substitution
des couleurs codées en dur pour que le schéma suive le thème de l'app.
"""

import pathlib
import re
import shutil
import subprocess
import tempfile

# `lmodern` est indispensable : sans lui, le texte en encodage T1 utilise les
# polices EC, que dvisvgm doit faire générer par Metafont. Quand cette
# génération échoue (constaté le 2026-11-10), dvisvgm écrit le SVG SANS les
# glyphes du texte — seules les maths restent — et ne lève aucune erreur.
# Latin Modern fournit des contours Type 1 : plus de Metafont, plus de texte perdu.
PREAMBULE = r"""\documentclass[border=3pt,dvisvgm]{standalone}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb}
\usepackage{siunitx}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{positioning,arrows.meta}
\usepackage{circuitikz}
\definecolor{colElec}{RGB}{29,78,216}
\definecolor{colAuto}{RGB}{21,128,61}
\definecolor{colMeca}{RGB}{194,65,12}
\definecolor{colTherm}{RGB}{185,28,28}
\definecolor{colInk}{RGB}{15,23,42}
\definecolor{colSlate}{RGB}{71,85,105}
\definecolor{colRule}{RGB}{203,213,225}
\begin{document}
"""

# `#0{3,6}` accepterait `#0000` et `#00000`, qui ne sont pas des couleurs
# hex valides : on n'autorise que 3 ou 6 zéros.
_NOIR = re.compile(r"(fill|stroke)=(['\"])#(?:0{3}|0{6})\2")
_BLANC = re.compile(r"(fill|stroke)=(['\"])#(?:fff|ffffff)\2", re.I)

# Palette « terre cuite et bois » de l'app publiée (capet-revision, commit
# 8ba1783 du 2026-10-13, qui demandait de reporter ici sa substitution) : les
# couleurs de domaine codées en dur deviennent des variables CSS du thème,
# toujours avec un repli. Bleus colElec -> accent ; teintes claires et gris ->
# ink-faible ; vert colAuto -> sauge (su) ; orange colMeca -> accent.
_PALETTE = {
    "#1d4ed8": "var(--accent, #c0603a)",
    "#143697": "var(--accent, #c0603a)",
    "#143797": "var(--accent, #c0603a)",
    "#839eea": "var(--ink-faible, #a89686)",
    "#8ea7ec": "var(--ink-faible, #a89686)",
    "#c0c0c0": "var(--ink-faible, #a89686)",
    "#15803d": "var(--su, #4b7536)",
    "#e8f3ec": "var(--su-fond, #e8f0df)",
    "#c2410c": "var(--accent, #c0603a)",
}
_COULEUR = re.compile(r"(fill|stroke)=(['\"])(#[0-9a-fA-F]{6})\2")


def appliquer_palette(svg: str) -> str:
    """Remplace les couleurs de domaine par les variables du thème (idempotent)."""
    return _COULEUR.sub(
        lambda m: (f"{m.group(1)}={m.group(2)}{_PALETTE[m.group(3).lower()]}{m.group(2)}"
                   if m.group(3).lower() in _PALETTE else m.group(0)),
        svg,
    )
_BALISE_SVG = re.compile(r"(<svg\b[^>]*>)")

# Feuille de style EMBARQUÉE dans le SVG. Indispensable : le SVG est chargé
# via <img>, donc c'est un document isolé que le CSS de la page ne traverse
# pas. Sans elle, `currentColor` resterait noir et `var(--svg-bg)` — sans
# valeur ni fallback — serait une déclaration invalide, peignant en noir les
# fonds de nœuds, y compris en thème clair (pire que le SVG non traité).
_STYLE = (
    "<style>"
    "svg{color:#0f172a}"
    "@media (prefers-color-scheme:dark){svg{color:#e2e8f0;--svg-bg:#1e293b}}"
    "</style>"
)


def themify(svg: str) -> str:
    """Rend le SVG sensible au thème du système.

    Le noir devient `currentColor`, le blanc `var(--svg-bg,#fff)` — toujours
    avec un fallback, jamais nu. Un `<style>` interne fournit les valeurs
    et bascule sur `prefers-color-scheme`.

    Limite connue et assumée : un `<img>` ne voit pas l'attribut
    `data-theme` de la page, donc le schéma suit le thème du SYSTÈME, pas la
    bascule manuelle de l'app. Un schéma reste toujours lisible ; il peut
    juste être en clair pendant que l'app est en sombre, si l'utilisateur a
    forcé la bascule. Corriger cela imposerait d'inliner chaque SVG par
    fetch — reporté en v2, hors périmètre.
    """
    svg = _NOIR.sub(lambda m: f"{m.group(1)}={m.group(2)}currentColor{m.group(2)}", svg)
    svg = _BLANC.sub(
        lambda m: f"{m.group(1)}={m.group(2)}var(--svg-bg,#fff){m.group(2)}", svg
    )
    svg = appliquer_palette(svg)
    return _BALISE_SVG.sub(lambda m: m.group(1) + _STYLE, svg, count=1)


def compile_tikz(code: str, env: str, dest: pathlib.Path) -> bool:
    """Compile un environnement TikZ isolé vers dest (.svg). True si succès."""
    if shutil.which("latex") is None or shutil.which("dvisvgm") is None:
        raise RuntimeError("latex et dvisvgm sont requis et introuvables dans le PATH")

    with tempfile.TemporaryDirectory() as tmp:
        tmpd = pathlib.Path(tmp)
        tex = tmpd / "s.tex"
        tex.write_text(PREAMBULE + code + "\n\\end{document}\n", encoding="utf-8")

        r = subprocess.run(
            ["latex", "-interaction=nonstopmode", "-halt-on-error", "s.tex"],
            cwd=tmpd, capture_output=True, text=True, timeout=120,
        )
        dvi = tmpd / "s.dvi"
        if r.returncode != 0 or not dvi.exists():
            return False

        r2 = subprocess.run(
            ["dvisvgm", "--no-fonts", "--exact", "--scale=1.4",
             "s.dvi", "-o", "s.svg"],
            cwd=tmpd, capture_output=True, text=True, timeout=120,
        )
        svg = tmpd / "s.svg"
        if r2.returncode != 0 or not svg.exists():
            return False

        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(themify(svg.read_text(encoding="utf-8")), encoding="utf-8")
        return True
