"""Problem RB-04: planar plates (T, I and C shapes) and their area elements, moments of inertia and centre of mass."""
import math

from figures.em_solutions import axis_out, figure, fixed_axis
from figures.em_sol.rb01 import add, d, sub
from figures.mech import S, Scene, bold

W, H, T = 4.0, 5.0, 0.8


def _ax(sym, s=None):
    return bold(sym) + (S("", s) if s else "")


def _plate(sc, pts, opacity=0.14):
    sc.poly(pts, "BLUE", 0.0, fill="BLUE", close=True, opacity=opacity)
    sc.poly(pts, "BLUE", 2.4, close=True)


def _element(sc, x, y, s=0.16):
    """Area element dA: a small dark orange square centred at (x, y)."""
    sc.poly([(x - s / 2, y - s / 2), (x + s / 2, y - s / 2), (x + s / 2, y + s / 2), (x - s / 2, y + s / 2)],
            "ACC", 1.2, fill="ACC", close=True, opacity=0.95)


def _leaders(sc, x, y, xlab_dy=-8, ylab_dx=6, y_to=0.0, x_to=0.0):
    """Dashed leaders from the element to the axes, labelled x and y."""
    sc.dashed((x, y), (x_to, y))
    sc.dashed((x, y), (x, y_to))
    sc.label(((x + x_to) / 2, y), "x", "TEXT", "middle", 15, dy=xlab_dy)
    sc.label((x, (y + y_to) / 2), "y", "TEXT", "start", 15, dx=ylab_dx, dy=5)


def _hdim(sc, x0, x1, y, name, ext, dy=-8, ext_to=None):
    """Horizontal dimension line from x0 to x1 at height y with extension lines from the heights in `ext`."""
    for xe, ye in ((x0, ext[0]), (x1, ext[1])):
        sc.dashed((xe, ye), (xe, y + (0.05 if y > ye else -0.05)))
    sc.dim((x0, y), (x1, y), name, off=(0, dy))


def _vdim(sc, x, y0, y1, name, ext, dx=-12, anchor_dy=5):
    for ye, xe in ((y0, ext[0]), (y1, ext[1])):
        sc.dashed((xe, ye), (x + (0.05 if x > xe else -0.05), ye))
    sc.dim((x, y0), (x, y1), "", off=(0, 0))
    sc.label((x, (y0 + y1) / 2), name, "TEXT", "end" if dx < 0 else "start", 15, dx=dx, dy=anchor_dy)


def _hatch(sc, x0, y0, x1, y1, step=0.22):
    """45-degree hatching of the rectangle [x0,x1] x [y0,y1]."""
    c = y0 - x1
    while c <= y1 - x0:
        # clip the segment y = x + c to the rectangle
        lo = max(x0, y0 - c)
        hi = min(x1, y1 - c)
        if lo < hi:
            sc.line((lo, lo + c), (hi, hi + c), "EDGE", 0.9)
        c += step


@figure("rb04-t-shape",
        "T-shaped plate with its auxiliary frame at the lower edge of the top bar, its centre of mass on the symmetry "
        "axis and two area elements.",
        r"The T split into the top bar and the stem in the frame $S_O$; $G$ lies on the symmetry line $Oy$ at the ordinate "
        r"$y_G$, and the axes $Gx$, $Gy$ are parallel to $Ox$, $Oy$.")
def t_shape():
    sc = Scene(680, 600, (330, 180), 80)
    w, h, t = W, H, T
    yg = (w * t * (t / 2) - t * (h - t) * ((h - t) / 2)) / (w * t + t * (h - t))
    pts = [(-w / 2, t), (w / 2, t), (w / 2, 0), (t / 2, 0), (t / 2, -(h - t)), (-t / 2, -(h - t)), (-t / 2, 0),
           (-w / 2, 0)]
    _plate(sc, pts)
    fixed_axis(sc, (0, 0), 0, 2.2, _ax("x"), off=(14, 6))
    fixed_axis(sc, (0, 0), 90, 1.3, _ax("y"), off=(14, 4))
    axis_out(sc, (0, 0), None, "HEAD")
    sc.label((0, 0), _ax("z"), "HEAD", "start", 16, weight="700", dx=14, dy=-12)
    # centre of mass and its axes
    sc.line((-1.7, yg), (1.7, yg), "EDGE", 1.2, "6 4")
    sc.label((1.7, yg), "Gx", "TEXT", "start", 15, dx=6, dy=5)
    sc.line((0.0, yg), (0.0, -(h - t) + 0.5), "EDGE", 1.2, "6 4")
    sc.label((0.0, -(h - t) + 0.5), "Gy", "TEXT", "start", 15, dx=7, dy=14)
    sc.dotp((0, 0), 3.5)
    sc.label((0, 0), "O", "HEAD", "end", 17, dx=-40, dy=18)
    sc.mass((0, yg), None, r=5, col="BLUE")
    sc.label((0, yg), "G", "HEAD", "end", 17, dx=-40, dy=-6)
    # dimensions
    _hdim(sc, -w / 2, w / 2, t + 0.95, "w", (t, t), dy=-8)
    _vdim(sc, w / 2 + 0.6, 0, t, "t", (w / 2, w / 2), dx=10)
    _hdim(sc, -t / 2, t / 2, -(h - t) - 0.5, "t", (-(h - t), -(h - t)), dy=20)
    _vdim(sc, -w / 2 - 0.65, -(h - t), t, "h", (-t / 2, -w / 2), dx=-12)
    _vdim(sc, 1.0, -(h - t), 0, "h − t", (t / 2, t / 2), dx=10)
    _vdim(sc, -1.0, yg, 0, sub("y", "G"), (-t / 2, -t / 2), dx=-12)
    # area elements
    _element(sc, 1.2, 0.4)
    _leaders(sc, 1.2, 0.4, y_to=0.0)
    sc.label((1.2, 0.4), "dA", "HEAD", "start", 15, dx=12, dy=5)
    _element(sc, 0.2, -2.6)
    sc.dashed((0.2, -2.6), (0.0, -2.6))
    sc.dashed((0.2, -2.6), (0.2, 0.0))
    sc.label((0.2, -1.3), "y", "TEXT", "start", 15, dx=5, dy=5)
    sc.label((0.2, -2.6), "dA", "HEAD", "start", 15, dx=22, dy=5)
    return sc


@figure("rb04-i-shape",
        "I-shaped plate centred at G with its two symmetry axes and the enclosing rectangle minus the two empty side "
        "rectangles.",
        r"The I in its central frame $S_G$; the planes $Gxz$ and $Gyz$ are planes of symmetry. About $Gx$ it equals the "
        r"rectangle $w \times h$ minus the two empty rectangles beside the stem.")
def i_shape():
    sc = Scene(680, 600, (330, 300), 70)
    w, h, t = W, H, T
    a, b = w / 2, h / 2
    pts = [(-a, b), (a, b), (a, b - t), (t / 2, b - t), (t / 2, -b + t), (a, -b + t), (a, -b), (-a, -b), (-a, -b + t),
           (-t / 2, -b + t), (-t / 2, b - t), (-a, b - t)]
    _hatch(sc, t / 2, -b + t, a, b - t)
    _hatch(sc, -a, -b + t, -t / 2, b - t)
    _plate(sc, pts)
    sc.poly([(-a, b), (a, b), (a, -b), (-a, -b)], "EDGE", 1.2, "6 4", close=True)
    fixed_axis(sc, (0, 0), 0, 2.45, _ax("x"), off=(14, 6))
    fixed_axis(sc, (0, 0), 90, 2.75, _ax("y"), off=(14, 4))
    axis_out(sc, (0, 0), None, "HEAD")
    sc.mass((0, 0), None, r=3, col="BLUE")
    sc.label((0, 0), _ax("z"), "HEAD", "start", 16, weight="700", dx=13, dy=-10)
    sc.label((0, 0), "G", "HEAD", "end", 17, dx=-14, dy=22)
    _hdim(sc, -a, a, b + 0.55, "w", (b, b), dy=-8)
    _vdim(sc, a + 0.55, b - t, b, "t", (a, a), dx=10)
    _vdim(sc, -a - 0.6, -b, b, "h", (-a, -a), dx=-12)
    sc.dim((-t / 2, -1.0), (t / 2, -1.0), "", off=(0, 0))
    sc.label((0, -1.0), "t", "TEXT", "middle", 15, dy=18)
    _element(sc, 1.2, 2.1)
    _leaders(sc, 1.2, 2.1, y_to=0.0)
    sc.label((1.2, 2.1), "dA", "HEAD", "start", 15, dx=12, dy=5)
    sc.note((-a, -b - 0.55), "hatched: (w − t) × (h − 2t) removed", "TEXT", "start", 14)
    return sc


@figure("rb04-c-shape",
        "C-shaped plate with its auxiliary frame at the back, its centre of mass on the horizontal symmetry axis and an "
        "area element.",
        r"The C in the frame $S_{O'}$; the plane $O'xz$ is a plane of symmetry, so $G$ is on $O'x$ at the abscissa $x_G$, "
        r"and the axis $Gy$ is parallel to $O'y$.")
def c_shape():
    sc = Scene(700, 600, (190, 310), 75)
    w, h, t = W, H, T
    b = h / 2
    xg = (2 * w * t * (w / 2) + t * (h - 2 * t) * (t / 2)) / (2 * w * t + t * (h - 2 * t))
    pts = [(0, b), (w, b), (w, b - t), (t, b - t), (t, -b + t), (w, -b + t), (w, -b), (0, -b)]
    _plate(sc, pts)
    fixed_axis(sc, (0, 0), 0, 4.75, _ax("x"), off=(14, 6))
    fixed_axis(sc, (0, 0), 90, 2.8, _ax("y"), off=(14, 4))
    axis_out(sc, (0, 0), None, "HEAD")
    sc.label((0, 0), _ax("z"), "HEAD", "end", 16, weight="700", dx=-14, dy=-10)
    sc.line((xg, -b - 0.5), (xg, b + 0.5), "EDGE", 1.2, "6 4")
    sc.label((xg, -b - 0.5), "Gy", "TEXT", "start", 15, dx=7, dy=4)
    sc.dotp((0, 0), 3.5)
    sc.label((0, 0), "O′", "HEAD", "end", 17, dx=-14, dy=22)
    sc.mass((xg, 0), None, r=5, col="BLUE")
    sc.label((xg, 0), "G", "HEAD", "start", 17, dx=10, dy=-10)
    _hdim(sc, 0, w, b + 0.75, "w", (b, b), dy=-8)
    _vdim(sc, w + 0.5, b - t, b, "t", (w, w), dx=10)
    _vdim(sc, -0.7, -b, b, "h", (0, 0), dx=-12)
    sc.dim((0, -1.3), (t, -1.3), "", off=(0, 0))
    sc.label((t / 2, -1.3), "t", "TEXT", "middle", 15, dy=18)
    sc.dim((0, -0.6), (xg, -0.6), "", off=(0, 0))
    sc.label((0.9, -0.6), sub("x", "G"), "TEXT", "start", 15, dy=18)
    _element(sc, 2.3, 2.1)
    _leaders(sc, 2.3, 2.1, y_to=0.0)
    sc.label((2.3, 2.1), "dA", "HEAD", "start", 15, dx=12, dy=5)
    return sc
