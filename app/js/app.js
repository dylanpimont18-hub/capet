// app/js/app.js
import { vueReviser } from "./views/reviser.js";
import { vuePriorites } from "./views/priorites.js";
import { vueReglages } from "./views/reglages.js";
import { doitRappeler, joursDepuisDerniereVisite, libelleRappel, enregistrerVisite } from "./rappel.js";
import { charger } from "./store.js";
import { fileDuJour } from "./scheduler.js";
import { echapper } from "./card-render.js";

const CLE_THEME = "capet.theme";

function appliquerTheme(t) {
  document.documentElement.dataset.theme = t;
  try { localStorage.setItem(CLE_THEME, t); } catch { /* mode privé */ }
}

let DATA = null;

async function donnees() {
  if (!DATA) DATA = await (await fetch("cards.json")).json();
  return DATA;
}

const ROUTES = {
  "#/reviser": vueReviser,
  "#/priorites": vuePriorites,
  "#/reglages": vueReglages,
};

async function naviguer() {
  const hash = location.hash || "#/reviser";
  const racine = document.getElementById("app");
  const vue = ROUTES[hash];

  // La couleur seule ne suffit pas : aria-current expose l'onglet courant
  // aux lecteurs d'écran, qui ne perçoivent pas la mise en évidence visuelle.
  document.querySelectorAll(".barre-bas a").forEach(a => {
    const courant = a.getAttribute("href") === hash;
    a.classList.toggle("actif", courant);
    if (courant) a.setAttribute("aria-current", "page");
    else a.removeAttribute("aria-current");
  });

  if (!vue) {
    racine.innerHTML = `<div class="carte"><p>Écran à venir.</p></div>`;
    return;
  }
  racine.innerHTML = `<div class="carte"><p class="consigne">Chargement…</p></div>`;
  try {
    vue(racine, await donnees());
  } catch (e) {
    racine.innerHTML = `<div class="carte"><p class="vedette">Données indisponibles</p>
      <p class="consigne">Lancez <code>python scripts/build_cards.py</code> puis rechargez.</p></div>`;
  }
}

window.addEventListener("hashchange", naviguer);
window.addEventListener("DOMContentLoaded", () => {
  // Ordre de décision : choix explicite de l'utilisateur, sinon réglage du
  // système, sinon sombre — la révision se fait surtout le soir.
  let t = null;
  try { t = localStorage.getItem(CLE_THEME); } catch { /* mode privé */ }
  if (!t) {
    const clairSysteme = window.matchMedia
      && window.matchMedia("(prefers-color-scheme: light)").matches;
    t = clairSysteme ? "clair" : "sombre";
  }
  appliquerTheme(t);

  document.getElementById("bascule-theme").onclick = () =>
    appliquerTheme(document.documentElement.dataset.theme === "clair" ? "sombre" : "clair");
  if (!location.hash) location.hash = "#/reviser";
  naviguer();

  verifierRappel();
  attacherLoupe();

  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("sw.js").then(reg => {
      if (!reg) return;
      // Le cache est cache-first sans expiration (sw.js) : sans cette
      // vérification active, un appareil installé et rarement relancé peut
      // ne jamais recevoir une correction de fiche avant l'écrit. On
      // revérifie à chaque lancement plutôt que d'attendre l'intervalle
      // (souvent 24h) que le navigateur applique de lui-même.
      reg.update().catch(() => { /* hors ligne : rien à faire */ });

      reg.addEventListener("updatefound", () => {
        const worker = reg.installing;
        if (!worker) return;
        worker.addEventListener("statechange", () => {
          // "installed" + un controller déjà actif = une VERSION PRÉCÉDENTE
          // tournait déjà : c'est une mise à jour, pas la toute première
          // installation (où il n'y a pas encore de controller).
          if (worker.state === "installed" && navigator.serviceWorker.controller) {
            annoncerMiseAJour(worker);
          }
        });
      });
    }).catch(() => { /* hors https/localhost */ });

    // Le nouveau service worker prend le contrôle (skipWaiting + clients.claim
    // côté sw.js) : recharger maintenant sert la version fraîche du cache
    // plutôt que de laisser l'onglet ouvert tourner sur l'ancien index.html.
    let dejaRecharge = false;
    navigator.serviceWorker.addEventListener("controllerchange", () => {
      if (dejaRecharge) return;
      dejaRecharge = true;
      location.reload();
    });
  }
});

function annoncerMiseAJour(worker) {
  if (document.getElementById("bandeau-maj")) return;
  const bandeau = document.createElement("div");
  bandeau.id = "bandeau-maj";
  bandeau.className = "bandeau-maj";
  bandeau.setAttribute("role", "status");
  bandeau.innerHTML = `<span>Nouvelle version disponible.</span>
    <button id="recharger-maj">Recharger</button>`;
  document.body.appendChild(bandeau);
  document.getElementById("recharger-maj").onclick = () => worker.postMessage({ type: "activer" });
}

// Vérifie AVANT d'écraser la date de dernière visite, sinon le seuil ne se
// déclenche jamais (chaque visite effacerait l'absence qui la précède).
async function verifierRappel() {
  const jours = joursDepuisDerniereVisite();
  if (doitRappeler()) {
    let enRetard = 0;
    try {
      const data = await donnees();
      enRetard = fileDuJour(data.cards, charger()).length;
    } catch { /* données indisponibles : bandeau sans le compte de cartes */ }
    afficherBandeauRappel(libelleRappel(enRetard, jours));
  }
  enregistrerVisite();
}

// Délégation globale plutôt qu'un écouteur par carte : #app est entièrement
// réécrit (innerHTML) à chaque révélation de verso et à chaque navigation
// (voir naviguer() ci-dessus), ce qui détruirait un écouteur posé
// directement sur .loupe-svg.
function attacherLoupe() {
  document.addEventListener("click", e => {
    const bouton = e.target.closest(".loupe-svg");
    if (bouton) { ouvrirLoupe(bouton.dataset.svg, bouton.dataset.alt); return; }
    if (e.target.closest("#loupe-fermer") || e.target.id === "loupe-fond") fermerLoupe();
  });
  document.addEventListener("keydown", e => {
    if (e.key === "Escape") fermerLoupe();
  });
}

function ouvrirLoupe(src, alt) {
  fermerLoupe();
  const fond = document.createElement("div");
  fond.id = "loupe-fond";
  fond.className = "loupe-fond";
  // src/alt viennent de dataset (déjà décodé) : ré-échapper avant de les
  // remettre dans innerHTML, sinon un alt contenant `<`/`>` s'interpréterait
  // comme du HTML au lieu du texte affiché par card-render.js.
  fond.innerHTML = `
    <div class="loupe-cadre">
      <img src="${echapper(src)}" alt="${echapper(alt)}">
    </div>
    <button type="button" id="loupe-fermer" aria-label="Fermer">✕</button>`;
  document.body.appendChild(fond);
}

function fermerLoupe() {
  document.getElementById("loupe-fond")?.remove();
}

function afficherBandeauRappel(texte) {
  const bandeau = document.createElement("div");
  bandeau.className = "bandeau-rappel";
  bandeau.setAttribute("role", "status");
  bandeau.innerHTML = `<span>${texte}</span><button id="fermer-rappel">Réviser</button>`;
  document.body.appendChild(bandeau);
  document.getElementById("fermer-rappel").onclick = () => {
    bandeau.remove();
    if (location.hash !== "#/reviser") location.hash = "#/reviser";
  };
}
