"""Engineering-drawing primitives for the Engineering Mechanics figures (pure stdlib, built on svgkit).

A `Scene` maps world coordinates (x to the right, y up, any length unit) to SVG pixels, so a figure is written
in the units of the problem and every angle is the mathematical one (degrees, counter-clockwise from +x).
Colour tokens are the ones of svgkit ("EDGE", "TEXT", "HEAD", "ACC", "BLUE", "PINK", "GREEN"), which become CSS
variables on the web and fixed colours in the vault copy.

Conventions used by every figure of the bank:
  * HEAD  solid bodies, fixed supports, frames drawn as thick lines
  * BLUE  coordinate axes and vectors of the problem (positions, velocities, accelerations)
  * PINK  forces
  * GREEN angles and angular rates
  * EDGE  construction lines (dashed), hatching, dimension lines
  * ACC   particles (filled)

`Scene.report()` lists labels that overlap each other or leave the canvas, so a figure can be checked before it is
looked at (the visual inspection is still done on a rendered PNG).
"""
import math

from figures.svgkit import Canvas, arrow_head, fmt, line, poly, circle, pathd

SERIF = "Newsreader, 'Times New Roman', Times, serif"   # Times has lining numerals (Georgia's old-style 0 and 1 read as o and l)


def S(base, sub=None, sup=None):
    """Label text with an optional subscript and/or superscript: S('v', 'A') -> v_A."""
    out = base
    if sub is not None:
        out += f'<tspan baseline-shift="sub" font-size="70%">{sub}</tspan>'
    if sup is not None:
        out += f'<tspan baseline-shift="super" font-size="70%">{sup}</tspan>'
    return out


def dot1(ch):
    """Letter with a dot over it (first time derivative)."""
    return ch + "̇"


def dot2(ch):
    """Letter with two dots over it (second time derivative)."""
    return ch + "̈"


def bold(s):
    return f'<tspan font-weight="700" font-style="normal">{s}</tspan>'


def _plain_len(s):
    import re
    return len(re.sub(r"<[^>]+>", "", s).replace("&amp;", "&"))


class Scene:
    def __init__(self, w, h, origin, k):
        """w, h: canvas size in px; origin: pixel position of world (0, 0); k: pixels per world unit."""
        self.c = Canvas(w, h)
        self.w, self.h, self.o, self.k = w, h, origin, k
        self.boxes = []          # (name, x0, y0, x1, y1) of every label, for the overlap report

    # ---- geometry -----------------------------------------------------------------------
    def P(self, x, y=None):
        if y is None:
            x, y = x
        return (self.o[0] + self.k * x, self.o[1] - self.k * y)

    # ---- text ---------------------------------------------------------------------------
    def label(self, p, s, col="HEAD", anchor="middle", size=17, italic=True, weight="400", dx=0, dy=0):
        """Text at a world point (shifted by dx, dy pixels)."""
        x, y = self.P(p)
        x, y = x + dx, y + dy
        style = ' font-style="italic"' if italic else ""
        self.c.add(f'<text x="{x:.1f}" y="{y:.1f}" fill="{col}" font-size="{size}" font-weight="{weight}" '
                   f'text-anchor="{anchor}" font-family="{SERIF}" style="font-variant-numeric:lining-nums"{style}>{s}</text>')
        width = _plain_len(s) * 0.52 * size
        x0 = x - width / 2 if anchor == "middle" else (x if anchor == "start" else x - width)
        self.boxes.append((s, x0, y - 0.8 * size, x0 + width, y + 0.25 * size))

    def note(self, p, s, col="TEXT", anchor="start", size=13, dx=0, dy=0):
        """Upright small text (data, remarks) in the sans font."""
        self.label(p, s, col=col, anchor=anchor, size=size, italic=False, dx=dx, dy=dy)

    def report(self):
        """Warnings: label boxes that overlap, or that fall outside the canvas."""
        out = []
        for i, a in enumerate(self.boxes):
            if a[1] < 0 or a[3] > self.c.w or a[2] < 0 or a[4] > self.c.h:
                out.append(f"label {a[0]!r} leaves the canvas")
            for b in self.boxes[i + 1:]:
                if a[1] < b[3] and b[1] < a[3] and a[2] < b[4] and b[2] < a[4]:
                    out.append(f"labels {a[0]!r} and {b[0]!r} overlap")
        return out

    # ---- lines and bodies ---------------------------------------------------------------
    def line(self, a, b, col="HEAD", w=1.6, dash=None):
        line(self.c, self.P(a), self.P(b), col, w, dash)

    def poly(self, pts, col="HEAD", w=1.6, dash=None, fill="none", close=False, opacity=None):
        poly(self.c, [self.P(p) for p in pts], col, w, dash, fill, close, opacity)

    def rod(self, a, b, w=4.0, col="HEAD"):
        """Rigid massless bar between two points."""
        self.line(a, b, col, w)

    def string(self, pts, col="EDGE", w=1.5, dash=None):
        self.poly(pts, col, w, dash)

    def dashed(self, a, b, col="EDGE"):
        self.line(a, b, col, 1.1, "5 4")

    def circle(self, c, r, col="HEAD", w=1.8, dash=None, fill="none", opacity=None):
        circle(self.c, self.P(c), r * self.k, col, w, dash, fill, opacity)

    def disk(self, c, r, col="HEAD", fill="HEAD", opacity=0.10, w=2.0):
        """Cylinder, spool or pulley seen along its axis, with its centre marked."""
        self.circle(c, r, col, w, fill=fill, opacity=opacity)
        self.dotp(c, 3.0, col)

    def dotp(self, p, r=3.5, col="HEAD"):
        x, y = self.P(p)
        self.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>')

    def mass(self, p, name=None, r=7.5, name_off=(12, -12), col="ACC", size=17):
        """Particle: filled disk with an outline, optionally labelled."""
        x, y = self.P(p)
        self.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}" fill-opacity="0.95" stroke="HEAD" stroke-width="1.6"/>')
        if name:
            self.label(p, name, "HEAD", "middle", size, dx=name_off[0], dy=name_off[1])

    def ground(self, a, b, side=-1, step=9, length=9, col="EDGE"):
        """Solid wall along a-b with hatching on the given side (-1: below/right of a->b in world, 1: above/left)."""
        self.line(a, b, "HEAD", 2.4)
        ax, ay = self.P(a)
        bx, by = self.P(b)
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy)
        tx, ty = dx / L, dy / L
        # screen normal pointing to the world side requested
        nx, ny = (ty, -tx) if side > 0 else (-ty, tx)
        k = 0.0
        while k <= L:
            px, py = ax + tx * k, ay + ty * k
            line(self.c, (px, py), (px + (nx - tx) * length * 0.7071, py + (ny - ty) * length * 0.7071), col, 1.0)
            k += step

    def pivot(self, p, size=0.30, hatch_w=0.55, down=True):
        """Fixed pin support: pin circle, triangle and hatched base."""
        x, y = self.P(p)
        s = size * self.k
        sgn = 1 if down else -1
        base_y = y + sgn * s * 1.35
        pts = [(x, y), (x - s * 0.8, base_y), (x + s * 0.8, base_y)]
        self.c.add(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" stroke="HEAD" stroke-width="1.8" stroke-linejoin="round"/>')
        half = hatch_w * self.k / 2
        line(self.c, (x - half, base_y), (x + half, base_y), "HEAD", 2.2)
        k = -half
        while k <= half:
            line(self.c, (x + k, base_y), (x + k - 7, base_y + sgn * 8), "EDGE", 1.0)
            k += 8
        self.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2" fill="var(--bg-surface, #ffffff)" stroke="HEAD" stroke-width="1.8"/>'.replace("var(--bg-surface, #ffffff)", "none"))

    def pin(self, p, r=4.2):
        x, y = self.P(p)
        self.c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="none" stroke="HEAD" stroke-width="1.8"/>')

    def spring(self, a, b, coils=7, amp=7.0, col="HEAD", lead=0.12, w=1.5):
        """Zigzag spring from a to b (world points); the first and last `lead` fraction are straight."""
        ax, ay = self.P(a)
        bx, by = self.P(b)
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy)
        tx, ty = dx / L, dy / L
        nx, ny = -ty, tx
        pts = [(ax, ay), (ax + tx * L * lead, ay + ty * L * lead)]
        n = coils * 2
        span = L * (1 - 2 * lead)
        for i in range(n):
            f = (i + 0.5) / n
            s = amp if i % 2 == 0 else -amp
            pts.append((ax + tx * (L * lead + span * f) + nx * s, ay + ty * (L * lead + span * f) + ny * s))
        pts += [(bx - tx * L * lead, by - ty * L * lead), (bx, by)]
        poly(self.c, pts, col, w)

    def damper(self, a, b, col="HEAD", w=1.6, width=9):
        """Dashpot: a cylinder with a piston rod, along a-b."""
        ax, ay = self.P(a)
        bx, by = self.P(b)
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy)
        tx, ty = dx / L, dy / L
        nx, ny = -ty, tx
        m1 = (ax + tx * L * 0.45, ay + ty * L * 0.45)
        m2 = (ax + tx * L * 0.62, ay + ty * L * 0.62)
        line(self.c, (ax, ay), m1, col, w)
        line(self.c, (m1[0] + nx * width, m1[1] + ny * width), (m1[0] - nx * width, m1[1] - ny * width), col, w)
        poly(self.c, [(m2[0] + tx * 0 + nx * width * 1.4 - tx * L * 0.3, m2[1] + ny * width * 1.4 - ty * L * 0.3),
                      (m2[0] + nx * width * 1.4, m2[1] + ny * width * 1.4),
                      (m2[0] - nx * width * 1.4, m2[1] - ny * width * 1.4),
                      (m2[0] - nx * width * 1.4 - tx * L * 0.3, m2[1] - ny * width * 1.4 - ty * L * 0.3)], col, w)
        line(self.c, m2, (bx, by), col, w)

    # ---- axes, vectors, angles ----------------------------------------------------------
    def vec(self, a, b, name=None, col="BLUE", w=2.0, name_off=(8, -8), size=16, head=9):
        """Arrow from world point a to b; the label sits near the tip, shifted by name_off pixels."""
        ax, ay = self.P(a)
        bx, by = self.P(b)
        ang = math.atan2(by - ay, bx - ax)
        tip = (bx - head * 0.6 * math.cos(ang), by - head * 0.6 * math.sin(ang))
        line(self.c, (ax, ay), tip, col, w)
        arrow_head(self.c, (ax, ay), (bx, by), col, head)
        if name:
            self.label(b, name, col, "middle", size, weight="700", dx=name_off[0], dy=name_off[1])

    def axes(self, o, angle=0.0, length=1.0, names=("x", "y"), col="BLUE", origin_name=None, name_off=(10, 6)):
        """Two orthogonal axes at world point o, rotated by `angle` degrees."""
        a = math.radians(angle)
        for i, nm in enumerate(names):
            th = a + i * math.pi / 2
            tip = (o[0] + length * math.cos(th), o[1] + length * math.sin(th))
            dx = name_off[0] * math.cos(th) + (0 if i else 0)
            self.vec(o, tip, nm, col, 1.9, name_off=(10 * math.cos(th), -10 * math.sin(th) + 4), size=16)
        if origin_name:
            self.label(o, origin_name, col, "end", 16, dx=-8, dy=16)

    def arc(self, c, r, a0, a1, col="GREEN", w=1.5, dash=None, head=False):
        """Circular arc about world point c, from angle a0 to a1 (degrees, counter-clockwise positive)."""
        r_px = r * self.k
        cx, cy = self.P(c)
        p0 = (cx + r_px * math.cos(math.radians(a0)), cy - r_px * math.sin(math.radians(a0)))
        p1 = (cx + r_px * math.cos(math.radians(a1)), cy - r_px * math.sin(math.radians(a1)))
        large = 1 if abs(a1 - a0) > 180 else 0
        sweep = 0 if a1 > a0 else 1
        pathd(self.c, f"M{p0[0]:.1f},{p0[1]:.1f} A{r_px:.1f},{r_px:.1f} 0 {large} {sweep} {p1[0]:.1f},{p1[1]:.1f}", col, w, dash)
        if head:
            sgn = 1 if a1 > a0 else -1
            ra = math.radians(a1)
            tx, ty = -math.sin(ra) * sgn, -math.cos(ra) * sgn          # screen tangent at the end
            arrow_head(self.c, (p1[0] - tx * 4, p1[1] - ty * 4), (p1[0] + tx * 3, p1[1] + ty * 3), col, 9)

    def angle(self, c, r, a0, a1, name, col="GREEN", name_r=None, size=16):
        """Angle mark between rays at a0 and a1 with its name just outside the arc."""
        self.arc(c, r, a0, a1, col, 1.5)
        mid = math.radians((a0 + a1) / 2)
        rr = (name_r if name_r is not None else r * 1.38)
        self.label((c[0] + rr * math.cos(mid), c[1] + rr * math.sin(mid)), name, col, "middle", size, dy=5)

    def spin(self, c, r, a0, a1, name, col="GREEN", name_r=None, size=16):
        """Curved arrow (rotation rate) about c from a0 to a1, with its name."""
        self.arc(c, r, a0, a1, col, 1.8, head=True)
        mid = math.radians((a0 + a1) / 2)
        rr = (name_r if name_r is not None else r * 1.3)
        self.label((c[0] + rr * math.cos(mid), c[1] + rr * math.sin(mid)), name, col, "middle", size, weight="700", dy=5)

    def dim(self, a, b, name, off=(0, 0), col="EDGE", size=15, gap=0.0):
        """Dimension line with arrowheads at both ends; the label is at the middle shifted by `off` pixels."""
        ax, ay = self.P(a)
        bx, by = self.P(b)
        line(self.c, (ax, ay), (bx, by), col, 1.1)
        arrow_head(self.c, (bx, by), (ax, ay), col, 7)
        arrow_head(self.c, (ax, ay), (bx, by), col, 7)
        mid = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        self.label(mid, name, "TEXT", "middle", size, dx=off[0], dy=off[1])

    def gravity(self, p, length=0.8, name="g"):
        """Gravity arrow pointing down with its label."""
        self.vec(p, (p[0], p[1] - length), name, "TEXT", 1.8, name_off=(12, 4), size=17)

    def curve(self, fn, t0, t1, n=120, col="HEAD", w=2.2, dash=None):
        """Parametric curve fn(t) -> (x, y) in world coordinates."""
        pts = [fn(t0 + (t1 - t0) * i / n) for i in range(n + 1)]
        self.poly(pts, col, w, dash)

    def svg(self, title):
        return self.c.svg(title)
