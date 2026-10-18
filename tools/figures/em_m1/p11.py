"""Figure of bank item P11 (pendulum whose string is hauled through a fixed ring)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold


@figure("p11-hauled-pendulum",
        "A string passes through a small fixed smooth ring O; below the ring it holds the bob P of mass m at the angle "
        "theta from the downward vertical, with variable length l(t); the free end of the string leaves the ring "
        "horizontally and is pulled with constant speed u",
        r"Pendulum hauled through a fixed smooth ring $O$: length $\ell(t)=\ell_0-ut$ between $O$ and the bob $P$, "
        r"angle $\theta$ from the downward vertical (positive towards $+x$), unit vectors $\mathbf e_r$ (from $O$ to $P$) "
        r"and $\mathbf e_\theta$; the free end is pulled with constant speed $u$")
def p11():
    sc = Scene(640, 360, (40, 345), 60)
    O = (4.2, 4.6)
    th = math.radians(32)
    L = 3.6
    P = (O[0] + L * math.sin(th), O[1] - L * math.cos(th))
    # support of the ring: a short bracket from the ceiling
    sc.ground((3.3, 5.25), (5.1, 5.25), side=1)
    sc.line((O[0], 5.25), (O[0], O[1] + 0.13), "HEAD", 2.4)
    sc.circle(O, 0.11, "HEAD", 2.0)
    sc.label(O, "O", "HEAD", "end", 17, dx=-14, dy=4)
    # string: bob -> ring -> free end (horizontal, to the right) pulled with speed u
    sc.line(P, O, "EDGE", 1.8)
    end = (8.3, O[1])
    sc.line(O, end, "EDGE", 1.8)
    sc.vec((end[0] + 0.05, end[1]), (end[0] + 0.95, end[1]), "u", "BLUE", 2.0, name_off=(4, -12))
    sc.note(end, "free end, pulled", dx=-12, dy=24, size=12)
    # vertical reference and the angle
    sc.dashed(O, (O[0], O[1] - L - 0.3))
    sc.angle(O, 1.15, -90, -90 + 32, "θ", name_r=1.45)
    sc.label(((O[0] + P[0]) / 2, (O[1] + P[1]) / 2), "ℓ(t)", "TEXT", "start", 17, dx=12, dy=-2)
    # bob and unit vectors
    sc.mass(P, None, r=8)
    sc.label(P, "P", "HEAD", "middle", 17, dx=-18, dy=-4)
    sc.label(P, "m", "TEXT", "middle", 15, dx=-22, dy=22)
    er = (math.sin(th), -math.cos(th))
    et = (math.cos(th), math.sin(th))
    sc.vec(P, (P[0] + 0.9 * er[0], P[1] + 0.9 * er[1]), S(bold("e"), "r"), "BLUE", 1.9, name_off=(16, 6))
    sc.vec(P, (P[0] + 0.9 * et[0], P[1] + 0.9 * et[1]), S(bold("e"), "θ"), "BLUE", 1.9, name_off=(14, -2))
    # inertial axes and gravity
    sc.axes((0.3, 0.3), 0, 0.9, ("x", "y"))
    sc.gravity((9.0, 2.6), 0.9, "g")
    return sc
