# T11 — Variation de vitesse / Commande des machines

> **Fréquence :** 22/22 sujets · **Intensité moyenne :** 🟠 Important
> Fil conducteur dans les sujets industriels (2020 Exotec, 2022 Banc essai) et transport (2017 Métro, 2019 Transport câble). Inclut les variateurs, hacheurs, onduleurs et commande MAS.

---

## Notions clés

### Machine asynchrone (MAS) — Rappels essentiels

| Formule | Description | Mémoire |
|---|---|:---:|
| $N_s = 60 \cdot f/p$ | Vitesse synchrone (tr/min) | ❌ |
| $g = (N_s - N) / N_s$ | Glissement | ❌ |
| $I_n = P_u / (\eta \cdot \sqrt{3} \cdot U \cdot \cos\varphi)$ | Courant nominal | ❌ |
| $P = C \cdot \omega$ | Puissance mécanique | ❌ |
| $\omega = 2\pi \cdot N/60$ | Conversion tr/min → rad/s | ❌ |

> p = nombre de paires de pôles. En France f = 50 Hz.
> Exemple : moteur 4 pôles (p=2) → $N_s = 60 \cdot 50/2 = 1500$ tr/min

### Variateur de vitesse (onduleur de tension)

Structure : Réseau → **Redresseur** → Bus continu → **Onduleur MLI** → Moteur

**Dimensionnement du variateur :**
- Courant variateur $I_{n,var} \geq I_{n,moteur}$ (condition minimale)
- Seuil thermique $I_{th}$ : réglé à $I_{n,moteur}$ (protection thermique)
- Tension variateur adaptée à la tension réseau (400 V triphasé → variateur 400 V)

**Commande scalaire (V/f constant) :**
- Principe : maintenir V/f = constante pour conserver le flux
- Avantage : simple, robuste
- Limite : peu précis, pas adapté aux grandes plages de vitesse

**Commande vectorielle (FOC) :**
- Découplage flux/couple par orientation du repère selon le flux rotorique
- Utilisée pour les applications à haute dynamique (machines-outils, traction)

### Hacheur dévolteur (Buck — Abaisseur)

```
   E ──┬── Interrupteur K ──┬── L ──┬── Charge
       │                   │       │
       │              Diode │       C
       │                   │       │
      GND ─────────────────┴───────┘
```

- Tension moyenne sortie : $$V_s = \alpha \cdot E$$
- Rapport cyclique : $\alpha = V_s / E$ (0 < α < 1)
- Courant ondulation : $\Delta I_L = (E - V_s) \cdot \alpha \cdot T / L$

### Hacheur survolteur (Boost — Élévateur)

- Tension sortie : $$V_{DC} = \frac{E_b}{1 - \alpha}$$
- Rapport cyclique : $\alpha = 1 - E_b / V_{DC}$
- Conservation puissance : $E_b \cdot I_b = V_{DC} \cdot I_S$

### Hacheur 4 quadrants (Pont en H)

- Tension moyenne : $$\langle u_f \rangle = E \cdot (2\alpha - 1)$$
- Permet le fonctionnement en mode moteur et frein régénératif

---

## Redresseurs — Rappel

| Type | Formule tension moyenne | Usage |
|---|---|---|
| Monophasé PD2 (pont diodes) | $V_{moy} = 2 \cdot V_{max}/\pi \approx 0{,}9 \cdot V_{eff}$ | Alimentation DC simple |
| Triphasé PD3 (pont diodes) | $V_{moy} \approx 1{,}35 \cdot V_{eff}$ (composée) | Bus continu variateur |
| Triphasé commandé (thyristors) | $V_{moy} = 1{,}35 \cdot V_{eff} \cdot \cos\alpha$ | Traction, MCC |

---

## Types de questions au concours

| Type | Exemple | Formule |
|---|---|---|
| Dimensionner un variateur | "Choisir le variateur pour un moteur de 22 kW" | $I_{var} \geq I_{n,moteur}$ |
| Rapport cyclique d'un hacheur | "Calculer α pour V_s = 48 V avec E = 72 V" | $\alpha = V_s/E = 48/72$ |
| Vitesse synchrone MAS | "Calculer N_s pour un moteur 4 pôles" | $N_s = 60 \cdot f/p$ |
| Glissement nominal | "Calculer g si N = 1460 tr/min, N_s = 1500" | $g = (1500 - 1460)/1500$ |
| Réglage Ith variateur | "Régler le seuil thermique" | $I_{th} = I_{n,moteur}$ |
| Choix commande V/f vs vectorielle | "Justifier le choix de commande" | Argumenter sur précision, dynamique |

---

## Pièges courants

1. **Confondre p (paires de pôles) et nombre de pôles** : un moteur "4 pôles" a p = 2 paires → $N_s = 60 \cdot 50/2 = 1500$ tr/min (et non $60 \cdot 50/4 = 750$).
2. **Oublier le rendement du moteur** dans le calcul du courant absorbé : $I = P_{méca}/(\eta \cdot \sqrt{3} \cdot U \cdot \cos\varphi)$.
3. **Appliquer $V_s = \alpha \cdot E$** pour un Boost (faux) → $V_s = E/(1-\alpha)$.
4. **Confondre $I_n$ variateur et $I_n$ moteur** : le courant variateur doit être $\geq$ courant moteur.
5. **Ne pas donner les unités** : $N_s$ en tr/min, $\omega$ en rad/s, ne pas mélanger.

---

## Calibrage de la réponse attendue

**Question type :** "Un moteur asynchrone 4 pôles, 22 kW, rendement 92 %, cosφ = 0,85, 400 V triphasé, tourne à 1460 tr/min en charge. Calculer le glissement nominal."

**Réponse attendue :**
- $N_s = 60 \cdot 50/2 = 1500$ tr/min
- $g = (1500 - 1460) / 1500 = 40/1500 =$ **0,0267 soit 2,67 %**
- Commentaire : "Le glissement nominal est faible (< 5 %), le moteur fonctionne proche de la vitesse synchrone, ce qui est normal en charge nominale."

---

## Liens avec d'autres thèmes

- → **T02 Puissance AC** : consommation du variateur + moteur, facteur de puissance
- → **T21 Modélisation** : modèle de la MAS, schéma-blocs de la boucle de vitesse
- → **T24 Correcteurs** : asservissement de vitesse par correcteur PI
- → **T14 Distribution** : protection du variateur, câblage de puissance

---

*Source : formulaire_capet.md §7–9 · sujets 2017 (Métro MF2000), 2019 (Transport câble), 2020 (Exotec), 2022 (Banc essai), 2024 (Extracteur air)*
