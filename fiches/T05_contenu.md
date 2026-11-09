# T05 — Phénomènes thermiques

## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

| Grandeur / Loi | Formule | Unité |
|----------------|---------|-------|
| Couple thermique équivalent (cycle) | $C_{th}^2 = \dfrac{\sum_{i} C_{mi}^2 \cdot \Delta t_i}{T}$ | N·m |
| Puissance dissipée effet Joule | $P_J = R \cdot I^2 = U \cdot I$ | W |
| Flux thermique (conduction) | $\Phi = \lambda \cdot S \cdot \dfrac{\Delta T}{e}$ | W |
| Résistance thermique (conduction) | $R_{th} = \dfrac{e}{\lambda \cdot S}$ | K/W |
| Résistance thermique (convection) | $R_{th,conv} = \dfrac{1}{h \cdot S}$ | K/W |
| Relation fondamentale thermique | $\Delta T = R_{th} \cdot P$ | K |
| Capacité thermique | $C_{th} = m \cdot c_p$ | J/K |
| Constante de temps thermique | $\tau_{th} = R_{th} \cdot C_{th,cap}$ | s |
| Température jonction composant | $T_j = T_{amb} + R_{th,ja} \cdot P_{dissipée}$ | °C |
| Transmetteur 4-20 mA (linéaire) | $I_{out} = 4 + 16 \cdot \dfrac{T - T_{min}}{T_{max} - T_{min}}$ | mA |
| Effet Seebeck (thermocouple) | $e_{AB} = k_{Seebeck} \cdot (T_1 - T_2)$ | V |
| PT100 (approximation linéaire) | $R(T) = 100 \cdot (1 + \alpha \cdot T)$ avec $\alpha \approx 3{,}85 \times 10^{-3}\,\text{K}^{-1}$ | Ω |

### 1.1 Convection et rayonnement

*(complément du référentiel, 2026-11-10 — notion hors sujets 2013–2026 sauf mention)*

**Flux échangé par convection (loi de Newton) :**
$$\Phi_{conv} = h \, S \, (T_s - T_a)$$
- Valable si le coefficient h est supposé uniforme sur la surface S

**Flux échangé par rayonnement (loi de Stefan-Boltzmann) :**
$$\Phi_{ray} = \varepsilon \, \sigma \, S \, (T_s^4 - T_a^4)$$
- Valable uniquement avec des températures exprimées en kelvins

**Coefficient d'échange radiatif linéarisé :**
$$h_r \approx 4 \, \varepsilon \, \sigma \, T_m^3$$
- Valable si l'écart entre T_s et T_a est faible devant la température moyenne T_m

---

## 2. QUESTIONS TYPES

### Q1 — Couple thermique équivalent (2019, Sujet IE)
**Source :** E2_Sujet_2019  
**Énoncé :** Un moteur subit un cycle de travail de période $T = 2048\,\text{s}$. Les couples et durées sont donnés par un tableau. Calculer le couple thermique équivalent $C_{th}$.  
**Corrigé :**  
$C_{th}^2 = \dfrac{\sum_{i} C_{mi}^2 \cdot \Delta t_i}{T}$  
Données du cycle (phases 1 et 2 principales) :  
- Phase 1 : $F_{e1} = 14{,}9\,\text{kN}$, $\Delta t_1 = 42\,\text{s}$  
- Phase 2 : $F_{e2} = 9{,}2\,\text{kN}$, $\Delta t_2 = 51\,\text{s}$  
- Phases 3 à 18 : $\sum C_{mi}^2 \cdot \Delta t_i = 558 \times 10^6\,\text{N}^2\text{m}^2\text{s}$  

$C_{th} = \sqrt{\dfrac{C_{m1}^2 \cdot \Delta t_1 + C_{m2}^2 \cdot \Delta t_2 + 558\times10^6}{T}}$

---

### Q2 — Surveillance par thermocouple type J (2024, Extracteur d'air, D1)
**Source :** E2_Disciplinaire_IE_2024, partie D  
**Énoncé :** Un thermocouple de type J est utilisé pour surveiller la température du moteur. Donner sa plage de mesure et sa tolérance.  
**Corrigé :**  
- Type J (Fer / Constantan) : plage $-30°\text{C}$ à $+700°\text{C}$  
- Tolérance classe 1 : $\pm 1{,}5°\text{C}$ ou $\pm 0{,}4\%$ de la valeur mesurée  
- Sensibilité : environ $51\,\mu\text{V/K}$  
Le principe est l'effet Seebeck : $e_{AB} = k_S \cdot (T_{mesure} - T_{ref})$

---

### Q3 — Transmetteur 4-20 mA température (2024, Extracteur d'air, partie E)
**Source :** E2_Disciplinaire_IE_2024, partie E  
**Énoncé :** Un transmetteur convertit la température en courant 4-20 mA. Plage : $T_{min} = -20°\text{C}$ correspond à $4\,\text{mA}$, $T_{max} = +200°\text{C}$ correspond à $20\,\text{mA}$. Calculer le courant pour une température de $120°\text{C}$.  
**Corrigé :** Relation linéaire :  
$I_{out} = 4 + 16 \cdot \dfrac{T - (-20)}{200 - (-20)} = 4 + 16 \cdot \dfrac{T + 20}{220}$  
Pour $T = 120°\text{C}$ : $I_{out} = 4 + 16 \cdot \dfrac{140}{220} \approx 4 + 10{,}2 = 14{,}2\,\text{mA}$

---

### Q4 — Surveillance condensats réseau vapeur (2022, Cogénération)
**Source :** E2_Disciplinaire_IE_2022, document technique partie B  
**Énoncé :** Trois sondes PT100 ($T_1$, $T_2$, $T_3$) surveillent la canalisation vapeur. Écrire l'algorithme de surveillance.  
**Corrigé :**  
```
SI (T1 - T2 < 12°C) ET (T3 < 160°C) ALORS
    État = Fonctionnement correct
SINON
    État = Alarme / Défaut
FIN SI
```
La différence $T_1 - T_2 < 12°\text{C}$ détecte un retour d'eau trop froid (condensat). La limite $T_3 < 160°\text{C}$ surveille la vapeur en fin de circuit.

---

### Q5 — Table de vapeur saturée (2022, Cogénération, DT B1)
**Source :** E2_Disciplinaire_IE_2022, document technique B1  
**Énoncé :** La chaudière fonctionne à une pression de $12\,\text{bars}$. Lire la température de vaporisation dans la table de vapeur saturée fournie.  
**Corrigé :** D'après la table de vapeur saturée :  
- $P_s = 12\,\text{bars}$ → $T_{vap} = 187{,}96°\text{C}$  
La table est fournie en DT (de 8 à 19 bars). Il faut savoir interpoler linéairement si la pression demandée n'est pas exactement dans la table.

---

### Q6 — Module Peltier et effet Seebeck (2022, Cogénération)
**Source :** E2_Disciplinaire_IE_2022  
**Énoncé :** Un module Peltier est utilisé pour convertir un différentiel de température en tension. Expliquer le principe.  
**Corrigé :** L'effet Seebeck (inverse de l'effet Peltier) : lorsque deux métaux différents A et B forment une jonction à deux températures $T_1 \neq T_2$, une force électromotrice $e$ apparaît :  
$e = k_S \cdot (T_1 - T_2)$  
où $k_S$ est le coefficient de Seebeck du couple de matériaux (en V/K). Ce principe est identique à celui d'un thermocouple.

---

## 3. ATTENTES DU JURY

**Rapport jury 2022 (résumé) :**  
Le jury note que les candidats traitent correctement les questions de surveillance par capteurs (PT100, DS1820) mais peinent à lire et interpoler les tables thermodynamiques (table de vapeur saturée). Il est attendu de savoir utiliser une documentation technique fournie.

**Rapport jury 2024 (résumé) :**  
La partie D (capteurs de température) a été globalement bien traitée. Le jury apprécie les candidats qui précisent la plage de mesure et la tolérance du capteur choisi, et qui vérifient la cohérence entre la grandeur mesurée et la plage du capteur.

**Rapport jury 2019 (résumé) :**  
Le calcul du couple thermique équivalent ($C_{th}$) est bien connu en principe, mais les candidats font des erreurs dans la sommation : oublier certaines phases du cycle ou confondre $C_{th}^2$ et $C_{th}$.

**Résumé des attentes :**
- Connaître le principe des capteurs de température (thermocouple, PT100, DS1820)
- Savoir lire et interpoler une table de vapeur saturée
- Savoir calculer le couple thermique équivalent sur un cycle
- Savoir convertir une grandeur physique en courant 4-20 mA (relation linéaire)
- Écrire un algorithme de surveillance avec conditions sur les températures

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur | Source |
|----------|--------|--------|
| Thermocouple type J plage | $-30°\text{C}$ à $+700°\text{C}$ | 2024 D1 |
| Thermocouple type J tolérance | $\pm 1{,}5°\text{C}$ (classe 1) | 2024 D1 |
| Thermocouple type K plage | $-200°\text{C}$ à $+1260°\text{C}$ | programme |
| PT100 résistance à 0°C | $R_0 = 100\,\Omega$ | — |
| PT100 coefficient $\alpha$ | $3{,}85 \times 10^{-3}\,\text{K}^{-1}$ | — |
| Transmetteur 2024 plage | $-20°\text{C}$ à $+200°\text{C}$ | 2024 E |
| Vapeur saturée à 12 bars | $T_{vap} = 187{,}96°\text{C}$ | 2022 DT B1 |
| Vapeur saturée à 8 bars | $T_{vap} \approx 170°\text{C}$ | 2022 DT B1 |
| Vapeur saturée à 19 bars | $T_{vap} \approx 210°\text{C}$ | 2022 DT B1 |
| Couple thermique cycle 2019 | $T = 2048\,\text{s}$, $\sum_{3..18} = 558\times10^6$ | 2019 |
| DS1820 plage | $-55°\text{C}$ à $+125°\text{C}$, bus 1-Wire | 2022 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **Couple thermique : $C_{th}^2$ ≠ $C_{th}$** : la formule donne le carré du couple thermique. Il faut prendre la racine carrée à la fin. Oublier ce pas final est l'erreur la plus fréquente.

2. **Interpolation dans les tables** : si la pression (ou température) n'est pas exactement dans la table de vapeur, il faut interpoler linéairement entre les deux valeurs encadrantes. Ne pas arrondir à la valeur la plus proche sans calcul.

3. **Transmetteur 4-20 mA** : la relation est linéaire entre ($T_{min}$, 4 mA) et ($T_{max}$, 20 mA). Attention à la plage : $\Delta I = 16\,\text{mA}$ correspond à $\Delta T = T_{max} - T_{min}$ (pas à 20 mA).

4. **Thermocouple : jonction froide** : la tension délivrée par un thermocouple est proportionnelle à la différence $T_{mesure} - T_{ref}$. Si la jonction froide n'est pas à 0°C, il faut appliquer une compensation.

5. **PT100 vs Thermocouple** : PT100 est un capteur résistif (mesure par pont de Wheatstone), adapté à $-200°\text{C}$ à $+850°\text{C}$ avec bonne précision. Le thermocouple a une plage plus étendue mais une sensibilité plus faible.

6. **Confusion Peltier/Seebeck** : l'effet Peltier (courant → différence de température) est l'inverse de l'effet Seebeck (différence de température → tension). Le thermocouple exploite l'effet Seebeck.

7. **Rayonnement en degrés Celsius** : appliquer la loi de Stefan-Boltzmann avec des températures en degrés Celsius. Les températures doivent être en kelvins, sinon le flux calculé n'a aucun sens.

8. **Convection naturelle ou forcée** : garder le même coefficient h avec et sans ventilateur. Le coefficient passe d'environ 5 à 25 W·m⁻²·K⁻¹ en convection naturelle à 25 à 250 en convection forcée.

9. **Échanges en parallèle** : additionner les résistances thermiques de convection et de rayonnement. Ces deux échanges partent de la même surface et se font en parallèle : ce sont les conductances $hS$ et $h_r S$ qui s'additionnent.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T01 (Électrocinétique)** : la puissance dissipée par effet Joule $P = R \cdot I^2$ est la source de chaleur dans les modèles thermiques des câbles, moteurs et composants électroniques.
- **T06 (MAS)** : les pertes Joule rotoriques $P_{Jr} = 3 R_r' \cdot I_r'^2 = g \cdot P_t$ (lien glissement/pertes) constituent la source thermique principale de la machine.
- **T14 (Automatismes, supervision)** : la surveillance des températures par PT100 ou thermocouple s'intègre dans les systèmes de supervision (SCADA, automate) avec des seuils d'alarme et des actions correctives.
- **T09 (Convertisseurs)** : les composants de puissance (IGBT, diodes) ont des limites thermiques ($T_{j,max}$) qui conditionnent le courant maximal admissible et le dimensionnement des dissipateurs.
- **T11 (Énergies renouvelables)** : la cogénération (2022) couple production d'électricité et récupération de chaleur ; la thermodynamique de la vapeur est centrale dans ce sujet.
