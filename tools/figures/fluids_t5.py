"""Topic 5 figures for Fluid Mechanics: hydrostatics (Notes.pdf, Chapter 5) and the problems FS1-FS10.

Theory figures (this module): the plane surface with its pressure prism and the folded-down front view, the curved
surface with its projections and the radial element, Archimedes' control volume, the stability of submerged and
floating bodies (Fig. 5.1 of the notes, redrawn, plus the metacentre as an extension), the U-tube manometer and the
standard atmosphere (Fig. 5.2, recomputed from Eqs. 5.20, 5.24, 5.25 and 5.18). Problem figures: tools/figures/fluids_t5p.py.

Colour code: BLUE liquid and pressure distributions, ACC resultant forces, GREEN geometry of the deduction
(right triangles, strips, areas), PINK weights and reactions, HEAD/TEXT/EDGE lines and labels.
"""
import math

from figures.svgkit import Canvas, Registry, arrow, circle, dim, dot, hatch, line, pathd, poly, rect, sub

REG = Registry("FM-T5")
SERIF = "Newsreader, Georgia, 'Times New Roman', serif"
RASTER = {}                     # name -> (alt, caption): crops of the official sheets, filled by fluids_t5p


def lab(c, p, s, col="HEAD", anchor="middle", size=17, italic=True, weight="400"):
    style = ' font-style="italic"' if italic else ""
    c.add(f'<text x="{p[0]:.1f}" y="{p[1]:.1f}" fill="{col}" font-size="{size}" font-weight="{weight}" '
          f'text-anchor="{anchor}" font-family="{SERIF}"{style}>{s}</text>')


def note(c, p, s, col="TEXT", anchor="middle", size=13):
    lab(c, p, s, col, anchor, size, italic=False)


def arc(c, centre, r, a0, a1, col="HEAD", w=1.4, head=False):
    """Arc of radius r from screen angle a0 to a1 (degrees, measured clockwise from +x as on screen)."""
    p0 = (centre[0] + r * math.cos(math.radians(a0)), centre[1] + r * math.sin(math.radians(a0)))
    p1 = (centre[0] + r * math.cos(math.radians(a1)), centre[1] + r * math.sin(math.radians(a1)))
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 1 if a1 > a0 else 0
    pathd(c, f"M{p0[0]:.1f},{p0[1]:.1f} A{r:.1f},{r:.1f} 0 {large} {sweep} {p1[0]:.1f},{p1[1]:.1f}", col, w)
    if head:
        k = -1 if a1 > a0 else 1
        t = (math.sin(math.radians(a1)) * k, -math.cos(math.radians(a1)) * k)
        from figures.svgkit import arrow_head
        arrow_head(c, (p1[0] - 8 * t[0], p1[1] - 8 * t[1]), p1, col, 8)


def water_surface(c, x0, x1, y, label=True, lab_x=None):
    line(c, (x0, y), (x1, y), "BLUE", 2.0)
    tri = [(x1 - 34, y - 12), (x1 - 22, y - 12), (x1 - 28, y - 2)]
    poly(c, tri, "BLUE", 1.2, close=True)
    for k, dx in enumerate((10, 6)):
        line(c, (x1 - 28 - dx, y + 5 + 4 * k), (x1 - 28 + dx, y + 5 + 4 * k), "BLUE", 1.0)
    if label:
        lab(c, (lab_x if lab_x is not None else x0 + 4, y - 8), sub("p", "a"), "HEAD", "start", 16)


# ----------------------------------------------------------------------------------------------- plane surface
def plane_surface():
    c = Canvas(800, 360)
    th = math.radians(50)
    d = (math.cos(th), math.sin(th))                        # down the plate (screen)
    up = (math.sin(th), -math.cos(th))                      # normal towards the liquid (up and right)
    O = (70, 70)
    P = lambda s: (O[0] + s * d[0], O[1] + s * d[1])
    s1, s2, sb = 110, 260, 300
    # liquid and wall
    poly(c, [O, (420, 70), (420, P(sb)[1]), P(sb)], "BLUE", 0, fill="BLUE", close=True, opacity=0.08)
    water_surface(c, 40, 420, 70, lab_x=300)
    line(c, O, P(sb), "EDGE", 2.0)
    hatch(c, O, P(sb), side=1, col="EDGE", step=11)
    line(c, P(s1), P(s2), "ACC", 5.0)
    # pressure prism: arrows normal to the plate, length proportional to the depth s sin(theta)
    k = 0.30
    for s in range(s1, s2 + 1, 15):
        a = (P(s)[0] + up[0] * k * s, P(s)[1] + up[1] * k * s)
        arrow(c, a, P(s), "BLUE", 1.2, 7)
    poly(c, [P(s1), (P(s1)[0] + up[0] * k * s1, P(s1)[1] + up[1] * k * s1),
             (P(s2)[0] + up[0] * k * s2, P(s2)[1] + up[1] * k * s2), P(s2)], "BLUE", 1.2)
    # right triangle of the depth
    sd = 205
    Q = P(sd)
    line(c, (Q[0], 70), Q, "GREEN", 1.4, dash="5,4")
    lab(c, (Q[0] + 30, 96), "s sin θ", "GREEN", "start", 15)
    line(c, (Q[0] + 26, 92), (Q[0] + 4, 100), "GREEN", 0.9)
    arc(c, O, 34, 0, 50, "HEAD", 1.3)
    lab(c, (O[0] + 44, O[1] + 24), "θ", "HEAD", "start", 17)
    lab(c, (O[0] - 6, O[1] + 2), "O", "HEAD", "end", 16, italic=False)
    # s axis along the plate, on the dry side
    off = (-up[0] * 26, -up[1] * 26)
    arrow(c, (O[0] + off[0], O[1] + off[1]), (P(sb)[0] + off[0], P(sb)[1] + off[1]), "HEAD", 1.2, 8)
    lab(c, (P(sb)[0] + off[0] - 12, P(sb)[1] + off[1] + 4), "s", "HEAD", "end", 17)
    # centroid, centre of pressure and resultant
    sC = (s1 + s2) / 2
    sCP = sC + (s2 - s1) ** 2 / 12 / sC
    for s, name, dy in ((sC, "C", -6), (sCP, "CP", 16)):
        dot(c, P(s), 3.6, "HEAD")
    Cl = P(sC - 16)
    lab(c, (Cl[0] - up[0] * 16 - 4, Cl[1] - up[1] * 16), "C", "HEAD", "end", 16, italic=False)
    F0 = P(sCP)
    F1 = (F0[0] - up[0] * 95, F0[1] - up[1] * 95)
    arrow(c, (F0[0] - up[0] * 5, F0[1] - up[1] * 5), F1, "ACC", 3.0, 12)
    lab(c, (F1[0] - 4, F1[1] + 20), sub("F", "R"), "ACC", "middle", 18)
    Pl = P(sCP + 20)
    lab(c, (Pl[0] - up[0] * 12, Pl[1] - up[1] * 12 + 10), "CP", "HEAD", "middle", 15, italic=False)
    note(c, (250, 345), "Side view: pressure prism, p − pₐ = ρg s sin θ", "TEXT", "middle", 13)

    # front view, folded down onto the paper
    x0, y0, sc = 560, 40, 0.95
    Y = lambda s: y0 + s * sc
    line(c, (500, y0), (770, y0), "BLUE", 1.4, dash="6,4")
    note(c, (770, y0 - 8), "line s = 0 (free surface)", "TEXT", "end", 12)
    arrow(c, (520, y0), (520, Y(sb) - 14), "HEAD", 1.2, 8)
    lab(c, (512, Y(sb) - 16), "s", "HEAD", "end", 17)
    rect(c, x0, Y(s1), 140, Y(s2) - Y(s1), "ACC", 2.2, fill="ACC", opacity=0.08)
    ss = 228
    rect(c, x0, Y(ss), 140, 9, "GREEN", 1.2, fill="GREEN", opacity=0.35)
    lab(c, (x0 + 150, Y(ss) + 9), "dA = w ds", "GREEN", "start", 15)
    dim(c, (x0, Y(s2) + 16), (x0 + 140, Y(s2) + 16), "w", "TEXT", (0, 18), size=16)
    line(c, (x0, Y(s2) + 6), (x0, Y(s2) + 22), "EDGE", 0.8)
    line(c, (x0 + 140, Y(s2) + 6), (x0 + 140, Y(s2) + 22), "EDGE", 0.8)
    dot(c, (x0 + 70, Y(sC)), 3.6, "HEAD")
    lab(c, (x0 + 58, Y(sC) + 2), "C", "HEAD", "end", 15, italic=False)
    dot(c, (x0 + 70, Y(sCP)), 3.6, "ACC")
    lab(c, (x0 + 82, Y(sCP) + 12), "CP", "ACC", "start", 15, italic=False)
    for s, t in ((sC, sub("s", "C")), (sCP, sub("s", "CP"))):
        line(c, (516, Y(s)), (x0, Y(s)), "EDGE", 0.8, dash="3,3")
    lab(c, (508, Y(sC) - 2), sub("s", "C"), "HEAD", "end", 15)
    lab(c, (508, Y(sCP) + 14), sub("s", "CP"), "ACC", "end", 15)
    note(c, (650, 345), "Front view (folded down): strip, C and CP", "TEXT", "middle", 13)
    REG.put("t5-plane-surface", c,
            "Plane surface inclined at theta: side view with the pressure prism, the depth triangle and the resultant at the "
            "centre of pressure, and front view with the strip dA = w ds, the centroid C and the centre of pressure CP",
            "Plane surface inclined at $\\theta$. Left: side view with the linear pressure distribution $p - p_a = \\rho g s\\sin\\theta$, "
            "the right triangle that turns the distance $s$ along the plate into the depth $s\\sin\\theta$ (hypotenuse $s$, leg opposite "
            "to $\\theta$), and the resultant $F_R$ normal to the plate at the centre of pressure CP. Right: the plate folded down onto "
            "the paper, with the strip $dA = w\\,ds$ and CP below the centroid C")


# ----------------------------------------------------------------------------------------------- curved surface
def curved_surface():
    c = Canvas(800, 330)
    O, R = (110, 60), 170
    pt = lambda a: (O[0] + R * math.cos(math.radians(a)), O[1] + R * math.sin(math.radians(a)))
    arc_pts = [pt(a) for a in range(0, 91, 3)]
    poly(c, [O] + arc_pts, "BLUE", 0, fill="BLUE", close=True, opacity=0.14)
    water_surface(c, 40, 340, 60)
    poly(c, arc_pts, "ACC", 4.5)
    hatch(c, arc_pts[0], arc_pts[-1], side=-1, col="EDGE", step=400)
    for i in range(len(arc_pts) - 1):
        hatch(c, arc_pts[i], arc_pts[i + 1], side=-1, col="EDGE", step=40, length=7)
    dot(c, O, 3.4, "HEAD")
    lab(c, (O[0] - 8, O[1] - 8), "O", "HEAD", "end", 16, italic=False)
    # element at theta measured from the horizontal radius
    a = 60
    E = pt(a)
    line(c, O, E, "GREEN", 1.3, dash="5,4")
    arc(c, O, 44, 0, a, "GREEN", 1.3)
    lab(c, (O[0] + 50, O[1] + 34), "θ", "GREEN", "start", 17)
    lab(c, ((O[0] + E[0]) / 2 - 10, (O[1] + E[1]) / 2 + 6), "R", "GREEN", "end", 16)
    u = (math.cos(math.radians(a)), math.sin(math.radians(a)))
    arrow(c, E, (E[0] + 70 * u[0], E[1] + 70 * u[1]), "ACC", 2.4, 11)
    lab(c, (E[0] + 74 * u[0] + 6, E[1] + 74 * u[1] + 4), "dF", "ACC", "start", 17)
    lab(c, (E[0] + 7, 112), "R sin θ", "GREEN", "start", 15)
    line(c, (E[0], O[1]), E, "GREEN", 1.0, dash="3,3")
    # vertical force: real column above the arc
    xg = O[0] + 4 * R / (3 * math.pi)
    arrow(c, (xg, 80), (xg, 160), "ACC", 3.0, 12)
    lab(c, (xg - 8, 128), sub("F", "V"), "ACC", "end", 18)
    lab(c, (210, 300), "real column above the arc: weight ρg b πR²/4", "BLUE", "middle", 13, italic=False)
    # horizontal force on the vertical projection
    xp = 540
    rect(c, xp, 60, 12, R, "HEAD", 1.2, fill="EDGE", opacity=0.25)
    line(c, (xp, 60), (xp - 90, 60 + R), "BLUE", 1.2)
    for k in range(1, 7):
        yy = 60 + k * R / 6
        arrow(c, (xp - 90 * k / 6, yy), (xp, yy), "BLUE", 1.1, 6)
    line(c, (xp, 60 + R), (xp - 90, 60 + R), "BLUE", 1.2)
    arrow(c, (xp + 18, 60 + 2 * R / 3), (xp + 108, 60 + 2 * R / 3), "ACC", 3.0, 12)
    lab(c, (xp + 60, 60 + 2 * R / 3 - 12), sub("F", "H"), "ACC", "middle", 18)
    dim(c, (xp + 150, 60), (xp + 150, 60 + 2 * R / 3), "2R/3", "TEXT", (8, 4), "start", 15)
    dim(c, (xp + 210, 60), (xp + 210, 60 + R), "R", "TEXT", (8, 4), "start", 16)
    lab(c, (xp, 300), "vertical projection of the arc, height R", "TEXT", "middle", 13, italic=False)
    REG.put("t5-curved-surface", c,
            "Quarter-cylinder gate of radius R with the liquid above it: radial pressure element dF at angle theta, vertical "
            "force equal to the weight of the real column above the arc, horizontal force on the vertical projection",
            "Quarter-cylinder gate of radius $R$ and width $b$, centre $O$ on the free surface, liquid above the arc. The element "
            "$dF$ at angle $\\theta$ is radial (depth $R\\sin\\theta$); $F_V$ is the weight of the real column above the arc, applied "
            "at $4R/(3\\pi)$ from $O$; $F_H$ is the force on the vertical projection of height $R$, applied at $2R/3$ below the surface")


# ----------------------------------------------------------------------------------------------- Archimedes
def archimedes():
    c = Canvas(560, 300)
    poly(c, [(40, 60), (520, 60), (520, 280), (40, 280)], "BLUE", 0, fill="BLUE", close=True, opacity=0.08)
    water_surface(c, 40, 520, 60)
    cx, cy, rx, ry = 270, 175, 120, 62
    c.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="ACC" fill-opacity="0.10" stroke="HEAD" stroke-width="2"/>')
    for k in range(12):
        a = 2 * math.pi * k / 12
        p = (cx + rx * math.cos(a), cy + ry * math.sin(a))
        nx, ny = math.cos(a) / rx, math.sin(a) / ry
        n = math.hypot(nx, ny)
        nx, ny = nx / n, ny / n
        L = 14 + 0.16 * (p[1] - 60)
        arrow(c, (p[0] + nx * L, p[1] + ny * L), p, "BLUE", 1.1, 6)
    arrow(c, (cx - 30, cy + 10), (cx - 30, cy - 70), "ACC", 3.0, 12)
    lab(c, (cx - 40, cy - 30), "ρgV", "ACC", "end", 18)
    dot(c, (cx - 30, cy + 10), 3.6, "ACC")
    lab(c, (cx - 40, cy + 26), sub("x", "g"), "ACC", "end", 16)
    arrow(c, (cx + 34, cy + 2), (cx + 34, cy + 72), "PINK", 3.0, 12)
    dot(c, (cx + 34, cy + 2), 3.6, "PINK")
    lab(c, (cx + 44, cy + 46), "W", "PINK", "start", 18)
    lab(c, (cx + 44, cy - 2), "G", "PINK", "start", 16, italic=False)
    lab(c, (cx + rx + 10, cy - ry + 4), "V", "HEAD", "start", 18)
    REG.put("t5-archimedes", c,
            "Submerged body of volume V: the pressure on its surface adds up to the buoyancy rho g V applied at the centroid x_g "
            "of the displaced liquid; the weight W acts at the centre of gravity G of the body",
            "Submerged body of volume $V$: the pressure on the closed surface adds up to the buoyancy $\\rho g V\\,\\vec{e}_z$, applied "
            "at the centroid $\\vec{x}_g$ of the displaced liquid (Eqs. 5.15 and 5.16); the weight $W$ acts at the centre of gravity "
            "$G$ of the body, which need not coincide with $\\vec{x}_g$")


# ----------------------------------------------------------------------------------------------- stability
def stability():
    c = Canvas(820, 320)

    def body(cx, cy, tilt, A_up):
        t = math.radians(tilt)
        rot = lambda dx, dy: (cx + dx * math.cos(t) - dy * math.sin(t), cy + dx * math.sin(t) + dy * math.cos(t))
        pts = [rot(35 * math.cos(a), 85 * math.sin(a)) for a in [2 * math.pi * k / 48 for k in range(48)]]
        poly(c, pts, "HEAD", 2.0, fill="ACC", close=True, opacity=0.08)
        line(c, rot(0, -95), rot(0, 95), "EDGE", 1.0, dash="4,4")
        A = rot(0, -28) if A_up else rot(0, 28)
        B = rot(0, 28) if A_up else rot(0, -28)
        dot(c, A, 4, "ACC")
        dot(c, B, 4, "PINK")
        lab(c, (A[0] - 10, A[1] + 5), "A", "ACC", "end", 16, italic=False)
        lab(c, (B[0] + 10, B[1] + 5), "B", "PINK", "start", 16, italic=False)
        arrow(c, A, (A[0], A[1] - 70), "ACC", 2.6, 11)
        lab(c, (A[0] - 12, A[1] - 52), "ρgV", "ACC", "end", 16)
        arrow(c, B, (B[0], B[1] + 70), "PINK", 2.6, 11)
        lab(c, (B[0] + 6, B[1] + 78), "W", "PINK", "start", 16)
        return A, B

    body(120, 160, 0, True)
    note(c, (120, 312), "upright: A above B", "TEXT", size=12)
    A, B = body(290, 160, 22, True)
    arc(c, (290, 160), 118, 115, 75, "GREEN", 1.8, head=True)
    note(c, (290, 312), "tilted: restoring torque", "TEXT", size=12)
    A, B = body(460, 160, 22, False)
    arc(c, (460, 160), 118, 65, 105, "PINK", 1.8, head=True)
    note(c, (460, 312), "B above A: overturns", "TEXT", size=12)

    # floating body and metacentre (extension)
    x0, wl = 690, 150
    t = math.radians(14)
    rot = lambda dx, dy: (x0 + dx * math.cos(t) - dy * math.sin(t), wl + dx * math.sin(t) + dy * math.cos(t))
    hull = [rot(-70, -40), rot(70, -40), rot(70, 50), rot(-70, 50)]
    poly(c, [(570, wl), (810, wl), (810, 290), (570, 290)], "BLUE", 0, fill="BLUE", close=True, opacity=0.08)
    line(c, (570, wl), (810, wl), "BLUE", 1.8)
    poly(c, hull, "HEAD", 2.0, fill="ACC", close=True, opacity=0.08)
    line(c, rot(0, -70), rot(0, 60), "EDGE", 1.0, dash="4,4")
    G = rot(0, -5)
    M = rot(0, -50)
    B = rot(0, 25)
    Bp = (M[0], wl + 28)
    dot(c, B, 3.6, "EDGE")
    lab(c, (B[0] - 9, B[1] + 5), "B", "TEXT", "end", 15, italic=False)
    line(c, Bp, (M[0], M[1] + 4), "ACC", 1.2, dash="4,3")
    arrow(c, Bp, (Bp[0], Bp[1] - 26), "ACC", 2.4, 10)
    dot(c, Bp, 4, "ACC")
    lab(c, (Bp[0] + 9, Bp[1] + 12), "B′", "ACC", "start", 16, italic=False)
    dot(c, G, 4, "PINK")
    lab(c, (G[0] - 9, G[1] + 2), "G", "PINK", "end", 16, italic=False)
    dot(c, M, 4, "GREEN")
    lab(c, (M[0] + 9, M[1] + 4), "M", "GREEN", "start", 16, italic=False)
    note(c, (690, 312), "floating: M above G (extension)", "TEXT", size=12)
    REG.put("t5-stability", c,
            "Stability of a submerged body, as in Fig. 5.1 of the notes: A, centroid of the displaced liquid, above B, centre of "
            "gravity, gives a restoring torque; B above A overturns. Right: a floating body heeled, with G, the shifted centre of "
            "buoyancy B prime and the metacentre M",
            "Stability (Notes.pdf, Fig. 5.1, redrawn): for a submerged body the buoyancy acts at the centroid $A$ of the displaced "
            "liquid and the weight at the centre of gravity $B$; with $A$ above $B$ a tilt produces a restoring torque, with $B$ "
            "above $A$ it overturns the body. Right (extension): a heeled floating body, where the centre of buoyancy moves to "
            "$B'$ and the vertical through $B'$ cuts the symmetry line at the metacentre $M$; the body is stable when $M$ lies above $G$")


# ----------------------------------------------------------------------------------------------- manometer
def manometer():
    c = Canvas(600, 330)
    # pipe with fluid at pressure p_A on the left
    rect(c, 30, 70, 150, 40, "HEAD", 1.8, fill="BLUE", opacity=0.10)
    lab(c, (60, 96), "A", "HEAD", "middle", 16, italic=False)
    dot(c, (80, 90), 3.5, "HEAD")
    lab(c, (105, 62), sub("p", "A") + ", ρ", "HEAD", "middle", 16)
    xl, xr, w = 160, 330, 20
    yb = 290
    # tube walls
    line(c, (xl, 110), (xl, yb), "HEAD", 1.8)
    line(c, (xl + w, 110), (xl + w, yb - w), "HEAD", 1.8)
    line(c, (xl, yb), (xr + w, yb), "HEAD", 1.8)
    line(c, (xl + w, yb - w), (xr, yb - w), "HEAD", 1.8)
    line(c, (xr, yb - w), (xr, 40), "HEAD", 1.8)
    line(c, (xr + w, yb), (xr + w, 40), "HEAD", 1.8)
    y1, y2 = 200, 120                                        # interface on the left, free level on the right
    rect(c, xl, 110, w, y1 - 110, "BLUE", 0, fill="BLUE", opacity=0.18)
    poly(c, [(xl, y1), (xl + w, y1), (xl + w, yb - w), (xr, yb - w), (xr, y2), (xr + w, y2), (xr + w, yb), (xl, yb)],
         "PINK", 0, fill="PINK", close=True, opacity=0.22)
    line(c, (xl - 6, y1), (xl + w + 6, y1), "PINK", 1.4)
    line(c, (xr - 6, y2), (xr + w + 6, y2), "PINK", 1.4)
    lab(c, (xr + w + 8, 52), sub("p", "a"), "HEAD", "start", 16)
    lab(c, (250, yb - 30), sub("ρ", "m"), "PINK", "middle", 17)
    # levels
    for yy in (90, y1, y2):
        line(c, (xl + w + 8, yy), (xr - 8, yy), "EDGE", 0.8, dash="3,3") if yy != 90 else None
    dim(c, (390, y2), (390, y1), sub("h", "2"), "TEXT", (8, 5), "start", 16)
    dim(c, (120, 90), (120, y1), sub("h", "1"), "TEXT", (-8, 5), "end", 16)
    line(c, (110, y1), (xl, y1), "EDGE", 0.8, dash="3,3")
    # walk
    lab(c, (440, 120), "walk from A to the open end:", "TEXT", "start", 13, italic=False)
    lab(c, (440, 146), "down h₁ in ρ:  + ρg h₁", "BLUE", "start", 14, italic=False)
    lab(c, (440, 170), "up h₂ in ρₘ:  − ρₘg h₂", "PINK", "start", 14, italic=False)
    lab(c, (440, 194), "arrive at the level: pₐ", "HEAD", "start", 14, italic=False)
    REG.put("t5-manometer", c,
            "U-tube manometer: pipe at pressure p_A filled with a liquid of density rho, manometric liquid rho_m, column h_1 "
            "from A down to the interface and difference of levels h_2 in the two branches, right branch open to p_a",
            "U-tube manometer (extension): walking from $A$ down the column $h_1$ of the pipe liquid adds $\\rho g h_1$, climbing "
            "the difference of levels $h_2$ in the manometric liquid subtracts $\\rho_m g h_2$, and the open end is at $p_a$")


# ----------------------------------------------------------------------------------------------- standard atmosphere
def atmosphere():
    c = Canvas(780, 330)
    g, Rg, T0, lam = 9.81, 287.0, 288.16, 6.5e-3
    n = g / (Rg * lam)
    T11 = T0 - lam * 11000
    p11 = (T11 / T0) ** n

    def T(z):
        return T0 - lam * z if z <= 11000 else T11

    def p(z):
        return (1 - lam * z / T0) ** n if z <= 11000 else p11 * math.exp(-g * (z - 11000) / (Rg * T11))

    def rho(z):
        return p(z) * T0 / T(z)

    top, bot = 30, 280
    Y = lambda z: bot - (bot - top) * z / 20000
    panels = [("T (K)", T, 200, 300, 40), ("p / pₐ", p, 0, 1, 300), ("ρ / ρ₀", rho, 0, 1, 540)]
    for name, f, lo, hi, x0 in panels:
        wpx = 200
        X = lambda v: x0 + wpx * (v - lo) / (hi - lo)
        line(c, (x0, bot), (x0 + wpx, bot), "EDGE", 1.0)
        line(c, (x0, bot), (x0, top), "EDGE", 1.0)
        for zk in (0, 5000, 10000, 15000, 20000):
            line(c, (x0 - 4, Y(zk)), (x0, Y(zk)), "EDGE", 1.0)
            if x0 == 40:
                note(c, (x0 - 8, Y(zk) + 4), f"{zk // 1000}", "TEXT", "end", 12)
        for v in (lo, (lo + hi) / 2, hi):
            note(c, (X(v), bot + 18), f"{v:g}", "TEXT", "middle", 12)
        lab(c, (x0 + wpx / 2, bot + 40), name, "HEAD", "middle", 15, italic=False)
        tro = [(X(f(z)), Y(z)) for z in range(0, 11001, 250)]
        stra = [(X(f(z)), Y(z)) for z in range(11000, 20001, 250)]
        poly(c, tro, "PINK", 2.4)
        poly(c, stra, "BLUE", 2.4)
        line(c, (x0, Y(8848)), (x0 + wpx, Y(8848)), "EDGE", 0.8, dash="4,4")
    note(c, (12, 22), "z (km)", "TEXT", "start", 12)
    lab(c, (788, Y(8848) - 6), "Everest", "TEXT", "end", 12, italic=False)
    REG.put("t5-atmosphere", c,
            "Standard atmosphere from 0 to 20 km: temperature, pressure ratio and density ratio, troposphere in pink and "
            "stratosphere in blue, with the height of Everest dashed",
            "Standard atmosphere recomputed from Eqs. (5.20), (5.24), (5.25) and (5.18) with $T_0 = 288.16$ K and "
            "$\\lambda = 6.5\\times10^{-3}$ K/m: temperature, $p/p_a$ and $\\rho/\\rho_0$ against the height $z$ (troposphere in pink, "
            "stratosphere in blue; dashed: Everest, 8848 m, where $\\rho/\\rho_0 \\approx 0.39$), as in Notes.pdf, Fig. 5.2")


def build():
    plane_surface()
    curved_surface()
    archimedes()
    stability()
    manometer()
    atmosphere()
    try:
        from figures import fluids_t5p
    except ImportError:
        return REG
    fluids_t5p.build(REG, RASTER)
    return REG
