"""P13: capsule descent with quadratic drag and two parachute stages (bank item P13).

y is measured downward from the release point, v = dy/dt >= 0. m v' = m g - c v^2.
Stage 1 (drogue): released from rest, v_t1 = 50 m/s. Stage 2 (main): opens at v1 = 40 m/s, v_t2 = 8 m/s.
Independent routes: substitution in the ODE, the position y(t) obtained by integrating v(t) (compared with v(y)),
the drag work integrated along the path (compared with the energy balance), and an RK4 integration.
"""
import numpy as np
import sympy as sp


def verify(chk):
    t, y = sp.symbols("t y", nonnegative=True)
    m, g, c, vt, v1, x = sp.symbols("m g c v_t v_1 x", positive=True)

    # terminal speed
    chk("v_t^2 = m g / c makes the right-hand side vanish", (m * g - c * vt**2).subs(c, m * g / vt**2), 0)
    # antiderivative used in the separation of variables (both branches)
    chk("d/dv [v_t artanh(v/v_t)] = 1/(1 - v^2/v_t^2)", sp.diff(vt * sp.atanh(x / vt), x), 1 / (1 - x**2 / vt**2))
    chk("d/dv [v_t arcoth(v/v_t)] = 1/(1 - v^2/v_t^2)", sp.diff(vt * sp.acoth(x / vt), x), 1 / (1 - x**2 / vt**2))
    chk("d/dv [-(v_t^2/2) ln(1 - v^2/v_t^2)] = v/(1 - v^2/v_t^2)", sp.diff(-vt**2 / 2 * sp.log(1 - x**2 / vt**2), x),
        x / (1 - x**2 / vt**2))

    # stage 1: v = v_t tanh(g t / v_t)
    cc = m * g / vt**2
    vs = vt * sp.tanh(g * t / vt)
    chk("v = v_t tanh(g t/v_t) solves m v' = m g - c v^2", m * vs.diff(t) - (m * g - cc * vs**2), 0)
    chk("v(0) = 0", vs.subs(t, 0), 0)
    ys = vt**2 / g * sp.log(sp.cosh(g * t / vt))
    chk("y(t) = (v_t^2/g) ln cosh(g t/v_t): dy/dt = v(t)", ys.diff(t), vs)
    chk("y(0) = 0", ys.subs(t, 0), 0)
    vy2 = vt**2 * (1 - sp.exp(-2 * g * y / vt**2))
    chk("v^2(y) = v_t^2 (1 - exp(-2 g y/v_t^2)) solves v dv/dy = g (1 - v^2/v_t^2)",
        vy2.diff(y) / 2, g * (1 - vy2 / vt**2))
    chk("v^2(y(t)) = v(t)^2", vy2.subs(y, vt**2 / g * sp.log(sp.cosh(g * t / vt))), vs**2)

    n = {m: 1000, g: sp.Rational(981, 100), vt: 50}
    chk.value("c1 = m g / v_t1^2 = 3.924 kg/m", cc.subs(n), 3.924)
    t95 = vt / g * sp.atanh(sp.Rational(19, 20))
    y95 = vt**2 / (2 * g) * sp.log(1 / (1 - sp.Rational(361, 400)))
    chk.value("artanh(0.95) = 1.8318", sp.atanh(sp.Rational(19, 20)), 1.83178, tol=1e-5)
    chk.value("ln(1/0.0975)/2 = 1.1640", sp.log(1 / (1 - sp.Rational(361, 400))) / 2, 1.16395, tol=1e-5)
    chk.value("t95 = 9.336 s", t95.subs(n), 9.3363, tol=1e-3)
    chk.value("y95 = 296.6 m", y95.subs(n), 296.62, tol=1e-2)
    chk.value("y(t95) from y(t) equals y95", (vt**2 / g * sp.log(sp.cosh(g * t95 / vt))).subs(n), y95.subs(n), tol=1e-9)
    # main chute opening during stage 1 at v1 = 40 m/s = 0.8 v_t1
    t1 = vt / g * sp.atanh(sp.Rational(4, 5))
    y1 = vt**2 / (2 * g) * sp.log(1 / (1 - sp.Rational(16, 25)))
    chk.value("time to 40 m/s: 5.600 s", t1.subs(n), 5.6000, tol=1e-3)
    chk.value("drop to 40 m/s: 130.2 m", y1.subs(n), 130.18, tol=1e-2)
    W1 = sp.Rational(1, 2) * m * 40**2 - m * g * y1
    chk.value("stage 1 drag work to 40 m/s = -477.1 kJ", (W1 / 1000).subs(n), -477.064, tol=1e-2)
    W1int = -sp.integrate((cc * vy2), (y, 0, y1))
    chk.value("stage 1 drag work by integration of -c v^2 dy", W1int.subs(n), W1.subs(n), tol=1e-6)

    # stage 2: v_t2 = 8 m/s, opening at v1 = 40 m/s > v_t2: v = v_t2 coth(g t/v_t2 + arcoth(v1/v_t2))
    vt2 = 8
    n2 = {m: 1000, g: sp.Rational(981, 100), vt: vt2, v1: 40}
    vc = vt * sp.coth(g * t / vt + sp.acoth(v1 / vt))
    chk("coth solution satisfies the ODE", m * vc.diff(t) - (m * g - cc * vc**2), 0)
    chk("coth solution starts at v1", vc.subs(t, 0), v1, numeric=n2)
    chk.true("tanh branch cannot start at v1 > v_t2 (artanh(5) is not real)", not sp.atanh(5).is_real)
    chk.value("c2 = 153.3 kg/m", cc.subs(n2), 153.28125, tol=1e-6)
    chk.value("c2/c1 = (v_t1/v_t2)^2 = 39.06", (cc.subs(n2) / cc.subs(n)), sp.Rational(625, 16))
    acc0 = (g * (1 - v1**2 / vt**2)).subs(n2)
    chk.value("deceleration at opening = -24 g = -235.4 m/s^2", acc0, -24 * 9.81)
    chk.value("drag at opening = c2 v1^2 = 245.25 kN", (cc * v1**2).subs(n2) / 1000, 245.25)
    tq = vt / g * (sp.acoth(sp.Rational(21, 20)) - sp.acoth(v1 / vt))
    chk.value("arcoth(1.05) = ln(41)/2 = 1.8568", sp.acoth(sp.Rational(21, 20)), sp.log(41) / 2)
    chk.value("arcoth(5) = ln(1.5)/2 = 0.2027", sp.acoth(5), sp.log(sp.Rational(3, 2)) / 2)
    chk.value("time from opening to 1.05 v_t2 = 1.349 s", tq.subs(n2), 1.34893, tol=1e-4)
    vy2b = vt**2 + (v1**2 - vt**2) * sp.exp(-2 * g * y / vt**2)
    chk("stage 2 v^2(y) solves v dv/dy = g(1 - v^2/v_t^2)", vy2b.diff(y) / 2, g * (1 - vy2b / vt**2))
    dyq = vt**2 / (2 * g) * sp.log((v1**2 - vt**2) / (sp.Rational(21, 20)**2 * vt**2 - vt**2))
    chk.value("distance from opening to 1.05 v_t2 = 17.80 m", dyq.subs(n2), 17.7967, tol=1e-3)
    # substitution w = 1 - v^2/v_t^2 (w < 0 in stage 2): g dy = -(v_t^2/2)(ln|w| - ln|w1|)
    vv = sp.symbols("vv", positive=True)
    w_of = 1 - vv**2 / vt**2
    chk.value("w1 = 1 - v1^2/v_t2^2 = -24", w_of.subs(vv, v1).subs(n2), -24)
    chk("d/dv[-(v_t^2/2) ln|w|] = v/(1 - v^2/v_t^2) for v > v_t", (-(vt**2) / 2 * sp.log(vv**2 / vt**2 - 1)).diff(vv),
        vv / w_of)
    gdy = -(vt**2) / 2 * (sp.log(-w_of.subs(vv, sp.Rational(21, 20) * vt)) - sp.log(-w_of.subs(vv, v1)))
    chk.value("Barrow with ln|w| gives the same Delta y", (gdy / g).subs(n2), dyq.subs(n2), tol=1e-9)
    ytq = (vt**2 / g * sp.log(sp.sinh(g * t / vt + sp.acoth(v1 / vt)) / sp.sinh(sp.acoth(v1 / vt))))
    chk("y(t) = (v_t^2/g) ln(sinh(g t/v_t + a)/sinh a) has derivative v(t)", ytq.diff(t), vc)
    chk.value("y(tq) from y(t) equals the distance from v(y)", ytq.subs(n2).subs(t, tq.subs(n2)), dyq.subs(n2), tol=1e-9)
    # energy balance in stage 2
    W2 = sp.Rational(1, 2) * m * ((sp.Rational(21, 20) * vt)**2 - v1**2) - m * g * dyq
    W2int = -sp.integrate(cc * vy2b, (y, 0, dyq))
    chk.value("stage 2 drag work = Delta Ekin - m g Delta y = -939.3 kJ", (W2 / 1000).subs(n2), -939.310, tol=1e-2)
    chk.value("stage 2 drag work by integration of -c v^2 dy", W2int.subs(n2), W2.subs(n2), tol=1e-6)
    chk.value("Delta Ekin stage 2 = -764.7 kJ", (sp.Rational(1, 2) * m * ((sp.Rational(21, 20) * vt)**2 - v1**2) / 1000).subs(n2), -764.72)
    chk.value("m g Delta y stage 2 = 174.6 kJ", (m * g * dyq / 1000).subs(n2), 174.590, tol=1e-2)

    chk.value("v_t1/g = 5.097 s", (vt / g).subs(n), 5.0968, tol=1e-4)
    chk.value("v_t1^2/(2g) = 127.4 m", (vt**2 / (2 * g)).subs(n), 127.42, tol=1e-2)
    chk.value("ln(1/0.36) = 1.0217", sp.log(1 / sp.Rational(9, 25)), 1.02165, tol=1e-5)
    chk.value("artanh(0.8) = 1.0986", sp.atanh(sp.Rational(4, 5)), 1.09861, tol=1e-5)
    chk.value("m g y1 = 1277.1 kJ", (m * g * y1 / 1000).subs(n), 1277.06, tol=1e-2)
    chk.value("v_t2/g = 0.8155 s", (vt / g).subs(n2), 0.81549, tol=1e-5)
    chk.value("v_t2^2/(2g) = 3.262 m", (vt**2 / (2 * g)).subs(n2), 3.2620, tol=1e-4)
    chk.value("ln(1536/6.56) = 5.456", sp.log(sp.Rational(1536 * 100, 656)), 5.4559, tol=1e-4)
    chk.value("drag power at opening c2 v1^3 = 9.81 MW", (cc * v1**3).subs(n2) / 10**6, 9.81)
    # analytic drag work: -c2 int v^2 dy = -(m g dy + m (v1^2 - v^2)/2)
    yy, vv = sp.symbols("Y V", positive=True)
    Wan = -sp.integrate((cc * (vt**2 + (v1**2 - vt**2) * sp.exp(-2 * g * y / vt**2))), (y, 0, yy))
    Wan = Wan.subs(yy, vt**2 / (2 * g) * sp.log((v1**2 - vt**2) / (vv**2 - vt**2)))
    chk("drag work along stage 2 = -(m g Dy + m (v1^2 - v^2)/2)", Wan,
        -(m * g * vt**2 / (2 * g) * sp.log((v1**2 - vt**2) / (vv**2 - vt**2)) + m * (v1**2 - vv**2) / 2),
        numeric={m: 1000, g: sp.Rational(981, 100), vt: 8, v1: 40, vv: sp.Rational(42, 5)})
    chk.value("ln(1/0.0975) = 2.3279", sp.log(1 / (1 - sp.Rational(361, 400))), 2.32790, tol=1e-5)
    chk.value("artanh(0.95) = ln(39)/2", sp.atanh(sp.Rational(19, 20)), sp.log(39) / 2)
    chk.value("c2 v1^2 / (m g) = 25", ((cc * v1**2) / (m * g)).subs(n2), 25)
    chk.value("W_drag2 / W_drag1 = 1.969 (almost twice)", W2.subs(n2) / W1.subs(n), 1.9689, tol=1e-3)
    chk("large-t asymptote: ln cosh x - (x - ln 2) -> 0", sp.limit(sp.log(sp.cosh(x)) - x + sp.log(2), x, sp.oo), 0)
    # RK4 of the two-stage descent (switch when v reaches 40 m/s)
    gg, M = 9.81, 1000.0
    c1n, c2n = M * gg / 50**2, M * gg / 8**2
    s = np.array([0.0, 0.0])
    tt, dt, c_now, t_open, y_open = 0.0, 1e-4, c1n, None, None
    while True:
        def f(z):
            return np.array([z[1], gg - c_now / M * z[1]**2])
        k1 = f(s); k2 = f(s + dt / 2 * k1); k3 = f(s + dt / 2 * k2); k4 = f(s + dt * k3)
        s_new = s + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if c_now == c1n and s_new[1] >= 40.0:
            fr = (40.0 - s[1]) / (s_new[1] - s[1])
            t_open, y_open = tt + fr * dt, s[0] + fr * (s_new[0] - s[0])
            s = np.array([y_open, 40.0]); tt = t_open; c_now = c2n
            continue
        if c_now == c2n and s_new[1] <= 8.4:
            fr = (s[1] - 8.4) / (s[1] - s_new[1])
            t_end, y_end = tt + fr * dt, s[0] + fr * (s_new[0] - s[0])
            break
        s, tt = s_new, tt + dt
    chk.true("RK4: opening at t = 5.600 s, y = 130.18 m", abs(t_open - 5.6000) < 1e-3 and abs(y_open - 130.18) < 1e-2,
             f"t = {t_open:.4f} s, y = {y_open:.3f} m")
    chk.true("RK4: 8.4 m/s reached 1.349 s and 17.80 m after opening",
             abs(t_end - t_open - 1.34893) < 1e-3 and abs(y_end - y_open - 17.7967) < 1e-2,
             f"dt = {t_end - t_open:.4f} s, dy = {y_end - y_open:.3f} m")
