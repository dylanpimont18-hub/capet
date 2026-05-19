# T04 — Transformateurs

> **Fréquence :** 4/22 sujets · **Intensité moyenne :** 🟡 Mentionné
> Présent dans les sujets de distribution électrique et adaptation de tension. Souvent en questions de dimensionnement.

---

## Notions clés

### Rapport de transformation

$$m = \frac{N_2}{N_1} = \frac{U_2}{U_1} = \frac{I_1}{I_2}$$

- $N_1$, $N_2$ : nombre de spires primaire et secondaire
- $U_1$, $U_2$ : tensions efficaces (à vide)
- La puissance est conservée : $S_1 = S_2$ (idéal)

### Transformateur idéal

| Grandeur | Relation |
|---|---|
| Tensions | $U_2 = m \cdot U_1$ |
| Courants | $I_1 = m \cdot I_2$ |
| Impédance ramenée | $Z'_2 = m^2 \cdot Z_2$ |
| Puissance apparente | $S = U_1 I_1 = U_2 I_2$ |

> ❌ **À mémoriser** : $Z_{vu\,du\,primaire} = Z_2 / m^2$

### Chute de tension en charge

$$\Delta U \approx \frac{P \cdot R_{cc} + Q \cdot X_{cc}}{U_n}$$

Où $R_{cc}$ et $X_{cc}$ sont les résistances et réactances de court-circuit ramenées à un enroulement.

### Pertes dans un transformateur

| Type de perte | Cause | Variation |
|---|---|---|
| Pertes fer $P_{Fe}$ | Hystérésis + courants de Foucault | Constantes (∝ U²) |
| Pertes cuivre $P_{Cu}$ | Effet Joule dans les enroulements | ∝ I² (charge) |
| **Rendement** | $\eta = P_{utile}/(P_{utile}+P_{Fe}+P_{Cu})$ | Max quand $P_{Fe} = P_{Cu}$ |

### Court-circuit d'un transformateur

$$U_{cc} = \frac{R_{cc} \cdot I_n}{U_n} \quad \text{(tension de court-circuit en %)}$$

Valeur typique : $u_{cc}$ = 4 à 6 % pour les transformateurs HTA/BT

### Couplage étoile-triangle (Dy)

- Primaire étoile, secondaire triangle : déphasage 30°
- Primaire triangle, secondaire étoile : déphasage −30°
- **Notation** : Dd0, Dy11, Yd1... le chiffre indique l'heure du déphasage (×30°)

---

## Types de questions au concours

| Type | Formule clé |
|---|---|
| Tension secondaire | $U_2 = m \cdot U_1 = (N_2/N_1) \cdot U_1$ |
| Courant primaire à pleine charge | $I_1 = S/(U_1)$ |
| Impédance vue du primaire | $Z'_2 = Z_2/m^2$ |
| Rendement | $\eta = 1 - (P_{Fe} + P_{Cu})/S$ |
| Puissance nominale | $S_n = U_n \cdot I_n$ (en kVA) |

---

## Pièges courants

1. **Rapport m** : certains sujets définissent $m = N_1/N_2$ (primaire/secondaire). Vérifier la convention du sujet.
2. **kVA ≠ kW** : la puissance d'un transformateur est en kVA (puissance apparente), pas en kW.
3. **Impedance ramenée** : le facteur est $m^2$, pas $m$. Très fréquent comme erreur.
4. **Puissance à vide ≠ puissance en charge** : à vide, seules les pertes fer existent.
