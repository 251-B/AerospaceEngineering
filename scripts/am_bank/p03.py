"""Bank P03: x^2 y'' - x(x+2) y' + (x+2) y = g, reduction of order, Abel, variation of parameters."""
import sympy as sp

x = sp.symbols("x", positive=True)
v = sp.Function("v")

def L(y):
    return x**2 * sp.diff(y, x, 2) - x * (x + 2) * sp.diff(y, x) + (x + 2) * y

y1 = x
assert sp.simplify(L(y1)) == 0
# reduction y = v x gives x^3 (v'' - v') = 0
red = sp.expand(L(v(x) * x))
assert sp.simplify(red - x**3 * (v(x).diff(x, 2) - v(x).diff(x))) == 0
y2 = x * sp.exp(x)
assert sp.simplify(L(y2)) == 0

# Abel: p = -(1 + 2/x), W = C exp(int (1 + 2/x)) = C x^2 e^x
p = -(1 + 2 / x)
assert sp.simplify(-x * (x + 2) / x**2 - p) == 0
W = sp.simplify(y1 * sp.diff(y2, x) - y2 * sp.diff(y1, x))
assert sp.simplify(W - x**2 * sp.exp(x)) == 0
assert sp.simplify(sp.diff(W, x) + p * W) == 0

# (c) forcing x^4: standard form g = x^2
g = x**2
I1 = sp.integrate(y2 * g / W, x)
I2 = sp.integrate(y1 * g / W, x)
assert sp.simplify(I1 - x**2 / 2) == 0
assert sp.simplify(I2 + (x + 1) * sp.exp(-x)) == 0
yp_full = sp.expand(-y1 * I1 + y2 * I2)
assert sp.simplify(yp_full - (-x**3 / 2 - x**2 - x)) == 0
yp = -x**3 / 2 - x**2
assert sp.simplify(L(yp) - x**4) == 0

# (d) IVP y(1) = 1/2, y'(1) = -1/2
Y = x + x * sp.exp(x - 1) - x**3 / 2 - x**2
assert sp.simplify(L(Y) - x**4) == 0
assert Y.subs(x, 1) == sp.Rational(1, 2)
assert sp.simplify(sp.diff(Y, x).subs(x, 1)) == -sp.Rational(1, 2)
c1, c2 = sp.symbols("c1 c2")
Gen = c1 * x + c2 * x * sp.exp(x) + yp
s = sp.solve([Gen.subs(x, 1) - sp.Rational(1, 2), sp.diff(Gen, x).subs(x, 1) + sp.Rational(1, 2)], [c1, c2])
assert s[c1] == 1 and sp.simplify(s[c2] - sp.exp(-1)) == 0
M = sp.Matrix([[y1, y2], [sp.diff(y1, x), sp.diff(y2, x)]]).subs(x, 1)
assert sp.simplify(M.det() - sp.E) == 0 and sp.simplify(W.subs(x, 1) - sp.E) == 0
assert sp.simplify(sp.limit(sp.diff(Y, x), x, 0, "+") - (1 + sp.exp(-1))) == 0
# with y_p keeping -x the IVP gives c1 = 2
s2 = sp.solve([(Gen - x).subs(x, 1) - sp.Rational(1, 2), sp.diff(Gen - x, x).subs(x, 1) + sp.Rational(1, 2)], [c1, c2])
assert s2[c1] == 2
# polynomial trial alpha x + beta gives beta (x + 2)
al, be = sp.symbols("alpha beta")
assert sp.simplify(L(al * x + be) - be * (x + 2)) == 0
print("p03 OK")
