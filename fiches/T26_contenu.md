# T26 — Modélisation des systèmes linéaires (automatique)
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

### 1.1 Transformée de Laplace et conditions de Heaviside

La transformée de Laplace d'une fonction $f(t)$ est définie par :

$$F(p) = \mathcal{L}\{f(t)\} = \int_0^{+\infty} f(t)\,e^{-pt}\,dt$$

**Transformées usuelles :**

| $f(t)$ | $F(p)$ |
|--------|--------|
| Échelon unité $u(t)$ | $\dfrac{1}{p}$ |
| Rampe $t \cdot u(t)$ | $\dfrac{1}{p^2}$ |
| Exponentielle $e^{-t/\tau}$ | $\dfrac{1}{1+\tau p}$ |
| Dérivée $\dfrac{df}{dt}$ | $p\,F(p) - f(0^-)$ |
| Intégrale $\int_0^t f(\tau)d\tau$ | $\dfrac{F(p)}{p}$ |

En **conditions de Heaviside** (conditions initiales nulles) : $\mathcal{L}\{f'(t)\} = p\,F(p)$.

### 1.2 Fonction de transfert

Pour un système linéaire invariant, la fonction de transfert est :
$$H(p) = \frac{S(p)}{E(p)}$$

**Forme canonique du 1er ordre :**
$$H(p) = \frac{K}{1 + \tau p}$$
- $K$ : gain statique (sans dimension ou [S]/[E])
- $\tau$ : constante de temps [s]
- Réponse indicielle : $s(t) = K\,E_0\,(1 - e^{-t/\tau})$

**Forme canonique du 2ème ordre :**
$$H(p) = \frac{K}{1 + \frac{2m}{\omega_0}p + \frac{p^2}{\omega_0^2}}$$
- $\omega_0$ : pulsation propre [rad·s$^{-1}$]
- $m$ : coefficient d'amortissement (sans dimension)
- Pour $m < 1$ : régime sous-amorti, oscillations
- Pour $m = 1$ : régime critique, pas de dépassement
- Pour $m > 1$ : régime sur-amorti

**Dépassement relatif** (pour $m < 1$) :
$$D\% = 100\,\exp\!\left(\frac{-m\pi}{\sqrt{1-m^2}}\right)$$

### 1.3 Modèle de la machine à courant continu (MCC)

**Équation électrique de l'induit :**
$$u(t) = R\,i(t) + L\,\frac{di(t)}{dt} + e(t)$$

En régime permanent : $U = R\,I + E$ avec $E = K_e\,\Omega$

**Constantes de la MCC :**
- $K_e = K_c$ [V·s·rad$^{-1}$] = [N·m·A$^{-1}$]

**Bilan de puissances :**
$$P_A = U\,I \quad;\quad P_{JR} = R\,I^2 \quad;\quad P_{EM} = E\,I \quad;\quad P_U = P_{EM} - P_{FM}$$

**Caractéristique mécanique :**
$$C_U = \frac{K_c}{R}\,(U - K_e\,\Omega) - C_p = f(\Omega)$$

*Source : E1 Sujet 2026 — actionneur MCC pour porte de bus (R = 6,6 Ω ; L = 100 mH ; $K_e$ = 1,044 V·s·rad$^{-1}$)*

### 1.4 Diagramme de Bode

Pour $H(j\omega) = \frac{K}{1 + j\omega\tau}$ :

- **Gain asymptotique :** $G_{dB}(\omega) = 20\log|H(j\omega)|$
  - Pour $\omega \ll 1/\tau$ : $G_{dB} \approx 20\log K$
  - Pour $\omega \gg 1/\tau$ : pente $-20$ dB/décade
- **Phase :** $\varphi(\omega) = -\arctan(\omega\tau)$
  - $\varphi(\omega_0) = -45°$ à la fréquence de coupure

Pour un filtre du 2ème ordre : pente $-40$ dB/décade après $\omega_0$.

### 1.5 Schéma-bloc : règles de manipulation

- **Mise en série :** $H_{eq}(p) = H_1(p) \cdot H_2(p)$
- **Mise en parallèle :** $H_{eq}(p) = H_1(p) + H_2(p)$
- **Boucle fermée avec retour H(p) :**
$$H_{BF}(p) = \frac{H_D(p)}{1 + H_D(p)\,H(p)}$$
- **Boucle ouverte (BO) :** $H_{BO}(p) = H_D(p)\,H(p)$

### 1.6 Identification par essai indiciel

**1er ordre :** à partir de la réponse à un échelon $E_0$ :
- Gain statique : $K = s(\infty)/E_0$
- Constante de temps $\tau$ : lire la valeur à $0{,}632\,K\,E_0$ sur la courbe (méthode des tangentes)

**2ème ordre :** identifier $\omega_0$ et $m$ à partir des pics et de la pseudo-période.

### 1.7 Systèmes d'état (représentation d'état)

$$\dot{\mathbf{x}}(t) = A\mathbf{x}(t) + B\mathbf{u}(t) \quad;\quad \mathbf{y}(t) = C\mathbf{x}(t) + D\mathbf{u}(t)$$

*Utilisé dans le sujet 2025 pour le convertisseur élévateur (modèle d'état moyen) et l'asservissement de tension.*

---

## 2. QUESTIONS TYPES

**Q1.** (2026 — E1 Q.A1) Écrire l'équation électrique de l'induit d'une MCC. Simplifier en régime permanent. Déterminer $R$ à partir d'un essai à rotor bloqué.

**Q2.** (2026 — E1 Q.A4) Déterminer la constante $K_e$ à partir du fonctionnement nominal en régime permanent.

**Q3.** (2026 — E1 Q.C1) À partir d'une équation différentielle du capteur de vitesse, déterminer la fonction de transfert $H_3(p) = V_{capt}(p)/\Omega(p)$ en appliquant les conditions de Heaviside.

**Q4.** (2026 — E1 Q.C4) À partir d'un essai indiciel, proposer un ordre pour $H_2(p)$ ; construire graphiquement ses paramètres ($K$, $\tau$) ; exprimer $H_2(p)$ sous forme canonique.

**Q5.** (2026 — E1 Q.C7–C8) Montrer que la FTBF d'une boucle d'asservissement se met sous la forme du 2ème ordre. Exprimer $\omega_0$ et $m$ en fonction du gain du correcteur $K_C$. En déduire la valeur de $K_C$ assurant un dépassement nul.

**Q6.** (2025 — E1 Q.37–38) Établir les fonctions de transfert $H_2(p)$ et $H_3(p)$ du modèle d'état moyen d'un convertisseur élévateur par superposition.

---

## 3. ATTENTES DU JURY

D'après les rapports de jury 2023, 2024, 2025 :

- Le jury **dénonce systématiquement** les lacunes en automatique : « *C'est un champ disciplinaire important des sciences industrielles auquel les candidats au CAPET de SII ne peuvent se soustraire. Le jury invite les candidats à revoir les concepts de base de ce domaine.* » (rapport 2023)
- Le jury attend la **maîtrise des conditions de Heaviside** et le passage équation différentielle → fonction de transfert.
- Les candidats doivent être capables de **lire un diagramme de Bode** pour identifier les paramètres d'une fonction de transfert.
- La **rédaction des démonstrations** est exigée : recopier la formule finale sans démonstration est sanctionné.
- Les **expressions littérales homogènes** et les **unités correctes** sont impératives.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique (sujets 2023–2026) |
|----------|----------------------------------|
| Constante de temps $\tau$ du moteur | $0{,}1$ à $0{,}9$ s |
| Gain statique MCC | $K_m = 2{,}88$ rad·s$^{-1}$·V$^{-1}$ (2026) |
| Pulsation propre $\omega_0$ de la FTBF | 5 à 7 000 rad·s$^{-1}$ selon l'application |
| Dépassement maximal admis | $D\% \leq 5\,\%$ |
| Temps de réponse à 5 % | $< 0{,}2$ s (2026), $< 50$ ms (filtre) |
| Erreur statique exigée | $< 5\,\%$ ou nulle |
| Fréquence d'échantillonnage pile (2026) | $f_{min} = 10/t_{R5\%}$ |
| Constante de temps pile à combustible | $\tau = 0{,}9$ s ; $K = 4°C\cdot V^{-1}$ (2026) |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **Confusion régime transitoire / permanent** : ne pas négliger $L$ en transitoire.
- **Conditions initiales non nulles** : oublier de vérifier que les conditions de Heaviside sont satisfaites.
- **Identification graphique** : lire $\tau$ à 63,2 % et non à 50 % ou 90 %.
- **Signe du retour** : dans $H_{BF} = H_D/(1 + H_{BO})$, le signe $+$ est pour un retour négatif.
- **Homogénéité** : confondre $K_e$ (V·s·rad$^{-1}$) et $K_c$ (N·m·A$^{-1}$) alors qu'ils sont numériquement égaux.
- **Bode pour $K_C = 1$** : le jury demande souvent le diagramme pour $K_C = 1$ avant de chercher le $K_C$ optimal.
- **Dépassement et amortissement** : la condition $D = 0$ implique $m \geq 1$, pas seulement $m = 1$.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T27** : la stabilité (marges) est l'étape naturellement suivante de la modélisation T26.
- **T15/T16 (convertisseurs statiques)** : les hacheurs et redresseurs fournissent les systèmes asservis (MCC, variateur).
- **T22/T24 (électronique analogique)** : filtres, amplificateurs op-amp, chaînes de mesure liées au conditionnement avant asservissement.
- **T30 (métrologie)** : chaîne d'acquisition = capteur + conditionneur + CAN ; précision et résolution influent sur les performances de l'asservissement.
- **T29 (automatisme)** : le correcteur numérique (relation de récurrence) est la traduction discrète du correcteur continu de T26.
