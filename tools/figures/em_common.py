"""Registry and helpers shared by the figure modules of the Engineering Mechanics Midterm 1 bank (tools/figures/em_m1/)."""
from figures.svgkit import Registry

REG = Registry("EM-M1")
FIGURES = {}


def figure(name, alt, caption):
    """Register `fn() -> Scene` as the figure `name` (file vault/attachments/EM-M1/<name>.svg).

    `alt` is the accessible description (plain words); `caption` may use $...$ math and is shown under the figure."""
    def deco(fn):
        if name in FIGURES:
            raise ValueError(f"figure {name} registered twice")
        FIGURES[name] = (fn, alt, caption)
        return fn
    return deco


def inertial_frame(sc, o=(0.0, 0.0), length=1.0, names=("x", "y")):
    """Inertial axes drawn in blue, with the origin named O."""
    sc.axes(o, 0, length, names, "BLUE")
    sc.label(o, "O", "BLUE", "end", 16, dx=-8, dy=16)
