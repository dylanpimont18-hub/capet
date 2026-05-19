#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — Génère app/data.js à partir des fichiers Markdown du projet CAPET SII IE.
Usage : python build.py
"""

import re
import json
import os
import pathlib

ROOT = pathlib.Path(__file__).parent
DOCS = ROOT / "docs" / "CAPET_SII_IE"
OUT  = ROOT / "app" / "data.js"

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

DOMAIN_TO_THEME = {
    "thermique":              "T03",
    "thermodynamique":        "T03",
    "vapeur":                 "T03",
    "énergies renouvelables": "T13",
    "photovoltaïque":         "T13",
    "stockage":               "T12",
    "batteries":              "T12",
    "électrotechnique":       "T02",
    "puissance & réseaux":    "T02",
    "câblage":                "T14",
    "distribution":           "T14",
    "hacheurs":               "T05",
    "convertisseurs dc":      "T05",
    "redresseurs":            "T06",
    "onduleurs":              "T07",
    "mcc":                    "T08",
    "courant continu":        "T08",
    "machine synchrone":      "T09",
    "synchrone":              "T09",
    "mas":                    "T10",
    "asynchrone":             "T10",
    "machines électriques":   "T11",
    "automatique":            "T24",
    "asservissement":         "T24",
    "cinématique":            "T30",
    "rdm":                    "T30",
    "mécanique":              "T30",
    "modélisation":           "T21",
    "capteurs":               "T20",
    "mesure":                 "T20",
    "éclairage":              "T16",
    "fluides":                "T18",
    "hydraulique":            "T18",
    "sécurité":               "T15",
    "régimes de neutre":      "T15",
    "électronique":           "T26",
    "amplificateur":          "T26",
    "signaux":                "T25",
    "algorithmique":          "T28",
    "programmation":          "T28",
    "communication":          "T29",
    "bus industriel":         "T29",
}

FICHE_THEMES = {
    "T01","T02","T03","T04","T05","T06","T07","T08","T09","T10",
    "T11","T12","T13","T14","T15","T16","T17","T18","T19","T20",
    "T21","T22","T23","T24","T25","T26","T27","T28","T29","T30",
}

_F = "docs/CAPET_SII_IE/04_Fiches_Themes/"
FICHE_PATHS = {
    "T01": _F + "T01_electrotechnique_bases.md",
    "T02": _F + "T02_puissance_AC.md",
    "T03": _F + "T03_thermique.md",
    "T04": _F + "T04_transformateurs.md",
    "T05": _F + "T05_hacheurs.md",
    "T06": _F + "T06_redresseurs.md",
    "T07": _F + "T07_onduleurs.md",
    "T08": _F + "T08_mcc.md",
    "T09": _F + "T09_machine_synchrone.md",
    "T10": _F + "T10_mas.md",
    "T11": _F + "T11_variation_vitesse.md",
    "T12": _F + "T12_stockage_energie.md",
    "T13": _F + "T13_energies_renouvelables.md",
    "T14": _F + "T14_distribution.md",
    "T15": _F + "T15_securite_electrique.md",
    "T16": _F + "T16_eclairage.md",
    "T17": _F + "T17_froid_climatisation.md",
    "T18": _F + "T18_fluides.md",
    "T19": _F + "T19_automatique_systemes.md",
    "T20": _F + "T20_capteurs_mesure.md",
    "T21": _F + "T21_modelisation.md",
    "T22": _F + "T22_simulation.md",
    "T23": _F + "T23_analyse_systeme.md",
    "T24": _F + "T24_correcteurs.md",
    "T25": _F + "T25_signaux.md",
    "T26": _F + "T26_electronique.md",
    "T27": _F + "T27_materiaux.md",
    "T28": _F + "T28_programmation.md",
    "T29": _F + "T29_communication.md",
    "T30": _F + "T30_mecanique.md",
}

EMOJI_TO_INTENSITE = {
    "🔴": "rouge",
    "🟠": "orange",
    "🟡": "jaune",
}

INTENSITE_ORDRE = {"rouge": 3, "orange": 2, "jaune": 1, "absent": 0}

TROU_CANDIDATES = [
    (r"\\sqrt\{3\}",    r"\sqrt{3}",     [r"\sqrt{2}", r"3", r"2\pi", r"\sqrt{3}/2"]),
    (r"\\cos\\varphi",  r"\cos\varphi",  [r"\sin\varphi", r"\tan\varphi", r"\varphi", r"\cos^2\varphi"]),
    (r"\\eta",          r"\eta",         [r"\varphi", r"\alpha", r"\omega", r"g"]),
    (r"\\omega",        r"\omega",       [r"\Omega", r"2\pi f", r"\omega_0", r"p"]),
    (r"\balpha\b",      r"\alpha",       [r"\beta", r"\eta", r"1-\alpha", r"\omega"]),
    (r"\bg\b",          r"g",            [r"1-g", r"g^2", r"N_s", r"\omega_s"]),
    (r"\\tau",          r"\tau",         [r"L/R", r"RC", r"T/2", r"1/\omega_c"]),
    (r"\\Delta T",      r"\Delta T",     [r"\Delta P", r"T_j - T_a", r"T_1 - T_2", r"\theta_{max}"]),
    (r"\\lambda",       r"\lambda",      [r"\mu", r"\sigma", r"k", r"\rho"]),
    (r"\\frac\{1\}\{2\}", r"\frac{1}{2}", [r"\frac{1}{3}", r"2", r"\frac{\pi}{2}", r"\frac{1}{4}"]),
    (r"\\sin\\varphi",  r"\sin\varphi",  [r"\cos\varphi", r"\tan\varphi", r"1-\cos\varphi", r"\varphi"]),
    (r"\\pi",           r"\pi",          [r"2\pi", r"\pi/2", r"\pi/4", r"180"]),
]

# ---------------------------------------------------------------------------
# Parsing formulaire_capet.md
# ---------------------------------------------------------------------------

def section_to_theme(title: str) -> str:
    t = title.lower()
    for keyword, theme_id in DOMAIN_TO_THEME.items():
        if keyword in t:
            return theme_id
    return "T01"


def extract_latex(cell: str) -> str | None:
    """Extrait le contenu LaTeX entre $ ... $ (le premier match)."""
    m = re.search(r'\$(.*?)\$', cell, re.DOTALL)
    if m:
        return m.group(1).strip()
    return None


def build_trou(latex: str) -> dict | None:
    for pattern, term, distractors in TROU_CANDIDATES:
        if re.search(pattern, latex):
            masked = re.sub(pattern, r"\\\\square", latex, count=1)
            return {
                "maskedTerm": term,
                "maskedLatex": masked,
                "choices": [term] + distractors[:3],
            }
    return None


def parse_formulaire(path: pathlib.Path) -> list:
    text = path.read_text(encoding="utf-8")
    formules = []
    current_section = "Général"
    current_theme = "T01"
    fid = 0

    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        # Nouveau header de section (## ou ###)
        m = re.match(r'^#{2,3}\s+(.+)', line)
        if m:
            current_section = m.group(1).strip()
            current_theme = section_to_theme(current_section)
            i += 1
            continue

        # Ligne de tableau : | ... | ... | ... | ... |
        # Ignorer lignes d'en-tête et séparateurs
        if line.strip().startswith('|') and '---' not in line:
            cells = [c.strip() for c in line.split('|')]
            cells = [c for c in cells if c != '']  # retirer vide en début/fin
            if len(cells) >= 4:
                latex_raw = cells[0]
                description = cells[1]
                donnee_cell = cells[2]
                freq_cell = cells[3]

                latex = extract_latex(latex_raw)
                if latex is None:
                    i += 1
                    continue

                # Ignorer les lignes d'en-tête (Formule / Description / etc.)
                if description.lower() in ("description", "domaine", "donnée ?", "fréq.", "formule"):
                    i += 1
                    continue

                donnee = "✅" in donnee_cell
                freq_match = re.search(r'\d+', freq_cell)
                frequence = int(freq_match.group()) if freq_match else 0

                fid += 1
                fid_str = f"f{fid:03d}"

                trou = build_trou(latex)

                formules.append({
                    "id": fid_str,
                    "themeId": current_theme,
                    "domaine": current_section,
                    "latex": latex,
                    "description": description,
                    "donnee": donnee,
                    "frequence": frequence,
                    "trou": trou,
                })

        i += 1

    return formules


# ---------------------------------------------------------------------------
# Parsing tableau_themes_capet.md
# ---------------------------------------------------------------------------

def parse_themes(path: pathlib.Path) -> list:
    text = path.read_text(encoding="utf-8")

    # S'arrêter avant "## Tableau de présence"
    stop_match = re.search(r'^## Tableau de pr[eé]sence', text, re.MULTILINE)
    if stop_match:
        text = text[:stop_match.start()]

    lines = text.splitlines()

    # Trouver la ligne d'en-tête du tableau (contient "2015 E1")
    header_idx = None
    for idx, line in enumerate(lines):
        if "2015 E1" in line or "2015 E2" in line:
            header_idx = idx
            break

    if header_idx is None:
        print("⚠️  En-tête du tableau non trouvé dans tableau_themes_capet.md")
        return []

    # Parser les colonnes de l'en-tête
    header_cells = [c.strip() for c in lines[header_idx].split('|')]
    header_cells = [c for c in header_cells if c != '']
    # header_cells[0] = "Thème", header_cells[1:] = "2015 E1", "2015 E2", ...
    # Ignorer la dernière colonne "Moy." ou "**Moy.**"
    col_names = header_cells[1:]  # liste des colonnes

    # Filtrer : garder seulement les colonnes qui matchent "\d{4} E[12]"
    col_indices = []  # (col_name_normalized, original_index_in_cells)
    for j, cn in enumerate(col_names):
        clean = re.sub(r'\*+', '', cn).strip()
        if re.match(r'\d{4}\s*E[12]', clean):
            col_key = clean.replace(' ', '_')
            col_indices.append((col_key, j + 1))  # +1 car on a skippé la colonne Thème

    themes = []
    for line in lines[header_idx + 2:]:  # +2 pour sauter la ligne de séparation
        if not line.strip().startswith('|'):
            continue
        if '---' in line:
            continue

        # Conserver les cellules vides pour préserver les positions de colonnes
        raw_cells = line.split('|')
        # Retirer le premier et dernier élément (vides dus aux | en début/fin)
        if len(raw_cells) >= 2:
            raw_cells = raw_cells[1:-1]
        cells_stripped = [c.strip() for c in raw_cells]
        
        if not cells_stripped:
            continue

        theme_cell = cells_stripped[0] if cells_stripped else ''
        # Réaffecter cells pour le reste du code (version sans vides pour compatibilité)
        cells = cells_stripped  # maintenant on garde les vides aussi
        # Extraire l'id (T01, T02, ...) et le nom
        m = re.match(r'(T\d{2})\s*[–—-]\s*(.+)', theme_cell)
        if not m:
            continue

        theme_id = m.group(1)
        nom = m.group(2).strip()

        # Parser les présences
        presences = {}
        max_intensite = "absent"
        for col_key, col_j in col_indices:
            if col_j < len(cells_stripped):
                cell_val = cells_stripped[col_j]
                intensite = None
                for emoji, val in EMOJI_TO_INTENSITE.items():
                    if emoji in cell_val:
                        intensite = val
                        break
                if intensite:
                    presences[col_key] = intensite
                    if INTENSITE_ORDRE.get(intensite, 0) > INTENSITE_ORDRE.get(max_intensite, 0):
                        max_intensite = intensite

        has_fiche = theme_id in FICHE_THEMES
        fiche_path = FICHE_PATHS.get(theme_id, None)

        themes.append({
            "id": theme_id,
            "nom": nom,
            "intensite": max_intensite,
            "presences": presences,
            "hasFiche": has_fiche,
            "fichePath": fiche_path,
        })

    # Trier par id
    themes.sort(key=lambda t: t["id"])
    return themes


# ---------------------------------------------------------------------------
# Parsing points_aveugles.md
# ---------------------------------------------------------------------------

def parse_points_aveugles(path: pathlib.Path) -> list:
    text = path.read_text(encoding="utf-8")
    items = []

    lines = text.splitlines()
    i = 0
    current_title = None
    current_detail = []

    while i < len(lines) and len(items) < 10:
        line = lines[i].strip()

        # Headers ### = un point aveugle
        m3 = re.match(r'^###\s+(.+)', line)
        if m3:
            # Sauvegarder le précédent
            if current_title:
                items.append({
                    "texte": current_title,
                    "detail": ' '.join(current_detail).strip() or current_title,
                    "source": "Rapports jury 2019–2025",
                })
            current_title = m3.group(1).strip()
            current_detail = []
            i += 1
            continue

        # Headers ## = nouvelle section, réinitialiser
        m2 = re.match(r'^##\s+(.+)', line)
        if m2:
            if current_title:
                items.append({
                    "texte": current_title,
                    "detail": ' '.join(current_detail).strip() or current_title,
                    "source": "Rapports jury 2019–2025",
                })
            current_title = None
            current_detail = []
            i += 1
            continue

        # Ligne de signal jury
        if current_title and line.startswith('- **Signal jury'):
            detail_m = re.match(r'^-\s+\*\*Signal jury.*?\*\*\s*[:\s]\s*["«]?(.+)', line)
            if detail_m:
                current_detail.append(detail_m.group(1).strip().rstrip('"».'))

        # Bullet simple  - **truc** : détail
        bm = re.match(r'^-\s+\*\*(.+?)\*\*\s*[:\—–-]\s*(.+)', line)
        if bm and not current_title:
            items.append({
                "texte": bm.group(1).strip(),
                "detail": bm.group(2).strip(),
                "source": "Rapports jury 2019–2025",
            })

        i += 1

    # Dernier item en cours
    if current_title and len(items) < 10:
        items.append({
            "texte": current_title,
            "detail": ' '.join(current_detail).strip() or current_title,
            "source": "Rapports jury 2019–2025",
        })

    return items[:10]


# ---------------------------------------------------------------------------
# Scanning des sujets
# ---------------------------------------------------------------------------

def parse_sujets(sujets_dir: pathlib.Path) -> list:
    sujets = []
    for md_file in sorted(sujets_dir.rglob("*.md")):
        # Exclure les meta.json et les fiches
        parts = md_file.parts

        # Extraire l'année depuis le chemin
        annee = None
        for part in parts:
            m = re.match(r'^(\d{4})$', part)
            if m:
                annee = int(m.group(1))
                break
        if annee is None:
            continue

        # Déterminer epreuve
        name = md_file.name
        parent_name = md_file.parent.name
        if "Epreuve1" in name or "Epreuve1" in parent_name:
            epreuve = "E1"
        elif "Epreuve2" in name or "Epreuve2" in parent_name:
            epreuve = "E2"
        else:
            epreuve = "E1"

        # Titre = nom du dossier parent
        titre = f"{annee} {parent_name.replace('_', ' ')}"

        # Chemin relatif POSIX depuis la racine
        rel_path = md_file.relative_to(ROOT).as_posix()

        sujets.append({
            "annee": annee,
            "epreuve": epreuve,
            "titre": titre,
            "path": rel_path,
            "themes": [],  # rempli après
        })

    return sujets


def fill_sujet_themes(sujets: list, themes: list) -> None:
    """Rempli le champ themes[] de chaque sujet à partir des presences."""
    for sujet in sujets:
        annee = sujet["annee"]
        epreuve = sujet["epreuve"]
        col_key = f"{annee}_{epreuve}"
        theme_ids = []
        for t in themes:
            if col_key in t["presences"]:
                theme_ids.append(t["id"])
        sujet["themes"] = theme_ids


# ---------------------------------------------------------------------------
# Génération de app/data.js
# ---------------------------------------------------------------------------

def to_js(obj) -> str:
    """Sérialise un objet Python en JS (JSON-compatible)."""
    return json.dumps(obj, ensure_ascii=False, indent=2)


def generate_data_js(themes, formules, sujets, points_aveugles) -> str:
    lines = [
        "// Généré par build.py — ne pas modifier manuellement",
        "window.DATA = {",
        f"  themes: {to_js(themes)},",
        f"  formules: {to_js(formules)},",
        f"  sujets: {to_js(sujets)},",
        f"  pointsAveugles: {to_js(points_aveugles)},",
        '  dateEpreuve: "2026-06-01"',
        "};",
    ]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Créer le répertoire app/ si nécessaire
    app_dir = ROOT / "app"
    app_dir.mkdir(exist_ok=True)

    print("📂 Lecture des fichiers sources…")

    # Thèmes
    themes_path = DOCS / "tableau_themes_capet.md"
    if not themes_path.exists():
        print(f"❌ Fichier non trouvé : {themes_path}")
        return
    themes = parse_themes(themes_path)
    print(f"   Thèmes : {len(themes)}")

    # Formules
    formulaire_path = DOCS / "formulaire_capet.md"
    if not formulaire_path.exists():
        print(f"❌ Fichier non trouvé : {formulaire_path}")
        return
    formules = parse_formulaire(formulaire_path)
    print(f"   Formules : {len(formules)}")

    # Points aveugles
    pa_path = DOCS / "points_aveugles.md"
    points_aveugles = []
    if pa_path.exists():
        points_aveugles = parse_points_aveugles(pa_path)
    print(f"   Points aveugles : {len(points_aveugles)}")

    # Sujets
    sujets_dir = DOCS / "01_Sujets"
    sujets = []
    if sujets_dir.exists():
        sujets = parse_sujets(sujets_dir)
        fill_sujet_themes(sujets, themes)
    print(f"   Sujets : {len(sujets)}")

    # Écrire data.js
    js_content = generate_data_js(themes, formules, sujets, points_aveugles)
    OUT.write_text(js_content, encoding="utf-8")

    print(f"\n✅ app/data.js — {len(themes)} thèmes, {len(formules)} formules, {len(sujets)} sujets")


if __name__ == "__main__":
    main()
