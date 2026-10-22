"""Bank P16: x^2 y'' - x y' + 2y = x sin(ln x), boundary-value problem on [1, b]. SymPy checks."""
import math
import sympy as sp

x, b = sp.symbols("x b", positive=True)
z = sp.symbols("z", real=True)
C1, C2, A, B, beta = sp.symbols("C1 C2 A B beta")
L = lambda y: x**2 * sp.diff(y, x, 2) - x * sp.diff(y, x) + 2 * y

# (a) chain rule x = e^z: y' = Y_z / x, y'' = (Y_zz - Y_z)/x^2
Y = sp.Function("Y")
yx = Y(sp.log(x))
assert sp.simplify(sp.diff(yx, x) - sp.Subs(sp.Derivative(Y(z), z), z, sp.log(x)).doit() / x) == 0
lhs = sp.simplify(L(yx))
target = (sp.Derivative(Y(z), z, 2) - 2 * sp.Derivative(Y(z), z) + 2 * Y(z)).subs(z, sp.log(x))
assert sp.simplify(lhs - target.doit()) == 0
r = sp.symbols("r")
assert set(sp.solve(r**2 - 2 * r + 2, r)) == {1 + sp.I, 1 - sp.I}
for yh in (x * sp.cos(sp.log(x)), x * sp.sin(sp.log(x))):
    assert sp.simplify(L(yh)) == 0

# (b) resonant particular: y = e^z w -> w'' + w = sin z; w = z (A cos z + B sin z)
w = sp.Function("w")
Yz = sp.exp(z) * w(z)
shift = sp.simplify((Yz.diff(z, 2) - 2 * Yz.diff(z) + 2 * Yz) / sp.exp(z))
assert sp.simplify(shift - (w(z).diff(z, 2) + w(z))) == 0
wg = z * (A * sp.cos(z) + B * sp.sin(z))
res = sp.expand(sp.diff(wg, z, 2) + wg)
assert sp.simplify(res - (-2 * A * sp.sin(z) + 2 * B * sp.cos(z))) == 0
assert sp.solve([-2 * A - 1, 2 * B], [A, B]) == {A: sp.Rational(-1, 2), B: 0}
yp = -x * sp.log(x) * sp.cos(sp.log(x)) / 2
assert sp.simplify(L(yp) - x * sp.sin(sp.log(x))) == 0
yg = C1 * x * sp.cos(sp.log(x)) + C2 * x * sp.sin(sp.log(x)) + yp
assert sp.simplify(L(yg) - x * sp.sin(sp.log(x))) == 0

# (c) BVP y(1) = 0, y(b) = 0
assert sp.simplify(yg.subs(x, 1)) == C1
yb = yg.subs(C1, 0)
c2 = sp.solve(yb.subs(x, b), C2)[0]
assert sp.simplify(c2 - sp.log(b) * sp.cos(sp.log(b)) / (2 * sp.sin(sp.log(b)))) == 0
ysol = x / 2 * (sp.log(b) * sp.cot(sp.log(b)) * sp.sin(sp.log(x)) - sp.log(x) * sp.cos(sp.log(x)))
assert sp.simplify(L(ysol) - x * sp.sin(sp.log(x))) == 0
assert sp.simplify(ysol.subs(x, 1)) == 0 and sp.simplify(ysol.subs(x, b)) == 0
# b = e^{pi/2}: the solution is yp itself
assert sp.simplify(ysol.subs(b, sp.exp(sp.pi / 2)) - yp) == 0
# b = e^{n pi}: y(b) = C2*0 + yp(b) = (-1)^(n+1) n pi e^{n pi}/2 != 0 -> no solution with y(b)=0
for k in range(1, 5):
    bk = sp.exp(k * sp.pi)
    val = sp.simplify(yb.subs(x, bk))
    assert sp.simplify(val - (-1) ** (k + 1) * k * sp.pi * bk / 2) == 0
    assert val != 0
# solvability: y(e^pi) = beta solvable iff beta = pi e^pi / 2, then C2 free
assert sp.simplify(yb.subs(x, sp.exp(sp.pi)) - sp.pi * sp.exp(sp.pi) / 2) == 0
assert abs(float(sp.pi * sp.exp(sp.pi) / 2) - 36.35) < 0.01
# numerical: b = e (ln b = 1): C2 = cot(1)/2
assert abs(float(c2.subs(b, sp.E)) - 0.5 / math.tan(1)) < 1e-12
assert abs(0.5 / math.tan(1) - 0.32105) < 1e-5
# self-adjoint form: L[y]/x^3 = (y'/x)' + 2y/x^3
yy = sp.Function("y")(x)
assert sp.simplify(L(yy) / x**3 - (sp.diff(sp.diff(yy, x) / x, x) + 2 * yy / x**3)) == 0
# Fredholm: forcing not orthogonal to x sin(ln x) on [1, e^{n pi}]
for k in range(1, 4):
    # substitution x = e^z, dx = e^z dz: integrand sin^2(ln x)/x dx -> sin^2 z dz
    integrand = (sp.sin(sp.log(x)) / x**2 * x * sp.sin(sp.log(x))).subs(x, sp.exp(z)) * sp.exp(z)
    assert sp.simplify(integrand - sp.sin(z) ** 2) == 0
    I = sp.integrate(sp.sin(z) ** 2, (z, 0, k * sp.pi))
    assert sp.simplify(I - k * sp.pi / 2) == 0
    xn = sp.exp(k * sp.pi)
    num = sp.Integral(sp.sin(sp.log(x)) ** 2 / x, (x, 1, xn)).evalf()
    assert abs(float(num) - float(k * sp.pi / 2)) < 1e-9
# b -> 1+: ln b cot(ln b) -> 1
s = sp.symbols("s", positive=True)
assert sp.limit(s * sp.cot(s), s, 0) == 1
print("p16 OK")
