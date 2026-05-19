# T29 — Communication industrielle & réseaux

> **Fréquence :** 5/22 sujets · **Intensité moyenne :** 🟡 Mentionné
> Présent dans les sujets de supervision, SCADA et systèmes distribués. Questions sur les bus de terrain, protocoles et paramètres de communication.

---

## Notions clés

### Paramètres d'une communication numérique

| Paramètre | Définition | Unité |
|---|---|---|
| Débit binaire | Bits transmis par seconde | bit/s (bps) |
| Débit utile | Données utiles (sans overhead) | bit/s |
| Latence | Délai entre émission et réception | ms, µs |
| Taux d'erreur binaire (BER) | $P(erreur) = N_{err}/N_{total}$ | sans unité |
| Topologie | Architecture du réseau | bus, étoile, anneau... |

### Relation débit-fréquence-modulation

$$D_b = f_s \cdot \log_2(M) \quad \text{(bit/s)}$$

- $f_s$ : fréquence symboles/s (baud)
- $M$ : nombre d'états par symbole

**Capacité de Shannon :**
$$C = B \cdot \log_2\left(1 + \frac{S}{N}\right)$$

- $B$ : largeur de bande (Hz)
- $S/N$ : rapport signal/bruit

### Principaux bus industriels

| Bus | Débit | Portée | Usage |
|---|---|---|---|
| CAN | 1 Mbit/s (1 m) / 250 kbit/s (250 m) | 10–1000 m | Automobile, machine |
| Modbus RTU | 115 kbit/s | 1200 m (RS485) | SCADA, supervision |
| Modbus TCP | 100 Mbit/s | Ethernet | Supervision IP |
| Profibus | 12 Mbit/s | 100 m | Automatisme industriel |
| EtherCAT | 100 Mbit/s | 100 m/segment | Motion control |
| DeviceNet | 500 kbit/s | 100–500 m | Capteurs/actionneurs |
| IO-Link | 230 kbit/s | 20 m | Capteurs intelligents |

### Protocoles couches (modèle OSI simplifié)

```
Couche 7 : Application (Modbus, PROFINET...)
Couche 4 : Transport (TCP/UDP)
Couche 3 : Réseau (IP)
Couche 2 : Liaison (Ethernet, CAN)
Couche 1 : Physique (câble, RS485, fibre...)
```

### Adressage Modbus

**Format d'une trame Modbus RTU :**
```
[Adresse esclave (1 oct)] [Code fonction (1 oct)] [Données] [CRC (2 oct)]
```

**Codes fonction courants :**
| Code | Fonction |
|---|---|
| 01 | Lire bobines (bits) |
| 03 | Lire registres (16 bits) |
| 05 | Écrire 1 bobine |
| 06 | Écrire 1 registre |

### Topologies réseau

| Topologie | Schéma | Avantages | Inconvénients |
|---|---|---|---|
| Bus | ─────○──○──○──── | Simple, économique | Rupture = panne totale |
| Étoile | Switch central | Robuste, isolement | Dépend du switch |
| Anneau | ○──○──○──○ | Redondance possible | Complexe |
| Maillée | Tous reliés | Très robuste | Coût élevé |

### Temps de cycle API / réseau

$$T_{cycle} = T_{lecture\_entrées} + T_{traitement} + T_{écriture\_sorties} + T_{communication}$$

Typiquement : 1 à 50 ms pour un API standard

---

## Types de questions au concours

| Type | Formule/Règle |
|---|---|
| Débit utile | $D_{utile} = D_{brut} \times (1 - overhead)$ |
| Temps de transmission | $t = N_{bits}/D_{brut}$ |
| Adresse Modbus d'un registre | Fournie dans le sujet |
| Choix de bus pour une application | Débit, portée, temps de réponse |
| Nombre d'esclaves sur un bus | Limité par le protocole (CAN : 127, Modbus : 247) |

---

## Pièges courants

1. **Débit brut vs utile** : le débit brut inclut les bits de start/stop, parité, adressage, CRC. Le débit utile (payload) est toujours inférieur.
2. **Modbus RTU vs Modbus TCP** : RTU = série (RS485), TCP = Ethernet. Même registres, même codes fonction, mais encapsulation différente.
3. **CAN** : le débit dépend de la longueur du bus. Plus le bus est long, plus le débit doit être faible (propagation du signal).
4. **Temps de réponse** : inclut le temps de traitement API + le temps de transmission réseau. Ne pas confondre débit (capacité) et latence (délai).
