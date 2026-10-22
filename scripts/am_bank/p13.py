"""Bank P13: Laplace in 0<x<pi, 0<y<1, u_x = 0 on x = 0, pi; u(x,0) = 2 + cos 2x, u(x,1) = 4 + 3 cos x. SymPy checks."""
import math
import sympy as sp

x, y = sp.symbols("x y", real=True)
a, b, mu = sp.symbols("a b mu")
n = sp.symbols("n", integer=True, positive=True)
pi = sp.pi
m = sp.symbols("m", positive=True)

# (a) eigenproblem X'' + lam X = 0, X'(0) = X'(pi) = 0
Xneg = a * sp.cosh(m * x) + b * sp.sinh(m * x)
sol = sp.solve([sp.diff(Xneg, x).subs(x, 0), sp.diff(Xneg, x).subs(x, pi)], [a, b], dict=True)
assert sol == [{a: 0, b: 0}]
X0 = a + b * x
assert sp.solve([sp.diff(X0, x).subs(x, 0), sp.diff(X0, x).subs(x, pi)], [b], dict=True) == [{b: 0}]
Xn = sp.cos(n * x)
assert sp.diff(Xn, x).subs(x, 0) == 0 and sp.simplify(sp.diff(Xn, x).subs(x, pi)) == 0

# (b)-(c) solution
u = 2 + 2 * y + sp.cos(2 * x) * sp.sinh(2 * (1 - y)) / sp.sinh(2) + 3 * sp.cos(x) * sp.sinh(y) / sp.sinh(1)
assert sp.simplify(sp.diff(u, x, 2) + sp.diff(u, y, 2)) == 0
assert sp.simplify(sp.diff(u, x).subs(x, 0)) == 0 and sp.simplify(sp.diff(u, x).subs(x, pi)) == 0
assert sp.simplify(u.subs(y, 0) - (2 + sp.cos(2 * x))) == 0
assert sp.simplify(u.subs(y, 1) - (4 + 3 * sp.cos(x))) == 0
# zero mode: A0 + B0 y
A0, B0 = sp.symbols("A0 B0")
assert sp.solve([A0 - 2, A0 + B0 - 4], [A0, B0]) == {A0: 2, B0: 2}
# general cosh/sinh form: for n = 2, A cosh 2y + B sinh 2y with A = 1, A cosh 2 + B sinh 2 = 0
A2, B2 = 1, -sp.cosh(2) / sp.sinh(2)
assert sp.simplify(sp.expand_trig((A2 * sp.cosh(2 * y) + B2 * sp.sinh(2 * y)) - sp.sinh(2 * (1 - y)) / sp.sinh(2)).rewrite(sp.exp)) == 0
# orthogonality projections of the bottom data
f0 = 2 + sp.cos(2 * x)
assert sp.integrate(f0, (x, 0, pi)) / pi == 2
for k in range(1, 6):
    proj = 2 / pi * sp.integrate(f0 * sp.cos(k * x), (x, 0, pi))
    assert sp.simplify(proj - (1 if k == 2 else 0)) == 0
g0 = 4 + 3 * sp.cos(x)
for k in range(1, 6):
    proj = 2 / pi * sp.integrate(g0 * sp.cos(k * x), (x, 0, pi))
    assert sp.simplify(proj - (3 if k == 1 else 0)) == 0

# (d) flux through every horizontal line is 2*pi; centre value 3 - 1/(2 cosh 1)
flux = sp.integrate(sp.diff(u, y), (x, 0, pi))
assert sp.simplify(flux - 2 * pi) == 0
uc = u.subs({x: pi / 2, y: sp.Rational(1, 2)})
assert sp.simplify((uc - (3 - 1 / (2 * sp.cosh(1)))).rewrite(sp.exp)) == 0
assert abs(float(uc) - 2.675973) < 1e-6
# range of boundary data: min 1 (bottom at x = pi/2), max 7 (top at x = 0)
assert abs(float(u.subs({x: 0, y: 1})) - 7) < 1e-12 and abs(float(u.subs({x: pi / 2, y: 0})) - 1) < 1e-12
# grid check of the maximum principle inside
vals = [float(u.subs({x: i * math.pi / 20, y: j / 20})) for i in range(21) for j in range(1, 20)]
assert 1 < min(vals) and max(vals) < 7
# uniqueness: an additive constant breaks the Dirichlet data
assert sp.simplify((u + 1).subs(y, 0) - (2 + sp.cos(2 * x))) != 0
uy = 2 + 3 * sp.cosh(y) / sp.sinh(1) * sp.cos(x) - 2 * sp.cosh(2 - 2 * y) / sp.sinh(2) * sp.cos(2 * x)
assert sp.simplify(sp.diff(u, y) - uy) == 0
assert sp.simplify((sp.sinh(2) - 2 * sp.sinh(1) * sp.cosh(1)).rewrite(sp.exp)) == 0
assert abs(1 / (2 * math.cosh(1)) - 0.324027) < 1e-6
# Phi'(y) = -[u_x]_0^pi = 0
assert sp.simplify(sp.integrate(sp.diff(u, y, 2), (x, 0, pi)) + (sp.diff(u, x).subs(x, pi) - sp.diff(u, x).subs(x, 0))) == 0
print("p13 OK")
