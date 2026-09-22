# T19 — AOP (amplificateur opérationnel)
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

### 1.1 Modèle de l'AOP idéal en régime linéaire
Un AOP parfait en régime linéaire vérifie les trois hypothèses (rappel présent dans les sujets 2024 et 2026) :
$$I_+ = 0 \quad ; \quad I_- = 0 \quad ; \quad \varepsilon = V_+ - V_- = 0 \implies V_+ = V_-$$

**Condition de fonctionnement linéaire :** la sortie est rebouclée sur l'entrée $«-»$ (contre-réaction négative). La sortie $V_s$ est bornée par les tensions d'alimentation : $-V_{cc} < V_s < +V_{cc}$.

### 1.2 Montage inverseur
$$\frac{V_s}{V_e} = -\frac{R_2}{R_1}$$

Gain en tension : $G = -R_2 / R_1$ (signe négatif = inversion de phase).

Impédance d'entrée : $Z_e = R_1$.

### 1.3 Montage non-inverseur
$$\frac{V_s}{V_e} = 1 + \frac{R_2}{R_1}$$

Gain toujours $\geq 1$, impédance d'entrée quasi infinie.

### 1.4 Montage suiveur (buffer)
$$V_s = V_e \quad \text{(cas particulier : } R_2 = 0, R_1 \to \infty \text{)}$$

Rôle : adaptation d'impédance — isole deux étages sans atténuation du signal.

### 1.5 Montage soustracteur (différentiel)
$$V_s = \frac{R_2}{R_1}(V_2 - V_1) \quad \text{si les quatre résistances sont appariées}$$

Utilisé pour amplifier une tension différentielle $e_{AB}$ issue d'un capteur de température (source : E1_Sujet_2024).

**Exemple sujets 2024 — transmetteur de température :**
- 1er sous-étage : $V_1 = G_1 \cdot e_{AB}$ avec $G_1 = (2R_1 + R_2)/R_2$
- 2e sous-étage : $G_2 = -100$
- 3e sous-étage : $G_3 = -1$
- Résultat global : $V_3 = G_1 \cdot G_2 \cdot G_3 \cdot e_{AB} = 340 \cdot e_{AB}$

### 1.6 Montage intégrateur
$$V_s(t) = -\frac{1}{RC} \int_0^t V_e(\tau)\,d\tau$$

Dans le domaine de Laplace :
$$H(p) = -\frac{1}{RC \cdot p}$$

Phase : $-90°$ à toutes les fréquences. Gain décroissant de $-20$ dB/décade.

### 1.7 Montage dérivateur
$$V_s(t) = -RC \cdot \frac{dV_e}{dt}$$

Dans le domaine de Laplace :
$$H(p) = -RC \cdot p$$

Phase : $+90°$. Gain croissant de $+20$ dB/décade (sensible au bruit).

### 1.8 Comparateur (fonctionnement non-linéaire)
Pas de contre-réaction négative. La sortie bascule entre $\pm V_{sat}$.

**Comparateur inverseur simple :** bascule quand $V_e > V_{ref}$.

**Comparateur à hystérésis (source : E2_Disciplinaire_IE_2023) :**
Contre-réaction **positive** sur l'entrée $«+»$. Deux seuils de basculement $V_{H}$ et $V_{B}$ :

$$V_+ = \frac{R_2 \cdot V_{ref} + R_1 \cdot V_s}{R_1 + R_2}$$

Pour $V_s = +V_{sat}$ : seuil haut $V_{H} = \frac{R_2 V_{ref} + R_1 V_{sat}}{R_1 + R_2}$

Pour $V_s = -V_{sat}$ : seuil bas $V_{B} = \frac{R_2 V_{ref} - R_1 V_{sat}}{R_1 + R_2}$

*Exemple numérique (E2_Disciplinaire_IE_2023) : $V_{ref2} = 2{,}42$ V, $V_{sat} = 15$ V, $R_1 = 1$ kΩ, $R_2 = 150$ kΩ.*

### 1.9 Conversion tension–courant (source : E1_Sujet_2024)
Montage permettant de produire un courant $I_s$ indépendant de la charge (résistance $R_{ana}$) :
$$I_s = \frac{V_4}{R_5}$$
avec $R_5 = 250$ Ω → plage $4$–$20$ mA pour $V_4 \in [1\,;\,5]$ V.

### 1.10 Montage de décalage (offset)
$$V_4 = V_3 + V_e \quad \text{(résultat par le théorème de Millman)}$$

Permet de translater un signal pour l'adapter à la plage d'un CAN ou d'un transmetteur normalisé.

---

## 2. QUESTIONS TYPES (max 6)

1. **(2024, E1–E2)** Écrire la loi des mailles impliquant $e_{AB}$, $\varepsilon_1$, $\varepsilon_2$ et $V_{R2}$. Montrer que $e_{AB} = V_{R2}$. Calculer numériquement le gain $G_1$.

2. **(2024, E4)** À l'aide du schéma de l'étage de décalage, montrer qu'en régime linéaire $V_4 = V_3 + V_e$.

3. **(2024, E9)** En utilisant la loi des nœuds au point A, exprimer le courant $I_s$ dans la résistance $R_{ana}$ et montrer qu'il est indépendant de $R_{ana}$.

4. **(2023, F6–F8)** Déterminer l'expression littérale de $V_+$ en fonction de $V_{ref2}$, $R_1$, $R_2$, $V_{s2}$. Calculer les seuils de basculement du comparateur à hystérésis.

5. **(2026, B4)** Exprimer la tension $v_T(t)$ en sortie du montage suiveur avec capteur $R_T$ et source de courant $I = 10$ mA. Mettre sous la forme $v_T = U_0(1 + aT)$ et expliquer le nom et le rôle du montage.

6. **(2026, B7–B8)** Identifier et justifier le choix du montage AOP (parmi inverseur, non-inverseur, soustracteur) pour réaliser l'amplificateur + conditionneur avec $v_A = c \cdot T$.

---

## 3. ATTENTES DU JURY

- **Connaître les trois conditions de l'AOP idéal** et les appliquer systématiquement sans les redémontrer ($V_+ = V_-$, $I_+ = I_- = 0$).
- **Distinguer régime linéaire et non-linéaire** : vérifier si la sortie est rebouclée sur $«-»$ avant d'appliquer $V_+ = V_-$.
- **Justifier le montage choisi** parmi les montages standards (suiveur, inverseur, non-inverseur, soustracteur) en expliquant son rôle fonctionnel (amplification, décalage, isolation).
- **Calculs numériques encadrés** avec unités. La simple application numérique d'une formule non justifiée ne rapporte pas de points.
- Le jury 2024 signale que la partie E (AOP) a été abordée par 70 % des candidats et traitée correctement par 47 % — résultat moyen qui traduit un manque de maîtrise des montages complexes (conversion T/I, décalage).
- Savoir utiliser le **théorème de Millman** pour les nœuds à plusieurs branches (appliqué en 2024, E4).

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Montage / Grandeur | Valeur typique |
|-------------------|---------------|
| Résistances inverseur 2024 | $R_1 = 1$ kΩ, $R_2 = 834{,}4$ Ω → $G_1 = 3{,}4$ |
| Gain 2e étage 2024 | $G_2 = -100$ |
| Gain 3e étage 2024 | $G_3 = -1$ |
| Gain total | $G = 340$ |
| Tension d'alimentation AOP | $\pm 15$ V (tensions de saturation $\pm 15$ V) |
| Plage sortie transmetteur courant | $4$–$20$ mA |
| Résistance $R_5$ convertisseur T/I | $250$ Ω |
| Seuil comparateur 2023 | $V_{ref} = 2{,}42$ V |
| Résistances hystérésis 2023 | $R_1 = 1$ kΩ, $R_2 = 150$ kΩ |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **Appliquer $V_+ = V_-$ sans vérifier la contre-réaction** : en mode comparateur (boucle ouverte ou contre-réaction positive), cette égalité est fausse.
- **Signe du gain inverseur** : oublier le signe $«-»$ et conclure à une amplification non-inverseuse.
- **Courants d'entrée non nuls** : certains candidats appliquent des lois de nœuds avec des courants $I_+$ ou $I_-$ non nuls — erreur fondamentale.
- **Confondre le suiveur (gain 1) avec un amplificateur** : le suiveur a pour rôle l'adaptation d'impédance, pas l'amplification.
- **Théorème de Millman** : méconnu de nombreux candidats ; savoir l'appliquer sur les nœuds à plusieurs admittances.
- **Hystérésis** : confondre les seuils montant et descendant, ou inverser les rôles de $R_1$ et $R_2$.
- **Conversion T/I** : ne pas comprendre pourquoi $I_s$ est indépendant de $R_{ana}$ (la boucle de contre-réaction maintient $\varepsilon = 0$).

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T18 — Composants** : l'AOP est souvent associé à des résistances et condensateurs pour former les montages de conditionnement ; la diode de protection des entrées AOP est analogue à la diode de protection CAN.
- **T20 — Filtres** : l'intégrateur est un filtre passe-bas du 1er ordre ; le dérivateur est un filtre passe-haut. Les filtres actifs associent AOP et cellules RC.
- **T21 — Fonctions de transfert** : la fonction de transfert d'un montage intégrateur est $H(p) = -1/(RCp)$ ; les montages AOP permettent d'implémenter un correcteur PI ou PID dans une boucle d'asservissement.
- **T06 — Chaîne d'acquisition** : l'AOP est au cœur du conditionneur (étage entre capteur et CAN) — thème récurrent dans tous les sujets E1 et E2 depuis 2019.
- **T05 — Capteurs** : PT100, thermocouple, capteur potentiométrique → tous conditionnés par des montages AOP.
