"""P12: block on a turntable that spins up with constant angular acceleration (bank item P12).

Inertial frame S0 = {O; i, j, k}, k up along the axis. Turntable angle phi = beta t^2 / 2, Omega = beta t.
Block stuck at distance r0. Independent routes: direct differentiation of the Cartesian position, the balance of
inertia forces in the rotating frame, and the decomposition a_rel = a_abs - a_drag at the slip instant.
"""
import sympy as sp


def verify(chk):
    t = sp.symbols("t", positive=True)
    m, g, mu, mk, r0, beta = sp.symbols("m g mu mu_k r0 beta", positive=True)
    phi = beta * t**2 / 2
    Om = phi.diff(t)
    chk("Omega = beta t", Om, beta * t)
    er = sp.Matrix([sp.cos(phi), sp.sin(phi), 0])
    eth = sp.Matrix([-sp.sin(phi), sp.cos(phi), 0])
    kk = sp.Matrix([0, 0, 1])
    # change of basis [e_r; e_phi; k] = R [i; j; k]
    q = sp.symbols("q", real=True)
    R = sp.Matrix([[sp.cos(q), sp.sin(q), 0], [-sp.sin(q), sp.cos(q), 0], [0, 0, 1]])
    chk("R rows are e_r, e_phi, k", sum(x**2 for x in (R - sp.Matrix.hstack(er, eth, kk).T.subs(phi, q))))
    chk("R R^T = I", sum(x**2 for x in (R * R.T - sp.eye(3))))
    chk("det R = +1", R.det(), 1)
    r = r0 * er
    v = r.diff(t)
    a = v.diff(t)
    chk("v = r0 Omega e_phi", v.dot(eth), r0 * beta * t)
    chk("v has no radial component", v.dot(er), 0)
    chk("a_r = -r0 Omega^2", a.dot(er), -r0 * (beta * t)**2)
    chk("a_phi = r0 beta", a.dot(eth), r0 * beta)

    # forces: N = m g (vertical balance), friction F = m a (horizontal)
    Fr, Fth = sp.trigsimp(sp.expand(m * a.dot(er))), sp.trigsimp(sp.expand(m * a.dot(eth)))
    chk("F_r = -m r0 Omega^2", Fr, -m * r0 * Om**2)
    chk("F_phi = m r0 beta", Fth, m * r0 * beta)
    Fmag2 = sp.simplify(Fr**2 + Fth**2)
    chk("|F|^2 = m^2 r0^2 (Omega^4 + beta^2)", Fmag2, m**2 * r0**2 * (Om**4 + beta**2))

    # rotating frame: centrifugal + Euler + friction = 0 while stuck (Coriolis = 0)
    w = Om * kk
    wd = w.diff(t)
    F = Fr * er + Fth * eth
    Fcf = -m * w.cross(w.cross(r))
    Feu = -m * wd.cross(r)
    for i in range(3):
        chk(f"F + F_centrifugal + F_Euler = 0 (component {i})", (F + Fcf + Feu)[i], 0)
    chk("F_centrifugal = m r0 Omega^2 e_r", Fcf.dot(er), m * r0 * Om**2)
    chk("F_Euler = -m r0 beta e_phi", Feu.dot(eth), -m * r0 * beta)

    # slip condition: Omega*^4 = (mu g / r0)^2 - beta^2
    Ws = ((mu * g / r0)**2 - beta**2)**sp.Rational(1, 4)
    ts = Ws / beta
    chk("|F(t*)| = mu m g", sp.simplify(Fmag2.subs(t, ts) - (mu * m * g)**2), 0)
    n = {mu: sp.Rational(2, 5), r0: sp.Rational(1, 2), beta: sp.Rational(1, 5), g: sp.Rational(981, 100), mk: sp.Rational(3, 10), m: 1}
    chk.value("mu g / r0 = 7.848 s^-2", (mu * g / r0).subs(n), 7.848)
    chk.value("Omega*^4 = 61.55 s^-4", (Ws**4).subs(n), 61.551104, tol=1e-6)
    chk.value("Omega*^2 = 7.8454 s^-2", (Ws**2).subs(n), 7.84545, tol=1e-4)
    chk.value("Omega* = 2.801 rad/s", Ws.subs(n), 2.80097, tol=1e-4)
    chk.value("t* = 14.00 s", ts.subs(n), 14.0049, tol=1e-3)
    chk.value("angle turned before slip Omega*^2/(2 beta) = 19.61 rad", (Ws**2 / (2 * beta)).subs(n), 19.6136, tol=1e-3)
    chk.value("= 3.122 revolutions", (Ws**2 / (2 * beta) / (2 * sp.pi)).subs(n), 3.12160, tol=1e-4)
    chk.value("speed at slip r0 Omega* = 1.400 m/s", (r0 * Ws).subs(n), 1.40049, tol=1e-4)
    chk.value("centripetal part r0 Omega*^2 = 3.923 m/s^2", (r0 * Ws**2).subs(n), 3.92273, tol=1e-4)
    chk.value("tangential part r0 beta = 0.1 m/s^2", (r0 * beta).subs(n), sp.Rational(1, 10))

    # direction of friction at slip: angle psi from the inward radius towards +e_phi, tan psi = beta / Omega*^2
    psi = sp.atan(beta / Ws**2)
    chk("tan psi = F_phi / |F_r| at t*", (Fth / (-Fr)).subs(t, ts), beta / Ws**2)
    chk.value("psi = 1.460 deg", (psi * 180 / sp.pi).subs(n), 1.46026, tol=1e-4)
    chk("cos psi = Omega*^2 r0/(mu g)", sp.cos(psi), Ws**2 * r0 / (mu * g), numeric=n)

    # just after slip (kinetic coefficient mu_k): a_rel = a_abs - a_drag, Coriolis = 0 because v_rel = 0
    Fhat = (F / sp.sqrt(Fmag2)).subs(t, ts)
    a_abs = mk * g * Fhat                 # kinetic friction keeps the direction (opposes the incipient sliding)
    a_drag = a.subs(t, ts)                # acceleration of the table point under the block = mu g Fhat
    chk("a_drag at t* = mu g F_hat (r)", a_drag.dot(er.subs(t, ts)), (mu * g * Fhat).dot(er.subs(t, ts)), numeric=n)
    chk("a_drag at t* = mu g F_hat (phi)", a_drag.dot(eth.subs(t, ts)), (mu * g * Fhat).dot(eth.subs(t, ts)), numeric=n)
    a_rel = a_abs - a_drag
    a_rel_r = a_rel.dot(er.subs(t, ts))
    a_rel_t = a_rel.dot(eth.subs(t, ts))
    chk.value("|a_rel(t*+)| = (mu - mu_k) g = 0.981 m/s^2", sp.sqrt(a_rel_r**2 + a_rel_t**2).subs(n), 0.981, tol=1e-9)
    chk.value("a_rel radial (outward) = 0.9807 m/s^2", a_rel_r.subs(n), 0.980681, tol=1e-5)
    chk.value("a_rel tangential (backward) = -0.0250 m/s^2", a_rel_t.subs(n), -0.0249993, tol=1e-6)
    chk.true("relative motion starts outward and backward, at psi behind the outward radius",
             sp.N(a_rel_r.subs(n)) > 0 and sp.N(a_rel_t.subs(n)) < 0)
    chk.value("angle of a_rel behind the outward radius = psi", sp.atan(-a_rel_t / a_rel_r).subs(n), psi.subs(n), tol=1e-9)
    chk("with mu_k = mu the initial relative acceleration vanishes", a_rel_r.subs(mk, mu), 0, numeric=n)
    chk.value("absolute acceleration just after slip mu_k g = 2.943 m/s^2", sp.sqrt(a_abs.dot(a_abs)).subs(n), 2.943, tol=1e-9)
    chk.value("(mu g / r0)^2 = 61.59 s^-4", ((mu * g / r0)**2).subs(n), 61.591104, tol=1e-6)
    chk.value("mu g = 3.924 m/s^2 (friction limit per unit mass)", (mu * g).subs(n), 3.924)
    chk.value("beta^2 / (mu g / r0)^2 = 6.49e-4", (beta**2 / (mu * g / r0)**2).subs(n) * 1e4, 6.4944, tol=1e-3)
    # inertial frame: velocity at slip is purely tangential
    chk("v(t*) radial = 0 (no radial launch)", v.dot(er).subs(t, ts), 0)
    # beta >= mu g / r0: slips at t = 0, friction purely tangential
    chk.true("beta = mu g / r0 gives Omega* = 0 (slip at t = 0, friction tangential)", Ws.subs(beta, mu * g / r0) == 0)
