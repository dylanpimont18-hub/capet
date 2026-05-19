# T15 — Sécurité électrique

> **Fréquence :** 7/22 sujets · **Intensité moyenne :** 🟠 Important
> Régimes de neutre (TT/TN/IT), protection des personnes, appareillage de protection. Questions fréquentes depuis 2020.

---

## Notions clés

### Effets du courant sur le corps humain

| Courant (mA) | Effet |
|---|---|
| < 1 | Imperceptible |
| 1–10 | Perception, fourmillements |
| 10–30 | Contraction musculaire (seuil de lâcher ≈ 15 mA) |
| 30–300 | Fibrillation ventriculaire, danger mortel |
| > 300 | Brûlures internes graves |

**Tension limite de contact :**
- **50 V AC** en milieu sec ($U_L = 50$ V)
- **25 V AC** en milieu humide
- **120 V DC** en milieu sec

**Résistance du corps humain (CEI 60479) :**
$$R_{corps} \approx 1000\ \Omega \text{ à } 5000\ \Omega \text{ (peau sèche)}$$

### Régimes de neutre

#### Schéma TT (Terre-Terre)

```
    Réseau ───────────────────────── Phase
    Neutre ──┐              ──────── Neutre
             ├─ Terre réseau       
             │                       │
             │                      DDR
                                     │
    Corps matériel ────────── Prise de terre installation
```

- Neutre réseau relié à la terre, masse des appareils reliée à une terre séparée
- Protection par **DDR** (dispositif différentiel résiduel)
- $I_d = U/(R_{neutre} + R_{installation})$, DDR déclenche si $I_d > I_{dif,n}$

#### Schéma TN (Terre-Neutre)

- TN-C : neutre et PE confondus (fil PEN) — interdit en ≤ 32 mm²
- TN-S : neutre (N) et protection (PE) séparés
- Protection par **disjoncteur** ou fusible
- Courant de défaut élevé → déclenchement rapide assuré

$$I_{défaut} = \frac{U_{phase}}{Z_{boucle}} \gg I_{déclenchement}$$

#### Schéma IT (Isolation-Terre)

- Neutre isolé ou impédant
- **Premier défaut** : courant de défaut très faible, alarme mais pas de coupure
- **Deuxième défaut** : coupure obligatoire
- Utilisé en milieu médical, industriel critique (continuité de service)
- Contrôlé par CPI (Contrôleur Permanent d'Isolement)

### Appareillage de protection

| Appareil | Rôle | Courant de déclenchement |
|---|---|---|
| Fusible | Court-circuit | $I_{cc}$ selon calibre |
| Disjoncteur magnétique | Court-circuit | $5$ à $15 \times I_n$ |
| Disjoncteur thermique | Surcharge | $1{,}13$ à $1{,}45 \times I_n$ |
| DDR (différentiel) | Défaut à la terre | $I_{dif,n}$ = 10, 30, 300 mA... |

**DDR 30 mA** : protection des personnes (standard France)  
**DDR 300 mA** : protection contre incendie (câblage)

### Classes de protection des matériels

| Classe | Protection | Symbole |
|---|---|---|
| 0 | Isolation principale seulement | Interdit nouvelles installations |
| I | Isolation + mise à la terre | ⏚ |
| II | Double isolation (sans terre) | □ |
| III | TBTS (< 50 V AC) | ◇ |

### Indices de protection (IP xx)

- Premier chiffre (0–6) : protection contre les corps solides
- Second chiffre (0–8) : protection contre l'eau
- IK : protection mécanique aux chocs

---

## Types de questions au concours

| Type | Formule/Règle |
|---|---|
| Tension de contact admissible | $U_L = 50$ V (AC, milieu sec) |
| Courant de défaut TN | $I_d = U/Z_{boucle}$ |
| Choix du différentiel | $I_{dif} \leq 0{,}03$ A (30 mA) personnes |
| Résistance de prise de terre (TT) | $R_A \leq U_L/I_{dif} = 50/0{,}03 = 1667\ \Omega$ |
| Vérification déclenchement disjoncteur TN | $I_{cc,min} > I_{déclenchement}$ |

---

## Pièges courants

1. **TT vs TN** : en TT, la protection est assurée par DDR (différentiel) car le courant de défaut est faible. En TN, c'est le disjoncteur/fusible.
2. **50 V** : c'est la tension de contact limite, pas la tension entre phases.
3. **DDR 30 mA vs 300 mA** : 30 mA pour les prises et protection des personnes, 300 mA pour les circuits en tête (incendie).
4. **Classe II** : pas de fil de terre → pas de borne PE. Ne pas câbler la borne de terre sur un appareil classe II.
