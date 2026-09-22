# T15 — Stockage d'énergie électrique

Sources analysées : E2_Sujet_2026_BAC3, E1_Sujet_2026, E2_Sujet_2021, Rapport_Jury_2021, E2_Sujet_2023, E2_Sujet_2020, Rapport_Jury_2020, E2_Disciplinaire_IE_2025, E1_Sujet_2024, Rapport_Jury_2024.

---

## 1. FORMULES ET COURS

### 1.1 Capacité et énergie d'une batterie

**Capacité d'une batterie :**
$$C_b = \frac{E_{nécessaire}}{U_{nom}}$$

- $C_b$ en A·h, $E_{nécessaire}$ en W·h, $U_{nom}$ en V
- Fréquence d'apparition : **très élevée** — dimensionnement de batterie présent dans les sujets 2020, 2023, 2026

**Énergie stockée :**
$$E = U_{nom} \cdot C_b$$

- $E$ en W·h, $U_{nom}$ en V, $C_b$ en A·h
- Source : Rapport_Jury_2020 (Q20, Q21) : $C_b$ calculée en A·h à partir de l'énergie en W·h divisée par la tension nominale

**Taux de décharge (DoD) :**
- Le taux de décharge maximum admissible est souvent imposé par le constructeur ; on ne décharge pas en dessous d'une fraction de la capacité nominale
- Source : E2_Sujet_2026_BAC3 (§ batterie) : « elles ne sont exploitées que jusqu'à 20 % de décharge »
- Source : Rapport_Jury_2020 : « vérifier que l'installation ne dépasse pas 70 % de décharge »
- Énergie utile : $E_{utile} = E_{totale} \times (1 - DoD_{min})$

### 1.2 Association de cellules en série et en parallèle

**Association série (pour obtenir la tension nominale souhaitée) :**
$$N_{série} = \frac{U_{batterie}}{U_{cellule}}$$

**Association parallèle (pour obtenir la capacité souhaitée) :**
$$N_{parallèle} = \frac{C_{batterie}}{C_{cellule}}$$

**Nombre total de cellules :**
$$N_{total} = N_{série} \times N_{parallèle}$$

- Source : E2_Sujet_2026_BAC3 (Q A3, A4) : cellules NMC HpCO de $U_{cell} = 3{,}5$ V et $C_{cell} = 53{,}5$ A·h, batterie 600 V / 128,4 kW·h
  - $N_{série} = \frac{600}{3{,}5} \approx 171$ cellules par module
  - $N_{total}$ commande constructeur : 684 cellules
- Source : Rapport_Jury_2020 (Q22) : « $N_{série} = \frac{48}{3{,}7} = 13$ cellules montées en série ; $N_{parallèle} = 4$ cellules montées en parallèle ; 52 cellules au total »

### 1.3 Autonomie d'un système à batterie

$$t_{autonomie} = \frac{E_{utile}}{P_{consommée}}$$

ou, en unités pratiques :
$$t_{autonomie} = \frac{C_b \times (1 - DoD_{min})}{I_{décharge}}$$

- Source : E2_Sujet_2026_BAC3 (Q A5) : « calculer l'autonomie du bus à 40 km·h$^{-1}$ jusqu'au niveau critique de décharge »
  - Énergie utile = $128{,}4 \times 0{,}8 = 102{,}72$ kW·h, $P = 22$ kW → $t = 4{,}67$ h → distance = $186{,}8$ km → le bus peut rentrer au dépôt
- Source : E2_Sujet_2023 (Q A8) : configurations 40/60/80 kW·h étudiées pour une durée minimale de 7 h

### 1.4 Rendement d'un système de stockage par pompage (STEP)

$$\eta_{st} = \frac{E_{turbinage}}{E_{pompage}}$$

$$E_{turbinage} = E_{potentielle} \times \eta_{turbinage}$$
$$E_{potentielle} = m \cdot g \cdot h = \rho \cdot V_{eau} \cdot g \cdot h$$

- Source : E2_Sujet_2021 (Q5, Q9, Q10) : « déterminer l'énergie potentielle disponible lorsque le niveau d'eau dans le réservoir supérieur est maximal » ; rendement global turbinage = 78 %
  - $E_{p} = 0{,}9 \times 1000 \times 1000 \times 9{,}81 \times 130 = 1{,}148$ MJ → 318,8 kW·h
  - $E_{elec\_dispo} = 318{,}8 \times 0{,}78 = 248{,}7$ kW·h (43 % des besoins journaliers du village)
  - $\eta_{st} = \frac{248{,}7}{427{,}5} = 58{,}2\%$ — peu performant mais écologique

### 1.5 Caractéristiques des technologies de cellules

| Technologie | Tension nominale | Énergie massique | Application typique |
|---|---|---|---|
| Li-Ion / NMC | 3,5 à 3,7 V | 150–250 W·h·kg$^{-1}$ | Bus, robot, véhicule électrique |
| Li-FePO4 (LFP) | 3,2 V | 100–160 W·h·kg$^{-1}$ | Stockage stationnaire |
| Plomb-acide | 2,0 V | 30–50 W·h·kg$^{-1}$ | Batterie de démarrage, bateau |
| Supercondensateur | 2,5–3,0 V | 5–20 W·h·kg$^{-1}$ | Tampon puissance (freinage) |

- Source : E2_Sujet_2026_BAC3 : cellule NMC HpCO, $U_{cell} = 3{,}5$ V, $C_{cell} = 53{,}5$ A·h
- Source : Rapport_Jury_2020 : cellule Li-Ion, $U_{cell} = 3{,}7$ V, $C_{cell} = 5{,}2$ A·h, $m_{cell} = 92$ g

### 1.6 Gestion de batterie (BMS) — notions qualitatives

- Le **BMS** (Battery Management System) surveille : la tension de chaque cellule, le courant, la température, le SOC (State of Charge) et le SOH (State of Health)
- Le **SOC** (% de charge restante) est déterminé par intégration du courant : $SOC = SOC_0 - \frac{1}{C_b} \int i \, dt$
- Le vieillissement des cellules se traduit par une diminution irréversible de la capacité et une augmentation de la résistance interne ; il est accéléré par les surcharges, les décharges profondes et les hautes températures
- Source : E2_Sujet_2026_BAC3 (§ batterie) : « dimensionnées pour ne pas avoir à être remplacées plus d'une fois au cours de la durée de vie du Hycity ; durée de vie estimée à huit ans »

---

## 2. QUESTIONS TYPES (max 6)

### Q1 — Dimensionnement d'une batterie par capacité en A·h
**Source :** Rapport_Jury_2020 (Q20, Q21) ; Rapport_Jury_2020 dessalinisateur
**Énoncé :** « Calculer l'énergie nécessaire pour réaliser 160 trajets types (en tenant compte du taux de décharge). En déduire la capacité nécessaire $C_b$ en A·h. »
**Données :** $E_{trajet} = 0{,}6$ W·h, 160 trajets, taux de décharge max 70 %, $U_{nom} = 48$ V
**Corrigé :** $E_{nécessaire} = \frac{160 \times 0{,}6}{0{,}7} = 137{,}1$ W·h ; $C_b = \frac{137{,}1}{48} = 2{,}86$ A·h. Structure : 13 cellules série × 4 parallèle = 52 cellules, masse 4,784 kg < 5 kg.

### Q2 — Association série/parallèle de cellules (bus Hycity 2026)
**Source :** E2_Sujet_2026_BAC3 (Q A3, A4)
**Énoncé :** « Calculer le nombre de cellules à associer en série dans chaque module pour respecter la tension nominale de 600 V. Calculer la capacité totale de la batterie en A·h. »
**Données :** $U_{cell} = 3{,}5$ V, $C_{cell} = 53{,}5$ A·h, $U_{batterie} = 600$ V, $E_{batterie} = 128{,}4$ kW·h, 2 branches de 2 modules
**Corrigé :** $N_{série} = \frac{600/2}{3{,}5} \approx 86$ cellules/module ; $C_{totale} = \frac{128{,}4 \times 10^3}{600} = 214$ A·h

### Q3 — Autonomie d'un système avec taux de décharge (bus électrique)
**Source :** E2_Sujet_2026_BAC3 (Q A5)
**Énoncé :** « Lorsque la batterie est totalement chargée, calculer l'autonomie du bus à 40 km·h$^{-1}$ jusqu'au niveau critique de décharge. Conclure. »
**Données :** $E_{utile} = 128{,}4 \times 0{,}8 = 102{,}72$ kW·h, $P_{moyenne} = 22$ kW
**Corrigé :** $t = \frac{102{,}72}{22} = 4{,}67$ h → distance = $4{,}67 \times 40 = 186{,}8$ km. Conclusion : le bus peut rentrer au dépôt depuis n'importe quel point du trajet type.

### Q4 — Rendement d'une STEP micro (stockage hydraulique)
**Source :** E2_Sujet_2021 (Q9, Q10), Rapport_Jury_2021
**Énoncé :** « Déterminer l'énergie électrique nécessaire au remplissage complet du réservoir. En déduire le rendement global du système de stockage $\eta_{st}$. »
**Données :** $P_{abs\,pompe} = 76$ kW, durée remplissage = 5,625 h, énergie turbinage disponible = 248,7 kW·h
**Corrigé :** $E_{pompage} = 76 \times 5{,}625 = 427{,}5$ kW·h ; $\eta_{st} = \frac{248{,}7}{427{,}5} = 58{,}2\%$. Conclusion : peu performant mais alternatif écologique au stockage par batteries.

### Q5 — Calcul de l'énergie potentielle du réservoir (STEP)
**Source :** E2_Sujet_2021 (Q5), Rapport_Jury_2021
**Énoncé :** « Déterminer l'énergie potentielle en kW·h disponible lorsque le niveau d'eau est maximal (volume utile = 90 % du volume total de 1 000 m$^3$). Hauteur de chute $h = 130$ m. »
**Données :** $\rho_{eau} = 1000$ kg·m$^{-3}$, $g = 9{,}81$ m·s$^{-2}$, $V_{utile} = 0{,}9 \times 1000 = 900$ m$^3$
**Corrigé :** $m = 1000 \times 900 = 9 \times 10^5$ kg ; $E_p = mgh = 9 \times 10^5 \times 9{,}81 \times 130 = 1{,}147$ GJ = 318,8 kW·h

### Q6 — Choix de la configuration batterie (robot viticole 2023)
**Source :** E2_Sujet_2023 (Q A6, A7, A8, A9)
**Énoncé :** « Déterminer la durée maximale de fonctionnement pour les trois configurations. Choisir la configuration permettant d'assurer la durée minimale de 7 h. »
**Données :** config 1 : 80 kW·h / 2500 kg ; config 2 : 60 kW·h / 2450 kg ; config 3 : 40 kW·h / 2400 kg ; $\eta_{global} = \eta_{CS} \times \eta_{MS} \times \eta_{réd}$
**Corrigé :** Calculer $P_{méca}$ pour chaque config ; en déduire $P_{élec}$ ; $t = E / P_{élec}$ → choisir la config dont $t \geq 7$ h tout en minimisant la masse.

---

## 3. ATTENTES DU JURY

### Rapport_Jury_2020 (dessalinisateur + robot)
> « Le jury déplore que des problématiques simples, comme le dimensionnement d'une batterie, ne soient pas maîtrisées. »
> « L'analyse de la documentation du panneau solaire et le calcul de l'énergie stockée dans la batterie ont été bien traités. Par contre les calculs de rendement ont été posés très souvent de manière erronée. »
> « Une critique à la fois qualitative et quantitative était attendue afin de vérifier que l'installation ne dépasse pas 70 % de décharge. Le jury déplore des réponses trop évasives sans aucun lien avec les documents techniques et/ou un manque de valeurs numériques. Les termes n'étaient pas maîtrisés par l'ensemble des candidats. »

**Implication candidat :** Savoir dimensionner une batterie (capacité en A·h, structure série/parallèle, contrainte de masse) sans approximation. Maîtriser les notions de taux de décharge, d'énergie utile et de rendement du cycle de charge/décharge.

### Rapport_Jury_2021 (micro-STEP)
> « Le jury note ici les progrès des candidats quant aux conversions d'unités. »
> « La conclusion quant aux performances et à l'intérêt du procédé de stockage par pompage devait mentionner le faible rendement (58 %) ET l'avantage environnemental par rapport au stockage par batteries. »

**Implication candidat :** Conclure toujours sur la valeur numérique du rendement ET sur la pertinence contextuelle (écologique, économique, faisabilité géographique).

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Paramètre | Valeur typique | Source |
|---|---|---|
| Tension cellule Li-Ion/NMC | 3,5 à 3,7 V | E2_Sujet_2026_BAC3, Rapport_Jury_2020 |
| Capacité cellule robot | 5,2 A·h, masse 92 g | Rapport_Jury_2020 |
| Capacité cellule bus Hycity | 53,5 A·h | E2_Sujet_2026_BAC3 |
| Tension batterie bus Hycity | 600 V | E2_Sujet_2026_BAC3 |
| Énergie batterie bus Hycity | 128,4 kW·h | E2_Sujet_2026_BAC3 |
| Taux de décharge minimum | 20 % (bus) / 30 % (bateau) | E2_Sujet_2026_BAC3 / Rapport_Jury_2020 |
| Durée de vie batterie bus | 8 ans | E2_Sujet_2026_BAC3 |
| Rendement global turbinage STEP | 78 % | E2_Sujet_2021 |
| Rendement global STEP (cycle complet) | 58 % | Rapport_Jury_2021 |
| Énergie potentielle réservoir 900 m³ à 130 m | 318,8 kW·h | Rapport_Jury_2021 |
| Consommation village 250 kW·h/jour | 43 % couvert par STEP seule | Rapport_Jury_2021 |
| Autonomie batteries bateau | 2 × 130 A·h (12 V) → 2 × 1560 W·h | Rapport_Jury_2020 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Confusion W·h / A·h** : la capacité s'exprime en A·h, l'énergie en W·h ou kW·h. La conversion est $E = U_{nom} \times C_b$. Ne pas additionner des A·h et des W·h.

2. **Oubli du taux de décharge** : si le constructeur impose DoD$_{max}$ = 70 %, l'énergie utile n'est que 70 % de l'énergie totale ; la capacité dimensionnée doit donc être divisée par 0,7.

3. **Erreur sur l'association série/parallèle** : en série, les tensions s'additionnent mais la capacité reste celle d'une cellule ; en parallèle, les capacités s'additionnent mais la tension reste celle d'une cellule. Erreur classique : multiplier les deux à la fois.

4. **Calcul de rendement d'une STEP** : le rendement global se calcule sur le cycle complet (pompage → stockage → turbinage), pas uniquement sur la phase de turbinage. Négliger les pertes au pompage donne un rendement fictif de 100 %.

5. **Formule de l'énergie potentielle** : utiliser $E_p = m \cdot g \cdot h$ avec la masse d'eau totale, pas le volume. Oublier la densité de l'eau ($\rho = 1000$ kg·m$^{-3}$) est une erreur fréquente.

6. **BMS et SOC** : ne pas confondre SOC (état de charge instantané en %) et capacité résiduelle en A·h. Le BMS ne contrôle pas la tension du réseau, il protège la batterie contre les surcharges et décharges profondes.

7. **Réponses qualitatives sans chiffres** : le jury 2020 déplore les réponses évasives. Toujours appuyer la conclusion (l'installation est-elle suffisante ?) par un calcul numérique comparant énergie disponible et énergie consommée.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T14 (Variation de vitesse)** : les sujets de véhicules électriques (bus 2026, robot viticole 2023) combinent batterie + variateur de vitesse. L'énergie récupérée au freinage régénératif se stocke dans la batterie. Voir E2_Sujet_2026_BAC3 (Q A10).
- **T16 (Énergies renouvelables)** : la STEP (micro-hydraulique) est un moyen de stockage associé à une centrale PV (E2_Sujet_2021) ; les panneaux PV rechargent la batterie via un convertisseur DC/DC avec MPPT (E2_Disciplinaire_IE_2025). Le stockage d'hydrogène (électrolyseur + pile à combustible) est une alternative présentée dans E2_Disciplinaire_IE_2025.
- **T17 (Distribution/Sécurité)** : l'installation de charge d'une batterie depuis le réseau (redresseur triphasé, pont P3 ou PD3) est étudiée dans E1_Sujet_2026 (partie E) ; la conformité NFC 15-100 (chute de tension, section de câble) s'applique aussi à l'alimentation du chargeur.
- **Électronique de puissance** : le convertisseur DC/DC de charge (hacheur élévateur ou abaisseur) est systématiquement étudié avec les batteries (E2_Sujet_2023 partie C, E2_Disciplinaire_IE_2025 partie 2).
