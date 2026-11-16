"""Problem RB-02: body with a point P on Oy, the axis Px_B through the fixed point A and the angle theta."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, d, rotation_view, sub
from figures.mech import S, Scene, bold

TH = 35.0


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


@figure("rb02-triangle-opa",
        "Right triangle formed by O, the fixed point A on Ox and the point P on Oy, with the angle theta at A.",
        r"Plane $Oxy$. The axis $Px_B$ is the hypotenuse $PA$ of the right triangle $OPA$; with the angle $\theta$ at $A$, "
        r"the opposite leg gives the position of $P$ and the hypotenuse has length $a/\cos\theta$.")
def triangle_opa():
    sc = Scene(700, 500, (130, 400), 330)
    t = math.radians(TH)
    O, A, P = (0.0, 0.0), (1.0, 0.0), (0.0, math.tan(t))
    triangle(sc, [O, A, P], "BLUE", 0.12)
    fixed_axis(sc, O, 0, 1.5, _ax("x"), off=(14, 6))
    fixed_axis(sc, O, 90, 1.0, _ax("y"), off=(14, 4))
    axis_out(sc, O, None, "HEAD")
    sc.label(O, _ax("k"), "HEAD", "end", 16, weight="700", dx=-14, dy=-8)
    sc.label(O, "O", "HEAD", "end", 17, dx=-14, dy=24)
    right_angle(sc, O, 0, 90, 0.05)
    # the axis P x_B: hypotenuse PA, extended a little beyond A
    u = (math.cos(t), -math.sin(t))
    sc.line(P, A, "HEAD", 2.0)
    sc.line(A, add(A, u, 0.2), "HEAD", 2.0, "6 4")
    sc.label(add(A, u, 0.2), S("Px", "B"), "HEAD", "start", 17, dx=8, dy=14)
    # dashed horizontal through P (parallel to Ox)
    sc.dashed(P, (1.15, P[1]))
    # unit vector i_B = i_1 along PA
    tip = add(P, u, 0.35)
    sc.vec(P, tip, None, "BLUE", 2.8, head=11)
    sc.label(tip, _ax("i", "B") + " = " + _ax("i", "1"), "BLUE", "end", 17, weight="700", dx=-2, dy=34)
    # angle theta at A and at P
    sc.arc(A, 0.28, 180 - TH, 180, "GREEN", 1.7, head=True)
    sc.label(add(A, d(180 - TH / 2), 0.40), "θ", "GREEN", "middle", 17, dy=5)
    sc.arc(P, 0.30, -TH, 0, "GREEN", 1.7, head=True)
    sc.label(add(P, d(-TH / 2), 0.43), "θ", "GREEN", "middle", 17, dy=5)
    # legs and hypotenuse
    sc.label((0.5, 0.0), "a", "TEXT", "middle", 17, dy=26)
    sc.label((0.0, P[1] / 2), "a tan θ", "TEXT", "end", 17, dx=-10, dy=5)
    sc.label((0.5, P[1] / 2), "a / cos θ", "TEXT", "start", 17, dx=12, dy=-12)
    for pt, nm, off in ((A, "A", (6, 24)), (P, "P", (-14, -8))):
        sc.mass(pt, None, r=5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    return sc


@figure("rb02-rotation-k",
        "View along k showing the first rotation, clockwise by theta, that takes i and j to i1 and j1.",
        r"First rotation, viewed with $\mathbf k$ out of the paper. The axis $Px_B$ turns clockwise from $\mathbf i$ by "
        r"$\theta$, the negative sense about $\mathbf k$, so $\mathbf i_1$ has the component $-\sin\theta$ along $\mathbf j$.")
def rotation_k():
    return rotation_view(540, 470, (200, 300), 160, -TH, _ax("i"), _ax("j"), _ax("i", "1"), _ax("j", "1"),
                         _ax("k") + " (⊙)", ("θ", ""), note="rotation −θ about k", note_pos=(-1.1, -0.75),
                         out_off=(-18, 26))


@figure("rb02-rotation-i1",
        "View along i1 showing the second rotation, counterclockwise by theta, that lifts jB above the plane Oxy.",
        r"Second rotation, viewed with $\mathbf i_1$ out of the paper. Turning about $\mathbf i_1$ keeps $Px_B$ in the plane "
        r"$Oxy$ and lifts $Py_B$ above that plane by the angle $\theta$, as the third condition requires.")
def rotation_i1():
    def pre(sc):
        sc.line((-1.4, 0.0), (0.0, 0.0), "EDGE", 1.2, "6 4")
        sc.note((-1.4, 0.0), "plane Oxy", "TEXT", "start", 14, dx=0, dy=-8)

    def post(sc):
        c, s = math.cos(math.radians(TH)), math.sin(math.radians(TH))
        sc.note((c, s / 2), "lift of " + S("Py", "B") + " above Oxy", "TEXT", "start", 13, dx=9, dy=26)

    return rotation_view(620, 470, (250, 330), 160, TH, _ax("j", "1"), _ax("k", "1"), _ax("j", "B"), _ax("k", "B"),
                         _ax("i", "1") + " (⊙)", ("θ", ""), pre=pre, post=post, out_off=(-16, 26))
