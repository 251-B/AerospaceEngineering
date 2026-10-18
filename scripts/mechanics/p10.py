"""P10: free fall from a tower on the rotating Earth (bank item P10).

Local frame S1 = {A; x east, y north, z up} rotating with the Earth, omega = Omega (0, cos lam, sin lam).
Effective gravity -g k (centrifugal term absorbed). Relative motion: a = -g k - 2 omega x v.
Independent routes: (1) order-by-order perturbation solved by sympy dsolve-free integration of the full
vector equation, (2) RK4 numerical integration of the exact linear equation with the real Earth rate.
"""
import numpy as np
import sympy as sp


def _rk4_drop(Om, lam, g, h, v0z=0.0, z0=None, n=20000):
    """Integrate a = -g k - 2 w x v from (0, 0, z0) with velocity (0, 0, v0z) until z returns to 0."""
    w = Om * np.array([0.0, np.cos(lam), np.sin(lam)])
    z0 = h if z0 is None else z0

    def f(s):
        v = s[3:]
        return np.concatenate([v, np.array([0.0, 0.0, -g]) - 2 * np.cross(w, v)])

    # flight time of the zeroth-order motion, used to size the step; stop by linear interpolation at z = 0
    T0 = (v0z + np.sqrt(v0z**2 + 2 * g * z0)) / g
    dt = 1.2 * T0 / n
    s = np.array([0.0, 0.0, z0, 0.0, 0.0, v0z])
    t = 0.0
    while True:
        k1 = f(s)
        k2 = f(s + dt / 2 * k1)
        k3 = f(s + dt / 2 * k2)
        k4 = f(s + dt * k3)
        s1 = s + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if t > 0.1 * T0 and s1[2] <= 0.0:
            fr = s[2] / (s[2] - s1[2])
            return s + fr * (s1 - s), t + fr * dt
        s, t = s1, t + dt


def verify(chk):
    t = sp.symbols("t", nonnegative=True)
    Om, g, h, v0, lam, eps = sp.symbols("Omega g h v0 lambda epsilon", positive=True)
    w = sp.Matrix([0, Om * sp.cos(lam), Om * sp.sin(lam)])

    # (a) angular velocity of S1 from the rotation of the Earth axis: k_E = cos(lam) j + sin(lam) k
    kE = sp.Matrix([0, sp.cos(lam), sp.sin(lam)])
    chk("|k_E| = 1", kE.dot(kE), 1)
    for i in range(3):
        chk(f"omega_10 = Omega k_E (component {i})", w[i], Om * kE[i])
    # change of basis [i; j; k] = R [e_rho; e_phi; k_E], all written in the local basis
    e_rho = sp.Matrix([0, -sp.sin(lam), sp.cos(lam)])
    e_phi = sp.Matrix([1, 0, 0])
    chk("{e_rho, e_phi, k_E} right-handed: e_rho x e_phi = k_E", (e_rho.cross(e_phi) - kE).dot(e_rho.cross(e_phi) - kE))
    R = sp.Matrix([[0, 1, 0], [-sp.sin(lam), 0, sp.cos(lam)], [sp.cos(lam), 0, sp.sin(lam)]])
    B = sp.Matrix.hstack(e_rho, e_phi, kE).T  # rows: e_rho, e_phi, k_E in local components
    chk("R maps (e_rho, e_phi, k_E) to (i, j, k)", sum(x**2 for x in (R * B - sp.eye(3))))
    chk("R R^T = I", sum(x**2 for x in (R * R.T - sp.eye(3))))
    chk("det R = +1", R.det(), 1)
    chk("third column of R gives k_E = cos(lam) j + sin(lam) k", (R[:, 2] - kE).dot(R[:, 2] - kE))

    # (b) Coriolis term components: -2 w x v with v = (vx, vy, vz)
    vx, vy, vz = sp.symbols("v_x v_y v_z")
    cor = -2 * w.cross(sp.Matrix([vx, vy, vz]))
    chk("x: -2 Omega (cos(lam) vz - sin(lam) vy)", cor[0], -2 * Om * (sp.cos(lam) * vz - sp.sin(lam) * vy))
    chk("y: -2 Omega sin(lam) vx", cor[1], -2 * Om * sp.sin(lam) * vx)
    chk("z: +2 Omega cos(lam) vx", cor[2], 2 * Om * sp.cos(lam) * vx)

    # (c) perturbation: Omega -> eps*Omega, expand r = r0 + eps r1 + eps^2 r2, solve order by order by integration
    def integrate_twice(acc, r0, v0vec):
        vel = sp.Matrix([v0vec[i] + sp.integrate(acc[i], (t, 0, t)) for i in range(3)])
        pos = sp.Matrix([r0[i] + sp.integrate(vel[i], (t, 0, t)) for i in range(3)])
        return pos, vel

    def series_solution(z0, vz0):
        we = eps * w
        r0, v0_ = integrate_twice(sp.Matrix([0, 0, -g]), [0, 0, z0], [0, 0, vz0])
        r1, v1 = integrate_twice(-2 * w.cross(v0_), [0, 0, 0], [0, 0, 0])
        r2, v2 = integrate_twice(-2 * w.cross(v1), [0, 0, 0], [0, 0, 0])
        r = r0 + eps * r1 + eps**2 * r2
        # residual of the full equation up to O(eps^2) included
        res = (r.diff(t, 2) - (sp.Matrix([0, 0, -g]) - 2 * we.cross(r.diff(t))))
        res = res.applyfunc(lambda e: sp.expand(e).coeff(eps, 0) + sp.expand(e).coeff(eps, 1) * eps
                            + sp.expand(e).coeff(eps, 2) * eps**2)
        return r0, r1, r2, res

    r0, r1, r2, res = series_solution(h, 0)
    chk.true("series solution satisfies the equation to O(Omega^2)", all(sp.simplify(e) == 0 for e in res))
    chk("x1 = (1/3) Omega g t^3 cos(lam)", r1[0], Om * g * t**3 * sp.cos(lam) / 3)
    chk("y1 = 0 (no first-order north-south deflection)", r1[1], 0)
    chk("z1 = 0 (no first-order correction of the height)", r1[2], 0)
    chk("y2 = -(1/6) Omega^2 g t^4 sin(lam) cos(lam)", r2[1], -Om**2 * g * t**4 * sp.sin(lam) * sp.cos(lam) / 6)
    tl = sp.sqrt(2 * h / g)
    chk("landing time t_f = sqrt(2h/g) solves z0 = 0", r0[2].subs(t, tl), 0)
    dx = r1[0].subs(t, tl)
    chk("Delta x = (2 sqrt2/3) Omega cos(lam) sqrt(h^3/g)", dx, 2 * sp.sqrt(2) / 3 * Om * sp.cos(lam) * sp.sqrt(h**3 / g))

    # (d) numbers: h = 100 m, lam = 40 deg, Omega = 7.292e-5 rad/s, g = 9.81 m/s^2
    num = {h: 100, g: sp.Rational(981, 100), Om: sp.Rational(7292, 10**8), lam: sp.pi * 40 / 180}
    chk.value("Omega = 2 pi / sidereal day (86164 s) = 7.292e-5 rad/s", 2 * sp.pi / 86164, 7.292e-5, tol=1e-8)
    chk.value("t_f = 4.515 s", tl.subs(num), 4.5152, tol=1e-3)
    chk.value("Delta x = 1.681 cm (first order)", (dx * 100).subs(num), 1.6814, tol=1e-3)
    chk.value("x at t_f/2 is Delta x/8 = 0.2102 cm", (r1[0].subs(t, tl / 2) * 100).subs(num), 0.21018, tol=1e-4)
    chk.value("sqrt(h^3/g) = 319.3 s", sp.sqrt(h**3 / g).subs(num), 319.28, tol=1e-2)
    chk.value("2h/g = 20.39 s^2", (2 * h / g).subs(num), 20.387, tol=1e-3)
    chk.value("Omega t_f = 3.29e-4 (expansion parameter)", (Om * tl).subs(num) * 1e4, 3.2925, tol=1e-3)
    chk.value("cos 40 deg = 0.7660", sp.cos(num[lam]), 0.76604, tol=1e-5)
    (s_end, t_end) = _rk4_drop(7.292e-5, np.radians(40), 9.81, 100.0)
    chk.true("RK4 of the exact equation: Delta x = 1.681 cm within 0.1 %", abs(s_end[0] * 100 / 1.68140 - 1) < 1e-3,
             f"RK4 {s_end[0] * 100:.5f} cm")
    chk.true("RK4: southward deflection is ~1e-6 m (second order)", -1e-5 < s_end[1] < 0, f"RK4 y = {s_end[1]:.3e} m")

    chk("naive estimate Omega h cos(lam) t_f is 3/2 of Delta x", Om * h * sp.cos(lam) * tl / dx, sp.Rational(3, 2))
    chk("first-order velocity x1' = Omega g t^2 cos(lam)", r1[0].diff(t), Om * g * t**2 * sp.cos(lam))

    # (e) order of magnitude: second-order south deflection and the centrifugal acceleration
    y2f = r2[1].subs(t, tl)
    chk("y2(t_f) = -(2/3) Omega^2 h^2 sin(lam) cos(lam) / g", y2f, -sp.Rational(2, 3) * Om**2 * h**2 * sp.sin(lam) * sp.cos(lam) / g)
    chk.value("y2(t_f) = -1.779e-6 m", y2f.subs(num) * 1e6, -1.7793, tol=1e-3)
    chk.value("Omega^2 R / g = 3.453e-3 (R = 6.371e6 m)", (num[Om]**2 * 6.371e6 / num[g]), 3.4533e-3, tol=1e-6)
    chk.value("ratio y2/Delta x = Omega t_f sin(lam) / 2 (= 1.06e-4)",
              (y2f / dx).subs(num), -(num[Om] * tl.subs(num) * sp.sin(num[lam]) / 2), tol=1e-12)
    chk.value("|y2/Delta x| = 1.058e-4", sp.Abs(y2f / dx).subs(num), 1.0581e-4, tol=1e-7)

    # residual centrifugal term -w x (w x r) with r = z k: y-component -Omega^2 z sin(lam) cos(lam)
    zz = sp.symbols("z")
    rz = sp.Matrix([0, 0, zz])
    cf = -w.cross(w.cross(rz))
    chk("residual centrifugal (y) = -Omega^2 z sin(lam) cos(lam)", cf[1], -Om**2 * zz * sp.sin(lam) * sp.cos(lam))
    chk("residual centrifugal (z) = Omega^2 z cos^2(lam)", cf[2], Om**2 * zz * sp.cos(lam)**2)
    ycf = sp.integrate(sp.integrate(cf[1].subs(zz, r0[2]), (t, 0, t)), (t, 0, t))
    chk("its deflection at t_f = -(5/6) Omega^2 h^2 sin(lam) cos(lam)/g", ycf.subs(t, tl),
        -sp.Rational(5, 6) * Om**2 * h**2 * sp.sin(lam) * sp.cos(lam) / g)
    chk.value("= -2.224e-6 m", ycf.subs(t, tl).subs(num) * 1e6, -2.2241, tol=1e-3)
    chk.value("Omega^2 h = 5.317e-7 m/s^2 (size of the neglected term)", (Om**2 * h).subs(num) * 1e7, 5.3173, tol=1e-3)

    # (f) projectile fired vertically upward from the ground with speed v0
    r0u, r1u, r2u, resu = series_solution(0, v0)
    chk.true("upward shot: series solution satisfies the equation to O(Omega^2)", all(sp.simplify(e) == 0 for e in resu))
    chk("x1 = -Omega cos(lam) (v0 t^2 - g t^3/3)", r1u[0], -Om * sp.cos(lam) * (v0 * t**2 - g * t**3 / 3))
    Tf = 2 * v0 / g
    chk("return time 2 v0/g", r0u[2].subs(t, Tf), 0)
    chk("Delta x = -(4/3) Omega cos(lam) v0^3/g^2", r1u[0].subs(t, Tf), -sp.Rational(4, 3) * Om * sp.cos(lam) * v0**3 / g**2)
    chk("x1'(T) = 0: the westward drift velocity is cancelled exactly at landing", r1u[0].diff(t).subs(t, Tf), 0)
    chk.true("x1'(t) <= 0 on [0, T] (always drifting west)", sp.simplify(r1u[0].diff(t) + Om * sp.cos(lam) * g * t * (Tf - t)) == 0)
    tmax = v0 / g
    chk("x at the apex = -(2/3) Omega cos(lam) v0^3/g^2", r1u[0].subs(t, tmax), -sp.Rational(2, 3) * Om * sp.cos(lam) * v0**3 / g**2)
    chk("upward shot to height h: Delta x = -4 x (drop deflection)",
        (r1u[0].subs(t, Tf) / dx).subs(v0, sp.sqrt(2 * g * h)), -4)
    chk.value("v0 = sqrt(2 g h) = 44.29 m/s, Delta x = -6.726 cm", (r1u[0].subs(t, Tf) * 100).subs(v0, sp.sqrt(2 * g * h)).subs(num), -6.7259, tol=1e-3)
    chk.value("v0 = 50 m/s: flight time 2 v0/g = 10.19 s", Tf.subs({v0: 50, g: num[g]}), 10.1937, tol=1e-3)
    chk.value("v0 = 50 m/s: apex v0^2/(2g) = 127.4 m", (v0**2 / (2 * g)).subs({v0: 50, g: num[g]}), 127.421, tol=1e-3)
    numu = dict(num)
    numu[v0] = 50
    chk.value("v0 = 50 m/s: Delta x = -9.674 cm", (r1u[0].subs(t, Tf) * 100).subs(numu), -9.6741, tol=1e-3)
    (su, tu) = _rk4_drop(7.292e-5, np.radians(40), 9.81, 0.0, v0z=50.0, z0=0.0)
    chk.true("RK4 upward shot: Delta x = -9.674 cm within 0.1 %", abs(su[0] * 100 / -9.6741 - 1) < 1e-3,
             f"RK4 {su[0] * 100:.5f} cm")
