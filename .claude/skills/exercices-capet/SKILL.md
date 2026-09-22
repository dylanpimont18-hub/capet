---
name: exercices-capet
description: Use when generating CAPET SII (option Ingénierie électrique) practice-exercise worksheets — triggered by queue mode ("fais-moi N notions d'exercices") or on-demand mode ("fais-moi des exercices sur [notion]")
---

# Banque d'exercices CAPET SII IE — Option Ingénierie électrique

## Contexte projet

Répertoire : `c:\Users\Dylan\Desktop\CAPET`

Indépendant du skill de fiches de cours (`fiches/`, LaTeX) : ce skill produit des **exercices
d'entraînement** dans `exercices/`, un fichier par notion, énoncé et corrigé dans le même PDF.

Sources de contenu :
- **Notions** : pas de référentiel dédié — reprend exactement le découpage `T01`–`T30` des fiches
  existantes. Table complète (code, titre, domaine) dans `CODEBASE_MAP.md` (section
  `fiches/T{nn}_contenu.md`) et `CLAUDE.md` (tableau domaines/couleurs).
- **Sujets réels** : chercher par mot-clé dans
  `docs/CAPET_Markdown-20260629T134311Z-3-001/CAPET_Markdown/docs/CAPET_SII_IE/06_PDFs_Originaux/{année}/*.md`
  (source la plus complète, 2013–2026 — voir `CODEBASE_MAP.md`), en complément
  `docs/CAPET_SII_IE/07_Ecrits_1ere_session/Markdown/*.md` (2025). Un exercice adapté d'un sujet réel
  cite sa référence exacte `"année, [nom de l'épreuve tel qu'il figure dans le sujet], question n°Y"`
  — ne pas supposer un nom d'épreuve, le lire dans le fichier source.
- **Rapports de jury** : même arborescence batch, `Rapport_Jury_*.md` (2018–2025 disponibles).

Fichiers de suivi (racine projet) : `FILE_EXERCICES.md` (file ordonnée), `PROGRESSION_EXERCICES.md`
(tableau de bord, régénéré par scan de `exercices/*.tex`).

L'utilisateur est candidat au CAPET externe SII, option Ingénierie électrique : tous les exercices
visent le **niveau réel des épreuves écrites du CAPET**, sans version "pédagogique" simplifiée.

---

## Mode file d'attente

Déclencheur : *"Fais-moi N notions d'exercices"*

1. Lire `FILE_EXERCICES.md` → prendre les N premières entrées non cochées `[ ]`
2. Générer les exercices de chaque notion (voir Génération)
3. Cocher les entrées `[x]`, ajouter `\include{T{nn}_exercices}` dans `exercices/main.tex` (ordre T01→T30)
4. Régénérer `PROGRESSION_EXERCICES.md`

## Mode à la demande

Déclencheur : *"Fais-moi des exercices sur [notion]"*

1. Retrouver le code `T{nn}` de la notion (table `CODEBASE_MAP.md`/`CLAUDE.md`, par titre ou mot-clé)
2. Générer les exercices de cette notion
3. Cocher l'entrée dans `FILE_EXERCICES.md`, ajouter l'`\include` dans `main.tex`, régénérer
   `PROGRESSION_EXERCICES.md`

---

## Sélection des exercices (4 à 6 par notion)

1. **Sujets réels** en priorité (voir sources ci-dessus, toutes années disponibles).
2. **Exercices inédits** pour compléter à 4-6. Référence affichée : `"exercice inédit"`. Ne jamais
   présenter un exercice inventé comme extrait d'un sujet réel.

Chaque exercice porte une difficulté 1 à 3 via `\difficulte{n}` (macro `preamble.tex`), calibrée sur
l'exigence CAPET — ne pas transposer un niveau agrégation si vous disposez des deux banques en parallèle.

### Exercice "lecture de document technique"

Sur les notions qui s'y prêtent naturellement (machines électriques, transformateur, redresseurs,
variation de vitesse — pas les notions purement analytiques comme les représentations complexes),
inclure **un exercice de la banque** (pas plus) construit sur un **extrait de document technique réel**
(datasheet constructeur, plaque signalétique, extrait de cahier des charges, schéma coté) plutôt que des
données déjà mises en forme pour le calcul. Rapport de jury 2022 : *"l'exploitation de documents
techniques pour la réalisation de schémas électriques est attendu d'un candidat au CAPET"* — de nombreux
candidats échouent à en extraire les bonnes données, pas à calculer une fois les données données.

- L'extrait de document est présenté dans un encadré `docTech` dédié (style `preamble.tex`), distinct
  visuellement de l'énoncé — voir gabarit ci-dessous.
- La **première question** est toujours une question d'extraction/lecture ("Identifier dans la plaque
  signalétique...", "Relever sur l'abaque...") — jamais un calcul direct sur des valeurs déjà isolées.
  Les questions suivantes enchaînent sur le calcul une fois les données extraites.
- Source du document : sujet réel si disponible (cité normalement), sinon un extrait plausible
  reconstitué à partir d'un ordre de grandeur vérifié par `WebSearch` — jamais inventé au hasard.

```latex
\begin{tcolorbox}[exoBox,
  title={Exercice N -- \difficulte{[1-3]} \hfill\normalfont\footnotesize [référence]}
]
\CAPETSHOW{
\begin{tcolorbox}[docTech, title={Document technique -- [nom, ex: Plaque signalétique moteur asynchrone}]
[extrait : tableau de valeurs, plaque signalétique, extrait de datasheet...]
\end{tcolorbox}

[contexte bref]

\begin{enumerate}
  \item Identifier dans le document [...] nécessaire(s) au calcul de [...].
  \item [question de calcul s'appuyant sur les valeurs extraites]
\end{enumerate}
}{
\textbf{Corrigé.}

\textbf{Étape 1 — Extraction des données.}
[valeurs relevées et leur provenance dans le document]

[étapes de calcul suivantes]
}
\end{tcolorbox}
```

## Vérification web (obligatoire)

Toute valeur numérique, norme ou ordre de grandeur professionnel non déjà sourcé mot pour mot dans un
sujet réel cité doit être vérifié avec `WebSearch`/`WebFetch` avant rédaction, source citée en commentaire
LaTeX (`%`) en tête du fichier. Si les sources divergent, le dire dans le corrigé plutôt que trancher
arbitrairement. Ne pas re-vérifier les faits mathématiques/physiques de base non controversés.

## Points de vigilance jury

Chercher par mot-clé dans les `Rapport_Jury_*.md` un point pertinent pour l'exercice ; si trouvé,
l'ajouter en fin de corrigé avec sa référence (`"rapport de jury CAPET année"`). Sinon, omettre plutôt
que d'en forcer une hors-sujet.

---

## Génération des exercices d'une notion

### Fichier à produire

Un seul fichier `exercices/T{nn}_exercices.tex`, standalone-compilable, même mécanisme que
`fiches/T{nn}_*.tex` (toggle `\CAPETINCLUDEMODE`/`\CAPETBEGINFILE`/`\CAPETENDFILE`), préambule partagé
via `\input{../fiches/preamble}`. Voir `exercices/T01_exercices.tex` comme référence structurelle.

```latex
\expandafter\ifx\csname CAPETINCLUDEMODE\endcsname\relax
\documentclass[11pt,a4paper]{article}
\input{../fiches/preamble}
\def\CAPETBEGINFILE{\begin{document}}
\def\CAPETENDFILE{\end{document}}
\else
\def\CAPETBEGINFILE{}
\def\CAPETENDFILE{}
\fi

\fancyhead[L]{\textbf{\textcolor{colExo}{T{nn}}} - Exercices - [Titre]}
\fancyhead[R]{\small\textit{Banque d'exercices \CAPETSHOW{(\'enonc\'es)}{(corrig\'es)}}}
\fancyfoot[C]{\small\thepage\,/\,\pageref{LastPage}}

\CAPETBEGINFILE

% en-tête (bloc colExo, cf. T01_exercices.tex) — ajouter \CAPETSHOW{(énoncés)}{(corrigés)}
% après "Banque d'exercices -- N exercices" dans le sous-titre, comme dans le fancyhead

\begin{tcolorbox}[exoBox,
  title={Exercice 1 -- \difficulte{[1-3]} \hfill\normalfont\footnotesize [référence]}
]
\CAPETSHOW{
[contexte + questions numérotées]
}{
\textbf{Corrigé.}

[démarche + résultats]

\textbf{Conclusion.} [phrase reliant le résultat à une exigence/un critère du cahier des charges ou de
l'énoncé -- ne jamais s'arrêter sur un résultat numérique brut, cf. rapport de jury 2019 sur la
justification des écarts]
}
\end{tcolorbox}

% ... jusqu'à 4-6 exercices

\CAPETENDFILE
```

Énoncé et corrigé d'un même exercice partagent la **même tcolorbox `exoBox`** mais dans des branches
`\CAPETSHOW{<énoncé>}{<corrigé>}` distinctes (macro définie dans `fiches/preamble.tex`) : une seule
source par notion, mais **deux PDF distincts** à la compilation (énoncés seuls / corrigés seuls) — voir
la section Compilation ci-dessous. Pas de `\tcbline` : les deux branches ne sont jamais rendues
ensemble.

### Schémas

Dès qu'un exercice porte sur un circuit ou un signal temporel, ajouter un schéma juste après le
paragraphe de contexte (avant `\begin{enumerate}`) :
- **Circuits** (diviseurs, mailles, redresseurs, RL/RC, hacheurs...) : `circuitikz`, option
  `[european, scale=0.8-0.9]` (résistances en rectangle, pas de zigzag américain). Inductance :
  `to[cute inductor, l=...]` (pas `to[L, ...]`, qui rend un bloc plein sous ce préambule). Toujours
  fermer les nœuds partagés avec `node[circ]{}` plutôt que de superposer deux `\draw` non reliés.
- **Chronogrammes** (signaux périodiques, créneaux) : `tikzpicture` nu (axes `-latex`, paliers en
  `\draw[thick]`, repères en `\draw[dotted]` + `node[below]`) — voir `exercices/T01_exercices.tex`,
  exercice 5, comme référence directe à copier/adapter.
- **Piège connu** : ne jamais chaîner un `to[sV]`/`to[V]` entre deux segments `to[short]` de longueur
  nulle dans un même `\draw` (ex. deux sources empilées reliées par un `to[short]`) — cela produit un
  glyphe parasite dans le symbole de la source. Donner à chaque source son propre segment isolé
  (coordonnées de départ/arrivée non partagées avec une autre source), voir la topologie de l'exercice 3
  (bus neutre + bus de sortie verticaux, phases horizontales) comme patron pour tout montage à plusieurs
  sources.
- Après génération, **toujours compiler** (`pdflatex`) et rendre la page en PNG (`pdftoppm -png -r 150`)
  pour vérifier visuellement le schéma avant de considérer l'exercice terminé — un schéma qui compile
  sans erreur peut quand même être topologiquement faux ou visuellement cassé.

### Compilation

Deux PDF par notion, générés depuis la même source via le drapeau `\CAPETCORRIGE` (2 passes chacun,
pour `\pageref{LastPage}`) :

```powershell
cd exercices
# PDF enonces seuls (mode par defaut, \CAPETCORRIGE non defini) :
pdflatex -interaction=nonstopmode -jobname=T{nn}_enonces T{nn}_exercices.tex
pdflatex -interaction=nonstopmode -jobname=T{nn}_enonces T{nn}_exercices.tex
# PDF corriges seuls (drapeau defini avant l'input) :
pdflatex -interaction=nonstopmode -jobname=T{nn}_corriges "\def\CAPETCORRIGE{1}\input{T{nn}_exercices.tex}"
pdflatex -interaction=nonstopmode -jobname=T{nn}_corriges "\def\CAPETCORRIGE{1}\input{T{nn}_exercices.tex}"
```

Même principe pour `main.tex` (`main_enonces.pdf` / `main_corriges.pdf`) : le drapeau se propage aux
notions incluses via `\include`, aucune modification de `main.tex` n'est nécessaire.

## PROGRESSION_EXERCICES.md — format attendu

Voir le fichier pour le format exact (tableau par domaine, colonnes "Exercices"/"Générée" ✓/✗).
Régénérer en comptant les occurrences de `\begin{tcolorbox}[exoBox` par fichier `exercices/T{nn}_exercices.tex`.

## Prérequis (déjà créés — ne pas recréer)

- `fiches/preamble.tex` — styles `exoBox`, couleur `colExo`, macro `\difficulte{n}`, macro `\CAPETSHOW`
  (bascule énoncé/corrigé), package `circuitikz` et correctif `\AtBeginDocument{\shorthandoff{:;!?}}`
  (babel français casse la syntaxe `to[...]` de circuitikz sinon — voir commentaire dans le fichier) —
  tout ajouté pour ce skill
- `exercices/main.tex`, `FILE_EXERCICES.md`, `PROGRESSION_EXERCICES.md`
- `exercices/T01_exercices.tex` — premier exemple généré et compilé, 5 exercices avec schémas
  (diviseur, mailles, redresseur P3, RL, chronogramme) — référence structurelle
