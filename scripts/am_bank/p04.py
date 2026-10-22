"""Bank P04: inverse problem y'' + a y' + b y = f, resonance and the modified guess."""
import sympy as sp

x, a, b, k, A, B, w = sp.symbols("x a b k A B omega", real=True)

def L(y, a=2, b=5):
    return sp.diff(y, x, 2) + a * sp.diff(y, x) + b * y

# (a) e^{-x} cos 2x solves the homogeneous equation -> a = 2, b = 5
yh = sp.exp(-x) * sp.cos(2 * x)
expr = sp.expand(sp.simplify(L(yh, a, b) / sp.exp(-x)))
eqs = [expr.coeff(sp.cos(2 * x)), expr.coeff(sp.sin(2 * x))]
assert sp.solve(eqs, [a, b]) == {a: 2, b: 5}
r = sp.symbols("r")
assert sp.solve(r**2 + 2 * r + 5, r) == [-1 - 2 * sp.I, -1 + 2 * sp.I]
# y_p = 5x - 2 solves with f = kx -> k = 25
assert sp.expand(L(5 * x - 2)) == 25 * x
# undetermined-coefficient derivation of y_p for f = 25x
sol = sp.solve(sp.Poly(sp.expand(L(A * x + B) - 25 * x), x).coeffs(), [A, B])
assert sol == {A: 5, B: -2}

# (b) resonant forcing 8 e^{-x} sin 2x: modified guess x e^{-x}(A cos 2x + B sin 2x)
u = sp.Function("u")
shift = sp.simplify(L(sp.exp(-x) * u(x)) / sp.exp(-x))
assert sp.simplify(shift - (u(x).diff(x, 2) + 4 * u(x))) == 0
ug = x * (A * sp.cos(2 * x) + B * sp.sin(2 * x))
res = sp.expand(sp.diff(ug, x, 2) + 4 * ug)
assert sp.simplify(res - (4 * B * sp.cos(2 * x) - 4 * A * sp.sin(2 * x))) == 0
yp = -2 * x * sp.exp(-x) * sp.cos(2 * x)
assert sp.simplify(L(yp) - 8 * sp.exp(-x) * sp.sin(2 * x)) == 0
# the unmodified guess fails: it is annihilated
assert sp.simplify(L(sp.exp(-x) * (A * sp.cos(2 * x) + B * sp.sin(2 * x)))) == 0

# (c) IVP y(0) = 1, y'(0) = -3
Y = sp.exp(-x) * (1 - 2 * x) * sp.cos(2 * x)
assert sp.simplify(L(Y) - 8 * sp.exp(-x) * sp.sin(2 * x)) == 0
assert Y.subs(x, 0) == 1 and sp.diff(Y, x).subs(x, 0) == -3
c1, c2 = sp.symbols("c1 c2")
G = sp.exp(-x) * (c1 * sp.cos(2 * x) + c2 * sp.sin(2 * x)) + yp
s = sp.solve([G.subs(x, 0) - 1, sp.diff(G, x).subs(x, 0) + 3], [c1, c2])
assert s == {c1: 1, c2: 0}
assert sp.limit(Y, x, sp.oo) == 0

# (d) pure cos(omega x) forcing: never resonant; amplitude 1/sqrt((5-w^2)^2 + 4 w^2)
yc = A * sp.cos(w * x) + B * sp.sin(w * x)
e = sp.expand(L(yc) - sp.cos(w * x))
sc = sp.solve([e.coeff(sp.cos(w * x)), e.coeff(sp.sin(w * x))], [A, B])
assert sp.simplify(sc[A] - (5 - w**2) / ((5 - w**2) ** 2 + 4 * w**2)) == 0
assert sp.simplify(sc[B] - 2 * w / ((5 - w**2) ** 2 + 4 * w**2)) == 0
D = (5 - w**2) ** 2 + 4 * w**2
assert sp.simplify(sp.expand(D) - (w**4 - 6 * w**2 + 25)) == 0
assert sp.simplify(sp.expand(D) - ((w**2 - 3) ** 2 + 16)) == 0
crit = [c for c in sp.solve(sp.diff(D, w), w) if c.is_positive]
assert crit == [sp.sqrt(3)]
assert sp.sqrt(D.subs(w, sp.sqrt(3))) == 4  # peak amplitude 1/4
assert sp.sqrt(D.subs(w, 0)) == 5  # static response 1/5
# derivatives written in step 1 of (a) and the bracket of step 2
assert sp.simplify(sp.diff(yh, x) - sp.exp(-x) * (-sp.cos(2 * x) - 2 * sp.sin(2 * x))) == 0
assert sp.simplify(sp.diff(yh, x, 2) - sp.exp(-x) * (-3 * sp.cos(2 * x) + 4 * sp.sin(2 * x))) == 0
assert sp.simplify(L(yh, a, b) - sp.exp(-x) * ((-3 - a + b) * sp.cos(2 * x) + (4 - 2 * a) * sp.sin(2 * x))) == 0
# 5x - 2 with general a, b: 5b x + (5a - 2b)
assert sp.expand(L(5 * x - 2, a, b)) == sp.expand(5 * b * x + 5 * a - 2 * b)
print("p04 OK")
