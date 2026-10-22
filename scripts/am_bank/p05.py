"""Bank P05: x' = A(a) x with A = [[-4, a], [1, 0]]."""
import sympy as sp

a, lam, t = sp.symbols("a lambda t", real=True)
A = sp.Matrix([[-4, a], [1, 0]])
assert A.trace() == -4 and A.det() == -a
cp = sp.expand((A - lam * sp.eye(2)).det())
assert cp == lam**2 + 4 * lam - a
assert sp.expand(A.trace() ** 2 - 4 * A.det()) == 16 + 4 * a
assert set(sp.solve(cp, lam)) == {-2 + sp.sqrt(a + 4), -2 - sp.sqrt(a + 4)}

# a = 0: eigenvalues 0, -4; line of equilibria x1 = 0
A0 = A.subs(a, 0)
assert set(A0.eigenvals()) == {0, -4}
assert A0.nullspace()[0] == sp.Matrix([0, 1])
assert (A0 * sp.Matrix([-4, 1])) == -4 * sp.Matrix([-4, 1])
# a = -4: repeated -2, single eigenvector (2, -1)
A4 = A.subs(a, -4)
assert A4.eigenvals() == {-2: 2}
ns = (A4 + 2 * sp.eye(2)).nullspace()
assert len(ns) == 1 and ns[0] == sp.Matrix([-2, 1])
# sample values for every type
assert A.subs(a, 5).det() < 0                    # saddle
assert set(A.subs(a, -3).eigenvals()) == {-1, -3}  # stable node
ev8 = set(A.subs(a, -8).eigenvals())
assert ev8 == {-2 + 2 * sp.I, -2 - 2 * sp.I}       # stable focus

# (b) a = -3
A3 = A.subs(a, -3)
v1 = sp.Matrix([1, -1]); v2 = sp.Matrix([3, -1])
assert A3 * v1 == -1 * v1 and A3 * v2 == -3 * v2
P = sp.Matrix.hstack(v1, v2)
assert P.det() == 2
assert P.inv() == sp.Matrix([[-sp.Rational(1, 2), -sp.Rational(3, 2)], [sp.Rational(1, 2), sp.Rational(1, 2)]])
assert A3 * P == sp.Matrix([[-1, -9], [1, 3]])
assert P.inv() * A3 * P == sp.diag(-1, -3)
c1, c2 = sp.symbols("c1 c2")
X = c1 * sp.exp(-t) * v1 + c2 * sp.exp(-3 * t) * v2
assert sp.simplify(X.diff(t) - A3 * X) == sp.zeros(2, 1)
# IVP x(0) = (1, 1): z0 = P^{-1} x0 = (-2, 1)
z0 = P.inv() * sp.Matrix([1, 1])
assert z0 == sp.Matrix([-2, 1])
Xi = -2 * sp.exp(-t) * v1 + sp.exp(-3 * t) * v2
assert Xi.subs(t, 0) == sp.Matrix([1, 1])
assert sp.simplify(Xi - sp.Matrix([-2 * sp.exp(-t) + 3 * sp.exp(-3 * t), 2 * sp.exp(-t) - sp.exp(-3 * t)])) == sp.zeros(2, 1)
# nullclines: x1' = 0 on -4x1 - 3x2 = 0, x2' = 0 on x1 = 0

# (c) a = -8
A8 = A.subs(a, -8)
L1 = -2 + 2 * sp.I
v = sp.Matrix([L1, 1])
assert sp.simplify(A8 * v - L1 * v) == sp.zeros(2, 1)
u = sp.Matrix([-2, 1]); w = sp.Matrix([2, 0])
rho, om = -2, 2
assert A8 * u == rho * u - om * w and A8 * w == om * u + rho * w
Q = sp.Matrix.hstack(u, w)
assert Q.det() == -2
assert Q.inv() == sp.Matrix([[0, 1], [sp.Rational(1, 2), 1]])
assert A8 * Q == sp.Matrix([[0, -8], [-2, 2]])
assert Q.inv() * A8 * Q == sp.Matrix([[-2, 2], [-2, -2]])
x0 = sp.Matrix([0, 1])
zz = Q.inv() * x0
assert zz == sp.Matrix([1, 1])
c, s = sp.cos(2 * t), sp.sin(2 * t)
Xc = sp.exp(-2 * t) * ((zz[0] * c + zz[1] * s) * u + (zz[1] * c - zz[0] * s) * w)
assert sp.simplify(Xc - sp.exp(-2 * t) * sp.Matrix([-4 * s, c + s])) == sp.zeros(2, 1)
assert sp.simplify(Xc.diff(t) - A8 * Xc) == sp.zeros(2, 1)
assert Xc.subs(t, 0) == x0
# general real solution
a1, b1 = sp.symbols("a1 b1")
Xg = sp.exp(-2 * t) * ((a1 * c + b1 * s) * u + (b1 * c - a1 * s) * w)
assert sp.simplify(Xg.diff(t) - A8 * Xg) == sp.zeros(2, 1)
# rotation: at (1, 0) the velocity is (-4, 1): anticlockwise
assert A8 * sp.Matrix([1, 0]) == sp.Matrix([-4, 1])
# radius factor per turn e^{2 pi rho/omega} = e^{-2 pi}
assert sp.exp(2 * sp.pi * rho / om) == sp.exp(-2 * sp.pi)
# first crossing of the x2 axis after t=0... x1 = -4 e^{-2t} sin 2t = 0 at t = pi/2: x2 = -e^{-pi}
assert sp.simplify(Xc.subs(t, sp.pi / 2) - sp.Matrix([0, -sp.exp(-sp.pi)])) == sp.zeros(2, 1)
D3 = P.inv() * A3 * P
assert D3.trace() == -4 and D3.det() == 3
J8 = Q.inv() * A8 * Q
assert J8.trace() == -4 and J8.det() == 8
# nullclines for a = -3 and the a = 0 slope
x1, x2 = sp.symbols("x1 x2")
assert sp.solve((A3 * sp.Matrix([x1, x2]))[0], x2) == [-4 * x1 / 3]
assert (A3 * sp.Matrix([0, x2]))[0] == -3 * x2
assert (A0 * sp.Matrix([x1, x2])) == sp.Matrix([-4 * x1, x1])
# x1 < 0 just after t = 0 on the focus orbit
assert Xc[0].subs(t, sp.Rational(1, 10)).evalf() < 0
assert abs(float(sp.exp(-2 * sp.pi)) - 0.0019) < 1e-4
print("p05 OK")
