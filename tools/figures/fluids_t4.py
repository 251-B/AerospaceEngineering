"""Topic 4 figures for Fluid Mechanics: the Navier-Stokes equations (Notes.pdf, Chapter 4).

One figure for the theory page: the sphere of radius R in a uniform stream used as the worked example of
initial and boundary conditions (Notes.pdf, p. 45 printed, Eqs. 4.43-4.48). It is redrawn with the same
symbols as the notes: stream U_inf e_x at temperature T_inf, gravity g pointing down, sphere surface
at temperature T_w, axes x, y, z centred on the sphere.
"""
import math

from figures.svgkit import Canvas, Registry, arrow, circle, line, sub, text

REG = Registry("FM-T4")

# Cropped originals (PNG in vault/attachments/FM-T4/, cropped by hand from the sheets): name -> (alt text, caption).
RASTER = {
    "ns1-statement": (
        "Horizontal porous wall at temperature T_w with suction velocity V_w, free stream U_inf, T_inf, P_inf, gravity g and axes x, z",
        "Statement figure (crop of NS1.pdf, p. 1): horizontal porous wall at temperature $T_w$ with suction velocity $V_w$, "
        "free stream $U_\infty$, $T_\infty$, $P_\infty$, gravity $g$ and axes $x$, $z$"),
    "ns2-statement": (
        "Two coaxial cylinders, inner of radius R1 at T1 rotating with Omega1, outer of radius R2 at T2 rotating with Omega2, polar coordinates r and theta",
        "Statement figure (crop of NS2.pdf, p. 1): inner cylinder $R_1$ at $T_1$ rotating with $\Omega_1$, outer cylinder $R_2$ at "
        "$T_2$ rotating with $\Omega_2$, polar coordinates $r$, $\theta$"),
    "ns4-statement": (
        "Gap of thickness h between two horizontal walls, upper wall moving with velocity U, dashed control volume V_o of unit length, axes x, z and gravity g",
        "Statement figure (crop of NS4.pdf, p. 1): gap of thickness $h$, upper wall moving with $U$, fixed control volume $V_o$ of "
        "unit length in $x$, axes $x$, $z$ and gravity $g$"),
}

SERIF = "Newsreader, Georgia, 'Times New Roman', serif"


def lab(c, p, s, col="HEAD", anchor="middle", size=17, italic=True, weight="400"):
    style = ' font-style="italic"' if italic else ""
    c.add(f'<text x="{p[0]:.1f}" y="{p[1]:.1f}" fill="{col}" font-size="{size}" font-weight="{weight}" '
          f'text-anchor="{anchor}" font-family="{SERIF}"{style}>{s}</text>')


def sphere_in_stream():
    c = Canvas(560, 300)
    centre = (380, 150)
    R = 70
    # free stream: three arrows, with U_inf and T_inf
    for y in (110, 150, 190):
        arrow(c, (40, y), (180, y), "BLUE", 1.8, 9)
    lab(c, (110, 98), sub("U", "&#8734;") + ' <tspan text-decoration="overline">e</tspan>' + sub("", "x"), "BLUE", size=18)
    lab(c, (110, 222), sub("T", "&#8734;"), "BLUE", size=18)
    # gravity
    arrow(c, (230, 30), (230, 90), "ACC", 2.0, 10)
    lab(c, (244, 62), "g", "ACC", "start", 18)
    # the sphere
    circle(c, centre, R, "EDGE", 2.4, fill="BLUE", opacity=0.10)
    lab(c, (centre[0] + R + 10, centre[1] + R * 0.72), sub("T", "w"), "HEAD", "start", 18)
    line(c, (centre[0] + R * 0.72, centre[1] + R * 0.70), (centre[0] + R + 8, centre[1] + R * 0.70 - 6), "EDGE", 1.0)
    # axes (x to the right, z up, y out of the plane drawn slanted)
    arrow(c, centre, (centre[0] + 44, centre[1]), "HEAD", 1.8, 9)
    arrow(c, centre, (centre[0], centre[1] - 44), "HEAD", 1.8, 9)
    arrow(c, centre, (centre[0] + 28, centre[1] - 14), "HEAD", 1.8, 9)
    lab(c, (centre[0] + 50, centre[1] + 6), "x", "HEAD", "start", 15)
    lab(c, (centre[0] - 8, centre[1] - 46), "z", "HEAD", "end", 17)
    lab(c, (centre[0] + 34, centre[1] - 18), "y", "HEAD", "start", 17)
    # radius
    line(c, centre, (centre[0] - R * 0.7071, centre[1] + R * 0.7071), "EDGE", 1.0, dash="4,3")
    lab(c, (centre[0] - 34, centre[1] + 52), "R", "TEXT", "end", 16)
    REG.put("sphere-in-stream", c,
            "Sphere of radius R at surface temperature T_w in a uniform stream U_inf e_x at temperature T_inf, with "
            "gravity g pointing down and the axes x, y, z centred on the sphere",
            "Sphere of radius $R$ in a stream of velocity $U_\\infty(t)\\,\\bar{e}_x$ and temperature $T_\\infty$, "
            "with surface temperature $T_w$ and gravity $\\bar{g} = -g\\,\\bar{e}_z$ (Notes.pdf, p. 45)")


def ns3_setup():
    c = Canvas(560, 300)
    centre = (230, 150)
    R = 52
    Rinf = 128
    circle(c, centre, Rinf, "GREEN", 1.8, dash="8,5")
    circle(c, centre, R, "EDGE", 2.4, fill="BLUE", opacity=0.14)
    lab(c, (centre[0], centre[1] + 6), "balloon", "TEXT", "middle", 14, italic=False)
    for a in (0, 60, 120, 180, 240, 300):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        arrow(c, (centre[0] + (R + 6) * ca, centre[1] + (R + 6) * sa), (centre[0] + (R + 34) * ca, centre[1] + (R + 34) * sa), "BLUE", 1.8, 8)
    line(c, centre, (centre[0] + R * 0.7071, centre[1] - R * 0.7071), "HEAD", 1.4)
    lab(c, (centre[0] + 18, centre[1] - 36), "R(t)", "HEAD", "start", 16)
    lab(c, (centre[0] + 104, centre[1] + 20), sub("v", "r") + "(r,t)", "BLUE", "start", 16)
    lab(c, (centre[0] + 54, centre[1] + 84), sub("v", "r") + "(R,t) = dR/dt", "BLUE", "start", 15)
    text(c, (centre[0] + Rinf + 14, centre[1] - 10), "liquid at rest", "TEXT", "start", 13)
    lab(c, (centre[0] + Rinf + 14, centre[1] + 12), sub("p", "&#8734;"), "HEAD", "start", 17)
    text(c, (centre[0] - Rinf + 6, centre[1] + Rinf + 18), "control volume of the energy balance (dashed)", "GREEN", "start", 12)
    REG.put("ns3-setup", c,
            "Spherical balloon of radius R(t) expanding in an infinite liquid: radial velocity field v_r(r,t), liquid at rest with "
            "pressure p_inf far away, and the control volume used in the energy balance",
            "Balloon of radius $R(t)$ in the liquid: radial velocity $v_r(r,t) = R^2\dot{R}/r^2$, liquid at rest with pressure "
            "$p_\infty$ far from the balloon, and the (dashed) control volume of the energy balance of Phase 3")


def build():
    sphere_in_stream()
    ns3_setup()
    return REG
