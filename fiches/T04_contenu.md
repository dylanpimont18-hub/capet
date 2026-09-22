# T04 — Harmoniques réseau, THD, puissance déformante

## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

| Grandeur / Loi | Formule | Unité |
|----------------|---------|-------|
| Décomposition de Fourier | $i(t) = I_0 + \sum_{n=1}^{\infty} I_n\sqrt{2}\cos(n\omega t + \varphi_n)$ | A |
| THD courant (définition IEC) | $THD = \dfrac{\sqrt{I_2^2 + I_3^2 + \cdots + I_n^2}}{I_1}$ | — |
| THD en % | $THD\% = THD \times 100$ | % |
| Valeur efficace totale | $I_{eff} = \sqrt{I_1^2 + I_2^2 + \cdots + I_n^2} = I_1\sqrt{1 + THD^2}$ | A |
| Puissance active | $P = V_1 \cdot I_1 \cdot \cos\varphi_1$ (seul le fondamental contribue si $v$ est sinusoïdale) | W |
| Puissance réactive | $Q = V_1 \cdot I_1 \cdot \sin\varphi_1$ | VAR |
| Puissance déformante | $D = V_1 \cdot \sqrt{I_2^2 + I_3^2 + \cdots}$ | VAD |
| Puissance apparente | $S = \sqrt{P^2 + Q^2 + D^2}$ | VA |
| Facteur de puissance (avec harm.) | $FP = \dfrac{P}{S} = \dfrac{\cos\varphi_1}{\sqrt{1 + THD^2}}$ | — |
| THD pleine onde triphasé (théorie) | $THD_{th} = \sqrt{(1/5)^2 + (1/7)^2 + \cdots} \approx 0{,}48$ | — |
| Norme IEC/EN 61000-2-2 | $THD < 25\%$ (= $0{,}25$) pour raccordement réseau | — |
| Rang des harmoniques (pont triphasé) | $h = 6k \pm 1$ : rangs $5, 7, 11, 13, \ldots$ | — |
| Rapport cyclique MLI | $\alpha = t_{on}/T_{MLI}$ | — |
| Fréquence de découpage | $f_{MLI}$ : typiquement 1 à 20 kHz | Hz |
| Filtre LC passe-bas (fréquence de coupure) | $f_c = \dfrac{1}{2\pi\sqrt{LC}}$ à placer sous $f_{MLI}$ | Hz |

---

## 2. QUESTIONS TYPES

### Q1 — Calcul du THD pleine onde (2024, Extracteur d'air, B9-B10)
**Source :** E2_Disciplinaire_IE_2024, partie B, questions B9-B10  
**Énoncé :** L'onduleur fonctionne en mode pleine onde (sans MLI). Calculer le THD du courant absorbé par la MAS en utilisant la décomposition spectrale fournie dans le DT.  
**Corrigé :** En pleine onde triphasé, les harmoniques dominants sont de rangs 5, 7, 11, 13... Le calcul donne :  
$THD_{cas\,1} = \sqrt{(I_5/I_1)^2 + (I_7/I_1)^2 + \cdots} \approx 0{,}59 \quad (59\%)$  
Ce THD dépasse la limite de la norme IEC 61000-2-2 ($THD < 25\%$).

---

### Q2 — Calcul du THD avec MLI 6 kHz (2024, Extracteur d'air, B11-B13)
**Source :** E2_Disciplinaire_IE_2024, partie B, questions B11-B13 ; Rapport_Jury_2024  
**Énoncé :** L'onduleur utilise une MLI à $f_{MLI} = 6\,\text{kHz}$. Calculer le THD. Expliquer comment la MLI modifie le spectre harmonique. Proposer un filtre.  
**Corrigé :**  
$THD_{cas\,2} = 0{,}25 \quad (25\%)$  
La MLI déplace les harmoniques de basse fréquence (rangs 5, 7...) vers les hautes fréquences (autour de $f_{MLI}$ et ses multiples). Cela permet de les filtrer avec un filtre passe-bas LC de fréquence de coupure $f_c < f_{MLI}$.  
**Jury 2024 :** *"La MLI permet de limiter le THD du courant et donc d'en limiter les ondulations. La mise en place de la MLI génère des harmoniques dans les hautes fréquences, permettant l'utilisation d'un filtre passe-bas."*

---

### Q3 — THD fondamental onduleur pleine onde (2025, Site isolé Mafate)
**Source :** E2_Disciplinaire_IE_2025, convertisseur CV3-2  
**Énoncé :** L'onduleur CV3-2 fonctionne en pleine onde. Calculer le THD sur le fondamental de la tension de sortie.  
**Corrigé :** Le THDfond de la tension d'un onduleur monophasé pleine onde est :  
$THD_{fond} = 0{,}48 \quad (48\%)$  
Ce résultat s'obtient par la série de Fourier : $v(t) = \dfrac{4V_{DC}}{\pi}\left(\cos\omega t - \dfrac{1}{3}\cos 3\omega t + \dfrac{1}{5}\cos 5\omega t - \cdots\right)$  
Le rapport $\sqrt{(1/3)^2 + (1/5)^2 + \cdots}/1 \approx 0{,}48$.

---

### Q4 — Facteur de puissance et puissance déformante (2018, Sujet IE)
**Source :** E2_Sujet_2018, questions 7-9  
**Énoncé :** Un convertisseur absorbe un courant déformé. Calculer la puissance déformante $D$ et le facteur de puissance réel $FP$.  
**Corrigé :**  
$D = V_1 \cdot I_{harm} = V_1 \cdot \sqrt{I_2^2 + I_3^2 + \cdots}$  
$FP = \dfrac{P}{S} = \dfrac{V_1 I_1 \cos\varphi_1}{\sqrt{(V_1 I_1 \cos\varphi_1)^2 + (V_1 I_1 \sin\varphi_1)^2 + D^2}}$  
Le facteur de déplacement $\cos\varphi_1$ est le déphasage entre $v_1(t)$ (fondamental de tension) et $i_1(t)$ (fondamental de courant).

---

### Q5 — Norme IEC 61000-2-2 et conformité (2024, B10)
**Source :** E2_Disciplinaire_IE_2024, partie B  
**Énoncé :** Comparer le THD calculé en cas 1 (pleine onde) et cas 2 (MLI 6 kHz) à la limite de la norme IEC/EN 61000-2-2. Conclure.  
**Corrigé :**  
- Cas 1 : $THD = 0{,}59 = 59\%$ → Non conforme ($> 25\%$)  
- Cas 2 : $THD = 0{,}25 = 25\%$ → Conforme à la limite ($\leq 25\%$)  
La MLI à 6 kHz est nécessaire pour respecter la norme de compatibilité électromagnétique.

---

### Q6 — Ondulation de courant hacheur entrelacé (2023, Robot Bakus)
**Source :** E2_Disciplinaire_IE_2023, hacheur 4 branches entrelacées  
**Énoncé :** Exprimer l'ondulation de courant $\Delta i_{Bakus}$ en sortie du hacheur DC/DC 4 branches entrelacées.  
**Corrigé :** Pour un hacheur élévateur à $f$ Hz, inductance $L$, rapport cyclique $\alpha$ :  
$\Delta i_{Bakus} = \dfrac{E_{LiFePO4} \cdot \alpha(1-\alpha)}{L \cdot f}$  
L'entrelacement de 4 branches réduit l'ondulation d'un facteur 4 environ, ce qui améliore la qualité du courant fourni à la batterie.

---

## 3. ATTENTES DU JURY

**Rapport jury 2024 (citation directe) :**  
> *"La MLI permet de limiter le THD du courant et donc d'en limiter les ondulations. La mise en place de la MLI génère des harmoniques dans les hautes fréquences, permettant l'utilisation d'un filtre passe-bas."*

**Rapport jury 2024 (sur les résultats) :**  
> *"THD cas 1 = 0,59 (pleine onde, non conforme norme IEC 61000-2-2) ; THD cas 2 = 0,25 (MLI 6 kHz, conforme)."*

**Rapport jury 2025 :**  
> *"La partie 2 (convertisseurs et harmoniques) a été abordée par 97% des candidats mais seulement 8,5% ont obtenu la moyenne. Le calcul de THD reste mal maîtrisé."*

**Résumé des attentes :**
- Connaître la définition normalisée du THD et savoir le calculer
- Expliquer qualitativement l'effet de la MLI sur le spectre harmonique
- Connaître la norme IEC/EN 61000-2-2 (THD < 25%) et savoir conclure sur la conformité
- Distinguer facteur de déplacement $\cos\varphi_1$ et facteur de puissance $FP$
- Savoir que la puissance déformante $D$ est due aux harmoniques (pas au déphasage)

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur | Source |
|----------|--------|--------|
| THD cas 1 (pleine onde 2024) | $0{,}59$ = $59\%$ | 2024 B9 |
| THD cas 2 (MLI 6 kHz 2024) | $0{,}25$ = $25\%$ | 2024 B11 |
| THDfond onduleur pleine onde 2025 | $0{,}48$ = $48\%$ | 2025 |
| Limite norme IEC 61000-2-2 | $THD < 25\%$ | IEC norm. |
| Fréquence MLI extracteur 2024 | $f_{MLI} = 6\,\text{kHz}$ | 2024 B11 |
| Harmoniques rangs (pont tri.) | $5, 7, 11, 13, 17, 19, \ldots$ | — |
| Amplitude harm. de rang $n$ (pleine onde) | $I_n = I_1/n$ | théorie |
| Rapport cyclique type | $\alpha \in [0{,}1 ; 0{,}9]$ | — |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Définition du THD** : la formule est $THD = \sqrt{\sum_{n\geq 2} I_n^2} / I_1$ (normalisée par le fondamental $I_1$), et non par la valeur efficace totale. Certains candidats confondent ces deux normalisations.

2. **Norme IEC 61000-2-2** : la limite de $25\%$ s'applique au THD global du courant injecté dans le réseau. Ne pas confondre avec des limites par harmonique individuelle.

3. **MLI ne supprime pas les harmoniques** : elle les déplace vers des fréquences plus élevées (autour de $f_{MLI}$ et ses multiples). Le filtrage LC est toujours nécessaire.

4. **Facteur de puissance $\neq$ $\cos\varphi_1$** : en présence d'harmoniques, $FP = \cos\varphi_1 / \sqrt{1 + THD^2} < \cos\varphi_1$. Confondre les deux est une erreur fréquente.

5. **Puissance active et harmoniques** : si la tension réseau est sinusoïdale, seul le fondamental du courant contribue à la puissance active $P$. Les harmoniques contribuent uniquement à $D$ (puissance déformante).

6. **Ondulation ≠ THD** : l'ondulation de courant est une grandeur crête-à-crête dans le domaine temporel, tandis que le THD est un indicateur fréquentiel. Ne pas les confondre dans les conclusions.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T01 (Électrocinétique)** : la compensation réactive par condensateur (T01 B3-B4) réduit $Q$ mais pas $D$. Pour réduire $D$, il faut des filtres actifs ou la MLI.
- **T03 (Impédances complexes)** : le facteur de déplacement $\cos\varphi_1$ est l'argument de l'impédance au fondamental. Les filtres LC se dimensionnent par $\omega_0 = 1/\sqrt{LC}$.
- **T09 (Convertisseurs DC/DC)** : le rapport cyclique $\alpha$ et la fréquence de découpage $f$ déterminent l'ondulation de courant, qui se traduit en harmoniques sur le bus DC.
- **T06 (MAS)** : les harmoniques de courant créent des harmoniques de couple (couple parasite) dans la MAS, réduisant son rendement et créant des vibrations.
- **T08 (Qualité de l'énergie)** : le THD est l'indicateur principal de la qualité de l'énergie électrique ; la norme IEC 61000-2-2 fixe les limites pour le raccordement au réseau.
