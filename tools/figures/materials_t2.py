"""Topic 2 figures for Aerospace Materials I (cubic directions and planes, hexagonal cell, cells, densities).

Figures that reproduce the slides are PNG crops registered with REG.raster; the remaining SVGs are portal
drawings that are not in the slides (EXTRA).

Planes are clipped exactly to the unit cube and directions start at O' (a 1 where an index is negative),
so the drawings follow the construction rules of the topic. Run `python tools/build_topic_pages.py` to
write the SVG files to vault/attachments/T2 and rebuild the page.
"""
import itertools
import math

from figures.svgkit import Canvas, Registry, dot, fmt, line, overline_label as label, text

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




# ============================================================================ figures (portal drawings, not in the slides)
def dir_panel(c, ox, items, title):
    cx, cy = ox + 120, 180
    cube(c, cx, cy)
    for ind, col, lab, lp in items:
        o, tip = direction(c, cx, cy, ind, col)
        t = proj(tip, cx, cy)
        text(c, t, lab, col, "middle", 14, "700", dx=lp[0], dy=lp[1])
    caption(c, ox + 125, 242, title, size=13)


def plane_panel(c, ox, hkl, title, sub=None, col="ACC", origin=None, w=255):
    cx, cy = ox + 120, 180
    cube(c, cx, cy)
    plane(c, cx, cy, hkl, col, origin)
    caption(c, ox + w / 2, 240, title, size=14)
    if sub:
        text(c, (ox + w / 2, 258), sub, "TEXT", "middle", 12)


def P(h, k, l):
    return label(f"({h} {k} {l})")


def fig_dir_reduce_extra():
    c = panel_row(1, 255, 250)
    dir_panel(c, 0, [((1, 2, 2), "GREEN", label("[1 2 2]"), (14, -6))], "½[1 2 2] → tip at (½, 1, 1)")
    REG.put("dir-reduce-extra", c, "Direction [122]",
            "The direction [1 2 2] reduced to ½[1 2 2] = [½, 1, 1] and drawn from the origin. Portal drawing, not in the slides (EXTRA).")


def fig_dir_family_extra():
    c = panel_row(1, 280, 255)
    cx, cy = 125, 180
    cube(c, cx, cy)
    for ind, col in (((1, 0, 0), "ACC"), ((0, 1, 0), "BLUE"), ((0, 0, 1), "GREEN")):
        direction(c, cx, cy, ind, col, show_origin=False)
    caption(c, 130, 245, "the cube edges &lt;1 0 0&gt;", size=13)
    REG.put("dir-family-extra", c, "The family &lt;100&gt;",
            "The cube edges [100], [010] and [001] of the family &lt;100&gt;. Portal drawing, not in the slides (EXTRA).")


def fig_plane_basic_extra():
    c = panel_row(1, 255, 265)
    plane_panel(c, 0, (1, 0, 0), P(1, 0, 0), "intercepts x = 1, y = ∞, z = ∞")
    REG.put("plane-basic-extra", c, "Plane (100)",
            "Plane (100): intercept x = 1, parallel to y and z, the front face of the cube. Portal drawing, not in the slides (EXTRA).")


def fig_plane_more_extra():
    c = panel_row(2, 255, 265)
    plane_panel(c, 0, (2, 1, 0), P(2, 1, 0), "x = ½, y = 1, z = ∞", "BLUE")
    plane_panel(c, 255, (0, 1, 1), P(0, 1, 1), "x = ∞, y = 1, z = 1", "GREEN")
    REG.put("plane-more-extra", c, "Planes (210) and (011)",
            "Planes (210) and (011) in the cubic cell, with their intercepts. Portal drawing, not in the slides (EXTRA).")


def fig_plane_family_extra():
    c = panel_row(1, 280, 265)
    cx, cy = 125, 180
    cube(c, cx, cy)
    plane(c, cx, cy, (1, 1, 1), "ACC", mark_intercepts=False)
    plane(c, cx, cy, (-1, 1, 1), "BLUE", mark_intercepts=False)
    caption(c, 130, 245, "two members of {1 1 1}", size=13)
    REG.put("plane-family-extra", c, "Two members of the family {111}",
            "The planes (111) and (-111), two of the eight members of the family {111}. Portal drawing, not in the slides (EXTRA).")


def fig_plane_normal():
    c = Canvas(300, 255); cx, cy = 130, 180
    cube(c, cx, cy)
    plane(c, cx, cy, (1, 1, 1), "BLUE", mark_intercepts=False)
    direction(c, cx, cy, (1, 1, 1), "ACC", show_origin=True)
    text(c, proj((1, 1, 1), cx, cy), label("[1 1 1]"), "ACC", "middle", 14, "700", dx=16, dy=-4)
    text(c, proj((0.33, 0.9, 0.2), cx, cy), P(1, 1, 1), "BLUE", "middle", 14, "700", dx=8, dy=26)
    REG.put("plane-normal", c, "In a cube the [111] direction is perpendicular to the (111) plane",
            "In a cubic cell the direction [111] is perpendicular to the plane (111). Portal drawing of the rule stated on Session 3 Slide 45, not in the slides (EXTRA).")


def fig_density_extra():
    c = panel_row(2, 250, 255)
    # [100] in FCC
    cx, cy = 120, 180
    cube(c, cx, cy, axes=False)
    line(c, proj((0, 0, 0), cx, cy), proj((1, 0, 0), cx, cy), "ACC", 3)
    for p in ((0, 0, 0), (1, 0, 0)):
        dot(c, proj(p, cx, cy), 7, "ACC")
    text(c, (125, 236), "[1 0 0] in FCC", "HEAD", "middle", 13, "700")
    text(c, (125, 253), "2 × ½ = 1 atom over length a", "TEXT", "middle", 12)
    # [111] in FCC: only the two corners lie on the body diagonal
    cx3 = 250 + 120
    cube(c, cx3, cy, axes=False)
    for p in [(0.5, 0.5, 0), (0.5, 0.5, 1), (0.5, 0, 0.5), (0.5, 1, 0.5), (0, 0.5, 0.5), (1, 0.5, 0.5)]:
        dot(c, proj(p, cx3, cy), 4, "EDGE", "none")
    line(c, proj((0, 0, 0), cx3, cy), proj((1, 1, 1), cx3, cy), "GREEN", 3)
    for p in ((0, 0, 0), (1, 1, 1)):
        dot(c, proj(p, cx3, cy), 7, "GREEN")
    text(c, (250 + 125, 236), "[1 1 1] in FCC", "HEAD", "middle", 13, "700")
    text(c, (250 + 125, 253), "only 2 × ½ = 1 atom over √3·a", "TEXT", "middle", 12)
    REG.put("density-extra", c, "Linear density along [100] and [111] in FCC",
            "Atoms whose centres lie on the [100] edge and on the [111] body diagonal of an FCC cell: 2 × ½ = 1 atom in both cases (no atom at the cube centre in FCC, see the note on the official material). Portal drawing, not in the slides (EXTRA).")


# ---------------------------------------------------------------- slide crops (not generated here)
def rasters():
    R = REG.raster
    R('stacking', 'Stacking sequences of close-packed layers',
      'Stacking of close-packed layers: A B A B ... gives hexagonal close packing (HCP, left) and A B C A B C ... gives face-centred cubic packing (FCC, right). Copied from Session 3 Slide 22', 380)
    R('cells', 'BCC, FCC and HCP unit cells',
      'Unit cells of the three main metallic structures: body-centred cubic (BCC), face-centred cubic (FCC) and hexagonal close-packed (HCP). Copied from Session 3 Slide 25', 700)
    R('touching-a', 'BCC reduced-sphere and hard-sphere cells',
      'BCC: reduced-sphere cell with the face diagonal d and the edge a, and hard-sphere cell with the body diagonal along which the atoms touch, 4R = √3·a. Copied from Session 3 Slide 26', 560)
    R('touching-b', 'FCC reduced-sphere and hard-sphere cells',
      'FCC: reduced-sphere cell with the face diagonal d and the edge a, and hard-sphere cell where the atoms touch along the face diagonal, 4R = √2·a. Copied from Session 3 Slide 27', 560)
    R('interstitial', 'Tetrahedral and octahedral sites in FCC',
      'Interstitial sites in the FCC cell: tetrahedral sites (left) and octahedral sites (right), with the metal atoms and the interstitial atoms. Copied from Session 3 Slide 31', 720)
    R('positions', 'Atomic positions in a cubic cell',
      'Atomic positions in a cubic cell, with the corners (0,0,1), (0,1,1) and (0,1,0) labelled. Copied from Session 3 Slide 37', 360)
    R('dir-basic', 'Directions drawn in the cubic cell',
      'Directions drawn from the origin of the cubic cell: [100] and [110] (first cube), [111], [210] and [-110] (bar over the first 1). Copied from Session 3 Slide 39', 760)
    R('dir-reduce-a', 'Direction [012]',
      'Example 1 of the slide: the direction [012] reduced to ½[0 1 2] = [0, ½, 1], drawn from the origin; the red arrow is the direction [110]. Copied from Session 3 Slide 39', 360)
    R('dir-negative', 'Directions with negative indices',
      'The directions [-111], [1-10] and [02-1] (bar over the negative index) drawn in one cube, each from its new origin O\' = (1,0,0), (0,1,0) and (0,0,1). Copied from Session 3 Slide 40', 420)
    R('dir-read-a', 'Reading the indices of a drawn direction: [1-11]',
      'A vector from (0,1,0) to (1,0,1): head minus tail gives (1, -1, 1), the direction [1-11]. Copied from Session 3 Slide 41', 340)
    R('dir-read-b', 'Reading the indices of a drawn direction: [0-1-1]',
      'A vector from (0,1,1) to the origin: head minus tail gives (0, -1, -1), the direction [0-1-1]. Copied from Session 3 Slide 41', 480)
    R('dir-family-a', 'The family <111>',
      'The four body diagonals of the cube, the family <111>. Copied from Session 3 Slide 42', 400)
    R('plane-basic-a', 'Plane (110)',
      'Plane (110): intersections a = 1, b = 1, c = ∞. Copied from Session 3 Slide 45', 360)
    R('plane-basic-b', 'Plane (111)',
      'Plane (111): intersections a = 1, b = 1, c = 1. Copied from Session 3 Slide 45', 360)
    R('plane-more-a', 'Plane (200)',
      'Plane (200): intersections a = ½, b = ∞, c = ∞. Copied from Session 3 Slide 45', 360)
    R('plane-negative', 'Planes with negative indices',
      'Planes (-100), (1-10), (1-1-1) and (-211) with their new origins O\' and intersections; the slide prints the last one as (2 1 1), but its intersection a = −½ shows the bar over the 2. Copied from Session 3 Slide 49', 760)
    R('plane-family', 'The family {100}',
      'The six cube faces, one shaded in each cube, form the family {100}. Copied from Session 3 Slide 50', 620)
    R('spacing', 'Spacing between (110) planes',
      'Parallel (110) planes seen along z, with their spacing d110. Copied from Session 3 Slide 53', 340)
    R('hex-axes', 'Axes of the hexagonal cell',
      'Hexagonal cell with the axes a1, a2, a3 (120° apart in the base) and c, and the shaded side face (01-10) ≡ (010). Copied from Session 3 Slide 51', 460)
    R('hex-dirs', 'Directions in the hexagonal cell',
      'Directions in the hexagonal cell: [2-1-10] along a1 (= [100] in three indices), [11-20] (= [110]), [0001] along c, and [1-211]; the short arrows labelled [100] and [110] are the three-index vectors. Copied from Session 3 Slide 52', 480)
    R('density-b', 'The (100) plane of FCC copper',
      'Planar density in FCC copper: the (100) face holds one central atom and four corner atoms shared by four faces, 2 atoms over the area a². Copied from Session 4 Slide 9', 340)


def build():
    for f in (fig_dir_reduce_extra, fig_dir_family_extra, fig_plane_basic_extra, fig_plane_more_extra,
              fig_plane_family_extra, fig_plane_normal, fig_density_extra, rasters):
        f()
    return REG


if __name__ == "__main__":
    print("\n".join(build().write()))
