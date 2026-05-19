# T12 — Stockage de l'énergie

> **Fréquence :** 6/22 sujets · **Intensité moyenne :** 🟠 Important
> Présent dans les sujets véhicules électriques, énergies renouvelables, systèmes embarqués. Questions fréquentes sur le dimensionnement batterie et les comparaisons de technologies.

---

## Notions clés

### Batteries électrochimiques

**Capacité :**
$$C_{Ah} \quad \text{(Ampère-heures)} \qquad C_{Wh} = C_{Ah} \cdot U_{nominale}$$

**Énergie disponible :**
$$E = C_{Ah} \cdot U \cdot \Delta t \quad \text{ou} \quad E = C_{Wh} = Q \cdot U$$

**Puissance maximale :**
$$P_{max} = U \cdot I_{max} = \frac{U^2}{R_{int}}$$

**État de charge (SOC) :**
$$SOC = \frac{Q_{restante}}{Q_{nominale}} \times 100\%$$

> ❌ **À mémoriser** : $E_{Wh} = C_{Ah} \times U$

### Supercondensateurs

$$E = \frac{1}{2} C U^2$$

- Densité de puissance très élevée, densité d'énergie faible
- Idéaux pour des pointes de puissance brèves

### STEP (Station de Transfert d'Énergie par Pompage)

$$E = m \cdot g \cdot h \cdot \eta = \rho \cdot V \cdot g \cdot h \cdot \eta$$

$$P = \rho \cdot g \cdot Q \cdot H \cdot \eta$$

- $m$ : masse d'eau (kg)
- $h$ ou $H$ : hauteur de chute (m)
- $Q$ : débit volumique (m³/s)
- $\rho$ = 1000 kg/m³

> ❌ **À mémoriser** : $P_{hydraulique} = \rho g Q H \eta$

### Volant d'inertie

$$E = \frac{1}{2} J \Omega^2$$

- $J$ : moment d'inertie (kg·m²)
- $\Omega$ : vitesse angulaire (rad/s)

### Comparaison des technologies

| Technologie | Densité d'énergie | Densité de puissance | Durée de vie cycles | Usage typique |
|---|---|---|---|---|
| Lithium-ion | 100–250 Wh/kg | 500–2000 W/kg | 500–2000 cycles | VE, électronique |
| Plomb-acide | 30–50 Wh/kg | 180 W/kg | 200–300 cycles | Démarrage, UPS |
| NiMH | 60–120 Wh/kg | 250 W/kg | 500–1500 cycles | Hybrides |
| Supercondensateur | 5–15 Wh/kg | 10 000+ W/kg | 100 000+ cycles | Pics de puissance |
| STEP | ~1 Wh/m³/m | variable | illimitée | Réseau électrique |

### Rendement de stockage aller-retour

$$\eta_{cycle} = \eta_{charge} \cdot \eta_{décharge}$$

Batterie Li-ion : $\eta_{cycle} \approx 85$ à 95 %

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Énergie d'une batterie | $E_{Wh} = C_{Ah} \times U_{nom}$ |
| Autonomie à puissance $P$ | $t = E_{Wh}/P$ |
| Énergie supercondensateur | $E = \frac{1}{2}CU^2$ |
| Puissance STEP | $P = \rho g Q H \eta$ |
| SOC après prélèvement | $SOC_{final} = SOC_{init} - \Delta Q/Q_n$ |

---

## Pièges courants

1. **Ah vs Wh** : la capacité est en Ah (charge), l'énergie en Wh. Multiplier par la tension nominale pour convertir.
2. **SOC de 0 à 1 ou 0 à 100 %** : vérifier l'unité dans le contexte.
3. **Tension de batterie variable** : en réalité $U_{batterie}$ diminue avec la décharge. Pour simplifier, utiliser la tension nominale sauf si le sujet donne la courbe.
4. **STEP** : l'énergie stockée = $\rho V g h$, mais la puissance maximale = $\rho g Q H$ avec le débit $Q$ (m³/s), pas le volume.
