"""Chapter 4, part 1, exercises 8 to 11: real eigenvalues, decoupling, uncoupled trajectories, a zero eigenvalue."""
import sympy as sp

from . import planar, portrait
from .ch4a import CLAIMS, SHEET, SOURCE, claim_canon
from .core import Note, register_figure, tex, vec, t

M = planar.M
EX8 = [
    ("i", 1, (1, 1), 2, (1, -1)), ("ii", 1, (1, 0), -2, (1, 1)), ("iii", -2, (1, 2), -3, (2, -3)), ("iv", 3, (2, 3), -5, (0, 1)),
    ("v", 3, (1, 2), 1, (1, -3)), ("vi", 2, (0, 1), -3, (1, 5)), ("vii", 1, (1, 1), 2, (2, 1)), ("viii", -3, (1, 3), -1, (-3, 2)),
]


def build_A(doc, l1, v1, l2, v2):
    """A = Q Lambda Q^{-1} from the eigen-data, with the products written out; returns A."""
    Q = sp.Matrix.hstack(sp.Matrix(v1), sp.Matrix(v2))
    Lam = sp.diag(l1, l2)
    A = sp.simplify(Q * Lam * Q.inv())
    doc.p("The statement gives the eigen-data, not the matrix. Since $A\\mathbf v_j = \\lambda_j\\mathbf v_j$ for $j = 1, 2$ means $AQ = Q\\Lambda$ with $Q = [\\mathbf v_1 \\mid \\mathbf v_2]$, the matrix is $A = Q\\Lambda Q^{-1}$ (it is needed to draw the portrait and to check the data):")
    doc.m(f"Q = {M(Q)}, \\qquad \\Lambda = {M(Lam)}, \\qquad \\det Q = {tex(Q.det())}, \\qquad Q^{{-1}} = {M(Q.inv())}")
    QL = planar.matmul_steps(doc, Q, Lam, "Q", "\\Lambda", "Q\\Lambda")
    doc.m(f"Q\\Lambda = {M(QL)}")
    A2 = planar.matmul_steps(doc, QL, Q.inv(), "(Q\\Lambda)", "Q^{-1}", "A")
    assert A2 == A
    doc.m(f"A = Q\\Lambda Q^{{-1}} = {M(A)}")
    return A


def ex8():
    n = Note(SHEET, 8, "General Solution and Phase Portrait from Eigenvalues and Eigenvectors", "Eigen-data • Nodes and Saddles • Eight Portraits",
             ["problema-resuelto", "retrato-de-fase", "nodos", "puntos-silla", "autovalores-reales"], SOURCE)
    st = n.statement
    st.p("Write down the general solution and draw the phase portrait for the equation $\\dot{\\mathbf x} = A\\mathbf x$, when the eigenvalues and eigenvectors of $A$ are as given in each case. You should take particular care with stable (or unstable) nodes to ensure that the trajectories approach (or move away from) the origin tangent to the correct eigenvector.")
    st.ul([f"({l}) $\\lambda_1 = {a}$, $\\mathbf v_1 = ({v1[0]}, {v1[1]})$ and $\\lambda_2 = {b}$, $\\mathbf v_2 = ({v2[0]}, {v2[1]})$;" for l, a, v1, b, v2 in EX8])
    p1 = n.phase(1, "Setup and classification")
    p1.p("In every item the two eigenvalues are real and distinct, with linearly independent eigenvectors (so $\\det[\\mathbf v_1\\ \\mathbf v_2] \\neq 0$, checked in each item). The general solution is then $\\mathbf x = c_1e^{\\lambda_1t}\\mathbf v_1 + c_2e^{\\lambda_2t}\\mathbf v_2$ (Robinson Eq. 28.1) and the portrait is determined by the signs of $\\lambda_1, \\lambda_2$ (Topic 4 Sec. 6 and 9):")
    p1.table(["Signs", "Origin", "Behaviour"],
             [["$\\lambda_1, \\lambda_2 < 0$", "stable node", "all orbits tend to $\\mathbf 0$, tangent to the eigenvector of the smaller $|\\lambda|$"],
              ["$\\lambda_1, \\lambda_2 > 0$", "unstable node", "all orbits leave $\\mathbf 0$, tangent to the eigenvector of the smaller $|\\lambda|$"],
              ["$\\lambda_1\\lambda_2 < 0$", "saddle", "only the orbits on the stable eigenline reach $\\mathbf 0$"]])
    p1.table(["Item", "$\\lambda_1, \\lambda_2$", "Type", "Slow direction (smaller $|\\lambda|$)"],
             [[f"({l})", f"${a}, {b}$", ("stable node" if a < 0 and b < 0 else "unstable node" if a > 0 and b > 0 else "saddle"),
               (f"$\\mathbf v_{1 if abs(a) < abs(b) else 2}$ = $({(v1 if abs(a) < abs(b) else v2)[0]}, {(v1 if abs(a) < abs(b) else v2)[1]})$" if a * b > 0 else "not applicable")] for l, a, v1, b, v2 in EX8])
    p2 = n.phase(2, "Formulation: how each item is treated")
    p2.p("For each item: (1) the general solution; (2) the matrix $A = Q\\Lambda Q^{-1}$ reconstructed from the data, used to draw and to check; (3) the canonical system $\\dot{\\mathbf z} = \\Lambda\\mathbf z$ with $\\mathbf z = Q^{-1}\\mathbf x$ and its solution; (4) the portrait in the $\\mathbf z$-plane and its image under $\\mathbf x = Q\\mathbf z$ in the $(x, y)$-plane, with the arrows and the tangent direction decided by the rules above.")
    p3 = n.phase(3, "Derivation of the eight portraits")
    for l, a, v1, b, v2 in EX8:
        p3.h(3, f"({l}) $\\lambda_1 = {a}$, $\\mathbf v_1 = ({v1[0]}, {v1[1]})^T$; $\\lambda_2 = {b}$, $\\mathbf v_2 = ({v2[0]}, {v2[1]})^T$")
        A = build_A(p3, a, v1, b, v2)
        out = planar.real_distinct(p3, A, "t", given=((sp.Integer(a), sp.Matrix(v1)), (sp.Integer(b), sp.Matrix(v2))))
        claim_canon(f"4I-E8-{l}", out)
        portrait.portrait(p3, out, f"ch4a-e8-{l}")
    p4 = n.phase(4, "Interpretation and checks")
    rows = []
    for l, a, v1, b, v2 in EX8:
        rows.append([f"({l})", f"$\\mathbf x = c_1e^{{{a}t}}\\begin{{pmatrix}} {v1[0]} \\\\ {v1[1]} \\end{{pmatrix}} + c_2e^{{{b}t}}\\begin{{pmatrix}} {v2[0]} \\\\ {v2[1]} \\end{{pmatrix}}$"])
    p4.table(["Item", "General solution"], rows)
    p4.ul(["In every item the reconstructed $A$ satisfies $A\\mathbf v_j = \\lambda_j\\mathbf v_j$ (checked in the text) and $\\det A = \\lambda_1\\lambda_2$, $\\operatorname{tr}A = \\lambda_1 + \\lambda_2$.",
           "Nodes: the tangent direction at the origin is the eigenvector of the **smaller** $|\\lambda|$ because $|z_2|/|z_1|^{\\lambda_2/\\lambda_1}$ is constant: if $|\\lambda_2| > |\\lambda_1|$ the exponent $r = \\lambda_2/\\lambda_1$ exceeds $1$, so $z_2 = K|z_1|^{r}$ tends to $0$ faster than $z_1$ and the curve hugs the $z_1$-axis (the slower eigendirection) near the origin; if $r < 1$ it hugs the $z_2$-axis, which is then the slower one. The phase portraits drawn above show this numerically (curves integrated from the matrix $A$ itself, not from the formula, so the tangency is a genuine check).",
           "Saddles (ii), (iv), (vi): the stable manifold is the eigenline of the negative eigenvalue.",
           "Items (ii), (iv) and (vi) have an eigenvector with a zero entry ((ii) $\\mathbf v_1 = (1, 0)$, (iv) $\\mathbf v_2 = (0, 1)$, (vi) $\\mathbf v_1 = (0, 1)$): that eigenline is an axis of the $(x, y)$-plane."])
    return n


EX9 = [("i", [[8, 14], [7, 1]]), ("ii", [[2, 0], [-5, -3]]), ("iii", [[11, -2], [3, 4]]), ("iv", [[1, 20], [40, -19]])]


def ex9():
    n = Note(SHEET, 9, "Decoupling Four Systems with Real Eigenvalues", "Diagonalisation • Decoupling • Four Matrices",
             ["problema-resuelto", "diagonalizacion", "desacoplamiento", "retrato-de-fase"], SOURCE)
    st = n.statement
    st.p("Find the eigenvalues and eigenvectors of the matrix on the right-hand side in each case, and hence find the coordinate transformation that will decouple the corresponding equations. Show that this transformation has the desired effect. You can also write down the general solution and draw the phase portrait for the equation.")
    st.ul([f"({l}) $\\dfrac{{d\\mathbf x}}{{dt}} = {M(sp.Matrix(A))}\\mathbf x$;" if l != "iv" else f"({l}) $\\dfrac{{d\\mathbf x}}{{dt}} = {M(sp.Matrix(A))}\\mathbf x$." for l, A in EX9])
    p1 = n.phase(1, "Setup")
    p1.p("Each system is $\\dot{\\mathbf x} = A\\mathbf x$ with a constant $2\\times 2$ matrix. Plan (Topic 4 Sec. 4 and 5): (a) characteristic equation $\\det(A - \\lambda I) = 0$; (b) eigenvectors from $(A - \\lambda I)\\mathbf v = \\mathbf 0$; (c) if the eigenvalues are real and distinct the eigenvectors are independent and $Q = [\\mathbf v_1\\ \\mathbf v_2]$ defines $\\mathbf z = Q^{-1}\\mathbf x$ with $\\dot{\\mathbf z} = Q^{-1}AQ\\,\\mathbf z$; (d) show $Q^{-1}AQ = \\Lambda$ by explicit multiplication.")
    p2 = n.phase(2, "Formulation")
    p2.p("Since $\\mathbf x = Q\\mathbf z$ with $Q$ constant, $\\dot{\\mathbf x} = Q\\dot{\\mathbf z}$ and $A\\mathbf x = AQ\\mathbf z$, so $\\dot{\\mathbf z} = Q^{-1}AQ\\,\\mathbf z$. If $Q^{-1}AQ = \\Lambda = \\operatorname{diag}(\\lambda_1, \\lambda_2)$ the equations $\\dot z_1 = \\lambda_1z_1$, $\\dot z_2 = \\lambda_2z_2$ are uncoupled.")
    p3 = n.phase(3, "Derivation")
    for l, A in EX9:
        A = sp.Matrix(A)
        p3.h(3, f"({l}) $A = {M(A)}$")
        out = planar.real_distinct(p3, A, "t")
        p3.h(4, "The decoupling transformation")
        Qi = out["Qi"]
        p3.p("In the original variables $\\mathbf x = (x, y)^T$ the new coordinates are $\\mathbf z = Q^{-1}\\mathbf x$:")
        p3.m(f"z_1 = {tex(sp.expand(Qi[0, 0] * sp.Symbol('x') + Qi[0, 1] * sp.Symbol('y')))}, \\qquad z_2 = {tex(sp.expand(Qi[1, 0] * sp.Symbol('x') + Qi[1, 1] * sp.Symbol('y')))}")
        claim_canon(f"4I-E9-{l}", out)
        portrait.portrait(p3, out, f"ch4a-e9-{l}")
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["Each $Q^{-1}AQ$ was multiplied out entry by entry above and equals $\\Lambda$ exactly; the eigenvalues satisfy $\\lambda_1 + \\lambda_2 = \\operatorname{tr}A$ and $\\lambda_1\\lambda_2 = \\det A$.",
           "(i) $15$ and $-6$: saddle; (ii) $2$ and $-3$ (lower-triangular matrix: the eigenvalues are the diagonal entries): saddle; (iii) $10$ and $5$: unstable node, tangent at the origin to the eigenvector of $5$; (iv) $21$ and $-39$: saddle with very different rates.",
           "(i) is the homogeneous part of Exercise 7(vii) and (ii) shows that for a triangular matrix the eigenvalues can be read off the diagonal (Topic 4 Examples 27.2 and 27.3).",
           "The change of coordinates is not the efficient way to solve the system (the general solution follows directly from the eigenpairs), but it is what justifies the portrait: it reduces every case to the uncoupled one (Robinson Sec. 28.2).",
           "Dimensional check: with $t$ in seconds the eigenvalues have units s$^{-1}$, and $Q$ is dimensionless (it mixes coordinates of equal units)."])
    return n


def ex10():
    n = Note(SHEET, 10, "Trajectories of an Uncoupled System by the Chain Rule", "Chain Rule • Separable Equation • Orbit Equation",
             ["problema-resuelto", "trayectorias", "variables-separables", "regla-de-la-cadena"], SOURCE)
    st = n.statement
    st.p("Using the chain rule for $y = y(x(t))$,")
    st.m(r"\frac{dy}{dt} = \frac{dy}{dx}\frac{dx}{dt} \;\Longrightarrow\; \frac{dy}{dx} = \frac{\dfrac{dy}{dt}}{\dfrac{dx}{dt}}.")
    st.p("Therefore, if")
    st.m(r"\frac{dx}{dt} = \lambda_1x, \qquad \frac{dy}{dt} = \lambda_2y")
    st.p("we have")
    st.m(r"\frac{dy}{dx} = \frac{\lambda_2y}{\lambda_1x}.")
    st.p("Solve the latter equation to determine the curves traced out by trajectories of the system of equations for $x(t)$ and $y(t)$.")
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("Real constants $\\lambda_1, \\lambda_2$. The chain rule is valid where $x(t)$ is a differentiable function with $\\dot x \\neq 0$, so that $t \\mapsto x$ is locally invertible and $y$ can be regarded as a function of $x$. Here $\\dot x = \\lambda_1x \\neq 0$ requires $\\lambda_1 \\neq 0$ and $x \\neq 0$. The cases $x = 0$ (the $y$-axis), $y = 0$ (the $x$-axis) and $\\lambda_1 = 0$ are treated separately at the end.")
    p2 = n.phase(2, "Formulation")
    p2.p("The orbit equation $\\frac{dy}{dx} = \\frac{\\lambda_2}{\\lambda_1}\\frac{y}{x}$ has no explicit $t$ and is **separable**: all the $y$ on the left and all the $x$ on the right.")
    p3 = n.phase(3, "Derivation")
    p3.h(4, "Integration")
    p3.p("Separate variables (for $y \\neq 0$, $x \\neq 0$) and integrate both sides with their antiderivatives, $\\int\\frac{dy}{y} = \\ln|y|$:")
    p3.m(r"\frac{dy}{y} = \frac{\lambda_2}{\lambda_1}\frac{dx}{x} \;\Longrightarrow\; \ln|y| = \frac{\lambda_2}{\lambda_1}\ln|x| + C")
    p3.p("Exponentiate and absorb $e^{C}$ in a constant $K = \\pm e^{C}$:")
    p3.m(r"|y| = e^{C}|x|^{\lambda_2/\lambda_1} \;\Longrightarrow\; \boxed{y = K\,|x|^{\lambda_2/\lambda_1}}, \qquad K \neq 0")
    p3.h(4, "Checking with the explicit solution")
    p3.p("The equations are solved directly by $x = x_0e^{\\lambda_1t}$, $y = y_0e^{\\lambda_2t}$ (separation of variables, $\\frac{d}{dt}(e^{-\\lambda t}u) = 0$). For $x_0 \\neq 0$, $|x|/|x_0| = e^{\\lambda_1t}$ so $e^{t} = (|x|/|x_0|)^{1/\\lambda_1}$ and")
    p3.m(r"y = y_0\left(e^{\lambda_1t}\right)^{\lambda_2/\lambda_1} = y_0\left(\frac{|x|}{|x_0|}\right)^{\lambda_2/\lambda_1} = \underbrace{y_0|x_0|^{-\lambda_2/\lambda_1}}_{K}|x|^{\lambda_2/\lambda_1}")
    p3.p("which is the same family, with $K = y_0|x_0|^{-\\lambda_2/\\lambda_1}$ (the sign of $y$ is the sign of $y_0$, preserved since $y = y_0e^{\\lambda_2t}$).")
    p3.h(4, "The axes")
    p3.p("If $x_0 = 0$ then $x(t) \\equiv 0$ and the orbit is on the $y$-axis (with $y = y_0e^{\\lambda_2t}$); if $y_0 = 0$ then $y \\equiv 0$ (that is $K = 0$) and the orbit lies on the $x$-axis. The origin is the equilibrium. If $\\lambda_1 = 0$, $x$ is constant and the orbits are vertical lines.")
    p3.h(4, "Shapes of the curves")
    p3.table(["Exponent $\\lambda_2/\\lambda_1$", "Curves $y = K|x|^{r}$", "Origin"],
             [["$r > 1$ (same sign, $|\\lambda_2| > |\\lambda_1|$)", "parabola-like, tangent to the $x$-axis at $0$", "node (stable if $\\lambda_i < 0$, unstable if $> 0$)"],
              ["$r = 1$ ($\\lambda_1 = \\lambda_2$)", "straight lines $y = Kx$ (rays)", "star"],
              ["$0 < r < 1$", "tangent to the $y$-axis at $0$", "node"],
              ["$r < 0$ (opposite signs)", "hyperbola-like, $y|x|^{-r} = K$, asymptotic to the axes", "saddle"],
              ["$r = -1$", "rectangular hyperbolas $xy = \\pm K$", "saddle"]])
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["This is the derivation behind the canonical portraits of Topic 4 Sec. 6.1: replace $(x, y)$ by $(z_1, z_2)$ and $\\lambda_1, \\lambda_2$ by the two eigenvalues to get $z_2 = K|z_1|^{\\lambda_2/\\lambda_1}$ (Robinson Eq. 28.12).",
           "Examples: $\\lambda_1 = 1$, $\\lambda_2 = 2$: $y = Kx^2$ (parabolas); $\\lambda_1 = 1$, $\\lambda_2 = -1$: $y = K/x$ (hyperbolas).",
           "Direction along the orbits is **not** given by the orbit equation: it is read from $\\dot x = \\lambda_1x$, $\\dot y = \\lambda_2y$ (away from $0$ along an axis if $\\lambda > 0$, towards it if $\\lambda < 0$).",
           "Differentiating the answer: $\\frac{dy}{dx} = K\\frac{\\lambda_2}{\\lambda_1}|x|^{\\lambda_2/\\lambda_1 - 1}\\operatorname{sign}(x) = \\frac{\\lambda_2}{\\lambda_1}\\frac{y}{x}$, which recovers the ODE (using $|x|^{r}/x = |x|^{r-1}\\operatorname{sign}x$)."])
    return n


def ex11():
    n = Note(SHEET, 11, "A Zero Eigenvalue: Lines of Equilibria", "Zero Eigenvalue • Line of Equilibria • Parallel Orbits",
             ["problema-resuelto", "autovalor-cero", "retrato-de-fase", "equilibrios"], SOURCE)
    st = n.statement
    st.p("Suppose that $A$ has eigenvalues $\\lambda_1 = 0$, $\\lambda_2 \\neq 0$, with eigenvectors $\\mathbf v_1$ and $\\mathbf v_2$, respectively.")
    st.ul(["(i) Write down the general solution of $\\dot{\\mathbf x} = A\\mathbf x$.",
           "(ii) After changing to a coordinate system $\\tilde{\\mathbf x}$ referred to the eigenvectors, we obtain $\\dfrac{d\\tilde{\\mathbf x}}{dt} = \\begin{pmatrix} 0 & 0 \\\\ 0 & \\lambda_2 \\end{pmatrix}\\tilde{\\mathbf x}$. By solving these equations draw the phase portrait in the $\\tilde{\\mathbf x}$ system, and sketch the phase portrait for the original coordinates $\\mathbf x$.",
           "(iii) Draw the phase portrait for the equation $\\dfrac{d\\mathbf x}{dt} = \\begin{pmatrix} -2 & 2 \\\\ 1 & -1 \\end{pmatrix}\\mathbf x$."])
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("$A$ is $2\\times 2$ real with eigenvalues $0$ and $\\lambda_2 \\neq 0$ (both real: $\\lambda_1 = 0$ is real and $\\lambda_2 = \\operatorname{tr}A$ is real because $A$ is real; being distinct, they have independent eigenvectors; $\\det A = 0$). $A\\mathbf v_1 = \\mathbf 0$, $A\\mathbf v_2 = \\lambda_2\\mathbf v_2$. Because $\\det A = 0$ the origin is **not** an isolated equilibrium: every point of $\\ker A = \\operatorname{span}\\{\\mathbf v_1\\}$ is an equilibrium ($A\\mathbf x = \\mathbf 0$).")
    p2 = n.phase(2, "Formulation")
    p2.p("Use the general result for distinct eigenvalues, $\\mathbf x = c_1e^{\\lambda_1t}\\mathbf v_1 + c_2e^{\\lambda_2t}\\mathbf v_2$ (Robinson Eq. 28.1), valid whenever the eigenvalues differ, in particular if one of them is $0$; and $Q = [\\mathbf v_1\\ \\mathbf v_2]$, $\\mathbf z = Q^{-1}\\mathbf x$.")
    p3 = n.phase(3, "Derivation")
    p3.h(3, "(i) General solution")
    p3.p("With $\\lambda_1 = 0$, $e^{\\lambda_1t} = e^{0} = 1$:")
    p3.m(r"\mathbf x(t) = c_1\mathbf v_1 + c_2e^{\lambda_2t}\mathbf v_2")
    p3.p("Check: $\\dot{\\mathbf x} = c_2\\lambda_2e^{\\lambda_2t}\\mathbf v_2$ and $A\\mathbf x = c_1A\\mathbf v_1 + c_2e^{\\lambda_2t}A\\mathbf v_2 = \\mathbf 0 + c_2\\lambda_2e^{\\lambda_2t}\\mathbf v_2$. They agree. The constant vector $c_1\\mathbf v_1$ is an equilibrium and $c_2e^{\\lambda_2t}\\mathbf v_2$ the time-dependent part.")
    p3.h(3, "(ii) Canonical phase portrait and its image")
    p3.p("In the coordinates $\\tilde{\\mathbf x} = (\\tilde x, \\tilde y)^T$ referred to $\\mathbf v_1, \\mathbf v_2$ the system is $\\dot{\\tilde x} = 0$, $\\dot{\\tilde y} = \\lambda_2\\tilde y$. The first gives $\\tilde x = c_1$ (constant); the second is separable: $\\frac{d\\tilde y}{\\tilde y} = \\lambda_2\\,dt$, $\\ln|\\tilde y| = \\lambda_2t + C$, so $\\tilde y = c_2e^{\\lambda_2t}$.")
    p3.m(r"\tilde x(t) = c_1, \qquad \tilde y(t) = c_2e^{\lambda_2t}")
    p3.ul(["Orbits: the **vertical lines** $\\tilde x = c_1$, because $\\tilde x$ never changes. Each such line is a pair of half-lines (for $\\tilde y > 0$ and $\\tilde y < 0$) and the point $(c_1, 0)$ is an equilibrium.",
           "The $\\tilde x$-axis ($\\tilde y = 0$) consists entirely of equilibria (it is the image of $\\ker A$).",
           "Direction: if $\\lambda_2 < 0$, $|\\tilde y| = |c_2|e^{\\lambda_2t}$ decreases: the arrows on every vertical line point **towards** the $\\tilde x$-axis, which they approach as $t \\to +\\infty$ without reaching it. If $\\lambda_2 > 0$ the arrows point **away** from the axis. The sign of $\\dot{\\tilde y} = \\lambda_2\\tilde y$ gives the direction at once.",
           "Original coordinates: $\\mathbf x = Q\\tilde{\\mathbf x} = \\tilde x\\mathbf v_1 + \\tilde y\\mathbf v_2$. The $\\tilde x$-axis goes to the line $\\operatorname{span}\\{\\mathbf v_1\\}$ of equilibria and the vertical lines go to the lines $c_1\\mathbf v_1 + s\\mathbf v_2$, $s \\in \\mathbb R$, **parallel to $\\mathbf v_2$**, drawn through the points of the line of equilibria. Straight lines remain straight: the picture is the canonical one sheared, with orbits along $\\mathbf v_2$ towards/away from the line of equilibria."])
    register_figure("ch4a-e11-ii-neg", dict(A=[[0.0, 0.0], [0.0, -1.0]], lines=[[1, 0, "z_1"], [0, 1, "z_2"]], axes=["x̃", "ỹ"], plane="z-plane, λ₂ < 0", title="canonical, lambda2<0",
                                            caption="Canonical $\\tilde{\\mathbf x}$-plane, $\\lambda_2 < 0$: the $\\tilde x$-axis (green) is a line of equilibria and the vertical orbits approach it."))
    register_figure("ch4a-e11-ii-pos", dict(A=[[0.0, 0.0], [0.0, 1.0]], lines=[[1, 0, "z_1"], [0, 1, "z_2"]], axes=["x̃", "ỹ"], plane="z-plane, λ₂ > 0", title="canonical, lambda2>0",
                                            caption="Canonical $\\tilde{\\mathbf x}$-plane, $\\lambda_2 > 0$: the vertical orbits leave the line of equilibria."))
    Aex = sp.Matrix([[0, 0], [0, -2]])
    Qs = sp.Matrix([[1, 1], [0, 1]])
    As = Qs * sp.diag(0, -2) * Qs.inv()
    register_figure("ch4a-e11-ii-x", dict(A=[[float(As[i, j]) for j in range(2)] for i in range(2)], lines=[[1, 0, "v_1"], [1, 1, "v_2"]], axes=["x", "y"], plane="x-plane, example",
                                          title="original coordinates, example", caption="Original $(x, y)$-plane for the example $\\mathbf v_1 = (1, 0)$, $\\mathbf v_2 = (1, 1)$, $\\lambda_2 = -2$: equilibria on the line of $\\mathbf v_1$, orbits parallel to $\\mathbf v_2$."))
    p3.fig("ch4a-e11-ii-neg", "Canonical $\\tilde{\\mathbf x}$-plane, $\\lambda_2 < 0$: the $\\tilde x$-axis (green) is a line of equilibria and the vertical orbits approach it.")
    p3.fig("ch4a-e11-ii-pos", "Canonical $\\tilde{\\mathbf x}$-plane, $\\lambda_2 > 0$: the vertical orbits leave the line of equilibria.")
    p3.fig("ch4a-e11-ii-x", "Original $(x, y)$-plane for the example $\\mathbf v_1 = (1, 0)$, $\\mathbf v_2 = (1, 1)$, $\\lambda_2 = -2$: equilibria on the line of $\\mathbf v_1$, orbits parallel to $\\mathbf v_2$.")
    p3.p(f"(For the sketch in the original plane, take the example $\\mathbf v_1 = (1, 0)$, $\\mathbf v_2 = (1, 1)$, $\\lambda_2 = -2$, whose matrix is $A = Q\\Lambda Q^{{-1}} = {M(As)}$; any other eigen-data give the same picture up to a linear change of the axes.)")
    p3.h(3, "(iii) The matrix $\\begin{pmatrix} -2 & 2 \\\\ 1 & -1 \\end{pmatrix}$")
    A = sp.Matrix([[-2, 2], [1, -1]])
    out = planar.real_distinct(p3, A, "t")
    claim_canon("4I-E11-iii", out)
    portrait.portrait(p3, out, "ch4a-e11-iii")
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["(iii): $\\operatorname{tr}A = -3$ and $\\det A = (-2)(-1) - 2\\cdot 1 = 0$, so the eigenvalues are $0$ and $-3$: the general solution is $\\mathbf x = c_1(1, 1)^T + c_2e^{-3t}(2, -1)^T$, every orbit converges to the equilibrium $c_1(1, 1)^T$, i.e. $\\mathbf x(t) \\to \\mathbf x_\\infty$ on the line $y = x$ along the direction $(2, -1)$.",
           "Explicit limit for $\\mathbf x(0) = (x_0, y_0)$: $\\mathbf x_\\infty = c_1(1, 1)^T$ with $c_1 = (x_0 + 2y_0)/3$ (from $Q^{-1}$ computed above, first row $(\\tfrac13, \\tfrac23)$). Example: $\\mathbf x(0) = (2, -1)$ gives $c_1 = 0$ and the orbit is the line $\\mathbf x = e^{-3t}(2, -1)$ going to the origin.",
           "The origin is no longer an isolated equilibrium: the node/saddle/spiral classification of Topic 4 Sec. 9 assumes $\\det A \\neq 0$ (see the trace-determinant discussion), and here $\\det A = 0$, which is the borderline between a stable node ($\\lambda_2 < 0$) and a saddle.",
           "Conserved quantity: the combination $\\tilde x = c_1$ is a first integral of the motion ($x + 2y$ in (iii), up to the factor $\\tfrac13$): $\\frac{d}{dt}(x + 2y) = (-2x + 2y) + 2(x - y) = 0$ $\\checkmark$."])
    return n
