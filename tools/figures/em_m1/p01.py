"""Figure of bank item P01 (bead on a vertical circular helix), drawn in an orthographic oblique view."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold

PSI = math.radians(28)       # azimuth of the viewer
EPS = math.radians(16)       # elevation of the viewer
R, B = 1.15, 0.26            # helix radius and pitch parameter (world units of the sketch)


def _pr(x, y, z):
    """Orthographic projection of a 3D point (z up) onto the sketch plane."""
    u = -math.sin(PSI) * x + math.cos(PSI) * y
    v = -math.sin(EPS) * (math.cos(PSI) * x + math.sin(PSI) * y) + math.cos(EPS) * z
    return (u, v)


def _depth(x, y):
    return math.cos(PSI) * x + math.sin(PSI) * y


def _helix(sc, f0, f1):
    """Helix from phi = f0 to f1, front half solid and back half dashed."""
    n = 360
    seg, front = [], None
    for i in range(n + 1):
        f = f0 + (f1 - f0) * i / n
        x, y = R * math.cos(f), R * math.sin(f)
        fr = _depth(x, y) >= 0
        p = _pr(x, y, B * f)
        if front is None or fr == front:
            seg.append(p)
        else:
            seg.append(p)
            sc.poly(seg, "HEAD", 2.6 if front else 1.3, None if front else "5 4")
            seg = [p]
        front = fr
    sc.poly(seg, "HEAD", 2.6 if front else 1.3, None if front else "5 4")


def _ellipse(sc, z, col="EDGE", dash="4 4"):
    pts = [_pr(R * math.cos(f), R * math.sin(f), z) for f in [2 * math.pi * i / 120 for i in range(121)]]
    sc.poly(pts, col, 1.0, dash)


@figure("p01-helix-bead",
        "Bead P on a vertical circular helix of radius R and pitch 2 pi b around the z axis, with the intrinsic triad t, n, b drawn at the bead and gravity pointing down",
        r"Bead $P$ on the smooth helix $\rho=R$, $z=b\varphi$ (pitch $2\pi b$), $z$ up and gravity $-g\,\mathbf k$; "
        r"$\varphi$ is the azimuth from the $x$ axis, and $\{\mathbf t,\mathbf n,\mathbf b\}$ is the Frenet triad at $P$")
def p01():
    sc = Scene(640, 500, (330, 432), 92)
    # vertical axis
    sc.dashed(_pr(0, 0, -0.35), _pr(0, 0, 4.15))
    # fixed axes at O
    O = _pr(0, 0, 0)
    sc.vec(O, _pr(1.55, 0, 0), "x", "BLUE", 1.9, name_off=(-14, 4))
    sc.vec(O, _pr(0, 1.75, 0), "y", "BLUE", 1.9, name_off=(10, 6))
    sc.vec(_pr(0, 0, 3.9), _pr(0, 0, 4.4), "z", "BLUE", 1.9, name_off=(12, 4))
    sc.label(O, "O", "BLUE", "start", 16, dx=8, dy=-8)
    # base circle, helix (2.4 turns)
    _ellipse(sc, 0.0)
    _helix(sc, 0.0, 2.4 * 2 * math.pi)
    # radius R on the base circle, towards phi = 90 deg + psi direction (a front-right point)
    fR = PSI - math.radians(90)
    sc.dim(O, _pr(R * math.cos(fR), R * math.sin(fR), 0), "R", off=(0, -8))
    # bead and its azimuth
    fP = 2 * math.pi + PSI + math.radians(40)
    xP, yP, zP = R * math.cos(fP), R * math.sin(fP), B * fP
    P = _pr(xP, yP, zP)
    Pp = _pr(xP, yP, 0)
    sc.dashed(Pp, P)
    sc.dashed(O, Pp)
    sc.dotp(Pp, 2.6, "EDGE")
    # azimuth arc in the base plane from x to the projection of P
    fa = fP - 2 * math.pi
    arc = [_pr(0.8 * math.cos(f), 0.8 * math.sin(f), 0) for f in [fa * i / 40 for i in range(41)]]
    sc.poly(arc, "GREEN", 1.5)
    mid = fa / 2
    sc.label(_pr(0.8 * math.cos(mid), 0.8 * math.sin(mid), 0), "φ", "GREEN", "middle", 16, dx=24, dy=22)
    # pitch: two successive passes on the same generator (phi = fp and fp + 2 pi)
    fp = PSI + math.radians(-95)
    xg, yg = R * math.cos(fp), R * math.sin(fp)
    z1, z2 = B * (fp + 2 * math.pi), B * (fp + 4 * math.pi)
    sc.dashed(_pr(xg, yg, z1), _pr(xg, yg, z2))
    a, b_ = _pr(xg, yg, z1), _pr(xg, yg, z2)
    sc.dim((a[0] - 0.32, a[1]), (b_[0] - 0.32, b_[1]), "2πb", off=(-26, 4))
    sc.line((a[0] - 0.4, a[1]), (a[0] - 0.05, a[1]), "EDGE", 1.0)
    sc.line((b_[0] - 0.4, b_[1]), (b_[0] - 0.05, b_[1]), "EDGE", 1.0)
    # Frenet triad at P
    h = math.hypot(R, B)
    ep = (-math.sin(fP), math.cos(fP), 0)
    er = (math.cos(fP), math.sin(fP), 0)
    L = 0.85
    tv = tuple((R * ep[i] + B * (i == 2)) / h for i in range(3))
    nv = tuple(-er[i] for i in range(3))
    bv = tuple((-B * ep[i] + R * (i == 2)) / h for i in range(3))
    for vec, nm, off in [(tv, bold("t"), (12, 2)), (nv, bold("n"), (-4, 16)), (bv, bold("b"), (-14, -2))]:
        sc.vec(P, _pr(xP + L * vec[0], yP + L * vec[1], zP + L * vec[2]), nm, "BLUE", 2.0, name_off=off)
    sc.mass(P, "P", r=7.5, name_off=(24, 14))
    sc.gravity((-2.75, 3.4), 0.9, "g")
    return sc
