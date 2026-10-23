"""Deduction figures of the Engineering Mechanics worked solutions (vault/03 - Engineering Mechanics/Solution Set - ...).

One module per problem in tools/figures/em_sol/ (pNN.py); each registers its figures with the `figure` decorator below.
They follow the figure rules of AGENTS.md ("Problem-solving standard"): the plane of the moving frame with dashed,
dimensioned projections, one view along each rotation axis (out of the paper or into it marked, fixed axes grey,
rotated axes coloured, arc of the angle) and the right triangles of non-trivial geometry.

Colour code of every solution figure (tokens of figures/svgkit.py):
  * EDGE  fixed (inertial) axes, construction lines, dashed projections
  * BLUE  the moving basis (i1, j1, k1) and position vectors
  * ACC   intrinsic or auxiliary unit vectors (e_t, e_n, e_QP), drawn in orange
  * GREEN angles and angular rates
  * PINK  forces
  * HEAD  bodies, wires, points

The vault copies go to vault/attachments/EM-SOL/<name>.svg; the web copies are inlined in the problem pages by
tools/build_mech_problems.py. `python scripts/generate_diagrams.py --set sol --png` renders PNG previews.
"""
import importlib
import math
import pkgutil

from figures.svgkit import Registry

REG = Registry("EM-SOL")
FIGURES = {}


# ---------------------------------------------------------------- drawing helpers (world coordinates of a mech.Scene)
def _dir(deg):
    return math.cos(math.radians(deg)), math.sin(math.radians(deg))


def fixed_axis(sc, o, deg, length, name, off=(10, 6), dashed=False):
    """Inertial axis: thin grey arrow (or a dashed grey line for a negative direction), name in grey."""
    d = _dir(deg)
    tip = (o[0] + length * d[0], o[1] + length * d[1])
    if dashed:
        sc.line(o, tip, "EDGE", 1.2, "4 4")
        sc.label(tip, name, "TEXT", "middle", 15, dx=off[0], dy=off[1])
    else:
        sc.vec(o, tip, None, "EDGE", 1.4, head=8)
        sc.label(tip, name, "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    return tip


def unit(sc, o, deg, length, name, col="BLUE", off=(10, -8)):
    """Unit vector of a basis: thick coloured arrow with its bold name near the tip."""
    d = _dir(deg)
    tip = (o[0] + length * d[0], o[1] + length * d[1])
    sc.vec(o, tip, name, col, 2.6, name_off=off, size=17, head=11)
    return tip


def axis_out(sc, p, name=None, col="HEAD", r_px=9, off=(0, 26)):
    """Axis pointing out of the paper, towards the reader (circle with a dot)."""
    x, y = sc.P(p)
    sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r_px}" fill="none" stroke="{col}" stroke-width="1.8"/>')
    sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{col}"/>')
    if name:
        sc.label(p, name, col, "middle", 15, dx=off[0], dy=off[1])


def axis_in(sc, p, name=None, col="HEAD", r_px=9, off=(0, 26)):
    """Axis pointing into the paper, away from the reader (circle with a cross)."""
    x, y = sc.P(p)
    s = r_px * 0.62
    sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r_px}" fill="none" stroke="{col}" stroke-width="1.8"/>')
    sc.c.add(f'<path d="M{x - s:.1f},{y - s:.1f} L{x + s:.1f},{y + s:.1f} M{x - s:.1f},{y + s:.1f} L{x + s:.1f},{y - s:.1f}" '
             f'stroke="{col}" stroke-width="1.6" fill="none"/>')
    if name:
        sc.label(p, name, col, "middle", 15, dx=off[0], dy=off[1])


def right_angle(sc, c, deg1, deg2, size=0.09, col="EDGE"):
    """Right-angle mark at corner c between the rays at deg1 and deg2."""
    a, b = _dir(deg1), _dir(deg2)
    p1 = (c[0] + size * a[0], c[1] + size * a[1])
    p2 = (c[0] + size * (a[0] + b[0]), c[1] + size * (a[1] + b[1]))
    p3 = (c[0] + size * b[0], c[1] + size * b[1])
    sc.poly([p1, p2, p3], col, 1.1)


def triangle(sc, pts, col="ACC", opacity=0.12):
    """Key right triangle of a deduction: light translucent fill, no outline."""
    sc.poly(pts, col, 0.0, fill=col, close=True, opacity=opacity)


def spin_about_vertical(sc, c, rx, ry, name, col="GREEN", name_off=(14, -4)):
    """Rotation about a vertical axis seen in perspective: a flat elliptical arc with an arrowhead, and its name."""
    from figures.svgkit import arrow_head
    x, y = sc.P(c)
    rxp, ryp = rx * sc.k, ry * sc.k
    p0 = (x - rxp, y)
    p1 = (x + rxp * 0.72, y + ryp * 0.69)
    sc.c.add(f'<path d="M{p0[0]:.1f},{p0[1]:.1f} A{rxp:.1f},{ryp:.1f} 0 0 0 {p1[0]:.1f},{p1[1]:.1f}" fill="none" '
             f'stroke="{col}" stroke-width="1.8"/>')
    arrow_head(sc.c, (p1[0] - 8, p1[1] + 1.2), (p1[0] + 3, p1[1] - 1.5), col, 9)
    sc.label(c, name, col, "start", 16, weight="700", dx=rxp + name_off[0], dy=name_off[1])


def figure(name, alt, caption):
    """Register `fn() -> Scene` as the figure `name` (file vault/attachments/EM-SOL/<name>.svg).

    `alt` is the accessible description (plain words); `caption` may use $...$ math and is shown under the figure."""
    def deco(fn):
        if name in FIGURES:
            raise ValueError(f"figure {name} registered twice")
        FIGURES[name] = (fn, alt, caption)
        return fn
    return deco


def _load():
    from figures import em_sol
    for m in sorted(pkgutil.iter_modules(em_sol.__path__), key=lambda m: m.name):
        importlib.import_module(f"figures.em_sol.{m.name}")


def build():
    """Register every figure in REG (idempotent) and return the overlap warnings per figure."""
    _load()
    warnings = {}
    for name, (fn, alt, caption) in FIGURES.items():
        sc = fn()
        REG.put(name, sc.c, alt, caption)
        warnings[name] = sc.report()
    return warnings
