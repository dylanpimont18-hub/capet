// Ordonnanceur SM-2 simplifié, pondéré par la fréquence d'apparition au concours.

const FACILITE_INIT = 2.4;
const FACILITE_MIN = 1.3;
const FACILITE_MAX = 2.8;
const JOUR_MS = 86400000;

// Plafond d'intervalle, en jours. Sans lui, la suite des « su » donne
// 1, 3, 8, 22, 62, 174, 487, 1364… : dès la 6e répétition la carte sort de
// l'horizon de révision (l'écrit est en mars). Avec 60 jours, une carte
// acquise revient au moins trois fois d'ici l'épreuve.
const INTERVALLE_MAX = 60;

// Places réservées aux cartes jamais vues dans chaque file quotidienne.
// Sans ce quota, les cartes échues (toujours prioritaires) saturent la file
// dès qu'il y en a 30, et la découverte du corpus s'arrête définitivement.
const QUOTA_NOUVELLES = 8;

export function etatInitial() {
  return { intervalle: 0, facilite: FACILITE_INIT, repetitions: 0, du: 0 };
}

function borner(f) {
  return Math.min(FACILITE_MAX, Math.max(FACILITE_MIN, Math.round(f * 100) / 100));
}

export function noter(etat, note, maintenant = Date.now()) {
  const e = { ...etat };

  if (note === "rate") {
    e.repetitions = 0;
    e.intervalle = 0;
    e.facilite = borner(e.facilite - 0.2);
  } else if (note === "hesite") {
    e.repetitions += 1;
    e.intervalle = Math.max(1, Math.round(e.intervalle * 1.2));
    e.facilite = borner(e.facilite - 0.05);
  } else if (note === "facile") {
    // Saute les paliers 1j/3j d'amorçage : une carte déjà solide n'a pas
    // besoin d'être revue dès le lendemain. Bonus de facilité doublé (+0.2)
    // pour que l'intervalle s'allonge plus vite qu'après un simple « su ».
    e.intervalle = e.repetitions === 0
      ? 4
      : Math.min(INTERVALLE_MAX, Math.round(Math.max(e.intervalle, 1) * e.facilite * 1.3));
    e.repetitions += 1;
    e.facilite = borner(e.facilite + 0.2);
  } else {
    // "su"
    if (e.repetitions === 0) e.intervalle = 1;
    else if (e.repetitions === 1) e.intervalle = 3;
    else e.intervalle = Math.min(INTERVALLE_MAX, Math.round(e.intervalle * e.facilite));
    e.repetitions += 1;
    e.facilite = borner(e.facilite + 0.1);
  }

  e.du = maintenant + e.intervalle * JOUR_MS;
  return e;
}

// Urgence d'UNE carte : fréquence au concours pondérée par l'éloignement à
// la facilité maximale. Une carte jamais vue (facilite = init) ou déjà
// ratée (facilite basse) pèse plus qu'une carte proche de FACILITE_MAX,
// même à poids de thème égal. Sert à trier fileDuJour — ordonnerThemes()
// (priorites.js) garde son agrégat par thème, qui répond à une question
// différente (« quel thème travailler ? » vs « quelle carte réviser
// maintenant ? »).
export function urgenceCarte(carte, etat) {
  const poids = carte.poids || 0;
  if (!etat) return poids;
  const eloignement = (FACILITE_MAX - etat.facilite) / (FACILITE_MAX - FACILITE_MIN);
  return poids * (0.4 + 0.6 * Math.max(0, Math.min(1, eloignement)));
}

export function fileDuJour(cartes, progression, maintenant = Date.now(), taille = 30) {
  const enRetard = [];
  const nouvelles = [];

  for (const c of cartes) {
    const p = progression[c.id];
    // Un état corrompu (du = NaN/undefined — import retouché à la main, ou
    // noter() lui-même si facilite est corrompue) ne doit jamais rendre une
    // carte injoignable : ni échue ni nouvelle, elle disparaîtrait sinon
    // silencieusement et définitivement de la rotation. On la retraite
    // comme nouvelle : l'app se répare d'elle-même.
    if (!p || !Number.isFinite(p.du)) nouvelles.push(c);
    else if (p.du <= maintenant) enRetard.push(c);
  }

  // Urgence par carte plutôt que par poids de thème seul : à poids égal,
  // une carte déjà ratée (facilite basse) passe devant une carte proche de
  // la maîtrise. Sans ça, une carte systématiquement ratée dans un thème à
  // 90 % maîtrisé se noyait dans la moyenne du thème (voir priorites.js,
  // qui répond à une question différente : quel thème, pas quelle carte).
  const parUrgence = (a, b) =>
    urgenceCarte(b, progression[b.id]) - urgenceCarte(a, progression[a.id]);
  enRetard.sort(parUrgence);
  nouvelles.sort(parUrgence);

  // Les cartes échues sont prioritaires, mais on garde des places pour les
  // cartes jamais vues : sinon, dès que 30 cartes sont échues, plus aucune
  // nouveauté n'entre et la découverte du corpus (~575 cartes) s'arrête.
  const placesRevisions = Math.max(0, taille - QUOTA_NOUVELLES);
  const retenues = enRetard.slice(0, placesRevisions);
  const neuves = nouvelles.slice(0, taille - retenues.length);

  // S'il reste de la place (peu de cartes neuves disponibles), on la rend
  // aux révisions en retard plutôt que de servir une file incomplète.
  const reste = taille - retenues.length - neuves.length;
  const complement = reste > 0 ? enRetard.slice(placesRevisions, placesRevisions + reste) : [];

  return [...retenues, ...complement, ...neuves];
}
