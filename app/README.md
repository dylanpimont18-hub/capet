# App de révision CAPET SII·IE

PWA hors-ligne d'entraînement au rappel actif : formules, schémas,
conditions d'application. Le contenu est **généré** depuis `fiches/` —
ne jamais l'éditer à la main dans `app/` (`cards.json`, `svg/`,
`sw-assets.js` sont écrasés à chaque régénération et ne sont pas
versionnés, voir plus bas).

État courant (2026-11-10) : 727 cartes — 421 formules, 272 pièges,
34 schémas — réparties sur 33 thèmes, poids de 0,231 à 1,3. 34 SVG
compilés depuis les fiches LaTeX (0 échec). KaTeX 0.16.9 vendored dans `app/vendor/katex/` (62 fichiers,
dont les 20 polices `.woff2` précachées par le service worker). 66
entrées dans le cache du service worker.

## Régénérer le contenu

```bash
python scripts/build_cards.py            # avec compilation des schémas (lent)
python scripts/build_cards.py --sans-svg # texte seul, itération rapide
```

Produit `app/cards.json` et `app/svg/*.svg`, plus `app/sw-assets.js`
(liste des fichiers à précacher : SVG + polices KaTeX). En mode
`--sans-svg`, une carte schéma dont le SVG n'existe pas encore est
omise plutôt que de pointer vers une image cassée.

## Lancer en local

Un seul serveur, lancé depuis la **racine du dépôt** (pas depuis `app/`) :

```bash
python -m http.server 8765 --directory .
```

- app : `http://localhost:8765/app/`
- harnais de test HTML : `http://localhost:8765/tests/*.html`

Un serveur est nécessaire : les modules ES et le service worker ne
fonctionnent pas en `file://`. Servir uniquement `app/` (`--directory
app`) sortirait les harnais de test de la racine servie — ne pas le
faire.

## Tests

```bash
python -m pytest tests/ -v   # 74 tests — parseurs Python (scripts/)
```

Plus 4 harnais de test HTML, à ouvrir dans le navigateur une fois le
serveur ci-dessus lancé :
`tests/test_scheduler.html`, `tests/test_store.html`,
`tests/test_card_render.html`, `tests/test_priorites.html`.

## Après avoir corrigé une fiche

Relancer `build_cards.py`. Les identifiants de carte sont
**positionnels** : `T19-f-003` = 3ᵉ formule de T19 dans l'ordre du
fichier. Insérer une formule **au milieu** d'une section décale tous
les ids suivants de ce thème et désaligne la progression déjà
enregistrée (la progression est indexée par id dans `localStorage`,
voir `app/js/store.js`). Ajouter en **fin** de section est sans effet.
En cas de doute, exporter la progression depuis l'écran Réglages avant
de régénérer une fiche en profondeur.

## Ce qui n'est pas extrait, volontairement

La section `## 3. ATTENTES DU JURY` des fiches n'est **pas** extraite,
et ne doit pas l'être. Un audit de véracité du 2026-09-20 a établi que
54 % des citations de jury des fiches étaient défectueuses, dont 27
sans aucun support textuel (fabriquées). Importer ces encadrés dans
l'outil de révision propagerait des citations inventées sous une
forme — la carte flash — qui invite justement à les mémoriser telles
quelles. Voir `CLAUDE.md` (racine) pour le détail de l'audit.

## Installer sur iPhone

Safari → icône Partager → « Ajouter à l'écran d'accueil ».

Ce n'est pas cosmétique : l'ajout à l'écran d'accueil est ce qui
**protège la progression**. Safari purge les données (dont
`localStorage`) d'un site simplement visité au bout de 7 jours
d'inactivité (ITP), mais pas celles d'une PWA installée via « Ajouter
à l'écran d'accueil ». Sans cette installation, deux semaines sans
réviser suffisent à perdre la progression.

Même installée, il n'y a **aucun serveur** derrière cette app :
l'export JSON de l'écran Réglages reste la seule vraie sauvegarde. À
faire avant tout changement d'appareil, réinstallation, ou refonte de
fiche (voir section précédente).

## Publication sur GitHub Pages

L'app est publiée depuis un **second dépôt, public et dédié** :
`dylanpimont18-hub/capet-revision` → https://dylanpimont18-hub.github.io/capet-revision/

Ce dépôt-ci reste privé : il contient les PDF officiels, les fiches LaTeX et
le pipeline. Seul le dossier `app/` est publié, allégé des polices KaTeX
inutiles (woff2 seul — Safari et Chrome n'utilisent que celui-là).

### Republier après une correction de fiche

⚠ **Mise à jour du 2026-11-10 — ne plus recopier `app/`.** Depuis octobre 2026,
`capet-revision` évolue de son côté : nouveaux écrans (Catégories, Sujets,
Cours), `js/` et `css/` plus récents qu'ici, et un `cards.json` enrichi
directement (règles des pièges, réponses des schémas, champ `forme`) au-delà
de son `corrections/cartes.json`. Recopier `app/` ou régénérer son
`cards.json` écraserait ce travail.

Procédure correcte (appliquée le 2026-11-10, détail dans `README-app.md` de
`capet-revision`) :

1. `git pull` dans `capet-revision` avant tout ;
2. `python scripts/build_cards.py` ici, pour obtenir les nouvelles cartes ;
3. **fusionner** : partir du `cards.json` publié et n'y ajouter que les cartes
   dont l'id est absent, en leur donnant les champs attendus par l'app publiée
   (`forme` pour un piège ; `label`, `question`, `reponse` et un SVG copié sous
   `svg/<id>.svg` pour un schéma) ; vérifier que les cartes publiées restent
   identiques ;
4. dans `capet-revision` : `python corrections/appliquer.py --verifier`
   (attendu : 0 modification), `python scripts/indexer_cours.py` (ajoute les SVG
   à `sw-cours.js`), `python scripts/version_cache.py` ;
5. commit et push sur `main`.

GitHub Pages redéploie en une à deux minutes.

⚠ **Le `sw-assets.js` copié doit refléter les polices présentes.** Si tu
recopies `app/` tel quel puis supprimes les .ttf/.woff, régénère la liste,
sinon le service worker tentera de précacher des fichiers absents et le
hors-ligne sera incomplet.

⚠ **`CACHE_VERSION` change à chaque modification de contenu**, ce qui force
le service worker à se réinstaller et purge l'ancien cache. C'est ce qui
garantit qu'une correction atteint réellement le téléphone.

## Direction visuelle

Minimalism & Swiss Style, **sombre par défaut** (la révision se fait le soir
et dans les transports). Le système de design est figé dans
`design-system/revision-capet/MASTER.md`.

Trois règles qui expliquent la plupart des choix :

1. **Aucune police à télécharger.** `-apple-system` donne San Francisco sur
   iPhone, dessinée par Apple pour ses écrans. Le système de design proposait
   Inter via Google Fonts : incompatible avec le hors-ligne, et Inter s'inspire
   de toute façon de San Francisco.
2. **La couleur ne porte jamais seule une information.** Les pastilles de
   l'écran Priorités sont doublées d'un `aria-label` textuel, les boutons de
   notation ont leur libellé.
3. **Un seul accent.** Tout le reste est encre et surface. Une interface
   qu'on regarde 20 minutes par jour pendant six mois ne doit pas fatiguer.

`tests/test_contraste.py` vérifie les ratios WCAG des deux thèmes à chaque
exécution de la suite : un jeton retouché à la main qui ferait passer un texte
sous 4,5:1 fait échouer le test.

## Geste de balayage

Sur écran tactile : glisser la carte à **gauche** = raté, à **droite** = su,
vers le **haut** = hésité. Les boutons restent la voie principale ; le geste
les double pour l'usage à une main. Il ne s'active que sur pointeur grossier
(`pointer: coarse`) et laisse le défilement vertical au navigateur.
