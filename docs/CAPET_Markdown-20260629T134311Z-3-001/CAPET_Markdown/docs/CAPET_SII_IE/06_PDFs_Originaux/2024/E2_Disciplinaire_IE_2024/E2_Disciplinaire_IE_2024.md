**EDE ENE 1** 

## **SESSION 2024** 

____ 

## CAPET 

# CONCOURS EXTERNE ET CAFEP CORRESPONDANT ET TROISIEME CONCOURS 

# **Section : SCIENCES INDUSTRIELLES DE L’INGÉNIEUR Option : INGÉNIERIE ÉLECTRIQUE** 

## **ÉPREUVE ÉCRITE DSICIPLINAIRE** 

## Durée : 5 heures 

____ 

_Calculatrice autorisée selon les modalités de la circulaire du 17 juin 2021 publiée au BOEN du 29 juillet 2021._ 

_L’usage de tout ouvrage de référence, de tout dictionnaire et de tout autre matériel électronique est rigoureusement interdit._ 

_Il appartient au candidat de vérifier qu’il a reçu un sujet complet et correspondant à l’épreuve à laquelle il se présente._ 

> _Si vous repérez ce qui vous semble être une erreur d’énoncé, vous devez le signaler très lisiblement sur votre copie, en proposer la correction et poursuivre l’épreuve en conséquence.  De même, si cela vous conduit à formuler une ou plusieurs hypothèses, vous devez la (ou les) mentionner explicitement._ 

**NB : Conformément au principe d’anonymat, votre copie ne doit comporter aucun signe distinctif, tel que nom, signature, origine, etc. Si le travail qui vous est demandé consiste notamment en la rédaction d’un projet ou d’une note, vous devrez impérativement vous abstenir de la signer ou de l’identifier. Le fait de rendre une copie blanche est éliminatoire.** 

A 

**Tournez la page S.V.P.** 

## **INFORMATION AUX CANDIDATS** 

Vous trouverez ci-après les codes nécessaires vous permettant de compléter les rubriques figurant en en-tête de votre copie 

Ces codes doivent être reportés sur chacune des copies que vous remettrez. 

## **► Concours externe du CAPET de l’enseignement public** : 

Concours Section/option Epreuve Matière EDE  1412E  101  9311 

## **► Concours externe du CAFEP/CAPET de l’enseignement privé** : 

Concours Section/option Epreuve Matière EDF  1412E  101  9311 

## **►Troisième concours externe du CAPET de l’enseignement public :** 

ConcoursSection/option Epreuve Matière EDV  1412E  101  9311 

‒ 2 ‒ 

EDE ENE 1 

## **Étude de l’extracteur d’air du pôle bois et menuiserie du lycée les Lombards de Troyes** 

Le fonctionnement d’une industrie comme celle du bois génère de nombreuses particules de natures différentes. Celles-ci sont nuisibles pour l’homme et pour l’environnement. Parmi ces particules, on retrouve la poussière en très grande quantité. Elle contient des composés pouvant provoquer de graves problèmes de santé, raison pour laquelle il est indispensable de trouver des solutions efficaces pour l’évacuer de manière adaptée. 

Chaque industrie en fonction de ses activités et des matières premières qu’elle utilise, peut avoir besoin d’une solution spécifique pour l’aspiration industrielle. Pour que la solution choisie soit efficace et adaptée aux besoins, il faudra prendre en compte : 

- le type de polluants concerné (il peut s’agir de poussières de verre, de bois, de farine, de plastique, ou encore de poussières métalliques) ; 

- la nature du (des) poste(s) à équiper. 

Dans le souci de préserver la santé des opérateurs des machines, la réglementation impose aux industriels de se doter de systèmes permettant de purifier l’air dans leurs locaux. 

L’étude porte sur un extracteur d’air (figure 1) équipant les locaux des salles de travaux pratiques du pôle bois et menuiserie (figure 2) du lycée les Lombards de Troyes. 

**Figure 1 : extracteur d'air** 

**Figure 2 : salle de travaux du CAP bois et menuiserie** 

B 

**Tournez la page S.V.P.** 

## **Problématique générale** 

Quelles sont les solutions technologiques permettant d’optimiser la consommation énergétique de l’extracteur d’air tout en assurant un fonctionnement conforme aux exigences du client et aux normes en vigueurs ? 

Ce sujet comporte cinq parties indépendantes abordant les problématiques suivantes : 

- **Partie A** : comment dimensionner le variateur et le moto-extracteur électriques afin d’optimiser la consommation énergétique de l’extracteur d’air ? 

- **Partie B** : comment vérifier la conformité de l’installation électrique vis-à-vis des normes ? 

- **Partie C** : comment optimiser le contrôle de la vitesse d’extraction d’air ? 

- **Partie D** : comment surveiller les températures des équipements de la chaine d’énergie ? 

- **Partie E** : comment mettre en forme le signal issu d’un capteur de température en vue de son traitement par un automate programmable ? 

‒ 2 ‒ 

## **Partie A : comment dimensionner le variateur et le moto-extracteur électriques afin d’optimiser la consommation énergétique de l’extracteur d’air ?** 

L'objectif de l’étude est de vérifier le dimensionnement de la motorisation utilisée pour entrainer les pales de l’extracteur d’air. 

Le principe de fonctionnement de l’extraction et du recyclage de l’air repose sur l’association d’un ventilateur et d’une machine asynchrone à vitesse variable et contrôlée **,** le descriptif est présenté sur la figure 3. 

**Figure 3 : synoptique de l’extraction et du recyclage de l’air** 

La première étape de l’étude consiste à dimensionner en puissance la pompe de l’extracteur d’air afin d’assurer le recyclage de l’air dans les conditions imposées par le client. Pour cela, le nombre de renouvellement par heure préconisé est égal à 10 (le volume total d’air de la pièce doit être renouvelé 10 fois par heure). Pour limiter le bruit, la vitesse de l’air dans les canalisations ne doit pas dépasser 5 ms[-1] . Le schéma de la figure 4 représente l’installation. L’extracteur doit permettre le renouvellement de l’air dans les deux salles du laboratoire. La salle 1 a un volume V1 = 2 500 m[3] alors que la deuxième salle a un volume V2 = 2 750 m[3] . 

**==> picture [258 x 123] intentionally omitted <==**

**----- Start of picture text -----**<br>
Canalisation<br>Extracteur d’air<br>poe1eee een. principale<br>| 1<br>I<br>.<br>Moteur  Ventilateur  i}.<br>asynchrone  centrifuge  i}<br>mmm me Salle 1   Salle 2<br>Volume  V1 = Volume  V2 =<br>2 500 𝑚𝑚 [3] 2 750 𝑚𝑚 [3]<br>**----- End of picture text -----**<br>


**Figure 4 : schéma de l'installation** 

‒ 3 ‒ 

**Tournez la page S.V.P.** 

- **A1 Calculer** les débits D1 et D2 respectivement dans les salles 1 et 2 en fonction des données imposées par le client. **En déduire** le débit total Dt dans la canalisation principale. 

Le réseau d'aspiration est constitué de nombreux coudes, tés, raccords et réductions qui augmentent fortement les pertes de charges des conduites. En tenant compte de la pression dynamique nécessaire pour mettre l'air en mouvement, l’extracteur doit alors exercer une pression totale p = 5 297 Pa. 

La puissance fournie par l’extracteur, notée Pextra , pour assurer le débit Dt s'exprime par : 

Pextra = ∆p × Dt avec Pextra en W, p en Pa et Dt en m[3] s[-1] . 

**A2 Calculer** la puissance Pextra et la puissance utile Pu du moteur asynchrone sachant que le ventilateur a un rendement ƞ = 0,78 . 

La seconde étape de l’étude vise à valider le choix de la motorisation au point de fonctionnement nominal. Le document technique DT1 précise le modèle de la machine asynchrone utilisé pour cette étude. La plaque signalétique du moteur asynchrone porte les indications suivantes : 

-  tension composée US = 400 V� soit une tension simple VS = 230 V ; 

-  courant nominal IS = 229 A� ; 

-  facteur de puissance cos φmot = 0,85 � ; 

-  fréquence d’alimentation du réseau f = 50 Hz� ; 

-  pulsation des grandeurs électriques ωs = 2π × f 

-  vitesse de rotation nominale N = 1 400 tr ⋅min[−1] ; 

-  nombre de paires de pôle p = 2. 

**A3** À l’aide du document technique DT1, **déterminer** l’expression littérale et **calculer** la vitesse des champs tournants vu du stator Ns en �tr ⋅min[−1] . **En déduire** la valeur du glissement nominal g . 

On note X la valeur efficace de la grandeur complexe X. 

**A4** À l’aide du document technique DT1, **exprimer** le courant Ir′ en fonction de R′R ′ Vs , Lf , ω𝑠𝑠 et . **Calculer** la valeur de Ir . g 

Dans la suite de l’étude on considère que Ir′ = 122 A et que le couple de pertes est constant et égal à Cp = 200 Nm . 

**A5** À l’aide du document technique DT1, **calculer** : - la puissance absorbée Pa ; 

- les pertes joules au rotor Pjr ; 

- les pertes mécaniques Ppm . 

‒ 4 ‒ 

**A6** À l’aide du document technique DT1, **en déduire** la valeur de la puissance utile Pu en sortie de la machine asynchrone. 

Pour la suite on pose Pu = 100 kW . 

- **A7 Valider** le choix de la motorisation en comparant le résultat obtenu à la question A2 et la valeur de Pu. 

Le document réponse DR1 représente les courbes suivantes : 

- évolution du couple utile Cu de la machine asynchrone en fonction de la vitesse de rotation de l’arbre Ω ; 

- évolution des couples aérodynamique Cv en fonction de Ω selon différentes valeur du diamètre, noté d, des pâles du ventilateur. 

On rappelle que la vitesse rotation nominal du moteur est N = 1400 tr ⋅min[−1] . 

- **A8** Sur le document réponse DR1, **placer** le point de fonctionnement nominal du moteur sur le courbe caractéristique Cu (Ω). **En déduire** le diamètre des pâles du ventilateur adapté au fonctionnement en régime établi. 

‒ 5 ‒ 

**Tournez la page S.V.P.** 

## **Partie B : comment rendre conforme l’installation électrique vis- à vis des normes ?** 

L’objectif de l’étude est d’identifier et de dimensionner les matériels requis pour garantir un transfert d’énergie de qualité et conforme à la norme. 

La figure 5 illustre l’installation électrique triphasée de l’atelier bois et menuiserie du lycée les lombards. L’atelier est alimenté par un réseau triphasé équilibré de tension composée Ur = 400 V et est constitué : 

- du moto-ventilateur de l’extracteur d’air dont les caractéristiques sont les suivantes : 

   -  tension composée Un = 400 V� soit une tension simple Vn = 230 V ; 

   -  courant nominal IS = 229 A� ; 

   -  facteur de puissance cos φmot = 0,85 � ; 

   -  fréquence d’alimentation du réseau f = 50 Hz� ; 

   -  pulsation d’alimentation ω = 2π × f . 

- d’ordinateurs et d’un automate de sécurité qui consomment une puissance électrique P0 = 1 kW avec un facteur de puissance cos φ0 = 1 � ; 

- du système d’éclairage et des équipements de l’atelier (groupe de perçage, brosses, chaines et scies) qui consomment une puissance active Pe = 43 kW et une puissance réactive Qe = 25,5 kVAR . 

**==> picture [397 x 237] intentionally omitted <==**

**----- Start of picture text -----**<br>
Réseau<br>Triphasé<br>400 V<br>Ordinateurs  Eclairage<br>MAS  +<br>+<br>Equipements<br>Automate<br>de sécurité<br>Extracteur<br>**----- End of picture text -----**<br>


## **Figure 5 : synoptique de l'installation de l’atelier bois et menuiserie** 

**B1 Calculer** , pour l’atelier, la puissance active totale Pcharge , la puissance réactive totale Qcharge et la puissance apparente totale Scharge . 

**B2 En déduire** le courant total absorbé noté Iabs , par cette installation ainsi que le facteur de puissance Fp . 

‒ 6 ‒ 

Pour la suite de l’étude on prend Pcharge = 178,3 kW et Qcharge = 108,7 kVAR . 

Le gestionnaire d’énergie impose un facteur de puissance compris entre 0,92 et 1. Pour cela, une batterie de condensateurs a été ajoutée en parallèle (un condensateur de capacité C par phase) de l’installation. 

Le dimensionnement des condensateurs de compensation d’énergie réactive est réalisé afin d’obtenir un facteur de puissance unitaire de l’ensemble de l’installation au point de fonctionnement nominal. 

**B3 Montrer** que l’expression permettant de calculer la capacité d’un condensateur à coupler en étoile et ramenant le facteur de puissance à 1 est : 

**==> picture [457 x 26] intentionally omitted <==**

## **B4 En déduire** la valeur de C pour compenser la puissance réactive. 

Dans la suite de l’étude, l’atelier équipé de la batterie de condensateurs est assimilé à une charge dont la puissance active est Pcharge = 178,3 kW et le facteur de puissance Fp = 1 . Le réseau électrique défini précédemment alimente l’atelier au travers d’une ligne triphasée de longueur X = 850 m via le secondaire du transformateur. Chaque fil de ligne est modélisé par l’association d’une résistance RL en série avec une inductance LL . Les câbles ont une résistance par unité de longueur Ru = 20 mΩ  km[−1] et une inductance par unité de longueur Lu = 1,2 mH  km[−1] . 

La figure 6 illustre le schéma équivalent de l’installation étudiée. Les grandeurs utilisées sur cette figure sont : 

- UD la valeur efficace de la tension composée tension au secondaire du transformateur considéré comme parfait ; 

- Ur la valeur efficace de la tension composée du réseau triphasé équilibré, alimentant l’atelier, Ur = 400 V ; 

- ∆U = UD −Ur la chute de tension composée ; 

- Itot la valeur efficace du courant dans un conducteur de phase. 

**==> picture [396 x 160] intentionally omitted <==**

**----- Start of picture text -----**<br>
∆𝑼𝑼<br>𝑅𝑅𝐿𝐿 𝐿𝐿𝐿𝐿 𝑰𝑰𝒕 𝒕𝒕<br>𝑼𝑼𝑫𝑫 𝑼𝑼𝒓𝒓 Pcharge =178,3 kW<br>F = 1<br>𝑝𝑝<br>Transformateur abaisseur parfait  Ligne équivalente Charge<br>**----- End of picture text -----**<br>


**Figure 6 : schéma équivalent du réseau électrique** 

‒ 7 ‒ 

**Tournez la page S.V.P.** 

- **B5 alculer** la résistance RL et l’inductance LL pour chaque fil de ligne de longueur =850 m. 

- **B6 Exprimer** et **calculer** la valeur efficace de l'intensité Itot du courant dans un conducteur de phase. 

Pour la suite, on pose Itot = 258 A . 

- **B7** Pour l'ensemble « réseau électrique et récepteur », **exprimer** et **calculer** la puissance active totale PT, la puissance réactive totale QT et la puissance apparente ST vue du secondaire du transformateur abaisseur parfait. 

- **B8 En déduire** la valeur efficace de la tension entre phases UD au secondaire du transformateur abaisseur ainsi que la chute de tension[∆] U en proportion de UD . 

- **B9** À l’aide du document technique DT2, **indiquer** si la valeur de ∆U est conforme à la norme NFC 15-100 sachant que le transformateur est du domaine public dans la catégorie « autres usages ». Dans le cas contraire, **proposer** une 

- ~~ee~~ solution pour diminuer la chute de tension. 

La suite de l’étude porte sur le fonctionnement du moto-extracteur en vitesse variable. L’objectif est de valider le choix d’une commande du variateur par MLI (Modulation de largeur d’impulsion) de l’onduleur au regard des impacts de compatibilité électromagnétique de celui-ci sur le reste du réseau. Le but est de calculer le taux de distorsion harmonique (THD) et de le valider vis-à-vis des exigences de la norme IEC/EN 61000-2-2. 

**==> picture [347 x 136] intentionally omitted <==**

**----- Start of picture text -----**<br>
Pont redresseur  Onduleur<br>Réseau  Cellule de filtrage<br>Moteur<br>triphasé<br>asynchrone<br>triphasé<br>𝑰𝑰𝒓𝒓 𝑰𝑰𝒔<br>M<br>VY= LC<br>Figure 7 : synoptique de la structure "variateur + moto-extracteur"<br>**----- End of picture text -----**<br>


La structure interne du variateur est présentée sur la figure 7. Il est constitué : 

- d’un pont redresseur, celui-ci génère des harmoniques sur le réseau ; 

- d’une cellule de filtrage ; 

- d’un onduleur commandé afin de piloter en vitesse la machine asynchrone. 

‒ 8 ‒ 

Les simulations réalisées sont présentées sur le document technique DT3. Deux cas d’études sont présentés : 

- le cas 1 où le variateur de vitesse est commandé en pleine onde ; 

- le cas 2 où le variateur de vitesse est commandé par MLI avec une fréquence de la porteuse fp = 6 000 Hz . 

On rappelle que le taux de distorsion harmonique (THD) est déterminé par la formule : 

**==> picture [155 x 34] intentionally omitted <==**

avec : 

- I1 : valeur efficace du fondamental du courant 

- I2 , �I3 , I4 , …, In valeurs efficaces des harmoniques du courant 

**B10** À l’aide du document technique DT3, **calculer,** à l’aide du fondamental et des harmoniques de rang 3, 5, 7 et 9 **,** le THD du courant réseau Ir dans les deux cas. 

La norme IEC/EN 61000-2-2 fixe un THD de courant inférieur à 25 % pour assurer une compatibilité électromagnétique conforme. 

**B11 Conclure** dans les deux cas sur la qualité du signal Ir vis-à-vis de l’exigence fixée par la norme IEC/EN 61000-2-2. 

**B12** À l’aide du document technique DT3, **commenter** la conséquence de la mise en place d’une MLI sur la décomposition spectrale du signal Ir . **Proposer** une solution pour pallier ce problème. 

**B13** À partir des résultats précédents, **justifier** le choix d’une commande MLI pour le pilotage du variateur de vitesse. 

‒ 9 ‒ 

**Tournez la page S.V.P.** 

**Partie C : Comment optimiser le contrôle de la vitesse d’extraction de l’air ?** 

L’objectif de cette partie est de définir une stratégie de commande permettant d’assurer le pilotage en vitesse de la motorisation. 

On suppose que le point de fonctionnement nominal de la vitesse N se trouve dans la zone de linéarité. La figure 8 décrit le principe de la commande scalaire (asservissement en vitesse) de la motorisation. Pour cela un capteur de vitesse mesure la vitesse instantanée Ω et la compare à une consigne de vitesse Ωréf . L’écart entre la consigne et la vitesse réelle permet d’établir la commande de pulsation des champs statoriques ωsref via un correcteur. 

**==> picture [320 x 135] intentionally omitted <==**

**----- Start of picture text -----**<br>
Variateur  Ω<br>De  MAS<br>Capteur de<br>Vitesse  vitesse<br>𝝎𝝎𝒔𝒔𝒓 𝒓𝒓 Correcteur  -  +  Ω𝒓 𝒓𝒓<br>Tob<br>Figure 8 : schéma de l'autopilotage de la motorisation<br>**----- End of picture text -----**<br>


- Le modèle de la machine asynchrone et les équations associées sont indiquées dans le document technique DT1. L’étude sera faite pour un glissement faible ( g ≈0) . **C1** À l’aide des équations 1 et 2 du document technique DT1 et de l’hypothèse d’un faible glissement, **montrer** que le couple Cem peut se mettre sous la forme 2 

- 3p Vs 

- Cem = Rr[′] × (ωs) ω𝑠𝑠 × g . 

- **C2** À l’aide du document technique DT1, **mettre** l’équation précédente sous la forme Cem = A  ωr avec ωr la pulsation des champs au rotor. **Donner** l’expression de A ′ 

- ~~——~~ en fonction de p, Vs, Rr  et ωs . **C3 Montrer** que l’équation 3 du document technique DT1 peut s’exprimer dans le domaine de Laplace (à conditions initiales nulles) sous la forme : K𝑚 𝑚 

- Ω(p) = [Cem(p) −Cr(p)] . 1+τmeca 

- **Exprimer** Kmeca et τ𝑚 𝑚 en fonction de J et f. **Déterminer** les valeurs numériques Kmeca et τmeca . 

- **C4** À partir de l’équation 2 du document technique DT1 et des résultats précédents, **compléter** le document réponse DR2 illustrant le modèle scalaire de la 

- ~~—~~ motorisation asynchrone dans le domaine de Laplace. ‒ 10 ‒ 

La suite de l’étude porte sur le dimensionnement du correcteur qui assure l’asservissement en vitesse de la motorisation. La figure 9 illustre la modélisation de Kmeca la boucle de vitesse. Pour la suite de l’étude, on considère que Hm(p) = . 1+τmecap 

**==> picture [299 x 82] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑯𝑯𝒎𝒎(𝒑𝒑) Ω(𝒑𝒑)<br>𝑲𝑲𝒑𝒑 -  +  𝑲𝑲𝒑𝒑𝒊𝒊 -  +  Ω𝒓 𝒓𝒓(𝒑𝒑)<br>**----- End of picture text -----**<br>


**Figure 9 : modélisation de la boucle d’asservissement de vitesse** 

Ω(p) **C5 Déterminer** la fonction de transfert Hbf(p) = en fonction de Ω𝑟 𝑟𝑟(p) Kp, Ki, Kmeca et τmeca . **Mettre** l’expression obtenue sous la forme canonique : 1 Hbf(p) = . 1+[2m] p+[1] p[2] ω0 ω0[2] 

**C6 Déterminer** l’expression de m et de ω0 en fonction de Kp, Ki, Kmeca et τmeca . 

**C7** À l’aide du théorème de la valeur finale, **montrer** que l’erreur statique de la boucle de vitesse est nulle lorsque l’entrée est un échelon de vitesse d’amplitude Ω0 . 

Pour la suite du problème on pose : 

- l’amortissement m=1 ; 

- le temps de réponse Tr (en s) = 1 s 

- 5 

- - la pulsation propre ω0(en rad  s[−1] ) = . Tr 

- avec Kmeca = 250 et τmeca = 8,5 s . 

**C8 Exprimer** les gains KP et Ki représentés figure 9 en fonction de m, Kmeca, τmeca et ω0 . **Déterminer** les valeurs numériques de KP et Ki. 

Les performances de l’autopilotage sont étudiées dans un premier temps pour une situation parfaite dans laquelle la génération de ωs à partir de ωsref se fait instantanément soit ωs = ωsref . 

Dans la suite de l’étude on considère que la consigne de vitesse est un échelon d’amplitude Ω0 . 

**C9** À l’aide du document technique DT4, **déterminer** l’erreur statique εs1 et le dépassement relatif D1 de la boucle de vitesse dans le cas où ωs = ωsref . 

‒ 11 ‒ 

**Tournez la page S.V.P.** 

La marge de phase correspond à la différence entre la phase pour un gain de 0 dB et 180°, soit Mφ = Arg(Hbf(0dB)) + 180° . La fonction Arg représente l’argument de Hbf(p) . 

**C10** À l’aide du document technique DT4, **déterminer** la marge de phase Mφ1 de la boucle de vitesse. 

Les exigences fixées par le cahier des charges sont : 

- un dépassement D% ≤5 %� ; 

- une erreur statique sur la boucle de vitesse εv nulle ; 

- une marge de phase Mφ ≥90°� . 

**C11 Conclure** sur les performances de la motorisation au regard des exigences fixées par le cahier des charges dans le cas où ωs = ωsref . 

Dans un second temps, il faut prendre en compte le régime transitoire du variateur de 1 vitesse tel que ωs = ωsref . 1+τvvp 

**C12** À l’aide du document technique DT5, **évaluer** dans cette situation : - l’erreur statique εs2 ; - le dépassement relatif D2 ; - la marge de phase Mφ2 . 

**C13 Conclure** sur les performances de la motorisation au regard des exigences 1 fixées par le cahier des charges dans le cas où ωs = ωsref . 1+τvvp 

‒ 12 ‒ 

**Partie D : Comment surveiller les températures des équipements de la chaine d’énergie ?** 

L’objectif est d’établir la constitution matérielle et logicielle de la chaine d’information assurant la régulation de la température de l’armoire électrique du variateur de vitesse. 

L’automate utilisé pour la gestion de la sécurité des équipements et la surveillance des températures est un Siemens S7-1500. 

Celui-ci est accompagné d’un module d’alimentation ainsi que de quatre modules d’entrées/sorties (E/S « tout ou rien » et analogiques). 

Parmi les fonctions de sécurité attribuées à l’automate, on retrouve également la surveillance les températures des éléments de la distribution en énergie : le redresseur, la cellule de filtrage, le moteur de l’extracteur mais aussi les températures intérieures et extérieures du bâtiment. Le diagramme des exigences de la figure 10 présente l’ensemble des fonctionnalités. 

**==> picture [27 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
:<br>i<br>:<br>:<br>i<br>IdText= "2"<br> =""<br>**----- End of picture text -----**<br>


**==> picture [63 x 67] intentionally omitted <==**

**----- Start of picture text -----**<br>
eextendedRequiremento|<br>Mesurer<br> les débits<br>Id="2.1"<br>reste *s Debits dans<br>les canalisations<br>+ Débits amont et<br>aval fitres"<br>**----- End of picture text -----**<br>


**Figure 10 : diagramme des exigences** 

‒ 13 ‒ 

**Tournez la page S.V.P.** 

Le diagramme de définition des blocs de la figure 11, détaille les composants utilisés pour la surveillance de la température de l’armoire électrique contenant le variateur de vitesse de l’extracteur d’air. 

**==> picture [25 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
system<br>Siemens<br>its<br>=<br>**----- End of picture text -----**<br>


**Figure 11 : diagramme de définition des blocs** 

## **1 - Typologie des capteurs de température** 

Les capteurs utilisés pour les mesures de l’ensemble des températures sont de type thermocouple. 

## _Principe de fonctionnement :_ si on réunit à 

une extrémité (jonction) deux fils métalliques de natures différentes et que l'on élève la température de cette extrémité, il apparaît une tension eAB aux extrémités restées libres (figure 12). 

**==> picture [279 x 57] intentionally omitted <==**

**----- Start of picture text -----**<br>
Soudure à<br>I Métal A<br>la jonction<br>\<br>eAB \<br>\<br>Métal B<br>**----- End of picture text -----**<br>


**Figure 12 : principe de fonctionnement du thermocouple** 

‒ 14 ‒ 

Il est possible de déterminer la température de l'extrémité à partir de la mesure de la tension eAB. 

La figure 13 présente les caractéristiques en fonction du type de thermocouple : 

|**Type**|**Plage de**<br>**mesure**<br>**conseillée**<br>**en°C **|**Alliages**|**Tolérance**<br>**(°C)**|**Comparaison**<br>**qualitative**<br>**des Prix**|**Fiabilité**<br>**Durée de vie**<br>**maintenance**|
|---|---|---|---|---|---|
|T|-200 à 350|Cuivre et<br>Constantan|+/-1|Très élevé|Répétabilité<br>exceptionnelle<br>de +/-0,1 °C<br>de<br>−200 à 200°C|
|K|-10 à 1 100|Chromel et<br>Alumel|+/- 2,5|Faible|Stabilité moins<br>satisfaisante<br>que d'autres<br>thermocouples|
|N|0 à 1250|Nicrosil et<br>Nisil|+/- 2,5|Très élevé|Stabilité<br>supérieure aux<br>autres<br>thermocouples<br>courants|
|J|-30 à 700|Fer et<br>Constantan|+/- 1,5|Élevé|S’oxyde<br>rapidement en<br>milieuhumide|
|E|0 à 800|Chromel et<br>Constantan|+/- 2|Élevé|Thermocouple<br>à la FEM1la<br>plus élevée|



**Figure 13 : caractéristiques en fonction du type de thermocouple** 

**D1** À l’aide des figures 10 et 13, **justifier** le choix d’un type J pour les capteurs de température thermocouple. 

## **2 – La chaine d’acquisition** 

La figure 14 présente les composants qui constituent la chaine d’acquisition de la température à l’intérieur de l’armoire électrique (TARM) vers l’automate programmable. 

> 1 FEM : Force Électro-Motrice 

‒ 15 ‒ 

**Tournez la page S.V.P.** 

Température dans l’armoire électrique : TARM 

**==> picture [505 x 162] intentionally omitted <==**

**----- Start of picture text -----**<br>
Capteur de température<br>Automate S7-1500<br>TT étalonné sur la  Module d’entrées<br>plage :  analogiques  Programme<br>Is : 4-20mA  Mot PIW8  Mot MW8<br>automate<br>2 fils   -20        200°C  4 fils  utilisateur<br>Entrée CH2<br>Transmetteur de Température<br>          (Référence : KOS 839)<br>**----- End of picture text -----**<br>


## **Figure 14 : chaîne d’acquisition de la température à l’intérieur de l’armoire électrique** 

Le transmetteur de température nommé « TT » convertit la tension (de l’ordre du millivolt) du capteur thermocouple en un signal de sortie normalisé, ici un courant 4 – 20 mA compatible avec le module d’entrée analogique de l’automate. 

Le document technique DT6 présente la documentation du transmetteur de température de référence « KOS 839 ». 

- **D2** À l’aide des documents techniques DT6, **compléter** le schéma de raccordement entre la sonde de température et le transmetteur de température TT, du document réponse DR3. 

Les documents techniques DT7 et DT8 présentent le module d’entrée analogique de référence « AI 8xU/I/RTD/TC ST ». 

- **D3** À l’aide des documents DT6 et DT7, **compléter** le schéma de raccordement entre le transmetteur de température TT et le module d’entrées analogiques sur le document réponse DR3. 

- **D4** À l’aide de la figure 14, **compléter** le document réponse DR4 afin de caractériser les valeurs d’entrée/sortie de la fonction de transfert Is = f(TARM) du transmetteur. **Préciser** l’unité employée. 

- **D5** À l’aide du document technique DT6, **compléter** le tableau de configuration du switch S1 du transmetteur de température sur le document réponse DR4. 

‒ 16 ‒ 

L'automate possède une mémoire interne lui permettant de stocker des variables. Une adresse mémoire codée sur 2 octets est allouée à chaque entrée, sortie et mot interne. Par exemple, MW8 est un mot interne permettant des traitements numériques via la programmation automate. 

Toutes les entrées / sorties analogiques commencent par un « P » : 

   - PIWi pour les entrées 

   - PQWj pour les sorties 

- **D6** À l’aide du document technique DT8, **indiquer** sur combien de bit est codée une entrée analogique, **préciser** le rôle du bit de poids fort. 

- **D7** À l’aide de la figure 14, **compléter** le tableau du document réponse DR4 permettant de connaître la valeur décimale du mot PIW8 en fonction du courant Is mesuré. 

- **D8 Compléter** et **dessiner** la caractéristique PIW8=f(Is) dans la zone de fonctionnement du transmetteur de température du document réponse DR5. 

MW8 est un mot interne à l’automate, il doit permettre de connaître la valeur de la température mesurée par le capteur de température en °C. Un calcul de « mise à l’échelle » entre les mots PIW8 et MW8 doit être élaboré dans le programme automate utilisateur. 

La caractéristique de la valeur décimale du mot mémoire MW8 en fonction de la valeur décimale du mot PIW8 est donnée sur le document réponse DR5 **.** 

- **D9 Compléter** le document réponse DR5 en indiquant les valeurs caractéristiques (PIW8min, PIW8max, MW8min et MW8max) dans la zone de fonctionnement du transmetteur de température. 

- **D10** En utilisant les noms des variables, **déterminer** l’équation de la droite traduisant l’évolution MW8 = f(PIW8) du document réponse DR5. **Déterminer** la forme numérique de cette équation en remplaçant les variables par leurs valeurs numériques. 

- **D11 Montrer** que l’équation de « mise en forme » permettant de connaître la valeur de la température mesurée en °C, en fonction de la valeur du mot PIW8 et de l’étendue de mesure E s’écrit : 

E  MW8 = f(E, PIW8) = PIW8 -20. 27 648 

‒ 17 ‒ 

**Tournez la page S.V.P.** 

## **3 - Principe de fonctionnement du ventilateur au niveau du tableau électrique qui contient le variateur de vitesse** 

Un système de ventilation est enclenché si la température mesurée dans le tableau est supérieure aux consignes. Il fonctionne selon le principe suivant : 

- si la température est inférieure à 35°C, pas de ventilation, 

- si la température est supérieure à CB=35°C alors le ventilateur est enclenché en petite vitesse (PV), 

- si la température est supérieure à CH=50°C alors le ventilateur est enclenché en grande vitesse (GV). 

Un exemple de profil de température est donné figure 15. Il permet également de voir la vitesse du ventilateur en fonction du temps et de la température. 

**Figure 15 : exemple traduisant le fonctionnement du ventilateur** 

Deux voyants permettent de visualiser la vitesse de fonctionnement du ventilateur : 

   - VPV pour un fonctionnement du ventilateur en petite vitesse 

   - VGV pour un fonctionnement en grande vitesse 

- E ~~⋅~~ 

- **D12** En utilisant l’équation MW8 = PIW8 - 20 , **isoler** la variable PIW8 et 27 648 

- **déterminer** la valeur décimale du mot PIW8 pour les valeurs de température CB et CH. 

**D13** Sur le document réponse DR6, **compléter** le schéma en portes logiques traduisant le fonctionnement du ventilateur. 

‒ 18 ‒ 

## **4 - Sous-programme de « mise à l’échelle »** 

Le sous-programme de « mise à l’échelle » est appelé par le programme principal de l’automate et gère la mise à l’échelle de l’entrée analogique en température (°C). Il s’agit de gérer le pilotage du ventilateur et de restituer une information à l’usager par le biais d’un voyant. 

Au départ, si l’entrée analogique envoie une valeur en dehors des valeurs limites alors un voyant de « défaut mesure » est enclenché et MW8 prend la valeur zéro. Dans le cas contraire, l’algorithme calcule la valeur de MW8 en degré Celsius (°C) en appliquant la formule : 

**==> picture [137 x 26] intentionally omitted <==**

La figure 16 illustre les mnémoniques et adressages utilisés par l’automate programmable. 

|**Adresses**|**Mnémoniques**|**Description**|
|---|---|---|
|PWI8|entree_ana|Valeur brute de la mesure sur l’entrée analogique<br>correspondante|
|MW8|mesure|Valeur de la température en°C|
|MW12|def_mesure|Valeur binaire d’un défaut de mesure : 1⇒Défaut,<br>0⇒Pas de défaut|
|MW14|etendue|Valeur décimale de l’étendue de mesure en°C|
|MW16|CB|Valeur décimale de la consigne de température<br>basse|
|MW18|CH|Valeur décimale de la consigne de température<br>haute|
|Q0.1|PV|Sortie TOR utilisée pour alimenter le ventilateur en<br>«Petite Vitesse»|
|Q0.2|GV|Sortie TOR utilisée pour alimenter le ventilateur en<br>«GrandeVitesse»|
|Q0.3|VPV|Voyantventilationen PetiteVitesse|
|Q0.4|VGV|Voyant ventilation en Grande Vitesse|



**Figure 16 : tableau des mnémoniques et adressages utilisés** 

Les mots MW16 et MW18 sont respectivement utilisés pour se laisser la possibilité de modifier les valeurs de CB et CH. De même, le mot MW14 permet de modifier l’étendue de mesure. 

**D14** Sur le document réponse DR7, **compléter** l’algorigramme de fonctionnement du sous- programme de « mise à l’échelle » en utilisant les mnémoniques indiqués sur la figure 16. 

‒ 19 ‒ 

**Tournez la page S.V.P.** 

## **5 – Gestion de la vitesse du ventilateur** 

La figure 17 illustre le schéma de câblage du moteur pilotant le ventilateur de refroidissement de l’armoire électrique. 

## **Figure 17** : **schéma du moteur asynchrone monophasé à 2 vitesses pour la gestion PV (petite vitesse) et GV (grande vitesse) du ventilateur** 

Le condensateur Cp, en série avec l’enroulement auxiliaire, produit le déphasage nécessaire au lancement du moteur, il reste sous tension en permanence. Les deux enroulements principaux permettent de choisir la grande vitesse (GV) ou la petite vitesse (PV). Deux relais 24 V continu, KA1 et KA2 sont prévus pour l’alimentation du moteur du ventilateur. 

**D15** Dans le cas où le contact KA1 de la figure 17 est fermé (KA2 ouvert), **dessiner** le schéma équivalent de l’alimentation du moteur du ventilateur. 

**D16** Dans le cas où le contact KA2 de la figure 17 est fermé (KA1 ouvert), **dessiner** le schéma équivalent de l’alimentation du moteur du ventilateur. 

**D17 Indiquer** , pour chaque cas, si le moteur est en grande vitesse ou en petite vitesse. **Justifier** la réponse. 

Sur le document réponse DR8 sont donnés : 

- le schéma partiel de la carte de sortie TOR de l’automate 

- les relais 24 V continu de commande de vitesse du moteur du ventilateur 

- les voyants de signalisation 24 V continu 

‒ 20 ‒ 

La figure 18 illustre les affectations de la carte de sortie TOR de l’automate programmable. 

|**Adresses**|**Mnémoniques**|**Descriptions**|
|---|---|---|
|Q0.0|defaut_mesure|Voyant de«défaut mesure»hors étendue de mesure|
|Q0.1|PV|Sortie TOR utilisée pour alimenter le ventilateur en<br>«Petite Vitesse»|
|Q0.2|GV|Sortie TOR utilisée pour alimenter le ventilateur en<br>«Grande Vitesse»|
|Q0.3|VPV|Voyant ventilation en Petite Vitesse|
|Q0.4|VGV|Voyant ventilation en Grande Vitesse|
|Q0.5|NC|Non connecté|
|Q0.6|NC|Non connecté|
|Q0.7|NC|Non connecté|



**Figure 18** : **affectations de la carte de sorties TOR** 

**D18 Compléter** le document réponse DR8 afin que le câblage des voyants de signalisation soit conforme aux affectations de la figure 18. 

Un verrouillage électrique est à prévoir entre les relais KA1 et KA2 afin d’empêcher l’alimentation simultané des deux relais. 

**D19 Compléter** le document réponse DR8 afin de proposer un raccordement des relais de commande de la ventilation. 

Le document technique DT9 présente les symboles utilisés pour la programmation de l’automate Siemens S7-1500. 

**D20 Compléter** le document réponse DR9 permettant de programmer la commande des voyants VPV et VGV. 

Les équations logiques qui permettent la commande en vitesse du moteur du ventilateur sont les suivantes : 

̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ - #PV = ( #CB < #mesure ) . ( #mesure > #CH ) - #GV = #mesure > #CH 

**D21 Compléter** le document réponse DR9 permettant de programmer la commande du ventilateur en petite et grande vitesse. 

‒ 21 ‒ 

**Tournez la page S.V.P.** 

## **Partie E : comment mettre en forme le signal issu d’un capteur de température en vue de son traitement par un automate programmable ?** 

L’objectif est de vérifier la chaine de conversion du transmetteur de température utilisé pour la régulation de la température au niveau de l’armoire électrique du variateur de vitesse. 

La figure 19 présente un synoptique du transmetteur de température identifiant la nature des signaux en entrée et en sortie de celui-ci. Il s’agit de convertir une tension 

eAB de quelques millivolts en entrée en un courant de sortie Is compris entre 4 et 20 mA compatible avec l’entrée analogique de l’automate. La plage de mesure de température est comprise entre -20 à 200 °C. 

**==> picture [454 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
Capteur de<br>température type<br>thermocouple<br>TT étalonné sur la<br>Vers module<br>plage :<br>eAB : Millivolts  Is : 4-20 mA  d’entrées<br>2 fils   -20°C         200°C  4 fils  analogiques de<br>l’automate<br>Entrée  Sortie<br>L S<br>Transmetteur de Température<br>**----- End of picture text -----**<br>


**Figure 19 : synoptique du transmetteur de température** 

Les caractéristiques des grandeurs eAB et Is en fonction de la température sont présentés dans le document technique DT10. On considère que les profils sont linéaires. 

La figure 20 présente le schéma fonctionnel interne du transmetteur de température. Il permet de distinguer 3 étages distincts permettant la résolution de la problématique de conversion. 

**==> picture [505 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
Is<br>Amplifier  Décaler  Convertir<br>eAB ( x Gain )  GeAB ( + Vd )  GeAB +Vd  Tension en Courant<br>A T y<br>Figure 20 : schéma fonctionnel interne du transmetteur de température<br>‒ 22 ‒<br>**----- End of picture text -----**<br>


On suppose que les amplificateurs opérationnels (AOP) sont parfaits et qu’ils fonctionnent en régime linéaire. 

## _Rappel sur les amplificateurs opérationnels en régime linéaire :_ 

Si la sortie de l’AOP est rebouclée sur l’entrée « - » alors on dit que l’AOP fonctionne en mode linéaire et on a : 

**==> picture [120 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
  Exemple de schéma<br>**----- End of picture text -----**<br>


**==> picture [386 x 148] intentionally omitted <==**

**----- Start of picture text -----**<br>
 I [+]  = 0  +Vcc<br>I [-]<br> I [-]  = 0<br>-<br> ε  = 0 V soit V [+]  = V  [-] ε<br>+<br>V [-] I [+]<br>V [+] -Vcc  Vs<br>fa I<br>**----- End of picture text -----**<br>


+Vcc et -Vcc sont les tensions d’alimentation de l’AOP. Les alimentations, qui ne font pas partie de l’étude, ne sont pas représentées dans les schémas de montage représentés dans la suite de l’étude. 

## **1. Étude de l’étage d’amplification** 

La figure 21 illustre les différents sous-étages constituant l’étage d’amplification du transmetteur de température. 

**==> picture [486 x 38] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 [ère]  amplification  2 [ème]  amplification  3 [ème]  amplification<br>eAB V1 V2 V3<br>Gain G1 Gain G2 = -100  Gain G3 = -1<br>**----- End of picture text -----**<br>


**Figure 21 : constituants de l’étage d’amplification** 

Dans le premier sous-étage d’amplification, la tension eAB issue du capteur de température est amplifiée pour aboutir à une tension V1. Le montage de ce sous-étage est illustré par la figure 22. 

‒ 23 ‒ 

**Tournez la page S.V.P.** 

**==> picture [103 x 39] intentionally omitted <==**

**----- Start of picture text -----**<br>
Valeurs :<br>-<br>R1 = 1 kΩ,<br>-<br>R2 = 834,4 Ω<br>**----- End of picture text -----**<br>


**Figure 22 : schéma de montage de la première amplification** 

**E1** À l’aide de la figure 22, **écrire** la loi des mailles impliquant eAB, 𝜀𝜀 1, 𝜀𝜀 2 et VR2 et ~~ee~~ **montrer** que eAB = VR2. V R2  ( 2R1 + R2 ) **E2** Sachant que V1 = , **calculer** numériquement le gain G1 permettant R2 d’écrire la tension V1= G1VR2 = G1eAB. ~~ne~~ Conformément à la figure 21, la tension V1 est encore amplifiée par deux étages successifs. 

**E3** À l’aide de la figure 21, **exprimer** la relation entre eAB, G1, G2, G3 et V3 puis ~~ee~~ **exprimer** numériquement V3 en fonction de eAB. 

## **2. Étude de l’étage de décalage en tension** 

La tension V3 fait office d’entrée pour le montage illustré figure 23. La tension V4 produite par ce montage correspond à un décalage en tension de V3. 

**==> picture [170 x 167] intentionally omitted <==**

**----- Start of picture text -----**<br>
Le théorème de Millman donne<br>les relations :<br>V3<br> + [Ve]<br>R R<br>V [+]  =  2<br>R<br>[V4]<br>R<br>V  [-]  = 2<br>R<br>**----- End of picture text -----**<br>


**Figure 23 : schéma de montage de l’étage de décalage en tension** 

‒ 24 ‒ 

**E4** À l’aide de la figure 23, **montrer** que, en régime linéaire, la tension V4 vérifie la relation V4 = V3 + Ve. **En déduire** la relation entre V4 et eAB. 

⋅ On donne Ve = 1,34 V ainsi que la relation V4 = 337,7 eAB + 1,34 

**E5** À l’aide du document technique DT10, **calculer** V4 pour les deux tensions extrêmes de eAB puis **compléter** le document réponse DR10. 

## **3. Étude de l’étage de conversion tension en courant** 

La tension V4 fait office d’entrée pour le montage illustré figure 24. Le courant Is produit par ce montage est le résultat de la conversion de la tension V4. 

**Figure 24 : schéma de montage pour la conversion de V4 en un courant Is** 

- **E6** À l’aide de la figure 24, **déterminer** les relations entre I2 et I2’ puis entre I1 et I1’. 

- **E7** En utilisant la loi des mailles dans la boucle 1* illustrée figure 24, **déterminer** la relation liant V4, I2, R5, Is et Rana. **En déduire** l’expression de I2 en fonction de V4, R5, Is, Rana. 

**E8** En utilisant la loi des mailles dans la boucle 2* illustrée figure 24, **déterminer** la relation liant ε , I1’, R5, I3 puis **montrer** que I3 = I1. 

−[R][ana][][I][s] L’expression du courant I1 est la suivante : I1 = avec R5 = 250 Ω. R5 

**E9** En utilisant la loi des nœuds au point A illustré figure 24, **exprimer** le courant Is dans la résistance Rana et **montrer** qu’il est indépendant de Rana. 

**E10 Calculer** Is pour V4=1 V puis pour V4=5 V et **conclure** quant à la conformité du transmetteur de temp 

‒ 25 ‒ 

EDE ENE 1 

## **DT1 : Modélisation de la machine asynchrone** 

## **Modèle monophasé équivalent de la machine asynchrone** 

**==> picture [242 x 85] intentionally omitted <==**

**----- Start of picture text -----**<br>
Is 𝐼𝐼𝑟𝑟 [′] 𝑗𝑗𝐿𝐿𝑓𝑓𝜔𝜔𝑠𝑠<br>Vs 𝑅𝑅𝑓𝑓 𝑗𝑗𝐿𝐿𝑀𝑀𝜔𝜔𝑠𝑠 R’R/g<br>**----- End of picture text -----**<br>


## Où : 

- Rf est la résistance équivalente aux pertes fer, on a Rf ; 

- R′R est la résistance du rotor ramenée au stator, on a R′R = 0,1 Ω ; 

- LM est l’inductance magnétisante ; 

- Lf est la l’inductance rotorique vue du stator, on a Lf = 3.6 mH ; 

- g est le glissement, on rappelle que g = ωs−ω ; ωs 

- VS est la tension simple d’alimentation du stator ; 

- IS est le courant dans une phase du stator. 

## **Le bilan de puissance de la machine asynchrone en convention moteur peut être illustré de la manière suivante :** 

**==> picture [492 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
′<br>𝑷𝑷𝒎 𝒄𝒄𝒂𝒂 = 𝟑𝟑 𝟏𝟏−𝒈𝒈  [𝑹𝑹] 𝒈𝒈 [𝒕𝒕] 𝑰𝑰′𝟐𝟐𝒕𝒕<br>𝑷𝑷𝒂𝒂 = 𝑷𝑷𝑭 + 𝑷𝑷𝒕 = 𝑪𝑪𝒎 Ω =(1-g)  𝑷𝑷𝒕<br>𝑷𝑷𝒂𝒂 = 𝟑𝟑𝑽𝑽𝒔𝒔𝑰𝑰𝒔𝒔𝒄 𝒔𝒔𝝋𝝋𝒎𝒎𝒄𝒄𝒕𝒕 𝑷𝑷𝒖𝒖 = 𝑪𝑪𝒖𝒖Ω<br>= 𝑷𝑷𝒂𝒂 −𝑷𝑷𝒋𝒋𝒕𝒕 −𝑷𝑷<br>𝟐𝟐 𝑷𝑷𝒋𝒋𝒕𝒕 = 𝟑𝟑𝑹𝑹𝒕𝒕 [′] 𝑰𝑰𝒕𝒕 [′𝟐𝟐] =g ⋅ 𝑷𝑷𝒕 𝑷𝑷𝒑𝒑𝒎𝒎 = 𝑪𝑪𝒑𝒑Ω<br>𝑷𝑷𝑭 = 𝟑𝟑 [𝑽𝑽] 𝑹𝑹 [𝒔𝒔] 𝒇𝒇<br>**----- End of picture text -----**<br>


Avec : 

- Ωs ∶vitesse de rotation du champ au stator 

- Ω∶vitesse nominale de rotation de la machine asynchrone 

- cos φmot ∶facteur de puissance de l′installation 

- Cem ∶Couple électromagnétique du moteur asynchrone 

- Cu ∶couple utile de charge 

- Cp ∶couple de pertes 

- Pa : puissance absorbée 

- PFS : pertes fer au stator 

- Pjr : pertes joules au rotor 

- Pmeca ∶ puissance mécanique sur le rotor 

- Ppm : pertes mécaniques 

C O 

**==> picture [398 x 60] intentionally omitted <==**

## **Avec :** 

**==> picture [286 x 47] intentionally omitted <==**

- ωs : pulsation des grandeurs électriques ; 

- p : le nombre de paires de pôle. 

60×𝑓  𝑁𝑁𝑠𝑠 = : vitesse de rotation du champ statorique en tr ⋅min[−1] 𝑝𝑝 **Équation 2 :   Expression de la pulsation des champs au rotor** 𝝎𝝎𝒓𝒓 

**==> picture [125 x 11] intentionally omitted <==**

## **Équation 3 : Principe fondamental de la dynamique en rotation** 

**==> picture [143 x 27] intentionally omitted <==**

Avec : 

- f = 4  10[−3] N  m  s  rad[−1] : coefficient de frottement ; 

- J = 0,035 m  kg[2] : moment d’inertie ramené à l’arbre du moteur. 

‒ 2 ‒ 

**DT2 : Extrait de la norme NF C 15-100** 

‒ 3 ‒ 

**DT3 : Résultats de simulations sur le variateur de vitesse** 

**Cas 1 : Variateur de vitesse commandé en pleine onde** . **Analyse spectrale de Ir pour une commande pleine onde** 

‒ 4 ‒ 

## **Cas 2 : Variateur de vitesse commandée par Modulation de largeur d’impulsion (MLI) avec une fréquence de la porteuse** 𝐟𝐟𝐩𝐩 = 𝟔 𝟔 

## **Analyse spectrale de Ir pour une commande MLI** 

‒ 5 ‒ 

**DT4 : Résultats de simulations pour l’autopilotage du moteur asynchrone pour le cas 1 : la génération de** 𝛚𝛚𝐬𝐬 **à partir de** 𝛚𝛚𝐬 𝐬 **se fait instantanément et sans erreur statique :** 𝛚𝛚𝐬𝐬 = 𝛚𝛚𝐬 𝐬 

**==> picture [30 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
;<br>𝒓𝒓é𝒇𝒇<br>Ω 𝒑𝒑  Ω 𝒑𝒑<br>**----- End of picture text -----**<br>


‒ 6 ‒ 

**DT5 : Résultats de simulations pour l’autopilotage du moteur asynchrone pour** 𝟏𝟏 **le cas 2 :** 𝛚𝛚𝐬𝐬 = 𝛚𝛚𝐬 𝐬 𝟏𝟏+𝛕𝛕𝐯 𝐩𝐩 

**==> picture [30 x 37] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝒓𝒓é𝒇𝒇<br>Ω 𝒑𝒑  Ω 𝒑𝒑<br>**----- End of picture text -----**<br>


‒ 7 ‒ 

## **DT6 : transmetteur de température KOS 839** ~~aS~~ **Universal Temperature Transmitter KOS 839** 

‒ 8 ‒ 

**DT7 : Module d’entrée analogique (partie 1)** 

## **Module d’entrée analogique** 

Référence : Analog input module **AI 8xU/I/RTD/TC ST** 

‒ 9 ‒ 

**DT8 : Module d’entrée analogique (partie 2)** 

## **Module d’entrée analogique suite** 

- Résolution of the analog values : PIWi 

- Représentation of analog values in the current measuring ranges 

‒ 10 ‒ 

## **DT9 : symboles utilisés par l’automate Siemens S7-1500** 

_Contacts Bobines TOR_ #variable #variable #variable Normalement %Ix,y %Ix,y Normalement Ouvert Fermé %Qx,y %Qx,y %Qx,y ~~se 0+~~ _Comparaisons_ #variable   ou   tag_value 0 ou 1 == ou < ou > Exemples ~~f= -—~~ #variable   ou   tag_value #variable 1 1234 #variable 1 = = > < #variable 2 #variable 2 1234 ~~LF -~~ L_ ~~k -~~ L_ ~~}~~ _Affectation :_ permet d’affecter une valeur quelconque (IN) à un mot en mémoire (OUT). **MOVE** EN EN0 #variable 1 ou IN OUT #variable 2 decimal value La variable 2 prend la valeur de la variable 1 ou d’une valeur décimale sur ‘IN’ ~~a~~ _Fonctions logiques : #I1 et #I2 binary variables_ **& #I1 #I2 Out & #I1 #I2 Out** 0 0 0 0 0 1 #I1 0 1 0 #I1 0 1 1 Out 1 0 0 Out 1 0 1 #I2 #I2 1 1 1 1 1 0 ~~(SE~~ **>=1 #I1 #I2 Out >=1 #I1 #I2 Out** 0 0 0 0 0 1 #I1 0 1 1 #I1 0 1 0 Out 1 0 1 Out 1 0 1 #I2 #I2 1 1 1 1 1 1 ~~{LES Le~~ ‒ 11 ‒ 

## **DT10 : Profil de la tension fournie par le capteur de température** 

**==> picture [498 x 215] intentionally omitted <==**

**----- Start of picture text -----**<br>
Tension fournie<br>eAB (mV)<br>Thermocouple<br>type J<br>eAB maxi = 10,8<br>-20<br>Température<br>-1 = eAB mini TARM (°C)<br>200<br>**----- End of picture text -----**<br>


## Points caractéristiques maximaux : 

|Points caractéristiques maximaux :|||
|---|---|---|
|Température mesurée (°C)|-20|200|
|Tension délivrée par le capteur (mV)|eABmini = -1|eABmaxi = 10,8|



## **Profil du courant délivré par le transmetteur de température TT** 

**==> picture [43 x 44] intentionally omitted <==**

**----- Start of picture text -----**<br>
Courant<br>délivré Is<br>(mA)<br>**----- End of picture text -----**<br>


**==> picture [453 x 187] intentionally omitted <==**

**----- Start of picture text -----**<br>
20<br>4 = Is mini<br>Température<br>TARM (°C)<br>-20<br>200<br>**----- End of picture text -----**<br>


**==> picture [59 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
Is maxi = 20<br>**----- End of picture text -----**<br>


‒ 12 ‒ 

**Modèle CMEN v3 Nom de famille :** _(Suivi, s’il y a lieu, du nom d’usage)_ $$$$$$$$$$$$$$$$$$$$$$$ **Prénom(s) :** $$$$$$$$$$$$$$$$$$$$$$$ **Numéro Né(e) Candidat : le :** $$$$$$$$$$$ $$ $$ $$$$ _Cadre réservé aux candidats de concours de recrutement et examens professionnels_ **Concours :** ................................................ **Option / Section :** .............................................. **N° d’inscription :** $$$ Cocher une seule case parmi les six types de concours suivants : Cocher public OU privé UNIQUEMENT pour les ! externe ! 3[e] externe ! externe spécial ! interne ou 1[er] interne ! 2[nd] interne ! 2[nd] interne spécial concours enseignants : ! public ! privé **Examen professionnel pour l’avancement au grade de :** ....................................................... _Cadre réservé aux candidats d’examens et du concours général_ **Examen :** .................................................................... **Série / Spécialité :** .................................................................. **Epreuve - Matière :** ................................................................................ **Session :** .................................................................. 

EDE ENE 1 

## **DR 1 - DR 2 - DR 3** 

## **Tous les documents réponses sont à rendre, même non complétés.** 

D 

**Tournez la page S.V.P.** 

## **NE RIEN ECRIRE DANS CE CADRE** 

## **Document réponse DR1 : question A8** 

## **Caractéristiques mécaniques du moteur asynchrone et de la charge** 

**==> picture [327 x 550] intentionally omitted <==**

**----- Start of picture text -----**<br>
°<br>°<br>ee<br>co<br>=<br>°<br>Ww<br>co<br>°<br>—<br>==<br>Ty =t<br>co<br>°<br>S<br>fa<br>Ss<br>E<br>ol a<br>ll :<br>a]<br>= =<br>=<br>;<br>== °co<br>tl<br>=<br>) ee<br>a<br>wo<br>=<br>S<br>ia<br>st<br>a<br>oS<br>ia<br>=)<br>o<br>2 ° 2 ° = =<br>ra 8 A S wn<br>a ia 4 o<br>)<br>-1<br>Vitesse moteur (rad.s<br>Couple (Nm)<br>**----- End of picture text -----**<br>


‒ 2 ‒ 

## 

**==> picture [423 x 662] intentionally omitted <==**

**----- Start of picture text -----**<br>
|<br>_<br>a|eeoeor<br>—s<br>oS<br>rs |<br>is<br>1<br>!1 oa£5 '<br>1 [= H<br>: 8<br>tx<br>H<br>Ht1<br>1H 7<br>11<br>1a<br>H<br>| !<br>35<br>S<br>iH i | H<br>11<br>!<br>hsH<br>H + t<br>!<br>H<br>HI = 1<br>& H<br>Low +<br>H<br>t<br>|<br>i<br>1<br>'<br>1 3 |<br>|<br>H<br>t<br>H<br>Hi<br>t<br>i1i*<br>H<br>!H w iH<br>3 i<br>tt<br>_<br>oS<br>+<br>£5<br>sy .<br>—~go iT =2<br>SB a s<br>> a<br>′arbre moteur<br>′arbre moteur<br>∶Couple résistif mesuré sur la charge mécanique (le ventilateur)<br>∶ consigne de vitesse de rotation en sortie de l<br>ref<br>mesurée<br>r<br>Ω(p) ∶vitesse de rotation en sortie de l Ω(p) C<br>∶consigne de la pulsation des grandeurs électriques<br>∶pulsation des grandeurs électriques  ∶pulsation du champs rotoriques<br>s sref r<br>ω ω ω<br>Rappel :<br>**----- End of picture text -----**<br>


‒ 3 ‒ 

**Tournez la page S.V.P.** 

## **Document réponse DR3 : questions D2 et D3** 

## Schéma de raccordement : 

**Transmetteur de Température Ub  0V    O-    I-    I+   O+** 

## 1 2 3 Capteur Thermocouple 4 5 Module d’entrées 6 analogiques 7 **AI 8xU/I/RTD/TC ST** 8 + 9 10 11 2 fils - 12 13 14 15 16 17 18 19 20 41    42   43   44 ‒ 4 ‒[L] 

**Modèle CMEN v3 Nom de famille :** _(Suivi, s’il y a lieu, du nom d’usage)_ $$$$$$$$$$$$$$$$$$$$$$$ **Prénom(s) :** $$$$$$$$$$$$$$$$$$$$$$$ **Numéro Né(e) Candidat : le :** $$$$$$$$$$$ $$ $$ $$$$ _Cadre réservé aux candidats de concours de recrutement et examens professionnels_ **Concours :** ................................................ **Option / Section :** .............................................. **N° d’inscription :** $$$ Cocher une seule case parmi les six types de concours suivants : Cocher public OU privé UNIQUEMENT pour les ! externe ! 3[e] externe ! externe spécial ! interne ou 1[er] interne ! 2[nd] interne ! 2[nd] interne spécial concours enseignants : ! public ! privé **Examen professionnel pour l’avancement au grade de :** ....................................................... _Cadre réservé aux candidats d’examens et du concours général_ **Examen :** .................................................................... **Série / Spécialité :** .................................................................. **Epreuve - Matière :** ................................................................................ **Session :** .................................................................. 

EDE ENE 1 

## **DR 4 - DR 5 - DR 6 - DR 7** 

## **Tous les documents réponses sont à rendre, même non complétés.** 

E 

**Tournez la page S.V.P.** 

## **NE RIEN ECRIRE DANS CE CADRE** 

## **Document réponse DR4 : questions D4 à D7** 

**D4** - Caractérisation des valeurs d’entrée/sortie de la fonction de transfert Is = f(TARM) du transmetteur. 

**==> picture [458 x 244] intentionally omitted <==**

**----- Start of picture text -----**<br>
Courant de sortie du<br>transmetteur de<br>température : Is<br>A compléter<br>………………<br>A compléter<br>……………… Température mesurée<br>(TARM en °C)<br>-20  200<br>**----- End of picture text -----**<br>


## **D5** - Configuration du switch S1 du transmetteur de température TT : 

|**S1**|**1**|**2**|**3**|**4**|**5**|**6**|
|---|---|---|---|---|---|---|
|**ON**|||||||
|**OFF**|||||||



## **D7** - Tableau des valeurs décimales du mot PIW8 en fonction du courant mesuré : 

|**D7**- Tableau des valeurs décima|les du mot P|IW8 en fon|ction du cou|rant mesuré|
|---|---|---|---|---|
|Courantmesuré en mA|1,185|4|20|22,81|
|Valeur décimale du mot PIW8|||||



‒ 2 ‒ 

## **Document réponse DR5 : questions D8 et D9** 

**D8** - Caractéristique de la valeur décimale du mot PIW8 en fonction du courant d’entrée du module d’entrées analogiques : PIW8 = f(Is) 

**==> picture [489 x 228] intentionally omitted <==**

**----- Start of picture text -----**<br>
Mot PIW8<br>Valeur décimale<br>A compléter<br>………………<br>A compléter<br>Courant d’entrée  Is<br>……………… (mA)<br>4  20<br>**----- End of picture text -----**<br>


**D9** - Caractéristique de la valeur décimale du mot mémoire MW8 en fonction de la valeur décimale du mot PIW8 : MW8 = f(PIW8) 

**==> picture [478 x 272] intentionally omitted <==**

**----- Start of picture text -----**<br>
Mot mémoire MW8<br>Température en °C<br>A compléter<br>………………<br>Étendue de la<br>mesure =  E<br>du transmetteur<br>de température<br>Mot PIW8<br>Valeur décimale<br>………………<br>……………… ………………<br>A compléter<br>A compléter  A compléter<br>**----- End of picture text -----**<br>


‒ 3 ‒ 

**Tournez la page S.V.P.** 

**Document réponse DR6 : question D13** 

**==> picture [454 x 619] intentionally omitted <==**

**----- Start of picture text -----**<br>
…..  A<br>A<B<br>mesure  B  PV<br>……<br>A<br>GV<br>A>B<br>…..  B<br>n i e d<br>Document réponse DR7 : question D14<br>Début PRG Mise à l’échelle<br>entree_ana < ………….<br>oui<br>OU<br>entree_ana > ……………<br>def_mesure :=   1<br>non<br>def_mesure := ………..<br>mesure := ……………<br>Ce<br>etendue := ………….<br>mesure := ( [etendue] x entree_ana ) -20<br>27 648<br>Fin PRG Mise à l’échelle<br>**----- End of picture text -----**<br>


‒ 4 ‒ 

**Modèle CMEN v3 Nom de famille :** _(Suivi, s’il y a lieu, du nom d’usage)_ $$$$$$$$$$$$$$$$$$$$$$$ **Prénom(s) :** $$$$$$$$$$$$$$$$$$$$$$$ **Numéro Né(e) Candidat : le :** $$$$$$$$$$$ $$ $$ $$$$ _Cadre réservé aux candidats de concours de recrutement et examens professionnels_ **Concours :** ................................................ **Option / Section :** .............................................. **N° d’inscription :** $$$ Cocher une seule case parmi les six types de concours suivants : Cocher public OU privé UNIQUEMENT pour les ! externe ! 3[e] externe ! externe spécial ! interne ou 1[er] interne ! 2[nd] interne ! 2[nd] interne spécial concours enseignants : ! public ! privé **Examen professionnel pour l’avancement au grade de :** ....................................................... _Cadre réservé aux candidats d’examens et du concours général_ **Examen :** .................................................................... **Série / Spécialité :** .................................................................. **Epreuve - Matière :** ................................................................................ **Session :** .................................................................. 

EDE ENE 1 

## **DR 8 - DR 9 - DR 10** 

## **Tous les documents réponses sont à rendre, même non complétés.** 

F 

**Tournez la page S.V.P.** 

## **NE RIEN ECRIRE DANS CE CADRE** 

## **Document réponse DR8 : questions D18 et D19** 

**==> picture [504 x 521] intentionally omitted <==**

**----- Start of picture text -----**<br>
24V DC<br>Q0.0<br>Q0.1<br>Module de<br>sorties TOR  Q0.2<br>Automate<br>Q0.3<br>Q0.4<br>Q0.5<br>Q0.6<br>Q0.7<br>COM<br>0 VDC<br>defaut_mesure  VPV VGV KA1  KA2<br>**----- End of picture text -----**<br>


‒ 2 ‒ 

## **Document Réponse DR9 : D20 et D21** 

**==> picture [518 x 656] intentionally omitted <==**

**----- Start of picture text -----**<br>
%Q0.0<br>ou<br># defaut_mesure<br># def_mesure<br>1<br>2<br>3<br>Question  D20<br>4<br>5<br>6<br>7<br>8<br>9<br>Question  D21<br>**----- End of picture text -----**<br>


‒ 3 ‒ 

**Tournez la page S.V.P.** 

## **Document Réponse DR10 : question E5** 

## Tableau de valeurs : 

|Tableau de valeurs :|||
|---|---|---|
|Température mesurée (°C)|-20|200|
|Tension délivrée par le capteur (mV)|eABmini = -1|eABmaxi = 10,8|
|Tension V4 (V)|||



## **Profil de la tension délivrée en sortie de l’étage de décalage :** 

**==> picture [454 x 278] intentionally omitted <==**

**----- Start of picture text -----**<br>
A compléter<br>Tension V4<br>(V)<br>…………..…………<br>Température<br>TARM (°C)<br>-20<br>200<br>……………..……<br>A compléter<br>**----- End of picture text -----**<br>


‒ 4 ‒ 

