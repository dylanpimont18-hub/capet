# T06 — Transformateur (monophasé et triphasé)

---

## 1. FORMULES ET COURS

| Formule LaTeX | Contexte | Fréquence | Donnée sujet ou mémoire |
|---|---|---|---|
| $m = \dfrac{N_2}{N_1} = \dfrac{V_2}{V_1} = \dfrac{I_1}{I_2}$ | Rapport de transformation (monophasé) | Très fréquent | Calculé à partir des tensions nominal (ex. 2026 E1 Q.E10) |
| $m = \dfrac{U_{2n}}{U_{1n}}$ | Rapport tensions composées (triphasé) | Fréquent | Idem couplage étoile-étoile |
| $P_0 = R_f \cdot I_0^2 \approx \dfrac{V_1^2}{R_f}$ | Pertes fer (essai à vide) | Fréquent | $P_0$ mesuré au wattmètre côté primaire |
| $Q_0 = X_m \cdot I_0^2 \approx \dfrac{V_1^2}{X_m}$ | Puissance réactive magnétisante | Fréquent | $Q_0 = \sqrt{S_0^2 - P_0^2}$ |
| $S_0 = V_1 \cdot I_0$ | Puissance apparente à vide | Courant | Donnée directe capteur |
| $R_f = \dfrac{V_1^2}{P_0}$ | Résistance perte fer (schéma équivalent) | Fréquent | Déduit de $P_0$ et $V_1$ |
| $X_m = \dfrac{V_1^2}{Q_0}$ | Réactance magnétisante | Fréquent | Déduit de $Q_0$ et $V_1$ |
| $P_{cc} = R_s \cdot I_{cc}^2$ | Pertes cuivre (essai court-circuit) | Courant | $R_s = R_1 + m^2 R_2$ ramenée au primaire |
| $\varepsilon_{cc} = \dfrac{V_{cc}}{V_{1n}}$ | Tension de court-circuit relative | Courant | Valeur typique $0{,}04$ à $0{,}10$ |
| $\Delta U \approx \varepsilon_{R}\cos\varphi + \varepsilon_{X}\sin\varphi$ | Chute de tension relative en charge | Courant | $\varepsilon_R = P_{cc}/S_n$, $\varepsilon_X \approx \varepsilon_{cc}$ |
| $\eta = \dfrac{P_2}{P_1} = \dfrac{P_2}{P_2 + P_{fer} + P_{cuivre}}$ | Rendement | Courant | Maximum pour $P_{fer} = P_{cuivre}$ |
| Couplage **Yy** : $U_{composée} = \sqrt{3}\cdot U_{simple}$ | Triphasé étoile-étoile | Très fréquent | Rapport $m$ conservé |
| Couplage **Yd** : décalage $30°$ entre primaire et secondaire | Triphasé étoile-triangle | Courant | Utilisé pour redresseurs (harmoniques) |
| $U_{s} = m \cdot U_{1}$ (sans charge) | Tension secondaire à vide | Base | Définition |

### 1.1 Circuit magnétique et électromagnétisme

*(complément du référentiel, 2026-11-10 — notion hors sujets 2013–2026 sauf mention)*

**Théorème d'Ampère sur un circuit magnétique :**
$$N \, I = H \, \ell$$
- Valable si le champ H est uniforme le long de la ligne de champ moyenne de longueur ℓ

**Réluctance d'un tronçon de circuit magnétique :**
$$\mathcal{R} = \frac{\ell}{\mu_0 \, \mu_r \, S}$$

**Loi d'Hopkinson :**
$$N \, I = \mathcal{R} \, \Phi$$
- Valable en régime linéaire, hors saturation du matériau

**Loi de Faraday :**
$$e = -N \, \frac{d\Phi}{dt}$$

**Formule de Boucherot :**
$$V_{eff} = 4{,}44 \, N \, f \, B_{max} \, S$$
- Valable en régime sinusoïdal, avec B_max valeur crête de l'induction

---

## 2. QUESTIONS TYPES

### Q1 — Sujet 2026, E1 Partie E, Question E8 (réseau → 600 V DC via P3)

**Source :** `2026/E1_Sujet_2026/E1_Sujet_2026.md`, Partie E, choix 2

**Énoncé :** Le réseau triphasé fournit $230/400\ \mathrm{V}$. La solution 1 utilise un transformateur triphasé suivi d'un pont P3 (3 diodes, cathodes communes). La tension moyenne en sortie du redresseur P3 est :
$$\bar{u}_s = \frac{3\sqrt{6}}{2\pi} \cdot V_{eff,simple}$$
Le cahier des charges impose $\bar{u}_s = 600\ \mathrm{V}$. Donner l'expression du rapport de transformation $m$ du transformateur étoile-étoile.

**Corrigé :**
- Tension simple secondaire nécessaire : $V_{s,simple} = \dfrac{600 \times 2\pi}{3\sqrt{6}} \approx \dfrac{600 \times 6{,}283}{7{,}348} \approx 513\ \mathrm{V}$
- Côté primaire : $V_{1,simple} = 230\ \mathrm{V}$ (réseau)
- Rapport de transformation : $m = \dfrac{V_{s,simple}}{V_{1,simple}} = \dfrac{513}{230} \approx 2{,}23$

*(Note : le sujet propose d'autres structures pour améliorer le facteur de puissance — cf. T08)*

---

### Q2 — Sujet 2026, E1 Partie E, Question E10 (couplage étoile-étoile, tension composée)

**Source :** `2026/E1_Sujet_2026/E1_Sujet_2026.md`, Partie E

**Énoncé :** Pour la solution 2 (pont PD3, $q = 6$ diodes), la tension moyenne vaut $\bar{u}_s = 0{,}95 \cdot U_M$ où $U_M$ est l'amplitude des tensions composées secondaires. Pour obtenir $600\ \mathrm{V}$, calculer $U_M$ puis en déduire la valeur efficace des tensions composées secondaires $U_{s,composée}$, et enfin le rapport de transformation $m$ (couplage étoile-étoile, primaire $400\ \mathrm{V}$).

**Corrigé :**
- $U_M = \dfrac{600}{0{,}95} \approx 631\ \mathrm{V}$
- $U_{s,composée} = \dfrac{U_M}{\sqrt{2}} = \dfrac{631}{\sqrt{2}} \approx 446\ \mathrm{V}$
- $m = \dfrac{U_{s,composée}}{U_{1,composée}} = \dfrac{446}{400} \approx 1{,}12$

---

### Q3 — Sujet 2026 BAC3, E2, Questions A12–A13 (essai à vide machine asynchrone — schéma analogue)

**Source :** `2026/E2_Sujet_2026_BAC3/E2_Sujet_2026_BAC3.md`, Questions A12–A13

**Énoncé :** Lors de l'essai à vide d'une machine asynchrone ($g \approx 0$), le schéma équivalent simplifié se réduit à $R_f$ et $X_m$ en parallèle. Avec $P_0 = 7{,}82\ \mathrm{kW}$ et $V_1 = 133\ \mathrm{V}$ (tension simple) : exprimer $P_0$ et $Q_0$ puis calculer $R_f$ et $X_m$.

**Corrigé :**
- $S_0 = V_1 \cdot I_0$, $P_0 = \dfrac{V_1^2}{R_f}$, donc $R_f = \dfrac{V_1^2}{P_0}$
- $R_f = \dfrac{133^2}{7820} \approx \dfrac{17689}{7820} \approx 2{,}26\ \Omega$
- $Q_0 = \sqrt{S_0^2 - P_0^2}$, puis $X_m = \dfrac{V_1^2}{Q_0}$
- *(Les valeurs numériques de $I_0$ et $X_m$ sont à calculer en séance avec les données complètes)*

---

## 3. ATTENTES DU JURY

| Source | Citation directe | Implication pour le candidat |
|---|---|---|
| `2025/Rapport_Jury_2025.md` | "De nombreux candidats ne maîtrisent pas les lois basiques de l'électricité (la loi des nœuds, la loi des mailles, les calculs de puissance ou encore la loi d'Ohm)" | Maîtriser les bilans de puissance $P_0$, $Q_0$, $S_0$ et leurs relations avec $R_f$, $X_m$ |
| `2025/Rapport_Jury_2025.md` | Le jury apprécie "la justification des démarches" et la "rigueur scientifique" | Ne pas juste écrire la formule : énoncer le modèle, les hypothèses (fréquence fixe, noyau magnétique linéaire), puis calculer |
| `2024/Rapport_Jury_2024.md` | Commentaire général sur les convertisseurs : les candidats confondent souvent les couplages étoile/triangle et les rapports de transformation associés | Vérifier si $m$ porte sur les tensions simples ou composées selon le couplage |

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique | Source |
|---|---|---|
| Réseau primaire triphasé | $230/400\ \mathrm{V}$, $50\ \mathrm{Hz}$ | Tous sujets |
| Tension secondaire (redresseur P3 → 600 V DC) | $V_{s,simple} \approx 513\ \mathrm{V}$ | 2026 E1 |
| Tension secondaire (redresseur PD3 → 600 V DC) | $U_{s,composée} \approx 446\ \mathrm{V}$ | 2026 E1 |
| Rapport de transformation P3 | $m \approx 2{,}2$ | 2026 E1 |
| Rapport de transformation PD3 | $m \approx 1{,}1$ | 2026 E1 |
| Pertes fer essai à vide | $P_0 = 7{,}82\ \mathrm{kW}$ (MAS, contexte similaire) | 2026 BAC3 |
| Tension simple d'essai à vide | $V_1 = 133\ \mathrm{V}$ | 2026 BAC3 |
| Tension de court-circuit relative $\varepsilon_{cc}$ | $4\ \%$ à $10\ \%$ | Cours général |
| Rendement typique transformateur | $\eta > 95\ \%$ | Cours général |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Confusion tensions simples / composées** : en couplage étoile-étoile, le rapport $m = U_{s,composée}/U_{1,composée} = V_{s,simple}/V_{1,simple}$. En couplage étoile-triangle, les tensions côté triangle sont des tensions composées ($\sqrt{3}$ fois les tensions simples) — ne pas appliquer $m$ sans vérifier.

2. **Oubli du facteur $\sqrt{3}$** : $U_{composée} = \sqrt{3} \cdot V_{simple}$ pour un couplage étoile.

3. **Essai à vide vs essai court-circuit** : à vide → pertes **fer** ($R_f$, $X_m$), courant faible. En court-circuit → pertes **cuivre** ($R_s = R_1 + m^2 R_2$), tension faible. Les candidats inversent parfois les deux.

4. **Signe de $Q_0$** : $Q_0 = \sqrt{S_0^2 - P_0^2}$ est toujours positif (inductif) ; certains candidats utilisent $P^2 - S^2$ et obtiennent une valeur imaginaire.

5. **Rapport de transformation et redresseur** : le transformateur en amont d'un redresseur a un $m$ déterminé par la tension DC souhaitée, pas directement par le rapport réseau. Il faut d'abord calculer la tension secondaire AC nécessaire, puis en déduire $m$.

6. **Décalage de phase couplage Yd** : le déphasage de $30°$ entre primaire et secondaire en couplage Yd est rarement demandé explicitement, mais peut être évoqué dans la justification du choix de couplage pour l'élimination d'harmoniques.

7. **Boucherot et valeur efficace de B** : introduire une induction efficace dans la formule de Boucherot. La formule fait intervenir l'induction crête $B_{max}$, qui vaut $\sqrt{2}$ fois l'induction efficace.

8. **Réluctance de l'entrefer** : négliger un entrefer de quelques dixièmes de millimètre. Avec une perméabilité relative du fer de 1 000 à 5 000, un entrefer de 0,5 mm peut présenter une réluctance supérieure à celle de tout le circuit en fer.

9. **Saturation** : appliquer la loi d'Hopkinson au-delà du coude de saturation. La relation linéaire ne vaut que pour une induction inférieure à environ 1,2 à 1,5 T dans les tôles usuelles.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

| Thème associé | Articulation |
|---|---|
| **T08 — Redresseurs** | Le transformateur est quasi toujours présent en amont du redresseur pour adapter la tension AC secondaire à la tension DC souhaitée. Le choix P3 vs PD3 influe directement sur $m$ (exemple 2026 E1). |
| **T02 — Machine asynchrone (MAS)** | Le schéma équivalent de la MAS à $g = 0$ est identique au modèle à vide du transformateur ($R_f$, $X_m$) — les essais à vide de la MAS sollicitent les mêmes formules (Q.A12–A13, 2026 BAC3). |
| **T09 — Onduleurs** | Les onduleurs alimentent parfois des transformateurs (isolation galvanique, adaptation de tension côté réseau). |
| **T01 — Circuits AC monophasé/triphasé** | La loi des tensions (mailles), des courants (nœuds) et les calculs de puissance active/réactive sont les outils de base pour les deux essais. |
| **T05 — Qualité de l'énergie / harmoniques** | Le couplage Yd du transformateur peut éliminer certains rangs harmoniques (rangs multiples de 3) injectés par les redresseurs. |
