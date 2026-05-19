/* ============================================================
   formulaire.js — Vue Formulaire global
   ============================================================ */

function renderFormulaire() {
  const formules = window.DATA.formules;
  const domaines = [...new Set(formules.map(f => f.domaine))].sort();

  return `
    <div>
      <h1>Formulaire</h1>
      <p class="text-muted" style="margin-bottom:20px">${formules.length} formules</p>

      <!-- Filtres -->
      <div class="filter-bar">
        <input type="text" id="filt-search" placeholder="Rechercher une formule…"
               oninput="filterFormulaire()" />
        <select id="filt-domaine" onchange="filterFormulaire()">
          <option value="">Tous les domaines</option>
          ${domaines.map(d => `<option value="${d}">${d}</option>`).join("")}
        </select>
        <button class="btn" id="btn-memoriser" onclick="toggleFiltMemoriser()">❌ À mémoriser</button>
        <button class="btn" id="btn-nonmaitr"  onclick="toggleFiltNonMaitr()">🎯 Non maîtrisées</button>
      </div>
      <div class="flex items-center justify-between" style="margin-bottom:12px">
        <span id="filt-count" class="text-muted text-sm">${formules.length} formules affichées</span>
        <button class="btn btn-primary" onclick="startQuizTransversal()">🧩 Quiz transversal</button>
      </div>

      <div id="quiz-transversal" style="margin-bottom:16px"></div>

      <table class="formule-table" id="formule-table-main">
        <thead>
          <tr>
            <th>Formule</th>
            <th>Description</th>
            <th>Domaine</th>
            <th>Donnée ?</th>
            <th>Fréq.</th>
            <th>État</th>
          </tr>
        </thead>
        <tbody>
          ${formules.map(f => `
            <tr
              data-id="${f.id}"
              data-domaine="${f.domaine}"
              data-desc="${f.description.toLowerCase()}"
              data-donnee="${f.donnee ? "oui" : "non"}"
              data-mastered="${Storage.isMastered(f.id) ? "oui" : "non"}"
            >
              <td>$${f.latex}$</td>
              <td>${f.description}</td>
              <td><span class="text-sm text-muted">${f.domaine}</span></td>
              <td>${f.donnee ? "✅ Fournie" : "❌"}</td>
              <td>${f.frequence}</td>
              <td>${Storage.isMastered(f.id) ? '<span class="badge badge-vert">✓</span>' : '<span class="badge text-muted">—</span>'}</td>
            </tr>`).join("")}
        </tbody>
      </table>
    </div>`;
}

/* État des filtres */
let _filtMemoriser = false;
let _filtNonMaitr  = false;

function toggleFiltMemoriser() {
  _filtMemoriser = !_filtMemoriser;
  const btn = document.getElementById("btn-memoriser");
  if (btn) btn.className = _filtMemoriser ? "btn btn-primary" : "btn";
  filterFormulaire();
}

function toggleFiltNonMaitr() {
  _filtNonMaitr = !_filtNonMaitr;
  const btn = document.getElementById("btn-nonmaitr");
  if (btn) btn.className = _filtNonMaitr ? "btn btn-primary" : "btn";
  filterFormulaire();
}

function filterFormulaire() {
  const search  = (document.getElementById("filt-search")?.value || "").toLowerCase();
  const domaine = document.getElementById("filt-domaine")?.value || "";
  let visible   = 0;

  document.querySelectorAll("#formule-table-main tbody tr").forEach(row => {
    const desc      = row.dataset.desc    || "";
    const dom       = row.dataset.domaine || "";
    const donnee    = row.dataset.donnee  === "oui";
    const mastered  = row.dataset.mastered === "oui";

    const okSearch   = !search   || desc.includes(search) || dom.toLowerCase().includes(search);
    const okDomaine  = !domaine  || dom === domaine;
    const okMemoriser = !_filtMemoriser || !donnee;
    const okNonMaitr  = !_filtNonMaitr  || !mastered;

    const show = okSearch && okDomaine && okMemoriser && okNonMaitr;
    row.style.display = show ? "" : "none";
    if (show) visible++;
  });

  const counter = document.getElementById("filt-count");
  if (counter) counter.textContent = `${visible} formule${visible !== 1 ? "s" : ""} affichées`;
}

function startQuizTransversal() {
  const container = document.getElementById("quiz-transversal");
  if (!container) return;

  // Récupérer les formules visibles, non données
  const ids = [];
  document.querySelectorAll("#formule-table-main tbody tr").forEach(row => {
    if (row.style.display !== "none" && row.dataset.donnee !== "oui") {
      ids.push(row.dataset.id);
    }
  });

  const subset = window.DATA.formules.filter(f => ids.includes(f.id));

  if (!subset.length) {
    container.innerHTML = `<p class="text-muted">Aucune formule à mémoriser dans la sélection.</p>`;
    return;
  }

  // Réinitialiser la session quiz
  _quizSession = null;
  const queue = shuffle(subset.filter(f => !Storage.isMastered(f.id)));
  if (!queue.length) {
    container.innerHTML = `<div class="card" style="text-align:center;padding:32px">
      <div style="font-size:48px">🏆</div>
      <h2>Toutes maîtrisées !</h2>
    </div>`;
    return;
  }

  _quizSession = { themeId: null, queue, index: 0, correct: 0, total: 0 };

  container.innerHTML = `
    <div class="card" style="margin-bottom:16px">
      <h3 style="margin-bottom:12px">🧩 Quiz transversal (${queue.length} formules)</h3>
      <div id="quiz-question"></div>
      <button id="quiz-next" class="btn btn-primary" style="display:none;margin-top:12px"
              onclick="nextQuizQuestion()">Question suivante →</button>
      <div id="quiz-results" style="display:none"></div>
    </div>`;

  if (_quizListener) document.removeEventListener("quizAnswer", _quizListener);
  _quizListener = function(e) {
    if (!_quizSession) return;
    _quizSession.total++;
    if (e.detail.isCorrect) _quizSession.correct++;
    const nextBtn = document.getElementById("quiz-next");
    if (nextBtn) nextBtn.style.display = "inline-block";
  };
  document.addEventListener("quizAnswer", _quizListener);

  nextQuizQuestion();
}
