"""Problem 32: particle on a string unwinding from a spool (plane of motion, view along k, free-body diagram).

Also hosts `basis_view`, `away` and `arrow` (generic helpers shared by the other modules of this batch)."""
import math

from figures.em_sol.p31 import _dvec, _matrix, _mname, _pol, _spin
from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle
from figures.mech import S, Scene, bold

PURPLE = "#8b5cf6"          # reaction (no kit token: a fixed colour, readable on every palette)
RED = "#ef4444"             # weight
ORANGE = "#f97316"          # auxiliary basis, spring force
YELLOW = "#eab308"          # right triangles


def away(sc, p, ref, text, col, off=16, anchor="middle", size=15, italic=True, weight="400"):
    """Label at world point p, pushed `off` pixels away from the world point ref (so it sits outside a triangle or a curve)."""
    px, py = sc.P(p)
    rx, ry = sc.P(ref)
    dx, dy = px - rx, py - ry
    n = math.hypot(dx, dy) or 1.0
    sc.label(p, text, col, anchor, size, italic=italic, weight=weight, dx=dx / n * off, dy=dy / n * off + 5)


def arrow(sc, a, v, col, w=3.0, head=12, k=1.0):
    """Arrow from a along the world vector v (scaled by k); returns the tip."""
    tip = (a[0] + k * v[0], a[1] + k * v[1])
    sc.vec(a, tip, None, col, w, head=head)
    return tip


def basis_view(sc, O, th, nfix, nrot, col="BLUE", L=2.0, u=1.4, axl=2.5, ang="θ", ra=0.7, rl=1.0, ls=15,
               legs=None, arcs=True, cf=0.5, lf=0.5, ra2=None, rl2=None, one=18, one2=None, l1dx=0, l4=(0, "middle", None), tri2=True):
    """View along a rotation axis: fixed axes at 0 and 90 degrees (grey), the rotated pair at th and 90 + th (th signed,
    counter-clockwise positive), arcs with arrowheads and the two right triangles of hypotenuse u.
    legs: (adjacent 1, opposite 1, adjacent 2, opposite 2) texts."""
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    leg = legs or ("cos " + ang, "sin " + ang, "cos " + ang, "sin " + ang)
    sh = lambda p: (O[0] + p[0], O[1] + p[1])
    t1 = [sh((0, 0)), sh((u * c, 0)), sh((u * c, u * s))]
    t2 = [sh((0, 0)), sh((0, u * c)), sh((-u * s, u * c))]
    triangle(sc, t1, "#eab308", 0.24)
    right_angle(sc, t1[1], 180 if c > 0 else 0, 90 if s > 0 else 270, 0.12)
    if tri2:
        triangle(sc, t2, "#eab308", 0.24)
        right_angle(sc, t2[1], 270 if c > 0 else 90, 180 if s > 0 else 0, 0.12)
    fixed_axis(sc, O, 0, axl, nfix[0], off=(16, 5))
    fixed_axis(sc, O, 90, axl, nfix[1], off=(0, -10))
    e1 = sh((L * c, L * s))
    e2 = sh((-L * s, L * c))
    sc.vec(O, e1, None, col, 2.6, head=11)
    sc.vec(O, e2, None, col, 2.6, head=11)
    sc.label(e1, nrot[0], col, "middle", 17, weight="700", dx=18 * c, dy=-18 * s + 5)
    sc.label(e2, nrot[1], col, "middle", 17, weight="700", dx=-18 * s, dy=-18 * c + 5)
    if arcs:
        sc.arc(O, ra, 0, th, "GREEN", 1.8, head=True)
        sc.arc(O, ra2 or ra, 90, 90 + th, "GREEN", 1.8, head=True)
        sc.label(_pol(O, rl, th * lf), ang, "GREEN", "middle", 16, dy=5)
        sc.label(_pol(O, rl2 or rl, 90 + th * lf), ang, "GREEN", "middle", 16, dy=5)
    sc.dashed(t1[2], t1[1])
    if tri2:
        sc.dashed(t2[2], t2[1])
    # leg labels, always on the outer side of each triangle
    if leg[0]:
        sc.label((O[0] + u * c / 2, O[1]), leg[0], "TEXT", "middle", ls, dx=l1dx, dy=22 if s > 0 else -12)
    if leg[1]:
        sc.label((O[0] + u * c, O[1] + u * s / 2), leg[1], "TEXT", "start" if c > 0 else "end", ls, dx=10 if c > 0 else -10, dy=5)
    if tri2:
        sc.label((O[0], O[1] + u * c * cf), leg[2], "TEXT", "start" if s > 0 else "end", ls, dx=10 if s > 0 else -10, dy=5)
        sc.label((O[0] - u * s / 2 + l4[0] / sc.k, O[1] + u * c), leg[3], "TEXT", l4[1], l4[2] or ls, dy=-10 if c > 0 else 24)
    away(sc, sh((u * c / 2, u * s / 2)), sh((u * c, 0)), "1", "TEXT", one, "middle", ls)
    if tri2:
        away(sc, sh((-u * s / 2, u * c / 2)), sh((0, u * c)), "1", "TEXT", one if one2 is None else one2, "middle", ls)
    return e1, e2


def _en(sub):
    return S(bold("e"), sub)


def _r0(sup):
    return bold("r") + f'<tspan baseline-shift="super" font-size="70%">{sup}</tspan><tspan baseline-shift="sub" font-size="70%" dx="-6">0</tspan>'


I1 = S(bold("i"), "1")
J1 = S(bold("j"), "1")
PHI = "φ"
PH = 45.0
A_ = 1.0
S_DRAW = 4.0
CP, SP = math.cos(math.radians(PH)), math.sin(math.radians(PH))
Bp = (A_ * CP, A_ * SP)
j1 = (-SP, CP)
i1 = (CP, SP)
Pp = (Bp[0] - S_DRAW * j1[0], Bp[1] - S_DRAW * j1[1])
Cc = (Bp[0], Pp[1])
Aa = (-A_, 0.0)


@figure("p32-plane",
        "Spool of radius a with the string wound from B to A and the free segment BP tangent at B, with the right triangle of legs s cos phi and s sin phi and the basis i_1, j_1 at B.",
        r"Plane of the motion, $\mathbf k$ out of the paper. The free segment is tangent at $B$ and leaves along $-\mathbf j_1$; it makes the angle $\phi$ with the downward vertical, so its legs are $s\cos\phi$ (vertical) and $s\sin\phi$ (horizontal), and $\mathbf r_0^P = a\,\mathbf i_1 - s\,\mathbf j_1$ with $s = a(3\pi - \omega t + \phi)$.")
def plane():
    sc = Scene(780, 560, (230, 230), 100)
    O = (0.0, 0.0)
    triangle(sc, [Bp, Cc, Pp], YELLOW, 0.26)
    sc.circle(O, A_, "HEAD", 2.2, fill="EDGE", opacity=0.20)
    # grey axes, 1.6 units each way
    fixed_axis(sc, O, 0, 1.6, "x", off=(14, 5))
    fixed_axis(sc, O, 90, 1.6, "y", off=(0, -10))
    sc.line(O, (-1.6, 0.0), "EDGE", 1.4)
    sc.line(O, (0.0, -1.6), "EDGE", 1.4)
    # wound string: thick arc from B counterclockwise over the top to A
    sc.arc(O, A_, PH, 180, "HEAD", 4.5)
    sc.label((-0.95, 1.2), "arc BA = a(π + ωt − φ)", "HEAD", "middle", 15)
    # radius OB and angle at O
    sc.line(O, Bp, "HEAD", 1.4)
    sc.label((Bp[0] / 2, Bp[1] / 2), "a", "HEAD", "middle", 16, dx=-13, dy=-3)
    sc.arc(O, 0.42, 0, PH, "GREEN", 1.8, head=True)
    sc.label(_pol(O, 0.66, PH / 2), PHI, "GREEN", "middle", 16, dy=5)
    # attachment A and its rotation
    sc.dotp(Aa, 4.5)
    sc.label(Aa, "A", "HEAD", "end", 17, dx=-10, dy=-10)
    sc.arc(O, 1.2, -118, -62, "TEXT", 1.8, head=True)
    sc.label((0.0, -1.2), "ω", "TEXT", "middle", 17, dx=20, dy=22)
    # free string, legs, angle at B
    sc.line(Bp, Cc, "EDGE", 1.1, "5 4")
    sc.line(Cc, Pp, "EDGE", 1.1, "5 4")
    sc.line(Bp, Pp, "HEAD", 4.5)
    right_angle(sc, Cc, 90, 0, 0.12)
    right_angle(sc, Bp, 225, 315, 0.15)
    sc.arc(Bp, 0.34, -90, -45, "GREEN", 1.8, head=True)
    sc.label(_pol(Bp, 0.58, -67.5), PHI, "GREEN", "middle", 16, dy=5)
    sc.label((Bp[0], (Bp[1] + Cc[1]) / 2 - 0.95), "s cos φ", "TEXT", "end", 15, dx=-10, dy=5)
    sc.label(((Bp[0] + Pp[0]) / 2, Pp[1]), "s sin φ", "TEXT", "middle", 15, dy=24)
    mid = ((Bp[0] + Pp[0]) / 2, (Bp[1] + Pp[1]) / 2)
    sc.label(mid, "s = a(3π − ωt + φ)", "HEAD", "start", 15, dx=14, dy=-12)
    sc.note((1.95, -1.78), "not to scale", "TEXT", "start", 13)
    # basis at B
    sc.vec(Bp, (Bp[0] + 0.8 * i1[0], Bp[1] + 0.8 * i1[1]), None, "BLUE", 2.6, head=11)
    sc.label((Bp[0] + 0.8 * i1[0], Bp[1] + 0.8 * i1[1]), I1, "BLUE", "middle", 17, weight="700", dx=14, dy=-6)
    sc.vec(Bp, (Bp[0] + 0.8 * j1[0], Bp[1] + 0.8 * j1[1]), None, "BLUE", 2.6, head=11)
    sc.label((Bp[0] + 0.8 * j1[0], Bp[1] + 0.8 * j1[1]), J1, "BLUE", "middle", 17, weight="700", dx=18, dy=-8)
    sc.dotp(Bp, 4.5)
    sc.label(Bp, "B", "HEAD", "start", 17, dx=14, dy=5)
    sc.dotp(Pp, 5.5)
    sc.label(Pp, "P", "HEAD", "start", 17, dx=14, dy=5)
    # position vector O-P
    _dvec(sc, O, (Pp[0] - 0.05, Pp[1] + 0.03), "HEAD", 1.6, 9)
    sc.label((-1.55, -2.4), _r0("P") + " = a " + I1 + " − s " + J1, "HEAD", "start", 17)
    axis_out(sc, O, None)
    sc.label(O, bold("k"), "HEAD", "end", 17, dx=-14, dy=24)
    return sc


@figure("p32-rotation-k",
        "View along k of the basis i_1, j_1 turned by phi from i, j, with the two unit right triangles.",
        r"Rotation by $\phi$ about $\mathbf k$ (out of the paper). The triangle of $\mathbf j_1$ has its opposite leg along $-\mathbf i$, which gives the minus sign in $\mathbf j_1 = -\sin\phi\,\mathbf i + \cos\phi\,\mathbf j$.")
def rotation_k():
    sc = Scene(860, 600, (330, 290), 80)
    O = (0.0, 0.0)
    basis_view(sc, O, 40.0, (bold("i"), bold("j")), (I1, J1), L=2.0, u=1.4, ang=PHI,
               legs=("cos φ", "sin φ", "cos φ", "−sin φ on i"), cf=0.9, l1dx=8, l4=(31, "end", 13))
    axis_out(sc, O, None)
    sc.label(O, bold("k"), "HEAD", "end", 17, dx=-14, dy=-6)
    _spin(sc, O, 0.3, 200, 340, "positive about k", (-26, 46), "end")
    _matrix(sc, 3.0, -1.2, _mname("0", "1"), (("cos φ", "−sin φ", "0"), ("sin φ", "cos φ", "0"), ("0", "0", "1")), colw=0.8)
    return sc


@figure("p32-fbd",
        "Free-body diagram of P with its weight and the string tension towards the tangency point B, and the weight split along i_1 and j_1.",
        r"Forces on $P$: the weight $-mg\,\mathbf j$ and the tension $T\,\mathbf j_1$ towards $B$. Only the weight has a component along $\mathbf i_1$, which gives the equation of motion free of $T$.")
def fbd():
    sc = Scene(780, 640, (230, 230), 100)
    O = (0.0, 0.0)
    sc.circle(O, A_, "EDGE", 1.6, fill="EDGE", opacity=0.10)
    sc.line(Bp, Pp, "EDGE", 1.6)
    sc.dotp(Bp, 3.5, "EDGE")
    sc.label(Bp, "B", "TEXT", "start", 16, dx=12, dy=-6)
    W = 1.2
    # weight and its decomposition on i_1, j_1 (dashed)
    wt = (Pp[0], Pp[1] - W)
    ci = (Pp[0] - W * SP * i1[0], Pp[1] - W * SP * i1[1])      # component along -i_1
    cj = (Pp[0] - W * CP * j1[0], Pp[1] - W * CP * j1[1])      # component along -j_1
    sc.line(wt, ci, RED, 1.0, "4 4")
    sc.line(wt, cj, RED, 1.0, "4 4")
    _dvec(sc, Pp, ci, RED, 2.0, 9)
    _dvec(sc, Pp, cj, RED, 2.0, 9)
    sc.vec(Pp, wt, None, RED, 3.0, head=12)
    sc.label(wt, "−m g " + bold("j"), RED, "middle", 16, dy=22)
    sc.label(ci, "−m g sin φ", RED, "end", 15, dx=-8, dy=18)
    sc.label(cj, "−m g cos φ", RED, "start", 15, dx=10, dy=6)
    # tension towards B, equal to m g in the equilibrium at rest
    tt = arrow(sc, Pp, j1, "PINK", 3.4, 12, W)
    sc.label(tt, "T " + J1, "PINK", "end", 17, dx=-12, dy=-8)
    # basis at P
    sc.vec(Pp, (Pp[0] + 0.7 * i1[0], Pp[1] + 0.7 * i1[1]), None, "BLUE", 2.4, head=10)
    sc.label((Pp[0] + 0.7 * i1[0], Pp[1] + 0.7 * i1[1]), I1, "BLUE", "start", 17, weight="700", dx=8, dy=-4)
    sc.vec(Pp, (Pp[0] + 0.7 * j1[0], Pp[1] + 0.7 * j1[1]), None, "BLUE", 2.4, head=10)
    sc.label((Pp[0] + 0.45 * j1[0], Pp[1] + 0.45 * j1[1]), J1, "BLUE", "end", 17, weight="700", dx=-10, dy=14)
    sc.dotp(Pp, 5.5)
    sc.label(Pp, "P", "HEAD", "start", 17, dx=16, dy=5)
    sc.note((-1.5, -3.9), "inertial frame: no inertia forces; the spool acts on the string only", "TEXT", "start", 13)
    return sc
