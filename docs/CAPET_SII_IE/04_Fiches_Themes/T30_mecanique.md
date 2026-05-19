# T30 — Mécanique (cinématique, bilan forces, RDM)

> **Fréquence :** 22/22 sujets · **Intensité moyenne :** 🟠 Important
> Présent dans tous les sujets d'E1 (épreuve pluritechnologique). Souvent en première partie (cinématique, bilan puissances) puis en question de RDM (dimensionnement structure). Le jury signale le TEC comme lacune majeure.

---

## Cinématique

### Grandeurs fondamentales

| Grandeur | Symbole | Unité | Formule |
|---|---|---|---|
| Position | x | m | — |
| Vitesse | v | m/s | $v = dx/dt$ |
| Accélération | γ (ou a) | m/s² | $\gamma = dv/dt$ |
| Vitesse angulaire | ω | rad/s | $\omega = d\theta/dt$ |
| Vitesse angulaire | N | tr/min | $N = 60\cdot\omega/(2\pi)$ |

### Conversions

$\omega = 2\pi N/60$ ← à restituer de mémoire, fréquence 5

$v = R\cdot\omega$ (liaison roulement sans glissement : $v_{roue} = R\cdot\omega_{roue}$)

### MRUA — Mouvement rectiligne uniformément accéléré

| Formule | Usage |
|---|---|
| $v(t) = v_0 + \gamma \cdot t$ | Vitesse à l'instant t |
| $x(t) = x_0 + v_0 \cdot t + \frac{1}{2}\gamma t^2$ | Position à l'instant t |
| $v^2 = v_0^2 + 2\gamma(x - x_0)$ | Relation vitesse-distance (sans t) |

**Distance d'arrêt :** $x_{arr} = -v_0^2/(2\Gamma)$ (avec $\Gamma$ = décélération < 0)

---

## Bilan des forces (PFD)

### Translation

$$\sum F = m\cdot\gamma \quad \text{(Principe fondamental de la dynamique)}$$

$$\sum F = 0 \quad \text{en statique (équilibre)}$$

Forces courantes :
- Poids : $P = m\cdot g$ ($g = 9{,}81$ m/s²)
- Normal (appui, réaction)
- Frottement : $F_f = f\cdot N$
- Poussée hydrostatique : $F = \rho\cdot g\cdot H\cdot S$

### Rotation

$$\sum C = J\cdot\alpha \quad \text{(couple résultant = moment d'inertie × accélération angulaire)}$$

- $J$ : moment d'inertie (kg·m²)
- $\alpha = d\omega/dt$ : accélération angulaire (rad/s²)

### Puissances

| Formule | Description |
|---|---|
| $P = F\cdot v$ | Puissance d'une force |
| $P = C\cdot\omega$ | Puissance d'un couple (mécanique) |
| $P_{pente} = -M\cdot g\cdot v\cdot\sin\alpha$ | Puissance de pesanteur sur pente |

---

## Théorème de l'énergie cinétique (TEC)

> **⚠ Signalé par le jury 2024 comme inconnu de la majorité des candidats**

$$\Delta E_c = W_{total}$$

$$E_c = \frac{1}{2}m v^2 \quad \text{(translation)} \qquad E_c = \frac{1}{2}J\omega^2 \quad \text{(rotation)}$$

$W_{total}$ = somme des travaux de toutes les forces (moteur, résistant, pesanteur, frottement...)

**Travail d'une force constante :** $W = F\cdot d\cdot\cos\theta$

**Travail du poids :** $W_p = m\cdot g\cdot\Delta h$ (positif si descente)

**Application type — freinage :**
- $\Delta E_c = 0 - \frac{1}{2}m v_0^2$ (la voiture s'arrête)
- $W_{frein} = -F_{frein} \cdot d$
- Bilan : $-\frac{1}{2}m v_0^2 = -F_{frein} \cdot d$ → $$d = \frac{m v_0^2}{2 F_{frein}}$$

---

## Réducteur / Transmission

| Formule | Description |
|---|---|
| $i = \omega_{moteur} / \omega_{charge}$ | Rapport de réduction |
| $i = C_{charge} / C_{moteur}$ (si $\eta=1$) | Rapport de réduction (côté couple) |
| $P_{sortie} = \eta \cdot P_{entrée}$ | Prise en compte du rendement |
| $C_{sortie} = i \cdot \eta \cdot C_{moteur}$ | Couple côté charge |

> ❌ **Rapport de réduction i = simple division** — signalé non maîtrisé (rapport jury 2025)

---

## Résistance des matériaux (RDM) — Flexion

### Poutre bi-appuyée sous charge répartie q (N/m)

```
    q (N/m)
    ↓↓↓↓↓↓↓↓↓
====●══════════════●====
    A               B
    L/2     |     L/2
            ↓ M_max
```

- Réactions : $Y_A = Y_B = \frac{qL}{2}$
- Moment fléchissant max (centre) : $M_{fz,max} = \frac{qL^2}{8}$
- Flèche maximale (centre) : $f_{max} = \frac{5qL^4}{384 E I}$

### Contrainte normale en flexion

$$\sigma_{max} = \frac{M_{fz,max} \cdot y_{max}}{I_{Gz}}$$

- $y_{max}$ : distance de la fibre neutre au bord le plus éloigné
- $I_{Gz}$ : moment quadratique de la section par rapport à l'axe neutre (donné dans les sujets)

**Condition de résistance :** $\sigma_{max} \leq R_e / s$ (avec $s$ = coefficient de sécurité)

### Moments quadratiques usuels

| Section | $I_{Gz}$ |
|---|---|
| Rectangle $b \times h$ | $b h^3/12$ |
| Cercle plein $\varnothing D$ | $\pi D^4/64$ |
| Tube rectangulaire | $[b h^3-(b-2e)(h-2e)^3]/12$ |

---

## Types de questions au concours

| Type | Exemple | Formule |
|---|---|---|
| Calcul vitesse/accélération | "Calculer γ pour passer de 0 à 5 m/s en 10 m" | $v^2 = 2\gamma x \Rightarrow \gamma = v^2/(2x)$ |
| Bilan des forces | "Exprimer la condition d'équilibre du bras racleur" | $\sum F = 0$ et $\sum M = 0$ |
| TEC — freinage | "Calculer la distance d'arrêt à 30 km/h" | $d = mv_0^2/(2F_{frein})$ |
| Puissance mécanique | "Calculer la puissance nécessaire en régime établi" | $P = C\cdot\omega = F\cdot v$ |
| Dimensionnement RDM | "Vérifier que la contrainte est < $R_e/2$" | $\sigma_{max} = M\cdot y/I \leq R_e/2$ |
| Flèche en service | "Vérifier que f < L/200" | $f = 5qL^4/(384EI)$ |

---

## Pièges courants

1. **Oublier le TEC** et appliquer $v = d/t$ à des phases d'accélération → résultats faux.
2. **Confondre couple et force** (signalé jury 2024) : $C$ en N·m, $F$ en N. $P = F\cdot v = C\cdot\omega$.
3. **Signe du travail** dans le TEC : travail moteur positif, travail résistant négatif.
4. **Moment quadratique $I \neq$ moment d'inertie $J$** : $I$ en m⁴ (RDM), $J$ en kg·m² (dynamique).
5. **Oublier les unités de q** : $q$ en N/m (linéique) → $M_{max} = qL^2/8$ en N·m si $L$ en m.

---

## Liens avec d'autres thèmes

- → **T11 Variation de vitesse** : couple moteur vs couple résistant à la charge mécanique
- → **T02 Puissance AC** : $P_{mécanique} = P_{électrique} \cdot \eta$ → lien entre mécanique et électrique
- → **T21 Modélisation** : modèle dynamique du système mécanique ($J$, $f$, $C_{em}$)
- → **T24 Correcteurs** : asservissement de position ou de force sur un axe mécanique

---

*Source : formulaire_capet.md §12–15 · sujets 2021 (Nickel), 2020 (Exotec), 2019 (Transport câble), 2022 (Banc essai), 2024 (Urbanloop)*
