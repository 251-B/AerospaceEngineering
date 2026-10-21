"""Linear systems x' = a x + b y + f(t), y' = c x + d y + g(t) solved by elimination (Topic 4, Sec. 2.1; Robinson Ch. 26)."""
import sympy as sp

from . import uc
from .core import tex, solve_steps, t


def pieces_from_expr(expr):
    """Decompose a sum of terms c t^n e^{s t} {1, cos wt, sin wt} into uc.Piece objects (same shape grouped)."""
    expr = sp.expand(expr)
    groups = {}
    for term in sp.Add.make_args(expr):
        if term == 0:
            continue
        coef, rest = term.as_independent(t)
        deg, sigma, omega, trig = 0, 0, 0, None
        for fac in sp.Mul.make_args(rest):
            if fac == t:
                deg += 1
            elif fac.is_Pow and fac.base == t:
                deg += int(fac.exp)
            elif fac.func == sp.exp:
                sigma += sp.simplify(fac.args[0] / t)
            elif fac.func in (sp.cos, sp.sin):
                omega = sp.simplify(fac.args[0] / t)
                trig = fac.func.__name__
            elif fac == 1:
                pass
            else:
                raise ValueError(f"cannot decompose {term}")
        key = (deg, sigma, omega if trig else 0)
        g = groups.setdefault(key, [0, 0, 0, trig is not None])
        if trig == "cos":
            g[1] += coef
        elif trig == "sin":
            g[2] += coef
        else:
            g[0] += coef
    out = []
    for (deg, sigma, omega), (c0, cc, cs, has_trig) in groups.items():
        if has_trig:
            if cs == 0:
                out.append(uc.Piece(c=1, deg=deg, sigma=sigma, omega=omega, trig="cos", cs=None) if False else uc.Piece(c=cc, deg=deg, sigma=sigma, omega=omega, trig="cos"))
            elif cc == 0:
                out.append(uc.Piece(c=cs, deg=deg, sigma=sigma, omega=omega, trig="sin"))
            else:
                out.append(uc.Piece(c=1, deg=deg, sigma=sigma, omega=omega, trig="mix", cs=(cc, cs)))
        else:
            out.append(uc.Piece(c=c0, deg=deg, sigma=sigma))
    return out


def d_tex(sym, order):
    return sym + "'" * order


def eliminate(doc, a, b, c, d, f, g, x0, y0=None, xdot0=None):
    """Solve the system by elimination of y; returns (x(t), y(t)) of the IVP.

    The data are (x(0), y(0)) or (x(0), x'(0)).  f and g are SymPy expressions in t (0 when homogeneous)."""
    a, b, c, d = [sp.nsimplify(v) for v in (a, b, c, d)]
    f, g = sp.sympify(f), sp.sympify(g)
    assert b != 0
    doc.p("The system is linear with constant coefficients, in the form $\\dot x = ax + by + f(t)$, $\\dot y = cx + dy + g(t)$ (Robinson Eq. 26.1) with")
    doc.m(f"a = {tex(a)},\\quad b = {tex(b)},\\quad c = {tex(c)},\\quad d = {tex(d)},\\quad f(t) = {tex(f)},\\quad g(t) = {tex(g)}")
    doc.h(4, "Elimination of $y$")
    doc.p(f"Since $b = {tex(b)} \\neq 0$, the first equation can be solved for $y$ (Eq. 26.2):")
    ysym = sp.Function("x")
    doc.m(f"y = \\frac{{\\dot x - ax - f}}{{b}} = \\frac{{1}}{{{tex(b)}}}\\left(\\dot x - ({tex(a)})x - ({tex(f)})\\right)")
    doc.p("Differentiate with respect to $t$ (everything is differentiable):")
    doc.m(f"\\dot y = \\frac{{\\ddot x - a\\dot x - \\dot f}}{{b}} = \\frac{{1}}{{{tex(b)}}}\\left(\\ddot x - ({tex(a)})\\dot x - ({tex(sp.diff(f, t))})\\right)")
    doc.p("Substitute both expressions into the second equation, $\\dot y = cx + dy + g$, and multiply by $b$:")
    doc.m(f"\\ddot x - a\\dot x - \\dot f = bc\\,x + d\\,(\\dot x - ax - f) + bg")
    doc.p("Collect the terms in $\\ddot x$, $\\dot x$ and $x$ (Eq. 26.3):")
    doc.m("\\ddot x - (a + d)\\dot x + (ad - bc)x = \\dot f + bg - df")
    coeffs = [1, -(a + d), a * d - b * c]
    rhs = sp.expand(sp.diff(f, t) + b * g - d * f)
    doc.p(f"Numerically, $a + d = {tex(a + d)}$, $ad - bc = ({tex(a)})({tex(d)}) - ({tex(b)})({tex(c)}) = {tex(a * d - b * c)}$ and $F(t) := \\dot f + bg - df = ({tex(sp.diff(f, t))}) + ({tex(b)})({tex(g)}) - ({tex(d)})({tex(f)}) = {tex(rhs)}$, so")
    doc.m(f"{uc.ode_tex(coeffs, 'x', rhs)}")
    f0 = f.subs(t, 0)
    if xdot0 is None:
        xdot0 = sp.nsimplify(a * x0 + b * y0 + f0)
        doc.p(f"Initial data. The condition on $y$ is converted into one on $\\dot x$ with the first equation at $t = 0$: $\\dot x(0) = a\\,x(0) + b\\,y(0) + f(0) = ({tex(a)})({tex(x0)}) + ({tex(b)})({tex(y0)}) + ({tex(f0)}) = {tex(xdot0)}$.")
    else:
        y0 = sp.nsimplify((xdot0 - a * x0 - f0) / b)
        doc.p(f"Initial data. Here $x(0)$ and $\\dot x(0)$ are given; the value of $y(0)$ follows from the first equation at $t = 0$: $y(0) = \\dfrac{{\\dot x(0) - a\\,x(0) - f(0)}}{{b}} = \\dfrac{{{tex(xdot0)} - ({tex(a)})({tex(x0)}) - ({tex(f0)})}}{{{tex(b)}}} = {tex(y0)}$.")
    pieces = pieces_from_expr(rhs)
    saved = uc.FNAME
    uc.FNAME = "F"
    try:
        general, final_x, xp = uc.solve_ivp(doc, coeffs, pieces, [x0, xdot0])
    finally:
        uc.FNAME = saved
    doc.h(4, "Recovering $y$")
    ydef = sp.expand((sp.diff(final_x, t) - a * final_x - f) / b)
    doc.p("From Eq. 26.2, $y = (\\dot x - ax - f)/b$. With the solution found,")
    doc.m(f"\\dot x(t) = {tex(sp.expand(sp.diff(final_x, t)))}")
    doc.m(f"y(t) = \\frac{{1}}{{{tex(b)}}}\\left(\\dot x - ({tex(a)})x - ({tex(f)})\\right) = {tex(ydef)}")
    assert sp.simplify(ydef.subs(t, 0) - y0) == 0
    # verification against the original equations
    r1 = sp.simplify(sp.diff(final_x, t) - (a * final_x + b * ydef + f))
    r2 = sp.simplify(sp.diff(ydef, t) - (c * final_x + d * ydef + g))
    assert r1 == 0 and r2 == 0, (r1, r2)
    doc.h(4, "Check in the original system")
    rows = []
    rows.append(f"\\dot x &= {tex(sp.expand(sp.diff(final_x, t)))} \\\\ ax + by + f &= {tex(sp.expand(a * final_x + b * ydef + f))}")
    rows.append(f"\\dot y &= {tex(sp.expand(sp.diff(ydef, t)))} \\\\ cx + dy + g &= {tex(sp.expand(c * final_x + d * ydef + g))}")
    doc.m(r"\begin{aligned} " + r" \\[4pt] ".join(rows) + r" \end{aligned}")
    doc.p(f"Both pairs of expressions coincide, and $x(0) = {tex(final_x.subs(t, 0))}$, $y(0) = {tex(ydef.subs(t, 0))}$ reproduce the initial data.")
    return final_x, ydef, dict(a=a, b=b, c=c, d=d, f=f, g=g, x0=x0, y0=y0, general=general)
