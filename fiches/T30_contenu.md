# T30 — Mesurage, instrumentation, schématisation
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

### 1.1 Chaîne de mesure

Structure générale d'une chaîne de mesure :

```
Grandeur physique → Capteur → Conditionneur → Amplificateur → Filtre → CAN → Traitement numérique
```

**Paramètres caractéristiques d'une chaîne :**
- **Sensibilité** $S$ : variation de la sortie par unité de variation de l'entrée ($[S] = [Sortie]/[Entrée]$)
- **Pleine échelle** (PE) : étendue maximale de mesure
- **Résolution** : plus petite variation détectable
- **Précision** : écart maximal entre valeur mesurée et valeur vraie

*Exemple concret (2026 BAC3 Q.B11) :*
> Sensibilité de la chaîne {capteur + amplificateur + conditionneur + CAN} = $2{,}684$ °C$^{-1}$

### 1.2 Convertisseur Analogique/Numérique (CAN)

**Quantum (pas de quantification) :**
$$q = \frac{U_{PE}}{2^n - 1} \approx \frac{U_{PE}}{2^n}$$

avec $n$ = nombre de bits, $U_{PE}$ = tension pleine échelle.

**Erreur de quantification maximale :** $\pm q/2$

**Mot numérique correspondant à une tension $U$ :**
$$N = \text{round}\!\left(\frac{U}{q}\right) = \text{round}\!\left(\frac{U \cdot 2^n}{U_{PE}}\right)$$

**Fréquence d'échantillonnage minimale (théorème de Shannon–Nyquist) :**
$$f_e \geq 2 \cdot f_{max}$$
avec $f_{max}$ = fréquence maximale du signal à numériser.

*Source directe (2026 BAC3 Q.B13–B17) :* l'asservissement de température de la pile impose au moins 10 échantillons dans le régime transitoire (durée $t_{R5\%}$) → $T_e \leq t_{R5\%}/10$, soit $f_{min} = 10/t_{R5\%}$.

**Filtre anti-repliement :** doit couper toutes les fréquences $f > f_e/2$ avant l'échantillonneur-bloqueur.

**Échantillonneur-bloqueur (E/B) d'ordre zéro :** maintient la valeur échantillonnée constante pendant une période $T_e$.

### 1.3 Capteurs courants en IE

| Capteur | Grandeur | Principe | Précision typique |
|---------|----------|----------|-------------------|
| Thermocouple J | Temp. ($-40°C$ à $750°C$) | Seebeck | $\pm 2{,}5°C$ |
| Thermocouple K | Temp. ($-10°C$ à $1100°C$) | Seebeck | $\pm 2{,}5°C$ |
| Thermocouple T | Temp. ($-200°C$ à $350°C$) | Seebeck | $\pm 1°C$ |
| Pt100 / Pt1000 | Temp. | Résistance | $\pm 0{,}3°C$ |
| Codeur incrémental | Position / vitesse | Optique | $0{,}15$ mm/impulsion (2023) |
| Codeur absolu | Position | Gray | — |
| LVDT | Déplacement linéaire | Inductif | — |
| Capteur de pression SHD-U | Pression | Piézorésistif | — |
| Débitmètre électromagnétique | Débit | Faraday | — |
| Capteur de niveau différentiel | Hauteur | Pression différentielle | $6{,}67\,\%$ d'erreur max (2021) |

*Source (2024 Q.D1) :* choix entre thermocouple J et T pour mesure de $-20°C$ à $40°C$ — le jury attendait le type J (moins cher, précision suffisante).

### 1.4 Schéma électrique — normes et conventions (IEC 61082)

**Principes de représentation normalisée :**
- Alimentation : barreau positif en haut, négatif (ou neutre) en bas
- Lecture de gauche à droite, de haut en bas
- Contacts normalement ouverts (NO) et normalement fermés (NF) représentés hors tension
- Bobines indiquées par un rectangle ou un cercle

**Symboles courants (IEC/CEI 60617) :**

| Composant | Symbole |
|-----------|---------|
| Contacteur (bobine) | Cercle avec étiquette KM |
| Contact NO | Deux traits parallèles + barre |
| Contact NF | Deux traits + barre diagonale |
| Disjoncteur | Carré avec croix |
| Fusible | Rectangle |
| Résistance | Rectangle ou zigzag |
| Condensateur | Deux barres parallèles |
| Bobine | Spirale |
| Transformateur | Deux bobines couplées |
| Interrupteur différentiel | Symbole spécifique |

**Schéma unifilaire :** une seule ligne représente l'ensemble des conducteurs d'un circuit triphasé.

**Schéma développé (déployé) :** chaque conducteur est représenté séparément.

**Schéma de commande :** tension de commande (typiquement 24 V DC), logique de contact (contacts du schéma de puissance + contacts auxiliaires).

### 1.5 Incertitudes de mesure

**Incertitude type (Type A — statistique) :**
$$u_A = \frac{s}{\sqrt{n}} \quad \text{avec } s = \text{écart-type des mesures}$$

**Incertitude type (Type B — données constructeur) :**
$$u_B = \frac{a}{\sqrt{3}} \quad \text{(distribution uniforme)}$$

**Incertitude élargie :**
$$U = k \cdot u_c \quad \text{avec } k = 2 \text{ (probabilité 95 \%)}$$

**Propagation des incertitudes :**
$$u_c(y) = \sqrt{\sum_i \left(\frac{\partial f}{\partial x_i}\right)^2 u^2(x_i)}$$

*Source indirecte (2026 BAC3 Q.B12) :* calcul de l'erreur de mesure de la température à partir de l'erreur de quantification maximale.

### 1.6 Instruments de mesure

**Oscilloscope numérique :**
- Mesure de tensions, fréquences, déphasages, formes d'onde
- Déclenchement (trigger) sur front montant/descendant
- Mesure d'une fréquence : $f = 1/T$
- Mesure d'un déphasage : $\varphi = 360° \times \Delta t / T$

**Multimètre (voltmètre, ampèremètre, ohmmètre) :**
- En tension : branché en **parallèle** (résistance interne élevée)
- En courant : branché en **série** (résistance interne faible)
- En résistance : circuit hors tension

**Wattmètre / analyseur de réseau :**
- Mesure de puissance active $P$ [W], réactive $Q$ [VAR], apparente $S$ [VA]
- Facteur de puissance $\cos\varphi = P/S$

**Clamp-mètre (pince ampèremétrique) :** mesure du courant sans coupure du circuit.

---

## 2. QUESTIONS TYPES

**Q1.** (2026 BAC3 — Q.B11) Montrer que la sensibilité $S = \Delta G_N / \Delta T$ de la chaîne {capteur + amplificateur + conditionneur + CAN} est égale à $2{,}684\,°C^{-1}$. En déduire le gain de la chaîne et le mot numérique $N_C$ correspondant à $T_C = 55\,°C$ en binaire puis en hexadécimal.

**Q2.** (2026 BAC3 — Q.B12) Déterminer l'erreur de quantification maximale du CAN. En déduire l'erreur de mesure de la température. Conclure vis-à-vis du cahier des charges.

**Q3.** (2026 BAC3 — Q.B13–B14) Déterminer la durée du régime transitoire à 5 %. Établir l'inégalité sur la période d'échantillonnage $T_e$. Définir le rôle de l'échantillonneur-bloqueur.

**Q4.** (2026 BAC3 — Q.B17) Définir le rôle du filtre anti-repliement. Rappeler le théorème de Shannon. Déduire la fréquence de coupure $f_c$ du filtre anti-repliement.

**Q5.** (2021 — E2 Q.21–22) À partir de la caractéristique Volume = f(Hauteur), déterminer la relation linéaire $V = f(H)$. Quantifier l'erreur de modélisation maximale.

**Q6.** (2018 — Rapport jury / 2021 — Rapport jury) Réaliser le schéma électrique de commande d'un variateur de fréquence (puissance + commande), en raccordant les entrées-sorties de l'automate. Choisir le module Tesys U et justifier la référence du disjoncteur associé.

---

## 3. ATTENTES DU JURY

D'après les rapports de jury 2018, 2021, 2022, 2023, 2024, 2025 :

- **Schéma électrique** : point noir majeur, systématiquement signalé par le jury depuis 2018 :
  - « *La majorité des candidats ne semble pas maîtriser la conception d'un schéma électrique.* » (rapport 2018)
  - Moyenne de **4,8/20** sur la partie schéma en 2021
  - « *Le jury s'interroge sur la faiblesse générale des candidats dans la réalisation de schémas électriques.* » (rapport 2021)

- **Instrumentation** : le jury signale que les postes de travaux pratiques disposent de : « *oscilloscopes numériques, multimètres, dynamomètres, tachymètres, cartes d'acquisition* » — ces instruments doivent être parfaitement connus et utilisables.

- **Chaîne de mesure numérique** : questions récurrentes sur le CAN, la résolution, la précision, le théorème de Shannon.

- **Choix de capteurs** : justifier le choix d'un thermocouple J vs T, d'un codeur incrémental vs absolu.

- **Calcul d'incertitude** : rarement demandé de façon exhaustive, mais la notion d'erreur de quantification et d'erreur de mesure est systématiquement abordée.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur observée dans les sujets |
|----------|---------------------------------|
| Résolution CAN capteur température | $\varepsilon_{quant} = \pm q/2$ |
| Sensibilité chaîne de mesure (2026) | $2{,}684\,°C^{-1}$ |
| Consigne de température pile (2026) | $T_C = 55\,°C$ |
| Gain capteur température (2026) | $K_c = 0{,}0316\,V\cdot°C^{-1}$ |
| Pleine échelle capteur niveau (2021) | $H_{PE} = 2\,m$ ; hauteur max $= 1{,}6\,m$ |
| Courant 4 mA–20 mA → hauteur | $I_{mes} = \frac{16}{200}\,H + 4$ (2021) |
| Nombre de bits entrée analogique S7 | 16 bits signés (bit de signe sur MSB) |
| Constante de temps régime transitoire (2026) | $t_{R5\%}$ lu graphiquement $\approx 4\tau = 4 \times 0{,}9 = 3{,}6$ s |
| Précision codeur incrémental (2023) | $0{,}15\,mm$/impulsion |
| Précision requise position perche | $5\,mm$ ; 8 bits de poids fort retenus |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **Schéma électrique** : confondre le schéma de puissance et le schéma de commande ; oublier le commun 24 V sur les entrées logiques du variateur.
- **CAN** : confondre résolution ($n$ bits) et précision (erreur de quantification $\pm q/2$) ; oublier que l'erreur totale inclut d'autres sources (non-linéarité, bruit…).
- **Shannon** : la fréquence d'échantillonnage doit être **strictement supérieure** à $2 f_{max}$, pas égale.
- **Filtre anti-repliement** : placer la fréquence de coupure à $f_e/2$, mais dans la pratique bien en dessous pour assurer l'atténuation.
- **Thermocouple** : la f.é.m. Seebeck est faible (quelques mV), nécessite un amplificateur de précision et une compensation de soudure froide.
- **4–20 mA** : la valeur 0 mA signifie une coupure de câble (défaut), ce qui est un avantage par rapport à 0–10 V.
- **Symboles IEC** : ne pas utiliser des symboles américains (ANSI) à la place des symboles européens (IEC 60617).
- **Confusion voltmètre / ampèremètre** : un voltmètre en série protège la mesure mais la fausse ; un ampèremètre en parallèle peut détruire l'appareil.
- **Schéma unifilaire ou multifilaire** : utiliser un schéma unifilaire pour décrire un câblage borne à borne. L'unifilaire représente plusieurs conducteurs par un seul trait et donne une vue d'ensemble ; le câblage se lit sur un schéma multifilaire, avec le repérage des bornes et des conducteurs.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T26/T27 (asservissement)** : la chaîne de mesure (capteur + CAN) est l'élément de retour de la boucle ; sa précision et sa bande passante conditionnent directement les performances de l'asservissement.
- **T28/T29 (numérique)** : le CAN produit un mot binaire ; la conversion, le codage et le traitement en virgule fixe relèvent des thèmes de logique numérique et de programmation d'automate.
- **T15/T16 (convertisseurs)** : la mesure du courant, de la tension et de la puissance des convertisseurs nécessite les instruments de T30 (multimètre, wattmètre, oscilloscope).
- **T22 (électronique analogique)** : l'amplificateur opérationnel est au cœur du conditionnement des capteurs (pont de Wheatstone, amplificateur d'instrumentation).
- **Travaux pratiques (épreuve de leçon)** : le jury liste explicitement oscilloscopes, multimètres, tachymètres et cartes d'acquisition parmi les équipements des postes TP — ce thème est donc directement lié à la partie pratique du concours.
