# Catalogue d'extraits — Session 2026 (support : bus hydrogène Hycity®)

Décorticage des trois documents 2026 téléchargés le 2026-11-08, pour préparer des sessions de
révision de 2 h (extraits de sujet + documents réponses à imprimer). Les numéros de page sont
ceux du **PDF** (page 1 = couverture), et non la pagination imprimée en bas de page.

## 1. Provenance

| Fichier téléchargé | Statut dans la base |
|---|---|
| `capet-externe-bac-3-…-premi-re-preuve-crite-…-2026-19474.pdf` | **Déjà présent**, identique octet pour octet (md5 `d4128c08…`) à `06_PDFs_Originaux/2026/E1_Sujet_2026.pdf` |
| `capet-externe-bac-3-…-seconde-preuve-crite-…-2026-19471.pdf` (+ copie « (1) ») | **Déjà présent**, identique (md5 `f4358cc2…`) à `06_PDFs_Originaux/2026/E2_Sujet_2026_BAC3.pdf` |
| `troisi-me-concours-…-rapport-du-jury-…-2026-20916.pdf` | **Nouveau**. Archivé sous `06_PDFs_Originaux/2026/Rapport_Jury_2026_3eConcours.pdf` + `.md` dans le lot Markdown |

Le rapport est celui du **troisième concours**, mais son épreuve écrite porte sur le **même
sujet** que l'épreuve 1 externe (bus Hycity, parties A à E). Il fournit donc le **corrigé officiel
de l'E1 2026**, avec un décalage de numérotation (table en §2.3). Il ne couvre pas l'E2 2026.

Abréviations : **RJ26** = `Rapport_Jury_2026_3eConcours` ; « ext. » = numérotation du sujet externe.

---

## 2. Épreuve 1 externe 2026 — « Étude de la modélisation d'un produit » (4 h, PDF 30 p.)

Parties A, B, C obligatoires ; D **ou** E au choix → 4 parties de 10 questions en 4 h,
soit **≈ 60 min par partie** au rythme de l'épreuve.

### 2.1 Pages à imprimer

| Bloc | Pages PDF |
|---|---|
| Couverture, codes, consignes | 1–5 (inutile en révision, sauf la p. 5 « Conseils aux candidats ») |
| Présentation du support (bus Hycity) | **6** — à joindre à toute session E1 |
| Partie A | 7–9 |
| Partie B | 10–12 |
| Partie C | 13–15 |
| Partie D (choix 1) | 16–19 |
| Partie E (choix 2) | 20–22 |
| Cahier DR n° 1 (en-tête d'identification) | 23 |
| DRA1 (A8, A9) + DRA2 (A10) | 24 |
| DRB1 (B2, B9) + DRB2 (B4) | 25 |
| DRB3 (B5) + DRC1 (C4) | 26 |
| Cahier DR n° 2 (en-tête) | 27 |
| DRC2 (C5, C6) | 28 |
| DRD1 (D3, D5, D6) + DRD2 (D8) | 29 |
| DRE1 (E1, E3, E5) | 30 |

⚠ Les pages 10, 12 et 26 sont des **images** (aucun texte extractible) : la conversion Markdown
`E1_Sujet_2026.md` en a un contenu incomplet. Imprimer depuis le PDF.

### 2.2 Contenu par partie

| Partie | Titre | Notions | Thèmes | Corrigé RJ26 | RJ26 : traitée / ≥ 10 |
|---|---|---|---|---|---|
| A | Évaluer les performances d'un actionneur électrique | MCC : modèle R-L-E, essai à rotor bloqué sous tension réduite, constante de temps (tangente à l'origine), $K_e$, couple de pertes, bilan de puissance et rendement, caractéristique $C_U(N)$, point de fonctionnement, quadrants → structure 4Q | T11, T01, T26, T07 | p. 7–9 | 100 % / 38 % |
| B | Qualifier la qualité d'une opération de filtrage | Spectre d'un signal, gabarit, gain en dB, ordre d'un filtre, RC 1er ordre, Bode asymptotique, application d'un filtre à un signal composé, temps de réponse, 2e ordre par cascade (loi des nœuds / Millman), forme canonique, choix R-C (série E12, tolérance), réponse indicielle | T20, T21, T03 | p. 10–13 | 88 % / 27 % |
| C | Contrôler les performances du système d'ouverture des portes du bus | FT d'un capteur 1er ordre, réducteur à engrenages (rayon / diamètre), schéma-bloc parcouru à contre-sens, identification indicielle, marges de stabilité, gain limite pour une marge de phase, FTBF, $\omega_0$ et $m$ d'un 2e ordre, abaque $t_{r5\%}$, choix d'un correcteur | T26, T27, T21, T10 | p. 13–16 | 50 % / 31 % |
| D | Vérifier la fiabilité d'une transmission de données | Bus CAN : série / asynchrone / half-duplex, paire différentielle, codage NRZ, structure de trame (111 bits), efficacité, débit, identificateur = fonction + nœud, hexadécimal, arbitrage bit à bit, décodage des données, masque en pseudo-code | T25, T24 | p. 17–18 | 78 % / 36 % |
| E | Évaluer les performances d'un système de redressement de tension | Redresseur triphasé P3 à diodes : intervalles de conduction, $\langle u_S\rangle$, $I_{D,eff}$, puissance apparente, facteur de puissance, alternative PD3, rapport de transformation | T08, T06, T02, T04 | p. 19–21 | 81 % / 50 % |

Statistiques RJ26 : 26 copies (public), moyenne 6,85/20, max 19,2 (RJ26 p. 21 et 25).
Ce sont des candidats du troisième concours (épreuve de 5 h), pas du concours externe.

### 2.3 Correspondance de numérotation sujet externe ↔ RJ26

Le sujet du troisième concours compte **11 questions par partie**, le sujet externe **10**.
Pour corriger une question externe, lire la question RJ26 indiquée.

| Partie | Correspondance | Questions RJ26 sans équivalent externe |
|---|---|---|
| A | ext. A1 = RJ A1 ; ext. A**n** = RJ A**(n+1)** pour n = 2…10 | RJ A2 ($I_n$, $\Omega_n$ lus dans la doc — utile pour ext. A4) |
| B | ext. B1…B8 = RJ B1…B8 ; ext. B9 = RJ B9 **+** B10 ; ext. B10 = RJ B11 | — |
| C | ext. C1 = RJ C1 ; ext. C**n** = RJ C**(n+1)** pour n = 2…10 | RJ C2 ($\tau_{capt}$, $K_{capt}$ lus sur le DTC1) |
| D | ext. D1…D8 = RJ D1…D8 ; ext. D9 = RJ D10 ; ext. D10 = RJ D11 | RJ D9 (bit de stuffing) |
| E | ext. E1…E6 = RJ E1…E6 ; ext. E**n** = RJ E**(n+1)** pour n = 7…10 | RJ E7 (choix de diode : 630 V, 5,77 A → DSEI 12-10A) |

### 2.4 Point de vigilance sur le corrigé officiel (à vérifier soi-même)

**B9 (RJ26 p. 13)** : le corrigé pose $\frac{1}{RC} = \frac{900}{10} = 90$, puis
$C = 11\ \mu\text{F}$ pour $R = 1\ \text{k}\Omega$. Or le gabarit DRB1 place la limite de bande
passante à $\omega_2/10$, et B1 donne $\omega_2 = 2\pi \cdot 900 = 5\,655\ \text{rad·s}^{-1}$.
900 est la **fréquence en Hz**, utilisée ici comme une pulsation. Avec $\omega_2/10 = 565\ \text{rad·s}^{-1}$,
on obtiendrait $C \approx 1{,}8\ \mu\text{F}$. La figure B5 du sujet ($t_{r5\%} \approx 0{,}1$ s) est
cohérente avec la valeur du rapport, ce qui suggère que l'incohérence vient du sujet lui-même.
Ne pas apprendre la valeur 11 µF comme une référence.

### 2.5 Ce que le jury relève (RJ26 p. 21–24, lignes du `.md`)

Les points ci-dessous sont **reformulés** ; pour citer, reprendre le verbatim à la ligne indiquée.

| Q. RJ26 (ext.) | Constat du jury | Ligne `.md` |
|---|---|---|
| A4 (A3) | Réponse indicielle mal exploitée ; constante de temps confondue avec $t_{r5\%}$ | 959–961 |
| A7 (A6) | Bilan de puissance : AN fausses faute de se placer au régime nominal | 966–968 |
| A10 (A9) | La notion de point de fonctionnement est mal traitée | 977–978 |
| A11 (A10) | Quadrants rarement identifiés ; structure de conversion souvent incohérente | 980–982 |
| B2 (B2) | Lien atténuation linéaire ↔ gain en dB et ordre ↔ pente par décade non connu | 989–991 |
| B5 (B5) | Lecture du Bode à la bonne fréquence ; lien module ↔ gain mal maîtrisé | 1001–1003 |
| B9 (B9) | Relation entre R, C et le gabarit quasiment jamais évoquée | 1015–1016 |
| C3 (C2) | Rapport de réduction d'un engrenage simple ; confusion diamètre / rayon | 1033–1034 |
| C4 (C3) | Parcours de schéma-bloc : diviser par la FT d'un bloc parcouru à contre-sens | 1035–1037 |
| C6 (C5) | Définitions des marges de gain et de phase connues d'une minorité | 1045–1046 |
| C7 (C6) | Gain limite pour une marge de phase : question mal interprétée | 1048–1049 |
| D4–D5 (D4–D5) | Comptage des bits de la trame erroné → efficacité et débit faux | 1076–1078 |
| D6 (D6) | Confusion identificateur / fonction / adresse du nœud | 1080–1081 |
| D8 (D8) | Oubli de proposer l'identifiant de priorité supérieure (lire toute la question) | 1086–1089 |
| D9 (—) | Bit de stuffing identifié par environ la moitié des candidats | 1091–1092 |
| E7 (—) | Critères de choix d'une diode mal appliqués ; confusion valeur max / efficace | 1124–1126 |
| E8 (E7) | Confusion puissance apparente / puissance active | 1128–1129 |

Conclusion du jury (l. 1140–1163) : lois de base (nœuds, mailles, Ohm, puissances) et outils
mathématiques (log, trigonométrie, valeur moyenne) insuffisants ; résultats à encadrer ;
démarche justifiée exigée ; beaucoup de questions sont indépendantes.

---

## 3. Épreuve 2 externe 2026 — « Résolution de problème » (4 h, PDF 29 p.)

Études A et B obligatoires, **20 questions chacune** → **une étude ≈ 2 h** : une étude = une
session complète au rythme réel.

**Aucun corrigé officiel** à ce jour (pas de rapport du jury externe 2026 dans la base) :
tout corrigé de l'E2 2026 est à produire et à marquer « non officiel ».

### 3.1 Pages à imprimer

| Bloc | Pages PDF |
|---|---|
| Couverture, consignes, sommaire | 1–3 (p. 3 = conseils + sommaire) |
| Présentation du support (bus Hycity) | **5** — à joindre aux deux études |
| Étude A | 6–11 |
| Étude B | 12–16 |
| DT de l'étude A : DTA1 (choix moteur), DTA2 (spectre MLI) | 17–18 |
| DT de l'étude B : DTB1-DTB2 (capteur), DTB3 (montages ALI), DTB4-DTB5 (CAN ADS7029-Q1) | 19–21 |
| Cahier DR étude A (en-tête) | 22 |
| DRA1 (A6, A7) + DRA2 (A15) | 23 |
| DRA3 (A16, A17) | 24 |
| DRA4 (A19) | 25 |
| Cahier DR étude B (en-tête) | 26 (p. 27 = cadre « ne rien écrire ») |
| DRB1 (B13, B15) | 28 |
| DRB2 (B20, programme Python) | 29 |

### 3.2 Contenu par étude

| Étude | Problématique | Blocs de questions | Thèmes |
|---|---|---|---|
| A — « Comment permettre les différentes mobilités du bus ? » | Choisir la motorisation de l'essieu ZF AVE 130 et la stratégie de commande du variateur | A1–A2 autonomie hydrogène (énergie, PCI, masse, volume) · A3–A5 batterie (cellules série/parallèle, capacité, autonomie) · A6–A9 conditions extrêmes (forces, puissance, réducteur, couple, choix moteur sur DTA1) · A10–A15 machine asynchrone (pôles, glissement, P, Q, essai à vide, $R_f$, $X_m$, couple de démarrage, couplage) · A16–A20 onduleur (commande pleine onde, chronogrammes, $v_1$, valeur efficace, harmoniques, MLI) | T15, T10, T13, T02, T09, T04, T14 |
| B — « Comment réguler la température de fonctionnement de la pile à combustible ? » | Choisir une partie de la chaîne de mesure de température ; établir la récurrence d'un correcteur numérique | B1–B3 capteur (transducteur, étendue, loi $R_T(T)$) · B4–B9 conditionnement et amplification à ALI (DTB3) · B10–B12 CAN (pleine échelle, résolution, quantum, sensibilité, mot en hexadécimal, erreur de quantification) · B13–B17 échantillonnage (période, E/B d'ordre 0, temps de conversion, Shannon, anti-repliement) · B18–B20 correcteur numérique (Laplace → équation différentielle → récurrence, programme Python) | T23, T19, T22, T30, T20, T27, T24 |

---

## 4. Sessions de 2 h tirées de ces documents

| Session | Contenu | Pages sujet | DR | Corrigé |
|---|---|---|---|---|
| 2026-E1-AB | E1 parties A + B | 6, 7–12 | 24, 25, 26 (moitié haute : DRB3) | RJ26 p. 7–13 (officiel) |
| 2026-E1-CD | E1 parties C + D | 6, 13–19 | 26 (moitié basse : DRC1), 28, 29 | RJ26 p. 13–18 (officiel) |
| 2026-E1-CE | E1 parties C + E (variante de la précédente) | 6, 13–15, 20–22 | 26, 28, 30 | RJ26 p. 13–16, 19–21 (officiel) |
| 2026-E2-A | E2 étude A | 5, 6–11, 17–18 | 23, 24, 25 | à produire (non officiel) |
| 2026-E2-B | E2 étude B | 5, 12–16, 19–21 | 28, 29 | à produire (non officiel) |

Le corrigé RJ26 est à imprimer **à part** et à ne lire qu'après la composition.
