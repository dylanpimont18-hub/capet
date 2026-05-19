# T10 — Machine asynchrone (MAS)

> **Fréquence :** 9/22 sujets · **Intensité moyenne :** 🔴 Central
> ⚠️ **Point aveugle majeur signalé jury 2022 et 2025** : moins de 30 % des candidats maîtrisent le bilan de puissance de la MAS.

---

## Notions clés

### Vitesse de synchronisme

$$n_s = \frac{60 \cdot f}{p} \quad \text{(tr/min)} \qquad \Omega_s = \frac{2\pi f}{p} \quad \text{(rad/s)}$$

### Glissement

$$g = \frac{n_s - n}{n_s} = \frac{\Omega_s - \Omega}{\Omega_s}$$

- $g = 0$ : vitesse synchrone (impossible en moteur, car couple nul)
- $g = 1$ : rotor bloqué (démarrage)
- $g$ nominal $\approx$ 2 à 10 % pour les MAS industrielles

> ❌ **À mémoriser** : $g = (n_s - n)/n_s$

### Bilan de puissance (chaîne)

$$P_{absorbée} \xrightarrow{-P_{Joule\,stator}} P_{transmise} \xrightarrow{-P_{Joule\,rotor}} P_{mécanique\,interne} \xrightarrow{-P_{pertes\,méca}} P_{utile}$$

$$P_{Joule\,rotor} = g \cdot P_{transmise}$$

$$P_{mécanique\,interne} = (1-g) \cdot P_{transmise} = T_{em} \cdot \Omega$$

> ❌ **À mémoriser** : $P_{Joule,rotor} = g \cdot P_{tr}$ et $P_{méca} = (1-g) \cdot P_{tr}$

### Vitesse du rotor

$$\Omega = \Omega_s \cdot (1 - g) \quad \text{ou} \quad n = n_s \cdot (1 - g)$$

### Couple électromagnétique

$$T_{em} = \frac{P_{transmise}}{\Omega_s} = \frac{P_{méca}}{\Omega}$$

### Rendement simplifié (sans pertes stator, fer, méca)

$$\eta \approx 1 - g$$

En pratique, pour un moteur de bonne qualité : $\eta = 85$ à 97 %

### Démarrage direct (DOL)

- Courant de démarrage : $I_{dém} = 5$ à $8 \cdot I_n$
- Couple de démarrage : $T_{dém} = 0{,}5$ à $2 \cdot T_n$
- Chute de tension réseau importante

### Schéma équivalent (monophasé par phase)

```
    R1   jX1          jX2'
 ─[   ]─[   ]─────[   ]─[  R2'/g  ]─
                        
 (stator)        (rotor ramené)
```

La résistance $R'_2/g = R'_2 + R'_2(1-g)/g$ : la partie $(1-g)/g$ représente la puissance mécanique.

---

## Modes de démarrage

| Mode | Avantage | Inconvénient |
|---|---|---|
| Direct (DOL) | Simple | Fort courant |
| Étoile-triangle | $I_d \div 3$, $T_d \div 3$ | Discontinuité de couple |
| Démarreur progressif | Couple contrôlé | Coût, harmoniques |
| Variateur de vitesse | Optimal | Coût |

---

## Variation de vitesse MAS

Pour varier la vitesse de façon économique :
- Varier la fréquence $f$ (variateur → onduleur triphasé)
- Maintenir $V/f$ = constante pour garder le flux constant

$$\frac{U}{f} = \text{constante} \quad \text{(loi } V/f \text{)}$$

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Vitesse de synchronisme | $n_s = 60f/p$ |
| Glissement | $g = (n_s - n)/n_s$ |
| Pertes Joule rotor | $P_{J2} = g \cdot P_{tr}$ |
| Puissance mécanique | $P_{méca} = (1-g) \cdot P_{tr}$ |
| Couple électromagnétique | $T_{em} = P_{tr}/\Omega_s$ |
| Vitesse réelle | $n = n_s(1-g)$ |

---

## Pièges courants

1. **$g$ en % vs décimal** : les données donnent souvent $g$ en %. Convertir en décimal pour les calculs.
2. **$P_{J2} = g P_{tr}$ vs $P_{méca} = (1-g) P_{tr}$** : ne pas inverser.
3. **Couple** : calculer $T_{em} = P_{tr}/\Omega_s$, pas $P_{méca}/\Omega_s$.
4. **Puissance absorbée $\neq$ puissance transmise** : il faut soustraire les pertes fer et Joule stator.
5. **4 paires de pôles vs 4 pôles** : une machine à 4 **pôles** a $p = 2$ paires → $n_s = 60 \times 50/2 = 1500$ tr/min.
