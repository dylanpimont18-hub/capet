**==> picture [66 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
LDE ENE 2<br>**----- End of picture text -----**<br>


## **SESSION 2026** 

____ Δ 

## CAPET 

# CONCOURS EXTERNE ET CAFEP CORRESPONDANT 

# (BAC + 3) 

# **Section : SCIENCES INDUSTRIELLES DE L’INGÉNIEUR** 

# **Option : : INGÉNIERIE ÉLECTRIQUE** 

## **ADMISSIBILITÉ : ÉPREUVE 2** 

_L'épreuve consiste en une résolution de problème._ 

_L'épreuve vise à apprécier la capacité du candidat, à partir de l'exploitation de ressources et documents techniques, à résoudre un problème technique posé et à établir des éléments de conception préliminaire._ 

## Durée : 4 heures 

____ 

_Calculatrice autorisée selon les modalités de la circulaire du 17 juin 2021 publiée au BOEN du 29 juillet 2021._ 

_L’usage de tout ouvrage de référence, de tout dictionnaire et de tout autre matériel électronique est rigoureusement interdit._ 

_Il appartient au candidat de vérifier qu’il a reçu un sujet complet et correspondant à l’épreuve à laquelle il se présente._ 

_Si vous repérez ce qui vous semble être une erreur d’énoncé, vous devez le signaler très lisiblement sur votre copie, en proposer la correction et poursuivre l’épreuve en conséquence.  De même, si cela vous conduit à formuler une ou plusieurs hypothèses, vous devez la (ou les) mentionner explicitement._ 

**NB : Conformément au principe d’anonymat, votre copie ne doit comporter aucun signe distinctif, tel que nom, signature, origine, etc. Si le travail qui vous est demandé consiste notamment en la rédaction d’un projet ou d’une note, vous devrez impérativement vous abstenir de la signer ou de l’identifier. Le fait de rendre une copie blanche est éliminatoire.** 

A 

**Tournez la page S.V.P.** 

## **INFORMATION AUX CANDIDATS** 

Vous trouverez ci-après les codes nécessaires vous permettant de compléter les rubriques figurant en en-tête de votre copie. 

Ces codes doivent être reportés sur chacune des copies que vous remettrez. 

## **► Concours externe du CAPET de l’enseignement public** : 

Concours 

Section/option 

Epreuve Matière 

## **► Concours externe du CAFEP/CAPET de l’enseignement privé** : 

Concours Section/option Epreuve Matière 

## **Conseils aux candidats** 

Il est demandé aux candidats : 

- de rédiger les réponses aux différentes études sur des feuilles de copie séparées et clairement repérées ; 

- de numéroter chaque feuille de copie et indiquer le numéro de la question traitée ; 

- de rendre tous les documents réponses, même non complétés ; 

- d’utiliser exclusivement les notations indiquées dans le sujet lors de la rédaction des réponses ; 

- de justifier clairement les réponses ; 

- d’encadrer ou souligner les résultats ; 

- de présenter lisiblement les applications numériques, sans omettre les unités, après avoir explicité les expressions littérales des calculs ; 

- de formuler les hypothèses nécessaires à la résolution des problèmes posés si celles-ci ne sont pas indiquées dans le sujet. 

## **Sommaire** 

Page **Sommaire ..................................................................................................................................................... 1 Présentation du support ............................................................................................................................. 2 ÉTUDE A (à traiter obligatoirement) .......................................................................................................... 3 ÉTUDE B (à traiter obligatoirement) .......................................................................................................... 9 DOCUMENTS TECHNIQUES DE L’ÉTUDE A ........................................................................................... 14 DOCUMENTS TECHNIQUES DE L’ÉTUDE B ........................................................................................... 16** 

Les études A et B sont à traiter obligatoirement par tous les candidats. 

Page 1 

LDE ENE 2 

## **Présentation du support** 

## **Étude du bus Hycity**[®] 

Hycity[®] est un autobus à hydrogène fabriqué par la société Safra, qui va prendre la suite du Businova[®] , un véhicule de transport urbain à haut niveau de performances techniques, économiques et écologiques. 

Dans cet autobus, présenté à la figure 1, toute la chaîne de propulsion a été revue avec un essieu électrifié ZF AVE 130 constitué de deux moteurs électriques ZF 125 kW, implantés directement sur l’essieu arrière. Ces moteurs assurent la propulsion, avec une plus forte puissance de freinage régénératif. 

Figure 1 – Présentation du bus Hycity[®] 

Safra a conservé la capacité énergétique de 128,4 kW·h pour les batteries. Elles ont été dimensionnées pour modérer l’impact environnemental de la construction du bus et pour ne pas avoir à être remplacées plus d’une fois au cours de la durée de vie du Hycity[®] . Pour la même raison, elles ne sont exploitées que jusqu’à 20 % de décharge. Leur durée de vie est estimée à huit ans. 

Le Businova[®] recevait une pile à combustible (PAC) de 30 kW. Le Hycity[®] va conserver cette puissance, mais via une limitation par logiciel sur une pile à combustible de 45 kW. Cette puissance est suffisante, et permettra de procéder à des évolutions en cas de besoin. 

Le stockage de l’hydrogène est assuré par six réservoirs de 232 litres qui offrent une autonomie minimale annoncée de 2 trajets types en cycle urbain. 

Page 2 

B 

**Tournez la page S.V.P.** 

## **ÉTUDE A (à traiter obligatoirement)** 

## **Comment permettre les différentes mobilités du bus ?** 

Lors d'un fonctionnement normal du bus, la pile à combustible fournit la plus grande partie de l'énergie nécessaire à la motorisation de celui-ci. Elle doit être capable de fournir l'énergie nécessaire pour au moins 2 trajets types complets. La batterie permet quant à elle de fournir un surplus de puissance lors des phases d'accélération et de récupérer de l'énergie lors des phases de freinage. En cas de défaillance de la PAC, elle doit également permettre de fournir l'énergie nécessaire pour rentrer au dépôt sans se décharger en dessous de 20 % de sa capacité totale. 

**Objectif :** Choisir la motorisation de l’essieu électrifié ZF AVE 130 et la stratégie de commande du variateur de vitesse. 

## **Autonomie moyenne du bus** 

Grâce à des simulations, le constructeur estime que pour un trajet type de 200 km, l'énergie à fournir par la pile à combustible (PAC) est de 852 MJ. 

- **Question A1** En considérant un rendement de la PAC de 50 % et sachant que le pouvoir calorifique de l'hydrogène est de 141 MJ·kg[-1] , déterminer la masse d'hydrogène à embarquer pour effectuer le trajet type. 

- **Question A2** Dans les conditions de stockage de l'hydrogène, sa masse volumique est estimée à environ 25 kg·m[-3] . En déduire le volume d'hydrogène nécessaire pour effectuer le trajet type puis le nombre de trajets types réalisables avec un remplissage complet des réservoirs du bus avant recharge. Conclure sur le respect du cahier des charges. 

La batterie du bus doit posséder une capacité de 128,4 kW·h et une tension nominale de 600 V. Pour la construire, deux branches de deux modules identiques composés de cellules NMC HpCO - 53,5 A·h de tension nominale de 3,5 V et de capacité 53,5 A·h sont associées. 

Cette structure est représentée par la figure A1. 

**==> picture [197 x 76] intentionally omitted <==**

Figure A1 – Structure de la batterie 

Page 3 

- **Question A3** Calculer le nombre de cellules à associer en série dans chaque module pour respecter la tension nominale de la batterie. 

- **Question A4** Calculer la capacité totale de la batterie en A·h. En déduire le nombre de cellules à associer en parallèle dans chaque module et le nombre total de cellules que doit commander le constructeur pour fabriquer la batterie d'un bus. 

En cas de défaillance de la pile à combustible, le constructeur évalue à 22 kW la puissance moyenne que doit délivrer la batterie pour permettre le déplacement du bus à une vitesse moyenne de 40 km·h[-1] . 

**Question A5** Lorsque la batterie est totalement chargée, calculer l'autonomie du bus à 40 km·h[-1] jusqu'au niveau critique de décharge. Conclure quant à la capacité du bus à rentrer au dépôt en cas de défaillance de la PAC. 

## **Conditions d'utilisation extrêmes du bus** 

Dans cette partie, on souhaite dimensionner la motorisation de l'essieu en tenant compte des conditions extrêmes d'utilisation du bus. Pour cela, deux cas particuliers sont identifiés : 

- cas n°1 : le bus roule à la vitesse maximale de 70 km·h[-1] sur une pente nulle ; 

- cas n°2 : le bus roule à la vitesse constante de 20 km·h[-1] sur une pente maximale de 15 %. 

La puissance mécanique nécessaire au déplacement du bus est fournie par les deux actionneurs électriques de l’essieu électrifié ZF AVE 130. L’expression de la force nécessaire pour assurer le déplacement du bus, à vitesse constante, est donnée par : 

**==> picture [282 x 22] intentionally omitted <==**

Les caractéristiques principales du bus ainsi que les notations utiles pour cette partie sont données ci-dessous. 

|M|Masse totale autorisée en charge|Masse totale autorisée en charge|21 tonnes|
|---|---|---|---|
|R|Rayon extérieur en charge des pneumatiques||0,44 m|
|CRR|Coefficient de résistance au roulement||0,01|
|Sf|Section frontale du véhicule||8,4 m2|
|Cx|Coefficient de pénétration dans l’air||0,34|
|Ωroue|Vitesse angulaire d’une roue||rd·s-1|
|Ωm|Vitesse angulaire de l’actionneur électrique||rd·s-1|
|k|Rapport de réduction du réducteur : k =|<br>Ωm<br>Ωroue|22,66|
|ηr|Rendement du réducteur||0,95|
|vmax|Vitesse maximale du véhicule||70 km·h-1|
|v|Vitesse du véhicule||m·s-1|
|Cch|Couple résistant imposé sur l’arbre d’un des actionneurs<br>électriques||N·m|
|Cm|Couple développé par un des actionneurs électriques||N·m|



Page 4 

**Tournez la page S.V.P.** 

|Jeq|Moment d’inertie équivalent de l’ensemble des pièces en<br>mouvement ramenées sur l’arbre moteur|2,4 kg·m2|
|---|---|---|
|p|Pente de la route||
|g|Accélération de la pesanteur|9,81 m·s-2|
|ρ|Masse volumique de l’air|1,28 kg·m-3|
|Pmax|Puissance mécanique maximale développée par le bus|W|



- **Question A6** Compléter le document réponse DRA1 en y indiquant les valeurs des forces nécessaires à l'avancée du bus dans les cas n°1 et n°2. Après avoir rappelé l'expression de la puissance mécanique d'un objet en translation rectiligne uniforme, compléter la colonne correspondante dans le document réponse DRA1. 

Pour un moteur, l'équation 2 rappelle l'expression de la puissance mécanique développée. 

P = Cm ∙ Ωm (Équation 2) 

- **Question A7** Donner l'expression de la vitesse de rotation d'un moteur Ωm en fonction de la vitesse d'avancée du bus, du rayon des roues et du rapport de réduction du réducteur. Faire l'application numérique dans les cas n°1 et n°2. En déduire le couple moteur Cm généré par un moteur dans les cas n°1 et n°2 sachant qu'il y a deux moteurs sur l'essieu et que le rendement du réducteur est imparfait. Compléter les deux dernières colonnes du document réponse DRA1. 

L’équation 3 donne l’expression obtenue par l’application du principe fondamental de la dynamique sur l’arbre d’un des deux actionneurs électriques. 

**==> picture [212 x 20] intentionally omitted <==**

Au cours du cycle de fonctionnement, le cas critique d'utilisation du moteur intervient lorsque dans une pente nulle on souhaite accélérer de 20 km·h[-1] à 70 km·h[-1] en 4 secondes. 

- **Question A8** En considérant un couple résistant Cch = 28 N·m  constant lors de l'accélération maximale du bus, déterminer la valeur du couple moteur lors de cette phase. 

- **Question A9** En utilisant les résultats des questions A7 et A8, choisir sur le document technique DTA1 un moteur pouvant convenir au bus parmi les trois solutions proposées. Justifier le choix. 

## **Modélisation de la machine asynchrone** 

Dans cette partie, un seul des deux actionneurs de l’essieu électrifié est mis en œuvre en charge puis à vide. 

La machine est un moteur asynchrone (MAS) triphasé à cage, 230 V / 400 V, 700 Hz. Deux essais sous tension et fréquence nominales en fonctionnement moteur ont été réalisés. 

Page 5 

Les résultats de ces essais sont les suivants : 

- à vide, un courant de ligne I0 = 42,5 A ; 

- sous charge nominale : 

|•sous ch|arge nominale|:||||
|---|---|---|---|---|---|
|Tension<br>efficace<br>nominale<br>simple Vn|Courant de<br>ligne<br>nominal In|Facteur de<br>puissance<br>nominal|Rendement<br>nominal|Vitesse<br>angulaire<br>nominale|Fréquence<br>nominale<br>d'alimentation|
|230 V|156 A|0,94|0,905|1079 rad·s-1|700 Hz|



Dans toute cette partie, les résistances et inductances de fuites statoriques, ainsi que les pertes mécaniques sont négligées. 

**Question A10** Déterminer le nombre de paires de pôles pm  de cette machine. 

- **Question A11** À partir de l'essai sous charge nominale, déterminer les valeurs numériques pour : 

   - le glissement gn ; 

   - la puissance active absorbée Pan ; 

   - la puissance réactive absorbée Qn ; 

   - la puissance utile Pun. 

La figure A2 présente le modèle équivalent simplifié d’une phase de la machine asynchrone. 

**==> picture [42 x 31] intentionally omitted <==**

**==> picture [40 x 45] intentionally omitted <==**

Figure A2 – Modèle équivalent simplifié d'une phase de la machine asynchrone (MAS) 

- **Question A12** Lors de l'essai à vide, indiquer quelle approximation est possible sur la valeur du glissement g. Dessiner le nouveau schéma équivalent simplifié d'une phase de la machine asynchrone dans ce cas puis donner les expressions littérales de la puissance active P0 et de la puissance réactive Q0 consommées par la machine en fonction de V la valeur efficace de la tension V, Rf et Xm. 

- **Question A13** Calculer la puissance apparente S0 consommée par la machine lors de l'essai à vide. En déduire la valeur de Rf et Xm sachant que P0 = 7,82 kW. 

Page 6 

**Tournez la page S.V.P.** 

D'autres essais ont mené aux valeurs suivantes : 

**==> picture [173 x 12] intentionally omitted <==**

Le calcul de la puissance électromagnétique via le modèle équivalent de la figure A2 mène à l'expression du couple utile CU donnée à l'équation 4 : 

**==> picture [212 x 35] intentionally omitted <==**

**Question A14** Donner la valeur du glissement g au démarrage de la machine. En déduire la valeur du couple utile CUd disponible au démarrage de la machine et conclure sur la capacité de la machine à démarrer sous tension et fréquence nominales sachant que le couple résistant sur l'arbre moteur est de 451 N·m à l'arrêt. 

## **Variation de vitesse** 

Le moteur, objet de l’étude précédente, est alimenté par un onduleur autonome triphasé. L’alimentation triphasée délivrée par l’onduleur au moteur présente une valeur efficace de tension simple V, une fréquence f et une pulsation . Le moteur est couplé en étoile. 

Le document réponse DRA2 représente la plaque à bornes de chaque machine asynchrone triphasée utilisée dans l’essieu électrifié. Celle-ci comporte six bornes (U1, V1, W1, U2, V2, W2) auxquelles sont reliées les entrées et les sorties des trois enroulements. Les phases disponibles en sortie de l’onduleur sont notées Ph1, Ph2 et Ph3. 

**Question A15** Compléter le câblage du moteur représenté sur le document réponse DRA2 afin de réaliser le couplage choisi par le constructeur. 

La figure A3 présente le schéma électrique de l’onduleur de tension étudié. On s’intéresse dans un premier temps à la mise en œuvre d’une commande simplifiée. 

Figure A3 – Schéma électrique de l’onduleur de tension 

Page 7 

## Hypothèses : 

- les composants sont idéaux. Les Ki sont des interrupteurs unidirectionnels, commandés à l'ouverture et à la fermeture. Un interrupteur en conduction présente une tension nulle à ses bornes ; 

- la tension U0 est continue ; 

- le moteur asynchrone triphasé est alimenté à partir des bornes repérées 1, 2 et 3 du schéma de la figure A3 ; 

- la commande des interrupteurs est périodique de fréquence f0 = 1/T0 et suit le séquencement indiqué dans le tableau ci-dessous (la présence d’un interrupteur correspond à l’état passant de celui-ci) : 

Pour un fonctionnement donné, l'intensité du courant i1(t) absorbée par la borne 1 de la machine asynchrone est représentée sur le document réponse DRA3. 

**Question A16** Tracer les chronogrammes de vK2(t), vK4(t), u12(t) et u31(t) sur le document DRA3. 

**Question A17** Sachant que u12(t) = v1(t) - v2(t) , u31(t) = v3(t) - v1(t) et v1(t) + u12(t) - u31(t) v2(t) + v3(t) = 0, montrer que : v1(t) = . Tracer alors l'allure de 3 v1 sur le document réponse DRA3. 

**Question A18** L'exploitation du tracé de v1 permet de déterminer sa valeur efficace √ 2 v1eff = U0. En déduire la valeur de U0 à appliquer pour obtenir une 3 alimentation correcte de la machine asynchrone. 

En optimisant l'origine des temps, la tension u12(t) peut se décomposer sous la forme donnée par l'équation 5 avec n un entier naturel correspondant au rang des harmoniques : 

**==> picture [367 x 35] intentionally omitted <==**

**Question A19** ' Calculer les amplitudes |An | des harmoniques de la tension u12(t) pour n<10 avec U0 = 490 V et f0 = 700 Hz. Compléter alors le spectre sur le document réponse DRA4. 

Le document technique DTA2 montre le spectre obtenu avec une autre stratégie de commande de l'onduleur : la modulation de largeur d'impulsion (MLI). Dans cette commande pour produire les signaux souhaités, on compare une modulante à la fréquence f0 = 700 Hz et une porteuse à la fréquence fP = 10 kHz. 

**Question A20** Pour les fréquences allant de 0 à 7 kHz environ, indiquer quelle stratégie de commande (simplifiée ou MLI) semble la plus optimale. Justifier. 

Page 8 

**Tournez la page S.V.P.** 

## **ÉTUDE B (à traiter obligatoirement)** 

## **Comment réguler la température de fonctionnement de la pile à combustible ?** 

Le niveau de performance d’un système à pile à combustible résulte d’une optimisation entre ses paramètres de fonctionnement : température, pression et humidité des gaz. 

En effet, le contrôle de la température de fonctionnement de la pile à combustible, de la pression des gaz ainsi que l’hydratation de la membrane permettent d’augmenter sa conductivité ionique. 

En particulier, la régulation en température de la pile doit répondre à trois objectifs : 

- protéger la pile. La température de la partie solide de la pile ne doit pas dépasser 85 °C et l’écart entre la température des gaz en entrée de la pile et celle de la pile doit être inférieure à 10 °C ; 

- optimiser le bon fonctionnement de la pile. Pour cela la température de la pile TS doit être asservie à une consigne Tcons variable, avec une précision de 2 °C. De plus, l’écart entre les températures des gaz en entrée et de l’eau en sortie de la pile doit être inférieur à 5 °C ; 

- assurer un bilan d’eau positif. Cet objectif devient prioritaire lorsque le volume d’eau stocké descend en-dessous d’un seuil limite. 

**Objectif :** Choisir une partie des constituants de la chaîne de mesure de température de la pile à combustible. Établir l’équation de récurrence d’un correcteur numérique 

## **Acquisition de la température de la pile à combustible** 

La mesure de la température est assurée par un capteur du constructeur Jumo, dont la référence est 902040/12-370-1003-1-7,5-29-121-20/000. Ses caractéristiques sont présentées dans le document technique DTB1. 

Le cahier des charges vis-à-vis de la mesure de la température est le suivant : 

|Étendue de mesure|-5°C à 90°C|
|---|---|
|Erreur de mesure|<1°C|



**Question B1** À partir du document technique DTB1 et de la référence du capteur, identifier : 

- le type de transducteur (conversion de la grandeur physique en une grandeur électrique) de ce capteur ; 

- l’étendue de mesure ; 

- le type de capteur : passif ou actif. 

D’après le document technique DTB2, le capteur peut être modélisé par une résistance équivalente notée RT. 

**Question B2** À l’aide du document technique DTB2 et du cahier des charges, donner la loi d’évolution de RT en fonction de la température. 

Page 9 

En première approche, cette résistance évolue selon la loi RT = R0(1+a ∙ T) où R0 est la résistance à 0°C et a, un coefficient à déterminer. 

**Question B3** Justifier pourquoi cette première approche est satisfaisante dans le cadre de l’étude. Identifier alors dans le document technique DTB2 les valeurs numériques de R0 et a. 

La chaîne de mesure de la température de la pile est donnée figure B1. 

|T|Capteur et<br>conditionneur|conditionneur<br>vT(t)|Amplificateur et<br>conditionneur<br>(t)|Amplificateur et<br>vA|CAN|GN|
|---|---|---|---|---|---|---|



Figure B1 – Chaîne d’acquisition de la mesure de la position angulaire 

Les conditionneurs et amplificateurs mettent en œuvre des amplificateurs linéaires intégrés (ALI ou AOP) considérés comme idéaux. 

L’évolution de la température est suffisamment lente pour que la température soit considérée comme constante. Les grandeurs électriques utilisées dans le conditionneur sont alors considérées comme continues. 

Le capteur Jumo est inséré dans un premier circuit conditionneur présenté à la figure B2. 

**==> picture [211 x 60] intentionally omitted <==**

**----- Start of picture text -----**<br>
<br>I = 10 mA<br>vT (t)<br>RT<br>**----- End of picture text -----**<br>


Figure B2 – Circuit de conditionnement du capteur de température 

**Question B4** Exprimer la tension vT (t), en sortie de l’ALI. 

La mettre sous la forme : vT = U0 ∙ (1+a ∙ T) en exprimant U0 qui est fonction de I et de R0, puis expliquer quel est le nom et le rôle de ce montage. 

**Question B5** Calculer les valeurs de vT pour les températures extrêmes données dans le cahier des charges. Représenter l’évolution de vT en fonction de T. 

L’utilisation optimale du convertisseur analogique numérique impose en sortie de l’ensemble {amplificateur + conditionneur} une tension vA directement proportionnelle à la température et évoluant sur une plage de tension de 3 V, telle que vA = c ∙ T, avec c > 0. Cela nécessite d’utiliser un ou plusieurs montages parmi ceux présentés dans le document technique DTB3. 

**Question B6** Justifier le besoin de l’ensemble {amplificateur + conditionneur} pour mesurer la température sur une plage de – 5 °C à 90 °C. Montrer que la valeur de c est égale à 0 ,0316 V∙°C[-1] . 

Quelles que soient les valeurs déterminées précédemment, on considérera désormais : 

**==> picture [97 x 12] intentionally omitted <==**

Page 10 

**Tournez la page S.V.P.** 

- **Question B7** Montrer que la tension UT2 du montage 1 du document technique DTB3 s’écrit sous la forme : Vs = R1+R0. En déduire le nom et le rôle de ce type VE R1 

- de montage. 

**Question B8** Choisir, en justifiant la réponse, un montage du document technique DTB3 afin de concevoir l’ensemble {amplificateur + conditionneur}. 

Le montage 3 est finalement retenu pour réaliser l’amplification et le conditionnement. 

**Question B9** Déterminer les valeurs des composants (résistances, sources de tension) pour obtenir l’expression de vA = f(T) désirée. 

La documentation du CAN choisi par le constructeur (ADS7029-Q1) est présentée dans le document technique DTB4. 

**Question B10** Relever les caractéristiques du CAN dans le document technique DTB4 et déterminer : 

- la grandeur pleine échelle ; 

- la résolution ; 

- le quantum q. 

**Question B11** ΔGN Montrer que la sensibilité S = de l’ensemble {capteur + amplificateur ΔT + conditionneur + CAN} est égale à 2,684 °C[−1] . En déduire le gain de l’ensemble de la chaîne de mesure ainsi que le mot numérique en binaire puis en hexadécimal, noté NC, correspondant à la température de consigne de la régulation de température TC = 55 °C. 

- **Question B12** À partir de l’exploitation du document technique DTB5, déterminer l’erreur de quantification maximale et en déduire l’erreur de mesure de la température T de la chaîne de mesure. Conclure vis-à-vis du cahier des charges. 

## **Asservissement de la température de fonctionnement de la pile** 

Pour un fonctionnement optimal de la pile à combustible, la température doit être maintenue en permanence entre 50 et 60 °C. Un extrait du diagramme d’exigences de la régulation de température est donné figure B3. 

Figure B3 – Exigences fonctionnelles liées à la régulation en température de la pile 

Page 11 

L’étude qui suit s’intéresse aux variations autour d’un point de fonctionnement fixé à TC = 55 °C (milieu de l’intervalle de fonctionnement optimal). 

Le schéma fonctionnel ci-dessous représente l’asservissement numérique en température du système de refroidissement de la pile à combustible. 

|Correcteur<br>numérique<br>uk<br>uC(t)<br>CNA<br>Système de<br>refroidissement<br>+<br>-<br>uR(t)<br>Nk<br> εk<br>Capteur<br>T(t)<br>Filtre anti-repliement<br>+ E/B<br>CAN|Système de<br>refroidissement|T(t)|
|---|---|---|



On note T(p) , UC(p)  et UR(p)  les transformées de Laplace associées aux variables temporelles T(t), uC(t) et uR(t). La température T est exprimée en °C et les tensions u(t) et uR(t) en V. 

Le système de refroidissement peut être modélisé par le système du premier ordre suivant : 

- constante de temps : τ = 0,9 s ; 

- gain statique : K = 4°C·V[ -1] . 

Le capteur de température est assimilé à un simple gain de valeur Kc = 0,0316 V·°C[-1] . 

## **Détermination de la fréquence d’échantillonnage** 

L’allure de la réponse de uR(t) pour un échelon de tension de commande uC(t) de 1 V est donnée sur le document réponse DRB1. Le constructeur désire obtenir au moins 10 échantillons au cours du régime transitoire. 

- **Question B13** Déterminer, en utilisant le document réponse DRB1, la durée du régime transitoire (de t = 0 à tR5%). Établir l’inégalité que doit respecter la période d’échantillonnage, Te. En déduire la fréquence d’échantillonnage minimale fmin à utiliser. 

- **Question B14** Définir le rôle de l’échantillonneur-bloqueur (E/B). Donner le schéma électrique d’un échantillonneur-bloqueur d’ordre zéro. 

Indépendamment des résultats obtenus, la période d’échantillonnage retenue par la suite est donnée par T2 = 0,25 s. 

- **Question B15** Compléter le document réponse DRB1 en représentant les allures du * 

- signal échantillonné uR (t) et du signal échantillonné – bloqué uRB(t). 

- **Question B16** Déterminer le temps de conversion Tc maximal que doit respecter le convertisseur numérique analogique. Conclure à partir du document technique DTB4 sur la capacité du CAN à convertir suffisamment rapidement la grandeur analogique. 

Page 12 

**Tournez la page S.V.P.** 

**Question B17** Définir le rôle du filtre anti-repliement. Rappeler le théorème de Shannon. En déduire l’ordre de grandeur de la fréquence de coupure fc du filtre antirepliement si ce dernier est considéré comme parfait. 

## **Établissement de la relation de récurrence du correcteur numérique** 

Le respect des exigences pour la régulation de la température de la pile a conduit le constructeur à choisir le correcteur C(p) de fonction de transfert : 

**==> picture [301 x 22] intentionally omitted <==**

La température est mesurée par l’intermédiaire d’un capteur et d’une chaîne de mesure de période d’échantillonnage notée Te. Après chaque acquisition de température à t = k∙Te, une commande de température uk est transmise au système de refroidissement. 

On note : 

- {uk} la suite des valeurs de commande de température générées aux instants k ∙ Te ; 

- {εk} la suite des valeurs de ε(t) calculées aux instants k ∙ Te. 

**Question B18** Donner l’expression de la transformée de Laplace de l’expression du(t) suivante : dans les conditions de Heaviside. À partir de l’expression dt de la fonction de transfert C(p), donner la relation permettant d’exprimer U(p) en fonction de ε(p). Démontrer que l’équation différentielle liant u(t) et e(t) est la suivante : Tco du(t) = Kcoε ( t ) +KcoTco dε(t) ~~.~~ dt dt 

On considère que l’expression gk − gk−1 constitue une expression numérique approchée de Te ∙ la dérivée de g(t) à l’instant k Te. 

∙ **Question B19** En posant t = k Te dans l’équation différentielle précédente, déterminer alors l’équation de récurrence permettant de calculer uk en fonction de uk-1 , εk  et εk-1 . La mettre sous la forme ci-dessous et exprimer les coefficients b1, a 0 et a 1 en fonction de Tco, Te et Kco : 

**==> picture [159 x 12] intentionally omitted <==**

**Question B20** Compléter sur le programme Python du document réponse DRB2 : 

- la définition des paramètres ; 

- l’expression de la relation de récurrence dans la fonction correcteur. 

Page 13 

LDE ENE 2 

## **DOCUMENTS TECHNIQUES DE L’ÉTUDE A** 

## **Document technique DTA1** 

Extrait de la documentation d'actionneurs (MAS) pour l’essieu électrifié 

## **Moteur 1** 

||**Moteur 1**||
|---|---|---|
|Nn|Fréquence de rotation nominale|2976 tr·mn-1|
|fn|Fréquence nominale des tensions d’alimentation|50 Hz|
|Cn|Couple utile nominal|350 N·m|
|Cmax|Couple utile maximal|980 N·m|
|Pn|Puissance utile nominale|110 kW|



## **Moteur 2** 

||**Moteur 2**||
|---|---|---|
|Nn|Fréquence de rotation nominale|10 300 tr·mn-1|
|fn|Fréquence nominale des tensions d’alimentation|700 Hz|
|Cn|Couple utile nominal|100 N·m|
|Cmax|Couple utile maximal|400 N·m|
|Pn|Puissance utile nominale|100 kW|



## **Moteur 3** 

||**Moteur 3**||
|---|---|---|
|Nn|Fréquence de rotation nominale|10 300 tr·mn-1|
|fn|Fréquence nominale des tensions d’alimentation|700 Hz|
|Cn|Couple utile nominal|85 N·m|
|Cmax|Couple utile maximal|475 N·m|
|Pn|Puissance utile nominale|92 kW|



Page 14 

C 

**Tournez la page S.V.P.** 

## **Document technique DTA2** 

Spectre de la tension composée u12(t) obtenu avec une commande MLI 

**==> picture [455 x 228] intentionally omitted <==**

Page 15 

**DOCUMENTS TECHNIQUES DE L’ÉTUDE B** 

## **Document technique DTB1** 

## **Document technique DTB2** 

Page 16 

**Tournez la page S.V.P.** 

## **Document technique DTB3** 

## **Montage 1** 

**==> picture [365 x 86] intentionally omitted <==**

**----- Start of picture text -----**<br>
<br>  = 0  Fonction de transfert<br>??<br>vE vS<br>R0<br>R1<br>**----- End of picture text -----**<br>


## **Montage 2** 

**==> picture [429 x 96] intentionally omitted <==**

**----- Start of picture text -----**<br>
 R0<br>R1<br> Fonction de transfert<br>  = 0<br>vE vS - [v][S] =  − [R][0]<br>vE R1<br>**----- End of picture text -----**<br>


## **Montage 3** 

**==> picture [161 x 100] intentionally omitted <==**

**----- Start of picture text -----**<br>
 R0<br>R1<br><br>v1   = 0<br>R1 vS<br>v2 R0<br>**----- End of picture text -----**<br>


**==> picture [163 x 53] intentionally omitted <==**

**----- Start of picture text -----**<br>
Fonction de transfert<br> vS = : [R][0] ⋅( v2  − v1 )<br>R1<br>**----- End of picture text -----**<br>


## **Montage 4** 

**==> picture [164 x 121] intentionally omitted <==**

**----- Start of picture text -----**<br>
R1<br><br>R2<br>v1   = 0<br>v2 vS<br> R0<br>R3<br>**----- End of picture text -----**<br>


## **Fonction de transfert** 

**==> picture [211 x 29] intentionally omitted <==**

Page 17 

## **Document technique DTB4** 

## **Document technique DTB5** 

Le CAN (convertisseur analogique numérique) délivre en sortie un nombre fini de codes numériques, correspondant à une gamme de tension analogique d’entrée bornée : c’est la plage de conversion. 

**==> picture [153 x 85] intentionally omitted <==**

**----- Start of picture text -----**<br>
GA  CAN  GN<br>an-1<br>  /  #<br>VE<br>Symbole  a1<br>**----- End of picture text -----**<br>


La courbe de transfert théorique donnant le mot binaire de sortie N(2) en fonction de la tension d’entrée VE, est une courbe en escalier présentée ci-contre dans le cas d’une quantification centrée. 

**==> picture [188 x 246] intentionally omitted <==**

**----- Start of picture text -----**<br>
N(2)<br>Caractéristique idéale<br>a2 a1 a0<br>\ 4<br>1   1   1<br>PE = 8 V<br>1   1   0<br>n = 3 bits<br>q<br>1   0   1  VE (V)<br>0     1     2     3     4     5     6     7     8<br> q<br>+ q/2<br>VE<br>- q/2<br>**----- End of picture text -----**<br>


On peut lui associer l’erreur de conversion ou erreur de quantification q en dents de scie. Celle-ci est comprise entre - q/2 et q/2. 

Page 18 

**Modèle CMEN v3 Nom de famille :** _(Suivi, s’il y a lieu, du nom d’usage)_ $$$$$$$$$$$$$$$$$$$$$$$ **Prénom(s) :** $$$$$$$$$$$$$$$$$$$$$$$ **Numéro Né(e) Candidat : le :** $$$$$$$$$$$ $$ $$ $$$$ _Cadre réservé aux candidats de concours de recrutement et examens professionnels_ **Concours :** ................................................ **Option / Section :** .............................................. **N° d’inscription :** $$$ Cocher une seule case parmi les six types de concours suivants : Cocher public OU privé UNIQUEMENT pour les ! externe ! 3[e] externe ! externe spécial ! interne ou 1[er] interne ! 2[nd] interne ! 2[nd] interne spécial concours enseignants : ! public ! privé **Examen professionnel pour l’avancement au grade de :** ....................................................... _Cadre réservé aux candidats d’examens et du concours général_ 

**Examen :** .................................................................... **Série / Spécialité :** .................................................................. **Epreuve - Matière :** ................................................................................ **Session :** .................................................................. 

LDE ENE 2 

## **DRA1 - DRA2 - DRA3 - DRA4** 

## **Tous les documents réponses sont à rendre, même non complétés.** 

D 

**Tournez la page S.V.P.** 

**NE RIEN ECRIRE DANS CE CADRE** — **DOCUMENT RÉPONSE DRA1 (Questions A6 et A7) Puissance Vitesse de Couple mécanique Force (N) rotation des généré par 1 développée par moteurs (rad·s[-1] ) moteur (N·m) le bus (kW) Cas n°1** v = 70 km·h[-1] p = 0 % **Cas n°2** v = 20 km·h[-1] p = 15 % 

## **DOCUMENT RÉPONSE DRA2 (Question A15)** 

Page 19 

**DOCUMENT RÉPONSE DRA3 (Questions A16 et A17)** 

Page 20 

**Tournez la page S.V.P.** 

**DOCUMENT RÉPONSE DRA4 (Question A19)** 

**==> picture [47 x 54] intentionally omitted <==**

Page 21 

**Modèle CMEN v3 Nom de famille :** _(Suivi, s’il y a lieu, du nom d’usage)_ $$$$$$$$$$$$$$$$$$$$$$$ **Prénom(s) :** $$$$$$$$$$$$$$$$$$$$$$$ **Numéro Né(e) Candidat : le :** $$$$$$$$$$$ $$ $$ $$$$ _Cadre réservé aux candidats de concours de recrutement et examens professionnels_ **Concours :** ................................................ **Option / Section :** .............................................. **N° d’inscription :** $$$ Cocher une seule case parmi les six types de concours suivants : Cocher public OU privé UNIQUEMENT pour les ! externe ! 3[e] externe ! externe spécial ! interne ou 1[er] interne ! 2[nd] interne ! 2[nd] interne spécial concours enseignants : ! public ! privé **Examen professionnel pour l’avancement au grade de :** ....................................................... _Cadre réservé aux candidats d’examens et du concours général_ **Examen :** .................................................................... **Série / Spécialité :** .................................................................. **Epreuve - Matière :** ................................................................................ **Session :** .................................................................. 

LDE ENE 2 

## **DRB1 - DRB2** 

## **Tous les documents réponses sont à rendre, même non complétés.** 

E 

**Tournez la page S.V.P.** 

**NE RIEN ECRIRE DANS CE CADRE** 

## **DOCUMENT RÉPONSE DRB1 (Question B13 et B15)** 

||uR(V)|(V)|||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0,1264 V<br>0,0948 V<br>0,0632 V<br>0,0316 V<br>0 V|0,1264 V<br>0,0948 V<br>0,0632 V<br>0,0316 V<br>0 V<br>~~$ ~~||~~ce5cnEEE~~||||||||||||||||||
|0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)|0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)|0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)|
|0,1264 V<br>0,0948 V<br>0,0632 V<br>0,0316 V<br>0V|uR<br>*(t)<br>0,1264 V<br>0,0948 V<br>0,0632 V<br>0,0316 V<br>0V<br>:<br>~~5 ~~||:<br>J<br>:<br>:<br>:<br>:<br>q<br>:<br> ~~ZSSSSEEE=~~||||||||||||||||al||
|0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)|0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)|0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)|
||uRB(t)||||||||||||||||||||
|0,1264 V|0,1264 V||||||||||||||||||||
||~~sessssssssossnesessessecseedpeseesessssssssssssssnssnspessessessensessessessssssbossnssggagaa@™Ottrressheejecsecssssssssssessnssssssfeseseccessessessssssssssnjonsessesssessesceseessesegsssssssssnssnssssssssessefeceesessssesssssssssssnenspessesssessessessessesseud~~||||||||||||||||||||
|0,0948 V|0,0948 V||||||||||||||||||||
|0,0632 V|0,0632 V||||||||||||||||||||
|0,0316 V<br>0V|0,0316 V<br>0V<br>~~f~~ sevsoseeeeeafusnnneeeeesunnnneeeeeenafnneeteneesunnesneeeeesunbeneeeenennunnneeeeesiaeafeetecensunsenteeesesnssnfeeeeseunesseeeeeessneseedhecetsenseeteeessneseseepecsaseneeeeeesiansseeeefenanneeeeeeeesaanesteeeejuseseneeeeeennsneseeeeeed||||||||||||||||||||
|0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)|||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)||0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)|0          0,5        1         1,5         2        2,5         3         3,5         4        4,5               t(s)|



Page 22 

**Tournez la page S.V.P.** 

## **DOCUMENT RÉPONSE DRB2 (Question B20)** 

Page 23 

