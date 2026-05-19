# T01 — Grandeurs électriques & électrocinétique

> **Fréquence :** 10/22 sujets · **Intensité moyenne :** 🟠 Important
> Thème fondamental : lois de base, circuits RLC, régimes transitoires. Souvent en questions préliminaires.

---

## Notions clés

### Lois de Kirchhoff

| Loi | Énoncé | Formule |
|---|---|---|
| Loi des nœuds | Somme des courants entrants = sortants | $\sum I_{entrant} = \sum I_{sortant}$ |
| Loi des mailles | Somme algébrique des tensions = 0 | $\sum U_k = 0$ |

### Composants passifs — impédances

| Composant | Résistance/Réactance | Comportement DC | Comportement AC (ω) |
|---|---|---|---|
| Résistance R | $Z = R$ | Normal | Normal |
| Inductance L | $Z = jL\omega$ | Court-circuit | Augmente avec ω |
| Condensateur C | $Z = \frac{1}{jC\omega}$ | Circuit ouvert | Diminue avec ω |

> ❌ **À mémoriser** : $Z_L = jL\omega$ et $Z_C = \frac{1}{jC\omega}$

### Diviseur de tension

$$U_2 = U_1 \cdot \frac{Z_2}{Z_1 + Z_2}$$

### Diviseur de courant

$$I_2 = I_{tot} \cdot \frac{Z_1}{Z_1 + Z_2}$$

### Énergie stockée

| Composant | Énergie stockée |
|---|---|
| Inductance | $E_L = \frac{1}{2}LI^2$ |
| Condensateur | $E_C = \frac{1}{2}CU^2$ |

### Régimes transitoires (1er ordre)

**Réponse d'un circuit RC ou RL** à un échelon :

$$u(t) = U_\infty + (U_0 - U_\infty) \cdot e^{-t/\tau}$$

- Constante de temps : $\tau = RC$ (condensateur) ou $\tau = L/R$ (inductance)
- À $t = \tau$ : la variable atteint 63 % de sa valeur finale
- À $t = 5\tau$ : régime permanent atteint (99 %)

```
  u(t)
  U∞ ─────────────────────────
     |        (1-e^{-t/τ})
  U0 ├──
     |
     └──────────────────> t
           τ    5τ
```

### Circuit RLC série (2e ordre)

$$\omega_0 = \frac{1}{\sqrt{LC}}, \quad m = \frac{R}{2}\sqrt{\frac{C}{L}}$$

- m < 1 : régime sous-amorti (oscillations)
- m = 1 : régime critique (retour rapide sans oscillation)
- m > 1 : régime sur-amorti

### Pont de Wheatstone

$$\frac{R_1}{R_2} = \frac{R_3}{R_4} \Rightarrow U_{AB} = 0 \quad \text{(pont équilibré)}$$

> ⚠️ **Signalé jury 2025** : moins de 20 % des candidats traitent les questions sur ce pont

---

## Types de questions au concours

| Type | Formule clé |
|---|---|
| Calcul courant de ligne | $I = U/Z$ ou loi des nœuds |
| Énergie stockée dans un condensateur de bus | $E_C = \frac{1}{2}CU^2$ |
| Constante de temps d'un filtre | $\tau = RC$ ou $L/R$ |
| Fréquence de coupure | $f_c = 1/(2\pi RC)$ |
| Bilan de puissance en circuit résistif | $P = RI^2 = U^2/R = UI$ |

---

## Pièges courants

1. **Signe dans les mailles** : choisir un sens de parcours et s'y tenir. Une source de tension en sens inverse change le signe.
2. **Impédance ≠ résistance** : L et C sont des impédances complexes, pas des résistances pures.
3. **Pont de Wheatstone** : trop souvent ignoré. Mémoriser la condition d'équilibre $R_1R_4 = R_2R_3$.
4. **Unités** : R en Ω, L en H, C en F. Attention aux µF, mH, kΩ dans les données.
