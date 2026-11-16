"""Problem RB-25: homogeneous cylinder hanging from the ceiling by two strings (yaw beta, pitch theta, roll phi)."""
import math

from figures.em_solutions import axis_out, figure
from figures.em_sol.rb01 import add, arrow_px, cross, d, norm, p3, p3v, ring, vadd, vscale, vsub
from figures.em_sol.rb06 import rlabel, rotation_view2
from figures.em_sol.rb24 import _hull
from figures.mech import S, Scene, bold

BETA, THETA, PHI = 40.0, 25.0, 30.0


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


@figure("rb25-beta",
        "Yaw rotation by beta about the vertical axis, seen from above.",
        r"Yaw: $\mathcal B_1$ is $\mathcal B_0$ turned by $\beta$ about $\mathbf k$ (⊙); $\mathbf j_1$ leans to negative "
        r"$\mathbf i$ (minus sign of $[{}_0R_1]$). $\mathbf i_1$ is the horizontal projection of the axis.")
def rotation_beta():
    def pre(sc):
        a = math.radians(BETA)
        t, n = (math.cos(a), math.sin(a)), (-math.sin(a), math.cos(a))
        pts = [add(add((0, 0), t, sx), n, sy) for sx, sy in ((-1, -1 / 3), (1, -1 / 3), (1, 1 / 3), (-1, 1 / 3))]
        sc.poly(pts, "EDGE", 0.0, close=True, fill="EDGE", opacity=0.10)

    return rotation_view2(660, 520, (260, 360), 150, BETA, _ax("i") + " (" + _ax("x", "0") + ")", _ax("j"),
                          _ax("i", "1") + " (" + _ax("x", "1") + ")", _ax("j", "1"),
                          _ax("k") + " = " + _ax("k", "1") + " (⊙) at G", ("β", ""), pre=pre, out_off=(-16, 28),
                          arc_r=0.30, cy=0.72, lab_r=0.50)


@figure("rb25-theta",
        "Pitch rotation by theta about the horizontal axis j1, tilting the cylinder axis below the horizontal.",
        r"Pitch: $\mathcal B_2$ is $\mathcal B_1$ turned by $\theta$ about $\mathbf j_1$ (⊙, with $\mathbf k_1$ to the "
        r"right and $\mathbf i_1$ up). $\mathbf i_2$ leans to negative $\mathbf k_1$, which gives $-\sin\theta$: the axis "
        r"dips below the horizontal.")
def rotation_theta():
    th = THETA
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    i2 = (-s, c)          # (k_1, i_1) components of i_2

    def post(sc):
        D, C = i2, (s, -c)
        sc.line((-1.35 * i2[0], -1.35 * i2[1]), (1.35 * i2[0], 1.35 * i2[1]), "ACC", 1.2, "6 4")
        for P, nm, dx, dy in ((D, "D", -14, -10), (C, "C", 14, 18)):
            sc.mass(P, None, r=4.5, col="ACC")
            sc.label(P, nm, "HEAD", "middle", 17, dx=dx, dy=dy)
        # horizontal extent (along k_1) of the segment CD, 2 l sin(theta)
        y0 = -1.12
        sc.line(D, (D[0], y0 - 0.05), "BLUE", 1.0, "4 3")
        sc.line(C, (C[0], y0 - 0.05), "BLUE", 1.0, "4 3")
        sc.dim((D[0], y0), (C[0], y0), "", gap=0.0)
        sc.label(((D[0] + C[0]) / 2, y0), "2 l sin θ", "TEXT", "middle", 15, dy=24)
        sc.note((0.62, -0.55), "in the usual side view (k up)", "TEXT", "start", 13)
        sc.note((0.62, -0.55), "i_2 dips below the horizontal by θ", "TEXT", "start", 13, dy=18)

    return rotation_view2(700, 560, (360, 330), 150, th, _ax("k", "1"), _ax("i", "1"), _ax("k", "2"),
                          _ax("i", "2") + " (" + _ax("x", "B") + ")", _ax("j", "1") + " = " + _ax("j", "2") + " (⊙)",
                          ("θ", ""), post=post, out_off=(-16, 28), arc_r=0.30, cy=0.72, lab_r=0.50,
                          m2_off=(-56, -4))


@figure("rb25-phi",
        "Roll rotation by phi about the axis of the cylinder.",
        r"Roll: $\mathcal B_B$ is $\mathcal B_2$ turned by $\phi$ about the axis $\mathbf i_2$ (⊙); $\mathbf k_B$ leans "
        r"to negative $\mathbf j_2$. The equal transverse moments make the tensor independent of $\phi$.")
def rotation_phi():
    def pre(sc):
        sc.circle((0.0, 0.0), 0.6, "EDGE", 1.4, fill="HEAD", opacity=0.07)

    def post(sc):
        sc.note((0.0, -0.6), "end face, radius l/3 (not to scale)", "TEXT", "middle", 13, dy=20)

    return rotation_view2(660, 520, (260, 350), 150, PHI, _ax("j", "2"), _ax("k", "2"), _ax("y", "B"), _ax("z", "B"),
                          _ax("i", "2") + " = " + _ax("i", "B") + " (⊙) at G", ("φ", ""), pre=pre, post=post,
                          out_off=(-16, 28), arc_r=0.30, cy=0.72, lab_r=0.50)


def _obl(x, y, z):
    """Oblique view of the body frame: x_B right, z_B up, y_B into the page (receding up and to the right)."""
    return (x + 0.433 * y, z + 0.25 * y)


@figure("rb25-cylinder",
        "Homogeneous cylinder with its body axes and a volume element in cylindrical coordinates.",
        r"Volume element in cylindrical coordinates about the axis $Gx_B$, with Jacobian $s$; $C$ and $D$ are the "
        r"centres of the end faces, at the distance $l$ from $G$.")
def cylinder():
    sc = Scene(760, 480, (340, 260), 125)
    l, R = 1.5, 0.5

    def ringx(x, r, a0=0.0, a1=360.0, n=72):
        pts = []
        for i in range(n + 1):
            a = math.radians(a0 + (a1 - a0) * i / n)
            pts.append(_obl(x, r * math.cos(a), r * math.sin(a)))
        return pts

    hull = _hull(ringx(-l, R) + ringx(l, R))
    sc.poly(hull, "HEAD", 1.8, fill="HEAD", close=True, opacity=0.06)
    sc.poly(ringx(l, R), "HEAD", 1.4)
    sc.poly(ringx(-l, R, 90, 270), "HEAD", 1.4)
    sc.poly(ringx(-l, R, -90, 90), "HEAD", 1.0, dash="4 3")
    # body axes from G
    for tip, nm, off in ((_obl(2.15, 0, 0), _ax("x", "B"), (16, 5)), (_obl(0, 0.9, 0), _ax("y", "B"), (-6, -10)),
                         (_obl(0, 0, 0.95), _ax("z", "B"), (12, 4))):
        sc.vec((0.0, 0.0), tip, None, "EDGE", 1.4, head=8)
        sc.label(tip, nm, "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    # volume element: x_B = 0.5, s = 0.35, alpha = 50 deg
    x0, s0, al, ds, dal, dx = 0.5, 0.35, math.radians(50), 0.12, math.radians(18), 0.2
    pa = lambda x, s, a: _obl(x, s * math.cos(a), s * math.sin(a))
    face = [pa(x0, s0, al - dal / 2), pa(x0, s0 + ds, al - dal / 2), pa(x0, s0 + ds, al + dal / 2),
            pa(x0, s0, al + dal / 2)]
    top = [pa(x0, s0 + ds, al - dal / 2), pa(x0 + dx, s0 + ds, al - dal / 2), pa(x0 + dx, s0 + ds, al + dal / 2),
           pa(x0, s0 + ds, al + dal / 2)]
    sc.poly(top, "BLUE", 1.2, fill="BLUE", close=True, opacity=0.45)
    sc.poly(face, "BLUE", 1.2, fill="BLUE", close=True, opacity=0.6)
    A0 = _obl(x0, 0, 0)
    sc.dotp(A0, 3.0, "BLUE")
    sc.line(A0, pa(x0, s0, al), "BLUE", 1.4, "5 3")
    sc.label(pa(x0, s0 / 2, al), "s", "BLUE", "start", 16, dx=10, dy=-6)
    sc.arc(A0, 0.20, 14, 50 + 4, "GREEN", 1.5)
    sc.line(A0, _obl(x0, 0.30, 0), "GREEN", 1.0, "3 3")
    sc.label(add(A0, (0.27 * math.cos(math.radians(22)), 0.27 * math.sin(math.radians(22)))), "α", "GREEN", "start", 15,
             dx=12, dy=8)
    sc.line(pa(x0 + dx, s0 + ds, al), (0.55, 0.86), "BLUE", 0.9)
    sc.label((0.55, 0.86), "dm = ρ s ds dα dx" + S("", "B"), "BLUE", "start", 15, dx=6, dy=-4)
    sc.dashed((0.0, 0.0), _obl(x0, 0, 0))
    sc.label(((0.0 + A0[0]) / 2, 0.0), _ax("x", "B"), "BLUE", "middle", 14, weight="700", dy=18)
    # G, C, D
    for x, nm, dx_, dy_ in ((0.0, "G", -14, 20), (-l, "C", -16, 4), (l, "D", 8, 26)):
        P = _obl(x, 0, 0)
        sc.dotp(P, 4.5)
        sc.label(P, nm, "HEAD", "middle", 17, dx=dx_, dy=dy_)
    # dimensions
    sc.dim((-l, -0.95), (l, -0.95), "2l", off=(0, 24), size=16)
    sc.line(_obl(-l, 0, -R), (-l, -1.0), "EDGE", 0.8, "2 4")
    sc.line(_obl(l, 0, -R), (l, -1.0), "EDGE", 0.8, "2 4")
    sc.line(_obl(l, 0, 0), _obl(l, 0, R), "TEXT", 1.2, "4 3")
    sc.label(_obl(l, 0, R), "R = l/3", "TEXT", "start", 15, dx=12, dy=-10)
    return sc


def _solve_G(i2, l=1.0, gx=-0.2):
    """G with |AC| = l and |BD| = l for C = G - l i2, D = G + l i2, A = 0, B = (0, 3l, 0), given x_G (lower root)."""
    p1 = (l * i2[1], l * i2[2])
    p2 = (3 * l - l * i2[1], -l * i2[2])
    r1 = math.sqrt(l * l - (gx - l * i2[0]) ** 2)
    r2 = math.sqrt(l * l - (gx + l * i2[0]) ** 2)
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    dd = math.hypot(dx, dy)
    a = (r1 * r1 - r2 * r2 + dd * dd) / (2 * dd)
    h = math.sqrt(max(0.0, r1 * r1 - a * a))
    mx, my = p1[0] + a * dx / dd, p1[1] + a * dy / dd
    cands = [(mx + h * dy / dd, my - h * dx / dd), (mx - h * dy / dd, my + h * dx / dd)]
    gy, gz = min(cands, key=lambda q: q[1])
    return (gx, gy, gz)


@figure("rb25-fbd",
        "Free-body diagram of the hanging cylinder with its weight and the two string tensions along the strings.",
        r"Free-body diagram: weight $-mg\,\mathbf k$ at $G$, $T_C$ at $C$ towards $A$ and $T_D$ at $D$ towards $B$. Both "
        r"strings act on the axis, so they have no moment about it.")
def fbd():
    sc = Scene(720, 460, (110, 110), 105)
    be, th = math.radians(70.0), math.radians(15.0)
    i2 = (math.cos(th) * math.cos(be), math.cos(th) * math.sin(be), -math.sin(th))
    j2 = (-math.sin(be), math.cos(be), 0.0)
    k2 = (math.sin(th) * math.cos(be), math.sin(th) * math.sin(be), math.cos(th))
    G = _solve_G(i2)
    C, D = vadd(G, i2, -1.0), vadd(G, i2, 1.0)
    A, B = (0.0, 0.0, 0.0), (0.0, 3.0, 0.0)
    # ceiling and its supports
    sc.ground(p3v((0.0, -0.45, 0.0)), p3v((0.0, 3.6, 0.0)), side=1)
    # fixed axes at A
    for tip, nm, off in ((p3(1.15, 0, 0), "x", (-12, 14)), (p3(0, 3.9, 0), "y", (12, 6)), (p3(0, 0, -0.0), "", (0, 0))):
        if nm:
            sc.vec(p3v(A), tip, None, "EDGE", 1.2, head=8)
            sc.label(tip, bold(nm), "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    sc.vec(p3v(A), p3(0, 0, 0.8), None, "EDGE", 1.2, head=8)
    sc.label(p3(0, 0, 0.8), bold("z"), "TEXT", "middle", 16, weight="700", dx=12, dy=2)
    # cylinder: silhouette of the two end rings
    R = 1.0 / 3
    pts = ring(C, j2, k2, R, n=48) + ring(D, j2, k2, R, n=48)
    sc.poly(_hull(pts), "HEAD", 1.8, fill="HEAD", close=True, opacity=0.06)
    sc.poly(ring(D, j2, k2, R), "HEAD", 1.3)
    sc.line(p3v(C), p3v(D), "HEAD", 1.0, "5 3")
    # strings (removed): dashed pink lines, and the tensions
    sc.line(p3v(C), p3v(A), "PINK", 1.2, "6 4")
    sc.line(p3v(D), p3v(B), "PINK", 1.2, "6 4")
    uC, uD = vsub(A, C), vsub(B, D)
    sc.vec(p3v(C), p3v(vadd(C, uC, 0.55)), S("T", "C"), "PINK", 3.4, name_off=(-16, 4), size=17, head=12)
    sc.vec(p3v(D), p3v(vadd(D, uD, 0.55)), S("T", "D"), "PINK", 3.4, name_off=(16, 6), size=17, head=12)
    sc.vec(p3v(G), p3v(vadd(G, (0.0, 0.0, 1.0), -0.7)), "mg", "PINK", 3.6, name_off=(-18, 8), size=17, head=13)
    # arms from G to C and D
    sc.vec(p3v(G), p3v(vadd(G, i2, -0.82)), None, "BLUE", 2.4, head=10)
    sc.vec(p3v(G), p3v(vadd(G, i2, 0.82)), None, "BLUE", 2.4, head=10)
    sc.label(p3v(vadd(G, i2, -0.45)), S(bold("r"), "G", "C") + " = −l " + _ax("i", "2"), "BLUE", "end", 15, weight="700",
             dx=-4, dy=24)
    sc.label(p3v(vadd(G, i2, 0.45)), S(bold("r"), "G", "D") + " = l " + _ax("i", "2"), "BLUE", "end", 15, weight="700",
             dx=30, dy=30)
    for P, nm, dx, dy in ((C, "C", -14, 8), (D, "D", 14, 10), (G, "G", 14, 22)):
        sc.dotp(p3v(P), 4.5)
        sc.label(p3v(P), nm, "HEAD", "middle", 17, dx=dx, dy=dy)
    for P, nm in ((A, "A"), (B, "B")):
        sc.mass(p3v(P), None, r=5, col="HEAD")
        sc.label(p3v(P), nm, "HEAD", "middle", 17, dx=-14 if nm == "A" else 14, dy=-12)
    return sc
