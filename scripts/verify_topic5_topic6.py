#!/usr/bin/env python3
"""Symbolic and numerical verification of Chapter 5 and Chapter 6 (Advanced Maths).

    python scripts/verify_topic5_topic6.py    # exit 1 if any check fails
"""
import math
import sys

import sympy as sp

checks = 0
failures = []


def check(name, cond, detail=""):
    global checks
    checks += 1
    if not cond:
        failures.append((name, detail))
        print(f"FAIL [{name}]: {detail}")


def is_zero(expr):
    expr = sp.sympify(expr)
    if sp.simplify(expr) == 0:
        return True
    return sp.simplify(sp.expand(expr)) == 0


# ============================================================================
# CHAPTER 5 — COUPLED NONLINEAR SYSTEMS
# ============================================================================
def verify_ch5():
    x, y, lam, k, omega = sp.symbols("x y lam k omega", real=True)

    # Ex 1: Linearised centre + radial ODE
    f1 = -y + lam * x * (x**2 + y**2)
    f2 = x + lam * y * (x**2 + y**2)
    J1 = sp.Matrix([[f1.diff(x), f1.diff(y)], [f2.diff(x), f2.diff(y)]]).subs({x: 0, y: 0})
    check("Ch5-Ex1 eigenvalues", set(J1.eigenvals().keys()) == {sp.I, -sp.I}, str(J1.eigenvals()))
    r2_dot = sp.expand(2 * x * f1 + 2 * y * f2)
    check("Ch5-Ex1 r^2 dot", is_zero(r2_dot - 2 * lam * (x**2 + y**2) ** 2), str(r2_dot))

    # Ex 2: Seven population models
    models = [
        ("2(i)", x * (2 - x - y), y * (2 - 2 * y - 2 * x), [(0, 0), (2, 0), (0, 1)]),
        ("2(ii)", x * (2 - x - y), y * (2 - 2 * y - x / 4), [(0, 0), (2, 0), (0, 1), (sp.Rational(8, 7), sp.Rational(6, 7))]),
        ("2(iii)", x * (2 - x - 3 * y), y * (2 - 2 * y - 3 * x), [(0, 0), (2, 0), (0, 1), (sp.Rational(2, 7), sp.Rational(4, 7))]),
        ("2(iv)", x * (1 - 2 * y), y * (-2 + 3 * x), [(0, 0), (sp.Rational(2, 3), sp.Rational(1, 2))]),
        ("2(v)", x * (4 - x / 2 - 3 * y), y * (-2 + x), [(0, 0), (8, 0), (2, 1)]),
        ("2(vi)", x * (10 - x - 3 * y), y * (1 + x - 10 * y), [(0, 0), (10, 0), (0, sp.Rational(1, 10)), (sp.Rational(97, 13), sp.Rational(11, 13))]),
        ("2(vii)", x * (3 - x - y), y * (-2 + x), [(0, 0), (3, 0), (2, 1)]),
    ]
    for tag, fx, fy, eqs in models:
        J = sp.Matrix([[fx.diff(x), fx.diff(y)], [fy.diff(x), fy.diff(y)]])
        for xs, ys in eqs:
            check(f"Ch5-Ex{tag} eq ({xs},{ys})",
                  is_zero(fx.subs({x: xs, y: ys})) and is_zero(fy.subs({x: xs, y: ys})),
                  "non-zero")
            Je = J.subs({x: xs, y: ys})
            check(f"Ch5-Ex{tag} non-degenerate ({xs},{ys})",
                  Je.det() != 0 or tag == "2(i)", f"det={Je.det()}")

    # Check 2(iv) Lotka-Volterra conserved quantity
    H_lv = 3 * x - 2 * sp.log(x) + 2 * y - sp.log(y)
    dH_lv = sp.simplify(H_lv.diff(x) * x * (1 - 2 * y) + H_lv.diff(y) * y * (-2 + 3 * x))
    check("Ch5-Ex2(iv) conserved H", dH_lv == 0, str(dH_lv))

    # Check 2(v) and 2(vii) interior stable spirals
    J2v = sp.Matrix([[(-x / 2).subs(x, 2), -6], [1, 0]])  # at (2,1): fx_x = -2/2 = -1
    J2v_exact = sp.Matrix([[(x * (4 - x / 2 - 3 * y)).diff(x), (x * (4 - x / 2 - 3 * y)).diff(y)],
                           [(y * (-2 + x)).diff(x), (y * (-2 + x)).diff(y)]]).subs({x: 2, y: 1})
    check("Ch5-Ex2(v) tr/det at (2,1)", J2v_exact.trace() == -1 and J2v_exact.det() == 6)
    J2vii = sp.Matrix([[(x * (3 - x - y)).diff(x), (x * (3 - x - y)).diff(y)],
                       [(y * (-2 + x)).diff(x), (y * (-2 + x)).diff(y)]]).subs({x: 2, y: 1})
    check("Ch5-Ex2(vii) tr/det at (2,1)", J2vii.trace() == -2 and J2vii.det() == 2)

    # Ex 3: Cooperative models
    f3a_x, f3a_y = x * (1 - x + y), y * (1 + x - 2 * y)
    for xs, ys in [(0, 0), (1, 0), (0, sp.Rational(1, 2)), (3, 2)]:
        check(f"Ch5-Ex3(i) eq ({xs},{ys})",
              is_zero(f3a_x.subs({x: xs, y: ys})) and is_zero(f3a_y.subs({x: xs, y: ys})))
    J3a = sp.Matrix([[f3a_x.diff(x), f3a_x.diff(y)], [f3a_y.diff(x), f3a_y.diff(y)]]).subs({x: 3, y: 2})
    check("Ch5-Ex3(i) stable node (3,2)", J3a.trace() == -7 and J3a.det() == 6)

    f3b_x, f3b_y = x * (2 - x + y), y * (4 + 2 * x - y)
    sol3b = sp.solve([2 - x + y, 4 + 2 * x - y], [x, y])
    check("Ch5-Ex3(ii) no positive coexistence", sol3b[x] < 0, str(sol3b))

    # Ex 4: Conservative potentials (including sheet vs Robinson Ex 4(iii))
    V4i = sp.Rational(1, 2) * omega**2 * x**2
    V4ii = sp.Rational(1, 2) * x**4 - x**2
    V4iii_sheet = sp.Rational(1, 2) * x**6 - sp.Rational(5, 4) * x**4 + 2 * x**2
    V4iii_rob = sp.Rational(1, 6) * x**6 - sp.Rational(5, 4) * x**4 + 2 * x**2
    for label, V in [("4(i)", V4i), ("4(ii)", V4ii), ("4(iii)-sheet", V4iii_sheet), ("4(iii)-rob", V4iii_rob)]:
        E = sp.Rational(1, 2) * y**2 + V
        Edot = sp.simplify(E.diff(x) * y + E.diff(y) * (-V.diff(x)))
        check(f"Ch5-Ex{label} dE/dt=0", Edot == 0, str(Edot))
    check("Ch5-Ex4(iii) sheet V' only x=0 real",
          sp.solve(V4iii_sheet.diff(x), x, domain=sp.S.Reals) == [0] or len([r for r in sp.solve(V4iii_sheet.diff(x), x) if r.is_real]) == 1)
    check("Ch5-Ex4(iii) Robinson V' roots",
          set(sp.solve(V4iii_rob.diff(x), x)) == {-2, -1, 0, 1, 2})

    # Ex 5: Particle on a wire (conservative)
    for label, V in [("5(i)", V4i), ("5(ii)", V4ii)]:
        Vp = V.diff(x)
        Vpp = Vp.diff(x)
        # d/dt [1/2 (1 + V'^2) y^2 + V] = 0 => y * [ (1+V'^2) y' + V' V'' y^2 + V' ] = 0
        ydot = -(Vp * (1 + Vpp * y**2)) / (1 + Vp**2)
        E_wire = sp.Rational(1, 2) * (1 + Vp**2) * y**2 + V
        Edot_w = sp.simplify(E_wire.diff(x) * y + E_wire.diff(y) * ydot)
        check(f"Ch5-Ex{label} wire dE/dt=0", Edot_w == 0, str(Edot_w))
        J_wire = sp.Matrix([[0, 1], [ydot.diff(x), ydot.diff(y)]]).subs({y: 0})
        # At equilibria V'(x*)=0
        xstar = 0 if label == "5(i)" else 1
        check(f"Ch5-Ex{label} wire Jacobian at eq",
              sp.simplify(J_wire.subs(x, xstar) - sp.Matrix([[0, 1], [-Vpp.subs(x, xstar), 0]])) == sp.zeros(2, 2))

    # Ex 6 & 7: Damped potentials & wire
    for label, V in [("6(i)", sp.Rational(1, 2) * x**2), ("6(ii)", V4ii), ("6(iii)-sheet", V4iii_sheet), ("6(iii)-rob", V4iii_rob)]:
        E = sp.Rational(1, 2) * y**2 + V
        Edot = sp.simplify(E.diff(x) * y + E.diff(y) * (-V.diff(x) - y))
        check(f"Ch5-Ex{label} dE/dt=-y^2", Edot == -y**2, str(Edot))

    # Ex 6(ii) eigenvalues at 0 and +/-1
    J6ii_0 = sp.Matrix([[0, 1], [-V4ii.diff(x, 2).subs(x, 0), -1]])
    J6ii_1 = sp.Matrix([[0, 1], [-V4ii.diff(x, 2).subs(x, 1), -1]])
    check("Ch5-Ex6(ii) origin saddle", set(J6ii_0.eigenvals().keys()) == {1, -2})
    check("Ch5-Ex6(ii) wells spirals", set(J6ii_1.eigenvals().keys()) == {
        sp.Rational(-1, 2) + sp.I * sp.sqrt(15) / 2,
        sp.Rational(-1, 2) - sp.I * sp.sqrt(15) / 2,
    })

    # Ex 7: damped wire horizontal drag ydot = (-V' - k*y - V'*V''*y^2)/(1+V'^2)
    V_gen = sp.Function("V")(x)
    Vp_g, Vpp_g = V_gen.diff(x), V_gen.diff(x, 2)
    vpp_sym = sp.Symbol("vpp_sym", real=True)
    ydot_7 = (-Vp_g - k * y - Vp_g * Vpp_g * y**2) / (1 + Vp_g**2)
    J7 = sp.Matrix([[0, 1], [ydot_7.diff(x), ydot_7.diff(y)]]).subs(y, 0).subs(Vpp_g, vpp_sym).subs(Vp_g, 0)
    check("Ch5-Ex7 wire Jacobian equals flat",
          sp.simplify(J7 - sp.Matrix([[0, 1], [-vpp_sym, -k]])) == sp.zeros(2, 2), str(J7))

    # Ex 8, 9, 10: Pendulums
    E_pend = sp.Rational(1, 2) * y**2 - sp.cos(x)
    check("Ch5-Ex8 dE/dt=0", sp.simplify(E_pend.diff(x) * y + E_pend.diff(y) * (-sp.sin(x))) == 0)
    check("Ch5-Ex9 dE/dt=-ky^2", sp.simplify(E_pend.diff(x) * y + E_pend.diff(y) * (-sp.sin(x) - k * y)) == -k * y**2)
    check("Ch5-Ex10 dE/dt (y>0)", sp.simplify(E_pend.diff(x) * y + E_pend.diff(y) * (-sp.sin(x) - k * y**2)) == -k * y**3)
    check("Ch5-Ex10 dE/dt (y<0)", sp.simplify(E_pend.diff(x) * y + E_pend.diff(y) * (-sp.sin(x) + k * y**2)) == k * y**3)


# ============================================================================
# CHAPTER 6 — STURM-LIOUVILLE PROBLEMS & FOURIER SERIES
# ============================================================================
def verify_ch6():
    x, L, t, lam = sp.symbols("x L t lam", real=True, positive=True)
    n, m = sp.symbols("n m", integer=True, positive=True)

    # Ex 1 (i)-(iii)
    phi1 = sp.sin(n * sp.pi * x)
    check("Ch6-Ex1(i) ODE & BCs",
          is_zero(phi1.diff(x, 2) + (n * sp.pi) ** 2 * phi1) and phi1.subs(x, 0) == 0 and phi1.subs(x, 1) == 0)
    lam2 = ((2 * n - 1) * sp.pi / 2) ** 2
    phi2 = sp.sin((2 * n - 1) * sp.pi * x / 2)
    check("Ch6-Ex1(ii) ODE & BCs",
          is_zero(phi2.diff(x, 2) + lam2 * phi2) and phi2.subs(x, 0) == 0 and sp.simplify(phi2.diff(x).subs(x, 1)) == 0)
    phi3 = sp.cos(n * sp.pi * x)
    check("Ch6-Ex1(iii) ODE & BCs",
          is_zero(phi3.diff(x, 2) + (n * sp.pi) ** 2 * phi3) and phi3.diff(x).subs(x, 0) == 0 and sp.simplify(phi3.diff(x).subs(x, 1)) == 0)
    # Ex 1(iv): numerical root for h=1
    mu1 = float(sp.nsolve(sp.tan(x) + x, 2.0))
    phi4 = math.sin(mu1 * 1.0)
    phi4p = mu1 * math.cos(mu1 * 1.0)
    check("Ch6-Ex1(iv) Robin BC at x=1 (h=1)", abs(phi4p + 1.0 * phi4) < 1e-10)

    # Ex 2 (i)-(iii)
    y2i = sp.exp(-x / 2) * sp.sin(n * sp.pi * x)
    lam2i = n**2 * sp.pi**2 - sp.Rational(3, 4)
    check("Ch6-Ex2(i) ODE & BCs",
          is_zero(y2i.diff(x, 2) + y2i.diff(x) + (1 + lam2i) * y2i)
          and y2i.subs(x, 0) == 0 and sp.simplify(y2i.subs(x, 1)) == 0)

    # Ex 2(ii): lambda_0 = 0 (y_0 = x e^{-x}) AND lambda_n = -omega_n^2 (tan(omega_n) = omega_n)
    y2ii_0 = x * sp.exp(-x)
    check("Ch6-Ex2(ii) lambda_0=0 ODE & BCs",
          is_zero(y2ii_0.diff(x, 2) + 2 * y2ii_0.diff(x) + y2ii_0)
          and y2ii_0.subs(x, 0) == 0 and sp.simplify(y2ii_0.diff(x).subs(x, 1)) == 0)
    om1 = float(sp.nsolve(sp.tan(x) - x, 4.5))
    y2ii_1_bc = (-math.sin(om1) + om1 * math.cos(om1)) * math.exp(-1.0)
    check("Ch6-Ex2(ii) tan(om)=om BC at x=1", abs(y2ii_1_bc) < 1e-10)
    # Check weighted orthogonality int_0^1 (x e^{-x})(e^{-x} sin(om1 x)) e^{2x} dx == int_0^1 x sin(om1 x) dx == 0
    orth_2ii = float(sp.integrate(x * sp.sin(om1 * x), (x, 0, 1)))
    check("Ch6-Ex2(ii) orthogonality y0 vs y1", abs(orth_2ii) < 1e-10, f"val={orth_2ii}")

    # Ex 2(iii): lambda_0 = -1 (y_0 = 1) AND lambda_n = n^2 pi^2 / 3 - 1/4
    y2iii_n = sp.exp(sp.Rational(3, 2) * x) * (sp.cos(n * sp.pi * x) - sp.Rational(3, 2) / (n * sp.pi) * sp.sin(n * sp.pi * x))
    lam2iii_n = n**2 * sp.pi**2 / 3 - sp.Rational(1, 4)
    check("Ch6-Ex2(iii) ODE & BCs",
          is_zero(y2iii_n.diff(x, 2) - 3 * y2iii_n.diff(x) + 3 * (1 + lam2iii_n) * y2iii_n)
          and sp.simplify(y2iii_n.diff(x).subs(x, 0)) == 0 and sp.simplify(y2iii_n.diff(x).subs(x, 1)) == 0)
    orth_2iii = sp.simplify(sp.integrate(1 * y2iii_n.subs(n, 1) * sp.exp(-3 * x), (x, 0, 1)))
    check("Ch6-Ex2(iii) orthogonality y0 vs y1", orth_2iii == 0, str(orth_2iii))

    # Ex 3: Integrating factor mu(x) = exp(int alpha(x) dx)
    xr = sp.Symbol("xr", real=True)
    alpha = sp.Function("alpha")(xr)
    beta = sp.Function("beta")(xr)
    gamma = sp.Function("gamma")(xr)
    phi = sp.Function("phi")(xr)
    mu = sp.exp(sp.Integral(alpha, xr))
    lhs3 = sp.diff(mu * phi.diff(xr), xr) + (lam * mu * beta + mu * gamma) * phi
    rhs3 = mu * (phi.diff(xr, 2) + alpha * phi.diff(xr) + (lam * beta + gamma) * phi)
    check("Ch6-Ex3 integrating factor identity", sp.simplify(lhs3 - rhs3) == 0)

    # Ex 4: Euler-Cauchy S-L on [1, 2]
    phi4_n = sp.sin(n * sp.pi * sp.log(x) / sp.log(2))
    lam4_n = (n * sp.pi / sp.log(2)) ** 2
    check("Ch6-Ex4 ODE & BCs",
          is_zero(x**2 * phi4_n.diff(x, 2) + x * phi4_n.diff(x) + lam4_n * phi4_n)
          and phi4_n.subs(x, 1) == 0 and sp.simplify(phi4_n.subs(x, 2)) == 0)
    orth_4 = sp.simplify(sp.integrate((1 / x) * phi4_n.subs(n, 1) * phi4_n.subs(n, 2), (x, 1, 2)))
    check("Ch6-Ex4 orthogonality weight 1/x", orth_4 == 0, str(orth_4))

    # Ex 5 (i)-(ix): Symbolic Fourier coefficients check for k=1..4
    xs = sp.Symbol("xs", real=True)

    def check_fourier_full(label, f_expr, half_L, exp_a0, exp_an, exp_bn, pieces=None):
        if pieces is None:
            a0 = sp.simplify(sp.integrate(f_expr, (xs, -half_L, half_L)) / (2 * half_L))
        else:
            a0 = sp.simplify(sum(sp.integrate(fe, (xs, a, b)) for fe, a, b in pieces) / (2 * half_L))
        check(f"Ch6-Ex{label} a0", sp.simplify(a0 - exp_a0) == 0, f"got {a0}, exp {exp_a0}")
        for k_val in range(1, 5):
            if pieces is None:
                an = sp.simplify(sp.integrate(f_expr * sp.cos(k_val * sp.pi * xs / half_L), (xs, -half_L, half_L)) / half_L)
                bn = sp.simplify(sp.integrate(f_expr * sp.sin(k_val * sp.pi * xs / half_L), (xs, -half_L, half_L)) / half_L)
            else:
                an = sp.simplify(sum(sp.integrate(fe * sp.cos(k_val * sp.pi * xs / half_L), (xs, a, b)) for fe, a, b in pieces) / half_L)
                bn = sp.simplify(sum(sp.integrate(fe * sp.sin(k_val * sp.pi * xs / half_L), (xs, a, b)) for fe, a, b in pieces) / half_L)
            check(f"Ch6-Ex{label} a_{k_val}", sp.simplify(an - exp_an(k_val)) == 0, f"got {an}, exp {exp_an(k_val)}")
            check(f"Ch6-Ex{label} b_{k_val}", sp.simplify(bn - exp_bn(k_val)) == 0, f"got {bn}, exp {exp_bn(k_val)}")

    pi = sp.pi
    check_fourier_full("5(i)", sp.Integer(1), pi, 1, lambda k: 0, lambda k: 0)
    check_fourier_full("5(ii)", xs, pi, 0, lambda k: 0, lambda k: 2 * (-1) ** (k + 1) / k)
    check_fourier_full("5(iii)", pi - xs, pi, pi, lambda k: 0, lambda k: 2 * (-1) ** k / k)
    check_fourier_full("5(iv)", sp.Abs(xs), pi, pi / 2,
                       lambda k: 2 * ((-1) ** k - 1) / (pi * k**2), lambda k: 0,
                       pieces=[(-xs, -pi, 0), (xs, 0, pi)])
    check_fourier_full("5(v)", xs**2, pi, pi**2 / 3,
                       lambda k: 4 * (-1) ** k / k**2, lambda k: 0)
    # 5(vi): cos(x) on [0, pi] (L = pi/2, shifted to [0, pi])
    check_fourier_full("5(vi) pi-periodic", sp.cos(xs), pi / 2, 0,
                       lambda k: 0, lambda k: 8 * k / (pi * (4 * k**2 - 1)),
                       pieces=[(sp.cos(xs), 0, pi)])
    # 5(vii): 0 on [-pi, 0), pi on [0, pi]
    check_fourier_full("5(vii)", None, pi, pi / 2,
                       lambda k: 0, lambda k: (1 - (-1) ** k) / k,
                       pieces=[(sp.Integer(0), -pi, 0), (pi, 0, pi)])
    # 5(viii): -pi/2 on [-pi, 0), pi/2 on [0, pi]
    check_fourier_full("5(viii)", None, pi, 0,
                       lambda k: 0, lambda k: (1 - (-1) ** k) / k,
                       pieces=[(-pi / 2, -pi, 0), (pi / 2, 0, pi)])
    # 5(ix): full pi-periodic on [0, pi] (L = pi/2)
    check_fourier_full("5(ix) pi-periodic", None, pi / 2, sp.Rational(3, 2),
                       lambda k: 0, lambda k: -2 / (pi * k) if k % 2 == 1 else 0,
                       pieces=[(sp.Integer(1), 0, pi / 2), (sp.Integer(2), pi / 2, pi)])
    # 5(ix): half-range cosine and sine on [0, pi] (L = pi)
    for k_val in range(1, 5):
        an_hr = sp.simplify((2 / pi) * (sp.integrate(1 * sp.cos(k_val * xs), (xs, 0, pi / 2))
                                       + sp.integrate(2 * sp.cos(k_val * xs), (xs, pi / 2, pi))))
        bn_hr = sp.simplify((2 / pi) * (sp.integrate(1 * sp.sin(k_val * xs), (xs, 0, pi / 2))
                                       + sp.integrate(2 * sp.sin(k_val * xs), (xs, pi / 2, pi))))
        check(f"Ch6-Ex5(ix) HR cos a_{k_val}", sp.simplify(an_hr - (-2 * sp.sin(k_val * pi / 2) / (k_val * pi))) == 0)
        check(f"Ch6-Ex5(ix) HR sin b_{k_val}",
              sp.simplify(bn_hr - (2 * (1 + sp.cos(k_val * pi / 2) - 2 * (-1) ** k_val) / (k_val * pi))) == 0)

    # Ex 6: 8 cos^3(3x) = 6 cos(3x) + 2 cos(9x)
    check("Ch6-Ex6 trig identity", sp.trigsimp(8 * sp.cos(3 * xs) ** 3 - (6 * sp.cos(3 * xs) + 2 * sp.cos(9 * xs))) == 0)

    # Ex 7: Orthogonality for m, n in 0..3
    for mv in range(4):
        for nv in range(4):
            si = sp.simplify(sp.integrate(sp.sin(mv * pi * xs / L) * sp.sin(nv * pi * xs / L), (xs, -L, L)))
            ci = sp.simplify(sp.integrate(sp.cos(mv * pi * xs / L) * sp.cos(nv * pi * xs / L), (xs, -L, L)))
            exp_s = L if (mv == nv and mv > 0) else 0
            exp_c = 2 * L if (mv == 0 and nv == 0) else (L if mv == nv else 0)
            check(f"Ch6-Ex7 sin({mv},{nv})", sp.simplify(si - exp_s) == 0, str(si))
            check(f"Ch6-Ex7 cos({mv},{nv})", sp.simplify(ci - exp_c) == 0, str(ci))

    # Ex 8 (i)-(iii): Fourier coefficients on [-L, L]
    check_fourier_full("8(i)", xs**2, L, L**2 / 3,
                       lambda k: 4 * L**2 * (-1) ** k / (k**2 * pi**2), lambda k: 0)
    check_fourier_full("8(ii)", sp.exp(xs), L, sp.sinh(L) / L,
                       lambda k: 2 * L * (-1) ** k * sp.sinh(L) / (L**2 + k**2 * pi**2),
                       lambda k: -2 * k * pi * (-1) ** k * sp.sinh(L) / (L**2 + k**2 * pi**2))
    check_fourier_full("8(iii)", None, L, 1 + L / 4,
                       lambda k: L * ((-1) ** k - 1) / (k**2 * pi**2),
                       lambda k: (-1) ** (k + 1) * L / (k * pi),
                       pieces=[(sp.Integer(1), -L, 0), (xs + 1, 0, L)])


if __name__ == "__main__":
    verify_ch5()
    verify_ch6()
    if failures:
        print(f"\nFAILED: {len(failures)} of {checks} checks")
        sys.exit(1)
    print(f"ALL {checks} SYMPY CHECKS PASSED (Ch5 Ex 1-10 & Ch6 Ex 1-8)")
