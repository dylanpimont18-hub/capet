// app/js/rappel.js
// Rappel local : pas de vrai push (l'app n'a aucun serveur, voir store.js),
// donc rien ne peut relancer l'utilisateur une fois l'app fermée. Le seul
// levier possible est d'afficher un bandeau AU RETOUR dans l'app, si assez
// de retard s'est accumulé depuis la dernière visite — sans ça, l'app reste
// muette même après deux semaines d'absence (le risque documenté dans le
// README : Safari purge localStorage au bout de 7 jours d'inactivité sans
// installation à l'écran d'accueil).

const CLE_DERNIERE_VISITE = "capet.derniere-visite";
const JOUR_MS = 86400000;
const SEUIL_JOURS = 3;

export function enregistrerVisite(maintenant = Date.now()) {
  try { localStorage.setItem(CLE_DERNIERE_VISITE, String(maintenant)); }
  catch { /* mode privé : le rappel sera simplement muet la prochaine fois */ }
}

// Retourne le nombre de jours écoulés depuis la dernière visite connue, ou
// null si aucune visite antérieure n'est enregistrée (première utilisation :
// rien à rappeler).
export function joursDepuisDerniereVisite(maintenant = Date.now()) {
  let brut;
  try { brut = localStorage.getItem(CLE_DERNIERE_VISITE); }
  catch { return null; }
  const t = Number(brut);
  if (!brut || !Number.isFinite(t)) return null;
  return Math.floor((maintenant - t) / JOUR_MS);
}

export function doitRappeler(maintenant = Date.now()) {
  const j = joursDepuisDerniereVisite(maintenant);
  return j !== null && j >= SEUIL_JOURS;
}

export function libelleRappel(nCartesEnRetard, jours) {
  const cartes = nCartesEnRetard > 0
    ? ` ${nCartesEnRetard} carte(s) en retard.`
    : "";
  return `Pas de révision depuis ${jours} jours.${cartes}`;
}
