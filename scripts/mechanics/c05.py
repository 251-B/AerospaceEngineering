"""C05: inertia forces (bank item C05).

(a) bead on a smooth horizontal rod rotating with constant Omega: Coriolis power, relative kinetic energy, rod reaction.
    Independent route: absolute Newton law in the inertial frame for the bead r(t), phi = Omega t.
(b) frame translating with constant acceleration a0: relative trajectory of a free particle.
"""
import sympy as sp


def verify(chk):
    t = sp.symbols("t", real=True)
    m, W, r0, a0, U = sp.symbols("m Omega r0 a0 U", positive=True)
    r = sp.Function("r")(t)

    # (a) absolute position of the bead: rod along e_r(phi = W t)
    er = sp.Matrix([sp.cos(W * t), sp.sin(W * t), 0])
    ep = sp.Matrix([-sp.sin(W * t), sp.cos(W * t), 0])
    k = sp.Matrix([0, 0, 1])
    pos = r * er
    acc = pos.diff(t, 2)
    chk("a . e_r = r'' - W^2 r", sp.simplify(acc.dot(er)), r.diff(t, 2) - W**2 * r)
    chk("a . e_phi = 2 W r'", sp.simplify(acc.dot(ep)), 2 * W * r.diff(t))
    # smooth rod: no force along e_r -> r'' = W^2 r; reaction along e_phi: N = 2 m W r'
    sol = sp.dsolve(sp.Eq(r.diff(t, 2), W**2 * r), r, ics={r.subs(t, 0): r0, r.diff(t).subs(t, 0): 0}).rhs
    chk("r(t) = r0 cosh(W t)", sol, (r0 * sp.cosh(W * t)).rewrite(sp.exp))
    v_rel = r.diff(t) * er
    cor = -2 * m * (W * k).cross(v_rel)
    chk("Coriolis force = -2 m W r' e_phi", (cor - (-2 * m * W * r.diff(t) * ep)).norm()**2, 0)
    chk("Coriolis power in the rotating frame = 0", cor.dot(v_rel), 0)
    cf = -m * (W * k).cross((W * k).cross(pos))
    chk("centrifugal force = m W^2 r e_r", (cf - m * W**2 * r * er).norm()**2, 0)
    chk("centrifugal power = m W^2 r r'", cf.dot(v_rel), m * W**2 * r * r.diff(t))
    Krel = m * sol.diff(t)**2 / 2
    chk("relative KE = m W^2 (r^2 - r0^2)/2", Krel, m * W**2 * (sol**2 - r0**2) / 2)
    # work of centrifugal force from r0 to r: integral of m W^2 s ds
    s, R1 = sp.symbols("s R1", positive=True)
    chk("work of centrifugal force r0 -> r = m W^2 (r^2 - r0^2)/2", sp.integrate(m * W**2 * s, (s, r0, R1)), m * W**2 * (R1**2 - r0**2) / 2)
    # rod reaction N e_phi balances Coriolis in the rotating frame: N = 2 m W r'
    N = 2 * m * W * r.diff(t)
    chk("relative Newton along e_phi: 0 = N - 2 m W r'", N + cor.dot(ep), 0)
    chk("absolute power of the reaction = N e_phi . v_abs = 2 m W^2 r r'", (N * ep).dot(pos.diff(t)), 2 * m * W**2 * r * r.diff(t))
    # full reaction N e_phi + N_z k with the weight -m g k: vertical balance (a . k = 0) gives N_z = m g
    gg = sp.symbols("g", positive=True)
    Nz = sp.solve(sp.Eq(m * acc.dot(k), -m * gg + sp.Symbol("Nz")), sp.Symbol("Nz"))[0]
    chk("vertical part of the rod reaction N_z = m g", Nz, m * gg)
    chk("vertical part does no work: m g k . v_abs = 0", (m * gg * k).dot(pos.diff(t)), 0)
    # absolute kinetic energy rate equals reaction power
    Kabs = m * pos.diff(t).dot(pos.diff(t)) / 2
    chk("d K_abs/dt = power of the reaction (on r'' = W^2 r)",
        sp.simplify(Kabs.diff(t).subs(r.diff(t, 2), W**2 * r)), 2 * m * W**2 * r * r.diff(t))

    # (b) translating frame with constant acceleration a0 i; free particle
    x0, y0 = sp.symbols("x0 y0", real=True)
    rr = sp.Matrix([x0 - a0 * t**2 / 2, y0 + U * t, 0])
    chk("relative acceleration = -a0 i (only inertia force)", (rr.diff(t, 2) - sp.Matrix([-a0, 0, 0])).norm()**2, 0)
    X, Y = sp.symbols("X Y", real=True)
    # eliminate t: Y - y0 = U t -> X - x0 = -a0 (Y-y0)^2/(2 U^2)
    chk("trajectory: x - x0 = -a0 (y - y0)^2 / (2 U^2)", rr[0] - x0, (-a0 * (rr[1] - y0)**2 / (2 * U**2)))
    vv = rr.diff(t)
    aa = rr.diff(t, 2)
    chk("v_rel x a_rel = -v0 x a0 (constant) = a0 U k", vv.cross(aa)[2], a0 * U)
    # general: v x a constant = v0 x (-a0 e); zero iff v0 parallel to a0
    v0 = sp.Matrix(sp.symbols("v0x v0y v0z", real=True))
    e = sp.Matrix(sp.symbols("ex ey ez", real=True))
    vg = v0 - a0 * t * e
    chk("v(t) x a = (v0 - a0 t e) x (-a0 e) = -a0 v0 x e (independent of t)", (vg.cross(-a0 * e) - (-a0 * v0.cross(e))).norm()**2, 0)
    # parallel initial velocity: straight line
    lam = sp.symbols("lambda", real=True)
    chk("v0 = lambda e -> v x a = 0 (rectilinear)", ((lam * e - a0 * t * e).cross(-a0 * e)).norm()**2, 0)
