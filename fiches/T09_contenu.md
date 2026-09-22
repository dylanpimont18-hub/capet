# T09 — Onduleurs (monophasé et triphasé)

---

## 1. FORMULES ET COURS

| Formule LaTeX | Contexte | Fréquence | Donnée sujet ou mémoire |
|---|---|---|---|
| $V_{eff,pleine\ onde} = V_{DC}$ | Valeur efficace onduleur monophasé pleine onde (tension créneau $\pm V_{DC}$) | Très fréquent | Identique à la tension du bus DC |
| $V_{eff,composée} = \sqrt{\dfrac{2}{3}} \cdot V_{DC} \approx 0{,}816 \cdot V_{DC}$ | Valeur efficace tension composée onduleur triphasé pleine onde | Fréquent | Commande $120°$ (6 états) |
| $\mathrm{THD} = \dfrac{\sqrt{\displaystyle\sum_{n=2}^{\infty} V_n^2}}{V_1}$ | Taux de distorsion harmonique total | Très fréquent | $V_n$ = valeur efficace harmonique de rang $n$ |
| $\mathrm{THD}_{pleine\ onde,mono} = \sqrt{\dfrac{\pi^2}{8} - 1} \approx 0{,}484$ | THD théorique onduleur monophasé pleine onde | Fréquent | Valeur de cours ; sujets donnent $\approx 0{,}48$ |
| $V_n = \dfrac{4V_{DC}}{n\pi}$ (n impair) | Harmoniques d'une tension en créneau (pleine onde) | Fréquent | Rangs impairs : $n = 1, 3, 5, 7, \ldots$ |
| $\mathrm{THD} = \dfrac{\sqrt{V_3^2 + V_5^2 + V_7^2 + \ldots}}{V_1}$ | Calcul pratique THD (harmoniques mesurés) | Très fréquent | Numériquement depuis le spectre donné en sujet |
| $m_a = \dfrac{\hat{V}_{ref}}{\hat{V}_{porteuse}}$ | Indice de modulation d'amplitude (MLI sinusoïdale) | Courant | $m_a \leq 1$ : linéaire ; $m_a > 1$ : surmodulation |
| $m_f = \dfrac{f_{porteuse}}{f_{fondamental}}$ | Indice de modulation de fréquence (MLI) | Courant | Ex. $f_p = 6\ \mathrm{kHz}$, $f = 50\ \mathrm{Hz}$ → $m_f = 120$ |
| $\hat{V}_{1,MLI} = m_a \cdot \dfrac{V_{DC}}{2}$ (monophasé) | Amplitude du fondamental en MLI (pleine onde) | Courant | Valide pour $m_a \leq 1$ |
| Puissance apparente : $S = V_{eff} \cdot I_{eff}$ | Bilan puissance onduleur | Courant | $P = S \cos\varphi$ |
| Puissance déformante : $D = S \cdot \mathrm{THD} / \sqrt{1+\mathrm{THD}^2}$ | Puissance liée aux harmoniques | Courant | Lien $S^2 = P^2 + Q^2 + D^2$ |
| Fréquence statorique MS : $f_s = p \cdot n_s / 60$ | Fréquence de commande onduleur triphasé (MS) | Fréquent | $p$ = nb paires pôles, $n_s$ = vitesse en tr/min |
| Tension composée triphasée étoile : $U = \sqrt{3} \cdot V$ | Relation tension simple/composée | Très fréquent | Onduleur triphasé étoile |

---

## 2. QUESTIONS TYPES

### Q1 — Sujet 2024, E2D Partie B, B11–B13 : onduleur MLI vs pleine onde, THD, conformité IEC

**Source :** `2024/E2_Disciplinaire_IE_2024/E2_Disciplinaire_IE_2024.md`, Questions B11–B13

**Énoncé :** Un variateur de vitesse pour extracteur d'air (lycée les Lombards, Troyes) contient un onduleur triphasé. Le spectre harmonique est mesuré pour deux cas :
- Cas 1 (pleine onde) : $V_1 = 170\ \mathrm{V}$, $V_5 = 95\ \mathrm{V}$, $V_7 = 27\ \mathrm{V}$, $V_{11} = 27\ \mathrm{V}$, $V_{13} = 20\ \mathrm{V}$.
- Cas 2 (MLI, $f_p = 6\ \mathrm{kHz}$) : $V_1 = 170\ \mathrm{V}$, $V_{119} = 37\ \mathrm{V}$, $V_{121} = 22\ \mathrm{V}$.
Calculer le THD dans chaque cas et conclure par rapport à la norme IEC/EN 61000-2-2 ($\mathrm{THD} < 25\ \%$).

**Corrigé :**
- Cas 1 :
  $$\mathrm{THD}_1 = \frac{\sqrt{95^2 + 27^2 + 27^2 + 20^2}}{170} = \frac{\sqrt{9025 + 729 + 729 + 400}}{170} = \frac{\sqrt{10883}}{170} = \frac{104{,}3}{170} \approx 0{,}59 = 59\ \%$$
  Non conforme ($59\ \% > 25\ \%$).
- Cas 2 :
  $$\mathrm{THD}_2 = \frac{\sqrt{37^2 + 22^2}}{170} = \frac{\sqrt{1369 + 484}}{170} = \frac{\sqrt{1853}}{170} = \frac{43{,}0}{170} \approx 0{,}25 = 25\ \%$$
  Conforme (limite atteinte).
- **Conclusion (B12–B13) :** La MLI repousse les harmoniques à haute fréquence ($\approx 6\ \mathrm{kHz}$, rangs $119$, $121$) facilement filtrables par les inductances de la machine ; la pleine onde génère des harmoniques d'ordre faible ($5$, $7$) difficiles à filtrer.

---

### Q2 — Sujet 2025, E2D CV3-2 : onduleur monophasé pleine onde, tension efficace et THD

**Source :** `2025/E2_Disciplinaire_IE_2025/E2_Disciplinaire_IE_2025.md`, CV3-2

**Énoncé :** L'onduleur CV3-2 est un onduleur monophasé pleine onde ($V_{DC} = 230\ \mathrm{V}$). La charge de distribution est $S_{distri} = 3\ \mathrm{kVA}$. Le spectre donne $\mathrm{THD} = 0{,}48$. Calculer la valeur efficace $V_{distri}$, puis la puissance active $P_{distri}$ et la puissance réactive $Q_{distri}$ absorbées par une charge résistive pure.

**Corrigé :**
- Pleine onde monophasé : $V_{eff} = V_{DC} = 230\ \mathrm{V}$
- Pour une charge purement résistive : $\cos\varphi_1 = 1$ (fondamental en phase avec courant fondamental)
- Puissance active : $P = V_{eff}^2 / R$ ; mais depuis $S = V_{eff} \cdot I_{eff}$ et $P = V_1 I_1 \cos\varphi_1$
- Avec $\mathrm{THD} = 0{,}48$ : le courant a des harmoniques, mais pour une charge $R$ pure, toute la puissance dissipée est active.
  $$P_{distri} = \frac{V_{eff}^2}{R} = S_{distri} = 3\ \mathrm{kW} \quad (R\ \mathrm{pure,}\ \cos\varphi = 1)$$
- Puissance réactive fondamentale $Q_{distri} = 0$ (charge résistive), mais puissance déformante $D \neq 0$.

---

### Q3 — Sujet 2024, E2 Appliquée Commune : onduleur triphasé pour machine synchrone (Urbanloop)

**Source :** `2024/E2_Appliquee_Commune_2024/E2_Appliquee_Commune_2024.md`, machine synchrone

**Énoncé :** Une machine synchrone triphasée à aimants permanents ($p = 14$ paires de pôles) est alimentée par un onduleur triphasé depuis un bus DC $72\ \mathrm{V}$. La capsule roule à $V_0 = 60\ \mathrm{km/h}$. Calculer la fréquence statorique $f_0$ à imposer à l'onduleur.

**Corrigé :**
- Vitesse angulaire mécanique : $\omega_m = 2\pi f_s / p$, soit $f_s = p \cdot \omega_m / (2\pi)$
- Depuis $V_0 = 60\ \mathrm{km/h} = 16{,}67\ \mathrm{m/s}$ et le rayon de la roue (données sujet), calculer $n_m$ en tr/min, puis :
  $$f_s = \frac{p \cdot n_m}{60} = \frac{14 \cdot n_m}{60}$$
- Couplage étoile : la tension de phase = $V_{DC}/\sqrt{3}$ en commande MLI ou $V_{DC}$ en pleine onde selon le schéma.

---

### Q4 — Rapport Jury 2024, correction B11–B13 : justification choix MLI

**Source :** `2024/Rapport_Jury_2024/Rapport_Jury_2024.md`, corrections B11–B13

**Énoncé :** Justifier pourquoi la MLI à $6\ \mathrm{kHz}$ est préférable à la commande pleine onde pour l'onduleur d'un variateur de vitesse alimentant une machine asynchrone.

**Corrigé (d'après rapport jury) :**
- La MLI déplace les harmoniques à haute fréquence ($n \approx m_f = 120$) : $f_{harm} \approx 6\ \mathrm{kHz}$.
- Ces harmoniques HF sont naturellement atténués par l'effet inductif des enroulements de la machine ($Z = j\omega L \rightarrow$ très élevé à $6\ \mathrm{kHz}$).
- La pleine onde génère des harmoniques de rang $5, 7$ ($250\ \mathrm{Hz}$, $350\ \mathrm{Hz}$) moins atténués → pertes supplémentaires et couple oscillant.
- Norme IEC/EN 61000-2-2 : $\mathrm{THD} < 25\ \%$ → seule la MLI est conforme ($\mathrm{THD} = 25\ \%$ vs $59\ \%$).

---

### Q5 — Rapport Jury 2025, correction Q14 : identification des convertisseurs dans la chaîne de conversion

**Source :** `2025/Rapport_Jury_2025/Rapport_Jury_2025.md`, Q14

**Énoncé :** Dans la chaîne de conversion du site isolé de Mafate : PV → CV1 → bus DC → CV3 → réseau local $230\ \mathrm{V}$. Identifier la nature de CV1, CV2 et CV3.

**Corrigé (rapport jury) :**
- CV1 = **Hacheur** (adapte la tension PV variable au bus DC)
- CV2 = **Redresseur** (batterie → bus DC dans certains modes)
- CV3 = **Onduleur** (bus DC → $230\ \mathrm{V}$ AC $50\ \mathrm{Hz}$ pour le réseau local)
- Le jury note : "les fonctions explicites doivent être nommées et justifiées, pas seulement schématisées".

---

## 3. ATTENTES DU JURY

| Source | Citation directe | Implication pour le candidat |
|---|---|---|
| `2024/Rapport_Jury_2024.md` | Corrections B11/B12/B13 : "THD cas 1 (pleine onde) = 0,59 ; THD cas 2 (MLI 6kHz) = 0,25 — confirmer conformité norme IEC/EN 61000-2-2 < 25 %" | Savoir calculer le THD depuis un spectre harmonique numérique donné en sujet, et **conclure** par rapport à une norme chiffrée |
| `2024/Rapport_Jury_2024.md` | "B13 : MLI limite ondulations THD, harmoniques HF supprimés par effet inductif enroulements machine" | Justifier physiquement le filtrage naturel par la machine, pas seulement citer le résultat |
| `2025/Rapport_Jury_2025.md` | "Q14 : les fonctions explicites doivent être nommées et justifiées" | Face à un schéma de chaîne de conversion, nommer chaque bloc (hacheur, redresseur, onduleur) et justifier par le sens du flux d'énergie (DC→AC = onduleur, AC→DC = redresseur, DC→DC = hacheur) |
| `2025/Rapport_Jury_2025.md` | "De nombreux candidats ne maîtrisent pas les lois basiques de l'électricité" | Pour l'onduleur : maîtriser $V_{eff} = V_{DC}$ (pleine onde), la décomposition de Fourier en créneaux ($V_n = 4V_{DC}/n\pi$), et le lien $\mathrm{THD} = f(\text{spectre})$ |
| `2023/Rapport_Jury_2023.md` | "Asservissement : trop peu de candidats l'ont traitée de manière satisfaisante" | La commande MLI et la boucle d'asservissement de l'onduleur (fréquence, amplitude) sont régulièrement demandées |

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique | Source |
|---|---|---|
| Tension bus DC onduleur monophasé | $V_{DC} = 230\ \mathrm{V}$ | 2025 E2D |
| Valeur efficace sortie pleine onde | $V_{eff} = 230\ \mathrm{V}$ (= $V_{DC}$) | 2025 E2D |
| THD onduleur monophasé pleine onde (mesuré) | $\mathrm{THD} = 0{,}48$ | 2025 E2D |
| THD onduleur triphasé pleine onde (calculé, norme) | $\mathrm{THD} = 0{,}59 = 59\ \%$ | 2024 E2D |
| THD onduleur triphasé MLI ($f_p = 6\ \mathrm{kHz}$) | $\mathrm{THD} = 0{,}25 = 25\ \%$ | 2024 E2D |
| Limite THD norme IEC/EN 61000-2-2 | $25\ \%$ | 2024 E2D |
| Fréquence porteuse MLI variateur | $f_p = 6\ \mathrm{kHz}$ | 2024 E2D |
| Puissance apparente distribution onduleur | $S = 3\ \mathrm{kVA}$ | 2025 E2D |
| Machine asynchrone variateur vitesse | $N = 1400\ \mathrm{tr/min}$, $p = 2$, $V_S = 230\ \mathrm{V}$, $\cos\varphi = 0{,}85$ | 2024 E2D |
| Paires de pôles MS onduleur (Urbanloop) | $p = 14$ | 2024 E2A |
| Bus DC onduleur triphasé (Urbanloop) | $72\ \mathrm{V}$ | 2024 E2A |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

1. **$V_{eff}$ pleine onde = $V_{DC}$** : la tension en créneau $\pm V_{DC}$ a une valeur efficace égale à $V_{DC}$ (carré toujours égal à $V_{DC}^2$ quelle que soit la phase). Certains candidats appliquent $V_{eff} = V_{DC}/\sqrt{2}$ (confusion avec sinusoïde).

2. **THD en valeur relative** : $\mathrm{THD} = \sqrt{\sum V_n^2} / V_1$ — le dénominateur est le **fondamental** $V_1$, pas la valeur efficace totale. Erreur fréquente : diviser par $V_{eff}$ total.

3. **Harmoniques présents en pleine onde triphasé** : pour un onduleur triphasé équilibré, les rangs $3, 9, 15, \ldots$ (multiples de 3) sont absents des tensions composées. Rangs présents : $1, 5, 7, 11, 13, \ldots$ ($6k \pm 1$).

4. **MLI : confondre $m_f$ et $m_a$** : $m_a$ contrôle l'amplitude du fondamental ; $m_f$ contrôle la localisation fréquentielle des harmoniques. Les harmoniques MLI apparaissent autour de $m_f$ et ses multiples.

5. **Fréquence de commande de l'onduleur triphasé pour une machine** : la vitesse mécanique $n_m$ impose $f_s = p \cdot n_m / 60$. L'onduleur doit générer exactement cette fréquence statorique.

6. **Onduleur en îlotage vs connecté réseau** : en mode îlotage (site isolé, 2025 E2D), l'onduleur doit lui-même fixer fréquence et tension ($f = 50\ \mathrm{Hz}$, $V = 230\ \mathrm{V}$). En mode connecté réseau, il est synchronisé sur le réseau.

7. **Pont en H monophasé** : les 4 transistors doivent être commandés avec complémentarité et temps mort (dead time) pour éviter les courts-circuits de bras. Ce temps mort n'est généralement pas demandé au CAPET mais peut être mentionné.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

| Thème associé | Articulation |
|---|---|
| **T08 — Redresseurs** | Dans un variateur de vitesse, la chaîne est : Redresseur PD6 → bus DC → Onduleur MLI triphasé. La tension DC $V_{DC}$ issue du redresseur est la tension d'alimentation de l'onduleur. |
| **T07 — Hacheurs** | Dans un système PV, la chaîne est : Panneaux → Hacheur Boost → bus DC → Onduleur triphasé. Le hacheur MPPT maintient $V_{DC}$ constant pour l'onduleur. |
| **T02 — Machine asynchrone** | L'onduleur MLI triphasé est le convertisseur d'un variateur de vitesse MAS. La fréquence de sortie de l'onduleur détermine la vitesse de la machine. |
| **T03 — Machine synchrone à aimants permanents (MSAP)** | L'onduleur triphasé alimente la MSAP en commande vectorielle ou en pleine onde. La fréquence statorique est imposée par l'onduleur selon la vitesse voulue ($f_s = p \cdot n_m/60$). |
| **T05 — Qualité de l'énergie / CEM** | Le THD de l'onduleur est le critère principal de qualité. La MLI réduit les harmoniques d'ordre faible mais génère des harmoniques HF → filtres nécessaires. |
| **T14 — Énergie renouvelable / MPPT** | L'onduleur de couplage réseau (grid-tie) ou d'îlotage est la brique finale de tout système PV ou éolien ; son fonctionnement en pleine onde vs MLI change radicalement le THD injecté sur le réseau. |
