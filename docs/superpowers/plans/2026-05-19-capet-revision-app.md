# CAPET Révision App — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construire une SPA statique (GitHub Pages) de révision CAPET SII IE avec accueil intelligent, 30 thèmes, ~130 formules, quiz QCM + texte à trous, et suivi de progression en localStorage.

**Architecture:** SPA Vanilla JS avec hash routing. Un script Python `build.py` lit les fichiers Markdown existants et génère `app/data.js`. L'app charge `data.js` au démarrage et navigue entre 5 vues via `window.location.hash`.

**Tech Stack:** HTML5, CSS3, Vanilla JS (ES6+), KaTeX 0.16 (CDN), Python 3 (build only)

---

## Structure des fichiers

```
/
├── index.html              # Shell SPA : nav, #app, KaTeX CDN, imports
├── app/
│   ├── data.js             # window.DATA — généré par build.py, commité
│   ├── router.js           # Hash routing — mappe #/vue/:param → renderView()
│   ├── storage.js          # get/setFormuleProgress, getThemeProgress, reset
│   ├── katex-render.js     # Utilitaire renderMath(el) via KaTeX
│   ├── views/
│   │   ├── accueil.js      # Suggestion prioritaire, points aveugles, stats
│   │   ├── themes.js       # Liste filtrée des 30 thèmes
│   │   ├── theme.js        # Vue thème : onglets Fiche/Formules/Quiz/Sujets
│   │   ├── formulaire.js   # Toutes les formules, filtres, quiz transversal
│   │   └── progression.js  # Grille 30 thèmes, totaux, reset
│   ├── quiz/
│   │   ├── qcm.js          # Moteur QCM : tirage, feedback, résultat
│   │   └── trous.js        # Moteur texte à trous : masquage, jetons, résultat
│   └── style.css
├── build.py                # MD → app/data.js (Python 3 stdlib)
└── docs/                   # Sources Markdown (existantes, non modifiées)
```

---

## Task 1 : build.py — Générer app/data.js

**Files :**
- Create : `build.py`
- Create : `app/data.js` (généré, commité)

### Contexte

`build.py` parse quatre sources :
1. `docs/CAPET_SII_IE/formulaire_capet.md` → `DATA.formules[]`
2. `docs/CAPET_SII_IE/tableau_themes_capet.md` → `DATA.themes[]`
3. `docs/CAPET_SII_IE/points_aveugles.md` → `DATA.pointsAveugles[]`
4. `docs/CAPET_SII_IE/01_Sujets/**` → `DATA.sujets[]`

- [ ] **Étape 1.1 : Créer build.py — mapping domaine → thème**

```python
#!/usr/bin/env python3
"""
build.py — Génère app/data.js depuis les fichiers Markdown CAPET.
Usage : python build.py
"""
import re, json, os, glob
from pathlib import Path

ROOT = Path(__file__).parent
DOCS = ROOT / "docs" / "CAPET_SII_IE"
OUT  = ROOT / "app" / "data.js"

# Mapping section formulaire → themeId
DOMAIN_TO_THEME = {
    "thermique": "T03",
    "thermodynamique": "T03",
    "énergies renouvelables": "T13",
    "stockage": "T12",
    "électrotechnique": "T02",
    "câblage": "T14",
    "distribution": "T14",
    "hacheurs": "T05",
    "convertisseurs": "T05",
    "mas": "T10",
    "asynchrone": "T10",
    "machines électriques": "T11",
    "automatique": "T24",
    "asservissement": "T24",
    "cinématique": "T30",
    "rdm": "T30",
    "mécanique": "T30",
    "modélisation": "T21",
}

def domain_to_theme(section_title: str) -> str:
    t = section_title.lower()
    for key, tid in DOMAIN_TO_THEME.items():
        if key in t:
            return tid
    return "T01"  # fallback
```

- [ ] **Étape 1.2 : Parser formulaire_capet.md**

```python
def parse_formules(md_path: Path) -> list[dict]:
    """Parse les tables Markdown du formulaire — renvoie liste de dicts."""
    text = md_path.read_text(encoding="utf-8")
    formules = []
    current_section = ""
    fid = 0

    for line in text.splitlines():
        # Détecter les headers de section (## N. Titre)
        m = re.match(r"^##\s+\d+\.\s+(.+)", line)
        if m:
            current_section = m.group(1).strip()
            continue

        # Détecter les lignes de table (| $latex$ | desc | ✅/❌ | N |)
        if not line.startswith("|") or line.startswith("| ---") or line.startswith("| Formule"):
            continue

        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) < 4:
            continue

        latex_raw, desc, donnee_raw, freq_raw = cols[0], cols[1], cols[2], cols[3]

        # Extraire le LaTeX entre $...$
        latex_m = re.search(r"\$(.+?)\$", latex_raw, re.DOTALL)
        if not latex_m:
            continue
        latex = latex_m.group(1).strip()

        # Nettoyer fréquence
        freq_clean = re.sub(r"[^\d]", "", freq_raw)
        freq = int(freq_clean) if freq_clean else 1

        fid += 1
        formules.append({
            "id": f"f{fid:03d}",
            "themeId": domain_to_theme(current_section),
            "domaine": current_section,
            "latex": latex,
            "description": desc,
            "donnee": "✅" in donnee_raw,
            "frequence": freq,
            "trou": build_trou(latex),  # None si non trou-able
        })

    return formules
```

- [ ] **Étape 1.3 : Générer les données trou pour chaque formule**

```python
# Termes masquables avec leurs distracteurs
TROU_CANDIDATES = [
    (r"\\sqrt\{3\}",      r"\sqrt{3}",   [r"\sqrt{2}", r"3", r"2\pi", r"\sqrt{3}/2"]),
    (r"\\cos\\varphi",    r"\cos\varphi",[r"\sin\varphi", r"\tan\varphi", r"\varphi", r"\cos^2\varphi"]),
    (r"\\eta",            r"\eta",       [r"\varphi", r"\alpha", r"\omega", r"g"]),
    (r"\\omega",          r"\omega",     [r"\Omega", r"2\pi f", r"\omega_0", r"p"]),
    (r"\balpha\b",        r"\alpha",     [r"\beta", r"\eta", r"1-\alpha", r"\omega"]),
    (r"\bg\b",            r"g",          [r"1-g", r"g^2", r"N_s", r"\omega_s"]),
]

def build_trou(latex: str) -> dict | None:
    """Retourne le dict trou si la formule contient un terme masquable."""
    for pattern, term, distractors in TROU_CANDIDATES:
        if re.search(pattern, latex):
            # Remplacer le terme par un placeholder visible
            masked = re.sub(pattern, r"\\boxed{\\,?\\,?}", latex, count=1)
            return {
                "maskedTerm": term,
                "maskedLatex": masked,
                "choices": [term] + distractors[:3],  # correct en premier, mélangé côté JS
            }
    return None
```

- [ ] **Étape 1.4 : Parser tableau_themes_capet.md → themes[]**

```python
INTENSITE_MAP = {"🔴": "rouge", "🟠": "orange", "🟡": "jaune"}
FICHES_EXISTANTES = {"T02", "T03", "T11", "T14", "T21", "T24", "T30"}

def parse_themes(md_path: Path) -> list[dict]:
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    themes = []

    # Trouver la 1ère table (intensité) — s'arrêter avant "## Tableau de présence"
    in_table = False
    header_cols = []  # noms des colonnes (années/épreuves)

    for line in lines:
        if "Tableau de présence" in line:
            break
        if line.startswith("| Thème"):
            # Extraire les en-têtes de colonnes
            header_cols = [c.strip() for c in line.split("|")[2:-2]]  # skip Thème + Moy.
            in_table = True
            continue
        if not in_table or line.startswith("| ---") or not line.startswith("|"):
            continue

        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) < 3:
            continue

        theme_col = cols[0]
        # Extraire l'id (T01, T02…)
        tid_m = re.match(r"(T\d{2})", theme_col)
        if not tid_m:
            continue
        tid = tid_m.group(1)
        nom = re.sub(r"T\d{2}\s*[–-]\s*", "", theme_col).strip()

        # Construire presences dict
        presences = {}
        for i, col_name in enumerate(header_cols):
            if i + 1 < len(cols):
                cell = cols[i + 1]
                intensite = INTENSITE_MAP.get(cell.strip(), None)
                if intensite:
                    presences[col_name] = intensite

        # Intensité globale = max présent dans presences
        poids = {"rouge": 3, "orange": 2, "jaune": 1}
        intensite_max = max(
            (poids.get(v, 0) for v in presences.values()),
            default=0
        )
        intensite = {3: "rouge", 2: "orange", 1: "jaune", 0: "absent"}[min(intensite_max, 3)]

        fiche_path = None
        if tid in FICHES_EXISTANTES:
            matches = list((DOCS / "04_Fiches_Themes").glob(f"{tid}_*.md"))
            if matches:
                fiche_path = matches[0].relative_to(ROOT).as_posix()

        themes.append({
            "id": tid,
            "nom": nom,
            "intensite": intensite,
            "presences": presences,
            "hasFiche": tid in FICHES_EXISTANTES,
            "fichePath": fiche_path,
        })

    return themes
```

- [ ] **Étape 1.5 : Parser points_aveugles.md et sujets/**

```python
def parse_points_aveugles(md_path: Path) -> list[dict]:
    """Extrait les items de liste (- **...**) comme points aveugles."""
    text = md_path.read_text(encoding="utf-8")
    points = []
    for line in text.splitlines():
        m = re.match(r"-\s+\*\*(.+?)\*\*\s*[:\—–-]?\s*(.+)?", line)
        if m:
            points.append({
                "texte": m.group(1).strip(),
                "detail": (m.group(2) or "").strip(),
                "source": "Rapports jury 2019–2025",
            })
        elif re.match(r"-\s+Facteur|Glissement|Signe|Unité|Bilan", line):
            clean = re.sub(r"^-\s+", "", line).strip()
            points.append({"texte": clean, "detail": "", "source": "Rapports jury"})
    return points[:10]  # garder les 10 premiers


def parse_sujets(sujets_dir: Path) -> list[dict]:
    sujets = []
    for md_file in sorted(sujets_dir.rglob("*.md")):
        parts = md_file.parts
        # Structure : .../01_Sujets/ANNÉE/NomDossier/fichier.md
        try:
            annee_idx = next(i for i, p in enumerate(parts) if re.match(r"^\d{4}$", p))
            annee = int(parts[annee_idx])
        except StopIteration:
            continue
        epreuve = "E1" if "Epreuve1" in md_file.name or "epreuve1" in md_file.name else "E2"
        sujets.append({
            "annee": annee,
            "epreuve": epreuve,
            "titre": md_file.stem.replace("_", " "),
            "path": md_file.relative_to(ROOT).as_posix(),
            "themes": [],  # rempli après en croisant avec DATA.themes[].presences
        })
    return sorted(sujets, key=lambda s: (s["annee"], s["epreuve"]))
```

- [ ] **Étape 1.6 : Enrichir sujets avec leurs thèmes et écrire data.js**

```python
def enrich_sujets_themes(sujets: list[dict], themes: list[dict]) -> None:
    """Ajoute la liste des thèmes présents à chaque sujet via presences."""
    for sujet in sujets:
        col_key = f"{sujet['annee']}_E{sujet['epreuve'][-1]}"
        sujet["themes"] = [
            t["id"] for t in themes
            if col_key in t.get("presences", {})
        ]


def write_data_js(themes, formules, sujets, points_aveugles, out_path: Path):
    data = {
        "themes": themes,
        "formules": formules,
        "sujets": sujets,
        "pointsAveugles": points_aveugles,
        "dateEpreuve": "2026-06-01",
    }
    js = "// Généré par build.py — ne pas modifier manuellement\n"
    js += "window.DATA = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"
    out_path.write_text(js, encoding="utf-8")
    print(f"✅ {out_path} — {len(themes)} thèmes, {len(formules)} formules, {len(sujets)} sujets")


if __name__ == "__main__":
    themes        = parse_themes(DOCS / "tableau_themes_capet.md")
    formules      = parse_formules(DOCS / "formulaire_capet.md")
    points        = parse_points_aveugles(DOCS / "points_aveugles.md")
    sujets        = parse_sujets(DOCS / "01_Sujets")
    enrich_sujets_themes(sujets, themes)
    os.makedirs(OUT.parent, exist_ok=True)
    write_data_js(themes, formules, sujets, points, OUT)
```

- [ ] **Étape 1.7 : Exécuter et vérifier la sortie**

```bash
python build.py
```

Sortie attendue :
```
✅ app/data.js — 30 thèmes, ~130 formules, 22 sujets
```

Vérifier dans `app/data.js` :
- `window.DATA.themes.length === 30`
- `window.DATA.formules.length >= 100`
- `window.DATA.formules.filter(f => f.trou !== null).length >= 20`
- `window.DATA.sujets.length === 22`

- [ ] **Étape 1.8 : Commit**

```bash
git init  # si pas encore fait
git add build.py app/data.js
git commit -m "feat: add build.py and generated data.js"
```

---

## Task 2 : index.html + style.css — Shell SPA

**Files :**
- Create : `index.html`
- Create : `app/style.css`

- [ ] **Étape 2.1 : Créer index.html**

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CAPET SII IE — Révision 2026</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <link rel="stylesheet" href="app/style.css">
</head>
<body>
  <nav id="nav">
    <span class="nav-brand">⚡ CAPET SII IE</span>
    <a href="#/accueil" class="nav-link">Accueil</a>
    <a href="#/themes" class="nav-link">Thèmes</a>
    <a href="#/formulaire" class="nav-link">Formulaire</a>
    <a href="#/progression" class="nav-link">Progression</a>
  </nav>
  <main id="app">Chargement…</main>

  <!-- KaTeX auto-render -->
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

  <!-- App -->
  <script src="app/data.js"></script>
  <script src="app/storage.js"></script>
  <script src="app/katex-render.js"></script>
  <script src="app/views/accueil.js"></script>
  <script src="app/views/themes.js"></script>
  <script src="app/views/theme.js"></script>
  <script src="app/views/formulaire.js"></script>
  <script src="app/views/progression.js"></script>
  <script src="app/quiz/qcm.js"></script>
  <script src="app/quiz/trous.js"></script>
  <script src="app/router.js"></script>
</body>
</html>
```

- [ ] **Étape 2.2 : Créer app/style.css — variables et base**

```css
:root {
  --bg: #0d1117;
  --bg2: #161b22;
  --bg3: #21262d;
  --border: #30363d;
  --text: #e6edf3;
  --text2: #8b949e;
  --rouge: #f85149;
  --orange: #fb923c;
  --jaune: #e3b341;
  --vert: #3fb950;
  --bleu: #58a6ff;
  --violet: #bc8cff;
  --radius: 8px;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  background: var(--bg);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 15px;
  min-height: 100vh;
}

#nav {
  background: var(--bg2);
  border-bottom: 1px solid var(--border);
  padding: 0 24px;
  height: 52px;
  display: flex;
  align-items: center;
  gap: 24px;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-brand { font-weight: 700; color: var(--bleu); font-size: 16px; margin-right: 8px; }
.nav-link { color: var(--text2); text-decoration: none; font-size: 14px; }
.nav-link:hover, .nav-link.active { color: var(--text); }

#app { max-width: 900px; margin: 0 auto; padding: 32px 24px; }

/* Cartes */
.card {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
  margin-bottom: 12px;
}

/* Badges */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
}
.badge-rouge  { background: #2d1214; color: var(--rouge); }
.badge-orange { background: #2d1a0a; color: var(--orange); }
.badge-jaune  { background: #2d2209; color: var(--jaune); }
.badge-bleu   { background: #0c1f3a; color: var(--bleu); }
.badge-vert   { background: #0d2416; color: var(--vert); }

/* Barre de progression */
.progress-bar { background: var(--bg3); border-radius: 10px; height: 6px; overflow: hidden; }
.progress-fill { height: 100%; border-radius: 10px; transition: width 0.3s; }
.progress-fill.rouge  { background: var(--rouge); }
.progress-fill.orange { background: var(--orange); }
.progress-fill.vert   { background: var(--vert); }

/* Onglets */
.tabs { display: flex; border-bottom: 1px solid var(--border); margin-bottom: 20px; gap: 0; }
.tab {
  padding: 10px 16px;
  cursor: pointer;
  color: var(--text2);
  font-size: 14px;
  border-bottom: 2px solid transparent;
  transition: color 0.15s;
}
.tab.active { color: var(--bleu); border-bottom-color: var(--bleu); }
.tab:hover { color: var(--text); }

/* Boutons */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: opacity 0.15s;
}
.btn:hover { opacity: 0.85; }
.btn-primary { background: #1f6feb; color: white; }
.btn-success { background: #1a7f37; color: white; }
.btn-danger  { background: #b91c1c; color: white; }
.btn-ghost   { background: var(--bg3); color: var(--text); }

/* Tableau formules */
.formule-table { width: 100%; border-collapse: collapse; }
.formule-table th { color: var(--text2); font-size: 12px; text-align: left; padding: 8px 12px; border-bottom: 1px solid var(--border); }
.formule-table td { padding: 10px 12px; border-bottom: 1px solid var(--bg3); vertical-align: middle; }
.formule-table tr:hover td { background: var(--bg3); }

/* Quiz */
.quiz-option {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 12px 16px;
  margin-bottom: 8px;
  cursor: pointer;
  transition: border-color 0.15s, background 0.15s;
}
.quiz-option:hover { border-color: var(--bleu); }
.quiz-option.correct  { background: #0d2416; border-color: var(--vert); color: var(--vert); }
.quiz-option.wrong    { background: #2d1214; border-color: var(--rouge); color: var(--rouge); }
.quiz-option.disabled { pointer-events: none; }

.jeton {
  display: inline-block;
  background: var(--bg3);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 6px 14px;
  margin: 4px;
  cursor: pointer;
  font-size: 13px;
  transition: border-color 0.15s;
}
.jeton:hover { border-color: var(--violet); }
.jeton.selected { background: #1f1d2e; border-color: var(--violet); color: var(--violet); }

/* Grille progression */
.progression-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 10px;
  margin-top: 16px;
}
.progression-cell {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 12px;
}

/* Utilitaires */
.text-muted { color: var(--text2); }
.text-sm { font-size: 13px; }
.mt-4 { margin-top: 16px; }
.mt-8 { margin-top: 32px; }
.flex { display: flex; }
.flex-col { flex-direction: column; }
.gap-2 { gap: 8px; }
.gap-4 { gap: 16px; }
.items-center { align-items: center; }
.justify-between { justify-content: space-between; }
h1 { font-size: 22px; margin-bottom: 8px; }
h2 { font-size: 18px; margin-bottom: 6px; }
h3 { font-size: 15px; }
```

- [ ] **Étape 2.3 : Ouvrir index.html dans le navigateur, vérifier que la nav s'affiche correctement**

Ouvrir `index.html` directement (double-clic ou `python -m http.server 8080`). Vérifier :
- Barre de navigation visible, fond sombre
- "Chargement…" dans `#app`
- Aucune erreur console (KaTeX peut échouer si hors ligne — normal)

- [ ] **Étape 2.4 : Commit**

```bash
git add index.html app/style.css
git commit -m "feat: add SPA shell with nav and base styles"
```

---

## Task 3 : router.js + katex-render.js

**Files :**
- Create : `app/router.js`
- Create : `app/katex-render.js`

- [ ] **Étape 3.1 : Créer app/katex-render.js**

```js
// Rend toutes les formules LaTeX dans un élément DOM.
// Dégradation gracieuse si KaTeX n'est pas chargé (hors ligne).
function renderMath(el) {
  if (typeof renderMathInElement !== "function") return;
  renderMathInElement(el, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false },
    ],
    throwOnError: false,
  });
}
```

- [ ] **Étape 3.2 : Créer app/router.js**

```js
// Mappe les routes hash vers les fonctions de rendu.
// Chaque vue exporte une fonction renderXxx(params) -> string HTML.
const ROUTES = {
  "/accueil":     () => renderAccueil(),
  "/themes":      () => renderThemes(),
  "/theme/:id":   (p) => renderTheme(p.id),
  "/formulaire":  () => renderFormulaire(),
  "/progression": () => renderProgression(),
};

function resolveRoute(hash) {
  const path = hash.replace(/^#/, "") || "/accueil";
  for (const [pattern, handler] of Object.entries(ROUTES)) {
    const keys = [];
    const re = new RegExp(
      "^" + pattern.replace(/:(\w+)/g, (_, k) => { keys.push(k); return "([^/]+)"; }) + "$"
    );
    const m = path.match(re);
    if (m) {
      const params = Object.fromEntries(keys.map((k, i) => [k, m[i + 1]]));
      return { handler, params };
    }
  }
  return { handler: () => "<p>Page introuvable</p>", params: {} };
}

function navigate() {
  const { handler, params } = resolveRoute(window.location.hash);
  const app = document.getElementById("app");
  app.innerHTML = handler(params);
  renderMath(app);

  // Mettre à jour l'état actif dans la nav
  document.querySelectorAll(".nav-link").forEach(a => {
    a.classList.toggle("active", window.location.hash.startsWith(a.getAttribute("href")));
  });
}

window.addEventListener("hashchange", navigate);
window.addEventListener("DOMContentLoaded", () => {
  if (!window.location.hash) window.location.hash = "#/accueil";
  navigate();
});
```

- [ ] **Étape 3.3 : Créer des stubs vides pour toutes les vues (pour que le router ne plante pas)**

Créer `app/views/accueil.js` :
```js
function renderAccueil() { return "<h1>Accueil</h1><p>À implémenter</p>"; }
```

Créer `app/views/themes.js` :
```js
function renderThemes() { return "<h1>Thèmes</h1><p>À implémenter</p>"; }
```

Créer `app/views/theme.js` :
```js
function renderTheme(id) { return `<h1>Thème ${id}</h1><p>À implémenter</p>`; }
```

Créer `app/views/formulaire.js` :
```js
function renderFormulaire() { return "<h1>Formulaire</h1><p>À implémenter</p>"; }
```

Créer `app/views/progression.js` :
```js
function renderProgression() { return "<h1>Progression</h1><p>À implémenter</p>"; }
```

Créer `app/quiz/qcm.js` :
```js
function renderQCM(formules, onDone) { return "<p>Quiz QCM à implémenter</p>"; }
```

Créer `app/quiz/trous.js` :
```js
function renderTrous(formules, onDone) { return "<p>Quiz Trous à implémenter</p>"; }
```

- [ ] **Étape 3.4 : Vérifier le routing dans le navigateur**

Ouvrir `index.html`. Cliquer sur chaque lien de nav. Vérifier :
- L'URL change (`#/accueil`, `#/themes`, etc.)
- Le contenu du `#app` change à chaque clic
- Aucune erreur JS dans la console

- [ ] **Étape 3.5 : Commit**

```bash
git add app/router.js app/katex-render.js app/views/ app/quiz/
git commit -m "feat: add hash router and view stubs"
```

---

## Task 4 : storage.js — Abstraction localStorage

**Files :**
- Create : `app/storage.js`

- [ ] **Étape 4.1 : Créer app/storage.js**

```js
// Abstraction localStorage pour la progression des formules et thèmes.
// Une formule est "maîtrisée" après 2 réponses correctes consécutives.

const Storage = (() => {
  const PREFIX = "capet_";

  function key(id) { return PREFIX + id; }

  function getFormule(id) {
    try {
      return JSON.parse(localStorage.getItem(key("f_" + id))) || {
        mastered: false, correct: 0, attempts: 0, consecutive: 0
      };
    } catch { return { mastered: false, correct: 0, attempts: 0, consecutive: 0 }; }
  }

  function recordAnswer(id, isCorrect) {
    const s = getFormule(id);
    s.attempts++;
    if (isCorrect) {
      s.correct++;
      s.consecutive++;
      if (s.consecutive >= 2) s.mastered = true;
    } else {
      s.consecutive = 0;
    }
    localStorage.setItem(key("f_" + id), JSON.stringify(s));
    return s;
  }

  function isMastered(id) { return getFormule(id).mastered; }

  // % formules maîtrisées pour un thème (0.0 → 1.0)
  function getThemeProgress(themeId) {
    const formules = window.DATA.formules.filter(
      f => f.themeId === themeId && !f.donnee
    );
    if (!formules.length) return 1;
    const done = formules.filter(f => isMastered(f.id)).length;
    return done / formules.length;
  }

  function resetTheme(themeId) {
    window.DATA.formules
      .filter(f => f.themeId === themeId)
      .forEach(f => localStorage.removeItem(key("f_" + f.id)));
  }

  function resetAll() {
    Object.keys(localStorage)
      .filter(k => k.startsWith(PREFIX))
      .forEach(k => localStorage.removeItem(k));
  }

  // Score de priorité pour l'accueil (plus élevé = plus urgent)
  function getPriorityScore(theme) {
    const poids = { rouge: 3, orange: 2, jaune: 1, absent: 0 };
    const intensite = poids[theme.intensite] || 0;
    const progress = getThemeProgress(theme.id);
    return intensite * (1 - progress);
  }

  return { getFormule, recordAnswer, isMastered, getThemeProgress, resetTheme, resetAll, getPriorityScore };
})();
```

- [ ] **Étape 4.2 : Vérifier dans la console du navigateur**

Ouvrir `index.html`. Dans la console :
```js
Storage.recordAnswer("f001", true)   // → { mastered: false, correct: 1, consecutive: 1, ... }
Storage.recordAnswer("f001", true)   // → { mastered: true, correct: 2, consecutive: 2, ... }
Storage.isMastered("f001")           // → true
Storage.getThemeProgress("T02")      // → 0.125 (1/8 formules T02 maîtrisées)
Storage.resetAll()
Storage.isMastered("f001")           // → false
```

- [ ] **Étape 4.3 : Commit**

```bash
git add app/storage.js
git commit -m "feat: add localStorage storage abstraction"
```

---

## Task 5 : views/accueil.js — Accueil intelligent

**Files :**
- Modify : `app/views/accueil.js`

- [ ] **Étape 5.1 : Implémenter renderAccueil()**

```js
function renderAccueil() {
  const { themes, formules, pointsAveugles, dateEpreuve } = window.DATA;

  // Compteurs
  const formulesMemoriser = formules.filter(f => !f.donnee);
  const formulesOK = formulesMemoriser.filter(f => Storage.isMastered(f.id)).length;
  const themesVus = themes.filter(t => Storage.getThemeProgress(t.id) > 0).length;
  const joursRestants = Math.max(0, Math.round(
    (new Date(dateEpreuve) - new Date()) / 86400000
  ));

  // Suggestion : thème rouge le plus urgent
  const suggestion = [...themes]
    .filter(t => t.intensite !== "absent")
    .sort((a, b) => Storage.getPriorityScore(b) - Storage.getPriorityScore(a))[0];

  const suggProgress = Math.round(Storage.getThemeProgress(suggestion.id) * 100);

  // Points aveugles (max 4)
  const aveugles = pointsAveugles.slice(0, 4);

  // Thèmes prioritaires (rouge + orange, max 6)
  const prioritaires = themes
    .filter(t => t.intensite === "rouge" || t.intensite === "orange")
    .sort((a, b) => Storage.getPriorityScore(b) - Storage.getPriorityScore(a))
    .slice(0, 6);

  return `
    <div class="flex justify-between items-center" style="margin-bottom:24px">
      <div>
        <h1>⚡ Révision CAPET SII IE 2026</h1>
        <p class="text-muted text-sm">Bonne révision !</p>
      </div>
      <span class="badge badge-bleu" style="font-size:14px">J-${joursRestants}</span>
    </div>

    <div class="flex gap-4" style="margin-bottom:20px">
      ${statCard(themesVus, "thèmes vus", "📚")}
      ${statCard(formulesOK, "formules OK", "✅")}
      ${statCard(formulesMemoriser.length - formulesOK, "formules restantes", "🎯")}
    </div>

    <div class="card" style="border-left:3px solid var(--vert); margin-bottom:16px">
      <p class="text-muted text-sm" style="margin-bottom:4px">✨ À réviser maintenant</p>
      <h2>${suggestion.id} — ${suggestion.nom}</h2>
      <div class="flex gap-2 items-center" style="margin:8px 0">
        <span class="badge badge-${suggestion.intensite}">🔴 Prioritaire</span>
        <span class="badge badge-bleu">${Object.keys(suggestion.presences).length}/22 épreuves</span>
      </div>
      <div class="progress-bar" style="margin:8px 0"><div class="progress-fill vert" style="width:${suggProgress}%"></div></div>
      <p class="text-muted text-sm">${suggProgress}% maîtrisé</p>
      <a href="#/theme/${suggestion.id}" class="btn btn-success" style="margin-top:12px;display:inline-flex">Commencer →</a>
    </div>

    <div class="card" style="border-left:3px solid var(--jaune); margin-bottom:16px">
      <p class="text-muted text-sm" style="margin-bottom:8px">⚠️ Points aveugles — Rapports jury 2019–2025</p>
      ${aveugles.map(p => `<p class="text-sm" style="margin-bottom:4px">• ${p.texte}</p>`).join("")}
    </div>

    <h2 style="margin-bottom:12px">Thèmes prioritaires</h2>
    ${prioritaires.map(t => themeRow(t)).join("")}
  `;
}

function statCard(val, label, icon) {
  return `
    <div class="card" style="flex:1;text-align:center;padding:16px">
      <div style="font-size:28px;font-weight:700;color:var(--bleu)">${val}</div>
      <div class="text-muted text-sm">${icon} ${label}</div>
    </div>`;
}

function themeRow(t) {
  const pct = Math.round(Storage.getThemeProgress(t.id) * 100);
  const color = pct >= 75 ? "vert" : pct >= 40 ? "orange" : "rouge";
  const formules = window.DATA.formules.filter(f => f.themeId === t.id && !f.donnee);
  return `
    <a href="#/theme/${t.id}" style="text-decoration:none;display:block">
      <div class="card" style="margin-bottom:8px">
        <div class="flex justify-between items-center">
          <div>
            <span class="badge badge-${t.intensite}" style="margin-right:8px">${t.id}</span>
            <span>${t.nom}</span>
          </div>
          <span class="text-muted text-sm">${pct}%</span>
        </div>
        <div class="progress-bar" style="margin-top:8px">
          <div class="progress-fill ${color}" style="width:${pct}%"></div>
        </div>
        <p class="text-muted text-sm" style="margin-top:4px">${formules.length} formules à mémoriser</p>
      </div>
    </a>`;
}
```

- [ ] **Étape 5.2 : Vérifier dans le navigateur**

Naviguer vers `#/accueil`. Vérifier :
- Les 3 compteurs affichés
- Le thème suggéré a un badge d'intensité et une barre de progression
- La section "points aveugles" liste au moins 2 items
- La liste des thèmes prioritaires contient des thèmes rouge/orange
- Le bouton "Commencer →" redirige vers `#/theme/TXX`

- [ ] **Étape 5.3 : Commit**

```bash
git add app/views/accueil.js
git commit -m "feat: implement accueil intelligent with priority suggestion"
```

---

## Task 6 : views/themes.js — Liste filtrée des 30 thèmes

**Files :**
- Modify : `app/views/themes.js`

- [ ] **Étape 6.1 : Implémenter renderThemes()**

```js
function renderThemes() {
  const { themes } = window.DATA;
  return `
    <h1>Les 30 thèmes</h1>
    <p class="text-muted text-sm" style="margin-bottom:16px">Cliquez sur un thème pour accéder à sa fiche, ses formules et son quiz.</p>

    <div class="flex gap-2" style="margin-bottom:20px" id="theme-filters">
      ${["Tous","rouge","orange","jaune"].map((f,i) =>
        `<button class="btn ${i===0?"btn-primary":"btn-ghost"}" onclick="filterThemes('${f}')" data-filter="${f}">
          ${f==="Tous" ? "Tous" : f==="rouge" ? "🔴 Prioritaires" : f==="orange" ? "🟠 Importants" : "🟡 Mentionnés"}
        </button>`
      ).join("")}
    </div>

    <div id="themes-list">
      ${themes.map(t => themeCard(t)).join("")}
    </div>
  `;
}

function themeCard(t) {
  const pct = Math.round(Storage.getThemeProgress(t.id) * 100);
  const color = pct >= 75 ? "vert" : pct >= 40 ? "orange" : "rouge";
  const nbEpreuves = Object.keys(t.presences).length;
  const formules = window.DATA.formules.filter(f => f.themeId === t.id && !f.donnee);
  return `
    <a href="#/theme/${t.id}" style="text-decoration:none" data-intensite="${t.intensite}">
      <div class="card" style="margin-bottom:8px">
        <div class="flex justify-between items-center">
          <div class="flex items-center gap-2">
            <span class="badge badge-${t.intensite}">${t.id}</span>
            <strong>${t.nom}</strong>
          </div>
          <span class="text-muted text-sm">${pct}%</span>
        </div>
        <div class="flex gap-2 items-center" style="margin-top:8px">
          <span class="text-muted text-sm">${nbEpreuves}/22 épreuves · ${formules.length} formules à mémoriser</span>
        </div>
        <div class="progress-bar" style="margin-top:8px">
          <div class="progress-fill ${color}" style="width:${pct}%"></div>
        </div>
      </div>
    </a>`;
}

function filterThemes(filter) {
  const cards = document.querySelectorAll("#themes-list a");
  cards.forEach(card => {
    const intensite = card.dataset.intensite;
    card.style.display = (filter === "Tous" || intensite === filter) ? "block" : "none";
  });
  document.querySelectorAll("#theme-filters button").forEach(btn => {
    btn.className = "btn " + (btn.dataset.filter === filter ? "btn-primary" : "btn-ghost");
  });
}
```

- [ ] **Étape 6.2 : Vérifier dans le navigateur**

Naviguer vers `#/themes`. Vérifier :
- 30 cartes affichées
- Boutons de filtre fonctionnels (Prioritaires → seuls les 🔴 restent)
- Clic sur une carte → navigation vers `#/theme/TXX`

- [ ] **Étape 6.3 : Commit**

```bash
git add app/views/themes.js
git commit -m "feat: implement themes list with filter"
```

---

## Task 7 : views/theme.js — Onglets Fiche + Formules

**Files :**
- Modify : `app/views/theme.js`

- [ ] **Étape 7.1 : Structure de la vue thème avec onglets**

```js
function renderTheme(id) {
  const theme = window.DATA.themes.find(t => t.id === id);
  if (!theme) return `<p>Thème ${id} introuvable.</p>`;

  const formules = window.DATA.formules.filter(f => f.themeId === id);
  const formulesAMemoriser = formules.filter(f => !f.donnee);
  const maitrisees = formulesAMemoriser.filter(f => Storage.isMastered(f.id));
  const pct = formulesAMemoriser.length
    ? Math.round(maitrisees.length / formulesAMemoriser.length * 100)
    : 100;
  const nbEpreuves = Object.keys(theme.presences).length;

  return `
    <div style="margin-bottom:4px">
      <a href="#/themes" class="text-muted text-sm" style="text-decoration:none">← Tous les thèmes</a>
    </div>
    <h1 style="margin-bottom:8px">${theme.id} — ${theme.nom}</h1>
    <div class="flex gap-2" style="margin-bottom:12px">
      <span class="badge badge-${theme.intensite}">🔴 ${theme.intensite}</span>
      <span class="badge badge-bleu">${nbEpreuves}/22 épreuves</span>
      <span class="badge badge-${maitrisees.length === formulesAMemoriser.length ? "vert" : "rouge"}">${formulesAMemoriser.length - maitrisees.length} formules restantes</span>
    </div>
    <div class="progress-bar" style="margin-bottom:20px">
      <div class="progress-fill vert" style="width:${pct}%"></div>
    </div>

    <div class="tabs">
      <div class="tab active" onclick="switchTab(event,'fiche')">📖 Fiche</div>
      <div class="tab" onclick="switchTab(event,'formules')">🧮 Formules</div>
      <div class="tab" onclick="switchTab(event,'quiz')">🧩 Quiz</div>
      <div class="tab" onclick="switchTab(event,'sujets')">📋 Sujets</div>
    </div>

    <div id="tab-fiche">${renderOngletFiche(theme)}</div>
    <div id="tab-formules" style="display:none">${renderOngletFormules(formules)}</div>
    <div id="tab-quiz" style="display:none">${renderOngletQuiz(id, formulesAMemoriser)}</div>
    <div id="tab-sujets" style="display:none">${renderOngletSujets(theme)}</div>
  `;
}

function switchTab(event, name) {
  ["fiche","formules","quiz","sujets"].forEach(n => {
    document.getElementById("tab-" + n).style.display = n === name ? "block" : "none";
  });
  document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
  event.target.classList.add("active");
  if (name === "quiz") initQuiz(event.target.closest("[id]")?.id);
  renderMath(document.getElementById("tab-" + name));
}
```

- [ ] **Étape 7.2 : Onglet Fiche**

```js
function renderOngletFiche(theme) {
  if (!theme.hasFiche) {
    // Pas de fiche dédiée : afficher un résumé des formules du domaine
    const formules = window.DATA.formules.filter(f => f.themeId === theme.id);
    if (!formules.length) return `<p class="text-muted">Pas de fiche ni de formules pour ce thème.</p>`;
    return `
      <div class="card">
        <p class="text-muted text-sm" style="margin-bottom:12px">Pas de fiche rédigée pour ce thème — voici les formules associées :</p>
        ${formules.map(f => `
          <div style="padding:10px 0;border-bottom:1px solid var(--bg3)">
            <p style="font-size:14px">$${f.latex}$</p>
            <p class="text-muted text-sm">${f.description}</p>
          </div>`).join("")}
      </div>`;
  }
  // Fiche disponible : charger via fetch (fonctionne en HTTP, pas en file://)
  return `<div id="fiche-content" class="card">
    <p class="text-muted text-sm">Chargement de la fiche…</p>
  </div>
  <script>
    fetch("${theme.fichePath}")
      .then(r => r.text())
      .then(md => {
        document.getElementById("fiche-content").innerHTML = mdToHtml(md);
        renderMath(document.getElementById("fiche-content"));
      })
      .catch(() => {
        document.getElementById("fiche-content").innerHTML =
          "<p class=\\"text-muted\\">Impossible de charger la fiche (mode local ?).</p>";
      });
  <\/script>`;
}

// Convertisseur Markdown minimal (titres, gras, listes, paragraphes)
function mdToHtml(md) {
  return md
    .replace(/^#{3} (.+)$/gm, "<h3>$1</h3>")
    .replace(/^#{2} (.+)$/gm, "<h2>$1</h2>")
    .replace(/^# (.+)$/gm, "<h1>$1</h1>")
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\*(.+?)\*/g, "<em>$1</em>")
    .replace(/^- (.+)$/gm, "<li>$1</li>")
    .replace(/(<li>.*<\/li>)/gs, "<ul>$1</ul>")
    .replace(/\n\n/g, "</p><p>")
    .replace(/^(?!<[hul])(.+)$/gm, "<p>$1</p>")
    .replace(/<p><\/p>/g, "");
}
```

- [ ] **Étape 7.3 : Onglet Formules**

```js
function renderOngletFormules(formules) {
  if (!formules.length) return `<p class="text-muted">Aucune formule pour ce thème.</p>`;
  return `
    <table class="formule-table">
      <thead><tr>
        <th>Formule</th>
        <th>Description</th>
        <th>Donnée ?</th>
        <th>Fréq.</th>
        <th>État</th>
      </tr></thead>
      <tbody>
        ${formules.map(f => {
          const mastered = Storage.isMastered(f.id);
          return `<tr>
            <td style="font-size:13px">$${f.latex}$</td>
            <td class="text-sm">${f.description}</td>
            <td style="text-align:center">${f.donnee ? "✅" : "❌"}</td>
            <td style="text-align:center" class="text-muted text-sm">${f.frequence}</td>
            <td style="text-align:center">
              ${f.donnee ? "—" : mastered
                ? `<span class="badge badge-vert">✓</span>`
                : `<span class="badge" style="background:var(--bg3);color:var(--text2)">—</span>`}
            </td>
          </tr>`;
        }).join("")}
      </tbody>
    </table>`;
}
```

- [ ] **Étape 7.4 : Vérifier dans le navigateur**

Naviguer vers `#/theme/T02`. Vérifier :
- Header avec badges, barre de progression
- Onglet Fiche actif par défaut, contenu visible
- Onglet Formules → tableau avec formules KaTeX rendues
- Switch entre onglets sans rechargement de page

- [ ] **Étape 7.5 : Commit**

```bash
git add app/views/theme.js
git commit -m "feat: implement theme view with fiche and formules tabs"
```

---

## Task 8 : quiz/qcm.js — Moteur QCM

**Files :**
- Modify : `app/quiz/qcm.js`

- [ ] **Étape 8.1 : Implémenter le moteur QCM**

```js
// Génère et gère une question QCM.
// formule : objet formule de DATA.formules
// allFormules : toutes les formules du thème (pour les distracteurs)
// onAnswer(formuleId, isCorrect) : callback après réponse
function renderQCMQuestion(formule, allFormules, onAnswer) {
  // 3 distracteurs : autres formules du même domaine, sinon du même thème
  const pool = allFormules
    .filter(f => f.id !== formule.id && f.domaine === formule.domaine);
  const wider = allFormules.filter(f => f.id !== formule.id && f.themeId === formule.themeId);
  const distractors = shuffle([...pool, ...wider]).slice(0, 3);

  const options = shuffle([
    { latex: formule.latex, correct: true },
    ...distractors.map(d => ({ latex: d.latex, correct: false })),
  ]);

  const qid = "qcm_" + Date.now();
  return `
    <div class="card">
      <p class="text-muted text-sm" style="margin-bottom:8px">QCM — Quelle formule correspond à :</p>
      <h3 style="margin-bottom:16px">${formule.description}</h3>
      <p class="text-muted text-sm" style="margin-bottom:8px">
        Domaine : ${formule.domaine} · Fréq. ${formule.frequence}/22
      </p>
    </div>
    <div id="${qid}-options">
      ${options.map((opt, i) => `
        <div class="quiz-option" onclick="answerQCM('${qid}',${opt.correct},'${formule.id}')">
          $${opt.latex}$
        </div>`).join("")}
    </div>
    <div id="${qid}-feedback" style="display:none"></div>
  `;
}

function answerQCM(qid, isCorrect, formuleId) {
  const options = document.querySelectorAll(`#${qid}-options .quiz-option`);
  options.forEach(opt => {
    opt.classList.add("disabled");
    // Trouver la bonne réponse pour la mettre en vert
  });
  options[0].classList.add(isCorrect ? "correct" : "wrong");

  const s = Storage.recordAnswer(formuleId, isCorrect);
  const feedback = document.getElementById(`${qid}-feedback`);
  feedback.style.display = "block";

  const f = window.DATA.formules.find(f => f.id === formuleId);
  feedback.innerHTML = `
    <div class="card" style="border-left:3px solid ${isCorrect ? "var(--vert)" : "var(--rouge)"}; margin-top:12px">
      <p style="color:${isCorrect ? "var(--vert)" : "var(--rouge)"}; margin-bottom:4px">
        ${isCorrect ? "✓ Correct !" : "✗ Raté — la bonne réponse était :"}
      </p>
      ${!isCorrect ? `<p style="margin-bottom:8px">$${f.latex}$</p>` : ""}
      <p class="text-muted text-sm">${s.mastered ? "🏆 Formule maîtrisée !" : `${s.consecutive}/2 consécutives`}</p>
    </div>`;
  renderMath(feedback);

  // Notifier le moteur de quiz parent
  document.dispatchEvent(new CustomEvent("quizAnswer", { detail: { formuleId, isCorrect } }));
}

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
```

- [ ] **Étape 8.2 : Commit**

```bash
git add app/quiz/qcm.js
git commit -m "feat: implement QCM quiz engine with distractors"
```

---

## Task 9 : quiz/trous.js — Moteur texte à trous

**Files :**
- Modify : `app/quiz/trous.js`

- [ ] **Étape 9.1 : Implémenter le moteur texte à trous**

```js
// Génère une question texte à trous pour une formule qui a un champ `trou`.
// Si la formule n'a pas de trou, retourne null.
function renderTrouQuestion(formule, onAnswer) {
  if (!formule.trou) return null;
  const { maskedTerm, maskedLatex, choices } = formule.trou;
  const shuffled = shuffle(choices);
  const qid = "trou_" + Date.now();

  return `
    <div class="card">
      <p class="text-muted text-sm" style="margin-bottom:8px">Texte à trous — Complétez la formule :</p>
      <h3 style="margin-bottom:4px">${formule.description}</h3>
      <p class="text-muted text-sm">${formule.domaine} · Fréq. ${formule.frequence}/22</p>
    </div>
    <div class="card" style="text-align:center; margin:12px 0; font-size:18px">
      $${maskedLatex}$
    </div>
    <p class="text-muted text-sm" style="margin-bottom:8px">Cliquez sur le bon terme :</p>
    <div id="${qid}-jetons">
      ${shuffled.map(c => `
        <span class="jeton" onclick="answerTrou('${qid}','${c}','${maskedTerm}','${formule.id}')">
          $${c}$
        </span>`).join("")}
    </div>
    <div id="${qid}-feedback" style="display:none"></div>
  `;
}

function answerTrou(qid, chosen, correct, formuleId) {
  const jetons = document.querySelectorAll(`#${qid}-jetons .jeton`);
  jetons.forEach(j => {
    j.style.pointerEvents = "none";
    if (j.textContent.trim() === correct || j.innerText.includes(correct)) {
      j.classList.add("selected");
    }
  });

  const isCorrect = chosen === correct;
  const s = Storage.recordAnswer(formuleId, isCorrect);
  const f = window.DATA.formules.find(f => f.id === formuleId);
  const feedback = document.getElementById(`${qid}-feedback`);
  feedback.style.display = "block";
  feedback.innerHTML = `
    <div class="card" style="border-left:3px solid ${isCorrect ? "var(--vert)" : "var(--rouge)"}; margin-top:12px">
      <p style="color:${isCorrect ? "var(--vert)" : "var(--rouge)"}">
        ${isCorrect ? "✓ Correct !" : `✗ Raté — le terme attendu était : $${correct}$`}
      </p>
      <p class="text-muted text-sm" style="margin-top:4px">
        Formule complète : $${f.latex}$
      </p>
      <p class="text-muted text-sm">${s.mastered ? "🏆 Formule maîtrisée !" : `${s.consecutive}/2 consécutives`}</p>
    </div>`;
  renderMath(feedback);
  document.dispatchEvent(new CustomEvent("quizAnswer", { detail: { formuleId, isCorrect } }));
}
```

- [ ] **Étape 9.2 : Commit**

```bash
git add app/quiz/trous.js
git commit -m "feat: implement fill-in-the-blank quiz engine"
```

---

## Task 10 : views/theme.js — Onglet Quiz (intégration QCM + Trous)

**Files :**
- Modify : `app/views/theme.js` (ajouter `renderOngletQuiz` et `initQuiz`)

- [ ] **Étape 10.1 : Ajouter le moteur de session quiz**

Ajouter dans `app/views/theme.js` :

```js
// État de session quiz (module-level)
let _quizSession = null;

function renderOngletQuiz(themeId, formulesAMemoriser) {
  const restantes = formulesAMemoriser.filter(f => !Storage.isMastered(f.id));
  if (!restantes.length) {
    return `<div class="card" style="text-align:center;padding:40px">
      <p style="font-size:32px">🏆</p>
      <h2 style="margin:8px 0">Toutes les formules maîtrisées !</h2>
      <p class="text-muted">Revenez après un reset pour vous re-tester.</p>
      <button class="btn btn-ghost" style="margin-top:16px"
        onclick="Storage.resetTheme('${themeId}'); window.location.hash='#/theme/${themeId}'">
        Recommencer
      </button>
    </div>`;
  }
  return `<div id="quiz-container">
    <div class="flex justify-between items-center" style="margin-bottom:16px">
      <p class="text-muted text-sm">${restantes.length} formules restantes dans ce thème</p>
      <button class="btn btn-ghost btn-sm" onclick="startQuiz('${themeId}')">🔄 Relancer</button>
    </div>
    <div id="quiz-question">Chargement…</div>
    <div id="quiz-next" style="display:none;margin-top:16px">
      <button class="btn btn-primary" onclick="nextQuizQuestion()">Question suivante →</button>
    </div>
    <div id="quiz-results" style="display:none"></div>
  </div>`;
}

function initQuiz(containerId) {
  // Appelé lors du switch vers l'onglet quiz
  const hash = window.location.hash;
  const id = hash.match(/#\/theme\/(\w+)/)?.[1];
  if (id) startQuiz(id);
}

function startQuiz(themeId) {
  const formules = window.DATA.formules.filter(
    f => f.themeId === themeId && !f.donnee && !Storage.isMastered(f.id)
  );
  _quizSession = {
    themeId,
    queue: shuffle([...formules]),
    index: 0,
    correct: 0,
    total: 0,
  };
  nextQuizQuestion();

  document.addEventListener("quizAnswer", onQuizAnswer, { once: false });
}

function nextQuizQuestion() {
  const s = _quizSession;
  if (!s || s.index >= s.queue.length) {
    showQuizResults();
    return;
  }

  document.getElementById("quiz-next").style.display = "none";
  const formule = s.queue[s.index];
  const allThemeFormules = window.DATA.formules.filter(f => f.themeId === s.themeId && !f.donnee);

  // Alterner aléatoirement QCM / trous
  const useTrou = formule.trou && Math.random() < 0.5;
  let html;
  if (useTrou) {
    html = renderTrouQuestion(formule);
  }
  if (!html) {
    html = renderQCMQuestion(formule, allThemeFormules, () => {});
  }

  document.getElementById("quiz-question").innerHTML = html;
  renderMath(document.getElementById("quiz-question"));
  s.index++;
}

function onQuizAnswer(e) {
  if (!_quizSession) return;
  _quizSession.total++;
  if (e.detail.isCorrect) _quizSession.correct++;
  document.getElementById("quiz-next").style.display = "block";
}

function showQuizResults() {
  const s = _quizSession;
  document.removeEventListener("quizAnswer", onQuizAnswer);
  const pct = s.total ? Math.round(s.correct / s.total * 100) : 0;
  document.getElementById("quiz-results").style.display = "block";
  document.getElementById("quiz-results").innerHTML = `
    <div class="card" style="text-align:center;padding:32px;margin-top:16px">
      <p style="font-size:48px;margin-bottom:8px">${pct >= 80 ? "🏆" : pct >= 50 ? "📈" : "💪"}</p>
      <h2>${pct}% — ${s.correct} / ${s.total}</h2>
      <p class="text-muted" style="margin-top:8px">Session terminée pour le thème ${s.themeId}</p>
      <button class="btn btn-primary" style="margin-top:16px"
        onclick="startQuiz('${s.themeId}')">Rejouer les erreurs</button>
    </div>`;
}
```

- [ ] **Étape 10.2 : Vérifier le quiz dans le navigateur**

Naviguer vers `#/theme/T02`, onglet Quiz. Vérifier :
- Une question QCM ou trous s'affiche avec la formule en KaTeX
- Clic sur une réponse → feedback couleur + explication
- Bouton "Question suivante" apparaît après réponse
- Fin de session → score affiché
- Formule maîtrisée après 2 bonnes réponses (barre de progression se met à jour)

- [ ] **Étape 10.3 : Commit**

```bash
git add app/views/theme.js app/quiz/qcm.js app/quiz/trous.js
git commit -m "feat: implement quiz session with QCM and fill-in-the-blank alternation"
```

---

## Task 11 : views/theme.js — Onglet Sujets

**Files :**
- Modify : `app/views/theme.js` (ajouter `renderOngletSujets`)

- [ ] **Étape 11.1 : Ajouter renderOngletSujets()**

```js
function renderOngletSujets(theme) {
  const sujets = window.DATA.sujets.filter(s => s.themes.includes(theme.id));
  if (!sujets.length) {
    return `<p class="text-muted">Ce thème n'a pas été identifié dans les sujets disponibles.</p>`;
  }

  const INTENSITE_LABEL = { rouge: "🔴 Central", orange: "🟠 Important", jaune: "🟡 Mentionné" };

  return `
    <p class="text-muted text-sm" style="margin-bottom:16px">
      ${sujets.length} épreuves contiennent ce thème (source : tableau_themes_capet.md)
    </p>
    ${sujets.map(s => {
      const colKey = `${s.annee}_E${s.epreuve.slice(-1)}`;
      const intensite = theme.presences[colKey];
      return `
        <div class="card" style="margin-bottom:8px">
          <div class="flex justify-between items-center">
            <div>
              <strong>${s.annee} — ${s.epreuve}</strong>
              <span class="text-muted text-sm" style="margin-left:8px">${s.titre}</span>
            </div>
            ${intensite ? `<span class="badge badge-${intensite}">${INTENSITE_LABEL[intensite] || intensite}</span>` : ""}
          </div>
          <button class="btn btn-ghost" style="margin-top:10px;font-size:12px"
            onclick="loadSujet(this,'${s.path}')">
            📄 Lire le sujet
          </button>
          <div class="sujet-content" style="display:none;margin-top:12px"></div>
        </div>`;
    }).join("")}
  `;
}

function loadSujet(btn, path) {
  const container = btn.nextElementSibling;
  if (container.style.display === "block") {
    container.style.display = "none";
    btn.textContent = "📄 Lire le sujet";
    return;
  }
  btn.textContent = "Chargement…";
  fetch(path)
    .then(r => r.text())
    .then(md => {
      container.innerHTML = `<div class="card" style="background:var(--bg3)">${mdToHtml(md)}</div>`;
      container.style.display = "block";
      btn.textContent = "▲ Fermer";
      renderMath(container);
    })
    .catch(() => {
      container.innerHTML = `<p class="text-muted text-sm">Impossible de charger (nécessite un serveur HTTP).</p>`;
      container.style.display = "block";
      btn.textContent = "▲ Fermer";
    });
}
```

- [ ] **Étape 11.2 : Vérifier l'onglet Sujets**

Lancer un serveur local : `python -m http.server 8080`, puis ouvrir `http://localhost:8080`.
Naviguer vers `#/theme/T02`, onglet Sujets. Vérifier :
- Liste des épreuves avec badges d'intensité
- Bouton "Lire le sujet" charge et affiche le Markdown
- Second clic replie le contenu

- [ ] **Étape 11.3 : Commit**

```bash
git add app/views/theme.js
git commit -m "feat: implement sujets tab with markdown fetch and display"
```

---

## Task 12 : views/formulaire.js — Toutes les formules + filtres

**Files :**
- Modify : `app/views/formulaire.js`

- [ ] **Étape 12.1 : Implémenter renderFormulaire()**

```js
function renderFormulaire() {
  const { formules } = window.DATA;
  const domaines = [...new Set(formules.map(f => f.domaine))].sort();

  return `
    <h1>Formulaire complet</h1>
    <p class="text-muted text-sm" style="margin-bottom:16px">${formules.length} formules · Sources : corrigés 2016–2021, rapports jury 2019–2025</p>

    <div class="flex gap-2" style="margin-bottom:12px;flex-wrap:wrap" id="form-filters">
      <input type="text" placeholder="🔍 Rechercher…" oninput="filterFormulaire()"
        id="form-search"
        style="background:var(--bg2);border:1px solid var(--border);border-radius:6px;padding:8px 12px;color:var(--text);font-size:14px;flex:1;min-width:180px">
      <select id="form-domaine" onchange="filterFormulaire()"
        style="background:var(--bg2);border:1px solid var(--border);border-radius:6px;padding:8px 12px;color:var(--text);font-size:14px">
        <option value="">Tous les domaines</option>
        ${domaines.map(d => `<option value="${d}">${d}</option>`).join("")}
      </select>
      <button class="btn btn-ghost" onclick="toggleFormFilter('memoriser')" id="btn-memoriser">❌ À mémoriser</button>
      <button class="btn btn-ghost" onclick="toggleFormFilter('nonmaitrises')" id="btn-nonmaitrises">🎯 Non maîtrisées</button>
    </div>

    <div id="form-count" class="text-muted text-sm" style="margin-bottom:12px">${formules.length} formules affichées</div>

    <table class="formule-table" id="form-table">
      <thead><tr>
        <th>Formule</th>
        <th>Description</th>
        <th>Domaine</th>
        <th>Donnée ?</th>
        <th>Fréq.</th>
        <th>État</th>
      </tr></thead>
      <tbody>
        ${formules.map(f => {
          const mastered = Storage.isMastered(f.id);
          return `<tr data-domaine="${f.domaine}" data-desc="${f.description.toLowerCase()}" data-donnee="${f.donnee}" data-mastered="${mastered}">
            <td style="font-size:13px;white-space:nowrap">$${f.latex}$</td>
            <td class="text-sm">${f.description}</td>
            <td class="text-sm text-muted">${f.domaine}</td>
            <td style="text-align:center">${f.donnee ? "✅" : "❌"}</td>
            <td style="text-align:center" class="text-muted text-sm">${f.frequence}</td>
            <td style="text-align:center">
              ${f.donnee ? "—" : mastered
                ? `<span class="badge badge-vert">✓</span>`
                : `<span class="badge" style="background:var(--bg3);color:var(--text2)">—</span>`}
            </td>
          </tr>`;
        }).join("")}
      </tbody>
    </table>

    <div style="margin-top:24px">
      <button class="btn btn-primary" onclick="startQuizTransversal()">🧩 Quiz transversal sur les formules filtrées</button>
    </div>
    <div id="quiz-transversal" style="margin-top:16px"></div>
  `;
}

let _formFilters = { memoriser: false, nonmaitrises: false };

function toggleFormFilter(name) {
  _formFilters[name] = !_formFilters[name];
  const btn = document.getElementById("btn-" + name);
  btn.className = "btn " + (_formFilters[name] ? "btn-primary" : "btn-ghost");
  filterFormulaire();
}

function filterFormulaire() {
  const search = document.getElementById("form-search").value.toLowerCase();
  const domaine = document.getElementById("form-domaine").value;
  const rows = document.querySelectorAll("#form-table tbody tr");
  let count = 0;
  rows.forEach(row => {
    const matchSearch = !search || row.dataset.desc.includes(search);
    const matchDomaine = !domaine || row.dataset.domaine === domaine;
    const matchMemoriser = !_formFilters.memoriser || row.dataset.donnee === "false";
    const matchNonMaitrises = !_formFilters.nonmaitrises || row.dataset.mastered === "false";
    const show = matchSearch && matchDomaine && matchMemoriser && matchNonMaitrises;
    row.style.display = show ? "" : "none";
    if (show) count++;
  });
  document.getElementById("form-count").textContent = `${count} formule${count > 1 ? "s" : ""} affichée${count > 1 ? "s" : ""}`;
}

function startQuizTransversal() {
  const rows = [...document.querySelectorAll("#form-table tbody tr")]
    .filter(r => r.style.display !== "none");
  const ids = rows.map(r => {
    // Extraire l'id depuis le data-attribute n'est pas disponible ici — chercher par latex
    const latexCell = r.cells[0]?.textContent?.replace(/^\$|\$$/g, "").trim();
    return window.DATA.formules.find(f => f.latex === latexCell)?.id;
  }).filter(Boolean);

  const formules = window.DATA.formules.filter(f => ids.includes(f.id) && !f.donnee);
  if (!formules.length) {
    document.getElementById("quiz-transversal").innerHTML =
      `<p class="text-muted">Aucune formule à mémoriser dans la sélection actuelle.</p>`;
    return;
  }
  _quizSession = { themeId: "transversal", queue: shuffle(formules), index: 0, correct: 0, total: 0 };
  document.getElementById("quiz-transversal").innerHTML = `
    <div id="quiz-question"></div>
    <div id="quiz-next" style="display:none;margin-top:12px">
      <button class="btn btn-primary" onclick="nextQuizQuestion()">Suivante →</button>
    </div>
    <div id="quiz-results" style="display:none"></div>`;
  nextQuizQuestion();
  document.addEventListener("quizAnswer", onQuizAnswer, { once: false });
}
```

- [ ] **Étape 12.2 : Ajouter un data-id aux lignes de table (correction du quiz transversal)**

Modifier la génération du `<tr>` dans `renderFormulaire()` — ajouter `data-id="${f.id}"` :

```js
return `<tr data-id="${f.id}" data-domaine="${f.domaine}" ...>
```

Et corriger `startQuizTransversal()` :
```js
const ids = rows.map(r => r.dataset.id).filter(Boolean);
```

- [ ] **Étape 12.3 : Vérifier dans le navigateur**

Naviguer vers `#/formulaire`. Vérifier :
- Toutes les formules en tableau avec KaTeX
- Filtre par domaine fonctionne
- Filtre "À mémoriser" masque les ✅
- Recherche texte filtre par description
- Bouton "Quiz transversal" lance un quiz sur les formules visibles

- [ ] **Étape 12.4 : Commit**

```bash
git add app/views/formulaire.js
git commit -m "feat: implement full formulaire view with filters and transversal quiz"
```

---

## Task 13 : views/progression.js — Bilan et reset

**Files :**
- Modify : `app/views/progression.js`

- [ ] **Étape 13.1 : Implémenter renderProgression()**

```js
function renderProgression() {
  const { themes, formules } = window.DATA;
  const formulesAMem = formules.filter(f => !f.donnee);
  const totalMaitrisees = formulesAMem.filter(f => Storage.isMastered(f.id)).length;
  const total = formulesAMem.length;
  const pctGlobal = total ? Math.round(totalMaitrisees / total * 100) : 0;

  return `
    <h1>Ma progression</h1>
    <div class="card" style="margin-bottom:24px;text-align:center;padding:24px">
      <div style="font-size:48px;font-weight:700;color:var(--bleu)">${totalMaitrisees}</div>
      <div class="text-muted">formules maîtrisées sur ${total}</div>
      <div class="progress-bar" style="margin:12px 0;height:10px">
        <div class="progress-fill vert" style="width:${pctGlobal}%"></div>
      </div>
      <div class="text-muted text-sm">${pctGlobal}% du formulaire maîtrisé</div>
      <button class="btn btn-danger" style="margin-top:16px"
        onclick="if(confirm('Réinitialiser toute la progression ?')) { Storage.resetAll(); window.location.reload(); }">
        🗑️ Tout réinitialiser
      </button>
    </div>

    <h2 style="margin-bottom:12px">Par thème</h2>
    <div class="progression-grid">
      ${themes.map(t => {
        const themeFormules = formulesAMem.filter(f => f.themeId === t.id);
        const done = themeFormules.filter(f => Storage.isMastered(f.id)).length;
        const pct = themeFormules.length ? Math.round(done / themeFormules.length * 100) : 100;
        const color = pct >= 75 ? "vert" : pct >= 40 ? "orange" : "rouge";
        return `
          <div class="progression-cell">
            <div class="flex justify-between items-center" style="margin-bottom:6px">
              <span class="badge badge-${t.intensite}" style="font-size:11px">${t.id}</span>
              <span class="text-muted text-sm">${done}/${themeFormules.length}</span>
            </div>
            <div class="text-sm" style="margin-bottom:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${t.nom}</div>
            <div class="progress-bar">
              <div class="progress-fill ${color}" style="width:${pct}%"></div>
            </div>
            ${themeFormules.length > 0 ? `
              <button class="btn btn-ghost" style="margin-top:8px;font-size:11px;padding:4px 8px"
                onclick="if(confirm('Reset ${t.id} ?')) { Storage.resetTheme('${t.id}'); window.location.reload(); }">
                Reset
              </button>` : ""}
          </div>`;
      }).join("")}
    </div>
  `;
}
```

- [ ] **Étape 13.2 : Vérifier dans le navigateur**

Naviguer vers `#/progression`. Vérifier :
- Total global affiché
- Grille 30 thèmes avec barres de progression
- Bouton "Reset" par thème avec confirmation
- Bouton "Tout réinitialiser" avec confirmation
- Après reset, les barres reviennent à 0

- [ ] **Étape 13.3 : Commit**

```bash
git add app/views/progression.js
git commit -m "feat: implement progression view with per-theme reset"
```

---

## Task 14 : Mode jour/nuit — Toggle thème clair/sombre

**Files :**
- Modify : `index.html` (bouton toggle dans la nav)
- Modify : `app/style.css` (variables thème clair + classe `.light`)
- Create : `app/theme.js` (persistance du thème en localStorage)

- [ ] **Étape 14.1 : Ajouter les variables thème clair dans style.css**

Ajouter à la fin du bloc `:root` existant, puis ajouter le bloc `.light` :

```css
/* Thème clair — surcharge les variables root quand body a la classe .light */
body.light {
  --bg: #f6f8fa;
  --bg2: #ffffff;
  --bg3: #eaeef2;
  --border: #d0d7de;
  --text: #1f2328;
  --text2: #656d76;
  --rouge: #cf222e;
  --orange: #bc4c00;
  --jaune: #9a6700;
  --vert: #1a7f37;
  --bleu: #0969da;
  --violet: #8250df;
}

body.light #nav {
  background: #ffffff;
  border-bottom: 1px solid #d0d7de;
  box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}

body.light .quiz-option {
  background: #ffffff;
  border-color: #d0d7de;
}

body.light .quiz-option:hover {
  border-color: var(--bleu);
  background: #f0f6ff;
}

body.light .jeton {
  background: #eaeef2;
  border-color: #d0d7de;
}

#theme-toggle {
  margin-left: auto;
  background: none;
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 4px 12px;
  cursor: pointer;
  color: var(--text2);
  font-size: 13px;
  transition: border-color 0.15s, color 0.15s;
}
#theme-toggle:hover { color: var(--text); border-color: var(--text2); }
```

- [ ] **Étape 14.2 : Créer app/theme.js**

```js
const Theme = (() => {
  const KEY = "capet_theme";

  function apply(mode) {
    document.body.classList.toggle("light", mode === "light");
    const btn = document.getElementById("theme-toggle");
    if (btn) btn.textContent = mode === "light" ? "🌙 Nuit" : "☀️ Jour";
  }

  function init() {
    const saved = localStorage.getItem(KEY) || "dark";
    apply(saved);
  }

  function toggle() {
    const current = document.body.classList.contains("light") ? "light" : "dark";
    const next = current === "light" ? "dark" : "light";
    localStorage.setItem(KEY, next);
    apply(next);
  }

  return { init, toggle };
})();
```

- [ ] **Étape 14.3 : Modifier index.html — ajouter le bouton et le script theme.js**

Dans la balise `<nav>`, ajouter le bouton avant la fermeture `</nav>` :

```html
<button id="theme-toggle" onclick="Theme.toggle()">☀️ Jour</button>
```

Ajouter le `<script src="app/theme.js"></script>` **avant** `app/router.js` dans la liste des scripts.

Ajouter l'appel `Theme.init()` au tout début du script `router.js`, dans le listener `DOMContentLoaded` :

```js
window.addEventListener("DOMContentLoaded", () => {
  Theme.init();  // ← ajouter cette ligne
  if (!window.location.hash) window.location.hash = "#/accueil";
  navigate();
});
```

- [ ] **Étape 14.4 : Vérifier dans le navigateur**

Ouvrir `index.html`. Vérifier :
- Bouton "☀️ Jour" visible dans la nav à droite
- Clic → mode clair activé, fond blanc, textes sombres, bouton devient "🌙 Nuit"
- Re-clic → retour au mode sombre
- Rechargement → le mode choisi est conservé (localStorage)
- Toutes les vues (accueil, thèmes, quiz) lisibles dans les deux modes

- [ ] **Étape 14.5 : Vérifier que l'app fonctionne via HTTP local (golden path)**

```bash
python -m http.server 8080
```

Ouvrir `http://localhost:8080`. Tester :
1. Accueil → suggestion visible, points aveugles listés
2. Clic "Commencer →" → vue thème T02
3. Onglet Formules → tableau KaTeX rendu
4. Onglet Quiz → question QCM + feedback → question suivante → score final
5. Onglet Sujets → liste des épreuves → bouton "Lire" charge le sujet
6. `#/themes` → filtre "🔴 Prioritaires" fonctionne
7. `#/formulaire` → filtre "À mémoriser" + quiz transversal
8. `#/progression` → grille 30 thèmes, reset par thème
9. Toggle jour/nuit → toutes les vues lisibles dans les deux modes

- [ ] **Étape 14.6 : Commit**

```bash
git add app/theme.js app/style.css index.html app/router.js
git commit -m "feat: add light/dark mode toggle with localStorage persistence"
```

---

## Récapitulatif des commits

| Tâche | Commit |
|---|---|
| Task 1 | `feat: add build.py and generated data.js` |
| Task 2 | `feat: add SPA shell with nav and base styles` |
| Task 3 | `feat: add hash router and view stubs` |
| Task 4 | `feat: add localStorage storage abstraction` |
| Task 5 | `feat: implement accueil intelligent with priority suggestion` |
| Task 6 | `feat: implement themes list with filter` |
| Task 7 | `feat: implement theme view with fiche and formules tabs` |
| Task 8 | `feat: implement QCM quiz engine with distractors` |
| Task 9 | `feat: implement fill-in-the-blank quiz engine` |
| Task 10 | `feat: implement quiz session with QCM and fill-in-the-blank alternation` |
| Task 11 | `feat: implement sujets tab with markdown fetch and display` |
| Task 12 | `feat: implement full formulaire view with filters and transversal quiz` |
| Task 13 | `feat: implement progression view with per-theme reset` |
| Task 14 | `feat: add light/dark mode toggle with localStorage persistence` |
