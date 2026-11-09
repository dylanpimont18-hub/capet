# T08 — Redresseurs (monophasé et triphasé)

---

## 1. FORMULES ET COURS

| Formule LaTeX | Contexte | Fréquence | Donnée sujet ou mémoire |
|---|---|---|---|
| $\bar{U}_{PD2} = \dfrac{2\sqrt{2}}{\pi} V_{eff} \approx 0{,}9 \cdot V_{eff}$ | Tension moyenne redresseur monophasé PD2 (Graëtz, 4 diodes) | Très fréquent | $V_{eff}$ = valeur efficace tension AC primaire |
| $\bar{U}_{P3} = \dfrac{3\sqrt{6}}{2\pi} V_{eff,simple} \approx 1{,}17 \cdot V_{eff,simple}$ | Tension moyenne redresseur triphasé P3 (3 diodes, simple alternance) | Très fréquent | $V_{eff,simple}$ = tension simple secondaire |
| $\bar{U}_{PD6} = \dfrac{3\sqrt{2}}{\pi} V_{eff,composée} \approx 2{,}34 \cdot V_{eff,simple}$ | Tension moyenne redresseur triphasé PD6 (6 diodes, double alternance) | Très fréquent | Aussi noté PD3 en sujets CAPET 2026 |
| $\bar{U}_{PD6} = 0{,}95 \cdot U_M$ | Tension moyenne PD6 avec $U_M$ = amplitude tensions composées | Fréquent | $U_M = \sqrt{2} \cdot U_{eff,composée}$ (formule compacte sujet 2026) |
| $f_P = \dfrac{\sqrt{q}}{\pi} \sin\!\left(\dfrac{\pi}{q}\right)$ | Facteur de puissance redresseur $q$ pulsations (diodes seules) | Très fréquent | $q = 2$ (PD2), $q = 3$ (P3), $q = 6$ (PD6) |
| $f_{P,PD2} = \dfrac{\sqrt{2}}{\pi} \approx 0{,}45$ | Facteur de puissance PD2 (sans filtrage) | Fréquent | Faible → filtre LC indispensable |
| $f_{P,P3} = \dfrac{\sqrt{3}}{\pi} \sin\!\left(\dfrac{\pi}{3}\right) \approx 0{,}827$ | Facteur de puissance P3 | Très fréquent | Non conforme si CDC impose $f_P > 0{,}9$ (2026 E1) |
| $f_{P,PD6} = \dfrac{\sqrt{6}}{\pi} \sin\!\left(\dfrac{\pi}{6}\right) \approx 0{,}955$ | Facteur de puissance PD6 | Très fréquent | Conforme si $f_P > 0{,}9$ (2026 E1) |
| Courant efficace diode P3 : $I_{D,eff} = \dfrac{I_S}{\sqrt{3}}$ | Courant efficace traversant chaque diode P3 | Fréquent | $I_S$ = courant côté secondaire transformateur (continu) |
| Tension inverse max diode P3 : $U_{inv} = \sqrt{6} \cdot V_{eff,simple}$ | Tenue en tension des diodes P3 | Courant | Critère de choix des composants |
| Ondulation tension PD6 : $\delta U / \bar{U} = 4{,}2\ \%$ | Taux d'ondulation résiduelle (diodes) | Courant | P3 : $18{,}3\ \%$ ; PD2 : $48{,}2\ \%$ |
| Redresseur commandé (thyristors) : $\bar{U}_\alpha = \bar{U}_0 \cos\alpha$ | Tension moyenne en fonction de l'angle d'amorçage $\alpha$ | Courant | Formule pour pont de Graëtz commandé |

### 1.1 Lissage par condensateur

*(complément du référentiel, 2026-11-10 — notion hors sujets 2013–2026 sauf mention)*

**Ondulation de tension avec un condensateur de lissage :**
$$\Delta u \approx \frac{I}{f_{ond} \, C}$$
- Valable si l'ondulation reste faible devant la tension moyenne

---

## 2. QUESTIONS TYPES

### Q1 — Sujet 2026, E1 Partie E, Q.E7–E8 : redresseur P3, tension moyenne et facteur de puissance

**Source :** `2026/E1_Sujet_2026/E1_Sujet_2026.md`, Partie E, Choix 2, Questions E7–E8

**Énoncé :** Un réseau triphasé $230/400\ \mathrm{V}$ alimente un transformateur (rapport $m$) suivi d'un pont P3 (3 diodes cathodes communes). La période de la tension redressée est $T_S = T_1/3$ (réseau $50\ \mathrm{Hz}$ → $T_1 = 20\ \mathrm{ms}$). La valeur moyenne de la tension de sortie vaut :
$$\bar{u}_s = \frac{3\sqrt{6}}{2\pi} \cdot V_{eff,simple}$$
Le cahier des charges impose une tension DC de $600\ \mathrm{V}$ et un facteur de puissance $f_P \geq 0{,}9$. Calculer $f_P$ pour P3 et conclure.

**Corrigé :**
- Facteur de puissance P3 avec $q = 3$ :
  $$f_{P,P3} = \frac{\sqrt{3}}{\pi} \cdot \sin\!\left(\frac{\pi}{3}\right) = \frac{1{,}732}{3{,}1416} \times 0{,}866 \approx 0{,}827$$
- $f_{P,P3} = 0{,}827 < 0{,}9$ → **non conforme** au cahier des charges.
- Conclusion : la solution P3 est insuffisante ; il faut passer à un pont PD6 (6 diodes).

---

### Q2 — Sujet 2026, E1 Partie E, Q.E9 : redresseur PD6 (PD3 double alternance)

**Source :** `2026/E1_Sujet_2026/E1_Sujet_2026.md`, Partie E, Question E9

**Énoncé :** La solution 2 utilise un pont PD6 (6 diodes). La tension moyenne est $\bar{u}_s = 0{,}95 \cdot U_M$ où $U_M$ est l'amplitude des tensions composées secondaires. Calculer le facteur de puissance $f_{P,PD6}$ ($q = 6$).

**Corrigé :**
$$f_{P,PD6} = \frac{\sqrt{6}}{\pi} \cdot \sin\!\left(\frac{\pi}{6}\right) = \frac{2{,}449}{3{,}1416} \times 0{,}5 \approx 0{,}955$$
- $f_{P,PD6} = 0{,}955 > 0{,}9$ → **conforme** au cahier des charges. La solution PD6 est retenue.

---

### Q3 — Sujet 2026, E1 Partie E, Q.E10 : rapport de transformation pour PD6 → 600 V DC

**Source :** `2026/E1_Sujet_2026/E1_Sujet_2026.md`, Partie E, Question E10

**Énoncé :** Pour obtenir $\bar{u}_s = 600\ \mathrm{V}$ avec le pont PD6 alimenté par un transformateur étoile-étoile (primaire $400\ \mathrm{V}$ composés), calculer le rapport de transformation $m$.

**Corrigé :**
- $\bar{u}_s = 0{,}95 \cdot U_M$, donc $U_M = 600/0{,}95 \approx 631\ \mathrm{V}$
- Valeur efficace des tensions composées secondaires : $U_{s,comp} = U_M/\sqrt{2} = 631/1{,}414 \approx 446\ \mathrm{V}$
- Rapport de transformation (étoile-étoile) : $m = U_{s,comp}/U_{1,comp} = 446/400 \approx 1{,}12$

---

### Q4 — Sujet 2024, E2 Appliquée Commune, alimentation Urbanloop : PD2 + hacheur

**Source :** `2024/E2_Appliquee_Commune_2024/E2_Appliquee_Commune_2024.md`, boîtier alimentation

**Énoncé :** Le boîtier alimentation de la capsule Urbanloop convertit le réseau EDF $230\ \mathrm{V}$ monophasé en $72\ \mathrm{V}$ DC sur les rails. La structure est : PD2 (pont de Graëtz) + filtre LC + hacheur série. Justifier que le PD2 sans filtre fournirait $\bar{U} \approx 0{,}9 \times 230 \approx 207\ \mathrm{V}$ DC, et qu'un hacheur est nécessaire pour descendre à $72\ \mathrm{V}$.

**Corrigé :**
- PD2 : $\bar{U}_{PD2} = \dfrac{2\sqrt{2}}{\pi} \times 230 = \dfrac{2 \times 1{,}414}{3{,}1416} \times 230 \approx 0{,}9 \times 230 = 207\ \mathrm{V}$
- Rapport de tension DC : $72/207 \approx 0{,}35$ → rapport cyclique $\alpha \approx 0{,}35$ du hacheur Buck.
- Le PD2 fournit la tension continue et le hacheur adapte au niveau requis par les rails $72\ \mathrm{V}$.

---

### Q5 — Sujet 2022, E2 Appliquée Commune, hacheur 4 quadrants (frein à courant de Foucault)

**Source :** `2022/E2_Appliquee_Commune_2022/E2_Appliquee_Commune_2022.md`, Questions 30–35

**Énoncé :** L'alimentation du frein à courant de Foucault utilise un redresseur PD2 (D1, D2, D3, D4) suivi d'un hacheur 4 quadrants (T1/D1', T2/D2', T3/D3', T4/D4' — pont en H). La tension filtrée $E = 207\ \mathrm{V}$. Justifier le choix d'un hacheur 4 quadrants et calculer $\alpha$ pour atteindre un point de fonctionnement nominal avec $\langle u_f \rangle = R_f \langle i_f \rangle$.

**Corrigé :**
- Le frein doit permettre l'inversion du courant (démagnétisation) → 4 quadrants nécessaires.
- Pont en H : $\langle u_f \rangle = (2\alpha - 1) \cdot E$ en commande bipolaire.
- Pour $\langle u_f \rangle = R_f \langle i_f \rangle > 0$ : $\alpha > 0{,}5$ ; pour l'inversion : $\alpha < 0{,}5$.
- Valeur de $\alpha$ : $\alpha = \dfrac{1}{2}\left(1 + \dfrac{R_f \langle i_f \rangle}{E}\right)$

---

## 3. ATTENTES DU JURY

| Source | Citation directe | Implication pour le candidat |
|---|---|---|
| `2026/E1_Sujet_2026.md` (contexte) | Le sujet impose explicitement $f_P \geq 0{,}9$ et demande de **justifier le choix** entre P3 et PD6 | Savoir calculer $f_P$ pour $q$ quelconque et **conclure** par rapport à un cahier des charges — ne pas juste énoncer la formule |
| `2025/Rapport_Jury_2025.md` | "De nombreux candidats ne maîtrisent pas les calculs de puissance" | Distinguer clairement $P$ (active), $Q$ (réactive), $S$ (apparente) dans le bilan du redresseur ; le facteur de puissance $f_P = P/S$ |
| `2025/Rapport_Jury_2025.md` | Jury apprécie "la rigueur scientifique" et la "justification des démarches" | Pour chaque structure de redresseur : dessiner la forme d'onde $u_{DC}(t)$, identifier les intervalles de conduction, puis calculer $\bar{U}_{DC}$ par intégration |
| `2024/Rapport_Jury_2024.md` | Commentaires sur B11–B12 (variateur de vitesse) : le redresseur PD2 est l'étage d'entrée — son rôle dans le THD global doit être identifié | Savoir que le redresseur injecte des harmoniques côté réseau (rangs $6k\pm 1$ pour PD6, $2k\pm 1$ pour PD2) |

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique | Source |
|---|---|---|
| Réseau monophasé | $230\ \mathrm{V}$ eff, $50\ \mathrm{Hz}$ | Tous sujets |
| Réseau triphasé | $230/400\ \mathrm{V}$, $50\ \mathrm{Hz}$ | Tous sujets |
| Tension DC sortie PD2 (réseau 230 V) | $\approx 207\ \mathrm{V}$ | 2022 E2A, 2024 E2A |
| Tension DC rails Urbanloop | $72\ \mathrm{V}$ | 2024 E2A |
| Tension DC objectif recharge batterie | $600\ \mathrm{V}$ | 2026 E1 |
| Tension composée secondaire pour 600 V via PD6 | $\approx 446\ \mathrm{V}$ eff | 2026 E1 |
| Facteur de puissance P3 | $f_P \approx 0{,}827$ | 2026 E1 |
| Facteur de puissance PD6 | $f_P \approx 0{,}955$ | 2026 E1 |
| Tension continue filtrée (condensateur) | $E = 207\ \mathrm{V}$ | 2022 E2A |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Formule de $\bar{U}$ selon le type de pont** : PD2 ($q=2$) ≠ P3 ($q=3$) ≠ PD6 ($q=6$). Le facteur numérique change. Mémoriser : PD2 $\approx 0{,}9 V_{eff}$, P3 $\approx 1{,}17 V_{eff,simple}$, PD6 $\approx 2{,}34 V_{eff,simple}$.

2. **Confusion P3 et PD6** : P3 = 3 diodes (cathodes communes), simple alternance, 3 pulsations par période. PD6 = 6 diodes (pont de Graëtz triphasé), double alternance, 6 pulsations.

3. **Tension PD6 : simple ou composée ?** La formule $\bar{U}_{PD6} = 0{,}95 U_M$ utilise l'amplitude des tensions **composées**. Erreur fréquente : utiliser la tension simple ($U_M$ divisé par $\sqrt{3}$).

4. **Facteur de puissance ≠ $\cos\varphi$** : pour un redresseur à diodes, le courant d'entrée n'est pas sinusoïdal, donc $f_P \neq \cos\varphi$. Le facteur de puissance inclut le taux de distorsion harmonique (THD) : $f_P = \cos\varphi_1 / \sqrt{1 + \mathrm{THD}^2}$.

5. **Angle d'amorçage $\alpha$ des thyristors** : ne pas confondre $\alpha$ rapport cyclique (hacheur) et $\alpha$ angle d'amorçage (thyristor/redresseur commandé). Dans les sujets récents, les redresseurs à diodes sont privilégiés mais les thyristors peuvent apparaître (2022 frein à courant de Foucault).

6. **Courant efficace de la diode** : dans un P3, $I_{D,eff} = I_S/\sqrt{3}$ (chaque diode conduit $1/3$ de la période). Dans un PD6, $I_{D,eff} = I_{DC}/\sqrt{3}$ (chaque diode conduit $1/3$ également). Ne pas confondre avec la valeur moyenne.

7. **Choisir une diode : chaque critère avec la bonne valeur** : comparer une valeur efficace à une valeur maximale, ou l'inverse, conduit à éliminer la mauvaise diode. La tension inverse se compare à la tension inverse crête et le courant au courant de la diode (ici efficace, $I_S/\sqrt{3}$), chacun majoré du coefficient de sécurité : $630 \times 1{,}5 = 945$ V et $5{,}77 \times 1{,}5 = 8{,}7$ A dans le sujet 2026. Source : rapport du jury 2026 du troisième concours (même sujet que l'E1 externe 2026), question E7, sans équivalent dans le sujet externe.

8. **Puissance apparente d'un secondaire qui alimente un redresseur** : prendre $S = P$, ou une formule en $\cos\varphi$, alors que les courants ne sont pas sinusoïdaux. Au secondaire triphasé, $S = 3\,V_{eff}\,I_{D,eff}$ ; la puissance active est celle de la charge, $P = \langle u_S \rangle\, I_S$ ; pour le P3, $f_P = P/S = 3/(\pi\sqrt{2}) \approx 0{,}68$. Source : rapport du jury 2026 du troisième concours (même sujet que l'E1 externe 2026), question E8 et E9 = question E7 et E8 du sujet externe.

9. **Fréquence d'ondulation** : prendre la fréquence du réseau pour dimensionner un condensateur de lissage. La fréquence de l'ondulation vaut 2f pour un PD2 et 6f pour un PD6 ; avec 50 Hz au lieu de 100 Hz, on double inutilement la capacité.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

| Thème associé | Articulation |
|---|---|
| **T06 — Transformateur** | Le transformateur est l'étage amont du redresseur : son rapport $m$ est déterminé par la tension DC souhaitée et le type de pont (P3 ou PD6 donnent des $m$ différents pour la même $V_{DC}$ cible). |
| **T07 — Hacheurs** | Dans un variateur de vitesse ou une alimentation à découpage, la chaîne est : Redresseur PD2 → filtre → hacheur Buck. Le redresseur fixe la tension DC d'entrée du hacheur. |
| **T09 — Onduleurs** | Dans un variateur de vitesse AC : Redresseur PD6 → bus DC → onduleur MLI triphasé. La qualité de la tension DC (ondulation, valeur moyenne) impacte les performances de l'onduleur. |
| **T05 — Qualité de l'énergie / harmoniques** | Les redresseurs à diodes injectent des harmoniques côté réseau (rangs $6k\pm 1$). Le passage de PD2 à PD6 réduit le THD. Filtres actifs ou passifs peuvent être ajoutés. |
| **T01 — Circuits AC** | L'analyse du redresseur repose sur les formes d'onde tension/courant, le calcul de la valeur moyenne (intégrale) et la valeur efficace (intégrale du carré). |
