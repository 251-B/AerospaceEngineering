"""Theory figures of Topic 7 (Momentum, Kinetic Energy and Rigid Body Dynamics)."""
import math

from figures.em_theory import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.mech import S, Scene, bold

RED = "#ef4444"          # principal axes e1, e2, e3
DRED = "#be123c"         # angular momentum H_G
ORANGE = "ACC"


def _d(deg):
    return math.cos(math.radians(deg)), math.sin(math.radians(deg))


def _add(p, q, k=1.0):
    return (p[0] + k * q[0], p[1] + k * q[1])


def _blob(c, r, phase=0.0, n=72):
    pts = []
    for i in range(n):
        f = 2 * math.pi * i / n
        rr = r * (1 + 0.12 * math.sin(3 * f + phase) + 0.07 * math.cos(2 * f) + 0.04 * math.sin(5 * f))
        pts.append((c[0] + rr * math.cos(f), c[1] + 0.82 * rr * math.sin(f)))
    return pts


def _frame(sc, o, names, col, length, offs, w=2.2):
    """Short parallel frame (x down-left at 218 deg, y right, z up) with subscripted names."""
    dirs = [(-0.789, -0.614), (1.0, 0.0), (0.0, 1.0)]
    for dv, nm, off in zip(dirs, names, offs):
        tip = _add(o, dv, length)
        sc.vec(o, tip, nm, col, w, name_off=off, size=15, head=8)


def _frame_axes(sc, o, lens, offs, names):
    dirs = [(-0.789, -0.614), (1.0, 0.0), (0.0, 1.0)]
    for dv, ln, nm, off in zip(dirs, lens, names, offs):
        sc.vec(o, _add(o, dv, ln), None, "EDGE", 1.4, head=8)
        sc.label(_add(o, dv, ln), nm, "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])


def _xyz(sub):
    return [bold(c) + S("", sub) for c in ("x", "y", "z")]


# --------------------------------------------------------------------------------------------------------------------
@figure("t7-material-system",
        "A rigid body with its centre of mass G, a material element P and a generic point A, with the position vectors "
        "from O, A and G.",
        r"Material system $B$ moving in the fixed frame $S_0$. The frames $S_A$ and $S_G$ have origins at $A$ and $G$ "
        r"and axes parallel to $S_0$, so they translate without rotating.")
def material_system():
    sc = Scene(600, 420, (190, 290), 150)
    O, A, G, P = (0.0, 0.0), (-0.5, 0.8), (1.3, 0.0), (1.0, 1.0)
    triangle(sc, _blob((1.4, 0.4), 0.9), "BLUE", 0.16)
    sc.poly(_blob((1.4, 0.4), 0.9), "BLUE", 1.6, close=True)
    sc.note((2.15, 0.95), "B", "TEXT", "start", 15)
    _frame_axes(sc, O, [1.1, 2.4, 1.6], [(-12, 14), (8, 20), (-14, 4)], _xyz("0"))
    # parallel frames
    _frame(sc, G, _xyz("G"), "BLUE", 0.6, [(-16, 10), (4, 20), (16, 6)])
    _frame(sc, A, _xyz("A"), "PINK", 0.6, [(-16, 10), (14, 14), (-16, 4)])
    # position vectors
    sc.vec(O, A, None, "HEAD", 1.9, head=9)
    sc.vec(O, G, None, "HEAD", 1.9, head=9)
    sc.vec(O, P, None, "HEAD", 1.9, head=9)
    sc.vec(A, P, None, "PINK", 2.0, head=9)
    sc.vec(G, P, None, "BLUE", 2.0, head=9)
    sc.label((-0.30, 0.50), S(bold("r"), "0", "A"), "HEAD", "end", 16, dx=-10, dy=0)
    sc.label((0.65, -0.02), S(bold("r"), "0", "G"), "HEAD", "middle", 16, dy=-12)
    sc.label((0.55, 0.55), S(bold("r"), "0", "P"), "HEAD", "start", 16, dx=8, dy=14)
    sc.label((0.25, 0.92), S(bold("r"), "A", "P"), "PINK", "middle", 16, dy=-9)
    sc.label((1.15, 0.52), S(bold("r"), "G", "P"), "BLUE", "end", 16, dx=-10, dy=-8)
    # velocities
    sc.vec(P, _add(P, (0.55, 0.45)), S(bold("v"), "0", "P"), "BLUE", 2.6, name_off=(26, -2), size=16, head=10)
    sc.vec(G, _add(G, (0.55, 0.45)), S(bold("v"), "0", "G"), "BLUE", 2.6, name_off=(26, -2), size=16, head=10)
    # points
    sc.dotp(O, 4)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=18)
    sc.mass(A, None, r=5, col="PINK")
    sc.label(A, "A", "PINK", "middle", 17, dx=-12, dy=-8)
    sc.mass(G, None, r=5, col="BLUE")
    sc.label(G, "G", "BLUE", "middle", 17, dx=10, dy=18)
    sx, sy = sc.P(P)
    sc.c.add(f'<rect x="{sx - 5:.1f}" y="{sy - 5:.1f}" width="10" height="10" fill="HEAD" fill-opacity="0.9"/>')
    sc.label(P, "P", "HEAD", "middle", 17, dx=-16, dy=-8)
    sc.note(P, "dm", "TEXT", "start", 14, dx=8, dy=-16)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t7-internal-external-forces",
        "Particles of a material system acted on by external forces and by equal and opposite collinear internal forces.",
        r"External forces come from the environment; internal forces act in equal, opposite and collinear pairs, so "
        r"their resultant and their moment about any point vanish.")
def internal_external():
    sc = Scene(680, 480, (150, 340), 160)
    O = (0.0, 0.0)
    P1, P2, P3, G, A = (0.8, 1.0), (1.9, 1.1), (1.6, 0.5), (1.3, 0.6), (1.9, -0.2)
    blob = _blob((1.4, 0.6), 0.85, 1.0)
    triangle(sc, blob, "BLUE", 0.14)
    sc.poly(blob, "BLUE", 1.6, close=True)
    _frame_axes(sc, O, [0.9, 3.0, 1.9], [(-12, 14), (10, 18), (-14, 4)], _xyz("0"))
    _frame(sc, G, _xyz("G"), "BLUE", 0.38, [(-14, 10), (16, -10), (16, 14)], w=1.8)
    # position vectors
    sc.vec(O, P1, None, "HEAD", 1.8, head=8)
    sc.vec(O, G, None, "HEAD", 1.8, head=8)
    sc.vec(G, P1, None, "BLUE", 1.9, head=8)
    sc.vec(A, P3, None, "PINK", 1.9, head=8)
    sc.label((0.40, 0.46), S(bold("r"), "0", "P1"), "HEAD", "end", 16, dx=-3, dy=16)
    sc.label((0.62, 0.20), S(bold("r"), "0", "G"), "HEAD", "start", 16, dx=6, dy=18)
    sc.label((1.05, 0.80), S(bold("r"), "G", "P1"), "BLUE", "end", 16, dx=-4, dy=-4)
    sc.label((1.75, 0.15), S(bold("r"), "A", "P3"), "PINK", "start", 16, dx=6, dy=4)
    # internal pair on the dashed line P1P2
    sc.dashed(P1, P2)
    u = ((P2[0] - P1[0]) / math.hypot(P2[0] - P1[0], P2[1] - P1[1]), (P2[1] - P1[1]) / math.hypot(P2[0] - P1[0], P2[1] - P1[1]))
    sc.vec(P1, _add(P1, u, 0.5), None, "GREEN", 2.2, head=9)
    sc.vec(P2, _add(P2, u, -0.5), None, "GREEN", 2.2, head=9)
    sc.label(_add(P1, u, 0.42), S(bold("f"), "P2", "P1"), "GREEN", "middle", 16, dx=-6, dy=24)
    sc.label(_add(P2, u, -0.42), S(bold("f"), "P1", "P2"), "GREEN", "middle", 16, dy=-14)
    # external forces
    sc.vec(P1, _add(P1, _d(120), 0.62), S(bold("F"), None, "P1"), "GREEN", 3.2, name_off=(-14, -4), size=17, head=11)
    sc.vec(P2, _add(P2, (0.65, 0.0)), S(bold("F"), None, "P2"), "GREEN", 3.2, name_off=(8, -12), size=17, head=11)
    sc.vec(P3, _add(P3, (0.8, 0.0)), S(bold("F"), None, "P3"), "GREEN", 3.2, name_off=(24, 4), size=17, head=11)
    # points
    sc.dotp(O, 4)
    sc.label(O, "O", "HEAD", "end", 17, dx=-8, dy=18)
    for p, nm, off in ((P1, "P1", (-20, 6)), (P2, "P2", (0, -14)), (P3, "P3", (-16, 6))):
        sc.mass(p, None, r=5.5)
        sc.label(p, S("P", None, None).replace("P", "P") + f'<tspan baseline-shift="sub" font-size="70%">{nm[1]}</tspan>',
                 "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.mass(G, None, r=5, col="BLUE")
    sc.label(G, "G", "BLUE", "middle", 17, dx=-16, dy=-4)
    sc.mass(A, None, r=5, col="PINK")
    sc.label(A, "A", "PINK", "middle", 17, dx=12, dy=18)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t7-spring-pair",
        "Two particles joined by a spring of stiffness k, with their position vectors and the pair of spring forces.",
        r"The spring forces derive from one potential energy of the pair; that term appears once in the energy equation.")
def spring_pair():
    sc = Scene(700, 450, (150, 335), 130)
    O = (2.0, 0.0)
    P1, P2 = (0.0, 0.3), (1.6, 1.8)
    for dv, nm, ln, off in (((-0.789, -0.614), bold("x") + S("", "0"), 1.05, (-14, 14)),
                            ((1.0, 0.0), bold("y") + S("", "0"), 1.5, (10, 18)),
                            ((0.0, 1.0), bold("z") + S("", "0"), 2.2, (10, 2))):
        sc.vec(O, _add(O, dv, ln), None, "HEAD", 2.6, head=10)
        sc.label(_add(O, dv, ln), nm, "HEAD", "middle", 17, weight="700", dx=off[0], dy=off[1])
    sc.vec(O, P1, None, "EDGE", 1.4, head=8)
    sc.vec(O, P2, None, "EDGE", 1.4, head=8)
    sc.label((1.0, 0.12), S(bold("r"), "0", "P1"), "TEXT", "middle", 16, dy=-12)
    sc.label((1.80, 1.0), S(bold("r"), "0", "P2"), "TEXT", "start", 16, dx=10, dy=0)
    sc.spring(P1, P2, coils=6, amp=8, col="BLUE", lead=0.12, w=1.8)
    mid = ((P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2)
    sc.label(mid, "k", "BLUE", "end", 18, dx=-20, dy=0)
    n = (math.hypot(P2[0] - P1[0], P2[1] - P1[1]))
    u = ((P2[0] - P1[0]) / n, (P2[1] - P1[1]) / n)
    nrm = (u[1], -u[0])              # to the right of the spring direction
    q1, q2 = _add(P1, nrm, 0.16), _add(P2, nrm, 0.16)
    sc.vec(q1, _add(q1, u, 0.62), None, "GREEN", 2.6, head=10)
    sc.vec(q2, _add(q2, u, -0.62), None, "GREEN", 2.6, head=10)
    sc.label(_add(q1, u, 0.5), S(bold("f"), "P2", "P1"), "GREEN", "start", 16, dx=14, dy=20)
    sc.label(_add(q2, u, -0.5), S(bold("f"), "P1", "P2"), "GREEN", "start", 16, dx=14, dy=14)
    sc.mass(P1, None, r=7, col="PINK")
    sc.mass(P2, None, r=7, col="PINK")
    sc.label(P1, S("P", "1"), "HEAD", "middle", 17, dx=-4, dy=-16)
    sc.label(P2, S("P", "2"), "HEAD", "middle", 17, dx=-4, dy=-16)
    sc.dotp(O, 4)
    sc.label(O, "O", "HEAD", "start", 17, dx=8, dy=20)
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _bar(sc, o, ang=15.0, L=2.0, t=0.12):
    d = _d(ang)
    n = (-d[1], d[0])
    pts = [_add(o, n, -t / 2), _add(_add(o, n, -t / 2), d, L), _add(_add(o, n, t / 2), d, L), _add(o, n, t / 2)]
    sc.poly(pts, "BLUE", 1.8, close=True, fill="BLUE", opacity=0.30)
    return lambda s: _add(o, d, s)


@figure("t7-equivalent-force-systems",
        "Three equivalent load systems on a bar: individual forces, the reduction at A and the reduction at B.",
        r"Three equivalent force systems on a rigid bar. The resultant force is the same; the moment changes with the "
        r"reduction point following Eq. 12.15.")
def equivalent_systems():
    sc = Scene(860, 300, (50, 200), 100)
    W = 2.55
    F = S(bold("F"))
    # left: individual forces
    o1 = (0.0, 0.0)
    pt = _bar(sc, o1)
    p1, p2, p3 = pt(0.0), pt(2.0 / 3), pt(2.0)
    sc.vec(p1, _add(p1, _d(65), 0.85), S(bold("F"), None, "P1"), "GREEN", 3.0, name_off=(-18, -4), size=17, head=11)
    sc.vec(p2, _add(p2, _d(-60), 0.85), S(bold("F"), None, "P2"), "GREEN", 3.0, name_off=(22, 12), size=17, head=11)
    sc.vec(p3, _add(p3, _d(-90), 0.85), S(bold("F"), None, "P3"), "GREEN", 3.0, name_off=(22, 10), size=17, head=11)
    for p in (p1, p2, p3):
        sc.dotp(p, 3.2, "HEAD")
    # middle: reduction at A
    o2 = (W, 0.0)
    pt = _bar(sc, o2)
    A = pt(2.0 / 3)
    sc.vec(A, _add(A, _d(-60), 0.9), bold("F"), "GREEN", 3.0, name_off=(18, 10), size=17, head=11)
    sc.spin(A, 0.30, -10, 255, S(bold("M"), "A"), "GREEN", name_r=0.55)
    sc.dotp(A, 3.4, "HEAD")
    sc.label(A, "A", "HEAD", "middle", 17, dx=-32, dy=40)
    # right: reduction at B
    o3 = (2 * W, 0.0)
    pt = _bar(sc, o3)
    B = pt(2.0)
    sc.vec(B, _add(B, _d(-60), 0.9), bold("F"), "GREEN", 3.0, name_off=(18, 10), size=17, head=11)
    sc.spin(B, 0.44, -10, 255, S(bold("M"), "B"), "GREEN", name_r=0.70)
    sc.dotp(B, 3.4, "HEAD")
    sc.label(B, "B", "HEAD", "middle", 17, dx=-4, dy=-52)
    # equivalence signs and axes
    sc.label((W - 0.30, 0.45), "≡", "TEXT", "middle", 26, italic=False)
    sc.label((2 * W - 0.30, 0.45), "≡", "TEXT", "middle", 26, italic=False)
    axis_out(sc, (-0.25, 1.55), bold("k"), "HEAD", off=(18, 5))
    return sc


# --------------------------------------------------------------------------------------------------------------------
def _box(sc, g, a, b, c, col="#1e3a8a"):
    """Parallelepiped centred at g with edge vectors a, b, c (page vectors); faces +c, +b and -a are visible."""
    def corner(sa, sb, sc_):
        return (g[0] + sa * a[0] / 2 + sb * b[0] / 2 + sc_ * c[0] / 2,
                g[1] + sa * a[1] / 2 + sb * b[1] / 2 + sc_ * c[1] / 2)
    faces = [([corner(-1, -1, 1), corner(1, -1, 1), corner(1, 1, 1), corner(-1, 1, 1)], 0.50),      # top (+c)
             ([corner(-1, 1, 1), corner(1, 1, 1), corner(1, 1, -1), corner(-1, 1, -1)], 0.36),       # front (+b)
             ([corner(-1, -1, 1), corner(-1, 1, 1), corner(-1, 1, -1), corner(-1, -1, -1)], 0.24)]   # end (-a)
    for pts, op in faces:
        sc.poly(pts, col, 1.6, close=True, fill=col, opacity=op)


def _principal_panel(sc, g, dirty, title):
    s = 1.0
    a = _add((0, 0), _d(150), 1.2)
    b = _add((0, 0), _d(225), 0.4)
    c = (0.0, 0.25)
    # fixed axes (grey), longer than the principal axes
    for deg, ln, nm, off in ((225, 1.25, bold("i") + S("", "0"), (-14, 14)), (0, 1.15, bold("j") + S("", "0"), (14, 6)),
                             (90, 1.15, bold("k") + S("", "0"), (-14, 4))):
        sc.vec(g, _add(g, _d(deg), ln), None, "EDGE", 1.3, head=7)
        sc.label(_add(g, _d(deg), ln), nm, "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    _box(sc, g, a, b, c)
    # principal axes
    for deg, ln, nm, off in ((225, 0.85, bold("e") + S("", "1"), (-14, 14)), (90, 0.85, bold("e") + S("", "2"), (14, 0)),
                             (150, 1.0, bold("e") + S("", "3"), (16, -10))):
        sc.vec(g, _add(g, _d(deg), ln), nm, RED, 2.2, name_off=off, size=16, head=9)
    if not dirty:
        sc.vec(g, _add(g, _d(150), 1.6), S(bold("ω"), "B0"), "GREEN", 3.4, name_off=(-26, -8), size=17, head=11)
        sc.vec(g, _add(g, _d(150), 1.2), None, DRED, 2.2, head=9)
        sc.label(_add(g, _d(150), 1.2), S(bold("H"), "G,0"), DRED, "middle", 17, weight="700", dx=-34, dy=26)
    else:
        sc.vec(g, _add(g, _d(160), 1.6), S(bold("ω"), "B0"), "GREEN", 3.4, name_off=(-28, 2), size=17, head=11)
        sc.vec(g, _add(g, _d(175), 1.25), S(bold("H"), "G,0"), DRED, 2.4, name_off=(-30, 8), size=17, head=10)
        sc.arc(g, 1.05, 160, 175, "GREEN", 1.4)
    sc.dotp(g, 4)
    sc.label(g, "G", "HEAD", "middle", 17, dx=14, dy=22)
    sc.label((g[0], g[1] - 1.55), title, "TEXT", "middle", 16, italic=False)


@figure("t7-principal-axes",
        "A block spinning about a principal axis with parallel angular velocity and angular momentum, and spinning off "
        "the axis with the two vectors apart.",
        r"In a clean rotation about a principal axis the angular momentum about $G$ is parallel to the angular velocity; "
        r"off the principal axes it is not, and the Euler equations couple.")
def principal_axes():
    sc = Scene(780, 390, (400, 215), 92)
    _principal_panel(sc, (-2.05, 0.0), False, "clean rotation")
    _principal_panel(sc, (2.05, 0.0), True, "dirty rotation")
    sc.line((0.0, 1.9), (0.0, -1.9), "EDGE", 1.0, "4 4")
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t7-planar-motion",
        "A lamina in plane motion with its body axes turned by theta about the normal axis that points out of the paper.",
        r"Plane motion: the body axes turn by $\theta$ about $\mathbf k_0$, which points out of the paper; the shaded "
        r"triangle gives the components of $\mathbf i_1$ in the fixed basis.")
def planar_motion():
    sc = Scene(640, 470, (60, 410), 150)
    O, G = (0.0, 0.0), (2.0, 1.2)
    TH = 30.0
    th = math.radians(TH)
    pts = []
    for i in range(96):
        f = 2 * math.pi * i / 96
        cx, sx = math.cos(f), math.sin(f)
        x = 1.5 * math.copysign(abs(cx) ** 0.5, cx)
        y = 0.95 * math.copysign(abs(sx) ** 0.5, sx)
        pts.append((G[0] + x * math.cos(th) - y * math.sin(th), G[1] + x * math.sin(th) + y * math.cos(th)))
    triangle(sc, pts, "BLUE", 0.13)
    sc.poly(pts, "BLUE", 1.8, close=True)
    # fixed axes at O
    fixed_axis(sc, O, 0, 1.3, bold("i") + S("", "0"), off=(14, 6))
    fixed_axis(sc, O, 90, 1.3, bold("j") + S("", "0"), off=(14, 4))
    axis_out(sc, O, bold("k") + S("", "0"), off=(-24, -8))
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "start", 17, dx=8, dy=24)
    sc.vec(O, G, None, "HEAD", 2.0, head=9)
    sc.label((1.0, 0.6), S(bold("r"), "0", "G"), "HEAD", "end", 17, dx=-4, dy=-10)
    # dashed parallel through G, triangle of i1
    c, s = math.cos(th), math.sin(th)
    foot = (G[0] + c, G[1])
    tip = (G[0] + c, G[1] + s)
    sc.line((G[0] - 1.05, G[1]), (G[0] + 1.35, G[1]), "EDGE", 1.1, "5 4")
    triangle(sc, [G, foot, tip], "ACC", 0.20)
    sc.dashed(foot, tip)
    right_angle(sc, foot, 180, 90, 0.07)
    sc.label(((G[0] + foot[0]) / 2 + 0.18, G[1]), "cos θ", "TEXT", "middle", 16, dy=22)
    sc.label((foot[0], G[1] + s / 2), "sin θ", "TEXT", "start", 16, dx=9, dy=5)
    unit(sc, G, TH, 1.0, bold("i") + S("", "1"), off=(-6, -14))
    unit(sc, G, TH + 90, 1.0, bold("j") + S("", "1"), off=(-14, -8))
    sc.angle(G, 0.38, 0, TH, "θ", name_r=0.55)
    # k out of the paper at G, rotation rate omega
    axis_out(sc, G, None, "HEAD")
    sc.spin(G, 0.30, 195, 330, "ω", "GREEN", name_r=0.50)
    sc.label(G, "G", "HEAD", "middle", 17, dx=-24, dy=-14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@figure("t7-compound-pendulum",
        "A uniform rod hanging from a pin at its end, turned by theta, with the triangle that locates G and its "
        "free-body diagram.",
        r"Compound pendulum: position of $G$ from the shaded triangle, and the free-body diagram with the weight at $G$ "
        r"and the pin reaction at $O$.")
def compound_pendulum():
    sc = Scene(720, 420, (150, 110), 100)
    TH = 35.0
    t = math.radians(TH)
    L = 3.0
    ui = (math.sin(t), -math.cos(t))          # i1: along the rod
    uj = (math.cos(t), math.sin(t))           # j1: theta + 90 deg
    ang_i1 = -90 + TH

    def rod(o):
        n = uj
        a, b = o, _add(o, ui, L)
        pts = [_add(a, n, -0.05), _add(b, n, -0.05), _add(b, n, 0.05), _add(a, n, 0.05)]
        sc.poly(pts, "BLUE", 1.8, close=True, fill="BLUE", opacity=0.35)

    # ------------------------------------------------ left: deduction
    O = (0.0, 0.0)
    sc.ground((-0.6, 0.16), (0.6, 0.16), side=1)
    sc.line((0.0, 0.16), (0.0, 0.0), "HEAD", 1.8)
    rod(O)
    G = _add(O, ui, L / 2)
    A = _add(O, ui, L)
    foot = (0.0, G[1])
    fixed_axis(sc, O, -90, 2.1, bold("i") + S("", "0"), off=(-4, 20))
    fixed_axis(sc, O, 0, 2.15, bold("j") + S("", "0"), off=(14, 6))
    triangle(sc, [O, foot, G], "ACC", 0.18)
    sc.dashed(G, foot)
    sc.dashed(G, (G[0], 0.0))
    right_angle(sc, foot, 90, 0, 0.08)
    unit(sc, O, ang_i1, 1.0, bold("i") + S("", "1"), off=(18, 6))
    unit(sc, O, ang_i1 + 90, 0.8, bold("j") + S("", "1"), off=(10, -12))
    sc.angle(O, 0.50, -90, ang_i1, "θ", name_r=0.70)
    sc.pin(O, 5)
    sc.dotp(G, 4.5)
    sc.dotp(A, 4.5)
    sc.label(G, "G", "HEAD", "middle", 17, dx=18, dy=14)
    sc.label(A, "A", "HEAD", "middle", 17, dx=16, dy=18)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=-4)
    axis_out(sc, (-0.62, 0.62), bold("k") + S("", "0"), "HEAD", off=(-4, -24))
    sc.label(_add(O, ui, 1.3), "L/2", "HEAD", "end", 16, dx=-12, dy=0)
    sc.label((0.0, G[1] / 2), "(L/2) cos θ", "TEXT", "end", 15, dx=-8, dy=5)
    sc.label((0.0, G[1]), "(L/2) sin θ", "TEXT", "start", 14, dx=5, dy=22)
    sc.note((0.2, -2.95), "deduction", "TEXT", "start", 13)
    # ------------------------------------------------ right: free-body diagram
    X = 3.7
    O2 = (X, 0.0)
    sc.ground((X - 0.6, 0.16), (X + 0.6, 0.16), side=1)
    rod(O2)
    G2 = _add(O2, ui, L / 2)
    sc.pin(O2, 5)
    sc.dotp(G2, 4.5)
    sc.label(G2, "G", "HEAD", "middle", 17, dx=-18, dy=14)
    sc.label(O2, "O", "HEAD", "end", 17, dx=-10, dy=-4)
    sc.label(_add(O2, ui, L), "A", "HEAD", "middle", 17, dx=16, dy=18)
    sc.vec(G2, (G2[0], G2[1] - 1.0), S("m ") + "g", "GREEN", 3.0, name_off=(24, 6), size=17, head=11)
    q = _add(O2, uj, 0.16)
    sc.vec(q, _add(q, ui, 0.95), S(bold("R"), "1"), ORANGE, 3.0, name_off=(22, -6), size=17, head=11)
    sc.vec(O2, _add(O2, uj, 0.95), S(bold("R"), "2"), ORANGE, 3.0, name_off=(18, -8), size=17, head=11)
    sc.note((X - 0.6, -2.95), "free-body diagram", "TEXT", "start", 13)
    return sc
