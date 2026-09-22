# T23 — Capteurs et Conditionnement du Signal
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

### 1.1 Taxonomie des capteurs

| Critère | Catégories |
|---|---|
| Nature | Actif (génère une FEM : thermocouple, piézoélectrique) / Passif (nécessite alimentation : PT100, jauge, potentiomètre) |
| Grandeur mesurée | Température, position, pression, débit, force, luminosité, humidité |
| Signal de sortie | TOR (tout ou rien), analogique continu, courant normalisé 4–20 mA, numérique (OneWire, CANopen) |

### 1.2 Capteurs de température

**PT100 (thermorésistance) :**
- Résistance à 0°C : $R_0 = 100\ \Omega$
- Loi linéarisée : $R_T = R_0(1 + \alpha T)$ avec $\alpha = 3{,}85 \times 10^{-3}\ °\text{C}^{-1}$
- Capteur **passif**, nécessite un pont d'alimentation
- Plage typique : $-200°$C à $+850°$C
- Utilisé en 2022 (TRT200 : sondes PT100 pour surveillance de purge)

**Thermocouple (effet Seebeck) :**
- Capteur **actif** : génère une FEM $e_{AB}$ de quelques mV (ex. type J : $-1$ mV à $+10{,}8$ mV pour $-20°$C à $+200°$C)
- Types usuels : J (Fe/Constantan), K (Chromel/Alumel), E, N, T
- Tolérance type J : $\pm 2{,}5°$C ; plage : $-210°$C à $+1200°$C
- Nécessite un transmetteur (convertisseur mV → 4–20 mA)
- Utilisé en 2024 (armoire électrique, thermocouple type J + transmetteur KOS 839)

**Sensibilité d'un capteur PT100 modélisé par résistance $R_T$ :**
$$\frac{\Delta R_T}{\Delta T} = R_0 \cdot \alpha = 100 \times 3{,}85 \times 10^{-3} = 0{,}385\ \Omega/°\text{C}$$

### 1.3 Capteurs de position et déplacement

**Potentiomètre angulaire (capteur résistif) :**
- Tension de sortie proportionnelle à l'angle
- Capteur **passif**, nécessite une tension d'alimentation $V_{cc}$
- Utilisé en 2026 E1 (mesure de position angulaire de porte de bus)

**Codeur absolu (CANopen, 2014 E1) :**
- Résolution : 13 bits (codeur multi-tours)
- Interface CANopen = protocole sur bus CAN

**Capteur inductif (2020 E1) :**
- Détection de passage de dents (signal carré)
- Fréquence signal : $f = \frac{N \cdot Z \cdot n}{60}$ où $N$ = vitesse (tr/min), $Z$ = nombre de dents
- Ex. : $f = 240 \times 24 / 60 = 96$ Hz → choix du capteur selon fréquence max admissible

**Jauge de contrainte (2021 E1, 2025 E2 Commune) :**
- Variation de résistance sous contrainte mécanique : $\Delta R / R = \Delta R_0 / R_0$ (indépendant de T grâce au pont de Wheatstone)
- Facteur de jauge $k = \Delta R/R / \varepsilon$ (déformation)

### 1.4 Capteurs de pression

**Capteur piézorésistif 4–20 mA (2021 E2, capteur SHD-U) :**
- Signal conditionné en boucle de courant 4–20 mA sur 2 fils
- Avantage : immunité aux perturbations CEM sur grande longueur de câble
- Non-linéarité typique : $0{,}15\%$ de la pleine échelle
- Plage d'alimentation : 6 à 38 V DC

**Correspondance courant ↔ valeur mesurée (signal 4–20 mA) :**
$$x = x_{min} + \frac{I_s - 4}{16} \cdot (x_{max} - x_{min})$$

Pour le PLC (automate S7-1500, 2024) : le mot PIW8 varie de 0 à 27 648 pour $I_s \in [4;20]$ mA.

### 1.5 Pont de Wheatstone (2025 E2 Commune, Rapport 2025)

Structure : 4 résistances en pont, tension d'alimentation $V_{cc}$.

**Tension de déséquilibre (approximation petits déséquilibres, $\Delta R \ll R_0$) :**
$$V_{out} \approx \frac{V_{cc}}{4} \cdot \frac{\Delta R}{R_0}$$

Avantage fondamental : compense les dérives thermiques (la variation $\Delta R$ due à la température se cancelle si les 4 jauges sont identiques et au même endroit).

L'amplificateur différentiel (gain $K_a$) amplifie $V_{out}$ jusqu'à la plage d'entrée du CAN :
$$V_{entrée\_CAN} = K_a \cdot \frac{V_{cc}}{4} \cdot \frac{\Delta R}{R_0}$$

Exemple (2025 Rapport Jury) : $V_{entrée\_CAN} = 5$ V pour $\Delta R = 0{,}0153\ \Omega$, $R_0 = 120\ \Omega$, $V_{cc} = 1$ V → $K_a = 15{,}6 \times 10^4$.

### 1.6 Conditionnement du signal

**Montages AOP courants en conditionnement (2026 E2 BAC3) :**
- Amplificateur inverseur : $V_{out} = -\frac{R_f}{R_e} V_{in}$
- Amplificateur non-inverseur : $V_{out} = \left(1 + \frac{R_f}{R_e}\right) V_{in}$
- Montage soustracteur (ampli différentiel) : $V_{out} = \frac{R_2}{R_1}(V^+ - V^-)$
- Montage suiveur : $V_{out} = V_{in}$ (adaptation d'impédance)
- Montage sommateur

**Objectif du conditionnement :** adapter la plage de sortie du capteur à la plage d'entrée du CAN (ex. 2026 BAC3 : capteur Jumo → $v_A \in [0;3\ \text{V}]$ pour couvrir $T \in [-5°;90°]$C).

**Transmetteur 4–20 mA (2024 E1) :**
Convertit la FEM $e_{AB}$ du thermocouple (quelques mV) en courant $I_s \in [4;20]$ mA.
- Entrée : $e_{AB} \in [-1;10{,}8]$ mV
- Sortie : $I_s \in [4;20]$ mA
- Calcul de mise à l'échelle dans l'automate : $MW8 = f(PIW8)$

---

## 2. QUESTIONS TYPES

**Q1 — 2026 E2 BAC3** : Identifier le type de transducteur d'un capteur Jumo (PT100 ou thermocouple ?), son principe de mesure, et sa nature active/passive.
> *Attendu :* identifier le type via la référence (code 370 = PT100), transducteur résistif, capteur passif.

**Q2 — 2026 E2 BAC3** : Justifier le besoin d'un ensemble \{amplificateur + conditionneur\} pour mesurer $T \in [-5°;90°]$C. Montrer que $c = 0{,}0316$ V·°C$^{-1}$ ($v_A = c \cdot T$).
> *Attendu :* plage de sortie capteur trop faible et décalée ; calcul $c = 3/(90-(-5)) = 3/95 \approx 0{,}0316$.

**Q3 — 2024 E1 (Thermocouple type J)** : Justifier le choix du type J pour une plage $[-20;200]°$C avec un milieu sec.
> *Attendu :* plage J couvre $[-210;1200]°$C, tolérance $\pm 2{,}5°$C acceptable, moins cher que type T, milieu sec.

**Q4 — 2025 E2 Commune (Pont de Wheatstone)** : Expliquer pourquoi un pont de Wheatstone est utilisé plutôt qu'une mesure directe de la résistance d'une jauge. Donner l'expression de la tension de sortie.
> *Attendu :* compensation thermique, expression $V_{out} = (V_{cc}/4) \cdot (\Delta R/R_0)$.

**Q5 — 2021 E1 (Capteur de couple)** : Choisir un capteur à jauges parmi une liste selon la charge nominale. Vérifier que la flèche n'excède pas 1 mm.

**Q6 — 2020 E1 (Capteur inductif)** : Calculer la fréquence du signal du capteur inductif et choisir la référence du capteur adapté à partir de la documentation.

---

## 3. ATTENTES DU JURY

- **Identifier les caractéristiques d'un capteur à partir de sa référence ou d'un document technique** : type, plage, précision, signal de sortie, nature active/passive.
- **Justifier le choix d'un capteur** : le jury (2020) souligne que « le choix du capteur est rarement justifié » — toute conclusion doit être chiffrée.
- **Maîtriser le pont de Wheatstone** : le jury (2025) note que moins de 20 % des candidats traitent correctement le pont de Wheatstone et l'expression simplifiée de la tension de sortie.
- **Calculer le gain d'un montage AOP** de conditionnement pour adapter la plage capteur à la plage CAN.
- **Signal 4–20 mA** : savoir écrire la relation linéaire entre courant et grandeur physique, et calculer la mise à l'échelle dans l'automate.
- **Ne pas confondre** thermocouple (actif, FEM de l'ordre du mV) et PT100 (passif, résistance).

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur |
|---|---|
| PT100 : $R_0$ | $100\ \Omega$ à 0°C |
| PT100 : $\alpha$ | $3{,}85 \times 10^{-3}\ °\text{C}^{-1}$ |
| Thermocouple J : $e_{AB}$ | $-1$ mV (à $-20°$C) à $+10{,}8$ mV (à $+200°$C) |
| Thermocouple K : plage | $-10$ à $+1100°$C, tolérance $\pm 2{,}5°$C |
| Signal normalisé industriel | $4$–$20$ mA (2 fils), $0$–$10$ V |
| Pont Wheatstone, $R_0$ jauge | $120\ \Omega$ (typique) |
| Capteur inductif IMT 12-4B | $f_{max}$ selon datasheet |
| Signal PWM servomoteur | 50 Hz, rapport cyclique pilote angle ($-90°$ à $+90°$) |
| Capteur niveau HITEC CP5220 | Signal 4–20 mA, pleine échelle réglable |
| Capteur DS1820 (OneWire) | Température sur 12 bits, $\pm 0{,}0625°$C/LSB |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **Pont de Wheatstone mal maîtrisé** : l'expression simplifiée suppose $\Delta R \ll R_0$ ; si ce n'est pas justifié, le jury attend l'expression exacte.
- **Confusion capteur actif/passif** : le thermocouple génère lui-même une tension ; la PT100 ne fait que varier sa résistance.
- **Signal 4–20 mA** : oublier que 4 mA correspond à la valeur minimale (pas à zéro) — piège de la mise à l'échelle.
- **Choix du type de thermocouple** : le candidat doit comparer plusieurs critères (plage, tolérance, coût, environnement) et ne pas se limiter à la plage.
- **Capteur à jauges** : ne pas confondre la flèche (déformation géométrique, en mm) avec la déformation relative $\varepsilon = \Delta L/L$.
- **Caractérisation du filtre** passe-bas de conditionnement : il doit être dimensionné en lien avec $f_e$ du CAN (théorème de Shannon).

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T22 (CAN/numérisation)** : le conditionnement aboutit toujours au CAN — les deux thèmes sont indissociables et systématiquement co-présents dans les sujets CAPET IE.
- **T24 (Systèmes embarqués / automates)** : l'automate lit le signal conditionné via son module d'entrées analogiques (4–20 mA ou 0–10 V) ; la mise à l'échelle est programmée dans l'automate (2024 S7-1500).
- **Asservissements (T1x)** : le capteur est l'élément de retour de la boucle fermée ; sa sensibilité (gain $K_c$) entre dans la fonction de transfert globale.
- **Électronique analogique (AOP)** : montages inverseur, non-inverseur, soustracteur, suiveur sont tous issus du cours sur les AOP idéaux — approfondissement nécessaire.
- **Transmission (T25)** : les capteurs intelligents (DS1820 OneWire, codeurs CANopen) transmettent leurs données sur un bus numérique — lien direct avec les protocoles de communication.
