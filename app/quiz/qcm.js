/* ============================================================
   qcm.js — Quiz QCM (formule à retrouver)
   ============================================================ */

function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

let _qcmCounter = 0;

function renderQCMQuestion(formule, allFormules) {
  const qid = "qcm_" + (++_qcmCounter);

  // Distracteurs : même domaine en priorité, sinon même thème
  const sameDomain = allFormules.filter(f => f.id !== formule.id && f.domaine === formule.domaine);
  const sameTheme  = allFormules.filter(f => f.id !== formule.id && f.themeId === formule.themeId && f.domaine !== formule.domaine);
  const pool       = sameDomain.length >= 3 ? sameDomain : [...sameDomain, ...sameTheme];
  const distractors = shuffle(pool).slice(0, 3);

  const options = shuffle([formule, ...distractors]);

  const optionsHtml = options.map((f, idx) => {
    const isCorrect = f.id === formule.id;
    return `<button
      class="quiz-option"
      id="${qid}_opt${idx}"
      onclick="answerQCM('${qid}', ${isCorrect}, '${formule.id}', '${f.id}')"
    >$${f.latex}$</button>`;
  }).join("");

  return `
    <div class="card" id="${qid}" style="margin-bottom:16px">
      <div class="text-sm text-muted" style="margin-bottom:8px">QCM — Quelle est la formule pour :</div>
      <p style="font-size:16px;font-weight:500;margin-bottom:16px">${formule.description}</p>
      <div id="${qid}_opts">${optionsHtml}</div>
      <div id="${qid}_feedback" style="display:none"></div>
    </div>`;
}

function answerQCM(qid, isCorrect, formuleId, chosenId) {
  // Désactiver toutes les options
  document.querySelectorAll(`#${qid}_opts .quiz-option`).forEach(btn => {
    btn.classList.add("disabled");
    btn.onclick = null;
  });

  // Colorer correct/wrong
  document.querySelectorAll(`#${qid}_opts .quiz-option`).forEach(btn => {
    const onclick = btn.getAttribute("onclick") || "";
    const m = onclick.match(/'([^']+)', '([^']+)'\)$/);
    if (!m) return;
    const bFormuleId = m[1];
    const bChosenId  = m[2];
    if (bChosenId === bFormuleId) {
      btn.classList.add("correct");
    } else if (bChosenId === chosenId && !isCorrect) {
      btn.classList.add("wrong");
    }
  });

  // Colorer la bonne réponse en vert
  document.querySelectorAll(`#${qid}_opts .quiz-option`).forEach(btn => {
    const onclick = btn.getAttribute("onclick") || "";
    // La bonne option = celle où formuleId == chosenId dans l'attribut
    // On la retrouve par le paramètre isCorrect passé lors du onclick dynamique
  });

  const state   = Storage.recordAnswer(formuleId, isCorrect);
  const formule = window.DATA.formules.find(f => f.id === formuleId);
  const fb      = document.getElementById(qid + "_feedback");

  if (fb) {
    const masMsg = state.mastered ? " — <span style='color:var(--vert)'>✅ Maîtrisée !</span>" : "";
    fb.style.display = "block";
    fb.innerHTML = `
      <div class="quiz-feedback ${isCorrect ? "correct" : "wrong"}">
        ${isCorrect ? "✅ Correct !" : "❌ Raté"}${masMsg}
        <div style="margin-top:8px;font-size:13px;color:var(--text2)">
          Formule : $${formule ? formule.latex : ""}$
        </div>
      </div>`;
    renderMath(fb);
  }

  document.dispatchEvent(new CustomEvent("quizAnswer", {
    detail: { formuleId, isCorrect },
  }));
}
