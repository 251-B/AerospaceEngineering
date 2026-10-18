"""C01: intrinsic kinematics on the curve R = a, z = a phi^2 / 2 (bank item C01).

Independent route: Cartesian position vector differentiated directly in SymPy, intrinsic components from
a_t = a.v/|v| and curvature from |r' x r''| / |r'|^3 (parametric formula, no time law involved).
"""
import sympy as sp


def verify(chk):
    t = sp.symbols("t", nonnegative=True)
    a, w, v0 = sp.symbols("a omega v0", positive=True)
    p = sp.symbols("phi", positive=True)

    # (a) time law phi = omega t
    ph = w * t
    r = sp.Matrix([a * sp.cos(ph), a * sp.sin(ph), a * ph**2 / 2])
    v = r.diff(t)
    acc = v.diff(t)
    eR = sp.Matrix([sp.cos(ph), sp.sin(ph), 0])
    ephi = sp.Matrix([-sp.sin(ph), sp.cos(ph), 0])
    ez = sp.Matrix([0, 0, 1])
    chk("v = a w e_phi + a w phi e_z", (v - (a * w * ephi + a * w * ph * ez)).norm()**2, 0)
    chk("a = a w^2 (-e_R + e_z)", (acc - a * w**2 * (-eR + ez)).norm()**2, 0)
    speed = sp.sqrt(sp.simplify(v.dot(v)))
    chk("|v| = a w sqrt(1 + phi^2)", speed, a * w * sp.sqrt(1 + ph**2))
    at = sp.simplify(speed.diff(t))
    chk("a_t = d|v|/dt = a w^2 phi / sqrt(1+phi^2)", at, a * w**2 * ph / sp.sqrt(1 + ph**2))
    chk("a_t = a.v/|v| (same result)", sp.simplify(acc.dot(v) / speed), at)
    t1 = 1 / w  # phi = 1
    chk("a_t(phi=1) = a w^2 / sqrt2", at.subs(t, t1), a * w**2 / sp.sqrt(2))
    a2 = sp.simplify(acc.dot(acc))
    chk("|a|^2 = 2 a^2 w^4", a2, 2 * a**2 * w**4)
    an = sp.sqrt(a2 - at**2)
    chk("a_n(phi=1) = sqrt(3/2) a w^2", an.subs(t, t1), sp.sqrt(sp.Rational(3, 2)) * a * w**2)
    chk.true("a_t(phi=1) is not zero (statement (a) is false)", sp.simplify(at.subs(t, t1)) != 0)
    # normal vector at phi = 1 from the kinematics
    v1, a1 = v.subs(t, t1), acc.subs(t, t1)
    et1 = v1 / v1.norm()
    an_vec = a1 - a1.dot(et1) * et1
    en_kin = sp.simplify(an_vec / sp.sqrt(an_vec.dot(an_vec)))
    eR1, ephi1 = eR.subs(t, t1), ephi.subs(t, t1)
    en_claim = (-2 * eR1 - ephi1 + ez) / sp.sqrt(6)
    chk("e_n(phi=1) = (-2 e_R - e_phi + e_z)/sqrt6 (from the kinematics)", (en_kin - en_claim).norm()**2, 0)
    chk("a_t e_t at phi=1 = a w^2 (e_phi + e_z)/2", (a1.dot(et1) * et1 - a * w**2 * (ephi1 + ez) / 2).norm()**2, 0)

    # (b) curvature from the geometry only (parameter phi)
    rg = sp.Matrix([a * sp.cos(p), a * sp.sin(p), a * p**2 / 2])
    r1, r2 = rg.diff(p), rg.diff(p, 2)
    cr = r1.cross(r2)
    chk("r' x r'' = a^2 (cos+phi sin, sin-phi cos, 1)", (cr - a**2 * sp.Matrix([sp.cos(p) + p * sp.sin(p), sp.sin(p) - p * sp.cos(p), 1])).norm()**2, 0)
    chk("|r' x r''|^2 = a^4 (2 + phi^2)", sp.simplify(cr.dot(cr)), a**4 * (2 + p**2))
    kappa = sp.simplify(sp.sqrt(sp.simplify(r1.cross(r2).dot(r1.cross(r2)))) / sp.sqrt(sp.simplify(r1.dot(r1)))**3)
    chk("kappa(phi) = sqrt(2+phi^2) / (a (1+phi^2)^(3/2))", kappa, sp.sqrt(2 + p**2) / (a * (1 + p**2)**sp.Rational(3, 2)))
    chk("kappa(1) = sqrt6/(4a)", kappa.subs(p, 1), sp.sqrt(6) / (4 * a))
    chk("kappa(0) = sqrt2/a", kappa.subs(p, 0), sp.sqrt(2) / a)
    chk("kappa ~ 1/(a phi^2) for phi -> oo", sp.limit(kappa * a * p**2, p, sp.oo), 1)
    chk("a_n = kappa v^2 in (a) at phi=1", an.subs(t, t1), (kappa.subs(p, 1) * speed.subs(t, t1)**2))
    # geometric principal normal: derivative of the unit tangent with respect to phi
    T = r1 / sp.sqrt(sp.simplify(r1.dot(r1)))
    dT = sp.simplify(T.diff(p)).subs(p, 1)
    en_geo = sp.simplify(dT / sp.sqrt(sp.simplify(dT.dot(dT))))
    en_claim_p = (-2 * sp.Matrix([sp.cos(1), sp.sin(1), 0]) - sp.Matrix([-sp.sin(1), sp.cos(1), 0]) + ez) / sp.sqrt(6)
    chk("geometric e_n(phi=1) is the same unit vector as in (a)", (en_geo - en_claim_p).norm()**2, 0)
    # constant speed v0: a = v0^2 kappa e_n, a.v = 0
    chk("constant speed: |a| = sqrt6 v0^2 / (4a) at phi = 1", v0**2 * kappa.subs(p, 1), sp.sqrt(6) * v0**2 / (4 * a))
    # constant speed time law: phi_dot = v0 / (a sqrt(1+phi^2)); check a.v = 0 by direct differentiation
    s = sp.Function("phi")(t)
    rs = sp.Matrix([a * sp.cos(s), a * sp.sin(s), a * s**2 / 2])
    vs = rs.diff(t)
    accs = vs.diff(t)
    law = {s.diff(t, 2): sp.diff(v0 / (a * sp.sqrt(1 + s**2)), t), }
    accs = accs.subs(law).subs(s.diff(t), v0 / (a * sp.sqrt(1 + s**2)))
    vs = vs.subs(s.diff(t), v0 / (a * sp.sqrt(1 + s**2)))
    chk("constant speed: |v| = v0", sp.simplify(vs.dot(vs)), v0**2)
    chk("constant speed: a . v = 0 (a perpendicular to v)", sp.simplify(accs.dot(vs)), 0)
    chk("constant speed: |a|(phi=1) = sqrt6 v0^2/(4a) (direct)", sp.simplify(accs.dot(accs)).subs(s, 1), 6 * v0**4 / (16 * a**2))
