# T20 — Capteurs & mesure

> **Fréquence :** 6/22 sujets · **Intensité moyenne :** 🟠 Important
> Présent dans les sujets de régulation et supervision. Questions sur le choix du capteur, le conditionnement du signal et la chaîne de mesure.

---

## Notions clés

### Caractéristiques d'un capteur

| Paramètre | Définition |
|---|---|
| Étendue de mesure | Plage de valeurs mesurables (ex. −10 à 150 °C) |
| Sensibilité | $S = \Delta V_{out}/\Delta X$ (V/°C, mV/Pa...) |
| Résolution | Plus petite variation détectable |
| Linéarité | Écart par rapport à la droite idéale |
| Temps de réponse | $t_{63\%}$ ou $t_{95\%}$ à un échelon |
| Précision / exactitude | Écart systématique par rapport à la valeur vraie |

### Capteur résistif (thermistance, jauge de contrainte)

**CTN (Coefficient de Température Négatif) :**
$$R(T) = R_0 \cdot e^{B(1/T - 1/T_0)}$$

**CTP (Coefficient Positif) :**
$$R(T) = R_0 \cdot (1 + \alpha \cdot \Delta T) \quad (\text{métal, Pt100})$$

Pt100 : $R_0 = 100\,\Omega$ à 0 °C, $\alpha = 3{,}85 \times 10^{-3}\,°C^{-1}$

**Jauge de contrainte :**
$$\frac{\Delta R}{R} = k \cdot \varepsilon \quad \text{(k = facteur de jauge ≈ 2)}$$

### Thermocouple

- Effet Seebeck : FEM $e = S_{AB} \cdot \Delta T$
- Types K (chromel-alumel), J, T, E...
- Type K : $S \approx 41\,\mu V/°C$
- Nécessite une compensation de soudure froide (CJC)

### Capteur de position

**Codeur incrémental :**
- $N$ impulsions par tour
- Résolution angulaire : $\theta_{res} = 360°/N$
- Vitesse : $n = f_{impulsions}/(N \cdot 60)$ (tr/min)

**Résolveur :**
- Signaux sinus/cosinus : position absolue par arctan

**Capteur inductif / LVDT :**
- Linéaire, robuste, mesure déplacement
- Sortie : tension proportionnelle à la position

### Signal de capteur — conditionnement

**4–20 mA (boucle de courant) :**
$$I = 4 + 16 \cdot \frac{X - X_{min}}{X_{max} - X_{min}} \quad (mA)$$

- 4 mA = valeur minimale (0 % de l'étendue)
- 20 mA = valeur maximale (100 % de l'étendue)
- Avantage : résistant au bruit, détection de rupture fil (I < 4 mA)

> ❌ **À mémoriser** : $I = 4 + 16 \cdot \frac{X-X_{min}}{X_{max}-X_{min}}$

**0–10 V :**
$$V = 10 \cdot \frac{X - X_{min}}{X_{max} - X_{min}}$$

### Conversion analogique-numérique (CAN)

$$\text{Résolution} = \frac{V_{ref}}{2^n - 1} \approx \frac{V_{ref}}{2^n}$$

- $n$ : nombre de bits
- 8 bits : 256 niveaux, résolution ≈ 0,4 % de pleine échelle
- 12 bits : 4096 niveaux, résolution ≈ 0,02 %

**Théorème de Shannon :**
$$f_e \geq 2 \cdot f_{max,signal}$$

### Pont de Wheatstone (capteur résistif)

$$V_{out} = V_{alim} \cdot \frac{R_1}{R_1 + R_2} - V_{alim} \cdot \frac{R_3}{R_3 + R_4}$$

À l'équilibre ($V_{out} = 0$) : $R_1 R_4 = R_2 R_3$

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Signal courant pour mesurande $X$ | $I = 4 + 16(X-X_{min})/(X_{max}-X_{min})$ |
| Retour valeur à partir signal 4-20mA | $X = X_{min} + (X_{max}-X_{min})(I-4)/16$ |
| Résolution d'un CAN $n$ bits | $\Delta V = V_{ref}/2^n$ |
| Fréquence d'échantillonnage | $f_e \geq 2 f_{max}$ |
| Pt100 à température $T$ | $R = 100(1 + 3{,}85\times10^{-3} T)$ |

---

## Pièges courants

1. **4 mA ≠ 0** : dans une boucle 4-20 mA, le zéro physique correspond à 4 mA, pas à 0 mA.
2. **Shannon** : $f_e \geq 2f_{max}$. Si $f_{max}$ = 50 Hz, alors $f_e \geq 100$ Hz. En pratique, prendre $f_e = 5$ à 10 $\times f_{max}$.
3. **CAN** : la résolution est $V_{ref}/2^n$, mais l'erreur quantification maximale est $\pm\frac{1}{2} \cdot V_{ref}/2^n$.
4. **Thermocouple** : la mesure est une différence de température entre la soudure chaude et la soudure froide. Sans compensation CJC, l'erreur peut être importante.
