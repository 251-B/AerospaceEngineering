"""P09: bead on a vertical hoop held by a spring, equilibria and a pitchfork bifurcation (bank item P09).

Hoop of radius a, centre C, vertical plane; A on the vertical through C at height d = 2a above C; spring k with natural
length l0 = d - a = a from A to the bead P. theta measured from the top of the hoop. kappa = k a / (m g).
"""
import sympy as sp


def verify(chk):
    t = sp.symbols("t", real=True)
    m, g, a, k = sp.symbols("m g a k", positive=True)
    d = 2 * a
    l0 = d - a
    th = sp.Function("theta")(t)
    thd = th.diff(t)

    # position of P with respect to C (x horizontal, y up), A = (0, d)
    rP = sp.Matrix([a * sp.sin(th), a * sp.cos(th)])
    AP = rP - sp.Matrix([0, d])
    l = sp.sqrt(AP.dot(AP))
    q = sp.symbols("q", real=True)
    lq = sp.sqrt(a**2 + d**2 - 2 * a * d * sp.cos(q))
    chk("l^2 = a^2 + d^2 - 2 a d cos(theta)", (AP.dot(AP)).subs(th, q), lq**2)
    chk("l(0) = l0 (spring unstretched at the top)", lq.subs(q, 0), l0)
    chk("l(pi) = 3a", lq.subs(q, sp.pi), 3 * a)

    V = m * g * a * sp.cos(q) + k / 2 * (lq - l0)**2
    # Lagrange equation (independent of the Newton projection of the note)
    T = m * rP.diff(t).dot(rP.diff(t)) / 2
    L = T - V.subs(q, th)
    eq = sp.diff(L.diff(thd), t) - L.diff(th)
    thdd = sp.solve(sp.Eq(eq, 0), th.diff(t, 2))[0]
    Vp = sp.diff(V, q)
    chk("EOM: m a^2 theta'' = -V'(theta)", m * a**2 * thdd, -Vp.subs(q, th))
    G = -m * g * a + k * a * d * (1 - l0 / lq)
    chk("V'(theta) = sin(theta) [ -m g a + k a d (1 - l0/l) ]", Vp, sp.sin(q) * G)
    # tangential Newton form: m a theta'' = sin(theta) [ m g - k d (1 - l0/l) ]
    chk("m a theta'' = sin th [m g - k d (1 - l0/l)]", (m * a * thdd), (sp.sin(q) * (m * g - k * d * (1 - l0 / lq))).subs(q, th))

    # Newton with the reaction: N along e_r (outward), e_r = (sin, cos), e_th = (cos, -sin)
    er = sp.Matrix([sp.sin(th), sp.cos(th)])
    eth = sp.Matrix([sp.cos(th), -sp.sin(th)])
    # change of basis [e_theta; e_r] = R [i; j] (right-handed order: e_theta x e_r = +k)
    qa = sp.symbols("qa", real=True)
    Rm = sp.Matrix([[sp.cos(qa), -sp.sin(qa)], [sp.sin(qa), sp.cos(qa)]])
    chk("R rows are e_theta, e_r", sum(xx**2 for xx in (Rm - sp.Matrix.hstack(eth, er).T.subs(th, qa))))
    chk("R R^T = I", sum(xx**2 for xx in (Rm * Rm.T - sp.eye(2))))
    chk("det R = +1", Rm.det(), 1)
    chk("e_theta x e_r = +k", eth[0] * er[1] - eth[1] * er[0], 1)
    chk("order {e_r, e_theta} would give det -1", er[0] * eth[1] - er[1] * eth[0], -1)
    acc = rP.diff(t, 2)
    chk("a_P . e_r = -a theta'^2", acc.dot(er), -a * thd**2)
    chk("a_P . e_th = a theta''", acc.dot(eth), a * th.diff(t, 2))
    lt = lq.subs(q, th)
    Fs = -k * (lt - l0) / lt * AP
    W = sp.Matrix([0, -m * g])
    chk("F_s . e_r = -k (1 - l0/l)(a - d cos th)", Fs.dot(er), -k * (1 - l0 / lt) * (a - d * sp.cos(th)))
    chk("F_s . e_th = -k (1 - l0/l) d sin th", Fs.dot(eth), -k * (1 - l0 / lt) * d * sp.sin(th))
    N = sp.symbols("N")
    Nsol = sp.solve(sp.Eq(m * acc.dot(er), W.dot(er) + Fs.dot(er) + N), N)[0]
    chk("N = m g cos th + k (1 - l0/l)(a - d cos th) - m a th'^2", Nsol,
        m * g * sp.cos(th) + k * (1 - l0 / lt) * (a - d * sp.cos(th)) - m * a * thd**2)
    chk("tangential Newton = Lagrange", (W.dot(eth) + Fs.dot(eth)) / (m * a), thdd)

    # equilibria in terms of kappa = k a/(m g)
    kap = sp.symbols("kappa", positive=True)
    Vk = (V / (m * g * a)).subs(k, kap * m * g / a)
    Vkp = sp.simplify(sp.diff(Vk, q))
    chk("V'/(m g a) = sin th [ -1 + 2 kappa (1 - 1/sqrt(5 - 4 cos th)) ]", Vkp,
        sp.sin(q) * (-1 + 2 * kap * (1 - 1 / sp.sqrt(5 - 4 * sp.cos(q)))))
    cstar = (5 - 4 * kap**2 / (2 * kap - 1)**2) / 4
    lstar = 2 * kap * a / (2 * kap - 1)
    chk("l* = 2 kappa a/(2 kappa - 1) solves 1 - l0/l = 1/(2 kappa)", 1 - l0 / lstar, 1 / (2 * kap))
    chk("cos th* = (5 - (l*/a)^2)/4", cstar, (5 - (lstar / a)**2) / 4)
    chk("cos th* = -1 at kappa = 3/4 (pair born at the bottom)", cstar.subs(kap, sp.Rational(3, 4)), -1)
    chk.value("cos th* -> 1 as kappa -> infinity", sp.limit(cstar, kap, sp.oo), 1)
    chk.true("cos th* in (-1, 1) for kappa = 1 and 5; outside for kappa = 0.7",
             -1 < cstar.subs(kap, 1) < 1 and -1 < cstar.subs(kap, 5) < 1 and cstar.subs(kap, sp.Rational(7, 10)) < -1)
    # stability
    Vkpp = sp.diff(Vk, q, 2)
    chk("V''(0)/(m g a) = -1 (top always unstable)", Vkpp.subs(q, 0), -1)
    chk("V''(pi)/(m g a) = 1 - 4 kappa/3", Vkpp.subs(q, sp.pi), 1 - 4 * kap / 3)
    # at the bifurcation, V''(pi) = 0 and the 4th derivative decides
    V4 = sp.diff(Vk, q, 4).subs({q: sp.pi, kap: sp.Rational(3, 4)})
    chk.true("kappa = 3/4: V''''(pi) > 0 (bottom still stable, supercritical pitchfork)", sp.N(V4) > 0, f"{sp.nsimplify(V4)}")
    chk.value("kappa = 3/4: V'''(pi) = 0", sp.diff(Vk, q, 3).subs({q: sp.pi, kap: sp.Rational(3, 4)}), 0)
    # V''(theta*) = sin^2 th* k a^2 d^2 l0 / l*^3 (dimensional)
    Vpp = sp.diff(V, q, 2)
    for kv in (1, 2, sp.Rational(9, 10)):
        ks = kv * m * g / a
        thstar = sp.acos(cstar.subs(kap, kv))
        lhs = Vpp.subs({q: thstar, k: ks})
        rhs = (sp.sin(thstar)**2 * ks * a**2 * d**2 * l0 / lstar.subs(kap, kv)**3)
        chk(f"V''(theta*) = sin^2 k a^2 d^2 l0 / l^3 > 0 (kappa = {kv})", lhs, rhs)
        chk(f"V'(theta*) = 0 (kappa = {kv})", Vp.subs({q: thstar, k: ks}))
    # kappa = 1: theta* and the frequency
    chk("kappa = 1: l* = 2a", lstar.subs(kap, 1), 2 * a)
    chk("kappa = 1: cos th* = 1/4", cstar.subs(kap, 1), sp.Rational(1, 4))
    chk.value("kappa = 1: th* = 75.52 deg", sp.acos(sp.Rational(1, 4)) * 180 / sp.pi, 75.5225, tol=1e-3)
    w2 = (Vpp.subs({q: sp.acos(sp.Rational(1, 4)), k: m * g / a})) / (m * a**2)
    chk("kappa = 1: omega^2 = (15/32) g/a", w2, sp.Rational(15, 32) * g / a)
    # kappa = 1/2: frequency about the bottom
    w2b = (Vpp.subs({q: sp.pi, k: m * g / (2 * a)})) / (m * a**2)
    chk("kappa = 1/2: omega^2 = g/(3a) about the bottom", w2b, g / (3 * a))
    # energy: released from the top with a vanishing push, kappa = 1/2
    chk("V(pi) - V(0) = 2 m g a (kappa - 1)", (V.subs(q, sp.pi) - V.subs(q, 0)).subs(k, kap * m * g / a), 2 * m * g * a * (kap - 1))
    v2 = 2 * (V.subs(q, 0) - V.subs(q, sp.pi)) / m
    chk("kappa = 1/2: v_bottom^2 = 2 g a", v2.subs(k, m * g / (2 * a)), 2 * g * a)
    chk("kappa = 0: v_bottom^2 = 4 g a (no spring)", v2.subs(k, 0), 4 * g * a)
    Nb = (m * g * sp.cos(q) + k * (1 - l0 / lq) * (a - d * sp.cos(q))).subs({q: sp.pi, k: m * g / (2 * a)}) - m * v2.subs(k, m * g / (2 * a)) / a
    chk("kappa = 1/2: N(bottom) = -2 m g (hoop pushes the bead up)", Nb, -2 * m * g)
    chk.true("kappa = 1/2: V decreasing on (0, pi) (no intermediate turning point)",
             all(sp.N(Vkp.subs({kap: sp.Rational(1, 2), q: sp.pi * j / 20})) < 0 for j in range(1, 20)))
    # kappa = 1 released from the top: V(pi) = V(0), the bottom is reached only asymptotically
    chk("kappa = 1: V(pi) = V(0)", (V.subs(q, sp.pi) - V.subs(q, 0)).subs(k, m * g / a), 0)
    # numbers: a = 0.40 m, g = 9.81
    num = {a: sp.Rational(2, 5), g: sp.Rational(981, 100)}
    chk.value("v_bottom = 2.801 m/s (kappa = 1/2, a = 0.40 m)", sp.sqrt((2 * g * a).subs(num)), 2.80143, tol=1e-4)
    chk.value("omega = 3.391 rad/s (kappa = 1)", sp.sqrt((sp.Rational(15, 32) * g / a).subs(num)), 3.39054, tol=1e-4)
    chk.value("omega = 2.859 rad/s (kappa = 1/2, bottom)", sp.sqrt((g / (3 * a)).subs(num)), 2.85920, tol=1e-4)
    chk.value("omega^2 = g/(3a) = 8.175 s^-2", (g / (3 * a)).subs(num), 8.175, tol=1e-3)
    chk.value("omega^2 = (15/32) g/a = 11.50 s^-2", (sp.Rational(15, 32) * g / a).subs(num), 11.496, tol=1e-3)
    chk("sin^2 theta* = 15/16 (kappa = 1)", 1 - cstar.subs(kap, 1)**2, sp.Rational(15, 16))
    chk("kappa = 1/2: V''(pi) = m g a / 3", Vpp.subs({q: sp.pi, k: m * g / (2 * a)}), m * g * a / 3)
    chk("G(pi) = -m g a + (4/3) k a^2", G.subs(q, sp.pi), -m * g * a + sp.Rational(4, 3) * k * a**2)
