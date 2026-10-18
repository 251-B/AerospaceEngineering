"""P01: bead on a vertical circular helix (bank item P01).

Helix of radius R and pitch parameter b: rho = R, z = b*phi (z up, gravity -g k). Bead P of mass m, smooth wire,
released from rest at phi = phi0. Independent routes: Cartesian position differentiated directly, Frenet quantities
from the parametric formulas kappa = |r' x r''| / |r'|^3 and tau = (r' x r'').r''' / |r' x r''|^2, Lagrange equation.
"""
import sympy as sp


def _vec(chk):
    """Wrap chk so that a Matrix check passes when every component simplifies to zero."""
    def vchk(name, left, right=None):
        left = sp.Matrix(left)
        right = sp.zeros(*left.shape) if right is None else sp.Matrix(right)
        d = (left - right).applyfunc(lambda e: sp.simplify(sp.trigsimp(e)))
        return chk.true(name, all(e == 0 for e in d), "" if all(e == 0 for e in d) else f"residual {list(d)}")
    return vchk


def verify(chk):
    vchk = _vec(chk)
    t = sp.symbols("t", real=True)
    m, R, b, g = sp.symbols("m R b g", positive=True)
    ph0, u = sp.symbols("phi0 u", real=True)
    ph = sp.Function("phi")(t)
    phd, phdd = ph.diff(t), ph.diff(t, 2)
    h = sp.sqrt(R**2 + b**2)

    # Cartesian position and its derivatives
    r = sp.Matrix([R * sp.cos(ph), R * sp.sin(ph), b * ph])
    v, a = r.diff(t), r.diff(t, 2)
    erho = sp.Matrix([sp.cos(ph), sp.sin(ph), 0])
    ephi = sp.Matrix([-sp.sin(ph), sp.cos(ph), 0])
    k = sp.Matrix([0, 0, 1])
    # change of basis [e_rho; e_phi; k] = R [i; j; k] and Frenet triad [t; n; b] = Q [e_rho; e_phi; k]
    q = sp.symbols("q", real=True)
    Rm = sp.Matrix([[sp.cos(q), sp.sin(q), 0], [-sp.sin(q), sp.cos(q), 0], [0, 0, 1]])
    chk("R rows are e_rho, e_phi, k", sum(x**2 for x in (Rm - sp.Matrix.hstack(erho, ephi, k).T.subs(ph, q))))
    chk("R R^T = I", sum(x**2 for x in (Rm * Rm.T - sp.eye(3))))
    chk("det R = +1", Rm.det(), 1)
    Q = sp.Matrix([[0, R / h, b / h], [-1, 0, 0], [0, -b / h, R / h]])
    chk("Q Q^T = I (Frenet triad in the cylindrical basis)", sum(x**2 for x in (Q * Q.T - sp.eye(3))))
    chk("det Q = +1", Q.det(), 1)
    vchk("v = R phi' e_phi + b phi' k", v, R * phd * ephi + b * phd * k)
    vchk("a = -R phi'^2 e_rho + R phi'' e_phi + b phi'' k", a, -R * phd**2 * erho + R * phdd * ephi + b * phdd * k)
    chk("|v|^2 = (R^2+b^2) phi'^2", v.dot(v), h**2 * phd**2)

    # Frenet quantities of the curve r(u) (parameter u = phi)
    ru = sp.Matrix([R * sp.cos(u), R * sp.sin(u), b * u])
    r1, r2, r3 = ru.diff(u), ru.diff(u, 2), ru.diff(u, 3)
    cr = r1.cross(r2)
    kappa = sp.sqrt(sp.simplify(cr.dot(cr))) / sp.sqrt(sp.simplify(r1.dot(r1)))**3
    tau = sp.simplify(cr.dot(r3) / cr.dot(cr))
    chk("curvature kappa = R/(R^2+b^2)", kappa, R / h**2)
    chk("torsion tau = b/(R^2+b^2)", tau, b / h**2)
    tv = r1 / h
    nv = sp.simplify(tv.diff(u) / h / (R / h**2))
    bv = sp.simplify(tv.cross(nv))
    eru = sp.Matrix([sp.cos(u), sp.sin(u), 0])
    epu = sp.Matrix([-sp.sin(u), sp.cos(u), 0])
    vchk("t = (R e_phi + b k)/h", tv, (R * epu + b * k) / h)
    vchk("n = -e_rho (towards the axis)", nv, -eru)
    vchk("b = (-b e_phi + R k)/h", bv, (-b * epu + R * k) / h)
    vchk("Frenet: db/ds = -tau n", bv.diff(u) / h, -(b / h**2) * nv)
    vchk("Frenet: dn/ds = -kappa t + tau b", nv.diff(u) / h, -(R / h**2) * tv + (b / h**2) * bv)

    # intrinsic components of the acceleration (on the motion, basis at phi(t))
    sub = {u: ph}
    T, N, B = tv.subs(sub), nv.subs(sub), bv.subs(sub)
    chk("a.t = h phi''", a.dot(T), h * phdd)
    chk("a.n = R phi'^2 (= kappa s'^2)", a.dot(N), R * phd**2)
    chk("a.b = 0", a.dot(B))
    vchk("weight components: k.t = b/h, k.n = 0, k.b = R/h", sp.Matrix([k.dot(T), k.dot(N), k.dot(B)]),
        sp.Matrix([b / h, 0, R / h]))

    # Lagrange equation (independent of the Newton projection)
    L = m * v.dot(v) / 2 - m * g * r[2]
    eq = sp.diff(L.diff(phd), t) - L.diff(ph)
    acc = sp.solve(sp.Eq(eq, 0), phdd)[0]
    chk("EOM: phi'' = -g b/(R^2+b^2), constant", acc, -g * b / h**2)

    # reaction = m a - W with phi'' from the EOM
    W = sp.Matrix([0, 0, -m * g])
    Nr = (m * a - W).subs(phdd, acc)
    chk("reaction has no tangential component", Nr.dot(T))
    chk("N_n = m R phi'^2", Nr.dot(N), m * R * phd**2)
    chk("N_b = m g R/h", Nr.dot(B), m * g * R / h)

    # energy first integral and phi'^2(phi)
    E = m * h**2 * phd**2 / 2 + m * g * b * ph
    chk("dE/dt = 0 on the motion", sp.diff(E, t).subs(phdd, acc))
    w2 = 2 * g * b * (ph0 - u) / h**2
    chk("phi'^2 = 2 g b (phi0 - phi)/h^2 from E(phi0, 0)", (m * h**2 * w2 / 2 + m * g * b * u) - m * g * b * ph0)
    chk("N_n(phi) = 2 m g R b (phi0-phi)/h^2", m * R * w2, 2 * m * g * R * b * (ph0 - u) / h**2)

    # law of motion and one full turn (phi0 - phi = 2 pi)
    ts = sp.symbols("t", positive=True)
    phit = ph0 - g * b * ts**2 / (2 * h**2)
    vchk("phi(t) = phi0 - g b t^2/(2 h^2) satisfies the EOM and the ICs",
        sp.Matrix([phit.diff(ts, 2) - acc, phit.subs(ts, 0) - ph0, phit.diff(ts).subs(ts, 0)]), sp.zeros(3, 1))
    t1 = 2 * h * sp.sqrt(sp.pi / (g * b))
    chk("time for one turn t1 = 2 h sqrt(pi/(g b))", phit.subs(ts, t1), ph0 - 2 * sp.pi)
    speed = h * sp.sqrt(w2.subs(u, ph0 - 2 * sp.pi))
    chk("speed after one turn = sqrt(4 pi g b) = sqrt(2 g dz)", speed, sp.sqrt(4 * sp.pi * g * b))
    chk("same speed from the velocity of the law of motion", h * sp.Abs(phit.diff(ts).subs(ts, t1)), sp.sqrt(4 * sp.pi * g * b))
    Nn1 = m * R * w2.subs(u, ph0 - 2 * sp.pi)
    chk("N_n after one turn = 4 pi m g R b/h^2", Nn1, 4 * sp.pi * m * g * R * b / h**2)

    # limits used in the interpretation
    chk("z'' = b phi'' = -g b^2/h^2 (-> -g when R -> 0)", b * acc, -g * b**2 / h**2)
    chk.true("z'' -> -g as R -> 0", sp.limit(b * acc, R, 0) == -g)
    chk.true("phi'' -> 0 as b -> 0", sp.limit(acc, b, 0) == 0)
    chk("d tau/db = 0 at b = R (maximum torsion)", sp.diff(b / h**2, b).subs(b, R))
    chk("energy integral from the EOM: h^2 phi' phi'' = -g b phi'", (h**2 * phd * phdd).subs(phdd, acc), -g * b * phd)
    chk("N_n = 2 m g kappa dz with dz = b (phi0 - phi)", 2 * m * g * (R / h**2) * b * (ph0 - u), m * R * w2)

    # numerical case R = 0.3 m, b = 0.4 m, g = 9.81 m/s^2
    num = {R: sp.Rational(3, 10), b: sp.Rational(2, 5), g: sp.Rational(981, 100), m: 1}
    chk.value("h = 0.5 m", h.subs(num), 0.5)
    chk.value("kappa = 1.2 1/m", (R / h**2).subs(num), 1.2)
    chk.value("tau = 1.6 1/m", (b / h**2).subs(num), 1.6)
    chk.value("phi'' = -15.696 rad/s^2", acc.subs(num), -15.696)
    chk.value("tangential acceleration h phi'' = -7.848 m/s^2", (h * acc).subs(num), -7.848)
    chk.value("t1 = 0.8948 s", t1.subs(num), 0.894774, tol=1e-5)
    chk.value("speed after one turn = 7.022 m/s", speed.subs(num), 7.02214, tol=1e-4)
    chk.value("|phi'| after one turn = 14.04 rad/s", sp.sqrt(w2.subs(u, ph0 - 2 * sp.pi)).subs(num), 14.0440, tol=1e-3)
    chk.value("N_n/(m g) after one turn = 1.92 pi = 6.032", (Nn1 / (m * g)).subs(num), 1.92 * float(sp.pi))
    chk.value("N_b/(m g) = 0.6", (R / h).subs(num), 0.6)
    chk.value("|N|/(m g) after one turn = 6.062", sp.sqrt((1.92 * sp.pi)**2 + sp.Rational(9, 25)), 6.06163, tol=1e-4)
    chk.value("helix angle: sin(alpha) = b/h = 0.8, alpha = 53.13 deg", sp.asin((b / h).subs(num)) * 180 / sp.pi, 53.1301, tol=1e-3)
