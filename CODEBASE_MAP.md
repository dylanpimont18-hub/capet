# CODEBASE_MAP.md

Index de navigation du dépôt CAPET SII Ingénierie Électrique.

---

## Fichiers racine

---

## fiches/preamble.tex
Preamble LaTeX commun à toutes les fiches (et à la banque d'exercices) : packages, couleurs, styles tcolorbox.
- Encodage PDF texte : `\input{glyphtounicode}`, `\pdfgentounicode=1`, `\usepackage{cmap}` pour améliorer recherche/copie des caractères accentués
- `colElec`, `colAuto`, `colMeca`, `colTherm` — palettes de couleurs par domaine
- `colExo` — couleur cyan dédiée à la banque d'exercices (`exercices/`), distincte des fiches
- `\sisetup{... group-minimum-digits=4}` — séparateur de milliers appliqué dès 4 chiffres dans les `\SI` (2026-09-02 ; sans cela siunitx rendait « 6000 Hz » sans espace)
- `\jour`, `ar`, `ad`, `	r` — unités non fournies par siunitx, déclarées ici une fois pour toutes sous garde `\ifdefined` (2026-09-02). **Ne pas les redéclarer dans les fichiers** ; les déclarations locales subsistantes des exercices sont elles aussi sous garde
- `ficheSection` — style tcolorbox pour sections principales
- `questiontype` — style tcolorbox pour questions types (fond vert clair)
- `exoBox` — style tcolorbox pour les exercices/corrigés de `exercices/` (fond cyan clair)
- `jury` — style tcolorbox pour encadrés jury (fond jaune ambre)
- `\difficulte{1|2|3}` — macro affichant la difficulté d'un exercice en étoiles (`$\bigstar$`)
- `circuitikz` (option `european`) — schémas de circuits pour `exercices/` ; `\AtBeginDocument{\shorthandoff{:;!?}}` juste après `babel[french]` (sinon `to[...]` de circuitikz plante — babel active ces raccourcis à `\begin{document}`)
- `docTech` — style tcolorbox neutre (gris) pour encadrer un extrait de document technique (plaque signalétique, datasheet) dans un exercice

## fiches/main.tex
Point d'entree du manuel complet : page de couverture puis agregration des fiches T01 a T30 via `\include` sur les sources LaTeX.
- `\CAPETINCLUDEMODE` — active le mode inclusion des fiches pour Overleaf et compilation source unique
- Page de garde : bloc "Usage cible" et signature de bas de couverture presentes (rendu complet harmonise avec Overleaf)

## fiches/T01_Grandeurs_Electrocinetique.tex a fiches/T30_Mesurage_Instrumentation.tex
Fiches compilables de deux manieres : seules comme documents autonomes, ou incluses dans `main.tex` pour former un manuel unique.
- `\CAPETBEGINFILE` / `\CAPETENDFILE` — encapsulent l'ouverture et la fermeture du document selon le mode de compilation
- Correction post-audit 2026-08-24 appliquée aux 30 fiches (encadré générique Bloc 3 supprimé, Bloc 0/Bloc 5 resynchronisés, en-têtes < 35 car., erreurs de calcul de l'audit corrigées) — voir `AUDIT_FICHES_2026.md` et `CORRECTIONS_APPLIQUEES_2026.md`

## fiches/AUDIT_FICHES_2026.md
Audit qualité 2026-08-24 des 30 fiches : classement /100, problèmes systémiques (§2), plan de correction priorisé (§3), détail par fiche (§4).

## fiches/CORRECTIONS_APPLIQUEES_2026.md
Synthèse des corrections post-audit (workflow multi-agent 2026-08-24) : bilan 29/30 vérifiées OK, détail par fiche, cas T15 en relecture humaine, choix assumés documentés.

## fiches/TEMPLATE_FICHE.md
Spécifications structurelles complètes pour la génération des fiches LaTeX.
- Décrit les 5 blocs obligatoires, les règles typographiques, et la checklist de validation

## fiches/T02_Puissance_AC.tex
Fiche compilable T02 — Puissance en régime alternatif sinusoïdal. Domaine colElec.
- Texte remis en UTF-8 lisible (accents français restaurés dans les titres et contenus)
- Seule fiche correcte dès l'origine (accents + triangle des puissances déjà présents)

## fiches/T03_Representations_Complexes_Impedances.tex
Fiche compilable T03 — Représentation complexe, impédances, modèle MAS, Bode. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (diagramme de Fresnel, circuit RL série, I/U_R/U_L/U et angle φ)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T04_Harmoniques_THD.tex
Fiche compilable T04 — Harmoniques réseau, THD, puissance déformante, MLI, norme IEC. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (spectre en raies I_n/I_1 par rang harmonique, bâtons décroissants)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T05_Phenomenes_Thermiques.tex
Fiche compilable T05 — Couple thermique, résistance thermique, PT100, thermocouple, 4-20 mA. Domaine colTherm.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (circuit thermique équivalent, analogie électrique R_th/Φ/ΔT)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- Audit de veracite 2026-09-20 (Bloc 4) : citation « jury 2019 » (couple thermique equivalent) supprimee et citation « jury 2024 » (plage/tolerance capteur) remplacee — toutes deux fabriquees. L'encadre ne porte plus qu'une citation authentique, Rapport_Jury_2020.md l.703.
- Audit de veracite 2026-09-20 (Bloc 4) : citation « jury 2019 » (couple thermique equivalent) supprimee et citation « jury 2024 » (plage/tolerance capteur) remplacee — toutes deux fabriquees. L'encadre ne porte plus qu'une citation authentique, Rapport_Jury_2020.md l.703.

## fiches/T06_Transformateur.tex
Fiche compilable T06 — Transformateur monophasé/triphasé, essai à vide/court-circuit, rendement. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (schéma équivalent essai à vide, V1/Rf/Xm en parallèle)
- Piège circuitikz : `to[cute inductor, l=...]` pour X_m, jamais `to[L, ...]` (rend un bloc plein sous ce préambule — cf. note `exercices-capet/SKILL.md`)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T07_Hacheurs.tex
Fiche compilable T07 — Hacheurs Buck/Boost/4Q, ondulation, entrelacement. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (chronogramme u_sortie(t) hacheur Buck, ON/OFF, valeur moyenne αE)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T08_Redresseurs.tex
Fiche compilable T08 — Redresseurs PD2/P3/PD6, facteur de puissance, harmoniques. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (chronogramme tension redressée PD2, |sin| avec valeur moyenne)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T01_Grandeurs_Electrocinetique.tex
Fiche compilable T01 — Grandeurs électriques fondamentales, lois de Kirchhoff, diviseurs, ALI parfait. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout des schémas manquants (diviseur de tension circuitikz E/R_A/R_B/Vs ; chronogramme u(t) avec U_max et U_eff)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T09_Onduleurs.tex
Fiche compilable T09 — Onduleurs monophasé/triphasé, pleine onde, MLI, THD. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (chronogramme tension pleine onde ±V_DC)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- Audit de veracite 2026-09-20 : citation fabriquee « les fonctions explicites doivent etre nommees et justifiees » (jury 2025) retiree aux deux endroits — note du corrige de QT2 de-attribuee, citation du Bloc 4 remplacee par Rapport_Jury_2025.md l.486. Citation MLI/THD « jury 2024 (B13) » inchangee.
- Audit de veracite 2026-09-20 : citation fabriquee « les fonctions explicites doivent etre nommees et justifiees » (jury 2025) retiree aux deux endroits — note du corrige de QT2 de-attribuee, citation du Bloc 4 remplacee par Rapport_Jury_2025.md l.486. Citation MLI/THD « jury 2024 (B13) » inchangee.

## fiches/T10_Mecanique.tex
Fiche compilable T10 — PFD, couple/puissance, réducteurs, inertie ramenée, couple thermique. Domaine colMeca.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (schéma-bloc chaîne cinématique Moteur→Réducteur→Charge)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- Piège tikz : nœud multi-ligne avec `\\` nécessite l'option `align=center` (sinon erreur "Not allowed in LR mode")
- Audit de veracite 2026-09-20 (Bloc 4) : citation fabriquee « jury 2023 » (expressions litterales) remplacee par Rapport_Jury_2024.md l.515, re-attribuee au rapport 2024. Citation couple/force (Rapport_Jury_2024.md l.1079) verifiee conforme et inchangee.
- Audit de veracite 2026-09-20 (Bloc 4) : citation fabriquee « jury 2023 » (expressions litterales) remplacee par Rapport_Jury_2024.md l.515, re-attribuee au rapport 2024. Citation couple/force (Rapport_Jury_2024.md l.1079) verifiee conforme et inchangee.

## fiches/T11_Machine_CC.tex
Fiche compilable T11 — Machine à courant continu (MCC), quadrants de fonctionnement, hacheur 1Q/4Q. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (plan couple-vitesse Ω/Cem, famille de caractéristiques pour U1>U2>U3, quadrants I à IV)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- Audit de veracite 2026-09-20 (Bloc 4) : encadre jury entierement supprime — ses deux citations (« jury 2022 » bilan de puissance MCC, « jury 2023 » hacheur 1Q/2Q/4Q) etaient fabriquees et aucun des 8 rapports 2018-2025 ne traite ces themes. La fiche n'a plus de citation de jury (assume).
- Audit de veracite 2026-09-20 (Bloc 4) : encadre jury entierement supprime — ses deux citations (« jury 2022 » bilan de puissance MCC, « jury 2023 » hacheur 1Q/2Q/4Q) etaient fabriquees et aucun des 8 rapports 2018-2025 ne traite ces themes. La fiche n'a plus de citation de jury (assume).

## fiches/T21_Fonctions_Transfert_Bode.tex
Fiche compilable T21 — Fonctions de transfert, diagramme de Bode 1er/2e ordre, marges de stabilité. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (diagramme de Bode asymptotique gain + phase, 1er ordre)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- Audit de véracité 2026-09-20 : citation jury 2025 reformulée remplacée par le verbatim RJ2025 l.484 ; la citation 2023 et la statistique 2024 restent conformes

## fiches/T27_Systemes_Boucles_Correcteurs.tex
Fiche compilable T27 — Asservissements, FTBO/FTBF, correcteurs P/PI/PID, correcteur numérique. Domaine colAuto. Audit veracite 2026-09-20 : citation jury 2024 du Bloc 4 supprimee (fabriquee ; remplacement RJ2023 l.459 ecarte car doublon avec la citation 2023 deja presente).
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (schéma-bloc de l'asservissement à retour unitaire, E(p)→C(p)→Hproc(p)→S(p) avec retour Hcapt(p))
- QT1-QT3 : ajout/renforcement d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T12_Machine_Synchrone.tex
Fiche compilable T12 — Machine synchrone et servomoteur PMSM/BLDC. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (diagramme de Kapp, Vs/jXsIs/E et angle de charge δ)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- Audit de veracite 2026-09-20 (Bloc 4) : encadre jury entierement supprime (citations « jury 2024 » partie 3.3 et « jury 2025 » servomoteur, fabriquees) et note « Le jury 2025 deplore... » du point 5 de-attribuee. La fiche n'a plus de citation de jury (assume).
- Audit de veracite 2026-09-20 (Bloc 4) : encadre jury entierement supprime (citations « jury 2024 » partie 3.3 et « jury 2025 » servomoteur, fabriquees) et note « Le jury 2025 deplore... » du point 5 de-attribuee. La fiche n'a plus de citation de jury (assume).

## fiches/T13_Machine_Asynchrone.tex
Fiche compilable T13 — MAS, vitesse/glissement, bilan de puissance, couple électromagnétique. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (courbe couple-vitesse, zone linéarisée au voisinage du synchronisme)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- Audit de veracite 2026-09-20 (Bloc 4) : les deux attributions au « jury 2023 » autour de « verifier que le resultat est un entier » supprimees (provenaient du corrige technique Rapport_Jury_2023.md l.720, pas d'un commentaire de jury). Les 3 citations 2024 conformes sont inchangees.
- Audit de veracite 2026-09-20 (Bloc 4) : les deux attributions au « jury 2023 » autour de « verifier que le resultat est un entier » supprimees (provenaient du corrige technique Rapport_Jury_2023.md l.720, pas d'un commentaire de jury). Les 3 citations 2024 conformes sont inchangees.

## fiches/T14_Variation_Vitesse.tex
Fiche compilable T14 — Variateurs, commande V/f, THD, ATV630, boucle PI, 4 quadrants. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (schéma-bloc structure variateur Réseau→Redresseur→Bus DC→Onduleur→MAS)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T15_Stockage_Energie.tex
Fiche compilable T15 — Batteries (capacité, DoD, autonomie), association série/parallèle, STEP. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (grille de cellules N_s série × N_p parallèle)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T16_Energies_Renouvelables.tex
Fiche compilable T16 — PV, MPPT, éolien, STEP. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (courbe P=f(U) avec point MPP, U1/U2 de part et d'autre)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- Audit de véracité 2026-09-20 : les 2 citations « jury 2021 » fabriquées (correction en température ; justification du choix de l'onduleur) remplacées par les verbatims RJ2021 l.759 et l.757

## fiches/T17_Distribution_Securite.tex
Fiche compilable T17 — SLT (TT/TN-S/TN-C/IT), DDR, chute de tension, disjoncteur MA. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (ligne R_uL/X_uL entre source U_D et récepteur U, ΔU)
- Tableau SLT reformaté en colonnes `p{}` + `\footnotesize` (débordait du cadre avec 5 colonnes `l`)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- QT2 (chute de tension) recalculée le 2026-09-02 sur les données authentiques du sujet (E2_Disciplinaire_IE_2024 l.227 : Ru = 20 mΩ/km, Lu = 1,2 mH/km, X = 850 m) : conversion explicite X_L = L_u·X·ω, bilan de puissances (charge compensée Fp = 1 comme le pose le sujet), U_D = 431 V, ΔU = 31 V soit 7,2 % de U_D — conforme au corrigé officiel. Corrige deux erreurs cumulées : valeurs linéiques fausses (0,0424/0,0902 mΩ/m) et cos φ = 0,85 périmé. Verdict NF C 15-100 (public, « autres usages », ≤ 5 %) : non conforme.
- Audit de véracité 2026-09-20 : pseudo-citation « jury 2024 : ne pas omettre la partie réactive » (introuvable) supprimée ; les 3 citations de l'encadré jury restent conformes

## fiches/T18_Composants_Electroniques.tex
Fiche compilable T18 — Diode, BJT, MOSFET/IGBT, hacheur abaisseur. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (droite de charge diode + caractéristique, point de fonctionnement Q)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- Audit de véracité 2026-09-20 : les 2 citations de l'encadré jury (2024, 2025) étaient reformulées — remplacées par les verbatims RJ2024 l.511 et RJ2025 l.486

## fiches/T19_AOP.tex
Fiche compilable T19 — Montages AOP (inverseur, soustracteur...), comparateur à hystérésis, 4-20 mA. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (cycle d'hystérésis, seuils V_H/V_B, trajets montant/descendant)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- Audit de véracité 2026-09-20 : citation jury 2024 réduite au verbatim chiffré RJ2024 l.509 (70 %/47 %, sans la mention fabriquée « partie E (AOP) ») ; citation sur les trois conditions de l'AOP idéal (introuvable) remplacée par RJ2024 l.515

## fiches/T20_Filtres_RC_RL.tex
Fiche compilable T20 — Filtres passifs RC/RL 1er et 2e ordre, régime sinusoïdal. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (diagramme de Bode gain+phase, marqueur ω_c)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- Audit de véracité 2026-09-20 : citation attribuée à un « rapport jury 2026 » INEXISTANT remplacée par le verbatim RJ2023 l.459 ; le fait sur le filtre passe-bas RL des enroulements requalifié en extrait du corrigé officiel 2024 (RJ2024 l.239), et non en commentaire de jury

## fiches/T22_CAN_CNA_Numerisation.tex
Fiche compilable T22 — CAN/CNA, numérisation, échantillonnage. Domaine colElec.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (escalier de quantification avec rampe analogique et pas q)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)
- Audit de véracité 2026-09-20 : verbatim RJ2020 l.2386 restitué (« ne sache pas ») et l'ajout fabriqué sur l'encadrement des résultats retiré

## fiches/T23_Capteurs_Conditionnement.tex
Fiche compilable T23 — Capteurs et conditionnement (pont de Wheatstone, jauges de contrainte). Domaine colElec. Audit veracite 2026-09-20 : citation jury 2025 du Bloc 4 ramenee au verbatim RJ2025 l.1024.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (pont de Wheatstone en circuitikz, R1-R4 + jauge ΔR, V+/V-)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T24_Systemes_Embarques.tex
Fiche compilable T24 — Systèmes embarqués, API, microcontrôleurs, CAN, bus. Domaine colAuto.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (chronogramme PWM)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T25_Transmission_Numerique.tex
Fiche compilable T25 — Transmission numérique, FSK/LoRa/CAN. Domaine colElec. Audit veracite 2026-09-20 : encadre de citations jury du Bloc 4 supprime en entier (citations LoRa 2022 et trame CAN « 2026 » fabriquees, annee 2026 inexistante).
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (structure de trame CAN : SOF/ID/RTR/IDE+r0/DLC/Data/CRC/ACK/EOF)
- Correction TikZ : ajout de `align=center` sur les nœuds de la séquence de trame (erreur "Not allowed in LR mode")
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T26_Modelisation_Systemes.tex
Fiche compilable T26 — Modélisation de systèmes, réponse indicielle 1er ordre. Domaine colAuto. Audit veracite 2026-09-20 : citation jury 2025 remplacee par le verbatim RJ2025 l.484, citation jury 2024 (« forme canonique ») supprimee.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (essai indiciel : courbe exponentielle, asymptote KE0, marqueurs 0,632·KE0/τ)
- Correction d'un typo `**` introduit par erreur (habitude markdown) dans "Régime permanent"
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T28_Logique_Combinatoire.tex
Fiche compilable T28 — Logique combinatoire (portes, demi-additionneur). Domaine colAuto. Audit veracite 2026-09-20 : citation jury 2023 remplacee par le verbatim RJ2023 l.463.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (circuit demi-additionneur : portes XOR/AND alimentées par bus d'entrée)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T29_Logique_Sequentielle_GRAFCET.tex
Fiche compilable T29 — Logique séquentielle, GRAFCET. Domaine colAuto. Corrigée post-audit 2026 (présence 5/13, encadré générique Bloc 3 supprimé, note GRAFCET jamais interrogé). Audit veracite 2026-09-20 : citation « jury 2022 » remplacee par le verbatim RJ2021 l.819, annee corrigee en 2021.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (séquence GRAFCET : étape initiale double-bordée, transitions avec réceptivités)
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/T30_Mesurage_Instrumentation.tex
Fiche compilable T30 — Métrologie et instrumentation (chaîne capteur→conditionneur→CAN). Domaine colElec. Audit veracite 2026-09-20 : citation jury 2021 restituee au verbatim RJ2021 l.775 (liste d'instruments de TP ajoutee retiree), citation jury 2024 (« Shannon ») supprimee.
- Accents français restaurés dans tout le fichier (source était intégralement désaccentuée)
- Bloc 1 : ajout du schéma manquant (chaîne de mesure en blocs : Capteur→Conditionneur→CAN)
- Correction d'une cellule de formulaire garbled : "Periode (&)" → "Période d'éch."
- QT1-QT3 : ajout d'une étape "Conclusion" reliant chaque résultat à une exigence (règle `TEMPLATE_FICHE.md` Bloc 3)

## fiches/preamble.tex
Preamble LaTeX commun : ajout des bibliothèques TikZ `positioning` et `arrows.meta` pour compatibilité des schémas (`>=Stealth`).
- `\CAPETSHOW{enonce}{corrige}` — bascule de compilation pour `exercices/` : affiche la 1re branche par défaut, la 2e si `\CAPETCORRIGE` est défini avant l'`\input` (voir `.claude/skills/exercices-capet/SKILL.md`)

## exercices/main.tex
Point d'entrée de la banque d'exercices : titlepage puis agrégation des notions traitées via `\include`.
- `\CAPETINCLUDEMODE` — même mécanisme que `fiches/main.tex` pour la double compilation (autonome/inclus)
- Compilé en 2 PDF (`main_enonces.pdf`/`main_corriges.pdf`) via le drapeau `\CAPETCORRIGE`, propagé aux notions incluses — voir `fiches/preamble.tex` (`\CAPETSHOW`) et le skill `exercices-capet`

## exercices/T01_exercices.tex
5 exercices : diviseur de tension et loi des mailles (inédits, ★/★★), redresseur P3 valeur efficace/moyenne (2026, Épreuve 1, ★★), frein à courant de Foucault loi d'Ohm généralisée + hacheur 4Q avec point de vigilance jury 2022 (★★★), valeur efficace d'un créneau bipolaire (inédit, ★). Chaque exercice a un schéma (circuitikz pour les 4 circuits, tikz nu pour le chronogramme de l'exercice 5) — sert de référence structurelle (schémas + contenu) pour le skill `exercices-capet`. Compilé en `T01_enonces.pdf`/`T01_corriges.pdf`.

## exercices/T04_exercices.tex
6 exercices sur le THD et la puissance déformante, **complémentaires des 3 QT de la fiche T04** (aucun recouvrement : QT1 = 2024 B9-B13, QT2 = 2018 q.7-9, QT3 = 2025 CV3-2 ne sont repris nulle part ici) : spectre harmonique donné + calcul THD/Ieff (inédit, ★), **exercice `docTech`** — relevés d'analyseur DRS 3/DRS 4, comparaison LUBIO vs COMPACTO II sur 4 points de fonctionnement, question d'extraction puis Q1/D (2018, ville de Dampmart, q.6-9, ★★), dimensionnement filtre LC passe-bas (inédit, ★★), spectre de Fourier d'un onduleur triphasé six créneaux — |An| = 2√3·U0/(nπ), THD tronqué vs THD∞ (2026, essieu électrifié, A16-A19, ★★), comparaison six créneaux / MLI 10 kHz avec impédance harmonique de la machine (2026, A20 prolongée, ★★★), surcharge du conducteur de neutre par l'harmonique de rang 3 (inédit, contexte 2018, ★★★). Visuels : histogramme de spectre (tikz nu), filtre LC et réseau triphasé + neutre (circuitikz), chronogramme de tension composée six créneaux (tikz nu), tableau `docTech` de relevés constructeur. Compilé en `T04_enonces.pdf` (3 p.)/`T04_corriges.pdf` (4 p.).

## exercices/T02_exercices.tex
Notion T02 (puissance en régime sinusoïdal), 5 exercices. Rétro-convertie à la bascule `\CAPETSHOW` énoncé/corrigé (2026-07-15) ; compilée en `T02_enonces.pdf`/`T02_corriges.pdf`.

## exercices/T03_exercices.tex
5 exercices sur la représentation complexe et les impédances : circuit RLC série, module/argument et résonance (inédit, ★), **impédance de ligne triphasée et chute de tension** (réel, 2024 épreuve écrite disciplinaire B5-B9, ★★, **exercice `docTech`** — encadré DT2 extrait NF C 15-100, type A/B × éclairage/autres usages), condensateur de démarrage d'un moteur monophasé (inspiré 2024 D15-D17, ★★, circuitikz deux enroulements), **tension injectée en opposition de phase d'un régulateur d'éclairage public** (réel, 2018 EDE ENE 2 partie B Q10-11, ★★, diagramme de Fresnel tikz, citation jury 2018 verbatim), **synthèse d'un asservissement de vitesse à deux boucles imbriquées** (réel, 2024 partie C C5-C8, ★★★, schéma-bloc tikz, forme canonique 2ᵉ ordre → K_p = 0,336 / K_i ≈ 2,53). Compilé en `T03_enonces.pdf`/`T03_corriges.pdf`.
- 2026-09-02 : les exercices 2, 4 et 5 recouvraient les 3 Questions Types de la fiche T03 (QT1 modèle monophasé MAS, QT2 expression analytique d'un filtre, QT3 marge de phase) — les trois remplacés par d'autres questions des mêmes sujets réels (2024 partie B et partie C, 2018 Q10-11 dans son contexte d'origine). La **citation fabriquée** attribuée aux « rapports de jury 2024 et 2025 » sur la marge de phase (signalée 🟥 par l'audit) a disparu avec l'ancien exercice 5 ; les 2 citations subsistantes (jury 2018 l.2498, jury 2024 l.505) sont des verbatims vérifiés. Ligne DT2 reconstituée (table NF C 15-100 standard, WebSearch) — le tableau est une image omise par la conversion Markdown du sujet.

## exercices/T05_exercices.tex
5 exercices sur les phénomènes thermiques : **numérisation et mise à l'échelle de la chaîne d'acquisition de température** (réel, 2024 épreuve écrite disciplinaire D6-D11, ★, **exercice `docTech`** — encadré DT10/DT8, module AI 8xU/I/RTD/TC ST, PIW8 → MW8, seuils ventilation 6 912 / 8 797), résistance thermique en chaîne d'un transistor TO-220 (inédit, analogie électrique-thermique, schéma circuitikz résistances en série avec source de courant P), thermocouple type J et compensation de soudure froide (réel, 2024 D1, schéma circuitikz boucle fer/constantan), pont de Wheatstone quart de pont PT100 (inédit, schéma diamant circuitikz avec voltmètre), couple thermique équivalent sur cycle (réel, 2019 rame de métro Q25-28, ★★★, chronogramme effort/temps). Valeurs Rth,jc TO-220 et Tj,max composants vérifiées WebSearch. Compilé en `T05_enonces.pdf`/`T05_corriges.pdf`.
- 2026-09-02 : l'exercice 1 (transmetteur 4-20 mA linéaire, calcul de $I_{out}$ à $T = 120$ °C) était un **doublon strict de la QT2 de la fiche T05** — remplacé par la suite de la même partie D du même sujet 2024 (D6-D11, numérisation PIW8/mise à l'échelle MW8), et converti en **exercice `docTech`** (comble l'absence relevée §2.5 de l'audit). Valeurs du corrigé (a = 220/27 648, E = 220, PIW8 = 6 912 / 8 797) = verbatim des éléments de correction D9-D11 du `Rapport_Jury_2024`. Ligne PIW8 du DT8 reconstituée (table Siemens standard, WebSearch) — traçabilité détaillée en commentaire `%` en tête du fichier.

## exercices/T06_exercices.tex
5 exercices sur le transformateur, complémentaires des Questions Types de la fiche (passe 2026-09-02) : essai en court-circuit et chute de tension en charge (inédit, transfo 250 kVA, schéma Rs-Xs), **docTech** choix du calibre d'un régulateur abaisseur COMPACTO II dans la gamme constructeur (réel, 2018 EDE ENE 2 Q13-15, encadré DRS 4 §8 + DRS 6, 1re question = extraction), couplage Yy vs Yd et filtrage des harmoniques de rang 3 (inédit, schémas étoile/triangle), dimensionnement du circuit magnétique par la formule de Boucherot (inédit, N1=2200/N2=44, Bmax=1,58 T, schéma noyau 3 colonnes), rendement et condition Pfer=Pcu (inédit, diagramme de flux de puissance). Les deux exercices qui reproduisaient les QT de la fiche (P3 vs PD3 de 2026 E1 partie E — également notion T08 ; essai à vide Rf-Xm de 2026 BAC3 QA12-13) ont été remplacés. Ucc typique et formule de Boucherot vérifiés WebSearch. Compilé en `T06_enonces.pdf`/`T06_corriges.pdf`.

## exercices/T07_exercices.tex
5 exercices sur les hacheurs : MPPT photovoltaique CV1, fonction de modulation f_m sur 3 points et deduction Boost/Buck (reel, 2025 epreuve ecrite disciplinaire appliquee Q14/Q19, diagramme bloc PV->hacheur->bus, ★), **docTech** lecture du DT5 2025 (plaque panneau monocristallin 375 W / 39,6 V / 48,2 V / 9,92 A / 1980x1002 mm) -> composition du champ, puissance, surface et calibres courant/tension des semi-conducteurs de CV1 (reel, 2025 Q16, encadre docTech, ★★), equations differentielles des deux phases du Buck de recharge du robot Bakus et retour a <u> = alpha.E par periodicite (reel, 2023 epreuve ecrite disciplinaire appliquee C3/C4, schema circuitikz avec R_Li-ion, ★★), Boost a deux branches entrelacees CV3-1 : i_L2 decale de T/2, <i_S> = I_b(1-alpha) par bilan de puissance (reel, 2025 Q29/Q31/Q32, chronogramme tikz i_L1/i_L2, citation verbatim rapport jury 2025, ★★★), pont en H 4 quadrants commande bipolaire/unipolaire (inedit, schema circuitikz H complet avec diodes antiparalleles, ★★★). Compile en `T07_enonces.pdf`/`T07_corriges.pdf`.
- 2026-09-02 (complementarite fiches) : les 3 exercices qui dupliquaient les Questions Types de `fiches/T07_Hacheurs.tex` ont ete remplaces — ex. Buck L_min 2023 C5/C6 (= QT1) -> equations differentielles C3/C4 ; ex. entrelacement 4 bras 2023 C8 (= QT3) -> entrelacement 2 branches 2025 Q29/Q31/Q32 par bilan de puissance ; ex. derivation Boost 2025 Q26/Q27/Q32 (= QT2) -> exercice docTech sur le DT5. Gradation portee a 1-2-2-3-3.

## exercices/T08_exercices.tex
6 exercices sur les redresseurs monophase/triphase, rendus **complementaires** de la fiche `fiches/T08_Redresseurs.tex` (passe 2026-09-02). Ex1 : PD2 monophase, valeur moyenne/efficace et courant efficace de diode pour le calibrage (inedit, *, schema circuitikz pont en diamant, point de vigilance jury 2025 verbatim sur les lois de base) - disjoint des QT, conserve. Ex2 : PD2 + reversibilite en courant, risque de l'energie de freinage non evacuee (reel, 2024 Epreuve ecrite disciplinaire appliquee Q37/Q48/Q49, Urbanloop, **, diagramme bloc tikz) - disjoint de QT3 (qui calcule <U_PD2> et le rapport cyclique), conserve. Ex3 : taux d'ondulation PD2/P3/PD6 et rangs harmoniques, avec la distinction explicite ondulation efficace (48,3/18,3/4,2 %) vs cretea-crete (157 %) (inedit, **, chronogramme tikz). Ex4 : **exercice docTech** - lecture du DT1 (fleche du rail vs section), choix du profile 150x90x11 mm, resistance lineique 51,6 uohm/m, position la plus defavorable, L_max = 1395 m et verification que deux boitiers suffisent sur 1,1 km, puis rapport cyclique du hacheur (reel, 2024 Epreuve ecrite disciplinaire appliquee Q38 a Q43, Urbanloop, **, encadre docTech, 1re question = extraction) - **ajout** repondant au constat 2.5 de l'audit (nb_docTech etait 0). Ex5 : etude du P3 HYCITY - relation v1/vD1/uS du commutateur << plus positif >>, periode T_S = T1/3, **etablissement** de <uS> = (3V6/2pi)Veff par calcul integral, allure et valeur efficace de i_D1, puis facteur de puissance **f_P = 0,675** etabli et non applique (reel, 2026 Epreuve 1 partie E, questions E2/E4/E6/E8, ***, schema circuitikz P3 cathodes communes + chronogramme creneau) - **remplace** l'ancien exercice HYCITY sur E8/E9/E10, doublon de QT1 (f_P du PD3 = 0,955) et de QT2 (UM = 631 V, U2comp = 446 V, m = 1,12, valeurs identiques). Ex6 : PD2 tout thyristor, demonstration integrale de <uS> = <uS>_0 cos(alpha) et onduleur assiste (inedit, ***, chronogramme tikz avec angle d'amorcage). Gradation monotone 1-2-2-2-3-3. Compile en `T08_enonces.pdf` (5 p.) / `T08_corriges.pdf` (5 p.), rc=0, 0 erreur, 0 overfull, etancheite verifiee par pdftotext.
- 2026-09-02 : le facteur de puissance du P3 valait 0,827, issu d'une formule apocryphe `f_P = (q/pi).sin(pi/q)` (q = pulsations). Le sujet 2026 ne donne sa formule `f_P = (2/pi).Vq.sin(pi/q)` (q = **phases**) que pour le PD3 (E9 -> 0,955) ; la question E8 sur le P3 demande de l'etablir. La valeur retenue est **0,675** (= 3V2/2pi), verifiee par bilan de puissances et par le facteur de distorsion. La valeur 0,827 n'apparait plus que dans les commentaires `%` d'en-tete qui documentent l'erreur.
- **Incoherence fiche/exercices restante (hors perimetre)** : `fiches/T08_Redresseurs.tex` porte encore, en QT1, la valeur fausse f_P(P3) = 0,827 et la formule apocryphe. A corriger dans la fiche.

## exercices/T09_exercices.tex
5 exercices sur les onduleurs monophasé/triphasé, rendus **complémentaires** de la fiche `fiches/T09_Onduleurs.tex` (2026-09-02 : les 3 exercices qui dupliquaient les QT1/QT2/QT3 de la fiche ont été remplacés par d'autres questions des mêmes sujets réels ou d'une autre année). Ex1 : pont en H pleine onde charge R, Ueff/harmoniques/THD théorique (inédit, ★, schéma circuitikz). Ex2 : couplage étoile/triangle d'une MAS et détermination du bus continu U0 d'un onduleur triphasé (réel, 2026 Admissibilité : épreuve 2, questions A15 et A18, bus à pile à combustible, ★, schéma circuitikz 6 interrupteurs) — remplace l'ancienne identification CV1/CV2/CV3 (doublon QT2). Ex3 : onduleur CV3-2 charge RL, Pdistri/Qdistri/THD (réel, 2025 Épreuve écrite disciplinaire Q21-Q23, Mafate, ★★, schéma circuitikz + chronogramme) — disjoint des QT, conservé. Ex4 : quadrants de fonctionnement, réversibilité de la chaîne et risques du pont PD2 non réversible (réel, 2024 Épreuve écrite disciplinaire appliquée, questions 44/48/49, Urbanloop, ★★, schéma circuitikz pont PD2 en losange) — remplace l'ancien calcul de f0 = 185,6 Hz (doublon QT3). Ex5 : **exercice docTech** — extrait DT12 (tension d'une cellule lithium vs profondeur de décharge), nombre de cellules, ΔEb, tension efficace délivrée par l'onduleur et conformité ±10 % (réel, 2025 Épreuve écrite disciplinaire Q33-Q35, ★★★, encadré docTech + citation verbatim Rapport_Jury_2025 Q42) — remplace l'ancien THD 170/95/27/27/20 A (doublon QT1, déjà traité en T04 et T14). Gradation monotone 1-1-2-2-3. Compilé en `T09_enonces.pdf` (3 p.) / `T09_corriges.pdf` (4 p.), rc=0, étanchéité vérifiée par pdftotext.

## exercices/T10_exercices.tex
6 exercices de mécanique (cinématique, forces, moments, réducteurs), banque rendue complémentaire de la fiche T10 (aucune reprise des QT1/QT2/QT3) : rapport de réduction treuil pont levant (réel, 2014 Corrigé Épreuve 1 Q16, Chaban-Delmas, ★) ; **docTech** choix des freins d'urgence de la capsule Urbanloop — extraction du catalogue DT2 (couples 60/100/150/250/500 N·m et masses associées), puis situation dégradée « un frein avant en moins » et rechoix des références (réel, 2024 Épreuve écrite disciplinaire appliquée Q16 et Q18, ★, encadré docTech + question d'extraction, citation rapport jury 2024 sur la confusion couple/force) ; train d'engrenages deux étages, inertie équivalente et couple moteur (inédit, ★★, schéma tikz cercles tangents) ; aptitude à la traction et adhérence roue/rail — Fe, Ne, condition Fe < μr·Ne non vérifiée et leviers d'action (réel, 2019 E2 Q23/Q24/Q30, transformation rame métro, ★★, schéma tikz motrice sur voie) ; PFD sur pente et couple motoréducteurs (réel, 2023 épreuve écrite disciplinaire Q A1-A4, robot Bakus, ★★★, schéma tikz plan incliné) ; PFD en rotation sur l'axe 6 — accélération angulaire lue sur rampe puis Cm = Jeq·α et choix du robot (réel, 2025 Épreuve écrite disciplinaire appliquée Q10/Q11, KUKA, ★★★, chronogramme tikz, citation rapport jury 2025 sur les unités d'accélération angulaire). Compilé en `T10_enonces.pdf` (3 p.) / `T10_corriges.pdf` (4 p.), 0 erreur / 0 warning, étanchéité vérifiée par pdftotext.
- 2026-09-02 : passe complémentarité — trois doublons remplacés. L'ancien ex. « freinage Q16/Q17 » (décalque de la QT3) devient l'exercice docTech Q18 sur le catalogue DT2 ; l'ancien ex. « Ce puis Cm via ρ et η_red, Q25/Q26 » (décalque strict de la QT1, mêmes ρ=0,17 / η=97 % / de=0,86 m / 14,9 et 9,2 kN) est remplacé par l'aptitude à la traction Q23/Q24/Q30 du même sujet ; l'ancien ex. « Jeq par Huygens, KUKA Q6/Q8/Q9 » (décalque de la QT2) est remplacé par le PFD en rotation Q10/Q11, qui part du Jeq officiel = 0,0118 kg·m² imposé par le sujet. Corrigé officiel de 2025 retrouvé dans `Rapport_Jury_2025.md` (α = 431,1 rad/s², Cm = 5,086 N·m, couples robots 3,83 / 8,21 N·m) ; celui de 2024 dans `Rapport_Jury_2024.md` (TF = 1 350 N, aC = −1,35 m/s², rechoix 150/100 N·m → −1,75 m/s²). Le couple thermique équivalent Cth du sujet 2019 (Q27) reste traité en T11, pas repris ici.

## exercices/T11_exercices.tex
6 exercices sur la machine a courant continu (MCC), banque rendue complementaire de la fiche T11 (aucune reprise des QT1/QT2/QT3) : modele electrique de base E/Ia/Cem et bilan de puissance (inedit, ★, schema circuitikz induit) ; **docTech** chaine de couple de la rame de metro VMI — extraction sur les tables constructeur (transmission d'essieu, profil d'effort, plaque signaletique Alsthom, definition du couple thermique equivalent), puis Ce = Fe·de/2, Cm = Ce·ρ/η_red, Cth et Cnom (reel, 2019 Etude d'un systeme, d'un procede ou d'une organisation Q25 a Q28, ★, encadre docTech + question d'extraction + schema tikz moteur→reducteur→essieu) ; quadrants de fonctionnement et necessite du hacheur 4Q (inedit inspire de la Q A10 du sujet 2026, ★★, diagramme tikz plan Ω/Cem) ; essai a rotor bloque et determination de R et L (reel, 2026 Epreuve 1 partie A QA1-QA3, ★★, schema circuitikz induit + chronogramme courant) ; regime nominal Ke/Cp/bilan de puissance (reel, 2026 Epreuve 1 partie A QA4-QA6, ★★★, diagramme d'ecoulement des puissances tikz, point de vigilance jury 2024 verifie mot pour mot) ; energie dissipee par les rheostats de demarrage — integration de p(t) avec V(t)=γt puis bilan sur le trajet aller-retour (reel, 2019 Etude d'un systeme Q9 et Q10, ★★★, chronogramme p(t) tikz avec aire E_Rh). Compile en `T11_enonces.pdf` (5 p.) / `T11_corriges.pdf` (4 p.), 0 erreur / 0 warning, etancheite verifiee par pdftotext.
- 2026-09-02 : passe complementarite — l'ancien exercice « Cnom + comparaison a Cth » (decalque de la QT3) est remplace par la chaine de couple Q25-Q28, qui **reconstruit** Cth = 557,0 N·m au lieu de le parachuter (recalcul independant confirme ; valeur et presentation preservees, aucune requalification). L'ancien exercice « loi Rth(V) + p(t) » (decalque de la QT1) est remplace par les Q9/Q10 du meme sujet (calcul integral + bilan energetique, travail intellectuel distinct). Ajout du seul encadre docTech du fichier.

## exercices/T12_exercices.tex
5 exercices sur la machine synchrone et brushless (PMSM/BLDC), banque rendue complémentaire de la fiche T12 (aucune reprise des QT1/QT2/QT3) : **docTech** choix du servomoteur brushless d'axe 6 à partir de l'extrait de gamme KUKA DT2 (réel, 2025 Épreuve écrite disciplinaire appliquée Q11/Q12/Q13, encadré docTech + question d'extraction, ★), quadrants de fonctionnement de la machine synchrone sur le profil de vitesse Urbanloop (réel, 2024 Épreuve écrite disciplinaire appliquée Q44, ★, profil de vitesse tikz), résolveur et chaîne d'acquisition de position — δθ, δv et nombre de bits du CAN (réel, 2025 Épreuve écrite disciplinaire appliquée Q25/Q26/Q27, ★★, schéma tikz du résolveur), réversibilité pont PD2, dimensionnement ET vérification énergétique des supercondensateurs de freinage — l'agencement à 5 éléments est invalidé par Q52/Q53 (réel, 2024 Épreuve écrite disciplinaire appliquée Q48/Q49/Q51/Q52/Q53, ★★★, schéma circuitikz pont de Graëtz), diagramme de Kapp calcul de E et de l'angle de charge δ (inédit, ★★★, diagramme vectoriel tikz). Compilé en `T12_enonces.pdf` (3 p.) / `T12_corriges.pdf` (4 p.), 0 erreur / 0 warning.
- 2026-09-02 : exercice 3 — retrait de l'attribution fabriquée du produit « 0,98 × 0,80 × 0,80 » au sujet 2023 (celui-ci ne donne que le rendement global de 63 % ; le 0,98 y concerne l'onduleur du hangar). Remplacée par une reconstruction honnête par inversion du résultat officiel (3 584/5 715 ≈ 0,627). Aucun résultat numérique modifié.

## exercices/T13_exercices.tex
5 exercices sur la machine asynchrone (MAS), refondus pour être complémentaires de la fiche T13 (aucun recouvrement avec ses QT) : nombre de paires de pôles et glissement à partir des caractéristiques constructeur (réel, 2023 Épreuve écrite disciplinaire appliquée Q18, serre semi-fermée, ★, citation jury 2023 verbatim) ; **exercice docTech** — lecture de la plaque signalétique et du DT1, dimensionnement aéraulique, calcul de I'r par la loi d'Ohm complexe sur la branche rotorique, validation de la motorisation et choix du diamètre de pâles (réel, 2024 Épreuve écrite disciplinaire QA2/A4/A7/A8, extracteur d'air, ★★, encadré docTech + schéma circuitikz du modèle monophasé) ; moteur asynchrone monophasé à 2 vitesses par couplage de pôles PV/GV et verrouillage câblé (réel, 2024 QD15/D16/D17, ★★, schéma circuitikz) ; couple linéarisé C = 0,32(Ns−N), équilibre avec Cr = 1,77·10⁻⁵N² et plage de fréquence 23,1–41,8 Hz en commande V/f (réel, 2023 Q19/Q20, ★★★, graphe tikz C(N)/Cr(N)) ; THD pleine onde vs MLI et norme IEC/EN 61000-2-2 (inédit, valeurs harmoniques 1/n vérifiées WebSearch, ★★★, diagrammes en bâtons tikz). Compilé en `T13_enonces.pdf`/`T13_corriges.pdf` (4 pages chacun, étanchéité vérifiée par pdftotext).

## exercices/T14_exercices.tex
6 exercices sur la variation de vitesse et de couple des machines : vitesse de synchronisme et glissement MAS, principe V/f (réel, 2024 Épreuve écrite disciplinaire QA3, ★), conversion tr/min↔rad/s et puissance utile (inédit, piège jury unités Rapport 2020, ★), bilan de puissance de la MAS et validation du dimensionnement (réel, 2024 Épreuve écrite disciplinaire QA2 et QA5-A7, ★★), **choix d'un variateur Altivar 71 sur documents techniques DT5/DT6** (réel, 2014 Analyse d'un système pluritechnique Q22-Q24, ★★, **exercice `docTech`** : deux encadrés document technique + question d'extraction en première position), quadrants MCC bidirectionnelle (réel, 2026 Épreuve 1 QA10, ★★, plan couple-vitesse tikz), boucle d'asservissement scalaire complète (PI + plant mécanique, dérivation FTBF, calcul Kp/Ki) (réel, 2024 Épreuve écrite disciplinaire QC3/C5-C11, ★★★, schéma-blocs tikz 2 boucles). Passe complémentarité 2026-09-02 : les deux exercices qui dupliquaient les Questions Types de la fiche T14 (THD 2024 B10-B11 = QT1 ; ATV630 2021 Q15-18 = QT2) ont été remplacés ; provenance des données du DT6 (courants 259/314 A reconstitués du catalogue Altivar 71, OCR du sujet illisible) documentée en commentaire LaTeX. Compilé en `T14_enonces.pdf` (3 p.) / `T14_corriges.pdf` (5 p.).

## exercices/T15_exercices.tex
6 exercices sur le stockage d'energie electrique, rendus complementaires de la fiche T15 (passe 2026-09-02 : les 4 exercices qui dupliquaient les Questions Types QT1/QT2/QT3 ont ete remplaces par d'autres questions des memes sujets reels). Exercice docTech : parc de 2 batteries d'un voilier, extrait de catalogue DT6 reconstitue, energie exploitable a 70 % de decharge (reel, 2020, Etude d'un systeme d'un procede ou d'une organisation option IE, Q9/Q12/Q13). Stockage d'hydrogene du bus Hycity : masse et volume de H2 par trajet type, nombre de trajets avec 6 reservoirs de 232 L (reel, 2026 epreuve 2 d'admissibilite BAC+3, QA1/QA2, schema-bloc tikz). Comptage coulometrique du SOC et role du BMS (inedit, chronogrammes i(t)/SOC(t)). Dimensionnement d'un parc de batteries 12 V en parallele, autonomie 2 jours et DoD 80 % (reel, 2020, meme epreuve, Q14/Q15, schema circuitikz). Mesure de la quantite d'energie stockee d'une micro-STEP : non-linearite V=f(H), ecart au modele lineaire, seuils numeriques Res_plein/Res_vide (reel, 2021, Etude d'un systeme, Q21 a Q23, courbe tikz). Bilan energetique et financier sur 25 ans d'une micro-STEP solaire, cout de revient du kWh (reel, 2021, meme epreuve, Q26 a Q29). Compile en `T15_enonces.pdf`/`T15_corriges.pdf` (4 pages chacun).

## exercices/T16_exercices.tex
6 exercices sur les energies renouvelables, complementaires des Questions Types de la fiche T16 (passe complementarite 2026-09-02) : comparaison filieres PV/micro-turbine/Peltier (reel, 2022 Q19, tableau) ; surface de champ PV a partir de l'irradiance annuelle et de la chaine de rendements (reel, 2025 Q6-Q7, schema-bloc tikz) ; lecture de document technique DT5 -- datasheet panneau, raccordement serie, Pnom et surface du champ (reel, 2025 Q16, encadre docTech + question d'extraction) ; micro-centrale hydraulique au fil de l'eau (inedit, formule reelle de fiches/T16_contenu.md, schema bloc riviere->turbine->alternateur) ; bilan energetique d'une micro-STEP -- energie potentielle, rendement de stockage (reel, 2021 Q5/Q6/Q9/Q10, schema tikz pompage/turbinage) ; identification des convertisseurs CV1-CV3, MPPT et fonction de modulation f_m (reel, 2025 Q14/Q15/Q19, synoptique tikz). Compile en `T16_enonces.pdf`/`T16_corriges.pdf` (3 et 4 pages).

## exercices/T17_exercices.tex
6 exercices sur la distribution et la sécurité électrique, refondus le 2026-09-02 pour être complémentaires de la fiche T17 (les 5 exercices qui doublonnaient QT1/QT2/QT3 et le Bloc 4 de la fiche ont été remplacés par d'autres questions des mêmes sujets réels) : bilan de puissances Boucherot d'un atelier (2024 B1-B2, schéma tikz répartition 3 phases), courants des récepteurs monophasés d'un spa et choix du calibre (2017 B1.1-B1.2, valeurs authentiques du corrigé officiel), compensation d'énergie réactive par batterie de condensateurs étoile (2024 B3-B4, schéma circuitikz), déséquilibre triphasé et choix du nouvel abonnement (2017 B2.3), **docTech** choix d'un parafoudre PF et de son disjoncteur de déconnexion sur catalogue Merlin Gerin (2018 Q18-Q19, extrait DRS7 textuellement présent dans le sujet, question 1 d'extraction), réglage du courant thermique Ith d'un variateur ATV630 (2021 Q16+Q18, schéma tikz chaîne variateur-moteur-pompe). Citations jury 2018 et 2021 vérifiées verbatim. Compilé en `T17_enonces.pdf`/`T17_corriges.pdf` (4 pages chacun).

## exercices/T18_exercices.tex
6 exercices sur les circuits électroniques et composants (diode, transistor) : shunt R0 et diode de protection contre les tensions **négatives** de l'entrée ADC1 du CAN (réel, 2022, épreuve écrite disciplinaire Q26+Q27, écrêtage à −0,6 V conforme au corrigé du Rapport_Jury_2022, schéma circuitikz), rôle de l'onduleur PV et commande IGBT/MLI (réel, 2013, épreuve E1 Q48, schéma bloc), droite de charge et point de fonctionnement d'une diode (inédit, ★★, schéma + graphe caractéristique/droite de charge avec point Q), viabilité des états Q1/D1 et lois de Kirchhoff d'un hacheur batterie (inédit inspiré de 2025 Q24+Q26+Q32, schéma circuitikz buck entièrement fléché v_Q1/v_D1/i_Q1/i_D1), **exercice docTech** : dimensionnement d'une commande de relais à partir d'un extrait de datasheet BC337-25 Fairchild (inédit, ★★, encadré `docTech` avec ratings et ON characteristics constructeur, 1re question d'extraction, schéma circuitikz NPN + diode de roue libre), thyristor et angle d'amorçage pont P1 (inédit, ★★★, chronogramme tikz, formule ⟨u_S⟩=(Vm/2π)(1+cosα) redémontrée — corrige un facteur 2 manquant dans `T18_contenu.md`). Compilé en `T18_enonces.pdf`/`T18_corriges.pdf`.

## exercices/T19_exercices.tex
6 exercices sur l'AOP, banque rendue complementaire de la fiche T19_AOP.tex (aucun exercice ne rejoue les QT1/QT2/QT3) : montage suiveur conditionneur de sonde Jumo (reel, 2026, epreuve BAC3 Q B4-B5, source de courant 10 mA + RT, schema circuitikz) ; **docTech** lecture du document technique DT10 - thermocouple type J, eAB de -1 a 10,8 mV, profil 4-20 mA - puis calcul de V4 = 337,7 eAB + 1,34 (reel, 2024, epreuve ecrite disciplinaire Q E5, resultats 1 V / 5 V confirmes par le Rapport_Jury_2024) ; etage de decalage par theoreme de Millman V4=V3+Ve (reel, 2024 Q E4, schema circuitikz) ; tableau de synthese choix de montage AOP (inedit) ; choix et justification d'un montage du document technique DTB3 pour realiser {amplificateur + conditionneur} (reel, 2026 Q B7-B8, demonstration du non-inverseur, selection du soustracteur) ; dimensionnement inverse du comparateur a hysteresis du robot Bakus - largeur d'hysteresis et demi-somme des seuils donnent R2 = 149 kOhm et Vref2 = 2,416 V, verification des valeurs normalisees 150 kOhm / 2,42 V (reel, 2023, epreuve ecrite disciplinaire Q F9-F10, schema circuitikz contre-reaction positive + trace du cycle). Gradation monotone 1,1,2,2,2,3. Schemas AOP via le node circuitikz `op amp` (anchors `.+`/`.-`/`.out`). Compile en `T19_enonces.pdf` (3 p.) / `T19_corriges.pdf` (4 p.).

## exercices/AUDIT_EXERCICES_2026.md
Rapport d'audit qualité multi-agent des 19 notions T01–T19 de la banque d'exercices (2026-08-25) — audit seul, aucun `.tex` modifié. Pré-passe scriptée (38 compilations + greps), 19 agents d'audit, 32 contre-vérifications adversariales (30 constats confirmés, 2 réfutés). Score moyen 72,1/100 (min 59 T14, max 83 T13/T18). Contient : classement, 10 problèmes systémiques (citations jury fabriquées ×9 notions, recouvrement fiches 18/19, 0 docTech, 15 erreurs de calcul confirmées, 8 schémas faux…), listes consolidées, détail par notion, note de méthode (points à relire humainement : T17 ex2 Ru/Xu, schémas, THD 61,4 %).

## FILE_EXERCICES.md
File d'attente des notions T01–T30 à traiter pour la banque d'exercices (mode file d'attente du skill `exercices-capet`). T01–T19 cochées.

## PROGRESSION_EXERCICES.md
Tableau de bord de la banque d'exercices, par domaine, régénéré par scan de `exercices/*.tex`. État : 19/30 notions, 103 exercices.

## .claude/skills/exercices-capet/SKILL.md
Skill projet : génération des exercices d'entraînement CAPET (mode file d'attente ou à la demande), sources sujets réels/rapports jury, format LaTeX unique énoncé+corrigé via `exoBox`/`\tcbline`.

## fiches/T{nn}_contenu.md (T01–T30)
Fichiers sources documentaires pour chaque fiche — formules, questions types, citations jury.

| Fichier | Thème |
|---|---|
| T01_contenu.md | Grandeurs électriques, électrocinétique |
| T02_contenu.md | Puissance en régime alternatif sinusoïdal |
| T03_contenu.md | Représentation complexe, impédances |
| T04_contenu.md | Harmoniques réseau, THD, puissance déformante |
| T05_contenu.md | Phénomènes thermiques |
| T06_contenu.md | Transformateur (monophasé et triphasé) |
| T07_contenu.md | Hacheurs (1, 2 et 4 quadrants) |
| T08_contenu.md | Redresseurs (monophasé et triphasé) |
| T09_contenu.md | Onduleurs (monophasé et triphasé) |
| T10_contenu.md | Mécanique : cinématique, forces, moments, réducteurs |
| T11_contenu.md | Machine à courant continu (MCC) |
| T12_contenu.md | Machine synchrone et brushless (PMSM / BLDC) |
| T13_contenu.md | Machine asynchrone (MAS) |
| T14_contenu.md | Variation de vitesse et de couple des machines |
| T15_contenu.md | Stockage d'énergie électrique |
| T16_contenu.md | Énergies renouvelables : photovoltaïque, hydraulique, éolien |
| T17_contenu.md | Distribution et sécurité électrique, régimes de terre |
| T18_contenu.md | Circuits électroniques, composants (diode, transistor) |
| T19_contenu.md | AOP (amplificateur opérationnel) |
| T20_contenu.md | Régime sinusoïdal, filtres 1er/2e ordre (électronique) |
| T21_contenu.md | Fonctions de transfert, diagramme de Bode |
| T22_contenu.md | CAN/CNA, Numérisation, Échantillonnage |
| T23_contenu.md | Capteurs et Conditionnement du Signal |
| T24_contenu.md | Systèmes Embarqués, FPGA, VHDL |
| T25_contenu.md | Transmission Numérique, Modulations |
| T26_contenu.md | Modélisation des systèmes linéaires (automatique) |
| T27_contenu.md | Systèmes bouclés, correcteurs, stabilité |
| T28_contenu.md | Logique combinatoire |
| T29_contenu.md | Logique séquentielle, GRAFCET |
| T30_contenu.md | Mesurage, instrumentation, schématisation |

---

## colab_convert_pdfs.py
Script Google Colab pour convertir tous les PDFs en Markdown.
- `PdfConverter(config)` — convertit un PDF en Markdown via Marker (GPU)
- `text_from_rendered(rendered)` — extrait texte + images du résultat Marker
- Fallback automatique sur `pymupdf4llm` si Marker échoue

## PDFs_CAPET_SII_IE.zip
Archive source contenant les 41 PDFs organisés par année (2013–2026).

---

## docs/CAPET_SII_IE/06_PDFs_Originaux/

PDFs officiels organisés par année. Chaque sous-dossier `{doc_name}/` contient le PDF et éventuellement son `.md` converti (batch précédent).

| Année | Documents disponibles |
|---|---|
| 2013 | E1_Sujet, E1_Corrige |
| 2014 | E1_Sujet, E1_Corrige |
| 2015 | E1_Sujet |
| 2016 | E1_Sujet, E1_Corrige |
| 2017 | E1_Sujet, E1_Corrige, E2_Sujet, E2_Corrige |
| 2018 | E1_Sujet, E2_Sujet, Rapport_Jury |
| 2019 | E1_Sujet, E2_Sujet, Rapport_Jury |
| 2020 | E1_Sujet, E2_Sujet, Rapport_Jury |
| 2021 | E1_Sujet, E2_Sujet, Rapport_Jury |
| 2022 | E1_Sujet, Rapport_Jury *(E2 manquant dans ce dossier)* |
| 2023 | E1_Sujet, Rapport_Jury *(E2 manquant dans ce dossier)* |
| 2024 | E1_Sujet, E2_Appliquee_Commune, E2_Disciplinaire_IE, Rapport_Jury |
| 2025 | E1_Sujet, E2_Appliquee_Commune, E2_Disciplinaire_IE, Rapport_Jury |
| 2026 | E1_Sujet, E2_Sujet_BAC3 |

Fichiers `.md` présents dans ce dossier : 26 (2013–2023 partiels).

---

## docs/CAPET_SII_IE/07_Ecrits_1ere_session/

Regroupement des écrits CAPET SII de la 1ère session 2025 (sans rapport jury), pour accès direct.

- `PDF/E1_Sujet_2025.pdf` — Épreuve commune E1 sujet
- `PDF/E2_Appliquee_Commune_2025.pdf` — Épreuve appliquée commune E2
- `PDF/E2_Disciplinaire_IE_2025.pdf` — Épreuve disciplinaire IE
- `Markdown/E1_Sujet_2025.md` — Conversion Markdown de E1
- `Markdown/E2_Appliquee_Commune_2025.md` — Conversion Markdown de E2 appliquée commune
- `Markdown/E2_Disciplinaire_IE_2025.md` — Conversion Markdown de E2 disciplinaire IE

---

## docs/CAPET_SII_IE/08_Impression_E1_4_dernières_annees/

Dossier prêt à imprimer avec uniquement les sujets E1 des 4 années les plus récentes.

- `01-2026-E1_Sujet_2026.pdf` — E1 session 2026
- `02-2025-E1_Sujet_2025.pdf` — E1 session 2025
- `03-2024-E1_Sujet_2024.pdf` — E1 session 2024
- `04-2023-E1_Sujet_2023.pdf` — E1 session 2023

---

## docs/CAPET_Markdown-20260629T134311Z-3-001/CAPET_Markdown/

Résultat du dernier batch de conversion Colab (2026-06-29). Couverture complète : 41 fichiers `.md`.
Même arborescence que `06_PDFs_Originaux/`. À utiliser comme source de référence la plus complète.

### 2013
- `2013/E1_Sujet_2013_commun_SII/E1_Sujet_2013_commun_SII.md` — Épreuve commune E1 sujet
- `2013/E1_Corrige_2013_commun_SII/E1_Corrige_2013_commun_SII.md` — Épreuve commune E1 corrigé

### 2014
- `2014/E1_Sujet_2014_commun_SII/E1_Sujet_2014_commun_SII.md` — Épreuve commune E1 sujet
- `2014/E1_Corrige_2014_commun_SII/E1_Corrige_2014_commun_SII.md` — Épreuve commune E1 corrigé

### 2015
- `2015/E1_Sujet_2015_commun_SII/E1_Sujet_2015_commun_SII.md` — Épreuve commune E1 sujet

### 2016
- `2016/E1_Sujet_2016_commun_SII/E1_Sujet_2016_commun_SII.md` — Épreuve commune E1 sujet
- `2016/E1_Corrige_2016_commun_SII/E1_Corrige_2016_commun_SII.md` — Épreuve commune E1 corrigé

### 2017
- `2017/E1_Sujet_2017/E1_Sujet_2017.md` — Épreuve commune E1 sujet
- `2017/E1_Corrige_2017/E1_Corrige_2017.md` — Épreuve commune E1 corrigé
- `2017/E2_Sujet_2017/E2_Sujet_2017.md` — Épreuve disciplinaire IE sujet
- `2017/E2_Corrige_2017/E2_Corrige_2017.md` — Épreuve disciplinaire IE corrigé

### 2018
- `2018/E1_Sujet_2018/E1_Sujet_2018.md` — Épreuve commune E1 sujet
- `2018/E2_Sujet_2018/E2_Sujet_2018.md` — Épreuve disciplinaire IE sujet
- `2018/Rapport_Jury_2018/Rapport_Jury_2018.md` — Rapport jury

### 2019
- `2019/E1_Sujet_2019/E1_Sujet_2019.md` — Épreuve commune E1 sujet
- `2019/E2_Sujet_2019/E2_Sujet_2019.md` — Épreuve disciplinaire IE sujet
- `2019/Rapport_Jury_2019/Rapport_Jury_2019.md` — Rapport jury

### 2020
- `2020/E1_Sujet_2020/E1_Sujet_2020.md` — Épreuve commune E1 sujet
- `2020/E2_Sujet_2020/E2_Sujet_2020.md` — Épreuve disciplinaire IE sujet
- `2020/Rapport_Jury_2020/Rapport_Jury_2020.md` — Rapport jury

### 2021
- `2021/E1_Sujet_2021/E1_Sujet_2021.md` — Épreuve commune E1 sujet
- `2021/E2_Sujet_2021/E2_Sujet_2021.md` — Épreuve disciplinaire IE sujet
- `2021/Rapport_Jury_2021/Rapport_Jury_2021.md` — Rapport jury

### 2022
- `2022/E1_Sujet_2022/E1_Sujet_2022.md` — Épreuve commune E1 sujet
- `2022/E2_Appliquee_Commune_2022/E2_Appliquee_Commune_2022.md` — Épreuve appliquée commune E2
- `2022/E2_Disciplinaire_IE_2022/E2_Disciplinaire_IE_2022.md` — Épreuve disciplinaire IE
- `2022/Rapport_Jury_2022/Rapport_Jury_2022.md` — Rapport jury

### 2023
- `2023/E1_Sujet_2023/E1_Sujet_2023.md` — Épreuve commune E1 sujet
- `2023/E2_Appliquee_Commune_2023/E2_Appliquee_Commune_2023.md` — Épreuve appliquée commune E2
- `2023/E2_Disciplinaire_IE_2023/E2_Disciplinaire_IE_2023.md` — Épreuve disciplinaire IE
- `2023/Rapport_Jury_2023/Rapport_Jury_2023.md` — Rapport jury

### 2024
- `2024/E1_Sujet_2024/E1_Sujet_2024.md` — Épreuve commune E1 sujet
- `2024/E2_Appliquee_Commune_2024/E2_Appliquee_Commune_2024.md` — Épreuve appliquée commune E2
- `2024/E2_Disciplinaire_IE_2024/E2_Disciplinaire_IE_2024.md` — Épreuve disciplinaire IE
- `2024/Rapport_Jury_2024/Rapport_Jury_2024.md` — Rapport jury

### 2025
- `2025/E1_Sujet_2025/E1_Sujet_2025.md` — Épreuve commune E1 sujet
- `2025/E2_Appliquee_Commune_2025/E2_Appliquee_Commune_2025.md` — Épreuve appliquée commune E2
- `2025/E2_Disciplinaire_IE_2025/E2_Disciplinaire_IE_2025.md` — Épreuve disciplinaire IE
- `2025/Rapport_Jury_2025/Rapport_Jury_2025.md` — Rapport jury

### 2026
- `2026/E1_Sujet_2026/E1_Sujet_2026.md` — Épreuve commune E1 sujet (session en cours)
- `2026/E2_Sujet_2026_BAC3/E2_Sujet_2026_BAC3.md` — Épreuve BAC3 (nouveau format 2026)

---

*Chemin complet : tous les chemins ci-dessus sous `docs/CAPET_Markdown-20260629T134311Z-3-001/CAPET_Markdown/docs/CAPET_SII_IE/06_PDFs_Originaux/`*

---

## manuel/main.tex
Point d'entrée du manuel de révision imprimable (assemblage cours + exercices, 378 p.).
- couverture, sommaire `hyperref`, 4 parties, annexe A des corrigés
- `\CAPETOUVRENOTION{code}{titre}{couleur}` — saut de page + entrée de sommaire + `\CAPETNOTION`
- `\CAPETBANDEAUEXOS{code}{titre}` — bandeau d'ouverture de la section exercices
- `\subimport{../fiches/}{...}` et `\subimport{../exercices/}{...}` — inclusion sans duplication
- compilation : `pdflatex main.tex` ×3 depuis `manuel/`

## manuel/parties.tex
Intercalaires de partie du manuel.
- `\CAPETPARTIE{numéro}{titre}{sous-titre}{couleur}` — page de garde de partie

## fiches/preamble.tex (ajouts 2026-09-20)
- `\CAPETSHOW` à 3 modes (énoncés / corrigés / manuel) — voir CLAUDE.md
- `\CAPETSHOWEXO`, `\CAPETANNEXE`, `\CAPETNOTION`, `\CAPETLIBELLEENONCES`
- compteurs `CAPETexo` / `CAPETannexe` — numérotation continue des exercices du manuel
- `\degree` redéfini sous `\AtBeginDocument` (conflit hyperref, cf. CLAUDE.md)

---

## docs/superpowers/plans/2026-09-21-app-revision-capet.md
Plan d'implémentation (14 tasks) de l'app de révision : entraîneur formules /
schémas / conditions d'application. Non encore implémenté.
- Décisions de cadrage verrouillées (écrit mars 2026, révélation + auto-notation,
  extraction auto depuis les sources, pas d'encadrés jury en v1)
- Tableau des 16 défauts trouvés en revue adverse et corrigés avant publication
- Invariants de non-régression : 191 formules tableau, 153 formules bloc,
  199 pièges, 31 schémas — tout écart signale un parseur cassé
