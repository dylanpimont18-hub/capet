# T09 — Machine synchrone

> **Fréquence :** 8/22 sujets · **Intensité moyenne :** 🔴 Central
> Présent dans les sujets éolien, traction ferroviaire, alternateurs. Diagramme de Fresnel et puissance maximale sont très souvent demandés.

---

## Notions clés

### Relation vitesse-fréquence

$$n_s = \frac{60 \cdot f}{p} \quad \text{(tr/min)} \qquad \Omega_s = \frac{2\pi f}{p} \quad \text{(rad/s)}$$

- $f$ : fréquence réseau (Hz)
- $p$ : nombre de paires de pôles

> ❌ **À mémoriser** : $n_s = 60f/p$

### FEM à vide (alternateur)

$$E_0 = K \cdot \Phi \cdot \Omega_s = K \cdot \Phi \cdot n_s$$

- Proportionnelle au flux et à la vitesse
- Mesurée à vide (sans charge)

### Équation de la machine synchrone (modèle simplifié)

**Alternateur (générateur) :**
$$\vec{U} = \vec{E_0} - jX_s \cdot \vec{I}$$

**Moteur :**
$$\vec{E_0} = \vec{U} - jX_s \cdot \vec{I}$$

Ou en termes de modules (approximation résistance nulle) :
$$U^2 = E_0^2 + (X_s I)^2 + 2 E_0 X_s I \sin\psi$$

- $X_s$ : réactance synchrone
- $\psi$ : déphasage interne

### Diagramme de Fresnel

```
         E0·sinδ
    E0 /|
      / |
     /  | X_s·I·cosφ
    / δ |
   U────┘
         X_s·I·sinφ
```

- $\delta$ : angle de décalage entre $E_0$ et $U$ (angle de charge)

### Puissance active (par phase)

$$P = \frac{E_0 \cdot U}{X_s} \cdot \sin\delta$$

Puissance maximale : $P_{max} = \frac{E_0 \cdot U}{X_s}$ pour $\delta = 90^\circ$

> ❌ **À mémoriser** : $P = \frac{E_0 U}{X_s} \sin\delta$ (par phase)

### Puissance totale (triphasé)

$$P_{tot} = 3 \cdot P_{phase} = 3 \cdot \frac{E_0 \cdot U_{ph}}{X_s} \cdot \sin\delta = \sqrt{3} \cdot E_0 \cdot U_{comp} \cdot \sin\delta / X_s$$

### Puissance réactive

$$Q = \frac{U}{X_s}(E_0 \cos\delta - U) = U \cdot I \cdot \sin\varphi$$

- $Q > 0$ (surexcitée) : fournit de la puissance réactive → condensateur
- $Q < 0$ (sous-excitée) : absorbe de la puissance réactive → inductance

### Couple électromagnétique

$$T_e = \frac{P}{\Omega_s} = \frac{p \cdot E_0 \cdot U}{X_s \cdot \omega_s} \cdot \sin\delta$$

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Vitesse de synchronisme | $n_s = 60f/p$ |
| Puissance active fournie | $P = 3 E_0 U \sin\delta / X_s$ |
| Vérifier si $\delta < 90^\circ$ | Condition de stabilité |
| Courant de court-circuit | $I_{cc} = E_0/X_s$ |
| Facteur de puissance | $\cos\varphi = P/(S) = P/(UI)$ |

---

## Pièges courants

1. **Tension phase vs composée** : $U_{phase} = U_{composée}/\sqrt{3}$ en étoile. Les formules de puissance par phase utilisent $U_{phase}$.
2. **$\delta$ vs $\varphi$** : $\delta$ est l'angle interne (entre $E_0$ et $U$), $\varphi$ est l'angle de déphasage entre $U$ et $I$.
3. **p vs 2p** : $p$ = nombre de **paires** de pôles. $p = 1$ pour 2 pôles, $p = 2$ pour 4 pôles…
4. **Résistance du stator** : en pratique $R_s \ll X_s$, mais certains sujets l'incluent : $\vec{U} = \vec{E_0} - (R_s + jX_s)\vec{I}$.
