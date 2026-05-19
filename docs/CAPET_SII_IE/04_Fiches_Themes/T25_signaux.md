# T25 — Signaux & traitement du signal

> **Fréquence :** 5/22 sujets · **Intensité moyenne :** 🟡 Mentionné
> Présent dans les sujets de communication, mesure et traitement de données. Questions sur la représentation des signaux, l'échantillonnage et les filtres.

---

## Notions clés

### Types de signaux

| Type | Description | Exemple |
|---|---|---|
| Analogique continu | Valeur continue dans le temps | Signal capteur |
| Numérique discret | Suite d'échantillons quantifiés | Signal Arduino |
| Périodique | $x(t+T) = x(t)$ | Sinusoïde, PWM |
| Aléatoire | Caractère statistique | Bruit thermique |

### Représentation d'un signal sinusoïdal

$$x(t) = X_{max} \cdot \sin(\omega t + \varphi) = X_{max} \cdot \sin(2\pi f t + \varphi)$$

- Valeur efficace : $X_{eff} = \frac{X_{max}}{\sqrt{2}}$
- Valeur moyenne sur une période : 0 (sinusoïde pure)
- Puissance : $P = \frac{X_{eff}^2}{R}$ ou $P = X_{eff} \cdot I_{eff} \cdot \cos\varphi$

### Décomposition en série de Fourier

Tout signal périodique peut s'écrire :
$$x(t) = a_0 + \sum_{n=1}^{\infty} a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t)$$

- $a_0$ : composante continue (valeur moyenne)
- $n = 1$ : fondamental (fréquence $f_0 = 1/T$)
- $n \geq 2$ : harmoniques

**THD (Taux de Distorsion Harmonique) :**
$$THD = \frac{\sqrt{X_2^2 + X_3^2 + \cdots}}{X_1} \times 100\%$$

### Échantillonnage & théorème de Shannon-Nyquist

$$f_e \geq 2 \cdot f_{max}$$

- $f_e$ : fréquence d'échantillonnage
- $f_{max}$ : fréquence maximale du signal à numériser
- Si $f_e < 2f_{max}$ → **repliement spectral** (aliasing) → signal déformé

**En pratique :** $f_e = 5$ à $10 \times f_{max}$

### Quantification & résolution

$$\Delta = \frac{V_{max} - V_{min}}{2^n} \quad \text{(quantum — pas de quantification)}$$

- $n$ = nombre de bits du CAN
- Erreur max de quantification : $\pm \Delta/2$

### Filtres

| Type | Passe | Bloque | Exemple |
|---|---|---|---|
| Passe-bas | Basse fréquence | Haute fréquence | Anti-repliement avant CAN |
| Passe-haut | Haute fréquence | Basse fréquence | Suppression DC |
| Passe-bande | Bande centrée | Reste | Radio, audio |
| Coupe-bande | Tout sauf bande | Bande | Éliminateur 50 Hz |

**Filtre RC passe-bas du 1er ordre :**
$$H(f) = \frac{1}{1 + j f/f_c} \quad \text{avec } f_c = \frac{1}{2\pi RC}$$

**Filtre RL passe-haut du 1er ordre :**
$$H(f) = \frac{jf/f_c}{1 + jf/f_c} \quad \text{avec } f_c = \frac{R}{2\pi L}$$

### Transformée de Fourier (DFT)

- Permet de passer du domaine temporel au domaine fréquentiel
- En pratique : FFT (Fast Fourier Transform) sur les signaux numériques
- Résolution fréquentielle : $\Delta f = f_e / N$ ($N$ = nombre de points)

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Valeur efficace | $X_{eff} = X_{max}/\sqrt{2}$ |
| Fréquence d'échantillonnage min | $f_e = 2 f_{max}$ |
| Résolution CAN | $\Delta = V_{ref}/2^n$ |
| Fréquence de coupure RC | $f_c = 1/(2\pi RC)$ |
| THD | $\sqrt{\sum_{n\geq2} X_n^2}/X_1$ |

---

## Pièges courants

1. **$\sqrt{2}$ vs $2$** : valeur efficace = pic / $\sqrt{2}$, valeur moyenne redressée = pic $\times 2/\pi \approx$ pic $\times 0{,}637$.
2. **Shannon** : $f_e \geq 2f_{max}$, pas $f_e \geq f_{max}$.
3. **THD** : ne pas inclure le fondamental ($X_1$) dans la somme du numérateur.
4. **Repliement spectral** : si l'aliasing est présent, il est impossible de le corriger après échantillonnage. La prévention se fait en amont avec un filtre anti-repliement.
