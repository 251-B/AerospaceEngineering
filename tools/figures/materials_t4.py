"""Topic 4 figures for Aerospace Materials I: phase diagrams (Session 7 T4 Phase diagrams I).

The theory figures (diagrams, micrographs, sketches) are 200 DPI PNG crops of the slides, registered with
`REG.raster`. The remaining SVGs are the problem-sheet figures (`pd_*`, `fc_*`, Problems T4_PhaseDiagrams I.pdf,
inlined in the problems pages), the cooling curves of the isomorphous construction and the Fe-Cr-Ni reading
overlay (both EXTRA, not in the slides).
Run `python tools/build_topic_pages.py` to write the SVG files to vault/attachments/T4 and rebuild the page.
"""
import math

from figures.svgkit import Canvas, Registry, dot, fmt, line, text

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


def circle(c, p, r, col="EDGE", w=1.4, fill="none", op=None):
    o = f' fill-opacity="{op}"' if op is not None else ""
    c.add(f'<circle cx="{fmt(p[0])}" cy="{fmt(p[1])}" r="{fmt(r)}" fill="{fill}"{o} stroke="{col}" stroke-width="{w}"/>')


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


# --------------------------------------------------------------------------- reference shapes
def lens(x, ta, tb, up):
    """Isomorphous liquidus (up=True, above the chord) or solidus between the melting points of A and B."""
    return ta + (tb - ta) * (x ** 0.62 if up else x ** 1.9)


# Pb-Sn as drawn in the slides [Session 7 Slide 32]: eutectic 183 °C at 61.9 wt% Sn, alpha 18.3, beta 97.8.
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


# --------------------------------------------------------------------------- Session 9 figures (Part III, Fe-C)


def fec_a3(x):
    """A3 line (γ / α + γ) from 912 °C at 0 % C to the eutectoid point, through 775 °C at 0.4 % C."""
    return lagrange([(0, 912), (0.4, 775), (0.76, 727)])(x)


def fec_a3_inv(t):
    return bisect(lambda x: fec_a3(x) - t, 0.0, 0.76)


def fec_acm_inv(t):
    return 0.76 + (t - 727) * (2.14 - 0.76) / (1147 - 727)


def fec_diagram(c, P, uid, labels=True):
    """The metastable Fe-Fe3C diagram of Session 9 Slide 4, clipped to the plot box of P."""
    c.add(f'<clipPath id="clip-{uid}"><rect x="{fmt(P.x0)}" y="{fmt(P.y0)}" width="{fmt(P.x1 - P.x0)}" '
          f'height="{fmt(P.y1 - P.y0)}"/></clipPath>')
    c.add(f'<g clip-path="url(#clip-{uid})">')
    a3 = [(x, fec_a3(x)) for x in lin(0, 0.76)]
    P.area([(0, 2000), (0, 1538), (0.53, 1493), (4.30, 1147), (6.67, 1250), (6.67, 2000)], "BLUE", 0.08)
    P.area([(0, 1394), (0.16, 1493), (2.14, 1147), (0.76, 727)] + list(reversed(a3)), "BLUE", 0.16)
    P.area([(0, 912), (0.022, 727), (0.008, 600), (0, 300)], "BLUE", 0.16)
    segs = ([(0, 1538), (0.53, 1493), (4.30, 1147)], [(0, 1538), (0.09, 1493)], [(0, 1394), (0.09, 1493)],
            [(0, 1394), (0.16, 1493)], [(0.09, 1493), (0.53, 1493)], [(0.16, 1493), (2.14, 1147)],
            [(2.14, 1147), (6.67, 1147)], [(2.14, 1147), (0.76, 727)], a3, [(0, 912), (0.022, 727)],
            [(0.022, 727), (0.012, 600), (0.004, 400), (0, 300)], [(0.022, 727), (6.67, 727)], [(6.67, 300), (6.67, 1250)])
    for s in segs:
        P.line(s, "ACC", 2.2)
    P.line([(4.30, 1147), (5.5, 1215), (6.67, 1250)], "ACC", 1.8, "7,5")
    c.add("</g>")
    if labels:
        P.text(0.9, 960, "γ, austenite", size=12.5)
        P.text(0.2, 790, "α + γ", size=11.5)
        P.text(3.8, 640, "α + Fe₃C", size=13)
        P.text(3.8, 950, "γ + Fe₃C", size=13)


def fec_part3():
    REG.raster("s9-steel-micrographs", "Micrographs of two steels",
               "Different microstructures in the Fe-C system. From Session 9 Slide 2", 600)
    REG.raster("s9-iron-cells", "FCC and BCC cells of iron", "Unit cells of Fe-γ (FCC, top) and Fe-α (BCC, bottom). From Session 9 "
               "Slide 3", 200)
    REG.raster("s9-ferrite", "Ferrite: BCC cell and micrograph", "α-ferrite: BCC cell and micrograph of its grains. From Session 9 Slide 5", 480)
    REG.raster("s9-austenite", "Austenite: FCC cell with a carbon atom and micrograph",
               "Austenite: FCC cell with a C atom in an interstitial site, and micrograph. From Session 9 Slide 6", 460)
    REG.raster("s9-cementite-cell", "Unit cell of cementite", "Unit cell of cementite, Fe₃C. From Session 9 Slide 8", 280)
    REG.raster("s9-microconstituents", "Microconstituents of the Fe-C system",
               "Microconstituents of the Fe-C system: pearlite, ferrite and cementite in steels; ledeburite in cast "
               "irons. The figure uses older values (0.83 % C, 723 and 1130 °C). From Session 9 Slide 11", 640)
    REG.raster("s9-pearlite-micrograph", "Micrograph of pearlite",
               "Pearlite: alternating layers of ferrite (light) and cementite (dark). From Session 9 Slide 12", 360)
    REG.raster("s9-pearlite-growth", "Growth of pearlite",
               "Growth of pearlite from an austenite grain boundary: ferrite rejects carbon, which diffuses to the "
               "neighbouring zones where cementite forms. From Session 9 Slide 12", 420)
    REG.raster("s9-hypoeutectoid-micrograph", "Micrograph of a hypoeutectoid steel",
               "Hypoeutectoid steel: light proeutectoid (primary) ferrite and dark pearlite. From Session 9 Slide 14", 480)
    REG.raster("s9-hypereutectoid-micrograph", "Micrograph of a hypereutectoid steel",
               "Hypereutectoid steel: a network of proeutectoid cementite (light) around pearlite colonies. From "
               "Session 9 Slide 19", 340)
    REG.raster("s9-microstructures", "Microstructures of 0.4, 0.8 and 1.2 % C steels",
               "Microstructures on cooling of steels with 0.4, 0.8 and 1.2 % C. The figure uses older values (0.8 % C, "
               "723 °C). From Session 9 Slide 20", 660)
    REG.raster("s9-cooling-rate", "Effect of the cooling rate on the eutectoid",
               "With a higher cooling rate the eutectoid point moves to lower temperatures and lower carbon contents. "
               "From Session 9 Slide 21", 600)
    REG.raster("s9-coarse-fine-pearlite", "Coarse and fine pearlite",
               "Coarse pearlite (slow cooling, top) and fine pearlite (fast cooling, bottom). From Session 9 Slide 21", 240)
    REG.raster("s9-alloy-elements", "Effect of Cr and Mn on the Fe-C diagram",
               "α-stabilising elements such as Cr shift the eutectoid to higher temperature and lower %C; γ-stabilising "
               "elements such as Mn shift it to lower temperature and lower %C. From Session 9 Slide 22", 640)
    REG.raster("s9-alloy-curves", "Eutectoid composition and temperature against alloying content",
               "Influence of alloying elements on the eutectoid composition (left) and temperature (right). From "
               "Session 9 Slide 23", 640)


# --------------------------------------------------------------------------- Session 10 figures (Part IV)


def tern_xy(cx, cy, side, a, b, c_):
    """Point of the triangle with A at the top, the second component at the bottom left and the third at the
    bottom right (fractions add up to 1)."""
    h = side * math.sqrt(3) / 2
    top, bl, br = (cx, cy - 2 * h / 3), (cx - side / 2, cy + h / 3), (cx + side / 2, cy + h / 3)
    return (a * top[0] + b * bl[0] + c_ * br[0], a * top[1] + b * bl[1] + c_ * br[1])


def tern_grid(c, cx, cy, side, names, ticks=True):
    pt = lambda a, b, c_: tern_xy(cx, cy, side, a, b, c_)      # noqa: E731
    for k in range(1, 10):
        f = k / 10
        line(c, pt(f, 1 - f, 0), pt(f, 0, 1 - f), "EDGE", 0.7)
        line(c, pt(0, f, 1 - f), pt(1 - f, f, 0), "EDGE", 0.7)
        line(c, pt(0, 1 - f, f), pt(1 - f, 0, f), "EDGE", 0.7)
    poly(c, [pt(1, 0, 0), pt(0, 1, 0), pt(0, 0, 1)], "HEAD", 2, fill="BLUE", op=0.06)
    poly(c, [pt(1, 0, 0), pt(0, 1, 0), pt(0, 0, 1), pt(1, 0, 0)], "HEAD", 2)
    ta, tb, tc = names
    text(c, pt(1, 0, 0), ta, "HEAD", "middle", 14, "700", dy=-10)
    text(c, pt(0, 1, 0), tb, "HEAD", "end", 14, "700", dx=-8, dy=8)
    text(c, pt(0, 0, 1), tc, "HEAD", "start", 14, "700", dx=8, dy=8)
    return pt


def tern_reading(name, title, caption, names, point, label, axes):
    """Triangle with one point and the three lines through it parallel to the sides (the reading construction)."""
    c = Canvas(560, 470)
    pt = tern_grid(c, 280, 260, 400, names)
    a, b, c_ = point
    p = pt(a, b, c_)
    for q, col in ((pt(a, 1 - a, 0), "PINK"), (pt(a, 0, 1 - a), "PINK"), (pt(0, b, 1 - b), "GREEN"), (pt(1 - b, b, 0), "GREEN"),
                   (pt(0, 1 - c_, c_), "BLUE"), (pt(1 - c_, 0, c_), "BLUE")):
        line(c, p, q, col, 1.8, "6,4")
    dot(c, p, 6, "ACC")
    text(c, p, label, "ACC", "start", 14, "700", dx=8, dy=-8)
    text(c, pt(a, 0, 1 - a), axes[0], "PINK", "start", 12.5, "700", dx=10, dy=4)       # top component: right side
    text(c, pt(1 - b, b, 0), axes[1], "GREEN", "end", 12.5, "700", dx=-10, dy=4)      # bottom-left: left side
    text(c, pt(0, 1 - c_, c_), axes[2], "BLUE", "middle", 12.5, "700", dy=22)        # bottom-right: bottom side
    REG.put(name, c, title, caption)


def part4():
    tern_reading("fecrni-reading", "Reading points 1 and 2 of the Fe-Cr-Ni isotherm",
                 "Reading of point 1 of the Fe-Cr-Ni isotherm at 650 °C: the three lines through it parallel to the sides "
                 "meet the axes at 60 % Cr, 20 % Ni and 20 % Fe. Reading construction for point 1 of Session 10 Slide 7; the slide prints the values but does not draw these lines (EXTRA)",
                 ("Cr", "Fe", "Ni"), (0.6, 0.2, 0.2), "1", ("60 % Cr", "20 % Fe", "20 % Ni"))
    tern_reading("fc-p11", "Problem FC11: reading the ternary alloy H",
                 "Alloy H of the problem sheet: the lines through H parallel to the sides give 30 % A, 30 % B and 40 % C",
                 ("A", "B", "C"), (0.3, 0.3, 0.4), "H", ("30 % A", "30 % B", "40 % C"))
    REG.raster("s10-alcr-wide", "Al2O3-Cr2O3 down to 600 °C",
               "Al₂O₃-Cr₂O₃ over a wider temperature range: complete solid solution between about 2100 and 950 °C, and "
               "two solid solutions (immiscibility) below 950 °C. From Session 10 Slide 2", 300)
    REG.raster("s10-alsi-refractories", "Refractories and microstructures in Al2O3-SiO2",
               "Al₂O₃-SiO₂ (composition in wt% SiO₂) with the microstructures of alumina and mullite refractories, "
               "firebrick and silica brick; mullite, 3Al₂O₃·2SiO₂, is the intermediate phase. From Session 10 Slide 4", 620)
    REG.raster("s10-ternary-3d", "Space model of a ternary diagram",
               "A ternary phase diagram as a solid: composition in the triangle base, temperature upwards. From Session 10 "
               "Slide 5", 460)
    REG.raster("s10-agcuzn", "Ag-Cu-Zn liquidus, solidus and 350 °C isotherm",
               "Ag-Cu-Zn: projections of the liquidus and solidus surfaces and the isotherm at 350 °C. From Session 10 "
               "Slide 6", 640)
    REG.raster("s10-fecrni", "Fe-Cr-Ni isotherm at 650 °C",
               "Fe-Cr-Ni isotherm at 650 °C (stainless steels) with points 1 and 2. From Session 10 Slide 7", 520)
    REG.raster("s10-ceramic-ternaries", "CaO-Al2O3-SiO2 and clay-feldspar-quartz diagrams",
               "Ceramic ternary diagrams: CaO-Al₂O₃-SiO₂ (cements, glasses, refractories) and clay-feldspar-quartz "
               "(traditional ceramics: porcelains, pottery, earthenware). From Session 10 Slide 8", 640)
    REG.raster("fc-p11-sheet", "Ternary diagram of problem 11",
               "Ternary diagram with the alloy H (Problems T4_PhaseDiagrams II.pdf, p. 3)", 420)


def fc_problem(name, c0, marks, ties, title, caption):
    """Problem of sheet II on the Fe-Fe3C diagram: alloy line, temperatures and tie lines.
    marks: (T, label); ties: (T, c_left, c_right, label_left, label_right). Temperatures 1147 ± ΔT and 727 ± ΔT
    are drawn 12 °C apart so that they can be told apart."""
    c = Canvas(680, 430)
    P = Plot(c, (80, 30, 600, 360), (0, 6.7), (400, 1600))
    fec_diagram(c, P, name, labels=False)
    P.frame([(x, str(x)) for x in range(7)], [(t, str(t)) for t in range(400, 1601, 200)],
            "Composition (wt% C)", "Temperature (°C)")
    P.text(4.6, 1420, "L", size=13)
    P.text(0.7, 1000, "γ", size=13)
    P.text(4.8, 940, "γ + Fe₃C", size=12)
    P.text(4.8, 560, "α + Fe₃C", size=12)
    P.vseg(c0, 400, 1590, "GREEN", 1.5, "6,4")
    P.text(c0, 1560, sub("C", "0") + f" = {c0:g}", "GREEN", "start", 12, dx=6)
    for t, cl, cr, ll, lr in ties:
        P.line([(cl, t), (cr, t)], "BLUE", 1.8)
        P.dot(cl, t, 3.2, "BLUE"); P.dot(cr, t, 3.2, "BLUE")
        if ll:
            P.text(cl, t, ll, "BLUE", "end", 11, dx=-4, dy=4)
        if lr:
            P.text(cr, t, lr, "BLUE", "start", 11, dx=5, dy=4)
    for t, s in marks:
        P.dot(c0, t, 3.8, "GREEN")
        above = t in (1155, 735) or (t > 727 and t not in (1139, 900, 800, 600))
        P.text(c0, t, s, "GREEN", "start", 11.5, dx=6, dy=-6 if above else (15 if t in (1139, 719) else -6))
    REG.put(name, c, title, caption)


def fc_problems():
    REG.raster("fc-sheet-diagram", "Fe-Fe3C phase diagram of the problem sheet",
               "Fe-Fe₃C phase diagram (Problems T4_PhaseDiagrams II.pdf, p. 1)", 640)
    up, dn, ep, ed = 1155, 1139, 735, 719
    fc_problem("fc-p1", 0.5, ((up, "T₁"), (dn, "T₂"), (900, "T₃"), (ep, "T₄"), (ed, "T₅")),
               ((ep, 0.022, 0.76, "", "0.76"), (ed, 0.022, 6.67, "", "6.67")), "Problem FC01: steel of 0.5 % C",
               "Fe-0.5 % C: γ at T₁, T₂ and T₃; α (0.022) + γ (0.76) just above 727 °C; α + Fe₃C just below it. "
               "Temperatures 1147 ± ΔT and 727 ± ΔT are drawn slightly apart")
    fc_problem("fc-p2", 0.76, ((up, "T₁"), (dn, "T₂"), (900, "T₃"), (ep, "T₄"), (ed, "T₅")),
               ((ed, 0.022, 6.67, "", "6.67"),), "Problem FC02: eutectoid steel",
               "Fe-0.76 % C: γ down to 727 °C, then pearlite (α + Fe₃C)")
    fc_problem("fc-p3", 1.5, ((up, "T₁"), (dn, "T₂"), (900, "T₃"), (ep, "T₄"), (ed, "T₅")),
               ((900, 1.3, 6.67, "1.3", "6.67"), (ep, 0.76, 6.67, "0.76", ""), (ed, 0.022, 6.67, "", "")),
               "Problem FC03: steel of 1.5 % C",
               "Fe-1.5 % C: γ at 1147 ± ΔT; γ + Fe₃C at 900 °C (γ of about 1.3 % C, a reading) and just above 727 °C; "
               "α + Fe₃C below 727 °C")
    fc_problem("fc-p4", 4.3, ((up, "T₁"), (dn, "T₂"), (900, "T₃"), (ep, "T₄"), (ed, "T₅")),
               ((dn, 2.14, 6.67, "2.14", ""), (900, 1.3, 6.67, "1.3", ""), (ep, 0.76, 6.67, "0.76", ""), (ed, 0.022, 6.67, "", "")),
               "Problem FC04: eutectic cast iron",
               "Fe-4.3 % C: liquid above 1147 °C, ledeburite (γ + Fe₃C) below it, and the tie lines at 900 °C and "
               "727 ± ΔT")
    fc_problem("fc-p5", 2.55, ((ed, "727 − ΔT"),), ((ed, 0.022, 6.67, "", "6.67"),), "Problem FC05: alloy from its cementite",
               "The alloy with 38 % Fe₃C just below 727 °C lies at 2.55 % C (computed in the problem)")
    fc_problem("fc-p6", 3.55, ((up, "T₁"), (dn, "T₂"), (ed, "727 − ΔT")),
               ((up, 2.14, 4.30, "2.14", "4.30"), (dn, 2.14, 6.67, "", "6.67"), (ed, 0.022, 6.67, "", "")),
               "Problem FC06: hypoeutectic cast iron",
               "The alloy with 47 % α just below 727 °C lies at about 3.55 % C: γ + L above 1147 °C, γ + Fe₃C below it")
    fc_problem("fc-p7", 4.88, ((up, "T₁"), (dn, "T₂"), (ed, "727 − ΔT")),
               ((up, 4.30, 6.67, "4.30", ""), (dn, 2.14, 6.67, "2.14", ""), (ed, 0.022, 6.67, "", "")),
               "Problem FC07: hypereutectic cast iron",
               "The alloy with 73 % Fe₃C just below 727 °C lies at about 4.88 % C: L + Fe₃C above 1147 °C, "
               "γ + Fe₃C below it")
    fc_problem("fc-p8", 0.55, ((ed, "726 °C"), (600, "600 °C")),
               ((ed, 0.022, 6.67, "", "6.67"), (600, 0.012, 6.67, "", "")), "Problem FC08: annealed steel of 0.55 % C",
               "Fe-0.55 % C at 726 °C and at 600 °C: α + Fe₃C, as proeutectoid ferrite and pearlite")
    fc_problem("fc-p9", 3.0, ((1155, "1148 °C"), (1139, "1146 °C"), (800, "800 °C")),
               ((1155, 2.14, 4.30, "2.14", "4.30"), (1139, 2.14, 6.67, "", ""), (800, 1.0, 6.67, "1.0", "")),
               "Problem FC09: hypoeutectic cast iron of 3 % C",
               "Fe-3 % C: γ + L just above 1147 °C, primary γ + ledeburite just below it, γ (about 1.0 % C, a reading) "
               "+ Fe₃C at 800 °C")
    fc_problem("fc-p10", 4.9, ((ed, "727 − ΔT"),), ((ed, 0.022, 6.67, "", "6.67"),), "Problem FC10: alloy from its ferrite",
               "The alloy with 26.7 % α just below 727 °C lies at about 4.9 % C, a hypereutectic cast iron")
    micro_figure("fc-micro-p1", "Problem FC01: microstructure of a 0.5 % C steel",
                 "Fe-0.5 % C below 727 °C: proeutectoid ferrite (35 %) and pearlite (65 %)",
                 BLOBS_MANY[:5], "proeutectoid α", "pearlite (α + Fe₃C)")
    micro_figure("fc-micro-p2", "Problem FC02: microstructure of a eutectoid steel",
                 "Fe-0.76 % C below 727 °C: 100 % pearlite", [], "", "pearlite (α + Fe₃C)")
    micro_figure("fc-micro-p8", "Problem FC08: microstructure of a 0.55 % C steel",
                 "Fe-0.55 % C below 727 °C: proeutectoid ferrite (28 %) and pearlite (72 %)",
                 BLOBS_FEW + [(-55, 30, 14)], "proeutectoid α", "pearlite (α + Fe₃C)")
    micro_figure("fc-micro-p9", "Problem FC09: microstructure of a 3 % C cast iron at 1146 °C",
                 "Fe-3 % C just below 1147 °C: primary austenite (60 %) and ledeburite (40 %)",
                 BLOBS_MANY, "primary γ", "ledeburite (γ + Fe₃C)")


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
    micro_figure("pd-micro-p12", "Problem 12: microstructure of Ni-40 at.% Mo just below 1310 °C",
                 "Ni-40 at.% Mo just below 1310 °C: primary NiMo (25 %) in the eutectic α + NiMo (75 %)",
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


def iso_construction_extra():
    c = Canvas(400, 330)
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
    REG.put("iso-construction-extra", c, "Cooling curves of five A-B alloys",
            "Cooling curves of alloys with 0, 20, 50, 80 and 100 % B: the pure components solidify at one temperature, "
            "the alloys between the start (liquidus) and the end (solidus) of solidification, the green points. "
            "Redrawn because on Session 7 Slide 9 the milk photographs cover the curves. Portal drawing, not in the slides (EXTRA).")


def theory_rasters():
    """Theory figures copied from the slides (200 DPI crops in vault/attachments/T4)."""
    REG.raster("co2", "Phase diagram of CO2",
               "Phase diagram of CO2 (labels in Spanish: Sólido, Líquido, Gas; Presión, Temperatura): triple point at 5.1 atm and −56.6 °C, sublimation at 1 atm and −78.2 °C, critical point at 73 atm and 31.1 °C. Copied from Session 7 Slide 3", 440)
    REG.raster("water", "Phase diagram and cooling curve of water",
               "Left: P-T diagram of water with the sublimation (A to P_T), melting (P_T to B) and vaporisation (P_T to C) lines and the triple point P_T; the dashed line is the cooling path at constant pressure. Right: its cooling curve, with the plateaus 2 (condensation at T_v) and 4 (solidification at T_m). The blue marks are handwritten on the slide. Copied from Session 7 Slide 5", 720)
    REG.raster("water-logp", "Water at 1 atm on a log-pressure diagram",
               "Temperature against pressure (log scale) for water: at 1 atm the vertical line meets the melting line at 0 °C and the vaporisation line at 100 °C. Copied from Session 7 Slide 5", 540)
    REG.raster("iron-pt", "Phase diagram of pure iron",
               "P-T diagram of pure iron (pressure on a log scale) with α-Fe (BCC), γ-Fe (FCC), δ-Fe (BCC), liquid and vapour, the triple points and the slide's potato analogy. Copied from Session 7 Slide 6", 720)
    REG.raster("cooling-curves", "Cooling curves of pure iron and of a pure metal",
               "Left: cooling curve of pure iron, with a thermal arrest at 1538, 1394 and 912 °C. Right: cooling curve of a pure metal: A to B cooling of the liquid, B solidification begins, C solidification ends, C to D cooling of the solid. Copied from Session 7 Slide 8", 760)
    REG.raster("iso-construction", "Isomorphous diagram",
               "Binary isomorphous diagram: liquidus and solidus between the melting points of A and B, with the regions L, L + SS and SS. Copied from Session 7 Slide 9", 460)
    REG.raster("iso-micro", "Microstructure along the cooling of an isomorphous alloy",
               "An alloy (system composition) cooled through the isomorphous diagram: all liquid L_system above the liquidus, crystallites of SS1 in a matrix of L1 at T1, and a polycrystalline solid SS_system below the solidus. Copied from Session 7 Slide 10", 600)
    REG.raster("complete-solubility-a", "Complete solid solubility",
               "Isomorphous diagram with complete solid solubility from the melting point of A (1118 °C) to that of B (1553 °C), composition in mole fraction; the green dashed lines mark the alloys whose atom arrangements are shown below. Copied from Session 7 Slide 11", 420)
    REG.raster("complete-solubility-b", "Atomic arrangements of A-B solid solutions",
               "Arrangement of A and B atoms in the same lattice for increasing B content: B atoms replace A atoms at any proportion. Copied from Session 7 Slide 11", 720)
    REG.raster("gibbs-a", "Gibbs phase rule in a unary diagram",
               "One component, F = C − P + 2: F = 2 in a single-phase region, 1 on a two-phase line and 0 at the triple point. Copied from Session 7 Slide 13", 460)
    REG.raster("gibbs-b", "Gibbs phase rule in a binary diagram",
               "Two components at 1 atm, F = C − P + 1: F = 2 in L or in the solid, 1 in L + solid and on its boundaries, 0 at the melting point of a pure component. Copied from Session 7 Slide 13", 440)
    REG.raster("tie-line-a", "Tie line and lever rule",
               "Tie line through the alloy B (C_0) in the α + liquid region: it ends at C_L on the liquidus and at C_α on the solidus, and R and S are its two arms; Slide 16 prints C_L = 32, C_0 = 35 and C_α = 43 wt% Ni. Copied from Session 7 Slide 15", 520)
    REG.raster("coring", "Non-equilibrium solidification of Cu-35 wt% Ni",
               "Cooling of a Cu-35 wt% Ni alloy too fast for equilibrium: tie lines at b′, c′, d′ and e′, the cored crystals (46, 40, 35 and 31 wt% Ni from the centre out) and the dashed non-equilibrium solidus. Temperature (°C) against composition (wt% Ni). Copied from Session 7 Slide 23", 460)
    REG.raster("coring-nicu", "Equilibrium and non-equilibrium solidus of Ni-30 wt% Cu",
               "Ni-30 wt% Cu alloy (labels in Spanish): with equilibrium cooling the solid follows α1 … α5 and solidification ends at T5; with fast cooling the average composition follows the non-equilibrium solidus α′2 … α′7 and it ends at T7. Copied from Session 7 Slide 24", 520)
    REG.raster("eutectic-generic", "Binary eutectic system",
               "Binary eutectic diagram with liquidus, solidus and solvus, the regions L, α, β, α + L, L + β and α + β, the eutectic temperature and composition, and the eutectic microstructure of fine alternating layers of α and β. Copied from Session 7 Slide 26", 760)
    REG.raster("eutectic-cooling", "Cooling curve of the eutectic alloy and the eutectic reaction",
               "Cooling curve at the eutectic temperature (183 °C plateau; axes in Spanish, Temperatura and Tiempo) and the shape of the eutectic reaction L → α + β on the diagram. Copied from Session 7 Slide 27", 720)
    REG.raster("pbsn", "The Pb-Sn eutectic system",
               "Pb-Sn phase diagram (axes in Spanish: Temperatura, Peso porcentual de estaño) with the eutectic at about 61.9 wt% Sn and 183 °C; the thick arrows point to the sketches of the eutectic reaction shown below. Copied from Session 7 Slide 28", 480)
    REG.raster("hypoeutectic-a", "Hypoeutectic Pb-Sn alloy on the diagram",
               "Pb-Sn diagram with the dashed line of the hypoeutectic alloy (about 30 wt% Sn); the arrows point to the microstructure sketches shown below. Copied from Session 7 Slide 30", 400)
    REG.raster("hypoeutectic-b", "Cooling curve of a hypoeutectic alloy",
               "Cooling curve of the hypoeutectic alloy: liquidus at 260 °C, α + L, the eutectic plateau at 183 °C (L → α + β) and α + eutectic below it. Copied from Session 7 Slide 30", 460)
    REG.raster("hypereutectic-a", "Hypereutectic alloy on the diagram",
               "Eutectic diagram with the dashed line of a hypereutectic alloy and its points in L, L + β and α + β; the arrows point to the microstructure sketches shown below. Copied from Session 7 Slide 31", 460)
    REG.raster("hypereutectic-b", "Cooling curve of a hypereutectic alloy",
               "Cooling curve of the hypereutectic alloy: primary β forms below the liquidus, then the eutectic plateau (L → α + β) and β + eutectic below it; the slide repeats the labels 260 and 183 °C of the hypoeutectic curve. Copied from Session 7 Slide 31", 460)
    REG.raster("eutectic-lever", "Lever rule in the Pb-Sn eutectic diagram",
               "Pb-Sn diagram with the segments P, Q and R of the tie line just below 183 °C, from 18.3 wt% Sn (α) through the alloy C′4 and the eutectic 61.9 wt% Sn to 97.8 wt% Sn (β). Copied from Session 7 Slide 32", 520)
    REG.raster("precip-pbsn-a", "Pb-1 wt% Sn below the solvus",
               "Pb-Sn diagram with the alloy C1 (1 wt% Sn) and its microstructures at a (liquid), b (α + L) and c (only α). Copied from Session 8 Slide 2", 340)
    REG.raster("precip-pbsn-b", "Pb-16 wt% Sn crossing the solvus",
               "Pb-Sn diagram with the alloy C2 (16 wt% Sn) and its microstructures at d (liquid), e (α + L), f (only α) and g (α + β precipitates after crossing the solvus line). Copied from Session 8 Slide 4", 360)
    REG.raster("precip-generic", "Solid-state precipitation in an alloy of 20 % B",
               "Cooling of an alloy of 20 % B: all liquid, α1 in a matrix of L1, all α, and β2 particles in a matrix of α2 after crossing the solvus (the slide prints '00%' for 100 %). Copied from Session 8 Slide 3", 620)
    REG.raster("invariant-table", "The five invariant reactions of binary diagrams",
               "Eutectic, peritectic, monotectic, eutectoid and peritectoid reactions with their equations on cooling and their shape on the diagram; the last two are solid-state reactions. Copied from Session 8 Slide 6", 700)
    REG.raster("cuzn-eutectoid", "The eutectoid point of the Cu-Zn system",
               "Detail of the Cu-Zn diagram around the eutectoid point E (560 °C, about 74 % Zn), where δ gives γ + ε, and the peritectic point P (598 °C). Copied from Session 8 Slide 7", 560)
    REG.raster("peritectic-generic", "A peritectic point",
               "Generic peritectic diagram: the reaction α + L → β at the peritectic point P, temperature T_P, between the points a and b. Copied from Session 8 Slide 8", 340)
    REG.raster("feni-peritectic", "The peritectic point of the Fe-Ni system",
               "Fe-Ni diagram near the peritectic at 1517 °C: δ (4.0 % Ni) + L (5.4 % Ni) → γ (4.3 % Ni), with the points a, b and c of the 4.3 % Ni alloy. Copied from Session 8 Slide 8", 520)
    REG.raster("ptag-peritectic", "The peritectic reaction in the Pt-Ag system",
               "Pt-Ag diagram with alloy 1 (42.4 % Ag) and alloy 2 (about 60 % Ag), the tie lines at 1400 °C and 1150 °C and the peritectic line at 1186 °C; the arrows lead to the microstructure sketches of the slide. Copied from Session 8 Slide 9", 440)
    REG.raster("peritectoid-generic", "A peritectoid point",
               "Generic peritectoid diagram: the solids α and β react to give γ at the circled peritectoid point. Copied from Session 8 Slide 11", 340)
    REG.raster("monotectic-cupb", "The monotectic reaction in the Cu-Pb system",
               "Cu-Pb diagram with the monotectic at 955 °C (36 % Pb, the blue dot), the miscibility gap of the liquid up to 991 °C and the line at 326 °C. Copied from Session 8 Slide 12", 460)
    REG.raster("mgni-melting", "Congruent and incongruent melting in the Mg-Ni system",
               "Mg-Ni diagram: MgNi2 melts congruently (at a maximum of the liquidus) and Mg2Ni incongruently (it ends at a horizontal peritectic line). Copied from Session 8 Slide 17", 720)
    REG.raster("fe-allotropy", "Allotropic phases of pure iron",
               "Allotropic phases of pure iron from room temperature to the liquid: Fe-α (BCC) up to 910 °C, Fe-γ (FCC) up to 1390 °C and Fe-δ (BCC) up to 1535 °C. Copied from Session 9 Slide 3", 300)
    REG.raster("fec-full", "The metastable Fe-Fe3C phase diagram",
               "Fe-Fe3C diagram up to 6.67 wt% C with the peritectic, eutectic (4.30 % C, 1147 °C) and eutectoid (0.76 % C, 727 °C) points marked, the limit 2.14 % C, and the ranges of hypoeutectoid and hypereutectoid steels and of hypoeutectic and hypereutectic cast irons. Copied from Session 9 Slide 4", 640)
    REG.raster("fec-eutectoid", "Cooling of a eutectoid steel (0.76 % C)",
               "Eutectoid steel: at a (above 727 °C) only austenite; at b (just below 727 °C) the austenite has become pearlite, layers of α and Fe3C. Copied from Session 9 Slide 12", 380)
    REG.raster("fec-hypo", "Cooling of a hypoeutectoid steel (0.3 % C)",
               "Hypoeutectoid steel C0: c only γ; d and e, proeutectoid α growing at the γ grain boundaries between the A3 line M-O and 727 °C; f, proeutectoid α and pearlite. Copied from Session 9 Slide 14", 420)
    REG.raster("fec-hyper", "Cooling of a hypereutectoid steel (1.2 % C)",
               "Hypereutectoid steel C1: g only γ; h, proeutectoid Fe3C at the γ grain boundaries below the Acm line; i, proeutectoid Fe3C and pearlite. Copied from Session 9 Slide 19", 420)
    REG.raster("alcr", "The Al2O3-Cr2O3 phase diagram",
               "Al2O3-Cr2O3: a lens-shaped liquid + solid solution region between the melting points of Al2O3 (2045 ± 5 °C) and Cr2O3 (2275 ± 25 °C), and the solid solution Al2-xCrxO3 below it. Copied from Session 10 Slide 2", 440)
    REG.raster("alsi", "The Al2O3-SiO2 phase diagram",
               "Al2O3-SiO2 with the eutectic at 1587 ± 10 °C, the mullite solid solution and the line at 1890 ± 10 °C where mullite melts incongruently. Copied from Session 10 Slide 3", 460)
    REG.raster("ternary-scheme", "Composition triangle of a ternary system",
               "Composition triangle of a ternary system A-B-C (A at the top, C bottom left, B bottom right) with a 10 % grid on each side. Copied from Session 10 Slide 5", 460)


def build():
    theory_rasters()
    iso_construction_extra()
    part2_rasters()
    rasters()
    fec_part3()
    problems()
    problems_part2()
    fc_problems()
    part4()
    return REG
