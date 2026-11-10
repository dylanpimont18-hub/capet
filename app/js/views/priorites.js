// app/js/views/priorites.js
import { charger } from "../store.js";
import { echapper } from "../card-render.js";
import { fileDuJour } from "../scheduler.js";

// Date de l'écrit CAPET externe SII, session 2026 — à corriger si le
// calendrier officiel Eduscol/SIAC publie une date différente.
const DATE_ECRIT = new Date("2026-03-09T00:00:00");
const JOUR_MS_P = 86400000;

const SEUIL_REPET = 2;
// 2,3 et non 2,4 : la facilité initiale VAUT 2,4, donc un unique « hésité »
// (−0,05) la fait tomber à 2,35 et la carte n'est plus comptée acquise,
// même après deux réussites. Le seuil doit être strictement sous l'initiale.
const SEUIL_FACILITE = 2.3;

export function calculerMaitrise(cartes, progression) {
  const par = new Map();
  for (const c of cartes) {
    if (!par.has(c.theme)) par.set(c.theme, { vues: 0, acquises: 0, total: 0 });
    const e = par.get(c.theme);
    e.total += 1;
    const p = progression[c.id];
    if (p) {
      e.vues += 1;
      if (p.repetitions >= SEUIL_REPET && p.facilite >= SEUIL_FACILITE) e.acquises += 1;
    }
  }
  for (const e of par.values()) {
    e.maitrise = e.total ? e.acquises / e.total : 0;
  }
  return par;
}

export function ordonnerThemes(themes, maitrises) {
  return themes
    .map(t => {
      const m = maitrises.get(t.code) || { maitrise: 0, vues: 0, total: 0 };
      return { ...t, ...m, urgence: (t.poids || 0) * (1 - m.maitrise) };
    })
    .sort((a, b) => b.urgence - a.urgence);
}

function couleur(u) {
  if (u >= 0.5) return "var(--rate)";
  if (u >= 0.25) return "var(--hesite)";
  return "var(--su)";
}

// La couleur ne doit jamais porter seule l'information : chaque pastille
// est doublée d'un libellé lisible, y compris par un lecteur d'écran.
function niveau(u) {
  if (u >= 0.5) return { mot: "Prioritaire", couleur: "var(--rate)" };
  if (u >= 0.25) return { mot: "À revoir", couleur: "var(--hesite)" };
  return { mot: "Acquis", couleur: "var(--su)" };
}

// Jours restants avant l'écrit, et dette de révision (cartes en retard,
// toutes échéances confondues — pas seulement la file du jour plafonnée à
// 30). Sert de signal « on track / off track » directement actionnable pour
// une échéance fixe, plutôt qu'un tableau de bord générique sans référence.
function compteARebours(cartes, progression, maintenant = Date.now()) {
  const jours = Math.ceil((DATE_ECRIT.getTime() - maintenant) / JOUR_MS_P);
  const dette = fileDuJour(cartes, progression, maintenant, cartes.length)
    .filter(c => {
      const p = progression[c.id];
      return p && Number.isFinite(p.du) && p.du <= maintenant;
    }).length;
  return { jours, dette };
}

export function vuePriorites(racine, data) {
  const progression = charger();
  const m = calculerMaitrise(data.cards, progression);
  const themes = ordonnerThemes(data.themes, m);
  const { jours, dette } = compteARebours(data.cards, progression);

  const bandeauEcheance = jours > 0
    ? `<p class="sous-titre">
        <strong>${jours} jour${jours > 1 ? "s" : ""}</strong> avant l'écrit
        · <strong>${dette}</strong> carte${dette > 1 ? "s" : ""} en retard</p>`
    : "";

  // Trois colonnes seulement : à 390 px, six colonnes deviennent illisibles.
  // Les chiffres secondaires passent sous le titre, en petit corps.
  const lignes = themes.map(t => {
    const n = niveau(t.urgence);
    const pct = Math.round(t.maitrise * 100);
    return `
    <tr>
      <td><span class="pastille" style="background:${n.couleur}"
            role="img" aria-label="${n.mot}"></span></td>
      <td>
        <div class="theme">${echapper(t.titre)}</div>
        <div class="meta">
          <span class="code">${echapper(t.code)}</span>
          · ${t.presence_n}/${t.presence_sur} sujets
          · ${t.vues}/${t.total} vues
        </div>
      </td>
      <td class="pct">${pct}&nbsp;%</td>
    </tr>`;
  }).join("");

  const prioritaires = themes.filter(t => t.urgence >= 0.5).length;

  racine.innerHTML = `
    <div class="carte">
      <p class="consigne">Priorités</p>
      <p class="vedette">${prioritaires} thème${prioritaires > 1 ? "s" : ""} à travailler</p>
      ${bandeauEcheance}
      <p class="sous-titre">Fréquence au concours croisée avec votre maîtrise.
        Les premiers de la liste tombent souvent et sont mal maîtrisés.</p>
      <table class="grille">
        <caption class="sr-only">Thèmes classés par urgence décroissante</caption>
        <thead>
          <tr><th><span class="sr-only">Niveau</span></th>
              <th>Thème</th>
              <th class="pct">Maîtrise</th></tr>
        </thead>
        <tbody>${lignes}</tbody>
      </table>
    </div>`;
}
