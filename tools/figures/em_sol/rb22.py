"""Problem RB-22: sphere with a bar articulated at O on an inclined plane (angles gamma, theta, beta and phi)."""
import math

from figures.em_solutions import axis_in, axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d, rotation_view
from figures.em_sol.rb12 import plane_rotation
from figures.em_sol.rb16 import I_DIR, K_DIR, _weight_components
from figures.mech import S, Scene, bold

ORANGE = "ACC"
I, J, K = bold("i"), bold("j"), bold("k")
I2, J2 = S(bold("i"), "2"), S(bold("j"), "2")
GAMMA = 25.0
GR = math.radians(GAMMA)


@figure("rb22-rot-gamma",
        "The basis of the inclined plane, turned by gamma about the horizontal axis j, with the components of the weight.",
        r"Rotation about $\mathbf j$ (⊗) by $\gamma$; the weight is $Mg\sin\gamma\,\mathbf i - Mg\cos\gamma\,\mathbf k$.")
def rot_gamma():
    def pre(sc):
        sc.ground(add((0.0, 0.0), I_DIR, -1.6), add((0.0, 0.0), I_DIR, 3.6), -1)

    def post(sc):
        sc.label((0.0, 0.0), "O", "HEAD", "middle", 17, dx=-16, dy=-6)
        _weight_components(sc, (2.6, 2.3), 1.6, "Mg", "Mg sin γ", "Mg cos γ", (30, 6), (2, -26), (12, 6))
    return rotation_view(860, 600, (330, 390), 125, -GAMMA, bold("I"), bold("K"), I, K, J + " (⊗)", ("γ", ""), pre=pre,
                         post=post, out_kind="in", out_off=(-6, 30))


@figure("rb22-rot-theta",
        "Top view of the inclined plane with the auxiliary basis i_2, j_2 and the contact point P at distance d from O.",
        r"Rotation about $\mathbf k$ (⊙) by $\theta$. $P$ is at the distance $d$ from $O$ along $\mathbf i_2$; with rolling, "
        r"$P$ stays on the circle of radius $d$.")
def rot_theta():
    ang, dd, w = 35.0, 2.25, 1.0
    th = math.radians(ang)
    P = (dd * math.cos(th), dd * math.sin(th))
    u2 = (math.cos(th), math.sin(th))
    nrm = (math.sin(th), -math.cos(th))

    def pre(sc):
        sc.poly([(dd * math.cos(math.radians(t)), dd * math.sin(math.radians(t))) for t in range(0, 361, 4)],
                "EDGE", 1.2, "6 4", close=True)
        sc.line((0.0, 0.0), add(P, u2, 0.45), "HEAD", 5.0)

    def post(sc):
        sc.label((0.0, 0.0), "O", "HEAD", "middle", 17, dx=-8, dy=26)
        # in-plane weight component at P and its two parts
        Q = add(P, (1.0, 0.0), w)
        P2 = add(P, u2, w * math.cos(th))
        sc.dashed(P, P2)
        sc.dashed(P2, Q)
        sc.vec(P, Q, None, "PINK", 3.0, head=12)
        sc.label(add(P, (1.0, 0.0), w * 0.5), "Mg sin γ", "PINK", "middle", 16, weight="700", dx=6, dy=24)
        sc.label(add(P, u2, w * math.cos(th) * 0.5), "Mg sin γ cos θ", "TEXT", "end", 14, dx=-4, dy=-16)
        sc.label(add(P2, (math.sin(th), -math.cos(th)), w * math.sin(th) * 0.5), "Mg sin γ sin θ", "TEXT", "start", 14,
                 dx=10, dy=-6)
        sc.mass(P, None, r=5, col="ACC")
        sc.label(P, "P", "HEAD", "middle", 17, dx=-14, dy=22)
        sc.label(add((0.0, 0.0), u2, 1.55), "rod (projection)", "TEXT", "end", 13, italic=False, dx=-14, dy=-30)
        # distance d from O to P
        sc.dashed(add((0.0, 0.0), nrm, 0.0), add((0.0, 0.0), nrm, 1.3))
        sc.dashed(P, add(P, nrm, 1.3))
        sc.dim(add((0.0, 0.0), nrm, 1.2), add(P, nrm, 1.2), "d", off=(18, 20))
    return plane_rotation(960, 780, (400, 400), 140, ang, (I, J, I2, J2), K + " (⊙)", ("θ", ""), None, extra_pre=pre,
                          extra_post=post, out_off=(-44, 22))


# ------------------------------------------------------------------------------------------------ section of the rod
R, DD = 1.0, 2.15
BETA = math.degrees(math.atan2(R, DD))
BR = math.radians(BETA)
L = math.hypot(DD, R)
UDIR = (math.cos(BR), math.sin(BR))
WDIR = (-math.sin(BR), math.cos(BR))


def _rod(sc, o, t0, t1, col="HEAD", w=5.0, dash=None, dirv=UDIR):
    sc.line(add(o, dirv, t0), add(o, dirv, t1), col, w, dash)


@figure("rb22-rod-section",
        "Section through O, P and G with the right triangle of the rod, the angle beta and the rod basis u, w.",
        r"Rod frame: $\mathbf u = \cos\beta\,\mathbf i_2 + \sin\beta\,\mathbf k$ and $\mathbf w = -\sin\beta\,\mathbf i_2 + "
        r"\cos\beta\,\mathbf k$, from the right triangle $OPG$ with legs $d$, $R$ and hypotenuse $L$.")
def rod_section():
    sc = Scene(820, 540, (150, 400), 128)
    O, P, G = (0.0, 0.0), (DD, 0.0), (DD, R)
    sc.ground((-0.5, 0.0), (3.3, 0.0), -1)
    sc.circle(G, R, "HEAD", 2.0, fill="EDGE", opacity=0.10)
    triangle(sc, [O, P, G], ORANGE, 0.14)
    # the rod, dashed inside the sphere
    _rod(sc, O, 0.0, L - R)
    _rod(sc, O, L - R, L + R, "HEAD", 3.0, "8 5")
    _rod(sc, O, L + R, L + R + 0.45)
    fixed_axis(sc, O, 0, 3.7, I2, off=(14, -8))
    fixed_axis(sc, O, 90, 2.4, K, off=(12, 6))
    # legs and right angle
    right_angle(sc, P, 180, 90, 0.12)
    sc.dim((0.0, -0.4), (DD, -0.4), "d", off=(0, 20))
    sc.dashed((0.0, 0.0), (0.0, -0.5))
    sc.dashed(P, (DD, -0.5))
    sc.label((DD, R / 2), "R", "TEXT", "start", 16, dx=10, dy=5)
    mid = add(O, UDIR, L / 2)
    sc.label(add(mid, WDIR, 0.3), "L = √(d² + R²)", "TEXT", "end", 16, dx=0, dy=-2)
    # basis u, w and their small triangles
    foot, tip = (math.cos(BR), 0.0), UDIR
    sc.dashed(foot, tip)
    sc.label((foot[0] / 2, 0.0), "cos β", "TEXT", "middle", 14, dy=22)
    sc.label((foot[0], foot[1] + 0.15), "sin β", "TEXT", "start", 14, dx=6, dy=-2)
    f2, t2 = (0.0, math.cos(BR)), WDIR
    triangle(sc, [O, f2, t2 and (t2[0], t2[1])], ORANGE, 0.14)
    sc.dashed(f2, (t2[0], t2[1]))
    sc.label((0.0, f2[1] / 2), "cos β", "TEXT", "start", 14, dx=8, dy=6)
    sc.label((t2[0] / 2, t2[1]), "sin β", "TEXT", "middle", 14, dy=-8)
    unit(sc, O, BETA, 1.0, bold("u"), "BLUE", off=(14, -12))
    unit(sc, O, BETA + 90, 1.0, bold("w"), "BLUE", off=(-12, -10))
    # arcs of beta
    sc.arc(O, 0.55, 0, BETA, "GREEN", 1.7, head=True)
    sc.label(add(O, d(BETA / 2), 0.55), "β", "GREEN", "middle", 17, dx=18, dy=2)
    sc.arc(O, 0.55, 90, 90 + BETA, "GREEN", 1.7, head=True)
    sc.label(add(O, d(90 + BETA / 2), 0.55), "β", "GREEN", "middle", 17, dx=-16, dy=-4)
    for pt, nm, off in ((P, "P", (12, 24)), (G, "G", (-16, -10))):
        sc.mass(pt, None, r=4.5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    axis_in(sc, O, None, "HEAD")
    sc.label(O, J2 + " (⊗)", "HEAD", "end", 16, weight="700", dx=-16, dy=-12)
    sc.label(O, "O", "HEAD", "middle", 17, dx=-14, dy=24)
    sc.note((1.0, 2.55), "rotation about −" + J2 + " (counterclockwise as seen)", "TEXT", "start", 14)
    return sc


@figure("rb22-rot-phi",
        "The rotation phi of the sphere about the rod, measured from the normal w to the rod.",
        r"Rotation about the rod $\mathbf u$ (⊙) by $\varphi$, measured from $\mathbf w$, the normal to the rod in the "
        r"vertical plane of $\mathbf i_2$ and $\mathbf k$ (read from the statement figure).")
def rot_phi():
    ang, Rs = 40.0, 1.42

    def pre(sc):
        sc.poly([(Rs * math.cos(math.radians(t)), Rs * math.sin(math.radians(t))) for t in range(0, 361, 4)],
                "HEAD", 1.8, fill="EDGE", close=True, opacity=0.08)
        sc.ground((-0.9, -Rs - 0.08), (0.9, -Rs - 0.08), -1)
        sc.label((0.0, -Rs - 0.08), "plane", "TEXT", "middle", 15, dy=34)

    def post(sc):
        pe = add((0.0, 0.0), d(90 + ang), Rs)
        sc.dashed(add((0.0, 0.0), d(90 + ang), 1.0), pe)
        sc.mass(pe, None, r=5, col="ACC")
        sc.label(pe, "mark", "HEAD", "end", 15, dx=-10, dy=-4)
        sc.label((0.0, 0.0), "G", "HEAD", "middle", 17, dx=16, dy=-14)
        sc.dashed((0.0, 0.0), add((0.0, 0.0), d(-50), Rs))
        sc.label(add((0.0, 0.0), d(-50), Rs / 2), "R", "TEXT", "start", 16, dx=8, dy=14)
    return rotation_view(760, 820, (380, 470), 190, ang, J2, bold("w"), S(bold("e"), "2"), S(bold("e"), "3"),
                         bold("u") + " (⊙)", ("φ", ""), col="ACC", pre=pre, post=post, out_off=(-16, 28))


# ------------------------------------------------------------------------------------------------ exploded view
@figure("rb22-exploded",
        "Exploded view of the rod and the sphere with the action-reaction pair at G, the joint force at O and the forces of "
        "the plane at P.",
        r"Exploded view. The massless rod is in equilibrium under $\mathbf R_O$ at $O$ and $-\mathbf F_r$, $-\mathbf Q_r$ at "
        r"$G$, which gives $\mathbf R_O = \mathbf F_r$ and $\mathbf Q_r = -L\,\mathbf u\times\mathbf F_r$.")
def exploded():
    sc = Scene(900, 900, (150, 800), 110)
    wd = (math.sin(GR), -math.cos(GR))          # weight direction in the plane (i2, k): tilted by gamma from -k towards +i2
    # ---- rod alone (top part)
    O1 = (0.0, 3.6)
    G1 = add(O1, UDIR, L)
    sc.note((-0.8, 6.0), "ROD (massless)", "HEAD", "start", 15)
    sc.line(O1, G1, "HEAD", 5.0)
    fixed_axis(sc, O1, 0, 3.0, I2, off=(14, 6))
    fixed_axis(sc, O1, 90, 1.4, K, off=(12, 6))
    sc.mass(O1, None, r=5, col="BLUE")
    sc.label(O1, "O", "HEAD", "middle", 17, dx=-14, dy=24)
    sc.mass(G1, None, r=5, col="BLUE")
    sc.label(G1, "G", "HEAD", "middle", 17, dx=-16, dy=-8)
    # force at O: R_O = F_w w (+ F_j j2 normal to the paper)
    sc.vec(O1, add(O1, WDIR, 1.2), S("R", "O"), "GREEN", 3.0, name_off=(-20, -4), size=17, head=12)
    sc.label(add(O1, WDIR, 0.65), S("F", "w") + " " + bold("w"), "GREEN", "start", 15, weight="700", dx=14, dy=0)
    sc.note((-0.5, 2.95), "F" + '<tspan baseline-shift="sub" font-size="70%">j</tspan>' + " along " + "j" + '<tspan baseline-shift="sub" font-size="70%">2</tspan>' + " (normal to the paper)", "TEXT", "start", 13)
    sc.note((-0.5, 2.65), "joint torque " + S("Q", "O") + " " + bold("i") + '<tspan baseline-shift="sub" font-size="70%">2</tspan>' + " = 0", "TEXT", "start", 13)
    # reaction at G on the rod: -F_r = -F_w w and the torque -Q_r (counterclockwise as seen)
    sc.vec(G1, add(G1, WDIR, -0.9), "−" + S("F", "r"), ORANGE, 3.0, name_off=(26, 10), size=17, head=12)
    sc.spin(G1, 0.42, 30, 150, "", ORANGE)
    sc.label(add(G1, d(90), 0.42), "−" + S("Q", "r"), ORANGE, "middle", 16, weight="700", dy=-16)
    # ---- sphere alone (bottom part)
    P = (DD, 0.0)
    G = (DD, R)
    sc.ground((-0.5, 0.0), (4.4, 0.0), -1)
    sc.circle(G, R, "HEAD", 2.0, fill="EDGE", opacity=0.10)
    sc.note((-0.8, 2.2), "SPHERE", "HEAD", "start", 15)
    sc.mass(G, None, r=5, col="BLUE")
    sc.label(G, "G", "HEAD", "middle", 17, dx=-16, dy=-6)
    sc.mass(P, None, r=4.5, col="BLUE")
    sc.label(P, "P", "HEAD", "middle", 17, dx=16, dy=24)
    # weight (tilted by gamma) and the rod force F_r = F_w w drawn against w, side by side (they coincide for beta = gamma)
    sc.vec(G, add(G, wd, 0.8), None, "PINK", 3.0, head=12)
    sc.label(add(G, wd, 0.8), "Mg", "PINK", "end", 17, weight="700", dx=-8, dy=16)
    t0 = add(G, UDIR, 0.18)
    sc.vec(t0, add(t0, WDIR, -0.8), None, ORANGE, 3.0, head=12)
    sc.label(add(t0, WDIR, -0.8), S("F", "r") + " = " + S("F", "w") + " " + bold("w"), ORANGE, "start", 16, weight="700",
             dx=8, dy=14)
    # torque of the rod on the sphere (clockwise as seen: positive about j2)
    sc.spin(G, 0.42, 150, 30, "", ORANGE)
    sc.line(add(G, d(150), 0.42), (G[0] - 1.1, G[1] + 0.6), ORANGE, 1.0)
    sc.label((G[0] - 1.1, G[1] + 0.6), S("Q", "r") + " = L " + S("F", "w") + " " + J2, ORANGE, "end", 15, weight="700", dx=-4, dy=-4)
    # contact forces at P
    sc.vec(P, (P[0], P[1] + 0.6), None, "GREEN", 3.0, head=12)
    sc.label((P[0], 0.3), "N", "GREEN", "end", 17, weight="700", dx=-8, dy=5)
    sc.vec(P, (P[0] - 1.2, 0.0), None, "GREEN", 3.0, head=12)
    sc.label((P[0] - 1.2, 0.0), S("T", "1"), "GREEN", "end", 16, weight="700", dx=-8, dy=-8)
    sc.note((P[0] + 0.45, -0.5), "T" + '<tspan baseline-shift="sub" font-size="70%">2</tspan>' + " along " + J2 + " (normal to the paper)", "TEXT", "start", 13)
    # arm G to P, drawn offset to the left of the line GP
    off = -0.5
    sc.dim((G[0] + off, G[1]), (P[0] + off, 0.0), "", off=(0, 0))
    sc.dashed(G, (G[0] + off - 0.1, G[1]))
    sc.dashed(P, (P[0] + off - 0.1, 0.0))
    sc.label((P[0] + off, R / 2), "−R " + K, "TEXT", "end", 15, dx=-8, dy=5)
    # action-reaction connectors between the two parts
    sc.dashed(add(G1, (0.0, 0.0)), (G1[0], G[1] + R + 0.12))
    sc.note((G1[0] + 0.1, 3.0), "action – reaction", "TEXT", "start", 13)
    sc.note((G1[0] + 0.1, 2.75), "pair at G", "TEXT", "start", 13)
    return sc
