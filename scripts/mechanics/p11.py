"""P11: pendulum whose string is hauled through a fixed smooth ring (bank item P11).

Ring O at the origin, x horizontal, y up; e_r = (sin th, -cos th) points from O to the bob, e_th = (cos th, sin th).
Length l(t) = l0 - u t (u > 0 constant). Independent routes: Lagrange equation with a rheonomic constraint,
direct vector differentiation, an exact Bessel solution of the linearised equation and an RK4 integration.
"""
import numpy as np
import sympy as sp


def verify(chk):
    t = sp.symbols("t", real=True)
    m, g, u, l0 = sp.symbols("m g u l0", positive=True)
    th = sp.Function("theta")(t)
    thd, thdd = th.diff(t), th.diff(t, 2)
    l = l0 - u * t
    ld, ldd = l.diff(t), l.diff(t, 2)
    chk("l' = -u", ld, -u)
    chk("l'' = 0", ldd, 0)

    er = sp.Matrix([sp.sin(th), -sp.cos(th)])
    eth = sp.Matrix([sp.cos(th), sp.sin(th)])
    # change of basis [e_r; e_th; k] = R [i; j; k]
    q = sp.symbols("q", real=True)
    R = sp.Matrix([[sp.sin(q), -sp.cos(q), 0], [sp.cos(q), sp.sin(q), 0], [0, 0, 1]])
    chk("R rows 1-2 are e_r, e_th", sum(x**2 for x in (R[:2, :2] - sp.Matrix.hstack(er, eth).T.subs(th, q))))
    chk("R R^T = I", sum(x**2 for x in (R * R.T - sp.eye(3))))
    chk("det R = +1", R.det(), 1)
    # (e) antiderivative used for the work of the hauler: F(l) = -m h^2 / (2 l^2), F' = m h^2 / l^3
    hh, lv = sp.symbols("h_ell lv", positive=True)
    Fant = -m * hh**2 / (2 * lv**2)
    chk("F'(l) = m h^2 / l^3", Fant.diff(lv), m * hh**2 / lv**3)
    chk("F(l0) - F(l) = (m h^2/2)(1/l^2 - 1/l0^2)", Fant.subs(lv, l0) - Fant, m * hh**2 / 2 * (1 / lv**2 - 1 / l0**2))
    r = l * er
    v = r.diff(t)
    a = v.diff(t)
    # (b) polar components with variable length (general L(t) first, then l = l0 - u t)
    L = sp.Function("L")(t)
    rL = L * er
    vL, aL = rL.diff(t), rL.diff(t, 2)
    chk("v = L' e_r + L th' e_th (r)", vL.dot(er), L.diff(t))
    chk("v = L' e_r + L th' e_th (th)", vL.dot(eth), L * thd)
    chk("a_r = L'' - L th'^2", aL.dot(er), L.diff(t, 2) - L * thd**2)
    chk("a_th = L th'' + 2 L' th'", aL.dot(eth), L * thdd + 2 * L.diff(t) * thd)
    chk("with l = l0 - u t: a_th = l th'' - 2 u th'", a.dot(eth), l * thdd - 2 * u * thd)
    chk("with l = l0 - u t: a_r = -l th'^2", a.dot(er), -l * thd**2)

    # (c) Lagrange with the rheonomic constraint (independent of Newton)
    Lag = m * v.dot(v) / 2 - m * g * r[1]
    eq = sp.diff(Lag.diff(thd), t) - Lag.diff(th)
    sol = sp.solve(sp.Eq(eq, 0), thdd)[0]
    chk("EOM: l th'' + 2 l' th' + g sin th = 0", l * sol + 2 * ld * thd + g * sp.sin(th), 0)
    T = sp.symbols("T")
    W = sp.Matrix([0, -m * g])
    Tsol = sp.solve(sp.Eq(m * a.dot(er), W.dot(er) - T), T)[0]
    chk("T = m (g cos th + l th'^2 - l'')", Tsol, m * (g * sp.cos(th) + l * thd**2 - ldd))
    chk("W = m g (cos th e_r - sin th e_th): radial", W.dot(er), m * g * sp.cos(th))
    chk("W = m g (cos th e_r - sin th e_th): transverse", W.dot(eth), -m * g * sp.sin(th))

    # (d) angular momentum about O (z component) and its rate
    Hz = m * (r[0] * v[1] - r[1] * v[0])
    chk("H_O = m l^2 th' k", Hz, m * l**2 * thd)
    Mz = r[0] * W[1] - r[1] * W[0]
    chk("dH_O/dt = M_O(weight) = -m g l sin th (on the motion)", Hz.diff(t).subs(thdd, sol), Mz)
    chk("M_O(weight) = -m g l sin th", Mz, -m * g * l * sp.sin(th))
    # gravity-free case: l^2 th' = h, T = m l th'^2 = m h^2 / l^3
    hh, ll = sp.symbols("h ell", positive=True)
    sol0 = sol.subs(g, 0)
    chk("g = 0: d(l^2 th')/dt = 0", (l**2 * thd).diff(t).subs(thdd, sol0), 0)
    chk("g = 0: T = m h^2 / l^3", (Tsol.subs(g, 0)).subs(thd, hh / l**2), m * hh**2 / l**3)
    # numbers: m = 0.5 kg, l0 = 2 m, u = 0.5 m/s, initial transverse speed 1 m/s -> h = 2 m^2/s
    n = {m: sp.Rational(1, 2), l0: 2, u: sp.Rational(1, 2)}
    hn = 2 * 1
    chk.value("time to reach l = 0.5 m: 3 s", ((n[l0] - sp.Rational(1, 2)) / n[u]), 3)
    chk.value("th' at l = 0.5 m: 8 rad/s", hn / sp.Rational(1, 2)**2, 8)
    chk.value("transverse speed at 0.5 m: 4 m/s", hn / sp.Rational(1, 2), 4)
    chk.value("speed at 0.5 m: sqrt(16.25) = 4.031 m/s", sp.sqrt(sp.Rational(1, 4) + 16), 4.0311, tol=1e-4)
    chk.value("T(2 m) = 0.25 N", (m * hh**2 / ll**3).subs({m: n[m], hh: hn, ll: 2}), sp.Rational(1, 4))
    chk.value("T(0.5 m) = 16 N", (m * hh**2 / ll**3).subs({m: n[m], hh: hn, ll: sp.Rational(1, 2)}), 16)

    # (e) energy: work of the hauling force = kinetic energy gain (g = 0) and power balance (g != 0)
    Ekin = m * v.dot(v) / 2
    V = m * g * r[1]
    P_haul = Tsol * u                     # force T on the free end, which moves with speed u
    chk("d(Ekin + V)/dt = T u on the motion", (Ekin + V).diff(t).subs(thdd, sol), P_haul)
    chk("power of the tension on the bob = -T l' = T u", (-Tsol * er).dot(v), P_haul)
    l1, l2 = sp.symbols("l1 l2", positive=True)
    Wh = sp.integrate(m * hh**2 / ll**3, (ll, l2, l1))   # dt = -dl/u, T u dt = -T dl
    chk("W_haul = (m h^2 / 2)(1/l2^2 - 1/l1^2)", Wh, m * hh**2 / 2 * (1 / l2**2 - 1 / l1**2))
    dE = m / 2 * (u**2 + hh**2 / l2**2) - m / 2 * (u**2 + hh**2 / l1**2)
    chk("Delta Ekin = W_haul (g = 0)", dE, Wh)
    chk.value("numbers: W_haul = 3.75 J", Wh.subs({m: n[m], hh: hn, l1: 2, l2: sp.Rational(1, 2)}), sp.Rational(15, 4))

    # (f) extension: linearised equation in the variable l, exact Bessel solution and the l^(-3/4) law
    s = sp.symbols("s", positive=True)          # s = l as the independent variable
    k = sp.symbols("k", positive=True)          # k = g / u^2
    Th = sp.Function("Th")(s)
    # chain rule d/dt = l' d/dl = -u d/dl: th' = -u Th', th'' = u^2 Th''
    lin_t = l * thdd + 2 * ld * thd + g * th
    lin_l = (s * u**2 * Th.diff(s, 2) + 2 * (-u) * (-u * Th.diff(s)) + g * Th)
    chk("linearised equation in l: l Th'' + 2 Th' + (g/u^2) Th = 0", sp.expand(lin_l / u**2),
        sp.expand(s * Th.diff(s, 2) + 2 * Th.diff(s) + g / u**2 * Th))
    chk("l Th'' + 2 Th' = (1/l) d/dl (l^2 Th')", (s**2 * Th.diff(s)).diff(s) / s, s * Th.diff(s, 2) + 2 * Th.diff(s))
    for name, B in (("J1", sp.besselj), ("Y1", sp.bessely)):
        y = s**sp.Rational(-1, 2) * B(1, 2 * sp.sqrt(k * s))
        res = s * y.diff(s, 2) + 2 * y.diff(s) + k * y
        vals = [abs(sp.N(res.subs({k: 9.81 / 0.01**2, s: sv}))) for sv in (0.3, 0.6, 1.0)]
        chk.true(f"l^(-1/2) {name}(2 sqrt(g l)/u) solves the linearised equation (numeric residual)",
                 max(vals) < 1e-6, f"max residual {max(vals):.2e}")
    # asymptotic amplitude: J1(z) ~ sqrt(2/(pi z)) cos(...), z = 2 sqrt(g l)/u ~ l^(1/2) -> amplitude ~ l^(-1/2) l^(-1/4)
    zz = 2 * sp.sqrt(k * s)
    amp = s**sp.Rational(-1, 2) * sp.sqrt(2 / (sp.pi * zz))
    chk.true("amplitude envelope ~ l^(-3/4)", not sp.simplify(amp / s**sp.Rational(-3, 4)).has(s))
    chk.value("adiabatic law: amplitude ratio from l = 1 m to 0.25 m = 4^(3/4) = 2.828", sp.Rational(1, 4)**sp.Rational(-3, 4), 2.8284, tol=1e-4)
    chk.value("adiabatic invariant J = E/omega ~ l^(3/2) A^2 constant -> A ~ l^(-3/4)",
              (sp.Rational(1, 4)**sp.Rational(3, 2) * (sp.Rational(1, 4)**sp.Rational(-3, 4))**2), 1)
    chk.value("slowness condition at l = 0.25 m: u / sqrt(g l) = 0.0064", 0.01 / sp.sqrt(9.81 * 0.25), 0.006386, tol=1e-5)

    chk.value("Bessel argument at l = 0.25 m: 2 sqrt(g l)/u = 313.2 >> 1", 2 * sp.sqrt(9.81 * 0.25) / 0.01, 313.21, tol=1e-2)
    chk.value("law at l = 0.25 m: 0.05 * 4^(3/4) = 0.1414 rad", 0.05 * sp.Rational(4)**sp.Rational(3, 4), 0.141421, tol=1e-6)
    chk.value("horizontal excursion l A ~ l^(1/4): ratio 0.25^(1/4) = 0.7071", sp.Rational(1, 4)**sp.Rational(1, 4), 0.707107, tol=1e-6)
    # RK4 of the full nonlinear equation, l0 = 1 m, u = 0.01 m/s, theta0 = 0.05 rad, until l = 0.25 m (t = 75 s)
    gg, uu, L0 = 9.81, 0.01, 1.0

    def f(tt, y):
        lt = L0 - uu * tt
        return np.array([y[1], (-gg * np.sin(y[0]) + 2 * uu * y[1]) / lt])

    dt, tt, y = 1e-3, 0.0, np.array([0.05, 0.0])
    peaks = []
    prev = y.copy()
    while tt < 75.0 - 1e-9:
        k1 = f(tt, y)
        k2 = f(tt + dt / 2, y + dt / 2 * k1)
        k3 = f(tt + dt / 2, y + dt / 2 * k2)
        k4 = f(tt + dt, y + dt * k3)
        ynew = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if prev[1] > 0 >= ynew[1] or (prev[1] < 0 <= ynew[1]):
            peaks.append((tt, abs(ynew[0])))
        prev, y, tt = ynew, ynew, tt + dt
    t_last, A_last = peaks[-1]
    pred = 0.05 * ((L0 - uu * t_last) / L0) ** (-0.75)
    chk.true("RK4: last amplitude matches 0.05 (l/l0)^(-3/4) within 0.2 %", abs(A_last / pred - 1) < 2e-3,
             f"RK4 {A_last:.5f} rad vs {pred:.5f} rad at l = {L0 - uu * t_last:.3f} m")
