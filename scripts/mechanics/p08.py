"""P08: seismic accelerometer on a vibrating base (bank item P08).

Case base moves vertically z(t) = Z cos(nu t) (up positive, inertial). Proof mass m on a spring k (natural length L0)
and a damper c, both between the case floor and the mass. xi = height of the mass above the case floor, x = xi - xi_e
(relative coordinate from the static equilibrium). Numbers: m = 0.050 kg, k = 500 N/m, c = 2.0 N s/m, Z = 2.0 mm,
nu = 50 rad/s, g = 9.81 m/s^2.
"""
import sympy as sp


def verify(chk):
    t = sp.symbols("t", real=True)
    m, k, c, g, Z, nu, L0 = sp.symbols("m k c g Z nu L_0", positive=True)
    xi = sp.Function("xi")(t)
    z = Z * sp.cos(nu * t)

    # Lagrange in the inertial frame with the absolute height y = z + xi (independent of the inertia-force route)
    y = z + xi
    T = m * y.diff(t)**2 / 2
    V = m * g * y + k * (xi - L0)**2 / 2
    L = T - V
    Qd = -c * xi.diff(t)                                  # damper: generalised force on xi
    eq = sp.diff(L.diff(xi.diff(t)), t) - L.diff(xi) - Qd
    xie = L0 - m * g / k
    chk("static equilibrium xi_e = L0 - m g/k (z = 0)", (k * (xi - L0) + m * g).subs(xi, xie))
    x = sp.Function("x")(t)
    eqx = sp.expand(eq.subs(xi, x + xie).doit())
    target = m * x.diff(t, 2) + c * x.diff(t) + k * x - m * nu**2 * Z * sp.cos(nu * t)
    chk("EOM: m x'' + c x' + k x = m nu^2 Z cos(nu t) (gravity cancels)", eqx, target)
    chk("inertia force -m z'' = m nu^2 Z cos(nu t)", -m * z.diff(t, 2), m * nu**2 * Z * sp.cos(nu * t))
    chk("absolute acceleration = z'' + x''", y.diff(t, 2).subs(xi, x + xie).doit(), z.diff(t, 2) + x.diff(t, 2))

    # steady state with the complex representation
    w0, zeta = sp.symbols("omega_0 zeta", positive=True)
    sub_w = {k: m * w0**2, c: 2 * zeta * m * w0}
    A = sp.symbols("A")
    Asol = sp.solve(sp.Eq((-m * nu**2 + sp.I * c * nu + k) * A, m * nu**2 * Z), A)[0].subs(sub_w)
    X = nu**2 * Z / sp.sqrt((w0**2 - nu**2)**2 + 4 * zeta**2 * w0**2 * nu**2)
    chk("|A| = nu^2 Z / sqrt((w0^2-nu^2)^2 + 4 zeta^2 w0^2 nu^2)", sp.Abs(Asol)**2, X**2,
        numeric={w0: 100, nu: 50, zeta: sp.Rational(1, 5), Z: 1})
    phi = sp.atan2(-2 * zeta * w0 * nu, w0**2 - nu**2)
    xp = X * sp.cos(nu * t + phi)
    res = (m * xp.diff(t, 2) + c * xp.diff(t) + k * xp - m * nu**2 * Z * sp.cos(nu * t)).subs(sub_w)
    for tv in (0, sp.Rational(1, 7), sp.Rational(3, 10)):
        chk.value(f"particular solution satisfies the EOM (t = {tv})",
                  res.subs({w0: 100, nu: 50, zeta: sp.Rational(1, 5), m: 1, Z: 1, t: tv}), 0, tol=1e-8)
    res2 = res.subs({w0: 100, nu: 300, zeta: sp.Rational(1, 5), m: 1, Z: 1, t: sp.Rational(1, 9)})
    chk.value("particular solution, above resonance (nu = 300)", res2, 0, tol=1e-6)

    # regimes
    r = sp.symbols("r", positive=True)
    H = r**2 / sp.sqrt((1 - r**2)**2 + (2 * zeta * r)**2)
    chk("X/Z = r^2 / sqrt((1-r^2)^2 + (2 zeta r)^2)", (X / Z).subs(nu, r * w0), H)
    chk("low frequency: X ~ nu^2 Z / w0^2 (H/r^2 -> 1)", sp.limit(H / r**2, r, 0), 1)
    chk("high frequency: X/Z -> 1", sp.limit(H, r, sp.oo), 1)
    chk.value("high frequency: phase -> -pi (r = 1e4)", sp.atan2(-2 * sp.Rational(1, 5) * 10**4, 1 - 10**8), -sp.pi, tol=1e-4)
    chk.value("low frequency: phase -> 0 (r = 1e-4)", sp.atan2(-2 * sp.Rational(1, 5) * sp.Rational(1, 10**4), 1 - sp.Rational(1, 10**8)), 0, tol=1e-4)
    s = sp.symbols("s", positive=True)
    f = s**2 / ((1 - s)**2 + 4 * zeta**2 * s)
    crit = sp.solve(sp.diff(f, s), s)
    chk.true("d/ds (X/Z)^2 = 0 at s = r^2 = 1/(1 - 2 zeta^2)",
             any(sp.simplify(cc - 1 / (1 - 2 * zeta**2)) == 0 for cc in crit), f"{crit}")
    chk("peak value X/Z = 1/(2 zeta sqrt(1 - zeta^2))", f.subs(s, 1 / (1 - 2 * zeta**2)), 1 / (4 * zeta**2 * (1 - zeta**2)))
    chk.true("peak is a maximum (zeta = 0.2)", sp.N(sp.diff(f, s, 2).subs({zeta: sp.Rational(1, 5), s: 1 / (1 - 2 * sp.Rational(1, 25))})) < 0)

    # energy per cycle W = int_0^{2pi/nu} c x'^2 dt = pi c nu X^2
    Xs, ph = sp.symbols("X phi", positive=True)
    xs = Xs * sp.cos(nu * t + ph)
    W = sp.integrate(c * xs.diff(t)**2, (t, 0, 2 * sp.pi / nu))
    chk("W = pi c nu X^2", W, sp.pi * c * nu * Xs**2)
    # input power of the inertia force over a cycle equals W (energy balance in steady state)
    Win = sp.integrate((m * nu**2 * Z * sp.cos(nu * t)) * xs.diff(t), (t, 0, 2 * sp.pi / nu))
    chk("work of -m z'' per cycle = pi m nu^2 Z X sin(-phi)", Win, -sp.pi * m * nu**2 * Z * Xs * sp.sin(ph))

    # numbers
    num = {m: sp.Rational(1, 20), k: 500, c: 2, Z: sp.Rational(2, 1000), nu: 50, g: sp.Rational(981, 100)}
    w0n = sp.sqrt(num[k] / num[m])
    zn = num[c] / (2 * sp.sqrt(num[k] * num[m]))
    chk("omega_0 = 100 rad/s", w0n, 100)
    chk("zeta = 0.2", zn, sp.Rational(1, 5))
    Xn = X.subs({w0: w0n, zeta: zn, nu: 50, Z: num[Z]})
    chk.value("X = 0.6442 mm", Xn * 1000, 0.644157, tol=1e-5)
    chk.value("X/Z = 0.25/sqrt(0.6025) = 0.3221", Xn / num[Z], 0.322078, tol=1e-5)
    chk.value("omega_0^2 X = 6.44 m/s^2 uses 1e4 * 6.442e-4", w0n**2 * Xn, 6.442, tol=1e-3)
    phn = sp.atan2(-2 * zn * w0n * 50, w0n**2 - 2500)
    chk.value("phi = -14.93 deg", phn * 180 / sp.pi, -14.9314, tol=1e-3)
    Wn = sp.pi * num[c] * 50 * Xn**2
    chk.value("W = 1.304e-4 J per cycle", Wn, 1.30362e-4, tol=1e-8)
    chk.value("input work per cycle = W", (sp.pi * num[m] * 2500 * num[Z] * Xn * sp.sin(-phn)), Wn, tol=1e-10)
    chk.value("static deflection m g/k = 0.981 mm", num[m] * num[g] / num[k] * 1000, 0.981)
    chk.value("base acceleration amplitude nu^2 Z = 5.0 m/s^2", 2500 * num[Z], 5.0)
    chk.value("accelerometer reading w0^2 X = 6.442 m/s^2 (+28.8 %)", w0n**2 * Xn, 6.44157, tol=1e-4)
    chk.value("relative error +28.8 %", (w0n**2 * Xn / 5 - 1) * 100, 28.83, tol=1e-2)
    H07 = 1 / sp.sqrt((1 - sp.Rational(1, 4))**2 + (2 * sp.Rational(7, 10) * sp.Rational(1, 2))**2)
    chk.value("with zeta = 0.7: X w0^2 / (nu^2 Z) = 0.975 (-2.5 %)", H07, 0.97474, tol=1e-4)
    chk.value("decay rate zeta w0 = 20 1/s, relaxation time 0.05 s", 1 / (zn * w0n), 0.05)
    chk.value("transient below 1 % after ln(100)/20 = 0.230 s", sp.log(100) / (zn * w0n), 0.230259, tol=1e-5)
    chk.value("damped frequency w0 sqrt(1 - zeta^2) = 97.98 rad/s", w0n * sp.sqrt(1 - zn**2), 97.9796, tol=1e-3)
    chk.value("nu_peak = w0/sqrt(1 - 2 zeta^2) = 104.3 rad/s", w0n / sp.sqrt(1 - 2 * zn**2), 104.257, tol=1e-3)
    chk.value("X_peak/Z = 2.552", 1 / (2 * zn * sp.sqrt(1 - zn**2)), 2.55155, tol=1e-4)
    chk.value("X_peak = 5.103 mm", 1000 * num[Z] / (2 * zn * sp.sqrt(1 - zn**2)), 5.1031, tol=1e-3)
    chk.value("X/Z at nu = w0: 1/(2 zeta) = 2.5 (below the peak)", H.subs({r: 1, zeta: zn}), 2.5)
