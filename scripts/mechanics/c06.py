"""C06: particle on the outside of a smooth sphere whose centre is moved up and down, h(t) = b sin(Omega t) (bank item C06).

Checks the constraint function, the velocity decomposition, the power of the normal reaction in S0 and in the frame of
the centre, and the Lagrangian with two coordinates (theta, phi) as an independent count of the degrees of freedom.
"""
import sympy as sp


def verify(chk):
    t = sp.symbols("t", real=True)
    R, b, W, m, g, N, H = sp.symbols("R b Omega m g N H", positive=True)
    th = sp.Function("theta")(t)
    ph = sp.Function("phi")(t)
    h = H + b * sp.sin(W * t)

    ur = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
    et = sp.Matrix([sp.cos(th) * sp.cos(ph), sp.cos(th) * sp.sin(ph), -sp.sin(th)])
    ep = sp.Matrix([-sp.sin(ph), sp.cos(ph), 0])
    k = sp.Matrix([0, 0, 1])
    rC = h * k
    rP = rC + R * ur

    # constraint function f(r, t) = |r - h(t) k| - R, zero on the surface (holonomic, explicit t: rheonomic)
    x, y, z = sp.symbols("x y z", real=True)
    f = sp.sqrt(x**2 + y**2 + (z - h)**2) - R
    chk("f(r_P, t) = 0 on the sphere", sp.simplify(f.subs({x: rP[0], y: rP[1], z: rP[2]})), 0)
    chk.true("df/dt explicit != 0 (rheonomic)", sp.simplify(sp.diff(f, t)) != 0)

    chk("df/dt = -(z - h) h' / |r - h k|", sp.diff(f, t), -(z - h) * h.diff(t) / sp.sqrt(x**2 + y**2 + (z - h)**2))
    chk("d u_r/dt = th' e_th + sin th phi' e_phi", (ur.diff(t) - (th.diff(t) * et + sp.sin(th) * ph.diff(t) * ep)).norm()**2, 0)
    vP = rP.diff(t)
    v_rel = R * (th.diff(t) * et + sp.sin(th) * ph.diff(t) * ep)
    chk("v_P = h' k + R (th' e_th + sin th phi' e_phi)", (vP - (h.diff(t) * k + v_rel)).norm()**2, 0)
    chk("u_r . v_rel = 0 (reaction normal to the surface velocity)", sp.simplify(ur.dot(v_rel)), 0)
    chk("power of N u_r in S0 = N h' cos th", sp.simplify((N * ur).dot(vP)), N * h.diff(t) * sp.cos(th))
    chk("= N b W cos(W t) cos th", sp.simplify((N * ur).dot(vP)), N * b * W * sp.cos(W * t) * sp.cos(th))
    chk.true("nonzero example: th = 0, t = 0 -> N b W", sp.simplify(((N * ur).dot(vP)).subs(th, 0).subs(t, 0)) == N * b * W)

    # Lagrangian in (theta, phi): two independent coordinates, both appear with their own second derivative
    L = m * vP.dot(vP) / 2 - m * g * rP[2]
    eqs = [sp.simplify(sp.diff(L.diff(q.diff(t)), t) - L.diff(q)) for q in (th, ph)]
    chk.true("EOM theta contains theta''", eqs[0].has(th.diff(t, 2)))
    chk.true("EOM phi contains phi''", eqs[1].has(ph.diff(t, 2)))
    J = sp.Matrix([[sp.diff(e, q.diff(t, 2)) for q in (th, ph)] for e in eqs])
    chk("mass matrix det = m^2 R^4 sin^2 th (nonsingular: 2 DOF)", sp.simplify(J.det()), m**2 * R**4 * sp.sin(th)**2)
    # theta equation: m R^2 th'' - m R^2 sin cos phi'^2 = (m g + m h'') R sin th  (frame of C: gravity + inertia force)
    chk("theta EOM: R th'' - R sin cos phi'^2 - (g + h'') sin th = 0",
        sp.simplify(eqs[0] / (m * R)), R * th.diff(t, 2) - R * sp.sin(th) * sp.cos(th) * ph.diff(t)**2 - (g + h.diff(t, 2)) * sp.sin(th))
    # Newton along u_r gives N (unilateral: N >= 0 while in contact)
    aP = vP.diff(t)
    Nsol = sp.simplify(m * aP.dot(ur) + m * g * k.dot(ur))
    chk("N = m(g + h'') cos th - m R (th'^2 + sin^2 th phi'^2)", Nsol,
        m * (g + h.diff(t, 2)) * sp.cos(th) - m * R * (th.diff(t)**2 + sp.sin(th)**2 * ph.diff(t)**2))
