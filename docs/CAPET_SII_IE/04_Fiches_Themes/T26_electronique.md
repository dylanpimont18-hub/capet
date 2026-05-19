# T26 — Électronique

> **Fréquence :** 5/22 sujets · **Intensité moyenne :** 🟡 Mentionné
> Ampli-op, transistors de commutation, diodes. Présent dans les sujets de conditionnement de capteurs et d'interface de commande.

---

## Notions clés

### Amplificateur opérationnel (AOP) idéal

**Hypothèses de l'AOP idéal :**
- $V_+ = V_-$ (égalisation des entrées en contre-réaction négative)
- $I_+ = I_- = 0$ (pas de courant dans les entrées)
- Gain différentiel infini en boucle ouverte : $A_d \to \infty$

### Montages de base

**Amplificateur non-inverseur :**
$$V_{out} = V_{in} \cdot \left(1 + \frac{R_2}{R_1}\right)$$

```
    Vin ──────────── V+ ──────┐
                    AOP       │
         ┌── R2 ── V- ─ Vout ─┤
         │                    │
         R1                   │
         │                    │
        GND                  Vout
```

**Amplificateur inverseur :**
$$V_{out} = -V_{in} \cdot \frac{R_2}{R_1}$$

**Suiveur de tension (gain = 1) :**
$$V_{out} = V_{in}$$

(Cas particulier du non-inverseur avec $R_1 \to \infty$ ou $R_2 = 0$)

**Additionneur inverseur :**
$$V_{out} = -\left(\frac{R_f}{R_1} V_1 + \frac{R_f}{R_2} V_2\right)$$

**Intégrateur :**
$$V_{out} = -\frac{1}{RC} \int V_{in}\, dt$$

**Dérivateur :**
$$V_{out} = -RC \cdot \frac{dV_{in}}{dt}$$

**Comparateur :**
- Pas de contre-réaction
- $V_{out} = V_{sat+}$ si $V_+ > V_-$
- $V_{out} = V_{sat-}$ si $V_+ < V_-$

### Diode

**Caractéristique I-V :**
$$I_D = I_s \left(e^{V_D/V_T} - 1\right) \approx I_s e^{V_D/V_T}$$

- $V_T \approx 26$ mV à 25°C (tension thermique)
- Modèle simplifié : $V_D = 0{,}7$ V (Si) en conduction

**Diode Zener :** régulation de tension — claquage en inverse à $V_Z$

### Transistor en commutation (MOSFET/BJT)

**BJT (NPN) en commutation :**
- **Saturation** (fermé) : $V_{CE} \approx 0{,}2$ V, $I_C = V_{CC}/R_C$
- **Blocage** (ouvert) : $I_C \approx 0$

Condition de saturation : $I_B \geq I_C / h_{FE}$

**MOSFET en commutation :**
- **Passant** : $R_{DS,on}$ faible, $V_{DS} = R_{DS,on} \cdot I_D$
- **Bloqué** : $I_D \approx 0$
- Commandé en tension ($V_{GS} > V_{th}$ pour conduire)

### Pont diviseur de tension (conditionnement résistif)

$$V_{out} = V_{cc} \cdot \frac{R_2}{R_1 + R_2}$$

Avec un capteur résistif $R_{capteur}$ à la place de $R_2$ :
$$V_{out} = V_{cc} \cdot \frac{R_{capteur}}{R_{fixe} + R_{capteur}}$$

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Gain amplificateur non-inverseur | $G = 1 + R_2/R_1$ |
| Gain amplificateur inverseur | $G = -R_2/R_1$ |
| Tension seuil comparateur | $V_{seuil} = V_{ref}$ (entrée $V_-$) |
| Conditionnement capteur résistif | $V = V_{cc} \cdot R_{capteur}/(R + R_{capteur})$ |
| Courant de base BJT | $I_B = I_C/h_{FE}$ |

---

## Pièges courants

1. **Inverseur vs non-inverseur** : l'inverseur ajoute un signe $-$ sur $V_{out}$. Si la polarité est critique, vérifier.
2. **AOP idéal en comparateur** : sans contre-réaction, l'AOP n'est plus idéal au sens précédent — il n'y a plus $V_+ = V_-$.
3. **MOSFET vs BJT** : le MOSFET est commandé en tension (pas de courant de grille), le BJT nécessite un courant de base.
4. **Saturation de l'AOP** : $V_{out}$ est limité à $\pm V_{alim}$ (ou $\pm(V_{alim} - 1{,}5\,V)$ pour les AOP non rail-to-rail).
