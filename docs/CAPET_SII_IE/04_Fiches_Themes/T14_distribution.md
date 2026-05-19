# T14 — Production / Transport / Distribution électrique

> **Fréquence :** 22/22 sujets · **Intensité moyenne :** 🔴 Central
> Thème transversal présent dans presque tous les sujets : câblage, protection, choix des équipements, régimes de neutre.

---

## Notions clés

### Chute de tension en ligne

$$\Delta U = \rho \cdot \frac{L}{S} \cdot I \quad \text{(monophasé ou DC)}$$

$$\Delta U = \sqrt{3} \cdot \rho \cdot \frac{L}{S} \cdot I \quad \text{(triphasé)}$$

- $\rho$ : résistivité du conducteur ($\rho_{Cu} = 1{,}7 \times 10^{-8}\ \Omega\cdot\text{m} \approx 0{,}017\ \Omega\cdot\text{mm}^2/\text{m}$ ; $\rho_{Al} = 0{,}028\ \Omega\cdot\text{mm}^2/\text{m}$)
- $L$ : longueur du câble (aller simple, en m)
- $S$ : section du conducteur (mm²)
- $I$ : courant (A)
- $\Delta U\% = \Delta U/U_n \times 100$ → norme : $\Delta U\% \leq 3\ \%$ pour l'éclairage, $\leq 5\ \%$ pour les moteurs

> **Formule à restituer de mémoire** — fréquence 3 au concours

### Section de câble

$$S = \frac{\rho \cdot L \cdot I}{\Delta U_{max}}$$

← section minimale pour respecter la chute de tension

Sections normalisées (cuivre) : 1,5 – 2,5 – 4 – 6 – 10 – 16 – 25 – 35 – 50 – 70 – 95 – 120 mm²

### Choix du disjoncteur / fusible

$I_{calibre} \geq I_{n,charge} / \eta$ (surcourant ≤ 20 % de $I_{calibre}$ en régime établi)

Courbes de déclenchement :
- **B** : protection câbles résidentiels, démarrage doux ($3$–$5 \times I_n$)
- **C** : moteurs à démarrage direct ($5$–$10 \times I_n$)
- **D** : moteurs à fort courant d'appel ($10$–$20 \times I_n$)

### Puissance et pertes en ligne

$$P_{pertes} = 3 \cdot R_L \cdot I^2 \quad \text{(triphasé)}$$

$$P_{totale} = P_{charge} + P_{pertes}$$

---

## Régimes de neutre (Schémas de liaison à la terre)

| Régime | 1ère lettre | 2ème lettre | Principe | Usage |
|---|:---:|:---:|---|---|
| **TT** | T = neutre relié terre | T = masses reliées terre | Disjoncteur différentiel 30 mA obligatoire | Résidentiel, bâtiments |
| **TN-S** | T = neutre relié terre | N = masses reliées neutre | Neutre et PE séparés | Industrie, tertiaire |
| **TN-C** | T = neutre relié terre | N = masses reliées neutre | Neutre et PE confondus (PEN) | Anciens bâtiments |
| **IT** | I = neutre isolé | T = masses reliées terre | Premier défaut non dangereux | Blocs opératoires, salle d'eau |

**Courant de défaut :**
- Régime TT : $I_f = U_n / R_{défaut}$ (limité par $R_{terre}$) → DDR nécessaire
- Régime TN : $I_f = U_n / Z_{boucle}$ (fort courant) → protection magnétique
- Régime IT : $I_{f1}$ faible (1er défaut) ; $I_{f2}$ après 2e défaut = dangereux

---

## Sécurité électrique — Classes de protection

| Classe | Symbole | Protection | Exemple |
|---|:---:|---|---|
| I | — | Masse reliée à la terre (fil PE) | Moteur électrique, machine-outil |
| II | ⬜ | Double isolation (pas de terre) | Outillage portatif, appareils HiFi |
| III | ◇ | Alimentation TBTS < 50 V | Jouets, salle de bains |

### Indices de protection (IP)

**IP X Y** — X : protection solides (0–6), Y : protection liquides (0–8)

Exemples : IP 20 (doigts, pas d'eau) · IP 55 (poussière + jets d'eau) · IP 67 (immersion)

---

## Éclairage — Notions de base (sujet 2018 E2)

| Grandeur | Unité | Définition |
|---|---|---|
| Flux lumineux $\Phi$ | Lumen (lm) | Quantité de lumière émise |
| Intensité lumineuse $I$ | Candela (cd) | Flux par unité d'angle solide |
| Éclairement $E$ | Lux (lx) | Flux reçu par unité de surface |
| Luminance $L$ | cd/m² | Intensité perçue par unité de surface |

$$E = \Phi / S \quad \text{(en lux, si flux uniformément réparti sur surface } S\text{)}$$

---

## Types de questions au concours

| Type | Exemple | Formule |
|---|---|---|
| Chute de tension | "Vérifier que ΔU% ≤ 5 % pour le câble 50 m" | $\Delta U = \sqrt{3} \cdot \rho \cdot L \cdot I/S$ |
| Section minimale | "Calculer la section pour le câble d'alimentation" | $S = \rho \cdot L \cdot I/\Delta U_{max}$ |
| Calibre disjoncteur | "Choisir le calibre du disjoncteur du moteur" | $I_{cal} \geq I_n$ → courbe C |
| Régime de neutre | "Quel régime de neutre pour une salle d'eau ?" | IT ou TBTS |
| Courant de court-circuit | "Calculer $I_{cc}$ pour vérifier le pouvoir de coupure" | $I_{cc} = U/Z_{boucle}$ |
| Pertes en ligne | "Calculer les pertes Joule dans les câbles" | $P_{pertes} = 3 \cdot R_L \cdot I^2$ |

---

## Pièges courants

1. **Confondre L aller et L aller-retour** : $\Delta U = \rho \cdot (L/S) \cdot I$ utilise $L$ = longueur aller seulement (la formule intègre déjà le facteur 2 ou $\sqrt{3}$ selon le régime).
2. **Mauvaise résistivité** : $\rho_{Cu} \approx 0{,}017\ \Omega\cdot\text{mm}^2/\text{m}$ (à 20°C). En pratique les sujets donnent $\rho$ — vérifier.
3. **Confondre TN et TT** : en TT, le DDR est obligatoire ; en TN, c'est la protection magnétique qui protège.
4. **Oublier le courant d'appel** dans le choix du disjoncteur : un moteur a un courant d'appel 5–8× $I_n$ → courbe C ou D.

---

## Liens avec d'autres thèmes

- → **T02 Puissance AC** : courant absorbé = base du calcul de $\Delta U$ et du dimensionnement câble
- → **T11 Variation de vitesse** : câblage du variateur de vitesse
- → **T13 ENR** : raccordement PV au réseau, onduleur raccordé réseau
- → **T15 Sécurité** : régimes de neutre, protection différentielle

---

*Source : formulaire_capet.md §6 · sujets 2015, 2016 (Maison active), 2018 (Éclairage), 2022 (Réseau chaleur), 2025 (Site isolé)*
