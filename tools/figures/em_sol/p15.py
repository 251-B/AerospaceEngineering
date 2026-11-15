"""Problem 15: sphere falling in a fluid at rest with Stokes drag (axis i pointing down)."""
from figures.em_solutions import axis_out, figure
from figures.mech import S, Scene, bold, dot1

ORANGE = "#f97316"          # drag (no kit token: a fixed colour, readable on every palette)
RED = "#ef4444"             # weight
PURPLE = "#8b5cf6"          # buoyancy
FLUID = "#94a3b8"           # fluid at rest: very light blue-grey fill


def _r0p():
    return bold("r") + '<tspan baseline-shift="super" font-size="70%">P</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>'


def _xdot():
    return dot1("x")


@figure("p15-fall-axis",
        "The sphere P falling along the vertical through the release point O, with the downward axis i and the distance fallen x.",
        r"Plane of the fall. The axis $\mathbf i$ points down, so the distance fallen $x$ and the velocity $\dot x$ are "
        r"positive during the whole motion; $\mathbf k$ points out of the paper.")
def fall_axis():
    W, H, K = 580, 480, 56
    sc = Scene(W, H, (280, 70), K)
    # the fluid at rest fills the drawing
    sc.poly([(-280 / K, 70 / K), ((W - 280) / K, 70 / K), ((W - 280) / K, (70 - H) / K), (-280 / K, (70 - H) / K)],
            FLUID, 0.0, fill=FLUID, close=True, opacity=0.16)
    sc.label(((W - 280 - 10) / K, 0.78), "fluid at rest, density " + S("ρ", "0") + ", viscosity μ", "TEXT", "end", 15)
    # line of fall
    sc.line((0.0, 0.0), (0.0, -6.7), "EDGE", 1.2, "6 4")
    # basis at O
    axis_out(sc, (0.0, 0.0), bold("k"), off=(-30, -16))
    sc.vec((0.0, 0.0), (0.0, -1.2), bold("i"), "BLUE", 2.6, name_off=(-14, 4), size=17, head=11)
    sc.vec((0.0, 0.0), (1.2, 0.0), bold("j"), "BLUE", 2.6, name_off=(0, 24), size=17, head=11)
    # sphere at release
    sc.circle((0.0, 0.0), 0.35, "HEAD", 1.3, "3 3")
    sc.label((0.0, 0.0), "t = 0, v = 0", "TEXT", "end", 14, dx=-24, dy=48)
    # sphere P
    sc.circle((0.0, -5.0), 0.35, "HEAD", 1.8, fill="HEAD", opacity=0.35)
    sc.label((0.0, -5.0), "P (radius r, density 2" + S("ρ", "0") + ")", "HEAD", "end", 17, dx=-26, dy=5)
    # position vector, slightly right of the line of fall
    xr = 0.15
    sc.vec((xr, 0.0), (xr, -4.64), None, "HEAD", 2.2, head=10)
    sc.label((xr, -2.5), _r0p() + " = x " + bold("i"), "HEAD", "start", 17, dx=14, dy=5)
    # dimension line of x
    xd = 2.4
    sc.line((xd, 0.0), (xd, -5.0), "EDGE", 1.1)
    for y in (0.0, -5.0):
        sc.line((xd - 0.12, y), (xd + 0.12, y), "EDGE", 1.4)
    sc.label((xd, -2.5), "x", "TEXT", "start", 17, dx=12, dy=5)
    # velocity
    xv = 0.35 + 0.5
    sc.vec((xv, -5.0), (xv, -6.4), None, "GREEN", 2.8, head=11)
    sc.label((xv, -6.4), "v = " + _xdot() + " " + bold("i"), "GREEN", "start", 16, dx=12, dy=5)
    return sc


@figure("p15-fbd",
        "Free-body diagram of the sphere with the weight down and the buoyancy and the drag up.",
        r"Forces on the falling sphere. The buoyancy cancels half of the weight; the drag, opposite to the downward "
        r"velocity, grows linearly with the speed until it balances the other half at the terminal velocity.")
def fbd():
    K = 70
    sc = Scene(560, 430, (275, 135), K)
    O = (0.0, 0.0)
    sc.circle(O, 1.0, "HEAD", 2.0, fill="HEAD", opacity=0.14)
    # weight
    sc.vec(O, (0.0, -3.0), None, RED, 3.0, head=12)
    sc.label((0.0, -3.0), "m g " + bold("i"), RED, "start", 17, dx=14, dy=5)
    # buoyancy (half of the weight)
    sc.vec((-0.25, 0.0), (-0.25, 1.5), None, PURPLE, 3.0, head=12)
    sc.label((-0.25, 1.5), "−" + S("ρ", "0") + " V g " + bold("i"), PURPLE, "end", 17, dx=-12, dy=5)
    # drag at v = 2/3 of the terminal velocity
    sc.vec((0.25, 0.0), (0.25, 1.0), None, ORANGE, 3.0, head=12)
    sc.label((0.25, 1.0), "−6π μ r " + dot1("x") + " " + bold("i"), ORANGE, "start", 17, dx=14, dy=-10)
    sc.dotp(O, 4.0)
    # velocity beside the sphere
    sc.vec((2.0, 0.5), (2.0, -0.7), None, "GREEN", 2.2, head=10)
    sc.label((2.0, -0.7), dot1("x") + " > 0", "GREEN", "middle", 16, dy=24)
    # reference axes in the lower left corner
    C = (-2.9, -1.0)
    axis_out(sc, C, bold("k"), off=(-16, -12))
    sc.vec(C, (C[0], C[1] - 0.8), bold("i"), "BLUE", 2.4, name_off=(-14, 4), size=16, head=10)
    sc.vec(C, (C[0] + 0.8, C[1]), bold("j"), "BLUE", 2.4, name_off=(0, 22), size=16, head=10)
    sc.note((0.0, -3.9), "free sphere: no reaction; inertial frame: no inertia forces", "TEXT", "middle", 13)
    return sc
