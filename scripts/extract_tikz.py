# scripts/extract_tikz.py
"""Isolation des environnements TikZ/circuitikz d'une fiche .tex."""

import hashlib
import re
import sys

_ENVS = ("circuitikz", "tikzpicture")


def _hash(code: str) -> str:
    return hashlib.sha1(code.encode("utf-8")).hexdigest()[:12]


def extract_tikz_envs(texte_tex: str) -> list[dict]:
    """Retourne chaque environnement de dessin, dans l'ordre du fichier.

    Gère l'imbrication du même environnement par comptage de profondeur.
    """
    trouves = []
    for env in _ENVS:
        ouvre = re.compile(r"\\begin\{" + env + r"\}")
        ferme = re.compile(r"\\end\{" + env + r"\}")
        for m in ouvre.finditer(texte_tex):
            depart = m.start()
            profondeur = 1
            pos = m.end()
            while profondeur > 0:
                suivant_o = ouvre.search(texte_tex, pos)
                suivant_f = ferme.search(texte_tex, pos)
                if not suivant_f:
                    break  # environnement non fermé : source malformée
                if suivant_o and suivant_o.start() < suivant_f.start():
                    profondeur += 1
                    pos = suivant_o.end()
                else:
                    profondeur -= 1
                    pos = suivant_f.end()
            if profondeur != 0:
                print(f"  ! environnement {env} non ferme, schema ignore",
                      file=sys.stderr)
            if profondeur == 0:
                code = texte_tex[depart:pos]
                trouves.append({"env": env, "code": code, "hash": _hash(code),
                                "_pos": depart})

    trouves.sort(key=lambda d: d["_pos"])
    for d in trouves:
        del d["_pos"]
    return trouves
