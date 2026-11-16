"""Problem RB-16: homogeneous sphere rolling on an inclined plane with an attraction towards a point O of the plane."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, arrow_px, d, p3, p3v, ring, rotation_view, sub
from figures.em_sol.rb15 import _hull
from figures.mech import S, Scene, bold

ORANGE = "ACC"
AL = 25.0
AR = math.radians(AL)
I_DIR = (math.cos(AR), -math.sin(AR))          # downhill, in the (I, K) view
K_DIR = (math.sin(AR), math.cos(AR))           # normal to the plane
W_I, W_K = bold("I"), bold("K")


def _weight_components(sc, tail, L, wname, comp_i, comp_k, name_off, i_off, k_off):
    """Weight vector from `tail` (length L, straight down) with the dashed legs L sin(a) along i and L cos(a) along -k."""
    tip = (tail[0], tail[1] - L)
    q1 = add(tail, I_DIR, L * math.sin(AR))
    sc.dashed(tail, q1)
    sc.dashed(q1, tip)
    sc.vec(tail, tip, wname, "PINK", 3.0, name_off=name_off, size=17, head=12)
    sc.label(((tail[0] + q1[0]) / 2, (tail[1] + q1[1]) / 2), comp_i, "TEXT", "start", 15, dx=i_off[0], dy=i_off[1])
    sc.label(((q1[0] + tip[0]) / 2, (q1[1] + tip[1]) / 2), comp_k, "TEXT", "start", 15, dx=k_off[0], dy=k_off[1])


@figure("rb16-rot-alpha",
        "The basis of the inclined plane obtained by turning the horizontal basis by alpha about j, with the components "
        "of the weight.",
        r"Rotation about $\mathbf j$ (⊗) by $\alpha$: $\mathbf i$ points downhill and $\mathbf k$ is the normal to the plane. "
        r"The weight splits into $mg\sin\alpha$ along $\mathbf i$ and $mg\cos\alpha$ against $\mathbf k$.")
def rot_alpha():
    def pre(sc):
        a = add((0.0, 0.0), I_DIR, -1.6)
        b = add((0.0, 0.0), I_DIR, 3.6)
        sc.ground(a, b, -1)

    def post(sc):
        sc.label((0.0, 0.0), "O", "HEAD", "middle", 17, dx=-16, dy=-6)
        _weight_components(sc, (2.6, 2.3), 1.6, "−g " + W_K, "g sin α", "g cos α", (30, 6), (2, -26), (12, 6))
    sc = rotation_view(860, 600, (330, 390), 125, -AL, W_I, W_K, bold("i"), bold("k"), bold("j") + " (⊗)",
                       ("α", ""), pre=pre, post=post, out_kind="in", out_off=(-6, 30))
    return sc


def _ell(c, a, b, tilt, t):
    tr = math.radians(tilt)
    x, y = a * math.cos(math.radians(t)), b * math.sin(math.radians(t))
    return (c[0] + x * math.cos(tr) - y * math.sin(tr), c[1] + x * math.sin(tr) + y * math.cos(tr))


@figure("rb16-plane",
        "Top view of the inclined plane with O, the equilibrium point E and the elliptical path of the centre of the "
        "sphere.",
        r"Top view of the plane. $P$ is the contact point, straight below $G$; the in-plane forces vanish at $E$, and $G$ "
        r"moves on an ellipse centred above $E$.")
def plane():
    sc = Scene(800, 480, (80, 300), 76)
    O, E = (0.0, 0.0), (4.0, 0.0)
    fixed_axis(sc, O, 0, 8.2, bold("i"), off=(14, 6))
    fixed_axis(sc, O, 90, 3.2, bold("j"), off=(12, 8))
    axis_out(sc, O, None, "HEAD")
    sc.label(O, bold("k") + " (⊙)", "HEAD", "end", 16, weight="700", dx=-14, dy=26)
    # trajectory
    sc.poly([_ell(E, 3.0, 1.5, 20.0, t) for t in range(0, 361, 4)], "EDGE", 1.6, "7 5", close=True)
    P = _ell(E, 3.0, 1.5, 20.0, 20.0)
    # equilibrium point and its dimension below the axis
    sc.mass(E, None, r=4.5, col="BLUE")
    sc.label(E, "E", "HEAD", "middle", 17, dx=0, dy=-14)
    sc.dashed((0.0, -0.1), (0.0, -0.85))
    sc.dashed((4.0, -0.1), (4.0, -0.85))
    sc.dim((0.0, -0.7), (4.0, -0.7), S("x", "E") + " = g sin α / κ", off=(0, 20))
    # projections of P
    sc.dashed(P, (P[0], 0.0))
    sc.dashed(P, (0.0, P[1]))
    sc.label((P[0], 0.0), "x", "TEXT", "middle", 16, dx=0, dy=22)
    sc.label((0.0, P[1]), "y", "TEXT", "end", 16, dx=-10, dy=5)
    # forces and velocity at P
    ang_o = math.degrees(math.atan2(-P[1], -P[0]))
    sc.vec(P, add(P, d(ang_o), 2.0), None, "GREEN", 3.0, head=12)
    tipa = add(P, d(ang_o), 2.0)
    sc.label(tipa, "attraction −m κ r", "GREEN", "end", 15, weight="700", dx=-8, dy=10)
    sc.label(tipa, "(in-plane part)", "GREEN", "end", 14, weight="400", dx=-8, dy=28)
    sc.vec(P, add(P, (1.55, 0.0)), None, "PINK", 3.0, head=12)
    sc.label(add(P, (1.1, 0.0)), "m g sin α", "PINK", "middle", 16, weight="700", dy=24)
    tr = math.radians(20.0)
    tx, ty = -3.0 * math.sin(math.radians(20)), 1.5 * math.cos(math.radians(20))
    v = (tx * math.cos(tr) - ty * math.sin(tr), tx * math.sin(tr) + ty * math.cos(tr))
    n = math.hypot(*v)
    v = (v[0] / n, v[1] / n)
    sc.vec(P, add(P, v, 1.5), S(bold("v"), "G"), "BLUE", 3.0, name_off=(-18, -6), size=17, head=12)
    sc.mass(P, None, r=5, col="ACC")
    sc.line(P, add(P, (0.3, 0.42)), "EDGE", 1.0)
    sc.label(add(P, (0.3, 0.42)), "P (below G)", "HEAD", "start", 16, dx=4, dy=-4)
    # spin about the normal at P
    sc.spin(P, 0.45, 50, 130, "", "GREEN")
    sc.label(add(P, d(90), 0.45), S("ω", "z"), "GREEN", "middle", 16, weight="700", dy=-24)
    sc.label(O, "O", "HEAD", "middle", 17, dx=12, dy=22)
    return sc


def _sph(r, chi, lam):
    c, l = math.radians(chi), math.radians(lam)
    return (r * math.sin(c) * math.cos(l), r * math.sin(c) * math.sin(l), r * math.cos(c))


def _pr(q):
    """Oblique view from above: x towards the viewer (down), y to the right, z up."""
    return (q[1] - 0.18 * q[0], q[2] - 0.55 * q[0])


@figure("rb16-sphere-element",
        "Spherical volume element of the solid sphere with its coordinates r, chi and lambda.",
        r"Volume element $dV = r^2\sin\chi\,dr\,d\chi\,d\lambda$ used for the mass and the moments of inertia of the sphere.")
def sphere_element():
    sc = Scene(760, 610, (330, 345), 82)
    R, r0, CHI, LAM = 3.0, 2.2, 50.0, 35.0
    G3 = (0.0, 0.0, 0.0)
    circ = [(R * math.cos(math.radians(t)), R * math.sin(math.radians(t))) for t in range(0, 361, 4)]
    sc.poly(circ, "EDGE", 0.0, fill="EDGE", close=True, opacity=0.14)
    sc.poly(circ, "HEAD", 2.0, close=True)
    sc.poly([_pr((R * math.cos(math.radians(t)), R * math.sin(math.radians(t)), 0)) for t in range(0, 361, 5)],
            "EDGE", 1.0, "3 4", close=True)
    # axes
    sc.vec(_pr(G3), _pr((0, 0, 3.9)), "z", "BLUE", 2.6, name_off=(-12, 2), size=17, head=11)
    sc.vec(_pr(G3), _pr((0, 3.9, 0)), "y", "BLUE", 2.6, name_off=(14, 6), size=17, head=11)
    sc.vec(_pr(G3), _pr((3.7, 0, 0)), "x", "BLUE", 2.6, name_off=(-12, 14), size=17, head=11)
    sc.dashed(_pr(G3), _pr((0, -R, 0)))
    sc.label(_pr((0, -R * 0.5, 0)), "R", "TEXT", "middle", 16, dx=0, dy=-10)
    # element
    pe = _sph(r0, CHI, LAM)
    foot = (pe[0], pe[1], 0.0)
    sc.dashed(_pr(G3), _pr(pe))
    sc.label(_pr(_sph(r0 * 0.5, CHI, LAM)), "r", "TEXT", "middle", 16, dx=-12, dy=-4)
    sc.dashed(_pr(G3), _pr(foot))
    sc.dashed(_pr(pe), _pr(foot))
    sc.label(_pr(foot), "r sin χ", "TEXT", "start", 15, dx=8, dy=22)
    # arc of the colatitude (meridian plane) and of the longitude (xy plane)
    ua = (math.cos(math.radians(LAM)), math.sin(math.radians(LAM)))
    ar = [_pr((1.5 * math.sin(math.radians(t)) * ua[0], 1.5 * math.sin(math.radians(t)) * ua[1],
               1.5 * math.cos(math.radians(t)))) for t in [CHI * i / 20 for i in range(21)]]
    sc.poly(ar, "GREEN", 1.8)
    arrow_px(sc, ar[-3], ar[-1], "GREEN", 9)
    sc.label(ar[11], "χ", "GREEN", "middle", 17, dx=-6, dy=-8)
    lr = [_pr((1.1 * math.cos(math.radians(t)), 1.1 * math.sin(math.radians(t)), 0.0)) for t in [LAM * i / 20 for i in range(21)]]
    sc.poly(lr, "GREEN", 1.8)
    arrow_px(sc, lr[-3], lr[-1], "GREEN", 9)
    sc.label(lr[10], "λ", "GREEN", "middle", 17, dx=-2, dy=26)
    # the curved box dr x r dchi x r sin(chi) dlambda (exaggerated)
    dr, dc, dl = 0.5, 12.0, 16.0
    corners = [_sph(r0 + a * dr, CHI + b * dc, LAM + c * dl) for a in (-.5, .5) for b in (-.5, .5) for c in (-.5, .5)]
    pts = [_pr(q) for q in corners]
    sc.poly(_hull(pts), "ACC", 1.6, fill="ACC", close=True, opacity=0.65)
    for ia in range(8):
        for ib in range(ia + 1, 8):
            if bin(ia ^ ib).count("1") == 1:
                sc.line(pts[ia], pts[ib], "HEAD", 0.9)
    tp = _pr(pe)
    sc.line((tp[0] + 0.12, tp[1] + 0.12), (tp[0] + 0.9, tp[1] + 0.9), "ACC", 1.2)
    sc.label((tp[0] + 0.95, tp[1] + 0.95), "dr,  r dχ,  r sin χ dλ", "ACC", "start", 16, weight="700", dx=4, dy=4)
    sc.mass(_pr(G3), None, r=5, col="BLUE")
    sc.label(_pr(G3), "G", "HEAD", "middle", 17, dx=-14, dy=-8)
    return sc


@figure("rb16-fbd",
        "Free-body diagram of the sphere: weight and attraction at G, normal reaction and friction at the contact point.",
        r"Free-body diagram. The weight and the attraction act at $G$ and have no moment about it; only the friction at $P$, "
        r"with the arm $-R\,\mathbf k$, changes the rotation.")
def fbd():
    sc = Scene(900, 480, (470, 290), 82)
    R = 1.5
    P = (0.0, 0.0)
    Gc = add(P, K_DIR, R)
    O = add(P, I_DIR, -5.0)
    sc.ground(add(P, I_DIR, -5.8), add(P, I_DIR, 4.6), -1)
    sc.circle(Gc, R, "HEAD", 2.2, fill="EDGE", opacity=0.10)
    # arm GP as an offset dimension (the line GP itself carries N)
    off = (-0.55 * I_DIR[0], -0.55 * I_DIR[1])
    sc.dim(add(Gc, off), add(P, off), "R", off=(-14, 4))
    sc.dashed(Gc, add(Gc, off, 1.15))
    sc.dashed(P, add(P, off, 1.15))
    # weight and its components
    _weight_components(sc, Gc, 1.0, "mg", "mg sin α", "mg cos α", (0, 22), (14, -8), (10, 8))
    # attraction towards O
    u = (O[0] - Gc[0], O[1] - Gc[1])
    n = math.hypot(*u)
    u = (u[0] / n, u[1] / n)
    sc.vec(Gc, add(Gc, u, 2.5), None, "GREEN", 3.0, head=12)
    sc.label(add(Gc, u, 2.5), "m κ |OG|", "GREEN", "middle", 16, weight="700", dx=0, dy=-14)
    # contact forces
    sc.vec(P, add(P, K_DIR, 0.8), "N", "GREEN", 3.0, name_off=(-14, -2), size=17, head=12)
    sc.vec(P, add(P, I_DIR, -1.6), S("F", "x"), "GREEN", 3.0, name_off=(-6, -14), size=17, head=12)
    sc.note((2.35, 0.5), S("F", "y") + " along j (normal to the paper)", "TEXT", "start", 13)
    # basis at O and the angle of the plane
    unit(sc, O, math.degrees(math.atan2(I_DIR[1], I_DIR[0])), 1.0, bold("i"), "BLUE", off=(6, -14))
    unit(sc, O, math.degrees(math.atan2(K_DIR[1], K_DIR[0])), 1.0, bold("k"), "BLUE", off=(8, -12))
    foot = add(P, I_DIR, 3.0)
    sc.dashed(foot, add(foot, (1.0, 0.0), 1.5))
    sc.arc(foot, 0.9, -AL, 0, "GREEN", 1.8, head=True)
    sc.label(add(foot, d(-AL / 2), 0.9), "α", "GREEN", "start", 17, dx=8, dy=6)
    for pt, nm, o in ((Gc, "G", (12, -12)), (P, "P", (22, 24)), (O, "O", (-14, -10))):
        sc.mass(pt, None, r=4.5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=o[0], dy=o[1])
    return sc
