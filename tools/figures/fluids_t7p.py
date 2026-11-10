"""Problem figures of Fluid Mechanics Topic 7 (viscous-flow sheets VF2-VF20; VF10 has no figure).

One statement figure per sheet that has a drawing, redrawn from the sheet (the scans carry the handwritten key next
to it). Registered in the FM-T7 registry of tools/figures/fluids_t7.py; colour code as there (BLUE liquid and
velocities, ACC forces and the unknown, GREEN dimensions, HEAD/TEXT/EDGE lines and labels).
"""
import math

from figures.fluids_t5 import arc
from figures.fluids_t6 import lab, note
from figures.svgkit import Canvas, arrow, circle, dim, dot, hatch, line, pathd, poly, rect, sub

REG = None


def put(name, c, title, caption):
    REG.put(name, c, title, caption)


def liquid(c, pts, op=0.12):
    poly(c, pts, "BLUE", 0, fill="BLUE", close=True, opacity=op)


def ground(c, x0, x1, y, side=-1):
    line(c, (x0, y), (x1, y), "HEAD", 2.4)
    hatch(c, (x0, y + 2), (x1, y + 2), side=side, col="EDGE", step=12)


def axes(c, o, lx="x", ly="y", n=40):
    line(c, o, (o[0] + n, o[1]), "HEAD", 1.2, head=True)
    line(c, o, (o[0], o[1] - n), "HEAD", 1.2, head=True)
    lab(c, (o[0] + n + 4, o[1] + 5), lx, "HEAD", "start", 15)
    lab(c, (o[0] - 6, o[1] - n - 2), ly, "HEAD", "end", 15)


def gravity(c, x, y0=40, y1=100):
    arrow(c, (x, y0), (x, y1), "HEAD", 2.0, 10)
    lab(c, (x + 10, (y0 + y1) / 2 + 6), "g", "HEAD", "start", 18)


# ------------------------------------------------------------------------------------------------- VF2
def vf2():
    c = Canvas(560, 260)
    ground(c, 70, 500, 190)
    liquid(c, [(70, 70), (500, 70), (500, 190), (70, 190)])
    line(c, (70, 70), (500, 70), "BLUE", 2.0)
    lab(c, (285, 52), sub("p", "a"), "HEAD", "middle", 18)
    dim(c, (110, 70), (110, 190), "h", "GREEN", (-16, 6), size=18)
    axes(c, (300, 190), n=46)
    line(c, (220, 228), (380, 228), "ACC", 2.4, head=True)
    line(c, (380, 228), (220, 228), "ACC", 2.4, head=True)
    lab(c, (300, 248), "V cos(ωt)", "ACC", "middle", 17)
    put("vf2-statement", c, "Oscillating wall under a liquid layer",
        "Statement figure (redrawn from VF2_w_solution.pdf, p. 1): a liquid layer of thickness h with a free surface at "
        "p_a on a wall that oscillates with velocity V cos(ωt); y is normal to the wall and x along it")


# ------------------------------------------------------------------------------------------------- VF3
def vf3():
    c = Canvas(600, 290)
    yc, a, b = 150, 95, 48                              # axis, outer radius a, inner radius αa
    for s in (-1, 1):
        line(c, (90, yc + s * a), (540, yc + s * a), "HEAD", 3.6)
    rect(c, 70, yc - b, 490, 2 * b, "HEAD", 1.8, fill="EDGE", opacity=0.12)
    hatch(c, (70, yc - b), (560, yc - b), side=1, col="EDGE", step=10)
    liquid(c, [(90, yc - a), (540, yc - a), (540, yc - b), (90, yc - b)], 0.14)
    liquid(c, [(90, yc + a), (540, yc + a), (540, yc + b), (90, yc + b)], 0.14)
    arrow(c, (440, yc - a - 22), (330, yc - a - 22), "ACC", 3.0, 12)
    lab(c, (385, yc - a - 32), "V", "ACC", "middle", 19)
    dim(c, (572, yc - a), (572, yc + a), "2a", "GREEN", (14, 6), size=16)
    dim(c, (50, yc - b), (50, yc + b), "2αa", "GREEN", (-18, 6), size=16)
    lab(c, (200, yc - b - 14), "ρ, μ", "HEAD", "middle", 17)
    lab(c, (200, yc + b + 36), sub("P", "l"), "ACC", "middle", 17)
    axes(c, (85, 268), "x", "r", 38)
    put("vf3-statement", c, "Annulus with a moving outer cylinder",
        "Statement figure (redrawn from VF3.pdf): liquid of density ρ and viscosity μ between a rod of radius αa and "
        "a cylinder of radius a, along x, driven by the pressure gradient P_l; the outer cylinder moves backward with "
        "velocity V")


# ------------------------------------------------------------------------------------------------- VF4
def vf4():
    c = Canvas(640, 290)
    yc, R = 150, 55
    x0, x1 = 150, 600
    liquid(c, [(60, 90), (x0, 90), (x0, yc - R), (x1, yc - R), (x1, yc + R), (x0, yc + R), (x0, 230), (60, 230)])
    line(c, (x0, yc - R), (x1, yc - R), "HEAD", 3.0)
    line(c, (x0, yc + R), (x1, yc + R), "HEAD", 3.0)
    line(c, (x0, 70), (x0, yc - R), "HEAD", 3.0)
    line(c, (x0, yc + R), (x0, 250), "HEAD", 3.0)
    xb = 430
    rect(c, xb, yc - 24, x1 + 20 - xb, 48, "HEAD", 1.8, fill="EDGE", opacity=0.30)
    hatch(c, (xb, yc - 24), (x1 + 20, yc - 24), side=1, col="EDGE", step=9)
    lab(c, (100, 120), sub("p", "c"), "ACC", "middle", 19)
    lab(c, (xb - 6, yc - R - 34), sub("p", "o"), "ACC", "end", 19)
    line(c, (xb - 4, yc - R - 28), (xb + 6, yc - 28), "ACC", 1.0)
    lab(c, (x1 + 26, yc - 8), sub("p", "a"), "ACC", "start", 19)
    dim(c, (x0 - 22, yc - R), (x0 - 22, yc + R), "D", "GREEN", (-14, 6), size=17)
    dim(c, (xb, 44), (x1, 44), "βL", "GREEN", (0, -8), size=17)
    dim(c, (x0, 258), (x1, 258), "L", "GREEN", (0, 18), size=17)
    dim(c, (x1 - 40, yc - 24), (x1 - 40, yc + 24), "αD", "GREEN", (-22, 5), size=15)
    axes(c, (200, 226), "x", "r", 36)
    put("vf4-statement", c, "Pipe with a partly inserted bar",
        "Statement figure (redrawn from VF4.pdf): a container at p_c discharging through a pipe of diameter D and "
        "length L; a coaxial bar of diameter αD enters from the exit along the last stretch βL; p_o is the pressure "
        "where the bar starts and p_a the exit pressure")


# ------------------------------------------------------------------------------------------------- VF5
def vf5():
    c = Canvas(560, 340)
    xl, xr = 230, 310
    line(c, (xl, 40), (xl, 310), "HEAD", 3.0)
    line(c, (xr, 40), (xr, 310), "HEAD", 3.0)
    liquid(c, [(xl, 70), (xr, 70), (xr, 170), (xl, 170)], 0.12)
    poly(c, [(xl, 170), (xr, 170), (xr, 270), (xl, 270)], "ACC", 0, fill="ACC", close=True, opacity=0.10)
    line(c, (xl, 70), (xr, 70), "BLUE", 1.6)
    line(c, (xl, 170), (xr, 170), "HEAD", 1.4, dash="6,3")
    line(c, (xl, 270), (xr, 270), "HEAD", 1.4, dash="4,4")
    lab(c, (150, 120), sub("ρ", "1") + ", " + sub("μ", "1"), "HEAD", "middle", 17)
    lab(c, (150, 225), sub("ρ", "2") + ", " + sub("μ", "2"), "HEAD", "middle", 17)
    dim(c, (350, 70), (350, 170), sub("l", "1"), "GREEN", (16, 5), size=17)
    dim(c, (350, 170), (350, 270), "h(t)", "GREEN", (22, 5), size=17)
    lab(c, (270, 36), sub("p", "a"), "ACC", "middle", 18)
    lab(c, (300, 336), sub("p", "a"), "ACC", "start", 18)
    lab(c, (222, 190), sub("p", "s"), "ACC", "end", 17)
    dim(c, (xl, 22), (xr, 22), "2a", "GREEN", (0, -6), size=16)
    arrow(c, (430, 60), (430, 130), "HEAD", 2.0, 10)
    lab(c, (442, 100), "g", "HEAD", "start", 18)
    arrow(c, (190, 60), (190, 100), "HEAD", 1.2, 8)
    lab(c, (176, 100), "x", "HEAD", "end", 16)
    arrow(c, (190, 290), (190, 250), "HEAD", 1.2, 8)
    lab(c, (176, 258), "z", "HEAD", "end", 16)
    arrow(c, (270, 316), (270, 336), "BLUE", 1.4, 7)
    put("vf5-statement", c, "Vertical tube with two immiscible liquids",
        "Statement figure (redrawn from VF5.pdf): a vertical tube of radius a, open at both ends once the bottom is "
        "released, with liquid 1 (ρ_1, μ_1) of height l_1 above liquid 2 (ρ_2, μ_2) of height h(t); p_s is the "
        "pressure at the interface")


# ------------------------------------------------------------------------------------------------- VF6
def vf6():
    c = Canvas(560, 340)
    xl, xr = 230, 310
    line(c, (xl, 50), (xl, 260), "HEAD", 3.0)
    line(c, (xr, 50), (xr, 260), "HEAD", 3.0)
    line(c, (xl, 50), (xr, 50), "HEAD", 3.0)
    liquid(c, [(xl, 130), (xr, 130), (xr, 260), (xl, 260)], 0.16)
    line(c, (xl, 130), (xr, 130), "BLUE", 1.8)
    liquid(c, [(150, 260), (390, 260), (390, 300), (150, 300)], 0.12)
    line(c, (150, 260), (390, 260), "BLUE", 1.6)
    lab(c, (150, 252), sub("p", "a"), "ACC", "end", 18)
    lab(c, (270, 92), "p = 0", "HEAD", "middle", 17)
    lab(c, (180, 190), "ρ, μ", "HEAD", "middle", 17)
    dim(c, (350, 130), (350, 260), "h(t)", "GREEN", (22, 5), size=17)
    dim(c, (xl, 32), (xr, 32), "2a", "GREEN", (0, -6), size=16)
    gravity(c, 450, 70, 140)
    arrow(c, (200, 262), (200, 222), "HEAD", 1.2, 8)
    lab(c, (210, 236), "z", "HEAD", "start", 16)
    put("vf6-statement", c, "Oil rising in a vertical tube",
        "Statement figure (redrawn from VF6.pdf): a vertical tube of radius a, closed at the top, with its lower end "
        "in a pool at p_a; the oil column of height h(t) has p = 0 above it; z is the vertical axis from the pool")


# ------------------------------------------------------------------------------------------------- VF7
def vf7():
    c = Canvas(560, 370)
    yb, yt = 310, 50
    xb0, xb1, xt0, xt1 = 270, 290, 200, 360              # narrow bottom, wide top
    line(c, (xb0, yb), (xt0, yt), "HEAD", 3.0)
    line(c, (xb1, yb), (xt1, yt), "HEAD", 3.0)
    ys = 120                                              # free surface
    f = (yb - ys) / (yb - yt)
    liquid(c, [(xb0, yb), (xb0 + (xt0 - xb0) * f, ys), (xb1 + (xt1 - xb1) * f, ys), (xb1, yb)], 0.16)
    line(c, (xb0 + (xt0 - xb0) * f, ys), (xb1 + (xt1 - xb1) * f, ys), "BLUE", 1.8)
    dim(c, (150, yb), (150, yt), "L", "GREEN", (-16, 6), size=18)
    dim(c, (400, yb), (400, ys), "h(t)", "GREEN", (24, 5), size=17)
    lab(c, (280, yb + 28), "2a", "GREEN", "middle", 16)
    lab(c, (280, yt - 12), sub("p", "a"), "ACC", "middle", 18)
    lab(c, (330, yb + 8), sub("p", "a"), "ACC", "start", 17)
    gravity(c, 470, 70, 140)
    arrow(c, (240, yb - 6), (240, yb - 46), "HEAD", 1.2, 8)
    lab(c, (230, yb - 24), "z", "HEAD", "end", 16)
    for y in (yb - 70, yb - 40, yb - 12):
        arrow(c, (280, y), (280, y + 22), "BLUE", 1.3, 7)
    lab(c, (410, 352), "a(z) = a₀(1 + αz/L)", "HEAD", "middle", 15)
    put("vf7-statement", c, "Vertical conical pipe",
        "Statement figure (redrawn from VF7.pdf): a vertical conical pipe of length L, radius a_0 at the lower end "
        "and increasing linearly upward, open at both ends, with the free surface at the height h(t) above the lower end")


# ------------------------------------------------------------------------------------------------- VF8
def vf8():
    c = Canvas(560, 290)
    ground(c, 60, 500, 210)
    rect(c, 190, 80, 180, 112, "HEAD", 2.4, fill="EDGE", opacity=0.12)
    liquid(c, [(190, 192), (370, 192), (370, 210), (190, 210)], 0.30)
    dim(c, (190, 60), (370, 60), "2R", "GREEN", (0, -8), size=18)
    dim(c, (175, 192), (175, 210), "h(t)", "GREEN", (-26, -14), size=16)
    lab(c, (110, 160), sub("P", "o"), "ACC", "middle", 19)
    lab(c, (450, 160), sub("P", "o"), "ACC", "middle", 19)
    arrow(c, (280, 130), (280, 90), "ACC", 3.0, 12)
    lab(c, (292, 112), "ḣ", "ACC", "start", 19)
    arrow(c, (440, 201), (385, 201), "BLUE", 1.4, 7)
    arrow(c, (95, 201), (150, 201), "BLUE", 1.4, 7)
    axes(c, (480, 268), "r", "y", 34)
    put("vf8-statement", c, "Cylinder lifted from an oil film",
        "Statement figure (redrawn from VF8.pdf): a cylindrical body of radius R lifted with velocity ḣ from a "
        "horizontal surface; the oil film of thickness h(t) between them is fed by a radial inflow from the outer "
        "pressure P_o")


# ------------------------------------------------------------------------------------------------- VF9
def vf9():
    c = Canvas(640, 380)
    al = math.radians(20)
    O = (90, 300)
    ux, uy = math.cos(al), -math.sin(al)                  # along the slope
    vx, vy = -math.sin(al), -math.cos(al)                 # normal to the slope, away from the belt

    def T(u, v):
        return (O[0] + u * ux + v * vx, O[1] + u * uy + v * vy)
    L, h = 170, 22
    # fixed upper wall with a step
    wall = [T(0, 2 * h), T(L, 2 * h), T(L, h), T(2 * L, h), T(2 * L, h + 26), T(0, 2 * h + 26)]
    poly(c, wall, "HEAD", 2.0, fill="EDGE", close=True, opacity=0.28)
    liquid(c, [T(0, 0), T(0, 2 * h), T(L, 2 * h), T(L, h), T(2 * L, h), T(2 * L, 0)], 0.20)
    line(c, T(-10, 0), T(2 * L + 10, 0), "HEAD", 3.0)                       # the belt
    for u in (0, 2 * L):
        circle(c, T(u, -9), 9, "HEAD", 1.8)
    for k in range(5):
        a = T(40 + 70 * k, -22)
        arrow(c, a, (a[0] + 26 * ux, a[1] + 26 * uy), "ACC", 2.0, 8)
    lab(c, T(2 * L - 80, -44), "V", "ACC", "middle", 19)
    dim(c, T(L / 2, 0), T(L / 2, 2 * h), "2h", "GREEN", (-20, 4), size=15)
    dim(c, T(1.5 * L, 0), T(1.5 * L, h), "h", "GREEN", (-16, 4), size=15)
    line(c, T(0, -94), T(L, -94), "GREEN", 1.1, head=True)
    line(c, T(L, -94), T(0, -94), "GREEN", 1.1, head=True)
    lab(c, T(L / 2, -108), "L", "GREEN", "middle", 17)
    line(c, T(L, -94), T(2 * L, -94), "GREEN", 1.1, head=True)
    line(c, T(2 * L, -94), T(L, -94), "GREEN", 1.1, head=True)
    lab(c, T(1.5 * L, -108), "L", "GREEN", "middle", 17)
    arc(c, O, 52, 0, -20, "HEAD", 1.3)
    lab(c, (O[0] + 62, O[1] - 8), "α", "HEAD", "start", 17)
    line(c, O, (O[0] + 90, O[1]), "EDGE", 0.8, dash="4,4")
    lab(c, (T(L, 2 * h + 40)[0], T(L, 2 * h + 40)[1]), sub("p", "0"), "ACC", "middle", 17)
    lab(c, (O[0] - 30, O[1] - 30), sub("p", "a"), "ACC", "middle", 18)
    lab(c, (T(2 * L, 2 * h + 6)[0] + 24, T(2 * L, h)[1] - 36), sub("p", "a"), "ACC", "middle", 18)
    gravity(c, 560, 40, 110)
    a1 = T(-40, 2 * h + 56)
    line(c, a1, (a1[0] + 34 * ux, a1[1] + 34 * uy), "HEAD", 1.2, head=True)
    lab(c, (a1[0] + 38 * ux, a1[1] + 38 * uy + 14), "x", "HEAD", "start", 15)
    line(c, a1, (a1[0] + 34 * vx, a1[1] + 34 * vy), "HEAD", 1.2, head=True)
    lab(c, (a1[0] + 38 * vx - 8, a1[1] + 38 * vy), "y", "HEAD", "end", 15)
    put("vf9-statement", c, "Conveyor belt pumping up an incline",
        "Statement figure (redrawn from VF9.pdf): an inclined channel at the angle α between the conveyor belt, which "
        "moves up the slope with velocity V, and a fixed wall with a step (gap 2h over a length L, then h over a "
        "length L); both ends are at p_a and p_0 is the pressure at the step")


# ------------------------------------------------------------------------------------------------- VF11
def vf11():
    c = Canvas(600, 280)
    ground(c, 60, 560, 220)
    line(c, (120, 130), (500, 130), "HEAD", 4.0)
    line(c, (120, 130), (120, 220), "HEAD", 4.0)
    liquid(c, [(120, 130), (500, 130), (500, 220), (120, 220)], 0.16)
    dot(c, (500, 130), 5, "HEAD")
    lab(c, (516, 116), "A", "HEAD", "start", 18)
    arrow(c, (330, 192), (230, 192), "ACC", 3.0, 12)
    lab(c, (280, 184), "V", "ACC", "middle", 19)
    arrow(c, (500, 100), (560, 100), "ACC", 2.4, 11)
    lab(c, (535, 86), sub("F", "x"), "ACC", "middle", 18)
    dim(c, (120, 60), (500, 60), "L", "GREEN", (0, -8), size=18)
    dim(c, (90, 130), (90, 220), "h", "GREEN", (-14, 6), size=18)
    lab(c, (96, 100), sub("p", "a"), "ACC", "end", 18)
    lab(c, (556, 168), sub("p", "a"), "ACC", "end", 18)
    lab(c, (150, 178), sub("p", "o"), "ACC", "start", 17)
    axes(c, (560, 262), "x", "y", 26)
    put("vf11-statement", c, "Windshield wiper",
        "Statement figure (redrawn from VF11.pdf): an L-shaped arm whose horizontal bar of length L is at a height h "
        "above the wall and whose vertical leg closes the channel at x = 0; the wall moves with velocity V towards "
        "−x in the frame of the arm, F_x acts at A and p_o is the pressure at x = 0")


# ------------------------------------------------------------------------------------------------- VF12
def vf12():
    c = Canvas(640, 360)
    C = (330, 175)
    Rb, R, e = 150, 128, 14
    O = (C[0] - e, C[1])
    circle(c, C, Rb, "HEAD", 3.0, fill="BLUE", opacity=0.10)
    circle(c, O, R, "HEAD", 2.2, fill="EDGE", opacity=0.12)
    line(c, O, (C[0] + Rb + 20, O[1]), "EDGE", 0.9, dash="4,4")
    th = math.radians(55)
    P1 = (O[0] + R * math.cos(th), O[1] - R * math.sin(th))
    # casing point along the ray from O (solve |O + t d - C| = Rb)
    dx, dy = math.cos(th), -math.sin(th)
    bx, by = O[0] - C[0], O[1] - C[1]
    b = bx * dx + by * dy
    t = -b + math.sqrt(b * b - (bx * bx + by * by - Rb * Rb))
    P2 = (O[0] + t * dx, O[1] + t * dy)
    line(c, O, P2, "HEAD", 1.2)
    line(c, P1, P2, "ACC", 3.0)
    lab(c, (P2[0] + 8, P2[1] - 6), "h", "ACC", "start", 18)
    lab(c, ((O[0] + P1[0]) / 2 - 12, (O[1] + P1[1]) / 2 + 12), "R", "HEAD", "end", 17)
    arc(c, O, 36, 0, -55, "HEAD", 1.3)
    lab(c, (O[0] + 46, O[1] - 18), "θ", "HEAD", "start", 17)
    dim(c, (O[0], C[1] + 30), (C[0], C[1] + 30), "e", "GREEN", (0, 20), size=16)
    line(c, (O[0], C[1] + 22), (O[0], C[1] + 38), "EDGE", 0.8)
    line(c, (C[0], C[1] + 22), (C[0], C[1] + 38), "EDGE", 0.8)
    dot(c, O, 3, "HEAD")
    dot(c, C, 3, "HEAD")
    lab(c, (O[0] - 8, O[1] - 6), "O", "HEAD", "end", 15, italic=False)
    lab(c, (C[0] + 8, C[1] - 6), "C", "HEAD", "start", 15, italic=False)
    arc(c, O, 70, -150, -210, "ACC", 2.4, head=True)
    lab(c, (O[0] - 94, O[1] - 20), "ω", "ACC", "middle", 19)
    lab(c, (C[0] + Rb + 10, C[1] + 20), sub("R", "b"), "HEAD", "start", 17)
    lab(c, (O[0] + R * math.cos(math.radians(27)) + 14, O[1] - R * math.sin(math.radians(27)) + 8), "x = Rθ", "HEAD",
        "start", 15)
    put("vf12-statement", c, "Journal bearing",
        "Statement figure (redrawn from VF12.pdf): a shaft of radius R rotating with ω inside a fixed casing of "
        "radius R_b, their centres O and C a distance e apart; θ is measured from the line of centres, h(θ) is the "
        "gap, x = Rθ the arc along the shaft and y the distance across the gap, from the shaft to the casing")


# ------------------------------------------------------------------------------------------------- VF13
def vf13():
    c = Canvas(600, 280)
    O = (90, 220)
    ground(c, 40, 540, 220)
    al = math.radians(10)
    Pend = (O[0] + 400 * math.cos(al), O[1] - 400 * math.sin(al))
    line(c, O, Pend, "HEAD", 5.0)
    liquid(c, [O, Pend, (Pend[0], 220)], 0.20)
    arc(c, O, 90, 0, -10, "HEAD", 1.3)
    lab(c, (O[0] + 100, O[1] - 7), "α", "HEAD", "start", 17)
    xs = 330
    hs = 220 - (O[1] - (xs - O[0]) * math.tan(al))
    line(c, (xs, 220), (xs, 220 - (xs - O[0]) * math.tan(al)), "GREEN", 1.6, head=True)
    line(c, (xs, 220 - (xs - O[0]) * math.tan(al)), (xs, 220), "GREEN", 1.6, head=True)
    lab(c, (xs + 8, 202), "h(x, t)", "GREEN", "start", 16)
    lab(c, (330, 148), "L", "GREEN", "middle", 18)
    arc(c, O, 26, 330, 200, "ACC", 2.4, head=True)
    lab(c, (O[0] - 16, O[1] - 36), "M", "ACC", "end", 19)
    arc(c, O, 140, -14, -46, "ACC", 2.2, head=True)
    lab(c, (O[0] + 150, O[1] - 98), "ω", "ACC", "start", 19)
    lab(c, (Pend[0] + 20, 190), sub("P", "∞"), "ACC", "start", 19)
    axes(c, (24, 246), "x", "y", 26)
    dot(c, O, 4, "HEAD")
    lab(c, (O[0] - 6, O[1] + 18), "O", "HEAD", "end", 15, italic=False)
    put("vf13-statement", c, "Plate rotating over a wall",
        "Statement figure (redrawn from VF13.pdf): a plate of length L hinged at O on a horizontal wall, rotating "
        "with ω = dα/dt under the torque M; the gap is h(x, t) = αx and the surrounding liquid is at P_∞")


# ------------------------------------------------------------------------------------------------- VF14
def vf14():
    c = Canvas(600, 280)
    ground(c, 60, 560, 215)
    yb = 160
    line(c, (120, yb), (500, yb), "HEAD", 4.0)
    line(c, (120, yb), (120, 215), "HEAD", 4.0)
    liquid(c, [(120, yb), (500, yb), (500, 215), (120, 215)], 0.18)
    dot(c, (500, yb), 5, "HEAD")
    lab(c, (512, yb - 12), "A", "HEAD", "start", 18)
    arrow(c, (310, yb - 54), (310, yb - 12), "ACC", 3.0, 12)
    lab(c, (322, yb - 34), "ḣ", "ACC", "start", 19)
    dim(c, (120, 60), (500, 60), "L", "GREEN", (0, -8), size=18)
    dim(c, (90, yb), (90, 215), "h(t)", "GREEN", (-22, 5), size=17)
    lab(c, (556, 190), sub("P", "∞"), "ACC", "end", 19)
    lab(c, (150, 192), sub("P", "o"), "ACC", "start", 17)
    axes(c, (540, 262), "x", "y", 28)
    put("vf14-statement", c, "Arm approaching a wall",
        "Statement figure (redrawn from VF14.pdf): an L-shaped arm whose horizontal bar of length L is at the height "
        "h(t) above a wall and whose vertical leg closes the channel at x = 0; A is the end of the bar and P_∞ the "
        "pressure outside; P_o is the pressure at x = 0")


# ------------------------------------------------------------------------------------------------- VF15
def vf15():
    c = Canvas(680, 300)
    for yc, name in ((95, "u"), (195, "l")):
        rect(c, 150, yc - 20, 330, 40, "HEAD", 1.8, rx=20)
        circle(c, (170, yc), 16, "HEAD", 1.2)
        circle(c, (460, yc), 16, "HEAD", 1.2)
    arrow(c, (280, 124), (330, 124), "BLUE", 1.8, 9)
    lab(c, (338, 129), sub("V", "u"), "BLUE", "start", 16)
    arrow(c, (280, 166), (330, 166), "BLUE", 1.8, 9)
    lab(c, (338, 171), sub("V", "l"), "BLUE", "start", 16)
    arrow(c, (330, 76), (280, 76), "EDGE", 1.2, 8)
    arrow(c, (330, 214), (280, 214), "EDGE", 1.2, 8)
    dim(c, (400, 115), (400, 175), "h", "GREEN", (14, 6), size=16)
    line(c, (130, 28), (130, 262), "HEAD", 1.4)
    line(c, (500, 28), (500, 262), "HEAD", 1.4)
    dim(c, (150, 258), (480, 258), "L", "GREEN", (0, 20), size=16)
    lab(c, (70, 150), sub("P", "0"), "ACC", "middle", 17)
    lab(c, (594, 150), sub("P", "0") + " + ΔP", "ACC", "middle", 17)
    lab(c, (70, 60), "ρ, μ", "HEAD", "middle", 16)
    axes(c, (560, 250), "x", "y", 30)
    put("vf15-statement", c, "Two-belt viscous pump",
        "Statement figure (redrawn from VF15.pdf): two parallel belts of length L, a distance h apart, whose facing "
        "strands move at V_u and V_l and drag liquid of density ρ and viscosity μ from a reservoir at P_0 to one at "
        "P_0 + ΔP")


# ------------------------------------------------------------------------------------------------- VF16
def vf16():
    c = Canvas(620, 360)
    xl, xr, yb = 120, 520, 290
    xm = (xl + xr) / 2
    hole = 22                                              # αR in pixels
    line(c, (xl, 60), (xl, yb), "HEAD", 3.4)
    line(c, (xr, 60), (xr, yb), "HEAD", 3.4)
    line(c, (xl, yb), (xm - hole, yb), "HEAD", 3.4)
    line(c, (xm + hole, yb), (xr, yb), "HEAD", 3.4)
    pathd(c, f"M{xm - hole},{yb} C{xm - hole},{yb + 24} {xm - hole},{yb + 34} {xm - hole - 8},{yb + 50}", "HEAD", 2.4)
    pathd(c, f"M{xm + hole},{yb} C{xm + hole},{yb + 24} {xm + hole},{yb + 34} {xm + hole + 8},{yb + 50}", "HEAD", 2.4)
    yp = 150
    liquid(c, [(xl, yp + 24), (xr, yp + 24), (xr, yb), (xm + hole, yb), (xm - hole, yb), (xl, yb)], 0.14)
    rect(c, xl, yp, xr - xl, 24, "HEAD", 2.0, fill="EDGE", opacity=0.45)
    arrow(c, (xm, yp - 52), (xm, yp - 6), "HEAD", 3.0, 13)
    lab(c, (xm + 12, yp - 28), "W", "HEAD", "start", 19)
    lab(c, (xl + 20, yp - 40), sub("p", "a"), "ACC", "start", 18)
    lab(c, (xm + 50, yb + 52), sub("p", "a"), "ACC", "start", 18)
    dim(c, (xl, 76), (xm, 76), "R", "GREEN", (0, -8), size=18)
    dim(c, (xm, yb - 14), (xm + hole, yb - 14), "αR", "GREEN", (14, 24), size=14)
    dim(c, (xr + 24, yb), (xr + 24, yp + 24), "h(t)", "GREEN", (28, 5), size=17)
    line(c, (xm, 40), (xm, yb + 60), "EDGE", 0.9, dash="8,4,2,4")
    arrow(c, (xm - 60, yb - 60), (xm - 26, yb - 14), "BLUE", 1.5, 7)
    arrow(c, (xm + 60, yb - 60), (xm + 26, yb - 14), "BLUE", 1.5, 7)
    gravity(c, 580, 60, 130)
    put("vf16-statement", c, "Piston over a liquid layer with a central hole",
        "Statement figure (redrawn from VF16.pdf): a piston of weight W and radius R at the height h(t) above the "
        "bottom of a container; the liquid below it leaves through a central hole of radius αR at the pressure p_a "
        "(axisymmetric section, r radial and z vertical)")


# ------------------------------------------------------------------------------------------------- VF17
def vf17():
    c = Canvas(680, 300)
    yc, h = 150, 90
    line(c, (30, yc - h), (650, yc - h), "HEAD", 3.2)
    line(c, (30, yc + h), (650, yc + h), "HEAD", 3.2)
    for yy in (yc - h - 16, yc + h + 16):
        arrow(c, (50, yy), (120, yy), "ACC", 2.4, 11)
        lab(c, (135, yy + 5), "U", "ACC", "start", 17)
    xa, xb = 210, 470
    line(c, (xa, yc), (xb, yc), "HEAD", 5.0)
    for y in (yc - 66, yc - 44, yc - 22, yc + 22, yc + 44, yc + 66):
        pass
    for s in (-1, 1):
        for k in range(1, 9):
            y = k * h / 9.0
            v = 60 * (y / h) * (4 - 3 * y / h) / 1.33
            arrow(c, (xa + 40, yc + s * y), (xa + 40 + v, yc + s * y), "BLUE", 1.0, 6)
        pts = [(xa + 40 + 60 * (y / h) * (4 - 3 * y / h) / 1.33, yc + s * y) for y in [h * i / 30 for i in range(31)]]
        pathd(c, "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts), "BLUE", 1.8)
    for yy in (yc - 40, yc - 14, yc + 14, yc + 40):
        arrow(c, (40, yy), (100, yy), "BLUE", 1.4, 8)
        arrow(c, (590, yy), (650, yy), "BLUE", 1.4, 8)
    lab(c, (150, yc - 4), sub("P", "−∞"), "ACC", "middle", 16)
    lab(c, (150, yc + 16), sub("T", "−∞"), "ACC", "middle", 16)
    lab(c, (540, yc - 4), sub("P", "∞"), "ACC", "middle", 16)
    lab(c, (540, yc + 16), sub("T", "∞"), "ACC", "middle", 16)
    dim(c, (xa, 278), (xb, 278), "L", "GREEN", (0, 18), size=17)
    line(c, (xa, 262), (xa, 286), "EDGE", 0.8, dash="4,3")
    line(c, (xb, 262), (xb, 286), "EDGE", 0.8, dash="4,3")
    dim(c, (xb + 40, yc), (xb + 40, yc - h), "h", "GREEN", (14, 5), size=16)
    dim(c, (xb + 40, yc), (xb + 40, yc + h), "h", "GREEN", (14, 5), size=16)
    line(c, (xa, yc), (xa, yc - 40), "HEAD", 1.0, head=True)
    lab(c, (xa - 6, yc - 42), "y", "HEAD", "end", 15)
    lab(c, (xa - 14, yc + 18), "x = 0", "HEAD", "end", 14)
    put("vf17-statement", c, "Thin plate in a Couette channel",
        "Statement figure (redrawn from VF17.pdf): a channel between two walls at y = ±h moving with velocity U, "
        "with a thin plate of length L on the centre line from x = 0 to x = L; the liquid far upstream and "
        "downstream moves with U at the pressures and temperatures P_{−∞}, T_{−∞} and P_∞, T_∞; the sketched "
        "profiles are those found in the solution")


# ------------------------------------------------------------------------------------------------- VF18
def vf18():
    c = Canvas(560, 360)
    ys, xw, xp = 200, 150, 190                            # free surface level, wall x, plate x
    liquid(c, [(xw, 60), (xp, 60), (xp, 280), (xw, 280)], 0.0)
    liquid(c, [(xw, 90), (xp, 90), (xp, 280), (xw, 280)], 0.22)
    liquid(c, [(xp, ys), (480, ys), (480, 320), (xw, 320), (xw, 280), (xp, 280)], 0.14)
    line(c, (xp, ys), (480, ys), "BLUE", 1.8)
    line(c, (xw, 40), (xw, 320), "HEAD", 5.0)
    line(c, (xp, 40), (xp, 280), "HEAD", 2.4)
    line(c, (xw, 320), (480, 320), "HEAD", 3.0)
    line(c, (480, ys - 20), (480, 320), "HEAD", 3.0)
    arrow(c, (100, 250), (100, 150), "ACC", 3.0, 13)
    lab(c, (88, 205), "V", "ACC", "end", 19)
    dim(c, (xw, 56), (xp, 56), "d", "GREEN", (0, -8), size=16)
    dim(c, (300, ys), (300, 280), "H", "GREEN", (18, 5), size=17)
    dim(c, (232, ys), (232, 90), "h(t)", "GREEN", (28, 5), size=17)
    lab(c, (170, 78), sub("p", "a"), "ACC", "middle", 16)
    lab(c, (400, ys - 10), sub("p", "a"), "ACC", "middle", 17)
    line(c, (xp + 6, ys + 100), (xp + 6, ys + 60), "HEAD", 1.2, head=True)
    lab(c, (xp + 16, ys + 70), "z", "HEAD", "start", 15)
    gravity(c, 520, 50, 120)
    put("vf18-statement", c, "Liquid dragged into a gap by a moving wall",
        "Statement figure (redrawn from VF18.pdf, panel t > 0): a vertical wall that moves up with velocity V and a "
        "fixed plate at the distance d, with its lower end at the depth H below the free surface; the gap is "
        "filled with liquid up to the height h(t) above the free surface; p_a acts on the free surface and on the "
        "top of the column")


# ------------------------------------------------------------------------------------------------- VF19
def vf19():
    c = Canvas(600, 420)
    xm = 300
    r2, r1 = 46, 22
    poly(c, [(60, 340), (540, 340), (540, 400), (60, 400)], "HEAD", 1.6, fill="BLUE", close=True, opacity=0.14)
    poly(c, [(60, 40), (540, 40), (540, 100), (60, 100)], "HEAD", 1.6, fill="BLUE", close=True, opacity=0.14)
    line(c, (60, 340), (540, 340), "BLUE", 1.8)
    line(c, (60, 100), (540, 100), "HEAD", 1.6)
    for s in (-1, 1):
        line(c, (xm + s * r2, 100), (xm + s * r2, 340), "HEAD", 3.0)
    liquid(c, [(xm - r2, 100), (xm + r2, 100), (xm + r2, 340), (xm - r2, 340)], 0.18)
    rect(c, xm - r1, 30, 2 * r1, 380, "HEAD", 2.0, fill="EDGE", opacity=0.35)
    arrow(c, (xm + 80, 260), (xm + 80, 200), "ACC", 3.4, 13)
    lab(c, (xm + 92, 232), "U", "ACC", "start", 19)
    dim(c, (xm - 120, 340), (xm - 120, 100), "L", "GREEN", (-16, 6), size=18)
    dim(c, (90, 100), (90, 40), "H", "GREEN", (-16, 6), size=17)
    lab(c, (110, 330), sub("p", "a"), "ACC", "middle", 17)
    lab(c, (130, 64), sub("p", "a"), "ACC", "middle", 17)
    lab(c, (xm + r2 + 10, 150), "2R₂", "GREEN", "start", 15)
    lab(c, (xm - 8, 215), "2R₁", "GREEN", "end", 15)
    gravity(c, 540, 150, 230)
    line(c, (xm + 160, 330), (xm + 160, 290), "HEAD", 1.2, head=True)
    lab(c, (xm + 170, 300), "z", "HEAD", "start", 15)
    line(c, (xm + 160, 330), (xm + 200, 330), "HEAD", 1.2, head=True)
    lab(c, (xm + 204, 335), "r", "HEAD", "start", 15)
    put("vf19-statement", c, "Viscous pump with a moving rod",
        "Statement figure (redrawn from VF19.pdf): a reservoir at p_a, a vertical pipe of radius R_2 and length L up "
        "to the bottom of an open container of depth H, and a coaxial rod of radius R_1 moving up with velocity U "
        "inside the pipe; z is vertical and r radial")


# ------------------------------------------------------------------------------------------------- VF20
def vf20():
    c = Canvas(620, 360)
    yb = 280
    line(c, (40, yb), (580, yb), "HEAD", 3.0)
    hatch(c, (40, yb + 2), (580, yb + 2), side=-1, col="EDGE", step=12)
    s = 110                                               # R in pixels
    xc, hh = 310, 22
    poly(c, [(xc - s, yb - hh), (xc + s, yb - hh), (xc + s, yb - hh - 2 * s), (xc - s, yb - hh - 2 * s)], "HEAD", 2.4,
         fill="ACC", close=True, opacity=0.18)
    lab(c, (xc, yb - hh - s + 6), sub("ρ", "s"), "HEAD", "middle", 22)
    dim(c, (xc - s, 36), (xc + s, 36), "2R", "GREEN", (0, -8), size=18)
    dim(c, (xc + s + 24, yb - hh), (xc + s + 24, yb - hh - 2 * s), "2R", "GREEN", (28, 6), size=18)
    dim(c, (xc - s - 24, yb), (xc - s - 24, yb - hh), "h", "GREEN", (-16, 5), size=17)
    pathd(c, f"M{xc - 8},{yb} L{xc - 8},{yb + 50}", "HEAD", 2.4)
    pathd(c, f"M{xc + 8},{yb} L{xc + 8},{yb + 50}", "HEAD", 2.4)
    arrow(c, (xc, yb + 48), (xc, yb - 14), "BLUE", 3.0, 12)
    lab(c, (xc + 16, yb + 40), "Q", "BLUE", "start", 19)
    for k in range(3):
        arrow(c, (xc + 20 + 24 * k, yb - hh / 2 - 1), (xc + 56 + 24 * k, yb - hh / 2 - 1), "BLUE", 1.2, 6)
        arrow(c, (xc - 20 - 24 * k, yb - hh / 2 - 1), (xc - 56 - 24 * k, yb - hh / 2 - 1), "BLUE", 1.2, 6)
    lab(c, (90, 150), "ρ, μ", "HEAD", "middle", 18)
    lab(c, (90, 180), sub("P", "0"), "ACC", "middle", 18)
    lab(c, (550, 230), sub("P", "0"), "ACC", "middle", 18)
    gravity(c, 560, 60, 130)
    line(c, (80, yb - 6), (80, yb - 46), "HEAD", 1.2, head=True)
    lab(c, (70, yb - 30), "z", "HEAD", "end", 15)
    line(c, (80, yb - 6), (120, yb - 6), "HEAD", 1.2, head=True)
    lab(c, (124, yb - 2), "r", "HEAD", "start", 15)
    put("vf20-statement", c, "Cylinder levitated by a jet",
        "Statement figure (redrawn from VF20.pdf): a cylinder of radius R, height 2R and density ρ_s hovering at the "
        "height h above the bottom of a tank of liquid (ρ, μ, pressure P_0 far away) on a jet of flow rate Q "
        "injected at the centre of its base; z is vertical and r radial")


def build(reg, raster):
    global REG
    REG = reg
    for f in (vf2, vf3, vf4, vf5, vf6, vf7, vf8, vf9, vf11, vf12, vf13, vf14, vf15, vf16, vf17, vf18, vf19, vf20):
        f()
