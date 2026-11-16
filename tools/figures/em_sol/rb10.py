"""Problem RB-10: firedoor hanging from two equal links (parallelogram, curvilinear translation)."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle
from figures.em_sol.rb01 import add, arrow_px, d
from figures.em_sol.rb06 import rlabel
from figures.mech import S, Scene, bold, dot1

TH = 30.0
L_, B_, H_, W_ = 1.6, 2.2, 1.8, 2.6


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


def _tick(sc, p, deg, n=1, size=0.06):
    """Equal-length mark: n short strokes across the line at `deg` degrees, centred at p."""
    a = math.radians(deg)
    t = (math.cos(a), math.sin(a))
    nrm = (-t[1], t[0])
    for k in range(n):
        off = (k - (n - 1) / 2) * 0.05
        c = (p[0] + off * t[0], p[1] + off * t[1])
        sc.line((c[0] - size * nrm[0], c[1] - size * nrm[1]), (c[0] + size * nrm[0], c[1] + size * nrm[1]), "HEAD", 1.6)


def _door(sc, A, B, w=W_, h=H_, top=True):
    """Door outline: thin rectangle of width w and height h below the top edge AB (centred on AB)."""
    cx = (A[0] + B[0]) / 2
    y0 = A[1]
    pts = [(cx - w / 2, y0), (cx - w / 2, y0 - h), (cx + w / 2, y0 - h), (cx + w / 2, y0)]
    sc.poly(pts, "HEAD", 1.4)
    sc.line((cx - w / 2, y0), (cx + w / 2, y0), "HEAD", 1.4)
    return pts


@figure("rb10-parallelogram",
        "Parallelogram formed by the ceiling, the two equal links and the top edge of the door.",
        r"The ceiling pins, the two links of length $L$ and the top edge $AB$ form a parallelogram, so $AB$ stays "
        r"parallel to the ceiling: the door translates and $\boldsymbol\omega_{B0} = \mathbf 0$.")
def parallelogram():
    sc = Scene(600, 480, (150, 90), 95)
    s, c = math.sin(math.radians(TH)), math.cos(math.radians(TH))
    OA, OB = (0.0, 0.0), (B_, 0.0)
    A, B = (L_ * s, -L_ * c), (B_ + L_ * s, -L_ * c)
    sc.ground((-0.9, 0.0), (B_ + 1.0, 0.0), side=1)
    _door(sc, A, B)
    sc.line(OA, A, "EDGE", 5.0)
    sc.line(OB, B, "EDGE", 5.0)
    sc.line(A, B, "HEAD", 3.6)
    # dashed vertical and the angle theta
    sc.line(OA, (0.0, -L_ * c - 0.25), "EDGE", 1.1, "5 4")
    sc.arc(OA, 0.9, 270, 270 + TH, "GREEN", 1.7, head=True)
    sc.label(add(OA, d(270 + TH / 2), 0.9), "θ", "GREEN", "middle", 17, dx=-6, dy=34)
    # the closed loop, drawn just inside the parallelogram
    cen = ((OA[0] + A[0] + B[0] + OB[0]) / 4, (OA[1] + A[1] + B[1] + OB[1]) / 4)

    def inner(p, q, k=0.16):
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        tx, ty = q[0] - p[0], q[1] - p[1]
        n = math.hypot(tx, ty)
        nx, ny = -ty / n, tx / n
        if (cen[0] - mx) * nx + (cen[1] - my) * ny < 0:
            nx, ny = -nx, -ny
        sh = (nx * k, ny * k)
        u = (tx / n * 0.22, ty / n * 0.22)
        return (p[0] + sh[0] + u[0], p[1] + sh[1] + u[1]), (q[0] + sh[0] - u[0], q[1] + sh[1] - u[1])

    for p, q in ((OA, A), (A, B), (B, OB), (OB, OA)):
        a, b = inner(p, q)
        sc.vec(a, b, None, "BLUE", 2.4, head=10)
    sc.label(((OA[0] + A[0]) / 2, (OA[1] + A[1]) / 2), "L " + _ax("e", "L"), "BLUE", "start", 16, weight="700", dx=34, dy=2)
    sc.label(((A[0] + B[0]) / 2, A[1]), "b " + _ax("i", "B"), "BLUE", "middle", 16, weight="700", dy=-22)
    sc.label(((B[0] + OB[0]) / 2, (B[1] + OB[1]) / 2), "−L " + _ax("e", "L"), "BLUE", "end", 16, weight="700", dx=-34, dy=2)
    sc.label(((OA[0] + OB[0]) / 2, 0.0), "−b " + _ax("i"), "BLUE", "middle", 16, weight="700", dy=36)
    # equal-length marks
    _tick(sc, ((OA[0] + A[0]) / 2, (OA[1] + A[1]) / 2), -90 + TH + 90 - 90 + 0, 1)
    _tick(sc, ((OB[0] + B[0]) / 2, (OB[1] + B[1]) / 2), -90 + TH + 90 - 90 + 0, 1)
    _tick(sc, ((OA[0] + OB[0]) / 2, 0.0), 0, 2)
    _tick(sc, ((A[0] + B[0]) / 2, A[1]), 0, 2)
    # pins and points
    for p, nm, dx, dy in ((OA, S("O", "A"), -4, -20), (OB, S("O", "B"), 4, -20), (A, "A", -24, -6), (B, "B", 14, -14)):
        sc.mass(p, None, r=5, col="HEAD")
        sc.label(p, nm, "HEAD", "middle", 17, dx=dx, dy=dy)
    axis_out(sc, (-0.55, -0.55), None, "HEAD")
    sc.label((-0.55, -0.55), _ax("k") + " (⊙)", "HEAD", "middle", 15, weight="700", dx=0, dy=28)
    return sc


@figure("rb10-kinematics",
        "Right triangle of the left link with the link basis e_t, e_n and the circular path of the centre of mass.",
        r"Link of length $L$ as the hypotenuse: legs $L\sin\theta$ (horizontal) and $L\cos\theta$ (vertical). "
        r"$\mathbf e_t$ and $\mathbf e_n$ are $\mathbf i$ and $\mathbf j$ turned by $\theta$ about $\mathbf k$ (⊙); $G$ "
        r"moves on a circle of radius $L$.")
def kinematics():
    sc = Scene(640, 520, (120, 90), 105)
    s, c = math.sin(math.radians(TH)), math.cos(math.radians(TH))
    OA = (0.0, 0.0)
    A = (L_ * s, -L_ * c)
    foot = (0.0, -L_ * c)
    G = (A[0] + B_ / 2, A[1] - H_ / 2)
    cen = (B_ / 2, -H_ / 2)
    triangle(sc, [OA, foot, A], "BLUE", 0.20)
    fixed_axis(sc, OA, 0, 0.9, _ax("i"), off=(14, 6))
    fixed_axis(sc, OA, 90, 0.55, _ax("j"), off=(14, 4))
    axis_out(sc, OA, None, "HEAD")
    sc.label(OA, _ax("k") + " (⊙) at O" + S("", "A"), "HEAD", "end", 15, weight="700", dx=-14, dy=22)
    sc.line(OA, A, "EDGE", 5.0)
    sc.line(OA, foot, "EDGE", 1.1, "5 4")
    sc.dashed(foot, A)
    right_angle(sc, foot, 90, 0, 0.07)
    sc.arc(OA, 0.5, 270, 270 + TH, "GREEN", 1.7, head=True)
    sc.label(add(OA, d(270 + TH / 2), 0.5), "θ", "GREEN", "middle", 16, dx=-12, dy=22)
    sc.label((0.0, -L_ * c / 2), "L cos θ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.label((L_ * s / 2, -L_ * c), "L sin θ", "TEXT", "middle", 15, dx=-8, dy=22)
    sc.label((L_ * s / 2, -L_ * c / 2), "L", "TEXT", "start", 16, dx=12, dy=-10)
    # unit vectors e_t, e_n at A and the copy of the fixed axes
    sc.vec(A, (A[0] + 0.55, A[1]), None, "EDGE", 1.3, head=8)
    sc.vec(A, (A[0], A[1] + 0.55), None, "EDGE", 1.3, head=8)
    sc.label((A[0] + 0.55, A[1]), _ax("i"), "TEXT", "middle", 15, weight="700", dx=12, dy=14)
    sc.label((A[0], A[1] + 0.55), _ax("j"), "TEXT", "middle", 15, weight="700", dx=12, dy=4)
    et = (A[0] + 0.62 * c, A[1] + 0.62 * s)
    en = (A[0] - 0.62 * s, A[1] + 0.62 * c)
    sc.vec(A, et, _ax("e", "t"), "ACC", 3.0, name_off=(18, -6), size=17, head=11)
    sc.vec(A, en, _ax("e", "n"), "ACC", 3.0, name_off=(-16, -2), size=17, head=11)
    sc.arc(A, 0.36, 0, TH, "GREEN", 1.5, head=True)
    sc.arc(A, 0.36, 90, 90 + TH, "GREEN", 1.5, head=True)
    sc.label(add(A, d(TH / 2 - 8), 0.50), "θ", "GREEN", "middle", 14, dx=2, dy=14)
    sc.label(add(A, d(90 + TH / 2), 0.52), "θ", "GREEN", "middle", 14, dx=0, dy=5)
    # centre of mass and its circle
    sc.dashed(A, (G[0], A[1]))
    sc.dashed((G[0], A[1]), G)
    sc.label((A[0] + 0.72 * (G[0] - A[0]), A[1]), "b/2", "TEXT", "middle", 15, dy=-8)
    sc.label((G[0], (A[1] + G[1]) / 2), "h/2", "TEXT", "start", 15, dx=8, dy=5)
    pts = [add(cen, d(a), L_) for a in range(-140, -22, 3)]
    sc.poly(pts, "EDGE", 1.3, "7 4")
    sc.vec(G, add(G, d(TH), 0.9), None, "GREEN", 3.0, head=12)
    sc.label(add(G, d(TH), 0.9), S(bold("v"), "0", "G") + " = L" + dot1("θ") + " " + _ax("e", "t"), "GREEN", "start", 16,
             weight="700", dx=8, dy=-8)
    sc.dotp(G, 4.5)
    sc.label(G, "G", "HEAD", "middle", 17, dx=-14, dy=20)
    sc.mass(A, None, r=5, col="HEAD")
    sc.label(A, "A", "HEAD", "middle", 17, dx=-4, dy=28)
    return sc


@figure("rb10-plate",
        "Door plate with its centre of mass and the arms to the two pins.",
        r"Centre of mass of the door at the centre of the rectangle; the arms to the pins are "
        r"$\mathbf r_G^A = -\tfrac b2\,\mathbf i + \tfrac h2\,\mathbf j$ and $\mathbf r_G^B = \tfrac b2\,\mathbf i + "
        r"\tfrac h2\,\mathbf j$.")
def plate():
    sc = Scene(640, 480, (320, 250), 100)
    w, h, b = W_, H_, B_
    sc.poly([(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)], "HEAD", 1.8, close=True)
    sc.vec((0, 0), (w / 2 + 0.3, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((w / 2 + 0.3, 0.0), "x′", "TEXT", "middle", 16, weight="700", dx=12, dy=5)
    sc.vec((0, 0), (0.0, h / 2 + 0.2), None, "EDGE", 1.4, head=8)
    sc.label((0.0, h / 2 + 0.2), "y′", "TEXT", "middle", 16, weight="700", dx=12, dy=2)
    # arms to the pins
    for sgn, nm, sym in ((-1, "A", S(bold("r"), "G", "A")), (1, "B", S(bold("r"), "G", "B"))):
        P = (sgn * b / 2, h / 2)
        sc.vec((0, 0), (P[0] * 0.97, P[1] * 0.97), None, "BLUE", 2.6, head=11)
        sc.mass(P, None, r=5, col="HEAD")
        sc.label(P, nm, "HEAD", "middle", 17, dx=sgn * 14, dy=-10)
        sc.label((P[0] * 0.5, P[1] * 0.5), sym, "BLUE", "end", 16, weight="700", dx=-6 if sgn < 0 else -2,
                 dy=-8 if sgn < 0 else -10)
    # mass element
    px, py, e = 0.5 * w / 2, 0.4 * h / 2, 0.04
    sc.poly([(px - e, py - e), (px + e, py - e), (px + e, py + e), (px - e, py + e)], "BLUE", 1.2, fill="BLUE",
            close=True, opacity=0.5)
    sc.line((px, py - e), (px, 0.0), "BLUE", 1.1, "4 3")
    sc.line((px - e, py), (0.0, py), "BLUE", 1.1, "4 3")
    sc.label((px, 0.0), "x′", "BLUE", "middle", 15, weight="700", dy=20)
    sc.label((0.0, py), "y′", "BLUE", "end", 15, weight="700", dx=-8, dy=5)
    sc.label((px, py), "dm", "BLUE", "start", 15, dx=12, dy=20)
    # dimensions
    sc.dim((-b / 2, h / 2 + 0.42), (b / 2, h / 2 + 0.42), "b", off=(-40, -8), size=16)
    sc.dim((-w / 2 - 0.25, -h / 2), (-w / 2 - 0.25, h / 2), "h", off=(-14, 5), size=16)
    sc.dim((-w / 2, -h / 2 - 0.25), (w / 2, -h / 2 - 0.25), "w", off=(0, 24), size=16)
    sc.dotp((0, 0), 4.5)
    sc.label((0, 0), "G", "HEAD", "middle", 17, dx=-12, dy=22)
    return sc


@figure("rb10-fbd",
        "Free-body diagram of the door with its weight and the two link forces along the links.",
        r"Free-body diagram: weight $-mg\,\mathbf j$ at $G$ and the link forces $T_A\,\mathbf e_n$ at $A$ and "
        r"$T_B\,\mathbf e_n$ at $B$, along the links (two-force members); for $\theta \gt 0$ the left link pulls harder.")
def fbd():
    sc = Scene(640, 520, (330, 250), 100)
    w, h, b = W_, H_, B_
    s, c = math.sin(math.radians(TH)), math.cos(math.radians(TH))
    sc.poly([(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)], "HEAD", 1.8, close=True)
    A, B = (-b / 2, h / 2), (b / 2, h / 2)
    en = (-s, c)
    for P, T, nm, lab in ((A, 0.85, "A", S("T", "A")), (B, 0.35, "B", S("T", "B"))):
        sc.line(P, add(P, en, 1.45), "EDGE", 1.2, "6 4")
        tip = add(P, en, T)
        sc.vec(P, tip, lab, "PINK", 3.4, name_off=(-18, 4) if nm == "A" else (-18, 6), size=17, head=12)
        sc.mass(P, None, r=5, col="HEAD")
        sc.label(P, nm, "HEAD", "middle", 17, dx=-2, dy=24)
    sc.line((0, 0), A, "EDGE", 1.1, "4 3")
    sc.line((0, 0), B, "EDGE", 1.1, "4 3")
    sc.vec((0, 0), (0, -1.2), "mg", "PINK", 3.4, name_off=(24, 6), size=17, head=12)
    sc.dotp((0, 0), 4.5)
    sc.label((0, 0), "G", "HEAD", "middle", 17, dx=-12, dy=22)
    # reference link basis at a corner
    o = (-w / 2 - 0.55, -h / 2 + 0.15)
    sc.vec(o, add(o, d(TH), 0.55), _ax("e", "t"), "ACC", 3.0, name_off=(16, -2), size=17, head=11)
    sc.vec(o, add(o, d(90 + TH), 0.55), _ax("e", "n"), "ACC", 3.0, name_off=(-14, -4), size=17, head=11)
    sc.label(o, "link basis", "TEXT", "middle", 13, italic=False, dy=24)
    return sc
