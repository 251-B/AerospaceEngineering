"""Problem RB-39: yo-yo hanging from a string wound on its inner cylinder (coordinates xi and theta; two graphs)."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb12 import plane_rotation
from figures.em_sol.rb23 import circle_pts
from figures.mech import S, Scene, bold, dot1, dot2

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I0, J0, K0 = S(I, "0"), S(J, "0"), S(K, "0")
I1, J1 = S(I, "1"), S(J, "1")
TH = 30.0
THR = math.radians(TH)
I1D = (math.cos(THR), math.sin(THR))
J1D = (-math.sin(THR), math.cos(THR))
STR = (-J1D[0], -J1D[1])                       # direction of the string, from O towards the yo-yo


def _ceiling(sc, x0, x1, y=0.0, step=0.12, up=0.11):
    """Ceiling line with hatching ticks on its upper side."""
    sc.line((x0, y), (x1, y), "HEAD", 2.4)
    x = x0 + 0.06
    while x < x1:
        sc.line((x, y), (x - up * 0.7, y + up), "EDGE", 1.0)
        x += step


# ------------------------------------------------------------------------------------------------ rb39-rot-theta
@figure("rb39-rot-theta",
        "The basis of the string, turned counterclockwise by theta from the fixed basis.",
        r"Rotation about $\mathbf k_0$ (⊙) by $\theta$; the string runs along $-\mathbf j_1$ from $O$ and $\mathbf i_1$ "
        r"is normal to it.")
def rot_theta():
    def pre(sc):
        # ceiling: left of O and beyond the tip of the axis i0 (the axis itself stands for the ceiling in between)
        _ceiling(sc, -2.5, -0.16)
        _ceiling(sc, 1.8, 2.5)
        sc.label((-1.9, 0.0), "ceiling", "TEXT", "middle", 14, italic=False, dy=24)
        # string and the downward vertical
        s = 3.0
        sc.dashed((0.0, 0.0), (0.0, -s))
        sc.line((0.0, 0.0), add((0.0, 0.0), STR, s), "HEAD", 2.4)
        sc.arc((0.0, 0.0), 1.75, -90.0, -90.0 + TH, "GREEN", 1.8, head=True)
        sc.label(add((0.0, 0.0), d(-90.0 + TH / 2), 1.75), "θ", "GREEN", "middle", 17, dx=-14, dy=14)
        sc.label(add((0.0, 0.0), STR, 1.5), "−" + J1 + " along the string", "TEXT", "start", 15, weight="700", dx=14, dy=6)
        sc.label(add((0.0, 0.0), STR, s), "string", "TEXT", "start", 14, italic=False, dx=10, dy=6)

    def post(sc):
        sc.label((0.0, 0.0), "O", "HEAD", "middle", 17, dx=14, dy=-12)
    return plane_rotation(860, 900, (400, 330), 170, TH, (I0, J0, I1, J1), K0 + " (⊙)", ("θ", ""), None,
                          extra_pre=pre, extra_post=post, out_off=(-26, 26))


# ------------------------------------------------------------------------------------------------ geometry of the yo-yo
XI, A, RR = 3.0, 0.35, 1.0
T_PT = (XI * STR[0], XI * STR[1])
C_PT = (T_PT[0] - A * I1D[0], T_PT[1] - A * I1D[1])


def _yoyo(sc, c, faint=False):
    sc.poly(circle_pts(c, RR), "HEAD", 1.6 if faint else 1.8, fill="EDGE", close=True, opacity=0.07)
    sc.poly(circle_pts(c, A), "HEAD", 2.8, fill="EDGE", close=True, opacity=0.18)


@figure("rb39-position",
        "The position of the centre C as the string segment OT plus the radius TC normal to the string.",
        r"$\mathbf r_0^C = \overrightarrow{OT} + \overrightarrow{TC} = -\xi\,\mathbf j_1 - a\,\mathbf i_1$; the triangle "
        r"$OTC$ is right-angled at $T$ because the string is tangent to the inner cylinder.")
def position():
    sc = Scene(860, 870, (250, 90), 165)
    O = (0.0, 0.0)
    _ceiling(sc, -1.4, 1.2)
    # outer disk and inner cylinder
    _yoyo(sc, C_PT)
    # triangle O-T-C
    triangle(sc, [O, T_PT, C_PT], ORANGE, 0.32)
    sc.dashed(O, C_PT)
    right_angle(sc, T_PT, 90.0 + TH, 180.0 + TH, 0.07)
    # string and vertical
    sc.dashed(O, (0.0, -XI))
    sc.line(O, T_PT, "HEAD", 2.4)
    sc.arc(O, 1.1, -90.0, -90.0 + TH, "GREEN", 1.8, head=True)
    sc.label(add(O, d(-90.0 + TH / 2), 1.1), "θ", "GREEN", "middle", 17, dx=-14, dy=12)
    sc.label(add(O, STR, XI * 0.45), "ξ", "HEAD", "start", 18, dx=14, dy=-2)
    # radius TC
    sc.line(C_PT, T_PT, "HEAD", 2.4)
    sc.label(add(C_PT, I1D, A / 2), "a", "HEAD", "middle", 16, dx=4, dy=26)
    # unit vectors at T
    sc.vec(T_PT, add(T_PT, I1D, 0.5), I1, "BLUE", 2.8, name_off=(10, 24), size=17, head=11)
    sc.vec(T_PT, add(T_PT, J1D, 0.55), J1, "BLUE", 2.8, name_off=(-18, -4), size=17, head=11)
    for p, nm, off in ((T_PT, "T", (16, 16)), (C_PT, "C", (-16, 20))):
        sc.mass(p, None, r=4.5, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.dotp(O, 4.0)
    sc.label(O, "O", "HEAD", "middle", 17, dx=-14, dy=-8)
    # spin of the yo-yo and the no-slip note
    sc.spin(C_PT, 0.66, 205.0, 335.0, "φ̇", "GREEN", name_r=0.84)
    sc.note((C_PT[0], C_PT[1] - RR - 0.38), "string unwinds without slip at T", "TEXT", "middle", 14)
    sc.note((C_PT[0], C_PT[1] - RR - 0.72), "R = 1 (outer disks), a = 0.35 (inner cylinder)", "TEXT", "middle", 13)
    axis_out(sc, (-0.95, -1.2), None, "HEAD")
    sc.label((-0.95, -1.2), K0 + " (⊙)", "HEAD", "start", 16, weight="700", dx=16, dy=5)
    return sc


# ------------------------------------------------------------------------------------------------ rb39-fbd
@figure("rb39-fbd",
        "Free-body diagram of the yo-yo: its weight at C and the string tension at the tangent point T.",
        r"Free-body diagram. The tension $F\,\mathbf j_1$ acts at $T$, at the arm $a\,\mathbf i_1$ from $C$, and gives the "
        r"counterclockwise torque $aF\,\mathbf k_0$.")
def fbd():
    sc = Scene(820, 840, (400, 520), 190)
    C = (0.0, 0.0)
    T = (A * I1D[0], A * I1D[1])
    _yoyo(sc, C)
    # string: stub, tension and the faint line towards O
    far = add(T, J1D, 2.45)
    sc.line(T, add(T, J1D, 1.1), "HEAD", 2.0)
    sc.vec(T, add(T, J1D, 1.5), None, "PINK", 3.2, head=12)
    sc.label(add(T, J1D, 1.5), "F", "PINK", "start", 18, weight="700", dx=14, dy=4)
    sc.line(add(T, J1D, 1.5), far, "EDGE", 1.2, "6 5")
    sc.vec(add(T, J1D, 2.2), far, None, "EDGE", 1.4, head=9)
    sc.label(far, "to O", "TEXT", "start", 15, italic=False, dx=12, dy=4)
    # weight
    sc.vec(C, (0.0, -0.95), "mg", "PINK", 3.2, name_off=(24, 6), size=18, head=12)
    # arm C-T as a dimension offset on the side of -j1
    off = (-0.26 * J1D[0], -0.26 * J1D[1])
    sc.dim(add(C, off), add(T, off), "a " + I1, off=(30, 22))
    sc.dashed(C, add(C, off, 1.15))
    sc.dashed(T, add(T, off, 1.15))
    # body basis at C
    sc.vec(C, add(C, I1D, 0.62), I1, "BLUE", 2.6, name_off=(20, -4), size=17, head=11)
    sc.vec(C, add(C, J1D, 0.62), J1, "BLUE", 2.6, name_off=(-18, -4), size=17, head=11)
    # torque
    sc.spin(C, 0.84, 112.0, 242.0, "", "PINK")
    sc.label(add(C, d(177.0), 0.84), "M" + S("", "C") + " = aF", "PINK", "end", 17, weight="700", dx=-46, dy=5)
    for p, nm, o in ((C, "C", (-18, 22)), (T, "T", (16, 20))):
        sc.mass(p, None, r=4.5, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 17, dx=o[0], dy=o[1])
    sc.note((0.0, -1.38), "R = 1, a = 0.35, θ = 30°", "TEXT", "middle", 13)
    return sc


# ------------------------------------------------------------------------------------------------ the two graphs
def _axes(sc, Q, xmax, ymax, xticks, yticks, xfmt, yfmt, xname, yname, x0=0.0):
    sc.vec(Q(x0, 0), Q(xmax, 0), None, "EDGE", 1.6, head=9)
    sc.vec(Q(x0, 0), Q(x0, ymax), None, "EDGE", 1.6, head=9)
    for t in xticks:
        sc.line(Q(t, 0), (Q(t, 0)[0], Q(t, 0)[1] - 0.0), "EDGE", 1.2)
        sc.line(Q(t, 0), Q(t, -0.012 * ymax / 0.8), "EDGE", 1.2)
        sc.label(Q(t, 0), xfmt(t), "TEXT", "middle", 14, italic=False, dy=24)
    for v in yticks:
        sc.line(Q(x0, v), Q(xmax, v), "EDGE", 0.6, "2 4")
        sc.label(Q(x0, v), yfmt(v), "TEXT", "end", 14, italic=False, dx=-8, dy=5)
    sc.label(Q(xmax, 0), xname, "TEXT", "end", 16, dy=48)
    sc.label(Q(x0, ymax), yname, "TEXT", "start", 16, dx=12, dy=-8)


@figure("rb39-graph-accel",
        "Graph of the initial acceleration of the yo-yo, decreasing from two thirds of g at R equal to a towards zero.",
        r"$\ddot\xi_0/g = 2/(2 + (R/a)^2)$, with $\theta$ fixed at zero: the larger the disks compared with the axle, "
        r"the slower the fall.")
def graph_accel():
    sx, sy = 100.0, 620.0
    sc = Scene(960, 720, (110, 620), 1.0)
    x0 = 0.5

    def Q(x, y):
        return ((x - x0) * sx, y * sy)
    _axes(sc, Q, 8.4, 0.88, range(1, 9), (0.2, 0.4, 0.6, 0.8), lambda t: f"{t}", lambda v: f"{v:.1f}",
          "R / a", S(dot2("ξ"), "0") + " / g", x0=x0)
    # asymptote 2/x^2 (dashed grey) and the exact curve
    xs = [2.5 + 5.5 * i / 100 for i in range(101)]
    sc.poly([Q(x, 2.0 / x ** 2) for x in xs], "EDGE", 2.2, "7 5")
    xs2 = [1.0 + 7.0 * i / 160 for i in range(161)]
    sc.poly([Q(x, 2.0 / (2.0 + x * x)) for x in xs2], "BLUE", 3.4)
    for x, y, nm, dx, dy in ((1.0, 2.0 / 3.0, "2g/3", 12, -14), (2.0, 1.0 / 3.0, "g/3", 12, -14), (4.0, 1.0 / 9.0, "g/9", 12, -14)):
        sc.mass(Q(x, y), None, r=5, col="BLUE")
        sc.label(Q(x, y), nm, "BLUE", "start", 17, weight="700", dx=dx, dy=dy)
        sc.dashed(Q(x, 0), Q(x, y))
    sc.label(Q(3.2, 2.0 / (2.0 + 3.2 ** 2)), "2g / (2 + (R/a)²)", "BLUE", "start", 16, weight="700", dx=18, dy=-30)
    sc.label(Q(5.0, 2.0 / 25.0), "2g a² / R²  (large R/a)", "TEXT", "start", 15, dx=22, dy=-40)
    return sc


@figure("rb39-graph-omega",
        "Graph of the minimum initial spin, decreasing like one over the square root of R.",
        r"Minimum initial spin to climb from $\xi_0 = 2R$ to the origin, for $a \ll R$: "
        r"$\Omega_{0,\min} \approx \sqrt{8g/R}$.")
def graph_omega():
    sx, sy = 190.0, 80.0
    sc = Scene(960, 740, (110, 660), 1.0)

    def Q(x, y):
        return (x * sx, y * sy)
    _axes(sc, Q, 4.3, 7.4, (0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4), (1, 2, 3, 4, 5, 6, 7),
          lambda t: f"{t:g}", lambda v: f"{v}", "R  (units of " + S("R", "ref") + ")",
          S("Ω", "0,min") + " / √(g/" + S("R", "ref") + ")")
    xs = [0.2 + 3.8 * i / 200 for i in range(201)]
    sc.poly([Q(x, math.sqrt(8.0 / x)) for x in xs], "BLUE", 3.4)
    sc.mass(Q(1.0, math.sqrt(8.0)), None, r=5, col="BLUE")
    sc.dashed(Q(1.0, 0), Q(1.0, math.sqrt(8.0)))
    sc.dashed(Q(0, math.sqrt(8.0)), Q(1.0, math.sqrt(8.0)))
    sc.label(Q(1.0, math.sqrt(8.0)), "√8 = 2.83", "BLUE", "start", 17, weight="700", dx=14, dy=-12)
    sc.label(Q(2.0, math.sqrt(4.0)), S("Ω", "0,min") + " ≈ √(8g/R),  a ≪ R", "BLUE", "start", 17, weight="700", dx=14, dy=-34)
    return sc
