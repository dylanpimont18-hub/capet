# T14 — Variation de vitesse et de couple des machines

Sources analysées : E1_Sujet_2024, Rapport_Jury_2024, E2_Sujet_2021, Rapport_Jury_2021, E2_Sujet_2026_BAC3, E1_Sujet_2026, E2_Sujet_2018, Rapport_Jury_2018, E1_Sujet_2020, Rapport_Jury_2020.

---

## 1. FORMULES ET COURS

### 1.1 Vitesse synchrone et glissement de la machine asynchrone (MAS)
$$N_s = \frac{60 \cdot f}{p}$$
- $N_s$ : vitesse des champs tournants (tr/min), $f$ : fréquence statorique (Hz), $p$ : nombre de paires de pôles
- Formule fondamentale du variateur scalaire : pour maintenir le flux, on impose $V_s / f = \text{constante}$
- Fréquence d'apparition : **très élevée** — présente dans tous les sujets comportant une MAS (2021, 2024, 2026)
- Source : E1_Sujet_2024 (A3) : « $N_s = 1500$ tr/min pour $f = 50$ Hz et $p = 2$ »

**Glissement nominal :**
$$g = \frac{N_s - N}{N_s}$$
- Source : E1_Sujet_2024 (A3) : $N = 1400$ tr/min, $N_s = 1500$ tr/min → $g = 0{,}067$

### 1.2 Couple électromagnétique — modèle simplifié (glissement faible)
$$C_{em} = \frac{3p}{R'_r} \cdot \left(\frac{V_s}{\omega_s}\right)^2 \cdot \omega_r$$
où $\omega_r = \omega_s - \omega$ est la pulsation de glissement.
- Pour $g \approx 0$ : $C_{em} \approx A \cdot \omega_r$ avec $A = \frac{3p}{R'_r} \cdot \left(\frac{V_s}{\omega_s}\right)^2$
- Source : E1_Sujet_2024 (C1, C2) — démonstration complète demandée au candidat

**Équation mécanique (domaine temporel) :**
$$C_{em}(t) - C_r(t) = J \frac{d\Omega}{dt} + f \Omega$$

**Fonction de transfert mécanique (domaine de Laplace) :**
$$\Omega(p) = \frac{K_{meca}}{1 + \tau_{meca} p} \cdot [C_{em}(p) - C_r(p)]$$
avec $K_{meca} = \frac{1}{f}$ et $\tau_{meca} = \frac{J}{f}$
- Source : E1_Sujet_2024 (C3, C4) — données numériques : $K_{meca} = 250$, $\tau_{meca} = 8{,}5$ s

### 1.3 Commande scalaire V/f
- Principe : maintenir le rapport $V_s / f_s = \text{constante}$ pour conserver le flux magnétique
- Mise en œuvre via un variateur de fréquence (onduleur de tension + MLI)
- Source : E1_Sujet_2024 (C1–C12) et Rapport_Jury_2024 (partie C) : « le contrôle de la vitesse d'extraction de l'air peut être réalisé efficacement via une commande scalaire de la machine asynchrone et une boucle d'asservissement »
- Boucle de vitesse avec correcteur PI : $H_{BF}(p) = \frac{1}{1 + \frac{2m}{\omega_0} p + \frac{1}{\omega_0^2} p^2}$

### 1.4 Taux de distorsion harmonique (THD) — onduleur MLI
$$THD = \frac{\sqrt{I_2^2 + I_3^2 + \cdots + I_n^2}}{I_1}$$
- Commande pleine onde : $THD = 0{,}59$ (59 %) → ne respecte pas la norme IEC/EN 61000-2-2 (< 25 %)
- Commande MLI ($f_p = 6$ kHz) : $THD = 0{,}25$ (25 %) → conforme
- Source : E1_Sujet_2024 (B10, B11) et Rapport_Jury_2024 (B10) — calcul numérique complet

### 1.5 Structure interne d'un variateur de fréquence
Structure : **Pont redresseur → Cellule de filtrage (bus DC) → Onduleur MLI → MAS**
- Source : E1_Sujet_2024 (figure 7) ; E2_Sujet_2026_BAC3 : onduleur MLI pour moteurs ZF 125 kW

### 1.6 Puissances dans la MAS
$$P_a = 3 V_s I_s \cos\varphi_{mot}$$
$$P_{jr} = g \cdot P_{em}$$
$$P_u = P_{em} - P_{pm} = P_a - P_{js} - P_{jr} - P_{pm}$$
- Source : E1_Sujet_2024 (A5, A6) — données : $I_s = 229$ A, $\cos\varphi = 0{,}85$, $V_s = 230$ V

### 1.7 Sélection d'un variateur de vitesse (dimensionnement)
- Critère principal : puissance moteur + surcharge admissible
- Exemple ATV630 (Schneider) : pour 90 kW, surcharge 150 % (Heavy Duty) → référence ATV630C11N4
- Courant nominal moteur : $I_{n,moteur} = \frac{P_u}{\eta \cdot \sqrt{3} \cdot U \cdot \cos\varphi}$
- Source : Rapport_Jury_2021 (Q16, Q17, Q18) — détail complet

### 1.8 Freinage par récupération / 4 quadrants
- Bus ZF AVE 130 (2026) : « moteurs assurent la propulsion avec une plus forte puissance de freinage régénératif »
- Essieu ZF 2 × 125 kW, tension batterie 600 V
- Source : E2_Sujet_2026_BAC3 (présentation, Q A10) : identification des quadrants de fonctionnement

---

## 2. QUESTIONS TYPES (max 6, les plus représentatives)

### Q1 — Glissement et vitesse synchrone (récurrent)
**Source :** E1_Sujet_2024 (A3)
**Énoncé :** « À l'aide du document technique DT1, déterminer l'expression littérale et calculer la vitesse des champs tournants $N_s$ en tr/min. En déduire la valeur du glissement nominal $g$. »
**Données :** $f = 50$ Hz, $p = 2$, $N = 1400$ tr/min
**Corrigé :** $N_s = \frac{60 \times 50}{2} = 1500$ tr/min ; $g = \frac{1500 - 1400}{1500} = 0{,}067$

### Q2 — Calcul du couple et modèle scalaire
**Source :** E1_Sujet_2024 (C1–C4)
**Énoncé :** « Montrer que le couple $C_{em}$ peut se mettre sous la forme $C_{em} = \frac{3p}{R'_r} \cdot \left(\frac{V_s}{\omega_s}\right)^2 \cdot \omega_r$. »
**Données :** modèle circuit équivalent MAS, $V_s = 230$ V, $p = 2$
**Corrigé :** Partir de l'expression générale du couple, poser $g \approx 0$, factoriser : $C_{em} = A \cdot \omega_r$ avec $A = \frac{3p \cdot V_s^2}{R'_r \cdot \omega_s^2}$

### Q3 — THD et choix commande MLI
**Source :** E1_Sujet_2024 (B10–B13) et Rapport_Jury_2024
**Énoncé :** « Calculer le THD du courant réseau dans les deux cas (pleine onde et MLI $f_p = 6$ kHz). Conclure sur la conformité à la norme IEC/EN 61000-2-2. »
**Données :** Harmoniques cas 1 : $I_1 = 170$ A, $I_3 = 95$ A, $I_5 = 27$ A, $I_7 = 27$ A, $I_9 = 20$ A ; Cas 2 : $I_1 = 170$ A, $I_3 = 37$ A, $I_5 = 22$ A
**Corrigé :** Cas 1 : $THD = \frac{\sqrt{95^2 + 27^2 + 27^2 + 20^2}}{170} = 0{,}59$ → non conforme. Cas 2 : $THD = \frac{\sqrt{37^2 + 22^2}}{170} = 0{,}25$ → conforme (< 25 %).

### Q4 — Choix et dimensionnement d'un variateur ATV630
**Source :** Rapport_Jury_2021 (Q15 à Q18)
**Énoncé :** « Citer deux avantages du variateur de vitesse et indiquer les paramètres physiques contrôlables. Choisir le modèle ATV630 pour un moteur de 90 kW, surcharge 150 %. »
**Données :** $P_u = 90$ kW, $U = 400$ V, $\cos\varphi = 0{,}86$, $\eta = 0{,}942$
**Corrigé :** Avantages : contrôle vitesse/couple, économie d'énergie, rampe d'accélération douce. Référence : ATV630C11N4, $I_n = 170$ A. Disjoncteur : NSX250N MA220, ICU = 50 kA.

### Q5 — Boucle d'asservissement de vitesse scalaire
**Source :** E1_Sujet_2024 (C5–C11) et Rapport_Jury_2024
**Énoncé :** « Déterminer la fonction de transfert en boucle fermée $H_{BF}(p)$. Exprimer $m$ et $\omega_0$ en fonction de $K_p$, $K_i$, $K_{meca}$, $\tau_{meca}$. »
**Données :** $m = 1$, $T_r = 1$ s, $K_{meca} = 250$, $\tau_{meca} = 8{,}5$ s
**Corrigé :** $K_p = 0{,}35$, $K_i = 2{,}5$ ; dépassement nul, erreur statique nulle, marge de phase 180° → cahier des charges respecté.

### Q6 — Choix motorisation, variateur 4 quadrants (bus électrique 2026)
**Source :** E2_Sujet_2026_BAC3 (Q A10) et E1_Sujet_2026
**Énoncé :** « Identifier les grandeurs électriques $(U, I)$ associées aux grandeurs mécaniques $(C, \Omega)$ dans une machine à courant continu. Hachurer les quadrants de fonctionnement et proposer une structure de variateur adaptée. »
**Données :** actionneur bi-directionnel, fonctionnement moteur uniquement
**Corrigé :** Deux sens de rotation → quadrants 1 et 3 → variateur 2 quadrants (hacheur à 4 interrupteurs) ou onduleur triphasé si MAS.

---

## 3. ATTENTES DU JURY (citations directes des Rapport_Jury)

### Rapport_Jury_2021
> « Dans cette partie, le candidat est amené à choisir le variateur de fréquence et sa protection, puis, à réaliser une partie du schéma électrique du circuit de pompage en montrant les interactions entre le variateur et l'automate. »
> « Les candidats se sont limités à proposer une référence de composants parfois incomplète sans justification, sans indiquer clairement les critères de choix. »
> « Le jury constate que beaucoup de candidats ne sont pas à l'aise dans la réalisation de schémas électriques. Un candidat au CAPET doit être capable de câbler une entrée ou une sortie TOR-analogique d'un automate industriel programmable, ainsi que la partie commande d'un variateur de fréquence. »

**Implication candidat :** Maîtriser le câblage du circuit de puissance ET de commande d'un variateur ATV-type. Justifier le choix (puissance, surcharge, calibre disjoncteur associé). Citer les critères (HD/ND, ICU).

### Rapport_Jury_2024
> « Le contrôle de la vitesse d'extraction de l'air peut être réalisé efficacement via une commande scalaire de la machine asynchrone et une boucle d'asservissement. L'objectif de cette partie est d'étudier les paramètres à respecter comme l'erreur statique, le dépassement et la marge de phase. »
> « L'objectif de cette partie est de dimensionner le variateur et du moto-extracteur électrique pour optimiser la consommation énergétique de l'extracteur d'air. »

**Implication candidat :** Savoir démontrer le modèle scalaire (V/f), calculer les gains d'un correcteur PI, analyser un diagramme de Bode pour la marge de phase.

### Rapport_Jury_2020
> « Le jury note ici les progrès des candidats quant aux conversions d'unités mais déplore que des problématiques simples, comme le dimensionnement d'une batterie, ne soient pas maîtrisées. »

**Implication candidat :** Le dimensionnement énergétique (batterie + variateur) constitue un ensemble cohérent — ne pas traiter la partie variateur isolément.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Paramètre | Valeur typique | Source |
|---|---|---|
| Tension composée réseau | 400 V (triphasé) | Tous sujets |
| Tension simple | 230 V | E1_Sujet_2024 |
| Fréquence réseau | 50 Hz | Tous sujets |
| Courant nominal moteur 100 kW | 229 A | E1_Sujet_2024 |
| $\cos\varphi$ moteur | 0,85 | E1_Sujet_2024 |
| Nombre de paires de pôles | $p = 2$ | E1_Sujet_2024 |
| Vitesse synchrone | 1500 tr/min | E1_Sujet_2024 |
| Vitesse nominale | 1400 tr/min | E1_Sujet_2024 |
| Glissement nominal | 0,067 (6,7 %) | E1_Sujet_2024 |
| Couple utile nominal | 686 N·m | Rapport_Jury_2024 |
| $K_{meca}$ | 250 | E1_Sujet_2024 |
| $\tau_{meca}$ | 8,5 s | E1_Sujet_2024 |
| Surcharge variateur HD | 150 % | Rapport_Jury_2021 |
| ICU disjoncteur variateur | 50 kA | Rapport_Jury_2021 |
| Fréquence de découpage MLI | 6 000 Hz (typique) | E1_Sujet_2024 |
| THD admissible (norme IEC 61000-2-2) | < 25 % | E1_Sujet_2024 |
| Fréquence modulante bus électrique | $f_0 = 700$ Hz | E2_Sujet_2026_BAC3 |
| Puissance moteur bus ZF AVE 130 | 2 × 125 kW | E2_Sujet_2026_BAC3 |
| Tension batterie bus électrique | 600 V | E2_Sujet_2026_BAC3 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Pas de justification du choix du variateur** : les candidats donnent une référence sans expliquer les critères (puissance > $P_u$, surcharge ND ou HD, tension réseau). Rapport_Jury_2021 : « sans justification, sans indiquer clairement les critères de choix ».

2. **Confusion entre commande scalaire et vectorielle** : la commande scalaire V/f suffit pour les applications à couple variable (pompe, ventilateur). La commande vectorielle FOC n'est pas exigée en calcul mais doit être citée comme alternative pour couples dynamiques élevés.

3. **Câblage du circuit de commande variateur** : le jury 2021 insiste explicitement sur l'obligation de savoir câbler les entrées TOR/analogiques automate vers le variateur. Pièges : sens de rotation (LI1/LI2), référence de vitesse (entrée 0–10 V ou 4–20 mA), retour de défaut.

4. **Calcul THD** : oublier de mettre les harmoniques au carré sous la racine, ou diviser par $I_1$ au lieu de l'amplitude totale. Attention : l'harmonique de rang 1 est le fondamental.

5. **Unités angulaires** : mélanger tr/min et rad/s. $\Omega = \frac{2\pi N}{60}$. Rapport_Jury_2020 : « déplore que des conversions d'unités ne soient pas maîtrisées ».

6. **Boucle de vitesse** : ne pas confondre $K_{meca} = 1/f$ (frottement visqueux) avec le gain statique global. Ne pas oublier le terme de charge $C_r(p)$ dans la fonction de transfert en boucle ouverte.

7. **Freinage régénératif** : si le sujet mentionne 4 quadrants, identifier les quadrants I, II, III, IV (couple/vitesse) et vérifier que la structure matérielle le permet (onduleur réversible ou résistance de freinage).

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T15 (Stockage)** : les sujets de bus électrique (2026) combinent variateur + batterie. L'énergie récupérée au freinage se stocke dans la batterie. Voir E2_Sujet_2026_BAC3.
- **T17 (Distribution/Sécurité)** : le variateur impose un disjoncteur magnétique MA (protection court-circuit uniquement, la protection thermique est assurée par le variateur). Régime TT → DDR obligatoire. Voir Rapport_Jury_2021 (Q17) et E2_Sujet_2021 (Q19).
- **T16 (ENR)** : onduleur PV ↔ onduleur variateur — même structure de base (pont MLI), mais le sens du flux d'énergie est inversé. MPPT pour PV = analogie avec régulation de vitesse optimale.
- **Systèmes asservis** : la boucle de vitesse scalaire (E1_Sujet_2024, partie C) mobilise les notions de correcteur PI, fonction de transfert du second ordre, marge de phase.
