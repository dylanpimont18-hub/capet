# T16 — Énergies renouvelables : photovoltaïque, hydraulique, éolien

Sources analysées : E2_Sujet_2021, Rapport_Jury_2021, E2_Disciplinaire_IE_2025, Rapport_Jury_2025, E2_Sujet_2023, E1_Sujet_2026, E2_Disciplinaire_IE_2022, Rapport_Jury_2022, E2_Sujet_2020.

---

## 1. FORMULES ET COURS

### 1.1 Photovoltaïque — modèle électrique d'un panneau

**Modèle simplifié d'une cellule PV :**
- Source de courant $I_{ph}$ proportionnelle à l'irradiance, en parallèle avec une diode (jonction PN)
- Courant court-circuit : $I_{sc}$ (idem $I_{ph}$ en première approximation)
- Tension en circuit ouvert : $V_{oc}$

**Paramètres à l'état standard (STC : irradiance 1000 W·m$^{-2}$, $T = 25$°C) :**
| Paramètre | Notation | Valeur typique |
|---|---|---|
| Puissance crête | $P_{crête}$ | 320 W |
| Courant de court-circuit | $I_{sc}$ | 9,76 A |
| Tension en circuit ouvert | $V_{oc}$ | 40,96 V |
| Courant au point de puissance max | $I_{MPP}$ | 9,34 A |
| Tension au point de puissance max | $V_{MPP}$ | 34,32 V |
| Dimensions | — | 1675 × 992 mm (1,66 m²) |

- Source : E2_Sujet_2021 (Q11, Q12) et Rapport_Jury_2021 : panneau DMH320M6, 60 cellules en série

**Puissance d'un champ de panneaux :**
$$P_{champ} = N_{panneaux} \times P_{crête} \times \frac{G}{G_0}$$

où $G$ est l'irradiance réelle (W·m$^{-2}$) et $G_0 = 1000$ W·m$^{-2}$ l'irradiance de référence.

**Influence de la température** (effet négatif sur la puissance) :
- Augmentation de 1 °C → diminution de ≈ 0,4 % de $P_{crête}$ pour les cellules Si-mono
- Exemple : irradiance 600 W·m$^{-2}$, $T = 50$°C → $P_{MPP} = 140 \times 0{,}9 = 126$ kW (chute de 10 % par rapport à 25°C)
- Source : Rapport_Jury_2021 (Q14)

### 1.2 MPPT — Maximum Power Point Tracking

**Définition :** commande qui extrait en permanence la puissance maximale du champ photovoltaïque en ajustant le rapport cyclique du convertisseur DC/DC (hacheur élévateur) pour que le panneau fonctionne à sa tension $V_{MPP}$.

**Algorithme perturbation et observation (P&O) :**
- Imposer $U + \Delta U$ au panneau
- Si $\Delta P > 0$ : continuer dans le même sens (on se rapproche du MPP)
- Si $\Delta P < 0$ : inverser le sens de la perturbation (on s'éloigne du MPP)
- Source : E2_Disciplinaire_IE_2025 (Q17, Q18), Rapport_Jury_2025 (Q18)

**Calcul du rapport cyclique (hacheur élévateur) :**
$$f_m = \frac{U_{PV}}{E_b}$$

où $U_{PV}$ est la tension du champ PV et $E_b$ la tension du bus continu en sortie.

- Source : Rapport_Jury_2025 (Q19) : pour $P_1$ : $f_m = \frac{195}{48} = 4{,}06$ ; pour $P_{max}$ : $f_m = \frac{317}{48} = 6{,}6$ ; pour $P_2$ : $f_m = \frac{340}{48} = 7{,}08$

**Connexion des panneaux sur onduleur :**
$$N_{série} = \frac{V_{MPP\,max\,onduleur}}{V_{MPP\,panneau}}, \quad N_{onduleurs} = \frac{N_{total}}{N_{entrées} \times N_{série}}$$

- Source : E2_Sujet_2021 (Q13), Rapport_Jury_2021 : « 26 panneaux en série par entrée, 5 entrées par onduleur → $P_{MPP} = 26 \times 320 = 8320$ W par entrée ; $V_{MPP} = 26 \times 34{,}32 = 892$ V »

### 1.3 Hydraulique — Micro-STEP et micro-centrale

**Énergie potentielle d'une retenue d'eau :**
$$E_p = m \cdot g \cdot h = \rho_{eau} \cdot V \cdot g \cdot h$$

- $\rho_{eau} = 1000$ kg·m$^{-3}$, $g = 9{,}81$ m·s$^{-2}$
- Source : E2_Sujet_2021 (Q5) : $V_{utile} = 900$ m$^3$, $h = 130$ m → $E_p = 318{,}8$ kW·h

**Puissance hydraulique à la turbine :**
$$P_{turb} = \rho \cdot g \cdot Q \cdot H_{net} \cdot \eta_{turb}$$

- $Q$ : débit volumique (m$^3$·s$^{-1}$), $H_{net}$ : hauteur nette (m), $\eta_{turb}$ : rendement turbine-alternateur
- Source : E2_Sujet_2021 (Q5–Q10)

**Débit et durée de pompage :**
- Débit de la pompe lu sur les courbes constructeur : $Q_{pompe} = 160$ m$^3$·h$^{-1}$
- Durée de remplissage : $T = V / Q_{pompe}$
- Source : Rapport_Jury_2021 (Q8) : « $T = 900/160 = 5{,}625$ h soit 5 h 37 min »

**Rendement global du stockage par pompage :**
$$\eta_{st} = \frac{E_{élec\_turbinage}}{E_{élec\_pompage}}$$

- Source : Rapport_Jury_2021 (Q9) : $\eta_{st} = 248{,}7 / 427{,}5 = 58{,}2\%$

### 1.4 Éolien — notions qualitatives

**Puissance maximale extractible du vent (loi de Betz) :**
$$P_{vent} = \frac{1}{2} \rho_{air} \cdot A_{rotor} \cdot v^3$$

$$P_{extrait} = C_p \cdot P_{vent} = C_p \cdot \frac{1}{2} \rho_{air} \cdot A_{rotor} \cdot v^3$$

- $C_p$ : coefficient de puissance (facteur de Betz : $C_p^{max} \leq 16/27 \approx 0{,}593$)
- $A_{rotor} = \pi R^2$ : surface balayée par le rotor (m²)
- $v$ : vitesse du vent (m·s$^{-1}$)
- Fréquence d'apparition dans les sujets CAPET IE analysés : **faible** — non directement posé dans les sujets E2 disciplinaires consultés mais présent dans le programme officiel et dans les sujets E1 communs (allusions au vent)

**Machine asynchrone à double alimentation (DFIG) :**
- Stator connecté directement au réseau (50 Hz)
- Rotor connecté au réseau via un convertisseur de fréquence (contrôle du glissement)
- Permet la production à vitesse variable tout en maintenant une fréquence statorique fixe
- Avantages : rendement élevé, contrôle indépendant de $P$ et $Q$
- Source : programme CAPET SII IE 2026

**Comparaison des filières de production renouvelable :**
- Source : E2_Disciplinaire_IE_2022 (Q19), Rapport_Jury_2022

| Filière | Avantages | Inconvénients |
|---|---|---|
| Panneaux PV | Silencieux, entretien faible, modulaire | Intermittent, surface importante |
| Micro-turbine alternateur | Disponible nuit et jour (si eau) | Lieu spécifique, débit variable |
| Module Peltier | Pas de pièce mobile, très fiable | Rendement très faible (< 5 %) |
| Éolienne | Bonne productivité côtier/montagne | Bruit, intermittent, accord riverains |

### 1.5 Chaîne de conversion PV complète

```
Panneaux PV → Convertisseur DC/DC (MPPT, hacheur élévateur) → Bus DC → Onduleur → Réseau AC
                                                                         ↕
                                                                    Batterie (via hacheur bidirectionnel)
```

- CV1 = hacheur élévateur (MPPT)
- CV2 = redresseur (réseau AC → DC, pour charge depuis réseau)
- CV3 = onduleur (DC → AC pour alimentation des charges)
- Source : E2_Disciplinaire_IE_2025 (Q14) et Rapport_Jury_2025 (Q14) : tableau des convertisseurs CV1–CV3

### 1.6 Vitesse spécifique d'une éolienne

*(complément du référentiel, 2026-11-10 — notion hors sujets 2013–2026 sauf mention)*

**Vitesse spécifique d'une éolienne :**
$$\lambda = \frac{\Omega \, R}{v}$$
- Valable pour un rotor de rayon R tournant à Ω sous un vent de vitesse v

---

## 2. QUESTIONS TYPES (max 6)

### Q1 — Superficie et nombre de panneaux nécessaires
**Source :** E2_Sujet_2021 (Q11), Rapport_Jury_2021
**Énoncé :** « Déterminer la superficie nécessaire pour atteindre la puissance crête souhaitée. »
**Données :** $P_{crête\,souhaitée} = 250$ kW, $P_{panneau} = 320$ W, dimensions = 1,675 m × 0,992 m
**Corrigé :** $N_{panneaux} = \frac{250000}{320} = 782$ panneaux ; superficie = $782 \times 1{,}66 = 1298$ m² ≈ 1300 m² (valeur constructeur confirmée).

### Q2 — Paramétrage du modèle d'une cellule PV
**Source :** E2_Sujet_2021 (Q12), Rapport_Jury_2021
**Énoncé :** « Indiquer les valeurs $I_{sc}$ et $V_{oc}$ à renseigner dans le modèle d'une cellule, sachant que le panneau contient 60 cellules en série. »
**Données :** $I_{sc\,panneau} = 9{,}76$ A, $V_{oc\,panneau} = 40{,}96$ V, 60 cellules série
**Corrigé :** Cellules en série : courant identique → $I_{sc\,cell} = 9{,}76$ A ; tensions s'ajoutent → $V_{oc\,cell} = 40{,}96 / 60 = 0{,}683$ V.

### Q3 — Dimensionnement des entrées onduleur (MPPT)
**Source :** E2_Sujet_2021 (Q13), Rapport_Jury_2021
**Énoncé :** « Définir le nombre de panneaux $N_s$ à connecter en série sur chaque entrée. En déduire la puissance MPPT, la tension MPPT et le courant MPPT. »
**Données :** 782 panneaux, 5 onduleurs × 6 entrées = 30 groupes ; $V_{MPP} = 34{,}32$ V, $I_{MPP} = 9{,}34$ A, $P_{crête} = 320$ W
**Corrigé :** $N_{panneaux/groupe} = 782/30 = 26$ ; $P_{MPP} = 26 \times 320 = 8320$ W/entrée ; $V_{MPP} = 26 \times 34{,}32 = 892$ V ; $I_{MPP} = 9{,}34$ A. Vérification : valeurs compatibles avec les plages de l'onduleur.

### Q4 — Algorithme MPPT (perturbation et observation)
**Source :** E2_Disciplinaire_IE_2025 (Q17, Q18), Rapport_Jury_2025
**Énoncé :** « Indiquer le signe de la variation de puissance dP dans les deux cas P1 (U1 = 195 V, I1 = 7,5 A) et P2 (U2 = 340 V, I2 = 7,5 A) après application de ΔV > 0. Expliquer comment le régulateur MPPT opère. »
**Corrigé :** Cas P1 : point avant le MPP ($U_{MPP} = 317$ V) → $dP > 0$ → continuer dans le même sens (augmenter la tension). Cas P2 : point après le MPP → $dP < 0$ → inverser (réduire la tension). Le régulateur ajuste le rapport cyclique du hacheur jusqu'à $dP = 0$ (point MPP).

### Q5 — Bilan énergétique d'une micro-centrale hydraulique
**Source :** E2_Sujet_2021 (Q5, Q6), Rapport_Jury_2021
**Énoncé :** « Déterminer l'énergie électrique disponible produite à partir de l'énergie potentielle. Comparer à la consommation journalière du village (580 kW·h). »
**Données :** $E_p = 318{,}8$ kW·h, rendement global turbinage = 78 %
**Corrigé :** $E_{élec} = 318{,}8 \times 0{,}78 = 248{,}7$ kW·h. Rapport : 248,7/580 = 43 %. La micro-STEP ne couvre que 43 % des besoins journaliers ; le complément est assuré par les panneaux PV.

### Q6 — Comparaison de filières (cogénération / PV / turbine)
**Source :** E2_Disciplinaire_IE_2022 (Q19), Rapport_Jury_2022
**Énoncé :** « Comparer les trois modes de production autonomes (module Peltier, micro turbine-alternateur, panneaux photovoltaïques) en établissant la liste des avantages et inconvénients. »
**Corrigé :** Voir tableau section 1.4. PV : meilleur compromis pour un usage décentralisé. Micro-turbine : plus régulier que PV mais dépend de la disponibilité en gaz ou en eau. Peltier : très faible rendement, justifié uniquement en milieu extrême (absence de tout autre source).

---

## 3. ATTENTES DU JURY

### Rapport_Jury_2021 (micro-STEP + PV)
> « L'objectif de cette partie est de valider le dimensionnement de la centrale solaire et vérifier sa capacité à produire suffisamment d'énergie. »
> « Les candidats se sont contentés de lire les valeurs sur les courbes sans effectuer la correction en température demandée pour la question 14. »
> « Le jury insiste sur la nécessité de justifier le choix de l'onduleur en vérifiant que les valeurs de tension et de courant calculées sont bien dans les plages admissibles de l'onduleur. »

**Implication candidat :** Savoir lire et interpoler les courbes I=f(U) et P=f(U) d'un champ PV. Toujours corriger la puissance en température. Vérifier explicitement la compatibilité entre les valeurs calculées ($V_{MPP}$, $I_{MPP}$) et les plages de l'onduleur.

### Rapport_Jury_2025 (MPPT)
> « MPPT : Maximum Power Point Tracking (à la recherche du point maximum de puissance). Cette commande permet d'extraire le maximum de puissance sur une installation photovoltaïque. »
> « La stratégie de commande est basée sur la mesure de U et I et du calcul de P. Une boucle permet d'augmenter ou de diminuer le rapport cyclique du hacheur en fonction de l'évolution de dP jusqu'à obtenir le point de la puissance maximum (dP = 0). »

**Implication candidat :** Savoir expliquer le principe de l'algorithme P&O en deux à trois phrases. Relier le rapport cyclique du hacheur à la position sur la courbe P=f(U) du panneau.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Paramètre | Valeur typique | Source |
|---|---|---|
| Puissance crête panneau | 320 W | E2_Sujet_2021, E2_Disciplinaire_IE_2025 |
| $I_{sc}$ panneau (STC) | 9,76 A | Rapport_Jury_2021 |
| $V_{oc}$ panneau (STC) | 40,96 V | Rapport_Jury_2021 |
| $V_{MPP}$ panneau (STC) | 34,32 V | Rapport_Jury_2021 |
| $I_{MPP}$ panneau (STC) | 9,34 A | Rapport_Jury_2021 |
| Surface d'un panneau 320 W | 1,66 m² | E2_Sujet_2021 |
| Nombre panneaux pour 250 kW | 782 panneaux sur 1300 m² | Rapport_Jury_2021 |
| Chute de puissance PV à +25°C | -10 % | Rapport_Jury_2021 |
| Hauteur de chute micro-STEP | 130 m | E2_Sujet_2021 |
| Volume réservoir micro-STEP | 1000 m³ (utile 90 %) | E2_Sujet_2021 |
| Débit pompe micro-STEP | 160 m³·h$^{-1}$ | Rapport_Jury_2021 |
| Puissance absorbée pompe 90 kW | 76 kW (sur courbe) | Rapport_Jury_2021 |
| HMT vue par la pompe | 135 m | E2_Sujet_2021 |
| Rendement global turbinage | 78 % | E2_Sujet_2021 |
| Rendement cycle complet STEP | 58 % | Rapport_Jury_2021 |
| Puissance MPPT par entrée onduleur | 8320 W (26 panneaux) | Rapport_Jury_2021 |
| Tension MPPT par entrée onduleur | 892 V (26 × 34,32 V) | Rapport_Jury_2021 |
| Tension bus DC installation PV isolée | 48 V | E2_Disciplinaire_IE_2025 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Oublier la correction en température** : lire la puissance sur la courbe P=f(U) à 25°C, puis corriger pour la température réelle. Un panneau à 50°C produit 10 % de moins qu'à 25°C pour les modèles courants. Rapport_Jury_2021 : « les candidats ne corrigent pas ».

2. **Erreur sur les cellules en série dans un panneau** : le courant d'une cellule = courant du panneau ; la tension d'une cellule = tension du panneau divisée par le nombre de cellules. Ne pas confondre avec l'association de panneaux en série (qui, là, additionne les tensions des panneaux).

3. **Ne pas vérifier la compatibilité avec l'onduleur** : après avoir calculé $V_{MPP}$ et $I_{MPP}$ de la série de panneaux, vérifier que ces valeurs sont dans les plages min–max de l'onduleur (tension d'entrée MPP, courant d'entrée max). L'omission est signalée comme lacune fréquente.

4. **Confusion P\&O : le sens de la perturbation** : si $dP > 0$ après $+\Delta U$, continuer dans le même sens. Si $dP < 0$, inverser. Beaucoup de candidats inversent la logique.

5. **Rendement de la STEP** : calculer séparément le rendement de turbinage et le rendement global du cycle. Ne pas affirmer que la STEP est très efficace sans citer le chiffre ($\approx 58\%$), et toujours relativiser : « peu performant, mais écologique et préférable à des batteries supplémentaires ».

6. **Unités de la puissance du vent** : $P \propto v^3$ — si la vitesse double, la puissance est multipliée par 8. Erreur fréquente : appliquer un facteur 2 au lieu de 8.

7. **DFIG vs MAS classique** : la DFIG est une MAS à rotor bobiné dont le rotor est connecté au réseau via un convertisseur, permettant un fonctionnement à vitesse variable. Ne pas confondre avec une MAS à cage (rotor en court-circuit), utilisée à vitesse fixe ou semi-variable.

8. **Limite de Betz** : prendre $C_p = 0{,}593$ pour une éolienne réelle. La limite de Betz est un maximum théorique ; une éolienne tripale atteint 0,4 à 0,5, et seulement autour de sa vitesse spécifique optimale.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T15 (Stockage)** : la centrale PV + STEP = système combiné production + stockage (E2_Sujet_2021). Les batteries Li-Ion servent de complément ou d'alternative à la STEP (E2_Disciplinaire_IE_2025). L'hydrogène (électrolyseur + pile à combustible) est une troisième forme de stockage longue durée.
- **T14 (Variation de vitesse)** : l'onduleur de l'installation PV a la même structure de base qu'un onduleur de variateur de fréquence (pont MLI). Le THD de tension produit par l'onduleur PV est un critère de qualité (E2_Disciplinaire_IE_2025, Q23 : THD = 0,48 → signal non sinusoïdal).
- **T17 (Distribution/Sécurité)** : le schéma de liaison à la terre (SLT) de type TT est prescrit dans E2_Sujet_2021 (Q19) pour le circuit de pompage. Le choix du DDR et du disjoncteur de protection du variateur de pompe découle directement du SLT.
- **Électronique de puissance** : hacheur élévateur comme convertisseur MPPT (E2_Disciplinaire_IE_2025, Q19) ; onduleur monophasé pour distribution locale (E2_Disciplinaire_IE_2025, Q20–Q23) ; pont redresseur pour charge de batterie depuis réseau AC (E1_Sujet_2026, partie E).
