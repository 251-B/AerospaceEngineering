"""Chapter 4, part 1 (probls_ch4-i_2627_v2.pdf): eleven exercises on first-order systems."""
import sympy as sp

from . import elim, planar, portrait
from .core import Doc, Note, register_figure, tex, vec, mat, t

SHEET = dict(code="Ch4-I", label="4.I", id_prefix="e",
             tema="Tema 4: Systems of First-Order ODEs and the Phase Plane",
             index_note="Problem Set - Chapter 4 Part 1",
             theory_note="Concept - Planar Systems with Complex Eigenvalues")
SOURCE = "probls_ch4-i_2627_v2.pdf"
CLAIMS = []
M = planar.M


def claim_canon(tag, out):
    CLAIMS.append(dict(kind="canon", id=tag, A=out["A"], Q=out["Q"], J=out["J"], sol=out.get("sol")))


# =============================================================================================== Exercise 1
def ex1():
    n = Note(SHEET, 1, "An n-th Order Equation as a First-Order System and Its Uniqueness", "Reduction to a System • Existence and Uniqueness",
             ["problema-resuelto", "sistemas", "reduccion-de-orden", "unicidad"], SOURCE)
    st = n.statement
    st.p("By choosing an appropriate collection of new variables $x_1, \\dots, x_n$, rewrite the $n$th order differential equation")
    st.m(r"\frac{d^nx}{dt^n} = f\left(\frac{d^{n-1}x}{dt^{n-1}}, \dots, \frac{dx}{dt}, x, t\right)")
    st.p("as a set of $n$ coupled linear first order equations. Find the conditions on the function $f(x_n, \\dots, x_1, t)$ for the original differential equation to have a unique solution.")
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("Unknown: $x(t)$, $n$ times differentiable on an interval $I$. Data: $f(x_n, \\dots, x_1, t)$ defined on a region $\\Omega \\subset \\mathbb R^{n+1}$. The initial value problem prescribes the $n$ numbers $x(t_0), \\dot x(t_0), \\dots, x^{(n-1)}(t_0)$. The tool for uniqueness is the existence and uniqueness theorem for first-order systems $\\dot{\\mathbf x} = \\mathbf F(\\mathbf x, t)$ (Robinson Thm 25.2, Topic 4 Sec. 1).")
    p2 = n.phase(2, "Formulation: the new variables")
    p2.p("Introduce one variable for the function and for each derivative below the highest order (Robinson Sec. 25.1):")
    p2.m(r"x_1 = x,\quad x_2 = \frac{dx}{dt},\quad x_3 = \frac{d^2x}{dt^2},\quad \dots,\quad x_n = \frac{d^{n-1}x}{dt^{n-1}}, \qquad\text{i.e. } x_k = x^{(k-1)}\ (k = 1, \dots, n)")
    p3 = n.phase(3, "Derivation")
    p3.h(4, "The system")
    p3.p("By construction $\\dot x_k = x^{(k)} = x_{k+1}$ for $k = 1, \\dots, n - 1$, and $\\dot x_n = x^{(n)} = f(x_n, \\dots, x_1, t)$ by the original equation:")
    p3.m(r"\begin{aligned} \dot x_1 &= x_2 \\ \dot x_2 &= x_3 \\ &\ \,\vdots \\ \dot x_{n-1} &= x_n \\ \dot x_n &= f(x_n, x_{n-1}, \dots, x_1, t) \end{aligned} \qquad\Longleftrightarrow\qquad \dot{\mathbf x} = \mathbf F(\mathbf x, t) = \begin{pmatrix} x_2 \\ x_3 \\ \vdots \\ x_n \\ f(x_n, \dots, x_1, t) \end{pmatrix}")
    p3.p("The first $n - 1$ equations are linear in the unknowns (they say $\\dot x_k = x_{k+1}$); the last one is linear exactly when $f$ is a linear function of $x_1, \\dots, x_n$ (as for a linear ODE, where the whole system is linear, $\\dot{\\mathbf x} = A(t)\\mathbf x + \\mathbf b(t)$). The first-order system form is valid for any $f$.")
    p3.h(4, "Equivalence")
    p3.p("(a) If $x$ solves the $n$th-order equation, then $\\mathbf x = (x, \\dot x, \\dots, x^{(n-1)})^T$ solves the system. (b) Conversely, if $(x_1, \\dots, x_n)$ solves the system, then $\\dot x_1 = x_2$, $\\ddot x_1 = \\dot x_2 = x_3$, ..., $x_1^{(k)} = x_{k+1}$ for $k \\leq n - 1$, and $x_1^{(n)} = \\dot x_n = f(x_n, \\dots, x_1, t) = f(x_1^{(n-1)}, \\dots, \\dot x_1, x_1, t)$: the function $x = x_1$ solves the original equation. The initial condition $\\mathbf x(t_0) = (x_1^0, \\dots, x_n^0)$ is exactly $x(t_0) = x_1^0$, $\\dot x(t_0) = x_2^0$, ..., $x^{(n-1)}(t_0) = x_n^0$.")
    p3.h(4, "Conditions for a unique solution")
    p3.p("Theorem 25.2 (Robinson p. 250) requires $\\mathbf F$ and the matrix of partial derivatives $D\\mathbf F$ to be continuous on an open set containing the initial point. Compute it row by row: for $F_k = x_{k+1}$ ($k < n$) the partial derivatives are $0$ or $1$, and for $F_n = f$ they are $\\partial f/\\partial x_j$:")
    p3.m(r"D\mathbf F = \begin{pmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & & & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1 \\ \dfrac{\partial f}{\partial x_1} & \dfrac{\partial f}{\partial x_2} & \dfrac{\partial f}{\partial x_3} & \cdots & \dfrac{\partial f}{\partial x_n} \end{pmatrix}")
    p3.p("The first $n - 1$ rows are constant, hence continuous. Therefore all the conditions reduce to the last row:")
    p3.callout("result", "Condition for uniqueness", ["**$f(x_n, \\dots, x_1, t)$ and its partial derivatives $\\partial f/\\partial x_j$, $j = 1, \\dots, n$, must be continuous in an open region containing the initial point $(x(t_0), \\dots, x^{(n-1)}(t_0), t_0)$.** Then the IVP has exactly one solution on some interval around $t_0$ (local existence and uniqueness), and two solutions with the same $x(t_0), \\dots, x^{(n-1)}(t_0)$ coincide wherever both exist."])
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["For $n = 2$ the system is $\\dot x_1 = x_2$, $\\dot x_2 = f(x_2, x_1, t)$ and the condition is Theorem 11.1 of Topic 3 (continuity of $f$, $\\partial f/\\partial x_1$, $\\partial f/\\partial x_2$); for $n = 1$ it is Picard's theorem.",
           "No condition on $\\partial f/\\partial t$ is needed: the theorem asks continuity in $t$ but no differentiability in $t$.",
           "Dependence on the $n$ derivatives: continuity of the partial derivatives $\\partial f/\\partial x_j$ gives a local Lipschitz bound in $(x_1, \\dots, x_n)$, which is what excludes branching solutions (compare Exercise 2.14 of Chapter 2, where the Lipschitz condition fails).",
           "For a linear equation $x^{(n)} + a_{n-1}(t)x^{(n-1)} + \\dots + a_0(t)x = g(t)$, $f = g - \\sum a_{k}x_{k+1}$ and $\\partial f/\\partial x_{k+1} = -a_k(t)$: the conditions reduce to continuity of the $a_k$ and $g$. For linear equations the solution in fact exists on the whole interval of continuity of the coefficients (a standard result for linear systems, not in Robinson Thm 25.2, which is local; see the continuation argument in Exercise 4).",
           "Check with the mass-spring-damper (Topic 4 Sec. 1.1): $n = 2$, $f = -\\lambda x_2 - \\omega^2x_1$ has constant partial derivatives $-\\omega^2$ and $-\\lambda$: unique solutions for all data."])
    return n


# =============================================================================================== Exercise 2
SYS = r"\begin{cases} \dfrac{dx}{dt} = a_1(t)x + b_1(t)y, \\[4pt] \dfrac{dy}{dt} = a_2(t)x + b_2(t)y \end{cases}"


def ex2():
    n = Note(SHEET, 2, "Superposition for Homogeneous Linear Systems", "Superposition • Linear Combination of Solutions",
             ["problema-resuelto", "sistemas-lineales", "superposicion"], SOURCE)
    st = n.statement
    st.p("Show that if a homogeneous linear system")
    st.m(r"\begin{cases} \dfrac{dx}{dt} = a_1(t)x + b_1(t)y, \\[4pt] \dfrac{dy}{dt} = a_2(t)x + b_2(t)y \end{cases} \tag{1}")
    st.p("has two solutions")
    st.m(r"\begin{cases} x = x_1(t) \\ y = y_1(t) \end{cases} \quad\text{and}\quad \begin{cases} x = x_2(t) \\ y = y_2(t) \end{cases} \tag{2}")
    st.p("then any linear combination")
    st.m(r"\begin{cases} x = c_1x_1(t) + c_2x_2(t) \\ y = c_1y_1(t) + c_2y_2(t) \end{cases} \tag{3}")
    st.p("with constants $c_1, c_2 \\in \\mathbb R$ is a solution as well.")
    p1 = n.phase(1, "Setup")
    p1.p("Hypotheses: $a_i, b_i$ are functions of $t$ (not necessarily constant) defined on an interval $I$, and $(x_1, y_1)$, $(x_2, y_2)$ are differentiable on $I$ with")
    p1.m(r"\dot x_j = a_1x_j + b_1y_j, \qquad \dot y_j = a_2x_j + b_2y_j \qquad (j = 1, 2) \tag{H}")
    p2 = n.phase(2, "Formulation")
    p2.p("To show: with $x = c_1x_1 + c_2x_2$ and $y = c_1y_1 + c_2y_2$ the two equations of (1) hold. Tool: differentiation is linear, $\\frac{d}{dt}(c_1f + c_2g) = c_1\\dot f + c_2\\dot g$ for constants $c_1, c_2$. In vector notation: $\\mathbf x = c_1\\mathbf x_1 + c_2\\mathbf x_2$ solves $\\dot{\\mathbf x} = A(t)\\mathbf x$ because the right-hand side is linear in $\\mathbf x$ (Robinson Eq. 27.3).")
    p3 = n.phase(3, "Derivation")
    p3.p("First equation. Differentiate $x = c_1x_1 + c_2x_2$ and use (H):")
    p3.m(r"\dot x = c_1\dot x_1 + c_2\dot x_2 = c_1(a_1x_1 + b_1y_1) + c_2(a_1x_2 + b_1y_2)")
    p3.p("Regroup the terms with $a_1$ and with $b_1$:")
    p3.m(r"\dot x = a_1(c_1x_1 + c_2x_2) + b_1(c_1y_1 + c_2y_2) = a_1\,x + b_1\,y")
    p3.p("Second equation. In the same way")
    p3.m(r"\dot y = c_1\dot y_1 + c_2\dot y_2 = c_1(a_2x_1 + b_2y_1) + c_2(a_2x_2 + b_2y_2) = a_2(c_1x_1 + c_2x_2) + b_2(c_1y_1 + c_2y_2) = a_2\,x + b_2\,y")
    p3.p("Both equations of (1) are satisfied by (3). $\\blacksquare$")
    p3.h(4, "Matrix form")
    p3.m(r"\dot{\mathbf x} = c_1\dot{\mathbf x}_1 + c_2\dot{\mathbf x}_2 = c_1A\mathbf x_1 + c_2A\mathbf x_2 = A(c_1\mathbf x_1 + c_2\mathbf x_2) = A\mathbf x, \qquad A(t) = \begin{pmatrix} a_1 & b_1 \\ a_2 & b_2 \end{pmatrix}")
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["Linearity and homogeneity are both used: homogeneity guarantees that the right-hand side of (1) vanishes when $x = y = 0$ (a forcing term $f(t)$ would be multiplied by $c_1 + c_2$ instead of by $1$, and the combination would not be a solution unless $c_1 + c_2 = 1$ and so on).",
           "Constant coefficients were not needed: only linearity of the derivative and of $(x, y) \\mapsto (a_1x + b_1y, a_2x + b_2y)$.",
           "The set of solutions is therefore a vector space; Exercises 3 and 4 show that it has dimension $2$.",
           "Quick example: $\\dot x = y$, $\\dot y = -x$ has $(\\cos t, -\\sin t)$ and $(\\sin t, \\cos t)$ as solutions, and so $(c_1\\cos t + c_2\\sin t,\\ -c_1\\sin t + c_2\\cos t)$ does."])
    return n


def ex3():
    n = Note(SHEET, 3, "The Wronskian of a Linear System: Liouville's Formula and the Dichotomy", "Wronskian • Liouville • Dichotomy",
             ["problema-resuelto", "wronskiano", "formula-de-liouville", "sistemas-lineales"], SOURCE)
    st = n.statement
    st.p("Show that given a homogeneous linear system (1) with continuous coefficients in $[a, b]$, then the Wronskian $W(t)$ of two solutions (2) satisfies the first order ODE")
    st.m(r"\frac{dW}{dt} = \left(a_1(t) + b_2(t)\right)W.")
    st.p("Deduce that this Wronskian is either identically $0$ or nowhere zero in $[a, b]$.")
    p1 = n.phase(1, "Setup")
    p1.p("System (1) of Exercise 2 with $a_1, b_1, a_2, b_2$ continuous on $[a, b]$. For two solutions $(x_1, y_1)$ and $(x_2, y_2)$ the Wronskian is the determinant of the matrix whose columns are the solutions (Topic 4 Sec. 3):")
    p1.m(r"W(t) = \begin{vmatrix} x_1 & x_2 \\ y_1 & y_2 \end{vmatrix} = x_1y_2 - x_2y_1")
    p2 = n.phase(2, "Formulation")
    p2.p("Differentiate $W$ with the product rule, substitute the equations (H) of Exercise 2 for each derivative, and recognise $W$. The resulting scalar linear ODE is solved by an integrating factor.")
    p3 = n.phase(3, "Derivation")
    p3.h(4, "Step 1: the product rule")
    p3.m(r"\dot W = \dot x_1y_2 + x_1\dot y_2 - \dot x_2y_1 - x_2\dot y_1")
    p3.h(4, "Step 2: substitute the system")
    p3.m(r"\dot W = (a_1x_1 + b_1y_1)y_2 + x_1(a_2x_2 + b_2y_2) - (a_1x_2 + b_1y_2)y_1 - x_2(a_2x_1 + b_2y_1)")
    p3.p("Expand and collect by coefficient:")
    p3.m(r"\dot W = a_1(x_1y_2 - x_2y_1) + b_2(x_1y_2 - x_2y_1) + b_1(y_1y_2 - y_2y_1) + a_2(x_1x_2 - x_2x_1)")
    p3.p("The terms in $b_1$ and $a_2$ vanish identically ($y_1y_2 - y_2y_1 = 0$ and $x_1x_2 - x_2x_1 = 0$), and the remaining brackets are $W$:")
    p3.m(r"\boxed{\dot W = \left(a_1 + b_2\right)W} \qquad (= (\operatorname{tr}A)\,W)")
    p3.h(4, "Step 3: solve the scalar equation")
    p3.p("Let $\\tau(t) = \\int_{t_0}^{t}\\left[a_1(s) + b_2(s)\\right]ds$, which exists and is differentiable because $a_1 + b_2$ is continuous, with $\\tau'(t) = a_1(t) + b_2(t)$ (fundamental theorem of calculus). The chain rule gives $\\frac{d}{dt}e^{-\\tau(t)} = -\\tau'(t)e^{-\\tau(t)}$, so by the product rule $\\frac{d}{dt}\\left(e^{-\\tau}W\\right) = e^{-\\tau}\\dot W - \\tau'e^{-\\tau}W = e^{-\\tau}(\\dot W - \\tau'W) = e^{-\\tau}\\left(\\dot W - (a_1 + b_2)W\\right) = 0$, so $e^{-\\tau}W$ is constant on $[a, b]$. Barrow's rule, $[e^{-\\tau(s)}W(s)]_{t_0}^{t} = 0$, gives $e^{-\\tau(t)}W(t) = e^{-\\tau(t_0)}W(t_0) = W(t_0)$ (as $\\tau(t_0) = 0$):")
    p3.m(r"W(t) = W(t_0)\exp\left(\int_{t_0}^{t}\left[a_1(s) + b_2(s)\right]ds\right), \qquad t \in [a, b]")
    p3.h(4, "Step 4: the dichotomy")
    p3.p("The exponential is finite and strictly positive, so $W(t) = 0$ exactly when $W(t_0) = 0$. Since $t_0 \\in [a, b]$ was arbitrary: either $W(t_0) = 0$ for one (hence every) $t_0$, and then $W \\equiv 0$ on $[a, b]$; or $W(t_0) \\neq 0$ for one (hence every) $t_0$, and then $W$ does not vanish anywhere on $[a, b]$. There is no third possibility. $\\blacksquare$")
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["Constant coefficients: $W(t) = W(0)e^{(a_1 + b_2)t} = W(0)e^{(\\operatorname{tr}A)t}$ (Topic 4 Sec. 3, Liouville). Check with Example 28.1: eigenvalues $2$ and $-3$ have trace $-1$ and $W \\propto e^{2t}e^{-3t} = e^{-t}$.",
           "For the system of a second-order equation $\\ddot x + p\\dot x + qx = 0$, $a_1 = 0$ and $b_2 = -p$ and the result is Abel's identity $\\dot W = -pW$ (Exercise 6).",
           "Geometric meaning: $|W|$ is the area of the parallelogram spanned by the two solution vectors; $\\operatorname{tr}A$ is the divergence of the flow, which rates the growth of areas. If $\\operatorname{tr}A = 0$ areas are conserved ($W$ constant).",
           "This dichotomy is what makes the Wronskian a test for independence: it is enough to evaluate it at a single instant (Exercise 4)."])
    return n


def ex4():
    n = Note(SHEET, 4, "A Non-Vanishing Wronskian Gives the General Solution", "Fundamental Set • General Solution • Uniqueness",
             ["problema-resuelto", "wronskiano", "solucion-general", "sistemas-lineales"], SOURCE)
    st = n.statement
    st.p("Show that if two solutions (2) of (1) have a Wronskian that does not vanish in $[a, b]$, then (3) gives the general solution of the system.")
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("System (1) with coefficients continuous on $[a, b]$ (as in Exercise 3). $(x_1, y_1)$ and $(x_2, y_2)$ are solutions with $W(t) = x_1y_2 - x_2y_1 \\neq 0$ for all $t \\in [a, b]$. To show: for every solution $(x, y)$ of (1) there are constants $c_1, c_2$ with $x = c_1x_1 + c_2x_2$ and $y = c_1y_1 + c_2y_2$ on $[a, b]$. (By Exercise 2 every combination is a solution, so this shows that (3) describes all of them.)")
    p2 = n.phase(2, "Formulation")
    p2.p("Tools: (a) uniqueness for linear systems with continuous coefficients: two solutions with the same value at one instant $t_0 \\in [a, b]$ coincide on all of $[a, b]$. Robinson Thm 25.2 gives this locally (near $t_0$); the extension to $[a, b]$ is a continuation argument: the set $S$ of instants where the two solutions agree contains $t_0$, is closed (the solutions are continuous) and is open in $[a, b]$ (at each point of $S$ the local uniqueness applies, since the coefficients are continuous), and an interval is connected, so $S = [a, b]$; (b) Cramer's rule: a $2\\times 2$ linear system with non-zero determinant has exactly one solution. Plan: match the given solution at one instant with a combination, then invoke uniqueness.")
    p3 = n.phase(3, "Derivation")
    p3.h(4, "Step 1: choose the constants at one instant")
    p3.p("Let $(x, y)$ be any solution and fix $t_0 \\in [a, b]$. We look for $c_1, c_2$ such that the combination equals $(x, y)$ at $t_0$:")
    p3.m(r"\begin{pmatrix} x_1(t_0) & x_2(t_0) \\ y_1(t_0) & y_2(t_0) \end{pmatrix}\begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = \begin{pmatrix} x(t_0) \\ y(t_0) \end{pmatrix}")
    p3.p("The determinant of the coefficient matrix is $W(t_0) \\neq 0$ by hypothesis, so there is exactly one solution (Cramer):")
    p3.m(r"c_1 = \frac{x(t_0)y_2(t_0) - x_2(t_0)y(t_0)}{W(t_0)}, \qquad c_2 = \frac{x_1(t_0)y(t_0) - x(t_0)y_1(t_0)}{W(t_0)}")
    p3.h(4, "Step 2: uniqueness")
    p3.p("Define $\\tilde x = c_1x_1 + c_2x_2$, $\\tilde y = c_1y_1 + c_2y_2$. By Exercise 2 $(\\tilde x, \\tilde y)$ solves (1), and by Step 1 $(\\tilde x(t_0), \\tilde y(t_0)) = (x(t_0), y(t_0))$. Both $(x, y)$ and $(\\tilde x, \\tilde y)$ solve the same IVP at $t_0$, so by uniqueness $(x, y) = (\\tilde x, \\tilde y)$ on $[a, b]$. $\\blacksquare$")
    p3.h(4, "Where Exercise 3 enters")
    p3.p("If the Wronskian were known not to vanish at only some $t_0$, the argument would work at that $t_0$; Exercise 3 shows that a non-zero value at one point already implies $W \\neq 0$ everywhere, so one test is enough. Also, two solutions with $W \\equiv 0$ cannot form a general solution: then the matrix above is singular at each instant, and not every initial vector can be matched.")
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["The solution space is a 2-dimensional vector space with basis $\\{(x_1, y_1), (x_2, y_2)\\}$ (a **fundamental set**; $\\Phi = [\\mathbf x_1\\ \\mathbf x_2]$ is a fundamental matrix and $\\mathbf c = \\Phi(t_0)^{-1}\\mathbf x(t_0)$, Topic 4 Sec. 3).",
           "Example: for $\\dot x = x + y$, $\\dot y = 4x - 2y$ the solutions $e^{2t}(1, 1)$ and $e^{-3t}(1, -4)$ have $W = e^{2t}e^{-3t}(-4 - 1) = -5e^{-t} \\neq 0$, hence form a fundamental set (Topic 4 Example 28.1).",
           "Check: if $x_2 = kx_1$ and $y_2 = ky_1$ (parallel solutions) then $W = kx_1y_1 - kx_1y_1 = 0$ and the argument rightly fails.",
           "The same proof works for $n \\times n$ systems with $\\det\\Phi(t_0) \\neq 0$."])
    return n


def ex5():
    n = Note(SHEET, 5, "General Solution of an Inhomogeneous System", "Inhomogeneous System • Particular Solution",
             ["problema-resuelto", "sistemas-inhomogeneos", "solucion-particular"], SOURCE)
    st = n.statement
    st.p("Suppose that we have an inhomogeneous system")
    st.m(r"\begin{cases} \dfrac{dx}{dt} = a_1(t)x + b_1(t)y + f_1(t), \\[4pt] \dfrac{dy}{dt} = a_2(t)x + b_2(t)y + f_2(t) \end{cases} \tag{4}")
    st.p("and one particular solution")
    st.m(r"\begin{cases} x = x_p(t) \\ y = y_p(t). \end{cases} \tag{5}")
    st.p("Show that, if $x_1(t)$ and $x_2(t)$ are linearly independent solutions of the homogeneous system, then the general solution of (4) is")
    st.m(r"\begin{cases} x = c_1x_1(t) + c_2x_2(t) + x_p(t) \\ y = c_1y_1(t) + c_2y_2(t) + y_p(t) \end{cases}")
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("Coefficients and forcings $f_1, f_2$ continuous on $[a, b]$. The homogeneous system is (1) of Exercise 2. $\\mathbf x_1 = (x_1, y_1)$ and $\\mathbf x_2 = (x_2, y_2)$ are linearly independent solutions of (1) (the statement writes \"$x_1(t)$ and $x_2(t)$\" for the two solution vectors). Their Wronskian is non-zero on $[a, b]$: by Exercise 3 it is either $\\equiv 0$ or never zero, and if $W(t_0) = 0$ there would be $(c_1, c_2) \\neq (0, 0)$ with $c_1\\mathbf x_1(t_0) + c_2\\mathbf x_2(t_0) = \\mathbf 0$; the combination $c_1\\mathbf x_1 + c_2\\mathbf x_2$ solves (1) with zero data at $t_0$, so it is $\\equiv \\mathbf 0$ by uniqueness (Exercise 4, Step 2), contradicting independence. $\\mathbf x_p = (x_p, y_p)$ solves (4).")
    p2 = n.phase(2, "Formulation")
    p2.p("Two claims: (A) every function of the displayed form solves (4); (B) every solution of (4) has that form. The key idea (Robinson Sec. 14.1 for scalar equations, Topic 4 Sec. 3.1) is that the difference of two solutions of (4) solves the **homogeneous** system.")
    p3 = n.phase(3, "Derivation")
    p3.h(4, "(A) The family solves (4)")
    p3.p("Write $\\mathbf x = c_1\\mathbf x_1 + c_2\\mathbf x_2 + \\mathbf x_p$ and $\\dot{\\mathbf x} = A\\mathbf x + \\mathbf f$ with $A = \\begin{pmatrix} a_1 & b_1 \\\\ a_2 & b_2 \\end{pmatrix}$, $\\mathbf f = (f_1, f_2)^T$. Using $\\dot{\\mathbf x}_j = A\\mathbf x_j$ and $\\dot{\\mathbf x}_p = A\\mathbf x_p + \\mathbf f$:")
    p3.m(r"\dot{\mathbf x} = c_1A\mathbf x_1 + c_2A\mathbf x_2 + A\mathbf x_p + \mathbf f = A(c_1\mathbf x_1 + c_2\mathbf x_2 + \mathbf x_p) + \mathbf f = A\mathbf x + \mathbf f")
    p3.h(4, "(B) Every solution has this form")
    p3.p("Let $\\mathbf x = (x, y)$ be any solution of (4) and put $\\mathbf z = \\mathbf x - \\mathbf x_p$. Then")
    p3.m(r"\dot{\mathbf z} = \dot{\mathbf x} - \dot{\mathbf x}_p = (A\mathbf x + \mathbf f) - (A\mathbf x_p + \mathbf f) = A(\mathbf x - \mathbf x_p) = A\mathbf z")
    p3.p("so $\\mathbf z$ solves the homogeneous system (1). Since $\\mathbf x_1, \\mathbf x_2$ are independent solutions of (1) (non-zero Wronskian), Exercise 4 gives constants $c_1, c_2$ with $\\mathbf z = c_1\\mathbf x_1 + c_2\\mathbf x_2$. Hence $\\mathbf x = c_1\\mathbf x_1 + c_2\\mathbf x_2 + \\mathbf x_p$. $\\blacksquare$")
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["The structure \"general = complementary + particular\" is the same as for scalar linear equations (Topic 3 Sec. 5 lemma). The two constants are fixed by an initial condition $\\mathbf x(t_0) = \\mathbf x_0$: $\\mathbf c = \\Phi(t_0)^{-1}\\left[\\mathbf x_0 - \\mathbf x_p(t_0)\\right]$.",
           "Example (Topic 4 Example 26.1): $\\dot x = x + y$, $\\dot y = 4x - 2y + 4e^{-2t}$ has the particular solution $(-e^{-2t}, 3e^{-2t})$: check $\\dot x_p = 2e^{-2t} = x_p + y_p = -e^{-2t} + 3e^{-2t}$ and $\\dot y_p = -6e^{-2t} = 4(-e^{-2t}) - 2(3e^{-2t}) + 4e^{-2t} = -6e^{-2t}$.",
           "A particular solution can be found by elimination (Exercise 7), undetermined coefficients, or variation of parameters $\\mathbf x_p = \\Phi\\int\\Phi^{-1}\\mathbf f$ (Topic 4 Sec. 3.1).",
           "Different particular solutions differ by a homogeneous solution, which is absorbed in $c_1, c_2$."])
    return n


def ex6():
    n = Note(SHEET, 6, "A Second-Order Equation as a System: the Two Wronskians Coincide", "Second Order to System • Wronskian • Abel",
             ["problema-resuelto", "wronskiano", "sistemas", "identidad-de-abel"], SOURCE)
    st = n.statement
    st.p("Suppose that we have a second order linear ODE $x''(t) + p(t)x'(t) + q(t)x(t) = 0$, and two solutions $x_1(t)$ and $x_2(t)$. Write it as a linear system of two first order ODEs. Check that if")
    st.m(r"\begin{cases} x = x_1(t) \\ y = y_1(t) \end{cases} \quad\text{and}\quad \begin{cases} x = x_2(t) \\ y = y_2(t) \end{cases}")
    st.p("are the corresponding solutions of the system, then the Wronskian as defined in this chapter coincides with the definition that we had before for second order ODEs.")
    p1 = n.phase(1, "Setup")
    p1.p("$p, q$ continuous on an interval $I$. Two definitions to compare: the scalar Wronskian $W_2[x_1, x_2] = x_1x_2' - x_2x_1'$ (Topic 3 Sec. 2.1) and the Wronskian of vector solutions $W_{sys} = \\det[\\mathbf x_1\\ \\mathbf x_2]$ (Topic 4 Sec. 3).")
    p2 = n.phase(2, "Formulation: the system")
    p2.p("Introduce $y = x'$ (Robinson Sec. 25.1: $x_1 \\to x$, $x_2 \\to x'$). Then $x' = y$ and, from the ODE, $y' = x'' = -p\\,x' - q\\,x = -q\\,x - p\\,y$:")
    p2.m(r"\begin{cases} x' = 0\cdot x + 1\cdot y \\ y' = -q(t)\,x - p(t)\,y \end{cases} \qquad \dot{\mathbf x} = \begin{pmatrix} 0 & 1 \\ -q & -p \end{pmatrix}\mathbf x")
    p2.p("This has the form (1) with $a_1 = 0$, $b_1 = 1$, $a_2 = -q$, $b_2 = -p$ (continuous). A solution $x_j(t)$ of the ODE gives the solution $(x_j, y_j) = (x_j, x_j')$ of the system, and conversely the first component of a system solution solves the ODE.")
    p3 = n.phase(3, "Derivation")
    p3.p("The corresponding solutions of the system are $\\mathbf x_1 = (x_1, x_1')^T$ and $\\mathbf x_2 = (x_2, x_2')^T$, so $y_j = x_j'$. Their system Wronskian is")
    p3.m(r"W_{sys} = \begin{vmatrix} x_1 & x_2 \\ y_1 & y_2 \end{vmatrix} = x_1y_2 - x_2y_1 = x_1x_2' - x_2x_1' = W_2[x_1, x_2]")
    p3.p("The two definitions coincide identically. $\\blacksquare$")
    p3.h(4, "Consistency with Exercise 3")
    p3.p("Exercise 3 applied to this system ($a_1 + b_2 = 0 + (-p) = -p$) gives $\\dot W = -pW$, i.e. $W(t) = W(t_0)\\exp\\left(-\\int_{t_0}^{t}p\\right)$, which is Abel's identity of Topic 3 (Robinson Exercise 11.2). Direct check from the scalar definition: $W_2' = x_1'x_2' + x_1x_2'' - x_2'x_1' - x_2x_1'' = x_1x_2'' - x_2x_1'' = x_1(-px_2' - qx_2) - x_2(-px_1' - qx_1) = -p(x_1x_2' - x_2x_1') = -pW_2$, the same equation.")
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["Therefore all the theory of systems (non-vanishing Wronskian $\\Leftrightarrow$ independence, general solution, dichotomy) contains the scalar results of Topic 3 as the special case $A = \\begin{pmatrix} 0 & 1 \\\\ -q & -p \\end{pmatrix}$; the notation $\\mathbf x(t_0) = (x(t_0), \\dot x(t_0))$ for the initial data is the same pair as in Theorem 11.1.",
           "Example: $\\ddot x + x = 0$, $x_1 = \\cos t$, $x_2 = \\sin t$: $W_2 = \\cos^2t + \\sin^2t = 1$ and $W_{sys} = \\begin{vmatrix} \\cos t & \\sin t \\\\ -\\sin t & \\cos t \\end{vmatrix} = 1$; $p = 0$ so $W$ is constant, as Abel/Liouville predict.",
           "The matrix $\\begin{pmatrix} 0 & 1 \\\\ -q & -p \\end{pmatrix}$ has trace $-p$ and determinant $q$; for constants it gives the characteristic polynomial $\\mu^2 + p\\mu + q$ of Topic 3."])
    return n


# =============================================================================================== Exercise 7
EX7 = [
    ("i", (4, -1, 2, 1, 0, t ** 2, 0, 1, None), r"\dot x = 4x - y,\quad \dot y = 2x + y + t^2", "x(0) = 0,\\ y(0) = 1"),
    ("ii", (1, -4, 1, 1, sp.cos(2 * t), 0, 1, 1, None), r"\dot x = x - 4y + \cos 2t,\quad \dot y = x + y", "x(0) = 1,\\ y(0) = 1"),
    ("iii", (2, 2, 6, 3, 0, sp.exp(t), 0, None, 1), r"\dot x = 2x + 2y,\quad \dot y = 6x + 3y + e^{t}", "x(0) = 0,\\ \\dot x(0) = 1"),
    ("iv", (5, -4, 1, 1, sp.exp(3 * t), 0, 1, -1, None), r"\dot x = 5x - 4y + e^{3t},\quad \dot y = x + y", "x(0) = 1,\\ y(0) = -1"),
    ("v", (2, 5, -2, 0, 0, sp.cos(3 * t), 2, -1, None), r"\dot x = 2x + 5y,\quad \dot y = -2x + \cos 3t", "x(0) = 2,\\ y(0) = -1"),
    ("vi", (1, 1, 4, -2, sp.exp(-t), sp.exp(2 * t), 1, -1, None), r"\dot x = x + y + e^{-t},\quad \dot y = 4x - 2y + e^{2t}", "x(0) = 1,\\ y(0) = -1"),
    ("vii", (8, 14, 7, 1, 0, 0, 1, 1, None), r"\dot x = 8x + 14y,\quad \dot y = 7x + y", "x(0) = y(0) = 1"),
]


def ex7():
    n = Note(SHEET, 7, "Seven Linear Systems Solved by Elimination", "Elimination Method • Seven IVPs • Undetermined Coefficients",
             ["problema-resuelto", "metodo-de-eliminacion", "sistemas-lineales", "pvi"], SOURCE)
    st = n.statement
    st.p("Find the general solutions of the following differential equations by converting them into a single second-order equation. Also find the solution that satisfies the given initial conditions.")
    st.ul([f"({l}) ${eq}$, $\\quad {ic}$;" if l != "vii" else f"({l}) ${eq}$, $\\quad {ic}$." for l, _, eq, ic in EX7])
    p1 = n.phase(1, "Setup and classification")
    p1.p("Each system is linear with constant coefficients, of the form $\\dot x = ax + by + f(t)$, $\\dot y = cx + dy + g(t)$ (Robinson Eq. 26.1), homogeneous when $f = g = 0$. In every item $b \\neq 0$, so the first equation can be solved for $y$. Hypotheses: coefficients and forcings continuous on $\\mathbb R$, so the IVP has a unique solution, which exists on all of $\\mathbb R$ (linear system with continuous coefficients; Thm 25.2 gives local existence and uniqueness and the continuation argument of Exercise 4 extends it). Item (iii) gives $x(0)$ and $\\dot x(0)$; the value of $y(0)$ then follows from the first equation.")
    p2 = n.phase(2, "Method: elimination (Topic 4 Sec. 2.1)")
    p2.p("Solve the first equation for $y = (\\dot x - ax - f)/b$ (26.2), differentiate, and substitute in the second equation. The result is one second-order equation for $x$ (26.3):")
    p2.m(r"\ddot x - (a + d)\dot x + (ad - bc)x = \dot f + bg - df")
    p2.p("Its coefficients are the trace and determinant of the matrix $\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$, so its characteristic polynomial is the one of the eigenvalue method. It is solved by the methods of Topic 3 (complementary function plus undetermined coefficients). Then $y$ is recovered from (26.2) and the constants from the data.")
    p3 = n.phase(3, "Derivation of the seven solutions")
    finals = {}
    for l, (a, b, c, d, f, g, x0, y0, xd0), eq, ic in EX7:
        p3.h(3, f"({l}) ${eq}$, $\\ {ic}$")
        x, y, info = elim.eliminate(p3, a, b, c, d, f, g, x0, y0, xd0)
        finals[l] = (x, y)
        CLAIMS.append(dict(kind="system", id=f"4I-E7-{l}", A=sp.Matrix([[a, b], [c, d]]), f=sp.sympify(f), g=sp.sympify(g), x0=info["x0"], y0=info["y0"], sol=(x, y)))
    p4 = n.phase(4, "Interpretation and checks")
    p4.table(["Item", "$x(t)$", "$y(t)$"], [[f"({l})", f"${tex(finals[l][0])}$", f"${tex(finals[l][1])}$"] for l, *_ in EX7])
    p4.ul(["Every pair $(x, y)$ was substituted in **both** original equations and in the initial data (shown in each item and re-checked symbolically in `scripts/verify_topic3_topic4.py`).",
           "Characteristic exponents seen: (i) $2, 3$ (real); (ii) $1 \\pm 2i$ (spiral) with the forcing $\\cos 2t$ at a different frequency; (iii) $6, -1$ (saddle; the forcing $e^{t}$ has exponent $1$, which is **not** a root, so no extra factor $t$); (iv) $3$ double (improper-node type), and the forcing $e^{3t}$ resonates with the double root, giving $t^2e^{3t}$; (v) $1 \\pm 3i$; (vi) $2, -3$ with the forcing exponent $2$ resonant (term $te^{2t}$) and $-1$ not; (vii) $15, -6$ (homogeneous saddle).",
           "Cross-check of the homogeneous parts with Topic 4: (iv) and (v) have the same matrices as Examples 8.2 and 7.1; (vii) is the matrix of Exercise 9 (i).",
           "Dimensions: with $t$ in seconds the matrix entries have units s$^{-1}$ and the forcings those of $\\dot x$; the elimination keeps this consistent ($a + d$ in s$^{-1}$, $ad - bc$ in s$^{-2}$)."])
    return n
