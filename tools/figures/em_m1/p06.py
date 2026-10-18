"""Figure of bank item P06 (precessing orbit under an attractive inverse-cube perturbation)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold

RC, ECC, K = 1.296, 0.62, 0.9          # semi-parameter r_c (1e7 m), eccentricity, k = sqrt(1 - eps/h^2)


def _r(th):
    return RC / (1 + ECC * math.cos(K * th))


def _pt(th_deg):
    th = math.radians(th_deg)
    r = _r(th)
    return (r * math.cos(th), r * math.sin(th))


@figure("p06-precessing-orbit",
        "Rosette-like orbit about the centre O: the particle P at distance r and polar angle theta, the first perigee Pi1 on the "
        "reference line theta = 0, the apogee A at 200 degrees and the next perigee Pi2 advanced by the angle Delta phi = 40 degrees",
        r"Orbit of $P$ about $O$ for $arepsilon=0.19\,h^2$, $e=0.62$: one radial cycle from the perigee $\Pi_1$ through the "
        r"apogee $A$ to the next perigee $\Pi_2$ (solid) and the start of the next cycle (dashed); $r$, $	heta$, the polar "
        r"unit vectors at $P$ and the apsidal advance $\Delta\phi$")
def p06():
    sc = Scene(640, 470, (392, 200), 110)
    O = (0.0, 0.0)
    # orbit: one radial cycle from perigee to perigee, then the beginning of the next one dashed
    sc.curve(lambda s: _pt(s), 0, 400, n=400, col="HEAD", w=2.2)
    sc.curve(lambda s: _pt(s), 400, 560, n=160, col="EDGE", w=1.4, dash="6 5")
    # reference line theta = 0 through the first perigee, and the direction of the second perigee
    sc.dashed((-0.4, 0.0), (1.45, 0.0))
    sc.dashed(O, (1.45 * math.cos(math.radians(40)), 1.45 * math.sin(math.radians(40))))
    sc.dotp(O, 4.0)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=20)
    # apsides
    p0, p1, pa = _pt(0), _pt(400), _pt(200)
    for p in (p0, p1, pa):
        sc.dotp(p, 4.0)
    sc.label(p0, S("Π", "1"), "HEAD", "start", 16, italic=False, dx=8, dy=20)
    sc.label(p1, S("Π", "2"), "HEAD", "end", 16, italic=False, dx=-12, dy=-10)
    sc.label(pa, "A", "HEAD", "start", 16, dx=8, dy=20)
    sc.dashed(O, pa)
    # apsidal advance
    sc.angle(O, 1.2, 0, 40, "Δφ", name_r=1.38)
    # particle at a generic angle, its radius vector and the polar unit vectors
    thp = 145
    P = _pt(thp)
    sc.vec(O, P, None, "BLUE")
    sc.label((P[0] * 0.35, P[1] * 0.35), bold("r"), "BLUE", "middle", 16, dx=8, dy=-12)
    sc.angle(O, 0.32, 0, thp, "θ", name_r=0.5)
    ur = (math.cos(math.radians(thp)), math.sin(math.radians(thp)))
    ut = (-ur[1], ur[0])
    sc.vec(P, (P[0] + 0.5 * ur[0], P[1] + 0.5 * ur[1]), S(bold("e"), "r"), "BLUE", w=1.8, name_off=(-14, 4))
    sc.vec(P, (P[0] + 0.5 * ut[0], P[1] + 0.5 * ut[1]), S(bold("e"), "θ"), "BLUE", w=1.8, name_off=(-6, 18))
    sc.mass(P, "P", r=7, name_off=(14, -10))
    # data
    sc.note((0.55, -1.55), bold("F") + " = −m(μ/r² + ε/r³) " + S(bold("e"), "r"), "TEXT", "start", 13)
    sc.note((0.55, -1.75), "k² = 1 − ε/h²", "TEXT", "start", 13)
    sc.note((0.55, -1.95), "Δφ = 2π(1/k − 1)", "TEXT", "start", 13)
    return sc
