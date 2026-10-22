"""Bank P12: heat equation u_t = k u_xx + Q with ends at T_A, T_B, source switched on at t = 0. SymPy checks."""
import math
import sympy as sp

x, t, L, k, Q = sp.symbols("x t L k Q", positive=True)
TA, TB = sp.symbols("T_A T_B", real=True)
n = sp.symbols("n", integer=True, positive=True)
pi = sp.pi

# (a) steady state
us = TA + (TB - TA) * x / L + Q * x * (L - x) / (2 * k)
assert sp.simplify(k * sp.diff(us, x, 2) + Q) == 0
assert sp.simplify(us.subs(x, 0) - TA) == 0 and sp.simplify(us.subs(x, L) - TB) == 0
assert sp.simplify(us.subs(x, L / 2) - ((TA + TB) / 2 + Q * L**2 / (8 * k))) == 0

# (b) separation: lambda<0 and lambda=0 only trivial
a, b = sp.symbols("a b")
mu = sp.symbols("mu", positive=True)
Xneg = a * sp.cosh(mu * x) + b * sp.sinh(mu * x)
sol = sp.solve([Xneg.subs(x, 0), Xneg.subs(x, L)], [a, b], dict=True)
assert sol == [{a: 0, b: 0}]
X0 = a + b * x
assert sp.solve([X0.subs(x, 0), X0.subs(x, L)], [a, b], dict=True) == [{a: 0, b: 0}]
Xn = sp.sin(n * pi * x / L)
lam = (n * pi / L) ** 2
assert sp.simplify(sp.diff(Xn, x, 2) + lam * Xn) == 0 and Xn.subs(x, L) == 0

# (c) initial v0 = u0 - us = -Q x (L - x) / (2k); its sine coefficients
u0 = TA + (TB - TA) * x / L
v0 = sp.simplify(u0 - us)
assert sp.simplify(v0 + Q * x * (L - x) / (2 * k)) == 0
cn = -4 * Q * L**2 * (1 - (-1) ** n) / (2 * k * pi**3 * n**3)  # = -4QL^2/(k pi^3 n^3) for odd n
for m in range(1, 8):
    direct = 2 / L * sp.integrate(v0 * sp.sin(m * pi * x / L), (x, 0, L))
    assert sp.simplify(direct - cn.subs(n, m)) == 0
# x(L-x) sine coefficients 8L^2/(pi^3 n^3) for odd n
for m in (1, 3, 5):
    assert sp.simplify(2 / L * sp.integrate(x * (L - x) * sp.sin(m * pi * x / L), (x, 0, L)) - 8 * L**2 / (pi**3 * m**3)) == 0
# each mode satisfies v_t = k v_xx
vn = sp.sin(n * pi * x / L) * sp.exp(-k * n**2 * pi**2 * t / L**2)
assert sp.simplify(sp.diff(vn, t) - k * sp.diff(vn, x, 2)) == 0

# midpoint at t=0 consistent: (4QL^2/(k pi^3)) * pi^3/32 = QL^2/(8k)
assert sp.simplify(4 * Q * L**2 / (k * pi**3) * pi**3 / 32 - Q * L**2 / (8 * k)) == 0

# numeric check of the series at t = 0 and t = tau1
def u_series(xv, tv, Lv=0.5, kv=1e-4, Qv=0.02, TAv=20.0, TBv=40.0, N=4001):
    s = 0.0
    for m in range(1, N + 1, 2):
        s += -4 * Qv * Lv**2 / (kv * math.pi**3 * m**3) * math.sin(m * math.pi * xv / Lv) * math.exp(-kv * m**2 * math.pi**2 * tv / Lv**2)
    return TAv + (TBv - TAv) * xv / Lv + Qv * xv * (Lv - xv) / (2 * kv) + s

assert abs(u_series(0.2, 0.0) - (20 + 20 * 0.2 / 0.5)) < 1e-6

# (d) numbers: L = 0.5 m, k = 1e-4 m^2/s, Q = 0.02 K/s, T_A = 20, T_B = 40 C
Lv, kv, Qv = 0.5, 1e-4, 0.02
tau1 = Lv**2 / (kv * math.pi**2)
assert abs(tau1 - 253.30) < 0.01
rise = Qv * Lv**2 / (8 * kv)
assert abs(rise - 6.25) < 1e-12
assert abs(us.subs({TA: 20, TB: 40, Q: Qv, L: Lv, k: kv, x: Lv / 2}) - 36.25) < 1e-9
t99 = tau1 * math.log(3200 / math.pi**3)
assert abs(math.log(3200 / math.pi**3) - 4.6367) < 1e-4
assert abs(t99 - 1174.5) < 0.2
# one-mode deficit vs the full series at t99: the n=3 term is below 1e-15 of the first
mid_full = u_series(Lv / 2, t99)
mid_steady = 30 + rise
assert abs((mid_steady - mid_full) / rise - 0.01) < 1e-9
# second mode decays 9 times faster
assert sp.simplify(((3 * pi / L) ** 2 * k) / ((pi / L) ** 2 * k) - 9) == 0
assert abs(3200 / math.pi**3 - 103.2) < 0.01 and abs(t99 / 60 - 19.6) < 0.05
assert math.exp(-8 * math.log(3200 / math.pi**3)) / 27 < 1e-17
# interior maximum of the steady state
xs_ = sp.solve(sp.diff(us, x), x)[0]
assert sp.simplify(xs_ - (L / 2 + k * (TB - TA) / (Q * L))) == 0
assert abs(float(xs_.subs({L: Lv, k: kv, Q: Qv, TA: 20, TB: 40})) - 0.45) < 1e-12
print("p12 OK")
