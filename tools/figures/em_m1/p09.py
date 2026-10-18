"""Figure of bank item P09 (bead on a vertical hoop held by a spring)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold


def _v(th, kap):
    """V / (m g a) for d = 2a, l0 = a."""
    return math.cos(th) + kap / 2 * (math.sqrt(5 - 4 * math.cos(th)) - 1) ** 2


@figure("p09-hoop-spring-bead",
        "Left: smooth vertical hoop of radius a and centre C, fixed point A on the vertical through C at height d above C, "
        "spring from A to the bead P, angle theta from the top of the hoop, gravity downwards. Right: potential energy V over "
        "m g a against theta from 0 to pi for kappa = 1/2 (decreasing) and kappa = 1 (minimum at theta star)",
        r"Bead $P$ on the smooth hoop (centre $C$, radius $a$), spring of stiffness $k$ from the fixed point $A$ at height "
        r"$d=2a$ above $C$, angle $\theta$ from the top; right: $V(\theta)/(mga)$ for $\kappa=ka/(mg)=1/2$ and $\kappa=1$")
def p09():
    sc = Scene(640, 400, (140, 250), 88)
    C = (0.0, 0.0)
    A = (0.0, 2.0)
    th = math.radians(62)
    P = (math.sin(th), math.cos(th))
    # hoop and axis
    sc.circle(C, 1.0, "HEAD", 2.4)
    sc.dotp(C, 3.5)
    sc.label(C, "C", "HEAD", "end", 17, dx=-8, dy=18)
    sc.dashed((0.0, -1.2), (0.0, 2.0))
    # fixed point A (ceiling support)
    sc.pivot(A, down=False)
    sc.label(A, "A", "HEAD", "end", 17, dx=-14, dy=14)
    # dimensions d and a
    sc.dim((-1.3, 0.0), (-1.3, 2.0), "d", off=(-12, 4))
    sc.dashed((-1.4, 0.0), (-0.05, 0.0))
    sc.dashed((-1.4, 2.0), (-0.2, 2.0))
    ang = math.radians(300)
    sc.line(C, (math.cos(ang), math.sin(ang)), "EDGE", 1.2)
    sc.label((0.5 * math.cos(ang), 0.5 * math.sin(ang)), "a", "TEXT", "middle", 17, dx=12, dy=4)
    # spring and bead
    sc.spring(A, P, coils=7, amp=6)
    sc.line(C, P, "EDGE", 1.1, "4 3")
    sc.angle(C, 0.36, 90, 90 - 62, "θ", name_r=0.52)
    er = (math.sin(th), math.cos(th))
    et = (math.cos(th), -math.sin(th))
    sc.vec(P, (P[0] + 0.5 * er[0], P[1] + 0.5 * er[1]), S(bold("e"), "r"), "BLUE", w=1.7, name_off=(10, -4), size=15)
    sc.vec(P, (P[0] + 0.5 * et[0], P[1] + 0.5 * et[1]), S(bold("e"), "θ"), "BLUE", w=1.7, name_off=(14, 6), size=15)
    sc.mass(P, "P", r=7, name_off=(-20, -2))
    sc.label(((A[0] + P[0]) / 2, (A[1] + P[1]) / 2), "k", "TEXT", "start", 17, dx=10, dy=-4)
    sc.gravity((1.55, 1.95), 0.8, "g")
    # right panel: V/(m g a) against theta
    ox, oy, sx, sy = 2.2, -1.2, 2.7 / math.pi, 1.75
    sc.vec((ox, oy), (ox + 3.0, oy), "θ", "BLUE", 1.6, name_off=(10, 5), size=15)
    sc.vec((ox, oy), (ox, oy + 2.2), None, "BLUE", 1.6)
    sc.note((ox, oy + 2.2), "V/(mga)", "BLUE", "start", 13, dx=8, dy=4)
    for val, txt in ((0.0, "0"), (math.pi, "π")):
        sc.line((ox + sx * val, oy), (ox + sx * val, oy - 0.07), "EDGE", 1.1)
        sc.note((ox + sx * val, oy), txt, "TEXT", "middle", 13, dy=18)
    for val in (1.0,):
        sc.line((ox, oy + sy * val), (ox - 0.07, oy + sy * val), "EDGE", 1.1)
        sc.note((ox, oy + sy * val), "1", "TEXT", "end", 13, dx=-8, dy=4)
    sc.dashed((ox, oy + sy), (ox + sx * math.pi, oy + sy))
    sc.curve(lambda s: (ox + sx * s, oy + sy * _v(s, 0.5)), 0, math.pi, n=120, col="PINK", w=2.0)
    sc.curve(lambda s: (ox + sx * s, oy + sy * _v(s, 1.0)), 0, math.pi, n=120, col="GREEN", w=2.0)
    sc.note((ox + sx * 2.3, oy + sy * _v(2.3, 0.5)), "κ = 1/2", "PINK", "start", 13, dx=8, dy=-6)
    ts = math.acos(0.25)
    sc.dotp((ox + sx * ts, oy + sy * _v(ts, 1.0)), 3.5, "GREEN")
    sc.note((ox + sx * ts, oy + sy * _v(ts, 1.0)), "κ = 1", "GREEN", "start", 13, dx=8, dy=20)
    sc.label((ox + sx * ts, oy), S("θ", "*"), "GREEN", "middle", 14, dy=18)
    sc.line((ox + sx * ts, oy), (ox + sx * ts, oy + sy * _v(ts, 1.0)), "EDGE", 1.0, "3 3")
    return sc
