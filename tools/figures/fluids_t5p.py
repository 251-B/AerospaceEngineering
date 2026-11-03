"""Problem figures of Fluid Mechanics Topic 5 (hydrostatics sheets FS1-FS10, FS8 = second scan of FS2).

Per problem: the statement figure redrawn from the sheet (the scans carry the handwritten key on the drawing),
the deduction figure (coordinates, right triangles, strips, areas) and the free-body diagram. Registered in the
FM-T5 registry of tools/figures/fluids_t5.py; colour code as there (BLUE liquid, ACC resultant forces, GREEN
deduction geometry, PINK weights and reactions).
"""
import math

from figures.fluids_t5 import arc, lab, note, water_surface
from figures.svgkit import Canvas, arrow, circle, dim, dot, hatch, line, pathd, poly, rect, sub

REG = None


def put(name, c, title, caption):
    REG.put(name, c, title, caption)


def liquid(c, pts, op=0.10):
    poly(c, pts, "BLUE", 0, fill="BLUE", close=True, opacity=op)


def floor(c, x0, x1, y):
    line(c, (x0, y), (x1, y), "EDGE", 2.0)
    hatch(c, (x1, y), (x0, y), side=1, col="EDGE", step=12)


# ------------------------------------------------------------------------------------------------- FS1
def fs1():
    c = Canvas(560, 300)
    liquid(c, [(60, 110), (330, 110), (330, 270), (60, 270)])
    line(c, (50, 60), (50, 280), "HEAD", 6)
    line(c, (340, 60), (340, 280), "HEAD", 6)
    line(c, (50, 280), (340, 280), "HEAD", 6)
    line(c, (53, 110), (337, 110), "BLUE", 1.6)
    rect(c, 150, 70, 80, 80, "HEAD", 2.0, fill="ACC", opacity=0.10)
    line(c, (150, 110), (230, 110), "HEAD", 1.0, dash="4,3")
    lab(c, (190, 98), sub("V", "h") + ", " + sub("ρ", "h"), "HEAD", "middle", 16)
    lab(c, (190, 135), sub("V", "s"), "HEAD", "middle", 16)
    lab(c, (195, 215), sub("ρ", "f"), "BLUE", "middle", 18)
    lab(c, (400, 90), "ice cube: " + sub("ρ", "h") + " < " + sub("ρ", "f"), "TEXT", "start", 14, italic=False)
    lab(c, (400, 115), "melt water: " + sub("ρ", "a"), "TEXT", "start", 14, italic=False)
    lab(c, (400, 140), sub("ρ", "h") + " < " + sub("ρ", "a") + " < " + sub("ρ", "f"), "TEXT", "start", 14, italic=False)
    put("fs1-statement", c,
        "Ice cube of density rho_h and volume V_h floating in a liquid of density rho_f, with the submerged part V_s",
        "Statement figure (redrawn from fluid_statics_1.pdf, p. 1): ice cube of volume $V_h$ and density $\\rho_h$ floating in a "
        "liquid of density $\\rho_f > \\rho_h$, submerged volume $V_s$")

    c = Canvas(640, 300)
    # (a) floating cube
    liquid(c, [(30, 120), (290, 120), (290, 280), (30, 280)])
    line(c, (30, 120), (290, 120), "BLUE", 1.6)
    lab(c, (36, 112), sub("p", "a"), "HEAD", "start", 15)
    rect(c, 110, 60, 100, 100, "HEAD", 2.0, fill="ACC", opacity=0.10)
    rect(c, 110, 120, 100, 40, "GREEN", 0, fill="GREEN", opacity=0.25)
    dot(c, (160, 110), 3.6, "PINK")
    arrow(c, (160, 110), (160, 200), "PINK", 2.6, 11)
    lab(c, (168, 200), sub("ρ", "h") + "g" + sub("V", "h"), "PINK", "start", 16)
    dot(c, (140, 140), 3.6, "ACC")
    arrow(c, (140, 140), (140, 40), "ACC", 2.6, 11)
    lab(c, (130, 60), sub("ρ", "f") + "g" + sub("V", "s"), "ACC", "end", 16)
    lab(c, (232, 146), sub("V", "s"), "GREEN", "start", 16)
    note(c, (160, 296), "(a) floating cube: weight and buoyancy", "TEXT", size=13)
    # (b) volumes compared
    x0 = 360
    floor(c, x0, 620, 270)
    rect(c, x0 + 30, 270 - 70, 70, 70, "GREEN", 1.6, fill="GREEN", opacity=0.25)
    lab(c, (x0 + 65, 192), sub("V", "s") + " = " + sub("ρ", "h") + sub("V", "h") + "/" + sub("ρ", "f"), "GREEN", "middle", 14)
    rect(c, x0 + 150, 270 - 95, 70, 95, "BLUE", 1.6, fill="BLUE", opacity=0.20)
    lab(c, (x0 + 185, 167), sub("V", "a") + " = " + sub("ρ", "h") + sub("V", "h") + "/" + sub("ρ", "a"), "BLUE", "middle", 14)
    dim(c, (x0 + 240, 270 - 95), (x0 + 240, 270 - 70), sub("V", "d"), "ACC", (8, 5), "start", 16)
    line(c, (x0 + 30, 200), (x0 + 250, 200), "EDGE", 0.8, dash="3,3")
    note(c, (490, 296), "(b) after melting: " + sub("V", "d") + " = " + sub("V", "a") + " − " + sub("V", "s"), "TEXT", size=13)
    put("fs1-fbd", c,
        "Left: free-body diagram of the floating cube, weight rho_h g V_h and buoyancy rho_f g V_s. Right: the volume V_s "
        "displaced by the cube and the volume V_a of its melt water; the difference V_d is the extra volume of liquid",
        "(a) The floating cube: weight $\\rho_h g V_h$ at its centre of gravity, buoyancy $\\rho_f g V_s$ at the centroid of the "
        "submerged part. (b) The cube displaced $V_s$; once melted, the same mass occupies $V_a = \\rho_h V_h/\\rho_a$; the "
        "difference $V_d = V_a - V_s$ is the volume the liquid gains")


# ------------------------------------------------------------------------------------------------- FS2 (= FS8)
def fs2():
    c = Canvas(560, 300)
    liquid(c, [(40, 50), (520, 50), (520, 250), (40, 250)], 0.08)
    water_surface(c, 40, 520, 50)
    floor(c, 40, 520, 250)
    cx, R = 330, 80
    pathd(c, f"M{cx - R},250 A{R},{R} 0 0 1 {cx + R},250 Z", "HEAD", 2.4, fill="ACC", opacity=0.10)
    lab(c, (cx, 230), sub("p", "a"), "HEAD", "middle", 16)
    line(c, (cx, 250), (cx + R * 0.7071, 250 - R * 0.7071), "EDGE", 1.0, dash="4,3")
    lab(c, (cx + 34, 214), "R", "HEAD", "start", 16)
    dim(c, (110, 50), (110, 250), "H", "TEXT", (-10, 5), "end", 18)
    arrow(c, (160, 250), (160, 200), "HEAD", 1.4, 8)
    lab(c, (168, 206), "z", "HEAD", "start", 16)
    put("fs2-statement", c,
        "Hemispherical station of radius R on the sea floor at depth H, air at p_a inside, axis z up from the floor",
        "Statement figure (redrawn from fluid_statics_2.pdf and fluid_statics_8.pdf, p. 1): hemispherical station of radius $R$ "
        "on the sea floor at depth $H$, atmospheric pressure $p_a$ inside, axis $z$ up from the floor")

    c = Canvas(720, 325)
    # meridian section
    O = (190, 270)
    R = 150
    pathd(c, f"M{O[0] - R},{O[1]} A{R},{R} 0 0 1 {O[0] + R},{O[1]}", "HEAD", 2.2)
    line(c, (O[0] - R - 20, O[1]), (O[0] + R + 20, O[1]), "EDGE", 1.4)
    phi = math.radians(40)
    P = (O[0] + R * math.cos(phi), O[1] - R * math.sin(phi))
    line(c, O, P, "GREEN", 1.4)
    line(c, P, (P[0], O[1]), "GREEN", 1.2, dash="4,3")
    lab(c, (P[0] + 6, (P[1] + O[1]) / 2 + 20), "z = R sin φ", "GREEN", "start", 15)
    lab(c, ((O[0] + P[0]) / 2, O[1] + 20), "R cos φ", "GREEN", "middle", 15)
    lab(c, ((O[0] + P[0]) / 2 + 12, (O[1] + P[1]) / 2 + 16), "R", "GREEN", "start", 16)
    arc(c, O, 40, 0, -40, "HEAD", 1.3)
    lab(c, (O[0] + 48, O[1] - 12), "φ", "HEAD", "start", 17)
    er = (math.cos(phi), -math.sin(phi))
    arrow(c, P, (P[0] + 60 * er[0], P[1] + 60 * er[1]), "BLUE", 2.2, 10)
    lab(c, (P[0] + 64 * er[0] + 4, P[1] + 64 * er[1]), "n = " + sub("e", "r"), "BLUE", "start", 16)
    arrow(c, (P[0] - 6 * er[0], P[1] - 6 * er[1]), (P[0] - 55 * er[0], P[1] - 55 * er[1]), "ACC", 2.2, 10)
    lab(c, (P[0] - 60 * er[0] - 8, P[1] - 60 * er[1] - 4), "−(p−pₐ) n dS", "ACC", "end", 14, italic=False)
    arc(c, P, 26, -40, -90, "BLUE", 1.0)
    line(c, P, (P[0], P[1] - 40), "EDGE", 0.9, dash="3,3")
    lab(c, (P[0] - 6, P[1] - 44), sub("n", "z") + " = sin φ", "BLUE", "end", 14)
    dot(c, O, 3.4)
    lab(c, (O[0] - 6, O[1] + 18), "O", "HEAD", "end", 15, italic=False)
    note(c, (190, 312), "meridian section θ = const", "TEXT", size=13)
    # element on the sphere: top view
    T = (540, 160)
    circle(c, T, 120, "HEAD", 1.6)
    circle(c, T, 120 * math.cos(phi), "GREEN", 1.4, dash="5,4")
    th = math.radians(-30)
    Q = (T[0] + 92 * math.cos(th), T[1] + 92 * math.sin(th))
    line(c, T, Q, "GREEN", 1.2)
    arc(c, T, 30, 0, -30, "HEAD", 1.2)
    lab(c, (T[0] + 36, T[1] - 4), "θ", "HEAD", "start", 16)
    rect(c, Q[0] - 7, Q[1] - 7, 14, 14, "ACC", 1.4, fill="ACC", opacity=0.35)
    lab(c, (Q[0] + 12, Q[1] - 10), "dS", "ACC", "start", 16)
    lab(c, (T[0], 296), "dashed: ring of radius R cos φ", "GREEN", "middle", 13, italic=False)
    lab(c, (T[0], 316), "dS = (R cos φ dθ)(R dφ)", "ACC", "middle", 15)
    note(c, (540, 22), "top view", "TEXT", size=13)
    put("fs2-geometry", c,
        "Left: meridian section of the hemisphere with the elevation angle phi, the right triangle z = R sin phi and R cos phi, "
        "the outward normal e_r and its vertical component sin phi. Right: top view with the ring of radius R cos phi and the "
        "element dS = R^2 cos phi dtheta dphi",
        "Spherical coordinates of the station. Left: meridian section; the radius $R$ is the hypotenuse, $z = R\\sin\\varphi$ is "
        "the leg opposite to the elevation $\\varphi$ and $R\\cos\\varphi$ the adjacent leg; the outward normal is $\\vec{e}_r$, with "
        "$n_z = \\sin\\varphi$; the water pushes along $-\\vec{e}_r$. Right: top view; at elevation $\\varphi$ the parallel is a ring of "
        "radius $R\\cos\\varphi$, so the element is $dS = (R\\cos\\varphi\\,d\\theta)(R\\,d\\varphi)$")

    c = Canvas(560, 300)
    liquid(c, [(40, 40), (520, 40), (520, 260), (40, 260)], 0.06)
    water_surface(c, 40, 520, 40, label=False)
    floor(c, 40, 520, 260)
    cx, R = 280, 90
    pathd(c, f"M{cx - R},40 L{cx - R},260 A{R},{R} 0 0 1 {cx + R},260 L{cx + R},40 Z", "BLUE", 1.6, fill="BLUE", opacity=0.22)
    pathd(c, f"M{cx - R},260 A{R},{R} 0 0 1 {cx + R},260 Z", "HEAD", 2.2, fill="ACC", opacity=0.15)
    arrow(c, (cx, 70), (cx, 150), "ACC", 3.0, 12)
    lab(c, (cx + 10, 120), sub("F", "z"), "ACC", "start", 18)
    lab(c, (cx + R + 14, 120), "column πR²H", "BLUE", "start", 14, italic=False)
    lab(c, (cx + R + 14, 140), "minus hemisphere (2/3)πR³", "TEXT", "start", 14, italic=False)
    dim(c, (cx - R - 30, 40), (cx - R - 30, 260), "H", "TEXT", (-10, 5), "end", 18)
    put("fs2-column", c,
        "Check by the projection rule: the vertical force is the weight of the water column of radius R and height H above the "
        "floor minus the hemisphere, which is not water",
        "Projection rule (Eq. 5.14): $F_z$ is the weight of the water that would stand above the hemisphere, the cylinder "
        "$\\pi R^2 H$ minus the hemisphere $\\tfrac{2}{3}\\pi R^3$; it points down")


# ------------------------------------------------------------------------------------------------- FS3
def fs3():
    c = Canvas(560, 300)
    x0, y0, Lp = 190, 50, 180
    lab(c, (110, 80), sub("p", "a"), "HEAD", "middle", 18)
    liquid(c, [(40, 130), (x0, 130), (x0, 280), (40, 280)], 0.08)
    liquid(c, [(x0 + Lp, 130), (520, 130), (520, 280), (x0 + Lp, 280)], 0.08)
    line(c, (40, 130), (x0, 130), "BLUE", 1.6)
    line(c, (x0 + Lp, 130), (520, 130), "BLUE", 1.6)
    liquid(c, [(x0, y0 + Lp), (x0 + Lp, y0 + Lp), (x0 + Lp, 280), (x0, 280)], 0.08)
    liquid(c, [(x0, 160), (x0 + Lp, 160), (x0 + Lp, y0 + Lp), (x0, y0 + Lp)], 0.22)
    rect(c, x0, y0, Lp, Lp, "HEAD", 2.2)
    line(c, (x0, 160), (x0 + Lp, 160), "BLUE", 1.4)
    line(c, (x0 + Lp / 2 - 8, y0 + Lp), (x0 + Lp / 2 + 8, y0 + Lp), "BLUE", 4)
    lab(c, (x0 + Lp / 2, 110), sub("p", "c"), "HEAD", "middle", 18)
    dim(c, (420, 130), (420, 160), sub("H", "1"), "TEXT", (10, 5), "start", 17)
    dim(c, (420, 160), (420, y0 + Lp), sub("H", "2"), "TEXT", (10, 5), "start", 17)
    line(c, (x0 + Lp, 160), (430, 160), "EDGE", 0.8, dash="3,3")
    line(c, (x0 + Lp, y0 + Lp), (430, y0 + Lp), "EDGE", 0.8, dash="3,3")
    dim(c, (x0, y0 - 14), (x0 + Lp, y0 - 14), "L", "TEXT", (0, -6), size=16)
    lab(c, (x0 + Lp / 2, 250), "orifice", "TEXT", "middle", 12, italic=False)
    put("fs3-statement", c,
        "Hollow cube of side L floating with an orifice in its base; outer free surface, inner interface H_1 below it and "
        "inner water layer H_2, air at p_c inside and p_a outside",
        "Statement figure (redrawn from fluid_statics_3.pdf, p. 1): hollow cube of side $L$ with an orifice in its base; the "
        "inner interface is $H_1$ below the outer free surface and $H_2$ above the base; air at $p_c$ inside, $p_a$ outside")

    c = Canvas(700, 320)
    x0, y0, Lp = 120, 60, 180
    liquid(c, [(30, 140), (x0, 140), (x0, 300), (30, 300)], 0.08)
    liquid(c, [(x0 + Lp, 140), (360, 140), (360, 300), (x0 + Lp, 300)], 0.08)
    line(c, (30, 140), (x0, 140), "BLUE", 1.6)
    line(c, (x0 + Lp, 140), (360, 140), "BLUE", 1.6)
    liquid(c, [(x0, y0 + Lp), (x0 + Lp, y0 + Lp), (x0 + Lp, 300), (x0, 300)], 0.08)
    liquid(c, [(x0, 175), (x0 + Lp, 175), (x0 + Lp, y0 + Lp), (x0, y0 + Lp)], 0.22)
    rect(c, x0, y0, Lp, Lp, "HEAD", 2.2)
    line(c, (x0, 175), (x0 + Lp, 175), "BLUE", 1.4)
    for k in range(5):
        xx = x0 + 20 + k * 35
        arrow(c, (xx, y0 - 34), (xx, y0 - 3), "BLUE", 1.1, 6)
        arrow(c, (xx + 10, y0 + 42), (xx + 10, y0 + 4), "ACC", 1.1, 6)
    lab(c, (x0 + Lp + 8, y0 - 18), sub("p", "a") + sub("L", "2", sup=True), "BLUE", "start", 15)
    lab(c, (x0 + Lp - 8, y0 + 58), sub("p", "c") + sub("L", "2", sup=True), "ACC", "end", 15)
    dot(c, (x0 + Lp / 2, y0 + 52), 3.6, "PINK")
    arrow(c, (x0 + Lp / 2, y0 + 52), (x0 + Lp / 2, y0 + 104), "PINK", 2.6, 11)
    lab(c, (x0 + Lp / 2 + 8, y0 + 96), "W", "PINK", "start", 17)
    note(c, (x0 + Lp / 2, 316), "(a) shell of the cube: top face", "TEXT", size=13)
    # (b) pressure walk
    xw = 470
    line(c, (xw, 60), (xw, 260), "EDGE", 1.0)
    dot(c, (xw, 90), 4, "BLUE")
    lab(c, (xw + 12, 95), "outer free surface: p = pₐ", "BLUE", "start", 14, italic=False)
    arrow(c, (xw - 14, 96), (xw - 14, 176), "BLUE", 1.4, 8)
    lab(c, (xw - 20, 140), "+ρg" + sub("H", "1"), "BLUE", "end", 15)
    dot(c, (xw, 180), 4, "ACC")
    lab(c, (xw + 12, 185), "inner interface: " + sub("p", "c") + " = pₐ + ρg" + sub("H", "1"), "ACC", "start", 14, italic=False)
    lab(c, (xw + 12, 215), "(gas pressure uniform", "TEXT", "start", 13, italic=False)
    lab(c, (xw + 12, 233), "inside the cube)", "TEXT", "start", 13, italic=False)
    note(c, (560, 316), "(b) walk through the liquid", "TEXT", size=13)
    put("fs3-fbd", c,
        "Left: free-body diagram of the cube shell; the outside air pushes the top face down with p_a L^2, the trapped air pushes "
        "it up with p_c L^2, and the weight W acts down. Right: walk from the outer free surface down H_1 to the inner interface",
        "(a) Vertical forces on the shell of the cube (thin walls): $p_a L^2$ down on the top face from outside, $p_c L^2$ up on "
        "it from the trapped air, weight $W$ down; the side walls carry only horizontal forces, which cancel. (b) Walking from "
        "the outer free surface down the depth $H_1$ to the inner interface gives $p_c = p_a + \\rho g H_1$")


# ------------------------------------------------------------------------------------------------- FS4
def fs4():
    c = Canvas(560, 300)
    liquid(c, [(80, 70), (330, 70), (330, 260), (80, 260)], 0.08)
    line(c, (80, 40), (80, 260), "HEAD", 2.0)
    line(c, (80, 260), (440, 260), "HEAD", 2.0)
    line(c, (330, 40), (330, 196), "HEAD", 2.0)
    line(c, (330, 196), (440, 196), "HEAD", 2.0)
    line(c, (84, 70), (326, 70), "BLUE", 1.6)
    for dx in (-14, 0, 14):
        line(c, (200 + dx - 6, 64), (200 + dx + 6, 64), "BLUE", 1.0)
    line(c, (330, 196), (330, 260), "ACC", 5)
    dot(c, (330, 228), 4, "HEAD")
    lab(c, (340, 222), "O", "HEAD", "start", 15, italic=False)
    arrow(c, (280, 228), (326, 228), "ACC", 2.4, 10)
    lab(c, (290, 220), "F", "ACC", "end", 17)
    arrow(c, (370, 256), (336, 256), "PINK", 2.2, 9)
    lab(c, (378, 252), sub("F", "A"), "PINK", "start", 16)
    dim(c, (60, 70), (60, 260), "h", "TEXT", (-10, 5), "end", 18)
    dim(c, (460, 196), (460, 260), "L", "TEXT", (10, 5), "start", 18)
    arrow(c, (200, 258), (200, 216), "HEAD", 1.4, 8)
    lab(c, (208, 222), "z", "HEAD", "start", 16)
    put("fs4-statement", c,
        "Tank of depth h with a square valve of side L in the right wall at the bottom, pivoting about a horizontal axis O "
        "through its centre; F is the water force and F_A the force applied at the base of the valve",
        "Statement figure (redrawn from fluid_statics_4.pdf, p. 1): square valve of side $L$ at the bottom of the right wall, "
        "pivoting about the horizontal axis $O$ through its centre; water depth $h$; $F_A$ is applied at the base of the valve")

    c = Canvas(720, 320)
    # side view with the pressure distribution on the valve
    xw, yb, Lp = 250, 280, 180
    k = 0.45
    line(c, (xw, yb - Lp - 40), (xw, yb), "HEAD", 1.6)
    line(c, (xw, yb - Lp), (xw, yb), "ACC", 5)
    hd = 130                                          # free surface above the top edge (screen units)
    p = lambda zz: (hd + Lp - zz)                     # depth below the free surface
    for zz in range(0, Lp + 1, 20):
        y = yb - zz
        arrow(c, (xw - k * p(zz), y), (xw - 2, y), "BLUE", 1.1, 6)
    poly(c, [(xw, yb), (xw - k * p(0), yb), (xw - k * p(Lp), yb - Lp), (xw, yb - Lp)], "BLUE", 1.2)
    lab(c, (xw - k * p(0) - 6, yb + 4), "ρg h", "BLUE", "end", 15)
    lab(c, (xw - k * p(Lp) - 6, yb - Lp + 4), "ρg(h − L)", "BLUE", "end", 15)
    dot(c, (xw, yb - Lp / 2), 4, "HEAD")
    lab(c, (xw + 10, yb - Lp / 2 + 5), "O  (z = L/2)", "HEAD", "start", 15, italic=False)
    zz = 50
    rect(c, xw + 2, yb - zz - 5, 12, 10, "GREEN", 1.2, fill="GREEN", opacity=0.4)
    lab(c, (xw + 20, yb - zz - 9), "dA = L dz at height z", "GREEN", "start", 14, italic=False)
    dim(c, (xw + 200, yb - Lp / 2), (xw + 200, yb - zz), "L/2 − z", "GREEN", (8, 5), "start", 15)
    line(c, (xw + 14, yb - zz), (xw + 205, yb - zz), "EDGE", 0.8, dash="3,3")
    line(c, (xw + 150, yb - Lp / 2), (xw + 205, yb - Lp / 2), "EDGE", 0.8, dash="3,3")
    arrow(c, (xw + 60, yb), (xw + 60, yb - 40), "HEAD", 1.3, 8)
    lab(c, (xw + 68, yb - 30), "z", "HEAD", "start", 16)
    line(c, (xw - 10, yb), (xw + 120, yb), "EDGE", 1.0)
    note(c, (200, 312), "side view: p(z) = pₐ + ρg(h − z) on 0 ≤ z ≤ L", "TEXT", size=13)
    # front view of the valve
    fx, fy, fs = 560, 90, 150
    rect(c, fx, fy, fs, fs, "ACC", 2.0, fill="ACC", opacity=0.08)
    line(c, (fx - 16, fy + fs / 2), (fx + fs + 16, fy + fs / 2), "HEAD", 1.2, dash="8,4")
    lab(c, (fx + fs + 18, fy + fs / 2 + 5), "axis", "HEAD", "start", 13, italic=False)
    rect(c, fx, fy + fs - 50, fs, 9, "GREEN", 1.2, fill="GREEN", opacity=0.4)
    dim(c, (fx, fy + fs + 16), (fx + fs, fy + fs + 16), "L", "TEXT", (0, 18), size=16)
    lab(c, (fx + fs / 2, fy - 12), "front view", "TEXT", "middle", 13, italic=False)
    put("fs4-geometry", c,
        "Side view of the valve with the trapezoidal pressure distribution from rho g (h - L) at the top to rho g h at the "
        "bottom, the strip dA = L dz at height z and its arm L/2 - z about the axis O; front view of the square valve",
        "Left: side view; the gauge pressure on the valve grows linearly from $\\rho g(h-L)$ at the top edge to $\\rho g h$ at the "
        "bottom; the strip $dA = L\\,dz$ at height $z$ has the arm $L/2 - z$ about the axis $O$. Right: front view of the valve, "
        "the horizontal axis through its centre and the strip")

    c = Canvas(560, 300)
    xw, yb, Lp = 260, 270, 200
    line(c, (xw, yb - Lp), (xw, yb), "ACC", 5)
    dot(c, (xw, yb - Lp / 2), 4.5, "HEAD")
    lab(c, (xw + 12, yb - Lp / 2 - 6), "O", "HEAD", "start", 16, italic=False)
    e = 34
    arrow(c, (xw - 110, yb - Lp / 2 + e), (xw - 4, yb - Lp / 2 + e), "ACC", 3.0, 12)
    lab(c, (xw - 112, yb - Lp / 2 + e - 10), "F", "ACC", "start", 18)
    dot(c, (xw, yb - Lp / 2 + e), 3.4, "ACC")
    lab(c, (xw - 8, yb - Lp / 2 + e + 18), "CP", "ACC", "end", 14, italic=False)
    dim(c, (xw + 50, yb - Lp / 2), (xw + 50, yb - Lp / 2 + e), "e", "TEXT", (8, 5), "start", 16)
    line(c, (xw + 4, yb - Lp / 2 + e), (xw + 56, yb - Lp / 2 + e), "EDGE", 0.8, dash="3,3")
    arrow(c, (xw + 100, yb), (xw + 4, yb), "PINK", 2.6, 11)
    lab(c, (xw + 104, yb + 4), sub("F", "A"), "PINK", "start", 17)
    dim(c, (xw + 150, yb - Lp / 2), (xw + 150, yb), "L/2", "TEXT", (8, 5), "start", 16)
    line(c, (xw + 4, yb - Lp / 2), (xw + 156, yb - Lp / 2), "EDGE", 0.8, dash="3,3")
    arrow(c, (xw - 40, yb - Lp / 2 - 40), (xw - 6, yb - Lp / 2 - 6), "PINK", 1.8, 9)
    lab(c, (xw - 44, yb - Lp / 2 - 44), "axis reaction", "PINK", "end", 13, italic=False)
    put("fs4-fbd", c,
        "Free-body diagram of the valve: water force F at the centre of pressure, a distance e below the axis O; force F_A "
        "at the base, arm L/2; reaction of the axis at O",
        "Free-body diagram of the valve: the water force $F$ acts at the centre of pressure, a distance $e$ below the axis $O$; "
        "$F_A$ acts at the base with the arm $L/2$; the axis reaction passes through $O$ and has no moment about it")


# ------------------------------------------------------------------------------------------------- FS5
def fs5():
    c = Canvas(560, 300)
    xg, yb, H1, H2 = 300, 260, 190, 120
    liquid(c, [(90, yb - H1), (xg, yb - H1), (xg, yb), (90, yb)], 0.08)
    liquid(c, [(xg, yb - H2), (480, yb - H2), (480, yb), (xg, yb)], 0.20)
    line(c, (90, 40), (90, yb), "HEAD", 2.0)
    line(c, (480, 40), (480, yb), "HEAD", 2.0)
    floor(c, 90, 480, yb)
    line(c, (90, yb - H1), (xg, yb - H1), "BLUE", 1.6)
    line(c, (xg, yb - H2), (480, yb - H2), "BLUE", 1.6)
    line(c, (xg, yb - H1), (xg, yb), "ACC", 4.5)
    dot(c, (xg, yb), 5, "HEAD")
    poly(c, [(xg + 3, yb - H1), (xg + 15, yb - H1 - 7), (xg + 15, yb - H1 + 7)], "HEAD", 1.4, close=True)
    lab(c, (190, 160), sub("ρ", "1"), "HEAD", "middle", 18)
    lab(c, (390, 210), sub("ρ", "2"), "HEAD", "middle", 18)
    lab(c, (190, yb - H1 - 10), sub("p", "a"), "HEAD", "middle", 16)
    lab(c, (390, yb - H2 - 10), sub("p", "a"), "HEAD", "middle", 16)
    dim(c, (60, yb - H1), (60, yb), sub("H", "1"), "TEXT", (-10, 5), "end", 17)
    dim(c, (510, yb - H2), (510, yb), sub("H", "2"), "TEXT", (10, 5), "start", 17)
    lab(c, (xg + 20, yb - H1 - 6), "stop", "TEXT", "start", 12, italic=False)
    lab(c, (xg + 10, yb + 22), "hinge", "TEXT", "start", 12, italic=False)
    put("fs5-statement", c,
        "Vertical gate between two liquids, rho_1 on the left with height H_1 and rho_2 on the right with height H_2, hinged "
        "at the bottom and resting against a stop at the top",
        "Statement figure (redrawn from fluid_statics_5.pdf, p. 1): gate of height $H_1$ between the liquids $\\rho_1$ (left, "
        "height $H_1$) and $\\rho_2 > \\rho_1$ (right, height $H_2 < H_1$), hinged at the bottom and resting on a stop at the top")

    c = Canvas(640, 320)
    xg, yb, H1, H2, k = 320, 290, 240, 150, 0.55
    line(c, (xg, yb - H1), (xg, yb), "ACC", 5)
    dot(c, (xg, yb), 5, "HEAD")
    lab(c, (xg + 10, yb + 18), "hinge O", "HEAD", "start", 14, italic=False)
    for zz in range(0, H1 + 1, 24):
        L = k * (H1 - zz)
        if L > 6:
            arrow(c, (xg - L, yb - zz), (xg - 3, yb - zz), "BLUE", 1.1, 6)
    poly(c, [(xg, yb), (xg - k * H1, yb), (xg, yb - H1)], "BLUE", 1.2)
    for zz in range(12, H2 + 1, 24):
        L = 1.4 * k * (H2 - zz)
        if L > 6:
            arrow(c, (xg + L, yb - zz), (xg + 3, yb - zz), "GREEN", 1.1, 6)
    poly(c, [(xg, yb), (xg + 1.4 * k * H2, yb), (xg, yb - H2)], "GREEN", 1.2)
    arrow(c, (xg - 70, yb - H1 / 3), (xg - 6, yb - H1 / 3), "ACC", 3.0, 12)
    lab(c, (xg - 50, yb - H1 / 3 + 22), sub("F", "1"), "ACC", "middle", 18)
    arrow(c, (xg + 150, yb - H2 / 3), (xg + 6, yb - H2 / 3), "ACC", 3.0, 12)
    lab(c, (xg + 154, yb - H2 / 3 + 5), sub("F", "2"), "ACC", "start", 18)
    arrow(c, (xg + 60, yb - H1), (xg + 4, yb - H1), "PINK", 2.6, 11)
    lab(c, (xg + 64, yb - H1 + 5), "R (stop)", "PINK", "start", 15)
    dim(c, (xg - 200, yb - H1 / 3), (xg - 200, yb), sub("H", "1") + "/3", "TEXT", (-8, 5), "end", 15)
    line(c, (xg - 205, yb - H1 / 3), (xg - 76, yb - H1 / 3), "EDGE", 0.8, dash="3,3")
    dim(c, (xg + 230, yb - H2 / 3), (xg + 230, yb), sub("H", "2") + "/3", "TEXT", (8, 5), "start", 15)
    line(c, (xg + 160, yb - H2 / 3), (xg + 235, yb - H2 / 3), "EDGE", 0.8, dash="3,3")
    line(c, (xg - 205, yb), (xg + 235, yb), "EDGE", 0.8, dash="3,3")
    arrow(c, (xg, yb + 2), (xg, yb - 34), "HEAD", 1.3, 8)
    lab(c, (xg - 8, yb - 36), "z", "HEAD", "end", 16)
    lab(c, (xg - 120, yb - 120), sub("ρ", "1") + "g(" + sub("H", "1") + " − z)", "BLUE", "end", 14)
    lab(c, (xg + 100, yb - 70), sub("ρ", "2") + "g(" + sub("H", "2") + " − z)", "GREEN", "start", 14)
    put("fs5-fbd", c,
        "Free-body diagram of the gate: triangular pressure distributions of the two liquids, their resultants F_1 and F_2 at "
        "H_1/3 and H_2/3 above the hinge, reaction R of the stop at the top and the hinge O",
        "Free-body diagram of the gate (unit width): the triangular gauge pressures $\\rho_1 g(H_1 - z)$ and $\\rho_2 g(H_2 - z)$, "
        "their resultants $F_1$ and $F_2$ at $H_1/3$ and $H_2/3$ above the hinge $O$, and the stop reaction $R$ at the top")


# ------------------------------------------------------------------------------------------------- FS6
def fs6():
    s3 = math.sqrt(3)
    c = Canvas(560, 300)
    Lp = 220
    Hp = Lp * s3 / 2
    xb, yb = 150, 270
    A, B, Cpt = (xb, yb), (xb + Lp, yb), (xb + Lp / 2, yb - Hp)
    ws = yb - 100                                       # outer free surface
    hi = 30                                            # inner level below the outer one
    yi = ws + hi
    liquid(c, [(40, ws), (520, ws), (520, 290), (40, 290)], 0.08)
    line(c, (40, ws), (xb + (yb - ws) / s3 * 0 + (Hp - (yb - ws)) / s3 * 0 + 30, ws), "BLUE", 1.6)
    xl = lambda y: xb + (yb - y) / s3                   # left side at height y
    xr = lambda y: xb + Lp - (yb - y) / s3
    line(c, (40, ws), (xl(ws), ws), "BLUE", 1.6)
    line(c, (xr(ws), ws), (520, ws), "BLUE", 1.6)
    poly(c, [(xl(yi), yi), (xr(yi), yi), B, A], "BLUE", 0, fill="BLUE", close=True, opacity=0.14)
    poly(c, [A, Cpt, B], "HEAD", 2.2)
    line(c, (xb + Lp / 2 - 18, yb), (xb + Lp / 2 + 18, yb), "BLUE", 4)
    line(c, (xl(yi), yi), (xr(yi), yi), "BLUE", 1.4)
    dim(c, (Cpt[0] - 18, ws), (Cpt[0] - 18, yi), "h", "TEXT", (-8, 5), "end", 16)
    dim(c, (470, ws), (470, yb), "H", "TEXT", (10, 5), "start", 17)
    line(c, B, (476, yb), "EDGE", 0.8, dash="3,3")
    dim(c, (xb, yb + 16), (xb + Lp, yb + 16), "L", "TEXT", (0, 18), size=16)
    put("fs6-statement", c,
        "Equilateral triangle of side L, open through an orifice in its lower side, floating with its base at depth H below "
        "the outer free surface and the inner level a depth h below it",
        "Statement figure (redrawn from fluid_statics_6.pdf, p. 1): equilateral triangle of side $L$ with an orifice in the "
        "lower side; its base is at the depth $H$ below the outer free surface and the inner level is $h$ below it")

    c = Canvas(720, 330)
    Lp = 260
    Hp = Lp * s3 / 2
    xb, yb = 70, 300
    A, B, Cpt = (xb, yb), (xb + Lp, yb), (xb + Lp / 2, yb - Hp)
    xl = lambda y: xb + (yb - y) / s3
    xr = lambda y: xb + Lp - (yb - y) / s3
    ws, yi = yb - 120, yb - 120 + 34
    poly(c, [(xl(yi), yi), (xr(yi), yi), Cpt], "ACC", 0, fill="ACC", close=True, opacity=0.18)
    poly(c, [(xl(ws), ws), (xr(ws), ws), (xr(yi), yi), (xl(yi), yi)], "GREEN", 0, fill="GREEN", close=True, opacity=0.35)
    poly(c, [A, Cpt, B], "HEAD", 2.2)
    line(c, (20, ws), (xl(ws), ws), "BLUE", 1.6)
    line(c, (xr(ws), ws), (xr(ws) + 50, ws), "BLUE", 1.6)
    line(c, (xl(yi), yi), (xr(yi), yi), "BLUE", 1.4)
    line(c, Cpt, (Cpt[0], yb), "EDGE", 0.9, dash="4,4")
    xa = 400
    dim(c, (xa, Cpt[1]), (xa, yi), "a = L√3/2 + h − H", "ACC", (8, 18), "start", 15)
    line(c, Cpt, (xa + 6, Cpt[1]), "EDGE", 0.8, dash="3,3")
    line(c, (xr(yi), yi), (xa + 6, yi), "EDGE", 0.8, dash="3,3")
    dim(c, (xa + 200, Cpt[1]), (xa + 200, ws), "L√3/2 − H", "GREEN", (8, 5), "start", 15)
    line(c, (xa + 6, Cpt[1]), (xa + 206, Cpt[1]), "EDGE", 0.8, dash="3,3")
    line(c, (xr(ws), ws), (xa + 206, ws), "EDGE", 0.8, dash="3,3")
    dim(c, (xl(yi), yi + 18), (Cpt[0], yi + 18), "a/√3", "ACC", (0, 18), size=14)
    arc(c, Cpt, 34, 90, 120, "HEAD", 1.2)
    lab(c, (Cpt[0] - 17, Cpt[1] + 58), "30°", "HEAD", "middle", 12, italic=False)
    lab(c, (Cpt[0], ws - 14), sub("A", "T"), "HEAD", "middle", 15)
    lab(c, (Cpt[0] + 30, ws + 24), sub("A", "d"), "GREEN", "start", 15)
    dim(c, (xb, yb + 12), (xb + Lp, yb + 12), "L", "TEXT", (-30, 16), size=15)
    lab(c, (20, ws - 8), "outer free surface", "BLUE", "start", 12, italic=False)
    put("fs6-geometry", c,
        "Similar triangles of the deduction: the air triangle of height a = L sqrt3/2 + h - H above the inner level, its half "
        "base a/sqrt3 from the 30 degree half-angle at the apex, the emerged triangle A_T above the outer free surface and the "
        "displaced area A_d between the two levels",
        "Every horizontal section of the equilateral triangle is the base of a smaller equilateral triangle with the same apex. "
        "The half-angle at the apex is $30^\\circ$, so a triangle of height $a$ has the half base $a\\tan 30^\\circ = a/\\sqrt{3}$ "
        "and the area $a^2/\\sqrt{3}$. Orange: the air triangle, height $a = L\\sqrt{3}/2 + h - H$; green: the displaced area "
        "$A_d$ between the outer free surface and the inner level; $A_T$: the part above the outer free surface")

    c = Canvas(560, 300)
    Lp = 220
    Hp = Lp * s3 / 2
    xb, yb = 120, 270
    A, B, Cpt = (xb, yb), (xb + Lp, yb), (xb + Lp / 2, yb - Hp)
    xl = lambda y: xb + (yb - y) / s3
    xr = lambda y: xb + Lp - (yb - y) / s3
    ws, yi = yb - 100, yb - 70
    poly(c, [(xl(ws), ws), (xr(ws), ws), (xr(yi), yi), (xl(yi), yi)], "GREEN", 0, fill="GREEN", close=True, opacity=0.3)
    poly(c, [A, Cpt, B], "HEAD", 2.0)
    line(c, (40, ws), (xl(ws), ws), "BLUE", 1.6)
    line(c, (xr(ws), ws), (520, ws), "BLUE", 1.6)
    line(c, (xl(yi), yi), (xr(yi), yi), "BLUE", 1.4)
    dot(c, (Cpt[0] + 30, ws - 34), 3.6, "PINK")
    arrow(c, (Cpt[0] + 30, ws - 34), (Cpt[0] + 30, ws + 46), "PINK", 2.6, 11)
    lab(c, (Cpt[0] + 38, ws + 8), "W", "PINK", "start", 17)
    arrow(c, (Cpt[0] - 20, ws + 22), (Cpt[0] - 20, ws - 70), "ACC", 2.6, 11)
    lab(c, (Cpt[0] - 12, ws - 82), "ρg" + sub("A", "d"), "ACC", "start", 17)
    lab(c, (430, 120), "system: triangle + air", "TEXT", "middle", 13, italic=False)
    lab(c, (430, 140), "(unit length)", "TEXT", "middle", 13, italic=False)
    put("fs6-fbd", c,
        "Free-body diagram of the floating system triangle plus trapped air, per unit length: weight W down and buoyancy "
        "rho g A_d up, A_d being the air area below the outer free surface",
        "Free-body diagram of the system triangle plus trapped air, per unit length: the weight $W$ (air weight neglected) and "
        "the buoyancy $\\rho g A_d$, where $A_d$ is the part of the air region below the outer free surface (Archimedes, Eq. 5.15)")


# ------------------------------------------------------------------------------------------------- FS7
def fs7():
    c = Canvas(560, 300)
    O = (280, 250)
    al = math.radians(30)
    Hh = 200
    TL = (O[0] - Hh * math.tan(al), O[1] - Hh)
    TR = (O[0] + Hh * math.tan(al), O[1] - Hh)
    h1, h2 = 140, 95
    liquid(c, [(40, O[1] - h1), (O[0] - h1 * math.tan(al), O[1] - h1), O, (40, O[1])], 0.10)
    liquid(c, [(O[0] + h2 * math.tan(al), O[1] - h2), (520, O[1] - h2), (520, O[1]), O], 0.22)
    floor(c, 30, 530, O[1])
    poly(c, [TL, TR, O], "HEAD", 2.2, fill="ACC", close=True, opacity=0.08)
    line(c, (40, O[1] - h1), (O[0] - h1 * math.tan(al), O[1] - h1), "BLUE", 1.6)
    line(c, (O[0] + h2 * math.tan(al), O[1] - h2), (520, O[1] - h2), "BLUE", 1.6)
    arc(c, O, 40, -120, -60, "HEAD", 1.2)
    lab(c, (O[0], O[1] - 48), "2α", "HEAD", "middle", 16)
    lab(c, (O[0], O[1] + 20), "O", "HEAD", "middle", 15, italic=False)
    dim(c, (150, O[1] - h1), (150, O[1]), sub("h", "1"), "TEXT", (-8, 5), "end", 17)
    dim(c, (430, O[1] - h2), (430, O[1]), sub("h", "2"), "TEXT", (8, 5), "start", 17)
    lab(c, (80, O[1] - 20), sub("ρ", "1"), "HEAD", "middle", 17)
    lab(c, (490, O[1] - 20), sub("ρ", "2"), "HEAD", "middle", 17)
    lab(c, (500, 40), sub("p", "a"), "HEAD", "middle", 16)
    put("fs7-statement", c,
        "Two-dimensional wedge of angle 2 alpha resting on its lower vertex O, liquid rho_1 of depth h_1 on the left and "
        "rho_2 of depth h_2 on the right",
        "Statement figure (redrawn from fluid_statics_7.pdf, p. 1): wedge of angle $2\\alpha$ and weight $W$ per unit length "
        "resting on its vertex $O$; liquid $\\rho_1$ of depth $h_1$ on the left and $\\rho_2 > \\rho_1$ of depth $h_2$ on the right")

    c = Canvas(700, 330)
    O = (300, 300)
    al = math.radians(30)
    Hh = 260
    TL = (O[0] - Hh * math.tan(al), O[1] - Hh)
    TR = (O[0] + Hh * math.tan(al), O[1] - Hh)
    poly(c, [TL, TR, O], "HEAD", 2.0, fill="ACC", close=True, opacity=0.06)
    line(c, O, (O[0], O[1] - Hh), "EDGE", 0.9, dash="4,4")
    y = 150
    Pp = (O[0] - y * math.tan(al), O[1] - y)
    dy = 36
    Pq = (O[0] - (y + dy) * math.tan(al), O[1] - y - dy)
    line(c, Pp, Pq, "GREEN", 4)
    line(c, Pp, (Pp[0], Pq[1]), "GREEN", 1.2, dash="3,3")
    line(c, (Pp[0], Pq[1]), Pq, "GREEN", 1.2, dash="3,3")
    lab(c, (Pp[0] + 6, Pp[1] - 14), "dy", "GREEN", "start", 15)
    lab(c, (Pp[0] + 4, Pq[1] - 10), "dy tan α", "GREEN", "start", 14)
    lab(c, (Pp[0] + 6, Pp[1] + 16), "dl", "GREEN", "start", 16)
    nvec = (-math.cos(al), math.sin(al))                # screen components of n_1 = (-cos a, -sin a)
    mid = ((Pp[0] + Pq[0]) / 2, (Pp[1] + Pq[1]) / 2)
    arrow(c, mid, (mid[0] + 70 * nvec[0], mid[1] + 70 * nvec[1]), "BLUE", 2.0, 10)
    lab(c, (mid[0] + 74 * nvec[0] - 4, mid[1] + 74 * nvec[1] + 12), sub("n", "1"), "BLUE", "end", 17)
    sh = (-14 * math.sin(al), -14 * math.cos(al))     # shifted up along the face so the two arrows do not overlap
    arrow(c, (mid[0] + 70 * nvec[0] + sh[0] * 3, mid[1] + 70 * nvec[1] + sh[1] * 3),
          (mid[0] + 4 * nvec[0] + sh[0] * 3, mid[1] + 4 * nvec[1] + sh[1] * 3), "ACC", 2.0, 10)
    lab(c, (mid[0] + 72 * nvec[0] + sh[0] * 3 - 6, mid[1] + 72 * nvec[1] + sh[1] * 3), "−p n₁ dl", "ACC", "end", 14, italic=False)
    arc(c, O, 46, -90, -120, "HEAD", 1.2)
    lab(c, (O[0] - 22, O[1] - 52), "α", "HEAD", "middle", 16)
    line(c, O, (O[0] - 120, O[1]), "EDGE", 1.0)
    arrow(c, (O[0] + 70, O[1]), (O[0] + 130, O[1]), "HEAD", 1.4, 8)
    arrow(c, (O[0] + 70, O[1]), (O[0] + 70, O[1] - 60), "HEAD", 1.4, 8)
    lab(c, (O[0] + 134, O[1] + 5), "x", "HEAD", "start", 16)
    lab(c, (O[0] + 76, O[1] - 60), "y", "HEAD", "start", 16)
    lab(c, (O[0] - 4, O[1] + 20), "O", "HEAD", "middle", 15, italic=False)
    dim(c, (O[0] + 12, O[1]), (O[0] + 12, Pp[1]), "y", "TEXT", (8, 30), "start", 15)
    line(c, Pp, (O[0] + 18, Pp[1]), "EDGE", 0.8, dash="3,3")
    lab(c, (O[0] - 110, O[1] - 70), "l = y / cos α", "GREEN", "end", 15)
    lab(c, (520, 80), sub("n", "1") + " = (−cos α, −sin α)", "BLUE", "start", 15)
    lab(c, (520, 110), "dl = dy / cos α", "GREEN", "start", 15)
    lab(c, (520, 140), sub("p", "1") + " − pₐ = " + sub("ρ", "1") + "g(" + sub("h", "1") + " − y)", "BLUE", "start", 15)
    put("fs7-geometry", c,
        "Left face of the wedge: element dl between heights y and y + dy, the right triangle with legs dy and dy tan alpha, the "
        "unit normal n_1 towards liquid 1, the force -p n_1 dl and the distance l = y / cos alpha from O along the face",
        "Left face of the wedge, making the angle $\\alpha$ with the vertical. The element $dl$ is the hypotenuse of the right "
        "triangle with the vertical leg $dy$ (adjacent to $\\alpha$) and the horizontal leg $dy\\tan\\alpha$ (opposite), so "
        "$dl = dy/\\cos\\alpha$; for the same reason the distance from $O$ along the face is $l = y/\\cos\\alpha$. The unit normal "
        "towards liquid 1 is $\\vec{n}_1 = -\\cos\\alpha\\,\\vec{e}_x - \\sin\\alpha\\,\\vec{e}_y$ and the force on the wedge is "
        "$-p\\vec{n}_1\\,dl$")

    c = Canvas(640, 330)
    O = (320, 300)
    al = math.radians(30)
    Hh = 260
    TL = (O[0] - Hh * math.tan(al), O[1] - Hh)
    TR = (O[0] + Hh * math.tan(al), O[1] - Hh)
    poly(c, [TL, TR, O], "HEAD", 2.0, fill="ACC", close=True, opacity=0.06)
    h1, h2 = 180, 130
    q1 = (O[0] - h1 / 3 * math.tan(al), O[1] - h1 / 3)
    q2 = (O[0] + h2 / 3 * math.tan(al), O[1] - h2 / 3)
    u1 = (math.cos(al), math.sin(al))
    s1 = (q1[0] - 110 * u1[0], q1[1] + 110 * u1[1])
    s2 = (q2[0] + 110 * u1[0], q2[1] + 110 * u1[1])
    arrow(c, s1, q1, "ACC", 3.0, 12)
    lab(c, (s1[0] - 8, s1[1] + 4), sub("F", "1"), "ACC", "end", 18)
    arrow(c, s2, q2, "ACC", 3.0, 12)
    lab(c, (s2[0] + 8, s2[1] + 4), sub("F", "2"), "ACC", "start", 18)
    G = (O[0], O[1] - 2 * Hh / 3)
    dot(c, G, 4, "PINK")
    arrow(c, G, (G[0], G[1] + 70), "PINK", 2.6, 11)
    lab(c, (G[0] + 8, G[1] + 60), "W", "PINK", "start", 17)
    arrow(c, (O[0] + 70, O[1] + 20), (O[0] + 4, O[1] + 2), "PINK", 2.4, 10)
    lab(c, (O[0] + 74, O[1] + 26), "R", "PINK", "start", 17)
    dot(c, O, 4, "HEAD")
    lab(c, (O[0] - 8, O[1] + 20), "O", "HEAD", "end", 15, italic=False)
    lab(c, (O[0] + 170, 70), "green: arms from O along the faces,", "GREEN", "start", 13, italic=False)
    lab(c, (O[0] + 170, 90), sub("h", "1") + "/(3 cos α) and " + sub("h", "2") + "/(3 cos α)", "GREEN", "start", 14)
    line(c, O, q1, "GREEN", 2.0)
    line(c, O, q2, "GREEN", 2.0)
    put("fs7-fbd", c,
        "Free-body diagram of the wedge: forces F_1 and F_2 normal to the two faces at the centres of pressure, a distance "
        "h_i / (3 cos alpha) from O along each face; weight W on the symmetry line; reaction R at the vertex O",
        "Free-body diagram of the wedge (per unit length): $F_1$ and $F_2$ normal to the faces, applied at the centres of "
        "pressure, at the distances $h_1/(3\\cos\\alpha)$ and $h_2/(3\\cos\\alpha)$ from $O$ along the faces; the weight $W$ on "
        "the symmetry line through $O$; the reaction $R$ at $O$")


# ------------------------------------------------------------------------------------------------- FS9
def fs9():
    c = Canvas(560, 320)
    xg, yb = 330, 295
    lt, hp = 120, 50                                     # l and h in screen units
    yh = yb - hp
    ytop = yh - lt
    ysurf = ytop - 80
    liquid(c, [(60, ysurf), (xg, ysurf), (xg, yb), (60, yb)], 0.10)
    floor(c, 50, 480, yb)
    line(c, (60, ysurf), (xg, ysurf), "BLUE", 1.6)
    rect(c, xg - 4, 30, 10, ytop - 30, "HEAD", 1.4, fill="HEAD", opacity=0.6)
    line(c, (xg, ytop), (xg, yb - 2), "ACC", 5)
    dot(c, (xg, yh), 5, "HEAD")
    lab(c, (xg + 14, yh + 5), "hinge", "HEAD", "start", 14, italic=False)
    rect(c, xg + 3, yb - 12, 10, 12, "HEAD", 1.0, fill="HEAD", opacity=0.6)
    lab(c, (200, ysurf + 40), "water", "BLUE", "middle", 14, italic=False)
    lab(c, (430, 120), sub("p", "a"), "HEAD", "middle", 18)
    lab(c, (100, ysurf - 10), sub("p", "a"), "HEAD", "middle", 16)
    dim(c, (xg + 60, ysurf), (xg + 60, ytop), "H", "TEXT", (8, 5), "start", 17)
    line(c, (xg, ysurf), (xg + 66, ysurf), "EDGE", 0.8, dash="3,3")
    line(c, (xg + 6, ytop), (xg + 66, ytop), "EDGE", 0.8, dash="3,3")
    dim(c, (xg - 40, ytop), (xg - 40, yh), "l", "TEXT", (-8, 5), "end", 17)
    dim(c, (xg - 40, yh), (xg - 40, yb), "h", "TEXT", (-8, 5), "end", 17)
    line(c, (xg - 46, yh), (xg, yh), "EDGE", 0.8, dash="3,3")
    line(c, (xg - 46, ytop), (xg, ytop), "EDGE", 0.8, dash="3,3")
    put("fs9-statement", c,
        "Vertical gate below a fixed wall, hinged at a distance l below its top edge and h above the floor, water on the left "
        "with its free surface H above the top edge, air at p_a on both sides",
        "Statement figure (redrawn from fluid_statics_9.pdf, p. 1): gate hinged at a distance $l$ below its top edge and $h < l$ "
        "above the floor; the water surface is $H$ above the top edge; air at $p_a$ on both sides; a stop at the floor on the dry side")

    c = Canvas(640, 330)
    xg, yb = 340, 300
    lt, hp = 160, 70
    yh = yb - hp
    ytop = yh - lt
    k = 0.35
    Hs = 90
    depth = lambda y: Hs + (y - ytop)
    line(c, (xg, ytop), (xg, yb), "ACC", 5)
    for y in range(int(ytop), yb + 1, 18):
        arrow(c, (xg - k * depth(y), y), (xg - 3, y), "BLUE", 1.1, 6)
    poly(c, [(xg, ytop), (xg - k * depth(ytop), ytop), (xg - k * depth(yb), yb), (xg, yb)], "BLUE", 1.2)
    lab(c, (xg - k * depth(ytop) - 6, ytop + 4), "ρg H", "BLUE", "end", 15)
    lab(c, (xg - k * depth(yb) - 6, yb + 4), "ρg(H + l + h)", "BLUE", "end", 15)
    dot(c, (xg, yh), 5, "HEAD")
    lab(c, (xg + 10, yh + 18), "hinge, z = 0", "HEAD", "start", 14, italic=False)
    arrow(c, (xg + 160, yh), (xg + 160, yh - 50), "HEAD", 1.3, 8)
    lab(c, (xg + 166, yh - 44), "z", "HEAD", "start", 16)
    zz = 130
    rect(c, xg + 2, yh - zz - 5, 12, 10, "GREEN", 1.2, fill="GREEN", opacity=0.4)
    lab(c, (xg + 20, yh - zz + 5), "dA = b dz, arm z", "GREEN", "start", 14, italic=False)
    lab(c, (xg + 20, yh - zz + 25), "depth H + l − z", "GREEN", "start", 14, italic=False)
    dim(c, (xg + 200, ytop), (xg + 200, yh), "l", "TEXT", (8, 5), "start", 16)
    dim(c, (xg + 200, yh), (xg + 200, yb), "h", "TEXT", (8, 5), "start", 16)
    line(c, (xg + 6, ytop), (xg + 206, ytop), "EDGE", 0.8, dash="3,3")
    line(c, (xg + 6, yh), (xg + 206, yh), "EDGE", 0.8, dash="3,3")
    arrow(c, (xg + 70, yb - 6), (xg + 6, yb - 6), "PINK", 2.4, 10)
    lab(c, (xg + 74, yb - 2), "stop", "PINK", "start", 14, italic=False)
    arc(c, (xg, yh), 60, -70, -30, "ACC", 1.6, head=True)
    arc(c, (xg, yh), 52, 70, 30, "ACC", 1.6, head=True)
    lab(c, (xg + 66, yh - 36), "opens", "ACC", "start", 13, italic=False)
    lab(c, (xg + 60, yh + 48), "closes", "ACC", "start", 13, italic=False)
    put("fs9-fbd", c,
        "Free-body diagram of the gate: trapezoidal pressure distribution from rho g H at the top edge to rho g (H + l + h) at "
        "the floor, axis z up from the hinge, strip b dz with arm z; the upper part turns the gate open, the lower part against "
        "the stop",
        "Free-body diagram of the gate (width $b$): the gauge pressure grows from $\\rho g H$ at the top edge to "
        "$\\rho g(H + l + h)$ at the floor; with $z$ measured up from the hinge, the strip $b\\,dz$ has depth $H + l - z$ and arm "
        "$z$. The part above the hinge turns the gate open; the part below presses it against the stop")


# ------------------------------------------------------------------------------------------------- FS10
def fs10():
    c = Canvas(600, 260)
    floor(c, 40, 560, 210)
    cx, R = 300, 70
    liquid(c, [(60, 210 - 2 * R), (cx, 210 - 2 * R), (cx, 210), (60, 210)], 0.10)
    liquid(c, [(cx, 210 - R), (540, 210 - R), (540, 210), (cx, 210)], 0.10)
    circle(c, (cx, 210 - R), R, "HEAD", 2.4, fill="ACC", opacity=0.10)
    line(c, (60, 210 - 2 * R), (cx, 210 - 2 * R), "BLUE", 1.6)
    line(c, (cx + R * 0.3, 210 - R), (540, 210 - R), "BLUE", 1.6)
    line(c, (cx - R * 0.7071, 210 - R + R * 0.7071), (cx + R * 0.7071, 210 - R - R * 0.7071), "EDGE", 1.0)
    lab(c, (cx + R + 10, 210 - 2 * R + 14), "D = 1 m", "HEAD", "start", 15, italic=False)
    dim(c, (150, 210 - 2 * R), (150, 210), "1 m", "TEXT", (-8, 5), "end", 15)
    dim(c, (480, 210 - R), (480, 210), "0.5 m", "TEXT", (8, 5), "start", 15)
    lab(c, (300, 245), "cylinder length 5 m (normal to the paper)", "TEXT", "middle", 13, italic=False)
    put("fs10-statement", c,
        "Cylinder of diameter 1 m and length 5 m lying on the floor, water 1 m deep on the left (up to its top) and 0.5 m deep "
        "on the right (up to its centre)",
        "Statement figure (redrawn from fluid_statics_10.pdf, p. 1): cylinder of diameter $D = 1$ m and length 5 m on the floor; "
        "water 1 m deep on the left, up to the top of the cylinder, and 0.5 m deep on the right, up to its centre")

    c = Canvas(720, 320)
    cx, cy, R = 230, 170, 120
    floor(c, 40, 440, cy + R)
    liquid(c, [(40, cy - R), (cx, cy - R), (cx, cy + R), (40, cy + R)], 0.08)
    liquid(c, [(cx, cy), (440, cy), (440, cy + R), (cx, cy + R)], 0.08)
    circle(c, (cx, cy), R, "HEAD", 2.2)
    line(c, (40, cy - R), (cx, cy - R), "BLUE", 1.6)
    line(c, (cx + R, cy), (440, cy), "BLUE", 1.6)
    line(c, (cx, cy - R - 20), (cx, cy + R), "EDGE", 0.9, dash="4,4")
    th = math.radians(55)
    P = (cx - R * math.sin(th), cy - R * math.cos(th))
    line(c, (cx, cy), P, "GREEN", 1.3)
    arc(c, (cx, cy), 36, -90, -90 - 55, "GREEN", 1.3)
    lab(c, (cx - 26, cy - 44), "θ", "GREEN", "middle", 17)
    line(c, P, (P[0], cy), "GREEN", 1.0, dash="3,3")
    line(c, (P[0], cy), (cx, cy), "GREEN", 1.0, dash="3,3")
    lab(c, ((P[0] + cx) / 2, cy + 18), "R sin θ", "GREEN", "middle", 14)
    lab(c, (P[0] - 12, (P[1] + cy) / 2 + 22), "R cos θ", "GREEN", "end", 14)
    nvec = (-math.sin(th), -math.cos(th))
    arrow(c, P, (P[0] + 50 * nvec[0], P[1] + 50 * nvec[1]), "BLUE", 2.0, 10)
    lab(c, (P[0] + 56 * nvec[0] - 4, P[1] + 56 * nvec[1]), "n", "BLUE", "end", 17)
    arrow(c, (P[0] + 60 * nvec[0] + 10, P[1] + 60 * nvec[1] + 40), (P[0] + 4 * nvec[0] + 10, P[1] + 4 * nvec[1] + 40), "ACC", 2.0, 10)
    lab(c, (P[0] + 60 * nvec[0] + 4, P[1] + 60 * nvec[1] + 58), "dF", "ACC", "end", 16)
    lab(c, (cx + 8, cy - 6), "C", "HEAD", "start", 15, italic=False)
    dot(c, (cx, cy), 3.4)
    arrow(c, (60, cy + R), (60, cy + R - 50), "HEAD", 1.3, 8)
    lab(c, (66, cy + R - 44), "y", "HEAD", "start", 16)
    lab(c, (470, 70), "y = R + R cos θ (from the floor)", "GREEN", "start", 14, italic=False)
    lab(c, (470, 95), "depth on the left: 2R − y", "BLUE", "start", 14, italic=False)
    lab(c, (470, 120), sub("n", "x") + " = −sin θ on the left half", "BLUE", "start", 14, italic=False)
    lab(c, (470, 145), sub("n", "x") + " = +sin θ on the right half", "BLUE", "start", 14, italic=False)
    lab(c, (470, 170), "dS = L R dθ", "ACC", "start", 14, italic=False)
    put("fs10-geometry", c,
        "Cylinder section: element on the left half at angle theta from the upward vertical, right triangle with legs R sin theta "
        "and R cos theta, height y = R + R cos theta above the floor, unit normal n towards the water and the force dF",
        "Element of the cylinder at the angle $\\theta$ measured from the upward vertical through the centre $C$. In the right "
        "triangle with hypotenuse $R$, the horizontal leg $R\\sin\\theta$ is opposite to $\\theta$ and the vertical leg "
        "$R\\cos\\theta$ adjacent, so the element is at $y = R + R\\cos\\theta$ above the floor. The unit normal towards the water "
        "on the left half is $\\vec{n} = -\\sin\\theta\\,\\vec{e}_x + \\cos\\theta\\,\\vec{e}_y$ and the area is $dS = LR\\,d\\theta$")


def build(reg, raster):
    global REG
    REG = reg
    for f in (fs1, fs2, fs3, fs4, fs5, fs6, fs7, fs9, fs10):
        f()
