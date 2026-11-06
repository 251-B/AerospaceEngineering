"""Topic 6 figures for Aerospace Materials I: electrical properties (Session 13).

Schematic redraws of the slides (labels and qualitative shape kept, not to scale) plus PNG crops of the slides
for the charts and tables whose values cannot be redrawn faithfully (registered with `REG.raster`).
The figures of the solved problems live in tools/figures/materials_t6_problems.py and are added to the same
registry by `build()`. Run `python tools/build_topic_pages.py` (theory) or `python tools/build_materials_problems.py`
(problems) to write the SVG files to vault/attachments/T6.
"""
import importlib.util
import math

from figures.svgkit import (Canvas, Registry, arrow, circle, dim, dot, hatch, line, pathd, poly, rect, sub, text)

REG = Registry("T6")


# ---------------------------------------------------------------- small helpers

def sup(base, s):
    return sub(base, s, True)


def txt(c, x, y, s, col="TEXT", anchor="middle", size=13, weight="400"):
    text(c, (x, y), s, col, anchor, size, weight)


def axes(c, o, xend, yend, xl=None, yl=None, xdy=24):
    """Thin axes from the origin o to (xend, o.y) and (o.x, yend), with arrow heads and bold end labels."""
    line(c, o, (xend, o[1]), "EDGE", 1.3, head=True)
    line(c, o, (o[0], yend), "EDGE", 1.3, head=True)
    if xl:
        text(c, (xend, o[1] + xdy), xl, "HEAD", "end", 13, "700")
    if yl:
        text(c, (o[0] + 8, yend + 4), yl, "HEAD", "start", 13, "700")


def band(c, x, y, w, h, col, op=0.30):
    rect(c, x, y, w, h, col, 1.5, None, col, op)


def electrons(c, x, y, w, h, nx, ny, r=3, col="HEAD"):
    """A grid of small filled circles (electrons) inside a band."""
    for i in range(nx):
        for j in range(ny):
            dot(c, (x + (i + 0.5) * w / nx, y + (j + 0.5) * h / ny), r, col, col)


def wave(c, a, b, amp=6, n=5, col="ACC", w=2.0):
    """Wavy line (a photon) from a to b ending with an arrow head."""
    L = math.hypot(b[0] - a[0], b[1] - a[1])
    ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
    nx, ny = -uy, ux
    pts = []
    for i in range(0, 81):
        t = i / 80
        d = amp * math.sin(2 * math.pi * n * t)
        pts.append((a[0] + ux * L * t + nx * d, a[1] + uy * L * t + ny * d))
    poly(c, pts, col, w)
    from figures.svgkit import arrow_head
    arrow_head(c, (b[0] - ux * 8, b[1] - uy * 8), b, col, 10)


def battery(c, x, y, h=26):
    """Battery symbol drawn on a vertical wire at x, centre y: long plate on top (+), short plate below (-)."""
    line(c, (x - 12, y - 4), (x + 12, y - 4), "HEAD", 2.4)
    line(c, (x - 6, y + 4), (x + 6, y + 4), "HEAD", 2.4)
    txt(c, x - 18, y - 6, "+", "TEXT", "end", 12)
    txt(c, x - 18, y + 12, "−", "TEXT", "end", 12)


def atom_grid(c, x0, y0, nx, ny, d, r=9, col="HEAD", op=0.45, skip=(), offs=None):
    """Grid of atoms; returns the list of centres (None for skipped ones)."""
    pts = {}
    for j in range(ny):
        for i in range(nx):
            x, y = x0 + i * d, y0 + j * d
            if offs and (i, j) in offs:
                x, y = x + offs[(i, j)][0], y + offs[(i, j)][1]
            pts[(i, j)] = (x, y)
            if (i, j) in skip:
                circle(c, (x, y), r, "EDGE", 1.2, "3,3")
            else:
                circle(c, (x, y), r, col, 1.4, None, col, op)
    return pts


# ---------------------------------------------------------------- bands of solids (S3-S8)

def band_formation():
    c = Canvas(640, 350)
    txt(c, 24, 24, "Electron energy", "HEAD", "start", 13, "700")
    line(c, (38, 300), (38, 36), "EDGE", 1.3, head=True)
    cols = [100, 215, 330, 500]
    names = ["One atom", "Two atoms", "Few atoms", "Large number (solid)"]
    ups, lows = 105, 205
    # guides
    for yv in (ups, lows):
        for a, b in ((cols[0] + 20, cols[1] - 22), (cols[1] + 22, cols[2] - 34), (cols[2] + 34, cols[3] - 50)):
            line(c, (a, yv), (b, yv), "EDGE", 1.0, "3,4")
    for yv in (ups, lows):
        line(c, (cols[0] - 20, yv), (cols[0] + 20, yv), "HEAD", 2.2)
        for dy in (-9, 9):
            line(c, (cols[1] - 20, yv + dy), (cols[1] + 20, yv + dy), "HEAD", 2.0)
        for k in range(6):
            line(c, (cols[2] - 30, yv - 15 + 6 * k), (cols[2] + 30, yv - 15 + 6 * k), "HEAD", 1.6)
        band(c, cols[3] - 50, yv - 26, 100, 52, "ACC", 0.35)
    for x in cols[:3]:
        line(c, (x - 20 - (10 if x == cols[2] else 0), 290), (x + 20 + (10 if x == cols[2] else 0), 290), "TEXT", 2.0)
    line(c, (cols[3] - 50, 290), (cols[3] + 50, 290), "TEXT", 2.0)
    dim(c, (cols[3] + 70, ups + 26), (cols[3] + 70, lows - 26), "", "TEXT")
    txt(c, cols[3] + 80, 160, sub("E", "g"), "HEAD", "start", 15, "700")
    txt(c, cols[3] + 80, 178, "band gap", "TEXT", "start", 12)
    txt(c, 38 + 8, 313, "core-level electrons", "TEXT", "start", 12)
    for x, n in zip(cols, names):
        txt(c, x, 336, n, "HEAD", "middle", 12, "700")
    REG.put("band-formation", c, "Formation of energy bands",
            "Atomic energy levels split as atoms approach each other: two atoms give two levels, many atoms give a quasi-continuous band, and a gap Eg remains between bands (schematic, not to scale)")


def bands_vs_spacing():
    c = Canvas(640, 330)
    o = (70, 290)
    axes(c, o, 600, 20, "Inter-atomic distance", "Energy")

    def edges(xp, yc, wmax, f0=520, span=380):
        f = max(0.0, (f0 - xp) / span) ** 1.5
        w = wmax * f + 2
        return yc - w / 2, yc + w / 2

    xs = list(range(140, 521, 4))
    for yc, wm, col in ((95, 100, "GREEN"), (190, 100, "BLUE")):
        top = [(x, edges(x, yc, wm)[0]) for x in xs]
        bot = [(x, edges(x, yc, wm)[1]) for x in reversed(xs)]
        poly(c, top + bot, col, 1.6, None, col, True, 0.35)
    line(c, (300, 30), (300, 288), "ACC", 1.5, "6,4")
    txt(c, 300, 22, "Equilibrium inter-atomic distance", "ACC", "middle", 12, "700")
    t1, b1 = edges(300, 95, 100)[1], edges(300, 190, 100)[0]
    dim(c, (330, t1), (330, b1), "", "TEXT")
    txt(c, 340, (t1 + b1) / 2 + 5, sub("E", "g"), "HEAD", "start", 15, "700")
    txt(c, 540, 78, "Conduction band", "GREEN", "start", 13, "700")
    txt(c, 540, 205, "Valence band", "BLUE", "start", 13, "700")
    txt(c, 540, 130, "Band gap", "TEXT", "start", 12)
    REG.put("bands-vs-spacing", c, "Energy bands against the inter-atomic distance",
            "The bands widen as the inter-atomic distance decreases; at the equilibrium distance the valence and conduction bands are separated by the band gap Eg (schematic, not to scale)")


def band_types():
    c = Canvas(700, 340)
    arrow(c, (14, 260), (14, 40), "EDGE", 1.4, 9)
    txt(c, 14, 28, "E", "HEAD", "middle", 13, "700")
    x0 = [40, 215, 390, 560]
    titles = ["Metal", "Metal", "Semiconductor", "Insulator"]
    for x, t in zip(x0, titles):
        txt(c, x + 60, 28, t, "HEAD", "middle", 13, "700")
    # A: half filled
    x = x0[0]
    band(c, x, 70, 120, 90, "GREEN", 0.12)
    band(c, x, 160, 120, 90, "ATOM", 0.45)
    line(c, (x - 6, 160), (x + 126, 160), "HEAD", 1.4, "5,3")
    txt(c, x + 132, 164, sub("E", "f"), "HEAD", "start", 13, "700")
    txt(c, x + 60, 120, "empty states", "TEXT", "middle", 11)
    txt(c, x + 60, 210, "filled states", "TEXT", "middle", 11)
    txt(c, x + 60, 275, "Half-filled band", "TEXT", "middle", 12)
    txt(c, x + 60, 293, "(Na, Al, Cu)", "TEXT", "middle", 12)
    # B: overlap
    x = x0[1]
    band(c, x, 140, 120, 110, "ATOM", 0.45)
    band(c, x, 70, 120, 95, "GREEN", 0.18)
    line(c, (x - 6, 152), (x + 126, 152), "HEAD", 1.4, "5,3")
    txt(c, x + 132, 156, sub("E", "f"), "HEAD", "start", 13, "700")
    txt(c, x + 60, 110, "empty 3p", "TEXT", "middle", 11)
    txt(c, x + 60, 215, "filled 3s", "TEXT", "middle", 11)
    txt(c, x + 60, 275, "Overlapping bands", "TEXT", "middle", 12)
    txt(c, x + 60, 293, "(Mg)", "TEXT", "middle", 12)
    # C: semiconductor
    x = x0[2]
    band(c, x, 50, 120, 80, "GREEN", 0.25)
    band(c, x, 170, 120, 80, "ATOM", 0.45)
    dim(c, (x + 60, 132), (x + 60, 168), "", "TEXT")
    txt(c, x + 68, 154, sub("E", "g") + " < 2 eV", "HEAD", "start", 12, "700")
    txt(c, x + 60, 90, "conduction band", "TEXT", "middle", 11)
    txt(c, x + 60, 215, "valence band", "TEXT", "middle", 11)
    txt(c, x + 60, 275, "Si: 1.1 eV", "TEXT", "middle", 12)
    txt(c, x + 60, 293, "Ge: 0.67 eV", "TEXT", "middle", 12)
    # D: insulator
    x = x0[3]
    band(c, x, 50, 120, 50, "GREEN", 0.25)
    band(c, x, 200, 120, 50, "ATOM", 0.45)
    dim(c, (x + 60, 102), (x + 60, 198), "", "TEXT")
    txt(c, x + 68, 154, sub("E", "g") + " > 2 eV", "HEAD", "start", 12, "700")
    txt(c, x + 60, 80, "conduction band", "TEXT", "middle", 11)
    txt(c, x + 60, 230, "valence band", "TEXT", "middle", 11)
    txt(c, x + 60, 275, "Diamond:", "TEXT", "middle", 12)
    txt(c, x + 60, 293, "6-7 eV", "TEXT", "middle", 12)
    REG.put("band-types", c, "Band structure of metals, semiconductors and insulators",
            "Band structure of conductors (half-filled band, overlapping bands), semiconductors (narrow gap) and insulators (wide gap) (schematic, not to scale)")


def conductivity_scale():
    c = Canvas(700, 260)
    x0, k = 40, 21.0

    def X(e):
        return x0 + (e + 20) * k
    for e in range(-20, 9, 4):
        line(c, (X(e), 212), (X(e), 218), "EDGE", 1.1)
        txt(c, X(e), 234, sup("10", "−" + str(-e)) if e < 0 else (sup("10", str(e)) if e else "1"), "TEXT", "middle", 12)
    line(c, (x0 - 10, 212), (X(9), 212), "EDGE", 1.3, head=True)
    txt(c, X(9) + 4, 250, "σ in (Ω·m)" + "⁻¹" + " (logarithmic scale)", "HEAD", "end", 12, "700")
    rows = [(-20, -10, 66, "ATOM"), (-6, 4, 116, "GREEN"), (6.5, 7.5, 166, "PINK")]
    for a, b, y, col in rows:
        rect(c, X(a), y, X(b) - X(a), 28, col, 1.5, None, col, 0.35)
    txt(c, X(-10) + 10, 85, "Insulators: 10⁻²⁰ to 10⁻¹⁰, e.g. polyethylene", "HEAD", "start", 13, "700")
    txt(c, X(-6) - 10, 135, "Semiconductors: 10⁻⁶ to 10⁴, e.g. Si, Ge", "HEAD", "end", 13, "700")
    txt(c, X(6.5) - 10, 185, "Conductors: about 10⁷, e.g. metals", "HEAD", "end", 13, "700")
    REG.put("conductivity-scale", c, "Classification of materials by electrical conductivity",
            "Insulators, semiconductors and conductors on a logarithmic conductivity scale, with the ranges printed on the slide (schematic, not to scale)")


# ---------------------------------------------------------------- metallic conductors (S10-S17)

def electron_drift():
    c = Canvas(680, 310)
    # left: path
    txt(c, 160, 24, "Electron path under a field E", "HEAD", "middle", 13, "700")
    arrow(c, (260, 52), (60, 52), "GREEN", 2.4, 11)
    txt(c, 160, 44, "E", "GREEN", "middle", 15, "700")
    pts = [(40, 200), (90, 130), (125, 205), (185, 105), (215, 210), (270, 150), (300, 195)]
    poly(c, pts, "BLUE", 1.8)
    for p_ in pts[1:-1]:
        dot(c, p_, 5, "ACC", "ACC")
    dot(c, pts[0], 5, "BLUE", "BLUE")
    txt(c, 150, 235, "scattering events", "ACC", "middle", 12)
    arrow(c, (50, 268), (290, 268), "PINK", 2.2, 10)
    txt(c, 170, 290, "net electron motion", "PINK", "middle", 12)
    # right: v(t)
    o = (400, 250)
    axes(c, o, 650, 40, "Time", "Drift velocity")
    t = 80
    for i in range(3):
        a, b = (o[0] + 20 + i * t, o[1]), (o[0] + 20 + (i + 1) * t, 100)
        poly(c, [a, b], "PINK", 2.4)
        if i < 2:
            poly(c, [b, (b[0], o[1])], "PINK", 1.4, "3,3")
    line(c, (o[0], 100), (o[0] + 270, 100), "EDGE", 1.1, "5,4")
    line(c, (o[0], 175), (o[0] + 270, 175), "EDGE", 1.1, "5,4")
    txt(c, o[0] - 6, 104, sub("v", "max"), "TEXT", "end", 12)
    txt(c, o[0] - 6, 179, sub("v", "av"), "TEXT", "end", 12)
    dim(c, (o[0] + 20, o[1] + 22), (o[0] + 100, o[1] + 22), "2τ", "TEXT", (0, 18))
    txt(c, o[0] + 120, 92, "collisions", "ACC", "start", 12)
    REG.put("electron-drift", c, "Free electron in a metal under an electric field",
            "Left: path of a conduction electron with scattering events under a field E. Right: drift velocity against time, which restarts after each collision (classical model, schematic)")


def ohm_geometry():
    c = Canvas(640, 310)
    rect(c, 150, 110, 300, 80, "HEAD", 1.8, None, "ATOM", 0.18)
    c.add('<ellipse cx="450" cy="150" rx="16" ry="40" fill="none" stroke="HEAD" stroke-width="1.8"/>')
    arrow(c, (60, 150), (146, 150), "BLUE", 2.4, 11)
    arrow(c, (466, 150), (560, 150), "BLUE", 2.4, 11)
    txt(c, 100, 140, "I", "BLUE", "middle", 15, "700")
    txt(c, 520, 140, "I", "BLUE", "middle", 15, "700")
    arrow(c, (175, 132), (400, 132), "GREEN", 2.2, 10)
    txt(c, 288, 125, "E", "GREEN", "middle", 14, "700")
    arrow(c, (175, 170), (400, 170), "PINK", 2.2, 10)
    txt(c, 288, 187, "J", "PINK", "middle", 14, "700")
    dim(c, (150, 80), (450, 80), "V = E l", "TEXT", (0, -8))
    dim(c, (150, 222), (450, 222), "l", "TEXT", (0, 18))
    txt(c, 490, 106, "A", "HEAD", "start", 14, "700")
    line(c, (486, 110), (466, 128), "EDGE", 1.0)
    txt(c, 320, 264, "J = σ E,   σ = 1/ρ,   R = V / I = ρ l / A", "HEAD", "middle", 14, "700")
    txt(c, 320, 286, "(I = J A and V = E l give R = l / (σ A))", "TEXT", "middle", 12)
    REG.put("ohm-geometry", c, "Ohm's law and the geometry of a conductor",
            "A bar of length l and cross-section A carries a current I under a voltage V: E = V/l, J = I/A, so the resistance is R = ρ l / A (schematic)")


def matthiessen():
    c = Canvas(640, 320)
    o = (70, 270)
    axes(c, o, 600, 30, "Temperature (K)", "Electrical resistivity", 30)
    base = 215

    def rho(x):
        t = (x - o[0]) / 430
        return 190 * t * t / (t + 0.35)
    pts = [(x, o[1] - 55 - rho(x)) for x in range(70, 501, 6)]
    poly(c, pts, "PINK", 2.6)
    line(c, (70, base), (520, base), "EDGE", 1.4, "7,4")
    ya, yb = o[1] - 55 - rho(480), base
    arrow(c, (480, base), (480, ya), "BLUE", 1.6, 9)
    arrow(c, (480, ya), (480, base), "BLUE", 1.6, 9)
    arrow(c, (480, o[1]), (480, base), "GREEN", 1.6, 9)
    arrow(c, (480, base), (480, o[1]), "GREEN", 1.6, 9)
    txt(c, 492, (ya + base) / 2 + 4, sub("ρ", "T"), "BLUE", "start", 15, "700")
    txt(c, 540, (ya + base) / 2 - 8, "temperature", "BLUE", "start", 12)
    txt(c, 540, (ya + base) / 2 + 8, "component", "BLUE", "start", 12)
    txt(c, 492, (base + o[1]) / 2 + 4, sub("ρ", "r"), "GREEN", "start", 15, "700")
    txt(c, 520, (base + o[1]) / 2 + 22, "residual component", "GREEN", "start", 12)
    txt(c, 90, 56, sub("ρ", "total") + " = " + sub("ρ", "T") + " + " + sub("ρ", "r"), "HEAD", "start", 16, "700")
    REG.put("matthiessen", c, "Matthiessen's law",
            "Resistivity of a metal against temperature: a temperature-dependent part ρT on top of a temperature-independent residual part ρr (schematic, not to scale)")


def scattering_sources():
    c = Canvas(720, 290)
    xs = [10, 250, 490]
    titles = ["Perfect crystal", "Crystal at high temperature", "Crystal with atomic defects"]
    notes = ["no scattering", "thermal scattering, " + sub("ρ", "T"), "defect scattering, " + sub("ρ", "r")]
    vib = {(1, 0): (4, 5), (2, 1): (-5, 4), (3, 0): (5, -5), (0, 1): (-4, -5), (1, 2): (5, 4), (3, 2): (-5, 5),
           (2, 3): (4, -5), (4, 1): (-4, 6), (0, 3): (5, 4), (4, 3): (-6, -4), (2, 0): (-5, -4), (1, 3): (-4, 5)}
    for k, x0 in enumerate(xs):
        txt(c, x0 + 105, 26, titles[k], "HEAD", "middle", 13, "700")
        if k == 0:
            g = atom_grid(c, x0 + 22, 62, 5, 4, 42, 11, "HEAD", 0.40)
            arrow(c, (x0 + 4, 125), (x0 + 206, 125), "BLUE", 2.2, 10)
        elif k == 1:
            g = atom_grid(c, x0 + 22, 62, 5, 4, 42, 11, "HEAD", 0.40, offs=vib)
            poly(c, [(x0 + 4, 125), (x0 + 50, 100), (x0 + 72, 152), (x0 + 120, 101), (x0 + 150, 150), (x0 + 206, 112)], "BLUE", 2.0)
            arrow_pts = (x0 + 190, 118), (x0 + 206, 112)
            arrow(c, arrow_pts[0], arrow_pts[1], "BLUE", 2.0, 9)
        else:
            g = atom_grid(c, x0 + 22, 62, 5, 4, 42, 11, "HEAD", 0.40, skip={(1, 1)})
            circle(c, (x0 + 22 + 3 * 42, 62 + 2 * 42), 11, "PINK", 1.6, None, "PINK", 0.45)
            circle(c, (x0 + 22 + 2.5 * 42, 62 + 0.5 * 42), 4, "ACC", 1.4, None, "ACC", 0.9)
            poly(c, [(x0 + 4, 125), (x0 + 30, 125), (x0 + 63, 104), (x0 + 100, 134), (x0 + 132, 128), (x0 + 160, 150), (x0 + 206, 118)], "BLUE", 2.0)
            arrow(c, (x0 + 190, 124), (x0 + 206, 118), "BLUE", 2.0, 9)
            txt(c, x0 + 105, 226, "dashed circle: vacancy", "TEXT", "middle", 11)
            txt(c, x0 + 105, 240, "pink: impurity atom", "PINK", "middle", 11)
            txt(c, x0 + 105, 254, "orange dot: interstitial atom", "ACC", "middle", 11)
        txt(c, x0 + 105, 276, notes[k], "TEXT", "middle", 12)
    REG.put("scattering-sources", c, "Scattering of conduction electrons",
            "Electron path through a perfect crystal, a crystal at high temperature (vibrating atoms) and a crystal with atomic-scale defects; scattering reduces the mobility and the conductivity (schematic)")


# ---------------------------------------------------------------- non-metallic conductors (S21-S22)

def graphene_lattice():
    c = Canvas(560, 345)
    s = 30.0
    edges = set()
    verts = set()
    for col in range(5):
        for row in range(4):
            cx = 70 + col * 1.5 * s * 1.0
            cy = 90 + row * math.sqrt(3) * s + (math.sqrt(3) * s / 2 if col % 2 else 0)
            pts = [(cx + s * math.cos(math.radians(60 * k)), cy + s * math.sin(math.radians(60 * k))) for k in range(6)]
            for k in range(6):
                a, b = pts[k], pts[(k + 1) % 6]
                key = tuple(sorted(((round(a[0]), round(a[1])), (round(b[0]), round(b[1])))))
                edges.add(key)
            for q in pts:
                verts.add((round(q[0]), round(q[1])))
    rect(c, 40, 52, 330, 272, "GREEN", 1.2, "5,4", "GREEN", 0.10, 18)
    for a, b in edges:
        line(c, a, b, "HEAD", 2.0)
    for v in verts:
        dot(c, v, 4, "ATOM", "ATOM")
    txt(c, 205, 38, "Single layer, hexagonal lattice: one carbon atom at each vertex", "HEAD", "middle", 13, "700")
    txt(c, 385, 120, "Delocalised π", "GREEN", "start", 13, "700")
    txt(c, 385, 138, "electron cloud above", "GREEN", "start", 12)
    txt(c, 385, 154, "and below the plane", "GREEN", "start", 12)
    txt(c, 385, 190, "Electrons move over the", "TEXT", "start", 12)
    txt(c, 385, 206, "whole surface at about", "TEXT", "start", 12)
    txt(c, 385, 222, "1000 km/s", "TEXT", "start", 12)
    REG.put("graphene-lattice", c, "Graphene lattice",
            "Graphene: a single layer of carbon atoms on a hexagonal lattice, with a π cloud of delocalised electrons (schematic)")


def ionic_conduction():
    c = Canvas(700, 290)
    txt(c, 170, 26, "Movement of ions through vacancies", "HEAD", "middle", 13, "700")
    g = atom_grid(c, 60, 60, 5, 4, 46, 12, "HEAD", 0.45, skip={(2, 1)})
    arrow(c, (g[(3, 1)][0] - 14, g[(3, 1)][1]), (g[(2, 1)][0] + 12, g[(2, 1)][1]), "ACC", 2.4, 10)
    txt(c, 170, 236, "dashed circle: vacancy", "TEXT", "middle", 12)
    txt(c, 170, 264, "an ion jumps into the vacancy, the vacancy moves the other way", "TEXT", "middle", 11)
    txt(c, 530, 26, "Interstitial cations", "HEAD", "middle", 13, "700")
    g2 = atom_grid(c, 420, 60, 5, 4, 46, 12, "HEAD", 0.45)
    p1 = (g2[(1, 1)][0] + 23, g2[(1, 1)][1] + 23)
    p2 = (g2[(2, 1)][0] + 23, g2[(2, 1)][1] + 23)
    p3 = (g2[(3, 1)][0] + 23, g2[(3, 1)][1] + 23)
    for p_ in (p2, p3):
        circle(c, p_, 6, "EDGE", 1.0, "2,3")
    dot(c, p1, 5, "PINK", "PINK")
    arrow(c, (p1[0] + 8, p1[1]), (p2[0] - 9, p2[1]), "ACC", 2.4, 10)
    arrow(c, (p2[0] + 8, p2[1]), (p3[0] - 9, p3[1]), "ACC", 2.4, 10)
    txt(c, 530, 236, "pink: interstitial cation, " + sub("r", "i") + " < " + sub("r", "atom"), "PINK", "middle", 12)
    txt(c, 530, 264, "a small cation moves through the interstitial voids", "TEXT", "middle", 11)
    REG.put("ionic-conduction", c, "Ionic conduction in ceramics",
            "Ionic conduction: an ion hops into a neighbouring vacancy (left), or a small interstitial cation moves through the interstitial voids (right) (schematic)")


# ---------------------------------------------------------------- semiconductors (S27-S44)

def intrinsic_excitation():
    c = Canvas(700, 330)
    arrow(c, (36, 296), (36, 36), "EDGE", 1.4, 9)
    txt(c, 36, 26, "Energy", "HEAD", "middle", 13, "700")
    txt(c, 160, 30, "Before excitation", "HEAD", "middle", 13, "700")
    txt(c, 470, 30, "After excitation", "HEAD", "middle", 13, "700")
    for x in (70, 380):
        band(c, x, 50, 180, 70, "GREEN", 0.10)
        band(c, x, 210, 180, 80, "ATOM", 0.30)
        txt(c, x + 55, 90, "conduction band", "TEXT", "middle", 11)
    electrons(c, 70, 210, 180, 80, 9, 4)
    electrons(c, 380, 210, 180, 80, 9, 4)
    # hole at (500, 250): remove one electron by drawing an open circle
    circle(c, (500, 250), 6, "PINK", 2.0)
    dot(c, (500, 85), 5, "BLUE", "BLUE")
    arrow(c, (500, 240), (500, 94), "ACC", 2.0, 10)
    dim(c, (160, 122), (160, 208), "", "TEXT")
    txt(c, 170, 170, sub("E", "g"), "HEAD", "start", 15, "700")
    txt(c, 512, 176, "thermal or electrical", "ACC", "start", 11)
    txt(c, 512, 191, "excitation, E ≥ " + sub("E", "g"), "ACC", "start", 11)
    txt(c, 572, 88, "free electron", "BLUE", "start", 12, "700")
    txt(c, 572, 254, "hole in the", "PINK", "start", 12, "700")
    txt(c, 572, 269, "valence band", "PINK", "start", 12, "700")
    txt(c, 160, 312, "valence band, full", "TEXT", "middle", 11)
    REG.put("intrinsic-excitation", c, "Excitation of an electron in an intrinsic semiconductor",
            "Intrinsic semiconductor: an electron excited across the gap leaves a hole in the valence band, giving two types of charge carrier (schematic, not to scale)")


def intrinsic_arrhenius():
    c = Canvas(560, 320)
    o = (70, 270)
    axes(c, o, 540, 30, "1/T", "ln σ")
    a, b = (110, 80), (500, 232)
    line(c, a, b, "PINK", 2.8)
    p1, p2 = (200, 80 + (200 - 110) * 0.4), (400, 80 + (400 - 110) * 0.4)
    line(c, p1, (p2[0], p1[1]), "EDGE", 1.2, "5,4")
    line(c, (p2[0], p1[1]), p2, "EDGE", 1.2, "5,4")
    dot(c, p1, 4, "PINK", "PINK")
    dot(c, p2, 4, "PINK", "PINK")
    txt(c, 300, p1[1] - 8, "Δ(1/T)", "TEXT", "middle", 12)
    txt(c, p2[0] + 10, (p1[1] + p2[1]) / 2 + 4, "Δ ln σ", "TEXT", "start", 12)
    txt(c, 190, 205, "slope = −" + sub("E", "g") + " / 2k", "PINK", "middle", 14, "700")
    txt(c, 100, 52, "ln σ = ln " + sub("σ", "0") + " − " + sub("E", "g") + " / (2kT)", "HEAD", "start", 15, "700")
    txt(c, 110, 292, "high T", "TEXT", "middle", 12)
    txt(c, 500, 292, "low T", "TEXT", "middle", 12)
    REG.put("intrinsic-arrhenius", c, "Arrhenius plot of an intrinsic semiconductor",
            "ln σ against 1/T is a straight line of slope −Eg/2k for an intrinsic semiconductor (schematic, not to scale)")


def compound_trend():
    c = Canvas(700, 300)
    rect(c, 30, 60, 210, 46, "HEAD", 1.6, None, "ATOM", 0.25, 6)
    txt(c, 135, 88, "Si    " + sub("E", "g") + " = 1.1 eV", "HEAD", "middle", 14, "700")
    arrow(c, (135, 112), (135, 158), "ACC", 2.4, 11)
    txt(c, 148, 140, "atom size increases", "ACC", "start", 12)
    rect(c, 30, 164, 210, 46, "HEAD", 1.6, None, "ATOM", 0.25, 6)
    txt(c, 135, 192, "Ge    " + sub("E", "g") + " = 0.67 eV", "HEAD", "middle", 14, "700")
    txt(c, 135, 236, sub("E", "g") + " decreases, σ increases", "TEXT", "middle", 12)
    txt(c, 135, 42, "Group 14, covalent bonds", "HEAD", "middle", 13, "700")
    # right
    arrow(c, (500, 78), (300, 78), "GREEN", 3.0, 12)
    arrow(c, (500, 78), (680, 78), "PINK", 3.0, 12)
    txt(c, 300, 66, "more covalent", "GREEN", "start", 13, "700")
    txt(c, 680, 66, "more ionic", "PINK", "end", 13, "700")
    for x, l1, l2 in ((300, "Group 14", "Si, Ge"), (430, "Groups 13-15", "GaAs, InSb"), (560, "Groups 12-16", "CdS, ZnTe")):
        rect(c, x, 100, 120, 52, "HEAD", 1.5, None, "ATOM", 0.18, 6)
        txt(c, x + 60, 122, l1, "TEXT", "middle", 12)
        txt(c, x + 60, 141, l2, "HEAD", "middle", 13, "700")
    arrow(c, (300, 196), (680, 196), "BLUE", 2.4, 11)
    txt(c, 490, 186, sub("E", "g") + " increases", "BLUE", "middle", 13, "700")
    arrow(c, (300, 250), (680, 250), "PINK", 2.4, 11)
    txt(c, 490, 240, "σ decreases (intrinsic semiconductors)", "PINK", "middle", 13, "700")
    REG.put("compound-trend", c, "Band gap trends in intrinsic semiconductors",
            "Trends of the band gap: it falls as the atom size grows in group 14 and rises as the bonding becomes less covalent and more ionic; the conductivity follows the opposite trend (schematic)")


def _si_cell(c, cx, cy, d, dopant, label, hole=False):
    """3x3 block of Si atoms (bonds drawn) with the dopant at the centre."""
    pts = {}
    for i in range(3):
        for j in range(3):
            pts[(i, j)] = (cx + (i - 1) * d, cy + (j - 1) * d)
    for i in range(3):
        for j in range(3):
            if i < 2:
                line(c, pts[(i, j)], pts[(i + 1, j)], "EDGE", 1.6)
            if j < 2:
                line(c, pts[(i, j)], pts[(i, j + 1)], "EDGE", 1.6)
    for k, p_ in pts.items():
        if k == (1, 1):
            circle(c, p_, 17, "ACC", 2.0, None, "ACC", 0.45)
            txt(c, p_[0], p_[1] + 5, dopant, "HEAD", "middle", 14, "700")
        else:
            circle(c, p_, 17, "HEAD", 1.6, None, "ATOM", 0.30)
            txt(c, p_[0], p_[1] + 5, "Si", "HEAD", "middle", 13)
    return pts


def donor_level():
    c = Canvas(720, 340)
    arrow(c, (30, 300), (30, 30), "EDGE", 1.4, 9)
    txt(c, 30, 22, "Energy", "HEAD", "middle", 13, "700")
    band(c, 60, 40, 200, 50, "GREEN", 0.22)
    band(c, 60, 230, 200, 50, "ATOM", 0.30)
    line(c, (60, 112), (260, 112), "ACC", 2.0, "6,4")
    dot(c, (160, 112), 4.5, "BLUE", "BLUE")
    arrow(c, (160, 104), (160, 84), "BLUE", 1.8, 8)
    txt(c, 272, 94, sub("E", "c"), "HEAD", "start", 13, "700")
    txt(c, 272, 117, sub("E", "d"), "ACC", "start", 13, "700")
    txt(c, 272, 232, sub("E", "v"), "HEAD", "start", 13, "700")
    dim(c, (90, 90), (90, 230), "", "TEXT")
    txt(c, 98, 165, sub("E", "g"), "HEAD", "start", 14, "700")
    txt(c, 170, 130, "donor level", "ACC", "start", 11)
    txt(c, 170, 70, "conduction band", "TEXT", "start", 11)
    txt(c, 160, 258, "valence band", "TEXT", "middle", 11)
    txt(c, 160, 308, "ΔE = " + sub("E", "c") + " − " + sub("E", "d") + " (small)", "BLUE", "middle", 12, "700")
    pts = _si_cell(c, 500, 150, 62, "P", "P")
    p_ = pts[(1, 1)]
    circle(c, p_, 33, "BLUE", 1.2, "3,3")
    dot(c, (p_[0] + 23, p_[1] - 23), 4.5, "BLUE", "BLUE")
    txt(c, 500, 262, "Si: 4 valence electrons", "TEXT", "middle", 12)
    txt(c, 500, 280, "P: 5 valence electrons, one is free", "BLUE", "middle", 12, "700")
    txt(c, 500, 24, "n-type: donor impurity (P)", "HEAD", "middle", 13, "700")
    REG.put("donor-level", c, "Donor level in an n-type semiconductor",
            "n-type semiconductor: a P atom (5 valence electrons) in Si gives an extra electron in a donor level Ed just below the conduction band, so little energy is needed to free it (schematic, not to scale)")


def acceptor_level():
    c = Canvas(720, 340)
    arrow(c, (30, 300), (30, 30), "EDGE", 1.4, 9)
    txt(c, 30, 22, "Energy", "HEAD", "middle", 13, "700")
    band(c, 60, 40, 200, 50, "GREEN", 0.22)
    band(c, 60, 230, 200, 50, "ATOM", 0.30)
    line(c, (60, 210), (260, 210), "ACC", 2.0, "6,4")
    dot(c, (120, 248), 4.5, "BLUE", "BLUE")
    arrow(c, (120, 240), (120, 218), "BLUE", 1.8, 8)
    circle(c, (190, 248), 5, "PINK", 2.0)
    txt(c, 272, 94, sub("E", "c"), "HEAD", "start", 13, "700")
    txt(c, 272, 215, sub("E", "a"), "ACC", "start", 13, "700")
    txt(c, 272, 240, sub("E", "v"), "HEAD", "start", 13, "700")
    dim(c, (90, 90), (90, 230), "", "TEXT")
    txt(c, 98, 150, sub("E", "g"), "HEAD", "start", 14, "700")
    txt(c, 130, 200, "acceptor level", "ACC", "start", 11)
    txt(c, 170, 70, "conduction band", "TEXT", "start", 11)
    txt(c, 205, 270, "hole", "PINK", "start", 11, "700")
    txt(c, 160, 308, "ΔE = " + sub("E", "a") + " − " + sub("E", "v") + " (small)", "BLUE", "middle", 12, "700")
    pts = _si_cell(c, 500, 150, 62, "B", "B")
    hp = ((pts[(1, 1)][0] + pts[(2, 1)][0]) / 2, pts[(1, 1)][1])
    circle(c, hp, 7, "PINK", 2.0, None, "none")
    txt(c, 500, 262, "Si: 4 valence electrons", "TEXT", "middle", 12)
    txt(c, 500, 280, "B: 3 valence electrons, one bond lacks an electron", "PINK", "middle", 12, "700")
    txt(c, 500, 24, "p-type: acceptor impurity (B)", "HEAD", "middle", 13, "700")
    REG.put("acceptor-level", c, "Acceptor level in a p-type semiconductor",
            "p-type semiconductor: a B atom (3 valence electrons) in Si creates an acceptor level Ea just above the valence band; an electron that jumps into it leaves a hole in the valence band (schematic, not to scale)")


def extrinsic_temperature():
    c = Canvas(680, 350)
    o = (60, 300)
    axes(c, o, 650, 30, "1/T", "ln σ")
    xa, xb = 175, 255
    poly(c, [(80, 50), (xa, 225)], "PINK", 2.8)
    poly(c, [(xa, 225), (xa + 18, 200), (xa + 45, 190), (xb, 192)], "PINK", 2.4, "5,4")
    poly(c, [(xb, 192), (520, 262)], "BLUE", 2.8)
    for x in (xa, xb):
        line(c, (x, 120), (x, o[1]), "EDGE", 1.0, "3,4")
    txt(c, 80, 322, "high T", "TEXT", "middle", 12)
    txt(c, 560, 322, "low T", "TEXT", "middle", 12)
    txt(c, 340, 54, "Intrinsic range: slope = −" + sub("E", "g") + " / 2k", "PINK", "start", 13, "700")
    line(c, (335, 50), (125, 130), "PINK", 0.9)
    txt(c, 340, 118, "Exhaustion (n) / saturation (p) range:", "TEXT", "start", 12, "700")
    txt(c, 340, 134, "all impurities ionised, σ almost constant", "TEXT", "start", 12)
    line(c, (335, 128), (222, 192), "EDGE", 0.9)
    txt(c, 340, 186, "Extrinsic range: slope = −(" + sub("E", "c") + " − " + sub("E", "d") + ") / 2k", "BLUE", "start", 13, "700")
    txt(c, 340, 203, "(p-type: −(" + sub("E", "a") + " − " + sub("E", "v") + ") / 2k)", "BLUE", "start", 12)
    line(c, (420, 216), (420, 234), "BLUE", 0.9)
    REG.put("extrinsic-temperature", c, "Effect of temperature on an extrinsic semiconductor",
            "ln σ against 1/T of an extrinsic semiconductor: extrinsic range at low T, exhaustion (n-type) or saturation (p-type) range at intermediate T, intrinsic range at high T (schematic, not to scale)")


# ---------------------------------------------------------------- applications (S45-S49)

def pn_junction():
    c = Canvas(660, 290)
    rect(c, 80, 60, 220, 140, "BLUE", 1.6, None, "BLUE", 0.12)
    rect(c, 300, 60, 220, 140, "PINK", 1.6, None, "PINK", 0.12)
    line(c, (300, 44), (300, 216), "HEAD", 1.6, "6,4")
    txt(c, 300, 36, "p–n junction (interface)", "HEAD", "middle", 13, "700")
    hp = [(115, 90), (180, 80), (245, 100), (140, 140), (205, 130), (265, 160), (110, 175), (190, 180)]
    ep = [(335, 95), (400, 85), (470, 105), (350, 145), (425, 135), (495, 165), (330, 180), (440, 182)]
    for x, y in hp:
        circle(c, (x, y), 6, "BLUE", 1.8)
        txt(c, x, y + 4, "+", "BLUE", "middle", 11, "700")
    for x, y in ep:
        dot(c, (x, y), 6, "PINK", "PINK")
        txt(c, x, y + 4, "−", "HEAD", "middle", 11, "700")
    txt(c, 190, 224, "p-type", "BLUE", "middle", 14, "700")
    txt(c, 190, 242, "holes are the majority carriers", "TEXT", "middle", 12)
    txt(c, 410, 224, "n-type", "PINK", "middle", 14, "700")
    txt(c, 410, 242, "electrons are the majority carriers", "TEXT", "middle", 12)
    REG.put("pn-junction", c, "A p–n junction",
            "A p–n junction is the boundary between a p-type region (holes) and an n-type region (electrons) (qualitative sketch)")


def photoconductivity():
    c = Canvas(700, 320)
    arrow(c, (30, 290), (30, 36), "EDGE", 1.4, 9)
    txt(c, 30, 26, "Energy", "HEAD", "middle", 13, "700")
    band(c, 60, 50, 230, 60, "GREEN", 0.12)
    band(c, 60, 200, 230, 70, "ATOM", 0.30)
    electrons(c, 60, 200, 230, 70, 10, 3)
    dim(c, (90, 112), (90, 198), "", "TEXT")
    txt(c, 98, 160, sub("E", "g"), "HEAD", "start", 15, "700")
    wave(c, (130, 114), (176, 192), 4, 3, "ACC", 2.2)
    txt(c, 190, 150, "photon", "ACC", "start", 12)
    txt(c, 190, 166, "hν ≥ " + sub("E", "g"), "ACC", "start", 13, "700")
    arrow(c, (262, 196), (262, 112), "BLUE", 1.8, 9)
    dot(c, (262, 96), 5, "BLUE", "BLUE")
    txt(c, 250, 100, "free electron", "BLUE", "end", 12, "700")
    txt(c, 70, 72, "conduction band", "TEXT", "start", 11)
    txt(c, 175, 306, "Photoconductivity", "HEAD", "middle", 13, "700")
    # thresholds
    txt(c, 520, 36, "Photons absorbed (as printed)", "HEAD", "middle", 13, "700")

    def X(e):
        return 400 + (e - 0.8) * 200
    for e in (1.0, 1.5, 2.0):
        line(c, (X(e), 190), (X(e), 196), "EDGE", 1.1)
        txt(c, X(e), 211, f"{e:.1f}", "TEXT", "middle", 11)
    line(c, (X(0.8), 190), (X(2.1), 190), "EDGE", 1.3, head=True)
    txt(c, X(2.1), 232, "photon energy (eV)", "HEAD", "end", 12, "700")
    for k, (name, e, y, col) in enumerate((("Si", 1.1, 62, "BLUE"), ("GaAs", 1.43, 106, "GREEN"), ("AlGaAs", 1.7, 150, "PINK"))):
        rect(c, X(e), y, X(2.1) - X(e), 26, col, 1.4, None, col, 0.30)
        txt(c, 396, y + 18, name, "HEAD", "start", 12, "700")
        txt(c, X(2.1) - 6, y + 18, f"> {e} eV", "HEAD", "end", 12)
    line(c, (X(1.5), 50), (X(1.5), 190), "ACC", 1.5, "6,4")
    txt(c, X(1.5), 270, "solar light " + sub("E", "g") + " about 1.5 eV", "ACC", "middle", 12, "700")
    REG.put("photoconductivity", c, "Photoconductivity and photovoltaic cells",
            "A photon with hν ≥ Eg lifts an electron across the gap, so the conductivity rises; the absorption thresholds of Si, GaAs and AlGaAs and the Eg of solar light (about 1.5 eV) are those printed on the slide (schematic)")


def led_recombination():
    c = Canvas(700, 310)
    rect(c, 50, 70, 130, 100, "BLUE", 1.6, None, "BLUE", 0.14)
    rect(c, 180, 70, 130, 100, "PINK", 1.6, None, "PINK", 0.14)
    txt(c, 115, 62, "p", "BLUE", "middle", 14, "700")
    txt(c, 245, 62, "n", "PINK", "middle", 14, "700")
    for x, y in ((80, 100), (125, 90), (95, 140), (150, 130)):
        circle(c, (x, y), 5, "BLUE", 1.8)
    for x, y in ((210, 100), (255, 90), (225, 140), (285, 130)):
        dot(c, (x, y), 5, "PINK", "PINK")
    arrow(c, (155, 118), (176, 118), "BLUE", 1.8, 8)
    arrow(c, (205, 118), (184, 118), "PINK", 1.8, 8)
    wave(c, (180, 112), (180, 26), 5, 3, "ACC", 2.2)
    txt(c, 192, 38, "light", "ACC", "start", 12, "700")
    # battery, forward bias: + on p side
    line(c, (50, 170), (50, 215), "HEAD", 1.6)
    line(c, (310, 170), (310, 215), "HEAD", 1.6)
    line(c, (50, 215), (155, 215), "HEAD", 1.6)
    line(c, (205, 215), (310, 215), "HEAD", 1.6)
    line(c, (155, 203), (155, 227), "HEAD", 2.6)
    line(c, (167, 209), (167, 221), "HEAD", 2.6)
    line(c, (167, 215), (205, 215), "HEAD", 1.6)
    txt(c, 147, 200, "+", "TEXT", "end", 12)
    txt(c, 175, 200, "−", "TEXT", "start", 12)
    txt(c, 180, 252, "Forward-biased p–n junction", "HEAD", "middle", 13, "700")
    # band picture
    band(c, 430, 50, 110, 50, "GREEN", 0.22)
    band(c, 430, 160, 110, 50, "ATOM", 0.30)
    dot(c, (470, 82), 5, "PINK", "PINK")
    arrow(c, (470, 90), (470, 150), "PINK", 1.6, 8)
    circle(c, (470, 190), 5, "BLUE", 1.8)
    wave(c, (505, 100), (580, 150), 4, 3, "ACC", 2.2)
    dim(c, (420, 102), (420, 158), "", "TEXT")
    txt(c, 412, 134, sub("E", "g"), "HEAD", "end", 14, "700")
    txt(c, 590, 160, "hν = " + sub("E", "g"), "ACC", "start", 13, "700")
    txt(c, 485, 252, "Electron–hole recombination", "HEAD", "middle", 13, "700")
    txt(c, 350, 286, "The colour depends on " + sub("E", "g") + ": red and infra-red (AlGaAs), green (GaN, GaP), blue (ZnSe, InGaN, SiC), ultra-violet (diamond)", "TEXT", "middle", 11)
    REG.put("led-recombination", c, "Light-emitting diode",
            "LED: in a forward-biased p–n junction, electrons and holes recombine and emit a photon of energy about Eg, so the colour depends on the band gap (schematic)")


# ---------------------------------------------------------------- dielectrics (S51-S53)

def dipole_polarization():
    c = Canvas(720, 330)
    circle(c, (150, 80), 24, "BLUE", 2.0, None, "BLUE", 0.15)
    txt(c, 150, 86, "−q", "BLUE", "middle", 16, "700")
    circle(c, (150, 220), 24, "PINK", 2.0, None, "PINK", 0.15)
    txt(c, 150, 226, "+q", "PINK", "middle", 16, "700")
    line(c, (150, 104), (150, 196), "EDGE", 1.6, "5,4")
    dim(c, (205, 104), (205, 196), "d", "TEXT", (14, 5), "start")
    arrow(c, (95, 108), (95, 192), "ACC", 2.8, 12)
    txt(c, 84, 155, "p", "ACC", "end", 17, "700")
    txt(c, 150, 280, "p = q · d", "HEAD", "middle", 16, "700")
    # plates
    def dip(x, y, ang, col_a="BLUE", col_b="PINK"):
        L = 9
        dx, dy = L * math.sin(ang), L * math.cos(ang)
        circle(c, (x - dx, y - dy), 4, col_a, 1.4)
        dot(c, (x + dx, y + dy), 4, col_b, col_b)
        line(c, (x - dx, y - dy), (x + dx, y + dy), "EDGE", 1.2)
    # unpolarised
    line(c, (330, 40), (690, 40), "HEAD", 3)
    line(c, (330, 110), (690, 110), "HEAD", 3)
    txt(c, 510, 30, "Unpolarised", "HEAD", "middle", 13, "700")
    angs = [0.4, 2.2, 4.1, 5.2, 1.3, 3.0, 5.8, 0.9]
    for i, ang in enumerate(angs):
        dip(360 + (i % 8) * 42, 60 + ((i * 17) % 3) * 16, ang)
    line(c, (330, 190), (690, 190), "HEAD", 3)
    line(c, (330, 270), (690, 270), "HEAD", 3)
    txt(c, 510, 150, "Polarised by an applied electric field", "HEAD", "middle", 13, "700")
    for i in range(10):
        txt(c, 345 + i * 36, 184, "+", "PINK", "middle", 14, "700")
        txt(c, 345 + i * 36, 286, "−", "BLUE", "middle", 16, "700")
    for i in range(8):
        dip(360 + i * 42, 214, 0)
        dip(360 + i * 42, 248, 0)
    arrow(c, (700, 200), (700, 262), "GREEN", 2.2, 10)
    txt(c, 690, 238, "E", "GREEN", "end", 14, "700")
    REG.put("dipole-polarization", c, "Dipole moment and polarisation",
            "Dipole moment p = q d of two opposite charges a distance d apart; in a dielectric the dipoles are random without a field and line up with an applied electric field (schematic)")


def capacitor_dielectric():
    c = Canvas(720, 320)

    def cap(x0, with_d):
        line(c, (x0, 80), (x0 + 200, 80), "HEAD", 4)
        line(c, (x0, 210), (x0 + 200, 210), "HEAD", 4)
        battery(c, x0 - 16, 145)
        line(c, (x0 - 16, 80), (x0 - 16, 141), "HEAD", 1.6)
        line(c, (x0 - 16, 149), (x0 - 16, 210), "HEAD", 1.6)
        line(c, (x0 - 16, 80), (x0, 80), "HEAD", 1.6)
        line(c, (x0 - 16, 210), (x0, 210), "HEAD", 1.6)
        for i in range(7):
            txt(c, x0 + 16 + i * 28, 72, "+", "PINK", "middle", 14, "700")
            txt(c, x0 + 16 + i * 28, 232, "−", "BLUE", "middle", 16, "700")
        dim(c, (x0 + 215, 80), (x0 + 215, 210), "d", "TEXT", (12, 5), "start")
        txt(c, x0 + 100, 262, "area A", "TEXT", "middle", 12)
    cap(60, False)
    cap(400, True)
    txt(c, 160, 30, "Vacuum", "HEAD", "middle", 13, "700")
    txt(c, 160, 292, sub("C", "0") + " = " + sub("ε", "0") + " A / d", "HEAD", "middle", 14, "700")
    txt(c, 160, 100, "+" + sub("Q", "0"), "PINK", "middle", 12, "700")
    rect(c, 400, 90, 200, 110, "ACC", 1.4, None, "ACC", 0.20)
    for i in range(6):
        txt(c, 418 + i * 32, 108, "−", "BLUE", "middle", 14, "700")
        txt(c, 418 + i * 32, 192, "+", "PINK", "middle", 14, "700")
    txt(c, 500, 150, "dielectric, " + sub("ε", "r"), "HEAD", "middle", 13, "700")
    txt(c, 500, 30, "With a dielectric", "HEAD", "middle", 13, "700")
    txt(c, 500, 292, "C = " + sub("ε", "r") + " " + sub("ε", "0") + " A / d = " + sub("ε", "r") + " " + sub("C", "0"), "HEAD", "middle", 14, "700")
    txt(c, 640, 76, "net charge on the plates", "TEXT", "start", 11)
    txt(c, 640, 92, "+(" + sub("Q", "0") + " + Q′)", "PINK", "start", 12, "700")
    REG.put("capacitor-dielectric", c, "Parallel-plate capacitor with a dielectric",
            "Parallel-plate capacitor in vacuum and with a dielectric: the polarisation charges of the dielectric let the plates hold more charge, so C = εr C0 (schematic)")


def loss_factor():
    c = Canvas(700, 290)

    def box(x0, up):
        line(c, (x0, 50), (x0 + 220, 50), "HEAD", 3)
        line(c, (x0, 170), (x0 + 220, 170), "HEAD", 3)
        for i in range(7):
            txt(c, x0 + 14 + i * 32, 44, "+" if up else "−", "PINK" if up else "BLUE", "middle", 14, "700")
            txt(c, x0 + 14 + i * 32, 190, "−" if up else "+", "BLUE" if up else "PINK", "middle", 16, "700")
        for i in range(5):
            x = x0 + 30 + i * 40
            ya, yb = (80, 140) if up else (140, 80)
            circle(c, (x, ya), 8, "BLUE", 1.6)
            dot(c, (x, yb), 8, "PINK", "PINK")
            line(c, (x, ya + (8 if up else -8)), (x, yb - (8 if up else -8)), "EDGE", 1.4)
    box(30, True)
    box(450, False)
    txt(c, 140, 30, "Field in one direction", "HEAD", "middle", 13, "700")
    txt(c, 560, 30, "Field reversed", "HEAD", "middle", 13, "700")
    arrow(c, (275, 110), (425, 110), "ACC", 2.4, 11)
    txt(c, 350, 98, "dipoles reorient", "ACC", "middle", 12, "700")
    for k in range(3):
        wave(c, (300 + k * 38, 172), (300 + k * 38, 130), 3, 1.5, "PINK", 1.6)
    txt(c, 350, 205, "friction between dipoles: heat", "PINK", "middle", 12, "700")
    txt(c, 350, 236, "tan δ = electrical energy lost as heat by the capacitor in an alternating current", "HEAD", "middle", 12, "700")
    txt(c, 350, 256, "tan δ increases with moisture, temperature and frequency of the current", "TEXT", "middle", 12)
    REG.put("loss-factor", c, "Dielectric loss in an alternating field",
            "In an alternating current the dipoles of the dielectric must realign at every change of the field; the friction turns electrical energy into heat, measured by the loss factor tan δ (schematic)")


def ferro_hysteresis():
    c = Canvas(640, 350)
    o = (320, 180)
    line(c, (60, o[1]), (600, o[1]), "EDGE", 1.3, head=True)
    line(c, (o[0], 330), (o[0], 20), "EDGE", 1.3, head=True)
    txt(c, 600, o[1] + 24, "Electric field E", "HEAD", "end", 13, "700")
    txt(c, o[0] + 8, 28, "Polarisation P", "HEAD", "start", 13, "700")
    Ps, Ec, w = 100.0, 60.0, 70.0

    def up(e):
        return Ps * math.tanh((e + Ec) / w)

    def dn(e):
        return Ps * math.tanh((e - Ec) / w)
    X = lambda e: o[0] + e * 1.05
    Y = lambda p: o[1] - p * 1.2
    es = [-250 + 5 * i for i in range(101)]
    poly(c, [(X(e), Y(up(e))) for e in es], "PINK", 2.6)
    poly(c, [(X(e), Y(dn(e))) for e in es], "GREEN", 2.6)
    line(c, (X(-250), Y(Ps)), (X(250), Y(Ps)), "EDGE", 1.0, "5,4")
    line(c, (X(-250), Y(-Ps)), (X(250), Y(-Ps)), "EDGE", 1.0, "5,4")
    pr = up(0)
    line(c, (X(-150), Y(pr)), (X(0), Y(pr)), "EDGE", 1.0, "5,4")
    dot(c, (X(0), Y(pr)), 4, "HEAD", "HEAD")
    dot(c, (X(0), Y(-pr)), 4, "HEAD", "HEAD")
    dot(c, (X(Ec), o[1]), 4, "HEAD", "HEAD")
    dot(c, (X(-Ec), o[1]), 4, "HEAD", "HEAD")
    txt(c, X(Ec) + 4, o[1] + 16, "+" + sub("E", "c"), "HEAD", "start", 12, "700")
    txt(c, X(-Ec) - 6, o[1] - 8, "−" + sub("E", "c"), "HEAD", "end", 12, "700")
    txt(c, X(0) - 8, Y(pr) - 8, "+" + sub("P", "r"), "HEAD", "end", 12, "700")
    txt(c, X(0) + 8, Y(-pr) + 16, "−" + sub("P", "r"), "HEAD", "start", 12, "700")
    txt(c, X(250), Y(Ps) - 7, "+" + sub("P", "s") + " (saturation polarisation)", "TEXT", "end", 12)
    txt(c, X(-250), Y(-Ps) + 16, "−" + sub("P", "s"), "TEXT", "start", 12)
    xd = X(-150)
    dim(c, (xd, Y(Ps)), (xd, Y(pr)), "", "TEXT")
    txt(c, xd - 8, (Y(Ps) + Y(pr)) / 2 - 2, "non-remanent", "TEXT", "end", 11)
    txt(c, xd - 8, (Y(Ps) + Y(pr)) / 2 + 12, "polarisation", "TEXT", "end", 11)
    dim(c, (xd, Y(pr)), (xd, o[1]), "", "TEXT")
    txt(c, xd - 8, (Y(pr) + o[1]) / 2 + 2, "remanent", "TEXT", "end", 11)
    txt(c, xd - 8, (Y(pr) + o[1]) / 2 + 16, "polarisation " + sub("P", "r"), "TEXT", "end", 11)
    REG.put("ferro-hysteresis", c, "Ferroelectric hysteresis loop",
            "Polarisation against electric field of a ferroelectric: remanent polarisation Pr at E = 0, coercive field Ec, saturation polarisation Ps; the area of the loop is the energy needed to reorient the dipoles (schematic, not to scale)")


def batio3_cell():
    c = Canvas(720, 340)

    def cube(x0, y0, s, h, dx, dy, ti_shift, o_shift, title):
        F = [(x0, y0), (x0 + s, y0), (x0 + s, y0 + h), (x0, y0 + h)]
        B = [(a + dx, b + dy) for a, b in F]
        for k in range(4):
            line(c, F[k], F[(k + 1) % 4], "HEAD", 1.8)
            line(c, F[k], B[k], "EDGE", 1.2, "4,3" if k == 3 else None)
        for k in range(4):
            line(c, B[k], B[(k + 1) % 4], "EDGE", 1.2, "4,3")
        for p_ in F + B:
            circle(c, p_, 8, "ACC", 1.4, None, "ACC", 0.8)
        faces = [(x0 + s / 2, y0 + h / 2), (x0 + s / 2 + dx, y0 + h / 2 + dy), (x0 + dx / 2, y0 + h / 2 + dy / 2),
                 (x0 + s + dx / 2, y0 + h / 2 + dy / 2), (x0 + s / 2 + dx / 2, y0 + dy / 2), (x0 + s / 2 + dx / 2, y0 + h + dy / 2)]
        for p_ in faces:
            circle(c, (p_[0], p_[1] + o_shift), 5, "PINK", 1.4, None, "PINK", 0.8)
        ctr = (x0 + s / 2 + dx / 2, y0 + h / 2 + dy / 2 + ti_shift)
        circle(c, ctr, 6.5, "HEAD", 1.6, None, "HEAD", 0.9)
        txt(c, x0 + s / 2 + dx / 2, y0 + h + 52, title, "HEAD", "middle", 13, "700")
        return ctr
    cube(60, 100, 110, 110, 44, -44, 0, 0, "T > 120 °C: cubic")
    txt(c, 160, 288, "no permanent dipole", "TEXT", "middle", 12)
    ctr = cube(400, 92, 110, 124, 44, -44, -12, 6, "T < 120 °C: tetragonal")
    txt(c, 480, 286, "Ti and O displaced: permanent dipole", "TEXT", "middle", 12)
    arrow(c, (610, 200), (610, 120), "GREEN", 3.0, 12)
    txt(c, 622, 164, sub("P", "s"), "GREEN", "start", 15, "700")
    # legend
    circle(c, (60, 322), 7, "ACC", 1.4, None, "ACC", 0.8)
    txt(c, 74, 326, "Ba²⁺", "TEXT", "start", 12)
    circle(c, (140, 322), 6, "HEAD", 1.4, None, "HEAD", 0.9)
    txt(c, 152, 326, "Ti⁴⁺", "TEXT", "start", 12)
    circle(c, (220, 322), 5, "PINK", 1.4, None, "PINK", 0.8)
    txt(c, 232, 326, "O²⁻", "TEXT", "start", 12)
    txt(c, 360, 24, "BaTiO" + sub("", "3") + ": spontaneous polarisation below the Curie temperature", "HEAD", "middle", 13, "700")
    REG.put("batio3-cell", c, "BaTiO3 unit cell above and below the Curie temperature",
            "BaTiO3 unit cell: cubic with a centred Ti ion above 120 °C (no permanent dipoles) and tetragonal below it, with Ti and O displaced so that a permanent dipole appears (schematic, displacements exaggerated)")


def piezo_effects():
    c = Canvas(740, 345)
    # direct effect: the block is compressed, charges appear on its faces
    txt(c, 170, 26, "Direct effect", "HEAD", "middle", 14, "700")
    rect(c, 100, 100, 140, 110, "EDGE", 1.2, "4,4")
    rect(c, 100, 110, 140, 90, "ACC", 1.6, None, "ACC", 0.25)
    for x in (130, 170, 210):
        arrow(c, (x, 58), (x, 102), "BLUE", 2.2, 9)
        arrow(c, (x, 252), (x, 208), "BLUE", 2.2, 9)
    txt(c, 262, 84, "stress \u03c3", "BLUE", "start", 12, "700")
    for i in range(4):
        txt(c, 114 + i * 34, 126, "+", "PINK", "middle", 14, "700")
        txt(c, 114 + i * 34, 194, "\u2212", "BLUE", "middle", 16, "700")
    line(c, (100, 112), (60, 112), "HEAD", 1.5)
    line(c, (100, 198), (60, 198), "HEAD", 1.5)
    line(c, (60, 112), (60, 134), "HEAD", 1.5)
    line(c, (60, 176), (60, 198), "HEAD", 1.5)
    circle(c, (60, 155), 21, "HEAD", 1.6)
    txt(c, 60, 160, "V", "HEAD", "middle", 15, "700")
    txt(c, 170, 282, "stress \u2192 deformation of the structure", "TEXT", "middle", 11)
    txt(c, 170, 298, "\u2192 dipole change \u2192 electric field", "TEXT", "middle", 11)
    # reverse effect: the block elongates
    txt(c, 570, 26, "Reverse effect (electrostriction)", "HEAD", "middle", 14, "700")
    rect(c, 500, 120, 140, 90, "EDGE", 1.2, "4,4")
    rect(c, 500, 100, 140, 110, "ACC", 1.6, None, "ACC", 0.25)
    dim(c, (656, 100), (656, 120), "", "TEXT")
    txt(c, 664, 114, "\u0394l", "TEXT", "start", 13)
    line(c, (500, 212), (470, 212), "HEAD", 1.5)
    line(c, (500, 105), (470, 105), "HEAD", 1.5)
    battery(c, 470, 160)
    line(c, (470, 105), (470, 156), "HEAD", 1.5)
    line(c, (470, 164), (470, 212), "HEAD", 1.5)
    txt(c, 570, 160, "P", "HEAD", "middle", 15, "700")
    txt(c, 570, 282, "electric field \u2192 dipole change", "TEXT", "middle", 11)
    txt(c, 570, 298, "\u2192 deformation: dimensions change", "TEXT", "middle", 11)
    txt(c, 370, 330, "dashed outline: size without stress or field", "TEXT", "middle", 11)
    REG.put("piezo-effects", c, "Direct and reverse piezoelectric effect",
            "Piezoelectric material: an external stress changes the dipoles and generates an electric field (direct effect), and an external electric field deforms the structure (reverse effect) (schematic)")


# ---------------------------------------------------------------- slide crops (not generated here)

def rasters():
    REG.raster("s13-resistivity-table", "Resistivity at 0 degrees C and temperature coefficient of selected metals",
               "Resistivity at 0 °C and temperature coefficient of resistivity of aluminium, copper, gold, iron and silver, copied from Session 13 Slide 14", 460)
    REG.raster("s13-resistivity-metals-chart", "Resistivity against temperature of selected metals",
               "Effect of temperature on the electrical resistivity of selected metals, copied from Session 13 Slide 14", 520)
    REG.raster("s13-matthiessen-copper", "Resistivity of copper and Cu-Ni alloys against temperature",
               "Resistivity against temperature of pure, alloyed (Cu + Ni) and deformed copper, showing the thermal, impurity and deformation parts, copied from Session 13 Slide 17", 520)
    REG.raster("s13-impurity-copper", "Effect of impurities on the resistivity of copper",
               "Effect of small additions of various elements on the room-temperature electrical resistivity of copper, copied from Session 13 Slide 16", 400)
    REG.raster("s13-hardening-conductivity", "Yield strength and conductivity against cold work and zinc content",
               "Yield strength and electrical conductivity against percent cold work (left) and percent Zn (right), copied from Session 13 Slide 18", 700)
    REG.raster("s13-intrinsic-charts", "Conductivity of an intrinsic semiconductor against temperature",
               "Electrical conductivity against temperature (left) and against 1/T with the slope −Eg/2k (right) of an intrinsic semiconductor, copied from Session 13 Slide 29", 620)
    REG.raster("s13-si-ge-table", "Properties of silicon and germanium",
               "Energy gap, mobilities, intrinsic carrier density, intrinsic resistivity and density of Si and Ge, copied from Session 13 Slide 31", 640)
    REG.raster("s13-semiconductor-table", "Band gap, conductivity and mobilities of intrinsic semiconductors",
               "Band gap, electrical conductivity and mobilities of Si, Ge, GaP, GaAs, InSb, CdS and ZnTe, copied from Session 13 Slide 33", 640)
    REG.raster("s13-dopant-levels", "Donor and acceptor energy gaps in silicon and germanium",
               "Donor and acceptor energy gaps (in eV) when silicon and germanium are doped, copied from Session 13 Slide 40", 640)
    REG.raster("s13-dopant-solubility", "Maximum solid solubility of dopants in silicon and germanium",
               "Maximum solid solubility of some dopants in Si and Ge, copied from Session 13 Slide 40", 460)
    REG.raster("s13-mobility-silicon", "Mobility of electrons and holes in silicon against dopant concentration",
               "Dependence of the room-temperature electron and hole mobilities on the dopant concentration for Si, copied from Session 13 Slide 42", 480)
    REG.raster("s13-thermistor", "Conductivity of aluminium and germanium against temperature",
               "Electrical conductivity against temperature of aluminium (reducing mobility) and germanium (increasing charge carriers), the basis of thermistors, copied from Session 13 Slide 48", 420)


def theory():
    band_formation()
    bands_vs_spacing()
    band_types()
    conductivity_scale()
    electron_drift()
    ohm_geometry()
    matthiessen()
    scattering_sources()
    graphene_lattice()
    ionic_conduction()
    intrinsic_excitation()
    intrinsic_arrhenius()
    compound_trend()
    donor_level()
    acceptor_level()
    extrinsic_temperature()
    pn_junction()
    photoconductivity()
    led_recombination()
    dipole_polarization()
    capacitor_dielectric()
    loss_factor()
    ferro_hysteresis()
    batio3_cell()
    piezo_effects()
    rasters()


def build():
    theory()
    if importlib.util.find_spec("figures.materials_t6_problems") is not None:
        from figures import materials_t6_problems
        materials_t6_problems.problems(REG)
    return REG
