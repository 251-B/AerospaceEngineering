"""P22: u_t = k u_xx on (0,L), u_x(0,t) = u_x(L,t) = 0, u(x,0) = 20 + 40 cos^4(pi x / (2L))."""
import math
import sympy as sp

x, t, k, L = sp.symbols("x t k L", positive=True)
th = sp.symbols("theta", real=True)

# cos^4 identity
assert sp.simplify(sp.cos(th) ** 4 - (3 + 4 * sp.cos(2 * th) + sp.cos(4 * th)) / 8) == 0
f = 20 + 40 * sp.cos(sp.pi * x / (2 * L)) ** 4
f_cos = 35 + 20 * sp.cos(sp.pi * x / L) + 5 * sp.cos(2 * sp.pi * x / L)
assert sp.simplify(sp.expand_trig(f - f_cos)) == 0 or abs(sp.N((f - f_cos).subs({x: 0.37, L: 1.3}))) < 1e-12
for xv in (0, 0.1, 0.25, 0.4, 0.5):
    assert abs(sp.N((f - f_cos).subs({L: sp.Rational(1, 2), x: xv}))) < 1e-12

# Neumann eigenfunctions cos(n pi x / L), lambda_n = (n pi / L)^2, n = 0, 1, ...
n = sp.symbols("n", integer=True, nonnegative=True)
X = sp.cos(n * sp.pi * x / L)
assert sp.simplify(sp.diff(X, x).subs(x, 0)) == 0 and sp.simplify(sp.diff(X, x).subs(x, L)) == 0

u = 35 + 20 * sp.exp(-k * sp.pi**2 * t / L**2) * sp.cos(sp.pi * x / L) + 5 * sp.exp(-4 * k * sp.pi**2 * t / L**2) * sp.cos(2 * sp.pi * x / L)
assert sp.simplify(sp.diff(u, t) - k * sp.diff(u, x, 2)) == 0
assert sp.simplify(sp.diff(u, x).subs(x, 0)) == 0 and sp.simplify(sp.diff(u, x).subs(x, L)) == 0
assert sp.simplify(u.subs(t, 0) - f_cos) == 0

# coefficients by integration: A0 = (1/L) int f, An = (2/L) int f cos
A0 = sp.integrate(f_cos, (x, 0, L)) / L
assert sp.simplify(A0 - 35) == 0
for nv, expected in [(1, 20), (2, 5), (3, 0), (4, 0)]:
    An = 2 / L * sp.integrate(f_cos * sp.cos(nv * sp.pi * x / L), (x, 0, L))
    assert sp.simplify(An - expected) == 0
# with the original cos^4 form, numerically for L = 1/2
fl = f.subs(L, sp.Rational(1, 2))
assert abs(sp.N(2 * sp.Integral(fl, (x, 0, sp.Rational(1, 2)))) - 35) < 1e-10
assert abs(sp.N(4 * sp.Integral(fl * sp.cos(2 * sp.pi * x), (x, 0, sp.Rational(1, 2)))) - 20) < 1e-10
assert abs(sp.N(4 * sp.Integral(fl * sp.cos(4 * sp.pi * x), (x, 0, sp.Rational(1, 2)))) - 5) < 1e-10

# conservation of heat
H = sp.integrate(u, (x, 0, L))
assert sp.simplify(H - 35 * L) == 0
assert sp.limit(u, t, sp.oo) == 35

# initial values
assert sp.simplify(f.subs(x, 0) - 60) == 0 and sp.simplify(f.subs(x, L) - 20) == 0
assert sp.simplify(f.subs(x, L / 2) - 30) == 0
assert sp.simplify(u.subs(x, L / 2) - (35 - 5 * sp.exp(-4 * k * sp.pi**2 * t / L**2))) == 0

# numbers: L = 0.5 m, k = 1e-4 m^2/s
Lv, kv = 0.5, 1e-4
t10 = Lv**2 * math.log(10) / (4 * math.pi**2 * kv)
assert abs(t10 - 145.8) < 0.05
tau1 = Lv**2 / (math.pi**2 * kv)
assert abs(tau1 - 253.3) < 0.05
assert abs(tau1 / 4 - 63.3) < 0.05
assert abs(4 * t10 - 583.3) < 0.05 and abs(math.exp(-t10 / tau1) - 10 ** -0.25) < 1e-12 and abs(10 ** -0.25 - 0.5623) < 1e-4
uf = sp.lambdify((x, t), u.subs({L: Lv, k: kv}))
assert abs(uf(Lv / 2, t10) - (35 - 0.5)) < 1e-9
# end temperatures at t10
assert abs(uf(0, t10) - (35 + 20 * math.exp(-t10 / tau1) + 0.5)) < 1e-9
assert abs(uf(0, t10) - 46.75) < 0.01 and abs(uf(Lv, t10) - 24.25) < 0.01

print("p22 OK")
