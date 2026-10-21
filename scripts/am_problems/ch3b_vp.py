"""Chapter 3, part 2, exercises 6 to 9: variation of constants, structure of IVP solutions, reduction of order."""
import sympy as sp

from .core import Note, tex
from .ch3b import SHEET, SOURCE, CLAIMS

X = sp.Symbol("x", real=True)
T = sp.Symbol("t", real=True)


def vp_steps(doc, y1, y2, g, v, name="y", p=0, q=0, label=("y_1", "y_2")):
    """Variation of constants (Robinson Eq. 18.8) with the pieces written out; returns the particular solution.

    y1, y2: independent homogeneous solutions (expressions in v); g: forcing in standard form y'' + p y' + q y = g."""
    a1, a2 = label
    W = sp.simplify(y1 * sp.diff(y2, v) - y2 * sp.diff(y1, v))
    doc.p(f"The homogeneous solutions are ${a1} = {tex(y1)}$ and ${a2} = {tex(y2)}$. Their Wronskian is")
    doc.m(f"W = {a1}\\,{a2}' - {a2}\\,{a1}' = ({tex(y1)})({tex(sp.diff(y2, v))}) - ({tex(y2)})({tex(sp.diff(y1, v))}) = {tex(W)}")
    u1p = sp.simplify(-y2 * g / W)
    u2p = sp.simplify(y1 * g / W)
    doc.p(f"With $g = {tex(g)}$ (equation in standard form, coefficient of ${name}''$ equal to $1$), Cramer's rule gives $u_1' = -\\dfrac{{{a2}\\,g}}{{W}}$ and $u_2' = \\dfrac{{{a1}\\,g}}{{W}}$:")
    doc.m(f"u_1' = -\\frac{{({tex(y2)})({tex(g)})}}{{{tex(W)}}} = {tex(u1p)}, \\qquad u_2' = \\frac{{({tex(y1)})({tex(g)})}}{{{tex(W)}}} = {tex(u2p)}")
    return W, u1p, u2p


def verify_particular(expr, coeffs_pq, g, v):
    p, q = coeffs_pq
    res = sp.simplify(sp.diff(expr, v, 2) + p * sp.diff(expr, v) + q * expr - g)
    assert res == 0, res


def ex6():
    n = Note(SHEET, 6, "Variation of Constants: Five Particular Solutions", "Variation of Parameters • Euler Equation • Integral Answers",
             ["problema-resuelto", "variacion-de-constantes", "wronskiano", "ecuacion-de-euler"], SOURCE)
    st = n.statement
    st.p("Use the method of variation of constants to find a particular solution for the following equations:")
    st.ul(["(i) $y'' - y' - 6y = e^{x}$;", "(ii) $\\ddot x - x = t^{-1}$ (leave the answer as an integral);",
           "(iii) $y'' + 4y = \\cot 2x$. Use that $\\int\\csc x\\,dx = \\ln|\\csc x - \\cot x|$;",
           "(iv) $t^2\\ddot x - 2x = t^3$ (to find the solutions of the homogeneous equation, try solutions of the form $x = t^k$ with $k$ a parameter);",
           "(v) $\\ddot x - 4\\dot x = \\tan t$ (leave your answer as an integral)."])
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("Each equation is linear, second-order, inhomogeneous. Variation of constants (Lagrange; Robinson Ch. 18, Topic 3 Sec. 8) needs: (a) the equation in **standard form** $\\ddot x + p\\dot x + qx = g$ with the coefficient of the highest derivative equal to $1$; (b) two linearly independent solutions $x_1, x_2$ of the homogeneous equation; (c) $g$ continuous on an interval $I$ where the coefficients are continuous. Then, on $I$,")
    p1.m(r"x_p = -x_1\int\frac{x_2\,g}{W}\,dt + x_2\int\frac{x_1\,g}{W}\,dt, \qquad W = x_1\dot x_2 - x_2\dot x_1 \neq 0 \quad (\text{Robinson Eq. 18.8})")
    p1.table(["Item", "Standard form", "Interval $I$ where $g$ and the coefficients are continuous"],
             [["(i)", "$y'' - y' - 6y = e^x$", "$\\mathbb R$"], ["(ii)", "$\\ddot x - x = 1/t$", "$t > 0$ (or $t < 0$)"],
              ["(iii)", "$y'' + 4y = \\cot 2x$", "$0 < x < \\pi/2$ (between zeros of $\\sin 2x$)"],
              ["(iv)", "$\\ddot x - \\dfrac{2}{t^2}x = t$ (divide by $t^2$)", "$t > 0$ (or $t < 0$)"],
              ["(v)", "$\\ddot x - 4\\dot x = \\tan t$", "$-\\pi/2 < t < \\pi/2$"]])
    p2 = n.phase(2, "Formulation: the derivation of the formula, recalled")
    p2.p("Replace the constants of $x_h = c_1x_1 + c_2x_2$ by functions: $x = u_1x_1 + u_2x_2$. Choose $\\dot u_1x_1 + \\dot u_2x_2 = 0$ (18.7), so that $\\dot x = u_1\\dot x_1 + u_2\\dot x_2$; substituting in the equation and using $L[x_1] = L[x_2] = 0$ leaves $\\dot u_1\\dot x_1 + \\dot u_2\\dot x_2 = g$. Cramer's rule on the system with determinant $W$ gives")
    p2.m(r"\dot u_1 = -\frac{x_2\,g}{W}, \qquad \dot u_2 = \frac{x_1\,g}{W}, \qquad x_p = u_1x_1 + u_2x_2")
    p2.p("Constants of integration only add multiples of $x_1, x_2$, so they may be dropped.")
    p3 = n.phase(3, "Derivation")
    # (i)
    p3.h(3, "(i) $y'' - y' - 6y = e^x$")
    p3.p("Homogeneous equation: $y = e^{kx}$ gives $k^2 - k - 6 = (k - 3)(k + 2) = 0$, so $k = 3, -2$.")
    y1, y2, g = sp.exp(3 * X), sp.exp(-2 * X), sp.exp(X)
    W, u1p, u2p = vp_steps(p3, y1, y2, g, X)
    u1, u2 = sp.integrate(u1p, X), sp.integrate(u2p, X)
    p3.p("Integrate (antiderivatives of exponentials, $\\int e^{kx}dx = e^{kx}/k$):")
    p3.m(f"u_1 = \\int {tex(u1p)}\\,dx = {tex(u1)}, \\qquad u_2 = \\int {tex(u2p)}\\,dx = {tex(u2)}")
    yp = sp.simplify(u1 * y1 + u2 * y2)
    p3.m(f"y_p = u_1y_1 + u_2y_2 = \\left({tex(u1)}\\right)e^{{3x}} + \\left({tex(u2)}\\right)e^{{-2x}} = {tex(sp.expand(u1 * y1 + u2 * y2))} = {tex(yp)}")
    verify_particular(yp, (-1, -6), g, X)
    p3.p(f"Check: $y_p' = {tex(sp.diff(yp, X))}$, $y_p'' = {tex(sp.diff(yp, X, 2))}$, so $y_p'' - y_p' - 6y_p = ({tex(sp.diff(yp, X, 2))}) - ({tex(sp.diff(yp, X))}) - 6({tex(yp)}) = e^x$.")
    CLAIMS.append(dict(kind="ode", id="3II-E6-i", coeffs=[1, -1, -6], rhs=g, ics=None, solution=yp, ivar=X, particular=True))
    # (ii)
    p3.h(3, "(ii) $\\ddot x - x = t^{-1}$ (answer as an integral)")
    p3.p("Homogeneous equation: $k^2 - 1 = 0$, so $k = \\pm 1$: $x_1 = e^{t}$, $x_2 = e^{-t}$.")
    x1, x2, g = sp.exp(T), sp.exp(-T), 1 / T
    W, u1p, u2p = vp_steps(p3, x1, x2, g, T, name="x", label=("x_1", "x_2"))
    p3.p("The antiderivatives of $e^{-s}/s$ and $e^{s}/s$ are not elementary (they are exponential integrals). We keep them as integrals from a fixed base point $t_0 > 0$ (the interval where $g = 1/t$ is continuous, $t > 0$), which is a legitimate antiderivative by the fundamental theorem of calculus:")
    p3.m(r"u_1(t) = \frac12\int_{t_0}^{t}\frac{e^{-s}}{s}\,ds, \qquad u_2(t) = -\frac12\int_{t_0}^{t}\frac{e^{s}}{s}\,ds")
    p3.m(r"\boxed{x_p(t) = \frac{e^{t}}{2}\int_{t_0}^{t}\frac{e^{-s}}{s}\,ds - \frac{e^{-t}}{2}\int_{t_0}^{t}\frac{e^{s}}{s}\,ds \quad (t, t_0 > 0)}")
    p3.p("Combining the exponentials inside one integral, $x_p(t) = \\dfrac12\\displaystyle\\int_{t_0}^{t}\\frac{e^{t - s} - e^{-(t - s)}}{s}\\,ds = \\int_{t_0}^{t}\\frac{\\sinh(t - s)}{s}\\,ds$.")
    p3.h(4, "Verification by differentiation (Leibniz rule)")
    p3.p("Let $I_1(t) = \\int_{t_0}^{t}e^{-s}s^{-1}ds$ and $I_2(t) = \\int_{t_0}^{t}e^{s}s^{-1}ds$, so $I_1' = e^{-t}/t$ and $I_2' = e^{t}/t$. Then $x_p = \\frac12(e^tI_1 - e^{-t}I_2)$ and, by the product rule,")
    p3.m(r"\dot x_p = \frac12\left(e^tI_1 + e^{-t}I_2\right) + \frac12\left(e^t\frac{e^{-t}}{t} - e^{-t}\frac{e^{t}}{t}\right) = \frac12\left(e^tI_1 + e^{-t}I_2\right)")
    p3.m(r"\ddot x_p = \frac12\left(e^tI_1 - e^{-t}I_2\right) + \frac12\left(e^t\frac{e^{-t}}{t} + e^{-t}\frac{e^{t}}{t}\right) = x_p + \frac1t")
    p3.p("so $\\ddot x_p - x_p = 1/t$, as required.")
    CLAIMS.append(dict(kind="integral_ode", id="3II-E6-ii", coeffs=[1, 0, -1], rhs=1 / T, ivar=T, y1=x1, y2=x2, g=g))
    # (iii)
    p3.h(3, "(iii) $y'' + 4y = \\cot 2x$")
    p3.p("Homogeneous equation: $k^2 + 4 = 0$, $k = \\pm 2i$, so $y_1 = \\cos 2x$, $y_2 = \\sin 2x$.")
    y1, y2, g = sp.cos(2 * X), sp.sin(2 * X), sp.cot(2 * X)
    W = sp.simplify(y1 * sp.diff(y2, X) - y2 * sp.diff(y1, X))
    p3.p("Wronskian (chain rule: $(\\cos 2x)' = -2\\sin 2x$, $(\\sin 2x)' = 2\\cos 2x$):")
    p3.m(r"W = \cos 2x\cdot 2\cos 2x - \sin 2x\cdot(-2\sin 2x) = 2(\cos^2 2x + \sin^2 2x) = 2")
    p3.p("Cramer's rule with $g = \\cot 2x = \\cos 2x/\\sin 2x$:")
    p3.m(r"u_1' = -\frac{\sin 2x\,\cot 2x}{2} = -\frac{\cos 2x}{2}, \qquad u_2' = \frac{\cos 2x\,\cot 2x}{2} = \frac{\cos^2 2x}{2\sin 2x}")
    p3.p("For $u_2'$ use $\\cos^2 2x = 1 - \\sin^2 2x$: $u_2' = \\dfrac{1 - \\sin^2 2x}{2\\sin 2x} = \\dfrac12\\left(\\csc 2x - \\sin 2x\\right)$. Integrate with the substitution $s = 2x$, $ds = 2\\,dx$, and the hint $\\int\\csc s\\,ds = \\ln|\\csc s - \\cot s|$:")
    p3.m(r"u_1 = -\frac12\int\cos 2x\,dx = -\frac12\cdot\frac{\sin 2x}{2} = -\frac{\sin 2x}{4}")
    p3.m(r"\int\csc 2x\,dx = \frac12\int\csc s\,ds = \frac12\ln|\csc 2x - \cot 2x|, \qquad \int\sin 2x\,dx = -\frac{\cos 2x}{2}")
    p3.m(r"u_2 = \frac12\left[\frac12\ln|\csc 2x - \cot 2x| + \frac{\cos 2x}{2}\right] = \frac14\ln|\csc 2x - \cot 2x| + \frac{\cos 2x}{4}")
    p3.p("Assemble $y_p = u_1y_1 + u_2y_2$; the terms in $\\sin 2x\\cos 2x$ cancel:")
    p3.m(r"y_p = -\frac{\sin 2x\cos 2x}{4} + \left[\frac14\ln|\csc 2x - \cot 2x| + \frac{\cos 2x}{4}\right]\sin 2x = \frac14\,\sin 2x\;\ln\left|\csc 2x - \cot 2x\right|")
    p3.p("Since $\\csc 2x - \\cot 2x = \\dfrac{1 - \\cos 2x}{\\sin 2x} = \\dfrac{2\\sin^2x}{2\\sin x\\cos x} = \\tan x$, an equivalent form is $y_p = \\tfrac14\\sin 2x\\,\\ln|\\tan x|$.")
    yp3 = sp.sin(2 * X) * sp.log(sp.tan(X)) / 4
    res = sp.diff(yp3, X, 2) + 4 * yp3 - sp.cot(2 * X)
    assert all(abs(sp.N(res.subs(X, pt))) < 1e-12 for pt in (0.2, 0.5, 0.9, 1.3)), res
    CLAIMS.append(dict(kind="ode", id="3II-E6-iii", coeffs=[1, 0, 4], rhs=g, ics=None, solution=yp3, ivar=X, particular=True))
    p3.p("Check by differentiating $y_p = \\frac14\\sin 2x\\,\\ell$ with $\\ell = \\ln\\tan x$, $\\ell' = \\frac{\\sec^2x}{\\tan x} = \\frac{2}{\\sin 2x}$: $y_p' = \\frac12\\cos 2x\\,\\ell + \\frac14\\sin 2x\\cdot\\frac{2}{\\sin 2x} = \\frac12\\cos 2x\\,\\ell + \\frac12$; $y_p'' = -\\sin 2x\\,\\ell + \\frac12\\cos 2x\\cdot\\frac{2}{\\sin 2x} = -\\sin 2x\\,\\ell + \\cot 2x$; hence $y_p'' + 4y_p = -\\sin 2x\\,\\ell + \\cot 2x + \\sin 2x\\,\\ell = \\cot 2x$.")
    # (iv)
    p3.h(3, "(iv) $t^2\\ddot x - 2x = t^3$")
    p3.p("Homogeneous equation $t^2\\ddot x - 2x = 0$. Try $x = t^k$ (chain/power rule): $\\dot x = kt^{k-1}$, $\\ddot x = k(k - 1)t^{k-2}$, so $t^2\\ddot x - 2x = [k(k - 1) - 2]t^k = (k^2 - k - 2)t^k = (k - 2)(k + 1)t^k = 0$, hence $k = 2, -1$: $x_1 = t^2$, $x_2 = t^{-1}$ ($t > 0$).")
    p3.p("Standard form: divide by $t^2$ (coefficient of $\\ddot x$ must be $1$): $\\ddot x - \\dfrac{2}{t^2}x = \\dfrac{t^3}{t^2} = t$, so $g(t) = t$ (**not** $t^3$).")
    x1, x2, g = T ** 2, 1 / T, T
    W, u1p, u2p = vp_steps(p3, x1, x2, g, T, name="x", label=("x_1", "x_2"))
    u1, u2 = sp.integrate(u1p, T), sp.integrate(u2p, T)
    p3.m(f"u_1 = \\int {tex(u1p)}\\,dt = {tex(u1)}, \\qquad u_2 = \\int {tex(u2p)}\\,dt = {tex(u2)}")
    xp = sp.simplify(u1 * x1 + u2 * x2)
    p3.m(f"x_p = u_1x_1 + u_2x_2 = \\left({tex(u1)}\\right)t^2 + \\left({tex(u2)}\\right)t^{{-1}} = {tex(sp.expand(u1 * x1 + u2 * x2))} = {tex(xp)}")
    p3.p(f"Check in the original equation: $\\ddot x_p = {tex(sp.diff(xp, T, 2))}$, so $t^2\\ddot x_p - 2x_p = {tex(sp.expand(T ** 2 * sp.diff(xp, T, 2)))} - {tex(2 * xp)} = t^3$.")
    assert sp.simplify(T ** 2 * sp.diff(xp, T, 2) - 2 * xp - T ** 3) == 0
    CLAIMS.append(dict(kind="ode", id="3II-E6-iv", coeffs=[T ** 2, 0, -2], rhs=T ** 3, ics=None, solution=xp, ivar=T, particular=True, euler=True))
    # (v)
    p3.h(3, "(v) $\\ddot x - 4\\dot x = \\tan t$ (answer as an integral)")
    p3.p("Homogeneous equation: $k^2 - 4k = k(k - 4) = 0$, $k = 0, 4$: $x_1 = 1$, $x_2 = e^{4t}$.")
    x1, x2, g = sp.Integer(1), sp.exp(4 * T), sp.tan(T)
    W, u1p, u2p = vp_steps(p3, x1, x2, g, T, name="x", label=("x_1", "x_2"))
    p3.p("The first integral is elementary: $\\int -\\frac14\\tan t\\,dt = \\frac14\\ln|\\cos t|$ (since $\\frac{d}{dt}\\ln\\cos t = -\\tan t$). The second, $\\int e^{-4s}\\tan s\\,ds$, is not elementary, so it is left as an integral from a base point $t_0 \\in (-\\pi/2, \\pi/2)$:")
    p3.m(r"u_1(t) = \frac14\ln\cos t, \qquad u_2(t) = \frac14\int_{t_0}^{t}e^{-4s}\tan s\,ds")
    p3.m(r"\boxed{x_p(t) = \frac14\ln\cos t + \frac{e^{4t}}{4}\int_{t_0}^{t}e^{-4s}\tan s\,ds \qquad (|t|, |t_0| < \pi/2)}")
    p3.h(4, "Verification by differentiation")
    p3.p("With $I(t) = \\int_{t_0}^{t}e^{-4s}\\tan s\\,ds$, $I' = e^{-4t}\\tan t$. Product rule: $\\dot x_p = -\\frac14\\tan t + e^{4t}I + \\frac{e^{4t}}{4}e^{-4t}\\tan t = e^{4t}I$ (the two tangent terms cancel). Again, $\\ddot x_p = 4e^{4t}I + e^{4t}e^{-4t}\\tan t = 4\\dot x_p + \\tan t$, i.e. $\\ddot x_p - 4\\dot x_p = \\tan t$.")
    CLAIMS.append(dict(kind="integral_ode", id="3II-E6-v", coeffs=[1, -4, 0], rhs=sp.tan(T), ivar=T, y1=x1, y2=x2, g=g))
    p4 = n.phase(4, "Interpretation and checks")
    p4.table(["Item", "Particular solution $x_p$", "Domain"],
             [["(i)", "$-\\dfrac{e^{x}}{6}$", "$\\mathbb R$"],
              ["(ii)", "$\\dfrac{e^{t}}{2}\\displaystyle\\int_{t_0}^{t}\\frac{e^{-s}}{s}ds - \\dfrac{e^{-t}}{2}\\int_{t_0}^{t}\\frac{e^{s}}{s}ds$", "$t > 0$"],
              ["(iii)", "$\\dfrac14\\sin 2x\\,\\ln|\\csc 2x - \\cot 2x| = \\dfrac14\\sin 2x\\,\\ln|\\tan x|$", "$0 < x < \\pi/2$"],
              ["(iv)", "$\\dfrac{t^3}{4}$", "$t > 0$"],
              ["(v)", "$\\dfrac14\\ln\\cos t + \\dfrac{e^{4t}}{4}\\displaystyle\\int_{t_0}^{t}e^{-4s}\\tan s\\,ds$", "$|t| < \\pi/2$"]])
    p4.ul(["The general solution of each equation is $x_h + x_p$ with the two homogeneous solutions used above.",
           "(i) and (iv) could also have been found by undetermined coefficients ($Ke^x$ and $Kt^3$); both methods agree ($-\\frac16e^x$ and $\\frac14t^3$), a useful cross-check of the Wronskian bookkeeping. (iii) and (v) have forcings ($\\cot$, $\\tan$) outside the family of undetermined coefficients, which is the reason for the method.",
           "(iv) is an Euler equation: the substitution $x = t^k$ turns it into an algebraic equation for $k$, and its standard form needs the division by $t^2$ before applying the formula.",
           "Wronskians: $-5e^{x}$ in (i) (consistent with Abel's identity, $W = W_0e^{x}$ since $p = -1$), $-2$ in (ii), $2$ in (iii), $-3$ in (iv) and $4e^{4t}$ in (v) (Abel: $p = -4$, $W = W_0e^{4t}$); none vanishes on its interval.",
           "The sheet works in dimensionless variables, so no unit check is attached to the forcings ($t^3$, $e^{x}$, $\\cot 2x$, $\\tan t$ are pure numbers); the check that matters is that each particular solution reproduces its forcing exactly, which was done symbolically.",
           "Every particular solution (and the integral forms, via the differentiation above) was verified symbolically in `scripts/verify_topic3_topic4.py`."])
    return n


def ex7():
    n = Note(SHEET, 7, "Splitting the Solution of an IVP into Homogeneous and Inhomogeneous Parts", "Initial Value Problem • Superposition • Uniqueness",
             ["problema-resuelto", "pvi-segundo-orden", "superposicion", "unicidad"], SOURCE)
    st = n.statement
    st.p("Show that the solution of the initial value problem")
    st.m(r"L[y] = y'' + p(t)y' + q(t)y = g(t), \qquad y(t_0) = y_0, \quad y'(t_0) = y_0'")
    st.p("can be written as $y(t) = u(t) + v(t)$, where $u$ and $v$ are solutions of two different initial value problems:")
    st.m(r"\begin{aligned} L[u] &= 0, & u(t_0) &= y_0, & u'(t_0) &= y_0', \\ L[v] &= g(t), & v(t_0) &= 0, & v'(t_0) &= 0. \end{aligned}")
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("Hypotheses: $p, q, g$ are continuous on an open interval $I \\ni t_0$. Under these hypotheses the existence and uniqueness theorem (Robinson Thm 11.1, Topic 3 Sec. 1; for linear equations the solution exists on the whole of $I$) states that every IVP $L[w] = h$, $w(t_0) = w_0$, $w'(t_0) = w_1$ has exactly one solution on $I$. Define $L[y] = y'' + p\\,y' + q\\,y$; $L$ is a **linear operator**: $L[\\alpha y_1 + \\beta y_2] = \\alpha L[y_1] + \\beta L[y_2]$ (Robinson Eq. 11.11).")
    p2 = n.phase(2, "Formulation")
    p2.p("Let $y$ be the unique solution of the original IVP, $u$ the unique solution of the homogeneous IVP with the data of $y$, and $v$ the unique solution of the inhomogeneous IVP with zero data (both exist on $I$ by the theorem). The claim is $y = u + v$ on $I$. Proof strategy: show that $u + v$ solves the **original** IVP; uniqueness then forces $u + v = y$.")
    p3 = n.phase(3, "Derivation")
    p3.h(4, "Step 1: $u + v$ solves the differential equation")
    p3.m(r"L[u + v] = L[u] + L[v] = 0 + g(t) = g(t) \quad \text{on } I,")
    p3.p("by linearity of $L$ (differentiation is linear: $(u + v)' = u' + v'$ and $(u + v)'' = u'' + v''$, so $L[u + v] = u'' + v'' + p(u' + v') + q(u + v) = (u'' + pu' + qu) + (v'' + pv' + qv)$).")
    p3.h(4, "Step 2: $u + v$ satisfies the initial conditions")
    p3.m(r"(u + v)(t_0) = u(t_0) + v(t_0) = y_0 + 0 = y_0, \qquad (u + v)'(t_0) = u'(t_0) + v'(t_0) = y_0' + 0 = y_0'")
    p3.h(4, "Step 3: uniqueness")
    p3.p("Both $y$ and $u + v$ solve the IVP $L[w] = g$, $w(t_0) = y_0$, $w'(t_0) = y_0'$ on $I$. By uniqueness (Robinson Thm 11.1), $y = u + v$ on $I$. An equivalent argument that avoids quoting the theorem twice: $w = y - (u + v)$ satisfies $L[w] = g - g = 0$ with $w(t_0) = 0$ and $w'(t_0) = 0$; the zero function solves the same homogeneous IVP, so $w \\equiv 0$ by uniqueness. $\\blacksquare$")
    p3.h(4, "Where the hypotheses were used")
    p3.ul(["Linearity of $L$: Steps 1 and the alternative argument.", "Uniqueness: Step 3. Existence of $u$ and $v$ on all of $I$: needed so that $u + v$ is defined where $y$ is; it holds because $L$ is linear with continuous coefficients."])
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["Meaning: $u$ is the **free response** (the system left to itself with the given initial state) and $v$ the **forced response** from rest (zero state). This is the decomposition used in control and vibration analysis, e.g. $u$ = transient from initial displacement and velocity, $v$ = response to the external force from a state of rest.",
           "It reduces any IVP with general data to two simpler ones: the homogeneous one with the data, and the inhomogeneous one with zero data. Variation of constants gives $v$ directly: with $x_1, x_2$ independent homogeneous solutions and $W$ their Wronskian, $v(t) = \\int_{t_0}^{t}\\dfrac{x_1(s)x_2(t) - x_1(t)x_2(s)}{W(s)}\\,g(s)\\,ds$ (check: $v(t_0) = 0$ and $v'(t_0) = 0$ because the integrand vanishes at $s = t$ and the extra boundary term is $0$).",
           "Example (Exercise 1(ii) of this sheet, $\\ddot x - 4\\dot x = t^2$, $x(0) = 2$, $\\dot x(0) = 0$): $u = 2$ (constant; it solves $\\ddot u - 4\\dot u = 0$ with $u(0) = 2$, $\\dot u(0) = 0$) and $v = x_p + c_1 + c_2e^{4t}$ with $v(0) = \\dot v(0) = 0$; their sum is the solution found there."])
    return n


def ex8():
    n = Note(SHEET, 8, "Reduction of Order for the Inhomogeneous Equation", "Reduction of Order • Integrating Factor • General Solution",
             ["problema-resuelto", "reduccion-de-orden", "factor-integrante", "ecuacion-inhomogenea"], SOURCE)
    st = n.statement
    st.p("The so-called method of reduction of order can be used to find one solution of the inhomogeneous equation $L[y] = y'' + p(t)y' + q(t)y = g(t)$, provided one solution $y_1(t)$ of the corresponding homogeneous equation is known. Indeed, writing $y = v(t)y_1(t)$, show that $y(t)$ satisfies $L[y] = g$ if $v$ is a solution of")
    st.m(r"y_1(t)v'' + \left[2y_1' + p(t)y_1\right]v' = g(t).")
    st.p("This is a first order linear equation for $v'(t)$. Solving this equation, integrating the result, and then multiplying by $y_1(t)$ leads to the general solution of the problem for $y(t)$.")
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("Hypotheses: $p, q, g$ continuous on an interval $I$; $y_1$ is a known solution of $L[y_1] = 0$ with $y_1 \\neq 0$ on $I$ (so that we can divide by $y_1$). Unknown: $v(t)$, with $y = vy_1$.")
    p2 = n.phase(2, "Formulation")
    p2.p("The idea is the same as in Topic 3, Sec. 7: promote the constant in $Ay_1$ to a function, $y = vy_1$. The product rule is used twice:")
    p2.m(r"y' = v'y_1 + vy_1', \qquad y'' = v''y_1 + 2v'y_1' + vy_1''")
    p3 = n.phase(3, "Derivation")
    p3.h(4, "Step 1: substitute in $L[y]$")
    p3.m(r"L[y] = y'' + py' + qy = \left(v''y_1 + 2v'y_1' + vy_1''\right) + p\left(v'y_1 + vy_1'\right) + qvy_1")
    p3.p("Group the terms by $v''$, $v'$ and $v$:")
    p3.m(r"L[y] = y_1v'' + \left(2y_1' + py_1\right)v' + v\underbrace{\left(y_1'' + py_1' + qy_1\right)}_{L[y_1] = 0}")
    p3.p("The bracket multiplying $v$ is $L[y_1]$, which is zero because $y_1$ solves the homogeneous equation; this is why the undifferentiated $v$ disappears. Therefore")
    p3.m(r"L[y] = y_1v'' + \left(2y_1' + py_1\right)v' ")
    p3.p("and $L[y] = g$ holds if and only if $y_1v'' + [2y_1' + py_1]v' = g$, which is the equation of the statement. $\\blacksquare$")
    p3.h(4, "Step 2: solve the first-order equation for $w = v'$")
    p3.p("Divide by $y_1 \\neq 0$ and put $w = v'$:")
    p3.m(r"w' + \left(\frac{2y_1'}{y_1} + p\right)w = \frac{g}{y_1}")
    p3.p("This is a linear first-order equation (Topic 2). The integrating factor is $\\mu = \\exp\\int\\left(\\frac{2y_1'}{y_1} + p\\right)dt = y_1^2\\,e^{P(t)}$, with $P(t) = \\int p\\,dt$ (because $\\int\\frac{2y_1'}{y_1}dt = 2\\ln|y_1|$). The product rule gives $\\frac{d}{dt}(\\mu w) = \\mu w' + \\mu'w = \\mu\\left(w' + \\left(\\frac{2y_1'}{y_1} + p\\right)w\\right) = \\mu\\frac{g}{y_1}$:")
    p3.m(r"\frac{d}{dt}\left(y_1^2e^{P}w\right) = y_1e^{P}g \quad\Longrightarrow\quad w(t) = \frac{1}{y_1^2e^{P}}\left[\int y_1e^{P}g\,dt + c_1\right]")
    p3.h(4, "Step 3: integrate for $v$ and multiply by $y_1$")
    p3.m(r"v(t) = \int w\,dt + c_2, \qquad y(t) = y_1(t)\,v(t) = y_1(t)\left\{c_2 + \int\frac{1}{y_1^2e^{P}}\left[c_1 + \int y_1e^{P}g\,dt\right]dt\right\}")
    p3.p("This expression contains two arbitrary constants $c_1, c_2$. Setting $g = 0$ it reduces to the homogeneous solutions $y = c_2y_1 + c_1y_1\\int\\frac{dt}{y_1^2e^{P}}$ (the second solution of Robinson Exercise 17.7), and the part that does not contain $c_1, c_2$ is a particular solution of $L[y] = g$. The two homogeneous solutions $y_1$ and $y_2 = y_1\\int\\frac{dt}{y_1^2e^{P}}$ are independent: by the product rule $y_2' = y_1'\\int\\frac{dt}{y_1^2e^{P}} + \\frac{1}{y_1e^{P}}$, so $W = y_1y_2' - y_2y_1' = e^{-P} \\neq 0$ (the terms with the integral cancel). Hence complementary function plus particular integral, with two free constants, is the general solution (Robinson Sec. 14.1).")
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["The constant $c_2$ multiplies $y_1$ itself (the known solution) and $c_1$ multiplies $y_1\\int\\frac{dt}{y_1^2e^{P}}$, a second, independent homogeneous solution. Their Wronskian is $W = e^{-P}$, nowhere zero: consistent with Abel's identity $W = W_0\\exp(-\\int p)$.",
           "Check of the Wronskian: $y_2 = y_1\\int\\frac{dt}{y_1^2e^{P}}$ gives $y_2' = y_1'\\int\\frac{dt}{y_1^2e^P} + \\frac{1}{y_1e^{P}}$, hence $W = y_1y_2' - y_2y_1' = \\frac{1}{e^{P}}$ (the $y_1y_1'\\int\\dots$ terms cancel).",
           "Compared with variation of constants, reduction of order needs only **one** homogeneous solution, at the price of two nested integrations.",
           "The method applies on any interval where $y_1 \\neq 0$; where $y_1$ vanishes the division is not allowed and the intervals must be treated separately."])
    return n


def ex9():
    n = Note(SHEET, 9, "A Second Solution of an Euler Equation by Reduction of Order", "Reduction of Order • Euler Equation • Wronskian",
             ["problema-resuelto", "reduccion-de-orden", "ecuacion-de-euler", "wronskiano"], SOURCE)
    st = n.statement
    st.p("For $t > 0$ the function $y_1(t) = 1/t$ is a solution of $t^2\\ddot y - 2t\\dot y - 4y = 0$. Using the previous exercise, find a second, linearly independent solution.")
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("Domain $t > 0$ (so $y_1 = 1/t \\neq 0$). The equation $t^2\\ddot y - 2t\\dot y - 4y = 0$ is homogeneous with variable coefficients; dividing by $t^2$ gives the standard form $\\ddot y + p\\dot y + qy = 0$ with $p(t) = -\\dfrac{2}{t}$, $q(t) = -\\dfrac{4}{t^2}$, continuous for $t > 0$. First check that $y_1$ is a solution:")
    p1.m(r"y_1 = t^{-1},\ \ \dot y_1 = -t^{-2},\ \ \ddot y_1 = 2t^{-3} \;\Rightarrow\; t^2(2t^{-3}) - 2t(-t^{-2}) - 4t^{-1} = 2t^{-1} + 2t^{-1} - 4t^{-1} = 0\ \checkmark")
    p2 = n.phase(2, "Formulation")
    p2.p("Apply Exercise 8 with $g = 0$: write $y = v\\,y_1 = v/t$, so that $v$ must satisfy $y_1\\ddot v + [2\\dot y_1 + py_1]\\dot v = 0$. A second independent solution is $y_2 = v\\,y_1$ with $v$ non-constant.")
    p3 = n.phase(3, "Derivation")
    p3.h(4, "The equation for $v$")
    p3.p("Compute the coefficient: $2\\dot y_1 + py_1 = 2(-t^{-2}) + \\left(-\\dfrac{2}{t}\\right)\\left(\\dfrac1t\\right) = -2t^{-2} - 2t^{-2} = -4t^{-2}$. The equation of Exercise 8 is")
    p3.m(r"\frac1t\,\ddot v - \frac{4}{t^2}\,\dot v = 0 \quad\Longleftrightarrow\quad \ddot v = \frac4t\,\dot v \quad (\text{multiplying by } t)")
    p3.h(4, "Solve for $w = \\dot v$")
    p3.p("$\\dot w = \\dfrac{4}{t}w$ is separable (or use the integrating factor $e^{-4\\ln t} = t^{-4}$): $\\dfrac{d}{dt}(t^{-4}w) = t^{-4}\\dot w - 4t^{-5}w = t^{-4}\\left(\\dot w - \\dfrac4tw\\right) = 0$, so $t^{-4}w = c$ and")
    p3.m(r"w = \dot v = c\,t^4")
    p3.h(4, "Integrate and multiply by $y_1$")
    p3.m(r"v = \int ct^4\,dt = \frac{c}{5}t^5 + b \quad\Longrightarrow\quad y = \frac{v}{t} = \frac{c}{5}t^4 + \frac{b}{t}")
    p3.p("The term in $b$ is the known solution $y_1 = 1/t$; the new, independent solution is (taking $c = 5$, $b = 0$)")
    p3.m(r"\boxed{y_2(t) = t^4}")
    p3.h(4, "Verification")
    p3.p("Substitute: $y_2 = t^4$, $\\dot y_2 = 4t^3$, $\\ddot y_2 = 12t^2$, so $t^2(12t^2) - 2t(4t^3) - 4t^4 = (12 - 8 - 4)t^4 = 0$ $\\checkmark$. Wronskian:")
    p3.m(r"W[y_1, y_2] = y_1\dot y_2 - y_2\dot y_1 = \frac1t(4t^3) - t^4\left(-\frac{1}{t^2}\right) = 4t^2 + t^2 = 5t^2 \neq 0 \quad (t > 0)")
    p3.p("so $y_1$ and $y_2$ are linearly independent on $t > 0$. Abel's identity gives the same dependence on $t$: $W = W_0\\exp\\left(-\\int p\\,dt\\right) = W_0\\exp\\left(\\int\\frac{2}{t}dt\\right) = W_0t^2$, consistent with $5t^2$ ($W_0 = 5$).")
    p4 = n.phase(4, "Interpretation and checks")
    p4.callout("result", "Result", ["A second independent solution is $y_2 = t^4$, and the general solution on $t > 0$ is $y = c_1t^{-1} + c_2t^{4}$."])
    p4.ul(["Euler cross-check: for $t^2\\ddot y - 2t\\dot y - 4y = 0$ the trial $y = t^k$ gives $k(k - 1) - 2k - 4 = k^2 - 3k - 4 = (k - 4)(k + 1) = 0$, so $k = 4, -1$: the same two solutions, found by a different method.",
           "Dimensional/scaling check: under $t \\to \\lambda t$ the Euler equation is invariant and the solutions are homogeneous power functions of degree $-1$ and $4$.",
           "The general solution is not defined at $t = 0$ (where $y_1$ blows up and the equation is singular), consistent with the restriction $t > 0$."])
    CLAIMS.append(dict(kind="ode", id="3II-E9", coeffs=[T ** 2, -2 * T, -4], rhs=0, ics=None, solution=T ** 4, ivar=T, particular=True, euler=True))
    return n
