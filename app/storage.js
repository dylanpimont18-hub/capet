const Storage = (() => {
  const PREFIX = "capet_";

  function key(id) { return PREFIX + "f_" + id; }

  function _defaults() {
    return { mastered: false, correct: 0, attempts: 0, consecutive: 0,
             ef: 2.5, interval: 0, repetitions: 0, nextReview: 0 };
  }

  function getFormule(id) {
    try {
      const s = JSON.parse(localStorage.getItem(key(id)));
      return s ? Object.assign(_defaults(), s) : _defaults();
    } catch {
      return _defaults();
    }
  }

  /* SM-2 : recordAnswer met à jour ef/interval/repetitions/nextReview */
  function recordAnswer(id, isCorrect) {
    const s = getFormule(id);
    s.attempts++;
    if (isCorrect) {
      s.correct++;
      s.consecutive++;
      // Mise à jour EF (SM-2, r=5 pour bonne réponse)
      s.ef = Math.max(1.3, s.ef + 0.1);
      // Calcul intervalle SM-2
      if (s.repetitions === 0)      s.interval = 1;
      else if (s.repetitions === 1) s.interval = 6;
      else                          s.interval = Math.round(s.interval * s.ef);
      s.repetitions++;
      s.nextReview = Date.now() + s.interval * 86400000;
      if (s.consecutive >= 2) s.mastered = true;
    } else {
      s.consecutive = 0;
      s.repetitions = 0;
      s.interval     = 1;
      s.nextReview   = Date.now() + 86400000;
      s.ef = Math.max(1.3, s.ef - 0.2);
    }
    localStorage.setItem(key(id), JSON.stringify(s));
    return s;
  }

  function isMastered(id) { return !!getFormule(id).mastered; }

  /* Retourne true si la formule est due pour révision (SM-2) */
  function isDue(id) {
    const s = getFormule(id);
    return !s.nextReview || s.nextReview <= Date.now();
  }

  function getThemeProgress(themeId) {
    const formules = window.DATA.formules.filter(f => f.themeId === themeId && !f.donnee);
    if (!formules.length) return 0;
    return formules.filter(f => isMastered(f.id)).length / formules.length;
  }

  /* Trie une liste de formules selon la priorité SM-2 (due > non-due, puis par consecutive croissant) */
  function sortByPriority(formules) {
    const now = Date.now();
    const due    = formules.filter(f => isDue(f.id));
    const notDue = formules.filter(f => !isDue(f.id));
    const byConsec = arr => arr.slice().sort((a, b) =>
      (getFormule(a.id).consecutive || 0) - (getFormule(b.id).consecutive || 0)
    );
    return [...byConsec(due), ...byConsec(notDue)];
  }

  function resetTheme(themeId) {
    window.DATA.formules
      .filter(f => f.themeId === themeId)
      .forEach(f => localStorage.removeItem(key(f.id)));
  }

  function resetAll() {
    Object.keys(localStorage)
      .filter(k => k.startsWith(PREFIX))
      .forEach(k => localStorage.removeItem(k));
  }

  function getPriorityScore(theme) {
    const poids = { rouge: 3, orange: 2, jaune: 1, absent: 0 };
    return (poids[theme.intensite] || 0) * (1 - getThemeProgress(theme.id));
  }

  return { getFormule, recordAnswer, isMastered, isDue, sortByPriority,
           getThemeProgress, resetTheme, resetAll, getPriorityScore };
})();
