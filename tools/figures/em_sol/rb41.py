"""Problem RB-41: sail sledge on three blades A, B, C (angle psi, rear blade turned by theta; instantaneous centre I)."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d
from figures.em_sol.rb12 import plane_rotation
from figures.mech import S, Scene, bold, dot1, dot2

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I0, J0, K0 = S(I, "0"), S(J, "0"), S(K, "0")
IB, JB = S(I, "b"), S(J, "b")
EC, NC = S(bold("e"), "C"), S(bold("n"), "C")
UINF = S("U", "∞")
PSI = 20.0
TH = 40.0
SQ3 = math.sqrt(3.0)
A_PT, B_PT, C_PT = (0.5, SQ3 / 2), (0.5, -SQ3 / 2), (-1.0, 0.0)
M_PT = (0.5, 0.0)
I_PT = (0.5, -1.5 / math.tan(math.radians(TH)))


# ------------------------------------------------------------------------------------------------ rb41-rot-psi
@figure("rb41-rot-psi",
        "The body basis of the sledge, turned counterclockwise by psi from the fixed basis.",
        r"Rotation about the vertical $\mathbf k_0$ (⊙) by $\psi$; the wind blows along $\mathbf j_0$.")
def rot_psi():
    def pre(sc):
        sc.dashed((-2.3, 0.0), (0.0, 0.0))

    def post(sc):
        sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=-16, dy=-12)
        # gravity into the paper, small symbol in a corner
        axis_in(sc, (-2.2, -1.1), None, "HEAD")
        sc.label((-2.2, -1.1), "g  (into the paper)", "HEAD", "start", 16, weight="700", dx=16, dy=5)
        # wind
        sc.vec((2.3, -1.6), (2.3, -0.45), UINF, "HEAD", 3.0, name_off=(26, 6), size=18, head=12)
        sc.note((2.3, -1.95), "wind", "TEXT", "middle", 14)
    return plane_rotation(880, 700, (430, 360), 165, PSI, (I0, J0, IB, JB), K0 + " (⊙)", ("ψ", ""), None,
                          extra_pre=pre, extra_post=post, out_off=(-26, 30), L=1.5)


# ------------------------------------------------------------------------------------------------ rb41-blades
def _blade(sc, p, ang, half=0.2, w=4.0, col="HEAD"):
    sc.line(add(p, d(ang), -half), add(p, d(ang), half), col, w)


def _triangle_body(sc, fill=True):
    sc.poly([A_PT, B_PT, C_PT], "EDGE", 1.6, fill="EDGE", close=True, opacity=0.10)
    sc.line(C_PT, M_PT, "EDGE", 1.2, "7 5")


@figure("rb41-blades",
        "The triangle of blades, the blade directions, and the instantaneous centre at the meeting point of the "
        "normals to the blades.",
        r"The blades are at $\ell$ from $G$; $A$ and $B$ stand $\ell/2$ ahead of $G$. The instantaneous centre $I$ is "
        r"where the normals to the blades meet: $\overrightarrow{GI} = \tfrac{\ell}{2}\,\mathbf i_b - "
        r"\tfrac{3\ell}{2}\cot\theta\,\mathbf j_b$.")
def blades():
    sc = Scene(1000, 740, (400, 300), 175)
    G = (0.0, 0.0)
    _triangle_body(sc)
    # right triangle G-M-A
    triangle(sc, [G, M_PT, A_PT], ORANGE, 0.30)
    right_angle(sc, M_PT, 180, 90, 0.07)
    sc.line(G, A_PT, "EDGE", 1.2, "3 3")
    # blades
    _blade(sc, A_PT, 0.0)
    _blade(sc, B_PT, 0.0)
    _blade(sc, C_PT, TH)
    # angle theta at C from the axis direction
    sc.arc(C_PT, 0.46, 0.0, TH, "GREEN", 1.8, head=True)
    sc.label(add(C_PT, d(TH / 2 - 4), 0.46), "θ", "GREEN", "middle", 17, dx=18, dy=8)
    # unit vectors of the blade at C
    unit(sc, C_PT, TH, 0.62, EC, "GREEN", off=(16, 4))
    unit(sc, C_PT, TH + 90.0, 0.62, NC, "GREEN", off=(-14, -4))
    # normals to the blades, dashed, and the instantaneous centre
    sc.line(B_PT, I_PT, "EDGE", 1.3, "6 4")
    sc.line(A_PT, (A_PT[0], A_PT[1] + 0.3), "EDGE", 1.3, "6 4")
    sc.line(C_PT, I_PT, "EDGE", 1.3, "6 4")
    sc.line(G, I_PT, "HEAD", 1.4, "4 3")
    sc.mass(I_PT, None, r=5.0, col="ACC")
    sc.label(I_PT, "I", "HEAD", "middle", 18, dx=16, dy=-8)
    sc.arc(I_PT, 0.42, 25.0, -155.0, "GREEN", 1.9, head=True)
    sc.label(add(I_PT, d(-90.0), 0.42), "turning with u > 0", "GREEN", "middle", 15, italic=False, dy=26)
    # dimensions
    sc.label((-0.5, 0.0), "GC = ℓ", "TEXT", "middle", 15, dy=22)
    sc.label((0.27, 0.0), "GM = ℓ/2", "TEXT", "middle", 14, dy=22)
    sc.label((0.2, 0.46), "GA = ℓ", "TEXT", "end", 14, dx=-6, dy=-6)
    for x, y0, y1, nm in ((0.88, 0.0, SQ3 / 2, "MA = √3 ℓ/2"), (1.58, -SQ3 / 2, SQ3 / 2, "AB = √3 ℓ")):
        sc.dim((x, y0), (x, y1), "", off=(0, 0))
        sc.dashed((0.58, y1), (x + 0.1, y1))
        sc.dashed((0.58, y0), (x + 0.1, y0)) if y0 != 0.0 else None
        sc.label((x, (y0 + y1) / 2), nm, "TEXT", "start", 15, dx=10, dy=5)
    # points and body basis
    for p, nm, off in ((A_PT, "A", (-18, -12)), (B_PT, "B", (-18, 24)), (C_PT, "C", (-18, 26)), (M_PT, "M", (14, 22))):
        sc.mass(p, None, r=4.5, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=-14, dy=24)
    O = (-1.7, 0.85)
    sc.vec(O, (O[0] + 0.6, O[1]), IB, "EDGE", 1.6, name_off=(16, 6), size=16, head=8)
    sc.vec(O, (O[0], O[1] + 0.6), JB, "EDGE", 1.6, name_off=(12, -2), size=16, head=8)
    axis_out(sc, O, None, "HEAD", r_px=7)
    sc.label(O, K0 + " (⊙)", "HEAD", "end", 15, weight="700", dx=-14, dy=5)
    sc.note((1.58, -1.55), "θ = 40°,  ℓ = 1", "TEXT", "start", 13)
    return sc


# ------------------------------------------------------------------------------------------------ rb41-fbd
@figure("rb41-fbd",
        "Free-body diagram of the sledge in top view and side view: weight, normal and side reactions of the blades, "
        "and the aerodynamic force at the centre of pressure.",
        r"Free-body diagram. The blades take forces normal to themselves and vertical reactions; the sail force acts at "
        r"$P$, $\ell$ above $G$. In the side view the lift pitches the sledge about the line $AB$ and unloads the rear "
        r"blade $C$.")
def fbd():
    sc = Scene(1360, 600, (330, 300), 150)
    G = (0.0, 0.0)
    # ---------------- left panel: top view
    _triangle_body(sc)
    _blade(sc, A_PT, 0.0, 0.18, 4.0)
    _blade(sc, B_PT, 0.0, 0.18, 4.0)
    _blade(sc, C_PT, TH, 0.18, 4.0)
    nC = d(TH + 90.0)
    Y = 0.6
    sc.vec(A_PT, (A_PT[0], A_PT[1] + Y), "Y", "GREEN", 3.2, name_off=(18, 4), size=18, head=11)
    sc.vec(B_PT, (B_PT[0], B_PT[1] + Y), "Y", "GREEN", 3.2, name_off=(18, 4), size=18, head=11)
    sc.vec(C_PT, add(C_PT, nC, 0.7), S("Y", "C") + " " + NC, "GREEN", 3.2, name_off=(-30, -6), size=18, head=11)
    # aerodynamic force (horizontal) drawn at G, acting at P above G
    ang = 77.0
    sc.vec(G, add(G, d(ang), 1.0), None, "PINK", 3.4, head=12)
    sc.label(add(G, d(ang), 1.0), "L + D at P (above G)", "PINK", "end", 16, weight="700", dx=-6, dy=-4)
    for p, nm, off in ((A_PT, "A", (-16, -10)), (B_PT, "B", (-16, 24)), (C_PT, "C", (-16, 26))):
        sc.mass(p, None, r=4.5, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.mass(G, None, r=4.5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=12, dy=24)
    O = (-1.95, 1.15)
    sc.vec(O, (O[0] + 0.5, O[1]), IB, "EDGE", 1.6, name_off=(16, 6), size=16, head=8)
    sc.vec(O, (O[0], O[1] + 0.5), JB, "EDGE", 1.6, name_off=(12, -2), size=16, head=8)
    sc.note((-0.9, -1.5), "top view", "TEXT", "start", 14)
    # ---------------- right panel: side view
    X0 = 4.4
    sc.ground((X0 - 1.9, 0.0), (X0 + 2.3, 0.0), -1, step=9, length=9)
    Gs = (X0, 0.0)
    Cs = (X0 - 1.0, 0.0)
    Ab = (X0 + 0.5, 0.0)
    Ps = (X0, 1.0)
    sc.dashed(Gs, Ps)
    sc.dim((X0 - 0.3, 1.0), (X0 - 0.3, 0.0), "ℓ", off=(-14, 4))
    sc.dashed(Ps, (X0 - 0.35, 1.0))
    sc.vec(Ps, (X0 + 0.7, 1.0), "L", "PINK", 3.4, name_off=(14, 6), size=18, head=12)
    sc.vec(Gs, (X0, -0.45), "mg", "PINK", 3.2, name_off=(22, 4), size=18, head=12)
    sc.vec(Cs, (X0 - 1.0, 0.55), S("N", "C"), "GREEN", 3.2, name_off=(-20, 4), size=18, head=11)
    sc.vec(Ab, (X0 + 0.5, 0.6), S("N", "A") + " + " + S("N", "B"), "GREEN", 3.2, name_off=(0, -14), size=18, head=11)
    for p, nm, off in ((Cs, "C", (-4, 28)), (Ab, "A, B", (22, 28)), (Gs, "G", (-16, 24)), (Ps, "P", (-16, -12))):
        sc.mass(p, None, r=4.5, col="BLUE")
        sc.label(p, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    # horizontal dimensions below the ice
    yd = -0.85
    sc.dim((X0 - 1.0, yd), (X0, yd), "ℓ", off=(0, 22))
    sc.dim((X0, yd), (X0 + 0.5, yd), "ℓ/2", off=(0, 22))
    for x in (X0 - 1.0, X0, X0 + 0.5):
        sc.dashed((x, -0.62), (x, yd - 0.1))
    # tipping about AB
    sc.arc(Ab, 1.0, 55.0, 5.0, "GREEN", 1.9, dash="6 4", head=True)
    sc.label(add(Ab, d(5.0), 1.0), "tipping about AB", "GREEN", "start", 15, italic=False, dx=12, dy=-6)
    axis_in(sc, (X0 - 1.8, 1.5), None, "HEAD", r_px=7)
    sc.label((X0 - 1.8, 1.5), "side view:  " + S(bold("j"), "b") + " into the paper", "TEXT", "start", 14, italic=False, dx=16, dy=5)
    return sc


# ------------------------------------------------------------------------------------------------ rb41-wind
@figure("rb41-wind",
        "The relative wind of the moving sledge and the lift and drag forces it produces.",
        r"Relative wind $\mathbf u_b^w = U_\infty\,\mathbf j_0 - v\,\mathbf i_0$; the forward force is "
        r"$\sqrt{U_\infty^2 + v^2}\,(b_L U_\infty - b_D v)$, zero at $v = b_L U_\infty/b_D$.")
def wind():
    U, V = 1.0, 1.2
    u = math.hypot(U, V)
    ud = (-V / u, U / u)                 # relative wind direction (-v, U)/u
    ld = (U / u, V / u)                  # u x k0 = (U, V)/u
    sc = Scene(1120, 640, (300, 520), 170)
    # ---- left: velocity triangle at the point P_v
    Pv = (0.0, 0.0)
    sc.dashed((-V, 0.0), (-V, U))
    sc.dashed((0.0, U), (-V, U))
    sc.vec(Pv, (0.0, U), UINF + " " + J0, "HEAD", 3.0, name_off=(34, 6), size=17, head=12)
    sc.vec(Pv, (-V, 0.0), "−v " + I0, "HEAD", 3.0, name_off=(0, 26), size=17, head=12)
    sc.vec(Pv, (-V, U), None, "BLUE", 3.4, head=13)
    sc.label((-0.9, 0.86), "√(" + S("U", "∞") + "² + v²)", "BLUE", "start", 16, weight="700")
    right_angle(sc, Pv, 90, 180, 0.09)
    sc.mass(Pv, None, r=4.5, col="BLUE")
    sc.label(Pv, "P", "HEAD", "middle", 17, dx=14, dy=22)
    sc.label((-V, U), "relative wind  u", "BLUE", "start", 15, italic=False, dx=6, dy=-14)
    sc.note((-V / 2, -0.55), "velocities, to scale  (" + S("U", "∞") + " = 1, v = 1.2)", "TEXT", "middle", 13)
    # ---- right: forces at P
    F0 = (2.5, 0.0)
    sc.vec((F0[0] - 1.3, 0.0), (F0[0] + 1.9, 0.0), None, "EDGE", 1.4, head=8)
    sc.label((F0[0] + 1.9, 0.0), I0, "TEXT", "middle", 16, weight="700", dx=14, dy=6)
    Dl, Ll = 0.9, 1.8
    Dt = add(F0, ud, Dl)
    Lt = add(F0, ld, Ll)
    sc.vec(F0, Dt, "D", "PINK", 3.4, name_off=(-14, -6), size=18, head=12)
    sc.vec(F0, Lt, "L", "PINK", 3.4, name_off=(16, -4), size=18, head=12)
    # projections on i0
    sc.dashed(Dt, (Dt[0], 0.0))
    sc.dashed(Lt, (Lt[0], 0.0))
    sc.vec((F0[0], -0.2), (Lt[0], -0.2), None, "PINK", 2.2, head=9)
    sc.label(((F0[0] + Lt[0]) / 2, -0.2), S("b", "L") + " " + UINF + " u", "PINK", "middle", 16, weight="700", dy=26)
    sc.vec((F0[0], -0.2), (Dt[0], -0.2), None, "PINK", 2.2, head=9)
    sc.label(((F0[0] + Dt[0]) / 2, -0.2), "−" + S("b", "D") + " v u", "PINK", "middle", 16, weight="700", dy=26, dx=-26)
    right_angle(sc, F0, math.degrees(math.atan2(ud[1], ud[0])), math.degrees(math.atan2(ld[1], ld[0])), 0.1)
    sc.mass(F0, None, r=4.5, col="BLUE")
    sc.label(F0, "P", "HEAD", "middle", 17, dx=14, dy=22)
    sc.note((F0[0] + 0.3, 2.25), "L = 2 D  " + "(" + S("b", "L") + " / " + S("b", "D") + " = 2)", "TEXT", "middle", 13)
    axis_out(sc, (-1.7, 1.6), None, "HEAD", r_px=7)
    sc.label((-1.7, 1.6), K0 + " (⊙)", "HEAD", "start", 15, weight="700", dx=14, dy=5)
    return sc
