/* ============================================================
   trous.js — Quiz à trous (terme masqué à retrouver)
   ============================================================ */

let _trouCounter = 0;

function renderTrouQuestion(formule) {
  if (!formule.trou) return null;
  const qid = "trou_" + (++_trouCounter);
  const trou = formule.trou;

  const choices = shuffle(trou.choices);

  const jetonsHtml = choices.map((c, idx) => `
    <button
      class="jeton"
      id="${qid}_jeton${idx}"
      onclick="answerTrou('${qid}', '${c.replace(/\\/g, "\\\\").replace(/'/g, "\\'")}', '${trou.maskedTerm.replace(/\\/g, "\\\\").replace(/'/g, "\\'")}', '${formule.id}')"
    >$${c}$</button>`).join("");

  return `
    <div class="card" id="${qid}" style="margin-bottom:16px">
      <div class="text-sm text-muted" style="margin-bottom:8px">Complétez — Quel terme remplace □ ?</div>
      <p style="font-size:16px;font-weight:500;margin-bottom:12px">${formule.description}</p>
      <div style="font-size:20px;margin-bottom:16px;text-align:center">
        $${trou.maskedLatex}$
      </div>
      <div id="${qid}_jetons" style="text-align:center;margin-bottom:8px">${jetonsHtml}</div>
      <div id="${qid}_feedback" style="display:none"></div>
    </div>`;
}

function answerTrou(qid, chosen, correct, formuleId) {
  const isCorrect = chosen === correct;

  // Désactiver les jetons
  document.querySelectorAll(`#${qid}_jetons .jeton`).forEach(btn => {
    btn.classList.add("disabled");
    btn.onclick = null;
  });

  // Mettre en évidence
  document.querySelectorAll(`#${qid}_jetons .jeton`).forEach(btn => {
    const onclick = btn.getAttribute("onclick") || "";
    // Extraire le premier argument du onclick pour identifier le jeton
    const m = onclick.match(/answerTrou\('[^']+',\s*'((?:[^'\\]|\\.)*)'/);
    if (!m) return;
    const btnChosen = m[1].replace(/\\'/g, "'").replace(/\\\\/g, "\\");
    if (btnChosen === correct) {
      btn.classList.add("correct");
    } else if (btnChosen === chosen && !isCorrect) {
      btn.classList.add("wrong");
    }
  });

  const state   = Storage.recordAnswer(formuleId, isCorrect);
  const formule = window.DATA.formules.find(f => f.id === formuleId);
  const fb      = document.getElementById(qid + "_feedback");

  if (fb) {
    const masMsg = state.mastered ? " — <span style='color:var(--vert)'>✅ Maîtrisée !</span>" : "";
    fb.style.display = "block";
    fb.innerHTML = `
      <div class="quiz-feedback ${isCorrect ? "correct" : "wrong"}">
        ${isCorrect ? "✅ Correct !" : `❌ Raté — la réponse était $${correct}$`}${masMsg}
        <div style="margin-top:8px;font-size:13px;color:var(--text2)">
          Formule complète : $${formule ? formule.latex : ""}$
        </div>
      </div>`;
    renderMath(fb);
  }

  document.dispatchEvent(new CustomEvent("quizAnswer", {
    detail: { formuleId, isCorrect },
  }));
}
