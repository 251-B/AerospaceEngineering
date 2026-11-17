"""Figures of the Part II problems P09 to P12 of the Midterm 2 bank (archetype fe-c-steels).

Every number printed on a figure comes from the Fe-Fe3C values of Session 9 Slides 4 and 10 (eutectoid 727 °C at
0.76 wt% C, ferrite 0.022 wt% C, cementite 6.67 wt% C, austenite 2.14 wt% C at 1147 °C) and from the data of the
problem it belongs to:

* p09-microstructure  sketch of the 0.45 wt% C steel just below 727 °C (P09, part d);
* p10-diagram         steel corner of the Fe-Fe3C diagram with the 1.10 wt% C steel of P10 (Acm drawn straight
                      between (0.76, 727) and (2.14, 1147), as in tools/figures/materials_t4.py);
* p11-micrograph      schematic micrograph of the unknown steel of P11 (light continuous network around lamellar
                      colonies; the network is labelled only "X" so the figure does not name it);
* p12-constituents    microconstituent fractions of the three steels of P12 just below 727 °C.
"""
import math

from figures.svgkit import Canvas, line, text, poly, dot, rect
from figures.mat_mt2.common import figure
from figures.materials_t4 import Plot, fec_diagram

C_ALPHA, C_E, C_CEM = 0.022, 0.76, 6.67


def _lamellae(c, pts, angle, uid, gap=5.0, w=1.0):
    """Parallel lines (pearlite lamellae) clipped to the polygon pts (absolute pixel coordinates)."""
    s = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    cx = sum(p[0] for p in pts) / len(pts)
    cy = sum(p[1] for p in pts) / len(pts)
    c.add(f'<clipPath id="cl-{uid}"><polygon points="{s}"/></clipPath><g clip-path="url(#cl-{uid})">')
    dx, dy = math.cos(angle), math.sin(angle)
    for k in range(-40, 41):
        px, py = cx + k * gap * -dy, cy + k * gap * dx
        line(c, (px - 150 * dx, py - 150 * dy), (px + 150 * dx, py + 150 * dy), "HEAD", w)
    c.add("</g>")


def _grid_grains(ox, oy, size, n, jitter):
    """A perturbed n x n grid of grain vertices -> list of quadrilateral grains (absolute pixels)."""
    step = size / n
    v = {}
    for i in range(n + 1):
        for j in range(n + 1):
            jx = 0 if i in (0, n) else jitter[(i * 7 + j * 3) % len(jitter)]
            jy = 0 if j in (0, n) else jitter[(i * 5 + j * 11 + 2) % len(jitter)]
            v[i, j] = (ox + i * step + jx, oy + j * step + jy)
    return [[v[i, j], v[i + 1, j], v[i + 1, j + 1], v[i, j + 1]] for j in range(n) for i in range(n)]


def _area(pts):
    return abs(sum(pts[k][0] * pts[k - 1][1] - pts[k - 1][0] * pts[k][1] for k in range(len(pts)))) / 2


JIT = [9, -7, 4, -11, 6, -3, 10, -8, 2, -5, 7]


# --------------------------------------------------------------------------- P09
FERRITE_P09 = (0, 2, 5, 6, 9, 13, 15)


@figure("p09-microstructure", "Sketch of a 0.45 wt% C steel just below 727 °C: light proeutectoid ferrite grains "
        "and lamellar pearlite colonies",
        "Bank P09 (d): 0.45 wt% C steel at 727 - ΔT °C. Light grains: proeutectoid ferrite (about 42 % of the area). "
        "Lamellar grains: pearlite (about 58 %), alternating ferrite and cementite lamellae")
def p09_micro():
    c = Canvas(480, 270)
    ox, oy, size = 20, 20, 220
    grains = _grid_grains(ox, oy, size, 4, JIT)
    for k, g in enumerate(grains):
        if k in FERRITE_P09:
            poly(c, g, "HEAD", 1.0, fill="BLUE", opacity=0.10, close=True)
        else:
            _lamellae(c, g, 0.4 + 0.8 * k, f"p09g{k}", gap=4.6)
        poly(c, g, "HEAD", 1.4, close=True)
    rect(c, ox, oy, size, size, "HEAD", 1.8)
    # leader lines to grains 0 (ferrite) and 9 (pearlite), labels outside the sketch
    fx = sum(p[0] for p in grains[6]) / 4
    fy = sum(p[1] for p in grains[6]) / 4
    px = sum(p[0] for p in grains[10]) / 4
    py = sum(p[1] for p in grains[10]) / 4
    dot(c, (fx, fy), 3, "GREEN")
    dot(c, (px, py), 3, "GREEN")
    line(c, (fx, fy), (262, 70), "GREEN", 1.2)
    line(c, (px, py), (262, 170), "GREEN", 1.2)
    text(c, (268, 66), "Proeutectoid ferrite, αp", "HEAD", "start", 13, "700")
    text(c, (268, 84), "light grains, 0.022 wt% C", "TEXT", "start", 12)
    text(c, (268, 166), "Pearlite (α + Fe₃C)", "HEAD", "start", 13, "700")
    text(c, (268, 184), "lamellar colonies, 0.76 wt% C", "TEXT", "start", 12)
    text(c, (ox, oy + size + 22), "0.45 wt% C, 727 - ΔT °C", "TEXT", "start", 12)
    return c


# --------------------------------------------------------------------------- P10
@figure("p10-diagram", "Steel corner of the Fe-Fe3C diagram with a vertical line at 1.10 wt% C and the points a and b",
        "Bank P10: steel region of the metastable Fe-Fe3C diagram with the values of Session 9 Slides 4 and 10 "
        "(eutectoid 727 °C at 0.76 wt% C, ferrite 0.022 wt% C, austenite 2.14 wt% C at 1147 °C). Dashed grid every "
        "50 °C. The vertical line is the 1.10 wt% C steel; a is the start of the cooling, b the crossing of the Acm line")
def p10_diagram():
    c = Canvas(660, 430)
    P = Plot(c, (80, 34, 600, 370), (0, 2.4), (600, 1250))
    fec_diagram(c, P, "p10", labels=False)
    P.frame([(0, "0"), (0.5, "0.5"), (0.76, "0.76"), (1.10, "1.10"), (1.5, "1.5"), (2.14, "2.14")],
            [(600, "600"), (727, "727"), (800, "800"), (900, "900"), (1000, "1000"), (1100, "1100"), (1147, "1147")],
            "Composition (wt% C)", "Temperature (°C)", grid=[("y", t) for t in range(650, 1250, 50) if t not in (1150,)])
    P.vseg(1.10, 600, 1250, "GREEN", 1.6, "6,4")
    P.text(1.10, 1250, "1.10 wt% C", "GREEN", "start", 12, dx=6, dy=16)
    t_b = 727 + (1.10 - C_E) * (1147 - 727) / (2.14 - C_E)
    P.dot(1.10, 950, 4.5, "GREEN")
    P.text(1.10, 950, "a", "GREEN", "start", 14, dx=8, dy=5)
    P.dot(1.10, t_b, 4.5, "GREEN")
    P.text(1.10, t_b, "b", "GREEN", "end", 14, dx=-8, dy=-6)
    P.text(0.95, 1040, "γ (austenite)", size=13)
    P.text(0.30, 745, "α + γ", size=11.5)
    P.text(1.85, 900, "γ + Fe₃C", size=13)
    P.text(1.55, 650, "α + Fe₃C", size=13)
    P.text(2.25, 1215, "γ + L", size=11)
    P.text(0.022, 727, "0.022", "TEXT", "start", 11.5, "400", dx=6, dy=16)
    P.text(0.0, 912, "912", "TEXT", "start", 11.5, "400", dx=6, dy=-6)
    P.text(2.4, 727, "727 °C", "TEXT", "end", 11.5, "400", dx=-4, dy=-6)
    P.text(1.70, 1060, "Acm", "ACC", "end", 12)
    P.text(0.30, 850, "A3", "ACC", "start", 12)
    return c


# --------------------------------------------------------------------------- P11
@figure("p11-micrograph", "Schematic micrograph of a slowly cooled steel: lamellar colonies surrounded by a continuous "
        "light network labelled X",
        "Bank P11: schematic micrograph of the unknown steel after slow cooling (polished and etched). Lamellar "
        "colonies are surrounded by a thin, continuous, light network X along the former austenite grain boundaries")
def p11_micro():
    c = Canvas(430, 280)
    ox, oy, size = 20, 20, 230
    grains = _grid_grains(ox, oy, size, 3, JIT)
    for k, g in enumerate(grains):
        _lamellae(c, g, 0.3 + 1.05 * k, f"p11g{k}", gap=5.0)
    for g in grains:                       # the network: a wide light band along every boundary
        poly(c, g, "ACC", 7.0, close=True)
    rect(c, ox, oy, size, size, "HEAD", 1.8)
    nx, ny = grains[4][1]                  # a vertex of the central grain lies on the network
    gx = sum(p[0] for p in grains[8]) / 4
    gy = sum(p[1] for p in grains[8]) / 4
    dot(c, (nx, ny), 3.2, "GREEN")
    dot(c, (gx, gy), 3.2, "GREEN")
    line(c, (nx, ny), (272, 70), "GREEN", 1.2)
    line(c, (gx, gy), (272, 200), "GREEN", 1.2)
    text(c, (278, 66), "X: continuous light", "HEAD", "start", 13, "700")
    text(c, (278, 84), "network at the grain", "TEXT", "start", 12)
    text(c, (278, 100), "boundaries", "TEXT", "start", 12)
    text(c, (278, 196), "Lamellar colonies", "HEAD", "start", 13, "700")
    text(c, (278, 214), "88.0 % of the area", "TEXT", "start", 12)
    text(c, (ox, oy + size + 22), "Slowly cooled, room temperature", "TEXT", "start", 12)
    return c


# --------------------------------------------------------------------------- P12
def _constituents(c0):
    if c0 < C_E:
        wp = (C_E - c0) / (C_E - C_ALPHA)
        return wp, 1 - wp, 0.0
    wc = (c0 - C_E) / (C_CEM - C_E)
    return 0.0, 1 - wc, wc


@figure("p12-constituents", "Stacked bars of proeutectoid ferrite, pearlite and proeutectoid cementite for steels "
        "S1 (0.25), S2 (0.60) and S3 (1.35 wt% C)",
        "Bank P12: mass fractions of the microconstituents just below 727 °C (lever rule with 0.022, 0.76 and "
        "6.67 wt% C, Session 9 Slides 4 and 10)")
def p12_bars():
    c = Canvas(640, 260)
    x0, x1 = 170, 590
    steels = (("S1, 0.25 wt% C", 0.25), ("S2, 0.60 wt% C", 0.60), ("S3, 1.35 wt% C", 1.35))
    for i, (lab, c0) in enumerate(steels):
        y = 30 + i * 62
        fa, pe, fc = _constituents(c0)
        text(c, (x0 - 10, y + 23), lab, "HEAD", "end", 13, "700")
        x = x0
        for frac, col, op, name in ((fa, "BLUE", 0.22, "αp"), (pe, "HEAD", 0.18, "pearlite"), (fc, "ACC", 0.55, "Fe₃Cp")):
            if frac <= 0:
                continue
            w = frac * (x1 - x0)
            rect(c, x, y, w, 34, "HEAD", 1.2, fill=col, opacity=op)
            if w > 90:
                text(c, (x + w / 2, y + 22), f"{name} {100 * frac:.1f} %", "HEAD", "middle", 12.5, "700")
            else:
                text(c, (x + w / 2, y + 52), f"{name} {100 * frac:.1f} %", "HEAD", "middle", 11.5, "700")
            x += w
    for f in (0, 0.25, 0.5, 0.75, 1.0):
        xx = x0 + f * (x1 - x0)
        line(c, (xx, 222), (xx, 227), "EDGE", 1.2)
        text(c, (xx, 242), f"{int(f * 100)} %", "TEXT", "middle", 11.5)
    line(c, (x0, 222), (x1, 222), "EDGE", 1.2)
    return c
