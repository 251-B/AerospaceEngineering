"""Topic 6 figures for Fluid Mechanics: dimensional analysis (Notes.pdf, Chapter 6) and the problems DA1-DA14.

Theory figures (this module): the fall of a point mass (Fig. 6.1 of the notes, redrawn), the sphere moving in a
stagnant liquid (Fig. 6.2, redrawn) and a sketch of the two limits of the drag law, Eqs. (6.51) and (6.53), drawn on
logarithmic axes (a sketch of the slopes only: the constants C1 and C2 are not given in the notes). Problem figures:
tools/figures/fluids_t6p.py.

Colour code: BLUE fluid and velocities, ACC forces and the unknown, GREEN geometry and scales, HEAD/TEXT/EDGE lines
and labels.
"""
import math

from figures.svgkit import Canvas, Registry, arrow, circle, dot, hatch, line, pathd, rect, sub

REG = Registry("FM-T6")
SERIF = "Newsreader, Georgia, 'Times New Roman', serif"
RASTER = {}                     # name -> (alt, caption): crops of the official sheets, filled by fluids_t6p


def lab(c, p, s, col="HEAD", anchor="middle", size=17, italic=True, weight="400"):
    style = ' font-style="italic"' if italic else ""
    c.add(f'<text x="{p[0]:.1f}" y="{p[1]:.1f}" fill="{col}" font-size="{size}" font-weight="{weight}" '
          f'text-anchor="{anchor}" font-family="{SERIF}"{style}>{s}</text>')


def note(c, p, s, col="TEXT", anchor="middle", size=13):
    lab(c, p, s, col, anchor, size, italic=False)


# ----------------------------------------------------------------------------------------------- Fig. 6.1
def falling_mass():
    c = Canvas(520, 300)
    ground = 250
    line(c, (60, ground), (460, ground), "EDGE", 2.0)
    hatch(c, (60, ground), (460, ground), side=1, col="EDGE", step=12)
    m = (200, 60)
    circle(c, m, 13, "HEAD", 2.0, fill="ACC", opacity=0.25)
    lab(c, (m[0] + 22, m[1] + 6), "m", "HEAD", "start", 19)
    # falling height
    line(c, (130, m[1]), (130, ground), "GREEN", 1.2)
    line(c, (122, m[1]), (138, m[1]), "GREEN", 1.2)
    lab(c, (118, (m[1] + ground) / 2 + 6), "h", "GREEN", "end", 19)
    line(c, (m[0], m[1] + 16), (m[0], ground - 6), "HEAD", 1.0, dash="5,5")
    # gravity
    arrow(c, (390, 70), (390, 150), "HEAD", 2.0, 11)
    lab(c, (402, 118), "g", "HEAD", "start", 19)
    # unknowns at impact
    dot(c, (m[0], ground), 4, "ACC")
    arrow(c, (m[0] + 32, ground - 70), (m[0] + 32, ground - 14), "ACC", 2.2, 10)
    lab(c, (m[0] + 42, ground - 36), sub("v", "c") + "  at  t = " + sub("t", "c"), "ACC", "start", 17)
    lab(c, (260, 290), "unknowns " + sub("t", "c") + " and " + sub("v", "c") + ", functions of (m, h, g): Eq. (6.1)",
        "TEXT", "middle", 13, italic=False)
    REG.put("t6-falling-mass", c, "The fall of a point mass (Fig. 6.1 of the notes)",
            "The fall of a point mass, Fig. 6.1 of the notes: a mass m released from rest at a height h falls under "
            "gravity g; the unknowns are the collision time t_c and the collision velocity v_c")


# ----------------------------------------------------------------------------------------------- Fig. 6.2
def sphere():
    c = Canvas(640, 320)
    C = (380, 170)
    R = 62
    circle(c, C, R, "HEAD", 2.2, fill="EDGE", opacity=0.10)
    # radius
    line(c, C, (C[0] - 44, C[1] + 44), "GREEN", 1.4)
    lab(c, (C[0] - 34, C[1] + 20), "R", "GREEN", "end", 18)
    # axes at the centre
    arrow(c, C, (C[0] + 38, C[1]), "HEAD", 1.3, 8)
    lab(c, (C[0] + 42, C[1] + 16), "x", "HEAD", "start", 16)
    arrow(c, C, (C[0], C[1] - 38), "HEAD", 1.3, 8)
    lab(c, (C[0] - 6, C[1] - 42), "z", "HEAD", "end", 16)
    arrow(c, C, (C[0] + 22, C[1] - 16), "HEAD", 1.1, 7)
    lab(c, (C[0] + 26, C[1] - 18), "y", "HEAD", "start", 15)
    # uniform stream far away (frame of the sphere)
    for y in (90, 150, 210, 270):
        arrow(c, (60, y), (150, y), "BLUE", 1.8, 10)
    lab(c, (105, 76), "U", "BLUE", "middle", 19)
    lab(c, (60, 40), "p + ρgz = " + sub("P", "∞"), "HEAD", "start", 17)
    note(c, (60, 305), "liquid of density ρ and viscosity μ", "TEXT", "start", 13)
    # gravity
    arrow(c, (585, 50), (585, 120), "HEAD", 2.0, 11)
    lab(c, (597, 96), "g", "HEAD", "start", 19)
    # drag
    arrow(c, (C[0] + R + 6, C[1] + 50), (C[0] + R + 76, C[1] + 50), "ACC", 2.6, 11)
    lab(c, (C[0] + R + 82, C[1] + 56), sub("F", "x"), "ACC", "start", 19)
    REG.put("t6-sphere", c, "Fluid motion around a sphere (Fig. 6.2 of the notes)",
            "Fluid motion around a sphere, Fig. 6.2 of the notes, seen from the sphere: far away the liquid moves "
            "with velocity U and its pressure is hydrostatic, p + ρgz = P_∞; the unknown is the drag F_x")


# ----------------------------------------------------------------------------------------------- limits
def drag_limits():
    """Log-log sketch of Fx/(rho U^2 R^2) = f(Re): slope -1 for Re << 1 (6.53), constant for Re >> 1 (6.51)."""
    c = Canvas(640, 360)
    x0, y0, x1, y1 = 90, 300, 600, 40                   # plot box (screen)
    line(c, (x0, y0), (x1, y0), "HEAD", 1.4, head=True)
    line(c, (x0, y0), (x0, y1), "HEAD", 1.4, head=True)
    lab(c, (x1 - 4, y0 + 30), "log Re", "HEAD", "end", 16)
    lab(c, (x0 - 10, y1 + 6), "log", "HEAD", "end", 15, italic=False)
    lab(c, (x0 + 10, y1 + 6), sub("F", "x") + " / (ρ" + "U² R²)", "HEAD", "start", 16)
    xm, yc, k = 330, 210, 80                            # Re = 1 at x = xm; C1 at height yc; k px per decade
    line(c, (xm, y0), (xm, y1 + 30), "GREEN", 1.0, dash="4,5")
    note(c, (xm, y0 + 20), "Re ∼ 1", "GREEN", "middle", 13)
    # the two asymptotes (equal decades on both axes, so slope -1 is drawn at 45 degrees)
    line(c, (xm - (yc - 70), 70), (xm + 70, yc + 70), "BLUE", 1.4, dash="7,5")
    line(c, (xm - 90, yc), (x1 - 20, yc), "BLUE", 1.4, dash="7,5")
    # one smooth curve with both limits: log f = log C1 + log(1 + 1/Re)
    pts = []
    for i in range(0, 61):
        x = x0 + 20 + i * (x1 - 40 - x0) / 60
        u = (x - xm) / k
        y = yc - k * math.log10(1 + 10 ** (-u))
        if y >= 66:
            pts.append((x, y))
    pathd(c, "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts), "ACC", 2.6)
    lab(c, (x0 + 30, 240), "slope −1:", "BLUE", "start", 15, italic=False)
    lab(c, (x0 + 30, 260), sub("C", "2") + " Re⁻¹, Eq. (6.53)", "BLUE", "start", 15)
    lab(c, (x1 - 24, yc - 14), sub("C", "1") + ", Eq. (6.51)", "BLUE", "end", 15)
    note(c, (345, 350), "Sketch of the two limits only: the constants C₁ and C₂ are not given in the notes", "TEXT", "middle", 13)
    REG.put("t6-drag-limits", c, "The two limits of the drag law of the sphere",
            "Sketch, on logarithmic axes, of the two limits of Eq. (6.35): for Re ≪ 1 the dimensionless drag "
            "falls as C₂/Re, Eq. (6.53); for Re ≫ 1 it tends to the constant C₁, Eq. (6.51). Only the slopes are "
            "drawn: the constants and the shape of the curve in between are not in the notes")


def build():
    falling_mass()
    sphere()
    drag_limits()
    try:
        from figures import fluids_t6p
    except ImportError:
        return REG
    fluids_t6p.build(REG, RASTER)
    return REG
