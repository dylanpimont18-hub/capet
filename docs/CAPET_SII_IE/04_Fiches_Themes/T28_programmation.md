# T28 — Programmation & algorithmique

> **Fréquence :** 7/22 sujets · **Intensité moyenne :** 🔴 Central
> ⚠️ **Point aveugle critique signalé jury TOUTES sessions** : "lacunes massives et récurrentes". Moins de 20 % des candidats répondent correctement aux questions de programmation.

---

## Notions clés

### Structures algorithmiques de base

**Séquence :**
```
instruction_1
instruction_2
instruction_3
```

**Condition :**
```
SI condition ALORS
    instructions_vraies
SINON
    instructions_fausses
FIN SI
```

**Boucle POUR (nombre d'itérations connu) :**
```
POUR i DE 0 À n-1 FAIRE
    instructions
FIN POUR
```

**Boucle TANT QUE (condition) :**
```
TANT QUE condition FAIRE
    instructions
FIN TANT QUE
```

### Pseudo-code et Python équivalents

| Pseudo-code | Python |
|---|---|
| `valeur ← 5` | `valeur = 5` |
| `SI x > 0 ALORS` | `if x > 0:` |
| `POUR i DE 0 À 9` | `for i in range(10):` |
| `TANT QUE x < 10` | `while x < 10:` |
| `Afficher(valeur)` | `print(valeur)` |
| `RETOURNER valeur` | `return valeur` |

### Chronogramme — lecture d'un programme

Un chronogramme montre l'évolution des variables dans le temps.

**Exemple : machine d'états pour un moteur**
```
État:    ARRET ──► DEMARRAGE ──► MARCHE ──► FREINAGE ──► ARRET
             ↑ bouton_on           ↑ vitesse atteinte   ↑ bouton_stop
```

### Automates programmables industriels (API)

**Structure d'un programme API (cycle) :**
```
Lecture des entrées (capteurs)
    ↓
Exécution du programme (traitement)
    ↓
Écriture des sorties (actionneurs)
    ↓
(recommencer)
```

**Langages API (norme IEC 61131-3) :**
| Langage | Type | Usage |
|---|---|---|
| LD (Ladder Diagram) | Graphique | Logique séquentielle |
| FBD (Function Block Diagram) | Graphique | Blocs fonctionnels |
| ST (Structured Text) | Texte | Calculs, boucles |
| IL (Instruction List) | Texte bas niveau | Ancien |
| SFC (Sequential Function Chart) | Grafcet | Séquencement |

### Grafcet

- **Étape** : état stable du système
- **Transition** : condition de passage
- **Réceptivité** : condition logique sur les capteurs

```
   [1] Attente
    |
    | Bouton_on
    |
   [2] Démarrage
    |
    | vitesse_OK
    |
   [3] Marche nominale
```

### Opérateurs logiques

| Opérateur | Python | Description |
|---|---|---|
| ET | `and` | Vrai si les deux sont vrais |
| OU | `or` | Vrai si au moins un est vrai |
| NON | `not` | Inversion |
| XOR | `^` | Vrai si exactement un est vrai |

### Fonctions et procédures

```python
def calculer_puissance(U, I, cos_phi):
    """Calcule la puissance active."""
    P = U * I * cos_phi
    return P

# Appel
P_moteur = calculer_puissance(230, 5.2, 0.8)
```

---

## Types de questions au concours

| Type | Approche |
|---|---|
| Lire un algorithme et dérouler | Suivre les variables étape par étape |
| Écrire un algorithme pour une tâche | Décomposer en séquence/condition/boucle |
| Compléter un Grafcet | Identifier étapes manquantes et transitions |
| Lire un chronogramme API | Associer les états des sorties aux entrées |
| Corriger un bug dans un programme | Chercher la condition ou l'opérateur erroné |

---

## Pièges courants

1. **Indentation Python** : Python est sensible à l'indentation. Un bloc `if` ou `for` doit être indenté de 4 espaces.
2. **Boucle infinies** : `while True` sans condition de sortie = programme bloqué.
3. **Index 0** : en Python et dans la plupart des langages, les listes commencent à l'indice 0. `liste[0]` est le premier élément.
4. **Grafcet** : une transition ne se déclenche que si l'étape précédente est active ET la réceptivité est vraie. Bien distinguer étape (rectangle) et transition (trait horizontal).
5. **Jury** : répondre même partiellement aux questions de programmation. Commenter le code/algorithme pour montrer la compréhension même si la syntaxe est fausse.
