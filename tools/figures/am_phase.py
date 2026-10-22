"""Phase-portrait figures for Advanced Maths, Topic 4 (sections 7 and 8).

Every portrait is drawn from the exact solution of the canonical system in the
z-plane (z = Q^-1 x) and, when a matrix Q is given, mapped to the x-plane by
x = Q z.  Stdlib only; the markup reuses the classes of the topic page
(.ax, .eig, .c1 ..., .ah1 ..., .st, .un, .semi).

Public entry point: FIGURES, a dict {name: html} of ready <figure> blocks that
tools/am_phase_build.py splices into subjects/advanced-maths/teoria/topic-4.html.
"""
import math

BOX0, BOXW = 14.0, 202.0
CX = CY = BOX0 + BOXW / 2.0


def _f(v):
    return f"{v:.1f}"


def _matvec(Q, p):
    return (Q[0][0] * p[0] + Q[0][1] * p[1], Q[1][0] * p[0] + Q[1][1] * p[1])


def _sigma_max(Q):
    a = Q[0][0] ** 2 + Q[1][0] ** 2
    b = Q[0][0] * Q[0][1] + Q[1][0] * Q[1][1]
    d = Q[0][1] ** 2 + Q[1][1] ** 2
    tr, det = a + d, a * d - b * b
    return math.sqrt(tr / 2.0 + math.sqrt(max(tr * tr / 4.0 - det, 0.0)))


def sample(fn, t0, t1, n, bound):
    """Pieces of the curve t -> fn(t), t in [t0, t1], that stay inside |coords| <= bound."""
    pieces, cur = [], []
    for i in range(n + 1):
        t = t0 + (t1 - t0) * i / n
        p = fn(t)
        if abs(p[0]) <= bound and abs(p[1]) <= bound:
            cur.append(p)
        else:
            if len(cur) > 1:
                pieces.append(cur)
            cur = []
    if len(cur) > 1:
        pieces.append(cur)
    return pieces


class Panel:
    """One square phase-portrait panel (math coordinates, half-width R)."""

    def __init__(self, uid, title, R, axes=("", ""), eq="st"):
        self.uid, self.title, self.R, self.axes, self.eq = uid, title, R, axes, eq
        self.s = (BOXW / 2.0) / R
        self.parts = []

    def px(self, p):
        return CX + self.s * p[0], CY - self.s * p[1]

    # -- primitives ---------------------------------------------------------
    def axis_lines(self):
        self.parts.append(f'<line class="ax" x1="{_f(BOX0)}" y1="{_f(CY)}" x2="{_f(BOX0 + BOXW)}" y2="{_f(CY)}"/>')
        self.parts.append(f'<line class="ax" x1="{_f(CX)}" y1="{_f(BOX0 + BOXW)}" x2="{_f(CX)}" y2="{_f(BOX0)}"/>')

    def axis_labels(self):
        a, b = self.axes
        if a:
            self.parts.append(f'<text class="small halo" x="{_f(BOX0 + BOXW - 4)}" y="{_f(CY - 5)}" text-anchor="end">{a}</text>')
        if b:
            self.parts.append(f'<text class="small halo" x="{_f(CX - 5)}" y="{_f(BOX0 + 11)}" text-anchor="end">{b}</text>')

    def eig_line(self, d, label="", cls="eig dash"):
        n = math.hypot(*d)
        d = (d[0] / n, d[1] / n)
        L = 3.0 * self.R
        a, b = self.px((-L * d[0], -L * d[1])), self.px((L * d[0], L * d[1]))
        self.parts.append(f'<line class="{cls}" x1="{_f(a[0])}" y1="{_f(a[1])}" x2="{_f(b[0])}" y2="{_f(b[1])}"/>')
        if label:
            e = self.R / max(abs(d[0]), abs(d[1]))
            tip = self.px((0.8 * e * d[0], 0.8 * e * d[1]))
            nx, ny = d[1], d[0]  # screen-space perpendicular to the line
            self.parts.append(
                f'<text class="small halo" x="{_f(tip[0] + 10 * nx)}" y="{_f(tip[1] + 10 * ny + 3)}" text-anchor="middle">{label}</text>')

    def arrow(self, p, d, cls):
        n = math.hypot(*d)
        if n == 0:
            return
        ux, uy = d[0] / n, -d[1] / n  # screen direction
        x, y = self.px(p)
        tip = (x + 4.6 * ux, y + 4.6 * uy)
        b = (x - 3.4 * ux, y - 3.4 * uy)
        l, r = (b[0] - 3.4 * uy, b[1] + 3.4 * ux), (b[0] + 3.4 * uy, b[1] - 3.4 * ux)
        self.parts.append(
            f'<polygon class="{cls}" points="{_f(tip[0])},{_f(tip[1])} {_f(l[0])},{_f(l[1])} {_f(r[0])},{_f(r[1])}"/>')

    def traj(self, pieces, cls="c1", ah="ah1", fracs=(0.3, 0.7), thin=True):
        """Draw the pieces (ordered by increasing t) and put arrowheads along the longest one."""
        best, best_len, best_pts = None, -1.0, None
        for piece in pieces:
            pts = []
            for p in piece:
                q = self.px(p)
                if not pts or math.hypot(q[0] - pts[-1][0], q[1] - pts[-1][1]) >= 2.2:
                    pts.append(q)
                    continue
            if len(pts) < 2:
                continue
            d = "M" + " L".join(f"{_f(x)},{_f(y)}" for x, y in pts)
            self.parts.append(f'<path class="{cls}{" thin" if thin else ""}" d="{d}"/>')
            length = sum(math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(len(pts) - 1))
            if length > best_len:
                best, best_len, best_pts = piece, length, pts
        if not best_pts or best_len < 24:
            return
        cum = [0.0]
        for i in range(len(best_pts) - 1):
            cum.append(cum[-1] + math.hypot(best_pts[i + 1][0] - best_pts[i][0], best_pts[i + 1][1] - best_pts[i][1]))
        for fr in fracs:
            target = fr * best_len
            k = next(i for i in range(len(cum)) if cum[i] >= target)
            k = min(max(k, 1), len(best_pts) - 1)
            (x0, y0), (x1, y1) = best_pts[k - 1], best_pts[k]
            mid = ((x0 + x1) / 2.0, (y0 + y1) / 2.0)
            m = ((mid[0] - CX) / self.s, -(mid[1] - CY) / self.s)
            self.arrow(m, ((x1 - x0), -(y1 - y0)), ah)

    def mark(self, p, label=""):
        x, y = self.px(p)
        self.parts.append(f'<circle class="st" cx="{_f(x)}" cy="{_f(y)}" r="2.8"/>')
        if label:
            if x > CX + 55:
                self.parts.append(f'<text class="small halo" x="{_f(x - 6)}" y="{_f(y - 6)}" text-anchor="end">{label}</text>')
            else:
                self.parts.append(f'<text class="small halo" x="{_f(x + 6)}" y="{_f(y - 6)}">{label}</text>')

    # -- output -------------------------------------------------------------
    def svg(self, label):
        eq = {"st": "st", "un": "un", "semi": "semi"}[self.eq]
        head = (f'<svg viewBox="0 -6 230 236" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">'
                f'<defs><clipPath id="{self.uid}"><rect x="{_f(BOX0)}" y="{_f(BOX0)}" width="{_f(BOXW)}" height="{_f(BOXW)}"/></clipPath></defs>')
        body = "".join(self.parts)
        tail = (f'<circle class="{eq}" cx="{_f(CX)}" cy="{_f(CY)}" r="5"/>'
                f'<rect class="ax" x="{_f(BOX0)}" y="{_f(BOX0)}" width="{_f(BOXW)}" height="{_f(BOXW)}"/>'
                f'<text x="115" y="8" text-anchor="middle" class="small">{self.title}</text></svg>')
        return head + body_clip(self, body) + tail


def body_clip(panel, body):
    # the clipped group holds curves and lines; labels and axes names sit inside it too
    return f'<g clip-path="url(#{panel.uid})">{body}</g>'


# ---------------------------------------------------------------------------
# canonical flows in the z-plane
# ---------------------------------------------------------------------------
def spiral_flow(rho, omega, z0):
    def fn(t):
        e = math.exp(rho * t)
        c, s = math.cos(omega * t), math.sin(omega * t)
        return (e * (z0[0] * c + z0[1] * s), e * (-z0[0] * s + z0[1] * c))
    return fn


def jordan_flow(lam, z0):
    def fn(t):
        e = math.exp(lam * t)
        return (e * (z0[0] + z0[1] * t), e * z0[1])
    return fn


def node_flow(l1, l2, z0):
    def fn(t):
        return (z0[0] * math.exp(l1 * t), z0[1] * math.exp(l2 * t))
    return fn


def node_panel(uid, title, label, l1, l2, Q=None, R=1.0, Rview=None):
    """Portrait of x' = A x with Q^-1 A Q = diag(l1, l2), l1 != l2 real and non-zero.  Q None: draw the z-plane."""
    Rv = Rview or (R * (_sigma_max(Q) if Q else 1.0))
    eq = "st" if (l1 < 0 and l2 < 0) else "un"
    pan = Panel(uid, title, Rv, axes=("x₁", "x₂") if Q else ("z₁", "z₂"), eq=eq)
    pan.axis_lines()
    if Q:
        pan.eig_line(_matvec(Q, (1, 0)), "v₁", "eig dash")
        pan.eig_line(_matvec(Q, (0, 1)), "v₂", "eig dash")
    pan.axis_labels()
    bound = 1.2 * Rv
    to_plot = (lambda p: _matvec(Q, p)) if Q else (lambda p: p)
    T = math.log(400.0) / min(abs(l1), abs(l2))
    for k in range(16):
        a = 2 * math.pi * (k + 0.5) / 16
        z0 = (0.9 * R * math.cos(a), 0.9 * R * math.sin(a))
        fn = node_flow(l1, l2, z0)
        pan.traj(sample(lambda t, fn=fn: to_plot(fn(t)), -T, T, 6000, bound), fracs=(0.5,))
    # the two eigen-axes are orbits: four half-lines, arrows by the sign of the eigenvalue
    for d, lam in (((1, 0), l1), ((-1, 0), l1), ((0, 1), l2), ((0, -1), l2)):
        pts = [to_plot((d[0] * R * 1.3 * s / 40, d[1] * R * 1.3 * s / 40)) for s in range(1, 41)]
        if lam < 0:
            pts = pts[::-1]
        pan.traj([pts], cls="c3", ah="ah3", fracs=(0.55,), thin=False)
    return pan.svg(label)


def zero_panel(uid, title, label, l2, Q=None, R=1.0, Rview=None):
    """x' = A x with Q^-1 A Q = diag(0, l2): a line of equilibria (span v1) and straight orbits parallel to v2."""
    Rv = Rview or (R * (_sigma_max(Q) if Q else 1.0))
    pan = Panel(uid, title, Rv, axes=("x₁", "x₂") if Q else ("z₁", "z₂"), eq="semi")
    pan.axis_lines()
    if Q:
        pan.eig_line(_matvec(Q, (0, 1)), "v₂", "eig dash")
    pan.axis_labels()
    to_plot = (lambda p: _matvec(Q, p)) if Q else (lambda p: p)
    span = 3.0 * Rv
    a, b = to_plot((-span, 0)), to_plot((span, 0))
    pa, pb = pan.px(a), pan.px(b)
    pan.parts.append(f'<line class="c3" x1="{_f(pa[0])}" y1="{_f(pa[1])}" x2="{_f(pb[0])}" y2="{_f(pb[1])}"/>')
    for k in range(-6, 7):
        if k == 0:
            continue
        c = 1.25 * Rv * k / 6
        for sgn in (1, -1):
            pts = [to_plot((c, sgn * 1.3 * Rv * s / 40)) for s in range(1, 41)]
            if l2 < 0:
                pts = pts[::-1]
            pan.traj([pts], fracs=(0.5,))
        pan.mark(to_plot((c, 0)))
    return pan.svg(label)


def _ring(r, k, phase=0.0):
    return [(r * math.cos(phase + 2 * math.pi * i / k), r * math.sin(phase + 2 * math.pi * i / k)) for i in range(k)]


def spiral_panel(uid, title, label, rho, omega, Q=None, R=1.0, seeds=None, marks=(), arms=3):
    """Portrait of x' = A x with Q^-1 A Q = [[rho, omega], [-omega, rho]].  Q None: draw the z-plane."""
    Rv = R * (_sigma_max(Q) if Q else 1.0)
    eq = "st" if rho < 0 else ("un" if rho > 0 else "semi")
    pan = Panel(uid, title, Rv, axes=("x₁", "x₂") if Q else ("z₁", "z₂"), eq=eq)
    pan.axis_lines()
    if Q:
        pan.eig_line(_matvec(Q, (1, 0)), "u", "eig dash")
        pan.eig_line(_matvec(Q, (0, 1)), "w", "eig dash")
    pan.axis_labels()
    bound = 1.2 * Rv
    if rho == 0:
        seeds = seeds or [(0.4, 0), (0.7, 0), (1.0, 0)]
        period = 2 * math.pi / omega
        for z0 in seeds:
            fn = spiral_flow(0.0, omega, z0)
            g = (lambda t, fn=fn: _matvec(Q, fn(t))) if Q else fn
            pan.traj(sample(g, 0.0, period, 400, bound), fracs=(0.12, 0.62))
    else:
        seeds = seeds or _ring(1.0, arms)
        T = math.log(80.0) / abs(rho)
        for z0 in seeds:
            fn = spiral_flow(rho, omega, z0)
            g = (lambda t, fn=fn: _matvec(Q, fn(t))) if Q else fn
            t0, t1 = (0.0, T) if rho < 0 else (-T, 0.0)
            n = int(max(4000, T * omega * 60))
            pan.traj(sample(g, t0, t1, n, bound), fracs=(0.3, 0.72))
    for p, lab in marks:
        pan.mark(_matvec(Q, p) if Q else p, lab)
    return pan.svg(label)


def star_panel(uid, title, label, lam, R=1.0):
    pan = Panel(uid, title, R, axes=("x₁", "x₂"), eq="st" if lam < 0 else "un")
    pan.axis_lines()
    pan.axis_labels()
    for i in range(12):
        a = 2 * math.pi * i / 12 + math.pi / 12
        d = (math.cos(a), math.sin(a))
        r0, r1 = (0.96 * R, 0.0) if lam < 0 else (0.0, 0.96 * R)
        pts = [((r0 + (r1 - r0) * k / 40) * d[0], (r0 + (r1 - r0) * k / 40) * d[1]) for k in range(41)]
        pan.traj([pts], fracs=(0.5,))
    return pan.svg(label)


def _inv(Q):
    det = Q[0][0] * Q[1][1] - Q[0][1] * Q[1][0]
    return ((Q[1][1] / det, -Q[0][1] / det), (-Q[1][0] / det, Q[0][0] / det))


def jordan_panel(uid, title, label, lam, Q=None, R=1.0, Rview=None, marks=(), highlight=()):
    """Portrait of x' = A x with Q^-1 A Q = [[lam, 1], [0, lam]].  Seeds are laid out in the plane that is drawn."""
    Rv = Rview or (R * (_sigma_max(Q) if Q else 1.0))
    pan = Panel(uid, title, Rv, axes=("x₁", "x₂") if Q else ("z₁", "z₂"), eq="st" if lam < 0 else "un")
    pan.axis_lines()
    pan.eig_line(_matvec(Q, (1, 0)) if Q else (1, 0), "v₁" if Q else "", "eig dash")
    pan.axis_labels()
    bound = 1.2 * Rv
    T = 7.0 / abs(lam)
    n = 9000
    Qi = _inv(Q) if Q else None
    to_z = (lambda p: _matvec(Qi, p)) if Q else (lambda p: p)
    to_plot = (lambda p: _matvec(Q, p)) if Q else (lambda p: p)
    seeds = []
    for xs in (-0.9, -0.45, 0.0, 0.45, 0.9):
        seeds += [(xs * Rv, 0.9 * Rv), (xs * Rv, -0.9 * Rv)]
    seeds += [(0.9 * Rv, 0.3 * Rv), (0.9 * Rv, -0.3 * Rv), (-0.9 * Rv, 0.3 * Rv), (-0.9 * Rv, -0.3 * Rv)]
    seeds = [to_z(p) for p in seeds]

    def orbit(z0, **kw):
        fn = jordan_flow(lam, z0)
        pan.traj(sample(lambda t: to_plot(fn(t)), -T, T, n, bound), **kw)

    for z0 in seeds:
        orbit(z0, fracs=(0.35, 0.7))
    # the invariant eigen-line carries two orbits (c2 = 0): its two half-lines
    for sgn in (1, -1):
        orbit((sgn * 0.9 * Rv / (_sigma_max(Q) if Q else 1.0), 0.0), cls="c3", ah="ah3", fracs=(0.5,), thin=False)
    for z0 in highlight:
        orbit(z0, cls="c2", ah="ah2", fracs=(0.4,), thin=False)
    for p, lab in marks:
        pan.mark(to_plot(p), lab)
    return pan.svg(label)


# ---------------------------------------------------------------------------
# <figure> blocks
# ---------------------------------------------------------------------------
def _fig(panels, caption, trio=False):
    cls = "fig pair trio" if trio else "fig pair"
    inner = "".join(f"<div>{p}</div>" for p in panels)
    return f'<figure class="{cls}">{inner}<figcaption>{caption}</figcaption></figure>'


Q0 = ((1, 2), (1, 0))     # Example 7.3:  u = (1, 1),  w = (2, 0)
Q1 = ((5, 0), (-1, 3))    # Example 7.1:  u = (5, -1), w = (0, 3)
Q2 = ((2, 0), (1, -1))    # Example 7.2:  u = (2, 1),  w = (0, -1)
Q3 = ((2, 1), (1, 0))     # Example 8.1:  v1 = (2, 1), v2 = (1, 0)
Q3s = ((2, -1), (1, 0))   # stable twin:  v1 = (2, 1), v2' = (-1, 0)


def build():
    f = {}
    f["spirals_z"] = _fig([
        spiral_panel("am-sz1", "stable spiral: ρ = −0.3, ω = 1", "stable spiral in the z-plane", -0.3, 1.0),
        spiral_panel("am-sz2", "unstable spiral: ρ = 0.3, ω = 1", "unstable spiral in the z-plane", 0.3, 1.0),
        spiral_panel("am-sz3", "centre: ρ = 0, ω = 1", "centre in the z-plane", 0.0, 1.0),
    ], "<b>Figure 4.4.</b> The canonical complex system in the $\\mathbf z$-plane. All three turn <em>clockwise</em> ($\\dot\\theta = -\\omega$); the sign of $\\rho$ decides whether the radius shrinks, grows or stays fixed.", trio=True)
    f["ex71"] = _fig([
        spiral_panel("am-e1z", "z-plane: J = (1 3; −3 1)", "Example 7.1 in the z-plane", 1.0, 3.0, marks=[((1.0, 0.0), "(1,0)"), ((0.0, 1.0), "(0,1)")], R=1.25, arms=4),
        spiral_panel("am-e1x", "x-plane: x = Q z", "Example 7.1 in the x-plane", 1.0, 3.0, Q=Q1, marks=[((1.0, 0.0), ""), ((0.0, 1.0), "")], R=1.25, arms=4),
    ], "<b>Figure 4.5.</b> Example 7.1, $\\dot x = 2x + 5y$, $\\dot y = -2x$ (unstable spiral). Left: the canonical portrait. Right: the same orbits seen in the $(x_1, x_2)$-plane after $\\mathbf x = Q\\mathbf z$; the dashed lines are the images of the $z_1$- and $z_2$-axes, i.e. the lines through $\\mathbf u$ and $\\mathbf w$. Both turn clockwise because $\\det Q > 0$.")
    f["ex72"] = _fig([
        spiral_panel("am-e2z", "z-plane: J = (0 1; −1 0)", "Example 7.2 in the z-plane", 0.0, 1.0, marks=[((1.0, 0.0), "(1,0)")], R=1.25),
        spiral_panel("am-e2x", "x-plane: x = Q z", "Example 7.2 in the x-plane", 0.0, 1.0, Q=Q2, marks=[((1.0, 0.0), "")], R=1.25),
    ], "<b>Figure 4.6.</b> Example 7.2, $\\dot x = x - 2y$, $\\dot y = x - y$ (centre). The circles of the $\\mathbf z$-plane turn clockwise, but $\\det Q = -2 < 0$ reflects the plane, so the ellipses of the $\\mathbf x$-plane turn <em>counter-clockwise</em>.")
    f["ex73"] = _fig([
        spiral_panel("am-e0z", "z-plane: J = (−1 2; −2 −1)", "Example 7.3 in the z-plane", -1.0, 2.0, marks=[((1.0, 0.0), "(1,0)")], R=1.25),
        spiral_panel("am-e0x", "x-plane: x = Q z", "Example 7.3 in the x-plane", -1.0, 2.0, Q=Q0, marks=[((1.0, 0.0), "")], R=1.25),
    ], "<b>Figure 4.7.</b> Example 7.3, $\dot x = -5y$, $\dot y = x - 2y$ (stable spiral). The spiral turns clockwise in the $\mathbf z$-plane and counter-clockwise in the $\mathbf x$-plane, because $\det Q = -2 < 0$.")
    f["stars"] = _fig([
        star_panel("am-st1", "stable star: λ = −1", "stable star", -1.0),
        star_panel("am-st2", "unstable star: λ = 1", "unstable star", 1.0),
    ], "<b>Figure 4.8.</b> $A = \\lambda I$: every line through the origin is invariant and every solution moves along its own line. The picture is the same in any basis, so there is no separate $\\mathbf z$-plane.")
    f["improper_z"] = _fig([
        jordan_panel("am-jz1", "unstable improper node: J = (3 1; 0 3)", "improper node in the z-plane", 3.0, R=1.25, highlight=[(0.0, 1.0)]),
        jordan_panel("am-jz2", "stable improper node: J = (−3 1; 0 −3)", "stable improper node in the z-plane", -3.0, R=1.25, highlight=[(0.0, 1.0)]),
    ], "<b>Figure 4.9.</b> The canonical improper node in the $\\mathbf z$-plane. Amber: the invariant $z_1$-axis (the only eigendirection). Green: the orbit through $(0, 1)$. All orbits are tangent to the $z_1$-axis at the origin and become parallel to it at infinity; above the axis they move right, below it left.")
    f["ex82"] = _fig([
        jordan_panel("am-e3z", "z-plane: J = (3 1; 0 3)", "Example 8.1 in the z-plane", 3.0, R=1.25, highlight=[(0.0, 1.0)], marks=[((0.0, 1.0), "(0,1)")]),
        jordan_panel("am-e3x", "x-plane: x = Q z", "Example 8.1 in the x-plane", 3.0, Q=Q3, Rview=2.6, highlight=[(0.0, 1.0)], marks=[((0.0, 1.0), "(1,0)")]),
    ], "<b>Figure 4.10.</b> Example 8.1, $\\dot x = 5x - 4y$, $\\dot y = x + y$ (unstable improper node, $\\lambda = 3$). Left: canonical portrait. Right: the same orbits in the $(x_1, x_2)$-plane, with $\\mathbf v_1 = (2,1)^T$ and $\\mathbf v_2 = (1,0)^T$. The amber line is $\\mathrm{span}\\,\\mathbf v_1$; the green orbit is $\\mathbf x(t) = e^{3t}(2t+1,\\ t)^T$. Because $\\det Q = -1$, the map reverses orientation, so the S is traversed in the opposite sense to the one in the $\\mathbf z$-plane.")
    f["ex82s"] = _fig([
        jordan_panel("am-e4z", "z-plane: J = (−3 1; 0 −3)", "stable twin in the z-plane", -3.0, R=1.25, highlight=[(0.0, 1.0)]),
        jordan_panel("am-e4x", "x-plane: x = Q' z", "stable twin in the x-plane", -3.0, Q=Q3s, Rview=2.6, highlight=[(0.0, 1.0)]),
    ], "<b>Figure 4.11.</b> The stable twin $A' = -A = \\begin{pmatrix} -5 & 4 \\\\ -1 & -1\\end{pmatrix}$ ($\\lambda = -3$, $Q' = [\\mathbf v_1\\mid -\\mathbf v_2]$): the same curves with every arrow reversed.")
    f["real_z6a"] = _fig([
        node_panel("am-n1", "0 < λ₁ < λ₂ (1, 2)", "unstable node, lambda1 less than lambda2", 1.0, 2.0),
        node_panel("am-n2", "0 < λ₂ < λ₁ (2, 1)", "unstable node, lambda2 less than lambda1", 2.0, 1.0),
        node_panel("am-n3", "λ₁ < 0 < λ₂ (−1, 1)", "saddle, lambda1 less than 0 less than lambda2", -1.0, 1.0),
    ], "<b>Figure 4.1 (a).</b> The uncoupled system $\\dot z_1 = \\lambda_1z_1$, $\\dot z_2 = \\lambda_2z_2$ in the $\\mathbf z$-plane, with the orderings drawn in the class notes (p. 9). Amber: the axes, which are orbits. Unstable nodes leave the origin tangent to the axis of the eigenvalue with the smaller modulus; at a saddle the axis of the negative eigenvalue comes in and the other goes out.", trio=True)
    f["real_z6b"] = _fig([
        node_panel("am-n4", "λ₂ < λ₁ < 0 (−1, −2)", "stable node, lambda2 less than lambda1 less than 0", -1.0, -2.0),
        node_panel("am-n5", "λ₁ < λ₂ < 0 (−2, −1)", "stable node, lambda1 less than lambda2 less than 0", -2.0, -1.0),
        node_panel("am-n6", "λ₂ < 0 < λ₁ (1, −1)", "saddle, lambda2 less than 0 less than lambda1", 1.0, -1.0),
    ], "<b>Figure 4.1 (b).</b> The same with the arrows reversed: stable nodes, entering the origin tangent to the axis of the eigenvalue with the smaller modulus, and the other saddle. Each orbit is the curve $z_2 = \\tilde C\\,z_1^{\\lambda_2/\\lambda_1}$.", trio=True)
    f["zero_eig"] = _fig([
        zero_panel("am-zz", "z-plane: λ₁ = 0, λ₂ = −2", "zero eigenvalue in the z-plane", -2.0, R=1.25),
        zero_panel("am-zx", "x-plane: x = P z", "zero eigenvalue in the x-plane", -2.0, Q=((1, 1), (1, -1)), R=1.25, Rview=2.0),
    ], "<b>Figure 4.3.</b> A zero eigenvalue: $\\dot{\\mathbf x} = A\\mathbf x$ with $A = \\begin{pmatrix} -1 & 1 \\\\ 1 & -1\\end{pmatrix}$, $\\lambda_1 = 0$ with $\\mathbf v_1 = (1, 1)^T$ and $\\lambda_2 = -2$ with $\\mathbf v_2 = (1, -1)^T$. Amber: the line $\\operatorname{span}\\mathbf v_1$, made of equilibria (dots). Every other orbit is a straight segment parallel to $\\mathbf v_2$ that ends on that line, as in the sketch of the class notes.")
    return f


FIGURES = build()

if __name__ == "__main__":
    for k, v in FIGURES.items():
        print(k, len(v))
