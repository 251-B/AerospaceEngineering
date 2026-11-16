"""Registry and decorator shared by the figure modules of the Aerospace Materials I Midterm 2 bank (tools/figures/mat_mt2/)."""
from figures.svgkit import Registry

REG = Registry("MAT-MT2")
FIGURES = {}


def figure(name, alt, caption=None):
    """Register `fn() -> Canvas` as the figure `name` (file vault/attachments/MAT-MT2/<name>.svg).

    `alt` is the accessible description in plain words; `caption` is shown under the figure (defaults to `alt`).
    A figure used as an option of a "choose the picture" question must not give the answer away in its labels."""
    def deco(fn):
        if name in FIGURES:
            raise ValueError(f"figure {name} registered twice")
        FIGURES[name] = (fn, alt, caption)
        return fn
    return deco
