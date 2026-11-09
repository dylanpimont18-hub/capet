# T33 — Informatique embarquée, programmation et réseaux industriels
## Contenu documentaire — créé le 2026-11-10 pour couvrir le référentiel

> L'algorithmique (algorigramme ou pseudo-code à compléter) et la programmation apparaissent
> dans 11 des 13 années 2013–2025 ; Python en 2019, 2021, 2022, 2023 et en E2 2026 ; liaison
> série et ASCII en 2018, 2023, 2025 ; Modbus et Ethernet en 2013, 2014, 2023, 2025 ; IHM en 2018.
> Ce thème complète T24 (systèmes embarqués) et T25 (transmission), sans répéter leurs cartes.

---

## 1. FORMULES ET COURS

### 1.1 Codage, opérations bit à bit, architecture

| Grandeur | Formule | Unité | Fréquence | Source |
|---|---|---|---|---|
| Test du bit de rang k | $b_k = (x \gg k)\ \&\ 1$ | — | Présent | E1 2026 D10 (masque) |
| Mise à 1 du bit de rang k | $x \leftarrow x \mid (1 \ll k)$ | — | Courant | Cours |
| Mise à 0 du bit de rang k | $x \leftarrow x\ \&\ \sim(1 \ll k)$ | — | Courant | Cours |
| Inversion du bit de rang k | $x \leftarrow x \oplus (1 \ll k)$ | — | Courant | Cours |
| Plage d'un entier non signé sur n bits | $0 \le x \le 2^n - 1$ | — | Courant | Cours |
| Plage d'un entier signé en complément à 2 sur n bits | $-2^{n-1} \le x \le 2^{n-1} - 1$ | — | Courant | Cours |
| Capacité d'une mémoire ($n_{adr}$ bits d'adresse, mots de w bits) | $C = 2^{n_{adr}} \times w$ | bit | Courant | Cours |
| Durée d'exécution d'un programme | $t = \frac{N_{cycles}}{f_{clk}}$ | s | Courant | Cours |
| Période de débordement d'un timer | $T = \frac{P \, (ARR + 1)}{f_{clk}}$ | s | Courant | Cours |
| Énergie par la méthode des rectangles | $E \approx \sum_i \phi_i \, \Delta t$ | J | Présent | E2 disciplinaire 2025, Q4 |

### 1.2 Liaisons série et réseaux industriels

| Grandeur | Formule | Unité | Fréquence | Source |
|---|---|---|---|---|
| Durée d'un caractère en liaison série asynchrone | $t_{car} = \frac{1 + n_d + n_p + n_s}{R}$ | s | Présent | E2 disciplinaire 2023, E4 |
| Débit utile d'une liaison série asynchrone | $D_u = R \cdot \frac{n_d}{1 + n_d + n_p + n_s}$ | bit/s | Courant | Cours |
| Durée d'une trame de N caractères | $t_{trame} = N \, t_{car}$ | s | Présent | E2 disciplinaire 2023, E7 |
| Silence minimal entre deux trames Modbus RTU | $t_{sil} \ge 3{,}5 \, t_{car}$ | s | Courant | Cours |
| Nombre d'adresses d'un bus I2C à 7 bits | $N_{adr} = 2^7 = 128$ | — | Courant | Cours |

---

## 2. QUESTIONS TYPES

**QT1 — Lire un bit d'alarme avec un masque (E1 2026, D10 ; corrigé officiel = RJ26 D11)** :
masque 0004 (hexadécimal) ; si `Datafield ET Masque` vaut 0, renvoyer 0, sinon 1.

**QT2 — Durée d'une trame GPS (E2 disciplinaire 2023, E4–E8 ; corrigé officiel)** : 10 bits par
caractère ; « E » = 45 (hexadécimal) ; 71 caractères à 115 200 bauds : 6,16 ms ; à 6 km/h, le robot
parcourt 1,03 cm (le rapport écrit 1,03 m : erreur d'unité) > 1 cm exigé.

**QT3 — Intégrer une irradiance et compléter l'algorithme (E2 disciplinaire 2025, Q4–Q5 ;
corrigé officiel)** : pas de 20 s ; 1 327 × 20 = 26 540 J/m² = 7,37 Wh/m². Le corrigé officiel
divise par 1 000 alors que le temps est en secondes : diviser par 3,6·10⁶ pour obtenir des kWh.

---

## 3. ATTENTES DU JURY

> « Depuis la session 2017, que ce soit à l’agrégation ou au CAPET, à l’externe comme à
> l’interne, il existe une option ingénierie informatique et surtout un programme d’informatique
> pour toutes les options de ces concours. Les compétences liées à ce programme sont par
> conséquent également évaluées. Le jury conseille aux futurs candidats de ne surtout pas faire
> l’impasse sur l’informatique […] »
> — Rapport_Jury_2018.md l.158 (avant-propos, commun à toutes les options)

---

## 4. DONNÉES NUMÉRIQUES TYPIQUES

| Grandeur | Valeur typique |
|---|---|
| Débits UART usuels | 9 600, 19 200, 115 200 bauds |
| Format le plus courant | 8N1 : 10 bits par octet |
| RS-485 | 32 nœuds, 1 200 m |
| I2C standard / rapide | 100 / 400 kbit/s |
| Modbus : adresses esclaves | 1 à 247 (0 = diffusion) |
| Modbus TCP | port 502 |

---

## 5. LACUNES ET PIÈGES RÉCURRENTS

- **Indices en Python** : faire commencer une boucle à 1 ou la poursuivre jusqu'à n inclus. Une liste de n éléments est indexée de 0 à n − 1 et range(n) s'arrête à n − 1 ; lire t[i+1] impose de s'arrêter à n − 2.
- **Division entière** : écrire 7/2 en attendant 3. En Python 3, 7/2 vaut 3,5 et 7//2 vaut 3 ; en C, 7/2 vaut 3 entre deux entiers.
- **Affectation et comparaison** : écrire if (x = 5) en C. Le test d'égalité s'écrit ==, l'affectation =, et en langage ST l'affectation s'écrit := (voir T29).
- **Priorité des opérateurs** : tester un bit en écrivant x & m == 0. En C, == est prioritaire sur & : il faut écrire (x & m) == 0.
- **Bits par caractère** : compter 8 bits par caractère en liaison série asynchrone. Il faut ajouter le start, le ou les stops et l'éventuelle parité : en 8N1, un caractère fait 10 bits (E2 2023, question E4).
- **Ordre des bits en UART** : lire une trame série en plaçant le bit de poids fort en premier. L'UART émet le bit de poids faible juste après le start : « E » (45 en hexadécimal) part sous la forme 1, 0, 1, 0, 0, 0, 1, 0.
- **Bauds et débit utile** : prendre 115 200 bauds pour le débit de données. En 8N1, le débit utile est de 92 160 bit/s, soit 11 520 octets par seconde.
- **RS-232 et RS-485** : raccorder plusieurs équipements sur une liaison RS-232. La RS-232 est point à point et limitée à une quinzaine de mètres ; la RS-485, différentielle, accepte 32 équipements sur environ 1 200 m.
- **I2C et SPI** : oublier les résistances de tirage d'un bus I2C. Les lignes SDA et SCL sont à collecteur ouvert et exigent des résistances de tirage ; le SPI, lui, demande un fil de sélection par esclave.
- **Échanges Modbus** : attendre qu'un esclave Modbus émette de lui-même. Seul le maître initie un échange ; l'esclave répond à son adresse (1 à 247), et l'adresse 0 sert à la diffusion, sans réponse.
- **Scrutation et interruption** : surveiller un événement bref par scrutation dans une boucle lente. Un événement plus court que la période de scrutation est manqué ; une interruption le capte quel que soit l'état du programme principal.
- **Complément à 2** : interpréter FF (hexadécimal) comme 255 pour une variable signée. Sur 8 bits signés, FF vaut −1 et la plage va de −128 à 127.
- **Alarmes d'une IHM** : signaler un défaut par la seule couleur. Une IHM double la couleur d'un texte ou d'un symbole, horodate les alarmes et demande leur acquittement.

---

## 6. CONNEXIONS AVEC D'AUTRES THÈMES

| Thème associé | Articulation |
|---|---|
| **T24 — Systèmes embarqués** | Registres, MLI, API S7-1500 ; T33 ajoute la programmation, les liaisons et l'IHM. |
| **T25 — Transmission numérique** | Bus CAN, LoRa, débits ; T33 traite UART, RS-485, I2C, SPI, Modbus, Ethernet. |
| **T28 — Logique combinatoire** | Numération et masques reposent sur l'algèbre de Boole. |
| **T29 — Logique séquentielle et API** | Algorigrammes, langages IEC 61131-3, machines à états. |
| **T31 — Télécommunications** | Couche physique (codage NRZ, supports) des liaisons. |
| **T32 — Ingénierie système** | La chaîne d'information s'implémente sur microcontrôleur et réseaux. |
