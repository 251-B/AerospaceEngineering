"""P04: bead in a smooth radial tube on a turntable with angular rate Omega(t) = Omega0 + beta t (bank item P04).

The bead (mass m) is tied to the axis point O by a spring of zero natural length and stiffness k. S0 inertial,
S1 = {O; i1, j1, k} turns with the tube (i1 along the tube), theta = Omega0 t + beta t^2/2.
Independent routes: Newton in S0 with the absolute acceleration of x(t)(cos theta, sin theta, 0), the angular
momentum about the axis, and direct substitution of the closed-form solutions into the ODE.
"""
import sympy as sp


def _vec(chk):
    def vchk(name, left, right=None):
        left = sp.Matrix(left)
        right = sp.zeros(*left.shape) if right is None else sp.Matrix(right)
        d = (left - right).applyfunc(lambda e: sp.simplify(sp.trigsimp(e)))
        ok = all(e == 0 for e in d)
        return chk.true(name, ok, "" if ok else f"residual {list(d)}")
    return vchk


def verify(chk):
    vchk = _vec(chk)
    t = sp.symbols("t", real=True)
    m, k, g, Om0, IT = sp.symbols("m k g Omega0 I_T", positive=True)
    beta, x0, v0 = sp.symbols("beta x0 v0", real=True)
    x = sp.Function("x")(t)
    xd, xdd = x.diff(t), x.diff(t, 2)
    th = Om0 * t + beta * t**2 / 2
    Om = th.diff(t)
    chk("theta' = Omega0 + beta t", Om, Om0 + beta * t)

    R01 = sp.Matrix([[sp.cos(th), -sp.sin(th), 0], [sp.sin(th), sp.cos(th), 0], [0, 0, 1]])
    chk("det [0R1] = 1", R01.det(), 1)
    vchk("[0R1][0R1]^T = I", R01 * R01.T, sp.eye(3))
    i1, j1, kk = R01[:, 0], R01[:, 1], R01[:, 2]

    pos = x * i1
    a0 = pos.diff(t, 2)
    a1 = sp.simplify(R01.T * a0)
    vchk("absolute acceleration in B1: (x'' - Omega^2 x, 2 Omega x' + beta x, 0)", a1,
         sp.Matrix([xdd - Om**2 * x, 2 * Om * xd + beta * x, 0]))
    # Coriolis theorem term by term
    w = sp.Matrix([0, 0, Om])
    al = sp.Matrix([0, 0, beta])
    r1 = sp.Matrix([x, 0, 0])
    vr = sp.Matrix([xd, 0, 0])
    ar = sp.Matrix([xdd, 0, 0])
    vchk("a0 = a_rel + alpha x r + w x (w x r) + 2 w x v_rel", a1, ar + al.cross(r1) + w.cross(w.cross(r1)) + 2 * w.cross(vr))
    vchk("Euler force -m alpha x r = -m beta x j1", -m * al.cross(r1), sp.Matrix([0, -m * beta * x, 0]))
    vchk("centrifugal force = m Omega^2 x i1", -m * w.cross(w.cross(r1)), sp.Matrix([m * Om**2 * x, 0, 0]))
    vchk("Coriolis force = -2 m Omega x' j1", -2 * m * w.cross(vr), sp.Matrix([0, -2 * m * Om * xd, 0]))

    # Newton in S0, components in B1, unknowns x'', N_y, N_z
    Ny, Nz = sp.symbols("N_y N_z")
    F1 = sp.Matrix([-k * x, Ny, Nz - m * g])
    sol = sp.solve(list(m * a1 - F1), [xdd, Ny, Nz], dict=True)[0]
    chk("EOM: x'' + (k/m - Omega(t)^2) x = 0 (no beta)", sol[xdd], -(k / m - Om**2) * x)
    chk("N_y = m (beta x + 2 Omega x')", sol[Ny], m * (beta * x + 2 * Om * xd))
    chk("N_z = m g", sol[Nz], m * g)

    # angular momentum about the axis and the torque on the bead
    v0vec = pos.diff(t)
    Hz = sp.simplify(kk.dot(pos.cross(m * v0vec)))
    chk("H_z = m x^2 Omega", Hz, m * x**2 * Om)
    chk("dH_z/dt = x N_y (torque of the tube reaction)", sp.diff(Hz, t), x * sol[Ny])
    chk("torque of the spring and weight about the axis is zero", kk.dot(pos.cross(-k * pos + sp.Matrix([0, 0, -m * g]))))
    M = IT * beta + sp.diff(Hz, t)
    chk("motor torque M = I_T beta + m x (beta x + 2 Omega x')", M, IT * beta + m * x * (beta * x + 2 * Om * xd))

    # power balance in S0: d(T + V)/dt = power of the tube reaction = Omega x N_y
    E = m * v0vec.dot(v0vec) / 2 + k * x**2 / 2
    chk("d(T+V)/dt = Omega x N_y on the motion", sp.simplify(sp.diff(E, t).subs(xdd, sol[xdd])), Om * x * sol[Ny])
    chk("power of N_y j1 on the absolute velocity = Omega x N_y", (sol[Ny] * j1).dot(v0vec), Om * x * sol[Ny])
    chk("reaction does no work in S1 (N . v_rel = 0)", sp.Matrix([0, sol[Ny], sol[Nz]]).dot(vr))

    # beta = 0: the three regimes
    ts = sp.symbols("t", real=True)
    wn2 = k / m
    om = sp.sqrt(wn2 - Om0**2)
    lam = sp.sqrt(Om0**2 - wn2)
    for name, xs, cond in [
        ("Omega0^2 < k/m: x = x0 cos(w t) + (v0/w) sin(w t)", x0 * sp.cos(om * ts) + v0 / om * sp.sin(om * ts), None),
        ("Omega0^2 = k/m: x = x0 + v0 t", x0 + v0 * ts, {Om0: sp.sqrt(k / m)}),
        ("Omega0^2 > k/m: x = x0 cosh(l t) + (v0/l) sinh(l t)", x0 * sp.cosh(lam * ts) + v0 / lam * sp.sinh(lam * ts), None),
    ]:
        ode = xs.diff(ts, 2) + (wn2 - Om0**2) * xs
        if cond:
            ode = ode.subs(cond)
        vchk(name, sp.Matrix([ode, xs.subs(ts, 0) - x0, xs.diff(ts).subs(ts, 0) - v0]))
    xs3 = x0 * sp.exp(-lam * ts)
    chk("Omega0^2 > k/m with v0 = -lambda x0: x = x0 exp(-lambda t) (decays to O)",
        (x0 * sp.cosh(lam * ts) - lam * x0 / lam * sp.sinh(lam * ts)).rewrite(sp.exp), xs3)
    # Jacobi integral in S1 for beta = 0
    J = xd**2 / 2 + (wn2 - Om0**2) * x**2 / 2
    chk("Jacobi integral x'^2/2 + (k/m - Omega0^2) x^2/2 is constant for beta = 0",
        sp.diff(J, t).subs(xdd, sol[xdd].subs(beta, 0)))

    # numbers: m = 0.2 kg, k = 20 N/m, x0 = 0.1 m, v0 = 0
    num = {m: sp.Rational(1, 5), k: 20}
    chk.value("omega_n = sqrt(k/m) = 10 rad/s", sp.sqrt(wn2).subs(num), 10)
    chk.value("Omega0 = 6: w = 8 rad/s", om.subs(num).subs(Om0, 6), 8)
    chk.value("Omega0 = 6: period 2 pi/8 = 0.7854 s", (2 * sp.pi / om).subs(num).subs(Om0, 6), 0.785398, tol=1e-6)
    chk.value("Omega0 = 12.5: lambda = 7.5 1/s", lam.subs(num).subs(Om0, sp.Rational(25, 2)), 7.5)
    n3 = {**num, Om0: sp.Rational(25, 2), x0: sp.Rational(1, 10), v0: 0, beta: 0}
    Lt = sp.Rational(1, 2)
    t_end = sp.acosh(5) / sp.Rational(15, 2)
    chk("x(t_end) = 0.5 m with t_end = arccosh(5)/7.5", (x0 * sp.cosh(lam * t_end)).subs(n3), Lt)
    chk.value("t_end = 0.3057 s", t_end, 0.305657, tol=1e-6)
    chk.value("arccosh 5 = 2.2924", sp.acosh(5), 2.29243, tol=1e-5)
    chk("k = 0 limit: x = x0 cosh(Omega0 t) solves x'' = Omega0^2 x",
        (x0 * sp.cosh(Om0 * ts)).diff(ts, 2) - Om0**2 * x0 * sp.cosh(Om0 * ts))
    chk("table: I_T beta = M - x N_y", IT * beta, M - x * sol[Ny])
    xdot_end = (x0 * lam * sp.sinh(lam * t_end)).subs(n3)
    chk("x'(t_end) = 0.75 sqrt24 m/s", xdot_end, sp.Rational(3, 4) * sp.sqrt(24))
    chk.value("x'(t_end) = 3.674 m/s", xdot_end, 3.67423, tol=1e-5)
    chk("x'^2 at L from the Jacobi integral: lambda^2 (L^2 - x0^2)", xdot_end**2, (lam**2 * (Lt**2 - x0**2)).subs(n3))
    Ny_end = (2 * m * Om0 * xdot_end).subs(n3)
    chk.value("N_y(t_end) = 18.37 N", Ny_end, 18.3712, tol=1e-4)
    chk.value("torque on the bead x N_y = 9.186 N m", Lt * Ny_end, 9.18559, tol=1e-4)
    chk.value("motor power on the bead Omega x N_y = 114.8 W", sp.Rational(25, 2) * Lt * Ny_end, 114.820, tol=1e-3)
    chk.value("N_y/(m g) = 9.36 (about nine times the weight)", Ny_end / sp.Rational(1962, 1000), 9.3635, tol=1e-3)
    chk.value("N_z = m g = 1.962 N", (m * g).subs(num).subs(g, sp.Rational(981, 100)), 1.962)
    # energy delivered by the motor between x0 and L: Omega * Delta H = m Omega^2 (L^2 - x0^2)
    E_of = lambda X, XD: (m * (XD**2 + Om0**2 * X**2) / 2 + k * X**2 / 2).subs(n3)
    dE = E_of(Lt, xdot_end) - E_of(sp.Rational(1, 10), 0)
    chk("Delta(T + V) = 7.5 J", dE, sp.Rational(15, 2))
    chk("work of the motor = Omega Delta H_z = m Omega0^2 (L^2 - x0^2)", dE, (m * Om0**2 * (Lt**2 - x0**2)).subs(n3))
    chk.value("T at x0 = 0.15625 J", (m * Om0**2 * x0**2 / 2).subs(n3), 0.15625)
    chk.value("V at x0 = 0.1 J", (k * x0**2 / 2).subs(n3), 0.1)
    chk.value("T at L = 5.25625 J", (m * (xdot_end**2 + Om0**2 * Lt**2) / 2).subs(n3), 5.25625)
    chk.value("V at L = 2.5 J", (k * Lt**2 / 2).subs(n3), 2.5)
