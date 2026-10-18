"""P14: drone flying a logarithmic spiral r = r0 exp(b phi) at constant speed v0 (bank item P14).

Independent route: the time law r(t) = r0 + c t, phi(t) = ln(r/r0)/b is checked against the speed directly in Cartesian
coordinates, the acceleration is obtained by differentiating the Cartesian position twice, and the radius of curvature
comes from the Cartesian curvature formula of the curve (x(phi), y(phi)), not from the polar components of the note.
"""
import sympy as sp


def verify(chk):
    ph = sp.symbols("phi", real=True)
    t = sp.symbols("t", nonnegative=True)
    r0, b, v0, m = sp.symbols("r0 b v0 m", positive=True)
    k = sp.sqrt(1 + b**2)

    # ---- (a) polar velocity from the constant speed
    phd = sp.symbols("phidot", positive=True)
    r_of = r0 * sp.exp(b * ph)
    rd = sp.diff(r_of, ph) * phd                       # chain rule: dr/dt = (dr/dphi) phi'
    chk("r' = b r phi'", rd, b * r_of * phd)
    sol = sp.solve(sp.Eq(rd**2 + (r_of * phd)**2, v0**2), phd)
    chk.true("speed fixes a single positive phi'", len(sol) == 1)
    chk("phi' = v0 / (r sqrt(1+b^2))", sol[0], v0 / (r_of * k))
    chk("r' = b v0 / sqrt(1+b^2) (constant)", rd.subs(phd, sol[0]), b * v0 / k)
    chk("tan(alpha) = v_phi / v_r = 1/b", (r_of * phd) / rd, 1 / b)

    # ---- time law: r(t) = r0 + c t, phi(t) from the quadrature with u = r0 + c t
    c = b * v0 / k
    r_t = r0 + c * t
    u = sp.symbols("u", positive=True)
    phi_t = sp.integrate((v0 / k) / u, (u, r0, r_t)) / c      # dphi = (v0/k) dt / r, dt = du / c
    chk("phi(t) = ln(r(t)/r0)/b", sp.expand_log(phi_t - sp.log(r_t / r0) / b, force=True))
    X = r_t * sp.cos(phi_t)
    Y = r_t * sp.sin(phi_t)
    speed2 = sp.diff(X, t)**2 + sp.diff(Y, t)**2
    chk("Cartesian check: |v|^2 = v0^2 along the time law", speed2, v0**2)
    chk("Cartesian check: the time law lies on the spiral", r_t - r0 * sp.exp(b * phi_t))

    # ---- (b) times and angles, numbers r0 = 20 m, b = 3/4, v0 = 10 m/s, m = 2 kg, r1 = 20 m, r2 = 50 m
    num = {r0: 20, b: sp.Rational(3, 4), v0: 10, m: 2}
    chk("sqrt(1+b^2) = 5/4", k.subs(num), sp.Rational(5, 4))
    chk("r' = 6 m/s", c.subs(num), 6)
    chk("r phi' = 8 m/s", (v0 / k).subs(num), 8)
    t12 = sp.solve(sp.Eq(r_t.subs(num), 50), t)[0]
    chk("time from r = 20 m to r = 50 m: 5 s", t12, 5)
    chk("time = (r2 - r1) sqrt(1+b^2)/(b v0)", t12, ((50 - 20) * k / (b * v0)).subs(num))
    dphi = phi_t.subs(num).subs(t, t12)
    chk("turned angle = ln(2.5)/0.75", dphi, sp.log(sp.Rational(5, 2)) * sp.Rational(4, 3))
    chk.value("turned angle = 1.2217 rad = 70.00 deg", dphi * 180 / sp.pi, 69.9995, tol=1e-3)

    # ---- (c) arc length and intrinsic basis
    rr = sp.symbols("r", positive=True)
    ds_dr = sp.sqrt(1 + (rr * sp.diff(sp.log(rr / r0) / b, rr))**2)   # ds = sqrt(dr^2 + r^2 dphi^2), phi(r) = ln(r/r0)/b
    chk("ds/dr = sqrt(1+b^2)/b", ds_dr, k / b)
    s_r = sp.integrate(ds_dr, (rr, r0, rr))
    chk("s(r) = (r - r0) sqrt(1+b^2)/b", s_r, (rr - r0) * k / b)
    chk("s from 20 m to 50 m = 50 m = v0 * t12", s_r.subs(num).subs(rr, 50), 50)
    tvec = sp.Matrix([b, 1]) / k
    nvec = sp.Matrix([-1, b]) / k
    chk("t . n = 0", tvec.dot(nvec))
    chk("|n| = 1", nvec.dot(nvec), 1)
    # d e_t/dt with constant polar components: (b e_r' + e_phi')/k = phi' (b e_phi - e_r)/k -> curvature phi'/v0
    phd_t = v0 / (rr * k)
    chk("|de_t/ds| = phi'/v0 = 1/(r sqrt(1+b^2))", phd_t / v0, 1 / (rr * k))
    chk("n = t rotated +90 deg (k x t), e_r", -tvec[1], nvec[0])
    chk("n = t rotated +90 deg (k x t), e_phi", tvec[0], nvec[1])

    # ---- (d) acceleration: Cartesian differentiation vs polar components of the note
    AX, AY = sp.diff(X, t, 2), sp.diff(Y, t, 2)
    er = sp.Matrix([sp.cos(phi_t), sp.sin(phi_t)])
    ep = sp.Matrix([-sp.sin(phi_t), sp.cos(phi_t)])
    # change of basis [e_r; e_phi] = R [i; j]
    qa = sp.symbols("qa", real=True)
    Rm = sp.Matrix([[sp.cos(qa), sp.sin(qa)], [-sp.sin(qa), sp.cos(qa)]])
    chk("R rows are e_r, e_phi", sum(xx**2 for xx in (Rm - sp.Matrix.hstack(er, ep).T.subs(phi_t, qa))))
    chk("R R^T = I", sum(xx**2 for xx in (Rm * Rm.T - sp.eye(2))))
    chk("det R = +1", Rm.det(), 1)
    A = sp.Matrix([AX, AY])
    a_r = sp.simplify(A.dot(er))
    a_p = sp.simplify(A.dot(ep))
    chk("a_r = -v0^2 / (r (1+b^2))", a_r, -v0**2 / (r_t * k**2))
    chk("a_phi = b v0^2 / (r (1+b^2))", a_p, b * v0**2 / (r_t * k**2))
    chk("polar: phi'' = -r' phi' / r", sp.diff(phi_t, t, 2), -c * sp.diff(phi_t, t) / r_t)
    chk("polar: a_phi = r phi'' + 2 r' phi' = r' phi'", r_t * sp.diff(phi_t, t, 2) + 2 * c * sp.diff(phi_t, t),
        c * sp.diff(phi_t, t))
    chk("a . v = 0 (tangential acceleration zero)", A.dot(sp.Matrix([sp.diff(X, t), sp.diff(Y, t)])))
    # radius of curvature of the curve itself
    xp, yp = r_of * sp.cos(ph), r_of * sp.sin(ph)
    num_k = sp.diff(xp, ph) * sp.diff(yp, ph, 2) - sp.diff(yp, ph) * sp.diff(xp, ph, 2)
    den_k = (sp.diff(xp, ph)**2 + sp.diff(yp, ph)**2)**sp.Rational(3, 2)
    rho = sp.simplify(den_k / num_k)
    chk("Cartesian curvature: rho = r sqrt(1+b^2)", rho, r_of * k)
    chk("|a| = v0^2 / rho", sp.sqrt(a_r**2 + a_p**2), v0**2 / (r_t * k))
    chk("a = (v0^2/rho) n, e_r component", a_r, (v0**2 / (r_t * k)) * nvec[0])
    chk("a = (v0^2/rho) n, e_phi component", a_p, (v0**2 / (r_t * k)) * nvec[1])
    at20 = {t: 0}
    chk("rho(20 m) = 25 m", (r_t * k).subs(num).subs(at20), 25)
    chk("|a|(20 m) = 4 m/s^2", (v0**2 / (r_t * k)).subs(num).subs(at20), 4)
    chk("a_r(20 m) = -3.2 m/s^2", a_r.subs(num).subs(at20), -sp.Rational(16, 5))
    chk("a_phi(20 m) = 2.4 m/s^2", a_p.subs(num).subs(at20), sp.Rational(12, 5))
    chk("rho(50 m) = 62.5 m", (r_t * k).subs(num).subs(t, 5), sp.Rational(125, 2))
    chk("a_phi = -b a_r", a_p, -b * a_r)
    chk("polar power: a_r r' + a_phi r phi' = 0", a_r * c + a_p * v0 / k)
    chk("|a|(50 m) = 1.6 m/s^2", (v0**2 / (r_t * k)).subs(num).subs(t, 5), sp.Rational(8, 5))

    # ---- (e) force, torque, angular momentum
    F_r, F_p = (m * a_r).subs(num).subs(at20), (m * a_p).subs(num).subs(at20)
    chk("F_r(20 m) = -6.4 N", F_r, -sp.Rational(32, 5))
    chk("F_phi(20 m) = 4.8 N", F_p, sp.Rational(24, 5))
    chk("|F|(20 m) = 8 N", sp.sqrt(F_r**2 + F_p**2), 8)
    h = X * sp.diff(Y, t) - Y * sp.diff(X, t)             # k-component of r x v (per unit mass)
    chk("h = r^2 phi' = r v0 / sqrt(1+b^2)", h, r_t * v0 / k)
    chk("dh/dt = r a_phi", sp.diff(h, t), r_t * a_p)
    chk("dh/dt = b v0^2/(1+b^2) (constant)", sp.diff(h, t), b * v0**2 / k**2)
    chk("torque M_O = m r a_phi = 96 N m", (m * r_t * a_p).subs(num), 96)
    chk("h(20 m) = 160 m^2/s", h.subs(num).subs(at20), 160)
    chk("h(50 m) = 400 m^2/s", h.subs(num).subs(t, 5), 400)
    chk("Delta h = (dh/dt) * 5 s = 240 m^2/s", (sp.diff(h, t) * 5).subs(num), 240)
    chk("H_O = m h(50 m) = 800 kg m^2/s", (m * h).subs(num).subs(t, 5), 800)
    chk("H_O = m h(20 m) = 320 kg m^2/s", (m * h).subs(num).subs(at20), 320)
    chk("Delta H_O = M_O * 5 s = 480 kg m^2/s", 96 * 5, (m * h).subs(num).subs(t, 5) - (m * h).subs(num).subs(at20))
    chk("angle between F and -e_r: cos = 1/sqrt(1+b^2), i.e. tan = b", -nvec[0], 1 / k)
    chk.value("angle between F and -e_r = atan(3/4) = 36.87 deg", sp.atan(sp.Rational(3, 4)) * 180 / sp.pi, 36.8699, tol=1e-3)
    chk.value("alpha = atan(4/3) = 53.13 deg", sp.atan(sp.Rational(4, 3)) * 180 / sp.pi, 53.1301, tol=1e-3)
    # flying inwards (phi decreasing): r reaches 0 in finite time after infinitely many turns, with finite length
    chk("inwards: time to reach O from r0 = r0 sqrt(1+b^2)/(b v0) = 10/3 s", (r0 * k / (b * v0)).subs(num), sp.Rational(10, 3))
    chk("inwards: length to O = s(r0) - s(0) = r0 sqrt(1+b^2)/b = 100/3 m", (s_r.subs(rr, r0) - s_r.subs(rr, 0)).subs(num), sp.Rational(100, 3))
    chk.true("inwards: phi = ln(r/r0)/b -> -oo as r -> 0", sp.limit(sp.log(rr / r0) / b, rr, 0, "+") == -sp.oo)

    # ---- (f) power and kinetic energy
    v = sp.Matrix([sp.diff(X, t), sp.diff(Y, t)])
    chk("power F . v = 0", (m * A).dot(v))
    chk("d(E_kin)/dt = 0", sp.diff(m * v.dot(v) / 2, t))
    chk("E_kin = 100 J", (m * v0**2 / 2).subs(num), 100)
