# T06 — Redresseurs

> **Fréquence :** 6/22 sujets · **Intensité moyenne :** 🟠 Important
> ⚠️ **Point aveugle signalé jury** : lacune fréquente sur les valeurs moyennes et efficaces. Thème présent dans les sujets alimentation, industrie, traction.

---

## Notions clés

### Redresseur monophasé simple alternance (P1)

```
    ~─[D]─┬──→ +Vd
          [R]
    ~─────┴──→ -
```

$$V_{d0} = \frac{V_{max}}{\pi} = \frac{\sqrt{2} \cdot V_{eff}}{\pi} \approx 0{,}45 \cdot V_{eff}$$

### Redresseur monophasé pont (PD2 — pont de Graetz)

$$V_{d0} = \frac{2 \cdot V_{max}}{\pi} = \frac{2\sqrt{2} \cdot V_{eff}}{\pi} \approx 0{,}90 \cdot V_{eff}$$

> ❌ **À mémoriser** : $V_{d0} = 0{,}90 \cdot V_{eff}$ (pont monophasé)

### Redresseur triphasé pont (PD3 — pont de Graetz triphasé)

$$V_{d0} = \frac{3\sqrt{2}}{\pi} \cdot V_{composée,eff} \approx 1{,}35 \cdot V_{composée,eff}$$

Ou en fonction de la tension simple : $V_{d0} = \frac{3\sqrt{6}}{\pi} \cdot V_{simple,eff} \approx 2{,}34 \cdot V_{simple,eff}$

> ❌ **À mémoriser** : $V_{d0} = 1{,}35 \cdot U_{composée}$ (pont triphasé)

### Taux d'ondulation

$$\tau = \frac{\Delta V_d}{V_{d0}} \quad \text{(plus } \tau \text{ est faible, mieux c'est)}$$

| Redresseur | Fréquence d'ondulation | $\tau$ sans filtre |
|---|---|---|
| P1 (1 diode) | $f_{réseau}$ | ~1,21 |
| PD2 (pont mono) | $2 \cdot f_{réseau}$ | ~0,48 |
| PD3 (pont tri) | $6 \cdot f_{réseau}$ | ~0,04 |

### Filtrage par condensateur

$$C = \frac{I_d}{f_{ondulation} \cdot \Delta V} = \frac{P/U_d}{f_r \cdot \Delta V}$$

> ❌ **À mémoriser** : $C \approx \frac{I_{charge}}{f_r \cdot \Delta U_{max}}$

### Valeurs efficaces et moyennes

| Signal | Valeur efficace | Valeur moyenne |
|---|---|---|
| Sinusoïde $v = V_{max}\sin(\omega t)$ | $V_{eff} = V_{max}/\sqrt{2}$ | 0 |
| Redressé mono-alternance | $V_{eff} = V_{max}/2$ | $V_{moy} = V_{max}/\pi$ |
| Redressé double-alternance | $V_{eff} = V_{max}/\sqrt{2}$ | $V_{moy} = 2V_{max}/\pi$ |

---

## Redresseur commandé (thyristors)

$$V_d = V_{d0} \cdot \cos\alpha$$

- $\alpha$ : angle d'amorçage (0° à 90° → redressement ; 90° à 180° → onduleur)

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Tension continue d'un pont monophasé | $V_{d0} = 0{,}90 \cdot V_{eff}$ |
| Tension continue d'un pont triphasé | $V_{d0} = 1{,}35 \cdot U_{composée}$ |
| Dimensionner un condensateur de filtrage | $C = I_d/(f_r \cdot \Delta U)$ |
| Courant moyen dans une diode (pont mono) | $I_{D,moy} = I_d/2$ |
| Courant moyen dans une diode (pont tri) | $I_{D,moy} = I_d/3$ |

---

## Pièges courants

1. **0,90 vs 0,45** : le pont (double-alternance) donne $0{,}90 \cdot V$ ; la simple alternance donne $0{,}45 \cdot V$.
2. **Tension d'entrée** : pour le pont triphasé, vérifier si $V_{eff}$ est la tension composée (400 V) ou simple (230 V).
3. **Courant efficace $\neq$ courant moyen** : $I_{eff} = I_{max}/\sqrt{2}$ pour une sinusoïde, mais $I_{moy} = 2I_{max}/\pi$ pour une sinusoïde redressée.
4. **Diodes réelles** : chute de tension $V_D \approx 0{,}7$ V → $V_d = V_{d0} - n \cdot V_D$ ($n$ = nombre de diodes en série).
