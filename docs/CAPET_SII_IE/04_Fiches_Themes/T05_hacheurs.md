# T05 — Hacheurs / Convertisseurs DC-DC

> **Fréquence :** 8/22 sujets · **Intensité moyenne :** 🟠 Important
> Thème récurrent dans les sujets véhicules électriques, robotique, systèmes embarqués. Dimensionnement des hacheurs série/parallèle et calcul de l'ondulation.

---

## Notions clés

### Hacheur série (abaisseur / Buck)

```
    + ─────[K]────────────[L]─────── +
    |         |           |          |
   Vs        [D]         [C]        Vs·α
    |         |           |          |
    - ────────┴───────────┴───────── -
```

$$U_s = \alpha \cdot U_e \qquad \text{avec } 0 \le \alpha \le 1$$

- $\alpha = t_{on}/T$ : rapport cyclique
- $U_s < U_e$ : tension de sortie inférieure à l'entrée
- Courant inducteur continu en régime établi : $I_L = I_{sortie}$

### Hacheur parallèle (élévateur / Boost)

$$U_s = \frac{U_e}{1-\alpha}$$

- $U_s > U_e$ : tension de sortie supérieure à l'entrée
- Attention : $\alpha \to 1$ ⟹ $U_s \to \infty$ (non physique — limité par les pertes)

### Hacheur 4 quadrants (Buck-Boost)

$$U_s = \frac{\alpha}{1-\alpha} \cdot U_e \qquad \text{(buck-boost)}$$

### Ondulation de courant (hacheur Buck)

$$\Delta I_L = \frac{U_e \cdot \alpha \cdot (1-\alpha)}{L \cdot f_s} = \frac{(U_e - U_s) \cdot \alpha}{L \cdot f_s}$$

> ❌ **À mémoriser** : $\Delta I_L = \frac{U_e - U_s}{L} \cdot \alpha \cdot T$

### Ondulation de tension (condensateur de sortie)

$$\Delta U_C = \frac{\Delta I_L}{8 \cdot C \cdot f_s}$$

### Bilan énergétique (idéal)

$$P_{entrée} = P_{sortie} \Rightarrow U_e \cdot I_e = U_s \cdot I_s \Rightarrow I_e = \alpha \cdot I_s \text{ (Buck)}$$

### Énergie stockée dans l'inductance

$$E_L = \frac{1}{2} L I^2$$

Le courant moyen dans l'inductance = courant de charge : $I_{L,moy} = I_s$

---

## Synthèse des topologies

| Topologie | Rapport $U_s/U_e$ | Application |
|---|---|---|
| Buck (série) | $\alpha$ | Charge batterie, alimentations |
| Boost (parallèle) | $1/(1-\alpha)$ | Récupération frein, PV |
| Buck-Boost | $\alpha/(1-\alpha)$ | Batterie bi-directionnelle |
| Pont H (4Q) | $\pm(2\alpha-1)$ | Moteur DC réversible |

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Tension de sortie d'un Buck | $U_s = \alpha \cdot U_e$ |
| Rapport cyclique à partir de $U_s/U_e$ | $\alpha = U_s/U_e$ |
| Courant moyen de l'inductance | $I_{L,moy} = I_s = P_s/U_s$ |
| Fréquence de commutation minimale | $f_s = (U_e - U_s)\alpha / (L \cdot \Delta I_{max})$ |
| Dimensionner L pour $\Delta I$ | $L = (U_e - U_s)\alpha / (f_s \cdot \Delta I)$ |

---

## Pièges courants

1. **Buck vs Boost** : confondre les formules. Buck = $\alpha$, Boost = $1/(1-\alpha)$.
2. **$\alpha$** est sans unité, $0 \le \alpha \le 1$. Ne pas exprimer en %.
3. **Courant inducteur** : $I_{L,moy} = I_{sortie}$ pour Buck, mais $I_{L,moy} = I_{entrée}$ pour Boost.
4. **Régime discontinu** : si $I_{L,min} < 0$, la diode bloque → analyse différente. Vérifier $I_{L,min} = I_{L,moy} - \Delta I_L/2 > 0$.
