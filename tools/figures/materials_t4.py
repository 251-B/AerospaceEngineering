"""Topic 4 figures for Aerospace Materials I: phase diagrams (Session 7 T4 Phase diagrams I).

The diagrams are redrawn from the slides: the labelled values (temperatures, compositions) are the ones the
slides print, and the curves between them are smooth shapes that pass through those values. Micrographs and
hand-drawn sketches are copied from the slides as PNG files (registered with `REG.raster`). The `pd_*`
figures belong to the problem sheet (Problems T4_PhaseDiagrams I.pdf) and are inlined in the problems page.
Run `python tools/build_topic_pages.py` to write the SVG files to vault/attachments/T4 and rebuild the page.
"""
import math

from figures.svgkit import Canvas, Registry, arrow_head, dot, fmt, line, text

REG = Registry("T4")


def sub(s, i):
    return f'{s}<tspan baseline-shift="sub" font-size="72%">{i}</tspan>'


def poly(c, pts, col="ACC", w=2.2, dash=None, fill="none", op=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' fill-opacity="{op}"' if op is not None else ""
    stroke = f' stroke="{col}" stroke-width="{w}"' if col else ' stroke="none"'
    path = "M" + " L".join(f"{fmt(x)},{fmt(y)}" for x, y in pts)
    if fill != "none":
        path += " Z"
    c.add(f'<path d="{path}" fill="{fill}"{o}{stroke}{d} stroke-linejoin="round"/>')


def smooth(c, pts, col="ACC", w=2.4, dash=None):
    """Smooth curve through the pixel points (Catmull-Rom spline written as cubic Beziers)."""
    d = f"M{fmt(pts[0][0])},{fmt(pts[0][1])}"
    for i in range(len(pts) - 1):
        p0, p1, p2 = pts[max(i - 1, 0)], pts[i], pts[i + 1]
        p3 = pts[min(i + 2, len(pts) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{fmt(c1[0])},{fmt(c1[1])} {fmt(c2[0])},{fmt(c2[1])} {fmt(p2[0])},{fmt(p2[1])}"
    da = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}"{da}/>')


def circle(c, p, r, col="EDGE", w=1.4, fill="none", op=None):
    o = f' fill-opacity="{op}"' if op is not None else ""
    c.add(f'<circle cx="{fmt(p[0])}" cy="{fmt(p[1])}" r="{fmt(r)}" fill="{fill}"{o} stroke="{col}" stroke-width="{w}"/>')


def rect(c, x, y, w, h, col="EDGE", sw=1.4, fill="none", op=None):
    o = f' fill-opacity="{op}"' if op is not None else ""
    c.add(f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" fill="{fill}"{o} stroke="{col}" stroke-width="{sw}"/>')


def lin(a, b, n=40):
    return [a + (b - a) * k / n for k in range(n + 1)]


class Plot:
    """Data coordinates (composition, temperature) inside a pixel box (left, top, right, bottom)."""

    def __init__(self, c, box, xr, yr):
        self.c = c
        self.x0, self.y0, self.x1, self.y1 = box
        self.xa, self.xb = xr
        self.ya, self.yb = yr

    def p(self, x, y):
        return (self.x0 + (x - self.xa) / (self.xb - self.xa) * (self.x1 - self.x0),
                self.y1 - (y - self.ya) / (self.yb - self.ya) * (self.y1 - self.y0))

    def frame(self, xt=(), yt=(), xl="", yl="", box=True, grid=(), xl_dy=38):
        c = self.c
        for g in grid:
            if g[0] == "x":
                line(c, self.p(g[1], self.ya), self.p(g[1], self.yb), "EDGE", 0.7, "2,4")
            else:
                line(c, self.p(self.xa, g[1]), self.p(self.xb, g[1]), "EDGE", 0.7, "2,4")
        line(c, (self.x0, self.y1), (self.x1, self.y1), "EDGE", 1.4)
        line(c, (self.x0, self.y0), (self.x0, self.y1), "EDGE", 1.4)
        if box:
            line(c, (self.x1, self.y0), (self.x1, self.y1), "EDGE", 1.4)
            line(c, (self.x0, self.y0), (self.x1, self.y0), "EDGE", 0.8)
        for v, s in xt:
            x, y = self.p(v, self.ya)
            line(c, (x, y), (x, y + 5), "EDGE", 1.2)
            text(c, (x, y + 19), s, "TEXT", "middle", 12)
        for v, s in yt:
            x, y = self.p(self.xa, v)
            line(c, (x - 5, y), (x, y), "EDGE", 1.2)
            text(c, (x - 8, y + 4), s, "TEXT", "end", 12)
        if xl:
            text(c, ((self.x0 + self.x1) / 2, self.y1 + xl_dy), xl, "HEAD", "middle", 12.5, "700")
        if yl:
            text(c, (self.x0 + 4, self.y0 - 10), yl, "HEAD", "start", 12.5, "700")

    def line(self, pts, col="ACC", w=2.2, dash=None):
        poly(self.c, [self.p(*q) for q in pts], col, w, dash)

    def area(self, pts, col="BLUE", op=0.12):
        poly(self.c, [self.p(*q) for q in pts], None, 0, None, col, op)

    def text(self, x, y, s, col="HEAD", anchor="middle", size=13, weight="700", dx=0, dy=0):
        text(self.c, self.p(x, y), s, col, anchor, size, weight, dx, dy)

    def dot(self, x, y, r=4, col="GREEN", fill=None):
        dot(self.c, self.p(x, y), r, col, fill)

    def hseg(self, xa, xb, y, col="EDGE", w=1, dash="4,4"):
        line(self.c, self.p(xa, y), self.p(xb, y), col, w, dash)

    def vseg(self, x, ya, yb, col="EDGE", w=1, dash="4,4"):
        line(self.c, self.p(x, ya), self.p(x, yb), col, w, dash)


def bracket(c, a, b, label, col="BLUE", dy=-6):
    """Double-headed measuring arrow between two pixel points with a centred label above it."""
    line(c, a, b, col, 1.4)
    arrow_head(c, b, a, col, 7)
    arrow_head(c, a, b, col, 7)
    text(c, ((a[0] + b[0]) / 2, a[1] + dy), label, col, "middle", 13, "700")


# --------------------------------------------------------------------------- reference shapes
def lens(x, ta, tb, up):
    """Isomorphous liquidus (up=True, above the chord) or solidus between the melting points of A and B."""
    return ta + (tb - ta) * (x ** 0.62 if up else x ** 1.9)


# Pb-Sn as drawn in the slides [Session 7 Slide 32]: eutectic 183 °C at 61.9 wt% Sn, alpha 18.3, beta 97.8.
PBSN = dict(tpb=327, tsn=232, te=183, ca=18.3, ce=61.9, cb=97.8, bulge=0.0029, sol_p=0.75, solv_a=2.14, solv_b=4.0)
# Pb-Sn as drawn in the problem sheet (Problems T4_PhaseDiagrams I.pdf, p. 1): alpha 19.2, beta 97.5; the
# shapes pass through the readings used in the official solutions (36 % Sn liquid and 12 % Sn alpha at
# 250 °C, 5 % Sn alpha at 100 °C).
PBSN_SHEET = dict(tpb=327, tsn=232, te=183, ca=19.2, ce=61.9, cb=97.5, bulge=0.00724, sol_p=0.751, solv_a=2.224, solv_b=4.0)


def pbsn_curves(d):
    """Polylines (composition, T) of the Pb-Sn boundaries for the data set d."""
    tpb, tsn, te, ca, ce, cb = d["tpb"], d["tsn"], d["te"], d["ca"], d["ce"], d["cb"]
    liq_a = [(x, tpb - (tpb - te) * x / ce + d["bulge"] * x * (ce - x)) for x in lin(0, ce)]
    liq_b = [(x, te + (tsn - te) * (x - ce) / (100 - ce)) for x in lin(ce, 100, 8)]
    sol_a = [(ca * ((tpb - t) / (tpb - te)) ** d["sol_p"], t) for t in lin(tpb, te)]
    sol_b = [(cb + (100 - cb) * ((t - te) / (tsn - te)) ** 0.5, t) for t in lin(te, tsn, 20)]
    solv_a = [(ca * (t / te) ** d["solv_a"], t) for t in lin(te, 2, 40)]
    solv_b = [(100 - (100 - cb) * (t / te) ** d["solv_b"], t) for t in lin(te, 2, 40)]
    return liq_a, liq_b, sol_a, sol_b, solv_a, solv_b


def pbsn_diagram(c, P, d, labels=True, values=True):
    liq_a, liq_b, sol_a, sol_b, solv_a, solv_b = pbsn_curves(d)
    P.area([(0, P.yb)] + liq_a + liq_b + [(100, P.yb)], "BLUE", 0.08)
    P.area(sol_a + solv_a + [(0, 0)], "BLUE", 0.16)
    P.area([(100, d["tsn"])] + list(reversed(sol_b)) + solv_b + [(100, 0)], "BLUE", 0.16)
    for curve in (liq_a, liq_b, sol_a, sol_b, solv_a, solv_b):
        P.line(curve, "ACC", 2.2)
    P.line([(d["ca"], d["te"]), (d["cb"], d["te"])], "ACC", 2.2)
    if labels:
        P.text(45, 290, "L")
        P.text(8, 205, "α")
        P.text(100, 205, "β", "HEAD", "start", dx=8)
        P.text(40, 205, "α + L", size=12.5)
        P.text(83, 199, "β + L", size=12.5)
        P.text(55, 90, "α + β")
    if values:
        P.text(0, d["tpb"], f'{d["tpb"]} °C', "TEXT", "start", 11.5, "400", dx=8, dy=-4)
        P.text(100, d["tsn"], f'{d["tsn"]} °C', "TEXT", "end", 11.5, "400", dx=-6, dy=-8)
        P.text(45, d["te"], f'{d["te"]} °C', "TEXT", "middle", 11.5, "400", dy=16)


# --------------------------------------------------------------------------- Session 7 figures
def co2():
    c = Canvas(600, 340)
    x0, y0, x1, y1 = 90, 30, 540, 290
    line(c, (x0, y1), (x1, y1)); line(c, (x0, y0), (x0, y1))
    xt = {-78.2: 150, -56.6: 255, 31.1: 480}
    yt = {1: 262, 5.1: 222, 73: 55}
    tp, cp, sb = (xt[-56.6], yt[5.1]), (xt[31.1], yt[73]), (xt[-78.2], yt[1])
    smooth(c, [(x0 + 5, 284), sb, tp])
    smooth(c, [tp, (400, 160), cp])
    smooth(c, [tp, (tp[0] + 18, y0)])
    for v, (x, y) in ((-78.2, sb), (-56.6, tp), (31.1, cp)):
        line(c, (x, y1), (x, y), "EDGE", 1, "4,4")
        line(c, (x0, y), (x, y), "EDGE", 1, "4,4")
        text(c, (x, y1 + 18), f"{v:.1f}" if v > 0 else f"−{abs(v):.1f}", "TEXT", "middle", 12)
    for v, y in yt.items():
        text(c, (x0 - 8, y + 4), f"{v:g}", "TEXT", "end", 12)
    dot(c, sb, 3.5, "HEAD")
    dot(c, tp, 4.5, "GREEN"); dot(c, cp, 4.5, "GREEN")
    text(c, (tp[0] + 12, tp[1] + 18), "triple point", "GREEN", weight="700")
    text(c, (cp[0] + 10, cp[1] + 22), "critical point", "GREEN", "start", weight="700")
    text(c, (170, 150), "Solid", "HEAD", "middle", 14, "700")
    text(c, (370, 130), "Liquid", "HEAD", "middle", 14, "700")
    text(c, (360, 255), "Gas", "HEAD", "middle", 14, "700")
    text(c, (520, 36), "supercritical fluid", "TEXT", "middle", 12)
    text(c, ((x0 + x1) / 2, y1 + 40), "Temperature (°C)", "HEAD", "middle", 12.5, "700")
    text(c, (x0 + 4, y0 - 10), "Pressure (atm)", "HEAD", "start", 12.5, "700")
    REG.put("co2", c, "Phase diagram of CO2",
            "Phase diagram of CO₂ (axes not to scale): triple point at 5.1 atm and −56.6 °C, sublimation at 1 atm "
            "and −78.2 °C, critical point at 73 atm and 31.1 °C. Redrawn from Session 7 Slide 3")


def water():
    c = Canvas(660, 300)
    # left: P-T diagram
    x0, y0, x1, y1 = 50, 30, 300, 250
    line(c, (x0, y1), (x1, y1)); line(c, (x0, y0), (x0, y1))
    a, pt, b, cc = (60, 232), (175, 168), (205, 35), (292, 92)
    yp = 122
    tm, tv = (186, yp), (271, yp)
    smooth(c, [a, (120, 205), pt])
    smooth(c, [pt, tm, b])
    smooth(c, [pt, (230, 150), tv, cc])
    line(c, (x0, yp), (x1 + 8, yp), "BLUE", 1.3, "5,4")
    arrow_head(c, (x1 + 8, yp), (x1 - 4, yp), "BLUE", 9)
    dot(c, tm, 4.5, "GREEN"); dot(c, tv, 4.5, "GREEN"); dot(c, pt, 4, "HEAD")
    text(c, (tm[0] + 6, yp - 8), sub("T", "m"), "GREEN", weight="700")
    text(c, (tv[0] - 6, yp - 8), sub("T", "v"), "GREEN", "end", weight="700")
    text(c, (pt[0] + 6, pt[1] + 18), sub("P", "T"), "HEAD", weight="700")
    for p, s, dx, dy in ((a, "A", -2, 16), (b, "B", 6, 4), (cc, "C", 6, -4)):
        text(c, (p[0] + dx, p[1] + dy), s, "HEAD", weight="700")
    text(c, (105, 75), "Solid", "HEAD", "middle", 14, "700")
    text(c, (245, 70), "Liquid", "HEAD", "middle", 14, "700")
    text(c, (175, 220), "Vapour", "HEAD", "middle", 14, "700")
    text(c, ((x0 + x1) / 2, y1 + 22), "Temperature (T)", "HEAD", "middle", 12.5, "700")
    text(c, (x0 + 4, y0 - 10), "Pressure (p)", "HEAD", "start", 12.5, "700")
    # right: cooling curve at the pressure of the dashed line
    u0, v0, u1, v1 = 390, 30, 640, 250
    line(c, (u0, v1), (u1, v1)); line(c, (u0, v0), (u0, v1))
    ytv, ytm = 95, 175
    pts = [(400, 40), (430, ytv), (480, ytv), (550, ytm), (590, ytm), (632, 235)]
    poly(c, pts, "ACC", 2.4)
    for (x, y), s in zip(((400, 40), (455, ytv), (515, 135), (570, ytm), (612, 205)), "12345"):
        text(c, (x + 8, y - 6), s, "HEAD", weight="700")
    line(c, (u0, ytv), (430, ytv), "EDGE", 1, "4,4"); line(c, (u0, ytm), (550, ytm), "EDGE", 1, "4,4")
    text(c, (u0 - 6, ytv + 4), sub("T", "v"), "HEAD", "end", weight="700")
    text(c, (u0 - 6, ytm + 4), sub("T", "m"), "HEAD", "end", weight="700")
    text(c, ((u0 + u1) / 2, v1 + 22), "time", "HEAD", "middle", 12.5, "700")
    text(c, (u0 + 4, v0 - 10), "T", "HEAD", "start", 12.5, "700")
    REG.put("water", c, "Phase diagram and cooling curve of water",
            "Left: P-T diagram of water with the sublimation (A to P_T), melting (P_T to B) and vaporisation (P_T to C) "
            "lines and the triple point P_T; cooling along the dashed line at constant pressure crosses the vaporisation "
            "line at T_v and the melting line at T_m. Right: the cooling curve, with a plateau at each transition "
            "(2: condensation, 4: solidification). Redrawn from Session 7 Slide 5")


def water_logp():
    c = Canvas(560, 300)
    P = Plot(c, (70, 30, 400, 250), (0, 1), (0, 1))
    line(c, (70, 250), (400, 250)); line(c, (70, 30), (70, 250))
    tp = (125, 192)
    sub_c = [(75 + k * 50 / 20, 248 - (248 - tp[1]) * (k / 20) ** 0.8) for k in range(21)]
    vap = [(tp[0] + k * 6.5, tp[1] - 150 * ((k * 6.5) / 130) ** 0.62) for k in range(21)]
    melt = [tp, (360, 208)]
    for pts in (sub_c, vap, melt):
        poly(c, pts, "BLUE", 2.4)
    xa = 185
    y100 = tp[1] - 150 * ((xa - tp[0]) / 130) ** 0.62
    y0 = tp[1] + (208 - tp[1]) * (xa - tp[0]) / (360 - tp[0])
    line(c, (xa, 250), (xa, 40), "EDGE", 1, "4,4")
    line(c, (xa, y100), (470, y100), "EDGE", 1, "4,4"); line(c, (xa, y0), (470, y0), "EDGE", 1, "4,4")
    text(c, (476, y100 + 4), "100 °C · steam / water", "TEXT", size=12)
    text(c, (476, y0 + 4), "0 °C · water / ice", "TEXT", size=12)
    text(c, (xa, 268), "1 atm", "TEXT", "middle", 12)
    text(c, (120, 80), "Gas", "HEAD", "middle", 14, "700")
    text(c, (300, 140), "Liquid", "HEAD", "middle", 14, "700")
    text(c, (300, 232), "Solid", "HEAD", "middle", 14, "700")
    text(c, (235, 290), "Pressure (log scale)", "HEAD", "middle", 12.5, "700")
    text(c, (74, 20), "Temperature", "HEAD", "start", 12.5, "700")
    REG.put("water-logp", c, "Water at 1 atm on a log-pressure diagram",
            "Temperature against pressure (log scale) for water: at 1 atm the vertical line meets the melting line at "
            "0 °C and the vaporisation line at 100 °C. Redrawn from Session 7 Slide 5")


def iron_pt():
    c = Canvas(600, 330)
    P = Plot(c, (90, 30, 540, 280), (-14, 6), (300, 2900))
    xt = [(-12, "10⁻¹²"), (-8, "10⁻⁸"), (-4, "10⁻⁴"), (0, "1"), (4, "10⁴")]
    P.frame(xt, [(500, "500"), (1000, "1000"), (1500, "1500"), (2000, "2000"), (2500, "2500")],
            "Pressure (atm)", "Temperature (°C)", box=False)
    t1, t2, t3 = (-10.5, 910), (-5.3, 1394), (-4.0, 1538)
    subl = [(-14, 640), (-12, 790), t1, (-8, 1130), t2, t3]
    boil = [t3] + [(-4 + k * 0.25, 1538 + 1200 * ((k * 0.25) / 3.5) ** 1.35) for k in range(1, 15)]
    P.area(subl + [(6, 1538), (6, 300), (-14, 300)], "BLUE", 0.12)
    P.line(subl, "ACC", 2.4)
    P.line(boil, "PINK", 2.4)
    P.line([t3, (6, 1545)], "ACC", 2.2)
    P.line([t2, (6, 1394)], "EDGE", 1.4)
    P.line([t1, (6, 910)], "EDGE", 1.4)
    for t in (t1, t2, t3):
        P.dot(*t, r=4.5, col="GREEN")
    P.text(-12.4, 1650, "triple points", "GREEN", "middle", 12.5)
    for t in (t1, t2, t3):
        line(c, P.p(-11.4, 1600), P.p(*t), "GREEN", 1, head=True)
    P.text(-6, 2500, "Vapour", size=14)
    P.text(1, 2050, "Liquid", size=14)
    P.text(1.5, 1405, "δ Fe (BCC)", "HEAD", size=11)
    P.text(-1, 1150, "γ Fe (FCC)", "HEAD", size=12.5)
    P.text(-1, 650, "α Fe (BCC)", "HEAD", size=12.5)
    for v, y in ((1538, 1538), (1394, 1394), (910, 910)):
        P.text(6, y, f"{v} °C", "TEXT", "start", 12, "400", dx=6, dy=4)
    REG.put("iron-pt", c, "Phase diagram of pure iron",
            "P-T diagram of pure iron (pressure on a log scale): three solid phases, α (BCC) below 910 °C, γ (FCC) "
            "between 910 and 1394 °C and δ (BCC) up to the melting point, 1538 °C; at each triple point three phases "
            "coexist. Redrawn from Session 7 Slide 6")


def cooling_curves():
    c = Canvas(680, 300)
    P = Plot(c, (70, 30, 300, 250), (0, 10), (600, 1700))
    P.frame((), [(912, "912"), (1394, "1394"), (1538, "1538")], "time (t)", "Temperature (°C)", box=False)
    pts = [(0.2, 1680), (1.2, 1538), (3.2, 1538), (4.0, 1394), (5.6, 1394), (6.4, 912), (8.0, 912), (9.6, 720)]
    P.line(pts, "PINK", 2.4)
    for y in (1538, 1394, 912):
        P.hseg(0, 10, y)
    P.text(4.5, 1610, "Liquid", "TEXT", size=12, weight="400")
    P.text(7.3, 1460, "δ iron (solid)", "TEXT", size=12, weight="400")
    P.text(7.8, 1080, "γ iron (solid)", "TEXT", size=12, weight="400")
    P.text(4.0, 760, "α iron (solid)", "TEXT", size=12, weight="400")
    Q = Plot(c, (420, 30, 660, 250), (0, 10), (0, 10))
    Q.frame((), (), "time (t)", "Temp (T)", box=False)
    Q.line([(0, 9.2)] + [(k * 0.1, 9.2 - 3.6 * (1 - math.exp(-k * 0.1 * 0.9)) / (1 - math.exp(-2.25))) for k in range(1, 26)],
           "PINK", 2.4)
    Q.line([(2.5, 5.6), (6.5, 5.6)], "PINK", 2.4)
    Q.line([(2.5, 5.6), (3.2, 4.8), (3.9, 5.6)], "PINK", 1.6, "5,4")
    Q.line([(6.5, 5.6)] + [(6.5 + k * 0.15, 5.6 - 3.0 * (1 - math.exp(-k * 0.15 * 1.2))) for k in range(1, 22)], "PINK", 2.4)
    for x, s in ((0, "A"), (2.5, "B"), (6.5, "C"), (9.6, "D")):
        y = {0: 9.2, 2.5: 5.6, 6.5: 5.6, 9.6: 5.6 - 3.0 * (1 - math.exp(-3.15 * 1.2))}[x]
        Q.text(x, y, s, "HEAD", "middle", 13, "700", dx=6 if x else 8, dy=-8)
    Q.hseg(0, 2.5, 5.6)
    Q.text(0, 9.2, "pouring temp", "TEXT", "end", 11.5, "400", dx=-6, dy=4)
    Q.text(0, 5.6, "freezing temp", "TEXT", "end", 11.5, "400", dx=-6, dy=4)
    Q.vseg(2.5, 0, 5.6); Q.vseg(6.5, 0, 5.6)
    Q.text(1.25, 0.6, "liquid", "TEXT", size=11.5, weight="400")
    Q.text(4.5, 0.6, "liquid + solid", "TEXT", size=11.5, weight="400")
    Q.text(8.3, 0.6, "solid", "TEXT", size=11.5, weight="400")
    REG.put("cooling-curves", c, "Cooling curves of pure iron and of a pure metal",
            "Left: cooling curve of pure iron, with a thermal arrest at each transition (1538, 1394 and 912 °C). Right: "
            "cooling curve of a pure metal: A to B cooling of the liquid, B solidification begins (after a small "
            "undercooling, dashed), C solidification ends, C to D cooling of the solid. Redrawn from Session 7 Slide 8")


def iso_construction():
    c = Canvas(720, 330)
    ta, tb = 0.32, 0.78
    y_of = lambda t: 280 - t * 240                       # same temperature scale as the diagram on the right
    comps = (0.0, 0.2, 0.5, 0.8, 1.0)
    for k, x in enumerate(comps):
        u0 = 30 + k * 72
        line(c, (u0, 280), (u0 + 60, 280), "EDGE", 1); line(c, (u0, 40), (u0, 280), "EDGE", 1)
        tl, ts = lens(x, ta, tb, True), lens(x, ta, tb, False)
        top = 0.97
        if x in (0.0, 1.0):
            pts = [(u0 + 2, y_of(top)), (u0 + 16, y_of(tl)), (u0 + 38, y_of(tl)), (u0 + 58, y_of(tl - 0.22))]
            marks = [(u0 + 16, tl), (u0 + 38, tl)]
        else:
            pts = [(u0 + 2, y_of(top)), (u0 + 14, y_of(tl)), (u0 + 40, y_of(ts)), (u0 + 58, y_of(ts - 0.2))]
            marks = [(u0 + 14, tl), (u0 + 40, ts)]
        poly(c, pts, "PINK", 2.2)
        for u, t in marks:
            dot(c, (u, y_of(t)), 3.2, "GREEN")
        text(c, (u0 + 30, 298), f"{round(x * 100)} % B", "TEXT", "middle", 11.5)
    text(c, (30, 30), "cooling curves (T against time)", "HEAD", "start", 12.5, "700")
    P = Plot(c, (450, 40, 690, 280), (0, 100), (0, 1))
    P.area([(0, 1)] + [(100 * x, lens(x, ta, tb, True)) for x in lin(0, 1)] + [(100, 1)], "BLUE", 0.08)
    P.area([(100 * x, lens(x, ta, tb, False)) for x in lin(0, 1)] + [(100, 0), (0, 0)], "BLUE", 0.18)
    P.line([(100 * x, lens(x, ta, tb, True)) for x in lin(0, 1)], "ACC", 2.4)
    P.line([(100 * x, lens(x, ta, tb, False)) for x in lin(0, 1)], "ACC", 2.4)
    P.frame([(0, "0"), (20, "20"), (50, "50"), (80, "80"), (100, "100")], (), "Composition (wt% B)", "Temperature")
    for x in comps:
        for up in (True, False):
            P.dot(100 * x, lens(x, ta, tb, up), 3.2, "GREEN")
    P.text(18, 0.85, "L", size=14)
    P.text(50, 0.505, "L + SS", size=12)
    P.text(75, 0.2, "SS", size=14)
    P.text(48, 0.80, "liquidus", "TEXT", size=11.5, weight="400", dx=-10)
    P.text(60, 0.34, "solidus", "TEXT", size=11.5, weight="400")
    REG.put("iso-construction", c, "Building an isomorphous diagram from cooling curves",
            "Each cooling curve gives the temperature where solidification starts (a point of the liquidus) and where "
            "it ends (a point of the solidus); the pure components (0 and 100 % B) solidify at a single temperature. "
            "Joining the points gives the diagram with the regions L, L + SS and SS. Redrawn from Session 7 Slide 9")


def iso_micro():
    c = Canvas(640, 330)
    ta, tb = 0.42, 0.88
    P = Plot(c, (60, 40, 320, 290), (0, 100), (0, 1))
    P.area([(0, 1)] + [(100 * x, lens(x, ta, tb, True)) for x in lin(0, 1)] + [(100, 1)], "BLUE", 0.08)
    P.area([(100 * x, lens(x, ta, tb, False)) for x in lin(0, 1)] + [(100, 0), (0, 0)], "BLUE", 0.18)
    P.line([(100 * x, lens(x, ta, tb, True)) for x in lin(0, 1)], "ACC", 2.4)
    P.line([(100 * x, lens(x, ta, tb, False)) for x in lin(0, 1)], "ACC", 2.4)
    P.frame([(0, "A"), (100, "B")], (), "Composition", "Temperature")
    x0 = 50
    P.vseg(x0, 0, 1, "GREEN", 1.4)
    t1 = 0.66
    xl = (((t1 - ta) / (tb - ta)) ** (1 / 0.62)) * 100
    xs = (((t1 - ta) / (tb - ta)) ** (1 / 1.9)) * 100
    P.hseg(0, xs, t1)
    P.dot(xl, t1, 4.5, "HEAD"); P.dot(xs, t1, 4.5, "HEAD")
    P.text(xl, t1, sub("L", "1"), "HEAD", dx=-4, dy=-10)
    P.text(xs, t1, sub("SS", "1"), "HEAD", dx=20, dy=18)
    P.text(0, t1, sub("T", "1"), "HEAD", "end", dx=-8, dy=4)
    for y, name in ((0.92, "L"), (t1, None), (0.22, "SS")):
        circle(c, P.p(x0, y), 4.5, "GREEN", 1.6, "none")
    P.text(x0, 0.92, sub("L", "system"), "GREEN", dx=36, dy=-8)
    P.text(x0, 0.22, sub("SS", "system"), "GREEN", dx=46, dy=-8)
    bx = 400
    boxes = ((0.92, "All liquid"), (t1, "Crystallites of SS₁ in L₁"), (0.22, "Polycrystalline solid"))
    for y, lab in boxes:
        py = P.p(x0, y)[1]
        rect(c, bx, py - 32, 64, 64, "HEAD", 1.4)
        line(c, (P.p(x0, y)[0] + 6, py), (bx - 2, py), "EDGE", 1, head=True)
        text(c, (bx + 74, py + 4), lab, "TEXT", "start", 12.5)
    py = P.p(x0, t1)[1]
    for (u, v, r) in ((415, py - 16, 9), (445, py - 12, 8), (420, py + 14, 10), (450, py + 18, 7)):
        circle(c, (u, v), r, "HEAD", 1.3)
    py = P.p(x0, 0.22)[1]
    for a, b in (((400, py - 6), (422, py - 10)), ((422, py - 10), (440, py - 32)), ((422, py - 10), (430, py + 10)),
                 ((430, py + 10), (400, py + 22)), ((430, py + 10), (464, py + 14)), ((440, py - 32 + 22), (464, py - 6)),
                 ((422, py - 10), (440, py - 10)), ((440, py - 10), (464, py - 6)), ((430, py + 10), (418, py + 32))):
        line(c, a, b, "HEAD", 1.2)
    REG.put("iso-micro", c, "Microstructure along the cooling of an isomorphous alloy",
            "An alloy cooled through the isomorphous diagram: all liquid above the liquidus, crystallites of solid "
            "solution SS₁ in a liquid L₁ at T₁, and a polycrystalline single-phase solid below the solidus. Redrawn "
            "from Session 7 Slide 10")


def complete_solubility():
    c = Canvas(640, 420)
    P = Plot(c, (90, 30, 420, 250), (0, 100), (1100, 1600))
    liq = [(100 * x, 1118 + 435 * x ** 0.45) for x in lin(0, 1)]
    sol = [(100 * x, 1118 + 435 * x ** 1.5) for x in lin(0, 1)]
    P.area([(0, 1600)] + liq + [(100, 1600)], "BLUE", 0.08)
    P.area(sol + [(100, 1100), (0, 1100)], "BLUE", 0.18)
    P.line(liq, "ACC", 2.4); P.line(sol, "ACC", 2.4)
    P.frame([(0, "0"), (20, "20"), (40, "40"), (60, "60"), (80, "80"), (100, "100")],
            [(1100, "1100"), (1200, "1200"), (1300, "1300"), (1400, "1400"), (1500, "1500"), (1600, "1600")],
            "Composition (mole fraction of B, %)", "Temperature (°C)")
    P.text(0, 1118, "1118", "TEXT", "start", 11.5, "400", dx=6, dy=-6)
    P.text(100, 1553, "1553", "TEXT", "end", 11.5, "400", dx=-6, dy=-8)
    P.text(30, 1520, "Liquid", size=13.5)
    P.text(42, 1310, "Liquid + Solid", size=12)
    P.text(62, 1200, "Solid", size=13.5)
    P.text(72, 1530, "liquidus", "TEXT", size=11.5, weight="400", dx=-20, dy=-6)
    P.text(80, 1380, "solidus", "TEXT", size=11.5, weight="400", dx=20)
    rows = (("A", 0), ("mostly A", 3), ("A + B", 8), ("B", 16))
    rng = [5, 11, 2, 14, 7, 0, 9, 13, 3, 10, 6, 15, 1, 12, 4, 8]
    for k, (lab, nb) in enumerate(rows):
        u0 = 92 + k * 132
        bset = set(rng[:nb])
        for i in range(4):
            for j in range(4):
                isb = (i * 4 + j) in bset
                circle(c, (u0 + 14 + j * 22, 316 + i * 20), 9, "HEAD", 1.2, "none" if isb else "PINK", None if isb else 0.55)
        text(c, (u0 + 47, 414), lab, "TEXT", "middle", 12)
    text(c, (450, 60), "● A atom", "PINK", "start", 12.5, "700")
    text(c, (450, 80), "○ B atom", "HEAD", "start", 12.5, "700")
    REG.put("complete-solubility", c, "Complete solid solubility",
            "Isomorphous system with complete solid solubility, from the melting point of A (1118 °C) to that of B "
            "(1553 °C): B atoms replace A atoms in the same crystal lattice at any proportion, so the solid is a single "
            "phase, and the alloys solidify over a range of temperatures. Redrawn from Session 7 Slide 11")


def gibbs():
    c = Canvas(720, 340)
    # left: one component, F = C - P + 2
    line(c, (60, 270), (320, 270)); line(c, (60, 40), (60, 270))
    tp = (110, 205)
    sub_c = [(64 + k * 46 / 20, 268 - (268 - tp[1]) * (k / 20) ** 0.8) for k in range(21)]
    vap = [(tp[0] + k * 6, tp[1] - 160 * ((k * 6) / 120) ** 0.62) for k in range(21)]
    melt = [tp, (300, 222)]
    for pts in (sub_c, vap, melt):
        poly(c, pts, "BLUE", 2.2)
    dot(c, tp, 4.5, "GREEN")
    text(c, (190, 20), "one component: F = C − P + 2", "HEAD", "middle", 12.5, "700")
    text(c, (90, 80), "Gas", "HEAD", "middle", 13, "700")
    text(c, (220, 140), "Liquid", "HEAD", "middle", 13, "700")
    text(c, (220, 250), "Solid", "HEAD", "middle", 13, "700")
    text(c, (232, 165), "F = 1 − 1 + 2 = 2", "GREEN", "middle", 12, "700")
    text(c, (175, 90), "F = 1 − 2 + 2 = 1", "GREEN", "start", 12, "700")
    line(c, (173, 86), (148, 98), "GREEN", 1, head=True)
    text(c, (122, 318), "F = 1 − 3 + 2 = 0", "GREEN", "middle", 12, "700")
    line(c, (118, 306), (tp[0] + 2, tp[1] + 6), "GREEN", 1, head=True)
    text(c, (250, 288), "Pressure (log scale)", "TEXT", "middle", 12)
    text(c, (64, 34), "Temperature", "TEXT", "start", 12)
    # right: two components at 1 atm, F = C - P + 1
    ta, tb = 0.42, 0.85
    P = Plot(c, (440, 40, 690, 270), (0, 100), (0, 1))
    liq = [(100 * x, lens(x, ta, tb, True)) for x in lin(0, 1)]
    sol = [(100 * x, lens(x, ta, tb, False)) for x in lin(0, 1)]
    P.area([(0, 1)] + liq + [(100, 1)], "BLUE", 0.08)
    P.area(sol + [(100, 0), (0, 0)], "BLUE", 0.18)
    P.line(liq, "ACC", 2.2); P.line(sol, "ACC", 2.2)
    P.frame([(0, "A"), (100, "B")], (), "Composition", "")
    text(c, (565, 20), "two components at 1 atm: F = C − P + 1", "HEAD", "middle", 12.5, "700")
    P.text(28, 0.88, "F = 2 − 1 + 1 = 2", "GREEN", size=12)
    P.text(38, 0.555, "F = 2 − 2 + 1 = 1", "GREEN", size=11.5)
    P.text(45, 0.18, "F = 2 − 1 + 1 = 2", "GREEN", size=12)
    P.dot(100, tb, 4.5, "GREEN")
    P.text(100, tb, "F = 1 − 2 + 1 = 0", "GREEN", "end", 12, dx=-8, dy=-12)
    xb = 85
    P.dot(xb, lens(xb / 100, ta, tb, False), 4, "HEAD")
    P.text(70, 0.38, "F = 2 − 2 + 1 = 1", "HEAD", "middle", 11.5)
    line(c, P.p(76, 0.42), P.p(xb - 1, lens(xb / 100, ta, tb, False) - 0.02), "HEAD", 1, head=True)
    REG.put("gibbs", c, "Gibbs phase rule in a unary and a binary diagram",
            "Degrees of freedom from F = C − P + N. Left, one component with pressure and temperature free (N = 2): "
            "F = 2 in a single-phase region, 1 on a two-phase line, 0 at the triple point. Right, two components at "
            "1 atm (N = 1): F = 2 in L or in the solid, 1 in L + solid and on its boundaries, 0 at the melting point "
            "of a pure component. Redrawn from Session 7 Slide 13")


def _cuni_liq(x):
    return 1200 + (1250 - 1200) / 12 * (x - 20)


def _cuni_sol(x):
    return 1250 + (1250 - 1162) / 23 * (x - 43)


def tie_line():
    c = Canvas(600, 360)
    P = Plot(c, (80, 30, 520, 280), (20, 50), (1150, 1340))
    P.frame([(20, "20"), (30, "30"), (40, "40"), (50, "50")], [(1200, "1200"), (1300, "1300")],
            "Composition (wt% Ni)", "Temperature (°C)", grid=(("x", 30), ("x", 40), ("y", 1200), ("y", 1300)), xl_dy=62)
    liq = [(x, _cuni_liq(x)) for x in (20, 50)]
    sol = [(x, _cuni_sol(x)) for x in (20, 50)]
    P.area([(20, 1340)] + liq + [(50, 1340)], "BLUE", 0.08)
    P.area(sol + [(50, 1150), (20, 1150)], "BLUE", 0.18)
    P.line(liq, "ACC", 2.6); P.line(sol, "ACC", 2.6)
    P.line([(32, 1250), (43, 1250)], "BLUE", 2.4)
    for x, s in ((32, sub("C", "L")), (35, sub("C", "0")), (43, sub("C", "α"))):
        P.vseg(x, 1150, 1250, "HEAD", 1.2, "6,4")
        P.text(x, 1150, s, "HEAD", dy=36)
    P.dot(35, 1250, 5, "GREEN")
    P.text(35, 1250, "B", "GREEN", dx=0, dy=-10)
    a, b, d = P.p(32, 1195), P.p(35, 1195), P.p(43, 1195)
    bracket(c, a, b, "R")
    bracket(c, b, d, "S")
    P.text(25, 1312, "Liquid", "HEAD", size=13)
    P.text(42, 1270, "α + Liquid", "HEAD", size=12.5)
    P.text(25.5, 1203, "α + Liquid", "HEAD", size=12.5)
    P.text(46, 1210, "α", "HEAD", size=14)
    P.text(23, 1160, "α", "HEAD", size=14)
    P.text(28, 1285, "tie line", "BLUE", size=12.5)
    line(c, P.p(29.5, 1280), P.p(33.5, 1252), "BLUE", 1, head=True)
    REG.put("tie-line", c, "Tie line and lever rule in the Cu-Ni system",
            "Alloy B, 35 wt% Ni at 1250 °C, in the α + L region of the Cu-Ni diagram. The tie line through B ends on "
            "the liquidus at C_L = 32 wt% Ni and on the solidus at C_α = 43 wt% Ni; R and S are the lengths of its two "
            "arms. Redrawn from Session 7 Slides 15-21")


def coring():
    c = Canvas(700, 440)
    P = Plot(c, (80, 30, 470, 380), (15, 55), (1150, 1320))
    P.frame([(20, "20"), (30, "30"), (40, "40"), (50, "50")], [(1200, "1200"), (1300, "1300")],
            "Composition (wt% Ni)", "Temperature (°C)")
    P.line([(15, _cuni_liq(15)), (20 + 120 / (50 / 12), 1320)], "ACC", 2.4)
    P.line([(43 - 100 * 23 / 88, 1150), (55, _cuni_sol(55))], "ACC", 2.4)
    pts = {"a′": (1300, None, None, None), "b′": (_cuni_liq(35), 35, 46, 46), "c′": (_cuni_liq(29), 29, 40, 42),
           "d′": (_cuni_liq(24), 24, 35, 38), "e′": (_cuni_liq(21), 21, 31, 35), "f′": (1175, None, None, None)}
    P.vseg(35, 1150, 1315, "HEAD", 1.2, "6,4")
    noneq = []
    for name, (t, cl, ce, cav) in pts.items():
        P.dot(35, t, 4, "HEAD")
        P.text(35, t, name, "HEAD", "start", 12.5, dx=-22, dy=-6)
        if cl is None:
            continue
        P.line([(cl, t), (max(ce, cav), t)], "BLUE", 2.4)
        P.text(cl, t, f"L({cl})", "TEXT", "end", 11.5, "700", dx=-4, dy=4)
        P.text(ce, t, f"α({ce})", "TEXT", "middle", 11.5, "700", dy=-7)
        if cav != ce:
            P.text(cav, t, f"α({cav})", "PINK", "start", 11.5, "700", dx=6, dy=4)
        noneq.append((cav, t))
    P.line(noneq + [(35 - 1.0, _cuni_liq(21) - 6)], "PINK", 1.6, "6,4")
    P.text(35, 1300, "L (35 Ni)", "TEXT", "start", 11.5, "700", dx=8, dy=4)
    P.text(22, 1300, "L", size=14)
    P.text(49, 1300, "α + L", size=13)
    P.text(50, 1200, "α", size=14)
    # cored microstructures (schematic of the slide sketches)
    u0 = 500
    rings = ((90, ["46", "40"]), (210, ["46", "40", "35", "31"]), (330, ["46", "40", "35", "31"]))
    for k, (yy, labs) in enumerate(rings):
        cx, cy = u0 + 40, yy
        circle(c, (cx, cy), 34, "HEAD", 1.4, "BLUE" if k < 2 else "PINK", 0.08 if k < 2 else 0.16)
        for j, lab in enumerate(labs):
            circle(c, (cx, cy), 6 + 6 * j, "PINK", 1.2, "PINK", 0.12)
        text(c, (cx + 44, cy - 10), "α: " + " → ".join(labs) + " Ni", "TEXT", "start", 11.5)
        text(c, (cx + 44, cy + 8), "in liquid" if k < 2 else "solid, cored", "TEXT", "start", 11.5)
        line(c, P.p(35.6, {0: _cuni_liq(29), 1: _cuni_liq(21), 2: 1175}[k]), (cx - 36, cy), "EDGE", 1)
    REG.put("coring", c, "Non-equilibrium solidification of a Cu-35 wt% Ni alloy",
            "Fast cooling of Cu-35 wt% Ni: at each temperature only the surface of the growing crystals reaches the "
            "equilibrium composition (blue tie lines), so the average composition of the solid (dashed line) stays "
            "richer in Ni: 42 instead of 40 at c′, 38 instead of 35 at d′. Liquid remains below the equilibrium "
            "solidus and the grains end up cored, from 46 % Ni at the centre to 31 % Ni at the edge. Redrawn from "
            "Session 7 Slide 23")


def coring_nicu():
    c = Canvas(560, 360)
    P = Plot(c, (80, 30, 480, 300), (0, 80), (0, 10))
    P.frame([(0, "100 % Ni"), (30, "30 % Cu")], (), "Composition (wt% Cu)", "Temperature")
    liq_x = [0, 30, 40, 49, 55, 62, 68, 74]
    eq_x = [0, 5, 9, 13, 18, 30, 38, 44]
    ne_x = [0, 5, 8, 11, 14, 18, 24, 30]
    temps = [9.2, 8.4, 7.4, 6.4, 5.4, 4.4, 3.4, 2.4]
    P.line(list(zip(liq_x, temps)), "ACC", 2.4)
    P.line(list(zip(eq_x, temps)), "ACC", 2.2)
    P.line(list(zip(ne_x, temps)), "PINK", 2.0, "6,4")
    P.vseg(30, 0, 9.8, "HEAD", 1.2, "6,4")
    for k in range(1, 8):
        t = temps[k]
        P.hseg(0, liq_x[k], t, "EDGE", 0.8, "3,3")
        P.dot(liq_x[k], t, 3.2, "HEAD"); P.dot(eq_x[k], t, 3.2, "HEAD"); P.dot(ne_x[k], t, 3.2, "PINK")
        P.text(liq_x[k], t, sub("L", k), "TEXT", "start", 11.5, dx=5, dy=-4)
        if k > 1:
            P.text(eq_x[k], t, sub("α", k), "TEXT", "start", 11.5, dx=5, dy=-4)
            P.text(ne_x[k], t, sub("α′", k), "PINK", "end", 11.5, dx=-5, dy=12)
        P.text(0, t, sub("T", k), "HEAD", "end", 12, dx=-8, dy=4)
    P.text(0, 9.2, "1455", "HEAD", "end", 12, dx=-8, dy=4)
    P.text(0, 9.8, sub("T", 0), "HEAD", "end", 12, dx=-8, dy=-2)
    P.dot(30, 9.8, 3.5, "GREEN")
    P.text(62, 8.6, "Liquid", size=13.5)
    P.text(38, 6.0, "α + liquid", size=12.5)
    P.text(8, 2.0, "α", size=14)
    P.text(44, 1.6, "equilibrium solidus", "ACC", "start", 11.5, dx=-4)
    P.text(31, 0.8, "non-equilibrium solidus", "PINK", "start", 11.5)
    REG.put("coring-nicu", c, "Equilibrium and non-equilibrium solidus of a Ni-30 wt% Cu alloy",
            "Ni-30 wt% Cu cooled from T₀: in equilibrium the solid follows α₁ … α₅ and solidification ends at T₅; "
            "with fast cooling the average composition of the solid follows α′₂ … α′₇ (non-equilibrium solidus) and "
            "solidification ends only at T₇. Schematic redrawn from Session 7 Slide 24")


def eutectic_generic():
    c = Canvas(760, 400)
    P = Plot(c, (170, 30, 540, 320), (0, 100), (0, 100))
    ta, tb, te, ca, ce, cb = 78, 70, 42, 30, 59, 89
    liq_a = [(x, ta - (ta - te) * x / ce + 0.004 * x * (ce - x)) for x in lin(0, ce)]
    liq_b = [(x, te + (tb - te) * ((x - ce) / (100 - ce)) ** 0.85) for x in lin(ce, 100, 20)]
    sol_a = [(ca * ((ta - t) / (ta - te)) ** 0.8, t) for t in lin(ta, te)]
    sol_b = [(100 - (100 - cb) * ((tb - t) / (tb - te)) ** 0.8, t) for t in lin(tb, te, 20)]
    solv_a = [(ca - (ca - 12) * (1 - t / te) ** 1.3, t) for t in lin(te, 0)]
    solv_b = [(cb + (97 - cb) * (1 - t / te) ** 1.3, t) for t in lin(te, 0)]
    P.area([(0, 100)] + liq_a + liq_b + [(100, 100)], "BLUE", 0.08)
    P.area(sol_a + solv_a + [(0, 0)], "BLUE", 0.18)
    P.area([(100, tb)] + sol_b + solv_b + [(100, 0)], "BLUE", 0.18)
    for cv in (liq_a, liq_b, sol_a, sol_b, solv_a, solv_b):
        P.line(cv, "ACC", 2.4)
    P.line([(ca, te), (cb, te)], "ACC", 2.4)
    P.frame([(0, "A"), (100, "B")], (), "Composition", "Temperature", xl_dy=62)
    P.vseg(ce, 0, 100, "HEAD", 1, "3,4")
    P.text(ce, 0, "eutectic composition", "GREEN", dy=36, size=12)
    P.hseg(0, ca, te, "HEAD", 1, "3,4")
    P.text(0, te, "eutectic temperature", "GREEN", "end", 12, dx=-8, dy=4)
    P.text(45, 85, "L", size=15)
    P.text(8, 30, "α", size=15)
    P.text(95, 30, "β", size=15)
    P.text(39, 50, "α + L", size=13.5)
    P.text(77, 50, "L + β", size=13.5)
    P.text(56, 22, "α + β", size=14)
    P.text(14, 72, "liquidus", "TEXT", "start", 11.5, dx=10)
    P.text(10, 56, "solidus", "TEXT", "start", 11.5, dx=8)
    P.text(19, 18, "solvus", "TEXT", "start", 11.5)
    circle(c, P.p(ce, 82), 5, "GREEN", 1.6)
    circle(c, P.p(ce, 28), 5, "GREEN", 1.6)
    bx = 600
    for (yy, lab1, lab2), lam in (((82, "All liquid", "(L at the eutectic composition)"), False),
                                  ((28, "Eutectic microstructure:", "fine alternating layers of α and β"), True)):
        y = P.p(ce, yy)[1]
        rect(c, bx, y - 30, 60, 60, "HEAD", 1.4)
        line(c, (P.p(ce, yy)[0] + 7, y), (bx - 2, y), "EDGE", 1, head=True)
        if lam:
            for k in range(1, 10):
                line(c, (bx + k * 6, y - 30), (bx + k * 6, y + 30), "HEAD", 1.2)
        text(c, (bx - 6, y + 46), lab1, "TEXT", "start", 11.5, "700")
        text(c, (bx - 6, y + 62), lab2, "TEXT", "start", 11.5)
    REG.put("eutectic-generic", c, "Binary eutectic system",
            "Two components with partial solid solubility and an invariant eutectic reaction: the liquidus, solidus "
            "and solvus lines bound the regions L, α, β, α + L, L + β and α + β; the liquid of eutectic composition "
            "solidifies at the eutectic temperature into fine alternating layers of α and β. Redrawn from Session 7 "
            "Slide 26")


def eutectic_cooling():
    c = Canvas(660, 290)
    P = Plot(c, (70, 30, 330, 240), (0, 10), (0, 330))
    P.frame((), [(0, "0"), (100, "100"), (183, "183"), (300, "300")], "time", "Temperature (°C)", box=False)
    P.line([(0.1, 325), (0.6, 260), (1.4, 205), (2.0, 183), (7.2, 183), (8.2, 130), (9.6, 55)], "ACC", 2.6)
    P.hseg(0, 2.0, 183)
    P.text(4.6, 183, "L → α + β at constant T", "HEAD", size=12, dy=-10)
    u0, y0 = 420, 140
    text(c, (530, 50), "Eutectic reaction:  L → α + β", "HEAD", "middle", 14, "700")
    line(c, (u0 + 20, y0), (u0 + 220, y0), "ACC", 2.4)
    c.add(f'<path d="M{u0},{y0 - 40} Q{u0 + 8},{y0} {u0 + 20},{y0}" fill="none" stroke="ACC" stroke-width="2.4"/>')
    c.add(f'<path d="M{u0 - 2},{y0 + 30} Q{u0 + 6},{y0 + 6} {u0 + 20},{y0}" fill="none" stroke="ACC" stroke-width="2.4"/>')
    c.add(f'<path d="M{u0 + 240},{y0 - 40} Q{u0 + 232},{y0} {u0 + 220},{y0}" fill="none" stroke="ACC" stroke-width="2.4"/>')
    c.add(f'<path d="M{u0 + 242},{y0 + 30} Q{u0 + 234},{y0 + 6} {u0 + 220},{y0}" fill="none" stroke="ACC" stroke-width="2.4"/>')
    c.add(f'<path d="M{u0 + 80},{y0 - 50} Q{u0 + 110},{y0 - 20} {u0 + 118},{y0}" fill="none" stroke="ACC" stroke-width="2.4"/>')
    c.add(f'<path d="M{u0 + 156},{y0 - 50} Q{u0 + 126},{y0 - 20} {u0 + 118},{y0}" fill="none" stroke="ACC" stroke-width="2.4"/>')
    text(c, (u0 - 10, y0 - 6), "α", "HEAD", "end", 14, "700")
    text(c, (u0 + 252, y0 - 6), "β", "HEAD", "start", 14, "700")
    text(c, (u0 + 118, y0 - 46), "L", "HEAD", "middle", 14, "700")
    text(c, (u0 + 118, y0 + 26), "α + β", "HEAD", "middle", 13.5, "700")
    REG.put("eutectic-cooling", c, "Cooling curve of the eutectic alloy and the eutectic reaction",
            "Left: the eutectic alloy solidifies at a single temperature (183 °C for Pb-Sn), with a thermal arrest like "
            "a pure metal. Right: around the eutectic point, the liquid L transforms into the two solids α and β. "
            "Redrawn from Session 7 Slide 27")


def pbsn():
    c = Canvas(620, 390)
    P = Plot(c, (80, 30, 540, 300), (0, 100), (0, 350))
    pbsn_diagram(c, P, PBSN)
    P.frame([(0, "0 (Pb)"), (20, "20"), (40, "40"), (60, "60"), (80, "80"), (100, "100 (Sn)")],
            [(0, "0"), (100, "100"), (200, "200"), (300, "300")], "Composition (wt% Sn)", "Temperature (°C)", xl_dy=78)
    for x in (PBSN["ca"], PBSN["ce"], PBSN["cb"]):
        P.vseg(x, 0, PBSN["te"], "HEAD", 1, "3,4")
        P.text(x, 0, f"{x}", "GREEN", size=12, dy=52 if x != PBSN["ce"] else 36)
    P.dot(PBSN["ce"], PBSN["te"], 4.5, "GREEN")
    REG.put("pbsn", c, "The Pb-Sn eutectic system",
            "Pb-Sn diagram: eutectic point at 61.9 wt% Sn and 183 °C; at that temperature the maximum solubility is "
            "18.3 wt% Sn in α (Pb-rich) and the β phase (Sn-rich) contains 97.8 wt% Sn. Melting points 327 °C (Pb) and "
            "232 °C (Sn). Redrawn from Session 7 Slides 28 and 32")


def hypoeutectic():
    c = Canvas(700, 340)
    P = Plot(c, (80, 30, 400, 280), (0, 100), (0, 400))
    pbsn_diagram(c, P, PBSN, values=False)
    P.frame([(0, "Pb"), (20, "20"), (40, "40"), (60, "60"), (80, "80"), (100, "Sn")],
            [(0, "0"), (100, "100"), (200, "200"), (300, "300"), (400, "400")], "Composition (wt% Sn)", "Temperature (°C)")
    x0 = 30
    P.vseg(x0, 0, 390, "GREEN", 1.6, "6,4")
    for t in (300, 220, 184, 120):
        P.dot(x0, t, 3.6, "GREEN")
    Q = Plot(c, (480, 30, 680, 280), (0, 10), (0, 400))
    Q.frame((), [(0, "0"), (100, "100"), (183, "183"), (260, "260"), (300, "300"), (400, "400")], "time", "", box=False)
    Q.line([(0.1, 390), (1.4, 300), (2.6, 260), (4.2, 220), (5.4, 183), (7.2, 183), (8.2, 120), (9.6, 40)], "ACC", 2.6)
    Q.hseg(0, 2.6, 260); Q.hseg(0, 5.4, 183)
    Q.text(1.2, 300, "L", "HEAD", "end", 12.5, dx=-6)
    Q.text(3.9, 238, "α + L", "HEAD", "start", 12.5, dx=6)
    Q.text(6.3, 183, "L → α + β", "HEAD", size=12, dy=18)
    Q.text(8.6, 120, "α + eutectic", "HEAD", "start", 12, dx=6)
    Q.text(2.6, 260, "liquidus", "TEXT", "start", 11.5, dx=4, dy=-8)
    REG.put("hypoeutectic", c, "Cooling of a hypoeutectic Pb-Sn alloy",
            "Hypoeutectic Pb-Sn alloy (dashed line, about 30 wt% Sn in the slide figure): primary α forms between the "
            "liquidus (260 °C on the cooling curve) and the eutectic temperature; at 183 °C the remaining liquid, now "
            "of eutectic composition, solidifies at constant temperature; the final structure is primary α plus "
            "eutectic. Redrawn from Session 7 Slide 30")


def hypereutectic():
    c = Canvas(700, 340)
    P = Plot(c, (80, 30, 400, 280), (0, 100), (0, 100))
    ta, tb, te, ca, ce, cb = 86, 74, 42, 27, 52, 86
    liq_a = [(x, ta - (ta - te) * x / ce) for x in lin(0, ce, 4)]
    liq_b = [(x, te + (tb - te) * (x - ce) / (100 - ce)) for x in lin(ce, 100, 4)]
    sol_a = [(ca * ((ta - t) / (ta - te)) ** 0.8, t) for t in lin(ta, te)]
    sol_b = [(100 - (100 - cb) * ((tb - t) / (tb - te)) ** 0.8, t) for t in lin(tb, te, 20)]
    solv_a = [(ca - (ca - 12) * (1 - t / te) ** 1.3, t) for t in lin(te, 0)]
    solv_b = [(cb + (96 - cb) * (1 - t / te) ** 1.3, t) for t in lin(te, 0)]
    P.area([(0, 100)] + liq_a + liq_b + [(100, 100)], "BLUE", 0.08)
    P.area(sol_a + solv_a + [(0, 0)], "BLUE", 0.18)
    P.area([(100, tb)] + sol_b + solv_b + [(100, 0)], "BLUE", 0.18)
    for cv in (liq_a, liq_b, sol_a, sol_b, solv_a, solv_b):
        P.line(cv, "ACC", 2.4)
    P.line([(ca, te), (cb, te)], "ACC", 2.4)
    P.frame([(0, "A"), (100, "B")], (), "Composition", "Temperature")
    x0 = 76
    P.vseg(x0, 0, 98, "GREEN", 1.6, "6,4")
    for t in (55, 43.5, 25):
        P.dot(x0, t, 3.6, "GREEN")
    P.text(45, 85, "L", size=15)
    P.text(8, 30, "α", size=15)
    P.text(95, 30, "β", size=15)
    P.text(32, 50, "α + L", size=13)
    P.text(68, 62, "L + β", size=13)
    P.text(50, 22, "α + β", size=14)
    Q = Plot(c, (480, 30, 680, 280), (0, 10), (0, 10))
    Q.frame((), [(4.2, sub("T", "E")), (6.4, sub("T", "L"))], "time", "", box=False)
    Q.line([(0.1, 9.6), (1.6, 6.4), (3.2, 5.0), (4.0, 4.2), (6.6, 4.2), (7.8, 2.6), (9.6, 0.8)], "ACC", 2.6)
    Q.hseg(0, 1.6, 6.4); Q.hseg(0, 4.0, 4.2)
    Q.text(1.0, 8.0, "L", "HEAD", "start", 12.5, dx=6)
    Q.text(2.6, 5.7, "β + L", "HEAD", "start", 12.5, dx=6)
    Q.text(5.3, 4.2, "L → α + β", "HEAD", size=12, dy=18)
    Q.text(7.6, 2.6, "β + eutectic", "HEAD", "start", 12, dx=6)
    REG.put("hypereutectic", c, "Cooling of a hypereutectic alloy",
            "Hypereutectic alloy (dashed line, between the eutectic composition and the β limit): primary β forms "
            "between the liquidus T_L and the eutectic temperature T_E; at T_E the remaining liquid gives the eutectic; "
            "the final structure is primary β plus eutectic. Redrawn from Session 7 Slide 31")


def eutectic_lever():
    c = Canvas(640, 380)
    P = Plot(c, (80, 30, 560, 290), (0, 100), (0, 350))
    pbsn_diagram(c, P, PBSN, values=False)
    P.frame([(0, "(Pb)"), (100, "(Sn)")], [(0, "0"), (100, "100"), (200, "200"), (300, "300")],
            "Composition (wt% Sn)", "Temperature (°C)", xl_dy=80)
    c4 = 34
    for x, s in ((PBSN["ca"], "18.3"), (c4, "C′₄"), (PBSN["ce"], "61.9"), (PBSN["cb"], "97.8")):
        P.vseg(x, 0, PBSN["te"], "HEAD", 1.1, "6,4")
        P.text(x, 0, s, "GREEN" if x != c4 else "HEAD", size=12.5, dy=36 if x != c4 else 52)
    y = 160
    a, b, d, e = P.p(PBSN["ca"], y), P.p(c4, y), P.p(PBSN["ce"], y), P.p(PBSN["cb"], y)
    bracket(c, a, b, "P"); bracket(c, b, d, "Q"); bracket(c, d, e, "R")
    REG.put("eutectic-lever", c, "Lever rule in the Pb-Sn eutectic diagram",
            "Just below the eutectic temperature the tie line runs from 18.3 to 97.8 wt% Sn. For an alloy C′₄ the "
            "segments P, Q and R give the fractions of primary α and eutectic (from P and Q) and of the phases α and β "
            "(from P + Q + R). Redrawn from Session 7 Slide 32")


# --------------------------------------------------------------------------- Session 8 figures (Part II)
def bisect(f, a, b, n=60):
    """Root of f in [a, b] (f(a) and f(b) of opposite sign)."""
    fa = f(a)
    for _ in range(n):
        m = (a + b) / 2
        if (f(m) > 0) == (fa > 0):
            a, fa = m, f(m)
        else:
            b = m
    return (a + b) / 2


def precip_pbsn():
    c = Canvas(640, 400)
    P = Plot(c, (80, 30, 520, 320), (0, 50), (0, 400))
    liq_a, _, sol_a, _, solv_a, _ = pbsn_curves(PBSN)
    liq = [(x, t) for x, t in liq_a if x <= 50]
    P.area([(0, 400)] + liq + [(50, 400)], "BLUE", 0.08)
    P.area(sol_a + solv_a + [(0, 0)], "BLUE", 0.16)
    for cv in (liq, sol_a, solv_a):
        P.line(cv, "ACC", 2.2)
    P.line([(PBSN["ca"], PBSN["te"]), (50, PBSN["te"])], "ACC", 2.2)
    P.frame([(0, "0"), (10, "10"), (20, "20"), (30, "30"), (40, "40"), (50, "50")],
            [(0, "0"), (100, "100"), (200, "200"), (300, "300"), (400, "400")], "Composition (wt% Sn)", "Temperature (°C)")
    for x, pts, lab in ((1, ((350, "a"), (325, "b"), (270, "c")), sub("C", "1") + " = 1"),
                        (16, ((350, "d"), (270, "e"), (192, "f"), (121, "g")), sub("C", "2") + " = 16")):
        P.vseg(x, 0, 395, "GREEN", 1.5, "6,4")
        P.text(x, 0, lab, "GREEN", "middle", 12, dy=52)
        for t, s in pts:
            P.dot(x, t, 4, "GREEN")
            P.text(x, t, s, "GREEN", "start", 13, dx=7, dy=-4)
    P.text(32, 350, "L", size=14)
    P.text(32, 225, "α + L", size=13)
    P.text(8, 60, "α", size=14, dx=-12)
    P.text(34, 90, "α + β", size=13.5)
    P.text(40, 265, "liquidus", "TEXT", "middle", 11.5, "400")
    P.text(12, 240, "solidus", "TEXT", "start", 11.5, "400")
    P.text(9, 120, "solvus", "TEXT", "start", 11.5, "400")
    REG.put("precip-pbsn", c, "Pb-Sn alloys below and above the solid solubility limit",
            "Pb-1 wt% Sn (a liquid, b α starts to form, c only α) never crosses the solvus; Pb-16 wt% Sn (d liquid, "
            "e α + L, f only α) crosses the solvus on cooling and at g contains α + β. Redrawn from Session 8 Slides 2 and 4")


def generic_eutectic(P, ta=78, tb=70, te=42, ca=30, ce=59, cb=89, a0=12, b0=97):
    """Draw the schematic eutectic diagram of the slides on P (0-100 x 0-100) and return its boundary functions."""
    f_liq_a = lambda x: ta - (ta - te) * x / ce + 0.004 * x * (ce - x)        # noqa: E731
    f_sol_a = lambda t: ca * ((ta - t) / (ta - te)) ** 0.8                    # noqa: E731
    f_solv_a = lambda t: ca - (ca - a0) * (1 - t / te) ** 1.3                # noqa: E731
    f_solv_b = lambda t: cb + (b0 - cb) * (1 - t / te) ** 1.3                # noqa: E731
    liq_a = [(x, f_liq_a(x)) for x in lin(0, ce)]
    liq_b = [(x, te + (tb - te) * ((x - ce) / (100 - ce)) ** 0.85) for x in lin(ce, 100, 20)]
    sol_a = [(f_sol_a(t), t) for t in lin(ta, te)]
    sol_b = [(100 - (100 - cb) * ((tb - t) / (tb - te)) ** 0.8, t) for t in lin(tb, te, 20)]
    solv_a = [(f_solv_a(t), t) for t in lin(te, 0)]
    solv_b = [(f_solv_b(t), t) for t in lin(te, 0)]
    P.area([(0, 100)] + liq_a + liq_b + [(100, 100)], "BLUE", 0.08)
    P.area(sol_a + solv_a + [(0, 0)], "BLUE", 0.18)
    P.area([(100, tb)] + sol_b + solv_b + [(100, 0)], "BLUE", 0.18)
    for cv in (liq_a, liq_b, sol_a, sol_b, solv_a, solv_b):
        P.line(cv, "ACC", 2.4)
    P.line([(ca, te), (cb, te)], "ACC", 2.4)
    return dict(liq_a=f_liq_a, sol_a=f_sol_a, solv_a=f_solv_a, solv_b=f_solv_b)


def precip_generic():
    c = Canvas(720, 380)
    P = Plot(c, (330, 30, 680, 320), (0, 100), (0, 100))
    f = generic_eutectic(P)
    P.frame([(0, "A"), (20, "20"), (100, "B")], (), "Composition (wt% B)", "Temperature")
    x0 = 20
    P.vseg(x0, 0, 95, "GREEN", 1.5, "6,4")
    t1 = 64
    cl1 = bisect(lambda x: f["liq_a"](x) - t1, 0.1, 58)
    cs1 = f["sol_a"](t1)
    P.line([(cs1, t1), (cl1, t1)], "BLUE", 1.8)
    P.dot(cs1, t1, 3.6, "HEAD"); P.dot(cl1, t1, 3.6, "HEAD")
    P.text(cs1, t1, sub("α", "1"), "HEAD", "end", 12.5, dx=-5, dy=4)
    P.text(cl1, t1, sub("L", "1"), "HEAD", "start", 12.5, dx=5, dy=4)
    for t, k in ((14, "2"), (6, "3")):
        ca, cb = f["solv_a"](t), f["solv_b"](t)
        P.line([(ca, t), (cb, t)], "BLUE", 1.2, "4,4")
        P.dot(ca, t, 3.6, "HEAD"); P.dot(cb, t, 3.6, "HEAD")
        P.text(ca, t, sub("α", k), "HEAD", "end", 12.5, dx=-5, dy=4)
        P.text(cb, t, sub("β", k), "HEAD", "start", 12.5, dx=5, dy=4)
    marks = ((88, sub("L", "system")), (t1, ""), (35, sub("α", "system")), (14, ""))
    for t, lab in marks:
        circle(c, P.p(x0, t), 4.5, "GREEN", 1.6)
        if lab:
            P.text(x0, t, lab, "GREEN", "start", 12, dx=8, dy=-6)
    P.text(45, 85, "L", size=15)
    P.text(46, 22, "α + β", size=13.5)
    boxes = ((88, "100 % liquid", "(L = 20 % B)"), (t1, "α₁ crystals in", "a matrix of L₁"),
             (35, "100 % α", "(α = 20 % B)"), (14, "small β₂ particles", "in a matrix of α₂"))
    for k, (t, l1, l2) in enumerate(boxes):
        y = P.p(x0, t)[1] + (14 if k == 3 else 0)
        bx = 150
        rect(c, bx, y - 26, 52, 52, "HEAD", 1.3)
        line(c, (bx + 54, y), (P.p(x0, t)[0] - 7, P.p(x0, t)[1]), "EDGE", 1, head=True)
        text(c, (bx - 8, y - 2), l1, "TEXT", "end", 11.5)
        text(c, (bx - 8, y + 13), l2, "TEXT", "end", 11.5)
        if k == 1:
            for u, v, r in ((bx + 14, y - 10, 8), (bx + 36, y - 8, 7), (bx + 22, y + 13, 8)):
                circle(c, (u, v), r, "HEAD", 1.2)
        if k in (2, 3):
            for a, b in (((bx, y - 4), (bx + 20, y - 8)), ((bx + 20, y - 8), (bx + 30, y - 26)), ((bx + 20, y - 8), (bx + 28, y + 10)),
                         ((bx + 28, y + 10), (bx, y + 16)), ((bx + 28, y + 10), (bx + 52, y + 6)), ((bx + 28, y + 10), (bx + 32, y + 26)),
                         ((bx + 20, y - 8), (bx + 52, y - 12))):
                line(c, a, b, "HEAD", 1.1)
        if k == 3:
            for u, v in ((bx + 20, y - 8), (bx + 28, y + 10)):
                dot(c, (u, v), 3.2, "HEAD")
    REG.put("precip-generic", c, "Solid-state precipitation on cooling an alloy of 20 % B",
            "An alloy of 20 % B: all liquid, then α₁ crystals in liquid L₁, then 100 % α of the alloy's composition. "
            "Below the solvus the solubility of B in α is exceeded and small β particles form, mainly at the grain "
            "boundaries, and grow as the temperature falls (α₂ + β₂, then α₃ + β₃). Redrawn from Session 8 Slide 3")


def scheme(c, x0, y0, kind):
    """Small schematic of an invariant reaction around a horizontal line at (x0 .. x0 + 240, y0)."""
    w = 240
    line(c, (x0 + 18, y0), (x0 + w - 18, y0), "ACC", 2.2)
    mid = x0 + w / 2
    lab = lambda p, s, a="middle": text(c, p, s, "HEAD", a, 13, "700")      # noqa: E731
    up_v = lambda: (smooth(c, [(mid - 22, y0 - 26), (mid - 8, y0 - 10), (mid, y0)], "ACC", 2),          # noqa: E731
                    smooth(c, [(mid + 22, y0 - 26), (mid + 8, y0 - 10), (mid, y0)], "ACC", 2))
    down_v = lambda: (smooth(c, [(mid - 18, y0 + 24), (mid - 6, y0 + 8), (mid, y0)], "ACC", 2),          # noqa: E731
                      smooth(c, [(mid + 18, y0 + 24), (mid + 6, y0 + 8), (mid, y0)], "ACC", 2))
    left_end = lambda: (smooth(c, [(x0 + 4, y0 - 24), (x0 + 12, y0 - 8), (x0 + 18, y0)], "ACC", 2),     # noqa: E731
                        smooth(c, [(x0 + 4, y0 + 24), (x0 + 12, y0 + 8), (x0 + 18, y0)], "ACC", 2))
    right_end = lambda: (smooth(c, [(x0 + w - 4, y0 - 24), (x0 + w - 12, y0 - 8), (x0 + w - 18, y0)], "ACC", 2),   # noqa: E731
                         smooth(c, [(x0 + w - 4, y0 + 24), (x0 + w - 12, y0 + 8), (x0 + w - 18, y0)], "ACC", 2))
    if kind in ("eutectic", "eutectoid"):
        left_end(); right_end(); up_v()
        lab((x0 - 2, y0 + 5), "α", "end"); lab((x0 + w + 2, y0 + 5), "β", "start")
        lab((mid, y0 - 30), "L" if kind == "eutectic" else "γ"); lab((mid, y0 + 20), "α + β")
    elif kind in ("peritectic", "peritectoid"):
        left_end(); down_v()
        if kind == "peritectic":
            smooth(c, [(x0 + w - 30, y0 - 22), (x0 + w - 22, y0 - 6), (x0 + w - 18, y0)], "ACC", 2)
            lab((x0 + w + 2, y0 + 5), "L", "start"); lab((mid, y0 - 10), "α + L"); lab((mid, y0 + 38), "β")
        else:
            right_end()
            lab((x0 + w + 2, y0 + 5), "β", "start"); lab((mid, y0 - 10), "α + β"); lab((mid, y0 + 38), "γ")
        lab((x0 - 2, y0 + 5), "α", "end")
    else:  # monotectic
        smooth(c, [(x0 + 18, y0), (x0 + 50, y0 - 32), (x0 + 95, y0 - 34), (mid, y0)], "ACC", 2)
        smooth(c, [(mid, y0), (mid + 40, y0 - 18), (mid + 80, y0 - 24)], "ACC", 2)
        right_end()
        lab((x0 + 10, y0 - 4), sub("L", "2"), "end"); lab((mid + 6, y0 - 14), sub("L", "1"), "start")
        lab((x0 + w + 2, y0 + 5), "α", "start"); lab((mid, y0 + 20), "α + " + sub("L", "2"))
        text(c, (x0 - 6, y0 - 26), "miscibility gap", "TEXT", "end", 11.5)


def invariant_table():
    c = Canvas(700, 480)
    rows = (("Eutectic", "L → α + β", "eutectic"), ("Peritectic", "α + L → β", "peritectic"),
            ("Monotectic", "L₁ → L₂ + α", "monotectic"), ("Eutectoid", "γ → α + β", "eutectoid"),
            ("Peritectoid", "α + β → γ", "peritectoid"))
    for k, (name, eq, kind) in enumerate(rows):
        y = 56 + k * 90
        line(c, (20, y - 46), (690, y - 46), "EDGE", 0.8)
        text(c, (30, y + 5), name, "HEAD", "start", 14, "700")
        text(c, (160, y + 5), eq, "HEAD", "start", 14, "700")
        scheme(c, 400, y, kind)
    line(c, (20, 56 + 4 * 90 + 46), (690, 56 + 4 * 90 + 46), "EDGE", 0.8)
    text(c, (30, 56 + 3 * 90 + 26), "solid-state reactions", "GREEN", "start", 11.5, "700")
    REG.put("invariant-table", c, "The five invariant reactions of binary diagrams",
            "Eutectic, peritectic and monotectic reactions involve a liquid; the eutectoid and the peritectoid happen "
            "entirely in the solid state. Redrawn from Session 8 Slide 6")


def cuzn():
    c = Canvas(640, 380)
    P = Plot(c, (80, 30, 560, 300), (60, 95), (430, 760))
    for g in (70, 80, 90):
        P.vseg(g, 430, 760, "EDGE", 0.6, "2,4")
    for g in (500, 600, 700):
        P.hseg(60, 95, g, "EDGE", 0.6, "2,4")
    segs = (
        [(67.6, 747), (69.1, 697), (70.0, 561), (67.9, 438)],
        [(69.1, 697), (80.0, 697)],
        [(72.6, 695), (73.7, 561)], [(72.6, 695), (76.1, 597)], [(76.1, 597), (73.7, 561)],
        [(76.1, 597), (87.6, 597)], [(70.0, 561), (78.2, 561)],
        [(78.2, 597), (78.2, 438)],
        [(75.9, 747), (80.0, 697), (87.6, 597), (94.5, 498), (95, 490)],
    )
    for s in segs:
        P.line(s, "ACC", 2.2)
    P.line([(78.2, 597), (81.5, 560), (84.5, 505), (86.7, 453), (87.4, 430)], "ACC", 2.2)
    P.frame([(60, "60"), (70, "70"), (80, "80"), (90, "90")], [(500, "500"), (600, "600"), (700, "700")],
            "Composition (wt% Zn)", "Temperature (°C)")
    P.hseg(62, 84, 560, "BLUE", 1.2, "5,4")
    P.vseg(73.7, 430, 680, "BLUE", 1.0, "4,4")
    P.dot(73.7, 561, 4.5, "GREEN"); P.dot(78.2, 597, 4.5, "GREEN")
    P.text(73.7, 561, "E", "GREEN", "middle", 13, dy=18)
    P.text(78.2, 597, "P", "GREEN", "middle", 13, dy=-8)
    P.text(64, 560, "560 °C", "BLUE", "start", 12, dy=-6)
    P.text(84, 597, "598 °C", "HEAD", "middle", 12, "400", dy=-6)
    for x, t, s in ((74, 735, "γ + L"), (71.2, 640, "γ + δ"), (74.6, 625, "δ"), (82, 650, "δ + L"), (92, 680, "L"),
                    (77.3, 578, "δ + ε"), (81.5, 500, "ε"), (90, 500, "ε + L"), (74, 490, "γ + ε"), (64, 640, "γ")):
        P.text(x, t, s, size=12.5)
    REG.put("cuzn-eutectoid", c, "The eutectoid point of the Cu-Zn system",
            "Part of the Cu-Zn diagram: at E (560 °C, 74 % Zn) the solid δ transforms on cooling into γ (70 % Zn) and "
            "ε (78 % Zn), an invariant reaction in the solid state; P (598 °C) is a peritectic point. Redrawn from "
            "Session 8 Slide 7 (compositions read on the figure)")


def peritectic_generic():
    c = Canvas(520, 330)
    P = Plot(c, (60, 30, 440, 290), (0, 100), (0, 100))
    liq = [(0, 95), (30, 87), (60, 75), (82, 60), (100, 45)]
    P.area([(0, 100)] + liq + [(100, 100)], "BLUE", 0.08)
    smooth(c, [P.p(*q) for q in liq], "ACC", 2.4)
    P.line([(0, 95), (30, 60)], "ACC", 2.4)
    P.line([(30, 60), (82, 60)], "ACC", 2.4)
    smooth(c, [P.p(30, 60), P.p(28, 30), P.p(26, 0)], "ACC", 2.2)
    smooth(c, [P.p(55, 60), P.p(57, 30), P.p(59, 0)], "ACC", 2.2)
    smooth(c, [P.p(55, 60), P.p(80, 52), P.p(100, 45)], "ACC", 2.2)
    P.frame([(0, "A"), (100, "B")], (), "composition", "Temperature")
    for x, t, s in ((30, 60, "a"), (55, 60, "P"), (82, 60, "b")):
        P.dot(x, t, 4, "GREEN")
        P.text(x, t, s, "GREEN", "middle", 13, dy=-8)
    P.text(0, 95, sub("T", "A"), "HEAD", "end", 12.5, dx=-6, dy=4)
    P.text(100, 60, sub("T", "P"), "HEAD", "start", 12.5, dx=6, dy=4)
    P.text(100, 45, sub("T", "B"), "HEAD", "start", 12.5, dx=6, dy=4)
    for x, t, s in ((60, 90, "L"), (35, 75, "L + α"), (10, 40, "α"), (42, 30, "α + β"), (80, 30, "β"), (80, 55, "L + β")):
        P.text(x, t, s, size=12.5)
    REG.put("peritectic-generic", c, "A peritectic point",
            "Peritectic point P: on cooling at T_P, the solid α of composition a and the liquid of composition b react "
            "to give a different solid, β (α + L → β). Redrawn from Session 8 Slide 8")


def feni():
    c = Canvas(600, 360)
    P = Plot(c, (80, 30, 520, 300), (0, 9), (1380, 1560))
    P.line([(0, 1538), (5.4, 1517), (9, 1503)], "PINK", 2.2)
    P.line([(0, 1538), (4.0, 1517)], "ACC", 2.2)
    P.line([(0, 1394), (4.0, 1517)], "ACC", 2.2)
    P.line([(0, 1394), (4.3, 1517)], "PINK", 2.2)
    P.line([(4.3, 1517), (9, 1487)], "ACC", 2.2)
    P.line([(4.0, 1517), (5.4, 1517)], "HEAD", 2)
    P.frame([(x, str(x)) for x in range(10)], [(1400, "1400"), (1450, "1450"), (1500, "1500"), (1550, "1550")],
            "Composition (wt% Ni)", "Temperature (°C)")
    P.vseg(4.3, 1380, 1555, "GREEN", 1.4, "6,4")
    P.dot(4.3, 1517, 4.5, "GREEN")
    P.hseg(0, 4.0, 1517, "EDGE", 1, "4,4")
    for x, t, s in ((0, 1538, "1538"), (0, 1394, "1394"), (0, 1517, "1517")):
        P.text(x, t, s, "TEXT", "start", 11.5, "400", dx=6, dy=-5 if s != "1394" else 14)
    for x, s in ((4.0, "4.0"), (5.4, "5.4")):
        P.text(x, 1517, s, "HEAD", "middle", 12, dy=-8)
    P.text(4.3, 1380, "4.3", "GREEN", "middle", 12, dy=52)
    for x, t, s in ((7.5, 1545, "Liquid"), (2.2, 1532, "L + δ"), (1.2, 1480, "δ"), (2.6, 1440, "γ + δ"), (6.5, 1440, "γ"),
                    (8.3, 1499, "L + γ")):
        P.text(x, t, s, size=12.5)
    REG.put("feni-peritectic", c, "The peritectic point of the Fe-Ni system",
            "Fe-Ni at 1517 °C: δ of 4.0 % Ni and liquid of 5.4 % Ni react to give γ of 4.3 % Ni. Redrawn from Session 8 "
            "Slide 8")


def ptag():
    c = Canvas(640, 400)
    P = Plot(c, (80, 30, 540, 320), (0, 100), (600, 1900))
    liq = [(0, 1780), (25, 1640), (55, 1400), (66.3, 1186), (77, 1150), (88, 1060), (100, 961)]
    sol_b = [(42.4, 1186), (48, 1150), (65, 1080), (85, 1010), (100, 961)]
    solv_a = [(10.5, 1186), (8, 1000), (5, 800), (3, 600)]
    beta_l = [(42.4, 1186), (55, 1000), (72, 800), (88, 600)]
    P.area([(0, 1900)] + liq + [(100, 1900)], "BLUE", 0.08)
    smooth(c, [P.p(*q) for q in liq], "PINK", 2.4)
    P.line([(0, 1780), (7, 1400), (10.5, 1186)], "PINK", 2.2)
    smooth(c, [P.p(*q) for q in solv_a], "PINK", 2.2)
    smooth(c, [P.p(*q) for q in sol_b], "PINK", 2.2)
    smooth(c, [P.p(*q) for q in beta_l], "PINK", 2.2)
    P.line([(10.5, 1186), (66.3, 1186)], "PINK", 2.2)
    P.frame([(x, str(x)) for x in range(0, 101, 10)], [(t, str(t)) for t in (600, 800, 1000, 1200, 1400, 1600, 1800)],
            "Composition (wt% Ag)", "Temperature (°C)")
    for x, lab in ((42.4, "alloy 1 (42.4)"), (60, "alloy 2 (60)")):
        P.vseg(x, 600, 1880, "GREEN", 1.3, "6,4")
        P.text(x, 1880, lab, "GREEN", "middle", 11.5, dy=-4)
    for t, a, b, la, lb in ((1400, 7, 55, "7", "55"), (1150, 48, 77, "48", "77")):
        P.line([(a, t), (b, t)], "BLUE", 1.8)
        P.text(a, t, la, "BLUE", "middle" if la == "48" else "end", 11.5, dx=0 if la == "48" else -4, dy=16 if la == "48" else -4)
        P.text(b, t, lb, "BLUE", "start", 11.5, dx=4, dy=-4)
    P.dot(42.4, 1400, 4, "GREEN"); P.dot(42.4, 1186, 4.5, "GREEN"); P.dot(60, 1150, 4, "GREEN")
    P.text(10.5, 1186, "10.5", "HEAD", "end", 11.5, dx=-4, dy=14)
    P.text(66.3, 1186, "66.3", "HEAD", "start", 11.5, dx=6, dy=-4)
    P.text(30, 1186, "1186 °C", "HEAD", "middle", 11.5, "400", dy=-6)
    for x, t, s in ((70, 1600, "Liquid"), (20, 1450, "L + α"), (4, 1000, "α"), (30, 900, "α + β"), (86, 780, "β"),
                    (82, 1080, "L + β")):
        P.text(x, t, s, size=12.5)
    REG.put("ptag-peritectic", c, "The peritectic reaction in the Pt-Ag system",
            "Pt-Ag: at 1186 °C α (10.5 % Ag) and liquid (66.3 % Ag) give β (42.4 % Ag). Alloy 1 has the peritectic "
            "composition; alloy 2 (about 60 % Ag, a reading of the figure) ends in L + β at 1150 °C. Redrawn from Session 8 "
            "Slide 9")


def peritectoid_generic():
    c = Canvas(520, 300)
    P = Plot(c, (60, 30, 440, 270), (0, 100), (0, 100))
    P.line([(0, 100), (70, 60)], "ACC", 2.2)
    P.line([(0, 100), (12, 60)], "ACC", 2.2)
    P.line([(12, 60), (70, 60)], "ACC", 2.2)
    P.line([(12, 60), (2, 0)], "ACC", 2.2)
    P.line([(45, 60), (32, 0)], "ACC", 2.2)
    P.line([(45, 60), (58, 0)], "ACC", 2.2)
    P.line([(70, 60), (82, 0)], "ACC", 2.2)
    P.line([(70, 60), (100, 25)], "ACC", 2.2)
    P.frame((), (), "", "")
    circle(c, P.p(45, 60), 9, "PINK", 1.6)
    for x, t, s in ((70, 85, "solid β"), (30, 70, "β + α"), (5, 70, "α"), (20, 25, "α + γ"), (45, 18, "γ"), (75, 25, "γ + β")):
        P.text(x, t, s, size=12.5)
    REG.put("peritectoid-generic", c, "A peritectoid point",
            "Peritectoid point (circled): on cooling, two solid phases, α and β, react to give a new solid phase γ. "
            "Redrawn from Session 8 Slide 11")


def monotectic_cupb():
    c = Canvas(640, 380)
    P = Plot(c, (80, 30, 540, 310), (0, 100), (200, 1200))
    smooth(c, [P.p(0, 1084.5), P.p(15, 1010), P.p(36, 955)], "PINK", 2.4)
    smooth(c, [P.p(36, 955), P.p(50, 985), P.p(63, 991), P.p(76, 982), P.p(87, 955)], "PINK", 2.4)
    smooth(c, [P.p(87, 955), P.p(96, 820), P.p(99, 600), P.p(99.94, 327)], "PINK", 2.4)
    P.line([(0, 955), (87, 955)], "HEAD", 1.6)
    P.line([(0, 326), (99.94, 326)], "HEAD", 1.6)
    P.frame([(x, str(x)) for x in (0, 20, 40, 60, 80, 100)], [(t, str(t)) for t in (200, 400, 600, 800, 1000)],
            "Composition (wt% Pb)", "Temperature (°C)")
    P.dot(36, 955, 5, "GREEN")
    for x, t, s, a in ((0, 1084.5, "1084.5 °C", "start"), (63, 991, "991 °C", "middle"), (50, 955, "955 °C", "middle"),
                       (36, 955, "36", "middle"), (87, 955, "87", "start"), (50, 326, "326 °C", "middle")):
        P.text(x, t, s, "TEXT", a, 11.5, "400", dx=6 if a == "start" else 0, dy=-8 if s not in ("36", "955 °C") else 16)
    for x, t, s in ((40, 1100, "L"), (8, 985, "α + L₁"), (63, 965, "L₁ + L₂"), (40, 650, "α + L₂"), (40, 260, "α + β")):
        P.text(x, t, s, size=12.5)
    REG.put("monotectic-cupb", c, "The monotectic reaction in the Cu-Pb system",
            "Cu-Pb at 955 °C: the liquid L₁ of 36 % Pb gives a second liquid L₂ of 87 % Pb and solid α (practically "
            "pure Cu). The dome above is the miscibility gap of the liquid. Redrawn from Session 8 Slide 12")


def mgni():
    c = Canvas(660, 380)
    P = Plot(c, (80, 30, 560, 310), (0, 100), (300, 1500))
    smooth(c, [P.p(0, 650), P.p(12, 585), P.p(23.6, 505)], "PINK", 2.4)
    smooth(c, [P.p(23.6, 505), P.p(35, 640), P.p(51, 760)], "PINK", 2.4)
    smooth(c, [P.p(51, 760), P.p(65, 1020), P.p(82.5, 1146)], "PINK", 2.4)
    smooth(c, [P.p(82.5, 1146), P.p(86.5, 1125), P.p(90, 1086)], "PINK", 2.4)
    smooth(c, [P.p(90, 1086), P.p(95, 1300), P.p(100, 1450)], "PINK", 2.4)
    P.line([(0.6, 505), (54.75, 505)], "HEAD", 1.6)
    P.line([(51, 760), (82.5, 760)], "HEAD", 1.6)
    P.line([(54.75, 300), (54.75, 760)], "HEAD", 2)
    P.line([(82.5, 300), (82.5, 1146)], "HEAD", 2)
    P.line([(82.5, 1086), (98, 1086)], "HEAD", 1.6)
    P.frame([(x, str(x)) for x in range(0, 101, 10)], [(t, str(t)) for t in (300, 700, 1100, 1500)],
            "Composition (wt% Ni)", "Temperature (°C)")
    for x, t, s in ((20, 1300, "Liquid"), (8, 560, "L + α"), (25, 420, "α + Mg₂Ni"), (42, 620, "L + Mg₂Ni"),
                    (68, 600, "Mg₂Ni + MgNi₂"), (68, 860, "L + MgNi₂"), (91, 700, "MgNi₂ + β"), (96, 1150, "β")):
        P.text(x, t, s, size=12)
    P.text(54.75, 760, "Mg₂Ni: incongruent melting", "GREEN", "end", 12, dx=-6, dy=-40)
    line(c, P.p(50, 820), P.p(54.5, 765), "GREEN", 1, head=True)
    P.text(82.5, 1146, "MgNi₂: congruent melting", "GREEN", "end", 12, dx=-10, dy=-16)
    REG.put("mgni-melting", c, "Congruent and incongruent melting in the Mg-Ni system",
            "Mg-Ni: MgNi₂ melts congruently (the liquid keeps its composition, a maximum of the liquidus), while Mg₂Ni "
            "melts incongruently: on heating it gives liquid plus MgNi₂ at the horizontal line, the reverse of a "
            "peritectic reaction. Redrawn from Session 8 Slide 17")


def part2_rasters():
    REG.raster("s8-precipitation-micrograph", "Micrograph of precipitates at grain boundaries",
               "Micrograph of solid-state precipitates at the grain boundaries (scale bar 20 µm). From Session 8 Slide 3", 360)
    REG.raster("s8-precipitation-micrographs", "Micrographs of precipitates inside the grains",
               "Precipitates inside the grains; on the right, a detail of the circled area. From Session 8 Slide 4", 560)
    REG.raster("s8-cuzn-micrograph", "Micrograph of the Cu-Zn eutectoid structure",
               "Micrograph of the eutectoid product of the Cu-Zn alloy, a fine mixture of γ and ε. From Session 8 Slide 7", 320)
    REG.raster("s8-ptag-sequence", "Microstructure during the peritectic reaction",
               "Peritectic reaction with decreasing temperature: α crystals in liquid; β forms around them; all β. From "
               "Session 8 Slide 9", 500)
    REG.raster("s8-peritectic-rapid", "Rapid solidification in a peritectic system",
               "Rapid (non-equilibrium) solidification of alloy X: the solid follows non-equilibrium compositions (α′, "
               "β′) and the peritectic reaction is incomplete. From Session 8 Slide 10", 520)
    REG.raster("s8-peritectic-encasement", "β surrounding primary α during the peritectic reaction",
               "Encasement: the β formed by the peritectic reaction surrounds the primary α, so B atoms from the liquid "
               "and A atoms from α must diffuse through it. From Session 8 Slide 10", 380)
    REG.raster("s8-cow-peritectoid", "The Co-W phase diagram with a peritectoid point",
               "Co-W diagram: the arrow marks a peritectoid point, where two solid phases give the new solid γ. From "
               "Session 8 Slide 11", 600)
    REG.raster("s8-intermetallic-phases", "Terminal and intermediate phases",
               "A diagram with terminal phases (α, ζ) at the ends and intermediate phases (β, γ, δ, ε) inside, around "
               "the compounds A₂B, AB, AB₂ and AB₄. From Session 8 Slide 14", 560)
    REG.raster("s8-tib", "The Ti-B diagram of the slides",
               "Ti-B: Ti₃B₄ is a stoichiometric compound (a vertical line); TiB and TiB₂ have a range of compositions. "
               "From Session 8 Slide 15", 440)


def theory_part2():
    precip_pbsn()
    precip_generic()
    invariant_table()
    cuzn()
    peritectic_generic()
    feni()
    ptag()
    peritectoid_generic()
    monotectic_cupb()
    mgni()
    part2_rasters()


# --------------------------------------------------------------------------- problem sheet I (problems 1-8)
def lagrange(pts):
    """Quadratic through three (x, y) points, returned as a function of x."""
    (x0, y0), (x1, y1), (x2, y2) = pts
    return lambda x: (y0 * (x - x1) * (x - x2) / ((x0 - x1) * (x0 - x2)) + y1 * (x - x0) * (x - x2) / ((x1 - x0) * (x1 - x2))
                      + y2 * (x - x0) * (x - x1) / ((x2 - x0) * (x2 - x1)))


def agcu_curves():
    """Ag-Cu as printed in the problem sheet (p. 2): eutectic 779.1 °C at 28.1 wt% Cu, (Ag) 8.8, (Cu) 92 wt% Cu,
    melting points 961.93 and 1084.87 °C. The curves pass through the readings of the official solutions
    (liquid of 58 wt% Cu and (Cu) of 93 wt% Cu at 900 °C; Ag-10 wt% Cu still liquid at 900 °C)."""
    te = 779.1
    liq_a = lagrange([(0, 961.93), (10, 893), (28.1, te)])
    liq_b = lagrange([(28.1, te), (58, 900), (100, 1084.87)])
    sol_b = lagrange([(te, 92), (900, 93), (1084.87, 100)])
    return dict(
        liq_a=[(x, liq_a(x)) for x in lin(0, 28.1)],
        liq_b=[(x, liq_b(x)) for x in lin(28.1, 100)],
        sol_a=[(8.8 * ((961.93 - t) / (961.93 - te)) ** 0.8, t) for t in lin(961.93, te)],
        sol_b=[(sol_b(t), t) for t in lin(te, 1084.87)],
        solv_a=[(0.4 + 8.4 * ((t - 200) / (te - 200)) ** 1.6, t) for t in lin(te, 200)],
        solv_b=[(99.6 - 7.6 * ((t - 200) / (te - 200)) ** 1.6, t) for t in lin(te, 200)])


def agcu_diagram(P):
    k = agcu_curves()
    P.area([(0, 1200)] + k["liq_a"] + k["liq_b"] + [(100, 1200)], "BLUE", 0.08)
    P.area(k["sol_a"] + k["solv_a"] + [(0, 200)], "BLUE", 0.16)
    P.area([(100, 1084.87)] + list(reversed(k["sol_b"])) + k["solv_b"] + [(100, 200)], "BLUE", 0.16)
    for name in ("liq_a", "liq_b", "sol_a", "sol_b", "solv_a", "solv_b"):
        P.line(k[name], "ACC", 2.2)
    P.line([(8.8, 779.1), (92, 779.1)], "ACC", 2.2)
    P.text(55, 1080, "L")
    P.text(4, 860, "(Ag)", "HEAD", "start", 12)
    P.text(100, 860, "(Cu)", "HEAD", "start", 12, dx=8)
    P.text(48, 500, "(Ag) + (Cu)", size=12.5)
    P.text(0, 961.93, "961.93 °C", "TEXT", "start", 11, "400", dx=6, dy=-6)
    P.text(100, 1084.87, "1084.87 °C", "TEXT", "end", 11, "400", dx=-6, dy=-8)
    P.text(60, 779.1, "779.1 °C", "TEXT", "middle", 11, "400", dy=16)


def problem_diagram(name, kind, alloy, marks, ties, title, caption):
    """Sheet diagram (kind 'pbsn' or 'agcu') with the alloy line, the temperatures of the problem and the tie lines.
    marks: (T, label); ties: (T, c_left, c_right, label_left, label_right)."""
    c = Canvas(640, 400)
    if kind == "pbsn":
        P = Plot(c, (80, 30, 560, 310), (0, 100), (0, 350))
        pbsn_diagram(c, P, PBSN_SHEET)
        P.frame([(0, "0 (Pb)"), (20, "20"), (40, "40"), (60, "60"), (80, "80"), (100, "100 (Sn)")],
                [(0, "0"), (100, "100"), (200, "200"), (300, "300")], "Composition (wt% Sn)", "Temperature (°C)")
    else:
        P = Plot(c, (80, 30, 560, 310), (0, 100), (200, 1200))
        agcu_diagram(P)
        P.frame([(0, "0 (Ag)"), (20, "20"), (40, "40"), (60, "60"), (80, "80"), (100, "100 (Cu)")],
                [(200, "200"), (400, "400"), (600, "600"), (800, "800"), (1000, "1000"), (1200, "1200")],
                "Composition (wt% Cu)", "Temperature (°C)")
    P.vseg(alloy, P.ya, P.yb, "GREEN", 1.6, "6,4")
    P.text(alloy, P.yb, sub("C", "0") + f" = {alloy:g}", "GREEN", "start", 12, dx=6, dy=16)
    for t, cl, cr, ll, lr in ties:
        P.line([(cl, t), (cr, t)], "BLUE", 2.2)
        P.dot(cl, t, 3.4, "BLUE"); P.dot(cr, t, 3.4, "BLUE")
        if ll:
            P.text(cl, t, ll, "BLUE", "end", 11.5, dx=-5, dy=4)
        if lr:
            P.text(cr, t, lr, "BLUE", "start", 11.5, dx=5, dy=4)
    for t, lab, *pos in marks:
        anchor, dx, dy = pos if pos else ("start", 7, -6)
        P.dot(alloy, t, 4.2, "GREEN")
        P.text(alloy, t, lab, "GREEN", anchor, 12.5, dx=dx, dy=dy)
    REG.put(name, c, title, caption)


def micro(c, cx, cy, r, blobs, uid, primary_lab, matrix_lab, matrix="eutectic"):
    """Schematic microstructure: primary grains (blobs: list of (dx, dy, radius)) in a lamellar eutectic."""
    holes = "".join(f'<circle cx="{fmt(cx + dx)}" cy="{fmt(cy + dy)}" r="{fmt(rr)}" fill="black"/>' for dx, dy, rr in blobs)
    c.add(f'<clipPath id="clip-{uid}"><circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(r)}"/></clipPath>')
    c.add(f'<mask id="mask-{uid}"><rect x="{fmt(cx - r)}" y="{fmt(cy - r)}" width="{fmt(2 * r)}" height="{fmt(2 * r)}" '
          f'fill="white"/>{holes}</mask>')
    c.add(f'<g clip-path="url(#clip-{uid})">')
    if matrix == "eutectic":
        c.add(f'<g mask="url(#mask-{uid})">')
        for k in range(-2 * int(r), 2 * int(r) + 1, 6):
            line(c, (cx + k - r, cy + r), (cx + k + r, cy - r), "HEAD", 1.1)
        c.add("</g>")
    for dx, dy, rr in blobs:
        circle(c, (cx + dx, cy + dy), rr, "HEAD", 1.4, "BLUE", 0.15)
    c.add("</g>")
    circle(c, (cx, cy), r, "HEAD", 1.6)
    if primary_lab:
        line(c, (cx + blobs[0][0] + blobs[0][2] * 0.6, cy + blobs[0][1] - blobs[0][2] * 0.6), (cx + r + 16, cy - r + 10), "EDGE", 1)
        text(c, (cx + r + 20, cy - r + 14), primary_lab, "HEAD", "start", 12, "700")
    if matrix_lab:
        line(c, (cx + r * 0.55, cy + r * 0.55), (cx + r + 16, cy + r - 10), "EDGE", 1)
        text(c, (cx + r + 20, cy + r - 6), matrix_lab, "HEAD", "start", 12, "700")


def micro_figure(name, title, caption, blobs, primary_lab, matrix_lab, matrix="eutectic"):
    c = Canvas(420, 220)
    micro(c, 110, 110, 92, blobs, name, primary_lab, matrix_lab, matrix)
    REG.put(name, c, title, caption)


BLOBS_MANY = [(-40, -30, 22), (25, -45, 20), (-10, 20, 24), (45, 15, 21), (-50, 40, 18), (20, 60, 17), (55, -10, 12)]
BLOBS_FEW = [(-30, -20, 20), (35, 25, 18), (10, -55, 14)]


def pd_p1():
    c = Canvas(600, 300)
    P = Plot(c, (80, 30, 540, 230), (0, 100), (0, 10))
    P.frame([(0, "A"), (11.7, "11.7"), (30, "30"), (65, "65"), (95, "95"), (100, "B")], (), "Composition (% B)", "Temperature")
    P.line([(11.7, 5), (9, 2), (7, 0)], "ACC", 2.2); P.line([(11.7, 5), (14, 8.5), (15, 10)], "ACC", 2.2)
    P.line([(95, 5), (97, 2), (98, 0)], "ACC", 2.2); P.line([(95, 5), (93, 8.5), (92, 10)], "ACC", 2.2)
    P.line([(11.7, 5), (95, 5)], "BLUE", 2.4)
    P.dot(11.7, 5, 4, "BLUE"); P.dot(95, 5, 4, "BLUE")
    for x, lab in ((30, "alloy 1: Wα = 0.78"), (65, "alloy 2: Wα = 0.36")):
        P.vseg(x, 0, 9.5, "GREEN", 1.4, "6,4")
        P.dot(x, 5, 4.5, "GREEN")
        P.text(x, 9.5, lab, "GREEN", size=12, dy=-4)
    P.text(5, 7.5, "α", size=14); P.text(98, 7.5, "β", size=14, dx=-6); P.text(50, 2.5, "α + β", size=14)
    P.text(11.7, 5, sub("C", "α"), "BLUE", "end", 13, dx=-6, dy=-6); P.text(95, 5, sub("C", "β"), "BLUE", "start", 13, dx=6, dy=-6)
    REG.put("pd-p1", c, "Problem 1: two alloys on the same tie line",
            "Both alloys are in the α + β region at the same temperature, so they share the tie line from C_α to C_β; "
            "the two lever-rule equations give C_α = 11.7 % B and C_β = 95 % B")


def pd_p8():
    c = Canvas(640, 400)
    P = Plot(c, (80, 30, 560, 310), (0, 100), (0, 1000))
    P.area([(0, 1000), (0, 700), (65, 400), (100, 600), (100, 1000)], "BLUE", 0.08)
    P.area([(0, 700), (25, 400), (5, 0), (0, 0)], "BLUE", 0.16)
    P.area([(100, 600), (80, 400), (90, 0), (100, 0)], "BLUE", 0.16)
    for seg in (((0, 700), (65, 400)), ((100, 600), (65, 400)), ((0, 700), (25, 400)), ((100, 600), (80, 400)),
                ((25, 400), (5, 0)), ((80, 400), (90, 0)), ((25, 400), (80, 400))):
        P.line(list(seg), "ACC", 2.2)
    P.frame([(x, str(x)) for x in range(0, 101, 10)], [(t, str(t)) for t in range(0, 1001, 100)], "Composition (% B)",
            "Temperature (°C)")
    for x, t in ((0, 700), (100, 600), (25, 400), (65, 400), (80, 400), (5, 0), (90, 0)):
        P.dot(x, t, 4, "HEAD")
    P.text(40, 820, "L", size=15)
    P.text(4, 300, "α", size=14); P.text(94, 300, "β", size=14)
    P.text(14, 520, "α + L", size=12.5, dx=-6); P.text(86, 470, "β + L", size=12.5)
    P.text(52, 200, "α + β", size=14)
    P.vseg(40, 0, 1000, "GREEN", 1.6, "6,4")
    P.text(40, 1000, sub("C", "0") + " = 40", "GREEN", dy=-6, size=12)
    for t, cl, cr, ll, lr in ((450, 20.83, 54.17, "20.8", "54.2"), (412, 25, 65, "25", "65"), (388, 25, 80, "", "80")):
        P.line([(cl, t), (cr, t)], "BLUE", 2.2)
        P.dot(cl, t, 3.4, "BLUE"); P.dot(cr, t, 3.4, "BLUE")
        if ll:
            P.text(cl, t, ll, "BLUE", "end", 11.5, dx=-5, dy=4 if t == 450 else -4)
        P.text(cr, t, lr, "BLUE", "start", 11.5, dx=5, dy=4 if t != 412 else -4)
    for t in (450, 412, 388):
        P.dot(40, t, 4, "GREEN")
    P.text(40, 450, "450 °C", "GREEN", "start", 11.5, dx=7, dy=-8)
    REG.put("pd-p8", c, "Problem 8: the A-B diagram drawn from the data",
            "A-B diagram with straight lines: melting points 700 °C (A) and 600 °C (B), eutectic at 400 °C and 65 % B, "
            "maximum solubilities 25 % B in α and 20 % A in β (80 % B) at 400 °C, and 5 % B in α and 10 % A in β (90 % B) "
            "at 0 °C. Dashed: the 40 % B alloy, with its tie lines at 450 °C and just above and below 400 °C")


def problems():
    pd_p1()
    problem_diagram("pd-p2", "pbsn", 90, [(187, "183 + ΔT", "end", -7, -8), (178, "183 − ΔT", "end", -7, 18)],
                    [(187, 61.9, 97.5, "61.9", "97.5"), (178, 19.2, 97.5, "19.2", "")],
                    "Problem 2: Pb-90 wt% Sn around the eutectic temperature",
                    "Pb-Sn diagram of the problem sheet (eutectic 61.9 wt% Sn at 183 °C, α 19.2 and β 97.5 wt% Sn). The alloy "
                    "with 79 % primary β is the hypereutectic Pb-90 wt% Sn; the tie lines just above and below 183 °C give the "
                    "primary β and the total β")
    problem_diagram("pd-p3", "pbsn", 80, [(250, "T₁"), (188, "T₂", "end", -7, -8), (177, "T₃", "end", -7, 18), (100, "T₄")],
                    [(188, 61.9, 97.5, "61.9", "97.5"), (177, 19.2, 97.5, "19.2", ""), (100, 5, 100, "5", "")],
                    "Problem 3: Pb-80 wt% Sn",
                    "Pb-80 wt% Sn at T₁ = 250 °C (liquid), T₂ = 183 + ΔT (β + L), T₃ = 183 − ΔT (α + β) and T₄ = 100 °C "
                    "(α + β, with α of 5 and β of 100 wt% Sn, a reading of the figure). Problem sheet diagram")
    problem_diagram("pd-p4", "pbsn", 30, [(250, "T₁"), (188, "T₂", "end", -7, -8), (177, "T₃", "end", -7, 18), (100, "T₄")],
                    [(250, 12, 36, "12", "36"), (188, 19.2, 61.9, "19.2", "61.9"), (177, 19.2, 97.5, "", "97.5"),
                     (100, 5, 100, "5", "100")],
                    "Problem 4: Pb-30 wt% Sn",
                    "Pb-30 wt% Sn at T₁ = 250 °C (α of 12 and L of 36 wt% Sn, a reading of the figure), T₂ = 183 + ΔT (α + L), "
                    "T₃ = 183 − ΔT (α + β) and T₄ = 100 °C. Problem sheet diagram")
    problem_diagram("pd-p5", "agcu", 28.1, [(900, "T₁"), (795, "T₂", "end", -7, -8), (763, "T₃", "end", -7, 18)],
                    [(763, 8.8, 92, "8.8", "92")],
                    "Problem 5: Ag-28.1 wt% Cu, the eutectic alloy",
                    "Ag-Cu diagram of the problem sheet. The eutectic alloy is liquid down to 779.1 °C and then becomes "
                    "(Ag) of 8.8 and (Cu) of 92 wt% Cu")
    problem_diagram("pd-p6", "agcu", 80, [(900, "T₁"), (795, "T₂", "end", -7, -8), (763, "T₃", "end", -7, 18)],
                    [(900, 58, 93, "58", "93"), (795, 28.1, 92, "28.1", "92"), (763, 8.8, 92, "8.8", "")],
                    "Problem 6: Ag-80 wt% Cu",
                    "Ag-80 wt% Cu at T₁ = 900 °C (L of 58 and (Cu) of 93 wt% Cu, a reading of the figure), T₂ = 780 + ΔT and "
                    "T₃ = 780 − ΔT. Problem sheet diagram")
    problem_diagram("pd-p7", "agcu", 10, [(900, "T₁"), (795, "T₂", "end", -7, -8), (763, "T₃", "end", -7, 18)],
                    [(795, 8.8, 28.1, "8.8", "28.1"), (763, 8.8, 92, "", "92")],
                    "Problem 7: Ag-10 wt% Cu",
                    "Ag-10 wt% Cu at T₁ = 900 °C (liquid, just above the liquidus, a reading of the figure), T₂ = 780 + ΔT "
                    "and T₃ = 780 − ΔT. Problem sheet diagram")
    pd_p8()
    micro_figure("pd-micro-p3", "Problem 3: microstructure of Pb-80 wt% Sn below 183 °C",
                 "Pb-80 wt% Sn below the eutectic temperature: primary β (51 %) in the eutectic α + β (49 %)",
                 BLOBS_MANY[:5], "primary β", "eutectic (α + β)")
    micro_figure("pd-micro-p4", "Problem 4: microstructure of Pb-30 wt% Sn below 183 °C",
                 "Pb-30 wt% Sn below the eutectic temperature: primary α (75 %) in the eutectic α + β (25 %)",
                 BLOBS_MANY, "primary α", "eutectic (α + β)")
    micro_figure("pd-micro-p5", "Problem 5: microstructure of the eutectic alloy",
                 "Ag-28.1 wt% Cu below 779 °C: 100 % eutectic, (Ag) and (Cu) in alternating layers",
                 [], "", "eutectic ((Ag) + (Cu))")
    micro_figure("pd-micro-p6", "Problem 6: microstructure of Ag-80 wt% Cu",
                 "Ag-80 wt% Cu below 779 °C: primary (Cu) (81 %) in the eutectic (19 %)",
                 BLOBS_MANY, "primary (Cu)", "eutectic")
    micro_figure("pd-micro-p7", "Problem 7: microstructure of Ag-10 wt% Cu",
                 "Ag-10 wt% Cu below 779 °C: primary (Ag) (94 %) with a little eutectic (6 %) between the grains",
                 [(-42, -38, 34), (30, -42, 32), (-38, 36, 33), (36, 32, 33), (0, 0, 22), (-75, 0, 18), (75, -2, 18),
                  (0, -78, 16), (2, 76, 18)], "primary (Ag)", "eutectic")
    micro_figure("pd-micro-p8", "Problem 8: microstructure of the 40 % B alloy below 400 °C",
                 "40 % B alloy at 400 − ΔT: proeutectic α (62.5 %) in the eutectic α + β (37.5 %)",
                 BLOBS_MANY[:6], "proeutectic α", "eutectic (α + β)")


def pd_p11():
    c = Canvas(660, 420)
    P = Plot(c, (80, 30, 560, 330), (0, 100), (0, 1100))
    ab2 = 200 / 3
    P.area([(0, 1100), (0, 850), (30, 700), (ab2, 1000), (95, 500), (100, 350), (100, 1100)], "BLUE", 0.08)
    P.area([(0, 850), (10, 700), (2, 25), (0, 25)], "BLUE", 0.16)
    P.area([(80, 500), (100, 350), (100, 25), (75, 25)], "BLUE", 0.16)
    for seg in (((0, 850), (30, 700)), ((0, 850), (10, 700)), ((10, 700), (2, 25)), ((10, 700), (ab2, 700)),
                ((30, 700), (ab2, 1000)), ((ab2, 1000), (95, 500)), ((ab2, 500), (95, 500)), ((95, 500), (100, 350)),
                ((80, 500), (100, 350)), ((80, 500), (75, 25))):
        P.line(list(seg), "ACC", 2.2)
    P.line([(ab2, 25), (ab2, 1000)], "HEAD", 2.4)
    P.frame([(0, "0 (A)"), (10, "10"), (30, "30"), (66.7, "66.7"), (80, "80"), (95, "95"), (100, "B")],
            [(t, str(t)) for t in (0, 200, 400, 600, 800, 1000)], "Composition (at.% B)", "Temperature (°C)")
    for x, t in ((0, 850), (100, 350), (ab2, 1000), (30, 700), (10, 700), (2, 25), (80, 500), (95, 500), (75, 25)):
        P.dot(x, t, 3.8, "GREEN")
    for x, t, s, a, dx, dy in ((0, 850, "850 °C", "start", 6, -6), (100, 350, "350 °C", "end", -6, 16), (ab2, 1000, "AB₂ 1000 °C", "middle", 0, -8),
                               (30, 700, "E (700 °C)", "middle", 0, 18), (80, 500, "P (500 °C)", "end", -6, 16), (2, 25, "2", "start", 6, -4),
                               (75, 25, "75", "end", -6, -4)):
        P.text(x, t, s, "GREEN", a, 11.5, dx=dx, dy=dy)
    for x, t, s in ((45, 1000, "L"), (12, 760, "α + L"), (3, 400, "α"), (38, 350, "α + AB₂"), (52, 790, "L + AB₂"),
                    (78, 680, "L + AB₂"), (73, 250, "AB₂ + β"), (93, 440, "L + β"), (91, 200, "β")):
        P.text(x, t, s, size=12)
    REG.put("pd-p11", c, "Problem 11: the A-B diagram drawn from the data",
            "A-B with straight lines: A melts at 850 °C, B at 350 °C, the stoichiometric compound AB₂ (66.7 at.% B) melts "
            "congruently at 1000 °C; eutectic E at 700 °C and 30 at.% B; peritectic P at 500 °C (β of 80, liquid of "
            "95 at.% B); solubility of B in α 10 at.% at 700 °C and 2 at.% at 25 °C; solubility of A in β 25 at.% at 25 °C")


def problems_part2():
    REG.raster("pd-p9-alni", "Al-Ni phase diagram of the problem sheet",
               "Al-Ni phase diagram (Problems T4_PhaseDiagrams I.pdf, p. 3)", 620)
    REG.raster("pd-p10-cusn", "Cu-Sn phase diagram of the problem sheet",
               "Cu-Sn phase diagram (Problems T4_PhaseDiagrams I.pdf, p. 4)", 640)
    REG.raster("pd-p12-nimo", "Ni-Mo phase diagram of the problem sheet",
               "Ni-Mo phase diagram (Problems T4_PhaseDiagrams I.pdf, p. 5)", 600)
    REG.raster("pd-p13-tisi", "Ti-Si phase diagram of the problem sheet",
               "Ti-Si phase diagram (Problems T4_PhaseDiagrams I.pdf, p. 6)", 640)
    REG.raster("pd-p14-diagram", "Hypothetical A-B phase diagram of problem 14",
               "Hypothetical A-B phase diagram (Problems T4_PhaseDiagrams I.pdf, p. 6)", 420)
    REG.raster("pd-p15-tib", "Ti-B phase diagram of the problem sheet",
               "Ti-B phase diagram in weight percent (Problems T4_PhaseDiagrams I.pdf, p. 7)", 640)
    pd_p11()
    micro_figure("pd-micro-p9", "Problem 9: microstructure of Al-20 wt% Ni at 400 °C",
                 "Al-20 wt% Ni at 400 °C: primary Al₃Ni crystals (about 39 %) in the eutectic (Al) + Al₃Ni (about 61 %)",
                 BLOBS_FEW + [(-55, 30, 14)], "primary Al₃Ni", "eutectic ((Al) + Al₃Ni)")
    micro_figure("pd-micro-p12", "Problem 12: microstructure of Ni-40 wt% Mo just below 1310 °C",
                 "Ni-40 wt% Mo just below 1310 °C: primary NiMo (25 %) in the eutectic α + NiMo (75 %)",
                 BLOBS_FEW, "primary NiMo", "eutectic (α + NiMo)")
    micro_figure("pd-micro-p13", "Problem 13: microstructure of Ti-30 wt% Si just below 1330 °C",
                 "Ti-30 wt% Si just below 1330 °C: primary Ti₅Si₃ (76 %) in the eutectic βTi + Ti₅Si₃ (24 %)",
                 BLOBS_MANY, "primary Ti₅Si₃", "eutectic (βTi + Ti₅Si₃)")
    micro_figure("pd-micro-p15", "Problem 15: microstructure of Ti-10 wt% B",
                 "Ti-10 wt% B below 1540 °C: primary TiB (50 %) in the eutectic Ti + TiB (50 %)",
                 BLOBS_MANY[:4], "primary TiB", "eutectic (Ti + TiB)")


# --------------------------------------------------------------------------- figures copied from the slides
def rasters():
    REG.raster("s7-ferrite-pearlite", "Micrograph of a steel with ferrite and pearlite",
               "Microconstituents in a steel: 1 is ferrite, 2 and 3 are pearlite (ferrite + cementite). From Session 7 "
               "Slide 2", 520)
    REG.raster("s7-water-high-pressure", "Phase diagram of water up to 4 GPa",
               "Water at high pressure (up to 4 GPa): several crystal structures of ice (I, II, III, V, VI, VII, VIII), each "
               "a different solid phase. From Session 7 Slide 5", 440)
    REG.raster("s7-coring-sketches", "Cored crystals growing in the liquid at T2 and T4",
               "Cored crystals of the Ni-30 % Cu alloy growing in the liquid at T₂ and T₄: each new layer (α′₁, α′₂, …) has "
               "a different composition. From Session 7 Slide 24", 480)
    REG.raster("s7-coring-micrograph", "Micrograph of a cored structure",
               "Micrograph of a cored (microsegregated) structure: the rings in each grain are layers of different "
               "composition. From Session 7 Slide 24", 440)
    REG.raster("s7-eutectic-sketches", "Eutectic forming from the liquid in Pb-Sn",
               "Pb-Sn eutectic: layers of α and β grow together from the liquid of 61.9 % Sn (top) until the whole "
               "structure is eutectic colonies (bottom). From Session 7 Slide 28", 260)
    REG.raster("s7-eutectic-lamellae", "Lamellae of the eutectic product",
               "The eutectic product: alternating lamellae of α and β; λ is the spacing of the layers. From Session 7 "
               "Slide 28", 240)
    REG.raster("s7-pbsn-eutectic-micrograph", "Micrograph of the Pb-Sn eutectic",
               "Micrograph of the Pb-Sn eutectic (scale bar 40 µm): dark and light layers are the two phases. From "
               "Session 7 Slide 28", 420)
    REG.raster("s7-eutectic-micrographs", "Eutectic microstructures of four alloys",
               "Eutectic microstructures: (a) Sn-50 % In, (b) Al-13 % Si, (c) Al-33 % Cu, (d) Mg-37 % Sn. From Session 7 "
               "Slide 29", 620)
    REG.raster("s7-hypoeutectic-mould", "Hypoeutectic solidification in a mould",
               "Hypoeutectic solidification in a mould: primary α grows from the mould wall and the last liquid, between "
               "the crystals, reaches the eutectic composition. From Session 7 Slide 30", 360)
    REG.raster("s7-hypoeutectic-sketches", "Microstructure of a hypoeutectic Pb-Sn alloy during cooling",
               "Hypoeutectic Pb-Sn alloy, from top to bottom: α crystals in the liquid; α of 19 % Sn in liquid of 61.9 % Sn "
               "just above the eutectic temperature; eutectic forming around the α; primary α in a eutectic matrix. From "
               "Session 7 Slide 30", 300)
    REG.raster("s7-hypoeutectic-micrograph", "Micrograph of a hypoeutectic Pb-Sn alloy",
               "Micrograph of a hypoeutectic Pb-Sn alloy: dark rounded primary α in the lamellar eutectic. From "
               "Session 7 Slide 30", 400)
    REG.raster("s7-hypereutectic-sketches", "Microstructure of a hypereutectic alloy during cooling",
               "Hypereutectic alloy, from top to bottom: β crystals in the liquid; primary β just above the eutectic "
               "temperature; primary β in a eutectic matrix. From Session 7 Slide 31", 150)
    REG.raster("s7-hypereutectic-micrograph", "Micrograph of a hypereutectic alloy",
               "Micrograph of a hypereutectic alloy: light rounded primary β in the eutectic. From Session 7 Slide 31", 440)


def build():
    co2()
    water()
    water_logp()
    iron_pt()
    cooling_curves()
    iso_construction()
    iso_micro()
    complete_solubility()
    gibbs()
    tie_line()
    coring()
    coring_nicu()
    eutectic_generic()
    eutectic_cooling()
    pbsn()
    hypoeutectic()
    hypereutectic()
    eutectic_lever()
    rasters()
    theory_part2()
    problems()
    problems_part2()
    return REG
