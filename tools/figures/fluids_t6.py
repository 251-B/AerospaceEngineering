"""Topic 6 figures for Fluid Mechanics: dimensional analysis (Notes.pdf, Chapter 6) and the problems DA1-DA14.

Theory figures (this module): the fall of a point mass (Fig. 6.1 of the notes) and the sphere moving in a
stagnant liquid (Fig. 6.2), both PNG crops of Notes.pdf, and a sketch of the two limits of the drag law, Eqs. (6.51) and (6.53), drawn on
logarithmic axes (a sketch of the slopes only: the constants C1 and C2 are not given in the notes). Problem figures:
tools/figures/fluids_t6p.py.

Colour code: BLUE fluid and velocities, ACC forces and the unknown, GREEN geometry and scales, HEAD/TEXT/EDGE lines
and labels.
"""
import math

from figures.svgkit import Canvas, Registry, line, pathd, sub

REG = Registry("FM-T6")
SERIF = "Newsreader, Georgia, 'Times New Roman', serif"
RASTER = {}                     # name -> (alt, caption): crops of the official sheets, filled by fluids_t6p


def lab(c, p, s, col="HEAD", anchor="middle", size=17, italic=True, weight="400"):
    style = ' font-style="italic"' if italic else ""
    c.add(f'<text x="{p[0]:.1f}" y="{p[1]:.1f}" fill="{col}" font-size="{size}" font-weight="{weight}" '
          f'text-anchor="{anchor}" font-family="{SERIF}"{style}>{s}</text>')


def note(c, p, s, col="TEXT", anchor="middle", size=13):
    lab(c, p, s, col, anchor, size, italic=False)


# ----------------------------------------------------------------------------------------------- Figs. 6.1 and 6.2
def crops():
    REG.raster("t6-falling-mass", "The fall of a point mass (Fig. 6.1 of the notes)",
               "The fall of a point mass: a mass m released from rest at a height h falls under gravity g; the unknowns "
               "are the collision time t_c and the collision velocity v_c. Copied from Notes.pdf, Fig. 6.1, p. 66.", 440)
    REG.raster("t6-sphere", "Fluid motion around a sphere (Fig. 6.2 of the notes)",
               "Fluid motion around a sphere, seen from the sphere: far away the liquid moves with velocity U and its "
               "pressure is hydrostatic, p + ρgz = P_∞; the unknown is the drag F_x. Copied from Notes.pdf, Fig. 6.2, "
               "p. 73.", 640)


# ----------------------------------------------------------------------------------------------- limits
def drag_limits():
    # EXTRA: sketch of the drag limits, not printed in Notes.pdf
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
    crops()
    drag_limits()
    try:
        from figures import fluids_t6p
    except ImportError:
        return REG
    fluids_t6p.build(REG, RASTER)
    return REG
