"""Figure of bank item C02 (cubic potential V = V0 (u^3 - 3u), u = x/b, with two energy levels)."""
from figures.em_common import figure
from figures.mech import S, Scene

KY = 0.42          # world units per V0 on the vertical axis


def _V(u):
    return u**3 - 3 * u


@figure("c02-cubic-potential",
        "Graph of the potential energy V against x: a maximum 2 V0 at x = -b, a minimum -2 V0 at x = b; "
        "dashed horizontal lines mark the energy levels E = 2 V0 and E = 0",
        r"Potential $V(x)=V_0\big[(x/b)^3-3x/b\big]$ with the energy levels $E=2V_0$ (released at $x=2b$) "
        r"and $E=0$ (released at $x=0$)")
def c02():
    sc = Scene(640, 380, (330, 205), 118)
    # axes
    sc.vec((-2.45, 0), (2.55, 0), None, "BLUE", 1.6)
    sc.label((2.55, 0), "x", "BLUE", "middle", 17, dx=4, dy=22)
    sc.vec((0, -1.45), (0, 1.55), None, "BLUE", 1.6)
    sc.label((0, 1.55), "V", "BLUE", "start", 17, dx=8, dy=6)
    # potential curve, clipped to the drawing window
    sc.curve(lambda u: (u, KY * _V(u)), -2.12, 2.16, n=200, col="HEAD", w=2.4)
    # energy levels
    e2 = KY * 2
    sc.dashed((-2.35, e2), (2.35, e2), "PINK")
    sc.label((-2.35, e2), S("E", None) + " = 2" + S("V", "0"), "PINK", "start", 15, dx=0, dy=-8)
    # E = 0 lies on the axis: mark the allowed band of part (b) just above it
    sc.line((0, 0.05), (3 ** 0.5, 0.05), "GREEN", 3.0)
    sc.label((0.5, 0.05), "E = 0", "GREEN", "middle", 15, dy=-9)
    # marked abscissas
    for u in (-1, 1, 2, 3 ** 0.5):
        sc.dashed((u, 0), (u, KY * _V(u)))
        sc.dotp((u, 0), 3.0, "EDGE")
    sc.label((-1, 0), "−b", "TEXT", "middle", 15, dy=20)
    sc.label((1, 0), "b", "TEXT", "middle", 15, dx=12, dy=20)
    sc.label((3 ** 0.5, 0), "√3 b", "TEXT", "middle", 15, dx=-26, dy=20)
    sc.label((2, 0), "2b", "TEXT", "middle", 15, dx=6, dy=20)
    sc.label((0, 0), "O", "BLUE", "end", 15, dx=-6, dy=18)
    # values at the critical points
    sc.dotp((-1, e2), 4.0, "HEAD")
    sc.dotp((1, -e2), 4.0, "HEAD")
    sc.dotp((2, e2), 4.0, "ACC")
    sc.label((-1, e2), S("V", "max") + " = 2" + S("V", "0"), "HEAD", "middle", 14, dy=-12)
    sc.label((1, -e2), S("V", "min") + " = −2" + S("V", "0"), "HEAD", "middle", 14, dy=24)
    sc.label((2, e2), "start (a)", "ACC", "start", 13, italic=False, dx=10, dy=18)
    return sc
