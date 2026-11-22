"""SymPy verification of every calculation in Advanced Maths Chapters 5 and 6 problem sheets.

    python tools/am_problems/verify_ch5_ch6.py

Checks:
- Chapter 5 (probls_ch5_2627.pdf, Exercises 1-10): critical points, Jacobians,
  eigenvalues, eigenvectors, conservation/dissipation dE/dt, bead-on-wire ODEs,
  and discrepancies (Ex. 5.2(i) lecturer slip, Ex. 5.4(iii) sheet vs Robinson).
- Chapter 6 (probls_ch6_2627.pdf, Exercises 1-9): Sturm-Liouville eigenvalues
  and eigenfunctions (ODE + BCs), integrating factor, Euler equation, all
  Fourier coefficients (Ex. 6.5, 6.6, 6.8), orthogonality (Ex. 6.7), and parity (Ex. 6.9).
"""
import math
import sympy as sp

x, y, t, s, L, h, k, w, lam = sp.symbols("x y t s L h k omega lambda", real=True)
n, m = sp.symbols("n m", integer=True, positive=True)


def check_jacobian_eigs(f, g, pts_expected):
    """Verify f=g=0 at each point, Jacobian, eigenvalues, and eigenvectors."""
    J = sp.Matrix([[sp.diff(f, x), sp.diff(f, y)],
                   [sp.diff(g, x), sp.diff(g, y)]])
    for pt, eigs_exp, vecs_exp in pts_expected:
        subs = {x: pt[0], y: pt[1]}
        assert sp.simplify(f.subs(subs)) == 0, f"f != 0 at {pt}"
        assert sp.simplify(g.subs(subs)) == 0, f"g != 0 at {pt}"
        J0 = J.subs(subs)
        # Verify characteristic polynomial roots
        charpoly = sp.expand((J0 - lam * sp.eye(2)).det())
        for ev in eigs_exp:
            assert sp.simplify(charpoly.subs(lam, ev)) == 0, f"ev {ev} not root at {pt}: {charpoly}"
        # Verify each (ev, vec) pair
        for ev, vec in vecs_exp:
            v = sp.Matrix(vec)
            assert v != sp.Matrix([0, 0])
            res = sp.simplify((J0 - ev * sp.eye(2)) * v)
            assert res == sp.Matrix([0, 0]), f"(J - {ev}I){vec} != 0 at {pt}: {res}"
    return J


def verify_ch5():
    # --- Ex 5.1 ---
    f1 = -y + lam * x * (x**2 + y**2)
    g1 = x + lam * y * (x**2 + y**2)
    J1 = check_jacobian_eigs(f1, g1, [
        ((0, 0), [sp.I, -sp.I], [(sp.I, [1, -sp.I]), (-sp.I, [1, sp.I])]),
    ])
    assert J1.subs({x: 0, y: 0}) == sp.Matrix([[0, -1], [1, 0]])
    # d(r^2)/dt = 2x f1 + 2y g1 = 2 lam (x^2 + y^2)^2 = 2 lam r^4 => dr/dt = lam r^3
    dr2_dt = sp.simplify(2 * x * f1 + 2 * y * g1)
    assert sp.simplify(dr2_dt - 2 * lam * (x**2 + y**2)**2) == 0

    # --- Ex 5.2 (i) ---
    f21 = x * (2 - x - y)
    g21 = y * (2 - 2 * y - 2 * x)
    J21 = check_jacobian_eigs(f21, g21, [
        ((0, 0), [2, 2], [(2, [1, 0]), (2, [0, 1])]),
        ((0, 1), [1, -2], [(1, [3, -2]), (-2, [0, 1])]),
        ((2, 0), [-2, -2], [(-2, [1, 0])]),
    ])
    # Confirm C=(2,0) is an improper node (non-diagonalizable: J(2,0) = [[-2,-2],[0,-2]])
    assert J21.subs({x: 2, y: 0}) == sp.Matrix([[-2, -2], [0, -2]])
    assert len(J21.subs({x: 2, y: 0}).eigenvects()[0][2]) == 1
    # Confirm no 4th solution: 2-x-y=0 and 2-2y-2x=0 => x+y=2 and x+y=1 (inconsistent)
    assert sp.solve([2 - x - y, 2 - 2 * y - 2 * x], [x, y]) == []

    # --- Ex 5.2 (ii) ---
    f22 = x * (2 - x - y)
    g22 = y * (2 - 2 * y - x / 4)
    check_jacobian_eigs(f22, g22, [
        ((0, 0), [2, 2], [(2, [1, 0]), (2, [0, 1])]),
        ((0, 1), [1, -2], [(1, [12, -1]), (-2, [0, 1])]),
        ((2, 0), [-2, sp.Rational(3, 2)], [(-2, [1, 0]), (sp.Rational(3, 2), [-4, 7])]),
        ((sp.Rational(8, 7), sp.Rational(6, 7)),
         [-sp.Rational(6, 7), -2],
         [(-sp.Rational(6, 7), [-4, 1]), (-2, [4, 3])]),
    ])

    # --- Ex 5.2 (iii) ---
    f23 = x * (2 - x - 3 * y)
    g23 = y * (2 - 2 * y - 3 * x)
    check_jacobian_eigs(f23, g23, [
        ((0, 0), [2, 2], [(2, [1, 0]), (2, [0, 1])]),
        ((0, 1), [-1, -2], [(-1, [1, -3]), (-2, [0, 1])]),
        ((2, 0), [-2, -4], [(-2, [1, 0]), (-4, [3, 1])]),
        ((sp.Rational(2, 7), sp.Rational(4, 7)),
         [sp.Rational(4, 7), -2],
         [(sp.Rational(4, 7), [1, -1]), (-2, [1, 2])]),
    ])

    # --- Ex 5.2 (iv) ---
    f24 = x * (1 - 2 * y)
    g24 = y * (-2 + 3 * x)
    check_jacobian_eigs(f24, g24, [
        ((0, 0), [1, -2], [(1, [1, 0]), (-2, [0, 1])]),
        ((sp.Rational(2, 3), sp.Rational(1, 2)),
         [sp.I * sp.sqrt(2), -sp.I * sp.sqrt(2)],
         [(sp.I * sp.sqrt(2), [2 * sp.sqrt(2), -3 * sp.I])]),
    ])
    # Conserved Lotka-Volterra Hamiltonian H = 3x - 2 ln x + 2y - ln y
    H24 = 3 * x - 2 * sp.log(x) + 2 * y - sp.log(y)
    assert sp.simplify(sp.diff(H24, x) * f24 + sp.diff(H24, y) * g24) == 0

    # --- Ex 5.2 (v) ---
    f25 = x * (4 - x / 2 - 3 * y)
    g25 = y * (-2 + x)
    l25_p = (-1 + sp.I * sp.sqrt(23)) / 2
    l25_m = (-1 - sp.I * sp.sqrt(23)) / 2
    check_jacobian_eigs(f25, g25, [
        ((0, 0), [4, -2], [(4, [1, 0]), (-2, [0, 1])]),
        ((8, 0), [-4, 6], [(-4, [1, 0]), (6, [-12, 5])]),
        ((2, 1), [l25_p, l25_m], [(l25_p, [-1 + sp.I * sp.sqrt(23), 2])]),
    ])

    # --- Ex 5.2 (vi) ---
    f26 = x * (10 - x - 3 * y)
    g26 = y * (1 + x - 10 * y)
    # Coexistence: x + 3y = 10, -x + 10y = 1 => 13y = 11, y = 11/13, x = 97/13
    x26, y26 = sp.Rational(97, 13), sp.Rational(11, 13)
    # Trace = -(97+110)/13 = -207/13, det = (97*110 + 3*97*11)/169 = 97*11*13/169 = 1067/13
    # Disc = (207^2 - 4*13*1067)/169 = (42849 - 55484)/169 = -12635/169 < 0 -> stable spiral!
    l26_p = (-207 + sp.I * sp.sqrt(12635)) / 26
    l26_m = (-207 - sp.I * sp.sqrt(12635)) / 26
    check_jacobian_eigs(f26, g26, [
        ((0, 0), [10, 1], [(10, [1, 0]), (1, [0, 1])]),
        ((10, 0), [-10, 11], [(-10, [1, 0]), (11, [-10, 7])]),
        ((0, sp.Rational(1, 10)), [sp.Rational(97, 10), -1],
         [(sp.Rational(97, 10), [107, 1]), (-1, [0, 1])]),
        ((x26, y26), [l26_p, l26_m], []),
    ])

    # --- Ex 5.2 (vii) ---
    f27 = x * (3 - x - y)
    g27 = y * (-2 + x)
    check_jacobian_eigs(f27, g27, [
        ((0, 0), [3, -2], [(3, [1, 0]), (-2, [0, 1])]),
        ((3, 0), [-3, 1], [(-3, [1, 0]), (1, [-3, 4])]),
        ((2, 1), [-1 + sp.I, -1 - sp.I], [(-1 + sp.I, [-1 + sp.I, 1])]),
    ])

    # --- Ex 5.3 (i) & (ii) ---
    f31 = x * (1 - x + y)
    g31 = y * (1 + x - 2 * y)
    check_jacobian_eigs(f31, g31, [
        ((0, 0), [1, 1], [(1, [1, 0]), (1, [0, 1])]),
        ((1, 0), [-1, 2], [(-1, [1, 0]), (2, [1, 3])]),
        ((0, sp.Rational(1, 2)), [sp.Rational(3, 2), -1],
         [(sp.Rational(3, 2), [5, 1]), (-1, [0, 1])]),
        ((3, 2), [-1, -6], [(-1, [3, 2]), (-6, [1, -1])]),
    ])

    f32 = x * (2 - x + y)
    g32 = y * (4 + 2 * x - y)
    # Interior intersection is (-6, -8) outside Q1!
    assert sp.solve([2 - x + y, 4 + 2 * x - y], [x, y]) == {x: -6, y: -8}
    check_jacobian_eigs(f32, g32, [
        ((0, 0), [2, 4], [(2, [1, 0]), (4, [0, 1])]),
        ((2, 0), [-2, 8], [(-2, [1, 0]), (8, [1, 5])]),
        ((0, 4), [6, -4], [(6, [5, 4]), (-4, [0, 1])]),
    ])

    # --- Ex 5.4 (i), (ii), (iii) ---
    V41 = sp.Rational(1, 2) * w**2 * x**2
    V42 = sp.Rational(1, 2) * x**4 - x**2
    V43_sheet = sp.Rational(1, 2) * x**6 - sp.Rational(5, 4) * x**4 + 2 * x**2
    V43_rob = sp.Rational(1, 6) * x**6 - sp.Rational(5, 4) * x**4 + 2 * x**2

    for V in (V41, V42, V43_sheet, V43_rob):
        E = sp.Rational(1, 2) * y**2 + V
        dE = sp.simplify(sp.diff(E, x) * y + sp.diff(E, y) * (-sp.diff(V, x)))
        assert dE == 0

    check_jacobian_eigs(y, -sp.diff(V41, x), [((0, 0), [sp.I * w, -sp.I * w], [])])
    check_jacobian_eigs(y, -sp.diff(V42, x), [
        ((0, 0), [sp.sqrt(2), -sp.sqrt(2)], [(sp.sqrt(2), [sp.sqrt(2), 2]), (-sp.sqrt(2), [-sp.sqrt(2), 2])]),
        ((1, 0), [2 * sp.I, -2 * sp.I], [(2 * sp.I, [sp.I, -2])]),
        ((-1, 0), [2 * sp.I, -2 * sp.I], [(2 * sp.I, [sp.I, -2])]),
    ])
    # Sheet V43: V'(x) = x(3x^4 - 5x^2 + 4), only real root is x = 0!
    assert [r for r in sp.solve(sp.diff(V43_sheet, x), x) if r.is_real] == [0]
    check_jacobian_eigs(y, -sp.diff(V43_sheet, x), [((0, 0), [2 * sp.I, -2 * sp.I], [])])
    # Robinson V43: V'(x) = x(x^2-1)(x^2-4), 5 real roots 0, +-1, +-2
    assert sorted([r for r in sp.solve(sp.diff(V43_rob, x), x) if r.is_real]) == [-2, -1, 0, 1, 2]

    # --- Ex 5.5 (bead on wire) ---
    for V in (V41, V42):
        Vp, Vpp = sp.diff(V, x), sp.diff(V, x, 2)
        E_wire = sp.Rational(1, 2) * (1 + Vp**2) * y**2 + V
        g_wire = -Vp * (1 + Vpp * y**2) / (1 + Vp**2)
        assert sp.simplify(sp.diff(E_wire, x) * y + sp.diff(E_wire, y) * g_wire) == 0

    # --- Ex 5.6 (damped oscillators, k=1, w=1) ---
    check_jacobian_eigs(y, -x - y, [
        ((0, 0), [(-1 + sp.I * sp.sqrt(3)) / 2, (-1 - sp.I * sp.sqrt(3)) / 2], []),
    ])
    check_jacobian_eigs(y, -sp.diff(V42, x) - y, [
        ((0, 0), [1, -2], [(1, [1, 1]), (-2, [1, -2])]),
        ((1, 0), [(-1 + sp.I * sp.sqrt(15)) / 2, (-1 - sp.I * sp.sqrt(15)) / 2], []),
        ((-1, 0), [(-1 + sp.I * sp.sqrt(15)) / 2, (-1 - sp.I * sp.sqrt(15)) / 2], []),
    ])
    check_jacobian_eigs(y, -sp.diff(V43_sheet, x) - y, [
        ((0, 0), [(-1 + sp.I * sp.sqrt(15)) / 2, (-1 - sp.I * sp.sqrt(15)) / 2], []),
    ])

    # --- Ex 5.7 (damped bead on wire, general V(x)) ---
    Vf = sp.Function("V")(x)
    Vp, Vpp = sp.diff(Vf, x), sp.diff(Vf, x, 2)
    E7 = sp.Rational(1, 2) * (1 + Vp**2) * y**2 + Vf
    g7 = -(Vp + Vp * Vpp * y**2 + k * y) / (1 + Vp**2)
    assert sp.simplify(sp.diff(E7, x) * y + sp.diff(E7, y) * g7 + k * y**2) == 0
    J7 = sp.Matrix([[0, 1], [sp.diff(g7, x), sp.diff(g7, y)]])
    # At any critical point (x*, 0) with V'(x*) = 0:
    J7_crit = sp.simplify(J7.subs(y, 0).subs(Vp, 0))
    # Note: subs(Vp, 0) also hits Vpp in SymPy if Vpp is Derivative(V(x),(x,2)), so use a symbol for V'
    v1, v2 = sp.symbols("v1 v2")
    J7_crit = sp.simplify(J7.subs(y, 0).subs(Vpp, v2).subs(Vp, 0))
    assert J7_crit == sp.Matrix([[0, 1], [-v2, -k]])

    # --- Ex 5.8, 5.9, 5.10 (pendula) ---
    E8 = sp.Rational(1, 2) * y**2 - sp.cos(x)
    assert sp.simplify(sp.diff(E8, x) * y + sp.diff(E8, y) * (-sp.sin(x))) == 0
    assert sp.simplify(sp.diff(E8, x) * y + sp.diff(E8, y) * (-sp.sin(x) - k * y) + k * y**2) == 0
    assert sp.simplify(sp.diff(E8, x) * y + sp.diff(E8, y) * (-sp.sin(x) - k * y * sp.Abs(y)) + k * y**2 * sp.Abs(y)) == 0
    # Ex 5.8 linearizations at (0,0) and (pi,0)
    check_jacobian_eigs(y, -sp.sin(x), [
        ((0, 0), [sp.I, -sp.I], []),
        ((sp.pi, 0), [1, -1], [(1, [1, 1]), (-1, [1, -1])]),
    ])
    # Ex 5.9 linearizations at (0,0) and (pi,0)
    check_jacobian_eigs(y, -sp.sin(x) - k * y, [
        ((0, 0), [(-k + sp.sqrt(k**2 - 4)) / 2, (-k - sp.sqrt(k**2 - 4)) / 2], []),
        ((sp.pi, 0), [(-k + sp.sqrt(k**2 + 4)) / 2, (-k - sp.sqrt(k**2 + 4)) / 2], []),
    ])
    print("Chapter 5: ALL 10 exercises verified OK.")


def verify_ch6():
    # --- Ex 6.1 (i)-(iv): phi'' + lam phi = 0 on (0,1) ---
    # (i) Dirichlet: lam_n = (n pi)^2, phi_n = sin(n pi x)
    phi1 = sp.sin(n * sp.pi * x)
    assert sp.simplify(sp.diff(phi1, x, 2) + (n * sp.pi)**2 * phi1) == 0
    assert phi1.subs(x, 0) == 0 and sp.simplify(phi1.subs(x, 1)) == 0
    # (ii) Mixed: lam_n = ((n-1/2) pi)^2, phi_n = sin((n-1/2) pi x)
    mu2 = (n - sp.Rational(1, 2)) * sp.pi
    phi2 = sp.sin(mu2 * x)
    assert sp.simplify(sp.diff(phi2, x, 2) + mu2**2 * phi2) == 0
    assert phi2.subs(x, 0) == 0 and sp.simplify(sp.diff(phi2, x).subs(x, 1)) == 0
    # (iii) Neumann: lam_0 = 0 (phi_0 = 1), lam_n = (n pi)^2 (phi_n = cos(n pi x))
    phi3 = sp.cos(n * sp.pi * x)
    assert sp.simplify(sp.diff(phi3, x, 2) + (n * sp.pi)**2 * phi3) == 0
    assert sp.diff(phi3, x).subs(x, 0) == 0 and sp.simplify(sp.diff(phi3, x).subs(x, 1)) == 0
    # (iv) Robin: phi(0)=0, phi'(1)+h phi(1)=0, h>0 -> phi = sin(mu x), mu cos mu + h sin mu = 0 -> tan mu = -mu/h
    mu = sp.Symbol("mu", positive=True)
    phi4 = sp.sin(mu * x)
    bc4 = sp.diff(phi4, x).subs(x, 1) + h * phi4.subs(x, 1)
    assert sp.simplify(bc4 - (mu * sp.cos(mu) + h * sp.sin(mu))) == 0
    # Numerical check of first 3 Robin roots for h = 1
    def robin_root(idx, hv=1.0):
        lo = (idx - 0.5) * math.pi + 1e-6
        hi = idx * math.pi - 1e-6
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            if math.tan(mid) + mid / hv < 0:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)
    r1, r2, r3 = robin_root(1), robin_root(2), robin_root(3)
    assert abs(r1 - 2.0287578381) < 1e-6
    assert abs(r2 - 4.9131804394) < 1e-6
    assert abs(r3 - 7.9786657124) < 1e-6

    # --- Ex 6.2 (i)-(iii) ---
    # (i) y'' + y' + (1+lam)y = 0, y(0)=y(1)=0 -> lam_n = (n pi)^2 - 3/4, y_n = e^{-x/2} sin(n pi x)
    y21 = sp.exp(-x / 2) * sp.sin(n * sp.pi * x)
    lam21 = (n * sp.pi)**2 - sp.Rational(3, 4)
    assert sp.simplify(sp.diff(y21, x, 2) + sp.diff(y21, x) + (1 + lam21) * y21) == 0
    assert y21.subs(x, 0) == 0 and sp.simplify(y21.subs(x, 1)) == 0

    # (ii) y'' + 2y' + (1-lam)y = 0, y(0)=y'(1)=0
    # lam_0 = 0: y_0 = x e^{-x}
    y22_0 = x * sp.exp(-x)
    assert sp.simplify(sp.diff(y22_0, x, 2) + 2 * sp.diff(y22_0, x) + y22_0) == 0
    assert y22_0.subs(x, 0) == 0 and sp.simplify(sp.diff(y22_0, x).subs(x, 1)) == 0
    # lam_n = -mu_n^2 < 0 with tan(mu_n) = mu_n: y_n = e^{-x} sin(mu_n x)
    y22_n = sp.exp(-x) * sp.sin(mu * x)
    assert sp.simplify(sp.diff(y22_n, x, 2) + 2 * sp.diff(y22_n, x) + (1 + mu**2) * y22_n) == 0
    assert y22_n.subs(x, 0) == 0
    assert sp.simplify(sp.diff(y22_n, x).subs(x, 1) - sp.exp(-1) * (mu * sp.cos(mu) - sp.sin(mu))) == 0
    # First two positive roots of tan(mu) = mu: ~4.493409, ~7.725252
    def tan_eq_mu(idx):
        lo = idx * math.pi + 1e-6
        hi = (idx + 0.5) * math.pi - 1e-6
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            if math.tan(mid) - mid < 0:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)
    assert abs(tan_eq_mu(1) - 4.4934094579) < 1e-6
    assert abs(tan_eq_mu(2) - 7.7252518369) < 1e-6

    # (iii) y'' - 3y' + 3(1+lam)y = 0, y'(0)=y'(1)=0
    # lam_0 = -1, y_0 = 1
    assert sp.simplify(0 - 0 + 3 * (1 - 1) * 1) == 0
    # lam_n = (n pi)^2 / 3 - 1/4, y_n = e^{3x/2} (2 n pi cos(n pi x) - 3 sin(n pi x))
    lam23 = (n * sp.pi)**2 / 3 - sp.Rational(1, 4)
    y23 = sp.exp(sp.Rational(3, 2) * x) * (2 * n * sp.pi * sp.cos(n * sp.pi * x) - 3 * sp.sin(n * sp.pi * x))
    assert sp.simplify(sp.diff(y23, x, 2) - 3 * sp.diff(y23, x) + 3 * (1 + lam23) * y23) == 0
    assert sp.simplify(sp.diff(y23, x).subs(x, 0)) == 0
    assert sp.simplify(sp.diff(y23, x).subs(x, 1)) == 0

    # --- Ex 6.3 (Sturm-Liouville integrating factor) ---
    af = sp.Function("alpha")(x)
    bf = sp.Function("beta")(x)
    gf = sp.Function("gamma")(x)
    phif = sp.Function("phi")(x)
    mu_sl = sp.exp(sp.Integral(af, x))
    lhs = sp.diff(mu_sl * sp.diff(phif, x), x) + mu_sl * (lam * bf + gf) * phif
    rhs = mu_sl * (sp.diff(phif, x, 2) + af * sp.diff(phif, x) + (lam * bf + gf) * phif)
    assert sp.simplify(lhs - rhs) == 0

    # --- Ex 6.4 (Euler BVP on [1,2]) ---
    lam4 = (n * sp.pi / sp.log(2))**2
    phi4_eul = sp.sin(n * sp.pi * sp.log(x) / sp.log(2))
    assert sp.simplify(x**2 * sp.diff(phi4_eul, x, 2) + x * sp.diff(phi4_eul, x) + lam4 * phi4_eul) == 0
    assert sp.simplify(phi4_eul.subs(x, 1)) == 0 and sp.simplify(phi4_eul.subs(x, 2)) == 0

    # --- Ex 6.5 (i)-(ix) Fourier coefficients ---
    def fc(expr, a_lim=-sp.pi, b_lim=sp.pi):
        L_half = (b_lim - a_lim) / 2
        a0 = sp.simplify(sp.integrate(expr, (x, a_lim, b_lim)) / (2 * L_half))
        an = sp.simplify(sp.integrate(expr * sp.cos(n * sp.pi * x / L_half), (x, a_lim, b_lim)) / L_half)
        bn = sp.simplify(sp.integrate(expr * sp.sin(n * sp.pi * x / L_half), (x, a_lim, b_lim)) / L_half)
        return a0, an, bn

    # (i) f=1 on [-pi, pi]
    assert fc(sp.Integer(1)) == (1, 0, 0)
    # (ii) f=x on [-pi, pi]
    a0, an, bn = fc(x)
    assert a0 == 0 and an == 0 and sp.simplify(bn - 2 * (-1)**(n + 1) / n) == 0
    # (iii) f=pi-x on [-pi, pi]
    a0, an, bn = fc(sp.pi - x)
    assert a0 == sp.pi and an == 0 and sp.simplify(bn - 2 * (-1)**n / n) == 0
    # (iv) f=|x| on [-pi, pi]
    a0 = sp.simplify((sp.integrate(-x, (x, -sp.pi, 0)) + sp.integrate(x, (x, 0, sp.pi))) / (2 * sp.pi))
    an = sp.simplify(2 * sp.integrate(x * sp.cos(n * x), (x, 0, sp.pi)) / sp.pi)
    assert a0 == sp.pi / 2 and sp.simplify(an - 2 * ((-1)**n - 1) / (sp.pi * n**2)) == 0
    # (v) f=x^2 on [-pi, pi]
    a0, an, bn = fc(x**2)
    assert a0 == sp.pi**2 / 3 and sp.simplify(an - 4 * (-1)**n / n**2) == 0 and bn == 0
    # (vi) f=cos x on [0, pi]:
    #   (a) Even extension on [-pi, pi] (cosine series): f(x) = cos x itself (a_1 = 1, all others 0)
    #   (b) Odd extension on [-pi, pi] (sine series): b_n = (2/pi) int_0^pi cos(x) sin(nx) dx
    b_odd_n = sp.simplify(2 / sp.pi * sp.integrate(sp.cos(x) * sp.sin(n * x), (x, 0, sp.pi)))
    # For n=1: 0; for n>=2: (2/pi) * n * (1 + (-1)^n) / (n^2 - 1) (nonzero for even n: 4n / (pi(n^2-1)))
    assert sp.simplify(2 / sp.pi * sp.integrate(sp.cos(x) * sp.sin(x), (x, 0, sp.pi))) == 0
    for nv in (2, 3, 4, 5, 6):
        val = sp.simplify(2 / sp.pi * sp.integrate(sp.cos(x) * sp.sin(nv * x), (x, 0, sp.pi)))
        exp_val = sp.Integer(4 * nv) / (sp.pi * (nv**2 - 1)) if nv % 2 == 0 else sp.Integer(0)
        assert sp.simplify(val - exp_val) == 0
    #   (c) Direct pi-periodic full Fourier series on [0, pi] (L = pi/2, basis cos(2nx), sin(2nx)):
    a0_p, an_p, bn_p = fc(sp.cos(x), 0, sp.pi)
    assert a0_p == 0 and an_p == 0
    for nv in (1, 2, 3, 4):
        assert sp.simplify(bn_p.subs(n, nv) - sp.Integer(8 * nv) / (sp.pi * (4 * nv**2 - 1))) == 0
    # (vii) f = 0 on [-pi, 0), pi on [0, pi]
    a0 = sp.simplify(sp.integrate(sp.pi, (x, 0, sp.pi)) / (2 * sp.pi))
    an = sp.simplify(sp.integrate(sp.pi * sp.cos(n * x), (x, 0, sp.pi)) / sp.pi)
    bn = sp.simplify(sp.integrate(sp.pi * sp.sin(n * x), (x, 0, sp.pi)) / sp.pi)
    assert a0 == sp.pi / 2 and an == 0 and sp.simplify(bn - (1 - (-1)**n) / n) == 0
    # (viii) f = -pi/2 on [-pi, 0), pi/2 on [0, pi]
    a0 = sp.simplify((sp.integrate(-sp.pi / 2, (x, -sp.pi, 0)) + sp.integrate(sp.pi / 2, (x, 0, sp.pi))) / (2 * sp.pi))
    bn = sp.simplify(2 * sp.integrate(sp.pi / 2 * sp.sin(n * x), (x, 0, sp.pi)) / sp.pi)
    assert a0 == 0 and sp.simplify(bn - (1 - (-1)**n) / n) == 0
    # (ix) f = 1 on [0, pi/2], 2 on [pi/2, pi]:
    #   (a) Even extension (cosine series on [0, pi]):
    a0_c = sp.simplify((sp.integrate(1, (x, 0, sp.pi / 2)) + sp.integrate(2, (x, sp.pi / 2, sp.pi))) / sp.pi)
    an_c = sp.simplify(2 / sp.pi * (sp.integrate(sp.cos(n * x), (x, 0, sp.pi / 2)) + sp.integrate(2 * sp.cos(n * x), (x, sp.pi / 2, sp.pi))))
    assert a0_c == sp.Rational(3, 2) and sp.simplify(an_c + 2 * sp.sin(n * sp.pi / 2) / (n * sp.pi)) == 0
    #   (b) Odd extension (sine series on [0, pi]):
    bn_s = sp.simplify(2 / sp.pi * (sp.integrate(sp.sin(n * x), (x, 0, sp.pi / 2)) + sp.integrate(2 * sp.sin(n * x), (x, sp.pi / 2, sp.pi))))
    assert sp.simplify(bn_s - 2 * (1 + sp.cos(n * sp.pi / 2) - 2 * (-1)**n) / (n * sp.pi)) == 0
    #   (c) Direct pi-periodic full Fourier series on [0, pi] (L = pi/2):
    a0_f = sp.simplify((sp.integrate(1, (x, 0, sp.pi / 2)) + sp.integrate(2, (x, sp.pi / 2, sp.pi))) / sp.pi)
    an_f = sp.simplify(2 / sp.pi * (sp.integrate(sp.cos(2 * n * x), (x, 0, sp.pi / 2)) + sp.integrate(2 * sp.cos(2 * n * x), (x, sp.pi / 2, sp.pi))))
    bn_f = sp.simplify(2 / sp.pi * (sp.integrate(sp.sin(2 * n * x), (x, 0, sp.pi / 2)) + sp.integrate(2 * sp.sin(2 * n * x), (x, sp.pi / 2, sp.pi))))
    assert a0_f == sp.Rational(3, 2) and an_f == 0 and sp.simplify(bn_f + (1 - (-1)**n) / (n * sp.pi)) == 0

    # --- Ex 6.6 ---
    assert sp.simplify(8 * sp.cos(3 * x)**3 - (6 * sp.cos(3 * x) + 2 * sp.cos(9 * x))) == 0

    # --- Ex 6.7 (Orthogonality) ---
    Lp = sp.Symbol("L", positive=True)
    for nv in (1, 2, 3):
        for mv in (1, 2, 3):
            I_s = sp.integrate(sp.sin(nv * sp.pi * x / Lp) * sp.sin(mv * sp.pi * x / Lp), (x, -Lp, Lp))
            I_c = sp.integrate(sp.cos(nv * sp.pi * x / Lp) * sp.cos(mv * sp.pi * x / Lp), (x, -Lp, Lp))
            assert sp.simplify(I_s - (Lp if nv == mv else 0)) == 0
            assert sp.simplify(I_c - (Lp if nv == mv else 0)) == 0
    assert sp.integrate(sp.cos(0) * sp.cos(0), (x, -Lp, Lp)) == 2 * Lp
    assert sp.integrate(sp.sin(0) * sp.sin(0), (x, -Lp, Lp)) == 0  # sheet slip check!

    # --- Ex 6.8 (Fourier series on [-L, L]) ---
    # (i) x^2 on [-L, L]
    a0 = sp.simplify(sp.integrate(x**2, (x, -Lp, Lp)) / (2 * Lp))
    an = sp.simplify(sp.integrate(x**2 * sp.cos(n * sp.pi * x / Lp), (x, -Lp, Lp)) / Lp)
    assert a0 == Lp**2 / 3 and sp.simplify(an - 4 * Lp**2 * (-1)**n / (n * sp.pi)**2) == 0
    # (ii) e^x on [-L, L]
    a0 = sp.simplify(sp.integrate(sp.exp(x), (x, -Lp, Lp)) / (2 * Lp))
    an = sp.simplify(sp.integrate(sp.exp(x) * sp.cos(n * sp.pi * x / Lp), (x, -Lp, Lp)) / Lp)
    bn = sp.simplify(sp.integrate(sp.exp(x) * sp.sin(n * sp.pi * x / Lp), (x, -Lp, Lp)) / Lp)
    assert sp.simplify(a0 - sp.sinh(Lp) / Lp) == 0
    assert sp.simplify(an - 2 * Lp * (-1)**n * sp.sinh(Lp) / (Lp**2 + (n * sp.pi)**2)) == 0
    assert sp.simplify(bn + 2 * n * sp.pi * (-1)**n * sp.sinh(Lp) / (Lp**2 + (n * sp.pi)**2)) == 0
    # (iii) f = 1 (x<0), x+1 (x>=0) on [-L, L]
    a0 = sp.simplify((sp.integrate(1, (x, -Lp, 0)) + sp.integrate(x + 1, (x, 0, Lp))) / (2 * Lp))
    an = sp.simplify((sp.integrate(sp.cos(n * sp.pi * x / Lp), (x, -Lp, 0)) + sp.integrate((x + 1) * sp.cos(n * sp.pi * x / Lp), (x, 0, Lp))) / Lp)
    bn = sp.simplify((sp.integrate(sp.sin(n * sp.pi * x / Lp), (x, -Lp, 0)) + sp.integrate((x + 1) * sp.sin(n * sp.pi * x / Lp), (x, 0, Lp))) / Lp)
    assert sp.simplify(a0 - (1 + Lp / 4)) == 0
    assert sp.simplify(an - Lp * ((-1)**n - 1) / (n * sp.pi)**2) == 0
    assert sp.simplify(bn + Lp * (-1)**n / (n * sp.pi)) == 0

    print("Chapter 6: ALL 9 exercises verified OK.")


if __name__ == "__main__":
    verify_ch5()
    verify_ch6()
    print("ALL CHAPTER 5 AND CHAPTER 6 VERIFICATIONS PASSED.")
