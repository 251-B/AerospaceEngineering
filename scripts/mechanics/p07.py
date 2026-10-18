"""P07: insertion orbit and circularisation impulse (bank item P07).

Probe at r0 from the planet centre O with speed v0 = sqrt(mu/r0) and flight-path angle gamma = 30 deg (outward).
Numbers: mu = 4.0e14 m^3/s^2, r0 = 1.0e7 m, planet radius R = 6.0e6 m.
"""
import sympy as sp


def verify(chk):
    mu, r0 = sp.symbols("mu r_0", positive=True)
    gam = sp.pi / 6
    v0 = sp.sqrt(mu / r0)
    vc = sp.sqrt(mu / r0)                     # reference speed

    # (a) conserved quantities
    h = r0 * v0 * sp.cos(gam)
    chk("h^2 = (3/4) mu r0", h**2, sp.Rational(3, 4) * mu * r0)
    E = v0**2 / 2 - mu / r0
    chk("E/m = -mu/(2 r0) < 0 (ellipse)", E, -mu / (2 * r0))
    a = -mu / (2 * E)
    chk("a = r0", a, r0)

    # (b) p, e, apsides
    p = h**2 / mu
    chk("p = 3 r0/4", p, sp.Rational(3, 4) * r0)
    e = sp.sqrt(1 + 2 * E * h**2 / mu**2)
    chk("e = sqrt(1 + 2 E h^2/mu^2) = 1/2", e, sp.Rational(1, 2))
    chk("p = a (1 - e^2)", p, a * (1 - e**2))
    rp, ra = p / (1 + e), p / (1 - e)
    chk("r_p = r0/2", rp, r0 / 2)
    chk("r_a = 3 r0/2", ra, 3 * r0 / 2)
    # independent: apsides are the roots of v_theta^2 + 0 radial speed in the energy equation
    rr = sp.symbols("r", positive=True)
    roots = sp.solve(sp.Eq(h**2 / (2 * rr**2) - mu / rr, E), rr)
    chk.true("energy equation with r_dot = 0 has roots r0/2 and 3r0/2",
             set(sp.simplify(x / r0) for x in roots) == {sp.Rational(1, 2), sp.Rational(3, 2)}, f"{roots}")

    # change of basis [e_r; e_theta; k] = R [i; j; k]
    qa = sp.symbols("qa", real=True)
    Rm = sp.Matrix([[sp.cos(qa), sp.sin(qa), 0], [-sp.sin(qa), sp.cos(qa), 0], [0, 0, 1]])
    chk("R R^T = I", sum(xx**2 for xx in (Rm * Rm.T - sp.eye(3))))
    chk("det R = +1", Rm.det(), 1)
    chk("e_r x e_theta = k (rows of R)", sum(xx**2 for xx in (Rm[0, :].cross(Rm[1, :]) - Rm[2, :])))
    # (e) r_dot = a e sin(E) E_dot with E_dot = n/(1 - e cos E) satisfies the energy equation with the right sign
    #     on both branches (outbound sin E > 0, inbound sin E < 0)
    EE = sp.symbols("EE", real=True)
    nn = sp.sqrt(mu / a**3)
    rE = a * (1 - e * sp.cos(EE))
    rdotE = a * e * sp.sin(EE) * nn / (1 - e * sp.cos(EE))
    chk("r_dot^2 + h^2/r^2 - 2 mu/r = 2E/m for every E", rdotE**2 + h**2 / rE**2 - 2 * mu / rE, 2 * E)
    chk("r_dot = sqrt(mu/a) a e sin E / r for every E", rdotE, sp.sqrt(mu / a) * a * e * sp.sin(EE) / rE)
    chk.true("inbound branch E = 3 pi/2: r_dot < 0", sp.N(rdotE.subs(EE, 3 * sp.pi / 2).subs(mu, 1).subs(r0, 1)) < 0)
    chk.true("outbound branch E = pi/2: r_dot > 0", sp.N(rdotE.subs(EE, sp.pi / 2).subs(mu, 1).subs(r0, 1)) > 0)

    # (c) true anomaly at r0, apsidal speeds, period
    th = sp.symbols("theta", real=True)
    costh0 = sp.solve(sp.Eq(p / (1 + e * sp.cos(th)), r0), sp.cos(th))
    chk.true("cos theta0 = -1/2", costh0 == [sp.Rational(-1, 2)] or sp.Rational(-1, 2) in costh0, f"{costh0}")
    th0 = 2 * sp.pi / 3
    rdot0 = mu / h * e * sp.sin(th0)
    chk("r_dot(theta0 = 120 deg) = v0 sin gamma > 0 (outbound)", rdot0, v0 * sp.sin(gam))
    chk("r theta_dot at r0 = v0 cos gamma", h / r0, v0 * sp.cos(gam))
    vp, va = h / rp, h / ra
    chk("v_p = sqrt3 sqrt(mu/r0)", vp, sp.sqrt(3) * vc)
    chk("v_a = sqrt(mu/r0)/sqrt3", va, vc / sp.sqrt(3))
    chk("vis-viva at the apogee", va**2, mu * (2 / ra - 1 / a))
    chk("vis-viva at the perigee", vp**2, mu * (2 / rp - 1 / a))
    T = 2 * sp.pi * sp.sqrt(a**3 / mu)
    chk("T = 2 pi sqrt(r0^3/mu)", T, 2 * sp.pi * sp.sqrt(r0**3 / mu))

    # (d) circularisation at the apogee
    vcirc = sp.sqrt(mu / ra)
    chk("v_circ(r_a) = sqrt(2/3) sqrt(mu/r0)", vcirc, sp.sqrt(sp.Rational(2, 3)) * vc)
    dv = vcirc - va
    chk("Delta v = (sqrt2 - 1)/sqrt3 sqrt(mu/r0)", dv, (sp.sqrt(2) - 1) / sp.sqrt(3) * vc)
    chk.true("Delta v > 0 (prograde)", sp.N(dv.subs({mu: 1, r0: 1})) > 0)
    dE = (vcirc**2 - va**2) / 2
    chk("Delta E/m = mu/(6 r0)", dE, mu / (6 * r0))
    chk("Delta E/m = -mu/(2 r_a) + mu/(2a)", dE, -mu / (2 * ra) + mu / (2 * a))
    T2 = 2 * sp.pi * sp.sqrt(ra**3 / mu)
    chk("T_circ / T = (3/2)^(3/2)", T2 / T, sp.Rational(3, 2)**sp.Rational(3, 2))

    # (e) time of flight r0 -> apogee with the eccentric anomaly (extension)
    Ean = sp.symbols("E", real=True)
    # r = a(1 - e cos E) and r = p/(1 + e cos th) -> cos E = (e + cos th)/(1 + e cos th)
    chk("r(E) = r(theta) with cos E = (e+cos th)/(1+e cos th)",
        a * (1 - e * (e + sp.cos(th)) / (1 + e * sp.cos(th))), p / (1 + e * sp.cos(th)))
    cosE0 = (e + sp.cos(th0)) / (1 + e * sp.cos(th0))
    chk("cos E0 = 0 -> E0 = pi/2", cosE0, 0)
    # Kepler's equation: radial energy with r = a(1 - e cos E) gives (1 - e cos E) dE = n dt
    c = sp.symbols("c")
    lhs = 2 * a * (a * (1 - e * c)) - (a * (1 - e * c))**2 - a**2 * (1 - e**2)
    chk("2ar - r^2 - a^2(1-e^2) = a^2 e^2 (1 - cos^2 E)", lhs, a**2 * e**2 * (1 - c**2))
    n = sp.sqrt(mu / a**3)
    tof = ((sp.pi - e * sp.sin(sp.pi)) - (sp.pi / 2 - e * sp.sin(sp.pi / 2))) / n
    chk("t(r0 -> apogee) = (pi/2 + 1/2) sqrt(r0^3/mu)", tof, (sp.pi / 2 + sp.Rational(1, 2)) * sp.sqrt(r0**3 / mu))
    # independent route: t = int r^2/h dtheta from 120 to 180 deg (numerical quadrature, mu = r0 = 1)
    integrand = (p / (1 + e * sp.cos(th)))**2 / h
    tnum = sp.Integral(integrand.subs({mu: 1, r0: 1}), (th, th0, sp.pi)).evalf(20)
    chk.value("quadrature of r^2/h dtheta = pi/2 + 1/2", tnum, sp.pi / 2 + sp.Rational(1, 2), tol=1e-10)
    chk.value("fraction of the period = (pi/2 + 1/2)/(2 pi) = 0.3296", (sp.pi / 2 + sp.Rational(1, 2)) / (2 * sp.pi), 0.32958, tol=1e-4)

    # (f) numbers
    sub = {mu: sp.Integer(4) * 10**14, r0: sp.Integer(10)**7}
    chk.value("v0 = 6325 m/s", v0.subs(sub), 6324.555, tol=1e-2)
    chk.value("h = 5.477e10 m^2/s", h.subs(sub), 5.4772e10, tol=1e7)
    chk.value("E/m = -2.0e7 J/kg", E.subs(sub), -2.0e7)
    chk.value("v_p = 1.095e4 m/s", vp.subs(sub), 10954.45, tol=1e-1)
    chk.value("v_a = 3651 m/s", va.subs(sub), 3651.48, tol=1e-1)
    chk.value("T = 9935 s", T.subs(sub), 9934.59, tol=1e-1)
    chk.value("v_circ(r_a) = 5164 m/s", vcirc.subs(sub), 5163.98, tol=1e-1)
    chk.value("Delta v = 1512 m/s", dv.subs(sub), 1512.50, tol=1e-1)
    chk.value("Delta E/m = 6.67e6 J/kg", dE.subs(sub), 6.6667e6, tol=1e2)
    chk.value("T_circ = 1.825e4 s", T2.subs(sub), 18251.0, tol=2)
    chk.value("t(r0 -> apogee) = 3274 s", tof.subs(sub), 3274.24, tol=1e-1)
    chk.value("naive 60/360 of T = 1656 s", (T / 6).subs(sub), 1655.77, tol=1e-1)
    chk.value("sqrt(r0^3/mu) = 1581 s", sp.sqrt(r0**3 / mu).subs(sub), 1581.14, tol=1e-2)
    # failed burn: impact with R = 6.0e6 m at cos theta = 0.5 (theta = 300 deg)
    R = sp.Integer(6) * 10**6
    cth = sp.solve(sp.Eq((p / (1 + e * sp.cos(th))).subs(sub), R), sp.cos(th))
    chk.true("impact at cos theta = 1/2", sp.Rational(1, 2) in cth, f"{cth}")
    cosEi = (e + sp.Rational(1, 2)) / (1 + e * sp.Rational(1, 2))
    chk("cos E_i = 4/5", cosEi, sp.Rational(4, 5))
    Ei = 2 * sp.pi - sp.acos(sp.Rational(4, 5))           # theta = 300 deg is on the inbound branch
    ti = ((Ei - e * sp.sin(Ei)) - sp.pi) / n
    chk.value("time apogee -> impact = 4424 s", ti.subs(sub), 4424.1, tol=1)
    chk.value("E_i = 5.640 rad", Ei, 5.6397, tol=1e-3)
    chk.value("n t = E_i - e sin E_i - pi = 2.798", Ei - e * sp.sin(Ei) - sp.pi, 2.7981, tol=1e-3)
    chk("sin E_i = -3/5", sp.sin(Ei), sp.Rational(-3, 5))
    chk.value("Delta v / sqrt(mu/r0) = 0.239", (sp.sqrt(2) - 1) / sp.sqrt(3), 0.23915, tol=1e-4)
    chk.value("(3/2)^(3/2) = 1.837", sp.Rational(3, 2)**sp.Rational(3, 2), 1.8371, tol=1e-4)
    chk.value("pi/2 + 1/2 = 2.071", sp.pi / 2 + sp.Rational(1, 2), 2.0708, tol=1e-4)
    chk.value("h at r_p check: v_p r_p = h", (vp * rp).subs(sub), h.subs(sub), tol=1)
    tnum2 =sp.Integral(integrand.subs(sub), (th, sp.pi, 5 * sp.pi / 3)).evalf(15)
    chk.value("quadrature apogee -> impact agrees", tnum2, ti.subs(sub), tol=1e-3)
