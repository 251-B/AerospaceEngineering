"""Problem RB-34: velocity field of a rigid body in pure rotation at one instant (points A and B)."""
import math

from figures.em_solutions import figure
from figures.em_sol.rb01 import add, norm, p3, p3v, sub, vadd, vscale, vsub
from figures.mech import S, Scene, bold


def _right_mark(sc, corner, u, w, s=0.12):
    """Right-angle mark at `corner` (3D point) between the unit directions u and w."""
    p1 = vadd(corner, u, s)
    p2 = vadd(p1, w, s)
    p3_ = vadd(corner, w, s)
    sc.poly([p3v(p1), p3v(p2), p3v(p3_)], "EDGE", 1.2)


@figure("rb34-velocity-field",
        "Points A and B of the body with their velocities, the angular velocity and the instantaneous axis of rotation "
        "through the point I.",
        r"Snapshot of the body. The foot $I$ of the perpendicular from $A$ to the instantaneous axis has zero velocity; "
        r"the axis is parallel to $\boldsymbol\omega_{b0}$.")
def velocity_field():
    sc = Scene(780, 500, (210, 330), 150)
    A, B = (0.0, 0.0, 0.0), (1.0, 0.0, 0.0)
    I = (4 / 9, 5 / 9, -2 / 9)
    w = (-2.0, 2.0, 1.0)
    for tip, nm, off in ((p3(1.45, 0, 0), bold("i"), (-12, 14)), (p3(0, 1.9, 0), bold("j"), (14, 6)),
                         (p3(0, 0, 1.45), bold("k"), (-12, -2))):
        sc.vec((0.0, 0.0), tip, None, "EDGE", 1.4, head=8)
        sc.label(tip, nm, "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    # instantaneous axis through I (dashed green) and omega from I
    sc.line(p3v(vadd(I, w, -0.35)), p3v(vadd(I, w, 0.75)), "GREEN", 1.5, "7 5")
    sc.note(p3v(vadd(I, w, 0.75)), "IAR", "GREEN", "start", 14, dx=8, dy=2)
    sc.vec(p3v(I), p3v(vadd(I, w, 0.4)), None, "GREEN", 3.4, head=12)
    sc.label(p3v(vadd(I, w, 0.4)), sub("ω", "b0"), "GREEN", "middle", 18, weight="700", dx=-6, dy=-14)
    # AI (blue dashed arrow) and the right angle at I
    sc.line(p3v(A), p3v(I), "BLUE", 2.0, "6 4")
    sc.vec((0.0, 0.0), p3v(I), None, "BLUE", 0.1, head=11)
    sc.label(p3v(vscale(I, 0.5)), sub("AI", ""), "BLUE", "middle", 16, weight="700", dx=-14, dy=22)
    _right_mark(sc, I, norm(vsub(A, I)), norm(w))
    # segment AB and the velocities (orange, scale 0.45)
    sc.line(p3v(A), p3v(B), "HEAD", 2.4)
    kv = 0.45
    vA, vB = (1.0, 0.0, 2.0), (1.0, 1.0, 0.0)
    sc.vec(p3v(A), p3v(vscale(vA, kv)), sub("v", "0", "A"), "ACC", 2.8, name_off=(-28, -4), size=17, head=11)
    sc.vec(p3v(B), add(p3v(B), p3v(vscale(vB, kv))), sub("v", "0", "B"), "ACC", 2.8, name_off=(2, 22), size=17, head=11)
    for pt, nm, off in ((A, "A", (14, -12)), (B, "B", (-14, 18))):
        sc.mass(p3v(pt), None, r=5, col="BLUE")
        sc.label(p3v(pt), nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.dotp(p3v(I), 4.5)
    sc.label(p3v(I), "I", "HEAD", "middle", 17, dx=14, dy=20)
    return sc
