# T25 — Transmission Numérique, Modulations
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

### 1.1 Notions fondamentales de transmission numérique

**Débit binaire** $D_b$ (bit/s) : nombre de bits transmis par seconde.
$$D_b = \frac{1}{T_b}$$
où $T_b$ est la durée d'un bit.

**Débit symbole** (baud) : nombre de symboles par seconde. Chaque symbole peut coder $k = \log_2 M$ bits (modulation à $M$ états).
$$D_b = k \cdot D_s = \log_2(M) \cdot D_s$$

**Efficacité spectrale :** $\eta = D_b / B$ [bit/s/Hz], où $B$ est la bande passante.

**Capacité de Shannon :**
$$C = B \cdot \log_2(1 + SNR)$$
où $SNR$ est le rapport signal/bruit (linéaire, sans unité).

### 1.2 Modulations analogiques (FM — 2015 E1)

**Modulation de fréquence (FM) :**
$$\Phi(t) = 2\pi f_0 t + k_f \int_0^t v_m(\tau)\,d\tau$$
$$f_{inst}(t) = f_0 + k_f \cdot v_m(t)$$

**Indice de modulation FM :**
$$m = \frac{\Delta f}{f_m} = \frac{k_f \cdot V_m}{f_m}$$

**Modulation FSK (2015 E1, 2022 E1/E2) :**
Le modulant prend deux valeurs discrètes $v_m(t) = \pm 1$ :
- $f_0 = f_n - \Delta f$ lorsque $v_m = -1$ (bit « 0 »)
- $f_1 = f_n + \Delta f$ lorsque $v_m = +1$ (bit « 1 »)
- Excursion en fréquence : $\Delta f = f_1 - f_n = f_n - f_0$

Exemple (2015 E1 — Abri déployable) :
- Porteuse $f_n = 433$ MHz, excursion $\Delta f = 300$ kHz
- Diviseur $R = 1024$, signal PLL/VCO

### 1.3 Modulations numériques — tableau récapitulatif

| Modulation | Principe | Avantage | Usage CAPET |
|---|---|---|---|
| FSK | Fréquence varie selon bit | Robuste au bruit d'amplitude | 2015 E1, LoRa (SF7 FSK) |
| PSK / BPSK | Phase commute entre 0° et 180° | Bonne efficacité spectrale | Programme (non explicite sujets) |
| QAM | Amplitude + Phase | Haute efficacité spectrale | Programme (non explicite sujets) |
| CSS / LoRa | Étalement de spectre Chirp | Longue portée, faible puissance | 2022 E1/E2 |
| MLI / PWM | Largeur d'impulsion | Commande d'actionneur | 2025 E2 Commune, 2013 Corrigé |

### 1.4 Protocole LoRa / LoRaWAN (2022 E1/E2)

**Modulation LoRa = Chirp Spread Spectrum (CSS), propriétaire Semtech.**
- Bandes ISM : 868 MHz (Europe), 915 MHz (Amérique du Nord)
- Portée : $\sim 5$ km urbain, $\sim 15$ km rural
- Très faible consommation — IoT (Internet des Objets)

**Paramètres clés :**
- **SF (Spreading Factor)** : SF7 à SF12 — plus SF est grand, plus la portée augmente mais le débit baisse
- **Bande passante BP** : 125 kHz, 250 kHz, 500 kHz
- **Taux de codage CR** : 4/5, 4/6, 4/7, 4/8 (bits redondants pour correction d'erreurs)

**Tableau débits LoRa (2022 E1/E2 — extrait sujet) :**

| DR | Modulation | SF | BP | Débit physique (bit/s) |
|---|---|---|---|---|
| 0 | LoRa | 12 | 125 kHz | 250 |
| 1 | LoRa | 11 | 125 kHz | 440 |
| 2 | LoRa | 10 | 125 kHz | 980 |
| 3 | LoRa | 9 | 125 kHz | 1 760 |
| 4 | LoRa | 8 | 125 kHz | 3 125 |
| 5 | LoRa | 7 | 125 kHz | 5 470 |
| 6 | LoRa | 7 | 250 kHz | 11 000 |
| 7 | FSK | 50 kbit/s | — | 50 000 |

**Débit binaire utile avec taux de codage :**
$$D_{utile} = D_{physique} \times CR = D_{physique} \times \frac{4}{5} \quad \text{si } CR = 4/5$$

Exemple (2022 Q29) : $D_b = $ débit physique pour BP = 125 kHz, CR = 4/5. Calcul à partir de la table.

### 1.5 Bus CAN — transmission série de terrain (2026 E1, 2019 E2, 2018 E2)

**Bus CAN (Controller Area Network) :**
- Bus série différentiel : $U_D = U_{CAN\_H} - U_{CAN\_L}$
- Niveaux : bit dominant $U_D > 2$ V, bit récessif $U_D < 0{,}5$ V
- Multi-maîtres, arbitrage sans destructeur de message (CSMA/CD-like)
- Vitesse max : 1 Mbit/s (CAN High Speed)

**Structure d'une trame CAN (2026 E1) :**
$$\underbrace{SOF}_{1} + \underbrace{ID}_{11} + \underbrace{RTR}_{1} + \underbrace{IDE+r0}_{2} + \underbrace{DLC}_{4} + \underbrace{Data}_{0-64} + \underbrace{CRC}_{15} + \underbrace{CRC delim.}_{1} + \underbrace{ACK}_{2} + \underbrace{EOF}_{7}$$

Taille maximale d'une trame CAN : 111 bits (avec 8 octets de données).

**Calcul de débit binaire (2026 E1 Q D5) :**
À partir d'un chronogramme, mesurer la durée d'un bit $T_b$ :
$$D_b = \frac{1}{T_b}$$
Durée de la trame : $t_{trame} = 111 \times T_b$.

**Protocole CANopen (2019 E2) :**
- Couche applicative standardisée sur CAN
- TPDO (Transmit Process Data Object) : trames cycliques de données process
- Identifiant TPDO : $ID = 180h + n°_{noeud}$

### 1.6 MLI / PWM en contexte de transmission (2025 E2, 2013 Corrigé)

La MLI (Modulation de Largeur d'Impulsion = PWM) est une technique de modulation numérique pour :
1. **Transmission de consignes à des servomoteurs** : signal créneau à 50 Hz, durée $t_{on}$ codant l'angle
2. **Commande d'onduleurs** (MLI sinusoïdale) : comparaison modulante/porteuse pour générer un signal alternatif

**Formule rapport cyclique → angle :**
$$\alpha = \frac{t_{on}}{T} \Rightarrow t_{on} = \frac{\theta - \theta_{min}}{\theta_{max} - \theta_{min}} \cdot (t_{on\_max} - t_{on\_min}) + t_{on\_min}$$

### 1.7 Comparaison UART vs PWM (2025 E2 Commune Q22)

| Critère | UART | PWM |
|---|---|---|
| Synchronisation | Asynchrone (baud rate) | Synchrone (fréquence fixe) |
| Complexité réception | Élevée (protocole complet) | Simple (mesure durée d'impulsion) |
| Immunité bruit | Faible | Élevée (signal TOR) |
| Débit | Élevé | Faible (1 valeur/période) |

---

## 2. QUESTIONS TYPES

**Q1 — 2015 E1 (Shelter déployable — FSK)** : Exprimer l'angle de phase instantané $\Phi(t)$ en fonction de $f_0$, $k_f$, $V_m$ et $f_m$. Donner l'indice de modulation $m$.
> *Attendu :* $\Phi(t) = 2\pi f_0 t + m \sin(2\pi f_m t)$ avec $m = k_f V_m / f_m$.

**Q2 — 2015 E1 (FSK)** : Donner les deux fréquences du signal FSK en fonction de la valeur binaire transmise ($v_m = \pm 1$). Exprimer l'excursion $\Delta f$.

**Q3 — 2022 E1/E2 (LoRa)** : Calculer le débit binaire utile pour une bande passante de 125 kHz avec CR = 4/5. Discuter de la valeur obtenue.
> *Attendu :* lire SF7 dans la table → $D_{physique} = 5470$ bit/s ; $D_{utile} = 5470 \times 4/5 = 4376$ bit/s.

**Q4 — 2026 E1 (Bus CAN)** : Pour le protocole CAN, préciser le type de codage en ligne, la vitesse de transmission, la longueur de trame.

**Q5 — 2026 E1 (Bus CAN) Q D5** : À partir d'un chronogramme, déterminer la durée d'un bit et le débit binaire. En déduire la durée de la trame (111 bits). Conclure sur le respect de l'exigence de durée de transmission.

**Q6 — 2025 E2 Commune** : Comparer UART et PWM pour la transmission de consignes à une interface de commande de robots. Justifier le choix du format PWM.

---

## 3. ATTENTES DU JURY

- **Maîtriser la structure d'une trame CAN** : savoir identifier chaque champ et calculer la durée totale d'une trame.
- **Calcul du débit binaire** à partir d'un chronogramme ou d'une table (LoRa) : résultat avec unité, cohérence avec la bande passante.
- **Modulation FSK** : savoir énoncer le principe, les deux fréquences, l'indice de modulation. Sujet 2015 = seul sujet à traiter en profondeur la modulation de fréquence.
- **LoRa** : comprendre le compromis portée/débit selon le SF — question de 2022 explicitement sur le calcul du débit utile.
- **MLI/PWM** : ne pas confondre la MLI de commande d'onduleur (électronique de puissance) et la PWM de transmission de consigne à un servomoteur.
- **Shannon** : le théorème est attendu dans tout contexte d'échantillonnage (T22 et T25 sont liés ici).

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur |
|---|---|
| Fréquence porteuse FSK (2015) | 433 MHz |
| Excursion FSK (2015) | $\Delta f = 300$ kHz |
| Bande ISM LoRa (Europe) | 868 MHz |
| Portée LoRa SF12, zone rurale | 15 km |
| Débit LoRa SF7 / 125 kHz | 5 470 bit/s (physique) |
| Débit LoRa FSK | 50 000 bit/s |
| Débit bus CAN max | 1 Mbit/s |
| Trame CAN (8 octets données) | 111 bits |
| PWM servomoteur | 50 Hz, $t_{on} \in [1;2]$ ms |
| Débit UART Arduino typique | 9 600 baud |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **Confondre bus CAN (protocole réseau) et CAN (convertisseur analogique-numérique)** : en 2026, la même épreuve contient les deux — la distinction par contexte est impérative.
- **FSK vs FM** : FSK = cas particulier de FM avec modulant binaire ($\pm 1$) — l'étudiant doit savoir passer de la FM générale à la FSK.
- **Taux de codage LoRa** : CR = 4/5 signifie que pour 4 bits utiles, 1 bit redondant est ajouté, soit 5 bits transmis — le débit utile est donc $\times 4/5$ du débit physique.
- **Chronogramme CAN** : la lecture d'un chronogramme pour mesurer $T_b$ est souvent mal réalisée — compter les transitions clairement.
- **Shannon** : la formule $f_e \geq 2 f_{max}$ est souvent confondue avec la capacité de Shannon $C = B \log_2(1+SNR)$ — deux théorèmes distincts.
- **PWM et angle** : la relation entre durée $t_{on}$ et angle n'est pas linéaire si le datasheet donne des bornes non symétriques — toujours relire la documentation.
- **Trame CAN : compter les bits champ par champ** : un décompte approximatif fausse en cascade l'efficacité et le débit. Dans le sujet 2026 : en-tête $1 + 12 + 6 = 19$ bits, données 64 bits au plus, terminateur $16 + 2 + 7 + 3 = 28$ bits, soit 111 bits ; efficacité $E_f = 64/111 \approx 58\ \%$ ; à 8 µs par bit, la trame dure 888 µs. Source : rapport du jury 2026 du troisième concours (même sujet que l'E1 externe 2026), question D4 et D5 = question D4 et D5 du sujet externe.
- **Identificateur, fonction et adresse de nœud** : confondre ces trois champs fausse la lecture de la trame. Dans le sujet 2026, l'identificateur de 11 bits regroupe le code de fonction (4 bits de poids fort) et l'adresse du nœud (7 bits) : lire le découpage donné par le sujet avant de convertir en hexadécimal. Source : rapport du jury 2026 du troisième concours (même sujet que l'E1 externe 2026), question D6 = question D6 du sujet externe.
- **Arbitrage CAN : le plus petit identificateur gagne** : croire que l'identificateur le plus grand est prioritaire. Le bit dominant est 0 : à la comparaison bit à bit, la station qui émet un 1 récessif face à un 0 perd et se retire, donc le message le plus prioritaire porte l'identificateur le plus petit. Source : rapport du jury 2026 du troisième concours (même sujet que l'E1 externe 2026), question D8 = question D8 du sujet externe.
- **Bit de stuffing au décodage** : découper les octets de données sans retirer les bits de bourrage décale tout le décodage. Après cinq bits identiques consécutifs, l'émetteur insère un bit de niveau opposé, sans information, que le récepteur retire. Source : rapport du jury 2026 du troisième concours (même sujet que l'E1 externe 2026), question D9, sans équivalent dans le sujet externe.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T22 (CAN/Shannon)** : le théorème de Shannon sur l'échantillonnage ($f_e \geq 2 f_{max}$) est commun aux deux thèmes — T22 = côté acquisition, T25 = côté transmission.
- **T24 (Systèmes embarqués)** : le bus CAN est un protocole embarqué (automobile, industrie) ; les protocoles UART, SPI, I2C, LoRa sont des périphériques de microcontrôleur.
- **T23 (Capteurs intelligents)** : les capteurs CANopen (codeurs 2014) et DS1820 (OneWire 2022) transmettent numériquement leurs données — lien direct T23-T25.
- **Énergie (T0x)** : LoRa est utilisé pour les applications IoT à très faible consommation (capteurs sans fil industriels, bâtiments connectés).
- **Asservissements** : la commande par PWM d'un servomoteur (2025) ou la commande MLI d'un onduleur (2013, 2024, 2026) illustrent comment la transmission numérique s'insère dans une boucle de régulation.
