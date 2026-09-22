# Design — Fiches de révision CAPET SII IE

Date : 2026-06-29

## Objectif

Produire un ensemble de fiches de révision imprimables (PDF via LaTeX) pour la préparation au CAPET SII option Ingénierie Électrique, session 2026.

## Ensemble cible

1. **Fiches thématiques** (~30 fiches, une par thème du programme)
2. **Fiches par domaine** (4–6 fiches regroupant les thèmes par grand domaine)
3. **Fiches transversales** (Formulaire global, Méthodes types, Points jury)

## Structure d'une fiche thématique (4–6 pages A4)

1. **En-tête** — code thème, titre, domaine, fréquence (N/13 sujets analysés)
2. **Rappels de cours** — définitions, lois fondamentales, schémas textuels
3. **Formulaire** — tableau : formule | notation | unité | condition d'application
4. **Questions types** — 2–3 questions extraites des sujets réels + corrigé rédigé
5. **Attentes du jury** — erreurs récurrentes, formulations attendues
6. **Pied de page** — années d'apparition dans les sujets

## Format technique

- **Langage** : LaTeX
- **Distribution** : MiKTeX (Windows)
- **Packages** : `geometry`, `tcolorbox`, `amsmath`, `siunitx`, `array`, `booktabs`, `multicol`, `xcolor`, `fontenc`, `inputenc`
- **Format papier** : A4, marges 1.5 cm
- **Couleurs par domaine** : Électrotechnique (bleu), Automatique (vert), Mécanique (orange), Thermique (rouge)

## Sources

Fichiers `.md` issus de la conversion Marker, sous :
`docs/CAPET_Markdown-20260629T134311Z-3-001/CAPET_Markdown/docs/CAPET_SII_IE/06_PDFs_Originaux/`

## Pilote

Thème T02 — Puissance AC (présent dans 100% des sujets).
Fichier de sortie : `fiches/T02_Puissance_AC.tex`

## Organisation des fichiers

```
fiches/
  T02_Puissance_AC.tex
  T03_Thermique.tex
  ...
  main.tex          — compile toutes les fiches en un seul PDF
  preamble.tex      — packages et commandes communes
```
