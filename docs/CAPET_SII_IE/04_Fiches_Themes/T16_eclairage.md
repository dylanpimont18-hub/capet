# T16 — Éclairage

> **Fréquence :** 4/22 sujets · **Intensité moyenne :** 🟡 Mentionné
> Présent dans les sujets d'éclairage public et bâtiment. Questions de dimensionnement photométrique et bilan énergétique.

---

## Notions clés

### Grandeurs photométriques

| Grandeur | Symbole | Unité | Définition |
|---|---|---|---|
| Flux lumineux | $\Phi$ | lumen (lm) | Puissance lumineuse totale émise |
| Intensité lumineuse | $I$ | candela (cd) | Flux par unité d'angle solide |
| Éclairement | $E$ | lux (lx) | Flux reçu par unité de surface |
| Luminance | $L$ | cd/m² | Intensité par unité de surface apparente |

**Relations :**
$$E = \frac{\Phi}{A} = \frac{I}{d^2} \quad \text{(source ponctuelle, normale)}$$

**Loi du cosinus (Lambertien) :**
$$E = \frac{I \cdot \cos\theta}{d^2}$$

> ❌ **À mémoriser** : $E = \frac{I \cos\theta}{d^2}$ (lux)

### Rendement lumineux (efficacité)

$$\eta_{lum} = \frac{\Phi_{sortie}}{P_{électrique}} \quad \text{(lm/W)}$$

| Source | Rendement typique |
|---|---|
| Incandescence | 10–15 lm/W |
| Fluorescent (tubes) | 70–100 lm/W |
| LED | 80–200 lm/W |
| Sodium haute pression | 80–130 lm/W |

### Méthode des lux (calcul d'installation)

$$E_{moy} = \frac{N \cdot \Phi_{lampe} \cdot \eta_{luminaire} \cdot FU \cdot FM}{A}$$

- $N$ : nombre de luminaires
- $FU$ : facteur d'utilisation (0,5 à 0,8)
- $FM$ : facteur de maintenance (0,6 à 0,9)
- $A$ : surface du local (m²)

**Nombre de luminaires pour atteindre $E_{req}$ :**
$$N = \frac{E_{req} \cdot A}{\Phi_{lampe} \cdot FU \cdot FM}$$

### Température de couleur

| Couleur | Température (K) | Application |
|---|---|---|
| Blanc chaud | 2700–3000 K | Logement, confort |
| Blanc neutre | 3500–4000 K | Bureaux, commerces |
| Blanc froid | > 5000 K | Industrie, médical |

### IRC (Indice de Rendu des Couleurs)

- IRC de 0 à 100
- IRC > 80 : requis pour bureaux, magasins
- IRC > 90 : musées, contrôle qualité

### Consommation d'énergie

$$W = P \cdot t \quad \text{(Wh)} \qquad C = W/1000 \quad \text{(kWh)}$$

**Consommation annuelle éclairage public :**
$$W_{an} = N_{points} \cdot P_{unitaire} \cdot h_{fonctionnement}$$

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Éclairement sur une surface | $E = I\cos\theta/d^2$ |
| Nombre de luminaires | $N = E_{req} \cdot A/(\Phi \cdot FU \cdot FM)$ |
| Puissance installée pour $E$ | $P = E_{req} \cdot A/(\eta_{lum} \cdot FU \cdot FM)$ |
| Économie énergie par remplacement | $\Delta P \cdot h_{an} \cdot N$ |
| Temps de retour investissement | $C_{install}/(\Delta P \cdot h_{an} \cdot N \cdot c_{kWh})$ |

---

## Pièges courants

1. **Lux ≠ lumens** : le lux est une densité surfacique de flux (lm/m²), les lumens c'est le flux total de la source.
2. **Facteur $\cos\theta$** : pour une source non perpendiculaire à la surface, ne pas oublier $\cos\theta$.
3. **FU et FM** : souvent donnés dans le sujet, mais si pas donnés, utiliser $0{,}65 \times 0{,}8 = 0{,}52$ comme valeur conservative.
4. **IRC vs température** : deux critères indépendants. Un tube sodium peut avoir haute efficacité mais mauvais IRC (< 25).
