# App de révision CAPET — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construire une PWA hors-ligne d'entraînement au rappel actif sur trois objets — formules, schémas, conditions d'application — alimentée automatiquement par les sources LaTeX/Markdown existantes du projet.

**Architecture:** Un script Python (`build_cards.py`) parse les 30 `fiches/T{nn}_contenu.md` et les 30 `fiches/T{nn}_*.tex`, en extrait des cartes typées et produit `app/cards.json`. Un second script (`build_svg.py`) compile chaque environnement TikZ/circuitikz isolé en SVG vectoriel via `latex` + `dvisvgm`, avec post-traitement des couleurs pour le thème sombre. Le front est du vanilla JS sans build step : modules ES chargés directement, `localStorage` pour la progression, KaTeX pour les formules. Les sources LaTeX restent l'unique source de vérité ; l'app est un artefact régénérable.

**Tech Stack:** Python 3 (stdlib seule — `re`, `json`, `pathlib`, `subprocess`, `hashlib`), `pytest` pour les tests du parseur, `latex` + `dvisvgm` (déjà installés, vérifiés), vanilla JS ES modules, KaTeX 0.16.9 (vendored local, pas de CDN — l'app doit être hors-ligne), CSS custom properties.

**Spec:** Ce plan est sa propre spec — il est issu de la session de cadrage du 2026-09-21 (brainstorm-personas), dont les décisions utilisateur sont reportées dans « Décisions de cadrage » ci-dessous.

## Décisions de cadrage (verrouillées, ne pas réinterpréter)

1. **Échéance** : écrit mars 2026, ~30 min/jour → la répétition espacée est pertinente ; la file quotidienne vise ~30 cartes.
2. **Format par défaut** : révélation + auto-notation (`su` / `hésité` / `raté`). Le QCM à 4 options est une **bascule secondaire**, pas le cœur.
3. **Source du contenu** : extraction automatique depuis les sources. Aucune rédaction manuelle de contenu pédagogique. Zéro duplication.
4. **Schémas** : trois niveaux d'entraînement (reconnaissance / calcul / tracé), le niveau étant une propriété de la carte.
5. **Conditions d'application** : présentes **à la fois** au verso des cartes formule **et** comme cartes piège autonomes.
6. **Les encadrés jury ne sont PAS importés en v1** (audit de véracité 2026-09-20 : 54 % de citations défectueuses). Interdiction absolue d'extraire la section `## 3. ATTENTES DU JURY`.

## Défauts corrigés avant publication (revue adverse du 2026-09-21)

Ce plan a été soumis à une relecture adverse qui a exécuté son code contre les
30 fiches réelles. **16 défauts ont été trouvés et corrigés.** Les pièges
ci-dessous sont documentés dans leur task ; ne pas les réintroduire en
« simplifiant » le code.

| # | Task | Défaut | Impact évité |
|---|---|---|---|
| 1 | 1 | Colonne « Formule » supposée en position 2 | 107/191 formules faussées **silencieusement** |
| 2 | 3 | Un seul des 3 formats de section 5 géré | 8 pièges extraits sur 199 (−96 %) |
| 3 | 4 | `[^}]*` cassé par les accolades imbriquées (T20) | domaine vide, le plan se bloquait sur sa propre Task 4 |
| 4 | 2 | Marqueur `pour ` trop large | 97 lignes de prose prises pour des conditions |
| 5 | 1 | `split("\|")` naïf sur `$\|Z\|$` | 3 cartes dont le verso était le caractère `$` |
| 6 | 1/7 | Colonne « Fréquence » ignorée | 114 pondérations par formule perdues |
| 7 | 6/10 | `var(--svg-bg)` sans fallback dans un `<img>` | schémas peints en noir, **même en thème clair** |
| 8 | 10 | 26 labels contiennent du LaTeX inline | affiché en source brute au recto |
| 9 | 8 | Intervalles non plafonnés | carte hors horizon dès la 6ᵉ réussite (174 j) |
| 10 | 8 | Échues toujours prioritaires | famine des cartes neuves dès 30 échues |
| 11 | 12 | `SEUIL_FACILITE` = facilité initiale | un « hésité » annulait la maîtrise |
| 12 | 11 | Carte ratée renotée au 2ᵉ passage | la reprise pénalisait au lieu d'aider |
| 13 | 7 | `--sans-svg` émettait des cartes sans image | 31 images cassées en mode itération |
| 14 | 13 | SVG et polices absents du précache | hors-ligne non fonctionnel (test non déterministe) |
| 15 | 3 | Gras Markdown résiduel | `**` affichés littéralement sur 13 cartes |
| 16 | 6 | `.gitignore` créé 8 tasks trop tard | artefacts régénérables committés |

**État de validation à la publication** : les parseurs des Tasks 1, 3 et 4 ont
été exécutés sur les 30 fiches → **191 formules tableau, 153 formules bloc,
199 pièges, 30 jeux de métadonnées, 0 anomalie**. La chaîne SVG a compilé un
montage ALI réel, vérifié visuellement.

## Global Constraints

- **Python 3 stdlib uniquement** pour les scripts de build. Pas de `pip install`. `pytest` est la seule dépendance de test.
- **Aucune requête réseau à l'exécution de l'app.** KaTeX est vendored dans `app/vendor/`. Pas de CDN, pas de Google Fonts.
- **Pas de build step JS.** Pas de npm, pas de bundler, pas de TypeScript. Modules ES natifs chargés par `<script type="module">`.
- **Le contenu pédagogique n'est jamais écrit à la main dans le code.** Toute chaîne de contenu provient de `cards.json`. Un test le vérifie (Task 12).
- **Décimales françaises** dans tout contenu affiché : `0,85` et non `0.85`. Les sources respectent déjà cette règle ; le parseur ne doit pas la casser.
- **`fiches/` et `exercices/` sont en lecture seule** pour ce projet. Aucun script de ce plan n'écrit dans ces dossiers. Seuls `app/`, `scripts/` et `tests/` sont modifiables.
- **Encodage UTF-8 explicite partout** (`encoding="utf-8"` à chaque `open()`). Windows par défaut ouvre en cp1252 et corromprait les accents.
- **Chemins** : les scripts s'exécutent depuis la racine du repo et résolvent les chemins via `pathlib.Path(__file__).resolve().parents[1]`. Jamais de chemin absolu codé en dur.
- Plateforme de développement : Windows 11, shell Git Bash disponible. Les commandes de test sont données en syntaxe POSIX.
- **Cible d'usage : iPhone, PWA ajoutée à l'écran d'accueil.** Trois conséquences non négociables :
  - Les balises `apple-mobile-web-app-*` sont obligatoires (Safari ignore `display: standalone` du manifeste) ; sans elles l'app garde la barre Safari.
  - Safari **purge les données d'un site non visité pendant 7 jours** (ITP). Une PWA *installée sur l'écran d'accueil* y échappe, mais pas une simple page ouverte dans Safari. C'est la raison principale pour laquelle l'export JSON de la Task 9 est en v1 et non en v2.
  - Pas de notification push (hors iOS 16.4+ et hors périmètre) : l'app ne peut pas rappeler de réviser. C'est assumé.

## Structure de fichiers

| Fichier | Responsabilité |
|---|---|
| `scripts/parse_formules.py` | Extraire les cartes formule des deux formats (tableau MD + bloc `$$`) |
| `scripts/parse_pieges.py` | Extraire les cartes piège de la section 5 |
| `scripts/parse_meta.py` | Extraire titre/domaine/présence `n/13` des `.tex` |
| `scripts/extract_tikz.py` | Isoler les environnements TikZ des `.tex` |
| `scripts/build_svg.py` | Compiler TikZ → SVG thémable (orchestre `extract_tikz`) |
| `scripts/build_cards.py` | Orchestrateur : assemble tout en `app/cards.json` |
| `app/index.html` | Coquille HTML unique, PWA |
| `app/js/store.js` | Persistance `localStorage`, export/import JSON |
| `app/js/scheduler.js` | Algorithme SM-2 simplifié pondéré par la fréquence |
| `app/js/card-render.js` | Rendu d'une carte selon son type |
| `app/js/views/reviser.js` | Écran file quotidienne |
| `app/js/views/priorites.js` | Écran grille fréquence × maîtrise |
| `app/js/views/reglages.js` | Écran export/import/reset |
| `app/js/app.js` | Routeur hash + amorçage |
| `app/css/style.css` | Thème clair/sombre via custom properties |
| `app/sw.js` | Service worker (cache-first) |
| `app/manifest.webmanifest` | Manifeste PWA |

---

### Task 1: Parseur des formules — format tableau Markdown

**Files:**
- Create: `scripts/parse_formules.py`
- Test: `tests/test_parse_formules.py`

**Interfaces:**
- Produces: `parse_table_formulas(section_text: str, theme_id: str) -> list[dict]` — chaque dict a les clés `type` (`"formule"`), `theme`, `label`, `latex`, `unites`, `frequence`, `conditions` (str, vide ici), `source_format` (`"table"`).

**⚠ Piège central de cette task — les colonnes ne sont PAS à position fixe.**

Mesure faite sur les 30 fiches réelles : **107 formules sur 191 ont la formule en colonne 1**, et 78 en colonne 2. Deux schémas d'en-tête coexistent :

```
| Grandeur / Loi | Formule | Unité |            <- formule en colonne 2 (22 fiches)
| Formule LaTeX | Contexte | Fréquence | Source |  <- formule en colonne 1 (T06-T13)
```

Un parseur qui prendrait toujours la colonne 2 extrairait le *contexte* au lieu de la formule pour 58 % du corpus — et **silencieusement**, en produisant des cartes d'apparence plausible mais fausses. C'est le défaut le plus dangereux de tout ce plan.

**La solution obligatoire** : lire la ligne d'en-tête du tableau et en déduire l'index de chaque colonne. Un tableau sans colonne « Formule » dans son en-tête n'est pas un tableau de formules (ex. `| Technologie | Tension nominale | Énergie massique |`, `| Quadrant | Couple | Vitesse | Mode |`) et doit être **ignoré entièrement**.

**Bonus à ne pas perdre** : 114 formules portent une colonne `Fréquence` propre (`Très fréquent`, `Systématique`…). C'est une pondération plus fine que le poids de thème ; elle est conservée dans le champ `frequence`.

Exemple réel de `fiches/T01_contenu.md` (colonne 2) :

```
| Grandeur / Loi | Formule | Unité |
|----------------|---------|-------|
| Loi d'Ohm (résistif) | $u = R \cdot i$ | V, Ω, A |
```

Exemple réel de `fiches/T08_contenu.md` (colonne 1) :

```
| Formule LaTeX | Contexte | Fréquence | Source |
|---------------|----------|-----------|--------|
| $\bar{U}_{PD2} = \dfrac{2\sqrt{2}V}{\pi}$ | Redresseur monophasé PD2 | Très fréquent | 2019 |
```

- [ ] **Step 1: Write the failing test**

```python
# tests/test_parse_formules.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_parse_formules.py -v`
Expected: FAIL avec `ModuleNotFoundError: No module named 'scripts.parse_formules'`

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/parse_formules.py
"""Extraction des cartes formule depuis les fichiers T{nn}_contenu.md."""

import re

_SEP = re.compile(r"^[\s|:\-]+$")

# Mots-clés de reconnaissance des colonnes, testés sur la ligne d'en-tête.
_CLE_LABEL = ("grandeur", "loi", "contexte", "paramètre", "parametre", "nom")
_CLE_UNITE = ("unité", "unite")
_CLE_FREQ = ("fréquence", "frequence")


def _cellules(ligne: str) -> list[str]:
    """Découpe une ligne de tableau en respectant les segments math.

    Un `split("|")` naïf casse `$|\\underline{Z}| = \\sqrt{R^2}$` (module
    d'une impédance, T03) : les barres verticales de la notation « module »
    sont prises pour des séparateurs de colonnes. Résultat sans cette garde :
    une carte dont le verso est le seul caractère `$`.
    """
    contenu = ligne.strip().strip("|")
    parts: list[str] = []
    buf: list[str] = []
    dans_math = False
    for ch in contenu:
        if ch == "$":
            dans_math = not dans_math
            buf.append(ch)
        elif ch == "|" and not dans_math:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf))
    return [p.strip() for p in parts]


def _strip_math(s: str) -> str:
    """Retire les délimiteurs $...$ autour d'une formule.

    Uniquement quand la cellule est UN seul segment math. Une cellule comme
    `$R = U^2/P$ (charge purement résistive)` en contient deux morceaux :
    retirer le premier et le dernier `$` produirait du LaTeX invalide.
    """
    s = s.strip()
    if s.count("$") == 2 and s.startswith("$") and s.endswith("$"):
        return s[1:-1].strip()
    return s


def _clean_unit(s: str) -> str:
    """Le tiret cadratin signifie 'sans unité'."""
    s = s.strip()
    return "" if s in {"—", "-", "–", "", "sans unité"} else s


def _indices(entete: list[str]) -> dict | None:
    """Déduit la position de chaque colonne depuis la ligne d'en-tête.

    Retourne None si le tableau n'a pas de colonne « Formule » : ce n'est
    alors pas un tableau de formules (tableau de technologies, de quadrants,
    de caractéristiques…) et il doit être ignoré entièrement.
    """
    bas = [c.lower() for c in entete]
    i_formule = next((i for i, c in enumerate(bas) if "formule" in c), None)
    if i_formule is None:
        return None

    def cherche(cles, exclure):
        return next(
            (i for i, c in enumerate(bas)
             if i != exclure and any(k in c for k in cles)),
            None,
        )

    i_label = cherche(_CLE_LABEL, i_formule)
    if i_label is None:
        # Pas de colonne descriptive nommée : on prend la colonne voisine.
        i_label = 1 if i_formule == 0 and len(bas) > 1 else (0 if i_formule > 0 else None)

    return {
        "formule": i_formule,
        "label": i_label,
        "unite": cherche(_CLE_UNITE, i_formule),
        "freq": cherche(_CLE_FREQ, i_formule),
    }


def parse_table_formulas(section_text: str, theme_id: str) -> list[dict]:
    """Extrait les formules écrites sous forme de tableau Markdown.

    Les colonnes sont localisées par la ligne d'en-tête, JAMAIS par position
    fixe : le corpus mélange `| Grandeur | Formule | Unité |` (formule en
    colonne 2) et `| Formule LaTeX | Contexte | Fréquence | Source |`
    (formule en colonne 1). Supposer une position fixe corrompt 58 % du
    corpus sans lever d'erreur.
    """
    cards = []
    idx = None

    for ligne in section_text.splitlines():
        ligne = ligne.rstrip()
        if not ligne.startswith("|") or _SEP.match(ligne):
            continue

        cells = _cellules(ligne)

        # Une ligne sans $ est une ligne d'en-tête : elle (re)définit le schéma.
        if "$" not in ligne:
            idx = _indices(cells)
            continue

        if idx is None:
            continue  # tableau sans colonne Formule : ignoré

        def col(nom: str) -> str:
            i = idx[nom]
            return cells[i] if i is not None and i < len(cells) else ""

        latex = col("formule")
        if "$" not in latex:
            continue

        cards.append({
            "type": "formule",
            "theme": theme_id,
            "label": col("label"),
            "latex": _strip_math(latex),
            "unites": _clean_unit(col("unite")),
            "frequence": col("freq"),
            "conditions": "",
            "source_format": "table",
        })
    return cards
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_parse_formules.py -v`
Expected: PASS (5 tests)

- [ ] **Step 5: Vérifier sur les données réelles — les DEUX schémas de colonnes**

Sous Windows, forcer la sortie UTF-8 : la console est en cp1252 et un `print`
d'un caractère `Ω` lève `UnicodeEncodeError`, ce qui ferait croire à tort à un
bug du parseur.

Run:
```bash
PYTHONIOENCODING=utf-8 python -c "
import sys, pathlib, re; sys.path.insert(0,'.')
from scripts.parse_formules import parse_table_formulas
S1 = re.compile(r'^## 1\..*?(?=^## 2\.|\Z)', re.S|re.M)
tot = fq = sans_label = 0
for f in sorted(pathlib.Path('fiches').glob('T*_contenu.md')):
    m = S1.search(f.read_text(encoding='utf-8'))
    if not m: continue
    for c in parse_table_formulas(m.group(0), f.name[:3]):
        tot += 1
        fq += 1 if c['frequence'] else 0
        sans_label += 0 if c['label'] else 1
print('total:', tot, '| avec frequence:', fq, '| sans label:', sans_label)
# Controle cible du schema colonne 1 (T08) :
t = pathlib.Path('fiches/T08_contenu.md').read_text(encoding='utf-8')
c = parse_table_formulas(S1.search(t).group(0), 'T08')[0]
print('T08 premiere carte -> label:', repr(c['label']))
print('                      latex:', repr(c['latex'][:40]))
"
```
Expected exactement : `total: 191 | avec frequence: 114 | sans label: 0`.

Puis, pour T08, le `label` doit être un **contexte lisible** (`'Tension moyenne redresseur mon...'`) et le `latex` doit commencer par une commande LaTeX (`'\\bar{U}_{PD2} = ...'`). **Si le label contient du LaTeX et le champ latex du texte français, la détection de colonnes est inversée** — c'est le bug que cette task existe pour empêcher. Ne pas continuer sans l'avoir corrigé.

- [ ] **Step 6: Commit**

```bash
git add scripts/parse_formules.py tests/test_parse_formules.py
git commit -m "feat(build): parseur des formules au format tableau Markdown"
```

---

### Task 2: Parseur des formules — format bloc `$$` avec conditions

**Files:**
- Modify: `scripts/parse_formules.py`
- Test: `tests/test_parse_formules.py`

**Interfaces:**
- Consumes: rien de Task 1 (fonction sœur indépendante).
- Produces: `parse_block_formulas(section_text: str, theme_id: str) -> list[dict]` — mêmes clés que Task 1, avec `source_format = "bloc"` et `conditions` renseigné depuis le texte suivant la formule.

Contexte : 10 fiches (T14, T19, T22, T23, T24, T25, T27 notamment) utilisent des blocs `$$`. Le heading `### 1.2 Montage inverseur` donne le label. Le texte qui suit porte les conditions. Exemple réel de `fiches/T19_contenu.md` :

```
### 1.5 Montage soustracteur (différentiel)
$$V_s = \frac{R_2}{R_1}(V_2 - V_1) \quad \text{si les quatre résistances sont appariées}$$

Utilisé pour amplifier une tension différentielle.
```

**Règle de capture des conditions.** On prend les lignes non vides suivant le bloc `$$`, jusqu'au prochain heading `###` ou au prochain `$$`, en ne gardant que celles qui portent un marqueur de condition (`si `, `valable`, `à condition`, `hypothèse`, `uniquement`, `lorsque`, `en régime`, `condition`), puis on écarte trois formes de bruit : plus de 200 caractères (paragraphe avalé), fin par `:` (amorce de paragraphe), présence de `Source :` / `Exemple` (métadonnée).

**⚠ `pour ` est volontairement exclu des marqueurs.** Mesure sur le corpus : il capture à lui seul **97 lignes de prose sur 138** — « Pour une installation comportant plusieurs récepteurs… », « pour $f = 50$ Hz », « pour diminuer le courant ». Avec lui, 35 des 45 conditions extraites sont du bruit ; sans lui, il en reste 7 avant filtrage et **0 après**. Ne pas le réintroduire en voyant le faible rendement.

**Rendement attendu, et pourquoi c'est acceptable.** Ce parseur ne produit que **~10 conditions sur 153 blocs**, parce que les fiches n'énoncent presque jamais les conditions à côté de la formule. C'est un constat de source, pas un défaut d'implémentation : le vrai gisement de conditions d'application est la **section 5**, exploitée par la Task 3 (199 cartes piège). Les conditions extraites ici sont un bonus attaché au verso des formules ; l'axe « conditions d'application » de la v1 repose sur les cartes piège.

- [ ] **Step 1: Write the failing test**

```python
# à ajouter dans tests/test_parse_formules.py
from scripts.parse_formules import parse_block_formulas

BLOCS = """## 1. FORMULES ET COURS

### 1.2 Montage inverseur
$$\\frac{V_s}{V_e} = -\\frac{R_2}{R_1}$$

Gain en tension : inversion de phase.

### 1.5 Montage soustracteur
$$V_s = \\frac{R_2}{R_1}(V_2 - V_1)$$

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

AMORCE = """## 1. FORMULES ET COURS

### 1.1 AOP idéal
$$\\varepsilon = 0$$

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

GRAS = """## 1. FORMULES ET COURS

### 1.1 AOP idéal
$$\\varepsilon = 0$$

**Condition de fonctionnement linéaire :** la sortie est rebouclée sur l'entrée.
"""

def test_marques_de_gras_retirees_des_conditions():
    c = parse_block_formulas(GRAS, "T19")[0]
    assert "**" not in c["conditions"]
    assert "rebouclée" in c["conditions"]

def test_frequence_vide_pour_les_blocs():
    assert parse_block_formulas(BLOCS, "T19")[0]["frequence"] == ""
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_parse_formules.py -v -k block`
Expected: FAIL avec `ImportError: cannot import name 'parse_block_formulas'`

- [ ] **Step 3: Write minimal implementation**

```python
# à ajouter dans scripts/parse_formules.py

_HEADING = re.compile(r"^###\s+(?:\d+\.\d+\s+)?(?P<titre>.+?)\s*$")
_BLOCK = re.compile(r"^\$\$(?P<latex>.*?)\$\$\s*$", re.S)

# « pour » est VOLONTAIREMENT absent : mesuré sur le corpus, il capture à lui
# seul 97 lignes de prose sur 138 (« Pour une installation comportant… »,
# « pour $f = 50$ Hz », « pour diminuer le courant ») et fait passer le bruit
# de 7 à 35 captures. Ne pas le rajouter.
_MARQUEURS = (
    "si ", "valable", "à condition", "hypothèse", "hypothèses",
    "uniquement", "lorsque", "en régime", "condition",
)

# Une « condition » qui cite une source ou se termine par « : » est en fait
# une métadonnée ou une amorce de paragraphe, pas une condition.
_REJETS = ("source :", "source directe", "exemple", "résultat imposé")
_LONGUEUR_MAX = 200


def _nettoyer(ligne: str) -> str:
    """Retire puces et marques de gras d'une condition.

    `lstrip("*- ")` seul laisse le `**` FERMANT : sur « **Attention** : … »
    il produit « Attention** : … », affiché tel quel par echapper(). On retire
    donc la puce par regex, puis les paires de gras.
    """
    s = re.sub(r"^\s*[-*]+\s*", "", ligne.strip())
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    return s.replace("**", "").strip()


def _est_condition(ligne: str) -> bool:
    """Vrai si la ligne énonce une condition d'application exploitable."""
    s = _nettoyer(ligne)
    bas = s.lower()

    if len(s) > _LONGUEUR_MAX:
        return False                      # paragraphe entier, pas une condition
    if s.rstrip().endswith(":"):
        return False                      # amorce de paragraphe
    if any(r in bas for r in _REJETS):
        return False                      # métadonnée de source

    return any(bas.startswith(m) or f" {m}" in bas for m in _MARQUEURS)


def parse_block_formulas(section_text: str, theme_id: str) -> list[dict]:
    """Extrait les formules écrites en blocs $$ ... $$.

    Le label provient du heading `###` courant, privé de sa numérotation.
    Les conditions proviennent des lignes suivant le bloc qui portent un
    marqueur de condition ; la prose descriptive est écartée.
    """
    lignes = section_text.splitlines()
    cards = []
    label_courant = ""

    i = 0
    while i < len(lignes):
        ligne = lignes[i].rstrip()

        h = _HEADING.match(ligne)
        if h:
            label_courant = h.group("titre").strip()
            i += 1
            continue

        if ligne.startswith("$$"):
            # Bloc sur une ligne, ou multi-lignes jusqu'au $$ fermant.
            if ligne.endswith("$$") and len(ligne) > 4:
                latex = ligne[2:-2].strip()
                j = i + 1
            else:
                buf = [ligne[2:]]
                j = i + 1
                while j < len(lignes) and not lignes[j].rstrip().endswith("$$"):
                    buf.append(lignes[j])
                    j += 1
                if j < len(lignes):
                    buf.append(lignes[j].rstrip()[:-2])
                    j += 1
                latex = "\n".join(buf).strip()

            # Conditions : lignes suivantes jusqu'au prochain heading ou bloc.
            conditions = []
            k = j
            while k < len(lignes):
                suite = lignes[k].rstrip()
                if suite.startswith("###") or suite.startswith("$$") or suite.startswith("## "):
                    break
                if suite.strip() and _est_condition(suite):
                    conditions.append(_nettoyer(suite))
                k += 1

            if latex:
                cards.append({
                    "type": "formule",
                    "theme": theme_id,
                    "label": label_courant or "(sans titre)",
                    "latex": latex,
                    "unites": "",
                    "frequence": "",
                    "conditions": " ".join(conditions),
                    "source_format": "bloc",
                })
            i = j
            continue

        i += 1

    return cards
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_parse_formules.py -v`
Expected: PASS (11 tests au total)

- [ ] **Step 5: Vérifier sur T19 réel**

Run:
```bash
python -c "
import sys, pathlib, re; sys.path.insert(0,'.')
from scripts.parse_formules import parse_block_formulas
t = pathlib.Path('fiches/T19_contenu.md').read_text(encoding='utf-8')
sec = re.search(r'## 1\..*?(?=^## 2\.)', t, re.S|re.M).group(0)
for c in parse_block_formulas(sec, 'T19')[:4]:
    print('-', c['label'], '||', c['latex'][:50], '|| cond:', c['conditions'][:60])
"
```
Expected: au moins 4 formules avec des labels lisibles (`Modèle de l'AOP idéal...`, `Montage inverseur`, …).

- [ ] **Step 6: Commit**

```bash
git add scripts/parse_formules.py tests/test_parse_formules.py
git commit -m "feat(build): parseur des formules en blocs \$\$ avec conditions"
```

---

### Task 3: Parseur des cartes piège (section 5)

**Files:**
- Create: `scripts/parse_pieges.py`
- Test: `tests/test_parse_pieges.py`

**Interfaces:**
- Produces: `parse_pieges(texte_fiche: str, theme_id: str) -> list[dict]` — clés `type` (`"piege"`), `theme`, `titre`, `piege`, `regle`, `erreur_type`.

**⚠ Piège central de cette task — la section 5 a TROIS formats distincts.**

Mesure faite sur les 30 fiches : **199 items au total**, répartis ainsi.

**Format A — sous-titres `###` (T02 seulement, 8 items)** :

```
### 5.1 Confusion entre $F_P$ et $\cos\varphi$

**Le piège** : Confondre le facteur de puissance et le facteur de déplacement.

**La distinction** :
- Si le signal est purement sinusoïdal : $F_P = \cos\varphi$.

**Erreur type** : Dans le sujet 2018, certains candidats confondaient les colonnes.
```

**Format B — liste numérotée (T01 à T17, 103 items)** :

```
1. **Signe dans la loi des mailles** : oublier de changer le signe d'une tension
   selon le sens de parcours. Toujours définir un sens avant d'écrire.

2. **Valeur efficace vs crête** : $V_{eff} = V_{max}/\sqrt{2}$ seulement pour un
   sinusoïdal pur. Pour un signal déformé, utiliser la définition intégrale.
```

**Format C — liste à puces (T18 à T30, 88 items)** :

```
- **Appliquer $V_+ = V_-$ sans vérifier la contre-réaction** : en mode comparateur,
  cette égalité est fausse.
- **Signe du gain inverseur** : oublier le signe et conclure à une amplification
  non-inverseuse.
```

Un parseur qui ne gérerait que le format A extrairait **8 pièges sur 199**, soit 4 % du gisement — en échouant silencieusement sur 29 fiches. Les formats B et C portent à eux seuls 96 % du matériau.

**Normalisation retenue.** Pour A : `piege` ← « Le piège » ; `regle` ← la première de (`La distinction`, `Règle`, `Correction`, `Méthode correcte`) présente ; `erreur_type` ← « Erreur type ». Pour B et C : `titre` ← le texte en gras ; `piege` ← la première phrase du corps ; `regle` ← le reste du corps ; `erreur_type` ← vide.

Le découpage phrase/reste pour B et C se fait au premier `. ` suivi d'une majuscule. Si le corps n'a qu'une phrase, `regle` reste vide et la carte reste utilisable (le verso affiche alors le titre et le piège).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_parse_pieges.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from scripts.parse_pieges import parse_pieges

FICHE_A = """# T02 — Puissance

## 1. FORMULES ET COURS
| a | $b$ | c |

## 5. LACUNES ET PIÈGES RÉCURRENTS

### 5.1 Confusion entre $F_P$ et $\\cos\\varphi$

**Le piège** : Confondre le facteur de puissance et le facteur de déplacement.

**La distinction** :
- Si le signal est purement sinusoïdal : $F_P = \\cos\\varphi$.

**Erreur type** : Dans le sujet 2018, des candidats confondaient les colonnes.

### 5.2 Oubli du rendement

**Le piège** : Calculer sans diviser par le rendement.

**Correction** : La formule correcte inclut $\\eta$ au dénominateur.

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

Rien ici.
"""

FICHE_B = """# T01

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Signe dans la loi des mailles** : oublier de changer le signe d'une tension. Toujours définir un sens de parcours avant d'écrire.

2. **Valeur efficace vs crête** : $V_{eff} = V_{max}/\\sqrt{2}$ seulement pour un sinusoïdal pur.

## 6. CONNEXIONS
Rien.
"""

FICHE_C = """# T19

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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_parse_pieges.py -v`
Expected: FAIL avec `ModuleNotFoundError: No module named 'scripts.parse_pieges'`

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/parse_pieges.py
"""Extraction des cartes piège depuis la section 5 des fiches.

La section 5 « LACUNES ET PIÈGES RÉCURRENTS » contient les conditions
d'application des formules, sous forme d'erreurs à éviter. C'est le
matériau des cartes de type « piege ».
"""

import re

_SECTION_5 = re.compile(r"^## 5\..*?(?=^## 6\.|\Z)", re.S | re.M)

# Format A : sous-titre ### (T02)
_H3 = re.compile(r"^###\s+(?:\d+\.\d+\s+)?(?P<titre>.+?)\s*$", re.M)
# Formats B et C : « 1. **Titre** : corps » ou « - **Titre** : corps »
_PUCE = re.compile(r"^(?:\d+\.|[-*])\s+\*\*(?P<titre>.+?)\*\*\s*:?\s*(?P<corps>.*)$")

# « Formule correcte » est un libellé réel de T02, absent d'une première
# lecture rapide : sans lui, la règle de ce piège reste vide.
_ALIAS_REGLE = ("La distinction", "Règle", "Correction", "Méthode correcte",
                "Formule correcte")

# Le lookahead de _champ doit s'arrêter sur un LIBELLÉ de champ, pas sur
# n'importe quel gras : sinon « ...valeur efficace du **fondamental** $I_1$ »
# tronque le champ au milieu d'une phrase (cas réel T02).
_LIBELLES = (
    r"(?:Le piège|La distinction|Règle|Correction|Méthode correcte"
    r"|Erreur type|Formule correcte)"
)

# Fin de première phrase : un point suivi d'un espace et d'une majuscule.
_FIN_PHRASE = re.compile(r"(?<=\.)\s+(?=[A-ZÀÉÈÊÎÔÛÇ])")


def _demarquer(s: str) -> str:
    """Retire le gras Markdown résiduel d'un texte de carte.

    Les corps de pièges contiennent du gras d'emphase en milieu de phrase
    (« confondre les deux colonnes **FP** et **cos φ** »). Sans ce
    nettoyage, `echapper()` afficherait les astérisques littéralement.
    """
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    return s.replace("**", "").strip()


def _champ(bloc: str, libelle: str) -> str:
    """Récupère le texte d'un champ `**Libellé** : ...` jusqu'au champ suivant.

    La borne est `\\n**` (gras en début de ligne), et non `**` : un gras en
    milieu de phrase (« Confondre **F_P** et cos φ ») ne doit pas tronquer
    le champ.
    """
    motif = re.compile(
        r"\*\*" + re.escape(libelle) + r"\*\*\s*:?\s*(?P<val>.*?)"
        r"(?=\n\s*\*\*" + _LIBELLES + r"\*\*|\Z)",
        re.S,
    )
    m = motif.search(bloc)
    if not m:
        return ""
    val = m.group("val").strip()
    val = re.sub(r"\n\s*[-*]\s*", " ", val)   # aplatit les sous-listes
    val = re.sub(r"\s*\n\s*", " ", val)
    return _demarquer(val)


def _couper(corps: str) -> tuple[str, str]:
    """Sépare le corps en (première phrase, reste)."""
    corps = corps.strip()
    parties = _FIN_PHRASE.split(corps, maxsplit=1)
    if len(parties) == 2:
        return parties[0].strip(), parties[1].strip()
    return corps, ""


def _parse_format_h3(section: str, theme_id: str) -> list[dict]:
    positions = [(m.start(), m.group("titre")) for m in _H3.finditer(section)]
    cartes = []
    for i, (debut, titre) in enumerate(positions):
        fin = positions[i + 1][0] if i + 1 < len(positions) else len(section)
        bloc = section[debut:fin]
        regle = ""
        for alias in _ALIAS_REGLE:
            regle = _champ(bloc, alias)
            if regle:
                break
        cartes.append({
            "type": "piege", "theme": theme_id, "titre": _demarquer(titre),
            "piege": _champ(bloc, "Le piège"), "regle": regle,
            "erreur_type": _champ(bloc, "Erreur type"),
        })
    return cartes


def _parse_format_liste(section: str, theme_id: str) -> list[dict]:
    """Formats B et C : item sur une ligne, éventuellement continué.

    Une ligne qui ne commence pas par une puce ni un chiffre prolonge l'item
    courant (les sources coupent parfois un item sur deux lignes).
    """
    cartes: list[dict] = []
    courant: list[str] = []
    titre_courant = ""

    def cloturer():
        if not titre_courant:
            return
        piege, regle = _couper(_demarquer(" ".join(courant)))
        cartes.append({
            "type": "piege", "theme": theme_id, "titre": _demarquer(titre_courant),
            "piege": piege, "regle": regle, "erreur_type": "",
        })

    for ligne in section.splitlines():
        nue = ligne.strip()
        if not nue or nue.startswith("#") or nue.startswith("---"):
            continue
        m = _PUCE.match(nue)
        if m:
            cloturer()
            titre_courant = m.group("titre").strip()
            courant = [m.group("corps").strip()]
        elif titre_courant:
            courant.append(nue)
    cloturer()
    return cartes


def parse_pieges(texte_fiche: str, theme_id: str) -> list[dict]:
    """Extrait les items de la section 5 en cartes piège.

    La section 5 a trois formats dans le corpus : sous-titres ### (T02),
    liste numérotée (T01-T17) et liste à puces (T18-T30). Les trois sont
    gérés ; ne traiter que le premier ne ramènerait que 8 items sur 199.
    """
    m = _SECTION_5.search(texte_fiche)
    if not m:
        return []
    section = m.group(0)

    cartes = _parse_format_h3(section, theme_id)
    if cartes:
        return cartes
    return _parse_format_liste(section, theme_id)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_parse_pieges.py -v`
Expected: PASS (9 tests)

- [ ] **Step 5: Vérifier le volume réel sur les 30 fiches**

Run:
```bash
python -c "
import sys, pathlib; sys.path.insert(0,'.')
from scripts.parse_pieges import parse_pieges
tot=0; vides=0
for f in sorted(pathlib.Path('fiches').glob('T*_contenu.md')):
    cs = parse_pieges(f.read_text(encoding='utf-8'), f.name[:3])
    tot += len(cs)
    vides += sum(1 for c in cs if not c['piege'])
print('pieges extraits:', tot, '| sans champ piege:', vides)
"
```
Expected: **199 pièges extraits, 0 sans champ piège** (mesuré sur le corpus au 2026-09-21). Si le total tombe autour de 8, le parseur ne gère que le format A — les formats B et C sont cassés. Si des fiches remontent 0 piège, lister lesquelles et inspecter leur section 5 avant de continuer.

- [ ] **Step 6: Commit**

```bash
git add scripts/parse_pieges.py tests/test_parse_pieges.py
git commit -m "feat(build): parseur des cartes piege depuis la section 5"
```

---

### Task 4: Parseur des métadonnées de thème (`.tex`)

**Files:**
- Create: `scripts/parse_meta.py`
- Test: `tests/test_parse_meta.py`

**Interfaces:**
- Produces: `parse_meta(texte_tex: str) -> dict` — clés `code`, `titre`, `domaine`, `presence_n`, `presence_sur`, `poids`.

Contexte : chaque `fiches/T{nn}_*.tex` porte un `\ficheEntete` et une ligne de présence. Format réel observé :

```latex
\ficheEntete{T19}{AOP (amplificateur opérationnel)}{colElec}%
  {électronique - Conditionnement du signal}%
  {\textbf{Présence :} \textbf{4/13} sujets (2013-2026) - thème \emph{régulier depuis 2019}}%
```

**Deux cas particuliers réels, tous deux vérifiés sur le corpus :**

1. **T28** écrit `\textbf{3/13} sujets (implicite)` au lieu de `(2013-2026)`. Le `n/13` reste parsable : ne pas ancrer le regex sur l'année.
2. **T20 contient des accolades imbriquées dans son titre** :
   `\ficheEntete{T20}{Filtres RC/RL - 1\textsuperscript{er} et 2\textsuperscript{e} ordre}{colElec}`.
   Un motif `\{[^}]*\}` s'arrête au premier `}` de `\textsuperscript{er}`, décale
   tous les groupes suivants, et le domaine ressort vide. **Le titre et le
   domaine doivent donc être extraits par comptage d'accolades**, pas par
   `[^}]*`. C'est la seule fiche concernée aujourd'hui, mais rien n'empêche
   qu'une autre le devienne.

Le parseur lit donc les arguments de `\ficheEntete` un par un, en équilibrant les accolades. `argument(n)` retourne le n-ième argument : 0 = code, 1 = titre, 2 = couleur, 3 = domaine, 4 = ligne de présence.

`poids` est dérivé : `presence_n / presence_sur`, arrondi à 3 décimales. Il pondère la file de révision (Task 8).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_parse_meta.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_parse_meta.py -v`
Expected: FAIL avec `ModuleNotFoundError: No module named 'scripts.parse_meta'`

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/parse_meta.py
"""Extraction des métadonnées de thème depuis les fiches .tex."""

import re

_MACRO = "\\ficheEntete"
_PRESENCE = re.compile(
    r"Présence\s*:\}\s*\\textbf\{(?P<n>\d+)\s*/\s*(?P<sur>\d+)\}"
)


def _arguments(texte: str, depart: int, combien: int) -> list[str]:
    """Lit `combien` arguments {…} consécutifs à partir de `depart`.

    Équilibre les accolades : le titre de T20 contient
    `1\\textsuperscript{er}`, qu'un motif `[^}]*` tronquerait, décalant
    silencieusement tous les arguments suivants.
    """
    args: list[str] = []
    i = depart
    n = len(texte)
    while len(args) < combien and i < n:
        while i < n and texte[i] != "{":
            # Entre deux arguments on ne tolère que des blancs, % et sauts.
            if texte[i] not in " \t\r\n%":
                return args
            i += 1
        if i >= n:
            break
        profondeur = 1
        i += 1
        debut = i
        while i < n and profondeur:
            if texte[i] == "{":
                profondeur += 1
            elif texte[i] == "}":
                profondeur -= 1
            i += 1
        args.append(texte[debut:i - 1])
    return args


_BALISE = re.compile(r"\\[a-zA-Z]+\s*")


def _detex(s: str) -> str:
    """Transforme un fragment LaTeX en texte affichable.

    Le titre de T20 vaut `Filtres RC/RL - 1\\textsuperscript{er} et
    2\\textsuperscript{e} ordre` : sans nettoyage, l'app afficherait la
    commande telle quelle. On retire la commande et on garde son argument.
    """
    s = _BALISE.sub("", s)
    s = s.replace("{", "").replace("}", "")
    s = s.replace("~", " ").replace("\\", "")
    return re.sub(r"\s+", " ", s).strip()


def parse_meta(texte_tex: str) -> dict:
    """Extrait code, titre, domaine et fréquence d'apparition d'une fiche.

    Lève ValueError si la fiche n'a pas de \\ficheEntete — c'est un défaut
    de la source, pas un cas à ignorer silencieusement.
    """
    pos = texte_tex.find(_MACRO)
    if pos == -1:
        raise ValueError("aucun \\ficheEntete trouvé dans la fiche")

    # 0 = code, 1 = titre, 2 = couleur, 3 = domaine, 4 = ligne de présence
    args = _arguments(texte_tex, pos + len(_MACRO), 5)
    if len(args) < 2:
        raise ValueError("\\ficheEntete incomplet (moins de 2 arguments)")

    code = args[0].strip()
    titre = _detex(args[1])
    domaine = _detex(args[3]) if len(args) > 3 else ""

    p = _PRESENCE.search(args[4] if len(args) > 4 else texte_tex)
    n = int(p.group("n")) if p else 0
    sur = int(p.group("sur")) if p else 13
    poids = round(n / sur, 3) if sur else 0.0

    return {
        "code": code,
        "titre": titre,
        "domaine": domaine,
        "presence_n": n,
        "presence_sur": sur,
        "poids": poids,
    }
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_parse_meta.py -v`
Expected: PASS (6 tests)

- [ ] **Step 5: Vérifier sur les 30 fiches réelles**

Run:
```bash
python -c "
import sys, pathlib; sys.path.insert(0,'.')
from scripts.parse_meta import parse_meta
ok=0
for f in sorted(pathlib.Path('fiches').glob('T[0-9][0-9]_[A-Z]*.tex')):
    if 'contenu' in f.name or 'pilote' in f.name: continue
    m = parse_meta(f.read_text(encoding='utf-8'))
    ok += 1
    if m['presence_n']==0 or not m['domaine']: print('INCOMPLET:', f.name, m)
print(ok, 'fiches parsees sans erreur')
"
```
Expected exactement : `30 fiches parsees sans erreur`, **aucune ligne `INCOMPLET`**.

Contrôles ciblés sur les deux cas limites connus :
- `T20` doit donner `titre = "Filtres RC/RL - 1er et 2e ordre"` (sans `\textsuperscript`) et un `domaine` **non vide** — c'est la fiche qui révèle le bug des accolades imbriquées.
- `T28` doit donner `presence_n = 3` malgré son `(implicite)`.

Les poids attendus s'échelonnent de `0.231` (T28) à `1.000` (T01, T02, T06, T08, T10). Si tous les poids valent `0.0`, le regex `_PRESENCE` ne matche pas : vérifier l'accent de « Présence ».

- [ ] **Step 6: Commit**

```bash
git add scripts/parse_meta.py tests/test_parse_meta.py
git commit -m "feat(build): parseur des metadonnees de theme depuis les .tex"
```

---

### Task 5: Extraction des environnements TikZ

**Files:**
- Create: `scripts/extract_tikz.py`
- Test: `tests/test_extract_tikz.py`

**Interfaces:**
- Produces: `extract_tikz_envs(texte_tex: str) -> list[dict]` — clés `env` (`"tikzpicture"` ou `"circuitikz"`), `code` (le bloc complet, délimiteurs inclus), `hash` (sha1 tronqué à 12, identifiant stable du schéma).

Le `hash` sert de nom de fichier SVG et de clé de cache : un schéma inchangé n'est pas recompilé.

Attention : les environnements peuvent être imbriqués (`tikzpicture` dans une `tcolorbox`), mais **pas l'un dans l'autre** dans ce corpus. Un comptage de profondeur simple sur `\begin{env}` / `\end{env}` suffit.

- [ ] **Step 1: Write the failing test**

```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_extract_tikz.py -v`
Expected: FAIL avec `ModuleNotFoundError: No module named 'scripts.extract_tikz'`

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/extract_tikz.py
"""Isolation des environnements TikZ/circuitikz d'une fiche .tex."""

import hashlib
import re
import sys

_ENVS = ("circuitikz", "tikzpicture")


def _hash(code: str) -> str:
    return hashlib.sha1(code.encode("utf-8")).hexdigest()[:12]


def extract_tikz_envs(texte_tex: str) -> list[dict]:
    """Retourne chaque environnement de dessin, dans l'ordre du fichier.

    Gère l'imbrication du même environnement par comptage de profondeur.
    """
    trouves = []
    for env in _ENVS:
        ouvre = re.compile(r"\\begin\{" + env + r"\}")
        ferme = re.compile(r"\\end\{" + env + r"\}")
        for m in ouvre.finditer(texte_tex):
            depart = m.start()
            profondeur = 1
            pos = m.end()
            while profondeur > 0:
                suivant_o = ouvre.search(texte_tex, pos)
                suivant_f = ferme.search(texte_tex, pos)
                if not suivant_f:
                    break  # environnement non fermé : source malformée
                if suivant_o and suivant_o.start() < suivant_f.start():
                    profondeur += 1
                    pos = suivant_o.end()
                else:
                    profondeur -= 1
                    pos = suivant_f.end()
            if profondeur != 0:
                print(f"  ! environnement {env} non ferme, schema ignore",
                      file=sys.stderr)
            if profondeur == 0:
                code = texte_tex[depart:pos]
                trouves.append({"env": env, "code": code, "hash": _hash(code),
                                "_pos": depart})

    trouves.sort(key=lambda d: d["_pos"])
    for d in trouves:
        del d["_pos"]
    return trouves
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_extract_tikz.py -v`
Expected: PASS (6 tests)

- [ ] **Step 5: Compter les schémas réels**

Run:
```bash
python -c "
import sys, pathlib; sys.path.insert(0,'.')
from scripts.extract_tikz import extract_tikz_envs
tot=0
for f in sorted(pathlib.Path('fiches').glob('T[0-9][0-9]_[A-Z]*.tex')):
    if 'contenu' in f.name or 'pilote' in f.name: continue
    n = len(extract_tikz_envs(f.read_text(encoding='utf-8')))
    tot += n
print('schemas fiches:', tot)
tote=0
for f in sorted(pathlib.Path('exercices').glob('T*_exercices.tex')):
    tote += len(extract_tikz_envs(f.read_text(encoding='utf-8')))
print('schemas exercices:', tote)
"
```
Expected: **31 schémas fiches, 155 schémas exercices**.

**Décision de périmètre, à ne pas réinterpréter** : seuls les **31 schémas des fiches** entrent dans la v1. Le comptage des 155 schémas d'`exercices/` est ici uniquement pour vérifier que le parseur les verrait — ils relèvent du mode simulation (v2) et gonfleraient la v1 de 5× en temps de compilation LaTeX. L'orchestrateur de la Task 7 n'itère donc **que** sur `fiches/`. Ne pas « compléter » ce comportement en ajoutant `exercices/`.

- [ ] **Step 6: Commit**

```bash
git add scripts/extract_tikz.py tests/test_extract_tikz.py
git commit -m "feat(build): extraction des environnements TikZ des fiches"
```

---

### Task 6: Compilation TikZ → SVG thémable

**Files:**
- Create: `scripts/build_svg.py`
- Test: `tests/test_build_svg.py`

**Interfaces:**
- Consumes: `extract_tikz_envs()` de Task 5.
- Produces:
  - `themify(svg: str) -> str` — remplace les couleurs codées en dur par `currentColor` / `var(--bg)`.
  - `compile_tikz(code: str, env: str, dest: pathlib.Path) -> bool` — écrit un SVG, retourne True si succès.

**Chaîne validée en amont de ce plan** : `latex -interaction=nonstopmode` → `.dvi` → `dvisvgm --no-fonts --exact` → SVG vectoriel de ~12 Ko. Le test a produit un montage inverseur à ALI correctement rendu. `--no-fonts` convertit le texte en tracés : aucune dépendance de police côté navigateur.

**Problème identifié et résolu** : le SVG sort avec `fill='#000'` et `fill='#fff'` codés en dur, donc **invisible en thème sombre**. `themify()` substitue vers `currentColor` et `var(--bg)`. La substitution a été testée : le SVG reste bien formé (validé par `xml.etree.ElementTree`).

Préambule du document standalone — il doit refléter `fiches/preamble.tex` pour les couleurs et les bibliothèques, sans charger le préambule complet (qui tire `fancyhdr`, `geometry`, `tcolorbox` et casserait `standalone`) :

```latex
\documentclass[border=3pt,dvisvgm]{standalone}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
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
```

- [ ] **Step 1: Write the failing test**

```python
# tests/test_build_svg.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_build_svg.py -v`
Expected: FAIL avec `ModuleNotFoundError: No module named 'scripts.build_svg'`

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/build_svg.py
"""Compilation des environnements TikZ en SVG thémables.

Chaîne : latex -> .dvi -> dvisvgm --no-fonts -> .svg, puis substitution
des couleurs codées en dur pour que le schéma suive le thème de l'app.
"""

import pathlib
import re
import shutil
import subprocess
import tempfile

PREAMBULE = r"""\documentclass[border=3pt,dvisvgm]{standalone}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_build_svg.py -v`
Expected: PASS (4 tests)

- [ ] **Step 5: Compiler un schéma réel de bout en bout**

Run:
```bash
python -c "
import sys, pathlib; sys.path.insert(0,'.')
from scripts.extract_tikz import extract_tikz_envs
from scripts.build_svg import compile_tikz
tex = pathlib.Path('fiches/T19_AOP.tex').read_text(encoding='utf-8')
e = extract_tikz_envs(tex)[0]
ok = compile_tikz(e['code'], e['env'], pathlib.Path('app/svg/_essai.svg'))
p = pathlib.Path('app/svg/_essai.svg')
print('compile:', ok, '| taille:', p.stat().st_size if p.exists() else 0)
print('themable:', 'currentColor' in p.read_text(encoding='utf-8') if p.exists() else False)
"
```
Expected: `compile: True`, taille > 2000 octets, `themable: True`.

- [ ] **Step 6: Exclure les artefacts du dépôt — AVANT le premier build**

Cette étape vient ici, et non en fin de plan : c'est la première task qui
écrit dans `app/svg/`. Plus tard, les `git add app/...` des Tasks 7, 11 et 13
auraient committé des centaines de SVG régénérables, à désindexer ensuite.

```bash
cat >> .gitignore <<'EOF'

# App de révision — artefacts régénérables (cf. scripts/build_cards.py)
app/svg/
app/cards.json
app/sw-assets.js
EOF
git check-ignore -v app/svg/test.svg app/cards.json app/sw-assets.js
```
Expected: les trois chemins sont listés comme ignorés par `.gitignore`.

- [ ] **Step 7: Commit**

```bash
rm -f app/svg/_essai.svg
git add scripts/build_svg.py tests/test_build_svg.py .gitignore
git commit -m "feat(build): compilation TikZ vers SVG themable"
```

---

### Task 7: Orchestrateur `build_cards.py`

**Files:**
- Create: `scripts/build_cards.py`
- Test: `tests/test_build_cards.py`

**Interfaces:**
- Consumes: `parse_table_formulas`, `parse_block_formulas` (Tasks 1-2), `parse_pieges` (Task 3), `parse_meta` (Task 4), `extract_tikz_envs` (Task 5), `compile_tikz` (Task 6).
- Produces: `app/cards.json` de schéma :

```json
{
  "version": 1,
  "genere_le": "2026-09-21",
  "themes": [
    {"code": "T19", "titre": "AOP", "domaine": "électronique", "poids": 0.308,
     "presence_n": 4, "presence_sur": 13}
  ],
  "cards": [
    {"id": "T19-f-003", "type": "formule", "theme": "T19",
     "label": "Montage inverseur", "latex": "...", "unites": "",
     "conditions": "...", "poids": 0.308},
    {"id": "T19-p-001", "type": "piege", "theme": "T19", "titre": "...",
     "piege": "...", "regle": "...", "erreur_type": "...", "poids": 0.308},
    {"id": "T19-s-001", "type": "schema", "theme": "T19",
     "svg": "svg/a1b2c3d4e5f6.svg", "niveau": "reconnaissance",
     "label": "Schéma T19 n°1", "poids": 0.308}
  ]
}
```

**Règle d'`id`** : `{theme}-{f|p|s}-{compteur sur 3 chiffres}`. Stable tant que l'ordre des sources ne change pas — la progression `localStorage` est indexée par cet id.

**Niveau des cartes schéma** : `reconnaissance` par défaut. La v1 ne tente pas de deviner `calcul` ou `trace` automatiquement — ce serait une heuristique fragile. Un fichier `scripts/niveaux_schemas.json` (créé vide, `{}`) permet de surclasser manuellement un hash de schéma vers `calcul` ou `trace`. C'est le seul endroit où une saisie manuelle est admise, et elle ne porte pas sur du contenu pédagogique mais sur une classification.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_build_cards.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_build_cards.py -v`
Expected: FAIL avec `ModuleNotFoundError: No module named 'scripts.build_cards'`

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/build_cards.py
"""Orchestrateur : assemble app/cards.json depuis les sources LaTeX/Markdown.

Usage : python scripts/build_cards.py [--sans-svg]
"""

import argparse
import datetime
import json
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE))

from scripts.parse_formules import parse_table_formulas, parse_block_formulas
from scripts.parse_pieges import parse_pieges
from scripts.parse_meta import parse_meta
from scripts.extract_tikz import extract_tikz_envs
from scripts.build_svg import compile_tikz

_PREFIXE = {"formule": "f", "piege": "p", "schema": "s"}
_SECTION_1 = re.compile(r"^## 1\..*?(?=^## 2\.|\Z)", re.S | re.M)


def faire_id(theme: str, type_carte: str, n: int) -> str:
    return f"{theme}-{_PREFIXE[type_carte]}-{n:03d}"


# Vocabulaire réel de la colonne « Fréquence » des fiches, relevé sur le
# corpus au 2026-09-21. Multiplie le poids de thème pour les 114 formules
# qui le portent ; une valeur inconnue laisse le poids inchangé (1.0).
_BONUS_FREQUENCE = {
    "systématique": 1.30,
    "à connaître par cœur": 1.30,
    "très fréquent": 1.20,
    "fréquent": 1.10,
    "base": 1.10,
    "courant": 1.00,
    "présent": 0.90,
}


def _poids_final(poids_theme: float, frequence: str) -> float:
    """Affine le poids de thème par la fréquence propre à la formule.

    Le texte est normalisé (minuscules, accords féminins, parenthèses
    retirées) puis cherché par préfixe : « Très fréquente (donnée ou
    calculée) » doit valoir autant que « Très fréquent ».
    """
    if not frequence:
        return round(poids_theme, 4)
    f = frequence.lower().split("(")[0].strip().rstrip("es").strip()
    for cle, bonus in _BONUS_FREQUENCE.items():
        base = cle.rstrip("es")
        if f.startswith(base):
            return round(poids_theme * bonus, 4)
    return round(poids_theme, 4)


def assembler(themes: list[dict], cartes: list[dict]) -> dict:
    """Assemble la structure finale, en attribuant ids et poids."""
    poids_par_theme = {t["code"]: t["poids"] for t in themes}
    compteurs: dict[tuple[str, str], int] = {}
    sorties = []

    for c in cartes:
        theme = c["theme"]
        if theme not in poids_par_theme:
            raise ValueError(f"carte rattachée à un thème inconnu : {theme}")
        cle = (theme, c["type"])
        compteurs[cle] = compteurs.get(cle, 0) + 1
        carte = dict(c)
        carte["id"] = faire_id(theme, c["type"], compteurs[cle])
        carte["poids"] = _poids_final(poids_par_theme[theme], c.get("frequence", ""))
        sorties.append(carte)

    return {
        "version": 1,
        "genere_le": datetime.date.today().isoformat(),
        "themes": themes,
        "cards": sorties,
    }


def construire(sans_svg: bool = False) -> dict:
    fiches = RACINE / "fiches"
    niveaux_path = RACINE / "scripts" / "niveaux_schemas.json"
    niveaux = json.loads(niveaux_path.read_text(encoding="utf-8")) if niveaux_path.exists() else {}

    themes, cartes = [], []

    for tex in sorted(fiches.glob("T[0-9][0-9]_[A-Z]*.tex")):
        if "contenu" in tex.name or "pilote" in tex.name:
            continue
        texte_tex = tex.read_text(encoding="utf-8")
        meta = parse_meta(texte_tex)
        code = meta["code"]
        themes.append(meta)

        md = fiches / f"{code}_contenu.md"
        if md.exists():
            texte_md = md.read_text(encoding="utf-8")
            m1 = _SECTION_1.search(texte_md)
            if m1:
                section1 = m1.group(0)
                cartes += parse_table_formulas(section1, code)
                cartes += parse_block_formulas(section1, code)
            cartes += parse_pieges(texte_md, code)

        for i, env in enumerate(extract_tikz_envs(texte_tex), start=1):
            rel = f"svg/{env['hash']}.svg"
            dest = RACINE / "app" / rel
            if not sans_svg and not dest.exists():
                if not compile_tikz(env["code"], env["env"], dest):
                    print(f"  ! schema non compile : {code} n°{i}", file=sys.stderr)
                    continue
            # Une carte schéma sans son image n'a aucun sens : en mode
            # --sans-svg, on ne l'émet pas plutôt que de produire une carte
            # dont le recto est une image cassée.
            if not dest.exists():
                continue
            cartes.append({
                "type": "schema",
                "theme": code,
                "svg": rel,
                "niveau": niveaux.get(env["hash"], "reconnaissance"),
                "label": f"Schéma {code} n°{i}",
            })

    return assembler(themes, cartes)


def ecrire_sw_assets(app_dir: pathlib.Path) -> int:
    """Génère app/sw-assets.js : la liste des fichiers à précacher.

    Le service worker doit connaître les SVG de schémas et les polices
    KaTeX. Sans cela, un schéma jamais affiché avant la coupure réseau
    donne une image cassée, et les formules tombent sur une police de
    substitution au premier lancement hors-ligne.
    """
    chemins: list[str] = []

    svg_dir = app_dir / "svg"
    if svg_dir.exists():
        chemins += sorted(f"./svg/{p.name}" for p in svg_dir.glob("*.svg"))

    fonts = app_dir / "vendor" / "katex" / "fonts"
    if fonts.exists():
        # Les .woff2 suffisent : tous les navigateurs cibles les gèrent.
        chemins += sorted(f"./vendor/katex/fonts/{p.name}"
                          for p in fonts.glob("*.woff2"))

    contenu = (
        "// Généré par build_cards.py — ne pas modifier à la main.\n"
        "self.ASSETS = " + json.dumps(chemins, indent=1) + ";\n"
    )
    (app_dir / "sw-assets.js").write_text(contenu, encoding="utf-8")
    return len(chemins)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sans-svg", action="store_true",
                    help="n'appelle pas LaTeX : itération rapide sur le texte. "
                         "Les cartes schéma dont le SVG n'existe pas encore "
                         "sont alors OMISES (pas d'image cassée).")
    args = ap.parse_args()

    data = construire(sans_svg=args.sans_svg)
    sortie = RACINE / "app" / "cards.json"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(
        json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    ecrire_sw_assets(RACINE / "app")
    par_type: dict[str, int] = {}
    for c in data["cards"]:
        par_type[c["type"]] = par_type.get(c["type"], 0) + 1
    print(f"{len(data['themes'])} themes, {len(data['cards'])} cartes -> {sortie}")
    print("  detail :", par_type)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_build_cards.py -v`
Expected: PASS (5 tests)

- [ ] **Step 5: Build réel sans SVG (rapide)**

Run:
```bash
echo '{}' > scripts/niveaux_schemas.json
python scripts/build_cards.py --sans-svg
```
Expected : `30 themes, ~575 cartes -> .../app/cards.json`, avec un détail **mesuré sur le corpus au 2026-09-21** :

| Compteur | Valeur attendue |
|---|---|
| formules (tableau) | **191** |
| formules (bloc `$$`) | **153** |
| pièges | **199** |
| schémas | **31** |
| **total** | **574** |

Ces nombres sont des invariants de non-régression, pas des ordres de grandeur. Un écart signale un parseur cassé — en particulier : **8 pièges** = seul le format `###` est géré ; **~78 formules tableau** = la détection de colonne est retombée sur une position fixe.

- [ ] **Step 6: Build complet avec SVG**

Run: `python scripts/build_cards.py`
Expected: même sortie, plus la création de `app/svg/*.svg`. Quelques `! schema non compile` sont tolérables ; si plus de 5 échouent, inspecter un cas avant de continuer.

- [ ] **Step 7: Commit**

```bash
git add scripts/build_cards.py scripts/niveaux_schemas.json tests/test_build_cards.py
git commit -m "feat(build): orchestrateur de generation de cards.json"
```

---

### Task 8: Ordonnanceur de révision (SM-2 pondéré)

**Files:**
- Create: `app/js/scheduler.js`
- Test: `tests/test_scheduler.html` (harnais de test navigateur, sans dépendance)

**Interfaces:**
- Produces:
  - `noter(etat, note) -> etat` où `note ∈ {"su","hesite","rate"}`. `etat` a les clés `intervalle` (jours), `facilite` (float ≥ 1.3), `repetitions` (int), `du` (timestamp ms).
  - `fileDuJour(cartes, progression, maintenant, taille) -> Card[]`

Algorithme : SM-2 simplifié à trois notes.
- `rate` → `repetitions = 0`, `intervalle = 0` (revient dans la même session), `facilite -= 0,20`
- `hesite` → `intervalle = max(1, round(intervalle × 1,2))`, `facilite -= 0,05`
- `su` → `repetitions == 0 → 1 j` ; `== 1 → 3 j` ; sinon `round(intervalle × facilite)`. `facilite += 0,10`
- `facilite` bornée à `[1,3 ; 2,8]`, initialisée à `2,4`.

**Pondération par la fréquence au concours** : à échéance égale, une carte de thème `13/13` passe avant une carte `3/13`. Tri de la file : d'abord les cartes en retard (`du <= maintenant`) par `poids` décroissant, puis les nouvelles cartes par `poids` décroissant. C'est ce qui exploite le Bloc 5 des fiches.

- [ ] **Step 1: Write the failing test**

```html
<!-- tests/test_scheduler.html -->
<!doctype html><meta charset="utf-8"><title>Tests scheduler</title>
<body><pre id="out"></pre>
<script type="module">
import { noter, fileDuJour, etatInitial } from "../app/js/scheduler.js";

const res = [];
const ok = (nom, cond) => res.push((cond ? "PASS " : "FAIL ") + nom);

// noter()
let e = etatInitial();
ok("facilite initiale 2,4", e.facilite === 2.4);
ok("intervalle initial 0", e.intervalle === 0);

let s = noter(etatInitial(), "su");
ok("su depuis zero -> 1 jour", s.intervalle === 1);
ok("su incremente repetitions", s.repetitions === 1);

let s2 = noter(s, "su");
ok("2e su -> 3 jours", s2.intervalle === 3);

let r = noter(s2, "rate");
ok("rate remet intervalle a 0", r.intervalle === 0);
ok("rate remet repetitions a 0", r.repetitions === 0);
ok("rate baisse la facilite", r.facilite < s2.facilite);

let plancher = { intervalle: 1, facilite: 1.3, repetitions: 1, du: 0 };
ok("facilite plancher 1,3", noter(plancher, "rate").facilite === 1.3);

let plafond = { intervalle: 1, facilite: 2.8, repetitions: 5, du: 0 };
ok("facilite plafond 2,8", noter(plafond, "su").facilite === 2.8);

let h = noter({ intervalle: 10, facilite: 2.4, repetitions: 3, du: 0 }, "hesite");
ok("hesite allonge peu", h.intervalle === 12);

// fileDuJour()
const cartes = [
  { id: "a", poids: 0.3 }, { id: "b", poids: 1.0 }, { id: "c", poids: 0.5 },
];
const maintenant = 1000000;
const vide = {};
const f = fileDuJour(cartes, vide, maintenant, 3);
ok("nouvelles cartes triees par poids", f[0].id === "b" && f[1].id === "c");
ok("taille de file respectee", fileDuJour(cartes, vide, maintenant, 2).length === 2);

const prog = {
  a: { intervalle: 1, facilite: 2.4, repetitions: 1, du: maintenant - 1 },
  b: { intervalle: 5, facilite: 2.4, repetitions: 2, du: maintenant + 999999 },
};
const f2 = fileDuJour(cartes, prog, maintenant, 3);
ok("carte non echue exclue", !f2.some(c => c.id === "b"));
ok("carte en retard incluse", f2.some(c => c.id === "a"));
ok("carte en retard avant nouvelle", f2[0].id === "a");

// Plafond d'intervalle : l'écrit est en mars, rien ne doit dépasser 60 jours.
let acquise = { intervalle: 40, facilite: 2.8, repetitions: 5, du: 0 };
ok("intervalle plafonne a 60 jours", noter(acquise, "su").intervalle === 60);
let long = etatInitial();
for (let i = 0; i < 12; i++) long = noter(long, "su");
ok("aucune derive apres 12 reussites", long.intervalle === 60);

// Famine des cartes neuves : 50 cartes échues ne doivent pas tout saturer.
const gros = [], pr = {};
for (let i = 0; i < 50; i++) {
  gros.push({ id: "r" + i, poids: 1.0 });
  pr["r" + i] = { intervalle: 5, facilite: 2.4, repetitions: 2, du: maintenant - 1 };
}
for (let i = 0; i < 20; i++) gros.push({ id: "n" + i, poids: 0.5 });
const f3 = fileDuJour(gros, pr, maintenant, 30);
ok("quota de nouvelles respecte malgre 50 echues",
   f3.filter(c => c.id.startsWith("n")).length === 8);
ok("file remplie a la taille demandee", f3.length === 30);

// Peu de cartes neuves : les places inutilisées reviennent aux révisions.
const f4 = fileDuJour([...gros.slice(0, 50), { id: "n0", poids: 0.5 }], pr, maintenant, 30);
ok("places rendues aux revisions si peu de neuves", f4.length === 30);

document.getElementById("out").textContent = res.join("\n") +
  "\n\n" + res.filter(r => r.startsWith("FAIL")).length + " echec(s)";
</script>
```

- [ ] **Step 2: Run test to verify it fails**

Run:
```bash
python -m http.server 8765 --directory . &
sleep 1
echo "Ouvrir http://localhost:8765/tests/test_scheduler.html"
```
Expected: la page affiche une erreur console `Failed to resolve module specifier` / fichier `scheduler.js` introuvable.

- [ ] **Step 3: Write minimal implementation**

```javascript
// app/js/scheduler.js
// Ordonnanceur SM-2 simplifié, pondéré par la fréquence d'apparition au concours.

const FACILITE_INIT = 2.4;
const FACILITE_MIN = 1.3;
const FACILITE_MAX = 2.8;
const JOUR_MS = 86400000;

// Plafond d'intervalle, en jours. Sans lui, la suite des « su » donne
// 1, 3, 8, 22, 62, 174, 487, 1364… : dès la 6e répétition la carte sort de
// l'horizon de révision (l'écrit est en mars). Avec 60 jours, une carte
// acquise revient au moins trois fois d'ici l'épreuve.
const INTERVALLE_MAX = 60;

// Places réservées aux cartes jamais vues dans chaque file quotidienne.
// Sans ce quota, les cartes échues (toujours prioritaires) saturent la file
// dès qu'il y en a 30, et la découverte du corpus s'arrête définitivement.
const QUOTA_NOUVELLES = 8;

export function etatInitial() {
  return { intervalle: 0, facilite: FACILITE_INIT, repetitions: 0, du: 0 };
}

function borner(f) {
  return Math.min(FACILITE_MAX, Math.max(FACILITE_MIN, Math.round(f * 100) / 100));
}

export function noter(etat, note, maintenant = Date.now()) {
  const e = { ...etat };

  if (note === "rate") {
    e.repetitions = 0;
    e.intervalle = 0;
    e.facilite = borner(e.facilite - 0.2);
  } else if (note === "hesite") {
    e.repetitions += 1;
    e.intervalle = Math.max(1, Math.round(e.intervalle * 1.2));
    e.facilite = borner(e.facilite - 0.05);
  } else {
    // "su"
    if (e.repetitions === 0) e.intervalle = 1;
    else if (e.repetitions === 1) e.intervalle = 3;
    else e.intervalle = Math.min(INTERVALLE_MAX, Math.round(e.intervalle * e.facilite));
    e.repetitions += 1;
    e.facilite = borner(e.facilite + 0.1);
  }

  e.du = maintenant + e.intervalle * JOUR_MS;
  return e;
}

export function fileDuJour(cartes, progression, maintenant = Date.now(), taille = 30) {
  const enRetard = [];
  const nouvelles = [];

  for (const c of cartes) {
    const p = progression[c.id];
    if (!p) nouvelles.push(c);
    else if (p.du <= maintenant) enRetard.push(c);
  }

  const parPoids = (a, b) => (b.poids || 0) - (a.poids || 0);
  enRetard.sort(parPoids);
  nouvelles.sort(parPoids);

  // Les cartes échues sont prioritaires, mais on garde des places pour les
  // cartes jamais vues : sinon, dès que 30 cartes sont échues, plus aucune
  // nouveauté n'entre et la découverte du corpus (~575 cartes) s'arrête.
  const placesRevisions = Math.max(0, taille - QUOTA_NOUVELLES);
  const retenues = enRetard.slice(0, placesRevisions);
  const neuves = nouvelles.slice(0, taille - retenues.length);

  // S'il reste de la place (peu de cartes neuves disponibles), on la rend
  // aux révisions en retard plutôt que de servir une file incomplète.
  const reste = taille - retenues.length - neuves.length;
  const complement = reste > 0 ? enRetard.slice(placesRevisions, placesRevisions + reste) : [];

  return [...retenues, ...complement, ...neuves];
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: recharger `http://localhost:8765/tests/test_scheduler.html`
Expected: toutes les lignes en `PASS`, `0 echec(s)`.

- [ ] **Step 5: Commit**

```bash
git add app/js/scheduler.js tests/test_scheduler.html
git commit -m "feat(app): ordonnanceur SM-2 pondere par la frequence au concours"
```

---

### Task 9: Persistance `localStorage` avec export/import

**Files:**
- Create: `app/js/store.js`
- Test: `tests/test_store.html`

**Interfaces:**
- Produces: `charger()`, `sauver(prog)`, `majCarte(id, etat)`, `exporter()`, `importer(json)`, `reinitialiser()`.

Clé `localStorage` : `capet.progression.v1`. Sans serveur, l'export JSON est le **seul** filet de sécurité — d'où sa présence en v1 et non en v2.

`importer()` doit rejeter une entrée malformée plutôt que corrompre la progression existante.

- [ ] **Step 1: Write the failing test**

```html
<!-- tests/test_store.html -->
<!doctype html><meta charset="utf-8"><title>Tests store</title>
<body><pre id="out"></pre>
<script type="module">
import { charger, sauver, majCarte, exporter, importer, reinitialiser, CLE }
  from "../app/js/store.js";

const res = [];
const ok = (n, c) => res.push((c ? "PASS " : "FAIL ") + n);

reinitialiser();
ok("charge vide apres reset", Object.keys(charger()).length === 0);

majCarte("T01-f-001", { intervalle: 1, facilite: 2.4, repetitions: 1, du: 42 });
ok("carte persistee", charger()["T01-f-001"].du === 42);

sauver({ "T02-p-001": { intervalle: 3, facilite: 2.5, repetitions: 2, du: 99 } });
ok("sauver remplace tout", charger()["T01-f-001"] === undefined);

const dump = exporter();
ok("export est du JSON valide", typeof JSON.parse(dump) === "object");
ok("export porte une version", JSON.parse(dump).version === 1);

reinitialiser();
ok("import restaure", importer(dump) && charger()["T02-p-001"].du === 99);

const avant = JSON.stringify(charger());
ok("import refuse du JSON casse", importer("{pas du json") === false);
ok("progression intacte apres refus", JSON.stringify(charger()) === avant);
ok("import refuse une structure sans progression", importer('{"version":1}') === false);

document.getElementById("out").textContent = res.join("\n") +
  "\n\n" + res.filter(r => r.startsWith("FAIL")).length + " echec(s)";
</script>
```

- [ ] **Step 2: Run test to verify it fails**

Run: ouvrir `http://localhost:8765/tests/test_store.html`
Expected: erreur de résolution du module `store.js`.

- [ ] **Step 3: Write minimal implementation**

```javascript
// app/js/store.js
// Persistance de la progression. Aucun serveur : l'export JSON est le seul backup.

export const CLE = "capet.progression.v1";

export function charger() {
  try {
    const brut = localStorage.getItem(CLE);
    return brut ? JSON.parse(brut) : {};
  } catch {
    return {};
  }
}

export function sauver(progression) {
  localStorage.setItem(CLE, JSON.stringify(progression));
}

export function majCarte(id, etat) {
  const p = charger();
  p[id] = etat;
  sauver(p);
}

export function reinitialiser() {
  localStorage.removeItem(CLE);
}

export function exporter() {
  return JSON.stringify(
    { version: 1, exporte_le: new Date().toISOString(), progression: charger() },
    null, 1
  );
}

export function importer(texte) {
  let data;
  try {
    data = JSON.parse(texte);
  } catch {
    return false;
  }
  if (!data || typeof data !== "object") return false;
  if (!data.progression || typeof data.progression !== "object") return false;
  sauver(data.progression);
  return true;
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: recharger `http://localhost:8765/tests/test_store.html`
Expected: `0 echec(s)`.

- [ ] **Step 5: Commit**

```bash
git add app/js/store.js tests/test_store.html
git commit -m "feat(app): persistance localStorage avec export/import JSON"
```

---

### Task 10: Rendu des cartes (3 types, révélation)

**Files:**
- Create: `app/js/card-render.js`
- Create: `app/vendor/` (KaTeX vendored)
- Test: `tests/test_card_render.html`

**Interfaces:**
- Consumes: rien.
- Produces: `rendreRecto(carte) -> string` (HTML), `rendreVerso(carte) -> string` (HTML).

Règles de rendu, par type :

| Type | Recto | Verso |
|---|---|---|
| `formule` | « Énoncez la relation : **{label}** » | formule KaTeX + unités + **conditions** (si présentes) |
| `piege` | « **{titre}** — {piege} » + « Légitime ou non ? » | **{regle}** + erreur type (si présente) |
| `schema` (reconnaissance) | le SVG + « Quel montage ? Quelle relation ? » | {label} + le SVG |
| `schema` (calcul) | le SVG + « Calculez la grandeur demandée » | {label} + le SVG |
| `schema` (trace) | « Tracez de mémoire : **{label}** » | le SVG |

**Sécurité du rendu** : le contenu vient de sources contrôlées (le repo), mais il contient du LaTeX avec des caractères `<`, `>`, `&`. Tout texte inséré passe par `echapper()`. Le LaTeX est rendu par KaTeX, pas par `innerHTML` brut.

**KaTeX vendored** : télécharger `katex.min.js`, `katex.min.css` et le dossier `fonts/` de KaTeX 0.16.9 dans `app/vendor/katex/`. Contrainte hors-ligne : aucun CDN.

- [ ] **Step 1: Write the failing test**

```html
<!-- tests/test_card_render.html -->
<!doctype html><meta charset="utf-8"><title>Tests rendu</title>
<body><pre id="out"></pre>
<script type="module">
import { rendreRecto, rendreVerso, echapper, texteAvecMaths }
  from "../app/js/card-render.js";

const res = [];
const ok = (n, c) => res.push((c ? "PASS " : "FAIL ") + n);

ok("echappe les chevrons", echapper("a<b>&c") === "a&lt;b&gt;&amp;c");

// 26 labels réels contiennent du LaTeX inline : « Phase $t \in [0;\alpha T[$ »
ok("texte sans maths reste echappe",
   texteAvecMaths("a<b>") === "a&lt;b&gt;");
ok("segment math non affiche en source brute",
   !texteAvecMaths("Phase $t \\in [0;T[$").includes("$t"));
ok("texte hors maths conserve",
   texteAvecMaths("Phase $x$").includes("Phase"));
ok("chevrons hors maths toujours echappes",
   texteAvecMaths("a<b> $x$").includes("&lt;b&gt;"));

const f = { type: "formule", label: "Loi d'Ohm", latex: "u = R i",
            unites: "V, Ω, A", conditions: "régime continu" };
ok("recto formule cite le label", rendreRecto(f).includes("Loi d&#039;Ohm") ||
                                   rendreRecto(f).includes("Loi d'Ohm"));
ok("recto formule ne devoile pas la formule", !rendreRecto(f).includes("u = R i"));
ok("verso formule montre les unites", rendreVerso(f).includes("V, Ω, A"));
ok("verso formule montre les conditions", rendreVerso(f).includes("régime continu"));

const fsc = { type: "formule", label: "X", latex: "a", unites: "", conditions: "" };
ok("verso sans conditions n'affiche pas le bloc",
   !rendreVerso(fsc).includes("Conditions"));

const p = { type: "piege", titre: "Confusion FP", piege: "On écrit I=P/U",
            regle: "Diviser par le rendement", erreur_type: "sujet 2018" };
ok("recto piege pose la question", rendreRecto(p).includes("Légitime"));
ok("recto piege ne devoile pas la regle", !rendreRecto(p).includes("rendement"));
ok("verso piege montre la regle", rendreVerso(p).includes("Diviser par le rendement"));
ok("verso piege montre l'erreur type", rendreVerso(p).includes("sujet 2018"));

const sr = { type: "schema", niveau: "reconnaissance",
             svg: "svg/abc.svg", label: "Schéma T19 n°1" };
ok("recto schema reconnaissance affiche le svg", rendreRecto(sr).includes("svg/abc.svg"));
ok("recto schema reconnaissance cache le label", !rendreRecto(sr).includes("T19 n°1"));
ok("verso schema reconnaissance montre le label", rendreVerso(sr).includes("T19 n°1"));

const st = { type: "schema", niveau: "trace", svg: "svg/abc.svg", label: "Pont de Graetz" };
ok("recto trace montre le label", rendreRecto(st).includes("Pont de Graetz"));
ok("recto trace cache le svg", !rendreRecto(st).includes("svg/abc.svg"));
ok("verso trace montre le svg", rendreVerso(st).includes("svg/abc.svg"));

document.getElementById("out").textContent = res.join("\n") +
  "\n\n" + res.filter(r => r.startsWith("FAIL")).length + " echec(s)";
</script>
```

- [ ] **Step 2: Run test to verify it fails**

Run: ouvrir `http://localhost:8765/tests/test_card_render.html`
Expected: module `card-render.js` introuvable.

- [ ] **Step 3: Vendorer KaTeX**

Run:
```bash
mkdir -p app/vendor/katex
curl -L -o /tmp/katex.zip https://github.com/KaTeX/KaTeX/releases/download/v0.16.9/katex.zip
unzip -q -o /tmp/katex.zip -d /tmp/katexdist
cp /tmp/katexdist/katex/katex.min.js /tmp/katexdist/katex/katex.min.css app/vendor/katex/
cp -r /tmp/katexdist/katex/fonts app/vendor/katex/fonts
ls app/vendor/katex
```
Expected: `fonts  katex.min.css  katex.min.js`.

Si le téléchargement échoue (pas de réseau), l'app doit rester fonctionnelle : `card-render.js` teste `window.katex` et retombe sur un affichage en `<code>` du LaTeX brut.

- [ ] **Step 4: Write minimal implementation**

```javascript
// app/js/card-render.js
// Rendu HTML d'une carte, recto et verso. Aucun contenu pédagogique en dur ici.

export function echapper(s) {
  return String(s ?? "")
    .replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;").replaceAll("'", "&#039;");
}

function maths(latex, displayMode = true) {
  if (window.katex) {
    try {
      return window.katex.renderToString(latex, { displayMode, throwOnError: false });
    } catch { /* retombe sur le brut */ }
  }
  return `<code class="latex-brut">${echapper(latex)}</code>`;
}

// 26 labels du corpus contiennent du LaTeX inline — « Phase $t \in [0;\alpha T[$ »,
// « Rapport cyclique maximisant $\Delta i_L$ ». Affichés via echapper() seul,
// ils apparaîtraient en source brute. On rend donc chaque segment $…$ par
// KaTeX et on échappe le texte autour.
export function texteAvecMaths(s) {
  const brut = String(s ?? "");
  if (!brut.includes("$")) return echapper(brut);
  return brut
    .split(/(\$[^$]+\$)/g)
    .map(seg =>
      seg.startsWith("$") && seg.endsWith("$") && seg.length > 2
        ? maths(seg.slice(1, -1), false)
        : echapper(seg)
    )
    .join("");
}

function svg(chemin, alt) {
  return `<div class="carte-svg"><img src="${echapper(chemin)}" alt="${echapper(alt)}" loading="lazy"></div>`;
}

export function rendreRecto(c) {
  if (c.type === "formule") {
    return `<p class="consigne">Énoncez la relation :</p>
            <p class="vedette">${texteAvecMaths(c.label)}</p>`;
  }
  if (c.type === "piege") {
    return `<p class="titre-piege">${texteAvecMaths(c.titre)}</p>
            <p class="enonce">${texteAvecMaths(c.piege)}</p>
            <p class="consigne">Légitime, ou non ?</p>`;
  }
  // schema
  if (c.niveau === "trace") {
    return `<p class="consigne">Tracez de mémoire :</p>
            <p class="vedette">${texteAvecMaths(c.label)}</p>`;
  }
  const question = c.niveau === "calcul"
    ? "Calculez la grandeur demandée."
    : "Quel montage ? Quelle relation entrée/sortie ?";
  return `${svg(c.svg, "schéma à identifier")}
          <p class="consigne">${question}</p>`;
}

export function rendreVerso(c) {
  if (c.type === "formule") {
    const u = c.unites
      ? `<p class="unites">Unités : ${texteAvecMaths(c.unites)}</p>` : "";
    const cond = c.conditions
      ? `<p class="conditions"><strong>Conditions :</strong> ${texteAvecMaths(c.conditions)}</p>` : "";
    return `${maths(c.latex)}${u}${cond}`;
  }
  if (c.type === "piege") {
    const err = c.erreur_type
      ? `<p class="erreur-type">${texteAvecMaths(c.erreur_type)}</p>` : "";
    return `<p class="regle">${texteAvecMaths(c.regle)}</p>${err}`;
  }
  if (c.niveau === "trace") {
    return svg(c.svg, echapper(c.label));
  }
  return `<p class="vedette">${texteAvecMaths(c.label)}</p>${svg(c.svg, c.label)}`;
}
```

- [ ] **Step 5: Run test to verify it passes**

Run: recharger `http://localhost:8765/tests/test_card_render.html`
Expected: `0 echec(s)`.

- [ ] **Step 6: Commit**

```bash
git add app/js/card-render.js app/vendor tests/test_card_render.html
git commit -m "feat(app): rendu des cartes formule, piege et schema"
```

---

### Task 11: Écran Réviser + coquille HTML + thème

**Files:**
- Create: `app/index.html`
- Create: `app/css/style.css`
- Create: `app/js/app.js`
- Create: `app/js/views/reviser.js`

**Interfaces:**
- Consumes: `fileDuJour`, `noter`, `etatInitial` (Task 8) ; `charger`, `majCarte` (Task 9) ; `rendreRecto`, `rendreVerso` (Task 10) ; `app/cards.json` (Task 7).
- Produces: `vueReviser(racine, data)` monte l'écran de révision dans l'élément `racine`.

Déroulé d'une session : on affiche le recto → bouton « Révéler » → le verso apparaît sous le recto (on ne cache pas la question : voir sa réponse à côté de la question est ce qui ancre) → trois boutons `Su` / `Hésité` / `Raté` → carte suivante. Fin de file : écran de résumé.

**Cible mobile** : boutons de notation d'au moins 44 px de haut, en bas d'écran, atteignables au pouce. C'est l'usage réel visé (transports, 20 min).

**Thème sombre** : variables CSS, dont `--svg-bg` consommée par les SVG thémés en Task 6.

- [ ] **Step 1: Écrire la coquille HTML**

```html
<!-- app/index.html -->
<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Révision CAPET SII IE</title>
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#1d4ed8">

<!-- iOS : Safari ignore `display: standalone` du manifeste. Sans ces trois
     balises, l'app ajoutée à l'écran d'accueil s'ouvre AVEC la barre Safari,
     ce qui mange ~15 % de la hauteur utile sur un écran de téléphone. -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="CAPET IE">
<link rel="apple-touch-icon" href="icons/icone-192.png">
<link rel="stylesheet" href="vendor/katex/katex.min.css">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<header class="barre-haut">
  <span class="marque">CAPET SII·IE</span>
  <button id="bascule-theme" aria-label="Changer de thème">◐</button>
</header>

<main id="app" aria-live="polite"></main>

<nav class="barre-bas">
  <a href="#/reviser">Réviser</a>
  <a href="#/priorites">Priorités</a>
  <a href="#/reglages">Réglages</a>
</nav>

<script src="vendor/katex/katex.min.js" defer></script>
<script type="module" src="js/app.js"></script>
</body>
</html>
```

- [ ] **Step 2: Écrire le CSS (thème clair/sombre, mobile-first)**

```css
/* app/css/style.css */
:root {
  --bg: #f8fafc; --surface: #ffffff; --ink: #0f172a; --slate: #475569;
  --rule: #cbd5e1; --accent: #1d4ed8; --svg-bg: #ffffff;
  --su: #15803d; --hesite: #b45309; --rate: #b91c1c;
}
:root[data-theme="sombre"] {
  --bg: #0f172a; --surface: #1e293b; --ink: #e2e8f0; --slate: #94a3b8;
  --rule: #334155; --accent: #60a5fa; --svg-bg: #1e293b;
  --su: #4ade80; --hesite: #fbbf24; --rate: #f87171;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--ink);
  font: 16px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif;
  padding-top: env(safe-area-inset-top);
  padding-bottom: calc(64px + env(safe-area-inset-bottom));
}
.barre-haut {
  display: flex; justify-content: space-between; align-items: center;
  padding: .6rem 1rem; border-bottom: 1px solid var(--rule); background: var(--surface);
}
.marque { font-weight: 700; color: var(--accent); letter-spacing: .02em; }
#bascule-theme {
  background: none; border: 1px solid var(--rule); color: var(--ink);
  border-radius: 8px; min-width: 44px; min-height: 44px; font-size: 1.1rem;
}
main { padding: 1rem; max-width: 720px; margin: 0 auto; }
.carte {
  background: var(--surface); border: 1px solid var(--rule); border-radius: 14px;
  padding: 1.1rem; margin-bottom: 1rem;
}
.consigne { color: var(--slate); font-size: .92rem; margin: .2rem 0 .6rem; }
.vedette { font-size: 1.25rem; font-weight: 650; margin: .2rem 0; }
.titre-piege { font-weight: 650; color: var(--accent); margin: 0 0 .4rem; }
.conditions { border-left: 3px solid var(--accent); padding-left: .7rem; }
.erreur-type { color: var(--slate); font-size: .92rem; font-style: italic; }
.carte-svg { text-align: center; margin: .8rem 0; }
.carte-svg img { max-width: 100%; height: auto; color: var(--ink); }
.latex-brut { font-family: ui-monospace, monospace; word-break: break-all; }
.actions { display: flex; gap: .5rem; }
.actions button, .revelateur {
  flex: 1; min-height: 48px; border-radius: 10px; border: 1px solid var(--rule);
  background: var(--surface); color: var(--ink); font-size: 1rem; font-weight: 600;
}
.revelateur { width: 100%; background: var(--accent); color: #fff; border: none; }
.b-su { border-color: var(--su); color: var(--su); }
.b-hesite { border-color: var(--hesite); color: var(--hesite); }
.b-rate { border-color: var(--rate); color: var(--rate); }
.barre-bas {
  position: fixed; bottom: 0; left: 0; right: 0; display: flex;
  background: var(--surface); border-top: 1px solid var(--rule);
  padding-bottom: env(safe-area-inset-bottom);
}
.barre-bas a {
  flex: 1; text-align: center; padding: 1rem .4rem; text-decoration: none;
  color: var(--slate); font-size: .9rem; min-height: 44px;
}
.barre-bas a.actif { color: var(--accent); font-weight: 650; }
.progression-file { color: var(--slate); font-size: .85rem; text-align: right; }
table.grille { width: 100%; border-collapse: collapse; font-size: .9rem; }
table.grille th, table.grille td {
  border-bottom: 1px solid var(--rule); padding: .5rem .4rem; text-align: left;
}
.pastille { display: inline-block; width: 10px; height: 10px; border-radius: 50%; }
```

- [ ] **Step 3: Écrire la vue Réviser**

```javascript
// app/js/views/reviser.js
import { fileDuJour, noter, etatInitial } from "../scheduler.js";
import { charger, majCarte } from "../store.js";
import { rendreRecto, rendreVerso } from "../card-render.js";

const TAILLE_FILE = 30;
const JOUR_MS_VUE = 86400000;

export function vueReviser(racine, data) {
  const progression = charger();
  const file = fileDuJour(data.cards, progression, Date.now(), TAILLE_FILE);

  if (file.length === 0) {
    racine.innerHTML = `<div class="carte">
      <p class="vedette">Rien à réviser pour l'instant.</p>
      <p class="consigne">Toutes les cartes échues ont été vues. Revenez demain.</p>
    </div>`;
    return;
  }

  let i = 0;
  let notees = 0;
  const total = file.length;          // figé : les reprises ne le gonflent pas
  const reprises = new Set();         // cartes ratées, rejouées en fin de file

  function afficher() {
    if (i >= file.length) {
      racine.innerHTML = `<div class="carte">
        <p class="vedette">Session terminée</p>
        <p class="consigne">${notees} carte(s) révisée(s).</p>
      </div>`;
      return;
    }
    const c = file[i];
    const restantes = Math.max(0, file.length - i);
    racine.innerHTML = `
      <p class="progression-file">${Math.min(i + 1, total)} / ${total}${
        restantes > total - i ? " (+ reprises)" : ""}</p>
      <div class="carte">${rendreRecto(c)}</div>
      <div id="verso" hidden></div>
      <div id="commandes"><button class="revelateur" id="reveler">Révéler</button></div>`;

    document.getElementById("reveler").onclick = () => {
      const v = document.getElementById("verso");
      v.innerHTML = `<div class="carte">${rendreVerso(c)}</div>`;
      v.hidden = false;
      document.getElementById("commandes").innerHTML = `
        <div class="actions">
          <button class="b-rate"   data-n="rate">Raté</button>
          <button class="b-hesite" data-n="hesite">Hésité</button>
          <button class="b-su"     data-n="su">Su</button>
        </div>`;
      document.querySelectorAll("[data-n]").forEach(b => {
        b.onclick = () => {
          const note = b.dataset.n;
          const estReprise = reprises.has(c.id);

          if (estReprise) {
            // Deuxième passage dans la même session : la carte a DÉJÀ été
            // notée « raté » (repetitions remis à 0). La renoter ici la
            // pénaliserait une seconde fois — un « su » donnerait 1 jour au
            // lieu de 3. On planifie donc sans repasser par noter().
            reprises.delete(c.id);
            if (note !== "rate") {
              const etat = progression[c.id] || etatInitial();
              progression[c.id] = { ...etat, du: Date.now() + JOUR_MS_VUE };
              majCarte(c.id, progression[c.id]);
            } else {
              file.push(c);
              reprises.add(c.id);
            }
          } else {
            const suivant = noter(progression[c.id] || etatInitial(), note);
            progression[c.id] = suivant;
            majCarte(c.id, suivant);
            notees += 1;
            // Une carte ratée revient en fin de file, dans la même session.
            if (note === "rate") {
              file.push(c);
              reprises.add(c.id);
            }
          }
          i += 1;
          afficher();
        };
      });
    };
  }

  afficher();
}
```

- [ ] **Step 4: Écrire le routeur**

```javascript
// app/js/app.js
import { vueReviser } from "./views/reviser.js";

const CLE_THEME = "capet.theme";

function appliquerTheme(t) {
  document.documentElement.dataset.theme = t;
  try { localStorage.setItem(CLE_THEME, t); } catch { /* mode privé */ }
}

let DATA = null;

async function donnees() {
  if (!DATA) DATA = await (await fetch("cards.json")).json();
  return DATA;
}

const ROUTES = {
  "#/reviser": vueReviser,
};

async function naviguer() {
  const hash = location.hash || "#/reviser";
  const racine = document.getElementById("app");
  const vue = ROUTES[hash];

  document.querySelectorAll(".barre-bas a").forEach(a =>
    a.classList.toggle("actif", a.getAttribute("href") === hash));

  if (!vue) {
    racine.innerHTML = `<div class="carte"><p>Écran à venir.</p></div>`;
    return;
  }
  racine.innerHTML = `<div class="carte"><p class="consigne">Chargement…</p></div>`;
  try {
    vue(racine, await donnees());
  } catch (e) {
    racine.innerHTML = `<div class="carte"><p class="vedette">Données indisponibles</p>
      <p class="consigne">Lancez <code>python scripts/build_cards.py</code> puis rechargez.</p></div>`;
  }
}

window.addEventListener("hashchange", naviguer);
window.addEventListener("DOMContentLoaded", () => {
  let t = "clair";
  try { t = localStorage.getItem(CLE_THEME) || "clair"; } catch { /* ignore */ }
  appliquerTheme(t);
  document.getElementById("bascule-theme").onclick = () =>
    appliquerTheme(document.documentElement.dataset.theme === "sombre" ? "clair" : "sombre");
  if (!location.hash) location.hash = "#/reviser";
  naviguer();
});
```

- [ ] **Step 5: Vérifier manuellement dans le navigateur**

Run:
```bash
python scripts/build_cards.py --sans-svg
python -m http.server 8765 --directory . &
sleep 1
echo "Ouvrir http://localhost:8765/app/"
```

Liste de contrôle (cocher chaque point en observant l'écran) :
- [ ] Une carte s'affiche, le compteur indique `1 / 30`
- [ ] « Révéler » fait apparaître le verso **sans masquer le recto**
- [ ] Les trois boutons de notation apparaissent après révélation
- [ ] Noter fait avancer le compteur
- [ ] La bascule de thème fonctionne et le texte reste lisible dans les deux
- [ ] En largeur 390 px (outils développeur, iPhone), rien ne déborde horizontalement
- [ ] Recharger la page conserve la progression (les cartes déjà notées ne reviennent pas)

- [ ] **Step 6: Commit**

```bash
git add app/index.html app/css/style.css app/js/app.js app/js/views/reviser.js
git commit -m "feat(app): ecran Reviser, coquille HTML et theme clair/sombre"
```

---

### Task 12: Écran Priorités + écran Réglages

**Files:**
- Create: `app/js/views/priorites.js`
- Create: `app/js/views/reglages.js`
- Modify: `app/js/app.js` (enregistrer les deux routes)
- Test: `tests/test_priorites.html`

**Interfaces:**
- Consumes: `charger`, `exporter`, `importer`, `reinitialiser` (Task 9).
- Produces: `calculerMaitrise(cartes, progression) -> Map<theme, {vues, total, maitrise}>` — `maitrise` = part des cartes du thème dont `repetitions >= 2` et `facilite >= 2,4`.

L'écran Priorités croise `poids` (fréquence au concours) et `maitrise`. Le quadrant dangereux — **fort poids, faible maîtrise** — est signalé en tête de tableau. C'est la raison d'être de l'écran.

- [ ] **Step 1: Write the failing test**

```html
<!-- tests/test_priorites.html -->
<!doctype html><meta charset="utf-8"><title>Tests priorites</title>
<body><pre id="out"></pre>
<script type="module">
import { calculerMaitrise, ordonnerThemes } from "../app/js/views/priorites.js";

const res = [];
const ok = (n, c) => res.push((c ? "PASS " : "FAIL ") + n);

const cartes = [
  { id: "a", theme: "T01" }, { id: "b", theme: "T01" },
  { id: "c", theme: "T02" },
];
const prog = {
  a: { repetitions: 3, facilite: 2.5, intervalle: 5, du: 0 },
  b: { repetitions: 1, facilite: 2.4, intervalle: 1, du: 0 },
};

const m = calculerMaitrise(cartes, prog);
ok("total par theme", m.get("T01").total === 2 && m.get("T02").total === 1);
ok("vues comptees", m.get("T01").vues === 2);
ok("maitrise partielle", Math.abs(m.get("T01").maitrise - 0.5) < 1e-9);
ok("theme jamais vu a maitrise 0", m.get("T02").maitrise === 0);

const themes = [
  { code: "T01", poids: 0.3, titre: "A" },
  { code: "T02", poids: 1.0, titre: "B" },
];
const ordre = ordonnerThemes(themes, m);
ok("fort poids faible maitrise en tete", ordre[0].code === "T02");
ok("urgence calculee", ordre[0].urgence > ordre[1].urgence);

document.getElementById("out").textContent = res.join("\n") +
  "\n\n" + res.filter(r => r.startsWith("FAIL")).length + " echec(s)";
</script>
```

- [ ] **Step 2: Run test to verify it fails**

Run: ouvrir `http://localhost:8765/tests/test_priorites.html`
Expected: module `priorites.js` introuvable.

- [ ] **Step 3: Write minimal implementation**

```javascript
// app/js/views/priorites.js
import { charger } from "../store.js";

const SEUIL_REPET = 2;
// 2,3 et non 2,4 : la facilité initiale VAUT 2,4, donc un unique « hésité »
// (−0,05) la fait tomber à 2,35 et la carte n'est plus comptée acquise,
// même après deux réussites. Le seuil doit être strictement sous l'initiale.
const SEUIL_FACILITE = 2.3;

export function calculerMaitrise(cartes, progression) {
  const par = new Map();
  for (const c of cartes) {
    if (!par.has(c.theme)) par.set(c.theme, { vues: 0, acquises: 0, total: 0 });
    const e = par.get(c.theme);
    e.total += 1;
    const p = progression[c.id];
    if (p) {
      e.vues += 1;
      if (p.repetitions >= SEUIL_REPET && p.facilite >= SEUIL_FACILITE) e.acquises += 1;
    }
  }
  for (const e of par.values()) {
    e.maitrise = e.total ? e.acquises / e.total : 0;
  }
  return par;
}

export function ordonnerThemes(themes, maitrises) {
  return themes
    .map(t => {
      const m = maitrises.get(t.code) || { maitrise: 0, vues: 0, total: 0 };
      return { ...t, ...m, urgence: (t.poids || 0) * (1 - m.maitrise) };
    })
    .sort((a, b) => b.urgence - a.urgence);
}

function couleur(u) {
  if (u >= 0.5) return "var(--rate)";
  if (u >= 0.25) return "var(--hesite)";
  return "var(--su)";
}

export function vuePriorites(racine, data) {
  const m = calculerMaitrise(data.cards, charger());
  const lignes = ordonnerThemes(data.themes, m).map(t => `
    <tr>
      <td><span class="pastille" style="background:${couleur(t.urgence)}"></span></td>
      <td>${t.code}</td>
      <td>${t.titre}</td>
      <td>${t.presence_n}/${t.presence_sur}</td>
      <td>${Math.round(t.maitrise * 100)} %</td>
      <td>${t.vues}/${t.total}</td>
    </tr>`).join("");

  racine.innerHTML = `
    <div class="carte">
      <p class="vedette">Priorités</p>
      <p class="consigne">Croisement fréquence au concours × maîtrise.
        En rouge : tombe souvent, mal maîtrisé.</p>
      <table class="grille">
        <thead><tr><th></th><th>Code</th><th>Thème</th>
          <th>Sujets</th><th>Maîtrise</th><th>Vues</th></tr></thead>
        <tbody>${lignes}</tbody>
      </table>
    </div>`;
}
```

```javascript
// app/js/views/reglages.js
import { exporter, importer, reinitialiser, charger } from "../store.js";

export function vueReglages(racine, data) {
  const n = Object.keys(charger()).length;
  racine.innerHTML = `
    <div class="carte">
      <p class="vedette">Réglages</p>
      <p class="consigne">${n} carte(s) suivie(s) sur ${data.cards.length}.
        Aucun serveur : l'export est votre seule sauvegarde.</p>
      <div class="actions" style="margin-bottom:.6rem">
        <button id="exp">Exporter</button>
        <button id="imp">Importer</button>
      </div>
      <button class="revelateur" id="raz" style="background:var(--rate)">
        Tout réinitialiser</button>
      <p id="msg" class="consigne"></p>
      <textarea id="zone" rows="6" style="width:100%;display:none;
        background:var(--bg);color:var(--ink);border:1px solid var(--rule);
        border-radius:8px;padding:.5rem"></textarea>
    </div>`;

  const zone = document.getElementById("zone");
  const msg = document.getElementById("msg");

  document.getElementById("exp").onclick = () => {
    zone.style.display = "block";
    zone.value = exporter();
    zone.select();
    msg.textContent = "Copiez ce texte et conservez-le.";
  };

  document.getElementById("imp").onclick = () => {
    if (zone.style.display === "none" || !zone.value.trim()) {
      zone.style.display = "block";
      zone.value = "";
      msg.textContent = "Collez un export puis cliquez de nouveau sur Importer.";
      return;
    }
    msg.textContent = importer(zone.value)
      ? "Progression restaurée. Rechargez la page."
      : "Import refusé : le contenu n'est pas un export valide.";
  };

  document.getElementById("raz").onclick = () => {
    if (confirm("Effacer toute la progression ? Action irréversible.")) {
      reinitialiser();
      msg.textContent = "Progression effacée.";
    }
  };
}
```

- [ ] **Step 4: Enregistrer les routes**

Dans `app/js/app.js`, remplacer le bloc `ROUTES` et ses imports :

```javascript
import { vueReviser } from "./views/reviser.js";
import { vuePriorites } from "./views/priorites.js";
import { vueReglages } from "./views/reglages.js";

const ROUTES = {
  "#/reviser": vueReviser,
  "#/priorites": vuePriorites,
  "#/reglages": vueReglages,
};
```

- [ ] **Step 5: Run test to verify it passes**

Run: recharger `http://localhost:8765/tests/test_priorites.html`
Expected: `0 echec(s)`.

- [ ] **Step 6: Vérifier le garde-fou « aucun contenu pédagogique en dur »**

Run:
```bash
grep -rnE "cos\\\\varphi|\\\\frac|Loi d'Ohm|sinusoïdal" app/js/ && echo "ECHEC: contenu pedagogique dans le code" || echo "OK: aucun contenu pedagogique en dur"
```
Expected: `OK: aucun contenu pedagogique en dur`

- [ ] **Step 7: Commit**

```bash
git add app/js/views/priorites.js app/js/views/reglages.js app/js/app.js tests/test_priorites.html
git commit -m "feat(app): ecrans Priorites et Reglages"
```

---

### Task 13: PWA — manifeste, service worker, installabilité

**Files:**
- Create: `app/manifest.webmanifest`
- Create: `app/sw.js`
- Create: `app/icons/icone-192.png`, `app/icons/icone-512.png`
- Modify: `app/js/app.js` (enregistrement du service worker)

**Interfaces:**
- Consumes: tous les fichiers produits par les tasks précédentes.

Stratégie de cache : **cache-first** avec liste explicite. L'app doit fonctionner sans réseau après la première visite — c'est l'exigence d'usage (transports). Le nom du cache porte une version ; l'incrémenter force le rafraîchissement.

Attention : `cards.json` et les SVG doivent être dans le cache, sinon l'app s'ouvre vide hors-ligne.

- [ ] **Step 1: Écrire le manifeste**

```json
{
  "name": "Révision CAPET SII·IE",
  "short_name": "CAPET IE",
  "start_url": "./index.html",
  "scope": "./",
  "display": "standalone",
  "orientation": "portrait",
  "background_color": "#f8fafc",
  "theme_color": "#1d4ed8",
  "lang": "fr",
  "icons": [
    { "src": "icons/icone-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any" },
    { "src": "icons/icone-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable" }
  ]
}
```

- [ ] **Step 2: Générer les icônes**

```bash
python - <<'PY'
import pathlib, struct, zlib

def png_uni(taille, rgb, chemin):
    """Génère un PNG monochrome sans dépendance externe."""
    r, g, b = rgb
    lignes = b"".join(b"\x00" + bytes([r, g, b]) * taille for _ in range(taille))
    def bloc(t, d):
        c = struct.pack(">I", len(d)) + t + d
        return c + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    ihdr = struct.pack(">IIBBBBB", taille, taille, 8, 2, 0, 0, 0)
    png = (b"\x89PNG\r\n\x1a\n" + bloc(b"IHDR", ihdr)
           + bloc(b"IDAT", zlib.compress(lignes)) + bloc(b"IEND", b""))
    pathlib.Path(chemin).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(chemin).write_bytes(png)

png_uni(192, (29, 78, 216), "app/icons/icone-192.png")
png_uni(512, (29, 78, 216), "app/icons/icone-512.png")
print("icones generees")
PY
```
Expected: `icones generees`, deux fichiers PNG bleus créés.

- [ ] **Step 3: Écrire le service worker**

```javascript
// app/sw.js
// Cache-first : l'app doit fonctionner sans réseau (usage en transports).
const CACHE = "capet-v1";

// Liste générée par build_cards.py : tous les SVG de schémas + les polices
// KaTeX réellement utilisées. Sans elle, un schéma jamais affiché avant la
// coupure réseau donne une image cassée, et les formules tombent sur une
// police de substitution.
importScripts("./sw-assets.js");   // définit self.ASSETS = [...]

const SOCLE = [
  "./", "./index.html", "./cards.json",
  "./css/style.css",
  "./js/app.js", "./js/store.js", "./js/scheduler.js", "./js/card-render.js",
  "./js/views/reviser.js", "./js/views/priorites.js", "./js/views/reglages.js",
  "./vendor/katex/katex.min.js", "./vendor/katex/katex.min.css",
  "./manifest.webmanifest",
  "./icons/icone-192.png", "./icons/icone-512.png",
  ...(self.ASSETS || []),
];

self.addEventListener("install", e => {
  e.waitUntil(
    caches.open(CACHE)
      // addAll échoue en bloc si un seul fichier manque : on tolère l'absence.
      .then(c => Promise.allSettled(SOCLE.map(u => c.add(u))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys()
      .then(noms => Promise.all(noms.filter(n => n !== CACHE).map(n => caches.delete(n))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  e.respondWith(
    caches.match(e.request).then(hit => hit || fetch(e.request).then(rep => {
      // Les SVG et polices sont mis en cache à la volée.
      if (rep.ok && new URL(e.request.url).origin === location.origin) {
        const copie = rep.clone();
        caches.open(CACHE).then(c => c.put(e.request, copie));
      }
      return rep;
    }).catch(() => {
      // Le fallback ne vaut que pour une NAVIGATION. Renvoyer index.html
      // pour un cards.json ou un .svg absent produirait une erreur de parse
      // JSON opaque au lieu d'un échec lisible.
      if (e.request.mode === "navigate") return caches.match("./index.html");
      return Response.error();
    }))
  );
});
```

- [ ] **Step 4: Enregistrer le service worker**

Ajouter à la fin du handler `DOMContentLoaded` dans `app/js/app.js` :

```javascript
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("sw.js").catch(() => { /* hors https/localhost */ });
  }
```

- [ ] **Step 5: Vérifier l'installabilité et le hors-ligne**

Run:
```bash
python scripts/build_cards.py
python -m http.server 8765 --directory . &
sleep 1
echo "Ouvrir http://localhost:8765/app/"
```

Liste de contrôle :
- [ ] Onglet Application → Manifest : aucune erreur, icônes affichées
- [ ] Onglet Application → Service Workers : `activated and is running`
- [ ] Onglet Network → cocher `Offline` → recharger : l'app démarre et les cartes s'affichent
- [ ] Toujours hors-ligne, naviguer vers Priorités : le tableau s'affiche
- [ ] Une carte schéma affiche bien son SVG hors-ligne — en **forçant** une carte de type `schema` (l'ordre de tirage étant pondéré, ne pas conclure sur une session où aucune n'est sortie)
- [ ] En mode sombre système, le schéma reste lisible (traits clairs sur fond sombre, pas d'aplat noir)

**Contrôle iPhone (la cible réelle)** — à faire sur le téléphone, pas seulement dans les outils développeur :
- [ ] Safari → Partager → « Ajouter à l'écran d'accueil » : l'icône et le nom « CAPET IE » apparaissent
- [ ] Lancée depuis l'écran d'accueil, l'app s'ouvre **sans la barre d'adresse Safari**
- [ ] Rien n'est masqué par l'encoche ni par la barre d'accueil (safe-areas)
- [ ] Mode Avion activé : l'app démarre et une session de révision complète est possible
- [ ] Les boutons Su / Hésité / Raté sont atteignables au pouce, sans repositionner la main

- [ ] **Step 6: Commit**

```bash
git add app/manifest.webmanifest app/sw.js app/icons app/js/app.js
git commit -m "feat(app): PWA installable et fonctionnelle hors-ligne"
```

---

### Task 14: Documentation et intégration au dépôt

**Files:**
- Create: `app/README.md`
- Modify: `CODEBASE_MAP.md`
- Modify: `CLAUDE.md`
- Create: `.gitignore` (entrées app)

**Interfaces:** aucune (task de clôture).

Conformément à l'instruction globale du projet, `CODEBASE_MAP.md` doit être mis à jour pour chaque fichier touché.

- [ ] **Step 1: Écrire le README de l'app**

```markdown
# App de révision CAPET SII·IE

PWA hors-ligne d'entraînement au rappel actif : formules, schémas,
conditions d'application. Le contenu est **généré** depuis `fiches/` —
ne jamais l'éditer à la main dans `app/`.

## Régénérer le contenu

```bash
python scripts/build_cards.py            # avec compilation des schémas (lent)
python scripts/build_cards.py --sans-svg # texte seul, itération rapide
```

Produit `app/cards.json` et `app/svg/*.svg`.

## Lancer en local

```bash
python -m http.server 8765 --directory .
# puis http://localhost:8765/app/
```

Un serveur est nécessaire : les modules ES et le service worker ne
fonctionnent pas en `file://`.

## Tests

```bash
python -m pytest tests/ -v                       # parseurs
python -m http.server 8765 --directory .          # app: /app/  tests: /tests/*.html
```

## Après avoir corrigé une fiche

Relancer `build_cards.py`. Les identifiants de cartes sont positionnels :
ajouter une formule **au milieu** d'une fiche décale les ids suivants et
désaligne la progression de ce thème. Ajouter en fin de section est sans
effet. En cas de doute, exporter la progression depuis Réglages avant de
régénérer.
```

- [ ] **Step 2: Mettre à jour CODEBASE_MAP.md**

Ajouter la section suivante (adapter si le fichier a une convention de tri) :

```markdown
## scripts/parse_formules.py
Extraction des cartes formule depuis les fiches Markdown.
- parse_table_formulas(section, theme) — formules en tableau Markdown
- parse_block_formulas(section, theme) — formules en blocs $$ avec conditions

## scripts/parse_pieges.py
Extraction des conditions d'application depuis la section 5 des fiches.
- parse_pieges(texte, theme) — items « piège / règle / erreur type »

## scripts/parse_meta.py
Métadonnées de thème depuis les .tex.
- parse_meta(tex) — code, titre, domaine, présence n/13, poids

## scripts/extract_tikz.py
Isolation des schémas TikZ des fiches.
- extract_tikz_envs(tex) — environnements tikzpicture/circuitikz + hash stable

## scripts/build_svg.py
Compilation des schémas en SVG thémables.
- themify(svg) — couleurs codées en dur vers currentColor/var(--svg-bg)
- compile_tikz(code, env, dest) — latex + dvisvgm vers un fichier SVG

## scripts/build_cards.py
Orchestrateur de génération du contenu de l'app.
- faire_id(theme, type, n) — identifiant stable de carte
- assembler(themes, cartes) — structure finale de cards.json
- construire(sans_svg) — parcourt fiches/ et produit la structure

## app/js/scheduler.js
Ordonnancement SM-2 pondéré par la fréquence au concours.
- etatInitial() — état d'une carte jamais vue
- noter(etat, note) — met à jour intervalle, facilité, échéance
- fileDuJour(cartes, progression, maintenant, taille) — file triée

## app/js/store.js
Persistance localStorage de la progression.
- charger() / sauver(prog) / majCarte(id, etat) — lecture-écriture
- exporter() / importer(json) / reinitialiser() — sauvegarde manuelle

## app/js/card-render.js
Rendu HTML des cartes, recto et verso.
- echapper(s) — échappement HTML
- rendreRecto(carte) / rendreVerso(carte) — selon type et niveau

## app/js/views/reviser.js
Écran de révision : file du jour, révélation, auto-notation.
- vueReviser(racine, data) — monte l'écran

## app/js/views/priorites.js
Écran de priorisation fréquence × maîtrise.
- calculerMaitrise(cartes, progression) — taux d'acquisition par thème
- ordonnerThemes(themes, maitrises) — tri par urgence décroissante
- vuePriorites(racine, data) — monte l'écran

## app/js/views/reglages.js
Écran export/import/réinitialisation.
- vueReglages(racine, data) — monte l'écran

## app/js/app.js
Routeur hash, thème clair/sombre, chargement de cards.json.

## app/sw.js
Service worker cache-first pour le fonctionnement hors-ligne.
```

- [ ] **Step 3: Documenter dans CLAUDE.md**

Ajouter avant la section « Conventions de contenu » :

```markdown
## App de révision (`app/`)

PWA hors-ligne d'entraînement au rappel actif, créée le 2026-09-21.
Trois types de cartes : **formule**, **piège** (conditions d'application),
**schéma** (3 niveaux : reconnaissance / calcul / tracé).

### Principe : l'app est un artefact régénérable

`app/cards.json` et `app/svg/` sont **générés** par `scripts/build_cards.py`
depuis `fiches/`. Ne jamais éditer de contenu pédagogique dans `app/` :
la prochaine génération l'écraserait. Les sources LaTeX/Markdown restent
l'unique source de vérité.

### Sources d'extraction

| Type de carte | Source | Volume |
|---|---|---|
| formule | `T{nn}_contenu.md` § 1 (tableau MD **et** blocs `$$`) | 344 |
| piège | `T{nn}_contenu.md` § 5 « Lacunes et pièges » | 199 |
| schéma | environnements TikZ des `T{nn}_*.tex` → SVG | 31 |

⚠ La section `## 3. ATTENTES DU JURY` n'est **pas** extraite, et ne doit pas
l'être : l'audit de véracité du 2026-09-20 a établi que 54 % des citations
jury étaient défectueuses. Importer ces encadrés propagerait des citations
fabriquées dans l'outil de révision.

### Pondération par la fréquence au concours

La pondération a **deux niveaux**, et les deux viennent des sources :

1. **Niveau thème** — le `\ficheEntete` de chaque fiche porte
   `Présence : n/13 sujets`. Ce ratio est le poids de base de toutes les
   cartes du thème.
2. **Niveau formule** — 114 formules portent une colonne `Fréquence`
   (`Systématique`, `Très fréquent`, `Présent`…) qui multiplie ce poids de
   base (0,9 à 1,3). Une formule systématique d'un thème fréquent passe
   ainsi devant une formule anecdotique du même thème.

Le poids pilote l'ordre de la file quotidienne et le calcul d'urgence de
l'écran Priorités (`urgence = poids × (1 − maîtrise)`).

### Piège : les identifiants de carte sont positionnels

Un id vaut `T19-f-003` (3ᵉ formule de T19 dans l'ordre du fichier). Insérer
une formule **au milieu** d'une section décale tous les ids suivants de ce
thème et désaligne la progression enregistrée. Ajouter en fin de section est
sans effet. Exporter la progression (écran Réglages) avant une refonte de fiche.

### Chaîne SVG

`latex` → `.dvi` → `dvisvgm --no-fonts --exact` → post-traitement des couleurs.
Le `--no-fonts` convertit le texte en tracés (aucune police à charger) ; le
post-traitement remplace `#000`/`#fff` par `currentColor`/`var(--svg-bg)`,
sans quoi les schémas sont invisibles en thème sombre.
```

- [ ] **Step 4: Vérifier que les artefacts restent hors du dépôt**

Le `.gitignore` a été écrit en Task 6 (avant le premier build). On contrôle
seulement qu'aucun artefact n'a été committé entre-temps.

```bash
git ls-files app/ | grep -E 'app/svg/|app/cards\.json|app/sw-assets\.js' && echo "ECHEC: artefacts committes" || echo "OK: aucun artefact dans l'index"
```
Expected: `OK: aucun artefact dans l'index`. Si des fichiers apparaissent, les désindexer avec `git rm --cached` avant de continuer.

Note : `cards.json`, `sw-assets.js` et les SVG sont exclus du dépôt car entièrement dérivés des sources. Quiconque clone lance `python scripts/build_cards.py`.

- [ ] **Step 5: Vérification finale de bout en bout**

Run:
```bash
python -m pytest tests/ -v
python scripts/build_cards.py
python -c "
import json, pathlib
d = json.loads(pathlib.Path('app/cards.json').read_text(encoding='utf-8'))
par = {}
for c in d['cards']: par[c['type']] = par.get(c['type'],0)+1
print('themes:', len(d['themes']), '| cartes:', len(d['cards']), '|', par)
ids = [c['id'] for c in d['cards']]
assert len(ids) == len(set(ids)), 'IDS DUPLIQUES'
assert all(c.get('poids') is not None for c in d['cards']), 'POIDS MANQUANT'
svgs = [c['svg'] for c in d['cards'] if c['type']=='schema']
manquants = [s for s in svgs if not pathlib.Path('app',s).exists()]
assert not manquants, f'SVG MANQUANTS: {manquants[:3]}'
print('coherence: OK')
"
```
Expected: tous les tests pytest passent, puis `coherence: OK`.

- [ ] **Step 6: Commit**

```bash
git add app/README.md CODEBASE_MAP.md CLAUDE.md .gitignore
git commit -m "docs: documentation de l'app de revision et mise a jour du CODEBASE_MAP"
```

---

## Ce que la v1 ne fait pas (périmètre explicitement exclu)

Décisions de non-faire, à ne pas « compléter » spontanément lors de l'exécution :

- **Pas de mode simulation chronométré.** Reporté en v2, après preuve d'usage.
- **Pas de lecteur de fiches ni de formulaire consultable.** Le manuel PDF le fait déjà mieux.
- **Pas de QCM à 4 options.** La bascule QCM est reportée : le format par défaut (révélation + auto-notation) doit être éprouvé seul d'abord, sinon on ne saura pas lequel des deux porte les résultats.
- **Pas d'extraction des questions types (§ 2 des fiches).** Elles relèvent du mode simulation, donc de la v2.
- **Pas de statistiques historiques ni de graphiques de progression.**
- **Pas de synchronisation multi-appareils.** L'export/import JSON manuel en tient lieu.

## Règle d'arrêt

Décidée en cadrage : si après deux semaines d'usage réel l'app n'est pas ouverte spontanément, le projet s'arrête et la révision retourne au manuel papier. Le corpus LaTeX n'est pas affecté — il n'a jamais été modifié par ce projet.
