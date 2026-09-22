# PROGRESSION_EXERCICES.md

Tableau de bord de la banque d'exercices CAPET SII IE (`exercices/`).
Régénéré par scan de `exercices/*.tex` (compter les occurrences de `\begin{tcolorbox}[exoBox` par fichier) et comparaison avec `FILE_EXERCICES.md`.

Dernière régénération : 2026-07-16 (T18, T19 ajoutés).

**Correction post-audit (audit `exercices/AUDIT_EXERCICES_2026.md` du 2026-08-25)** — état au 2026-09-02 :
- **Lot 1 vérifié** : T01, T03, T08, T09, T10, T12, T14, T15, T16, T17.
- **Lot 2 vérifié** (2026-09-02) : T02, T04, T05, T06, T07, T11, T13, T18, T19 — 9/9 `VERDICT: OK` en vérification indépendante (recalcul from scratch de toutes les AN, contrôle du traitement des constats §4, recompilation des 2 variantes par le vérificateur, étanchéité énoncés/corrigés). Les constats §2.3 (doublons avec les fiches) et §2.5 (absence d'exercice `docTech`) restent hors périmètre et non traités sur l'ensemble du corpus.
- **Non-régression confirmée** : le C_th ≈ 557 N·m de T11 (constat RÉFUTÉ §3.3) est resté intact et a été reconstruit indépendamment depuis E2_Sujet_2019 (557,0 N·m).
- **Point ouvert tranché** : voir T08 ci-dessous (formule f_P).
- ✅ **T08 exercice 4 — corrigé le 2026-09-02** : le facteur de puissance du P3 valait 0,827, valeur fausse issue d'une formule apocryphe `f_P = (q/π)·sin(π/q)` (q = pulsations). Vérification à la source (`E1_Sujet_2026.md` l.654-664) : le sujet ne donne sa formule `f_P = (2/π)·√q·sin(π/q)` (q = nombre de **phases**) que pour le **PD3** (question E9 → 0,955) ; la question E8, sur le P3, demande au candidat de l'établir lui-même. L'exercice fait désormais établir f_P du P3 (I_D,eff = I_S/√3, P_A = ⟨u_S⟩·I_S, S = √3·V·I_S) → **f_P = 3√2/2π ≈ 0,675**, confirmé par deux voies indépendantes (bilan de puissances et facteur de distorsion du créneau 120°). La formule du sujet n'est plus employée que pour le PD3. Conclusion pédagogique inchangée (P3 écarté, PD3 retenu), l'écart au critère 0,9 est même plus net.
- **Consolidation `fiches/preamble.tex` (2026-09-02)** : `group-minimum-digits=4` ajouté au `\sisetup` (les nombres à 4 chiffres passés en `\SI` étaient rendus sans séparateur, ex. « 6000 Hz »), et les unités `ar`, `ad`, `	r` déclarées une fois pour toutes, sous garde `\ifdefined`. Les déclarations locales restées dans 9 fichiers d'exercices ont été mises sous garde pour éviter tout conflit de redéfinition. Corpus entier recompilé après ce changement : **38/38 compilations d'exercices** (19 notions × énoncés/corrigés) et **30/30 fiches**, toutes rc = 0, aucune régression.

**Chantier « entraînement complémentaire » (2026-09-02, décision utilisateur)** — les deux constats systémiques §2.3 et §2.5 de l'audit ont été traités sur les **18 notions concernées** (T01 était déjà disjointe de sa fiche) :
- **§2.3 doublons** : tout exercice reprenant la même source ET le même travail intellectuel qu'une Question Type de la fiche a été remplacé par d'autres questions **des mêmes sujets réels** (chaque sujet en contient 40 à 65). Recours à l'inédit en dernier ressort seulement.
- **§2.5 docTech** : 18/19 notions disposent désormais d'un exercice de lecture de document technique, avec encadré `docTech` et première question d'extraction. T01 n'en a pas (hors chantier).
- **Correction de l'audit dans les deux sens** : doublons supplémentaires trouvés (T17 : 5 au lieu de 4 ; T18 : doublon franc et non partiel ; T03 : recouvrement bien plus lourd que le « mineur » annoncé) et faux doublons écartés (T05, T09, T14, T08 ont conservé des exercices que l'audit condamnait à tort, après réidentification source par source).
- **Deux fiches corrigées** au passage, car elles contredisaient les exercices :
  - `fiches/T08_Redresseurs.tex` : f_P(P3) 0,827 → **0,675**, formule apocryphe `(q/π)·sin(π/q)` remplacée par la définition générale `f_P = (I₁,eff/I_eff)·cos φ₁`. La formule ne reproduisait même pas la valeur PD2 du propre tableau de la fiche (0,637 au lieu de 0,90).
  - `fiches/T18_Composants_Electroniques.tex` : **QT3 physiquement fausse**. Elle décrivait une diode écrêtant une SURtension à V_ref + 0,6 = 4,1 V ; le corrigé officiel (`Rapport_Jury_2022.md` l.343) établit que la protection joue contre une tension **NÉGATIVE** née de l'inversion du courant dans le shunt R₀, avec écrêtage à **−0,6 V**. QT3 réécrite, référence d'épreuve corrigée.
- **Passe de vérification indépendante** (5 notions les plus à risque : T03, T08, T15, T17, T18) : 4 `VERDICT: OK`, 2 `A_REPRENDRE` portant sur des défauts que j'avais moi-même introduits ou laissés, tous corrigés depuis :
  - **T03** : mes remplacements de texte avaient laissé deux fragments orphelins rendus dans les PDF, dont un « ΔU_max = 8 % » contredisant la conclusion à 5 % dans la même phrase. Supprimés, citation jury remise au verbatim exact, recompilé.
  - **`fiches/T08_Redresseurs.tex`** : j'avais corrigé les *valeurs* mais laissé la **formule apocryphe** `(q/π)·sin(π/q)` à deux endroits rendus (Bloc 1 et Bloc 4). Un candidat suivant la consigne retombait mécaniquement sur 0,827. Remplacée par la définition générale (facteur de distorsion / bilan de puissances) avec avertissement explicite qu'aucune formule unique en q ne vaut pour tous les montages.
  - **`fiches/T17_Distribution_Securite.tex`** : citation jury 2021 **fabriquée** (« Il est impératif de justifier le choix du disjoncteur… ») — introuvable dans le rapport, dont l'unique occurrence d'« impératif » (l.969) porte sur un tout autre sujet. Remplacée par le verbatim exact de la l.769.
- **Sauvegarde** des 19 sources avant réécriture (scratchpad `backup_avant_complementarite/`), `exercices/` n'étant pas suivi par git.
- Corpus recompilé : **38/38 variantes rc = 0**, gradations monotones partout, étanchéité énoncés/corrigés vérifiée sur les 19 notions. Seuls échecs : `fiches/T02_pilote_v1/v2/v3.tex`, fichiers pilotes de la comparaison de styles du 2026-08-25 qui font `\input{preamble}` puis redéfinissent `icheHeaders` — conflit préexistant, sans rapport avec ce changement ; ils n'ont jamais produit de PDF et sont candidats à la suppression.

## Électrotechnique (T01–T17)

| Notion | Exercices | Générée |
|---|---|---|
| T01 — Grandeurs électriques, électrocinétique | 5 | ✓ |
| T02 — Puissance en régime alternatif sinusoïdal | 5 | ✓ |
| T03 — Représentation complexe, impédances | 5 | ✓ |
| T04 — Harmoniques réseau, THD, puissance déformante | 5 | ✓ |
| T05 — Phénomènes thermiques | 5 | ✓ |
| T06 — Transformateur | 5 | ✓ |
| T07 — Hacheurs | 5 | ✓ |
| T08 — Redresseurs | 5 | ✓ |
| T09 — Onduleurs | 5 | ✓ |
| T10 — Mécanique | 6 | ✓ |
| T11 — Machine à courant continu | 6 | ✓ |
| T12 — Machine synchrone | 5 | ✓ |
| T13 — Machine asynchrone | 5 | ✓ |
| T14 — Variation de vitesse | 6 | ✓ |
| T15 — Stockage d'énergie | 6 | ✓ |
| T16 — Énergies renouvelables | 6 | ✓ |
| T17 — Distribution et sécurité électrique | 6 | ✓ |

## Électronique (T18–T25)

| Notion | Exercices | Générée |
|---|---|---|
| T18 — Composants électroniques | 6 | ✓ |
| T19 — AOP | 6 | ✓ |
| T20 — Filtres RC/RL | 0 | ✗ |
| T21 — Fonctions de transfert, Bode | 0 | ✗ |
| T22 — CAN/CNA, numérisation | 0 | ✗ |
| T23 — Capteurs, conditionnement | 0 | ✗ |
| T24 — Systèmes embarqués | 0 | ✗ |
| T25 — Transmission numérique | 0 | ✗ |

## Automatique (T26–T29)

| Notion | Exercices | Générée |
|---|---|---|
| T26 — Modélisation des systèmes | 0 | ✗ |
| T27 — Systèmes bouclés, correcteurs | 0 | ✗ |
| T28 — Logique combinatoire | 0 | ✗ |
| T29 — Logique séquentielle, GRAFCET | 0 | ✗ |

## Mesurage (T30)

| Notion | Exercices | Générée |
|---|---|---|
| T30 — Mesurage, instrumentation | 0 | ✗ |

**Total : 19/30 notions traitées, 103 exercices générés.**

## Mise à jour 2026-09-20 — corpus complet

- **30/30 notions** générées, **171 exercices** au total.
- T20–T30 ajoutées ce jour (6 exercices chacune), chacune avec un exercice `docTech`
  et une passe d'inspection visuelle PNG des schémas.
- 60/60 PDF par notion (énoncés + corrigés) compilés rc = 0.
- `exercices/main.tex` inclut désormais les 30 notions : `main_enonces.pdf` 115 p.,
  `main_corriges.pdf` 150 p.
- Ces exercices alimentent aussi le manuel assemblé `manuel/main.pdf` (378 p.).
- **Thèmes non sourçables** (0 occurrence dans le corpus 2013–2026) : GRAFCET interrogé,
  Karnaugh/table de vérité, incertitudes/classe de précision, FPGA/VHDL. Les exercices
  correspondants sont inédits et marqués comme tels.
