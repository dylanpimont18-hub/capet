# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projet

Base documentaire pour la préparation au **CAPET SII option Ingénierie Électrique**, session 2026. Contient les ressources officielles et les outils de synthèse générés à partir de l'analyse des sujets 2015–2025.

## Structure des ressources

Tout le contenu est sous `docs/CAPET_SII_IE/` :

```
00_Programme_Referentiel/   — programme officiel session 2026
01_Sujets/{année}/          — sujets E1 (commune) + E2 (disciplinaire IE), 2015–2025
02_Rapports_Jury/           — rapports jury 2019, 2020, 2022–2025
03_Corriges/                — corrigés 2016, 2017, 2021
04_Fiches_Themes/           — fiches thématiques T02, T03, T11, T14, T21, T24, T30
```

Fichiers de synthèse à la racine de `docs/CAPET_SII_IE/` :

| Fichier | Rôle |
|---|---|
| `index_ressources.md` | Index complet de toutes les ressources avec chemins |
| `tableau_themes_capet.md` | Matrice 30 thèmes × 22 épreuves avec intensité (🔴/🟠/🟡) |
| `formulaire_capet.md` | ~130 formules classées par domaine, avec fréquence et si mémorisable |
| `plan_revision.md` | Plan de révision en 5 phases avec suivi de progression |
| `synthese_rapports_jury.md` | Synthèse des recommandations jury 2019–2025 |
| `points_aveugles.md` | Lacunes récurrentes signalées par le jury |

## Conventions de contenu

- **Formules** : notation LaTeX inline (`$...$`) dans les tableaux Markdown
- **Fréquence** dans `formulaire_capet.md` : nombre de sujets/corrigés/rapports où la formule apparaît
- **Intensité** dans `tableau_themes_capet.md` : 🔴 Central · 🟠 Important · 🟡 Mentionné · (vide) Absent
- **Données sujet** dans `formulaire_capet.md` : ✅ fournie dans le sujet · ❌ à restituer de mémoire

## Thèmes prioritaires (présents dans 100 % des sujets)

T02 Puissance AC · T03 Thermique · T11 Variation vitesse · T14 Distribution · T21 Modélisation · T24 Correcteurs · T30 Mécanique
