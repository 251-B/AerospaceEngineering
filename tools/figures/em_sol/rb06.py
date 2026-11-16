"""Problem RB-06: spinner (blade runner), two simple rotations and the instantaneous axis through the point I."""
import math

from figures.em_solutions import figure
from figures.em_sol.rb01 import add, arrow_px, d
from figures.mech import S, Scene, bold
from figures.em_solutions import axis_in, axis_out, fixed_axis, right_angle, triangle, unit


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


def rotation_view2(w, h, o, k, ang, right, up, m1, m2, out, hdr, col="BLUE", tri="ACC", pre=None, post=None,
                   out_off=(-16, 26), out_kind="out", L=1.0, arc_r=0.42, cy=0.72, side=None, lab_r=0.64, lab_off=(0, 5), jlab=None, m1_off=None, m2_off=None):
    """Like rb01.rotation_view (flat view of one elementary rotation, counterclockwise positive), with signed leg
    labels (the leg along the negative axis reads "-sin") and the cosine label of the second triangle on its own side.
    Shared by the Topic 7 modules rb06 .. rb38."""
    sc = Scene(w, h, o, k)
    O = (0.0, 0.0)
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    ccw = ang > 0
    side = side or ("right" if ccw else "left")
    Lf = 1.62 * max(L, 1.0) if L >= 1.0 else 1.62 * L + 0.6
    if pre:
        pre(sc)
    fixed_axis(sc, O, 0, Lf, right, off=(16, 6))
    fixed_axis(sc, O, 90, Lf, up, off=(16, 4))
    foot1, tip1 = (L * c, 0.0), (L * c, L * s)
    triangle(sc, [O, foot1, tip1], tri, 0.20)
    sc.dashed(foot1, tip1)
    right_angle(sc, foot1, 180, 90 if ccw else 270, 0.07 * L if L < 1 else 0.07)
    foot2, tip2 = (0.0, L * c), (-L * s, L * c)
    triangle(sc, [O, foot2, tip2], tri, 0.20)
    sc.dashed(foot2, tip2)
    right_angle(sc, foot2, 270, 180 if ccw else 0, 0.07 * L if L < 1 else 0.07)
    unit(sc, O, ang, L, m1, col, off=m1_off or ((18, -10) if ccw else (18, 18)))
    unit(sc, O, ang + 90, L, m2, col, off=m2_off or ((-6, -14) if ccw else (6, -14)))
    a = hdr[0]
    sc.label((L * c / 2, 0), "cos " + a, "TEXT", "middle", 15, dy=24 if ccw else -8)
    sc.label((L * c, L * s / 2), ("sin " if ccw else "−sin ") + a, "TEXT", "start", 15, dx=9, dy=5)
    sc.label((-L * s / 2, L * c), ("−sin " if ccw else "sin ") + a, "TEXT", "middle", 15, dy=-8)
    if side == "right":
        sc.label((0, L * c * cy), "cos " + a, "TEXT", "start", 15, dx=9, dy=5)
    else:
        sc.label((0, L * c * cy), "cos " + a, "TEXT", "end", 15, dx=-9, dy=5)
    sc.arc(O, arc_r, 0, ang, "GREEN", 1.7, head=True)
    sc.arc(O, arc_r, 90, 90 + ang, "GREEN", 1.7, head=True)
    sc.label(add(O, d(ang / 2), lab_r), a, "GREEN", "middle", 17, dx=lab_off[0], dy=lab_off[1])
    if jlab:
        sc.label(add(O, d(jlab[0]), jlab[1]), a, "GREEN", "middle", 17, dx=lab_off[0], dy=lab_off[1])
    else:
        sc.label(add(O, d(90 + ang / 2), lab_r), a, "GREEN", "middle", 17, dx=lab_off[0], dy=lab_off[1])
    (axis_out if out_kind == "out" else axis_in)(sc, O, None, "HEAD")
    sc.label(O, out, "HEAD", "end", 16, weight="700", dx=out_off[0], dy=out_off[1])
    if post:
        post(sc)
    return sc


def rlabel(sc, p, text, col="TEXT", deg=0.0, perp=0.0, size=15, anchor="middle", italic=False, weight="400"):
    """Text along a line at `deg` degrees (counterclockwise), anchored at the world point p and shifted by `perp`
    pixels to the left of the direction of the text. Shared by the Topic 7 modules."""
    from figures.mech import SERIF
    x, y = sc.P(p)
    a = math.radians(deg)
    x += perp * (-math.sin(a))
    y += perp * (-math.cos(a))
    style = ' font-style="italic"' if italic else ""
    sc.c.add(f'<text x="{x:.1f}" y="{y:.1f}" fill="{col}" font-size="{size}" font-weight="{weight}" '
             f'text-anchor="{anchor}" font-family="{SERIF}" style="font-variant-numeric:lining-nums"{style} '
             f'transform="rotate({-deg:.1f} {x:.1f} {y:.1f})">{text}</text>')


@figure("rb06-rotation-psi",
        "Top view of the first rotation of the spinner basis, 45 degrees about the vertical axis k, with the right "
        "triangles of its sines and cosines.",
        r"First simple rotation, by $45^\circ$ about $\mathbf k$ (⊙). The axis $\mathbf i_1$ takes the direction of the "
        r"length of the spinner; $\mathbf j_1$ leans to negative $\mathbf i$, which gives the minus sign of $[{}_0R_1]$.")
def rotation_psi():
    return rotation_view2(620, 500, (230, 340), 160, 45.0, _ax("i"), _ax("j"), _ax("i", "1"), _ax("j", "1"),
                         _ax("k") + " (⊙)", ("45°", ""), out_off=(-16, 28))


def _half_turn(sc, r, start, col="GREEN"):
    """Counterclockwise arc of 180 degrees from the ray at `start` degrees, with an arrowhead."""
    pts = [add((0.0, 0.0), d(start + 180 * i / 60), r) for i in range(61)]
    sc.poly(pts, col, 1.8)
    arrow_px(sc, pts[-3], pts[-1], col, 9)


@figure("rb06-rotation-flip",
        "View along the axis of the car showing the half turn that sends the vertical axis down and the lateral axis to "
        "the left.",
        r"Second simple rotation, a half turn about $\mathbf i_1$ (⊙): $\mathbf j_B$ is opposite to $\mathbf j_1$ and "
        r"$\mathbf k_B$ points to the ground, as in the side view of the statement.")
def rotation_flip():
    sc = Scene(640, 520, (300, 250), 150)
    O = (0.0, 0.0)
    fixed_axis(sc, O, 0, 1.55, _ax("j", "1"), off=(18, 6))
    fixed_axis(sc, O, 90, 1.5, _ax("k", "1") + " = " + _ax("k"), off=(34, 6))
    unit(sc, O, 180, 1.0, _ax("j", "B"), off=(-8, -14))
    unit(sc, O, 270, 1.0, _ax("k", "B"), off=(20, 8))
    _half_turn(sc, 0.42, 0)
    _half_turn(sc, 0.62, 90)
    sc.label(add((0, 0), d(45), 0.62), "π", "GREEN", "middle", 17, dy=6)
    sc.label(add((0, 0), d(225), 0.8), "π", "GREEN", "middle", 17, dy=6)
    axis_out(sc, O, None, "HEAD")
    sc.label(O, _ax("i", "1") + " = " + _ax("i", "B"), "HEAD", "start", 16, weight="700", dx=14, dy=34)
    return sc


@figure("rb06-iar",
        "Body axes at the centre of mass with the velocity of G, the angular velocity and the instantaneous axis "
        "through the point I.",
        r"Instantaneous axis of rotation of the spinner. $I$ is the foot of the perpendicular from $G$; the axis is "
        r"parallel to $\boldsymbol\omega_{B0}$ and lies in the vertical plane of the car.")
def iar():
    sc = Scene(700, 560, (300, 330), 160)
    s2 = math.sqrt(2.0)

    def pr(x, y, z):
        """Cabinet view of the body frame: i_B right, k_B down, j_B towards the viewer (lower left, foreshortened)."""
        return (x - 0.433 * y, -z - 0.25 * y)

    G = (0.0, 0.0)
    for tip, nm, off in ((pr(1.25, 0, 0), _ax("i", "B"), (6, 20)), (pr(0, 0, 1.0), _ax("k", "B"), (-16, 10)),
                         (pr(0, 1.0, 0), _ax("j", "B"), (-18, 16))):
        sc.vec(G, tip, None, "EDGE", 1.4, head=8)
        sc.label(tip, nm, "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    I = pr(-0.5, 0, -s2 / 2)
    # instantaneous axis: dashed green line through I along (sqrt2, 0, -1)
    u = pr(s2, 0, -1.0)
    sc.line(add(I, u, -0.78), add(I, u, 0.95), "GREEN", 1.5, "7 5")
    sc.note(add(I, u, 0.95), "IAR", "GREEN", "start", 15, dx=8, dy=0)
    # dashed projections of I and the arm GI
    sc.dashed(G, pr(-0.5, 0, 0))
    sc.dashed(pr(-0.5, 0, 0), I)
    sc.label(pr(-0.25, 0, 0), "L/2", "TEXT", "middle", 15, dy=-9)
    sc.label(pr(-0.5, 0, -s2 / 4), "√2 L/2", "TEXT", "end", 15, dx=-8, dy=5)
    sc.line(G, I, "BLUE", 2.0, "6 4")
    arrow_px(sc, G, I, "BLUE", 10)
    sc.label(pr(-0.25, 0, -s2 / 4), "GI", "BLUE", "start", 17, weight="700", dx=10, dy=4)
    # right angle at I between IG and the axis
    ug = (0.5, -s2 / 2)
    n = math.hypot(*ug)
    a = (ug[0] / n, ug[1] / n)
    b = (u[0] / math.hypot(*u), u[1] / math.hypot(*u))
    q = 0.07
    sc.poly([add(I, a, q), add(add(I, a, q), b, q), add(I, b, q)], "EDGE", 1.1)
    # velocity of G and angular velocity at I
    vG = pr(0, -1.5 * 0.4, 0)
    sc.vec(G, vG, None, "ACC", 2.8, head=11)
    sc.label(vG, S(bold("v"), "0", "G"), "ACC", "start", 17, weight="700", dx=8, dy=0)
    w = pr(s2 * 0.4, 0, -0.4)
    sc.vec(I, add(I, w), None, "GREEN", 3.2, head=12)
    sc.label(add(I, w), S(bold("ω"), "B0"), "GREEN", "start", 17, weight="700", dx=-26, dy=-16)
    # point A and the points G, I
    A = pr(0.5, 0.25, 0)
    ax, ay = sc.P(A)
    sc.c.add(f'<rect x="{ax - 5:.1f}" y="{ay - 5:.1f}" width="10" height="10" fill="HEAD"/>')
    sc.label(A, "A", "HEAD", "middle", 17, dx=-4, dy=24)
    sc.dotp(G, 4.0)
    sc.label(G, "G", "HEAD", "middle", 17, dx=14, dy=20)
    sc.dotp(I, 4.5)
    sc.label(I, "I", "HEAD", "middle", 17, dx=-14, dy=-8)
    return sc
