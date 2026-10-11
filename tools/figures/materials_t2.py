"""Topic 2 figures for Aerospace Materials I (cubic directions and planes, hexagonal cell, cells, densities).

Planes are clipped exactly to the unit cube and directions start at O' (a 1 where an index is negative),
so the drawings follow the construction rules of the topic. Run `python tools/build_topic_pages.py` to
write the SVG files to vault/attachments/T2 and rebuild the page.
"""
import itertools
import math

from figures.svgkit import Canvas, Registry, arrow_head, dot, fmt, line, overline_label as label, text

REG = Registry("T2")
L = 110.0  # cube edge in px


def proj(p, cx, cy):
    x, y, z = p
    return (cx + y * L - x * L * 0.42, cy - z * L + x * L * 0.26)


def fmt(v):
    return f"{v:.1f}"


CUBE_V = list(itertools.product((0, 1), repeat=3))
CUBE_E = [(a, b) for a, b in itertools.combinations(CUBE_V, 2) if sum(abs(i - j) for i, j in zip(a, b)) == 1]


def cube(c, cx, cy, axes=True, corner_labels=()):
    for a, b in CUBE_E:
        hidden = (0, 0, 0) in (a, b)
        line(c, proj(a, cx, cy), proj(b, cx, cy), dash="4,4" if hidden else None, w=1.2)
    if axes:
        o = proj((0, 0, 0), cx, cy)
        for v, name in (((1.55, 0, 0), "x"), ((0, 1.45, 0), "y"), ((0, 0, 1.4), "z")):
            p = proj(v, cx, cy)
            line(c, proj(tuple(min(1, t) for t in v), cx, cy), p, w=1.0, head=True)
            text(c, p, name, "TEXT", "middle", dx=(6 if name == "y" else -8 if name == "x" else 0), dy=(4 if name != "z" else -6))
    for pt, s, dx, dy in corner_labels:
        text(c, proj(pt, cx, cy), s, "TEXT", "middle", size=11, dx=dx, dy=dy)


def direction(c, cx, cy, ind, col="ACC", name=None, name_pos=None, show_origin=True):
    """Draw [u v w] from O' (1 where the index is negative) to O' + v / max|v|."""
    m = max(abs(t) for t in ind)
    o = tuple(1 if t < 0 else 0 for t in ind)
    tip = tuple(oi + t / m for oi, t in zip(o, ind))
    a, b = proj(o, cx, cy), proj(tip, cx, cy)
    line(c, a, b, col, 2.6, head=True)
    if show_origin:
        dot(c, a, 4, col)
    if name:
        p = name_pos if name_pos else ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        text(c, p, name, col, "middle", 14, "700")
    return o, tip


def plane_poly(h, k, l, origin=None):
    """Polygon of h(x-ox)+k(y-oy)+l(z-oz)=1 inside the unit cube, O' = 1 where the index is negative."""
    o = origin or tuple(1 if t < 0 else 0 for t in (h, k, l))
    n = (h, k, l)
    f = lambda p: sum(ni * (pi - oi) for ni, pi, oi in zip(n, p, o)) - 1
    pts = [v for v in CUBE_V if abs(f(v)) < 1e-9]
    for a, b in CUBE_E:
        fa, fb = f(a), f(b)
        if fa * fb < 0 and abs(fa) > 1e-9 and abs(fb) > 1e-9:
            t = fa / (fa - fb)
            pts.append(tuple(ai + t * (bi - ai) for ai, bi in zip(a, b)))
    uniq = []
    for p in pts:
        if all(sum((pi - qi) ** 2 for pi, qi in zip(p, q)) > 1e-9 for q in uniq):
            uniq.append(p)
    cen = tuple(sum(p[i] for p in uniq) / len(uniq) for i in range(3))
    # basis in the plane
    nn = math.sqrt(sum(t * t for t in n))
    nu = tuple(t / nn for t in n)
    ref = (1, 0, 0) if abs(nu[0]) < 0.9 else (0, 1, 0)
    u = cross(nu, ref); un = math.sqrt(sum(t * t for t in u)); u = tuple(t / un for t in u)
    v = cross(nu, u)
    ang = lambda p: math.atan2(dot3(sub(p, cen), v), dot3(sub(p, cen), u))
    return sorted(uniq, key=ang), o


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot3(a, b):
    return sum(x * y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def plane(c, cx, cy, hkl, col="ACC", origin=None, mark_intercepts=True):
    poly, o = plane_poly(*hkl, origin=origin)
    pts = " ".join(f"{fmt(x)},{fmt(y)}" for x, y in (proj(p, cx, cy) for p in poly))
    c.add(f'<polygon points="{pts}" fill="{col}" fill-opacity="0.28" stroke="{col}" stroke-width="1.8"/>')
    if mark_intercepts:
        for i, t in enumerate(hkl):
            if t != 0:
                p = list(o); p[i] = o[i] + 1 / t
                if -1e-9 <= p[i] <= 1 + 1e-9:
                    dot(c, proj(tuple(p), cx, cy), 3.5, col)
    if any(t < 0 for t in hkl) or origin:
        po = proj(o, cx, cy)
        dot(c, po, 4.5, "HEAD", "none")
        text(c, po, "O′", "HEAD", "middle", 13, "700", dx=-12, dy=14)
    return poly, o


def caption(c, x, y, s, col="HEAD", size=14):
    text(c, (x, y), s, col, "middle", size, "700")


def panel_row(n, w=250, h=250):
    return Canvas(n * w, h)


# ============================================================================ figures
def fig_positions():
    c = Canvas(300, 250); cx, cy = 130, 175
    cube(c, cx, cy)
    for p in CUBE_V:
        dot(c, proj(p, cx, cy), 4.5, "ATOM")
    for p, s, dx, dy in (((0, 0, 0), "(0,0,0)", 30, 14), ((1, 0, 0), "(1,0,0)", -38, 4), ((0, 1, 0), "(0,1,0)", 28, 16),
                         ((0, 0, 1), "(0,0,1)", -28, -8), ((1, 1, 1), "(1,1,1)", -30, -8), ((0, 1, 1), "(0,1,1)", 28, -8)):
        text(c, proj(p, cx, cy), s, "TEXT", "middle", 11, dx=dx, dy=dy)
    REG.put("positions", c, "Atomic positions in a cubic cell")


def dir_panel(c, ox, items, title):
    cx, cy = ox + 120, 180
    cube(c, cx, cy)
    for ind, col, lab, lp in items:
        o, tip = direction(c, cx, cy, ind, col)
        t = proj(tip, cx, cy)
        text(c, t, lab, col, "middle", 14, "700", dx=lp[0], dy=lp[1])
    caption(c, ox + 125, 242, title, size=13)


def fig_dir_basic():
    c = panel_row(3, 255, 250)
    dir_panel(c, 0, [((1, 0, 0), "ACC", label("[1 0 0]"), (8, -12))], "tip at (1, 0, 0)")
    dir_panel(c, 255, [((1, 1, 0), "ACC", label("[1 1 0]"), (10, 18))], "tip at (1, 1, 0)")
    dir_panel(c, 510, [((1, 1, 1), "ACC", label("[1 1 1]"), (12, 4))], "tip at (1, 1, 1)")
    REG.put("dir-basic", c, "Directions [100], [110] and [111]")


def fig_dir_reduce():
    c = panel_row(3, 255, 250)
    dir_panel(c, 0, [((0, 1, 2), "ACC", label("[0 1 2]"), (14, -6))], "½[0 1 2] → tip at (0, ½, 1)")
    dir_panel(c, 255, [((2, 1, 0), "BLUE", label("[2 1 0]"), (30, 2))], "½[2 1 0] → tip at (1, ½, 0)")
    dir_panel(c, 510, [((1, 2, 2), "GREEN", label("[1 2 2]"), (14, -6))], "½[1 2 2] → tip at (½, 1, 1)")
    REG.put("dir-reduce", c, "Directions that need reducing: [012], [210], [122]")


def fig_dir_negative():
    c = panel_row(3, 255, 255)
    items = [((-1, 1, 1), "ACC", label("[-1 1 1]"), "O′ = (1, 0, 0)"),
             ((1, -1, 0), "BLUE", label("[1 -1 0]"), "O′ = (0, 1, 0)"),
             ((0, 2, -1), "GREEN", label("[0 2 -1]"), "O′ = (0, 0, 1)")]
    for i, (ind, col, lab, cap) in enumerate(items):
        ox = i * 255; cx, cy = ox + 120, 180
        cube(c, cx, cy)
        o, tip = direction(c, cx, cy, ind, col)
        po = proj(o, cx, cy)
        text(c, po, "O′", "HEAD", "middle", 13, "700", dx=-12, dy=16)
        text(c, proj(tip, cx, cy), lab, col, "middle", 14, "700", dx=14, dy=-8)
        caption(c, ox + 125, 245, cap, size=13)
    REG.put("dir-negative", c, "Directions with negative indices and their new origins")


def fig_dir_read():
    """Reading the indices of a drawn vector: tail (1,0,0), head (0,1,1) -> [-1 1 1]."""
    c = Canvas(560, 260); cx, cy = 140, 185
    cube(c, cx, cy)
    tail, head = (1, 0, 0), (0, 1, 1)
    a, b = proj(tail, cx, cy), proj(head, cx, cy)
    line(c, a, b, "ACC", 2.6, head=True)
    dot(c, a, 4, "ACC")
    text(c, a, "tail (1, 0, 0)", "ACC", "middle", 12, "700", dx=0, dy=18)
    text(c, b, "head (0, 1, 1)", "ACC", "middle", 12, "700", dx=0, dy=-10)
    rows = ["head − tail = (0−1, 1−0, 1−0)", "= (−1, 1, 1)", "already the smallest integers", "→ " + label("[-1 1 1]")]
    for i, r in enumerate(rows):
        text(c, (330, 90 + 28 * i), r, "HEAD" if i == 3 else "TEXT", "start", 15 if i == 3 else 13, "700" if i == 3 else "400")
    REG.put("dir-read", c, "Reading the indices of a drawn direction")


def fig_dir_family():
    c = panel_row(2, 280, 255)
    cx, cy = 125, 180
    cube(c, cx, cy)
    for ind, col in (((1, 1, 1), "ACC"), ((-1, 1, 1), "BLUE"), ((1, -1, 1), "GREEN"), ((1, 1, -1), "PINK")):
        direction(c, cx, cy, ind, col, show_origin=False)
    caption(c, 130, 245, "the 4 body diagonals &lt;1 1 1&gt;", size=13)
    cx2 = 280 + 125
    cube(c, cx2, cy)
    for ind, col in (((1, 0, 0), "ACC"), ((0, 1, 0), "BLUE"), ((0, 0, 1), "GREEN")):
        direction(c, cx2, cy, ind, col, show_origin=False)
    caption(c, 280 + 130, 245, "the cube edges &lt;1 0 0&gt;", size=13)
    REG.put("dir-family", c, "Families of directions &lt;111&gt; and &lt;100&gt;")


def plane_panel(c, ox, hkl, title, sub=None, col="ACC", origin=None, w=255):
    cx, cy = ox + 120, 180
    cube(c, cx, cy)
    plane(c, cx, cy, hkl, col, origin)
    caption(c, ox + w / 2, 240, title, size=14)
    if sub:
        text(c, (ox + w / 2, 258), sub, "TEXT", "middle", 12)


def P(h, k, l):
    return label(f"({h} {k} {l})")


def fig_plane_basic():
    c = panel_row(3, 255, 265)
    plane_panel(c, 0, (1, 0, 0), P(1, 0, 0), "intercepts x = 1, y = ∞, z = ∞")
    plane_panel(c, 255, (1, 1, 0), P(1, 1, 0), "intercepts x = 1, y = 1, z = ∞", "BLUE")
    plane_panel(c, 510, (1, 1, 1), P(1, 1, 1), "intercepts x = 1, y = 1, z = 1", "GREEN")
    REG.put("plane-basic", c, "Planes (100), (110) and (111)")


def fig_plane_more():
    c = panel_row(3, 255, 265)
    plane_panel(c, 0, (2, 0, 0), P(2, 0, 0), "x = ½, y = ∞, z = ∞")
    plane_panel(c, 255, (2, 1, 0), P(2, 1, 0), "x = ½, y = 1, z = ∞", "BLUE")
    plane_panel(c, 510, (0, 1, 1), P(0, 1, 1), "x = ∞, y = 1, z = 1", "GREEN")
    REG.put("plane-more", c, "Planes (200), (210) and (011)")


def fig_plane_negative():
    c = panel_row(4, 240, 265)
    items = [((-1, 0, 0), "O′ = (1,0,0): x = −1", "ACC"), ((1, -1, 0), "O′ = (0,1,0): x = 1, y = −1", "BLUE"),
             ((1, -1, -1), "O′ = (0,1,1): 1, −1, −1", "GREEN"), ((-2, 1, 1), "O′ = (1,0,0): −½, 1, 1", "PINK")]
    for i, (hkl, sub, col) in enumerate(items):
        plane_panel(c, i * 240, hkl, P(*hkl), sub, col, w=240)
    REG.put("plane-negative", c, "Planes with negative indices and their new origins")


def fig_plane_family():
    c = panel_row(2, 280, 265)
    cx, cy = 125, 180
    cube(c, cx, cy)
    for hkl, col in (((1, 0, 0), "ACC"), ((0, 1, 0), "BLUE"), ((0, 0, 1), "GREEN")):
        plane(c, cx, cy, hkl, col, mark_intercepts=False)
    caption(c, 130, 245, "{1 0 0}: the cube faces", size=13)
    cx2 = 280 + 125
    cube(c, cx2, cy)
    plane(c, cx2, cy, (1, 1, 1), "ACC", mark_intercepts=False)
    plane(c, cx2, cy, (-1, 1, 1), "BLUE", mark_intercepts=False)
    caption(c, 280 + 130, 245, "two members of {1 1 1}", size=13)
    REG.put("plane-family", c, "Families of planes {100} and {111}")


def fig_plane_normal():
    c = Canvas(300, 255); cx, cy = 130, 180
    cube(c, cx, cy)
    plane(c, cx, cy, (1, 1, 1), "BLUE", mark_intercepts=False)
    direction(c, cx, cy, (1, 1, 1), "ACC", show_origin=True)
    text(c, proj((1, 1, 1), cx, cy), label("[1 1 1]"), "ACC", "middle", 14, "700", dx=16, dy=-4)
    text(c, proj((0.33, 0.9, 0.2), cx, cy), P(1, 1, 1), "BLUE", "middle", 14, "700", dx=8, dy=26)
    REG.put("plane-normal", c, "In a cube the [111] direction is perpendicular to the (111) plane")


def fig_spacing():
    """Parallel (110) planes seen from above (along z): spacing d110 = a/sqrt(2)."""
    c = Canvas(400, 240); s = 150; x0, y0 = 60, 45
    c.add(f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="none" stroke="EDGE" stroke-width="1.4"/>')
    for t, col in ((0, "BLUE"), (1, "ACC"), (2, "BLUE")):
        # line x + y = t (in cell units), from top view: x right, y up
        pts = []
        for u in (-0.3, 1.3):
            v = t - u
            pts.append((x0 + u * s, y0 + s - v * s))
        line(c, pts[0], pts[1], col, 2.2)
    text(c, (x0 + s / 2, y0 + s + 22), "a", "TEXT", "middle")
    text(c, (x0 - 14, y0 + s / 2), "a", "TEXT", "middle")
    m1 = (x0 + 0.5 * s, y0 + s - 0.5 * s); m0 = (x0 + 0.25 * s, y0 + s - 0.25 * s)
    line(c, m0, m1, "HEAD", 1.6, head=True)
    text(c, (m0[0] - 6, m0[1] - 8), "d₁₁₀", "HEAD", "end", 13, "700")
    text(c, (285, 80), "view along z", "TEXT", "start", 12)
    text(c, (285, 102), "(1 1 0) planes", "ACC", "start", 12, "700")
    text(c, (285, 124), "d = a/√2", "HEAD", "start", 13, "700")
    REG.put("spacing", c, "Spacing between parallel (110) planes")


# ---------------------------------------------------------------- hexagonal cell
def hproj(p, cx, cy, s=95):
    X, Y, Z = p
    return (cx + X * s, cy - Z * s * 1.05 - Y * s * 0.48)


def hex_cell(c, cx, cy):
    """Hexagonal prism. a2 points right, a1 towards the viewer (down-left), a3 to the back (up-left)."""
    r3 = math.sqrt(3) / 2
    A = [(-0.5, -r3, 0), (1.0, 0.0, 0), (-0.5, r3, 0)]          # a1, a2, a3
    corners = [A[1], tuple(-t for t in A[2]), A[0], tuple(-t for t in A[1]), A[2], tuple(-t for t in A[0])]
    H = 1.2
    for z in (0, H):
        for i in range(6):
            p, q = corners[i], corners[(i + 1) % 6]
            back = (p[1] + q[1]) / 2 > 0.3
            line(c, hproj((p[0], p[1], z), cx, cy), hproj((q[0], q[1], z), cx, cy), dash="4,4" if (back and z == 0) else None, w=1.2)
    for p in corners:
        back = p[1] > 0.6
        line(c, hproj((p[0], p[1], 0), cx, cy), hproj((p[0], p[1], H), cx, cy), dash="4,4" if back else None, w=1.2)
    return A, corners


def fig_hex_axes():
    c = Canvas(600, 310); cx, cy = 170, 225
    A, corners = hex_cell(c, cx, cy)
    o = hproj((0, 0, 0), cx, cy)
    for v, name, col in ((A[0], "a₁", "PINK"), (A[1], "a₂", "PINK"), (A[2], "a₃", "PINK")):
        line(c, o, hproj(v, cx, cy), col, 2.4, head=True)
        text(c, hproj(v, cx, cy), name, col, "middle", 14, "700", dx=(12 if v[0] > 0 else -12), dy=(16 if v[1] < 0 else -4))
    line(c, o, hproj((0, 0, 1.2), cx, cy), "PINK", 2.4, head=True)
    text(c, hproj((0, 0, 1.2), cx, cy), "c", "PINK", "middle", 14, "700", dx=10, dy=-4)
    # the (0 1 -1 0) plane: through a2 (=+1 on a2) and -a3, parallel to a1 and c
    p, q = A[1], tuple(-t for t in A[2])
    quad = [(p[0], p[1], 0), (q[0], q[1], 0), (q[0], q[1], 1.2), (p[0], p[1], 1.2)]
    pts = " ".join(f"{fmt(x)},{fmt(y)}" for x, y in (hproj(t, cx, cy) for t in quad))
    c.add(f'<polygon points="{pts}" fill="ACC" fill-opacity="0.28" stroke="ACC" stroke-width="1.8"/>')
    text(c, (380, 70), "4 axes: a₁, a₂, a₃ (120° apart, in the base)", "TEXT", "start", 12)
    text(c, (380, 90), "and c (vertical)", "TEXT", "start", 12)
    text(c, (380, 130), "shaded face:", "ACC", "start", 13, "700")
    text(c, (380, 150), "a₁ = ∞, a₂ = 1, a₃ = −1, c = ∞", "TEXT", "start", 12)
    text(c, (380, 172), label("(0 1 -1 0)") + " ≡ " + label("(0 1 0)"), "ACC", "start", 15, "700")
    text(c, (380, 194), "check: i = −(h + k) = −(0 + 1) = −1", "TEXT", "start", 12)
    REG.put("hex-axes", c, "Hexagonal cell: the four axes and the (0 1 -1 0) plane")


def fig_hex_dirs():
    c = Canvas(640, 310); cx, cy = 190, 225
    A, corners = hex_cell(c, cx, cy)
    o = hproj((0, 0, 0), cx, cy)
    for v, name, col, d in ((A[0], label("[2 -1 -1 0]") + " = [1 0 0]", "ACC", (-30, 22)),
                            (tuple(-t for t in A[2]), label("[1 1 -2 0]") + " = [1 1 0]", "BLUE", (70, 20)),
                            ((0, 0, 1.2), "[0 0 0 1] = [0 0 1]", "GREEN", (0, -10))):
        line(c, o, hproj(v, cx, cy), col, 2.6, head=True)
        text(c, hproj(v, cx, cy), name, col, "middle", 13, "700", dx=d[0], dy=d[1])
    text(c, (400, 70), "[1 0 0] → h = ⅓(2·1 − 0) = ⅔", "TEXT", "start", 12)
    text(c, (400, 90), "k = ⅓(2·0 − 1) = −⅓,  i = −⅓(1 + 0) = −⅓", "TEXT", "start", 12)
    text(c, (400, 110), "×3 → " + label("[2 -1 -1 0]"), "ACC", "start", 13, "700")
    text(c, (400, 145), "[1 1 0] → h = ⅓, k = ⅓, i = −⅔", "TEXT", "start", 12)
    text(c, (400, 165), "×3 → " + label("[1 1 -2 0]"), "BLUE", "start", 13, "700")
    REG.put("hex-dirs", c, "Directions in the hexagonal cell in 4-index notation")


# ---------------------------------------------------------------- unit cells and structures
def fig_cells():
    c = panel_row(3, 250, 255)
    sets = [("BCC", [(0.5, 0.5, 0.5)], "2 atoms/cell, CN = 8"),
            ("FCC", [(0.5, 0.5, 0), (0.5, 0.5, 1), (0.5, 0, 0.5), (0.5, 1, 0.5), (0, 0.5, 0.5), (1, 0.5, 0.5)], "4 atoms/cell, CN = 12"),
            ("simple cubic", [], "1 atom/cell")]
    order = [2, 0, 1]
    for i, j in enumerate(order):
        name, extra, sub = sets[j]
        ox = i * 250; cx, cy = ox + 120, 180
        cube(c, cx, cy, axes=False)
        for p in CUBE_V:
            dot(c, proj(p, cx, cy), 6, "ATOM")
        for p in extra:
            dot(c, proj(p, cx, cy), 6, "BLUE")
        if name == "BCC":
            line(c, proj((1, 0, 0), cx, cy), proj((0, 1, 1), cx, cy), "BLUE", 1.2, "3,3")
        caption(c, ox + 125, 236, name, size=14)
        text(c, (ox + 125, 254), sub, "TEXT", "middle", 12)
    REG.put("cells", c, "Simple cubic, BCC and FCC unit cells")


def fig_bcc_fcc_geometry():
    c = panel_row(2, 290, 250)
    # BCC: body diagonal 4R = sqrt(3) a
    cx, cy = 125, 180
    cube(c, cx, cy, axes=False)
    line(c, proj((1, 0, 0), cx, cy), proj((0, 1, 1), cx, cy), "ACC", 2.4)
    for t in (0, 0.5, 1):
        p = tuple(1 - t if i == 0 else t for i in range(3))
        dot(c, proj(p, cx, cy), 7, "ACC")
    text(c, (145, 236), "BCC: body diagonal = 4R = √3·a", "HEAD", "middle", 13, "700")
    # FCC: face diagonal 4R = sqrt(2) a
    cx2 = 290 + 125
    cube(c, cx2, cy, axes=False)
    line(c, proj((1, 0, 0), cx2, cy), proj((1, 1, 1), cx2, cy), "BLUE", 2.4)
    for t in (0, 0.5, 1):
        dot(c, proj((1, t, t), cx2, cy), 7, "BLUE")
    text(c, (290 + 145, 236), "FCC: face diagonal = 4R = √2·a", "HEAD", "middle", 13, "700")
    REG.put("touching", c, "Where the atoms touch in BCC and FCC")


def fig_stacking():
    c = Canvas(560, 200); r = 16
    def layer(x0, y0, off, col, n=5, rows=1):
        for i in range(n):
            c.add(f'<circle cx="{fmt(x0 + off + i * 2 * r)}" cy="{fmt(y0)}" r="{r}" fill="{col}" fill-opacity="0.55" stroke="{col}"/>')
    # side views of stacked rows
    for k, (lab, seq) in enumerate((("HCP: A B A B …", "ABAB"), ("FCC: A B C A B C …", "ABCA"))):
        x0 = 40 + k * 280
        cols = {"A": "ACC", "B": "BLUE", "C": "GREEN"}
        offs = {"A": 0, "B": r, "C": 2 * r}
        for j, L_ in enumerate(seq):
            layer(x0, 150 - j * 28, offs[L_] * 0.66, cols[L_])
            text(c, (x0 - 18, 155 - j * 28), L_, cols[L_], "middle", 13, "700")
        text(c, (x0 + 90, 190), lab, "HEAD", "middle", 13, "700")
    REG.put("stacking", c, "Stacking sequences of close-packed planes")


def fig_interstitial():
    c = panel_row(2, 290, 255)
    cx, cy = 125, 180
    cube(c, cx, cy, axes=False)
    fcc = list(CUBE_V) + [(0.5, 0.5, 0), (0.5, 0.5, 1), (0.5, 0, 0.5), (0.5, 1, 0.5), (0, 0.5, 0.5), (1, 0.5, 0.5)]
    for p in fcc:
        dot(c, proj(p, cx, cy), 5, "ATOM")
    for p in [(0.5, 0.5, 0.5)] + [e for e in itertools.product((0, 0.5, 1), repeat=3) if sorted(e).count(0.5) == 1 and all(t in (0, 1, 0.5) for t in e)]:
        if sum(1 for t in p if t == 0.5) in (1, 3):
            dot(c, proj(p, cx, cy), 4, "BLUE", "none")
    text(c, (145, 236), "FCC octahedral sites:", "HEAD", "middle", 13, "700")
    text(c, (145, 253), "centre (1) + 12 edges × ¼ = 4", "TEXT", "middle", 12)
    cx2 = 290 + 125
    cube(c, cx2, cy, axes=False)
    for p in fcc:
        dot(c, proj(p, cx2, cy), 5, "ATOM")
    for p in itertools.product((0.25, 0.75), repeat=3):
        dot(c, proj(p, cx2, cy), 4, "GREEN", "none")
    text(c, (290 + 145, 236), "FCC tetrahedral sites:", "HEAD", "middle", 13, "700")
    text(c, (290 + 145, 253), "8 inside the cell = 8", "TEXT", "middle", 12)
    REG.put("interstitial", c, "Octahedral and tetrahedral interstitial sites in FCC")


def fig_density():
    c = panel_row(3, 250, 255)
    # [100] in FCC
    cx, cy = 120, 180
    cube(c, cx, cy, axes=False)
    line(c, proj((0, 0, 0), cx, cy), proj((1, 0, 0), cx, cy), "ACC", 3)
    for p in ((0, 0, 0), (1, 0, 0)):
        dot(c, proj(p, cx, cy), 7, "ACC")
    text(c, (125, 236), "[1 0 0] in FCC", "HEAD", "middle", 13, "700")
    text(c, (125, 253), "2 × ½ = 1 atom over length a", "TEXT", "middle", 12)
    # (100) face in FCC
    cx2 = 250 + 120
    cube(c, cx2, cy, axes=False)
    plane(c, cx2, cy, (1, 0, 0), "BLUE", mark_intercepts=False)
    for p in ((1, 0, 0), (1, 1, 0), (1, 0, 1), (1, 1, 1)):
        dot(c, proj(p, cx2, cy), 6, "BLUE")
    dot(c, proj((1, 0.5, 0.5), cx2, cy), 7, "BLUE")
    text(c, (250 + 125, 236), "(1 0 0) face in FCC", "HEAD", "middle", 13, "700")
    text(c, (250 + 125, 253), "1 + 4 × ¼ = 2 atoms over area a²", "TEXT", "middle", 12)
    # [111] in FCC: only the two corners lie on the body diagonal
    cx3 = 500 + 120
    cube(c, cx3, cy, axes=False)
    for p in [(0.5, 0.5, 0), (0.5, 0.5, 1), (0.5, 0, 0.5), (0.5, 1, 0.5), (0, 0.5, 0.5), (1, 0.5, 0.5)]:
        dot(c, proj(p, cx3, cy), 4, "EDGE", "none")
    line(c, proj((0, 0, 0), cx3, cy), proj((1, 1, 1), cx3, cy), "GREEN", 3)
    for p in ((0, 0, 0), (1, 1, 1)):
        dot(c, proj(p, cx3, cy), 7, "GREEN")
    text(c, (500 + 125, 236), "[1 1 1] in FCC", "HEAD", "middle", 13, "700")
    text(c, (500 + 125, 253), "only 2 × ½ = 1 atom over √3·a", "TEXT", "middle", 12)
    REG.put("density", c, "Linear and planar density examples in FCC")


def build():
    for f in (fig_positions, fig_dir_basic, fig_dir_reduce, fig_dir_negative, fig_dir_read, fig_dir_family,
              fig_plane_basic, fig_plane_more, fig_plane_negative, fig_plane_family, fig_plane_normal, fig_spacing,
              fig_hex_axes, fig_hex_dirs, fig_cells, fig_bcc_fcc_geometry, fig_stacking, fig_interstitial, fig_density):
        f()
    return REG


if __name__ == "__main__":
    print("\n".join(build().write()))
