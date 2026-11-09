# T32 — Ingénierie système : analyse fonctionnelle et SysML
## Contenu documentaire — créé le 2026-11-10 pour couvrir le référentiel

> SysML et l'analyse fonctionnelle apparaissent dans 8 des 13 années 2013–2025 (ibd en 2014,
> 2021, 2022, 2023 ; cas d'utilisation en 2018, 2021, 2022 ; diagramme d'états en 2017, 2019,
> 2021 ; exigences en 2022 et en E2 2026). Le thème produit peu de formules : l'essentiel des
> cartes est fait de pièges (définitions et confusions classiques).

---

## 1. FORMULES ET COURS

### 1.1 Chaîne d'énergie et vérification des exigences

| Grandeur | Formule | Unité | Fréquence | Source |
|---|---|---|---|---|
| Rendement global d'une chaîne d'étages en série | $\eta_g = \prod_i \eta_i$ | — | Courant | Cours ; chaînes d'énergie de tous les sujets |
| Puissance à fournir en amont d'une chaîne | $P_a = \frac{P_u}{\eta_g}$ | W | Courant | Cours |
| Énergie consommée sur un profil de mission | $E = \sum_k P_k \, \Delta t_k$ | J | Courant | Cours |
| Rendement hydraulique d'une pompe ($Q$ en m³/h, $P_1$ en kW) | $\eta_h = \frac{H \, Q}{367 \, P_1}$ | — | Présent | E2 disciplinaire 2022, Q11 |
| Écart relatif entre valeur obtenue et valeur exigée | $\varepsilon_r = \frac{\lvert x - x_{exig} \rvert}{x_{exig}}$ | — | Courant | Cours |
| Marge par rapport à une valeur limite | $M = \frac{x_{lim} - x}{x_{lim}}$ | — | Courant | Cours |

### 1.2 Repères de cours (sans formule)

- Bête à cornes : à qui rend-il service, sur quoi agit-il, dans quel but.
- Pieuvre : fonctions principales (relient deux éléments du milieu extérieur par le produit) et
  fonctions contraintes.
- FAST : décomposition « pourquoi ? / comment ? » jusqu'aux solutions.
- SysML : exigences (req), cas d'utilisation (uc), séquence (sd), états (stm), activité (act),
  définition de blocs (bdd), blocs internes (ibd), paramétrique (par), paquetages (pkg).
- Chaîne d'information : acquérir, traiter, communiquer. Chaîne d'énergie : alimenter,
  distribuer, convertir, transmettre.

---

## 2. QUESTIONS TYPES

**QT1 — Vérifier les exigences SysML d'une pompe (E2 disciplinaire 2022, Q11–Q12)** :
$\eta_h = 11{,}2 \times 36 / (367 \times 2{,}8) = 39{,}2$ % > 35 %, $\eta_e = 2{,}2/2{,}8 = 78{,}6$ % > 75 %,
$H_a = 150$ mm > 100 mm : exigences satisfaites (corrigé officiel, rapport 2022 l.208–222).

**QT2 — Qualifier un convertisseur et le placer dans l'ibd (E2 disciplinaire 2022, Q21–Q22)** :
convertisseur DC-DC élévateur (hacheur parallèle) ; fonction « Convertir » ; flux d'énergie
électrique continue (rapport 2022 l.287–296).

**QT3 — Rendement global et exigence de puissance (exercice inédit)** :
$\eta_g = 0{,}97 \times 0{,}94 \times 0{,}96 = 0{,}875$ ; $P_a = 182{,}8$ kW > 180 kW, exigence non
satisfaite ; il faudrait un moteur à 95,5 % au moins.

---

## 3. ATTENTES DU JURY

> « Le jury constate une maîtrise inégale du langage de modélisation SysML permettant la
> description du système étudié. Les principaux diagrammes de SysML et les notions associées
> (type de relation, cardinalité, etc.) doivent être connus des candidats. »
> — Rapport_Jury_2018.md l.2875 (épreuve « Étude d'un système », option ingénierie informatique)

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Étage | Rendement typique |
|---|---|
| Onduleur, hacheur | 0,95 à 0,98 |
| Machine asynchrone / synchrone à aimants | 0,85 à 0,95 / 0,93 à 0,97 |
| Réducteur à engrenages (par étage) | 0,95 à 0,98 |
| Batterie lithium-ion (aller-retour) | 0,90 à 0,95 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **bdd et ibd** : confondre le diagramme de définition de blocs et le diagramme de blocs internes. Le bdd décrit les types de blocs et leurs relations ; l'ibd montre les parties d'un bloc, leurs ports et les flux qui circulent entre elles.
- **Composition et agrégation** : utiliser le losange vide pour une partie indissociable du système. La composition (losange plein) lie l'existence de la partie à celle du tout ; l'agrégation (losange vide) désigne une partie partageable ou amovible.
- **Relations entre exigences** : relier un essai à une exigence par «satisfy». Un bloc «satisfy» une exigence, un cas de test la «verify», «refine» la précise et «deriveReqt» en tire une exigence dérivée.
- **Cas d'utilisation** : décrire le fonctionnement interne dans le diagramme des cas d'utilisation. Il ne montre que les services rendus aux acteurs extérieurs ; le comportement interne relève des diagrammes de séquence, d'états ou d'activité.
- **Flux d'un ibd** : tracer des liaisons sans en préciser la nature. Chaque flux est d'énergie, de matière ou d'information et doit être orienté, ce que demandent les sujets (E2 2022 Q22, épreuve commune 2023 Q53).
- **Diagramme de séquence** : lire l'axe vertical comme une échelle de temps graduée. Il ordonne les messages sans les dater ; une contrainte de durée doit être notée explicitement.
- **Diagramme d'états** : confondre un état et une action. Un état dure dans le temps ; une transition est déclenchée par un événement et peut porter une garde et un effet.
- **Bête à cornes et pieuvre** : y faire figurer une solution technique. Ces outils expriment le besoin et les fonctions de service ; les solutions n'apparaissent que dans le FAST.
- **Rendement global** : additionner les pertes exprimées en pourcentage. Les rendements d'étages en série se multiplient : cinq étages à 0,9 donnent 0,59, et non 0,5.
- **Vérification d'une exigence** : conclure qu'une exigence est respectée sans la chiffrer. Une vérification compare explicitement la valeur obtenue à la valeur exigée et donne l'écart ou la marge.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

| Thème associé | Articulation |
|---|---|
| **T29 — Logique séquentielle** | Le diagramme d'états SysML décrit une machine à états ; GRAFCET et stm se répondent. |
| **T07, T09, T13 — Convertisseurs et machines** | Chaque bloc de la chaîne d'énergie a son rendement ; T32 les assemble. |
| **T33 — Informatique embarquée** | La chaîne d'information (acquérir, traiter, communiquer) s'implémente sur microcontrôleur et réseaux. |
| **T30 — Mesurage** | Vérifier une exigence suppose une mesure et son incertitude. |
