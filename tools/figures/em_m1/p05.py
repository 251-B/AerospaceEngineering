"""Figure of bank item P05 (flight pendulum on an accelerating support)."""
import math

from figures.em_common import figure, inertial_frame
from figures.mech import S, Scene, bold


@figure("p05-flight-pendulum",
        "Pendulum of length l hanging from a support A that accelerates horizontally with acceleration a; the bob P of mass m makes the angle theta with the downward vertical",
        r"Flight pendulum: support $A$ with acceleration $\mathbf a_A=a_0\,\mathbf i$, string of length $\ell$, bob $P$ of mass $m$, "
        r"angle $\theta$ from the downward vertical, positive towards $+x$")
def p05():
    sc = Scene(640, 340, (60, 312), 58)
    A = (4.4, 3.9)
    th = math.radians(28)
    L = 3.0
    P = (A[0] + L * math.sin(th), A[1] - L * math.cos(th))
    inertial_frame(sc, (0.0, 0.0), 1.0)
    # ceiling rail the support slides on
    sc.ground((3.0, 3.9), (5.8, 3.9), side=1)
    sc.mass(A, None, r=5, col="HEAD")
    sc.label(A, "A", "HEAD", "end", 17, dx=-10, dy=-4)
    sc.vec((4.5, 4.55), (5.5, 4.55), S(bold("a"), "A"), "PINK", name_off=(18, 5))
    # vertical reference and string
    sc.dashed(A, (A[0], A[1] - L - 0.35))
    sc.line(A, P, "EDGE", 1.8)
    sc.mass(P, "P", r=8, name_off=(16, 6))
    sc.label(P, "m", "TEXT", "middle", 15, dx=0, dy=28)
    sc.angle(A, 1.0, -90, -90 + 28, "θ", name_r=1.32)
    sc.label(((A[0] + P[0]) / 2, (A[1] + P[1]) / 2), "ℓ", "TEXT", "middle", 17, dx=18, dy=-4)
    sc.gravity((7.0, 3.6), 1.0, "g")
    return sc
