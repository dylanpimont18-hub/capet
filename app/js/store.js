// app/js/store.js
// Persistance de la progression. Aucun serveur : l'export JSON est le seul backup.

export const CLE = "capet.progression.v1";

export function charger() {
  try {
    const brut = localStorage.getItem(CLE);
    return brut ? JSON.parse(brut) : {};
  } catch {
    return {};
  }
}

export function sauver(progression) {
  localStorage.setItem(CLE, JSON.stringify(progression));
}

export function majCarte(id, etat) {
  const p = charger();
  p[id] = etat;
  sauver(p);
}

export function reinitialiser() {
  localStorage.removeItem(CLE);
}

export function exporter() {
  return JSON.stringify(
    { version: 1, exporte_le: new Date().toISOString(), progression: charger() },
    null, 1
  );
}

export function importer(texte) {
  let data;
  try {
    data = JSON.parse(texte);
  } catch {
    return false;
  }
  if (!data || typeof data !== "object") return false;
  if (!data.progression || typeof data.progression !== "object") return false;
  sauver(data.progression);
  return true;
}
