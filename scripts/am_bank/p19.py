"""P19: X'' + lam X = 0 on (0,1), X(0) = 0, X'(1) + h X(1) = 0, h > 0."""
import sympy as sp
import mpmath as mp

x = sp.symbols("x", real=True)
h, mu, A, B = sp.symbols("h mu A B", positive=True)

# lam = 0: X = A x + B
X0 = A * x + B
assert X0.subs(x, 0) == B
assert sp.simplify((sp.diff(X0, x) + h * X0).subs(x, 1).subs(B, 0) - A * (1 + h)) == 0
# lam = -mu^2: X = sinh(mu x); BC gives mu cosh mu + h sinh mu > 0
Xm = sp.sinh(mu * x)
assert sp.simplify(sp.diff(Xm, x, 2) - mu**2 * Xm) == 0
assert sp.simplify((sp.diff(Xm, x) + h * Xm).subs(x, 1) - (mu * sp.cosh(mu) + h * sp.sinh(mu))) == 0
# lam = mu^2: X = sin(mu x); BC: mu cos mu + h sin mu = 0
Xp = sp.sin(mu * x)
assert sp.simplify(sp.diff(Xp, x, 2) + mu**2 * Xp) == 0
assert sp.simplify((sp.diff(Xp, x) + h * Xp).subs(x, 1) - (mu * sp.cos(mu) + h * sp.sin(mu))) == 0

# h = 1: roots of tan mu = -mu in ((n-1/2)pi, n pi)
mp.mp.dps = 30
g = lambda m: m * mp.cos(m) + mp.sin(m)
roots = [mp.findroot(g, ((n - 0.5) * mp.pi + 1e-9, n * mp.pi), solver="anderson") for n in (1, 2, 3)]
for n, r in zip((1, 2, 3), roots):
    assert (n - 0.5) * mp.pi < r < n * mp.pi
assert abs(roots[0] - mp.mpf("2.028757838110434")) < 1e-12
assert abs(roots[0] ** 2 - mp.mpf("4.115858365")) < 1e-8
assert abs(roots[1] - mp.mpf("4.913180439434884")) < 1e-12
assert abs(roots[1] ** 2 - mp.mpf("24.1393")) < 1e-4
# asymptotic values quoted for h = 1, n = 1, 2
assert abs(mp.pi / 2 + 2 / mp.pi - mp.mpf("2.2074")) < 1e-4
assert abs(3 * mp.pi / 2 + 2 / (3 * mp.pi) - mp.mpf("4.9246")) < 1e-4
assert abs(mp.pi**2 / 4 + 2 - mp.mpf("4.4674")) < 1e-4
assert abs(9 * mp.pi**2 / 4 + 2 - mp.mpf("24.2066")) < 1e-4
assert 0.08 < (mp.pi**2 / 4 + 2 - roots[0] ** 2) / roots[0] ** 2 < 0.09
assert 0.002 < (9 * mp.pi**2 / 4 + 2 - roots[1] ** 2) / roots[1] ** 2 < 0.0035
# asymptotic mu_n ~ (n-1/2)pi + h/((n-1/2)pi); lam_n ~ (n-1/2)^2 pi^2 + 2h
for hv in (1, 3):
    gh = lambda m: m * mp.cos(m) + hv * mp.sin(m)
    for n in (20, 40):
        r = mp.findroot(gh, ((n - 0.5) * mp.pi + 1e-12, n * mp.pi), solver="anderson")
        p = (n - 0.5) * mp.pi
        assert abs(r - (p + hv / p)) < 3 * hv**2 / p**3 + hv**3 / p**3
        assert abs(r**2 - (p**2 + 2 * hv)) < 5 * hv**2 / p**2

# orthogonality: numeric for h = 1, modes 1,2
f = lambda a, b: mp.quad(lambda s: mp.sin(a * s) * mp.sin(b * s), [0, 1])
assert abs(f(roots[0], roots[1])) < 1e-20 and abs(f(roots[0], roots[2])) < 1e-20
# symbolic orthogonality: integral of sin(m x) sin(n x) = (n sin m cos n - m cos m sin n)/(m^2 - n^2) ... vanishes with the BC
m_, n_ = sp.symbols("m n", positive=True)
I = sp.integrate(sp.sin(m_ * x) * sp.sin(n_ * x), (x, 0, 1), conds="none")
I = sp.simplify(I.args[-1][0] if isinstance(I, sp.Piecewise) else I)
Isub = I.subs({sp.cos(m_): -h * sp.sin(m_) / m_, sp.cos(n_): -h * sp.sin(n_) / n_})
assert sp.simplify(Isub) == 0

# norm: int_0^1 sin^2(mu x) dx = 1/2 - sin(2mu)/(4mu) = (h^2+mu^2+h)/(2(h^2+mu^2)) on eigenvalues
N2 = sp.integrate(sp.sin(mu * x) ** 2, (x, 0, 1))
assert sp.simplify(N2 - (sp.Rational(1, 2) - sp.sin(2 * mu) / (4 * mu))) == 0
for hv, r in [(1, roots[0]), (1, roots[1])]:
    lhs = mp.quad(lambda s: mp.sin(r * s) ** 2, [0, 1])
    rhs = (hv**2 + r**2 + hv) / (2 * (hv**2 + r**2))
    assert abs(lhs - rhs) < 1e-20
# value for n = 1, h = 1
assert abs((1 + roots[0] ** 2 + 1) / (2 * (1 + roots[0] ** 2)) - mp.mpf("0.5977")) < 1e-4

print("p19 OK")
