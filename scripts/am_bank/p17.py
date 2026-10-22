"""P17: predator-prey with logistic prey, x' = x(1-x) - x y, y' = y(x - a), 0 < a < 1."""
import sympy as sp

x, y, a, t = sp.symbols("x y a t", real=True)
F = sp.Matrix([x * (1 - x) - x * y, y * (x - a)])
J = F.jacobian([x, y])
assert sp.simplify(J - sp.Matrix([[1 - 2 * x - y, -x], [y, x - a]])) == sp.zeros(2)

# equilibria
eqs = sp.solve(list(F), [x, y], dict=True)
pts = {(sp.simplify(e[x]), sp.simplify(e[y])) for e in eqs}
assert pts == {(0, 0), (1, 0), (a, 1 - a)}

# (0,0): saddle, eigenvalues 1 and -a
J00 = J.subs({x: 0, y: 0})
assert J00 == sp.Matrix([[1, 0], [0, -a]])
# (1,0): eigenvalues -1 and 1-a, eigenvectors (1,0) and (1, a-2)
J10 = J.subs({x: 1, y: 0})
assert J10 == sp.Matrix([[-1, -1], [0, 1 - a]])
assert sp.simplify(J10 * sp.Matrix([1, a - 2]) - (1 - a) * sp.Matrix([1, a - 2])) == sp.zeros(2, 1)

# interior point
Ji = J.subs({x: a, y: 1 - a})
assert sp.simplify(Ji - sp.Matrix([[-a, -a], [1 - a, 0]])) == sp.zeros(2)
tr, det = Ji.trace(), sp.simplify(Ji.det())
assert sp.simplify(tr + a) == 0 and sp.simplify(det - a * (1 - a)) == 0
disc = sp.expand(tr**2 - 4 * det)
assert sp.simplify(disc - a * (5 * a - 4)) == 0
assert sp.solve(sp.Eq(disc, 0), a) == [0, sp.Rational(4, 5)]

# a = 4/5: double eigenvalue -2/5, single eigenvector (2,-1)
J45 = Ji.subs(a, sp.Rational(4, 5))
assert J45.eigenvals() == {-sp.Rational(2, 5): 2}
M = J45 + sp.Rational(2, 5) * sp.eye(2)
assert M != sp.zeros(2) and M * sp.Matrix([2, -1]) == sp.zeros(2, 1)
# f vanishes at the coexistence point
assert sp.simplify(F.subs({x: a, y: 1 - a})) == sp.zeros(2, 1)

# a = 1/2: focus with eigenvalues -1/4 +- i sqrt(3)/4
J_half = Ji.subs(a, sp.Rational(1, 2))
ev = set(J_half.eigenvals())
assert ev == {-sp.Rational(1, 4) + sp.I * sp.sqrt(3) / 4, -sp.Rational(1, 4) - sp.I * sp.sqrt(3) / 4}
# rotation: J*(1,0) = (-a, 1-a), second component > 0 -> counter-clockwise
assert (J_half * sp.Matrix([1, 0]))[1] == sp.Rational(1, 2)

# a = 9/11: node, eigenvalues -3/11, -6/11, eigenvectors (3,-2), (3,-1)
J9 = Ji.subs(a, sp.Rational(9, 11))
assert J9 == sp.Matrix([[-sp.Rational(9, 11), -sp.Rational(9, 11)], [sp.Rational(2, 11), 0]])
assert set(J9.eigenvals()) == {-sp.Rational(3, 11), -sp.Rational(6, 11)}
v1, v2 = sp.Matrix([3, -2]), sp.Matrix([3, -1])
assert J9 * v1 == -sp.Rational(3, 11) * v1 and J9 * v2 == -sp.Rational(6, 11) * v2
P = sp.Matrix.hstack(v1, v2)
assert P.det() == 3 and P.inv() == sp.Matrix([[-1, -3], [2, 3]]) / 3
assert P.inv() * J9 * P == sp.diag(-sp.Rational(3, 11), -sp.Rational(6, 11))

# Lyapunov function (extension): V' = -(x-a)^2
b = 1 - a
V = x - a - a * sp.log(x / a) + y - b - b * sp.log(y / b)
Vdot = sp.diff(V, x) * F[0] + sp.diff(V, y) * F[1]
assert sp.simplify(Vdot + (x - a) ** 2) == 0

# numerical sanity: orbit from (0.2, 0.2) tends to (a, 1-a) for a = 1/2
import numpy as np
from scipy.integrate import solve_ivp
for av in (0.5, 9 / 11):
    sol = solve_ivp(lambda s, z: [z[0] * (1 - z[0]) - z[0] * z[1], z[1] * (z[0] - av)], (0, 400), [0.2, 0.2], rtol=1e-10, atol=1e-12)
    assert np.allclose(sol.y[:, -1], [av, 1 - av], atol=1e-6)

print("p17 OK")
