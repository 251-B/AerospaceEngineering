"""Problem RB-03: gyroscope with outer gimbal (beta about Y), inner gimbal (gamma about CD) and flywheel (theta about EF)."""
import math

from figures.em_solutions import figure
from figures.em_sol.rb01 import (add, arrow_px, cross, norm, p3, p3v, rotation_view, sub, vadd, vscale)
from figures.mech import S, Scene, bold, dot1

BETA, GAMMA, THETA = 25.0, 30.0, 40.0


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


def _frame_vectors():
    cb, sb = math.cos(math.radians(BETA)), math.sin(math.radians(BETA))
    cg, sg = math.cos(math.radians(GAMMA)), math.sin(math.radians(GAMMA))
    j = (0.0, 1.0, 0.0)
    i1 = (cb, 0.0, -sb)
    k1 = (sb, 0.0, cb)
    j2 = vadd(vscale(j, cg), k1, sg)
    k2 = vadd(vscale(j, -sg), k1, cg)
    return j, i1, k1, j2, k2


def _curved(sc, centre, axis, r, t0, t1, col, name, name_off=(0, 0), size=17):
    """Circular arrow of radius r about `axis` (right-hand sense) from t0 to t1 degrees, in the cabinet view."""
    w = norm(axis)
    helper = (0.0, 0.0, 1.0) if abs(w[2]) < 0.9 else (1.0, 0.0, 0.0)
    u = norm(cross(helper, w))
    v = cross(w, u)
    pts = []
    n = 40
    for i in range(n + 1):
        t = math.radians(t0 + (t1 - t0) * i / n)
        q = vadd(centre, vadd(vscale(u, r * math.cos(t)), v, r * math.sin(t)))
        pts.append(p3v(q))
    sc.poly(pts, col, 1.8)
    arrow_px(sc, pts[-3], pts[-1], col, 10)
    mid = pts[n // 2]
    if name:
        sc.label(mid, name, col, "middle", size, weight="700", dx=name_off[0], dy=name_off[1])


def _rect(sc, c, a, b, ha, hb, col, w=2.0, opacity=None):
    pts = [vadd(vadd(c, a, ha), b, hb), vadd(vadd(c, a, ha), b, -hb), vadd(vadd(c, a, -ha), b, -hb),
           vadd(vadd(c, a, -ha), b, hb)]
    q = [p3v(p) for p in pts]
    if opacity:
        sc.poly(q, col, 0.0, fill=col, close=True, opacity=opacity)
    sc.poly(q, col, w, close=True)


@figure("rb03-gimbal-chain",
        "Schematic of the outer gimbal, inner gimbal and flywheel with their three rotation axes AB, CD and EF.",
        r"Kinematic chain of the gyroscope: the outer gimbal turns by $\beta$ about the fixed axis $AB$ ($Y$), the inner "
        r"gimbal by $\gamma$ about $CD$, and the flywheel by $\theta$ about its axle $EF$; each rate acts along its own "
        r"bearing axis.")
def gimbal_chain():
    sc = Scene(760, 520, (330, 270), 150)
    O = (0.0, 0.0, 0.0)
    j, i1, k1, j2, k2 = _frame_vectors()
    ex, ey, ez = (1.0, 0.0, 0.0), j, (0.0, 0.0, 1.0)
    # fixed axes (thin grey)
    for tip, nm, off in ((vscale(ex, 1.2), "X", (-12, 14)), (vscale(ey, 2.45), "Y", (12, 14)),
                         (vscale(ez, 1.45), "Z", (-12, 0))):
        sc.vec((0.0, 0.0), p3v(tip), None, "EDGE", 1.4, head=8)
        sc.label(p3v(tip), bold(nm), "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    # outer gimbal: rectangle in the plane (Y, i1); bearings A, B on Y; pins to C and D along i1
    wy, hi = 1.55, 1.0
    _rect(sc, O, ey, i1, wy, hi, "BLUE", 2.2, 0.06)
    A, B = vscale(ey, -wy), vscale(ey, wy)
    # inner gimbal: rectangle in the plane (i1, j2); pivots C, D on i1; bearings E, F on j2
    wi, hc = 0.95, 0.78
    _rect(sc, O, i1, j2, hc, wi, "GREEN", 2.2, 0.08)
    C, D = vscale(i1, hc), vscale(i1, -hc)
    sc.line(p3v(C), p3v(vscale(i1, hi)), "GREEN", 2.0)
    sc.line(p3v(D), p3v(vscale(i1, -hi)), "GREEN", 2.0)
    E, F = vscale(j2, -wi), vscale(j2, wi)
    # flywheel: circle in the plane (i1, k2), axle EF along j2
    fl = []
    for t in range(0, 361, 6):
        a = math.radians(t)
        fl.append(p3v(vadd(vscale(i1, 0.52 * math.cos(a)), k2, 0.52 * math.sin(a))))
    sc.poly(fl, "ACC", 0.0, fill="ACC", close=True, opacity=0.25)
    sc.poly(fl, "ACC", 2.2, close=True)
    sc.line(p3v(E), p3v(F), "ACC", 2.6)
    ang = math.radians(THETA + 30)
    rad = vadd(vscale(i1, 0.52 * math.cos(ang)), k2, 0.52 * math.sin(ang))
    sc.line((0.0, 0.0), p3v(rad), "ACC", 1.6)
    # bearings
    for pt, nm, col, off in ((A, "A", "BLUE", (-14, 18)), (B, "B", "BLUE", (14, 18)), (C, "C", "GREEN", (-16, 8)),
                             (D, "D", "GREEN", (10, -8)), (E, "E", "ACC", (-18, 6)), (F, "F", "ACC", (-6, -12))):
        sc.mass(p3v(pt), None, r=5, col=col)
        sc.label(p3v(pt), nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.dotp((0.0, 0.0), 3.5)
    sc.label((0.0, 0.0), "O", "HEAD", "middle", 17, dx=16, dy=22)
    # rate vectors beyond the bearings, each with its curved arrow
    sc.vec(p3v(vadd(B, ey, 0.05)), p3v(vadd(B, ey, 0.55)), dot1("β") + " " + _ax("j"), "BLUE", 3.0,
           name_off=(2, -14), size=17, head=11)
    sc.vec(p3v(vadd(C, i1, 0.30)), p3v(vadd(C, i1, 0.85)), dot1("γ") + " " + _ax("i", "1"), "GREEN", 3.0,
           name_off=(-40, 14), size=17, head=11)
    sc.vec(p3v(vadd(F, j2, 0.05)), p3v(vadd(F, j2, 0.55)), dot1("θ") + " " + _ax("j", "2"), "ACC", 3.0,
           name_off=(6, -14), size=17, head=11)
    _curved(sc, vadd(B, ey, 0.30), ey, 0.20, 40, 300, "BLUE", "β", (22, 6))
    _curved(sc, vadd(C, i1, 0.58), i1, 0.20, 40, 300, "GREEN", "γ", (-8, 22))
    _curved(sc, vadd(F, j2, 0.30), j2, 0.20, 40, 300, "ACC", "θ", (22, 6))
    sc.note(p3v(A), "axis AB = Y", "TEXT", "start", 13, dx=-26, dy=40)
    return sc


@figure("rb03-rotation-beta",
        "View along the bearing axis AB showing the outer gimbal rotation by beta.",
        r"Outer gimbal, viewed with $\mathbf j$ out of the paper ($\mathbf k$ to the right, $\mathbf i$ up). A "
        r"counterclockwise turn by $\beta$ makes $\mathbf i_1$ lean towards $-\mathbf k$, which is the minus sign in the "
        r"third row of the matrix.")
def rotation_beta():
    def post(sc):
        c, s = math.cos(math.radians(30)), math.sin(math.radians(30))
        sc.note((-s / 2, c / 2), "axis CD (D to C)", "BLUE", "end", 13, dx=-12, dy=4)

    return rotation_view(620, 470, (300, 330), 160, 30.0, _ax("k"), _ax("i"), _ax("k", "1"), _ax("i", "1"),
                         _ax("j") + " = " + _ax("j", "1") + " (AB)", ("β", ""), post=post, out_off=(-16, 28))


@figure("rb03-rotation-gamma",
        "View along the bearing axis CD showing the inner gimbal rotation by gamma.",
        r"Inner gimbal, viewed with $\mathbf i_1$ out of the paper. The counterclockwise turn by $\gamma$ tilts the "
        r"flywheel axle $\mathbf j_2$ from $\mathbf j_1$ towards $\mathbf k_1$.")
def rotation_gamma():
    def post(sc):
        c, s = math.cos(math.radians(30)), math.sin(math.radians(30))
        sc.note((0.45, 0.50), "axle EF", "GREEN", "start", 13)

    return rotation_view(620, 470, (260, 330), 160, 30.0, _ax("j", "1"), _ax("k", "1"), _ax("j", "2"), _ax("k", "2"),
                         _ax("i", "1") + " = " + _ax("i", "2") + " (CD)", ("γ", ""), col="GREEN", post=post,
                         out_off=(-16, 28))


@figure("rb03-rotation-theta",
        "View along the flywheel axle showing the spin rotation by theta.",
        r"Flywheel, viewed with its axle $\mathbf j_2$ out of the paper ($\mathbf k_2$ to the right, $\mathbf i_2$ up). "
        r"The spin by $\theta$ makes $\mathbf i_B$ lean towards $-\mathbf k_2$, as in the outer gimbal view.")
def rotation_theta():
    def pre(sc):
        sc.circle((0.0, 0.0), 1.0, "ACC", 1.6, fill="ACC", opacity=0.10)

    return rotation_view(620, 540, (300, 330), 160, THETA, _ax("k", "2"), _ax("i", "2"), _ax("k", "B") + " (z)",
                         _ax("i", "B") + " (x)", _ax("j", "2") + " = " + _ax("j", "B") + " (EF, y)", ("θ", ""),
                         col="ACC", tri="BLUE", pre=pre, out_off=(-16, 28))
