"""Figures for Advanced Maths Topic 6 — Heat Equation, Sturm-Liouville Problems and Fourier Series.

Official textbook figures (Haberman, BookPDE's.pdf) are cropped at 200 DPI into vault/attachments/AM-T6/
and registered via REG.raster. Computed Fourier partial sums, spatial modes, extensions and Robin roots
are generated as clean, theme-aware SVGs (EXTRA).
"""
import math
from .svgkit import Canvas, Registry, arrow, curve, dot, line, poly, sub, text


def fig_heat_modes():
    """First three spatial eigenfunctions sin(n*pi*x/L) and exponential decay e^{-(n*pi/L)^2 t}."""
    c = Canvas(680, 265)
    # Left panel: spatial eigenfunctions
    ox1, oy1 = 50.0, 135.0
    w1, h1 = 260.0, 78.0
    arrow(c, (ox1 - 8, oy1), (ox1 + w1 + 20, oy1), col="EDGE", w=1.4, size=7)
    arrow(c, (ox1, oy1 + h1 + 16), (ox1, oy1 - h1 - 18), col="EDGE", w=1.4, size=7)
    text(c, (ox1 + w1 + 24, oy1 + 4), "x", col="HEAD", size=12, weight="700")
    text(c, (ox1 + 8, oy1 - h1 - 10), "φₙ(x)", col="HEAD", size=12, weight="700")
    text(c, (ox1 + w1, oy1 + 16), "L", col="HEAD", anchor="middle", size=11, weight="700")
    text(c, (ox1 - 10, oy1 + 16), "0", col="HEAD", size=11)
    xs = [i / 100.0 for i in range(101)]
    px1 = lambda u: ox1 + u * w1
    curve(c, lambda u: math.sin(math.pi * u), xs, px1, oy1, h1, 20, 240, col="BLUE", w=2.2)
    curve(c, lambda u: math.sin(2 * math.pi * u), xs, px1, oy1, h1, 20, 240, col="GREEN", w=1.8, dash="6,3")
    curve(c, lambda u: math.sin(3 * math.pi * u), xs, px1, oy1, h1, 20, 240, col="ACC", w=1.6, dash="2,3")
    text(c, (ox1 + w1 * 0.5, 24), "Spatial eigenfunctions sin(nπx/L)", col="HEAD", anchor="middle", size=13, weight="700")
    text(c, (ox1 + w1 * 0.5, 248), "Blue: n=1 · Dashed green: n=2 · Dotted orange: n=3", col="TEXT", anchor="middle", size=11)

    # Right panel: time decay exp(-n^2 * t)
    ox2, oy2 = 395.0, 210.0
    w2, h2 = 240.0, 150.0
    arrow(c, (ox2 - 8, oy2), (ox2 + w2 + 20, oy2), col="EDGE", w=1.4, size=7)
    arrow(c, (ox2, oy2 + 12), (ox2, oy2 - h2 - 18), col="EDGE", w=1.4, size=7)
    text(c, (ox2 + w2 + 24, oy2 + 4), "t", col="HEAD", size=12, weight="700")
    text(c, (ox2 + 8, oy2 - h2 - 10), "Tₙ(t)", col="HEAD", size=12, weight="700")
    ts = [i * 0.02 for i in range(101)]
    px2 = lambda t: ox2 + (t / 2.0) * w2
    curve(c, lambda t: math.exp(-t), ts, px2, oy2, h2, 30, 220, col="BLUE", w=2.2)
    curve(c, lambda t: math.exp(-4 * t), ts, px2, oy2, h2, 30, 220, col="GREEN", w=1.8, dash="6,3")
    curve(c, lambda t: math.exp(-9 * t), ts, px2, oy2, h2, 30, 220, col="ACC", w=1.6, dash="2,3")
    text(c, (ox2 - 10, oy2 - h2 + 4), "1", col="HEAD", anchor="end", size=11)
    text(c, (ox2 + w2 * 0.5, 24), "Time factors exp(−λₙt)", col="HEAD", anchor="middle", size=13, weight="700")
    text(c, (ox2 + w2 * 0.5, 248), "Higher modes (n ≥ 2) decay n² times faster", col="TEXT", anchor="middle", size=11)
    return c


def fig_step_partial_sums():
    """Computed partial sums S_1, S_5, S_15 of the lecturer's step function (Notes pp. 10-11)."""
    c = Canvas(680, 290)
    ox, oy = 340.0, 215.0
    sx, sy = 140.0, 130.0
    px = lambda x: ox + x * sx
    py = lambda y: oy - y * sy

    arrow(c, (32, oy), (655, oy), col="EDGE", w=1.4, size=7)
    arrow(c, (ox, 255), (ox, 25), col="EDGE", w=1.4, size=7)
    text(c, (660, oy + 4), "x", col="HEAD", size=12, weight="700")
    text(c, (ox + 8, 32), "f(x)", col="HEAD", size=12, weight="700")

    # Ticks
    for v, lab in [(-2, "−2L"), (-1, "−L"), (1, "L"), (2, "2L")]:
        line(c, (px(v), oy - 4), (px(v), oy + 4), col="EDGE", w=1.2)
        text(c, (px(v), oy + 18), lab, col="HEAD", anchor="middle", size=11)
    text(c, (ox - 10, py(1) + 4), "1", col="HEAD", anchor="end", size=11)
    text(c, (ox - 10, py(0.5) + 4), "½", col="HEAD", anchor="end", size=11)

    # Exact periodic step function (period 2 in units of L)
    for a, b, val in [(-2, -1, 1), (-1, 0, 0), (0, 1, 1), (1, 2, 0)]:
        line(c, (px(a), py(val)), (px(b), py(val)), col="HEAD", w=2.2)

    def s_n(x, N):
        s = 0.5
        for m in range(1, N + 1, 2):
            s += (2.0 / (m * math.pi)) * math.sin(m * math.pi * x)
        return s

    xs = [-2.0 + i * 0.01 for i in range(401)]
    curve(c, lambda x: s_n(x, 1), xs, px, oy, sy, 28, 250, col="ACC", w=1.4, dash="5,4")
    curve(c, lambda x: s_n(x, 5), xs, px, oy, sy, 28, 250, col="GREEN", w=1.7)
    curve(c, lambda x: s_n(x, 15), xs, px, oy, sy, 28, 250, col="BLUE", w=2.0)

    # Midpoint dots at jumps
    for j in (-1, 0, 1):
        dot(c, (px(j), py(0.5)), r=4.0, col="PINK")

    text(c, (340, 276), "Exact step (black) · S₁ (dashed orange) · S₅ (green) · S₁₅ (blue) · Jump midpoint ½ (pink)",
         col="TEXT", anchor="middle", size=11)
    return c


def fig_sawtooth_partial_sums():
    """Computed partial sums S_1, S_5, S_15 of f(x) = x on [-L, L] (Notes pp. 11-12)."""
    c = Canvas(680, 290)
    ox, oy = 340.0, 145.0
    sx, sy = 140.0, 90.0
    px = lambda x: ox + x * sx
    py = lambda y: oy - y * sy

    arrow(c, (32, oy), (655, oy), col="EDGE", w=1.4, size=7)
    arrow(c, (ox, 258), (ox, 24), col="EDGE", w=1.4, size=7)
    text(c, (660, oy + 4), "x", col="HEAD", size=12, weight="700")
    text(c, (ox + 8, 30), "y", col="HEAD", size=12, weight="700")

    for v, lab in [(-2, "−2L"), (-1, "−L"), (1, "L"), (2, "2L")]:
        line(c, (px(v), oy - 4), (px(v), oy + 4), col="EDGE", w=1.2)
        text(c, (px(v), oy + 18), lab, col="HEAD", anchor="middle", size=11)
    text(c, (ox - 10, py(1) + 4), "L", col="HEAD", anchor="end", size=11)
    text(c, (ox - 10, py(-1) + 4), "−L", col="HEAD", anchor="end", size=11)

    # Exact 2L-periodic extension of f(x) = x
    for k in (-2, 0, 2):
        a, b = max(-2.0, k - 1.0), min(2.0, k + 1.0)
        line(c, (px(a), py(a - k)), (px(b), py(b - k)), col="HEAD", w=2.0)

    def s_n(x, N):
        return sum((2.0 / (n * math.pi)) * ((-1) ** (n + 1)) * math.sin(n * math.pi * x) for n in range(1, N + 1))

    xs = [-2.0 + i * 0.01 for i in range(401)]
    curve(c, lambda x: s_n(x, 1), xs, px, oy, sy, 26, 255, col="ACC", w=1.4, dash="5,4")
    curve(c, lambda x: s_n(x, 5), xs, px, oy, sy, 26, 255, col="GREEN", w=1.7)
    curve(c, lambda x: s_n(x, 15), xs, px, oy, sy, 26, 255, col="BLUE", w=2.0)

    for j in (-1, 1):
        dot(c, (px(j), oy), r=4.0, col="PINK")

    text(c, (340, 278), "2L-periodic sawtooth of f(x)=x (black) · S₁ (dashed orange) · S₅ (green) · S₁₅ (blue) · Jumps at ±L converge to 0",
         col="TEXT", anchor="middle", size=11)
    return c


def fig_even_odd_ext():
    """Even (cosine) vs odd (sine) 2L-periodic extensions of f(x) = x on [0, L] (Notes p. 12)."""
    c = Canvas(680, 260)
    # Left: Even extension (triangle wave, continuous!)
    ox1, oy1 = 175.0, 185.0
    sx, sy = 62.0, 95.0
    px1 = lambda x: ox1 + x * sx
    py1 = lambda y: oy1 - y * sy
    arrow(c, (24, oy1), (328, oy1), col="EDGE", w=1.3, size=7)
    arrow(c, (ox1, 215), (ox1, 45), col="EDGE", w=1.3, size=7)
    pts_even = [(px1(x), py1(abs(x - 2 * round(x / 2)))) for x in [-2, -1, 0, 1, 2]]
    poly(c, pts_even, col="BLUE", w=2.2)
    line(c, (px1(0), py1(0)), (px1(1), py1(1)), col="ACC", w=3.2)
    for v, lab in [(-2, "−2L"), (-1, "−L"), (1, "L"), (2, "2L")]:
        text(c, (px1(v), oy1 + 16), lab, col="HEAD", anchor="middle", size=10)
    text(c, (ox1, 24), "Even extension (cosine series)", col="HEAD", anchor="middle", size=13, weight="700")
    text(c, (ox1, 242), "Continuous everywhere (no jumps at 0 or ±L)", col="TEXT", anchor="middle", size=11)

    # Right: Odd extension (sawtooth, jumps at +/- L)
    ox2, oy2 = 510.0, 130.0
    px2 = lambda x: ox2 + x * sx
    py2 = lambda y: oy2 - y * 65.0
    arrow(c, (360, oy2), (664, oy2), col="EDGE", w=1.3, size=7)
    arrow(c, (ox2, 215), (ox2, 45), col="EDGE", w=1.3, size=7)
    for k in (-2, 0, 2):
        a, b = max(-2.0, k - 1.0), min(2.0, k + 1.0)
        line(c, (px2(a), py2(a - k)), (px2(b), py2(b - k)), col="GREEN", w=2.2)
    line(c, (px2(0), py2(0)), (px2(1), py2(1)), col="ACC", w=3.2)
    for j in (-1, 1):
        dot(c, (px2(j), oy2), r=3.8, col="PINK")
    for v, lab in [(-2, "−2L"), (-1, "−L"), (1, "L"), (2, "2L")]:
        text(c, (px2(v), oy2 + 16), lab, col="HEAD", anchor="middle", size=10)
    text(c, (ox2, 24), "Odd extension (sine series)", col="HEAD", anchor="middle", size=13, weight="700")
    text(c, (ox2, 242), "Jumps at ±L (series converges to 0 there)", col="TEXT", anchor="middle", size=11)
    return c


def fig_robin_graphical():
    """Graphical solution of tan(z) = -z / (hL) for Robin BC phi'(L) + h*phi(L) = 0, h > 0 (Sheet 6 Ex. 6.1(iv))."""
    c = Canvas(680, 315)
    ox, oy = 70.0, 155.0
    sx, sy = 56.0, 28.0
    px = lambda z: ox + z * sx
    py = lambda y: oy - y * sy

    arrow(c, (55, oy), (645, oy), col="HEAD", w=1.5, size=7)
    arrow(c, (ox, 270), (ox, 24), col="HEAD", w=1.5, size=7)
    text(c, (650, oy + 4), "z = √λ L", col="HEAD", size=12, weight="700")
    text(c, (ox + 10, 32), "y", col="HEAD", size=12, weight="700")

    # Asymptotes at (k + 0.5)*pi
    for k in range(3):
        za = (k + 0.5) * math.pi
        line(c, (px(za), 32), (px(za), 262), col="EDGE", w=1.1, dash="4,4")
        text(c, (px(za), 278), f"{2*k+1}π/2", col="TEXT", anchor="middle", size=10)

    # tan(z) branches
    branches = [(0.0, 1.43), (1.71, 4.56), (4.86, 7.70), (8.00, 9.8)]
    for a, b in branches:
        zs = [a + (b - a) * i / 80.0 for i in range(81)]
        curve(c, math.tan, zs, px, oy, sy, 32, 260, col="BLUE", w=2.0)

    # Line y = -z / (hL) with hL = 2.0
    hL = 2.0
    line(c, (px(0), py(0)), (px(9.6), py(-9.6 / hL)), col="ACC", w=2.1)
    text(c, (px(5.7), py(-2.85) + 26), "y = −z / (hL)", col="ACC", size=12, weight="700")

    # Find first 3 positive roots by bisection and mark them
    for k, (lo, hi) in enumerate([(1.7, 3.14), (4.85, 6.28), (8.0, 9.42)], 1):
        a, b = lo, hi
        for _ in range(40):
            mid = 0.5 * (a + b)
            if math.tan(mid) + mid / hL < 0:
                a = mid
            else:
                b = mid
        z_root = 0.5 * (a + b)
        dot(c, (px(z_root), py(-z_root / hL)), r=4.5, col="PINK")
        dy = 16 if k < 3 else -10
        text(c, (px(z_root) + 8, py(-z_root / hL) + dy), sub("z", str(k)), col="PINK", size=11, weight="700")

    text(c, (355, 304), "Intersections zₙ = √λₙ L lie in ((2n−1)π/2, nπ) and approach (2n−1)π/2 as n → ∞",
         col="TEXT", anchor="middle", size=11)
    return c


def build():
    reg = Registry("AM-T6")
    # Official book crops (Screenshot-First, Haberman BookPDE's.pdf)
    reg.raster("hab-fig-3-1-4-periodic", "Periodic extension of a non-periodic function",
               "The 2L-periodic extension of f(x) = (3/2)x (original function dashed outside [−L, L]). Copied from Haberman, Fig. 3.1.4, p. 77", width=480)
    reg.raster("hab-fig-3-2-2-step", "Fourier series of a step function",
               "Fourier series of Haberman's step function (jump at x = L/2), with × marking the midpoint ½ at every jump. Copied from Haberman, Fig. 3.2.2, p. 79", width=520)
    reg.raster("hab-fig-3-4-1-diff", "Fourier sine series of f(x) = x",
               "Fourier sine series of f(x) = x on 0 ≤ x ≤ L: jumps at odd multiples of L prevent term-by-term differentiation. Copied from Haberman, Fig. 3.4.1, p. 100", width=420)

    # Computed SVGs (EXTRA: not printed in Haberman)
    reg.put("t6-heat-modes", fig_heat_modes(), "Heat equation spatial eigenfunctions and time decay",
            "First three Dirichlet eigenfunctions φₙ(x) = sin(nπx/L) (left) and their exponential decay factors Tₙ(t) = exp(−λₙt) (right) (Notes09-12-Nov.pdf, pp. 4-5)")  # EXTRA
    reg.put("t6-step-partial-sums", fig_step_partial_sums(), "Partial sums of the step function Fourier series",
            "Computed partial sums S₁, S₅ and S₁₅ for the step function of Notes09-12-Nov.pdf, pp. 10-11 (f = 1 on (0, L), 0 on (−L, 0]): convergence to ½ at jumps x = 0, ±L")  # EXTRA
    reg.put("t6-sawtooth-partial-sums", fig_sawtooth_partial_sums(), "Partial sums of f(x) = x on [-L, L]",
            "Computed partial sums S₁, S₅ and S₁₅ of f(x) = x on [−L, L] with bₙ = 2L(−1)^(n+1)/(nπ), converging to 0 at jumps x = ±L (Notes09-12-Nov.pdf, pp. 11-12)")  # EXTRA
    reg.put("t6-even-odd-ext", fig_even_odd_ext(), "Even and odd periodic extensions on [0, L]",
            "Even 2L-periodic extension (cosine series, continuous) vs odd 2L-periodic extension (sine series, jumps at ±L) of f(x) = x given on [0, L] (Notes09-12-Nov.pdf, p. 12)")  # EXTRA
    reg.put("t6-robin-graphical", fig_robin_graphical(), "Graphical solution of the Robin eigenvalue equation",
            "Graphical determination of the positive eigenvalues of φ'' + λφ = 0 with φ(0) = 0 and φ'(L) + hφ(L) = 0 (h > 0): intersections of tan(z) and −z/(hL) (Haberman, Sec. 5.8, p. 169; Sheet 6, Ex. 6.1(iv))")  # EXTRA
    return reg
