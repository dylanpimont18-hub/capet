# T29 — Logique séquentielle, GRAFCET
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

> **Note :** Le mot « GRAFCET » n'apparaît que deux fois dans les 41 fichiers Markdown : dans le tableau du programme au sein du sujet commun SII 2017 (référence au programme, pas une question sur le GRAFCET). Les questions sur la programmation d'automates (Siemens S7, Schneider M340) apparaissent sous forme d'**algorigramme/organigramme** et de **schéma électrique de câblage** — sans GRAFCET explicite. La logique séquentielle pure (bascules, machines à états) est **absente** des épreuves analysées.
>
> La section 1 présente le cours théorique complet du programme. Les sections 2 et 3 s'appuient sur les éléments trouvés dans les sources.

---

## 1. FORMULES ET COURS

### 1.1 Bascules (éléments mémorisants)

**Bascule RS (Set-Reset) :**

| $S$ | $R$ | $Q_{n+1}$ | Note |
|-----|-----|-----------|------|
| 0 | 0 | $Q_n$ | Mémorisation |
| 0 | 1 | 0 | Reset |
| 1 | 0 | 1 | Set |
| 1 | 1 | Interdit | — |

**Bascule D (Data) :** $Q_{n+1} = D$ (synchrone, sur front d'horloge)

**Bascule JK :**

| $J$ | $K$ | $Q_{n+1}$ |
|-----|-----|-----------|
| 0 | 0 | $Q_n$ |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | $\overline{Q_n}$ |

**Bascule T :** $Q_{n+1} = Q_n \oplus T$ (toggle si $T=1$)

### 1.2 Registres et compteurs

**Registre à décalage :** $n$ bascules D en cascade ; permet la conversion série/parallèle.

**Compteur binaire modulo $2^n$ :** $n$ bascules T ou JK en cascade ; compte de 0 à $2^n - 1$.

**Compteur BCD modulo 10 :** remise à zéro forcée lorsque la valeur atteint 10.

### 1.3 Machine à états (automate de Mealy / Moore)

**Définition :** un automate fini est un quintuplet $(Q, \Sigma, \delta, q_0, F)$ :
- $Q$ : ensemble fini d'états
- $\Sigma$ : alphabet d'entrée
- $\delta : Q \times \Sigma \to Q$ : fonction de transition
- $q_0$ : état initial
- $F$ : états d'acceptation

**Automate de Moore :** sorties ne dépendent que de l'état courant.
**Automate de Mealy :** sorties dépendent de l'état et des entrées.

### 1.4 GRAFCET (IEC 60848 / NF EN 61131-3)

**Éléments constitutifs :**
- **Étape** : rectangle numéroté, avec actions associées (actions continues, à impulsion)
- **Transition** : trait horizontal avec réceptivité (condition booléenne)
- **Liaison orientée** : flèche reliant étapes et transitions

**Règles d'évolution :**
1. L'**étape initiale** est active au démarrage (double rectangle)
2. Une transition est **franchissable** si toutes les étapes amont sont actives ET sa réceptivité est vraie
3. Le franchissement désactive les étapes amont et active les étapes aval
4. Plusieurs transitions franchissables simultanément le sont effectivement (simultanéité)

**Structures courantes :**

| Structure | Représentation |
|-----------|----------------|
| Séquence simple | étapes en série |
| Divergence OU (aiguillage) | plusieurs branches alternatives |
| Convergence OU (réunion) | plusieurs branches se rejoignent |
| Divergence ET (parallélisme) | double barre, branches simultanées |
| Convergence ET | double barre de synchronisation |
| Saut en avant / arrière | lien direct entre étapes non consécutives |

**Réceptivités typiques :**
- Condition sur entrée TOR : `capteur = 1`
- Temporisation : `t/étape X/durée T`
- Condition sur front montant : `↑ bouton`

### 1.5 Langages de programmation automate (IEC 61131-3)

| Langage | Type | Usage typique |
|---------|------|---------------|
| Ladder (LD) | Graphique | Logique de commande, contacts et bobines |
| Bloc fonctionnel (FBD) | Graphique | Blocs standard (PID, temporisateur…) |
| Liste d'instructions (IL) | Textuel | Bas niveau, proche assembleur |
| Texte structuré (ST) | Textuel | Algorithmie, calculs, conditions |
| Grafcet/SFC | Graphique | Séquencement, GRAFCET → SFC |

**Temporisateurs (Timer) :**
- TON (Timer ON-delay) : sortie active après délai si entrée maintenue
- TOF (Timer OFF-delay) : sortie active immédiatement, désactivée après délai
- TP (Timer Pulse) : sortie active pour une durée fixe

### 1.6 Câblage automate programmable industriel (API)

**Entrées TOR :** câblées en commun positif (source) ou commun négatif (sink).

**Sorties TOR :** relais ou transistor ; protégées par fusibles.

**Entrées analogiques :** typiquement 4–20 mA ou 0–10 V, convertisseur CAN interne (12 ou 16 bits signés).

**Câblage variateur — automate (source : sujets 2021, 2024) :**
- Sortie analogique de l'automate → borne de consigne du variateur (0–10 V ou 4–20 mA)
- Sortie TOR marche/arrêt → bornes LI1/LI2 du variateur
- Entrées TOR depuis le variateur : signal défaut (SD), disponible, etc.

### 1.7 Machines de Moore et de Mealy

*(complément du référentiel, 2026-11-10 — notion hors sujets 2013–2026 sauf mention)*

**Nombre minimal de bascules pour coder N états :**
$$n = \lceil \log_2 N \rceil$$
- Valable en codage binaire ; un codage « one-hot » utilise N bascules

---

## 2. QUESTIONS TYPES

> Les questions suivantes sont extraites de sujets réels ; elles mobilisent des compétences de la logique séquentielle (automate, câblage, algorithme), sans GRAFCET explicite.

**Q1.** (2021 — E2 Q.19–20) Réaliser les schémas de puissance et de commande du variateur ATV630 en complétant les documents réponses ; câbler le débitmètre, le capteur de pression, l'électrovanne et le pressostat aux modules d'entrées-sorties de l'automate M340.
*Compétence : câblage d'un API (Schneider M340) et d'un variateur.*

**Q2.** (2021 — E2 Q.24) Proposer un algorigramme du programme à écrire dans le bloc fonction « Contrôler le volume ». L'algorigramme doit faire apparaître les calculs nécessaires et les relations permettant de définir les sorties ($Rés\_plein$, $Rés\_vide$) en fonction de l'entrée.
*Compétence : algorithmie, structures conditionnelles (SI…ALORS).*

**Q3.** (2022 — E2 Q.14) Compléter le schéma électrique en y ajoutant les contacts SD (PRIMAIRE ALIM 24 Vcc et CONTROLEUR DE RÉSEAU TRI) afin de signaler des défauts vers le module TRT200.
*Compétence : schéma de commande, contacts de signalisation.*

**Q4.** (2017 — E1, programme) Décrire et analyser le comportement d'un système à l'aide d'un langage de description : graphe d'états, logigramme, GRAFCET, algorigramme.

**Q5.** (2024 — E2 Q.D, rapport jury) Déterminer les broches GPIO d'une carte de contrôle Raspberry Pi pour une liaison série avec un module GPS ; compléter le chronogramme d'un échange UART.
*Compétence : logique séquentielle appliquée aux protocoles de communication.*

**Q6.** (Transverse) Écrire en langage texte structuré (ST) ou sous forme d'algorigramme la gestion d'un système à deux états avec temporisation (modèle de base d'une machine à états).

---

## 3. ATTENTES DU JURY

D'après les rapports de jury 2021, 2022, 2023 :

- Le jury **déplore que les notions de base d'algorithmie ne soient pas maîtrisées** (rapport 2021). « Les candidats doivent acquérir des connaissances dans l'algorithmie et dans la réalisation de schémas électriques prenant appui sur de la documentation constructeur. »
- Un candidat au CAPET doit être capable de **câbler une entrée ou une sortie TOR/analogique d'un automate industriel** ainsi que **la partie commande d'un variateur de fréquence** (rapport 2021 : « ces notions sont largement accessibles à un étudiant de BTS »).
- Le jury attend la **maîtrise des langages de programmation de base** (algorigramme, texte structuré).
- La réalisation d'un schéma électrique de commande (variateur + automate) est un **point noir récurrent** : moyenne de 4,8/20 en 2021.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur observée |
|----------|----------------|
| Courant nominal moteur (calcul Ith variateur) | $I_{th} = 0{,}94 \times I_n$ (2021) |
| Courant nominal variateur ATV630 | 170 A (sujet 2021, moteur 90 kW) |
| Seuil pressostat/remplissage | $Rés\_plein$ à 95 % du volume max ; $Rés\_vide$ à 5 % |
| Vitesse de transmission UART | 115 200 bauds (sujet 2023) |
| Durée de transmission d'une trame de 71 caractères | $\approx 6{,}16$ ms à 115 200 bauds |
| Nombre de bits par caractère UART | 10 (1 start + 8 data + 1 stop) |
| Adressage modules E/S Siemens S7-1500 | entrées analogiques sur 16 bits signés (2024) |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **GRAFCET : franchissement simultané** de transitions — les transitions franchissables le même cycle le sont toutes simultanément.
- **Action d'étape vs réceptivité** : confusion fréquente entre ce qui se passe dans l'étape (action) et la condition pour quitter l'étape (réceptivité/transition).
- **Câblage variateur** : oublier le retour commun (GND 24 V) sur les entrées logiques LI du variateur.
- **Entrée analogique** : la plage 4–20 mA (et non 0–20 mA) permet la détection d'une coupure de fil (0 mA = défaut).
- **Algorigramme** : structures « POUR » vs « TANT QUE » — ne pas utiliser de boucle FOR là où un WHILE suffit.
- **Langage ST** : oublier le point-virgule en fin d'instruction ; confusion `:=` (affectation) et `=` (comparaison).
- **Timer TON** : la sortie $Q$ n'est active que si l'entrée reste vraie pendant la durée $PT$.
- **Moore et Mealy** : attribuer à une machine de Moore des sorties qui dépendent des entrées. Dans une machine de Moore, les sorties ne dépendent que de l'état ; si elles dépendent aussi des entrées, c'est une machine de Mealy.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T28 (logique combinatoire)** : la partie combinatoire d'un automate (équations de sortie et de transition) s'exprime par la logique de Boole.
- **T26/T27 (asservissement)** : la boucle d'asservissement est supervisée par l'automate (démarrage, arrêt, gestion des défauts, modes dégradés).
- **T30 (métrologie)** : les capteurs TOR et analogiques sont connectés aux entrées de l'automate ; la précision de la chaîne de mesure conditionne la qualité de la régulation.
- **T15/T16 (convertisseurs)** : le variateur de vitesse est l'actionneur piloté par l'automate ; connaître son câblage (partie puissance ET partie commande) est indispensable.
- **Informatique industrielle** : le texte structuré (ST) et l'algorigramme sont en continuité avec la programmation Python utilisée dans plusieurs sujets récents (2023, 2026).
