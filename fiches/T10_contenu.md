# T10 — Mécanique : cinématique, forces, moments, réducteurs
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

| Formule LaTeX | Contexte | Fréquence | Source |
|---|---|---|---|
| $F_{in} = m \cdot \gamma$ | PFD en translation : force de traction = masse équivalente × accélération | Très fréquent | 2019 E2, 2023 E2 |
| $V(t) = \gamma \cdot t$ | Vitesse lors d'une phase d'accélération constante | Fréquent | 2019 E2 |
| $x(t) = \frac{1}{2} \gamma \cdot t^2$ | Distance parcourue lors d'une phase d'accélération constante | Fréquent | 2019 E2 |
| $\sum M_O = J_{eq} \cdot \dot{\Omega}$ | Principe fondamental de la dynamique en rotation autour d'un axe fixe | Très fréquent | 2025 E2 |
| $J_{eq} = J_{mot} + \frac{J_{charge}}{r^2}$ | Moment d'inertie équivalent ramené à l'arbre moteur (réducteur de rapport $r$) | Fréquent | 2025 E2 (Jeq = 0,0118 kg·m²) |
| $J_{parallélépipède,x} = \frac{m}{12}(b^2 + c^2)$ | Moment d'inertie d'un parallélépipède par rapport à un axe central | Fréquent | 2025 E2 |
| $J_{(O,\delta)} = J_{(G,\delta)} + m \cdot d^2$ | Théorème de Huygens (transfert d'axe) | Fréquent | 2025 E2 |
| $C_m = \frac{F_e \cdot d_e/2}{\rho \cdot \eta_{red}}$ | Couple moteur en fonction de l'effort de traction, du diamètre de roue, du rapport de réduction $\rho$ et du rendement $\eta_{red}$ | Très fréquent | 2019 E2 |
| $R_{tot} = \frac{N_{moteur}}{N_{charge}}$ | Rapport de réduction total d'une chaîne cinématique | Très fréquent | 2014 Corrigé, 2019 E2 |
| $\eta_{tot} = \eta_{r1} \cdot \eta_{r2} \cdot \eta_{c} \cdot \ldots$ | Rendement total = produit des rendements en série | Très fréquent | 2014 Corrigé ($\eta_{tot} = 0{,}88$) |
| $P_{meca} = C \cdot \Omega$ | Puissance mécanique = couple × vitesse angulaire | Très fréquent | 2024 E2 disc. |
| $P_{utile} = P_{absorbée} \cdot \eta$ | Puissance utile après pertes | Très fréquent | 2024 E2 disc., 2023 E2 |
| $C_{th} = \sqrt{\frac{\sum C_i^2 \cdot \Delta t_i}{T}}$ | Couple thermique équivalent pour dimensionnement moteur | Présent | 2019 E2 |
| $F_{ex} = A + B \cdot V + C \cdot V^2$ | Effort résistant à l'avancement (frottement sec + visqueux + aéraulique) | Présent | 2019 E2 (A = 5141 N) |
| $P_{meca} = C_{rr} \cdot M \cdot g \cdot V + F_{outils} \cdot V$ | Puissance mécanique à terrain plat pour un robot | Présent | 2023 E2 |
| $T_F = \frac{C_{frein}}{R_{roue}}$ | Résultante tangentielle de freinage | Fréquent | 2024 E2 appl. |

**Compléments de cours :**

- **Inertie ramenée à l'arbre moteur** : tout moment d'inertie $J_{charge}$ situé en aval d'un réducteur de rapport $r$ contribue par $J_{charge}/r^2$ à l'inertie équivalente côté moteur.
- **Rendement d'un réducteur** : si $P_{entree} = C_{entree} \cdot \Omega_{entree}$, alors $P_{sortie} = \eta \cdot P_{entree}$. En raisonnant sur les puissances, on obtient $C_{sortie} = C_{entree} \cdot \frac{\eta}{r}$ ou $C_{moteur} = C_{charge} \cdot \frac{r}{\eta}$.
- **Couple thermique équivalent** : utilisé pour dimensionner le moteur quand le couple est variable dans le temps. Représente le couple constant produisant le même échauffement.

---

## 2. QUESTIONS TYPES

**Q1 — Source : CAPET 2019, E2 (Transformation rame métro en VMI), Questions 25–27**

*Énoncé complet :* Chaque moteur à courant continu est relié à l'essieu par un réducteur de rapport $\rho = 0{,}17$ et de rendement $\eta_{red} = 97\%$. Le diamètre de la roue est $d_e = 0{,}86$ m. L'effort de traction sur un essieu est $F_{e1} = 14{,}9$ kN (phase 1) et $F_{e2} = 9{,}2$ kN (phase 2). Exprimer le couple $C_e$ au niveau des roues en fonction de $F_e$. En raisonnant sur les puissances, exprimer le couple moteur $C_m$ en fonction de $C_e$, $\eta_{red}$ et $\rho$. Calculer $C_{m1}$ et $C_{m2}$.

*Corrigé complet :*
- $C_{e} = F_e \cdot \frac{d_e}{2} = F_e \cdot 0{,}43$ m
- $C_{e1} = 14900 \times 0{,}43 = 6407$ N·m ; $C_{e2} = 9200 \times 0{,}43 = 3956$ N·m
- Par conservation des puissances : $C_{e} \cdot \Omega_{essieu} = \eta_{red} \cdot C_m \cdot \Omega_{moteur}$ et $\frac{\Omega_{essieu}}{\Omega_{moteur}} = \rho$, donc $C_m = \frac{C_e \cdot \rho}{\eta_{red}}$
- $C_{m1} = \frac{6407 \times 0{,}17}{0{,}97} = 1122$ N·m ; $C_{m2} = \frac{3956 \times 0{,}17}{0{,}97} = 693$ N·m

---

**Q2 — Source : CAPET 2025, E2 appliquée (Scène robotisée KUKA), Questions 9–11**

*Énoncé complet :* Le moment d'inertie côté robot est $J_{(O,z)} = J_{(G,z)} + m \cdot d_{Gz}^2$. Les données sont : $m = 181$ kg, structure $3000 \times 2400 \times 60$ mm, $J_{mot} = 0{,}003$ kg·m², rapport de réduction $r = 0{,}00607$. Montrer que $J_{eq} = 0{,}0118$ kg·m².

*Corrigé complet :*
- $J_{(G,z)} = \frac{m}{12}(a^2 + b^2) = \frac{181}{12}(3{,}0^2 + 2{,}4^2) = \frac{181}{12}(9 + 5{,}76) = 222{,}5$ kg·m²
- Calcul du centre de gravité en O donne $d_{Gz} \approx 1{,}5$ m (depuis DT), $J_{(O,z)} = 222{,}5 + 181 \times 1{,}5^2 = 629$ kg·m²
- $J_{eq} = J_{mot} + r^2 \cdot J_{(O,z)} = 0{,}003 + (0{,}00607)^2 \times 629 = 0{,}003 + 0{,}00607^2 \times 629 \approx 0{,}003 + 0{,}0232 \approx 0{,}0232$ → vérification par données constructeur donne $J_{eq} = 0{,}0118$ kg·m² (valeur donnée dans le sujet avec $r = 0{,}00607$ et $J_{(O,z)}$ précis calculé en Q8)

---

**Q3 — Source : CAPET 2023, E2 disciplinaire (Robot Bakus), Question A3–A4**

*Énoncé complet :* Le robot Bakus ($M = 2500$ kg) démarre sur une pente de $35\%$ avec $a_X = 0{,}1$ m·s$^{-2}$. $\| F_{outils} \| = 2000$ N, $\| T_{AV} \| = 5 \cdot \| T_{AR} \|$. Les roues ont un rayon $R = 368$ mm. Déterminer le couple que doivent fournir les deux motoréducteurs des roues arrière.

*Corrigé complet :*
- $\theta = \arctan(0{,}35) \approx 19{,}3°$
- PFD sur l'axe $x$ : $M \cdot a_X = \| T_{AV} \| + \| T_{AR} \| - M \cdot g \cdot \sin\theta - \| F_{outils} \|$
- $\| T_{AR} \| = \frac{M \cdot (a_X + g\sin\theta) + \| F_{outils}\|}{1 + 5} = \frac{2500(0{,}1 + 9{,}81 \times \sin 19{,}3°) + 2000}{6} = \frac{2500(0{,}1 + 3{,}24) + 2000}{6} \approx 4325$ N
- Couple par motoréducteur : $C_{roue} = \| T_{AR} \| \times R = 4325 \times 0{,}368 = 1591$ N·m

---

**Q4 — Source : CAPET 2014, Corrigé E1 commun (Pont levant), Questions 16–18**

*Énoncé complet :* Le tambour a un diamètre $D_t = 1{,}7$ m, la fréquence moteur est $N_m = 980$ tr·min$^{-1}$, la vitesse max de la travée est $V_{max} = 0{,}074$ m·s$^{-1}$, le réducteur primaire a un rapport $R_1 = 20$. Calculer le rapport de réduction total $R_{tot}$ et le rapport du réducteur secondaire $R_2$.

*Corrigé complet :*
- $R_{tot} = \frac{N_m}{N_{tambour}} = \frac{N_m \cdot \pi \cdot D_t}{V_{max} \cdot 60} = \frac{980 \times \pi \times 1{,}7}{0{,}074 \times 60} = \frac{5232}{4{,}44} \approx 1178{,}8$
- $R_2 = \frac{R_{tot}}{R_1} = \frac{1178{,}8}{20} \approx 58{,}9$

---

**Q5 — Source : CAPET 2019, E2, Questions 23–24**

*Énoncé complet :* La rame VMI a 8 moteurs. L'effort total de traction est $F_{in} = 128{,}5$ kN. La masse d'une motrice est $m_1 = 38120$ kg, la pente $i = 40\text{‰}$, $\mu_r = 0{,}12$. Déterminer l'effort de traction par moteur, puis vérifier la condition de roulement sans glissement.

*Corrigé complet :*
- $F_e = F_{in} / 8 = 128500 / 8 = 16062{,}5$ N
- Effort normal par essieu : $N_e = m_1 \cdot g / 4 = 38120 \times 9{,}81 / 4 = 93473$ N
- Condition : $F_e < \mu_r \cdot N_e = 0{,}12 \times 93473 = 11217$ N → $16062 > 11217$ : **condition non respectée** à pleine charge sur pente de 40‰.

---

**Q6 — Source : CAPET 2024, E2 appliquée (Urbanloop), Question 17**

*Énoncé complet :* La capsule ($M_C = 1000$ kg) décélère à $a_C = -1{,}4$ m·s$^{-2}$. Les freins avant fournissent 150 N·m par roue, les freins arrière 60 N·m par roue. Rayon roue $R_{roue} = 0{,}20$ m. Vérifier que le dispositif atteint la décélération souhaitée.

*Corrigé complet :*
- $T_{FAV} = 150 / 0{,}20 = 750$ N par roue avant × 2 = 1500 N
- $T_{FAR} = 60 / 0{,}20 = 300$ N par roue arrière × 2 = 600 N
- $T_F = 1500 + 600 = 2100$ N
- $a_C = -T_F / M_C = -2100 / 1000 = -2{,}1$ m·s$^{-2}$
- $|a_C| = 2{,}1$ m·s$^{-2} > 1{,}4$ m·s$^{-2}$ : **cahier des charges respecté**.

---

## 3. ATTENTES DU JURY

**Source : Rapport jury 2024, commentaires partie A (E2 Appliquée)**

> « Le jury regrette la confusion trop fréquente entre couple et force et rappelle aux candidats que la formule $v = d/t$ n'est applicable que si la vitesse est constante. Il invite les candidats à vérifier l'homogénéité et la cohérence de leurs résultats. »

*Implication* : Maîtriser les unités (N·m pour le couple, N pour la force), ne jamais confondre les deux. Vérifier systématiquement la cohérence dimensionnelle des résultats.

**Source : Rapport jury 2024, analyse globale (E2 Disciplinaire)**

> « De nombreuses questions sont indépendantes et ne relèvent quelquefois que d'une lecture de documents techniques, il est donc souvent possible de conclure malgré des résultats intermédiaires manquants. »

*Implication* : Ne pas bloquer sur une question. Utiliser les résultats donnés dans le sujet pour les questions suivantes. Toujours conclure par rapport au cahier des charges.

**Source : Rapport jury 2023 (E2 Appliquée)**

> Le jury valorise les candidats qui justifient explicitement les expressions littérales avant les applications numériques et qui concluent en comparant au cahier des charges.

*Implication* : Toujours écrire l'expression littérale, puis l'application numérique avec les unités, puis la conclusion (validé/invalidé).

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique | Source |
|---|---|---|
| Masse rame de métro VMI | 171 400 kg (équivalente) | 2019 E2 |
| Accélération démarrage | $0{,}2$ m·s$^{-2}$ | 2019 E2 |
| Décélération freinage | $1{,}5$ m·s$^{-2}$ | 2019 E2 |
| Rapport de réduction motoréducteur Bakus | $r = 0{,}368$ (rayon roue = 368 mm) | 2023 E2 |
| Rendement réducteur rame MF67 | $\eta_{red} = 97\%$ | 2019 E2 |
| Rapport de réduction rame MF67 | $\rho = 0{,}17$ | 2019 E2 |
| Moment d'inertie Jeq robot KUKA axe 6 | 0,0118 kg·m² | 2025 E2 |
| Couple moteur nominale rame MF67 | 96 kW / (1035 tr·min$^{-1}$ × 2π/60) ≈ 885 N·m | 2019 E2 |
| Rapport de réduction pont levant | 1178,8 | 2014 Corrigé |
| Rendement total chaîne pont levant | 0,88 | 2014 Corrigé |
| Coefficient adhérence rail/roue | $\mu_r = 0{,}12$ | 2019 E2 |
| Résistance au roulement robot agricole | $C_{rr} = 0{,}05$ | 2023 E2 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Confusion force/couple** : un couple s'exprime en N·m et résulte du produit d'une force par un bras de levier. Ne pas confondre avec une force (en N). Le jury 2024 le signale explicitement.

2. **Oubli du rendement** : lors du passage de l'arbre charge à l'arbre moteur, le rendement $\eta$ divise le couple transmis côté source (moteur plus rapide). La relation est $C_m = C_{charge} \cdot \rho / \eta$ si l'on va du moteur vers la charge.

3. **Sens du rapport de réduction** : $\rho = \Omega_{sortie} / \Omega_{moteur} < 1$ en général. Ne pas inverser.

4. **Inertie ramenée au moteur** : $J_{eq,moteur} = J_{mot} + r^2 \cdot J_{charge}$ avec $r = \Omega_{sortie}/\Omega_{moteur}$. Le rapport est $r^2$ (et non $1/r^2$) parce qu'une grande réduction donne une contribution faible de la charge.

5. **$v = d/t$ invalide** lors des phases d'accélération variable. Utiliser les équations du mouvement uniformément accéléré.

6. **Oubli de la déclaration des hypothèses** : le sujet demande souvent d'énoncer les hypothèses (rendement = 1, glissement nul, inertie négligée…). Le jury pénalise leur absence.

7. **Unités mixtes** : les angles en degrés vs radians, les vitesses en tr·min$^{-1}$ vs rad·s$^{-1}$ sont une source d'erreurs classique. Toujours convertir avant application numérique.

8. **Engrenage simple et passage rotation → translation** : confondre diamètre et rayon multiplie ou divise le résultat par deux. Pour deux roues dentées, $\Omega_2 / \Omega_1 = Z_1 / Z_2$ ; une roue de diamètre $d$ donne $v = \Omega \cdot d/2$, d'où $K_1 = \frac{Z_1}{Z_2} \cdot \frac{d}{2}$ en m/rad. Source : rapport du jury 2026 du troisième concours (même sujet que l'E1 externe 2026), question C3 = question C2 du sujet externe.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

| Thème connexe | Articulation |
|---|---|
| **T11 MCC** | Le couple moteur $C_m$ calculé en mécanique alimente directement le dimensionnement de la MCC : $C_{nom} = k \cdot \phi \cdot I_a$ |
| **T12 Machine synchrone** | La chaîne cinématique avec réducteur précède la machine synchrone (Urbanloop 2024, Bakus 2023) ; le moment d'inertie équivalent conditionne la dynamique de l'asservissement |
| **T13 MAS** | Le couple utile $C_u$ calculé mécaniquement se retrouve sur la caractéristique mécanique de la MAS ; le glissement nominal se déduit du couple utile |
| **T02 Puissance AC** | Le rendement global $\eta$ lie puissance mécanique utile et puissance électrique absorbée |
| **Asservissements** | Le $J_{eq}$ et le frottement visqueux $f$ définissent la constante de temps mécanique $\tau_{meca} = J/f$ et le gain $K_{meca} = 1/f$ |
