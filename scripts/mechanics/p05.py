"""P05: flight pendulum on an accelerating support (bank item P05).

Support A moves with constant horizontal acceleration a0 along +x; bob P (mass m) hangs on a massless inextensible
string of length l. theta is measured from the downward vertical towards +x.
"""
import sympy as sp

from ._kit import unit


def verify(chk):
    t = sp.symbols("t", real=True)
    m, l, g, a0 = sp.symbols("m l g a0", positive=True)
    th = sp.Function("theta")(t)
    thd, thdd = th.diff(t), th.diff(t, 2)

    # Absolute position in S0: A(t) = (a0 t^2/2, 0) (starts at rest), P = A + l (sin th, -cos th)
    rA = sp.Matrix([a0 * t**2 / 2, 0])
    rP = rA + l * sp.Matrix([sp.sin(th), -sp.cos(th)])
    aP = rP.diff(t, 2)

    # Lagrange equation (independent of the Newton derivation of the note)
    T_kin = m * (rP.diff(t).dot(rP.diff(t))) / 2
    V = m * g * rP[1]
    L = T_kin - V
    eq = sp.diff(L.diff(thd), t) - L.diff(th)
    sol = sp.solve(sp.Eq(eq, 0), thdd)[0]
    chk("EOM: l*theta'' = -g sin(th) - a0 cos(th)", l * sol, -g * sp.sin(th) - a0 * sp.cos(th))

    # Relative kinematics: e_r = (sin th, -cos th), e_th = (cos th, sin th)
    er = sp.Matrix([sp.sin(th), -sp.cos(th)])
    eth = sp.Matrix([sp.cos(th), sp.sin(th)])
    a_rel = l * thdd * eth - l * thd**2 * er
    chk("a_P = a_A + a_rel (x)", aP[0], a0 + a_rel[0])
    chk("a_P = a_A + a_rel (y)", aP[1], a_rel[1])

    # Tension from Newton along e_r: -m l th'^2 = m g cos th - m a0 sin th - T
    T = sp.symbols("T")
    Tsol = sp.solve(sp.Eq(m * aP.dot(er), -T + m * sp.Matrix([0, -g]).dot(er)), T)[0]
    chk("T = m(l th'^2 + g cos th - a0 sin th)", Tsol, m * (l * thd**2 + g * sp.cos(th) - a0 * sp.sin(th)),
        numeric=None)
    # (uses the string constraint only; th'' cancels because aP.er has no th'' term)

    # Equilibrium and frequency of the linearised motion about it
    ge = sp.sqrt(g**2 + a0**2)
    th_e = sp.atan(-a0 / g)
    chk("theta_e = -atan(a0/g) is an equilibrium", (-g * sp.sin(th) - a0 * sp.cos(th)).subs(th, th_e))
    omega2 = sp.diff(-g * sp.sin(th) - a0 * sp.cos(th), th).subs(th, th_e) / l
    chk("omega^2 = -(d/dth)(RHS)/l = g_eff/l", -omega2, ge / l)

    # Numeric case: a0 = g/sqrt(3) -> theta_e = -30 deg, g_eff = 2g/sqrt(3)
    a0n = g / sp.sqrt(3)
    chk.value("theta_e(a0=g/sqrt3) = -pi/6", th_e.subs(a0, a0n), -sp.pi / 6)
    gen = ge.subs(a0, a0n)
    chk("g_eff = 2g/sqrt3", gen, 2 * g / sp.sqrt(3))

    # Energy in S1 (inertia force is conservative): E = l^2 th'^2/2 - g l cos th + a0 l sin th
    E = l**2 * thd**2 / 2 - g * l * sp.cos(th) + a0 * l * sp.sin(th)
    dE = sp.diff(E, t).subs(thdd, sol)
    chk("dE/dt = 0 on the motion", dE)

    # Released from rest at theta = 0: th'^2 at angle phi = th - th_e measured from equilibrium
    x = sp.symbols("x")  # theta
    E0 = E.subs({thd: 0, th: 0})
    thd2 = sp.solve(sp.Eq(l**2 * sp.Symbol("w")**2 / 2 - g * l * sp.cos(x) + a0 * l * sp.sin(x), E0), sp.Symbol("w")**2)
    w2 = (2 / l**2) * (E0 + g * l * sp.cos(x) - a0 * l * sp.sin(x))
    w2n = sp.simplify(w2.subs(a0, a0n))
    # maximum angle: w2 = 0 -> x = 2 theta_e
    chk("max angle is 2*theta_e = -pi/3", w2n.subs(x, -sp.pi / 3))
    # speed at equilibrium
    w2e = sp.simplify(w2n.subs(x, -sp.pi / 6))
    chk("l th_dot^2 at theta_e = 2 g_eff (1 - cos 30deg)", l * w2e, 2 * gen * (1 - sp.cos(sp.pi / 6)))
    Te = sp.simplify((m * (l * w2e + g * sp.cos(x) - a0n * sp.sin(x))).subs(x, -sp.pi / 6))
    chk("T(theta_e) = m g_eff (3 - sqrt3)", Te, m * gen * (3 - sp.sqrt(3)))
    chk.value("T(theta_e)/(m g) = 2(3-sqrt3)/sqrt3 ~ 1.4641", Te / (m * g), 2 * (3 - sp.sqrt(3)) / sp.sqrt(3))

    # Taut string over the whole swing: T(phi) = m g_eff (3 cos phi - 2 cos 30deg), phi in [-30, 30] deg
    phi = sp.symbols("phi")
    Tphi = m * gen * (3 * sp.cos(phi) - 2 * sp.cos(sp.pi / 6))
    chk("T(phi) consistent with the energy law", Tphi.subs(phi, 0), Te)
    chk.true("T(phi) > 0 on [-30, 30] deg (minimum at the ends = m g_eff cos30)",
             sp.N(Tphi.subs(phi, sp.pi / 6).subs({m: 1, g: 1})) > 0)

    # Phase 2: at theta = theta_e the support stops accelerating (a0 -> 0), the speed is kept
    thd_e2 = sp.simplify(w2e)                      # th'^2 at theta_e (units 1/s^2)
    cos_max = sp.simplify(1 - (l**2 * thd_e2 / 2 + g * l * (1 - sp.cos(sp.pi / 6))) / (g * l))
    chk.value("phase 2: cos(theta_max) = 1 - sqrt3/6", cos_max.subs({g: 1, l: 1}), 1 - sp.sqrt(3) / 6)
    chk.value("phase 2: theta_max = 44.64 deg", sp.acos(1 - sp.sqrt(3) / 6) * 180 / sp.pi, 44.6572, tol=1e-3)
    # speed and tension when the pendulum passes the vertical in phase 2 (a0 = 0, g only)
    k2 = sp.simplify(l * w2e) + 2 * g * (1 - sp.cos(sp.pi / 6)) * 0  # l*th'^2 at theta_e (phase 2 starts there)
    lth_vert = k2 + 2 * g * (sp.cos(0) - sp.cos(sp.pi / 6))        # energy: l th'^2/2 - g cos th const -> at th=0
    chk("phase 2: l th'^2 at the vertical = g/sqrt3", sp.simplify(lth_vert.subs(a0, a0n)), g / sp.sqrt(3))
    chk("phase 2: T at the vertical = m g (1 + 1/sqrt3)", m * (lth_vert.subs(a0, a0n) + g), m * g * (1 + 1 / sp.sqrt(3)))
    chk("T at the turning points of phase 1 = m g (T = m g_eff cos(alpha), g_eff cos(alpha) = g)", Tphi.subs(phi, sp.pi / 6), m * g)

    # change of basis {e_r, e_theta} <- {i, j}: orthonormal and right-handed
    R = sp.Matrix([[sp.sin(th), -sp.cos(th)], [sp.cos(th), sp.sin(th)]])
    chk.true("R R^T = I", sp.simplify(R * R.T) == sp.eye(2))
    chk("det R = 1", R.det(), 1)
    chk("i = sin(th) e_r + cos(th) e_th (x)", 1 - (sp.sin(th) * er[0] + sp.cos(th) * eth[0]))
    chk("i = sin(th) e_r + cos(th) e_th (y)", 0 - (sp.sin(th) * er[1] + sp.cos(th) * eth[1]))
