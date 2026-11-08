"""Figures of the solved problems of Topic 6 (electrical properties), Aerospace Materials I.

Every plotted line or bar is computed here from the same numbers as the solution of its problem
(Problems T6andT7_Electric and Magnetic Properties.pdf, problems 1-10 and the data of Session 13).
`problems(REG)` is called by `figures.materials_t6.build()`; it adds the figures to the registry of the topic.
"""
import math

from figures.svgkit import (Canvas, arrow, circle, dot, line, pathd, poly, rect, sub, text)

K_B = 8.62e-5            # eV/K (the sheet)
Q = 1.602e-19            # C


class M:
    """Data coordinates mapped to pixels: the origin is at (x0, y0), sx and sy are pixels per unit, y points up."""

    def __init__(self, x0, y0, sx, sy):
        self.x0, self.y0, self.sx, self.sy = x0, y0, sx, sy

    def p(self, x, y):
        return (self.x0 + x * self.sx, self.y0 - y * self.sy)


def axes(c, m, xmin, xmax, ymax, xlabel, ylabel, xt=(), yt=(), xl_dy=40):
    """Axes with the origin of the data frame at the pixel origin; ticks are (value, label) pairs."""
    line(c, m.p(xmin, 0), m.p(xmax, 0), "EDGE", 1.3, head=True)
    line(c, m.p(xmin, 0), m.p(xmin, ymax), "EDGE", 1.3, head=True)
    for v, s in xt:
        x, y = m.p(v, 0)
        line(c, (x, y), (x, y + 5), "EDGE", 1.1)
        text(c, (x, y + 19), s, "TEXT", "middle", 12)
    for v, s in yt:
        x, y = m.p(xmin, v)
        line(c, (x - 5, y), (x, y), "EDGE", 1.1)
        text(c, (x - 8, y + 4), s, "TEXT", "end", 12)
    x, y = m.p(xmax, 0)
    text(c, (x, y + xl_dy), xlabel, "HEAD", "end", 13, "700")
    x, y = m.p(xmin, ymax)
    text(c, (x + 8, y + 4), ylabel, "HEAD", "start", 13, "700")


def badge(c, x, y, n, col="GREEN"):
    circle(c, (x, y), 10, col, 1.8, fill=col, opacity=0.18)
    text(c, (x, y + 4.5), str(n), col, "middle", 13, "700")


# ---------------------------------------------------------------- problem 1
def p1():
    rho_al = lambda t: 2.70 * (1 + 0.0039 * t)           # 1e-6 ohm cm
    rho_ag = lambda t: 1.47 * (1 + 0.0038 * t)
    r45 = rho_al(45)
    t_ag = (r45 - 1.47) / (1.47 * 0.0038)
    c = Canvas(640, 340)
    m = M(80, 280, 1.35, 55)
    axes(c, m, 0, 380, 4.1, "T (°C)", "ρ (10⁻⁶ Ω·cm)",
         [(0, "0"), (100, "100"), (200, "200"), (300, "300")], [(1, "1"), (2, "2"), (3, "3"), (4, "4")])
    poly(c, [m.p(t, rho_al(t)) for t in range(0, 101, 5)], "BLUE", 2.6)
    poly(c, [m.p(t, rho_ag(t)) for t in range(0, 381, 10)], "PINK", 2.6)
    # guides: Al at 45 C, level rho_Al(45), silver at t_ag
    line(c, m.p(45, 0), m.p(45, r45), "EDGE", 1.2, "4,4")
    line(c, m.p(45, r45), m.p(t_ag, r45), "GREEN", 1.6, "6,4")
    line(c, m.p(t_ag, r45), m.p(t_ag, 0), "EDGE", 1.2, "4,4")
    dot(c, m.p(45, r45), 5, "BLUE", "BLUE")
    dot(c, m.p(t_ag, r45), 5, "PINK", "PINK")
    text(c, m.p(45, 0), "45", "BLUE", "middle", 12, "700", dy=34)
    text(c, m.p(t_ag, 0), f"{t_ag:.1f}", "PINK", "middle", 12, "700", dy=34)
    text(c, (m.p(45, r45)[0] + 12, m.p(45, r45)[1] + 24), f"ρ(Al, 45 °C) = {r45:.3f}", "BLUE", "start", 12, "700")
    text(c, (m.p(t_ag, r45)[0] + 2, m.p(t_ag, r45)[1] - 12), "same ρ in Ag", "PINK", "middle", 12, "700")
    # legend
    lx, ly = 372, 205
    line(c, (lx, ly), (lx + 26, ly), "BLUE", 2.6)
    text(c, (lx + 34, ly + 4), "Al: ρ = 2.70 (1 + 0.0039 T)", "TEXT", "start", 12)
    line(c, (lx, ly + 24), (lx + 26, ly + 24), "PINK", 2.6)
    text(c, (lx + 34, ly + 28), "Ag: ρ = 1.47 (1 + 0.0038 T)", "TEXT", "start", 12)
    REG.put("t6-p1-resistivity-lines", c, "Resistivity of silver and aluminium against temperature",
            f"Problem 1: ρ = ρ0 (1 + αT) for Al and Ag; the Al wire at 45 °C has ρ = {r45:.3f}×10⁻⁶ Ω·cm and silver reaches it at {t_ag:.1f} °C")


# ---------------------------------------------------------------- problem 2
def p2():
    c = Canvas(640, 360)
    ox, oy = 320, 190
    line(c, (80, oy), (570, oy), "EDGE", 1.3, head=True)
    line(c, (ox, 340), (ox, 28), "EDGE", 1.3, head=True)
    text(c, (572, oy + 22), "conductivity σ", "HEAD", "end", 13, "700")
    text(c, (80, oy + 22), "decreases", "TEXT", "start", 12)
    text(c, (570, oy + 38), "increases", "TEXT", "end", 12)
    text(c, (ox + 10, 40), "tensile strength", "HEAD", "start", 13, "700")
    text(c, (ox - 10, 52), "increases", "TEXT", "end", 12)
    text(c, (ox - 10, 328), "decreases", "TEXT", "end", 12)
    rect(c, ox, 28, 250, 162, "GREEN", 1.2, "5,4", "GREEN", 0.07)
    text(c, (ox + 244, 56), "both improve", "GREEN", "end", 12, "700")
    # (label, dx, dy, colour, label offset): directions of the key
    items = [("a", -120, -52, "PINK", (-12, -2)), ("b", 150, -105, "GREEN", (12, -4)), ("c", 105, 85, "BLUE", (12, 12)),
             ("d", -125, -105, "PINK", (-12, -4)), ("e", -35, -110, "PINK", (-12, -2))]
    for lab, dx, dy, col, off in items:
        arrow(c, (ox, oy), (ox + dx, oy + dy), col, 2.6, 11)
        text(c, (ox + dx + off[0], oy + dy + off[1] + 4), lab, col, "end" if off[0] < 0 else "start", 16, "700")
    dot(c, (ox, oy), 4, "HEAD", "HEAD")
    notes = [("a  alloying with Cu", "PINK"), ("b  lower working temperature", "GREEN"), ("c  larger grains", "BLUE"),
             ("d  intermetallic precipitates", "PINK"), ("e  cold work", "PINK")]
    for i, (s, col) in enumerate(notes):
        text(c, (80, 262 + 18 * i), s, col, "start", 12, "700")
    REG.put("t6-p2-strategies", c, "Effect of five strategies on conductivity and strength",
            "Problem 2: direction of the change of conductivity (horizontal) and tensile strength (vertical) for the five strategies a to e (arrows are schematic, not to scale)")


# ---------------------------------------------------------------- problem 3
def p3():
    c = Canvas(640, 330)
    # metal lattice
    sp, r = 36, 12
    x0, y0 = 40, 70
    vac = (2, 1)
    for i in range(5):
        for j in range(4):
            p = (x0 + i * sp, y0 + j * sp)
            if (i, j) == vac:
                circle(c, p, r, "EDGE", 1.4, "4,3")
            else:
                circle(c, p, r, "ACC", 1.6, fill="ACC", opacity=0.30)
    # electron path scattered by the vacancy
    pts = [(10, 200), (60, 188), (100, 150), (118, 112), (150, 100), (180, 126), (205, 160), (240, 170), (262, 150)]
    poly(c, pts, "BLUE", 1.8)
    arrow(c, pts[-2], pts[-1], "BLUE", 1.8, 9)
    dot(c, pts[0], 4, "BLUE", "BLUE")
    text(c, (x0 + 2 * sp, 40), "metal", "HEAD", "middle", 15, "700")
    text(c, (x0 + 2 * sp, 232), "free electrons scatter", "BLUE", "middle", 12)
    text(c, (x0 + 2 * sp, 248), "at the vacancy: σ falls", "BLUE", "middle", 12)
    text(c, (x0 + 2 * sp, 290), "vacancy, disorder, solute, heat: ρ up", "TEXT", "middle", 12)
    line(c, (320, 30), (320, 310), "EDGE", 1.0, "5,5")
    # ionic lattice
    x1, y1 = 370, 70
    for i in range(5):
        for j in range(4):
            p = (x1 + i * sp, y1 + j * sp)
            cation = (i + j) % 2 == 0
            if (i, j) == (2, 2):
                circle(c, p, 9, "EDGE", 1.4, "4,3")        # cation vacancy
            elif cation:
                circle(c, p, 9, "BLUE", 1.8, fill="BLUE", opacity=0.30)
            else:
                circle(c, p, 13, "PINK", 1.8, fill="PINK", opacity=0.25)
    # a cation (1, 1) hops diagonally into the cation vacancy (2, 2)
    a, b = (x1 + 1 * sp, y1 + 1 * sp), (x1 + 2 * sp, y1 + 2 * sp)
    arrow(c, (a[0] + 11, a[1] + 11), (b[0] - 11, b[1] - 11), "GREEN", 2.4, 11)
    # interstitial cation in the void between (0,2), (1,2), (0,3), (1,3)
    ip = (x1 + 0.5 * sp, y1 + 2.5 * sp)
    circle(c, ip, 6, "GREEN", 1.8, fill="GREEN", opacity=0.55)
    text(c, (x1 + 2 * sp, 40), "ionic ceramic", "HEAD", "middle", 15, "700")
    text(c, (x1 + 2 * sp, 236), "ions hop into vacancies and", "GREEN", "middle", 12)
    text(c, (x1 + 2 * sp, 252), "interstitial voids: σ rises", "GREEN", "middle", 12)
    text(c, (x1 + 2 * sp, 290), "vacancy, disorder, heat, doping: σ up", "TEXT", "middle", 12)
    # legend
    circle(c, (352, 312), 9, "BLUE", 1.6, fill="BLUE", opacity=0.30)
    text(c, (366, 316), "cation", "TEXT", "start", 12)
    circle(c, (418, 312), 12, "PINK", 1.6, fill="PINK", opacity=0.25)
    text(c, (436, 316), "anion", "TEXT", "start", 12)
    circle(c, (484, 312), 9, "EDGE", 1.4, "4,3")
    text(c, (498, 316), "vacancy", "TEXT", "start", 12)
    circle(c, (556, 312), 6, "GREEN", 1.8, fill="GREEN", opacity=0.55)
    text(c, (568, 316), "interstitial", "TEXT", "start", 12)
    REG.put("t6-p3-ionic-metal", c, "Metallic and ionic conduction with defects",
            "Problem 3: in a metal the electrons scatter at a vacancy; in an ionic ceramic the cations hop into vacancies and move through interstitial voids (schematic)")


# ---------------------------------------------------------------- problem 4
def p4():
    c = Canvas(640, 330)
    a = 0.67 / (2 * K_B)                                   # Eg/2k in K for Ge
    metal = lambda t: (1 + 0.0039 * 25) / (1 + 0.0039 * t)              # sigma / sigma(25 C), Cu
    semi = lambda t: math.exp(a * (1 / 298.15 - 1 / (t + 273.15)))       # sigma / sigma(25 C), Ge
    ts = list(range(0, 201, 5))
    # left panel
    m1 = M(60, 270, 1.35, 150)
    axes(c, m1, 0, 215, 1.5, "T (°C)", "σ / σ(25 °C)", [(0, "0"), (100, "100"), (200, "200")],
         [(0.5, "0.5"), (1.0, "1.0")], xl_dy=34)
    poly(c, [m1.p(t, metal(t)) for t in ts], "BLUE", 2.6)
    for t in (25, 75):
        dot(c, m1.p(t, metal(t)), 4, "BLUE", "BLUE")
    text(c, (m1.p(75, metal(75))[0] + 8, m1.p(75, metal(75))[1] - 10), f"{metal(75):.3f} at 75 °C", "BLUE", "start", 12, "700")
    text(c, (150, 14), "metal (Cu): ρ = ρ0 (1 + αT)", "HEAD", "middle", 13, "700")
    text(c, (150, 30), "σ decreases", "BLUE", "middle", 12)
    # right panel
    m2 = M(380, 270, 1.35, 1.65)
    axes(c, m2, 0, 215, 140, "T (°C)", "σ / σ(25 °C)", [(0, "0"), (100, "100"), (200, "200")],
         [(50, "50"), (100, "100")], xl_dy=34)
    poly(c, [m2.p(t, semi(t)) for t in ts], "PINK", 2.6)
    for t in (25, 75):
        dot(c, m2.p(t, semi(t)), 4, "PINK", "PINK")
    text(c, (m2.p(75, semi(75))[0] + 10, m2.p(75, semi(75))[1] - 14), f"{semi(75):.2f} at 75 °C", "PINK", "start", 12, "700")
    text(c, (470, 14), "intrinsic Ge: σ ∝ exp(−Eg / 2kT)", "HEAD", "middle", 13, "700")
    text(c, (470, 30), "σ increases", "PINK", "middle", 12)
    REG.put("t6-p4-sigma-temperature", c, "Conductivity against temperature for a metal and an intrinsic semiconductor",
            "Problem 4: relative conductivity of copper (ρ = ρ0(1 + αT), α = 0.0039 °C⁻¹) and of intrinsic germanium (Eg = 0.67 eV) against temperature, each divided by its value at 25 °C")


# ---------------------------------------------------------------- problem 5
def p5():
    c = Canvas(640, 340)
    cw, ch = 74, 46
    x0, y0 = 80, 60
    cols = [("13", "3 valence e⁻", ["B", "Al", "Ga", "In"]), ("14", "4 valence e⁻", ["C", "Si", "Ge", "Sn"]),
            ("15", "5 valence e⁻", ["N", "P", "As", "Sb"])]
    host = {"Si", "Ge"}
    donor = {"Sb", "As"}
    accept = {"Ga"}
    for ci, (g, ve, els) in enumerate(cols):
        x = x0 + ci * (cw + 12)
        text(c, (x + cw / 2, y0 - 26), f"group {g}", "HEAD", "middle", 13, "700")
        text(c, (x + cw / 2, y0 - 10), ve, "TEXT", "middle", 11)
        for ri, el in enumerate(els):
            y = y0 + ri * (ch + 8)
            col, op, w = "EDGE", None, 1.2
            if el in host:
                col, op, w = "GREEN", 0.22, 2.0
            elif el in donor:
                col, op, w = "PINK", 0.25, 2.2
            elif el in accept:
                col, op, w = "BLUE", 0.25, 2.2
            rect(c, x, y, cw, ch, col, w, None, col if op else "none", op, 6)
            text(c, (x + cw / 2, y + ch / 2 + 6), el, "HEAD" if op else "TEXT", "middle", 18, "700" if op else "400")
    # explanations
    tx = 372
    rect(c, tx, 62, 240, 66, "PINK", 1.4, None, "PINK", 0.08, 6)
    text(c, (tx + 12, 84), "Sb, As: 5 valence e⁻ (group 15)", "PINK", "start", 13, "700")
    text(c, (tx + 12, 102), "one more than Si: donors, n-type", "TEXT", "start", 12)
    text(c, (tx + 12, 118), "(a) Si + Sb, (b) Si + As", "TEXT", "start", 12)
    rect(c, tx, 144, 240, 54, "BLUE", 1.4, None, "BLUE", 0.08, 6)
    text(c, (tx + 12, 166), "Ga: 3 valence e⁻ (group 13)", "BLUE", "start", 13, "700")
    text(c, (tx + 12, 184), "one less: acceptor, p-type: (c) Si + Ga", "TEXT", "start", 12)
    rect(c, tx, 214, 240, 54, "GREEN", 1.4, None, "GREEN", 0.08, 6)
    text(c, (tx + 12, 236), "Si, Ge: 4 valence e⁻ (group 14)", "GREEN", "start", 13, "700")
    text(c, (tx + 12, 254), "the host lattices of the problem", "TEXT", "start", 12)
    REG.put("t6-p5-doping-groups", c, "Groups 13, 14 and 15 of the periodic table",
            "Problem 5: the valence electrons of the dopants (groups 15 and 13) against the 4 of the silicon or germanium host (group 14) decide donor or acceptor behaviour")


# ---------------------------------------------------------------- problem 6
def p6():
    c = Canvas(640, 300)
    bx, by, bw, bh = 60, 100, 440, 110
    rect(c, bx, by, bw, bh, "HEAD", 2.0, None, "GREEN", 0.07, 4)
    # Si lattice (small circles) with three P atoms
    pa = {(2, 1), (6, 2), (9, 0)}
    for i in range(12):
        for j in range(3):
            p = (bx + 30 + i * 34, by + 22 + j * 34)
            if (i, j) in pa:
                circle(c, p, 9, "PINK", 1.8, fill="PINK", opacity=0.35)
                text(c, (p[0], p[1] + 4), "P", "HEAD", "middle", 10, "700")
                dot(c, (p[0] + 15, p[1] - 11), 3.5, "BLUE", "BLUE")
            else:
                circle(c, p, 9, "EDGE", 1.2, fill="EDGE", opacity=0.20)
    text(c, (bx + 6, by + bh + 20), "Si bar, n-type: n = 10²³ m⁻³ free electrons (one per P)", "TEXT", "start", 12)
    # field and currents
    arrow(c, (bx + 40, by - 34), (bx + 190, by - 34), "ACC", 2.4, 11)
    text(c, (bx + 40, by - 42), "E", "ACC", "start", 15, "700")
    arrow(c, (bx + 400, by - 34), (bx + 250, by - 34), "BLUE", 2.4, 11)
    text(c, (bx + 400, by - 42), sub("v", "d") + " (electrons)", "BLUE", "end", 13, "700")
    arrow(c, (bx + 40, by + bh + 44), (bx + 190, by + bh + 44), "GREEN", 2.4, 11)
    text(c, (bx + 200, by + bh + 49), "J = n q μe E", "GREEN", "start", 14, "700")
    # data box
    text(c, (520, 112), "μe = 0.14", "TEXT", "start", 12)
    text(c, (520, 128), "m²/(V·s)", "TEXT", "start", 12)
    text(c, (520, 152), "q = 1.602×10⁻¹⁹ C", "TEXT", "start", 12)
    text(c, (520, 184), "σ = n q μe", "HEAD", "start", 13, "700")
    REG.put("t6-p6-n-type-bar", c, "Phosphorus-doped silicon bar",
            "Problem 6: n-type silicon with 10²³ m⁻³ conduction electrons from P donors; the field E drives the electrons against E, so the current density J points along E (schematic)")


# ---------------------------------------------------------------- problem 7
def p7():
    s1, s2 = 2.22, 2.22 * math.exp(0.67 / (2 * K_B) * (1 / 298.15 - 1 / 348.15))
    a = 0.67 / (2 * K_B) / 1000                             # slope magnitude per 1e-3 K^-1
    x1, x2 = 1000 / 298.15, 1000 / 348.15
    y1, y2 = math.log(s1), math.log(s2)
    c = Canvas(640, 340)
    m = M(80, 290, 270, 62)                                  # x from 2.6 to 3.6 -> shift
    P = lambda x, y: (80 + (x - 2.6) * 480, 290 - (y - 0) * 62)
    line(c, (80, 290), (600, 290), "EDGE", 1.3, head=True)
    line(c, (80, 290), (80, 30), "EDGE", 1.3, head=True)
    for v in (2.8, 3.0, 3.2, 3.4):
        x = P(v, 0)[0]
        line(c, (x, 290), (x, 295), "EDGE", 1.1)
        text(c, (x, 309), f"{v:.1f}", "TEXT", "middle", 12)
    for v in (0, 1, 2, 3, 4):
        y = P(2.6, v)[1]
        line(c, (75, y), (80, y), "EDGE", 1.1)
        text(c, (70, y + 4), str(v), "TEXT", "end", 12)
    text(c, (600, 330), "1/T (10⁻³ K⁻¹)", "HEAD", "end", 13, "700")
    text(c, (88, 40), "ln σ  (σ in Ω⁻¹ m⁻¹)", "HEAD", "start", 13, "700")
    xs = [2.65, 3.45]
    poly(c, [P(x, y1 - a * (x - x1)) for x in xs], "PINK", 2.6)
    for (x, y, lab, dx) in ((x1, y1, "25 °C: σ = 2.22", -10), (x2, y2, "75 °C: σ = %.1f" % s2, 10)):
        dot(c, P(x, y), 5, "BLUE", "BLUE")
        line(c, P(x, y), P(x, 0), "EDGE", 1.1, "4,4")
        line(c, P(x, y), P(2.6, y), "EDGE", 1.1, "4,4")
    text(c, (P(x1, y1)[0] + 12, P(x1, y1)[1] - 12), "25 °C: σ = 2.22", "BLUE", "start", 12, "700")
    text(c, (P(x2, y2)[0] - 12, P(x2, y2)[1] + 22), "75 °C: σ = %.1f" % s2, "BLUE", "end", 12, "700")
    # slope triangle
    line(c, P(x2, y2), P(x1, y2), "GREEN", 1.8)
    line(c, P(x1, y2), P(x1, y1), "GREEN", 1.8)
    text(c, ((P(x2, y2)[0] + P(x1, y2)[0]) / 2, P(x2, y2)[1] - 8), "Δ(1/T) = 0.4817", "GREEN", "middle", 12)
    text(c, (P(x1, y1)[0] + 8, (P(x1, y2)[1] + P(x1, y1)[1]) / 2 + 4), f"Δln σ = {y2 - y1:.3f}", "GREEN", "start", 12)
    text(c, (330, 62), "slope = −Eg/2k = −3886 K", "PINK", "start", 13, "700")
    text(c, (330, 80), "high T on the left", "TEXT", "start", 12)
    REG.put("t6-p7-arrhenius-ge", c, "ln of the conductivity of intrinsic germanium against 1/T",
            f"Problem 7: ln σ = ln σ0 − Eg/(2kT) for germanium (Eg = 0.67 eV); the points are the given 25 °C value and the computed 75 °C value, σ = {s2:.1f} Ω⁻¹m⁻¹")


# ---------------------------------------------------------------- problem 8
def p8():
    sigma = 4e-4
    mu_e, mu_h = 0.14, 0.048
    se = sigma * mu_e / (mu_e + mu_h)
    sh = sigma - se
    c = Canvas(640, 330)
    # band diagram
    bx = 40
    rect(c, bx, 40, 220, 60, "BLUE", 1.6, None, "BLUE", 0.10)
    rect(c, bx, 190, 220, 70, "PINK", 1.6, None, "PINK", 0.10)
    text(c, (bx + 110, 36), "conduction band", "BLUE", "middle", 12, "700")
    text(c, (bx + 110, 278), "valence band", "PINK", "middle", 12, "700")
    for i in range(5):
        dot(c, (bx + 28 + i * 40, 62 + (i % 2) * 18), 6, "BLUE", "BLUE")
        circle(c, (bx + 48 + i * 40, 216 + (i % 2) * 20), 6, "PINK", 2.0, fill="PINK", opacity=0.05)
    line(c, (bx + 238, 100), (bx + 238, 190), "EDGE", 1.2)
    text(c, (bx + 246, 148), "Eg", "HEAD", "start", 14, "700")
    text(c, (bx + 110, 154), "n = p = " + sub("n", "i"), "HEAD", "middle", 14, "700")
    arrow(c, (bx + 160, 188), (bx + 160, 104), "GREEN", 1.8, 9)
    text(c, (bx + 168, 130), "excitation", "GREEN", "start", 11)
    # share bar
    sx, sy, sw, sh_ = 330, 120, 270, 44
    we = sw * se / sigma
    rect(c, sx, sy, we, sh_, "BLUE", 1.6, None, "BLUE", 0.25)
    rect(c, sx + we, sy, sw - we, sh_, "PINK", 1.6, None, "PINK", 0.25)
    text(c, (sx + we / 2, sy + 28), f"{100 * se / sigma:.1f} %", "HEAD", "middle", 14, "700")
    text(c, (sx + we + (sw - we) / 2, sy + 28), f"{100 * sh / sigma:.1f} %", "HEAD", "middle", 14, "700")
    text(c, (sx + we / 2, sy - 10), "electrons", "BLUE", "middle", 12, "700")
    text(c, (sx + we + (sw - we) / 2, sy - 10), "holes", "PINK", "middle", 12, "700")
    text(c, (sx + sw / 2, sy + 70), "σ = 4×10⁻⁴ Ω⁻¹m⁻¹ = σe + σh", "HEAD", "middle", 13, "700")
    text(c, (sx + we / 2, sy + 98), sub("σ", "e") + " = " + sci_sub(se), "BLUE", "middle", 12)
    text(c, (sx + sw - 50, sy + 98), sub("σ", "h") + " = " + sci_sub(sh), "PINK", "middle", 12)
    text(c, (sx + sw / 2, sy + 130), "shares in the ratio μe : μh = 0.14 : 0.048", "TEXT", "middle", 12)
    REG.put("t6-p8-carriers", c, "Electrons and holes of intrinsic silicon",
            "Problem 8: an intrinsic semiconductor has as many electrons as holes (n = p = ni, the intrinsic concentration); the conductivity splits in the ratio of the mobilities, 0.14 to 0.048 (schematic band diagram, bar to scale)")


# ---------------------------------------------------------------- problem 9
def logbar_panel(c, x0, y0, w, h, title, bars, lo, hi, fmt, ref=None):
    """Bars on a log axis from 10^lo to 10^hi; bars = (label, value, colour, rank)."""
    text(c, (x0 + w / 2, y0 - 12), title, "HEAD", "middle", 13, "700")
    line(c, (x0, y0 + h), (x0 + w, y0 + h), "EDGE", 1.2)
    line(c, (x0, y0), (x0, y0 + h), "EDGE", 1.2)
    n = len(bars)
    bw = w / n * 0.56
    scale = h / (hi - lo)
    for i, (lab, val, col, rank) in enumerate(bars):
        cx = x0 + w * (i + 0.5) / n
        top = y0 + h - (math.log10(val) - lo) * scale
        rect(c, cx - bw / 2, top, bw, y0 + h - top, col, 1.6, None, col, 0.30)
        text(c, (cx, top - 6), fmt(val), "HEAD", "middle", 11, "700")
        text(c, (cx, y0 + h + 16), lab, "TEXT", "middle", 11)
        badge(c, cx, y0 + h + 40, rank, col)
    if ref:
        yy = y0 + h - (math.log10(ref[0]) - lo) * scale
        line(c, (x0, yy), (x0 + w, yy), "ACC", 1.4, "5,4")
        pass


def sci_sub(v, nd=3):
    """A x 10^n label with a real superscript (SVG markup)."""
    e = int(math.floor(math.log10(abs(v))))
    return f"{v / 10 ** e:.{nd}f}×" + sub("10", ("−" if e < 0 else "") + str(abs(e)), True)


def sci(v):
    """3 significant digits as a x 10^n with unicode superscripts."""
    e = int(math.floor(math.log10(v)))
    mant = v / 10 ** e
    sup = str(e).translate(str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))
    return f"{mant:.3g}×10{sup}"


def p9():
    a = 0.67 / (2 * K_B)
    rel = lambda t: math.exp(a * (1 / 273.15 - 1 / (t + 273.15)))
    c = Canvas(640, 352)
    logbar_panel(c, 36, 70, 160, 180, "a) pure Ge, σ / σ(0 °C)",
                 [("0 °C", 1.0, "BLUE", 3), ("25 °C", rel(25), "GREEN", 2), ("50 °C", rel(50), "PINK", 1)], -0.2, 1.2,
                 lambda v: f"{v:.2f}")
    # b) sigma of pure Si and doped Si (1 ppm, bounds)
    n_si = 2.33e6 * 6.022e23 / 28.09 * 1e-6
    lo_s, hi_s = n_si * Q * 0.001, n_si * Q * 0.135
    logbar_panel(c, 250, 70, 170, 180, "b) Si at 300 K, σ (Ω⁻¹m⁻¹)",
                 [("pure", 4e-4, "BLUE", 2), ("P, 1 ppm", hi_s, "PINK", 1)], -4, 4,
                 lambda v: sci(v) if v < 1 else f"{v:.0f}")
    yy = 70 + 180 - (math.log10(lo_s) + 4) * (180 / 8)
    line(c, (250 + 170 * 0.75 - 22, yy), (250 + 170 * 0.75 + 22, yy), "HEAD", 2.0)
    text(c, (250 + 170 * 0.75 + 26, yy + 4), f"{lo_s:.1f}", "TEXT", "start", 10)
    n_ge1 = 5.32e6 * 6.022e23 / 72.63 * 1e-6
    logbar_panel(c, 470, 70, 150, 180, "c) Ge, N donors, n (m⁻³)",
                 [("100 ppb", n_ge1 / 10, "BLUE", 2), ("1 ppm", n_ge1, "PINK", 1)], 18, 23,
                 sci, ref=(2.4e19, sub("n", "i")))
    text(c, (320, 324), "badge 1 = highest conductivity; panel b: bar = upper bound (μe = 0.135), tick = lower bound (μe = 0.001)", "TEXT", "middle", 11)
    text(c, (320, 342), "orange dashed line in c: " + sub("n", "i") + " of intrinsic Ge = 2.4×10¹⁹ m⁻³ (S31)", "ACC", "middle", 11, "700")
    REG.put("t6-p9-ordering", c, "Ranking of the semiconductors of problem 9",
            "Problem 9: (a) germanium against temperature, (b) pure and phosphorus-doped silicon, (c) germanium with 100 ppb and 1 ppm of N; bars are computed with the data of the solution (logarithmic scale in b and c), 1 marks the highest conductivity")


# ---------------------------------------------------------------- problem 10
def p10():
    c = Canvas(640, 446)
    pw, ph = 196, 150
    panels = [
        ("a) Eg of the compound (eV)", [("InSb", 0.17, "BLUE", 1), ("GaAs", 1.42, "GREEN", 2), ("AlP", 2.45, "PINK", 3)], 2.8, "e", "AlP ≈ 2.45: extension"),
        ("b) Eg (eV)", [("InSb", 0.17, "BLUE", 1), ("CdTe", 1.5, "PINK", 2)], 2.8, "e", "CdTe ≈ 1.5: extension"),
        ("c) " + sub("E", "d") + " in Ge (eV)", [("Sb", 0.0096, "BLUE", 1), ("P", 0.0120, "PINK", 2)], 0.0150, "d", ""),
        ("d) " + sub("E", "d") + " of P (eV)", [("Ge", 0.0120, "BLUE", 1), ("Si", 0.045, "PINK", 2)], 0.055, "d", "μe: Ge 0.39, Si 0.135"),
        ("e) " + sub("E", "a") + " in Si (eV)", [("B", 0.045, "BLUE", 1), ("In", 0.160, "PINK", 2)], 0.19, "d", ""),
        ("f) " + sub("E", "d") + " in Ge (eV)", [("Sb", 0.0096, "BLUE", 1), ("As", 0.0127, "PINK", 2)], 0.0150, "d", ""),
    ]
    for idx, (title, bars, vmax, kind, note) in enumerate(panels):
        col, row = idx % 3, idx // 3
        x0, y0 = 26 + col * (pw + 20), 48 + row * 205
        text(c, (x0 + pw / 2, y0 - 16), title, "HEAD", "middle", 12, "700")
        line(c, (x0, y0 + ph - 38), (x0 + pw, y0 + ph - 38), "EDGE", 1.2)
        line(c, (x0, y0), (x0, y0 + ph - 38), "EDGE", 1.2)
        hh = ph - 38
        n = len(bars)
        bw = pw / n * 0.46
        for i, (lab, val, colr, rank) in enumerate(bars):
            cx = x0 + pw * (i + 0.5) / n
            top = y0 + hh - val / vmax * hh
            dash = "4,3" if (note.startswith(lab) and "extension" in note) else None
            rect(c, cx - bw / 2, top, bw, y0 + hh - top, colr, 1.6, dash, colr, 0.30)
            text(c, (cx, top - 6), f"{val:g}", "HEAD", "middle", 11, "700")
            text(c, (cx, y0 + hh + 15), lab, "TEXT", "middle", 11)
            badge(c, cx, y0 + hh + 34, rank, colr)
        if note:
            text(c, (x0 + pw / 2, y0 + hh + 58), note, "TEXT", "middle", 11)
    text(c, (320, 436), "badge 1 = highest conductivity; smaller gap or ionisation energy means more carriers (S31-S33, S40)", "TEXT", "middle", 11)
    REG.put("t6-p10-ordering", c, "Ranking of the semiconductors of problem 10",
            "Problem 10: band gaps (a, b) and donor or acceptor ionisation energies (c to f) of the pairs compared, with the data of Session 13 Slides 33 and 40; 1 marks the higher conductivity")


def problems(REG_):
    global REG
    REG = REG_
    for fn in (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        fn()


REG = None
