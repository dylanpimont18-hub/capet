# CAPET SII IE — Index ressources

Racine : `docs/CAPET_SII_IE/` · 36 fichiers · Sessions 2015–2025

## Structure

```
00_Programme_Referentiel/   ← programme officiel 2026
01_Sujets/{année}/          ← 22 sujets (E1 commune + E2 disciplinaire)
02_Rapports_Jury/           ← 6 rapports jury (2019,2020,2022–2025)
03_Corriges/                ← 6 corrigés (2016,2017,2021)
tableau_themes_capet.md     ← matrice thèmes × années
formulaire_capet.md         ← ~130 formules par domaine
```

---

## 00 — Programme

`00_Programme_Referentiel/Programme_CAPET_SII_Electrique_Session_2026/Programme_CAPET_SII_Electrique_Session_2026.md`
Programme officiel BAC+3 session 2026. Thèmes : Énergie (MCC/MAS/synchrone, hacheurs, redresseurs, onduleurs, ENR, distribution) · Électronique (analogique, numérique, FPGA/VHDL, RF) · Automatique · Automatisme (API, GRAFCET) · Informatique (µC, I2C/SPI)

---

## 01 — Sujets

Chemin type : `01_Sujets/{année}/Epreuve{N}_{Nom}/{Nom}.md`
E1 = épreuve commune pluritechnique (EDE STI2D) · E2 = épreuve disciplinaire Ingénierie Électrique

| Année | E1 — Système | E2 — Système |
|---|---|---|
| 2015 | Shelter déployable militaire | École Kolbsheim — bâtiment énergie positive (PV+géothermie) |
| 2016 | Maison active énergie positive (PAC+PV, Alsace) | Éclairage autonome abri tramway (solaire) |
| 2017 | Métro MF 2000 RATP — traction électrique | Spa Sydney Premium — balnéothérapie (thermique/régulation) |
| 2018 | Catamaran solaire SunSeaRider | Éclairage public LED — Dampmart |
| 2019 | Transport urbain câble POMA (climatisation tropicale) | Transformation rame métro / bains thermaux |
| 2020 | Robots Skypod Exotec — entrepôt automatisé | Dessalinisateur eau mer DUO 60 AC&DC |
| 2021 | Extraction nickel — Vale, Nouvelle-Calédonie | Micro-STEP solaire pompage-turbinage (Corse) |
| 2022 | Réseau chaleur urbain — cogénération | Banc essais automobile Autoscan Fi |
| 2023 | Commune STI2D 2023 | Traitement air serre agricole |
| 2024 | Commune STI2D 2024 | Extracteur air — capsule Urbanloop |
| 2025 | Commune STI2D 2025 | Électrification site isolé (PV + stockage) |

---

## 02 — Rapports de jury

Chemin type : `02_Rapports_Jury/Rapport_Jury_{année}/Rapport_Jury_{année}.md`
Contenu type : stats · correction écrite · épreuve de leçon · entretien

| Année | Sujets couverts |
|---|---|
| 2019 | Transport câble + Spa Sydney |
| 2020 | Exotec + Dessalinisateur |
| 2022 | Réseau chaleur + Banc essai |
| 2023 | Traitement air serre |
| 2024 | Extracteur air Urbanloop |
| 2025 | Site isolé |

---

## 03 — Corrigés

Chemin type : `03_Corriges/{année}_Epreuve{N}_{Nom}/{Nom}.md`

| Fichier | Contenu clé |
|---|---|
| 2016_E1 Maison Active | Bilan thermique, PV, PAC |
| 2016_E2 Tramway | Enjeux pédagogiques STI2D, éclairage solaire |
| 2017_E1 Métro MF2000 | Cinématique roues-rail, puissance, inertie |
| 2017_E2 Spa Sydney | Régulation thermique, GRAFCET |
| 2021_E1 Nickel | Mécanique fluides, couple, viscosité |
| 2021_E2 STEP | Dimensionnement PV, rendement, bilan éco |

---

## Outils de synthèse

**`tableau_themes_capet.md`** — Matrice 30 thèmes × 22 épreuves (2015–2025)
- Table 1 : intensité 🔴 Central / 🟠 Important / 🟡 Mentionné / ⬜ Absent + colonne Moyenne
- Table 2 : binaire 🟢 / vide + colonne Total (/22)
- Thèmes top : T02 Puissance AC · T03 Thermique · T11 Variation vitesse · T13 ENR · T14 Distribution · T21 Modélisation · T24 Correcteurs · T30 Mécanique

**`formulaire_capet.md`** — ~130 formules · 17 domaines · sources : corrigés + rapports jury 2019–2025
- Colonnes : Formule (LaTeX) · Description · Donnée sujet ✅/❌ · Fréquence
- Domaines : Thermique · PAC/Fick · ENR · Électrotechnique · Câblage · Hacheurs · MAS · Automatique · Capteurs · Mécanique · RDM · Hydraulique · Économique
