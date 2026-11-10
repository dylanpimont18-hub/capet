// app/js/views/reglages.js
import { exporter, importer, reinitialiser, charger, futCorrompu } from "../store.js";

export function vueReglages(racine, data) {
  const progression = charger();
  const n = Object.keys(progression).length;

  const alerteCorruption = futCorrompu()
    ? `<div class="carte alerte-stockage" role="alert" style="margin-bottom:.6rem">
         <p class="consigne">Progression illisible détectée et réinitialisée.
           Si vous avez un export récent, importez-le ci-dessous pour la
           restaurer.</p>
       </div>`
    : "";

  racine.innerHTML = `
    <div class="carte">
      <p class="vedette">Réglages</p>
      <p class="consigne">${n} carte(s) suivie(s) sur ${data.cards.length}.
        Aucun serveur : l'export est votre seule sauvegarde.</p>
      ${alerteCorruption}
      <div class="actions" style="margin-bottom:.6rem">
        <button id="exp">Exporter</button>
        <button id="tel">Télécharger</button>
        <button id="imp">Importer</button>
      </div>
      <button class="revelateur" id="raz" style="background:var(--rate)">
        Tout réinitialiser</button>
      <p id="msg" class="consigne"></p>
      <textarea id="zone" rows="6" style="width:100%;display:none;
        background:var(--bg);color:var(--ink);border:1px solid var(--rule);
        border-radius:8px;padding:.5rem"></textarea>
    </div>`;

  const zone = document.getElementById("zone");
  const msg = document.getElementById("msg");

  document.getElementById("exp").onclick = () => {
    zone.style.display = "block";
    zone.value = exporter();
    zone.select();
    msg.textContent = "Copiez ce texte et conservez-le.";
  };

  // Copier-coller manuel seul a une friction élevée pour la seule vraie
  // sauvegarde de l'app (voir README) : un fichier téléchargé se range de
  // lui-même (iCloud/Drive) sans étape de copie.
  document.getElementById("tel").onclick = () => {
    const blob = new Blob([exporter()], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `capet-progression-${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    msg.textContent = "Fichier téléchargé.";
  };

  document.getElementById("imp").onclick = () => {
    if (zone.style.display === "none" || !zone.value.trim()) {
      zone.style.display = "block";
      zone.value = "";
      msg.textContent = "Collez un export puis cliquez de nouveau sur Importer.";
      return;
    }
    // Écraserait silencieusement toute progression existante sinon — seule
    // action de cet écran aussi destructrice que le RAZ, qui a déjà sa
    // confirmation.
    if (n > 0 && !confirm(`Remplacer les ${n} carte(s) suivie(s) actuelles par cet export ? Action irréversible.`)) {
      msg.textContent = "Import annulé.";
      return;
    }
    msg.textContent = importer(zone.value)
      ? "Progression restaurée. Rechargez la page."
      : "Import refusé : le contenu n'est pas un export valide.";
  };

  document.getElementById("raz").onclick = () => {
    if (confirm("Effacer toute la progression ? Action irréversible.")) {
      reinitialiser();
      msg.textContent = "Progression effacée.";
    }
  };
}
