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


# ----------------------------------------------------------------------------------------- build
def build():
    for fn in (cl22_statement, cl22_cv, cl21_statement, cl21_cv, cl20_statement, cl20_cv,
               cl12_statement, cl12_cv, cl2_statement, cl2_cv,
               cl6_statement, cl6_cv, cl19_statement, cl19_cv, cl10_statement, cl10_cv, cl3_statement, cl3_cv,
               cl8_statement, cl8_cv):
        fn()
    return REG
