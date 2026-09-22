# T13 — Machine asynchrone (MAS)
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

| Formule LaTeX | Contexte | Fréquence | Source |
|---|---|---|---|
| $N_s = \frac{60 f}{p}$ | Vitesse de synchronisme (tr·min$^{-1}$), avec $p$ paires de pôles | Très fréquent | 2024 E2 disc., 2023 Rapport |
| $g = \frac{N_s - N}{N_s} = \frac{\omega_s - \omega}{\omega_s}$ | Glissement nominal | Très fréquent | 2024 E2 disc. (A3) |
| $P_a = 3 V_s I_s \cos\varphi_{mot}$ | Puissance absorbée au stator | Très fréquent | 2024 E2 disc. (A5) |
| $P_{Js} = 3 R_s I_s^2$ | Pertes joules au stator | Fréquent | général |
| $P_t = P_a - P_{Js} - P_{Fs}$ | Puissance transmise au rotor = puissance absorbée − pertes joules stator − pertes fer stator | Très fréquent | 2024 E2 disc. DT1 |
| $P_{Jr} = g \cdot P_t = 3 R'_R I'^2_r$ | Pertes joules au rotor | Très fréquent | 2024 E2 disc. DT1 |
| $P_{meca} = (1-g) \cdot P_t$ | Puissance mécanique développée au rotor | Très fréquent | 2024 E2 disc. DT1 |
| $P_u = P_{meca} - P_{pm} = C_u \cdot \Omega$ | Puissance utile en sortie de l'arbre (pertes mécaniques $P_{pm} = C_p \Omega$) | Très fréquent | 2024 E2 disc. (A6) |
| $C_{em} = \frac{P_t}{\Omega_s}$ | Couple électromagnétique | Très fréquent | général |
| $C_u = C_{em} - C_p$ | Couple utile = couple EM − couple de pertes | Fréquent | 2024 E2 disc. |
| $I'_r = \frac{V_s}{\sqrt{R'^2_R/g^2 + (L_f \omega_s)^2}}$ | Courant rotorique ramené au stator (schéma équivalent simplifié, $L_M \to \infty$) | Fréquent | 2024 E2 disc. (A4) |
| $C_{em} \approx \frac{3p V_s^2}{R'_R \omega_s^2} \cdot g$ | Couple EM linéarisé pour faibles glissements ($g \ll 1$) | Fréquent | 2024 E2 disc. (C1) |
| $C_{em}(p) = A \cdot \omega_r(p) = \frac{3p V_s^2}{R'_R \omega_s^2} \cdot \omega_r$ | Couple EM en fonction de la pulsation rotorique $\omega_r = g \cdot \omega_s$ | Présent | 2024 E2 disc. (C2) |
| $\Omega(p) = \frac{K_{meca}}{1 + \tau_{meca} p} [C_{em}(p) - C_r(p)]$ | Modèle mécanique de la MAS dans le domaine de Laplace | Fréquent | 2024 E2 disc. (C3) |
| $K_{meca} = 1/f$, $\tau_{meca} = J/f$ | Gain et constante de temps mécaniques | Fréquent | 2024 E2 disc. |
| $\text{THD} = \frac{\sqrt{I_2^2 + I_3^2 + \ldots + I_n^2}}{I_1}$ | Taux de distorsion harmonique (norme IEC/EN 61000-2-2 : THD < 25%) | Présent | 2024 E2 disc. (B10) |

**Schéma équivalent monophasé de la MAS (circuit de Thévenin simplifié) :**

```
Is      Rf       Lf·ωs         Ir'
Vs ─── ─── jLMωs ─── jLfωs ─── R'R/g ───
```

Où :
- $R_f$ : résistance pertes fer stator (souvent négligée ou mise en parallèle)
- $R'_R/g$ : résistance rotorique ramenée au stator, dépendante du glissement
- $L_M$ : inductance magnétisante (circuit ouvert pour les calculs simplifiés)
- $L_f$ : inductance rotorique de fuite ramenée au stator

**Bilan de puissance complet :**

$$P_a \xrightarrow{-P_{Js}-P_{Fs}} P_t \xrightarrow{-P_{Jr}=-g P_t} P_{meca}=(1-g)P_t \xrightarrow{-P_{pm}} P_u = C_u \Omega$$

**Commande scalaire V/f :** Pour maintenir le flux magnétique constant lors d'une variation de fréquence, on maintient le rapport $V_s/f$ constant. Cela permet de faire varier la vitesse tout en conservant les performances en couple.

**Démarrage étoile-triangle :**
- En étoile : tension par enroulement = $V_{réseau}/\sqrt{3}$, courant de démarrage divisé par 3
- Passage en triangle une fois la vitesse quasi-nominale atteinte
- Convient pour les démarrages à vide ou faible charge (couple de démarrage réduit)

---

## 2. QUESTIONS TYPES

**Q1 — Source : CAPET 2024, E2 disciplinaire (Extracteur d'air atelier), Questions A1–A7**

*Énoncé complet :* La plaque signalétique du moteur asynchrone indique : $V_{composée} = 400$ V, $V_s = 230$ V, $I_s = 229$ A, $\cos\varphi_{mot} = 0{,}85$, $f = 50$ Hz, $N = 1400$ tr·min$^{-1}$, $p = 2$ paires de pôles. Le courant rotorique calculé est $I'_r = 122$ A, le couple de pertes $C_p = 200$ N·m. Calculer la vitesse synchrone $N_s$, le glissement nominal $g$, la puissance absorbée $P_a$, les pertes joules rotoriques $P_{Jr}$, et la puissance utile $P_u$.

*Corrigé complet :*
- $N_s = 60f/p = 60 \times 50 / 2 = 1500$ tr·min$^{-1}$
- $g = (N_s - N)/N_s = (1500 - 1400)/1500 = 100/1500 = 0{,}0\overline{6} \approx 6{,}67\%$
- $P_a = 3 V_s I_s \cos\varphi = 3 \times 230 \times 229 \times 0{,}85 = 134{,}6$ kW
- $P_t = 3 \frac{R'_R}{g} I'^2_r = 3 \times (0{,}1/0{,}0\overline{6}) \times 122^2 = 3 \times 1{,}5 \times 14884 = 67{,}0$ kW (puissance transmise)
- $P_{Jr} = g \cdot P_t = 0{,}0\overline{6} \times 67000 = 4467$ W $\approx 4{,}47$ kW
- $P_{meca} = (1-g) P_t = 0{,}933 \times 67000 = 62{,}5$ kW
- $\Omega = 1400 \times 2\pi/60 = 146{,}6$ rad·s$^{-1}$
- $P_{pm} = C_p \cdot \Omega = 200 \times 146{,}6 = 29{,}3$ kW
- $P_u = P_{meca} - P_{pm} = 62{,}5 - 29{,}3 = 33{,}2$ kW → (le sujet précise : utiliser $I'_r = 122$ A, résultat $P_u$ ≈ 100 kW avec les vraies données du DT1)

*Note : le sujet donne ensuite $P_u = 100$ kW pour la suite. L'important est la méthode.*

---

**Q2 — Source : CAPET 2024, E2 disciplinaire, Questions C1–C2**

*Énoncé complet :* Pour un faible glissement ($g \approx 0$), montrer que le couple EM peut s'écrire $C_{em} = \frac{3p V_s^2}{R'_R \omega_s^2} \cdot g$. En déduire que $C_{em} = A \cdot \omega_r$ avec $A = \frac{3p V_s^2}{R'_R \omega_s^2}$.

*Corrigé complet :*
- Équation 1 du DT1 pour $g \approx 0$ : $I'_r \approx \frac{V_s g}{R'_R/\omega_s} \cdot \frac{1}{\omega_s} = \frac{V_s g}{R'_R/\omega_s}$... En simplifiant le schéma équivalent avec $L_f \omega_s \ll R'_R/g$ (pour $g$ petit) :
$$I'_r \approx \frac{V_s}{\frac{R'_R}{g}} = \frac{V_s \cdot g}{R'_R}$$
- $P_t = 3 \frac{R'_R}{g} I'^2_r = 3 \frac{R'_R}{g} \cdot \frac{V_s^2 g^2}{R'^2_R} = \frac{3 V_s^2 g}{R'_R}$
- $C_{em} = P_t / \Omega_s = \frac{3 V_s^2 g}{R'_R \omega_s} \cdot p = \frac{3p V_s^2}{R'_R \omega_s^2} \cdot g \cdot \omega_s = \frac{3p V_s^2}{R'_R \omega_s^2} \cdot (g \omega_s) = A \cdot \omega_r$
- Avec $\omega_r = g \omega_s$ la pulsation des champs au rotor.

---

**Q3 — Source : CAPET 2024, E2 disciplinaire, Question C3**

*Énoncé complet :* Montrer que l'équation mécanique de la MAS (équation 3 du DT1) peut s'écrire dans le domaine de Laplace : $\Omega(p) = \frac{K_{meca}}{1 + \tau_{meca} p} [C_{em}(p) - C_r(p)]$. Exprimer $K_{meca}$ et $\tau_{meca}$.

*Corrigé complet :*
- Équation 3 du DT1 : $J \frac{d\Omega}{dt} + f\Omega = C_{em} - C_r$
- Dans le domaine de Laplace : $Jp\Omega(p) + f\Omega(p) = C_{em}(p) - C_r(p)$
- $\Omega(p)(Jp + f) = C_{em}(p) - C_r(p)$
- $\Omega(p) = \frac{1/f}{1 + (J/f)p} [C_{em}(p) - C_r(p)]$
- Donc $K_{meca} = 1/f$ et $\tau_{meca} = J/f$
- Valeurs numériques : $J = 0{,}035$ kg·m², $f = 4 \times 10^{-3}$ N·m·s·rad$^{-1}$
- $K_{meca} = 1/0{,}004 = 250$ rad·s$^{-1}$·N$^{-1}$·m$^{-1}$
- $\tau_{meca} = 0{,}035/0{,}004 = 8{,}75$ s

---

**Q4 — Source : CAPET 2023, Rapport jury, Questions 18–20 (MAS serre ventilation)**

*Énoncé complet :* La vitesse nominale d'un moteur asynchrone est $N_{nom} = 950$ tr·min$^{-1}$ pour $f = 50$ Hz. Le couple varie linéairement autour du point de fonctionnement nominal. La loi V/f impose $C = 0{,}32 \cdot (N_s - N)$. Calculer la fréquence d'alimentation pour les vitesses $N = 450$ tr·min$^{-1}$ (hiver) et $N = 800$ tr·min$^{-1}$ (été).

*Corrigé complet :*
- $p = 3$ paires de pôles (calculé au Q18)
- Loi couple-glissement : $C = 0{,}32 \cdot (N_s - N) = 0{,}32 \cdot (60f/3 - N)$
- En régime établi, $C_{charge} = C_{moteur}$ → $C \propto N^2$ (ventilateur centrifuge), donc $f = 1{,}77 \times 10^{-5} N^2 + N \cdot p/60$... (loi donnée dans le sujet)
- Pour $N = 450$ tr·min$^{-1}$ : $f = 23{,}1$ Hz
- Pour $N = 800$ tr·min$^{-1}$ : $f = 41{,}8$ Hz

---

**Q5 — Source : CAPET 2024, E2 disciplinaire, Question A2**

*Énoncé complet :* La puissance nécessaire à l'extracteur est $P_{extra} = \Delta p \times D_t$ avec $\Delta p = 5297$ Pa et $D_t$ le débit total en m$^3$·s$^{-1}$. Le ventilateur a un rendement $\eta = 0{,}78$. Les salles ont des volumes $V_1 = 2500$ m$^3$ et $V_2 = 2750$ m$^3$, avec 10 renouvellements par heure et vitesse d'air max 5 m·s$^{-1}$. Calculer $P_{extra}$ et la puissance utile $P_u$ du moteur.

*Corrigé complet :*
- $D_t = (V_1 + V_2) \times 10 / 3600 = 5250 \times 10 / 3600 = 14{,}58$ m$^3$·s$^{-1}$
- $P_{extra} = 5297 \times 14{,}58 = 77{,}23$ kW
- $P_u = P_{extra} / \eta = 77{,}23 / 0{,}78 = 99{,}0$ kW $\approx 100$ kW

---

**Q6 — Source : CAPET 2024, E2 disciplinaire, Questions B10–B11**

*Énoncé complet :* Le variateur de vitesse commande l'onduleur en MLI à $f_p = 6000$ Hz. Le DT3 fournit le spectre du courant réseau avec $I_1 = 100$ A, $I_3 = 5$ A, $I_5 = 4$ A, $I_7 = 2$ A, $I_9 = 1$ A (valeurs fictives pour illustration). Calculer le THD et conclure vis-à-vis de la norme.

*Corrigé complet :*
- $\text{THD} = \frac{\sqrt{5^2 + 4^2 + 2^2 + 1^2}}{100} = \frac{\sqrt{25 + 16 + 4 + 1}}{100} = \frac{\sqrt{46}}{100} = \frac{6{,}78}{100} = 6{,}78\%$
- THD = 6,78% < 25% → **conforme à la norme IEC/EN 61000-2-2**
- Comparaison avec commande pleine onde : THD beaucoup plus élevé (plusieurs dizaines de %) car les harmoniques de rang faible (3, 5, 7) sont importants. La MLI repousse les harmoniques vers les hautes fréquences (autour de $f_p$ et ses multiples) → THD pleine onde > 25%.

---

## 3. ATTENTES DU JURY

**Source : Rapport jury 2024, commentaires E2 Disciplinaire (Partie A)**

> « L'objectif de cette partie est de dimensionner le variateur et du moto-extracteur électrique pour optimiser la consommation énergétique. En premier lieu, il s'agit d'établir le cahier des charges du client, de sélectionner une machine asynchrone avec un variateur de vitesse puis de calculer ses pertes. Seulement 55% des candidats l'ont traitée correctement. »

*Implication* : Maîtriser le bilan de puissance de la MAS et savoir calculer les grandeurs successives ($P_a \to P_t \to P_{meca} \to P_u$).

**Source : Rapport jury 2024, analyse globale E2 Disciplinaire**

> « Le jury regrette le manque de maîtrise des formules de base sur les réseaux triphasés, le régime sinusoïdal et les relations d'électrocinétique. »

*Implication* : La formule $P_a = 3 V_s I_s \cos\varphi$ en triphasé (tension SIMPLE × courant de phase) doit être assimilée. Ne pas oublier le facteur 3.

**Source : Rapport jury 2023, commentaires (MAS ventilation serre)**

> « La majorité des candidats maîtrise la formule de la vitesse de synchronisme mais beaucoup oublient de vérifier que le résultat est un entier pour le nombre de paires de pôles. Le jury attend un raisonnement explicite. »

*Implication* : Calculer $p = 60f/N_{nom}$, vérifier que c'est proche d'un entier, puis recalculer $N_s$ avec $p$ entier.

**Source : Rapport jury 2024, Conclusion**

> « Le jury apprécie les copies qui justifient les démarches. Des résultats donnés directement, sans calcul et sans justification ne répondent pas aux attendus. »

*Implication* : Écrire l'expression littérale, puis l'application numérique avec unités, puis une phrase de conclusion par rapport au cahier des charges.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique | Source |
|---|---|---|
| Tensions réseau | $U_{composée} = 400$ V, $V_s = 230$ V | 2024 E2 disc. |
| Courant nominal | 229 A | 2024 E2 disc. |
| Facteur de puissance | $\cos\varphi = 0{,}85$ | 2024 E2 disc. |
| Vitesse nominale | 1400 tr·min$^{-1}$ ($p = 2$, $N_s = 1500$) | 2024 E2 disc. |
| Glissement nominal | $g = 6{,}67\%$ | 2024 E2 disc. |
| $R'_R$ (résistance rotorique ramenée) | 0,1 Ω | 2024 E2 disc. DT1 |
| $L_f$ (inductance rotorique ramenée) | 3,6 mH | 2024 E2 disc. DT1 |
| $J$ (moment d'inertie arbre moteur) | 0,035 kg·m² | 2024 E2 disc. DT1 |
| $f$ (coefficient frottement visqueux) | $4 \times 10^{-3}$ N·m·s·rad$^{-1}$ | 2024 E2 disc. DT1 |
| Couple de pertes | $C_p = 200$ N·m | 2024 E2 disc. |
| Puissance extracteur d'air | 100 kW (nominale) | 2024 E2 disc. |
| Vitesse synchronisme serre (p=3) | 1000 tr·min$^{-1}$ | 2023 Rapport |
| Vitesse nominale serre | 950 tr·min$^{-1}$, $g = 5\%$ | 2023 Rapport |
| Fréquence variateur hiver/été | 23,1 Hz / 41,8 Hz | 2023 Rapport |
| THD norme max | 25% (IEC/EN 61000-2-2) | 2024 E2 disc. |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Oubli du facteur 3 en triphasé** : $P_a = 3 V_s I_s \cos\varphi$ et non $V_s I_s \cos\varphi$. Erreur très fréquente.

2. **Confusion entre puissance transmise et puissance mécanique** : $P_t$ est la puissance transmise au rotor (= puissance de l'entrefer), $P_{meca} = (1-g)P_t$ est la puissance mécanique développée. $P_{Jr} = g \cdot P_t$ est perdue par effet Joule au rotor.

3. **Nombre de paires de pôles non entier** : calculer $p = 60f/N_{nom}$, arrondir à l'entier le plus proche, puis recalculer $N_s$ avec cet entier. Beaucoup de candidats oublient cette vérification.

4. **Glissement exprimé en % vs valeur décimale** : $g = 0{,}05$ (décimal) dans les formules, pas $g = 5$. L'oubli de cette conversion donne des résultats aberrants.

5. **Signe du glissement en générateur** : $g < 0$ pour un fonctionnement en générateur (frein asynchrone ou production). Vérifier le signe dans les questions portant sur la réversibilité.

6. **THD et pleine onde vs MLI** : la MLI repousse les harmoniques vers les hautes fréquences mais ne les élimine pas. Un filtre CLC est nécessaire pour respecter la norme. Ne pas conclure que la MLI seule suffit.

7. **Modèle scalaire vs vectoriel** : au CAPET, le modèle utilisé est le modèle scalaire (V/f) avec approximation des faibles glissements. Le contrôle vectoriel (FOC) n'est pas au programme mais le terme peut apparaître dans les sujets récents.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

| Thème connexe | Articulation |
|---|---|
| **T10 Mécanique** | La puissance utile $P_u = C_u \Omega$ lie la MAS à la charge mécanique ; le couple résistant de la charge ventilateur ($C \propto N^2$) détermine le point de fonctionnement |
| **T12 Machine synchrone** | Comparaison des deux types : MAS moins chère, robuste, mais glissement et couple de démarrage limités ; MS plus efficace, vitesse parfaitement contrôlée par la fréquence |
| **T02 Puissance AC** | Le réseau triphasé alimente la MAS ; facteur de puissance inductif ($\cos\varphi = 0{,}85$) nécessite correction par condensateurs pour réduire la puissance réactive |
| **T11 MCC** | Comparaison : la MCC offre un meilleur contrôle du couple (proportionnel au courant) mais nécessite plus d'entretien ; la MAS avec variateur devient concurrente pour les applications à vitesse variable |
| **Asservissements (T14, T15)** | Le modèle de Laplace de la MAS $\Omega(p) = K_{meca}/(1+\tau_{meca}p) \cdot [C_{em}-C_r]$ est la base du réglage de la boucle de vitesse (partie C du sujet 2024) |
| **Convertisseurs** | Le variateur de vitesse (pont redresseur + onduleur MLI) est indissociable de la MAS moderne ; les harmoniques générés impactent le réseau (THD) et nécessitent un filtrage |
