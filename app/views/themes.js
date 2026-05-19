/* ============================================================
   themes.js — Vue liste des thèmes
   ============================================================ */

function renderThemes() {
  const themes = window.DATA.themes;

  return `
    <div>
      <h1>Thèmes</h1>
      <p class="text-muted" style="margin-bottom:20px">30 thèmes · Session 2015–2025</p>

      <div class="flex gap-2" style="flex-wrap:wrap;margin-bottom:20px">
        <button class="btn btn-primary" onclick="filterThemes('all')"    id="filter-all">Tous</button>
        <button class="btn"             onclick="filterThemes('rouge')"  id="filter-rouge">🔴 Prioritaires</button>
        <button class="btn"             onclick="filterThemes('orange')" id="filter-orange">🟠 Importants</button>
        <button class="btn"             onclick="filterThemes('jaune')"  id="filter-jaune">🟡 Mentionnés</button>
      </div>

      <div id="themes-list">
        ${themes.map(t => {
          const pct       = Storage.getThemeProgress(t.id);
          const formCount = window.DATA.formules.filter(f => f.themeId === t.id && !f.donnee).length;
          const epCount   = Object.keys(t.presences).length;
          const dueCount = window.DATA.formules.filter(f =>
            f.themeId === t.id && !f.donnee &&
            Storage.isDue(f.id) && Storage.getFormule(f.id).repetitions > 0
          ).length;
          return `
            <a href="#/theme/${t.id}" data-intensite="${t.intensite}"
               style="text-decoration:none;display:block;margin-bottom:10px">
              <div class="card" style="padding:14px">
                <div class="flex items-center justify-between gap-2">
                  <div class="flex items-center gap-2" style="flex:1;min-width:0">
                    <span class="badge">${t.id}</span>
                    <span style="font-size:14px;font-weight:500;color:var(--text);
                                 overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${t.nom}</span>
                  </div>
                  <div class="flex items-center gap-2">
                    ${dueCount > 0 ? `<span class="badge" style="background:var(--orange,#f59e0b);color:#fff">🔔 ${dueCount}</span>` : ""}
                    ${t.intensite !== "absent" ? `<span class="badge badge-${t.intensite}">${{rouge:"🔴",orange:"🟠",jaune:"🟡"}[t.intensite]} ${t.intensite}</span>` : ""}
                    <span class="text-sm text-muted">${formCount === 0 ? "—" : Math.round(pct * 100) + "%"}</span>
                  </div>
                </div>
                <div class="text-sm text-muted" style="margin:6px 0">
                  ${epCount}/22 épreuves · ${formCount} formule${formCount !== 1 ? "s" : ""} à mémoriser
                </div>
                <div class="progress-bar">
                  <div class="progress-fill ${formCount === 0 ? "" : pct < 0.4 ? "rouge" : pct < 0.75 ? "orange" : "vert"}"
                       style="width:${formCount === 0 ? 0 : Math.round(pct * 100)}%"></div>
                </div>
              </div>
            </a>`;
        }).join("")}
      </div>
    </div>`;
}

function filterThemes(filter) {
  // Mettre à jour les boutons
  ["all", "rouge", "orange", "jaune"].forEach(f => {
    const btn = document.getElementById("filter-" + f);
    if (!btn) return;
    btn.className = f === filter ? "btn btn-primary" : "btn";
  });

  // Afficher/masquer les cartes
  document.querySelectorAll("#themes-list > a").forEach(el => {
    const intensite = el.dataset.intensite;
    if (filter === "all") {
      el.style.display = "block";
    } else {
      el.style.display = intensite === filter ? "block" : "none";
    }
  });
}
