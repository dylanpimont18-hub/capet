# T27 — Matériaux électriques

> **Fréquence :** 3/22 sujets · **Intensité moyenne :** 🟡 Mentionné
> Présent dans les sujets de câblage, dimensionnement de conducteurs et choix de matériaux isolants.

---

## Notions clés

### Résistivité et résistance d'un conducteur

$$R = \rho \cdot \frac{L}{S}$$

- $\rho$ : résistivité (Ω·m)
- $L$ : longueur (m)
- $S$ : section (m²)

> ❌ **À mémoriser** : $R = \rho L/S$

### Résistivités courantes

| Matériau | $\rho$ (Ω·m) à 20°C |
|---|---|
| Cuivre (Cu) | $1{,}72 \times 10^{-8}$ |
| Aluminium (Al) | $2{,}82 \times 10^{-8}$ |
| Argent (Ag) | $1{,}59 \times 10^{-8}$ |
| Fer | $10^{-7}$ |
| Nickel | $7 \times 10^{-8}$ |

### Influence de la température

$$R(T) = R_0 \cdot [1 + \alpha (T - T_0)]$$

- $\alpha$ : coefficient de température (1/°C)
- Cuivre : $\alpha_{Cu} \approx 3{,}9 \times 10^{-3}$ °C$^{-1}$
- Aluminium : $\alpha_{Al} \approx 4{,}3 \times 10^{-3}$ °C$^{-1}$

### Conducteurs et câbles

**Densité de courant admissible :**
$$J = I/S \quad (A/m^2)$$

Valeur typique câble cuivre : $J_{max}$ = 1 à 6 A/mm² selon refroidissement

**Chute de tension dans un câble :**
$$\Delta U = R \cdot I = \rho \cdot \frac{L}{S} \cdot I$$

Critère NF C 15-100 : $\Delta U \leq 3\%$ de $U_n$ (circuits terminaux), $\leq 5\%$ total

### Semi-conducteurs

| Matériau | $E_{gap}$ (eV) | $T_{max}$ | Usage |
|---|---|---|---|
| Silicium (Si) | 1,12 | ~150°C | Diodes, transistors, IGBT |
| Carbure de silicium (SiC) | 3,26 | ~250°C | MOSFET haute tension |
| Nitrure de gallium (GaN) | 3,44 | ~150°C | Haute fréquence |

### Perméabilité magnétique

$$B = \mu_0 \mu_r H \quad \text{avec } \mu_0 = 4\pi \times 10^{-7} \text{ H/m}$$

| Matériau | $\mu_r$ |
|---|---|
| Vide / Air | 1 |
| Aluminium | ≈ 1 |
| Fer doux | 1 000 – 10 000 |
| Ferrite | 1 000 – 15 000 |
| Acier laminé | 500 – 5 000 |

### Isolants électriques

| Matériau | Rigidité diélectrique (kV/mm) | $T_{max}$ |
|---|---|---|
| Air | ≈ 3 | — |
| PVC | 15 – 35 | 70°C |
| XLPE (polyéthylène réticulé) | 20 – 40 | 90°C |
| SF₆ | ≈ 80 | — |
| Résine époxy | 20 – 50 | 130°C |

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Résistance d'un câble | $R = \rho L/S$ |
| Chute de tension | $\Delta U = RI = \rho L I / S$ |
| Section minimale de câble | $S = \rho L I / \Delta U_{max}$ |
| Résistance à chaud | $R(T) = R_0[1+\alpha(T-T_0)]$ |
| Pertes par effet Joule | $P_J = R I^2 = \rho L I^2/S$ |

---

## Pièges courants

1. **mm² vs m²** : les sections de câbles sont en mm², mais $\rho$ est en Ω·m. Convertir : $S_{m^2} = S_{mm^2} \times 10^{-6}$.
2. **Cu vs Al** : l'aluminium est plus résistif que le cuivre mais plus léger. Pour la même résistance, il faut une section 1,64× plus grande.
3. **$\mu_r$** : l'air a $\mu_r = 1$, pas 0. Pour calculer le champ $B$ dans l'air : $B = \mu_0 H$.
4. **Chute de tension aller-retour** : la longueur du câble c'est L aller + L retour = 2L pour un circuit monophasé.
