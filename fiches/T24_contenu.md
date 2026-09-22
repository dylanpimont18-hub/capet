# T24 — Systèmes Embarqués, FPGA, VHDL
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

### 1.1 Architecture des systèmes embarqués

Un système embarqué est un système électronique intégré dans un dispositif plus grand pour remplir une fonction de contrôle/commande dédiée. Il regroupe :

| Composant | Rôle | Exemples CAPET |
|---|---|---|
| Microcontrôleur (µC) | CPU + périphériques intégrés (CAN, UART, SPI, I2C, PWM) | Arduino Uno/Nano (ATmega), PIC 18F8723, PIC 18F1823 |
| DSP | Traitement numérique du signal haute vitesse | DSP fréquence 40 MHz (2024 E2) |
| Automate Programmable Industriel (API/PLC) | Contrôle industriel, robustesse, entrées/sorties TOR/analogiques | Schneider M340, Siemens S7-1500 (2024) |
| FPGA | Circuit logique reconfigurable, traitement parallèle | Non trouvé explicitement dans les sujets CAPET IE |

### 1.2 Microcontrôleur — périphériques courants

**CAN interne (PIC 18F8723, 2022) :**
- 1 CAN partagé entre 16 entrées analogiques (AN0–AN15) via multiplexeur
- Sélection par registre ADCON0, champs CHS3:CHS0
- Résolution : 10 bits (PIC 18F8723), puis 12 bits selon version
- Quantum : $q = V_{ref}/2^n$

**PWM (Modulation de Largeur d'Impulsion, 2025 E2 Commune) :**
- Signal créneau de fréquence fixe (50 Hz pour servomoteur)
- Rapport cyclique $\alpha = t_{on}/T$ pilote l'angle ou la vitesse
- Formule : rapport cyclique → angle entre $\theta_{min}$ et $\theta_{max}$
- Fréquence d'échantillonnage nécessaire pour résolution angulaire $\delta\theta$ :
  $$f_{ech} = \frac{1}{T} \cdot \frac{\theta_{max}-\theta_{min}}{\delta\theta}$$
  Exemple (2025) : $\delta\theta = 0{,}1°$, plage $180°$ → $N = 1800$ positions → $f_{ech} = 1{,}8$ MHz

**UART / RS232 / RS485 :**
- Transmission asynchrone série
- Paramètres : débit baud, bits de données, parité, stop
- RS485 = version différentielle, longue distance, bus multi-esclaves

**SPI / I2C :**
- SPI : 4 fils (MOSI, MISO, SCK, SS), full-duplex, maître/esclave
- I2C : 2 fils (SDA, SCL), adressage 7 bits, multi-maîtres
- OneWire (DS1820) : 1 seul fil + masse, adressage par identifiant unique 64 bits (2022 E1/E2)

### 1.3 DSP — Processeur de signal numérique (2024 E2 Appliquée Commune)

Un DSP est un microprocesseur optimisé pour exécuter des applications de traitement numérique du signal le plus rapidement possible.

**Fréquence maximale de traitement requise :**
Avec un codeur incrémental de $P$ points par tour, à $n$ tr/min :
$$f_{max} = \frac{P \cdot n}{60}$$

Le DSP doit avoir une fréquence d'horloge $f_{DSP}$ vérifiant : $f_{DSP} \geq f_{max}$.

Exemple (2024) : $f_{max} = 1326$ Hz, $f_{DSP} = 40$ MHz → condition vérifiée.

### 1.4 Automate Programmable Industriel (API)

**Rôle :** Gestion de processus industriels, interfaces avec capteurs/actionneurs via modules TOR et analogiques.

**Structure Siemens S7-1500 (2024 E1) :**
- Entrées analogiques (module AI 8xU/I/RTD/TC ST) : code PIW8 (0–27 648 pour 4–20 mA)
- Entrées/sorties TOR : adressage mnémonique (I, Q, M)
- Programme cyclique : lecture entrées → traitement → écriture sorties
- Mise à l'échelle : $MW8 = f(PIW8)$ calculée linéairement

**Mise à l'échelle (2024 E1) :**
$$T = T_{min} + \frac{PIW8 - 0}{27648 - 0} \cdot (T_{max} - T_{min})$$

**Langage de programmation :** Ladder, Grafcet/SFC, blocs fonctionnels, Python (2021 E1).

**Diagramme états-transitions (2021 E1) :** description du comportement séquentiel d'un automate de sonde — transitions conditionnées par états des capteurs.

### 1.5 Bus de terrain (protocoles embarqués)

**Bus CAN (Controller Area Network) — 2026 E1, 2019 E2, 2018 E2 :**
- Bus série de terrain, multi-maîtres, résistance aux perturbations EM
- Débit : jusqu'à 1 Mbit/s
- Mode différentiel : CAN_H et CAN_L, $U_D = U_{CAN\_H} - U_{CAN\_L}$
- Structure de trame : SOF, identifiant (11 bits), RTR, DLC (4 bits), Data (0–8 octets), CRC, ACK, EOF
- CANopen = couche applicative sur CAN (codeurs absolus multi-tours, batteries)

**Protocole OneWire / DS1820 (2022 E1/E2) :**
- 1 fil de données + masse
- Identifiant unique 64 bits par capteur (famille + numéro + CRC)
- Commande 0x44 : lancement conversion température (750 ms pour 12 bits)
- Commande 0xBE : lecture Scratchpad (9 octets)
- Résolution configurable : 9–12 bits ($\pm 0{,}5°$C à $\pm 0{,}0625°$C)

**LoRaWAN (2022 E1/E2 — IoT) :**
- Modulation CSS (Chirp Spread Spectrum)
- Bande ISM 868 MHz (Europe)
- Portée : 5 km urbain, 15 km rural
- Débit physique de 250 bit/s à 50 kbit/s selon SF et BP

### 1.6 FPGA et VHDL

Non trouvé directement dans les 41 fichiers CAPET SII IE 2013–2026. Le programme le mentionne mais les sujets se concentrent sur microcontrôleurs et automates.

**Éléments de cours à maîtriser (programme) :**
- FPGA = réseau de portes programmables, reconfigurables après fabrication
- VHDL = langage de description matérielle : entité + architecture, signal, process, concurrent/séquentiel
- Structure : `entity`, `architecture`, `process`, `signal`, `std_logic`, `std_logic_vector`
- Avantage : parallélisme massif, déterminisme temporel fort
- Utilisé pour : décodeur, compteur, machine d'état, traitement temps-réel

---

## 2. QUESTIONS TYPES

**Q1 — 2022 E1/E2 (PIC 18F8723)** : Remplir le registre ADCON0 pour sélectionner l'entrée AN2 et lancer la conversion. Exprimer en hexadécimal.
> *Attendu :* CHS = 0010, ADON = 1, GO/DONE = 1 → valeur hex à déduire de la structure du registre.

**Q2 — 2022 E1/E2 (OneWire DS1820)** : Donner la valeur de la variable `temp` en binaire à partir des bytes 0 et 1 du Scratchpad.

**Q3 — 2024 E2 Commune (DSP)** : Calculer la fréquence maximale $f_{cmax}$ des signaux issus du codeur. Conclure sur la fréquence du DSP choisi (40 MHz).

**Q4 — 2025 E2 Commune (PWM)** : Représenter l'allure du signal PWM pour une consigne de $60°$. Préciser à quelle fréquence le récepteur doit échantillonner pour une précision $\delta\theta = 0{,}1°$.
> *Attendu :* $N = 1800$ positions → $f_{ech} = 1{,}8$ MHz ; discussion sur compatibilité avec Arduino (84 MHz).

**Q5 — 2024 E1 (Automate S7-1500)** : Écrire le sous-programme de mise à l'échelle convertissant PIW8 en température MW8 (°C) pour la plage $[-20;200]°$C.

**Q6 — 2021 E1 (Diagramme états-transitions)** : À partir du diagramme états-transitions de l'automate de sonde, identifier les transitions et actions, puis programmer en Python.

---

## 3. ATTENTES DU JURY

- **Jury 2023** : « Notions d'algorithmes et de programmes, variable informatique, boucles, systèmes embarqués sont des connaissances » attendues des candidats.
- **Jury 2021** : « Un candidat au CAPET doit être capable de câbler une entrée ou une sortie TOR/analogique d'un automate industriel programmable. »
- Maîtriser la **structure d'une trame CAN** : identifier SOF, ID, DLC, données, CRC.
- Savoir **configurer un registre de microcontrôleur** (ADCON0 du PIC, par exemple) en justifiant la valeur de chaque bit.
- **Algorithme de mise à l'échelle** : relation linéaire entre valeur brute automate et grandeur physique, avec calcul des coefficients.
- **PWM** : savoir calculer la durée $t_{on}$ pour un angle donné et identifier la fréquence de cadence.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Composant | Paramètre | Valeur |
|---|---|---|
| Arduino Nano | ATmega328, $f_{horloge}$ | 16 MHz (ou 84 MHz selon version) |
| PIC 18F8723 | CAN interne | 1 CAN, 10 bits, 16 entrées AN0–AN15 |
| DS1820 | Identifiant | 64 bits (8 octets), famille 0x10 ou 0x28 |
| DS1820 | Résolution 12 bits | 750 ms de conversion, $0{,}0625°$C/LSB |
| Siemens S7-1500 | Module AI, plage 4–20 mA | PIW8 ∈ [0 ; 27 648] |
| Bus CAN | Débit max (CAN 2.0) | 1 Mbit/s |
| LoRa SF7 / 125 kHz | Débit physique | 5 470 bit/s |
| LoRa FSK | Débit | 50 000 bit/s |
| DSP (2024) | $f_{max}$ | 40 MHz |
| PWM servomoteur | Fréquence | 50 Hz (période 20 ms) |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **FPGA/VHDL** : très peu présents dans les sujets réels — si la question apparaît, s'appuyer sur le cours théorique. Ne pas confondre VHDL (description matérielle) et C (programmation logicielle).
- **Confusion API et microcontrôleur** : l'API est programmé en Ladder/Grafcet pour l'industrie ; le µC est programmé en C/Python pour des fonctions embarquées légères.
- **Registre ADCON0** : chaque bit a un rôle précis (sélection voie, démarrage conversion, indicateur fin) — répondre bit par bit avec justification.
- **OneWire** : la commande 0x44 lance la conversion, 0xBE lit le résultat — les confondre est une erreur fréquente.
- **Mise à l'échelle** : ne pas oublier le décalage (offset) quand la plage ne commence pas à zéro (ex. 4 mA ≠ 0).
- **Bus CAN** : dans les sujets, « CAN » désigne parfois le bus Controller Area Network (protocole réseau) et parfois le Convertisseur Analogique Numérique — contexte obligatoire pour distinguer.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T22 (CAN numérique)** : le CAN interne du microcontrôleur est un périphérique clé du système embarqué ; configuration du registre ADCON0 = interface entre T22 et T24.
- **T23 (Capteurs)** : le capteur DS1820 (OneWire) ou PT100 alimentent les entrées du µC ou de l'automate ; le transmetteur 4–20 mA conditionne le signal pour l'API.
- **T25 (Transmission)** : les protocoles bus CAN, CANopen, LoRaWAN, OneWire, UART, SPI sont des protocoles de transmission numérique — lien direct avec T25.
- **Asservissements (T1x)** : l'automate ou le DSP implémente le correcteur numérique ; PWM = commande de l'actionneur.
- **Énergie (T0x)** : les systèmes embarqués gèrent la puissance embarquée, optimisent la consommation — lien avec gestion des batteries et IoT basse consommation (LoRa).
