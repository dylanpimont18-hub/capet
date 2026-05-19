const ROUTES = {
  "/accueil":     ()  => renderAccueil(),
  "/themes":      ()  => renderThemes(),
  "/theme/:id":   (p) => renderTheme(p.id),
  "/formulaire":  ()  => renderFormulaire(),
  "/progression": ()  => renderProgression(),
};

function resolveRoute(hash) {
  const path = hash.replace(/^#/, "") || "/accueil";
  for (const [pattern, handler] of Object.entries(ROUTES)) {
    const keys = [];
    const re = new RegExp(
      "^" + pattern.replace(/:(\w+)/g, (_, k) => { keys.push(k); return "([^/]+)"; }) + "$"
    );
    const m = path.match(re);
    if (m) {
      const params = Object.fromEntries(keys.map((k, i) => [k, m[i + 1]]));
      return { handler, params };
    }
  }
  return { handler: () => "<p>Page introuvable</p>", params: {} };
}

function navigate() {
  const { handler, params } = resolveRoute(window.location.hash);
  const app = document.getElementById("app");
  app.innerHTML = handler(params);
  renderMath(app);
  document.querySelectorAll(".nav-link").forEach(a => {
    a.classList.toggle("active", window.location.hash.startsWith(a.getAttribute("href")));
  });
  window.scrollTo(0, 0);
}

window.addEventListener("hashchange", navigate);
window.addEventListener("DOMContentLoaded", () => {
  Theme.init();
  if (!window.location.hash) window.location.hash = "#/accueil";
  navigate();
});
