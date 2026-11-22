"""Theory figures of Topic 2, part B (Notes.pdf Chapter 5 and Lecture 6): the harmonic oscillator (free, damped and forced
motion, resonance, linearisation) and the extension on the bead on a rotating hoop. Figures of part A are in t2.py.
Every curve is computed from the formulas of the note with the values of its brief."""
import math

from figures.em_theory import axis_in, axis_out, figure, fixed_axis, right_angle, triangle  # noqa: F401
from figures.em_th.t1 import ORANGE, MINUS, P3, _add, _circ3, _line3, _matrix, _mul, _poly3, _unit3, _v3, _vec3, dot1
from figures.em_th.t2 import _dbl, _dir, _pt
from figures.mech import S, Scene, bold
from figures.svgkit import fmt, rect as _rect

NAVY = "#1e3a8a"
BLUE2 = "#1d4ed8"
DORANGE = "#a16207"

TEXT = {
    't2-spring-mass': (
        'A block on a smooth floor attached to a wall by a spring and a damper, pulled by an applied force, and beside it its free-body diagram with the spring, damper and applied forces along the axis and the weight and floor reaction vertical.',
        'Spring-mass-damper system and the forces on the mass: $-k x\\,\\mathbf i$, $-\\lambda\\dot x\\,\\mathbf i$ and $F_x(t)\\,\\mathbf i$ along the line of motion; the weight and the reaction of the floor cancel ([Lecture 6, Slide 5]).'),
    't2-oscillator-potential': (
        'A parabolic potential energy curve cut by a horizontal energy level at two points minus a and a, the turning points of the oscillation.',
        'Potential energy of the harmonic oscillator $V(x) = \\tfrac12 k x^2$; an energy $E$ allows the motion between the turning points $\\pm a = \\pm\\sqrt{2E/k}$ (Notes.pdf Fig. 5.1; [Lecture 6, Slide 7]).'),
    't2-free-oscillation': (
        'A cosine oscillation of amplitude a starting at x zero with a positive slope, its period marked between two maxima, and an inset right triangle relating the constants C1 and C2 to the amplitude and the initial phase.',
        'Free undamped oscillation $x = a\\cos(\\omega_0 t + \\phi)$: amplitude $a$, period $\\tau = 2\\pi/\\omega_0$, and the constants $C_1 = a\\cos\\phi$, $C_2 = -a\\sin\\phi$ as the legs of a right triangle of hypotenuse $a$ (Notes.pdf Eqs. 5.10 to 5.12).'),
    't2-phasor': (
        'Two drawings of the complex plane: a phasor of constant length turning counterclockwise on a circle with its projection on the real axis, and a phasor spiralling towards the origin when the oscillation is damped.',
        'The complex solution as a phasor: it turns at the angular frequency on a circle of radius $a$ (left), or spirals in with modulus $a\\exp(-\\gamma t)$ when damped (right); the real part is the displacement (Notes.pdf Fig. 5.2; [Lecture 6, Slide 4]).'),
    't2-damped-responses': (
        'Three graphs of a released oscillator: a decaying oscillation inside an exponential envelope, a fast return to zero without oscillation, and a slow creeping return for heavy damping.',
        'Free response from $x_0 = 1$ m at rest for small ($\\gamma = 0.1\\,\\omega_0$), critical ($\\gamma = \\omega_0$) and large ($\\gamma = 2\\,\\omega_0$) damping, $\\omega_0 = 2\\pi\\ \\mathrm{rad/s}$ (Notes.pdf Fig. 5.3; [Lecture 6, Slides 8-10]).'),
    't2-decay-rates': (
        'The decay rate of the free oscillator against the damping ratio: one straight branch up to one, then splitting into a rising fast rate and a falling slow rate, so the slowest rate peaks at critical damping.',
        'Decay rates $-\\Re(p)$ against $\\gamma/\\omega_0$: the smaller decay rate of the two independent solutions is maximal, equal to $\\omega_0$, at critical damping ([Lecture 6, Slide 10]).'),
    't2-forced-triangle': (
        'Right triangles in the complex plane formed by the real part omega0 squared minus omega1 squared and the imaginary part two gamma omega1, below and above resonance, and two phasors showing the response lagging behind the force.',
        'The coefficient $\\omega_0^2 - \\omega_1^2 + 2i\\gamma\\omega_1$ of Eq. 5.38: its modulus is $(F_1/m)/a_1$ and its argument is $-\\phi_1$, below $90^\\circ$ under resonance and above it over resonance; the response phasor lags the force phasor by $\\lvert\\phi_1\\rvert$ (Notes.pdf Eqs. 5.38-5.42; [Lecture 6, Slide 12]).'),
    't2-beats': (
        'A fast oscillation whose amplitude swells and fades periodically inside a slowly varying sine envelope, and an inset where the amplitude grows linearly at exact resonance.',
        'Extension: beats of an undamped oscillator started at rest and driven at $\\omega_1 = 9\\ \\mathrm{rad/s}$ near $\\omega_0 = 10\\ \\mathrm{rad/s}$; at $\\omega_1 = \\omega_0$ the amplitude grows linearly (inset).'),
    't2-amplification': (
        'Amplification factor against the frequency ratio for five damping ratios, sharply peaked near one for small damping, and the phase lag falling from zero to minus pi through minus pi over two at ratio one.',
        'Amplification factor $a_1 k/F_1$ and phase lag $\\phi_1$ against $\\omega_1/\\omega_0$ for $\\gamma/\\omega_0 = 0.05$ to $1$; the dotted curve joins the maxima at $\\omega_1 = \\sqrt{\\omega_0^2 - 2\\gamma^2}$ (Notes.pdf Fig. 5.4; [Lecture 6, Slides 13-14]).'),
    't2-linearisation': (
        'The pendulum potential with an upward parabola fitted at its minimum and a downward parabola at its maximum, and below it the force with its tangent lines at the two equilibria.',
        'Linearisation about an equilibrium: near $x^*$ the force is replaced by its tangent line, slope $-k$, and the potential by a parabola; $k > 0$ at the minimum, $k < 0$ at the maximum ([Lecture 6, Slide 15]).'),
    't2-hoop': (
        'A circular hoop spinning about its vertical diameter with a bead on it, showing the fixed axes, the rotating basis of the hoop, the rotation angle Omega t and the bead angle theta.',
        'Extension: bead $P$ on a hoop of radius $b$ turning about its vertical diameter at the rate $\\Omega$; $\\mathcal B_h$ turns with the hoop and $\\theta$ is measured from the downward vertical in the plane of the hoop.'),
    't2-hoop-top': (
        'Top view of the spinning hoop with the fixed and rotating horizontal unit vectors, the rotation angle between them, their projection triangles and the change of basis matrix.',
        'Extension: view from above, $\\mathbf k$ out of the paper: $\\mathcal B_h$ is $\\mathcal B_0$ turned by $\\Omega t$ about $\\mathbf k$, which puts $-\\sin\\Omega t$ in entry $(1,2)$ of $[{}_0R_h]$.'),
    't2-hoop-plane': (
        'The plane of the hoop with the bead, the right triangle of the radius with the vertical, and the radial and tangential unit vectors at the bead.',
        'Extension: plane of the hoop, $\\mathbf j_h$ into the paper: $\\mathbf r_0^P = b\\sin\\theta\\,\\mathbf i_h - b\\cos\\theta\\,\\mathbf k = b\\,\\mathbf u_r$, and $\\mathbf u_\\theta$ is tangent to the hoop.'),
    't2-hoop-fbd': (
        'Free-body diagram of the bead with its weight split along and across the hoop and the two components of the reaction of the smooth hoop, one in its plane and one normal to it.',
        'Extension: forces on the bead: weight $m g\\cos\\theta\\,\\mathbf u_r - m g\\sin\\theta\\,\\mathbf u_\\theta$ and reaction $N_r\\,\\mathbf u_r + N_h\\,\\mathbf j_h$, with no tangential component.'),
    't2-hoop-potential': (
        'The effective potential of the bead for four rotation rates: a single well at the bottom below the critical rate, a flat bottom at the critical rate, and a double well with a hump at the bottom above it.',
        'Extension: effective potential $V_{\\mathrm{eff}} = m g b(1 - \\cos\\theta) - \\tfrac12 m b^2\\Omega^2\\sin^2\\theta$; above $\\Omega_c = \\sqrt{g/b}$ the bottom becomes a maximum and two minima appear at $\\pm\\theta_e$.'),
    't2-hoop-bifurcation': (
        'Bifurcation diagram of the bead: the bottom equilibrium is stable up to the critical rate and unstable after it, where two stable branches split off symmetrically and approach plus and minus pi over two.',
        'Extension: pitchfork bifurcation of the bead on the rotating hoop at $\\Omega = \\Omega_c$: the bottom loses its stability and the stable equilibria $\\pm\\theta_e$, $\\cos\\theta_e = \\Omega_c^2/\\Omega^2$, branch off.'),
}


def _fig(name):
    alt, cap = TEXT[name]
    return figure(name, alt, cap)


def _vb(name, sub=None, sup=None):
    return bold(name) + S("", sub, sup)


def _i(s):
    """Italic run inside a label that is otherwise upright."""
    return f'<tspan font-style="italic">{s}</tspan>'


def _w(sc, px, py):
    """World point of a pixel position."""
    return ((px - sc.o[0]) / sc.k, (sc.o[1] - py) / sc.k)


def _pl(sc, pts, col, w=1.8, dash=None, op=None):
    """Polyline through world points, with an optional stroke opacity."""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' stroke-opacity="{op}"' if op is not None else ""
    pp = " ".join(f"{fmt(x)},{fmt(y)}" for x, y in (sc.P(p) for p in pts))
    sc.c.add(f'<polyline points="{pp}" fill="none" stroke="{col}" stroke-width="{w}"{d}{o} stroke-linejoin="round"/>')


def _fn(f, a, b, n=400):
    return [(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)]


def _tick(sc, p, s, side="below", size=15, tl=0.07, dx=0, dy=0):
    """Axis tick at the world point p with its label (below a horizontal axis, left of a vertical one)."""
    if side == "below":
        sc.line(p, (p[0], p[1] - tl), "EDGE", 1.3)
        sc.label(p, s, "TEXT", "middle", size, italic=False, dy=21 + dy, dx=dx)
    else:
        sc.line(p, (p[0] - tl, p[1]), "EDGE", 1.3)
        sc.label(p, s, "TEXT", "end", size, italic=False, dx=-9 + dx, dy=5 + dy)


def _axes(sc, x0, x1, y0, y1, nx, ny, ox=0.0, oy=0.0, offx=(4, 24), offy=(12, 4), sizes=16):
    """Axes through (ox, oy) from x0 to x1 and y0 to y1, with the names at the tips."""
    sc.vec((x0, oy), (x1, oy), None, "EDGE", 1.4, head=8)
    sc.vec((ox, y0), (ox, y1), None, "EDGE", 1.4, head=8)
    sc.label((x1, oy), nx, "TEXT", "middle", sizes, weight="700", dx=offx[0], dy=offx[1])
    sc.label((ox, y1), ny, "TEXT", "start", sizes, weight="700", dx=offy[0], dy=offy[1])


W0 = S("ω", "0")
G0 = S("γ")


# --------------------------------------------------------------------------------------------------------------------
@_fig("t2-spring-mass")
def spring_mass():
    sc = Scene(930, 320, (50, 175), 60)
    sc.ground((0.0, -1.6), (0.0, 1.8), side=1)
    sc.line((0.0, 0.0), (6.6, 0.0), "HEAD", 1.4)
    bx0, bx1, bh = 3.0, 4.4, 1.4
    x, y = sc.P(bx0, bh)
    _rect(sc.c, x, y, (bx1 - bx0) * sc.k, bh * sc.k, "HEAD", 1.8, fill="EDGE", opacity=0.25)
    sc.label((3.7, 0.7), "m", "HEAD", "middle", 19, dy=6)
    sc.spring((0.0, 0.55), (bx0, 0.55), coils=7, amp=7.0, col="HEAD")
    sc.damper((0.0, 1.15), (bx0, 1.15), col="HEAD")
    sc.label((1.5, 0.55), "k", "HEAD", "middle", 18, dy=26)
    sc.label((1.5, 1.15), "λ", "HEAD", "middle", 18, dy=-24)
    sc.vec((bx1, 0.7), (5.9, 0.7), None, "PINK", 3.2, head=12)
    sc.label((5.15, 0.7), S("F", "x") + "(t)", "PINK", "middle", 18, weight="700", dy=-12)
    # axis Ox below the floor, unit vector i and the dimension line x
    O = (0.0, -0.8)
    sc.vec(O, (6.4, -0.8), None, "EDGE", 1.3, head=8)
    sc.label((6.4, -0.8), "x", "TEXT", "middle", 16, weight="700", dx=12, dy=5)
    sc.vec(O, (1.0, -0.8), bold("i"), "EDGE", 2.8, name_off=(0, -12), size=17, head=11)
    sc.dotp(O, 3.0, "HEAD")
    sc.label(O, "O", "HEAD", "start", 17, dx=-30, dy=-12)
    sc.line((3.7, 0.0), (3.7, -1.45), "EDGE", 1.1, "5 4")
    sc.dim((0.0, -1.3), (3.7, -1.3), "x", off=(0, 22))
    # free-body diagram
    P = (10.2, 0.9)
    sc.label((P[0] - 2.0, 2.3), "free-body diagram", "TEXT", "middle", 17, italic=False)
    h = 0.7
    sc.poly([(P[0] - h, P[1] - h), (P[0] + h, P[1] - h), (P[0] + h, P[1] + h), (P[0] - h, P[1] + h)], "EDGE", 1.6, "6 4", close=True)
    sc.vec(P, (P[0] - 2.3, P[1]), None, "PINK", 3.0, head=11)
    sc.label((P[0] - 2.3, P[1]), MINUS + "k x " + bold("i"), "PINK", "end", 17, dx=-8, dy=6)
    Q = (P[0], P[1] - 0.45)
    sc.vec(Q, (Q[0] - 1.4, Q[1]), None, "PINK", 3.0, head=11)
    sc.label((Q[0] - 1.4, Q[1]), MINUS + "λ" + dot1("x") + " " + bold("i"), "PINK", "end", 17, dx=-8, dy=6)
    sc.note((Q[0] - 1.4, Q[1]), "for " + _i("ẋ") + " > 0", "TEXT", "end", 14, dx=-8, dy=28)
    sc.vec(P, (P[0] + 2.0, P[1]), None, "PINK", 3.0, head=11)
    sc.label((P[0] + 2.0, P[1]), S("F", "x") + "(t) " + bold("i"), "PINK", "start", 17, dx=8, dy=6)
    sc.vec(P, (P[0], P[1] - 1.4), None, "PINK", 3.0, head=11)
    sc.label((P[0], P[1] - 1.4), MINUS + "m g " + bold("j"), "PINK", "middle", 17, dy=24)
    sc.vec(P, (P[0], P[1] + 1.4), None, "PINK", 3.0, head=11)
    sc.label((P[0], P[1] + 1.4), _vb("N", "s"), "PINK", "middle", 17, dy=-8)
    sc.dotp(P, 4.5, "HEAD")
    sc.label(P, "P", "HEAD", "start", 17, dx=8, dy=-8)
    B = (12.9, -0.6)
    sc.vec(B, (B[0] + 0.8, B[1]), bold("i"), "EDGE", 2.4, name_off=(10, 6), size=17, head=10)
    sc.vec(B, (B[0], B[1] + 0.8), bold("j"), "EDGE", 2.4, name_off=(-12, 4), size=17, head=10)
    axis_out(sc, B, bold("k"), "HEAD", off=(-16, 26))
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t2-oscillator-potential")
def oscillator_potential():
    sc = Scene(800, 430, (440, 350), 150)
    k, E = 2.0, 1.0
    a = math.sqrt(2 * E / k)
    ym = 2.15
    for sg in (-1, 1):
        x0, x1 = sg * a, sg * 1.5
        sc.poly([(x0, 0.0), (x1, 0.0), (x1, ym - 0.1), (x0, ym - 0.1)], "EDGE", 0.0, fill="EDGE", close=True, opacity=0.16)
        sc.note(((x0 + x1) / 2, 0.45), "forbidden", "TEXT", "middle", 13, dy=0)
    _axes(sc, -1.65, 1.65, -0.05, ym, "x", "V(x)", offx=(8, 24), offy=(12, 4))
    sc.poly([(x, 0.5 * k * x * x) for x, _ in _fn(lambda x: 0, -1.4, 1.4, 300)], "HEAD", 2.6)
    sc.line((-1.5, E), (1.5, E), "BLUE", 1.9, "8 5")
    sc.label((1.5, E), "E", "BLUE", "start", 19, weight="700", dx=8, dy=6)
    for sg in (-1, 1):
        sc.line((sg * a, 0.0), (sg * a, E), "EDGE", 1.2, "5 4")
        sc.dotp((sg * a, E), 5.0, "GREEN")
    _tick(sc, (-a, 0.0), MINUS + "a", dx=-4)
    _tick(sc, (a, 0.0), "a", dx=4)
    sc.label((0.0, 0.0), "0", "TEXT", "end", 15, italic=False, dx=-9, dy=20)
    # spring and mass sketch, upper left, as in the notes
    y0 = 1.85
    sc.ground((-2.75, y0 - 0.3), (-2.75, y0 + 0.3), side=1)
    sc.spring((-2.75, y0), (-2.25, y0), coils=4, amp=6.0, col="HEAD", lead=0.15)
    x, y = sc.P(-2.25, y0 + 0.17)
    _rect(sc.c, x, y, 0.34 * sc.k, 0.34 * sc.k, "HEAD", 1.6, fill="EDGE", opacity=0.25)
    sc.label((-2.5, y0), "k", "HEAD", "middle", 16, dy=-14)
    sc.label((-2.08, y0), "m", "HEAD", "middle", 16, dy=5)
    sc.line((-2.75, y0 - 0.3), (-1.9, y0 - 0.3), "HEAD", 1.2)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t2-free-oscillation")
def free_oscillation():
    sc = Scene(900, 450, (165, 240), 150)
    w0, a, phi = 2 * math.pi, 1.0, -math.pi / 3
    YS = 0.9

    def X(t):
        return a * math.cos(w0 * t + phi)

    _axes(sc, -0.1, 2.8, -1.28 * YS, 1.32 * YS, "t (s)", "x (m)", offx=(20, 6), offy=(12, 4))
    for t in (0.5, 1.0, 1.5, 2.0, 2.5):
        _tick(sc, (t, 0.0), f"{t:g}", dx=0, dy=0)
    for sg in (-1, 1):
        sc.line((0.0, sg * a * YS), (2.62, sg * a * YS), "EDGE", 1.3, "7 5")
    sc.label((0.0, a * YS), "a", "TEXT", "end", 17, dx=-9, dy=5)
    sc.label((0.0, -a * YS), MINUS + "a", "TEXT", "end", 17, dx=-9, dy=5)
    sc.poly([(t, X(t) * YS) for t, _ in _fn(lambda t: 0, 0.0, 2.5, 500)], "BLUE", 3.2)
    x0, v0 = X(0.0), -a * w0 * math.sin(phi)
    sc.line((-0.05, (x0 - 0.05 * v0) * YS), (0.05, (x0 + 0.05 * v0) * YS), ORANGE, 2.6)
    sc.dotp((0.0, x0 * YS), 4.5, "HEAD")
    sc.label((0.0, x0 * YS), S("x", "0"), "HEAD", "end", 17, dx=-12, dy=5)
    sc.label((-0.05, (x0 - 0.05 * v0) * YS), "slope " + dot1("x") + S("", "0"), ORANGE, "end", 17, dx=-8, dy=6)
    # first maximum and the period
    t1, t2 = -phi / w0, -phi / w0 + 1.0
    sc.line((t1, 0.0), (t1, 1.22 * YS), "EDGE", 1.2, "4 4")
    sc.line((t2, 0.0), (t2, 1.22 * YS), "EDGE", 1.2, "4 4")
    sc.line((t1, 0.0), (t1, -0.07), "HEAD", 1.8)
    sc.label((t1, 0.0), MINUS + "φ/" + W0, "HEAD", "middle", 17, dy=44, dx=2)
    _dbl(sc, (t1, 1.22 * YS), (t2, 1.22 * YS), "GREEN", 1.8, 9)
    sc.label(((t1 + t2) / 2, 1.22 * YS), "τ = 2π/" + W0, "GREEN", "middle", 17, dy=-10)
    # inset: the right triangle of the constants
    ox, oy, u = 710, 135, 150
    _rect(sc.c, 590, 18, 295, 262, "EDGE", 1.2, rx=8)
    sc.label(_w(sc, 737, 42), "constants", "TEXT", "middle", 17, italic=False)

    def I(a_, b_):
        return _w(sc, ox + u * a_, oy - u * b_)

    C1, C2 = a * math.cos(phi), -a * math.sin(phi)
    sc.vec(I(-0.15, 0), I(1.05, 0), None, "EDGE", 1.4, head=8)
    sc.label(I(1.05, 0), S("C", "1") + " direction", "TEXT", "end", 15, dy=-10, dx=2)
    tip = I(C1, -C2)
    O = I(0, 0)
    triangle(sc, [O, I(C1, 0), tip], "GREEN", 0.18)
    sc.line(O, tip, "HEAD", 2.4)
    sc.line(I(C1, 0), tip, "HEAD", 2.0)
    sc.line(O, I(C1, 0), "HEAD", 2.0)
    right_angle(sc, I(C1, 0), 180, 270, 0.07)
    sc.dotp(tip, 4.0, "HEAD")
    sc.label(I(C1 / 2, 0), S("C", "1") + " = a cos φ", "HEAD", "middle", 15, dy=-9)
    sc.label(I(C1, -C2 / 2), MINUS + S("C", "2") + " = a sin φ", "HEAD", "start", 15, dx=10, dy=5)
    sc.label(I(C1 / 2, -C2 / 2), "a", "HEAD", "middle", 17, dx=-14, dy=14)
    sc.arc(O, 0.2, 0, -60, "GREEN", 1.7, head=True)
    sc.label(I(0.31 * math.cos(math.radians(-27)), 0.31 * math.sin(math.radians(-27))), "φ", "GREEN", "middle", 16, dx=0, dy=7)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t2-phasor")
def phasor():
    sc = Scene(940, 450, (230, 262), 125)
    PHI, WT = 30.0, 70.0

    def plane(ox, title):
        sc.vec((ox - 1.4, 0.0), (ox + 1.5, 0.0), None, "EDGE", 1.4, head=8)
        sc.vec((ox, -1.35), (ox, 1.5), None, "EDGE", 1.4, head=8)
        sc.label((ox + 1.5, 0.0), "Re(z)", "TEXT", "start", 16, italic=False, dx=6, dy=5)
        sc.label((ox, 1.5), "Im(z)", "TEXT", "start", 16, italic=False, dx=10, dy=-4)
        sc.label((ox, 1.75), title, "TEXT", "middle", 18, italic=False)
        sc.dotp((ox, 0.0), 2.5, "HEAD")
        sc.label((ox, 0.0), "O", "HEAD", "start", 17, dx=7, dy=18)

    # undamped
    plane(0.0, "undamped")
    sc.circle((0.0, 0.0), 1.0, "HEAD", 1.3)
    A = _dir(PHI)
    z = _dir(PHI + WT)
    sc.vec((0, 0), A, None, "BLUE", 3.4, head=12)
    sc.label(A, "A = a exp(iφ)", "BLUE", "start", 17, weight="700", dx=10, dy=-4)
    sc.vec((0, 0), z, None, "BLUE", 3.4, head=12)
    sc.label(z, "z", "BLUE", "middle", 19, weight="700", dx=-8, dy=-12)
    sc.arc((0, 0), 0.28, 0, PHI, "GREEN", 1.7, head=True)
    sc.label(_pt((0, 0), PHI / 2 - 4, 0.50), "φ", "GREEN", "middle", 17, dx=8, dy=7)
    sc.arc((0, 0), 0.50, PHI, PHI + WT, "GREEN", 1.7, head=True)
    sc.label(_pt((0, 0), PHI + WT / 2, 0.70), W0 + "t", "GREEN", "middle", 17, dx=-4, dy=4)
    sc.line(z, (z[0], 0.0), ORANGE, 1.8, "6 4")
    sc.dotp((z[0], 0.0), 4.5, ORANGE)
    sc.label((z[0], 0.0), "x = Re(z)", ORANGE, "end", 17, dx=8, dy=26)
    sc.arc((0, 0), 1.2, 200, 245, "GREEN", 1.9, head=True)
    sc.label(_pt((0, 0), 222, 1.38), W0, "GREEN", "middle", 17, weight="700", dx=-6, dy=10)
    # damped
    ox = 3.4
    plane(ox, "damped")
    g = 0.1
    a_ = math.radians(PHI)
    pts = []
    for i in range(401):
        wt = 4 * math.pi * i / 400
        r = math.exp(-g * wt)
        pts.append((ox + r * math.cos(a_ + wt), r * math.sin(a_ + wt)))
    _pl(sc, pts, "BLUE", 1.6)
    sc.dotp((ox + A[0], A[1]), 4.0, "BLUE")
    sc.label((ox + A[0], A[1]), "A", "BLUE", "start", 17, weight="700", dx=9, dy=-6)
    wt = 2.5
    r = math.exp(-g * wt)
    tz = (ox + r * math.cos(a_ + wt), r * math.sin(a_ + wt))
    sc.circle((ox, 0.0), r, "EDGE", 1.5, "6 4")
    sc.vec((ox, 0.0), tz, None, "BLUE", 3.4, head=12)
    sc.label(tz, "z", "BLUE", "middle", 19, weight="700", dx=-8, dy=-12)
    sc.line(tz, (tz[0], 0.0), ORANGE, 1.8, "6 4")
    sc.dotp((tz[0], 0.0), 4.5, ORANGE)
    sc.label((ox, -1.0), "|z| = a exp(−γt)", "TEXT", "start", 17, italic=False, dx=10)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t2-damped-responses")
def damped_responses():
    sc = Scene(1150, 345, (70, 205), 95)
    w0 = 2 * math.pi
    gs = 0.1 * w0                       # small damping
    ws = math.sqrt(w0 * w0 - gs * gs)
    gl = 2 * w0                         # large damping
    r = math.sqrt(gl * gl - w0 * w0)
    gp, gm = gl + r, gl - r
    cm, cp = gp / (gp - gm), -gm / (gp - gm)
    T = 3.0
    titles = [(S("γ") + " &lt; " + W0 + " (small damping)"), (S("γ") + " = " + W0 + " (critical damping)"),
              (S("γ") + " &gt; " + W0 + " (large damping)")]
    for n in range(3):
        ox = n * 3.7

        def Pt(pts):
            return [(ox + t, y) for t, y in pts]

        sc.vec((ox - 0.1, 0.0), (ox + 3.3, 0.0), None, "EDGE", 1.4, head=8)
        sc.vec((ox, -1.15), (ox, 1.25), None, "EDGE", 1.4, head=8)
        sc.label((ox + 3.3, 0.0), "t (s)", "TEXT", "start", 15, weight="700", dx=6, dy=5)
        sc.label((ox, 1.25), "x (m)", "TEXT", "start", 15, weight="700", dx=8, dy=-2)
        for t in (1, 2, 3):
            _tick(sc, (ox + t, 0.0), str(t), size=14, dy=-10 + 22)
        for v in (-1, 1):
            sc.line((ox, v), (ox - 0.06, v), "EDGE", 1.3)
            sc.label((ox, v), MINUS + "1" if v < 0 else "1", "TEXT", "end", 14, italic=False, dx=-9, dy=5)
        sc.label((ox + 1.65, 1.62), titles[n], "HEAD", "middle", 18, italic=False)
        sc.dotp((ox, 1.0), 4.8, "HEAD")
    # small damping
    env = lambda t: math.exp(-gs * t)
    sc.poly([(t, y) for t, y in _fn(lambda t: env(t), 0, T, 200)], "EDGE", 1.5, "6 4")
    sc.poly([(t, y) for t, y in _fn(lambda t: -env(t), 0, T, 200)], "EDGE", 1.5, "6 4")
    sc.poly([(t, y) for t, y in _fn(lambda t: env(t) * (math.cos(ws * t) + gs / ws * math.sin(ws * t)), 0, T, 600)], "BLUE", 3.0)
    sc.label((1.15, env(1.15)), "±" + _i("a") + " exp(" + MINUS + _i("γ") + _i("t") + ")", "TEXT", "start", 15, italic=False, dx=14, dy=-12)
    # critical
    sc.poly([(3.7 + t, y) for t, y in _fn(lambda t: (1 + w0 * t) * math.exp(-w0 * t), 0, T, 400)], "BLUE", 3.0)
    # large
    sc.poly([(7.4 + t, y) for t, y in _fn(lambda t: cp * math.exp(-gp * t) + cm * math.exp(-gm * t), 0, T, 400)], "BLUE", 3.0)
    sc.poly([(7.4 + t, y) for t, y in _fn(lambda t: cm * math.exp(-gm * t), 0, T, 400)], "EDGE", 1.8, "6 4")
    sc.label((7.4 + 1.6, cm * math.exp(-gm * 1.6)), "slow term", "TEXT", "middle", 15, italic=False, dy=-14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t2-decay-rates")
def decay_rates():
    sc = Scene(830, 540, (90, 470), 240)
    YS = 0.55

    def Y(v):
        return v * YS

    _axes(sc, -0.05, 2.62, -0.04, 3.2 * YS, G0 + "/" + W0, "−Re(p)", offx=(34, 6), offy=(12, 4))
    sc.line((1.0, 0.0), (1.0, Y(3.0)), "EDGE", 1.3, "6 4")
    sg = lambda z: z - math.sqrt(max(z * z - 1, 0.0))
    up = lambda z: z + math.sqrt(max(z * z - 1, 0.0))
    zc = 1.0 + 0.0
    zt = 5.0 / 3.0
    seg = [(0.0, 0.0), (1.0, Y(1.0))]
    lo = [(z, Y(sg(z))) for z, _ in _fn(lambda z: 0, 1.0, 2.5, 300)]
    hi = [(z, Y(up(z))) for z, _ in _fn(lambda z: 0, 1.0, zt, 300)]
    sc.poly(hi, "HEAD", 1.6)
    for pts in (seg, lo):
        sc.poly(pts, "HEAD", 4.4)
        sc.poly(pts, "BLUE", 2.4)
    sc.label((0.5, Y(0.5)), G0, "HEAD", "middle", 20, dx=-16, dy=-6)
    sc.label((zt, Y(3.0)), "γ" + S("", "+"), "HEAD", "start", 19, dx=10, dy=6)
    sc.label((2.0, Y(sg(2.0))), "γ" + S("", "−"), "HEAD", "middle", 19, dy=-14)
    sc.dotp((1.0, Y(1.0)), 5.5, "BLUE")
    sc.note((1.0, Y(1.0)), "slowest rate maximal:", "BLUE", "start", 15, dx=16, dy=-26)
    sc.note((1.0, Y(1.0)), "critical damping", "BLUE", "start", 15, dx=16, dy=-8)
    _tick(sc, (0.0, 0.0), "0", dy=0, dx=-8)
    _tick(sc, (1.0, 0.0), "1")
    sc.line((0.0, Y(1.0)), (-0.05, Y(1.0)), "EDGE", 1.3)
    sc.label((0.0, Y(1.0)), W0, "TEXT", "end", 17, dx=-9, dy=5)
    sc.label((0.0, 0.0), "0", "TEXT", "end", 15, italic=False, dx=-9, dy=5)
    return sc


# --------------------------------------------------------------------------------------------------------------------
W1 = "ω" + S("", "1")
HYP = "√((" + W0 + "² − " + W1 + "²)² + 4γ²" + W1 + "²)"
FRAC = "= (F" + S("", "1") + "/m) / a" + S("", "1")


@_fig("t2-forced-triangle")
def forced_triangle():
    sc = Scene(1200, 400, (95, 320), 280)
    w0, g = 1.0, 0.15
    O1 = (0.0, 0.0)
    O2 = (1.95, 0.0)
    for O, w1, title in ((O1, 0.8, W1 + " &lt; " + W0), (O2, 1.25, W1 + " &gt; " + W0)):
        legx = w0 * w0 - w1 * w1
        legy = 2 * g * w1
        arg = math.degrees(math.atan2(legy, legx))
        tip = (O[0] + legx, legy)
        foot = (O[0] + legx, 0.0)
        right = legx > 0
        sc.vec((O[0] - 0.72, 0.0), (O[0] + 0.52, 0.0), None, "EDGE", 1.4, head=8)
        sc.vec((O[0], -0.12), (O[0], 0.72), None, "EDGE", 1.4, head=8)
        sc.label((O[0] + 0.52, 0.0), "Re", "TEXT", "start", 16, italic=False, dx=6, dy=5)
        sc.label((O[0], 0.72), "Im", "TEXT", "start", 16, italic=False, dx=8, dy=-2)
        sc.label((O[0] - 0.05, 0.98), title, "HEAD", "middle", 19, italic=False)
        triangle(sc, [O, foot, tip], "ACC", 0.20)
        sc.line(O, foot, "HEAD", 1.6)
        sc.line(foot, tip, "HEAD", 1.6)
        sc.vec(O, tip, None, "BLUE", 3.6, head=12)
        right_angle(sc, foot, 180 if right else 0, 90, 0.045)
        sc.dotp(O, 2.5, "HEAD")
        sc.arc(O, 0.13, 0, arg, "GREEN", 1.8, head=True)
        m = math.radians(arg / 2)
        sc.label((O[0] + 0.205 * math.cos(m), 0.205 * math.sin(m)), MINUS + "φ" + S("", "1"), "GREEN", "middle", 16,
                 dx=(2 if right else 16), dy=(8 if right else 8))
        if right:
            sc.label(O, "O", "HEAD", "end", 16, dx=-6, dy=18)
            sc.label(O, W0 + "² − " + W1 + "² (adjacent)", "HEAD", "start", 16, italic=False, dx=8, dy=26)
        else:
            sc.label(O, "O", "HEAD", "start", 16, dx=8, dy=18)
            sc.label(O, W0 + "² − " + W1 + "² (adjacent)", "HEAD", "end", 16, italic=False, dx=-8, dy=26)
        sc.label((foot[0], legy / 2), "2γ" + W1 + " (opposite)", "HEAD", "start" if right else "end", 16, italic=False,
                 dx=(12 if right else -12), dy=5)
        sc.label(tip, HYP, "BLUE", "start" if right else "middle", 16, italic=False, dx=(-40 if right else 10), dy=-40)
        sc.label(tip, FRAC, "BLUE", "start" if right else "middle", 16, italic=False, dx=(-40 if right else 10), dy=-20)
    # panel 3: phasors at one instant
    C = (3.16, 0.30)
    R = 0.45
    sc.label((C[0], 0.98), "phasors at one instant", "HEAD", "middle", 19, italic=False)
    sc.circle(C, R, "EDGE", 1.4)
    phi1 = -math.atan2(2 * g * 0.8, 1 - 0.64)
    af, ar = 60.0, 60.0 + math.degrees(phi1)
    sc.vec(C, _pt(C, af, 0.95 * R), None, "PINK", 3.4, head=12)
    sc.label(_pt(C, af, 1.12 * R), "force", "PINK", "middle", 17, weight="700", italic=False, dy=-8)
    sc.vec(C, _pt(C, ar, 0.72 * R), None, "BLUE", 3.4, head=12)
    sc.label(_pt(C, ar, 1.12 * R), "response", "BLUE", "start", 17, weight="700", italic=False, dx=4, dy=5)
    sc.dotp(C, 2.5, "HEAD")
    sc.arc(C, 0.30, ar, af, "GREEN", 1.8)
    sc.label(_pt(C, (af + ar) / 2 + 3, 1.12 * R), "|φ" + S("", "1") + "| (lag)", "GREEN", "start", 16, italic=False, dx=8, dy=-8)
    sc.arc(C, 0.55, 118, 170, "GREEN", 1.9, head=True)
    sc.label(_pt(C, 144, 0.64), W1, "GREEN", "middle", 17, weight="700", dx=-14, dy=0)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t2-beats")
def beats():
    sc = Scene(1010, 585, (95, 350), 52)
    w0, w1, F = 10.0, 9.0, 1.0
    B1 = F / (w0 * w0 - w1 * w1)
    YS = 18.0
    _axes(sc, -0.3, 15.8, -2.5, 3.0, "t (s)", "x (m)", offx=(26, 6), offy=(12, 4))
    for v in (-0.1, 0.1):
        sc.line((0.0, v * YS), (-0.12, v * YS), "EDGE", 1.3)
        sc.label((0.0, v * YS), (MINUS if v < 0 else "") + "0.1", "TEXT", "end", 14, italic=False, dx=-9, dy=5)
    for sg in (-1, 1):
        sc.line((0.0, sg * 2 * B1 * YS), (15.0, sg * 2 * B1 * YS), "EDGE", 1.3, "7 5")
    sc.label((15.0, 2 * B1 * YS), "2" + _i("B") + S("", "1"), "TEXT", "start", 16, italic=False, dx=8, dy=5)
    sc.label((15.0, -2 * B1 * YS), MINUS + "2" + _i("B") + S("", "1"), "TEXT", "start", 16, italic=False, dx=8, dy=5)
    env = lambda t: 2 * B1 * math.sin((w0 - w1) * t / 2)
    sc.poly([(t, y * YS) for t, y in _fn(lambda t: env(t) * math.sin((w0 + w1) * t / 2), 0, 15, 4500)], "BLUE", 1.2)
    sc.poly([(t, y * YS) for t, y in _fn(env, 0, 15, 600)], ORANGE, 1.8, "6 4")
    sc.poly([(t, -y * YS) for t, y in _fn(env, 0, 15, 600)], ORANGE, 1.8, "6 4")
    sc.label((math.pi, 2 * B1 * YS), "envelope", ORANGE, "middle", 17, italic=False, dy=-12)
    # time scale below the curve and the beat period
    yr = -2.3
    sc.line((0.0, yr), (15.3, yr), "EDGE", 1.2)
    for t in (5, 10, 15):
        sc.line((t, yr), (t, yr + 0.12), "EDGE", 1.3)
        sc.label((t, yr), str(t), "TEXT", "middle", 14, italic=False, dy=19)
    tb = 2 * math.pi / abs(w0 - w1)
    ya = -3.5
    for t in (0.0, tb):
        sc.line((t, 0.0), (t, ya - 0.15), "EDGE", 1.2, "4 4")
    _dbl(sc, (0.0, ya), (tb, ya), "GREEN", 1.8, 9)
    sc.label((tb / 2, ya), "beat period 2π/|" + W0 + " − " + W1 + "|", "GREEN", "middle", 17, italic=False, dy=26)
    # inset: exact resonance
    ox, oy = 640, 120
    _rect(sc.c, 585, 10, 400, 222, "EDGE", 1.2, rx=8)
    sc.label(_w(sc, 785, 34), W1 + " = " + W0, "HEAD", "middle", 18, italic=False)
    kt, kx = 46.0, 300.0
    I = lambda t, x: _w(sc, ox + kt * t, oy - kx * x)
    slope = F / (2 * w0)
    sc.vec(I(-0.2, 0), I(6.5, 0), None, "EDGE", 1.3, head=8)
    sc.vec(I(0, -0.34), I(0, 0.36), None, "EDGE", 1.3, head=8)
    sc.label(I(6.5, 0), "t", "TEXT", "middle", 15, weight="700", dx=10, dy=16)
    sc.label(I(0, 0.36), "x", "TEXT", "start", 15, weight="700", dx=8, dy=6)
    for sg in (-1, 1):
        sc.line(I(0, 0), I(6, sg * slope * 6), ORANGE, 1.8, "6 4")
    sc.poly([I(t, slope * t * math.sin(w0 * t)) for t, _ in _fn(lambda t: 0, 0, 6, 1800)], "BLUE", 1.2)
    return sc


# --------------------------------------------------------------------------------------------------------------------
ZETAS = (0.05, 0.1, 0.25, 0.5, 1.0)
ZCOL = [(NAVY, 1.0), (BLUE2, 1.0), ("BLUE", 1.0), ("BLUE", 0.62), ("BLUE", 0.38)]


def _amp(r, z):
    return 1.0 / math.sqrt((1 - r * r) ** 2 + 4 * z * z * r * r)


def _lag(r, z):
    return -math.atan2(2 * z * r, 1 - r * r)


@_fig("t2-amplification")
def amplification():
    sc = Scene(1170, 520, (140, 450), 150)
    AY = 0.2                              # world units per unit of amplification
    XR = (730 - 140) / 150.0              # world offset of the right graph
    Y0 = 1.9                              # world height of the zero of the phase (the bottom is -pi at height 0)
    RY = lambda ph: Y0 * (1 + ph / math.pi)
    rr = [i * 2.5 / 1500 for i in range(1501)]
    # ---- left graph
    sc.label((1.25, 2.62), "Amplification factor", "HEAD", "middle", 19, italic=False)
    _axes(sc, -0.05, 2.62, -0.04, 11.0 * AY + 0.1, "ω" + S("", "1") + "/" + W0, "a" + S("", "1") + "k/F" + S("", "1"), offx=(40, 6), offy=(12, 4))
    for t in (0.5, 1.0, 1.5, 2.0, 2.5):
        _tick(sc, (t, 0.0), f"{t:g}", size=14)
    for v in (0, 5, 10):
        sc.line((0.0, v * AY), (-0.05, v * AY), "EDGE", 1.3)
        sc.label((0.0, v * AY), str(v), "TEXT", "end", 14, italic=False, dx=-9, dy=5)
    sc.line((0.0, AY), (2.5, AY), "EDGE", 1.3, "7 5")
    sc.label((0.0, AY), "static, F" + S("", "1") + "/k", "TEXT", "end", 14, italic=False, dx=-24, dy=-8)
    sc.line((1.0, 0.0), (1.0, 11.0 * AY), "EDGE", 1.3, "7 5")
    mx = []
    zz = 0.0455
    while zz <= 0.7071:
        mx.append((math.sqrt(1 - 2 * zz * zz), AY / (2 * zz * math.sqrt(1 - zz * zz))))
        zz += 0.002
    sc.poly(mx, "HEAD", 1.8, "2 4")
    rows = (9.3, 7.4, 5.5, 3.9, 2.7)
    for (z, (col, op)), rowv in zip(zip(ZETAS, ZCOL), rows):
        pts = [(r, _amp(r, z) * AY) for r in rr]
        _pl(sc, pts, col, 2.6, None, op if op < 1 else None)
    for (z, (col, op)), rowv in zip(zip(ZETAS, ZCOL), rows):
        Q = 1 / (2 * z)
        rp = math.sqrt(1 - 2 * z * z) if z < 0.7071 else 1.0
        ap = _amp(rp, z)
        _pl(sc, [(rp, ap * AY), (1.42, rowv * AY)], col, 1.1, None, 0.75 if op == 1 else 0.6)
        sc.label((1.44, rowv * AY), G0 + "/" + W0 + " = " + f"{z:g}" + " (Q = " + f"{Q:g}" + ")", col if op == 1 else "BLUE", "start", 15,
                 italic=False, dy=5, weight="700" if False else "400")
    sc.note((0.92, 9.3 * AY), "High Q", "HEAD", "end", 16, dx=0, dy=0)
    sc.note((0.92, 7.4 * AY), "maxima", "HEAD", "end", 16, dx=0, dy=0)
    sc.note((2.45, 1.6 * AY), "Low Q", "HEAD", "end", 16, dx=0, dy=0)
    # ---- right graph
    sc.label((XR + 1.25, 2.62), "Phase lag", "HEAD", "middle", 19, italic=False)
    _axes(sc, XR - 0.05, XR + 2.62, -0.04, RY(0) + 0.3, "ω" + S("", "1") + "/" + W0, "φ" + S("", "1"), oy=0.0, ox=XR, offx=(40, 6), offy=(12, 4))
    sc.line((XR, RY(0)), (XR - 0.05, RY(0)), "EDGE", 1.3)
    sc.line((XR, RY(-math.pi / 2)), (XR - 0.05, RY(-math.pi / 2)), "EDGE", 1.3)
    sc.label((XR, RY(0)), "0", "TEXT", "end", 14, italic=False, dx=-9, dy=5)
    sc.label((XR, RY(-math.pi / 2)), MINUS + "π/2", "TEXT", "end", 14, italic=False, dx=-9, dy=5)
    sc.label((XR, 0.0), MINUS + "π", "TEXT", "end", 14, italic=False, dx=-9, dy=-4)
    for t in (0.5, 1.0, 1.5, 2.0, 2.5):
        _tick(sc, (XR + t, 0.0), f"{t:g}", size=14)
    sc.line((XR, RY(-math.pi / 2)), (XR + 2.5, RY(-math.pi / 2)), "EDGE", 1.3, "7 5")
    sc.line((XR + 1.0, 0.0), (XR + 1.0, RY(0)), "EDGE", 1.3, "7 5")
    for z, (col, op) in zip(ZETAS, ZCOL):
        _pl(sc, [(XR + r, RY(_lag(r, z))) for r in rr if r > 0 or True], col, 2.6, None, op if op < 1 else None)
    sc.dotp((XR + 1.0, RY(-math.pi / 2)), 4.5, "HEAD")
    sc.note((XR + 2.5, RY(-0.38 * math.pi)), "same curves as on the left", "TEXT", "end", 14)
    return sc


# --------------------------------------------------------------------------------------------------------------------
@_fig("t2-linearisation")
def linearisation():
    sc = Scene(960, 660, (330, 235), 78)
    YU = 1.1
    FL = -3.1
    FS = 1.2
    PI = math.pi
    xa, xb = -1.2 * PI, 2.2 * PI
    V = lambda x: 1 - math.cos(x)
    Fz = lambda x: -math.sin(x)
    yb = FL - 1.65                         # bottom axis
    sc.label((xa + 0.5, 2.75), "potential", "HEAD", "start", 19, italic=False, dx=8)
    sc.label((xa + 0.5, FL + 1.55), "force", "HEAD", "start", 19, italic=False, dx=8)
    # axes
    sc.vec((xa, 0.0), (xb + 0.2, 0.0), None, "EDGE", 1.4, head=8)
    sc.vec((xa, -0.35), (xa, 2.8), None, "EDGE", 1.4, head=8)
    sc.label((xa, 2.8), "V", "TEXT", "start", 17, weight="700", dx=10, dy=4)
    sc.vec((xa, FL - 1.6), (xa, FL + 1.55), None, "EDGE", 1.4, head=8)
    sc.label((xa, FL + 1.55), "F", "TEXT", "start", 17, weight="700", dx=10, dy=4)
    sc.vec((xa, FL), (xb + 0.2, FL), None, "EDGE", 1.4, head=8)
    sc.line((xa, yb), (xb + 0.2, yb), "EDGE", 1.4)
    sc.label((xb + 0.2, yb), "x", "TEXT", "middle", 17, weight="700", dx=12, dy=5)
    for x, nm in ((0.0, "0"), (PI, "πℓ"), (2 * PI, "2πℓ")):
        sc.line((x, yb), (x, yb + 0.1), "EDGE", 1.3)
        sc.label((x, yb), nm, "TEXT", "middle", 15, italic=False, dy=22)
    # curves
    sc.poly([(x, YU * V(x)) for x, _ in _fn(lambda t: 0, xa, xb, 500)], "HEAD", 2.8)
    sc.poly([(x, FL + FS * Fz(x)) for x, _ in _fn(lambda t: 0, xa, xb, 500)], "PINK", 2.8)
    xi = _fn(lambda t: 0, -1.6, 1.6, 100)
    sc.poly([(x, YU * 0.5 * x * x) for x, _ in xi], "BLUE", 2.2, "7 5")
    sc.poly([(PI + x, YU * (2 - 0.5 * x * x)) for x, _ in xi], ORANGE, 2.2, "7 5")
    sc.poly([(x, FL + FS * (-x)) for x in (-1.15, 1.15)], "BLUE", 2.0, "7 5")
    sc.poly([(PI + x, FL + FS * x) for x in (-1.15, 1.15)], ORANGE, 2.0, "7 5")
    # joining lines and equilibria
    for x in (0.0, PI):
        sc.line((x, YU * V(x)), (x, yb), "EDGE", 1.2, "2 4")
    sc.dotp((0.0, 0.0), 5.5, "GREEN")
    sc.dotp((PI, 2 * YU), 5.5, "GREEN")
    sc.dotp((0.0, FL), 4.5, "GREEN")
    sc.dotp((PI, FL), 4.5, "GREEN")
    sc.label((0.0, 0.0), "stable (minimum)", "GREEN", "end", 16, italic=False, dx=-12, dy=26)
    sc.label((PI, 2 * YU), "unstable (maximum)", "GREEN", "start", 16, italic=False, dx=44, dy=-2)
    sc.label((0.0, 1.9), "½" + _i("k") + _i("ξ") + "², " + _i("k") + " &gt; 0", "BLUE", "middle", 17, italic=False)
    sc.label((PI, 2 * YU), _i("k") + " &lt; 0", ORANGE, "middle", 17, italic=False, dy=-24)
    sc.vec((0.0, -0.3), (0.9, -0.3), None, "HEAD", 1.6, head=8)
    sc.vec((0.9, -0.3), (0.0, -0.3), None, "HEAD", 1.6, head=8)
    sc.label((0.45, -0.3), "ξ", "HEAD", "middle", 17, dy=22)
    sc.label((-1.15, FL + FS * 1.15), "slope −" + _i("k"), "BLUE", "end", 16, italic=False, dx=-8, dy=4)
    sc.label((PI + 1.15, FL + FS * 1.15), "slope −" + _i("k"), ORANGE, "start", 16, italic=False, dx=8, dy=4)
    return sc
