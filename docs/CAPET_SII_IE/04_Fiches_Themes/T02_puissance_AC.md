# T02 — Régime sinusoïdal / Puissance AC

> **Fréquence :** 22/22 sujets · **Intensité moyenne :** 🔴 Central
> **Rang :** thème #1 au concours — présent dans toutes les épreuves, souvent en fil conducteur

---

## Notions clés

### Régime sinusoïdal monophasé

- Représentation de Fresnel (phaseur) : $u(t) = U_{max} \cdot \sin(\omega t + \varphi)$ → $\bar{U} = U\angle\varphi$ (valeurs efficaces)
- Impédances : R (résistive), $jL\omega$ (inductance), $\frac{1}{jC\omega}$ (condensateur)
- Loi des mailles et loi des nœuds avec impédances complexes

### Triangle des puissances

```
     S (VA)
    /|
   / |
  /  |
 /φ  |
P────Q
(W)  (VAR)
```

| Grandeur | Formule monophasé | Formule triphasé |
|---|---|---|
| Puissance active P | $U \cdot I \cdot \cos\varphi$ | $\sqrt{3} \cdot U \cdot I \cdot \cos\varphi$ |
| Puissance réactive Q | $U \cdot I \cdot \sin\varphi$ | $\sqrt{3} \cdot U \cdot I \cdot \sin\varphi$ |
| Puissance apparente S | $U \cdot I$ | $\sqrt{3} \cdot U \cdot I$ |
| Facteur de puissance | $\cos\varphi = P/S$ | $\cos\varphi = P/S$ |
| Relation triangle | $S^2 = P^2 + Q^2$ | $S^2 = P^2 + Q^2$ |
| Énergie | $E = P \cdot t$ | $E = P \cdot t$ |

> ❌ **Formule à restituer de mémoire** : $P = \sqrt{3} \cdot U \cdot I \cdot \cos\varphi$ (triphasé) — fréquence 6 au concours

### Réseaux triphasés équilibrés

- Tension composée $U = \sqrt{3} \cdot V_{simple}$ (U ≈ 400 V, $V_{simple}$ ≈ 230 V en France)
- Couplage **étoile** : $I_{ligne} = I_{phase}$, $U_{composée} = \sqrt{3} \cdot V_{phase}$
- Couplage **triangle** : $U_{ligne} = U_{phase}$, $I_{ligne} = \sqrt{3} \cdot I_{phase}$
- Déphasage entre phases : 120°

### Compensation d'énergie réactive

- Condensateur pour compenser le facteur de puissance :
  $$C = \frac{Q_{abs}}{3 \cdot \omega \cdot V_p^2}$$ (triphasé, condensateurs en étoile)
  ou $C = \frac{P \cdot \tan\varphi_1 - P \cdot \tan\varphi_2}{\omega \cdot U^2}$ (monophasé)
- But : réduire I pour même P → moins de pertes en ligne, moins de pénalités

### Taux de distorsion harmonique (THD)

$$THD = \frac{\sqrt{\sum_{n \geq 2} I_n^2}}{I_1}$$

Apparaît dans les sujets traitant de variateurs de vitesse, convertisseurs, MLI.

---

## Types de questions au concours

| Type | Exemple | Formule mobilisée |
|---|---|---|
| Calcul de puissance consommée | "Quelle est la puissance active du moteur ?" | $P = \sqrt{3} \cdot U \cdot I \cdot \cos\varphi$ |
| Calcul de courant nominal | "Calculer In du moteur" | $I = \frac{P}{\sqrt{3} \cdot U \cdot \cos\varphi \cdot \eta}$ |
| Bilan de puissance | "Vérifier le calibre du disjoncteur" | $I_n > I_{moteur} / \eta$ |
| Compensation réactive | "Dimensionner la batterie de condensateurs" | $C = Q/(\omega \cdot U^2)$ |
| Énergie consommée | "Coût annuel de fonctionnement" | $E = P \cdot t$ → coût $= E \cdot c_{tarif}$ |
| Analyse THD | "La norme est-elle respectée ?" | THD < 5 % (norme EN 50160) |

---

## Pièges courants (signalés jury)

1. **Confondre U composée et V simple** : U = 400 V composé, V = 230 V simple. Toujours vérifier quelle tension est donnée dans le sujet.
2. **Oublier η dans le calcul du courant** : $I = P_{élec} / (\sqrt{3} \cdot U \cdot \cos\varphi) \neq I = P_{mécanique} / (\sqrt{3} \cdot U \cdot \cos\varphi \cdot \eta)$.
3. **Utiliser la formule monophasée en triphasé** : $P = U \cdot I \cdot \cos\varphi$ (faux) → $P = \sqrt{3} \cdot U \cdot I \cdot \cos\varphi$ (correct en triphasé).
4. **Omettre les unités** : signalé dans tous les rapports. Donner W, kW ou MW selon l'ordre de grandeur.
5. **Confondre puissance et énergie** : P en watts, $E = P \cdot t$ en joules ou kWh.

---

## Calibrage de la réponse attendue

**Question type :** "Le moteur a une puissance nominale de 22 kW, un rendement de 92 %, un cosφ = 0,85, alimenté en 400 V triphasé. Calculer le courant absorbé."

**Réponse attendue :**
- Formule : $P_{absorbée} = P_{mécanique} / \eta = 22\,000 / 0{,}92 = 23\,913$ W
- $I = P_{absorbée} / (\sqrt{3} \cdot U \cdot \cos\varphi) = 23\,913 / (1{,}732 \cdot 400 \cdot 0{,}85) =$ **40,5 A**
- Résultat encadré, unités présentes, conclusion si applicable ("calibre disjoncteur ≥ 50 A")

---

## Liens avec d'autres thèmes

- → **T11 Variation de vitesse** : le variateur consomme du réactif (cosφ variable)
- → **T14 Distribution** : chute de tension liée au courant absorbé
- → **T24 Correcteurs** : asservissement de puissance active (sites ENR)
- → **T03 Thermique** : puissance thermique dissipée = pertes = $P_{abs} - P_{utile}$

---

*Source : formulaire_capet.md §5 · tableau_themes_capet.md T02 · sujets 2015–2025*
