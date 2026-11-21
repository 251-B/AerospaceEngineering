"""Theory figures of Topic 7 (Momentum, Kinetic Energy and Rigid Body Dynamics)."""
import math

from figures.em_theory import axis_out, figure, fixed_axis, raster, right_angle, triangle, unit
from figures.mech import S, Scene, bold

RED = "#ef4444"          # principal axes e1, e2, e3
DRED = "#be123c"         # angular momentum H_G
ORANGE = "ACC"


def _d(deg):
    return math.cos(math.radians(deg)), math.sin(math.radians(deg))


def _add(p, q, k=1.0):
    return (p[0] + k * q[0], p[1] + k * q[1])


# --------------------------------------------------------------------------------------------------------------------
raster("t7-material-system",
       "A rigid body with its centre of mass G, a material element P and a generic point A, with the position vectors from O, A and G.",
       r"Material system $B$ moving in the fixed frame $S_0$. The frames $S_A$ and $S_G$ have origins at $A$ and $G$ and axes parallel to $S_0$, so they translate without rotating. Copied from Notes.pdf, Fig. 11.1, p. 90", 460)


# --------------------------------------------------------------------------------------------------------------------
raster("t7-internal-external-forces",
       "Particles of a material system acted on by external forces and by equal and opposite collinear internal forces.",
       r"External forces come from the environment; internal forces act in equal, opposite and collinear pairs, so their resultant and their moment about any point vanish. Copied from Notes.pdf, Fig. 12.1, p. 94", 480)


# --------------------------------------------------------------------------------------------------------------------
# INVIABLE: the slide sketch sits under an equation; no clean crop
@figure("t7-spring-pair",
        "Two particles joined by a spring of stiffness k, with their position vectors and the pair of spring forces.",
        r"The spring forces derive from one potential energy of the pair; that term appears once in the energy equation.")
def spring_pair():
    sc = Scene(560, 450, (230, 380), 150)
    O = (2.0, 0.0)
    P1, P2 = (0.0, 0.3), (1.6, 1.8)
    for dv, nm, ln, off in (((-0.789, -0.614), bold("x") + S("", "0"), 1.05, (-14, 14)),
                            ((1.0, 0.0), bold("y") + S("", "0"), 1.5, (10, 18)),
                            ((0.0, 1.0), bold("z") + S("", "0"), 2.2, (10, 2))):
        sc.vec(O, _add(O, dv, ln), None, "HEAD", 2.6, head=10)
        sc.label(_add(O, dv, ln), nm, "HEAD", "middle", 17, weight="700", dx=off[0], dy=off[1])
    sc.vec(O, P1, None, "EDGE", 1.4, head=8)
    sc.vec(O, P2, None, "EDGE", 1.4, head=8)
    sc.label((1.0, 0.12), S(bold("r"), "0", "P1"), "TEXT", "middle", 16, dy=-6)
    sc.label((1.80, 1.0), S(bold("r"), "0", "P2"), "TEXT", "start", 16, dx=4, dy=0)
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
# --------------------------------------------------------------------------------------------------------------------
raster("t7-equivalent-force-systems",
       "Three equivalent load systems on a bar: individual forces, the reduction at A and the reduction at B.",
       r"Three equivalent force systems on a rigid bar. The resultant force is the same; the moment changes with the reduction point following Eq. 12.15. Copied from Notes.pdf, Fig. 12.2, p. 98", 760)


# --------------------------------------------------------------------------------------------------------------------
def _box(sc, g, a, b, c, col="#1e3a8a"):
    """Parallelepiped centred at g with edge vectors a, b, c (page vectors); faces +c, +b and -a are visible."""
    def corner(sa, sb, sc_):
        return (g[0] + sa * a[0] / 2 + sb * b[0] / 2 + sc_ * c[0] / 2,
                g[1] + sa * a[1] / 2 + sb * b[1] / 2 + sc_ * c[1] / 2)
    faces = [([corner(-1, -1, 1), corner(1, -1, 1), corner(1, 1, 1), corner(-1, 1, 1)], 0.95),      # top (+c)
             ([corner(-1, 1, 1), corner(1, 1, 1), corner(1, 1, -1), corner(-1, 1, -1)], 0.80),       # front (+b)
             ([corner(-1, -1, 1), corner(-1, 1, 1), corner(-1, 1, -1), corner(-1, -1, -1)], 0.62)]   # end (-a)
    for pts, op in faces:
        sc.poly(pts, "#bfdbfe", 1.4, close=True, fill=col, opacity=op)


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
                             (150, 1.0, bold("e") + S("", "3"), (-16, -6))):
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


# --------------------------------------------------------------------------------------------------------------------
# EXTRA: deduction, free-body or per-rotation figure, not printed in the official material
@figure("t7-principal-axes",
        "A block spinning about a principal axis with parallel angular velocity and angular momentum, and spinning off "
        "the axis with the two vectors apart.",
        r"In a clean rotation about a principal axis the angular momentum about $G$ is parallel to the angular velocity; "
        r"off the principal axes it is not, and the Euler equations couple.")
def principal_axes():
    sc = Scene(780, 430, (400, 250), 92)
    _principal_panel(sc, (-2.05, 0.0), False, "clean rotation")
    _principal_panel(sc, (2.05, 0.0), True, "dirty rotation")
    sc.line((0.0, 1.9), (0.0, -1.9), "EDGE", 1.0, "4 4")
    return sc


# --------------------------------------------------------------------------------------------------------------------
# EXTRA: deduction, free-body or per-rotation figure, not printed in the official material
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
    axis_out(sc, O, bold("k") + S("", "0"), off=(-18, 4))
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=22)
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
# EXTRA: deduction, free-body or per-rotation figure, not printed in the official material
@figure("t7-compound-pendulum",
        "A uniform rod hanging from a pin at its end, turned by theta, with the triangle that locates G and its "
        "free-body diagram.",
        r"Compound pendulum: position of $G$ from the shaded triangle, and the free-body diagram with the weight at $G$ "
        r"and the pin reaction at $O$.")
def compound_pendulum():
    sc = Scene(720, 480, (150, 90), 100)
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
    unit(sc, O, ang_i1, 0.95, bold("i") + S("", "1"), off=(16, 10))
    unit(sc, O, ang_i1 + 90, 0.8, bold("j") + S("", "1"), off=(10, -12))
    sc.angle(O, 0.50, -90, ang_i1, "θ", name_r=0.70)
    sc.pin(O, 5)
    sc.dotp(G, 4.5)
    sc.dotp(A, 4.5)
    sc.label(G, "G", "HEAD", "middle", 17, dx=18, dy=14)
    sc.label(A, "A", "HEAD", "middle", 17, dx=16, dy=18)
    sc.label(O, "O", "HEAD", "end", 17, dx=-10, dy=-4)
    axis_out(sc, (-0.62, 0.62), bold("k") + S("", "0"), "HEAD", off=(-4, -24))
    sc.label((G[0] / 2, G[1] / 2), "L/2", "HEAD", "start", 16, dx=12, dy=-6)
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
