"""Bank P08: competing species x' = x(6-2x-y), y' = y(4-y-bx). SymPy checks."""
import sympy as sp

x, y, b, lam = sp.symbols("x y b lam", real=True)
F = sp.Matrix([x*(6 - 2*x - y), y*(4 - y - b*x)])
Jac = F.jacobian([x, y])
assert sp.expand(Jac - sp.Matrix([[6 - 4*x - y, -x], [-b*y, 4 - 2*y - b*x]])) == sp.zeros(2)

# equilibria
xs, ys = 2/(2 - b), (8 - 6*b)/(2 - b)
assert sp.simplify(F.subs({x: xs, y: ys})) == sp.zeros(2, 1)
for p in [(0, 0), (3, 0), (0, 4)]:
    assert sp.simplify(F.subs({x: p[0], y: p[1]})) == sp.zeros(2, 1)
# coexistence in open quadrant iff b < 4/3 (b>0)
assert sp.solve(sp.Eq(8 - 6*b, 0), b) == [sp.Rational(4, 3)]

J00 = Jac.subs({x: 0, y: 0}); assert J00 == sp.diag(6, 4)
J30 = Jac.subs({x: 3, y: 0}); assert J30 == sp.Matrix([[-6, -3], [0, 4 - 3*b]])
J04 = Jac.subs({x: 0, y: 4}); assert J04 == sp.Matrix([[2, 0], [-4*b, -4]])
Jc = sp.simplify(Jac.subs({x: xs, y: ys}))
assert sp.simplify(Jc - sp.Matrix([[-2*xs, -xs], [-b*ys, -ys]])) == sp.zeros(2)
trc = sp.simplify(Jc.trace()); detc = sp.simplify(Jc.det())
assert sp.simplify(detc - xs*ys*(2 - b)) == 0
assert sp.simplify(detc - 2*(8 - 6*b)/(2 - b)) == 0
assert sp.simplify(trc - (-(4 + 8 - 6*b)/(2 - b))) == 0   # tr = -(2x*+y*) = -(12-6b)/(2-b) = -6
assert sp.simplify(trc + 6) == 0
disc = sp.simplify(trc**2 - 4*detc)
assert sp.simplify(disc - (ys - 2*xs)**2 - 4*b*xs*ys) == 0  # (a-d)^2 + 4bc form, >0
# disc > 0 for 0<b<4/3 (real eigenvalues: node)
for bv in [sp.Rational(1, 10), sp.Rational(1, 2), 1, sp.Rational(13, 10)]:
    assert disc.subs(b, bv) > 0 and detc.subs(b, bv) > 0
# at b = 4/3 the coexistence point merges with (3,0)
assert (xs.subs(b, sp.Rational(4, 3)), ys.subs(b, sp.Rational(4, 3))) == (3, 0)

# b = 1
J1 = Jac.subs(b, 1)
Jc1 = J1.subs({x: 2, y: 2}); assert Jc1 == sp.Matrix([[-4, -2], [-2, -2]])
assert (xs.subs(b, 1), ys.subs(b, 1)) == (2, 2)
ev = Jc1.eigenvals(); assert ev == {-3 + sp.sqrt(5): 1, -3 - sp.sqrt(5): 1}
vs = sp.Matrix([2, -1 - sp.sqrt(5)]); vf = sp.Matrix([2, sp.sqrt(5) - 1])
assert sp.simplify(Jc1*vs - (-3 + sp.sqrt(5))*vs) == sp.zeros(2, 1)
assert sp.simplify(Jc1*vf - (-3 - sp.sqrt(5))*vf) == sp.zeros(2, 1)
J30b1 = J30.subs(b, 1); assert J30b1 == sp.Matrix([[-6, -3], [0, 1]])
assert J30b1*sp.Matrix([3, -7]) == sp.Matrix([3, -7])
J04b1 = J04.subs(b, 1); assert J04b1 == sp.Matrix([[2, 0], [-4, -4]])
assert J04b1*sp.Matrix([3, -2]) == 2*sp.Matrix([3, -2])
assert J04b1*sp.Matrix([0, 1]) == -4*sp.Matrix([0, 1])
# numerical eigenvalues
assert abs(float(-3 + sp.sqrt(5)) + 0.763932) < 1e-6 and abs(float(-3 - sp.sqrt(5)) + 5.236068) < 1e-6

# b = 2: no coexistence (parallel nullclines 2x+y=6 and 2x+y=4)
F2 = F.subs(b, 2)
eq = sp.solve(list(F2), [x, y], dict=True)
assert {(e[x], e[y]) for e in eq} == {(0, 0), (3, 0), (0, 4)}
J30b2 = J30.subs(b, 2); assert J30b2 == sp.Matrix([[-6, -3], [0, -2]])
assert J30b2*sp.Matrix([3, -4]) == -2*sp.Matrix([3, -4])
J04b2 = J04.subs(b, 2); assert J04b2 == sp.Matrix([[2, 0], [-8, -4]])
assert J04b2*sp.Matrix([3, -4]) == 2*sp.Matrix([3, -4])
# in strip 4 < 2x+y < 6 (x,y>0): x' > 0, y' < 0  (sample point (1.5, 2): 2x+y = 5)
pt = {x: sp.Rational(3, 2), y: 2}
assert F2.subs(pt)[0] > 0 and F2.subs(pt)[1] < 0
# b = 1 region checks: between nullclines x+y=4 and 2x+y=6 for x<2 ... sample points
pt1 = {x: 1, y: 3.5}  # 2x+y=5.5<6 -> x'>0 ; x+y=4.5>4 -> y'<0
F1 = F.subs(b, 1)
assert F1.subs(pt1)[0] > 0 and F1.subs(pt1)[1] < 0
pt2 = {x: sp.Rational(5, 2), y: sp.Rational(1, 2)}  # 2x+y=5.5 -> x'>0? ; x+y=3<4 -> y'>0
assert F1.subs(pt2)[0] > 0 and F1.subs(pt2)[1] > 0
pt3 = {x: 3, y: sp.Rational(1, 2)}  # 2x+y=6.5>6 -> x'<0 ; x+y=3.5<4 -> y'>0
assert F1.subs(pt3)[0] < 0 and F1.subs(pt3)[1] > 0
# (0,4) unstable eigenvector (3, -2b) for every b
assert sp.expand(J04*sp.Matrix([3, -2*b]) - 2*sp.Matrix([3, -2*b])) == sp.zeros(2, 1)
# b = 1 eigenvalue sum and product; limit b -> 0
assert sp.expand((-3 + sp.sqrt(5)) + (-3 - sp.sqrt(5))) == -6 and sp.expand((-3 + sp.sqrt(5))*(-3 - sp.sqrt(5))) == 4
assert (xs.subs(b, 0), ys.subs(b, 0)) == (1, 4)
# trapping-region boundary formulas (b = 1)
assert sp.expand((y*(4 - x - y)).subs(y, 6 - 2*x) - (6 - 2*x)*(x - 2)) == 0
assert sp.expand((x*(6 - 2*x - y)).subs(y, 4 - x) - x*(2 - x)) == 0
# b = 2 sample point values
assert F2.subs(pt) == sp.Matrix([sp.Rational(3, 2), -2])
# axes invariant
assert F[0].subs(x, 0) == 0 and F[1].subs(y, 0) == 0

print("p08 OK")
