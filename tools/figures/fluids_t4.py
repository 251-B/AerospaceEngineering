"""Topic 4 figures for Fluid Mechanics: the Navier-Stokes equations (Notes.pdf, Chapter 4).

One figure for the theory page: the sphere of radius R in a uniform stream used as the worked example of
initial and boundary conditions (Notes.pdf, p. 45 printed, Eqs. 4.43-4.48). It is redrawn with the same
symbols as the notes: stream U_inf e_x at temperature T_inf, gravity g pointing down, sphere surface
at temperature T_w, axes x, y, z centred on the sphere.
"""
import math

from figures.svgkit import Canvas, Registry, arrow, circle, dim, hatch, line, pathd, poly, rect, sub, text

REG = Registry("FM-T4")

# Cropped originals (PNG in vault/attachments/FM-T4/, cropped by hand from the sheets): name -> (alt text, caption).
RASTER = {
    "ns1-statement": (
        "Horizontal porous wall at temperature T_w with suction velocity V_w, free stream U_inf, T_inf, P_inf, gravity g and axes x, z",
        "Statement figure (crop of NS1.pdf, p. 1): horizontal porous wall at temperature $T_w$ with suction velocity $V_w$, "
        "free stream $U_\\infty$, $T_\\infty$, $P_\\infty$, gravity $g$ and axes $x$, $z$"),
    "ns2-statement": (
        "Two coaxial cylinders, inner of radius R1 at T1 rotating with Omega1, outer of radius R2 at T2 rotating with Omega2, polar coordinates r and theta",
        "Statement figure (crop of NS2.pdf, p. 1): inner cylinder $R_1$ at $T_1$ rotating with $\\Omega_1$, outer cylinder $R_2$ at "
        "$T_2$ rotating with $\\Omega_2$, polar coordinates $r$, $\\theta$"),
    "ns11-statement": (
        "Channel of height h between two porous plates, lower wall at rest with injection velocity v_l, upper wall moving with U, axes x and y",
        "Statement figure (crop of NS11.pdf, p. 1): channel of height $h$ between two porous plates, injection velocity $v_l$ through "
        "the lower wall at rest, upper wall moving with velocity $U$, axes $x$ and $y$"),
    "ns12-statement": (
        "Two concentric spheres of radii kappa R and R with entrance and exit ducts of half-angle epsilon, radius r and polar angle",
        "Statement figure (crop of NS12.pdf, p. 1): gap between two concentric spheres of radii $\\kappa R$ and $R$, entrance and exit "
        "sections of half-angle $\\epsilon$ and the radial coordinate $r$"),
    "ns13-statement": (
        "Two coaxial porous cylinders of radii R_i and R_o rotating with angular velocities Omega_i and Omega_o, liquid injected through the inner surface with velocity V_i, polar coordinates r and theta",
        "Statement figure (crop of NS13.pdf, p. 1): porous cylinders of radii $R_i$ and $R_o$ rotating with $\\Omega_i$ and $\\Omega_o$, "
        "injection velocity $V_i$ through the inner surface, polar coordinates $r$, $\\theta$"),
    "ns14-statement": (
        "Annular gap between two concentric cylinders of radii R_i and R_o, the inner one moving axially with velocity U, the outer one rotating with angular velocity Omega, axes r and z",
        "Statement figure (crop of NS14.pdf, p. 1): annular gap between the cylinders of radii $R_i$ and $R_o$, inner cylinder moving "
        "axially with $U$, outer cylinder rotating with $\\Omega$, axes $r$, $z$"),
    "ns17-statement": (
        "Infinitely large porous disk rotating with angular velocity Omega about the z axis, side view with axes z and r, and top view with the angle theta",
        "Statement figure (crop of NS17.pdf, p. 1): porous disk rotating with angular velocity $\\Omega$, side view (axes $z$, $r$) "
        "and top view (polar angle $\\theta$)"),
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
    c = Canvas(560, 340)
    centre = (230, 150)
    R = 52
    Rinf = 128
    circle(c, centre, Rinf, "GREEN", 1.8, dash="8,5")
    circle(c, centre, R, "EDGE", 2.4, fill="BLUE", opacity=0.14)
    text(c, (centre[0], centre[1] + 28), "balloon", "TEXT", "middle", 13)
    for a in (0, 60, 120, 180, 240, 300):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        arrow(c, (centre[0] + (R + 6) * ca, centre[1] + (R + 6) * sa), (centre[0] + (R + 34) * ca, centre[1] + (R + 34) * sa), "BLUE", 1.8, 8)
    line(c, centre, (centre[0] + R * 0.7071, centre[1] - R * 0.7071), "HEAD", 1.4)
    lab(c, (centre[0] + 6, centre[1] - 10), "R(t)", "HEAD", "start", 15)
    lab(c, (centre[0] + 92, centre[1] - 72), sub("v", "r") + "(r,t)", "BLUE", "start", 16)
    text(c, (centre[0] + Rinf + 14, centre[1] - 14), "liquid at rest", "TEXT", "start", 13)
    lab(c, (centre[0] + Rinf + 14, centre[1] + 8), sub("p", "&#8734;"), "HEAD", "start", 17)
    lab(c, (centre[0] + Rinf + 14, centre[1] + 40), sub("v", "r") + "(R,t) = dR/dt", "BLUE", "start", 15)
    text(c, (centre[0] - Rinf + 6, centre[1] + Rinf + 28), "control volume of the energy balance (dashed)", "GREEN", "start", 12)
    REG.put("ns3-setup", c,
            "Spherical balloon of radius R(t) expanding in an infinite liquid: radial velocity field v_r(r,t), liquid at rest with "
            "pressure p_inf far away, and the control volume used in the energy balance",
            "Balloon of radius $R(t)$ in the liquid: radial velocity $v_r(r,t) = R^2\\dot{R}/r^2$, liquid at rest with pressure "
            "$p_\\infty$ far from the balloon, and the (dashed) control volume of the energy balance of Phase 3")


def ns5_statement():
    c = Canvas(460, 330)
    rect(c, 110, 20, 60, 280, "EDGE", 1.6, fill="BLUE", opacity=0.15)
    rect(c, 250, 20, 60, 280, "EDGE", 1.6, fill="BLUE", opacity=0.15)
    rect(c, 170, 20, 80, 280, "HEAD", 2.2, fill="EDGE", opacity=0.10)
    arrow(c, (210, 170), (210, 56), "ACC", 2.4, 11)
    lab(c, (222, 100), "U", "ACC", "start", 20)
    dim(c, (170, 215), (250, 215), "", "TEXT")
    lab(c, (210, 207), "2a", "HEAD", "middle", 16)
    dim(c, (250, 262), (310, 262), "", "TEXT")
    lab(c, (280, 254), "h", "HEAD", "middle", 16)
    lab(c, (72, 150), sub("p", "a"), "HEAD", "middle", 18)
    lab(c, (350, 150), sub("p", "a"), "HEAD", "middle", 18)
    text(c, (140, 120), "liquid", "BLUE", "middle", 12)
    text(c, (280, 120), "liquid", "BLUE", "middle", 12)
    text(c, (210, 130), "solid", "TEXT", "middle", 12)
    arrow(c, (405, 50), (405, 130), "ACC", 2.0, 10)
    lab(c, (418, 94), "g", "ACC", "start", 18)
    arrow(c, (385, 290), (385, 246), "HEAD", 1.6, 9)
    lab(c, (378, 244), "z", "HEAD", "end", 16)
    arrow(c, (385, 290), (432, 290), "HEAD", 1.6, 9)
    lab(c, (434, 285), "r", "HEAD", "start", 16)
    REG.put("ns5-statement", c,
            "Solid cylinder of radius a moving upward with velocity U, dragging a coaxial liquid layer of thickness h, "
            "surrounded by air at pressure p_a; gravity g pointing down and axes r, z",
            "Statement figure (redrawn from NS5.pdf, p. 1): solid cylinder of radius $a$ moving upward with $U$, coaxial liquid "
            "layer of thickness $h$, surrounding air at pressure $p_a$, gravity $g$ and axes $r$, $z$")


def ns7_statement():
    c = Canvas(600, 330)
    al = math.radians(20)
    t = (math.cos(al), math.sin(al))
    n = (math.sin(al), -math.cos(al))
    P0 = (40.0, 110.0)

    def pt(s, d=0.0):
        return (P0[0] + s * t[0] + d * n[0], P0[1] + s * t[1] + d * n[1])
    H = 76
    poly(c, [pt(0), pt(470), pt(470, H), pt(0, H)], "none", 0, fill="BLUE", close=True, opacity=0.13)
    line(c, pt(0), pt(470), "HEAD", 2.4)
    hatch(c, pt(0), pt(470), 1, "EDGE")
    line(c, pt(0, H), pt(470, H), "EDGE", 1.6)
    poly(c, [pt(230), pt(360), pt(360, H), pt(230, H)], "GREEN", 1.8, "7,4", close=True)
    dim(c, pt(230, H + 16), pt(360, H + 16), "", "TEXT")
    lab(c, pt(295, H + 34), "1", "TEXT", "middle", 15)
    lab(c, pt(380, 48), sub("V", "o"), "GREEN", "start", 18)
    dim(c, pt(110), pt(110, H), "", "TEXT")
    lab(c, pt(100, H / 2), "h", "HEAD", "end", 17)
    O = pt(205)
    arrow(c, O, (O[0] + 52 * t[0], O[1] + 52 * t[1]), "HEAD", 1.7, 9)
    arrow(c, O, (O[0] + 52 * n[0], O[1] + 52 * n[1]), "HEAD", 1.7, 9)
    lab(c, (O[0] + 58 * t[0], O[1] + 58 * t[1] + 18), "x", "HEAD", "start", 16)
    lab(c, (O[0] + 50 * n[0] - 14, O[1] + 58 * n[1]), "y", "HEAD", "end", 16)
    lab(c, pt(60, H + 22), sub("p", "a"), "HEAD", "middle", 17)
    arrow(c, (480, 40), (480, 120), "ACC", 2.0, 10)
    lab(c, (494, 84), "g", "ACC", "start", 18)
    E = pt(470)
    line(c, (E[0] - 150, E[1]), E, "EDGE", 1.2, dash="5,4")
    pathd(c, f"M{E[0] - 100 * t[0]:.1f},{E[1] - 100 * t[1]:.1f} A100,100 0 0 1 {E[0] - 100:.1f},{E[1]:.1f}", "TEXT", 1.2)
    lab(c, (E[0] - 128, E[1] - 8), "&#945;", "HEAD", "middle", 17)
    REG.put("ns7-statement", c,
            "Liquid layer of constant thickness h flowing down an inclined plane of angle alpha, with axes x along the plane and y "
            "normal to it, gravity g, air at pressure p_a above, and the fixed control volume V_o of unit length",
            "Statement figure (redrawn from NS7.pdf, p. 1): layer of thickness $h$ on a plane inclined at $\\alpha$, axes $x$ (down the "
            "plane) and $y$ (normal to it), gravity $\\bar{g} = g\\sin\\alpha\\,\\bar{e}_x - g\\cos\\alpha\\,\\bar{e}_y$, air at "
            "$p_a$ and the fixed control volume $V_o$ of unit length")


def ns8_statement():
    c = Canvas(620, 330)
    top, bot, x0, x1 = 130, 230, 120, 470
    line(c, (x0, top), (x1, top), "HEAD", 2.2)
    line(c, (x0, bot), (x1, bot), "HEAD", 2.2)
    pathd(c, f"M{x0},{top} C{x0 - 22},{top + 20} {x0 - 22},{bot - 20} {x0},{bot}", "HEAD", 2.2)
    pathd(c, f"M{x1},{top} A20,50 0 1 1 {x1},{bot} A20,50 0 1 1 {x1},{top}", "HEAD", 2.2, fill="BLUE", opacity=0.10)
    for x in range(150, 450, 30):
        arrow(c, (x, top - 30), (x, top - 2), "BLUE", 1.5, 8)
        arrow(c, (x, bot + 30), (x, bot + 2), "BLUE", 1.5, 8)
    arrow(c, (220, 180), (330, 180), "ACC", 2.4, 11)
    lab(c, (275, 168), "U", "ACC", "middle", 20)
    lab(c, (90, 108), sub("T", "c"), "HEAD", "end", 18)
    line(c, (96, 112), (130, 130), "EDGE", 1.0)
    lab(c, (480, 90), "V", "BLUE", "start", 20)
    lab(c, (210, 40), sub("p", "&#8734;"), "HEAD", "middle", 20)
    lab(c, (310, 40), sub("T", "&#8734;"), "HEAD", "middle", 20)
    arrow(c, (540, 215), (540, 165), "HEAD", 1.6, 9)
    lab(c, (532, 170), "r", "HEAD", "end", 17)
    arrow(c, (540, 215), (590, 215), "HEAD", 1.6, 9)
    lab(c, (592, 232), "z", "HEAD", "start", 17)
    REG.put("ns8-statement", c,
            "Infinitely long porous cylinder moving axially with velocity U while liquid is sucked through its surface with "
            "velocity V, with pressure p_inf and temperature T_inf far away, wall temperature T_c and axes r, z",
            "Statement figure (redrawn from NS8.pdf, p. 1): porous cylinder of radius $R$ at temperature $T_c$ moving with $U$ along "
            "$z$, suction velocity $V$ through its surface, ambient $p_\\infty$, $T_\\infty$ and axes $r$, $z$")


def ns9_setup():
    c = Canvas(620, 330)
    top, bot, x0, x1 = 130, 230, 120, 470
    line(c, (x0, top), (x1, top), "HEAD", 2.2)
    line(c, (x0, bot), (x1, bot), "HEAD", 2.2)
    pathd(c, f"M{x0},{top} C{x0 - 22},{top + 20} {x0 - 22},{bot - 20} {x0},{bot}", "HEAD", 2.2)
    pathd(c, f"M{x1},{top} A20,50 0 1 1 {x1},{bot} A20,50 0 1 1 {x1},{top}", "HEAD", 2.2, fill="BLUE", opacity=0.10)
    for x in range(150, 450, 30):
        arrow(c, (x, top - 30), (x, top - 2), "BLUE", 1.5, 8)
        arrow(c, (x, bot + 30), (x, bot + 2), "BLUE", 1.5, 8)
    arrow(c, (220, 180), (330, 180), "ACC", 2.4, 11)
    lab(c, (275, 168), sub("U", "w"), "ACC", "middle", 20)
    lab(c, (90, 108), sub("T", "w"), "HEAD", "end", 18)
    line(c, (96, 112), (130, 130), "EDGE", 1.0)
    lab(c, (480, 90), sub("V", "w"), "BLUE", "start", 20)
    lab(c, (210, 40), sub("p", "&#8734;"), "HEAD", "middle", 20)
    lab(c, (310, 40), sub("T", "&#8734;"), "HEAD", "middle", 20)
    arrow(c, (540, 215), (540, 165), "HEAD", 1.6, 9)
    lab(c, (532, 170), "r", "HEAD", "end", 17)
    arrow(c, (540, 215), (590, 215), "HEAD", 1.6, 9)
    lab(c, (592, 232), "z", "HEAD", "start", 17)
    REG.put("ns9-setup", c,
            "Infinitely long porous cylinder moving axially with velocity U_w while liquid is sucked through its wall with velocity "
            "V_w, with the fluid at rest at pressure p_inf and temperature T_inf far away, wall temperature T_w and axes r, z",
            "Setup of NS9 (drawn for the solution): porous cylinder of radius $R$ at temperature $T_w$ moving with $U_w$ along $z$, "
            "suction velocity $V_w$ ($q = 2\\pi R V_w$ per unit length), fluid at rest at $p_\\infty$, $T_\\infty$ far away, axes $r$, $z$")


def ns10_setup():
    c = Canvas(560, 320)
    centre = (230, 150)
    R = 46
    Rf = 120
    circle(c, centre, Rf, "EDGE", 1.2, dash="3,5")
    circle(c, centre, R, "ACC", 2.4, fill="BLUE", opacity=0.0)
    text(c, (centre[0], centre[1] + 6), "cavity", "TEXT", "middle", 13)
    for a in (0, 60, 120, 180, 240, 300):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        arrow(c, (centre[0] + (R + 6) * ca, centre[1] + (R + 6) * sa), (centre[0] + (R + 36) * ca, centre[1] + (R + 36) * sa), "BLUE", 1.8, 8)
    line(c, centre, (centre[0] + R * 0.7071, centre[1] - R * 0.7071), "HEAD", 1.4)
    lab(c, (centre[0] + 4, centre[1] - 14), sub("R", "c") + "(t)", "HEAD", "start", 15)
    lab(c, (centre[0] + 82, centre[1] - 70), sub("v", "r") + "(r,t)", "BLUE", "start", 16)
    text(c, (centre[0] + Rf + 14, centre[1] - 14), "ocean at rest", "TEXT", "start", 13)
    lab(c, (centre[0] + Rf + 14, centre[1] + 8), sub("p", "&#8734;"), "HEAD", "start", 17)
    lab(c, (centre[0] + Rf + 14, centre[1] + 40), sub("p", "R") + "(t) at the cavity wall", "HEAD", "start", 15)
    REG.put("ns10-setup", c,
            "Spherical cavity of radius R_c(t) expanding in the ocean with initial radius R_0 and initial radial velocity V_0, "
            "liquid at rest with pressure p_inf far away",
            "Setup of NS10 (drawn for the solution): cavity of radius $R_c(t)$ ($R_c(0) = R_0$, $\\dot{R}_c(0) = V_0$) expanding in the "
            "ocean, radial velocity field $v_r(r,t)$, pressure $p_R(t)$ at the cavity wall and $p_\\infty$ far away")


def ns15_statement():
    c = Canvas(640, 330)
    wy = 230
    x0, x1 = 20, 520
    line(c, (x0, wy), (x1, wy), "HEAD", 2.4)
    for x in range(30, 520, 18):
        arrow(c, (x, wy + 2), (x, wy + 26), "BLUE", 1.3, 7)
        line(c, (x, wy), (x - 5, wy - 6), "EDGE", 1.0)
    lab(c, (22, 205), sub("V", "w"), "BLUE", "start", 18)
    arrow(c, (526, wy), (604, wy), "ACC", 2.4, 11)
    lab(c, (610, wy - 8), sub("U", "w"), "ACC", "start", 19)
    lab(c, (450, wy + 46), sub("T", "w"), "HEAD", "start", 17)
    line(c, (448, wy + 36), (432, wy + 4), "EDGE", 1.0)
    # control volume
    cvx0, cvx1, cvy0, cvy1 = 230, 410, wy, 40
    rect(c, cvx0, cvy1, cvx1 - cvx0, cvy0 - cvy1, "GREEN", 1.8, "7,4")
    dim(c, (cvx0, 135), (cvx1, 135), "", "TEXT")
    text(c, ((cvx0 + cvx1) / 2, 126), "δx = 1", "TEXT", "middle", 14)
    lab(c, (cvx1 + 12, 70), sub("V", "c"), "GREEN", "start", 18)
    arrow(c, (cvx0, 175), (cvx0 - 38, 175), "HEAD", 1.4, 8)
    lab(c, (cvx0 - 22, 165), "n", "HEAD", "middle", 15)
    arrow(c, (330, wy + 4), (330, wy + 40), "HEAD", 1.4, 8)
    lab(c, (342, wy + 44), "n", "HEAD", "start", 15)
    arrow(c, (480, wy), (480, wy - 36), "HEAD", 1.4, 8)
    lab(c, (488, wy - 18), sub("n", "w"), "HEAD", "start", 15)
    lab(c, (150, 30), sub("p", "&#8734;"), "HEAD", "middle", 18)
    lab(c, (290, 30), sub("T", "&#8734;"), "HEAD", "middle", 18)
    arrow(c, (120, wy), (120, wy - 60), "HEAD", 1.6, 9)
    lab(c, (112, wy - 62), "y", "HEAD", "end", 17)
    arrow(c, (120, wy), (170, wy), "HEAD", 1.6, 9)
    lab(c, (172, wy - 8), "x", "HEAD", "start", 17)
    REG.put("ns15-statement", c,
            "Semi-infinite liquid above a porous wall moving with velocity U_w while liquid is removed through it with velocity V_w; "
            "fixed control volume V_c of unit length, axes x, y, normals n and n_w, far-field pressure p_inf and temperature T_inf",
            "Statement figure (redrawn from NS15.pdf, p. 1): porous wall at temperature $T_w$ moving with $U_w$ and sucking with "
            "$V_w$, axes $x$, $y$, normals $\\bar{n}$ and $\\bar{n}_w$, far field $p_\\infty$, $T_\\infty$ and the fixed control "
            "volume $V_c$ of unit length ($\\delta x = 1$)")


def build():
    sphere_in_stream()
    ns3_setup()
    ns5_statement()
    ns7_statement()
    ns8_statement()
    ns9_setup()
    ns10_setup()
    ns15_statement()
    return REG
