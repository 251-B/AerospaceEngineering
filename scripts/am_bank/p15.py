"""Bank P15: x y'' - (x+2) y' + 2y = 0 with y1 = e^x; forced version with x^3 e^x. SymPy checks."""
import sympy as sp

x = sp.symbols("x", positive=True)
C, D, C1, C2 = sp.symbols("C D C1 C2")
L = lambda y: x * sp.diff(y, x, 2) - (x + 2) * sp.diff(y, x) + 2 * y

y1 = sp.exp(x)
assert sp.simplify(L(y1)) == 0
# (a) reduction: y = v e^x -> x v'' + (x - 2) v' = 0
v = sp.Function("v")
red = sp.simplify(L(v(x) * y1) / y1)
assert sp.simplify(red - (x * v(x).diff(x, 2) + (x - 2) * v(x).diff(x))) == 0
w = x**2 * sp.exp(-x)
assert sp.simplify(x * sp.diff(w, x) + (x - 2) * w) == 0
assert sp.simplify(sp.diff(-(x**2 + 2 * x + 2) * sp.exp(-x), x) - w) == 0
y2 = x**2 + 2 * x + 2
assert sp.simplify(L(y2)) == 0
W = sp.simplify(y1 * sp.diff(y2, x) - sp.diff(y1, x) * y2)
assert sp.simplify(W + x**2 * sp.exp(x)) == 0
# Abel: W = K exp(-int p), p = -(x+2)/x -> exp(x + 2 ln x) = x^2 e^x
assert sp.simplify(sp.exp(sp.integrate((x + 2) / x, x)) - x**2 * sp.exp(x)) == 0

# (b) forced: L y = x^3 e^x; reduction gives x v'' + (x-2) v' = x^3
redf = sp.simplify((L(v(x) * y1) - x**3 * sp.exp(x)) / sp.exp(x))
assert sp.simplify(redf - (x * v(x).diff(x, 2) + (x - 2) * v(x).diff(x) - x**3)) == 0
mu = sp.exp(x) / x**2
assert sp.simplify(sp.diff(mu, x) - mu * (1 - 2 / x)) == 0
wf = x**2 + C * x**2 * sp.exp(-x)
assert sp.simplify(sp.diff(wf, x) + (1 - 2 / x) * wf - x**2) == 0
vf = x**3 / 3 - C * (x**2 + 2 * x + 2) * sp.exp(-x) + D
assert sp.simplify(sp.diff(vf, x) - wf) == 0
yp = x**3 * sp.exp(x) / 3
assert sp.simplify(L(yp) - x**3 * sp.exp(x)) == 0
yg = C1 * sp.exp(x) + C2 * (x**2 + 2 * x + 2) + yp
assert sp.simplify(L(yg) - x**3 * sp.exp(x)) == 0
# variation of parameters cross-check (standard form f = x^2 e^x)
f = x**2 * sp.exp(x)
yvp = -y1 * sp.integrate(sp.simplify(y2 * f / W), x) + y2 * sp.integrate(sp.simplify(y1 * f / W), x)
assert sp.simplify(L(yvp) - x**3 * sp.exp(x)) == 0
assert sp.simplify(yvp - (yp - 2 * sp.exp(x))) == 0

# (c) singular point x = 0: every solution has y'(0) = y(0)
xs = sp.symbols("xs", real=True)
ygr = yg.subs(x, xs)
assert sp.simplify(ygr.subs(xs, 0) - sp.diff(ygr, xs).subs(xs, 0)) == 0
assert sp.simplify(ygr.subs(xs, 0) - (C1 + 2 * C2)) == 0
# IVP y(0)=1, y'(0)=1: one-parameter family; y(0)=1, y'(0)=0 impossible
# IVP at x = 1 is uniquely solvable: y(1)=0, y'(1)=0
sol = sp.solve([yg.subs(x, 1), sp.diff(yg, x).subs(x, 1)], [C1, C2], dict=True)
assert len(sol) == 1  # x = 1 is a regular point: unique solution
print("p15 OK")
