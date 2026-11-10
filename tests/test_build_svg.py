import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from scripts.build_svg import themify

SVG = """<svg xmlns='http://www.w3.org/2000/svg'>
<path fill='#000' d='M0 0'/>
<rect fill='#ffffff' stroke='#000000'/>
<path fill='none' stroke='#000'/>
</svg>"""

def test_noir_devient_currentcolor():
    out = themify(SVG)
    assert "#000" not in out
    assert "currentColor" in out

def test_blanc_devient_variable_css_avec_fallback():
    out = themify(SVG)
    assert "#ffffff" not in out
    # Le fallback est obligatoire : var(--svg-bg) nu est invalide dans un
    # <img> et repeindrait les fonds en noir, même en thème clair.
    assert "var(--svg-bg,#fff)" in out

def test_style_interne_injecte():
    out = themify(SVG)
    assert "<style>" in out
    assert "prefers-color-scheme" in out

def test_style_injecte_une_seule_fois():
    assert themify(SVG).count("<style>") == 1

def test_none_preserve():
    assert "fill='none'" in themify(SVG)

def test_hex_invalides_non_convertis():
    # #0000 et #00000 ne sont pas des couleurs valides : ne pas les toucher.
    assert "currentColor" not in themify("<svg xmlns='http://www.w3.org/2000/svg'><path fill='#0000'/></svg>")

def test_reste_xml_bien_forme():
    import xml.etree.ElementTree as ET
    ET.fromstring(themify(SVG))  # ne doit pas lever

def test_palette_terre_cuite():
    # Report de la palette de l'app publiée (capet-revision 8ba1783).
    src = "<svg xmlns='http://www.w3.org/2000/svg'><path fill='#1D4ED8' stroke='#15803d'/><path fill='#123456'/></svg>"
    out = themify(src)
    assert "var(--accent, #c0603a)" in out
    assert "var(--su, #4b7536)" in out
    assert "#123456" in out          # couleur hors palette : inchangée
    assert themify(out).count("var(--accent") == 1   # idempotent
