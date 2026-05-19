# Design — App de révision CAPET SII Ingénierie Électrique

**Date :** 2026-05-19  
**Statut :** Approuvé  
**Cible :** Session CAPET SII IE 2026

---

## Résumé

Application web statique (GitHub Pages) de révision pour le CAPET SII Ingénierie Électrique. SPA (Single Page Application) en Vanilla JS/HTML/CSS avec hash routing. Toutes les données sont pré-compilées depuis les fichiers Markdown existants via un script Python.

---

## Architecture générale

### Stack technique

- **Frontend :** Vanilla JS + HTML + CSS — zéro dépendance, zéro build step côté app
- **Hébergement :** GitHub Pages (purement statique)
- **Persistance :** `localStorage` pour la progression utilisateur
- **Routing :** Hash routing (`#/accueil`, `#/themes`, `#/theme/T02`, `#/formulaire`, `#/progression`)
- **Données :** Script Python `build.py` qui lit les `.md` et génère `app/data.js`

### Pipeline de données

```
docs/CAPET_SII_IE/**/*.md
        ↓
    build.py
        ↓
    app/data.js   (window.DATA = { themes, formules, sujets, rapports })
        ↓
    index.html
        ↓
  GitHub Pages
```

`build.py` est relancé manuellement après modification du contenu Markdown. `data.js` est commité avec le reste du code.

### Structure des fichiers

```
/
├── index.html              # Point d'entrée unique
├── app/
│   ├── data.js             # Données générées par build.py
│   ├── router.js           # Hash routing
│   ├── views/
│   │   ├── accueil.js
│   │   ├── themes.js
│   │   ├── theme.js        # Vue thème avec onglets
│   │   ├── formulaire.js
│   │   └── progression.js
│   ├── quiz/
│   │   ├── qcm.js
│   │   └── trous.js
│   ├── storage.js          # Abstraction localStorage
│   └── style.css
├── build.py                # Script de génération data.js
└── docs/                   # Sources Markdown (existantes)
```

---

## Vues

### 1. `#accueil` — Accueil intelligent

**Objectif :** orienter immédiatement vers ce qui mérite le plus d'attention.

**Composants :**
- **Compteurs en haut :** thèmes vus, formules maîtrisées, jours avant l'épreuve (date cible : 2026)
- **Suggestion prioritaire :** le thème 🔴 le moins avancé parmi ceux non maîtrisés (calculé depuis localStorage). Bouton "Commencer →" qui redirige vers `#theme/:id`
- **Points aveugles jury :** extraits de `points_aveugles.md` — 3 à 5 lacunes récurrentes signalées par le jury 2022–2025
- **Thèmes prioritaires :** liste des thèmes 🔴 et 🟠 avec barre de progression (% formules maîtrisées par thème)

**Logique de suggestion :** priorité = intensité × (1 - progression). Les thèmes 🔴 non commencés remontent en premier.

---

### 2. `#themes` — Liste des 30 thèmes

**Objectif :** vue d'ensemble et point d'entrée alternatif.

**Composants :**
- Liste des 30 thèmes (T01–T30) avec : intensité (🔴/🟠/🟡), nombre d'épreuves où présent, barre de progression formules
- Filtre par intensité : Tous / 🔴 Prioritaires / 🟠 Importants / 🟡 Mentionnés
- Clic → `#theme/:id`

---

### 3. `#theme/:id` — Vue thème

**Objectif :** point d'entrée de tout le travail sur un thème donné.

**Header :** nom du thème, badges (intensité, nb épreuves, nb formules ❌ restantes), barre de progression.

**4 onglets :**

#### Onglet Fiche (📖)
Contenu Markdown de `04_Fiches_Themes/T{id}_*.md` rendu en HTML.  
Pour les 23 thèmes sans fiche dédiée : afficher les formules du domaine correspondant avec leurs descriptions.

#### Onglet Formules (🧮)
Tableau des formules du thème extraites de `formulaire_capet.md` :
- Formule (rendue en LaTeX via KaTeX CDN)
- Description
- Donnée sujet (✅/❌)
- Fréquence
- Badge "Maîtrisée" (état localStorage)

#### Onglet Quiz (🧩)
Session de quiz sur les formules ❌ (à mémoriser) du thème.  
Les deux modes **alternent aléatoirement** à chaque question :

- **QCM :** 4 propositions. 3 distracteurs générés depuis les autres formules du même domaine (même structure, coefficient différent). Feedback immédiat + explication après réponse.
- **Texte à trous :** la formule s'affiche avec un terme masqué, 4 jetons cliquables. Le terme masqué est choisi parmi les variables/coefficients les plus discriminants (√3, cosφ, η, etc.).

Fin de session : score, liste des formules à revoir, sauvegarde en localStorage (nb correctes, nb tentatives par formule).

#### Onglet Sujets (📋)
Liste des années où le thème apparaît, avec son intensité par épreuve (extraite de `tableau_themes_capet.md`).  
Lien vers le fichier Markdown du sujet correspondant (affiché en lecture dans la même page ou dans un panneau latéral).

---

### 4. `#formulaire` — Toutes les formules

**Objectif :** référence rapide et quiz transversal.

**Composants :**
- Toutes les ~130 formules en tableau (KaTeX)
- Filtres : domaine, fréquence ≥ N, ❌ uniquement, non maîtrisées uniquement
- Barre de recherche texte
- Bouton "Quiz transversal" : lance un quiz sur les formules filtrées

---

### 5. `#progression` — Ma progression

**Objectif :** bilan et gestion de la progression sauvegardée.

**Composants :**
- Grille 30 thèmes avec % formules maîtrisées (couleur : rouge < 40%, orange 40–75%, vert > 75%)
- Total global : X / ~130 formules maîtrisées
- Bouton reset par thème ou reset global (avec confirmation)

---

## Données — structure de `data.js`

```js
window.DATA = {
  themes: [
    {
      id: "T02",
      nom: "Régime sinusoïdal / puissance (P, Q, triphasé)",
      intensite: "rouge",   // rouge | orange | jaune
      presences: { "2015_E1": "orange", "2015_E2": "jaune", ... },
      hasFiche: true,
      fichePath: "docs/CAPET_SII_IE/04_Fiches_Themes/T02_puissance_AC.md"
    },
    ...
  ],
  formules: [
    {
      id: "f001",
      themeId: "T02",
      domaine: "Électrotechnique — triphasé",
      latex: "P = \\sqrt{3}\\,U I \\cos\\varphi",
      description: "Puissance active triphasée",
      donnee: false,   // false = ❌ à mémoriser
      frequence: 6
    },
    ...
  ],
  sujets: [
    {
      annee: 2024,
      epreuve: "E1",
      titre: "Epreuve commune",
      themes: ["T02", "T14", "T30"],
      path: "docs/CAPET_SII_IE/01_Sujets/2024/Epreuve1_Commune/2024_Epreuve1_Commune.md"
    },
    ...
  ],
  pointsAveugles: [
    { texte: "Facteur de puissance cosφ mal appliqué", source: "Jury 2022–2025" },
    ...
  ],
  dateEpreuve: "2026-06-01"   // à ajuster selon calendrier officiel
}
```

---

## Rendu LaTeX

KaTeX chargé via CDN (`<link>` + `<script>` dans `index.html`). Rendu automatique sur tous les éléments `.katex-render` au chargement de chaque vue. Pas de MathJax (trop lourd). En cas d'absence de connexion, les formules s'affichent en LaTeX brut (dégradation acceptable, pas d'erreur bloquante).

---

## Progression — localStorage

```js
// Clé par formule
localStorage.setItem("formule_f001", JSON.stringify({ mastered: true, attempts: 3, correct: 2 }))

// Clé par thème (cache calculé)
localStorage.setItem("theme_T02_progress", "0.375")  // 3/8 formules maîtrisées
```

Une formule est considérée **maîtrisée** après 2 réponses correctes consécutives.

---

## Contraintes

- Purement statique : aucune requête serveur à l'exécution (sauf fetch des `.md` pour l'onglet Sujets, qui fonctionne sur GitHub Pages)
- `build.py` nécessite Python 3 et aucune dépendance externe (stdlib uniquement)
- Compatibilité navigateurs modernes uniquement (pas d'IE)
- KaTeX chargé via CDN (nécessite une connexion internet)
