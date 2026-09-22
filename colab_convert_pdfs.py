!pip install marker-pdf tqdm pymupdf4llm -q

import subprocess
subprocess.run(["nvidia-smi"], check=True)

from google.colab import drive
drive.mount("/content/drive")

from IPython.display import display, Javascript
display(Javascript("""
function keepAlive() {
    console.log("keep-alive ping");
    var btn = document.querySelector("colab-toolbar-button#connect");
    if (btn) btn.click();
}
setInterval(keepAlive, 60000);
"""))

import json
import zipfile
import time
from pathlib import Path
from tqdm.notebook import tqdm

ZIP_NAME   = "/content/drive/My Drive/PDFs_CAPET_SII_IE.zip"
INPUT_DIR  = Path("/content/capet/pdfs")
OUTPUT_DIR = Path("/content/drive/My Drive/CAPET_Markdown")

INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Extraction du ZIP...")
with zipfile.ZipFile(ZIP_NAME, "r") as z:
    z.extractall(INPUT_DIR)

pdfs = sorted(INPUT_DIR.rglob("*.pdf"))
print(f"{len(pdfs)} PDFs trouves\n")

print("Chargement des modeles Marker...")
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.config.parser import ConfigParser
from marker.output import text_from_rendered

config = ConfigParser({"output_format": "markdown", "langs": "fr"})
models = create_model_dict()
converter = PdfConverter(
    artifact_dict=models,
    config=config.generate_config_dict()
)
print("Modeles charges.\n")

ok, fail = 0, 0
failed = []
t_global = time.time()

bar = tqdm(pdfs, desc="Conversion", unit="pdf")
for pdf in bar:
    rel = pdf.relative_to(INPUT_DIR)
    out_dir = OUTPUT_DIR / rel.parent / rel.stem
    out_dir.mkdir(parents=True, exist_ok=True)

    bar.set_postfix_str(str(rel)[:40])

    if any(out_dir.glob("*.md")):
        ok += 1
        bar.write(f"  SKIP : {rel}")
        continue

    t0 = time.time()
    try:
        rendered = converter(str(pdf))
        text, _, images = text_from_rendered(rendered)

        (out_dir / (rel.stem + ".md")).write_text(text, encoding="utf-8")

        for img_name, img in images.items():
            img_path = out_dir / img_name
            fmt = img_path.suffix.lstrip(".").upper() or "PNG"
            if fmt == "JPG":
                fmt = "JPEG"
            if hasattr(img, "save"):
                img.save(img_path, format=fmt)
            else:
                img_path.write_bytes(img)

        elapsed = time.time() - t0
        bar.write(f"  OK  {rel}  ({len(text)} chars, {len(images)} images, {elapsed:.0f}s)")
        ok += 1

    except Exception as e:
        bar.write(f"  WARN marker echoue ({e.__class__.__name__}), fallback pymupdf4llm...")
        try:
            import pymupdf4llm
            text = pymupdf4llm.to_markdown(str(pdf))
            (out_dir / (rel.stem + ".md")).write_text(text, encoding="utf-8")
            elapsed = time.time() - t0
            bar.write(f"  OK  {rel}  (fallback, {len(text)} chars, {elapsed:.0f}s)")
            ok += 1
        except Exception as e2:
            bar.write(f"  ERR {rel} : {e2}")
            fail += 1
            failed.append(str(rel))

total_min = (time.time() - t_global) / 60
print(f"\n=== TERMINE : {ok} OK / {fail} echecs  —  {total_min:.1f} min ===")
if failed:
    print("Echecs :")
    for f in failed:
        print(f"  - {f}")

print(f"\nFichiers disponibles dans Drive : CAPET_Markdown/")
