"""Figure of bank item P07 (insertion orbit and circularisation impulse)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold

P_SEMI, ECC = 0.75, 0.5        # semi-latus rectum and eccentricity, lengths in units of r0
R_PLANET = 0.6


def _pt(th_deg):
    th = math.radians(th_deg)
    r = P_SEMI / (1 + ECC * math.cos(th))
    return (r * math.cos(th), r * math.sin(th))


@figure("p07-insertion-orbit",
        "Elliptic orbit with the planet centre O at one focus: the probe P at distance r0 and true anomaly theta0 = 120 degrees "
        "with velocity v0 making the flight-path angle gamma with the local horizontal; perigee Pi, apogee A where the "
        "tangential impulse Delta v is applied, and the dashed circular target orbit of radius r_a",
        r"Insertion orbit: focus $O$ (planet of radius $R$), probe $P$ at $r_0$ with velocity $\mathbf v_0$ and flight-path "
        r"angle $\gamma$ above the local horizontal $\mathbf e_\theta$; true anomaly $\theta_0$ from the perigee $\Pi$; "
        r"apogee $A$, impulse $\Delta\mathbf v$ and the circular target orbit $r=r_a$ (dashed)")
def p07():
    sc = Scene(640, 440, (352, 220), 128)
    O = (0.0, 0.0)
    # planet
    sc.circle(O, R_PLANET, "HEAD", 1.6, fill="HEAD", opacity=0.08)
    sc.label((R_PLANET * math.cos(math.radians(-60)), R_PLANET * math.sin(math.radians(-60))), "R", "TEXT",
             "start", 16, dx=6, dy=14)
    sc.line(O, (R_PLANET * math.cos(math.radians(-60)), R_PLANET * math.sin(math.radians(-60))), "EDGE", 1.0)
    # target circle and the ellipse (flown arc solid, the rest dashed)
    sc.circle(O, 1.5, "EDGE", 1.3, dash="7 5")
    sc.curve(_pt, 120, 180, n=60, col="HEAD", w=2.4)
    sc.curve(_pt, 180, 480, n=300, col="HEAD", w=1.3, dash="5 4")
    # apse line
    sc.dashed((-1.5, 0.0), (0.75, 0.0))
    sc.dotp(O, 4.0)
    sc.label(O, "O", "HEAD", "end", 17, dx=-6, dy=20)
    Pi = _pt(0)
    sc.dotp(Pi, 4.0)
    sc.label(Pi, "Π", "HEAD", "start", 16, italic=False, dx=8, dy=-8)
    A = _pt(180)
    sc.dotp(A, 4.0)
    sc.label(A, "A", "HEAD", "end", 17, dx=-8, dy=-8)
    # impulse at the apogee, along the velocity there (direction of motion: -y)
    sc.vec(A, (A[0], A[1] - 0.42), "Δ" + bold("v"), "PINK", name_off=(-22, 6))
    # probe, radius and true anomaly
    P = _pt(120)
    sc.line(O, P, "BLUE", 1.6)
    sc.label((P[0] * 0.5, P[1] * 0.5), S("r", "0"), "BLUE", "middle", 16, dx=12, dy=4)
    sc.angle(O, 0.26, 0, 120, S("θ", "0"), name_r=0.42)
    # local horizontal (e_theta) and velocity (gamma above it, outward)
    eth = (-math.sin(math.radians(120)), math.cos(math.radians(120)))
    sc.dashed((P[0] - 0.35 * eth[0], P[1] - 0.35 * eth[1]), (P[0] + 0.75 * eth[0], P[1] + 0.75 * eth[1]))
    sc.vec(P, (P[0] + 0.7 * eth[0], P[1] + 0.7 * eth[1]), S(bold("e"), "θ"), "BLUE", w=1.4, name_off=(-6, 18), size=15)
    sc.vec(P, (P[0] - 0.62, P[1]), S(bold("v"), "0"), "BLUE", name_off=(-14, -8))
    sc.angle(P, 0.3, 180, 210, "γ", name_r=0.45)
    sc.mass(P, "P", r=7, name_off=(10, -14))
    # labels of the orbits
    sc.note((1.08, 1.12), "circular orbit r = " + S("r", "a"), "TEXT", "start", 13)
    return sc
