"""Box-and-arrow helpers for the Business Management diagrams (pure stdlib, built on svgkit)."""
from figures.svgkit import fmt, line, text


def box(c, x, y, w, h, lines, col="BLUE", weight="400", size=13, fill=True, head_first=False, rx=8):
    """Rounded box centred text; `lines` is a string or a list of lines (first one bold if head_first)."""
    op = ' fill-opacity="0.10"' if fill else ""
    c.add(f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" rx="{rx}" '
          f'fill="{col if fill else "none"}"{op} stroke="{col}" stroke-width="1.4"/>')
    lines = [lines] if isinstance(lines, str) else lines
    lh = size + 4
    y0 = y + h / 2 - (len(lines) - 1) * lh / 2 + size * 0.35
    for i, s in enumerate(lines):
        wgt = "700" if (head_first and i == 0) else weight
        colr = "HEAD" if (head_first and i == 0) or weight == "700" else "TEXT"
        text(c, (x + w / 2, y0 + i * lh), s, colr, "middle", size=size, weight=wgt)
    return (x, y, w, h)


def mid(b, side):
    x, y, w, h = b
    return {"top": (x + w / 2, y), "bottom": (x + w / 2, y + h), "left": (x, y + h / 2),
            "right": (x + w, y + h / 2)}[side]


def arrow(c, a, b, col="EDGE", w=1.6, dash=None):
    line(c, a, b, col, w, dash, head=True)


def elbow(c, pts, col="EDGE", w=1.6):
    """Polyline through pts with an arrow head on the last segment."""
    for p, q in zip(pts[:-2], pts[1:-1]):
        line(c, p, q, col, w)
    line(c, pts[-2], pts[-1], col, w, head=True)
