# T17 — Distribution et sécurité électrique, régimes de terre

Sources analysées : E2_Sujet_2017 (spa), E2_Sujet_2021 (micro-STEP), E1_Sujet_2024 (extracteur), Rapport_Jury_2024, E2_Sujet_2018 (parafoudres), E2_Disciplinaire_IE_2024, E2_Sujet_2020 (dessalinisateur), Rapport_Jury_2020.

---

## 1. FORMULES ET COURS

### 1.1 Schémas de liaison à la terre (SLT / régimes de neutre)

Les trois régimes de neutre normalisés par la NF C 15-100 :

**Régime TT :**
- Neutre du transformateur HTA/BT mis directement à la terre (côté source)
- Masses des récepteurs reliées à une prise de terre indépendante (côté utilisateur)
- Protection contre les contacts indirects : **DDR (interrupteur différentiel résiduel)** obligatoire
- Application typique : installations domestiques et tertiaires classiques, installations isolées
- Source : E2_Sujet_2021 (Q19) : « le schéma des liaisons à la terre est de type TT »

**Régime TN :**
- Neutre de la source relié directement à la terre
- Masses des récepteurs reliées à cette même terre (neutre) par un conducteur PE (ou PEN)
- **TN-S** : neutre (N) et protecteur (PE) séparés sur tout le circuit → DDR possible
- **TN-C** : neutre et protecteur confondus dans un conducteur PEN → DDR interdit sur ce tronçon
- Protection contre les contacts indirects : disjoncteur ou fusible (courant de défaut élevé → coupure rapide)
- Source : E2_Sujet_2018 (DRS7 parafoudres) : tableau de compatibilité TT / TN-S / TN-C / IT

**Régime IT :**
- Neutre de la source impédant (isolé ou mis à la terre via une impédance élevée)
- Masses reliées à la terre côté utilisateur
- Un premier défaut ne provoque pas de coupure : simple signalisation par le CPI (Contrôleur Permanent d'Isolement)
- Protection : au deuxième défaut → coupure par disjoncteur ou fusible
- Applications : blocs opératoires, sites industriels exigeant la continuité de service
- Source : E2_Sujet_2018 (DRS7) : tableau compatibilité parafoudres selon SLT

**Tableau récapitulatif :**

| Régime | Neutre source | Masses récepteurs | Protection contacts indirects | Applications typiques |
|---|---|---|---|---|
| TT | Terre directe | Terre indépendante | DDR obligatoire | Résidentiel, tertiaire |
| TN-S | Terre directe | Reliées au neutre (PE séparé) | Disjoncteur (fort $I_{cc}$) | Industriel, scolaire |
| TN-C | Terre directe | Reliées au neutre (PEN) | Disjoncteur (DDR interdit) | Anciens réseaux |
| IT | Impédant | Terre | CPI + coupure au 2e défaut | Médical, industrie critique |

### 1.2 Dispositifs différentiels résiduels (DDR)

**Principe :** mesure la somme algébrique des courants dans tous les conducteurs (phases + neutre). Si $\sum i \neq 0$, un courant de fuite vers la terre est détecté → déclenchement.

**Sensibilités normalisées :**
| Sensibilité | Usage | Norme |
|---|---|---|
| 30 mA (haute sensibilité) | Protection des personnes | NF C 15-100 obligatoire en TT |
| 300 mA ou 500 mA | Protection incendie, sélectivité | — |
| 1 A ou plus | Protection de tête (sélectivité ampèremétrique) | — |

**Sélectivité différentielle :**
- Utiliser des DDR de sensibilité croissante vers la source (30 mA en aval, 300 mA en amont) ou des DDR temporisés en amont
- Source : E2_Sujet_2017 (partie B1) : « la protection des personnes est assurée dans l'armoire du spa par un interrupteur différentiel »

### 1.3 Disjoncteur — caractéristiques et sélectivité

**Déclencheurs :**
- **Déclencheur thermique** (bimétallique) : protège contre les surcharges (courant > $I_{th}$, action différée)
- **Déclencheur magnétique** : protège contre les courts-circuits (courant > $I_{rm}$, action instantanée)
- **Disjoncteur magnétique seul (MA)** : uniquement protection court-circuit — utilisé en amont d'un variateur de fréquence qui assure lui-même la protection thermique

**Caractéristiques du pouvoir de coupure :**
- $I_{cu}$ (Ultimate breaking capacity) : pouvoir de coupure ultime en kA
- $I_{cs}$ (Service breaking capacity) : pouvoir de coupure en service
- Exemple : NSX250N MA220 → $I_{cu} = 50$ kA, seuil magnétique $I_{rm} = 2860$ A
- Source : Rapport_Jury_2021 (Q17) et Rapport_Jury_2024

**Sélectivité ampèremétrique :**
- Le disjoncteur aval déclenche avant le disjoncteur amont si les courants de réglage sont correctement échelonnés
- $I_{rm,aval} < I_{rm,amont}$ et les courbes temps-courant ne se croisent pas dans la zone de défaut attendue

### 1.4 Chute de tension et choix de section de câble (NF C 15-100)

**Chute de tension relative (en %) :**
$$\Delta U\% = \frac{\sqrt{3} \cdot I \cdot L \cdot (R_u \cos\varphi + X_u \sin\varphi)}{U_D} \times 100$$

Pour des câbles de faible inductance (BT, courte distance) :
$$\Delta U \approx \frac{\sqrt{3} \cdot I \cdot R_u \cdot L}{U_D}$$

où $R_u$ est la résistance linéique du conducteur (Ω·km$^{-1}$) et $L$ la longueur (m).

**Valeurs limites imposées par la NF C 15-100 :**
| Domaine | Limite $\Delta U\%$ |
|---|---|
| Domaine public — éclairage | 3 % |
| Domaine public — autres usages | **5 %** |
| Installation intérieure privée | 3 % (éclairage) / 5 % (autres) |

**Remède si dépassement :** augmenter la section des conducteurs pour réduire $R_u$ (et $L_u$).
- Source : E1_Sujet_2024 (B9), Rapport_Jury_2024 (B9) : « la norme NFC 15-100 impose une chute de tension inférieure à 5 %. Pour diminuer la chute de tension, augmenter la section du câble. »

**Calcul de la résistance et de l'inductance par mètre :**
$$R_u = \frac{\rho}{S}, \quad L_u = f(S, \text{géométrie})$$

- $\rho_{cuivre} \approx 1{,}7 \times 10^{-8}$ Ω·m, $\rho_{aluminium} \approx 2{,}8 \times 10^{-8}$ Ω·m
- Source : E1_Sujet_2024 (B5) : « calculer $R_L$ et $L_L$ pour chaque fil de ligne de longueur 850 m »

### 1.5 Bilan de puissance et choix de l'abonnement

**Puissances en monophasé et triphasé :**
$$P = U \cdot I \cdot \cos\varphi \quad \text{(monophasé)}$$
$$P = \sqrt{3} \cdot U_D \cdot I \cdot \cos\varphi \quad \text{(triphasé)}$$
$$Q = \sqrt{3} \cdot U_D \cdot I \cdot \sin\varphi, \quad S = \sqrt{3} \cdot U_D \cdot I$$

**Courant sur une phase :**
$$I = \frac{P}{U \cdot \cos\varphi} \quad \text{(monophasé)}$$

**Abonnement :** la puissance apparente souscrite (en kVA) doit couvrir la puissance apparente totale maximale, en tenant compte du déséquilibre éventuel entre phases.

- Source : E2_Sujet_2017 (B2.3) : « en tenant compte du déséquilibre lors du fonctionnement du réchauffeur, déterminer le nouvel abonnement nécessaire »

### 1.6 Parafoudres — protection contre les surtensions d'origine atmosphérique

**Types normalisés :**
- **Type 1** (protection de tête, $I_{imp}$ : kA) : en entrée d'installation, coordonné avec le paratonnerre
- **Type 2** (protection secondaire, $I_n$ : kA) : en aval du TGBT, gamme PF Merlin Gérin
- **Type 3** (protection fine) : au plus près des équipements sensibles

**Compatibilité selon le SLT :**
- TT et TN-S : protection en mode commun ET en mode différentiel possible
- TN-C : protection en mode commun uniquement (pas de mode différentiel entre N et PE car confondus)
- IT : protection en mode commun

- Source : E2_Sujet_2018 (DRS7) : tableau de compatibilité TT/TN-S/TN-C/IT

### 1.7 Production et transport de l'énergie

*(complément du référentiel, 2026-11-10 — notion hors sujets 2013–2026 sauf mention)*

**Pertes Joule d'une ligne triphasée transportant une puissance P :**
$$P_J = \frac{R \, P^2}{U^2 \cos^2\varphi}$$
- Valable pour une ligne triphasée équilibrée de résistance R par phase, U étant la tension composée

---

## 2. QUESTIONS TYPES (max 6)

### Q1 — Identification du SLT et choix du DDR
**Source :** E2_Sujet_2021 (Q19), E2_Sujet_2017 (B1.3)
**Énoncé :** « Le schéma des liaisons à la terre est de type TT. Justifier la présence d'un interrupteur différentiel dans l'installation. Indiquer la sensibilité à retenir pour assurer la protection des personnes. »
**Corrigé :** En régime TT, le courant de défaut à la terre est limité par les résistances de prise de terre (faible valeur) → le disjoncteur ne peut pas détecter le défaut seul. Un DDR 30 mA est obligatoire pour la protection des personnes. Le DDR mesure le courant différentiel $I_{diff} = \sum i_{conducteurs}$ et déclenche dès 30 mA.

### Q2 — Calcul de la chute de tension et conformité NF C 15-100
**Source :** E1_Sujet_2024 (B5 à B9), Rapport_Jury_2024 (B9)
**Énoncé :** « Exprimer et calculer la chute de tension $\Delta U$ en proportion de $U_D$. Indiquer si la valeur est conforme à la norme NF C 15-100 (domaine public, autre usage). Dans le cas contraire, proposer une solution. »
**Données :** $I_{tot} = 258$ A, $\cos\varphi = 0{,}85$, $L = 850$ m, $R_u$ et $L_u$ donnés
**Corrigé :** $\Delta U\% = \frac{\sqrt{3} \cdot I_{tot} \cdot L \cdot (R_u \cos\varphi + X_u \sin\varphi)}{U_D} \times 100$. Si $\Delta U > 5\%$ → non conforme → augmenter la section du câble (réduire $R_u$).

### Q3 — Bilan de puissance et déséquilibre entre phases
**Source :** E2_Sujet_2017 (B2.2, B2.3)
**Énoncé :** « Faire un bilan de puissance pour les différents cas de fonctionnement. Déterminer le courant maximal sur chaque phase et choisir l'abonnement. »
**Données :** Réchauffeur 3 kW sur phase 1, pompes 1 et 2 sur phases 2 et 3 ($\cos\varphi = 0{,}86$), pompe circulation sur phase 1 ($\cos\varphi = 0{,}8$)
**Corrigé :** Calculer $I_{phase}$ pour chaque récepteur : $I = P / (U \cdot \cos\varphi)$. La phase 1 reçoit le réchauffeur + la pompe de circulation → courant le plus élevé → dimensionner l'abonnement sur la phase la plus chargée, avec prise en compte du déséquilibre.

### Q4 — Choix du disjoncteur associé à un variateur de fréquence
**Source :** Rapport_Jury_2021 (Q17), Rapport_Jury_2024
**Énoncé :** « Déterminer la référence complète du disjoncteur à associer au variateur ATV630C11N4. Indiquer et développer les types de protection assurés. »
**Données :** $I_{cc\,max\,variateur} = 50$ kA
**Corrigé :** Référence : NSX250**N** MA220. La lettre **N** correspond à $I_{cu} = 50$ kA (pouvoir de coupure adapté). Déclencheur **MA** = magnétique seul (seuil $I_{rm} = 2860$ A) : uniquement protection court-circuit. La protection thermique est assurée par le variateur lui-même (paramètre $I_{th}$ réglable de 0,2 à 1,1 $I_n$).

### Q5 — Compatibilité parafoudre et SLT
**Source :** E2_Sujet_2018 (DRS7)
**Énoncé :** « Identifier le type de parafoudre adapté à une installation en régime TN-C. Justifier. »
**Corrigé :** En TN-C, les conducteurs N et PE sont confondus dans le conducteur PEN. La protection en mode différentiel (entre phase et neutre) est impossible car il n'y a pas de neutre séparé. Seule la protection en **mode commun** (entre phase et terre) est possible. Choisir un parafoudre de type 2 en mode commun uniquement, avec signalisation.

### Q6 — Sélectivité des protections (disjoncteur + DDR)
**Source :** E2_Sujet_2021 (Q19), NF C 15-100
**Énoncé :** « Justifier le choix d'un interrupteur différentiel 300 mA en tête du tableau et de DDR 30 mA sur chaque départ, dans un schéma TT. »
**Corrigé :** Sélectivité différentielle : les DDR 30 mA en aval déclenchent avant le DDR 300 mA en amont pour les défauts à la terre sur chaque départ. En cas de défaut sur un circuit, seul ce circuit est coupé, les autres restent alimentés. La sélectivité est assurée par le rapport des sensibilités (facteur ≥ 3) et/ou par la temporisation du DDR amont.

---

## 3. ATTENTES DU JURY

### Rapport_Jury_2024 (extracteur d'air — partie B)
> « La chute de tension n'est pas respectée. En effet, dans le domaine public pour un "autre usage", la norme NFC 15-100 impose une chute de tension inférieure à 5 %. Pour diminuer la chute de tension, il est possible de modifier les valeurs de $R_u$ et $L_u$ en augmentant la section du câble. »
> « Le jury rappelle que le calcul de la chute de tension est une application directe de la loi d'Ohm sur la ligne équivalente, et que le résultat doit être comparé explicitement à la limite normative. »

**Implication candidat :** Toujours conclure par rapport à la valeur normative (5 % domaine public, 3 % éclairage). Ne pas oublier la partie réactive ($X_u \sin\varphi$) si le sujet donne l'inductance linéique.

### Rapport_Jury_2021 (choix du disjoncteur variateur)
> « Le jury constate que beaucoup de candidats ne sont pas à l'aise dans la réalisation de schémas électriques et dans le choix du matériel de protection. »
> « Il est impératif de justifier le choix du disjoncteur en citant le pouvoir de coupure, le type de déclencheur et le réglage. »

**Implication candidat :** Pour un disjoncteur associé à un variateur, justifier systématiquement : (1) le pouvoir de coupure vis-à-vis du courant de court-circuit du réseau, (2) le type MA (magnétique seul, car le variateur assure la protection thermique), (3) le seuil $I_{rm}$.

### Rapport_Jury_2020 (sécurité électrique sur bateau)
> « Une critique à la fois qualitative et quantitative était attendue. Le jury déplore des réponses trop évasives sans aucun lien avec les documents techniques. »

**Implication candidat :** Toujours appuyer le choix du SLT ou du matériel par un argument technique précis (valeur numérique, référence normative, explication physique du risque).

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Paramètre | Valeur | Source |
|---|---|---|
| Tension réseau BT | 230 V (monophasé) / 400 V (triphasé) | Tous sujets |
| Fréquence | 50 Hz | Tous sujets |
| Limite $\Delta U$ domaine public (autre usage) | 5 % | NF C 15-100, E1_Sujet_2024 |
| Limite $\Delta U$ éclairage | 3 % | NF C 15-100 |
| Sensibilité DDR protection personnes | 30 mA | NF C 15-100 |
| Sensibilité DDR protection incendie | 300 mA ou 500 mA | NF C 15-100 |
| Longueur câble type dans sujets | 850 m | E1_Sujet_2024 |
| Courant total extracteur | 258 A | E1_Sujet_2024 |
| $\cos\varphi$ pompe d'hydromassage | 0,86 | E2_Sujet_2017 |
| $\cos\varphi$ pompe de circulation | 0,80 | E2_Sujet_2017 |
| Pouvoir de coupure disjoncteur variateur | 50 kA | Rapport_Jury_2021 |
| Seuil magnétique NSX250N MA220 | $I_{rm} = 2860$ A | Rapport_Jury_2021 |
| Réglage thermique variateur | 0,2 à 1,1 $I_n$ | Rapport_Jury_2021 |
| Abonnement spa typique | 18 kVA (triphasé) | E2_Sujet_2017 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Confondre TN-S et TN-C** : en TN-C, le conducteur PEN interdit le DDR sur ce tronçon (courant de mise à la terre passe par le PEN, pas de courant différentiel mesurable). En TN-S, le PE et le N sont séparés → DDR possible.

2. **Omettre le DDR en régime TT** : en TT, le courant de défaut est limité par la résistance de prise de terre (quelques dizaines d'ohms) → courant trop faible pour déclencher un disjoncteur seul → le DDR est indispensable et obligatoire selon NF C 15-100.

3. **Oublier la partie réactive dans la chute de tension** : si $\sin\varphi \neq 0$ et que $X_u$ est fourni, négliger $X_u \sin\varphi$ peut conduire à sous-estimer $\Delta U$ de 10 à 20 % selon la longueur de câble.

4. **Choisir un disjoncteur magnéto-thermique pour un variateur** : le variateur de fréquence assure lui-même la protection thermique du moteur (réglage $I_{th}$). Un disjoncteur magnéto-thermique en amont créerait un double étage thermique pouvant provoquer une décoordination. La norme impose un déclencheur magnétique seul (MA) en amont du variateur.

5. **Appliquer la formule monophasé à un circuit triphasé** : en triphasé, la tension de référence pour le calcul de la chute de tension est la tension composée $U_D$, et le facteur $\sqrt{3}$ doit apparaître dans la formule.

6. **Sélectivité différentielle** : pour assurer la sélectivité, le rapport des sensibilités DDR amont/aval doit être $\geq 3$ (DDR aval 30 mA → DDR amont $\geq$ 90 mA, soit 300 mA). De plus, un DDR sélectif (type S, avec retard) peut être utilisé en amont.

7. **Parafoudre en TN-C** : la protection en mode différentiel est impossible (N et PE confondus). Proposer uniquement mode commun. Erreur fréquente : proposer le même parafoudre qu'en TN-S.

8. **Intérêt de la haute tension** : croire que les pertes en ligne diminuent proportionnellement à la tension. À puissance transportée donnée, les pertes Joule décroissent comme $1/U^2$ : doubler la tension divise les pertes par quatre.

9. **Domaines de tension** : classer le réseau de distribution 20 kV en HTB. Le 20 kV appartient à la HTA (1 à 50 kV) ; la HTB commence au-delà de 50 kV.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T14 (Variation de vitesse)** : le disjoncteur en amont d'un variateur de fréquence (type MA, pouvoir de coupure 50 kA) est un élément de sécurité directement lié à la partie variation de vitesse. Le SLT TT impose un DDR entre le réseau et le variateur pour la protection des personnes. Source : E2_Sujet_2021 (Q19), Rapport_Jury_2021 (Q17).
- **T15 (Stockage)** : le circuit de charge d'une batterie depuis le réseau (redresseur triphasé) est soumis aux mêmes règles NF C 15-100 en matière de chute de tension et de protection différentielle. Source : E1_Sujet_2026 (partie E).
- **T16 (Énergies renouvelables)** : le raccordement d'une installation PV au réseau public impose le choix du SLT et des protections (DDR, disjoncteur d'interconnexion). Un onduleur PV raccordé en TT nécessite un DDR 30 mA. La norme NF C 15-100 s'applique à tout le câblage BT de l'installation.
- **Puissance et facteur de puissance** : la sélection de l'abonnement EDF (puissance souscrite en kVA) implique de calculer la puissance apparente totale, ce qui suppose de maîtriser le triangle des puissances et le facteur de puissance $\cos\varphi$.
- **Qualité de l'énergie** : les harmoniques générées par les variateurs de fréquence (THD courant) peuvent déclencher les DDR par courant différentiel parasite (courant de fuite capacitif vers la terre via les câbles moteur). Utiliser des DDR de type A (sensibles aux composantes continues pulsées) plutôt que des DDR de type AC pour les circuits avec variateurs.
