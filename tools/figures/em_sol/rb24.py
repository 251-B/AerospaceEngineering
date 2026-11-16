"""Problem RB-24: Lagrange's top (heavy axisymmetric pegtop with its vertex fixed at O)."""
import math

from figures.em_solutions import axis_in, figure, fixed_axis, right_angle, triangle
from figures.em_sol.rb01 import add, arrow_px, cross, d, norm, p3, p3v, ring, vadd, vscale
from figures.em_sol.rb03 import _curved
from figures.em_sol.rb06 import rlabel, rotation_view2
from figures.mech import S, Scene, bold

PSI, THETA, PHI = 35.0, 30.0, 40.0
ELL = 1.0


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


def _profile(t):
    """Radius of the pegtop at the axial distance t from the vertex (units of ell): cone, belly at 1.2, round top."""
    if t <= 0.0:
        return 0.0
    if t <= 1.2:
        return 0.8 * (t / 1.2) ** 0.8
    u = (t - 1.2) / 0.55
    return 0.8 * math.sqrt(max(0.0, 1.0 - u * u))


def _hull(pts):
    pts = sorted(set((round(x, 6), round(y, 6)) for x, y in pts))
    if len(pts) < 3:
        return pts

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


@figure("rb24-psi",
        "Precession rotation by psi about the vertical axis, seen from above.",
        r"Precession: $\mathcal B_1$ is $\mathcal B_0$ turned by $\psi$ about $\mathbf k$ (⊙). $\mathbf j_1$ leans to "
        r"negative $\mathbf i$, which gives the minus sign of $[{}_0R_1]$; $\mathbf i_1$ is the line of nodes.")
def rotation_psi():
    def post(sc):
        c, s = math.cos(math.radians(PSI)), math.sin(math.radians(PSI))
        sc.note((c, s), "line of nodes", "BLUE", "start", 13, dx=10, dy=-34)

    return rotation_view2(640, 520, (250, 350), 160, PSI, _ax("i"), _ax("j"), _ax("i", "1"), _ax("j", "1"),
                          _ax("k") + " = " + _ax("k", "1") + " (⊙)", ("ψ", ""), post=post, out_off=(-16, 28))


@figure("rb24-theta",
        "Nutation rotation by theta about the line of nodes, with the symmetry axis tilted from the vertical.",
        r"Nutation: $\mathcal B_2$ is $\mathcal B_1$ turned by $\theta$ about $\mathbf i_1$ (⊙). The axis $\mathbf k_2$ "
        r"leans to negative $\mathbf j_1$ (minus sign of $[{}_1R_2]$); the height of $G$ is $\ell\cos\theta$.")
def rotation_theta():
    th = THETA
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    ell = 0.75
    G = (-s * ell, c * ell)

    def post(sc):
        sc.dashed(G, (0.0, G[1]))
        sc.dim((0.20, 0.0), (0.20, G[1]), "", gap=0.0)
        sc.line((0.0, G[1]), (0.24, G[1]), "EDGE", 0.8, "2 4")
        sc.label((0.20, G[1] / 2), "ℓ cos θ", "TEXT", "start", 15, dx=8, dy=5)
        sc.dotp(G, 4.5)
        sc.label(G, "G", "HEAD", "middle", 17, dx=-14, dy=18)
        sc.label((G[0] / 2, G[1] / 2), "ℓ", "TEXT", "end", 16, dx=-10, dy=5)

    return rotation_view2(640, 520, (300, 360), 160, th, _ax("j", "1"), _ax("k", "1"), _ax("j", "2"),
                          _ax("k", "2") + " = " + _ax("k", "B"), _ax("i", "1") + " = " + _ax("i", "2") + " (⊙)",
                          ("θ", ""), post=post, out_off=(-16, 28), cy=0.88, side="left", lab_r=0.62,
                          arc_r=0.40, m2_off=(-50, -6))


@figure("rb24-phi",
        "Spin rotation by phi about the symmetry axis of the top.",
        r"Spin: $\mathcal B_B$ is $\mathcal B_2$ turned by $\varphi$ about $\mathbf k_2$ (⊙). Because the cross-section "
        r"is axisymmetric, the inertia tensor has the same components in $\mathcal B_2$ and $\mathcal B_B$.")
def rotation_phi():
    def pre(sc):
        sc.circle((0.0, 0.0), 1.2, "EDGE", 1.4, fill="HEAD", opacity=0.05)

    def post(sc):
        sc.note((0.0, -1.2), "axisymmetric: equal moments A m ℓ² about every transverse axis", "TEXT", "middle", 13,
                dy=24)

    return rotation_view2(700, 640, (350, 340), 160, PHI, _ax("i", "2"), _ax("j", "2"), _ax("i", "B"), _ax("j", "B"),
                          _ax("k", "2") + " = " + _ax("k", "B") + " (⊙) at G", ("φ", ""), pre=pre, post=post,
                          out_off=(-16, 28), arc_r=0.34, cy=0.72, lab_r=0.52)


@figure("rb24-steiner",
        "Pegtop with its tip O, centre of mass G on the axis and the parallel axes at O and G.",
        r"Steiner's theorem from $G$ to $O$: the offset $\ell\,\mathbf k_B$ lies on the symmetry axis, so only the two "
        r"transverse moments grow, by $m\ell^2$.")
def steiner():
    sc = Scene(760, 600, (400, 520), 150)
    ts = [1.75 * i / 90 for i in range(0, 91)]
    left = [(-_profile(t), t) for t in ts]
    right = [(_profile(t), t) for t in reversed(ts)]
    sc.poly(left + right, "HEAD", 2.0, fill="HEAD", close=True, opacity=0.07)
    G, O = (0.0, ELL), (0.0, 0.0)
    # grey axes through G
    sc.vec(G, (1.0, ELL), None, "EDGE", 1.4, head=8)
    sc.label((1.0, ELL), _ax("x", "B"), "TEXT", "middle", 16, weight="700", dx=16, dy=5)
    sc.vec(G, (0.0, ELL + 0.55), None, "EDGE", 1.4, head=8)
    sc.label((0.0, ELL + 0.55), _ax("z", "B"), "TEXT", "middle", 16, weight="700", dx=14, dy=4)
    # parallel axes at O (blue)
    sc.vec(O, (0.9, 0.0), None, "BLUE", 2.4, head=10)
    sc.label((0.9, 0.0), _ax("x", "B") + "′", "BLUE", "middle", 16, weight="700", dx=18, dy=5)
    sc.vec(O, (0.0, -0.45), None, "BLUE", 2.4, head=10)
    sc.label((0.0, -0.45), _ax("z", "B") + "′", "BLUE", "middle", 16, weight="700", dx=18, dy=4)
    sc.note((0.9, 0.0), "parallel axes at O", "BLUE", "start", 13, dx=-30, dy=48)
    # r_O^G
    sc.vec((0.0, 0.03), (0.0, ELL - 0.03), None, "ACC", 3.2, head=12)
    sc.label((0.0, ELL / 2), S(bold("r"), "O", "G") + " = ℓ " + _ax("k", "B"), "ACC", "end", 17, weight="700", dx=-12, dy=5)
    sc.dim((0.55, 0.0), (0.55, ELL), "")
    sc.label((0.55, ELL / 2), "ℓ", "TEXT", "start", 17, dx=10, dy=5)
    sc.line((0.0, ELL), (0.6, ELL), "EDGE", 0.8, "2 4")
    sc.dotp(G, 4.5)
    sc.label(G, "G", "HEAD", "middle", 17, dx=-16, dy=-8)
    sc.dotp(O, 4.5)
    sc.label(O, "O", "HEAD", "middle", 17, dx=-16, dy=18)
    # j_B into the paper
    axis_in(sc, (-1.3, 1.85), None, "HEAD")
    sc.label((-1.3, 1.85), _ax("j", "B"), "HEAD", "start", 16, weight="700", dx=16, dy=5)
    sc.note((-1.95, -0.05), "Steiner: + m ℓ² on x_B and y_B,", "TEXT", "start", 13)
    sc.note((-1.95, -0.05), "+ 0 on z_B", "TEXT", "start", 13, dy=18)
    return sc


@figure("rb24-fbd",
        "Free-body diagram of the top: weight at the centre of mass and reaction at the fixed tip.",
        r"Free-body diagram: weight $-mg\,\mathbf k$ at $G$ and the reaction $\mathbf R$ at the fixed vertex $O$ (no "
        r"torque). About $O$ only the weight has a moment, $mg\ell\sin\theta\,\mathbf i_2$, along the line of nodes.")
def fbd():
    sc = Scene(700, 620, (360, 470), 150)
    ps, th = math.radians(PSI), math.radians(THETA)
    i1 = (math.cos(ps), math.sin(ps), 0.0)
    j1 = (-math.sin(ps), math.cos(ps), 0.0)
    k = (0.0, 0.0, 1.0)
    i2 = i1
    j2 = vadd(vscale(j1, math.cos(th)), k, math.sin(th))
    k2 = vadd(vscale(j1, -math.sin(th)), k, math.cos(th))
    O = (0.0, 0.0, 0.0)
    # fixed axes (thin grey)
    for tip, nm, off in ((vscale((1.0, 0.0, 0.0), 1.1), "i", (-12, 14)), (vscale((0.0, 1.0, 0.0), 1.5), "j", (12, 12)),
                         (vscale(k, 2.45), "k", (-12, 2))):
        sc.vec((0.0, 0.0), p3v(tip), None, "EDGE", 1.3, head=8)
        sc.label(p3v(tip), bold(nm), "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    # the top: silhouette of rings perpendicular to k_2
    pts = []
    for i in range(0, 91, 3):
        t = i * 0.02
        pts += ring(vscale(k2, t), i2, j2, _profile(t), n=48)
    hull = _hull(pts)
    sc.poly(hull, "HEAD", 2.0, fill="HEAD", close=True, opacity=0.07)
    pb = ring(vscale(k2, 1.2), i2, j2, 0.8, n=72)
    sc.poly(pb, "HEAD", 1.2, "5 4")
    # axis k_2 (blue) and line of nodes i_1 = i_2 (grey)
    sc.vec(p3v(O), p3v(vscale(k2, 2.05)), None, "BLUE", 2.8, head=11)
    sc.label(p3v(vscale(k2, 2.05)), _ax("k", "2"), "BLUE", "middle", 17, weight="700", dx=-16, dy=-4)
    sc.line(p3v(vscale(i1, -0.9)), p3v(vscale(i1, 1.5)), "EDGE", 1.5)
    sc.label(p3v(vscale(i1, 1.5)), _ax("i", "1") + " = " + _ax("i", "2"), "TEXT", "end", 15, weight="700", dx=-84, dy=24)
    G = vscale(k2, ELL)
    # weight
    Wt = vadd(G, k, -0.95)
    sc.vec(p3v(G), p3v(Wt), "mg", "PINK", 3.6, name_off=(-20, 14), size=17, head=13)
    # reaction at O and its components along i_2, j_2, k_2
    R1, R2, R3 = 0.45, 0.35, 1.05
    Rv = vadd(vadd(vscale(i2, R1), j2, R2), k2, R3)
    for u, v, nm, off in ((i2, R1, S("R", "1"), (20, 14)), (j2, R2, S("R", "2"), (14, 6)), (k2, R3, S("R", "3"), (-14, -2))):
        tip = vscale(u, v)
        sc.line(p3v(O), p3v(tip), "PINK", 1.4, "5 4")
        sc.label(p3v(tip), nm, "PINK", "middle", 16, weight="700", dx=off[0], dy=off[1])
    sc.vec(p3v(O), p3v(Rv), None, "PINK", 3.6, head=13)
    sc.label(p3v(Rv), "R", "PINK", "middle", 18, weight="700", dx=16, dy=-2)
    # moment of the weight about O, about the line of nodes
    c = vscale(i1, 1.35)
    _curved(sc, c, i1, 0.42, 30, 320, "ACC", "", size=16)
    sc.label(p3v(c), S(bold("M"), "O") + " = mgℓ sin θ " + _ax("i", "2"), "ACC", "start", 16, weight="700", dx=96, dy=-4)
    sc.dotp(p3v(G), 4.5)
    sc.label(p3v(G), "G", "HEAD", "middle", 17, dx=18, dy=4)
    sc.mass(p3v(O), None, r=5, col="HEAD")
    sc.label(p3v(O), "O", "HEAD", "middle", 17, dx=-16, dy=22)
    return sc
