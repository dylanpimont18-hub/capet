# T03 — Phénomènes thermiques

> **Fréquence :** 22/22 sujets · **Intensité moyenne :** 🟠 Important
> Thème fil conducteur dans les sujets bâtiment (2015 Shelter, 2016 Maison active, 2022 Réseau chaleur) et climatisation. Présent en questions isolées partout ailleurs.

---

## Notions clés

### Analogie thermique / électrique

| Thermique | Électrique |
|---|---|
| Flux thermique $\varphi$ (W) | Courant I (A) |
| Température T (°C ou K) | Tension U (V) |
| Résistance thermique $R_{th}$ (K/W) | Résistance R (Ω) |
| $\Delta T$ | $\Delta U$ |

### Loi de Fourier — Conduction

$$\varphi = -\frac{\Delta T}{R_{th}}$$

(flux = différence de température / résistance thermique)

$$R_{th} = \frac{e}{\lambda \cdot S}$$

- $e$ : épaisseur de la couche (m)
- $\lambda$ : conductivité thermique (W/m·K)
- $S$ : surface (m²)

### Résistances en série (parois en couches)

$$\frac{1}{K} = \sum \frac{e_i}{\lambda_i} + R_{s,int} + R_{s,ext}$$

où $K$ est le coefficient de transmission surfacique global (W/m²·K)

$$\varphi_{paroi} = K \cdot S \cdot \Delta T$$

### Résistances en parallèle (ponts thermiques)

$$\varphi_{tot} = \left(\frac{\lambda_{eq} \cdot S_v}{e_{eq}} + \frac{\lambda_p \cdot S_p}{e_p}\right) \cdot \Delta T$$

---

## Pompe à chaleur (PAC) — Cycle thermodynamique

### Bilan énergétique

```
         Q₁ (chaleur fournie au logement)
         ↑
    ┌────────────┐
W ──►  Compresseur │
    └────────────┘
         ↓
         Q₂ (chaleur prélevée à l'extérieur)
```

Bilan : $W + Q_1 + Q_2 = 0$ (avec $Q_1 < 0$ car fourni, $Q_2 > 0$ car prélevé)

Entropie (cycle réversible) : $\frac{Q_1}{T_c} + \frac{Q_2}{T_f} = 0$

### COP

| Formule | À retenir |
|---|---|
| $COP = \|Q_1\| / W$ | COP de la PAC (chaleur fournie / travail consommé) |
| $COP_{max} = \frac{T_c}{T_c - T_f}$ | COP de Carnot — **à restituer de mémoire** |
| $\varphi = n \cdot \|Q_1\| = n \cdot W \cdot COP$ | Flux thermique total (n PAC en parallèle) |

> **$T_c$ et $T_f$ en Kelvin** ($T(K) = T(°C) + 273$)

---

## Rayonnement thermique

**Loi de Stefan-Boltzmann :**

$$P_s = \left(\frac{T_S}{100}\right)^4 \cdot \sigma \quad \text{où } \sigma = 5{,}67 \text{ W/m}^2\text{·K}^4$$

Utilisée dans les sujets de bâtiment à énergie positive, bilan radiatif.

---

## Condensation de vapeur — Loi de Fick

$$P_S = \exp\!\left(25{,}5 - \frac{5204{,}9}{T + 273}\right)$$ ← pression de vapeur saturante (donnée sujet)

$$P_V = HR \times P_S$$ ← pression partielle de vapeur

$$g = -\frac{\Delta P}{R_{vap}}$$ ← flux de vapeur (loi de Fick)

Utilisé dans les sujets de bâtiment : risque de condensation dans les parois, isolation.

---

## Types de questions au concours

| Type | Exemple | Formule |
|---|---|---|
| Résistance thermique d'une paroi | "Calculer $R_{th}$ de la toiture" | $R_{th} = \frac{e}{\lambda \cdot S}$ |
| Flux thermique perdu | "Calculer les déperditions de la maison" | $\varphi = K \cdot S \cdot \Delta T$ |
| COP d'une PAC | "Calculer le COP théorique" | $COP_{max} = \frac{T_c}{T_c - T_f}$ |
| Puissance électrique PAC | "Quelle puissance absorbe le compresseur ?" | $P_e = \varphi / (COP \cdot r_g)$ |
| Bilan économique chauffage | "Comparer PAC vs résistance" | $Eco = \varphi \cdot t / COP$ vs $\varphi \cdot t / 1$ |
| Risque de condensation | "Y a-t-il risque de condensation ?" | $P_V > P_S$ → condensation |

---

## Pièges courants

1. **Températures en °C au lieu de K** dans le COP de Carnot → résultat faux. Toujours convertir.
2. **Confusion $Q_1$ et $Q_2$** dans le bilan PAC : $Q_1$ est la chaleur fournie au bâtiment (côté chaud), $Q_2$ est prélevée à l'extérieur (côté froid).
3. **Résistances en série vs parallèle** : couches superposées = série (additionner $R_{th}$) ; voies parallèles (fenêtre + mur) = parallèle (additionner les flux).
4. **Oublier la surface** dans $R_{th}$ : $R_{th} = e/(\lambda \cdot S)$. Quand $S = 1$ m², $R_{th} = e/\lambda$ en K/W.

---

## Calibrage de la réponse attendue

**Question type :** "Une PAC chauffe un bâtiment à $T_c = 20°C$ depuis un extérieur à $T_f = 5°C$. Calculer le COP théorique."

**Réponse attendue :**
- $T_c = 20 + 273 = 293$ K, $T_f = 5 + 273 = 278$ K
- $COP_{max} = T_c / (T_c - T_f) = 293 / (293 - 278) = 293 / 15 =$ **19,5**
- Commentaire : "En pratique le COP réel est bien inférieur (3 à 5) en raison des irréversibilités."

---

## Liens avec d'autres thèmes

- → **T02 Puissance AC** : puissance électrique du compresseur PAC
- → **T13 ENR** : bâtiment à énergie positive (PV + PAC + bilan thermique global)
- → **T14 Distribution** : alimentation électrique de la PAC, protection
- → **T24 Correcteurs** : régulation de température par thermostat PID

---

*Source : formulaire_capet.md §1–3 · sujets 2015 (Shelter), 2016 (Maison active), 2017 (Spa Sydney), 2022 (Réseau chaleur)*
