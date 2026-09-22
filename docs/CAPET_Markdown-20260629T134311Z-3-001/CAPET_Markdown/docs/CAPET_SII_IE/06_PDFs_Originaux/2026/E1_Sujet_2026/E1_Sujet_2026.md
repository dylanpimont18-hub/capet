**==> picture [66 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
LDE ENE 1<br>**----- End of picture text -----**<br>


## **SESSION 2026** 

____ Δ 

# CAPET CONCOURS EXTERNE ET CAFEP CORRESPONDANT (BAC + 3) 

# **Section : SCIENCES INDUSTRIELLES DE L’INGÉNIEUR** 

# **Option : INGÉNIERIE ÉLECTRIQUE** 

## **ADMISSIBILITÉ : ÉPREUVE 1** 

_L'épreuve consiste en l'étude de la modélisation d'un produit._ 

_Elle a pour objectif de vérifier la capacité du candidat à conduire une étude d'un produit pour en caractériser les performances en mobilisant ses connaissances scientifiques et technologiques relevant de l'option du concours._ 

_L'épreuve est constituée de plusieurs parties indépendantes, certaines d'entre elles sont à traiter obligatoirement et d'autres sont au choix du candidat._ 

## Durée : 4 heures 

____ 

_Calculatrice autorisée selon les modalités de la circulaire du 17 juin 2021 publiée au BOEN du 29 juillet 2021. L’usage de tout ouvrage de référence, de tout dictionnaire et de tout autre matériel électronique est rigoureusement interdit._ 

_Il appartient au candidat de vérifier qu’il a reçu un sujet complet et correspondant à l’épreuve à laquelle il se présente._ 

_Si vous repérez ce qui vous semble être une erreur d’énoncé, vous devez le signaler très lisiblement sur votre copie, en proposer la correction et poursuivre l’épreuve en conséquence.  De même, si cela vous conduit à formuler une ou plusieurs hypothèses, vous devez la (ou les) mentionner explicitement._ 

**NB : Conformément au principe d’anonymat, votre copie ne doit comporter aucun signe distinctif, tel que nom, signature, origine, etc. Si le travail qui vous est demandé consiste notamment en la rédaction d’un projet ou d’une note, vous devrez impérativement vous abstenir de la signer ou de l’identifier. Le fait de rendre une copie blanche est éliminatoire.** 

A 

**Tournez la page S.V.P.** 

## **INFORMATION AUX CANDIDATS** 

Vous trouverez ci-après les codes nécessaires vous permettant de compléter les rubriques figurant en en-tête de votre copie. 

Ces codes doivent être reportés sur chacune des copies que vous remettrez. 

## **► Concours externe du CAPET de l’enseignement public** : 

Concours Section/option Epreuve Matière 

## **► Concours externe du CAFEP/CAPET de l’enseignement privé** : 

Concours Section/option Epreuve Matière 

‒ 2 ‒ 

LDE ENE 1 

## **Conseils aux candidats** 

Il est demandé aux candidats : 

- de rédiger les réponses aux différents parties sur des feuilles de copie séparées et clairement repérées ; 

- de numéroter chaque feuille de copie et indiquer le numéro de la question traitée ; 

- de rendre tous les documents réponses, même non complétés ; 

- d’utiliser exclusivement les notations indiquées dans le sujet lors de la rédaction des réponses ; 

- de justifier clairement les réponses ; 

- d’encadrer ou souligner les résultats ; 

- de présenter lisiblement les applications numériques, sans omettre les unités, après avoir explicité les expressions littérales des calculs ; 

- de formuler les hypothèses nécessaires à la résolution des problèmes posés si celles-ci ne sont pas indiquées dans le sujet. 

## **Sommaire** 

Page **Sommaire ..................................................................................................................................................... 1 Présentation du support ............................................................................................................................. 2 Partie A (à traiter obligatoirement) ............................................................................................................ 3 Partie B (à traiter obligatoirement) ............................................................................................................ 6 Partie C (à traiter obligatoirement) ............................................................................................................ 9 Partie D (choix 1) ....................................................................................................................................... 12 Partie E (choix 2) ........................................................................................................................................ 16** 

Les parties A, B et C sont à traiter obligatoirement par tous les candidats. 

Les candidats devront choisir de traiter la partie D (choix 1) ou la partie E (choix 2). 

B 

**Tournez la page S.V.P.** 

Page 1 

## **Présentation du support** 

## **BUS HYDROGÈNE HYCITY[®]** 

Hycity[®] est le dernier né des autobus hydrogène fabriqués par la société Safra. Cet autobus offre aux autorités organisatrices de mobilité une alternative écologique pour évoluer audelà des énergies fossiles. Hycity[®] ne produit pas de CO2 ni de particules fines au roulage, et ne rejette que de l’eau. 

Grâce à la technologie hydrogène, ces véhicules contribuent à la neutralité carbone et répondent donc parfaitement à la réglementation française et européenne sur les véhicules propres. 

**==> picture [231 x 42] intentionally omitted <==**

**----- Start of picture text -----**<br>
Communication entre la pile à combustible<br>Symbio et le calculateur du Hycity [®] , basée<br>sur une architecture bus CAN<br>**----- End of picture text -----**<br>


**==> picture [424 x 58] intentionally omitted <==**

**----- Start of picture text -----**<br>
Onduleur de type MLI  Asservissement en vitesse de<br>permettant la variation  l’ouverture et la fermeture des<br>de vitesse de l’essieu  portes<br>motorisé ZF AVE 130<br>**----- End of picture text -----**<br>


Présentation du bus Hycity[®] 

Les parties proposées sont toutes indépendantes et exploitent une partie des constituants du bus Hycity[®] . 

Les parties A, B et C proposent des problématiques autour de l’ouverture et la fermeture des portes du bus. 

La partie D s’intéresse au système de transmission entre le calculateur et les différents constituants tels que la pile à combustible. 

La partie E a pour objet la recharge de la batterie de secours à partir du réseau via un redresseur triphasé. 

Page 2 

## **Partie A (à traiter obligatoirement)** 

## **Évaluer les performances d'un actionneur électrique** 

L’ouverture et la fermeture des portes du bus est assurée par un actionneur à courant continu à excitation constante. Les principales notations utilisées dans cette étude sont données ci-dessous. 

|**Symbole**|**Grandeur**|**Unité**|
|---|---|---|
|u(t)|Tension aux bornes de l’induit de l’actionneur|V|
|N(t)|Vitesse de rotation de l’actionneur|tr·min-1|
|i(t)|Courant absorbé par l’induit de l’actionneur|A|
|Ω(t)|Vitesse de rotation de l’actionneur|rad·s-1|
|L|Inductance de l’induit de l’actionneur|mH|
|R|Résistance de l’induit de l’actionneur|W|
|e(t)|Force contre électromotrice de l’actionneur : e(t) = Ke∙Ω(t)|V|
|Ke|Constante de force contre électromotrice|V·s·rad-1|
|Kc|Constante de couple (Kc =Ke)|Nm·A-1|
|CP|Couple de pertes|N⋅m|
|CU|Couple utile|N⋅m|
|CR|Couple résistant|N⋅m|
|η|Rendement de l’actionneur hors excitation||



**Objectif :** Vérifier que l'actionneur électrique permet d'assurer toutes les phases de fonctionnement de la porte du bus. 

## **Détermination des paramètres du modèle de l'actionneur** 

Le schéma de l'induit de l'actionneur électrique est donné figure A1. 

**==> picture [120 x 143] intentionally omitted <==**

**----- Start of picture text -----**<br>
i(t)<br>L<br>u(t)  R<br>e(t)<br>4<br>**----- End of picture text -----**<br>


Figure A1 – Schéma électrique de l'induit de la machine à courant continu 

**Tournez la page S.V.P.** 

Page 3 

**Question A1** Donner l’équation électrique permettant d’exprimer u(t) en fonction de R, L, e(t) et de i(t). Préciser ce que devient cette équation en régime permanent (grandeurs continues). 

Un extrait de la documentation constructeur de l’actionneur, pour un fonctionnement en régime nominal, est donné ci-dessous : 

- tension nominale : Un = 200 V ; 

- courant nominal : In = 0,5 A ; 

- vitesse de rotation nominale : Nn = 1800 tr·min[ -1] . 

**==> picture [486 x 260] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lors d'un essai à rotor bloqué sous tension réduite U = 3,3 V, l'évolution du courant absorbé<br>par le moteur i(t) est régie par une équation différentielle d'ordre 1 à coefficients constants<br>L<br>dont la constante de temps est τ = . Cette évolution est représentée figure A2.<br>R<br>u(t) (V)<br>3,3<br>t (ms)<br>—<br>0  5  15  30<br>i(t) (A)<br>0,5<br>t (ms)<br>0  5  15  30<br>**----- End of picture text -----**<br>


Figure A2 – Évolutions de u(t) et i(t) lors d'un essai à rotor bloqué 

## **Question A2** 

Simplifier l'équation obtenue question A1 dans le cadre de l'essai à rotor bloqué lorsque le régime permanent est atteint. En déduire la valeur de R. Déterminer la valeur du courant absorbé par l’actionneur en régime permanent si cet essai avait été fait sous tension nominale. Justifier alors le choix d’effectuer cet essai sous tension réduite. 

**Question A3** En exploitant la figure A2, déterminer la valeur de l'inductance L. 

Indépendamment des résultats obtenus, pour la suite de l’étude les valeurs numériques suivantes seront retenues : 

R = 6,6 Ω ; L = 100 mH. 

**Question A4** En utilisant le fonctionnement en régime nominal permanent déterminer la valeur de la constante Ke. 

Lors d'un essai à vide, la tension d'alimentation est de 200 V et le courant absorbé par l'induit de l'actionneur de 0,05 A en régime permanent. 

Page 4 

## **Question A5** 

Déterminer l’expression, puis la valeur numérique de Cp qui représente le couple de pertes. Cette valeur sera supposée constante par la suite. 

## **Détermination des points de fonctionnement** 

La figure A3 représente les différentes puissances mises en jeu dans l’induit de l'actionneur électrique. 

**==> picture [287 x 74] intentionally omitted <==**

**----- Start of picture text -----**<br>
PA PEM PU<br>PJR PFM<br>**----- End of picture text -----**<br>


Figure A3 – Schéma d’écoulement des puissances de l’actionneur 

Indépendamment des résultats obtenus, pour la suite de l’étude les valeurs numériques suivantes seront retenues : 

Ke = 1,044 V·s·rad[-1 ] ; Kc = 1,044 Nm·A[-1] et  Cp = 0,052 Nm. 

- **Question A6** En régime nominal, déterminer successivement les expressions puis les valeurs numériques de la puissance active PA, des pertes Joule PJR, de la puissance électro-magnétique PEM , des pertes fer PFM , de la puissance utile PU et du rendement du moteur η. 

**Question A7** Établir les équations numériques CU = f(N) pour U = 200 V et U = 150 V. 

Le document réponse DRA1 présente l'évolution de la caractéristique mécanique de l'actionneur CU = f(N) pour U = 200 V. 

**Question A8** Tracer l’évolution du couple utile CU en fonction de la vitesse de rotation N sur le document réponse DRA1 pour U = 150 V. 

La charge que doit entraîner l’actionneur électrique impose un couple résistant constant quel que soit la vitesse tel que CR = 0,4 Nm. 

- **Question A9** Tracer l’évolution du couple résistant CR  en fonction de N sur le document réponse DRA1. Identifier les points de fonctionnement du moteur (couple utile et fréquence de rotation) pour les deux valeurs de tension de commande U considérées (200 V et 150 V). 

L’actionneur électrique doit être capable d’entrainer la charge suivant deux sens de rotation (fonctionnement moteur uniquement). Le document réponse DRA2 présente le plan couplevitesse de l’actionneur. 

- **Question A10** Identifier les grandeurs électriques de commande (U et I) que l'on peut associer aux grandeurs mécaniques (C et Ω ) dans une machine à courant continu puis compléter le document réponse DRA2 en hachurant les quadrants de fonctionnement correspondant aux besoins. Conclure en proposant une structure de variateur de vitesse permettant de répondre aux besoins. 

**Tournez la page S.V.P.** 

Page 5 

Partie B (a traiter obligatoirement) 

## Qualifier la qualité d'une opération de filtrage 

La chaine de mesure du sous-systeme permettant d’acquérir la position angulaire de la porte du bus est constituée d’un capteur potentiométrique, d’un conditionneur, d'un amplificateur, d’un filtre et d'un convertisseur analogique numérique comme représenté sur la figure B1. 

**==> picture [457 x 62] intentionally omitted <==**

**----- Start of picture text -----**<br>
Position<br>angulaire Convertisseur<br>de la porte =ayteue Vaa(t) Amplificateur va(t) va(t) analogique / GN<br>conditionneur numérique<br>**----- End of picture text -----**<br>


Figure B1 — Chaine d'acquisition de la mesure de position angulaire 

Objectif: Valider les performances de la structure de filtrage du signal de mesure de la position angulaire de la porte du bus. 

## Evaluation des besoins du filtre 

La mesure du signal fourni par l'ensemble {capteur + conditionneur + amplificateur} permet de mettre en évidence la présence d’un signal perturbateur non désiré (présence des actionneurs électriques pres du capteur). La figure B2 donne le spectre du signal v>, sachant que v2(t) = Vo + A- Sin(Wot). 

**==> picture [408 x 236] intentionally omitted <==**

**----- Start of picture text -----**<br>
Spectre du signal v2<br>2.5 | | |<br>2V<br>= af<br>&<br>=]<br>z<br>=<br>o 1.5<br>E<br>©<br>£<br>a<br>2 1<br>@ 0,5V<br>To<br>=<br>©<br>3B  0.5-0 -|<br>i | | | ! |<br>0 200 400 600 800 1000 1200 1400 1600 1800 2000<br>fréquence (Hz)<br>**----- End of picture text -----**<br>


Figure B2 — Spectre du signal v>(t) 

Question B1 En exploitant la figure B2, déterminer les valeurs numériques de Vo, A et W>. Identifier ensuite dans le signal v2(t) le signal informatif (proportionnel a la mesure de position angulaire) et le signal perturbateur. 

Page 6 

V3 ( jω ) Le filtre à mettre en place est caractérisé par sa fonction de transfert : HFi ( jω ) = et ~~_~~ V2 ( jω ) doit respecter le cahier des charges résumé par le tableau ci-dessous et le gabarit présenté sur le document réponse DRB1. 

|doit respecter le cahier des charges résumé par le tableau ci-dessous et le gabarit présenté<br>sur le document réponse DRB1.|doit respecter le cahier des charges résumé par le tableau ci-dessous et le gabarit présenté|
|---|---|
|Facteur d’atténuation du signal perturbateur|>100|
|Temps de réponse à 5 %|<50 ms|



**Question B2** Déterminer la valeur du gain en dB du filtre pour la pulsation ω2 afin de respecter la première exigence du cahier des charges. Placer ce point nommé P1  (pulsation et gain) sur le document réponse DRB1. En déduire l'ordre et le type du filtre à mettre en place pour respecter le cahier des charges. 

## **Première proposition de filtre** 

Le constructeur a choisi un filtre passif dont la structure est présentée à la figure B3. 

|Figure B3 – Schéma électrique du premier filtre retenu<br>R<br>V2<br>C<br>V3<br>I<br>~~bti~~|Figure B3 – Schéma électrique du premier filtre retenu<br>Résistance<br>d'entrée de<br>l'étage qui suit<br>le filtre,<br>considérée<br>infinie.|
|---|---|



Figure B3 – Schéma électrique du premier filtre retenu 

Indépendamment des résultats obtenus, pour la suite de l’étude les valeurs numériques suivantes seront retenues : 

**==> picture [192 x 15] intentionally omitted <==**

**Question B3** Montrer que la fonction de transfert complexe du premier filtre peut 1 s'écrire   HF1 ( jω ) = ~~.~~ Exprimer ω0 en fonction de R et C. 1+j ~~[ω]~~ ω0 

- **Question B4** Sur le document réponse DRB2, tracer le diagramme de Bode asymptotique (courbes de gain et de phase) du filtre étudié puis esquisser le tracé réel. 

Le signal v2 (t) est appliqué à l’entrée du filtre et a pour expression : 

v2 (t) =  v21 (t) + v22 (t) = 2 + 0,5 ⋅ sin ( 2 ⋅ π ⋅ 900 ⋅ t) 

- **Question B5** Déterminer à partir du diagramme de Bode les gains G en dB, les modules H et les phases  associés aux pulsations des signaux v21(t) et v22(t). Compléter le tableau du document réponse DRB3. 

- **Question B6** Déterminer l'expression du signal v3(t) en sortie du filtre ainsi qu'une estimation du temps de réponse à 5 % du filtre. Conclure alors sur la capacité du filtre à valider le cahier des charges. 

**Tournez la page S.V.P.** 

Page 7 

## Seconde proposition de filtre 

Afin de répondre pleinement aux exigences du cahier des charges la structure du filtre retenue est constituée de deux filtres mis en cascade comme présenteé sur la figure B4. 

**==> picture [476 x 304] intentionally omitted <==**

**----- Start of picture text -----**<br>
R 10R<br>V2 C I Va & i V3<br>2 VA 10 _3<br>WUT TH<br>Figure B4 — Schéma électrique du second filtre retenu<br>Question B7 Exprimer V3 en fonction de Va, R et C puis montrer que V, peut<br>ee - - \ _ 10-V2(jw)+V3Gw) _<br>s'exprimer sous la forme : Va(jw) = —awoReis ”<br>Question B8_ | A partir des résultats de la question précédente, exprimer la fonction de<br>transfert H->(jw) du second filtre sous la forme :<br>Hea(iw) = 22<br>V2 jw), (jw)?<br>142m ()+(GD)<br>Exprimer la pulsation propre Woy et le paramétre m en fonction de R et C.<br>**----- End of picture text -----**<br>


- Question B9 Proposer des valeurs pour R et C permettant de satisfaire le gabarit du document réponse DRB1. Justifier si la réponse indicielle de ce filtre présente ou non des oscillations. 

Suite a l’application en entrée du filtre du signal vo(t) = v24(t) +V22(t)= 2 + 0,5- sin ( 2-11-900-t), le signal v3(t) en sortie du filtre présente alors l'allure de la figure B5. 

**==> picture [346 x 174] intentionally omitted <==**

**----- Start of picture text -----**<br>
v3(t) . . .<br>2V<br>1V |<br>0,05 0,1 0,15 0,2 0,25 t(s)<br>**----- End of picture text -----**<br>


**==> picture [192 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
Figure B5 — Evolution du signal v(t)<br>**----- End of picture text -----**<br>


- Question B10 | Relever le temps de réponse a 5 % de ce nouveau filtre et conclure sur la capacité de celui-ci a repondre a l'exigence de rapidité du cahier des charges. Proposer si besoin une modification du filtre. 

Page 8 

## **Partie C (à traiter obligatoirement)** 

## **Contrôler les performances du système d'ouverture des portes du bus** 

La chaîne d'énergie permettant l'ouverture et la fermeture des portes du bus est composée d'un hacheur alimentant une machine à courant continu, d'un réducteur et d'un système de transformation de mouvement de type pignon-crémaillère. 

Afin de maîtriser la vitesse d'ouverture et de fermeture des portes, ces constituants sont inclus dans une boucle de rétroaction comprenant un adaptateur de consigne, un comparateur, un correcteur et un capteur de vitesse. Cet ensemble est représenté par la figure C1. 

**==> picture [483 x 105] intentionally omitted <==**

Figure C1 – Schéma-bloc de la boucle d'asservissement de vitesse 

**Objectif :** Identifier les composants du système puis paramétrer un correcteur afin de répondre aux exigences de performances du cahier des charges. 

## **Identification des fonctions de transferts** 

L'équation différentielle régissant le fonctionnement du capteur de vitesse est : 

**==> picture [442 x 34] intentionally omitted <==**

Le réducteur est un engrenage simple dont le pignon d'entrée possède Z1 = 10 dents et le pignon de sortie qui engrène à la crémaillère possède un diamètre primitif d = 0,1 m et Z2 = 50 dents. 

**Question C1** En considérant les conditions de Heaviside satisfaites, déterminer à partir de l'équation différentielle fournie la fonction de transfert H3 ( p ) = Vcapt ( p ) Ω(p) avec Vcapt(p) et Ω(p) les transformées de Laplace respectives de vcapt(t) et ω(t). 

**Question C2** Calculer l'expression littérale puis la valeur numérique du coefficient K1 en mrad[-1] . 

**Question C3** Exprimer le signal ε(p) en fonction de K1, H1 ( p ), H3 ( p ) , V(p) et Vref ( p ) . Sachant que pour assurer un fonctionnement correct du système ce signal doit être nul lorsque V(p) = Vref ( p ) en déduire l'expression de H1 ( p ) . Exprimer finalement H1(p) en fonction de p variable de Laplace et des différentes constantes du système. 

Suite à un essai indiciel effectué sur l'ensemble {moteur + hacheur}, les résultats présentés sur le document réponse DRC1 sont obtenus. 

**Tournez la page S.V.P.** 

Page 9 

## **Question C4** 

- En s'appuyant sur l'essai indiciel du document réponse DRC1, proposer, en le justifiant, un ordre pour la fonction de transfert H2(p). À l’aide de constructions graphiques sur le document réponse DRC1, exprimer H2(p) sous forme canonique en précisant la valeur de ses paramètres caractéristiques. 

## **Étude de la stabilité du système** 

Le cahier des charges impose au système une bonne stabilité et définit ainsi des marges telles que : 

|||
|---|---|
|Marge degain|> 10 dB|
|Marge de phase|>45°|



Le document réponse DRC2 présente le diagramme de Bode de la fonction de transfert en boucle ouverte (FTBO) du système pour un correcteur proportionnel C ( p ) = KC = 1. 

- **Question C5** Sur le document réponse DRC2, tracer la marge de phase du système (considérer que le gain est nul pour ω = 1 rad ⋅ s[-1] ) et donner sa valeur. Donner la marge de gain puis préciser si le cahier des charges est respecté. 

- **Question C6** Toujours en s'appuyant sur le document réponse DRC2, déterminer la valeur du gain du correcteur KClim permettant de se placer à la limite du critère portant sur la marge de phase. 

## **Étude des performances du système** 

Le cahier des charges impose au système les critères ci-dessous : 

|Dépassement|Nul|
|---|---|
|Erreur statique|< 5 %|
|Temps de réponse à 5 %|< 0,2 s|



Quelles que soient les valeurs déterminées précédemment, on considérera désormais : C ( p ) = KC H2 ( p ) = 1+τKmm.p avec Km = 2,88 rad ⋅ s[-1] ⋅ V[-1] et τm = 0,2 s 

**Question C7** Montrer que la fonction de transfert en boucle fermée HBF ( p ) = V ( p ) Vref(p) s'exprime : 

**==> picture [207 x 49] intentionally omitted <==**

**Question C8** Déterminer l'expression de la pulsation propre ω0  et du paramètre d'amortissement m du système en fonction de KC . Sachant qu'un dépassement apparait pour toutes les valeurs du paramètre d'amortissement inférieures à 1, en déduire la valeur maximale de KC permettant de satisfaire le cahier des charges. 

Page 10 

La figure C2 montre l'évolution du temps de réponse à 5 % réduit en fonction du coefficient d'amortissement. 

Figure C2 – Évolution du temps de réponse réduit à 5 % 

- **Question C9** Déterminer, en utilisant la figure C2, la valeur du temps de réponse à 5 % du système dans le cas où KC = 4,5. Conclure alors vis-à-vis du cahier des charges en termes de rapidité. 

- **Question C10** Afin de satisfaire tous les critères du cahier des charges simultanément, trois correcteurs sont finalement envisagés. En vous appuyant sur les relevés présentés sur la figure C3, choisir un correcteur, en justifiant la réponse, parmi les trois proposés. 

**==> picture [421 x 321] intentionally omitted <==**

**----- Start of picture text -----**<br>
Correcteur 1  Correcteur 2<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>oO (0)<br>$0.4 $0.4w<br>S 0.2 — Entrée (m ⋅ s [-1] )  > 0.2 —- Entrée. (m ⋅ s [-1] )<br>0.0 —__1 Sortiei (m ⋅ s [-1] )  0.0 — Sortie (m ⋅ s [-1] )<br>00 0102 03 04 05 06 0.0 0.1 0.2 0.3 04 0.5 0.6<br>Temps(s) Temps(s)<br>Correcteur 3<br>1.0<br>0.8<br>0.6<br>{o)<br>an<br>0.4<br>><br>0.2 — Entrée, (m ⋅ s [-1] )<br>— Sortie (m ⋅ s [-1] )<br>)  )<br>-1 -1<br>(ms ⋅ (ms ⋅<br>)<br>-1<br>(ms ⋅<br>**----- End of picture text -----**<br>


Figure C3 – Propositions de correcteurs 

**Tournez la page S.V.P.** 

Page 11 

## **Partie D (choix 1)** 

## **Vérifier la fiabilité d'une transmission de données** 

La communication entre la pile à combustible et le calculateur du bus Hycity[®] est basée sur une architecture de type bus CAN. Cette communication permet notamment de confier au calculateur la régulation de la température de la pile à partir de la mesure effectuée au préalable. 

## **Structure du bus CAN** 

Le bus CAN (Controller Area Network) est un bus série de terrain car il doit fonctionner dans un environnement limité et sévère (milieu industriel, atelier, voiture…) permettant la transmission asynchrone de données numériques. Il s'agit d'un bus multiplexé. Les particularités de ce bus sont : 

- un bus producteur/consommateur où tous les participants ont les mêmes droits ; 

- les nœuds (hôtes) de ce bus ne sont pas adressés ; seuls les messages transmis possèdent un identificateur ; chaque nœud scrute en permanence le bus et décide selon l’identificateur si le message lui est destiné ou pas ; 

- une fiabilité élevée des mécanismes de protection du protocole. 

Les éléments communiquent par l’intermédiaire du bus CAN composé d’un support de transmission et d’unités de contrôle électroniques (ECU) qui sont les stations du réseau (nœuds CAN). La figure D1 présente l’interconnexion de ces composants. 

Figure D1 – Structure du bus CAN 

**Objectif :** Interpréter les données transmises sur le bus CAN et vérifier leur fiabilité. 

**Question D1** Pour le protocole de communication CAN préciser : 

- le type de transmission : série ou parallèle ; 

- la nature de la transmission : synchrone ou asynchrone ; 

- le mode de transmission : simplex, half-duplex ou full-duplex. 

Page 12 

Dans sa version CAN High Speed, la couche physique comporte deux signaux CAN_L et CAN_H construits de façon symétrique, on parle alors de mode différentiel. Dès lors, c’est la différence de tension UD entre les deux conducteurs du bus qui est prise en compte pour l’interprétation des données (bits) sur le bus : UD = UCANH - UCANL. 

**Question D2** Expliquer comment la couche physique permet l'élimination des perturbations électromagnétiques. 

Deux domaines de tension de UD sont définis pour l’interprétation des données sur le bus : l’état de bus caractérisé par un niveau récessif ou un niveau dominant (on parle de codage NRZ) : 

   - si UD  0,5 V, le bus présente un état récessif (état logique « 1 ») ; 

   - si UD  0,9 V, on assiste à un état dominant (état logique « 0 »). 

- **Question D3** Compléter le document réponse DRD1 en y représentant les évolutions de : 

      - UD sur le premier chronogramme ; 

      - l'état logique correspondant (codage NRZ) sur le deuxième chronogramme. 

La figure D2 présente la structure des trames du bus CAN mis en œuvre dans le système étudié. 

Figure D2 – Trame du bus CAN 

## **Question D4** 

À partir de la structure de la trame CAN, donner : 

- la taille en bits de l'en-tête et du terminateur ; 

- la taille maximale en bits d'une trame CAN ; 

- l'efficacité maximale de la transmission notée Ef et définie comme le rapport du nombre de bits utiles sur le nombre de bits total. 

**Tournez la page S.V.P.** 

Page 13 

## **Interprétation d'une trame** 

Lors de la mise au point du système de communication entre la pile et le calculateur, un test de procédure d’urgence est effectué : la pile envoie un message d’urgence concernant un défaut grave, comme une surchauffe, aux autres équipements. 

Pour valider la procédure, le message doit être envoyé en moins de 1 ms et présenter le bon code d’urgence. 

Dans le cas d’un message d’urgence, 8 octets de données doivent être transmis. 

Le document réponse DRD1 représente les trames échangées lors du test. 

- **Question D5** À partir de la trame présentée sur le document réponse DRD1, déterminer la durée d'un bit ainsi que le débit binaire. En déduire la durée de la trame sachant que celle-ci est constituée de 111 bits. Conclure alors quant à l'exigence sur la durée de transmission. 

Le champ de l’identificateur contient 11 bits. Le constructeur réserve les 4 premiers bits de poids forts aux fonctions et les 7 autres bits pour l’adresse du nœud. 

- **Question D6** Donner le code de la fonction de la trame CAN présentée sur le document réponse DRD1 ainsi que l'adresse du nœud concerné. 

Le constructeur précise également que dans le cas d’un message d’urgence, l’identificateur admet une valeur en hexadécimal comprise entre 81(16) et FF(16). 

- **Question D7** Donner la valeur de l'identificateur transmis en hexadécimal et vérifier qu'il s'agit bien d'un message d'urgence. 

Le principe d’arbitrage consiste, pour les stations émettant simultanément sur le bus, à comparer bit à bit l'identificateur de leur message avec celui des messages concurrents. En cas de conflit (émissions simultanées), l’état « 0 » (dominant) écrase l’état « 1 (récessif). Lors de l'arbitrage bit à bit, dès qu'une station émettrice se trouve en état récessif et détecte un état dominant, elle perd la compétition et arrête d'émettre. 

Le document réponse DRD2 présente un tableau qui contient sur 11 bits les identifiants des messages capturés lors d’échanges sur le bus. 

L’identifiant du message Climatisation en hexadécimal est 110(16) 

- **Question D8** Compléter le tableau du document réponse DRD2 avec les 11 bits correspondant au message "Climatisation" puis entourer en rouge le bit à partir duquel le message "Climatisation" remporte la compétition. Proposer alors un identifiant en hexadécimal pour le message "Pile" qui doit être de niveau de priorité supérieur à ceux déjà présentés sur le document réponse DRD2. 

Page 14 

Les structures du champ de données du message pile est constituée de 4 octets est la suivante : 

|**Désignation du signal**|**Bits**|**Position**|
|---|---|---|
|Température pile en °C|8|1|
|Température gaz en entrée pile en °C|8|2|
|Température eau en sortie pile en °C|8|3|
|Non utilisé (NU)|3|4.2 à 4.0|
|Alerte écart température gaz entrée vs eau sortie|1|4.3|
|Alerte écart température pile vs température gaz|1|4.4|
|Alerte température pile|1|4.5|
|Consigne pompe refroidissement|1|4.6|
|État pompe refroidissement|1|4.7|



L’encodage des données de température est en complément à 2, sur 8 bits. 

Les descriptions des alertes sont les suivantes : 

- alerte température pile : la température de la partie solide de la pile ne doit pas dépasser 85 °C ; 

- alerte écart température pile vs température gaz : l’écart entre la température des gaz en entrée de la pile et celle de la pile doit être inférieure à 10 °C ; 

- alerte écart température gaz entrée vs eau sortie : l’écart entre les températures des gaz en entrée et de l’eau en sortie de la pile doit être inférieur à 6 °C ; 

Le signal CAN_H capturé lors d’un échange de données entre la pile et le calculateur a fourni le chronogramme dont un extrait (champs DLC et Data) a été retranscrit à la figure D3. 

|0|1|0|0||0||1||0|<br>|1||0||1||0||0|0|1|0|1|1|1|1|1||0||1||0||1||1||0|<br>|1||0||1||1||0|1|0|0|0|0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|DLC||||Data||||||||||||||||||||||||||||||||||||||||||||||||NU|||



Figure D3 – Trame de données du message "Pile" capturé sur le bus CAN 

## **Question D9** 

Par lecture de la trame de la figure D3 déterminer : 

- les températures : des gaz en entrée de la pile, de la pile ellemême et de l'eau en sortie de la pile ; 

- la valeur du 4[ème] octet de données en hexadécimal en justifiant l'état des différents bits le composant au vu des températures relevées. 

## **Question D10** 

Pour programmer le calculateur, on souhaite accéder directement à l'état de l'alerte température pile à partir d'une variable Datafield de type long int. Proposer une fonction en pseudo-langage qui renvoie la valeur 1 en cas d'alerte et 0 sinon. 

**Tournez la page S.V.P.** 

Page 15 

## **Partie E (choix 2)** 

## **Évaluer les performances d'un système de redressement de tension** 

Afin d'anticiper une éventuelle défaillance, le bus est équipé d'une batterie de secours qui doit être rechargée périodiquement. Pour cela, le constructeur a choisi d'exploiter l'énergie disponible sur le réseau d'alimentation triphasé. Il faut donc utiliser un dispositif de conversion pour alimenter la batterie en continu. 

**Objectif :** Dimensionner une partie du dispositif de conversion de puissance en respectant les exigences de performance du cahier des charges. 

Le cahier des charges partiel du système de redressement est le suivant : 

|Forme de l'énergie en entrée (primaire)|Sinusoïdale triphasée 230/400 V–50 Hz|
|---|---|
|Forme de l'énergie en sortie|Continue 600 V|
|Facteur de puissance secondaire|> 0,9|



Une première solution est représentée figure E1. Il s'agit de l'association d'un transformateur triphasé (seul le secondaire est représenté) et d'un pont redresseur à diodes de type P3. Pour simplifier l'étude, la charge est supposée fortement inductive et est donc modélisée par une source de courant. 

**==> picture [33 x 61] intentionally omitted <==**

**==> picture [69 x 128] intentionally omitted <==**

**==> picture [67 x 62] intentionally omitted <==**

Figure E1 – Association transformateur triphasé / Pont redresseur P3 

Dans ce montage, les diodes sont à cathodes communes et sont supposées parfaites. Le fonctionnement est alors décrit comme celui d'un commutateur "plus positif", c'est-à-dire que la diode voyant le plus haut potentiel à son anode est à l'état passant, les autres sont bloquées. 

**Question E1** À l'aide de la figure E1 et des indications ci-dessus, compléter les 3 premières lignes du document réponse DRE1 en y indiquant par des 1 les intervalles durant lesquels les diodes conduisent le courant et par des 0 les intervalles durant lesquels elles ne conduisent pas. 

## **Question E2** 

Dans le cas général, établir la relation liant v1, vD1 et uS. Simplifier cette relation dans le cas où la diode D1 est à l'état passant. 

Page 16 

**Question E3** En utilisant les résultats de la question précédente, compléter le document réponse DRE1 en représentant l'allure de la tension uS au cours du temps. 

t L'expression temporelle de la tension v1 est v1 ( t ) = √ 2 Veff. cos ( ω1t ) = √ 2Veff. cos 2π ( T1 ~~)~~ avec ω1 = 100π rad·s[-1] la pulsation, T1 la période et Veff la valeur efficace. 

2π La valeur moyenne notée 𝑥 d'une grandeur périodiquement variable x ( t ) de période T = ω peut se calculer en utilisant la formule suivante : 

**==> picture [276 x 95] intentionally omitted <==**

**Question E4** Donner la période TS de la tension uS en fonction de T1 la période de la tension v1. Montrer alors que la valeur moyenne de la tension uS notée ~~u~~ S s'exprime : 

**==> picture [74 x 31] intentionally omitted <==**

La charge étant fortement inductive, le courant IS est supposé constant. 

**Question E5** Compléter le document réponse DRE1 en représentant l'allure du courant iD1 traversant la diode D1 et le premier enroulement au secondaire du transformateur. 

**Question E6** En utilisant le tracé précédent, déterminer, en fonction de IS, la valeur efficace du courant iD1 notée ID1eff et définie par la relation : 

**==> picture [479 x 110] intentionally omitted <==**

Le transformateur et les diodes étant supposés parfaits, la puissance active est uniquement consommée par la charge. Cette puissance s'exprime alors par : PA = ~~u~~ S ~~.~~ IS. 

**Tournez la page S.V.P.** 

Page 17 

## **Question E8** 

- Rappeler la définition du facteur de puissance fP  au secondaire du transformateur puis calculer sa valeur. Conclure alors vis-à-vis du cahier des charges pour le critère portant sur le facteur de puissance. 

Pour répondre au problème précédent, il est possible de mettre en place une deuxième solution comprenant un pont redresseur parallèle double (PD3) tel que représenté sur la figure E2. 

**==> picture [285 x 108] intentionally omitted <==**

**==> picture [123 x 47] intentionally omitted <==**

Figure E2 – Association transformateur triphasé / Pont redresseur PD3 

2 π Dans ce cas, le facteur de puissance s'exprime fP = √ ~~[q]~~ sin avec q le nombre de π ( q ~~)~~ phases. La tension moyenne aux bornes de la charge est ~~u~~ S = 0,95 UM avec UM l'amplitude des tensions composées au secondaire du transformateur. **Question E9** Vérifier qu'avec ce montage le critère portant sur le facteur de puissance est bien satisfait. 

- **Question E10** En assimilant la tension aux bornes de la charge à sa valeur moyenne, calculer le rapport de transformation m du transformateur couplé en étoile au primaire et au secondaire pour assurer une recharge correcte de la batterie. 

Page 18 

**Modèle CMEN v3 Nom de famille :** _(Suivi, s’il y a lieu, du nom d’usage)_ $$$$$$$$$$$$$$$$$$$$$$$ **Prénom(s) :** $$$$$$$$$$$$$$$$$$$$$$$ **Numéro Né(e) Candidat : le :** $$$$$$$$$$$ $$ $$ $$$$ _Cadre réservé aux candidats de concours de recrutement et examens professionnels_ **Concours :** ................................................ **Option / Section :** .............................................. **N° d’inscription :** $$$ Cocher une seule case parmi les six types de concours suivants : Cocher public OU privé UNIQUEMENT pour les ! externe ! 3[e] externe ! externe spécial ! interne ou 1[er] interne ! 2[nd] interne ! 2[nd] interne spécial concours enseignants : ! public ! privé **Examen professionnel pour l’avancement au grade de :** ....................................................... _Cadre réservé aux candidats d’examens et du concours général_ 

**Examen :** .................................................................... **Série / Spécialité :** .................................................................. **Epreuve - Matière :** ................................................................................ **Session :** .................................................................. 

LDE ENE 1 

## **DRA1 - DRA2 - DRB1 - DRB2 - DRB3 - DRC1** 

## **Tous les documents réponses sont à rendre, même non complétés.** 

C 

**Tournez la page S.V.P.** 

**==> picture [564 x 526] intentionally omitted <==**

**----- Start of picture text -----**<br>
NE RIEN ECRIRE DANS CE CADRE<br>DOCUMENT RÉPONSE DRA1 (Questions A8 et A9)<br>—<br>CU (Nm), CR (Nm)<br>U = 200 V<br>  0,7<br>  0,6<br>  0,5<br>  0,4<br> 0,3<br>  0,2<br>  0,1<br>N (tr·min [-1] )<br>0<br>0  500  1000  1500  2000<br>**----- End of picture text -----**<br>


## **DOCUMENT RÉPONSE DRA2 (Question A10)** 

CU (Nm) Ω (rad·s[ -1] ) 

Page 19 

**DOCUMENT RÉPONSE DRB1 (Questions B2 et B9)** 

**==> picture [427 x 56] intentionally omitted <==**

**----- Start of picture text -----**<br>
G=20log HF ( jω<br>ω2<br>10 ω2 ω (rad ⋅ s [-1] )<br>-3dB<br>**----- End of picture text -----**<br>


**==> picture [509 x 455] intentionally omitted <==**

**----- Start of picture text -----**<br>
DOCUMENT RÉPONSE DRB2 (Question B4)<br>G  (dB)<br>0<br>10    20  100  10 [3 ] 10 [4 ]<br>-5     (r ad ⋅ s [-1] )<br>-10<br>-15<br>-20<br>-25<br>-30<br>farts<br> (degrés)<br>0<br>10    20  100  10 [3 ] 10 [4 ]<br>-15     (rad ⋅ s [-1] )<br>-30<br>-45<br>-60<br>-75<br>-90<br>ae<br>Tournez la page S.V.P.<br> Page 20<br>**----- End of picture text -----**<br>


DOCUMENT REPONSE DRB3 (Question B5) 

## DOCUMENT REPONSE DRC1 (Question C4) 

**==> picture [409 x 292] intentionally omitted <==**

**----- Start of picture text -----**<br>
20 pom ata Too 60<br>50<br>S1<br>~<br>® 15 1 =<1<br>2 40.2<br>oO \ ©<br>E | 30 2<br>910 5<br>oS o<br>S I ®<br>2)ee 3<br>- | 105<br>——- Tension de commande (V)<br>0! - —— Vitesse de rotation (rad-s") 0<br>0 02 04 06 08 1 1.2 1.4<br>Temps (s)<br>**----- End of picture text -----**<br>


Page 21 

**Modèle CMEN v3 Nom de famille :** _(Suivi, s’il y a lieu, du nom d’usage)_ $$$$$$$$$$$$$$$$$$$$$$$ **Prénom(s) :** $$$$$$$$$$$$$$$$$$$$$$$ **Numéro Né(e) Candidat : le :** $$$$$$$$$$$ $$ $$ $$$$ _Cadre réservé aux candidats de concours de recrutement et examens professionnels_ **Concours :** ................................................ **Option / Section :** .............................................. **N° d’inscription :** $$$ Cocher une seule case parmi les six types de concours suivants : Cocher public OU privé UNIQUEMENT pour les ! externe ! 3[e] externe ! externe spécial ! interne ou 1[er] interne ! 2[nd] interne ! 2[nd] interne spécial concours enseignants : ! public ! privé **Examen professionnel pour l’avancement au grade de :** ....................................................... _Cadre réservé aux candidats d’examens et du concours général_ 

**Examen :** .................................................................... **Série / Spécialité :** .................................................................. **Epreuve - Matière :** ................................................................................ **Session :** .................................................................. 

LDE ENE 1 

## **DRC2 - DRD1 - DRD2 - DRE1** 

## **Tous les documents réponses sont à rendre, même non complétés.** 

D 

**Tournez la page S.V.P.** 

## **NE RIEN ECRIRE DANS CE CADRE** 

## **DOCUMENT RÉPONSE DRC2 (Questions C5 et C6)** 

**==> picture [408 x 315] intentionally omitted <==**

**----- Start of picture text -----**<br>
(rad ⋅ s [-1] )<br>(rad ⋅ s [-1] )<br>**----- End of picture text -----**<br>


Page 22 

**DOCUMENT RÉPONSE DRD1 (Questions D3, D5 et D6)** ~~>}~~ 

**==> picture [436 x 256] intentionally omitted <==**

**----- Start of picture text -----**<br>
CAN H<br>4<br>3<br>2<br>1<br>0<br>0    16    32   48         80         112      144         176         208         240<br>Temps (s)<br>2<br>0<br>1<br>0<br>Tension (V)<br> (V)<br>D<br>U<br>Niveaux  logiques<br>**----- End of picture text -----**<br>


## **DOCUMENT RÉPONSE DRD2 (Question D8)** ~~J~~ 

a10 a9 a8 a7 a6 a5 a4 a3 a2 a1 a0 Porte 2 0 0 1 1 0 1 0 0 0 0 0 ~~meEee~~ Porte 1 0 0 1 1 1 1 1 0 0 0 1 Climatisation ~~ee ee~~ 

**Tournez la page S.V.P.** 

Page 23 

**DOCUMENT RÉPONSE DRE1 (Questions E1, E3 et E5)** 

**==> picture [470 x 220] intentionally omitted <==**

**==> picture [88 x 36] intentionally omitted <==**

Page 24 

