# T11 — Machine à courant continu (MCC)
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

| Formule LaTeX | Contexte | Fréquence | Source |
|---|---|---|---|
| $U = E + R_a \cdot I_a$ | Équation électrique de la MCC en convention moteur ($U$ tension d'alimentation, $E$ FCEM, $R_a$ résistance d'induit, $I_a$ courant d'induit) | Très fréquent | 2019 E2, général |
| $E = k \cdot \phi \cdot \Omega$ | Force contre-électromotrice (FCEM) proportionnelle au flux inducteur $\phi$ et à la vitesse angulaire $\Omega$ | Très fréquent | 2019 E2 |
| $C_{em} = k \cdot \phi \cdot I_a$ | Couple électromagnétique développé par la MCC | Très fréquent | 2019 E2 |
| $P_{meca} = E \cdot I_a = C_{em} \cdot \Omega$ | Puissance mécanique développée par l'induit | Très fréquent | général |
| $P_{abs} = U \cdot I_a$ | Puissance électrique absorbée | Très fréquent | général |
| $\eta = \frac{C_{em} \cdot \Omega}{U \cdot I_a}$ | Rendement de la MCC | Fréquent | général |
| $U_{hacheur} = \alpha \cdot E_{dc}$ | Tension moyenne en sortie d'un hacheur de rapport cyclique $\alpha$ alimenté par une source continue $E_{dc}$ | Très fréquent | 2022 E2 appl. ($E_{dc} = 207$ V) |
| $\alpha = \frac{1}{2}\left(\frac{\langle u_f \rangle}{E} + 1\right)$ | Rapport cyclique d'un hacheur 4 quadrants | Présent | 2022 E2 appl. corrigé |
| $C_{nom} = \frac{P_{nom}}{\Omega_{nom}}$ | Couple nominal d'une MCC à partir de la puissance et de la vitesse nominales | Très fréquent | 2019 E2 (Q28) |
| $\Omega_{nom} = \frac{2\pi \cdot N_{nom}}{60}$ | Conversion tr·min$^{-1}$ → rad·s$^{-1}$ | Très fréquent | général |
| $I_{demarrage} = \frac{U}{R_a}$ | Courant de démarrage (à l'arrêt, $E = 0$) | Fréquent | général |
| $\Delta R_{rh}(t) = f(V_{train})$ | Loi de commande des rhéostats pour maintenir le courant constant lors du démarrage | Présent | 2019 E2 (Q7) |

**Modèle électrique de la MCC à excitation séparée (flux $\phi$ constant) :**

$$U = R_a \cdot I_a + L_a \cdot \frac{dI_a}{dt} + E \qquad \text{avec} \quad E = k\phi\Omega$$

En régime permanent (dérivée nulle) :

$$\Omega = \frac{U - R_a \cdot I_a}{k\phi}$$

**Bilan de puissance :**

$$P_{abs} = U \cdot I_a = R_a I_a^2 + E \cdot I_a = P_{joules} + P_{meca}$$

**Quadrants de fonctionnement :**

| Quadrant | Couple | Vitesse | Mode |
|---|---|---|---|
| I | $C > 0$ | $\Omega > 0$ | Moteur direct |
| II | $C < 0$ | $\Omega > 0$ | Générateur / frein récupératif |
| III | $C < 0$ | $\Omega < 0$ | Moteur inverse |
| IV | $C > 0$ | $\Omega < 0$ | Générateur inverse |

**Hacheur 4 quadrants (H-bridge) :**
- Permet la réversibilité en couple et en vitesse
- La tension moyenne de sortie est : $\langle U_{charge} \rangle = E_{dc} \cdot (2\alpha - 1)$ avec $0 \leq \alpha \leq 1$
- Pour $\alpha = 0{,}5$ : tension nulle (arrêt)
- Pour $\alpha > 0{,}5$ : tension positive (marche avant)
- Pour $\alpha < 0{,}5$ : tension négative (marche arrière)

---

## 2. QUESTIONS TYPES

**Q1 — Source : CAPET 2019, E2 (VMI rame métro), Questions 7–9**

*Énoncé complet :* Les moteurs à CC de la rame sont alimentés en série (4 moteurs). La tension d'alimentation est $V_{alim} = 750$ V. Lors du démarrage, le courant est maintenu constant à 380 A par des rhéostats. La tension aux bornes d'un moteur est $U_{moteur} = k_2 \cdot V^2$ avec $k_2 = 0{,}1$ V·s·m$^{-1}$, où $V$ est la vitesse du train. La résistance des bobinages est négligée. Donner l'expression du courant d'induit en fonction de $V_{alim}$, $V$, $k_2$ et $R_{th}$ (résistance totale des rhéostats). En déduire la loi de commande des rhéostats.

*Corrigé complet :*
- 4 moteurs en série : $U_{alim} = 4 \cdot U_{moteur} + V_{alim,rheostat}$ mais en simplifiant avec $R_a \approx 0$, la tension aux bornes d'un moteur est $U_{moteur} = k_2 \cdot V^2$.
- Courant d'induit : $I = \frac{V_{alim} - 4 k_2 V^2}{R_{th}}$
- Pour maintenir $I = 380$ A constant : $R_{th}(V) = \frac{V_{alim} - 4k_2 V^2}{380} = \frac{750 - 4 \times 0{,}1 \times V^2}{380}$
- La résistance des rhéostats diminue à mesure que le train accélère (la FCEM augmente).

---

**Q2 — Source : CAPET 2019, E2, Question 8**

*Énoncé complet :* Donner l'expression de la puissance instantanée $p(t)$ dissipée par les rhéostats lors d'une phase de démarrage à courant constant 380 A.

*Corrigé complet :*
- $p(t) = R_{th}(t) \cdot I^2 = (V_{alim} - 4k_2 V^2) \cdot I = (750 - 4 \times 0{,}1 \times V^2) \times 380$
- Avec $V(t) = \gamma \cdot t$ et $\gamma = 0{,}2$ m·s$^{-2}$ : $p(t) = (750 - 0{,}4 \times (0{,}2t)^2) \times 380$
- Cette puissance est dissipée par effet Joule dans les rhéostats (énergie perdue lors du démarrage rhéostatique).

---

**Q3 — Source : CAPET 2019, E2, Question 28**

*Énoncé complet :* Les moteurs Alsthom à courant continu ont les caractéristiques : tension nominale 360 V, courant nominal 305 A, puissance nominale 96 kW, vitesse nominale 1035 tr·min$^{-1}$. Calculer le couple nominal. Conclure sur la possibilité d'utiliser ces moteurs pour tracter la rame VMI.

*Corrigé complet :*
- $\Omega_{nom} = 1035 \times \frac{2\pi}{60} = 108{,}4$ rad·s$^{-1}$
- $C_{nom} = \frac{P_{nom}}{\Omega_{nom}} = \frac{96000}{108{,}4} = 885{,}6$ N·m
- Le couple thermique équivalent calculé sur le trajet est $C_{th} \approx 595$ N·m < $C_{nom}$ → les moteurs sont **correctement dimensionnés**.

---

**Q4 — Source : CAPET 2022, E2 appliquée (Banc d'essai automobile), Questions 35–37**

*Énoncé complet :* Le frein à courant de Foucault est alimenté par un hacheur. La tension en entrée du filtre est $E = 207$ V constante. Exprimer la valeur moyenne $\langle u_f(t) \rangle$ en sortie du hacheur en fonction de $E$ et du rapport cyclique $\alpha$. Calculer $\alpha$ pour le point de fonctionnement nominal ($\langle u_f \rangle = 192$ V). Conclure sur le contrôle du couple.

*Corrigé complet :*
- Hacheur série : $\langle u_f \rangle = \alpha \cdot E = \alpha \times 207$
- $\alpha = 192/207 = 0{,}927$
- Le hacheur permet de couvrir toute la plage de tension jusqu'à la valeur nominale, ce qui permet de contrôler précisément le courant dans le frein et donc le couple appliqué au véhicule.
- Hacheur 4Q (réversible) : $\langle u_f \rangle = E(2\alpha - 1) \Rightarrow \alpha = \frac{1}{2}\left(\frac{192}{207} + 1\right) = 0{,}963$

---

**Q5 — Source : CAPET 2022, E2 appliquée, Question 30**

*Énoncé complet :* Justifier la structure du hacheur utilisé (figure 18) pour alimenter le frein à courant de Foucault.

*Corrigé complet :*
- Pour faire varier le couple du frein, il faut faire varier le courant d'alimentation.
- Pour démagnétiser le frein, il faut inverser le courant. Il faut donc inverser la tension d'alimentation.
- Il faut un hacheur réversible en tension et en courant : **hacheur 4 quadrants** (H-bridge), permettant de piloter des charges inductives avec inversion de courant.

---

**Q6 — Source : CAPET 2019, E2, Questions 25–27 (corrigé Q28)**

*Énoncé complet :* Après calcul, le couple thermique équivalent sur le cycle de fonctionnement de la rame est donné par $C_{th}^2 = \frac{\sum_{i=1}^{18} C_{mi}^2 \cdot \Delta t_i}{T}$ avec $\sum_{i=3}^{18} C_{mi}^2 \Delta t_i = 558 \times 10^6$ N²·m²·s, $T = 2048$ s. Calculer $C_{th}$ et conclure.

*Corrigé complet :*
- $C_{m1} = 1122$ N·m, $\Delta t_1 = 42$ s ; $C_{m2} = 693$ N·m, $\Delta t_2 = 51$ s
- $C_{th}^2 = \frac{1122^2 \times 42 + 693^2 \times 51 + 558 \times 10^6}{2048} = \frac{52895364 + 24470523 + 558000000}{2048} = \frac{635365887}{2048} = 310233$ N²·m²
- $C_{th} = \sqrt{310233} \approx 557$ N·m < $C_{nom} = 885{,}6$ N·m → **moteurs adaptés**.

---

## 3. ATTENTES DU JURY

**Source : Rapport jury 2022, commentaires E2 appliquée**

> « Le jury apprécie les candidats qui maîtrisent le bilan de puissance de la machine à courant continu et qui distinguent clairement la puissance électrique absorbée, les pertes Joule, et la puissance mécanique disponible. »

*Implication* : Connaître par cœur les 3 niveaux du bilan de puissance : $P_{abs} = P_{joules} + P_{meca}$.

**Source : Rapport jury 2023, commentaires**

> Le jury signale que les candidats oublient souvent de justifier le choix du type de convertisseur (hacheur 1Q, 2Q ou 4Q) et se contentent de calculer le rapport cyclique sans argumenter sur la nécessité de la réversibilité.

*Implication* : Toujours justifier le choix du hacheur par l'analyse des quadrants de fonctionnement.

**Source : Rapport jury 2024, commentaires généraux**

> « Le jury regrette le manque de maîtrise des formules de base sur les relations d'électrocinétique. »

*Implication* : Savoir écrire sans hésitation $U = E + R_a I_a$ (convention moteur) ou $U = E - R_a I_a$ (convention générateur). Bien distinguer les deux conventions.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique | Source |
|---|---|---|
| Tension nominale moteur rame MF67 | 360 V | 2019 E2 |
| Courant nominal | 305 A | 2019 E2 |
| Puissance nominale | 96 kW | 2019 E2 |
| Vitesse nominale | 1035 tr·min$^{-1}$ | 2019 E2 |
| Couple nominal calculé | ≈ 886 N·m | 2019 E2 |
| Tension bus continu (rame 750 V DC) | 750 V | 2019 E2 |
| Tension bus continu Urbanloop | 72 V | 2024 E2 appl. |
| Courant de démarrage rhéostatique | 380 A | 2019 E2 |
| Tension filtre hacheur (banc auto) | 207 V | 2022 E2 appl. |
| Rapport cyclique nominal (banc auto) | $\alpha = 0{,}963$ | 2022 E2 appl. corrigé |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Convention moteur vs générateur** : en moteur, $U > E$ et $U = E + R_a I_a$. En générateur, $E > U$ et $E = U + R_a I_a$. La confusion est sanctionnée.

2. **Oubli du régime transitoire** : au démarrage, $E = 0$ donc le courant est $I_a = U/R_a$, ce qui est très élevé. C'est pourquoi on insère des rhéostats ou on utilise un hacheur.

3. **Confondre couple électromagnétique et couple utile** : $C_{em} = k\phi I_a$ est le couple développé par la force de Laplace ; le couple utile est $C_u = C_{em} - C_{pertes}$ (pertes mécaniques et frottements).

4. **Ne pas vérifier les unités du gain $k\phi$** : $[k\phi] = $ V·s·rad$^{-1}$ = N·m·A$^{-1}$. Ce même coefficient est utilisé dans les deux équations (FCEM et couple).

5. **Démarrage rhéostatique = énergie perdue** : toute l'énergie dissipée dans les rhéostats l'est par effet Joule. C'est un point fréquemment traité dans les sujets (calcul de l'énergie perdue).

6. **Hacheur 4Q nécessaire pour freinage récupératif** : un hacheur 1Q (rapport cyclique $0 \leq \alpha \leq 1$, tension toujours positive) ne permet pas la réversibilité. Le hacheur 4Q est indispensable si le couple ou la vitesse doivent changer de signe.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

| Thème connexe | Articulation |
|---|---|
| **T10 Mécanique** | Le couple moteur $C_m$ issu du dimensionnement mécanique (réducteur, inertie) définit le courant d'induit nécessaire via $I_a = C_{em}/(k\phi)$ |
| **T02 Puissance AC** | Le redresseur AC/DC fournit la tension continue $E_{dc}$ au hacheur ; les harmoniques de courant impactent le réseau |
| **T13 MAS** | Comparaison des deux machines : la MCC offre un meilleur contrôle du couple au démarrage mais nécessite entretien (balais/collecteur) ; la MAS est plus robuste |
| **Asservissements** | La MCC est le moteur historique des asservissements de vitesse et de position grâce à la relation linéaire $C_{em} = k\phi I_a$ |
| **Convertisseurs (hacheurs)** | La commande de la MCC par hacheur (MLI) est centrale dans les sujets depuis 2019 |
