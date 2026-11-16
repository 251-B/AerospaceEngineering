"""Problem RB-07: ring tilted 45 degrees rolling on the ground plane, section through G and attraction of Mordor."""
import math

from figures.em_solutions import axis_in, figure, fixed_axis, right_angle, triangle, unit
from figures.em_sol.rb01 import add, arrow_px, p3, p3v, ring, sub, vadd, vscale, vsub
from figures.em_sol.rb06 import rotation_view2
from figures.mech import S, Scene, bold


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


@figure("rb07-rotation",
        "View of the plane Oxz showing the body axes of the ring turned 45 degrees about the axis normal to the paper.",
        r"The body basis of the ring is $\mathcal B_0$ turned by $45^\circ$ about $-\mathbf j$ (out of the paper, "
        r"$\mathbf j$ ⊗). The axis $\mathbf k_B$ leans to negative $\mathbf i$, which gives the minus sign of "
        r"$[{}_0R_B]$.")
def rotation():
    def post(sc):
        sc.note((0.0, 0.0), "rotation +45° about −j (out of the paper)", "TEXT", "start", 13, dx=16, dy=44)

    return rotation_view2(660, 500, (250, 340), 160, 45.0, _ax("i"), _ax("k"), _ax("i", "B"), _ax("k", "B"),
                          _ax("j") + " = " + _ax("j", "B") + " (⊗)", ("45°", ""), post=post, out_kind="in",
                          out_off=(-16, 30))


@figure("rb07-contact-section",
        "Vertical section through the tilted ring showing the centre G, the contact point C on the ground and the "
        "height of G.",
        r"Section of the ring by the plane $Oxz$. The coordinates of $C$ in the body frame, turned into $\mathcal B_0$, "
        r"give the height of $G$, $\sqrt2 R/2$, and the horizontal offset $9\sqrt2 R/20$ of the contact point.")
def contact_section():
    sc = Scene(700, 480, (330, 360), 170)
    s2 = math.sqrt(2.0) / 2
    G, F = (0.0, s2), (0.0, 0.0)
    iB, kB = (s2, s2), (-s2, s2)
    C = (9 * math.sqrt(2.0) / 20, 0.0)
    J = add(G, iB, -0.05)
    # ground plane z = 0
    sc.ground((-1.35, 0.0), (1.55, 0.0), side=-1)
    sc.note((-1.35, 0.0), "ground plane Oxy (z = 0)", "TEXT", "start", 13, dy=-10)
    # the ring seen edge-on: thin band along k_B (half width R/20, half length 0.95 R so that C is its lowest corner)
    hl, hw = 0.95, 0.05
    band = [add(add(G, kB, hl), iB, hw), add(add(G, kB, hl), iB, -hw), add(add(G, kB, -hl), iB, -hw),
            add(add(G, kB, -hl), iB, hw)]
    sc.poly(band, "HEAD", 1.4, fill="HEAD", close=True, opacity=0.14)
    # key right triangle G - C - F
    triangle(sc, [G, C, F], "GREEN", 0.16)
    sc.line(G, F, "GREEN", 1.2, "6 4")
    sc.line(F, C, "GREEN", 1.2, "6 4")
    right_angle(sc, F, 90, 0, 0.07)
    # the two dashed segments of r_G^C in the body frame and the vector itself
    sc.line(G, J, "BLUE", 1.8, "4 3")
    sc.line(J, C, "BLUE", 1.8, "6 4")
    right_angle(sc, J, 45 + 180, 45 + 180 + 90, 0.05)
    sc.vec(G, C, None, "ACC", 2.6, head=10)
    M = ((J[0] + C[0]) / 2, (J[1] + C[1]) / 2)
    sc.label(add(M, iB, 0.12), S(bold("r"), "G", "C"), "ACC", "start", 17, weight="700", dx=10, dy=4)
    sc.label(J, "R/20", "BLUE", "end", 15, italic=False, dx=-14, dy=-8)
    sc.label(add(M, iB, -0.12), "19R/20", "BLUE", "end", 15, italic=False, dx=-6, dy=4)
    sc.label((0.0, s2 / 2), "z" + S("", "G") + " = √2 R/2", "TEXT", "end", 15, dx=-10, dy=5)
    sc.label((C[0] / 2, 0.0), "9√2 R/20", "TEXT", "middle", 15, italic=False, dy=-10)
    # body axes at G
    sc.vec(G, add(G, iB, 0.55), _ax("i", "B"), "BLUE", 2.8, name_off=(16, -6), size=17, head=11)
    sc.vec(G, add(G, kB, 0.55), _ax("k", "B"), "BLUE", 2.8, name_off=(-16, -8), size=17, head=11)
    sc.dotp(G, 4.0)
    sc.label(G, "G", "HEAD", "middle", 17, dx=-16, dy=20)
    sc.mass(C, None, r=5, col="ACC")
    sc.label(C, "C", "HEAD", "middle", 17, dx=16, dy=-14)
    # j into the paper
    axis_in(sc, (0.95, 1.25), None, "HEAD")
    sc.label((0.95, 1.25), _ax("j") + " = " + _ax("j", "B"), "HEAD", "start", 16, weight="700", dx=16, dy=5)
    return sc


@figure("rb07-mordor",
        "The ring attracted by Mordor at the origin, with the force on one mass element and the resultant applied at "
        "the centre of mass.",
        r"The attraction of Mordor on each element points to $O$ and is proportional to $dm$ and to the distance. Its "
        r"resultant is $-\beta M\,\mathbf r_0^G$, applied at $G$, with zero moment about $G$.")
def mordor():
    sc = Scene(760, 560, (330, 400), 125)
    s2 = math.sqrt(2.0) / 2
    O = (0.0, 0.0, 0.0)
    G = (1.6, 0.0, s2)
    jB, kB = (0.0, 1.0, 0.0), (-s2, 0.0, s2)
    ex, ey, ez = (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)
    for tip, nm, off in ((vscale(ex, 2.3), "i", (-12, 14)), (vscale(ey, 2.9), "j", (12, 12)),
                         (vscale(ez, 2.0), "k", (-12, 2))):
        sc.vec((0.0, 0.0), p3v(tip), None, "EDGE", 1.4, head=8)
        sc.label(p3v(tip), bold(nm), "TEXT", "middle", 16, weight="700", dx=off[0], dy=off[1])
    # the ring
    pts = ring(G, jB, kB, 1.0)
    sc.poly(pts, "HEAD", 2.2, fill="HEAD", close=True, opacity=0.07)
    # a mass element P at 60 degrees
    a = math.radians(130)
    P = vadd(G, vadd(vscale(jB, math.cos(a)), kB, math.sin(a)))
    nP = math.sqrt(sum(x * x for x in P))
    sc.line(p3v(O), p3v(P), "EDGE", 1.3, "6 4")
    sc.line(p3v(G), p3v(P), "BLUE", 1.8)
    dF = vadd(P, P, -0.8 / nP)
    sc.vec(p3v(P), p3v(dF), None, "PINK", 2.2, head=10)
    sc.label(p3v(dF), "dF = −β " + S(bold("r"), "0", "P") + " dm", "PINK", "start", 16, weight="700", dx=18, dy=-12)
    sc.label(p3v(vscale(P, 0.5)), S(bold("r"), "0", "P"), "TEXT", "start", 16, weight="700", dx=6, dy=22)
    sc.label(p3v(vadd(G, vsub(P, G), 0.5)), S(bold("r"), "G", "P"), "BLUE", "end", 16, weight="700", dx=-10, dy=2)
    sc.mass(p3v(P), None, r=4.5, col="ACC")
    sc.label(p3v(P), "P", "HEAD", "middle", 17, dx=12, dy=-10)
    # resultant at G
    F = vadd(G, G, -1.0 / math.sqrt(sum(x * x for x in G)))
    sc.vec(p3v(G), p3v(F), None, "PINK", 3.6, head=13)
    sc.label(p3v(F), "F = −β M " + S(bold("r"), "0", "G"), "PINK", "start", 17, weight="700", dx=-60, dy=48)
    sc.dotp(p3v(G), 4.0)
    sc.label(p3v(G), "G", "HEAD", "middle", 17, dx=-12, dy=-10)
    sc.label(p3v(G), S("M", "G") + " = 0", "TEXT", "end", 16, dx=-14, dy=24)
    # Mordor at O
    sc.mass(p3v(O), None, r=7, col="HEAD")
    sc.label(p3v(O), "Mordor (O)", "HEAD", "start", 16, dx=14, dy=-12)
    return sc
