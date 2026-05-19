# Points aveugles — CAPET SII Ingénierie Électrique

> Ce fichier recense les zones de fragilité structurelle : thèmes sous-estimés, incohérences dans les données, lacunes signalées par le jury mais non couvertes par le formulaire ou les fiches thématiques.

---

## 1. Incohérence entre les deux tableaux du `tableau_themes_capet.md`

Le `tableau_themes_capet.md` contient deux tables qui se **contredisent** sur plusieurs thèmes :

| Thème | Intensité (table 1) | Présence binaire (table 2) | Interprétation |
|---|:---:|:---:|---|
| T06 – Redresseurs | *(toutes cases vides)* | 22/22 🟢 | Paradoxal : présent partout mais jamais noté comme important |
| T08 – MCC | *(toutes cases vides)* | 22/22 🟢 | Même paradoxe |
| T10 – MAS | *(toutes cases vides)* | 22/22 🟢 | Même paradoxe |
| T16 – Composants | *(toutes cases vides)* | 22/22 🟢 | Même paradoxe |
| T17 – Bode/FT | Quelques 🟡 | 22/22 🟢 | Table 2 surévalue la présence |
| T18 – Amplification | *(toutes cases vides)* | 22/22 🟢 | Probable sur-génération de la table 2 |
| T19 – Numérisation | Quelques 🟡 | 22/22 🟢 | Idem |
| T26 – Logique combinatoire | Quelques 🟡 | 22/22 🟢 | Idem |
| T28 – Programmation | Quelques 🟡/🟠 | 22/22 🟢 | La table 1 est plus fidèle |

**Conclusion :** la table binaire (présence 22/22) semble avoir été générée avec un seuil très bas ou une erreur de génération. Se fier à la **table d'intensité (table 1)** pour prioriser les révisions. La table 2 est moins fiable.

---

## 2. Thèmes "invisibles" dans la table d'intensité mais réellement présents

Ces thèmes n'apparaissent pas en fil conducteur (jamais 🔴 ni 🟠) mais reviennent dans les questions d'application de nombreux sujets :

### T06 – Redresseurs

- **Pourquoi il compte :** Questions sur les alimentations de variateurs, convertisseurs AC/DC dans les sujets de variation de vitesse et ENR.
- **Ce qu'il faut savoir :** redresseur monophasé PD2, triphasé PD3, tension moyenne V_moy = 0,9·V_eff (mono), formules de base.
- **Risque :** être incapable de traiter une question sur un onduleur ou un variateur sans maîtriser le redresseur en amont.

### T08 – Machine à courant continu (MCC)

- **Pourquoi il compte :** Questions de modélisation, asservissement de vitesse (MCC souvent utilisé comme modèle simple pour introduire la boucle fermée).
- **Ce qu'il faut savoir :** équation de tension (U = E + R·I), équation de la force électromotrice (E = K·φ·ω), couple (C = K·φ·I).
- **Risque :** la MCC est souvent la machine utilisée dans les parties automatique/asservissement. Ne pas la connaître ferme ces parties.

### T10 – Machine asynchrone (MAS)

- **Note :** la MAS est abondamment couverte dans T11 (variation de vitesse) et dans le formulaire. Son absence de la table d'intensité est probablement une erreur de génération.
- **Ce qu'il faut savoir :** voir fiche T11 et formulaire section 8.

---

## 3. Lacunes signalées par le jury — non couvertes par les fiches thématiques

### Théorème de l'énergie cinétique (TEC)

- **Signal jury :** "inconnu de la majorité des candidats" (rapport 2024, épreuve E1 Urbanloop).
- **Formule :** ΔEc = ½·m·(v₂²–v₁²) = W_total (somme des travaux de toutes les forces)
- **Application type :** freinage d'un véhicule, accélération d'un engin mobile, variation de vitesse d'un convoyeur.
- **Piège fréquent :** appliquer v = d/t au lieu de TEC dès que la vitesse n'est pas constante.

### Pont de Wheatstone

- **Signal jury :** "traité par moins de 20 % des candidats" (rapport 2025).
- **Formule :** ΔU ≈ V_cc · ΔR / (4·R₀) (pont légèrement déséquilibré)
- **Utilisation :** conditionnement signal d'une jauge de contrainte, d'un capteur résistif.
- **Pourquoi négligé :** thème T20 (capteurs) souvent jugé secondaire, mais ces questions sont faciles à traiter.

### Informatique et algorithmique

- **Signal jury :** "lacunes massives" dans toutes les sessions récentes.
- **Ce qui revient dans les sujets :**
  - Organigrammes (conditions, boucles)
  - Lecture et complétion de programmes Python simples
  - Protocoles de communication série (I2C, SPI, UART)
  - Codage numérique (binaire, hexadécimal, complément à 2)
  - Trame LoRa, débit utile
  - Lecture d'un programme automate (Ladder, Grafcet → ST)
- **Risque :** les questions d'informatique sont souvent dans la dernière partie d'un sujet — les candidats épuisés ne les traitent pas, même quand elles sont accessibles.

### Chimie / thermodynamique des cycles

- **Signal jury 2025 :** des questions de chimie non traitées alors que "toute la démarche était fournie et qu'aucune connaissance spécifique en chimie n'était nécessaire".
- **Ce que ça signifie :** certains candidats abandonnent des questions de lecture de document par peur d'un domaine qu'ils jugent hors de leur spécialité.
- **Stratégie :** toujours lire les questions de chimie/thermodynamique — souvent les formules et la démarche sont fournies, seul le calcul est demandé.

---

## 4. Thèmes sous-estimés au regard des sujets récents

### T28 – Programmation / algorithmique

- Absent de l'intensité 🔴 mais présent dans 22/22 sujets selon la table binaire.
- Les rapports 2024 et 2025 signalent une montée en puissance des questions informatiques.
- **Tendance récente :** sujets 2023 (décodage), 2024 (API, capteurs numériques), 2025 (site isolé avec gestion IoT).

### T15 – Sécurité électrique / régimes de neutre

- Présent dans 9/22 sujets (41 %).
- Fréquence en hausse dans les sujets récents liés aux bâtiments, sites isolés, énergies renouvelables.
- **Ce qu'il faut savoir :** régimes TT, TN-S, TN-C, IT — courant de défaut, DDR, déclenchement.

### T13 – ENR (énergies renouvelables)

- La table d'intensité montre une intensité variable mais le thème revient dans **tous les sujets récents** (2021, 2022, 2024, 2025) avec au moins une partie ENR.
- **Ce qu'il faut savoir :** panneaux PV (MPPT, mise en série/parallèle, production annuelle), stockage (STEP, batteries), bilan énergétique.

---

## 5. Zones pédagogiques souvent zappées

Ces aspects sont propres à l'E1 (épreuve appliquée) mais représentent des points accessibles souvent non traités :

| Zone | Fréquence | Pourquoi zappée | Points en jeu |
|---|:---:|---|:---:|
| Question pédagogique finale | Dans tous les E1 | Candidats épuisés, jugent la partie "hors spécialité" | 15–20 % des points E1 |
| Lecture de SysML | Fréquente | Diagrammes jugés complexes sans l'être réellement | 5–10 % des points |
| Correction de copies d'élèves | ~50 % des E1 | Méconnaissance du processus d'analyse d'erreurs | 5–8 % des points |
| Questions "bon sens" (lecture doc.) | Systématique | Candidats qui passent trop vite à la suivante | 5–10 % des points |

**Stratégie :** ces parties sont souvent les **plus rentables** — elles ne nécessitent pas de calculs complexes. Ne jamais les sauter.

---

## 6. Thèmes du programme officiels absents des sujets récents

Ces thèmes sont au programme mais n'ont pas été fil conducteur depuis plusieurs années. Probabilité faible mais non nulle en 2027 :

| Thème | Dernière apparition significative | Risque |
|---|---|:---:|
| T04 – Transformateurs | 2016–2018 | Faible |
| T08 – MCC (fil conducteur) | 2016–2017 | Faible |
| T25 – Correction numérique | 2020–2021 | Faible |
| T23 – Nyquist / stabilité | 2022 | Moyen |
| FPGA / VHDL | Jamais | Très faible |

**Stratégie :** ne pas y consacrer plus de 10 % du temps de révision total.

---

*Généré le 2026-05-19 — Basé sur l'analyse de `tableau_themes_capet.md` et des rapports jury 2019–2025*
