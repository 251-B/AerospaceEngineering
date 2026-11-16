"""Unit 6 figures of the Midterm 2 bank: energy-band diagrams, ln(sigma) against 1/T plots and a ferroelectric loop."""
from figures.svgkit import Canvas, line, text, poly, dot, rect, circle, arrow, sub, dim
from figures.mat_mt2.common import figure


# ---------------------------------------------------------------- energy-band diagrams

def _energy_axis(c, top=18, bottom=214):
    arrow(c, (30, bottom), (30, top), "EDGE", 1.6, 9)
    c.add(f'<text x="22" y="{(top + bottom) / 2:.1f}" fill="TEXT" font-size="12" text-anchor="middle" '
          f'transform="rotate(-90 22 {(top + bottom) / 2:.1f})">Energy</text>')


def _band(c, x, y, w, h, filled, label):
    if filled:
        rect(c, x, y, w, h, "HEAD", 1.5, None, "ACC", 0.35)
    else:
        rect(c, x, y, w, h, "HEAD", 1.5, None, "BLUE", 0.10)
    if label:
        text(c, (x + w / 2, y + h / 2 + 5), label, "HEAD", "middle", 12)


def _gap_diagram(c, gap_px, eg_text, level=None, intrinsic=False):
    """Valence band (filled) at the bottom, conduction band (empty) on top, gap of gap_px pixels."""
    _energy_axis(c)
    x, w = 50, 120
    vb_top = 214 - 56
    cb_bot = vb_top - gap_px
    _band(c, x, cb_bot - 56, w, 56, False, "Conduction band")
    _band(c, x, vb_top, w, 56, True, "Valence band")
    dim(c, (x + w + 18, cb_bot), (x + w + 18, vb_top), "", "TEXT", size=12)
    text(c, (x + w + 26, (cb_bot + vb_top) / 2 + 5), eg_text, "HEAD", "start", 12)
    if level == "donor":
        line(c, (x + 8, cb_bot + 10), (x + w - 8, cb_bot + 10), "PINK", 1.8, "6 4")
        for k in range(5):
            dot(c, (x + 18 + 21 * k, cb_bot + 10), 3.6, "PINK")
    elif level == "acceptor":
        line(c, (x + 8, vb_top - 10), (x + w - 8, vb_top - 10), "GREEN", 1.8, "6 4")
        for k in range(5):
            circle(c, (x + 18 + 21 * k, vb_top - 10), 3.6, "GREEN", 1.4, fill="none")
    if intrinsic:
        for k in range(3):
            dot(c, (x + 25 + 35 * k, cb_bot - 12), 3.6, "PINK")
            circle(c, (x + 25 + 35 * k, vb_top + 12), 3.8, "HEAD", 1.4, fill="#ffffff")


def _half_filled(c):
    _energy_axis(c)
    x, w = 50, 120
    _band(c, x, 20, w, 56, False, "Empty band")
    rect(c, x, 120, w, 46, "HEAD", 1.5, None, "BLUE", 0.10)
    text(c, (x + w / 2, 148), "Empty states", "HEAD", "middle", 12)
    rect(c, x, 166, w, 48, "HEAD", 1.5, None, "ACC", 0.35)
    text(c, (x + w / 2, 195), "Filled states", "HEAD", "middle", 12)
    text(c, (x + w + 8, 171), sub("E", "f"), "HEAD", "start", 13)


def _overlap(c):
    _energy_axis(c)
    rect(c, 90, 20, 110, 120, "HEAD", 1.5, None, "BLUE", 0.10)
    text(c, (160, 60), "Empty band", "HEAD", "middle", 12)
    rect(c, 45, 112, 110, 102, "HEAD", 1.5, None, "ACC", 0.35)
    text(c, (95, 180), "Filled band", "HEAD", "middle", 12)


def _canvas():
    return Canvas(270, 228)


# Set used by "Which picture describes ... an insulator?"
@figure("u6-bands-a", "Band diagram A")
def bands_a():
    c = _canvas(); _gap_diagram(c, 30, sub("E", "g") + " = 1.1 eV"); return c


@figure("u6-bands-b", "Band diagram B")
def bands_b():
    c = _canvas(); _half_filled(c); return c


@figure("u6-bands-c", "Band diagram C")
def bands_c():
    c = _canvas(); _overlap(c); return c


@figure("u6-bands-d", "Band diagram D")
def bands_d():
    c = _canvas(); _gap_diagram(c, 96, sub("E", "g") + " = 6 eV"); return c


# Set used by "Which picture describes ... magnesium?"
@figure("u6-solid-p", "Electron energy bands, picture A")
def solid_p():
    c = _canvas(); _gap_diagram(c, 22, sub("E", "g") + " = 0.67 eV"); return c


@figure("u6-solid-q", "Electron energy bands, picture B")
def solid_q():
    c = _canvas(); _overlap(c); return c


@figure("u6-solid-r", "Electron energy bands, picture C")
def solid_r():
    c = _canvas(); _half_filled(c); return c


@figure("u6-solid-s", "Electron energy bands, picture D")
def solid_s():
    c = _canvas(); _gap_diagram(c, 100, sub("E", "g") + " = 7 eV"); return c


# Set used by "Which picture describes an n-type semiconductor?"
@figure("u6-impurity-scheme-1", "Semiconductor band picture A")
def doped_w():
    c = _canvas(); _gap_diagram(c, 40, sub("E", "g") + " = 1.1 eV", level="donor"); return c


@figure("u6-impurity-scheme-2", "Semiconductor band picture B")
def doped_x():
    c = _canvas(); _gap_diagram(c, 40, sub("E", "g") + " = 1.1 eV", level="acceptor"); return c


@figure("u6-impurity-scheme-3", "Semiconductor band picture C")
def doped_y():
    c = _canvas(); _gap_diagram(c, 40, sub("E", "g") + " = 1.1 eV", intrinsic=True); return c


@figure("u6-impurity-scheme-4", "Semiconductor band picture D")
def doped_z():
    c = _canvas(); _gap_diagram(c, 100, sub("E", "g") + " = 6 eV"); return c


# Phosphorus-doped silicon with the energies of the levels (Session 13 Slides 8 and 40)
@figure("u6-si-p-levels", "Energy-band diagram of phosphorus-doped silicon with the energies of the band edges and of the impurity level")
def si_p_levels():
    c = Canvas(360, 260)
    _energy_axis(c, 18, 246)
    x, w = 60, 150
    ev, ec = 196, 76            # 0 eV and 1.10 eV (scale 109 px per eV)
    ed = ec + 0.045 * 109
    rect(c, x, ev, w, 50, "HEAD", 1.5, None, "ACC", 0.35)
    text(c, (x + w / 2, ev + 30), "Valence band", "HEAD", "middle", 12)
    rect(c, x, ec - 50, w, 50, "HEAD", 1.5, None, "BLUE", 0.10)
    text(c, (x + w / 2, ec - 20), "Conduction band", "HEAD", "middle", 12)
    line(c, (x + 8, ed + 4), (x + w - 8, ed + 4), "PINK", 1.8, "6 4")
    for k in range(6):
        dot(c, (x + 18 + 23 * k, ed + 4), 3.4, "PINK")
    for y, lab in ((ec, sub("E", "c") + " = 1.100 eV"), (ed + 4, sub("E", "d") + " = 1.055 eV"), (ev, sub("E", "v") + " = 0 eV")):
        line(c, (x + w, y), (x + w + 14, y), "EDGE", 1.0)
    text(c, (x + w + 18, ec - 4), sub("E", "c") + " = 1.100 eV", "HEAD", "start", 12)
    text(c, (x + w + 18, ed + 18), sub("E", "d") + " = 1.055 eV", "PINK", "start", 12)
    text(c, (x + w + 18, ev + 5), sub("E", "v") + " = 0 eV", "HEAD", "start", 12)
    return c


# ---------------------------------------------------------------- ln(sigma) against 1/T

def _small_axes(c, x0=40, y0=150, x1=230, y1=16):
    arrow(c, (x0, y0), (x1, y0), "EDGE", 1.5, 8)
    arrow(c, (x0, y0), (x0, y1), "EDGE", 1.5, 8)
    text(c, (x1 - 4, y0 + 18), "1/T", "TEXT", "end", 12)
    text(c, (x0 + 6, y1 + 6), "ln σ", "TEXT", "start", 12)


def _lnsig_canvas():
    return Canvas(250, 172)


@figure("u6-lnsig-1", "Conductivity plot A")
def lnsig_1():
    c = _lnsig_canvas(); _small_axes(c); poly(c, [(60, 36), (210, 132)], "PINK", 2.6); return c


@figure("u6-lnsig-2", "Conductivity plot B")
def lnsig_2():
    c = _lnsig_canvas(); _small_axes(c); poly(c, [(60, 132), (210, 36)], "PINK", 2.6); return c


@figure("u6-lnsig-3", "Conductivity plot C")
def lnsig_3():
    c = _lnsig_canvas(); _small_axes(c)
    poly(c, [(58, 30), (98, 96), (140, 96), (210, 128)], "PINK", 2.6)
    return c


@figure("u6-lnsig-4", "Conductivity plot D")
def lnsig_4():
    c = _lnsig_canvas(); _small_axes(c); poly(c, [(60, 84), (210, 84)], "PINK", 2.6); return c


@figure("u6-extrinsic-regions", "ln σ against 1/T for an n-type semiconductor, with three regions marked I, II and III")
def extrinsic_regions():
    c = Canvas(460, 290)
    x0, y0 = 60, 240
    arrow(c, (x0, y0), (430, y0), "EDGE", 1.5, 9)
    arrow(c, (x0, y0), (x0, 20), "EDGE", 1.5, 9)
    text(c, (245, 278), "1/T", "TEXT", "middle", 13)
    text(c, (x0 - 6, 258), "High T", "TEXT", "start", 12)
    text(c, (420, 258), "Low T", "TEXT", "end", 12)
    c.add('<text x="36" y="130" fill="TEXT" font-size="13" text-anchor="middle" transform="rotate(-90 36 130)">ln σ</text>')
    pts = [(80, 40), (144, 160), (230, 160), (400, 214)]
    poly(c, pts, "PINK", 2.6)
    for x in (143, 232):
        line(c, (x, 60), (x, 236), "EDGE", 1.0, "4 4")
    text(c, (128, 74), "I", "HEAD", "middle", 15, "700")
    text(c, (188, 148), "II", "HEAD", "middle", 15, "700")
    text(c, (316, 168), "III", "HEAD", "middle", 15, "700")
    return c


@figure("u6-intrinsic-line", "ln σ against 1/T for an intrinsic semiconductor: a straight line through two marked points")
def intrinsic_line():
    c = Canvas(440, 300)
    x0, y0 = 70, 250
    sx, sy = 110.0, 26.0           # px per 1e-3 K^-1, px per unit of ln sigma

    def P(u, v):
        return (x0 + u * sx, y0 - v * sy)
    arrow(c, (x0, y0), (x0 + 3.4 * sx, y0), "EDGE", 1.5, 9)
    arrow(c, (x0, y0), (x0, y0 - 8.8 * sy), "EDGE", 1.5, 9)
    for u in (1, 2, 3):
        line(c, P(u, 0), (P(u, 0)[0], y0 + 5), "EDGE", 1.0)
        text(c, (P(u, 0)[0], y0 + 20), f"{u}.0", "TEXT", "middle", 12)
    text(c, (x0 + 1.7 * sx, y0 + 42), "1/T (" + sub("10", "−3", True) + " K" + sub("", "−1", True) + ")", "TEXT", "middle", 12)
    for v in (0, 2, 4, 6, 8):
        line(c, (x0 - 5, P(0, v)[1]), P(0, v), "EDGE", 1.0)
        text(c, (x0 - 9, P(0, v)[1] + 4), str(v), "TEXT", "end", 12)
    c.add(f'<text x="24" y="{y0 - 4.4 * sy:.1f}" fill="TEXT" font-size="13" text-anchor="middle" '
          f'transform="rotate(-90 24 {y0 - 4.4 * sy:.1f})">ln σ, σ in (Ω·m)⁻¹</text>')
    poly(c, [P(0.85, 7.96), P(2.09, 0.02)], "PINK", 2.4)
    for u, v in ((1.0, 7.0), (2.0, 0.6)):
        line(c, P(u, 0), P(u, v), "EDGE", 1.0, "4 4")
        line(c, P(0, v), P(u, v), "EDGE", 1.0, "4 4")
        dot(c, P(u, v), 4.2, "HEAD")
    text(c, (P(1.0, 7.0)[0] + 10, P(1.0, 7.0)[1] - 6), "(1.0, 7.0)", "HEAD", "start", 12)
    text(c, (P(2.0, 0.6)[0] + 10, P(2.0, 0.6)[1] - 8), "(2.0, 0.6)", "HEAD", "start", 12)
    return c


# ---------------------------------------------------------------- ferroelectric loop

@figure("u6-pe-loop", "Polarisation against electric field loop of a ferroelectric with four marked points K, L, M and N")
def pe_loop():
    import math
    c = Canvas(420, 300)
    ox, oy = 210, 150
    arrow(c, (40, oy), (395, oy), "EDGE", 1.5, 9)
    arrow(c, (ox, 285), (ox, 15), "EDGE", 1.5, 9)
    text(c, (392, oy + 20), "E", "TEXT", "end", 13)
    text(c, (ox + 8, 26), "Polarisation", "TEXT", "start", 13)

    def branch(sign):
        pts = []
        for k in range(61):
            e = -150 + 5 * k
            p = 100 * math.tanh((e + sign * 45) / 50.0)
            pts.append((ox + e, oy - p))
        return pts
    poly(c, branch(+1), "PINK", 2.3)       # descending branch (crosses E axis at -45)
    poly(c, branch(-1), "BLUE", 2.3)       # ascending branch (crosses E axis at +45)
    pr = 100 * math.tanh(45 / 50.0)
    tip = (ox + 150, oy - 100 * math.tanh(105 / 50.0))
    dot(c, tip, 4.5, "HEAD")
    text(c, (tip[0] - 4, tip[1] - 12), "K", "HEAD", "middle", 14, "700")
    dot(c, (ox - 45, oy), 4.5, "HEAD")
    text(c, (ox - 28, oy + 20), "L", "HEAD", "middle", 14, "700")
    dot(c, (ox, oy - pr), 4.5, "HEAD")
    text(c, (ox - 12, oy - pr - 8), "M", "HEAD", "end", 14, "700")
    dot(c, (ox, oy), 4.5, "HEAD")
    text(c, (ox + 10, oy + 20), "N", "HEAD", "start", 14, "700")
    return c
