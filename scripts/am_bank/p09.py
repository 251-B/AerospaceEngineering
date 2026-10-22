"""Bank P09: x'' = 4x - x^3, V = x^4/4 - 2x^2. SymPy checks."""
import sympy as sp

x, y, t, E, lam = sp.symbols("x y t E lam", real=True)
V = x**4/4 - 2*x**2
Vp = sp.diff(V, x)
assert sp.expand(Vp - (x**3 - 4*x)) == 0
F = sp.Matrix([y, -Vp])
eqs = sp.solve(list(F), [x, y], dict=True)
assert {(e[x], e[y]) for e in eqs} == {(0, 0), (2, 0), (-2, 0)}
assert V.subs(x, 0) == 0 and V.subs(x, 2) == -4 and V.subs(x, -2) == -4
Vpp = sp.diff(V, x, 2); assert sp.expand(Vpp - (3*x**2 - 4)) == 0
Jac = F.jacobian([x, y])
J0 = Jac.subs({x: 0, y: 0}); assert J0 == sp.Matrix([[0, 1], [4, 0]])
assert J0.eigenvals() == {2: 1, -2: 1}
assert J0*sp.Matrix([1, 2]) == 2*sp.Matrix([1, 2]) and J0*sp.Matrix([1, -2]) == -2*sp.Matrix([1, -2])
J2 = Jac.subs({x: 2, y: 0}); assert J2 == sp.Matrix([[0, 1], [-8, 0]])
assert J2.eigenvals() == {2*sp.sqrt(2)*sp.I: 1, -2*sp.sqrt(2)*sp.I: 1}
assert Jac.subs({x: -2, y: 0}) == J2
assert sp.expand((J2 - lam*sp.eye(2)).det()) == lam**2 + 8

# first integral
H = y**2/2 + V
dH = sp.expand(sp.diff(H, x)*F[0] + sp.diff(H, y)*F[1])
assert dH == 0
# Hessian at centres positive definite
Hes = sp.hessian(H, (x, y)).subs({x: 2, y: 0}); assert Hes == sp.diag(8, 1)
# rotation at centre (2,0): at (2,1) x' = 1 > 0  -> clockwise
assert F.subs({x: 2, y: 1}) == sp.Matrix([1, 0])
# small-oscillation period 2*pi/sqrt(8) = pi/sqrt(2)
assert sp.simplify(2*sp.pi/sp.sqrt(8) - sp.pi/sp.sqrt(2)) == 0

# separatrix E = 0: y^2 = x^2(8 - x^2)/2
assert sp.expand(-2*V - x**2*(8 - x**2)/2) == 0
assert set(sp.solve(sp.Eq(V, 0), x)) == {-2*sp.sqrt(2), 0, 2*sp.sqrt(2)}
# max |y| on separatrix at x = 2: y^2 = 8
g = x**2*(8 - x**2)/2
assert sp.solve(sp.diff(g, x), x) == [-2, 0, 2] and g.subs(x, 2) == 8
# homoclinic solution x = 2 sqrt2 sech(2t)
xh = 2*sp.sqrt(2)/sp.cosh(2*t)
res = sp.simplify((sp.diff(xh, t, 2) - 4*xh + xh**3).rewrite(sp.exp))
assert res == 0
assert sp.simplify((sp.diff(xh, t)**2/2 + V.subs(x, xh)).rewrite(sp.exp)) == 0
assert xh.subs(t, 0) == 2*sp.sqrt(2) and sp.limit(xh, t, sp.oo) == 0
yh = sp.diff(xh, t)
assert sp.simplify(yh + 4*sp.sqrt(2)*sp.tanh(2*t)/sp.cosh(2*t)) == 0
# max |y| on the loop: y = -4 sqrt2 sech tanh, max at sech^2 = 1/2 -> |y| = 2 sqrt2
s = sp.symbols("s", positive=True)
h = 4*sp.sqrt(2)*s*sp.sqrt(1 - s**2)
assert sp.solve(sp.diff(h, s), s) == [1/sp.sqrt(2)] and sp.simplify(h.subs(s, 1/sp.sqrt(2))) == 2*sp.sqrt(2)

# turning points V(x) = E: x^2 = 4 +- 2 sqrt(4+E)
X2 = sp.symbols("X2")
roots = sp.solve(sp.Eq(X2**2/4 - 2*X2, E), X2)
assert set(sp.simplify(r) for r in roots) == {4 - 2*sp.sqrt(E + 4), 4 + 2*sp.sqrt(E + 4)}
# example E = -3: x^2 = 2 or 6
assert {r.subs(E, -3) for r in roots} == {2, 6}
assert V.subs(x, sp.sqrt(2)) == -3 and V.subs(x, sp.sqrt(6)) == -3
# example E = 5 (outer orbit): x^2 = 4 + 6 = 10, crosses x = 0 at y = +-sqrt(10)
assert V.subs(x, sp.sqrt(10)) == 5 and sp.solve(sp.Eq(y**2/2, 5), y) == [-sp.sqrt(10), sp.sqrt(10)]

# period near the centre tends to pi/sqrt2 (numerical quadrature, E = -4 + 1e-4)
import mpmath as mp
def period(Ev):
    xm = mp.sqrt(4 - 2*mp.sqrt(4 + Ev)); xp = mp.sqrt(4 + 2*mp.sqrt(4 + Ev))
    Vf = lambda s: s**4/4 - 2*s**2
    # factor E - V = (x^2 - xm^2)(xp^2 - x^2)/4 to avoid cancellation at the turning points
    return 2*mp.quad(lambda s: 1/mp.sqrt((s**2 - xm**2)*(xp**2 - s**2)/2), [xm, 2, xp])
assert abs(period(mp.mpf(-4) + mp.mpf("1e-4")) - mp.pi/mp.sqrt(2)) < 1e-3
# period grows as E -> 0^-
assert period(mp.mpf("-1e-3")) > period(mp.mpf("-0.1")) > period(mp.mpf(-2))
# amplitude for large E ~ (4E)^(1/4)
Eb = sp.Integer(10)**8
assert abs(float(sp.sqrt(4 + 2*sp.sqrt(4 + Eb)))/float((4*Eb)**sp.Rational(1, 4)) - 1) < 1e-3
print("p09 OK")
