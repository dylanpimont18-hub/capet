# T03 — Représentation complexe, impédances

## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

| Grandeur / Loi | Formule | Unité |
|----------------|---------|-------|
| Impédance résistive | $\underline{Z}_R = R$ | Ω |
| Impédance capacitive | $\underline{Z}_C = \dfrac{1}{j C \omega} = \dfrac{-j}{C\omega}$ | Ω |
| Impédance inductive | $\underline{Z}_L = j L \omega$ | Ω |
| Loi d'Ohm complexe | $\underline{U} = \underline{Z} \cdot \underline{I}$ | V |
| Admittance | $\underline{Y} = 1/\underline{Z}$ | S |
| Module d'une impédance RC série | $|\underline{Z}| = \sqrt{R^2 + (1/C\omega)^2}$ | Ω |
| Module d'une impédance RL série | $|\underline{Z}| = \sqrt{R^2 + (L\omega)^2}$ | Ω |
| Déphasage circuit RC série | $\varphi = -\arctan\!\left(\dfrac{1}{RC\omega}\right)$ | rad |
| Déphasage circuit RL série | $\varphi = \arctan\!\left(\dfrac{L\omega}{R}\right)$ | rad |
| Résonance en série (fréquence) | $f_0 = \dfrac{1}{2\pi\sqrt{LC}}$ | Hz |
| Résonance en série (pulsation) | $\omega_0 = \dfrac{1}{\sqrt{LC}}$ | rad/s |
| Facteur de qualité (série) | $Q = \dfrac{L\omega_0}{R} = \dfrac{1}{RC\omega_0}$ | — |
| Fonction de transfert 1er ordre | $H(j\omega) = \dfrac{1}{1 + j\omega/\omega_c}$ | — |
| Forme canonique 2e ordre | $H(j\omega) = \dfrac{1}{1 + 2m\,j\omega/\omega_0 - (\omega/\omega_0)^2}$ | — |
| Gain Bode (dB) | $G_{dB} = 20\log_{10}|H(j\omega)|$ | dB |
| Déphasage Bode | $\varphi(\omega) = \arg(H(j\omega))$ | ° |
| Marge de phase | $M_\varphi = 180° + \arg(H_{BO}(j\omega_{c0}))$ | ° |
| Impédance MAS (modèle monophasé) | $\underline{I}_r' = \dfrac{\underline{V}_s}{jL_f\omega_s + R_r'/g}$ | A |
| Condensateur de démarrage moteur | $\underline{Z}_{Cp} = 1/(jC_p\omega)$ ; produit déphasage $\approx 90°$ | Ω |

---

## 2. QUESTIONS TYPES

### Q1 — Modèle monophasé équivalent MAS (2024, Extracteur d'air, DT1)
**Source :** E2_Disciplinaire_IE_2024, document technique DT1, partie A  
**Énoncé :** La machine asynchrone est modélisée en monophasé équivalent. Exprimer le courant rotorique ramené au stator $I_r'$ en fonction de $V_s$, $L_f$, $\omega_s$, $R_r'$, $g$.  
**Corrigé :** En notation complexe, le circuit monophasé équivalent de la MAS donne :  
$\underline{I}_r' = \dfrac{\underline{V}_s}{j L_f \omega_s + R_r'/g}$  
Le module de cette impédance varie avec le glissement $g$ : à $g = 1$ (démarrage), $R_r'/g = R_r'$ (résistance nominale) ; en régime établi ($g \approx 0{,}03$), $R_r'/g \gg L_f\omega_s$.

---

### Q2 — Condensateur de déphasage moteur monophasé (2024, Extracteur d'air, D15)
**Source :** E2_Disciplinaire_IE_2024 / E1_Sujet_2024, partie D  
**Énoncé :** Un condensateur $C_p$ est placé en série avec l'enroulement auxiliaire d'un moteur asynchrone monophasé pour produire le déphasage nécessaire au démarrage. Décrire le rôle de $C_p$.  
**Corrigé :** $C_p$ crée une impédance $\underline{Z}_{Cp} = 1/(jC_p\omega)$ déphasant le courant dans l'enroulement auxiliaire de $-90°$ par rapport à l'enroulement principal. Ce déphasage crée un champ tournant elliptique permettant le démarrage autonome.

---

### Q3 — Déphasage et expression analytique de tension (2018, Rapport jury)
**Source :** Rapport_Jury_2018, partie C, questions 10-11  
**Énoncé :** Valider le principe d'un régulateur de tension par démarche analytique. Donner la valeur du déphasage introduit par le filtre.  
**Corrigé (résumé jury) :** Beaucoup de candidats ont su donner la valeur numérique du déphasage, mais peu ont obtenu l'expression analytique correcte de la tension. Il faut exprimer $v_s(t) = |H(j\omega)| \cdot V_m \cos(\omega t + \varphi)$ avec $\varphi = \arg(H(j\omega))$.

---

### Q4 — Facteur de puissance et puissance déformante (2018, Sujet IE)
**Source :** E2_Sujet_2018, partie sur les harmoniques, questions 7-9  
**Énoncé :** Le courant absorbé par un convertisseur contient des harmoniques. Définir le facteur de puissance (FP) et le facteur de déplacement ($\cos\varphi_1$). Calculer la puissance réactive $Q_1$ liée au fondamental et la puissance déformante $D$.  
**Corrigé :**  
- $\cos\varphi_1$ : déphasage entre la tension (sinusoïdale) et le fondamental du courant  
- $FP = P / S = \cos\varphi_1 / \sqrt{1 + THD^2}$ (en tenant compte des harmoniques)  
- $Q_1 = V_1 \cdot I_1 \cdot \sin\varphi_1$  
- $D = V_1 \cdot \sqrt{I_2^2 + I_3^2 + \cdots} = V_1 \cdot I_1 \cdot THD / \sqrt{1 + THD^2}$

---

### Q5 — Marge de phase et stabilité (2024, Extracteur d'air, C5-C10)
**Source :** E2_Disciplinaire_IE_2024, partie C  
**Énoncé :** À partir de la fonction de transfert en boucle ouverte $H_{BO}(p)$ du correcteur + moteur, calculer la marge de phase. Conclure sur la stabilité.  
**Corrigé :** La marge de phase se lit sur le diagramme de Bode :  
$M_\varphi = 180° + \arg\!\left(H_{BO}(j\omega_{c0})\right)$  
où $\omega_{c0}$ est la pulsation de coupure à $0\,\text{dB}$. Une marge de phase $> 45°$ garantit un système stable avec un dépassement acceptable. Seuls $31\%$ des candidats ont traité correctement cette partie en 2024.

---

### Q6 — Forme canonique du second ordre (cours)
**Source :** Cours / programme — non trouvé directement dans les sujets mais attendu par le jury  
**Énoncé :** Écrire la forme canonique d'une fonction de transfert du 2e ordre. Identifier $\omega_0$ et $m$.  
**Corrigé :**  
$H(j\omega) = \dfrac{H_0}{1 + 2m\,(j\omega/\omega_0) + (j\omega/\omega_0)^2}$  
- $\omega_0$ : pulsation propre (rad/s)  
- $m$ : coefficient d'amortissement (sans unité)  
- Pour $m < 1$ : régime pseudo-périodique (oscillations)  
- Pour $m \geq 1$ : régime apériodique (sans oscillation)  
- Marge de phase optimale : $m \approx 0{,}7$ donne $M_\varphi \approx 65°$

---

## 3. ATTENTES DU JURY

**Rapport jury 2024 (citation directe) :**  
> *"La partie C (asservissement) a été abordée par seulement 31% des candidats avec correction ; le jury note que la représentation complexe et les diagrammes de Bode font partie des bases attendues à ce niveau."*

**Rapport jury 2018 (citation directe) :**  
> *"Si beaucoup de candidats ont su donner la valeur du déphasage, peu d'entre eux ont obtenu une expression analytique correcte de la tension."*

**Rapport jury 2025 :**  
> *"La partie 3 (asservissement) n'a été abordée que par 74% des candidats, et seulement 7% ont obtenu la moyenne sur cette partie. Le jury rappelle que les outils de l'automatique linéaire (Bode, diagramme de Black, marge de phase) sont au programme."*

**Résumé des attentes :**
- Savoir calculer module et argument d'une impédance complexe
- Identifier la forme canonique du 1er et 2e ordre dans une fonction de transfert
- Tracer (ou lire) un diagramme de Bode asymptotique
- Calculer la marge de phase et conclure sur la stabilité
- Exprimer analytiquement un déphasage, pas seulement une valeur numérique

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique | Source |
|----------|----------------|--------|
| Pulsation réseau | $\omega = 314\,\text{rad/s}$ | — |
| Impédance inductive MAS ($L_f$) | dépend du modèle (fourni en DT) | 2024 DT1 |
| Résistance rotorique $R_r'$ | fournie dans le DT | 2024 |
| Glissement nominal | $g \approx 0{,}03$ à $0{,}05$ | 2024 |
| Coefficient d'amortissement optimal | $m \approx 0{,}7$ ($M_\varphi \approx 65°$) | cours |
| Fréquence de coupure filtre LC (2024) | calculée à partir de $L$, $C$ fournis | 2024 partie C |
| Capacité démarrage moteur mono | quelques µF à quelques dizaines µF | 2024 D15 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Oublier $j$ dans l'impédance** : écrire $Z_L = L\omega$ au lieu de $\underline{Z}_L = jL\omega$ perd l'information de déphasage et fait des calculs de puissance incorrects.

2. **Confondre $\cos\varphi$ et facteur de puissance** : en présence d'harmoniques, $FP \neq \cos\varphi_1$. Le $FP$ est réduit par le THD.

3. **Lire une marge de phase sur Bode** : la marge de phase n'est pas la phase à $0\,\text{dB}$, mais $180° +$ cette phase (attention au signe).

4. **Forme canonique 2e ordre** : ne pas confondre $m$ (adimensionnel) et $\omega_0$ (rad/s). Beaucoup de candidats inversent les termes ou oublient le facteur 2 dans $2m/\omega_0$.

5. **Modèle MAS** : à l'arrêt ($g = 1$) l'impédance rotorique est $R_r'$ ; en régime ($g \approx 0{,}03$), elle devient $R_r'/g \approx 33 R_r'$. Ne pas confondre les deux situations.

6. **Déphasage ≠ argument** : l'argument d'une impédance donne le déphasage courant/tension, avec un signe conventionnel ($i$ en retard sur $u$ si $\varphi > 0$, inductif).

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T01 (Électrocinétique)** : les lois de Kirchhoff s'appliquent directement en notation complexe. La représentation de Fresnel est l'outil graphique des mailles complexes.
- **T04 (Harmoniques)** : le facteur de déplacement de puissance $\cos\varphi_1$ est l'argument de l'impédance au fondamental ; les harmoniques dégradent le facteur de puissance global.
- **T06 (MAS)** : le modèle monophasé équivalent de la MAS est une application directe des impédances complexes ($\underline{Z}_{rotor} = R_r'/g + jL_f\omega_s$).
- **T09 (Convertisseurs)** : les filtres LC en sortie d'onduleur ou de hacheur se dimensionnent par les formules de résonance $\omega_0 = 1/\sqrt{LC}$ et le facteur de qualité $Q$.
- **T02 (Asservissement)** : les diagrammes de Bode et la marge de phase sont les outils centraux de l'automatique linéaire fréquentielle.
