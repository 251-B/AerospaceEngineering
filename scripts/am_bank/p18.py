"""P18: damped mass-spring m x'' + c x' + k x = 0 as a first-order system; critically damped case m=1, k=4, c=4."""
import sympy as sp

t = sp.symbols("t", real=True)
m, k, c = sp.symbols("m k c", positive=True)
A = sp.Matrix([[0, 1], [-k / m, -c / m]])
lam = sp.symbols("lambda")
charp = sp.expand((A - lam * sp.eye(2)).det())
assert sp.simplify(charp - (lam**2 + c / m * lam + k / m)) == 0
assert A.trace() == -c / m and sp.simplify(A.det() - k / m) == 0
disc = sp.simplify(A.trace() ** 2 - 4 * A.det())
assert sp.simplify(disc - (c**2 - 4 * m * k) / m**2) == 0
# critical damping
assert sp.solve(sp.Eq(c**2 - 4 * m * k, 0), c) == [2 * sp.sqrt(k * m)]

# numbers: m = 1 kg, k = 4 N/m; c = 4 critical; regimes for c = 0, 2, 4, 5
for cv, kind in [(0, "centre"), (2, "focus"), (4, "degenerate"), (5, "node")]:
    An = A.subs({m: 1, k: 4, c: cv})
    ev = An.eigenvals()
    if kind == "centre":
        assert set(ev) == {2 * sp.I, -2 * sp.I}
    if kind == "focus":
        assert set(ev) == {-1 + sp.sqrt(3) * sp.I, -1 - sp.sqrt(3) * sp.I}
    if kind == "degenerate":
        assert ev == {-2: 2}
    if kind == "node":
        assert set(ev) == {-1, -4}

A4 = sp.Matrix([[0, 1], [-4, -4]])
N = A4 + 2 * sp.eye(2)
assert N == sp.Matrix([[2, 1], [-4, -2]]) and N * N == sp.zeros(2)
v = sp.Matrix([1, -2])
w = sp.Matrix([0, 1])
assert N * v == sp.zeros(2, 1) and N * w == v
P = sp.Matrix.hstack(v, w)
assert P.det() == 1 and P.inv() == sp.Matrix([[1, 0], [2, 1]])
assert A4 * P == sp.Matrix([[-2, 1], [4, -4]])
assert P.inv() * A4 * P == sp.Matrix([[-2, 1], [0, -2]])

# general solution x = c1 e^{-2t} v + c2 e^{-2t}(t v + w)
c1, c2 = sp.symbols("c1 c2")
X = c1 * sp.exp(-2 * t) * v + c2 * sp.exp(-2 * t) * (t * v + w)
assert sp.simplify(X.diff(t) - A4 * X) == sp.zeros(2, 1)
assert sp.simplify(X[0] - (c1 + c2 * t) * sp.exp(-2 * t)) == 0
assert sp.simplify(X[1] - (-2 * c1 + c2 - 2 * c2 * t) * sp.exp(-2 * t)) == 0

# IVP x(0) = 1, v(0) = v0: c1 = 1, c2 = v0 + 2
v0 = sp.symbols("v0", real=True)
sol = sp.solve([X[0].subs(t, 0) - 1, X[1].subs(t, 0) - v0], [c1, c2])
assert sol == {c1: 1, c2: v0 + 2}
xs = X[0].subs(sol)
assert sp.simplify(xs - (1 + (v0 + 2) * t) * sp.exp(-2 * t)) == 0
assert sp.simplify(xs.diff(t, 2) + 4 * xs.diff(t) + 4 * xs) == 0
# crossing time t* = -1/(v0+2) > 0 iff v0 < -2; example v0 = -6: t* = 1/4 s
assert sp.solve(sp.Eq(1 + (v0 + 2) * t, 0), t) == [-1 / (v0 + 2)]
assert (-1 / (v0 + 2)).subs(v0, -6) == sp.Rational(1, 4)
# v0 = 0: x = (1+2t)e^{-2t}, speed x' = -4t e^{-2t}, max |x'| at t = 1/2: 2/e
x0 = xs.subs(v0, 0)
assert sp.simplify(x0 - (1 + 2 * t) * sp.exp(-2 * t)) == 0
xd = sp.simplify(x0.diff(t))
assert sp.simplify(xd + 4 * t * sp.exp(-2 * t)) == 0
assert sp.solve(sp.diff(xd, t), t) == [sp.Rational(1, 2)]
assert sp.simplify(xd.subs(t, sp.Rational(1, 2)) + 2 / sp.E) == 0

print("p18 OK")
