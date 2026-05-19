# Plan de révision — CAPET SII Ingénierie Électrique

> Basé sur : `tableau_themes_capet.md` · `synthese_rapports_jury.md` · `formulaire_capet.md` · Programme session 2026
>
> **Point de départ :** mai 2026. Selon votre situation :
> - **Admissible session 2026** → priorité aux phases Oral (phases 4–5)
> - **Préparation session 2027** → suivre toutes les phases dans l'ordre

---

## Vue d'ensemble

| Phase | Contenu | Durée conseillée |
|---|---|---|
| 1 | Fondamentaux non négociables | 3–4 semaines |
| 2 | Thèmes prioritaires (top fréquence) | 6–8 semaines |
| 3 | Thèmes secondaires et transversaux | 4 semaines |
| 4 | Entraînement sur annales | 4–6 semaines |
| 5 | Préparation orale (leçon + entretien) | 3–4 semaines |

---

## Phase 1 — Fondamentaux non négociables

> Le jury signale ces lacunes **dans tous les rapports**. Sans elles, la majorité des questions de toutes les parties sont bloquées.

### 1.1 Électricité fondamentale

- [ ] Loi des nœuds, loi des mailles, loi d'Ohm (DC et AC)
- [ ] Régime sinusoïdal : représentation de Fresnel, impédances complexes
- [ ] Puissances AC monophasé : P = U·I·cosφ, Q = U·I·sinφ, S = U·I
- [ ] Puissances AC triphasé : P = √3·U·I·cosφ — relations tensions étoile/triangle
- [ ] Triangle des puissances, facteur de puissance cosφ
- [ ] Énergie : E = P·t (formule à restituer de mémoire, fréquence 7)

### 1.2 Mathématiques de base (signalées comme lacune jury)

- [ ] Conversions d'unités : W ↔ kW ↔ MW, J ↔ kWh, tr/min ↔ rad/s
- [ ] Trigonométrie : sin, cos, tan, loi des sinus, Pythagore
- [ ] Résolution d'équation du 1er degré, coefficient directeur d'une droite
- [ ] Analyse dimensionnelle systématique (vérification homogénéité)

### 1.3 Mécanique de base

- [ ] ω = 2π·N/60 (conversion tr/min → rad/s)
- [ ] P = C·ω (puissance mécanique)
- [ ] PFD en translation : ΣF = m·a
- [ ] PFD en rotation : ΣC = J·α
- [ ] **Théorème de l'énergie cinétique (TEC)** — inconnu de la majorité (jury 2024) : ΔEc = W_total

### 1.4 Machines électriques essentielles

- [ ] MAS : vitesse synchrone Ns = 60f/p, glissement g = (Ns–N)/Ns
- [ ] MAS : courant nominal In = Pu/(η·√3·U·cosφ)
- [ ] Rapport de réduction i = ω_moteur/ω_charge = C_charge/C_moteur
- [ ] Rendement global : η_global = Π η_i

**Durée estimée :** 3–4 semaines, 1h/jour

---

## Phase 2 — Thèmes prioritaires

> Classés par fréquence et intensité au concours (source : `tableau_themes_capet.md`)

### Priorité 1 — Présents dans > 80 % des sujets avec forte intensité

| Thème | Fréq. | Intensité moy. | Fiche disponible |
|---|:---:|:---:|:---:|
| T02 – Régime sinusoïdal / puissance | 22/22 | 🔴 | `04_Fiches_Themes/T02_puissance_AC.md` |
| T14 – Production / distribution / câblage | 22/22 | 🔴 | `04_Fiches_Themes/T14_distribution.md` |
| T03 – Thermique | 22/22 | 🟠 | `04_Fiches_Themes/T03_thermique.md` |
| T11 – Variation de vitesse | 22/22 | 🟠 | `04_Fiches_Themes/T11_variation_vitesse.md` |
| T21 – Modélisation (FT, schéma-blocs) | 22/22 | 🟠 | `04_Fiches_Themes/T21_modelisation.md` |
| T30 – Mécanique (cinématique, RDM) | 22/22 | 🟠 | `04_Fiches_Themes/T30_mecanique.md` |
| T24 – Correcteurs / asservissement | 5/22 | 🟠 | `04_Fiches_Themes/T24_correcteurs.md` |

**Pour chaque thème :**
1. Lire la fiche thématique correspondante
2. Réviser les formules dans `formulaire_capet.md`
3. Traiter les questions du thème dans 3 sujets récents

### Priorité 2 — Présents régulièrement (≥ 50 %)

| Thème | Fréq. | À réviser |
|---|:---:|---|
| T13 – ENR (PV, éolien, hydraulique) | 22/22* | Surface PV, MPPT, STEP, H₂ |
| T12 – Stockage d'énergie | 22/22* | Batteries (C_b = E/U), STEP, supercap |
| T20 – Capteurs & mesure | 22/22* | Pont Wheatstone, CAN, codeurs |
| T28 – Programmation / algorithmique | 22/22* | Python, organigrammes, API |
| T27 – API / GRAFCET | 13/22 | GRAFCET, langages Ladder/ST, séquenceurs |
| T29 – Réseaux industriels | 13/22 | Modbus, CAN bus, I2C, SPI, LoRa |

*Présents dans les sujets mais intensité variable selon les années.

**Durée estimée phase 2 :** 6–8 semaines, 1h30/jour

---

## Phase 3 — Thèmes secondaires et transversaux

> Moins fréquents comme fil conducteur, mais apparaissent régulièrement en questions isolées.

| Thème | Fréq. binaire | Travail à faire |
|---|:---:|---|
| T07 – Onduleurs / MLI | 12/22 | MLI sinus-triangle, commande IGBT, harmoniques |
| T22 – Réponse indicielle | 10/22 | Identification ordre 1 et 2, K, τ, ξ |
| T15 – Sécurité électrique / régimes neutre | 9/22 | TT, TN-S, IT — courant défaut, déclenchement |
| T23 – Analyse fréquentielle / Nyquist | 8/22 | Diagramme de Bode asymptotique, marge phase/gain |
| T17 – Fonctions de transfert / filtres | partiel | Ordre 1 et 2, filtres passe-bas/haut |
| T05 – Hacheurs DC-DC | 7/22 | Buck, Boost, rapport cyclique α |
| T09 – Machine synchrone / MSAP | 7/22 | FEM, équation de tension, commande vectorielle |

**Durée estimée phase 3 :** 4 semaines, 1h/jour

---

## Phase 4 — Entraînement sur annales

> Le jury recommande **explicitement** dans tous les rapports de s'entraîner sur les sujets passés.

### Protocole de travail sur un sujet

1. **Lire le sujet en entier** (10 min) — identifier les parties indépendantes
2. **Planifier** : noter les questions sur lesquelles on est fort vs faible
3. **Traiter en temps contraint** : 4h E2 ou 5h E1
4. **Ne pas consulter le corrigé** avant d'avoir traité toutes les parties abordables
5. **Corriger et analyser** : noter les formules oubliées, les erreurs de méthode

### Ordre recommandé pour les annales

| Priorité | Sujets | Pourquoi |
|---|---|---|
| 1 | 2025, 2024, 2023 | Plus représentatifs du concours actuel |
| 2 | 2022, 2021, 2020 | Diversité des systèmes et thèmes |
| 3 | 2019, 2018, 2017 | Compléments — certains thèmes absents des récents |
| Corrigés | 2016, 2017, 2021 | Calibrer sa rédaction sur des réponses attendues |

### Objectif par semaine (phase 4)

- 1 sujet E2 complet (4h) en conditions d'examen
- 1 sujet E1 complet (5h) en conditions d'examen
- 1 session de correction approfondie + mise à jour du formulaire personnel

**Durée estimée phase 4 :** 4–6 semaines

---

## Phase 5 — Préparation orale

### 5.1 Épreuve de leçon (coeff. 5 — déterminante)

**Connaissances à maîtriser :**

- [ ] Programme technologie collège cycle 4 (compétences, démarche d'investigation)
- [ ] Programme STI2D complet (enseignements, spécialités, épreuves)
- [ ] Programme spécialité SI (voie générale)
- [ ] Socle commun de connaissances, compétences et culture
- [ ] CRCN (Cadre de Référence des Compétences Numériques)
- [ ] Réforme du lycée 2019 : nouveau bac, Grand Oral, spécialités
- [ ] Évaluations : diagnostique, formative, sommative, certificative — différences et usages
- [ ] Évaluation par compétences : critères, indicateurs, remédiation

**S'entraîner à :**

- Construire une séance à partir d'un TP (transposition didactique)
- Présenter en 20 min une séance sans lire ses notes
- Décrire différenciation pédagogique et gestion de la diversité
- Utiliser le numérique éducatif dans une séance (ENT, simulation, collecte données)

### 5.2 Épreuve d'entretien

**Textes à connaître :**
- Référentiel de compétences des enseignants (arrêté 01/07/2013)
- Droits et obligations du fonctionnaire de catégorie A
- Code de l'Éducation articles L111-1 à L111-4
- Vade-mecum laïcité (version en vigueur)
- Charte de la laïcité à l'école

**Structure de la présentation de 5 min :**
1. Qui je suis (formation, expériences)
2. Pourquoi l'enseignement (lien avec compétences acquises — pas juste "transmettre")
3. Quelle vision du métier (3 compétences clés que j'apporte)
4. Ce que je souhaite apporter aux élèves

**S'entraîner aux mises en situation :**
- Identifier les personnes ressources : psy-EN, infirmier, assistant social, acteurs extérieurs
- Analyser selon 3 scénarios différents
- Répondre selon 3 temporalités : court / moyen / long terme

**Durée estimée phase 5 :** 3–4 semaines

---

## Indicateurs de progression

### Auto-évaluation par thème (à tenir à jour)

| Thème | Niveau actuel | Objectif | Semaine cible |
|---|:---:|:---:|:---:|
| T02 Puissance AC | ⬜ | 🟢 | |
| T03 Thermique | ⬜ | 🟢 | |
| T11 Variation vitesse | ⬜ | 🟢 | |
| T14 Distribution | ⬜ | 🟢 | |
| T21 Modélisation | ⬜ | 🟢 | |
| T24 Correcteurs | ⬜ | 🟠 | |
| T30 Mécanique | ⬜ | 🟢 | |
| T13 ENR | ⬜ | 🟠 | |
| T28 Informatique | ⬜ | 🟠 | |
| TEC (mécanique) | ⬜ | 🟢 | |
| Leçon pédagogique | ⬜ | 🟢 | |
| Entretien | ⬜ | 🟢 | |

> 🟢 Maîtrisé · 🟠 Partiellement maîtrisé · 🔴 Lacune · ⬜ Non évalué

### Suivi des sujets traités

| Sujet | Traité | Note estimée | Points bloquants |
|---|:---:|:---:|---|
| 2025 E1 | ⬜ | | |
| 2025 E2 | ⬜ | | |
| 2024 E1 | ⬜ | | |
| 2024 E2 | ⬜ | | |
| 2023 E1 | ⬜ | | |
| 2023 E2 | ⬜ | | |
| 2022 E1 | ⬜ | | |
| 2022 E2 | ⬜ | | |
| 2021 E1 | ⬜ | | |
| 2021 E2 | ⬜ | | |
| 2020 E1 | ⬜ | | |
| 2020 E2 | ⬜ | | |

---

*Généré le 2026-05-19 — Basé sur l'analyse de 22 sujets et 6 rapports jury CAPET SII IE 2015–2025*
