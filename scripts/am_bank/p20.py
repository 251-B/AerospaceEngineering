"""P20: Fourier series of f(x) = |sin x| on (-pi, pi), convention f ~ a0 + sum (an cos nx + bn sin nx)."""
import sympy as sp

x = sp.symbols("x", real=True)
n = sp.symbols("n", integer=True, positive=True)
k = sp.symbols("k", integer=True, positive=True)
f = sp.Abs(sp.sin(x))

a0 = sp.integrate(sp.sin(x), (x, 0, sp.pi)) / sp.pi  # (1/2pi) * 2 * int_0^pi sin
assert a0 == 2 / sp.pi
assert sp.simplify(sp.integrate(f, (x, -sp.pi, sp.pi)) / (2 * sp.pi) - a0) == 0

# product-to-sum and the two elementary integrals (n != 1)
assert sp.simplify(sp.sin(x) * sp.cos(n * x) - (sp.sin((n + 1) * x) - sp.sin((n - 1) * x)) / 2) == 0
I1 = sp.integrate(sp.sin((n + 1) * x), (x, 0, sp.pi))
assert sp.simplify(I1 - (1 + (-1) ** n) / (n + 1)) == 0
for nv in range(2, 12):
    an = sp.integrate(sp.sin(x) * sp.cos(nv * x), (x, 0, sp.pi)) * 2 / sp.pi
    expected = -4 / (sp.pi * (nv**2 - 1)) if nv % 2 == 0 else 0
    assert sp.simplify(an - expected) == 0
    # direct integration of |sin x| cos nx over (-pi, pi)
    an_direct = (sp.integrate(-sp.sin(x) * sp.cos(nv * x), (x, -sp.pi, 0)) + sp.integrate(sp.sin(x) * sp.cos(nv * x), (x, 0, sp.pi))) / sp.pi
    assert sp.simplify(an_direct - expected) == 0
a1 = sp.integrate(sp.sin(x) * sp.cos(x), (x, 0, sp.pi)) * 2 / sp.pi
assert a1 == 0
# b_n = 0 (even function)
for nv in range(1, 6):
    bn = (sp.integrate(-sp.sin(x) * sp.sin(nv * x), (x, -sp.pi, 0)) + sp.integrate(sp.sin(x) * sp.sin(nv * x), (x, 0, sp.pi))) / sp.pi
    assert sp.simplify(bn) == 0

# sums
S0 = sp.summation(1 / (4 * k**2 - 1), (k, 1, sp.oo))
assert sp.simplify(S0 - sp.Rational(1, 2)) == 0
S1 = sp.summation((-1) ** (k + 1) / (4 * k**2 - 1), (k, 1, sp.oo))
assert sp.simplify(S1 - (sp.pi - 2) / 4) == 0
# telescoping partial sum
N = sp.symbols("N", integer=True, positive=True)
SN = sp.summation(1 / (4 * k**2 - 1), (k, 1, N))
assert sp.simplify(SN - (sp.Rational(1, 2) - 1 / (2 * (2 * N + 1)))) == 0

# series at x = 0 and x = pi/2 reproduces f
import math
series = lambda xv, K: 2 / math.pi - 4 / math.pi * sum(math.cos(2 * kk * xv) / (4 * kk**2 - 1) for kk in range(1, K + 1))
assert abs(series(0, 4000) - 0) < 1e-3
assert abs(series(math.pi / 2, 4000) - 1) < 1e-6
assert abs(series(0.7, 4000) - math.sin(0.7)) < 1e-3
assert abs(series(-2.5, 4000) - abs(math.sin(-2.5))) < 1e-3

# uniform error bound: |f - S_N| <= (4/pi) * sum_{k>N} 1/(4k^2-1) = 2/(pi (2N+1))
assert sp.simplify(4 / sp.pi * (sp.Rational(1, 2) - SN) - 2 / (sp.pi * (2 * N + 1))) == 0
# N = 10 -> bound 2/(21 pi) ~ 0.0303
assert abs(sp.N(2 / (21 * sp.pi)) - 0.0303) < 1e-4
assert abs(sp.N(2 / (19 * sp.pi)) - 0.0335) < 1e-4 and sp.N(2 / (17 * sp.pi)) > 0.035
assert abs(sp.N(2 / (sp.Rational(35, 1000) * sp.pi)) - 18.19) < 0.01
# sup error attained at x = 0 for K = 9
assert abs(abs(series(0, 9)) - 2 / (19 * math.pi)) < 1e-12
assert abs(1 / 3 - 1 / 15 + 1 / 35 - 1 / 63 - 0.2794) < 1e-4 and abs((math.pi - 2) / 4 - 0.2854) < 1e-4

# Parseval check (extension): (1/pi) int |sin|^2 = 2 a0^2 + sum a_n^2 -> sum 1/(4k^2-1)^2 = (pi^2 - 8)/16
import mpmath as mp
mp.mp.dps = 30
S2 = mp.nsum(lambda kk: 1 / (4 * kk**2 - 1) ** 2, [1, mp.inf])
assert abs(S2 - (mp.pi**2 - 8) / 16) < mp.mpf(10) ** -25

print("p20 OK")
