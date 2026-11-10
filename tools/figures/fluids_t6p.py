"""Problem figures of Fluid Mechanics Topic 6 (dimensional analysis sheets DA1-DA14).

One statement figure per sheet that has a drawing, redrawn from the sheet (the scans carry the handwritten key next
to it); DA5 redraws the measured curve W1(n1) with the points read in the key; DA8 keeps the photograph of the robotic
wings as a crop of the sheet. Registered in the FM-T6 registry of tools/figures/fluids_t6.py; colour code as there
(BLUE fluid and velocities, ACC forces, power and the unknown, GREEN geometry, HEAD/TEXT/EDGE lines and labels).
"""
import math

from figures.fluids_t5 import arc, water_surface
from figures.fluids_t6 import lab, note
from figures.svgkit import Canvas, arrow, circle, dim, dot, hatch, line, pathd, poly, rect, sub

REG = None


def put(name, c, title, caption):
    REG.put(name, c, title, caption)


def liquid(c, pts, op=0.10):
    poly(c, pts, "BLUE", 0, fill="BLUE", close=True, opacity=op)


def floor(c, x0, x1, y):
    line(c, (x0, y), (x1, y), "EDGE", 2.0)
    hatch(c, (x1, y), (x0, y), side=1, col="EDGE", step=12)


# ------------------------------------------------------------------------------------------------- DA2
def da2():
    c = Canvas(640, 240)
    for y in (70, 120, 170):
        arrow(c, (40, y), (130, y), "BLUE", 1.8, 10)
    lab(c, (85, 58), "U", "BLUE", "middle", 19)
    lab(c, (85, 200), "ρ, μ", "HEAD", "middle", 17)
    C, R = (250, 120), 50
    circle(c, C, R, "HEAD", 2.2, fill="EDGE", opacity=0.10)
    line(c, (C[0] - R, C[1]), (C[0] + R, C[1]), "GREEN", 1.2, head=True)
    line(c, (C[0] + R, C[1]), (C[0] - R, C[1]), "GREEN", 1.2, head=True)
    lab(c, (C[0], C[1] - 8), "2R", "GREEN", "middle", 16)
    # alternate vortices of opposite circulation
    for x, y, ccw in ((360, 70, False), (470, 70, False), (410, 170, True), (530, 170, True)):
        arc(c, (x, y), 18, 180, 450 if not ccw else -90, "BLUE", 1.6)
    lab(c, (450, 225), "vortices shed alternately from the top and the bottom, U > " + sub("U", "c"), "TEXT", "middle", 13,
        italic=False)
    put("da2-statement", c, "Wind over a circular wire",
        "Statement figure (redrawn from DA2.pdf): a wind stream of velocity U, density ρ and viscosity μ over a "
        "wire of radius R; above the critical velocity the wake becomes a periodic street of vortices of "
        "opposite circulation")


# ------------------------------------------------------------------------------------------------- DA3
def da3():
    c = Canvas(560, 340)
    x0, x1, top, bot = 140, 420, 50, 300
    yl = 110                                         # tar level
    liquid(c, [(x0, yl), (x1, yl), (x1, bot), (x0, bot)], 0.16)
    line(c, (x0, top), (x0, bot), "HEAD", 2.4)
    line(c, (x1, top), (x1, bot), "HEAD", 2.4)
    line(c, (x0, bot), (x1, bot), "HEAD", 2.4)
    line(c, (x0, yl), (x1, yl), "BLUE", 1.8)
    lab(c, ((x0 + x1) / 2 - 60, yl + 26), "p = " + sub("p", "a"), "HEAD", "middle", 15)
    lab(c, ((x0 + x1) / 2 + 70, 200), "tar: " + sub("ρ", "t") + ", " + sub("ν", "t"), "HEAD", "middle", 15)
    # shaft and three-blade stirrer at the bottom (side view: two blades seen)
    xc = (x0 + x1) / 2
    line(c, (xc, top - 10), (xc, bot - 30), "HEAD", 2.0)
    rect(c, xc - 70, bot - 30, 140, 24, "ACC", 1.8, fill="ACC", opacity=0.25)
    dim(c, (x1 + 22, bot - 30), (x1 + 22, bot - 6), "h", "GREEN", (14, 6), size=16)
    line(c, (xc + 70, bot - 30), (x1 + 30, bot - 30), "GREEN", 0.8, dash="3,3")
    line(c, (xc + 70, bot - 6), (x1 + 30, bot - 6), "GREEN", 0.8, dash="3,3")
    dim(c, (x0, top - 12), (x1, top - 12), "D", "GREEN", (0, -8), size=16)
    arc(c, (xc, top + 12), 22, 200, 340, "ACC", 1.8, head=True)
    lab(c, (xc + 30, top + 6), "Ω", "ACC", "start", 18)
    arrow(c, (500, 90), (500, 160), "HEAD", 2.0, 10)
    lab(c, (512, 135), "g", "HEAD", "start", 18)
    note(c, (280, 330), "volume V of tar; 3-blade stirrer of height h at the bottom", "TEXT", "middle", 13)
    put("da3-statement", c, "Tar tank with a bottom stirrer",
        "Statement figure (redrawn from DA3.pdf, section view): a container of diameter D holding a volume V of tar, "
        "free surface at p_a, with a 3-blade stirrer of height h at its bottom rotating at Ω; gravity g downward")


# ------------------------------------------------------------------------------------------------- DA5
DA5_POINTS = ((125, 4.0), (150, 5.5), (175, 6.5), (200, 7.0), (225, 6.0), (250, 4.5))


def da5():
    c = Canvas(560, 330)
    X = lambda n: 90 + (n - 112.5) * 3.0
    Y = lambda w: 280 - (w - 3.5) * 60
    line(c, (X(112.5), Y(3.5)), (X(262), Y(3.5)), "HEAD", 1.4, head=True)
    line(c, (X(112.5), Y(3.5)), (X(112.5), Y(7.7)), "HEAD", 1.4, head=True)
    for n in (125, 150, 175, 200, 225, 250):
        line(c, (X(n), Y(3.5)), (X(n), Y(7.2)), "EDGE", 0.6, dash="2,4")
        note(c, (X(n), Y(3.5) + 18), str(n), "TEXT", "middle", 13)
    for w in (4, 5, 6, 7):
        line(c, (X(112.5), Y(w)), (X(255), Y(w)), "EDGE", 0.6, dash="2,4")
        note(c, (X(112.5) - 10, Y(w) + 5), str(w), "TEXT", "end", 13)
    pts = [(X(n), Y(w)) for n, w in DA5_POINTS]
    poly(c, pts, "ACC", 2.4)
    for p in pts:
        dot(c, p, 3.4, "ACC")
    lab(c, (X(262), Y(3.5) + 34), sub("n", "1") + " (rpm)", "HEAD", "end", 16)
    lab(c, (X(112.5) + 8, Y(7.7) + 4), sub("W", "1") + " (kW)", "HEAD", "start", 16)
    note(c, (280, 325), "D = 5 m, U = 10 m/s; points as read in the key", "TEXT", "middle", 13)
    put("da5-statement", c, "Measured power of the wind turbine",
        "Statement figure (redrawn from DA5.pdf): power W_1 delivered by the turbine of diameter D = 5 m against its "
        "angular velocity n_1 for a wind of U = 10 m/s; the dots are the values read in the official key "
        "(4, 5.5, 6.5, 7, 6 and 4.5 kW at 125 to 250 rpm), a reading of the plot")


# ------------------------------------------------------------------------------------------------- DA6
def da6():
    c = Canvas(680, 300)
    base = 170
    # sea bed and coast
    pathd(c, "M40,250 L380,250 C470,248 540,200 560,170 L660,170", "EDGE", 1.8)
    # still water and the wave
    pathd(c, "M40,170 L120,170 C170,170 190,60 250,60 C300,58 300,96 282,100 C300,140 330,170 380,170 L555,170",
          "BLUE", 2.0)
    liquid(c, [(40, 170), (120, 170), (180, 100), (250, 62), (290, 100), (330, 160), (380, 170), (555, 170),
               (540, 200), (470, 248), (380, 250), (40, 250)], 0.10)
    line(c, (120, 62), (120, 170), "GREEN", 1.2, head=True)
    line(c, (120, 170), (120, 62), "GREEN", 1.2, head=True)
    line(c, (112, 62), (250, 62), "GREEN", 0.8, dash="4,4")
    lab(c, (110, 122), "h", "GREEN", "end", 18)
    arrow(c, (320, 90), (390, 90), "ACC", 3.0, 12)
    lab(c, (355, 78), "U", "ACC", "middle", 18)
    # wall
    poly(c, [(560, 170), (585, 80), (625, 80), (625, 170)], "HEAD", 2.0, fill="EDGE", close=True, opacity=0.15)
    dim(c, (645, 80), (645, 170), "H", "GREEN", (14, 6), size=18)
    arrow(c, (440, 30), (440, 70), "HEAD", 2.0, 10)
    lab(c, (452, 56), "g", "HEAD", "start", 18)
    note(c, (340, 290), "tsunami of height h and velocity U against a coastal wall of height H", "TEXT", "middle", 13)
    put("da6-statement", c, "Tsunami against a protection wall",
        "Statement figure (redrawn from DA6.pdf): a tsunami of height h travelling with velocity U towards a coastal "
        "protection wall of height H; the unknowns are U and the impact force per unit width of wall F")


# ------------------------------------------------------------------------------------------------- DA7
def da7():
    c = Canvas(660, 300)
    pathd(c, "M160,50 C360,58 520,95 600,130", "HEAD", 2.4)
    pathd(c, "M160,250 C360,242 520,205 600,170", "HEAD", 2.4)
    line(c, (600, 130), (600, 170), "GREEN", 1.0, dash="3,3")
    line(c, (160, 50), (160, 250), "GREEN", 1.0, dash="3,3")
    lab(c, (160, 40), sub("A", "e"), "GREEN", "middle", 17)
    lab(c, (606, 122), sub("A", "s"), "GREEN", "start", 17)
    for y, bend in ((95, 30), (150, 0), (205, -30)):
        pathd(c, f"M40,{y - bend * 2} C90,{y - bend} 120,{y} 175,{y}", "BLUE", 1.4)
        arrow(c, (165, y), (180, y), "BLUE", 1.4, 8)
    for y in (140, 150, 160):
        arrow(c, (600, y), (650, y), "BLUE", 1.4, 8)
    line(c, (40, 150), (650, 150), "EDGE", 0.8, dash="8,4,2,4")
    # fan
    c.add('<ellipse cx="330" cy="150" rx="8" ry="58" fill="none" stroke="HEAD" stroke-width="1.8"/>')
    lab(c, (345, 108), "Ẇ", "ACC", "start", 18)
    arrow(c, (470, 150), (420, 150), "ACC", 3.0, 12)
    lab(c, (446, 138), "E", "ACC", "middle", 18)
    lab(c, (90, 235), "ρ, μ", "HEAD", "middle", 17)
    note(c, (330, 292), "nozzle with a fan of power Ẇ; thrust E with the submarine at rest", "TEXT", "middle", 13)
    put("da7-statement", c, "Shrouded fan of a submarine",
        "Statement figure (redrawn from DA7.pdf): a nozzle of inlet area A_e and outlet area A_s with a fan inside "
        "that gives the power Ẇ to water of density ρ and viscosity μ; E is the thrust")


# ------------------------------------------------------------------------------------------------- DA10
def da10():
    c = Canvas(680, 300)
    for yc, v, lbl in ((95, -1, "u"), (195, 1, "l")):
        r = 20
        rect(c, 150, yc - r, 330, 2 * r, "HEAD", 1.8, rx=r)
        circle(c, (170, yc), r - 4, "HEAD", 1.2)
        circle(c, (460, yc), r - 4, "HEAD", 1.2)
    # belt faces in contact with the liquid move to the right (towards the high-pressure reservoir)
    arrow(c, (280, 124), (330, 124), "BLUE", 1.8, 9)
    lab(c, (338, 129), sub("V", "u"), "BLUE", "start", 16)
    arrow(c, (280, 166), (330, 166), "BLUE", 1.8, 9)
    lab(c, (338, 171), sub("V", "l"), "BLUE", "start", 16)
    arrow(c, (330, 86), (280, 86), "EDGE", 1.2, 8)
    arrow(c, (330, 204), (280, 204), "EDGE", 1.2, 8)
    dim(c, (400, 115), (400, 175), "h", "GREEN", (14, 6), size=16)
    line(c, (130, 30), (130, 270), "HEAD", 1.4)
    line(c, (500, 30), (500, 270), "HEAD", 1.4)
    dim(c, (150, 260), (480, 260), "L", "GREEN", (0, 20), size=16)
    lab(c, (70, 152), sub("P", "0"), "HEAD", "middle", 17)
    lab(c, (590, 152), sub("P", "0") + " + ΔP", "HEAD", "middle", 17)
    lab(c, (70, 60), "ρ, μ", "HEAD", "middle", 16)
    put("da10-statement", c, "Two-belt viscous pump",
        "Statement figure (redrawn from DA10.pdf): two parallel belts of length L, a distance h ≪ L apart, driven at "
        "V_u and V_l, drag liquid of density ρ and viscosity μ from a reservoir at reduced pressure P_0 to one at "
        "P_0 + ΔP")


# ------------------------------------------------------------------------------------------------- DA11
def da11():
    c = Canvas(680, 400)
    # top: undisturbed pool
    floor(c, 60, 470, 170)
    liquid(c, [(60, 80), (440, 80), (440, 170), (60, 170)])
    line(c, (60, 80), (440, 80), "BLUE", 2.0)
    rect(c, 440, 50, 12, 120, "HEAD", 1.6, fill="EDGE", opacity=0.6)
    rect(c, 452, 100, 50, 12, "HEAD", 1.6, fill="EDGE", opacity=0.6)
    dim(c, (300, 80), (300, 170), "H", "GREEN", (14, 6), size=17)
    lab(c, (130, 130), "ρ, μ", "HEAD", "middle", 17)
    arrow(c, (40, 20), (40, 70), "HEAD", 2.0, 10)
    lab(c, (52, 50), "g", "HEAD", "start", 18)
    # bottom: moving wall generating waves
    floor(c, 60, 470, 370)
    pathd(c, "M60,275 C130,265 160,315 230,312 C300,310 330,262 410,262", "BLUE", 2.0)
    liquid(c, [(60, 275), (230, 312), (410, 262), (410, 370), (60, 370)])
    rect(c, 410, 255, 12, 115, "HEAD", 1.6, fill="EDGE", opacity=0.6)
    rect(c, 422, 305, 50, 12, "HEAD", 1.6, fill="EDGE", opacity=0.6)
    line(c, (380, 232), (470, 232), "HEAD", 1.2, head=True)
    line(c, (470, 232), (380, 232), "HEAD", 1.2, head=True)
    lab(c, (425, 222), "x = A cos(2πωt)", "HEAD", "middle", 15)
    arrow(c, (220, 240), (160, 240), "ACC", 3.0, 12)
    lab(c, (190, 228), "V", "ACC", "middle", 17)
    arrow(c, (560, 311), (485, 311), "ACC", 3.0, 12)
    lab(c, (540, 300), "Ẇ", "ACC", "middle", 18)
    put("da11-statement", c, "Wave generator in a pool",
        "Statement figure (redrawn from DA11.pdf): above, the pool of liquid (ρ, μ) of undisturbed depth H; below, "
        "the lateral wall moved harmonically, x = A cos(2πωt), by the power Ẇ, generating gravity waves")


# ------------------------------------------------------------------------------------------------- DA12
def da12():
    c = Canvas(660, 280)
    # missile
    poly(c, [(300, 140), (330, 115), (520, 115), (520, 165), (330, 165)], "HEAD", 2.0, fill="EDGE", close=True,
         opacity=0.12)
    poly(c, [(470, 115), (520, 80), (540, 80), (520, 115)], "HEAD", 1.6, close=True)
    poly(c, [(470, 165), (520, 200), (540, 200), (520, 165)], "HEAD", 1.6, close=True)
    dim(c, (345, 115), (345, 165), "D", "GREEN", (14, 6), size=16)
    # bow shock
    pathd(c, "M430,20 C300,60 250,110 250,140 C250,170 300,220 430,260", "ACC", 2.2)
    lab(c, (440, 30), "bow shock", "ACC", "start", 14, italic=False)
    line(c, (250, 185), (300, 185), "GREEN", 1.2, head=True)
    line(c, (300, 185), (250, 185), "GREEN", 1.2, head=True)
    lab(c, (275, 205), "d", "GREEN", "middle", 17)
    arrow(c, (70, 140), (160, 140), "BLUE", 2.4, 11)
    lab(c, (115, 128), "U", "BLUE", "middle", 18)
    lab(c, (115, 90), "ρ, μ", "HEAD", "middle", 17)
    lab(c, (115, 175), "c", "HEAD", "middle", 17)
    arrow(c, (610, 30), (610, 80), "HEAD", 2.0, 10)
    lab(c, (622, 60), "g", "HEAD", "start", 18)
    put("da12-statement", c, "Supersonic missile with its bow shock",
        "Statement figure (redrawn from DA12.pdf, frame of the missile): a gas of density ρ, viscosity μ and sound "
        "speed c meets the missile of diameter D at a speed U > c; a bow shock stands at a distance d ahead of the tip")


# ------------------------------------------------------------------------------------------------- DA13
def da13():
    c = Canvas(460, 360)
    C = (230, 150)
    pathd(c, f"M{C[0] - 120},{C[1]} A120,110 0 0 1 {C[0] + 120},{C[1]}", "HEAD", 2.4, fill="EDGE", opacity=0.10)
    line(c, (C[0] - 120, C[1]), (C[0] + 120, C[1]), "HEAD", 2.4)
    m = (230, 310)
    for x in (C[0] - 120, C[0] - 50, C[0], C[0] + 50, C[0] + 120):
        line(c, (x, C[1]), m, "HEAD", 1.0)
    dot(c, m, 10, "HEAD")
    lab(c, (m[0] + 18, m[1] + 6), "m", "HEAD", "start", 20)
    dim(c, (C[0] - 120, 28), (C[0] + 120, 28), "D", "GREEN", (0, -8), size=18)
    arrow(c, (60, 190), (60, 260), "HEAD", 2.0, 10)
    lab(c, (72, 236), "g", "HEAD", "start", 19)
    arrow(c, (380, 250), (380, 320), "BLUE", 2.2, 10)
    lab(c, (392, 290), "V", "BLUE", "start", 19)
    put("da13-statement", c, "Module descending under a parachute",
        "Statement figure (redrawn from DA13.pdf): a module of mass m hangs from a parachute of diameter D and falls "
        "at its terminal velocity V under gravity g")


# ------------------------------------------------------------------------------------------------- DA14
def da14():
    c = Canvas(440, 360)
    C, R = (210, 180), 140
    circle(c, C, R, "HEAD", 3.0, fill="BLUE", opacity=0.08)
    line(c, C, (C[0] + R, C[1]), "HEAD", 1.2)
    lab(c, (C[0] + 70, C[1] + 20), "R", "GREEN", "middle", 17)
    th = math.radians(35)
    P = (C[0] + 95 * math.cos(th), C[1] - 95 * math.sin(th))
    line(c, C, P, "HEAD", 1.2)
    lab(c, (C[0] + 30, C[1] - 32), "r", "HEAD", "middle", 16)
    arc(c, C, 34, -35, 0, "HEAD", 1.2)
    lab(c, (C[0] + 44, C[1] - 6), "θ", "HEAD", "start", 16)
    lab(c, (C[0] - 50, C[1] - 50), "ρ, μ", "HEAD", "middle", 18)
    arc(c, C, R + 14, 15, -40, "ACC", 2.0, head=True)
    lab(c, (C[0] + R + 26, C[1] - 40), "Ω", "ACC", "start", 19)
    lab(c, (C[0] + 95, C[1] - R + 4), sub("T", "0"), "HEAD", "middle", 17)
    put("da14-statement", c, "Circular cavity inside a rotating case",
        "Statement figure (redrawn from DA14.pdf): a circular cavity of radius R full of liquid (ρ, μ), initially at "
        "rest, inside a case at temperature T_0 that is set to rotate at Ω at t = 0⁺")


def build(reg, raster):
    global REG
    REG = reg
    for f in (da2, da3, da5, da6, da7, da10, da11, da12, da13, da14):
        f()
    reg.raster("da8-statement", "Robotic fly wings in mineral oil",
               "Photograph of the sheet (crop of DA8.pdf): the pair of robotic wings of Dickinson's facility, "
               "which flap in a tank of mineral oil", width=660)
