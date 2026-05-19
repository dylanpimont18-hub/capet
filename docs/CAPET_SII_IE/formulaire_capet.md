# Formulaire CAPET SII — Ingénierie Électrique

> **Sources :** Corrigés 2016–2021 · Rapports jury 2019–2025 · Sujets 2015–2025
>
> **Légende colonne "Donnée ?"**
> - ✅ **Oui** — fournie dans le sujet (données, rappels, documents techniques)
> - ❌ **Non** — à connaître et restituer de mémoire
>
> **Colonne "Fréq."** : nombre de sujets/corrigés/rapports jury où la formule est mobilisée.

---

## Vue d'ensemble — Top formules (fréquence ≥ 3)

| Formule | Domaine | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $E = P \cdot t$ | Énergétique | ❌ | **7** |
| $P = C \cdot \omega_m$ | Machines | ❌ | **6** |
| $P = \sqrt{3}\,U I \cos\varphi$ | Électrotechnique — triphasé | ❌ | **6** |
| $S = \sqrt{P^2 + Q^2}$ | Puissance apparente | ❌ | **5** |
| $\eta_{global} = \prod_i \eta_i$ | Énergétique | ❌ | **5** |
| $\omega = 2\pi N/60$ | Cinématique | ❌ | **5** |
| $\sigma_{max} = M_{fz}\,y_{max}/I_{Gz}$ | RDM — Flexion | ✅ (I donné) | **4** |
| $P = U \cdot I \cdot \cos\varphi$ | Électrotechnique — monophasé | ❌ | **4** |
| $\phi_t = -\Delta T / R_{th}$ | Thermique | ✅ | **4** |
| $COP = \|Q_1\|/W$ | Thermodynamique — PAC | ✅ | **3** |
| $COP_{max} = T_c/(T_c-T_f)$ | Thermodynamique — Carnot | ❌ | **3** |
| $V_{DC} = E_b/(1-\alpha)$ | Élec. puissance — Boost | ❌ | **3** |
| $I_n = P_u/(\eta\sqrt{3}\,U\cos\varphi)$ | Machines — MAS | ❌ | **3** |
| $N_s = 60f/p$ | Machines — MAS (vitesse synchrone) | ❌ | **3** |
| $g = (N_s-N)/N_s$ | Machines — MAS (glissement) | ❌ | **3** |
| $M_{fz,max} = qL^2/8$ | RDM | ❌ | **3** |
| $\Delta U = \rho\,(L/S)\,I$ | Câblage — chute de tension | ❌ | **3** |

---

## 1. Thermique — Conduction & Résistances thermiques

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $\phi_t = -\dfrac{\Delta T}{R_{th}}$ | Flux thermique — loi de Fourier | ✅ | 4 |
| $R_{th} = \dfrac{e}{\lambda \cdot S}$ | Résistance thermique d'une couche | ❌ | 3 |
| $\dfrac{1}{K} = \displaystyle\sum_i \dfrac{e_i}{\lambda_i} + R_{s,int} + R_{s,ext}$ | Coefficient de transmission global $K$ | ✅ | 2 |
| $\phi_{paroi} = K \cdot S \cdot \Delta T$ | Flux à travers une paroi opaque | ❌ | 2 |
| $\phi_{tot} = \left(\dfrac{\lambda_{eq} S_v}{e_{eq}} + \dfrac{\lambda_p S_p}{e_p}\right)\Delta T$ | Flux total (parois parallèles) | ❌ | 2 |
| $\lambda_{eq} = \dfrac{\sum e_i}{\sum e_i/\lambda_i}$ | Conductivité équivalente en série | ❌ | 2 |
| $P_s = \left(\dfrac{T_S}{100}\right)^4$ — $T_S = 100\sqrt[4]{P_s}$ | Rayonnement — loi de Stefan-Boltzmann | ❌ | 1 |

---

## 2. Thermique — Vapeur & Condensation

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $P_S = \exp\!\left(25{,}5 - \dfrac{5204{,}9}{T+273}\right)$ | Pression de vapeur saturante | ✅ | 1 |
| $P_V = HR \times P_S$ | Pression partielle de vapeur | ✅ | 1 |
| $g = -\Delta P / R_{vap}$ | Flux de vapeur — loi de Fick | ✅ | 1 |

---

## 3. Thermodynamique — Pompe à chaleur (PAC)

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $W + Q_1 + Q_2 = 0$ | Bilan énergétique sur un cycle PAC | ✅ | 1 |
| $\dfrac{Q_1}{T_c} + \dfrac{Q_2}{T_f} = 0$ | Bilan entropique — cycle réversible | ✅ | 1 |
| $COP = \dfrac{\|Q_1\|}{W}$ | COP de la pompe à chaleur | ✅ | 3 |
| $COP_{max} = \dfrac{T_c}{T_c - T_f}$ | COP théorique de Carnot | ❌ | 3 |
| $\phi = n \cdot \|Q_1\| = n \cdot W \cdot COP$ | Flux thermique fourni par la PAC | ❌ | 1 |
| $P_e = \phi\,/\,(COP \cdot r_g)$ | Puissance électrique du compresseur PAC | ❌ | 1 |
| $C_{spa} = c_{eau} \times m_{eau}$ | Capacité thermique massique | ❌ | 1 |

---

## 4. Énergies renouvelables & Stockage

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $P_{ann} = N_{panneaux} \cdot P_c \cdot E_{sol}$ | Production annuelle PV | ✅ | 2 |
| $S_{totale} = E_{TOT}\,/\,(\eta_{ligne}\,\eta_{mod}\,\eta_{pan}\,E_{an})$ | Surface PV nécessaire | ❌ | 1 |
| $E_p = m \cdot g \cdot h$ | Énergie potentielle gravitationnelle (STEP) | ❌ | 2 |
| $\eta_{st} = E_{élec,dispo}\,/\,E_{remplissage}$ | Rendement global stockage par pompage | ❌ | 1 |
| $V = nRT\,/\,P$ | Loi des gaz parfaits (stockage H₂) | ❌ | 1 |
| $\eta_{global} = E_{ER}\,/\,E_{EH}$ | Rendement global chaîne hydrogène | ❌ | 1 |
| $E_{UH} = E_u \cdot m_{H_2}\,/\,m_{mol}$ | Énergie utile de l'hydrogène | ❌ | 1 |
| $E_{EH} = E_{UH}\,/\,\eta_E$ | Énergie électrique pour produire H₂ | ❌ | 1 |
| $t = V / Q_{pompe}$ | Durée de remplissage réservoir | ❌ | 1 |

---

## 5. Électrotechnique — Puissance & Réseaux

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $P = U \cdot I$ | Puissance (continu) | ❌ | 4 |
| $P = U \cdot I \cdot \cos\varphi$ | Puissance active (AC monophasé) | ❌ | 4 |
| $P = \sqrt{3}\,U\,I\,\cos\varphi$ | Puissance active (AC triphasé) | ❌ | 6 |
| $Q = P \cdot \tan\varphi$ | Puissance réactive | ❌ | 4 |
| $S = \sqrt{P^2 + Q^2}$ | Puissance apparente | ❌ | 5 |
| $\cos\varphi = P\,/\,S$ | Facteur de puissance | ❌ | 4 |
| $THD = \sqrt{\sum_{n \geq 2} I_n^2}\,/\,I_1$ | Taux de distorsion harmonique | ❌ | 2 |
| $C = Q_{abs}\,/\,(3\,\omega\,V_p^2)$ | Condensateur de compensation réactive | ❌ | 2 |
| $E = \tfrac{1}{2}\,C\,(V_{max}^2 - V_{min}^2)$ | Énergie stockée — condensateur / supercap | ❌ | 2 |
| $E = P \cdot t$ | Énergie = Puissance × Durée | ❌ | 7 |
| $\eta_{global} = \prod_i \eta_i$ | Rendement global en cascade | ❌ | 5 |
| $R = U^2\,/\,P$ | Résistance par dissipation de puissance | ❌ | 1 |
| $C_{coût} = E_{HP}\,T_{HP} + E_{HC}\,T_{HC}$ | Coût facture électricité HP/HC | ✅ (tarifs donnés) | 2 |

---

## 6. Câblage & Distribution

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $\Delta U = \rho\,(L/S)\,I$ | Chute de tension en ligne | ❌ | 3 |
| $I = P\,/\,(\eta\,U\,\cos\varphi)$ | Courant absorbé (moteur AC) | ❌ | 2 |
| $C_b = E_{nécessaire}\,/\,U_{bat}$ | Capacité batterie (A·h) | ❌ | 2 |
| $P_T = P_{charge} + 3\,R_L\,I^2$ | Puissance active totale (avec pertes ligne) | ❌ | 1 |
| $Q_T = 3\,L_L\,\omega\,I^2$ | Puissance réactive totale (avec inductance ligne) | ❌ | 1 |
| $\Delta U\,\% = (U_D - U_r)\,/\,U_D \times 100$ | Taux de chute de tension | ❌ | 2 |
| $L_{max} = 0{,}1\,U_0\,/\,(R_\ell\,I_{moy})$ | Longueur limite de câble | ❌ | 1 |
| $R_{eq} = 2\,R_\ell\,L\,(1-x/L)\,(x/L)$ | Résistance équivalente câble à prise intermédiaire | ❌ | 1 |

---

## 7. Électronique de puissance — Hacheurs

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $V_{DC} = E_b\,/\,(1-\alpha)$ | Tension de sortie — Hacheur Boost | ❌ | 3 |
| $\alpha = 1 - E_b\,/\,V_{DC}$ | Rapport cyclique — Hacheur Boost | ❌ | 3 |
| $E_b = L\,di_L/dt$ | Équation bobine (phase passante) | ❌ | 2 |
| $I_{S,moy} = I_b\,(1-\alpha)$ | Courant moyen de sortie Boost | ❌ | 2 |
| $P_E = V_b\,I_b = V_{DC}\,I_S$ | Conservation de puissance — convertisseur | ❌ | 2 |
| $R_0 = V_{DC}^2\,/\,P_{S0}$ | Résistance de charge équivalente | ❌ | 1 |
| $\langle u_f \rangle = E\,(2\alpha-1)$ | Tension moyenne — pont en H | ❌ | 2 |
| $L = (1-\alpha)\,\alpha\,T\,E\,/\,\Delta i_L$ | Inductance minimale hacheur (ondulation) | ❌ | 1 |
| $\langle U_{Li} \rangle = \alpha \cdot E_{LiFePo4}$ | Tension moyenne sortie (Buck) | ❌ | 1 |
| $H_{boost}(p) = \dfrac{\frac{E_{b0}}{(1-\alpha_0)^2}\!\left(1-\frac{L}{R_0(1-\alpha_0)^2}p\right)}{1+\frac{L}{R_0(1-\alpha_0)^2}p+\frac{LC}{(1-\alpha_0)^2}p^2}$ | Fonction de transfert petit signal Boost | ❌ | 1 |

---

## 8. Machines électriques — MAS (Asynchrone)

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $N_s = 60\,f\,/\,p$ | Vitesse synchrone (tr/min) | ❌ | 3 |
| $g = (N_s - N)\,/\,N_s$ | Glissement | ❌ | 3 |
| $I_n = P_u\,/\,(\eta\,\sqrt{3}\,U\,\cos\varphi)$ | Courant nominal MAS triphasée | ❌ | 3 |
| $I_r' = V_s\,/\,\sqrt{(L_f\omega_s)^2 + (R_r'/g)^2}$ | Courant rotor (modèle équivalent) | ❌ | 1 |
| $C_{em} = \dfrac{3p}{R'_r}\left(\dfrac{V_s}{\omega_s}\right)^2(\omega_s - \omega)$ | Couple électromagnétique MAS | ❌ | 1 |
| $P_a = 3\,V_s\,I_s\,\cos\varphi$ | Puissance absorbée | ❌ | 2 |
| $P_{jr} = 3\,R'_r\,{I'_r}^2$ | Pertes Joule rotor | ❌ | 1 |
| $Q_0 = 3\,V^2\,/\,(L_p\,\omega)$ | Puissance réactive de magnétisation | ❌ | 1 |
| $C_{th} = \sqrt{\tfrac{1}{T}\sum_k C_k^2 t_k}$ | Couple thermique équivalent | ❌ | 1 |

---

## 9. Machines électriques — Généralités

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $P = C \cdot \omega_m$ | Puissance mécanique | ❌ | 6 |
| $C_{nom} = P_{nom}\,/\,\Omega_{nom}$ | Couple nominal | ❌ | 3 |
| $\omega = 2\pi\,N\,/\,60$ | Conversion tr/min → rad/s | ❌ | 5 |
| $\eta = C_e\,\rho\,/\,C_m$ | Rendement réducteur | ❌ | 2 |

---

## 10. Automatique & Asservissement

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $K = y_{sortie}\,/\,u_0$ | Gain statique (système ordre 1) | ❌ | 2 |
| $FTBO(p) = \dfrac{K_{PV}\,K_M\,K_{GT}}{(1+p/\omega_A)(1+p/\omega_B)}$ | Fonction de transfert BO (exemple 2 pôles) | ❌ | 1 |
| $\omega_0 = \sqrt{\tau\,/\,(K_p\,K_i\,K_{mec})}$ | Pulsation naturelle boucle fermée | ❌ | 1 |
| $K_p = (2\,m\,\tau_{mec}\,\omega_0 - 1)\,/\,K_{mec}$ | Gain proportionnel PI (synthèse) | ❌ | 1 |
| $K_i = \tau_{mec}\,\omega_0^2\,/\,(K_p\,K_{mec})$ | Gain intégral PI (synthèse) | ❌ | 1 |
| $\varepsilon_s = \lim_{p\to 0}\,p\,\varepsilon(p) = 0$ | Erreur statique nulle (correcteur I) | ❌ | 2 |

---

## 11. Capteurs & Mesure

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $\Delta U \approx V_{cc}\,\Delta R\,/\,(4\,R_0)$ | Pont de Wheatstone déséquilibré | ❌ | 2 |
| $R(F) = R_0 + K_R \cdot F$ | Jauge de contrainte | ❌ | 1 |
| $q = (V_{REF+} - V_{REF-})\,/\,(2^n - 1)$ | Pas de quantification CAN ($n$ bits) | ❌ | 2 |
| $K_{cod} = 2\pi\,R_{poulie}\,/\,N_{incr}$ | Résolution codeur incrémental | ❌ | 1 |
| $T_{bit} = 1\,/\,F_{baud}$ | Durée d'un bit — liaison série | ❌ | 1 |
| $R_b = SF \cdot BW \cdot CR\,/\,2^{SF}$ | Débit utile LoRa | ❌ | 1 |
| $T_{trans} = n_{bits}\,/\,débit$ | Temps de transmission d'une trame | ❌ | 1 |

---

## 12. Mécanique — Cinématique & Dynamique

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $V_t = R\,\omega_r = R\,\omega_m\,/\,N$ | Cinématique roulement sans glissement | ✅ | 3 |
| $V(t) = \gamma\,t$ — $x(t) = \gamma\,t^2/2$ | MRUA (accélération constante) | ❌ | 3 |
| $x_{arr} = -V_0^2\,/\,(2\Gamma)$ | Distance d'arrêt — freinage | ❌ | 2 |
| $D_{min} = V_0\,t_r - V_0^2\,/\,(2\,a_0)$ | Distance de freinage avec temps de réaction | ❌ | 1 |
| $P_{pente} = -M\,g\,V_t\,\sin\alpha$ | Puissance pesanteur en pente | ✅ | 1 |
| $P_{av} = -(A\,V + B\,V^2 + C\,V^3)$ | Puissance résistance à l'avancement | ✅ | 1 |
| $P_{moy} = (C_{rr}\,Mg + F_{outils})\,V$ | Puissance motrice moyenne (engin) | ❌ | 1 |
| $a_X = (2T_{AV}+2T_{AR}-F_{out}-Mg\sin\theta)\,/\,M$ | Accélération — PFD (engin) | ❌ | 1 |

---

## 13. Mécanique — Statique & Équilibre

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $\sum \vec{F} = \vec{0}$ et $\sum \vec{M} = \vec{0}$ | Principe fondamental statique | ❌ | 5 |
| $Z_i = mg(1/2 + d/L)$, $Z_j = mg(1/2 - d/L)$ | Réactions — poutre bi-appuyée avec excentrage | ❌ | 2 |
| $N_c = \dfrac{c\sin\beta - d\cos\beta}{b}\,F_r$ | Effort normal — mécanisme | ❌ | 1 |
| $F_e = p\,g\,H_{max}\,S$ | Effort de poussée hydrostatique | ❌ | 1 |
| $P_{terre} = \tfrac{1}{2}\,K_s\,L\,\gamma_{sol}\,(h_2^2-h_1^2)$ | Poussée des terres (génie civil) | ❌ | 1 |

---

## 14. RDM — Résistance des matériaux

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $Y_A = Y_C = qL/2$ | Réactions — poutre bi-appuyée, charge uniforme | ❌ | 2 |
| $M_{fz,max} = qL^2/8$ | Moment fléchissant maximal (centre, bi-appuyée) | ❌ | 3 |
| $\sigma = N/S - M_{fz}\,y/I_{Gz}$ | Contrainte normale combinée (N + flexion) | ❌ | 2 |
| $\sigma_{max} = M_{fz,max}\,y_{max}\,/\,I_{Gz}$ | Contrainte normale maximale en flexion | ✅ (I donné) | 4 |
| $|\sigma_{max}| = 6\,F\,L\,\sin\alpha\,/\,(b\,h^2)$ | Contrainte max — poutre encastrée inclinée | ❌ | 1 |
| $f_{max} = 5\,q\,L^4\,/\,(384\,E\,I)$ | Flèche — poutre bi-appuyée, charge uniforme | ❌ | 1 |
| $f = F\,L^3\,/\,(3\,E\,I)$ | Flèche en bout — console sous force concentrée | ❌ | 2 |
| $f = q\,L^4\,/\,(8\,E\,I)$ | Flèche max — console sous charge répartie | ❌ | 1 |
| $E\,I\,y''(x) = M_{fz}(x)$ | Équation différentielle de la déformée | ❌ | 1 |
| $I = b\,h^3/12$ | Moment quadratique — section rectangulaire pleine | ❌ | 3 |
| $I = \pi\,D^4/64$ | Moment quadratique — section circulaire pleine | ❌ | 1 |
| $I = [b\,h^3-(b-2e)(h-2e)^3]/12$ | Moment quadratique — section tubulaire rectangulaire | ❌ | 2 |

---

## 15. Mécanique — Transmission & Friction

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $C_f = \tfrac{4}{3}\,f\,p_x\,[(R_i+h)^3-R_i^3]\,\alpha$ | Couple de friction (intégration sur surface) | ❌ | 1 |
| $F_{tmax} = 2\,\eta\,C_{max}\,/\,(d_p\,k_v\,k_p)$ | Force de traction maximale | ❌ | 1 |
| $F_{sangle} = 2\,T_{rouleau}\,/\,\cos(\arctan(a/b))$ | Force de sangle sur banc d'essai | ❌ | 1 |
| $pas_{opt} = 2\pi\sqrt{I_{vis}/m_{ch}}$ | Pas optimal — vis-écrou | ❌ | 1 |
| $C_m = \ddot{x}\left(\frac{2\pi}{pas}I_{vis} + m_{ch}\frac{pas}{2\pi}\right)$ | Couple moteur — système vis-écrou | ❌ | 1 |

---

## 16. Hydraulique & Fluides

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $Q = débit\,/\,section$ | Débit volumique | ❌ | 2 |
| $V_{pluie} = h_{pluie} \cdot S_{collecte}$ | Volume d'eau collecté | ❌ | 1 |
| $C = k\,\rho\,\omega\,h\,\tfrac{1}{3}(R_{ext}^3-R_{int}^3)$ | Couple résistant bras dans fluide (intégration) | ❌ | 1 |

---

## 17. Énergétique générale & Économique

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $\Delta E_C = -\tfrac{1}{2}\,m\,V^2$ | Énergie cinétique perdue au freinage | ❌ | 2 |
| $E_{dép} = F_{in}\,\gamma\,\Delta t^2\,/\,2$ | Énergie de déplacement (MRUA) | ❌ | 1 |
| $RI = C_{invest}\,/\,(Eco_{conso}+Eco_{abo})$ | Retour sur investissement (PAC) | ❌ | 1 |
| $Q_F = E_{TOT}\,/\,(\eta_{ligne}\,\eta_{GE}\,\eta_{GT}\,PCI)$ | Quantité de carburant nécessaire | ❌ | 1 |

---

---

## 18. Transformateurs

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $m = N_2/N_1 = U_2/U_1 = I_1/I_2$ | Rapport de transformation | ❌ | 4 |
| $U_2 = m \cdot U_1$ | Tension secondaire | ❌ | 4 |
| $I_1 = m \cdot I_2$ | Courant primaire en charge | ❌ | 3 |
| $Z'_2 = Z_2 / m^2$ | Impédance ramenée au primaire | ❌ | 2 |
| $\eta = P_{utile}/(P_{utile} + P_{Fe} + P_{Cu})$ | Rendement transformateur | ❌ | 2 |
| $P_{Cu} = R_{cc} \cdot I^2$ | Pertes cuivre (charge) | ❌ | 2 |
| $\Delta U \approx (P \cdot R_{cc} + Q \cdot X_{cc})/U_n$ | Chute de tension en charge | ❌ | 1 |

---

## 19. Redresseurs

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $V_{d0} = 0{,}90 \cdot V_{eff}$ | Tension moyenne — pont monophasé (PD2) | ❌ | 3 |
| $V_{d0} = 1{,}35 \cdot U_{composée}$ | Tension moyenne — pont triphasé (PD6) | ❌ | 3 |
| $V_{d0} = 0{,}45 \cdot V_{eff}$ | Tension moyenne — simple alternance (P1) | ❌ | 1 |
| $V_d = V_{d0} \cdot \cos\alpha$ | Tension avec thyristors (angle d'amorçage) | ❌ | 2 |
| $C = I_d / (f_r \cdot \Delta U)$ | Condensateur de filtrage | ❌ | 2 |
| $V_{eff} = V_{max}/\sqrt{2}$ | Valeur efficace d'une sinusoïde | ❌ | 4 |

---

## 20. Onduleurs & MLI

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $U_1 = m_a \cdot V_{dc}/\sqrt{2}$ | Tension fondamentale (pont monophasé MLI) | ❌ | 2 |
| $U_1 \approx 0{,}612 \cdot m_a \cdot V_{dc}$ | Tension simple fondamentale (onduleur triphasé) | ❌ | 2 |
| $m_a = V_{ref}/V_{porteuse}$ | Indice de modulation d'amplitude | ❌ | 2 |
| $m_f = f_s/f_{fondamental}$ | Indice de modulation de fréquence | ❌ | 1 |
| $THD = \sqrt{\sum_{n\geq2} U_n^2}/U_1 \times 100\%$ | Taux de distorsion harmonique | ❌ | 2 |
| $V_{dc} \geq \sqrt{2} \cdot U_{AC}/m_a$ | Tension bus DC minimale | ❌ | 2 |

---

## 21. Machine à courant continu (MCC)

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $E = K \cdot \Phi \cdot \Omega$ | Force électromotrice (fém) MCC | ❌ | 4 |
| $T_e = K \cdot \Phi \cdot I_a$ | Couple électromagnétique MCC | ❌ | 4 |
| $U = E + R_a \cdot I_a$ | Équation de la MCC (moteur) | ❌ | 4 |
| $\Omega = (U - R_a I_a)/(K\Phi)$ | Vitesse en fonction de la tension | ❌ | 3 |
| $P_{élmag} = E \cdot I_a = T_e \cdot \Omega$ | Puissance électromagnétique | ❌ | 3 |
| $I_{dém} = U/R_a$ | Courant de démarrage (E=0) | ❌ | 2 |
| $\eta = T_e \cdot \Omega / (U \cdot I_a)$ | Rendement MCC | ❌ | 2 |

---

## 22. Machine synchrone (MS)

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $n_s = 60f/p$ | Vitesse de synchronisme (tr/min) | ❌ | 4 |
| $E_0 = K \cdot \Phi \cdot \Omega_s$ | FEM à vide | ❌ | 3 |
| $P = 3 \cdot E_0 U \sin\delta / X_s$ | Puissance active (triphasé, par phase) | ❌ | 3 |
| $P_{max} = 3 E_0 U / X_s$ | Puissance maximale ($\delta = 90°$) | ❌ | 2 |
| $\vec{U} = \vec{E_0} - jX_s \vec{I}$ | Équation vectorielle MS (alternateur) | ❌ | 2 |
| $Q = (U/X_s)(E_0\cos\delta - U)$ | Puissance réactive | ❌ | 2 |
| $T_e = P/\Omega_s$ | Couple électromagnétique | ❌ | 2 |

---

## 23. MAS — Bilan de puissance

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $P_{J,rotor} = g \cdot P_{transmise}$ | Pertes Joule rotor | ❌ | 4 |
| $P_{méca} = (1-g) \cdot P_{transmise}$ | Puissance mécanique interne | ❌ | 4 |
| $n = n_s(1-g)$ | Vitesse réelle du rotor | ❌ | 3 |
| $T_{em} = P_{transmise}/\Omega_s$ | Couple électromagnétique MAS | ❌ | 3 |
| $\eta \approx 1-g$ | Rendement simplifié (sans pertes stator) | ❌ | 2 |

---

## 24. Stockage d'énergie

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $E_{Wh} = C_{Ah} \times U_{nom}$ | Énergie batterie (Wh) | ❌ | 3 |
| $E = \frac{1}{2}CU^2$ | Énergie supercondensateur | ❌ | 3 |
| $E = \frac{1}{2}J\Omega^2$ | Énergie volant d'inertie | ❌ | 2 |
| $SOC = Q_{restante}/Q_{nominale}$ | État de charge | ❌ | 2 |
| $t_{autonomie} = E_{Wh}/P$ | Autonomie à puissance constante | ❌ | 2 |
| $C_{Ah} = E_{Wh}/(U \cdot DOD)$ | Dimensionnement batterie avec profondeur de décharge | ❌ | 2 |

---

## 25. Énergies renouvelables — Éolien & Hydraulique

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $P = \frac{1}{2}\rho S v^3 C_p$ | Puissance éolienne | ❌ | 3 |
| $C_{p,max} = 0{,}593$ | Limite de Betz | ❌ | 2 |
| $P = \rho g Q H \eta$ | Puissance hydraulique (turbine / pompe) | ❌ | 3 |
| $P_{PV} = \eta \cdot S \cdot E_{irr}$ | Puissance d'un panneau PV | ❌ | 3 |
| $N_{panneaux} = E_{conso}/(P_{STC} \cdot E_{irr}/1000 \cdot \eta_{sys})$ | Nombre de panneaux PV | ❌ | 2 |

---

## 26. Sécurité électrique

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $U_L = 50\,V$ (AC sec) | Tension limite de contact | ❌ | 2 |
| $R_A \leq U_L / I_{dif}$ | Résistance de prise de terre max (schéma TT) | ❌ | 2 |
| $I_d = U_{phase}/Z_{boucle}$ | Courant de défaut (schéma TN) | ❌ | 2 |
| $I_{dif,n} \leq 30\,mA$ | Calibre différentiel — protection personnes | ❌ | 2 |

---

## 27. Éclairage

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $E = I \cos\theta / d^2$ | Éclairement (loi du cosinus) | ❌ | 2 |
| $\eta_{lum} = \Phi/P$ | Rendement lumineux (lm/W) | ❌ | 2 |
| $N = E_{req} \cdot A / (\Phi \cdot FU \cdot FM)$ | Nombre de luminaires | ❌ | 2 |
| $E = \Phi/A$ | Éclairement moyen (source étendue) | ❌ | 2 |

---

## 28. Fluides & Hydraulique

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $Q_V = S \cdot v$ | Débit volumique | ❌ | 3 |
| $S_1 v_1 = S_2 v_2$ | Équation de continuité | ❌ | 3 |
| $P + \frac{1}{2}\rho v^2 + \rho g z = \text{cste}$ | Équation de Bernoulli | ❌ | 2 |
| $HMT = \Delta z + \Delta P_{stat}/(\rho g) + h_J$ | Hauteur manométrique totale | ❌ | 2 |
| $P_{mot} = \rho g Q H / \eta_{pompe}$ | Puissance moteur pompe | ❌ | 2 |
| $Q_1/Q_2 = N_1/N_2$, $H \propto N^2$, $P \propto N^3$ | Lois de similitude pompe | ❌ | 2 |

---

## 29. Capteurs — Conditionnement signal

| Formule | Description | Donnée ? | Fréq. |
|---|---|:---:|:---:|
| $I = 4 + 16(X-X_{min})/(X_{max}-X_{min})$ | Signal 4–20 mA | ❌ | 2 |
| $R(T) = 100(1 + 3{,}85\times10^{-3} T)$ | Résistance Pt100 | ❌ | 2 |
| $f_e \geq 2 f_{max}$ | Théorème de Shannon | ❌ | 2 |
| $\Delta V = V_{ref}/2^n$ | Résolution CAN n bits | ❌ | 2 |

---

*Généré le 2026-05-19 — Sources : corrigés 2016–2021 · rapports jury 2019–2025 · sujets 2015–2025*
*~190 formules recensées, 29 domaines*
