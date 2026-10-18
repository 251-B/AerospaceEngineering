"""C07: damped and forced oscillator m = 2 kg, k = 50 N/m, c = 4 N s/m, F1 = 10 N (bank item C07).

(a) underdamped decay per period of the damped motion: amplitude and mechanical energy (exact, from the general solution).
(b) steady-state amplitude and phase versus the forcing frequency: phase at omega1 = omega0 and the true maximum.
"""
import sympy as sp


def verify(chk):
    t = sp.symbols("t", real=True)
    m, k, c, F1 = sp.Integer(2), sp.Integer(50), sp.Integer(4), sp.Integer(10)
    gam = c / (2 * m)
    w0 = sp.sqrt(k / m)
    chk("gamma = c/(2m) = 1 1/s", gam, 1)
    chk("omega0 = sqrt(k/m) = 5 1/s", w0, 5)
    chk.true("underdamped: gamma < omega0", gam < w0)
    wd = sp.sqrt(w0**2 - gam**2)
    chk("omega = sqrt(omega0^2 - gamma^2) = 2 sqrt6", wd, 2 * sp.sqrt(6))
    # characteristic roots of m p^2 + c p + k = 0
    p = sp.symbols("p")
    roots = sp.solve(m * p**2 + c * p + k, p)
    chk.true("roots p = -1 +- 2 sqrt6 i", set(roots) == {-1 + 2 * sp.sqrt(6) * sp.I, -1 - 2 * sp.sqrt(6) * sp.I})
    # general underdamped solution and exact decay over one damped period
    A, B = sp.symbols("A B", real=True)
    x = sp.exp(-gam * t) * (A * sp.cos(wd * t) + B * sp.sin(wd * t))
    chk("x solves m x'' + c x' + k x = 0", m * x.diff(t, 2) + c * x.diff(t) + k * x, 0)
    T = 2 * sp.pi / wd
    chk("x(t+T) = exp(-gamma T) x(t)", x.subs(t, t + T), sp.exp(-gam * T) * x)
    E = m * x.diff(t)**2 / 2 + k * x**2 / 2
    chk("E(t+T) = exp(-2 gamma T) E(t)", sp.simplify(E.subs(t, t + T) - sp.exp(-2 * gam * T) * E), 0)
    chk("gamma T = pi/sqrt6", gam * T, sp.pi / sp.sqrt(6))
    chk.value("amplitude factor exp(-pi/sqrt6) = 0.2773", sp.exp(-sp.pi / sp.sqrt(6)), 0.27731, tol=5e-5)
    chk.value("energy factor exp(-2pi/sqrt6) = 0.07691", sp.exp(-2 * sp.pi / sp.sqrt(6)), 0.076912, tol=5e-6)
    chk("dE/dt = -c x'^2 (power of the damper)", sp.simplify(E.diff(t) + c * x.diff(t)**2), 0)
    chk.value("T = 2 pi/omega = 1.283 s", T, 1.28255, tol=5e-5)

    # (b) steady state x = a1 cos(w1 t + alpha1)
    w1 = sp.symbols("omega1", positive=True)
    a1 = (F1 / m) / sp.sqrt((w0**2 - w1**2)**2 + 4 * gam**2 * w1**2)
    # independent route: complex amplitude from (-m w1^2 + i c w1 + k) A1 = F1
    A1 = F1 / (-m * w1**2 + sp.I * c * w1 + k)
    chk("|A1| = a1 (Notes Eq. 5.41)", sp.Abs(A1).subs(w1, sp.Rational(37, 10)), a1.subs(w1, sp.Rational(37, 10)))
    chk("a1(omega0) = F1/(2 m gamma omega0) = 0.5 m", a1.subs(w1, w0), sp.Rational(1, 2))
    chk("phase at omega1 = omega0: A1 = -i |A1| (lag of pi/2)", A1.subs(w1, w0), -sp.I * sp.Rational(1, 2))
    chk("arg A1 at resonance = -pi/2", sp.arg(A1.subs(w1, w0)), -sp.pi / 2)
    # maximum of a1 over omega1: minimise D = (w0^2 - w1^2)^2 + 4 gamma^2 w1^2 in s = w1^2
    s = sp.symbols("s", positive=True)
    D = (w0**2 - s)**2 + 4 * gam**2 * s
    s_star = sp.solve(sp.diff(D, s), s)[0]
    chk("dD/ds = 0 at omega1^2 = omega0^2 - 2 gamma^2 = 23", s_star, 23)
    chk("d2D/ds2 = 2 > 0", sp.diff(D, s, 2), 2)
    g_, W0 = sp.symbols("g_ W0", positive=True)
    Dg = (W0**2 - s)**2 + 4 * g_**2 * s
    chk("D(s*) = 4 gamma^2 (omega0^2 - gamma^2) (symbolic)", Dg.subs(s, W0**2 - 2 * g_**2), 4 * g_**2 * (W0**2 - g_**2))
    chk("static amplitude a1(0) = F1/k = 0.2 m", a1.subs(w1, 0), sp.Rational(1, 5))
    chk.value("omega = 2 sqrt6 = 4.899 1/s", wd, 4.89898, tol=5e-5)
    chk("a1_max = F1 / (2 m gamma sqrt(omega0^2 - gamma^2)) = 5/(2 sqrt24)", a1.subs(w1, sp.sqrt(s_star)), 5 / (2 * sp.sqrt(24)))
    chk.value("a1_max = 0.5103 m", 5 / (2 * sp.sqrt(24)), 0.51031, tol=5e-5)
    chk.value("omega1* = sqrt23 = 4.796 1/s", sp.sqrt(23), 4.79583, tol=5e-5)
    chk.true("a1_max > a1(omega0)", a1.subs(w1, sp.sqrt(23)) > a1.subs(w1, w0))
    # phase at the amplitude maximum
    al = sp.arg(A1.subs(w1, sp.sqrt(23)))
    chk("tan(alpha1) at omega1^2 = 23: -2 gamma w1/(w0^2 - w1^2) = -sqrt23", sp.tan(al), -sp.sqrt(23))
    chk.value("alpha1 at the amplitude maximum = -78.2 deg", al * 180 / sp.pi, -78.22, tol=5e-3)
