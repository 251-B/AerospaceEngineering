"""Figure of bank item P02 (particle on the smooth inner surface of a paraboloid of revolution)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold


@figure("p02-paraboloid",
        "Left: meridian section of the paraboloid z equals r squared over 2c with the particle P at radius r, the surface normal n and the weight. Right: top view with the azimuth phi and the polar unit vectors",
        r"Particle $P$ on the smooth inner surface $z=r^2/(2c)$ (axis $Oz$ vertical, gravity $-g\,\mathbf k$). "
        r"Left: meridian plane through $P$ with the unit normal $\mathbf n$; right: top view with the azimuth $\varphi$")
def p02():
    sc = Scene(640, 360, (175, 300), 72)
    c = 1.0
    f = lambda r: r * r / (2 * c)
    # ---- meridian section -------------------------------------------------------------
    sc.curve(lambda s: (s, f(s)), -2.05, 2.05, col="HEAD", w=2.6)
    sc.vec((-2.3, 0), (2.4, 0), "r", "BLUE", 1.9, name_off=(10, 16))
    sc.vec((0, -0.25), (0, 3.0), "z", "BLUE", 1.9, name_off=(12, 4))
    sc.label((0, 0), "O", "BLUE", "end", 16, dx=-8, dy=18)
    rP = 1.45
    P = (rP, f(rP))
    sc.dashed((rP, 0), P)
    sc.dim((0, -0.32), (rP, -0.32), "r", off=(0, 18))
    sc.dashed((rP, 0), (rP, -0.42))
    # normal n = (-r/c, 1)/q (inwards and up)
    q = math.hypot(rP / c, 1.0)
    nv = (-rP / c / q, 1 / q)
    sc.vec(P, (P[0] + 0.95 * nv[0], P[1] + 0.95 * nv[1]), bold("n"), "BLUE", 2.0, name_off=(-6, -8))
    sc.vec(P, (P[0], P[1] - 0.75), "m" + bold("g"), "PINK", 2.0, name_off=(-22, 0))
    sc.mass(P, "P", r=7.5, name_off=(16, 2))
    sc.label((-2.3, 2.55), "z = r²/(2c)", "HEAD", "start", 16)
    # mark the point r = c of the meridian (height c/2) to show the scale c
    sc.dashed((-c, 0), (-c, f(c)))
    sc.dim((-c, -0.32), (0, -0.32), "c", off=(0, 18))
    sc.dashed((-c, 0), (-c, -0.42))
    sc.gravity((-2.25, 1.9), 0.75, "g")
    # ---- top view ------------------------------------------------------------------------
    C = (4.3, 1.45)
    R = 1.2
    sc.circle(C, R, "EDGE", 1.2, dash="5 4")
    sc.vec(C, (C[0] + 1.6, C[1]), "x", "BLUE", 1.9, name_off=(10, 16))
    sc.vec(C, (C[0], C[1] + 1.75), "y", "BLUE", 1.9, name_off=(12, 4))
    sc.label(C, "z", "BLUE", "end", 15, dx=-10, dy=18)
    sc.circle(C, 0.07, "BLUE", 1.4)
    sc.dotp(C, 2.0, "BLUE")
    phi = math.radians(38)
    Pt = (C[0] + R * math.cos(phi), C[1] + R * math.sin(phi))
    sc.line(C, Pt, "EDGE", 1.2)
    sc.angle(C, 0.55, 0, 38, "φ", name_r=0.78)
    er = (math.cos(phi), math.sin(phi))
    ep = (-math.sin(phi), math.cos(phi))
    sc.vec(Pt, (Pt[0] + 0.65 * er[0], Pt[1] + 0.65 * er[1]), S(bold("e"), "r"), "BLUE", 2.0, name_off=(14, 4))
    sc.vec(Pt, (Pt[0] + 0.75 * ep[0], Pt[1] + 0.75 * ep[1]), S(bold("e"), "φ"), "BLUE", 2.0, name_off=(-12, -6))
    sc.mass(Pt, "P", r=7.5, name_off=(-26, 2))
    sc.note((3.0, -0.15), "top view", "TEXT", size=13)
    return sc
