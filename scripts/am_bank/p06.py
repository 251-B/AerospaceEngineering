"""Bank P06: inverse problem, rebuild A from one real spiral solution. SymPy checks."""
import sympy as sp

t = sp.symbols("t", real=True)
I = sp.I

# Given real solution curve
xg = sp.exp(-t) * sp.Matrix([sp.cos(2*t) - sp.sin(2*t), sp.cos(2*t) - 2*sp.sin(2*t)])

# (a) read u, w, rho, omega and rebuild A = Q J Q^{-1}
u = sp.Matrix([1, 1]); w = sp.Matrix([1, 2]); rho, om = -1, 2
assert sp.simplify(xg - sp.exp(rho*t)*(sp.cos(om*t)*u - sp.sin(om*t)*w)) == sp.zeros(2, 1)
Q = sp.Matrix.hstack(u, w)
assert Q.det() == 1
Qi = Q.inv()
assert Qi == sp.Matrix([[2, -1], [-1, 1]])
J = sp.Matrix([[rho, om], [-om, rho]])
assert Q*J == sp.Matrix([[-3, 1], [-5, 0]])
A = Q*J*Qi
assert A == sp.Matrix([[-7, 4], [-10, 5]])
# x' = A x along the given curve (the defining property)
assert sp.simplify(xg.diff(t) - A*xg) == sp.zeros(2, 1)
# second method: x'(0) and x'(pi/4)
assert xg.subs(t, 0) == sp.Matrix([1, 1]) and xg.diff(t).subs(t, 0) == sp.Matrix([-3, -5])
assert sp.simplify(xg.subs(t, sp.pi/4) / sp.exp(-sp.pi/4)) == sp.Matrix([-1, -2])
assert sp.simplify(xg.diff(t).subs(t, sp.pi/4) / sp.exp(-sp.pi/4)) == sp.Matrix([-1, 0])
assert A*sp.Matrix([1, 2]) == sp.Matrix([1, 0])
# checks: trace, det, eigenpair
lam = sp.symbols("lam")
assert sp.expand((A - lam*sp.eye(2)).det()) == lam**2 + 2*lam + 5
assert A.trace() == -2 and A.det() == 5
eta = u + I*w
assert sp.expand(A*eta - (rho + I*om)*eta) == sp.zeros(2, 1)
assert Qi*A*Q == J

# (b) second real solution, general solution, IVP x(0) = (1, 0)
x1 = xg
x2 = sp.exp(-t)*(sp.sin(2*t)*u + sp.cos(2*t)*w)
assert sp.simplify(x2 - sp.exp(-t)*sp.Matrix([sp.sin(2*t) + sp.cos(2*t), sp.sin(2*t) + 2*sp.cos(2*t)])) == sp.zeros(2, 1)
assert sp.simplify(x2.diff(t) - A*x2) == sp.zeros(2, 1)
W0 = sp.Matrix.hstack(x1.subs(t, 0), x2.subs(t, 0)).det()
assert W0 == 1
c1, c2 = 2, -1
xs = c1*x1 + c2*x2
xIVP = sp.exp(-t)*sp.Matrix([sp.cos(2*t) - 3*sp.sin(2*t), -5*sp.sin(2*t)])
assert sp.simplify(xs - xIVP) == sp.zeros(2, 1)
assert xIVP.subs(t, 0) == sp.Matrix([1, 0])
assert sp.simplify(xIVP.diff(t) - A*xIVP) == sp.zeros(2, 1)

# (c) rotation: test vector at (1,0) and cross product x*y' - y*x'
assert A*sp.Matrix([1, 0]) == sp.Matrix([-7, -10])
X, Y = sp.symbols("X Y", real=True)
v = A*sp.Matrix([X, Y])
cross = sp.expand(X*v[1] - Y*v[0])
assert cross == -10*X**2 + 12*X*Y - 4*Y**2   # = -2(5X^2-6XY+2Y^2) < 0
assert sp.expand(cross + 2*(5*X**2 - 6*X*Y + 2*Y**2)) == 0
# 5X^2-6XY+2Y^2 positive definite: 5>0, det 10-9=1>0
assert sp.Matrix([[5, -3], [-3, 2]]).det() == 1

# (d) V = |Q^{-1}x|^2 = 5x^2 - 6xy + 2y^2, dV/dt = -2V, halving time of sqrt(V) = ln 2
S = Qi.T*Qi
assert S == sp.Matrix([[5, -3], [-3, 2]])
V = sp.expand((sp.Matrix([[X, Y]])*S*sp.Matrix([X, Y]))[0])
assert V == 5*X**2 - 6*X*Y + 2*Y**2
dV = sp.expand(sp.diff(V, X)*v[0] + sp.diff(V, Y)*v[1])
assert sp.expand(dV + 2*V) == 0
VIVP = sp.simplify(V.subs({X: xIVP[0], Y: xIVP[1]}))
assert sp.simplify(VIVP - 5*sp.exp(-2*t)) == 0
th = sp.solve(sp.Eq(sp.exp(-t), sp.Rational(1, 2)), t)
assert th == [sp.log(2)]
# return to positive x-axis at t = pi, distance multiplied by e^{-pi}; negative axis at pi/2
assert sp.simplify(xIVP.subs(t, sp.pi) - sp.exp(-sp.pi)*sp.Matrix([1, 0])) == sp.zeros(2, 1)
assert sp.simplify(xIVP.subs(t, sp.pi/2) - sp.Matrix([-sp.exp(-sp.pi/2), 0])) == sp.zeros(2, 1)
# Euclidean |x|^2 is not monotone: d|x|^2/dt = 2 x^T A x indefinite
q = sp.expand((sp.Matrix([[X, Y]])*A*sp.Matrix([X, Y]))[0])
assert q == -7*X**2 - 6*X*Y + 5*Y**2 and q.subs({X: 0, Y: 1}) == 5 and q.subs({X: 1, Y: 0}) == -7
# x1' explicit
assert sp.simplify(xg.diff(t) - sp.exp(-t)*sp.Matrix([-3*sp.cos(2*t) - sp.sin(2*t), -5*sp.cos(2*t)])) == sp.zeros(2, 1)
# eigenvector from row 1 with eta1 = 1+i
lp = -1 + 2*I
assert sp.expand((-7 - lp)*(1 + I) + 4*(1 + 2*I)) == 0 and sp.expand(-10*(1 + I) + (5 - lp)*(1 + 2*I)) == 0
# first y = 0 crossing for t>0 is pi/2 (sin 2t = 0); x there negative
assert abs(float(sp.exp(-sp.pi)) - 0.0432139) < 1e-6
assert abs(float(sp.log(2)) - 0.693147) < 1e-6

print("p06 OK")
