"""P15: relative motion near a target on a circular orbit, Clohessy-Wiltshire equations (bank item P15).

Independent routes: the relative acceleration is obtained by differentiating the inertial position of the chaser written
with the rotating unit vectors (no transport formula); the linear equations come from a SymPy series of the exact gravity
difference; the closed-form solution is checked by substitution into the ODEs and the initial conditions; the numerical
case is also integrated with the full nonlinear two-body equations (RK4) to confirm the linear prediction.
"""
import math

import numpy as np
import sympy as sp


def verify(chk):
    t = sp.symbols("t", real=True)
    mu, R, n = sp.symbols("mu R_T n", positive=True)
    x = sp.Function("x")(t)
    y = sp.Function("y")(t)
    xd, yd, xdd, ydd = x.diff(t), y.diff(t), x.diff(t, 2), y.diff(t, 2)
    # change of basis [e_x; e_y; k] = R [i; j; k] with R a rotation by n t about k
    Rm = sp.Matrix([[sp.cos(n * t), sp.sin(n * t), 0], [-sp.sin(n * t), sp.cos(n * t), 0], [0, 0, 1]])
    chk("R R^T = I", sum(xx**2 for xx in (Rm * Rm.T - sp.eye(3))))
    chk("det R = +1", Rm.det(), 1)
    ex_, ey_, kk_ = Rm[0, :].T, Rm[1, :].T, Rm[2, :].T
    chk("e_y = k x e_x", sum(xx**2 for xx in (kk_.cross(ex_) - ey_)))
    chk("Poisson: d e_x/dt = n k x e_x", sum(xx**2 for xx in (ex_.diff(t) - n * kk_.cross(ex_))))
    chk("Poisson: d e_y/dt = n k x e_y", sum(xx**2 for xx in (ey_.diff(t) - n * kk_.cross(ey_))))

    # ---- (a) inertial position with the rotating basis e_x = (cos nt, sin nt), e_y = (-sin nt, cos nt)
    ex = sp.Matrix([sp.cos(n * t), sp.sin(n * t)])
    ey = sp.Matrix([-sp.sin(n * t), sp.cos(n * t)])
    rP = (R + x) * ex + y * ey
    aP = rP.diff(t, 2)
    ax_rot = sp.simplify(aP.dot(ex))
    ay_rot = sp.simplify(aP.dot(ey))
    # transport formula of the note: a_P = a_T + a_rel + 2 w x v_rel + w x (w x rho)
    chk("a_P . e_x = -n^2 R + x'' - 2 n y' - n^2 x", ax_rot, -n**2 * R + xdd - 2 * n * yd - n**2 * x)
    chk("a_P . e_y = y'' + 2 n x' - n^2 y", ay_rot, ydd + 2 * n * xd - n**2 * y)

    # ---- (b) gravity difference, linearised
    eps = sp.symbols("epsilon")
    X, Y = sp.symbols("X Y", real=True)
    gx = -mu * (R + eps * X) / ((R + eps * X)**2 + (eps * Y)**2)**sp.Rational(3, 2)
    gy = -mu * (eps * Y) / ((R + eps * X)**2 + (eps * Y)**2)**sp.Rational(3, 2)
    gx1 = sp.series(gx, eps, 0, 2).removeO()
    gy1 = sp.series(gy, eps, 0, 2).removeO()
    chk("g_x = -mu/R^2 + 2 mu X/R^3 + O(rho^2)", gx1.subs(eps, 1), -mu / R**2 + 2 * mu * X / R**3)
    chk("g_y = -mu Y/R^3 + O(rho^2)", gy1.subs(eps, 1), -mu * Y / R**3)
    nn = sp.sqrt(mu / R**3)
    chk("target on circular orbit: n^2 R = mu/R^2", nn**2 * R, mu / R**2)
    # Newton: a_P = g(r_P) -> CW equations
    cwx = sp.expand((ax_rot - (gx1.subs(eps, 1)).subs({X: x, Y: y})).subs(mu, n**2 * R**3))
    cwy = sp.expand((ay_rot - (gy1.subs(eps, 1)).subs({X: x, Y: y})).subs(mu, n**2 * R**3))
    chk("CW radial: x'' - 2 n y' - 3 n^2 x = 0", cwx, xdd - 2 * n * yd - 3 * n**2 * x)
    chk("CW along-track: y'' + 2 n x' = 0", cwy, ydd + 2 * n * xd)

    # ---- (c) closed-form solution
    x0, y0, u0, w0 = sp.symbols("x0 y0 xdot0 ydot0", real=True)
    c, s_ = sp.cos(n * t), sp.sin(n * t)
    xs = 4 * x0 + 2 * w0 / n - (3 * x0 + 2 * w0 / n) * c + (u0 / n) * s_
    ys = y0 - (6 * n * x0 + 3 * w0) * t + (6 * x0 + 4 * w0 / n) * s_ + (2 * u0 / n) * (c - 1)
    chk("solution satisfies the radial equation", xs.diff(t, 2) - 2 * n * ys.diff(t) - 3 * n**2 * xs)
    chk("solution satisfies the along-track equation", ys.diff(t, 2) + 2 * n * xs.diff(t))
    chk("x(0) = x0", xs.subs(t, 0), x0)
    chk("y(0) = y0", ys.subs(t, 0), y0)
    chk("x'(0) = xdot0", xs.diff(t).subs(t, 0), u0)
    chk("y'(0) = ydot0", ys.diff(t).subs(t, 0), w0)
    chk("first integral y' + 2 n x = ydot0 + 2 n x0", ys.diff(t) + 2 * n * xs, w0 + 2 * n * x0)
    # quadrature for y of the note: y = y0 + int_0^t (C - 2 n x) dt
    tau = sp.symbols("tau", real=True)
    yq = y0 + sp.integrate((w0 + 2 * n * x0 - 2 * n * xs).subs(t, tau), (tau, 0, t))
    chk("y from the quadrature y' = C - 2 n x", yq, ys)
    # dsolve as a third route
    sol = sp.dsolve([sp.Eq(xdd - 2 * n * yd - 3 * n**2 * x, 0), sp.Eq(ydd + 2 * n * xd, 0)], [x, y],
                    ics={x.subs(t, 0): x0, y.subs(t, 0): y0, xd.subs(t, 0): u0, yd.subs(t, 0): w0})
    chk("dsolve agrees: x(t)", sp.simplify(sol[0].rhs - xs).rewrite(sp.cos), 0)
    chk("dsolve agrees: y(t)", sp.simplify(sol[1].rhs - ys).rewrite(sp.cos), 0)

    # ---- (d) secular drift
    lin = sp.Poly(sp.expand(ys - y0 - (6 * x0 + 4 * w0 / n) * s_ - (2 * u0 / n) * (c - 1)), t)
    chk("secular term coefficient = -(6 n x0 + 3 ydot0)", lin.coeff_monomial(t), -(6 * n * x0 + 3 * w0))
    Torb = 2 * sp.pi / n
    dy = sp.simplify(ys.subs(t, Torb) - y0)
    chk("drift per orbit = -12 pi x0 - 6 pi ydot0/n", dy, -12 * sp.pi * x0 - 6 * sp.pi * w0 / n)
    chk("x returns after one orbit", xs.subs(t, Torb), x0)
    chk("no drift iff ydot0 = -2 n x0", sp.solve(sp.Eq(6 * n * x0 + 3 * w0, 0), w0)[0], -2 * n * x0)
    chk("chaser at rest in S1 (ydot0 = 0): drift -12 pi x0", dy.subs(w0, 0), -12 * sp.pi * x0)
    # chaser on its own circular orbit of radius R + x0: angular rate n' = sqrt(mu/(R+x0)^3)
    d = sp.symbols("delta")
    w_circ = ((R + d * x0) * (sp.sqrt(mu / (R + d * x0)**3) - sp.sqrt(mu / R**3)))
    w_circ1 = sp.series(w_circ, d, 0, 2).removeO().subs(d, 1)
    chk("own circular orbit: ydot0 = -(3/2) n x0 to first order", w_circ1.subs(mu, n**2 * R**3), -sp.Rational(3, 2) * n * x0)
    chk("own circular orbit: drift per orbit = -3 pi x0", dy.subs(w0, -sp.Rational(3, 2) * n * x0), -3 * sp.pi * x0)
    chk("own circular orbit: x(t) = x0 for all t (u0 = 0)", xs.subs({w0: -sp.Rational(3, 2) * n * x0, u0: 0}), x0)
    chk("own circular orbit: y' = -(3/2) n x0 for all t", ys.diff(t).subs({w0: -sp.Rational(3, 2) * n * x0, u0: 0}),
        -sp.Rational(3, 2) * n * x0)
    chk("x0 = -1 km on own circular orbit: +9.425 km per orbit", (-3 * sp.pi * x0).subs(x0, -1000), 3000 * sp.pi)
    chk.value("3000 pi = 9424.8 m", 3000 * sp.pi, 9424.778, tol=1e-3)
    chk.value("x0 = -1 km at rest in S1: +37.70 km per orbit", (-12 * sp.pi * x0).subs(x0, -1000), 37699.11, tol=1e-2)

    chk("at rest in S1: x = 4 x0 - 3 x0 cos nt", xs.subs({w0: 0, u0: 0}), 4 * x0 - 3 * x0 * c)
    chk("at rest in S1: x at half orbit = 7 x0", xs.subs({w0: 0, u0: 0}).subs(t, sp.pi / n), 7 * x0)
    # semi-major axis offset from the linearised vis-viva: da = 2 dv/n + 2 dr, dv = y' + n x (inertial along-track)
    e1 = sp.symbols("e1")
    a_of = 1 / (2 / (R + e1 * x0) - (n * R + e1 * (w0 + n * x0))**2 / (n**2 * R**3))   # vis-viva, v = nR + dv
    da1 = sp.series(a_of, e1, 0, 2).removeO().subs(e1, 1) - R
    chk("vis-viva linearised: delta a = 2 C / n", da1, 2 * (w0 + 2 * n * x0) / n)
    # limit n -> 0: uniform straight motion
    chk("n -> 0: x -> x0 + xdot0 t", sp.limit(xs, n, 0), x0 + u0 * t)
    chk("n -> 0: y -> y0 + ydot0 t", sp.limit(ys, n, 0), y0 + w0 * t)

    # ---- (e) bounded motion: ellipse 2:1
    xb = xs.subs(w0, -2 * n * x0)
    yb = ys.subs(w0, -2 * n * x0)
    chk("bounded x = x0 cos nt + (xdot0/n) sin nt", xb, x0 * c + (u0 / n) * s_)
    yc = y0 - 2 * u0 / n
    chk("bounded y = y_c - 2 x0 sin nt + (2 xdot0/n) cos nt", yb, yc - 2 * x0 * s_ + (2 * u0 / n) * c)
    A2 = x0**2 + (u0 / n)**2
    chk("ellipse x^2 + (y - y_c)^2/4 = A^2", xb**2 + (yb - yc)**2 / 4, A2)
    # sense of motion at the top (x = A > 0 at t with sin = 0, x0 > 0, u0 = 0): y' = -2 n x0 < 0
    th = sp.symbols("theta")
    Ae = sp.symbols("A_e", positive=True)
    xe, ye = Ae * sp.cos(th), -2 * Ae * sp.sin(th)
    chk("sense: x y' - (y - y_c) x' = -2 n A_e^2", xe * sp.diff(ye, th) * n - ye * sp.diff(xe, th) * n, -2 * n * Ae**2)
    chk("at x = x0 (u0 = 0) the chaser moves with y' = -2 n x0 (towards -y)", yb.diff(t).subs({u0: 0, t: 0}), -2 * n * x0)

    # ---- (f) numbers: LEO
    mu_n, R_n = 3.986e14, 6.778e6
    n_n = math.sqrt(mu_n / R_n**3)
    chk.value("n = 1.1314e-3 rad/s", n_n, 1.13142e-3, tol=2e-8)
    T_n = 2 * math.pi / n_n
    chk.value("T = 5553 s = 92.6 min", T_n, 5553.4, tol=0.5)
    # case (i): x0 = 0, y0 = -1000 m, xdot0 = +0.5 m/s, ydot0 = 0
    case1 = {x0: 0, y0: -1000, u0: 0.5, w0: 0, n: n_n}
    chk.value("case (i): x after one orbit = 0", xs.subs(case1).subs(t, T_n), 0, tol=1e-6)
    chk.value("case (i): y after one orbit = -1000 m", ys.subs(case1).subs(t, T_n), -1000, tol=1e-6)
    chk.value("case (i): radial amplitude xdot0/n = 441.9 m", 0.5 / n_n, 441.93, tol=0.01)
    chk.value("case (i): y at half orbit = -1000 - 4 xdot0/n = -2768 m", ys.subs(case1).subs(t, T_n / 2), -2767.7, tol=0.1)
    chk.value("case (i): ellipse centre y_c = y0 - 2 xdot0/n = -1884 m", -1000 - 2 * 0.5 / n_n, -1883.8, tol=0.1)
    # case (ii): which along-track impulse brings the chaser to T after exactly one orbit (x0 = 0, xdot0 = 0)
    wsol = sp.solve(sp.Eq(ys.subs({x0: 0, u0: 0, y0: -1000}).subs(t, 2 * sp.pi / n), 0), w0)[0]
    chk("case (ii): ydot0 = y0 n / (6 pi) = -1000/(3 T)", wsol, -1000 * n / (6 * sp.pi))
    w_n = float(wsol.subs(n, n_n))
    chk.value("case (ii): ydot0 = -0.0600 m/s (backward)", w_n, -0.060023, tol=2e-6)
    case2 = {x0: 0, y0: -1000, u0: 0, w0: w_n, n: n_n}
    chk.value("case (ii): x(T) = 0", xs.subs(case2).subs(t, T_n), 0, tol=1e-6)
    chk.value("case (ii): x'(T) = 0", xs.diff(t).subs(case2).subs(t, T_n), 0, tol=1e-9)
    chk.value("case (ii): y'(T) = ydot0 (braking impulse +0.0600 m/s)", ys.diff(t).subs(case2).subs(t, T_n), w_n, tol=1e-9)
    chk.value("case (ii): x at half orbit = 4 ydot0/n = -212.2 m", xs.subs(case2).subs(t, T_n / 2), -212.2, tol=0.1)

    # nonlinear two-body integration of case (ii) in the inertial frame (RK4), result rotated into S1
    def f(s):
        r = math.hypot(s[0], s[1])
        return np.array([s[2], s[3], -mu_n * s[0] / r**3, -mu_n * s[1] / r**3])

    vT = n_n * R_n
    # chaser at y = -1000 m (behind) on the e_y axis at t = 0: r = R e_x + y0 e_y, v = v_T e_y + w x rho + v_rel
    y0n = -1000.0
    st = np.array([R_n, y0n, -n_n * y0n + 0.0, vT + w_n])
    N = 20000
    h = T_n / N
    for _ in range(N):
        k1 = f(st); k2 = f(st + h / 2 * k1); k3 = f(st + h / 2 * k2); k4 = f(st + h * k3)
        st = st + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    # target after one orbit is back at (R, 0); rotating basis is the inertial one at t = T
    chk.true("nonlinear check: miss distance after one orbit about 3 m, i.e. 2.8 m (linear theory: 0)",
             abs(math.hypot(st[0] - R_n, st[1]) - 2.8) < 0.05, f"miss = {math.hypot(st[0] - R_n, st[1]):.2f} m")
