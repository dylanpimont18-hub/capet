# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projet

Base documentaire pour la préparation au **CAPET SII option Ingénierie Électrique**, session 2026. Contient les PDFs officiels (sujets, corrigés, rapports jury 2013–2026) et leur conversion Markdown via l'outil Marker.

## Structure des fichiers

```
colab_convert_pdfs.py                          — script Google Colab : PDF → Markdown (Marker)
PDFs_CAPET_SII_IE.zip                          — archive source de tous les PDFs

docs/CAPET_SII_IE/06_PDFs_Originaux/{année}/  — PDFs organisés par année (2013–2026)
    ├── E1_Sujet_{année}/                      — épreuve commune (sujet)
    ├── E1_Corrige_{année}/                    — épreuve commune (corrigé, si dispo)
    ├── E2_Sujet_{année}/  ou E2_Appliquee_Commune_{année}/
    ├── E2_Disciplinaire_IE_{année}/           — épreuve disciplinaire IE
    └── Rapport_Jury_{année}/

docs/CAPET_Markdown-{timestamp}/CAPET_Markdown/  — résultat du dernier batch Colab
    └── docs/CAPET_SII_IE/06_PDFs_Originaux/     — même arborescence, fichiers .md
```

## Workflow de conversion

1. Les PDFs sont archivés dans `PDFs_CAPET_SII_IE.zip` et organisés sous `06_PDFs_Originaux/`
2. `colab_convert_pdfs.py` tourne sur Google Colab (GPU), utilise Marker (fallback pymupdf4llm)
3. Le résultat est téléchargé depuis Google Drive et extrait sous `docs/CAPET_Markdown-{timestamp}/`
4. Les `.md` convertis peuvent ensuite être copiés/fusionnés dans `06_PDFs_Originaux/`

## État de la conversion (2026-06-29)

- 41 PDFs disponibles (2013–2026), + 1 le 2026-11-09 : `2026/Rapport_Jury_2026_3eConcours.pdf`
- 26 fichiers `.md` déjà dans `06_PDFs_Originaux/` (2013–2023 partiels)
- 41 fichiers `.md` dans le dernier batch Colab (couverture complète 2013–2026), + 1 le
  2026-11-09 : `2026/Rapport_Jury_2026_3eConcours/…md` (extraction PyMuPDF, pas Marker)

## Sessions de révision de 2 h (`docs/CAPET_SII_IE/09_Sessions_2h/`)

Créé le 2026-11-09 pour réviser l'admissibilité par blocs de 2 h imprimés (extrait de sujet +
documents réponses + corrigé séparé).

- `PROMPT_SESSIONS_2H.md` — prompt et cahier des charges à coller dans une **autre**
  conversation, qui génère les packs à imprimer à partir des PDF fournis
- `catalogue/{année}_{support}.md` — décorticage d'un sujet : pages PDF de chaque partie, des
  DT et des DR, thèmes T01–T30, pages du corrigé officiel, correspondance de numérotation,
  constats du jury avec numéros de ligne. Seul `2026_Hycity.md` existe pour l'instant.
- `packs/` — 15 sessions prêtes à imprimer (S01–S15), toutes avec corrigé **officiel** (E1 2026
  + épreuves disciplinaires IE 2022–2025, désormais entièrement utilisées ; reste l'E2 2026,
  sans corrigé officiel). Données dans `sessions.py`, génération par
  `build_packs.py` vers `packs/pdf/` (ignoré par git). Les fichiers `E1_Sujet_2023/2024/2025.pdf`
  sont des **doublons** de `E2_Disciplinaire_IE_{année}.pdf` (md5 identiques) : c'est l'épreuve
  disciplinaire IE de 5 h, corrigée dans `Rapport_Jury_{année}`.

## Couverture du référentiel (audit du 2026-11-09)

`docs/CAPET_SII_IE/AUDIT_REFERENTIEL_2026-11-09.md` : sur 89 éléments du référentiel, 45 couverts,
24 partiels, 20 absents au 2026-11-09. **Comblé le 2026-11-10** : trois fiches nouvelles (T31
télécoms et RF, T32 ingénierie système et SysML, T33 informatique embarquée et réseaux) et des
compléments dans 13 fiches (T05, T06, T07, T08, T12, T16, T17, T19, T20, T22, T27, T29, T30).
Restent hors système : les exercices de ces notions et leur intégration au manuel `manuel/`.

**Présence des fiches T31–T33** : nombre d'années 2013–2025 où un sujet *mentionne* la notion
(mots-clés, termes ambigus exclus : « porteuse » désigne aussi la porteuse de MLI, « programme »
le programme du concours). Ce n'est pas un nombre de questions. Leurs questions types inédites
(T31 QT2–QT3, T32 QT3) sont marquées comme telles.

## Fiches de révision LaTeX (`fiches/`)

33 fiches thématiques : T01–T30 construites sur les sujets 2013–2025, T31–T33 ajoutées le
2026-11-10 pour couvrir le reste du référentiel.

```
fiches/
  preamble.tex                  — packages, couleurs, styles tcolorbox communs
  main.tex                      — point d'entrée pour compiler une ou plusieurs fiches
  TEMPLATE_FICHE.md             — spécifications structurelles pour la génération des fiches
  T{nn}_{Titre}.tex             — fiche compilable autonome (pdflatex)
  T{nn}_contenu.md              — contenu documentaire source (formules, QT, citations jury)
```

### Domaines et couleurs

| Domaine | Couleur LaTeX | Fiches |
|---|---|---|
| Électrotechnique | `colElec` (bleu) | T01–T17 |
| Électronique | `colElec` | T18–T25, T31 (télécoms et RF), T33 (informatique embarquée) |
| Automatique | `colAuto` (vert) | T26–T29, T32 (ingénierie système) |
| Mécanique | `colMeca` (orange) | T10 |
| Thermique | `colTherm` (rouge) | T05 |

### Refonte visuelle 2026 (direction « moderne coloré », appliquée le 2026-08-25)

Style validé sur pilote T02 (3 variantes comparées), déployé sur les 30 fiches. Tout est
centralisé dans `preamble.tex` :

- **Polices** : Lato (`lato` avec `[default]`) + maths sans-serif assorties (`newtxsf`),
  chargées après `lmodern`. S'applique aussi à `exercices/` (préambule partagé).
- **Palette vivifiée** : `colElec` RGB 29,78,216 · `colAuto` 21,128,61 · `colMeca` 194,65,12 ·
  `colTherm` 185,28,28 + encres `colInk`/`colSlate`/`colRule` (texte courant = `colInk`
  via `\AtBeginDocument{\color{colInk}}`).
- **Boîtes** : plus de double cadre. `ficheSection` = bandeau titre coloré arrondi + fond
  à 4 % ; `questiontype` = carte blanche, bandeau `colElec!78!black` (uniforme, tous
  domaines), liseré très clair ; `jury` = bandeau ambre `colJuryFrame`, fond crème ;
  bloc 5 « Présence » = `ficheSection=colPresence` (ardoise).
- **Macros communes** (remplacent le code dupliqué dans chaque fiche) :
  - `\ficheHeaders{code}{titre court}{couleur}` — en-tête/pied fancyhdr
  - `\ficheEntete{code}{titre}{couleur}{domaine}{ligne présence}{sous-thèmes}` — BLOC 0
    (bandeau dégradé) ; les 30 fiches les utilisent, ne pas réintroduire de tcolorbox
    d'en-tête codée en dur.

### Structure d'une fiche (5 blocs obligatoires)

1. **BLOC 0** — En-tête (tcolorbox fond coloré : code + domaine + présence + sous-thèmes)
2. **BLOC 1** — Rappels de cours (sous-sections 1.1, 1.2… + tableaux booktabs + TikZ si applicable)
3. **BLOC 2** — Formulaire synthétique (2 colonnes `multicols`, 8–16 formules)
4. **BLOC 3** — Questions types (2–3 QT issues de sujets réels, avec `\tcbline` énoncé/corrigé)
5. **BLOC 4** — Attentes du jury (6–8 points + citation directe rapport jury)
6. **BLOC 5** — Tableau de présence dans les sujets 2013–2025

### Règles LaTeX critiques

- **Jamais** `\newpage`, `\clearpage`, `\pagebreak` — laisser LaTeX gérer
- Toutes les tcolorbox ont l'option `breakable`
- Décimales françaises : `0{,}85` (jamais `0.85`)
- Unités via `siunitx` : `\SI{230}{\volt}`, `\si{\ohm}`
- Vecteurs complexes : `\underline{Z}`, pas `\vec{Z}`

### Workflow de compilation

```bash
cd fiches/
# Compiler une fiche autonome :
pdflatex T01_Grandeurs_Electrocinetique.tex
# Compiler via main.tex (inclure la/les fiches souhaitées dans main.tex) :
pdflatex main.tex
```

### État des fiches (2026-08-24)

- **Audit qualité complet** : `fiches/AUDIT_FICHES_2026.md` (2026-08-24, score moyen initial 78/100,
  recalcul indépendant de toutes les AN, vérification des citations jury contre les rapports sources).
- **Correction post-audit appliquée** (workflow multi-agent, 2026-08-24) : les 30 fiches corrigées et
  recompilées, 29/30 validées par une passe de vérification indépendante. Détail complet dans
  `fiches/CORRECTIONS_APPLIQUEES_2026.md`. Corrections transversales : encadré générique
  « Procédure type copie concours » supprimé du Bloc 3 des 30 fiches, tous les couples Bloc 0/Bloc 5
  resynchronisés par recomptage, tous les en-têtes `\fancyhead[L]` < 35 caractères, citations jury de
  T06/T07/T08/T15 remplacées par les verbatims exacts des rapports (ou dé-guillemetées). Erreurs de
  formules/calculs de l'audit (§2.7) toutes corrigées (f_P redresseurs, PI numérique T27, trame CAN
  108 bits T24/T25, THD 61,4 % T09/T14, CAN 8 bits T22/T30, hacheur abaisseur T16, etc.).
- **⚠ Reste 1 point en relecture humaine : T15 QT2** (données d'énoncé 4,06 W·h / 70 % à remplacer
  par les valeurs officielles 4,64 W·h / 0,8 du Rapport_Jury_2020 — voir la dernière section de
  `CORRECTIONS_APPLIQUEES_2026.md`, correction proposée prête).

### Historique (2026-07-30)

- 30 fichiers `T{nn}_contenu.md` (T01–T30) — contenu documentaire complet
- 30 fichiers `.tex` générés (T01–T30), tous compilés en PDF, tous vérifiés visuellement (rendu PNG)
- **Défaut historique, corrigé** : la quasi-totalité des fiches (T01, T03–T30) avait été générée sans
  aucun accent français (texte ASCII : "theme", "Presence"...) et sans le schéma technique obligatoire
  du Bloc 1 (seul un flowchart méthode générique était présent, identique dans les 30 fiches — pas de
  diagramme de Bode, schéma-bloc, courbe couple-vitesse, etc. malgré la règle `TEMPLATE_FICHE.md`).
  Seule `T02_Puissance_AC.tex` était correcte dès l'origine.
  **Les 30 fiches (T01–T30) sont désormais corrigées** : accents restaurés, un schéma
  TikZ/circuitikz spécifique au domaine ajouté en Bloc 1, et chaque corrigé de Question Type se
  termine par une phrase de conclusion reliant le résultat numérique à une exigence/un critère
  (règle ajoutée dans `TEMPLATE_FICHE.md`).

## Banque d'exercices LaTeX (`exercices/`)

Exercices d'entraînement niveau CAPET, un fichier par notion, générés via le skill `exercices-capet`
(`.claude/skills/exercices-capet/SKILL.md`). Indépendant des fiches de cours (`fiches/`).

```
exercices/
  main.tex                 — point d'entrée (titlepage + \include des notions traitées)
  T{nn}_exercices.tex      — source unique (4-6 exercices) d'une notion, compilable seul ou via main.tex
```

- Reprend le découpage `T01`–`T30` des fiches (pas de référentiel de notions séparé)
- Préambule partagé avec `fiches/` : `\input{../fiches/preamble}`
- Style dédié `exoBox` (couleur `colExo`, cyan) + macro `\difficulte{1|2|3}` dans `fiches/preamble.tex`,
  pour distinguer visuellement la banque d'exercices des fiches de cours
- **Énoncés et corrigés en 2 PDF distincts**, générés à partir de la **même** source `.tex` (pas de
  duplication de contenu) via une bascule de compilation :
  - chaque exercice est écrit `\CAPETSHOW{<énoncé>}{<corrigé>}` dans sa tcolorbox `exoBox`
    (macro définie dans `fiches/preamble.tex`)
  - compilation normale (`pdflatex -jobname=T{nn}_enonces T{nn}_exercices.tex`) → PDF énoncés seuls
  - compilation avec le drapeau corrigé (`pdflatex -jobname=T{nn}_corriges
    "\def\CAPETCORRIGE{1}\input{T{nn}_exercices.tex}"`) → PDF corrigés seuls
  - `main.tex` suit la même bascule (`main_enonces.pdf`/`main_corriges.pdf`) — le drapeau se propage
    aux notions incluses via `\include`
- Schémas de circuits via `circuitikz` (option `european`), chronogrammes via `tikz` nu — ajoutés
  systématiquement dès qu'un exercice porte sur un circuit ou un signal temporel
- Suivi : `FILE_EXERCICES.md` (file d'attente), `PROGRESSION_EXERCICES.md` (tableau de bord)

### Piège LaTeX : babel[french] casse circuitikz

`babel[french]` active à `\begin{document}` des raccourcis de ponctuation (`:;!?`) qui font échouer la
syntaxe `to[...]` de `circuitikz` (erreur `+ or - expected`). Corrigé une fois pour toutes dans
`fiches/preamble.tex` via `\AtBeginDocument{\shorthandoff{:;!?}}` — ne pas retirer cette ligne.

### État (2026-09-20)

- **30/30 notions traitées** (T01–T30), **171 exercices** au total, **60/60 PDF** compilés
  (énoncés + corrigés par notion), tous avec schéma circuitikz/chronogramme/diagramme.
- T20–T30 générées le 2026-09-20 (6 exercices chacune), chacune avec un exercice `docTech`
  et une passe d'inspection visuelle PNG. Cette inspection a rattrapé des défauts qui
  compilaient sans erreur : diagramme de Bode à pente fausse (T21), chronogramme UART sans
  paliers (T25), signes `−` de retour tronqués sur 4 schémas-blocs (T27), 5 défauts de
  formalisme GRAFCET (T29), montages écrasés (T23, T30).

### Couverture réelle du corpus — constats établis le 2026-09-20

Relevés vérifiés sur les 41 fichiers 2013–2026. À connaître avant d'écrire un exercice :

| Thème | Occurrences dans le corpus |
|---|---|
| GRAFCET | **2**, toutes deux dans un tableau de programme STI2D (2017) — jamais une question |
| « réceptivité » | **0** |
| Karnaugh, table de vérité, De Morgan, NAND | **0** |
| « incertitude », « classe de précision », « wattmètre » | **0** |
| FPGA, VHDL | **0** |

Conséquence : sur ces thèmes, **aucun exercice ne peut être sourcé** sur un sujet réel. Les
exercices correspondants sont inédits et marqués comme tels — ne jamais fabriquer une
référence de sujet pour combler. Le séquentiel réellement interrogé passe par le
**diagramme états-transitions** (2017, 2021) et le câblage/paramétrage d'automates (2022).

## ⚠ Citations de rapports de jury — règle absolue

**Audit de véracité du 2026-09-20** : sur **68 citations** de rapport de jury présentes dans les
30 fiches, **37 (54 %) étaient défectueuses**, dont **27 sans aucun support textuel** — inventées.
Deux étaient attribuées à un « Rapport jury 2026 » **qui n'existait pas** à la date de l'audit
(le rapport 2026 du troisième concours, paru en septembre 2026, ne les contient pas non plus).

### Corpus réel des rapports

**9 rapports** existent :

- **2018 à 2025** (concours externe), dans
  `docs/CAPET_Markdown-.../06_PDFs_Originaux/{AAAA}/Rapport_Jury_{AAAA}/Rapport_Jury_{AAAA}.md` ;
- **2026, troisième concours** (ajouté le 2026-11-09), dans
  `docs/CAPET_Markdown-.../06_PDFs_Originaux/2026/Rapport_Jury_2026_3eConcours/Rapport_Jury_2026_3eConcours.md`.

**Il n'existe aucun rapport 2013–2017, ni de rapport 2026 du concours externe.** Toute citation
attribuée à ces sources est fabriquée par construction.

Le rapport 2026 du troisième concours corrige et commente une épreuve écrite dont le sujet est
**celui de l'E1 externe 2026** (bus Hycity), mais avec 11 questions par partie au lieu de 10 :
la numérotation est **décalée** (table de correspondance dans
`docs/CAPET_SII_IE/09_Sessions_2h/catalogue/2026_Hycity.md`). Une citation « jury 2026 » doit
donc préciser « troisième concours » et donner le numéro de question **du rapport**. Il ne dit
rien de l'E2 externe 2026. Son `.md` est une extraction PyMuPDF : les équations du corrigé
(p. 7–21) y sont mal linéarisées, il faut les vérifier sur le PDF.

### Règle

Avant d'écrire une citation de jury : **vérifier le verbatim par grep dans le rapport de l'année
revendiquée**, et noter `fichier:ligne` en commentaire `%`. En cas d'absence, **omettre** — une
citation absente vaut infiniment mieux qu'une citation inventée. Ne jamais reformuler entre
guillemets, ne jamais prolonger une citation authentique par une phrase ajoutée.

### Correction appliquée le 2026-09-20 (27 cas sans support)

20 fiches corrigées : remplacement par un verbatim authentique quand il en existait un,
suppression de l'encadré sinon. **T11, T12 et T25 n'ont plus d'encadré jury** — leurs citations
étaient toutes fabriquées ; c'est le résultat correct. Chaque fiche modifiée porte un en-tête `%`
documentant le changement.

### ⚠ Reste non corrigé (décision utilisateur : ne traiter que les cas sans support)

- **8 citations « noyau authentique + ajout inventé »** : T03, T04, T19, T22, T23, T30 et deux
  autres. Le début est vérifiable, la fin est ajoutée — motif le plus insidieux, car le début
  crédibilise la suite.
- **2 années d'attribution fausses** : T02 (attribuée « 2019-2025 », source réelle RJ2021:451).
- **Trois motifs de dégradation** distincts de la fabrication : recollage de passages distants sans
  marque d'élision (T04, T13, T29) ; requalification d'un corrigé technique en commentaire de jury
  (T08, T09, T15, T16, T24) ; paraphrase entre guillemets (T21 l.320).

### Deux erreurs de calcul de `fiches/T25_Transmission_Numerique.tex` — CORRIGÉES le 2026-09-20

1. **QT2 (LoRa) réécrite.** Elle se réclamait de la question 29 du sujet E2 disciplinaire IE 2022
   mais inventait un énoncé à SF = 7, résolu par « débit de table × CR » → 4 376 bit/s. La question
   réelle (`E2_Disciplinaire_IE_2022.md` l.507) impose **SF = 12**, rappelé deux fois dans le sujet,
   et le corrigé officiel (`Rapport_Jury_2022.md` l.349) donne
   **Rb = SF·BP·CR/2^SF = 293 bit/s** (recalcul indépendant : 292,97 ; Ts = 32,768 ms).
   Le Bloc 1, le formulaire et le point 3 du Bloc 4 ont été harmonisés sur cette formule — ils
   propageaient tous la méthode erronée.
2. **Trame CAN : 108 → 111 bits** (5 emplacements). Le décompte des champs
   (1+11+1+2+4+64+16+2+7 = 108) est exact mais omet les **3 bits d'intermission**. Le sujet 2026
   (`E1_Sujet_2026.md` l.517, question D5) écrit « constituée de 111 bits ». La fiche explicite
   désormais la décomposition 108 + 3 plutôt que de trancher silencieusement, et signale que le
   bit-stuffing n'est jamais compté forfaitairement. QT3 : t_trame = 111 µs, marge 44,5 %.

## Manuel de révision imprimable (`manuel/`)

Assemblage entrelacé cours + exercices en un PDF unique destiné à l'impression, créé le 2026-09-20.

```
manuel/
  main.tex      — assemblage : couverture, sommaire, 4 parties, \subimport des sources, annexe
  parties.tex   — macro \CAPETPARTIE{numéro}{titre}{sous-titre}{couleur} (intercalaires)
```

Structure du PDF : couverture → sommaire → Partie I Électrotechnique (T01–T17) →
Partie II Électronique (T18–T25) → Partie III Automatique (T26–T29) →
Partie IV Mesurage (T30) → Annexe A corrigés.

Pour chaque notion : la fiche de cours, puis ses exercices (énoncés seuls). Tous les corrigés
sont regroupés en Annexe A, avec renvois croisés cliquables énoncé ↔ corrigé.

### Principes

- **Assemblage, pas duplication** : `manuel/main.tex` n'héberge aucun contenu. Chaque fiche et
  chaque banque d'exercices reste l'unique source, compilable seule exactement comme avant.
- `\subimport` (package `import`) permet aux sources incluses de conserver leurs `\input`
  relatifs (`\input{preamble}` côté fiches, `\input{../fiches/preamble}` côté exercices).
- **Les sauts de page vivent dans `manuel/`**, jamais dans `fiches/T*.tex` — la règle
  « aucun `\newpage`/`\clearpage` dans les fiches » reste entière.

### Mécanique des corrigés différés — `\CAPETSHOW` à trois modes

`fiches/preamble.tex` expose désormais trois comportements, sélectionnés par drapeau :

| Mode | Drapeau | Comportement |
|---|---|---|
| Énoncés | *(aucun)* | imprime l'énoncé — comportement historique inchangé |
| Corrigés | `\CAPETCORRIGE` | imprime le corrigé — comportement historique inchangé |
| Manuel | `\CAPETMANUEL` | imprime l'énoncé, **diffère** le corrigé vers l'annexe |

En mode manuel, chaque corrigé est stocké dans une macro (`\csgdef`) puis rejoué par
`\CAPETANNEXE` : pas d'écriture fichier, donc les `circuitikz`, accents et `%` traversent intacts.
`\CAPETNOTION{code}{titre}` (posée par `\CAPETOUVRENOTION` dans `main.tex`) génère les
intertitres de notion dans l'annexe.

**Piège traité — appels décoratifs** : les fichiers d'exercices utilisent aussi `\CAPETSHOW` dans
leur `\fancyhead` et leur bloc de titre pour afficher « (énoncés) »/« (corrigés) ». Ces appels ne
sont pas des exercices : ils sont reconnus par comparaison au libellé `\CAPETLIBELLEENONCES` et
exclus de la numérotation. Sans cela, deux faux exercices par notion décalaient tous les renvois.

### Deux variantes d'impression

| Fichier | Pages | Usage |
|---|---|---|
| `main.tex` → `main.pdf` | 378 | simple face, marges symétriques 1,4 cm |
| `main_rectoverso.tex` → `main_rectoverso.pdf` | 404 | **recto verso relié** |

La variante recto verso (`main_rectoverso.tex` + `parties_rectoverso.tex`, créées le 2026-09-20) :

- `twoside` + `\cleardoublepage` : les 30 notions et les 4 parties ouvrent **toujours sur un recto**
  (en simple face, 17 notions sur 30 tombaient sur un verso)
- `\geometry{inner=2.2cm, outer=1.4cm}` — **surcharge locale**, `fiches/preamble.tex` n'est pas
  modifié, donc les fiches compilées seules gardent leurs marges symétriques
- `\ficheHeaders` redéfini localement : titre de notion vers l'**extérieur** de la double page
  (`LE`/`RO`), mention générale à l'intérieur (`RE`/`LO`)
- les 26 pages supplémentaires sont des pages blanches d'ajustement

⚠ **Piège vérifié** : le liminaire (couverture + sommaire) doit occuper un nombre **pair** de pages,
sinon parité logique et parité physique se décalent et `\cleardoublepage` ouvre les notions à gauche.
Contrôler la parité sur le PDF rendu, jamais sur le seul compteur LaTeX.

### Chapitres autonomes (`manuel/pdf/`)

`manuel/pdf/` contient les deux manuels complets **et un PDF par notion** (32 fichiers) :

```
pdf/00_Manuel_complet.pdf              378 p. — simple face
pdf/00_Manuel_complet_rectoverso.pdf   404 p. — recto verso relié
pdf/T{nn}_{Titre}.pdf                  10 à 16 p. — cours + exercices + corrigés de la notion
```

Chaque chapitre est **recompilé**, pas découpé : `chapitre.tex` est un gabarit paramétré
(`\CAPETCHAP`, `\CAPETFICHE`, `\CAPETEXOS`, `\CAPETTITRE`) qui réutilise le mode `\CAPETMANUEL`,
donc chaque fascicule repagine à partir de 1 et **génère sa propre annexe de corrigés**.

⚠ **Pourquoi ne pas découper le PDF du manuel** : l'annexe A est un flux continu et **25 sections
de corrigés sur 30 commencent en milieu de page**. Un découpage par page fait donc débuter le
chapitre T05 par la fin des corrigés de T04. Seule la recompilation donne des chapitres propres.

### Compilation

```bash
cd manuel/
pdflatex -interaction=nonstopmode main.tex              # 3 passes — simple face
pdflatex -interaction=nonstopmode main_rectoverso.tex   # 3 passes — recto verso relié

# Un chapitre (2 passes pour \pageref{LastPage}) ; chapitres.lst donne les 4 paramètres :
pdflatex -jobname=T05 "\def\CAPETCHAP{T05}\def\CAPETFICHE{T05_Phenomenes_Thermiques}\
\def\CAPETEXOS{T05_exercices}\def\CAPETTITRE{Phenomenes thermiques}\input{chapitre.tex}"
```

⚠ `chapitres.lst` doit être en **LF** : un CRLF injecte un `^^M` dans le titre et fait échouer
les 30 compilations avec « no legal \end found ».

**Critère de vérification** : le nombre de corrigés rendus en annexe doit égaler le nombre
d'exercices du corpus, et aucun renvoi ne doit afficher « p. ?? ».

## App de révision (`app/`)

PWA hors-ligne d'entraînement au rappel actif, créée le 2026-09-21.
Trois types de cartes : **formule**, **piège** (conditions d'application),
**schéma** (3 niveaux : reconnaissance / calcul / tracé). État courant
(2026-11-10) : 727 cartes (421 formules, 272 pièges, 34 schémas) sur
33 thèmes, poids de 0,231 à 1,3. Notice d'usage complète : `app/README.md`.

Ajouts du 2026-11-10 : T31–T33 (48 formules, 34 pièges, 3 schémas) et les compléments du
référentiel dans 13 fiches (29 formules en blocs `$$` en fin de § 1, 24 pièges en fin de § 5,
paragraphes sans TikZ en fin de bloc 1). 0 carte antérieure modifiée. Les 77 nouvelles
formules ont leur question dans `scripts/questions.json`.

Les 15 pièges ajoutés le 2026-11-09 (T08 p-007/008, T10 p-008, T11 p-007/008/009,
T20 p-008/009, T25 p-007 à 010, T26 p-008/009, T27 p-008) viennent des commentaires du
rapport du jury 2026 (troisième concours). Ils sont ajoutés **en fin** de § 5, donc aucun id
existant n'a bougé (vérifié : 0 carte ancienne modifiée). Chacun cite sa question source.

### ⚠ Publication : fusionner, ne jamais recopier `app/` (constat du 2026-11-10)

Le dépôt publié `capet-revision` (GitHub Pages) a divergé de `app/` : ses écrans
(Catégories, Sujets, Cours), son code et son `cards.json` sont plus récents, et ce dernier
porte des enrichissements faits à la main (règles des pièges, réponses des schémas, `forme`)
absents de son `corrections/cartes.json`. Recopier `app/` ou régénérer son `cards.json` les
détruirait. Toujours `git pull` dans `capet-revision`, puis **fusionner** les seules cartes
nouvelles (ids absents) dans le `cards.json` publié. Procédure complète : `app/README.md`,
section « Publication sur GitHub Pages ».

### Principe : l'app est un artefact régénérable

`app/cards.json` et `app/svg/` sont **générés** par `scripts/build_cards.py`
depuis `fiches/`. Ne jamais éditer de contenu pédagogique dans `app/` :
la prochaine génération l'écraserait. Les sources LaTeX/Markdown restent
l'unique source de vérité. Ces artefacts (`cards.json`, `svg/`,
`sw-assets.js`) sont exclus du dépôt (`.gitignore`) car entièrement
dérivés : quiconque clone lance `python scripts/build_cards.py`.

### Sources d'extraction

| Type de carte | Source | Volume |
|---|---|---|
| formule | `T{nn}_contenu.md` § 1 (tableau MD **et** blocs `$$`) | 421 |
| piège | `T{nn}_contenu.md` § 5 « Lacunes et pièges » | 272 |
| schéma | environnements TikZ des `T{nn}_*.tex` → SVG | 34 |

⚠ **Ajouter une formule à une fiche existante** : en bloc `$$` à la **fin** de la § 1, jamais en
ligne de tableau. Les formules en tableau sont numérotées avant les blocs : une ligne de tableau
ajoutée décalerait l'identifiant de toutes les formules en bloc du thème, et leurs questions.
Même logique pour les schémas : pas de TikZ inséré avant un TikZ existant.

⚠ La section `## 3. ATTENTES DU JURY` n'est **pas** extraite, et ne doit pas
l'être : l'audit de véracité du 2026-09-20 a établi que 54 % des citations
jury étaient défectueuses, dont 27 sans aucun support textuel. Importer ces
encadrés propagerait des citations fabriquées dans l'outil de révision.

### Pondération par la fréquence au concours

La pondération a **deux niveaux**, et les deux viennent des sources :

1. **Niveau thème** — le `\ficheEntete` de chaque fiche porte
   `Présence : n/13 sujets`. Ce ratio est le poids de base de toutes les
   cartes du thème.
2. **Niveau formule** — les formules dont la colonne `Fréquence` est
   renseignée (`Systématique`, `Très fréquent`, `Présent`…) voient ce poids
   de base multiplié par un bonus (0,9 à 1,3, cf. `_BONUS_FREQUENCE` dans
   `scripts/build_cards.py`). Une formule systématique d'un thème fréquent
   passe ainsi devant une formule anecdotique du même thème.

Le poids final pilote l'ordre de la file quotidienne et le calcul d'urgence
de l'écran Priorités (`urgence = poids × (1 − maîtrise)`).

### Piège : les identifiants de carte sont positionnels

Un id vaut `T19-f-003` (3ᵉ formule de T19 dans l'ordre du fichier). Insérer
une formule **au milieu** d'une section décale tous les ids suivants de ce
thème et désaligne la progression enregistrée (stockée par id dans
`localStorage`, cf. `app/js/store.js`). Ajouter en fin de section est sans
effet. Exporter la progression (écran Réglages) avant une refonte de fiche.

### Chaîne SVG

`latex` → `.dvi` → `dvisvgm --no-fonts --exact` → post-traitement des couleurs.
Le `--no-fonts` convertit le texte en tracés (aucune police à charger) ; le
post-traitement remplace `#000`/`#fff` par `currentColor`/`var(--svg-bg)`,
sans quoi les schémas sont invisibles en thème sombre.

### Lancer l'app et ses tests en local

Un seul serveur depuis la **racine** du dépôt (jamais `--directory app`,
sinon les harnais `tests/*.html` sortent de la racine servie) :

```bash
python -m http.server 8765 --directory .
# app : http://localhost:8765/app/
# tests : http://localhost:8765/tests/*.html
```

### Installation iPhone : condition de survie de la progression

Safari purge les données (`localStorage` compris) d'un site simplement
visité au bout de 7 jours d'inactivité (ITP), mais pas celles d'une PWA
ajoutée à l'écran d'accueil (Safari → Partager → « Ajouter à l'écran
d'accueil »). Sans cette installation, la progression ne survit pas à deux
semaines sans révision. Même installée, il n'y a aucun serveur derrière
cette app : l'export JSON de l'écran Réglages reste la seule vraie
sauvegarde.

## Conventions de contenu

- **Formules** : notation LaTeX inline (`$...$`) dans les tableaux Markdown
- Les fichiers `.md` issus de Marker contiennent les images inline (base64 ou fichiers séparés `.jpeg/.png`)
- Chaque dossier de conversion contient : `{nom}.md` + images associées
