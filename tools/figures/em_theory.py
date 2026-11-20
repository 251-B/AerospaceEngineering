"""Figures of the Engineering Mechanics theory notes (vault/03 - Engineering Mechanics/Topic N - ...).

One module per topic in tools/figures/em_th/ (tN.py); each registers its figures with the `figure` decorator below and
names them `tN-<slug>`. They follow the figure rules of AGENTS.md and the colour code and helpers of
figures/em_solutions.py (re-exported here): fixed axes grey, moving basis blue, auxiliary vectors orange, angles
green, forces pink, one view per rotation with the axis out of or into the paper, right triangles shaded.

The vault copies go to vault/attachments/EM-T/<name>.svg (generated figures) or are PNG crops registered with
`raster` (vault/attachments/EM-T/<name>.png); the web copies are inlined in the theory pages by
tools/build_topic_pages.py (flavor "mechanics", entry key "figures": "em_theory"), which calls build().
"""
import importlib
import pkgutil

from figures.em_solutions import (axis_in, axis_out, fixed_axis, right_angle, spin_about_vertical, triangle,  # noqa: F401
                                  unit)
from figures.svgkit import Registry

REG = Registry("EM-T")
FIGURES = {}
RASTERS = {}
WARNINGS = {}


def figure(name, alt, caption):
    """Register `fn() -> Scene` as the figure `name` (file vault/attachments/EM-T/<name>.svg)."""
    def deco(fn):
        if name in FIGURES:
            raise ValueError(f"figure {name} registered twice")
        FIGURES[name] = (fn, alt, caption)
        return fn
    return deco


def raster(name, alt, caption, width=None):
    """Register a PNG crop of the official PDFs (vault/attachments/EM-T/<name>.png; Screenshot-First rule of AGENTS.md)."""
    if name in FIGURES or name in RASTERS:
        raise ValueError(f"figure {name} registered twice")
    RASTERS[name] = (alt, caption, width)


def _load():
    from figures import em_th
    for m in sorted(pkgutil.iter_modules(em_th.__path__), key=lambda m: m.name):
        importlib.import_module(f"figures.em_th.{m.name}")


def build():
    """Register every figure in REG (idempotent) and return the registry; WARNINGS holds the overlap warnings."""
    _load()
    for name, (fn, alt, caption) in FIGURES.items():
        sc = fn()
        REG.put(name, sc.c, alt, caption)
        WARNINGS[name] = sc.report()
    for name, (alt, caption, width) in RASTERS.items():
        REG.raster(name, alt, caption, width)
    return REG
