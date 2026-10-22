"""Bank P10: Fourier series of f = 0 on (-pi,0), x^2 on (0,pi). SymPy checks."""
import sympy as sp

x = sp.symbols("x", real=True)
n = sp.symbols("n", integer=True, positive=True)
pi = sp.pi

a0 = sp.integrate(x**2, (x, 0, pi))/pi
assert a0 == pi**2/3
an = sp.simplify(sp.integrate(x**2*sp.cos(n*x), (x, 0, pi))/pi)
assert sp.simplify(an - 2*(-1)**n/n**2) == 0
bn = sp.simplify(sp.integrate(x**2*sp.sin(n*x), (x, 0, pi))/pi)
bn_note = -pi*(-1)**n/n + 2*((-1)**n - 1)/(pi*n**3)
assert sp.simplify(bn - bn_note) == 0
# antiderivatives used in the note
Fc = x**2*sp.sin(n*x)/n + 2*x*sp.cos(n*x)/n**2 - 2*sp.sin(n*x)/n**3
assert sp.simplify(sp.diff(Fc, x) - x**2*sp.cos(n*x)) == 0
Fs = -x**2*sp.cos(n*x)/n + 2*x*sp.sin(n*x)/n**2 + 2*sp.cos(n*x)/n**3
assert sp.simplify(sp.diff(Fs, x) - x**2*sp.sin(n*x)) == 0
# intermediate integrals int_0^pi x sin nx = -pi(-1)^n/n ; int_0^pi x cos nx = ((-1)^n - 1)/n^2
assert sp.simplify(sp.integrate(x*sp.sin(n*x), (x, 0, pi)) + pi*(-1)**n/n) == 0
assert sp.simplify(sp.integrate(x*sp.cos(n*x), (x, 0, pi)) - ((-1)**n - 1)/n**2) == 0
# odd and even n values of b_n
assert sp.simplify(bn_note.subs(n, 2*sp.Symbol("m", integer=True, positive=True)) + pi/(2*sp.Symbol("m", integer=True, positive=True))) == 0
for k in [1, 3, 5]:
    assert sp.simplify(bn_note.subs(n, k) - (pi/k - 4/(pi*k**3))) == 0
# first coefficients
assert [an.subs(n, k) for k in (1, 2, 3)] == [-2, sp.Rational(1, 2), -sp.Rational(2, 9)]
assert sp.simplify(bn_note.subs(n, 1) - (pi - 4/pi)) == 0
assert sp.simplify(bn_note.subs(n, 2) + pi/2) == 0

# Dirichlet values: x=0 -> 0, x = +-pi -> pi^2/2
# x = 0: 0 = pi^2/6 + 2 sum (-1)^n/n^2  =>  sum (-1)^(n+1)/n^2 = pi^2/12
s_alt = sp.summation((-1)**(n + 1)/n**2, (n, 1, sp.oo))
assert sp.simplify(s_alt - pi**2/12) == 0
assert sp.simplify(a0/2 + sp.summation(an, (n, 1, sp.oo))) == 0
# x = pi: cos n pi = (-1)^n, sin n pi = 0: pi^2/6 + 2 sum 1/n^2 = pi^2/2  =>  sum 1/n^2 = pi^2/6
assert sp.simplify(a0/2 + sp.summation(an*(-1)**n, (n, 1, sp.oo)) - pi**2/2) == 0
assert sp.summation(1/n**2, (n, 1, sp.oo)) == pi**2/6
# consistency: sum 1/n^2 - sum (-1)^(n+1)/n^2 = 2 sum_even 1/n^2 = (1/2) sum 1/n^2
assert sp.simplify(pi**2/6 - pi**2/12 - sp.Rational(1, 2)*pi**2/6) == 0
# wrong use of f(pi-) = pi^2 at the jump would give 5 pi^2/12
assert sp.simplify((pi**2 - pi**2/6)/2 - 5*pi**2/12) == 0
# mean value a0/2 = (1/2pi) int f
assert a0/2 == sp.integrate(x**2, (x, 0, pi))/(2*pi)
# leading 1/n part of b_n equals J (-1)^n/(n pi), J = f(pi+) - f(pi-) = -pi^2
Jmp = -pi**2
assert sp.simplify(bn_note - Jmp*(-1)**n/(n*pi) - 2*((-1)**n - 1)/(pi*n**3)) == 0
# x = pi/2 value pi^2/4, x = -pi/2 value 0 (Dirichlet, continuity points)
assert (x**2).subs(x, pi/2) == pi**2/4

# numerical partial sums approach the Dirichlet values
def S(xv, N):
    return float(a0/2) + sum(float(an.subs(n, k))*float(sp.cos(k*xv)) + float(bn_note.subs(n, k))*float(sp.sin(k*xv)) for k in range(1, N + 1))
assert abs(S(0.0, 4000)) < 1e-3
assert abs(S(float(pi), 4000) - float(pi**2/2)) < 1e-3
assert abs(S(float(pi/2), 4000) - float(pi**2/4)) < 2e-3
assert abs(S(-1.0, 4000)) < 2e-3
print("p10 OK")
