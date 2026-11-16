"""Problem RB-19: sphere on the floor with a spring from the point A of its surface to a fixed point C (Euler angles)."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, arrow_px, d, p3, p3v, rotation_view, sub
from figures.em_sol.rb12 import plane_rotation
from figures.em_sol.rb18 import _lane
from figures.mech import S, Scene, bold

ORANGE = "ACC"
K = bold("k")
I1, J1, K2 = S(bold("i"), "1"), S(bold("j"), "1"), S(bold("k"), "2")
I2, J2 = S(bold("i"), "2"), S(bold("j"), "2")
IB, JB = S(bold("i"), "b"), S(bold("j"), "b")
Y2 = S("y", "2")


@figure("rb19-rot-psi",
        "First Euler rotation, by psi about the vertical, which places the horizontal axis y_2.",
        r"First rotation, by $\psi$ about $\mathbf k$ (⊙). $\psi$ is the angle between $Oy$ and $Gy_2$.")
def rot_psi():
    ang = 30.0

    def post(sc):
        sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=14, dy=26)
        tip = add((0.0, 0.0), d(120.0), 1.0)
        sc.note(tip, "(horizontal)", "TEXT", "end", 13, dx=-60, dy=-26)
    return plane_rotation(780, 600, (330, 490), 250, ang, (bold("i"), bold("j"), I1, J1 + " = " + Y2), K + " (⊙)",
                          ("ψ", ""), None, extra_post=post, out_off=(-16, 28))


@figure("rb19-rot-theta",
        "Second Euler rotation, by theta about the horizontal axis y_2, which tilts GA away from the vertical.",
        r"Second rotation, by $\theta$ about $\mathbf j_1 = \mathbf j_2$ (⊗). $A$ is at the height $a(1 + \cos\theta)$ and at "
        r"the horizontal distance $a\sin\theta$ from $G$ along $\mathbf i_1$.")
def rot_theta():
    a, th = 2.0, 40.0
    t = math.radians(th)
    sc = Scene(780, 620, (260, 330), 105)
    O = (0.0, 0.0)
    sc.ground((-2.6, -a), (3.6, -a), -1)
    sc.circle(O, a, "HEAD", 1.8, fill="EDGE", opacity=0.08)
    fixed_axis(sc, O, 0, 2.4, I1, off=(14, 6))
    fixed_axis(sc, O, 90, 2.5, K, off=(12, 6))
    A = (a * math.sin(t), a * math.cos(t))
    # big triangle of k2: hypotenuse a, vertical leg a cos(theta), dashed horizontal leg a sin(theta)
    triangle(sc, [O, (0.0, A[1]), A], "ACC", 0.16)
    sc.dashed((0.0, A[1]), A)
    right_angle(sc, (0.0, A[1]), 270, 0, 0.12)
    sc.label((0.0, A[1] / 2), "a cos θ", "TEXT", "end", 15, dx=-8, dy=18)
    sc.label((A[0] / 2, A[1]), "a sin θ", "TEXT", "middle", 15, dy=-8)
    # i2 and its small triangle
    foot, tip = (math.cos(t), 0.0), (math.cos(t), -math.sin(t))
    triangle(sc, [O, foot, tip], "ACC", 0.20)
    sc.dashed(foot, tip)
    right_angle(sc, foot, 180, 270, 0.07)
    sc.label((foot[0] / 2, 0.0), "cos θ", "TEXT", "middle", 15, dy=-8)
    sc.label(tip, "sin θ", "TEXT", "start", 15, dx=8, dy=-10)
    unit(sc, O, -th, 1.0, I2, "BLUE", off=(16, 18))
    # k2 as a unit vector, continued to A
    unit(sc, O, 90 - th, 1.0, K2, "BLUE", off=(-26, 6))
    sc.line(d(90 - th), A, "BLUE", 1.4, "6 4")
    # arcs of theta
    sc.arc(O, 0.55, 90, 90 - th, "GREEN", 1.7, head=True)
    sc.label(add(O, d(90 - th / 2), 0.55), "θ", "GREEN", "middle", 17, dx=-2, dy=-12)
    sc.arc(O, 0.55, 0, -th, "GREEN", 1.7, head=True)
    sc.label(add(O, d(-th / 2), 0.55), "θ", "GREEN", "middle", 17, dx=22, dy=12)
    # A, G, P and the floor
    sc.mass(A, None, r=5, col="ACC")
    sc.label(A, "A", "HEAD", "middle", 17, dx=16, dy=-8)
    sc.mass((0.0, -a), None, r=4.5, col="BLUE")
    sc.label((0.0, -a), "P", "HEAD", "middle", 17, dx=-14, dy=-12)
    sc.dashed(O, (0.0, -a))
    sc.label((0.0, -a / 2), "a", "TEXT", "start", 15, dx=8, dy=5)
    axis_in(sc, O, None, "HEAD")
    sc.label(O, J1 + " = " + J2 + " (⊗)", "HEAD", "end", 16, weight="700", dx=-14, dy=26)
    sc.label(O, "G", "HEAD", "middle", 17, dx=14, dy=26)
    # height of A above the floor
    sc.dashed(A, (3.1, A[1]))
    sc.dashed((0.0, -a), (3.1, -a))
    sc.dim((2.9, -a), (2.9, A[1]), "", off=(0, 0))
    sc.label((2.9, -1.0), "a(1 + cos θ)", "TEXT", "end", 15, dx=-8, dy=5)
    return sc


@figure("rb19-rot-phi",
        "Third Euler rotation, the spin phi of the sphere about GA.",
        r"Third rotation, by $\varphi$ about $\mathbf k_2$ (⊙): the difference between $Gx_2y_2z_2$ and a body frame. "
        r"It does not move $A$.")
def rot_phi():
    def post(sc):
        sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=22, dy=26)
        sc.mass((0.0, 0.0), None, r=3, col="ACC")
        sc.note((0.0, 0.0), "A (dot at G) lies on the axis " + K2 + ", out of the paper", "TEXT", "start", 13, dx=-100, dy=62)
    return plane_rotation(780, 600, (330, 490), 250, 35.0, (I2, J2, IB, JB), K2 + " (⊙)", ("φ", ""), None,
                          extra_post=post, out_off=(-16, 28), col="ACC")


# ------------------------------------------------------------------------------------------------ spring geometry
def _p(q):
    return p3v(q)


@figure("rb19-spring",
        "The sphere on the floor with the spring from A to C and the coordinates xi and eta of G.",
        r"Spring geometry: $\overrightarrow{AC} = -(\xi + a\sin\theta\cos\psi)\,\mathbf i - (\eta + a\sin\theta\sin\psi)\,"
        r"\mathbf j + a(1 - \cos\theta)\,\mathbf k$. $A$ is never above $C$, so the spring never pushes the sphere down.")
def spring():
    sc = Scene(900, 690, (250, 480), 118)
    a, xi, eta, psi, th = 1.0, 1.2, 2.2, math.radians(30), math.radians(50)
    O = (0.0, 0.0, 0.0)
    # floor
    sc.poly([_p((0, 0, 0)), _p((3.2, 0, 0)), _p((3.2, 4.0, 0)), _p((0, 4.0, 0))], "EDGE", 0.0, fill="EDGE", close=True,
            opacity=0.08)
    sc.poly([_p((0, 0, 0)), _p((3.2, 0, 0)), _p((3.2, 4.0, 0)), _p((0, 4.0, 0))], "EDGE", 0.9, close=True)
    for tipq, nm, off in (((3.5, 0, 0), "x", (-12, 12)), ((0, 4.5, 0), "y", (12, 6)), ((0, 0, 3.2), "z", (-12, 4))):
        sc.vec(_p(O), _p(tipq), nm, "EDGE", 1.5, name_off=off, size=17, head=9)
    sc.label(_p(O), "O", "HEAD", "middle", 17, dx=-14, dy=18)
    C = (0.0, 0.0, 2 * a)
    G = (xi, eta, a)
    Pp = (xi, eta, 0.0)
    i1 = (math.cos(psi), math.sin(psi), 0.0)
    j1 = (-math.sin(psi), math.cos(psi), 0.0)
    k2 = tuple(math.sin(th) * i1[m] + math.cos(th) * (0, 0, 1)[m] for m in range(3))
    i2 = tuple(math.cos(th) * i1[m] - math.sin(th) * (0, 0, 1)[m] for m in range(3))
    Aq = tuple(G[m] + a * k2[m] for m in range(3))
    # sphere, contact point and its coordinates on the floor
    gp = _p(G)
    sc.circle(gp, a, "HEAD", 2.0, fill="EDGE", opacity=0.10)
    sc.dashed(_p(Pp), _p((xi, 0, 0)))
    sc.dashed(_p(Pp), _p((0, eta, 0)))
    sc.label(_p((xi, eta / 2, 0)), "ξ", "TEXT", "middle", 16, dx=0, dy=-8)
    sc.label(_p((xi / 2, eta, 0)), "η", "TEXT", "middle", 16, dx=16, dy=14)
    sc.dashed(_p(G), _p(Pp))
    sc.mass(_p(Pp), None, r=4.5, col="BLUE")
    sc.label(_p(Pp), "P", "HEAD", "middle", 17, dx=-4, dy=22)
    # point C and the height a(1 - cos(theta))
    sc.mass(_p(C), None, r=4.5, col="BLUE")
    sc.label(_p(C), "C", "HEAD", "middle", 17, dx=-14, dy=-6)
    zc = Aq[2]
    sc.dashed(_p(C), _p((0, 0, zc)))
    sc.dashed(_p((0, 0, zc)), _p(Aq))
    sc.dim(_p((0.0, 0.0, zc)), _p(C), "", off=(0, 0))
    sc.label(_p((0, 0, (zc + C[2]) / 2)), "a(1 − cos θ)", "TEXT", "end", 15, dx=-12, dy=5)
    # blue basis of the second frame at G and the axis GA
    for v, nm, off, ln in ((i2, I2, (20, 14), 0.62), (j1, J2, (18, -2), 0.7)):
        sc.vec(gp, add(gp, _p(tuple(ln * q for q in v))), nm, "BLUE", 2.4, name_off=off, size=16, head=10)
    ap = _p(Aq)
    sc.vec(gp, ap, K2, "BLUE", 2.8, name_off=(-20, 16), size=17, head=11)
    sc.mass(ap, None, r=5, col="ACC")
    sc.label(ap, "A", "HEAD", "middle", 17, dx=14, dy=-8)
    sc.mass(gp, None, r=4, col="BLUE")
    sc.label(gp, "G", "HEAD", "middle", 17, dx=-16, dy=8)
    # the spring from A to C, the force at A and the height of A
    sc.spring(ap, _p(C), coils=8, amp=8.0, col="HEAD", lead=0.10, w=1.8)
    u = (_p(C)[0] - ap[0], _p(C)[1] - ap[1])
    n = math.hypot(*u)
    u = (u[0] / n, u[1] / n)
    nrm = (-u[1], u[0])
    s0 = (ap[0] - 0.22 * nrm[0], ap[1] - 0.22 * nrm[1])
    sc.vec(s0, (s0[0] + 0.75 * u[0], s0[1] + 0.75 * u[1]), None, ORANGE, 3.0, head=12)
    sc.label((s0[0] + 0.75 * u[0], s0[1] + 0.75 * u[1]), S("F", "s") + " = k AC", ORANGE, "start", 16, weight="700",
             dx=8, dy=-12)
    foot = (Aq[0], Aq[1], 0.0)
    sc.dashed(ap, _p(foot))
    sc.label(_p((foot[0], foot[1], Aq[2] * 0.5)), "a(1 + cos θ)", "TEXT", "start", 15, dx=10, dy=5)
    return sc


@figure("rb19-fbd",
        "Free-body diagram of the sphere: weight at G, spring at A, normal reaction and, on the rough plane, friction at P.",
        r"Free-body diagram. On the smooth plane only the spring has a moment about $G$ (arm $a\,\mathbf k_2$); on the rough "
        r"plane the friction adds the moment of the arm $-a\,\mathbf k$.")
def fbd():
    a, th = 2.0, 40.0
    t = math.radians(th)
    sc = Scene(860, 560, (330, 270), 90)
    O = (0.0, 0.0)
    sc.line((-3.0, -a), (3.6, -a), "EDGE", 1.6)
    for i in range(46):
        x = -3.0 + 0.14 * i + 0.08
        sc.line((x, -a), (x - 0.09, -a - 0.11), "EDGE", 0.9)
    sc.circle(O, a, "HEAD", 2.2, fill="EDGE", opacity=0.10)
    A = (a * math.sin(t), a * math.cos(t))
    # arm GA and the angle theta
    sc.dashed(O, A)
    sc.label((A[0] / 2, A[1] / 2), "a " + K2, "TEXT", "start", 16, dx=10, dy=14)
    sc.dashed(O, (0.0, 1.2))
    sc.arc(O, 0.9, 90, 90 - th, "GREEN", 1.7, head=True)
    sc.label(add(O, d(90 - th / 2), 0.9), "θ", "GREEN", "middle", 16, dx=0, dy=-8)
    # forces
    sc.vec(O, (0.0, -0.95), None, "PINK", 3.2, head=12)
    sc.label((0.0, -0.5), "Mg", "PINK", "start", 17, weight="700", dx=12, dy=5)
    sc.vec((0.0, -a), (0.0, -a + 0.95), None, "GREEN", 3.2, head=12)
    sc.label((0.0, -a + 0.5), "N", "GREEN", "start", 17, weight="700", dx=12, dy=5)
    sc.line((0.0, -a), (1.0, -a), "GREEN", 2.2, "6 4")
    sc.vec((1.0, -a), (1.35, -a), None, "GREEN", 2.2, head=10)
    sc.label((1.2, -a), S("F", "1") + " " + I1 + " (rough plane only)", "GREEN", "start", 15, dx=14, dy=-10)
    sc.note((0.0, -a - 0.55), "F" + '<tspan baseline-shift="sub" font-size="70%">2</tspan>' + " along " + "j" + '<tspan baseline-shift="sub" font-size="70%">1</tspan>' + ", normal to the paper", "TEXT", "middle", 13)
    u = (-0.6, 0.8)
    sc.vec(A, add(A, u, 1.1), S("F", "s"), ORANGE, 3.2, name_off=(-18, -4), size=17, head=12)
    sc.mass(A, None, r=5, col="ACC")
    sc.label(A, "A", "HEAD", "middle", 17, dx=16, dy=0)
    sc.mass((0.0, -a), None, r=4.5, col="BLUE")
    sc.label((0.0, -a), "P", "HEAD", "middle", 17, dx=-14, dy=-8)
    sc.mass(O, None, r=4.5, col="BLUE")
    sc.label(O, "G", "HEAD", "middle", 17, dx=-14, dy=-10)
    axis_in(sc, (-2.7, 2.3), None, "HEAD")
    sc.label((-2.7, 2.3), J2 + " (into the paper)", "HEAD", "start", 16, weight="700", dx=16, dy=5)
    return sc
