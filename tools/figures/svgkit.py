"""Small SVG toolkit shared by the topic figure modules (pure stdlib).

A figure is drawn with colour tokens ("EDGE", "TEXT", "HEAD", "ACC", "BLUE", "PINK", "GREEN", "ATOM").
`Registry.put` writes the vault copy with fixed colours (readable on light and dark Obsidian themes)
to vault/attachments/<folder>/<name>.svg and keeps a web copy that uses the portal's CSS variables.
"""
import math
import re
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[2]
FIXED = {"EDGE": "#8a94a6", "TEXT": "#6b7280", "HEAD": "#4b5563", "ACC": "#f59e0b", "BLUE": "#3b82f6",
         "PINK": "#ec4899", "GREEN": "#10b981", "ATOM": "#f59e0b"}
# Web copies: the colours are CSS variables with the screen colour as fallback, so the print layout
# (assets/css/print.css) can map them to black and greys that survive black-and-white printing.
WEB = {"EDGE": "var(--text-faint)", "TEXT": "var(--text-muted)", "HEAD": "var(--text-heading)",
       "ACC": "var(--fig-acc, #f59e0b)", "BLUE": "var(--fig-blue, #3b82f6)", "PINK": "var(--fig-pink, #ec4899)",
       "GREEN": "var(--fig-green, #10b981)", "ATOM": "var(--fig-atom, #f59e0b)"}


def fmt(v):
    return f"{v:.1f}"


class Canvas:
    def __init__(self, w, h):
        self.w, self.h, self.parts = w, h, []

    def add(self, s):
        self.parts.append(s)

    def text_right(self):
        """Rough right edge of the widest text label (labels near the edge must not be clipped)."""
        right = 0
        for part in self.parts:
            m = re.match(r'<text x="([-\d.]+)" [^>]*font-size="([\d.]+)"[^>]*text-anchor="(\w+)"[^>]*>(.*)</text>$', part)
            if not m:
                continue
            x, size, anchor = float(m.group(1)), float(m.group(2)), m.group(3)
            width = len(re.sub(r"<[^>]+>|&[a-z]+;", "x", m.group(4))) * 0.58 * size
            right = max(right, x + {"start": width, "middle": width / 2}.get(anchor, 0))
        return right

    def svg(self, title):
        body = "\n".join(self.parts)
        w = max(self.w, int(self.text_right() + 6))            # widen the canvas to fit its labels
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {self.h}" width="100%" class="fig-kit" '
                f'style="max-width:{w}px;margin:0 auto;display:block" role="img" aria-label="{title}">\n'
                f'<g font-family="Inter, Arial, sans-serif" font-size="13" fill="EDGE">\n{body}\n</g></svg>')


def arrow_head(c, a, b, col, size=9):
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    p1 = (b[0] - size * math.cos(ang - 0.4), b[1] - size * math.sin(ang - 0.4))
    p2 = (b[0] - size * math.cos(ang + 0.4), b[1] - size * math.sin(ang + 0.4))
    c.add(f'<path d="M{fmt(b[0])},{fmt(b[1])} L{fmt(p1[0])},{fmt(p1[1])} L{fmt(p2[0])},{fmt(p2[1])} Z" fill="{col}"/>')


def line(c, a, b, col="EDGE", w=1.4, dash=None, head=False):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<line x1="{fmt(a[0])}" y1="{fmt(a[1])}" x2="{fmt(b[0])}" y2="{fmt(b[1])}" stroke="{col}" stroke-width="{w}"{d}/>')
    if head:
        arrow_head(c, a, b, col)


def text(c, p, s, col="TEXT", anchor="start", size=13, weight="400", dx=0, dy=0):
    c.add(f'<text x="{fmt(p[0] + dx)}" y="{fmt(p[1] + dy)}" fill="{col}" font-size="{size}" '
          f'font-weight="{weight}" text-anchor="{anchor}">{s}</text>')


def dot(c, p, r=4, col="HEAD", fill=None):
    c.add(f'<circle cx="{fmt(p[0])}" cy="{fmt(p[1])}" r="{r}" fill="{fill or col}" stroke="{col}" stroke-width="1"/>')


def sub(base, s, sup=False):
    """Label with a subscript (or superscript): sub('Σ', 'w') -> Σ with a lowered w."""
    return f'{base}<tspan baseline-shift="{"super" if sup else "sub"}" font-size="72%">{s}</tspan>'


def _style(col, w, dash, fill, opacity):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' fill-opacity="{opacity}"' if opacity is not None else ""
    return f'fill="{fill}"{o} stroke="{col}" stroke-width="{w}"{d} stroke-linejoin="round"'


def poly(c, pts, col="HEAD", w=1.6, dash=None, fill="none", close=False, opacity=None):
    """Polyline (or closed polygon) through the points."""
    tag = "polygon" if close else "polyline"
    c.add(f'<{tag} points="{" ".join(f"{fmt(x)},{fmt(y)}" for x, y in pts)}" {_style(col, w, dash, fill, opacity)}/>')


def rect(c, x, y, w, h, col="HEAD", sw=1.6, dash=None, fill="none", opacity=None, rx=0):
    r = f' rx="{rx}"' if rx else ""
    c.add(f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}"{r} {_style(col, sw, dash, fill, opacity)}/>')


def pathd(c, d, col="HEAD", w=1.6, dash=None, fill="none", opacity=None):
    """Raw SVG path data (arcs, Bezier curves)."""
    c.add(f'<path d="{d}" {_style(col, w, dash, fill, opacity)}/>')


def circle(c, p, r, col="HEAD", w=1.6, dash=None, fill="none", opacity=None):
    c.add(f'<circle cx="{fmt(p[0])}" cy="{fmt(p[1])}" r="{fmt(r)}" {_style(col, w, dash, fill, opacity)}/>')


def arrow(c, a, b, col="BLUE", w=1.8, size=9):
    """Straight arrow from a to b (head at b)."""
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    tip = (b[0] - size * 0.6 * math.cos(ang), b[1] - size * 0.6 * math.sin(ang))
    line(c, a, tip, col, w)
    arrow_head(c, a, b, col, size)


def dim(c, a, b, label, col="TEXT", lab_off=(0, 0), anchor="middle", size=14, w=1.1):
    """Dimension line with heads at both ends and its label at the middle (shifted by lab_off)."""
    line(c, a, b, col, w)
    arrow_head(c, b, a, col, 7)
    arrow_head(c, a, b, col, 7)
    mid = ((a[0] + b[0]) / 2 + lab_off[0], (a[1] + b[1]) / 2 + lab_off[1])
    text(c, mid, label, col, anchor, size=size)


def hatch(c, a, b, side=1, col="EDGE", step=9, length=8, w=1.0):
    """Short slanted strokes along the segment a-b, on the left (side=1) or right (side=-1) of a->b: a solid wall."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy)
    if L == 0:
        return
    tx, ty = dx / L, dy / L
    nx, ny = -ty * side, tx * side                     # unit normal on the chosen side (screen coordinates)
    k = 0.0
    while k <= L:
        p = (a[0] + tx * k, a[1] + ty * k)
        q = (p[0] + (nx - tx) * length * 0.7071, p[1] + (ny - ty) * length * 0.7071)
        line(c, p, q, col, w)
        k += step


def path_d(fn, xs, px, y0, scale, top, bottom):
    """SVG path data for y = fn(x), split where the curve leaves [top, bottom]."""
    segs, cur = [], []
    for x in xs:
        y = y0 - fn(x) * scale
        if top <= y <= bottom:
            cur.append(f"{px(x):.1f},{y:.1f}")
        elif cur:
            segs.append(cur)
            cur = []
    if cur:
        segs.append(cur)
    return " ".join("M" + " L".join(s) for s in segs if len(s) > 1)


def curve(c, fn, xs, px, y0, scale, top, bottom, col, w=2.4, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<path d="{path_d(fn, xs, px, y0, scale, top, bottom)}" fill="none" stroke="{col}" stroke-width="{w}"{d}/>')


def overline_label(s):
    """'[-1 1 0]' -> SVG text with overlined negatives; tokens separated by spaces inside the brackets."""
    out = []
    for t in s[1:-1].split():
        out.append(f'<tspan text-decoration="overline">{t[1:]}</tspan>' if t.startswith("-") else t)
    return s[0] + "".join(out) + s[-1]


class Registry:
    """Collects the figures of one topic: vault copies on disk, web copies and captions in memory."""

    def __init__(self, folder):
        self.folder = folder
        self.web, self.captions, self.files, self.rasters = {}, {}, {}, []

    def raster(self, name, title, caption=None, width=None):
        """A figure copied from the slides as vault/attachments/<folder>/<name>.png (not generated here).
        The web copy is an <img> for pages three levels below the root; `width` caps its size in px."""
        cap = f"max-width:min(100%,{width}px)" if width else "max-width:100%"
        self.rasters.append(f"vault/attachments/{self.folder}/{name}.png")
        self.web[name] = (f'<figure class="slide-figure" style="margin:0"><img src="../../../vault/attachments/{self.folder}/'
                          f'{name}.png" alt="{title}" loading="lazy" style="{cap};height:auto;display:block;margin:0 auto;'
                          f'background:#fff;border-radius:8px;padding:8px"></figure>')
        self.captions[name] = caption or title

    def put(self, name, canvas, title, caption=None):
        s = canvas.svg(title)
        fixed, web = s, s
        for k, v in FIXED.items():
            fixed = fixed.replace(f'"{k}"', f'"{v}"')
        for k, v in WEB.items():
            web = web.replace(f'"{k}"', f'"{v}"')
        self.files[f"vault/attachments/{self.folder}/{name}.svg"] = fixed
        self.web[name] = web
        self.captions[name] = caption or title

    def write(self, root=REPO):
        changed = []
        for rel, content in self.files.items():
            path = pathlib.Path(root, rel)
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8", newline="\n")
                changed.append(rel)
        return changed

    def stale(self, root=REPO):
        return [rel for rel, content in self.files.items()
                if not pathlib.Path(root, rel).exists() or pathlib.Path(root, rel).read_text(encoding="utf-8") != content] + \
               [rel for rel in self.rasters if not pathlib.Path(root, rel).exists()]
