const Theme = (() => {
  const KEY = "capet_theme";

  function apply(mode) {
    document.body.classList.toggle("light", mode === "light");
    const btn = document.getElementById("theme-toggle");
    if (btn) btn.textContent = mode === "light" ? "🌙 Nuit" : "☀️ Jour";
  }

  function init() {
    apply(localStorage.getItem(KEY) || "dark");
  }

  function toggle() {
    const next = document.body.classList.contains("light") ? "dark" : "light";
    localStorage.setItem(KEY, next);
    apply(next);
  }

  return { init, toggle };
})();
