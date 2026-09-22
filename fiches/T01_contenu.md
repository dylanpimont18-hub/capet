# T01 — Grandeurs électriques, électrocinétique

## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

| Grandeur / Loi | Formule | Unité |
|----------------|---------|-------|
| Loi d'Ohm (résistif) | $u = R \cdot i$ | V, Ω, A |
| Loi d'Ohm généralisée | $u = R \cdot i + e$ | V |
| Loi des mailles | $\sum e_k = \sum R_k \cdot i_k$ | V |
| Loi des nœuds | $\sum i_{entrants} = \sum i_{sortants}$ | A |
| Diviseur de tension | $V_s = V_e \cdot \dfrac{R_B}{R_A + R_B}$ | V |
| Diviseur de courant | $I_1 = I \cdot \dfrac{R_2}{R_1 + R_2}$ | A |
| Valeur efficace (sinusoïdal) | $V_{eff} = \dfrac{V_{max}}{\sqrt{2}}$ | V |
| Valeur efficace (générale) | $V_{eff} = \sqrt{\dfrac{1}{T}\int_0^T v^2(t)\,dt}$ | V |
| Puissance active (monophasé) | $P = V \cdot I \cdot \cos\varphi$ | W |
| Puissance active (triphasé) | $P = 3 \cdot V_s \cdot I_s \cdot \cos\varphi$ | W |
| Puissance réactive | $Q = V \cdot I \cdot \sin\varphi$ | VAR |
| Puissance apparente | $S = V \cdot I = \sqrt{P^2 + Q^2}$ | VA |
| Facteur de puissance | $\cos\varphi = P / S$ | — |
| Condensateur (circuit RC) | $\tau = R \cdot C$ | s |
| Inductance (circuit RL) | $\tau = L / R$ | s |
| Énergie condensateur | $E_C = \dfrac{1}{2} C \cdot V^2$ | J |
| Énergie inductance | $E_L = \dfrac{1}{2} L \cdot I^2$ | J |
| Condensateur compensation réactive | $C = \dfrac{Q_{abs}}{3 \cdot \omega \cdot V_n^2}$ | F |
| Glissement MAS | $g = \dfrac{N_s - N}{N_s}$ | — |
| Vitesse de synchronisme | $N_s = \dfrac{60 f}{p}$ | tr/min |

---

## 2. QUESTIONS TYPES

### Q1 — Loi des mailles avec ALI (2024, Extracteur d'air, E1/E2 partie A)
**Source :** E2_Disciplinaire_IE_2024, partie A, question E1  
**Énoncé :** Le montage comporte un ALI parfait. Écrire la relation liant $e_{AB}$ aux tensions du circuit.  
**Corrigé :** En régime linéaire d'un ALI parfait, la différence des entrées est nulle. La loi des mailles sur la boucle de retour donne :  
$e_{AB} = V_{R_2}$  
(La tension $e_{AB}$ se retrouve intégralement aux bornes de $R_2$, la chute sur $R_1$ étant nulle car $i_{+} = i_{-} = 0$.)

---

### Q2 — Loi des nœuds (2024, Extracteur d'air, E2 partie A)
**Source :** E2_Disciplinaire_IE_2024, partie A, question E6  
**Énoncé :** Appliquer la loi des nœuds au nœud de sortie du montage amplificateur.  
**Corrigé :** La loi des nœuds donne $I_2 = I_2' + I_+$. L'entrée d'un ALI parfait ne consomme pas de courant ($I_+ = 0$), donc :  
$I_2 = I_2'$

---

### Q3 — Diviseur de tension (2023, Robot Bakus, F2)
**Source :** E2_Disciplinaire_IE_2023, bloc fonctionnel F2  
**Énoncé :** Le circuit F2 est un pont diviseur de tension. Exprimer $V_{s1}$ en fonction de $V_{e1}$, $R_A$, $R_B$.  
**Corrigé :** $V_{s1} = V_{e1} \cdot \dfrac{R_B}{R_A + R_B}$  
Application numérique : pour $R_A = 9R_B$, on obtient $V_{s1} = V_{e1}/10$, soit un rapport d'atténuation de 10.

---

### Q4 — Calcul de la constante de temps $\tau$ (2023, Robot Bakus)
**Source :** E2_Disciplinaire_IE_2023, modèle Thévenin batterie  
**Énoncé :** La batterie est modélisée par une force électromotrice $E_{Li}$ en série avec une résistance $R_{Li}$ et une inductance $L$. Calculer la constante de temps du circuit.  
**Corrigé :** Le circuit RL a pour constante de temps :  
$\tau = \dfrac{L}{R_{Li}}$

---

### Q5 — Condensateur de compensation réactive (2024, Extracteur d'air, B3-B4)
**Source :** E2_Disciplinaire_IE_2024, partie B  
**Énoncé :** La MAS absorbe une puissance réactive $Q_{abs}$. Calculer la valeur du condensateur de compensation à placer en parallèle sur le réseau triphasé ($V_n$, $f = 50\,\text{Hz}$).  
**Corrigé :** Le condensateur doit fournir une puissance réactive égale à $Q_{abs}$ :  
$Q_C = 3 \cdot \omega \cdot C \cdot V_n^2 \Rightarrow C = \dfrac{Q_{abs}}{3 \cdot \omega \cdot V_n^2}$  
Application numérique : $C \approx 0{,}016\,\text{F}$.

---

### Q6 — Puissance triphasée et facteur de puissance MAS (2024, Extracteur d'air, A5)
**Source :** E2_Disciplinaire_IE_2024, partie A  
**Énoncé :** La MAS est alimentée en triphasé ($V_s$ tension de phase, $I_s$ courant de ligne). Exprimer la puissance active absorbée.  
**Corrigé :**  
$P_a = 3 \cdot V_s \cdot I_s \cdot \cos\varphi$  
où $\cos\varphi$ est le facteur de puissance lu sur le modèle monophasé équivalent.

---

## 3. ATTENTES DU JURY

**Rapport jury 2024 (citation directe) :**  
> *"Le jury a constaté le manque de maîtrise des formules de base sur les réseaux triphasés, le régime sinusoïdal et les relations d'électrocinétique telles que la loi des mailles, la loi des nœuds ou encore la loi d'Ohm."*

**Rapport jury 2025 (citation directe) :**  
> *"De nombreux candidats ne maîtrisent pas les lois basiques de l'électricité (la loi des nœuds, la loi des mailles, les calculs de puissance ou encore la loi d'Ohm)."*

**Rapport jury 2021 :**  
> *"Il n'est pas concevable à ce niveau de concours que les candidats ne soient pas capables de résoudre une équation du premier degré. De même, il est décevant de constater que certains d'entre eux confondent les notions de puissance en régime continu et alternatif."*

**Résumé des attentes :**
- Savoir poser et résoudre une loi des mailles ou des nœuds sans erreur de signe
- Distinguer puissance en régime continu ($P = U \cdot I$) et alternatif ($P = U \cdot I \cdot \cos\varphi$)
- Calculer une valeur efficace, une constante de temps, un diviseur de tension
- Justifier chaque étape de calcul et encadrer les résultats

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique | Source |
|----------|----------------|--------|
| Tension réseau monophasé | $230\,\text{V}$ efficace | — |
| Tension réseau triphasé (phase) | $230\,\text{V}$, ligne-ligne $400\,\text{V}$ | — |
| Fréquence réseau | $f = 50\,\text{Hz}$ | — |
| $\omega$ réseau | $\omega = 2\pi \times 50 \approx 314\,\text{rad/s}$ | — |
| Condensateur compensation 2024 | $C \approx 0{,}016\,\text{F} = 16\,\text{mF}$ | 2024 B3-B4 |
| Vitesse synchronisme MAS 4 pôles | $N_s = 1500\,\text{tr/min}$ (à 50 Hz) | 2024 |
| Glissement nominal MAS | $g \approx 2{,}5\%$ à $5\%$ | — |
| Rapport diviseur de tension Bakus | $V_{s1}/V_{e1} = 1/10$ | 2023 F2 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Signe dans la loi des mailles** : oublier de changer le signe d'une tension selon le sens de parcours de la maille. Toujours définir un sens de parcours avant d'écrire.

2. **Puissance continue vs alternatif** : $P = U \cdot I$ (continu) ≠ $P = U_{eff} \cdot I_{eff} \cdot \cos\varphi$ (alternatif). Confusion fréquente signalée par le jury.

3. **Valeur efficace vs valeur de crête** : $V_{eff} = V_{max}/\sqrt{2}$ seulement pour un signal sinusoïdal pur. Pour un signal déformé, utiliser la définition intégrale.

4. **ALI parfait** : oublier que $i_+ = i_- = 0$ et $v_+ = v_-$ en régime linéaire, ce qui simplifie la loi des nœuds au nœud de sortie.

5. **Puissance triphasée** : ne pas multiplier par 3 ou confondre tension de phase $V_s$ et tension de ligne $V_L = \sqrt{3} \cdot V_s$.

6. **Condensateur de compensation** : la formule $C = Q/(3\omega V_n^2)$ suppose que $V_n$ est la tension de phase, pas la tension de ligne.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T03 (Impédances complexes)** : la loi d'Ohm généralisée en sinusoïdal devient $\underline{U} = \underline{Z} \cdot \underline{I}$. Les lois de Kirchhoff s'appliquent identiquement en complexe.
- **T04 (Harmoniques, THD)** : les lois de Kirchhoff s'appliquent par superposition à chaque harmonique. Le calcul de puissance réactive conduit au condensateur de compensation (T01 B3-B4).
- **T06 (Machine asynchrone)** : le modèle monophasé équivalent de la MAS repose sur la loi des mailles et la loi d'Ohm complexe ($\underline{I}_r' = \underline{V}_s / (j L_f \omega_s + R_r'/g)$).
- **T09 (Convertisseurs DC/DC)** : la loi des mailles en régime de conduction continue donne la relation $V_{DC} = E_b / (1-\alpha)$ pour un hacheur élévateur.
- **T05 (Thermique)** : la puissance dissipée par effet Joule ($P = R \cdot I^2$) est la source thermique dans les modèles thermiques des composants.
