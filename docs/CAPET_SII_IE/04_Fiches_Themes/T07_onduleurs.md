# T07 — Onduleurs / MLI

> **Fréquence :** 5/22 sujets · **Intensité moyenne :** 🟠 Important
> Présent dans les sujets variateurs de vitesse, véhicules électriques, raccordement PV au réseau.

---

## Notions clés

### Onduleur monophasé en pont (H-Bridge)

```
    +Vdc ─┬──[K1]──┬──[K3]──┬
           |        |        |
          [K2]     [M]      [K4]
           |        |        |
    -Vdc ─┴────────┴────────┴
```

Tension fondamentale de sortie (MLI sinusoïdale) :

$$U_{1,eff} = \frac{m_a \cdot V_{dc}}{\sqrt{2}} \qquad \text{(monophasé pont)}$$

### Onduleur triphasé (pont VSI)

$$U_{1,eff} = \frac{m_a \cdot V_{dc}}{\sqrt{2}} \cdot \frac{\sqrt{3}}{... } \approx \frac{m_a \cdot V_{dc} \cdot \sqrt{6}}{2\pi} \approx 0{,}612 \cdot m_a \cdot V_{dc}$$

Plus simplement, pour $m_a = 1$ (pleine modulation) :

$$U_{fondamentale,eff} \approx 0{,}612 \cdot V_{dc} \quad \text{(tension simple efficace)}$$

### Indice de modulation d'amplitude

$$m_a = \frac{V_{ref}}{V_{porteuse}} \quad (0 \le m_a \le 1)$$

- $m_a = 1$ : modulation maximale linéaire
- $m_a > 1$ : surmodulation (harmoniques importants)

### Indice de modulation de fréquence

$$m_f = \frac{f_s}{f_{fondamental}} \quad \text{(impair, multiple de 3 pour onduleur tri)}$$

- Plus $m_f$ est grand, plus les harmoniques sont éloignés du fondamental → filtrage facile
- Typiquement $m_f$ = 9, 15, 21...

### THD (Taux de Distorsion Harmonique)

$$THD = \frac{\sqrt{\sum_{n=2}^{\infty} U_n^2}}{U_1} \times 100\%$$

- Norme EN 50160 : THD < 8 % pour harmoniques de tension (réseau)
- Onduleur MLI bien conçu : THD < 5 %

### Bilan puissance onduleur

$$P_{out} = P_{in} - P_{pertes_{interrupteurs}}$$

En première approximation ($\eta \approx 1$) :

$$V_{dc} \cdot I_{dc} = \sqrt{3} \cdot U_{eff} \cdot I_{eff} \cdot \cos\varphi$$

---

## MLI (Modulation de Largeur d'Impulsion)

### Principe

Signal de référence sinusoïdal (fréquence $f_1$) comparé à une porteuse triangulaire (fréquence $f_s$) :
- Si $v_{ref} > v_{porteuse}$ → K haut = ON
- Si $v_{ref} < v_{porteuse}$ → K haut = OFF

### Rapport cyclique variable

$$\alpha(t) = \frac{1}{2}\left(1 + m_a \sin(\omega_1 t)\right)$$

---

## Types de questions au concours

| Type | Formule |
|---|---|
| Tension de sortie fondamentale | $U_1 = m_a \cdot V_{dc}/\sqrt{2}$ |
| Tension DC nécessaire pour $U_{AC}$ | $V_{dc} \geq \sqrt{2} \cdot U_{AC} / m_a$ |
| THD à respecter | $THD < 5\%$ (norme EN 50160) |
| Fréquence des harmoniques | $f_h = (k \cdot m_f \pm 1) \cdot f_1$ |
| Puissance active injectée | $P = \sqrt{3} \cdot U \cdot I \cdot \cos\varphi$ |

---

## Pièges courants

1. **$m_a$ vs $m_f$** : ne pas confondre l'indice de modulation d'amplitude ($m_a$, contrôle la tension) et de fréquence ($m_f$, contrôle les harmoniques).
2. **Tension composée vs simple** : $U_{composée} = \sqrt{3} \cdot U_{simple}$.
3. **THD** : le calcul implique la somme quadratique des harmoniques — ne pas sommer les amplitudes directement.
4. **Puissance réactive** : les condensateurs de l'onduleur participent à la compensation. Ne pas oublier $Q$ dans les bilans.
