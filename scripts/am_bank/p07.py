"""Bank P07: x' = A x + f with a repeated eigenvalue, constant forcing. SymPy checks."""
import sympy as sp

t, lam = sp.symbols("t lam")
A = sp.Matrix([[-1, 1], [-1, -3]])
f = sp.Matrix([0, 4])

# (a) eigenvalue, eigenvector, generalised eigenvector, Jordan form
assert sp.expand((A - lam*sp.eye(2)).det()) == lam**2 + 4*lam + 4
N = A + 2*sp.eye(2)
assert N == sp.Matrix([[1, 1], [-1, -1]]) and N.rank() == 1 and N**2 == sp.zeros(2)
v = sp.Matrix([1, -1]); w = sp.Matrix([1, 0])
assert N*v == sp.zeros(2, 1) and N*w == v
P = sp.Matrix.hstack(v, w)
assert P.det() == 1
Pi = P.inv()
assert Pi == sp.Matrix([[0, -1], [1, 1]])
assert A*P == sp.Matrix([[-2, -1], [2, -1]])
assert P*sp.Matrix([[-2, 1], [0, -2]]) == A*P
Jd = sp.Matrix([[-2, 1], [0, -2]])
assert Pi*A*P == Jd

# (b) equilibrium by undetermined constant vector, general solution
c = sp.Matrix(sp.symbols("p q"))
sol = sp.solve(list(A*c + f), list(c))
xs = sp.Matrix([sol[c[0]], sol[c[1]]])
assert xs == sp.Matrix([1, 1])
C1, C2 = sp.symbols("C1 C2")
xgen = xs + C1*sp.exp(-2*t)*v + C2*sp.exp(-2*t)*(t*v + w)
assert sp.simplify(xgen.diff(t) - A*xgen - f) == sp.zeros(2, 1)
assert sp.simplify(xgen - sp.Matrix([1 + (C1 + C2 + C2*t)*sp.exp(-2*t), 1 - (C1 + C2*t)*sp.exp(-2*t)])) == sp.zeros(2, 1)
# fundamental matrix Wronskian at t=0 equals det P
Phi = sp.Matrix.hstack(sp.exp(-2*t)*v, sp.exp(-2*t)*(t*v + w))
assert sp.simplify(Phi.det()) == sp.exp(-4*t)
# via Jordan coordinates z' = J z, z = P^{-1}(x - x*)
z = sp.Matrix([C1*sp.exp(-2*t) + C2*t*sp.exp(-2*t), C2*sp.exp(-2*t)])
assert sp.simplify(z.diff(t) - Jd*z) == sp.zeros(2, 1)
assert sp.simplify(P*z - (xgen - xs)) == sp.zeros(2, 1)

# (c) IVP x(0) = (3, 0)
x0 = sp.Matrix([3, 0])
cs = sp.solve(list(xgen.subs(t, 0) - x0), [C1, C2])
assert cs == {C1: 1, C2: 1}
xI = sp.Matrix([1 + (2 + t)*sp.exp(-2*t), 1 - (1 + t)*sp.exp(-2*t)])
assert sp.simplify(xgen.subs(cs) - xI) == sp.zeros(2, 1)
assert xI.subs(t, 0) == x0
assert sp.simplify(xI.diff(t) - A*xI - f) == sp.zeros(2, 1)
# deviation never on the eigenline: u1 + u2 = e^{-2t} != 0
u = xI - xs
assert sp.simplify(u[0] + u[1] - sp.exp(-2*t)) == 0
# direction for t -> +oo and -oo is along v (ratio u2/u1 -> -1)
r = sp.simplify(u[1]/u[0])
assert sp.limit(r, t, sp.oo) == -1 and sp.limit(r, t, -sp.oo) == -1
# x-component of deviation vanishes at t = -2 (before the initial time)
assert sp.solve(sp.Eq(2 + t, 0), t) == [-2]
# deviation y-component zero at t = -1
assert sp.solve(sp.Eq(1 + t, 0), t) == [-1]
# value at t = 1
assert sp.simplify(xI.subs(t, 1) - sp.Matrix([1 + 3*sp.exp(-2), 1 - 2*sp.exp(-2)])) == sp.zeros(2, 1)

# (d) classification, turning sense (cross product of deviation u and u' = A u)
X, Y = sp.symbols("X Y", real=True)
uu = sp.Matrix([X, Y]); du = A*uu
cr = sp.expand(X*du[1] - Y*du[0])
assert cr == -(X + Y)**2 or sp.expand(cr + (X + Y)**2) == 0
# test vector at u = w = (1,0)
assert A*w == sp.Matrix([-1, -1])
# nullclines through x*: x' = 0 on y = x ; y' = 0 on x + 3y = 4
assert sp.expand((A*sp.Matrix([X, X]) + f)[0]) == 0
assert sp.expand((A*sp.Matrix([4 - 3*Y, Y]) + f)[1]) == 0
# field at (3,0): x' = -3, y' = 1
assert A*sp.Matrix([3, 0]) + f == sp.Matrix([-3, 1])
# IVP derivatives
assert sp.simplify(xI.diff(t) - sp.Matrix([-(3 + 2*t)*sp.exp(-2*t), (1 + 2*t)*sp.exp(-2*t)])) == sp.zeros(2, 1)
# trace-determinant: tr^2 - 4 det = 0
assert A.trace()**2 - 4*A.det() == 0 and A.trace() == -4 and A.det() == 4

print("p07 OK")
