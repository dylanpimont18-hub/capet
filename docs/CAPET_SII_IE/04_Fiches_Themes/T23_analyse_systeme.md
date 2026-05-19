# T23 — Analyse de système & approche fonctionnelle

> **Fréquence :** 9/22 sujets · **Intensité moyenne :** 🔴 Central
> Thème méthodologique transversal. La lecture du cahier des charges, l'identification de la chaîne d'énergie et la frontière d'étude sont demandées dans pratiquement tous les sujets.

---

## Notions clés

### Démarche d'analyse de système

1. Identifier la **frontière d'étude** (ce qui est dans le système vs l'environnement)
2. Identifier les **flux d'énergie** (électrique, mécanique, thermique, hydraulique)
3. Identifier les **flux d'information** (capteurs, consignes, bus de communication)
4. Définir les **fonctions** du système (FP = fonction principale, FC = contrainte)

### Chaîne d'énergie

```
    Alimenter → Convertir → Transmettre → Agir
        ↑ commander                 ↑ acquérir
    (chaîne d'information)
```

**Exemple variateur moteur :**
```
    Réseau 400V → Redresseur → Bus DC → Onduleur → Moteur → Charge
                       ↑ consigne vitesse ↑ codeur retour
```

### Chaîne d'information

```
    Acquérir → Traiter → Communiquer → Commander
    (capteurs) (API/UC) (bus terrain) (actionneurs)
```

### Diagramme SysML — principaux diagrammes

| Diagramme | Usage |
|---|---|
| Bloc (BDD) | Structure du système, composants |
| Interne (IBD) | Flux entre composants |
| Cas d'utilisation (UC) | Fonctions attendues par les acteurs |
| Séquence (SD) | Interactions temporelles |
| État (STM) | Modes de fonctionnement |
| Exigences | Cahier des charges structuré |

### Cahier des charges fonctionnel (CdCF)

**Format d'une fonction :**
> $F_i$ : [verbe d'action] [objet] [dans quel contexte] [critère d'appréciation] [niveau acceptable]

**Exemple :**
> FP1 : Alimenter le moteur en énergie électrique triphasée à partir du réseau 400V/50Hz.
> Critère : Puissance fournie $\geq 15$ kW. Niveau : en régime permanent.

### Critères SMARTE (pour les exigences)

- **S**pécifique
- **M**esurable
- **A**tteignable
- **R**éaliste
- **T**emporel
- **E**nvironnementaux

### Bilan énergétique global

$$\eta_{système} = \frac{P_{utile}}{P_{absorbée}} = \prod_i \eta_i$$

Les rendements des étages se multiplient :
$$\eta_{total} = \eta_{redresseur} \cdot \eta_{onduleur} \cdot \eta_{moteur} \cdot \eta_{transmission}$$

---

## Types de questions au concours

| Type | Approche |
|---|---|
| Identifier la frontière d'étude | Tracer le contour du système |
| Compléter un diagramme IBD | Identifier les flux entrants/sortants |
| Formuler une exigence | Utiliser la forme "L'[élément] doit [action] [critère numérique]" |
| Calculer le rendement global | $\eta = \prod \eta_i$ |
| Identifier le maillon "faible" | Trouver l'étage avec le rendement le plus faible |

---

## Pièges courants

1. **Frontière d'étude** : bien distinguer ce qu'on étudie du reste. Un réseau électrique est généralement une entrée (extérieur), pas un composant du système.
2. **Fonction vs solution** : une analyse fonctionnelle décrit "quoi faire", pas "comment". Ne pas écrire "utiliser un moteur" dans une FP — écrire "convertir l'énergie électrique en énergie mécanique".
3. **Rendement multiplicatif** : $\eta_{total} \neq \sum \eta_i / n$ — c'est un produit.
4. **SysML** : le jury signale régulièrement des confusions entre les diagrammes BDD et IBD. BDD = structure des types, IBD = flux entre instances.
