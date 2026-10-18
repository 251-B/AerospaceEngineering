"""Figure of bank item C03 (slider on a smooth horizontal rail with a pendulum hanging from it)."""
import math

from figures.em_common import figure, inertial_frame
from figures.mech import S, Scene


@figure("c03-slider-pendulum",
        "A slider A of mass M on a smooth horizontal rail at abscissa x_A; a bob P of mass m hangs from A on a string "
        "of length l making the angle theta with the downward vertical",
        r"Slider $A$ (mass $M$) on a smooth horizontal rail, abscissa $x_A$; bob $P$ (mass $m$) on a string of length "
        r"$\ell$, angle $\theta$ from the downward vertical, positive towards $+x$")
def c03():
    sc = Scene(640, 300, (70, 262), 58)
    inertial_frame(sc, (0.0, 0.0), 0.9)
    # overhead rail (the slider runs under it; hatching above)
    sc.ground((1.4, 3.3), (8.6, 3.3), side=1)
    A = (4.6, 3.05)
    w = 0.55
    sc.poly([(A[0] - w, 3.3), (A[0] + w, 3.3), (A[0] + w, 2.8), (A[0] - w, 2.8)], "HEAD", 2.0,
            fill="HEAD", close=True, opacity=0.12)
    sc.dotp(A, 3.5, "HEAD")
    sc.label(A, "A", "HEAD", "end", 17, dx=-w * 58 - 8, dy=6)
    sc.label((A[0] + w, A[1]), "M", "TEXT", "start", 15, dx=8, dy=6)
    # abscissa of A
    sc.dim((0, 3.95), (A[0], 3.95), S("x", "A"), off=(0, -8))
    sc.dashed((0, 1.3), (0, 4.1))
    sc.dashed((A[0], 3.3), (A[0], 4.1))
    # string and bob
    th = math.radians(32)
    L = 2.5
    P = (A[0] + L * math.sin(th), A[1] - L * math.cos(th))
    sc.dashed(A, (A[0], A[1] - L - 0.3))
    sc.line(A, P, "EDGE", 1.8)
    sc.mass(P, "P", r=8, name_off=(16, 6))
    sc.label(P, "m", "TEXT", "middle", 15, dx=0, dy=28)
    sc.angle(A, 0.95, -90, -90 + 32, "θ", name_r=1.25)
    sc.label(((A[0] + P[0]) / 2, (A[1] + P[1]) / 2), "ℓ", "TEXT", "middle", 17, dx=16, dy=-2)
    sc.gravity((8.3, 1.6), 0.9, "g")
    return sc
