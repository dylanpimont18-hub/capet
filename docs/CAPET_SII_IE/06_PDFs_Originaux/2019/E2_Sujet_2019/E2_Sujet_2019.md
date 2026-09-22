![](_page_0_Picture_0.jpeg)

**EDE ENE 2** 

#### **SESSION 2019**

# CAPET CONCOURS EXTERNE ET CAFEP CORRESPONDANT

Section: SCIENCES INDUSTRIELLES DE L'INGÉNIEUR

**Option: INGÉNIERIE ÉLECTRIQUE** 

# ÉTUDE D'UN SYSTÈME, D'UN PROCÉDÉ OU D'UNE ORGANISATION

Durée: 4 heures

Calculatrice électronique de poche - y compris calculatrice programmable, alphanumérique ou à écran graphique — à fonctionnement autonome, non imprimante, autorisée conformément à la circulaire n° 99-186 du 16 novembre 1999.

L'usage de tout ouvrage de référence, de tout dictionnaire et de tout autre matériel électronique est rigoureusement interdit.

Si vous repérez ce qui vous semble être une erreur d'énoncé, vous devez le signaler très lisiblement sur votre copie, en proposer la correction et poursuivre l'épreuve en conséquence. De même, si cela vous conduit à formuler une ou plusieurs hypothèses, vous devez la (ou les) mentionner explicitement.

NB: Conformément au principe d'anonymat, votre copie ne doit comporter aucun signe distinctif, tel que nom, signature, origine, etc. Si le travail qui vous est demandé consiste notamment en la rédaction d'un projet ou d'une note, vous devrez impérativement vous abstenir de la signer ou de l'identifier.

#### **INFORMATION AUX CANDIDATS**

Vous trouverez ci-après les codes nécessaires vous permettant de compléter les rubriques figurant en en-tête de votre copie

Ces codes doivent être reportés sur chacune des copies que vous remettrez.

► Concours externe du CAPET de l'enseignement public :

![](_page_1_Figure_4.jpeg)

► Concours externe du CAFEP/CAPET de l'enseignement privé :

| Concours | Section/option | Epreuve | Matière |
|----------|----------------|---------|---------|
| EDF      | 1412E          | 102     | 7048    |

#### **Ce sujet comporte 3 dossiers :**

- − dossier de présentation et travail demandé pages 1 à 17 ;
- − dossiers documents annexes pages 18 à 23 ;
- − dossiers documents réponses pages 24 à 26.

# **Une lecture préalable et complète du sujet est indispensable.**

Le candidat doit répondre aux différentes questions du sujet sur les documents réponses quand cela est demandé, et sur feuilles de copie quand cela n'est pas précisé.

Il lui est rappelé qu'il doit utiliser les notations propres au sujet, présenter clairement les calculs et dégager ou encadrer tous les résultats.

Si le sujet (les questions ou les annexes) conduit à formuler une ou plusieurs hypothèses, il est demandé au candidat de la (ou les) mentionner explicitement sur la copie.

# **Transformation d'une rame de métro**

# **1 Mise en situation**

Dans le réseau Métro, des travaux de maintenance et de renouvellement des voies sont à prévoir dans les prochaines années. Cependant, il y a actuellement un manque de Véhicules de Maintenance Industriels (VMI). Il est donc impératif de trouver des solutions très rapidement pour répondre à toutes les demandes.

Il est proposé dans ce sujet d'étudier la faisabilité d'utiliser les motrices d'anciennes rames de métro MF67 en les transformant en VMI, avec le minimum de modifications possible.

Le véhicule de maintenance est composé de deux motrices (appelées locotracteurs), avec chacune 4 essieux motorisés (voir figure 1). Entre les deux locotracteurs, trois wagons permettent d'acheminer du matériel sur les chantiers de maintenance.

![](_page_3_Picture_5.jpeg)

**Figure 1 :** véhicules de Maintenance Industriels (VMI) avec deux locotracteurs

Lors d'un trajet vers une zone de chantier, les locotracteurs sont tout d'abord alimentés par le 3ème rail sous 750 V, puis par des batteries de traction. Tous les travaux se font pendant la nuit. Les batteries de traction sont donc rechargées pendant la journée.

Ce sujet comporte trois parties afin d'étudier la faisabilité de transformer d'anciennes motrices de rames de métro en VMI :

- − la détermination de la consommation d'énergie du véhicule lors d'une nuit de travaux ;
- − le dimensionnement du système de stockage et l'étude de sa recharge ;
- − la vérification de l'aptitude à la traction et du dimensionnement des moteurs.

#### 2 Étude énergétique

**Objectif**: évaluer la consommation d'énergie du véhicule afin de dimensionner la batterie.

Le véhicule de maintenance réalise un trajet aller-retour sur une zone de chantier pendant la nuit. Lors de ce trajet, le véhicule réalise plusieurs démarrages et freinages.

Le démarrage du véhicule se fait à accélération constante et par l'utilisation de rhéostats de démarrage.

Le freinage du véhicule est un freinage pneumatique utilisant des compresseurs pour assurer l'alimentation en air comprimé des freins.

#### 2.1 Mise en équations

Le déplacement du véhicule est décrit par l'équation suivante, issue du théorème de la résultante dynamique :  $m \times \gamma = F_{in} - F_{ex}$ ,

avec  $m = 171400 \,\mathrm{kg}$ , la masse équivalente de la rame (en prenant en compte les masses équivalentes tournantes);

 $\gamma$  , tel que  $\gamma = \left\| \stackrel{\Gamma}{\gamma}_{\textit{train/sol}} \right\|$  l'accélération de la rame en  $\mathbf{m} \cdot \mathbf{s}^{-2}$  ;

 $F_{in}$ , l'effort total de traction de la rame, généré par la motorisation, en Newton ;

 $F_{\rm ex}$ , l'effort résistant sur la rame, en Newton.

![](_page_4_Picture_11.jpeg)

Figure 2 : déplacement d'une rame

Les phases de démarrage se font à accélération constante ( $\gamma = 0.2 \text{ m} \cdot \text{s}^{-2}$ ) et les phases de freinage également ( $\gamma = -1.5 \text{ m} \cdot \text{s}^{-2}$ ).

#### **Question 1**

Exprimer la vitesse V(t) du train par rapport au sol et la distance parcourue x(t) en fonction du temps t et de l'accélération  $\gamma$  lors d'une phase de démarrage.

En considérant  $F_{in}$  constant, l'expression de l'énergie  $E_{dep}$  utilisée pour déplacer le train pendant une durée  $\Delta t$  est :

$$E_{dep} = \int_0^{\Delta t} F_{in} \cdot V(t) \cdot dt$$

Exprimer l'énergie  $E_{dep1}$ , correspondant à une phase à accélération constante, en fonction de  $F_{in}$ ,  $\Delta t_1$  et  $\gamma$ .

Après cette phase de démarrage, le train reste à la vitesse constante ( $V_0 = 30 \, \mathrm{km \cdot h^{-1}}$ ) pendant une durée  $\Delta t_2$ .

#### **Question 3**

Exprimer l'énergie  $E_{dep2}$ , correspondant à une phase à vitesse constante, en fonction de  $F_{in}$ ,  $V_0$  et  $\Delta t_2$ .

#### 2.2 Énergie utilisée pour parcourir le trajet

L'acheminement du convoi depuis le Parc de la Villette jusqu'au point le plus proche possible ( $\leq$  2 km) de la zone de chantier se fait à partir du rail d'alimentation ( $3^{\text{ème}}$  rail). À partir de ce point, le rail d'alimentation est hors tension, la fin de l'acheminement et la phase de chantier ( $\leq$  1 km) se fait en alimentation autonome par batterie (voir figure 3).

![](_page_5_Figure_7.jpeg)

Figure 3 : parcours défini pour l'étude

Le profil de voie défini pour cette étude synthétise les contraintes couramment rencontrées sur toutes les lignes du Métro. Ce profil tient compte des pentes et des courbes. L'annexe A1 présente le profil temporel de la vitesse du train ainsi que les pentes et les courbes rencontrées lors d'une phase « aller » sur la zone de transfert.

L'effort résistant  $F_{ex}$ , à faible vitesse, se définit par  $F_{ex} = F_b + F_c + F_d$ ,

avec  $F_b$ , l'effort de résistance à l'avancement ;

 ${\it F_c}$  , l'effort dû au rayon de courbure de la voie ;

 $F_d$  , l'effort dû à la pente de la voie.

Considérons une voie ayant une pente, supposée faible, de i ‰ et un rayon de courbure  $R_{v}$ , alors les différents efforts sont donnés par :

$$F_c = \frac{750}{R_v} \cdot 10^{-3} \cdot m \cdot g$$
$$F_d = i \cdot 10^{-3} \cdot m \cdot g$$

avec g l'accélération de la pesanteur, tel que  $g = 9.81 \,\mathrm{m}\cdot\mathrm{s}^{-2}$ 

L'effort de résistance à l'avancement est classiquement exprimé sous la forme :

$$F_b = A + B \cdot V + C \cdot V^2$$
 avec  $V = \|V_{train/sol}\|$  la vitesse du train.

Cette expression est réduite, dans cette étude, à la constante A = 5 141 N représentant l'ensemble des frottements secs. Les efforts de type visqueux, modélisés par  $B \cdot V$  et aérauliques, modélisés par  $C \cdot V^2$  sont négligeables aux vitesses de déplacement du VMI ( $\leq 30 \text{ km} \cdot \text{h}^{-1}$ ).

Rappel:

$$F_{in} = m \times \gamma + F_{ex}$$

Le profil peut être décomposé en 8 portions reprises dans le tableau ci-dessous. Les résultats concernant la zone de chantier ainsi que la phase de retour sont donnés. Le tableau permet de calculer l'énergie nécessaire pour effectuer un aller et un retour. Lors des phases de freinages, l'énergie n'est pas récupérée.

| Portion  | Pente  | Rayon   | Distance parcourue | Paramètre<br>constant                         | Durée  | F <sub>in</sub> (N) | E <sub>dep</sub><br>(W⋅h) |
|----------|--------|---------|--------------------|-----------------------------------------------|--------|---------------------|---------------------------|
| 1        | + 40 ‰ | 100 m   | 176 m              | $\gamma = 0.2 \text{ m} \cdot \text{s}^{-2}$  | 42 s   | 119 289             |                           |
| 2        | + 40 ‰ | 1 000 m | 424 m              | $V_0 = 30 \mathrm{km} \cdot \mathrm{h}^{-1}$  | 51 s   | 73 659              | 8 694                     |
| 3        | - 40 ‰ | 1 000 m | 400 m              | $V_0 = 30 \mathrm{km} \cdot \mathrm{h}^{-1}$  | 48 s   | -60 855             | 0                         |
| 4        | - 40 ‰ | 1 000 m | 27 m               | $\gamma = -1.5 \text{ m} \cdot \text{s}^{-2}$ | 6 s    | -317 955            | 0                         |
| 5        | + 30 % | 500 m   | 176 m              | $\gamma = 0.2 \text{ m} \cdot \text{s}^{-2}$  | 42 s   | 92 386              | 4 526                     |
| 6        | + 10 ‰ | 100 m   | 648 m              | $V_0 = 30 \mathrm{km} \cdot \mathrm{h}^{-1}$  | 78 s   |                     | 6 241                     |
| 7        | 0 ‰    | 7 500 m | 176 m              | $V_0 = 30 \mathrm{km} \cdot \mathrm{h}^{-1}$  | 21 s   | 5 309               |                           |
| 8        | 0 ‰    | 7 500 m | 27 m               | $\gamma = -1.5 \text{ m} \cdot \text{s}^{-2}$ | 6 s    | -251 790            | 0                         |
|          |        | 1       | 1                  |                                               |        | Total:              |                           |
| Chantier |        |         |                    |                                               | 12 000 |                     |                           |
| Retour   |        |         |                    |                                               | 12 550 |                     |                           |
| Total :  |        |         | otal :             |                                               |        |                     |                           |

#### **Question 4**

Compléter sur le document réponse DR1 le tableau et en déduire l'énergie  $E_{A\&R}$  nécessaire à la réalisation d'un trajet aller-retour.

#### **2.3 Énergie utilisée par le système de freinage pneumatique**

La rame MF67 possède un freinage pneumatique qui nécessite l'utilisation de compresseurs pour assurer l'alimentation en air comprimé des freins. On fait l'hypothèse que la consommation d'énergie du circuit de commande est négligeable devant celle du circuit de puissance.

L'énergie utilisée en phase de freinage est estimée à partir de mesures effectuées sur les compresseurs. Ces mesures permettent de déterminer la puissance absorbée par le moteur du compresseur qui fonctionne sur une durée de 6 minutes. La succession de ces durées de fonctionnement n'est pas périodique, elle dépend des demandes de freinage faites au cours de la nuit ainsi que des fuites des équipements.

La courbe de la figure 4 représente la puissance instantanée absorbée pendant un cycle de 6 minutes.

![](_page_7_Figure_4.jpeg)

**Figure 4 :** puissance consommée par les compresseurs d'un locotracteur

#### **Question 5**

*À partir de la courbe de la figure 4, calculer une valeur approchée de l'énergie Ecyc absorbée durant un cycle, en* W·h*.*

Une campagne de mesures effectuées sur les compresseurs durant trois nuits de travail sur chantier a permis de déterminer un nombre de mise en marche moyen de 17 fois par nuit et par locotracteur.

#### **Question 6**

*Calculer l'énergie moyenne Efreins utilisée par les compresseurs au cours d'une nuit de travaux.*

#### 2.4 Énergie consommée par le système de démarrage rhéostatique

Lors d'une phase de démarrage, le courant nécessaire au démarrage à accélération constante dans un moteur est considéré comme constant. La valeur du courant est de 380 A.

![](_page_8_Picture_2.jpeg)

**Figure 5 :** alimentation des moteurs au démarrage

Les quatre moteurs d'un bogie, lors du démarrage, sont connectés en série pour réduire la valeur de la tension à leurs bornes. Les rhéostats de démarrage permettent de maintenir le courant constant pendant cette phase. La tension aux bornes des moteurs est donnée par :

$$U_m = k_2 \cdot V$$
 avec  $V = \left\| \begin{matrix} \mathbf{u} \\ V_{train/sol} \end{matrix} \right\|$  la vitesse du train. On note :

- M<sub>1</sub>, M<sub>2</sub>, M<sub>3</sub> et M<sub>4</sub>, les moteurs du bogie;
- L<sub>1</sub>, L<sub>2</sub>, L<sub>3</sub> et L<sub>4</sub>, les inductances des moteurs du bogie;
- R<sub>th1</sub> et R<sub>th2</sub>, les rhéostats de démarrage.

Les calculs seront menés à partir des hypothèses suivantes :

- les résistances de bobinage d'induit et d'inducteur sont négligées ;
- toutes les chutes de tension inductive sont négligées.

#### **Question 7**

Donner l'expression du courant traversant l'induit des moteurs en fonction de  $V_{alim}$ , V,  $k_2$ ,  $R_{th1}$  et  $R_{th2}$ . En considérant  $R_{th1} = R_{th2}$  et un courant constant, déterminer la loi de commande des deux rhéostats  $R_{th1}$  et  $R_{th2}$  en fonction de V.

Rappel : l'énergie utilisée en fonction de la puissance est donnée par  $E = \int_{0}^{\Delta t} p(t) \cdot dt$ 

#### **Question 8**

Donner l'expression de la puissance instantanée p(t) dissipée par les deux rhéostats.

*À partir des réponses aux questions 1 et 8, donner l'expression de l'énergie utilisée ERh par ces rhéostats lors d'une phase de démarrage de durée Δ* <sup>1</sup> *t en fonction de* <sup>γ</sup> *, i, Valim, k*<sup>2</sup> *et Δ* <sup>1</sup> *t .*

Lors d'un trajet aller-retour, il y a quatre phases d'accélération d'une durée de 42 s et sur la zone de chantier il y a cinq phases d'accélération d'une durée de 7 s.

#### **Question 10**

*Calculer l'énergie totale ERHs dissipée lors des phases d'accélération avec k* <sup>−</sup> = ⋅ ⋅ <sup>1</sup> <sup>2</sup> 0,1V s m *.*

# **2.5 Énergie nécessaire totale**

L'énergie totale est :

$$E_{totale} = E_{A\&R} + E_{RHs} + E_{freins}$$

#### **Question 11**

*En déduire l'énergie totale utilisée pendant une nuit de travaux.*

# **3 Dimensionnement du système de stockage d'énergie**

*Objectif : choisir la technologie des batteries la mieux adaptée et étudier sa recharge.*

# **3.1 Choix des batteries**

Quels que soient les résultats trouvés précédemment, en tenant compte du rendement des équipements de la chaine de traction, la valeur de l'énergie nécessaire au déplacement du train pendant une nuit de travaux est évaluée à *Etotale* = 100 kW h⋅ **.**

Le questionnement suivant porte sur le choix d'un type de batterie, puis du dimensionnement.

De façon à préserver la durée de vie du bloc batterie, on impose une profondeur maximale de décharge de 80%, quelle que soit la technologie.

#### **Question 12**

*Calculer dans ces conditions la masse nécessaire du bloc batterie dans les deux cas de figure : batterie au plomb ou batterie au Lithium NCA. (voir document annexe A2).* 

*Commenter ces résultats en regard des valeurs utilisées dans le contexte de cette étude.* 

#### **Question 13**

*Choisir un type de batterie qui réponde au mieux au cahier des charges dans le contexte d'utilisation (voir document annexe A3), en expliquant la démarche de sélection.* 

Le concepteur du dispositif retient une solution basée sur une batterie d'accumulateurs Li-ion de tension nominale 515 V associés en parallèle (documentation en annexe A4), comme illustré à la figure 6.

![](_page_10_Figure_12.jpeg)

**Figure 6 :** synoptique de l'installation

*Calculer la capacité C en* A h⋅ *nécessaire avec les contraintes imposées. En déduire le nombre de modules Ion-Onboard à associer en parallèle dans le bloc batteries pour garantir le bon fonctionnement.*

#### **3.2 Dispositif de recharge de la batterie**

La partie grisée du synoptique de la figure 6 assure la recharge de la batterie d'accumulateurs en respectant les précautions nécessaires : chaque batterie Li-ion ayant des caractéristiques légèrement différentes des autres, il faut assurer le meilleur équilibrage possible des charges des différentes batteries. Ceci se fait au moyen d'un dispositif de balance qui ajuste le couplage des batteries.

L'algorithme de gestion de charge des batteries utilise les valeurs du courant, de la tension et de la température d'une batterie. Chaque bloc batterie est équipé de capteurs permettant de mesurer ces grandeurs. Les valeurs sont communiquées à l'unité de contrôle sur un réseau CANopen (voir figures 6 et 7). Le bus de données CAN, d'abord utilisé dans le secteur de l'automobile, est utilisé dans d'autres industries via des protocoles standardisés comme le protocole CANopen.

![](_page_11_Figure_5.jpeg)

**Figure 7** : détails de la topologie.

Les blocs batteries sont associés aux nœuds numéro 1 à n. Dans un réseau CANopen, les modules d'entrées/sorties peuvent être configurés pour transmettre cycliquement des trames de donnée (TPDO transmit-process data object). Chaque batterie transmet une trame TPDO dont l'identifiant est déterminé en utilisant la valeur 180h+n°du nœud. Le format d'une trame CAN et plus spécifiquement d'une trame TPDO issu d'un bloc batterie sont donnés en annexe A5.

Un traceur permet de visualiser les trames transitant sur ce réseau. La trame suivante a été récupérée (les valeurs sont données en hexadécimal) :

| ID   | DLC | Data1 | Data2 | Data3 | Data4 | Data5 | Data6 |
|------|-----|-------|-------|-------|-------|-------|-------|
| 182h | 05h | 7Eh   | 01h   | F1h   | FFh   | BAh   | C2h   |

Déterminer le numéro de la batterie ayant transmis cette trame.

#### **Question 16**

Déterminer la valeur de la tension mesurée.

#### **Question 17**

Déterminer la valeur du courant mesuré.

#### **Question 18**

Déterminer la température du bloc batterie.

Pour chaque batterie, un procédé de recharge indépendant dit CCCV est utilisé (courant constant puis tension constante). On obtient l'évolution des grandeurs caractéristiques au niveau d'une cellule élémentaire de la batterie de la figure 8 :

![](_page_12_Figure_9.jpeg)

Figure 8 : charge d'un module batterie

Le cycle de charge débute lorsque la tension cellule devient inférieure à 0,5 V, ce qui correspond à un état de charge de 10 % du maximum. L'état de charge final visé est de 90% du maximum. On considère donc que la charge dure ici 1,5 h.

Le niveau de courant envisagé lors de l'étape 1 est fixé au repère 1C, soit 56 A et la coupure se fait à 0,2C. Une élévation de plus de 5°C au cours de la recharge doit interrompre la charge pendant 10 minutes.

L'algorithme du programme de charge des étapes 1, 2 et 3 est fourni sur le document réponse DR2.

Les fonctions utilisées sont :

- − Lire\_tension() (renvoie la tension aux bornes d'une cellule) ;
- − Lire\_courant() (renvoie la valeur du courant de charge) ;
- − Fixe\_tension(2) (impose une tension de 2 V aux bornes d'une cellule) ;
- − Fixe\_courant(56) (impose un courant de charge de 56 A) ;
- − Lire\_temp() (renvoie la valeur de la température) ;
- − Pause (10) (bloque la charge pendant 10 min).

Les variables utilisées (nombres réels) sont *Temp* (température mesurée), *Vcell* (tension aux bornes d'une cellule), *Icharge* (courant de charge à travers une cellule), *Tinit* (température initiale).

# **Question 19**

*Compléter l'algorithme du document réponse DR2 pour que la charge suive les évolutions tracées sur la figure 8.*

Pour assurer la charge de l'association parallèle de batteries, deux approches sont envisageables : une recharge simultanée des batteries en parallèle ou une recharge des batteries les unes après les autres.

Dans le cas d'une recharge batterie après batterie, on utilise des commutateurs de puissance qui permettent de sélectionner une batterie à charger et de déconnecter les autres. Le contexte impose une durée maximale de recharge de 4 h. Pour les questions suivantes, on raisonne avec un système de stockage constitué de 5 batteries.

#### **Question 20**

*Dans le cas d'une recharge en parallèle, déterminer la valeur du courant à fournir par le chargeur pour que la charge complète du système de stockage soit effectuée en* 1,5 h*. Indiquer le problème qui risque de se poser en pratique avec ce procédé.*

#### **Question 21**

*En utilisant le courant nominal de charge préconisé par le constructeur (150 A), déterminer le nombre maximum de batterie pouvant être utilisées dans le système.* 

*Commenter la valeur obtenue au vu du contexte de l'application.*

#### **3.3 Restitution de l'énergie**

Le module nommé « Adaptation DC/DC » du synoptique assure le couplage entre la batterie d'accumulateurs et le module de puissance alimentant les moteurs.

On considère que la puissance moyenne à fournir au bloc de motorisation est de l'ordre de 96 kW, le rendement du module « Adaptation DC/DC » et du module de puissance étant respectivement de 97% et 95%.

*Calculer le courant moyen de décharge de la batterie d'accumulateurs. Justifier que cette valeur est adaptée au type de batterie choisie.*

# **4 Dimensionnement des moteurs de traction**

*Objectif : vérifier que les moteurs des essieux suffisent à démarrer puis à tracter le véhicule.*

Les moteurs équipant la rame de métro sont des moteurs à courant continu. Il s'agit ici de vérifier qu'ils sont bien dimensionnés, en régime permanent, pour la traction de la rame VMI 67.

# **4.1 Aptitude à la traction du véhicule**

L'étude menée dans la partie 2 du sujet a permis de déterminer l'effort total de traction de la rame *Fin* , devant être générée par la motorisation pour faire démarrer le véhicule avec une accélération de <sup>γ</sup> <sup>−</sup> = ⋅ <sup>2</sup> 0,2 m s , en tenant compte de l'effort à l'arrachement. Cet effort est estimé à *Fin* = 128,5 kN.

La rame est composée de deux motrices et de trois wagons. Chaque motrice, de masse *m*1, possède quatre essieux motorisés.

# **Question 23**

*Déterminer l'effort de traction Fe , générée par un moteur, lors d'un déplacement du véhicule.*

Lors d'un déplacement, la condition de roulement sans glissement doit être vérifiée pour qu'il n'y ait pas de patinage au niveau des roues motrices. Ainsi, l'effort de traction *Fe* doit vérifier l'inégalité suivante : *F N e re* < <sup>µ</sup> ⋅ ,

avec <sup>µ</sup>*<sup>r</sup>* , le coefficient d'adhérence des roues d'un essieu par rapport aux rails ; *Ne*, l'effort normal au niveau d'un essieu.

![](_page_14_Picture_12.jpeg)

**Figure 9 :** motrice d'une rame

Nous supposerons que la charge liée au poids *P* de la motrice est uniformément répartie sur les quatre essieux motorisés.

Données complémentaires pour les questions suivantes :

| Masse d'une motrice<br>(sans batterie d'accumulateur) | m1<br>=<br>38<br>120<br>kg      |
|-------------------------------------------------------|---------------------------------|
| Adhérence                                             | 0,12<br>=<br>µr                 |
| Pente de la voie                                      | i<br>= 40 ‰                     |
| Accélération de la pesanteur                          | s−<br>2<br>g<br>=<br>9,81m<br>⋅ |

#### **Question 24**

*Déterminer l'effort normal Ne, et vérifier la condition de roulement sans glissement.* 

Nous supposerons par la suite que les conditions pour qu'il y ait roulement sans glissement sont réunies.

# **4.2 Vérification du dimensionnement du moteur**

Chaque moteur à courant continu est relié à l'axe de rotation de l'essieu par l'intermédiaire d'un réducteur, de rapport de réduction *ρ* et de rendement η*red* . Deux roues, de diamètre *de* , sont solidaires de l'essieu.

![](_page_15_Picture_8.jpeg)

**Figure 10 :** motorisation d'un essieu

Données complémentaires pour les questions suivantes :

| Diamètre d'une roue    | de<br>0,86<br>m<br>= |
|------------------------|----------------------|
| Rapport de réduction   | ρ =<br>0,17          |
| Rendement du réducteur | =<br>97<br>%<br>ηred |

Lorsque le couple développé par une machine n'est pas constant sur son cycle de fonctionnement, il est nécessaire de connaître le couple thermique équivalent pour dimensionner un moteur. Ce couple, noté  $C_{th}$ , est équivalent à un couple constant qui provoquerait le même échauffement. Il est défini par :

$$C_{th} = \sqrt{\frac{1}{T} \int_{0}^{T} C_{m}^{2}(t) dt}$$

Le trajet de la rame de métro a déjà été décrit à la partie 2-2. Il se compose d'une zone de transfert et d'une zone sur chantier. L'effort de traction  $F_{\rm e}$ , qui doit être généré par un moteur, n'est pas constant sur le trajet et son évolution est décrite à la figure 11.

![](_page_16_Figure_3.jpeg)

Figure 11 : évolution temporelle de l'effort de traction sur le trajet

Le trajet aller-retour, avec la phase sur chantier, est composé de 18 phases à effort de traction constant. Ainsi, le couple thermique équivalent s'exprime par :

$$C_{th} = \sqrt{\frac{1}{T} \left( C_{m1}^2 \cdot \Delta t_1 + C_{m2}^2 \cdot \Delta t_2 + \sum_{i=3}^{18} C_{mi}^2 \cdot \Delta t_i \right)}$$

Données complémentaires pour les questions suivantes :

| Effort de traction durant la phase 1 du trajet     | $F_{\rm e1} = 14,9  \rm kN$                                  |
|----------------------------------------------------|--------------------------------------------------------------|
| Effort de traction durant la phase 2 du trajet     | $F_{e2} = 9.2  \text{kN}$                                    |
| Durée de la phase 1 du trajet                      | $\Delta t_1 = 42 \text{ s}$                                  |
| Durée de la phase 2 du trajet                      | $\Delta t_2 = 51 \mathrm{s}$                                 |
| Durée totale de trajet                             | T = 2048 s                                                   |
| Terme de la formule du couple équivalent thermique | $\sum_{i=3}^{18} C_{mi}^2 \cdot \Delta t_i = 558 \cdot 10^6$ |

*Exprimer le couple Ce au niveau des roues d'un essieu en fonction de Fe . Calculer les couples Ce*<sup>1</sup> *et Ce*<sup>2</sup> *des phases 1 et 2 du trajet.*

#### **Question 26**

*En raisonnant sur les puissances, et en tenant compte du rendement du réducteur* η*red , exprimer le couple moteur Cm en fonction Ce ,* η*red et* <sup>ρ</sup> *. Calculer alors les couples Cm*<sup>1</sup> *et Cm*2*.*

#### **Question 27**

*En déduire le couple thermique équivalent Cth sur le cycle de fonctionnement de la rame de métro.*

Les moteurs actuellement utilisés sont des moteurs Alsthom à courant continu. Leurs caractéristiques techniques sont fournies dans le tableau ci-dessous.

| Tension nominale   | 360<br>V                      |
|--------------------|-------------------------------|
| Courant nominal    | 305<br>A                      |
| Puissance nominale | 96<br>kW                      |
| Vitesse nominale   | − ⋅<br>1<br>1035<br>tr<br>min |

#### **Question 28**

*A partir des caractéristiques techniques des moteurs à courant continu, calculer le couple nominal Cnom des moteurs. Conclure sur la possibilité d'utiliser ces moteurs pour tracter la rame de métro.*

# **5 Synthèse**

*Objectif : Valider ou invalider la faisabilité de transformer d'anciennes motrices de rames de métro en VMI.*

Dans ce sujet, plusieurs points ont été abordés pour étudier la faisabilité d'utiliser d'anciennes motrices de rames de métro pour des véhicules de maintenance.

#### **Question 29**

*Faire le bilan des investissements que devra faire le réseau Métro pour développer de nouveaux véhicules de maintenance industriels à partir d'anciennes motrices de rame de métro.*

L'étude a montré que l'adhérence des roues était primordiale lors de l'effort d'arrachement de la rame. Pour que la rame puisse démarrer, il faut que la condition de roulement sans glissement soit vérifiée :

$$F_{\rm e} < \mu_{\rm r} \cdot N_{\rm e}$$

avec <sup>µ</sup>*<sup>r</sup>* , le coefficient d'adhérence des roues d'un essieu par rapport aux rails ;

*Ne*, l'effort normal au niveau d'un essieu,

*Fe* **,** l'effort de traction généré par un moteur.

#### **Question 30**

*Indiquer sur quels paramètres il est possible d'agir pour vérifier la condition de roulement sans glissement.*

# **DOCUMENTS ANNEXES**

![](_page_19_Picture_2.jpeg)

**Profils temporels du trajet ALLER sur la zone de transfert**  0 
 30 
 20 
 10 
 0 
 50 
 100 
 150 
 200 
 250 
 300 
 **Vitesse 
 (m/s) 
 Temps 
 (s)**  0 
 8000 
 6000 
 4000 
 2000 
 0 
 50 
 100 
 150 
 200 
 250 
 300 
 **Rayon 
 de 
 courbure 
 (m) 
 Temps 
 (s)**  -‐20 
 -‐40 
 0 
 40 
 20 
 0 
 50 
 100 
 150 
 200 
 250 
 300 
 **Pente 
 (‰) 
 Temps 
 (s)** 

**Document annexe A1** 

19 / 26

#### **Document annexe A2 Comparatif de technologies de batterie**

#### **Tableau comparatif des densités d'énergie massique**

![](_page_21_Figure_2.jpeg)

#### Légende :

#### Batteries classiques

Lead acid = batterie au plomb

NiCd = batterie Nickel Cadmium

NiMH = batterie Nickel Métal Hybride

#### Batteries au Lithium

LTO = Lithium Titanate

LFP = Lithium Fer Phosphate

LMO = Lithium Oxyde de Manganèse Cobalt

NMC = Lithium Oxyde de Nickel Manganèse Cobalt

LCO = Lithium Oxyde de Cobalt

NCA = Lithium Oxyde de Nickel Cobalt Aluminium

# **Document annexe A3** Tableau comparatif de technologies de batteries

| Type de<br>batterie | Lithium ion                                                                                                                                                                                                   | Plomb                                                                                                                       | Nickel Cadmium                                                                                                            |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inconvénients       | Nécessité d'un dispositif<br>de<br>recharge<br>adapté<br>(respect<br>absolu<br>des<br>normes<br>pour<br>des<br>problèmes de sécurité)<br>Technologie en cours de<br>développement<br>Recyclage très technique | Poids et encombrement<br>Débit<br>de<br>courant<br>très<br>importants<br>Pollution forte par plomb<br>en cas de destruction | Polluantes à cause du<br>cadmium<br>Décharge rapide<br>Tension faible<br>Effet mémoire                                    |
| Avantages           | Charge rapide<br>Forte tension<br>Pas d'effet mémoire<br>Rapport<br>encombrement/puissance<br>favorable<br>Rapport<br>encombrement/poids<br>favorable                                                         | Recyclage facile<br>Stockage longue durée<br>(décharge lente)<br>Faible coût<br>Technologie éprouvée                        | Acceptent les courants<br>forts<br>Très endurantes<br>Stockage<br>à<br>faible<br>niveau de charge<br>Technologie éprouvée |

#### Document annexe A4

# Documentation technique des modules batterie Li-ion

# Saft Ion-OnBoard® Regen Li-ion for Rail Battery system 515 V - 218 kW

Innovative battery system for regenerative energy storage for light rail rolling stock.

Saft's Ion-OnBoard® Regen Li-ion battery system 515 V - 218 kW battery unit has a nominal voltage of 515 V and is able to provide high discharge capability up to 218 kW in 30 s and store 232 kW of regen power in 10 s.

One battery system consists of:

- 26 Saft Modul'ion®-12
   (Mi 12-20.60 PFe) Super-Phosphate™
   (SLFP) connected in series
- Power box equipped with a manual switch, contactor and fuses
- Liquid cooling system and, as an option, a BTMS <sup>(1)</sup> for battery management

The Modul'ion®-12 and the power box are placed in a metallic box 'Long' type.

#### Applications

- For light rail systems: trams, streetcars and tram-trains
- To supply autonomous traction power for catenary free
- To store kinetic braking energy (regenerative braking) and reuse it for autonomous traction
- To maintain power quality for the local distribution network

#### Features

- Quick and high recharge capabilities (e.g. regenerative braking application)
- High life cycle performance
- Light weight and compact design for rail applications
- Robust construction withstanding onboard vehicle shocks and vibrations
- Liquid cooled system

#### Benefits

- High rate charge and discharge capability for an always available system
- Easy installation (roof mounted assembly)
- Minimum maintenance
- Reduced CO₂ footprint and saved energy
- [1] BTMS: Battery Thermal Management

![](_page_23_Picture_27.jpeg)

| Nominal characteristics                              | Values for 1 box                              |
|------------------------------------------------------|-----------------------------------------------|
| Li-ion module                                        | Modulion®-12 20.60 PFe                        |
| Number of modules in series                          | 2 rows of 13                                  |
| Voltage (Min/Max)                                    | 390 V - 601 V                                 |
| Nominal voltage                                      | 515V                                          |
| Rated capacity at C₅                                 | 56 Ah                                         |
| Rated energy at C <sub>5</sub>                       | 28.8 kWh                                      |
| Energy at C                                          | 28.7 kWh                                      |
| Mechanical characteristics                           |                                               |
| Dimensions (without BTMS) Lx W x H (mm)              | 1,713 x 1,385 x 300                           |
| Weight (without BTMS) (kg)                           | 621                                           |
| Cooling                                              | Liquid cooled                                 |
| Electrical characteristics at + 25℃                  |                                               |
| Nominal continuous current/power in charge/discharge | 150 A*/77 kW                                  |
| Maximum pulse power:                                 | ET-88 1 10 10 10 10 10 10 10 10 10 10 10 10 1 |
| - in 10 s in charge                                  | 450 A/232 kW                                  |
| - in 30 s in discharge                               | 424 A/ 218 kW                                 |
| Operating conditions                                 |                                               |
| Operating temperature                                | -25°C to +45°C (with BTMS)                    |
| Temperature for transport and storage                |                                               |
| - recommended                                        | -10°C to +30°C                                |
| - possible                                           | -30°C to +70°C                                |
| Maximum relative humidity                            | Up to 90%                                     |
| Maximum sound power level                            | < or= 84.5 dB(A)                              |

<sup>\*</sup>Typical values. To be sized according to customer load and cycle profile

![](_page_23_Picture_30.jpeg)

# **Document annexe A5**

# Bus CAN 2.0A « hign speed »

Description de la couche liaison de donnée (format d'une trame) :

![](_page_24_Figure_3.jpeg)

#### **SOF (Start of Frame)**

Constitué par un seul bit, de niveau dominant (0 par convention), indique aux nœuds le début de la trame. La détection du front descendant du SOF par les nœuds va leur permettre de se synchroniser sur la trame en cours de transmission.

# **Champ d'arbitrage**

Constitué de l'identificateur du message (11 bits en trame standard) et du bit RTR (Remote Transmission Request). L'identificateur de longueur 11 bits permet d'attribuer une adresse spécifique à chaque message.

**Le bit RTR** de niveau dominant (0) indique que c'est une trame de données qui est en cours de transmission. Le bit RTR de niveau récessif (1 par convention) indique que c'est une trame de requête (absence du champ de données) qui est en cours de transmission.

#### **Champ de commande constitué de 6 bits :**

- − 2 bits r1 et r0 : sont réservés et toujours au niveau dominant (0),
- − 4 bits formant le champ DLC qui indiquent le nombre d'octets qui seront transmis dans le champ de données.

**Champ de données :** Constitué de 0 à 8 octets maximums de données utiles.

**Champ CRC :** C'est un code de contrôle, constitué de 15 bits, suivi d'un bit délimiteur au niveau récessif (1).

**Champ d'acquittement :** ACK Constitué de 2 bits

**Fin de trame EOF :** Constitué de 7 bits au niveau récessif (1), il permet d'identifier la fin de la trame.

#### **Protocole CANopen**

Description d'une trame TPDO d'un bloc batterie :

| ID            | DLC | Data1  | Data2  | Data3 | Data4 | Data5  | Data6  |  |
|---------------|-----|--------|--------|-------|-------|--------|--------|--|
| 180h+n° noeud | 5   | Temp_L | Temp_H | Amp_L | Amp_H | Volt_L | Volt_H |  |

**La mesure de la température** est transmise sur deux octets en complément à 2 : Temp\_L est l'octet de poids faible et Temp\_H l'octet de poids fort. La température est transmise par nombre de dixièmes de degrés. Exemple : une température de 200,8° sera transmise avec Temp\_L=D8h et Temp\_H=07h

**La valeur du courant** est transmise sur deux octets en complément à 2, le courant est positif lors de la décharge. Exemple : pour un courant de décharge de 100 A, Amp\_L=64h et Amp\_H=00h.

**La mesure de la tension** est transmise sur deux octets en complément à 2 : Volt\_L est l'octet de poids faible et Volt\_H l'octet de poids fort. La tension est transmise par nombre dizaine de millivolt. Exemple : une tension de 515,34V sera transmise avec Volt\_L=4Eh et Volt\_H=C9h.

| Modèle CMEN-D         | OC v2 ©NEOPTEC                                                                                                                                                                                                                   |          |        |             |          |          |          |         |           |         |        |        |       |      |      |    |      |    |      |      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------|-------------|----------|----------|----------|---------|-----------|---------|--------|--------|-------|------|------|----|------|----|------|------|
| Non                   | n de famille : lieu, du nom d'usage)                                                                                                                                                                                             |          |        | $\prod$     |          |          |          |         |           |         |        |        |       |      |      |    |      |    |      |      |
|                       | Prénom(s) :                                                                                                                                                                                                                      |          |        |             |          |          |          |         |           |         |        |        |       |      |      |    |      |    |      |      |
|                       | Numéro<br>Inscription :                                                                                                                                                                                                          |          |        |             |          |          |          |         |           |         |        | ı      | é(e)  | le : |      | ]/ |      | ]/ |      |      |
|                       | (Le                                                                                                                                                                                                                              | e numéro | est ce | lui qui fiç | gure sur | r la cor | nvocatio | on ou l | la feuill | le d'ém | argeme | nt)    |       |      |      |    | <br> |    | <br> | <br> |
| (Remplir cette partie | à l'aide de la notice)  / Examen:                                                                                                                                                                                                |          |        |             |          |          |          | Se      | ectio     | n/Sp    | oécia  | lité/S | Série | :    | <br> |    | <br> |    | <br> | <br> |
|                       | Epreuve : Matière : Session :                                                                                                                                                                                                    |          |        |             |          |          |          |         |           |         |        |        |       |      |      |    |      |    |      |      |
| CONSIGNES             | <ul> <li>Remplir soigneusement, sur CHAQUE feuille officielle, la zone d'identification en MAJUSCULES.</li> <li>Ne pas signer la composition et ne pas y apporter de signe distinctif pouvant indiquer sa provenance.</li> </ul> |          |        |             |          |          |          |         |           |         |        |        |       |      |      |    |      |    |      |      |

EDE ENE 2

# **Documents réponses**

Tous les documents réponses sont à rendre, même non complétés.

#### **NE RIEN ECRIRE DANS CE CADRE**

#### **Document réponse DR1 (réponse à la question 4)**

| Portion  | Pente     | Rayon         | Distance<br>parcourue | Paramètre<br>constant                       | Durée   | Fin<br>(N)  | Edep<br>(W·h) |
|----------|-----------|---------------|-----------------------|---------------------------------------------|---------|-------------|---------------|
| 1        | + 40 ‰    | 100<br>m      | 176<br>m              | −<br>2<br>=<br>0,2 m<br>⋅<br>s<br>γ         | 42<br>s | 119 289     |               |
| 2        | + 40 ‰    | 1<br>000<br>m | 424<br>m              | −<br>1<br>V<br>=<br>30<br>km<br>⋅<br>h<br>0 | 51<br>s | 73 659      | 8 694         |
| 3        | -<br>40 ‰ | 1<br>000<br>m | 400<br>m              | 1<br>−<br>V<br>=<br>30<br>km<br>⋅<br>h<br>0 | 48<br>s | -60 855     | 0             |
| 4        | -<br>40 ‰ | 1<br>000<br>m | 27 m                  | s−<br>2<br>1,5 m<br>=<br>−<br>⋅<br>γ        | 6 s     | -317<br>955 | 0             |
| 5        | + 30 ‰    | 500<br>m      | 176<br>m              | −<br>2<br>0,2 m<br>s<br>=<br>⋅<br>γ         | 42<br>s | 92<br>386   | 4 526         |
| 6        | + 10 ‰    | 100<br>m      | 648<br>m              | 1<br>−<br>V<br>30<br>km<br>h<br>=<br>⋅<br>0 | 78<br>s |             | 6<br>241      |
| 7        | 0 ‰       | 7<br>500<br>m | 176<br>m              | −<br>1<br>V<br>30<br>km<br>h<br>=<br>⋅<br>0 | 21<br>s | 5 309       |               |
| 8        | 0 ‰       | 7<br>500<br>m | 27<br>m               | s−<br>2<br>1,5 m<br>=<br>−<br>⋅<br>γ        | 6 s     | -251<br>790 | 0             |
|          |           |               |                       |                                             |         | Total<br>:  |               |
| Chantier |           |               |                       |                                             |         |             | 12 000        |
| Retour   |           |               |                       |                                             |         |             | 12 550        |
|          |           |               |                       |                                             |         | Total :     |               |

#### **Document réponse DR2 (réponse à la question 19)**

Compléter le programme de charge d'un module batterie :

![](_page_27_Figure_2.jpeg)