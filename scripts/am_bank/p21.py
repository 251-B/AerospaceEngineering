"""P21: Laplace in a wedge 0<theta<alpha, r<a; u(r,0)=0, u_theta(r,alpha)=0, bounded at r=0, u(a,theta)=f."""
import sympy as sp

r, th, a, alpha = sp.symbols("r theta a alpha", positive=True)
n = sp.symbols("n", integer=True, positive=True)
lap = lambda u: sp.diff(u, r, 2) + sp.diff(u, r) / r + sp.diff(u, th, 2) / r**2

# angular eigenfunctions
nu = (2 * n - 1) * sp.pi / (2 * alpha)
Th = sp.sin(nu * th)
assert Th.subs(th, 0) == 0
assert sp.simplify(sp.diff(Th, th).subs(th, alpha)) == 0  # cos((2n-1)pi/2) = 0
assert sp.simplify(sp.diff(Th, th, 2) + nu**2 * Th) == 0
# lambda = 0 and lambda < 0 give only trivial solutions
A, B = sp.symbols("A B")
mu = sp.symbols("mu", positive=True)
assert sp.solve([(A * th + B).subs(th, 0), sp.diff(A * th + B, th).subs(th, alpha)], [A, B]) == {A: 0, B: 0}
Thm = sp.sinh(mu * th)
assert sp.simplify(sp.diff(Thm, th).subs(th, alpha) - mu * sp.cosh(mu * alpha)) == 0  # > 0

# radial Euler equation: r^2 R'' + r R' - nu^2 R = 0 -> r^nu, r^-nu
p = sp.symbols("p")
assert sp.simplify(r**2 * sp.diff(r**p, r, 2) + r * sp.diff(r**p, r) - nu**2 * r**p - (p**2 - nu**2) * r**p) == 0
assert sp.simplify(lap(r**nu * Th)) == 0 and sp.simplify(lap(r ** (-nu) * Th)) == 0

# alpha = pi/2: nu_n = 2n-1; data sin^3 theta = (3 sin th - sin 3th)/4
assert sp.simplify(nu.subs(alpha, sp.pi / 2) - (2 * n - 1)) == 0
f = sp.sin(th) ** 3
assert sp.simplify(sp.expand_trig(sp.sin(3 * th)) - (3 * sp.sin(th) - 4 * sp.sin(th) ** 3)) == 0
assert sp.simplify(f - (3 * sp.sin(th) - sp.sin(3 * th)) / 4) == 0
# coefficients by orthogonality: c_n = (4/pi) int_0^{pi/2} f sin((2n-1)th)
for nv in range(1, 6):
    cn = 4 / sp.pi * sp.integrate(f * sp.sin((2 * nv - 1) * th), (th, 0, sp.pi / 2))
    expected = {1: sp.Rational(3, 4), 2: -sp.Rational(1, 4)}.get(nv, 0)
    assert sp.simplify(cn - expected) == 0
assert sp.integrate(sp.sin(th) ** 4, (th, 0, sp.pi / 2)) == 3 * sp.pi / 16
assert sp.simplify(sp.sin(th) ** 4 - (sp.Rational(3, 8) - sp.cos(2 * th) / 2 + sp.cos(4 * th) / 8)) == 0
# general norm alpha/2
assert sp.simplify(sp.integrate(Th**2, (th, 0, alpha)) - alpha / 2) == 0
# norm int_0^{pi/2} sin^2((2n-1)th) = pi/4
assert sp.simplify(sp.integrate(sp.sin(3 * th) ** 2, (th, 0, sp.pi / 2)) - sp.pi / 4) == 0

u = sp.Rational(3, 4) * (r / a) * sp.sin(th) - sp.Rational(1, 4) * (r / a) ** 3 * sp.sin(3 * th)
assert sp.simplify(lap(u)) == 0
assert u.subs(th, 0) == 0
assert sp.simplify(sp.diff(u, th).subs(th, sp.pi / 2)) == 0
assert sp.simplify(u.subs(r, a) - f) == 0
# Cartesian form
X, Y = sp.symbols("x y", real=True)
uc = sp.Rational(3, 4) * Y / a - sp.Rational(1, 4) * (3 * X**2 * Y - Y**3) / a**3
assert sp.simplify(uc.subs({X: r * sp.cos(th), Y: r * sp.sin(th)}) - u) == 0
assert sp.diff(uc, X, 2) + sp.diff(uc, Y, 2) == 0
# u_x = 0 on the edge x = 0 (theta = pi/2) in Cartesian form
assert sp.diff(uc, X).subs(X, 0) == 0
# values: centre-line point r = a/2, theta = pi/2 : 3/8 + 1/32 = 13/32
assert sp.simplify(u.subs({r: a / 2, th: sp.pi / 2}) - sp.Rational(13, 32)) == 0
# r = a/2, theta = pi/6: 3/4*1/2*1/2 - 1/4*1/8*1 = 3/16 - 1/32 = 5/32
assert sp.simplify(u.subs({r: a / 2, th: sp.pi / 6}) - sp.Rational(5, 32)) == 0
# max on the boundary: f max = 1 at theta = pi/2; on the edge theta=pi/2 u(r) = 3/4 s + 1/4 s^3 <= 1
s = sp.symbols("s", positive=True)
assert sp.simplify(u.subs({th: sp.pi / 2, r: s * a}) - (sp.Rational(3, 4) * s + sp.Rational(1, 4) * s**3)) == 0

print("p21 OK")
