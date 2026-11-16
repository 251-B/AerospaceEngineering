"""Unit 7 figures of the Midterm 2 bank (magnetic and thermal properties, Session 15).

Option pictures (used as the options of "Which picture describes ..." questions) carry neutral names and neutral alt
texts, so that neither the file name seen in the vault nor the accessible label gives the answer away:

    u7-dip-1  dipoles in random directions          (paramagnetic, no field)
    u7-dip-2  all dipoles parallel                   (ferromagnetic, inside a domain)
    u7-dip-3  antiparallel dipoles of equal size     (antiferromagnetic)
    u7-dip-4  antiparallel dipoles of unequal size   (ferrimagnetic)
    u7-dipf-1 field H applied, dipoles aligned with H                (paramagnetic in a field)
    u7-dipf-2 field H applied, small induced dipoles opposite to H   (diamagnetic in a field)
    u7-dipf-3 field H applied, dipoles in random directions
    u7-dipf-4 field H applied, atoms without dipoles
    u7-loopopt-1..4  wide loop (hard), narrow loop (soft), square loop (memories), straight line (no hysteresis)

The other figures are read in the statement: the initial magnetization curve with numbered points, a loop with
lettered points, two loops on the same axes, a loop with a scale (Hc = 50 kA/m, Br = 0.9 T, Bs = 1.2 T), two
interatomic energy wells, the saturation magnetization of iron against temperature (Tc = 1043 K, Session 15 Slide 23)
and the resistivity of niobium against temperature (Tc = 9.26 K, Session 15 Slide 25). All are schematic.
"""
import math

from figures.svgkit import Canvas, line, text, poly, dot, rect, circle, arrow, sub
from figures.mat_mt2.common import figure

OPTION_ALT = "Arrangement of magnetic dipoles (option picture)"
LOOP_ALT = "B-H curve (option picture)"

# ------------------------------------------------------------------ dipole pictures

_COLS, _ROWS = 4, 3
_DX, _DY = 46, 44
_X0, _Y0 = 34, 30
# fixed "random" directions (degrees from the upward vertical), so the picture is the same on every build
_RANDOM = [35, 200, 110, 290, 160, 65, 250, 15, 320, 135, 230, 95]


def _atoms(c, x0=_X0):
    pts = []
    for r in range(_ROWS):
        for k in range(_COLS):
            p = (x0 + k * _DX, _Y0 + r * _DY)
            circle(c, p, 13, "EDGE", 1.0, fill="EDGE", opacity=0.12)
            pts.append(p)
    return pts


def _dipole(c, p, ang_deg, length, col="BLUE", w=2.4):
    a = math.radians(ang_deg)
    dx, dy = math.sin(a) * length / 2, -math.cos(a) * length / 2
    arrow(c, (p[0] - dx, p[1] - dy), (p[0] + dx, p[1] + dy), col, w, 8)


def _field(c, x=_X0 + _COLS * _DX + 6):
    """Applied field H pointing up, drawn at the right of the lattice."""
    arrow(c, (x, _Y0 + (_ROWS - 1) * _DY + 8), (x, _Y0 - 12), "PINK", 2.6, 11)
    text(c, (x + 10, _Y0 + _DY), "H", "PINK", "start", 15, "700")


def _lattice(width):
    return Canvas(width, _Y0 + (_ROWS - 1) * _DY + 30)


@figure("u7-dip-1", OPTION_ALT)
def dip_random():
    c = _lattice(200)
    for p, a in zip(_atoms(c), _RANDOM):
        _dipole(c, p, a, 30)
    return c


@figure("u7-dip-2", OPTION_ALT)
def dip_parallel():
    c = _lattice(200)
    for p in _atoms(c):
        _dipole(c, p, 0, 30)
    return c


@figure("u7-dip-3", OPTION_ALT)
def dip_antiparallel_equal():
    c = _lattice(200)
    for i, p in enumerate(_atoms(c)):
        r, k = divmod(i, _COLS)
        _dipole(c, p, 0 if (r + k) % 2 == 0 else 180, 30)
    return c


@figure("u7-dip-4", OPTION_ALT)
def dip_antiparallel_unequal():
    c = _lattice(200)
    for i, p in enumerate(_atoms(c)):
        r, k = divmod(i, _COLS)
        if (r + k) % 2 == 0:
            _dipole(c, p, 0, 32)
        else:
            _dipole(c, p, 180, 14, w=2.0)
    return c


@figure("u7-dipf-1", OPTION_ALT)
def dipf_aligned():
    c = _lattice(240)
    for p in _atoms(c):
        _dipole(c, p, 0, 28)
    _field(c)
    return c


@figure("u7-dipf-2", OPTION_ALT)
def dipf_opposite_small():
    c = _lattice(240)
    for p in _atoms(c):
        _dipole(c, p, 180, 14, w=2.0)
    _field(c)
    return c


@figure("u7-dipf-3", OPTION_ALT)
def dipf_random():
    c = _lattice(240)
    for p, a in zip(_atoms(c), _RANDOM[::-1]):
        _dipole(c, p, a, 28)
    _field(c)
    return c


@figure("u7-dipf-4", OPTION_ALT)
def dipf_none():
    c = _lattice(240)
    _atoms(c)
    _field(c)
    return c


# ------------------------------------------------------------------ B-H curves

def _bh_axes(c, o, half_w, half_h, xl="H", yl="B"):
    line(c, (o[0] - half_w, o[1]), (o[0] + half_w, o[1]), "EDGE", 1.3, head=True)
    line(c, (o[0], o[1] + half_h), (o[0], o[1] - half_h), "EDGE", 1.3, head=True)
    text(c, (o[0] + half_w, o[1] + 20), xl, "HEAD", "end", 14, "700")
    text(c, (o[0] + 8, o[1] - half_h + 6), yl, "HEAD", "start", 14, "700")


def _loop_points(o, amp, hc, w, span, n=150):
    """Upper (descending) and lower (ascending) branches of a tanh loop that close at +-span."""
    es = [-span + 2 * span * i / n for i in range(n + 1)]
    shift = lambda e: hc * (1 - (e / span) ** 2)  # noqa: E731  (the coercive shift fades out at saturation)
    up = [(o[0] + e, o[1] - amp * math.tanh((e + shift(e)) / w)) for e in es]
    dn = [(o[0] + e, o[1] - amp * math.tanh((e - shift(e)) / w)) for e in es]
    return up, dn


def _draw_loop(c, o, amp, hc, w, span, col, wd=2.6):
    up, dn = _loop_points(o, amp, hc, w, span)
    poly(c, up, col, wd)
    poly(c, dn, col, wd)
    return amp * math.tanh(hc / w)        # height of the remanence point above the H axis


@figure("u7-loopopt-1", LOOP_ALT)
def loopopt_wide():
    c = Canvas(220, 170)
    o = (110, 85)
    _bh_axes(c, o, 100, 75)
    _draw_loop(c, o, 52, 50, 26, 90, "BLUE")
    return c


@figure("u7-loopopt-2", LOOP_ALT)
def loopopt_narrow():
    c = Canvas(220, 170)
    o = (110, 85)
    _bh_axes(c, o, 100, 75)
    _draw_loop(c, o, 52, 7, 9, 90, "BLUE")
    return c


@figure("u7-loopopt-3", LOOP_ALT)
def loopopt_square():
    c = Canvas(220, 170)
    o = (110, 85)
    _bh_axes(c, o, 100, 75)
    hc, b = 22, 50
    poly(c, [(o[0] - 90, o[1] + b + 4), (o[0] - hc - 3, o[1] + b), (o[0] - hc, o[1] - b + 2), (o[0] - hc + 3, o[1] - b),
             (o[0] + 90, o[1] - b - 4), (o[0] + hc + 3, o[1] - b), (o[0] + hc, o[1] + b - 2), (o[0] + hc - 3, o[1] + b),
             (o[0] - 90, o[1] + b + 4)], "BLUE", 2.6)
    return c


@figure("u7-loopopt-4", LOOP_ALT)
def loopopt_line():
    c = Canvas(220, 170)
    o = (110, 85)
    _bh_axes(c, o, 100, 75)
    line(c, (o[0] - 90, o[1] + 22), (o[0] + 90, o[1] - 22), "BLUE", 2.6)
    return c


@figure("u7-loop-points", "Hysteresis loop B-H with four marked points P, Q, R and S")
def loop_points():
    c = Canvas(420, 300)
    o = (210, 150)
    _bh_axes(c, o, 190, 135)
    span, amp = 160, 105
    br = _draw_loop(c, o, amp, 60, 45, span, "BLUE")
    tip = amp * math.tanh(span / 45)
    pts = {"P": (o[0] + span, o[1] - tip), "Q": (o[0], o[1] - br), "R": (o[0] - 60, o[1]), "S": (o[0] - span, o[1] + tip)}
    for name, p in pts.items():
        dot(c, p, 5, "PINK", "PINK")
    text(c, (pts["P"][0] + 4, pts["P"][1] - 10), "P", "PINK", "start", 15, "700")
    text(c, (pts["Q"][0] - 10, pts["Q"][1] - 8), "Q", "PINK", "end", 15, "700")
    text(c, (pts["R"][0] - 10, pts["R"][1] + 22), "R", "PINK", "end", 15, "700")
    text(c, (pts["S"][0] - 4, pts["S"][1] + 22), "S", "PINK", "end", 15, "700")
    return c


@figure("u7-loop-pair", "Two hysteresis loops, labelled 1 and 2, drawn on the same B-H axes")
def loop_pair():
    c = Canvas(460, 300)
    o = (230, 150)
    _bh_axes(c, o, 210, 135)
    _draw_loop(c, o, 100, 95, 40, 180, "PINK")
    _draw_loop(c, o, 82, 9, 10, 180, "BLUE")
    text(c, (o[0] - 160, o[1] - 82), "1", "PINK", "middle", 16, "700")
    text(c, (o[0] + 60, o[1] - 100), "2", "BLUE", "middle", 16, "700")
    line(c, (o[0] + 54, o[1] - 95), (o[0] + 36, o[1] - 80), "BLUE", 1.0)
    return c


@figure("u7-loop-hard-scale", "Hysteresis loop with a scale: H from -150 to 150 kA/m and B from -1.2 to 1.2 T")
def loop_hard_scale():
    c = Canvas(520, 340)
    o = (260, 170)
    sx = 1.4                     # px per kA/m
    sy = 110.0                   # px per T
    _bh_axes(c, o, 235, 155, "H (kA/m)", "B (T)")
    span = 150 * sx
    # a loop with Bs = 1.2 T at +-150 kA/m, remanence 0.9 T and coercivity 50 kA/m
    hc_px, w = 50 * sx, 40.0
    amp_needed = 1.2 * sy

    # choose amp so that the tip reaches Bs and the remanence is 0.9 T: tanh(hc/w)*amp = 0.9*sy
    amp = 0.9 * sy / math.tanh(hc_px / w)
    w = span / math.atanh(min(0.999, amp_needed / amp)) if amp > amp_needed else w
    amp = 0.9 * sy / math.tanh(hc_px / w)
    _draw_loop(c, o, amp, hc_px, w, span, "BLUE")
    for v in (-150, -100, -50, 50, 100, 150):
        x = o[0] + v * sx
        line(c, (x, o[1] - 4), (x, o[1] + 4), "EDGE", 1.2)
        text(c, (x, o[1] + 20 if v > 0 else o[1] - 10), str(v), "TEXT", "middle", 11)
    for v in (-1.2, -0.9, 0.9, 1.2):
        y = o[1] - v * sy
        line(c, (o[0] - 4, y), (o[0] + 4, y), "EDGE", 1.2)
        text(c, (o[0] - 8, y + 4), f"{v:g}", "TEXT", "end", 11)
    line(c, (o[0], o[1] - 1.2 * sy), (o[0] + span, o[1] - 1.2 * sy), "EDGE", 1.0, "4,4")
    line(c, (o[0], o[1] + 1.2 * sy), (o[0] - span, o[1] + 1.2 * sy), "EDGE", 1.0, "4,4")
    return c


# ------------------------------------------------------------------ initial magnetization curve

@figure("u7-init-curve-stages", "Initial magnetization curve from the demagnetized state with numbered points 1, 2 and 3")
def init_curve_stages():
    c = Canvas(460, 300)
    o = (60, 260)
    line(c, o, (440, o[1]), "EDGE", 1.3, head=True)
    line(c, o, (o[0], 20), "EDGE", 1.3, head=True)
    text(c, (440, o[1] + 22), "H", "HEAD", "end", 14, "700")
    text(c, (o[0] + 8, 30), "B", "HEAD", "start", 14, "700")
    X, Y = 330.0, 200.0

    def f(t):
        t = max(0.0, min(1.0, t))
        return 0.10 * t + 0.90 * (3 * t * t - 2 * t ** 3)
    xs = [i / 100 for i in range(0, 101)]
    pts = [(o[0] + t * X, o[1] - Y * f(t)) for t in xs] + [(o[0] + X + 50, o[1] - Y)]
    poly(c, pts, "BLUE", 2.6)
    text(c, (o[0] - 12, o[1] + 18), "O", "HEAD", "middle", 13, "700")
    for label, t, dx, dy in (("1", 0.17, 10, 6), ("2", 0.62, 12, 14), ("3", 0.95, 0, -14)):
        p = (o[0] + t * X, o[1] - Y * f(t))
        dot(c, p, 5, "PINK", "PINK")
        text(c, (p[0] + dx, p[1] + dy), label, "PINK", "start" if dx else "middle", 15, "700")
    return c


# ------------------------------------------------------------------ energy wells (thermal expansion)

def _morse(r, depth, a, r0=1.0):
    return depth * ((1 - math.exp(-a * (r - r0))) ** 2 - 1)


@figure("u7-energy-wells", "Potential energy against interatomic distance for two materials, curves 1 and 2")
def energy_wells():
    c = Canvas(480, 320)
    o = (60, 70)                              # energy zero line at y = 70
    line(c, (o[0], 300), (o[0], 20), "EDGE", 1.3, head=True)
    line(c, (o[0], o[1]), (460, o[1]), "EDGE", 1.3, head=True)
    text(c, (460, o[1] - 8), "r", "HEAD", "end", 14, "700")
    text(c, (o[0] + 8, 30), "E", "HEAD", "start", 14, "700")
    text(c, (o[0] - 8, o[1] + 4), "0", "TEXT", "end", 12)
    PX = lambda r: o[0] + 30 + (r - 0.55) * 200  # noqa: E731
    PY = lambda e: o[1] - e * 1.0                 # noqa: E731
    rs = [0.55 + i * 1.5 / 300 for i in range(301)]
    deep = [(PX(r), PY(_morse(r, 210, 3.2))) for r in rs if _morse(r, 210, 3.2) < 30]
    shallow = [(PX(r), PY(_morse(r, 95, 1.6))) for r in rs if _morse(r, 95, 1.6) < 30]
    poly(c, deep, "PINK", 2.6)
    poly(c, shallow, "BLUE", 2.6)
    text(c, (PX(1.0) + 22, PY(-210) + 6), "1", "PINK", "start", 16, "700")
    text(c, (PX(1.75), PY(_morse(1.75, 95, 1.6)) + 26), "2", "BLUE", "middle", 16, "700")
    return c


# ------------------------------------------------------------------ Curie temperature

@figure("u7-ms-temperature", "Saturation magnetization of a ferromagnetic metal against temperature, from 0 to 1400 K")
def ms_temperature():
    c = Canvas(480, 280)
    o = (70, 230)
    sx = 300 / 1200                          # px per K
    line(c, o, (450, o[1]), "EDGE", 1.3, head=True)
    line(c, o, (o[0], 30), "EDGE", 1.3, head=True)
    text(c, (450, o[1] + 36), "T (K)", "HEAD", "end", 13, "700")
    text(c, (o[0] + 8, 40), sub("M", "s") + " (relative)", "HEAD", "start", 13, "700")
    tc = 1043
    pts = []
    for i in range(0, 201):
        t = tc * i / 200
        m = (1 - (t / tc) ** 3.2) ** 0.36
        pts.append((o[0] + t * sx, o[1] - 160 * m))
    pts.append((o[0] + 1400 * sx, o[1]))
    poly(c, pts, "BLUE", 2.6)
    for v in range(0, 1401, 200):
        x = o[0] + v * sx
        line(c, (x, o[1] - 4), (x, o[1] + 4), "EDGE", 1.2)
        text(c, (x, o[1] + 18), str(v), "TEXT", "middle", 11)
    text(c, (o[0] - 8, o[1] - 160 + 4), "1", "TEXT", "end", 11)
    line(c, (o[0] - 4, o[1] - 160), (o[0] + 4, o[1] - 160), "EDGE", 1.2)
    return c


# ------------------------------------------------------------------ superconductor

@figure("u7-rho-temperature", "Electrical resistivity of a pure metal against temperature, from 0 to 14 K")
def rho_temperature():
    c = Canvas(480, 280)
    o = (70, 230)
    sx = 340 / 14                            # px per K
    line(c, o, (450, o[1]), "EDGE", 1.3, head=True)
    line(c, o, (o[0], 30), "EDGE", 1.3, head=True)
    text(c, (450, o[1] + 36), "T (K)", "HEAD", "end", 13, "700")
    text(c, (o[0] + 8, 40), "ρ", "HEAD", "start", 15, "700")
    tc = 9.26
    normal = lambda t: 90 + 2.2 * t ** 1.4   # noqa: E731
    pts = [(o[0] + t * sx, o[1] - normal(t)) for t in [tc + i * (14 - tc) / 60 for i in range(61)]]
    poly(c, pts, "BLUE", 2.6)
    line(c, (o[0] + tc * sx, o[1] - normal(tc)), (o[0] + tc * sx, o[1] - 1.5), "BLUE", 2.6)
    line(c, (o[0], o[1] - 1.5), (o[0] + tc * sx, o[1] - 1.5), "BLUE", 2.6)
    for v in range(0, 15, 2):
        x = o[0] + v * sx
        line(c, (x, o[1] - 4), (x, o[1] + 4), "EDGE", 1.2)
        text(c, (x, o[1] + 18), str(v), "TEXT", "middle", 11)
    for v in range(1, 14, 2):
        x = o[0] + v * sx
        line(c, (x, o[1] - 3), (x, o[1] + 3), "EDGE", 1.0)
    return c
