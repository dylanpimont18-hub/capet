# T21 — Fonctions de transfert, diagramme de Bode
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

### 1.1 Transformée de Laplace — rappels
Pour un signal $x(t)$ à conditions initiales nulles (hypothèses de Heaviside) :
$$\mathcal{L}\left\{\frac{dx}{dt}\right\} = p \cdot X(p) \quad ; \quad \mathcal{L}\left\{\int x\,dt\right\} = \frac{X(p)}{p}$$

**Fonction de transfert :** $H(p) = \dfrac{S(p)}{E(p)}$ (sortie/entrée, CI nulles).

### 1.2 Systèmes du 1er ordre
**Forme canonique :**
$$H(p) = \frac{K}{1 + \tau p}$$

- $K$ : gain statique (gain pour $\omega \to 0$, lu graphiquement sur le diagramme de Bode)
- $\tau$ : constante de temps (s)
- Pulsation de coupure : $\omega_c = 1/\tau$

**Identification graphique sur le Bode (source : E2_Disciplinaire_IE_2023, Q D4 ; E1_Sujet_2026, Q C4) :**
- Gain DC (plateau BF) = $20\log K$ dB
- Pulsation de coupure = intersection des deux asymptotes (0 dB/décade et $-20$ dB/décade)
- Pente HF = $-20$ dB/décade

**Réponse indicielle :** $s(t) = K \cdot E \left(1 - e^{-t/\tau}\right)$

Temps de réponse à 5 % : $t_{r5\%} \approx 3\tau$

**Exemple moteur avec modulateur d'énergie (E2_Disciplinaire_IE_2023) :**
$$H_M(p) = \frac{K_M}{(1+\tau_a p)(1+\tau_b p)} \approx \frac{K_M}{1+\tau p} \quad \text{(si } \tau_a \gg \tau_b\text{)}$$
Gain lu graphiquement : $+26{,}4$ dB sur le diagramme de Bode de $H_M(p)$.

### 1.3 Systèmes du 2e ordre
**Forme canonique (sources : E2_Disciplinaire_IE_2024, E1_Sujet_2024, E2_Disciplinaire_IE_2023) :**
$$H(p) = \frac{K}{1 + \dfrac{2m}{\omega_0}p + \dfrac{1}{\omega_0^2}p^2}$$

- $K$ : gain statique
- $\omega_0$ : pulsation propre (rad/s)
- $m$ : facteur d'amortissement (sans dimension)

**Dépassement relatif :**
$$D\% = 100 \cdot e^{-m\pi/\sqrt{1-m^2}} \quad \text{(valable pour } m < 1\text{)}$$

Dépassement nul pour $m \geq 1$.

**Temps de réponse à 5 % réduit :** lu sur l'abaque $t_{r5\%} \cdot \omega_0 = f(m)$.

**Exemples numériques (E2_Disciplinaire_IE_2024, C5–C6) :**
$$H_{bf}(p) = \frac{K_i K_p K_{méca}}{\tau_{méca} p^2 + (1+K_p K_{méca})p + K_i K_p K_{méca}}$$
$$\omega_0 = \frac{5}{t_r} \quad ; \quad m = \frac{2\tau_{méca}\omega_0 K_{méca} - 1}{2 K_{méca}} \quad \text{(avec } K_{méca} = 250,\ \tau_{méca} = 8{,}5 \text{ s)}$$

### 1.4 Diagramme de Bode
Le diagramme de Bode est constitué de deux courbes tracées en fonction de la pulsation $\omega$ (axe log) :

**Courbe de gain :**
$$G_{dB}(\omega) = 20 \log|H(j\omega)|$$

**Courbe de phase :**
$$\varphi(\omega) = \arg(H(j\omega))$$

**Règles asymptotiques :**
| Facteur | Gain asymptotique | Phase asymptotique |
|---------|------------------|-------------------|
| Gain pur $K$ | $20\log K$ (constant) | $0°$ |
| Intégrateur $1/p$ | $-20$ dB/déc ($0$ dB à $\omega=1$) | $-90°$ |
| 1er ordre $(1+\tau p)^{-1}$ | $0$ puis $-20$ dB/déc à partir de $1/\tau$ | $0°$ puis $-90°$ |
| 2e ordre (avec $m$) | $0$ puis $-40$ dB/déc à partir de $\omega_0$ | $0°$ puis $-180°$ |

**Tracé réel vs asymptotique :**
- Pour $m < 1/\sqrt{2} \approx 0{,}707$ : résonance visible avec un pic de gain au-dessus de l'asymptote.
- Gain au pic : $G_{pic} = 20\log\dfrac{1}{2m\sqrt{1-m^2}}$

### 1.5 Marge de phase et marge de gain (sources : E2_Disciplinaire_IE_2023, E1_Sujet_2026, E2_Disciplinaire_IE_2024)
Pour la **Fonction de Transfert en Boucle Ouverte (FTBO)** :

**Marge de phase $M_\varphi$ :**
$$M_\varphi = 180° + \arg\bigl(FTBO(j\omega_u)\bigr) \quad \text{où } |FTBO(j\omega_u)| = 1 \text{ (0 dB)}$$

**Marge de gain $M_G$ :**
$$M_G = -20\log|FTBO(j\omega_\pi)| \quad \text{où } \arg(FTBO(j\omega_\pi)) = -180°$$

**Critères habituels du cahier des charges :**
- $M_\varphi \geq 45°$ (sources : E2_Disciplinaire_IE_2023, E1_Sujet_2026)
- $M_\varphi \geq 90°$ (sources : E2_Disciplinaire_IE_2024, E1_Sujet_2025)
- $M_G \geq 10$ dB (source : E1_Sujet_2026)

**Procédure graphique :**
1. Lire $\omega_u$ sur la courbe de gain (croisement 0 dB).
2. Lire la phase à $\omega_u$ → calculer $M_\varphi = 180° + \varphi(\omega_u)$.
3. Lire $\omega_\pi$ sur la courbe de phase (croisement $-180°$).
4. Lire le gain à $\omega_\pi$ → calculer $M_G = -G_{dB}(\omega_\pi)$.

### 1.6 Correcteur proportionnel et tracé du Bode de FTBO
**FTBO avec correcteur proportionnel $C(p) = K_C$ :**
$$FTBO(p) = K_C \cdot H_M(p) \cdot K_{GT}$$

Ajouter $K_C$ revient à **décaler** la courbe de gain de $+20\log K_C$ dB sans modifier la phase.

**Détermination de $K_C$ pour satisfaire la marge de phase (source : E2_Disciplinaire_IE_2023, Q D8) :**
1. Sur le Bode de FTBO pour $K_C = 1$, lire le gain $G_0$ dB à la pulsation $\omega_u$ souhaitée.
2. $K_C$ tel que $20\log K_C + G_0 = 0$ dB → $K_C = 10^{-G_0/20}$.

### 1.7 Erreur statique
**Erreur statique en poursuite :**
$$\varepsilon_s = \lim_{t\to\infty} \varepsilon(t) = \lim_{p\to 0} p \cdot \varepsilon(p) = \frac{E}{1 + K_{BO}}$$

Pour un système avec intégrateur en boucle ouverte (classe 1) : $\varepsilon_s = 0$.

---

## 2. QUESTIONS TYPES (max 6)

1. **(2023, D4)** À l'aide du diagramme de Bode de $H_M(p)$, déterminer les valeurs numériques de $K_M$, $\omega_a$ et $\omega_b$ par lecture graphique.

2. **(2023, D6–D7)** Déterminer l'expression de la FTBO $= U_{GT}(p)/\varepsilon_V(p)$. Tracer sur le document réponse le diagramme de Bode de la FTBO pour $K_{PV} = 1$.

3. **(2023, D8)** Déterminer la valeur de $K_{PV}$ pour respecter une marge de phase de 45°.

4. **(2026, C4)** En s'appuyant sur l'essai indiciel, proposer un ordre pour la fonction de transfert $H_2(p)$. Exprimer $H_2(p)$ sous forme canonique en précisant la valeur de ses paramètres caractéristiques.

5. **(2026, C5–C6)** Tracer la marge de phase et donner sa valeur. Donner la marge de gain. Préciser si le cahier des charges ($M_\varphi > 45°$, $M_G > 10$ dB) est respecté. Déterminer la valeur limite $K_{Clim}$.

6. **(2024, C5–C6)** Déterminer la fonction de transfert en boucle fermée $H_{bf}(p) = \Omega(p)/\Omega_{ref}(p)$. Mettre sous forme canonique. Déterminer $m$ et $\omega_0$ en fonction de $K_p$, $K_i$, $K_{méca}$, $\tau_{méca}$.

---

## 3. ATTENTES DU JURY

- **Lire graphiquement** un diagramme de Bode : savoir extraire $K$, $\tau$ (ou $\omega_0$, $m$) par construction graphique sur l'essai indiciel ou le Bode. Compétence clé testée à chaque session.
- **Tracer le Bode asymptotique** correctement : les erreurs sur les pentes ($-20$ vs $-40$ dB/décade) ou les phases asymptotiques ($-90°$ vs $-180°$) sont sévèrement pénalisées.
- **Mettre la fonction de transfert sous forme canonique** : le jury insiste sur la mise sous forme $H = K/(1+\tau p)$ ou forme 2e ordre avec $m$ et $\omega_0$ clairement identifiés.
- **Calculer les marges** avec la méthode graphique uniquement (document réponse fourni avec le Bode) — ne pas chercher à calculer analytiquement.
- La partie C (asservissement, Bode, marges) est celle qui a été traitée par 79 % des candidats en 2024 mais correctement par seulement 31 % — c'est le thème le plus discriminant de l'épreuve.
- Le jury 2025 déplore le manque de maîtrise des lois basiques de l'électricité (loi des mailles, loi des nœuds) nécessaires pour établir les fonctions de transfert.
- **Identifier correctement** les schémas-blocs fournis dans les sujets — nombreuses erreurs sur l'expression de la FTBO.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur numérique (source) |
|----------|--------------------------|
| Gain $H_M(p)$ en BF | $+26{,}4$ dB = $K_M = 20{,}9$ rad·s$^{-1}$·V$^{-1}$ (2023) |
| $\tau_{méca}$ | $8{,}5$ s (2024) |
| $K_{méca}$ | $250$ (2024) |
| Amortissement requis | $m = 1$ (2024) |
| Temps de réponse requis | $t_r = 1$ s → $\omega_0 = 5$ rad/s (2024) |
| Marge de phase requise | $M_\varphi \geq 45°$ (2023, 2026) ou $M_\varphi \geq 90°$ (2024, 2025) |
| Marge de gain requise | $M_G \geq 10$ dB (2026) |
| Dépassement toléré | $D\% \leq 5\%$ (2024) |
| Erreur statique | nulle (classe 1, intégrateur) |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **Confondre FTBO et FTBF** : la marge de phase se calcule sur la **boucle ouverte**, mais la stabilité s'apprécie sur la **boucle fermée**.
- **Gain statique ≠ gain à 0 dB** : $K = H(0)$ est la valeur du module à fréquence nulle, et $20\log K$ est le niveau du plateau BF en dB.
- **Signe de la marge de phase** : $M_\varphi = 180° + \varphi(\omega_u)$. Si $\varphi(\omega_u) = -120°$, alors $M_\varphi = 60°$ > 0 → stable.
- **Pulsation $\omega_u$ non trouvée** si la courbe de gain ne croise pas 0 dB : le système est toujours stable pour tout gain.
- **Confondre $p$ et $j\omega$** dans l'expression de la fonction de transfert : $H(p)$ est la FdT en Laplace, $H(j\omega)$ est la réponse fréquentielle obtenue par substitution $p = j\omega$.
- **Identification depuis l'essai indiciel** : la valeur finale donne $K$, le temps de premier passage par 63 % de la valeur finale donne $\tau$ (1er ordre). Pour un 2e ordre, utiliser les formules de dépassement et temps de montée.
- **Tracé Bode avec intégrateur** : la droite de gain passe par 0 dB à $\omega = K_{BO}$ (pour un système de gain $K_{BO}$ en boucle ouverte) — erreur courante de positionnement.
- **Marge de gain infinie** : pour un système dont la phase ne descend jamais à $-180°$ (exemple : système du 1er ordre), la marge de gain est infinie — à savoir interpréter.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T20 — Filtres** : la fonction de transfert d'un filtre RC du 1er ordre est $H(p) = 1/(1+\tau p)$ — forme canonique du système du 1er ordre. Le diagramme de Bode du filtre et celui de la FdT sont identiques.
- **T19 — AOP** : le correcteur PI (proportionnel-intégral) est implémenté par un AOP avec résistance et condensateur dans la boucle de contre-réaction. Sa FdT est $C(p) = K_p(1 + 1/(\tau_i p))$.
- **T18 — Composants** : le modèle moyen d'un hacheur autour d'un point de repos donne la FdT $\delta V_{DC}(p)/\delta\alpha(p)$ utilisée pour synthétiser le correcteur (source : E2_Disciplinaire_IE_2025).
- **T22 — Asservissements** : T21 est le prérequis indispensable — toute étude de stabilité, de marges, de performances (erreur statique, dépassement, rapidité) repose sur la maîtrise des FdT et du Bode.
- **T09 — Machines électriques** : la machine asynchrone avec son variateur est modélisée par une FdT du 1er ordre $K_{méca}/(1+\tau_{méca}p)$ dans les schémas-blocs d'asservissement de vitesse (récurrent 2024, 2025).
