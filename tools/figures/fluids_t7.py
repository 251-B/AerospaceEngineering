"""Topic 7 figures for Fluid Mechanics: viscous flows (Notes.pdf, Chapter 7) and the problems VF2-VF20.

Theory figures (this module): Figs. 7.1 to 7.6 of the notes redrawn (the pipe control volume, Rayleigh's layer, the
discharge pipe of variable section, the entrance region at small and large Reynolds number, the plane bearing and the
wedge effect) plus a sketch of the Couette, Poiseuille and combined profiles (an extension). Problem figures:
tools/figures/fluids_t7p.py.

Colour code: BLUE velocity profiles and the liquid, ACC pressure and forces, GREEN dimensions and scales, HEAD/TEXT/EDGE
lines and labels.
"""
import math

from figures.fluids_t5 import arc
from figures.fluids_t6 import lab, note
from figures.svgkit import Canvas, Registry, arrow, circle, dim, dot, hatch, line, pathd, poly, rect, sub

REG = Registry("FM-T7")
RASTER = {}                     # name -> (alt, caption): crops of the official sheets, filled by fluids_t7p


def parabola(c, x0, yc, R, vmax, col="BLUE", n=7, w=1.8, fill=True):
    """Poiseuille profile of a pipe along x: the curve x = x0 + vmax (1 - (s/R)^2), with arrows from the axis section."""
    pts = [(x0 + vmax * (1 - (s / R) ** 2), yc + s) for s in [(-R + 2 * R * i / 40) for i in range(41)]]
    pathd(c, "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts), col, w)
    for i in range(n):
        s = -R + R * (i + 0.5) * 2 / n
        arrow(c, (x0, yc + s), (x0 + vmax * (1 - (s / R) ** 2), yc + s), col, 1.1, 6)
    line(c, (x0, yc - R), (x0, yc + R), "EDGE", 0.8, dash="3,3")


# ----------------------------------------------------------------------------------------------- Fig. 7.1
def pipe_cv():
    c = Canvas(640, 300)
    yc, R = 150, 70
    line(c, (90, yc - R), (560, yc - R), "HEAD", 2.4)
    line(c, (90, yc + R), (560, yc + R), "HEAD", 2.4)
    parabola(c, 120, yc, R, 55)
    parabola(c, 510, yc, R, 55)
    rect(c, 165, yc - R + 6, 310, 2 * R - 12, "ACC", 1.6, dash="6,4", fill="ACC", opacity=0.06)
    for p, q in (((165, yc), (140, yc)), ((475, yc), (500, yc)), ((320, yc - R + 6), (320, yc - R - 16)),
                 ((320, yc + R - 6), (320, yc + R + 16))):
        arrow(c, p, q, "HEAD", 1.6, 8)
    for x, y in ((135, yc + 12), (505, yc + 12), (332, yc - R - 6), (332, yc + R + 24)):
        lab(c, (x, y), "n̄", "HEAD", "middle", 15)
    lab(c, (150, 62), sub("P", "1"), "ACC", "middle", 18)
    lab(c, (490, 62), sub("P", "2"), "ACC", "middle", 18)
    dim(c, (165, 268), (475, 268), "L", "GREEN", (0, 18), size=17)
    line(c, (165, 258), (165, 276), "EDGE", 0.8)
    line(c, (475, 258), (475, 276), "EDGE", 0.8)
    dim(c, (588, yc - R), (588, yc + R), "2a", "GREEN", (16, 5), size=16)
    note(c, (320, 292), "control volume Σc of a fully developed laminar flow, Poiseuille profile at both ends", "TEXT", "middle", 13)
    REG.put("t7-pipe-cv", c, "Fully developed laminar flow in a circular pipe (Fig. 7.1 of the notes)",
            "Fully developed laminar flow in a circular pipe, Fig. 7.1 of the notes: the control volume Σc of length L, "
            "radius a and outward normal n̄, with reduced pressures P_1 and P_2 at its ends and the same Poiseuille "
            "profile at both")


# ----------------------------------------------------------------------------------------------- Fig. 7.2
def rayleigh():
    c = Canvas(640, 300)
    y0 = 250                                                    # the wall; liquid above
    line(c, (60, y0), (600, y0), "HEAD", 3.0)
    hatch(c, (60, y0 + 2), (600, y0 + 2), side=-1, col="EDGE", step=12)
    arrow(c, (80, y0 + 26), (170, y0 + 26), "ACC", 3.0, 12)
    lab(c, (205, y0 + 32), "V", "ACC", "start", 19)
    ax = 100
    line(c, (ax, y0), (ax, 40), "HEAD", 1.2, head=True)
    lab(c, (ax - 8, 52), "y", "HEAD", "end", 17)
    line(c, (ax, y0), (590, y0), "HEAD", 1.2, head=True)
    lab(c, (588, y0 - 8), "x", "HEAD", "end", 17)
    cols = ("BLUE", "BLUE", "BLUE")
    for k, d in enumerate((50, 100, 160)):                      # delta grows like sqrt(t)
        xs = 200 + k * 130
        pts = [(xs + 90 * math.erfc(2 * s / d) , y0 - s) for s in range(0, 190, 5)]
        pathd(c, "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts), cols[k], 2.0)
        line(c, (xs, y0), (xs, y0 - 190), "EDGE", 0.8, dash="3,3")
        for s in (10, 30, 55, 85):
            if s < 2.0 * d:
                arrow(c, (xs, y0 - s), (xs + 90 * math.erfc(2 * s / d), y0 - s), "BLUE", 1.0, 6)
        line(c, (xs - 14, y0 - d), (xs + 8, y0 - d), "GREEN", 1.2)
        lab(c, (xs - 18, y0 - d + 5), "δ", "GREEN", "end", 17)
        note(c, (xs, 30), f"t{'₁₂₃'[k]}", "TEXT", "middle", 14)
    note(c, (340, 292), "δ(t) ~ (νt)^(1/2) grows while the wall velocity V stays fixed", "TEXT", "middle", 13)
    REG.put("t7-rayleigh", c, "Variation with t of the velocity for Rayleigh's problem (Fig. 7.2 of the notes)",
            "Rayleigh's problem, Fig. 7.2 of the notes: velocity profiles at three increasing times above a wall set in "
            "motion with velocity V at t = 0; the layer of moving liquid thickens as δ ~ (νt)^(1/2)")


# ----------------------------------------------------------------------------------------------- Fig. 7.3
def variable_pipe():
    c = Canvas(680, 300)
    pathd(c, "M60,110 L150,130 C260,125 380,150 470,140 L600,150", "HEAD", 2.4)
    pathd(c, "M60,210 L150,190 C260,195 380,190 470,180 L600,170", "HEAD", 2.4)
    liq = [(60, 110), (150, 130), (260, 128), (380, 142), (470, 140), (600, 150), (600, 170), (470, 180), (380, 188),
           (260, 193), (150, 190), (60, 210)]
    poly(c, liq, "BLUE", 0, fill="BLUE", close=True, opacity=0.10)
    pathd(c, "M60,110 L60,60 L40,60", "HEAD", 2.4)
    pathd(c, "M60,210 L60,260 L40,260", "HEAD", 2.4)
    lab(c, (30, 165), sub("P", "c") + "(t)", "ACC", "end", 18)
    pathd(c, "M170,160 C300,155 420,162 600,160", "EDGE", 1.0, dash="8,4,2,4")
    dim(c, (150, 120), (150, 200), "D", "GREEN", (-14, 5), size=17)
    line(c, (150, 235), (600, 235), "GREEN", 1.2, head=True)
    line(c, (600, 235), (150, 235), "GREEN", 1.2, head=True)
    lab(c, (375, 258), "L ≫ D", "GREEN", "middle", 17)
    lab(c, (664, 140), sub("P", "o"), "ACC", "middle", 18)
    for k in range(3):
        arrow(c, (606, 155 + 5 * k), (650, 155 + 5 * k), "BLUE", 1.4, 7)
    arrow(c, (480, 52), (400, 110), "HEAD", 1.0, 7)
    lab(c, (490, 50), "R ≫ D (curvature radius)", "HEAD", "start", 15)
    REG.put("t7-variable-pipe", c, "Discharge flow through a pipe of variable section (Fig. 7.3 of the notes)",
            "Discharge flow through a pipe of variable section, Fig. 7.3 of the notes: a container at reduced pressure "
            "P_c(t) feeds a slender pipe of diameter D, length L ≫ D and curvature radius R ≫ D that discharges at P_o")


# ----------------------------------------------------------------------------------------------- Fig. 7.4
def entrance():
    c = Canvas(680, 400)
    for yc, label, ent in ((100, "ρ " + sub("v", "L") + " D / μ ≲ 1", True), (290, "ρ " + sub("v", "L") + " D / μ ≫ 1", False)):
        D = 40
        line(c, (170, yc - D), (620, yc - D), "HEAD", 2.2)
        line(c, (170, yc + D), (620, yc + D), "HEAD", 2.2)
        for k in range(1, 4):                                   # streamlines coming from the container
            ang = 0.35 * k
            pathd(c, f"M60,{yc - 70 * k / 1.6:.0f} C130,{yc - 40 * k / 1.6:.0f} 160,{yc - 8 * k:.0f} 190,{yc - 8 * k:.0f}",
                  "BLUE", 1.0)
            pathd(c, f"M60,{yc + 70 * k / 1.6:.0f} C130,{yc + 40 * k / 1.6:.0f} 160,{yc + 8 * k:.0f} 190,{yc + 8 * k:.0f}",
                  "BLUE", 1.0)
        note(c, (110, yc + 3), "entrance region", "TEXT", "middle", 11)
        lab(c, (430, yc - D - 14), label, "ACC", "middle", 17, italic=False)
        if ent:
            parabola(c, 300, yc, D, 34, n=5)
            parabola(c, 500, yc, D, 34, n=5)
            dim(c, (185, yc + D + 16), (255, yc + D + 16), "D", "GREEN", (0, 16), size=15)
        else:
            # uniform profile at the entrance, boundary layers growing, Poiseuille after L_E
            for xs, lay in ((200, 3), (260, 9), (330, 17), (400, 25), (470, 33), (540, 40)):
                pts = [(xs + 34 * min(1.0, ((D - abs(s)) / lay) ** 0.7 if lay < D else (1 - (s / D) ** 2)), yc + s)
                       for s in range(-D, D + 1, 2)]
                pathd(c, "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts), "BLUE", 1.5)
            dim(c, (200, yc + D + 14), (470, yc + D + 14), "", "GREEN", (0, 0))
            lab(c, (338, yc + D + 36), sub("L", "E"), "GREEN", "middle", 16)
            line(c, (200, yc + D + 6), (200, yc + D + 22), "EDGE", 0.8)
            line(c, (470, yc + D + 6), (470, yc + D + 22), "EDGE", 0.8)
        dim(c, (170, 370 if not ent else 175), (620, 370 if not ent else 175), "L", "GREEN", (0, 18), size=16)
    REG.put("t7-entrance", c, "The entrance region in pipe flows dominated by viscosity (Fig. 7.4 of the notes)",
            "The entrance region in pipe flows dominated by viscosity, Fig. 7.4 of the notes: for ρ v_L D/μ ≲ 1 the "
            "Poiseuille profile is reached at a distance of order D; for ρ v_L D/μ ≫ 1 a boundary layer grows from the "
            "uniform entrance profile until it fills the pipe at x ~ L_E = ρ v_L D²/μ")


# ----------------------------------------------------------------------------------------------- Fig. 7.5
def bearing():
    c = Canvas(680, 260)
    y0 = 200
    line(c, (80, y0), (620, y0), "HEAD", 2.6)
    hatch(c, (80, y0 + 2), (620, y0 + 2), side=-1, col="EDGE", step=12)
    pathd(c, "M170,55 L170,90 C300,120 420,150 500,160 L500,55", "HEAD", 2.4)
    line(c, (170, 55), (500, 55), "HEAD", 1.0, dash="3,3")
    poly(c, [(170, 90), (300, 120), (420, 150), (500, 160), (500, y0), (170, y0)], "BLUE", 0, fill="BLUE", close=True,
         opacity=0.10)
    dim(c, (170, 40), (500, 40), "L", "GREEN", (0, -8), size=17)
    line(c, (420, 150), (420, y0), "GREEN", 1.2)
    lab(c, (428, 178), "h(x)", "GREEN", "start", 17)
    arrow(c, (260, 232), (400, 232), "ACC", 3.0, 12)
    lab(c, (330, 252), "V(t)", "ACC", "middle", 18)
    line(c, (110, y0), (110, 90), "HEAD", 1.2, head=True)
    lab(c, (100, 98), "y", "HEAD", "end", 16)
    line(c, (110, y0), (210, y0), "HEAD", 1.2, head=True)
    lab(c, (212, y0 - 8), "x", "HEAD", "start", 16)
    lab(c, (130, 130), sub("P", "o"), "ACC", "middle", 18)
    lab(c, (550, 130), sub("P", "o"), "ACC", "middle", 18)
    REG.put("t7-bearing", c, "Plane bearing (Fig. 7.5 of the notes)",
            "Plane bearing, Fig. 7.5 of the notes: a bearing of length L moves with velocity V(t) over a horizontal wall; "
            "the film of thickness h(x) is at the pressure P_o on both sides")


# ----------------------------------------------------------------------------------------------- Fig. 7.6
def wedge():
    c = Canvas(680, 520)
    X0, X1 = 110, 560
    def profile_row(y0, with_gradient):
        pathd(c, f"M{X0},{y0 - 120} C{X0 + 20},{y0 - 100} {X0 + 150},{y0 - 70} {X1 - 20},{y0 - 52} L{X1},{y0 - 120}",
              "HEAD", 2.0)
        line(c, (X0 - 20, y0), (X1 + 20, y0), "HEAD", 2.4)
        hatch(c, (X0 - 20, y0 + 2), (X1 + 20, y0 + 2), side=-1, col="EDGE", step=12)
        for x, h in ((170, 100), (330, 76), (490, 56)):
            hh = h
            for k in range(6):
                s = hh * k / 5
                if with_gradient:
                    pl = {170: -1, 330: 0, 490: 1}[x]
                    v = 48 * (1 - s / hh) + pl * 40 * (s / hh) * (1 - s / hh) * 4 / 1.0
                else:
                    v = 48 * (1 - s / hh)
                arrow(c, (x, y0 - s), (x + v, y0 - s), "BLUE", 1.2, 6)
            pts = []
            for k in range(0, 21):
                s = hh * k / 20
                if with_gradient:
                    pl = {170: -1, 330: 0, 490: 1}[x]
                    v = 48 * (1 - s / hh) + pl * 40 * (s / hh) * (1 - s / hh) * 4
                else:
                    v = 48 * (1 - s / hh)
                pts.append((x + v, y0 - s))
            pathd(c, "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts), "BLUE", 1.8)
            line(c, (x, y0), (x, y0 - hh), "EDGE", 0.7, dash="3,3")
        arrow(c, (X0 + 150, y0 + 24), (X0 + 270, y0 + 24), "ACC", 2.6, 11)
        lab(c, (X0 + 210, y0 + 44), "V(t)", "ACC", "middle", 16)
    profile_row(140, False)
    profile_row(330, True)
    lab(c, (X0 - 70, 92), sub("P", "l") + " = 0", "ACC", "start", 17)
    lab(c, (X0 - 70, 282), sub("P", "l") + " ≠ 0", "ACC", "start", 17)
    # pressure curve under the lower row
    pathd(c, f"M{X0},488 C{X0 + 110},462 {X0 + 190},452 {X0 + 230},452 C{X0 + 290},452 {X0 + 380},468 {X1},488", "ACC", 2.2)
    line(c, (X0 - 10, 488), (X1 + 10, 488), "HEAD", 1.2)
    lab(c, (X0 - 6, 508), sub("P", "o"), "ACC", "end", 16)
    lab(c, (X1 + 6, 508), sub("P", "o"), "ACC", "start", 16)
    lab(c, (X0 + 232, 442), sub("P", "max"), "ACC", "middle", 16)
    REG.put("t7-wedge", c, "The wedge effect (Fig. 7.6 of the notes)",
            "Schematic representation of the wedge effect, Fig. 7.6 of the notes: above, the Couette profiles that "
            "P_l = 0 would give, with a flux that changes along the film; below, the profiles with P_l ≠ 0 (reverse "
            "Poiseuille flow upstream of the maximum, forward downstream) and the overpressure P − P_o that keeps Q uniform")


# ----------------------------------------------------------------------------------------------- extension
def channel_profiles():
    c = Canvas(700, 260)
    h = 150
    for k, (title, x0) in enumerate((("Couette (7.9)", 40), ("Poiseuille (7.11)", 270), ("sum (7.12)", 500))):
        yb, yt = 200, 200 - h
        line(c, (x0, yb), (x0 + 160, yb), "HEAD", 2.4)
        line(c, (x0, yt), (x0 + 160, yt), "HEAD", 2.4)
        hatch(c, (x0, yb + 2), (x0 + 160, yb + 2), side=-1, col="EDGE", step=12)
        hatch(c, (x0 + 160, yt - 2), (x0, yt - 2), side=-1, col="EDGE", step=12)
        pts = []
        for i in range(0, 31):
            s = h * i / 30
            u = s / h
            vc = 90 * u
            vp = 60 * u * (1 - u) * 4 / 1.0 * 0.6
            v = (vc, vp, vc + vp)[k]
            pts.append((x0 + v, yb - s))
        pathd(c, "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts), "BLUE", 2.2)
        for i in range(1, 8):
            s = h * i / 8
            a, b = pts[int(round(30 * i / 8))]
            arrow(c, (x0, yb - s), (a, b), "BLUE", 1.0, 6)
        line(c, (x0, yb), (x0, yt), "EDGE", 0.8, dash="3,3")
        note(c, (x0 + 80, 236), title, "TEXT", "middle", 14)
        if k == 0:
            arrow(c, (x0 + 70, yt - 14), (x0 + 130, yt - 14), "ACC", 2.4, 10)
            lab(c, (x0 + 100, yt - 22), "V", "ACC", "middle", 16)
        if k > 0:
            lab(c, (x0 + 80, yt - 14), sub("P", "l") + " > 0", "ACC", "middle", 15)
    lab(c, (30, 50), "h", "GREEN", "end", 17)
    note(c, (350, 256), "superposition of the two linear solutions; the upper wall moves only in the first and third", "TEXT",
         "middle", 12)
    REG.put("t7-channel-profiles", c, "Couette, Poiseuille and combined profiles between two plane walls",
            "Couette profile (7.9), Poiseuille profile (7.11) and their sum (7.12) for the flow between two parallel "
            "walls a distance h apart; the problem is linear, so the solutions superpose (sketch, an extension)")


def build():
    pipe_cv()
    rayleigh()
    variable_pipe()
    entrance()
    bearing()
    wedge()
    channel_profiles()
    try:
        from figures import fluids_t7p
    except ImportError:
        return REG
    fluids_t7p.build(REG, RASTER)
    return REG
