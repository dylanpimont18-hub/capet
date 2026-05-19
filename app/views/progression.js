/* ============================================================
   progression.js — Vue Progression
   ============================================================ */

function renderDueSection(allF) {
  const now = Date.now();
  const startOfToday = new Date(); startOfToday.setHours(0,0,0,0);

  // Formules déjà vues (repetitions > 0) et dues aujourd'hui
  const dueToday = allF.filter(f => {
    const s = Storage.getFormule(f.id);
    return s.repetitions > 0 && s.nextReview <= now;
  }).length;

  // Histogramme 7 jours : combien de formules ont nextReview dans chaque journée
  const days = [];
  for (let d = 0; d < 7; d++) {
    const dayStart = startOfToday.getTime() + d * 86400000;
    const dayEnd   = dayStart + 86400000;
    const count = allF.filter(f => {
      const s = Storage.getFormule(f.id);
      return s.repetitions > 0 && s.nextReview >= dayStart && s.nextReview < dayEnd;
    }).length;
    const label = d === 0 ? "Auj." : d === 1 ? "Dem." : `J+${d}`;
    days.push({ label, count });
  }

  const maxCount = Math.max(...days.map(d => d.count), 1);

  const barsHtml = days.map(({ label, count }) => {
    const h = Math.round((count / maxCount) * 60);
    return `
      <div style="display:flex;flex-direction:column;align-items:center;gap:4px;flex:1">
        <span class="text-sm" style="font-size:11px;color:var(--text)">${count}</span>
        <div style="width:100%;background:var(--surface-2,#e5e7eb);border-radius:4px;height:64px;display:flex;align-items:flex-end">
          <div style="width:100%;height:${h}px;background:var(--primary,#6366f1);border-radius:4px;min-height:${count ? 4 : 0}px"></div>
        </div>
        <span class="text-sm" style="font-size:11px;color:var(--muted)">${label}</span>
      </div>`;
  }).join("");

  return `
    <div class="card" style="margin-bottom:24px">
      <div class="flex items-center justify-between" style="margin-bottom:12px">
        <span style="font-weight:600">Révisions dues</span>
        <span class="badge" style="background:${dueToday > 0 ? "var(--orange,#f59e0b)" : "var(--vert,#10b981)"};color:#fff">
          ${dueToday > 0 ? `🔔 ${dueToday} aujourd'hui` : "✓ Rien à réviser"}
        </span>
      </div>
      <div style="display:flex;gap:6px;align-items:flex-end;height:80px">
        ${barsHtml}
      </div>
      <p class="text-muted text-sm" style="margin-top:8px">
        Formules dont la révision SM-2 est planifiée sur les 7 prochains jours.
      </p>
    </div>`;
}

function renderProgression() {
  const themes  = window.DATA.themes;
  const allF    = window.DATA.formules.filter(f => !f.donnee);
  const mastered = allF.filter(f => Storage.isMastered(f.id));
  const pct     = allF.length ? mastered.length / allF.length : 0;
  const pctColor = pct < 0.4 ? "rouge" : pct < 0.75 ? "orange" : "vert";

  const cellsHtml = themes.map(t => {
    const fCount = window.DATA.formules.filter(f => f.themeId === t.id && !f.donnee).length;
    const mCount = window.DATA.formules.filter(f => f.themeId === t.id && !f.donnee && Storage.isMastered(f.id)).length;
    const tp    = fCount > 0 ? Storage.getThemeProgress(t.id) : null;
    const tpPct = tp !== null ? Math.round(tp * 100) : null;
    const color = tp === null ? "" : tp < 0.4 ? "rouge" : tp < 0.75 ? "orange" : "vert";

    return `
      <div class="progression-cell">
        <div class="flex items-center justify-between" style="margin-bottom:6px">
          <span class="badge">${t.id}</span>
          <span class="text-sm text-muted">${mCount}/${fCount}</span>
        </div>
        <div class="cell-name" title="${t.nom}">${t.nom}</div>
        <div class="progress-bar" style="margin:6px 0">
          <div class="progress-fill ${color}" style="width:${tpPct !== null ? tpPct : 0}%"></div>
        </div>
        <div class="flex items-center justify-between">
          <span class="text-sm text-muted">${tpPct !== null ? tpPct + "%" : "—"}</span>
          <button class="btn btn-ghost" style="font-size:12px;padding:2px 8px"
                  onclick="resetTheme('${t.id}', '${t.nom.replace(/'/g, "\\'")}')">Reset</button>
        </div>
      </div>`;
  }).join("");

  return `
    <div>
      <div class="flex items-center justify-between" style="margin-bottom:20px">
        <h1>Progression</h1>
        <button class="btn btn-danger" onclick="resetAll()">🗑️ Tout réinitialiser</button>
      </div>

      <!-- Compteur global -->
      <div class="card" style="margin-bottom:24px">
        <div class="flex items-center justify-between" style="margin-bottom:8px">
          <span style="font-weight:600">${mastered.length} / ${allF.length} formules maîtrisées</span>
          <span class="badge badge-${pctColor}">${Math.round(pct * 100)}%</span>
        </div>
        <div class="progress-bar">
          <div class="progress-fill ${pctColor}" style="width:${Math.round(pct * 100)}%"></div>
        </div>
        <p class="text-muted text-sm" style="margin-top:8px">
          Une formule est maîtrisée après 2 bonnes réponses consécutives.
        </p>
      </div>

      ${renderDueSection(allF)}

      <h2 style="margin-bottom:16px">Par thème</h2>
      <div class="progression-grid">
        ${cellsHtml}
      </div>
    </div>`;
}

function resetTheme(themeId, nomTheme) {
  if (!confirm(`Réinitialiser la progression pour "${nomTheme}" ?`)) return;
  Storage.resetTheme(themeId);
  window.location.reload();
}

function resetAll() {
  if (!confirm("Réinitialiser TOUTE la progression ? Cette action est irréversible.")) return;
  Storage.resetAll();
  window.location.reload();
}
