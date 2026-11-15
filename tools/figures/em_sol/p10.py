"""Problem 10: particle on the axis Ox under F = -c x^3 i (quartic well)."""
from figures.em_solutions import axis_out, figure, fixed_axis
from figures.mech import S, Scene, bold

PURPLE = "#8b5cf6"          # normal resultant R_perp (no kit token: a fixed colour, readable on every palette)

A = 4.0                     # drawn value of a
XP = -2.4                   # drawn abscissa of P


def _i():
    return bold("i")


def _r0p():
    return bold("r") + '<tspan baseline-shift="super" font-size="70%">P</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>'


@figure("p10-axis-basis",
        "The axis Ox with the fixed basis i, j, k, the particle P at negative abscissa and the force pulling it towards O.",
        r"Fixed basis $\mathcal B_0$ ($\mathbf k$ out of the paper) and position vector $\mathbf r_0^P = x\,\mathbf i$; "
        r"for negative $x$ the force $-c x^3\mathbf i$ points along $+\mathbf i$, towards $O$.")
def axis_basis():
    sc = Scene(680, 300, (340, 140), 50)
    O = (0.0, 0.0)
    sc.line((-5.9, 0.0), (5.9, 0.0), "EDGE", 1.2)
    for x, nm in ((-A, "−a"), (A, "+a")):
        sc.line((x, -0.12), (x, 0.12), "EDGE", 1.4)
        sc.label((x, 0.0), nm, "TEXT", "middle", 16, dy=26)
    fixed_axis(sc, O, 0, 1.4, bold("i"), off=(2, -12))
    fixed_axis(sc, O, 90, 1.4, bold("j"), off=(14, 4))
    axis_out(sc, O, bold("k"), off=(22, -14))
    # position vector (black), drawn parallel to the axis a little below it
    yr = -0.55
    sc.dashed((0.0, 0.0), (0.0, yr))
    sc.dashed((XP, 0.0), (XP, yr))
    sc.vec((0.0, yr), (XP, yr), None, "HEAD", 2.2, head=10)
    sc.label((XP / 2, yr), _r0p(), "HEAD", "middle", 17, dy=22)
    # force on the particle
    sc.vec((XP, 0.0), (XP + 2.0, 0.0), None, "PINK", 2.8, head=11)
    sc.label((XP + 1.0, 0.0), bold("F") + " = −c x" + S("", "", "3") + " " + _i(), "PINK", "middle", 16, dy=-16)
    sc.dotp((XP, 0.0), 6.0)
    sc.label((XP, 0.0), "P", "HEAD", "middle", 17, dx=-14, dy=-12)
    sc.label(O, "O", "HEAD", "middle", 17, dx=14, dy=26)
    # bracket x < 0
    yb = -1.3
    sc.line((0.0, yb + 0.12), (0.0, yb - 0.12), "EDGE", 1.1)
    sc.line((XP, yb + 0.12), (XP, yb - 0.12), "EDGE", 1.1)
    sc.line((0.0, yb), (XP, yb), "EDGE", 1.1, "5 4")
    sc.label((XP / 2, yb), "x < 0", "TEXT", "middle", 16, dy=24)
    return sc


@figure("p10-fbd",
        "Free-body diagram of the particle: the applied force along the axis and the resultant of the normal forces.",
        r"Free-body diagram. Only $\mathbf F$ has a component along $\mathbf i$; the normal resultant "
        r"$\mathbf R_\perp$ balances to zero.")
def fbd():
    sc = Scene(640, 320, (270, 205), 60)
    O = (0.0, 0.0)
    # the smooth guide: two thin parallel lines
    sc.line((-3.4, 0.16), (3.0, 0.16), "EDGE", 1.4)
    sc.line((-3.4, -0.16), (3.0, -0.16), "EDGE", 1.4)
    sc.vec(O, (2.5, 0.0), None, "PINK", 2.8, head=11)
    sc.label((1.25, 0.0), bold("F") + " = −c x" + S("", "", "3") + " " + _i(), "PINK", "middle", 16, dy=-22)
    sc.vec(O, (0.0, 1.5), None, PURPLE, 2.8, head=11)
    sc.label((0.0, 1.5), bold("R") + S("", "⊥") + " = " + bold("R") + S("", "y") + " " + bold("j") + " + " + bold("R")
             + S("", "z") + " " + bold("k"), PURPLE, "start", 16, dx=14, dy=5)
    sc.mass(O, None, r=8.5, col="HEAD")
    sc.label(O, "P", "HEAD", "middle", 17, dx=-16, dy=-14)
    sc.note((3.6, -1.6), "S₀ inertial: no inertia forces", "TEXT", "end", 13)
    # basis at a corner
    C = (-3.9, -1.5)
    fixed_axis(sc, C, 0, 1.0, bold("i"), off=(2, -12))
    fixed_axis(sc, C, 90, 1.0, bold("j"), off=(14, 4))
    axis_out(sc, (-3.1, -0.7), bold("k"), off=(18, 5))
    return sc


@figure("p10-potential",
        "The quartic well V0 = c x^4/4 with the energy level of the release and its two turning points.",
        r"Potential well and energy level of the release. The motion is allowed where $V_0 \le E_0$, between $-a$ and "
        r"$+a$; the kinetic energy is largest at the origin.")
def potential():
    SY = 2.25                      # world height per unit of V0 (c = a = 1)
    sc = Scene(800, 440, (370, 350), 200)
    E = 0.25
    V = lambda x: x ** 4 / 4.0
    sc.vec((-1.5, 0.0), (1.6, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((1.6, 0.0), "x", "TEXT", "middle", 17, dx=12, dy=5)
    sc.vec((0.0, -0.1), (0.0, 1.56), None, "EDGE", 1.4, head=8)
    sc.label((0.0, 1.56), S("V", "0") + "(x)", "TEXT", "start", 17, dx=12, dy=2)
    # allowed interval on the x axis
    sc.poly([(-1.0, -0.035), (1.0, -0.035), (1.0, 0.035), (-1.0, 0.035)], "ACC", 0.0, fill="ACC", close=True, opacity=0.40)
    # energy level
    sc.line((-1.3, SY * E), (1.3, SY * E), "ACC", 2.0, "7 4")
    sc.label((1.3, SY * E), S("E", "0") + " = c a" + S("", "", "4") + " / 4", "ACC", "start", 16, dx=10, dy=5)
    # potential curve
    sc.curve(lambda x: (x, SY * V(x)), -1.25, 1.25, 160, col="BLUE", w=2.8)
    for x, nm, sub in ((-1.0, "−a", "release"), (1.0, "+a", "next stop")):
        sc.line((x, SY * E), (x, 0.0), "EDGE", 1.2, "4 4")
        sc.dotp((x, SY * E), 4.5, "BLUE")
        sc.label((x, 0.0), nm, "TEXT", "middle", 16, dy=24)
        sc.note((x, 0.0), "(" + sub + ")", "TEXT", "middle", 12, dy=40)
    # kinetic energy at the origin
    sc.vec((0.0, 0.0), (0.0, SY * E), None, "ACC", 2.2, head=9)
    sc.vec((0.0, SY * E), (0.0, 0.0), None, "ACC", 2.2, head=9)
    sc.label((0.0, SY * E / 2), S("T", "0") + " = c a" + S("", "", "4") + " / 4", "ACC", "start", 15, dx=12, dy=-2)
    sc.note((0.0, SY * E / 2), "(largest)", "ACC", "start", 12, dx=12, dy=16)
    # sense of the first motion
    sc.vec((-0.6, -0.30), (0.6, -0.30), None, "GREEN", 2.2, head=10)
    sc.note((0.0, -0.30), "first motion", "GREEN", "middle", 12, dy=18)
    return sc
