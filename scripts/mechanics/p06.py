"""P06: precessing orbit under an attractive inverse-cube perturbation (bank item P06).

Particle P (mass m) under F = -(m mu / r^2 + m eps / r^3) e_r about the fixed centre O; polar coordinates (r, theta)
in the orbital plane, h = r^2 theta_dot. Numerical case: mu = 4.0e14 m^3/s^2, perigee r_p = 8.0e6 m with the speed
v_p = 1.0e4 m/s perpendicular to OP, eps = 0.19 h^2.
"""
import math

import sympy as sp


def _rk4_orbit(mu, h, eps, rp, dt, t_end):
    """Integrate r'' = h^2/r^3 - mu/r^2 - eps/r^3, theta' = h/r^2 from the perigee; return the perigee passages (t, theta)."""
    def f(s):
        r, rd, th = s
        return (rd, h * h / r**3 - mu / r**2 - eps / r**3, h / r**2)

    s = (rp, 0.0, 0.0)
    t = 0.0
    out = []
    while t < t_end:
        k1 = f(s)
        k2 = f(tuple(a + dt / 2 * b for a, b in zip(s, k1)))
        k3 = f(tuple(a + dt / 2 * b for a, b in zip(s, k2)))
        k4 = f(tuple(a + dt * b for a, b in zip(s, k3)))
        n = tuple(a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4))
        if s[1] < 0 <= n[1]:                       # r_dot changes sign from - to +: a perigee
            w = -s[1] / (n[1] - s[1])              # linear interpolation inside the step
            out.append((t + w * dt, s[2] + w * (n[2] - s[2])))
        s, t = n, t + dt
    return out


def verify(chk):
    t = sp.symbols("t", real=True)
    m, mu, eps, h = sp.symbols("m mu epsilon h", positive=True)
    r = sp.Function("r")(t)
    th = sp.Function("theta")(t)
    rd, thd = r.diff(t), th.diff(t)

    # (a) torque about O of a central force is zero -> H_O constant
    er = sp.Matrix([sp.cos(th), sp.sin(th), 0])
    F = -(m * mu / r**2 + m * eps / r**3) * er
    tq0 = (r * er).cross(F)
    chk("torque r x F = 0 (central force)", tq0.dot(tq0))
    vel = (r * er).diff(t)
    Hz = m * (r * er).cross(vel)[2]
    chk("H_O . k = m r^2 theta_dot", Hz, m * r**2 * thd)
    # change of basis [e_r; e_theta; k] = R [i; j; k]
    qa = sp.symbols("qa", real=True)
    Rm = sp.Matrix([[sp.cos(qa), sp.sin(qa), 0], [-sp.sin(qa), sp.cos(qa), 0], [0, 0, 1]])
    eth_ = sp.Matrix([-sp.sin(th), sp.cos(th), 0])
    chk("R rows are e_r, e_theta, k", sum(xx**2 for xx in (Rm - sp.Matrix.hstack(er, eth_, sp.Matrix([0, 0, 1])).T.subs(th, qa))))
    chk("R R^T = I", sum(xx**2 for xx in (Rm * Rm.T - sp.eye(3))))
    chk("det R = +1", Rm.det(), 1)
    # (b) V(r) = -int_oo^r f(r') dr' with Barrow limits
    rp_ = sp.symbols("rp_", positive=True)
    Vint = sp.integrate(m * mu / rp_**2 + m * eps / rp_**3, (rp_, sp.oo, sp.Symbol("rr", positive=True)))
    chk("V(r) = int_oo^r (m mu/r'^2 + m eps/r'^3) dr' = -m mu/r - m eps/(2 r^2)", Vint,
        (-m * mu / rp_ - m * eps / (2 * rp_**2)).subs(rp_, sp.Symbol("rr", positive=True)))

    # (b) Lagrange equations (independent of the Newton projection of the note)
    V = -m * mu / r - m * eps / (2 * r**2)
    chk("-dV/dr = -(m mu/r^2 + m eps/r^3)", -V.diff(r), -(m * mu / r**2 + m * eps / r**3))
    L = m * (rd**2 + r**2 * thd**2) / 2 - V
    eq_r = sp.diff(L.diff(rd), t) - L.diff(r)
    eq_th = sp.diff(L.diff(thd), t) - L.diff(th)
    chk("radial EOM: r'' - r th'^2 = -mu/r^2 - eps/r^3", eq_r / m, r.diff(t, 2) - r * thd**2 + mu / r**2 + eps / r**3)
    chk("azimuthal EOM: d/dt(m r^2 th') = 0", eq_th, sp.diff(m * r**2 * thd, t))

    rs = sp.symbols("r", positive=True)
    Ueff = (h**2 - eps) / (2 * rs**2) - mu / rs
    chk("U_eff = h^2/(2r^2) - mu/r - eps/(2r^2)", Ueff, h**2 / (2 * rs**2) - mu / rs - eps / (2 * rs**2))
    # energy is constant: dE/dt with the radial EOM and h = r^2 th'
    E = rd**2 / 2 + (r**2 * thd**2) / 2 - mu / r - eps / (2 * r**2)
    rdd = r * thd**2 - mu / r**2 - eps / r**3
    thdd = -2 * rd * thd / r                           # from d/dt(r^2 th') = 0
    dE = E.diff(t).subs({r.diff(t, 2): rdd, th.diff(t, 2): thdd})
    chk("dE/dt = 0 on the motion", dE)

    # (c) circular orbit and its stability
    rc = (h**2 - eps) / mu
    chk("U_eff'(r_c) = 0 with r_c = (h^2 - eps)/mu", Ueff.diff(rs).subs(rs, rc))
    chk("U_eff''(r_c) = mu/r_c^3", Ueff.diff(rs, 2).subs(rs, rc), mu / rc**3)
    chk("circular speed: v^2 = h^2/r_c^2 = mu/r_c + eps/r_c^2", (h / rc)**2, mu / rc + eps / rc**2)
    chk("omega_r^2 / theta_dot_c^2 = 1 - eps/h^2", (mu / rc**3) / (h / rc**2)**2, 1 - eps / h**2)

    # (d) Binet: u = 1/r, r_dot = -h u', r'' = -h^2 u^2 u''
    tq = sp.symbols("theta", real=True)
    u = sp.Function("u")(tq)
    # r(t) = 1/u(theta(t)) with theta' = h u^2
    r_of = 1 / u
    rdot = sp.diff(r_of, tq) * h * u**2
    chk("r_dot = -h u'", rdot, -h * u.diff(tq))
    rddot = sp.diff(rdot, tq) * h * u**2
    chk("r'' = -h^2 u^2 u''", rddot, -h**2 * u**2 * u.diff(tq, 2))
    binet = rddot - r_of * (h * u**2)**2 + mu * u**2 + eps * u**3      # radial EOM with r = 1/u
    k2 = 1 - eps / h**2
    chk("Binet: u'' + (1 - eps/h^2) u = mu/h^2", sp.expand(-binet / (h**2 * u**2)),
        u.diff(tq, 2) + k2 * u - mu / h**2)
    e = sp.symbols("e", nonnegative=True)
    kk = sp.sqrt(k2)
    usol = mu / (h**2 * k2) * (1 + e * sp.cos(kk * tq))
    chk("u = mu/(h^2 k^2) (1 + e cos k theta) solves Binet", usol.diff(tq, 2) + k2 * usol - mu / h**2)
    chk("perigee r_p = (h^2 - eps)/(mu(1+e))", 1 / usol.subs(tq, 0), (h**2 - eps) / (mu * (1 + e)))
    chk("apogee r_a = (h^2 - eps)/(mu(1-e)) at k theta = pi", 1 / usol.subs(tq, sp.pi / kk), (h**2 - eps) / (mu * (1 - e)))

    # (e) apsidal angle and precession
    dphi = 2 * sp.pi * (1 / kk - 1)
    x = sp.symbols("x", positive=True)                  # x = eps/h^2
    ser = sp.series((2 * sp.pi * (1 / sp.sqrt(1 - x) - 1)), x, 0, 2).removeO()
    chk("small-eps limit: Delta phi = pi eps/h^2 + O(eps^2)", ser, sp.pi * x)
    # radial motion is a Kepler problem with h~^2 = h^2 - eps: radial period 2 pi sqrt(a^3/mu)
    E_rad = -mu / (2 * (( (h**2 - eps) / (mu * (1 + e)) + (h**2 - eps) / (mu * (1 - e))) / 2))
    Erp = Ueff.subs(rs, (h**2 - eps) / (mu * (1 + e)))
    chk("E/m = -mu/(2a) with 2a = r_p + r_a", Erp, E_rad)

    # (f) numerical case
    mun, rpn, vpn = sp.Integer(4) * 10**14, sp.Integer(8) * 10**6, sp.Integer(10)**4
    hn = rpn * vpn
    epsn = sp.Rational(19, 100) * hn**2
    chk.value("h = 8.0e10 m^2/s", hn, 8.0e10)
    chk.value("eps = 1.216e21 m^4/s^2", epsn, 1.216e21, tol=1e9)
    kn = sp.sqrt(1 - epsn / hn**2)
    chk("k = 0.9", kn, sp.Rational(9, 10))
    rcn = (hn**2 - epsn) / mun
    chk.value("r_c = 1.296e7 m", rcn, 1.296e7, tol=1e-3)
    en = rcn / rpn - 1
    chk("e = 0.62", en, sp.Rational(62, 100))
    ran = rcn / (1 - en)
    chk.value("r_a = 3.411e7 m", ran, 34105263.1578947, tol=1e-3)
    an = (rpn + ran) / 2
    chk.value("a = 2.105e7 m", an, 21052631.5789474, tol=1e-3)
    En = vpn**2 / 2 - mun / rpn - epsn / (2 * rpn**2)
    chk.value("E/m = -9.50e6 J/kg (from the perigee data)", En, -9.5e6, tol=1e-3)
    chk.value("E/m = -mu/(2a)", -mun / (2 * an), -9.5e6, tol=1e-3)
    chk("v_p^2/2 = mu/r_p (the unperturbed orbit would be parabolic)", vpn**2 / 2, mun / rpn)
    dph = 2 * sp.pi * (1 / kn - 1)
    chk.value("Delta phi = 2 pi / 9 = 40 deg", dph * 180 / sp.pi, 40)
    chk.value("apsidal angle (perigee to apogee) = pi/k = 200 deg", sp.pi / kn * 180 / sp.pi, 200)
    chk.value("small-eps estimate pi eps/h^2 = 34.2 deg", sp.pi * epsn / hn**2 * 180 / sp.pi, 34.2)
    Trn = 2 * sp.pi * sp.sqrt(an**3 / mun)
    chk.value("radial period T_r = 3.035e4 s", Trn, 30346.559, tol=1e-2)
    # independent route: numerical integration of the polar equations
    passes = _rk4_orbit(4e14, 8e10, 1.216e21, 8e6, 1.0, 2.2 * 30346.56)
    chk.true("numerical: first return to perigee after 30347 s (+-2 s)", len(passes) >= 2 and abs(passes[0][0] - 30346.56) < 2,
             f"{passes[:2]}")
    chk.true("numerical: perigee advanced by 400 deg (+-0.1 deg)", abs(math.degrees(passes[0][1]) - 400) < 0.1,
             f"{math.degrees(passes[0][1]):.4f}")
    chk.true("numerical: second perigee at 800 deg", abs(math.degrees(passes[1][1]) - 800) < 0.2)
    # circular orbit with the same h (part c, numbers)
    chk.value("circular speed with the same h: h/r_c = 6173 m/s", hn / rcn, 6172.8395, tol=1e-3)
    chk.value("T_r = 8.43 h", Trn / 3600, 8.4296, tol=1e-3)
    chk.value("pi eps/h^2 = 0.597 rad", sp.pi * epsn / hn**2, 0.5969, tol=1e-3)
    chk.true("first-order estimate low by about 15 %", abs((1 - sp.Rational(342, 400)) - 0.145) < 0.01)
    chk.value("2a = 4.211e7 m", 2 * an, 4.2105e7, tol=1e4)
    chk("h / h~ = 1/k", h / sp.sqrt(h**2 - eps), 1 / kk)
    chk.value("orbit closes after 9 perigees: 9 * 400 deg = 10 turns", 9 * 2 * sp.pi / kn / (2 * sp.pi), 10)
