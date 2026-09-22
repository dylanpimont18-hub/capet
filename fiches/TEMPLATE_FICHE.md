# TEMPLATE — Fiches de révision CAPET SII Ingénierie Électrique

Ce fichier est lu par l'IA qui génère les fiches LaTeX. Il décrit **exactement** la structure, la mise en page et les règles à respecter pour que toutes les fiches soient visuellement et structurellement identiques.

---

## 1. Fichiers à utiliser

Le preamble commun à toutes les fiches est `preamble.tex`. Il contient les packages, couleurs et styles tcolorbox. **Ne jamais redéfinir dans le .tex de la fiche ce qui est déjà dans preamble.tex.**

Chaque fiche est un fichier autonome `{CODE}_{Titre}.tex` (ex : `T02_Puissance_AC.tex`) compilable directement avec `pdflatex`.

---

## 2. En-tête du fichier .tex

```latex
\documentclass[11pt,a4paper]{article}
\input{preamble}

\fancyhead[L]{\textbf{\textcolor{COULEUR_DOMAINE}{CODE}} · Titre court (max 5 mots)}
\fancyhead[R]{\small\textit{CAPET SII IE · Session 2026}}
\fancyfoot[C]{\small\thepage\,/\,\pageref{LastPage}}

\begin{document}
```

- `COULEUR_DOMAINE` : choisir parmi `colElec` (bleu), `colAuto` (vert), `colMeca` (orange), `colTherm` (rouge)
- `CODE` : ex. `T02`, `T11`, `T24`
- Le header gauche ne doit pas dépasser 35 caractères pour éviter la troncature

---

## 3. Structure des blocs — ordre obligatoire

Chaque fiche comporte exactement **5 blocs**, dans cet ordre, sans saut de page forcé entre eux :

```
[BLOC 0] En-tête
[BLOC 1] Rappels de cours
[BLOC 2] Formulaire synthétique
[BLOC 3] Questions types
[BLOC 4] Attentes du jury
[BLOC 5] Présence dans les sujets (pied)
```

---

## 4. BLOC 0 — En-tête de fiche

**Règle : ce bloc ne génère PAS de page blanche.** Il est directement suivi du Bloc 1 sur la même page.

```latex
\begin{tcolorbox}[
  enhanced, breakable,
  colback=COULEUR_DOMAINE,
  colframe=COULEUR_DOMAINE,
  left=6pt, right=6pt, top=5pt, bottom=5pt,
  before skip=0pt, after skip=4pt
]
  {\color{white}\bfseries\large CODE \quad Titre complet du thème}\\[2pt]
  {\color{colElecLight}\small          % adapter la couleur claire au domaine
    \textbf{Domaine :} NOM\_DOMAINE \quad
    \textbf{Présence :} \textbf{X/13} sujets (2013–2026) — [qualificatif]
  }\\[1pt]
  {\color{colElecLight!80!white}\footnotesize
    Sous-thèmes : mot-clé1 · mot-clé2 · mot-clé3 · mot-clé4
  }
\end{tcolorbox}
```

- `colElecLight` pour électrotechnique ; adapter si autre domaine (définir dans preamble si besoin)
- Le qualificatif de présence : "thème *systématiquement* présent" / "thème *très fréquent*" / "thème *fréquent*"
- Les sous-thèmes : 4 à 6 mots-clés séparés par ` · `

---

## 5. BLOC 1 — Rappels de cours

```latex
\begin{tcolorbox}[
  ficheSection=COULEUR_DOMAINE,
  title={1. Rappels de cours},
]
  % contenu ...
\end{tcolorbox}
```

### Règles de contenu

- Divisé en **sous-sections** numérotées `1.1`, `1.2`, `1.3`... en gras (`\textbf{1.1 Titre}`)
- Séparées par `\medskip\hrule\vspace{4pt}`
- Chaque sous-section : **définition** + **tableau** + éventuellement un **schéma TikZ**
- Maximum 3–4 sous-sections ; si le thème est plus riche, certains sous-thèmes vont dans le formulaire
- **Tableaux** : toujours avec `booktabs` (`\toprule`, `\midrule`, `\bottomrule`), `\renewcommand{\arraystretch}{1.45}`
- **Schéma TikZ obligatoire** si le thème a une représentation graphique naturelle (triangle des puissances, diagramme de Bode, schéma bloc, diagramme de Fresnel, courbe couple-vitesse…). Sinon, omettre.
- Pas de `\newpage` ni `\clearpage` dans ce bloc

### Modèle de sous-section avec tableau

```latex
\textbf{1.X Titre de la sous-section}

\smallskip
Phrase d'introduction courte (1–2 lignes maximum).

\begin{center}
\renewcommand{\arraystretch}{1.45}
\begin{tabular}{llll}
\toprule
\textbf{Grandeur} & \textbf{Symbole} & \textbf{Expression} & \textbf{Unité} \\
\midrule
Nom grandeur & $X$ & $X = ...$ & unité \\
\bottomrule
\end{tabular}
\end{center}
```

### Modèle de schéma TikZ (exemple triangle)

```latex
\begin{center}
\begin{tikzpicture}[scale=1.05, font=\small]
  % axes et vecteurs avec couleurs du domaine
  \draw[thick, COULEUR_DOMAINE, ->] (0,0) -- (3.2,0) node[right] {$...$};
  % angle
  \draw[COULEUR_DOMAINE!70!black] (0.7,0) arc[start angle=0, end angle=XX, radius=0.7];
  \node at (1.05, 0.2) {\footnotesize$\varphi$};
\end{tikzpicture}
\end{center}
```

---

## 6. BLOC 2 — Formulaire synthétique

```latex
\begin{tcolorbox}[
  ficheSection=COULEUR_DOMAINE,
  title={2. Formulaire synthétique},
]
\small
\begin{multicols}{2}
  % colonne gauche : formules fondamentales
  \renewcommand{\arraystretch}{1.45}
  \begin{tabular}{@{}p{3.8cm}ll@{}}
  \toprule
  \textbf{Formule} & \textbf{Usage} & \textbf{U.} \\
  \midrule
  % groupes séparés par \midrule avec titre \multicolumn
  \multicolumn{3}{@{}l}{\footnotesize\textit{Groupe 1}} \\
  $formule$ & usage & unité \\
  \bottomrule
  \end{tabular}

  \columnbreak

  % colonne droite : formules dérivées / cas particuliers
  \renewcommand{\arraystretch}{1.45}
  \begin{tabular}{@{}p{3.8cm}ll@{}}
  \toprule
  \textbf{Formule} & \textbf{Usage} & \textbf{U.} \\
  \midrule
  \multicolumn{3}{@{}l}{\footnotesize\textit{Groupe 2}} \\
  $formule$ & usage & unité \\
  \bottomrule
  \end{tabular}
\end{multicols}
\normalsize
\end{tcolorbox}
```

### Règles de contenu

- **2 colonnes obligatoires** via `multicols` — évite les pages blanches
- **8 à 16 formules** au total (en dessous : trop peu ; au-dessus : trop dense)
- Grouper par thématique avec des séparateurs `\multicolumn{3}{@{}l}{\footnotesize\textit{Nom groupe}}`
- Colonne droite en priorité pour : cas dérivés, rappels trigonométriques, conversions d'unités
- Formules en math mode `$...$`, jamais en mode display `\[...\]` dans ce tableau
- Si une formule est trop longue pour `p{3.8cm}`, la réécrire de façon plus compacte ou la mettre en dessous du tableau

---

## 7. BLOC 3 — Questions types

```latex
\begin{tcolorbox}[
  ficheSection=COULEUR_DOMAINE,
  title={3. Questions types — extraites des sujets réels},
]

\begin{tcolorbox}[questiontype,
  title={QT1 · Titre court de la question \hfill\normalfont\footnotesize Source exacte (ex: E2 disciplinaire 2024)}
]
  \textbf{Énoncé.} ...

  \tcbline

  \textbf{Corrigé.}

  \textbf{Étape 1 — Nom de l'étape.}
  \[ formule \]

  \textbf{Étape 2 — Nom de l'étape.}
  \[ formule \]
\end{tcolorbox}

\vspace{4pt}

% répéter pour QT2, QT3
\end{tcolorbox}
```

### Règles de contenu

- **2 à 3 questions types** par fiche (jamais 1, jamais plus de 3)
- Chaque QT comporte : **Énoncé** (données numériques exactes du sujet réel) + `\tcbline` + **Corrigé structuré en étapes**
- Les étapes du corrigé sont numérotées et nommées en gras : `\textbf{Étape 1 — Calcul de X.}`
- Les équations du corrigé sont **toujours en mode display** `\[...\]`, jamais inline — sauf les très courtes
- Pas plus de 3 `\qquad` dans une même équation display (risque d'overfull) — couper en 2 lignes si besoin
- Le résultat final de chaque étape est en **gras** : `\approx \mathbf{0{,}853}`
- **Dernière étape obligatoire — Conclusion.** Le corrigé ne s'arrête jamais sur un résultat numérique brut : une phrase finale relie explicitement le résultat à une exigence, un critère ou une conclusion attendue (ex. *"Cette valeur respecte le critère de chute de tension ≤ 5 % imposé par le cahier des charges."* / *"L'écart de 8 % dépasse la tolérance admise : la solution doit être revue."*). C'est une exigence directe des rapports de jury sur la justification des résultats (voir Bloc 4).
- La source est indiquée dans le titre, format : `E2 disciplinaire 2024` / `E1 2021` / `Rapport jury 2022`
- Si le corrigé officiel n'est pas disponible : le reconstituer proprement à partir de l'énoncé, et le marquer `[corrigé reconstitué]`

---

## 8. BLOC 4 — Attentes du jury

```latex
\begin{tcolorbox}[
  jury,
  title={4. Attentes du jury — Erreurs récurrentes et points de vigilance},
]

\begin{enumerate}[label=\textbf{\arabic*.}, leftmargin=*, itemsep=5pt]
  \item \textbf{Titre de l'erreur en gras.}
  Description concise (2–3 lignes). La méthode correcte est indiquée.

  \item ...
\end{enumerate}

\medskip
\begin{tcolorbox}[
  colback=colJuryFrame!12!colJury,
  colframe=colJuryFrame,
  left=4pt, right=4pt, top=2pt, bottom=2pt,
  fontupper=\small\itshape
]
Citation(s) directe(s) extraite(s) des rapports jury, entre guillemets français «~...~».
\end{tcolorbox}

\end{tcolorbox}
```

### Règles de contenu

- **6 à 8 points** numérotés, pas plus, pas moins
- Chaque point : titre en gras (l'erreur) + description + méthode correcte
- L'encadré de citations en bas est **obligatoire** : minimum 1 citation directe issue d'un rapport jury
- Formulation des titres : toujours à l'infinitif ou nominale — ex : "Confondre X et Y.", "Oublier le rendement.", "Ne pas vérifier le résultat."
- Ne pas répéter ce qui est déjà dans le cours — ces points sont uniquement des pièges et erreurs

---

## 9. BLOC 5 — Présence dans les sujets (pied de fiche)

```latex
\begin{tcolorbox}[
  enhanced, breakable,
  colback=colGrayLight,
  colframe=colSeparator,
  left=4pt, right=4pt, top=3pt, bottom=3pt,
  before skip=4pt, after skip=0pt,
  fonttitle=\small\bfseries,
  title={Présence dans les sujets analysés (2013–2026)},
]
\begin{center}
\footnotesize\renewcommand{\arraystretch}{1.15}
\begin{tabular}{lccccccccccccc}
\toprule
\textbf{Année} & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 20 & 21 & 22 & 23 & 24 & 25 \\
\midrule
E1 (commune)   & $\checkmark$ & ... \\
E2 discipl. IE & ... \\
\bottomrule
\end{tabular}
\end{center}
\smallskip
\footnotesize\textbf{Sous-thèmes fréquents :} sous-thème (X/13) · ...
\end{tcolorbox}
```

### Règles de contenu

- Tableau avec les 13 années de 2013 à 2025 (abréviées `13` à `25`)
- `$\checkmark$` si présent, `—` si absent
- Ligne E1 (commune à tous les candidats) + ligne E2 disciplinaire IE
- En dessous : liste des sous-thèmes avec leur fréquence `(X/13)`

---

## 10. Règles globales à respecter dans tout le fichier

### Mise en page
- **Jamais** de `\newpage`, `\clearpage`, `\pagebreak` explicite — laisser LaTeX gérer
- **Jamais** de tcolorbox non `breakable` — tout doit avoir l'option `breakable`
- Les équations longues (>1 `\qquad`) sont coupées sur 2 lignes `\[...\]` séparées
- Espacements entre blocs : `\vspace{4pt}` entre les QT, les blocs se suivent sans espace spécial

### Formules
- Unités : toujours via `\si{\...}` ou `\SI{valeur}{\...}` du package `siunitx`
- Décimales françaises : `0{,}85` (jamais `0.85` ni `0,85` sans accolade)
- Milliers : `\,` comme séparateur : `179\,100` (jamais `179100`)
- Vecteurs complexes soulignés : `\underline{Z}`, `\overline{\underline{I}}`

### Typographie
- Abréviations d'unités hors siunitx : VAR, kVAR, VA, kVA en mode texte `\text{VAR}`
- Citations jury : guillemets français `«~...~»`
- Emphase : `\textbf{}` pour les termes importants, `\textit{}` pour les sources et citations

### Ce que l'IA ne doit PAS faire
- Inventer des formules non présentes dans les sources
- Créer une 4e question type si seulement 2 sont disponibles dans les sources
- Mettre `\newpage` pour forcer la mise en page
- Utiliser `title style={colback=...}` (clé tikz invalide) — utiliser `colbacktitle=...`
- Mettre plus de 3 `\qquad` dans une même ligne display
- Sommer des $S_k$ directement (erreur pédagogique)

---

## 11. Correspondance couleurs / domaines

| Domaine | Clé couleur | Couleur claire associée |
|---|---|---|
| Électrotechnique | `colElec` | `colElecLight` |
| Automatique | `colAuto` | `colAuto!15!white` |
| Mécanique | `colMeca` | `colMeca!15!white` |
| Thermique | `colTherm` | `colTherm!15!white` |

Les couleurs claires (`colElecLight`, etc.) sont utilisées pour le texte sur fond coloré dans le Bloc 0.
Si le domaine n'est pas électrotechnique, définir `\definecolor{colXXXLight}{RGB}{...}` dans preamble.tex avant de générer.

---

## 12. Checklist avant de soumettre le .tex généré

- [ ] Le Bloc 0 ne génère pas de page blanche — le contenu commence sur la même page
- [ ] Toutes les tcolorbox ont l'option `breakable`
- [ ] Le formulaire est en 2 colonnes avec `multicols`
- [ ] Il y a exactement 2 ou 3 questions types avec source exacte
- [ ] Chaque QT a son `\tcbline` séparant énoncé et corrigé
- [ ] Chaque corrigé se termine par une phrase de conclusion reliant le résultat à une exigence/un critère
- [ ] Le Bloc 4 contient au moins une citation directe de rapport jury
- [ ] Le Bloc 5 (tableau de présence) est présent et complet
- [ ] Aucun `\newpage` ni `title style={colback=...}`
- [ ] Les décimales sont au format `0{,}XX`
- [ ] Le header gauche fait moins de 35 caractères
