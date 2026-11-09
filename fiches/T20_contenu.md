# T20 — Régime sinusoïdal, filtres 1er/2e ordre (électronique)
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

### 1.1 Représentation complexe en régime sinusoïdal
Un signal $v(t) = V_m \cos(\omega t + \varphi)$ est représenté par le phaseur $\underline{V} = \frac{V_m}{\sqrt{2}} e^{j\varphi}$ (valeur efficace).

**Impédances complexes :**
$$Z_R = R \quad ; \quad Z_L = j L\omega \quad ; \quad Z_C = \frac{1}{jC\omega} = \frac{-j}{C\omega}$$

**Notation en variable de Laplace (jω ↔ p) :**
$$Z_L = Lp \quad ; \quad Z_C = \frac{1}{Cp}$$

### 1.2 Filtre passe-bas RC du 1er ordre (source : E1_Sujet_2026 — partie B)
Schéma : résistance $R$ en série, condensateur $C$ en parallèle avec la sortie.

**Fonction de transfert :**
$$H_{F1}(j\omega) = \frac{V_3}{V_2} = \frac{1}{1 + j\dfrac{\omega}{\omega_0}} \quad \text{avec} \quad \omega_0 = \frac{1}{RC}$$

**Module :** $|H| = \dfrac{1}{\sqrt{1 + (\omega/\omega_0)^2}}$

**Phase :** $\varphi = -\arctan(\omega/\omega_0)$

**Gain en dB :** $G_{dB} = -20 \log\sqrt{1 + (\omega/\omega_0)^2}$

À la fréquence de coupure $\omega = \omega_0$ :
$$|H(\omega_0)| = \frac{1}{\sqrt{2}} \approx 0{,}707 \quad \Longrightarrow \quad G_{dB} = -3 \text{ dB}$$

**Temps de réponse à 5 % :** $t_{r5\%} \approx 3\,\tau = 3RC$ (source : E1_Sujet_2026, Q B6).

**Diagramme de Bode asymptotique :**
- $\omega \ll \omega_0$ : gain $= 0$ dB, phase $= 0°$
- $\omega \gg \omega_0$ : pente $= -20$ dB/décade, phase $\to -90°$

### 1.3 Cascade de filtres passe-bas (source : E1_Sujet_2026 — partie B)
Deux filtres RC identiques en cascade (résistance d'entrée de l'étage suivant supposée infinie) :
$$H(j\omega) = \left(\frac{1}{1 + j\omega/\omega_0}\right)^2$$

Pente asymptotique : $-40$ dB/décade. Ce filtre du 2e ordre présente une réponse indicielle **sans oscillations** si le facteur d'amortissement $m \geq 1$ (cas de la mise en cascade de deux 1er ordre).

### 1.4 Filtre RL passe-bas
Résistance $R$ en parallèle avec inductance $L$ :
$$H(j\omega) = \frac{R}{R + jL\omega} = \frac{1}{1 + j\omega\tau} \quad \text{avec} \quad \tau = \frac{L}{R}$$

Même forme que le filtre RC avec $\tau = L/R$ à la place de $RC$.

Les enroulements d'une machine asynchrone se comportent comme des filtres passe-bas RL, ce qui atténue les harmoniques de courant générés par la MLI (source : Rapport_Jury_2024, B12–B13).

### 1.5 Filtre passe-bas du 2e ordre — forme canonique
$$H(j\omega) = \frac{H_0}{1 + 2m\,\dfrac{j\omega}{\omega_0} + \left(\dfrac{j\omega}{\omega_0}\right)^2}$$

Paramètres :
- $\omega_0$ : pulsation propre (rad/s)
- $m$ : facteur d'amortissement (coefficient d'amortissement réduit)
- $Q = 1/(2m)$ : facteur de qualité

**Fréquence de résonance** (pour $m < 1/\sqrt{2}$) :
$$\omega_r = \omega_0 \sqrt{1 - 2m^2}$$

**Comportements :**
| $m$ | Comportement |
|-----|-------------|
| $m > 1$ | Sur-amorti, pas d'oscillations |
| $m = 1$ | Critique, retour le plus rapide sans dépassement |
| $m < 1$ | Sous-amorti, oscillations et résonance |

### 1.6 Filtre passe-haut du 1er ordre
$$H(j\omega) = \frac{j\omega/\omega_0}{1 + j\omega/\omega_0}$$

Pente asymptotique basse fréquence : $+20$ dB/décade, phase $\to +90°$ en BF.

### 1.7 Filtre passe-bande
Fréquence centrale $f_0$, largeur de bande $\Delta f = f_0 / Q$.
$$H(j\omega) = \frac{j\omega/(\omega_0 Q)}{1 + j\omega/(\omega_0 Q) + (j\omega/\omega_0)^2}$$

### 1.8 Gabarit et cahier des charges filtre (source : E1_Sujet_2026 — Q B2)
Pour filtrer un perturbateur à $\omega_2$ avec un facteur d'atténuation $> 100$ (soit $> 40$ dB) :
$$G_{dB}(\omega_2) \leq -40 \text{ dB}$$
La pente d'un filtre du 1er ordre est $-20$ dB/décade : insuffisant. Il faut un **filtre du 2e ordre** (pente $-40$ dB/décade) ou deux filtres du 1er ordre en cascade.

### 1.9 Filtre anti-repliement (source : E2_Sujet_2026_BAC3 — Q B17)
Placé avant le CAN pour respecter le théorème de Shannon : $f_e \geq 2 f_{max}$.
La fréquence de coupure du filtre anti-repliement parfait est :
$$f_c = \frac{f_e}{2}$$

### 1.10 Filtrage numérique

*(complément du référentiel, 2026-11-10 — notion hors sujets 2013–2026 sauf mention)*

**Filtre numérique à réponse impulsionnelle finie (RIF) :**
$$y_n = \sum_{k=0}^{N-1} b_k \, x_{n-k}$$

**Moyenne glissante sur N échantillons :**
$$y_n = \frac{1}{N} \sum_{k=0}^{N-1} x_{n-k}$$

**Filtre récursif du premier ordre (lissage exponentiel) :**
$$y_n = a \, y_{n-1} + (1 - a) \, x_n$$
- Valable avec a = τ/(τ + Te), en discrétisant un premier ordre de constante τ par la méthode d'Euler arrière

**Fonction de transfert en z d'un filtre RIF :**
$$H(z) = \sum_{k=0}^{N-1} b_k \, z^{-k}$$

**Transformation bilinéaire :**
$$p = \frac{2}{T_e} \, \frac{1 - z^{-1}}{1 + z^{-1}}$$

---

## 2. QUESTIONS TYPES (max 6)

1. **(2026, B3)** Montrer que la fonction de transfert complexe du premier filtre peut s'écrire $H_{F1}(j\omega) = \dfrac{1}{1+j\omega/\omega_0}$. Exprimer $\omega_0$ en fonction de $R$ et $C$.

2. **(2026, B4)** Tracer le diagramme de Bode asymptotique du filtre (courbes de gain et de phase) puis esquisser le tracé réel.

3. **(2026, B5)** Pour $v_2(t) = 2 + 0{,}5 \sin(2\pi \cdot 900 \cdot t)$, déterminer à partir du diagramme de Bode les gains $G$ en dB, les modules $|H|$ et les phases associés aux pulsations des signaux $v_{21}(t)$ et $v_{22}(t)$.

4. **(2026, B6)** Déterminer l'expression de $v_3(t)$ en sortie du filtre ainsi qu'une estimation du temps de réponse à 5 %. Conclure sur la capacité du filtre à valider le cahier des charges.

5. **(2026, B9)** Proposer des valeurs pour $R$ et $C$ permettant de satisfaire le gabarit. Justifier si la réponse indicielle de ce filtre présente ou non des oscillations.

6. **(2026, B17)** Définir le rôle du filtre anti-repliement. Rappeler le théorème de Shannon. En déduire l'ordre de grandeur de la fréquence de coupure $f_c$ du filtre anti-repliement si ce dernier est considéré comme parfait.

---

## 3. ATTENTES DU JURY

- **Maîtriser la forme canonique** du filtre du 1er ordre ($H = 1/(1 + j\omega/\omega_0)$) et savoir l'identifier dans un schéma RC ou RL.
- **Tracer les diagrammes de Bode asymptotiques** avec précision : pentes correctes ($-20$ dB/décade), jonction à $\omega_0$, phase $-45°$ à $\omega_0$.
- **Lire graphiquement** le gain et la phase sur un diagramme de Bode pour calculer la sortie en régime sinusoïdal.
- **Savoir déduire l'ordre du filtre** nécessaire à partir d'un gabarit (atténuation requise / pente disponible).
- Connaître le lien entre **temps de réponse à 5 %** et constante de temps $\tau$ : $t_{r5\%} \approx 3\tau$.
- Le jury attend que le candidat sache **distinguer filtre passif et filtre actif** et justifier le choix.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique |
|----------|---------------|
| Signal utile (2026 B1) | $V_0 = 2$ V, $f_1 \approx 0$ Hz (DC) |
| Signal perturbateur (2026 B1) | $A = 0{,}5$ V, $f_2 = 900$ Hz |
| Atténuation requise (2026 B2) | $>100$ ($> 40$ dB) |
| Temps de réponse requis (2026 B2) | $< 50$ ms |
| $\omega_0$ filtre (2026) | à calculer : $\omega_0 = 1/(RC)$ |
| Temps de réponse filtre du 1er ordre | $t_{r5\%} \approx 3RC$ |
| Fréquence de commutation MLI | $f_p = 6$ kHz → harmoniques filtrés par enroulements moteur |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **Confondre $\omega_0$ et $f_0$** : $\omega_0 = 2\pi f_0$ — vérifier les unités (rad/s vs Hz).
- **Pente en dB/décade vs dB/octave** : 1 décade = facteur 10 en fréquence ; 1 octave = facteur 2. Une pente de $-20$ dB/décade = $-6$ dB/octave.
- **Gain à $\omega_0$** : le gain n'est pas nul à $\omega_0$, il vaut $-3$ dB ($\approx 0{,}707$). Erreur fréquente : écrire $|H(\omega_0)| = 0$.
- **Filtre du 2e ordre par cascade** : deux 1er ordre en cascade donnent bien un 2e ordre mais sans résonance ($m = 1$ pour deux identiques) — différent d'un RLC série.
- **Temps de réponse et fréquence de coupure** : $t_{r5\%} \approx 3/(f_c \cdot 2\pi)$ — ne pas confondre les deux critères.
- **Phase d'un filtre d'ordre 2** : elle peut dépasser $-180°$ à haute fréquence — important pour l'étude de la stabilité (T21).
- **Filtre anti-repliement** : mal connu — ne pas confondre son rôle (filtrer avant le CAN) avec un filtre de reconstruction (après le CNA).
- **Atténuation imposée → gain en dB → ordre du filtre** : raisonner sur un rapport linéaire sans passer en décibels empêche de choisir l'ordre du filtre. Diviser une composante par 100 correspond à $G = 20\log(1/100) = -40$ dB ; un filtre d'ordre $n$ chute de $20n$ dB par décade, donc $-40$ dB une décade après la coupure impose un ordre 2. Source : rapport du jury 2026 du troisième concours (même sujet que l'E1 externe 2026), question B2 = question B2 du sujet externe.
- **Filtrer un signal composé : une lecture par composante** : appliquer un seul gain à tout le signal donne une sortie fausse. Chaque composante est lue à sa propre pulsation : amplitude multipliée par $H(\omega_k) = 10^{G(\omega_k)/20}$ et phase décalée de $\varphi(\omega_k)$ ; la composante continue est multipliée par $H(0)$. Source : rapport du jury 2026 du troisième concours (même sujet que l'E1 externe 2026), question B5 et B6 = question B5 et B6 du sujet externe.
- **Stabilité d'un filtre numérique** : croire qu'un filtre numérique est toujours stable. Un RIF l'est toujours ; un RII, qui réinjecte ses sorties, peut diverger si ses pôles sortent du cercle unité.
- **Retard unitaire** : lire $z^{-1}$ comme une dérivée. Il représente un retard d'une période d'échantillonnage : $z^{-1}X(z)$ correspond à $x_{n-1}$.
- **Retard d'une moyenne glissante** : oublier le retard introduit par une moyenne glissante. Une moyenne sur N points retarde le signal d'environ $(N-1)/2$ périodes d'échantillonnage.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T21 — Fonctions de transfert / Bode** : le diagramme de Bode du filtre est identique à celui de la fonction de transfert d'un système du 1er ou 2e ordre. La fréquence de coupure $\omega_0$ est la pulsation propre du système.
- **T19 — AOP** : les filtres actifs associent AOP et cellules RC. L'intégrateur AOP réalise un filtre passe-bas d'ordre 1 avec un gain de DC infini.
- **T17 — Convertisseurs / MLI** : les harmoniques générés par la MLI sont filtrés par les inductances des moteurs (filtre RL passe-bas naturel) ou par un filtre LC dédié.
- **T06 — Chaîne d'acquisition / CAN** : le filtre anti-repliement est indispensable avant tout CAN (théorème de Shannon). Présent dans les sujets 2026 et 2023.
- **T09 — Machines asynchrones** : le courant sinusoïdal statorique est obtenu grâce à l'effet filtrant naturel des enroulements (filtre passe-bas RL).
