## **Éléments de correction de l’épreuve « Étude d'un système, d'un procédé ou d'une – organisation » option ingénierie électrique** 

## **PARTIE A** 

## **Question A1** 

C’est la température de consigne _Tcons_ . 

## **Question A2** 

Variable « mode » qui correspondra à : « _hors gel_ », « _mode standard_ » et « _mode éco_ ». Variable « température de l’eau » : _Teau_ indique la température de l’eau dans le spa. Variable « chauffage » qui est utilisée pour la mise en marche ou l’arrêt du chauffage. 

## **Question A3** 

La température de consigne est réglée à 10°C. 

## **Question A4** : 

Si _filtration_ est vraie 

Alors 

Si _Teau_ est supérieure à la _Tcons_ 

Alors mise à l’arrêt du chauffage Si _Teau_ est inférieure à la Tcons-0,5 Alors mise en marche de chauffage 

Sinon mise à l’arrêt du chauffage 

Autre présentation Si filtration = vraie 

31 

Alors 

Si _Teau_ > _Tcons_ Alors chauffage← arrêt Si _Teau_ < ( _Tcons_ -0,5) Alors chauffage←marche Sinon chauffage← arrêt 

## **Question A5** . 

Tant que mode correspond au « mode eco » Faire Si filtration est vraie 

Alors 

Si _Teau_ > _Tcons_ Alors mise à l’arrêt du chauffage Si _Teau_ < _Tcons_ -0,5 Alors mise en marche du chauffage 

Sinon mise à l’arrêt du chauffage 

Mise à jour de la valeur de mode Fin tant que 

Autre présentation 

Tant que mode = « mode eco » faire Si filtration = vraie 

Alors 

Si _Teau_ > _Tcons_ Alors chauffage← arrêt Si _Teau_ < (Tcons-0,5) Alors chauffage←marche Sinon chauffage←arrêt Mise à jour de la valeur de mode Fin tant que 

## **PARTIE B** 

**Question B1.1** Réchauffeur : 3 kW Pompes d’hydro massage : 2 x 2,25 kW Pompes de circulation : 260 W 

**Question B1.2** 

Voir document réponse n°2. 

**Question B1.3 Réchauffeur** 

En monophasé pour 3 kW (4HP, il faut une base LUB32 Module de contrôle LUCC pour du monophasé _Iréchauffeu_ r = 13,05 A Þ calibre de 4,5 A à 18 A soit LUCC18** Commande 24 V alternatif Þ LUCC18B **Pompes d’hydro massage** En monophasé pour 2,25 kW (3 HP), il faut une base LUB32 Module de contrôle standard LUCC 

32 

_IPompe H_ = 11,37 A Þ calibre de 3 A à 12 A soit LUCC12** Commande 24 V alternatif Þ LUCC12B 

## **Pompe de circulation** 

En monophasé pour 0,26 kW (1/3 HP) Il faut une base LUB12 

Module de contrôle standard LUCC _IPompe C_ = 1,41 A Þ calibre de 1,25 à 5 A soit LUCC05** Commande 24 V alternatif Þ LUCC05B 

## **Question B1.4** 

Voir document réponse n°1 : le réchauffeur et les pompes doivent être raccordés sur les phases 1 et 3 du LUB et non rebouclés avec la phase 2. 

Le propriétaire du SPA a un abonnement de 18 kVA en triphasé avec heures creuses. Ces dernières factures font apparaître des consommations régulières de 16 kW au maximum sans déséquilibre notable. 

## **Question B2.1** 

Lors de l’utilisation des pompes d’hydro massage, la pompe de circulation n’est pas utilisée puisque le réchauffeur est arrêté. 

Cas 1 : pompe de filtration et réchauffeur. Cas 2 : pompes d’hydro massage. Cas 3 : pompe de filtration seule. 

## **En mode « éco »** 

Lors de l’utilisation des pompes d’hydro massage, la pompe de circulation n’est pas utilisée puisque le réchauffeur est arrêté. 

Cas 1 : pompe de filtration et réchauffeur. Cas 2 : pompes d’hydro massage. Cas 3 : pompe de filtration seule. 

Le mode « éco » est ainsi nommé, car pendant les phases de non filtration le réchauffeur n’est pas mis en marche quelle que soit la température. 

## **Question B2.2** 

Bilan de puissance et cas de fonctionnement : voir document réponse °2. 

Le SPA consomme plus de courant et de puissance quand le réchauffeur et la pompe de circulation fonctionnent. 

## **Question B2.3** 

C’est lors du fonctionnement du réchauffeur que la puissance est la plus élevée. La puissance supplémentaire sur la phase 1 est : 

_Pphase_ 1 = _Préchauffeur_ + _Pcirculation_ = 3000 + 260 = 3260 W soit 3,26 kW . Puissance nécessaire en plus sur l’abonnement triphasé : _P_ = 3 ´ _Pphase_ 1 = 3 ´ ,326 = ,978 kW . 

Nouvel abonnement = consommation maximale actuelle + puissance nécessaire en plus sur le triphasé : 

_P_ = 16 + ,978 = 25,78 kW . 

Soit un nouvel abonnement de 30 kVA. 

33 

||Puissance<br>souscrite (kVA)|Abonnement<br>annuel<br>(€ TTC/an)|Prix du kWh<br>(cts € TTC/kWh)|Prix du kWh<br>(cts € TTC/kWh)|
|---|---|---|---|---|
||||HP|HC|
|Ancien abonnement|18|266,84|16,36|11,50|
|Nouvel abonnement|30|761,47|16,36|11,50|



> Le tarif de l’abonnement augmente de : 761,47 - 266,86 = 494,61€ . Le tarif du kWh est le même. 

## **PARTIE C** 

## **Question C1.1** 

La puissance dissipée par une résistance soumise à une tension continue de 230 V est la même que celle d’une résistance soumise à une tension dont la valeur efficace vaut 230 V. 

Il est nécessaire de réaliser le modèle avec une tension continue, car il n’est pas possible de simuler correctement en même temps une fréquence de 50 Hz (tension du réseau) et une fréquence de 1,15*10[-5] Hz (fréquence de la température extérieure de la simulation). 

## **Question C1.2** 

La puissance du réchauffeur est de 3 000 W et la tension d’alimentation est de 230 V 

**==> picture [108 x 24] intentionally omitted <==**

## **Question C2.1** 

D’après le DT1, la masse de l’eau dans le SPA est de 1 620 kg, d’où : 

_C_ = 4 186 ´1 620 = 677 9700 J ×K-1 _spa_ 

## **Question C2.2** 

Les dimensions du SPA sont les suivantes : 2,18×2,18×0,90 soit une surface d’environ 2 _Se_ = ,218´ ,218 = ,475 m entre la couverture et l’eau du SPA. 

Unités en abscisses : seconde. 

34 

## **Question C2.3** 

**==> picture [166 x 24] intentionally omitted <==**

## **Question C3.1** 

Un cycle de filtration a lieu durant les heures pleines soit une énergie de _Efhp_ = ,026´ 4 = ,104 kWh . 

> Un cycle de filtration a lieu durant les heures creuses soit une énergie de _Efhc_ = ,026´ 4 = ,104 kWh . 

## **Question C3.2** 

_Cfh_ = _Efhp_ ´ ,01636+ _Efhc_ ´ ,0115 = 1,04´ 0,1636+1,04´ 0,115 = 0,170144+ 0,1196= 0,289744» 0,29 € 

## **Question C3.3** 

Si l’on considère que la simulation commence à minuit : la période d’heures pleines commence à 7 h 30 soit 7,5 h plus tard soit 27 000 s plus tard. 

La période d’heures pleines commence à l’instant t = 27 000 s. L’énergie à cet instant vaut 1,95 kWh. La période d’heures pleines se termine à 22 h 30 soit 15 h plus tard soit 54 000 s plus tard. La période d’heures pleines se termine à l’instant t = 27 000 + 54 000 = 81 000 s. 

L’énergie à cet instant vaut 5,85 kW·h. 

L’énergie consommée pendant la période d’heures pleines est donc de : 

_Efep_ = 5 _,_ 85 -1 _,_ 95 = 9,3kWh . 

La période d’heures creuses dure 9 h. La pompe fonctionnant en continu : 

_Efec_ = ,026´ 9 = ,234 kWh . 

## **Question C3.4** 

_Cfe_ = _Efep_ × 0 1636 _,_ + _Efec_ × 0 115 _,_ = 3 9 _,_ × 0 1636 _, +_ 2 34 _,_ ×0 115 _, =_ 0 63804 _, +_ 0 2691 _, =_ 0 90714 _,_ » 0 91 _, €_ . 

## **Question C3.5** 

La simulation débute en heures pleines. La période d’heures creuses commence à 22 h 30 soit 8,5 heures plus tard. Soit 30 600 secondes plus tard. Durant cette première période, 1 kWh a été consommé. 

La période d’heures creuses se termine à 7 h 30 soit 9 h plus tard soit 32 400 s plus tard. La nouvelle période d’heures pleines commence à l’instant t = 30 600 + 32 400 = 63 000 s 

· La consommation repart alors de 3 kW h jusqu’au maximum de température suivant qui correspond à 14 h 00 ; 1 kW·h a été consommé. _Erhp_ = 2 kW ×h . 

> La période d’heures creuses a lieu entre les instants 30 600 s et 63 000 s. _Erhc_ = 2kWh . 

**==> picture [53 x 32] intentionally omitted <==**

**----- Start of picture text -----**<br>
Unité en<br>abscisses :<br>seconde.<br>**----- End of picture text -----**<br>


**==> picture [15 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
35<br>**----- End of picture text -----**<br>


## **Question C3.6** 

_Crh_ = _Erhp_ ´ 0 _,_ 1636+ _Erhc_ ´ 0 _,_ 115 = 2´ 0 _,_ 1636 _+_ 2´ 0 _,_ 115 _=_ 0 _,_ 3272 _+_ 0 _,_ 23 _=_ 0 _,_ 5572 » 0 _,_ 56 € 

## **Question C3.7** 

La simulation débute en heures pleines. La période d’heures creuses commence à 22 h 30 soit 8,5 heures plus tard. Soit 30 600 secondes plus tard. Durant cette première période, il n’y a eu aucune consommation. 

La période d’heures creuses se termine à 7 h 30 soit 9 h plus tard soit 32 400 s plus tard. La nouvelle période d’heures pleines commence à l’instant t = 30 600 + 32 400 = 63 000 s 

La consommation repart alors de 2 kW·h. 

Jusqu’au maximum de température suivant qui correspond à 14 h 00, il n’y a eu aucune consommation. _E_ = 0 kWh _rep_ 

La période d’heures creuses a lieu entre les instants 30 600 s et 63 000 s 

_Erec_ = 2kWh . 

## **Question C3.8** 

_Cre_ = _Erep_ ´ 0 _,_ 1636+ _Erec_ ´ 0 _,_ 115 = 0´ 0 _,_ 1636 _+_ 2´ 0 _,_ 115 = ,023 € 

## **Question C3.9** 

Les pompes de massage fonctionnent de 17 h à 17 h 30 soit 0,5 h pendant les heures pleines. Leur puissance électrique consommée vaut 2×2,25 kW soit 4,5 kW. 

_Em_ = 5,4´ 0 _,_ 5 = ,225 kWh On en déduit que : _Cm_ = _Em_ ´0 _,_ 1636 = ,225´0 _,_ 1636 = ,03681» ,037 € . 

## **Question C3.10** 

_CTh_ = _Cfh_ + _Crh_ + _Cm_ = ,0289744+ ,05572+ ,03681» ,1215 € . 

_CTe_ = _Cfe_ + _Cre_ + _Cm_ = ,090714+ ,023 + ,03681» ,1515 € . 

**==> picture [453 x 23] intentionally omitted <==**

## **PARTIE D** 

## **Question D1.1** 

Voir document réponse n°3. 

## **Question D1.2** 

Il est possible de régler les programmes et l’horodateur pour profiter au maximum des heures creuses. 

## **Question D2.1** 

Il est possible de mettre en œuvre des panneaux solaires PV pour alimenter le spa la journée en heures pleines, d’utiliser des panneaux solaires thermiques ou une PAC pour maintenir la température de l’eau dans le SPA. 

## **Question D2.2** 

3000 _Tch_ = 20´ = 10 9,min. 5500 

36 

60 _W jPACété_ = 1500´ = ,055 kWh . 12 60 _W jPAChiver_ = 1500´ = ,109 kWh . 6 

## **Question D2.3** 

Voir document réponse n°3. 

## **Question D2.4** 

> Calcul de l’économie sur la consommation : _Eco_ . _conso_ . = 480,20 - 357,01= 123,19 € . 

> Calcul de l’économie sur l’abonnement : _Eco_ . _abo_ . = 661,91560,18 = 101,73 € . 

Le retour sur investissement est de : 

1800 1800 _RI_ = = = 8 ans 123,19 + 101,73 224,92 

L’investissement n’est pas très rentable financièrement par rapport à la durée de vie d’une PAC, mais il est intéressant du point de vue du développement durable. 

37 

