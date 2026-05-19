# Prompt d'implémentation — App de révision CAPET SII IE

Envoyer ce prompt tel quel à Claude Sonnet 4.6. Il contient tout le contexte nécessaire.

---

## PROMPT À ENVOYER

Tu vas implémenter une application web de révision pour le CAPET SII Ingénierie Électrique. Voici tout ce dont tu as besoin.

---

## Contexte du projet

**Répertoire de travail :** `c:\Users\Dylan\Desktop\CAPET`

Le projet contient des fichiers Markdown dans `docs/CAPET_SII_IE/` :
- `formulaire_capet.md` — ~130 formules en tableaux Markdown avec LaTeX
- `tableau_themes_capet.md` — matrice 30 thèmes × 22 épreuves (intensités 🔴/🟠/🟡)
- `points_aveugles.md` — lacunes signalées par le jury
- `01_Sujets/AAAA/NomDossier/fichier.md` — sujets d'examen 2015–2025
- `04_Fiches_Themes/T02_*.md`, `T03_*.md`, etc. — 7 fiches thématiques

**Ce que tu vas construire :** une SPA statique (zéro backend, fonctionne en `file://` ou GitHub Pages) en Vanilla JS/HTML/CSS avec hash routing.

**Contraintes strictes :**
- Vanilla JS uniquement — zéro framework, zéro dépendance npm
- Purement statique — tout fonctionne sans serveur (sauf fetch des .md pour l'onglet Sujets)
- Python 3 stdlib uniquement pour `build.py`
- KaTeX via CDN pour le rendu LaTeX

---

## Structure des fichiers à créer

```
c:\Users\Dylan\Desktop\CAPET\
├── index.html
├── build.py
├── app/
│   ├── data.js             ← généré par build.py, à commiter
│   ├── router.js
│   ├── storage.js
│   ├── theme.js            ← toggle jour/nuit
│   ├── katex-render.js
│   ├── style.css
│   ├── views/
│   │   ├── accueil.js
│   │   ├── themes.js
│   │   ├── theme.js
│   │   ├── formulaire.js
│   │   └── progression.js
│   └── quiz/
│       ├── qcm.js
│       └── trous.js
```

---

## Task 1 — build.py

Crée `build.py` à la racine. Il lit les `.md` et génère `app/data.js`.

### Règles de parsing

**formulaire_capet.md** — tables Markdown sous des headers `## N. Titre` :
```
| $latex$ | Description | ✅/❌ | Fréq |
```
- Extraire le LaTeX entre `$...$`
- `donnee = true` si `✅` dans la 3e colonne
- `frequence` = entier de la 4e colonne
- `themeId` déduit du titre de section (voir mapping ci-dessous)

**Mapping section → themeId :**
```python
DOMAIN_TO_THEME = {
    "thermique": "T03", "thermodynamique": "T03",
    "énergies renouvelables": "T13", "stockage": "T12",
    "électrotechnique": "T02", "câblage": "T14", "distribution": "T14",
    "hacheurs": "T05", "convertisseurs": "T05",
    "mas": "T10", "asynchrone": "T10",
    "machines électriques": "T11",
    "automatique": "T24", "asservissement": "T24",
    "cinématique": "T30", "rdm": "T30", "mécanique": "T30",
    "modélisation": "T21",
}
# Si aucun match → "T01"
```

**tableau_themes_capet.md** — 1ère table (intensité), s'arrêter avant "## Tableau de présence" :
```
| T02 – Nom du thème | 🟠 | 🟡 | ... |
```
- Extraire l'id `T02`, le nom (sans le préfixe `TXX – `)
- Colonnes = années/épreuves (en-têtes : `2015 E1`, `2015 E2`, etc.)
- Mapping emoji → intensité : `🔴`→`"rouge"`, `🟠`→`"orange"`, `🟡`→`"jaune"`, vide→absent
- `intensite` globale = max des présences
- `hasFiche` = `True` si `T02`, `T03`, `T11`, `T14`, `T21`, `T24`, `T30`
- `fichePath` = chemin relatif du .md correspondant dans `04_Fiches_Themes/`

**Clé de colonne** : transformer `2015 E1` en `2015_E1` pour le dict `presences`.

**points_aveugles.md** — extraire les items de liste sous forme `- **Titre** : détail` → `{ texte, detail, source }`. Garder les 10 premiers.

**01_Sujets/** — scanner récursivement les `.md`. Pour chaque fichier :
- Extraire l'année depuis le composant de chemin qui matche `\d{4}`
- `epreuve = "E1"` si `"Epreuve1"` dans le nom, sinon `"E2"`
- `path` = chemin relatif depuis la racine du projet (format POSIX)
- `themes[]` = rempli après en croisant avec `presences` (clé `{annee}_E{num}`)

### Données `trou` pour le quiz

Pour chaque formule, détecter si elle contient un terme masquable :
```python
TROU_CANDIDATES = [
    (r"\\sqrt\{3\}", r"\sqrt{3}", [r"\sqrt{2}", r"3", r"2\pi", r"\sqrt{3}/2"]),
    (r"\\cos\\varphi", r"\cos\varphi", [r"\sin\varphi", r"\tan\varphi", r"\varphi", r"\cos^2\varphi"]),
    (r"\\eta", r"\eta", [r"\varphi", r"\alpha", r"\omega", r"g"]),
    (r"\\omega", r"\omega", [r"\Omega", r"2\pi f", r"\omega_0", r"p"]),
    (r"\balpha\b", r"\alpha", [r"\beta", r"\eta", r"1-\alpha", r"\omega"]),
    (r"\bg\b", r"g", [r"1-g", r"g^2", r"N_s", r"\omega_s"]),
]
```
Si un terme matche, ajouter à la formule :
```python
"trou": {
    "maskedTerm": term,
    "maskedLatex": re.sub(pattern, r"\\square", latex, count=1),
    "choices": [term] + distractors[:3]
}
```
Sinon `"trou": None`.

### Structure de app/data.js

```js
// Généré par build.py — ne pas modifier manuellement
window.DATA = {
  themes: [
    {
      id: "T02",
      nom: "Régime sinusoïdal / puissance (P, Q, triphasé)",
      intensite: "rouge",          // "rouge"|"orange"|"jaune"|"absent"
      presences: { "2015_E1": "orange", "2016_E2": "rouge", ... },
      hasFiche: true,
      fichePath: "docs/CAPET_SII_IE/04_Fiches_Themes/T02_puissance_AC.md"
    }
  ],
  formules: [
    {
      id: "f001",
      themeId: "T02",
      domaine: "Électrotechnique — Puissance & Réseaux",
      latex: "P = \\sqrt{3}\\,U\\,I\\,\\cos\\varphi",
      description: "Puissance active triphasée",
      donnee: false,
      frequence: 6,
      trou: {
        maskedTerm: "\\sqrt{3}",
        maskedLatex: "P = \\square\\,U\\,I\\,\\cos\\varphi",
        choices: ["\\sqrt{3}", "\\sqrt{2}", "3", "2\\pi"]
      }
    }
  ],
  sujets: [
    {
      annee: 2024,
      epreuve: "E1",
      titre: "2024 Epreuve1 Commune",
      path: "docs/CAPET_SII_IE/01_Sujets/2024/Epreuve1_Commune/2024_Epreuve1_Commune.md",
      themes: ["T02", "T14", "T30"]
    }
  ],
  pointsAveugles: [
    { texte: "...", detail: "...", source: "Rapports jury 2019–2025" }
  ],
  dateEpreuve: "2026-06-01"
};
```

**Après avoir créé build.py**, l'exécuter :
```bash
python build.py
```
Vérifier la sortie : `✅ app/data.js — 30 thèmes, N formules, 22 sujets`

---

## Task 2 — index.html

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
    <button id="theme-toggle" onclick="Theme.toggle()">☀️ Jour</button>
  </nav>
  <main id="app">Chargement…</main>

  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

  <script src="app/data.js"></script>
  <script src="app/storage.js"></script>
  <script src="app/katex-render.js"></script>
  <script src="app/theme.js"></script>
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

---

## Task 3 — app/style.css

CSS complet. Variables CSS pour les deux thèmes :

```css
:root {
  --bg: #0d1117; --bg2: #161b22; --bg3: #21262d; --border: #30363d;
  --text: #e6edf3; --text2: #8b949e;
  --rouge: #f85149; --orange: #fb923c; --jaune: #e3b341;
  --vert: #3fb950; --bleu: #58a6ff; --violet: #bc8cff;
  --radius: 8px;
}

body.light {
  --bg: #f6f8fa; --bg2: #ffffff; --bg3: #eaeef2; --border: #d0d7de;
  --text: #1f2328; --text2: #656d76;
  --rouge: #cf222e; --orange: #bc4c00; --jaune: #9a6700;
  --vert: #1a7f37; --bleu: #0969da; --violet: #8250df;
}
```

Composants CSS à inclure (avec leurs classes) :

- **Base** : `*, body, #app` (max-width 900px, padding 32px 24px, centré)
- **Nav** : `#nav` sticky, height 52px, `#theme-toggle` (border pill, margin-left auto)
- **Nav active** : `.nav-link`, `.nav-link.active` (couleur texte)
- **Cards** : `.card` (background bg2, border, border-radius, padding 20px)
- **Badges** : `.badge`, `.badge-rouge`, `.badge-orange`, `.badge-jaune`, `.badge-bleu`, `.badge-vert`
- **Barre de progression** : `.progress-bar` + `.progress-fill` + `.progress-fill.rouge/orange/vert`
- **Onglets** : `.tabs`, `.tab`, `.tab.active` (border-bottom bleu)
- **Boutons** : `.btn`, `.btn-primary`, `.btn-success`, `.btn-danger`, `.btn-ghost`
- **Tableau formules** : `.formule-table` (width 100%, border-collapse)
- **Quiz** : `.quiz-option` (hover + `.correct` vert + `.wrong` rouge + `.disabled`), `.jeton` (`.selected` violet)
- **Grille progression** : `.progression-grid` (CSS grid auto-fill minmax 200px)
- **Utilitaires** : `.text-muted`, `.text-sm`, `.mt-4`, `.mt-8`, `.flex`, `.flex-col`, `.gap-2`, `.gap-4`, `.items-center`, `.justify-between`
- **Mode clair** : `body.light #nav`, `body.light .quiz-option`, `body.light .jeton`

---

## Task 4 — app/katex-render.js

```js
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

---

## Task 5 — app/theme.js (toggle jour/nuit)

```js
const Theme = (() => {
  const KEY = "capet_theme";

  function apply(mode) {
    document.body.classList.toggle("light", mode === "light");
    const btn = document.getElementById("theme-toggle");
    if (btn) btn.textContent = mode === "light" ? "🌙 Nuit" : "☀️ Jour";
  }

  function init() {
    apply(localStorage.getItem(KEY) || "dark");
  }

  function toggle() {
    const next = document.body.classList.contains("light") ? "dark" : "light";
    localStorage.setItem(KEY, next);
    apply(next);
  }

  return { init, toggle };
})();
```

---

## Task 6 — app/storage.js

```js
const Storage = (() => {
  const PREFIX = "capet_";

  function key(id) { return PREFIX + "f_" + id; }

  function getFormule(id) {
    try {
      return JSON.parse(localStorage.getItem(key(id))) ||
        { mastered: false, correct: 0, attempts: 0, consecutive: 0 };
    } catch {
      return { mastered: false, correct: 0, attempts: 0, consecutive: 0 };
    }
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
    localStorage.setItem(key(id), JSON.stringify(s));
    return s;
  }

  function isMastered(id) { return getFormule(id).mastered; }

  function getThemeProgress(themeId) {
    const formules = window.DATA.formules.filter(f => f.themeId === themeId && !f.donnee);
    if (!formules.length) return 1;
    return formules.filter(f => isMastered(f.id)).length / formules.length;
  }

  function resetTheme(themeId) {
    window.DATA.formules
      .filter(f => f.themeId === themeId)
      .forEach(f => localStorage.removeItem(key(f.id)));
  }

  function resetAll() {
    Object.keys(localStorage)
      .filter(k => k.startsWith(PREFIX))
      .forEach(k => localStorage.removeItem(k));
  }

  function getPriorityScore(theme) {
    const poids = { rouge: 3, orange: 2, jaune: 1, absent: 0 };
    return (poids[theme.intensite] || 0) * (1 - getThemeProgress(theme.id));
  }

  return { getFormule, recordAnswer, isMastered, getThemeProgress, resetTheme, resetAll, getPriorityScore };
})();
```

---

## Task 7 — app/router.js

```js
const ROUTES = {
  "/accueil":     ()  => renderAccueil(),
  "/themes":      ()  => renderThemes(),
  "/theme/:id":   (p) => renderTheme(p.id),
  "/formulaire":  ()  => renderFormulaire(),
  "/progression": ()  => renderProgression(),
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
  document.querySelectorAll(".nav-link").forEach(a => {
    a.classList.toggle("active", window.location.hash.startsWith(a.getAttribute("href")));
  });
}

window.addEventListener("hashchange", navigate);
window.addEventListener("DOMContentLoaded", () => {
  Theme.init();
  if (!window.location.hash) window.location.hash = "#/accueil";
  navigate();
});
```

---

## Task 8 — app/views/accueil.js

La vue accueil affiche :

1. **Titre** + badge `J-N` (jours avant `DATA.dateEpreuve`)
2. **3 stat cards** : thèmes vus (progress > 0), formules maîtrisées, formules restantes
3. **Carte suggestion** (border-left vert) : thème rouge/orange avec le plus haut `Storage.getPriorityScore()`, avec sa barre de progression et un bouton "Commencer →" → `#/theme/TXX`
4. **Carte points aveugles** (border-left jaune) : 4 premiers items de `DATA.pointsAveugles`
5. **Liste thèmes prioritaires** : thèmes rouge + orange triés par priorité (max 6), chacun avec barre de progression et lien vers `#/theme/TXX`

Fonctions helper globales (réutilisées par d'autres vues) :
- `statCard(val, label, icon)` → HTML string
- `themeRow(t)` → HTML string (lien + card + barre de progression)

---

## Task 9 — app/views/themes.js

La vue affiche les 30 thèmes filtrables :

1. **Titre + sous-titre**
2. **4 boutons filtre** : Tous / 🔴 Prioritaires / 🟠 Importants / 🟡 Mentionnés
3. **Liste de cards** : chaque thème → badge id, nom, "X/22 épreuves · Y formules à mémoriser", barre de progression. Clic → `#/theme/TXX`

Fonction `filterThemes(filter)` : affiche/masque les `<a>` selon `data-intensite`. Met à jour le bouton actif.

---

## Task 10 — app/views/theme.js

Vue la plus complexe. Affiche `#theme/:id`.

**Header** : `← Tous les thèmes`, nom du thème, 3 badges (intensite, nb épreuves, nb formules restantes), barre de progression globale.

**4 onglets** : Fiche / Formules / Quiz / Sujets. Fonction `switchTab(event, name)` gère l'affichage (`display:none`/`block`) et relit KaTeX sur l'onglet activé.

### Onglet Fiche

- Si `theme.hasFiche` : afficher un `<div id="fiche-content">` et le remplir via `fetch(theme.fichePath).then(md => mdToHtml(md))`
- Sinon : tableau des formules du thème avec latex et description

`mdToHtml(md)` — convertisseur Markdown minimal (h1/h2/h3, gras, listes, paragraphes). Attention : ne pas casser les formules LaTeX `$...$`.

### Onglet Formules

Tableau `.formule-table` avec colonnes : Formule (KaTeX), Description, Donnée ?, Fréq., État (badge vert si maîtrisée).

### Onglet Quiz

Voir Task 11.

### Onglet Sujets

Voir Task 12.

---

## Task 11 — app/quiz/qcm.js + app/quiz/trous.js

### qcm.js

Fonction `renderQCMQuestion(formule, allFormules)` → HTML string.

- Affiche la **description** de la formule (question)
- 4 options : la bonne formule (LaTeX) + 3 distracteurs tirés aléatoirement parmi les formules du même domaine, ou du même thème si pas assez
- Clic sur option → `answerQCM(qid, isCorrect, formuleId)` :
  - Disable toutes les options
  - Mettre en vert la correcte, en rouge la choisie si fausse
  - Appeler `Storage.recordAnswer(formuleId, isCorrect)`
  - Afficher feedback (correct/raté + formule complète + état maîtrise)
  - Dispatcher `new CustomEvent("quizAnswer", { detail: { formuleId, isCorrect } })`

Fonction `shuffle(arr)` globale.

### trous.js

Fonction `renderTrouQuestion(formule)` → HTML string ou `null` si `!formule.trou`.

- Affiche la description + formule avec `\square` à la place du terme masqué (rendu KaTeX)
- 4 jetons cliquables (choices mélangés)
- Clic jeton → `answerTrou(qid, chosen, correct, formuleId)` :
  - Disable les jetons
  - Feedback (correct/raté + formule complète)
  - `Storage.recordAnswer` + CustomEvent `"quizAnswer"`

---

## Task 12 — Onglet Quiz (dans app/views/theme.js)

Variable module-level `let _quizSession = null`.

**`renderOngletQuiz(themeId, formulesAMemoriser)`** :
- Si toutes maîtrisées → message 🏆 + bouton "Recommencer" (reset + reload)
- Sinon → container avec `#quiz-question`, `#quiz-next` (hidden), `#quiz-results` (hidden)

**`startQuiz(themeId)`** :
- Construire queue = formules non maîtrisées du thème, shuffled
- `_quizSession = { themeId, queue, index: 0, correct: 0, total: 0 }`
- Appeler `nextQuizQuestion()`
- Écouter `"quizAnswer"` via `document.addEventListener`

**`nextQuizQuestion()`** :
- Si `index >= queue.length` → `showQuizResults()`
- Sinon : tirer la formule suivante, choisir aléatoirement QCM ou trous (si `formule.trou` existe et `Math.random() < 0.5`), injecter dans `#quiz-question`, renderMath, incrémenter index
- Afficher `#quiz-next` après réponse (via event `"quizAnswer"`)

**`showQuizResults()`** :
- Retirer l'event listener
- Afficher score dans `#quiz-results` (emoji selon %, nb correct/total, bouton Rejouer)

**`switchTab`** doit appeler `startQuiz(id)` quand on bascule sur l'onglet quiz.

---

## Task 13 — Onglet Sujets (dans app/views/theme.js)

**`renderOngletSujets(theme)`** :
- Filtrer `DATA.sujets` par `s.themes.includes(theme.id)`
- Pour chaque sujet : card avec année, épreuve, titre, badge intensité (depuis `theme.presences[colKey]`)
- Bouton "📄 Lire le sujet" → `loadSujet(btn, path)` :
  - `fetch(path).then(md => mdToHtml(md))` → afficher dans un `div.sujet-content`
  - Toggle : second clic replie
  - En cas d'erreur fetch (mode file://) : message explicatif

---

## Task 14 — app/views/formulaire.js

**`renderFormulaire()`** :
- Titre + sous-titre (N formules)
- `<input>` recherche texte (filtre par description)
- `<select>` domaines (options générées depuis les domaines distincts)
- Boutons toggle "❌ À mémoriser" et "🎯 Non maîtrisées"
- Compteur "N formules affichées"
- Tableau `.formule-table` : colonnes Formule (KaTeX), Description, Domaine, Donnée ?, Fréq., État. Chaque `<tr>` a `data-id`, `data-domaine`, `data-desc` (lowercase), `data-donnee`, `data-mastered`
- Bouton "🧩 Quiz transversal" → `startQuizTransversal()`

**`filterFormulaire()`** : filtre les `<tr>` selon les 4 critères, met à jour le compteur.

**`startQuizTransversal()`** :
- Récupérer les `<tr>` visibles via `data-id`
- Construire formules subset (non donnee)
- Réutiliser `_quizSession`, `nextQuizQuestion`, `showQuizResults` (fonctions globales de theme.js)
- Container quiz dans `#quiz-transversal`

---

## Task 15 — app/views/progression.js

**`renderProgression()`** :
- Compteur global : N/total formules maîtrisées + barre de progression + % + bouton "🗑️ Tout réinitialiser" (avec `confirm()`)
- Titre "Par thème"
- Grille `.progression-grid` : 30 cellules `.progression-cell`, chacune avec badge id, nom tronqué, barre de progression colorée, bouton "Reset" (avec `confirm()`)
- Couleur barre : rouge si < 40%, orange si 40–75%, vert si > 75%
- Reset thème → `Storage.resetTheme(id)` + `window.location.reload()`
- Reset tout → `Storage.resetAll()` + `window.location.reload()`

---

## Ordre d'implémentation

Implémenter dans cet ordre exact (chaque étape dépend des précédentes) :

1. `build.py` → exécuter → vérifier `app/data.js`
2. `app/style.css`
3. `app/katex-render.js`
4. `app/theme.js`
5. `app/storage.js`
6. `app/router.js` + stubs vides pour toutes les vues (pour que le router ne plante pas)
7. `index.html`
8. Ouvrir dans le navigateur — vérifier nav + routing + toggle jour/nuit
9. `app/views/accueil.js`
10. `app/views/themes.js`
11. `app/quiz/qcm.js` + `app/quiz/trous.js`
12. `app/views/theme.js` (onglets Fiche + Formules + Quiz + Sujets — tout en une fois)
13. `app/views/formulaire.js`
14. `app/views/progression.js`

---

## Vérification finale

Lancer : `python -m http.server 8080` puis ouvrir `http://localhost:8080`

Golden path à tester :
1. Accueil → suggestion visible, jours avant épreuve, points aveugles listés
2. Toggle ☀️/🌙 → bascule les couleurs sur toutes les vues
3. Clic "Commencer →" → vue thème T02
4. Onglet Formules → tableau KaTeX rendu correctement
5. Onglet Quiz → QCM et/ou trous s'affichent, feedback après réponse, score final
6. Onglet Sujets → liste des épreuves avec badges, bouton "Lire" charge le sujet
7. `#/themes` → filtre "🔴 Prioritaires" masque les autres
8. `#/formulaire` → recherche + filtre "❌ À mémoriser" + quiz transversal
9. `#/progression` → grille 30 thèmes, reset par thème fonctionnel
10. Après avoir répondu 2× correctement à une formule → badge ✓ dans l'onglet Formules + barre de progression mise à jour

---

## Notes importantes

- **Fonctions globales** partagées entre vues : `shuffle()`, `renderMath()`, `mdToHtml()`, `_quizSession`, `nextQuizQuestion()`, `showQuizResults()`, `onQuizAnswer()`, `startQuiz()` — toutes dans `theme.js` ou `qcm.js`, accessibles globalement car chargées sans module
- **KaTeX** : si hors ligne, les formules s'affichent en LaTeX brut — comportement acceptable, ne pas bloquer sur ça
- **fetch des .md** : fonctionne sur `http://localhost:8080` et GitHub Pages, mais pas en `file://` — afficher un message explicatif dans ce cas
- **`\square`** dans les trous : c'est du LaTeX valide que KaTeX rend comme □
- **Tâches 12 et 13** modifient toutes les deux `app/views/theme.js` — les faire dans la foulée
