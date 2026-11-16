"""Problem RB-28: Euler's disk, a coin rolling on a horizontal plane (angles psi, beta, theta, delta)."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d, rotation_view
from figures.em_sol.rb12 import plane_rotation
from figures.em_sol.rb23 import circle_pts, rim_hatch, tri_pair
from figures.mech import S, Scene, bold, dot1
from figures.svgkit import arrow_head

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I0, J0, K0 = S(I, "0"), S(J, "0"), S(K, "0")
I1, J1, K1 = S(I, "1"), S(J, "1"), S(K, "1")
X2, Y2 = S(bold("x"), "2"), S(bold("y"), "2")
X3, Z3 = S(bold("x"), "3"), S(bold("z"), "3")
Y4, Z4 = S(bold("y"), "4"), S(bold("z"), "4")


# ------------------------------------------------------------------------------------------------ rb28-rot-psi
@figure("rb28-rot-psi",
        "Polar coordinates r and psi of the contact point and the polar basis i1, j1 at C.",
        r"Rotation about $\mathbf k_0$ (⊙) by $\psi$. The frame $S_1$ is attached to the contact point: $\mathbf i_1$ along "
        r"$OC$ and $\mathbf j_1$ normal to it.")
def rot_psi():
    psi, r = 35.0, 3.0
    sc = Scene(900, 740, (150, 660), 175)
    O = (0.0, 0.0)
    C = (r * math.cos(math.radians(psi)), r * math.sin(math.radians(psi)))
    fixed_axis(sc, O, 0, 4.0, I0, off=(16, 6))
    fixed_axis(sc, O, 90, 3.3, J0, off=(16, 4))
    sc.line(O, C, "HEAD", 3.0)
    sc.label(add(O, d(psi), r / 2), "r", "TEXT", "middle", 17, dx=12, dy=22)
    tri_pair(sc, C, 0, psi, I1, J1, "ψ", col="BLUE", arcs=False, off1=(18, -8), off2=(-10, -14))
    # psi arc at O
    sc.arc(O, 1.0, 0, psi, "GREEN", 1.8, head=True)
    sc.label(add(O, d(psi / 2), 1.0), "ψ", "GREEN", "middle", 17, dx=16, dy=-6)
    # leg labels at C
    c, s = math.cos(math.radians(psi)), math.sin(math.radians(psi))
    sc.label((C[0] + c / 2, C[1]), "cos ψ", "TEXT", "middle", 14, dy=22)
    sc.label((C[0] + c, C[1] + s / 2), "sin ψ", "TEXT", "start", 14, dx=8, dy=5)
    sc.label((C[0], C[1] + c / 2), "cos ψ", "TEXT", "start", 14, dx=8, dy=-14)
    sc.label((C[0] - s / 2, C[1] + c), "sin ψ", "TEXT", "middle", 14, dy=-8)
    sc.label(add(C, d(psi), 0.5), "1", "TEXT", "middle", 14, dx=-4, dy=18)
    sc.label(add(C, d(psi + 90), 0.5), "1", "TEXT", "middle", 14, dx=-12, dy=0)
    sc.mass(C, None, r=5, col="ACC")
    sc.label(C, "C", "HEAD", "middle", 17, dx=-14, dy=22)
    axis_out(sc, O, None, "HEAD")
    sc.label(O, "O", "HEAD", "middle", 17, dx=-14, dy=24)
    sc.label(O, K0 + " (⊙)", "HEAD", "end", 16, weight="700", dx=-14, dy=-14)
    return sc


# ------------------------------------------------------------------------------------------------ rb28-rot-beta
@figure("rb28-rot-beta",
        "Heading of the coin: the tangent y2 of the rim at C turned by beta from j1.",
        r"Rotation about $\mathbf k_1$ (⊙) by $\beta$. The horizontal tangent of the rim at $C$ is $\mathbf y_2$; "
        r"$\Lambda$, the rate of $\psi$ plus the rate of $\beta$, is the turning rate of the coin about the vertical.")
def rot_beta():
    ang = 25.0
    jb = d(ang + 90)

    def pre(sc):
        # trace of the coin on the plane: thick grey segment through C along y2
        sc.line(add((0.0, 0.0), jb, -1.9), add((0.0, 0.0), jb, 1.95), "EDGE", 6.0)

    def post(sc):
        sc.mass((0.0, 0.0), None, r=4.5, col="ACC")
        sc.label((0.0, 0.0), "C", "HEAD", "middle", 17, dx=14, dy=22)
        sc.label(add((0.0, 0.0), jb, -1.9), "tangent of the rim (coin seen from above)", "TEXT", "start", 14, dx=16, dy=6)
        sc.label(jb, Y2, "BLUE", "end", 17, weight="700", dx=-20, dy=-2)
    return plane_rotation(900, 720, (420, 360), 150, ang, (I1, J1, X2, ""), K1 + " (⊙)", ("β", ""), None,
                          extra_pre=pre, extra_post=post, out_off=(-44, 22))


# ------------------------------------------------------------------------------------------------ rb28-rot-theta
THETA, R = 30.0, 2.0
TR = math.radians(THETA)
Z3D = (-math.sin(TR), math.cos(TR))
X3D = (math.cos(TR), math.sin(TR))


def _plane_line(sc, x0, x1, gap=None):
    """The plane through C, edge-on: a solid line with hatching below, except in the middle (gap) where labels sit."""
    if gap is None:
        sc.ground((x0, 0.0), (x1, 0.0), -1)
    else:
        sc.ground((x0, 0.0), (gap[0], 0.0), -1)
        sc.line((gap[0], 0.0), (gap[1], 0.0), "HEAD", 2.4)
        sc.ground((gap[1], 0.0), (x1, 0.0), -1)


def _coin_edge(sc, w=8.0):
    sc.line((0.0, 0.0), add((0.0, 0.0), Z3D, 2 * R), "EDGE", w)


@figure("rb28-rot-theta",
        "Edge-on view of the coin tilted by theta, with z3 along CG and the normal x3.",
        r"Rotation by $\theta$ about $-\mathbf y_2$ (⊙). The coin leans towards $-\mathbf x_2$; $G$ is at the height "
        r"$R\cos\theta$ and at $R\sin\theta$ behind $C$.")
def rot_theta():
    G = add((0.0, 0.0), Z3D, R)
    F = (G[0], 0.0)

    def pre(sc):
        _plane_line(sc, -2.5, 3.3, (-1.2, 2.1))
        _coin_edge(sc)
        # triangle C, G, foot of G on the plane (hypotenuse R)
        triangle(sc, [(0.0, 0.0), F, G], ORANGE, 0.10)
        sc.dashed(F, G)
        right_angle(sc, F, 90, 0, 0.12)

    def post(sc):
        sc.mass(G, None, r=4.5, col="BLUE")
        sc.label(G, "G", "HEAD", "middle", 17, dx=-16, dy=-4)
        sc.label((0.0, 0.0), "C", "HEAD", "middle", 17, dx=-22, dy=24)
        sc.label(add((0.0, 0.0), Z3D, 1.0), Z3, "BLUE", "end", 17, weight="700", dx=-24, dy=12)
        sc.label((F[0] / 2, F[1]), "R sin θ", "TEXT", "middle", 15, dy=-8)
        sc.label((F[0], G[1] / 2), "R cos θ", "TEXT", "end", 15, dx=-8, dy=5)
        sc.label(add((0.0, 0.0), Z3D, R * 0.78), "R", "TEXT", "start", 16, dx=14, dy=-2)
        sc.note((0.9, 2.0), "⊙ : minus " + Y2, "TEXT", "start", 14)
    sc = rotation_view(900, 820, (400, 600), 125, THETA, X2, K1, X3, "", Y2 + " (⊗)", ("θ", ""), pre=pre, post=post,
                       out_kind="in", out_off=(-6, 54))
    return sc


# ------------------------------------------------------------------------------------------------ rb28-rot-delta
@figure("rb28-rot-delta",
        "The coin seen face-on, spinning by delta about its normal x3.",
        r"Rotation about the normal $\mathbf x_3$ (⊙) by $\delta$. The contact point $C$ is always the lowest point of the "
        r"rim, at $-R\,\mathbf z_3$, whatever $\delta$.")
def rot_delta():
    ang = 30.0

    def pre(sc):
        sc.poly(circle_pts((0.0, 0.0), R), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.08)
        z4 = d(ang + 90)
        pm = add((0.0, 0.0), z4, -R)
        sc.line((0.0, 0.0), pm, "HEAD", 1.6)

    def post(sc):
        z4 = d(ang + 90)
        pm = add((0.0, 0.0), z4, -R)
        sc.mass(pm, None, r=4.5, col="ACC")
        sc.label(pm, "mark", "HEAD", "start", 15, dx=10, dy=14)
        sc.mass((0.0, -R), None, r=4.5, col="BLUE")
        sc.label((0.0, -R), "C", "HEAD", "middle", 17, dx=-16, dy=22)
        sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=14, dy=22)
        sc.label(add((0.0, 0.0), d(-60), R * 0.55), "R", "TEXT", "start", 16, dx=0, dy=-4)
    return plane_rotation(840, 780, (420, 370), 140, ang, (Y2, Z3, Y4, Z4), X3 + " (⊙)", ("δ", ""), None,
                          extra_pre=pre, extra_post=post, out_off=(-44, 22))


# ------------------------------------------------------------------------------------------------ rb28-fbd
@figure("rb28-fbd",
        "Free-body diagram of the coin: weight at G and the contact force with its normal and two friction components at C.",
        r"Free-body diagram. The contact force acts at $C$ on the diameter through $G$: its moment about $G$ has no "
        r"component along $\mathbf z_3$.")
def fbd():
    sc = Scene(860, 760, (400, 590), 125)
    O = (0.0, 0.0)
    G = add(O, Z3D, R)
    _plane_line(sc, -2.6, 3.0)
    _coin_edge(sc)
    # arm from G to C, offset to the right of the coin (the line carries nothing else)
    off = 0.45
    a, b = add(G, X3D, off), add(O, X3D, off)
    sc.dim(a, b, "R", off=(26, 4))
    sc.dashed(G, add(G, X3D, off + 0.1))
    sc.dashed(O, add(O, X3D, off + 0.1))
    # basis at G
    sc.vec(G, add(G, Z3D, 0.9), Z3, "BLUE", 2.4, name_off=(-14, -4), size=16, head=10)
    sc.vec(G, add(G, X3D, 0.9), X3, "BLUE", 2.4, name_off=(16, -6), size=16, head=10)
    # forces
    sc.vec(G, (G[0], G[1] - 1.1), None, "PINK", 3.2, head=12)
    sc.label((G[0], G[1] - 1.1), "mg", "PINK", "start", 17, weight="700", dx=-30, dy=22)
    sc.vec(O, (0.0, 0.8), None, "GREEN", 3.2, head=12)
    sc.label((0.0, 0.8), "N", "GREEN", "start", 17, weight="700", dx=-24, dy=8)
    sc.vec(O, (1.6, 0.0), None, "GREEN", 3.2, head=12)
    sc.label((1.6, 0.0), S("F", "x"), "GREEN", "start", 17, weight="700", dx=6, dy=-8)
    # F_y: into the paper, a cross in a circle
    x, y = sc.P(O)
    sc.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="12" fill="none" stroke="GREEN" stroke-width="2.4"/>')
    sc.c.add(f'<path d="M{x - 7.5:.1f},{y - 7.5:.1f} L{x + 7.5:.1f},{y + 7.5:.1f} M{x - 7.5:.1f},{y + 7.5:.1f} L{x + 7.5:.1f},{y - 7.5:.1f}" '
             f'stroke="GREEN" stroke-width="2.2" fill="none"/>')
    sc.label(O, S("F", "y") + " (into the paper)", "GREEN", "start", 16, weight="700", dx=18, dy=36)
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=-16, dy=-4)
    sc.label(O, "C", "HEAD", "middle", 17, dx=-20, dy=22)
    return sc


# ------------------------------------------------------------------------------------------------ rb28-steady
SY = 0.40           # foreshortening of the horizontal depth axis in the oblique view


def _p3(x, y, z):
    """Oblique projection: x to the right, z up, the horizontal depth y drawn upwards on the screen with factor SY."""
    return (x, z + SY * y)


def _line3(sc, a, b, col="HEAD", w=1.6, dash=None):
    sc.line(_p3(*a), _p3(*b), col, w, dash)


def _ring3(c, u, v, r, t0=0.0, t1=360.0, n=96):
    pts = []
    for i in range(n + 1):
        t = math.radians(t0 + (t1 - t0) * i / n)
        q = tuple(c[m] + r * (math.cos(t) * u[m] + math.sin(t) * v[m]) for m in range(3))
        pts.append(_p3(*q))
    return pts


@figure("rb28-steady",
        "Steady motion of Euler's disk: G at rest above O, the contact point circling O.",
        r"Part (f). $G$ stays at the height $h$ above $O$; the contact point runs on the circle of radius $r$, and the "
        r"angular velocity lies along $CG$. Weight and normal reaction form a couple that turns the angular momentum "
        r"about the vertical.")
def steady():
    Rr, h = 2.0, 0.9
    r = math.sqrt(Rr * Rr - h * h)
    th = math.degrees(math.acos(h / Rr))
    psi = math.radians(-35.0)
    sc = Scene(900, 600, (450, 405), 118)
    O = (0.0, 0.0, 0.0)
    C = (r * math.cos(psi), r * math.sin(psi), 0.0)
    G = (0.0, 0.0, h)
    rad = (math.cos(psi), math.sin(psi), 0.0)            # radial unit vector i1
    tan = (-math.sin(psi), math.cos(psi), 0.0)           # tangent y2
    # plane: a light grey ellipse
    sc.poly(_ring3(O, (1, 0, 0), (0, 1, 0), 3.1), "EDGE", 1.4, fill="EDGE", close=True, opacity=0.10)
    # circle traced by C
    sc.poly(_ring3(O, (1, 0, 0), (0, 1, 0), r), "HEAD", 1.4, "6 5")
    # coin: disc through C and G, with the horizontal tangent y2
    u = tuple((G[m] - C[m]) / Rr for m in range(3))
    centre = G
    sc.poly(_ring3(centre, u, tan, Rr), "HEAD", 2.0, fill="EDGE", close=True, opacity=0.22)
    # vertical axis and the triangle O, C, G
    _line3(sc, O, (0, 0, 2.75), "EDGE", 1.4)
    sc.vec(_p3(0, 0, 2.4), _p3(0, 0, 2.75), None, "EDGE", 1.4, head=8)
    sc.label(_p3(0, 0, 2.75), K0, "TEXT", "middle", 16, weight="700", dx=14, dy=4)
    sc.poly([_p3(*O), _p3(*C), _p3(*G)], "ACC", 0.0, fill="ACC", close=True, opacity=0.20)
    _line3(sc, O, C, "HEAD", 1.6)
    _line3(sc, C, (C[0], C[1], 1.7), "EDGE", 1.1, "5 4")
    # angular velocity along CG
    tip = tuple(C[m] + 1.38 * (G[m] - C[m]) for m in range(3))
    sc.vec(_p3(*C), _p3(*tip), None, "ACC", 3.4, head=13)
    sc.label(_p3(*tip), "ω", "ACC", "start", 18, weight="700", dx=10, dy=-4)
    # normal reaction and weight
    sc.vec(_p3(*C), _p3(C[0], C[1], 1.15), None, "GREEN", 3.2, head=12)
    sc.label(_p3(C[0], C[1], 1.15), "N", "GREEN", "start", 17, weight="700", dx=8, dy=0)
    sc.vec(_p3(*G), _p3(0, 0, h - 0.55), None, "PINK", 3.2, head=12)
    sc.label(_p3(0, 0, h - 0.55), "mg", "PINK", "end", 17, weight="700", dx=-8, dy=10)
    # theta at C between the vertical and CG
    inw = tuple(-m for m in rad)
    arc = _ring3(C, (0, 0, 1), inw, 0.62, 0.0, th)
    sc.poly([(arc[i][0], arc[i][1]) for i in range(len(arc))], "GREEN", 1.8)
    mid = _ring3(C, (0, 0, 1), inw, 0.80, th / 2, th / 2, 1)[0]
    sc.label(mid, "θ", "GREEN", "middle", 17, dx=-10, dy=-2)
    # direction of increasing psi: arrow on the dashed circle
    t0 = math.radians(-95.0)
    sc.poly([_p3(r * math.cos(t0 - 0.30 + 0.30 * i / 8), r * math.sin(t0 - 0.30 + 0.30 * i / 8), 0.0) for i in range(9)],
            "GREEN", 2.4)
    pa = _p3(r * math.cos(t0), r * math.sin(t0), 0.0)
    pb = _p3(r * math.cos(t0 + 0.12), r * math.sin(t0 + 0.12), 0.0)
    arrow_head(sc.c, sc.P(*pa), sc.P(*pb), "GREEN", 11)
    sc.label(_p3(r * math.cos(t0 + 0.12), r * math.sin(t0 + 0.12), 0.0), dot1("ψ"), "GREEN", "start", 17, weight="700",
             dx=10, dy=22)
    # labels of the triangle
    sc.label(_p3(C[0] / 2, C[1] / 2, 0), "r", "TEXT", "middle", 17, dx=-4, dy=22)
    sc.label(_p3(0, 0, h * 0.4), "h", "TEXT", "start", 17, dx=10, dy=6)
    mid = tuple((C[m] + G[m]) / 2 for m in range(3))
    sc.label(_p3(*mid), "R", "TEXT", "start", 17, dx=10, dy=14)
    # points
    for pt, nm, off in ((O, "O", (-14, 22)), (G, "G", (-14, -8)), (C, "C", (-12, 24))):
        sc.mass(_p3(*pt), None, r=4.5, col="BLUE")
        sc.label(_p3(*pt), nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    return sc
