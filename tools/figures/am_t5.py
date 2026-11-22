"""Figures for Advanced Maths Topic 5 — Coupled Nonlinear Systems and the Phase Plane.

Official textbook figures (Robinson 2004) are cropped at 200 DPI into vault/attachments/AM-T5/
and registered via REG.raster. Computed phase portraits, stability discs and the p-q diagram
from the lecturer's handwritten notes are generated as clean, theme-aware SVGs (EXTRA).
"""
import math
from .svgkit import Canvas, Registry, arrow, arrow_head, circle, curve, dot, fmt, line, pathd, poly, sub, text


def _rk4_traj(f, x0, y0, dt, steps, xlim, ylim):
    """Integrate (dx/dt, dy/dt) = f(x, y) with 4th-order Runge-Kutta; stop outside box."""
    pts = [(x0, y0)]
    x, y = x0, y0
    for _ in range(steps):
        k1x, k1y = f(x, y)
        k2x, k2y = f(x + 0.5 * dt * k1x, y + 0.5 * dt * k1y)
        k3x, k3y = f(x + 0.5 * dt * k2x, y + 0.5 * dt * k2y)
        k4x, k4y = f(x + dt * k3x, y + dt * k3y)
        nx = x + (dt / 6.0) * (k1x + 2 * k2x + 2 * k3x + k4x)
        ny = y + (dt / 6.0) * (k1y + 2 * k2y + 2 * k3y + k4y)
        if not (xlim[0] <= nx <= xlim[1] and ylim[0] <= ny <= ylim[1]):
            break
        if math.hypot(nx - x, ny - y) < 1e-6:
            break
        x, y = nx, ny
        pts.append((x, y))
    return pts


def _draw_orbit(c, pts, px, py, col="BLUE", w=1.5, arrow_fracs=(0.45,)):
    if len(pts) < 2:
        return
    spts = [(px(x), py(y)) for x, y in pts]
    # Subsample slightly to keep SVG lean
    thin = [spts[0]]
    for p in spts[1:]:
        if math.hypot(p[0] - thin[-1][0], p[1] - thin[-1][1]) >= 2.5:
            thin.append(p)
    if len(thin) < 2:
        return
    poly(c, thin, col=col, w=w)
    for fr in arrow_fracs:
        idx = max(1, min(len(thin) - 2, int(fr * (len(thin) - 1))))
        arrow_head(c, thin[idx - 1], thin[idx + 1], col, size=6.5)


def fig_stability_discs():
    """Planar Lyapunov stability vs asymptotic stability with discs of radius r and R (Notes pp. 5-6)."""
    c = Canvas(680, 260)
    # Left panel: Stable
    cx1, cy1 = 170, 140
    R, r = 82, 42
    circle(c, (cx1, cy1), R, col="EDGE", w=1.4, dash="5,4", fill="BLUE", opacity=0.06)
    circle(c, (cx1, cy1), r, col="BLUE", w=1.5, dash="4,3", fill="BLUE", opacity=0.10)
    dot(c, (cx1, cy1), r=4.2, col="HEAD")
    # Trajectory starting inside r, meandering inside R
    pts = []
    for i in range(90):
        t = i * 0.14
        rad = 32 + 24 * math.sin(0.55 * t) * math.exp(-0.02 * t)
        pts.append((cx1 + rad * math.cos(t), cy1 - rad * math.sin(t)))
    poly(c, pts, col="GREEN", w=1.8)
    arrow_head(c, pts[22], pts[24], "GREEN", size=7)
    dot(c, pts[0], r=3.2, col="GREEN")
    # Radius labels
    line(c, (cx1, cy1), (cx1 + r * 0.707, cy1 - r * 0.707), col="BLUE", w=1.1)
    text(c, (cx1 + 14, cy1 - 24), "r", col="BLUE", size=12, weight="700")
    line(c, (cx1, cy1), (cx1 - R * 0.85, cy1 - R * 0.52), col="EDGE", w=1.1)
    text(c, (cx1 - 54, cy1 - 36), "R", col="TEXT", size=12, weight="700")
    text(c, (cx1 + 6, cy1 + 15), "(x*, y*)", col="HEAD", size=11)
    text(c, (cx1, 24), "Stable (Lyapunov)", col="HEAD", anchor="middle", size=14, weight="700")
    text(c, (cx1, 244), "Starts inside r, stays inside R for all t > t0", col="TEXT", anchor="middle", size=11)

    # Right panel: Asymptotically stable
    cx2, cy2 = 505, 140
    circle(c, (cx2, cy2), R, col="EDGE", w=1.4, dash="5,4", fill="GREEN", opacity=0.05)
    circle(c, (cx2, cy2), r + 8, col="GREEN", w=1.5, dash="4,3", fill="GREEN", opacity=0.09)
    dot(c, (cx2, cy2), r=4.2, col="HEAD")
    pts2 = []
    for i in range(110):
        t = i * 0.12
        rad = 46 * math.exp(-0.22 * t)
        pts2.append((cx2 + rad * math.cos(1.2 * t), cy2 - rad * math.sin(1.2 * t)))
    poly(c, pts2, col="BLUE", w=1.8)
    arrow_head(c, pts2[18], pts2[20], "BLUE", size=7)
    dot(c, pts2[0], r=3.2, col="BLUE")
    line(c, (cx2, cy2), (cx2 + (r + 8) * 0.75, cy2 - (r + 8) * 0.66), col="GREEN", w=1.1)
    text(c, (cx2 + 28, cy2 - 36), sub("r", "0"), col="GREEN", size=12, weight="700")
    text(c, (cx2 + 8, cy2 + 15), "(x*, y*)", col="HEAD", size=11)
    text(c, (cx2, 24), "Asymptotically stable", col="HEAD", anchor="middle", size=14, weight="700")
    text(c, (cx2, 244), "Stable, and trajectories inside r0 tend to (x*, y*)", col="TEXT", anchor="middle", size=11)
    return c


def fig_pq_diagram():
    """The p-q stability diagram for lambda^2 + p*lambda + q = 0 (Notes p. 7)."""
    c = Canvas(680, 380)
    ox, oy = 340.0, 245.0
    sx, sy = 56.0, 46.0
    px = lambda p: ox + p * sx
    py = lambda q: oy - q * sy

    # Axes
    arrow(c, (60, oy), (620, oy), col="HEAD", w=1.8, size=8)
    arrow(c, (ox, 355), (ox, 30), col="HEAD", w=1.8, size=8)
    text(c, (626, oy + 5), "p = -tr(J)", col="HEAD", size=12, weight="700")
    text(c, (ox + 10, 38), "q = det(J)", col="HEAD", size=12, weight="700")

    # Parabola q = p^2 / 4
    xs = [-4.0 + i * 0.08 for i in range(101)]
    curve(c, lambda p: 0.25 * p * p, xs, px, oy, sy, 38, 350, col="ACC", w=2.4)
    text(c, (px(3.35), py(2.15)), "p² - 4q = 0", col="ACC", size=12, weight="700")

    # Centre line (q > 0, p = 0)
    line(c, (ox, oy), (ox, 48), col="GREEN", w=2.6)
    text(c, (ox + 10, 82), "Centres (p = 0, q > 0)", col="GREEN", size=12, weight="700")

    # Regions
    text(c, (px(-1.9), py(2.85)), "Unstable spirals", col="PINK", anchor="middle", size=13, weight="700")
    text(c, (px(2.0), py(2.85)), "Stable spirals", col="BLUE", anchor="middle", size=13, weight="700")
    text(c, (px(-3.6), py(0.75)), "Unstable nodes", col="PINK", anchor="middle", size=13, weight="700")
    text(c, (px(3.6), py(0.75)), "Stable nodes", col="BLUE", anchor="middle", size=13, weight="700")
    text(c, (px(0.0), py(-1.25)), "Saddle points (q < 0, always unstable)", col="PINK", anchor="middle", size=13, weight="700")

    # Parabola branch labels (clear of parabola curve)
    text(c, (px(-4.75), py(3.65)), "Unstable improper", col="ACC", anchor="middle", size=11)
    text(c, (px(-4.75), py(3.35)), "nodes / stars", col="ACC", anchor="middle", size=11)
    text(c, (px(4.75), py(3.65)), "Stable improper", col="ACC", anchor="middle", size=11)
    text(c, (px(4.75), py(3.35)), "nodes / stars", col="ACC", anchor="middle", size=11)

    # Degenerate axis label
    text(c, (px(3.3), py(-0.42)), "Degenerate cases (q = 0)", col="TEXT", anchor="middle", size=11)
    dot(c, (ox, oy), r=4.0, col="HEAD")
    return c


def fig_damped_pendulum_ksqrt2():
    """Computed phase portrait of the damped pendulum theta'=v, v'=-sqrt(2)v - sin(theta) (Notes pp. 13-14)."""
    c = Canvas(700, 320)
    k = math.sqrt(2.0)
    xlim, ylim = (-2.3 * math.pi, 2.3 * math.pi), (-3.2, 3.2)
    px = lambda x: 350.0 + (x / xlim[1]) * 310.0
    py = lambda y: 160.0 - (y / ylim[1]) * 125.0

    # Axes
    arrow(c, (32, 160), (672, 160), col="EDGE", w=1.4, size=7)
    arrow(c, (350, 295), (350, 24), col="EDGE", w=1.4, size=7)
    text(c, (676, 164), "θ", col="HEAD", size=13, weight="700")
    text(c, (356, 30), "v", col="HEAD", size=13, weight="700")

    f = lambda th, v: (v, -k * v - math.sin(th))
    # Integrate forward from a grid of seeds
    seeds = [
        (-6.8, 2.8), (-6.8, 1.9), (-6.8, 1.1), (-4.0, 2.9), (-1.5, 2.9), (1.0, 2.9), (3.8, 2.9),
        (6.8, -2.8), (6.8, -1.9), (6.8, -1.1), (4.0, -2.9), (1.5, -2.9), (-1.0, -2.9), (-3.8, -2.9),
        (-3.14159 + 0.08, 0.05), (-3.14159 - 0.08, -0.05),
        (3.14159 - 0.08, -0.05), (3.14159 + 0.08, 0.05),
        (0.0, 1.8), (0.0, -1.8), (2 * math.pi, 1.5), (-2 * math.pi, -1.5),
    ]
    for th0, v0 in seeds:
        pts = _rk4_traj(f, th0, v0, 0.04, 320, xlim, ylim)
        _draw_orbit(c, pts, px, py, col="BLUE", w=1.35, arrow_fracs=(0.35,))

    # Critical points: even m = stable spirals, odd m = saddles
    labels = [(-2 * math.pi, "-2π", True), (-math.pi, "-π", False), (0.0, "0", True),
              (math.pi, "π", False), (2 * math.pi, "2π", True)]
    for th, lab, is_spiral in labels:
        col = "GREEN" if is_spiral else "PINK"
        dot(c, (px(th), py(0)), r=4.5, col=col, fill=col if is_spiral else "none")
        text(c, (px(th), py(0) + 18), lab, col="HEAD", anchor="middle", size=11, weight="700")

    text(c, (350, 310), "Green dots: stable spirals at m even (0, ±2π)   ·   Pink circles: saddles at m odd (±π)",
         col="TEXT", anchor="middle", size=11)
    return c


def fig_double_well():
    """Computed double-well potential V(x)=x^4/2-x^2 and its phase portrait (Notes pp. 15-17, Ex. 5.4(ii))."""
    c = Canvas(680, 420)
    # Top panel: V(x) = 0.5 x^4 - x^2
    px = lambda x: 340.0 + x * 135.0
    py_v = lambda v: 105.0 - v * 58.0
    arrow(c, (60, py_v(0)), (620, py_v(0)), col="EDGE", w=1.3, size=7)
    arrow(c, (340, 165), (340, 22), col="EDGE", w=1.3, size=7)
    text(c, (625, py_v(0) + 4), "x", col="HEAD", size=12, weight="700")
    text(c, (348, 28), "V(x) = ½x⁴ − x²", col="HEAD", size=12, weight="700")
    xs = [-1.75 + i * 0.035 for i in range(101)]
    curve(c, lambda x: 0.5 * x**4 - x**2, xs, px, 105.0, 58.0, 24, 165, col="ACC", w=2.2)
    dot(c, (px(-1), py_v(-0.5)), r=4, col="GREEN")
    dot(c, (px(1), py_v(-0.5)), r=4, col="GREEN")
    dot(c, (px(0), py_v(0)), r=4, col="PINK", fill="none")
    text(c, (px(-1), py_v(-0.5) + 16), "min (−1, −½)", col="GREEN", anchor="middle", size=11)
    text(c, (px(1), py_v(-0.5) + 16), "min (1, −½)", col="GREEN", anchor="middle", size=11)

    # Bottom panel: phase portrait y = +/- sqrt(2(E - V(x)))
    py = lambda y: 295.0 - y * 48.0
    arrow(c, (60, 295), (620, 295), col="EDGE", w=1.3, size=7)
    arrow(c, (340, 405), (340, 185), col="EDGE", w=1.3, size=7)
    text(c, (625, 299), "x", col="HEAD", size=12, weight="700")
    text(c, (348, 192), "y = ẋ", col="HEAD", size=12, weight="700")

    f = lambda x, y: (y, -2.0 * x * (x * x - 1.0))
    # Low-energy closed orbits around (-1, 0) and (1, 0)
    for x0 in [0.55, 0.78, -0.55, -0.78]:
        pts = _rk4_traj(f, x0, 0.0, 0.025, 200, (-2.1, 2.1), (-2.2, 2.2))
        _draw_orbit(c, pts, px, py, col="GREEN", w=1.5, arrow_fracs=(0.25, 0.75))
    # Separatrix E = 0 (figure-eight homoclinic loops)
    for dx, dy in [(0.02, 0.028), (-0.02, -0.028)]:
        pts = _rk4_traj(f, dx, dy, 0.025, 300, (-2.1, 2.1), (-2.2, 2.2))
        _draw_orbit(c, pts, px, py, col="ACC", w=2.1, arrow_fracs=(0.35, 0.75))
    # High-energy enclosing orbits E > 0
    for y0 in [0.65, 1.25]:
        pts = _rk4_traj(f, 0.0, y0, 0.025, 320, (-2.1, 2.1), (-2.2, 2.2))
        _draw_orbit(c, pts, px, py, col="BLUE", w=1.4, arrow_fracs=(0.25, 0.75))

    dot(c, (px(-1), py(0)), r=4.2, col="GREEN")
    dot(c, (px(1), py(0)), r=4.2, col="GREEN")
    dot(c, (px(0), py(0)), r=4.2, col="PINK", fill="none")
    text(c, (px(-1), py(0) + 15), "−1", col="HEAD", anchor="middle", size=11, weight="700")
    text(c, (px(1), py(0) + 15), "+1", col="HEAD", anchor="middle", size=11, weight="700")
    text(c, (px(1.55), py(1.35)), "E > 0 (high energy)", col="BLUE", size=11, weight="700")
    text(c, (px(-2.22), py(-1.95)), "E = 0 (separatrix)", col="ACC", size=11, weight="700")
    return c


def fig_ex52_competition():
    """Computed portraits & nullclines for Ex. 5.2 (i) exclusion and (ii) coexistence (Solved_exer_nonlinear_system.pdf)."""
    c = Canvas(700, 320)

    def panel(ox, oy, title, f, null_x, null_y, eqs, seeds):
        sc = 92.0
        px = lambda x: ox + x * sc
        py = lambda y: oy - y * sc
        arrow(c, (ox - 10, oy), (ox + 265, oy), col="HEAD", w=1.5, size=7)
        arrow(c, (ox, oy + 10), (ox, oy - 235), col="HEAD", w=1.5, size=7)
        text(c, (ox + 268, oy + 4), "x", col="HEAD", size=12, weight="700")
        text(c, (ox + 8, oy - 228), "y", col="HEAD", size=12, weight="700")
        text(c, (ox + 130, 22), title, col="HEAD", anchor="middle", size=13, weight="700")

        # Nullclines
        line(c, (px(null_x[0][0]), py(null_x[0][1])), (px(null_x[1][0]), py(null_x[1][1])), col="ACC", w=1.5, dash="6,4")
        line(c, (px(null_y[0][0]), py(null_y[0][1])), (px(null_y[1][0]), py(null_y[1][1])), col="GREEN", w=1.5, dash="3,3")

        for x0, y0 in seeds:
            pts = _rk4_traj(f, x0, y0, 0.03, 280, (0.0, 2.75), (0.0, 2.4))
            _draw_orbit(c, pts, px, py, col="BLUE", w=1.35, arrow_fracs=(0.4,))

        for x, y, col, filled, lab, off in eqs:
            dot(c, (px(x), py(y)), r=4.5, col=col, fill=col if filled else "none")
            text(c, (px(x) + off[0], py(y) + off[1]), lab, col="HEAD", size=11, weight="700")

    # (i) Competitive exclusion: x' = x(2-x-y), y' = y(2-2x-2y)
    panel(
        45, 280, "Ex. 5.2 (i): Exclusion (x → 2, y → 0)",
        lambda x, y: (x * (2 - x - y), y * (2 - 2 * x - 2 * y)),
        ((0, 2), (2, 0)), ((0, 1), (1, 0)),
        [(0, 0, "PINK", False, "A(0,0)", (-16, 16)),
         (0, 1, "PINK", False, "B(0,1)", (-34, 4)),
         (2, 0, "GREEN", True, "C(2,0)", (-8, 16))],
        [(0.08, 0.15), (0.12, 0.08), (0.05, 0.85), (0.3, 2.1), (1.0, 2.1), (2.2, 1.8), (2.5, 0.5), (0.4, 1.3)]
    )

    # (ii) Coexistence: x' = x(2-x-y), y' = y(2-2y-x/4)
    panel(
        395, 280, "Ex. 5.2 (ii): Coexistence at D(8/7, 6/7)",
        lambda x, y: (x * (2 - x - y), y * (2 - 2 * y - 0.25 * x)),
        ((0, 2), (2, 0)), ((0, 1), (2.6, 1 - 2.6 / 8.0)),
        [(0, 0, "PINK", False, "A(0,0)", (-16, 16)),
         (0, 1, "PINK", False, "B(0,1)", (-34, 4)),
         (2, 0, "PINK", False, "C(2,0)", (-8, 16)),
         (8 / 7, 6 / 7, "GREEN", True, "D(8/7, 6/7)", (16, -24))],
        [(0.08, 0.12), (0.15, 0.06), (0.06, 0.9), (0.4, 2.1), (1.5, 2.0), (2.5, 1.5), (2.5, 0.25), (1.9, 0.08)]
    )
    text(c, (350, 312), "Dashed orange: ẋ = 0 nullcline   ·   Dotted green: ẏ = 0 nullcline", col="TEXT", anchor="middle", size=11)
    return c


def build():
    reg = Registry("AM-T5")
    # Official book crops (Screenshot-First)
    reg.raster("rob-fig-32-6-nullclines", "Nullclines of a planar system",
               "Nullclines and direction regions of a planar system. Copied from Robinson, Fig. 32.6, p. 313", width=420)
    reg.raster("rob-fig-35-2-pendulum-local", "Local phase portraits of the simple pendulum",
               "Local phase portraits near (−π, 0), (0, 0) and (π, 0) for the undamped pendulum. Copied from Robinson, Fig. 35.2, p. 354", width=620)
    reg.raster("rob-fig-35-4-pendulum-global", "Global phase portrait of the simple pendulum",
               "Phase portrait of the simple pendulum with the E = 1 separatrix in bold. Copied from Robinson, Fig. 35.4, p. 355", width=520)
    reg.raster("rob-fig-35-5-damped-pendulum", "Phase portrait of the damped pendulum",
               "Phase portrait of the damped pendulum (k = 1) on [−π, π]. Copied from Robinson, Fig. 35.5, p. 357", width=480)

    # Computed SVGs from handwritten notes (EXTRA: not printed in Robinson)
    reg.put("t5-stability-discs", fig_stability_discs(), "Planar Lyapunov and asymptotic stability discs",
            "Planar stability (left) and asymptotic stability (right) with discs of radius r, r₀ and R (Notes03-05-Nov_v2.pdf, pp. 5-6)")  # EXTRA
    reg.put("t5-pq-diagram", fig_pq_diagram(), "Stability diagram in the p-q plane",
            "Classification of linear critical points in the (p, q) plane for λ² + pλ + q = 0 with parabola p² − 4q = 0 (Notes03-05-Nov_v2.pdf, p. 7)")  # EXTRA
    reg.put("t5-damped-pendulum-ksqrt2", fig_damped_pendulum_ksqrt2(), "Damped pendulum phase portrait for k = sqrt(2)",
            "Computed global phase portrait of the damped pendulum with k = √2: stable spirals at even multiples of π and saddles at odd multiples (Notes03-05-Nov_v2.pdf, pp. 13-14)")  # EXTRA
    reg.put("t5-double-well", fig_double_well(), "Double-well potential and phase portrait",
            "Potential V(x) = ½x⁴ − x² (top) aligned with its phase portrait (bottom): two centres at (±1, 0), a saddle at (0, 0), the E = 0 figure-eight separatrix and high-energy orbits (Notes03-05-Nov_v2.pdf, pp. 15-17; Exercise 5.4(ii))")  # EXTRA
    reg.put("t5-ex52-competition", fig_ex52_competition(), "Competition models Exercise 5.2 (i) and (ii)",
            "Computed phase portraits and nullclines for Exercise 5.2 (i) (competitive exclusion, C(2, 0) a stable improper node) and Exercise 5.2 (ii) (coexistence at the stable node D(8/7, 6/7); Solved_exer_nonlinear_system.pdf, pp. 1-5)")  # EXTRA
    return reg
