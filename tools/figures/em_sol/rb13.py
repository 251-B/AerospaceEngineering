"""Problem RB-13: flat sheet (disc with a circular hole) rolling and sliding on a rough horizontal line."""
import math

from figures.em_solutions import figure, right_angle, triangle
from figures.em_sol.rb01 import add, d, sub
from figures.em_sol.rb12 import ground_line, plane_rotation
from figures.mech import S, Scene, bold

ORANGE = "ACC"
R = 3.0
TH = 30.0
TR = math.radians(TH)
IBV = (math.cos(TR), math.sin(TR))
X = 2.0
O = (X, R)
OH = (O[0] + R / 2 * IBV[0], O[1] + R / 2 * IBV[1])
G = (O[0] - R / 6 * IBV[0], O[1] - R / 6 * IBV[1])
C = (X, 0.0)


def sheet(sc, o, r_out, oh, r_hole, fill="ACC", opacity=0.20, w=2.2):
    """Disc of radius r_out with a circular hole, as one even-odd path (the hole stays transparent)."""
    def circ(c, r):
        x, y = sc.P(c)
        rp = r * sc.k
        return f"M{x - rp:.1f},{y:.1f} A{rp:.1f},{rp:.1f} 0 1 0 {x + rp:.1f},{y:.1f} A{rp:.1f},{rp:.1f} 0 1 0 {x - rp:.1f},{y:.1f} Z"
    sc.c.add(f'<path d="{circ(o, r_out)} {circ(oh, r_hole)}" fill="{fill}" fill-opacity="{opacity}" fill-rule="evenodd" '
             f'stroke="HEAD" stroke-width="{w}"/>')


def _scene_sheet(faint=False):
    sc = Scene(800, 700, (200, 600), 92)
    ground_line(sc, -1.6, 5.9)
    sheet(sc, O, R, OH, R / 2, opacity=0.20)
    return sc


@figure("rb13-rotation",
        "The body basis of the sheet, with i_B pointing to the centre of the hole, turned counterclockwise by theta.",
        r"Rotation about $\mathbf k$ (⊙) by $\theta$. The initial spin of the statement is clockwise, so the initial rate "
        r"of $\theta$ is $-\omega$.")
def rotation():
    sc = plane_rotation(760, 620, (270, 500), 250, 35.0,
                        (bold("i"), bold("j"), S(bold("i"), "B"), S(bold("j"), "B")),
                        bold("k") + " (⊙)", ("θ", ""), None)
    sc.spin((0.0, 0.0), 0.17, -10, -120, "", "GREEN")
    sc.label((0.14, -0.33), "initial spin: −ω " + bold("k") + " (⊗)", "GREEN", "start", 15)
    sc.note((math.cos(math.radians(35)), math.sin(math.radians(35))), "towards the centre of the hole", "TEXT", "start", 13,
            dx=14, dy=30)
    return sc


@figure("rb13-geometry",
        "The sheet with its hole, the contact point below O and the centre of mass G at R/6 from O, opposite to the hole.",
        r"Main plane. $C$ is always below $O$; $G$ lies on the line of $\mathbf i_B$ at $R/6$ from $O$, on the side "
        r"opposite to the hole, with the legs $\tfrac R6\cos\theta$ and $\tfrac R6\sin\theta$.")
def geometry():
    sc = _scene_sheet()
    # contact radius
    sc.dashed(O, C)
    sc.label(((O[0] + C[0]) / 2, R / 2), "R", "TEXT", "start", 16, dx=10, dy=5)
    # triangle of OG
    A = (O[0] - R / 6 * math.cos(TR), O[1])
    triangle(sc, [O, A, G], ORANGE, 0.45)
    sc.line(O, G, "ACC", 1.8)
    sc.dashed(O, A)
    sc.dashed(A, G)
    right_angle(sc, A, 0, 270, 0.06)
    sc.label(A, "(R/6) cos θ", "TEXT", "end", 14, dx=-8, dy=5)
    sc.label(G, "(R/6) sin θ", "TEXT", "end", 14, dx=-8, dy=5)
    sc.label(((O[0] + G[0]) / 2, (O[1] + G[1]) / 2), "R/6", "TEXT", "middle", 14, dx=-4, dy=26)
    # body axis and velocity
    sc.vec(O, add(O, IBV, 1.1), sub("i", "B"), "BLUE", 2.8, name_off=(10, -12), size=17, head=11)
    sc.vec(O, (O[0] + 1.5, O[1]), "ẋ " + bold("i"), "GREEN", 2.6, name_off=(26, 18), size=17, head=11)
    # abscissa x
    yd = -0.62
    sc.dim((0.0, yd), (X, yd), "x", off=(0, -9))
    sc.dashed((0.0, 0.0), (0.0, yd - 0.12))
    sc.dashed(C, (X, yd - 0.12))
    for pt, nm, off in ((C, "C", (16, 22)), (G, "G", (-12, 26)), (O, "O", (4, -24)), (OH, sub("O", "h"), (4, 24))):
        sc.mass(pt, None, r=4.5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.dotp((0.0, 0.0), 3.5)
    sc.label((0.0, 0.0), "Q", "HEAD", "middle", 17, dx=-14, dy=-10)
    return sc


@figure("rb13-composite",
        "The sheet as a full disc minus a hole, with the polar mass element and the positions of O, O_h and G.",
        r"Composite body: full disc of mass $\tfrac43 m$ minus the hole of mass $\tfrac13 m$. Both moments of inertia "
        r"come from the polar element $dm = \sigma\,r\,dr\,d\alpha$; the hole is moved from $O_h$ to $O$ by the parallel "
        r"axis theorem.")
def composite():
    sc = Scene(920, 400, (130, 180), 62)
    r = 2.0
    cd, ch, cs = (0.0, 0.0), (5.0, 0.0), (10.0, 0.0)
    # full disc D
    sc.circle(cd, r, "HEAD", 2.0, fill="EDGE", opacity=0.14)
    sc.vec(cd, (0.95, 0.0), sub("i", "B"), "BLUE", 2.8, name_off=(2, -14), size=17, head=11)
    # annular element at radius 1.45, width 0.3 (drawn larger than dr for clarity)
    for rr in (1.30, 1.62):
        sc.circle(cd, rr, "ACC", 1.3, dash="5 3")
    sc.circle(cd, 1.46, "ACC", 10.0, opacity=0.25)
    sc.line(cd, add(cd, d(115), 1.46), "ACC", 1.5)
    sc.label(add(cd, d(115), 0.75), "r", "TEXT", "middle", 16, dx=-10, dy=0)
    sc.label(add(cd, d(-50), 1.81), "dr", "TEXT", "middle", 14, dy=5)
    sc.label((0.0, -0.85), "dm = σ r dr dα", "ACC", "middle", 14, weight="700")
    sc.dotp(cd, 3.5)
    sc.label(cd, "O", "HEAD", "middle", 17, dx=-12, dy=18)
    sc.label((0.0, -2.0), "D: mass 4m/3", "HEAD", "middle", 17, italic=False, dy=26)
    # hole H
    sc.circle(ch, r / 2, "HEAD", 2.0, fill="EDGE", opacity=0.14)
    sc.dotp(ch, 3.5)
    sc.label(ch, sub("O", "h"), "HEAD", "middle", 17, dx=-4, dy=-16)
    sc.label((5.0, -2.0), "H: mass m/3", "HEAD", "middle", 17, italic=False, dy=26)
    # sheet
    sheet(sc, cs, r, (cs[0] + r / 2, 0.0), r / 2, opacity=0.20)
    gx = cs[0] - r / 6
    for pt, nm, off in ((cs, "O", (-10, -14)), ((cs[0] + r / 2, 0.0), sub("O", "h"), (0, -14)), ((gx, 0.0), "G", (-6, 22))):
        sc.mass(pt, None, r=4.2, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    yd = -2.55
    sc.dim((gx, yd), (cs[0], yd), "", col="EDGE")
    sc.label((gx - 0.05, yd), "R/6", "TEXT", "end", 14, dx=-4, dy=5)
    sc.dim((cs[0], yd), (cs[0] + r / 2, yd), "R/2", off=(0, 18))
    for x in (gx, cs[0], cs[0] + r / 2):
        sc.dashed((x, 0.0), (x, yd - 0.12))
    # operators
    sc.label((2.5, 0.0), "−", "TEXT", "middle", 36, italic=False, dy=12)
    sc.label((7.5, 0.0), "=", "TEXT", "middle", 36, italic=False, dy=12)
    return sc


@figure("rb13-fbd",
        "Free-body diagram of the sheet: weight at G, normal reaction and friction at the contact point.",
        r"Free-body diagram. About $G$, the normal reaction has the arm $\tfrac R6\cos\theta$ and the friction force "
        r"the arm $R - \tfrac R6\sin\theta$.")
def fbd():
    sc = Scene(860, 700, (200, 600), 92)
    ground_line(sc, -1.6, 5.9)
    sheet(sc, O, R, OH, R / 2, opacity=0.10, w=2.0)
    corner = (G[0], 0.0)
    sc.dashed(G, corner)
    sc.dashed(corner, C)
    sc.dashed(G, C)
    sc.label((C[0], 0.0), "(R/6) cos θ", "TEXT", "end", 14, dx=-6, dy=34)
    sc.label((G[0], 1.0), "R − (R/6) sin θ", "TEXT", "end", 14, dx=-8, dy=5)
    sc.vec(G, (G[0], G[1] - 1.0), "mg", "PINK", 3.0, name_off=(-24, 4), size=17, head=12)
    sc.vec(C, (C[0], C[1] + 1.4), "N", "GREEN", 3.0, name_off=(16, 4), size=17, head=12)
    sc.vec(C, (C[0] + 1.4, 0.0), "F (zero if μ = 0)", "GREEN", 3.0, name_off=(74, 18), size=16, head=12)
    sc.spin(G, 0.45, 100, 200, "θ̈", "GREEN", name_r=0.72)
    for pt, nm, off in ((C, "C", (16, 22)), (G, "G", (14, 22))):
        sc.mass(pt, None, r=4.5, col="BLUE")
        sc.label(pt, nm, "HEAD", "middle", 17, dx=off[0], dy=off[1])
    sc.dotp(O, 3.5)
    sc.label(O, "O", "HEAD", "middle", 17, dx=4, dy=-24)
    sc.dotp((0.0, 0.0), 3.5)
    sc.label((0.0, 0.0), "Q", "HEAD", "middle", 17, dx=-14, dy=-10)
    return sc
