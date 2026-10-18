"""Figure of bank item C08 (elliptic orbit e = 1/3 and the orbit after a tangential impulse at perigee)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold


def _orbit(p, e):
    def fn(t):
        r = p / (1 + e * math.cos(t))
        return (r * math.cos(t), r * math.sin(t))
    return fn


@figure("c08-perigee-impulse",
        "Two coplanar orbits with a common focus F and a common perigee at distance r_p: the original ellipse with "
        "apogee at 2 r_p and, dashed, the orbit after a tangential impulse at perigee, with apogee at 3 r_p",
        r"Orbit of eccentricity $e=1/3$ about the focus $F$ (perigee $\Pi$ at $r_p$, apogee $A$ at $r_a=2r_p$) and, dashed, "
        r"the orbit after a tangential impulse $\Delta v$ at $\Pi$ (apogee $A'$)")
def c08():
    sc = Scene(640, 392, (420, 178), 90)
    # original orbit (r_p = 1, e = 1/3) and new orbit (r_p = 1, e = 1/2)
    sc.curve(_orbit(4 / 3, 1 / 3), 0, 2 * math.pi, n=240, col="HEAD", w=2.2)
    sc.curve(_orbit(1.5, 0.5), 0, 2 * math.pi, n=240, col="BLUE", w=1.6, dash="7 5")
    # apse line
    sc.dashed((-3.25, 0), (1.35, 0))
    # focus (Earth)
    sc.circle((0, 0), 0.11, "HEAD", 1.6, fill="HEAD", opacity=0.35)
    sc.label((0, 0), "F", "HEAD", "middle", 17, dx=0, dy=-14)
    # apsides
    sc.dotp((1, 0), 4.0, "HEAD")
    sc.label((1, 0), "Π", "HEAD", "start", 17, dx=8, dy=20)
    sc.dotp((-2, 0), 4.0, "HEAD")
    sc.label((-2, 0), "A", "HEAD", "end", 17, dx=-8, dy=-8)
    sc.dotp((-3, 0), 4.0, "BLUE")
    sc.label((-3, 0), "A′", "BLUE", "start", 17, dx=8, dy=-8)
    # distances along the apse line
    sc.dim((0, -0.35), (1, -0.35), S("r", "p"), off=(0, 18))
    sc.dim((-2, -0.35), (0, -0.35), "2" + S("r", "p"), off=(0, 18))
    sc.dim((-3, -1.95), (0, -1.95), "3" + S("r", "p"), off=(0, 18))
    sc.dashed((-3, -0.1), (-3, -2.05))
    sc.dashed((0, -0.2), (0, -2.05))
    # velocity at perigee and the impulse
    sc.vec((1, 0), (1, 0.95), S(bold("v"), "p"), "BLUE", name_off=(20, 34))
    sc.vec((1, 0.95), (1, 1.35), "Δ" + bold("v"), "PINK", name_off=(20, 6))
    # sense of motion
    t = math.radians(120)
    p0 = _orbit(4 / 3, 1 / 3)(t)
    p1 = _orbit(4 / 3, 1 / 3)(t + 0.12)
    sc.vec(p0, p1, None, "HEAD", 2.0)
    return sc
