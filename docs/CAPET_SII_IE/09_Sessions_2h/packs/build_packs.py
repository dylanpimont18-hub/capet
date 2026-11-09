"""Construit les packs imprimables des sessions de 2 h décrites dans sessions.py.

Pour chaque session :
  pdf/Sxx_<slug>_A_IMPRIMER.pdf  fiche de route + pages du sujet + DT + DR + grille
  pdf/Sxx_<slug>_CORRIGE.pdf     page de garde + pages officielles du corrigé + commentaires du jury
Plus pdf/00_PROGRAMME.pdf (vue d'ensemble des sessions).

Usage (depuis la racine du dépôt CAPET) :
  python docs/CAPET_SII_IE/09_Sessions_2h/packs/build_packs.py [dossier_de_travail]
"""
import pathlib
import subprocess
import sys
import tempfile

from pypdf import PdfReader, PdfWriter

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parents[3]          # .../CAPET
sys.path.insert(0, str(ICI))
from sessions import SESSIONS    # noqa: E402

SORTIE = ICI / "pdf"
TRAVAIL = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(tempfile.mkdtemp())
N_TOTAL = len(SESSIONS)

PREAMBULE = r"""\documentclass[11pt]{article}
\usepackage[a4paper,left=1.6cm,right=1.6cm,top=1.7cm,bottom=1.5cm,headsep=0.4cm]{geometry}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{textcomp}
\usepackage[french]{babel}
\usepackage{tabularx,longtable,booktabs,array,xcolor,colortbl,enumitem,amsmath,amssymb,fancyhdr}
\renewcommand{\familydefault}{\sfdefault}
\setlength{\parindent}{0pt}
\setlist{nosep,leftmargin=1.2em}
\pagestyle{fancy}\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\lhead{\small CAPET SII option ingénierie électrique --- révision de l'admissibilité}
\rhead{\small %(ID)s}
\cfoot{\small %(PIED)s}
\newcommand{\titrebloc}[1]{\par\medskip{\large\bfseries #1}\par\smallskip}
\begin{document}
"""


def hm(minutes: float) -> str:
    m = int(round(minutes))
    return f"{m // 60}\\,h\\,{m % 60:02d}"


def plage(debut: int, n: int) -> str:
    return f"p.\\,{debut}" if n == 1 else f"p.\\,{debut}--{debut + n - 1}"


def pages_orig(pages: list[int]) -> str:
    """[6,7,8,10] -> '6--8, 10'."""
    blocs, d = [], pages[0]
    for a, b in zip(pages, pages[1:] + [None]):
        if b != a + 1:
            blocs.append(str(d) if d == a else f"{d}--{a}")
            d = b
    return ", ".join(blocs)


def compiler(nom: str, corps: str, s: dict, pied: str) -> pathlib.Path:
    ident = f"\\textbf{{{s['id']}}} / {N_TOTAL}" if s else f"{N_TOTAL} sessions"
    tex = PREAMBULE % {"ID": ident, "PIED": pied} + corps + "\n\\end{document}\n"
    f = TRAVAIL / f"{nom}.tex"
    f.write_text(tex, encoding="utf-8")
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", f.name],
                       cwd=TRAVAIL, capture_output=True, text=True, encoding="utf-8", errors="replace")
    pdf = TRAVAIL / f"{nom}.pdf"
    if r.returncode != 0 or not pdf.exists():
        log = (TRAVAIL / f"{nom}.log").read_text(encoding="utf-8", errors="replace")
        erreurs = [l for l in log.splitlines() if l.startswith("!")][:5]
        raise RuntimeError(f"pdflatex a échoué pour {nom} : {erreurs}")
    n = len(PdfReader(str(pdf)).pages)
    if n != 1 and nom != "programme":
        raise RuntimeError(f"{nom} fait {n} pages au lieu d'une : à raccourcir")
    return pdf


def nouveau_bloc(prec: str, q: str) -> bool:
    """Vrai si la question q ouvre un nouveau bloc par rapport à prec.

    Questions lettrées (A1, B3…) : changement de lettre. Questions numérotées (Q14…) :
    rupture de la numérotation (Q19 puis Q33, ou Q7 puis Q28)."""
    if q[0] == "Q" and prec[0] == "Q":
        return int(q[1:]) != int(prec[1:]) + 1
    return q[0] != prec[0]


def groupes(s: dict) -> str:
    qs = [q for q, _ in s["questions"]]
    out, d = [], qs[0]
    for a, b in zip(qs, qs[1:] + [None]):
        if b is None or nouveau_bloc(a, b):
            out.append(d if d == a else f"{d} à {a}")
            d = b
    return " ; ".join(out)


def jalons(s: dict, debut: float, duree: float) -> list[tuple[float, str]]:
    qs = [q for q, _ in s["questions"]]
    n = len(qs)
    pas = duree / n

    idx = {0}
    for i in range(1, n):
        if nouveau_bloc(qs[i - 1], qs[i]):
            idx.add(i)
    for frac in (0.25, 0.5, 0.75):
        idx.add(round(n * frac))
    idx = sorted(i for i in idx if i < n)
    lignes = [(debut + i * pas, f"attaquer \\textbf{{{qs[i]}}}") for i in idx]
    # fusionne les jalons trop proches (< 8 min)
    propres = []
    for t, txt in lignes:
        if propres and t - propres[-1][0] < 8:
            continue
        propres.append((t, txt))
    return propres


def fiche_de_route(s: dict, offsets: dict) -> str:
    n = len(s["questions"])
    ref = n * s["min_q"]
    exam = s["format"] == "Examen"
    debut, duree = (0, 120) if exam else (5, 95)
    deroule = ("Examen : 120 min de composition stricte, sans document ; correction dans un créneau séparé de 30 min"
               if exam else "Entraînement : 5 min de lecture, 95 min de composition, 20 min d'auto-correction")
    corr_ouvrir = "après la session, dans le créneau de correction" if exam else "à 1\\,h\\,40, pas avant"
    qs = s["questions"]
    contenu = [f"\\item {plage(1, 1)} : cette fiche de route"]
    contenu.append(f"\\item {plage(*offsets['sujet'])} : énoncé (pages {pages_orig(s['sujet'][1])} du sujet original)")
    if s.get("dt"):
        contenu.append(f"\\item {plage(*offsets['dt'])} : documents techniques --- {s['dt_noms']}")
    contenu.append(f"\\item {plage(*offsets['dr'])} : documents réponses --- {s['dr_noms']} --- "
                   "\\textbf{à imprimer à 100\\,\\%, sans « ajuster à la page »}")
    contenu.append(f"\\item {plage(*offsets['grille'])} : grille d'auto-évaluation")
    lignes_j = [f"0\\,h\\,00 & lire cette fiche et la présentation du support \\\\"] if not exam else []
    for t, txt in jalons(s, debut, duree):
        lignes_j.append(f"{hm(t)} & {txt} \\\\")
    fin = debut + duree
    lignes_j.append(f"{hm(fin)} & {'fin de composition, ouvre le corrigé' if not exam else 'fin de composition, pose le stylo'} \\\\")
    if not exam:
        lignes_j.append("2\\,h\\,00 & grille remplie, BILAN envoyé \\\\")
    notes = "".join(f"\\item {x}\n" for x in s["notes"])
    mq = f"{s['min_q']:.1f}".replace(".", "{,}")
    pt = f"{20 / n:.2f}".replace(".", "{,}")
    return rf"""
{{\LARGE\bfseries Session {s['id']} --- fiche de route}}\par\smallskip
{{\large {s['source']}}}\par\smallskip
{{\large\bfseries {s['titre']}}}\par\medskip
\renewcommand{{\arraystretch}}{{1.25}}
\begin{{tabularx}}{{\textwidth}}{{@{{}}>{{\bfseries}}p{{3.5cm}}X@{{}}}}
\toprule
Format & {deroule} \\
Temps de référence & {round(ref)} min ({n} questions $\times$ {mq} min ; {s['base']}) \\
Questions & {groupes(s)} ({n} questions) \\
Barème indicatif & 20/{n} $\approx$ {pt} point par question (poids égal, non officiel) \\
Thèmes & {s['themes']} \\
Corrigé & officiel, fichier \texttt{{{s['id']}\_CORRIGE.pdf}} : à ouvrir {corr_ouvrir} \\
\bottomrule
\end{{tabularx}}

\titrebloc{{Contenu de ce fichier}}
\begin{{itemize}}\small
{chr(10).join(contenu)}
\end{{itemize}}

\titrebloc{{Jalons}}
\begin{{tabular}}{{@{{}}>{{\bfseries}}l l@{{}}}}
{chr(10).join(lignes_j)}
\end{{tabular}}

\titrebloc{{Consignes de rédaction}}
\begin{{itemize}}\small
\item Expression littérale d'abord, puis application numérique avec unités ; résultat encadré.
\item Une copie par partie, numéro de question en marge ; rends les DR même incomplets.
\item Lis chaque question jusqu'au bout avant d'écrire : c'est l'erreur la plus citée par le jury.
\item Bloqué plus de deux fois le temps prévu sur une question : passe à la suivante et note « T » dans la grille.
\item Calculatrice autorisée.
\end{{itemize}}

\titrebloc{{Points d'attention}}
\begin{{itemize}}\small
{notes}\end{{itemize}}
"""


def grille(s: dict) -> str:
    n = len(s["questions"])
    taille = "\\small" if n <= 18 else "\\footnotesize"
    etirement = "1.55" if n <= 18 else "1.42"
    lignes = "\n".join(
        f"\\textbf{{{q}}} & {lib} & $\\square$ & $\\square$ & $\\square$ & $\\square$ & & \\\\ \\hline"
        for q, lib in s["questions"])
    return rf"""
{{\LARGE\bfseries Grille d'auto-évaluation --- {s['id']}}}\par\smallskip
{{\small Remplis-la pendant la correction. Une case cochée = critère réussi.
Type d'erreur : \textbf{{C}} cours · \textbf{{M}} méthode · \textbf{{A}} calcul ou application numérique ·
\textbf{{L}} lecture de l'énoncé · \textbf{{T}} temps.}}\par\medskip
{taille}\renewcommand{{\arraystretch}}{{{etirement}}}
\begin{{tabularx}}{{\textwidth}}{{|>{{\centering\arraybackslash}}p{{0.75cm}}|X|c|c|c|c|p{{0.9cm}}|p{{1.0cm}}|}}
\hline
\rowcolor{{black!10}}\textbf{{N°}} & \textbf{{Objet de la question}} & \textbf{{Abordée}} & \textbf{{Démarche}} & \textbf{{AN}} & \textbf{{Unités}} & \textbf{{Min}} & \textbf{{Erreur}} \\ \hline
{lignes}
\end{{tabularx}}

\normalsize\medskip
\renewcommand{{\arraystretch}}{{1.6}}
\begin{{tabularx}}{{\textwidth}}{{@{{}}l X@{{}}}}
\textbf{{Score}} & \dotfill\ / {n} questions justes, soit \dotfill\ \% \\
\textbf{{Temps réel}} & \dotfill\ min de composition \\
\textbf{{À revoir}} & 1.\,\dotfill\quad 2.\,\dotfill\quad 3.\,\dotfill \\
\end{{tabularx}}

\medskip{{\small\textbf{{Message pour le suivi}} : \texttt{{BILAN {s['id']} : justes = \ldots/{n} ; ratées = \ldots{{}} (type) ; temps = \ldots{{}} min}}}}
"""


def page_corrige(s: dict, offsets: dict) -> str:
    rows = ""
    if s.get("correspondance"):
        rows = ("\\titrebloc{Correspondance des numéros}\n"
                "\\begin{tabular}{@{}ll@{}}\\toprule\\textbf{Ton sujet (externe)} & \\textbf{Rapport du jury} \\\\ \\midrule\n"
                + "\n".join(f"{a} & {b} \\\\" for a, b in s["correspondance"])
                + "\n\\bottomrule\\end{tabular}\n")
    notes = "".join(f"\\item {x}\n" for x in s.get("corrige_notes", []))
    pages = s["corrige"][1]
    comm = s["corrige"][2]
    contenu = f"\\item {plage(*offsets['corr'])} : éléments de correction officiels (pages {pages_orig(pages)} du rapport)\n"
    if comm:
        contenu += f"\\item {plage(*offsets['comm'])} : commentaires du jury (pages {pages_orig(comm)} du rapport)\n"
    return rf"""
{{\LARGE\bfseries Corrigé --- session {s['id']}}}\par\smallskip
{{\large\bfseries À n'ouvrir qu'après la composition.}}\par\medskip
{{\large {s['source']}}}\par
{s['titre']}\par\medskip
\textbf{{Source}} : {s['corrige_src']}

\titrebloc{{Contenu de ce fichier}}
\begin{{itemize}}
{contenu}\end{{itemize}}
Les pages sont reproduites entières : elles peuvent déborder sur des questions hors session.

{rows}
\titrebloc{{À savoir avant de lire}}
\begin{{itemize}}
{notes}\end{{itemize}}

\titrebloc{{Méthode de correction}}
\begin{{enumerate}}
\item Pour chaque question, compare d'abord la démarche, puis le résultat et ses unités.
\item Remplis la grille au fur et à mesure (dernière page du fichier à imprimer).
\item Lis les commentaires du jury sur les questions que tu as ratées.
\item Envoie ton \texttt{{BILAN}} dans la conversation de suivi.
\end{{enumerate}}
"""


def programme() -> str:
    lignes = []
    for s in SESSIONS:
        n = len(s["questions"])
        court = (s["source"].split(" --- ")[0]
                 .replace("Sujet E1 2026 externe", "E1 2026")
                 .replace("Épreuve disciplinaire IE", "Disciplinaire"))
        lignes.append(f"\\textbf{{{s['id']}}} & {court} & {s['titre']} & {s['format']} & "
                      f"{round(n * s['min_q'])} min & {s['themes']} \\\\ \\hline")
    return rf"""
{{\LARGE\bfseries Programme des {N_TOTAL} sessions de 2\,h}}\par\smallskip
{{\small Ordre conseillé : de S01 à S{N_TOTAL:02d}. Les sessions alternent courant fort et courant faible ;
{", ".join(s["id"] for s in SESSIONS if s["format"] == "Examen")} sont au format Examen (2\,h de composition stricte,
correction à part). Toutes ont un corrigé officiel.}}\par\medskip
\footnotesize\renewcommand{{\arraystretch}}{{1.3}}
\setlength{{\LTpre}}{{4pt}}\setlength{{\LTpost}}{{4pt}}
\begin{{longtable}}{{|p{{0.7cm}}|p{{2.2cm}}|p{{5.3cm}}|p{{1.85cm}}|p{{1.0cm}}|p{{4.0cm}}|}}
\hline\rowcolor{{black!10}}\textbf{{N°}} & \textbf{{Sujet}} & \textbf{{Contenu}} & \textbf{{Format}} & \textbf{{Réf.}} & \textbf{{Thèmes}} \\ \hline
\endhead
{chr(10).join(lignes)}
\end{{longtable}}

\normalsize\medskip
\textbf{{Pour chaque session, deux fichiers}} : \texttt{{Sxx\_\ldots\_A\_IMPRIMER.pdf}} (fiche de route, énoncé, documents
techniques, documents réponses à 100\,\%, grille) et \texttt{{Sxx\_\ldots\_CORRIGE.pdf}} (à imprimer à part et à ne lire
qu'après la composition).
"""


def ajouter(w: PdfWriter, src: str, pages: list[int]) -> None:
    r = PdfReader(str(RACINE / src))
    for p in pages:
        w.add_page(r.pages[p - 1])


def construire(s: dict) -> tuple[pathlib.Path, pathlib.Path]:
    # décalages des sections dans le fichier à imprimer
    off, cur = {}, 2
    for cle in ("sujet", "dt", "dr"):
        if s.get(cle):
            k = len(s[cle][1]); off[cle] = (cur, k); cur += k
    off["grille"] = (cur, 1)
    fiche = compiler(f"{s['id']}_fiche", fiche_de_route(s, off), s, "Fiche de route")
    gr = compiler(f"{s['id']}_grille", grille(s), s, "Grille d'auto-évaluation")

    w = PdfWriter()
    w.add_page(PdfReader(str(fiche)).pages[0])
    for cle in ("sujet", "dt", "dr"):
        if s.get(cle):
            ajouter(w, *s[cle])
    w.add_page(PdfReader(str(gr)).pages[0])
    a_imprimer = SORTIE / f"{s['id']}_{s['slug']}_A_IMPRIMER.pdf"
    w.compress_identical_objects()
    with open(a_imprimer, "wb") as f:
        w.write(f)

    src, pages, comm = s["corrige"]
    offc = {"corr": (2, len(pages))}
    if comm:
        offc["comm"] = (2 + len(pages), len(comm))
    garde = compiler(f"{s['id']}_corrige", page_corrige(s, offc), s, "Corrigé --- page de garde")
    w = PdfWriter()
    w.add_page(PdfReader(str(garde)).pages[0])
    ajouter(w, src, pages + comm)
    corrige = SORTIE / f"{s['id']}_{s['slug']}_CORRIGE.pdf"
    w.compress_identical_objects()
    with open(corrige, "wb") as f:
        w.write(f)
    return a_imprimer, corrige


def main() -> None:
    SORTIE.mkdir(exist_ok=True)
    TRAVAIL.mkdir(parents=True, exist_ok=True)
    prog = compiler("programme", programme(), None, "Programme des sessions")
    (SORTIE / "00_PROGRAMME.pdf").write_bytes(prog.read_bytes())
    for s in SESSIONS:
        a, c = construire(s)
        na, nc = len(PdfReader(str(a)).pages), len(PdfReader(str(c)).pages)
        print(f"{s['id']}  {na:2d} p. {a.stat().st_size / 1e6:5.1f} Mo | corrigé {nc:2d} p. {c.stat().st_size / 1e6:5.1f} Mo")


if __name__ == "__main__":
    main()
