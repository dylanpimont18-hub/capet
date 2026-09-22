# T22 — CAN/CNA, Numérisation, Échantillonnage
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

### 1.1 Convertisseur Analogique-Numérique (CAN)

Le CAN (Convertisseur Analogique Numérique) délivre en sortie un nombre fini de codes numériques correspondant à une gamme de tension analogique d'entrée bornée : c'est la plage de conversion.

**Quantum (pas de quantification) :**
$$q = \frac{V_{ref}}{2^n - 1} \approx \frac{V_{ref}}{2^n}$$

où $n$ est le nombre de bits et $V_{ref}$ la tension de référence (plage d'entrée).

**Valeur numérique de sortie :**
$$N = \frac{V_E}{q} = \frac{V_E \cdot 2^n}{V_{ref}}$$

**Nombre de bits nécessaires pour une précision $\delta$ :**
$$2^n \geq \frac{V_{ref}}{\delta} \Rightarrow n \geq \log_2\!\left(\frac{V_{ref}}{\delta}\right)$$

**Erreur de quantification maximale :** $\pm\,q/2$

**Sensibilité de la chaîne capteur–CAN :**
$$S = \frac{\Delta G_N}{\Delta T} \quad [\text{unité numérique par }°\text{C ou par unité physique}]$$

### 1.2 Convertisseur Numérique-Analogique (CNA)

Convertit un mot binaire $N$ en tension analogique :
$$V_S = N \cdot q = N \cdot \frac{V_{ref}}{2^n}$$

Utilisé en sortie du correcteur numérique dans une boucle d'asservissement échantillonné.

### 1.3 Théorème de Shannon (échantillonnage)

**Théorème :** Pour qu'un signal analogique de fréquence maximale $f_{max}$ soit reconstituable sans aliasing, la fréquence d'échantillonnage $f_e$ doit vérifier :
$$f_e \geq 2 \cdot f_{max}$$

**Filtre anti-repliement :** filtre passe-bas placé avant le CAN, de fréquence de coupure :
$$f_c \leq \frac{f_e}{2}$$

Son rôle est d'éliminer les composantes spectrales supérieures à $f_e/2$ qui causeraient un repliement de spectre (aliasing).

**Période d'échantillonnage** $T_e$ en asservissement numérique : elle doit être suffisamment petite devant la constante de temps du système, typiquement $T_e \leq T_{système}/10$.

### 1.4 Chaîne d'acquisition complète (structure type CAPET)

$$\text{Grandeur physique} \xrightarrow{\text{Capteur}} v_T(t) \xrightarrow{\text{Conditionneur+AMP}} v_A(t) \xrightarrow{\text{CAN}} G_N$$

La tension $v_A$ doit couvrir toute la plage d'entrée du CAN (ex. $[0{,}3 \text{ V}]$) pour utiliser au maximum la résolution.

### 1.5 Codage de sortie

- Binaire naturel (non signé)
- Binaire signé complément à 2
- Code hexadécimal : groupement par 4 bits

Exemple (2013, 12 bits, $V_{ref} = 10$ V) :
$$q = \frac{10}{2^{12}-1} = 2{,}44 \text{ mV}, \quad N(4{,}5\text{ V}) = \frac{4{,}5}{2{,}44\times10^{-3}} = 1842_{10} = 732_{16}$$

---

## 2. QUESTIONS TYPES

**Q1 — 2013 E1 (Tour laboratoire)** : Un signal de température est compris entre $-50°$C et $+50°$C, précision $0{,}1°$C, tension de sortie 0 à 10 V. Déterminer le nombre de bits nécessaires du CAN.
> *Réponse attendue :* $\delta = 0{,}1/100 \times 10 = 10$ mV ; $2^n \geq 10/0{,}01 = 1000$ ; $n \geq 10$ bits. Choix : 12 bits.

**Q2 — 2013 E1 (Corrigé)** : Exprimer la tension $V_E$ du CAN en fonction de la température $\theta$, puis coder la sortie en hexadécimal pour $\theta = -5°$C avec un CAN 12 bits, $V_{ref} = 10$ V.
> *Réponse :* $V_E = \frac{10}{100}(\theta + 50)$ ; pour $\theta=-5°$C : $V_E = 4{,}5$ V ; $q = 2{,}44$ mV ; $N = 1842_{10} = 732_{16}$.

**Q3 — 2022 E1/E2 (TRT200, PIC18F8723)** : À partir de la structure interne du CAN du microcontrôleur, indiquer le nombre de CAN, le nombre d'entrées disponibles, le rôle des entrées CHS0 à CHS3, et la résolution. Calculer le quantum pour $V_{ref} = 5$ V.
> *Réponse :* 1 CAN, 16 entrées multiplexées (AN0–AN15), CHS0:CHS3 = sélection de l'entrée, résolution 10 bits ; $q = 5/1023 \approx 4{,}9$ mV.

**Q4 — 2026 E2 BAC3** : Montrer que la sensibilité $S$ de l'ensemble \{capteur + ampli + conditionneur + CAN\} est égale à $2{,}684$ °C$^{-1}$. Déduire le mot numérique NC (binaire et hexa) pour $T_C = 55°$C.

**Q5 — 2026 E1 (Bus Hycity)** : Rappeler le théorème de Shannon. Définir le rôle du filtre anti-repliement. Déduire la fréquence de coupure $f_c$ si la fréquence d'échantillonnage est $f_e$.

**Q6 — 2025 E2 Commune** : Un CAN a une plage $[-5\text{ V},+5\text{ V}]$. Déterminer le nombre de bits nécessaire pour que l'erreur de quantification soit 10 fois plus petite que la variation $\delta v$ entre deux positions angulaires adjacentes.

---

## 3. ATTENTES DU JURY

- **Maîtriser la formule du quantum** et la distinguer de la résolution (souvent confondues par les candidats).
- **Justifier le choix du nombre de bits** par le rapport plage/précision souhaitée, et non par intuition.
- **Shannon** : ne pas se limiter à l'énoncé, appliquer la conséquence sur $f_c$ du filtre anti-repliement et sur $T_e$.
- **Chaîne de mesure complète** : savoir relier les blocs capteur–conditionneur–CAN, et calculer le gain global de la chaîne.
- Le jury (2020) déplore explicitement que « la majeure partie des candidats ne sache pas déterminer la résolution d'un capteur ».
- **Résultats encadrés, unités cohérentes**, vérification de cohérence dimensionnelle obligatoire.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Paramètre | Valeur typique rencontrée |
|---|---|
| Résolution typique | 8, 10, 12 bits (le plus fréquent : 10–12 bits) |
| $V_{ref}$ fréquente | 3 V, 3,5 V, 5 V, 10 V |
| Quantum 10 bits / 5 V | $q = 5/1023 \approx 4{,}9$ mV |
| Quantum 12 bits / 10 V | $q = 10/4095 \approx 2{,}44$ mV |
| Quantum 8 bits / 5 V | $q = 5/255 \approx 19{,}6$ mV |
| Fréquence d'éch. robot (2025) | $f_e = 1{,}8$ MHz pour précision $0{,}1°$ |
| Période éch. régulation T° (2026) | $T_e = 0{,}25$ s |
| Porteuse CAN (CAN interne PIC) | ADS7029-Q1, CAN sigma-delta LT2439 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **Confondre résolution (nombre de bits) et précision physique.** La résolution est $q = V_{ref}/2^n$ ; la précision globale dépend aussi des non-linéarités, du bruit.
- **Utiliser $2^n$ au lieu de $2^n - 1$** dans le quantum (erreur fréquente). Pour $n \geq 8$, l'approximation $2^n$ est acceptable mais doit être justifiée.
- **Oublier le filtre anti-repliement** dans la chaîne : le jury attend sa mention systématique dès qu'il y a CAN dans une boucle d'asservissement.
- **Ne pas vérifier le temps de conversion** du CAN par rapport à la période d'échantillonnage (exigence 2026 : $T_c \leq T_e$).
- **Confusion CAN/CNA** dans les boucles d'asservissement numérique : le CAN est en voie de mesure, le CNA est en voie de commande.
- **Codage hexadécimal** : grouper 4 bits depuis le bit de poids faible, pas depuis le MSB.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T23 (Capteurs et conditionnement)** : le CAN est systématiquement en bout de chaîne après le capteur et le conditionneur — T22 et T23 apparaissent toujours ensemble dans les sujets.
- **T24 (Systèmes embarqués/microcontrôleur)** : le CAN est souvent intégré dans le microcontrôleur (PIC, Arduino, DSP). Registre ADCON0 du PIC 18F8723 = configuration du CAN interne.
- **T25 (Transmission numérique, bus CAN)** : le bus CAN (Controller Area Network, 2026 E1) est un bus série de transmission de données numériques — à ne pas confondre avec le CAN (convertisseur).
- **Asservissements (T1x)** : dans un correcteur numérique, CAN + correcteur + CNA forment la boucle numérique ; Shannon régit la période $T_e$.
- **Électronique analogique (AOP)** : les montages de conditionnement (amplificateur différentiel, montage soustracteur) sont dimensionnés pour piloter l'entrée du CAN.
