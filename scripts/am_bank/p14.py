"""Bank P14: string fixed at both ends, released from rest position with velocity g = 4V x(L-x)/L^2. SymPy checks."""
import math
import sympy as sp

x, t, L, c, V, rho = sp.symbols("x t L c V rho", positive=True)
n = sp.symbols("n", integer=True, positive=True)
pi = sp.pi
g = 4 * V * x * (L - x) / L**2

# (a) modes
wn = n * pi * c / L
mode = sp.sin(n * pi * x / L) * sp.sin(wn * t)
assert sp.simplify(sp.diff(mode, t, 2) - c**2 * sp.diff(mode, x, 2)) == 0
assert mode.subs(x, 0) == 0 and sp.simplify(mode.subs(x, L)) == 0 and mode.subs(t, 0) == 0

# (b) coefficients: sine coefficients of g are 32V/(pi^3 n^3) for odd n, 0 for even
F = sp.integrate(x * (L - x) * sp.sin(n * pi * x / L), x)
for m in range(1, 9):
    gm = 2 / L * sp.integrate(g * sp.sin(m * pi * x / L), (x, 0, L))
    assert sp.simplify(gm - (32 * V / (pi**3 * m**3) if m % 2 else 0)) == 0
Bn = 32 * V * L / (c * pi**4 * n**4)
assert sp.simplify(Bn * wn - 32 * V / (pi**3 * n**3)) == 0

N = 401
def u_series(xv, tv, Lv=1.0, cv=1.0, Vv=1.0):
    return sum(32 * Vv * Lv / (cv * math.pi**4 * m**4) * math.sin(m * math.pi * xv / Lv) * math.sin(m * math.pi * cv * tv / Lv)
               for m in range(1, N, 2))

def ut_series(xv, tv, Lv=1.0, cv=1.0, Vv=1.0):
    return sum(32 * Vv / (math.pi**3 * m**3) * math.sin(m * math.pi * xv / Lv) * math.cos(m * math.pi * cv * tv / Lv)
               for m in range(1, N, 2))

assert abs(ut_series(0.3, 0) - 4 * 0.3 * 0.7) < 1e-6

# (c) d'Alembert at the midpoint for c t <= L/2
s, sig = sp.symbols("s sigma", real=True)
um = sp.integrate(g, (x, L / 2 - c * t, L / 2 + c * t)) / (2 * c)
assert sp.simplify(um - (V * t - 4 * V * c**2 * t**3 / (3 * L**2))) == 0
assert sp.simplify(um.subs(t, L / (2 * c)) - V * L / (3 * c)) == 0
for tv in (0.1, 0.25, 0.4, 0.5):
    assert abs(u_series(0.5, tv) - (tv - 4 * tv**3 / 3)) < 1e-8
assert sp.summation(1 / (2 * n - 1) ** 4, (n, 1, sp.oo)) == pi**4 / 96
assert sp.simplify(32 * V * L / (c * pi**4) * pi**4 / 96 - V * L / (3 * c)) == 0
# at t = L/(2c) the string is at rest (cos(n pi/2) = 0 for odd n)
assert abs(ut_series(0.37, 0.5)) < 1e-12

# (d) energy E = int (rho/2 u_t^2 + T/2 u_x^2), T = rho c^2
E0 = sp.integrate(rho / 2 * g**2, (x, 0, L))
assert sp.simplify(E0 - 4 * rho * V**2 * L / 15) == 0
En = rho * L / 4 * (32 * V / (pi**3 * n**3)) ** 2
# energy of one mode computed from the definition
Bk = sp.symbols("B_k", positive=True)
k1 = 3
uk = Bk * sp.sin(k1 * pi * x / L) * sp.sin(k1 * pi * c * t / L)
Ek = sp.integrate(rho / 2 * sp.diff(uk, t) ** 2 + rho * c**2 / 2 * sp.diff(uk, x) ** 2, (x, 0, L))
assert sp.simplify(Ek - rho * L / 4 * (k1 * pi * c / L) ** 2 * Bk**2) == 0
assert sp.simplify(En.subs(n, 1) - 256 * rho * L * V**2 / pi**6) == 0
assert sp.summation(1 / (2 * n - 1) ** 6, (n, 1, sp.oo)) == pi**6 / 960
assert sp.simplify(256 * rho * L * V**2 / pi**6 * pi**6 / 960 - E0) == 0
ratio = sp.Rational(960) / pi**6
assert abs(float(ratio) - 0.998555) < 1e-6
# periodicity: T = 2L/c, at t = L/c displacement 0 and velocity -g
assert abs(u_series(0.3, 1.0)) < 1e-12 and abs(u_series(0.3, 2.0)) < 1e-12
assert abs(ut_series(0.3, 1.0) + 4 * 0.3 * 0.7) < 1e-6
assert abs(u_series(0.3, 0.7) - u_series(0.3, 2.7)) < 1e-12
# symmetry u(x, L/c - t) = u(x, t)
assert abs(u_series(0.3, 0.2) - u_series(0.3, 0.8)) < 1e-12
assert abs(u_series(0.3, 0.4 + 1.0) + u_series(0.3, 0.4)) < 1e-12   # u(x, t + L/c) = -u(x, t)
assert sp.simplify(sp.integrate(x**2 * (L - x) ** 2, (x, 0, L)) - L**5 / 30) == 0
assert abs(u_series(0.5, 0.5) - 1 / 3) < 1e-8   # max midpoint displacement VL/(3c)
# small-t: u ~ t g(x)
assert abs(u_series(0.3, 1e-4) / 1e-4 - 4 * 0.3 * 0.7) < 1e-4
print("p14 OK")
