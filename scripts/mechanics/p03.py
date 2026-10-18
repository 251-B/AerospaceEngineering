"""P03: bead on a smooth parabolic wire y = x^2/(2p) spinning about its vertical axis y at constant rate Omega (bank item P03).

S0 = {O; i0, j0, k0} inertial (j0 vertical up), S1 = {O; i1, j1, k1} turns with the wire, omega_10 = Omega j0, theta = Omega t.
Independent routes: absolute position in S0 differentiated directly, Lagrange equation in S0 (no inertia forces), the
reaction as m a - W projected on the rotating basis.
"""
import sympy as sp


def _vec(chk):
    def vchk(name, left, right=None):
        left = sp.Matrix(left)
        right = sp.zeros(*left.shape) if right is None else sp.Matrix(right)
        d = (left - right).applyfunc(lambda e: sp.simplify(sp.trigsimp(e)))
        ok = all(e == 0 for e in d)
        return chk.true(name, ok, "" if ok else f"residual {list(d)}")
    return vchk


def verify(chk):
    vchk = _vec(chk)
    t = sp.symbols("t", real=True)
    m, p, g, Om, x0 = sp.symbols("m p g Omega x0", positive=True)
    s = sp.symbols("s", positive=True)                   # generic abscissa x
    x = sp.Function("x")(t)
    xd, xdd = x.diff(t), x.diff(t, 2)
    th = Om * t

    # change of basis [0R1] (columns: i1, j1, k1 in B0), rotation about j0
    R01 = sp.Matrix([[sp.cos(th), 0, sp.sin(th)], [0, 1, 0], [-sp.sin(th), 0, sp.cos(th)]])
    chk("det [0R1] = 1", R01.det(), 1)
    vchk("[0R1][0R1]^T = I", R01 * R01.T, sp.eye(3))
    i1, j1, k1 = R01[:, 0], R01[:, 1], R01[:, 2]
    W_ = sp.Matrix([0, Om, 0])
    vchk("Poisson: d i1/dt = omega x i1", i1.diff(t), W_.cross(i1))
    vchk("Poisson: d k1/dt = omega x k1", k1.diff(t), W_.cross(k1))

    # absolute position and acceleration in S0
    rel = sp.Matrix([x, x**2 / (2 * p), 0])            # components in B1
    pos = R01 * rel
    a0 = pos.diff(t, 2)
    a1 = R01.T * a0                                     # absolute acceleration in B1 components
    a_rel = sp.Matrix([xdd, (xdd * x + xd**2) / p, 0])
    vchk("a_rel = x'' (1, x/p, 0) + x'^2 (0, 1/p, 0)", rel.diff(t, 2), a_rel)
    # Coriolis theorem: a0 = a_rel + omega x (omega x r) + 2 omega x v_rel (alpha = 0, O fixed)
    v_rel = rel.diff(t)
    vchk("a0 = a_rel + w x (w x r) + 2 w x v_rel (in B1)", a1, a_rel + W_.cross(W_.cross(rel)) + 2 * W_.cross(v_rel))
    vchk("centrifugal force = m Omega^2 x i1", -m * W_.cross(W_.cross(rel)), sp.Matrix([m * Om**2 * x, 0, 0]))
    vchk("Coriolis force = 2 m Omega x' k1", -2 * m * W_.cross(v_rel), sp.Matrix([0, 0, 2 * m * Om * xd]))

    # Lagrange in S0
    v0 = pos.diff(t)
    L = m * v0.dot(v0) / 2 - m * g * pos[1]
    eq = sp.diff(L.diff(xd), t) - L.diff(x)
    xdd_L = sp.solve(sp.Eq(eq, 0), xdd)[0]
    chk("EOM: (1 + x^2/p^2) x'' + (x/p^2) x'^2 = x (Omega^2 - g/p)", xdd_L,
        (x * (Om**2 - g / p) - x * xd**2 / p**2) / (1 + x**2 / p**2))

    # reaction = m a0 - W in B1 components
    Wt = sp.Matrix([0, -m * g, 0])
    Rb1 = sp.simplify((m * a1 - Wt).subs(xdd, xdd_L))
    tang = sp.Matrix([1, x / p, 0])
    chk("reaction has no component along the wire", Rb1.dot(tang))
    chk("out-of-plane reaction N_z = -2 m Omega x'", Rb1[2], -2 * m * Om * xd)
    q = sp.sqrt(1 + x**2 / p**2)
    nin = sp.Matrix([-x / p, 1, 0]) / q
    chk("in-plane normal reaction N_n = m (x'^2/p + Omega^2 x^2/p + g)/q", Rb1.dot(nin),
        m * (xd**2 / p + Om**2 * x**2 / p + g) / q)

    chk("|v|^2 = q^2 x'^2 + Omega^2 x^2", v0.dot(v0), (1 + x**2 / p**2) * xd**2 + Om**2 * x**2)
    vchk("v = v_rel - Omega x k1 (in B1)", R01.T * v0, v_rel + sp.Matrix([0, 0, -Om * x]))
    chk("power of the reaction in S0 = 2 m Omega^2 x x'", (R01 * Rb1).dot(v0), 2 * m * Om**2 * x * xd)
    chk.true("p -> infinity: EOM -> x'' = Omega^2 x (rotating straight rod)",
             sp.simplify(sp.limit(xdd_L, p, sp.oo) - Om**2 * x) == 0)

    # Jacobi integral in S1
    J = (1 + x**2 / p**2) * xd**2 / 2 + x**2 * (g / p - Om**2) / 2
    chk("dJ/dt = 0 on the motion", sp.diff(J, t).subs(xdd, xdd_L))
    chk("J = kinetic energy in S1 + g y - Omega^2 x^2/2 (per unit mass)", J,
        v_rel.dot(v_rel) / 2 + g * x**2 / (2 * p) - Om**2 * x**2 / 2)

    # equilibrium x = 0 and its stability
    Veff = s**2 * (g / p - Om**2) / 2
    chk("x = 0 is an equilibrium for every Omega", sp.diff(Veff, s).subs(s, 0))
    chk("V_eff''(0) = g/p - Omega^2", sp.diff(Veff, s, 2), g / p - Om**2)
    lin = sp.diff(xdd_L.subs(xd, 0).subs(x, s), s).subs(s, 0)
    chk("linearised: x'' = (Omega^2 - g/p) x", lin, Om**2 - g / p)
    # critical rate: every point is an equilibrium and the speed along the wire is constant
    xdd_c = xdd_L.subs(Om, sp.sqrt(g / p))
    chk("Omega^2 = g/p: x'' = 0 when x' = 0, at any x", xdd_c.subs(xd, 0))
    chk("Omega^2 = g/p: (1 + x^2/p^2) x'^2 is constant (uniform speed along the wire)",
        sp.diff((1 + x**2 / p**2) * xd**2, t).subs(xdd, xdd_c))
    chk("speed along the wire = sqrt(1 + x^2/p^2) |x'|", v_rel.dot(v_rel), (1 + x**2 / p**2) * xd**2)

    # Omega^2 = 2 g/p, release from rest at x0
    Om2 = sp.sqrt(2 * g / p)
    xd2 = (g / p) * (s**2 - x0**2) / (1 + s**2 / p**2)
    chk("x'^2(x) from the Jacobi integral, J(x0, 0) = J(x, x')",
        (J.subs(Om, Om2).subs(xd, sp.sqrt(xd2)).subs(x, s)) - J.subs(Om, Om2).subs(xd, 0).subs(x, x0))
    # it satisfies the EOM: d(x'^2)/dx = 2 x''
    chk("d(x'^2)/dx = 2 x'' (consistent with the EOM)", sp.diff(xd2, s),
        2 * xdd_L.subs(Om, Om2).subs(xd, sp.sqrt(xd2)).subs(x, s))
    acc0 = xdd_L.subs(Om, Om2).subs(xd, 0).subs(x, x0)
    chk("x''(x0) = (g/p) x0/(1 + x0^2/p^2) > 0 (moves outwards)", acc0, (g / p) * x0 / (1 + x0**2 / p**2))
    chk.true("x''(x0) > 0", acc0.is_positive)
    Nz = -2 * m * Om2 * sp.sqrt(xd2)
    chk("N_z(x) = -(2 sqrt2 m g/p) sqrt((x^2 - x0^2)/(1 + x^2/p^2))", Nz,
        -(2 * sp.sqrt(2) * m * g / p) * sp.sqrt((s**2 - x0**2) / (1 + s**2 / p**2)))
    chk.true("x'^2 -> g p for x -> infinity", sp.limit(xd2, s, sp.oo) == g * p)
    chk.true("|N_z| -> 2 sqrt2 m g for x -> infinity", sp.limit(-Nz, s, sp.oo) == 2 * sp.sqrt(2) * m * g)
    sub = {x0: p / 2}
    chk("x0 = p/2, at x = p: x'^2 = 3 g p/8", xd2.subs(sub).subs(s, p), 3 * g * p / 8)
    chk("x0 = p/2, at x = p: N_z = -sqrt3 m g", Nz.subs(sub).subs(s, p), -sp.sqrt(3) * m * g)
    Nn_p = (m * (xd**2 / p + Om**2 * x**2 / p + g) / q).subs(Om, Om2).subs(xd, sp.sqrt(xd2)).subs(x, s)
    chk("x0 = p/2, at x = p: N_n = (27/8) m g/sqrt2", Nn_p.subs(sub).subs(s, p), 27 * m * g / (8 * sp.sqrt(2)))
    chk.value("27/(8 sqrt2) = 2.386", 27 / (8 * sp.sqrt(2)), 2.38649, tol=1e-5)
    chk.value("sqrt3 = 1.732", sp.sqrt(3), 1.73205, tol=1e-5)
    chk("x0 = p/2, at x = p: speed along the wire^2 = 3 g p/4", ((1 + s**2 / p**2) * xd2).subs(sub).subs(s, p), 3 * g * p / 4)
    # the in-plane reaction is always positive
    w_, X_ = sp.symbols("w X", real=True)
    chk.true("N_n > 0 for every state (sum of positive terms)",
             (m * (w_**2 / p + Om**2 * X_**2 / p + g) / sp.sqrt(1 + X_**2 / p**2)).is_positive)
    # Omega < sqrt(g/p): frequency of the small oscillations
    chk("small-oscillation frequency omega^2 = g/p - Omega^2", -lin, g / p - Om**2)
