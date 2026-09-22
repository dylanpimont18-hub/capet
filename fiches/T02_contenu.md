# T02 — Puissance en régime alternatif sinusoïdal
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

### 1.1 Puissance en monophasé

| Grandeur | Formule | Unité | Fréquence au CAPET |
|---|---|---|---|
| Puissance active | $P = U \cdot I \cdot \cos\varphi$ | W | Très fréquente (donnée ou calculée) |
| Puissance réactive | $Q = U \cdot I \cdot \sin\varphi$ | VAR | Fréquente |
| Puissance apparente | $S = U \cdot I$ | VA | Fréquente |
| Facteur de puissance | $\cos\varphi = P/S$ | sans unité | Systématique |
| Relation triangle | $S^2 = P^2 + Q^2$ | — | À connaître par cœur |
| Courant monophasé | $I = P/(U \cdot \cos\varphi)$ | A | Fréquente (pompes, réchauffeurs) |
| Résistance depuis P | $R = U^2/P$ (charge purement résistive) | Ω | 2017 (réchauffeur 3 kW, 230 V → R = 17,6 Ω) |

**Contexte** : le réseau monophasé standard France est à **230 V efficace** (tension simple). Les récepteurs monophasés (pompes, réchauffeurs de SPA, luminaires) sont alimentés à 230 V.

### 1.2 Puissance en triphasé équilibré

| Grandeur | Formule | Unité | Note |
|---|---|---|---|
| Puissance active totale | $P = \sqrt{3} \cdot U_{composée} \cdot I \cdot \cos\varphi = 3 \cdot V_{simple} \cdot I \cdot \cos\varphi$ | W | $U_{composée} = 400\,\text{V}$, $V_{simple} = 230\,\text{V}$ |
| Puissance réactive totale | $Q = \sqrt{3} \cdot U \cdot I \cdot \sin\varphi$ | VAR | |
| Puissance apparente totale | $S = \sqrt{3} \cdot U \cdot I$ | VA | |
| Courant de ligne (moteur) | $I = \dfrac{P}{\sqrt{3} \cdot U \cdot \cos\varphi}$ | A | U = tension composée 400 V |
| Courant de ligne (moteur, depuis puissance utile) | $I_n = \dfrac{P_u}{\eta \cdot \sqrt{3} \cdot U \cdot \cos\varphi}$ | A | **Formule pivot CAPET** (2014, 2021) |

**Rappel couplages** :
- Couplage **étoile (Y)** : $V_{simple} = U_{composée}/\sqrt{3}$ → 230 V si réseau 400 V.
- Couplage **triangle (Δ)** : tension aux bornes du bobinage = $U_{composée}$ = 400 V.
- Notation plaque signalétique : **230V/400V** signifie triangle 230 V / étoile 400 V (exploitation normale = étoile 400 V pour réseau européen).

**Fréquence** : La formule du courant de ligne moteur depuis $P_u$ apparaît dans les sujets 2014 E1_Corrige, 2021 Rapport_Jury. C'est la formule la plus souvent demandée dans les parties "installation électrique".

### 1.3 Bilan de puissance d'une installation (somme de récepteurs)

Pour une installation comportant plusieurs récepteurs hétérogènes (moteur, éclairage, informatique, etc.) :

$$P_{totale} = \sum_i P_i \quad [\text{W}]$$
$$Q_{totale} = \sum_i Q_i \quad [\text{VAR}]$$
$$S_{totale} = \sqrt{P_{totale}^2 + Q_{totale}^2} \quad [\text{VA}]$$

**Attention** : $S_{totale} \neq \sum S_i$ sauf si tous les récepteurs ont le même $\cos\varphi$.

**Courant total absorbé** (triphasé) :

$$I_{totale} = \frac{S_{totale}}{\sqrt{3} \cdot U_{composée}}$$

**Facteur de puissance global** :

$$F_P = \frac{P_{totale}}{S_{totale}}$$

*Exemple numérique 2024 E2 (extracteur d'air, lycée Lombards, Troyes)* :
- Moteur extracteur : $P_{mot}$, $\cos\varphi_{mot} = 0{,}85$, $I_n = 229\,\text{A}$
- Ordinateurs + automate : $P_0 = 1\,\text{kW}$, $\cos\varphi_0 = 1$ → $Q_0 = 0$
- Éclairage + équipements : $P_e = 43\,\text{kW}$, $Q_e = 25{,}5\,\text{kVAR}$
- Résultat imposé pour la suite : $P_{charge} = 178{,}3\,\text{kW}$, $Q_{charge} = 108{,}7\,\text{kVAR}$

*Exemple numérique 2017 E2 (SPA) — installation monophasée sur triphasé* :
- Réchauffeur phase 1 : $P = 3\,\text{kW}$, $\cos\varphi = 1$ (résistif pur)
- Pompes hydromassage phases 2 & 3 : $P = 2 \times 2{,}25\,\text{kW}$, $\cos\varphi = 0{,}86$
- Pompe circulation phase 1 : $P = 0{,}26\,\text{kW}$, $\cos\varphi = 0{,}8$

### 1.4 Facteur de puissance, facteur de déplacement et THD

**En présence d'harmoniques**, la distinction est obligatoire :

| Grandeur | Définition | Formule |
|---|---|---|
| Facteur de déplacement | $\cos\varphi$ du fondamental | $\cos\varphi_1 = P/S_1$ |
| Facteur de puissance (FP) | Rapport puissance active / apparente totale | $F_P = P/S_{totale}$ |
| Puissance réactive fondamentale | — | $Q_1 = P \cdot \tan\varphi_1$ |
| Puissance déformante | Due aux harmoniques | $D = \sqrt{S^2 - P^2 - Q_1^2}$ |
| Puissance apparente avec harmoniques | — | $S = \sqrt{P^2 + Q_1^2 + D^2}$ |
| Taux de distorsion harmonique | — | $\text{THD} = \dfrac{\sqrt{I_2^2 + I_3^2 + \cdots + I_n^2}}{I_1}$ |

**Relation FP vs $\cos\varphi$** : $F_P < \cos\varphi_1$ quand le THD est non nul. Si le signal est purement sinusoïdal, $F_P = \cos\varphi$.

**Fréquence** : Cette distinction apparaît systématiquement dans les sujets impliquant des convertisseurs électroniques (variateurs de vitesse 2024 E2, régulateurs d'éclairage public 2018 E2, redresseurs 2026 E1).

### 1.5 Relèvement du facteur de puissance — compensation par condensateurs

**Objectif** : réduire la puissance réactive consommée sur le réseau pour diminuer le courant de ligne et améliorer le $F_P$.

**Principe** : les condensateurs en parallèle fournissent de la puissance réactive capacitive $Q_C < 0$, compensant la puissance réactive inductive $Q_{inductif} > 0$ des charges.

$$Q_C = -3 \cdot C \cdot \omega \cdot V_n^2 \quad (\text{condensateurs couplés en étoile, triphasé})$$

Pour ramener $F_P$ à 1, il faut $Q_C + Q_{inductif} = 0$, donc :

$$C = \frac{Q_{absorb\acute{e}e}}{3 \cdot \omega \cdot V_n^2}$$

*Exemple numérique 2024 E2 (extracteur, lycée Lombards)* :
$$C = \frac{108{,}7 \times 10^3}{3 \times 2\pi \times 50 \times 230^2} = 0{,}016\,\text{F}$$

**Formule littérale démontrée** dans la question B3 : "Montrer que l'expression permettant de calculer la capacité d'un condensateur à coupler en étoile et ramenant le facteur de puissance à 1 est [formule omise — image]". La formule est $C = Q_{absorb\acute{e}e}/(3\omega V_n^2)$.

### 1.6 Chute de tension en ligne liée à une puissance

Pour une ligne triphasée de longueur $X$, résistance linéique $R_u$, inductance linéique $L_u$, charge de puissance active $P$ et courant $I_{tot}$ :

$$R_L = R_u \cdot X \quad [\Omega] \qquad L_L = L_u \cdot X \quad [\text{H}]$$

$$I_{tot} = \frac{P_{charge}}{\sqrt{3} \cdot U_r} \quad (\text{si } F_P = 1)$$

$$\Delta U = \sqrt{U_D^2 - U_r^2} \approx R_L \cdot I_{tot} \quad (\text{approximation})$$

*Exemple 2024 E2* : $X = 850\,\text{m}$, $R_u = 20\,\text{m}\Omega/\text{km}$, $L_u = 1{,}2\,\text{mH/km}$, $P_{charge} = 178{,}3\,\text{kW}$, $F_P = 1$, $U_r = 400\,\text{V}$. Conformité norme NFC 15-100 vérifiée sur $\Delta U / U_D$.

### 1.7 Rendement moteur et puissance absorbée

$$\eta = \frac{P_{utile}}{P_{absorb\acute{e}e}} \implies P_{absorb\acute{e}e} = \frac{P_{utile}}{\eta}$$

$$P_{absorb\acute{e}e} = \sqrt{3} \cdot U \cdot I \cdot \cos\varphi = \frac{P_{utile}}{\eta}$$

$$\implies I_n = \frac{P_{utile}}{\eta \cdot \sqrt{3} \cdot U \cdot \cos\varphi}$$

*Valeurs types* :
- Moteur WEG 132 kW (2014 Pont Chaban-Delmas) : $\eta = 94{,}4\,\%$, $\cos\varphi = 0{,}86$, $I_n = 270{,}1\,\text{A}$ à 400 V
- Moteur 90 kW (2021 Rapport_Jury) : $\eta = 0{,}942$, $\cos\varphi = 0{,}86$, $I_n = 160{,}4\,\text{A}$ à 400 V
- Moteur extracteur (2024) : $\cos\varphi = 0{,}85$, $I_n = 229\,\text{A}$, 400 V, $P_u = 100\,\text{kW}$
- MAS (2026 BAC3) : $I_n = 156\,\text{A}$, $\cos\varphi_{nom} = 0{,}94$, $\eta = 0{,}905$, 230V/400V (700 Hz — contexte variateur)

### 1.8 Essai à vide de la MAS — puissances

À vide ($g \approx 0$), le schéma équivalent se réduit à la branche magnétisante :

$$P_0 = \frac{V^2}{R_f} \quad (\text{pertes fer}) \qquad Q_0 = \frac{V^2}{X_m} \quad (\text{puissance réactive magnétisante})$$

$$S_0 = \sqrt{P_0^2 + Q_0^2}$$

*Exemple 2021 E1* : $Q_0 = 2137\,\text{VAR}$, $V = 133\,\text{V}$, $f = 50\,\text{Hz}$ → $X_m = V^2/Q_0$.

*Exemple 2026 BAC3* : $I_0 = 42{,}5\,\text{A}$, $P_0 = 7{,}82\,\text{kW}$ → calculer $R_f$ et $X_m$.

### 1.9 Abonnement EDF / puissance souscrite

L'abonnement triphasé est souscrit en **kVA** (puissance apparente). Pour passer d'une puissance active P à la puissance apparente S nécessaire, il faut connaître $\cos\varphi$ global de l'installation :

$$S_{abonnement} \geq S_{installation} = \frac{P_{installation}}{\cos\varphi}$$

*Exemple 2017 E2 (SPA)* : consommation actuelle 16 kW, ajout SPA crée un déséquilibre de $P_{phase1} = 3{,}26\,\text{kW}$ → puissance triphasée supplémentaire $P_{suppl} = 3 \times 3{,}26 = 9{,}978\,\text{kW}$ → $P_{totale} = 16 + 9{,}978 = 25{,}78\,\text{kW}$ → nouvel abonnement **30 kVA** (18 kVA → 30 kVA, surcoût 494,61 €/an).

---

## 2. QUESTIONS TYPES

### Q-TYPE 1 — Calcul du courant de ligne d'un moteur (triphasé, depuis puissance utile)
**Source** : 2014 E1_Corrige (Pont Chaban-Delmas) + 2021 Rapport_Jury

**Énoncé complet** (2014) :
> La motorisation d'un contrepoids du Pont Chaban-Delmas utilise un moteur WEG de 132 kW. D'après la documentation technique, le rendement est $\eta = 94{,}4\,\%$, le facteur de puissance $\cos\varphi = 0{,}86$, la tension d'alimentation est 400 V triphasé. Calculer le courant nominal $I_n$ absorbé par ce moteur lors du fonctionnement à pleine charge.

**Correction complète** :
$$P_{absorb\acute{e}e} = \frac{P_{utile}}{\eta} = \frac{132\,\text{kW}}{0{,}944} = 139{,}8\,\text{kW}$$

$$I_n = \frac{P_{absorb\acute{e}e}}{\sqrt{3} \cdot U \cdot \cos\varphi} = \frac{P_{utile}}{\eta \cdot \sqrt{3} \cdot U \cdot \cos\varphi} = \frac{151{,}9 \times 10^3}{0{,}944 \times \sqrt{3} \times 400 \times 0{,}86} = 270{,}1\,\text{A}$$

*(Note : 151,9 kW correspond à la puissance maximale de l'application particulière du sujet 2014 ; la formule est identique.)*

**Variante 2021** (90 kW) :
$$I_n = \frac{90\,000}{0{,}942 \times \sqrt{3} \times 400 \times 0{,}86} = 160{,}4\,\text{A}$$

**Ce qu'attend le jury** : la formule développée $I_n = P_u / (\eta \cdot \sqrt{3} \cdot U \cdot \cos\varphi)$ avec unités cohérentes.

---

### Q-TYPE 2 — Bilan de puissance d'une installation et choix d'abonnement
**Source** : 2017 E2 (SPA), questions B1.2, B2.2, B2.3

**Énoncé complet** :
> Un SPA est alimenté par un réseau triphasé 400 V. Il comprend :
> - Un réchauffeur monophasé (phase 1) : $P = 3\,\text{kW}$, $\cos\varphi = 1$
> - Deux pompes d'hydromassage monophasées (phases 2 et 3) : $P = 2{,}25\,\text{kW}$ chacune, $\cos\varphi = 0{,}86$
> - Une pompe de circulation monophasée (phase 1) : $P = 0{,}26\,\text{kW}$, $\cos\varphi = 0{,}8$
>
> Le propriétaire dispose d'un abonnement actuel de 18 kVA triphasé, consommation max 16 kW (sans déséquilibre).
>
> B1.2 : Déterminer le courant consommé par chaque récepteur.
>
> B2.2 : Identifier le cas de fonctionnement le plus consommateur.
>
> B2.3 : Déterminer le nouvel abonnement nécessaire en tenant compte du déséquilibre.

**Correction complète** :

B1.2 — Courants :
- Réchauffeur : $I_R = P/(U \cdot \cos\varphi) = 3000/(230 \times 1) = 13{,}05\,\text{A}$
- Pompe hydromassage : $I_{PH} = 2250/(230 \times 0{,}86) = 11{,}37\,\text{A}$
- Pompe circulation : $I_{PC} = 260/(230 \times 0{,}8) = 1{,}41\,\text{A}$

B2.2 : Le SPA consomme le plus de courant et de puissance quand le réchauffeur ET la pompe de circulation fonctionnent simultanément (cas 1 : pompe de filtration + réchauffeur).

B2.3 :
- Puissance supplémentaire sur la phase 1 : $P_{phase1} = P_{réchauffeur} + P_{circulation} = 3000 + 260 = 3260\,\text{W} = 3{,}26\,\text{kW}$
- L'alimentation est monophasée mais l'abonnement est triphasé → la puissance souscrite est triphasée. Pour équilibrer, on multiplie par 3 :
$$P_{suppl\acute{e}mentaire} = 3 \times 3{,}26 = 9{,}978\,\text{kW}$$
- Nouvelle puissance totale : $P_{totale} = 16 + 9{,}978 = 25{,}78\,\text{kW}$
- Abonnement en kVA → arrondi au palier supérieur disponible : **30 kVA**
- Surcoût : 761,47 - 266,84 = **494,63 €/an** (tarif kWh identique)

---

### Q-TYPE 3 — Puissances active, réactive, apparente avec THD (éclairage public)
**Source** : 2018 E2_Sujet (éclairage public SHP), 2018 Rapport_Jury (Questions 13–14)

**Énoncé complet** :
> Une installation d'éclairage public est alimentée par un réseau triphasé 3P+N 400 V / 50 Hz. La zone "rue des fêtes" comporte **46 luminaires** répartis de manière équilibrée sur les 3 phases. Chaque luminaire est constitué d'une lampe SHP SON T PIA Plus 150 W avec un facteur de puissance $\cos\varphi = 0{,}84$ et d'un amorceur de puissance $P_a = 50\,\text{W}$.
>
> D'après la documentation, 15 luminaires consomment 3020 W en mode nominal.
>
> Q13 : Vérifier la puissance active $P_{1L}$, déterminer la puissance réactive $Q_{1L}$ et la puissance apparente $S_{1L}$ pour un luminaire.
>
> Q14 : Calculer la puissance apparente totale $S_{TL}$.

**Correction complète** :
- Vérification $P_{1L}$ : $P_{1L} = 3020/15 = 201{,}3\,\text{W}$ ✓ (cohérent avec 150 W lampe + amorceur)
- $Q_{1L} = P_{1L} \cdot \tan(\arccos(0{,}86)) = 201{,}3 \times \tan(\arccos(0{,}86))$

Calcul intermédiaire : $\cos\varphi = 0{,}86$ → $\varphi = 30{,}7°$ → $\tan\varphi = 0{,}5936$
$$Q_{1L} = 201{,}3 \times 0{,}5936 = 119{,}5\,\text{VAR}$$
$$S_{1L} = \sqrt{P_{1L}^2 + Q_{1L}^2} = \sqrt{201{,}3^2 + 119{,}5^2} = 234\,\text{VA}$$
$$S_{TL} = 3 \times S_{1P} = 46 \times S_{1L} = 46 \times 234 = 10\,764\,\text{VA} \approx 10{,}8\,\text{kVA}$$

**Note** : Le jury précise que $\cos\varphi = 0{,}84$ est donné dans les données constructeur mais le calcul utilise $\cos\varphi = 0{,}86$ (valeur figurant dans les DRS). Vérifier la cohérence des données fournies.

---

### Q-TYPE 4 — Facteur de puissance vs facteur de déplacement (comparaison régulateurs)
**Source** : 2018 Rapport_Jury (Questions 7–9), sujet comparaison LUBIO® vs COMPACTO II®

**Énoncé complet** :
> Pour chaque type de régulateur d'éclairage public et pour le fonctionnement en mode nominal et économique, identifier et comparer la valeur du THD, du facteur de puissance (FP) et du facteur de déplacement ($\cos\varphi$).

**Tableau de données (extrait Rapport_Jury 2018)** :

| Grandeur | LUBIO® nominal (220 V) | LUBIO® éco (190 V) | COMPACTO II® nominal (220 V) | COMPACTO II® éco (190 V) |
|---|---|---|---|---|
| Tension (V) | 235 | 236,9 | 233,1 | 235,2 |
| Courant (A) | 11,69 | 9,71 | 8,48 | 6,5 |
| P (W) | 1930 | 1460 | 1900 | 1430 |
| S (VA) | 2720 | 2290 | 1980 | 1530 |
| THD (%) | 28,8 | 28,9 | 29,6 | 28,5 |
| FP | 0,71 | 0,64 | **0,96** | **0,94** |
| $\cos\varphi$ | 0,75 | 0,67 | **1** | **0,98** |
| $Q_1$ (VAR) | $P \times \tan\varphi = 1702$ | 1618 | 0 | 290 |
| D (VAD) | $\sqrt{S^2-P^2-Q_1^2} = 881$ | 703 | 557 | 460 |

**Formules utilisées** : $Q_1 = P \times \tan(\varphi)$, $D = \sqrt{S^2 - P^2 - Q_1^2}$

**Correction Q9 (jury 2018)** : "Le COMPACTO II® possède un facteur de puissance et un facteur de déplacement ($\cos\varphi$) **nettement meilleurs** que le LUBIO®. Il **absorbe moins de courant** pour une même puissance consommée. Son THD est équivalent à celui du LUBIO®, mais comme il consomme moins de courant les harmoniques de courant sont plus faibles. Il peut aussi piloter des LED ce que ne peut pas faire le LUBIO®."

---

### Q-TYPE 5 — Compensation par condensateurs (relèvement FP à 1)
**Source** : 2024 E2_Disciplinaire_IE (extracteur d'air, lycée Lombards), Questions B1–B4

**Énoncé complet** :
> L'atelier bois et menuiserie est alimenté par un réseau triphasé équilibré $U_r = 400\,\text{V}$.
> Les récepteurs sont :
> - Moto-ventilateur extracteur : $I_n = 229\,\text{A}$, $\cos\varphi_{mot} = 0{,}85$
> - Ordinateurs + automate : $P_0 = 1\,\text{kW}$, $\cos\varphi_0 = 1$
> - Éclairage + équipements : $P_e = 43\,\text{kW}$, $Q_e = 25{,}5\,\text{kVAR}$
>
> B1 : Calculer $P_{charge}$, $Q_{charge}$, $S_{charge}$ totaux.
>
> B2 : En déduire $I_{abs}$ et $F_P$.
>
> B3 : Montrer que $C = Q_{absorb\acute{e}e}/(3 \cdot \omega \cdot V_n^2)$ pour ramener $F_P$ à 1 (condensateurs étoile).
>
> B4 : Calculer C.

**Correction complète** :
*(Pour B1–B2, les valeurs exactes du moteur sont calculées à partir de $I_n$ et $\cos\varphi_{mot}$, puis sommées avec les autres récepteurs. Le sujet donne le résultat imposé pour la suite :)*
$$P_{charge} = 178{,}3\,\text{kW} \qquad Q_{charge} = 108{,}7\,\text{kVAR}$$
$$S_{charge} = \sqrt{178{,}3^2 + 108{,}7^2} \approx 210\,\text{kVA}$$
$$I_{abs} = \frac{S_{charge}}{\sqrt{3} \times 400} \approx 303\,\text{A}$$
$$F_P = \frac{P_{charge}}{S_{charge}} = \frac{178{,}3}{210} \approx 0{,}849$$

B3 — Démonstration :
Pour $F_P = 1$, il faut $Q_{totale} = Q_{absorb\acute{e}e} + Q_C = 0$, donc $Q_C = -Q_{absorb\acute{e}e}$.
Pour un condensateur $C$ couplé en étoile : $Q_C = -3 \cdot C \cdot \omega \cdot V_n^2$ (puissance réactive capacitive par phase × 3 phases), avec $V_n = 230\,\text{V}$ (tension simple).
$$\Rightarrow C = \frac{Q_{absorb\acute{e}e}}{3 \cdot \omega \cdot V_n^2}$$

B4 :
$$C = \frac{108{,}7 \times 10^3}{3 \times 2\pi \times 50 \times 230^2} = \frac{108\,700}{3 \times 314{,}16 \times 52\,900} = \frac{108\,700}{49\,886\,640} \approx 0{,}016\,\text{F} = 16\,\text{mF}$$

*(Le gestionnaire d'énergie impose $F_P \in [0{,}92\,;\,1]$, la compensation vise $F_P = 1$.)*

---

### Q-TYPE 6 — THD, FP et conformité à la norme (variateur de vitesse)
**Source** : 2024 E2_Disciplinaire_IE, Questions B10–B13

**Énoncé complet** :
> Un variateur de vitesse alimente un moteur asynchrone. Le pont redresseur génère des harmoniques sur le réseau. On compare deux modes de commande : cas 1 (pleine onde) et cas 2 (MLI $f_p = 6\,000\,\text{Hz}$). La norme IEC/EN 61000-2-2 fixe un THD de courant $\leq 25\,\%$.
>
> B10 : À l'aide du document DT3 (spectres donnés), calculer le THD pour les rangs 1, 3, 5, 7, 9.
>
> B11 : Conclure vis-à-vis de la norme.
>
> B12 : Commenter la conséquence de la MLI sur le spectre.

**Formule THD** :
$$\text{THD} = \frac{\sqrt{I_2^2 + I_3^2 + I_4^2 + \cdots + I_n^2}}{I_1}$$

**Correction (extrait Rapport_Jury 2024)** :
- Cas 2 : $\text{THD} = \sqrt{37^2 + 22^2}/170 = 0{,}25 = 25\,\%$ → répond juste à l'exigence (cas 1 dépasse 25 %).
- B12 : La MLI génère des harmoniques en **haute fréquence** (autour de $f_p$). Solution : filtre passe-bas (circuit R,L).
- B13 : La MLI **limite le THD** du courant et donc les ondulations du couple ; les harmoniques HF sont atténuées par l'effet inductif des enroulements du moteur.

---

## 3. ATTENTES DU JURY

### 3.1 Sur les formules de puissance (2018 Rapport_Jury, éclairage public)

**Citation directe** (Question 9, 2018 Rapport_Jury) :
> "Le COMPACTO II® possède un facteur de puissance et un facteur de déplacement (cos φ) nettement meilleurs que le LUBIO®. Il absorbe moins de courant pour une même puissance consommée."

**Implication** : Le jury attend que les candidats distinguent explicitement $F_P$ (facteur de puissance global) et $\cos\varphi$ (facteur de déplacement du fondamental) en présence d'harmoniques. La confusion entre les deux est un piège classique.

### 3.2 Sur la valeur efficace et la puissance (2017 E2_Corrige)

**Citation directe** (Question C1.1, 2017 E2_Corrige) :
> "La puissance dissipée par une résistance soumise à une tension continue de 230 V est la même que celle d'une résistance soumise à une tension dont la **valeur efficace** vaut 230 V."

**Implication** : Le jury attend la maîtrise de la notion de valeur efficace. La puissance dissipée dans une résistance est $P = U_{eff}^2/R$ quelle que soit la forme du signal, à condition d'utiliser la valeur efficace.

### 3.3 Sur le calcul du courant nominal d'un moteur (2021 Rapport_Jury)

**Citation directe** (Question 18, 2021 Rapport_Jury) :
> "$I_{n\,moteur} = P_u / (\eta \times \sqrt{3} \times U \times \cos\varphi) = 90\,000 / (0{,}942 \times \sqrt{3} \times 400 \times 0{,}86) = 160{,}4\,\text{A}$"

**Implication** : Le jury donne la formule complète avec rendement. Il est attendu que le candidat utilise la puissance **utile** $P_u$ (et non la puissance absorbée) avec le rendement $\eta$ dans la formule.

### 3.4 Sur l'abonnement EDF et le déséquilibre (2017 E2_Corrige)

**Citation directe** (Question B2.3, 2017 E2_Corrige) :
> "C'est lors du fonctionnement du réchauffeur que la puissance est la plus élevée. La puissance supplémentaire sur la phase 1 est : $P_{phase1} = P_{réchauffeur} + P_{circulation} = 3000 + 260 = 3260\,\text{W}$. Puissance nécessaire en plus sur l'abonnement triphasé : $P = 3 \times P_{phase1} = 3 \times 3{,}26 = 9{,}978\,\text{kW}$."

**Implication** : Le jury attend la compréhension du fait qu'un abonnement triphasé est exprimé en kVA *équilibré* ; pour intégrer une charge monophasée déséquilibrée, on convertit en équivalent triphasé en multipliant par 3.

### 3.5 Sur le THD et la conformité à la norme (2024 Rapport_Jury)

**Citation directe** (Question B11, 2024 Rapport_Jury) :
> "La norme IEC/EN 61000-2-2 fixe un THD de courant inférieur à 25 % pour assurer une compatibilité électromagnétique conforme. Ainsi le cas 2 répond à cette exigence mais pas le cas 1."

**Citation directe** (Question B12, 2024 Rapport_Jury) :
> "On remarque que la mise en place de la MLI génère des harmoniques dans les hautes fréquences. La solution pour les éliminer est d'introduire un **filtre passe bas** (circuit R,L par exemple)."

### 3.6 Sur le facteur de puissance d'un redresseur (2026 E1_Sujet)

**Citation directe** (Question E8, 2026 E1_Sujet) :
> "Rappeler la définition du facteur de puissance $f_P$ au secondaire du transformateur puis calculer sa valeur. Conclure alors vis-à-vis du cahier des charges pour le critère portant sur le facteur de puissance."

La cahier des charges impose $f_P > 0{,}9$. La formule pour un pont PD3 est $f_P = (\sqrt{q}/\pi) \times \sin(\pi/q)$ avec $q$ le nombre de phases.

**Implication** : La définition du facteur de puissance (FP = P/S) est une question récurrente. Le jury attend une définition claire, puis un calcul numérique, puis une conclusion binaire (conforme / non conforme au CDC).

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique | Contexte | Année |
|---|---|---|---|
| $\cos\varphi$ moteur électrique (MAS 132 kW) | 0,86 | Pont Chaban-Delmas, WEG 132 kW | 2014 |
| $\cos\varphi$ moteur (MAS 90 kW) | 0,86 | STEP solaire, variateur | 2021 |
| $\cos\varphi$ moteur extracteur (MAS 100 kW) | 0,85 | Extracteur d'air, lycée Lombards | 2024 |
| $\cos\varphi$ MAS nominal (BAC3 700 Hz) | 0,94 | MAS alimentée par convertisseur | 2026 |
| $\cos\varphi$ pompe hydromassage | 0,86 | SPA monophasé | 2017 |
| $\cos\varphi$ pompe de circulation | 0,80 | SPA monophasé | 2017 |
| $\cos\varphi$ lampe SHP 150 W | 0,84 | Éclairage public | 2018 |
| $\eta$ moteur WEG 132 kW | 94,4 % | Pont Chaban-Delmas | 2014 |
| $\eta$ moteur 90 kW | 94,2 % | STEP solaire | 2021 |
| $\eta$ MAS (2026 BAC3) | 90,5 % | MAS variateur | 2026 |
| Courant nominal WEG 132 kW à 400 V | 247 A (données plaque) / 270 A (calculé) | Pont Chaban-Delmas | 2014 |
| Courant nominal moteur 90 kW | 160,4 A | STEP solaire | 2021 |
| Courant nominal extracteur 100 kW | 229 A (plaque) | Extracteur lycée Lombards | 2024 |
| $Q_0$ essai à vide MAS | 2137 VAR | MAS monophasé test | 2021 |
| $P_0$ essai à vide MAS (BAC3) | 7,82 kW | MAS triphasé BAC3 | 2026 |
| Condensateur de compensation étoile | 16 mF | Installation triphasée 400 V, $Q = 108{,}7\,\text{kVAR}$ | 2024 |
| Abonnement EDF : paliers courants | 6, 9, 12, 18, 24, 30, 36 kVA | Abonnement résidentiel / petit tertiaire | 2017 |
| THD LUBIO nominal | 28,8 % | Régulateur éclairage public | 2018 |
| THD COMPACTO II nominal | 29,6 % | Régulateur éclairage public | 2018 |
| FP LUBIO nominal | 0,71 | Régulateur éclairage public | 2018 |
| FP COMPACTO II nominal | 0,96 | Régulateur éclairage public | 2018 |
| Norme THD courant réseau | < 25 % (IEC/EN 61000-2-2) | Variateur de vitesse | 2024 |
| Norme chute de tension ligne | vérification norme NFC 15-100 | Installation atelier bois | 2024 |
| Tension réseau monophasé France | 230 V efficace (tension simple) | Tous sujets | Systématique |
| Tension réseau triphasé France | 400 V composée, 230 V simple | Tous sujets | Systématique |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

### 5.1 Confusion entre $F_P$ et $\cos\varphi$

**Le piège** : Confondre le facteur de puissance $F_P = P/S$ et le facteur de déplacement $\cos\varphi_1$ (déphasage fondamental).

**La distinction** :
- Si le signal est **purement sinusoïdal** (pas d'harmoniques) : $F_P = \cos\varphi$.
- Si le signal **contient des harmoniques** (convertisseurs, variateurs, régulateurs) : $F_P < \cos\varphi_1$ car $S_{totale} > S_1$.
- La puissance déformante $D$ s'ajoute : $S = \sqrt{P^2 + Q_1^2 + D^2}$.

**Erreur type** : Dans le sujet 2018, certains candidats confondaient les deux colonnes "FP" et "cos φ" du tableau. Le jury 2018 insiste sur la **nettement meilleure** performance du COMPACTO II® pour $F_P$ et $\cos\varphi$.

### 5.2 Oubli du rendement dans le calcul du courant

**Le piège** : Calculer $I_n = P_{utile}/(\sqrt{3} \cdot U \cdot \cos\varphi)$ sans diviser par $\eta$.

**Correction** : La formule correcte est $I_n = P_{utile}/(\eta \cdot \sqrt{3} \cdot U \cdot \cos\varphi)$. L'oubli du rendement sous-estime le courant nominal, conduisant à un mauvais dimensionnement des protections.

### 5.3 Mauvais choix de la tension (230 V vs 400 V)

**Le piège** : Utiliser 400 V au lieu de 230 V pour le calcul de puissance d'un récepteur monophasé branché sur le réseau triphasé.

**Règle** :
- Récepteur **monophasé** branché entre phase et neutre → $U = V_{simple} = 230\,\text{V}$
- Récepteur **triphasé** → $U = U_{composée} = 400\,\text{V}$ dans les formules triphasées

**Erreur type** : Pour le réchauffeur du SPA 2017 : $I_R = 3000/(400 \times 1)$ → FAUX. Correct : $I_R = 3000/(230 \times 1) = 13{,}05\,\text{A}$.

### 5.4 Sommation incorrecte des puissances apparentes

**Le piège** : Calculer $S_{totale} = S_1 + S_2 + \cdots$ au lieu de passer par $P_{totale}$ et $Q_{totale}$.

**Règle** : On peut additionner $P$ et $Q$ algébriquement (scalaires), mais **pas** $S$ directement sauf si tous les $\cos\varphi$ sont identiques.

### 5.5 Mauvais traitement du déséquilibre triphasé

**Le piège** : Pour une installation monophasée déséquilibrée (ex. : SPA 2017 avec réchauffeur sur phase 1 uniquement), calculer la puissance totale sans tenir compte du déséquilibre.

**Méthode correcte** : Calculer la puissance max par phase, puis convertir en équivalent triphasé équilibré en multipliant par 3 (méthode du sujet 2017 : $P_{abonnement} = 3 \times P_{phase\,la\,plus\,chargée} + P_{actuelle}$).

### 5.6 Mauvaise utilisation de la formule de capacité de compensation

**Le piège** : Oublier que $V_n = 230\,\text{V}$ (tension **simple**, pas composée) dans la formule $C = Q/(3 \omega V_n^2)$ pour un couplage étoile.

**Règle** : En couplage étoile, la tension aux bornes de chaque condensateur est $V_n = U_{composée}/\sqrt{3} = 230\,\text{V}$.

### 5.7 Signe de la puissance réactive capacitive

**Le piège** : Confondre le signe dans le bilan de puissance réactive.

**Règle** : Par convention, $Q_{inductif} > 0$ (moteurs, inductances) et $Q_{capacitif} < 0$ (condensateurs). Pour compenser : $Q_C = -Q_{absorb\acute{e}e}$.

### 5.8 THD : numérateur et dénominateur

**Le piège** : Diviser par la valeur efficace totale plutôt que par la valeur efficace du **fondamental** $I_1$.

**Formule correcte** : $\text{THD} = \sqrt{\sum_{k=2}^{n} I_k^2} / I_1$ (dénominateur = fondamental uniquement).

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

### 6.1 → T01 (Machine asynchrone — fonctionnement)

La MAS est le principal récepteur inductif dans les sujets CAPET. Le T02 fournit le **courant de ligne nominal** calculé depuis la plaque signalétique (puissance, rendement, $\cos\varphi$), utilisé ensuite en T01 pour le modèle équivalent, le glissement, les essais à vide et en charge.

Formule charnière : $I_n = P_u/(\eta \cdot \sqrt{3} \cdot U \cdot \cos\varphi)$ (2014, 2021, 2024, 2026).

L'essai à vide fournit $Q_0 = V^2/X_m$ et $P_0 = V^2/R_f$, qui sont des formules de puissance T02 utilisées pour identifier les paramètres du schéma équivalent T01.

### 6.2 → T03 (Variateur de vitesse — MLI, onduleur)

Le THD du courant réseau généré par les variateurs (T03 — convertisseurs) est évalué avec les formules T02. La distinction $F_P$ vs $\cos\varphi$ en présence d'harmoniques est au croisement de ces deux thèmes (2018 E2, 2024 E2).

### 6.3 → T04 (Réseaux électriques — distribution, protection)

La chute de tension en ligne ($\Delta U$) est calculée depuis la puissance de la charge et le courant, liée au T02 (bilan de puissance) et au T04 (dimensionnement des câbles, normes NFC 15-100). Le 2024 E2 (Questions B5–B9) est entièrement à ce croisement.

Le choix de l'abonnement EDF (kVA) est une application directe du T02 dans un contexte réseau.

### 6.4 → Éclairage et efficacité énergétique

Les sujets sur l'éclairage public (2018) et l'éclairage de bâtiment (2013 Tour Elithis) croisent T02 pour le calcul des puissances réactives des luminaires, du THD des régulateurs, et du choix des protections.

### 6.5 → Compréhension pédagogique (CAPET — volet enseignement)

Le T02 est directement enseigné en STI2D (SIN, ITEC, EE) et en Sciences de l'ingénieur. Les formules $P = UI\cos\varphi$, $S^2 = P^2 + Q^2$ et le triangle des puissances font partie du programme de terminal STI2D (chapitre "Énergie, puissance"). Le facteur de puissance et son relèvement sont explicitement au programme.

**Contextes pédagogiques utilisables** :
- SPA (2017) : contexte habituel, accessible, connexion thermique/électrique.
- Éclairage public (2018) : contexte qualité de l'énergie, THD, intérêt pratique.
- Extracteur d'air (2024) : contexte atelier lycée professionnel, très proche des situations d'enseignement en BTS ET ou STS.

---

*Fichier produit par analyse documentaire des 41 fichiers Markdown CAPET SII IE 2013–2026.*
*Sources primaires : corpus `docs/CAPET_Markdown-20260629T134311Z-3-001/CAPET_Markdown/docs/CAPET_SII_IE/06_PDFs_Originaux/`*
*Fichiers avec contenu T02 substantiel : 2014/E1_Corrige, 2017/E2_Sujet + E2_Corrige, 2018/E2_Sujet + Rapport_Jury, 2021/E1_Sujet + Rapport_Jury, 2024/E2_Disciplinaire_IE + Rapport_Jury, 2026/E1_Sujet + E2_Sujet_BAC3.*
*Fichiers sans contenu T02 significatif : 2013 (Tour Elithis), 2015 (shelter deployable), 2016 (aucun fichier disponible avec T02), 2019 (téléphérique), 2020 (sans T02), 2022 (cogénération thermique), 2023 (robot viticole), 2025/E2 (île La Réunion, hydrogène), 2025/E2_Appliquee (palan), 2023/E2_Appliquee + 2024/E2_Appliquee.*
