/* ============================================================
   theme.js — Vue détail d'un thème (onglets Fiche/Formules/Quiz/Sujets)
   ============================================================ */

/* ----------------------------------------------------------
   Helpers partagés (utilisés aussi par formulaire.js)
   ---------------------------------------------------------- */

function mdToHtml(md) {
  if (!md) return "";
  // Protéger les formules LaTeX inline $...$ et $$...$$
  const math = [];
  let s = md;

  // Remplacer $$...$$ et $...$ par des placeholders
  s = s.replace(/\$\$[\s\S]*?\$\$/g, m => { math.push(m); return `@@MATH${math.length - 1}@@`; });
  s = s.replace(/\$[^$\n]+?\$/g,     m => { math.push(m); return `@@MATH${math.length - 1}@@`; });

  const lines  = s.split("\n");
  const out    = [];
  let inList   = false;
  let inTable  = false;
  let tableRows = [];

  function flushTable() {
    if (!tableRows.length) return;
    const rows = tableRows;
    tableRows = [];
    inTable = false;
    let html = '<table style="width:100%;border-collapse:collapse;margin:10px 0;font-size:13px">';
    rows.forEach((row, i) => {
      if (i === 1 && row.every(c => /^[-: ]+$/.test(c))) return; // séparateur
      const tag = i === 0 ? "th" : "td";
      html += "<tr>" + row.map(c => `<${tag} style="padding:7px 10px;border:1px solid var(--border)">${c}</${tag}>`).join("") + "</tr>";
    });
    html += "</table>";
    out.push(html);
  }

  function flushList() {
    if (inList) { out.push("</ul>"); inList = false; }
  }

  lines.forEach(line => {
    // Tables Markdown
    if (line.trim().startsWith("|")) {
      if (inList) flushList();
      inTable = true;
      const cells = line.split("|").slice(1, -1).map(c => c.trim());
      tableRows.push(cells);
      return;
    }
    if (inTable) flushTable();

    // Headers
    const hm = line.match(/^(#{1,3})\s+(.+)/);
    if (hm) {
      flushList();
      const level = hm[1].length;
      out.push(`<h${level}>${hm[2]}</h${level}>`);
      return;
    }

    // Listes
    const lm = line.match(/^[*\-]\s+(.+)/);
    if (lm) {
      if (!inList) { out.push("<ul>"); inList = true; }
      out.push(`<li>${applyInline(lm[1])}</li>`);
      return;
    }

    // HR
    if (/^---+$/.test(line.trim())) {
      flushList();
      out.push("<hr>");
      return;
    }

    // Paragraphe
    if (line.trim()) {
      flushList();
      out.push(`<p>${applyInline(line)}</p>`);
    } else {
      flushList();
    }
  });

  if (inTable) flushTable();
  if (inList)  out.push("</ul>");

  let result = out.join("\n");

  // Restaurer les formules
  result = result.replace(/@@MATH(\d+)@@/g, (_, i) => math[parseInt(i)]);

  return result;
}

function applyInline(s) {
  // Gras **...**
  s = s.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
  // Italique *...*
  s = s.replace(/\*(.+?)\*/g, "<em>$1</em>");
  // Code `...`
  s = s.replace(/`(.+?)`/g, "<code>$1</code>");
  return s;
}

/* ----------------------------------------------------------
   État de session quiz (partagé avec formulaire.js)
   ---------------------------------------------------------- */
let _quizSession    = null;
let _quizListener   = null;

function startQuiz(themeId) {
  // Tri SM-2 : formules dues en premier, puis par consecutive croissant (les moins maîtrisées d'abord)
  const candidates = window.DATA.formules.filter(f => f.themeId === themeId && !f.donnee && !Storage.isMastered(f.id));
  const queue = Storage.sortByPriority(candidates);
  _quizSession = { themeId, queue, index: 0, correct: 0, total: 0 };

  if (_quizListener) document.removeEventListener("quizAnswer", _quizListener);
  _quizListener = function(e) {
    if (!_quizSession) return;
    _quizSession.total++;
    if (e.detail.isCorrect) _quizSession.correct++;

    // Mise à jour immédiate du badge dans l'onglet Formules
    const row = document.getElementById("frow_" + e.detail.formuleId);
    if (row && Storage.isMastered(e.detail.formuleId)) {
      const cells = row.querySelectorAll("td");
      if (cells.length) cells[cells.length - 1].innerHTML = '<span class="badge badge-vert">✓ Maîtrisée</span>';
    }

    const nextBtn = document.getElementById("quiz-next");
    if (nextBtn) nextBtn.style.display = "inline-block";
  };
  document.addEventListener("quizAnswer", _quizListener);

  nextQuizQuestion();
}

function nextQuizQuestion() {
  if (!_quizSession) return;
  const { queue, index } = _quizSession;

  if (index >= queue.length) {
    showQuizResults();
    return;
  }

  _quizSession.index++;
  const formule = queue[index];
  const allF    = window.DATA.formules;

  // Choisir type : trou si disponible et 50%
  let html = null;
  if (formule.trou && Math.random() < 0.5) {
    html = renderTrouQuestion(formule);
  }
  if (!html) {
    html = renderQCMQuestion(formule, allF);
  }

  const container = document.getElementById("quiz-question");
  if (container) {
    container.innerHTML = html;
    renderMath(container);
  }

  const nextBtn = document.getElementById("quiz-next");
  if (nextBtn) nextBtn.style.display = "none";
}

function showQuizResults() {
  if (_quizListener) {
    document.removeEventListener("quizAnswer", _quizListener);
    _quizListener = null;
  }

  const s    = _quizSession;
  const pct  = s && s.total ? Math.round((s.correct / s.total) * 100) : 0;
  const emoji = pct >= 80 ? "🏆" : pct >= 50 ? "👍" : "💪";

  const container = document.getElementById("quiz-results");
  if (container) {
    container.style.display = "block";
    container.innerHTML = `
      <div class="card" style="text-align:center;padding:32px">
        <div style="font-size:48px;margin-bottom:12px">${emoji}</div>
        <h2>${pct}% de réussite</h2>
        <p class="text-muted" style="margin:8px 0">${s ? s.correct : 0} / ${s ? s.total : 0} bonnes réponses</p>
        <button class="btn btn-primary" style="margin-top:16px"
                onclick="window.location.reload()">Rejouer</button>
      </div>`;
  }

  const questionContainer = document.getElementById("quiz-question");
  if (questionContainer) questionContainer.innerHTML = "";
  const nextBtn = document.getElementById("quiz-next");
  if (nextBtn) nextBtn.style.display = "none";
}

/* ----------------------------------------------------------
   Rendu onglet Quiz
   ---------------------------------------------------------- */
function renderOngletQuiz(themeId, formulesAMemoriser) {
  const allMastered = formulesAMemoriser.every(f => Storage.isMastered(f.id));

  if (allMastered && formulesAMemoriser.length > 0) {
    return `
      <div style="text-align:center;padding:40px 20px">
        <div style="font-size:48px;margin-bottom:12px">🏆</div>
        <h2>Toutes les formules maîtrisées !</h2>
        <p class="text-muted" style="margin:8px 0">Excellent travail. Vous pouvez recommencer pour consolider.</p>
        <button class="btn btn-primary" style="margin-top:16px"
                onclick="Storage.resetTheme('${themeId}');window.location.reload()">Recommencer</button>
      </div>`;
  }

  const remaining = formulesAMemoriser.filter(f => !Storage.isMastered(f.id)).length;

  return `
    <div>
      <p class="text-muted" style="margin-bottom:16px">${remaining} formule${remaining !== 1 ? "s" : ""} restante${remaining !== 1 ? "s" : ""} à maîtriser</p>
      <div id="quiz-question"></div>
      <button id="quiz-next" class="btn btn-primary" style="display:none;margin-bottom:16px"
              onclick="nextQuizQuestion()">Question suivante →</button>
      <div id="quiz-results" style="display:none"></div>
    </div>`;
}

/* ----------------------------------------------------------
   Rendu onglet Sujets
   ---------------------------------------------------------- */
function renderOngletSujets(theme) {
  const sujets = window.DATA.sujets.filter(s => s.themes.includes(theme.id));

  if (!sujets.length) {
    return `<p class="text-muted">Aucun sujet associé à ce thème.</p>`;
  }

  return sujets.map(s => {
    const colKey    = `${s.annee}_${s.epreuve}`;
    const intensite = theme.presences[colKey];
    const badgeHtml = intensite
      ? `<span class="badge badge-${intensite}">${{rouge:"🔴",orange:"🟠",jaune:"🟡"}[intensite] || ""} ${intensite}</span>`
      : "";
    const btnId = `sujet_btn_${s.annee}_${s.epreuve.replace(" ", "_")}`;
    const divId = `sujet_div_${s.annee}_${s.epreuve.replace(" ", "_")}`;

    return `
      <div class="card" style="margin-bottom:12px">
        <div class="flex items-center justify-between gap-2">
          <div>
            <div class="flex items-center gap-2">
              <span class="badge">${s.annee} ${s.epreuve}</span>
              ${badgeHtml}
            </div>
            <div style="font-size:14px;margin-top:4px;color:var(--text2)">${s.titre}</div>
          </div>
          <button id="${btnId}" class="btn"
                  onclick="loadSujet('${btnId}', '${divId}', '${s.path}')">
            📄 Lire le sujet
          </button>
        </div>
        <div id="${divId}" style="display:none"></div>
      </div>`;
  }).join("");
}

function loadSujet(btnId, divId, path) {
  const div = document.getElementById(divId);
  const btn = document.getElementById(btnId);
  if (!div) return;

  if (div.style.display !== "none") {
    div.style.display = "none";
    if (btn) btn.textContent = "📄 Lire le sujet";
    return;
  }

  if (div.innerHTML) {
    div.style.display = "block";
    if (btn) btn.textContent = "▲ Replier";
    return;
  }

  if (btn) btn.textContent = "⏳ Chargement…";

  fetch(path)
    .then(r => {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.text();
    })
    .then(md => {
      div.innerHTML = `<div class="sujet-content">${mdToHtml(md)}</div>`;
      renderMath(div);
      div.style.display = "block";
      if (btn) btn.textContent = "▲ Replier";
    })
    .catch(err => {
      div.innerHTML = `
        <div class="card" style="margin-top:12px;border-color:var(--jaune)">
          <p class="text-muted" style="font-size:13px">
            ⚠️ Impossible de charger le sujet (${err.message}).<br>
            En mode <code>file://</code>, les fichiers Markdown ne peuvent pas être chargés.<br>
            Lancez un serveur local : <code>python -m http.server 8080</code>
          </p>
        </div>`;
      div.style.display = "block";
      if (btn) btn.textContent = "📄 Lire le sujet";
    });
}

/* ----------------------------------------------------------
   Gestion des onglets
   ---------------------------------------------------------- */
function switchTab(event, name) {
  const themeId = event.currentTarget.dataset.themeId;

  // Mettre à jour les classes des boutons
  document.querySelectorAll(".tab[data-theme-id]").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.tabName === name);
  });

  // Afficher/masquer les panneaux
  ["fiche", "formules", "quiz", "sujets"].forEach(tab => {
    const panel = document.getElementById("panel-" + tab);
    if (panel) panel.style.display = tab === name ? "block" : "none";
  });

  // Actions spéciales
  if (name === "fiche") {
    const panel = document.getElementById("panel-fiche");
    if (panel) renderMath(panel);
  }

  if (name === "quiz") {
    _quizSession = null;
    startQuiz(themeId);
  }
}

/* ----------------------------------------------------------
   Rendu principal de la vue thème
   ---------------------------------------------------------- */
function renderTheme(id) {
  const theme = window.DATA.themes.find(t => t.id === id);
  if (!theme) return `<p>Thème "${id}" introuvable.</p>`;

  const formules         = window.DATA.formules.filter(f => f.themeId === id);
  const formulesAMemoriser = formules.filter(f => !f.donnee);
  const epCount          = Object.keys(theme.presences).length;
  const pct              = Storage.getThemeProgress(id);
  const remaining        = formulesAMemoriser.filter(f => !Storage.isMastered(f.id)).length;
  const intensiteMap     = { rouge: "🔴", orange: "🟠", jaune: "🟡" };
  const pctColor         = pct < 0.4 ? "rouge" : pct < 0.75 ? "orange" : "vert";

  /* --- Onglet Fiche --- */
  let ficheContent = "";
  if (theme.hasFiche && theme.fichePath) {
    ficheContent = `<div id="fiche-content"><p class="text-muted text-sm">Chargement de la fiche…</p></div>`;
  } else {
    // Tableau de formules simplifié
    ficheContent = `
      <table class="formule-table">
        <thead><tr>
          <th>Formule</th><th>Description</th>
        </tr></thead>
        <tbody>
          ${formules.map(f => `
            <tr>
              <td>$${f.latex}$</td>
              <td>${f.description}</td>
            </tr>`).join("")}
        </tbody>
      </table>`;
  }

  /* --- Onglet Formules --- */
  const formulesContent = `
    <table class="formule-table">
      <thead><tr>
        <th>Formule</th><th>Description</th><th>Donnée ?</th><th>Fréq.</th><th>État</th>
      </tr></thead>
      <tbody>
        ${formules.map(f => `
          <tr id="frow_${f.id}">
            <td>$${f.latex}$</td>
            <td>${f.description}</td>
            <td>${f.donnee ? "✅ Fournie" : "❌ À mémoriser"}</td>
            <td>${f.frequence}</td>
            <td>${Storage.isMastered(f.id) ? '<span class="badge badge-vert">✓ Maîtrisée</span>' : '<span class="badge">En cours</span>'}</td>
          </tr>`).join("")}
      </tbody>
    </table>`;

  /* --- Onglet Quiz --- */
  const quizContent = renderOngletQuiz(id, formulesAMemoriser);

  /* --- Onglet Sujets --- */
  const sujetsContent = renderOngletSujets(theme);

  const html = `
    <div>
      <!-- Header -->
      <div style="margin-bottom:20px">
        <a href="#/themes" class="btn btn-ghost" style="margin-bottom:12px;display:inline-block">← Tous les thèmes</a>
        <h1>${theme.nom}</h1>
        <div class="flex items-center gap-2" style="flex-wrap:wrap;margin:8px 0">
          ${theme.intensite !== "absent" ? `<span class="badge badge-${theme.intensite}">${intensiteMap[theme.intensite] || ""} ${theme.intensite}</span>` : ""}
          <span class="badge">${epCount}/22 épreuves</span>
          <span class="badge">${remaining} formule${remaining !== 1 ? "s" : ""} restante${remaining !== 1 ? "s" : ""}</span>
        </div>
        <div class="progress-bar" style="margin-top:10px">
          <div class="progress-fill ${pctColor}" style="width:${Math.round(pct * 100)}%"></div>
        </div>
        <div class="text-sm text-muted" style="margin-top:4px">${Math.round(pct * 100)}% maîtrisé</div>
      </div>

      <!-- Onglets -->
      <div class="tabs">
        <button class="tab active" data-tab-name="fiche"    data-theme-id="${id}" onclick="switchTab(event,'fiche')">Fiche</button>
        <button class="tab"        data-tab-name="formules" data-theme-id="${id}" onclick="switchTab(event,'formules')">Formules (${formules.length})</button>
        <button class="tab"        data-tab-name="quiz"     data-theme-id="${id}" onclick="switchTab(event,'quiz')">Quiz</button>
        <button class="tab"        data-tab-name="sujets"   data-theme-id="${id}" onclick="switchTab(event,'sujets')">Sujets (${Object.keys(theme.presences).length})</button>
      </div>

      <div id="panel-fiche"    style="display:block">${ficheContent}</div>
      <div id="panel-formules" style="display:none">${formulesContent}</div>
      <div id="panel-quiz"     style="display:none">${quizContent}</div>
      <div id="panel-sujets"   style="display:none">${sujetsContent}</div>
    </div>`;

  // Charger la fiche après rendu
  if (theme.hasFiche && theme.fichePath) {
    setTimeout(() => {
      fetch(theme.fichePath)
        .then(r => {
          if (!r.ok) throw new Error("HTTP " + r.status);
          return r.text();
        })
        .then(md => {
          const el = document.getElementById("fiche-content");
          if (el) {
            el.innerHTML = mdToHtml(md);
            renderMath(el);
          }
        })
        .catch(err => {
          const el = document.getElementById("fiche-content");
          if (el) {
            el.innerHTML = `
              <p class="text-muted text-sm">
                ⚠️ Impossible de charger la fiche (${err.message}).<br>
                Lancez un serveur : <code>python -m http.server 8080</code>
              </p>
              ${ficheContent.replace('<div id="fiche-content"><p class="text-muted text-sm">Chargement de la fiche…</p></div>', '')}`;
          }
        });
    }, 50);
  }

  return html;
}
