"""Topic 3 figures for Fluid Mechanics: the conservation-laws problems CL1 to CL22.

Two figures per problem where the sources have them:
  clN-statement : the figure of the official statement, redrawn (same symbols, arrows and labels);
  clN-cv        : the control volume used in the worked solution (surfaces named exactly as in the text).
Conventions: geometry and walls in HEAD, fluid shaded in BLUE, velocities in BLUE, the control volume
dashed in GREEN with its surfaces and outward normals, forces and torques in ACC.
Problems whose figure is too intricate to redraw use a cropped PNG of the original (RASTER below).
"""
import math

from figures.svgkit import (Canvas, Registry, arrow, arrow_head, circle, dim, fmt, hatch, line, pathd, poly,
                            rect, sub, text)

REG = Registry("FM-T3")

# Cropped originals (PNG in vault/attachments/FM-T3/): name -> (alt text, caption).
RASTER = {}

SERIF = "Newsreader, Georgia, 'Times New Roman', serif"
CV_DASH = "8,5"


# ----------------------------------------------------------------------------------------- helpers
def vec(s):
    """A vector symbol with an overbar (the class notation)."""
    return f'<tspan text-decoration="overline">{s}</tspan>'


def lab(c, p, s, col="HEAD", anchor="middle", size=17, italic=True, weight="400"):
    """A mathematical label (serif, italic by default)."""
    style = ' font-style="italic"' if italic else ""
    c.add(f'<text x="{fmt(p[0])}" y="{fmt(p[1])}" fill="{col}" font-size="{size}" font-weight="{weight}" '
          f'text-anchor="{anchor}" font-family="{SERIF}"{style}>{s}</text>')


def note(c, p, s, col="TEXT", anchor="middle", size=13, weight="400"):
    """A short descriptive label (sans)."""
    text(c, p, s, col, anchor, size=size, weight=weight)


def ellipse(c, cx, cy, rx, ry, col="HEAD", w=1.6, dash=None, fill="none", opacity=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' fill-opacity="{opacity}"' if opacity is not None else ""
    c.add(f'<ellipse cx="{fmt(cx)}" cy="{fmt(cy)}" rx="{fmt(rx)}" ry="{fmt(ry)}" fill="{fill}"{o} '
          f'stroke="{col}" stroke-width="{w}"{d}/>')


def hatched_ellipse(c, cx, cy, rx, ry, col="EDGE", step=9, w=1.0):
    """Ellipse filled with 45-degree hatching (a solid bottom seen in perspective)."""
    k = -rx - ry
    while k <= rx + ry:
        # line x - cx = (y - cy) + k  ->  points on the ellipse
        a = 1 / rx ** 2 + 1 / ry ** 2
        b = 2 * k / rx ** 2
        cc = k ** 2 / rx ** 2 - 1
        disc = b * b - 4 * a * cc
        if disc > 0:
            u1 = (-b - math.sqrt(disc)) / (2 * a)
            u2 = (-b + math.sqrt(disc)) / (2 * a)
            line(c, (cx + u1 + k, cy + u1), (cx + u2 + k, cy + u2), col, w)
        k += step
    ellipse(c, cx, cy, rx, ry)


def normal(c, p, d, label=None, length=30, lab_off=(0, 0), anchor="middle"):
    """Outward unit normal of the control volume: green arrow from p along direction d."""
    label = vec("n") if label is None else label
    L = math.hypot(*d)
    q = (p[0] + d[0] / L * length, p[1] + d[1] / L * length)
    arrow(c, p, q, "GREEN", 1.6, 8)
    lab(c, (q[0] + lab_off[0], q[1] + lab_off[1]), label, "GREEN", anchor, size=15)


def sigma(c, p, s, anchor="middle", size=17):
    """Name of a control surface, in the colour of the control volume."""
    lab(c, p, sub("Σ", s), "GREEN", anchor, size=size, weight="600")


def arc_arrow(c, centre, r, a0, a1, col="ACC", w=2.0):
    """Circular arrow from angle a0 to a1 (degrees, counter-clockwise on screen when a1 < a0)."""
    p0 = (centre[0] + r * math.cos(math.radians(a0)), centre[1] - r * math.sin(math.radians(a0)))
    p1 = (centre[0] + r * math.cos(math.radians(a1)), centre[1] - r * math.sin(math.radians(a1)))
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 0 if a1 > a0 else 1
    pathd(c, f"M{fmt(p0[0])},{fmt(p0[1])} A{fmt(r)},{fmt(r)} 0 {large},{sweep} {fmt(p1[0])},{fmt(p1[1])}", col, w)
    t = math.radians(a1)
    tang = (-math.sin(t), -math.cos(t)) if a1 > a0 else (math.sin(t), math.cos(t))
    arrow_head(c, (p1[0] - tang[0] * 10, p1[1] - tang[1] * 10), p1, col, 9)


def flow_arrows(c, x0, x1, ys, col="BLUE", w=1.6):
    for y in ys:
        arrow(c, (x0, y), (x1, y), col, w, 8)


def block_arrow(c, tip, length=70, half=9, head=20, col="HEAD"):
    """Hollow arrow pointing to the left with its tip at `tip` (the speed of a moving front)."""
    x, y = tip
    pts = [(x, y), (x + head, y - half - 6), (x + head, y - half), (x + length, y - half),
           (x + length, y + half), (x + head, y + half), (x + head, y + half + 6)]
    poly(c, pts, col, 1.6, close=True)


def caption_label(c, p, s):
    note(c, p, s, "HEAD", "middle", size=14, weight="600")


# ----------------------------------------------------------------------------------------- CL22
def cl22_statement():
    c = Canvas(560, 430)
    bottom = 330
    # (a) t = 0
    xa, ra, ha = 150, 60, 100
    line(c, (xa - ra, 40), (xa - ra, bottom)); line(c, (xa + ra, 40), (xa + ra, bottom))
    rect(c, xa - ra, bottom - ha, 2 * ra, ha, "none", 0, fill="BLUE", opacity=0.13)
    ellipse(c, xa, bottom - ha, ra, 12)
    hatched_ellipse(c, xa, bottom, ra, 12)
    lab(c, (xa + ra + 22, 52), sub("p", "a"))
    arrow(c, (xa + ra + 40, 160), (xa + ra + 40, 215), "HEAD", 1.4, 8); lab(c, (xa + ra + 52, 195), "g", anchor="start")
    dim(c, (xa - ra - 20, bottom - ha), (xa - ra - 20, bottom), "", "TEXT")
    lab(c, (xa - ra - 30, bottom - ha / 2 + 6), sub("h", "0"), anchor="end")
    arrow(c, (xa, bottom), (xa, bottom - 55), "HEAD", 1.3, 8); lab(c, (xa + 8, bottom - 44), "z", anchor="start", size=16)
    arrow(c, (xa, bottom), (xa + 80, bottom), "HEAD", 1.3, 8); lab(c, (xa + 84, bottom + 16), "y", anchor="start", size=16)
    arrow(c, (xa, bottom), (xa - 30, bottom + 26), "HEAD", 1.3, 8); lab(c, (xa - 36, bottom + 40), "x", anchor="end", size=16)
    dim(c, (xa - ra, bottom + 62), (xa + ra, bottom + 62), "", "TEXT")
    lab(c, (xa, bottom + 56), "2" + sub("a", "0"))
    caption_label(c, (xa, bottom + 88), "t = 0   (a)")
    # (b) t > 0: smaller radius, higher level; control volume V2 up to a fixed level z
    xb, rb = 410, 42
    hb = ha * (ra / rb) ** 2
    zl = bottom - 95
    line(c, (xb - rb, 40), (xb - rb, bottom)); line(c, (xb + rb, 40), (xb + rb, bottom))
    rect(c, xb - rb, bottom - hb, 2 * rb, hb, "none", 0, fill="BLUE", opacity=0.13)
    ellipse(c, xb, bottom - hb, rb, 10)
    hatched_ellipse(c, xb, bottom, rb, 10)
    ellipse(c, xb, zl, rb, 10, "HEAD", 1.4, "6,4")
    line(c, (xb - rb, zl), (xb - rb, bottom), "HEAD", 1.4, "6,4"); line(c, (xb + rb, zl), (xb + rb, bottom), "HEAD", 1.4, "6,4")
    for dx in (-24, -8, 8, 24):
        arrow(c, (xb + dx, zl - 2), (xb + dx, zl - 26), "BLUE", 1.4, 7)
    lab(c, (xb, zl - 34), sub("v", "z") + "(z, t)", size=15)
    dim(c, (xb, bottom), (xb, zl + 12), "", "TEXT"); lab(c, (xb + 8, bottom - 40), "z", anchor="start", size=16)
    line(c, (xb + rb, bottom - 50), (xb + rb + 26, bottom - 40), "TEXT", 1)
    lab(c, (xb + rb + 30, bottom - 34), sub("V", "2"), anchor="start")
    dim(c, (xb - rb - 22, bottom - hb), (xb - rb - 22, bottom), "", "TEXT")
    lab(c, (xb - rb - 30, bottom - hb / 2 + 6), "h(t)", anchor="end")
    lab(c, (xb + rb + 22, 52), sub("p", "a"))
    arrow(c, (xb + rb + 40, 160), (xb + rb + 40, 215), "HEAD", 1.4, 8); lab(c, (xb + rb + 52, 195), "g", anchor="start")
    dim(c, (xb - rb, bottom + 62), (xb + rb, bottom + 62), "", "TEXT")
    lab(c, (xb, bottom + 56), "2a(t)")
    caption_label(c, (xb, bottom + 88), "t > 0   (b)")
    REG.put("cl22-statement", c,
            "Cylinder of radius a0 with water up to h0 at t = 0, and at t > 0 a smaller radius a(t), a higher level h(t) "
            "and the control volume V2 up to a fixed level z",
            "Statement figure (redrawn from CL22.pdf, p. 1): (a) at $t = 0$, radius $a_0$ and level $h_0$; "
            "(b) at $t > 0$, radius $a(t)$, level $h(t)$ and the fixed control volume $V_2$ up to the level $z$")


def cl22_cv():
    c = Canvas(560, 420)
    bottom, top = 320, 110
    # (1) control volume 1: the water itself
    x1, r1 = 150, 62
    rect(c, x1 - r1, top, 2 * r1, bottom - top, "none", 0, fill="BLUE", opacity=0.10)
    line(c, (x1 - r1, 40), (x1 - r1, bottom), "EDGE", 2.2); line(c, (x1 + r1, 40), (x1 + r1, bottom), "EDGE", 2.2)
    ellipse(c, x1, top, r1, 11, "GREEN", 2.0, CV_DASH)
    line(c, (x1 - r1 + 3, top), (x1 - r1 + 3, bottom), "GREEN", 2.0, CV_DASH)
    line(c, (x1 + r1 - 3, top), (x1 + r1 - 3, bottom), "GREEN", 2.0, CV_DASH)
    ellipse(c, x1, bottom, r1, 11, "GREEN", 2.0, CV_DASH)
    sigma(c, (x1 + r1 + 14, top + 6), "s", "start")
    sigma(c, (x1 + r1 + 14, (top + bottom) / 2 + 30), "L", "start")
    sigma(c, (x1 + r1 + 14, bottom + 18), "b", "start")
    normal(c, (x1 - 40, top - 4), (0, -1), lab_off=(0, -6))
    normal(c, (x1 + r1, (top + bottom) / 2 - 10), (1, 0), lab_off=(10, 5), anchor="start")
    normal(c, (x1, bottom + 11), (0, 1), lab_off=(14, 4), anchor="start")
    arrow(c, (x1 + 20, top - 2), (x1 + 20, top - 32), "BLUE", 1.6, 8); lab(c, (x1 + 12, top - 22), "dh/dt", "BLUE", "end", 15)
    arrow(c, (x1 - r1 - 2, 215), (x1 - r1 + 24, 215), "BLUE", 1.6, 8); lab(c, (x1 - r1 + 30, 220), "da/dt", "BLUE", "start", 15)
    dim(c, (x1 - r1 - 26, top), (x1 - r1 - 26, bottom), "", "TEXT"); lab(c, (x1 - r1 - 32, (top + bottom) / 2), "h(t)", anchor="end")
    caption_label(c, (x1, bottom + 60), "(1) control volume 1: the water")
    note(c, (x1, bottom + 80), "every surface moves with the fluid", "TEXT", size=12)
    # (2) control volume V2, from the bottom to the fixed level z
    x2, r2, zl = 420, 62, 225
    rect(c, x2 - r2, top, 2 * r2, bottom - top, "none", 0, fill="BLUE", opacity=0.10)
    line(c, (x2 - r2, 40), (x2 - r2, bottom), "EDGE", 2.2); line(c, (x2 + r2, 40), (x2 + r2, bottom), "EDGE", 2.2)
    ellipse(c, x2, top, r2, 11, "EDGE", 1.4)
    ellipse(c, x2, zl, r2, 11, "GREEN", 2.0, CV_DASH)
    line(c, (x2 - r2 + 3, zl), (x2 - r2 + 3, bottom), "GREEN", 2.0, CV_DASH)
    line(c, (x2 + r2 - 3, zl), (x2 + r2 - 3, bottom), "GREEN", 2.0, CV_DASH)
    ellipse(c, x2, bottom, r2, 11, "GREEN", 2.0, CV_DASH)
    for dx in (-8, 8, 24, 40):
        arrow(c, (x2 + dx, zl - 2), (x2 + dx, zl - 30), "BLUE", 1.5, 7)
    lab(c, (x2 + 16, zl - 40), sub("v", "z") + "(z, t)", "BLUE", size=15)
    normal(c, (x2 - 38, zl + 4), (0, -1), length=24, lab_off=(-10, 2), anchor="end")
    sigma(c, (x2 + r2 + 14, zl + 6), "z", "start")
    sigma(c, (x2 + r2 + 14, (zl + bottom) / 2 + 10), "L2", "start")
    sigma(c, (x2 + r2 + 14, bottom + 18), "b", "start")
    dim(c, (x2 - r2 - 26, zl), (x2 - r2 - 26, bottom), "", "TEXT"); lab(c, (x2 - r2 - 32, (zl + bottom) / 2 + 6), "z", anchor="end")
    caption_label(c, (x2, bottom + 60), "(2) control volume V₂")
    note(c, (x2, bottom + 80), "top fixed at the level z, side moving with the wall", "TEXT", size=12)
    REG.put("cl22-cv", c,
            "The two control volumes of the solution: the water itself, bounded by the free surface, the lateral wall "
            "and the bottom; and V2, from the bottom up to the fixed level z",
            "Control volumes of the solution: (1) the water, with $\\Sigma_s$, $\\Sigma_L$, $\\Sigma_b$ and their outward "
            "normals, used for mass, momentum and kinetic energy; (2) $V_2$, with the fixed section $\\Sigma_z$, the moving "
            "wall $\\Sigma_{L2}$ and $\\Sigma_b$, used for $v_z(z,t)$ (after the official solution, CL22.pdf, p. 2)")


# ----------------------------------------------------------------------------------------- CL21
def cl21_statement():
    c = Canvas(520, 470)
    cx, R = 260, 30
    ys = [55, 145, 235, 325, 415]
    for y in ys:
        circle(c, (cx, y), R, "HEAD", 1.6, fill="EDGE", opacity=0.35)
    dim(c, (cx - 70, ys[0]), (cx - 70, ys[1]), "", "TEXT")
    line(c, (cx - 82, ys[0]), (cx - 58, ys[0]), "TEXT", 1); line(c, (cx - 82, ys[1]), (cx - 58, ys[1]), "TEXT", 1)
    lab(c, (cx - 80, (ys[0] + ys[1]) / 2 + 6), "3R", anchor="end")
    ym = ys[2]
    lab(c, (70, ym - 50), sub("ρ", "1"), size=19)
    lab(c, (70, ym - 14), sub("U", "1"), size=19)
    arrow(c, (40, ym), (130, ym), "BLUE", 2.0, 10)
    lab(c, (70, ym + 32), sub("p", "1"), size=19)
    lab(c, (420, ym - 14), sub("U", "2"), size=19)
    arrow(c, (390, ym), (480, ym), "BLUE", 2.0, 10)
    lab(c, (420, ym + 32), sub("p", "2"), size=19)
    REG.put("cl21-statement", c,
            "Linear array of cylinders of radius R with centres 3R apart, across a gas stream U1, rho1, p1 that leaves "
            "with U2, p2",
            "Statement figure (redrawn from CL21.pdf, p. 1): array of cylinders of radius $R$, centres $3R$ apart, in a "
            "stream $U_1$, $\\rho_1$, $p_1$; far downstream $U_2$, $p_2$")


def cl21_cv():
    c = Canvas(600, 340)
    cx, R = 270, 30
    ym = 170
    x0, x1, yt, yb = 95, 445, ym - 45, ym + 45            # the control volume is 3R high
    for y in (ym - 90, ym, ym + 90):
        circle(c, (cx, y), R, "EDGE" if y != ym else "HEAD", 1.6, fill="EDGE", opacity=0.30)
    rect(c, x0, yt, x1 - x0, yb - yt, "GREEN", 2.0, CV_DASH)
    circle(c, (cx, ym), R + 6, "GREEN", 1.8, CV_DASH)
    sigma(c, (x0 - 12, ym - 14), "1", "end")
    sigma(c, (x1 + 12, ym - 14), "2", "start")
    sigma(c, (x0 + 50, yt - 10), "top")
    sigma(c, (x0 + 50, yb + 24), "bot")
    sigma(c, (cx + R + 40, ym - 18), "cyl", "start")
    normal(c, (x0, ym + 24), (-1, 0), length=28, lab_off=(-4, 5), anchor="end")
    normal(c, (x1, ym + 24), (1, 0), length=28, lab_off=(4, 5), anchor="start")
    normal(c, (x1 - 60, yt), (0, -1), length=26, lab_off=(14, 6), anchor="start")
    normal(c, (x1 - 60, yb), (0, 1), length=26, lab_off=(14, 6), anchor="start")
    q = (cx + (R + 6) * 0.7071, ym + (R + 6) * 0.7071)
    arrow(c, q, (q[0] - 13, q[1] - 13), "GREEN", 1.6, 7)
    lab(c, (q[0] + 4, q[1] + 16), vec("n"), "GREEN", "start", 15)
    arrow(c, (20, ym - 8), (75, ym - 8), "BLUE", 2.0, 9); lab(c, (46, ym - 18), sub("U", "1"), "BLUE", size=16)
    arrow(c, (x1 + 20, ym - 8), (x1 + 75, ym - 8), "BLUE", 2.0, 9); lab(c, (x1 + 46, ym - 18), sub("U", "2"), "BLUE", size=16)
    dim(c, (x1 + 110, yt), (x1 + 110, yb), "", "TEXT"); lab(c, (x1 + 118, ym + 6), "3R", anchor="start", size=15)
    arrow(c, (40, 300), (80, 300), "HEAD", 1.3, 8); lab(c, (86, 305), "x", anchor="start", size=15)
    arrow(c, (40, 300), (40, 262), "HEAD", 1.3, 8); lab(c, (46, 266), "y", anchor="start", size=15)
    REG.put("cl21-cv", c,
            "Control volume one period high around one cylinder: inlet and outlet sections, the two lines midway between "
            "cylinders and the cylinder surface",
            "Control volume of the solution: $\\Sigma_1$ and $\\Sigma_2$ far upstream and downstream, $\\Sigma_{top}$ and "
            "$\\Sigma_{bot}$ midway between cylinders ($3R$ apart; their fluxes cancel by periodicity) and the cylinder "
            "surface $\\Sigma_{cyl}$, with the outward normals")


# ----------------------------------------------------------------------------------------- CL20
def _contraction(x, xa, xb, ya, yb):
    s = min(max((x - xa) / (xb - xa), 0.0), 1.0)
    return ya + (yb - ya) * (1 - math.cos(math.pi * s)) / 2


def _contraction_walls(c, col="HEAD", w=2.6):
    xa, xb = 230, 440
    line(c, (20, 40), (xa, 40), col, w); line(c, (20, 260), (xa, 260), col, w)
    xs = [xa + (xb - xa) * k / 60 for k in range(61)]
    poly(c, [(x, _contraction(x, xa, xb, 40, 132)) for x in xs], col, w)
    poly(c, [(x, _contraction(x, xa, xb, 260, 168)) for x in xs], col, w)
    return xa, xb


def cl20_statement():
    c = Canvas(600, 300)
    xa, xb = _contraction_walls(c)
    ellipse(c, xa, 150, 12, 110, "HEAD", 1.4)
    ellipse(c, xb, 150, 6, 18, "HEAD", 1.6)
    flow_arrows(c, 165, 210, [60, 90, 120, 150, 180, 210, 240])
    lab(c, (150, 96), sub("p", "u"), anchor="end"); lab(c, (150, 156), sub("v", "u"), anchor="end")
    lab(c, (150, 216), sub("T", "u"), anchor="end")
    dim(c, (60, 40), (60, 260), "", "TEXT"); lab(c, (50, 156), "D", anchor="end", size=19)
    flow_arrows(c, xb + 8, xb + 60, [138, 150, 162], "BLUE", 1.5)
    lab(c, (xb + 70, 156), sub("T", "d"), anchor="start")
    arrow(c, (xb, 100), (xb, 130), "TEXT", 1.1, 7); arrow(c, (xb, 200), (xb, 170), "TEXT", 1.1, 7)
    lab(c, (xb + 8, 104), "d", anchor="start")
    lab(c, (xb + 8, 214), sub("v", "d"), anchor="start")
    lab(c, (345, 70), sub("p", "a"), anchor="start")
    arrow(c, (30, 285), (72, 285), "HEAD", 1.3, 8); lab(c, (78, 290), "x", anchor="start", size=15)
    REG.put("cl20-statement", c,
            "Pipe of diameter D ending in a coaxial contraction with an orifice of diameter d; upstream pu, vu, Tu; "
            "discharge vd, Td into the ambient pressure pa",
            "Statement figure (redrawn from CL20.pdf, p. 1, axial section): pipe of diameter $D$ with uniform $p_u$, $v_u$, "
            "$T_u$; contraction ending in the orifice of diameter $d$, discharging at $v_d$, $T_d$ into $p_a$")


def cl20_cv():
    c = Canvas(600, 310)
    xa, xb = _contraction_walls(c, "EDGE", 2.2)
    xs = [xa + (xb - xa) * k / 60 for k in range(61)]
    top = [(x, _contraction(x, xa, xb, 44, 135)) for x in xs]
    bot = [(x, _contraction(x, xa, xb, 256, 165)) for x in xs]
    poly(c, [(xa + 2, 256), (xa + 2, 44)] + top + [(xb - 2, 135), (xb - 2, 165)] + bot[::-1] + [(xa + 2, 256)],
         "GREEN", 2.0, CV_DASH, fill="BLUE", opacity=0.10)
    sigma(c, (xa + 2, 28), "u")
    sigma(c, (xb + 14, 120), "d", "start")
    sigma(c, (300, 100), "w", "start")
    normal(c, (xa + 2, 210), (-1, 0), length=30, lab_off=(-6, 5), anchor="end")
    normal(c, (xb - 2, 150), (1, 0), length=30, lab_off=(6, 5), anchor="start")
    xm = 290
    ym = _contraction(xm, xa, xb, 40, 132)
    normal(c, (xm, ym), (0.25, -1), length=26, lab_off=(8, 4), anchor="start")
    arrow(c, (150, 110), (205, 110), "BLUE", 2.0, 9); lab(c, (176, 100), sub("v", "u"), "BLUE", size=16)
    arrow(c, (xb + 50, 150), (xb + 105, 150), "BLUE", 2.0, 9); lab(c, (xb + 78, 140), sub("v", "d"), "BLUE", size=16)
    arrow(c, (260, 292), (340, 292), "ACC", 2.6, 11); lab(c, (350, 298), vec("F"), "ACC", "start", 18, weight="700")
    note(c, (372, 297), "force on the contraction", "ACC", "start", 12)
    lab(c, (395, 62), sub("p", "a") + " outside", anchor="start", size=14)
    REG.put("cl20-cv", c,
            "Control volume: the liquid inside the contraction, from the upstream section to the orifice, bounded by the "
            "contraction wall",
            "Control volume of the solution: the liquid inside the contraction, with $\\Sigma_u$ (upstream section, "
            "$\\bar{n} = -\\bar{e}_x$), $\\Sigma_d$ (orifice, $\\bar{n} = +\\bar{e}_x$) and $\\Sigma_w$ (wall, outer face at "
            "$p_a$); $\\bar{F}$ is the force on the contraction")


# ----------------------------------------------------------------------------------------- CL12
def _u_pipe(c, col="HEAD", w=2.2, fill=None):
    xl, xr, yt, yb, half = 120, 400, 70, 300, 24
    outer = [(xl - half, yb), (xl - half, yt - half), (xr + half, yt - half), (xr + half, yb)]
    inner = [(xl + half, yb), (xl + half, yt + half), (xr - half, yt + half), (xr - half, yb)]
    if fill:
        poly(c, outer + inner[::-1], "none", 0, fill=fill, opacity=0.10, close=True)
    poly(c, outer, col, w); poly(c, inner, col, w)
    return xl, xr, yt, yb, half


def cl12_statement():
    c = Canvas(540, 410)
    xl, xr, yt, yb, half = _u_pipe(c)
    ellipse(c, xl, yb, half, 6); ellipse(c, xr, yb, half, 6)
    arrow(c, (xl, yt + 4), (xl, yt - 40), "HEAD", 1.3, 8); lab(c, (xl - 8, yt - 36), "y", anchor="end", size=15)
    arrow(c, (xl, yt + 4), (xl + 50, yt + 4), "HEAD", 1.3, 8); lab(c, (xl + 54, yt + 9), "x", anchor="start", size=15)
    dim(c, (xl, 190), (xr, 190), "", "TEXT"); lab(c, ((xl + xr) / 2, 180), "L", size=19)
    lab(c, ((xl + xr) / 2, 30), sub("p", "a"))
    for dx in (-16, -8, 0, 8, 16):
        arrow(c, (xl + dx, 365), (xl + dx, 318), "BLUE", 1.5, 7)
        arrow(c, (xr + dx, 318), (xr + dx, 365), "BLUE", 1.5, 7)
    lab(c, (xl - 32, 335), sub("T", "u"), anchor="end"); lab(c, (xl + 32, 335), sub("p", "u"), anchor="start")
    lab(c, (xl, 392), sub("V", "u"))
    lab(c, (xr - 32, 335), sub("T", "o"), anchor="end"); lab(c, (xr + 32, 335), sub("p", "a"), anchor="start")
    lab(c, (xr, 392), sub("V", "o"))
    REG.put("cl12-statement", c,
            "Inverted U-pipe of constant section: the gas enters upwards at the left leg with Tu, pu, Vu and leaves "
            "downwards at the right leg, a distance L away, with To, pa, Vo",
            "Statement figure (redrawn from CL12.pdf, p. 1): inverted U-pipe of section $A$; inlet state $T_u$, $p_u$, $V_u$ "
            "in the left leg, outlet $T_o$, $p_a$, $V_o$ in the right leg, legs $L$ apart; origin on the axis of the left leg")


def cl12_cv():
    c = Canvas(540, 410)
    xl, xr, yt, yb, half = _u_pipe(c, "EDGE", 2.2)
    g = 3
    poly(c, [(xl - half + g, yb), (xl - half + g, yt - half + g), (xr + half - g, yt - half + g), (xr + half - g, yb),
             (xr - half - g, yb), (xr - half - g, yt + half - g), (xl + half + g, yt + half - g), (xl + half + g, yb)],
         "GREEN", 2.0, CV_DASH, fill="BLUE", opacity=0.10, close=True)
    sigma(c, (xl - 36, yb + 6), "u", "end")
    sigma(c, (xr + 36, yb + 6), "o", "start")
    sigma(c, (xr + half + 12, 170), "w", "start")
    normal(c, (xl + 10, yb), (0, 1), length=28, lab_off=(10, 4), anchor="start")
    normal(c, (xr + 10, yb), (0, 1), length=28, lab_off=(10, 4), anchor="start")
    arrow(c, (xl - 12, yb + 60), (xl - 12, yb + 6), "BLUE", 2.0, 9); lab(c, (xl - 18, yb + 50), sub("V", "u"), "BLUE", "end", 16)
    arrow(c, (xr - 12, yb + 6), (xr - 12, yb + 60), "BLUE", 2.0, 9); lab(c, (xr - 18, yb + 50), sub("V", "o"), "BLUE", "end", 16)
    c.add(f'<circle cx="{xl}" cy="{yt}" r="4" fill="HEAD"/>')
    lab(c, (xl - 8, yt + 20), "O", anchor="end", size=16)
    arrow(c, (xl, yt), (xl, yt - 42), "HEAD", 1.3, 8); lab(c, (xl - 8, yt - 38), "y", anchor="end", size=15)
    arrow(c, (xl, yt), (xl + 48, yt), "HEAD", 1.3, 8); lab(c, (xl + 52, yt + 5), "x", anchor="start", size=15)
    dim(c, (xl, 200), (xr, 200), "", "TEXT"); lab(c, ((xl + xr) / 2, 190), "L", size=18)
    arrow(c, (205, 175), (205, 120), "ACC", 2.6, 11); lab(c, (214, 140), vec("F"), "ACC", "start", 18, weight="700")
    arc_arrow(c, (320, 145), 22, 320, 200)
    lab(c, (350, 152), vec("M") + " (about O)", "ACC", "start", 16, weight="700")
    REG.put("cl12-cv", c,
            "Control volume: the gas inside the pipe between the measuring section and the outlet; origin O on the axis "
            "of the left leg; force and moment on the pipe",
            "Control volume of the solution: the gas in the pipe, with $\\Sigma_u$ (measuring section) and $\\Sigma_o$ "
            "(outlet), both with $\\bar{n} = -\\bar{e}_y$, and the wall $\\Sigma_w$; moments about $O$ on the axis of the "
            "left leg. $\\bar{F}$ points up and $\\bar{M}$ is counter-clockwise ($+\\bar{e}_z$), as in the results")


# ----------------------------------------------------------------------------------------- CL2
def _bore_surface(x):
    """Free surface: layer h0 on the left, rough front, layer h1 on the right (screen y)."""
    if x <= 240:
        return 170.0
    if x >= 330:
        return 110.0
    s = (x - 240) / 90
    return 170 - 60 * (3 * s * s - 2 * s ** 3) - 4 * math.sin(s * math.pi * 5) * math.sin(s * math.pi)


def _bore(c, x0=20, x1=540, col="HEAD"):
    xs = [x0 + (x1 - x0) * k / 260 for k in range(261)]
    pts = [(x, _bore_surface(x)) for x in xs]
    poly(c, pts + [(x1, 220), (x0, 220)], "none", 0, fill="BLUE", opacity=0.15, close=True)
    poly(c, pts, col, 1.8)
    line(c, (x0, 220), (x1, 220), "HEAD", 2.4)
    hatch(c, (x0, 220), (x1, 220), side=-1)


def cl2_statement():
    c = Canvas(600, 260)
    _bore(c)
    lab(c, (70, 90), sub("p", "a"))
    block_arrow(c, (236, 92), length=70)
    lab(c, (272, 74), "U")
    for y in (128, 144, 160, 176, 192, 208):
        arrow(c, (420, y), (370, y), "BLUE", 1.5, 8)
    lab(c, (400, 100), sub("U", "1"))
    dim(c, (470, 110), (470, 220), "", "TEXT"); lab(c, (478, 170), sub("h", "1"), anchor="start")
    dim(c, (60, 170), (60, 220), "", "TEXT"); lab(c, (68, 202), sub("h", "0"), anchor="start")
    arrow(c, (500, 220), (500, 192), "HEAD", 1.2, 7); lab(c, (506, 200), "z", anchor="start", size=15)
    arrow(c, (540, 220), (585, 220), "HEAD", 1.3, 8); lab(c, (590, 225), "x", anchor="start", size=15)
    arrow(c, (560, 105), (560, 150), "HEAD", 1.4, 8); lab(c, (570, 130), "g", anchor="start")
    REG.put("cl2-statement", c,
            "Bore moving to the left with speed U over a stagnant layer of thickness h0, leaving behind a layer h1 moving "
            "to the left with U1; bottom wall, ambient pressure pa, gravity g",
            "Statement figure (redrawn from CL2.pdf, p. 1): the bore advances to the left with speed $U$ over the stagnant "
            "layer $h_0$; behind it the layer $h_1$ moves with $U_1$; $z$ is measured from the bottom")


def cl2_cv():
    c = Canvas(600, 520)
    # (1) the hydrostatic column in the uniform layer ahead of the bore
    yfree, ybot, zc = 70, 210, 135
    rect(c, 60, yfree, 480, ybot - yfree, "none", 0, fill="BLUE", opacity=0.15)
    line(c, (60, yfree), (540, yfree), "HEAD", 1.8); line(c, (60, ybot), (540, ybot), "HEAD", 2.4)
    hatch(c, (60, ybot), (540, ybot), side=-1)
    rect(c, 260, yfree + 2, 80, zc - yfree - 2, "GREEN", 2.0, CV_DASH)
    sigma(c, (352, yfree - 8), "top", "start")
    sigma(c, (352, 110), "side", "start")
    sigma(c, (252, zc + 5), "bot", "end")
    normal(c, (300, yfree + 2), (0, -1), length=24, lab_off=(-10, 6), anchor="end")
    normal(c, (322, zc), (0, 1), length=22, lab_off=(10, 4), anchor="start")
    lab(c, (180, yfree - 8), sub("p", "a"))
    arrow(c, (292, 82), (292, 118), "ACC", 2.2, 9); note(c, (252, 104), "weight", "ACC", "end", 12)
    dim(c, (200, zc), (200, ybot), "", "TEXT"); lab(c, (192, 178), "z", anchor="end")
    dim(c, (260, 175), (340, 175), "", "TEXT"); lab(c, (300, 196), "Δx", size=15)
    dim(c, (450, yfree), (450, ybot), "", "TEXT"); lab(c, (458, 146), sub("h", "0"), anchor="start")
    caption_label(c, (300, 30), "(1) hydrostatic column in the uniform layer")
    # (2) mass and momentum, in the frame B of the bore (steady)
    dy = 250
    c.add(f'<g transform="translate(0,{dy})">')
    _bore(c, col="EDGE")
    x0, x1 = 150, 470
    xs = [x0 + (x1 - x0) * k / 120 for k in range(121)]
    surf = [(x, _bore_surface(x) + 3) for x in xs]
    poly(c, [(x0, 217)] + surf + [(x1, 217), (x0, 217)], "GREEN", 2.0, CV_DASH)
    sigma(c, (x0, 246), "0")
    sigma(c, (x1, 246), "1")
    sigma(c, (320, 246), "b")
    sigma(c, (232, 152), "s")
    normal(c, (x0, 196), (-1, 0), length=28, lab_off=(-4, -8), anchor="end")
    normal(c, (x1, 165), (1, 0), length=28, lab_off=(4, -8), anchor="start")
    normal(c, (400, 217), (0, 1), length=22, lab_off=(12, 0), anchor="start")
    normal(c, (420, 113), (0, -1), length=24, lab_off=(12, 6), anchor="start")
    for y in (188, 204):
        arrow(c, (30, y), (80, y), "BLUE", 1.6, 8)
    lab(c, (55, 178), "U", "BLUE", size=16)
    for y in (148, 174, 200):
        arrow(c, (535, y), (580, y), "BLUE", 1.6, 8)
    lab(c, (558, 134), "U − " + sub("U", "1"), "BLUE", size=15)
    c.add("</g>")
    caption_label(c, (300, dy + 40), "(2) mass and momentum, seen from the bore")
    note(c, (300, dy + 60), "frame B moves with −U ē" + sub("", "x") + ": the front is at rest", "TEXT", size=12)
    REG.put("cl2-cv", c,
            "Control volumes of the solution: the hydrostatic column in the uniform layer, and the bore seen from its "
            "own frame with the inlet and outlet sections, the bottom and the free surface",
            "Control volumes of the solution: (1) the column of width $\\Delta x$ between the height $z$ and the free "
            "surface ($\\Sigma_{bot}$, $\\Sigma_{top}$, $\\Sigma_{side}$), which gives the hydrostatic pressure; (2) in the "
            "frame of the bore, $\\Sigma_0$ (ahead, velocity $U$), $\\Sigma_1$ (behind, $U - U_1$), the bottom "
            "$\\Sigma_b$ and the free surface $\\Sigma_s$, with the outward normals")


# ----------------------------------------------------------------------------------------- build
def build():
    for fn in (cl22_statement, cl22_cv, cl21_statement, cl21_cv, cl20_statement, cl20_cv,
               cl12_statement, cl12_cv, cl2_statement, cl2_cv):
        fn()
    return REG
