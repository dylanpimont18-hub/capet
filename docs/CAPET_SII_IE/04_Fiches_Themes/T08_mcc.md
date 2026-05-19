# T08 — Machine à courant continu (MCC)

> **Fréquence :** 7/22 sujets · **Intensité moyenne :** 🔴 Central
> ⚠️ **Point aveugle majeur signalé jury 2022 et 2025** : moins d'un candidat sur deux maîtrise les formules de la MCC.

---

## Notions clés

### Équation fondamentale de la MCC

$$U = E + R_a \cdot I_a \quad \text{(moteur)}$$
$$U = E - R_a \cdot I_a \quad \text{(génératrice)}$$

- $U$ : tension d'alimentation
- $E$ : force électromotrice (fém)
- $R_a$ : résistance d'induit
- $I_a$ : courant d'induit

### Force électromotrice (fém)

$$E = K \cdot \Phi \cdot \Omega = K' \cdot n$$

- $K$ : constante de la machine (dépend de la construction)
- $\Phi$ : flux inducteur
- $\Omega$ : vitesse angulaire (rad/s)
- $n$ : vitesse en tr/min → $\Omega = 2\pi n/60$

> ❌ **À mémoriser** : $E = K \cdot \Phi \cdot \Omega$

### Couple électromagnétique

$$T_e = K \cdot \Phi \cdot I_a$$

> ❌ **À mémoriser** : $T_e = K \cdot \Phi \cdot I_a$

### Bilan de puissance

```
         P_elect = U·Ia
              ↓
    P_Joule = Ra·Ia²
              ↓
         P_élmag = E·Ia = Te·Ω
              ↓
    P_méca_pertes (frottements)
              ↓
         P_mécanique utile = Tu·Ω
```

$$P_{élmag} = E \cdot I_a = T_e \cdot \Omega$$

### Vitesse en fonction des paramètres

$$\Omega = \frac{U - R_a \cdot I_a}{K \cdot \Phi}$$

→ Pour contrôler la vitesse :
- Varier $U$ (hacheur)
- Varier $\Phi$ (affaiblissement de flux → $\Omega$ augmente)

### Régimes de fonctionnement (4 quadrants)

| Quadrant | $\Omega$ | $T_e$ | Mode |
|---|---|---|---|
| 1 | + | + | Moteur avant |
| 2 | + | − | Générateur avant (freinage récupératif) |
| 3 | − | − | Moteur arrière |
| 4 | − | + | Générateur arrière |

### Caractéristique mécanique

$$\Omega = \frac{U}{K\Phi} - \frac{R_a}{(K\Phi)^2} \cdot T_e$$

C'est une droite : vitesse diminue linéairement avec le couple.

```
  Ω
  │
Ω0├─── (U fixé)
  │ \
  │   \
  │     \
  └──────── Te
        Tc_cc
```

$\Omega_0 = U/(K\Phi)$ : vitesse à vide (à ne pas confondre avec vitesse nominale)

---

## Excitation

| Type | Caractéristique |
|---|---|
| Shunt (dérivation) | $\Phi$ = const, vitesse stable |
| Série | $\Phi \propto I_a$, fort couple démarrage |
| Composée | Mixte |
| Séparé (aimants permanents) | $\Phi$ = const, commande simple |

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Vitesse à partir de la tension | $\Omega = (U - R_a I_a)/(K\Phi)$ |
| Couple à partir du courant | $T_e = K\Phi \cdot I_a$ |
| Puissance mécanique | $P = T_e \cdot \Omega$ |
| Rendement | $\eta = P_{méca}/(U \cdot I_a)$ |
| Courant au démarrage ($\Omega = 0$) | $I_{dém} = U/R_a$ (fém nulle) |

---

## Pièges courants

1. **$E$ et $U$** : $E < U$ en moteur, $E > U$ en générateur. Ne pas inverser.
2. **Démarrage** : à $t=0$, $E=0$ donc $I_{dém} = U/R_a$ → très élevé ! On insère une résistance de démarrage.
3. **Unité de vitesse** : $\Omega$ en rad/s dans les formules, $n$ en tr/min dans les données. Convertir : $\Omega = 2\pi n/60$.
4. **Affaiblissement de flux** : augmenter $\Omega$ en réduisant $\Phi$, mais risque de décrochage si $I_a$ monte.
