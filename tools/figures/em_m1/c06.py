"""Figure of bank item C06 (particle on the outside of a smooth sphere whose centre moves along the vertical axis)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold


@figure("c06-moving-sphere",
        "Side view: a sphere of radius R whose centre C lies on the vertical z axis at height h(t) above O; "
        "a particle P rests on the outside of the sphere at polar angle theta from the upward vertical through C",
        r"Sphere of radius $R$ with centre $C$ at the prescribed height $h(t)=H+b\sin\Omega t$ on the vertical axis; particle $P$ on its "
        r"outer surface, polar angle $\theta$ from the upward vertical, azimuth $\varphi$ about the axis")
def c06():
    sc = Scene(640, 400, (290, 362), 55)
    C = (0.0, 3.1)
    R = 1.75
    # vertical axis and inertial axes at O
    sc.vec((0, 0), (0, 6.3), None, "BLUE", 1.6)
    sc.label((0, 6.3), "z", "BLUE", "start", 17, dx=8, dy=8)
    sc.vec((0, 0), (1.1, 0), "x", "BLUE", 1.8, name_off=(10, 6))
    sc.label((0, 0), "O", "BLUE", "end", 16, dx=-8, dy=20)
    # sphere and centre
    sc.circle(C, R, "HEAD", 2.2, fill="HEAD", opacity=0.08)
    sc.dotp(C, 3.5, "HEAD")
    sc.label(C, "C", "HEAD", "end", 17, dx=-8, dy=18)
    # height of C with its oscillation
    sc.dim((-2.6, 0), (-2.6, C[1]), "h(t)", off=(-26, 4))
    sc.dashed((-2.75, 0), (-0.15, 0))
    sc.dashed((-2.75, C[1]), (-0.1, C[1]))
    sc.vec((-3.25, C[1] - 0.55), (-3.25, C[1] + 0.55), None, "BLUE", 1.8)
    sc.vec((-3.25, C[1] + 0.55), (-3.25, C[1] - 0.55), None, "BLUE", 1.8)
    # particle at polar angle theta from the upward vertical
    th = math.radians(42)
    P = (C[0] + R * math.sin(th), C[1] + R * math.cos(th))
    sc.line(C, P, "EDGE", 1.4)
    sc.label(((C[0] + P[0]) / 2, (C[1] + P[1]) / 2), "R", "TEXT", "middle", 16, dx=12, dy=8)
    sc.angle(C, 0.8, 90 - 42, 90, "θ", name_r=1.08)
    # reaction along the outward normal, weight
    n = (math.sin(th), math.cos(th))
    sc.vec(P, (P[0] + 1.1 * n[0], P[1] + 1.1 * n[1]), bold("N"), "PINK", name_off=(12, -4))
    sc.vec(P, (P[0], P[1] - 1.15), "m" + bold("g"), "PINK", name_off=(22, 8))
    sc.mass(P, "P", r=7.5, name_off=(-22, -12))
    # azimuth mark (the meridian plane of P turns about z)
    sc.arc((0, 5.55), 0.3, 200, 520, "GREEN", 1.6, head=True)
    sc.label((0, 5.55), "φ", "GREEN", "start", 16, dx=26, dy=6)
    return sc
