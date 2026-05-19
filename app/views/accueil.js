/* ============================================================
   accueil.js — Vue Accueil
   ============================================================ */

function statCard(val, label, icon) {
  return `
    <div class="stat-card">
      <div class="stat-icon">${icon}</div>
      <div class="stat-val">${val}</div>
      <div class="stat-label">${label}</div>
    </div>`;
}

function badgeIntensiteHtml(intensite) {
  if (!intensite || intensite === "absent") return "";
  const map = { rouge: "🔴", orange: "🟠", jaune: "🟡" };
  return `<span class="badge badge-${intensite}">${map[intensite] || ""} ${intensite.charAt(0).toUpperCase() + intensite.slice(1)}</span>`;
}

function progressBarHtml(pct) {
  const color = pct < 0.4 ? "rouge" : pct < 0.75 ? "orange" : "vert";
  return `
    <div class="progress-bar" style="margin-top:8px">
      <div class="progress-fill ${color}" style="width:${Math.round(pct * 100)}%"></div>
    </div>`;
}

function themeRow(t) {
  const pct  = Storage.getThemeProgress(t.id);
  const formCount = window.DATA.formules.filter(f => f.themeId === t.id && !f.donnee).length;
  return `
    <a href="#/theme/${t.id}" style="text-decoration:none;display:block;margin-bottom:10px">
      <div class="card" style="padding:14px">
        <div class="flex items-center justify-between gap-2">
          <div class="flex items-center gap-2" style="flex:1;min-width:0">
            <span class="badge">${t.id}</span>
            <span style="font-size:14px;font-weight:500;color:var(--text);overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${t.nom}</span>
          </div>
          <div class="flex items-center gap-2">
            ${badgeIntensiteHtml(t.intensite)}
            <span class="text-sm text-muted">${Math.round(pct * 100)}%</span>
          </div>
        </div>
        ${progressBarHtml(pct)}
        <div class="text-sm text-muted" style="margin-top:6px">${formCount} formule${formCount !== 1 ? "s" : ""} à mémoriser</div>
      </div>
    </a>`;
}

function renderAccueil() {
  const data = window.DATA;

  // Compte à rebours
  const today     = new Date();
  const epreuve   = new Date(data.dateEpreuve);
  const diffMs    = epreuve - today;
  const diffDays  = Math.max(0, Math.ceil(diffMs / (1000 * 60 * 60 * 24)));

  // Stats
  const allFormules      = data.formules.filter(f => !f.donnee);
  const mastered         = allFormules.filter(f => Storage.isMastered(f.id));
  const themesVus        = data.themes.filter(t => {
    const fm = data.formules.filter(f => f.themeId === t.id && !f.donnee);
    return fm.length > 0 && Storage.getThemeProgress(t.id) > 0;
  });
  const restantes        = allFormules.length - mastered.length;

  // Suggestion : thème rouge/orange avec score max
  const prioritaires = data.themes
    .filter(t => t.intensite === "rouge" || t.intensite === "orange")
    .sort((a, b) => Storage.getPriorityScore(b) - Storage.getPriorityScore(a));
  const suggestion = prioritaires[0];

  // Points aveugles
  const pa4 = data.pointsAveugles.slice(0, 4);

  // Thèmes prioritaires (max 6)
  const top6 = prioritaires.slice(0, 6);

  return `
    <div>
      <div class="flex items-center justify-between gap-4" style="margin-bottom:24px">
        <div>
          <h1>Révision CAPET SII IE 2026</h1>
          <p class="text-muted">Session 2026 — Ingénierie Électrique</p>
        </div>
        <div class="badge badge-rouge" style="font-size:18px;padding:8px 16px">J-${diffDays}</div>
      </div>

      <div class="stats-grid">
        ${statCard(themesVus.length, "thèmes vus", "📚")}
        ${statCard(mastered.length, "formules maîtrisées", "✅")}
        ${statCard(restantes, "formules restantes", "🎯")}
      </div>

      ${suggestion ? `
      <div class="card" style="border-left:3px solid var(--vert);margin-bottom:16px">
        <div class="flex items-center justify-between gap-2" style="margin-bottom:8px">
          <div>
            <div class="text-sm text-muted" style="margin-bottom:4px">💡 Suggestion du jour</div>
            <div style="font-weight:600">${suggestion.nom}</div>
          </div>
          ${badgeIntensiteHtml(suggestion.intensite)}
        </div>
        ${progressBarHtml(Storage.getThemeProgress(suggestion.id))}
        <div style="margin-top:12px">
          <a href="#/theme/${suggestion.id}" class="btn btn-primary">Commencer →</a>
        </div>
      </div>` : ""}

      ${pa4.length > 0 ? `
      <div class="card" style="border-left:3px solid var(--jaune);margin-bottom:24px">
        <h3 style="margin-bottom:12px">⚠️ Points aveugles signalés par le jury</h3>
        <ul style="padding-left:20px;font-size:14px">
          ${pa4.map(p => `<li style="margin-bottom:6px"><strong>${p.texte}</strong>${p.detail && p.detail !== p.texte ? " — " + p.detail : ""}</li>`).join("")}
        </ul>
      </div>` : ""}

      <h2 style="margin-bottom:12px">Thèmes prioritaires</h2>
      ${top6.map(t => themeRow(t)).join("")}
    </div>`;
}
