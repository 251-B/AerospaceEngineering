"""Figure of bank item P03 (bead on a parabolic wire spinning about its vertical axis)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head


def _spin_ellipse(sc, c, a, b, t0, t1, col="GREEN"):
    """Arrowed elliptical arc (a rotation about a vertical axis seen obliquely), angles in degrees."""
    n = 60
    pts = [(c[0] + a * math.cos(math.radians(t0 + (t1 - t0) * i / n)),
            c[1] + b * math.sin(math.radians(t0 + (t1 - t0) * i / n))) for i in range(n + 1)]
    sc.poly(pts, col, 1.8)
    arrow_head(sc.c, sc.P(pts[-4]), sc.P(pts[-1]), col, 10)


@figure("p03-parabolic-wire",
        "Smooth wire shaped as the parabola y equals x squared over 2p in a vertical plane, spinning with rate Omega about its vertical axis; the bead P slides on it",
        r"Wire $y=x^2/(2p)$ in the plane $x_1y_1$ of $S_1$, which turns with $\boldsymbol\omega_{10}=\Omega\,\mathbf j$ about the "
        r"vertical axis; $\mathbf k_1$ is normal to the plane of the wire, gravity $-g\,\mathbf j$")
def p03():
    sc = Scene(640, 390, (300, 312), 92)
    p = 1.0
    f = lambda x: x * x / (2 * p)
    sc.curve(lambda s: (s, f(s)), -2.0, 2.0, col="HEAD", w=2.6)
    sc.vec((-2.35, 0), (2.45, 0), S("x", "1"), "BLUE", 1.9, name_off=(12, 16))
    sc.vec((0, -0.25), (0, 3.15), S("y", "1"), "BLUE", 1.9, name_off=(16, 4))
    sc.label((0, 0), "O", "BLUE", "end", 16, dx=-8, dy=18)
    # k1 out of the page
    sc.circle((0, 0), 0.075, "BLUE", 1.4)
    sc.dotp((0, 0), 2.0, "BLUE")
    sc.label((0, 0), S("z", "1"), "BLUE", "start", 15, dx=10, dy=20)
    # rotation about the vertical axis
    _spin_ellipse(sc, (0, 2.6), 0.55, 0.16, 200, 520)
    sc.label((0.6, 2.75), "Ω", "GREEN", "start", 17, weight="700", dx=6)
    # bead
    xP = 1.25
    P = (xP, f(xP))
    sc.mass(P, "P", r=7.5, name_off=(-18, -6))
    sc.dashed((xP, 0), P)
    sc.dim((0, -0.45), (xP, -0.45), "x", off=(0, 18))
    sc.dashed((xP, 0), (xP, -0.55))
    # scale p: the point x = p of the curve, at height p/2
    sc.dashed((-p, 0), (-p, f(p)))
    sc.dashed((-p, f(p)), (0, f(p)))
    sc.dim((-p, -0.45), (0, -0.45), "p", off=(0, 18))
    sc.dashed((-p, 0), (-p, -0.55))
    sc.label((0, f(p)), "p/2", "TEXT", "start", 14, italic=True, dx=8, dy=5)
    # weight of the bead
    sc.vec(P, (P[0], P[1] - 0.7), "m" + bold("g"), "PINK", 2.0, name_off=(24, 0))
    sc.label((-2.3, 2.7), "y = x²/(2p)", "HEAD", "start", 16)
    sc.gravity((-2.2, 2.2), 0.75, "g")
    return sc
