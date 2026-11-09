# T07 — Hacheurs (1, 2 et 4 quadrants)

---

## 1. FORMULES ET COURS

| Formule LaTeX | Contexte | Fréquence | Donnée sujet ou mémoire |
|---|---|---|---|
| $\langle u_{CS} \rangle = \alpha \cdot E$ | Tension moyenne sortie hacheur série (Buck) | Très fréquent | $\alpha \in [0{,}1]$, $E$ = tension source |
| $V_{DC} = \dfrac{E}{1-\alpha}$ | Tension moyenne sortie hacheur Boost (élévateur) | Très fréquent | $\alpha \in [0{,}1[$, $E$ = tension batterie côté bas |
| $\Delta i_L = \dfrac{E \cdot \alpha \cdot (1-\alpha)}{L \cdot f}$ | Ondulation courant inductance (hacheur Buck, conduction continue) | Très fréquent | $f$ = fréquence commutation, $L$ = inductance |
| $\Delta i_L = \dfrac{V_{DC} \cdot (1-\alpha)}{L \cdot f}$ | Ondulation courant inductance (Boost) | Fréquent | Forme équivalente |
| $\alpha_{max,ondulation} = 0{,}5$ | Rapport cyclique maximisant $\Delta i_L$ | Fréquent | À $\alpha = 0{,}5$ : $\Delta i_{L,max} = \dfrac{E}{4Lf}$ |
| $L_{min} = \dfrac{E \cdot \alpha_{max} \cdot (1-\alpha_{max})}{\Delta i_{L,max} \cdot f}$ | Inductance minimale (conduction continue garantie) | Fréquent | Dimensionnement au pire cas $\alpha = 0{,}5$ |
| $\Delta i_{L,entrelacé} = \dfrac{\Delta i_L}{n}$ | Ondulation résultante avec $n$ bras entrelacés | Courant | $n = 4$ bras → ondulation divisée par 4 (2023 E2D) |
| $t_{on} = \alpha \cdot T$, $t_{off} = (1-\alpha) \cdot T$ | Durées de conduction/blocage | Base | $T = 1/f$ |
| Hacheur 2 quadrants : $\langle u \rangle = \alpha \cdot E$, $i$ pouvant être $\pm$ | Commande MLI 2 quadrants (Buck réversible en courant) | Courant | Deux bras avec $T_1/D_1'$ et $T_2/D_2'$ |
| Pont en H (4 quadrants) : $\langle u \rangle = (2\alpha - 1) \cdot E$ | Tension moyenne réglable de $-E$ à $+E$ | Courant | Commande symétrique bipolaire |
| Bilan énergétique Boost : $E \cdot I_E = V_{DC} \cdot I_{DC}$ (sans pertes) | Conservation puissance (hacheur idéal) | Fréquent | Déduit depuis lois de Kirchhoff |
| Lois Kirchhoff hacheur Boost fermé ($Q_1$ passant) : $E = v_{L1} + 0$ ; $i_b = i_{L1}$ | Phase $t \in [0;\alpha T[$ | Fréquent | $v_{D1} = 0$ (diode bloquée) |
| Lois Kirchhoff hacheur Boost ouvert ($Q_1$ bloqué) : $E = v_{L1} + V_{DC}$ ; $i_{L1} = i_{DC}$ | Phase $t \in [\alpha T; T[$ | Fréquent | Diode $D_1$ passante |

---

## 2. QUESTIONS TYPES

### Q1 — Sujet 2023, E2D Questions C4–C6 : hacheur Buck, rapport cyclique et ondulation

**Source :** `2023/E2_Disciplinaire_IE_2023/E2_Disciplinaire_IE_2023.md`, Questions C4–C6

**Énoncé :** Un convertisseur DC/DC dévolteur (hacheur Buck) recharge une batterie Li-ion (robot Bakus) depuis une batterie LiFePO4 ($E = 500\ \mathrm{V}$). Interrupteurs : $K_a$ (commandé) et $K_b$ (diode). Conduction continue, courant $i_{Bakus}$ toujours positif, $i_L$ linéaire par morceaux.
- (C4) Exprimer $\langle u_{Li-ion} \rangle$ en fonction de $E$ et $\alpha$.
- (C5) Sachant que $\langle u_{Li-ion} \rangle \in [70\ ;\ 117{,}5]\ \mathrm{V}$, donner la plage de $\alpha$.
- (C6) Sachant que $\Delta i_{Bakus} \leq 2\ \mathrm{A}$, $f = 50\ \mathrm{kHz}$ et $E = 500\ \mathrm{V}$, calculer $L_{min}$.

**Corrigé :**
- (C4) Pendant $[0;\alpha T[$ : $K_a$ fermé, $u_{sortie} = E$ ; pendant $[\alpha T; T[$ : $K_b$ conduit, $u_{sortie} = 0$.
  $$\langle u_{Li-ion} \rangle = \alpha \cdot E$$
- (C5) $\alpha_{min} = \dfrac{70}{500} = 0{,}14$ ; $\alpha_{max} = \dfrac{117{,}5}{500} = 0{,}235$
- (C6) L'ondulation est maximale pour $\alpha = 0{,}5$ :
  $$\Delta i_{max} = \frac{E \cdot \alpha \cdot (1-\alpha)}{L \cdot f} \Rightarrow L_{min} = \frac{500 \times 0{,}5 \times 0{,}5}{2 \times 50\,000} = \frac{125}{100\,000} = 1{,}25\ \mathrm{mH}$$

---

### Q2 — Sujet 2023, E2D Questions C7 : 4 bras entrelacés

**Source :** `2023/E2_Disciplinaire_IE_2023/E2_Disciplinaire_IE_2023.md`, Question C7

**Énoncé :** Le convertisseur est réalisé avec 4 bras entrelacés (déphasage de $T/4$ entre chaque bras), chaque bras ayant l'inductance $L_{min} = 1{,}25\ \mathrm{mH}$. Quelle est l'ondulation résultante du courant $i_{Bakus}$ ?

**Corrigé :**
- Avec $n = 4$ bras entrelacés, les ondulations se compensent partiellement.
- L'ondulation résultante est divisée par $n = 4$ :
  $$\Delta i_{Bakus,entrelacé} = \frac{\Delta i_{L}}{4} = \frac{2}{4} = 0{,}5\ \mathrm{A} \ll 2\ \mathrm{A}$$
- Avantage : même spécification $L$ mais ondulation 4 fois réduite (ou $L$ 4 fois réduite pour même ondulation).

---

### Q3 — Sujet 2025, E2D Questions CV1 : hacheur Boost MPPT (photovoltaïque)

**Source :** `2025/E2_Disciplinaire_IE_2025/E2_Disciplinaire_IE_2025.md`, CV1

**Énoncé :** Le convertisseur CV1 adapte la tension des panneaux PV ($U_{PV}$) à la tension de bus DC ($E_b = 48\ \mathrm{V}$ batterie). Justifier que CV1 est un hacheur **élévateur** (Boost). Calculer le rapport cyclique $f_m$ pour les 3 points de fonctionnement : P1 ($U_1 = 195\ \mathrm{V}$), Pmax ($U = 317\ \mathrm{V}$), P2 ($U = 340\ \mathrm{V}$).

**Corrigé :**
- $V_{DC} = E_b = 48\ \mathrm{V}$ côté bas, $U_{PV} > E_b$ → CV1 est un **hacheur élévateur (Boost)**.
- Loi du Boost : $U_{PV} = f_m \cdot E_b$ (notation sujet), soit $f_m = U_{PV}/E_b$
- $f_{m1} = 195/48 \approx 4{,}06$ ; $f_{m,max} = 317/48 \approx 6{,}6$ ; $f_{m2} = 340/48 \approx 7{,}08$

*(Remarque : dans la notation du sujet 2025, $f_m$ joue le rôle de $1/(1-\alpha)$ ; les valeurs $> 1$ confirment le mode Boost.)*

---

### Q4 — Rapport Jury 2025, correction Q27–Q32 : lois de Kirchhoff hacheur Boost

**Source :** `2025/Rapport_Jury_2025/Rapport_Jury_2025.md`, Q27–Q32

**Énoncé :** Pour le hacheur élévateur CV3-1 ($E_b$ source, $V_{DC}$ charge) avec interrupteur $Q_1$ et diode $D_1$ : écrire les lois de Kirchhoff pendant les deux phases de commutation. En déduire $V_{DC} = E_b/(1-\alpha)$.

**Corrigé :**
- Phase 1 ($Q_1$ fermé, $t \in [0;\alpha T[$) : $v_{L1} = E_b$, diode $D_1$ bloquée, $i_{L1}$ croît.
- Phase 2 ($Q_1$ ouvert, $t \in [\alpha T;T[$) : $v_{L1} = E_b - V_{DC}$ (négatif si $V_{DC} > E_b$), $i_{L1}$ décroît.
- En régime permanent, la variation de courant dans $L$ sur une période est nulle (valeur moyenne de $v_L = 0$) :
  $$E_b \cdot \alpha T + (E_b - V_{DC})(1-\alpha)T = 0$$
  $$E_b \alpha + E_b(1-\alpha) - V_{DC}(1-\alpha) = 0 \Rightarrow E_b = V_{DC}(1-\alpha)$$
  $$\boxed{V_{DC} = \frac{E_b}{1-\alpha}}$$

---

### Q5 — Rapport Jury 2025, Q39–Q42 : sensibilité $V_{DC}$ à $\alpha$

**Source :** `2025/Rapport_Jury_2025/Rapport_Jury_2025.md`, Q39–Q42

**Énoncé :** $V_{DC} = E_b/(1-\alpha)$. Si $\alpha$ varie de $1\ \%$ (de $\Delta\alpha = 0{,}01$), quelle est la variation de $V_{DC}$ ? Si la batterie chute de $\Delta E_b$, quelle est la variation de $V_{DC}$ ?

**Corrigé (d'après rapport jury) :**
- $\dfrac{\partial V_{DC}}{\partial \alpha} = \dfrac{E_b}{(1-\alpha)^2}$ → variation $\Delta V_{DC} \approx 10{,}88\ \mathrm{V}$ pour $\Delta\alpha = 0{,}01$ (valeurs numériques sujet)
- Chute batterie $\Delta E_b \rightarrow \Delta V_{DC} \approx 49{,}5\ \mathrm{V}$ : le système est **très sensible** à $\alpha$ et à $E_b$, d'où la nécessité d'une boucle d'asservissement (MPPT ou régulation tension).

---

## 3. ATTENTES DU JURY

| Source | Citation directe | Implication pour le candidat |
|---|---|---|
| `2025/Rapport_Jury_2025.md` | Correction Q14 : "CV1=Hacheur, CV2=Redresseur, CV3=Onduleur — les fonctions explicites" | Être capable d'**identifier** rapidement la nature d'un convertisseur depuis son schéma et sa position dans la chaîne de conversion |
| `2025/Rapport_Jury_2025.md` | "Q18 : MPPT — boucle sur rapport cyclique hacheur jusqu'à dP=0" | Maîtriser le principe MPPT : $dP/dU = 0$ détermine le point de puissance maximale ; le hacheur est l'organe de contrôle |
| `2025/Rapport_Jury_2025.md` | Q27–Q32 : lois de Kirchhoff hacheur élévateur | "Trop peu de candidats appliquent correctement les lois de Kirchhoff aux deux phases de commutation" — écrire systématiquement $v_L$, $v_D$, $v_Q$ pour les deux états |
| `2023/Rapport_Jury_2023.md` | "Asservissement : trop peu de candidats l'ont traitée de manière satisfaisante" | La boucle de régulation du hacheur (correcteur P, PI) est un sujet récurrent ; revoir boucle ouverte, correcteur, marge de phase |

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique | Source |
|---|---|---|
| Fréquence commutation hacheur | $f = 50\ \mathrm{kHz}$ | 2023 E2D |
| Tension source hacheur Buck | $E = 500\ \mathrm{V}$ (batterie LiFePO4) | 2023 E2D |
| Plage tension sortie Buck | $70$ à $117{,}5\ \mathrm{V}$ (batterie Li-ion robot) | 2023 E2D |
| Ondulation courant max tolérée | $\Delta i \leq 2\ \mathrm{A}$ | 2023 E2D |
| Inductance minimale calculée | $L_{min} = 1{,}25\ \mathrm{mH}$ | 2023 E2D |
| Tension batterie Boost | $E_b = 48\ \mathrm{V}$ | 2025 E2D |
| Tension bus DC Boost | $V_{DC} = 195$ à $340\ \mathrm{V}$ (MPPT PV) | 2025 E2D |
| Rapport cyclique Boost | $\alpha \approx 0{,}75$ à $0{,}86$ | 2025 E2D |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Confusion Buck / Boost** : le Buck (dévolteur) donne $V_{out} = \alpha E < E$. Le Boost (élévateur) donne $V_{out} = E/(1-\alpha) > E$. L'erreur classique est d'appliquer la formule Buck à un schéma Boost.

2. **Signe de $v_L$ pendant la phase OFF du Boost** : $v_L = E_b - V_{DC} < 0$ (décroissance de $i_L$). Beaucoup de candidats écrivent $v_L = V_{DC} - E_b$ avec un mauvais signe et obtiennent un courant croissant dans les deux phases.

3. **Oubli de la condition de régime permanent** : $\langle v_L \rangle = 0$ sur une période est la clé pour dériver toutes les formules de tension moyenne (Buck et Boost). Sans cette condition, il est impossible de justifier les formules.

4. **Ondulation maximale à $\alpha = 0{,}5$** : certains candidats calculent $L_{min}$ pour la valeur de $\alpha$ nominal (ex. $\alpha = 0{,}14$) et non au pire cas ($\alpha = 0{,}5$), sous-estimant l'inductance nécessaire.

5. **Hacheur 4 quadrants (pont en H)** : la tension moyenne $\langle u \rangle = (2\alpha - 1) E$ suppose une commande symétrique bipolaire. Avec une commande unipolaire, la fréquence effective de l'ondulation est doublée ($2f$).

6. **Entrelacement de bras** : l'ondulation se divise par $n$ **seulement si les $n$ bras sont déphasés de $T/n$**. Sans déphasage, l'ondulation s'additionne.

7. **Deux quadrants et sens de rotation** : croire qu'un hacheur réversible en courant permet d'inverser le sens de rotation d'une MCC. Il inverse le courant, donc le couple (freinage récupératif), mais pas la tension ; inverser le sens de rotation demande un pont en H à quatre quadrants.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

| Thème associé | Articulation |
|---|---|
| **T08 — Redresseurs** | Dans un variateur de vitesse, la chaîne typique est : Redresseur → Filtre → Hacheur (ou onduleur). Le hacheur Buck peut alimenter la charge DC issue du redresseur PD2 (2024 E2A, capsule Urbanloop). |
| **T09 — Onduleurs** | Le hacheur Boost est souvent l'étage d'entrée (PV → bus DC élevé) avant l'onduleur triphasé. Le bus DC $V_{DC}$ est commun aux deux convertisseurs. |
| **T02 — Machines à courant continu / asservissement** | La vitesse d'une MCC est proportionnelle à la tension d'armature → régulée par $\alpha$ du hacheur ; la boucle d'asservissement est un sujet récurrent au jury. |
| **T14 — MPPT / énergie solaire** | Le hacheur Boost est l'organe de commande du MPPT : la boucle recherche $dP/dU = 0$ en ajustant $\alpha$. |
| **T01 — Circuits magnétiques / inductances** | L'inductance $L$ du hacheur est dimensionnée pour limiter $\Delta i_L$ ; son comportement est régi par $v_L = L \cdot di_L/dt$. |
| **T05 — CEM / harmoniques** | Les hacheurs génèrent des harmoniques à la fréquence de commutation $f$ et ses multiples ; l'entrelacement réduit les harmoniques à $nf$. |
