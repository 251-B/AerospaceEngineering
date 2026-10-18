"""P16: particle on a smooth wedge that is free to slide on a smooth table (bank item P16).

Geometry: the incline descends towards -x; s is measured along the incline, downwards, u = (-cos a, -sin a) is the
down-slope unit vector, nu = (-sin a, cos a) the outward normal. X is the abscissa of the wedge (positive towards +x).
Independent route: Lagrange equations in (X, s) for the accelerations; Newton's equations of the note for N; the first
integrals checked by differentiation along the motion.
"""
import sympy as sp


def verify(chk):
    t = sp.symbols("t", real=True)
    m, M, g, L = sp.symbols("m M g L", positive=True)
    a = sp.symbols("alpha", positive=True)
    X = sp.Function("X")(t)
    s = sp.Function("s")(t)
    Xd, sd, Xdd, sdd = X.diff(t), s.diff(t), X.diff(t, 2), s.diff(t, 2)
    u = sp.Matrix([-sp.cos(a), -sp.sin(a)])
    nu = sp.Matrix([sp.sin(a) * -1, sp.cos(a)])
    i = sp.Matrix([1, 0])
    j = sp.Matrix([0, 1])
    chk("u . nu = 0", u.dot(nu))
    chk("i . u = -cos a", i.dot(u), -sp.cos(a))
    chk("i . nu = -sin a", i.dot(nu), -sp.sin(a))
    chk("-j . u = sin a", -j.dot(u), sp.sin(a))
    chk("-j . nu = -cos a", -j.dot(nu), -sp.cos(a))
    # right-handed working basis {n, u}: n x u = +k; [i; j] = R [n; u]
    chk("n x u = +k (right-handed {n, u})", nu[0] * u[1] - nu[1] * u[0], 1)
    R = sp.Matrix([[-sp.sin(a), -sp.cos(a)], [sp.cos(a), -sp.sin(a)]])
    e1 = R[0, 0] * nu + R[0, 1] * u - i
    e2 = R[1, 0] * nu + R[1, 1] * u - j
    chk("i = R row 1 . (n, u)", e1.dot(e1))
    chk("j = R row 2 . (n, u)", e2.dot(e2))
    RRT = R * R.T - sp.eye(2)
    chk("R R^T = I", sum(x**2 for x in RRT))
    chk("det R = +1", R.det(), 1)

    # ---- Lagrange (independent of the Newton derivation)
    rP = X * i + s * u
    vP = rP.diff(t)
    Tk = M * Xd**2 / 2 + m * vP.dot(vP) / 2
    V = m * g * rP[1]
    Lg = Tk - V
    eX = sp.diff(Lg.diff(Xd), t) - Lg.diff(X)
    es = sp.diff(Lg.diff(sd), t) - Lg.diff(s)
    sol = sp.solve([eX, es], [Xdd, sdd], dict=True)[0]
    D = M + m * sp.sin(a)**2
    Xdd_n = m * g * sp.sin(a) * sp.cos(a) / D
    sdd_n = (M + m) * g * sp.sin(a) / D
    chk("X'' = m g sin a cos a / (M + m sin^2 a)", sol[Xdd], Xdd_n)
    chk("s'' = (M+m) g sin a / (M + m sin^2 a)", sol[sdd], sdd_n)

    # ---- Newton in S1 (note): along u, along nu, wedge horizontal
    N = sp.symbols("N")
    eq_u = sp.Eq(m * (Xdd * i.dot(u) + sdd), m * g * sp.sin(a))
    eq_nu = sp.Eq(m * Xdd * i.dot(nu), -m * g * sp.cos(a) + N)
    eq_w = sp.Eq(M * Xdd, N * sp.sin(a))
    nsol = sp.solve([eq_u, eq_nu, eq_w], [Xdd, sdd, N], dict=True)[0]
    chk("Newton gives the same X''", nsol[Xdd], Xdd_n)
    chk("Newton gives the same s''", nsol[sdd], sdd_n)
    N_n = M * m * g * sp.cos(a) / D
    chk("N = M m g cos a / (M + m sin^2 a)", nsol[N], N_n)
    chk("s'' = g sin a + X'' cos a", sdd_n, g * sp.sin(a) + Xdd_n * sp.cos(a))
    chk("N = m (g cos a - X'' sin a)", N_n, m * (g * sp.cos(a) - Xdd_n * sp.sin(a)))
    # inertia-force form: m a_rel = W + N nu - m X'' i, projected on u and nu
    a_rel = sdd * u
    res = m * a_rel - (-m * g * j + N * nu - m * Xdd * i)
    chk("S1 balance along u", res.dot(u).subs({Xdd: Xdd_n, sdd: sdd_n, N: N_n}))
    chk("S1 balance along nu", res.dot(nu).subs({Xdd: Xdd_n, sdd: sdd_n, N: N_n}))
    # table reaction on the wedge
    Rt = M * g + N_n * sp.cos(a)
    chk("table reaction R = M g + N cos a", Rt, M * g + N_n * sp.cos(a))
    aP = Xdd_n * i + sdd_n * u
    chk("system vertical balance: R - (M+m) g = m a_Py", Rt - (M + m) * g, m * aP[1])
    chk.true("R > M g > 0 for 0 < a < pi/2 ((R - M g) / cos^2 a is positive)", sp.simplify((Rt - M * g) / sp.cos(a)**2).is_positive)

    # ---- limits
    Ms = sp.symbols("Ms", positive=True)
    chk("M -> oo: s'' -> g sin a", sp.limit(sdd_n.subs(M, Ms), Ms, sp.oo), g * sp.sin(a))
    chk("M -> oo: X'' -> 0", sp.limit(Xdd_n.subs(M, Ms), Ms, sp.oo), 0)
    chk("M -> oo: N -> m g cos a", sp.limit(N_n.subs(M, Ms), Ms, sp.oo), m * g * sp.cos(a))
    chk("M -> 0: N -> 0", sp.limit(N_n.subs(M, Ms), Ms, 0), 0)
    chk("M -> 0: X'' -> g cot a", sp.limit(Xdd_n.subs(M, Ms), Ms, 0), g * sp.cos(a) / sp.sin(a))
    chk("M -> 0: s'' -> g / sin a", sp.limit(sdd_n.subs(M, Ms), Ms, 0), g / sp.sin(a))
    aP0x = sp.limit(aP[0].subs(M, Ms), Ms, 0)
    aP0y = sp.limit(aP[1].subs(M, Ms), Ms, 0)
    chk("M -> 0: a_P = -g j (free fall), x", aP0x, 0)
    chk("M -> 0: a_P = -g j (free fall), y", aP0y, -g)
    chk.true("N > 0 for M > 0, 0 < a < pi/2 (N / cos a is positive)", sp.simplify(N_n / sp.cos(a)).is_positive)
    fac = sdd_n / (g * sp.sin(a))
    chk("factor s''/(g sin a) - 1 = m cos^2 a / (M + m sin^2 a) >= 0", fac - 1, m * sp.cos(a)**2 / D)
    chk("M -> 0: factor -> 1/sin^2 a", sp.limit(fac.subs(M, Ms), Ms, 0), 1 / sp.sin(a)**2)

    chk("alpha -> 0: N -> m g", N_n.subs(a, 0), m * g)
    chk("alpha -> 0: X'' and s'' -> 0", Xdd_n.subs(a, 0) + sdd_n.subs(a, 0), 0)
    chk("alpha -> pi/2: N -> 0, X'' -> 0", N_n.subs(a, sp.pi / 2) + Xdd_n.subs(a, sp.pi / 2), 0)
    chk("alpha -> pi/2: s'' -> g", sdd_n.subs(a, sp.pi / 2), g)

    # ---- first integrals
    Px = sp.diff(Tk, Xd)
    chk("P_x = M X' + m (X' - s' cos a)", Px, M * Xd + m * (Xd - sd * sp.cos(a)))
    chk("dP_x/dt = 0 on the motion", sp.diff(Px, t).subs({Xdd: Xdd_n, sdd: sdd_n}))
    E = Tk + V
    chk("dE/dt = 0 on the motion", sp.expand(sp.diff(E, t).subs({Xdd: Xdd_n, sdd: sdd_n})))
    chk("from rest: X' = m cos a s' / (M + m)", sp.solve(sp.Eq(Px, 0), Xd)[0], m * sp.cos(a) * sd / (M + m))
    # power of N on P plus power of -N on the wedge
    vW = Xd * i
    chk("net power of the contact force: N nu . v_P - N nu . v_W = N nu . v_rel = 0",
        (N * nu).dot(vP) - (N * nu).dot(vW))
    # speeds after sliding L from rest, alpha = 30 deg, M = 2 m
    sv = sp.symbols("sdot", positive=True)
    Xv = m * sp.cos(a) * sv / (M + m)
    KE = (M * Xv**2 / 2 + m * ((Xv - sv * sp.cos(a))**2 + (sv * sp.sin(a))**2) / 2)
    num = {a: sp.pi / 6, M: 2 * m}
    chk("alpha = 30 deg, M = 2m: KE = (3/8) m s'^2", KE.subs(num), sp.Rational(3, 8) * m * sv**2)
    sdot_L = sp.sqrt(sp.solve(sp.Eq(KE.subs(num), m * g * L / 2), sv)[0]**2)
    chk("s'^2 = 4 g L / 3", sdot_L**2, 4 * g * L / 3)
    chk("consistent with s'^2 = 2 s'' L", sdot_L**2, 2 * sdd_n.subs(num) * L)
    chk("s'' = 2 g / 3", sdd_n.subs(num), 2 * g / 3)
    chk("X'' = sqrt3 g / 9", Xdd_n.subs(num), sp.sqrt(3) * g / 9)
    chk.value("X''/g = 0.1925", (Xdd_n.subs(num) / g), 0.19245, tol=1e-5)
    chk("N = sqrt3 m g / 2.25 = 4 sqrt3 m g / 9", N_n.subs(num), 4 * sp.sqrt(3) * m * g / 9)
    chk.value("N/(m g) = 0.7698", N_n.subs(num) / (m * g), 0.76980, tol=1e-5)
    Xdot_L = Xv.subs(num).subs(sv, sdot_L)
    chk("X' = sqrt(g L)/3", Xdot_L, sp.sqrt(g * L) / 3)
    chk.value("s'/sqrt(gL) = 1.1547", sdot_L / sp.sqrt(g * L), 1.154700, tol=1e-6)
    vPx = (Xv - sv * sp.cos(a)).subs(num).subs(sv, sdot_L)
    vPy = (-sv * sp.sin(a)).subs(num).subs(sv, sdot_L)
    chk("v_Px = -(2/3) sqrt(g L)", vPx, -2 * sp.sqrt(g * L) / 3)
    chk("v_Py = -sqrt(g L / 3)", vPy, -sp.sqrt(g * L / 3))
    chk("|v_P|^2 = 7 g L / 9", vPx**2 + vPy**2, 7 * g * L / 9)
    chk.value("|v_P|/sqrt(gL) = 0.8819", sp.sqrt(sp.Rational(7, 9)), 0.881917, tol=1e-6)
    chk("energy check: m|v_P|^2/2 + M X'^2/2 = m g L sin 30", m * (vPx**2 + vPy**2) / 2 + 2 * m * Xdot_L**2 / 2,
        m * g * L / 2)
    chk("work of N on P = E_kin,P - m g L sin a = -m g L / 9", m * (vPx**2 + vPy**2) / 2 - m * g * L / 2, -m * g * L / 9)
    chk("work of -N on the wedge = M X'^2/2 = +m g L / 9", 2 * m * Xdot_L**2 / 2, m * g * L / 9)
    chk("E_kin of P = 7 m g L / 18", m * (vPx**2 + vPy**2) / 2, 7 * m * g * L / 18)
    chk("Delta X = (m cos a/(M+m)) L = sqrt3 L / 6", (m * sp.cos(a) / (M + m)).subs(num) * L, sp.sqrt(3) * L / 6)
    chk("time to slide L: t_L = sqrt(2 L / s'') = sqrt(3 L / g)", sp.sqrt(2 * L / sdd_n.subs(num)), sp.sqrt(3 * L / g))

    # ---- absolute direction of P
    tanb = (-aP[1]) / (-aP[0])
    chk("tan(beta) = (1 + m/M) tan a", tanb, (1 + m / M) * sp.tan(a))
    chk("tan(beta) at 30 deg, M = 2m = sqrt3/2", tanb.subs(num), sp.sqrt(3) / 2)
    chk.value("beta = 40.89 deg", sp.atan(sp.sqrt(3) / 2) * 180 / sp.pi, 40.8934, tol=1e-3)
    # straight line: the velocity ratio equals the acceleration ratio (both start from rest, constant accelerations)
    chk("v_P direction = a_P direction (from rest, constant a_P)", vPy / vPx, aP[1].subs(num) / aP[0].subs(num))
    chk.true("beta > alpha (steeper than the incline)", sp.N(sp.atan(sp.sqrt(3) / 2)) > sp.N(sp.pi / 6))
    # centre of mass moves vertically only
    xG = (M * X + m * rP[0]) / (M + m)
    chk("x_G'' = 0", sp.diff(xG, t, 2).subs({Xdd: Xdd_n, sdd: sdd_n}))
