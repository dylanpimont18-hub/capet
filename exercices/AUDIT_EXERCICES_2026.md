# Audit qualité de la banque d'exercices CAPET SII IE — Session 2026

Audit réalisé le **2026-08-25** sur les **19 notions présentes** dans `exercices/` (`T01_exercices.tex`
à `T19_exercices.tex` — T20 à T30 pas encore générées, hors périmètre). Audit seul : **aucun fichier
source n'a été modifié**.

**Dispositif** (workflow multi-agent en 3 phases) :

1. **Pré-passe scriptée (sans LLM)** — compilation `pdflatex` réelle des 2 variantes de chaque notion
   (38 compilations : énoncés + corrigés, 2 passes chacune) et détections mécaniques : sauts de page
   interdits, décimales à point, nombres ≥ 4 chiffres sans `\,`, unités en `\mathrm`, `\vec`,
   comptages `exoBox`/`\difficulte`/`docTech`/schémas. Résultats transmis aux agents (non re-vérifiés
   par LLM).
2. **Audit fan-out** — un agent d'audit par notion : étanchéité énoncés/corrigés (`\CAPETSHOW`),
   recalcul indépendant de chaque application numérique des corrigés, vérification des sources par
   grep ciblé dans `docs/CAPET_Markdown-*` (sujets et rapports de jury 2013–2026), conformité
   structurelle au skill `exercices-capet`, forme, pédagogie, recouvrement avec les fiches.
3. **Contre-vérification adversariale** — chaque erreur de calcul et chaque problème de source de
   gravité majeure/bloquante a été soumis à un agent vérificateur indépendant chargé de le **réfuter**
   (recalcul from scratch, nouvelle recherche de la source). **32 contre-vérifications rendues :
   30 constats confirmés (15 calculs + 15 sources), 2 réfutés** (listés en §3.3). Seuls les constats
   confirmés figurent dans les listes consolidées.

**Score moyen : 72,1/100** (médiane 71 — min 59 [T14], max 83 [T13, T18])

**Couverture : 19/19 notions auditées** — aucune notion sautée, aucun constat majeur laissé sans
contre-vérification (le budget n'a écarté aucun agent ; une interruption de limite de session en cours
de run a été reprise par resume avec cache, sans relance des audits terminés).

Les **38 compilations passent sans erreur** (2–4 pages par variante). Le seul warning notable est sur
T06 (« missing character(s) in font » : accents littéraux `é` dans des indices en mode mathématique).
190 constats au total : 10 bloquants, 68 majeurs, 112 mineurs.

---

## 1. Classement (du plus faible au plus solide)

| Rang | Code | Notion | Score/100 | Structure/30 | Exactitude/35 | Pédago/15 | Forme/10 | Sources/10 | Exos |
|---|---|---|---|---|---|---|---|---|---|
| 1 | T14 | Variation de vitesse | **59** | 23 | 14 | 7 | 7 | 8 | 6 |
| 2 | T09 | Onduleurs | **62** | 23 | 14 | 10 | 7 | 8 | 5 |
| 2 | T12 | Machine synchrone | **62** | 24 | 13 | 10 | 9 | 6 | 5 |
| 4 | T08 | Redresseurs | **65** | 24 | 13 | 10 | 8 | 10 | 5 |
| 4 | T10 | Mécanique des entraînements | **65** | 25 | 14 | 8 | 8 | 10 | 6 |
| 4 | T15 | Stockage de l'énergie | **65** | 23 | 20 | 10 | 8 | 4 | 6 |
| 7 | T05 | Phénomènes thermiques | **67** | 19 | 26 | 10 | 8 | 4 | 5 |
| 8 | T07 | Hacheurs | **68** | 20 | 24 | 10 | 9 | 5 | 5 |
| 9 | T01 | Grandeurs / électrocinétique | **71** | 26 | 14 | 12 | 10 | 9 | 5 |
| 9 | T02 | Puissances en alternatif | **71** | 21 | 30 | 10 | 8 | 2 | 5 |
| 9 | T06 | Transformateur | **71** | 18 | 33 | 8 | 7 | 5 | 5 |
| 12 | T16 | Énergies renouvelables | **76** | 23 | 30 | 11 | 8 | 4 | 6 |
| 13 | T17 | Distribution / sécurité | **79** | 24 | 33 | 9 | 9 | 4 | 6 |
| 13 | T19 | AOP | **79** | 26 | 24 | 10 | 9 | 10 | 6 |
| 15 | T03 | Représentations complexes / impédances | **81** | 28 | 34 | 8 | 8 | 3 | 5 |
| 15 | T04 | Harmoniques / THD | **81** | 24 | 34 | 10 | 8 | 5 | 5 |
| 15 | T11 | Machine à courant continu | **81** | 24 | 33 | 10 | 8 | 6 | 6 |
| 18 | T13 | Machine asynchrone | **83** | 25 | 30 | 10 | 8 | 10 | 5 |
| 18 | T18 | Composants électroniques | **83** | 24 | 30 | 11 | 8 | 10 | 6 |

---

## 2. Problèmes systémiques transversaux (à corriger « en masse »)

Du plus grave au moins grave. Le premier est exactement le défaut le plus dommageable relevé dans
l'audit des fiches (`fiches/AUDIT_FICHES_2026.md` §2.7) — il a été activement recherché ici et il est
bien présent.

### 2.1 Citations « rapport de jury » fabriquées ou récrites, présentées comme authentiques — 9 notions

**10 constats confirmés en contre-vérification** : des encadrés « Point de vigilance jury » ou des
citations entre guillemets attribuées à un rapport de jury précis sont introuvables dans les
`Rapport_Jury_*.md` correspondants — soit inventés de toutes pièces, soit des synthèses/paraphrases
reformulées présentées comme verbatim, soit du contenu du *sujet* rebadgé « jury ».

Notions touchées : **T02** (×2 : « jury 2021 », « jury 2024 question B3 »), **T03** (ex. 5 — paraphrase
du sujet E2 2024 présentée comme citation des jurys 2024 et 2025, bloquant), **T04** (ex. 2 — citation
2024 assemblée/récrite), **T05** (ex. 5 — « jury 2024, partie capteurs »), **T07** (ex. 3 — « jury 2025
Q27–Q32 » embelli), **T12** (ex. 2 — « jury 2025 » fabriqué), **T15** (ex. 4 — verbatim fabriqué,
bloquant), **T16** (ex. 2 — synthèse présentée comme verbatim, bloquant), **T17** (ex. 4 — citation
« jurys 2021 et 2024 » fabriquée, bloquant).

À l'inverse, plusieurs citations jury sont **authentiques et verbatim** (T01 ex. 4 [2022], T02 ex. 4
[2018], T03 ex. 4 [2018], T14 ex. 6 [2020, mais sortie de son contexte]) : le corpus mélange donc vrai
et faux sans marquage, ce qui est pire qu'une absence de citation. **Correction de masse recommandée** :
supprimer ou dé-guillemeter/dé-attribuer tout encadré jury non retrouvé verbatim.

### 2.2 Données de sujets réels déformées ou inventées sous couvert de référence exacte — 4 notions

5 constats confirmés, distincts du cas précédent car ils touchent les **données d'énoncé** :
**T05** ex. 1 (les efforts 14,9/9,2 kN du sujet 2019 rebaptisés « couples » kN·m, rendant le résultat
incohérent avec le corrigé officiel), **T06** ex. 2 (V = 133 V / I0 = 68 A substitués aux 230 V /
42,5 A du sujet 2026 en gardant son P0 — résultats contredisant ceux des données authentiques),
**T15** ex. 3 (« trajet le plus éloigné ≈ 80 km » inventé dans un exercice sourcé « 2026 question
A5 »), **T17** ex. 2 et ex. 6 (valeurs Ru/Xu et configuration différentielle 300/30 mA attribuées à des
questions de sujets qui ne les contiennent pas). La règle du skill est pourtant explicite : ne jamais
présenter un contenu adapté/inventé comme extrait d'un sujet réel.

### 2.3 Recouvrement massif avec les Questions Types des fiches — 18 notions sur 19

Constat **majeur sur 16 notions** (T02, T04–T17 sauf T03, T19) et mineur sur T03 et T18 ; seule **T01**
est réellement disjointe de sa fiche. Typiquement 2 à 4 exercices par notion reprennent la même source,
les mêmes valeurs et les mêmes questions que les QT de la fiche correspondante (ex. : T05 ex. 1-2 = QT1-QT2
de la fiche ; T12 ex. 1-3 = les 3 QT ; T17 : 4 exercices sur 6). La banque d'exercices, censée être un
**entraînement complémentaire**, fait en grande partie refaire les exemples du cours : c'est le problème
de fond principal pour la valeur pédagogique du corpus. Correction de masse : remplacer les doublons par
d'autres questions des mêmes sujets (ils en contiennent) ou d'autres années.

### 2.4 Erreurs de calcul dans les corrigés — 15 confirmées, 12 notions

Voir la liste consolidée §3.1. Six sont **bloquantes** (résultat final faux, l'utilisateur réviserait
une valeur fausse) : T01 ex. 2 (système de mailles), T08 ex. 5 (taux d'ondulation : définition et
valeurs incompatibles), T09 ex. 4 et T14 ex. 3 (même THD 59 % au lieu de 61,4 % — erreur du rapport
jury 2024 recopiée alors que les fiches T09/T14 avaient déjà été corrigées à 61,4 % lors de l'audit
précédent), T10 ex. 4 (couple par motoréducteur : facteur 2), T12 ex. 5 (avance/retard du rotor
inversés). À noter le motif récurrent : l'erreur naît souvent d'une **incohérence interne** (une ligne
de calcul juste suivie d'un résultat qui ne s'en déduit pas), signe de corrigés partiellement recopiés.

### 2.5 Aucun exercice « lecture de document technique » — 0 encadré `docTech` sur les 19 notions

La pré-passe est formelle : `nb_docTech = 0` partout, alors que le skill l'exige sur les notions qui
s'y prêtent et que le style `docTech` existe dans `preamble.tex`. Constat **majeur sur 14 notions**
(T02, T04–T09, T11–T18) où les sujets sources fournissent des DT exploitables (plaques signalétiques,
datasheets DMH320M6/ATV630, DT spectres…), mineur sur T10 et T19. L'exigence du rapport de jury 2022
(« l'exploitation de documents techniques… est attendu d'un candidat au CAPET ») n'est couverte nulle
part. Correction de masse : ajouter un exercice docTech par notion concernée (ou convertir un exercice
existant dont les données constructeur sont déjà données « inline », cas T11 ex. 2-3, T05 ex. 3).

### 2.6 Schémas électriquement faux — 8 constats majeurs, 7 notions

Plus grave que l'absence de schéma, plusieurs schémas présents sont **faux** :
- diode de roue libre à l'envers (court-circuit de la source à l'amorçage) : **T07** ex. 1 (Buck),
  **T18** ex. 3 ;
- topologies non fermées ou en court-circuit : **T08** ex. 2 (PD6 sans point neutre — aucune maille de
  retour), **T15** ex. 1 et ex. 5 (chaque branche série refermée sur elle-même) ;
- incohérences énoncé/corrigé : **T12** ex. 5 (Fresnel avec E en avance alors que le corrigé calcule un
  retard), **T19** ex. 4 (R1/R2 intervertis par rapport à la formule démontrée), **T08** ex. 4
  (chronogramme du redressement commandé sans le saut de commutation) et ex. 5 (ligne U_S,min tracée à
  0,707·U_max pour une courbe qui touche 0).
S'y ajoutent des schémas obligatoires manquants (T02 ex. 2, mineurs T01 ex. 4, T11 ex. 3, T15 ex. 6).
Une passe de contrôle visuel (rendu PNG) est indispensable avant tout usage — elle n'a été faite par
aucune génération (voir §5).

### 2.7 Gradation des difficultés non conforme ou non progressive — 13 notions

- **Bornes violées** (règle : au moins un niveau 1 ET un niveau 3) : **T05** et **T06** sans aucun
  niveau 3, **T07** sans aucun niveau 1.
- **Progression non monotone** (mineur) : T01, T04, T08, T09, T10, T11, T14, T16, T17, T18, T19 —
  motif récurrent : un exercice de niveau 1 placé en fin de banque après le niveau 3 (l'ordre par
  source prime sur la progression pédagogique).

### 2.8 Références de questions/épreuves imprécises — 12 notions

Nombreux constats mineurs confirmés à la lecture des sujets : numéros de questions décalés (T02 ex. 3 :
B1.2 pour B1.3 ; T04 ex. 2 : B9-B11 pour B10-B12 ; T11 ex. 4 : « questions 7 à 9 » pour Q7-Q8 ; T14
ex. 2), plage annoncée ne couvrant pas le calcul demandé (T01 ex. 4 : Q36 hors « questions 33 à 35 »),
noms d'épreuve inexacts (T17 ex. 2), références non-questions (T07 ex. 4 : « CV1 » est le nom du
convertisseur). Moins grave que §2.1-2.2 (le contenu, lui, correspond), mais la règle du skill impose
la référence exacte lue dans le fichier source.

### 2.9 Corrigés sans phrase de conclusion — 16 notions

La règle du gabarit (chaque corrigé se termine par une conclusion reliant le résultat à une
exigence/un critère) est violée par au moins un exercice dans T01, T02, T03, T05, T06, T07, T08, T10,
T11, T12, T13, T14, T15, T17, T18, T19. C'est le même défaut transversal que celui corrigé dans les
fiches en 2026-08.

### 2.10 Forme : séparateurs de milliers et unités hors siunitx — 15 notions

- Nombres ≥ 4 chiffres sans `\,` dans du contenu mathématique rendu (règle `17\,689`) : quasi toutes
  les notions (hits confirmés de la pré-passe, souvent incohérents au sein d'un même fichier qui
  utilise `\,` ailleurs).
- Unités composées hors siunitx : `\text{VAR}`/`\text{VAD}` (T02, T04), `\mathrm{VAR}`/`\mathrm{V}`/
  `\mathrm{Hz}` (T09), `tr·min⁻¹` à la main (T13, T14), `\SI{...}{...\per jour}` avec unité « jour »
  non déclarée (T16), `$230\,\si{\volt}$` (T18). Les `\mathrm{d}` de différentielles détectés par la
  pré-passe sont en revanche légitimes.
- Divers : accents littéraux en mode math dans T06 (seul warning de compilation du corpus), une dizaine
  de coquilles de français localisées (« une survoltage » T08, « continuement » T07, « apriodique »
  T14, « coulombétrique » T15, « chemin de évacuation » T05…).

**Point positif transversal** : l'étanchéité énoncés/corrigés via `\CAPETSHOW` est quasi parfaite —
un seul constat mineur sur les 19 notions (T16 ex. 2 : l'énoncé révèle le « champ de 782 panneaux »,
réponse de l'ex. 1), aucune fuite de corrigé dans la variante énoncés.

---

## 3. Erreurs de calcul et problèmes de source — listes consolidées

Seuls figurent en 3.1/3.2 les constats **confirmés** par l'agent de contre-vérification
adversariale ; les constats réfutés sont en 3.3 et ne doivent PAS être corrigés.

### 3.1 Erreurs de calcul confirmées en contre-vérification adversariale

| Notion | Ex. | Valeur affichée dans le corrigé | Recalcul indépendant (2 agents concordants) |
|---|---|---|---|
| T01 | 2 q.2 | i2≈88,0 mA ; i1≈91,7 mA ; i3≈+3,7 mA | i1=(10·250+200·6)/35000=105,7 mA ; i2=(300·6+200·10)/35000=108,6 mA ; i3=−2,86 mA |
| T02 | 3 q.3 | 9,978 kW | 3 × 3,26 kW = 9,78 kW (corrigé officiel E2 2017 B2.3 : 9,78 ; puis 16 + 9,78 = 25,78 kW) |
| T05 | 1 q.2 | 9324,4×10³ kN²m²s | 222,01×42 = 9 324,42 kN²m²s (= 9 324,4×10⁶ N²m²s) ; le ×10³ affiché sur la valeur en kN²m²s est faux |
| T05 | 4 q.2-3 | +0,385 V | V+ = 2,5 V ; V− = 5×130,8/230,8 = 2,834 V ; U = V+−V− = −0,334 V exact, −0,385 V linéarisé : signe opposé |
| T07 | 1 q.3 | 1,25 mH (α = 0,5) | α_pire = 0,235 (jury 2023) → L_min = 500×0,235×0,765/(50 000×2) ≈ 0,899 mH ≈ 0,90 mH |
| T08 | 5 q.2 | Delta U=99,8 V ; Umax=257 V ; Umin=157 V | PD2 non filtré : Umax=sqrt(2)x230=325,3 V, Umin=0, Delta U crête-à-crête=325 V, tau_cc=325/207=157 % ; 48,2 % = ondulation RMS/moyenne (autre définition) |
| T09 | 4 q.2 | THD_1 ≈ 0,59 = 59 % | √(95²+27²+27²+20²)/170 = √10883/170 = 104,32/170 = 0,614 = 61,4 % |
| T10 | 4 q.4 | 635 N·m par motoréducteur arrière | T_AR ≈ 1725 N pour les 2 roues arrière → C_total = 1725×0,368 ≈ 635 N·m, soit ≈ 317 N·m par motoréducteur |
| T12 | 5 q.3 | moteur : rotor en avance sur le champ tournant ; générateur : en retard | E = 230 − (105,4 + j170) = 124,6 − j170 → arg(E) = −53,8° : E en RETARD sur V_s en moteur (rotor en retard sur le champ tournant) ; en générateur E en avance |
| T12 | 5 q.2 | E_y < 0 → E en avance sur V_s | E_y < 0 → phase de E négative → E en retard de δ = 53,8° sur V_s |
| T13 | 3 q.2 | Cem = 3pVs²/(R'R·ωs²)·g (donnerait 32,2×0,0667 ≈ 2,15 N·m) | Cem = 3pVs²·g/(R'R·ωs) = 317400×0,0667/9869,6·... ≈ 426 N·m ; la forme en ωs² n'est correcte que sous C_em = A·ω_r |
| T14 | 3 q.2 | 0,59 (59 %) | 95^2+27^2+27^2+20^2 = 10883 ; sqrt = 104,32 ; 104,32/170 = 0,614 = 61,4 % |
| T14 | 3 q.3 | 0,25 ; conforme | 37^2+22^2 = 1853 ; sqrt = 43,05 ; 43,05/170 = 0,2532 = 25,3 % > 25 % |
| T16 | 3 q.3 | rapport cyclique fm = 4,06 ; 6,60 ; 7,08 (>1), « confirment le rôle élévateur » | 195/48=4,06 ; 317/48=6,60 ; 340/48=7,08 : arithmétique exacte, mais fm = fonction de modulation (sujet 2025), pas un rapport cyclique (0≤α≤1) |
| T19 | 4 q.2 | (R2·Vref2 + R1·Vs2)/(R1+R2) | la fraction telle qu'écrite donne (R1·Vref2 + R2·Vs2)/(R1+R2) = (1000×2,42 + 150000×15)/151000 ≈ 14,92 V |

### 3.2 Problèmes de source confirmés (références/citations introuvables ou déformées)

- **T02, ex. 2 q.3** — Encadré « Point de vigilance jury » attribué au « rapport de jury CAPET 2021, sur cette même formule » : aucun passage du Rapport_Jury_2021.md (grep rendement/oubli/sous-estim/dénominateur/courant) ne contient cette recommandation. Attribution jury fabriquée bien que le conseil technique soit correct.
- **T02, ex. 5 q.4** — Encadré « Point de vigilance jury (rapport de jury CAPET 2024, question B3) » : le Rapport_Jury_2024.md contient le corrigé B3 (formule identique) mais aucun commentaire jury sur une « démonstration littérale complète » ni sur le piège Vn/Ur. Commentaire jury inventé et présenté comme authentique.
- **T03, ex. 5** — Citation entre guillemets attribuée aux « rapports de jury CAPET 2024 et 2025 » : introuvable dans Rapport_Jury_2024.md et Rapport_Jury_2025.md. C'est une paraphrase de la définition donnée dans le SUJET E2 2024 (l.383 : « Mφ = Arg(Hbf(0dB)) + 180° »), présentée comme un verbatim de jury — citation fabriquée/déformée.
- **T04, ex. 2** — Citation jury 2024 présentée entre guillemets comme verbatim mais assemblée/récrite : la 1re phrase est le verbatim de B13, la 2e fusionne et reformule B12 (texte réel : « On remarque que la mise en place de la MLI génère des harmoniques dans les hautes fréquences. La solution pour les éliminer est d'introduire un filtre passe bas (circuit R,L par exemple) »).
- **T05, ex. 1** — Données du sujet 2019 (E2, rame de métro, Q25-27) déformées : le sujet donne des EFFORTS Fe1 = 14,9 kN et Fe2 = 9,2 kN, et fait calculer les couples Cm1, Cm2 via le rayon de roue, ρ et η_red (Q25-26) avant Cth (Q27). L'exercice rebaptise ces efforts en couples C_m1 = 14,9 kN·m d'un « moteur de treuil », rendant le C_th = 2,63 kN·m incohérent avec le corrigé officiel (le terme ∑ = 558·10⁶, lui authentique, devient négligeable face aux phases 1-2 relabellisées).
- **T05, ex. 5** — « Point de vigilance jury » attribué au « rapport de jury CAPET 2024, partie capteurs de température » : introuvable dans Rapport_Jury_2024.md. Les valeurs -30 à 700 °C et ±1,5 °C viennent de la Figure 13 du SUJET E2 2024, pas du rapport ; la mention « classe 1 » n'apparaît ni dans le sujet ni dans le rapport (le rapport, partie D, justifie le choix du type J sur d'autres arguments : prix, milieu non humide, tolérance du type T).
- **T06, ex. 2** — Le sujet E2 BAC3 2026 (A12-A13) donne V = 230 V et I0 = 42,5 A ; l'exercice les remplace par 133 V et 68 A tout en conservant P0 = 7,82 kW du sujet. Les résultats (R_f = 6,79 Ω, X_m = 2,05 Ω) contredisent ceux issus des données authentiques (R_f ≈ 20,3 Ω, X_m ≈ 5,6 Ω, calculés dans la fiche T06). « valeurs complétées » est trompeur : les valeurs existent dans le sujet et sont différentes.
- **T07, ex. 3** — « Point de vigilance jury » attribué à « rapport de jury CAPET 2025, correction Q27–Q32 » : la remarque « trop peu de candidats appliquent correctement les lois de Kirchhoff aux deux phases de commutation » et l'« erreur fréquente vL1 = VDC − Eb » sont introuvables dans Rapport_Jury_2025.md. Le rapport ne contient qu'une remarque générale (« De nombreux candidats ne maitrisent pas les lois basiques de l'électricité »), hors section Q27–Q32 : attribution embellie/déformée.
- **T12, ex. 2** — « Point de vigilance jury » attribué au rapport de jury CAPET 2025 introuvable : le Rapport_Jury_2025.md (Q18, l.642-644) donne uniquement le corrigé de la définition servomoteur, sans aucun commentaire sur une « confusion fréquente » entre servomoteur et moteur classique. Commentaire jury fabriqué présenté comme authentique.
- **T15, ex. 4** — Citation jury 2021 présentée comme verbatim (guillemets + attribution « rapport de jury CAPET 2021 ») mais FABRIQUÉE : introuvable dans Rapport_Jury_2021.md. Le rapport contient seulement, en éléments de correction Q10, « n'est pas très performant (rendement de 58%) … plus respectueux de l'environnement que le stockage par batterie » et, en commentaire, « la conclusion finale a été souvent insuffisante ». La phrase guillemetée est une synthèse inventée présentée comme authentique.
- **T15, ex. 3** — Donnée « trajet type le plus éloigné du dépôt ≈ 80 km » introuvable dans E2_Sujet_2026_BAC3 : le sujet parle d'un trajet type de 200 km (l.125) et la question A5 ne fournit aucune distance au dépôt. Valeur inventée insérée dans un exercice sourcé « 2026, question A5 ».
- **T16, ex. 2** — Citation jury 2021 entre guillemets introuvable dans Rapport_Jury_2021.md : le rapport dit seulement « la plupart d'entre eux ont rencontré des difficultés à justifier le choix de l'onduleur » (l.757) et « Le jury déplore... » (l.759). La phrase citée est une synthèse reformulée présentée comme verbatim authentique.
- **T17, ex. 4** — Citation guillemetée attribuée aux rapports de jury 2021 et 2024, introuvable verbatim dans Rapport_Jury_2021.md et Rapport_Jury_2024.md (grep « impératif », « justifier le choix du disjoncteur » : aucun hit correspondant). Le principe est réel (rapport 2021 Q17 : NSX250N MA, Icu, Irm=2860 A, protection thermique par le variateur), mais la phrase citée est fabriquée et présentée comme authentique.
- **T17, ex. 2** — Ru = 0,225 Ω/km et Xu = 0,08 Ω/km présentés comme données du sujet 2024 (B5-B9) : introuvables dans les .md (DT2 en image omise), et la fiche T17_Distribution_Securite.tex traite la même question source avec Ru = 0,0424 mΩ/m et Xu = 0,0902 mΩ/m (ΔU ≈ 31,7 V soit ~7,9 %, vs 22,1 % ici). L'une des deux séries de valeurs déforme le sujet réel ; le résultat 22,1 % ne correspond probablement pas au corrigé officiel.
- **T17, ex. 6** — La configuration 300 mA en tête / 30 mA par départ et la sélectivité différentielle sont attribuées à la question 19 du sujet 2021 : introuvables dans E2_Sujet_2021.md (Q19 réelle = compléter les schémas de puissance et de commande du variateur, DR1/DR2) ni dans Rapport_Jury_2021.md (aucun hit « mA », « différentiel », « sélectivité »). L'attribution repose sur T17_contenu.md, lui-même non sourcé sur ce point.

### 3.3 Constats écartés après contre-vérification

- **T11, ex. 5 q.3** [source] — constat initial : C_th ≈ 557 N·m présenté comme donnée du système réel (« couple thermique équivalent estimé sur le trajet ») : cette valeur est le résultat de la Q27 du sujet 2019, introuvable dans E2_Sujet_2019.md et absente du Rapport_Jury_2019.md (corrigé E2 non p
  **Réfutation** : Valeur RÉFUTÉE comme invérifiable : recalcul from scratch depuis les données publiées de E2_Sujet_2019.md (lignes 411–448) : d_e = 0,86 m (r = 0,43 m), ρ = 0,17, η_red = 97 %, F_e1 = 14,9 kN, F_e2 = 9,2 kN, Δt1 = 42 s, Δt2 = 51 s, T = 2048 s, Σ C_mi²·Δt_i = 558·10⁶ (donnée fournie dans le sujet). C_e1 = 14900×0,43 = 6407 N·m ; C_e2 = 3956 N·m ; C_m = C_e·ρ/η_red → C_m1 ≈ 1122,9 N·m, C_m2 ≈ 693,3 N
- **T15, ex. 3** [calcul] — constat initial : Définition du DoD auto-contradictoire et inversée par rapport au sujet. L'énoncé pose DoD_max = 20 % puis affirme « jamais déchargée en dessous de 20 % de sa charge » (cela correspond à DoD_max = 80 %, pas 20 %). Le sujet réel 2026 dit « elles ne son
  **Réfutation** : Recalcul from scratch depuis l'énoncé du fichier (E=128,4 kW·h, 80 % exploitables, P=22 kW, V=40 km/h) : E_utile = 0,80×128,4 = 102,72 kW·h ; t = 102,72/22 = 4,669 ≈ 4,67 h ; d = 4,669×40 ≈ 186,8 km — identique au corrigé du fichier. La lecture « littérale » de l'auditeur (20 % exploitables) est réfutée par le sujet source lui-même : E2_Sujet_2026_BAC3.md ligne 119 précise pour le scénario exact d

---

## 4. Détail par notion

Constats classés bloquant / majeur / mineur. Les mentions **[CONFIRMÉ]**/**[RÉFUTÉ — écarté]**
renvoient à la contre-vérification adversariale (§3).

### T01 — Grandeurs / électrocinétique (71/100) — `exercices/T01_exercices.tex`

Structure 26/30 · Exactitude 14/35 · Pédagogie 12/15 · Forme 10/10 · Sources 9/10 — 5 exercices

**Sources vérifiées** : ex1: inédit; ex2: inédit; ex3: 2026 E1 partie E Q E4/E6 OK (E1_Sujet_2026.md l.616-644 — « commutateur "plus positif" », cathodes communes, TS/T1, ID1eff conformes; AN Veff=230/IS=15 ajoutée par l'exercice); ex4: 2022 E2 appliquée commune Q33-35 OK (E2_Appliquee_Commune_2022.md l.521-541 — modèle Rf-Lf fig.19, E=207 V confirmés; le calcul de α relève de la Q36) + citation jury AUTHENTIQUE quasi verbatim (Rapport_Jury_2022.md l.813 : « u=(R+L)*i ou u = R*L*i », « Sur les candidats IE, seuls 40% ont répondu correctement »); ex5: inédit

**🟥 Bloquant**
- **Ex. 2 q.2** [calcul] **[CONFIRMÉ]** — Résolution du système fausse : det=35000, i1=3700/35000=105,7 mA, i2=3800/35000=108,6 mA, i3=i1-i2=-2,86 mA (négatif : le courant circule en réalité de la maille 2 vers la maille 1, point physique masqué). Les trois résultats finaux du corrigé sont faux, la substitution écrite juste avant (-200(10+200 i2)/300+250 i2=6) donne pourtant 35000 i2=3800. *(affiché : i2≈88,0 mA ; i1≈91,7 mA ; i3≈+3,7 mA — recalcul : i1=(10·250+200·6)/35000=105,7 mA ; i2=(300·6+200·10)/35000=108,6 mA ; i3=−2,86 mA)*  
  Passage : `i_2 \approx \SI{88,0}{\milli\ampere} ... i_1 \approx \SI{91,7}{\milli\ampere} et i_3 ... \approx \SI{3,7}{\milli\ampere}`

**🟨 Mineur**
- **Ex. 1 q.3** [calcul] — 12×2,35/4,55=6,1978 V : l'arrondi correct à 3 chiffres est 6,20 V, le corrigé tronque à 6,19 V (le facteur 0,516 est lui correct). *(affiché : 6,19 V — recalcul : 28,2/4,55 = 6,198 V → 6,20 V)*  
  Passage : `V_s' = 12 \cdot \dfrac{2{,}35}{2{,}2 + 2{,}35} = 12 \cdot 0{,}516 = \SI{6,19}{\volt}`
- **Ex. 5** [structure] — Gradation non progressive : séquence 1,2,2,3,1 — la banque se termine par un exercice niveau 1 (valeurs moyennes/efficaces d'un créneau) placé après le niveau 3, alors qu'il est conceptuellement préalable aux exercices 3 et 4 qui utilisent ces notions.  
  Passage : `Exercice 5 -- \difficulte{1} \hfill ... exercice in\'edit`
- **Ex. 4** [schema] — Le hacheur en pont en H (4 interrupteurs + 4 diodes) décrit dans l'énoncé et objet de la question 3 n'est pas dessiné ; seul le modèle Rf-Lf du frein est schématisé. Le sujet source (figure 18) fournissait le schéma du pont. Accessoirement, node[left]{$i_f(t)$} étiquette un nœud avec un nom de courant, redondant avec i=$i_f$.  
  Passage : `hacheur en pont en H (4 interrupteurs command\'es, 4 diodes en antiparall\`ele)`
- **Ex. 2, 3, 5** [pedagogie] — Les corrigés des exercices 2, 3 et 5 s'arrêtent sur les valeurs numériques sans phrase de conclusion reliant le résultat à une exigence ou un critère (règle du gabarit ; l'ex. 4 se termine par la note jury, pas par une conclusion du résultat α=0,597). Seul l'ex. 1 conclut correctement.  
  Passage : `\langle u_S \rangle ... \approx \SI{269}{\volt}$ ; $I_{D1,eff} = 15/\sqrt{3} \approx \SI{8,66}{\ampere}$.`
- **Ex. 4 q.3** [source] — Le calcul de α correspond à la Question 36 du sujet 2022 (« En déduire la valeur de α... »), hors plage « questions 33 à 35 » annoncée dans le titre ; les données Rf=5 Ω et <if>=8 A sont introduites par l'exercice (le sujet renvoyait au point nominal de la Q25).  
  Passage : `2022, \'epreuve \'ecrite disciplinaire appliqu\'ee, questions 33 \`a 35`

*Non vérifié par l'agent : Rendu visuel des PDF compilés (audit sur source + résultats de pré-passe uniquement, les 2 variantes compilent sans erreur : 3 p. énoncés / 2 p. corrigés) ; provenance exacte des données Rf=5 Ω et <if>=8 A de l'ex4 (point nominal Q25 du sujet 2022 non retrouvé par grep ciblé — présentées comme données propres de l'exercice, pas comme issues du sujet, donc non fautives)*


### T02 — Puissances en alternatif (71/100) — `exercices/T02_exercices.tex`

Structure 21/30 · Exactitude 30/35 · Pédagogie 10/15 · Forme 8/10 · Sources 2/10 — 5 exercices

**Sources vérifiées** : ex1: inédit; ex2: formule et constantes retrouvées dans E1_Corrige_2014_commun_SII.md (I = Pu/(η·U·√3·cosφ), 0,944/400/0,86 — mais avec Pu_max=151,9 kW → 270,1 A ; les 234,7 A et la question disjoncteur 250 A sont une adaptation), vigilance « rapport jury 2021 » INTROUVABLE dans Rapport_Jury_2021.md; ex3: E2_Corrige_2017.md OK (B1.1 : 3 kW / 2×2,25 kW / 260 W ; B1.3 : 1,41 A ; B2.3 : 3260 W, 3×3,26=9,78, 25,78 kW, 30 kVA — numérotation B1.2 inexacte); ex4: Rapport_Jury_2018.md OK (tableau Q7 : 1930/2720/FP 0,71/cos 0,75 et 1900/1980/0,96/1 ; Q8 : Q1=1702, D=881 et 557 ; citation Q9 quasi verbatim authentique); ex5: E2_Disciplinaire_IE_2024.md OK (extracteur d'air lycée les Lombards Troyes, B1-B4, P=178,3 kW, Q=108,7 kVAR, FP∈[0,92;1], C=Q/(3ωVn²) avec Vn=230 V), vigilance « rapport jury 2024 q.B3 » INTROUVABLE dans Rapport_Jury_2024.md

**🟧 Majeur**
- **Ex. 2 q.3** [source] **[CONFIRMÉ]** — Encadré « Point de vigilance jury » attribué au « rapport de jury CAPET 2021, sur cette même formule » : aucun passage du Rapport_Jury_2021.md (grep rendement/oubli/sous-estim/dénominateur/courant) ne contient cette recommandation. Attribution jury fabriquée bien que le conseil technique soit correct.  
  Passage : `Point de vigilance jury (rapport de jury CAPET 2021, sur cette m\^eme formule)`
- **Ex. 5 q.4** [source] **[CONFIRMÉ]** — Encadré « Point de vigilance jury (rapport de jury CAPET 2024, question B3) » : le Rapport_Jury_2024.md contient le corrigé B3 (formule identique) mais aucun commentaire jury sur une « démonstration littérale complète » ni sur le piège Vn/Ur. Commentaire jury inventé et présenté comme authentique.  
  Passage : `Point de vigilance jury (rapport de jury CAPET 2024, question B3)`
- **Ex. 3 q.3** [calcul] **[CONFIRMÉ]** — Produit intermédiaire faux : 3 × 3,26 = 9,78 kW et non 9,978 (le corrigé officiel 2017 écrit 9,78 ; la suite 16 + 9,78 = 25,78 kW de l'exercice n'est cohérente qu'avec 9,78). La ligne suivante recopie d'ailleurs « 9,978 » dans une somme qui vaudrait alors 25,978. *(affiché : 9,978 kW — recalcul : 3 × 3,26 kW = 9,78 kW (corrigé officiel E2 2017 B2.3 : 9,78 ; puis 16 + 9,78 = 25,78 kW))*  
  Passage : `3 \times 3{,}26 = \SI{9,978}{\kilo\watt}`
- **Ex. toutes** [structure] — Aucun exercice « lecture de document technique » (nb_docTech = 0, aucune question d'extraction) alors que la notion s'y prête : le tableau de mesures LUBIO/COMPACTO (2018) ou la plaque moteur WEG 132 kW (2014) fournissaient un support d'extraction naturel.  
  Passage : `nb_docTech: 0 (pré-passe)`
- **Ex. 5** [pedagogie] — Recouvrement quasi identique avec QT1 + QT2 de la fiche T02_Puissance_AC.tex : mêmes données 2024 (P = 178,3 kW, Q = 108,7 kVAR), mêmes questions (S, FP, Iabs, démonstration C = Q/(3ωVn²), AN). L'unique exercice de niveau 3 n'apporte rien de plus que la fiche de cours.  
  Passage : `title={QT1 - Bilan de puissance...E2 disciplinaire 2024} / P=178,3 kW, Q=108,7 kVAR`
- **Ex. 2** [schema] — Seul exercice sans aucun schéma alors qu'il porte sur un circuit de puissance (départ moteur asynchrone triphasé + disjoncteur) : un unifilaire circuitikz réseau–disjoncteur–moteur est attendu par la règle du skill (schéma obligatoire pour tout exercice de circuit).  
  Passage : `Exercice 2 : aucun environnement circuitikz/tikzpicture`

**🟨 Mineur**
- **Ex. 1 q.3** [calcul] — Radicande intermédiaire faux : 841² + 881² = 707 281 + 776 161 = 1 483 442 et non 1 484 082. Le résultat final √· ≈ 1218 VA reste correct (1218,0). *(affiché : 1 484 082 — recalcul : 841² + 881² = 1 483 442 ; √1 483 442 ≈ 1218,0 VA (résultat final inchangé))*  
  Passage : `\sqrt{841^2+881^2} = \sqrt{1\,484\,082}`
- **Ex. 2** [source] — Adaptation non signalée du corrigé 2014 : le corrigé réel applique la formule avec Pu_max = 151,9 kW → 270,1 A (choix d'un variateur ATV71), pas 132 kW → 234,7 A ; la question du disjoncteur 250 A est inventée (le « d'après » couvre l'adaptation mais la mention « corrigé » suggère que 234,7 A en est issu).  
  Passage : `d'apr\`es 2014, \'Epreuve 1, corrig\'e (motorisation du pont Chaban-Delmas)`
- **Ex. 3** [source] — Numérotation citée inexacte : le calcul des courants (1,41 A...) figure en question B1.3 du corrigé 2017, pas B1.2 (B1.2 = « voir document réponse n°2 »).  
  Passage : `questions B1.2, B2.2 et B2.3 (installation SPA)`
- **Ex. 3** [schema] — Étiquettes du schéma incohérentes avec les notations de l'énoncé : « R+P_C », « P_H » au lieu de P_R + P_PC, P_PH ; toutes les charges (cos φ = 0,86 / 0,8) sont figurées par des résistances pures.  
  Passage : `to[R, l=$R+P_C$] ... to[R, l=$P_H$]`
- **Ex. 1** [pedagogie] — Le corrigé se termine par la simple vérification S² = P² + Q² (coche) sans phrase de conclusion reliant le résultat à une exigence ou un critère, contrairement à la règle du gabarit (les exercices 2 à 5 la respectent).  
  Passage : `\approx \SI{1218}{\volt\ampere} = S$ \checkmark`
- **Ex. 1, 3, 4** [forme] — Séparateur de milliers incohérent en mode mathématique : 1887, 3000, 2250, 3260, 1930, 2720, 1702, 1980, 1900 sans \, alors que 132\,000, 776\,696, 310\,400, 1\,484\,082 en ont un (règle : 17\,689). 60947 (norme) légitime.  
  Passage : `\sqrt{1887} ... \frac{3000}{230} ... \sqrt{2720^2 - 1930^2 - 1702^2}`
- **Ex. 4** [forme] — Unité de puissance déformante hétérogène et hors siunitx : « \text{VAD} » aux q.2-3 puis « \SI{557}{\volt\ampere_d} » en q.4 (unité non déclarée via \DeclareSIUnit, contrairement à \var).  
  Passage : `\approx 881\ \text{VAD} ... $D = \SI{557}{\volt\ampere_d}$`

*Non vérifié par l'agent : Ex4 : le renvoi complémentaire aux « questions 13-14 » du sujet 2018 n'a pas été contrôlé (Q7-9 suffisaient). Ex2 : le nom « pont Chaban-Delmas » n'apparaît pas en clair dans le .md 2014 (OCR dégradé), mais le support (travée levante, contrepoids, moteur WEG 132 kW, Bordeaux) correspond. Ex5 : l'AN officielle B4 du rapport 2024 se lit « 0,016 F » dans le .md, incohérente avec sa propre formule (108,7·10³/(3·2π·50·230²) = 2,18 mF) — artefact OCR probable, le 2,18 mF de l'exercice est cohérent avec la formule officielle. Rendu visuel des 2 PDF non inspecté (compilations OK d'après la pré-passe).*


### T03 — Représentations complexes / impédances (81/100) — `exercices/T03_exercices.tex`

Structure 28/30 · Exactitude 34/35 · Pédagogie 8/15 · Forme 8/10 · Sources 3/10 — 5 exercices

**Sources vérifiées** : ex1: inédit; ex2: 2024 E2 IE partie A/DT1 OK (question A4 et modèle Ir'=Vs/(Rr'/g+jLfωs) retrouvés, E2_Disciplinaire_IE_2024.md l.147, 789-813) mais valeurs DT1 réelles 0,1 Ω / 3,6 mH ≠ 0,8 Ω / 20 mH de l'exercice; ex3: 2024 E2 IE partie D OK (Figure 17 + Cp en série avec enroulement auxiliaire, l.614-622, D15-D17) — la mention « E1_Sujet » est invérifiable (E1_Sujet_2024.md converti est un doublon du contenu E2); ex4: citation jury 2018 VERBATIM (Rapport_Jury_2018.md l.2498) mais Q10-11 en partie B, pas C; ex5: E2 2024 partie C OK (C10-C13 marge de phase, l.383-399), « 31 % partie C 2024 » OK (Rapport_Jury_2024.md l.505), « 7 % 2025 » = partie 3 hacheur (l.482, contexte approximatif), citation guillemetée « la marge de phase n'est pas... » INTROUVABLE dans les rapports 2024/2025.

**🟥 Bloquant**
- **Ex. 5** [source] **[CONFIRMÉ]** — Citation entre guillemets attribuée aux « rapports de jury CAPET 2024 et 2025 » : introuvable dans Rapport_Jury_2024.md et Rapport_Jury_2025.md. C'est une paraphrase de la définition donnée dans le SUJET E2 2024 (l.383 : « Mφ = Arg(Hbf(0dB)) + 180° »), présentée comme un verbatim de jury — citation fabriquée/déformée.  
  Passage : `\guillemotleft\ la marge de phase n'est pas la phase \`a $\SI{0}{\decibel}$, mais $180...$ + cette phase \guillemotright`

**🟧 Majeur**
- **Ex. 5** [pedagogie] — Incohérence physique interne : la BF donnée (H0=50, m=0,25, régime pseudo-périodique avec dépassement) et la BO donnée (Mφ≈78,7°, « bon amortissement ») sont présentées comme le même axe alors que BF ≠ BO/(1+BO) (la BF issue de cette BO aurait un gain statique 1, pas 50, et Mφ=78,7° correspondrait à m≈0,7). Les conclusions des q.2 et q.4 se contredisent pour un même système.  
  Passage : `Sa fonction de transfert en boucle ferm\'ee s'\'ecrit [...] Par ailleurs, la fonction de transfert en boucle ouverte`

**🟨 Mineur**
- **Ex. 4** [source] — La citation jury est authentique et verbatim (Rapport_Jury_2018.md l.2498), mais les questions 10-11 appartiennent à la PARTIE B « validation du nouveau régulateur » (le titre « PARTIE C » commence l.2500, juste après le commentaire). L'attribution « partie C » est fausse (erreur héritée de la fiche T03 QT2). De plus le contexte réel (tension injectée en opposition de phase) est remplacé par un filtre RC sans mention d'adaptation.  
  Passage : `d'apr\`es 2018, rapport de jury, partie C, questions 10-11`
- **Ex. 2** [source] — Le DT1 réel du sujet E2 2024 donne R'R = 0,1 Ω et Lf = 3,6 mH (E2_Disciplinaire_IE_2024.md l.803, 807). Les valeurs de l'exercice (0,8 Ω / 20 mH) sont modifiées sans mention « valeurs adaptées » alors que le titre renvoie explicitement au « document technique DT1 ».  
  Passage : `$L_f = \SI{20}{\milli\henry}$ et $R_r' = \SI{0,8}{\ohm}$`
- **Ex. 5** [source] — Le 7 % est réel (Rapport_Jury_2025.md l.482) mais concerne la « partie 3 » de l'E2 2025 (hacheur/régulation du bus continu, Q39-42), pas spécifiquement une partie « asservissement/marge de phase » comme le suggère le contexte de l'exercice.  
  Passage : `en 2025, seuls $7\,\%$ ont obtenu la moyenne sur cette partie`
- **Ex. 1** [pedagogie] — Le corrigé s'arrête sur le calcul de Q sans phrase de conclusion reliant le résultat à une exigence ou un critère (règle du gabarit). Même défaut pour l'exercice 3 (s'arrête sur I_aux = 5,75 A).  
  Passage : `Q = \frac{L\omega_0}{R} = \frac{0{,}05 \times 447{,}2}{10} \approx 2{,}24`
- **Ex. 2, 4, 5** [pedagogie] — Recouvrement quasi complet avec les 3 Questions Types de la fiche T03 (QT1 = MAS E2 2024, QT2 = expression analytique jury 2018, QT3 = marge de phase E2 2024) : mêmes sources, mêmes questions centrales, mêmes citations jury. Les exercices ajoutent des AN mais n'apportent aucune situation nouvelle par rapport à la fiche.  
  Passage : `titres : mod\`ele monophas\'e MAS / expression analytique / marge de phase`
- **Ex. 4, 5** [forme] — Nombres de 4 chiffres sans séparateur de milliers (4700, 1256,6, 2500) dans du contenu mathématique — règle 17\,689 (hits confirmés par la pré-passe, lignes 172, 175-176, 189, 203).  
  Passage : `2\pi \times 4700 \times 220\times10^{-9} ; \cos(1256{,}6\,t ...) ; \dfrac{(j\omega)^2}{2500}`
- **Ex. 4** [forme] — Unité V composée en \text{V} au lieu de siunitx, et argument du cosinus mélangeant radians (1256,6 t) et degrés (52,4°) dans la même expression — notation formellement incohérente.  
  Passage : `v_s(t) \approx 6{,}10 \cos(1256{,}6\,t - 52{,}4\,\text{\textdegree})\ \text{V}`

*Non vérifié par l'agent : Rendu visuel des PDF (non recompilés, positionnement/lisibilité des schémas circuitikz non inspectés à l'image) ; attribution exacte à l'E1 2024 pour l'ex3 (le fichier Markdown E1_Sujet_2024 du batch est un doublon de conversion du contenu E2, impossible de confirmer ou d'infirmer la présence du moteur monophasé dans le vrai sujet E1).*


### T04 — Harmoniques / THD (81/100) — `exercices/T04_exercices.tex`

Structure 24/30 · Exactitude 34/35 · Pédagogie 10/15 · Forme 8/10 · Sources 5/10 — 5 exercices

**Sources vérifiées** : ex1: inédit (rien à vérifier); ex2: 2024 E2 disciplinaire OK (lycée les Lombards de Troyes, extracteur d'air, MLI fp=6000 Hz, norme IEC/EN 61000-2-2 THD courant<25% — mais questions réelles B10-B12, pas B9-B11; citation jury 2024 = B13 verbatim + B12 récrit; stat 97%/8,5% du Rapport_Jury_2025 exacte mais incise THD non sourcée); ex3: inédit contexte 2024, cohérent avec fp=6000 Hz du sujet; ex4: 2025 E2 disciplinaire OK (CV3-2, Q20-Q23, R0=17,7 Ω, L=10 mH, VDC=230 V, pleine onde F=50 Hz, THDfond=0,48 — tout conforme au sujet réel); ex5: 2018 E2 sujet OK (Dampmart, COMPACTO II vs LUBIO, 46 luminaires SHP SON T PIA Plus 150 W, questions 7-9 = FP/cosφ, Q1, D, S, intérêts — mais 0,84 est un facteur de puissance dans le sujet, pas un cosφ1; P=8 kW et THD=0,18 = valeurs adaptées comme annoncé)

**🟧 Majeur**
- **Ex. 2** [source] **[CONFIRMÉ]** — Citation jury 2024 présentée entre guillemets comme verbatim mais assemblée/récrite : la 1re phrase est le verbatim de B13, la 2e fusionne et reformule B12 (texte réel : « On remarque que la mise en place de la MLI génère des harmoniques dans les hautes fréquences. La solution pour les éliminer est d'introduire un filtre passe bas (circuit R,L par exemple) »).  
  Passage : `\guillemotleft\ la MLI permet de limiter le THD [...] permettant l'utilisation d'un filtre passe-bas \guillemotright`
- **Ex. toutes** [structure] — Aucun exercice « lecture de document technique » (nb_docTech=0) alors que la notion s'y prête : le sujet 2024 fournit un DT3 (spectres), le sujet 2018 des DRS3/DRS4 (grandeurs réseau des régulateurs). L'ex. 2 dit même « Le document technique fournit... » sans encadré docTech ni première question d'extraction.  
  Passage : `Le document technique fournit, pour chaque cas, les valeurs efficaces du fondamental`
- **Ex. 2, 4, 5** [pedagogie] — Recouvrement quasi complet avec la fiche T04 : ex.2 ≈ QT1 (2024 pleine onde vs MLI, mêmes THD ~59 %/~25 % et même conclusion norme), ex.4 ≈ QT3 (2025 CV3-2, même THD 0,48), ex.5 ≈ QT2 (2018 questions 7-9, puissance déformante/FP). Les 3 QT de la fiche sont dupliquées dans 3 des 5 exercices.  
  Passage : `QT1 - THD pleine onde vs MLI 6 kHz [...] QT2 [...] E2 sujet 2018 (questions 7-9) [...] QT3 [...] 2025 (CV3-2)`

**🟨 Mineur**
- **Ex. 2** [source] — Référence de questions décalée : le titre annonce « questions B9 à B11 » mais dans le sujet 2024 le THD correspond à B10-B12 (B9 porte sur la chute de tension et la NFC 15-100).  
  Passage : `2024, \'epreuve \'ecrite disciplinaire [...] questions B9 \`a B11`
- **Ex. 2** [source] — L'incise « le calcul du THD restant mal maîtrisé » est attribuée au rapport de jury 2025 mais introuvable : le rapport donne bien 97 %/8,5 % pour la partie 2, sans commentaire sur le THD (il évoque les formules de base, la chimie, l'algorithmique). La « partie consacrée aux convertisseurs et aux harmoniques » est une glose de « Partie 2 : étude de l'architecture fonctionnelle et structurelle d'un sous-réseau d'électrification ».  
  Passage : `seulement 8{,}5\,\% ont obtenu la moyenne -- le calcul du THD restant mal ma\^itris\'e`
- **Ex. 5** [source] — Le 0,84 est présenté comme « facteur de déplacement [...] cosφ1 (valeur du sujet) » alors que le sujet 2018 le donne comme « facteur de puissance de 0,84 » des ampoules SHP — repurposage de sens (si THD>0, FP < cosφ1). Atténué par la mention « valeurs numériques adaptées » du titre.  
  Passage : `facteur de d\'eplacement [...] vaut $\cos\varphi_1 = 0{,}84$ (valeur du sujet)`
- **Ex. 4 q.4** [pedagogie] — La limite « THD < 25 % » de l'IEC/EN 61000-2-2 (citée par le sujet 2024 pour un THD de COURANT) est appliquée ici au THD de TENSION de v_distri — comparaison normativement incohérente (le sujet 2025 réel, Q23, demandait seulement de commenter la qualité de l'onde).  
  Passage : `comparer \`a l'exigence de la norme IEC/EN 61000-2-2 ($THD < 25\,\%$)`
- **Ex. 5** [structure] — Gradation non monotone : difficultés 1,2,2,3,2 — l'exercice 5 (niveau 2) retombe après le niveau 3 de l'exercice 4. Les niveaux 1 et 3 sont bien présents.  
  Passage : `Exercice 5 -- \difficulte{2}`
- **Ex. 5** [forme] — Nombres >= 4 chiffres sans séparateur \, dans les corrigés (règle 17\,689) : 9524, 5168, 1714, 9677, 8000 (ex.5) et 6000, 8000 hors \SI (ex.2 énoncé, ex.3 corrigé q.2).  
  Passage : `S = \sqrt{8000^2 + 5168^2 + 1714^2} [...] \approx \SI{9677}{\volt\ampere}`
- **Ex. 4, 5** [forme] — Unités hors siunitx : « VAR » et « VAD » composés en \text{...} au lieu de \SI (ex.4 q.3 : 417 VAR ; ex.5 q.1-q.2 : 5168 VAR, 1714 VAD), alors que VA passe par \SI{...}{\volt\ampere} dans les mêmes lignes.  
  Passage : `\approx 417\ \text{VAR} [...] \approx 1714\ \text{VAD}`
- **Ex. 1 q.1** [forme] — Espace manquante dans l'énoncé : « rapport\`a » se rend « rapportà ».  
  Passage : `selon la d\'efinition normalis\'ee IEC (rapport\`a $I_1$)`

*Non vérifié par l'agent : Rendu visuel des PDF (histogrammes TikZ, chronogramme, diagramme des puissances) non inspecté — audit sur source seule, compilation attestée propre par la pré-passe (énoncés 3 p., corrigés 2 p., 0 erreur). Unité \decibel\per decade (ex.3) non testée isolément mais la compilation passe sans warning. Recalculs indépendants tous concordants : ex1 THD=0,2408→24,1 % et Ieff=20,57 A; ex2 √142/20=0,596 et √23,99/20=0,245; ex3 fc=600 Hz, L=7,04 mH, -40 dB/déc; ex4 V1=207,1 V, Lω=3,14 Ω, Z1=17,98 Ω, φ1=10,06°, I1=11,52 A, P=2,35 kW, Q=417 var, THD créneau=0,483≈0,48; ex5 S1=9524 VA, Q1=5168 var (sinφ=0,5426), D=1714, S=9677 VA, FP=0,827 (les deux méthodes concordent).*


### T05 — Phénomènes thermiques (67/100) — `exercices/T05_exercices.tex`

Structure 19/30 · Exactitude 26/35 · Pédagogie 10/15 · Forme 8/10 · Sources 4/10 — 5 exercices

**Sources vérifiées** : ex1: réf 2019 E2 TROUVÉE (E2_Sujet_2019.md l.494 et Q25-27) mais DÉFORMÉE : Fe1=14,9 kN / Fe2=9,2 kN (efforts, rame de métro) relabellisés couples kN·m d'un treuil ; T=2 048 s et ∑=558·10⁶ authentiques. ex2: 2024 E2 Disciplinaire IE « Extracteur d'air » partie E OK (plage -20/200 °C, 4-20 mA, Fig. 14/19). ex3: inédit (Rth TO-220 plausibles). ex4: inédit (α=3,85·10⁻³ standard). ex5: partie D 2024 OK (type J Fe/Constantan, -30 à 700, ±1,5, question D1) mais k_S=51 µV/K ajouté (absent du sujet) et note « rapport de jury 2024 » INTROUVABLE dans Rapport_Jury_2024.md.

**🟧 Majeur**
- **Ex. tous** [structure] — Aucun exercice de niveau 3 : difficultés [2,1,2,2,2], gradation quasi plate (4 exercices identiquement notés 2), pas de sommet de progression exigé par le gabarit.  
  Passage : `Exercice 1 -- \difficulte{2} ... Exercice 5 -- \difficulte{2}`
- **Ex. tous** [structure] — Aucun encadré docTech ni question d'extraction (nb_docTech=0) alors que la notion s'y prête clairement : ex3 injecte des données de datasheet TO-220 (Rth, Tj,max) et le sujet source 2024 fournit une table constructeur des thermocouples (Figure 13) et un DT6 transmetteur KOS 839 — matière idéale pour un exercice de lecture de document technique.  
  Passage : `R_{th,jc} = \SI{2}{\kelvin\per\watt}, ... T_{j,max} = \SI{150}{\celsius}`
- **Ex. 1 q.2** [calcul] **[CONFIRMÉ]** — Chaîne de calcul intermédiaire fausse d'un facteur 1000 : 222,01×42 = 9 324,42 (kN²m²s), pas 9324,4×10³. La ligne suivante (9324,4×10⁶ N²m²s) et le résultat final C_th ≈ 2 633 N·m sont, eux, corrects avec les données de l'énoncé. *(affiché : 9324,4×10³ kN²m²s — recalcul : 222,01×42 = 9 324,42 kN²m²s (= 9 324,4×10⁶ N²m²s) ; le ×10³ affiché sur la valeur en kN²m²s est faux)*  
  Passage : `222{,}01 \times 42 = 9324{,}4\times10^3\ \text{(en } \si{\kilo\newton\squared\meter\squared\second}\text{)}`
- **Ex. 4 q.2-3** [calcul] **[CONFIRMÉ]** — Erreur de signe cohérente énoncé/corrigé : avec le schéma (V+ = milieu des deux R fixes, V− = milieu R/R_T) et U_pont = V+ − V−, on a U = E(R−R_T)/(2(R+R_T)) < 0 pour T > 0. Le corrigé donne +E·ΔR/(4R) et +0,385 V. De plus αT = 0,308 à 80 °C n'est pas ≪ 1 : la valeur exacte est −0,334 V (écart 15 % non signalé). *(affiché : +0,385 V — recalcul : V+ = 2,5 V ; V− = 5×130,8/230,8 = 2,834 V ; U = V+−V− = −0,334 V exact, −0,385 V linéarisé : signe opposé)*  
  Passage : `U_{pont} = V_+ - V_- \approx E\cdot\dfrac{\Delta R}{4R} ... \approx \SI{0,385}{\volt}`
- **Ex. 1** [source] **[CONFIRMÉ]** — Données du sujet 2019 (E2, rame de métro, Q25-27) déformées : le sujet donne des EFFORTS Fe1 = 14,9 kN et Fe2 = 9,2 kN, et fait calculer les couples Cm1, Cm2 via le rayon de roue, ρ et η_red (Q25-26) avant Cth (Q27). L'exercice rebaptise ces efforts en couples C_m1 = 14,9 kN·m d'un « moteur de treuil », rendant le C_th = 2,63 kN·m incohérent avec le corrigé officiel (le terme ∑ = 558·10⁶, lui authentique, devient négligeable face aux phases 1-2 relabellisées).  
  Passage : `C_{m1} = \SI{14,9}{\kilo\newton\meter} pendant $\Delta t_1 = \SI{42}{\second}$`
- **Ex. 5** [source] **[CONFIRMÉ]** — « Point de vigilance jury » attribué au « rapport de jury CAPET 2024, partie capteurs de température » : introuvable dans Rapport_Jury_2024.md. Les valeurs -30 à 700 °C et ±1,5 °C viennent de la Figure 13 du SUJET E2 2024, pas du rapport ; la mention « classe 1 » n'apparaît ni dans le sujet ni dans le rapport (le rapport, partie D, justifie le choix du type J sur d'autres arguments : prix, milieu non humide, tolérance du type T).  
  Passage : `rapport de jury CAPET 2024, partie capteurs de temp\'erature`
- **Ex. 1 et 2** [pedagogie] — Recouvrement quasi identique avec la fiche T05 : ex1 = QT1 de la fiche (mêmes données T=2048 s, 14,9/9,2, 42/51 s, ∑=558×10⁶, même question C_th) ; ex2 = QT2 de la fiche (même plage -20→4 mA / 200→20 mA, même application T = 120 °C). 2 exercices sur 5 n'apportent rien de neuf par rapport au cours.  
  Passage : `fiche QT2 : « Calculer $I_{out}$ pour $T = 120^\circ$C » = ex2 q.2`

**🟨 Mineur**
- **Ex. 1** [forme] — Nombres ≥ 4 chiffres sans séparateur de milliers dans le contenu mathématique : 2048 (le sujet écrit « 2 048 s »), 9324,4, 4316,6, 2633 — règle 17\,689 non appliquée.  
  Passage : `\SI{2048}{\second} ... 9324{,}4\times10^6 ... \SI{2633}{\newton\meter}`
- **Ex. 3 q.2** [forme] — Faute de français dans le corrigé : « chemin de évacuation » au lieu de « chemin d'évacuation ».  
  Passage : `m\^eme chemin de \'evacuation de la chaleur`
- **Ex. 4** [pedagogie] — Le corrigé se termine sur le résultat numérique brut (0,385 V) sans phrase de conclusion reliant le résultat à une exigence/un critère (sensibilité de la chaîne, choix du conditionneur), contrairement à la règle du gabarit. Ex5 conclut, lui, seulement via la note jury (limite).  
  Passage : `= \dfrac{1{,}54}{4} \approx \SI{0,385}{\volt}.`

*Non vérifié par l'agent : Rendu visuel des 2 PDF (non recompilés, conformément à la consigne — compilation OK d'après la pré-passe : rc=0, 3 p. énoncés / 2 p. corrigés, 0 warning) ; question chiffrée exacte de la partie E du sujet 2024 correspondant au calcul de I_out (la partie E « transmetteur » est confirmée mais son détail question par question n'a pas été lu) ; valeur k_S = 51 µV/K du type J (plausible mais non tracée à une source du corpus).*


### T06 — Transformateur (71/100) — `exercices/T06_exercices.tex`

Structure 18/30 · Exactitude 33/35 · Pédagogie 8/15 · Forme 7/10 · Sources 5/10 — 5 exercices

**Sources vérifiées** : ex1: 2026 E1 partie E OK — 600 V DC, P3 cathodes communes, PD3 avec ū_S=0,95·U_M, transfo Yy retrouvés dans E1_Sujet_2026.md (réf « E8 » imprécise : E8 = facteur de puissance) ; ex2: 2026 E2 BAC3 A12-A13 retrouvées dans E2_Sujet_2026_BAC3.md mais données DÉFORMÉES (sujet : V=230 V, I0=42,5 A ; exercice : 133 V, 68 A ; P0=7,82 kW conservé) ; ex3, ex4, ex5: inédits (rien à vérifier ; Ucc 4 % cohérent avec la note de tête du fichier).

**🟧 Majeur**
- **Ex. global** [structure] — Aucun exercice de niveau 3 (difficultés 2,2,2,1,2) et gradation incohérente : le seul niveau 1 arrive en 4e position après trois niveau 2. La règle exige au moins un niveau 1 ET un niveau 3 avec progression plausible.  
  Passage : `Exercice 4 -- \difficulte{1}`
- **Ex. global** [structure] — Aucun exercice « lecture de document technique » (nb_docTech = 0) alors que la notion Transformateur s'y prête typiquement (plaque signalétique, fiche constructeur de transformateur de distribution).  
  Passage : `Banque d'exercices -- 5 exercices`
- **Ex. 2** [source] **[CONFIRMÉ]** — Le sujet E2 BAC3 2026 (A12-A13) donne V = 230 V et I0 = 42,5 A ; l'exercice les remplace par 133 V et 68 A tout en conservant P0 = 7,82 kW du sujet. Les résultats (R_f = 6,79 Ω, X_m = 2,05 Ω) contredisent ceux issus des données authentiques (R_f ≈ 20,3 Ω, X_m ≈ 5,6 Ω, calculés dans la fiche T06). « valeurs complétées » est trompeur : les valeurs existent dans le sujet et sont différentes.  
  Passage : `V_1 = \SI{133}{\volt} ... I_0 = \SI{68}{\ampere}`
- **Ex. 1** [pedagogie] — Recouvrement quasi verbatim avec la fiche T06 : Ex1 reproduit QT1+QT2 (mêmes valeurs 513 V, m=2,23, 631 V, 446 V, m=1,12, mêmes étapes) et Ex2 reprend QT3 (même source A12-A13, même modèle R_f/X_m). 2 exercices sur 5 dupliquent les 3 Questions Types de la fiche sans valeur ajoutée d'entraînement.  
  Passage : `calculer la tension simple secondaire n\'ecessaire $V_{s,simple}$, puis le rapport de transformation $m_1$`

**🟨 Mineur**
- **Ex. 1** [source] — Référence « questions E8 et E10 » imprécise : dans le sujet E1 2026, E8 porte sur le facteur de puissance (non traité par l'exercice) ; les questions correspondantes sont plutôt E4/E9-E10. Les données (600 V, 0,95·U_M, couplage Yy) sont fidèles.  
  Passage : `2026, \'Epreuve 1 (admissibilit\'e), partie E, questions E8 et E10`
- **Ex. 2** [pedagogie] — L'exercice porte sur une machine asynchrone à vide, hors notion T06 Transformateur ; l'analogie de modèle est explicitée mais le sujet reste une MAS (aimait mieux figurer en T07/machines asynchrones).  
  Passage : `essai \`a vide sur une machine asynchrone ($g\approx 0$)`
- **Ex. 4** [pedagogie] — Terme erroné dans la conclusion : fonctionner au rendement max vers 50 % de charge correspond à un SURdimensionnement volontaire du transformateur, pas un « sous-dimensionnement ».  
  Passage : `justifie le sous-dimensionnement volontaire des transformateurs de distribution`
- **Ex. 5** [pedagogie] — Le corrigé s'achève sur la réponse à la question 3 sans phrase de conclusion reliant le résultat à une exigence/un critère (règle du gabarit).  
  Passage : `le facteur $\sqrt{3}$ se simplifie des deux c\^ot\'es).`
- **Ex. 1 q.2** [compilation] — Accent littéral « é » dans des indices en mode mathématique ($U_{s,composée}$, lignes 54/64/65 et 220) : cause le warning « missing character(s) in font » dans les DEUX variantes — le glyphe est absent du PDF rendu. À écrire en \text{...} ou sans accent.  
  Passage : `$U_{s,composée} = \dfrac{U_M}{\sqrt{2}}$`
- **Ex. 2** [forme] — Nombres ≥ 4 chiffres sans séparateur \, dans les calculs des corrigés : 27100, 7820, 53067, 25900 (Ex2) ; 3500, 250000 (Ex3) ; 200000, 204300, 95600, 97200 (Ex4). Règle : 53\,067.  
  Passage : `\dfrac{3\times133^2}{7820} = \dfrac{53067}{7820}`
- **Ex. 2 q.2** [forme] — Unité « kVAR » composée en \text hors siunitx (attendu \SI{25,9}{\kilo\var} ou équivalent).  
  Passage : `\approx 25{,}9\ \text{kVAR}\ (\si{\kilo\volt\ampere} \text{ r\'eactifs})`

*Non vérifié par l'agent : Rendu visuel des PDF non inspecté (audit sans compilation) ; la formule P3 ū_S=(3√6/2π)V du sujet E1 2026 figure dans une image omise par la conversion Marker — vérifiée seulement par cohérence mathématique (valeur standard du P3) et par la fiche T06.*


### T07 — Hacheurs (68/100) — `exercices/T07_exercices.tex`

Structure 20/30 · Exactitude 24/35 · Pédagogie 10/15 · Forme 9/10 · Sources 5/10 — 5 exercices

**Sources vérifiées** : ex1: 2023 E2 disciplinaire appliquée C4-C6 OK (E2_Disciplinaire_IE_2023.md l.315-331 : 500 V, 70-117,5 V, 2 A, 50 kHz, robot Bakus confirmés ; mais corrigé officiel C6 du Rapport_Jury_2023 : α_pire = 0,235, pas 0,5) ; ex2: contexte entrelacement 4 branches confirmé (sujet 2023 C7-C8 + DT3), titre erroné C7 au lieu de C8 ; ex3: Rapport_Jury_2025 Q26-Q32 OK (vL1 = Eb et vL1 = Eb-VDC confirmés l.384-390), mais « point de vigilance jury » spécifique INTROUVABLE (seule remarque générale « lois basiques de l'électricité » p.16 du rapport, hors Q27-Q32) ; ex4: E2_Disciplinaire_IE_2025 Q14-Q19 (CV1, MPPT, Unom = 317 V) + Rapport_Jury_2025 Q19 (fm = 4,06 / 6,6 / 7,08 confirmés chiffre à chiffre), libellé « question CV1 » impropre ; ex5: inédit, rien à vérifier.

**🟧 Majeur**
- **Ex. 1** [schema] — Diode de roue libre Kb inversée dans le circuitikz du Buck : dessinée anode en haut (nœud) / cathode en bas, elle conduirait du nœud vers la masse — E serait court-circuitée quand Ka est fermé et la roue libre serait impossible. Elle doit être orientée de (3,0) vers (3,4).  
  Passage : `(3,4) to[empty diode, l=$K_b$] (3,0)`
- **Ex. 1 q.3** [calcul] **[CONFIRMÉ]** — L'énoncé demande l'inductance minimale « sur toute la plage de α » établie en q.2 ([0,14 ; 0,235]), mais le corrigé dimensionne à α = 0,5, hors plage. Le corrigé officiel du Rapport_Jury_2023 (C6) prend explicitement « ondulation maximale pour α = 0,235 ». Pour la plage donnée : L_min = 500×0,235×0,765/(2×50 000) ≈ 0,90 mH, pas 1,25 mH. *(affiché : 1,25 mH (α = 0,5) — recalcul : α_pire = 0,235 (jury 2023) → L_min = 500×0,235×0,765/(50 000×2) ≈ 0,899 mH ≈ 0,90 mH)*  
  Passage : `L_{min} = \dfrac{500 \times 0{,}25}{2 \times 50\,000} = \SI{1,25}{\milli\henry}`
- **Ex. 3** [source] **[CONFIRMÉ]** — « Point de vigilance jury » attribué à « rapport de jury CAPET 2025, correction Q27–Q32 » : la remarque « trop peu de candidats appliquent correctement les lois de Kirchhoff aux deux phases de commutation » et l'« erreur fréquente vL1 = VDC − Eb » sont introuvables dans Rapport_Jury_2025.md. Le rapport ne contient qu'une remarque générale (« De nombreux candidats ne maitrisent pas les lois basiques de l'électricité »), hors section Q27–Q32 : attribution embellie/déformée.  
  Passage : `Point de vigilance jury (rapport de jury CAPET 2025, correction Q27--Q32) : trop peu de candidats appliquent`
- **Ex. global** [structure] — Aucun exercice de difficulté 1 : la gradation relevée est 2, 2, 3, 2, 3. La règle exige au moins un niveau 1 ET un niveau 3 ; la progression n'est pas non plus monotone (un niveau 2 après un niveau 3).  
  Passage : `difficultes: [2, 2, 3, 2, 3]`
- **Ex. global** [structure] — Aucun exercice « lecture de document technique » (nb_docTech = 0) alors que la notion hacheurs s'y prête clairement : les sujets sources eux-mêmes s'appuient sur des DT (DT2/DT3 en 2023, DT7–DT10 en 2025).  
  Passage : `nb_docTech: 0`
- **Ex. 1, 2, 3** [pedagogie] — Recouvrement quasi identique avec les Questions Types de la fiche T07_Hacheurs.tex : Ex1 = QT1 (mêmes données 500 V / 70–117,5 V / 2 A / 50 kHz, même corrigé α = 0,5 → 1,25 mH), Ex2 = QT entrelacement (même Δi/4 = 0,5 A), Ex3 = QT2 (même dérivation Boost Q27–Q32). 3 exercices sur 5 dupliquent la fiche.  
  Passage : `fiche QT1 : « E2 disciplinaire 2023 (robot Bakus) ... L_min = 1{,}25 mH »`

**🟨 Mineur**
- **Ex. 2** [source] — Titre « question C7 » : dans le sujet 2023, C7 demande d'indiquer les interrupteurs passants sur les chronogrammes ; le contenu de l'exercice (ondulation divisée, conclusion sur l'intérêt) correspond à C8.  
  Passage : `2023, \'epreuve \'ecrite disciplinaire appliqu\'ee, question C7`
- **Ex. 4** [source] — Titre « question CV1 » : CV1 est le nom du convertisseur, pas un numéro de question. Le contenu correspond aux questions Q14–Q19 du sujet E2 2025 (fm calculés dans la correction de Q19 du rapport de jury).  
  Passage : `2025, \'epreuve \'ecrite disciplinaire appliqu\'ee, question CV1`
- **Ex. 1** [pedagogie] — Le corrigé se termine sur la formule de L_min sans phrase de conclusion reliant le résultat à l'exigence d'ondulation (règle du gabarit).  
  Passage : `= \dfrac{125}{100\,000} = \SI{1,25}{\milli\henry} \]`
- **Ex. 3** [pedagogie] — Le corrigé se termine sur α ≈ 0,848 sans phrase de conclusion reliant le résultat à un critère ou une exigence.  
  Passage : `1-\alpha \approx \dfrac{1}{6{,}6} \approx 0{,}1515 \;\Longrightarrow\; \alpha \approx 0{,}848`
- **Ex. 5** [forme] — Orthographe : « continuement » n'existe pas ; écrire « continûment » (ou « continument »).  
  Passage : `qui varie continuement de $-E$`
- **Ex. 5** [schema] — Pont en H dessiné avec 4 interrupteurs idéaux sans diodes antiparallèles : en commande complémentaire avec charge RL, la conduction inverse (roue libre via diodes) est physiquement nécessaire ; simplification tolérable mais schéma incomplet pour un 4 quadrants.  
  Passage : `to[normal open switch, l=$T_1$] (0,2) ... to[normal open switch, l=$T_2$]`

*Non vérifié par l'agent : Valeur numérique officielle de L_min dans le Rapport_Jury_2023 (formules en images omises par la conversion Markdown — seul « α = 0,235 » est textuel) ; présence des valeurs 195 V et 340 V (points P1/P2) dans le DT7 du sujet 2025 (vérifiées uniquement via le rapport de jury) ; rendu visuel des PDF compilés (audit sans recompilation, conformément à la consigne).*


### T08 — Redresseurs (65/100) — `exercices/T08_exercices.tex`

Structure 24/30 · Exactitude 13/35 · Pédagogie 10/15 · Forme 8/10 · Sources 10/10 — 5 exercices

**Sources vérifiées** : ex1: inédit, citation jury 2025 vérifiée VERBATIM (Rapport_Jury_2025.md l.484 : « De nombreux candidats ne maitrisent pas les lois basiques de l'électricité (la loi des nœuds, la loi des mailles, les calculs de puissance ou encore la loi d'Ohm) ») OK ; ex2: 2026 E1 partie E Q.E8-E10 OK (E1_Sujet_2026.md l.593-666 : bus Hycity, batterie de secours, CdC 600 V / fP>0,9, uS=0,95 UM, couplage étoile-étoile — divergence de formule fP avec radical documentée honnêtement en commentaire d'en-tête, OCR l.664) ; ex3: 2024 E2 appliquée commune Q37/Q48/Q49 OK (E2_Appliquee_Commune_2024.md l.498-500 : Pmoy=7,2 kW, U0=72 V, Q48 réversibilités, Q49 risques — Urbanloop) ; ex4: inédit, rien à vérifier ; ex5: inédit ; la référence norme IEC/EN 61000-2-2 « cf. sujet CAPET 2024 Épreuve 1 » vérifiée OK (E1_Sujet_2024.md l.265, l.301)

**🟥 Bloquant**
- **Ex. 5 q.2** [calcul] **[CONFIRMÉ]** — Incohérence définition/valeurs : les taux 48,2/18,3/4,2 % correspondent à la définition ondulation efficace/moyenne (PD2 : sqrt(pi^2/8-1)=48,3 %), pas à la définition crête-à-crête tau=Delta U/<uS> donnée dans l'énoncé. Avec cette définition, un PD2 non filtré donne Umax=sqrt(2)x230=325 V, Umin=0, Delta U=325 V (tau=157 %). Les résultats finaux du corrigé (Delta U=99,8 V, Umax=257 V, Umin=157 V) sont physiquement impossibles pour un PD2 sans filtrage. *(affiché : Delta U=99,8 V ; Umax=257 V ; Umin=157 V — recalcul : PD2 non filtré : Umax=sqrt(2)x230=325,3 V, Umin=0, Delta U crête-à-crête=325 V, tau_cc=325/207=157 % ; 48,2 % = ondulation RMS/moyenne (autre définition))*  
  Passage : `$\Delta U = \tau_{PD2}\times\langle u_S \rangle = 0{,}482\times 207 \approx \SI{99,8}{\volt}$`

**🟧 Majeur**
- **Ex. 4** [schema] — Chronogramme faux : le second segment trace -1.8*sin(x-180), soit +1.8*sin(x) — la courbe dessinée est une sinusoïde continue de alpha à 2pi+alpha, sans le saut de commutation en pi+alpha ni le motif répété positif-dominant du pont tout thyristor. Sur [pi+alpha, 2pi+alpha] on doit avoir uS=-sqrt(2)V sin(theta) (segment opposé à celui tracé).  
  Passage : `\draw[thick,domain=205:385,samples=60,smooth] plot ({...}, {-1.8*sin(\x-180)});`
- **Ex. 2** [schema] — Schéma PD6 électriquement non fermé : les trois sources v1, v2, v3 ont leur borne gauche flottante (aucun point neutre commun, aucun couplage étoile) — aucune maille de retour de courant n'existe. De plus la charge est dessinée en R alors que l'énoncé la décrit comme fortement inductive assimilée à une source de courant IS.  
  Passage : `\draw (0,9) to[sV, l=$v_1$] (2.5,9); ... \node[left] at (0,9) {phase 1};`
- **Ex. 5** [schema] — Figure incohérente : la ligne pointillée U_S,min est tracée à 0,707xUmax (y=1.41 pour un pic à 2) alors que la courbe PD2 dessinée touche 0 en theta=180° — et que le minimum réel d'un PD2 non filtré est 0. La figure accrédite visuellement l'erreur de définition du taux d'ondulation du corrigé.  
  Passage : `\draw[dashed,gray] (0,1.41) -- (8,1.41); \node[left] at (0,1.41) {$U_{S,min}$};`
- **Ex. toutes** [structure] — Aucun exercice de lecture de document technique (nb_docTech=0, confirmé par la pré-passe) alors que la notion Redresseurs s'y prête (documentation constructeur de pont, datasheet diodes, DT de sujet réel type DT4 Urbanloop). Pas de première question d'extraction de données.  
  Passage : `nb_docTech: 0 (pré-passe T08.json)`
- **Ex. 2** [pedagogie] — Recouvrement quasi intégral avec la fiche T08 : les 3 questions reproduisent QT1 (fP P3 0,827 vs PD6 0,955, même conclusion cahier des charges) et QT2 (rapport de transformation pour 600 V DC, E1 2026 Q.E10) — mêmes valeurs, mêmes calculs, même source. L'exercice n'apporte presque rien de plus que la fiche.  
  Passage : `fiche l.167 QT1 - Facteur de puissance P3 vs PD6 ; l.198 QT2 - PD6 à 600 V DC - rapport de transformation`

**🟨 Mineur**
- **Ex. 3 q.1** [forme] — Nombre de 4 chiffres sans séparateur de milliers dans du contenu mathématique : 7200 au lieu de 7\,200.  
  Passage : `\dfrac{7200}{72} = \SI{100}{\ampere}`
- **Ex. 3 q.3** [forme] — Faute de genre : « une survoltage » (masculin : un survoltage, ou mieux : une surtension).  
  Passage : `provoquant une survoltage dangereux pour les composants`
- **Ex. 2 q.3** [pedagogie] — Le corrigé s'arrête sur m=1,12 sans phrase de conclusion reliant le résultat à une exigence du cahier des charges (règle du gabarit).  
  Passage : `m = \frac{U_{2,comp}}{U_{1,comp}} = \frac{446}{400} \approx 1{,}12`
- **Ex. toutes** [structure] — Gradation 1-3-2-3-2 : le niveau 3 arrive dès l'exercice 2 puis la difficulté redescend ; les niveaux 1 et 3 sont présents mais la progression n'est pas croissante.  
  Passage : `difficultes: [1, 3, 2, 3, 2] (pré-passe)`

*Non vérifié par l'agent : Rendu visuel des PDF compilés (audit sur source seul, compilations OK 3+3 pages selon pré-passe) ; valeur tau_P3=18,3 % et tau_PD6=4,2 % recalculées uniquement en définition RMS (confirmées exactes dans cette définition-là) ; contenu exact de la figure E2 du sujet 2026 (image non textuelle dans le Markdown)*


### T09 — Onduleurs (62/100) — `exercices/T09_exercices.tex`

Structure 23/30 · Exactitude 14/35 · Pédagogie 10/15 · Forme 7/10 · Sources 8/10 — 5 exercices

**Sources vérifiées** : ex1: inédit; ex2: 2025 E2 disciplinaire Q21-Q23 OK (E2_Disciplinaire_IE_2025.md l.268-278 — VDC=230 V, R0=17,7 Ω, L=10 mH, Sdistri=3 kVA, THD=0,48 tous conformes); ex3: 2024 E2 appliquée commune Q45-46 OK (l.562-570 — 28 pôles, ωm=2πf/p, 60 km/h, 72 V composée et par enroulement, Rroue=20 cm l.345 ; f0=185,6 Hz conforme Rapport_Jury_2024 l.885) ; ex4: 2024 E2 disciplinaire B10-B13 OK (l.265-307 — norme IEC/EN 61000-2-2 25 %, fp=6000 Hz ; THD 0,59/0,25 = valeurs verbatim du Rapport_Jury_2024 l.229-233, mais le 0,59 officiel est lui-même arithmétiquement faux ; citation jury « abordée par 88 %... 42 % » vérifiée verbatim l.503) ; ex5: 2025 Q14 OK (l.232), table CV1/CV2/CV3 verbatim Rapport_Jury_2025 l.302-311 ; le « groupe électrogène » du synoptique non retrouvé dans la section Q14 du sujet (architecture annoncée : PV + batterie + pile à combustible)

**🟥 Bloquant**
- **Ex. 4 q.2** [calcul] **[CONFIRMÉ]** — Chaîne arithmétique incohérente : 104,3/170 = 0,614, pas 0,59. Le 0,59 recopie l'erreur du rapport jury 2024 (Rapport_Jury_2024.md l.229), mais la fiche projet T09_Onduleurs.tex (QT1, l.215) a déjà corrigé en 0,61 = 61 %. Le corrigé affiche donc un résultat final faux et contradictoire avec ses propres nombres intermédiaires. La conclusion q.3 (non-conformité) reste vraie dans les deux cas. *(affiché : THD_1 ≈ 0,59 = 59 % — recalcul : √(95²+27²+27²+20²)/170 = √10883/170 = 104,32/170 = 0,614 = 61,4 %)*  
  Passage : `\frac{\sqrt{10883}}{170} \approx \frac{104{,}3}{170} \approx 0{,}59 = 59\ \%`

**🟧 Majeur**
- **Ex. toutes** [structure] — Aucun exercice « lecture de document technique » avec encadré docTech ni question d'extraction, alors que la notion Onduleurs (variateurs de vitesse, onduleurs PV, chaînes de conversion) s'y prête pleinement — les sujets sources eux-mêmes s'appuient sur des DT (DT3 2024, DT6/DT8/DT9 2025).  
  Passage : `nb_docTech = 0 (pré-passe)`
- **Ex. 3, 4, 5** [pedagogie] — Recouvrement quasi identique avec les 3 Questions Types de la fiche T09_Onduleurs.tex : ex4 = QT1 (mêmes valeurs 170/95/27/27/20 et 37/22, même norme), ex5 = QT2 (même Mafate CV1-CV3), ex3 = QT3 (même Urbanloop 185,6 Hz). 3 exercices sur 5 dupliquent la fiche au lieu d'offrir un entraînement nouveau.  
  Passage : `QT1 - THD pleine onde vs MLI / QT2 - Identification des convertisseurs / QT3 - MSAP Urbanloop`

**🟨 Mineur**
- **Ex. 5** [source] — L'architecture du sujet 2025 autour de Q14 (E2_Disciplinaire_IE_2025.md l.230) est « PV + batterie lithium + pile à combustible/électrolyseur » ; le « groupe électrogène de secours » comme source AC de CV2 n'est pas retrouvé dans cette section (DT6 = image non convertie, invérifiable). La table réponse CV1/CV2/CV3 est en revanche reprise verbatim du Rapport_Jury_2025 (l.302-311).  
  Passage : `une batterie lithium et un groupe \'electrog\`ene de secours pour alimenter le r\'eseau local`
- **Ex. 2 q.2** [calcul] — Deux incohérences d'arrondi affichées : 3,1416×170,0 = 534,1 (le 534,5 exige I²=170,13) ; et √(3011²+534,5²) = 3058 VA, pas 3055 VA. Résultats finaux (534,5 VAR, conformes au corrigé officiel) corrects par ailleurs. *(affiché : 3,1416 × 170,0 ≈ 534,5 VAR ; S ≈ 3055 VA — recalcul : 3,1416×170,0 = 534,07 ; avec 13,043²=170,13 → 534,5 VAR ; √(3011²+534,5²) = 3058 VA)*  
  Passage : `\approx 3{,}1416 \times 170{,}0 \approx \num{534,5}\ \mathrm{VAR} ... \approx 3055\ \mathrm{VA}`
- **Ex. 2, 5** [forme] — Unités composées en \mathrm au lieu de siunitx (règle projet) : \mathrm{VAR}/\mathrm{VA}/\mathrm{kVA} (l.161-162), \mathrm{V}/\mathrm{Hz} (l.282, 292, 311, 324). Les \mathrm{THD} sont légitimes (opérateur).  
  Passage : `\num{534,5}\ \mathrm{VAR} ; 3055\ \mathrm{VA} ; $230\ \mathrm{V} / 50\ \mathrm{Hz}$`
- **Ex. 2, 4** [forme] — Nombres ≥ 4 chiffres sans séparateur \, en contenu mathématique (3000, 3011, 3055, 6000, 9025, 10883, 1369, 1853) — règle 17\,689. Le 61000 (norme) et 1416 (décimales de pi) sont légitimes. La fiche T09 écrit correctement 9\,025, 10\,883.  
  Passage : `\dfrac{3000}{230} ; \sqrt{9025+729+729+400} ; \sqrt{10883} ; \sqrt{1369+484} ; \sqrt{1853} ; 6000/50`
- **Ex. 2 q.2** [forme] — Faute de grammaire dans l'énoncé : « traversé » au lieu de « traversant ».  
  Passage : `le courant efficace global travers\'e la r\'esistance et l'inductance`
- **Ex. 5** [structure] — Gradation non monotone : l'exercice 5 (niveau 1, pure identification) est placé en dernier, après le niveau 3. Niveaux 1 et 3 bien présents par ailleurs.  
  Passage : `difficultes = [1, 2, 2, 3, 1]`

*Non vérifié par l'agent : DT3 2024 (spectre 170/95/27/27/20 A et 37/22 A : document = image non convertie ; valeurs cohérentes avec le calcul du rapport jury) ; DT6 2025 (synoptique en image omise : impossible de confirmer/infirmer la présence d'un groupe électrogène comme source de CV2) ; rendu visuel des PDF compilés (audit sans compilation, conformément aux consignes)*


### T10 — Mécanique des entraînements (65/100) — `exercices/T10_exercices.tex`

Structure 25/30 · Exactitude 14/35 · Pédagogie 8/15 · Forme 8/10 · Sources 10/10 — 6 exercices

**Sources vérifiées** : ex1: 2014 E1 Corrigé Q16 OK (E1_Corrige_2014_commun_SII.md : Dt=1,7 m, Nm=980 tr/min, Vmax=0,074, Rtot=1178,8, R2=58,94 — valeurs identiques); ex2: inédit (rien à vérifier, données déclarées inventées en commentaire d'en-tête); ex3: 2019 E2 Q25-26 OK (E2_Sujet_2019.md : de=0,86 m, ρ=0,17, ηred=97 %, Fe1=14,9 kN, Fe2=9,2 kN, libellés Q25/Q26 conformes); ex4: 2023 E2 disciplinaire IE Q A1-A4 OK (E2_Disciplinaire_IE_2023.md : M=2500 kg, pente 35 %, aX=0,1, F_outils=2000 N, R=368 mm ; nuance : Q A4 officielle demande le couple des DEUX motoréducteurs, l'exercice dit \"chacun\" — cf. constat bloquant ; la relation 5× est illisible dans la conversion Markdown); ex5: 2025 E2 appliquée commune Q6/8/9 OK (E2_Appliquee_Commune_2025.md : m=181 kg, 3000×2400×60 mm, Jmot=0,003, r=0,00607 ; adaptation d_OG=1,50 m déclarée dans le titre et l'en-tête — l'officiel donne Jeq=0,0118, cohérent avec d_OG≈0,30 m, l'exercice assume sa valeur de substitution); ex6: 2024 E2 appliquée commune Q16-17 OK (E2_Appliquee_Commune_2024.md : MC=1 t, Rroue=20 cm, freins 150/60 N·m, aC=-1,4 m·s⁻² ; citation jury retrouvée VERBATIM EXACTE dans Rapport_Jury_2024.md, Partie 2)

**🟥 Bloquant**
- **Ex. 4 q.4** [calcul] **[CONFIRMÉ]** — L'énoncé définit T_AR comme la composante tangentielle des forces du sol sur LES roues arrière (résultante, cf. PFD q.2 : M·aX = T_AV + T_AR − Mg·sinθ − F_outils) et demande le couple de CHACUN des deux motoréducteurs arrière. Le corrigé attribue pourtant la totalité de T_AR à chaque roue : le couple par motoréducteur devrait être (T_AR/2)·R ≈ 317 N·m (635 N·m étant le total des deux). Résultat final faux d'un facteur 2 ; le sujet officiel 2023 (Q A4) demandait d'ailleurs le couple des deux motoréducteurs ensemble, la reformulation en "chacun" sans division par 2 déforme la réponse. *(affiché : 635 N·m par motoréducteur arrière — recalcul : T_AR ≈ 1725 N pour les 2 roues arrière → C_total = 1725×0,368 ≈ 635 N·m, soit ≈ 317 N·m par motoréducteur)*  
  Passage : `C_{roue} = \|\vec T_{AR}\| \times R = 1725 \times 0{,}368 \approx \SI{635}{\newton\meter}`

**🟧 Majeur**
- **Ex. 3, 5, 6** [pedagogie] — Recouvrement quasi identique avec la moitié de la banque : la fiche fiches/T10_Mecanique.tex contient déjà QT1 (métro 2019, mêmes données ρ=0,17, η=97 %, d_e=0,86 m, 14,9/9,2 kN = Exercice 3), QT2 (KUKA 2025, inertie équivalente = Exercice 5) et QT3 (Urbanloop 2024, freinage Q17 = Exercice 6). 3 exercices sur 6 refont les Questions Types de la fiche au lieu d'apporter des situations d'entraînement nouvelles.  
  Passage : `fiche T10 : "QT1... ρ = 0{,}17, η_red = 97 %... F_{e1} = 14,9 kN" / "QT2 - ... KUKA... 2025 (Q9-11)" / "QT3 - Freinage Urbanloop"`

**🟨 Mineur**
- **Ex. 2 q.2** [pedagogie] — Commentaire de corrigé factuellement faux : avec J_eq = 0,004 + 0,00512 = 0,00912 kg·m², la charge contribue à 56 % de J_eq, soit la contribution MAJORITAIRE. Le r² atténue bien J_charge (÷625) mais l'affirmation "contribue très peu à J_eq" est contredite par les propres chiffres du corrigé. *(affiché : J_charge contribue très peu à J_eq — recalcul : 0,00512/0,00912 = 56 % de J_eq : contribution majoritaire (l'atténuation ÷625 est vraie, pas la conclusion))*  
  Passage : `$J_{charge}$ contribue tr\`es peu \`a $J_{eq}$ car le facteur $r^2 = 1{,}6\times10^{-3}$ att\'enue`
- **Ex. 2** [pedagogie] — Le corrigé se termine sur la valeur C_m ≈ 1,89 N·m sans phrase de conclusion reliant le résultat à une exigence ou un critère (règle du gabarit) ; les 5 autres exercices en ont une.  
  Passage : `C_m = \dfrac{45 \times 0{,}04}{0{,}95} \approx \SI{1,89}{\newton\meter} \] \end{enumerate}`
- **Ex. 6** [structure] — Gradation non monotone : difficultés 1,2,2,3,3 puis retour à 1 en dernier exercice. Les deux niveaux extrêmes sont présents (OK) mais l'exercice de niveau 1 placé après deux niveaux 3 casse la progression attendue.  
  Passage : `Exercice 6 -- \difficulte{1} ... 2024 ... Urbanloop`
- **Ex. toutes** [structure] — Aucun exercice "lecture de document technique" (nb_docTech = 0). La notion est majoritairement analytique (calculs de statique/dynamique), mais le thème entraînements s'y prêtait partiellement (courbes couple/vitesse de motoréducteurs de la figure 4 du sujet Bakus 2023, DT2 freins Urbanloop 2024) — extraction possible mais non exigible strictement, d'où mineur.  
  Passage : `nb_docTech: 0 (pré-passe)`
- **Ex. 1, 3, 4, 6** [forme] — Nombres >= 4 chiffres en mode mathématique hors \SI sans séparateur \, : 1178,8 (ex1), 14900/6407/9200/3956 (ex3), 2500/10351/1725 (ex4), 1500/2100/1000 (ex6). Règle du projet : 17\,689. Les occurrences dans \SI{...} sont acceptables (siunitx), les autres non.  
  Passage : `C_{e1} = 14900 \times 0{,}43 = \SI{6407}{\newton\meter} \qquad C_{e2} = 9200 \times 0{,}43`

*Non vérifié par l'agent : Rendu visuel des PDF compilés (les 2 schémas TikZ n'ont pas été inspectés en image, seule leur cohérence lue dans le code : topologie du train d'engrenages ex2 et du plan incliné ex4 conformes aux énoncés) ; sens exact de la relation officielle 2023 entre T_AV et T_AR (ligne corrompue par la conversion Markdown : « ‖ | =5x| ⃗⃗⃗ ‖V »), la version de l'exercice (T_AV = 5·T_AR) est plausible mais non confirmable*


### T11 — Machine à courant continu (81/100) — `exercices/T11_exercices.tex`

Structure 24/30 · Exactitude 33/35 · Pédagogie 10/15 · Forme 8/10 · Sources 6/10 — 6 exercices

**Sources vérifiées** : ex1: inédit (données pédagogiques, cohérentes) ; ex2: 2026 E1 partie A Q A1-A3 OK (E1_Sujet_2026.md l.129-193 : actionneur portes bus, Un=200V, In=0,5A, Nn=1800 tr/min, essai rotor bloqué 3,3V, R=6,6Ω, τ→L≈100mH, figure A2 avec repères 5/15/30 ms fidèle) ; ex3: 2026 E1 Q A4-A6 OK (l.195-221 : essai à vide 200V/0,05A, Ke=1,044, Cp=0,052 Nm, liste PA/PJR/PEM/PFM/PU/η identique — nuance : le sujet nomme PFM « pertes fer », l'exercice « pertes mécaniques et fer ») ; ex4: 2019 E2 Q7-Q8 OK (E2_Sujet_2019.md l.210-246 : I=380A, 4 moteurs série, rhéostats, 750V l.63, k2=0,1 l.262) mais Q9 (énergie ERh) non couverte malgré le titre « 7 à 9 » ; ex5: 2019 E2 Q28 OK (l.513-525 : table Alsthom 360V/305A/96kW/1035 tr/min conforme), MAIS Cth=557 N·m INTROUVABLE (résultat Q27 non publié dans le rapport jury local) ; ex6: inédit (décalque non signalé de la Q A10 du sujet 2026) ; citation jury 2024 de l'ex3 vérifiée mot pour mot (Rapport_Jury_2024.md l.511) et honnêtement présentée comme issue d'un « sujet différent ».

**🟧 Majeur**
- **Ex. global** [structure] — Aucun exercice « lecture de document technique » (nb_docTech=0) alors que la notion MCC s'y prête pleinement ; les données constructeur d'Ex2/Ex3 sont données inline sans encadré docTech ni question d'extraction.  
  Passage : `La documentation constructeur donne, en r\'egime nominal : tension nominale $U_n = \SI{200}{\volt}$`
- **Ex. 4 et 5** [pedagogie] — Recouvrement quasi identique avec la fiche T11 : Ex4 = QT1 (mêmes données 750 V, 380 A, k2=0,1, même loi R_th(V)) et Ex5 = QT3 (mêmes 96 kW, 1035 tr/min, 557 N·m, même conclusion). 2 exercices sur 6 dupliquent les Questions Types de la fiche de cours.  
  Passage : `QT1 - D\'emarrage rh\'eostatique... E2 sujet 2019 (Q7-9) / QT3 - Couple nominal... (Q28)`
- **Ex. 5 q.3** [source] **[RÉFUTÉ — écarté]** — C_th ≈ 557 N·m présenté comme donnée du système réel (« couple thermique équivalent estimé sur le trajet ») : cette valeur est le résultat de la Q27 du sujet 2019, introuvable dans E2_Sujet_2019.md et absente du Rapport_Jury_2019.md (corrigé E2 non publié). Valeur physiquement plausible mais invérifiable — reprise telle quelle de la fiche T11 QT3.  
  Passage : `le couple thermique \'equivalent estim\'e sur le trajet complet de la rame VMI est $C_{th} \approx \SI{557}{\newton\meter}$`

**🟨 Mineur**
- **Ex. 4** [source] — Titre annonce « questions 7 à 9 » mais l'exercice ne couvre que Q7 (courant + loi de commande, scindée en q1/q2) et Q8 (p(t)) ; la Q9 du sujet (énergie ERh sur Δt1) n'est pas traitée.  
  Passage : `2019, \'Etude d'un syst\`eme..., questions 7 \`a 9`
- **Ex. 2** [schema] — Chronogramme : le label « 0,5 » de l'asymptote est un \node sans coordonnée « at », donc placé à l'origine (0,0) au lieu de (0;2,5) — la valeur finale du courant n'est pas lisible au bon endroit sur la figure.  
  Passage : `\draw[dashed, gray] (0,2.5) -- (7,2.5); \node[left] {\footnotesize $0,5$};`
- **Ex. 3** [schema] — Exercice fondé sur le modèle de circuit de l'induit mais sans schéma propre (renvoi implicite « On reprend l'actionneur de l'exercice précédent ») ; le schéma d'écoulement des puissances (Figure A3 du sujet) n'est pas non plus reproduit pour la q3.  
  Passage : `On reprend l'actionneur \`a courant continu de l'exercice pr\'ec\'edent`
- **Ex. 2** [forme] — Décimales en mode math sans accolades dans le chronogramme : $0,5$ et $0,315$ rendent « 0, 5 » avec espace après la virgule (règle 0{,}5).  
  Passage : `\node[left] at (0,1.575) {\footnotesize $0,315$};`
- **Ex. 2, 3, 5** [forme] — Nombres ≥ 4 chiffres sans séparateur \, en mode math : 1800 (l.93, 136, 151), 1035 (l.217, 229), 96000 (l.230) — règle 96\,000.  
  Passage : `C_{nom} = \frac{P_n}{\Omega_n} = \frac{96000}{108{,}4}`
- **Ex. 1, 2, 3** [pedagogie] — Corrigés sans phrase de conclusion finale reliant le résultat numérique à une exigence/un critère (Ex2 s'arrête sur L ≈ 100 mH ; Ex1 et Ex3 s'arrêtent sur le rendement sans critère de validation). Ex4, Ex5, Ex6 concluent correctement.  
  Passage : `L = R \cdot \tau = 6{,}6 \times 15\times10^{-3} \approx \SI{99}{\milli\henry} \approx \SI{100}{\milli\henry}`
- **Ex. 5** [structure] — Gradation non progressive : Ex5 est \difficulte{1} placé après deux exercices \difficulte{3} (séquence 1-2-3-3-1-2) ; l'ordre par source prime sur la progression pédagogique.  
  Passage : `Exercice 5 -- \difficulte{1}`
- **Ex. 6** [source] — Déclaré « inédit » mais très proche de la question A10 du sujet 2026 déjà exploité par Ex2/Ex3 (quadrants du plan couple-vitesse + conclusion sur la structure de variateur) ; pas de fabrication, mais l'origine mériterait d'être mentionnée.  
  Passage : `exercice in\'edit ... associer \`a chacun un mode de fonctionnement`

*Non vérifié par l'agent : Valeur Cth=557 N·m (résultat du corrigé Q27 2019, corrigé E2 absent des sources locales) ; titre exact de l'épreuve E2 2019 admis sur la foi du commentaire d'en-tête du fichier (vérifié le 2026-07-15 sur la page de garde PDF, non re-vérifié ici) ; rendu visuel effectif des 2 PDF (audit sans recompilation, conformément à la consigne).*


### T12 — Machine synchrone (62/100) — `exercices/T12_exercices.tex`

Structure 24/30 · Exactitude 13/35 · Pédagogie 10/15 · Forme 9/10 · Sources 6/10 — 5 exercices

**Sources vérifiées** : ex1: 2024 E2 appliquée Q45-46 OK (E2_Appliquee_Commune_2024.md l.345, 564-568 : 28 pôles, R=20 cm, 72 V ; Rapport_Jury_2024.md l.883-887 : f0=185,6 Hz, couplage triangle). ex2: 2025 Q18/Q21 OK (E2_Appliquee_Commune_2025.md l.348, 366-370 ; Rapport_Jury_2025.md l.642-644 et 656-658 : 1833 µs, 0,555 µs, 1,8 MHz, 84 MHz Arduino repris verbatim) MAIS « point de vigilance jury » INTROUVABLE dans le rapport (fabriqué). ex3: 2023 A6-A7 OK (E2_Disciplinaire_IE_2023.md l.155-157 : Crr=0,05, F=2000 N ; l.237 : rendement global 63 % ; Rapport_Jury_2023.md l.171-176 : Pmoy=3584 W, Pabs=5715 W pour M=2500 kg). ex4: 2024 Q48/49/51 OK (Rapport_Jury_2024.md l.893 citation « unidirectionnel en courant et en tension » exacte, l.905-911 : Nsc=5, Ceq=13 F, UCeqmax=81 V ; E2_Appliquee_Commune_2024.md l.602-604 : 65 F, 16,2 V). ex5: inédit, rien à vérifier.

**🟥 Bloquant**
- **Ex. 5 q.3** [calcul] **[CONFIRMÉ]** — Réponse finale physiquement fausse : le corrigé affirme qu'en moteur le rotor est EN AVANCE sur le champ tournant et en générateur en retard — c'est l'inverse. Le propre calcul du corrigé (E_y = −170 V, donc arg(E) = −53,8°, E en retard sur V_s) et la fiche de cours T12 (l.69 : « en moteur, E est en retard sur V_s ») contredisent cette affirmation. *(affiché : moteur : rotor en avance sur le champ tournant ; générateur : en retard — recalcul : E = 230 − (105,4 + j170) = 124,6 − j170 → arg(E) = −53,8° : E en RETARD sur V_s en moteur (rotor en retard sur le champ tournant) ; en générateur E en avance)*  
  Passage : `en moteur, le rotor est en avance sur le champ tournant ($\delta > 0$)~; en g\'en\'erateur, il est en retard`

**🟧 Majeur**
- **Ex. 5 q.2** [calcul] **[CONFIRMÉ]** — Interprétation mathématique fausse du signe : une partie imaginaire négative (E_y = −170 V, V_s référence des phases) signifie que E est en retard sur V_s, pas en avance. La parenthèse inverse le sens du déphasage. *(affiché : E_y < 0 → E en avance sur V_s — recalcul : E_y < 0 → phase de E négative → E en retard de δ = 53,8° sur V_s)*  
  Passage : `le signe n\'egatif de $E_y$ traduit le fait que le rotor -- donc $\underline{E}$ -- est en avance sur $\underline{V}_s$`
- **Ex. 5** [schema] — Le diagramme de Fresnel de l'énoncé place E au-dessus de l'axe réel (en avance sur V_s, coordonnée (1.24, 2.0)) et trace −jX_sI_s vers le haut-gauche, alors que le calcul du corrigé donne E = 124,6 − j170 (sous l'axe) et −jX_sI_s = −105,4 − j170 (bas-gauche). Schéma incohérent avec le corrigé et avec la physique en convention moteur.  
  Passage : `\coordinate (E) at (1.24,2.0); ... \draw[-latex, dashed, orange] (Vs) -- (E) node[midway, above right]{$-jX_s\underline{I}_s$}`
- **Ex. tous** [structure] — Aucun exercice « lecture de document technique » (nb_docTech = 0 dans la pré-passe) alors que la notion machine synchrone/brushless s'y prête pleinement (plaque signalétique, datasheet PMSM, courbe couple-vitesse constructeur) et que le gabarit l'exige pour ce type de notion.  
  Passage : `nb_docTech: 0 (pré-passe) — 5 exoBox, aucun encadré docTech ni question d'extraction`
- **Ex. 2** [source] **[CONFIRMÉ]** — « Point de vigilance jury » attribué au rapport de jury CAPET 2025 introuvable : le Rapport_Jury_2025.md (Q18, l.642-644) donne uniquement le corrigé de la définition servomoteur, sans aucun commentaire sur une « confusion fréquente » entre servomoteur et moteur classique. Commentaire jury fabriqué présenté comme authentique.  
  Passage : `Point de vigilance jury (rapport de jury CAPET 2025, \'epreuve appliqu\'ee) : la confusion entre servomoteur et moteur classique`
- **Ex. 1, 2, 3** [pedagogie] — Recouvrement quasi identique avec les Questions Types de la fiche T12_Machine_Synchrone.tex : Ex1 = QT1 (Urbanloop 2024 Q44-46, mêmes données 28 pôles/72 V/60 km·h⁻¹/f0 = 185,6 Hz), Ex2 q.1 = QT2 (servomoteur Q18 2025 KUKA), Ex3 = QT3 (chaîne de puissance Bakus 2023). 3 exercices sur 5 dupliquent la fiche au lieu d'offrir un entraînement complémentaire.  
  Passage : `fiche T12 : QT1 - Fréquence d'alimentation et couplage - capsule Urbanloop ... E2 appl. 2024 (Q44-46)`

**🟨 Mineur**
- **Ex. 5 q.2** [calcul] — Erreur d'arrondi au-delà du légitime sur le module de E : √(15525 + 28900) = √44425 = 210,8 V, le corrigé affiche 210,5 V (210,5² = 44310). *(affiché : 210,5 V — recalcul : √(124,6² + 170²) = √44425,2 = 210,8 V)*  
  Passage : `\sqrt{15525 + 28900} \approx \SI{210,5}{\volt}`
- **Ex. 2** [schema] — Chronogramme PWM à échelle incohérente sans rupture d'axe : t_h = 1,83 ms placé à x = 1,83 mais T = 20 ms à x = 8,2, l'état bas paraît ~3,5 fois l'état haut au lieu de ~10 fois ; une rupture d'axe ou une échelle homogène serait attendue.  
  Passage : `\draw[thick] (0,1) -- (1.83,1) -- (1.83,0) -- (8.2,0);`
- **Ex. 1, 2, 3, 5** [forme] — Nombres ≥ 4 chiffres sans séparateur \, dans du contenu mathématique rendu : 60000 et 3600 (ex1 l.65), 1500/1833/1000/1800 (ex2), 4000/3600/1226/3585/5690 (ex3), 15525/28900 (ex5 l.250). Règle du gabarit : 17\,689.  
  Passage : `60000/3600 = \SI{16,67}... ; \sqrt{15525 + 28900}`
- **Ex. 3, 4** [pedagogie] — Corrigés sans phrase de conclusion finale reliant le résultat numérique à une exigence ou un critère (règle du gabarit) : Ex3 se termine sur l'explication de l'écart d'arrondi, Ex4 sur U_Ceq,max = 81 V sans relier à la marge par rapport aux 72 V du bus.  
  Passage : `U_{Ceq,max} = 5 \times 16{,}2 = \SI{81}{\volt} (fin du corrigé, pas de conclusion)`

*Non vérifié par l'agent : Rendu visuel des 2 PDF non inspecté (compilations OK d'après la pré-passe : énoncés 2 p., corrigés 3 p., 0 erreur/0 warning) ; vérification des sources faite sur les conversions Markdown (Marker), pas sur les PDFs originaux ; numérotation exacte Q44 vs Q45 du sujet 2024 non tranchée (le rapport traite f0 en Q45 et le couplage en Q46, cohérent avec le titre de l'Ex1).*


### T13 — Machine asynchrone (83/100) — `exercices/T13_exercices.tex`

Structure 25/30 · Exactitude 30/35 · Pédagogie 10/15 · Forme 8/10 · Sources 10/10 — 5 exercices

**Sources vérifiées** : ex1: 2024 E2 disciplinaire (extracteur d'air) A2/A3/A5/A6 OK — plaque (400 V, 230 V, 229 A, cosφ 0,85, 1400 tr/min, p=2), I'r=122 A et Cp=200 N·m (l.149), DT1 R'R=0,1 Ω / Lf=3,6 mH (l.803-807), « Pour la suite on pose Pu = 100 kW » (l.161) ; citation jury 2024 vérifiée VERBATIM (Rapport_Jury_2024, § épreuve disciplinaire : « le jury regrette le manque de maîtrise des formules de base sur les réseaux triphasés... »). ex2: 2023 E2 appliquée commune Q18 OK (l.313) ; N=950 tr/min, p=3, Ns=1000 confirmés par le corrigé officiel reproduit dans Rapport_Jury_2023 (l.720) ; citation jury 2023 VERBATIM (l.1037). ex3: 2024 C1-C2 OK (l.325-331) — mais la formule cible C1 est déformée dans l'énoncé de l'exercice (cf. constat calcul). ex4: 2024 C3 OK + DT1 J=0,035 kg·m², f=4·10⁻³ (l.869-871). ex5: inédit assumé (le vrai B10 utilise les rangs 3/5/7/9) ; norme IEC/EN 61000-2-2 THD<25 % VERBATIM dans le sujet 2024 (l.301) ; loi 1/n pleine onde (20/14,3/9,1/7,7 %) physiquement exacte.

**🟧 Majeur**
- **Ex. 3 q.2** [calcul] **[CONFIRMÉ]** — La formule cible que l'énoncé demande de démontrer est dimensionnellement fausse : il manque un facteur omega_s (la forme en omega_s^2 ne vaut que multipliée par omega_r = g·omega_s, comme en q.3). Le corrigé la « retrouve » via une égalité algébrique fausse : (3pVs²/(R'R ωs²))(g ωs) n'est pas égal à (3pVs²/(R'R ωs²))g. Le sujet réel 2024 (C1) donne la forme correcte Cem = (3p/R'R)(Vs/ωs)²·ωs·g. Les résultats numériques finaux (673 et 426 N·m) restent justes car calculés par la voie A·ωr. *(affiché : Cem = 3pVs²/(R'R·ωs²)·g (donnerait 32,2×0,0667 ≈ 2,15 N·m) — recalcul : Cem = 3pVs²·g/(R'R·ωs) = 317400×0,0667/9869,6·... ≈ 426 N·m ; la forme en ωs² n'est correcte que sous C_em = A·ω_r)*  
  Passage : `C_{em} = \frac{3p\,V_s^2}{R'_R\,\omega_s^2}\,g . \] (l.134) puis \,(g\,\omega_s) = ...\,g . (l.148)`
- **Ex. toutes** [structure] — Aucun exercice « lecture de document technique » (nb_docTech = 0 dans la pré-passe) alors que la notion Machine asynchrone s'y prête pleinement (plaque signalétique, DT1 du sujet 2024, figure 6 du sujet 2023) et que le gabarit l'exige : pas d'encadré docTech ni de première question d'extraction.  
  Passage : `"nb_docTech": 0 (pré-passe) — ex.1 cite « document technique DT1 du sujet » sans encadré docTech`
- **Ex. 1, 3, 4** [pedagogie] — Recouvrement quasi identique avec les Questions Types de la fiche T13_Machine_Asynchrone.tex : QT1 (Ns/g/Pa = 134,3 kW, mêmes données plaque 2024), QT2 (bilan de puissance R'R=0,1 Ω, I'r=122 A, Cp=200 N·m) et QT3 (couple linéarisé C1-C3 + Laplace) reprennent le même sujet 2024 avec les mêmes valeurs que les exercices 1, 3 et 4 — 3 exercices sur 5 dupliquent la fiche au lieu d'entraîner sur des variantes.  
  Passage : `fiche T13 : QT1 « E2 disc. 2024 (A1-A7, extracteur d'air) »... P_a = 134,3 kW ; QT2 I'r=122 A ; QT3 C1-C3`

**🟨 Mineur**
- **Ex. 4** [pedagogie] — Le corrigé se termine par le schéma-bloc sans phrase de conclusion reliant le résultat numérique (Kmeca = 250, τmeca = 8,75 s) à une exigence ou un critère (règle du gabarit).  
  Passage : `\draw[-latex] (block) -- ++(2.1,0) node[right]{$\Omega(p)$}; — fin du corrigé, pas de conclusion`
- **Ex. 1, 2, 3** [forme] — Nombreux nombres ≥ 4 chiffres sans séparateur de milliers \, dans du contenu mathématique rendu : 1500, 1400, 14884, 67000, 3000, 1000, 98696, 317400, 9869,6 (règle : 17\,689). Les occurrences 61000 (norme) sont légitimes.  
  Passage : `3\times 1{,}5\times 14884 ... \frac{317400}{9869{,}6}`
- **Ex. 1, 4** [forme] — Unités composées hors siunitx : « tr$\cdot$min$^{-1}$ » (ex.1, 2) et « N$\cdot$m$\cdot$s$\cdot$rad$^{-1}$ » (ex.4) écrites à la main alors que la règle du projet impose siunitx (utilisé ailleurs, ex. \SI{146,6}{rad.s^{-1}}).  
  Passage : `$f = 4\times 10^{-3}$~N$\cdot$m$\cdot$s$\cdot$rad$^{-1}$`

*Non vérifié par l'agent : Figure 6 du sujet 2023 (tableau des caractéristiques MAS, image non OCRisée) — la valeur 950 tr/min n'y est vérifiable qu'indirectement, via le corrigé du rapport jury 2023 (vérifié) ; la valeur Pextra/η ≈ 99 kW citée en ex.1 q.5 (dépend du débit Dt de la question A1, non extrait) ; rendu visuel des PDF compilés (non inspecté, compilation 2×3 pages sans erreur ni warning selon la pré-passe).*


### T14 — Variation de vitesse (59/100) — `exercices/T14_exercices.tex`

Structure 23/30 · Exactitude 14/35 · Pédagogie 7/15 · Forme 7/10 · Sources 8/10 — 6 exercices

**Sources vérifiées** : ex1: 2024 E1 q.A3 OK (E1_Sujet_2024.md l.143 champs tournants, l.171 N=1400 tr/min); ex2: 2024 E1 C5-C11 OK (Kmeca=250, taumeca=8,5 s l.369 ; m=1, Tr=1 s, omega0=5/Tr l.361-367 ; Rapport_Jury_2024 l.277 Kp=0.35/Ki=2.5, l.290 Mphi1=180 deg) mais plage citee "C3, C6 a C11" imprecise (Hbf = C5); ex3: 2024 E1 B10-B11 OK (l.299-303, norme 61000-2-2 <25 %) — le rapport officiel B10 affiche lui aussi 0.59 (valeur arithmetiquement fausse, fiche T14 corrigee a 61,4 %); ex4: 2021 E2 Q15-18 OK (Rapport_Jury_2021 l.651 : 160,4 A meme formule ; l.639 ATV630C11N4 ; l.641 NSX250N MA220 ; l.653 In=170 A) + citation jury verbatim exacte l.769; ex5: 2026 E1 q.A10 OK (l.193 R=6,6/L=100 mH ; l.219 Ke=Kc=1,044, Cp=0,052 ; l.235 enonce A10 quadrants + structure variateur); ex6: inedit (rien a verifier) + citation jury 2020 verbatim exacte l.709 (contexte d'origine : batterie, pas variation de vitesse)

**🟥 Bloquant**
- **Ex. 3 q.2** [calcul] **[CONFIRMÉ]** — THD cas 1 (pleine onde) faux : sqrt(10883)/170 = 0,614 soit 61,4 %, pas 0,59. La chaine de calcul affichee est interne­ment incoherente. Le Rapport_Jury_2024 (l.229) affiche lui aussi 0.59 (erreur du corrige officiel), mais la fiche T14 du projet a deja ete corrigee a 61,4 % (audit fiches, l.196 de T14_Variation_Vitesse.tex) — l'exercice reproduit la valeur fausse. Propagee en q.3 (« THD = 59 % »). *(affiché : 0,59 (59 %) — recalcul : 95^2+27^2+27^2+20^2 = 10883 ; sqrt = 104,32 ; 104,32/170 = 0,614 = 61,4 %)*  
  Passage : `\frac{\sqrt{10883}}{170} \approx 0{,}59`

**🟧 Majeur**
- **Ex. 3 q.3** [calcul] **[CONFIRMÉ]** — THD cas 2 : sqrt(1853)/170 = 0,2532 soit 25,3 % > 25 % ; conclure « conforme » a la norme (< 25 %) est strictement faux. La fiche T14 corrigee retient 25,3 %. Le corrige arrondit a 0,25 pour conclure a la conformite. *(affiché : 0,25 ; conforme — recalcul : 37^2+22^2 = 1853 ; sqrt = 43,05 ; 43,05/170 = 0,2532 = 25,3 % > 25 %)*  
  Passage : `Cas 2 : $THD = 25\,\%$, la commande MLI est (tout juste) \textbf{conforme}`
- **Ex. 4** [structure] — Aucun exercice « lecture de document technique » : nb_docTech = 0 alors que la notion variation de vitesse s'y prete parfaitement (DT9/DT10 ATV630 du sujet 2021 disponibles). L'ex. 4 paraphrase le document technique dans le corps de l'enonce au lieu d'un encadre docTech avec premiere question d'extraction.  
  Passage : `Le document technique du variateur ATV630 indique, pour une surcharge admissible de 150\,\%`
- **Ex. 2 q.4** [pedagogie] — Question non autosuffisante : la marge de phase de 180° provient d'une lecture graphique du DT4 avec la definition particuliere du sujet 2024 (Mφ = Arg(Hbf(0dB)) + 180°), ni le DT4 ni cette definition ne sont fournis dans l'enonce. Avec la definition standard (boucle ouverte equivalente ω0²/(p(p+2mω0)), m=1), Mφ ≈ 76° < 90° et l'exigence ne serait PAS respectee. Le corrige affirme une valeur non derivable des donnees. *(affiché : Mφ = 180° — recalcul : L(p)=ω0²/(p(p+2ω0)) ; |L|=1 a ω=0,486ω0 ; phase = -90-atan(0,243) = -103,7° ; Mφ ≈ 76°)*  
  Passage : `la marge de phase relev\'ee est de $180^\circ \geq 90^\circ$`
- **Ex. 3 et 4** [pedagogie] — Recouvrement quasi identique avec les deux Questions Types de la fiche T14_Variation_Vitesse.tex : QT1 (E1 2024 B10-B11, memes valeurs 170/95/27/27/20 et 37/22) = ex. 3 ; QT2 (2021 Q15-18, memes 90 kW, cosφ 0,86, η 0,942, ATV630C11N4, 170 A, NSX250N MA220) = ex. 4. Un tiers de la banque duplique la fiche.  
  Passage : `QT1 - THD et conformité norme - commande MLI vs pleine onde ... E1 2024 (B10-B11)`

**🟨 Mineur**
- **Ex. 2 et 6** [structure] — Gradation peu plausible : 1, 3, 2, 2, 2, 1 — le niveau 3 arrive en 2e position et la banque se termine par un niveau 1. Les bornes (niveaux 1 et 3 presents) sont respectees.  
  Passage : `Exercice 2 -- \difficulte{3}`
- **Ex. 2** [source] — Libelle de source imprecis : le titre annonce « questions C3, C6 a C11 » mais l'etablissement de Hbf demande en q.1 correspond a la question C5 du sujet 2024 (absente de la plage citee).  
  Passage : `questions C3, C6 \`a C11`
- **Ex. 6** [source] — Citation jury 2020 authentique (verbatim exact, Rapport_Jury_2020.md l.709) mais sortie de son contexte : elle porte sur la partie dimensionnement de batterie du robot, pas sur une etude de variation de vitesse.  
  Passage : `le jury note ici les progr\`es des candidats quant aux conversions d'unit\'es`
- **Ex. 6 q.3** [forme] — Unite hors siunitx : \num{15048}\ \text{W} au lieu de \SI{15048}{\watt} ; de meme tr.min^-1 compose en $\text{tr}\cdot\text{min}^{-1}$ dans les enonces des ex. 1 et 6 au lieu de siunitx.  
  Passage : `\approx \num{15048}\ \text{W} \approx \SI{15,05}{\kilo\watt}`
- **Ex. 3 q.2** [forme] — Nombres >= 4 chiffres sans separateur de milliers dans les calculs des corriges : 9025, 10883, 1369, 1853 (la fiche T14 ecrit 10\,883). Regle du projet : 17\,689.  
  Passage : `\frac{\sqrt{9025+729+729+400}}{170}`
- **Ex. 2 q.4** [forme] — Typo : « apriodique » pour « aperiodique ».  
  Passage : `syst\`eme apriodique critique, sans r\'esonance`
- **Ex. 1** [pedagogie] — Le corrige ne se termine pas par une phrase de conclusion reliant les resultats (Ns = 1500 tr/min, g = 6,7 %) a une exigence ou un critere (regle du gabarit).  
  Passage : `(commande scalaire dite \guillemotleft\ \`a flux constant \guillemotright)`
- **Ex. 5 q.2** [schema] — Legende du schema corrige incoherente : « Zones hachurees » alors que les quadrants I et III sont remplis en aplat (fill colExo!25), pas hachures (le sujet 2026 demandait de hachurer le DRA2).  
  Passage : `Zones hachur\'ees : quadrants I (moteur, sens de rotation 1) et III`

*Non vérifié par l'agent : DT3 du sujet 2024 (tableau des harmoniques 170/95/27/27/20 et 37/22) et DT4 (Bode) sont des images omises dans la conversion Markdown : valeurs verifiees indirectement via les calculs du Rapport_Jury_2024 (B10) qui utilisent exactement ces amplitudes ; DT9 2021 (In variateur 170 A) confirme via le rapport, pas le tableau constructeur lui-meme. Rendu visuel des 5 schemas TikZ non inspecte (audit sans compilation, conformement a la consigne).*


### T15 — Stockage de l'énergie (65/100) — `exercices/T15_exercices.tex`

Structure 23/30 · Exactitude 20/35 · Pédagogie 10/15 · Forme 8/10 · Sources 4/10 — 6 exercices

**Sources vérifiées** : ex1 : Rapport_Jury_2020 Q21-22 OK mot pour mot (l.486-502 : 13 série, 4 parallèle, 52 cellules, 4,784 kg, <5 kg) mais épreuve mal nommée (voir constat) ; ex2 : E2_Sujet_2026_BAC3 A3-A4 OK (l.131 : 128,4 kW·h, 600 V, 2 branches × 2 modules, NMC HpCO 3,5 V/53,5 A·h ; l.143) ; ex3 : A5 OK (l.103, 145-147 : 20 % de décharge, 22 kW, 40 km/h) mais lecture DoD contestable et « 80 km » INTROUVABLE (sujet : trajet type 200 km) ; ex4 : E2_Sujet_2021 Q5-Q10 + Rapport_Jury_2021 OK (l.557-587 : 318,825 kW·h, 248,68, 43 %, 160 m³/h, 5,625 h, 76 kW, 427,5, 58,17 %) mais citation jury guillemetée FABRIQUÉE (introuvable) ; ex5 : Rapport_Jury_2020 Q14-15 OK mot pour mot (l.1467-1492 : Ec=4654 W·h/j, 969,6 A·h, 8 batteries 130 A·h, 304 kg, alternative 220 A·h) et quote « % de décharge vs profondeur de décharge » quasi verbatim (l.1451-1453) ; ex6 : inédit, rien à vérifier.

**🟥 Bloquant**
- **Ex. 4** [source] **[CONFIRMÉ]** — Citation jury 2021 présentée comme verbatim (guillemets + attribution « rapport de jury CAPET 2021 ») mais FABRIQUÉE : introuvable dans Rapport_Jury_2021.md. Le rapport contient seulement, en éléments de correction Q10, « n'est pas très performant (rendement de 58%) … plus respectueux de l'environnement que le stockage par batterie » et, en commentaire, « la conclusion finale a été souvent insuffisante ». La phrase guillemetée est une synthèse inventée présentée comme authentique.  
  Passage : `\guillemotleft\ la conclusion quant aux performances et \`a l'int\'er\^et du proc\'ed\'e … devait mentionner`

**🟧 Majeur**
- **Ex. 3** [calcul] **[RÉFUTÉ — écarté]** — Définition du DoD auto-contradictoire et inversée par rapport au sujet. L'énoncé pose DoD_max = 20 % puis affirme « jamais déchargée en dessous de 20 % de sa charge » (cela correspond à DoD_max = 80 %, pas 20 %). Le sujet réel 2026 dit « elles ne sont exploitées que jusqu'à 20 % de décharge » (lecture littérale : 20 % exploitables, cohérente avec la durée de vie de 8 ans). Le corrigé retient 80 % exploitables ; le symbole « DoD_min restant » de la formule n'est défini nulle part. *(affiché : E_utile = 102,72 kW·h ; t = 4,67 h ; d = 186,8 km — recalcul : Lecture littérale du sujet (DoD_max = 20 %) : E_utile = 0,20×128,4 = 25,68 kW·h ; t = 25,68/22 = 1,17 h ; d ≈ 46,7 km — conclusion opposée possible)*  
  Passage : `taux de d\'echarge maximal $DoD_{max} = 20\,\%$ : … jamais d\'echarg\'ee en dessous de 20~\% de sa charge`
- **Ex. 3** [source] **[CONFIRMÉ]** — Donnée « trajet type le plus éloigné du dépôt ≈ 80 km » introuvable dans E2_Sujet_2026_BAC3 : le sujet parle d'un trajet type de 200 km (l.125) et la question A5 ne fournit aucune distance au dépôt. Valeur inventée insérée dans un exercice sourcé « 2026, question A5 ».  
  Passage : `le trajet type le plus \'eloign\'e du d\'ep\^ot repr\'esente environ \SI{80}{\kilo\meter}`
- **Ex. 1** [schema] — Schéma circuitikz électriquement faux : chaque rail referme une branche série sur elle-même (le tracé relie l'extrémité gauche et l'extrémité droite de la MÊME branche), donc les deux branches sont chacune court-circuitées et ne sont jamais interconnectées en parallèle ; la flèche U_nom pointe dans le vide, non reliée au circuit.  
  Passage : `\draw (0,1.1) -- (0,1.6) -- (5.6,1.6) -- (5.6,1.1);`
- **Ex. 5** [schema] — Même défaut de topologie : les rails haut et bas court-circuitent respectivement la batterie du haut et celle du bas sur elles-mêmes (bornes gauche et droite d'une même batterie reliées), la batterie centrale n'est connectée à rien, aucun bus parallèle commun ; la sortie 12 V flotte.  
  Passage : `\draw (0,0) -- (0,-0.5) -- (2.9,-0.5) -- (2.9,0);`
- **Ex. toutes** [structure] — Aucun exercice « lecture de document technique » (nb_docTech = 0) alors que la notion s'y prête pleinement : les sujets sources eux-mêmes s'appuient sur des DT (DT6/DT7 courbes de pompe 2021, fiche cellule NMC 2026, doc constructeur batteries 2020). Un exercice avec encadré docTech et première question d'extraction était attendu.  
  Passage : `nb_docTech = 0 (pré-passe) — aucun encadré docTech dans le fichier`
- **Ex. 1 à 4** [pedagogie] — Recouvrement quasi identique avec les 3 Questions Types de la fiche T15_Stockage_Energie.tex : QT1 (Hycity 2026 A3-A5, 86 cellules/214 A·h/186,8 km) = exercices 2+3 ; QT2 (robot 2020 Q20-22) = exercice 1 ; QT3 (STEP 2021 Q5-Q10, 318,8/248,7/58 %) = exercice 4. 4 des 6 exercices dupliquent la fiche avec les mêmes questions et les mêmes valeurs, sans variation.  
  Passage : `fiche : QT1 - … bus Hycity … E2 appl. 2026 (Q A3-A5) / QT3 - … STEP … 2021 (Q5-Q10)`

**🟨 Mineur**
- **Ex. 1** [source] — Épreuve mal attribuée : les questions 21/22 du robot proviennent de l'épreuve « analyse et exploitation pédagogique d'un système pluritechnique » (Rapport_Jury_2020, section l.332), pas de « Étude d'un système, d'un procédé ou d'une organisation » (qui est, pour l'IE 2020, le dessalinisateur). Toutes les valeurs sont par ailleurs exactes.  
  Passage : `2020, \'Etude d'un syst\`eme, questions 21 et 22`
- **Ex. 6** [schema] — Exercice portant sur un signal temporel (décharge à courant constant, intégration de i(t), évolution du SOC) sans chronogramme tikz i(t)/SOC(t), attendu par la règle du skill ; impact limité car le signal est constant.  
  Passage : `pr\'el\`eve un courant constant $I = \SI{2}{\ampere}$ pendant une dur\'ee $\Delta t = \SI{3}{\hour}$`
- **Ex. 2, 6** [pedagogie] — Corrigés sans phrase de conclusion reliant le résultat à une exigence/un critère (règle du gabarit) : l'ex. 2 s'arrête sur N_total = 688 sans conclusion ; l'ex. 6 se termine sur une explication sans lien à un critère.  
  Passage : `\[ N_{total} = 4\times 172 = 688\ \text{cellules} \]`
- **Ex. 4, 5** [forme] — Nombres ≥ 4 chiffres sans séparateur \, dans du contenu mathématique rendu : 4654, 9308 (ex. 5, l.238/240), 1148 et 1000 (ex. 4, l.189-190), contrairement à la règle 17\,689 (respectée ailleurs : 128\,400 l.122).  
  Passage : `E_{2\,jours} = 2\times 4654 = \SI{9308}{\watt\hour}`
- **Ex. 4** [forme] — Faute d'accord dans l'énoncé : « alimenté » au lieu de « alimente ».  
  Passage : `Une micro-STEP … solaire aliment\'e un village de montagne`
- **Ex. 6** [forme] — Orthographe : « comptage coulombétrique » (et « coulombmétrique » dans le commentaire d'en-tête) au lieu de « coulométrique ».  
  Passage : `principe du comptage coulomb\'etrique (intensiom\'etrique)`

*Non vérifié par l'agent : Corrigé officiel 2026 indisponible (aucun E2_Corrige_2026 dans la base) : l'interprétation officielle du « 20 % de décharge » de la question A5 n'a pas pu être tranchée définitivement (constat rédigé sur la lecture littérale du sujet). Rendu PDF non inspecté visuellement (audit sur source + résultats de compilation de la pré-passe uniquement).*


### T16 — Énergies renouvelables (76/100) — `exercices/T16_exercices.tex`

Structure 23/30 · Exactitude 30/35 · Pédagogie 11/15 · Forme 8/10 · Sources 4/10 — 6 exercices

**Sources vérifiées** : ex1: 2021 E2 Q11/Q12/Q14 OK (E2_Sujet_2021 l.161-195 : DMH320M6 320 W, 1675x992 mm, 600 W/m²+50°C ; Rapport_Jury_2021 l.595-619 : 782 panneaux, 1298 m², Voc_cell=0,683 V, chute 10%) ; ex2: 2021 Q13 données OK (Rapport_Jury_2021 l.609-615 : 30 entrées, 26 panneaux, 8320 W, 892,32 V, 9,34 A ; plage MPPT 200-800 V explicitement annoncée comme inventée) mais citation jury INTROUVABLE ; ex3: 2025 E2 Disciplinaire Q17-19 OK (E2_Disciplinaire_IE_2025 l.240-252 : U1=195 V/I1=7,5 A, U2=340 V/I2=7,5 A, Unom=317 V, Eb=48 V, UPV=fm·Eb ; Rapport_Jury_2025 l.335 : fm=4,06/6,6/7,08), citation jury quasi-verbatim (l.331, légèrement réécrite) — mais fm y est une « fonction de modulation », pas un rapport cyclique ; ex4: inédit (rien à vérifier) ; ex5: inédit (rien à vérifier) ; ex6: 2022 Q19 OK (Rapport_Jury_2022 l.270-273 : tableau Peltier/Turbine-Alternateur/Panneaux PV avantages-inconvénients)

**🟥 Bloquant**
- **Ex. 2** [source] **[CONFIRMÉ]** — Citation jury 2021 entre guillemets introuvable dans Rapport_Jury_2021.md : le rapport dit seulement « la plupart d'entre eux ont rencontré des difficultés à justifier le choix de l'onduleur » (l.757) et « Le jury déplore... » (l.759). La phrase citée est une synthèse reformulée présentée comme verbatim authentique.  
  Passage : `\guillemotleft\ le jury insiste sur la n\'ecessit\'e de justifier le choix de l'onduleur en v\'erifiant...`

**🟧 Majeur**
- **Ex. 3 q.3** [calcul] **[CONFIRMÉ]** — fm est appelé « rapport cyclique du hacheur élévateur » alors qu'un rapport cyclique est borné à 1 : les valeurs 4,06/6,60/7,08 sont physiquement impossibles pour un rapport cyclique. Le sujet 2025 définit fm comme une « fonction de modulation » (UPV = fm·Eb, l.252). La conclusion « confirment le rôle élévateur (tension d'entrée supérieure à la tension de bus) » est incohérente : côté PV (317 V) vers bus (48 V) c'est un abaissement — la fiche T16 corrigée dit d'ailleurs « hacheur abaisseur ». Valeurs numériques elles-mêmes conformes au jury. *(affiché : rapport cyclique fm = 4,06 ; 6,60 ; 7,08 (>1), « confirment le rôle élévateur » — recalcul : 195/48=4,06 ; 317/48=6,60 ; 340/48=7,08 : arithmétique exacte, mais fm = fonction de modulation (sujet 2025), pas un rapport cyclique (0≤α≤1))*  
  Passage : `Le rapport cyclique du hacheur \'el\'evateur est donn\'e par $f_m = U_{PV}/E_b$`
- **Ex. 1-2** [structure] — Aucun exercice « lecture de document technique » (nb_docTech=0) alors que la notion s'y prête pleinement : le sujet 2021 source repose sur la datasheet DT7 du panneau DMH320M6 et la plage MPPT d'un onduleur. Les données constructeur sont diluées dans le texte des énoncés 1 et 2 sans encadré docTech ni question d'extraction.  
  Passage : `Le constructeur donne, pour le panneau complet en STC : $I_{sc} = \SI{9,76}{\ampere}$...`
- **Ex. 1, 2, 3** [pedagogie] — Recouvrement quasi identique avec les Questions Types de la fiche T16 : ex1 q1 = QT fiche (N=250000/320=782, 1298≈1300 m²), ex2 = QT fiche (782/30=26 panneaux/entrée + vérif onduleur), ex3 q1-q2 = QT P&O de la fiche (U_MPP=317 V, convergence ΔP). 3 exercices sur 6 refont les mêmes calculs avec les mêmes valeurs.  
  Passage : `fiche l.191 : $N = 250\,000 / 320 = 782$ ; l.215 : $782/30 \approx 26$ ; l.238 : $U_{MPP}=317$ V`

**🟨 Mineur**
- **Ex. 2** [etancheite] — L'énoncé de l'exercice 2 (visible dans la variante énoncés) révèle « le champ de 782 panneaux de l'exercice précédent », soit la réponse de la question 1 de l'exercice 1.  
  Passage : `On reprend le champ de 782 panneaux de l'exercice pr\'ec\'edent`
- **Ex. 6** [structure] — Gradation des difficultés incohérente : 2,2,3,2,3,1 — l'unique exercice de niveau 1 clôt la banque au lieu de l'ouvrir ; progression non croissante.  
  Passage : `Exercice 6 -- \difficulte{1}`
- **Ex. 4** [forme] — Unité « jour » non déclarée dans siunitx (aucun \DeclareSIUnit dans preamble.tex) : \SI{3200}{\kilo\watt\hour\per jour} (l.206, 217) bascule en mode littéral, rendu non maîtrisé ; il faudrait déclarer \jour ou écrire l'unité hors \SI.  
  Passage : `\SI{3200}{\kilo\watt\hour\per jour}`
- **Ex. 1, 4** [forme] — Nombres ≥ 4 chiffres sans séparateur \, en math brut hors \SI : 600/1000 (l.84), 1000\times 9{,}81 (l.213), \frac{4003}{3200} (l.216) — la règle du projet impose 1\,000, 4\,003, 3\,200.  
  Passage : `\frac{E_{jour}}{E_c} = \frac{4003}{3200} \approx 1{,}25`
- **Ex. 3** [source] — Citation jury 2025 en guillemets légèrement réécrite par rapport au verbatim (Rapport_Jury_2025 l.331 : « et du calcul de P. Une boucle... le point de la puissance maximum (dP = 0) ») : mots modifiés (« et le calcul », « point de puissance maximum ») et fin tronquée, tout en étant présentée comme citation directe.  
  Passage : `\guillemotleft\ la strat\'egie de commande est bas\'ee sur la mesure de $U$ et $I$ et le calcul de $P$...`

*Non vérifié par l'agent : Rendu visuel des 5 schémas TikZ/circuitikz (audit statique sans recompilation, topologies vérifiées sur le code source uniquement) ; comportement exact de siunitx face à l'unité non déclarée « jour » (la compilation passe, rendu incertain) ; intitulé exact de l'épreuve E2 2021 (« Étude d'un système ») non recoupé contre la page de garde du sujet*


### T17 — Distribution / sécurité (79/100) — `exercices/T17_exercices.tex`

Structure 24/30 · Exactitude 33/35 · Pédagogie 9/15 · Forme 9/10 · Sources 4/10 — 6 exercices

**Sources vérifiées** : ex1: 2021 Q19 — mention « SLT de type TT » retrouvée (E2_Sujet_2021.md l.237) mais la Q19 réelle est un schéma DR1/DR2 (attribution approximative) ; ex2: 2024 B5-B9 OK (E2_Disciplinaire_IE_2024.md : L=850 m, Itot=258 A, cosφ=0,85, B9 conformité NFC 15-100) et citation Rapport_Jury_2024 B9 vérifiée mot pour mot, MAIS Ru/Xu introuvables (DT2 image) et contredits par la fiche T17 (0,0424/0,0902 mΩ/m), épreuve mal nommée ; ex3: annoncé « adapté » — spa 2017 OK (Partie B, B2.2/B2.3, cosφ 0,86 des pompes hydro retrouvé ; 0,80 pompe circulation non retrouvé dans le texte, plausiblement en DT) ; ex4: inédit — principe MA validé (Rapport_Jury_2021 Q17 : NSX250N MA, Icu, Irm=2860 A) mais citation jury guillemetée FABRIQUÉE (introuvable 2021 et 2024) ; ex5: 2018 DRS7 OK (tableau compatibilité TT/TN-S/TN-C/IT modes MC/MD, E2_Sujet_2018.md l.806-816) mais installation réelle en TT, pas TN-C ; ex6: sélectivité 300/30 mA attribuée à 2021 Q19 INTROUVABLE (sujet et rapport)

**🟥 Bloquant**
- **Ex. 4** [source] **[CONFIRMÉ]** — Citation guillemetée attribuée aux rapports de jury 2021 et 2024, introuvable verbatim dans Rapport_Jury_2021.md et Rapport_Jury_2024.md (grep « impératif », « justifier le choix du disjoncteur » : aucun hit correspondant). Le principe est réel (rapport 2021 Q17 : NSX250N MA, Icu, Irm=2860 A, protection thermique par le variateur), mais la phrase citée est fabriquée et présentée comme authentique.  
  Passage : `\guillemotleft\ il est imp\'eratif de justifier le choix du disjoncteur en citant le pouvoir de coupure...`

**🟧 Majeur**
- **Ex. 2** [source] **[CONFIRMÉ]** — Ru = 0,225 Ω/km et Xu = 0,08 Ω/km présentés comme données du sujet 2024 (B5-B9) : introuvables dans les .md (DT2 en image omise), et la fiche T17_Distribution_Securite.tex traite la même question source avec Ru = 0,0424 mΩ/m et Xu = 0,0902 mΩ/m (ΔU ≈ 31,7 V soit ~7,9 %, vs 22,1 % ici). L'une des deux séries de valeurs déforme le sujet réel ; le résultat 22,1 % ne correspond probablement pas au corrigé officiel.  
  Passage : `r\'esistance lin\'eique $R_u = \SI{0,225}{\ohm\per\kilo\meter}$ et une r\'eactance $X_u = \SI{0,08}`
- **Ex. 6** [source] **[CONFIRMÉ]** — La configuration 300 mA en tête / 30 mA par départ et la sélectivité différentielle sont attribuées à la question 19 du sujet 2021 : introuvables dans E2_Sujet_2021.md (Q19 réelle = compléter les schémas de puissance et de commande du variateur, DR1/DR2) ni dans Rapport_Jury_2021.md (aucun hit « mA », « différentiel », « sélectivité »). L'attribution repose sur T17_contenu.md, lui-même non sourcé sur ce point.  
  Passage : `2021, \'Etude d'un syst\`eme, question 19 (NF C 15-100)`
- **Ex. 4** [structure] — Aucun encadré docTech dans la notion (nb_docTech = 0) alors que T17 (distribution, choix de protections sur références constructeur) s'y prête pleinement : la table constructeur de l'exercice 4 aurait dû être un docTech avec une première question d'extraction ; sa question 1 est une question de cours, pas d'extraction.  
  Passage : `\emph{Table constructeur (extrait, disjoncteurs \`a d\'eclencheur magn\'etique seul...`
- **Ex. 1, 2, 5, 6** [pedagogie] — Recouvrement quasi identique de 4 exercices sur 6 avec les Questions Types de la fiche T17 : ex. 1 ≈ Q1 (SLT TT + DDR 30 mA), ex. 2 ≈ QT chute de tension (mêmes 258 A / 850 m / cosφ 0,85 / conclusion NF C 15-100), ex. 5 ≈ Q5 (TN-C mode commun seul), ex. 6 ≈ Q6 (300/30 mA, rapport ≥ 3). Très faible valeur ajoutée d'entraînement par rapport à la fiche.  
  Passage : `Exercice 1 -- ... SLT ... DDR / Exercice 2 -- ... chute de tension / Exercice 5 -- TN-C / Exercice 6 -- s\'electivit\'e`

**🟨 Mineur**
- **Ex. 2** [source] — Épreuve mal nommée : les questions B5-B9 (850 m, Itot = 258 A, cosφ 0,85, conformité NF C 15-100) sont dans E2_Disciplinaire_IE_2024.md (épreuve disciplinaire IE), pas dans l'épreuve « disciplinaire appliquée » (E2_Appliquee_Commune_2024, questions 40-43). Le commentaire d'en-tête du fichier dit de plus « E1_Sujet_2024 », également faux. La citation jury B9, elle, est vérifiée mot pour mot.  
  Passage : `2024, \'Epreuve \'ecrite disciplinaire appliqu\'ee, questions B5 \`a B9`
- **Ex. 1** [source] — La question 19 réelle du sujet 2021 demande de compléter les schémas de puissance et de commande (DR1/DR2) ; seule la phrase « le schéma des liaisons à la terre est de type TT » figure dans le préambule adjacent. L'exercice (nommer le SLT, justifier le DDR) est une adaptation non signalée comme telle (contrairement à l'ex. 3 qui dit « adapté de »).  
  Passage : `2021, \'Etude d'un syst\`eme, question 19`
- **Ex. 5** [source] — Le sujet 2018 précise « schéma de liaison à la terre de l'installation de type TT » ; le cas TN-C n'est qu'une colonne du tableau de compatibilité du DRS7. La transposition en installation TN-C n'est pas signalée (« adapté de » absent) ; dénomination « Épreuve disciplinaire » anachronique pour 2018 (idem ex. 3 pour 2017, terminologie post-réforme 2022).  
  Passage : `Une installation industrielle est raccord\'ee en r\'egime \textbf{TN-C}`
- **Ex. 2** [schema] — Le schéma circuitikz place la tension composée U_D (400 V) comme source directe d'une maille monophasée contenant l'impédance d'un seul conducteur de ligne : modèle incohérent (il faudrait la tension simple V = U_D/√3, le √3 étant ensuite porté par la formule). Illustratif mais physiquement approximatif.  
  Passage : `to[sV, l=$U_D$] (0,2.2) to[R, l=$R_u\!\cdot\! L$]`
- **Ex. 5** [structure] — Gradation non progressive : la séquence des difficultés est 1, 2, 2, 3, 1, 2 — un exercice de niveau 1 arrive après le niveau 3. Niveaux 1 et 3 bien présents par ailleurs.  
  Passage : `Exercice 5 -- \difficulte{1}`
- **Ex. 1, 5** [pedagogie] — Les corrigés des exercices 1 et 5 ne se terminent pas par une phrase de conclusion explicite reliant le résultat à une exigence ou un critère (règle du gabarit) ; les ex. 2, 3, 4 et 6 la respectent.  
  Passage : `...ind\'ependamment de la valeur des r\'esistances de terre. / ...sans \^etre d\'etect\'e comme diff\'erentiel).`
- **Ex. 3** [forme] — Nombres de 4 chiffres sans séparateur de milliers (3000, 1500, 3938) dans du contenu mathématique rendu, contraire à la règle 17\,689 du gabarit. Les décimales à point détectées par la pré-passe sont toutes dans des options TikZ/leftmargin (légitimes).  
  Passage : `\frac{3000}{230\times 1} ... \frac{1500}{230\times 0{,}86} ... \SI{3938}{\volt\ampere}`

*Non vérifié par l'agent : Valeurs linéiques Ru/Xu du DT2 du sujet 2024 et contenu des DT11-DT15 du sujet 2021 (tableaux/figures convertis en images omises dans les .md Marker) — impossible de trancher lesquelles des valeurs (0,225/0,08 Ω/km ou 0,0424/0,0902 mΩ/m) sont celles du sujet réel, ni de confirmer/infirmer définitivement la présence du 300/30 mA dans les DT 2021 ; cosφ 0,80 de la pompe de circulation 2017 (probablement en DT1/DT4, images) ; rendu visuel des PDF compilés (audit sans compilation, conformément à la consigne).*


### T18 — Composants électroniques (83/100) — `exercices/T18_exercices.tex`

Structure 24/30 · Exactitude 30/35 · Pédagogie 11/15 · Forme 8/10 · Sources 10/10 — 6 exercices

**Sources vérifiées** : ex1: 2022 E2_Disciplinaire_IE Q27 OK (E2_Disciplinaire_IE_2022.md l.475 : « la diode D1 est nécessaire pour protéger en tension l'entrée analogique du CAN » ; Vref=3,5 V l.455, seuil 0,6 V l.453 — valeurs conformes) ; ex2: inédit ; ex3: 2025 E2_Disciplinaire_IE Q24–Q27 OK (Q24 viabilité états Q1/D1 l.286, Q27 iL1 sur ]0;αT] et ]αT;T] l.318 — contexte pile à combustible/CV3/batterie conforme) ; ex4: 2013 E1_Sujet_commun_SII Q48 OK (l.531 : rôle onduleur PV, type de commande des transistors, « 24 onduleurs EI3300 ») ; ex5: inédit ; ex6: inédit (formule ⟨uS⟩=Vm(1+cosα)/2π redémontrée, dérivation vérifiée exacte)

**🟧 Majeur**
- **Ex. 3** [schema] — Diode de roue libre dessinée dans le mauvais sens : le chemin circuitikz va du nœud (3,4) vers la masse (3,0), donc anode au nœud et cathode à la masse. Avec cette orientation, D1 conduirait dès que Q1 est fermé (nœud à V_DC) et court-circuiterait la source — en contradiction directe avec le corrigé (« D1 voit alors une tension inverse et reste naturellement bloquée »). Pour la roue libre d'un Buck, la diode doit être tracée de (3,0) vers (3,4) (cathode au nœud).  
  Passage : `(3,4) to[empty diode, l=$D_1$] (3,0)`
- **Ex. toutes** [structure] — Aucun exercice « lecture de document technique » avec encadré docTech et question d'extraction, alors que la notion s'y prête : les datasheets de diodes/transistors (courants directs max, V_CE de claquage, caractéristiques statiques) sont des documents techniques canoniques, et les sujets sources exploités s'appuient eux-mêmes sur des DT (DT D3/D4 en 2022, DT10 en 2025).  
  Passage : `nb_docTech: 0 (pré-passe)`

**🟨 Mineur**
- **Ex. 4 q.2** [pedagogie] — La réponse à la question 2 (« Quel type de commande est utilisé pour les transistors de puissance ? ») figure textuellement dans l'énoncé deux paragraphes plus haut. Seule la partie « pourquoi préféré à pleine onde » reste réellement une question.  
  Passage : `La commande des transistors de puissance est de type MLI (modulation de largeur d'impulsion).`
- **Ex. 4** [structure] — Gradation non monotone : l'exercice 4 est de niveau 1 après deux exercices de niveau 2. Les bornes exigées (au moins un niveau 1 et un niveau 3) sont respectées, mais la progression est brisée en milieu de banque.  
  Passage : `difficultes: 1,2,2,1,2,3`
- **Ex. 2** [pedagogie] — Corrigé en 2 items pour 3 questions d'énoncé : la réponse à la question 2 (tracé + lecture graphique) est fusionnée dans l'item 1 du corrigé, ce qui désaligne la numérotation énoncé/corrigé.  
  Passage : `Graphiquement, l'intersection $Q$ [...] se situe vers $V_{AK,Q}$`
- **Ex. 1** [pedagogie] — Pas de phrase de conclusion reliant le résultat V_CAN,max = 4,1 V à une exigence (par ex. tension maximale admissible sur l'entrée analogique du PIC) : le corrigé s'achève sur l'explication de R_lim sans boucler sur le critère de protection.  
  Passage : `$R_{lim}$ borne ce courant \`a $(V_e - V_{CAN,max})/R_{lim}$ lorsque $D_1$ \'ecr\^ete.`
- **Ex. 1 et 3** [pedagogie] — Recouvrement partiel avec les Questions Types de la fiche T18 : l'exercice 1 reprend exactement la même source que QT3 (2022 E2 Q27, diode de protection CAN) et l'exercice 3 recouvre QT1 (hacheur 2025 E2 Q27). Les exercices vont plus loin (calculs de V_CAN,max, viabilité des états, E_b = αV_DC), mais le doublon de sources réduit la valeur ajoutée de la banque.  
  Passage : `QT3 - Diode de protection - entr\'ee analogique d'un CAN (E2 appl. 2022 Q27)`
- **Ex. 5** [forme] — Nombre de 4 chiffres sans séparateur de milliers dans du contenu mathématique rendu (détection pré-passe ligne 263). *(affiché : 2200 — recalcul : 2\,200 attendu (règle des milliers))*  
  Passage : `\dfrac{5-0{,}6}{2200}`
- **Ex. 4** [forme] — Valeur avec unité composée à la main ($230\,\si{\volt}$) au lieu de \SI{230}{\volt}, incohérent avec le reste du fichier qui utilise \SI partout.  
  Passage : `node[above]{$230\,\si{\volt}$, $\SI{50}{\hertz}$}`

*Non vérifié par l'agent : Rendu PDF non inspecté visuellement (audit sur source + pré-passe) : polarités des sources V/battery2 circuitikz des ex.1 et 3 non contrôlées au rendu ; annexe 11 du sujet 2013 non retrouvée pour confirmer que « MLI » y est bien la réponse attendue ; document DT10 (schéma exact du hacheur 2025) non comparé figure à figure au schéma de l'ex.3.*


### T19 — AOP (79/100) — `exercices/T19_exercices.tex`

Structure 26/30 · Exactitude 24/35 · Pédagogie 10/15 · Forme 9/10 · Sources 10/10 — 6 exercices

**Sources vérifiées** : ex1: 2024 partie E q.E1-E3 OK (E1_Sujet_2024.md l.724-745 : G2=-100, G3=-1, R2=834,4 Ω ; Rapport_Jury_2024 l.439-441 confirme G1=3,397≈3,4 et V3=340·eAB) ; ex2: 2024 q.E4-E5 OK (Millman V+=(V3+Ve)/2, V-=V4/2, l.754) ; ex3: 2024 q.E8-E10 OK (R5=250 Ω l.779, Is pour V4=1 et 5 V l.783, circuit simplifié par rapport à la figure 24 mais résultats conformes) ; ex4: 2023 q.F6-F9 OK (E2_Disciplinaire_IE_2023.md l.571-599 : Bakus, Vref2=2,42 V, ALI 15 V, R1=1 kΩ, R2=150 kΩ ; jury F10 : seuils 2,5/2,3 V conformes au corrigé — mais schéma de l'exercice inversé, cf. constats) ; ex5: 2026 E2_Sujet_2026_BAC3 q.B2-B5 OK (Jumo l.338, I=10 mA fig. B2 l.384, RT=R0(1+aT) l.362, suiveur/vT=U0(1+aT) q.B4 l.389-391 ; R0=100 Ω et a=3,85e-3 annoncés comme valeurs typiques, non attribués au sujet) ; ex6: inédit, rien à vérifier.

**🟧 Majeur**
- **Ex. 4** [schema] — Schéma circuitikz avec R1/R2 intervertis par rapport au sujet 2023 et au corrigé : le schéma place R2 en série avec Vref2 et R1 en rebouclage de Vs2, alors que la formule démontrée V+=(R2·Vref2+R1·Vs2)/(R1+R2) et les seuils officiels (jury F10 : 2,5/2,3 V) exigent Vref2 via R1 (1 kΩ) et rebouclage via R2 (150 kΩ). Avec le circuit tel que dessiné, V_H vaudrait ≈14,9 V.  
  Passage : `\draw (P) to[R, l=$R_2$] ++(-2.5,0) node[left]{$V_{ref2}$}; ... (S) to[R, l=$R_1$] ++(0,2)`
- **Ex. 4 q.2** [calcul] **[CONFIRMÉ]** — Ligne de Millman du corrigé algébriquement incohérente : la fraction écrite (Vref2/R2 + Vs2/R1)/(1/R1+1/R2) se réduit à (R1·Vref2+R2·Vs2)/(R1+R2), et non au résultat affiché (R2·Vref2+R1·Vs2)/(R1+R2). Le résultat final et les seuils numériques (2,50/2,30 V) sont pourtant les bons (conformes au rapport jury 2023) — seule la dérivation intermédiaire suit le schéma inversé. *(affiché : (R2·Vref2 + R1·Vs2)/(R1+R2) — recalcul : la fraction telle qu'écrite donne (R1·Vref2 + R2·Vs2)/(R1+R2) = (1000×2,42 + 150000×15)/151000 ≈ 14,92 V)*  
  Passage : `V_+ = \dfrac{\dfrac{V_{ref2}}{R_2} + \dfrac{V_{s2}}{R_1}}{\dfrac{1}{R_1}+\dfrac{1}{R_2}} = \dfrac{R_2\,V_{ref2} + R_1\,V_{s2}}{R_1+R_2}`
- **Ex. 1, 3, 4** [pedagogie] — Recouvrement quasi identique avec les 3 Questions Types de la fiche T19_AOP.tex : Ex1 ≡ QT1 (mêmes données 2024 : R2=834,4 Ω, G1≈3,4, G2=-100, G3=-1, gain global 340), Ex3 ≡ QT3 (R5=250 Ω, V4∈[1;5] V, Is=4/20 mA), Ex4 ≡ QT2 (2,42 V, 15 V, 1 kΩ/150 kΩ, mêmes seuils). 3 exercices sur 6 dupliquent la fiche avec les mêmes valeurs et résultats ; seules quelques questions de dérivation sont ajoutées.  
  Passage : `fiche QT1 : "\frac{2 \times 1000 + 834{,}4}{834{,}4} \approx \mathbf{3{,}4}" — identique à l'ex.1`

**🟨 Mineur**
- **Ex. 4 q.3** [calcul] — Arrondi erroné du seuil haut : 378 000/151 000 = 2,5033 V, arrondi correct 2,503 V, le corrigé affiche 2,504 V (la valeur 2,50 V reprise en q.4 est, elle, correcte). *(affiché : 2,504 V — recalcul : 378000/151000 = 2,50331 ≈ 2,503 V)*  
  Passage : `\dfrac{363\,000+15\,000}{151\,000} \approx \SI{2,504}{\volt}`
- **Ex. 3 q.2** [pedagogie] — Phrase du corrigé auto-contradictoire : Is est défini dans l'énoncé comme "le courant qui traverse R_ana", mais le corrigé affirme que l'expression ne fait pas intervenir "le courant qui circule effectivement dans R_ana".  
  Passage : `ne fait intervenir ni $R_{ana}$, ni le courant qui circule effectivement dans $R_{ana}$`
- **Ex. 2, 5** [pedagogie] — Corrigés sans phrase de conclusion finale reliant le résultat à une exigence/un critère (règle du gabarit) : l'ex.2 se termine sur V4=V3'+Ve, l'ex.5 sur la valeur 1,35 V, sans lien avec la chaîne de mesure ou le cahier des charges.  
  Passage : `\dfrac{V_3'+V_e}{2} = \dfrac{V_4}{2} \quad\Longrightarrow\quad V_4 = V_3' + V_e`
- **Ex. 5** [structure] — Gradation non monotone : suite de difficultés 1,2,2,3,1,2 — l'exercice 5 (niveau 1, suiveur) arrive après le niveau 3 (ex.4). Les niveaux 1 et 3 sont bien présents.  
  Passage : `Exercice 5 -- \difficulte{1} ... 2026, \'epreuve BAC3`
- **Ex. 5** [structure] — Aucun encadré docTech (nb_docTech=0) alors que l'ex.5 est tiré d'une partie de sujet fondée sur un document technique (DTB2 Jumo, questions B2-B3 d'extraction) : un exercice de lecture de datasheet (R0, a, classe de la sonde) était naturel ici. Notion majoritairement analytique, d'où gravité mineure.  
  Passage : `Sachant que $R_0 = \SI{100}{\ohm}$ et $a = \SI{3,85e-3}{\per\kelvin}$ (valeurs typiques`
- **Ex. 1, 4** [forme] — Nombres ≥ 4 chiffres sans séparateur \, dans du contenu mathématique : "1000", "2834{,}4" (ex.1 l.72) et "1000" (ex.4 l.190/192) alors que 150\,000 et 363\,000 sont correctement séparés dans les mêmes formules.  
  Passage : `G_1 = \dfrac{2\times 1000 + 834{,}4}{834{,}4} = \dfrac{2834{,}4}{834{,}4}`

*Non vérifié par l'agent : Rendu visuel des PDF (aucune compilation ni inspection graphique, conformément à la consigne) ; figure 23 exacte du sujet 2023 (image OCR omise — l'orientation R1/R2 est déduite du corrigé jury F6/F10, pas d'une lecture directe de la figure) ; contenu du document technique DTB2 du sujet 2026 (valeurs R0/a non confrontées au DT, mais l'exercice ne les attribue pas au sujet).*


---

## 5. Note de méthode — ce qui est vérifié, ce qui mérite une relecture humaine

**Vérifié par double passe indépendante (fiabilité forte)** :
- les **15 erreurs de calcul** du §3.1 : recalculées une première fois par l'agent d'audit puis une
  seconde fois, from scratch et à charge de réfutation, par un agent indépendant qui repartait des
  seules données d'énoncé — les deux recalculs concordent dans les 15 cas ;
- les **15 problèmes de source** du §3.2 : recherche initiale + seconde recherche indépendante
  multi-mots-clés (variantes orthographiques/OCR, années voisines) avant confirmation ;
- la **compilation** : 38 exécutions `pdflatex` réelles (pré-passe scriptée), pas d'inférence ;
- les détections mécaniques de forme (pré-passe grep) : exhaustives sur leurs motifs, puis filtrées
  des faux positifs par les agents (coordonnées TikZ, `\mathrm{d}`, numéros de normes, années).

**Vérifié en simple passe (fiabilité normale d'audit)** :
- les constats **mineurs** de calcul (arrondis T01 ex. 1, T02 ex. 1, T09 ex. 2, T12 ex. 5 q.2,
  T19 ex. 4 q.3…) n'ont pas été contre-vérifiés adversarialement (protocole réservé aux
  majeurs/bloquants) ;
- les constats structure/pédagogie/schéma et les recouvrements fiche/exercice (appréciation d'un seul
  agent, mais appuyée sur des greps ciblés des fiches).

**Deux constats initialement signalés ont été réfutés** en contre-vérification et sont **exclus** des
listes consolidées (détail §3.3) : T11 ex. 5 q.3 (le C_th ≈ 557 N·m est bien reconstructible depuis les
données publiées du sujet 2019) et T15 ex. 3 sur le DoD (la lecture de l'auditeur est contredite par le
sujet source lui-même ; reste le point distinct, confirmé, des « 80 km » inventés).

**Mérite une dernière relecture humaine avant toute correction** :
1. **T17 ex. 2 (Ru/Xu)** : le DT2 du sujet 2024 est une image absente des conversions Markdown — les
   agents n'ont pas pu trancher entre les valeurs de l'exercice (0,225 Ω/km) et celles de la fiche T17
   (0,0424 mΩ/m) ; vérifier sur le **PDF original** (`06_PDFs_Originaux/2024/`).
2. **Les 8 schémas signalés faux** (§2.6) : confirmés sur le code TikZ/circuitikz, mais aucun rendu
   PNG n'a été produit pendant l'audit — un contrôle visuel des pages concernées est recommandé pour
   écarter tout faux positif de lecture de code (et il révélera peut-être d'autres défauts purement
   visuels, invisibles dans la source).
3. **T09/T14 (THD 61,4 % vs 59 %)** : la « bonne » valeur retenue ici (61,4 %) est celle de l'audit des
   fiches 2026-08 ; le rapport de jury 2024 affiche lui-même 0,59 — décision éditoriale à confirmer
   (suivre le calcul exact, en le signalant, plutôt que le rapport).
4. Les attributions jury déclarées fabriquées (§3.2) l'ont été après **deux** recherches négatives dans
   les `Rapport_Jury_*.md` convertis ; une absence dans la conversion Markdown n'est pas une preuve
   absolue d'absence dans le PDF (tableaux/images non convertis) — sondage recommandé sur 2-3 cas dans
   les PDF originaux avant suppression en masse.

**Limites de périmètre** : notions T20–T30 non générées donc non auditées ; rendu visuel des PDF non
contrôlé (voir ci-dessus) ; le recouvrement fiche/exercice a été évalué par grep ciblé, pas par
comparaison exhaustive des 30 fiches.
