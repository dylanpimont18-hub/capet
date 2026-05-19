# T24 — Correcteurs / Asservissement

> **Fréquence :** 5/22 sujets (présence directe) · **Intensité moyenne :** 🟠 Important quand présent
> Souvent en partie 3 ou 4 des sujets. Présent massivement dans les sujets à forte composante automatique (2017 Métro, 2020 Exotec, 2021 STEP, 2022 Banc essai, 2025 Site isolé).

---

## Rappel — Architecture d'un asservissement

```
Consigne ──►(+)──► Correcteur C(p) ──► Procédé H(p) ──┬──► Sortie
             ↑(-)                                      │
             └──────────── Capteur R(p) ───────────────┘
```

$$FTBO(p) = C(p) \cdot H(p) \cdot R(p)$$

$$FTBF(p) = \frac{FTBO(p)}{1 + FTBO(p)}$$ (si $R(p) = 1$)

---

## Correcteurs usuels

### Correcteur Proportionnel (P)

$$C(p) = K_p$$

| Effet | Détail |
|---|---|
| Rapidité | Augmente avec $K_p$ |
| Précision | Erreur statique non nulle pour un procédé d'ordre 0 |
| Stabilité | Peut déstabiliser si $K_p$ trop grand |

Erreur statique : $\varepsilon_s = \frac{1}{1 + K_p \cdot H(0)} \neq 0$

### Correcteur Intégral (I)

$$C(p) = \frac{K_i}{p}$$

| Effet | Détail |
|---|---|
| Précision | Erreur statique = 0 (intégrateur annule l'erreur en régime permanent) |
| Stabilité | Dégrade la marge de phase (ajoute $-90°$ à toutes les fréquences) |
| Rapidité | Plus lent que P seul |

### Correcteur Proportionnel-Intégral (PI)

$$C(p) = K_p \cdot \left(1 + \frac{1}{T_i \cdot p}\right) = K_p \cdot \frac{1 + T_i \cdot p}{T_i \cdot p}$$

| Effet | Détail |
|---|---|
| Précision | Erreur statique = 0 |
| Rapidité | Meilleure que I seul (action P) |
| Stabilité | Acceptable si $T_i$ bien choisi |

**Règle de réglage :** placer le zéro du PI ($1/T_i$) à 10× plus bas que la fréquence de coupure de la FTBO sans correcteur → $T_i = 10/\omega_c$

### Correcteur Proportionnel-Intégral-Dérivé (PID)

$$C(p) = K_p \cdot \left(1 + \frac{1}{T_i \cdot p} + T_d \cdot p\right)$$

| Terme | Rôle |
|---|---|
| P | Rapidité, réduction de l'erreur |
| I | Précision (annule erreur statique) |
| D | Anticipation, réduit le dépassement, améliore la stabilité |

---

## Synthèse d'un correcteur PI (méthode analytique)

Objectifs : $\omega_0$ imposé, amortissement $\xi = 0{,}707$ (ou $m = 1/\sqrt{2}$)

Pour un procédé d'ordre 1 : $H(p) = K_{mec} / (1 + \tau_{mec} \cdot p)$

**Pulsation naturelle boucle fermée :**
$$\omega_0 = \sqrt{\frac{\tau_{mec}}{K_p \cdot K_i \cdot K_{mec}}}$$

**Gain proportionnel :**
$$K_p = \frac{2 \cdot m \cdot \tau_{mec} \cdot \omega_0 - 1}{K_{mec}}$$

**Gain intégral :**
$$K_i = \frac{\tau_{mec} \cdot \omega_0^2}{K_p \cdot K_{mec}}$$

---

## Critères de stabilité

### Marge de phase $\Phi_m$

Sur le diagramme de Bode de la FTBO :
1. Trouver $\omega_c$ : fréquence de coupure à 0 dB
2. $\Phi_m = 180° + \arg(FTBO(j\omega_c))$
3. Stable si $\Phi_m > 0°$ ; recommandé $\Phi_m \geq 45°$

### Marge de gain $G_m$

1. Trouver $\omega_\pi$ : fréquence pour laquelle $\arg(FTBO) = -180°$
2. $G_m = -20 \cdot \log|FTBO(j\omega_\pi)|$ en dB
3. Stable si $G_m > 0$ dB ; recommandé $G_m \geq 6$ dB

---

## Erreur statique

| Type d'entrée | Correcteur sans intégrateur | Correcteur avec intégrateur (I ou PI) |
|---|---|---|
| Échelon | $\varepsilon_s = \frac{1}{1 + K_{BO}} \neq 0$ | $\varepsilon_s = 0$ |
| Rampe | $\varepsilon_s \to \infty$ | $\varepsilon_s = cte \neq 0$ |
| Parabole | $\varepsilon_s \to \infty$ | $\varepsilon_s \to \infty$ |

$K_{BO} = \lim_{p \to 0} FTBO(p)$ = gain en DC de la FTBO

---

## Types de questions au concours

| Type | Exemple | Méthode |
|---|---|---|
| Identifier le correcteur adapté | "Quel correcteur pour annuler l'erreur statique ?" | Correcteur avec intégrateur (I ou PI) |
| Calculer $K_p$ et $K_i$ | "Dimensionner un correcteur PI pour $\omega_0 = 10$ rad/s" | Formules de synthèse ci-dessus |
| Vérifier la stabilité | "La marge de phase est-elle suffisante ?" | Bode → $\Phi_m \geq 45°$ |
| Calculer l'erreur statique | "Quelle est l'erreur en régime permanent ?" | $\varepsilon_s = \frac{1}{1 + K_{BO}}$ |
| Choisir entre P, PI, PID | "Justifier le choix du correcteur" | Argumenter rapidité/précision/stabilité |

---

## Pièges courants

1. **Confondre $\varepsilon_s = 0$ avec "le système est précis"** : un correcteur I donne bien $\varepsilon_s = 0$ pour un échelon, mais peut être lent ou instable.
2. **Oublier que D amplifie le bruit** : le correcteur PID est rarement recommandé sur des systèmes bruyants sans filtrage.
3. **Utiliser les formules de synthèse avec les mauvaises unités** : $K_{mec}$ en (rad/s)/V, $\tau_{mec}$ en secondes.
4. **Confondre FTBO et FTBF** dans le calcul de la marge de phase : la marge se mesure sur la FTBO.

---

## Liens avec d'autres thèmes

- → **T21 Modélisation** : la FT du procédé $H(p)$ est obtenue par identification du système
- → **T11 Variation de vitesse** : le correcteur PI est utilisé dans la boucle de vitesse du variateur
- → **T17 Bode/filtres** : la marge de phase se lit sur le diagramme de Bode

---

*Source : formulaire_capet.md §10 · sujets 2017 (Métro MF2000), 2020 (Exotec), 2021 (STEP), 2022 (Banc essai)*
