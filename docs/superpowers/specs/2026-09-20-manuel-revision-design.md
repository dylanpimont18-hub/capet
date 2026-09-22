# Manuel de révision imprimable — CAPET SII IE, session 2026

Date : 2026-09-20
Statut : approuvé par l'utilisateur, en cours d'implémentation

## Objectif

Produire un manuel de révision imprimable unique, entrelaçant le cours (30 fiches
`fiches/T01..T30.tex`) et les exercices (`exercices/T{nn}_exercices.tex`), avec les
corrigés regroupés en annexe.

## Décisions actées

| Sujet | Décision |
|---|---|
| Structure | Entrelacée par notion : cours T01 → exercices T01 → cours T02 → … |
| Corrigés | En annexe de fin, pas en regard de l'énoncé |
| Notions T20–T30 | Exercices générés AVANT l'assemblage (manuel complet du premier coup) |
| Mécanique corrigés | Approche A — capture différée dans `\CAPETSHOW` |
| Vérification | Passe indépendante par notion, comme pour T01–T19 |

## Architecture

Assemblage sans duplication : une seule source par fiche et par exercice.

```
manuel/main.tex     — couverture, sommaire, parties, \include, annexe, index
fiches/preamble.tex — MODIFIÉ : \CAPETSHOW à 3 modes
fiches/T01..T30.tex — inchangés
exercices/T01..T19.tex — inchangés ; T20..T30 à créer
```

Structure du PDF : couverture → sommaire → Partie I Électrotechnique (T01–T17) →
Partie II Électronique (T18–T25) → Partie III Automatique (T26–T29) →
Partie IV Mesurage (T30) → Annexe A corrigés → index des formules.

## Mécanique `\CAPETSHOW`

État actuel (`fiches/preamble.tex:82`) :

    \newcommand{\CAPETSHOW}[2]{\ifdefined\CAPETCORRIGE #2\else #1\fi}

Le drapeau est global et fixé au lancement de `pdflatex` : un document rend soit tous
les énoncés, soit tous les corrigés. Le manuel a besoin des deux dans un même PDF.

Trois modes après refonte, le comportement par défaut restant identique :

| Mode | Drapeau | Comportement |
|---|---|---|
| Énoncés | *(aucun)* | imprime l'énoncé — inchangé |
| Corrigés | `\CAPETCORRIGE` | imprime le corrigé — inchangé |
| Manuel | `\CAPETMANUEL` | imprime l'énoncé, diffère le corrigé vers l'annexe |

En mode manuel : numérotation continue des exercices, renvois croisés cliquables
(`hyperref`) entre énoncé et corrigé.

### Risque identifié et critère de vérification

La capture différée ré-exécute du contenu LaTeX hors de son contexte d'origine ; les
environnements `circuitikz`/`tikz` et les caractères spéciaux doivent y survivre.

Critère de contrôle : le nombre de corrigés rendus en annexe doit égaler le nombre
d'exercices du corpus, et chaque corrigé du manuel doit correspondre à celui du PDF
séparé de sa notion.

Repli si la capture par fichier auxiliaire s'avère fragile sur les schémas : stockage
en macros, même interface `\CAPETSHOW`, à signaler à l'utilisateur.

## Ordre de travail

1. Refonte `\CAPETSHOW` + non-régression des 38 variantes existantes (fait en premier :
   point technique risqué et court, à valider avant d'investir dans la génération).
2. Exercices T20–T30 (11 notions × 5–6 exercices) + vérification indépendante par notion.
3. Assemblage `manuel/` : sommaire, parties, sauts de page aux frontières de notion
   (dans le fichier d'assemblage uniquement), index des formules.
4. Vérification finale : compilation, comptage des corrigés, contrôle visuel PNG.
5. Mise à jour de `CLAUDE.md` et `CODEBASE_MAP.md`, en retard sur la réalité du dépôt
   (ils annoncent 4 notions d'exercices au lieu de 19).

## Contraintes à respecter

- Règle CLAUDE.md : pas de `\newpage`/`\clearpage` dans les fiches. Les sauts de page
  aux frontières de notion vivent dans `manuel/main.tex`, jamais dans les sources.
- Décimales françaises `0{,}85`, unités via `siunitx`, `\underline{Z}` pour les complexes.
- Ne pas retirer `\AtBeginDocument{\shorthandoff{:;!?}}` (babel french casse circuitikz).
- Les trois chaînes de compilation existantes doivent continuer à produire exactement
  les mêmes PDF.
