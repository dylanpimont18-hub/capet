# T17 — Froid & climatisation

> **Fréquence :** 5/22 sujets · **Intensité moyenne :** 🟡 Mentionné
> Présent dans les sujets de traitement d'air, bâtiments, data centers. Étroitement lié à T03 (thermique). Questions sur le COP et les bilans thermiques.

---

## Notions clés

### Cycle frigorifique à compression

```
    Condenseur  ← Q_c →  Ambiance haute température
         ↓                       ↑
    Détente (détendeur)       Compresseur (W)
         ↓                       ↑
    Évaporateur  ← Q_f →  Source froide (local à refroidir)
```

**Bilan énergétique :**
$$W = Q_c - Q_f \qquad \text{(1er principe)}$$

### COP (Coefficient of Performance)

**Machine frigorifique (refroidir) :**
$$COP_f = \frac{Q_f}{W} = \frac{Q_f}{Q_c - Q_f}$$

**Pompe à chaleur (chauffer) :**
$$COP_c = \frac{Q_c}{W} = \frac{Q_c}{Q_c - Q_f} = COP_f + 1$$

> ❌ **À mémoriser** : $COP_c = COP_f + 1$

**COP de Carnot (maximum théorique) :**
$$COP_{f,Carnot} = \frac{T_f}{T_c - T_f} \qquad \text{(températures en Kelvin !)}$$

$$COP_{c,Carnot} = \frac{T_c}{T_c - T_f}$$

### Conversion °C ↔ Kelvin

$$T(K) = T(°C) + 273$$

⚠️ Toujours utiliser les températures en Kelvin pour le COP de Carnot.

### Fluides frigorigènes

| Fluide | Type | GWP | Usage |
|---|---|---|---|
| R134a | HFC | 1430 | Réfrigérateurs, climatiseurs |
| R410A | HFC | 2088 | Climatiseurs splits |
| R32 | HFC | 675 | Climatiseurs (remplacement R410A) |
| R290 (propane) | HC | 3 | Petit froid (naturel) |
| R744 (CO₂) | naturel | 1 | Supercritique, froid commercial |

GWP = Global Warming Potential (référence CO₂ = 1)

### Bilan thermique d'un bâtiment

$$P_{thermique} = Q_{parois} + Q_{renouvellement\,air} + Q_{apports\,internes}$$

$$Q_{parois} = U_{mur} \cdot A \cdot \Delta T$$

- $U$ : coefficient de transmission thermique (W/m²·K)
- Lié à la résistance thermique : $R_{th} = 1/U$ (m²·K/W)

### SCOP / SEER

- **SCOP** : COP moyen saisonnier en chauffage
- **SEER** : COP saisonnier en refroidissement
- Mesurés selon EN 14825 (conditions météo européennes)
- Valeurs typiques : SCOP = 3 à 5, SEER = 4 à 8

---

## Types de questions au concours

| Type | Formule |
|---|---|
| COP d'une pompe à chaleur | $COP_c = Q_c/W$ |
| Relation chaud/froid/travail | $Q_c = Q_f + W$ |
| COP maximum (Carnot, froid) | $COP_f = T_f/(T_c - T_f)$ |
| Puissance électrique nécessaire | $W = Q_c/COP_c$ |
| Coût exploitation annuel | $E_{élec} = W \times h_{an}$, coût = $E \times c_{kWh}$ |

---

## Pièges courants

1. **$COP_c = COP_f + 1$** : en mode PAC, le COP est toujours supérieur à 1. C'est normal physiquement : on "déplace" l'énergie plutôt que de la créer.
2. **Températures en Kelvin** pour Carnot : $T_f = 5°C = 278$ K, $T_c = 35°C = 308$ K → $COP_{Carnot} = 278/(308-278) = 9{,}3$.
3. **COP réel ≪ COP Carnot** : un COP réel de 3 pour un Carnot de 9 est tout à fait normal (irréversibilités).
4. **PAC vs groupe froid** : même cycle, mais l'usage est différent. La PAC valorise la chaleur, le groupe froid valorise le froid.
