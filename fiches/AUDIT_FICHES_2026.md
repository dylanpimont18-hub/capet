# Audit qualité des fiches de révision CAPET SII IE — Session 2026

Audit réalisé le 2026-08-24 sur les 30 fiches `fiches/T01_*.tex` à `fiches/T30_*.tex`, par comparaison
systématique avec `TEMPLATE_FICHE.md` (structure, typographie) et re-calcul indépendant de chaque
application numérique des questions types, plus compilation `pdflatex` réelle de chaque fichier.

**Score moyen : 78,0/100** (médiane 78,5 — min 56 [T15], max 92 [T28])

Note de méthode : la notation technique a été faite par relecture experte + recalcul manuel des AN, pas
par un outil de calcul formel. Les erreurs listées ci-dessous ont été vérifiées mais méritent, pour les
plus sensibles (formules à corriger avant usage en révision), une dernière relecture humaine.

---

## 1. Classement (du plus faible au plus solide)

| Rang | Code | Titre | Score/100 | Structure/30 | Technique/35 | Pédago/15 | Forme/10 | Sources/10 |
|---|---|---|---|---|---|---|---|---|
| 1 | T15 | Stockage d'Énergie | **56** | 21 | 13 | 11 | 8 | 3 |
| 2 | T06 | Transformateur | **62** | 21 | 20 | 10 | 8 | 3 |
| 3 | T09 | Onduleurs | **64** | 19 | 22 | 12 | 7 | 4 |
| 4 | T02 | Puissance AC | **66** | 18 | 26 | 13 | 3 | 6 |
| 4 | T12 | Machine Synchrone | **66** | 22 | 22 | 11 | 9 | 2 |
| 6 | T08 | Redresseurs | **68** | 27 | 20 | 8 | 8 | 5 |
| 6 | T13 | Machine Asynchrone | **68** | 22 | 22 | 11 | 8 | 5 |
| 8 | T14 | Variation de Vitesse | **70** | 21 | 24 | 12 | 8 | 5 |
| 9 | T27 | Systèmes Bouclés / Correcteurs | **72** | 24 | 23 | 11 | 8 | 6 |
| 10 | T10 | Mécanique | **73** | 22 | 26 | 12 | 7 | 6 |
| 11 | T07 | Hacheurs | **75** | 24 | 29 | 11 | 7 | 4 |
| 11 | T11 | Machine CC | **75** | 24 | 26 | 12 | 8 | 5 |
| 11 | T22 | CAN/CNA / Numérisation | **75** | 25 | 22 | 12 | 9 | 7 |
| 14 | T30 | Mesurage / Instrumentation | **76** | 24 | 23 | 14 | 8 | 7 |
| 15 | T29 | Logique Séquentielle / GRAFCET | **78** | 22 | 30 | 13 | 8 | 5 |
| 16 | T16 | Énergies Renouvelables | **80** | 24 | 27 | 14 | 9 | 6 |
| 17 | T19 | AOP | **83** | 27 | 30 | 13 | 9 | 4 |
| 18 | T17 | Distribution / Sécurité | **84** | 24 | 33 | 14 | 9 | 4 |
| 18 | T24 | Systèmes Embarqués | **84** | 25 | 28 | 14 | 9 | 8 |
| 20 | T25 | Transmission Numérique | **85** | 24 | 29 | 14 | 9 | 9 |
| 20 | T26 | Modélisation des Systèmes | **85** | 23 | 32 | 13 | 8 | 9 |
| 22 | T18 | Composants Électroniques | **86** | 24 | 34 | 14 | 9 | 5 |
| 22 | T21 | Fonctions de Transfert / Bode | **86** | 25 | 31 | 13 | 9 | 8 |
| 24 | T01 | Grandeurs Électrocinétique | **87** | 24 | 32 | 13 | 9 | 9 |
| 24 | T03 | Représentations Complexes / Impédances | **87** | 26 | 30 | 14 | 9 | 8 |
| 24 | T04 | Harmoniques / THD | **87** | 26 | 30 | 14 | 9 | 8 |
| 27 | T05 | Phénomènes Thermiques | **89** | 27 | 32 | 14 | 8 | 8 |
| 28 | T20 | Filtres RC/RL | **90** | 28 | 34 | 14 | 9 | 5 |
| 29 | T23 | Capteurs / Conditionnement | **91** | 26 | 33 | 14 | 9 | 9 |
| 30 | T28 | Logique Combinatoire | **92** | 27 | 34 | 14 | 9 | 8 |

Toutes les fiches **compilent sans erreur bloquante** (`compile_ok: true` partout) — les problèmes
identifiés sont des erreurs de contenu, de conformité au template ou de forme, jamais des erreurs LaTeX
fatales.

---

## 2. Problèmes systémiques (touchant un grand nombre de fiches)

Ces défauts sont mutualisés entre plusieurs/la plupart des fiches — les corriger une fois « en masse »
rapporte plus que de corriger fiche par fiche.

### 2.1 En-tête `\fancyhead[L]` trop long (quasi toutes les fiches)
La règle du template impose < 35 caractères. Violée dans au moins 24 des 30 fiches, parfois très
largement (T10 : ~60 car., T25 : 56 car., T16 : 66 car., T24 : 54 car., T26 : 55 car., T17/T18 : 60-61
car.). Seules T15 (35, limite stricte) et T20 (37) s'en approchent. **Risque réel de troncature/chevauchement
visuel à l'impression.**

### 2.2 Bloc 3 : encadré générique « Procédure type copie concours » + flowchart générique — dans les 30 fiches
Un encadré « Procédure type copie concours (5 étapes) » suivi d'un schéma-flux générique
(Notions → Méthode → Application annale → Vérification jury) est inséré avant QT1 dans **la totalité des
30 fiches auditées**. Ce contenu n'est prévu nulle part dans `TEMPLATE_FICHE.md` (qui ne décrit que les
2-3 encadrés `questiontype`), n'apporte rien de spécifique au thème, et correspond très exactement au
défaut historique que `CLAUDE.md` du projet indique pourtant comme « corrigé » — il semble avoir été
réintroduit sous une autre forme lors d'une génération ultérieure. C'est la non-conformité structurelle
la plus répandue de tout le corpus.

### 2.3 Incohérence Bloc 0 / Bloc 5 : le chiffre « X/13 sujets » ne correspond pas au tableau de présence
Dans une majorité de fiches (T02, T04, T05, T06, T08, T09, T11, T12, T13, T14, T15, T16, T17, T18, T19,
T20, T26, T27, T28, T29, T30 — 21 fiches sur 30), le nombre affiché dans le bandeau du Bloc 0
(« Présence : X/13 sujets ») ne correspond pas à ce que montre le tableau du Bloc 5 une fois recompté
(parfois sous-estimé, parfois surestimé, écart de 1 à 6 unités). C'est un vrai risque pour la
crédibilité de l'outil de révision : il faut recompter chaque tableau et resynchroniser le Bloc 0.

### 2.4 Unités hors `siunitx` (`\mathrm{...}` au lieu de `\si{...}`/`\SI{...}{...}`)
Dans plusieurs fiches (T10, T11, T13, T15, T07...), les unités des corrigés/cours sont écrites en
`\mathrm{N\cdot m}`, `\mathrm{kg\cdot m^2}`, etc. au lieu des macros `siunitx` explicitement exigées par
`TEMPLATE_FICHE.md` §10 et `CLAUDE.md`. Application incohérente d'une fiche à l'autre.

### 2.5 Séparateur de milliers `\,` absent
Nombres à 4-5 chiffres écrits collés (`17689`, `10883`, `14900`, `2860`...) au lieu du format
`17\,689` imposé par le template — repéré dans T06, T09, T10, T14 au minimum.

### 2.6 Citations « jury » fabriquées ou trop librement paraphrasées, présentées comme des citations directes
Défaut le plus grave sur le plan de l'intégrité du contenu : dans **T06, T07, T08 et T15**, les citations
entre guillemets français attribuées à un rapport de jury précis ne se retrouvent pas telles quelles
dans les rapports jury du dépôt (`docs/CAPET_Markdown-*/...`) — soit elles sont totalement introuvables
(T07, T08), soit elles mélangent un fait réel et un conseil ajouté (T06), soit elles resserrent une
citation plus longue sans le signaler (T15). Pour un outil de révision concours, une fausse citation
jury présentée comme authentique est le type d'erreur le plus dommageable — un candidat pourrait la
citer telle quelle à l'écrit ou en fonder sa préparation dessus.

### 2.7 Erreurs de calcul non corrigées dans des questions types (liste consolidée)
- **T02** QT1 : `√(152,7²+92,9²)` ≠ 179,1 kVA (correct ≈ 178,7 kVA) + aucune des 3 QT ne se termine par
  la phrase de conclusion pourtant obligatoire.
- **T06** QT3 : I₀ = 42 A inventé, physiquement impossible (S₀ < P₀).
- **T07** / **T08** : la formule du facteur de puissance des redresseurs polyphasés `f_P = (√q/π)·sin(π/q)`
  comporte une racine carrée erronée (formule correcte : `f_P = (q/π)·sin(π/q)`), reproduite dans le
  cours, le formulaire ET les QT de T08.
- **T09** / **T14** : incohérence de calcul de THD (résultat affiché 59 % vs recalcul indépendant ≈ 61,4 %),
  la même erreur étant dupliquée dans les deux fiches (source commune probable).
- **T12** : diagramme de Kapp (Bloc 1) en contradiction de signe avec l'équation du cours juste au-dessus.
- **T13** : Pa, Pt, et une étape de dérivation du couple électromagnétique comportent des erreurs
  numériques/de facteur (p manquant).
- **T15** QT2 : confusion entre deux questions du rapport jury source → capacité de batterie sous-évaluée
  d'un facteur ×6,8 (2,86 A·h affiché contre 19,33 A·h dans le corrigé officiel du même rapport).
- **T16** : hacheur nommé « élévateur » avec une formule α = V_PV/E_b donnant des valeurs > 1
  (physiquement impossible pour un rapport cyclique) — c'est en réalité un hacheur abaisseur.
- **T22** : incohérence entre « CAN 10 bits » et la sensibilité S=2,684 LSB/°C annoncée (cette valeur ne
  correspond qu'à un CAN 8 bits).
- **T24** / **T25** : structure de trame CAN (bus de terrain) sommée à 111 bits dans le texte alors que le
  détail des champs ne totalise que 107-108 bits — erreur reproduite dans les deux fiches, avec
  propagation jusqu'au résultat numérique final de la QT3 de T25.
- **T27** : formule de récurrence du correcteur PI numérique erronée (rapport Tₑ/T_co inversé), présente
  à trois endroits de la fiche (cours, formulaire, corrigé).
- **T30** QT1 : la chaîne de calcul affichée ne redonne pas la valeur annoncée (recalcul ≈10,24 °C⁻¹
  contre 2,684 °C⁻¹ affiché).

### 2.8 Contenu inventé non marqué `[corrigé reconstitué]`
Le template impose explicitement ce marquage quand une donnée n'est pas dans le corrigé officiel. Des
valeurs numériques manifestement inventées (non présentes dans le `_contenu.md` source) apparaissent
sans ce marquage dans **T06** (I₀=42 A), **T09** (rayon de roue R=0,137 m), **T12** (trois rendements de
QT3), **T13** (P_u≈33kW alors que le sujet réel donne ≈100kW), **T24** (scénario numérique fictif présenté
sans distinction de la donnée réelle).

---

## 3. Plan de correction priorisé

**Priorité 1 — fiches sous la moyenne de solidité technique, à corriger en premier (score < 70) :**
T15 (56), T06 (62), T09 (64), T02 (66), T12 (66), T08 (68), T13 (68), T14 (70)

**Priorité 2 — corriger l'erreur de fond identifiée mais fiche globalement correcte (score 70-80) :**
T27, T10, T07, T11, T22, T30, T29, T16

**Priorité 3 — corrections mineures uniquement (header, typographie, cohérence Bloc0/Bloc5) (score > 80) :**
T19, T17, T24, T25, T26, T18, T21, T01, T03, T04, T05, T20, T23, T28

**Priorité 0 — transversal, à traiter une seule fois pour les 30 fiches :**
1. Supprimer l'encadré générique « Procédure type copie concours » + flowchart de tout le Bloc 3 (§2.2)
2. Recompter et resynchroniser tous les couples Bloc 0 / Bloc 5 (§2.3)
3. Raccourcir tous les en-têtes `\fancyhead[L]` sous 35 caractères (§2.1)
4. Vérifier mot à mot chaque citation jury contre les rapports sources, en particulier T06/T07/T08/T15 (§2.6)

---

## 4. Détail par fiche

### T01 — Grandeurs Électrocinétique — 87/100
**Erreurs bloquantes** : aucune.
**Erreurs mineures** : en-tête 47 car. (limite 35) ; formulaire à 18 formules (fourchette 8-16) ;
encadré générique hors template en Bloc 3.
**Points forts** : schémas circuitikz/courbe u(t) spécifiques et corrects ; 3 QT vérifiées justes avec
conclusion ; 2 citations jury cohérentes.

### T02 — Puissance AC — 66/100
**Erreurs bloquantes** :
- Aucune des 3 QT ne se termine par la phrase de conclusion obligatoire (violation systématique de la
  règle template §7), à la différence des 4 autres fiches du même lot.
- QT1 étape 3 : `√(152,7²+92,9²)` ≈ 178,7 kVA, pas 179,1 kVA annoncé ; l'erreur se propage à I_abs.
- Incohérence de fond QT1/QT2 sur le même sujet réel (rendement η=0,92 inventé en QT1 vs données
  officielles réutilisées en QT2 sans réconciliation, sans marquage `[corrigé reconstitué]`).

**Erreurs mineures** : défaut d'accentuation étendu (Bloc 3/4/5) ; guillemets droits au lieu de
guillemets français ; formulaire à 17 formules ; léger surclassement de présence en E2 discipl.
**Points forts** : QT3 (relèvement du facteur de puissance) intégralement correcte avec vérification
indépendante ; Bloc 4 très ciblé (8 points, aucun générique).

### T03 — Représentations Complexes / Impédances — 87/100
**Erreurs bloquantes** : aucune.
**Erreurs mineures** : en-tête 41 car. ; incohérence Bloc 0 (11/13) vs recomptage Bloc 5 (12/13).
**Points forts** : diagramme de Fresnel correct et spécifique ; 3 QT exactes et parfaitement sourcées ;
citations jury quantifiées et cohérentes.

### T04 — Harmoniques / THD — 87/100
**Erreurs bloquantes** : QT1 étape 1 — THD≈59% pour un onduleur triphasé pleine onde alimentant une MAS
est physiquement suspect (valeur théorique attendue ≈31% pour la tension, courant filtré généralement
inférieur) ; donnée spectrale source non reproduite dans le contenu.md, à vérifier manuellement.
**Erreurs mineures** : en-tête 44 car. ; écart Bloc 0 (10/13) vs Bloc 5 (9/13).
**Points forts** : QT3 exemple d'excellence (THD≈48% dérivé et vérifié exact = √(π²/8-1)) ; spectre en
bâtons spécifique ; citations jury chiffrées et crédibles.

### T05 — Phénomènes Thermiques — 89/100
**Erreurs bloquantes** : aucune.
**Erreurs mineures** : encadré Bloc 3 en couleur colElec au lieu de colTherm (seule fiche hors
électrotechnique du lot, incohérence de charte) ; écart Bloc 0 (8/13) vs Bloc 5 (7/13).
**Points forts** : schéma analogie électrique-thermique correct ; 3 QT exactes et bien sourcées ; pièges
Bloc 4 très concrets (racine carrée de C_th oubliée, confusion Peltier/Seebeck).

### T06 — Transformateur — 62/100
**Erreurs bloquantes** :
- QT2 : redresseur nommé « PD6 (6 diodes) », nomenclature non standard — la source et le sujet réel
  l'appellent « PD3 » (pont parallèle double triphasé).
- QT3 étape 2 : I₀=42 A inventé, non présent dans la source, et physiquement impossible (S₀ < P₀ obtenu).
  Aucun résultat final pour Xm, violant l'exigence de conclusion.
- Incohérence Bloc 0 (10/13) vs Bloc 5 (13/13 recompté).
- En-tête 44 car. (limite 35).

**Erreurs mineures** : εX≈εcc présenté sans la réserve de validité (εR≪εX) ; milliers non séparés
(17689, 5586) ; encadré générique Bloc 3 ; aucun corrigé marqué `[corrigé reconstitué]` malgré l'absence
de corrigé officiel identifié ; citation Bloc 4 mélangeant fait et conseil ajouté présentés comme
citation directe.
**Points forts** : schéma équivalent circuitikz de l'essai à vide correct ; QT1/QT2 exactes et conclues ;
Bloc 4 spécifique et utile.

### T07 — Hacheurs — 75/100
**Erreurs bloquantes** :
- Les deux citations jury du Bloc 4 sont introuvables telles quelles dans le rapport jury 2025 source
  (recherche « Kirchhoff » = 0 occurrence) — le fait sous-jacent est réel mais la formulation « citée »
  est inventée, sans marquage.
- Encadré générique Bloc 3 non prévu par le template, identique dans toutes les fiches.

**Erreurs mineures** : en-tête 36 car. ; sous-thème MPPT annoncé en Bloc 0 mais jamais traité dans le
corps ; unités hors siunitx ; source de QT3 (« question C7 ») probablement incorrecte (le calcul
numérique correspond en réalité à C8 du sujet réel) ; simplification non nuancée de la formule
d'entrelacement.
**Points forts** : 3 QT fidèlement sourcées et vérifiées exactes (E2 disc. 2023, robot Bakus) ; Bloc 1
techniquement rigoureux (dérivation Boost par ⟨v_L⟩=0) ; pièges Bloc 4 spécifiques et utiles.

### T08 — Redresseurs — 68/100
**Erreurs bloquantes** :
- Formule du facteur de puissance polyphasé `f_P=(√q/π)sin(π/q)` erronée (racine carrée en trop) ;
  appliquée littéralement elle ne redonne pas les résultats affichés (0,477 au lieu de 0,827 pour P3).
- f_P,PD2≈0,45 incohérent avec la valeur standard reconnue ≈0,90 (=2√2/π), fausse l'argument implicite
  sur le filtrage nécessaire.
- Les deux citations jury du Bloc 4 (2025, 2024) sont introuvables telles quelles dans les rapports
  sources correspondants — présentées à tort comme citations directes.
- Incohérence Bloc 0 (11/13) vs Bloc 5 (13/13 recompté).

**Erreurs mineures** : en-tête 41 car. ; encadré générique Bloc 3 ; empiétement/commutation non traité
(lacune de couverture, déjà absente de la source).
**Points forts** : 3 QT rigoureusement sourcées et vérifiées sur des sujets réels identifiés dans le
dépôt ; conclusions systématiquement reliées au cahier des charges ; Bloc 4 spécifique.

### T09 — Onduleurs — 64/100
**Erreurs bloquantes** :
- QT1 étape 1 : `√(95²+27²+27²+20²)/170 ≈ 61,4%` et non 0,59 (59%) affiché — erreur qui contamine
  ensuite le formulaire (Bloc 2) et la citation jury du Bloc 4.
- Incohérence Bloc 0 (9/13) vs Bloc 5 (12/13 recompté).
- QT3 : rayon de roue R=0,137 m inventé (absent de la source), non marqué `[corrigé reconstitué]`.

**Erreurs mineures** : en-tête 39 car. ; n_m/f_s légèrement décalés (écart ~0,2%) ; encadré générique
Bloc 3 utilisant le même style visuel que les vraies QT (risque de confusion avec une 4e QT) ; tiret
court au lieu de cadratin ; milliers non séparés.
**Points forts** : schéma TikZ (chronogramme créneau) spécifique ; formules fondamentales exactes et
cohérentes ; Bloc 4 avec pièges spécifiques et citations plausibles.

### T10 — Mécanique — 73/100
**Erreurs bloquantes** :
- QT2 (inertie équivalente robot KUKA) : J_eq recalculé ≈0,026 kg·m² contre 0,012 kg·m² visé par
  l'énoncé — écart ×2,2 non résolu, marqué `[incertain]` au lieu du `[corrigé reconstitué]` requis.
- En-tête ~60 car. (la violation la plus sévère du lot).
- Incohérence Bloc 0 (11/13) vs Bloc 5 (13/13 recompté).
- Bloc 5, paragraphe « Ordres de grandeur » : contenu entièrement électrotechnique (230V/400V/50Hz),
  hors-sujet pour une fiche de Mécanique — résidu probable d'un copié-collé.

**Erreurs mineures** : encadré générique en couleur colElec au lieu de colMeca (incohérence de charte) ;
milliers non séparés (14900, 9200...) ; unités hors siunitx systématiques.
**Points forts** : QT1/QT3 exactes et conclues ; schéma TikZ chaîne cinématique spécifique (pas un
flowchart générique, contrairement au défaut historique visé par CLAUDE.md) ; Bloc 4 pertinent avec
2 citations jury cohérentes.

### T11 — Machine CC — 75/100
**Erreurs bloquantes** :
- Incohérence Bloc 0 (8/13) vs Bloc 5 (10/13 recompté).
- Schéma TikZ §1.3 : pentes des caractéristiques couple-vitesse dessinées POSITIVES, alors que la
  caractéristique mécanique réelle d'une MCC à excitation séparée est tombante (pente négative) —
  inversion du sens physique.

**Erreurs mineures** : en-tête 37 car. ; séparateur « - » au lieu de « · » ; unités très majoritairement
hors siunitx ; QT2 étape 2 : arrondi 0,963 au lieu de 0,964 (troncature) ; encadré générique en plus du
schéma spécifique déjà présent ; source `_contenu.md` elle-même incohérente sur C_th (595 vs 557 N·m,
sans impact sur le .tex livré) et sur l'unité de k2.
**Points forts** : schéma couple-vitesse spécifique (malgré l'erreur de pente) ; cohérence physique
globale forte, AN principales vérifiées exactes ; citations jury spécifiques et E_dc=207V justifié
physiquement (redressement PD2 de 230V).

### T12 — Machine Synchrone — 66/100
**Erreurs bloquantes** :
- Incohérence Bloc 0 (6/13) vs Bloc 5 (4/13 recompté).
- Bloc 1 §1.2 : équation du cours (convention moteur, E=Vs-jXsIs) contredite par le diagramme de Kapp
  TikZ juste en dessous (construit selon la convention générateur, E=Vs+jXsIs).
- QT3 étape 1 : `0,97×0,90×0,72 = 0,6286`, pas 0,630 affiché ; erreur qui se propage à P_elec.
- QT3 : trois rendements élémentaires (η_CS, η_MS, η_red) inventés, absents de la source, non marqués
  `[corrigé reconstitué]`.

**Erreurs mineures** : en-tête ~50 car. ; énoncé QT1 omettant une précision nécessaire à la justification
de ω_roue=ω_moteur ; encadré générique alourdissant la fiche ; Bloc 4 point 4 (rotor en avance) à
vérifier — la convention usuelle place plutôt le rotor moteur en retard.
**Points forts** : QT fidèlement rattachées à la source, AN globalement vérifiées ; Bloc 4 spécifique et
crédible ; tenue typographique globalement soignée (le meilleur sous-score forme du lot T06-T15).

### T13 — Machine Asynchrone — 68/100
**Erreurs bloquantes** :
- QT1 étape 3 : Pa recalculé ≈134,3 kW contre 134,6 kW affiché.
- QT2 étape 1 : Pt recalculé ≈66,6-67,0 kW contre 66,8 kW affiché ; erreur propagée dans P_Jr/P_meca/P_u.
- QT3 étape 1 : égalité intermédiaire incohérente (facteur p omis, présent pourtant dans la source
  `_contenu.md`) ; résultat final correct mais étape affichée fausse.
- Incohérence Bloc 0 (9/13) vs Bloc 5 (7/13 recompté).

**Erreurs mineures** : deux encadrés génériques en plus des vraies QT ; schéma équivalent monophasé
annoncé en Bloc 0 mais jamais représenté ; corrigé QT1/QT2 de facto reconstitué (P_u≈33kW vs ≈100kW du
sujet réel) sans marquage ; unités hors siunitx sauf Bloc 5 ; overfull hbox.
**Points forts** : courbe couple-vitesse spécifique et correcte ; 3 QT en progression pédagogique
cohérente sur un même sujet réel ; Bloc 4 avec pièges spécifiques et 3 citations crédibles.

### T14 — Variation de Vitesse — 70/100
**Erreurs bloquantes** :
- QT1/QT3 : source indiquée « E2 disc. 2024 » alors que la source réelle est E1 (épreuve commune) —
  fausse aussi le tableau de présence Bloc 5.
- Incohérence Bloc 0 (8/13) vs Bloc 5 (5-6/13 recompté).
- QT3 étape 2 : formules d'identification (ω0, 2m) ne correspondant à aucune mise en équation standard ;
  application numérique donnant un temps de réponse ≈58s, très éloigné du Tr=1s visé.
- Contradiction interne : THD pleine onde annoncé 59% (Bloc 1 et formulaire) vs 61,4% recalculé en QT1 —
  même erreur que T09, non réconciliée entre les deux fiches.
- En-tête 52 car.

**Erreurs mineures** : sous-boîte citation sans `breakable` explicite ; milliers non séparés (2860) ;
encadré générique Bloc 3 ; sous-thème « freinage régénératif 3/13 » non traçable aux sources dans la
plage 2013-2025 du tableau.
**Points forts** : schéma-bloc variateur spécifique (Réseau→Redresseur→Bus DC→Onduleur→MAS) ; QT1/QT2
exactes et conclues ; Bloc 4 précis avec 2 citations authentiques.

### T15 — Stockage d'Énergie — 56/100 (score le plus bas du corpus)
**Erreurs bloquantes** :
- QT2 : confusion entre deux questions du rapport jury 2020 source (énergie récupérée en descente
  Q16 réutilisée comme énergie totale par trajet Q19) → capacité de batterie Cb=2,86 A·h annoncée contre
  19,33 A·h dans le corrigé officiel du même rapport (facteur ×6,8), sans que l'incohérence ne soit
  résolue — l'étape 2 du corrigé masque l'écart plutôt que de le corriger.
- Incohérence Bloc 0 (7/13) vs Bloc 5 (5-6/13 recompté, même en tenant compte de la note BAC3 2026).

**Erreurs mineures** : Bloc 1 en 5 sous-sections (max recommandé 3-4) ; encadré générique Bloc 3 ; ligne
« BAC3/E2 2026 » du Bloc 5 entièrement vide (colonne 2026 inexistante dans le tableau) ; vocabulaire DoD
incohérent entre 1.1 et QT2 (deux conventions opposées cohabitent) ; en-tête à 35 car. pile la limite ;
unités composées hors siunitx ; citation Bloc 4 resserrée présentée comme intégralement verbatim.
**Points forts** : QT1/QT3 recalculées exactes (QT1 même plus fidèle au sujet réel que la source
`_contenu.md`) ; schéma d'empilement Ns×Np spécifique ; compilation la plus propre du lot (aucun warning).

### T16 — Énergies Renouvelables — 80/100
**Erreurs bloquantes** :
- Bloc 1.2 : rapport cyclique de « hacheur élévateur » donné par α=V_PV/E_b, avec des valeurs toutes >1
  (physiquement impossible pour un α) — le montage est en réalité un hacheur ABAISSEUR (V_PV≫E_b), nom
  du convertisseur et orientation de la formule tous deux erronés.
- Incohérence Bloc 0 (7/13) vs Bloc 5 (6/13 recompté).

**Erreurs mineures** : en-tête 66 car. (très sévère) ; QT2 étape 1 : 782/30≈26,07 arrondi à 26 sans
discuter les 2 panneaux non affectés ; encadré générique Bloc 3.
**Points forts** : schéma MPPT (P=f(U)) spécifique et pertinent ; QT numériquement toutes vérifiées
justes ; citations jury précises et crédibles.

### T17 — Distribution / Sécurité — 84/100
**Erreurs bloquantes** : incohérence Bloc 0 (8/13) vs Bloc 5 (5-6/13 recompté).
**Erreurs mineures** : en-tête 60 car. ; label de source QT2 (« E1 disc. 2024 ») incohérent avec la
nomenclature du projet (« disciplinaire » ne qualifie que l'E2) ; encadré générique Bloc 3.
**Points forts** : schéma circuitikz ligne R+X/ΔU pertinent ; calcul de chute de tension de QT2
intégralement vérifié exact (≈31,7V, 7,9%, jugement conformité correct) ; Bloc 4 aligné sur 3 citations
distinctes.

### T18 — Composants Électroniques — 86/100
**Erreurs bloquantes** : incohérence Bloc 0 (7/13) vs Bloc 5 (4/13 recompté).
**Erreurs mineures** : en-tête 61 car. ; encadré générique Bloc 3.
**Points forts** : excellente cohérence technique (hacheur abaisseur correctement nommé, à la différence
de l'erreur analogue en T16) ; QT1/QT2 vérifiées exactes ; bon équilibre diode/BJT/MOSFET-IGBT avec cas
d'usage concrets ; Bloc 4 non générique.

### T19 — AOP — 83/100
**Erreurs bloquantes** :
- Incohérence Bloc 0 (8/13, « très fréquent ») vs Bloc 5 (4/13 recompté) — écart important avec le
  qualificatif affiché.
- Incohérence de formule « soustracteur » : le cours (Bloc 1.2) donne Vs=(R2/R1)(V2-V1) tandis que QT1
  utilise G1=(2R1+R2)/R2 pour un montage également qualifié « soustracteur » — deux topologies
  distinctes (ampli différentiel 1 AOP vs étage d'entrée d'instrumentation 2 AOP) non distinguées.

**Erreurs mineures** : en-tête 38 car. ; encadré générique Bloc 3.
**Points forts** : cycle d'hystérésis TikZ bien annoté ; tous les calculs vérifiés exacts (G1≈3,4,
G=340, V_H≈2,50V, V_B≈2,30V) ; citation jury très spécifique et crédible (statistique 70%/47%).

### T20 — Filtres RC/RL — 90/100 (2e meilleure fiche du corpus)
**Erreurs bloquantes** : incohérence Bloc 0 (7/13) vs Bloc 5 (5/13 recompté).
**Erreurs mineures** : en-tête 37 car. (la moins sévère du lot T16-T20) ; encadré générique Bloc 3.
**Points forts** : fiche la plus rigoureuse techniquement du lot T16-T20 (tous les calculs cohérents
entre cours/formulaire/QT) ; diagramme de Bode gain+phase spécifique avec asymptotes ET tracé réel ;
progression pédagogique exemplaire sur les 3 QT.

### T21 — Fonctions de Transfert / Bode — 86/100
**Erreurs bloquantes** :
- En-tête 48 car.
- QT2 étape 2 : le corrigé invente un scénario chiffré (« G0=+12dB, exemple ») non présent dans le sujet
  réel, mélangeant donnée réelle et fictive dans un même corrigé sans les distinguer.

**Erreurs mineures** : encadré générique Bloc 3 ; ambiguïté du template lui-même sur la plage d'années
(2013-2026 en Bloc 0 vs tableau 2013-2025 en Bloc 5), non imputable à l'auteur de la fiche.
**Points forts** : 3 QT recalculées exactes (20log(K)=26,4dB→K=20,9 ; Mφ=45° ; Kc≈0,25) ; diagramme de
Bode spécifique et pertinent ; Bloc 4 riche avec statistiques chiffrées crédibles.

### T22 — CAN/CNA / Numérisation — 75/100
**Erreurs bloquantes** : QT2 (E2 BAC3 2026) — pour un CAN annoncé « 10 bits », la sensibilité affichée
S=2,684 LSB/°C ne correspond en réalité qu'à un CAN 8 bits (recalcul à 10 bits : S≈10,77 LSB/°C).
L'étape de « vérification » du corrigé est arithmétiquement fausse telle qu'écrite.
**Erreurs mineures** : en-tête 47 car. ; overfull hbox mineur ; encadré générique Bloc 3.
**Points forts** : QT1 parfaitement vérifié de bout en bout (n=12 bits, q≈2,44mV, conversions binaire et
hexadécimale exactes) ; schéma de quantification spécifique et pertinent ; Bloc 4 avec piège rarement
documenté ailleurs (2ⁿ vs 2ⁿ-1).

### T23 — Capteurs / Conditionnement — 91/100 (meilleur score du lot T21-T25)
**Erreurs bloquantes** : aucune.
**Erreurs mineures** : en-tête 43 car. (la moins sévère du lot T21-T25) ; encadré générique Bloc 3.
**Points forts** : les 3 QT recalculées toutes exactes ; pont de Wheatstone circuitikz topologiquement
correct ; formulaire cohérent avec le cours ; citation jury 2025 très spécifique (moins de 20% de
réussite sur le pont de Wheatstone).

### T24 — Systèmes Embarqués — 84/100
**Erreurs bloquantes** : Bloc 1.6 (Bus CAN) — la trame listée (SOF+ID+RTR+IDE/r0+DLC+Data+CRC+ACK+EOF)
somme à 107 bits, pas 111 annoncé (au moins le bit de délimiteur CRC manque) ; erreur reprise dans le
formulaire sans correction.
**Erreurs mineures** : en-tête 54 car. ; corrigé QT1 marqué « [incertain] » plutôt que le tag standard
« [corrigé reconstitué] » ; encadré générique Bloc 3.
**Points forts** : calcul f_ech du PWM correctement recalculé à 90kHz, corrigeant une erreur présente
dans la source `_contenu.md` (bon signe de vérification indépendante) ; QT3 vérifiée aux deux bornes ;
2 citations jury authentiques.

### T25 — Transmission Numérique — 85/100
**Erreurs bloquantes** : même erreur de trame CAN que T24 (108 bits réels vs 111 annoncés), avec cette
fois propagation jusqu'au résultat numérique final de QT3 (t_trame=111×Tb au lieu de 108×Tb).
**Erreurs mineures** : en-tête 56 car. (la plus sévère du lot T21-T25) ; QT1 : indice de modulation
FSK=300, atypique (valeurs usuelles ~5-10), calcul juste mais sans remarque pédagogique sur ce
caractère atypique ; encadré générique Bloc 3.
**Points forts** : table des débits LoRaWAN conforme aux paramètres EU868 réels ; référence de sujet
2015 vérifiée présente dans le dépôt ; distinction rare et utile entre les deux théorèmes de Shannon.

### T26 — Modélisation des Systèmes — 85/100
**Erreurs bloquantes** : aucune.
**Erreurs mineures** : en-tête 55 car. ; encadré générique Bloc 3 ; QT1 reste littérale (pas d'AN
chiffrée complète, cohérent avec l'absence de données dans l'énoncé).
**Points forts** : schéma TikZ réponse indicielle 1er ordre spécifique ; tableau de présence cohérent
avec le Bloc 0 (rare dans le corpus) ; Bloc 4 avec pièges spécifiques bien choisis (identification à
63,2% et non 50%/90%, homogénéité Ke/Kc).

### T27 — Systèmes Bouclés / Correcteurs — 72/100
**Erreurs bloquantes** :
- Formule de récurrence du correcteur PI numérique fausse : rapport Tₑ/T_co inversé par rapport à la
  discrétisation d'Euler arrière correcte, présente à trois endroits (cours 1.6, formulaire, corrigé QT3).
- Incohérence Bloc 0 (11/13) vs Bloc 5 (9/13 recompté).

**Erreurs mineures** : en-tête 46 car. ; encadré générique Bloc 3 ; Bloc 4 point 5 renforce implicitement
la formule erronée sans la corriger.
**Points forts** : schéma-bloc d'asservissement spécifique et correct ; exemple de réglage de correcteur
P vérifié juste (Mφ=45°, gain=-59,4dB, K_lim≈933) ; Bloc 4 riche en pièges spécifiques.

### T28 — Logique Combinatoire — 92/100 (meilleur score de tout le corpus)
**Erreurs bloquantes** : aucune.
**Erreurs mineures** : léger écart Bloc 0 (4/13) vs Bloc 5 (3/13 recompté) ; encadré générique Bloc 3 ;
2 formules du formulaire hors-thème (quantum CAN, Shannon — relèvent plutôt de T30/T25).
**Points forts** : fiche remarquablement honnête sur la faible présence réelle du thème (QT2 sourcée
« Cours programme » plutôt que faussement rattachée à une année, cohérent avec la source) ; 3 QT
entièrement vérifiées justes ; schéma demi-additionneur spécifique et correct.

### T29 — Logique Séquentielle / GRAFCET — 78/100
**Erreurs bloquantes** :
- Incohérence Bloc 0 (7/13) vs Bloc 5 (5/13 recompté).
- Le titre et le Bloc 1.2 consacrent une sous-section entière au GRAFCET, mais aucune des 3 QT n'en
  traite et le Bloc 5 n'a même pas de ligne GRAFCET — alors que la source indique que ce mot n'apparaît
  que 2 fois dans les 41 sujets analysés et jamais comme question d'examen : sur-représentation d'un
  sous-thème que la fiche ne parvient pas à documenter par une preuve d'examen.

**Erreurs mineures** : en-tête 46 car. ; encadré générique Bloc 3 ; QT1 ne suit pas le format « Étape N —
Nom » attendu, contrairement à QT2/QT3 de la même fiche.
**Points forts** : Bloc 4 très concret et sourcé (moyenne 4,8/20 en 2021 citée explicitement) ; QT3
(durée de trame UART) vérifiée juste ; tableaux de bascules corrects et conformes.

### T30 — Mesurage / Instrumentation — 76/100
**Erreurs bloquantes** :
- QT1 : la démonstration « Montrer que S=2,684°C⁻¹ » est incohérente avec ses propres données —
  recalcul indépendant donnant S≈10,24°C⁻¹ avec les valeurs utilisées dans le corrigé lui-même.
- Incohérence Bloc 0 (10/13) vs Bloc 5 (12/13 recompté, cette fois par sous-estimation).

**Erreurs mineures** : en-tête 49 car. ; encadré générique Bloc 3.
**Points forts** : schéma-bloc chaîne de mesure spécifique et correct ; QT2 (Shannon/filtre
anti-repliement) entièrement vérifiée juste ; QT3 bien argumentée avec confrontation explicite au
cahier des charges.

---

## 5. Synthèse chiffrée

- **30/30 fiches compilent** sans erreur bloquante.
- **30/30 fiches** portent l'encadré générique hors-template en Bloc 3 (§2.2) — correction unique à
  fort effet de levier.
- **21/30 fiches** ont une incohérence Bloc 0 / Bloc 5 sur le chiffre de présence (§2.3).
- **~24/30 fiches** dépassent la limite de 35 caractères en en-tête (§2.1).
- **4 fiches** (T06, T07, T08, T15) contiennent une citation jury fabriquée ou trop librement paraphrasée
  présentée comme citation directe (§2.6) — priorité d'intégrité du contenu.
- **13 fiches** contiennent au moins une erreur de calcul ou de formule non corrigée dans une question
  type ou le cours (§2.7).
- Score moyen global : **78,0/100**. Domaine le plus solide en moyenne : électronique/numérique
  (T18-T30, moyenne ≈83) ; domaine le plus fragile : machines électriques et conversion de puissance
  (T06-T15, moyenne ≈69).
