# T22 — Simulation numérique

> **Fréquence :** 4/22 sujets · **Intensité moyenne :** 🟡 Mentionné
> Sujets demandant d'interpréter des résultats de simulation (Simulink, Python, PSIM), de valider un modèle ou d'identifier des paramètres.

---

## Notions clés

### Rôle de la simulation

- **Validation d'un modèle** : comparer résultats simulés vs mesures expérimentales
- **Analyse de sensibilité** : étudier l'effet de la variation d'un paramètre
- **Pré-dimensionnement** : tester des solutions avant fabrication
- **Formation** : comprendre le comportement d'un système complexe

### Modèle d'état (représentation d'état)

$$\dot{X} = A \cdot X + B \cdot U$$
$$Y = C \cdot X + D \cdot U$$

- $X$ : vecteur d'état (variables internes : courants, vitesses...)
- $U$ : entrées (tensions, consignes...)
- $Y$ : sorties (mesurables)

**Exemple MCC :**
$$\begin{cases} L \dot{I} = U - RI - K\Omega \\ J \dot{\Omega} = KI - f\Omega - T_{charge} \end{cases}$$

Soit : $X = [I, \Omega]^T$, $U = [U_{alim}, T_{charge}]^T$

### Discrétisation (simulation numérique)

**Méthode d'Euler explicite :**
$$X(k+1) = X(k) + h \cdot \dot{X}(k)$$

- $h$ : pas de temps (s)
- Instable si $h$ trop grand

**Critère de stabilité approché :**
$$h < \frac{2}{\omega_{max}}$$

Où $\omega_{max}$ est la pulsation la plus rapide du système.

### Logiciels courants dans les sujets

| Logiciel | Usage |
|---|---|
| MATLAB/Simulink | Systèmes d'asservissement, MCC, MAS |
| Python (scipy) | Simulation, traitement signal |
| PSIM / LTspice | Électronique de puissance |
| PLECS | Convertisseurs thermiques |

### Interprétation des résultats

**Régime transitoire → régime permanent** :
- Le transitoire dépend des pôles du système
- Temps de stabilisation $\approx 4\tau$ à $5\tau$

**Ondulation de courant / tension** :
- Amplitude reliée à $L$, $C$, fréquence de commutation
- Vérifier que l'ondulation est dans le cahier des charges

**Dépassement et oscillations** :
- Dépassement trop grand → coefficient d'amortissement $m$ trop faible
- Ajuster le correcteur (voir T24)

---

## Types de questions au concours

| Type | Approche |
|---|---|
| Lire une courbe simulée | Identifier $\tau$, dépassement, erreur statique |
| Valider un modèle | Comparer simulé vs mesure : écart < 5 % ? |
| Identifier $\tau$ sur courbe | $\tau$ = temps pour atteindre 63 % de la valeur finale |
| Détecter une instabilité simulée | Oscillations qui s'amplifient |
| Identifier le gain statique | $K = y_\infty / u_0$ (réponse à l'échelon $u_0$) |

---

## Pièges courants

1. **Simulé ≠ réel** : la simulation ne vaut que si le modèle est validé. Une petite erreur de paramètre peut donner un résultat très différent.
2. **Unités des axes** : toujours lire les unités des axes $x$ (temps) et $y$ (grandeur) avant d'interpréter.
3. **Régime permanent non atteint** : si la simulation est trop courte, la lecture de la valeur finale est fausse.
4. **Pas de temps $h$** : si $h$ est trop grand, la simulation diverge (instabilité numérique). Ne pas confondre avec une instabilité physique.
