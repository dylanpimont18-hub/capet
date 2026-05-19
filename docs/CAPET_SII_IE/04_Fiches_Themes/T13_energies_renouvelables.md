# T13 — Énergies renouvelables

> **Fréquence :** 8/22 sujets · **Intensité moyenne :** 🔴 Central
> Photovoltaïque, éolien et hydraulique sont les trois piliers. Le dimensionnement d'un système PV est quasi-systématique depuis 2020.

---

## Notions clés

### Photovoltaïque (PV)

**Puissance d'un panneau :**
$$P_{panneau} = \eta_{panneau} \cdot S_{panneau} \cdot E_{irradiance}$$

- $\eta$ : rendement du panneau (% — typiquement 15 à 22 %)
- $S$ : surface (m²)
- $E$ : éclairement / irradiance (W/m²) — typiquement 1000 W/m² (STC)

**Puissance d'un champ PV :**
$$P_{champ} = N_{panneaux} \cdot P_{STC} \cdot \frac{E_{réelle}}{1000}$$

**Point de Puissance Maximum (MPP) :**
- À l'intersection de la courbe I-V et de la courbe de puissance maximale
- Le MPPT (Maximum Power Point Tracker) ajuste le point de fonctionnement
- $V_{MPP} \approx 0{,}80 \cdot V_{oc}$, $I_{MPP} \approx 0{,}90 \cdot I_{sc}$

**Courbe I-V :**
```
  I
  Isc ─────────────────.
  |                   / ↑ MPP
  |                  /
  |                 /
  └──────────────────── V
                      Voc
```

**Facteur de forme (fill factor) :**
$$FF = \frac{P_{MPP}}{V_{oc} \cdot I_{sc}}$$

> ❌ **À mémoriser** : $P_{PV} = \eta \cdot S \cdot E_{irr}$

### Éolien

**Puissance théorique extraite du vent (loi de Betz) :**
$$P = \frac{1}{2} \rho \cdot S \cdot v^3 \cdot C_p$$

- $\rho$ : densité de l'air ≈ 1,225 kg/m³
- $S = \pi R^2$ : surface balayée par le rotor (m²)
- $v$ : vitesse du vent (m/s)
- $C_p$ : coefficient de puissance (max 0,593 → **limite de Betz**)

> ❌ **À mémoriser** : $P_{éolien} = \frac{1}{2}\rho S v^3 C_p$

**Plage de fonctionnement :**
- $v < v_{cut-in}$ (≈ 3 m/s) : arrêt
- $v_{cut-in} < v < v_{nominale}$ (≈ 12 m/s) : puissance croît en $v^3$
- $v_{nominale} < v < v_{cut-out}$ (≈ 25 m/s) : puissance constante (limitée)
- $v > v_{cut-out}$ : arrêt sécurité

**Énergie annuelle produite :**
$$E_{an} = P_{nominale} \cdot h_{pleine\_puissance}$$

Exemple : 3 MW × 2000 h = 6 GWh/an

### Hydraulique

**Puissance d'une turbine :**
$$P = \rho \cdot g \cdot Q \cdot H_{net} \cdot \eta_{turbine}$$

- $\rho$ = 1000 kg/m³ (eau)
- $g$ = 9,81 m/s²
- $Q$ : débit (m³/s)
- $H_{net}$ : hauteur de chute nette (m)
- $\eta$ : rendement (80 à 90 %)

> ❌ **À mémoriser** : $P = \rho g Q H \eta$

### Bilan d'un site isolé (PV + batterie)

$$E_{produite} \cdot \eta_{MPPT} \cdot \eta_{bat} = E_{consommée}$$

**Dimensionnement PV :**
$$N_{panneaux} = \frac{E_{journalière,conso}}{E_{panneau,jour} \cdot \eta_{système}}$$

**Dimensionnement batterie :**
$$C_{Ah} = \frac{E_{autonomie\_Wh}}{U_{batterie} \cdot DOD}$$

- $DOD$ : profondeur de décharge (Depth of Discharge) — typiquement 0,5 à 0,8

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Puissance PV à 800 W/m² | $P = N \cdot P_{STC} \times 0{,}80$ |
| Puissance éolienne | $P = \frac{1}{2}\rho \pi R^2 v^3 C_p$ |
| Puissance hydraulique | $P = \rho g Q H \eta$ |
| Nombre de panneaux | $N = E_{conso}/(E_{panneau} \cdot \eta)$ |
| Capacité batterie | $C = E_{Wh}/(U \cdot DOD)$ |

---

## Pièges courants

1. **$v^3$ dans éolien** : la puissance varie avec le cube de la vitesse, pas au carré. Doubler le vent → ×8 la puissance.
2. **Limite de Betz** : $C_p \le 0{,}593$. Pas de rendement supérieur à 59,3 % pour les éoliennes.
3. **STC** : les données constructeurs panneaux sont à 1000 W/m², 25°C. Corriger pour les conditions réelles.
4. **Pertes système PV** : penser aux pertes câbles, onduleur, mismatch. Rendement système ≈ 75–85 %.
