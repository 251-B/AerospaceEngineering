"""Bank P02: logistic growth with constant harvesting p' = p(1-p) - h."""
import sympy as sp

p, h, t = sp.symbols("p h t", real=True)
f = p * (1 - p) - h

# (a) equilibria and the critical rate
roots = sp.solve(f, p)
pm = (1 - sp.sqrt(1 - 4 * h)) / 2
pp = (1 + sp.sqrt(1 - 4 * h)) / 2
assert set(sp.simplify(r) for r in roots) == {sp.simplify(pm), sp.simplify(pp)}
assert sp.solve(sp.discriminant(f, p), h) == [sp.Rational(1, 4)]
assert sp.maximum(p * (1 - p), p) == sp.Rational(1, 4)

# (b) stability through f'(p*) = 1 - 2p*
fp = sp.diff(f, p)
assert sp.simplify(fp.subs(p, pm) - sp.sqrt(1 - 4 * h)) == 0  # > 0: unstable
assert sp.simplify(fp.subs(p, pp) + sp.sqrt(1 - 4 * h)) == 0  # < 0: stable
f14 = f.subs(h, sp.Rational(1, 4))
assert sp.factor(f14) == -(2 * p - 1) ** 2 / 4 or sp.simplify(f14 + (p - sp.Rational(1, 2)) ** 2) == 0

# (c) h = 2/9: equilibria 1/3 and 2/3, partial fractions, two IVPs
h1 = sp.Rational(2, 9)
f1 = f.subs(h, h1)
assert sp.simplify(f1 + (p - sp.Rational(1, 3)) * (p - sp.Rational(2, 3))) == 0
pf = sp.apart(1 / ((p - sp.Rational(1, 3)) * (p - sp.Rational(2, 3))), p)
assert sp.simplify(pf - (3 / (p - sp.Rational(2, 3)) - 3 / (p - sp.Rational(1, 3)))) == 0

def sol(K):
    E = K * sp.exp(-t / 3)
    return (2 - E) / (3 * (1 - E))

for p0, K in [(sp.Rational(1, 2), -1), (sp.Rational(1, 4), 5)]:
    assert (p0 - sp.Rational(2, 3)) / (p0 - sp.Rational(1, 3)) == K
    P = sol(K)
    assert sp.simplify(sp.diff(P, t) - f1.subs(p, P)) == 0
    assert sp.simplify(P.subs(t, 0) - p0) == 0

P1 = sol(-1)
assert sp.simplify(P1 - (2 + sp.exp(-t / 3)) / (3 * (1 + sp.exp(-t / 3)))) == 0
assert sp.limit(P1, t, sp.oo) == sp.Rational(2, 3)
P2 = sol(5)
assert sp.simplify(P2 - (2 * sp.exp(t / 3) - 5) / (3 * (sp.exp(t / 3) - 5))) == 0
T0 = 3 * sp.log(sp.Rational(5, 2))
assert sp.simplify(P2.subs(t, T0)) == 0
assert abs(float(T0) - 2.749) < 1e-3
# blow-down singularity at t = 3 ln 5 lies after T0 (solution reaches 0 first)
assert float(3 * sp.log(5)) > float(T0)

# (d) h = 1/2: no equilibria, finite time to collapse from p0 = 1
f2 = f.subs(h, sp.Rational(1, 2))
assert sp.simplify(f2 + ((p - sp.Rational(1, 2)) ** 2 + sp.Rational(1, 4))) == 0
F = 2 * sp.atan(2 * p - 1)
assert sp.simplify(sp.diff(F, p) - 1 / ((p - sp.Rational(1, 2)) ** 2 + sp.Rational(1, 4))) == 0
T = sp.integrate(1 / ((p - sp.Rational(1, 2)) ** 2 + sp.Rational(1, 4)), (p, 0, 1))
assert sp.simplify(T - sp.pi) == 0
assert sp.simplify(F.subs(p, 1) - F.subs(p, 0) - sp.pi) == 0
Pd = sp.Rational(1, 2) + sp.tan(sp.pi / 4 - t / 2) / 2
assert sp.simplify(sp.diff(Pd, t) - f2.subs(p, Pd)) == 0
assert Pd.subs(t, 0) == 1 and sp.simplify(Pd.subs(t, sp.pi)) == 0
# general p0 in [0,1): T(p0) = 2 arctan(2 p0 - 1) + pi/2; p0 = 1/2 gives pi/2
p0 = sp.symbols("p0")
Tg = 2 * sp.atan(2 * p0 - 1) + sp.pi / 2
assert sp.simplify(Tg.subs(p0, 1) - sp.pi) == 0 and Tg.subs(p0, sp.Rational(1, 2)) == sp.pi / 2
# general h > 1/4 from p0 = 1: T = (2/w) arctan(1/(2w)), w = sqrt(h - 1/4); h = 1/2 -> w = 1/2
om = sp.symbols("omega", positive=True)
Tw = sp.integrate(1 / ((p - sp.Rational(1, 2)) ** 2 + om**2), (p, 0, 1))
assert sp.simplify(Tw - 2 / om * sp.atan(1 / (2 * om))) == 0
assert sp.limit(2 / om * sp.atan(1 / (2 * om)), om, 0, "+") == sp.oo
w = sp.Rational(1, 2)
assert sp.simplify(2 / w * sp.atan(1 / (2 * w)) - sp.pi) == 0
print("p02 OK")
