"""Bank P11: half-range sine and cosine series of f(x) = x^2 on (0, pi). SymPy checks of every result in the note."""
import math
import sympy as sp

x = sp.symbols("x", real=True)
n = sp.symbols("n", integer=True, positive=True)
pi = sp.pi
f = x**2

# (a) sine series: antiderivative by parts and the coefficient formula
F = -x**2 * sp.cos(n * x) / n + 2 * x * sp.sin(n * x) / n**2 + 2 * sp.cos(n * x) / n**3
assert sp.simplify(sp.diff(F, x) - x**2 * sp.sin(n * x)) == 0
bn = 2 * pi * (-1) ** (n + 1) / n + 4 * ((-1) ** n - 1) / (pi * n**3)
for k in range(1, 9):
    direct = 2 / pi * sp.integrate(f * sp.sin(k * x), (x, 0, pi))
    assert sp.simplify(direct - bn.subs(n, k)) == 0
    odd = 2 * pi / k - 8 / (pi * k**3)
    even = -2 * pi / k
    assert sp.simplify(bn.subs(n, k) - (odd if k % 2 else even)) == 0
assert sp.simplify(bn.subs(n, 1) - (2 * pi - 8 / pi)) == 0
assert sp.simplify(bn.subs(n, 2) + pi) == 0

# (b) cosine series
G = x**2 * sp.sin(n * x) / n + 2 * x * sp.cos(n * x) / n**2 - 2 * sp.sin(n * x) / n**3
assert sp.simplify(sp.diff(G, x) - x**2 * sp.cos(n * x)) == 0
a0 = 2 / pi * sp.integrate(f, (x, 0, pi))
assert sp.simplify(a0 - 2 * pi**2 / 3) == 0
an = 4 * (-1) ** n / n**2
for k in range(1, 9):
    direct = 2 / pi * sp.integrate(f * sp.cos(k * x), (x, 0, pi))
    assert sp.simplify(direct - an.subs(n, k)) == 0


def S(xv, N=200000):
    """Sine series partial sum (float)."""
    s = 0.0
    for k in range(1, N + 1):
        b = 2 * math.pi * (-1) ** (k + 1) / k + 4 * ((-1) ** k - 1) / (math.pi * k**3)
        s += b * math.sin(k * xv)
    return s


def C(xv, N=20000):
    return math.pi**2 / 3 + sum(4 * (-1) ** k / k**2 * math.cos(k * xv) for k in range(1, N + 1))


# (c) values of the two series
P = math.pi
assert abs(S(P / 3) - (P / 3) ** 2) < 1e-3                 # interior point
assert abs(S(P)) < 1e-6                                    # midpoint of the jump pi^2 / -pi^2
assert abs(S(-P / 2) + P**2 / 4) < 1e-3                     # odd extension
assert abs(S(5 * P / 2) - P**2 / 4) < 1e-3                  # 2pi-periodic: 5pi/2 -> pi/2
assert abs(C(P) - P**2) < 1e-3
assert abs(C(-P / 2) - P**2 / 4) < 1e-3
assert abs(C(5 * P / 2) - P**2 / 4) < 1e-3
assert abs(C(2 * P)) < 1e-3
# continuity of the extensions: odd ext jumps at pi, even ext continuous; f'(pi) = 2pi
assert f.subs(x, pi) == pi**2 and sp.diff(f, x).subs(x, pi) == 2 * pi and sp.diff(f, x).subs(x, 0) == 0

# (d) numerical sums
assert sp.summation(1 / n**2, (n, 1, sp.oo)) == pi**2 / 6
assert sp.simplify(sp.summation((-1) ** (n + 1) / n**2, (n, 1, sp.oo)) - pi**2 / 12) == 0
S3 = sum((-1) ** k / (2 * k + 1) ** 3 for k in range(200000))
assert abs(S3 - math.pi**3 / 32) < 1e-12
# sine series at pi/2 written with the Leibniz sum pi/4 and S3: pi^2/2 - 8 S3/pi = pi^2/4
s3 = sp.symbols("S3")
assert sp.solve(sp.Eq(2 * pi * pi / 4 - 8 * s3 / pi, pi**2 / 4), s3) == [pi**3 / 32]
assert abs(float(pi**3 / 32) - 0.968946) < 1e-6
three = 1 - 1 / 27 + 1 / 125
assert abs(three - 0.970963) < 1e-6 and abs(three - math.pi**3 / 32) < 0.0021
# term-by-term derivative of the cosine series = sine series of 2x
for k in range(1, 6):
    assert sp.simplify(2 / pi * sp.integrate(2 * x * sp.sin(k * x), (x, 0, pi)) - 4 * (-1) ** (k + 1) / k) == 0
# boundary term of the cosine coefficient: [2x cos nx / n^2]_0^pi = (f'(pi)(-1)^n - f'(0))/n^2
assert sp.simplify((2 * x * sp.cos(n * x) / n**2).subs(x, pi) - (2 * x * sp.cos(n * x) / n**2).subs(x, 0) - 2 * pi * (-1) ** n / n**2) == 0
print("p11 OK")
