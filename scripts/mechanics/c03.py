"""C03: slider A (mass M) on a smooth horizontal rail with a pendulum bob P (mass m) hanging from it (bank item C03).

(a) free slider: Lagrange equations (independent of the Newton/energy argument of the note), tension from Newton on A,
    power balance of each particle and of the system, energy transferred to A when the bob passes the vertical.
(b) slider driven by a motor, x_A = b sin(Omega t): relative energy is not a first integral.
"""
import sympy as sp


def verify(chk):
    t = sp.symbols("t", real=True)
    M, m, l, g, b, W, th0 = sp.symbols("M m l g b Omega theta0", positive=True)
    x = sp.Function("x")(t)
    th = sp.Function("theta")(t)
    xd, thd = x.diff(t), th.diff(t)
    xdd, thdd = x.diff(t, 2), th.diff(t, 2)

    er = sp.Matrix([sp.sin(th), -sp.cos(th)])
    eth = sp.Matrix([sp.cos(th), sp.sin(th)])
    rA = sp.Matrix([x, 0])
    rP = rA + l * er
    vP = rP.diff(t)
    chk("v_P = x' i + l th' e_th", (vP - (sp.Matrix([xd, 0]) + l * thd * eth)).norm()**2, 0)

    # (a) Lagrange equations of the free system
    Tk = M * xd**2 / 2 + m * vP.dot(vP) / 2
    Vp = m * g * rP[1]
    L = Tk - Vp
    eqs = [sp.diff(L.diff(q.diff(t)), t) - L.diff(q) for q in (x, th)]
    sol = sp.solve(eqs, [xdd, thdd], dict=True)[0]
    # tension from Newton on A (horizontal): M x'' = T sin(th)  (string pulls A towards P)
    T = sp.simplify(M * sol[xdd] / sp.sin(th))
    # Newton on P along e_r must give the same T:  m a_P . e_r = -T + m g (j . e_r)... with weight -m g j
    aP = vP.diff(t).subs(sol)
    T_from_P = sp.simplify(-m * aP.dot(er) + (-m * g) * sp.Matrix([0, 1]).dot(er))
    chk("tension: Newton on A and Newton on P agree", T - T_from_P, 0)
    # Newton on P along e_th has no T: m a_P . e_th = -m g sin(th)
    chk("Newton on P along e_th (no tension)", sp.simplify(m * aP.dot(eth) + m * g * sp.sin(th)), 0)

    E_P = m * vP.dot(vP) / 2 + m * g * rP[1]
    E_A = M * xd**2 / 2
    dEP = sp.simplify(E_P.diff(t).subs(sol))
    dEA = sp.simplify(E_A.diff(t).subs(sol))
    chk("dE_P/dt = power of tension on P = -T x' sin(th)", dEP, -T * xd * sp.sin(th))
    chk("dE_A/dt = +T x' sin(th)", dEA, T * xd * sp.sin(th))
    chk("d(E_A + E_P)/dt = 0", dEP + dEA, 0)
    chk("tension power on P = -T e_r . v_P = -T x' sin(th)", (-T * er).dot(vP), -T * xd * sp.sin(th))
    chk("power of the tension pair = T e_r.(v_A - v_P) = 0", (T * er).dot(sp.Matrix([xd, 0]) - vP), 0)

    # horizontal momentum is conserved: (M+m) x' + m l th' cos(th) = const
    px = sp.diff(L, xd)
    chk("p_x = (M+m) x' + m l th' cos th, dp_x/dt = 0", sp.simplify(px.diff(t).subs(sol)), 0)
    # released from rest at th0: values when the bob passes the vertical
    X, Y = sp.symbols("X Y", real=True)   # X = x'(th=0), Y = th'(th=0)
    s = sp.solve([(M + m) * X + m * l * Y,
                  M * X**2 / 2 + m * ((X + l * Y)**2) / 2 - m * g * l + m * g * l * sp.cos(th0)], [X, Y], dict=True)
    s = [r for r in s if sp.N(r[Y].subs({g: 1, l: 1, M: 1, m: 1, th0: 1})) > 0][0]
    chk("l th'^2 at the vertical = 2 g (1-cos th0)(M+m)/M", l * s[Y]**2, 2 * g * (1 - sp.cos(th0)) * (M + m) / M)
    chk("E_A at the vertical = m^2 g l (1-cos th0)/(M+m) (taken from P)", M * s[X]**2 / 2, m**2 * g * l * (1 - sp.cos(th0)) / (M + m))
    Yv = sp.symbols("Yv", real=True)
    Xv = -m * l * Yv / (M + m)
    chk("x' + l th' = M l th'/(M+m) at the vertical", Xv + l * Yv, M * l * Yv / (M + m))
    chk("kinetic terms add up to M m l^2 th'^2 / (2 (M+m))",
        M * Xv**2 / 2 + m * (Xv + l * Yv)**2 / 2, M * m * l**2 * Yv**2 / (2 * (M + m)))

    # (b) driven slider x_A = b sin(W t): equation of the bob and the relative energy
    xA = b * sp.sin(W * t)
    rP2 = sp.Matrix([xA, 0]) + l * er
    vP2 = rP2.diff(t)
    L2 = m * vP2.dot(vP2) / 2 - m * g * rP2[1]
    eq2 = sp.diff(L2.diff(thd), t) - L2.diff(th)
    thdd2 = sp.solve(eq2, thdd)[0]
    chk("driven: l th'' = -g sin th - x_A'' cos th", l * thdd2, -g * sp.sin(th) - xA.diff(t, 2) * sp.cos(th))
    v_rel = l * thd * eth
    chk("S1: tension does no work (-T e_r . v_rel = 0)", (-sp.Symbol("T") * er).dot(v_rel), 0)
    E_rel = m * l**2 * thd**2 / 2 - m * g * l * sp.cos(th)
    dErel = sp.simplify(E_rel.diff(t).subs(thdd, thdd2))
    chk("dE_rel/dt = -m x_A'' l th' cos th = m b W^2 l sin(Wt) th' cos th", dErel, m * b * W**2 * l * sp.sin(W * t) * thd * sp.cos(th))
    chk("dE_rel/dt = power of the inertia force -m x_A'' i on v_rel", dErel, (-m * xA.diff(t, 2) * sp.Matrix([1, 0])).dot(v_rel))
    chk.true("dE_rel/dt != 0 at th = 0, th' = 1/s, W t = pi/2 (counterexample)",
             sp.simplify(dErel.subs({thd: 1}).subs(th, 0).subs(t, sp.pi / (2 * W))) != 0)
    chk("counterexample value: dE_rel/dt = m b W^2 l th' at W t = pi/2, th = 0",
        dErel.subs(th, 0).subs(t, sp.pi / (2 * W)), m * b * W**2 * l * thd.subs(th, 0))
    Estar =E_rel + m * xA.diff(t, 2) * l * sp.sin(th)
    dEstar = sp.simplify(Estar.diff(t).subs(thdd, thdd2))
    chk("with the frozen inertia potential: dE*/dt = m x_A''' l sin th != 0", dEstar, m * xA.diff(t, 3) * l * sp.sin(th))
