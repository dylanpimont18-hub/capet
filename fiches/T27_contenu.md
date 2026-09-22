# T27 — Systèmes bouclés, correcteurs, stabilité
## Contenu documentaire extrait des 41 fichiers Markdown CAPET SII IE (2013–2026)

---

## 1. FORMULES ET COURS

### 1.1 Structure d'un asservissement

```
                     ε(p)
Vref(p) --[+]--► C(p) --► H_process(p) --► V(p)
          [-]                                 |
           ◄─────── H_capteur(p) ◄────────────┘
```

- **FTBO** (fonction de transfert en boucle ouverte) : $H_{BO}(p) = C(p)\,H_{process}(p)\,H_{capteur}(p)$
- **FTBF** (boucle fermée) : $H_{BF}(p) = \dfrac{H_{BO}(p)}{1 + H_{BO}(p)}$ (retour unitaire)

### 1.2 Performances d'un asservissement

**Précision en régime permanent :**
- Erreur statique : $\varepsilon_s = \lim_{t\to\infty} \varepsilon(t) = \lim_{p\to 0} p\,\varepsilon(p)$
- Pour un échelon d'amplitude $E_0$ : $\varepsilon_s = \dfrac{E_0}{1 + H_{BO}(0)}$
- Si la FTBO contient un intégrateur ($p$ au dénominateur) : $\varepsilon_s = 0$ (erreur nulle)

**Rapidité :**
- Temps de réponse à 5 % : $t_{R5\%}$ (lié à $\omega_0$ par $t_{R5\%} \approx 3\tau$ pour 1er ordre)
- Bande passante : pulsation $\omega_{BP}$ pour laquelle $|H_{BF}| = -3$ dB

**Dépassement :**
$$D\% = 100\,\exp\!\left(\frac{-m\pi}{\sqrt{1-m^2}}\right)$$

### 1.3 Stabilité — critère des marges (diagramme de Bode)

**Définitions :**
- **Marge de phase** $M_\varphi$ : supplément de phase par rapport à $-180°$ à la pulsation de coupure $\omega_c$ (gain = 0 dB) :
$$M_\varphi = 180° + \arg(H_{BO}(j\omega_c))$$
- **Marge de gain** $M_G$ : inverse du gain (en dB) à la pulsation de déphasage $\omega_{-180°}$ (phase = $-180°$) :
$$M_G = -|H_{BO}(j\omega_{-180°})|_{dB}$$

**Cahiers des charges typiques rencontrés (sujets CAPET) :**
- $M_\varphi \geq 45°$ (robot Bakus 2023, porte de bus 2026)
- $M_\varphi \geq 90°$ (autopilotage 2024)
- $M_G \geq 10$ dB (porte de bus 2026)

**Condition de stabilité (critère de Bode, FTBO à déphasage minimal) :**
- Si $M_\varphi > 0°$ et $M_G > 0$ dB → système stable en boucle fermée.

*Source directe :* « La marge de phase correspond à la différence entre la phase pour un gain de 0 dB et 180°, soit $M_\varphi = \arg(H_{BF}(0\,dB)) + 180°$ » — E2 Disciplinaire IE 2024, Q.C10.

### 1.4 Correcteur proportionnel (P)

$$C(p) = K_C$$

- Agit sur le gain de la BO.
- Augmenter $K_C$ : améliore la précision, réduit la marge de phase (risque d'instabilité).
- Valeur maximale $K_{C\,lim}$ pour satisfaire la marge de phase : se lit graphiquement sur le diagramme de Bode de la BO pour $K_C = 1$.

*Procédure (sujet 2026 E1 Q.C6) :* sur le diagramme de Bode de la BO avec $K_C = 1$, identifier la pulsation $\omega_c$ telle que la phase vaut $-180° + M_{\varphi\,cible}$, puis relever le gain à cette pulsation : $K_{C\,lim} = 10^{-G_{dB}/20}$.

### 1.5 Correcteur proportionnel-intégral (PI)

$$C(p) = K_P\left(1 + \frac{1}{T_i\,p}\right) = \frac{K_P(1 + T_i\,p)}{T_i\,p}$$

- L'action intégrale annule l'erreur statique ($\varepsilon_s = 0$) pour un échelon.
- L'intégrateur ajoute $-90°$ de phase supplémentaire → risque de déstabilisation.

### 1.6 Correcteur proportionnel-intégral-dérivé (PID)

$$C(p) = K_P\left(1 + \frac{1}{T_i\,p} + T_d\,p\right)$$

- Action **P** : rapidité
- Action **I** : précision (erreur statique nulle)
- Action **D** : amélioration de la stabilité (anti-dépassement)

### 1.7 Correcteur PI numérique — relation de récurrence

Pour $C(p) = K_{co}\dfrac{1 + T_{co}\,p}{T_{co}\,p}$ avec période d'échantillonnage $T_e$ :

$$u_k = u_{k-1} + a_0\,\varepsilon_k + a_1\,\varepsilon_{k-1}$$

avec :
$$a_0 = K_{co}\left(1 + \frac{T_{co}}{T_e}\right) \quad;\quad a_1 = -K_{co}\frac{T_{co}}{T_e}$$

*Source directe : E2 Sujet 2026 Q.B19 — asservissement de température de pile à combustible.*

### 1.8 Réglage du correcteur par méthode du diagramme de Bode

**Procédure générale (visible dans les corrigés 2023, 2024) :**

1. Tracer le Bode de $H_{BO}(j\omega)$ pour $K_C = 1$.
2. Identifier la pulsation $\omega_B$ pour laquelle la phase vaut $-180° + M_{\varphi\,cible}$.
3. Le gain de la BO à $\omega_B$ vaut $-G_{dB}$. Pour que le gain soit 0 dB à $\omega_B$, il faut :
$$K_{PV} = 10^{G_{dB}/20}$$

*Exemple (corrigé 2023) :* Pour $M_\varphi = 45°$, $\omega_B = 7\,000$ rad·s$^{-1}$, gain à $\omega_B$ = $-59{,}4$ dB → $K_{PV} = 10^{59,4/20} = 933$.

---

## 2. QUESTIONS TYPES

**Q1.** (2026 — E1 Q.C5) À partir du diagramme de Bode de la FTBO tracé sur document réponse, déterminer graphiquement la marge de phase et la marge de gain. Conclure sur le respect du cahier des charges ($M_\varphi > 45°$, $M_G > 10$ dB).

**Q2.** (2026 — E1 Q.C6) Déterminer graphiquement $K_{C\,lim}$ permettant de se placer à la limite du critère de marge de phase.

**Q3.** (2023 — E1 Q.D8 / E2 Q.D8) Déterminer $K_{PV}$ pour obtenir une marge de phase de 45°, en s'appuyant sur le diagramme de Bode fourni.

**Q4.** (2024 — E2 Disciplinaire Q.C9–C12) Lire graphiquement l'erreur statique $\varepsilon_s$, le dépassement $D\%$ et la marge de phase $M_\varphi$ depuis les documents techniques DT4 et DT5. Conclure vis-à-vis du cahier des charges ($D\% \leq 5\,\%$, $\varepsilon_v = 0$, $M_\varphi \geq 90°$).

**Q5.** (2025 — E1/E2 Q.42) Analyser qualitativement les difficultés de mise en œuvre de la correction d'un convertisseur élévateur en termes de stabilité et précision.

**Q6.** (2026 — E2 BAC3 Q.B18–B19) Établir l'équation différentielle liant $u(t)$ et $\varepsilon(t)$, puis la relation de récurrence du correcteur numérique.

---

## 3. ATTENTES DU JURY

D'après les rapports de jury 2023, 2024, 2025 :

- **Thème systématiquement présent** depuis 2022 dans l'épreuve disciplinaire IE : asservissement de vitesse (moteur + variateur) + marge de phase.
- « *Trop peu de candidats l'ont traitée de manière satisfaisante. Le jury invite les candidats à revoir les concepts de base de ce domaine comme les notions de boucle ouverte, de correcteur ou encore de marge de phase.* » (rapport 2023)
- La **lecture graphique du diagramme de Bode** (marge de phase, marge de gain) est une compétence clé : les valeurs se lisent sur les documents réponses fournis.
- Le jury exige que les **conclusions soient argumentées** (comparer à la valeur du cahier des charges, pas juste donner un nombre).
- Les candidats qui **ne traitent pas la partie asservissement** sont fortement pénalisés.

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur(s) observées dans les sujets |
|----------|-------------------------------------|
| Marge de phase exigée | 45° (2023, 2026) ou 90° (2024) |
| Marge de gain exigée | $> 10$ dB (2026) |
| $K_{PV}$ calculé | 933 (sujet 2023) |
| $K_M$ (gain moteur) | 20,9 rad·s$^{-1}$·V$^{-1}$ (corrigé 2023) |
| $K_{GT}$ (tachymètre) | $0{,}048$ V·rad$^{-1}$·s (corrigé 2023) |
| $\omega_A$, $\omega_B$ (pulsations cassure) | extraites graphiquement sur Bode |
| Dépassement maximal admis | $D\% \leq 5\,\%$ (2024) |
| Erreur statique cible | nulle (intégrateur dans la BO) |
| Paramètres correcteur PI numérique | $K_{co}$, $T_{co}$, $T_e$ donnés dans le sujet |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **Confusion marge de phase / gain à $-180°$** : la marge de phase se lit à la pulsation de coupure (gain = 0 dB), pas à $-180°$.
- **Signe de la marge** : $M_\varphi = 180° + \arg(H_{BO}(j\omega_c))$ peut être négative si instable.
- **Oublier l'effet de $K_C$** sur le tracé du Bode : multiplier $K_C$ décale la courbe de gain de $20\log K_C$ sans changer la phase.
- **Correcteur PI** : l'action intégrale $1/(T_i p)$ garantit $\varepsilon_s = 0$ pour un échelon mais ajoute $-90°$ de phase.
- **Relation de récurrence** : erreur fréquente dans les approximations de la dérivée : $\dot{g}(kT_e) \approx (g_k - g_{k-1})/T_e$, pas $(g_{k+1} - g_k)/T_e$.
- **Confusion BO / BF** : le diagramme de Bode tracé est celui de la **boucle ouverte** ; la stabilité de la boucle fermée s'en déduit.
- **Cahier des charges** : toujours vérifier **toutes** les exigences (erreur, dépassement ET marge de phase).

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

- **T26** : la modélisation (fonctions de transfert, diagrammes de Bode) est le prérequis indispensable.
- **T15/T16** : les variateurs de vitesse (hacheur, variateur de fréquence) sont les actionneurs typiques des boucles asservies.
- **T22** : l'amplificateur opérationnel réalise physiquement les correcteurs PI/PID analogiques.
- **T29** : le correcteur numérique (relation de récurrence) est le pendant discret du correcteur continu ; nécessite la connaissance du théorème de Shannon et de la période d'échantillonnage.
- **T30** : précision de la chaîne de mesure (capteur + CAN) limite la précision de l'asservissement.
