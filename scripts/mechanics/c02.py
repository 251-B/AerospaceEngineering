"""C02: one-dimensional motion in the cubic potential V = V0 (u^3 - 3u), u = x/b (bank item C02).

Checks the critical points, the energy levels, the factorisations used for the turning points, the closed-form time
law near the separatrix (by differentiation and by a numerical quadrature) and the small-oscillation frequency.
"""
import sympy as sp


def verify(chk):
    u, w = sp.symbols("u w", real=True)
    V0, b, m = sp.symbols("V0 b m", positive=True)
    V = V0 * (u**3 - 3 * u)              # potential as a function of u = x/b
    dVdx = sp.diff(V, u) / b             # chain rule: dV/dx = (dV/du)(du/dx)

    chk("dV/dx = 3 V0 (u^2 - 1)/b", dVdx, 3 * V0 * (u**2 - 1) / b)
    chk.true("critical points u = -1, 1", set(sp.solve(sp.diff(V, u), u)) == {-1, 1})
    chk("V(-b) = 2 V0 (maximum)", V.subs(u, -1), 2 * V0)
    chk("V(b) = -2 V0 (minimum)", V.subs(u, 1), -2 * V0)
    chk.true("V''(-b) < 0, V''(b) > 0", (sp.diff(V, u, 2).subs(u, -1) < 0) and (sp.diff(V, u, 2).subs(u, 1) > 0))
    chk("V(2b) = 2 V0 = V(-b)", V.subs(u, 2), 2 * V0)
    chk("F(2b) = -dV/dx = -9 V0/b (towards -x)", -dVdx.subs(u, 2), -9 * V0 / b)
    chk("E - V = V0 (u+1)^2 (2-u) for E = 2 V0", 2 * V0 - V, V0 * (u + 1)**2 * (2 - u))

    # time from u = 2 to u in (-1, 2): t = b sqrt(m/(6 V0)) ln((sqrt3 + w)/(sqrt3 - w)), w = sqrt(2 - u)
    tw = b * sp.sqrt(m / (6 * V0)) * sp.log((sp.sqrt(3) + w) / (sp.sqrt(3) - w))
    # dt/dw must equal (2b/sqrt(2V0/m)) / (3 - w^2)
    chk("dt/dw = 2b / (sqrt(2V0/m) (3 - w^2))", sp.diff(tw, w), 2 * b / (sp.sqrt(2 * V0 / m) * (3 - w**2)))
    # and that is |dx|/|v| with u = 2 - w^2: |du/dw| = 2w, |v| = sqrt(2 V0/m) (u+1) sqrt(2-u) = sqrt(2V0/m)(3-w^2) w
    speed = sp.sqrt(2 * V0 / m) * (3 - w**2) * w
    chk("b |du/dw| / |v| = dt/dw (substitution u = 2 - w^2)", b * 2 * w / speed, sp.diff(tw, w))
    chk("t(w=0) = 0 (start at x = 2b)", tw.subs(w, 0), 0)
    chk.true("t -> oo as w -> sqrt3 (x -> -b)", sp.limit(tw, w, sp.sqrt(3), "-") == sp.oo)
    # numerical cross-check of the closed form: time from x = 2b to x = 0 (u = 0, w = sqrt2), V0 = m = b = 1
    num = sp.Integral(1 / sp.sqrt(2 * (2 - (u**3 - 3 * u))), (u, 0, 2)).evalf(20)
    chk.value("t(2b -> 0) quadrature = ln((sqrt3+sqrt2)/(sqrt3-sqrt2))/sqrt6", num,
              sp.log((sp.sqrt(3) + sp.sqrt(2)) / (sp.sqrt(3) - sp.sqrt(2))) / sp.sqrt(6), tol=1e-8)

    chk("(sqrt3+sqrt2)/(sqrt3-sqrt2) = 5 + 2 sqrt6", sp.radsimp((sp.sqrt(3) + sp.sqrt(2)) / (sp.sqrt(3) - sp.sqrt(2))), 5 + 2 * sp.sqrt(6))
    chk.value("t(x=0) = ln(5+2sqrt6)/sqrt6 ~ 0.936 b sqrt(m/V0)", sp.log(5 + 2 * sp.sqrt(6)) / sp.sqrt(6), 0.9359, tol=5e-4)
    chk("(u+1)^2 (2-u) = -u^3 + 3u + 2", sp.expand((u + 1)**2 * (2 - u)), -u**3 + 3 * u + 2)
    # (b) released from rest at x = 0: E = 0, turning points V(u) = 0
    chk("V(0) = 0", V.subs(u, 0), 0)
    chk("F(0) = +3 V0/b (towards +x)", -dVdx.subs(u, 0), 3 * V0 / b)
    chk("V = V0 u (u - sqrt3)(u + sqrt3)", V, V0 * u * (u - sp.sqrt(3)) * (u + sp.sqrt(3)))
    chk.true("V < 0 on (0, sqrt3): numeric sample", all(sp.N(V.subs({V0: 1, u: s})) < 0 for s in (0.2, 0.8, 1.2, 1.6, 1.7)))
    chk.true("V(2b) = 2V0 > 0 = E, so x = 2b is not reached", V.subs({u: 2, V0: 1}) > 0)
    chk("dV/dx at sqrt3 b = 6 V0/b (simple turning point, finite time)", dVdx.subs(u, sp.sqrt(3)), 6 * V0 / b)
    chk.value("sqrt3 - 1 = 0.732 vs 1 - 0 = 1 (not symmetric about b)", sp.sqrt(3) - 1, 0.7320508075688772)
    # small oscillations about x = b: omega^2 = V''(b)/m, V'' in x = (1/b^2) d2V/du2
    om2 = sp.diff(V, u, 2).subs(u, 1) / (b**2 * m)
    chk("omega^2 = 6 V0/(m b^2)", om2, 6 * V0 / (m * b**2))
    # energy E = 2 V0 is below V for u < -1 near the barrier? V > 2 V0 only for u > 2: check factor sign for u < -1
    chk.true("for u < -1: E - V = V0(u+1)^2(2-u) > 0 (region x < -b also allowed but not reached)",
             sp.N(((u + 1)**2 * (2 - u)).subs(u, -1.5)) > 0)
