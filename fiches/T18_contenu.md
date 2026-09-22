# T18 — Circuits électroniques, composants (diode, transistor)
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

### 1.1 La diode
La diode est un composant à deux bornes (anode A, cathode K) à comportement non-linéaire.

**Caractéristique idéale (modèle idéal) :**
- Passante si $V_{AK} > 0$ : $V_{AK} = 0$ V, courant $i \geq 0$
- Bloquée si $V_{AK} < 0$ : $i = 0$

**Modèle avec seuil :**
$$V_{AK} = V_{seuil} \approx 0{,}6 \text{ V (Si)} \quad \text{ou} \quad 0{,}3 \text{ V (Ge)}$$

**Diode de protection (retrouvée dans les sources — 2022, 2019) :** la diode $D_1$ protège l'entrée analogique d'un CAN en écrêtant la tension à $V_{seuil}$ :
$$V_{entrée\_CAN} \leq V_{ref} + V_{seuil}$$

**LED (diode électroluminescente) :** transformation de l'électricité en lumière. Durée de vie $\geq 25\,000$ h. Efficacité jusqu'à 90 lm/W (source : E1_Sujet_2013).

### 1.2 Droite de charge et point de fonctionnement
Pour un montage diode + résistance $R$ alimenté par $E$ :
$$E = R \cdot i + V_{AK}$$
Droite de charge : pente $= -1/R$, ordonnée à l'origine $E/R$ (sur l'axe $i$) et $E$ (sur l'axe $V_{AK}$).

Le **point de fonctionnement** $Q$ est l'intersection de la droite de charge avec la caractéristique $i(V_{AK})$ de la diode.

### 1.3 Transistor bipolaire (BJT)
Trois régimes :
| Régime | Condition | $I_C$ |
|--------|-----------|-------|
| Bloqué | $V_{BE} < 0{,}6$ V | $\approx 0$ |
| Actif | $V_{BE} \approx 0{,}6$ V, $V_{CE} > V_{CE(sat)}$ | $\beta \cdot I_B$ |
| Saturé | $V_{BE} \approx 0{,}6$ V, $V_{CE} \approx V_{CE(sat)}$ | limité par le circuit |

Relation en régime actif : $I_C = \beta \cdot I_B$ avec $\beta$ (gain statique) $\approx 50$–$500$.

### 1.4 Transistor MOSFET et IGBT (interrupteurs de puissance)
Les convertisseurs statiques (hacheurs, onduleurs) des sujets CAPET utilisent systématiquement des **transistors commandés** :

**MOSFET :** commandé en tension par $V_{GS}$. Utilisé à haute fréquence de commutation.

**IGBT :** commandé en tension par $V_{GE}$. Associé à une diode de roue libre anti-parallèle. Utilisé dans les variateurs de vitesse et onduleurs PV (source : E1_Sujet_2013 — onduleur photovoltaïque).

**Transistor $Q_1$ dans un hacheur abaisseur (sources : E2_Disciplinaire_IE_2025, E1_Sujet_2025) :**
- Pour $t \in [0\,;\,\alpha T]$ : $Q_1$ fermé, diode $D_1$ bloquée, $v_{Q1} = 0$, $v_{D1} = -V_{DC}$
- Pour $t \in [\alpha T\,;\,T]$ : $Q_1$ ouvert, diode $D_1$ passante (roue libre), $v_{Q1} = V_{DC}$

Tension moyenne de sortie :
$$\langle V_{sortie} \rangle = \alpha \cdot V_{DC}$$

### 1.5 Thyristor et Triac
**Thyristor (SCR) :** interrupteur semi-commandé — amorçage sur impulsion de gâchette, blocage au passage par zéro du courant.

**Triac :** thyristor bidirectionnel. Utilisé pour la commande de charges alternatives.

**Angle d'amorçage $\alpha$ :** la tension moyenne de sortie d'un montage à thyristors dépend de $\alpha$ :
$$V_{moy} = V_{m} \cdot \frac{1 + \cos\alpha}{\pi} \quad \text{(pont P1 demi-alternance)}$$

### 1.6 Redresseur à diodes — pont P3 (source : E1_Sujet_2026)
Pont redresseur triphasé PD3 (pont de Graëtz triphasé) associé à un transformateur triphasé et une charge fortement inductive (modélisée par source de courant).

Tension continue moyenne :
$$V_{DC} = \frac{3\sqrt{3}}{\pi} \cdot V_{max,phase} \approx 2{,}34 \cdot V_{eff,simple}$$

### 1.7 Commutation — notion de rapport cyclique
Dans un hacheur de rapport cyclique $\alpha$ ($0 \leq \alpha \leq 1$), la période $T$ est divisée en deux intervalles :
- $[0\,;\,\alpha T]$ : interrupteur fermé
- $[\alpha T\,;\,T]$ : interrupteur ouvert

L'ondulation de courant dans l'inductance $L$ :
$$\Delta i_L = \frac{V_{DC} \cdot \alpha \cdot (1-\alpha) \cdot T}{L}$$
maximale pour $\alpha = 0{,}5$.

---

## 2. QUESTIONS TYPES (max 6)

1. **(2022, Q27)** La diode $D_1$ est nécessaire pour protéger en tension l'entrée analogique du CAN. Expliquer le principe de cette protection. *(Réponse attendue : quand $V_{entrée} > V_{ref} + V_{seuil}$, la diode conduit et écrête la tension.)*

2. **(2025, Q27)** Pour $t \in [0\,;\,\alpha T]$ puis pour $t \in [\alpha T\,;\,T]$, en utilisant les lois de Kirchhoff, déterminer l'expression littérale de l'intensité du courant $i_{L1}$ sur les deux intervalles.

3. **(2025, Q28)** Dessiner l'allure temporelle de $i_{L1}$.

4. **(2023, Q C6)** Déterminer la valeur du rapport cyclique qui correspond à une ondulation $\Delta i_{Bakus}$ maximale. Déterminer la valeur de l'inductance minimale à installer pour respecter l'exigence d'ondulation maximale du courant.

5. **(type CAPET)** Sur le schéma d'un hacheur abaisseur avec transistor $Q_1$ et diode de roue libre $D_1$, identifier les états de $Q_1$ et $D_1$ pour chaque intervalle, puis calculer la tension moyenne de sortie.

6. **(2013, Q48)** Donner le type de commande des transistors de puissance d'un onduleur photovoltaïque et justifier le choix du modèle de l'onduleur.

---

## 3. ATTENTES DU JURY

- **Maîtrise des lois fondamentales** : le jury 2024 et 2025 déplore le manque de maîtrise de la loi des nœuds, la loi des mailles et la loi d'Ohm pour les composants élémentaires.
- **Justification des calculs** : les résultats donnés directement sans démarche ne sont pas valorisés.
- **Schémas électriques corrects** : dessiner les schémas équivalents pour chaque intervalle de commutation avec les composants dans leur état (ouvert/fermé).
- **Utilisation des conditions initiales nulles** et de la transformée de Laplace pour l'étude des régimes transitoires des circuits $RL$.
- Le jury attend que le candidat sache distinguer les trois zones de fonctionnement d'un transistor (bloqué, actif, saturé) et les associer à une application concrète.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique |
|----------|---------------|
| Tension de seuil diode Si | $V_{seuil} = 0{,}6$ V |
| Tension de seuil diode Ge | $V_{seuil} = 0{,}3$ V |
| Bus continu hacheur | $V_{DC} = 750$ V (système traction 2019) |
| Bus continu hacheur | $V_{DC} = 48$ V (robot Bakus 2023) |
| Fréquence de commutation MLI | $f_p = 6$ kHz (variateur 2024) |
| Inductance filtre | $L \sim $ quelques mH |
| $\beta$ transistor bipolaire | 50 à 500 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **Confondre diode passante et bloquée** selon le signe de $V_{AK}$ — erreur fréquente de signe.
- **Oublier la diode de roue libre** : sans $D_1$, tension aux bornes du transistor $Q_1$ diverge à l'ouverture (surtension destructrice).
- **Rapport cyclique et tension moyenne** : $\langle V \rangle = \alpha \cdot V_{DC}$ n'est valable qu'en conduction continue.
- **Ondulation maximale à $\alpha = 0{,}5$** et non à $\alpha = 1$ — erreur classique.
- **Distinction MOSFET / IGBT** : les deux sont commandés en tension sur la grille mais l'IGBT supporte des tensions plus élevées ; le MOSFET est plus rapide.
- **Saturation BJT vs MOSFET** : pour un BJT en saturation, $V_{CE} \approx 0{,}2$ V et la relation $I_C = \beta I_B$ ne s'applique plus.
- **Ne pas confondre** la caractéristique statique $i(V_{AK})$ de la diode (courbe exponentielle) et la droite de charge (relation du circuit extérieur).

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T17 — Convertisseurs statiques (hacheur, onduleur)** : les transistors $Q_1$ et diodes $D_1$ sont les briques de base de tous les convertisseurs étudiés.
- **T19 — AOP** : le comparateur à base d'AOP commande souvent la grille d'un transistor (signal de commande PWM).
- **T21 — Fonctions de transfert / Bode** : le modèle moyen du hacheur (linéarisé autour d'un point de repos) donne la fonction de transfert $\delta V_{DC}(p) / \delta\alpha(p)$ — source : E2_Disciplinaire_IE_2025.
- **T09 — Machines électriques** : l'IGBT alimente le moteur via l'onduleur ; la diode de roue libre protège lors de la commutation.
- **T06 — CAN/CNA** : la diode de protection des entrées analogiques du CAN est une application directe (source : E2_Disciplinaire_IE_2022).
