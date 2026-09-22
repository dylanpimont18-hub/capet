# T28 — Logique combinatoire
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

> **Note :** Les mots-clés « table de vérité », « porte logique », « Karnaugh », « équation logique », « multiplexeur », « additionneur », « logique combinatoire », « algèbre de Boole » sont **absents** des 41 fichiers Markdown analysés. Les sujets CAPET SII IE se concentrent sur l'électrotechnique, les convertisseurs et l'asservissement. La logique combinatoire pure n'a pas été rencontrée explicitement dans les questions des épreuves écrites 2013–2026.
>
> La section 1 présente donc le cours théorique complet du programme. Les sections 2 et 3 indiquent « Non trouvé dans les sources analysées ».

---

## 1. FORMULES ET COURS

### 1.1 Algèbre de Boole — axiomes

Variables binaires : $A \in \{0, 1\}$

**Opérateurs fondamentaux :**

| Opération | Symbole | Notation | Exemple |
|-----------|---------|----------|---------|
| ET (AND) | $\cdot$ | $A \cdot B$ | $1 \cdot 1 = 1$ |
| OU (OR) | $+$ | $A + B$ | $0 + 1 = 1$ |
| NON (NOT) | $\overline{\phantom{A}}$ | $\overline{A}$ | $\overline{0} = 1$ |

**Théorèmes fondamentaux :**
- Idempotence : $A \cdot A = A$ ; $A + A = A$
- Complémentarité : $A \cdot \overline{A} = 0$ ; $A + \overline{A} = 1$
- Absorption : $A \cdot (A + B) = A$ ; $A + (A \cdot B) = A$
- Distributivité : $A \cdot (B + C) = A \cdot B + A \cdot C$

**Théorèmes de De Morgan :**
$$\overline{A \cdot B} = \overline{A} + \overline{B} \qquad \overline{A + B} = \overline{A} \cdot \overline{B}$$

### 1.2 Portes logiques élémentaires

| Porte | Expression | Table de vérité (2 entrées) |
|-------|-----------|----------------------------|
| AND | $S = A \cdot B$ | $S=1$ ssi $A=B=1$ |
| OR | $S = A + B$ | $S=0$ ssi $A=B=0$ |
| NOT | $S = \overline{A}$ | inverseur |
| NAND | $S = \overline{A \cdot B}$ | universel |
| NOR | $S = \overline{A + B}$ | universel |
| XOR | $S = A \oplus B$ | $S=1$ ssi $A \neq B$ |
| XNOR | $S = \overline{A \oplus B}$ | $S=1$ ssi $A = B$ |

**Réalisation universelle :** toute fonction logique est réalisable avec des NAND seuls ou des NOR seuls.

### 1.3 Table de vérité et mintermes / maxtermes

Pour $n$ variables : $2^n$ lignes.

- **Forme canonique disjonctive (somme de mintermes, SOP) :** somme des mintermes pour lesquels $S = 1$
- **Forme canonique conjonctive (produit de maxtermes, POS) :** produit des maxtermes pour lesquels $S = 0$

*Exemple (demi-additionneur) :*

| $A$ | $B$ | Somme $S = A \oplus B$ | Retenue $C = A \cdot B$ |
|-----|-----|----------------------|------------------------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

### 1.4 Simplification par tableau de Karnaugh

**Principe :** grouper les « 1 » adjacents par puissances de 2 (1, 2, 4, 8…) pour éliminer des variables.

Tableau de Karnaugh à 4 variables ($A$, $B$, $C$, $D$) :

```
       CD
AB    00  01  11  10
00  [  ][ ][ ][ ]
01  [  ][ ][ ][ ]
11  [  ][ ][ ][ ]
10  [  ][ ][ ][ ]
```

**Règles :**
- Groupes de 2 : éliminent 1 variable
- Groupes de 4 : éliminent 2 variables
- Groupes de 8 : éliminent 3 variables
- Les groupes peuvent « boucler » sur les bords du tableau
- On cherche les plus grands groupes possibles (couverture minimale)

**Résultat :** expression minimale en somme de produits (SOP).

### 1.5 Circuits combinatoires courants

**Multiplexeur $2^n \to 1$ (MUX) :**
- $n$ entrées de sélection, $2^n$ entrées de données, 1 sortie
- Utilisé comme réalisateur universel de fonctions logiques

**Démultiplexeur $1 \to 2^n$ (DEMUX) :**
- L'inverse du MUX : aiguille une entrée vers une sortie

**Décodeur $n \to 2^n$ :**
- Active une seule sortie parmi $2^n$ selon le code binaire en entrée
- Ex. : décodeur 3 lignes vers 8 lignes (utilisé en adressage mémoire)

**Encodeur $2^n \to n$ (prioritaire) :**
- Encode en binaire la position de l'entrée active

**Additionneur 1 bit (Full Adder) :**
$$S = A \oplus B \oplus C_{in} \qquad C_{out} = A \cdot B + C_{in}(A \oplus B)$$

**Comparateur :** génère les signaux $A > B$, $A = B$, $A < B$.

### 1.6 Codage numérique

**Code binaire naturel (CBN) :**
$$N_{10} = b_{n-1} \cdot 2^{n-1} + \cdots + b_1 \cdot 2 + b_0$$

**Code BCD (Binary Coded Decimal) :** chaque décimale codée sur 4 bits.

**Code Gray :** code de distance 1 (un seul bit change entre deux mots consécutifs). Utilisé pour les codeurs angulaires.

*Connexion avec les sujets CAPET :* le codeur incrémental du sujet 2023 génère des impulsions comptées en binaire (résolution $0{,}15$ mm/impulsion, position sur 12 bits, 8 bits de poids fort retenus).

---

## 2. QUESTIONS TYPES

Non trouvé dans les sources analysées (aucune question explicite de logique combinatoire dans les épreuves écrites CAPET SII IE 2013–2026).

*Observations connexes :* les sujets contiennent régulièrement des questions de **codage binaire / hexadécimal** (liaison série, GPS, capteurs de température), qui mobilisent la logique combinatoire de manière implicite :
- Décoder un octet en hexadécimal (E2 disciplinaire 2022, 2023)
- Calculer le nombre de bits nécessaires pour coder une position (2023 Q.D2–D3)
- Opérations de décalage et masquage sur des registres (2022 Q.17)

---

## 3. ATTENTES DU JURY

Non trouvé dans les sources analysées pour la logique combinatoire pure.

*Indirectement* : le jury insiste depuis 2021 sur la maîtrise des **bases de la numération** (binaire, hexadécimal, conversions) et de l'**algorithmie** — compétences adjacentes à la logique combinatoire.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur observée dans les sujets |
|----------|---------------------------------|
| Résolution d'un codeur incrémental | $0{,}15$ mm/impulsion (2023) |
| Nombre de bits pour coder 680 mm / 0,15 = 4533 positions | 12 bits ($2^{12} = 4096 < 4533 < 8192 = 2^{13}$) → 13 bits |
| Résolution CAN | 10 à 12 bits typiquement |
| Valeur hexadécimale ASCII | 0x45 = « E », 0x57 = « W » (2023) |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **De Morgan** : erreur fréquente : $\overline{A + B} \neq \overline{A} + \overline{B}$. La bonne formule est $\overline{A + B} = \overline{A} \cdot \overline{B}$.
- **Karnaugh** : oublier que le tableau est torique (les bords gauche-droit et haut-bas sont adjacents).
- **Forme canonique vs minimale** : la forme SOP/POS canonique n'est pas minimisée ; Karnaugh sert à la minimiser.
- **Binaire non signé vs signé** : pour les CAN/CNA, vérifier si le signe est sur le bit de poids fort.
- **Confusion bit / octet** : reporté comme erreur fréquente par le jury 2023 (« beaucoup d'amalgames entre bit et octet »).
- **XOR vs OR** : $A \oplus B = 1$ si et seulement si $A \neq B$, à ne pas confondre avec le OR inclusif.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T22 (électronique numérique)** : les portes logiques sont les briques de base des circuits intégrés numériques ; la logique combinatoire est le fondement de l'arithmétique binaire (CAN, CNA, UAL).
- **T29 (logique séquentielle)** : la logique combinatoire est la partie purement instantanée (sans mémoire) des automates ; la logique séquentielle y ajoute les bascules (mémoire).
- **T30 (métrologie)** : la chaîne de mesure numérique (CAN) utilise le codage binaire, les erreurs de quantification liées à la résolution en bits.
- **T26/T27 (automatique)** : la commande numérique d'un asservissement (relation de récurrence, table de vérité d'un décodeur d'état) mobilise la logique combinatoire.
