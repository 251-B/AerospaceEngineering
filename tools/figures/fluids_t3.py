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


# ----------------------------------------------------------------------------------------- shared (Lote 2)
def overdot(c, p, s, col="HEAD", anchor="middle", size=17, weight="400", dx=0):
    """A label with a dot above it (time derivative), the dot drawn as a small circle so every font shows it."""
    lab(c, p, s, col, anchor, size, weight=weight)
    shift = {"middle": 0, "start": size * 0.32, "end": -size * 0.32}[anchor]
    c.add(f'<circle cx="{fmt(p[0] + shift + dx)}" cy="{fmt(p[1] - size * 0.86)}" r="1.7" fill="{col}"/>')


def cubic(p0, p1, p2, p3, n=60):
    """Points along a cubic Bezier curve."""
    out = []
    for k in range(n + 1):
        t = k / n
        a, b, cc, d = (1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t * t * (1 - t), t ** 3
        out.append((a * p0[0] + b * p1[0] + cc * p2[0] + d * p3[0], a * p0[1] + b * p1[1] + cc * p2[1] + d * p3[1]))
    return out


def leader(c, a, b, col="GREEN"):
    """Thin pointer from a label to the surface it names."""
    line(c, a, b, col, 1.0)


def axes(c, o, lx="x", ly="y", L=40):
    arrow(c, o, (o[0] + L, o[1]), "HEAD", 1.3, 8); lab(c, (o[0] + L + 6, o[1] + 5), lx, anchor="start", size=15)
    arrow(c, o, (o[0], o[1] - L), "HEAD", 1.3, 8); lab(c, (o[0] + 6, o[1] - L + 4), ly, anchor="start", size=15)


# ----------------------------------------------------------------------------------------- CL6
CL6_OUTER = "M130,105 L370,105 Q480,105 480,215 L480,470"
CL6_INNER = "M130,295 L330,295 Q400,295 400,365 L400,470"
CL6_BODY = "M130,105 L370,105 Q480,105 480,215 L480,470 L400,470 L400,365 Q400,295 330,295 L130,295 Z"


def _cl6_pipe(c, col="HEAD", w=2.2):
    pathd(c, CL6_BODY, "none", 0, fill="BLUE", opacity=0.10)
    pathd(c, CL6_OUTER, col, w); pathd(c, CL6_INNER, col, w)
    ellipse(c, 130, 200, 34, 95, col, w, fill="BLUE", opacity=0.10)
    ellipse(c, 440, 470, 40, 10, col, w)


def cl6_statement():
    c = Canvas(560, 560)
    _cl6_pipe(c)
    flow_arrows(c, 62, 152, [125, 150, 175, 200, 225, 250, 275])
    lab(c, (50, 155), sub("v", "i"), anchor="end"); lab(c, (50, 210), sub("p", "i"), anchor="end")
    lab(c, (50, 265), sub("T", "i"), anchor="end")
    lab(c, (172, 212), sub("A", "i"), anchor="start")
    arrow(c, (262, 222), (262, 168), "ACC", 2.0, 9); lab(c, (270, 176), sub("F", "z"), "ACC", "start", 18)
    arrow(c, (262, 222), (322, 222), "ACC", 2.0, 9); lab(c, (318, 244), sub("F", "x"), "ACC", "start", 18)
    for dx in (-14, 0, 14):
        arrow(c, (300 + dx - 8, 62), (300 + dx, 101), "PINK", 1.5, 7)
    lab(c, (300, 52), "Q", "PINK", size=18)
    lab(c, (500, 150), sub("p", "a"), anchor="start"); lab(c, (300, 340), sub("p", "a"))
    lab(c, (388, 470), sub("p", "a"), anchor="end")
    for x in (418, 432, 446, 460):
        arrow(c, (x, 482), (x, 534), "BLUE", 1.5, 7)
    lab(c, (408, 525), sub("v", "o"), anchor="end"); lab(c, (470, 530), sub("T", "o"), anchor="start")
    lab(c, (486, 478), sub("A", "o"), anchor="start")
    REG.put("cl6-statement", c,
            "Elbow-shaped pipe: horizontal inlet of area Ai with vi, pi, Ti; vertical outlet of area Ao discharging "
            "downwards with vo, To into the ambient pa; force components Fx, Fz and heat Q through the wall",
            "Statement figure (redrawn from CL6.pdf, p. 1): inlet section $A_i$ with $v_i$, $p_i$, $T_i$; outlet $A_o$ "
            "discharging a vertical jet $v_o$, $T_o$ into $p_a$; force components $F_x$, $F_z$ on the pipe and heat $Q$ "
            "through its walls")


def cl6_cv():
    c = Canvas(560, 560)
    _cl6_pipe(c, "EDGE", 2.0)
    pathd(c, "M136,111 L370,111 Q474,111 474,215 L474,466", "GREEN", 2.0, CV_DASH)
    pathd(c, "M136,289 L330,289 Q406,289 406,365 L406,466", "GREEN", 2.0, CV_DASH)
    ellipse(c, 136, 200, 28, 89, "GREEN", 2.0, CV_DASH)
    ellipse(c, 440, 466, 34, 7, "GREEN", 2.0, CV_DASH)
    sigma(c, (78, 345), "i", "end"); leader(c, (82, 338), (116, 272))
    sigma(c, (500, 300), "w", "start"); leader(c, (497, 294), (477, 284))
    sigma(c, (520, 452), "o", "start"); leader(c, (517, 452), (476, 466))
    normal(c, (108, 200), (-1, 0), length=34, lab_off=(-4, -8), anchor="end")
    normal(c, (300, 105), (0, -1), length=30, lab_off=(12, 6), anchor="start")
    normal(c, (424, 476), (0, 1), length=32, lab_off=(-8, 4), anchor="end")
    arrow(c, (178, 200), (240, 200), "BLUE", 2.0, 9); lab(c, (209, 190), sub("v", "i"), "BLUE", size=16)
    arrow(c, (456, 478), (456, 536), "BLUE", 2.0, 9); lab(c, (464, 524), sub("v", "o"), "BLUE", "start", 16)
    axes(c, (40, 520), "x", "z")
    REG.put("cl6-cv", c,
            "Control volume: the liquid inside the elbow, bounded by the inlet section, the pipe wall and the outlet section",
            "Control volume of the solution (as in the class notes): the liquid inside the pipe, with $\\Sigma_i$ (inlet, "
            "$\\bar{n} = -\\bar{e}_x$), $\\Sigma_o$ (outlet, $\\bar{n} = -\\bar{e}_z$) and the wall $\\Sigma_w$, where the "
            "force and the heat are collected")


# ----------------------------------------------------------------------------------------- CL19
def _cl19_pipe(c, col="HEAD", w=2.4):
    top = [(100, 250), (318, 250), (330, 238), (330, 60)]
    bot = [(100, 350), (418, 350), (430, 338), (430, 60)]
    poly(c, top + bot[::-1], "none", 0, fill="BLUE", opacity=0.10, close=True)
    poly(c, top, col, w); poly(c, bot, col, w)


def cl19_statement():
    c = Canvas(600, 430)
    _cl19_pipe(c)
    for k in range(12):
        y = 255 + k * 8
        arrow(c, (104, y), (160, y), "BLUE", 1.1, 6)
    yl1, yl2 = 300 - 50 / math.sqrt(2), 300 + 50 / math.sqrt(2)
    line(c, (66, yl1), (104, yl1), "HEAD", 1.0); line(c, (66, yl2), (104, yl2), "HEAD", 1.0)
    lab(c, (84, 247), sub("T", "2"), size=16); lab(c, (84, 306), sub("T", "1"), size=16)
    lab(c, (84, 368), sub("T", "2"), size=16)
    dim(c, (58, yl1), (58, yl2), "", "TEXT"); lab(c, (50, 306), "D/√2", anchor="end", size=16)
    lab(c, (172, 284), sub("U", "i"), anchor="start"); lab(c, (172, 330), sub("p", "i"), anchor="start")
    arrow(c, (150, 212), (150, 249), "TEXT", 1.1, 7); arrow(c, (150, 392), (150, 351), "TEXT", 1.1, 7)
    lab(c, (160, 226), "D", anchor="start")
    for k in range(12):
        x = 336 + k * 8.2
        arrow(c, (x, 60), (x, 26), "BLUE", 1.1, 6)
    lab(c, (380, 18), sub("T", "o"), size=16)
    lab(c, (316, 70), sub("U", "o"), anchor="end"); lab(c, (448, 74), sub("p", "a"), anchor="start")
    arrow(c, (292, 112), (329, 112), "TEXT", 1.1, 7); arrow(c, (470, 112), (431, 112), "TEXT", 1.1, 7)
    lab(c, (340, 132), "D", anchor="start")
    lab(c, (290, 190), sub("p", "a")); lab(c, (450, 400), sub("p", "a"))
    axes(c, (360, 312), "x", "y", 36)
    REG.put("cl19-statement", c,
            "Elbow of diameter D: at the horizontal inlet an inner stream of diameter D over root 2 at T1 and an outer "
            "coflow at T2, both with Ui and pi; the vertical outlet discharges at Uo and To into pa",
            "Statement figure (redrawn from CL19.pdf, p. 1): pipe of diameter $D$; at the inlet the inner stream (diameter "
            "$D/\\sqrt{2}$, temperature $T_1$) and the outer coflow ($T_2$), both with $U_i$ and $p_i$; outlet at $U_o$, "
            "$T_o$ into the atmosphere at $p_a$")


def cl19_cv():
    c = Canvas(600, 430)
    _cl19_pipe(c, "EDGE", 2.2)
    poly(c, [(104, 254), (316, 254), (326, 244), (326, 62), (434, 62)][:4], "GREEN", 2.0, CV_DASH)
    poly(c, [(104, 346), (416, 346), (426, 336), (426, 62)], "GREEN", 2.0, CV_DASH)
    line(c, (104, 254), (104, 346), "GREEN", 2.0, CV_DASH); line(c, (326, 62), (426, 62), "GREEN", 2.0, CV_DASH)
    sigma(c, (92, 380), "i", "end"); leader(c, (94, 372), (104, 340))
    sigma(c, (440, 48), "o", "start")
    sigma(c, (470, 240), "ℓ", "start"); leader(c, (468, 234), (430, 220))
    normal(c, (104, 300), (-1, 0), length=34, lab_off=(-4, -8), anchor="end")
    normal(c, (376, 62), (0, -1), length=30, lab_off=(12, 6), anchor="start")
    normal(c, (250, 254), (0, -1), length=28, lab_off=(12, 6), anchor="start")
    arrow(c, (150, 300), (215, 300), "BLUE", 2.0, 9); lab(c, (182, 290), sub("U", "i"), "BLUE", size=16)
    arrow(c, (348, 120), (348, 70), "BLUE", 2.0, 9); lab(c, (356, 100), sub("U", "o"), "BLUE", "start", 16)
    axes(c, (500, 400), "x", "y", 36)
    REG.put("cl19-cv", c,
            "Control volume: the air inside the elbow, bounded by the inlet section, the pipe wall and the outlet section",
            "Control volume of the solution: $\\Sigma_i$ (inlet, $\\bar{n} = -\\bar{e}_x$), $\\Sigma_o$ (outlet, "
            "$\\bar{n} = +\\bar{e}_y$) and the pipe wall $\\Sigma_\\ell$, where the force and the heat are collected")


# ----------------------------------------------------------------------------------------- CL10
def _cl10_device(c, col="HEAD", w=2.4):
    """Hood (entrance De at the bottom), neck with the fan, elbow to the exit Ds on the right."""
    left = "M210,330 L210,215 L285,165 L285,95 Q285,40 340,40 L470,40"
    right = "M420,330 L420,215 L345,165 L345,112 Q345,96 361,96 L470,96"
    fill = ("M210,330 L210,215 L285,165 L285,95 Q285,40 340,40 L470,40 L470,96 L361,96 Q345,96 345,112 "
            "L345,165 L420,215 L420,330 Z")
    pathd(c, fill, "none", 0, fill="BLUE", opacity=0.10)
    pathd(c, left, col, w); pathd(c, right, col, w)


def _fan(c, x, y, col="HEAD"):
    """The fan, drawn as the lemniscate of the statement."""
    pts = []
    for k in range(73):
        t = 2 * math.pi * k / 72
        d = 1 + math.sin(t) ** 2
        pts.append((x + 15 * math.cos(t) / d, y + 15 * math.sin(t) * math.cos(t) / d))
    poly(c, pts, col, 1.8, close=True)


def cl10_statement():
    c = Canvas(600, 540)
    _cl10_device(c)
    _fan(c, 315, 135)
    line(c, (196, 332), (434, 332), "TEXT", 1.2, "5,4")
    line(c, (470, 34), (470, 102), "TEXT", 1.2, "4,4")
    flow_arrows(c, 490, 545, [56, 82], "BLUE", 1.5)
    lab(c, (520, 40), sub("U", "s"), size=17); lab(c, (530, 120), sub("p", "a"), anchor="start")
    arrow(c, (440, 4), (440, 39), "TEXT", 1.1, 7); arrow(c, (440, 140), (440, 97), "TEXT", 1.1, 7)
    lab(c, (448, 20), sub("D", "s"), anchor="start")
    lab(c, (250, 40), sub("p", "a"), anchor="end")
    block_arrow_right(c, (278, 135))
    overdot(c, (190, 142), "W", anchor="end", size=19)
    line(c, (213, 280), (296, 280), "TEXT", 1.1); line(c, (334, 280), (417, 280), "TEXT", 1.1)
    arrow_head(c, (240, 280), (211, 280), "TEXT", 7); arrow_head(c, (390, 280), (419, 280), "TEXT", 7)
    lab(c, (315, 274), sub("D", "e"), size=17)
    lab(c, (228, 322), "(e)", italic=False, size=14, anchor="start")
    for x in (232, 266, 300, 334, 368, 402):
        arrow(c, (x, 378), (x, 344), "BLUE", 1.4, 7)
    lab(c, (290, 404), sub("U", "e"), size=16); lab(c, (345, 404), sub("p", "e"), size=16)
    pathd(c, "M70,470 Q210,470 228,420 L232,336", "TEXT", 1.2)
    c.add('<circle cx="70" cy="470" r="2.5" fill="TEXT"/>')
    lab(c, (70, 452), "(0)", italic=False, size=14)
    lab(c, (28, 450), sub("p", "a"), anchor="start"); lab(c, (24, 500), "U ≃ 0", anchor="start", size=16)
    line(c, (226, 438), (250, 470), "TEXT", 1.0); note(c, (252, 486), "streamline", "TEXT", "start", 13)
    axes(c, (520, 320), "x", "y", 36)
    REG.put("cl10-statement", c,
            "Ventilation device: air enters from the room through the entrance of diameter De with Ue, pe, passes a "
            "fan that does work W per unit time, and leaves through the exit pipe of diameter Ds with Us into pa; "
            "a streamline joins the still air (0) to the entrance (e)",
            "Statement figure (redrawn from CL10.pdf, p. 1): entrance section (e) of diameter $D_e$ with $U_e$, $p_e$; fan "
            "supplying the power $\\dot{W}$; exit pipe of diameter $D_s$ discharging at $U_s$ into $p_a$; the streamline "
            "from the still room air (0) ($p_a$, $U \\simeq 0$) to (e)")


def block_arrow_right(c, tip, length=70, half=9, head=20, col="HEAD"):
    x, y = tip
    pts = [(x, y), (x - head, y - half - 6), (x - head, y - half), (x - length, y - half),
           (x - length, y + half), (x - head, y + half), (x - head, y + half + 6)]
    poly(c, pts, col, 1.6, close=True)


def cl10_cv():
    c = Canvas(600, 430)
    _cl10_device(c, "EDGE", 2.2)
    pathd(c, "M214,330 L214,217 L289,167 L289,95 Q289,44 340,44 L466,44 L466,92 L361,92 Q341,92 341,112 "
             "L341,167 L416,217 L416,330 Z", "GREEN", 2.0, CV_DASH)
    _fan(c, 315, 135, "EDGE")
    ellipse(c, 315, 135, 24, 13, "GREEN", 1.6, "4,3")
    sigma(c, (315, 360), "e"); sigma(c, (490, 24), "s", "start"); leader(c, (488, 26), (468, 46))
    sigma(c, (160, 240), "w", "end"); leader(c, (163, 236), (210, 236))
    sigma(c, (390, 150), "m", "start"); leader(c, (388, 146), (338, 138))
    normal(c, (260, 330), (0, 1), length=30, lab_off=(12, 2), anchor="start")
    normal(c, (466, 68), (1, 0), length=30, lab_off=(4, -8), anchor="start")
    arrow(c, (380, 400), (380, 340), "BLUE", 2.0, 9); lab(c, (390, 392), sub("U", "e"), "BLUE", "start", 16)
    arrow(c, (504, 68), (566, 68), "BLUE", 2.0, 9); lab(c, (536, 92), sub("U", "s"), "BLUE", size=16)
    block_arrow_right(c, (284, 135), length=60, half=7, head=16, col="ACC")
    overdot(c, (214, 142), "W", "ACC", "end", 18)
    axes(c, (520, 330), "x", "y", 36)
    REG.put("cl10-cv", c,
            "Control volume: the air inside the device, from the entrance section to the exit section, bounded by the walls "
            "and the fan surface",
            "Control volume of the solution: $\\Sigma_e$ (entrance, $\\bar{n} = -\\bar{e}_y$), $\\Sigma_s$ (exit, "
            "$\\bar{n} = +\\bar{e}_x$), the fixed walls $\\Sigma_w$ and the fan surface $\\Sigma_m$ (dashed around the fan), "
            "through which the power $\\dot{W}$ enters")


# ----------------------------------------------------------------------------------------- CL3
CL3_TOP = "M235,70 L330,70 C372,70 368,230 410,230 L520,230"
CL3_BOT = "M235,120 L300,120 C342,120 338,260 380,260 L520,260"
CL3_BODY = ("M235,70 L330,70 C372,70 368,230 410,230 L520,230 L520,260 L380,260 C338,260 342,120 300,120 "
            "L235,120 Z")


def _break(c, x, y0, y1, col="HEAD", w=1.6):
    """Wavy end of a pipe drawn as cut."""
    m = (y0 + y1) / 2
    pathd(c, f"M{x},{y0} C{x - 10},{y0 + 12} {x + 8},{m - 6} {x},{m} C{x - 8},{m + 6} {x + 10},{y1 - 12} {x},{y1}", col, w)


def _cl3_mouth(c, col="HEAD", w=2.2):
    pathd(c, CL3_BODY, "none", 0, fill="BLUE", opacity=0.10)
    pathd(c, CL3_TOP, col, w); pathd(c, CL3_BOT, col, w)
    _break(c, 235, 70, 120, col); _break(c, 242, 70, 120, col)
    ellipse(c, 520, 245, 5, 15, col, 1.6)


def cl3_statement():
    c = Canvas(620, 310)
    line(c, (20, 70), (150, 70), "HEAD", 2.2); line(c, (20, 120), (150, 120), "HEAD", 2.2)
    rect(c, 20, 70, 130, 50, "none", 0, fill="BLUE", opacity=0.10)
    _break(c, 150, 70, 120)
    _cl3_mouth(c)
    arrow(c, (162, 95), (226, 95), "BLUE", 1.8, 9)
    lab(c, (192, 86), sub("U", "p")); lab(c, (192, 116), sub("p", "p"))
    arrow(c, (262, 40), (262, 69), "TEXT", 1.1, 7); arrow(c, (262, 150), (262, 121), "TEXT", 1.1, 7)
    lab(c, (270, 34), sub("A", "p"), anchor="start")
    c.add('<circle cx="262" cy="95" r="3" fill="ACC"/>')
    arrow(c, (262, 95), (312, 95), "ACC", 2.0, 9); lab(c, (306, 88), vec("F"), "ACC", "start", 17, weight="700")
    arc_arrow(c, (262, 95), 13, 200, -20)
    lab(c, (282, 116), vec("M"), "ACC", "start", 17, weight="700")
    line(c, (360, 95), (560, 95), "TEXT", 1.0, "10,3,2,3"); line(c, (360, 245), (470, 245), "TEXT", 1.0, "10,3,2,3")
    dim(c, (470, 96), (470, 244), "", "TEXT"); lab(c, (478, 175), "H", anchor="start", size=18)
    arrow(c, (500, 202), (500, 229), "TEXT", 1.1, 7); arrow(c, (500, 288), (500, 261), "TEXT", 1.1, 7)
    lab(c, (494, 214), sub("A", "o"), anchor="end")
    arrow(c, (528, 245), (585, 245), "BLUE", 1.8, 9); lab(c, (556, 236), sub("U", "o"))
    lab(c, (420, 292), sub("p", "a"))
    REG.put("cl3-statement", c,
            "Double-elbow mouth piece at the end of a pipe of section Ap: entrance velocity Up and pressure pp, exit "
            "section Ao a height H lower, discharging at Uo into pa; force F and moment M at the entrance section",
            "Statement figure (redrawn from CL3.pdf, p. 1): pipe of section $A_p$ ($U_p$, $p_p$ at the end of the pipe), "
            "mouth piece with two elbows dropping a height $H$ to the exit section $A_o$ ($U_o$, open atmosphere $p_a$); "
            "$F$ and $M$ act at the entrance section")


def cl3_cv():
    c = Canvas(620, 330)
    _cl3_mouth(c, "EDGE", 2.0)
    pathd(c, "M246,74 L330,74 C368,74 364,234 410,234 L516,234", "GREEN", 2.0, CV_DASH)
    pathd(c, "M246,116 L300,116 C346,116 342,256 380,256 L516,256", "GREEN", 2.0, CV_DASH)
    line(c, (246, 74), (246, 116), "GREEN", 2.0, CV_DASH); line(c, (516, 234), (516, 256), "GREEN", 2.0, CV_DASH)
    sigma(c, (232, 40), "p", "end"); leader(c, (230, 46), (246, 76))
    sigma(c, (540, 222), "o", "start")
    sigma(c, (392, 150), "w", "start"); leader(c, (390, 146), (360, 132))
    normal(c, (246, 108), (-1, 0), length=32, lab_off=(-4, 16), anchor="end")
    normal(c, (516, 250), (1, 0), length=32, lab_off=(4, 16), anchor="start")
    normal(c, (300, 70), (0, -1), length=26, lab_off=(12, 6), anchor="start")
    c.add('<circle cx="262" cy="95" r="3.5" fill="HEAD"/>'); lab(c, (256, 140), "O", anchor="end", size=16)
    leader(c, (258, 128), (262, 99), "HEAD")
    line(c, (262, 95), (515, 245), "HEAD", 1.2, "5,4"); arrow_head(c, (262, 95), (515, 245), "HEAD", 9)
    lab(c, (452, 190), vec("x") + sub("", "o"), anchor="start", size=17)
    arrow(c, (170, 270), (210, 270), "HEAD", 1.3, 8); lab(c, (216, 275), "x", anchor="start", size=15)
    arrow(c, (170, 270), (170, 232), "HEAD", 1.3, 8); lab(c, (176, 236), "y", anchor="start", size=15)
    arrow(c, (176, 84), (232, 84), "BLUE", 2.0, 9); lab(c, (202, 74), sub("U", "p"), "BLUE", size=16)
    arrow(c, (552, 245), (606, 245), "BLUE", 2.0, 9); lab(c, (580, 272), sub("U", "o"), "BLUE", size=16)
    REG.put("cl3-cv", c,
            "Control volume: the water inside the mouth piece, from the entrance section to the exit section; origin O at "
            "the centre of the entrance section and position of the exit centre",
            "Control volume of the solution: $\\Sigma_p$ (entrance, $\\bar{n} = -\\bar{e}_x$), $\\Sigma_o$ (exit, "
            "$\\bar{n} = +\\bar{e}_x$) and the inner wall $\\Sigma_w$; origin $O$ at the centre of the entrance section, "
            "exit centre at $\\bar{x}_o = X\\bar{e}_x - H\\bar{e}_y$ (moments about $O$)")


# ----------------------------------------------------------------------------------------- CL8
CL8_UP = ((130, 210), (300, 210), (356, 190), (360, 40))
CL8_DN = ((130, 270), (300, 270), (356, 290), (360, 440))


def _cl8_wall(c, col="HEAD"):
    rect(c, 376, 30, 8, 192, "none", 0, fill=col)
    rect(c, 376, 258, 8, 182, "none", 0, fill=col)


def _cl8_jet(c, col="HEAD", w=1.8):
    up, dn = cubic(*CL8_UP), cubic(*CL8_DN)
    poly(c, up + [(376, 40), (376, 440)] + dn[::-1], "none", 0, fill="BLUE", opacity=0.12, close=True)
    rect(c, 376, 228, 184, 24, "none", 0, fill="BLUE", opacity=0.12)
    poly(c, up, col, w); poly(c, dn, col, w)
    line(c, (384, 228), (560, 228), col, w); line(c, (384, 252), (560, 252), col, w)
    ellipse(c, 130, 240, 7, 30, col, 1.6)


def cl8_statement():
    c = Canvas(620, 480)
    _cl8_jet(c)
    _cl8_wall(c)
    line(c, (100, 240), (590, 240), "TEXT", 1.0, "10,3,2,3"); arrow_head(c, (560, 240), (600, 240), "TEXT", 9)
    flow_arrows(c, 72, 124, [226, 254])
    lab(c, (64, 236), sub("V", "j"), anchor="end")
    arrow(c, (130, 172), (130, 209), "TEXT", 1.1, 7); arrow(c, (130, 308), (130, 271), "TEXT", 1.1, 7)
    lab(c, (140, 192), sub("D", "j"), anchor="start")
    arrow(c, (368, 60), (368, 16), "BLUE", 1.6, 8); lab(c, (356, 26), sub("V", "r"), anchor="end")
    arrow(c, (318, 426), (358, 426), "TEXT", 1.1, 7); arrow(c, (420, 426), (377, 426), "TEXT", 1.1, 7)
    lab(c, (312, 432), "h(r)", anchor="end")
    arrow(c, (530, 196), (530, 227), "TEXT", 1.1, 7); arrow(c, (530, 284), (530, 253), "TEXT", 1.1, 7)
    lab(c, (522, 210), sub("D", "s"), anchor="end"); lab(c, (585, 226), sub("V", "s"), anchor="start")
    lab(c, (260, 130), sub("p", "a")); lab(c, (470, 300), sub("p", "a"))
    arrow(c, (24, 150), (78, 150), "HEAD", 1.4, 8); lab(c, (50, 140), vec("e") + sub("", "x"), size=16)
    REG.put("cl8-statement", c,
            "Circular jet of diameter Dj and velocity Vj hitting a wall with a coaxial orifice of diameter Ds: a secondary "
            "jet Vs crosses the orifice and the rest spreads as a radial wall jet of velocity Vr and thickness h(r)",
            "Statement figure (redrawn from CL8.pdf, p. 1, axial section): incoming jet $D_j$, $V_j$; orifice of diameter "
            "$D_s$ with the secondary jet $V_s$; radial wall jet $V_r$ of thickness $h(r)$; ambient pressure $p_a$ on both "
            "sides of the wall")


def cl8_cv():
    c = Canvas(620, 480)
    _cl8_jet(c, "EDGE", 1.6)
    _cl8_wall(c, "EDGE")
    up = [(x + 3, y + 3) for x, y in cubic(*CL8_UP, n=120) if x >= 150 and y >= 70]
    dn = [(x + 3, y - 3) for x, y in cubic(*CL8_DN, n=120) if x >= 150 and y <= 410]
    cv = [up[0]] + up + [(373, 70), (373, 225), (530, 231), (530, 249), (373, 255), (373, 410)] + dn[::-1]
    poly(c, cv[:1] + up + [(373, 70), (373, 225)], "GREEN", 2.0, CV_DASH)
    poly(c, [(373, 225), (384, 231), (530, 231), (530, 249), (384, 249), (373, 255), (373, 410)], "GREEN", 2.0, CV_DASH)
    poly(c, [(373, 410)] + dn[::-1] + [up[0]], "GREEN", 2.0, CV_DASH)
    sigma(c, (120, 330), "j", "end"); leader(c, (122, 322), (152, 262))
    sigma(c, (300, 74), "r", "end"); leader(c, (302, 72), (366, 70))
    sigma(c, (300, 422), "r", "end"); leader(c, (302, 416), (366, 410))
    pa = min(cubic(*CL8_UP, n=120), key=lambda q: abs(q[0] - 262))
    sigma(c, (240, 176), "a", "end"); leader(c, (242, 178), (pa[0], pa[1] - 1))
    sigma(c, (470, 286), "a", "start"); leader(c, (472, 280), (450, 250))
    sigma(c, (546, 214), "s", "start")
    sigma(c, (420, 150), "w", "start"); leader(c, (418, 146), (376, 140))
    normal(c, (153, 252), (-1, 0), length=32, lab_off=(-4, 16), anchor="end")
    normal(c, (530, 246), (1, 0), length=30, lab_off=(4, 18), anchor="start")
    normal(c, (366, 70), (0, -1), length=28, lab_off=(-6, 4), anchor="end")
    normal(c, (366, 410), (0, 1), length=28, lab_off=(-6, 12), anchor="end")
    arrow(c, (56, 226), (114, 226), "BLUE", 2.0, 9); lab(c, (84, 216), sub("V", "j"), "BLUE", size=16)
    arrow(c, (568, 234), (614, 234), "BLUE", 2.0, 9)
    arrow(c, (440, 98), (500, 98), "ACC", 2.6, 11); lab(c, (506, 104), vec("F") + sub("", "w"), "ACC", "start", 18, weight="700")
    note(c, (470, 124), "force on the wall", "ACC", "middle", 12)
    REG.put("cl8-cv", c,
            "Control volume around the water: incoming jet section, free surfaces, the two cuts across the wall jet at "
            "radius r, the wetted wall and the section of the secondary jet",
            "Control volume of the solution: $\\Sigma_j$ (incoming jet, $\\bar{n} = -\\bar{e}_x$), $\\Sigma_s$ (secondary "
            "jet, $\\bar{n} = +\\bar{e}_x$), $\\Sigma_r$ (cylinder of radius $r$ across the wall jet, $\\bar{n} = \\bar{e}_r$; "
            "its two traces in this section), the free surfaces $\\Sigma_a$ at $p_a$ and the wetted wall $\\Sigma_w$; "
            "$\\bar{F}_w$ is the force on the wall")


# ----------------------------------------------------------------------------------------- shared (Lote 3)
def hollow_arrow(c, tail, d, length=56, half=5, head=13, col="HEAD"):
    """Hollow arrow from `tail` along direction d (a flow rate leaving or entering)."""
    L = math.hypot(*d)
    t = (d[0] / L, d[1] / L)
    m = (-t[1], t[0])

    def P(a, b):
        return (tail[0] + t[0] * a + m[0] * b, tail[1] + t[1] * a + m[1] * b)
    pts = [P(0, -half), P(length - head, -half), P(length - head, -half - 5), P(length, 0),
           P(length - head, half + 5), P(length - head, half), P(0, half)]
    poly(c, pts, col, 1.5, close=True)


def angle_arc(c, centre, r, a0, a1, col="TEXT", w=1.1):
    """Arc between two directions given in degrees (counter-clockwise, screen y up)."""
    p0 = (centre[0] + r * math.cos(math.radians(a0)), centre[1] - r * math.sin(math.radians(a0)))
    p1 = (centre[0] + r * math.cos(math.radians(a1)), centre[1] - r * math.sin(math.radians(a1)))
    sweep = 0 if a1 > a0 else 1
    pathd(c, f"M{fmt(p0[0])},{fmt(p0[1])} A{fmt(r)},{fmt(r)} 0 0,{sweep} {fmt(p1[0])},{fmt(p1[1])}", col, w)


# ----------------------------------------------------------------------------------------- CL16
CL16_O, CL16_L, CL16_TH, CL16_H, CL16_H1, CL16_H2 = (300, 215), 180, 24, 20, 18, 22


def _cl16_geom():
    o, th = CL16_O, math.radians(CL16_TH)
    t1, t2 = (math.cos(th), -math.sin(th)), (math.cos(2 * th), math.sin(2 * th))
    m1, m2 = (-math.sin(th), -math.cos(th)), (-math.sin(2 * th), math.cos(2 * th))

    def P(t, m, s, eta):
        return (o[0] + t[0] * s + m[0] * eta, o[1] + t[1] * s + m[1] * eta)
    s1w, s2w = CL16_L / math.cos(th), CL16_L / math.cos(2 * th)
    return t1, t2, m1, m2, P, s1w, s2w


def _cl16_shapes(c, edges=True):
    o = CL16_O
    t1, t2, m1, m2, P, s1w, s2w = _cl16_geom()
    s1e, s2e = s1w + 62, s2w + 48
    poly(c, [o, P(t1, m1, s1w, 0), P(t2, m2, s2w, 0)], "TEXT" if edges else "EDGE", 1.6, fill="TEXT", opacity=0.14,
         close=True)
    band = [(80, o[1] - CL16_H), (270, o[1] - CL16_H), P(t1, m1, 0, CL16_H1), P(t1, m1, s1e, CL16_H1), P(t1, m1, s1e, 0),
            o, P(t2, m2, s2e, 0), P(t2, m2, s2e, CL16_H2), P(t2, m2, 0, CL16_H2), (270, o[1] + CL16_H), (80, o[1] + CL16_H)]
    poly(c, band, "HEAD" if edges else "none", 1.4 if edges else 0, fill="BLUE", opacity=0.30, close=True)
    return band, s1e, s2e


def cl16_statement():
    c = Canvas(640, 500)
    o = CL16_O
    t1, t2, m1, m2, P, s1w, s2w = _cl16_geom()
    band, s1e, s2e = _cl16_shapes(c)
    line(c, (30, o[1]), (o[0] - 8, o[1]), "TEXT", 1.0, "10,3,2,3")
    hollow_arrow(c, (18, o[1]), (1, 0), length=80, half=4, head=12)
    lab(c, (40, o[1] - 26), "Q"); lab(c, (66, o[1] + 46), "v, " + sub("T", "0"), anchor="end")
    arrow(c, (140, 150), (140, 193), "TEXT", 1.1, 7); arrow(c, (140, 285), (140, 237), "TEXT", 1.1, 7)
    lab(c, (148, 168), "h", anchor="start")
    arrow(c, (200, o[1]), (200, 168), "HEAD", 1.2, 7); lab(c, (206, 176), "y", anchor="start", size=16)
    arrow(c, (200, o[1]), (250, o[1]), "HEAD", 1.2, 7); lab(c, (234, o[1] - 6), "x", size=16)
    lab(c, (292, o[1] + 40), vec("x") + sub("", "0"), anchor="end")
    dim(c, (o[0] + 2, o[1]), (o[0] + CL16_L, o[1]), "", "TEXT"); lab(c, (410, o[1] + 22), "L")
    angle_arc(c, o, 44, 0, CL16_TH); lab(c, (o[0] + 54, o[1] - 6), "θ", anchor="start")
    angle_arc(c, o, 34, 0, -2 * CL16_TH); lab(c, (o[0] + 42, o[1] + 36), "2θ", anchor="start")
    for k in range(4):
        a = P(t1, m1, 120 + 14 * k, 30)
        arrow(c, a, P(t1, m1, 120 + 14 * k, 4), "PINK", 1.3, 7)
    lab(c, P(t1, m1, 150, -26), "q", "PINK")
    for k in range(4):
        a = P(t2, m2, 150 + 14 * k, -30)
        arrow(c, P(t2, m2, 150 + 14 * k, -2), a, "PINK", 1.3, 7)
    lab(c, P(t2, m2, 190, -42), "q", "PINK", anchor="start")
    e1, e2 = P(t1, m1, s1e - 30, CL16_H1 / 2), P(t2, m2, s2e - 30, CL16_H2 / 2)
    hollow_arrow(c, e1, t1, length=58, half=4, head=12); hollow_arrow(c, e2, t2, length=58, half=4, head=12)
    lab(c, P(t1, m1, s1e - 40, CL16_H1 + 14), sub("T", "1"), anchor="end")
    lab(c, (e1[0] + 64, e1[1] + 4), "αQ", anchor="start")
    lab(c, P(t2, m2, s2e - 60, -16), sub("T", "2"), anchor="start")
    lab(c, (e2[0] + 46, e2[1] + 40), "(1 − α)Q", anchor="start")
    lab(c, (390, 90), sub("p", "a")); lab(c, (585, 222), sub("p", "a")); lab(c, (200, 330), sub("p", "a"))
    REG.put("cl16-statement", c,
            "Plane jet of thickness h, flux Q, velocity v and temperature T0 hitting a wedge with its corner at x0: a part "
            "alpha Q leaves along the face at angle theta (temperature T1) and the rest along the face at angle 2 theta "
            "(T2); the faces end a distance L from the corner; heat q crosses the wetted faces",
            "Statement figure (redrawn from CL16.pdf, p. 1): plane jet ($h$, $Q$, $v$, $T_0$) on the wedge with corner "
            "$\\bar{x}_0$; the layer $\\alpha Q$ ($T_1$) leaves at $\\theta$ and $(1 - \\alpha)Q$ ($T_2$) at $2\\theta$; "
            "faces of horizontal extent $L$; heat flux $q$ into the wedge; ambient $p_a$")


def cl16_cv():
    c = Canvas(640, 500)
    o = CL16_O
    t1, t2, m1, m2, P, s1w, s2w = _cl16_geom()
    band, s1e, s2e = _cl16_shapes(c, edges=False)
    s1c, s2c = s1e - 14, s2e - 14
    cv = [(96, o[1] - CL16_H), (270, o[1] - CL16_H), P(t1, m1, 0, CL16_H1), P(t1, m1, s1c, CL16_H1), P(t1, m1, s1c, 0),
          o, P(t2, m2, s2c, 0), P(t2, m2, s2c, CL16_H2), P(t2, m2, 0, CL16_H2), (270, o[1] + CL16_H),
          (96, o[1] + CL16_H)]
    poly(c, cv, "GREEN", 2.0, CV_DASH, close=True)
    sigma(c, (86, o[1] + 50), "0", "end"); leader(c, (88, o[1] + 42), (96, o[1] + 14))
    sigma(c, P(t1, m1, s1c + 4, CL16_H1 + 26), "1", "start")
    sigma(c, P(t2, m2, s2c + 26, -8), "2", "start")
    sigma(c, (200, 166), "a"); leader(c, (200, 172), (210, o[1] - CL16_H))
    sigma(c, P(t2, m2, 110, CL16_H2 + 28), "a", "end"); leader(c, P(t2, m2, 110, CL16_H2 + 22), P(t2, m2, 110, CL16_H2))
    sigma(c, (420, 230), "w", "start"); leader(c, (418, 226), P(t1, m1, 120, 0)); leader(c, (430, 236), P(t2, m2, 150, 0))
    normal(c, (96, o[1] + 8), (-1, 0), length=30, lab_off=(-4, 5), anchor="end")
    normal(c, P(t1, m1, s1c, CL16_H1 / 2), t1, label=vec("t") + sub("", "1"), length=30, lab_off=(6, -4), anchor="start")
    normal(c, P(t2, m2, s2c, CL16_H2 / 2), t2, label=vec("t") + sub("", "2"), length=30, lab_off=(6, 12), anchor="start")
    a = P(t1, m1, 60, CL16_H1)
    arrow(c, a, (a[0] + m1[0] * 30, a[1] + m1[1] * 30), "HEAD", 1.3, 7)
    lab(c, (a[0] + m1[0] * 30 - 4, a[1] + m1[1] * 30 - 6), vec("m") + sub("", "1"), anchor="end", size=15)
    b = P(t2, m2, 60, CL16_H2)
    arrow(c, b, (b[0] + m2[0] * 30, b[1] + m2[1] * 30), "HEAD", 1.3, 7)
    lab(c, (b[0] + m2[0] * 30 - 4, b[1] + m2[1] * 30 + 14), vec("m") + sub("", "2"), anchor="end", size=15)
    c.add(f'<circle cx="{o[0]}" cy="{o[1]}" r="3.5" fill="HEAD"/>')
    lab(c, (o[0] + 12, o[1] + 6), vec("x") + sub("", "0"), anchor="start", size=16)
    arrow(c, (24, o[1] - 34), (74, o[1] - 34), "BLUE", 2.0, 9); lab(c, (48, o[1] - 44), "v", "BLUE", size=16)
    axes(c, (40, 440), "x", "y", 36)
    REG.put("cl16-cv", c,
            "Control volume around the liquid: the incoming jet section, the free surfaces, the two sections across the "
            "deflected layers and the wetted faces of the wedge",
            "Control volume of the solution: $\\Sigma_0$ (incoming jet, $\\bar{n} = -\\bar{e}_x$), $\\Sigma_1$ and "
            "$\\Sigma_2$ (sections across the layers, $\\bar{n} = \\bar{t}_1$, $\\bar{t}_2$), the free surfaces $\\Sigma_a$ "
            "at $p_a$ and the wetted faces $\\Sigma_w$; $\\bar{m}_1$, $\\bar{m}_2$ are the unit normals pointing away from "
            "the wedge, and moments are taken about the corner $\\bar{x}_0$")


# ----------------------------------------------------------------------------------------- CL18
CL18_FILL = "M40,30 C150,50 200,90 200,170 L200,470 L330,470 L330,170 C330,90 380,50 490,30 Z"


def _cl18_ejector(c, col="HEAD", w=2.2):
    pathd(c, CL18_FILL, "none", 0, fill="BLUE", opacity=0.10)
    pathd(c, "M40,30 C150,50 200,90 200,170 L200,470", col, w)
    pathd(c, "M490,30 C380,50 330,90 330,170 L330,470", col, w)
    poly(c, [(520, 118), (250, 118), (250, 172)], col, 1.8)
    poly(c, [(520, 132), (264, 132), (264, 172)], col, 1.8)
    line(c, (200, 470), (200, 540), "TEXT", 1.1, "2,4"); line(c, (330, 470), (330, 540), "TEXT", 1.1, "2,4")


def cl18_statement():
    c = Canvas(540, 560)
    _cl18_ejector(c)
    line(c, (200, 176), (330, 176), "TEXT", 1.0, "4,3")
    for x in list(range(208, 247, 9)) + list(range(272, 326, 9)):
        arrow(c, (x, 178), (x, 200), "BLUE", 1.1, 6)
    for x in (253, 257, 261):
        arrow(c, (x, 176), (x, 236), "BLUE", 1.1, 6)
    lab(c, (222, 222), sub("p", "e"), size=16); lab(c, (302, 222), sub("U", "e"), size=16)
    lab(c, (268, 246), sub("U", "j"), anchor="start", size=16)
    arrow(c, (226, 150), (249, 150), "TEXT", 1.1, 7); arrow(c, (290, 150), (265, 150), "TEXT", 1.1, 7)
    lab(c, (296, 156), sub("A", "j"), anchor="start", size=16)
    lab(c, (265, 70), sub("p", "a"))
    rect(c, 204, 179, 122, 289, "HEAD", 1.2, "5,4")
    lab(c, (360, 380), sub("V", "c"), anchor="start", size=16); line(c, (358, 374), (328, 360), "HEAD", 1.0)
    arrow(c, (204, 290), (172, 290), "HEAD", 1.3, 8); lab(c, (178, 280), vec("n"), size=15)
    arrow(c, (326, 290), (358, 290), "HEAD", 1.3, 8); lab(c, (352, 280), vec("n"), size=15)
    line(c, (206, 320), (250, 320), "TEXT", 1.1); line(c, (282, 320), (324, 320), "TEXT", 1.1)
    arrow_head(c, (230, 320), (205, 320), "TEXT", 7); arrow_head(c, (300, 320), (325, 320), "TEXT", 7)
    lab(c, (266, 326), "A", size=17)
    for x in range(208, 326, 9):
        arrow(c, (x, 474), (x, 500), "BLUE", 1.1, 6)
    lab(c, (190, 494), sub("p", "a"), anchor="end", size=16); lab(c, (300, 524), sub("U", "o"), size=16)
    REG.put("cl18-statement", c,
            "Ejector: a container at pa drains through a vertical pipe of section A; an injector tube brings the jet of "
            "section Aj and velocity Uj to the axis of the entrance section, where the surrounding liquid enters at Ue, pe; "
            "the control volume Vc spans the pipe and the mixed jet leaves at Uo into pa",
            "Statement figure (redrawn from CL18.pdf, p. 1): container at $p_a$, pipe of section $A$; jet $A_j$, $U_j$ "
            "injected on the axis; entrance section with $U_e$, $p_e$ around the jet; control volume $V_c$ with outward "
            "normals; uniform outlet jet $U_o$ into $p_a$")


def cl18_cv():
    c = Canvas(540, 560)
    _cl18_ejector(c, "EDGE", 2.0)
    rect(c, 204, 176, 122, 294, "GREEN", 2.0, CV_DASH)
    sigma(c, (150, 182), "e", "end"); leader(c, (152, 178), (204, 178))
    sigma(c, (372, 470), "o", "start"); leader(c, (370, 466), (328, 470))
    sigma(c, (372, 320), "w", "start"); leader(c, (370, 316), (330, 316))
    normal(c, (225, 176), (0, -1), length=30, lab_off=(-8, 4), anchor="end")
    normal(c, (240, 470), (0, 1), length=30, lab_off=(-8, 4), anchor="end")
    normal(c, (204, 360), (-1, 0), length=30, lab_off=(-4, -8), anchor="end")
    arrow(c, (288, 206), (288, 240), "BLUE", 1.8, 8); lab(c, (296, 236), sub("U", "e"), "BLUE", "start", 15)
    arrow(c, (257, 176), (257, 260), "BLUE", 2.0, 9); lab(c, (248, 252), sub("U", "j"), "BLUE", "end", 15)
    arrow(c, (290, 474), (290, 530), "BLUE", 2.0, 9); lab(c, (298, 520), sub("U", "o"), "BLUE", "start", 15)
    arrow(c, (470, 200), (470, 250), "HEAD", 1.3, 8); lab(c, (478, 240), vec("e") + sub("", "x"), anchor="start", size=16)
    REG.put("cl18-cv", c,
            "Control volume: the pipe between the entrance section (jet and annulus) and the outlet section, bounded by "
            "the straight pipe wall",
            "Control volume of the solution: $\\Sigma_e$ (entrance, $\\bar{n} = -\\bar{e}_x$, made of the jet $A_j$ and the "
            "annulus $A - A_j$), $\\Sigma_o$ (outlet, $\\bar{n} = +\\bar{e}_x$) and the straight wall $\\Sigma_w$ "
            "($\\bar{n}\\perp\\bar{e}_x$); $\\bar{e}_x$ points along the flow")


# ----------------------------------------------------------------------------------------- CL9
CL9_UP, CL9_DN = "M156,34 Q330,40 444,100", "M156,214 Q330,208 444,148"


def _cl9_nozzle(c, col="HEAD", w=2.2):
    pathd(c, "M156,34 Q330,40 444,100 L444,148 Q330,208 156,214 Z", "none", 0, fill="BLUE", opacity=0.10)
    pathd(c, CL9_UP, col, w); pathd(c, CL9_DN, col, w)


def _propeller(c, x, y, col="HEAD"):
    ellipse(c, x, y - 36, 5, 34, col, 1.5); ellipse(c, x, y + 36, 5, 34, col, 1.5)


def cl9_statement():
    c = Canvas(620, 250)
    _cl9_nozzle(c)
    line(c, (20, 124), (600, 124), "TEXT", 1.0, "10,3,2,3")
    for y0, y1 in ((10, 60), (40, 92), (208, 156), (238, 188)):
        pathd(c, f"M30,{y0} C90,{y0} 100,{y1} 150,{y1}", "TEXT", 1.2)
        arrow_head(c, (130, y1), (150, y1), "TEXT", 7)
    c.add('<circle cx="22" cy="124" r="3.5" fill="HEAD"/><circle cx="158" cy="124" r="3.5" fill="HEAD"/>'
          '<circle cx="446" cy="124" r="3.5" fill="HEAD"/>')
    lab(c, (24, 112), sub("p", "∞"), anchor="start", size=16); lab(c, (24, 144), "1", anchor="start", size=14)
    lab(c, (80, 146), "ρ", size=16); lab(c, (80, 182), "μ", size=16)
    lab(c, (156, 24), sub("A", "e"), size=16); lab(c, (170, 88), sub("U", "e"), anchor="start", size=16)
    lab(c, (170, 112), sub("p", "e"), anchor="start", size=16); lab(c, (164, 142), "e", anchor="start", size=15)
    _propeller(c, 262, 124)
    arc_arrow(c, (262, 92), 18, 60, -60, "ACC", 1.6)
    overdot(c, (292, 92), "W", "ACC", "start", 17)
    hollow_arrow(c, (400, 124), (-1, 0), length=66, half=8, head=18, col="HEAD")
    lab(c, (372, 100), "T", size=18)
    lab(c, (446, 90), sub("A", "s"), anchor="start", size=16); lab(c, (430, 118), sub("p", "s"), anchor="end", size=15)
    lab(c, (450, 142), "s", anchor="start", size=15)
    flow_arrows(c, 452, 520, [106, 116, 132, 142], "BLUE", 1.4)
    lab(c, (530, 118), sub("U", "s"), anchor="start", size=16)
    REG.put("cl9-statement", c,
            "Submarine propulsion device: a nozzle with inlet area Ae and outlet area As, a propeller inside driven with "
            "power W, thrust T; streamlines from the still water at point 1 (p infinity) reach the inlet e at Ue, pe; the "
            "jet leaves the outlet s at Us",
            "Statement figure (redrawn from CL9.pdf, p. 1): nozzle of inlet area $A_e$ ($U_e$, $p_e$) and outlet area "
            "$A_s$ ($U_s$, $p_s$); propeller supplying the power $\\dot{W}$; thrust $T$; the streamline from the still "
            "water at point 1 ($p_\\infty$) to the inlet $e$")


def cl9_cv():
    c = Canvas(620, 250)
    _cl9_nozzle(c, "EDGE", 2.0)
    pathd(c, "M160,38 Q330,44 440,102 L440,146 Q330,204 160,210 Z", "GREEN", 2.0, CV_DASH)
    _propeller(c, 262, 124, "EDGE")
    ellipse(c, 262, 124, 12, 76, "GREEN", 1.5, "4,3")
    sigma(c, (150, 236), "e", "end"); leader(c, (152, 230), (160, 200))
    sigma(c, (470, 82), "s", "start"); leader(c, (468, 86), (442, 110))
    sigma(c, (360, 236), "w", "start"); leader(c, (358, 230), (340, 196))
    sigma(c, (290, 230), "p", "end"); leader(c, (288, 224), (270, 196))
    normal(c, (160, 150), (-1, 0), length=30, lab_off=(-4, -6), anchor="end")
    normal(c, (440, 136), (1, 0), length=30, lab_off=(4, 14), anchor="start")
    normal(c, (315, 55), (0.22, -0.97), length=26, lab_off=(10, 6), anchor="start")
    arrow(c, (40, 100), (100, 100), "BLUE", 2.0, 9); lab(c, (70, 90), sub("U", "e"), "BLUE", size=16)
    arrow(c, (500, 124), (566, 124), "BLUE", 2.0, 9); lab(c, (533, 114), sub("U", "s"), "BLUE", size=16)
    arrow(c, (400, 124), (340, 124), "ACC", 2.6, 11)
    lab(c, (370, 104), vec("F") + " = −T " + vec("e") + sub("", "x"), "ACC", "middle", 15, weight="700")
    arrow(c, (40, 200), (82, 200), "HEAD", 1.3, 8); lab(c, (88, 205), vec("e") + sub("", "x"), anchor="start", size=15)
    REG.put("cl9-cv", c,
            "Control volume: the water inside the nozzle between the inlet and outlet sections, bounded by the nozzle walls "
            "and the propeller surface",
            "Control volume of the solution: $\\Sigma_e$ (inlet, $\\bar{n} = -\\bar{e}_x$), $\\Sigma_s$ (outlet, "
            "$\\bar{n} = +\\bar{e}_x$), the fixed nozzle walls $\\Sigma_w$ and the moving propeller $\\Sigma_p$ (dashed "
            "around it); the force of the water on the device is $\\bar{F} = -T\\bar{e}_x$")


# ----------------------------------------------------------------------------------------- CL14
def _cl14_section(c, col="HEAD", w=2.4):
    yc, ro, ri = 150, 130, 55
    rect(c, 230, yc - ro, 460, 2 * ro, "none", 0, fill="BLUE", opacity=0.10)
    hub = [(230, yc - ri), (330, yc - ri), (440, yc), (330, yc + ri), (230, yc + ri)]
    poly(c, hub, "none", 0, fill="TEXT", opacity=0.16, close=True)
    line(c, (230, yc - ro), (690, yc - ro), col, w); line(c, (230, yc + ro), (690, yc + ro), col, w)
    poly(c, hub, col, 1.6)
    for y0, y1 in ((yc - ro, yc - ri), (yc + ri, yc + ro)):
        rect(c, 280, y0, 8, y1 - y0, col, 1.3, fill="none")
    return yc, ro, ri


def cl14_statement():
    c = Canvas(760, 300)
    yc, ro, ri = _cl14_section(c)
    ellipse(c, 90, yc, 62, 120, "HEAD", 1.4); ellipse(c, 90, yc, 24, 52, "HEAD", 1.4)
    ellipse(c, 90, yc, 42, 86, "TEXT", 1.2, "4,4")
    arrow(c, (90, yc), (90, yc - 90), "HEAD", 1.2, 7); lab(c, (80, yc - 70), "r", anchor="end", size=16)
    arrow(c, (90, yc), (196, yc), "HEAD", 1.2, 7); lab(c, (200, yc + 20), "z", anchor="start", size=16)
    arrow(c, (118, yc - 82), (158, yc - 82), "BLUE", 1.4, 7); lab(c, (162, yc - 92), sub("u", "1"), "BLUE", "start", 16)
    arrow(c, (118, yc - 82), (136, yc - 58), "BLUE", 1.4, 7); lab(c, (114, yc - 60), sub("u", "θ"), "BLUE", "end", 16)
    lab(c, (150, yc + 98), sub("p", "1"), anchor="start", size=16); lab(c, (150, yc + 122), sub("ρ", "1"), anchor="start", size=16)
    line(c, (230, yc - ro), (230, yc - ri), "TEXT", 1.2, "4,3"); line(c, (230, yc + ri), (230, yc + ro), "TEXT", 1.2, "4,3")
    line(c, (690, yc - ro), (690, yc + ro), "TEXT", 1.2, "4,3")
    line(c, (230, yc), (690, yc), "TEXT", 1.0, "10,3,2,3")
    flow_arrows(c, 192, 226, [yc - 115, yc - 95, yc - 75, yc + 75, yc + 95, yc + 115], "BLUE", 1.3)
    flow_arrows(c, 694, 728, [yc - 115, yc - 95, yc - 75, yc - 55, yc - 35, yc + 35, yc + 55, yc + 75, yc + 95, yc + 115],
                "BLUE", 1.3)
    lab(c, (735, yc - 108), sub("u", "2"), anchor="start", size=16); lab(c, (735, yc - 86), sub("p", "2"), anchor="start", size=16)
    lab(c, (735, yc - 64), sub("ρ", "2"), anchor="start", size=16)
    note(c, (300, yc - 98), "stator", "HEAD", "start", 13); line(c, (298, yc - 102), (288, yc - 92), "HEAD", 1.0)
    note(c, (300, yc + 108), "stator", "HEAD", "start", 13); line(c, (298, yc + 102), (288, yc + 92), "HEAD", 1.0)
    note(c, (390, yc - 60), "conical diffuser", "HEAD", "start", 13); line(c, (388, yc - 56), (372, yc - 36), "HEAD", 1.0)
    dim(c, (246, yc), (246, yc - ri), "", "TEXT"); lab(c, (252, yc - 22), sub("R", "i"), anchor="start", size=16)
    dim(c, (560, yc), (560, yc - ro), "", "TEXT"); lab(c, (566, yc - 70), sub("R", "o"), anchor="start", size=16)
    REG.put("cl14-statement", c,
            "Diffuser module: front view of the inlet annulus with the axial and azimuthal velocity components u1, u theta, "
            "and axial section with the fixed stator of inner and outer radii Ri, Ro, the conical diffuser and the exit "
            "with u2, p2, rho2",
            "Statement figure (redrawn from CL14.pdf, p. 1): front view of the inlet ($u_1$, $u_\\theta$, $p_1$, $\\rho_1$) "
            "and axial section of the module: fixed stator between $R_i$ and $R_o$, conical diffuser, purely axial exit "
            "$u_2$, $p_2$, $\\rho_2$")


def cl14_cv():
    c = Canvas(700, 350)
    c.add('<g transform="translate(0,30)">')
    yc, ro, ri = _cl14_section(c, "EDGE", 2.0)
    poly(c, [(234, yc - ri - 4), (234, yc - ro + 4), (686, yc - ro + 4), (686, yc + ro - 4), (234, yc + ro - 4),
             (234, yc + ri + 4), (329, yc + ri + 4), (434, yc + 2), (434, yc - 2), (329, yc - ri - 4), (234, yc - ri - 4)],
         "GREEN", 2.0, CV_DASH)
    for y0, y1 in ((yc - ro + 4, yc - ri - 4), (yc + ri + 4, yc + ro - 4)):
        rect(c, 276, y0 + 3, 16, y1 - y0 - 6, "GREEN", 1.6, "4,3", rx=4)
    sigma(c, (220, 30), "in", "end"); leader(c, (222, 34), (234, 50))
    sigma(c, (660, 304), "out", "end"); leader(c, (662, 300), (686, 270))
    sigma(c, (500, 4), "w", "start"); leader(c, (498, 0), (480, yc - ro + 4)); leader(c, (508, 8), (420, yc - 18))
    sigma(c, (330, 304), "a", "start"); leader(c, (328, 298), (292, 260))
    normal(c, (234, 66), (-1, 0), length=30, lab_off=(-4, -6), anchor="end")
    normal(c, (686, 66), (1, 0), length=30, lab_off=(4, -6), anchor="start")
    normal(c, (600, yc - ro + 4), (0, -1), length=24, lab_off=(12, 6), anchor="start")
    arrow(c, (150, 236), (226, 236), "BLUE", 2.0, 9); lab(c, (188, 226), vec("v") + sub("", "1"), "BLUE", size=16)
    arrow(c, (600, yc + 60), (660, yc + 60), "BLUE", 2.0, 9); lab(c, (630, yc + 50), vec("v") + sub("", "2"), "BLUE", size=16)
    line(c, (230, yc), (690, yc), "TEXT", 1.0, "10,3,2,3")
    arrow(c, (40, 300), (84, 300), "HEAD", 1.3, 8); lab(c, (90, 305), vec("e") + sub("", "z"), anchor="start", size=15)
    arrow(c, (40, 300), (40, 258), "HEAD", 1.3, 8); lab(c, (46, 262), vec("e") + sub("", "r"), anchor="start", size=15)
    c.add("</g>")
    REG.put("cl14-cv", c,
            "Control volume in the axial section: inlet annulus, exit disc, the casing and cone walls and the surfaces "
            "around the stator aerofoils",
            "Control volume of the solution (axial section): $\\Sigma_{in}$ (inlet annulus, $\\bar{n} = -\\bar{e}_z$), "
            "$\\Sigma_{out}$ (exit disc, $\\bar{n} = +\\bar{e}_z$), $\\Sigma_w$ (inner wall of the casing and outer wall "
            "of the cone) and $\\Sigma_a$ (around the stator aerofoils); all are fixed")


# ----------------------------------------------------------------------------------------- CL1
CL1_YC, CL1_YM, CL1_Y0 = 165, 45, 130


def _cl1_streamline(sign):
    yc, ym, y0 = CL1_YC, CL1_YM, CL1_Y0
    return cubic((110, yc - sign * ym), (300, yc - sign * ym), (340, yc - sign * y0), (480, yc - sign * y0), 50)


def _cl1_airfoil(c, col="HEAD", fill="TEXT"):
    pathd(c, "M205,165 C205,145 240,150 305,165 C240,180 205,185 205,165 Z", col, 1.6, fill=fill, opacity=0.25)


def cl1_statement():
    c = Canvas(620, 330)
    yc = CL1_YC
    line(c, (60, 20), (60, 312), "HEAD", 1.6)
    for k in range(20):
        y = 24 + k * 15
        arrow(c, (60, y), (108, y), "BLUE", 1.2, 7)
    lab(c, (84, 14), "U", size=16)
    for sgn in (1, -1):
        poly(c, _cl1_streamline(sgn), "TEXT", 1.4, "3,3")
    line(c, (110, yc - CL1_YM), (110, yc + CL1_YM), "TEXT", 1.0, "3,3")
    _cl1_airfoil(c)
    line(c, (480, 20), (480, 312), "HEAD", 1.6)
    tips = []
    for k in range(20):
        y = 24 + k * 15
        d = abs(y - yc)
        L = 48 if d >= CL1_Y0 else 24 + 24 * d / CL1_Y0
        arrow(c, (480, y), (480 + L, y), "BLUE", 1.2, 7)
    for y in (20, yc - CL1_Y0, yc, yc + CL1_Y0, 312):
        d = abs(y - yc)
        tips.append((480 + (48 if d >= CL1_Y0 else 24 + 24 * d / CL1_Y0), y))
    poly(c, tips, "HEAD", 1.3)
    lab(c, (504, 14), "U", size=16); lab(c, (512, yc + 6), "U/2", anchor="start", size=15)
    lab(c, (536, yc - CL1_Y0 + 6), sub("y", "0"), anchor="start", size=15)
    lab(c, (536, yc + CL1_Y0 + 6), "−" + sub("y", "0"), anchor="start", size=15)
    dim(c, (124, yc), (124, yc - CL1_YM), "", "TEXT"); lab(c, (130, yc - 18), sub("y", "−∞"), anchor="start", size=15)
    REG.put("cl1-statement", c,
            "Airfoil in a wind tunnel: uniform velocity U upstream; the bounding streamlines start at y equal to plus or "
            "minus y minus infinity and reach plus or minus y0 at the section x0, where the wake profile drops linearly "
            "from U at the edges to U over 2 at the centreline",
            "Statement figure (redrawn from CL1.pdf, p. 1): uniform profile $U$ upstream; bounding streamlines from "
            "$y = \\pm y_{-\\infty}$ to $y = \\pm y_0$; wake profile at $x = x_0$ falling linearly from $U$ at $|y| = y_0$ to "
            "$U/2$ on the centreline")


def cl1_cv():
    c = Canvas(620, 330)
    yc = CL1_YC
    for sgn in (1, -1):
        poly(c, _cl1_streamline(sgn), "GREEN", 2.0, CV_DASH)
    line(c, (110, yc - CL1_YM), (110, yc + CL1_YM), "GREEN", 2.0, CV_DASH)
    line(c, (480, yc - CL1_Y0), (480, yc + CL1_Y0), "GREEN", 2.0, CV_DASH)
    pathd(c, "M110,120 C300,120 340,35 480,35 L480,295 C340,295 300,210 110,210 Z", "none", 0, fill="BLUE", opacity=0.08)
    _cl1_airfoil(c, "EDGE")
    pathd(c, "M199,165 C199,140 240,144 312,165 C240,186 199,190 199,165 Z", "GREEN", 1.6, "4,3")
    sigma(c, (100, 106), "1", "end")
    sigma(c, (494, 300), "2", "start")
    sigma(c, (300, 70), "l", "end"); leader(c, (302, 72), (330, 86))
    sigma(c, (300, 270), "l", "end"); leader(c, (302, 264), (330, 244))
    sigma(c, (250, 122), "w", "middle"); leader(c, (252, 128), (256, 150))
    normal(c, (110, 140), (-1, 0), length=30, lab_off=(-4, -6), anchor="end")
    normal(c, (480, 120), (1, 0), length=30, lab_off=(4, -6), anchor="start")
    normal(c, (410, 46), (0.28, -1), length=26, lab_off=(10, 6), anchor="start")
    normal(c, (410, 284), (0.28, 1), length=26, lab_off=(10, 6), anchor="start")
    normal(c, (250, 184), (0, -1), length=16, lab_off=(0, 34))
    arrow(c, (30, 165), (90, 165), "BLUE", 2.0, 9); lab(c, (60, 155), "U", "BLUE", size=16)
    axes(c, (40, 300), "x", "y", 34)
    REG.put("cl1-cv", c,
            "Control volume bounded by the far-upstream section, the two bounding streamlines, the wake section at x0 and "
            "the airfoil surface",
            "Control volume of the solution: $\\Sigma_1$ (far upstream, $|y| < y_{-\\infty}$, $\\bar{n} = -\\bar{e}_x$), "
            "$\\Sigma_2$ ($x = x_0$, $|y| < y_0$, $\\bar{n} = +\\bar{e}_x$), the bounding streamlines $\\Sigma_l$ and the "
            "airfoil surface $\\Sigma_w$ ($\\bar{n}$ into the airfoil). The official sketch names them $\\Sigma_u$, "
            "$\\Sigma_d$, $\\Sigma_\\ell$ and $\\Sigma_i$")


# ----------------------------------------------------------------------------------------- shared (Lote 4)
def mapper(k, ox, oy):
    """Coordinates of a reference drawing (pixels of the 200 dpi crop) scaled onto the canvas."""
    def T(x, y):
        return (x * k + ox, y * k + oy)

    def D(d):
        """Rewrite every 'x,y' pair of SVG path data through T."""
        import re as _re
        return _re.sub(r"(-?[\d.]+),(-?[\d.]+)", lambda m: "{:.1f},{:.1f}".format(*T(float(m.group(1)), float(m.group(2)))), d)
    return T, D


def blob(c, centre, r, col="TEXT", w=1.2, lobes=7, amp=0.18, seed=0.0):
    """Irregular closed outline (a heat source region)."""
    pts = []
    for k in range(73):
        t = 2 * math.pi * k / 72
        rr = r * (1 + amp * math.sin(lobes * t + seed) + 0.08 * math.sin(3 * t + 1))
        pts.append((centre[0] + rr * math.cos(t), centre[1] + 0.8 * rr * math.sin(t)))
    poly(c, pts, col, w, close=True)


# ----------------------------------------------------------------------------------------- CL15
CL15_K, CL15_OX, CL15_OY = 0.75, 5, 34
CL15_WALLS = ("M75,475 L378,475 C453,475 515,413 515,338 L515,62 L653,62 L653,338 C653,420 630,460 598,497 L598,655",
              "M75,613 L378,613 C460,613 530,580 570,530 L570,655")
CL15_FILL = ("M75,475 L378,475 C453,475 515,413 515,338 L515,62 L653,62 L653,338 C653,420 630,460 598,497 L598,655 "
             "L570,655 L570,530 C530,580 460,613 378,613 L75,613 Z")


def _cl15_elbow(c, col="HEAD", w=2.2):
    T, D = mapper(CL15_K, CL15_OX, CL15_OY)
    pathd(c, D(CL15_FILL), "none", 0, fill="BLUE", opacity=0.10)
    for d in CL15_WALLS:
        pathd(c, D(d), col, w)
    line(c, T(515, 62), T(653, 62), col, w)
    return T, D


def cl15_statement():
    c = Canvas(560, 640)
    T, D = _cl15_elbow(c)
    line(c, T(102, 475), T(102, 613), "HEAD", 1.4, "4,3"); line(c, T(570, 640), T(598, 640), "HEAD", 1.4, "4,3")
    line(c, T(40, 545), T(650, 545), "TEXT", 0.9, "10,3,2,3"); line(c, T(584, 30), T(584, 700), "TEXT", 0.9, "10,3,2,3")
    line(c, T(378, 338), T(570, 530), "TEXT", 0.9, "3,3")
    line(c, T(96, 545), T(108, 545), "HEAD", 1.4); line(c, T(102, 539), T(102, 551), "HEAD", 1.4)
    lab(c, T(112, 534), vec("x") + sub("", "1"), anchor="start", size=15)
    line(c, T(372, 338), T(384, 338), "HEAD", 1.2); line(c, T(378, 332), T(378, 344), "HEAD", 1.2)
    line(c, T(460, 62), T(505, 62), "TEXT", 0.9); line(c, T(325, 338), T(505, 338), "TEXT", 0.9)
    dim(c, T(473, 64), T(473, 336), "", "TEXT"); lab(c, T(458, 205), sub("L", "1"), anchor="end", size=16)
    dim(c, T(336, 340), T(336, 473), "", "TEXT"); lab(c, T(324, 418), sub("D", "1"), anchor="end", size=16)
    line(c, T(378, 345), T(378, 460), "TEXT", 0.9)
    dim(c, T(155, 477), T(155, 611), "", "TEXT"); lab(c, T(166, 556), sub("D", "1"), anchor="start", size=16)
    line(c, T(102, 620), T(102, 665), "TEXT", 0.9); line(c, T(378, 620), T(378, 665), "TEXT", 0.9)
    dim(c, T(104, 655), T(376, 655), "", "TEXT"); lab(c, T(240, 690), sub("L", "1"), size=16)
    line(c, T(610, 545), T(655, 545), "TEXT", 0.9); line(c, T(610, 640), T(655, 640), "TEXT", 0.9)
    dim(c, T(638, 547), T(638, 638), "", "TEXT"); lab(c, T(646, 600), sub("L", "2"), anchor="start", size=16)
    arrow(c, T(530, 612), T(569, 612), "TEXT", 1.0, 7); arrow(c, T(636, 612), T(599, 612), "TEXT", 1.0, 7)
    lab(c, T(524, 622), sub("D", "2"), anchor="end", size=16)
    for i, t in enumerate(("Density ρ", "Viscosity μ", "Conductivity k", "Specific heat c")):
        note(c, T(115, 185 + 40 * i), t, "HEAD", "start", 13)
    hollow_arrow(c, T(32, 545), (1, 0), length=40, half=4, head=11)
    hollow_arrow(c, T(584, 58), (0, -1), length=38, half=4, head=11)
    hollow_arrow(c, T(584, 708), (0, -1), length=38, half=4, head=11)
    lab(c, T(612, 32), sub("p", "a"), anchor="start", size=16)
    for i, s_ in enumerate((sub("v", "1"), sub("p", "1"), sub("T", "1"))):
        lab(c, T(30, 600 + 38 * i), s_, anchor="start", size=16)
    for i, s_ in enumerate((sub("v", "2"), sub("p", "2"), sub("T", "2"))):
        lab(c, T(606, 712 + 36 * i), s_, anchor="start", size=16)
    REG.put("cl15-statement", c,
            "Mixing elbow: main pipe of diameter D1 and length L1 with inlet state v1, p1, T1 at the section centred on x1; "
            "bend of radius D1; vertical exit pipe of length L1 discharging at pa; secondary pipe of diameter D2 entering "
            "at the elbow from below with v2, p2, T2, its inlet a distance L2 below the main axis",
            "Statement figure (redrawn from CL15.pdf, p. 1): main inlet ($D_1$, $v_1$, $p_1$, $T_1$, centre $\\bar{x}_1$), "
            "bend and exit pipe of length $L_1$ discharging at $p_a$; secondary inlet ($D_2$, $v_2$, $p_2$, $T_2$) at the "
            "elbow, $L_2$ below the main axis; the thin lines are the axes of the official figure")


def cl15_cv():
    c = Canvas(560, 640)
    T, D = _cl15_elbow(c, "EDGE", 2.0)
    cv = ("M102,481 L378,481 C449,481 509,421 509,338 L509,68 L647,68 L647,338 C647,418 625,456 592,495 L592,640 "
          "L576,640 L576,532 C536,584 462,607 378,607 L102,607 Z")
    pathd(c, D(cv), "GREEN", 2.0, CV_DASH)
    sigma(c, T(70, 445), "1", "end"); leader(c, T(72, 450), T(100, 485))
    sigma(c, T(500, 700), "2", "end"); leader(c, T(502, 694), T(576, 642))
    sigma(c, T(690, 70), "out", "start")
    sigma(c, T(690, 420), "wall", "start"); leader(c, T(688, 414), T(650, 400))
    normal(c, T(102, 580), (-1, 0), length=30, lab_off=(-4, -6), anchor="end")
    normal(c, T(540, 68), (0, -1), length=30, lab_off=(-6, 4), anchor="end")
    normal(c, T(584, 640), (0, 1), length=30, lab_off=(-8, 10), anchor="end")
    arrow(c, T(10, 520), T(90, 520), "BLUE", 2.0, 9); lab(c, T(50, 505), sub("v", "1"), "BLUE", size=16)
    arrow(c, T(625, 760), T(625, 690), "BLUE", 2.0, 9); lab(c, T(640, 740), sub("v", "2"), "BLUE", "start", 16)
    arrow(c, T(620, 50), T(620, -10), "BLUE", 2.0, 9); lab(c, T(636, 0), sub("v", "s"), "BLUE", "start", 16)
    c.add('<circle cx="{:.1f}" cy="{:.1f}" r="3.5" fill="HEAD"/>'.format(*T(102, 545)))
    lab(c, T(112, 534), vec("x") + sub("", "1"), anchor="start", size=15)
    axes(c, T(250, 760), "x", "y", 34)
    REG.put("cl15-cv", c,
            "Control volume: the water inside the elbow between the main inlet, the secondary inlet and the exit, bounded "
            "by the pipe wall; moments about the centre x1 of the main inlet",
            "Control volume of the solution: $\\Sigma_1$ (main inlet, $\\bar{n} = -\\bar{e}_x$), $\\Sigma_2$ (secondary "
            "inlet, $\\bar{n} = -\\bar{e}_y$), $\\Sigma_{out}$ (exit, $\\bar{n} = +\\bar{e}_y$) and $\\Sigma_{wall}$; "
            "moments about $\\bar{x}_1$")


# ----------------------------------------------------------------------------------------- CL11
CL11_K, CL11_OX, CL11_OY = 0.55, 30, 6
CL11_A = 33.0


def _cl11_dirs():
    a = math.radians(CL11_A)
    return (-math.sin(a), math.cos(a)), (math.cos(a), math.sin(a))


CL11_LEFT, CL11_RIGHT = "M218,185 C190,240 175,330 125,460", "M425,388 C360,445 300,462 269,554"


def _cl11_device(c, col="HEAD", w=2.2):
    T, D = mapper(CL11_K, CL11_OX, CL11_OY)
    pathd(c, D("M218,185 C260,140 300,128 345,128 L975,128 L975,392 L425,392 L425,388 C360,445 300,462 269,554 "
               "L125,460 C175,330 190,240 218,185 Z"), "none", 0, fill="BLUE", opacity=0.10)
    line(c, T(330, 128), T(975, 128), col, w); line(c, T(350, 392), T(975, 392), col, w)
    pathd(c, D(CL11_LEFT), col, w); pathd(c, D(CL11_RIGHT), col, w)
    circle(c, T(345, 262), 135 * CL11_K, col, w)
    return T, D


def _cl11_blades(c, T, col="HEAD"):
    for y in (212, 312):
        x, yy = T(660, y)
        c.add(f'<ellipse cx="{fmt(x)}" cy="{fmt(yy)}" rx="{fmt(13 * CL11_K)}" ry="{fmt(48 * CL11_K)}" fill="{col}"/>')


def cl11_statement():
    c = Canvas(600, 500)
    T, D = _cl11_device(c)
    d, pp = _cl11_dirs()
    o = (345, 262)
    line(c, T(345, 230), T(345, 870), "TEXT", 0.9, "10,3,2,3")
    line(c, T(*o), T(o[0] + d[0] * 600, o[1] + d[1] * 600), "TEXT", 0.9, "10,3,2,3")
    cx, cy = T(*o)
    angle_arc(c, (cx, cy), 150 * CL11_K, -90, -90 - CL11_A, "HEAD", 1.2)
    lab(c, T(290, 470), "α", size=19)
    arrow(c, T(*o), T(415, 262), "HEAD", 1.2, 7); lab(c, T(405, 290), "x", size=15)
    arrow(c, T(*o), T(345, 185), "HEAD", 1.2, 7); lab(c, T(325, 200), "y", size=15)
    E = (197, 507)
    for k in (-64, -32, 0, 32, 64):
        a = (E[0] + pp[0] * k + d[0] * 12, E[1] + pp[1] * k + d[1] * 12)
        arrow(c, T(*a), T(a[0] + d[0] * 150, a[1] + d[1] * 150), "BLUE", 1.3, 7)
    for e0 in ((125, 460), (269, 554)):
        line(c, T(*e0), T(e0[0] + d[0] * 260, e0[1] + d[1] * 260), "TEXT", 1.1, "2,4")
    arrow(c, T(60, 430), T(120, 456), "TEXT", 1.1, 7); arrow(c, T(335, 590), T(276, 557), "TEXT", 1.1, 7)
    lab(c, T(55, 425), sub("A", "e"), anchor="end", size=17)
    lab(c, T(70, 690), sub("p", "a"), size=16); lab(c, T(135, 700), sub("ρ", "e"), size=16)
    lab(c, T(80, 760), sub("U", "e"), size=16)
    for y in (165, 210, 255, 300, 345):
        arrow(c, T(935, y), T(872, y), "BLUE", 1.3, 7)
    line(c, T(866, 136), T(866, 384), "TEXT", 1.1, "4,3")
    lab(c, T(945, 180), sub("p", "i"), anchor="start", size=16); lab(c, T(945, 265), sub("U", "i"), anchor="start", size=16)
    lab(c, T(945, 350), sub("ρ", "a"), anchor="start", size=16)
    arrow(c, T(866, 60), T(866, 126), "TEXT", 1.1, 7); arrow(c, T(880, 450), T(880, 394), "TEXT", 1.1, 7)
    lab(c, T(890, 60), sub("A", "i"), anchor="start", size=17)
    lab(c, T(730, 110), sub("p", "a"), size=16)
    blob(c, T(535, 258), 32, "HEAD", 1.2, seed=0.6); lab(c, T(535, 272), "Q", size=17)
    _cl11_blades(c, T)
    lab(c, T(712, 275), "W", anchor="start", size=17)
    REG.put("cl11-statement", c,
            "VTOL propulsion device: horizontal intake of section Ai on the right (pi, Ui, rho a), duct with the heat "
            "addition Q and the mobile blades W, and a thrust-vectoring nozzle of exit section Ae turned an angle alpha "
            "from the vertical, discharging at Ue, rho e into pa",
            "Statement figure (redrawn from CL11.pdf, p. 1): intake $A_i$ ($p_i$, $U_i$, $\\rho_a$), heat $Q$ and blades "
            "$W$ inside the duct, nozzle of exit section $A_e$ at the angle $\\alpha$ from the vertical ($U_e$, $\\rho_e$, "
            "$p_a$); axes $x$, $y$ at the centre of the rotating joint")


def cl11_cv():
    c = Canvas(600, 500)
    T, D = _cl11_device(c, "EDGE", 2.0)
    d, pp = _cl11_dirs()
    pathd(c, D("M230,185 C262,150 300,136 345,136 L866,136 L866,384 L425,384 C358,446 300,468 262,550 L132,465 "
               "C187,330 202,240 230,185 Z"), "GREEN", 2.0, CV_DASH)
    blob(c, T(535, 258), 32, "EDGE", 1.2, seed=0.6)
    _cl11_blades(c, T, "EDGE")
    cx, cy = T(660, 262)
    ellipse(c, cx, cy, 24 * CL11_K, 112 * CL11_K, "GREEN", 1.5, "4,3")
    E = (197, 507)
    sigma(c, T(900, 440), "i", "start"); leader(c, T(898, 430), T(868, 360))
    sigma(c, T(40, 560), "e", "end"); leader(c, T(44, 555), T(150, 490))
    sigma(c, T(780, 90), "w", "start"); leader(c, T(778, 96), T(760, 132))
    sigma(c, T(720, 470), "m", "start"); leader(c, T(718, 458), T(672, 375))
    normal(c, T(866, 260), (1, 0), length=30, lab_off=(4, -6), anchor="start")
    normal(c, T(E[0] - pp[0] * 20, E[1] - pp[1] * 20), d, length=34, lab_off=(-8, 8), anchor="end")
    normal(c, T(600, 136), (0, -1), length=26, lab_off=(10, 6), anchor="start")
    arrow(c, T(1010, 350), T(905, 350), "BLUE", 2.0, 9); lab(c, T(958, 335), sub("U", "i"), "BLUE", size=16)
    a = (E[0] + pp[0] * 60 + d[0] * 30, E[1] + pp[1] * 60 + d[1] * 30)
    arrow(c, T(*a), T(a[0] + d[0] * 150, a[1] + d[1] * 150), "BLUE", 2.0, 9)
    lab(c, T(a[0] + d[0] * 120 + 30, a[1] + d[1] * 120), sub("U", "e"), "BLUE", "start", 16)
    arrow(c, T(345, 262), T(415, 262), "HEAD", 1.2, 7); lab(c, T(405, 290), "x", size=15)
    arrow(c, T(345, 262), T(345, 185), "HEAD", 1.2, 7); lab(c, T(325, 200), "y", size=15)
    REG.put("cl11-cv", c,
            "Control volume: the air inside the duct and the nozzle, from the intake section to the exit section, bounded "
            "by the fixed walls and the surface of the mobile blades",
            "Control volume of the solution: $\\Sigma_i$ (intake, $\\bar{n} = +\\bar{e}_x$, $\\bar{v} = -U_i\\bar{e}_x$), "
            "$\\Sigma_e$ (exit, $\\bar{n} = \\bar{v}_e/U_e$), the fixed walls $\\Sigma_w$ and the mobile blades "
            "$\\Sigma_m$ (dashed around them)")


# ----------------------------------------------------------------------------------------- CL5
CL5_K, CL5_OX, CL5_OY = 0.78, -100, 14
CL5_UP, CL5_DN = "M245,128 C330,92 420,62 490,62 L770,62", "M245,300 C330,345 420,385 490,385 L770,385"


def _cl5_engine(c, col="HEAD", w=2.4):
    T, D = mapper(CL5_K, CL5_OX, CL5_OY)
    pathd(c, D("M245,128 C330,92 420,62 490,62 L770,62 L770,385 L490,385 C420,385 330,345 245,300 Z"), "none", 0,
          fill="BLUE", opacity=0.10)
    pathd(c, D(CL5_UP), col, w); pathd(c, D(CL5_DN), col, w)
    return T, D


def _cl5_rotor(c, T, col="HEAD"):
    for y in (178, 282):
        x, yy = T(460, y)
        c.add(f'<ellipse cx="{fmt(x)}" cy="{fmt(yy)}" rx="{fmt(26 * CL5_K)}" ry="{fmt(52 * CL5_K)}" fill="{col}"/>')


def cl5_statement():
    c = Canvas(600, 370)
    T, D = _cl5_engine(c)
    pathd(c, D("M250,134 C333,99 422,68 490,68 L766,68 L766,379 L490,379 C422,379 333,339 250,294 Z"), "HEAD", 1.2, "4,3")
    for k in range(14):
        y = 140 + k * 12.5
        arrow(c, T(165, y), T(240, y), "BLUE", 1.1, 6)
    for k in range(21):
        y = 72 + k * 15
        arrow(c, T(700, y), T(762, y), "BLUE", 1.1, 6)
    arrow(c, T(245, 80), T(245, 124), "TEXT", 1.1, 7); arrow(c, T(245, 350), T(245, 304), "TEXT", 1.1, 7)
    lab(c, T(255, 345), sub("A", "1"), anchor="start", size=15)
    arrow(c, T(770, 10), T(770, 58), "TEXT", 1.1, 7); arrow(c, T(770, 432), T(770, 389), "TEXT", 1.1, 7)
    lab(c, T(755, 425), sub("A", "2"), anchor="end", size=15)
    for i, s_ in enumerate((sub("v", "1"), sub("p", "1"), sub("ρ", "1"))):
        lab(c, T(262, 168 + 30 * i), s_, anchor="start", size=15)
    for i, s_ in enumerate((sub("v", "2"), sub("p", "2"), sub("ρ", "2"))):
        lab(c, T(782, 110 + 30 * i), s_, anchor="start", size=15)
    _cl5_rotor(c, T)
    pathd(c, D("M460,120 C505,120 500,225 470,230 C500,235 505,340 460,340 C415,340 420,235 450,230 C420,225 415,120 "
               "460,120 Z"), "HEAD", 1.1, "4,3")
    arc_arrow(c, T(460, 230), 18, 200, -20, "HEAD", 1.3)
    blob(c, T(545, 255), 20, "TEXT", 1.0, seed=1.2); lab(c, T(545, 265), sub("Q", "r"), size=15)
    blob(c, T(615, 205), 22, "TEXT", 1.0, seed=2.1); lab(c, T(615, 215), sub("Q", "c"), size=15)
    axes(c, T(345, 215), "x", "y", 26)
    arrow(c, T(548, 62), T(548, 30), "HEAD", 1.2, 7); lab(c, T(560, 36), vec("n"), anchor="start", size=15)
    arrow(c, T(766, 240), T(800, 240), "HEAD", 1.2, 7); lab(c, T(800, 228), vec("n"), anchor="start", size=15)
    arrow(c, T(250, 298), T(212, 298), "HEAD", 1.2, 7); lab(c, T(208, 290), vec("n"), anchor="end", size=15)
    lab(c, T(282, 300), sub("Σ", "1"), anchor="start", size=15)
    lab(c, T(785, 330), sub("Σ", "2"), anchor="start", size=15)
    lab(c, T(318, 215), sub("Σ", "3"), anchor="end", size=15)
    line(c, T(322, 200), T(338, 112), "HEAD", 0.9); line(c, T(322, 222), T(338, 330), "HEAD", 0.9)
    lab(c, T(404, 150), sub("Σ", "4"), anchor="end", size=15); line(c, T(406, 144), T(432, 136), "HEAD", 0.9)
    REG.put("cl5-statement", c,
            "Turbojet on a testbench: entrance section A1 with v1, p1, rho1, exit section A2 with v2, p2, rho2; the rotor "
            "inside and the heat sources Qr and Qc; the official control volume with surfaces Sigma 1 to Sigma 4",
            "Statement figure (redrawn from CL5.pdf, p. 1): entrance $A_1$ ($v_1$, $p_1$, $\\rho_1$), exit $A_2$ ($v_2$, "
            "$p_2$, $\\rho_2$), rotor and heat sources $Q_r$, $Q_c$; the dashed control volume and its surfaces "
            "$\\Sigma_1$ to $\\Sigma_4$ belong to the official figure")


def cl5_cv():
    c = Canvas(620, 370)
    T, D = _cl5_engine(c, "EDGE", 2.0)
    pathd(c, D("M250,134 C333,99 422,68 490,68 L766,68 L766,379 L490,379 C422,379 333,339 250,294 Z"), "GREEN", 2.0,
          CV_DASH)
    _cl5_rotor(c, T, "EDGE")
    pathd(c, D("M460,120 C505,120 500,225 470,230 C500,235 505,340 460,340 C415,340 420,235 450,230 C420,225 415,120 "
               "460,120 Z"), "GREEN", 1.5, "4,3")
    arc_arrow(c, T(460, 230), 18, 200, -20, "ACC", 1.5)
    overdot(c, T(505, 150), "W", "ACC", "start", 16)
    blob(c, T(600, 230), 34, "PINK", 1.2, seed=0.4); lab(c, T(600, 222), sub("Q", "c"), "PINK", size=15)
    lab(c, T(600, 252), sub("Q", "R"), "PINK", size=15)
    sigma(c, T(225, 360), "1", "end"); leader(c, T(228, 352), T(250, 290))
    sigma(c, T(800, 360), "2", "start"); leader(c, T(798, 352), T(768, 340))
    sigma(c, T(640, 30), "w", "start"); leader(c, T(638, 36), T(620, 66))
    sigma(c, T(390, 140), "m", "end"); leader(c, T(392, 134), T(440, 128))
    normal(c, T(250, 214), (-1, 0), length=26, lab_off=(-4, -6), anchor="end")
    normal(c, T(766, 214), (1, 0), length=26, lab_off=(4, -6), anchor="start")
    normal(c, T(540, 379), (0, 1), length=24, lab_off=(10, 8), anchor="start")
    arrow(c, T(150, 160), T(236, 160), "BLUE", 2.0, 9); lab(c, T(190, 144), sub("v", "1"), "BLUE", size=15)
    arrow(c, T(790, 160), T(870, 160), "BLUE", 2.0, 9); lab(c, T(830, 144), sub("v", "2"), "BLUE", size=15)
    arrow(c, T(400, 430), T(320, 430), "ACC", 2.4, 10)
    lab(c, T(410, 436), vec("F") + " = −F " + vec("e") + sub("", "x"), "ACC", "start", 15, weight="700")
    arrow(c, T(120, 430), T(170, 430), "HEAD", 1.3, 8); lab(c, T(176, 436), vec("e") + sub("", "x"), anchor="start", size=15)
    REG.put("cl5-cv", c,
            "Control volume, as in the class notes: entrance and exit sections, fixed walls and the surface of the moving "
            "rotor; power W extracted by the rotor, heat sources Qc and QR, force F on the testbench",
            "Control volume of the solution (as in the class notes): $\\Sigma_1$ (entrance, $\\bar{n} = -\\bar{e}_x$), "
            "$\\Sigma_2$ (exit, $\\bar{n} = +\\bar{e}_x$), the fixed walls $\\Sigma_w$ and the surface $\\Sigma_m$ of the "
            "mobile parts. The official figure calls them $\\Sigma_1$, $\\Sigma_2$, $\\Sigma_3$ and $\\Sigma_4$")


# ----------------------------------------------------------------------------------------- Lote 5
# The statement figures of CL4, CL7, CL13 and CL17 are crops of the official PDFs (300 dpi, greyscale): their drawings
# carry the official control volumes and annotations, which a redraw would lose.
RASTER.update({
    "cl4-statement": ("Array of aerofoils a distance L apart in a uniform stream rho1, p1, v1; the official control volume "
                      "with the upstream section Sigma 1, the downstream section Sigma 2, the stream surfaces Sigma 3 and "
                      "Sigma 4 and the aerofoil surface Sigma 5; force components Fx, Fy",
                      "Statement figure (CL4.pdf, p. 1, cropped): cascade of aerofoils $L$ apart; the dashed control "
                      "volume ($\\Sigma_1$ to $\\Sigma_5$) and the handwritten notes belong to the official sheet"),
    "cl7-statement": ("Axisymmetric dryer: radial inlet of area A with velocity vr at rho a, resistance and fan inside, "
                      "exit of radius R with axial and azimuthal velocities vz, v theta",
                      "Statement figure (CL7.pdf, p. 1, cropped): radial inlet $A$ ($v_r$, $\\rho_a$), resistance and fan, "
                      "exit of diameter $2R$ with $v_z$ and $v_\\theta$; the surface names and notes are handwritten on the "
                      "official sheet"),
    "cl13-statement": ("Centrifugal pump: meridional section with the inlet pipe of diameter Do (Vo, po) and the lateral "
                       "exit of width h, and front view of the impeller of diameter D with the exit velocity Vs at the "
                       "angle alpha from the lateral surface",
                       "Statement figure (CL13.pdf, p. 1, cropped): inlet $D_o$ ($V_o$, $p_o$), lateral exit of width $h$ "
                       "and diameter $D$, exit velocity $V_s$ at the angle $\\alpha$ with the lateral surface; the "
                       "surface names are handwritten on the official sheet"),
    "cl17-statement": ("Experimental airplane: engine inlet of height ai below the centre of gravity (Vi, pi, rho i), "
                       "outlet of height ao above it (Vo, po, rho o), heat Q added; canard at a distance L ahead "
                       "giving the lift F",
                       "Statement figure (CL17.pdf, p. 1, cropped): inlet of height $a_i$ ($V_i$, $p_i$, $\\rho_i$) and "
                       "outlet of height $a_o$ ($V_o$, $p_o$, $\\rho_o$), heat $\\dot{Q}$, axes at the CoG, canard lift "
                       "$F$ at the distance $L$"),
})


# ----------------------------------------------------------------------------------------- CL4
def _aerofoil(c, dy, col="HEAD", fill="TEXT"):
    pathd(c, f"M240,{232 + dy} C240,{210 + dy} 300,{206 + dy} 372,{240 + dy} C318,{238 + dy} 262,{254 + dy} 240,{232 + dy} Z",
          col, 1.8, fill=fill, opacity=0.25)


def cl4_cv():
    c = Canvas(620, 400)
    _aerofoil(c, -120, "EDGE"); _aerofoil(c, 0, "EDGE")
    up = cubic((110, 170), (330, 170), (380, 245), (500, 245))
    dn = [(x, y + 120) for x, y in up]
    poly(c, up + [(500, 245), (500, 365)] + dn[::-1] + [(110, 290)], "none", 0, fill="BLUE", opacity=0.10, close=True)
    poly(c, up, "GREEN", 2.0, CV_DASH); poly(c, dn, "GREEN", 2.0, CV_DASH)
    line(c, (110, 170), (110, 290), "GREEN", 2.0, CV_DASH); line(c, (500, 245), (500, 365), "GREEN", 2.0, CV_DASH)
    pathd(c, "M233,232 C233,203 300,198 380,241 C318,246 258,262 233,232 Z", "GREEN", 1.5, "4,3")
    dim(c, (132, 172), (132, 288), "", "ACC"); lab(c, (140, 236), "L", "ACC", "start", 17)
    sigma(c, (150, 282), "1", "start")
    sigma(c, (512, 322), "2", "start")
    sigma(c, (430, 196), "l1", "start"); leader(c, (428, 200), (400, 222))
    sigma(c, (330, 342), "l2", "start"); leader(c, (346, 326), (352, 308))
    sigma(c, (300, 286), "w"); leader(c, (300, 272), (300, 252))
    normal(c, (110, 270), (-1, 0), length=28, lab_off=(-4, -6), anchor="end")
    normal(c, (500, 352), (1, 0), length=28, lab_off=(4, -6), anchor="start")
    normal(c, (210, 171), (0, -1), length=24, lab_off=(10, 6), anchor="start")
    normal(c, (210, 291), (0, 1), length=24, lab_off=(10, 8), anchor="start")
    normal(c, (262, 216), (0.3, 1), length=16, lab_off=(-4, -14), anchor="end")
    for y in (150, 195, 240):
        arrow(c, (20, y), (74, y), "BLUE", 1.6, 8)
    lab(c, (56, 330), vec("v") + sub("", "1") + " = " + sub("v", "1x") + vec("e") + sub("", "x"), "BLUE", size=15)
    for k in range(3):
        arrow(c, (540, 200 + 40 * k), (600, 228 + 40 * k), "BLUE", 1.6, 8)
    lab(c, (560, 192), vec("v") + sub("", "2"), "BLUE", "start", 16)
    axes(c, (40, 380), "x", "y", 32)
    REG.put("cl4-cv", c,
            "Control volume one period high, as in the class notes: upstream and downstream sections of height L, the two "
            "stream surfaces and the surface of one aerofoil",
            "Control volume of the solution (as in the class notes): $\\Sigma_1$ and $\\Sigma_2$ (sections of height $L$), "
            "the stream surfaces $\\Sigma_{l1}$ and $\\Sigma_{l2}$ ($\\Sigma_{l2}$ is $\\Sigma_{l1}$ shifted by $-L\\bar{e}_y$, "
            "so their fluxes cancel) and the aerofoil surface $\\Sigma_w$. The official figure calls them $\\Sigma_1$, "
            "$\\Sigma_2$, $\\Sigma_3$, $\\Sigma_4$ and $\\Sigma_5$")


# ----------------------------------------------------------------------------------------- CL7
CL7_TOP = "M90,70 L110,70 M210,70 C330,70 360,115 440,115 L500,115"
CL7_BOT = "M90,250 L110,250 M210,250 C330,250 360,205 440,205 L500,205"


def cl7_cv():
    c = Canvas(620, 330)
    pathd(c, "M90,70 L210,70 C330,70 360,115 440,115 L500,115 L500,205 L440,205 C360,205 330,250 210,250 L90,250 Z",
          "none", 0, fill="BLUE", opacity=0.10)
    pathd(c, CL7_TOP, "EDGE", 2.2); pathd(c, CL7_BOT, "EDGE", 2.2)
    ellipse(c, 90, 160, 18, 90, "EDGE", 2.2)
    ellipse(c, 500, 160, 12, 45, "EDGE", 1.6)
    loops = []
    for k in range(121):
        t = k / 120
        a = t * 3 * 2 * math.pi
        loops.append((235 + 70 * t + 9 * math.sin(a), 175 - 14 * math.cos(a)))
    poly(c, loops, "EDGE", 1.4)
    for sgn in (1, -1):
        ellipse(c, 360, 160 - sgn * 22, 6, 20, "EDGE", 1.5)
    ellipse(c, 360, 160, 14, 48, "GREEN", 1.5, "4,3")
    line(c, (110, 70), (210, 70), "GREEN", 2.2, CV_DASH); line(c, (110, 250), (210, 250), "GREEN", 2.2, CV_DASH)
    pathd(c, "M110,74 L96,74 M96,246 L110,246", "GREEN", 2.0, CV_DASH)
    ellipse(c, 92, 160, 14, 86, "GREEN", 1.6, CV_DASH)
    pathd(c, "M210,74 C330,74 360,119 440,119 L496,119 M210,246 C330,246 360,201 440,201 L496,201", "GREEN", 2.0, CV_DASH)
    ellipse(c, 496, 160, 10, 41, "GREEN", 1.8, CV_DASH)
    for x in (120, 136, 184, 200):
        arrow(c, (x, 30), (x, 64), "BLUE", 1.3, 7); arrow(c, (x, 290), (x, 256), "BLUE", 1.3, 7)
    lab(c, (214, 34), sub("v", "r"), "BLUE", "start", 16)
    flow_arrows(c, 512, 570, [140, 160, 180], "BLUE", 1.6)
    lab(c, (580, 165), sub("v", "z"), "BLUE", "start", 16)
    sigma(c, (96, 30), "1", "end"); leader(c, (98, 30), (116, 66)); sigma(c, (96, 300), "1", "end")
    leader(c, (98, 296), (116, 254))
    sigma(c, (520, 112), "2", "start"); leader(c, (518, 116), (502, 126))
    sigma(c, (300, 52), "w", "start"); leader(c, (298, 56), (290, 74)); leader(c, (296, 60), (270, 180))
    sigma(c, (405, 250), "m", "start"); leader(c, (403, 244), (368, 202))
    normal(c, (160, 70), (0, -1), length=26, lab_off=(0, -6))
    normal(c, (496, 190), (1, 0), length=28, lab_off=(4, 14), anchor="start")
    lab(c, (268, 205), "Q", "PINK", size=16)
    arrow(c, (520, 300), (564, 300), "HEAD", 1.3, 8); lab(c, (570, 305), vec("e") + sub("", "z"), anchor="start", size=15)
    arrow(c, (520, 300), (520, 258), "HEAD", 1.3, 8); lab(c, (526, 262), vec("e") + sub("", "r"), anchor="start", size=15)
    REG.put("cl7-cv", c,
            "Control volume of the dryer: the radial inlet band, the exit disc, the fixed casing with the resistance, and "
            "the fan blades",
            "Control volume of the solution (schematic axial section): $\\Sigma_1$ (radial inlet of area $A$, "
            "$\\bar{n} = \\bar{e}_r$, $\\bar{v} = -v_r\\bar{e}_r$), $\\Sigma_2$ (exit disc of radius $R$, "
            "$\\bar{n} = \\bar{e}_z$), $\\Sigma_w$ (fixed casing and resistance) and $\\Sigma_m$ (fan blades, dashed "
            "around them); the heat $Q$ is released by the resistance")


# ----------------------------------------------------------------------------------------- CL13
def cl13_cv():
    c = Canvas(640, 410)
    yc = 200
    pathd(c, "M20,165 L60,165 C150,165 210,110 210,40 L260,40 L260,360 L210,360 C210,290 150,235 60,235 L20,235 Z",
          "none", 0, fill="BLUE", opacity=0.10)
    pathd(c, "M20,165 L60,165 C150,165 210,110 210,40", "EDGE", 2.2)
    pathd(c, "M20,235 L60,235 C150,235 210,290 210,360", "EDGE", 2.2)
    line(c, (260, 30), (260, 370), "EDGE", 2.4)
    pathd(c, "M60,169 C150,169 214,114 214,44 L256,44 L256,356 L214,356 C214,286 150,231 60,231 Z", "GREEN", 2.0, CV_DASH)
    for y0, y1 in ((60, 150), (250, 340)):
        rect(c, 226, y0, 18, y1 - y0, "EDGE", 1.2, fill="none")
        rect(c, 221, y0 - 5, 28, y1 - y0 + 10, "GREEN", 1.4, "4,3", rx=6)
    line(c, (20, yc), (300, yc), "TEXT", 0.9, "10,3,2,3")
    sigma(c, (96, 118), "o", "end"); leader(c, (90, 124), (64, 168))
    sigma(c, (196, 30), "s", "end"); leader(c, (198, 30), (222, 44))
    sigma(c, (236, 396), "s")
    sigma(c, (290, 110), "w", "start"); leader(c, (288, 106), (258, 96)); leader(c, (288, 112), (190, 120))
    sigma(c, (150, 300), "b", "end"); leader(c, (152, 296), (222, 290))
    normal(c, (60, 222), (-1, 0), length=28, lab_off=(-4, 16), anchor="end")
    normal(c, (236, 40), (0, -1), length=22, lab_off=(10, 6), anchor="start")
    arrow(c, (8, 180), (52, 180), "BLUE", 2.0, 9); lab(c, (28, 158), sub("V", "o"), "BLUE", size=15)
    arrow(c, (300, 300), (340, 300), "HEAD", 1.3, 8); lab(c, (346, 305), vec("e") + sub("", "x"), anchor="start", size=15)
    # front view: impeller, exit velocity at the angle alpha with the lateral surface
    cx, cy, R, r0 = 480, 210, 135, 34
    circle(c, (cx, cy), R, "EDGE", 2.0, fill="BLUE", opacity=0.10); circle(c, (cx, cy), r0, "EDGE", 1.6)
    for k in range(6):
        pts = []
        for j in range(31):
            t = j / 30
            a = math.radians(60 * k) - 1.1 * t
            rr = r0 + (R - r0) * t
            pts.append((cx + rr * math.cos(a), cy - rr * math.sin(a)))
        poly(c, pts, "EDGE", 1.4)
    circle(c, (cx, cy), R + 5, "GREEN", 1.6, CV_DASH)
    ph = math.radians(100)
    P = (cx + R * math.cos(ph), cy - R * math.sin(ph))
    t_ = (math.sin(ph), math.cos(ph)); r_ = (math.cos(ph), -math.sin(ph))
    al = math.radians(30)
    V = (math.cos(al) * t_[0] + math.sin(al) * r_[0], math.cos(al) * t_[1] + math.sin(al) * r_[1])
    line(c, P, (P[0] + 80 * t_[0], P[1] + 80 * t_[1]), "TEXT", 1.0, "4,3")
    arrow(c, P, (P[0] + 80 * V[0], P[1] + 80 * V[1]), "BLUE", 2.0, 9)
    lab(c, (P[0] + 80 * V[0] - 6, P[1] + 80 * V[1] - 8), sub("V", "s"), "BLUE", "end", 16)
    angle_arc(c, P, 52, math.degrees(math.atan2(-t_[1], t_[0])), math.degrees(math.atan2(-V[1], V[0])), "HEAD", 1.1)
    lab(c, (P[0] + 62, P[1] - 4), "α", anchor="start", size=16)
    lab(c, (cx + R - 10, cy - R + 6), sub("Σ", "s"), "GREEN", "start", 16, weight="600")
    REG.put("cl13-cv", c,
            "Control volume of the pump: meridional section with the inlet disc, the lateral exit cylinder, the fixed "
            "casing and the rotating blades; front view with the exit velocity at the angle alpha from the lateral surface",
            "Control volume of the solution: $\\Sigma_o$ (inlet disc, $\\bar{n} = -\\bar{e}_x$), $\\Sigma_s$ (lateral exit "
            "cylinder of radius $D/2$ and width $h$, $\\bar{n} = \\bar{e}_r$), the fixed casing $\\Sigma_w$ and the rotating "
            "blades $\\Sigma_b$ (schematic); on the right, the exit velocity $V_s$ at the angle $\\alpha$ with the lateral "
            "surface: normal component $V_s\\sin\\alpha$, tangential $V_s\\cos\\alpha$")


# ----------------------------------------------------------------------------------------- CL17
def cl17_cv():
    c = Canvas(640, 300)
    y0 = 170
    pathd(c, "M140,66 C70,70 20,108 20,118 C20,128 70,166 140,170 L170,170 M140,66 L470,66 L560,100", "EDGE", 1.4)
    pathd(c, "M170,170 C300,170 420,100 560,100 L560,170 C450,200 330,245 170,240 Z", "none", 0, fill="BLUE",
          opacity=0.12)
    pathd(c, "M170,170 C300,170 420,100 560,100", "EDGE", 2.0)
    pathd(c, "M170,240 C330,245 450,200 560,170", "EDGE", 2.0)
    pathd(c, "M174,174 C300,174 420,104 556,104 L556,170 C450,197 330,238 174,236 Z", "GREEN", 2.0, CV_DASH)
    c.add('<circle cx="380" cy="170" r="4" fill="HEAD"/>')
    arrow(c, (380, 170), (425, 170), "HEAD", 1.3, 8); lab(c, (430, 175), "x", anchor="start", size=15)
    arrow(c, (380, 170), (380, 128), "HEAD", 1.3, 8); lab(c, (386, 132), "y", anchor="start", size=15)
    note(c, (372, 188), "CoG", "HEAD", "end", 12)
    flow_arrows(c, 112, 166, [180, 196, 212], "BLUE", 1.5); lab(c, (100, 202), sub("V", "i"), "BLUE", "end", 16)
    flow_arrows(c, 566, 620, [108, 126, 144], "BLUE", 1.5); lab(c, (594, 96), sub("V", "o"), "BLUE", size=16)
    overdot(c, (300, 214), "Q", "PINK", "middle", 17)
    sigma(c, (150, 268), "i", "end"); leader(c, (152, 262), (172, 236))
    sigma(c, (576, 196), "o", "start"); leader(c, (574, 190), (558, 166))
    sigma(c, (470, 240), "w", "start"); leader(c, (468, 234), (440, 206))
    normal(c, (174, 228), (-1, 0), length=28, lab_off=(-2, 16), anchor="end")
    normal(c, (556, 162), (1, 0), length=28, lab_off=(4, 16), anchor="start")
    dim(c, (196, 172), (196, 238), "", "TEXT"); lab(c, (204, 214), sub("a", "i"), anchor="start", size=15)
    dim(c, (530, 104), (530, 168), "", "TEXT"); lab(c, (522, 142), sub("a", "o"), anchor="end", size=15)
    REG.put("cl17-cv", c,
            "Control volume: the air inside the engine, from the inlet section below the axis to the outlet section above "
            "it, bounded by the engine walls; origin at the centre of gravity",
            "Control volume of the solution (schematic): $\\Sigma_i$ (inlet, $\\bar{n} = -\\bar{e}_x$, area $a_ib$, below "
            "the CoG), $\\Sigma_o$ (outlet, $\\bar{n} = +\\bar{e}_x$, area $a_ob$, above the CoG) and the engine walls "
            "$\\Sigma_w$; origin and moments at the CoG")


# ----------------------------------------------------------------------------------------- build
def build():
    for fn in (cl22_statement, cl22_cv, cl21_statement, cl21_cv, cl20_statement, cl20_cv,
               cl12_statement, cl12_cv, cl2_statement, cl2_cv,
               cl6_statement, cl6_cv, cl19_statement, cl19_cv, cl10_statement, cl10_cv, cl3_statement, cl3_cv,
               cl8_statement, cl8_cv, cl16_statement, cl16_cv, cl18_statement, cl18_cv, cl9_statement, cl9_cv,
               cl14_statement, cl14_cv, cl1_statement, cl1_cv, cl15_statement, cl15_cv, cl11_statement, cl11_cv,
               cl5_statement, cl5_cv, cl4_cv, cl7_cv, cl13_cv, cl17_cv):
        fn()
    return REG
