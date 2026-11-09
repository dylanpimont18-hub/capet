# T12 — Machine synchrone et brushless (PMSM / BLDC)
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

| Formule LaTeX | Contexte | Fréquence | Source |
|---|---|---|---|
| $\omega_m = \frac{2\pi f}{p}$ | Vitesse angulaire mécanique en fonction de la fréquence d'alimentation $f$ et du nombre de paires de pôles $p$ | Très fréquent | 2024 E2 appl. (Urbanloop) |
| $N_s = \frac{60 f}{p}$ | Vitesse de synchronisme en tr·min$^{-1}$ | Très fréquent | 2023 Rapport jury |
| $f_0 = p \cdot \frac{\omega_{m0}}{2\pi}$ | Fréquence d'alimentation pour atteindre une vitesse donnée | Fréquent | 2024 E2 appl. (Q45 : $f_0 = 185{,}6$ Hz) |
| $V_{composée} = \sqrt{3} \cdot V_{simple}$ | Relation entre tension composée et tension simple pour un couplage étoile | Très fréquent | 2024 E2 appl. |
| $\vec{V}_s = R_s \vec{I}_s + jX_s \vec{I}_s + \vec{E}$ | Équation électrique de la machine synchrone par phase (circuit équivalent) | Fréquent | général |
| $X_s = L_s \cdot \omega$ | Réactance synchrone | Fréquent | général |
| $P_{em} = 3 \frac{V_s E}{X_s} \sin\delta$ | Puissance électromagnétique en fonction de l'angle de charge $\delta$ | Fréquent | général |
| $C_{em} = \frac{P_{em}}{\Omega}$ | Couple électromagnétique de la machine synchrone | Fréquent | général |
| $P_{max} = 3 \frac{V_s E}{X_s}$ | Puissance maximale (angle de charge $\delta = 90°$) | Fréquent | général |
| $E = k \cdot \phi \cdot \Omega$ | Force électromotrice des aimants permanents (PMSM/BLDC) | Très fréquent | 2024 E2 appl. |
| $C_{em,PMSM} = k \cdot \phi \cdot I_q$ | Couple d'une PMSM (contrôle vectoriel, composante $I_q$) | Présent | général |

**Couplage étoile ou triangle :**
- **Étoile** : chaque enroulement supporte la tension simple $V_{simple} = V_{composée}/\sqrt{3}$
- **Triangle** : chaque enroulement supporte la tension composée $V_{composée}$
- Choix du couplage imposé par la tension nominale de l'enroulement vs la tension disponible sur le bus DC/onduleur.

**Servomoteur brushless (BLDC / PMSM) :**
- Rotor à aimants permanents → pas d'entretien des balais
- Stator triphasé alimenté par un onduleur commandé (capteurs de position : résolveur, encodeur ou capteurs Hall)
- La commutation est électronique (pas mécanique) → pas de collecteur
- **Différence servomoteur / moteur** : un servomoteur inclut une boucle de retour (capteur) et peut être asservi en position, vitesse ou couple avec précision.

**Diagramme de Kapp (machine synchrone) :**
- Diagramme vectoriel des tensions pour déterminer la FEM $E$ et l'angle de charge $\delta$
- $\vec{V}_s = \vec{E} + R_s \vec{I}_s + jX_s \vec{I}_s$
- Pour un moteur à facteur de puissance unitaire ($\vec{I}_s$ en phase avec $\vec{V}_s$) : $E = \sqrt{V_s^2 + (X_s I_s)^2}$ (effet démagnetisant nul)

**Autopilotage (PMSM)** :
- La fréquence de l'onduleur est asservie à la position du rotor (capteur Hall ou résolveur)
- La vitesse mécanique $\Omega$ est directement liée à la fréquence des courants statoriques
- Avantage : pas de décrochage possible contrairement à la machine synchrone classique

### 1.1 Moteur pas à pas

*(complément du référentiel, 2026-11-10 — notion hors sujets 2013–2026 sauf mention)*

**Pas angulaire d'un moteur pas à pas :**
$$\theta_p = \frac{360^\circ}{N_{pas}}$$

**Nombre de pas par tour d'un moteur à aimant en pas entier :**
$$N_{pas} = 2 \, p \, m$$
- Valable en pas entier, avec m phases et p paires de pôles au rotor

**Vitesse de rotation d'un moteur pas à pas :**
$$N = \frac{60 \, f_{imp}}{N_{pas}}$$
- Valable uniquement tant que le moteur ne décroche pas (aucun pas perdu)

---

## 2. QUESTIONS TYPES

**Q1 — Source : CAPET 2024, E2 appliquée (Urbanloop), Questions 44–46**

*Énoncé complet :* La capsule Urbanloop est motorisée par quatre machines synchrones triphasées à aimants permanents de 28 pôles, chacune entraînant directement une roue. La fréquence d'alimentation $f$ est variable. La relation est $\omega_m = 2\pi f / p$ avec $p$ le nombre de paires de pôles. La vitesse maximale est $V_0 = 60$ km·h$^{-1}$, le rayon de la roue est $R_{roue} = 0{,}20$ m. Les onduleurs délivrent une tension composée de 72 V efficace. Déterminer la fréquence d'alimentation $f_0$ pour atteindre $V_0$. Indiquer le couplage du stator.

*Corrigé complet :*
- $V_0 = 60$ km·h$^{-1}$ = $60000/3600 = 16{,}67$ m·s$^{-1}$
- Vitesse angulaire de la roue : $\omega_{roue} = V_0 / R_{roue} = 16{,}67 / 0{,}20 = 83{,}3$ rad·s$^{-1}$
- Nombre de paires de pôles : $p = 28/2 = 14$
- Fréquence : $f_0 = p \cdot \omega_{roue} / (2\pi) = 14 \times 83{,}3 / (2\pi) = 185{,}6$ Hz
- Couplage : tension nominale d'un enroulement = ? La tension composée est 72 V. En étoile, la tension par enroulement = $72/\sqrt{3} \approx 41{,}6$ V. En triangle, chaque enroulement supporte 72 V composée. La documentation indique que chaque enroulement supporte 72 V → **couplage triangle**.

---

**Q2 — Source : CAPET 2025, E2 appliquée (Scène robotisée KUKA), Question 18**

*Énoncé complet :* Les robots KUKA KR QUANTEC sont munis de servomoteurs brushless. Rappeler la définition d'un servomoteur en précisant la différence avec un moteur.

*Corrigé complet :*
- Un **moteur** convertit une énergie électrique en énergie mécanique sans retour d'information sur sa position ou vitesse.
- Un **servomoteur** est un moteur associé à un capteur de position (encodeur, résolveur, capteur Hall) et à une boucle d'asservissement. Il peut être commandé précisément en position, vitesse ou couple.
- La différence fondamentale est la présence de la boucle fermée qui garantit la précision du positionnement.
- Les servomoteurs brushless (PMSM/BLDC) utilisent des aimants permanents au rotor : pas de collecteur ni de balais → entretien réduit, durée de vie plus longue, densité de puissance élevée.

---

**Q3 — Source : CAPET 2023, E2 disciplinaire (Robot Bakus), Figure 5**

*Énoncé complet :* La chaîne de puissance du robot Bakus utilise un moteur synchrone avec réducteur et convertisseur statique. Les rendements sont $\eta_{CS}$, $\eta_{MS}$ et $\eta_{réd}$. La puissance mécanique nécessaire au mouvement est $P_{meca}$. Exprimer la puissance électrique $P_{elec}$ fournie par les batteries.

*Corrigé complet :*
- $P_{elec} = \frac{P_{meca}}{\eta_{CS} \cdot \eta_{MS} \cdot \eta_{réd}}$
- Le rendement global de la chaîne de puissance est le produit des rendements de chaque élément.
- Valeur numérique donnée dans le sujet : $\eta_{global} = 63\%$ → $P_{elec} = P_{meca} / 0{,}63$

---

**Q4 — Source : CAPET 2023, Rapport jury, Questions 18–20 (machine asynchrone serre)**

*Énoncé complet (adapté aux machines synchrones)* : Connaissant la vitesse nominale $N_{nom} = 950$ tr·min$^{-1}$ et la fréquence réseau $f = 50$ Hz, déterminer le nombre de paires de pôles $p$ et la vitesse de synchronisme $N_s$.

*Corrigé complet :*
- En supposant le glissement faible, $N_{nom} \approx N_s = 60f/p$
- $p \approx 60 \times 50 / 950 = 3{,}16$ → $p = 3$ (entier)
- $N_s = 60 \times 50 / 3 = 1000$ tr·min$^{-1}$
- Glissement réel : $g = (N_s - N_{nom})/N_s = (1000 - 950)/1000 = 0{,}05 = 5\%$

*(Note : cette question concerne techniquement la MAS, mais la détermination du nombre de paires de pôles à partir de la vitesse est commune aux deux types de machines.)*

---

**Q5 — Source : CAPET 2024, E2 appliquée, Questions 48–49**

*Énoncé complet :* La structure du boîtier d'alimentation Urbanloop comprend un pont redresseur PD2. Indiquer les réversibilités (tension/courant) des boîtiers d'alimentation. Conclure sur les risques.

*Corrigé complet :*
- Un pont PD2 (pont de Graëtz tout diodes) est **réversible en tension** (côté alternatif) mais **non réversible en courant** (le courant ne peut que circuler dans un sens côté continu).
- Lors du freinage récupératif, la machine synchrone fonctionne en générateur et tente de renvoyer de l'énergie sur le bus continu.
- Risque : le pont PD2 ne peut pas absorber ce courant → sur-tension sur le bus continu pouvant endommager les composants.
- Solution : ajouter un hacheur élévateur ou des supercondensateurs embarqués pour absorber l'énergie de freinage (solution retenue dans le sujet 2024).

---

**Q6 — Source : Cours général (diagramme de Kapp)**

*Énoncé complet :* Une machine synchrone triphasée à rotor bobiné alimente une charge inductive. En convention moteur, les données sont : $V_s = 230$ V (tension simple efficace), $I_s = 100$ A, $\cos\varphi = 0{,}85$ inductif, $X_s = 2$ Ω, $R_s \approx 0$. Calculer la FEM $E$ et l'angle de charge $\delta$.

*Corrigé complet :*
- $\varphi = \arccos(0{,}85) = 31{,}8°$ (courant en retard sur la tension)
- $\vec{E} = \vec{V}_s - jX_s \vec{I}_s$ (convention moteur avec $R_s = 0$)
- Composantes : $E_x = V_s - X_s I_s \sin\varphi = 230 - 2 \times 100 \times 0{,}529 = 230 - 105{,}8 = 124{,}2$ V
- $E_y = -X_s I_s \cos\varphi = -2 \times 100 \times 0{,}850 = -170$ V (retard du rotor)
- $E = \sqrt{124{,}2^2 + 170^2} = \sqrt{15426 + 28900} = \sqrt{44326} = 210{,}5$ V
- $\delta = \arctan(170/124{,}2) = 53{,}9°$

---

## 3. ATTENTES DU JURY

**Source : Rapport jury 2024, commentaires E2 Appliquée (Urbanloop)**

> « La partie portant sur l'étude de la machine synchrone (partie 3.3) a été globalement bien traitée par les candidats qui ont su appliquer la relation entre fréquence d'alimentation et vitesse de rotation. »

*Implication* : Maîtriser la relation $\omega_m = 2\pi f/p$ et savoir effectuer les conversions rad·s$^{-1}$ ↔ tr·min$^{-1}$.

**Source : Rapport jury 2025, commentaires E2 Appliquée (Scène KUKA)**

> « Le jury regrette que certains candidats confondent servomoteur et moteur classique, et ne précisent pas la nature de la boucle de retour ni son rôle dans la précision du positionnement. »

*Implication* : Toujours mentionner le capteur (résolveur, encodeur) et la boucle fermée lorsqu'on décrit un servomoteur.

**Source : Rapport jury 2022 (général)**

> « Les candidats doivent connaître les avantages des moteurs brushless (absence de collecteur, durée de vie, entretien) par rapport aux MCC. »

*Implication* : Être capable de comparer MCC, PMSM/BLDC sur les critères : entretien, densité de puissance, réversibilité, coût.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique | Source |
|---|---|---|
| Nombre de paires de pôles Urbanloop | $p = 14$ (28 pôles) | 2024 E2 appl. |
| Fréquence alimentation Urbanloop à 60 km·h$^{-1}$ | $f_0 = 185{,}6$ Hz | 2024 E2 appl. |
| Tension composée onduleur Urbanloop | 72 V | 2024 E2 appl. |
| Vitesse de synchronisme (serre ventilation) | 1000 tr·min$^{-1}$ ($p=3$, $f=50$ Hz) | 2023 Rapport |
| Rapport de réduction robot Bakus (couplage MS) | Rendement global chaîne 63% | 2023 E2 disc. |
| Rapport de réduction robot KUKA axe 6 | $r = 0{,}00607$ | 2025 E2 appl. |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Confusion entre nombre de pôles et nombre de paires de pôles** : $p$ désigne les paires de pôles. Une machine à 28 pôles a $p = 14$. La fréquence est $f = p \cdot n / 60$ (avec $n$ en tr·min$^{-1}$).

2. **Couplage étoile/triangle mal déterminé** : comparer systématiquement la tension nominale d'un enroulement (donnée constructeur) avec la tension composée disponible pour décider étoile ou triangle.

3. **Décrochage de la machine synchrone** : à vitesse fixe (réseau), le couple max est $C_{max} = 3V_s E / (X_s \Omega)$. Si le couple résistant dépasse cette valeur, la machine décroche. En autopilotage, ce risque est éliminé.

4. **Angle de charge et signe** : en moteur, $\delta > 0$ (rotor en avance sur le champ tournant) ; en générateur, $\delta < 0$. L'oubli du signe conduit à des erreurs dans le diagramme de Kapp.

5. **La PMSM n'a pas de résistance rotorique** : contrairement à la MAS, la PMSM à aimants permanents n'a pas de pertes Joule au rotor (pas de courants rotoriques) → meilleur rendement.

6. **Capteurs Hall** : utilisés dans les BLDC pour détecter la position du rotor à 6 positions par tour. Ne pas confondre avec un encodeur haute résolution (utilisé dans les servomoteurs de précision).

7. **Boucle ouverte du moteur pas à pas** : supposer que la position commandée est toujours atteinte. Le moteur pas à pas n'a pas de capteur : un pas perdu (surcharge, accélération trop brutale) n'est jamais détecté, contrairement à un servomoteur.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

| Thème connexe | Articulation |
|---|---|
| **T10 Mécanique** | L'inertie de la charge et le réducteur conditionnent les performances dynamiques de l'asservissement de la MS ; le couple utile nécessaire vient de l'analyse mécanique |
| **T13 MAS** | Comparaison machine synchrone / asynchrone : la MS a un rendement supérieur et une vitesse parfaitement contrôlable via la fréquence ; la MAS est moins chère |
| **T02 Puissance AC** | L'onduleur qui alimente la MS génère des harmoniques ; le facteur de puissance de la MS peut être ajusté par l'excitation (aimants permanents : cos φ ≈ 1) |
| **Asservissements** | La MS en autopilotage est le moteur des asservissements modernes (servo-drive) ; le réglage de la boucle de vitesse fait appel aux diagrammes de Bode |
| **Convertisseurs** | L'onduleur de tension triphasé (MLI) est indispensable pour la commande en fréquence variable de la MS ; la récupération d'énergie au freinage nécessite un onduleur réversible |
