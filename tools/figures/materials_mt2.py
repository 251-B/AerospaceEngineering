"""Figures of the Aerospace Materials I Midterm 2 bank (vault/02 - Aerospace Materials I/Problem Bank/).

One module per unit in tools/figures/mat_mt2/ (u4.py phase diagrams, u5.py stress-strain curves, u6.py energy bands,
u7.py hysteresis loops and dipole arrangements) and problems.py for the Part II problems; each registers its figures with
the `figure` decorator of figures/mat_mt2/common.py and draws them with figures/svgkit.py. The vault copies go to
vault/attachments/MAT-MT2/<name>.svg; the web copies use the portal's CSS variables. `python tools/build_materials_bank.py`
writes them; `python tools/materials_bank/preview_figures.py <name> ...` renders PNG previews to inspect the labels.
"""
import importlib
import pkgutil

from figures import mat_mt2
from figures.mat_mt2.common import FIGURES, REG

for _m in sorted(pkgutil.iter_modules(mat_mt2.__path__), key=lambda m: m.name):
    if _m.name != "common":
        importlib.import_module(f"figures.mat_mt2.{_m.name}")


def build():
    """Register every figure in REG (idempotent) and return REG."""
    for name, (fn, alt, caption) in FIGURES.items():
        REG.put(name, fn(), alt, caption)
    return REG
