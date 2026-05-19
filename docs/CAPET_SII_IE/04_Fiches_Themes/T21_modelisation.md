# T21 — Modélisation des systèmes

> **Fréquence :** 22/22 sujets · **Intensité moyenne :** 🟠 Important
> Transversal à toutes les épreuves. Concerne la modélisation par fonctions de transfert, schémas-blocs, et l'utilisation des diagrammes SysML dans les sujets récents.

---

## Notions clés

### Fonction de transfert (FT)

$$H(p) = \frac{S(p)}{E(p)}$$ (transformée de Laplace)

**Systèmes usuels :**

| Ordre | FT type | Paramètres | Réponse indicielle |
|---|---|---|---|
| 0 | $H(p) = K$ | $K$ = gain statique | Échelon immédiat |
| 1 | $H(p) = \frac{K}{1 + \tau \cdot p}$ | $K$ = gain statique, $\tau$ = constante de temps | Exponentielle → $K \cdot u$ |
| 2 | $H(p) = \frac{K \cdot \omega_0^2}{p^2 + 2 \cdot \xi \cdot \omega_0 \cdot p + \omega_0^2}$ | $\xi$ = amortissement, $\omega_0$ = pulsation propre | Oscillations si $\xi < 1$ |

### Identification d'un système d'ordre 1

À partir de la réponse à un échelon $u_0$ :

- **Gain statique :** $K = y(\infty) / u_0$
- **Constante de temps $\tau$ :** temps pour atteindre 63 % de $y(\infty)$
- **Méthode graphique :** tangente à l'origine coupe la valeur finale en $t = \tau$

### Schémas-blocs — Règles de base

| Association | Formule | Schéma |
|---|---|---|
| Série (cascade) | $H_{tot} = H_1 \cdot H_2$ | E→H₁→H₂→S |
| Parallèle | $H_{tot} = H_1 + H_2$ | — |
| Contre-réaction (boucle fermée) | $FTBF = \frac{FTBO}{1 + FTBO}$ | Avec $FTBO = C(p) \cdot H(p)$ |

**Système bouclé :**
```
        C(p)         H(p)
ε(p)→─►[Correcteur]─►[Procédé]──┬──► S(p)
 ↑                               │
 │         B(p)           R(p)   │
 └─────────[Capteur]◄────────────┘
```

$$FTBF = \frac{C \cdot H}{1 + C \cdot H \cdot R}$$

### Performances d'un système bouclé

| Critère | Définition | Lien avec FTBO |
|---|---|---|
| **Précision** | Erreur statique $\varepsilon_s$ | $\varepsilon_s = 0$ si FTBO contient un intégrateur |
| **Stabilité** | Marge de phase $\Phi_m$ | $\Phi_m = 180° + \arg(FTBO(j\omega_c)) \geq 45°$ recommandé |
| **Rapidité** | Bande passante $\omega_{BP}$ | Fréquence pour laquelle $|FTBF| = 1/\sqrt{2}$ |

---

## Diagramme de Bode — Tracé asymptotique

### Gain K (constante)

- Module : $|H| = 20 \cdot \log(K)$ dB (horizontal)
- Phase : $\arg(H) = 0°$

### Intégrateur 1/p

- Module : $-20$ dB/décade, passe par 0 dB à $\omega = 1$ rad/s
- Phase : $-90°$ (constante)

### 1er ordre $1/(1 + \tau p)$

- Pour $\omega \ll 1/\tau$ : module $\approx 0$ dB, phase $\approx 0°$
- Pour $\omega \gg 1/\tau$ : module $\approx -20$ dB/décade, phase $\approx -90°$
- En $\omega = 1/\tau$ : module $= -3$ dB, phase $= -45°$

### 2e ordre $\omega_0^2/(p^2 + 2\xi\omega_0 p + \omega_0^2)$

- Résonance si $\xi < 0{,}707$ : pic à $\omega \approx \omega_0 \cdot \sqrt{1 - 2\xi^2}$
- Pour $\omega \gg \omega_0$ : pente $-40$ dB/décade

---

## SysML dans les sujets CAPET

Les sujets récents (2020–2025) utilisent systématiquement des diagrammes SysML :

| Diagramme | Lecture | Ce qu'on demande |
|---|---|---|
| Exigences (req) | Arborescence d'exigences (id, text, satisfy) | Identifier la contrainte associée à une question |
| Cas d'utilisation (uc) | Acteurs + cas + relations | Identifier les utilisateurs et fonctions du système |
| Définition de blocs (bdd) | Hiérarchie des composants | Identifier les sous-systèmes |
| IBD (Internal Block Diagram) | Flux entre composants | Tracer les chemins énergie/information |
| Séquence (sd) | Échanges temporels entre blocs | Lire un protocole de communication |

**Stratégie :** ne jamais sauter une question de lecture de SysML — la réponse est dans le diagramme.

---

## Types de questions au concours

| Type | Exemple | Formule/Méthode |
|---|---|---|
| Identifier K et τ | "Déterminer le gain statique et la constante de temps depuis la courbe" | $K = y(\infty)/u_0$ ; $\tau$ lu graphiquement |
| Calculer FTBF | "Exprimer la FT en boucle fermée avec un correcteur P" | $FTBF = \frac{K_p \cdot H}{1 + K_p \cdot H}$ |
| Tracer Bode asymptotique | "Tracer le diagramme de Bode de $H(p) = 10/(1+0{,}1p)$" | Pente 0 dB puis $-20$ dB/dec en $\omega = 10$ |
| Marge de phase | "Vérifier la stabilité du système" | $\Phi_m \geq 45°$ → stable |
| Erreur statique | "Le système est-il précis en régime permanent ?" | FTBO contient $1/p$ → $\varepsilon_s = 0$ |
| Lire un IBD | "Identifier les formes d'énergie échangées" | Lecture directe du diagramme |

---

## Pièges courants

1. **Confondre FTBO et FTBF** dans le calcul de l'erreur et de la stabilité. La stabilité se juge sur la FTBO (diagramme de Bode), pas la FTBF.
2. **Oublier le capteur** dans la FTBO : si gain capteur $R \neq 1$, $FTBO = C \cdot H \cdot R$.
3. **Lecture de $\tau$** : $\tau$ n'est pas le temps pour atteindre 100 % mais 63 % de la valeur finale.
4. **Signe de la contre-réaction** : $\varepsilon = $ consigne $-$ mesure (soustraction, pas addition).

---

## Liens avec d'autres thèmes

- → **T24 Correcteurs** : la modélisation est nécessaire avant de choisir et dimensionner un correcteur
- → **T11 Variation de vitesse** : modèle de la MAS pour la boucle de vitesse
- → **T17 Bode/filtres** : le diagramme de Bode est l'outil de la modélisation fréquentielle

---

*Source : sujets 2017 (Métro MF2000), 2019 (Transport câble), 2020 (Exotec), 2022 (Banc essai) · formulaire_capet.md §10*
