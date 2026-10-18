"""Figure of bank item P15 (Clohessy-Wiltshire relative motion near a target on a circular orbit)."""
import math

from figures.em_common import figure
from figures.mech import S, Scene, bold

TH_T = 38.0       # angular position of the target in the sketch (deg)


@figure("p15-cw-relative-orbit",
        "Earth with the circular orbit of the target T; the frame S1 at T has x radially outwards and y along the "
        "direction of motion and rotates with the orbital rate n; the chaser P is close to T; an inset shows the bounded "
        "relative orbit of P about a centre C, an ellipse twice as long along y as along x",
        r"Target $T$ on a circular orbit of radius $R_T$ with mean motion $n$; rotating frame "
        r"$S_1=\{T;\mathbf e_x,\mathbf e_y\}$ ($x$ radial outwards, $y$ along-track); chaser $P$ at "
        r"$\boldsymbol\rho=x\,\mathbf e_x+y\,\mathbf e_y$ (distance exaggerated). Inset: bounded relative orbit "
        r"($\dot y_0=-2nx_0$), a $2{:}1$ ellipse about its centre $C$, run in the sense of the arrow")
def p15():
    sc = Scene(640, 400, (150, 215), 72)
    O = (0.0, 0.0)
    # Earth and the target orbit
    sc.circle(O, 0.95, "HEAD", 1.8, fill="HEAD", opacity=0.08)
    sc.dotp(O, 3.0)
    sc.label(O, "O", "HEAD", "middle", 16, dx=-12, dy=16)
    sc.circle(O, 1.85, "EDGE", 1.3, dash="6 4")
    sc.spin(O, 0.48, 200, 300, "n", name_r=0.70)
    sc.note((0.0, 0.42), "Earth (μ)", "TEXT", "middle", 13)
    # radius of the orbit
    a = math.radians(TH_T)
    T = (1.85 * math.cos(a), 1.85 * math.sin(a))
    sc.dim(O, (1.85 * math.cos(math.radians(160)), 1.85 * math.sin(math.radians(160))), S("R", "T"), off=(10, -34))
    # sense of the orbital motion on the orbit circle
    sc.arc(O, 1.85, 95, 112, "HEAD", 2.0, head=True)
    # rotating frame at T
    ex = (math.cos(a), math.sin(a))
    ey = (-math.sin(a), math.cos(a))
    Lx = 0.75
    sc.vec(T, (T[0] + Lx * ex[0], T[1] + Lx * ex[1]), "x", "BLUE", 1.9, name_off=(10, 4))
    sc.vec(T, (T[0] + Lx * ey[0], T[1] + Lx * ey[1]), "y", "BLUE", 1.9, name_off=(-6, -8))
    sc.mass(T, None, r=6, col="HEAD")
    sc.label(T, "T", "HEAD", "start", 17, dx=8, dy=20)
    # chaser below and behind the target (exaggerated)
    rho = (-0.48, -0.78)                           # components along e_x, e_y
    P = (T[0] + rho[0] * ex[0] + rho[1] * ey[0], T[1] + rho[0] * ex[1] + rho[1] * ey[1])
    sc.vec(T, P, None, "BLUE", 1.5)
    sc.label(((T[0] + P[0]) / 2, (T[1] + P[1]) / 2), bold("ρ"), "BLUE", "middle", 16, dx=-13, dy=2)
    sc.mass(P, "P", r=6.5, name_off=(14, 14))

    # ---- inset: bounded relative orbit, x up, y to the left (right-handed with k out of the page)
    C = (5.0, 0.35)
    A = 0.55
    sc.poly([(3.55, -1.15), (6.55, -1.15), (6.55, 2.35), (3.55, 2.35)], "EDGE", 1.0, close=True)
    sc.note((3.68, 2.08), "relative orbit in " + S("S", "1"), "TEXT", "start", 13)

    def ell(tau):
        xr = A * math.cos(tau)
        yr = -2 * A * math.sin(tau)           # y - y_c
        return (C[0] - yr, C[1] + xr)       # y axis drawn towards the left

    sc.curve(ell, 0.0, 2 * math.pi, n=160, col="HEAD", w=2.0)
    # sense: at the top (x = A) the chaser moves towards -y, i.e. to the right in the inset
    sc.vec(ell(0.80), ell(0.92), None, "HEAD", 2.0, head=11)
    sc.dotp(C, 3.0, "HEAD")
    sc.label(C, "C", "HEAD", "start", 15, dx=6, dy=16)
    # local axes through C
    sc.vec(C, (C[0], C[1] + 1.25), "x", "BLUE", 1.5, name_off=(10, 6))
    sc.vec(C, (C[0] - 1.35, C[1]), "y", "BLUE", 1.5, name_off=(-4, -8))
    # semi-axes
    sc.dim((C[0], C[1] - 1.25 * A - 0.05), (C[0] + 2 * A, C[1] - 1.25 * A - 0.05), "2" + S("A", "e"), off=(0, 16))
    sc.dim((C[0] + 2 * A + 0.18, C[1]), (C[0] + 2 * A + 0.18, C[1] + A), S("A", "e"), off=(14, 4))
    return sc
