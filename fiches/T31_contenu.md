# T31 — Télécommunications et RF
## Contenu documentaire — créé le 2026-11-10 pour couvrir le référentiel

> Thème au programme du CAPET SII IE mais quasi absent des sujets 2013–2026 : la fibre optique
> n'est interrogée qu'une fois (E1 commun 2014, question 38 ; mentions en 2018, 2024, 2025) et le
> codage NRZ apparaît en E1 2026 (D3). Les formules ci-dessous relèvent du cours ; la colonne
> Source le dit explicitement. Aucune n'est attribuée à un sujet qui ne la contient pas.

---

## 1. FORMULES ET COURS

### 1.1 Bande de base, modulations, multiplexage, synthèse de fréquence

| Grandeur | Formule | Unité | Fréquence | Source |
|---|---|---|---|---|
| Rapidité de modulation | $R = \frac{1}{T_s}$ | Bd | Programme | Cours |
| Rapidité maximale sur un canal idéal (Nyquist) | $R_{max} = 2B$ | Bd | Programme | Cours |
| Fondamental maximal d'un signal NRZ | $f_{max} = \frac{D}{2}$ | Hz | Programme | Cours ; NRZ en E1 2026 D3 |
| Fondamental maximal d'un code Manchester | $f_{max} = D$ | Hz | Programme | Cours |
| Bande occupée en multiplexage fréquentiel | $B_{tot} = N B + (N-1) B_g$ | Hz | Programme | Cours |
| Fréquence de sortie d'une PLL | $f_{out} = \frac{N}{R} f_{ref}$ | Hz | Programme | Cours |
| Pas de réglage d'un synthétiseur à PLL | $\Delta f = \frac{f_{ref}}{R}$ | Hz | Programme | Cours |
| Dérive en fréquence d'un quartz | $\Delta f = f_0 \cdot \delta \cdot 10^{-6}$ | Hz | Programme | Cours ($\delta$ en ppm) |
| Puissance exprimée en dBm | $P_{dBm} = 10 \log \frac{P}{1\ \mathrm{mW}}$ | dBm | Programme | Cours |
| Durée de réception d'un paquet de N bits | $t = \frac{N}{D} + \frac{d}{v}$ | s | Présent | E1 commun 2014, Q38 |

### 1.2 Propagation guidée : lignes et fibres optiques

| Grandeur | Formule | Unité | Fréquence | Source |
|---|---|---|---|---|
| Vitesse de propagation dans un diélectrique | $v = \frac{c}{\sqrt{\varepsilon_r}}$ | m/s | Programme | Cours |
| Impédance caractéristique d'une ligne sans pertes | $Z_c = \sqrt{\frac{L'}{C'}}$ | Ω | Programme | Cours |
| Coefficient de réflexion en bout de ligne | $\Gamma = \frac{Z_L - Z_c}{Z_L + Z_c}$ | — | Programme | Cours |
| Rapport d'ondes stationnaires | $\mathrm{ROS} = \frac{1 + \lvert\Gamma\rvert}{1 - \lvert\Gamma\rvert}$ | — | Programme | Cours |
| Affaiblissement de réflexion | $\mathrm{RL} = -20 \log \lvert\Gamma\rvert$ | dB | Programme | Cours |
| Puissance réfléchie par une charge désadaptée | $P_r = \lvert\Gamma\rvert^2 P_i$ | W | Programme | Cours |
| Ouverture numérique d'une fibre | $\mathrm{ON} = \sin\theta_{max} = \sqrt{n_1^2 - n_2^2}$ | — | Programme | Cours |
| Vitesse de la lumière dans le cœur d'une fibre | $v = \frac{c}{n_1}$ | m/s | Programme | Cours |
| Puissance en sortie d'une fibre de longueur L | $P_s = P_e - \alpha L$ | dBm | Programme | Cours ($\alpha$ en dB/km) |

### 1.3 Antennes, bilan de liaison, exposition aux champs

| Grandeur | Formule | Unité | Fréquence | Source |
|---|---|---|---|---|
| Longueur d'onde dans le vide | $\lambda = \frac{c}{f}$ | m | Programme | Cours |
| Longueur d'un dipôle demi-onde | $L \approx \frac{\lambda}{2}$ | m | Programme | Cours |
| Formule de Friis (champ lointain, espace libre) | $P_r = P_e G_e G_r \left(\frac{\lambda}{4 \pi d}\right)^2$ | W | Programme | Cours |
| Affaiblissement en espace libre | $A_{EL} = 20 \log \frac{4 \pi d}{\lambda}$ | dB | Programme | Cours |
| Densité de puissance rayonnée | $S = \frac{P_e G_e}{4 \pi d^2}$ | W/m² | Programme | Cours |
| Champ électrique en champ lointain | $E = \frac{\sqrt{30 P_e G_e}}{d}$ | V/m | Programme | Cours |
| Relation champ et densité de puissance (onde plane) | $S = \frac{E^2}{377}$ | W/m² | Programme | Cours |
| Niveau de référence d'exposition entre 400 et 2 000 MHz | $E_{lim} = 1{,}375 \sqrt{f_{MHz}}$ | V/m | Programme | Recommandation 1999/519/CE |

---

## 2. QUESTIONS TYPES

**QT1 — Fibre optique ou paire torsadée (E1 commun 2014, Q38, corrigé officiel)** : 256 octets sur
550 m ; fibre à 1 Gbit/s, cuivre à 2 Mbit/s. Fibre : 2,05 + 1,83 = 3,88 µs ; cuivre : 1,024 ms +
2,43 µs = 1,026 ms. Le corrigé officiel prend $v = 3\cdot10^8$ m/s dans la fibre ; avec $c/n_1$
on trouve 4,80 µs, sans changer la conclusion.

**QT2 — Bilan de liaison à 868 MHz (exercice inédit)** : $A_{EL} = 105{,}2$ dB à 5 km,
$P_r = -86{,}9$ dBm, marge de 50 dB ; champ à 1 m de 1,1 V/m contre 40,5 V/m autorisés.

**QT3 — Adaptation d'une antenne 75 Ω sur un coaxial 50 Ω (exercice inédit)** : $\Gamma = 0{,}2$,
ROS = 1,5, RL = 14 dB, 0,4 W réfléchis sur 10 W.

---

## 3. ATTENTES DU JURY

Aucun commentaire de jury sur ces notions dans les rapports 2018–2026 (recherche des mots
fibre, antenne, ligne, modulation, dBm le 2026-11-10). Ne pas en inventer.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique |
|---|---|
| Vitesse dans un coaxial ou une fibre | environ $2\cdot10^8$ m/s |
| Impédance des lignes RF / vidéo | 50 Ω / 75 Ω |
| Atténuation d'une fibre monomode à 1 550 nm | environ 0,2 dB/km |
| Gain d'un dipôle demi-onde | 2,15 dBi |
| Sensibilité d'un récepteur LoRa (SF12, 125 kHz) | environ −137 dBm |
| ROS jugé acceptable | ≤ 2 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **dB et dBm** : additionner deux puissances exprimées en dBm n'a pas de sens. Le dBm est une puissance absolue rapportée à 1 mW, le dB un rapport : on ajoute des gains en dB à une puissance en dBm, et deux puissances se somment en watts.
- **Bauds et bit/s** : confondre rapidité de modulation et débit binaire. Ils ne coïncident que pour $M = 2$ états ; en QPSK, 1 000 bauds transportent 2 000 bit/s.
- **Vitesse dans un câble** : prendre $c = 3\cdot10^8$ m/s dans un câble ou une fibre surestime la vitesse d'environ moitié. La vitesse vaut $c/\sqrt{\varepsilon_r}$ dans un coaxial et $c/n_1$ dans une fibre, soit environ $2\cdot10^8$ m/s.
- **Durée d'une transmission** : ne compter que la propagation oublie l'essentiel. La durée totale vaut $N/D$ (émission des bits) plus $d/v$ (propagation), et c'est souvent $N/D$ qui domine (E1 2014, question 38).
- **Ligne ou simple liaison** : traiter une liaison longue comme un fil idéal fausse le comportement en haute fréquence. Dès que la longueur dépasse environ $\lambda/10$, il faut adapter la charge à $Z_c$ pour éviter réflexions et ondes stationnaires.
- **ROS et adaptation** : croire qu'un ROS égal à 1 signale un défaut. Un ROS de 1 ($\Gamma = 0$) correspond à l'adaptation parfaite ; il tend vers l'infini en circuit ouvert ou en court-circuit.
- **Friis hors de son domaine** : appliquer la formule de Friis à quelques centimètres d'une antenne donne un résultat faux. Elle suppose le champ lointain ($d \gg \lambda$) et l'espace libre ; en intérieur, il faut prévoir une marge bien plus grande.
- **Niveau de référence d'exposition** : comparer un champ mesuré à 41 V/m quelle que soit la fréquence. Le niveau dépend de la bande : 28 V/m de 10 à 400 MHz, $1{,}375\sqrt{f_{MHz}}$ de 400 à 2 000 MHz, 61 V/m au-delà de 2 GHz.
- **Pas d'une PLL** : prendre $f_{out}/N$ pour le pas de réglage du synthétiseur. Le pas vaut $f_{ref}/R$, la fréquence à laquelle travaille le comparateur de phase.
- **NRZ et Manchester** : penser que le code Manchester augmente le débit. Il double la bande occupée pour un même débit ; son intérêt est de transporter l'horloge, avec une transition par bit.
- **Fibre multimode ou monomode** : choisir une fibre multimode pour une liaison longue à haut débit. La dispersion modale limite le produit débit × distance ; au-delà de quelques centaines de mètres à haut débit, on choisit le monomode.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

| Thème associé | Articulation |
|---|---|
| **T25 — Transmission numérique** | Débit, valence, FSK, LoRa et bus CAN y sont traités ; T31 ajoute la couche physique (codage, modulations, supports, antennes). |
| **T33 — Informatique embarquée et réseaux** | Les liaisons série et réseaux industriels utilisent les supports vus ici (paire différentielle, fibre). |
| **T22 — Numérisation** | Le théorème de Shannon sur l'échantillonnage et le critère de Nyquist sur la rapidité sont deux résultats distincts. |
| **T17 — Distribution et sécurité** | L'exposition aux champs basse fréquence (50 Hz) relève aussi de la sécurité des personnes. |
| **T20 — Filtres** | Les modulations exigent un filtrage de mise en forme ; l'analyseur de spectre vérifie la bande occupée. |
