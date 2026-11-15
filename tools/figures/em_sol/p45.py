"""Problem 45: disk of centre C held by a spring to O and driven at angular rate omega, centre of mass G at distance l."""
import math

from figures.em_solutions import _dir, axis_out, fixed_axis, figure, right_angle, triangle
from figures.mech import S, Scene, bold

DARKBLUE = "#1d4ed8"        # unbalance segment CG (no kit token: a fixed colour, readable on every palette)
PURPLE = "#8b5cf6"          # reaction
BROWN = "#a16207"           # motor couple
YELLOW = "#eab308"          # right triangles

OM = "ω"


def _vec(name, sup, sub="0"):
    """Bold vector name with the sup/sub-script of the course: r_0^P."""
    return bold(name) + f'<tspan baseline-shift="super" font-size="70%">{sup}</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">{sub}</tspan>'


def _coord(name, sup):
    """x_0^C."""
    return name + f'<tspan baseline-shift="super" font-size="70%">{sup}</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>'


def _matrix(sc, x0, y0, rows, colw, rowh=0.36):
    sc.label((x0, y0 - 1.5 * rowh), "[" + S("", "0") + "R" + S("", "1") + "] =", "HEAD", "end", 17, dx=-10, dy=5)
    h = 3 * rowh
    w = 3 * colw
    for x, s in ((x0, 1), (x0 + w, -1)):
        sc.line((x, y0), (x, y0 - h), "HEAD", 1.6)
        sc.line((x, y0), (x + s * 0.07, y0), "HEAD", 1.6)
        sc.line((x, y0 - h), (x + s * 0.07, y0 - h), "HEAD", 1.6)
    for i, row in enumerate(rows):
        for j, s in enumerate(row):
            sc.label((x0 + (j + 0.5) * colw, y0 - (i + 0.5) * rowh), s, "HEAD", "middle", 16, italic=False, dy=5)


CX, CY = 2.2, 1.6            # centre of the disk C
RD = 1.6                     # drawn radius of the disk
LL = 0.9                     # unbalance l (exaggerated)
WT = 60.0                    # drawn value of omega t in the main plane


def _gpos():
    return (CX + LL * math.cos(math.radians(WT)), CY + LL * math.sin(math.radians(WT)))


@figure("p45-disk-plane",
        "The disk of centre C held by a spring to O, with the centre of mass G at distance l along a direction at angle omega t.",
        r"Main plane. The position vector of $G$ is built as $\overrightarrow{OC}$ plus the unbalance $\overrightarrow{CG}$, "
        r"whose right triangle has hypotenuse $\ell$, horizontal leg $\ell\cos\omega t$ and vertical leg $\ell\sin\omega t$.")
def disk_plane():
    K = 108
    sc = Scene(640, 520, (110, 410), K)
    O = (0.0, 0.0)
    C = (CX, CY)
    G = _gpos()
    # disk
    sc.circle(C, RD, "HEAD", 1.8, fill="HEAD", opacity=0.10)
    # axes
    fixed_axis(sc, O, 0, 4.3, S(bold("i"), "0"), off=(16, 5))
    fixed_axis(sc, O, 90, 3.5, S(bold("j"), "0"), off=(18, 4))
    axis_out(sc, O, S(bold("k"), "0"), off=(-22, 22))
    # dashed projections of C
    sc.dashed(C, (CX, 0.0))
    sc.dashed(C, (0.0, CY))
    sc.label((CX, 0.0), _coord("x", "C"), "TEXT", "middle", 16, dy=24)
    sc.label((0.0, CY), _coord("y", "C"), "TEXT", "end", 16, dx=-12, dy=5)
    # spring on the line O-C
    sc.spring(O, C, coils=8, amp=7.0, col="HEAD", lead=0.10)
    nx, ny = -(CY) / math.hypot(CX, CY), CX / math.hypot(CX, CY)       # unit normal, up-left
    # position vectors: r_0^G on its own line, r_0^C drawn a little below the spring
    sc.vec(O, (G[0] - 0.12 * math.cos(math.atan2(G[1], G[0])), G[1] - 0.12 * math.sin(math.atan2(G[1], G[0]))), None, "HEAD", 2.2, head=10)
    off = 0.30
    ux, uy = CX / math.hypot(CX, CY), CY / math.hypot(CX, CY)
    tail = (-nx * off, -ny * off)
    head = (C[0] - nx * off - 0.10 * ux, C[1] - ny * off - 0.10 * uy)
    sc.dashed(O, tail)
    sc.dashed(C, (C[0] - nx * off, C[1] - ny * off))
    sc.vec(tail, head, None, "HEAD", 2.2, head=10)
    sc.label((G[0] / 2, G[1] / 2), _vec("r", "G"), "HEAD", "end", 17, dx=-10, dy=-8)
    sc.label((CX / 2 - nx * off, CY / 2 - ny * off), _vec("r", "C"), "HEAD", "start", 17, dx=10, dy=22)
    sc.label((CX / 2 + 0.05, CY / 2 + 0.05), "k", "TEXT", "end", 17, dx=-4, dy=-10)
    # unbalance segment, reference line, angle, right triangle
    cw, sw = LL * math.cos(math.radians(WT)), LL * math.sin(math.radians(WT))
    triangle(sc, [C, (CX + cw, CY), G], YELLOW, 0.30)
    sc.dashed(C, (CX + 1.3, CY))
    sc.dashed(G, (CX + cw, CY))
    sc.line(C, G, DARKBLUE, 3.0)
    sc.dotp(C, 4.0)
    sc.dotp(G, 5.0, DARKBLUE)
    sc.arc(C, 0.34, 0, WT, "GREEN", 1.6)
    sc.label((CX + 0.62 * math.cos(math.radians(20)), CY + 0.62 * math.sin(math.radians(20))), OM + "t", "GREEN", "middle", 16, dy=5)
    sc.label((CX + cw / 2 + 0.28, CY), "ℓ cos " + OM + "t", "TEXT", "middle", 15, dy=22)
    sc.label((CX + cw, CY + sw / 2), "ℓ sin " + OM + "t", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((CX + cw / 2, CY + sw / 2), "ℓ", DARKBLUE, "end", 17, dx=-8, dy=-6)
    sc.label(G, "G", DARKBLUE, "start", 17, dx=10, dy=-6)
    sc.label(C, "C", "HEAD", "end", 17, dx=-14, dy=-10)
    return sc


@figure("p45-rotation-view",
        "View along k0 of the fixed axes and of the disk axes turned by omega t counterclockwise.",
        r"Rotation of the disk basis about $\mathbf k_0$ (out of the paper). The leg of $\mathbf j_1$ along $-\mathbf i_0$ is the "
        r"origin of the minus sign in the first row of $[{}_0R_1]$.")
def rotation_view():
    K = 80
    sc = Scene(780, 420, (190, 250), K)
    O = (0.0, 0.0)
    a = 40.0
    u = 1.6
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    triangle(sc, [O, (u * c, 0.0), (u * c, u * s)], YELLOW, 0.22)
    triangle(sc, [O, (0.0, u * c), (-u * s, u * c)], YELLOW, 0.22)
    right_angle(sc, (u * c, 0.0), 180, 90, 0.12)
    right_angle(sc, (0.0, u * c), 0, 270, 0.12)
    fixed_axis(sc, O, 0, 2.0, S(bold("i"), "0"), off=(16, 5))
    fixed_axis(sc, O, 90, 2.0, S(bold("j"), "0"), off=(0, -10))
    i1 = (2.0 * c, 2.0 * s)
    j1 = (-2.0 * s, 2.0 * c)
    sc.vec(O, i1, S(bold("i"), "1"), "BLUE", 2.6, name_off=(18, -6), size=17, head=11)
    sc.vec(O, j1, S(bold("j"), "1"), "BLUE", 2.6, name_off=(-18, -6), size=17, head=11)
    sc.arc(O, 0.7, 0, a, "GREEN", 1.8, head=True)
    sc.label((1.05 * math.cos(math.radians(a / 2)), 1.05 * math.sin(math.radians(a / 2))), OM + "t", "GREEN", "middle", 16, dy=5)
    sc.arc(O, 0.7, 90, 90 + a, "GREEN", 1.8, head=True)
    sc.label((1.1 * math.cos(math.radians(90 + a / 2)), 1.1 * math.sin(math.radians(90 + a / 2))), OM + "t", "GREEN", "middle", 16, dy=5)
    sc.dashed((u * c, u * s), (u * c, 0.0))
    sc.dashed((-u * s, u * c), (0.0, u * c))
    sc.label((0.95, 0.0), "cos " + OM + "t", "TEXT", "middle", 15, dy=22)
    sc.label((u * c, u * s / 2), "sin " + OM + "t", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((0.0, u * c * 0.86), "cos " + OM + "t", "TEXT", "start", 15, dx=10, dy=5)
    sc.label((-u * s / 2, u * c), "sin " + OM + "t", "TEXT", "middle", 15, dy=-10)
    sc.note((-u * s / 2, u * c), "(−sin " + OM + "t " + S(bold("i"), "0") + ")", "TEXT", "middle", 12, dy=-28)
    sc.label((0.40, 0.58), "1", "TEXT", "middle", 15)
    sc.label((-u * s / 2 - 0.10, u * c / 2 + 0.10), "1", "TEXT", "end", 15, dx=-8, dy=0)
    # k0 out of the paper and the counterclockwise rotation about it
    axis_out(sc, O, None)
    sc.label(O, S(bold("k"), "0"), "HEAD", "end", 17, dx=-18, dy=6)
    sc.arc(O, 0.55, 225, 345, "GREEN", 1.8, head=True)
    sc.label((0.0, -0.55), OM + " " + S(bold("k"), "0"), "GREEN", "middle", 16, weight="700", dy=26)
    _matrix(sc, 3.2, 2.6, (("cos " + OM + "t", "−sin " + OM + "t", "0"), ("sin " + OM + "t", "cos " + OM + "t", "0"), ("0", "0", "1")), 0.85)
    return sc


@figure("p45-free-body",
        "Free-body diagram of the disk: the spring force at C, the reaction normal to the plane and the motor couple.",
        r"External actions on the disk. Only the spring force $-k\,\mathbf r_0^C$ has a component in the plane; the reaction "
        r"$R_z\mathbf k_0$ is normal to it and the motor couple has zero resultant, so neither enters the equation of $G$ in the plane.")
def free_body():
    K = 100
    sc = Scene(720, 480, (130, 370), K)
    C = (CX, CY)
    G = _gpos()
    sc.circle(C, RD, "HEAD", 2.0, fill="HEAD", opacity=0.10)
    sc.line(C, G, DARKBLUE, 2.4)
    sc.dotp(C, 4.0)
    sc.label(C, "C", "HEAD", "start", 17, dx=8, dy=22)
    # spring force at C, pointing to O
    d = (-CX / math.hypot(CX, CY), -CY / math.hypot(CX, CY))
    tip = (CX + 1.5 * d[0], CY + 1.5 * d[1])
    sc.vec(C, tip, None, "PINK", 3.0, head=12)
    sc.label(((CX + tip[0]) / 2, (CY + tip[1]) / 2), "−k " + _vec("r", "C"), "PINK", "end", 17, dx=-10, dy=-16)
    # reaction at G: out of the paper
    axis_out(sc, G, None, col=PURPLE, r_px=10)
    sc.dotp(G, 2.6, PURPLE)
    sc.line(G, (RD + CX + 0.25, G[1]), PURPLE, 1.0)
    sc.label((CX + RD + 0.3, G[1]), "R = " + S("R", "z") + " " + S(bold("k"), "0"), PURPLE, "start", 17, dx=4, dy=5)
    sc.note((CX + RD + 0.3, G[1]), "(normal to the plane)", PURPLE, "start", 13, dx=4, dy=22)
    # motor couple
    sc.arc(C, 0.5, 250, 540, BROWN, 2.2, head=True)
    sc.label((CX, CY - 0.95), "motor couple (zero resultant)", BROWN, "middle", 16, dy=5)
    sc.label(G, "G", DARKBLUE, "start", 17, dx=-24, dy=-10)
    # reference axes
    R0 = (-0.3, -0.4)
    fixed_axis(sc, R0, 0, 0.9, S(bold("i"), "0"), off=(14, 5))
    fixed_axis(sc, R0, 90, 0.9, S(bold("j"), "0"), off=(0, -10))
    axis_out(sc, R0, None)
    sc.label(R0, S(bold("k"), "0"), "HEAD", "end", 15, dx=-14, dy=18)
    sc.note((CX, -0.95), "weight neglected; inertial frame: no inertia forces", "TEXT", "middle", 13)
    return sc


@figure("p45-sub-super",
        "Positions of O, C and G on one line below and above the natural frequency.",
        r"Steady whirl below and above the natural frequency. Below it $C$ lies between $O$ and $G$; above it $G$ lies "
        r"between $O$ and $C$, so $|OC| \gt |OG|$, with ratio $m\omega^2/k$.")
def sub_super():
    K = 50
    sc = Scene(680, 440, (330, 225), K)
    ang = math.radians(30.0)
    u = (math.cos(ang), math.sin(ang))
    nrm = (-u[1], u[0])
    L = 1.6
    panels = (
        (-3.5, "ω < ω" + S("", "0") + "  (ω = 0.6 ω" + S("", "0") + ")", 0.5625 * L, 1.5625 * L, +1),
        (3.5, "ω > ω" + S("", "0") + "  (ω = 1.5 ω" + S("", "0") + ")", 1.8 * L, 0.8 * L, -1),
    )
    for cx, title, oc, og, sgn in panels:
        O = (cx, 0.0)
        at = lambda r: (O[0] + sgn * r * u[0], O[1] + sgn * r * u[1])
        sc.label((cx, 3.55), title, "TEXT", "middle", 16, italic=False)
        # circles of radius |OC| and |OG|
        sc.circle(O, oc, "EDGE", 1.2, "4 3")
        sc.circle(O, og, "EDGE", 1.2, "4 3")
        # the instantaneous line along i1
        R = max(oc, og) + 0.35
        sc.line((O[0] - R * u[0] * 0.0, O[1]), (O[0] + sgn * R * u[0], O[1] + sgn * R * u[1]), "EDGE", 1.0, "6 4")
        C, G = at(oc), at(og)
        sc.line(C, G, DARKBLUE, 3.4)
        sc.dotp(O, 4.0)
        sc.dotp(C, 5.0, "HEAD")
        sc.dotp(G, 5.0, DARKBLUE)
        sc.label(O, "O", "HEAD", "middle", 17, dx=-12, dy=22)
        sc.label(C, "C", "HEAD", "middle", 17, dx=-nrm[0] * 0 + 14, dy=-16)
        sc.label(G, "G", DARKBLUE, "middle", 17, dx=14, dy=-16)
        mid = ((C[0] + G[0]) / 2, (C[1] + G[1]) / 2)
        sc.label(mid, "ℓ", DARKBLUE, "middle", 17, dx=-4, dy=26)
        # radii, labelled outside their circles
        for rr, nm, a_deg in ((oc, "|OC|", -35.0), (og, "|OG|", -78.0)):
            ar = math.radians(a_deg)
            e = (O[0] + rr * math.cos(ar), O[1] + rr * math.sin(ar))
            sc.line(O, e, "EDGE", 0.9)
            sc.label((O[0] + (rr + 0.12) * math.cos(ar), O[1] + (rr + 0.12) * math.sin(ar)), nm, "TEXT", "start", 15, dx=2, dy=14)
    # i1 in the right panel
    sc.vec((3.5, 0.0), (3.5 + 1.2 * u[0], 1.2 * u[1]), S(bold("i"), "1"), "BLUE", 2.6, name_off=(14, -6), size=17, head=11)
    return sc
