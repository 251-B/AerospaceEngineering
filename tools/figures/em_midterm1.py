"""Figures of the Engineering Mechanics Midterm 1 problem bank (vault/03 - Engineering Mechanics/Problem Bank/).

One module per bank item in tools/figures/em_m1/ (pNN.py, cNN.py); each registers its figures with the `figure` decorator of
figures/em_common.py. Every figure is an engineering sketch drawn with the primitives of figures/mech.py in the units of its
problem. The vault copies go to vault/attachments/EM-M1/<name>.svg; the web copies use the portal's CSS variables (see
figures/svgkit.py). `python scripts/generate_diagrams.py` writes them, lists label collisions and renders PNG previews.
"""
import importlib
import pkgutil

from figures import em_m1
from figures.em_common import FIGURES, REG

for _m in sorted(pkgutil.iter_modules(em_m1.__path__), key=lambda m: m.name):
    importlib.import_module(f"figures.em_m1.{_m.name}")


def build():
    """Register every figure in REG (idempotent) and return the list of overlap warnings per figure."""
    warnings = {}
    for name, (fn, alt, caption) in FIGURES.items():
        sc = fn()
        REG.put(name, sc.c, alt, caption)
        warnings[name] = sc.report()
    return warnings
