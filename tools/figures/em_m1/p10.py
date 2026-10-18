"""Figure of bank item P10 (free fall from a tower on the rotating Earth)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold


def _into_page(sc, p, r=0.16, col="BLUE"):
    """Axis pointing into the page: circle with a cross."""
    sc.circle(p, r, col, 1.8)
    d = r * 0.7071
    sc.line((p[0] - d, p[1] - d), (p[0] + d, p[1] + d), col, 1.6)
    sc.line((p[0] - d, p[1] + d), (p[0] + d, p[1] - d), col, 1.6)


@figure("p10-earth-free-fall",
        "Left: the Earth with its rotation axis, the equator and a point A at latitude lambda. Right: the local frame at A "
        "enlarged, with z up, y north, x east into the page, the rotation vector inclined at lambda above the northward "
        "horizontal, and a tower of height h from whose top the particle P is released",
        r"Free fall on the rotating Earth: point $A$ at latitude $\lambda$, rotation $\boldsymbol\Omega$ along the Earth axis; "
        r"local frame $S_1=\{A;x\ \text{east},\,y\ \text{north},\,z\ \text{up}\}$ (east points into the page), "
        r"$\boldsymbol\Omega=\Omega\cos\lambda\,\mathbf j+\Omega\sin\lambda\,\mathbf k$, particle $P$ released from rest at height $h$")
def p10():
    sc = Scene(640, 330, (20, 305), 52)
    lam = math.radians(40)
    # ---- left panel: the Earth -------------------------------------------------------------
    C, R = (3.4, 2.75), 2.0
    sc.circle(C, R, "HEAD", 2.0, fill="HEAD", opacity=0.06)
    sc.dashed((C[0] - R - 0.2, C[1]), (C[0] + R + 0.2, C[1]))          # equator
    sc.note((C[0] - R - 0.2, C[1]), "equator", anchor="end", dx=-4, dy=4, size=12)
    sc.dashed((C[0], C[1] - R - 0.25), (C[0], C[1] + R))               # rotation axis
    sc.vec((C[0], C[1] + R), (C[0], C[1] + R + 0.95), bold("Ω"), "GREEN", name_off=(14, 6))
    sc.label((C[0], C[1] + R), "N", "TEXT", "end", 14, dx=-6, dy=-4)
    A = (C[0] + R * math.cos(lam), C[1] + R * math.sin(lam))
    sc.dashed(C, A)
    sc.angle(C, 0.75, 0, 40, "λ", name_r=1.0)
    sc.dotp(C, 3.0)
    # small tower at A along the local vertical
    up = (math.cos(lam), math.sin(lam))
    sc.line(A, (A[0] + 0.45 * up[0], A[1] + 0.45 * up[1]), "HEAD", 3.0)
    sc.label(A, "A", "HEAD", "start", 16, dx=4, dy=22)
    # ---- right panel: local frame enlarged ----------------------------------------------
    O = (8.6, 1.1)
    sc.ground((7.0, O[1]), (11.4, O[1]), side=-1)
    # tower
    H = 3.3
    sc.poly([(O[0] + 0.25, O[1]), (O[0] + 0.25, O[1] + H), (O[0] + 0.55, O[1] + H), (O[0] + 0.55, O[1])], "HEAD", 1.6,
            fill="HEAD", opacity=0.10, close=True)
    P = (O[0] + 0.12, O[1] + H)
    sc.mass(P, "P", r=7, name_off=(-14, -10))
    sc.dashed(P, (P[0], O[1] + 0.1))
    sc.dim((O[0] + 0.95, O[1]), (O[0] + 0.95, O[1] + H), "h", off=(12, 4))
    # axes at the foot A
    sc.vec(O, (O[0], O[1] + 1.25), "z", "BLUE", 1.9, name_off=(-12, 4))
    sc.vec(O, (O[0] - 1.25, O[1]), "y", "BLUE", 1.9, name_off=(0, 18))
    _into_page(sc, O)
    sc.label(O, "x", "BLUE", "start", 16, dx=10, dy=20)
    sc.label(O, "A", "HEAD", "middle", 16, dx=-12, dy=-24)
    sc.note((O[0] - 1.25, O[1]), "north", dx=-36, dy=-8, size=12)
    sc.note(O, "east (into page)", dx=24, dy=22, size=12)
    # rotation vector, parallel to the Earth axis: lambda above the northward horizontal
    L = 1.7
    tip = (O[0] - L * math.cos(lam), O[1] + L * math.sin(lam))
    sc.vec(O, tip, bold("Ω"), "GREEN", 2.0, name_off=(-14, -2))
    sc.angle(O, 0.9, 180 - 40, 180, "λ", name_r=1.15)
    sc.gravity((11.2, 4.3), 0.9, "g")
    return sc
