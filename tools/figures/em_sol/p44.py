"""Problem 44: the little Prince throwing seeds (launch point, view along k, free-body diagram, orbit)."""
import math

from figures.em_sol.p31 import _dvec, _matrix, _mname, _pol, _spin
from figures.em_sol.p32 import RED, YELLOW, arrow, away, basis_view
from figures.em_sol.p42 import ER, ETH, _along
from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle
from figures.mech import S, Scene, bold
from figures.svgkit import arrow_head

K_ = bold("k")
I_ = bold("i")
J_ = bold("j")
DARK = "#4b5563"
V0 = S(bold("v"), "0")


def _disc(sc, c, R, w=2.4):
    sc.circle(c, R, DARK, w, fill="EDGE", opacity=0.22)


@figure("p44-launch",
        "Launch point on the asteroid rim with the local vertical e_r, the local horizontal e_theta and the launch velocity at 60 degrees above the horizontal, with its right triangle.",
        r"Launch point, $\mathbf k$ out of the paper. In the right triangle of hypotenuse $v_0$ the horizontal leg $v_0\cos\gamma$ is adjacent to $\gamma$ and the vertical leg $v_0\sin\gamma$ opposite: $\dot r(0) = v_0\sin\gamma$ and $R\,\dot\theta(0) = v_0\cos\gamma$.")
def launch():
    sc = Scene(840, 470, (330, 300), 110)
    L = (0.0, 0.0)
    C = (-3.0, 0.0)
    g = math.radians(60.0)
    v0 = 2.4
    hz, vt = v0 * math.cos(g), v0 * math.sin(g)          # 1.2 and 2.078
    # asteroid: rim arc from -25 to +25 degrees, light grey inside
    arc = [(C[0] + 3.0 * math.cos(math.radians(a)), C[1] + 3.0 * math.sin(math.radians(a))) for a in [-25 + i for i in range(51)]]
    sc.poly(arc + [(-1.9, arc[-1][1]), (-1.9, arc[0][1])], "EDGE", 0.0, fill="EDGE", close=True, opacity=0.22)
    sc.arc(C, 3.0, -25, 25, DARK, 3.4)
    sc.vec((-0.9, 0.0), (-1.7, 0.0), None, "TEXT", 1.8, head=9)
    sc.label((-1.3, 0.0), "to O", "TEXT", "middle", 15, dy=-10)
    # right triangle of the launch velocity
    A = (0.0, hz)
    T = (vt, hz)
    triangle(sc, [L, A, T], YELLOW, 0.30)
    sc.line(A, T, "EDGE", 1.2, "5 4")
    right_angle(sc, A, 270, 0, 0.12)
    # local horizontal (tangent plane), dashed through L
    sc.line((0.0, -1.2), (0.0, 1.95), "EDGE", 1.3, "7 5")
    sc.label((0.0, -1.2), "local horizontal (tangent plane)", "TEXT", "start", 14, italic=False, dx=10, dy=4)
    sc.label((0.0, 0.93), V0 + " cos γ", "TEXT", "start", 15, italic=False, dx=14)
    sc.label((0.0, 0.75), "(adjacent, horizontal)", "TEXT", "start", 13, italic=False, dx=12)
    sc.label((vt / 2 + 0.2, hz), V0 + " sin γ (opposite, vertical)", "TEXT", "middle", 15, italic=False, dy=-12)
    # basis at L
    sc.vec(L, (1.4, 0.0), None, "BLUE", 2.8, head=11)
    sc.label((1.4, 0.0), ER + " = local vertical", "BLUE", "start", 16, dx=12, dy=-10)
    sc.vec(L, (0.0, 1.5), None, "BLUE", 2.8, head=11)
    sc.label((0.0, 1.5), ETH + " = local horizontal", "BLUE", "end", 16, dx=-12, dy=-4)
    # launch velocity
    sc.vec(L, T, None, "GREEN", 3.8, head=13)
    sc.label(T, V0, "GREEN", "start", 18, weight="700", dx=14, dy=22)
    # angle gamma between e_theta and v0 (clockwise from e_theta)
    sc.arc(L, 0.55, 90, 30, "GREEN", 1.8, head=True)
    sc.label(_pol(L, 0.74, 44), "γ = 60°", "GREEN", "middle", 15, italic=False, dy=5)
    sc.dotp(L, 6.0)
    sc.label(L, "launch point, r = R", "HEAD", "start", 16, dx=12, dy=26)
    axis_out(sc, (-2.4, 1.95), None)
    sc.label((-2.4, 1.95), K_, "HEAD", "start", 17, dx=16, dy=5)
    return sc


@figure("p44-rotation-k",
        "View along k of the polar basis e_r, e_theta turned by theta from i, j, with the two unit right triangles.",
        r"Rotation by $\theta$ about $\mathbf k$ (out of the paper). The triangle of $\mathbf e_\theta$ has its opposite leg along $-\mathbf i$: the minus sign of $\mathbf e_\theta = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j$.")
def rotation_k():
    sc = Scene(860, 600, (330, 290), 80)
    O = (0.0, 0.0)
    basis_view(sc, O, 42.0, (I_, J_), (ER, ETH), L=2.0, u=1.4, ang="θ",
               legs=("cos θ", "sin θ", "cos θ", "−sin θ on i"), cf=0.9, l1dx=8, l4=(12, "end", 13))
    axis_out(sc, O, None)
    sc.label(O, K_, "HEAD", "end", 17, dx=-20, dy=8)
    _spin(sc, O, 0.3, 200, 340, "positive about k", (-26, 46), "end")
    _matrix(sc, 3.0, -1.2, _mname("0", "1"), (("cos θ", "−sin θ", "0"), ("sin θ", "cos θ", "0"), ("0", "0", "1")), colw=0.8)
    return sc


@figure("p44-fbd",
        "Free-body diagram of the seed in flight with the single gravitational force towards the centre of the asteroid (velocity in a separate inset).",
        r"In flight the only force on the seed is the attraction of the asteroid, $-\mu m\,\mathbf e_r/r^2$ with $\mu = GM$; it passes through $O$, so the angular momentum about $O$ is conserved.")
def fbd():
    sc = Scene(900, 540, (200, 320), 110)
    O = (0.0, 0.0)
    th = 30.0
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    r = 2.0
    P = (r * c, r * s)
    _disc(sc, O, 1.0)
    sc.line((-0.1, 0.0), (0.1, 0.0), "TEXT", 1.6)
    sc.line((0.0, -0.1), (0.0, 0.1), "TEXT", 1.6)
    sc.label(O, "O, mass M", "TEXT", "middle", 15, dy=34)
    axis_out(sc, (-0.45, 0.45), None)
    sc.label((-0.45, 0.45), K_, "HEAD", "start", 16, dx=14, dy=5)
    sc.line(O, P, "EDGE", 1.2, "6 5")
    arrow(sc, P, (-c, -s), RED, 3.6, 13, 0.8)
    sc.label((1.6 * c, 1.6 * s), "F = −(μ m / " + S("r", None, "2") + ") " + ER + ",  μ = G M", RED, "start", 15, dx=12, dy=34)
    for d, nm, dx, dy, anc in (((c, s), ER, 8, 14, "start"), ((-s, c), ETH, -8, -6, "end")):
        tip = (P[0] + 0.6 * d[0], P[1] + 0.6 * d[1])
        sc.vec(P, tip, None, "BLUE", 2.6, head=10)
        sc.label(tip, nm, "BLUE", anc, 17, weight="700", dx=dx, dy=dy)
    sc.dotp(P, 5.5)
    sc.label(P, "P", "HEAD", "start", 17, dx=10, dy=24)
    # inset: velocity of P (not a force)
    x0, y0, x1, y1 = 3.1, -0.5, 5.9, 2.0
    sc.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], "EDGE", 1.2, close=True)
    sc.note((x0 + 0.12, y1 - 0.2), "velocity of P (inset, not a force)", "TEXT", "start", 13)
    Q = (3.7, -0.1)
    ang = th + 70.0
    tip = (Q[0] + math.cos(math.radians(ang)), Q[1] + math.sin(math.radians(ang)))
    for d in ((c, s),):
        e = (Q[0] + 0.5 * d[0], Q[1] + 0.5 * d[1])
        sc.vec(Q, e, None, "BLUE", 2.0, head=9)
        sc.label(e, ER, "BLUE", "start", 15, weight="700", dx=8, dy=14)
    sc.vec(Q, tip, None, "GREEN", 3.4, head=12)
    sc.label(tip, S(bold("v"), "0", "P"), "GREEN", "start", 17, weight="700", dx=10, dy=-4)
    sc.dotp(Q, 4.0)
    sc.note((-1.0, -1.7), "inertial frame (m much smaller than M): no inertia forces; no constraint in flight", "TEXT", "start", 13)
    return sc


# ---------------------------------------------------------------------------------------------------- orbit
PH = 12.0 / 35.0                      # semi-latus rectum in units of R
EC = 31.0 / 35.0
PHI0 = math.acos((PH - 1.0) / EC)     # r(theta = 0) = R: r = PH / (1 + EC cos(theta + PHI0))
AP_DEG = 180.0 - math.degrees(PHI0)   # polar angle of the apocentre (42.1 degrees)
LAND = 2.0 * AP_DEG                   # landing polar angle (84.2 degrees)


def _orb(th_deg):
    t = math.radians(th_deg)
    r = PH / (1 + EC * math.cos(t + PHI0))
    return (r * math.cos(t), r * math.sin(t))


@figure("p44-orbit",
        "The elliptical orbit of the seed with a focus at the centre of the asteroid, rising from the launch point to the apocentre at 3R and coming down to the surface before the pericentre, which lies inside the asteroid.",
        r"Orbit of the seed: an ellipse of eccentricity $31/35$ with a focus at $O$. The seed climbs to the apocentre $3R$, where its speed is $v_0/6$, and lands at $84.2^\circ$ from the launch point; the pericentre $2R/11$ lies inside the asteroid.")
def orbit():
    sc = Scene(830, 640, (270, 440), 150)
    O = (0.0, 0.0)
    ad = math.radians(AP_DEG)
    ea = (math.cos(ad), math.sin(ad))
    A = (3.0 * ea[0], 3.0 * ea[1])
    Pe = (-PH / (1 + EC) * ea[0], -PH / (1 + EC) * ea[1])
    a_ = PH / (1 - EC * EC)
    cen = (EC * a_ * ea[0], EC * a_ * ea[1])
    _disc(sc, O, 1.0)
    sc.label(_pol(O, 1.0, 232), "asteroid, radius R", "TEXT", "end", 15, dx=-8, dy=24)
    # major axis (dash-dot) through O and A
    sc.line((-0.42 * ea[0], -0.42 * ea[1]), (3.3 * ea[0], 3.3 * ea[1]), "EDGE", 1.2, "11 3 2 3")
    # rest of the ellipse, dashed (all of it lies inside the asteroid)
    sc.poly([_orb(LAND + (360.0 - LAND) * i / 240.0) for i in range(241)], "EDGE", 1.3, "6 5")
    # travelled arc
    pts = [_orb(LAND * i / 160.0) for i in range(161)]
    sc.poly(pts, DARK, 3.6)
    for idx in (45, 125):
        a, b = sc.P(pts[idx - 4]), sc.P(pts[idx + 4])
        arrow_head(sc.c, a, b, DARK, 12)
    # short axes i, j and k
    sc.vec(O, (1.5, 0.0), None, "EDGE", 1.3, head=8)
    sc.label((1.5, 0.0), "i", "TEXT", "middle", 15, weight="700", dx=10, dy=-2)
    sc.vec(O, (0.0, 0.6), None, "EDGE", 1.3, head=8)
    sc.label((0.0, 0.6), "j", "TEXT", "end", 15, weight="700", dx=-8, dy=4)
    axis_out(sc, O, None)
    sc.label(O, K_, "HEAD", "end", 16, dx=-14, dy=-10)
    # launch point and velocity
    L = (1.0, 0.0)
    sc.vec(L, (1.0 + 0.9 * math.cos(math.radians(30)), 0.9 * math.sin(math.radians(30))), None, "GREEN", 3.2, head=12)
    sc.label((1.0 + 0.9 * math.cos(math.radians(30)), 0.45), V0, "GREEN", "start", 17, weight="700", dx=10, dy=18)
    sc.dotp(L, 5.5)
    sc.label(L, "launch, r = R", "HEAD", "start", 15, dx=2, dy=26)
    # landing point and its label with a leader
    Ld = _orb(LAND)
    sc.dotp(Ld, 5.5)
    sc.line(Ld, (-0.3, 1.55), "EDGE", 1.0)
    sc.label((-0.3, 1.55), "lands, θ = 84.2°", "HEAD", "end", 15, dx=-4, dy=-4)
    # apocentre and speed there
    sc.dotp(A, 6.0)
    sc.label(A, "apocentre, r = 3R", "HEAD", "start", 16, dx=16, dy=12)
    vt = (-math.sin(ad), math.cos(ad))
    tipv = (A[0] + 0.16 * vt[0], A[1] + 0.16 * vt[1])
    sc.vec(A, tipv, None, "GREEN", 2.8, head=8)
    sc.label(A, S("v", "a") + " = " + S("v", "0") + " / 6", "GREEN", "middle", 15, dx=-8, dy=-34)
    # 3R dimension (offset from the dash-dot axis)
    nrm = (math.sin(ad), -math.cos(ad))
    off = 0.12
    sc.dim((O[0] + off * nrm[0], O[1] + off * nrm[1]), (0.95 * A[0] + off * nrm[0], 0.95 * A[1] + off * nrm[1]), "3R", off=(18, 14))
    # pericentre
    sc.circle(Pe, 0.04, "HEAD", 1.8)
    sc.line((Pe[0] + 0.02, Pe[1] - 0.05), (-0.1, -0.5), "EDGE", 1.0)
    sc.label((0.0, -0.62), "pericentre 2R/11 (not reached)", "HEAD", "middle", 14, italic=False)
    return sc
