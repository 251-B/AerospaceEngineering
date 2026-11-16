"""Problem RB-15: thin hemispherical shell rocking on a smooth horizontal plane (Euler angles psi, theta, phi)."""
import math

from figures.em_solutions import axis_out, figure, right_angle, triangle
from figures.em_sol.rb01 import add, arrow_px, d, p3, p3v, ring, sub
from figures.em_sol.rb12 import ground_line, half_disc_points, plane_rotation
from figures.mech import S, Scene, bold

ORANGE = "ACC"
A = 3.0
TH = 35.0
TR = math.radians(TH)


def _vname(sym, sup=None, sb=None):
    return S(bold(sym), sb, sup) if (sb or sup) else bold(sym)


K1 = S(bold("k"), "1")
I1, J1 = S(bold("i"), "1"), S(bold("j"), "1")
JP = bold("j") + "′"


@figure("rb15-rot-psi",
        "Precession: the horizontal axis Gx turned by psi from O1x1 about the vertical.",
        r"Precession about $\mathbf k_1$ (⊙) by $\psi$; $\mathbf i$ is the horizontal axis $Gx$ of the statement.")
def rot_psi():
    ang = 35.0

    def post(sc):
        tip = (math.cos(math.radians(ang)), math.sin(math.radians(ang)))
        sc.note(tip, "Gx (line of nodes, horizontal)", "TEXT", "start", 13, dx=-30, dy=-40)
        sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=14, dy=26)
    return plane_rotation(760, 600, (270, 490), 250, ang, (I1, J1, bold("i"), JP),
                          K1 + " (⊙)", ("ψ", ""), None, extra_post=post, out_off=(-16, 28))


@figure("rb15-rot-theta",
        "Nutation: the axis of revolution Gz tilted by theta from the vertical about the horizontal axis Gx.",
        r"Nutation about $\mathbf i$ (⊙) by $\theta$. The tip of $\mathbf k_1$ moves towards negative $\mathbf j'$, which "
        r"gives the minus sign in $\mathbf k = -\sin\theta\,\mathbf j' + \cos\theta\,\mathbf k_1$.")
def rot_theta():
    ang = 35.0

    def post(sc):
        tip = (-math.sin(math.radians(ang)), math.cos(math.radians(ang)))
        sc.note(tip, "Gz (axis of revolution, towards the rim)", "TEXT", "middle", 13, dx=0, dy=-40)
        sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=14, dy=26)
    return plane_rotation(800, 600, (340, 490), 250, ang, (JP, K1, bold("j"), bold("k")),
                          bold("i") + " (⊙)", ("θ", ""), None, extra_post=post, out_off=(-16, 28))


@figure("rb15-rot-phi",
        "Spin: the body axes turned by phi about the axis of revolution.",
        r"Spin about $\mathbf k$ (⊙) by $\varphi$. The frame $Gxyz$ does not follow this rotation; the axisymmetric "
        r"tensor keeps the same components in both bases.")
def rot_phi():
    def post(sc):
        sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=14, dy=26)
    sc = plane_rotation(760, 600, (270, 490), 250, 50.0,
                        (bold("i"), bold("j"), S(bold("i"), "b"), S(bold("j"), "b")),
                        bold("k") + " (⊙)", ("φ", ""), None, extra_post=post, out_off=(-16, 28), col="GREEN")
    return sc


# ------------------------------------------------------------------------------------------------ meridian section
O = (0.0, A)
KDIR = (-math.sin(TR), math.cos(TR))           # k, from the pole towards the rim, in the (j', k1) plane
TDIR = (math.cos(TR), math.sin(TR))            # rim direction (j)
G = (O[0] - A / 2 * KDIR[0], O[1] - A / 2 * KDIR[1])
POLE = (O[0] - A * KDIR[0], O[1] - A * KDIR[1])
P = (0.0, 0.0)


def _shell(sc, faint=False):
    pts = [(O[0] + A * (math.cos(math.radians(t)) * TDIR[0] - math.sin(math.radians(t)) * KDIR[0]),
            O[1] + A * (math.cos(math.radians(t)) * TDIR[1] - math.sin(math.radians(t)) * KDIR[1])) for t in range(0, 181, 2)]
    sc.poly(pts, "HEAD", 3.0, fill="EDGE", close=True, opacity=0.10)
    ground_line(sc, -3.7, 3.9)
    sc.line(add(O, TDIR, -A), add(O, TDIR, A), "EDGE", 1.3, "5 4")


def _scene():
    return Scene(800, 540, (280, 460), 72)


@figure("rb15-meridian",
        "Meridian section of the tilted hemispherical shell with its centre O at height a above the contact point and G "
        "halfway between O and the pole.",
        r"Meridian section. $O$ stays at the height $a$ above the contact point $P$; $G$ is at $a/2$ from $O$ along "
        r"$-\mathbf k$, so its height is $a - \tfrac a2\cos\theta$.")
def meridian():
    sc = _scene()
    _shell(sc)
    foot = (0.0, G[1])
    triangle(sc, [O, foot, G], ORANGE, 0.30)
    # axes: grey k1 and j', dashed vertical OP
    sc.vec(O, (0.0, A + 2.25), None, "EDGE", 1.4, head=8)
    sc.label((0.0, A + 2.25), K1, "TEXT", "middle", 16, weight="700", dx=-14, dy=-2)
    sc.vec(O, (1.15, A), None, "EDGE", 1.4, head=8)
    sc.label((1.15, A), JP, "TEXT", "start", 16, weight="700", dx=6, dy=18)
    sc.dashed(O, P)
    sc.label((0.0, A / 2 - 0.5), "a", "TEXT", "start", 16, dx=9, dy=5)
    sc.dashed(G, P)
    sc.dashed(foot, G)
    right_angle(sc, foot, 90, 0, 0.08)
    sc.label((0.0, foot[1] + 0.22), "(a/2) cos θ", "TEXT", "end", 14, dx=-9, dy=5)
    sc.label(G, "(a/2) sin θ", "TEXT", "start", 14, dx=12, dy=-8)
    # axis of revolution and k
    sc.line(add(POLE, KDIR, -0.05), add(O, KDIR, 1.2), "EDGE", 1.2, "7 4")
    sc.vec(G, add(G, KDIR, 2.15), bold("k"), "BLUE", 3.0, name_off=(-14, -6), size=17, head=12)
    sc.label(((O[0] + G[0]) / 2, (O[1] + G[1]) / 2), "a/2", "TEXT", "start", 14, dx=12, dy=-2)
    sc.arc(O, 0.75, 90, 90 + TH, "GREEN", 1.8, head=True)
    sc.label(add(O, d(90 + TH / 2), 1.05), "θ", "GREEN", "middle", 17, dx=-6, dy=-2)
    # height of G
    xd = 3.45
    sc.dim((xd, 0.0), (xd, G[1]), "", off=(0, 0))
    sc.dashed(G, (xd + 0.1, G[1]))
    sc.label((xd, G[1] / 2), S("z", "G") + " = a − (a/2) cos θ", "TEXT", "start", 14, dx=10, dy=5)
    # points
    for pt, nm, off in ((O, "O", (-12, 4)), (G, "G", (-18, 20)), (POLE, "pole", (26, 22)), (P, "P", (-4, 26))):
        sc.mass(pt, None, r=4.5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.note(add(O, TDIR, A), "rim", "TEXT", "start", 13, dx=8, dy=-4)
    axis_out(sc, (-2.85, 5.25), None, "HEAD")
    sc.label((-2.85, 5.25), bold("i") + " (out of the paper)", "HEAD", "start", 16, dx=16, dy=5)
    return sc


# ------------------------------------------------------------------------------------------------ shell element (3D)
def _hemi(a, beta, alpha):
    b, al = math.radians(beta), math.radians(alpha)
    return (a * math.sin(b) * math.cos(al), a * math.sin(b) * math.sin(al), -a * math.cos(b))


def _hull(points):
    pts = sorted(set(points))
    def cr(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for p in pts:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up) >= 2 and cr(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


@figure("rb15-shell-element",
        "Spherical surface element of the hemispherical shell and the position of its centre of mass.",
        r"Surface element $a^2\sin\beta\,d\beta\,d\alpha$ of the shell. Every point is at the distance $a$ from $O$, "
        r"which gives the isotropic tensor $\tfrac23 ma^2[U]$ about $O$; $G$ lies at $a/2$ below $O$.")
def shell_element():
    sc = Scene(860, 500, (330, 190), 70)
    BETA, ALPHA = 55.0, 40.0
    ex, ey, ez = (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)
    O3 = (0.0, 0.0, 0.0)
    # silhouette of the lower hemisphere: convex hull of its projected points
    cloud = [p3v(_hemi(A, b, a)) for b in range(0, 91, 3) for a in range(0, 360, 5)]
    sc.poly(_hull(cloud), "EDGE", 0.0, fill="EDGE", close=True, opacity=0.14)
    sc.poly(_hull(cloud), "HEAD", 2.0, close=True)
    # parallels and meridians
    for b in (30, 60):
        sc.poly([p3v(_hemi(A, b, a)) for a in range(0, 361, 6)], "EDGE", 0.9, "3 4")
    for a in (0, 90, 180, 270):
        sc.poly([p3v(_hemi(A, b, a)) for b in range(0, 91, 3)], "EDGE", 0.9, "3 4")
    sc.poly(ring(O3, ex, ey, A), "HEAD", 1.6, close=True)
    # axes
    sc.line(p3v(O3), p3v((0.0, 0.0, -A - 0.25)), "EDGE", 1.2, "7 4")
    sc.vec(p3v(O3), p3v((0.0, 0.0, 1.35)), bold("k"), "BLUE", 2.8, name_off=(-14, -2), size=17, head=11)
    sc.vec(p3v(O3), p3v((1.45, 0.0, 0.0)), S(bold("i"), "b"), "BLUE", 2.8, name_off=(-14, 14), size=17, head=11)
    sc.vec(p3v(O3), p3v((0.0, 1.45, 0.0)), S(bold("j"), "b"), "BLUE", 2.8, name_off=(14, 8), size=17, head=11)
    # arc of alpha in the rim plane
    sc.poly(ring(O3, ex, ey, 1.05, 0, ALPHA, 20), "GREEN", 1.8)
    arrow_px(sc, ring(O3, ex, ey, 1.05, 0, ALPHA, 20)[-3], ring(O3, ex, ey, 1.05, 0, ALPHA, 20)[-1], "GREEN", 9)
    ua = (math.cos(math.radians(ALPHA)), math.sin(math.radians(ALPHA)), 0.0)
    sc.dashed(p3v(O3), p3v((A * ua[0], A * ua[1], 0.0)))
    sc.label(p3v((1.5 * math.cos(math.radians(ALPHA / 2)), 1.5 * math.sin(math.radians(ALPHA / 2)), 0.0)), "α", "GREEN",
             "middle", 17, dx=8, dy=16)
    # arc of beta in the meridian plane of the element, from the pole axis
    pts = [p3v((2.2 * math.sin(math.radians(t)) * ua[0], 2.2 * math.sin(math.radians(t)) * ua[1],
                -2.2 * math.cos(math.radians(t)))) for t in [BETA * i / 20 for i in range(21)]]
    sc.poly(pts, "GREEN", 1.8)
    arrow_px(sc, pts[-3], pts[-1], "GREEN", 9)
    sc.label(p3v((2.55 * math.sin(math.radians(BETA / 2)) * ua[0], 2.55 * math.sin(math.radians(BETA / 2)) * ua[1],
                  -2.55 * math.cos(math.radians(BETA / 2)))), "β", "GREEN", "middle", 17, dx=-10, dy=10)
    # element and its radius
    pe = _hemi(A, BETA, ALPHA)
    sc.dashed(p3v(O3), p3v(pe))
    patch = ([p3v(_hemi(A, b, ALPHA - 5)) for b in (BETA - 4, BETA + 4)] +
             [p3v(_hemi(A, BETA + 4, a)) for a in (ALPHA - 5, ALPHA + 5)] +
             [p3v(_hemi(A, b, ALPHA + 5)) for b in (BETA + 4, BETA - 4)] +
             [p3v(_hemi(A, BETA - 4, a)) for a in (ALPHA + 5, ALPHA - 5)])
    sc.poly(patch, "ACC", 1.6, fill="ACC", close=True, opacity=0.65)
    mid = p3v(_hemi(A * 0.5, BETA, ALPHA))
    sc.label(mid, "a", "TEXT", "middle", 16, dx=14, dy=-4)
    lp = p3v(pe)
    sc.line(lp, (lp[0] + 1.55, lp[1] - 0.75), "ACC", 1.2)
    sc.label((lp[0] + 1.6, lp[1] - 0.75), "dA = a² sin β dβ dα", "ACC", "start", 16, weight="700", dx=6, dy=5)
    # G and O
    Gp = (0.0, 0.0, -A / 2)
    sc.mass(p3v(Gp), None, r=5, col="BLUE")
    sc.label(p3v(Gp), "G", "HEAD", "middle", 17, dx=-14, dy=4)
    sc.mass(p3v(O3), None, r=4.5, col="BLUE")
    sc.label(p3v(O3), "O", "HEAD", "middle", 17, dx=-14, dy=-8)
    sc.label(p3v((0.0, 0.0, -A - 0.25)), "pole", "TEXT", "middle", 15, dy=22)
    sc.label(p3v((0.0, 0.0, -A * 0.36)), "a/2", "TEXT", "end", 14, dx=-8, dy=4)
    return sc


@figure("rb15-fbd",
        "Free-body diagram of the shell: weight at G and vertical normal reaction at the contact point, whose line passes "
        "through O.",
        r"Free-body diagram. Both forces are vertical, so the horizontal momentum is conserved; the reaction passes "
        r"through $O$ on the axis of revolution and has no moment about $Gz$ nor about the vertical through $G$.")
def fbd():
    sc = _scene()
    _shell(sc, faint=True)
    sc.dashed(G, P)
    sc.vec(G, (G[0], G[1] - 1.1), "mg", "PINK", 3.0, name_off=(24, 6), size=17, head=12)
    sc.vec(P, (P[0], P[1] + 2.4), "N", "GREEN", 3.0, name_off=(-16, 6), size=17, head=12)
    sc.dashed((0.0, 2.4), O)
    sc.line(add(POLE, KDIR, -0.4), add(O, KDIR, 1.2), "EDGE", 1.2, "7 4")
    sc.arc(G, 0.45, 80, -20, "GREEN", 1.8, head=True)
    sc.label(add(G, d(30), 0.45), S("M", "G"), "GREEN", "start", 16, weight="700", dx=12, dy=4)
    sc.label((3.35, 2.55), S("M", "G") + " = −(a/2) N sin θ " + bold("i"), "GREEN", "start", 15)
    sc.label((3.35, 2.25), "(clockwise, i out of the paper)", "TEXT", "start", 13, italic=False)
    sc.note((3.35, 4.2), "smooth plane: no friction", "TEXT", "start", 14)
    for pt, nm, off in ((O, "O", (-12, 4)), (G, "G", (-14, 4)), (P, "P", (-4, 26))):
        sc.mass(pt, None, r=4.5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    axis_out(sc, (-2.85, 5.25), None, "HEAD")
    sc.label((-2.85, 5.25), bold("i") + " (out of the paper)", "HEAD", "start", 16, dx=16, dy=5)
    return sc
