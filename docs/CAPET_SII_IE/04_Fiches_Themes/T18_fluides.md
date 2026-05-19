# T18 — Mécanique des fluides & hydraulique

> **Fréquence :** 5/22 sujets · **Intensité moyenne :** 🟡 Mentionné
> Présent dans les sujets pompes, STEP, traitement d'eau, fluides industriels. Questions sur les débits, pressions et dimensionnement de pompes.

---

## Notions clés

### Equation de continuité (conservation du débit)

$$Q_V = S_1 \cdot v_1 = S_2 \cdot v_2 = \text{cste}$$

- $Q_V$ : débit volumique (m³/s)
- $S$ : section de passage (m²)
- $v$ : vitesse du fluide (m/s)

**Débit massique :**
$$Q_m = \rho \cdot Q_V \quad \text{(kg/s)}$$

### Équation de Bernoulli (fluide parfait)

$$\frac{1}{2}\rho v^2 + \rho g z + P = \text{constante}$$

Entre deux points 1 et 2 :

$$\frac{1}{2}\rho v_1^2 + \rho g z_1 + P_1 = \frac{1}{2}\rho v_2^2 + \rho g z_2 + P_2 + \Delta P_{pertes}$$

**Composantes de la pression totale :**
- $\frac{1}{2}\rho v^2$ : pression dynamique (Pa)
- $\rho g z$ : pression hydrostatique (Pa)
- $P$ : pression statique (Pa)

> ❌ **À mémoriser** : $P_{tot} = P_{stat} + \frac{1}{2}\rho v^2 + \rho g z$

### Pertes de charge régulières (Darcy-Weisbach)

$$\Delta P = \lambda \cdot \frac{L}{D} \cdot \frac{\rho v^2}{2} \quad \text{ou} \quad J = \lambda \frac{v^2}{2gD} \text{ (m/m)}$$

- $\lambda$ : coefficient de frottement (Moody ou Blasius)
- $L$ : longueur (m)
- $D$ : diamètre (m)

**Approximation turbulente (Blasius) :**
$$\lambda \approx \frac{0{,}316}{Re^{0{,}25}} \quad \text{pour } 4000 < Re < 100000$$

### Hauteur manométrique totale (HMT)

$$HMT = \Delta z + \frac{\Delta P_{stat}}{\rho g} + \frac{\Delta v^2}{2g} + \sum h_{pertes}$$

En pratique simplifié :
$$HMT \approx z_2 - z_1 + \frac{P_2 - P_1}{\rho g} + h_{J}$$

### Puissance hydraulique d'une pompe

$$P_{hydraulique} = \rho \cdot g \cdot Q \cdot HMT$$

$$P_{électrique} = \frac{P_{hydraulique}}{\eta_{pompe} \cdot \eta_{moteur}}$$

> ❌ **À mémoriser** : $P_{hyd} = \rho g Q H$

### Point de fonctionnement

Le point de fonctionnement est l'intersection de :
- **Courbe pompe** $H_p(Q)$ : caractéristique fournie par le constructeur
- **Courbe réseau** $H_r(Q) = H_{statique} + k Q^2$ : hauteur statique + pertes de charge

```
  H
  │   Courbe pompe (↘)
  │  \  ← Point de fonctionnement
  │   ×
  │    \   Courbe réseau (↗)
  │     \  /
  └──────────── Q
```

### Similitude des pompes (lois de similitude)

$$\frac{Q_1}{Q_2} = \frac{N_1}{N_2}, \quad \frac{H_1}{H_2} = \left(\frac{N_1}{N_2}\right)^2, \quad \frac{P_1}{P_2} = \left(\frac{N_1}{N_2}\right)^3$$

> Économies importantes sur la puissance en variant la vitesse : réduire $N$ de 20 % → $P$ réduite de $0{,}8^3 = 51\%$ !

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Vitesse dans une section | $v_2 = Q/S_2 = v_1 S_1/S_2$ |
| Puissance hydraulique | $P = \rho g Q H$ |
| Pression différentielle | Bernoulli entre deux points |
| HMT à partir du réseau | $HMT = \Delta z + h_{pertes}$ |
| Puissance moteur pompe | $P_{mot} = \rho g Q H / \eta_{pompe}$ |

---

## Pièges courants

1. **Unités** : $Q$ en m³/s (pas L/min — convertir !), $H$ en m, $\rho$ en kg/m³, $g$ = 9,81 m/s².
2. **Bernoulli sans pertes** : l'équation de base est pour un fluide parfait. Avec pertes, ajouter $\Delta P_{pertes}$ au membre de droite.
3. **Loi en $N^3$** : la puissance d'une pompe à vitesse variable varie avec le cube de la vitesse. C'est l'argument principal pour utiliser des variateurs de vitesse sur les pompes.
4. **HMT ≠ pression** : la HMT est une hauteur (mètres), pas une pression (Pa). $\Delta P = \rho g \cdot HMT$.
