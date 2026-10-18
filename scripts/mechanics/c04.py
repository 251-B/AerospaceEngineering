"""C04: angular momentum under a non-central force, and about a moving point (bank item C04).

(a) F = f(r) u_r + q(r) e_phi: Cartesian Newton equations, invariance of the plane z = 0, rate of h_z.
(b) circular central-force orbit about O, angular momentum about A moving with constant velocity u i.
"""
import sympy as sp


def verify(chk):
    t = sp.symbols("t", real=True)
    m, u, rho, n = sp.symbols("m u rho n", positive=True)
    f, q = sp.Function("f"), sp.Function("q")  # azimuthal force function q(r) (named q in the note)

    # (a) Cartesian components of the force at a generic point (x, y, z)
    x, y, z = sp.symbols("x y z", real=True)
    r = sp.sqrt(x**2 + y**2 + z**2)
    Rcyl = sp.sqrt(x**2 + y**2)
    ur = sp.Matrix([x, y, z]) / r
    ephi = sp.Matrix([-y, x, 0]) / Rcyl
    F = f(r) * ur + q(r) * ephi
    chk("F_z = f(r) z / r (vanishes on z = 0)", F[2], f(r) * z / r)
    chk("F_z(z=0) = 0", F[2].subs(z, 0), 0)
    rv = sp.Matrix([x, y, z])
    M_O = rv.cross(F)
    chk("M_O,z = r_cyl q(r) (not zero: h not conserved)", sp.simplify(M_O[2] / q(r)), Rcyl, numeric={x: sp.Rational(13, 10), y: sp.Rational(7, 10), z: sp.Rational(2, 5)})
    chk("M_O,z(z=0) = R q(R)", sp.simplify((M_O[2] / q(r)).subs(z, 0) - Rcyl), 0)
    chk("M_O on z = 0 is along k only", sp.simplify(M_O[0].subs(z, 0))**2 + sp.simplify(M_O[1].subs(z, 0))**2, 0)

    # polar form in the plane: d/dt (m R^2 phi') = R q(R)
    R = sp.Function("R")(t)
    ph = sp.Function("phi")(t)
    pos = sp.Matrix([R * sp.cos(ph), R * sp.sin(ph), 0])
    acc = pos.diff(t, 2)
    eR = sp.Matrix([sp.cos(ph), sp.sin(ph), 0])
    eP = sp.Matrix([-sp.sin(ph), sp.cos(ph), 0])
    hz = m * pos.cross(pos.diff(t))[2]
    chk("h_z = m R^2 phi'", hz, m * R**2 * ph.diff(t))
    chk("d h_z/dt = m R a_phi (and a_phi = q/m on the motion)", sp.simplify(hz.diff(t) - m * R * acc.dot(eP)), 0)
    chk("a_phi = R phi'' + 2 R' phi'", sp.simplify(acc.dot(eP)), R * ph.diff(t, 2) + 2 * R.diff(t) * ph.diff(t))
    # on the motion m a_phi = q(R): dh_z/dt = R q(R)
    chk("d h_z/dt = R q(R) on the motion", sp.simplify(hz.diff(t).subs(ph.diff(t, 2), (q(R) / m - 2 * R.diff(t) * ph.diff(t)) / R)),
        R * q(R))
    # h is perpendicular to r and v: r . h = 0
    chk("r . (r x m v) = 0 (motion in the plane normal to h)", pos.dot(pos.cross(m * pos.diff(t))), 0)

    # (b) circular orbit radius rho, rate n, about O; A at u t i
    rP = sp.Matrix([rho * sp.cos(n * t), rho * sp.sin(n * t), 0])
    vP = rP.diff(t)
    Fc = m * rP.diff(t, 2)
    chk("circular orbit force is central: r_P x F = 0", (rP.cross(Fc)).norm()**2, 0)
    rA = sp.Matrix([u * t, 0, 0])
    vA = rA.diff(t)
    HA = (rP - rA).cross(m * vP)
    chk("H_A,z = m (n rho^2 - u t n rho cos(nt))", sp.simplify(HA[2]), m * (n * rho**2 - u * t * n * rho * sp.cos(n * t)))
    dHA = sp.simplify(HA.diff(t))
    chk("dH_A/dt = M_A - v_A x m v_P (Notes Eq. 4.52)", (dHA - ((rP - rA).cross(Fc) - vA.cross(m * vP))).norm()**2, 0)
    chk("M_A = -r_A x F", ((rP - rA).cross(Fc) - (-rA.cross(Fc))).norm()**2, 0)
    chk("dH_A,z/dt = -m u n rho (cos nt - n t sin nt)", dHA[2], -m * u * n * rho * (sp.cos(n * t) - n * t * sp.sin(n * t)))
    chk("dH_A,z/dt (t=0) = -m u n rho != 0", dHA[2].subs(t, 0), -m * u * n * rho)
    # relative angular momentum (seen from S_A): rate = M_A, zero at t = 0 but not later
    HAA = (rP - rA).cross(m * (vP - vA))
    dHAA = sp.simplify(HAA.diff(t))
    chk("dH_A,A/dt = M_A (Notes Eq. 4.55)", (dHAA - (rP - rA).cross(Fc)).norm()**2, 0)
    chk("dH_A,A,z/dt = m u n^2 rho t sin(n t)", dHAA[2], m * u * n**2 * rho * t * sp.sin(n * t))
    chk.true("dH_A,A,z/dt != 0 at n t = pi/2", sp.simplify(dHAA[2].subs(t, sp.pi / (2 * n))) != 0)
