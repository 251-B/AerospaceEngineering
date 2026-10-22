"""Bank P01: two brine tanks in cascade. SymPy checks of every result in the note."""
import sympy as sp

t, kA, kB, k, x0 = sp.symbols("t k_A k_B k x_0", positive=True)

# (b) tank A by separation, tank B by integrating factor (different rates)
x = x0 * sp.exp(-kA * t)
assert sp.simplify(sp.diff(x, t) + kA * x) == 0 and x.subs(t, 0) == x0
y = x0 * kA / (kB - kA) * (sp.exp(-kA * t) - sp.exp(-kB * t))
assert sp.simplify(sp.diff(y, t) - (kA * x - kB * y)) == 0 and sp.simplify(y.subs(t, 0)) == 0
# integrating-factor integral: int_0^t kA x0 e^{(kB-kA)s} ds
s = sp.symbols("s", positive=True)
I = sp.integrate(kA * x0 * sp.exp((kB - kA) * s), (s, 0, t), conds="none")
assert sp.simplify(I * sp.exp(-kB * t) - y) == 0

# (c) equal rates: resonant case, and limit kB -> kA of the general formula
ye = x0 * k * t * sp.exp(-k * t)
xe = x0 * sp.exp(-k * t)
assert sp.simplify(sp.diff(ye, t) - (k * xe - k * ye)) == 0 and ye.subs(t, 0) == 0
lim = sp.limit(y.subs(kA, k), kB, k)
assert sp.simplify(lim - ye) == 0
tm = sp.solve(sp.diff(ye, t), t)
assert tm == [1 / k]
assert sp.simplify(ye.subs(t, 1 / k) - x0 / sp.E) == 0

# numbers: x0 = 20 kg, r = 10 L/min, V_A = V_B = 100 L  -> k = 0.1 /min
yn = ye.subs({x0: 20, k: sp.Rational(1, 10)})
assert sp.simplify(yn - 2 * t * sp.exp(-t / 10)) == 0
assert sp.simplify(yn.subs(t, 10) - 20 / sp.E) == 0
assert abs(float(20 / sp.E) - 7.358) < 1e-3

# (d) V_A = 100 L, V_B = 50 L: kA = 1/10, kB = 1/5
yd = y.subs({x0: 20, kA: sp.Rational(1, 10), kB: sp.Rational(1, 5)})
assert sp.simplify(yd - 20 * (sp.exp(-t / 10) - sp.exp(-t / 5))) == 0
td = 10 * sp.log(2)
assert sp.simplify(sp.diff(yd, t).subs(t, td)) == 0
assert sp.simplify(yd.subs(t, td)) == 5
assert sp.diff(yd, t, 2).subs(t, td).evalf() < 0
assert abs(float(td) - 6.931) < 1e-3
# general maximum time ln(kB/kA)/(kB-kA) and value x0 (kA/kB)^{kB/(kB-kA)}
tg = sp.log(kB / kA) / (kB - kA)
for va, vb in [(1, 2), (1, 3), (sp.Rational(1, 10), sp.Rational(1, 5))]:
    d = sp.diff(y, t).subs(t, tg).subs({kA: va, kB: vb})
    assert sp.simplify(sp.expand_log(d, force=True)) == 0 or abs(float(d.subs(x0, 1))) < 1e-14
    val = y.subs(t, tg).subs({kA: va, kB: vb})
    assert abs(float((val - x0 * (sp.Rational(va) / vb) ** (vb / (vb - va))).subs(x0, 1))) < 1e-14
assert td == tg.subs({kA: sp.Rational(1, 10), kB: sp.Rational(1, 5)})
assert sp.simplify(y.subs(t, tg).subs({kA: 1, kB: 2}) - x0 / 4) == 0
# long time: both -> 0; all salt leaves through B
assert sp.limit(yd, t, sp.oo) == 0
assert sp.integrate(sp.Rational(1, 5) * yd, (t, 0, sp.oo)) == 20
assert sp.integrate(k * ye, (t, 0, sp.oo)) == x0
# concentration in B at the maximum (case d): 5 kg / 50 L = 0.1 kg/L
assert sp.Rational(5, 50) == sp.Rational(1, 10)
print("p01 OK")
