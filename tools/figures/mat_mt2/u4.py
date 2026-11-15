"""Unit 4 figures of the Midterm 2 bank (phase diagrams).

Diagrams read by the "From the shown ... phase diagram" questions (Pb-Sn and Fe-Fe3C with the values of the slides,
hypothetical A-B systems whose printed temperatures and compositions are the ones the questions use) and the four-picture
option sets of the "Which picture describes ...?" questions (cooling curves, invariant points, microstructures). Option
pictures carry neutral labels (A to D) so they do not give the answer away.
"""
import math

from figures.svgkit import Canvas, line, text, poly, dot, rect, circle, sub
from figures.mat_mt2.common import figure
from figures.materials_t4 import Plot, pbsn_curves, fec_diagram, lin

# Pb-Sn with the values of Session 7 Slide 32 (eutectic 183 °C at 61.9 wt% Sn, alpha 18.3, beta 97.8) and the melting
# points of the problem sheet (327 and 232 °C); the curve shapes are those of tools/figures/materials_t4.py.
PBSN_SLIDES = dict(tpb=327, tsn=232, te=183, ca=18.3, ce=61.9, cb=97.8, bulge=0.00724, sol_p=0.751, solv_a=2.224, solv_b=4.0)


def catmull(pts, n=12):
    """Smooth curve through the points (x, y) (Catmull-Rom spline; passes exactly through every point)."""
    out = []
    ext = [pts[0]] + list(pts) + [pts[-1]]
    for i in range(1, len(ext) - 2):
        p0, p1, p2, p3 = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
        for k in range(n):
            t = k / n
            t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    out.append(pts[-1])
    return out


# --------------------------------------------------------------------------- Pb-Sn with marked points
@figure("u4-pbsn-points", "Pb-Sn phase diagram with four marked points 1 to 4",
        "Pb-Sn phase diagram with the values of Session 7 Slide 32 (eutectic at 183 °C and 61.9 wt% Sn; α of 18.3 and "
        "β of 97.8 wt% Sn at 183 °C) and four marked points")
def pbsn_points():
    c = Canvas(640, 380)
    P = Plot(c, (80, 30, 560, 310), (0, 100), (0, 350))
    liq_a, liq_b, sol_a, sol_b, solv_a, solv_b = pbsn_curves(PBSN_SLIDES)
    d = PBSN_SLIDES
    P.area([(0, 350)] + liq_a + liq_b + [(100, 350)], "BLUE", 0.08)
    P.area(sol_a + solv_a + [(0, 0)], "BLUE", 0.16)
    P.area([(100, d["tsn"])] + list(reversed(sol_b)) + solv_b + [(100, 0)], "BLUE", 0.16)
    for cv in (liq_a, liq_b, sol_a, sol_b, solv_a, solv_b):
        P.line(cv, "ACC", 2.2)
    P.line([(d["ca"], d["te"]), (d["cb"], d["te"])], "ACC", 2.2)
    P.frame([(0, "0 (Pb)"), (18.3, "18.3"), (40, "40"), (61.9, "61.9"), (80, "80"), (100, "100 (Sn)")],
            [(0, "0"), (100, "100"), (183, "183"), (232, "232"), (327, "327")],
            "Composition (wt% Sn)", "Temperature (°C)")
    P.text(97.8, 183, "97.8", "TEXT", "end", 11.5, "400", dx=-4, dy=16)
    P.text(30, 310, "L")
    P.text(5, 150, "α", size=14)
    P.text(100, 140, "β", "HEAD", "start", dx=8)
    P.text(42, 120, "α + β")
    P.text(36, 205, "α + L", size=12)
    for (x, t, lab, dx, dy) in ((10, 100, "1", 8, -6), (8, 250, "2", 8, -6), (90, 200, "3", 10, 4), (50, 280, "4", 8, -6)):
        P.dot(x, t, 4.5, "GREEN")
        P.text(x, t, lab, "GREEN", "start" if dx > 0 else "end", 13, dx=dx, dy=dy)
    return c


# --------------------------------------------------------------------------- hypothetical isomorphous A-B
def iso_liq(x):
    """Liquidus: quadratic through 1000 °C (A), 1200 °C at 30 wt% B and 1400 °C (B); 1251 °C at 40 wt% B."""
    b = -266.6667 / 7000
    return 1000 + (200 - 900 * b) / 30 * x + b * x * x


def iso_sol(x):
    """Solidus: 1200 °C at 55 wt% B; 1138 °C at 40 wt% B."""
    return 1000 + 400 * (x / 100) ** (math.log(0.5) / math.log(0.55))


@figure("u4-iso-ab", "Isomorphous A-B phase diagram with a tie line at 1200 °C",
        "Hypothetical isomorphous A-B system: A melts at 1000 °C and B at 1400 °C; the tie line at 1200 °C meets the "
        "liquidus at 30 wt% B and the solidus at 55 wt% B; the dashed line is the alloy of 40 wt% B, whose liquidus and "
        "solidus temperatures are 1250 and 1140 °C")
def iso_ab():
    c = Canvas(640, 380)
    P = Plot(c, (80, 30, 560, 310), (0, 100), (900, 1500))
    liq = [(x, iso_liq(x)) for x in lin(0, 100, 60)]
    sol = [(x, iso_sol(x)) for x in lin(0, 100, 60)]
    P.area(liq + list(reversed(sol)), "BLUE", 0.10)
    P.area([(0, 1000)] + sol + [(100, 900), (0, 900)], "BLUE", 0.16)
    P.line(liq, "ACC", 2.2)
    P.line(sol, "ACC", 2.2)
    P.frame([(0, "0 (A)"), (20, "20"), (30, "30"), (40, "40"), (55, "55"), (80, "80"), (100, "100 (B)")],
            [(900, "900"), (1000, "1000"), (1140, "1140"), (1200, "1200"), (1250, "1250"), (1400, "1400"), (1500, "1500")],
            "Composition (wt% B)", "Temperature (°C)")
    for t in (1140, 1250):
        P.hseg(0, 40, t, "EDGE", 1, "3,4")
    P.vseg(40, 900, 1470, "GREEN", 1.6, "6,4")
    P.text(40, 1470, sub("C", "0") + " = 40", "GREEN", "start", 12, dx=6, dy=4)
    P.line([(30, 1200), (55, 1200)], "BLUE", 2.4)
    P.dot(30, 1200, 3.6, "BLUE")
    P.dot(55, 1200, 3.6, "BLUE")
    P.dot(40, 1200, 4.2, "GREEN")
    P.text(18, 1380, "L", size=15)
    P.text(80, 1020, "α", size=15)
    P.text(64, 1290, "α + L", size=12.5, dx=-6)
    return c


# --------------------------------------------------------------------------- hypothetical eutectic A-B
@figure("u4-eut-ab", "Eutectic A-B phase diagram with labelled temperatures and compositions",
        "Hypothetical eutectic A-B system: A melts at 800 °C and B at 650 °C; eutectic at 450 °C and 60 wt% B; at 450 °C "
        "α holds at most 15 wt% B and β at least 90 wt% B")
def eut_ab():
    c = Canvas(640, 380)
    P = Plot(c, (80, 30, 560, 310), (0, 100), (0, 900))
    liq_a = catmull([(0, 800), (30, 650), (60, 450)])
    liq_b = catmull([(60, 450), (80, 560), (100, 650)])
    sol_a = [(0, 800), (15, 450)]
    sol_b = [(100, 650), (90, 450)]
    solv_a = catmull([(15, 450), (9, 250), (5, 0)])
    solv_b = catmull([(90, 450), (94, 250), (97, 0)])
    P.area([(0, 900)] + liq_a + liq_b + [(100, 900)], "BLUE", 0.08)
    P.area(sol_a + solv_a + [(0, 0)], "BLUE", 0.16)
    P.area([(100, 650)] + list(reversed(sol_b)) + solv_b + [(100, 0)], "BLUE", 0.16)
    for cv in (liq_a, liq_b, sol_a, sol_b, solv_a, solv_b, [(15, 450), (90, 450)]):
        P.line(cv, "ACC", 2.2)
    P.frame([(0, "0 (A)"), (15, "15"), (30, "30"), (45, "45"), (60, "60"), (75, "75"), (90, "90"), (100, "100 (B)")],
            [(0, "0"), (200, "200"), (450, "450"), (650, "650"), (800, "800")],
            "Composition (wt% B)", "Temperature (°C)")
    for x, t in ((15, 450), (60, 450), (90, 450)):
        P.dot(x, t, 3.6, "HEAD")
    P.text(45, 780, "L", size=15)
    P.text(4, 330, "α", size=14)
    P.text(97, 330, "β", size=14, dx=-2)
    P.text(19, 560, "α + L", size=12.5)
    P.text(83, 505, "β + L", size=12)
    P.text(52, 220, "α + β", size=14)
    return c


# --------------------------------------------------------------------------- Fe-Fe3C with marked points
@figure("u4-fec-points", "Fe-Fe3C phase diagram with four marked points 1 to 4",
        "Metastable Fe-Fe3C diagram with the values of Session 9 Slides 4 and 10 (eutectoid 727 °C, 0.022, 0.76 and "
        "6.67 wt% C; eutectic 1147 °C, 2.14 and 4.30 wt% C) and four marked points")
def fec_points():
    c = Canvas(640, 400)
    P = Plot(c, (80, 30, 560, 330), (0, 7), (400, 1600))
    fec_diagram(c, P, "u4fec", labels=False)
    P.frame([(0, "0"), (0.76, "0.76"), (2.14, "2.14"), (4.30, "4.30"), (6.67, "6.67")],
            [(400, "400"), (727, "727"), (912, "912"), (1147, "1147"), (1400, "1400"), (1600, "1600")],
            "Composition (wt% C)", "Temperature (°C)")
    P.text(5.6, 1450, "L", size=14)
    P.text(4.2, 1000, "γ + Fe₃C", size=12.5)
    P.text(4.2, 560, "α + Fe₃C", size=12.5)
    P.text(6.67, 900, "Fe₃C", "HEAD", "start", 12, dx=6)
    P.text(1.5, 1300, "γ + L", size=12)
    P.text(0.35, 1050, "γ", size=13)
    for (x, t, lab, dx, dy) in ((0.4, 900, "1", 8, -6), (1.0, 600, "2", 8, -6), (1.8, 850, "3", 8, -6), (2.8, 1220, "4", 9, 5)):
        P.dot(x, t, 4.5, "GREEN")
        P.text(x, t, lab, "GREEN", "start", 13, dx=dx, dy=dy)
    return c


# --------------------------------------------------------------------------- hypothetical diagram with two compounds
@figure("u4-compound-ab", "A-B phase diagram with the intermediate compounds AB and AB3",
        "Hypothetical A-B system with two line compounds: AB (40 wt% B) and AB3 (75 wt% B). Invariant lines at 850, "
        "950 and 1050 °C; A melts at 1000 °C and B at 1300 °C")
def compound_ab():
    c = Canvas(640, 400)
    P = Plot(c, (80, 30, 560, 330), (0, 100), (600, 1400))
    seg = [((0, 1000), (20, 850)), ((20, 850), (40, 1150)), ((40, 1150), (55, 950)), ((55, 950), (65, 1050)),
           ((65, 1050), (100, 1300)), ((0, 1000), (5, 850)), ((5, 850), (3, 600)), ((100, 1300), (90, 1050)),
           ((90, 1050), (95, 600)), ((5, 850), (40, 850)), ((40, 950), (75, 950)), ((65, 1050), (90, 1050)),
           ((40, 600), (40, 1150)), ((75, 600), (75, 1050))]
    P.area([(0, 1400), (0, 1000), (20, 850), (40, 1150), (55, 950), (65, 1050), (100, 1300), (100, 1400)], "BLUE", 0.08)
    P.area([(0, 1000), (5, 850), (3, 600), (0, 600)], "BLUE", 0.16)
    P.area([(100, 1300), (90, 1050), (95, 600), (100, 600)], "BLUE", 0.16)
    for a, b in seg:
        P.line([a, b], "ACC", 2.2)
    P.frame([(0, "0 (A)"), (20, "20"), (40, "40"), (55, "55"), (65, "65"), (75, "75"), (90, "90"), (100, "100 (B)")],
            [(600, "600"), (850, "850"), (950, "950"), (1050, "1050"), (1150, "1150"), (1300, "1300")],
            "Composition (wt% B)", "Temperature (°C)")
    P.text(0, 1000, "1000 °C", "TEXT", "start", 11.5, "400", dx=6, dy=-8)
    P.text(40, 1150, "AB", "HEAD", "middle", 12.5, dy=-8)
    P.text(75, 640, "AB₃", "HEAD", "start", 12.5, dx=5)
    P.text(40, 640, "AB", "HEAD", "start", 12.5, dx=5)
    P.text(22, 1250, "L", size=15)
    P.text(2.5, 720, "α", size=13)
    P.text(97.5, 900, "β", size=13)
    P.text(22, 720, "α + AB", size=12)
    P.text(57, 760, "AB + AB₃", size=12)
    P.text(83, 820, "AB₃ + β", size=11.5)
    P.text(82, 1110, "L + β", size=11.5)
    for x, t in ((5, 850), (20, 850), (55, 950), (65, 1050), (90, 1050)):
        P.dot(x, t, 3.4, "HEAD")
    return c


# --------------------------------------------------------------------------- hypothetical solid-state (eutectoid) part
@figure("u4-eutectoid-ab", "Solid-state part of an A-B phase diagram with an invariant point at 600 °C",
        "Solid-state part of a hypothetical A-B diagram: the solid solution γ ends at 600 °C and 40 wt% B; at that "
        "temperature α holds 10 wt% B and β 80 wt% B")
def eutectoid_ab():
    c = Canvas(640, 360)
    P = Plot(c, (80, 30, 560, 290), (0, 100), (300, 900))
    gl = catmull([(0, 820), (20, 720), (40, 600)])
    gr = catmull([(40, 600), (65, 720), (100, 850)])
    al = catmull([(0, 820), (10, 600)])
    br = catmull([(100, 850), (80, 600)])
    sa = catmull([(10, 600), (6, 450), (4, 300)])
    sb = catmull([(80, 600), (86, 450), (90, 300)])
    P.area([(0, 900), (0, 820)] + gl + gr + [(100, 850), (100, 900)], "BLUE", 0.10)
    P.area(al + sa + [(0, 300)], "BLUE", 0.16)
    P.area([(100, 850)] + br + sb + [(100, 300)], "BLUE", 0.16)
    for cv in (gl, gr, al, br, sa, sb, [(10, 600), (80, 600)]):
        P.line(cv, "ACC", 2.2)
    P.frame([(0, "0 (A)"), (10, "10"), (25, "25"), (40, "40"), (60, "60"), (80, "80"), (100, "100 (B)")],
            [(300, "300"), (450, "450"), (600, "600"), (750, "750"), (900, "900")],
            "Composition (wt% B)", "Temperature (°C)")
    for x in (10, 40, 80):
        P.dot(x, 600, 3.6, "HEAD")
    P.text(45, 820, "γ", size=15)
    P.text(4, 520, "α", size=13)
    P.text(95, 520, "β", size=13)
    P.text(14, 690, "α + γ", size=12)
    P.text(74, 690, "γ + β", size=12)
    P.text(45, 420, "α + β", size=14)
    return c


# --------------------------------------------------------------------------- unary P-T diagram
@figure("u4-unary-pt", "Pressure-temperature diagram of a pure substance with four marked points",
        "P-T diagram of a pure substance: solid, liquid and vapour regions, the triple point and four marked points")
def unary_pt():
    c = Canvas(560, 340)
    x0, y0, x1, y1 = 70, 30, 500, 290
    line(c, (x0, y1), (x1, y1), "EDGE", 1.4)
    line(c, (x0, y0), (x0, y1), "EDGE", 1.4)
    text(c, ((x0 + x1) / 2, y1 + 30), "Temperature", "HEAD", "middle", 12.5, "700")
    text(c, (x0 + 4, y0 - 10), "Pressure", "HEAD", "start", 12.5, "700")
    tp = (230, 210)
    poly(c, [(100, 280), (160, 255), tp], "ACC", 2.2)               # sublimation
    poly(c, [tp, (250, 140), (262, 45)], "ACC", 2.2)               # melting
    poly(c, [tp, (330, 175), (420, 120), (470, 80)], "ACC", 2.2)    # vaporisation
    text(c, (140, 120), "Solid", "HEAD", "middle", 13, "700")
    text(c, (360, 90), "Liquid", "HEAD", "middle", 13, "700")
    text(c, (360, 250), "Vapour", "HEAD", "middle", 13, "700")
    for (p, lab, dx, dy) in (((330, 120), "1", 8, -4), ((250, 140), "2", 8, 4), (tp, "3", 8, 20), ((150, 220), "4", -6, 16)):
        dot(c, p, 4.5, "GREEN")
        text(c, (p[0] + dx, p[1] + dy), lab, "GREEN", "start" if dx > 0 else "end", 13, "700")
    return c


# --------------------------------------------------------------------------- option set: cooling curves
def cooling(kind):
    c = Canvas(220, 160)
    x0, y0, x1, y1 = 30, 20, 200, 130
    line(c, (x0, y1), (x1, y1), "EDGE", 1.2)
    line(c, (x0, y0), (x0, y1), "EDGE", 1.2)
    text(c, (x1, y1 + 18), "time", "TEXT", "end", 11)
    text(c, (x0 - 6, y0 + 4), "T", "TEXT", "end", 12)
    pts = {"A": [(34, 24), (80, 70), (140, 70), (196, 118)],
           "B": [(34, 22), (64, 52), (150, 82), (196, 126)],
           "C": [(34, 22), (64, 52), (110, 72), (160, 72), (196, 120)],
           "D": [(34, 24), (70, 50), (110, 50), (135, 85), (170, 85), (196, 120)]}[kind]
    poly(c, pts, "PINK", 2.2)
    text(c, (200, 34), f"Curve {kind}", "HEAD", "end", 12.5, "700")
    return c


for _k in "ABCD":
    figure(f"u4-cool-{_k.lower()}", f"Cooling curve {_k}", f"Cooling curve {_k}")(lambda k=_k: cooling(k))


# --------------------------------------------------------------------------- option set: invariant points
def invariant(kind):
    c = Canvas(230, 170)
    s = 12
    if kind == "A":          # monotectic
        line(c, (30, 95), (200, 95), "ACC", 2)
        line(c, (30, 95), (20, 160), "ACC", 2)
        poly(c, [(95, 95), (120, 50), (150, 38), (180, 50), (200, 95)], "ACC", 2)
        line(c, (30, 95), (55, 20), "ACC", 2)
        text(c, (95, 30), sub("L", "1"), "HEAD", "middle", s, "700")
        text(c, (150, 78), sub("L", "1") + " + " + sub("L", "2"), "HEAD", "middle", s - 1, "700")
        text(c, (68, 80), "α + " + sub("L", "1"), "HEAD", "middle", s - 1, "700")
        text(c, (115, 135), "α + " + sub("L", "2"), "HEAD", "middle", s - 1, "700")
    elif kind == "B":        # eutectoid
        line(c, (30, 95), (200, 95), "ACC", 2)
        poly(c, [(20, 25), (115, 95), (210, 25)], "ACC", 2)
        line(c, (30, 95), (15, 20), "ACC", 2)
        line(c, (200, 95), (215, 20), "ACC", 2)
        text(c, (115, 40), "γ", "HEAD", "middle", s + 1, "700")
        text(c, (52, 80), "α + γ", "HEAD", "middle", s - 1, "700")
        text(c, (178, 80), "γ + β", "HEAD", "middle", s - 1, "700")
        text(c, (115, 135), "α + β", "HEAD", "middle", s, "700")
    elif kind == "C":        # peritectic
        line(c, (30, 70), (200, 70), "ACC", 2)
        poly(c, [(65, 160), (110, 70), (150, 160)], "ACC", 2)
        line(c, (200, 70), (215, 15), "ACC", 2)
        line(c, (30, 70), (20, 15), "ACC", 2)
        text(c, (110, 50), "α + L", "HEAD", "middle", s, "700")
        text(c, (110, 140), "β", "HEAD", "middle", s + 1, "700")
        text(c, (50, 125), "α + β", "HEAD", "middle", s - 1, "700")
        text(c, (180, 110), "β + L", "HEAD", "middle", s - 1, "700")
        text(c, (210, 58), "L", "HEAD", "start", s, "700")
    else:                    # eutectic
        line(c, (30, 95), (200, 95), "ACC", 2)
        poly(c, [(20, 25), (115, 95), (210, 25)], "ACC", 2)
        line(c, (30, 95), (15, 20), "ACC", 2)
        line(c, (200, 95), (215, 20), "ACC", 2)
        text(c, (115, 40), "L", "HEAD", "middle", s + 1, "700")
        text(c, (52, 80), "α + L", "HEAD", "middle", s - 1, "700")
        text(c, (178, 80), "β + L", "HEAD", "middle", s - 1, "700")
        text(c, (115, 135), "α + β", "HEAD", "middle", s, "700")
    text(c, (8, 165), f"Point {kind}", "TEXT", "start", 11)
    return c


for _k in "ABCD":
    figure(f"u4-inv-{_k.lower()}", f"Invariant point {_k}", f"Invariant point {_k}")(lambda k=_k: invariant(k))


# --------------------------------------------------------------------------- option set: microstructures
GRAINS = [[(0, 0), (70, 0), (60, 55), (0, 70)], [(70, 0), (160, 0), (160, 50), (110, 75), (60, 55)],
          [(0, 70), (60, 55), (110, 75), (90, 160), (0, 160)], [(110, 75), (160, 50), (160, 160), (90, 160)]]


def lamellae(c, poly_pts, ox, oy, angle, uid, gap=6):
    pts = " ".join(f"{ox + x:.1f},{oy + y:.1f}" for x, y in poly_pts)
    c.add(f'<clipPath id="cl-{uid}"><polygon points="{pts}"/></clipPath><g clip-path="url(#cl-{uid})">')
    dx, dy = math.cos(angle), math.sin(angle)
    for k in range(-30, 31):
        px, py = ox + 80 + k * gap * -dy, oy + 80 + k * gap * dx
        line(c, (px - 200 * dx, py - 200 * dy), (px + 200 * dx, py + 200 * dy), "HEAD", 1.1)
    c.add("</g>")


def micro_pic(kind):
    c = Canvas(200, 200)
    ox, oy = 20, 15
    if kind == "A":          # lamellar only
        for i, g in enumerate(GRAINS):
            lamellae(c, g, ox, oy, 0.4 + 0.9 * i, f"mA{i}")
    elif kind == "B":        # primary grains in a lamellar matrix
        blobs = ((35, 35, 20), (110, 30, 17), (70, 90, 22), (130, 115, 18), (30, 125, 15))
        holes = "".join(f'<circle cx="{ox + x}" cy="{oy + y}" r="{r}" fill="black"/>' for x, y, r in blobs)
        c.add(f'<mask id="mask-mB"><rect x="{ox}" y="{oy}" width="160" height="160" fill="white"/>{holes}</mask>')
        c.add('<g mask="url(#mask-mB)">')
        lamellae(c, [(0, 0), (160, 0), (160, 160), (0, 160)], ox, oy, 0.7, "mB")
        c.add("</g>")
        for (x, y, r) in blobs:
            circle(c, (ox + x, oy + y), r, "HEAD", 1.4, fill="BLUE", opacity=0.18)
    elif kind == "C":        # single-phase grains
        for g in GRAINS:
            poly(c, [(ox + x, oy + y) for x, y in g], "HEAD", 1.4, fill="BLUE", opacity=0.10, close=True)
    else:                    # grains with small particles inside and at the boundaries
        for g in GRAINS:
            poly(c, [(ox + x, oy + y) for x, y in g], "HEAD", 1.4, fill="BLUE", opacity=0.10, close=True)
        for (x, y) in ((60, 55), (110, 75), (70, 2), (2, 70), (35, 62), (85, 65), (135, 62), (100, 118), (30, 30),
                       (120, 30), (45, 115), (135, 130), (85, 40), (20, 100)):
            dot(c, (ox + x, oy + y), 2.8, "HEAD")
    rect(c, ox, oy, 160, 160, "HEAD", 1.6)
    text(c, (ox, oy + 180), f"Structure {kind}", "TEXT", "start", 11)
    return c


for _k in "ABCD":
    figure(f"u4-mic-{_k.lower()}", f"Microstructure {_k}", f"Structure {_k}")(lambda k=_k: micro_pic(k))


# --------------------------------------------------------------------------- option set: slowly cooled steels
def steel_pic(kind):
    c = Canvas(200, 200)
    ox, oy = 20, 15
    for i, g in enumerate(GRAINS):
        pts = [(ox + x, oy + y) for x, y in g]
        if kind == "A" or (kind == "C") or (kind == "B" and i in (1, 2)):
            lamellae(c, g, ox, oy, 0.5 + 1.1 * i, f"s{kind}{i}", gap=5)
        else:
            poly(c, pts, "HEAD", 1.0, fill="BLUE", opacity=0.08, close=True)
        poly(c, pts, "HEAD", 3.6 if kind == "C" else 1.2, close=True)
    rect(c, ox, oy, 160, 160, "HEAD", 1.6)
    text(c, (ox, oy + 180), f"Structure {kind}", "TEXT", "start", 11)
    return c


for _k in "ABCD":
    figure(f"u4-steel-{_k.lower()}", f"Steel microstructure {_k}", f"Structure {_k}")(lambda k=_k: steel_pic(k))
