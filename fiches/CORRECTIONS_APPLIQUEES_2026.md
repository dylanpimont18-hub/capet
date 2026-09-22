# Corrections appliquées aux fiches — 2026-08-24

Correction des 30 fiches selon `AUDIT_FICHES_2026.md`, par workflow multi-agent en deux passes :
une passe de correction (un agent par fiche) puis une passe de vérification indépendante (un agent
par fiche corrigée : recomptage du Bloc 5, comptage des en-têtes, recalcul chiffre par chiffre des
AN touchées).

## Bilan global

- **30/30 fiches corrigées**, toutes recompilées avec `pdflatex` sans erreur fatale.
- **29/30 validées** par la passe de vérification indépendante ; **1 fiche (T15) renvoyée en
  relecture humaine** (voir dernière section).
- Corrections transversales appliquées aux 30 fiches :
  - encadré générique « Procédure type copie concours » + flowchart supprimés du Bloc 3 partout où
    présents (dans T04/T05/T20 il avait déjà disparu ; dans T23/T28 il survivait sous la forme
    « Ordres de grandeur » réseau BT + « Synthèse express » en fin de Bloc 5, supprimés) ;
  - tableau du Bloc 5 recompté ligne par ligne et Bloc 0 « X/13 sujets » resynchronisé (qualificatif
    ajusté en conséquence) ;
  - tous les `\fancyhead[L]` ramenés sous 35 caractères ;
  - citations jury de T06/T07/T08/T15 vérifiées mot à mot contre les rapports sources : remplacées
    par le verbatim exact quand il existe, sinon dé-guillemetées et reformulées en constat sourcé.

## Présences Bloc 0 resynchronisées

| Fiche | Avant | Après | Fiche | Avant | Après | Fiche | Avant | Après |
|---|---|---|---|---|---|---|---|---|
| T01 | 13/13 | 13/13 (inchangé) | T11 | 8/13 | 10/13 | T21 | 9/13 | 8/13 |
| T02 | 13/13 | 13/13 (inchangé) | T12 | 6/13 | 4/13 | T22 | 8/13 | 6/13 |
| T03 | 11/13 | 12/13 | T13 | 9/13 | 7/13 | T23 | 9/13 | 9/13 (inchangé) |
| T04 | 9/13 | 9/13 (déjà corrigé) | T14 | 8/13 | 5/13 | T24 | 8/13 | 6/13 |
| T05 | 7/13 | 7/13 (déjà corrigé) | T15 | 7/13 | 5/13 | T25 | 6/13 | 4/13 |
| T06 | 10/13 | 13/13 | T16 | 7/13 | 6/13 | T26 | 9/13 | 9/13 (inchangé) |
| T07 | 9/13 | 12/13 | T17 | 8/13 | 5/13 | T27 | 11/13 | 9/13 |
| T08 | 11/13 | 13/13 | T18 | 7/13 | 4/13 | T28 | 3/13 | 3/13 (déjà corrigé) |
| T09 | 9/13 | 12/13 | T19 | 8/13 | 4/13 | T29 | 7/13 | 5/13 |
| T10 | 11/13 | 13/13 | T20 | 5/13 | 5/13 (déjà corrigé) | T30 | 10/13 | 12/13 |

## Détail par fiche (erreurs bloquantes traitées)

### T01 — Grandeurs Électrocinétique — vérifiée OK
Transversales uniquement (encadré générique, en-tête 47→33 car., Bloc 5 confirmé 13/13).

### T02 — Puissance AC — vérifiée OK
- QT1 réalignée sur les données officielles 2024 (plaque moteur In=229 A, cosφ=0,85 au lieu du
  η=0,92 inventé) : Pmot≈134,9 kW, Sch=√(178,3²+108,7²)≈208,8 kVA (remplace le 179,1 kVA faux),
  Iabs≈301 A, Fp≈0,854 — réconciliation complète QT1/QT2 sur le même sujet.
- Phrases de conclusion obligatoires ajoutées aux 3 QT (reliées au Fp exigé [0,92 ; 1] et au
  cahier des charges).
- QT2 : dénominateur 49 858 200 → 49 831 800 (cohérent avec ω=314 rad/s).

### T03 — Représentations Complexes / Impédances — vérifiée OK
Transversales uniquement (Bloc 0 11/13→12/13, en-tête 41→29 car.).

### T04 — Harmoniques / THD — vérifiée OK
- QT1 : amplitudes spectrales inventées (170/95/27/27/20 A…) supprimées — elles donnaient 0,61 au
  lieu du 0,59 du corrigé officiel 2024 ; l'énoncé renvoie au DT, le corrigé donne la méthode
  (rangs 6k±1) et la valeur officielle sourcée THD≈0,59 ; conclusion resynchronisée (59 %→25 %).
- Formulaire : THD_triphasé théorique corrigé 0,48 → ≈0,31 (0,48=√(π²/8−1) ne vaut qu'en
  monophasé) ; tableau 1.3 réécrit en distinguant tension (≈31 % tri, ≈48 % mono) et courant
  (jusqu'à ≈59 %, sujet 2024) ; légende du spectre corrigée.
- Réserve documentée : les amplitudes exactes du DT 2024 restent introuvables dans le dépôt —
  seules les valeurs officielles sourcées sont conservées.

### T05 — Phénomènes Thermiques — vérifiée OK
Aucune édition nécessaire : la version sur disque satisfaisait déjà l'audit (encadré absent,
7/13 exact, en-tête 27 car.). Les 3 QT recalculées exactes.

### T06 — Transformateur — vérifiée OK
- « PD6 (6 diodes) » → « PD3 (pont parallèle double triphasé, 6 diodes) » partout.
- QT3 : I₀=42 A inventé (S₀<P₀ impossible) remplacé par les données réelles du sujet E2 BAC3 2026
  (I₀=42,5 A, Vn=230 V, P₀=7,82 kW) ; corrigé recalculé en triphasé (S₀≈29,3 kVA, R_f≈20,3 Ω,
  X_m≈5,6 Ω), marqué `[corrigé reconstitué]`, résultat final et conclusion fournis.
- Citations jury : citation 2025 alignée verbatim sur le rapport ; fausse citation « 2024 »
  (étoile/triangle) remplacée par une citation 2025 authentique + constat reformulé sans guillemets.
- Choix documenté : modélisation sur Vn=230 V du sujet (la source contenu.md utilisait 133 V) —
  R_f passe de ≈2,26 Ω à ≈20,3 Ω, sans corrigé officiel pour trancher, d'où le marquage.

### T07 — Hacheurs — vérifiée OK
- Les 2 fausses citations jury (« Kirchhoff », introuvables) : remplacées par le verbatim réel du
  rapport 2025 (« lois basiques de l'électricité… ») / reformulées en constat sans guillemets
  (fait Q14 CV1/CV2/CV3 réel) ; idem pour la citation en conclusion de QT2.
- Sous-thème MPPT (jamais traité) retiré du Bloc 0. La formule f_P erronée de §2.7 ne concernait
  que T08 (vérifié absent de T07).

### T08 — Redresseurs — vérifiée OK
- Formule du facteur de puissance corrigée aux 4 emplacements : f_P=(q/π)·sin(π/q) (racine
  supprimée) ; AN resynchronisées (P3 : 0,827 ; PD6 : 0,955).
- f_P,PD2≈0,45 → 2√2/π≈0,90 (conformité CDC « Non »→« Limite »), hypothèse « courant lissé » ajoutée.
- Citations jury 2025/2024 : verbatim réel 2025 restauré ; citation 2024 introuvable dé-guillemetée
  et adossée au contenu réel du corrigé 2024 (IEC/EN 61000-2-2, THD<25 %).

### T09 — Onduleurs — vérifiée OK
- THD QT1 corrigé 59 %→61 % (√10 883/170≈0,614), propagé au Bloc 1 et au formulaire, avec note
  signalant que le corrigé officiel 2024 affiche 0,59 (conclusion de non-conformité inchangée) ;
  pseudo-citation jury contenant le 0,59 remplacée par la citation authentique B13.
- QT3 : R=0,137 m inventé remplacé par la vraie donnée du sujet Urbanloop (R_roue=0,20 m) ;
  n_m≈796 tr/min et f_s≈186 Hz recalculés et propagés.

### T10 — Mécanique — vérifiée OK
- QT2 (inertie KUKA) : `[incertain]` → `[corrigé reconstitué]`, valeur officielle 0,0118 kg·m²
  donnée en référence, écart ×2,2 expliqué (données DT absentes du dépôt) — réserve résiduelle
  documentée dans la fiche, irrésoluble sans le DT du sujet 2025.
- Bloc 5 « Ordres de grandeur » électrotechnique hors-sujet remplacé par des repères mécaniques
  sourcés (accélérations, rendements réducteur, adhérence rail/roue, couple MF67).
- En-tête ~60→33 car. ; milliers séparés dans QT1.

### T11 — Machine CC — vérifiée OK
- Schéma couple-vitesse §1.3 redessiné : pentes négatives (caractéristique tombante), étiquettes
  repositionnées.
- QT2 : arrondi 0,963 → 0,964 propagé aux deux occurrences.

### T12 — Machine Synchrone — vérifiée OK
- Diagramme de Kapp redessiné en convention moteur (E=Vs−jXsIs), cohérent avec l'équation du cours ;
  phrase « rotor en avance » corrigée en « rotor en retard » (§1.2 et Bloc 4 point 4).
- QT3 : les 3 rendements inventés (0,97/0,90/0,72 et le produit faux 0,630) supprimés — calcul
  refait avec le η_global=63 % donné dans le sujet : P_elec≈794 W, pertes≈294 W ;
  P_meca=500 W marqué `[corrigé reconstitué]`.
- `\vec` → `\underline` sur les équations touchées.

### T13 — Machine Asynchrone — vérifiée OK
- QT1 : Pa corrigé 134,6→134,3 kW (3×230×229×0,85=134 308,5 W).
- QT2 : Pt corrigé 66,8→66,6 kW, chaîne propagée (P_meca 62,2 kW, P_u 32,9 kW) ; marquage
  `[corrigé reconstitué]` ajouté (le sujet réel donne P_u≈100 kW).
- QT3 : facteur p rétabli dans la dérivation du couple (C_em=3pV_s²g/(R'_Rω_s)).
- Sous-thèmes du Bloc 5 plafonnés à 7/13 ; « schéma équivalent monophasé » retiré du Bloc 0
  (jamais représenté) ; overfull hbox de QT2 éliminé.

### T14 — Variation de Vitesse — vérifiée OK
- Sources QT1/QT3 corrigées « E2 disc. 2024 » → « E1 2024 » et coche fantôme retirée du Bloc 5.
- THD pleine onde resynchronisé partout sur 61,4 % (l'erreur 59 % dupliquée avec T09 est résolue
  dans les deux fiches).
- QT3 : formules d'identification fausses (Tr≈58 s) remplacées par la mise en équation standard
  PI + 1er ordre (ω0=√(K_meca·Ki/τ_meca)≈8,6 rad/s, m≈0,61), marquée `[corrigé reconstitué]` ;
  consignes inventées (m=1, Tr=1 s) supprimées de l'énoncé ; « dépassement nul » attribué
  explicitement au corrigé officiel (tension source/recalcul documentée, non tranchable sans la
  mise en équation exacte du sujet).

### T15 — Stockage d'Énergie — ⚠ RELECTURE HUMAINE (voir dernière section)
- QT2 : confusion Q16/Q19 corrigée — valeurs finales alignées sur le corrigé officiel 2020
  (E_nécessaire=928 W·h, Cb=19,33 A·h, 13s×4p, 52 cellules, 4,784 kg), fin du facteur ×6,8.
- 4 citations jury remplacées par les verbatims exacts des rapports 2020/2021 (dont la fausse
  citation 2021, remplacée par le verbatim du corrigé officiel Q10 correctement attribué).
- Ligne « BAC3/E2 2026 » vide supprimée du Bloc 5 ; mise en garde DoD ajoutée en 1.1.

### T16 — Énergies Renouvelables — vérifiée OK
- « Hacheur élévateur » → « hacheur abaisseur » partout, et formule α=V_PV/E_b (α>1 impossible)
  → α=E_b/V_PV avec 0<α<1, corrigée dans le cours ET le formulaire ; sens de variation de α
  reformulé dans QT3. En-tête 66→28 car. (violation la plus sévère du corpus).

### T17 — Distribution / Sécurité — vérifiée OK
Bloc 0 8/13→5/13 ; label « E1 disc. 2024 » corrigé ; sous-thème plafonné à 5/13 ; en-tête 60→30 car.

### T18 — Composants Électroniques — vérifiée OK
Bloc 0 7/13→4/13 (qualificatif « occasionnel ») ; en-tête 61→30 car.

### T19 — AOP — vérifiée OK
- Les deux topologies « soustracteur » distinguées explicitement : soustracteur 1 AOP
  (Vs=(R2/R1)(V2−V1)) vs étage d'instrumentation 2 AOP (G1=(2R1+R2)/R2) — paragraphe d'alerte
  ajouté en 1.2, titre/énoncé de QT1 reformulés, formulaire complété. Valeurs (G1≈3,4, G=340)
  inchangées (validées par l'audit).
- Bloc 0 8/13→4/13 (« régulier depuis 2019 » au lieu de « très fréquent »).

### T20 — Filtres RC/RL — vérifiée OK
Aucune édition nécessaire (version sur disque déjà conforme : 5/13 exact, en-tête 19 car., encadré
absent). Les 3 QT recalculées exactes.

### T21 — Fonctions de Transfert / Bode — vérifiée OK
- QT2 : scénario G0=+12 dB marqué `[corrigé reconstitué : valeur illustrative]` ; phrase de
  décalage de gain corrigée (20log 0,25=−12 dB). En-tête 48→28 car. ; Bloc 0 9/13→8/13.

### T22 — CAN/CNA / Numérisation — vérifiée OK
- QT2 : « CAN 10 bits » → « CAN 8 bits (ADS7029-Q1) » conformément au sujet réel ; corrigé
  recalculé (q=3/255≈11,76 mV, S=c/q=255/95≈2,684 LSB/°C exact cette fois), mot numérique
  resynchronisé (N_C≈148=94₁₆), conclusion en plage 8 bits ; marqué `[corrigé reconstitué]`.

### T23 — Capteurs / Conditionnement — vérifiée OK
Résidu générique du Bloc 5 (« Ordres de grandeur » réseau BT + « Synthèse express ») supprimé ;
9/13 et en-tête déjà conformes ; les 3 QT recalculées exactes.

### T24 — Systèmes Embarqués — vérifiée OK
- Trame CAN corrigée : délimiteur CRC ajouté, total 111 → 108 bits, propagé au formulaire.
- QT1 : `[incertain]` → `[corrigé reconstitué]` (valeur C8₁₆ non vérifiable sans le DT ADCON0).
- Bloc 0 8/13→6/13 ; en-tête 54→24 car.

### T25 — Transmission Numérique — vérifiée OK
- Même trame CAN corrigée 111→108 bits aux 5 emplacements, avec propagation jusqu'à QT3 :
  t_trame=108 µs (au lieu de 111), marge recalculée 46 %. Bloc 0 6/13→4/13 ; en-tête 56→28 car.

### T26 — Modélisation des Systèmes — vérifiée OK
Transversales uniquement (9/13 confirmé cohérent, en-tête 55→31 car.).

### T27 — Systèmes Bouclés / Correcteurs — vérifiée OK
- Récurrence du PI numérique corrigée aux 3 occurrences (cours 1.6, formulaire, corrigé QT3) :
  a₀=K_co(1+T_e/T_co), a₁=−K_co — re-dérivée par discrétisation d'Euler arrière (la source
  contenu.md portait la même erreur). Bloc 4 point 5 resynchronisé. Bloc 0 11/13→9/13.

### T28 — Logique Combinatoire — vérifiée OK
Résidu générique du Bloc 5 supprimé (comme T23) ; 3/13 et en-tête déjà conformes ; unités siunitx
dans la conclusion de QT1 ; les 3 QT recalculées exactes.

### T29 — Logique Séquentielle / GRAFCET — vérifiée OK
- Sur-représentation du GRAFCET traitée par honnêteté documentaire : note sourcée en tête de 1.2
  (« GRAFCET » n'apparaît que 2 fois dans les 41 sujets, jamais comme question d'examen) et
  sous-thème du Bloc 0 requalifié « au programme, jamais interrogé 2013-2026 ». Aucune ligne
  GRAFCET ajoutée au Bloc 5 (aucune épreuve ne l'interroge). Bloc 0 7/13→5/13.

### T30 — Mesurage / Instrumentation — vérifiée OK
- QT1 : chaîne incohérente (S≈10,24 avec les données affichées) remplacée par la dérivation
  cohérente du sujet E2 BAC3 2026 : c=3/95 V/°C, CAN 8 bits, q=3/255 → S=c/q=255/95≈2,684 °C⁻¹
  exact ; énoncé resynchronisé (8 bits, U_PE=3 V), conclusion en plage 8 bits, marqué
  `[corrigé reconstitué]`. Bloc 0 10/13→12/13 (sous-estimation).

## ⚠ Relecture humaine requise

### T15 — Stockage d'Énergie (seule fiche non validée par la passe de vérification)

Le correcteur a bien éliminé le facteur ×6,8 et toutes les valeurs finales de QT2 coïncident avec
le corrigé officiel (928 W·h, 19,33 A·h, 13s×4p, 4,784 kg). Mais le vérificateur a découvert que
le corrigé officiel Q19-Q20 est **lisible** dans
`docs/CAPET_SII_IE/06_PDFs_Originaux/2020/Rapport_Jury_2020.md` (le correcteur n'avait consulté
que la copie Colab, où ces formules sont des images omises) :

1. **Énoncé QT2** : la fiche affiche E_trajet ≈ 4,06 W·h `[corrigé reconstitué]` et un « taux de
   décharge max : 70 % » (non marqué), alors que le corrigé officiel donne **E_trajet = 4,64 W·h**
   (16 732,9 J) et une division par **0,8**. Les deux chaînes aboutissent au même 928 W·h — l'aval
   est juste — mais les données d'énoncé sont fausses.
2. **Mise en garde DoD ajoutée en Bloc 1.1** : elle présente la convention « /0,7 » comme certaine,
   alors que ni le corrigé E1 2020 (×30 %) ni le corrigé E2 robot (/0,8) ne l'utilisent — c'est
   précisément la confusion % de décharge / profondeur de décharge que la citation source dénonce.

**Correction proposée (à valider)** : remplacer 4,06 W·h → 4,64 W·h et /0,7 → /0,8 dans l'énoncé
et le corrigé de QT2 (le marquage `[corrigé reconstitué]` devient alors inutile, les valeurs étant
officielles), et reformuler la mise en garde DoD du Bloc 1.1 sans affirmer la convention /0,7.

## Choix assumés documentés dans les fiches (pas d'action requise, à connaître)

- **T06 QT3** : modélisation triphasée sur Vn=230 V du sujet (la source contenu.md utilisait
  133 V) — sans corrigé officiel, marqué `[corrigé reconstitué]`.
- **T09/T14** : THD pleine onde affiché 61,4 % (recalcul exact) avec note signalant le 0,59 du
  corrigé officiel 2024 — conclusion identique dans les deux cas.
- **T10 QT2** : écart ×2,2 entre reconstitution (0,026 kg·m²) et valeur officielle (0,0118 kg·m²)
  irrésoluble sans le DT du sujet 2025 — documenté dans la fiche.
- **T14 QT3** : m≈0,61 recalculé vs « dépassement nul » du corrigé officiel — attribution explicite,
  mise en équation exacte du sujet indisponible.
- **T04 QT1** : amplitudes spectrales du DT 2024 introuvables dans le dépôt — seules les valeurs
  officielles sourcées sont conservées.
