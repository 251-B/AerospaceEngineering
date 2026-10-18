"""P02: particle on the smooth inner surface of a paraboloid of revolution z = r^2/(2c) (bank item P02).

Axis vertical (z up), gravity -g k. Independent routes: Cartesian position differentiated directly, Lagrange equations
in (r, phi), the reaction obtained as m a - W and tested for being normal to the surface.
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
    m, c, g, r0, v0, H = sp.symbols("m c g r0 v0 H", positive=True)
    x = sp.symbols("x", positive=True)            # a generic radius
    r = sp.Function("r")(t)
    ph = sp.Function("phi")(t)
    rd, rdd, phd, phdd = r.diff(t), r.diff(t, 2), ph.diff(t), ph.diff(t, 2)
    q = sp.sqrt(1 + r**2 / c**2)

    er = sp.Matrix([sp.cos(ph), sp.sin(ph), 0])
    ep = sp.Matrix([-sp.sin(ph), sp.cos(ph), 0])
    k = sp.Matrix([0, 0, 1])
    # change of basis [e_r; e_phi; k] = R [i; j; k]
    qa = sp.symbols("qa", real=True)
    Rm = sp.Matrix([[sp.cos(qa), sp.sin(qa), 0], [-sp.sin(qa), sp.cos(qa), 0], [0, 0, 1]])
    chk("R rows are e_r, e_phi, k", sum(xx**2 for xx in (Rm - sp.Matrix.hstack(er, ep, k).T.subs(ph, qa))))
    chk("R R^T = I", sum(xx**2 for xx in (Rm * Rm.T - sp.eye(3))))
    chk("det R = +1", Rm.det(), 1)
    pos = r * er + r**2 / (2 * c) * k
    v, a = pos.diff(t), pos.diff(t, 2)
    vchk("v = r' e_r + r phi' e_phi + (r r'/c) k", v, rd * er + r * phd * ep + r * rd / c * k)
    vchk("a = (r''-r phi'^2) e_r + (2 r' phi' + r phi'') e_phi + ((r'^2 + r r'')/c) k", a,
         (rdd - r * phd**2) * er + (2 * rd * phd + r * phdd) * ep + (rd**2 + r * rdd) / c * k)

    # normal of the surface f = z - r^2/(2c): grad f = -(r/c) e_r + k
    nvec = (-(r / c) * er + k) / q
    chk("|n| = 1", nvec.dot(nvec), 1)
    chk("n is normal to the velocity (tangent plane)", nvec.dot(v))

    # Lagrange equations (independent of the Newton projection)
    L = m * v.dot(v) / 2 - m * g * pos[2]
    Er = sp.diff(L.diff(rd), t) - L.diff(r)
    Ep = sp.diff(L.diff(phd), t) - L.diff(ph)
    chk("phi equation: d/dt (m r^2 phi') = 0", Ep, sp.diff(m * r**2 * phd, t))
    rdd_L = sp.solve(sp.Eq(Er, 0), rdd)[0]
    rdd_note = (r * phd**2 - r * rd**2 / c**2 - g * r / c) / (1 + r**2 / c**2)
    chk("r equation: (1+r^2/c^2) r'' + r r'^2/c^2 - r phi'^2 + g r/c = 0", rdd_L, rdd_note)

    # reaction = m a - W must be along n, with N/q = m((r'^2 + r r'')/c + g)
    W = sp.Matrix([0, 0, -m * g])
    Rf = (m * a - W).subs({rdd: rdd_L, phdd: -2 * rd * phd / r})
    vchk("reaction parallel to the normal (cross product zero)", Rf.cross(nvec))
    Nmag = sp.simplify(Rf.dot(nvec))
    chk("N = q m ((r'^2 + r r'')/c + g)", Nmag, (q * m * ((rd**2 + r * rdd) / c + g)).subs(rdd, rdd_L))
    chk("e_r projection: m(r'' - r phi'^2) = -N r/(c q)", (m * (rdd - r * phd**2)).subs(rdd, rdd_L),
        -Nmag * r / (c * q))
    chk("moment of the forces about the z axis is zero (k.(r x F) = 0)", k.dot(pos.cross(Rf + W)))

    # with H = r^2 phi': equation for r alone and energy
    rdd_H = sp.simplify(rdd_note.subs(phd, H / r**2))
    E = (rd**2 * (1 + r**2 / c**2) + H**2 / r**2) / 2 + g * r**2 / (2 * c)
    chk("dE/dt = 0 on the motion (energy per unit mass)", sp.diff(E, t).subs(rdd, rdd_H))
    chk("energy = |v|^2/2 + g z with phi' = H/r^2", E, (v.dot(v) / 2 + g * pos[2]).subs(phd, H / r**2))

    # horizontal circular orbit: r' = 0, r'' = 0 -> phi'^2 = g/c whatever r0
    Om2 = sp.solve(sp.Eq(rdd_note.subs({rd: 0}).subs(r, r0), 0), phd**2)
    chk("circular orbit: phi'^2 = g/c (independent of r0)", Om2[0], g / c)
    Ncirc = (q * m * g).subs(r, r0)
    chk("circular orbit reaction N = m g sqrt(1 + r0^2/c^2)", Nmag.subs({rd: 0, phd: sp.sqrt(g / c)}).subs(r, r0), Ncirc)
    chk("orbital speed v = r0 sqrt(g/c)", sp.sqrt(v.dot(v).subs({rd: 0, phd: sp.sqrt(g / c)}).subs(r, r0)), r0 * sp.sqrt(g / c))

    # contrast: on a cone z = a r (same derivation) the circular rate depends on the radius, Omega^2 = g a / r0
    acone = sp.symbols("a", positive=True)
    pos_c = r * er + acone * r * k
    vc = pos_c.diff(t)
    Lc = m * vc.dot(vc) / 2 - m * g * pos_c[2]
    rdd_c = sp.solve(sp.Eq(sp.diff(Lc.diff(rd), t) - Lc.diff(r), 0), rdd)[0]
    Om2c = sp.solve(sp.Eq(rdd_c.subs(rd, 0).subs(r, r0), 0), phd**2)[0]
    chk("cone contrast: circular rate^2 = g a/r0 depends on r0", Om2c, g * acone / r0)
    chk("bowl near the vertex: V = (1/2)(m g/c) r^2, isotropic spring of stiffness m g/c", m * g * pos[2], (m * g / c) * r**2 / 2)

    # small radial oscillations about r0 with H = r0^2 sqrt(g/c)
    H0 = r0**2 * sp.sqrt(g / c)
    F = H0**2 / x**3 - g * x / c                    # right-hand side of (1 + r^2/c^2) r'' = F(r) at r' = 0
    chk("F(r0) = 0", F.subs(x, r0))
    chk("F'(r0) = -4 g/c", sp.diff(F, x).subs(x, r0), -4 * g / c)
    # linearise the full equation r'' = G(r, r') about (r0, 0): dG/dr' = 0 there, so omega^2 = -dG/dr
    G = sp.simplify(rdd_H.subs(H, H0))
    s1, s2 = sp.symbols("s1 s2")
    Gs = G.subs({rd: s2}).subs(r, s1)
    chk("dG/dr' = 0 at the circular orbit", sp.diff(Gs, s2).subs({s1: r0, s2: 0}))
    wr2 = sp.simplify(-sp.diff(Gs, s1).subs({s1: r0, s2: 0}))
    chk("omega_r^2 = 4 g c/(c^2 + r0^2)", wr2, 4 * g * c / (c**2 + r0**2))
    ratio = sp.sqrt(wr2 / (g / c))
    chk("omega_r/Omega0 = 2c/sqrt(c^2 + r0^2)", ratio, 2 * c / sp.sqrt(c**2 + r0**2))
    chk("ratio = sqrt2 for r0 = c", ratio.subs(r0, c), sp.sqrt(2))
    chk("ratio = 1 for r0 = sqrt3 c (orbit closes after one revolution)", ratio.subs(r0, sp.sqrt(3) * c), 1)
    chk.true("ratio -> 2 for r0 -> 0", sp.limit(ratio, r0, 0) == 2)

    # turning points: start at r0 with r' = 0 and horizontal speed v0 (H = r0 v0)
    u = sp.symbols("u", positive=True)               # u = r^2
    poly_u = sp.expand(g * u**2 / c - (v0**2 + g * r0**2 / c) * u + r0**2 * v0**2)
    chk("turning-point polynomial = (u - r0^2)(g u/c - v0^2)", poly_u, sp.expand((u - r0**2) * (g * u / c - v0**2)))
    Eturn = (r0**2 * v0**2 / x**2) / 2 + g * x**2 / (2 * c) - (v0**2 / 2 + g * r0**2 / (2 * c))
    chk("r = v0 sqrt(c/g) is a turning point", Eturn.subs(x, v0 * sp.sqrt(c / g)))

    # general reaction along any motion: N = m (2 E c^2 + H^2 + g c^3)/(c^2 + r^2)^(3/2), E = energy per unit mass
    Es = sp.symbols("E", positive=True)
    rd2g = (2 * Es - H**2 / x**2 - g * x**2 / c) / (1 + x**2 / c**2)
    rddg = (H**2 / x**3 - x * rd2g / c**2 - g * x / c) / (1 + x**2 / c**2)
    chk("r'' from the r equation with r'^2 from the energy", rddg, rdd_H.subs(rd, sp.sqrt(rd2g)).subs(r, x))
    qx2 = 1 + x**2 / c**2
    chk("r'^2 + r r'' = [2E + H^2/c^2 - (2 + r^2/c^2) g r^2/c]/q^4", rd2g + x * rddg,
        (2 * Es + H**2 / c**2 - (2 + x**2 / c**2) * g * x**2 / c) / qx2**2)
    chk("identity g c q^4 - (2 + r^2/c^2) g r^2/c = g c", g * c * qx2**2 - (2 + x**2 / c**2) * g * x**2 / c, g * c)
    chk("c q^3 = (c^2 + r^2)^(3/2)/c^2", c * qx2**sp.Rational(3, 2), (c**2 + x**2)**sp.Rational(3, 2) / c**2)
    Ng = sp.sqrt(1 + x**2 / c**2) * m * ((rd2g + x * rddg) / c + g)
    chk("N = m (2 E c^2 + H^2 + g c^3)/(c^2 + r^2)^(3/2) on every motion", Ng,
        m * (2 * Es * c**2 + H**2 + g * c**3) / (c**2 + x**2)**sp.Rational(3, 2))

    # numeric case r0 = c/2, v0 = 2 r0 Omega0 = c sqrt(g/c): r_max = c
    sub = {r0: c / 2, v0: c * sp.sqrt(g / c)}
    rmax = (v0 * sp.sqrt(c / g)).subs(sub)
    chk("r_max = c for v0 = 2 r0 Omega0, r0 = c/2", rmax, c)
    Hn = (r0 * v0).subs(sub)
    chk("H^2 = c^3 g/4", Hn**2, c**3 * g / 4)
    # reaction along the oscillation as a function of r (r'^2 from energy, r'' from the equation)
    Ein = (v0**2 / 2 + g * r0**2 / (2 * c)).subs(sub)
    rd2 = (2 * Ein - Hn**2 / x**2 - g * x**2 / c) / (1 + x**2 / c**2)
    rddx = rdd_H.subs(H, Hn).subs({rd: sp.sqrt(rd2)}).subs(r, x)
    Nx = sp.simplify((sp.sqrt(1 + x**2 / c**2) * m * ((rd2 + x * rddx) / c + g)))
    chk("numeric case: E = 5 g c/8", Ein, 5 * g * c / 8)
    chk("numeric case: N(r) = (5/2) m g c^3/(c^2 + r^2)^(3/2)", Nx, 5 * m * g * c**3 / (2 * (c**2 + x**2)**sp.Rational(3, 2)))
    chk("r'^2 vanishes at r = c/2 and r = c", sp.Matrix([rd2.subs(x, c / 2), rd2.subs(x, c)]).norm())
    chk("N at r = c/2 (inner turning point) = (4/sqrt5) m g", Nx.subs(x, c / 2), 4 * m * g / sp.sqrt(5))
    chk("N at r = c (outer turning point) = (5 sqrt2/8) m g", Nx.subs(x, c), 5 * sp.sqrt(2) * m * g / 8)
    chk("r'' at r = c/2 = 6g/5 (outwards)", rddx.subs(x, c / 2).subs(rd, 0), 6 * g / 5)
    chk("r'' at r = c = -3g/8 (inwards)", rddx.subs(x, c), -3 * g / 8)
    vals = [sp.N((Nx / (m * g)).subs(x, c / 2 + c / 2 * sp.Rational(i, 200)).subs(c, 1)) for i in range(201)]
    chk.true("N > 0 on the whole oscillation c/2 <= r <= c (min %.4f m g)" % min(vals), min(vals) > 0)
    chk.value("min of N/(m g) on [c/2, c] is at r = c: 0.8839", min(vals), 5 * sp.sqrt(2) / 8, tol=1e-6)
    chk.value("4/sqrt5 = 1.789", 4 / sp.sqrt(5), 1.78885, tol=1e-5)
    num = {c: 1, g: sp.Rational(981, 100)}
    chk.value("Omega0 = 3.132 rad/s for c = 1 m", sp.sqrt(g / c).subs(num), 3.13209, tol=1e-5)
    chk.value("v0 = 3.132 m/s for c = 1 m", (c * sp.sqrt(g / c)).subs(num), 3.13209, tol=1e-5)
    chk.value("omega_r for r0 = c/2: 4/sqrt5 Omega0 = 5.603 rad/s", sp.sqrt(wr2.subs(r0, c / 2)).subs(num), 5.60286, tol=1e-4)
