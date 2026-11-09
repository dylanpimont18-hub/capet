# Audit de couverture du référentiel — 2026-11-09

> **Mise à jour du 2026-11-10 : les manques ont été comblés** (détail en fin de document).
> Les 20 éléments absents et les 24 partiels ont désormais une fiche ou un complément de fiche
> et des cartes dans l'app. Les tableaux ci-dessous décrivent l'état **avant** comblement.

Confrontation du référentiel du CAPET externe SII option ingénierie électrique (liste fournie
par l'utilisateur le 2026-11-09, **non recoupée ici avec le texte officiel**) avec le système
de révision : 30 fiches (`fiches/T*.tex` et `T*_contenu.md`), 171 exercices (`exercices/`),
589 cartes de l'app (`app/cards.json`) et les 10 sessions de 2 h (`09_Sessions_2h/packs/`).

**Méthode** : pour chaque élément, recherche par expressions régulières dans les fiches, les
exercices et les cartes, contrôlée à la main pour les manques apparents. La colonne « Sujets »
compte les **sujets distincts** du corpus 2013–2026 (25, sans rapports, sans corrigés, sans
doublons) qui **mentionnent** la notion. Une mention n'est pas forcément une question.
Script : `scratchpad/tools/couverture.py` (non versionné ; à recréer si besoin).

**Statuts** :
- **Couvert** : fiche dédiée ou section substantielle, et cartes dans l'app.
- **Partiel** : mentionné ou effleuré, sans cours structuré, ou sans carte.
- **Absent** : aucune trace dans les fiches ni dans les cartes.

## Bilan

| | Couvert | Partiel | Absent | Total |
|---|---:|---:|---:|---:|
| 1. Énergie | 22 | 8 | 2 | 32 |
| 2. Électronique | 11 | 8 | 12 | 31 |
| 3. Automatique | 10 | 4 | 3 | 17 |
| 4. Informatique | 0 | 3 | 0 | 3 |
| 5. Transversal | 2 | 1 | 3 | 6 |
| **Total** | **45** | **24** | **20** | **89** |

Le cœur historique du concours (électrotechnique, électronique de puissance, machines,
asservissements, capteurs, numérisation) est couvert. Les manques se concentrent sur trois
blocs : **télécommunications et RF**, **ingénierie système (SysML, analyse fonctionnelle)**,
**informatique et réseaux industriels**.

## 1. Énergie

| Élément | Statut | Où | Sujets |
|---|---|---|---:|
| Grandeurs électriques, électrocinétique | Couvert | T01 | 7 |
| Mesurage | Couvert | T30 (incertitudes peu traitées, absentes du corpus) | 2 |
| Schématisation électrique | Partiel | T30, T14, T29 ; 2 cartes | 10 |
| Monophasé et triphasé équilibré, puissances | Couvert | T02 | 10 |
| Représentation complexe, impédances | Couvert | T03 | — |
| Harmoniques, puissance déformante | Couvert | T04 | 4 |
| Notions d'électromagnétisme | Partiel | allusions en T06, T13, T14, T30 ; aucune carte | 0 |
| Thermique : conduction | Couvert | T05 | 8 |
| Thermique : convection | Partiel | T05, 1 carte | 3 |
| Thermique : rayonnement | **Absent** | — (les mentions du corpus visent surtout le rayonnement solaire) | 5 |
| Analogies électro-thermiques | Couvert | T05, T11 | 3 |
| Transformateurs mono et tri | Couvert | T06 | 4 |
| Hacheurs 1 et 4 quadrants | Couvert | T07 | 5 |
| Hacheur 2 quadrants (réversible en courant) | Partiel | 1 mention, 1 carte | 0 |
| Redresseurs mono et tri | Couvert | T08 | 5 |
| Filtrage de puissance (lissage) | Partiel | T08, T04, T20 ; 2 cartes | 4 |
| Onduleurs mono et tri | Couvert | T09 | 11 |
| Cinématique translation / rotation | Couvert | T10 | 14 |
| Statique (forces, moments, équilibre) | Couvert | T10 (PFD surtout) | 20 |
| Machine à courant continu | Couvert | T11 | 2 |
| Machine synchrone, brushless | Couvert | T12 | 11 |
| Machine asynchrone | Couvert | T13 | 9 |
| **Moteurs pas à pas** | **Absent** | — | 0 |
| Servomoteurs | Partiel | T12 (brushless), T25 (commande PWM) ; 2 cartes | 2 |
| Variation de vitesse et de couple | Couvert | T14 | 9 |
| Stockage d'énergie électrique | Couvert | T15 | 21 |
| Éolien | Partiel | T16, T09 ; 2 cartes | 1 |
| Hydraulique | Couvert | T15 (STEP), T16 | 5 |
| Photovoltaïque | Couvert | T16 | 10 |
| Production et transport de l'énergie | Partiel | allusions T16, T17 ; aucune carte | 10 |
| Régimes de terre IT, TT, TN | Couvert | T17 (3 cartes seulement) | 9 |
| Protection des biens et des personnes | Couvert | T17 | 12 |

## 2. Électronique

| Élément | Statut | Où | Sujets |
|---|---|---|---:|
| Régimes linéaire, commutation, transitoire | Couvert | T18, T19, T07, T26 | 8 |
| Diode | Couvert | T18 | 7 |
| Transistor (BJT, MOSFET, IGBT) | Couvert | T18 | 2 |
| AOP | Couvert | T19 | 3 |
| Analyse spectrale | Couvert | T04, T09, T22 | 8 |
| Fonctions de transfert, Bode | Couvert | T21 | 6 |
| Filtres du 1er et du 2e ordre | Couvert | T20 | — |
| Amplification | Couvert | T19, T23 | 8 |
| **Génération de signaux (oscillateurs, astables)** | **Absent** | — | 1 |
| Capteurs | Couvert | T23, T05 | 19 |
| Amplificateur d'instrumentation | Partiel | T19, T23 ; 1 carte | — |
| **Isolation galvanique** | **Absent** | 1 allusion en T06 | 2 |
| **Adaptation de niveau** | **Absent** | 1 allusion en T01 | 0 |
| Numérisation, échantillonnage, Shannon | Couvert | T22 | — |
| CAN / CNA : structures (flash, SAR, R-2R…) | Partiel | T22 ; 4 cartes | 1 |
| CAN / CNA : performances | Couvert | T22, T30 | 18 |
| Architectures cibles (µC, DSP) | Partiel | T24 | 15 |
| FPGA | Partiel | T24 : « au programme », 1 carte | 0 |
| VHDL / Verilog | Partiel | T24 : mention seulement | 0 |
| Langages C / C++ | Partiel | T24 (Arduino) ; 1 carte | 6 |
| **Horloges et synthèse de fréquence (PLL)** | **Absent** | — | 1 |
| Modulations numériques | Partiel | T25 : FSK, LoRa ; ni ASK, ni PSK, ni QAM | 4 |
| **Transmission en bande de base (NRZ, Manchester)** | **Absent des fiches** | exercices T24, T28 seulement — pourtant le codage NRZ est demandé en E1 2026 (D3) | 1 |
| Transmission sans fil | Partiel | T25 (LoRa) ; 2 cartes | 10 |
| **Multiplexage fréquentiel** | **Absent** | — | 0 |
| **Lignes de transmission** | **Absent** | — | 1 |
| **Fibres optiques** | **Absent** | 1 exercice (T24) | 4 |
| **Antennes** | **Absent** | — | 1 |
| **Filtrage numérique (synthèse RIF / RII)** | **Absent** | T27 traite seulement la récurrence d'un correcteur | 0 |
| **Instrumentation RF** | **Absent** | — | 0 |
| **Exposition aux champs électromagnétiques** | **Absent** | — | 0 |

## 3. Automatique et systèmes

| Élément | Statut | Où | Sujets |
|---|---|---|---:|
| Modélisation, fonctions de transfert | Couvert | T26 | 7 |
| Analyse temporelle et fréquentielle | Couvert | T26, T21 | 8 |
| Stabilité, précision, rapidité | Couvert | T27 | 16 |
| Correcteurs P, PI, PID | Couvert | T27 | 8 |
| Robustesse | Partiel | allusions, aucune carte | 2 |
| Numération | Couvert | T28 | 13 |
| Logique combinatoire | Couvert | T28 | 1 |
| Logique séquentielle | Couvert | T29 (1 carte) | 8 |
| Machines à états | Partiel | T24, T29 ; 1 carte — c'est pourtant la forme réellement interrogée (2017, 2021) | 4 |
| GRAFCET | Couvert | T29 (jamais interrogé) | 1 |
| API, IEC 61131-3 | Couvert | T29, T24 (1 carte) | 6 |
| **IHM** | **Absent** | — | 7 |
| Bus CAN | Couvert | T25 (+ 4 pièges 2026) | 4 |
| **Modbus** | **Absent des fiches** | exercices T24, T25 | 3 |
| **Ethernet industriel** | **Absent des fiches** | exercices T24, T25 | 3 |
| Liaisons séries (UART, RS-232/485) | Partiel | T24, T25 ; aucune carte | 4 |
| I2C, SPI | Partiel | mentions T24, T25 ; aucune carte | 2 |

## 4. Informatique et algorithmique

| Élément | Statut | Où | Sujets |
|---|---|---|---:|
| Algorithmique générale | Partiel | T24, T29 (algorigrammes) ; 1 carte | **17** |
| Langages C, C++, Python | Partiel | Python : T24, T29 ; 1 carte | 8 |
| CPU, mémoire, bus, périphériques | Partiel | T24 (registres) ; 1 carte | 15 |

## 5. Compétences transversales (ingénierie système)

| Élément | Statut | Où | Sujets |
|---|---|---|---:|
| **Analyse fonctionnelle** | **Absent** | — | 2 |
| **SysML (exigences, BDD, IBD, séquence, états)** | **Absent des fiches** | 3 exercices (T25, T27, T29) | **11** |
| **MBSE, approche système** | **Absent** | — | 2 |
| Chaîne d'acquisition / d'actionnement | Partiel | T22, T23, T30 | 12 |
| Bilan des pertes, rendement global | Couvert | T10, T11, T13, T06 | 14 |
| Vérification des exigences du cahier des charges | Couvert | conclusion de chaque question type | 22 |

## Priorités de comblement

**Priorité 1 — au référentiel, présent dans les sujets, absent ou faible chez toi :**
SysML (11 sujets), algorithmique et Python (17 et 8), IHM (7), schématisation (10),
production et transport (10), machines à états (4), liaisons séries, Modbus, Ethernet, I2C/SPI
(3–4), fibres optiques (4), codage en bande de base (NRZ, demandé en 2026), isolation galvanique (2).

**Priorité 2 — au référentiel, quasi absent des sujets 2013–2026 :**
bloc télécoms et RF (lignes, antennes, PLL, multiplexage, filtrage numérique, instrumentation
RF, exposition aux champs), moteurs pas à pas, oscillateurs, adaptation de niveau,
électromagnétisme, rayonnement thermique, hacheur 2 quadrants, FPGA et VHDL.

Les 10 sessions de 2 h ne comblent aucun de ces manques : elles portent sur des sujets réels,
qui n'interrogent pas ces notions.

## Proposition (non réalisée, en attente de décision)

| Action | Contenu |
|---|---|
| Nouvelle fiche **T31 Télécommunications et RF** | bande de base, modulations ASK/FSK/PSK/QAM, multiplexage, PLL, lignes et adaptation, fibres, antennes, instrumentation RF, exposition aux champs |
| Nouvelle fiche **T32 Ingénierie système** | analyse fonctionnelle, SysML (5 diagrammes), MBSE, chaînes d'information et d'énergie |
| Nouvelle fiche **T33 Informatique embarquée** | algorithmique, Python et C, architecture µC (CPU, mémoire, interruptions, E/S), liaisons UART, I2C, SPI, Modbus, Ethernet industriel, IHM |
| Compléments de fiches existantes | T05 convection et rayonnement ; T06 circuit magnétique ; T07 hacheur 2Q ; T12 moteurs pas à pas et servomoteurs ; T16 éolien ; T17 production et transport ; T19 oscillateurs, isolation galvanique, adaptation de niveau ; T20 filtrage numérique ; T29 machines à états |

Les fiches T31–T33 n'auraient pas de « présence n/13 » au sens actuel : il faudra leur donner un
poids explicite dans l'app (sinon elles tombent au fond de la file).

## Comblement réalisé le 2026-11-10

### Trois nouvelles fiches (`.tex` compilable + `_contenu.md` source des cartes)

| Fiche | Contenu | Présence mesurée | Cartes |
|---|---|---|---|
| **T31 Télécommunications et RF** | bande de base NRZ/Manchester, modulations ASK/FSK/PSK/QAM, multiplexage, PLL et quartz, lignes (Zc, Γ, ROS), fibres, antennes, Friis, exposition aux champs, instrumentation RF | 4/13 (fibre optique 2014, 2018, 2024, 2025 ; NRZ en 2026) | 27 formules, 11 pièges, 1 schéma |
| **T32 Ingénierie système** | bête à cornes, pieuvre, FAST, 9 diagrammes SysML et leurs relations, chaînes d'information et d'énergie, rendement global, MBSE, vérification des exigences | 8/13 | 6 formules, 10 pièges, 1 schéma |
| **T33 Informatique embarquée et réseaux** | algorithmique, Python et C, opérations bit à bit, architecture µC (mémoire, timers, interruptions), FPGA et VHDL, UART, RS-232/485, I2C, SPI, Modbus, Ethernet industriel, IHM | 11/13 | 15 formules, 13 pièges, 1 schéma |

La présence est le nombre d'années 2013–2025 où au moins un sujet **mentionne** la notion
(recherche par mots-clés, mots ambigus exclus). Elle fixe le poids des cartes dans l'app.
Questions types : sujets réels avec corrigé officiel quand ils existent (E1 2014 Q38 ; E2 2022
Q11–12 et Q21–22 ; E1 2026 D10 ; E2 2023 E4–E8 ; E2 2025 Q4–Q5), sinon exercices marqués
« inédit ». Deux erreurs de corrigés officiels y sont signalées : unité de 2023 E8 (1,03 m pour
1,03 cm) et conversion de 2025 Q5 (division par 1 000 au lieu de 3,6·10⁶).

### Compléments dans 13 fiches existantes

| Fiche | Ajout |
|---|---|
| T05 | convection (loi de Newton), rayonnement (Stefan-Boltzmann), coefficient radiatif linéarisé |
| T06 | Ampère, réluctance, Hopkinson, Faraday, Boucherot |
| T07 | hacheur deux quadrants réversible en courant (cours + piège) |
| T08 | lissage par condensateur |
| T12 | moteur pas à pas (pas angulaire, nombre de pas, vitesse) |
| T16 | vitesse spécifique d'une éolienne |
| T17 | production et transport (pertes en 1/U², domaines HTA/HTB) |
| T19 | astable à AOP, NE555, amplificateur d'instrumentation, optocoupleur, isolation galvanique, adaptation de niveau |
| T20 | filtrage numérique (RIF, moyenne glissante, RII, H(z), transformation bilinéaire) |
| T22 | structures de CAN et CNA (flash, SAR, double rampe, sigma-delta, R-2R) |
| T27 | robustesse (marges, effet d'un retard pur) |
| T29 | machines de Moore et de Mealy, nombre de bascules |
| T30 | piège unifilaire / multifilaire |

Ajouts faits uniquement en fin de section (blocs `$$` en fin de § 1, pièges en fin de § 5,
paragraphe sans TikZ en fin de bloc 1) : aucune carte existante n'a changé d'identifiant ni de
contenu (vérifié sur les 589 cartes antérieures).

### Effet sur l'app

589 → **727 cartes** (421 formules, 272 pièges, 34 schémas) sur **33 thèmes**. 77 questions
rédigées ajoutées dans `scripts/questions.json`. 83 tests verts ; 105 segments LaTeX des
nouvelles cartes vérifiés avec KaTeX.

### Ce qui reste hors du système

- Pas d'**exercices** pour T31–T33 ni pour les compléments (la banque `exercices/` reste à T01–T30).
- Le **manuel imprimable** `manuel/` n'intègre pas encore T31–T33 (il entrelace fiches et exercices) ;
  `fiches/main.tex` les inclut.
- Les notions RF (antennes, lignes, PLL, exposition) n'ont aucun sujet réel : leurs questions
  types sont inédites.
