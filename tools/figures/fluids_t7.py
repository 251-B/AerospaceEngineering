"""Topic 7 figures for Fluid Mechanics: viscous flows (Notes.pdf, Chapter 7) and the problems VF2-VF20.

Theory figures (this module): Figs. 7.1 to 7.6 of the notes as PNG crops of Notes.pdf (the pipe control volume, Rayleigh's layer, the
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


# Figs. 7.1 to 7.6 of Notes.pdf: PNG crops (Screenshot-First), vault/attachments/FM-T7/.
def crops():
    REG.raster("t7-pipe-cv", "Fully developed laminar flow in a circular pipe (Fig. 7.1 of the notes)",
               "Fully developed laminar flow in a circular pipe: the control volume Σc of length L, radius a and outward "
               "normal n̄, with reduced pressures P_1 and P_2 at its ends and the same Poiseuille profile at both. "
               "Copied from Notes.pdf, Fig. 7.1, p. 85.", 560)
    REG.raster("t7-rayleigh", "Variation with t of the velocity for Rayleigh's problem (Fig. 7.2 of the notes)",
               "Rayleigh's problem: velocity profiles at three increasing times above a wall set in motion with velocity V "
               "at t = 0; the layer of moving liquid thickens as δ ~ (νt)^(1/2). Copied from Notes.pdf, Fig. 7.2, p. 86.", 480)
    REG.raster("t7-variable-pipe", "Discharge flow through a pipe of variable section (Fig. 7.3 of the notes)",
               "Discharge flow through a pipe of variable section: a container at reduced pressure P_c(t) feeds a slender "
               "pipe of diameter D, length L ≫ D and curvature radius R ≫ D that discharges at P_o. "
               "Copied from Notes.pdf, Fig. 7.3, p. 89.", 480)
    REG.raster("t7-entrance", "The entrance region in pipe flows dominated by viscosity (Fig. 7.4 of the notes)",
               "The entrance region in pipe flows dominated by viscosity: for ρ v_L D/μ ≲ 1 the Poiseuille profile is "
               "reached at a distance of order D; for ρ v_L D/μ ≫ 1 a boundary layer grows from the uniform entrance "
               "profile until it fills the pipe at x ~ L_E = ρ v_L D²/μ. Copied from Notes.pdf, Fig. 7.4, p. 94.", 640)
    REG.raster("t7-bearing", "Plane bearing (Fig. 7.5 of the notes)",
               "Plane bearing: a bearing of length L moves with velocity V(t) over a horizontal wall; the film of "
               "thickness h(x) is at the pressure P_o on both sides. Copied from Notes.pdf, Fig. 7.5, p. 96.", 640)
    REG.raster("t7-wedge", "The wedge effect (Fig. 7.6 of the notes)",
               "Schematic representation of the wedge effect: above, the Couette profiles that P_l = 0 would give, with a "
               "flux that changes along the film; below, the profiles with P_l ≠ 0 (reverse Poiseuille flow upstream of "
               "the maximum, forward downstream) and the overpressure P − P_o that keeps Q uniform. "
               "Copied from Notes.pdf, Fig. 7.6, p. 97.", 480)


# ----------------------------------------------------------------------------------------------- extension
def channel_profiles():
    # EXTRA: Couette/Poiseuille sketch, not printed in Notes.pdf
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
    crops()
    channel_profiles()
    try:
        from figures import fluids_t7p
    except ImportError:
        return REG
    fluids_t7p.build(REG, RASTER)
    return REG
