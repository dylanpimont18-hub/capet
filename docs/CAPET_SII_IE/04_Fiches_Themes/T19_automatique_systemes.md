# T19 — Systèmes automatisés & fonctions de transfert

> **Fréquence :** 8/22 sujets · **Intensité moyenne :** 🔴 Central
> Voir aussi T24 (correcteurs). Ce thème couvre la modélisation des systèmes en boucle ouverte et fermée, indispensable pour analyser un asservissement.

---

## Notions clés

### Schéma fonctionnel

```
         ε(t)           u(t)          y(t)
  r(t) ─►(+)─► Correcteur ─► Système ─►──── Sortie
         ↑-                              │
         └─────────── Capteur ───────────┘
```

- $r(t)$ : consigne (setpoint)
- $\varepsilon(t) = r(t) - y(t)$ : erreur
- $C(p)$ : fonction de transfert du correcteur
- $H(p)$ : fonction de transfert du système (procédé + capteur)

### Fonction de transfert en boucle ouverte (FTBO)

$$FTBO(p) = C(p) \cdot H(p) \cdot K_{capteur}$$

### Fonction de transfert en boucle fermée (FTBF)

$$FTBF(p) = \frac{FTBO(p)}{1 + FTBO(p)} = \frac{C \cdot H}{1 + C \cdot H}$$

> ❌ **À mémoriser** : $FTBF = \frac{FTBO}{1 + FTBO}$

### Modèles standard

**Système du 1er ordre :**
$$H(p) = \frac{K}{1 + \tau p}$$

- $K$ : gain statique
- $\tau$ : constante de temps (s)
- Réponse à un échelon : $y(t) = K \cdot U_0 (1 - e^{-t/\tau})$
- À $t = \tau$ : 63 % de la valeur finale
- Temps de réponse à 5 % : $t_{5\%} \approx 3\tau$

**Système du 2e ordre :**
$$H(p) = \frac{K \omega_0^2}{p^2 + 2m\omega_0 p + \omega_0^2}$$

- $\omega_0$ : pulsation propre (rad/s)
- $m$ : coefficient d'amortissement
- $m < 1$ : oscillant → dépassement $D\% = e^{-m\pi/\sqrt{1-m^2}} \times 100\%$
- $m = 1$ : critique (le plus rapide sans dépassement)
- $m > 1$ : amorti

**Intégrateur pur :**
$$H(p) = \frac{K}{p}$$

### Critères de performances

| Critère | Définition |
|---|---|
| Erreur statique $\varepsilon_\infty$ | $\lim_{t\to\infty} \varepsilon(t)$ — règle de l'échelon final |
| Dépassement $D\%$ | $(y_{max} - y_\infty)/y_\infty \times 100\%$ |
| Temps de réponse à 5 % $t_{r5\%}$ | Temps pour rester dans ±5 % de $y_\infty$ |
| Marge de phase $M\varphi$ | Marge avant instabilité (cible > 45°) |
| Marge de gain $MG$ | Marge en gain avant instabilité (cible > 6 dB) |

### Théorème de la valeur finale

$$\lim_{t\to\infty} y(t) = \lim_{p\to 0} p \cdot Y(p)$$

**Erreur statique en boucle fermée pour une consigne échelon :**
$$\varepsilon_\infty = \frac{1}{1 + K_{BO}} \cdot R_0$$

→ Si la FTBO contient un intégrateur (classe 1) : $\varepsilon_\infty = 0$

---

## Types de questions au concours

| Type | Formule/Méthode |
|---|---|
| FTBF à partir de FTBO | $FTBF = FTBO/(1+FTBO)$ |
| Erreur statique (échelon) | $\varepsilon_\infty = R_0/(1+K_{BO})$ |
| Constante de temps système 1er ordre | $\tau$ = lecture du tracé à 63% |
| Dépassement 2e ordre | $D\% = e^{-m\pi/\sqrt{1-m^2}} \times 100\%$ |
| Condition de stabilité | $M\varphi > 0$, tous pôles à partie réelle < 0 |

---

## Pièges courants

1. **Unité de $p$** : $p = j\omega$ en sinusoïdal permanent, $p = s$ (variable de Laplace) en temporel. Ne pas confondre.
2. **Boucle ouverte vs fermée** : la stabilité s'analyse en FTBO (diagramme de Bode), mais les performances se lisent en FTBF.
3. **Système instable** : $\varepsilon_\infty \to \infty$, le calcul n'a plus de sens. Vérifier les pôles avant.
4. **Classe du système** : le nombre d'intégrateurs détermine l'erreur statique. Classe 0 → erreur statique non nulle ; classe 1 → erreur nulle à l'échelon.
