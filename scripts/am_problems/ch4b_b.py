"""Chapter 4, part 2, exercises 5 to 8."""
import sympy as sp

from . import planar, portrait
from .ch4b import CLAIMS, EX5, EX5TXT, SHEET, SOURCE, claim_canon, eta_tex, cplx
from .core import Doc, Note, register_figure, tex, vec, t
from .planar import M


def ex5():
    n = Note(SHEET, 5, "Building a Matrix from a Complex Pair of Eigenvalues and Eigenvectors", "Inverse Problem • A = Q J Q⁻¹ • Three Matrices",
             ["problema-resuelto", "problema-inverso", "autovalores-complejos", "construccion-de-matrices"], SOURCE)
    st = n.statement
    st.p("Show how to construct a matrix with a complex conjugate pair of eigenvalues $\\lambda_\\pm = \\rho \\pm i\\omega$ and corresponding eigenvectors $\\boldsymbol\\eta_\\pm = \\mathbf v_1 \\pm i\\mathbf v_2$. Hence find the matrices with the following eigenvalues and eigenvectors:")
    st.ul([f"({l}) ${EX5TXT[l]}$;" if l != "iii" else f"({l}) ${EX5TXT[l]}$." for l, *_ in EX5])
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("We look for a real matrix $A$ ($2\\times 2$) with $A\\boldsymbol\\eta_+ = \\lambda_+\\boldsymbol\\eta_+$ where $\\boldsymbol\\eta_+ = \\mathbf v_1 + i\\mathbf v_2$ and $\\lambda_+ = \\rho + i\\omega$, with $\\mathbf v_1, \\mathbf v_2$ real and independent and $\\omega \\neq 0$. Because $A$ is real, $A\\bar{\\boldsymbol\\eta}_+ = \\bar\\lambda_+\\bar{\\boldsymbol\\eta}_+$ follows automatically. (Note on the statement: the sheet writes $\\boldsymbol\\eta_\\pm = \\mathbf v_1 \\pm i\\mathbf v_2$ for the eigenvectors of $\\lambda_\\pm = \\rho \\pm i\\omega$, i.e. $\\mathbf v_1 = \\mathbf u$, $\\mathbf v_2 = \\mathbf w$ of Topic 4.)")
    p2 = n.phase(2, "Formulation: the construction")
    p2.p("Expand $A(\\mathbf v_1 + i\\mathbf v_2) = (\\rho + i\\omega)(\\mathbf v_1 + i\\mathbf v_2)$ and separate real and imaginary parts (both $A\\mathbf v_j$ are real vectors, $i^2 = -1$):")
    p2.m(r"A\mathbf v_1 + iA\mathbf v_2 = (\rho\mathbf v_1 - \omega\mathbf v_2) + i(\omega\mathbf v_1 + \rho\mathbf v_2) \;\Longrightarrow\; A\mathbf v_1 = \rho\mathbf v_1 - \omega\mathbf v_2,\quad A\mathbf v_2 = \omega\mathbf v_1 + \rho\mathbf v_2")
    p2.p("Collect the two vector equations in one matrix equation, with $Q = [\\mathbf v_1 \\mid \\mathbf v_2]$ (columns): the first column of $QJ$ is $\\rho\\mathbf v_1 - \\omega\\mathbf v_2$ for $J = \\begin{pmatrix} \\rho & \\omega \\\\ -\\omega & \\rho \\end{pmatrix}$ and the second is $\\omega\\mathbf v_1 + \\rho\\mathbf v_2$. Hence $AQ = QJ$, and since $\\mathbf v_1, \\mathbf v_2$ are independent (Exercise 4) $Q$ is invertible:")
    p2.m(r"\boxed{A = QJQ^{-1}, \qquad Q = [\mathbf v_1 \mid \mathbf v_2], \qquad J = \begin{pmatrix} \rho & \omega \\ -\omega & \rho \end{pmatrix}}")
    p2.p("This $A$ is real (a product of real matrices), has the eigenvalues of $J$, $\\rho \\pm i\\omega$ (similar matrices have the same characteristic polynomial), and $A\\boldsymbol\\eta_+ = \\lambda_+\\boldsymbol\\eta_+$ by construction.")
    p3 = n.phase(3, "Derivation of the three matrices")
    for l, rho, om, v1, v2, eta in EX5:
        p3.h(3, f"({l}) ${EX5TXT[l]}$")
        v1, v2 = sp.Matrix(v1), sp.Matrix(v2)
        p3.p(f"$\\boldsymbol\\eta_+ = {eta_tex(eta)} = {vec(v1[0], v1[1])} + i{vec(v2[0], v2[1])}$, so $\\mathbf v_1 = {vec(v1[0], v1[1])}$, $\\mathbf v_2 = {vec(v2[0], v2[1])}$, $\\rho = {tex(rho)}$, $\\omega = {tex(om)}$.")
        Q = sp.Matrix.hstack(v1, v2)
        J = sp.Matrix([[rho, om], [-om, rho]])
        p3.m(f"Q = {M(Q)}, \\quad J = {M(J)}, \\quad \\det Q = {tex(Q.det())}, \\quad Q^{{-1}} = {M(Q.inv())}")
        QJ = planar.matmul_steps(p3, Q, J, "Q", "J", "QJ")
        A = planar.matmul_steps(p3, QJ, Q.inv(), "(QJ)", "Q^{-1}", "A")
        p3.m(f"A = QJQ^{{-1}} = {M(A)}")
        p3.h(4, "Verification")
        lam = cplx(rho, om)
        eta_v = sp.Matrix([cplx(*eta[0]), cplx(*eta[1])])
        lhs = sp.simplify(A * eta_v)
        rhs = sp.simplify(lam * eta_v)
        assert sp.simplify(lhs - rhs) == sp.zeros(2, 1)
        comp = []
        for i in range(2):
            comp.append(f"{par_c(A[i, 0])}\\,({tex(eta_v[0])}) + {par_c(A[i, 1])}\\,({tex(eta_v[1])}) = {tex(sp.expand(lhs[i]))}")
        p3.m(f"A\\boldsymbol\\eta_+ = {M(A)}{eta_tex(eta)} = \\begin{{pmatrix}} {comp[0]} \\\\ {comp[1]} \\end{{pmatrix}} = ({tex(lam)})\\,{eta_tex(eta)}")
        tr, det = A.trace(), A.det()
        p3.p(f"Characteristic polynomial: $\\lambda^2 - ({tex(tr)})\\lambda + ({tex(det)}) = 0$ has $\\operatorname{{tr}}A = {tex(tr)} = 2\\rho$ and $\\det A = {tex(det)} = \\rho^2 + \\omega^2$, hence $\\lambda = {tex(sp.Rational(tr, 2))} \\pm i\\sqrt{{{tex(det - sp.Rational(tr, 2) ** 2)}}}$, i.e. $\\rho \\pm i\\omega$ with $\\rho = {tex(rho)}$, $\\omega = {tex(om)}$.")
        assert tr == 2 * rho and det == rho ** 2 + om ** 2
        out = dict(A=A, Q=Q, J=J, kind="complex", rho=sp.Integer(rho), om=sp.Integer(om), u=v1, w=v2)
        claim_canon(f"4II-E5-{l}", out)
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["The matrix is **not unique** if only the eigenvalues are prescribed, but it is unique once $\\boldsymbol\\eta_+$ is given (up to the complex scalar multiple that every eigenvector admits: rescaling $\\boldsymbol\\eta_+$ by $c = c_r + ic_i$ changes $(\\mathbf v_1, \\mathbf v_2)$ and leaves $A$ unchanged, since $A\\bar{\\boldsymbol\\eta}_+$, $A\\boldsymbol\\eta_+$ still determine $A$ on the basis $\\{\\boldsymbol\\eta_+, \\bar{\\boldsymbol\\eta}_+\\}$ of $\\mathbb C^2$).",
           "For the three items $\\operatorname{tr}A = 6, 0, -4$ and $\\det A = 18, 9, 5$ respectively, which are $2\\rho$ and $\\rho^2 + \\omega^2$ as the construction predicts.",
           "(ii) has $\\rho = 0$: a centre. $A = \\begin{pmatrix} 2 & -1 \\\\ 13 & -2 \\end{pmatrix}$ has trace zero and determinant $9 = \\omega^2$.",
           "This is the inverse of Exercise 3: from $A$ to $(Q, J)$ there, from $(Q, J)$ to $A$ here."])
    return n


def par_c(x):
    s = tex(x)
    return f"({s})" if (x < 0 or " " in s.strip()) else s


EX6 = [("i", [[5, -4], [1, 1]]), ("ii", [[-6, 2], [-2, -2]]), ("iii", [[-3, -1], [1, -5]]), ("iv", [[13, 0], [0, 13]]), ("v", [[7, -4], [1, 3]])]


def ex6():
    n = Note(SHEET, 6, "Five Systems with a Repeated Eigenvalue: Stars and Improper Nodes", "Repeated Eigenvalue • Jordan Chain • Stars and Improper Nodes",
             ["problema-resuelto", "autovalor-repetido", "nodo-impropio", "cadena-de-jordan"], SOURCE)
    st = n.statement
    st.p("Find the eigenvalues and eigenvectors of the matrices occurring in the following equations, and draw the phase portrait. Find also the coordinate transformation that will put the equation into canonical form and show that this works. Write down the general solution.")
    st.ul([f"({l}) $\\dfrac{{d\\mathbf x}}{{dt}} = {M(sp.Matrix(A))}\\mathbf x$;" if l != "v" else f"({l}) $\\dfrac{{d\\mathbf x}}{{dt}} = {M(sp.Matrix(A))}\\mathbf x$." for l, A in EX6])
    p1 = n.phase(1, "Setup")
    p1.p("For every matrix the discriminant $\\Delta = (\\operatorname{tr}A)^2 - 4\\det A$ is zero (checked in each item), so there is one repeated eigenvalue $\\lambda = \\tfrac12\\operatorname{tr}A$ with algebraic multiplicity $m_a = 2$. The geometric multiplicity $m_g = \\dim\\ker(A - \\lambda I)$ is $2$ iff $A = \\lambda I$ (a **star**) and $1$ otherwise (an **improper node** with a Jordan chain), Topic 4 Sec. 8.2 to 8.4. The canonical form is $J = \\begin{pmatrix} \\lambda & 1 \\\\ 0 & \\lambda \\end{pmatrix}$ with $Q = [\\mathbf v_1 \\mid \\mathbf v_2]$, $(A - \\lambda I)\\mathbf v_2 = \\mathbf v_1$; for a star there is nothing to transform.")
    p2 = n.phase(2, "Formulation")
    p2.p("Algorithm (Topic 4 Sec. 8.10): $\\lambda = \\tfrac12\\operatorname{tr}A$; $N = A - \\lambda I$; if $N = O$ star, $\\mathbf x = e^{\\lambda t}\\mathbf x_0$; otherwise $\\mathbf v_1 \\in \\ker N$, solve $N\\mathbf v_2 = \\mathbf v_1$, $Q = [\\mathbf v_1 \\mid \\mathbf v_2]$, $\\mathbf z = Q^{-1}\\mathbf x$, $z_1 = (c_1 + c_2t)e^{\\lambda t}$, $z_2 = c_2e^{\\lambda t}$, $\\mathbf x = Q\\mathbf z$.")
    p3 = n.phase(3, "Derivation")
    for l, A in EX6:
        A = sp.Matrix(A)
        p3.h(3, f"({l}) $A = {M(A)}$")
        out = planar.repeated(p3, A, "t")
        claim_canon(f"4II-E6-{l}", out)
        portrait.portrait(p3, out, f"ch4b-e6-{l}")
    p4 = n.phase(4, "Interpretation and checks")
    p4.table(["Item", "$\\lambda$", "Type"], [["(i)", "$3$", "unstable improper node"], ["(ii)", "$-4$", "stable improper node"], ["(iii)", "$-4$", "stable improper node"], ["(iv)", "$13$", "unstable star"], ["(v)", "$5$", "unstable improper node"]])
    p4.ul(["(i) is exactly the worked Example 8.2 of Topic 4 (Robinson Example 30.1): $\\lambda = 3$, $\\mathbf v_1 = (2, 1)^T$, $\\mathbf v_2 = (1, 0)^T$ and $J = \\begin{pmatrix} 3 & 1 \\\\ 0 & 3 \\end{pmatrix}$ — the result reproduces it step by step.",
           "In each improper node $Q^{-1}AQ = J$ was multiplied out entry by entry; $N^2 = O$ was checked (Cayley-Hamilton).",
           "The general solution $\\mathbf x = e^{\\lambda t}[c_1\\mathbf v_1 + c_2(t\\mathbf v_1 + \\mathbf v_2)]$ contains the secular term $te^{\\lambda t}\\mathbf v_1$, which makes all orbits tangent to $\\mathbf v_1$ at both ends (S-shaped).",
           "(iv) is a multiple of the identity: every vector is an eigenvector and the orbits are rays; the canonical form is $A$ itself, and any basis (for instance $Q = I$) works.",
           "A repeated eigenvalue is a borderline case between nodes ($\\Delta > 0$) and spirals ($\\Delta < 0$)."])
    return n


def ex7():
    n = Note(SHEET, 7, "The Nilpotent Case: Zero as a Repeated Eigenvalue", "Nilpotent Matrix • Shear • Line of Equilibria",
             ["problema-resuelto", "matriz-nilpotente", "autovalor-cero", "retrato-de-fase"], SOURCE)
    st = n.statement
    st.p("Suppose that a non-zero matrix $A$ has zero as a repeated eigenvalue, with eigenvector $\\mathbf v$. Then we can change to coordinates referred to $\\mathbf v_2$ and $\\mathbf v_1 = A\\mathbf v_2$, where $\\mathbf v_2$ is any vector in a different direction to $\\mathbf v$, so that $\\tilde{\\mathbf x} = \\tilde x\\mathbf v_1 + \\tilde y\\mathbf v_2$. The equation $d\\mathbf x/dt = A\\mathbf x$ becomes $\\dfrac{d\\tilde{\\mathbf x}}{dt} = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix}\\tilde{\\mathbf x}$, hence,")
    st.m(r"\frac{d\tilde x}{dt} = \tilde y \quad\text{and}\quad \frac{d\tilde y}{dt} = 0.")
    st.ul(["(i) Solve the equations for $\\tilde x(t)$ and $\\tilde y(t)$, and hence write down the general solution for $\\mathbf x(t)$.",
           "(ii) Draw the phase diagram in the $(\\tilde x, \\tilde y)$ and $(x, y)$ planes.",
           "(iii) Draw the phase diagram for the equation $\\dfrac{d\\mathbf x}{dt} = \\begin{pmatrix} -1 & 1 \\\\ -1 & 1 \\end{pmatrix}\\mathbf x$."])
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("$A \\neq O$ is $2\\times 2$ with the double eigenvalue $0$: $\\operatorname{tr}A = 0$, $\\det A = 0$, so by Cayley-Hamilton $A^2 = O$ ($A^2 - (\\operatorname{tr}A)A + (\\det A)I = O$). Since $A \\neq O$, $\\ker A$ is one-dimensional, spanned by $\\mathbf v$: $m_g = 1$ (Topic 4 Sec. 8.4 with $\\lambda = 0$, $N = A$).")
    p1.p("Why the proposed basis works: take $\\mathbf v_2 \\notin \\operatorname{span}\\{\\mathbf v\\}$. Then $A\\mathbf v_2 \\neq \\mathbf 0$ (otherwise $\\mathbf v_2$ would be in $\\ker A$), and $\\mathbf v_1 = A\\mathbf v_2$ satisfies $A\\mathbf v_1 = A^2\\mathbf v_2 = \\mathbf 0$, so $\\mathbf v_1 \\in \\ker A = \\operatorname{span}\\{\\mathbf v\\}$ and $\\mathbf v_1 \\neq \\mathbf 0$ is an eigenvector. $\\mathbf v_1, \\mathbf v_2$ are independent (not parallel), and")
    p1.m(r"A\mathbf v_1 = \mathbf 0 = 0\cdot\mathbf v_1 + 0\cdot\mathbf v_2, \qquad A\mathbf v_2 = \mathbf v_1 = 1\cdot\mathbf v_1 + 0\cdot\mathbf v_2 \;\Longrightarrow\; Q^{-1}AQ = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}")
    p2 = n.phase(2, "Formulation")
    p2.p("With $Q = [\\mathbf v_1 \\mid \\mathbf v_2]$ and $\\mathbf x = Q\\tilde{\\mathbf x} = \\tilde x\\mathbf v_1 + \\tilde y\\mathbf v_2$ the canonical system is $\\dot{\\tilde x} = \\tilde y$, $\\dot{\\tilde y} = 0$ (the Jordan block of Topic 4 Eq. 8.3 with $\\lambda = 0$).")
    p3 = n.phase(3, "Derivation")
    p3.h(3, "(i) Solution")
    p3.p("The second equation $\\dot{\\tilde y} = 0$ integrates to $\\tilde y(t) = c_2$ (a constant). Substituting in the first, $\\dot{\\tilde x} = c_2$, and Barrow's rule between $0$ and $t$ gives $\\tilde x(t) - \\tilde x(0) = \\int_0^t c_2\\,ds = c_2t$:")
    p3.m(r"\tilde x(t) = c_1 + c_2t, \qquad \tilde y(t) = c_2 \qquad (c_1 = \tilde x(0),\ c_2 = \tilde y(0))")
    p3.p("Back to the original coordinates, $\\mathbf x = \\tilde x\\mathbf v_1 + \\tilde y\\mathbf v_2$:")
    p3.m(r"\boxed{\mathbf x(t) = (c_1 + c_2t)\,\mathbf v_1 + c_2\,\mathbf v_2}")
    p3.p("Check: $\\dot{\\mathbf x} = c_2\\mathbf v_1$ and $A\\mathbf x = (c_1 + c_2t)A\\mathbf v_1 + c_2A\\mathbf v_2 = \\mathbf 0 + c_2\\mathbf v_1$. They agree. Unlike the case $\\lambda \\neq 0$ there is no exponential: the secular term grows only **linearly**.")
    p3.h(3, "(ii) Phase diagrams")
    register_figure("ch4b-e7-ii-z", dict(A=[[0.0, 1.0], [0.0, 0.0]], lines=[[1, 0, "x̃"]], axes=["x̃", "ỹ"], plane="canonical plane", title="nilpotent canonical",
                                         caption="$(\\tilde x, \\tilde y)$-plane: horizontal lines $\\tilde y = c_2$ traversed to the right above the axis and to the left below it; the $\\tilde x$-axis is all equilibria."))
    p3.p("In the $(\\tilde x, \\tilde y)$ plane the orbits are the **horizontal lines** $\\tilde y = c_2$ (since $\\tilde y$ is constant). On the line $\\tilde y = c_2 > 0$ the abscissa $\\tilde x = c_1 + c_2t$ increases at constant speed $c_2$: motion to the right; for $c_2 < 0$ to the left. The $\\tilde x$-axis ($c_2 = 0$) consists of equilibria. There are no curved orbits: the speed is proportional to the height $\\tilde y$ (a *shear* flow).")
    p3.fig("ch4b-e7-ii-z", "$(\\tilde x, \\tilde y)$-plane: horizontal lines $\\tilde y = c_2$ traversed to the right above the axis and to the left below it; the $\\tilde x$-axis is all equilibria.")
    p3.p("In the $(x, y)$ plane, $\\mathbf x = \\tilde x\\mathbf v_1 + \\tilde y\\mathbf v_2$ maps horizontal lines to **lines parallel to $\\mathbf v_1$**, offset from the line $\\operatorname{span}\\{\\mathbf v_1\\}$ of equilibria by $c_2\\mathbf v_2$; they are traversed along $+\\mathbf v_1$ on the side of $\\operatorname{span}\\{\\mathbf v_1\\}$ where $\\mathbf v_2$ points and along $-\\mathbf v_1$ on the other side. The $(x, y)$-diagram of the following item shows a concrete example.")
    p3.h(3, "(iii) The matrix $\\begin{pmatrix} -1 & 1 \\\\ -1 & 1 \\end{pmatrix}$")
    A = sp.Matrix([[-1, 1], [-1, 1]])
    p3.p(f"$\\operatorname{{tr}}A = -1 + 1 = 0$ and $\\det A = (-1)(1) - (1)(-1) = 0$, so the characteristic equation is $\\lambda^2 = 0$: the double eigenvalue $0$, and $A \\neq O$. Check $A^2 = O$:")
    planar.matmul_steps(p3, A, A, "A", "A", "A^2")
    p3.p("Eigenvector: $A\\mathbf v = \\mathbf 0$ gives $-v_1 + v_2 = 0$ (both rows are the same equation up to sign), so $\\mathbf v = (1, 1)^T$. Following the exercise, take any $\\mathbf v_2$ not parallel to $\\mathbf v$, for instance $\\mathbf v_2 = (1, 0)^T$, and set $\\mathbf v_1 = A\\mathbf v_2$:")
    v2 = sp.Matrix([1, 0])
    v1 = A * v2
    p3.m(f"\\mathbf v_1 = A\\mathbf v_2 = {M(A)}{vec(1, 0)} = {vec(v1[0], v1[1])}")
    p3.p("$\\mathbf v_1 = (-1, -1)^T$ is indeed an eigenvector ($A\\mathbf v_1 = (1 - 1, 1 - 1)^T = \\mathbf 0$), a multiple of $\\mathbf v$.")
    Q = sp.Matrix.hstack(v1, v2)
    p3.m(f"Q = [\\mathbf v_1 \\mid \\mathbf v_2] = {M(Q)}")
    Qi, detQ = planar.inverse_steps(p3, Q)
    AQ = sp.Matrix.hstack(A * v1, A * v2)
    p3.m(f"AQ = [A\\mathbf v_1 \\mid A\\mathbf v_2] = [\\mathbf 0 \\mid \\mathbf v_1] = {M(AQ)}")
    prod = planar.matmul_steps(p3, Qi, AQ, "Q^{-1}", "(AQ)", "Q^{-1}AQ")
    J = sp.Matrix([[0, 1], [0, 0]])
    assert prod == J
    p3.m(f"Q^{{-1}}AQ = {M(prod)}")
    c1s, c2s = sp.symbols("c_1 c_2")
    x1 = sp.expand((c1s + c2s * t) * v1[0] + c2s * v2[0])
    x2 = sp.expand((c1s + c2s * t) * v1[1] + c2s * v2[1])
    p3.p("By part (i) the general solution is $\\mathbf x(t) = (c_1 + c_2t)\\mathbf v_1 + c_2\\mathbf v_2$:")
    p3.m(f"x(t) = {tex(x1)}, \\qquad y(t) = {tex(x2)}")
    p3.p(f"Check: $\\dot x = {tex(sp.diff(x1, t))}$ and $-x + y = {tex(sp.expand(-x1 + x2))}$; $\\dot y = {tex(sp.diff(x2, t))}$ and $-x + y$ again: both equations $\\dot x = -x + y$, $\\dot y = -x + y$ hold.")
    assert sp.simplify(sp.diff(x1, t) - (-x1 + x2)) == 0 and sp.simplify(sp.diff(x2, t) - (-x1 + x2)) == 0
    p3.p("The coordinates are $\\tilde{\\mathbf x} = Q^{-1}\\mathbf x$: $\\tilde x = -y$, $\\tilde y = x - y$ (first row $(0, -1)$, second row $(1, -1)$ of $Q^{-1}$). Every orbit is a straight line parallel to $\\mathbf v = (1, 1)$; the line $y = x$ ($\\tilde y = 0$) consists of equilibria.")
    p3.p("Direction: $\\dot{\\mathbf x} = (y - x)(1, 1)^T$. Above the line $y = x$ ($y > x$) the motion is along $+(1, 1)$ (up and to the right); below it, along $-(1, 1)$ (down and to the left). The speed $|y - x|\\sqrt2$ grows with the distance to the line of equilibria.")
    out = dict(kind="improper", A=A, J=J, lam=sp.Integer(0), v1=v1, v2=v2, N=A, Q=Q, Qi=Qi)
    claim_canon("4II-E7-iii", out)
    portrait.improper_portrait(p3, out, "ch4b-e7-iii")
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["This is the limit $\\lambda \\to 0$ of the improper node $J = \\begin{pmatrix} \\lambda & 1 \\\\ 0 & \\lambda \\end{pmatrix}$: the factor $e^{\\lambda t}$ disappears and only the shear remains (the origin of the trace-determinant plane): the flow is $\\mathbf x(t) = \\mathbf x_0 + t\\,A\\mathbf x_0$ (the series of $e^{At}$ stops after the linear term because $A^2 = O$): in (iii), $\\mathbf x(t) = \\mathbf x_0 + t(y_0 - x_0)(1, 1)^T$, which matches the direction and speed found.",
           "Check at a point: $\\mathbf x_0 = (1, 0)$: formula gives $\\mathbf x(t) = (1, 0) + t(0 - 1)(1, 1) = (1 - t, -t)$, and the general solution with $c_2 = \\tilde y(0) = x_0 - y_0 = 1$, $c_1 = \\tilde x(0) = -y_0 = 0$ gives $x = -(0 + t)(1) + 1 = 1 - t$ and $y = -t$. They coincide.",
           "$\\operatorname{tr}A = \\det A = 0$ is the origin of the trace-determinant plane (Topic 4 Sec. 9.1), where all the portrait types meet.",
           "The solutions are polynomials in $t$, so every orbit not on the line of equilibria leaves to infinity linearly in time in both directions."])
    return n


Q8 = [
    ("i", "real", dict(l1=3, v1=(1, 1), l2=-2, v2=(1, -2)), "$\\lambda_1 = 3$ with $\\mathbf v_1 = (1, 1)$ and $\\lambda_2 = -2$ with $\\mathbf v_2 = (1, -2)$"),
    ("ii", "cplx", dict(rho=-1, om=3, sense="ccw"), "complex conjugate eigenvalues $\\lambda_\\pm = -1 \\pm 3i$, with $\\dot x < 0$ when $x = 0$ and $y > 0$"),
    ("iii", "rep", dict(lam=13, v1=(3, 2), A=[[7, 9], [-4, 19]]), "a single eigenvalue $\\lambda = 13$ with eigenvector $(3, 2)$, and $\\dot x > 0$ when $x = 0$ and $y > 0$"),
    ("iv", "real", dict(l1=-2, v1=(2, 1), l2=-3, v2=(1, -1)), "$\\lambda_1 = -2$ with $\\mathbf v_1 = (2, 1)$ and $\\lambda_2 = -3$ with $\\mathbf v_2 = (1, -1)$"),
    ("v", "rep", dict(lam=-3, v1=(1, -1), A=[[-2, 1], [-1, -4]]), "a single eigenvalue $\\lambda = -3$ with eigenvector $(1, -1)$, and $\\dot x > 0$ when $x = 0$ and $y > 0$"),
    ("vi", "cplx", dict(rho=0, om=2, sense="cw"), "$\\lambda_\\pm = \\pm 2i$, where $\\dot y < 0$ when $y = 0$ and $x > 0$"),
    ("vii", "real", dict(l1=1, v1=(3, 2), l2=5, v2=(1, -4)), "$\\lambda_1 = 1$ with $\\mathbf v_1 = (3, 2)$ and $\\lambda_2 = 5$ with $\\mathbf v_2 = (1, -4)$"),
    ("viii", "cplx", dict(rho=5, om=1, sense="ccw"), "$\\lambda_\\pm = 5 \\pm i$, and $\\dot y > 0$ when $y = 0$ and $x > 0$"),
    ("ix", "star", dict(lam=-7), "a single eigenvalue $\\lambda = -7$, with the matrix $A$ being a multiple of the identity"),
]
Q8STMT = [
    "(i) $\\lambda_1 = 3$ with $\\mathbf v_1 = (1, 1)$ and $\\lambda_2 = -2$ with $\\mathbf v_2 = (1, -2)$;",
    "(ii) complex conjugate eigenvalues $\\lambda_\\pm = -1 \\pm 3i$, with $\\dot x < 0$ when $x = 0$ and $y > 0$;",
    "(iii) a single eigenvalue $\\lambda = 13$ with eigenvector $(3, 2)$, and $\\dot x > 0$ when $x = 0$ and $y > 0$;",
    "(iv) $\\lambda_1 = -2$ with $\\mathbf v_1 = (2, 1)$ and $\\lambda_2 = -3$ with $\\mathbf v_2 = (1, -1)$;",
    "(v) a single eigenvalue $\\lambda = -3$ with eigenvector $(1, -1)$, and $\\dot x > 0$ when $x = 0$ and $y > 0$;",
    "(vi) $\\lambda_\\pm = \\pm 2i$, where $\\dot y < 0$ when $y = 0$ and $x > 0$;",
    "(vii) $\\lambda_1 = 1$ with $\\mathbf v_1 = (3, 2)$ and $\\lambda_2 = 5$ with $\\mathbf v_2 = (1, -4)$;",
    "(viii) $\\lambda_\\pm = 5 \\pm i$, and $\\dot y > 0$ when $y = 0$ and $x > 0$;",
    "(ix) a single eigenvalue $\\lambda = -7$, with the matrix $A$ being a multiple of the identity.",
]


def ex8():
    n = Note(SHEET, 8, "Nine Qualitative Phase Portraits from Partial Data", "Qualitative Portraits • Classification • Nine Cases",
             ["problema-resuelto", "retrato-de-fase", "clasificacion", "analisis-cualitativo"], SOURCE)
    st = n.statement
    st.p("Draw the phase portrait for the equation $d\\mathbf x/dt = A\\mathbf x$ when the eigenvalues and eigenvectors of $A$ are as given:")
    st.ul(Q8STMT)
    p1 = n.phase(1, "Setup: what the data determine")
    p1.p("The data fix the **type** of the origin and the position of the eigenlines, which is all that the phase portrait of a linear system needs (Topic 4 Sec. 9, Robinson Ch. 31). A matrix consistent with the data is built in each item, to draw the portrait and to check the sign information numerically; any other matrix with the same data has the same portrait up to a linear distortion of the plane.")
    p1.table(["Data", "Origin is a", "Extra information used"],
             [["two real eigenvalues, opposite signs", "saddle", "eigenlines; stable = negative eigenvalue"],
              ["two real eigenvalues, same sign", "node", "tangent to the eigenvector of the smaller $|\\lambda|$; stable iff $\\lambda < 0$"],
              ["complex $\\rho \\pm i\\omega$, $\\rho \\neq 0$", "spiral", "stable iff $\\rho < 0$; sense from the sign of $\\dot x$ at $(0, 1)$ or $\\dot y$ at $(1, 0)$"],
              ["imaginary $\\pm i\\omega$", "centre", "closed orbits; sense from the sign condition"],
              ["single eigenvalue, one eigenvector", "improper node", "S-shaped orbits along the eigenline; side/orientation from the sign condition"],
              ["single eigenvalue, $A = \\lambda I$", "star", "straight rays"]])
    p2 = n.phase(2, "Formulation: how the sign conditions are read")
    p2.p("At the point $(0, 1)$ the vector field is $A(0, 1)^T = (a_{12}, a_{22})^T$, so the sign of $\\dot x$ there is the sign of $a_{12}$: positive means motion to the right at the top of the plane, which is clockwise; negative means counter-clockwise. At $(1, 0)$ the field is $(a_{11}, a_{21})^T$, so the sign of $\\dot y$ there is the sign of $a_{21}$: negative means downwards on the right-hand side, i.e. clockwise; positive means counter-clockwise (Topic 4 Sec. 7.8).")
    p3 = n.phase(3, "Derivation of the nine portraits")
    for (l, kind, data, desc), stmt in zip(Q8, Q8STMT):
        p3.h(3, f"({l}) " + stmt[stmt.index(")") + 2:].rstrip(";."))
        pre = f"ch4b-e8-{l}"
        if kind == "real":
            l1, v1, l2, v2 = data["l1"], sp.Matrix(data["v1"]), data["l2"], sp.Matrix(data["v2"])
            Q = sp.Matrix.hstack(v1, v2)
            A = sp.simplify(Q * sp.diag(l1, l2) * Q.inv())
            p3.p(f"Two real eigenvalues with independent eigenvectors ($\\det[\\mathbf v_1\\ \\mathbf v_2] = {tex(Q.det())} \\neq 0$). A consistent matrix is $A = Q\\Lambda Q^{{-1}} = {M(A)}$ (checked: $A\\mathbf v_1 = {vec(*(A * v1))} = {l1}\\mathbf v_1$, $A\\mathbf v_2 = {vec(*(A * v2))} = {l2}\\mathbf v_2$).")
            out = dict(kind="real", A=A, Q=Q, J=sp.diag(l1, l2), l1=sp.Integer(l1), l2=sp.Integer(l2), v1=v1, v2=v2)
            claim_canon(f"4II-E8-{l}", out)
            portrait.portrait(p3, out, pre)
        elif kind == "cplx":
            rho, om, sense = data["rho"], data["om"], data["sense"]
            s = 1 if sense == "cw" else -1
            A = sp.Matrix([[rho, s * om], [-s * om, rho]])
            if l == "vi":
                p3.p(f"$\\dot y = a_{{21}}x + a_{{22}}y$ at $(1, 0)$ equals $a_{{21}}$, and $\\dot y < 0$ there, so $a_{{21}} < 0$: at the right-hand side of the plane the motion is downwards, i.e. **clockwise**. A consistent matrix with eigenvalues $\\pm 2i$ and $a_{{21}} < 0$ is $A = {M(A)}$ ($\\operatorname{{tr}}A = 0$, $\\det A = 4$, eigenvalues $\\pm 2i$; $a_{{21}} = {tex(A[1, 0])} < 0$).")
            elif l == "viii":
                p3.p(f"$\\dot y > 0$ at $(1, 0)$ gives $a_{{21}} > 0$: upwards on the right-hand side, i.e. **counter-clockwise**. A consistent matrix with eigenvalues $5 \\pm i$ is $A = {M(A)}$ ($\\operatorname{{tr}}A = 10$, $\\det A = 26$, $\\lambda = 5 \\pm i$; $a_{{21}} = {tex(A[1, 0])} > 0$).")
            else:
                p3.p(f"$\\dot x < 0$ at $(0, 1)$ gives $a_{{12}} < 0$: leftwards at the top of the plane, i.e. **counter-clockwise**. A consistent matrix with eigenvalues $-1 \\pm 3i$ is $A = {M(A)}$ ($\\operatorname{{tr}}A = -2$, $\\det A = 10$, $\\lambda = -1 \\pm 3i$; $a_{{12}} = {tex(A[0, 1])} < 0$).")
            out = planar.complex_pair(Doc(), A, "t")
            claim_canon(f"4II-E8-{l}", out)
            portrait.portrait(p3, out, pre)
        elif kind == "rep":
            A = sp.Matrix(data["A"])
            lam, v1 = data["lam"], sp.Matrix(data["v1"])
            N = A - lam * sp.eye(2)
            if l == "iii":
                p3.p(f"Single eigenvalue $13$ with one eigenvector $(3, 2)^T$: $A \\neq 13I$ (a star would have two independent eigenvectors), so $N = A - 13I$ is non-zero, $N^2 = O$ and $\\ker N = \\operatorname{{span}}\\{{(3, 2)^T\\}}$. Hence $N = c\\begin{{pmatrix}} 3 \\\\ 2 \\end{{pmatrix}}(2, -3) = c\\begin{{pmatrix}} 6 & -9 \\\\ 4 & -6 \\end{{pmatrix}}$ (rows orthogonal to $(3, 2)$ so that $N(3, 2)^T = \\mathbf 0$), and $a_{{12}} = N_{{12}} = -9c$. The condition $\\dot x > 0$ at $(0, 1)$ means $a_{{12}} > 0$, so $c < 0$; take $c = -1$: $N = {M(N)}$, $A = 13I + N = {M(A)}$.")
            else:
                p3.p(f"Single eigenvalue $-3$ with one eigenvector $(1, -1)^T$: $A \\neq -3I$ and $N = A + 3I \\neq O$ with $\\ker N = \\operatorname{{span}}\\{{(1, -1)^T\\}}$. Hence $N = c\\begin{{pmatrix}} 1 & 1 \\\\ -1 & -1 \\end{{pmatrix}}$ and $a_{{12}} = N_{{12}} = c$. The condition $\\dot x > 0$ at $(0, 1)$ means $a_{{12}} > 0$, so $c > 0$; take $c = 1$: $N = {M(N)}$, $A = -3I + N = {M(A)}$.")
            assert N * v1 == sp.zeros(2, 1) and N * N == sp.zeros(2, 2) and A[0, 1] > 0
            out = planar.repeated(Doc(), A, "t")
            claim_canon(f"4II-E8-{l}", out)
            portrait.portrait(p3, out, pre)
        else:
            lam = data["lam"]
            A = sp.Matrix([[lam, 0], [0, lam]])
            p3.p(f"$A$ is a multiple of the identity with eigenvalue $-7$: $A = {M(A)}$.")
            out = planar.repeated(Doc(), A, "t")
            claim_canon(f"4II-E8-{l}", out)
            portrait.portrait(p3, out, pre)
    p4 = n.phase(4, "Interpretation and checks")
    p4.table(["Item", "Origin", "Stability"],
             [["(i)", "saddle", "unstable"], ["(ii)", "spiral, counter-clockwise", "stable"], ["(iii)", "improper node", "unstable"], ["(iv)", "node, tangent to $\\mathbf v_1 = (2, 1)$", "stable"],
              ["(v)", "improper node", "stable"], ["(vi)", "centre, clockwise", "stable, not asymptotically"], ["(vii)", "node, tangent to $\\mathbf v_1 = (3, 2)$", "unstable"],
              ["(viii)", "spiral, counter-clockwise", "unstable"], ["(ix)", "star", "asymptotically stable"]])
    p4.ul(["The nine items cover the nine pictures of Robinson's classification (Ch. 31, Fig. 31.1, as reproduced in Topic 4 Fig. 4.11; the unstable star is the time reversal of the stable one): saddle (i); stable node (iv); unstable node (vii); stable spiral (ii); unstable spiral (viii); centre (vi); stable star (ix); stable improper node (v); unstable improper node (iii).",
           "The tangency of nodes was verified on the numerical orbits: the orbits of (iv) are tangent at the origin to $\\mathbf v_1 = (2, 1)$ ($|\\lambda| = 2 < 3$) and those of (vii) to $\\mathbf v_1 = (3, 2)$ ($1 < 5$).",
           "In (iii) and (v) the sign condition only chooses the orientation of the S-shaped orbits (on which side of the eigenline the orbit moves along $+\\mathbf v_1$); the eigenline and the type do not depend on it.",
           "Trace-determinant check: (i) $\\det A = -6 < 0$ saddle; (iv) $\\operatorname{tr} = -5$, $\\det = 6$, $\\Delta = 1 > 0$ stable node; (vii) $\\operatorname{tr} = 6$, $\\det = 5$ unstable node; (iii) $\\operatorname{tr}^2 = 4\\det = 676$; (ix) $\\operatorname{tr}^2 = 4\\det = 196$.",
           "Spiral (viii) has $\\rho/\\omega = 5$: one turn multiplies the radius by $e^{2\\pi\\rho/\\omega} = e^{10\\pi} \\approx 4\\times 10^{13}$, so it is a genuine spiral that, on the scale of the figure, looks like almost radial curves (the winding is invisible after the first fraction of a turn); in (ii), $\\rho/\\omega = -\\tfrac13$ the winding is clearly visible."])
    return n


def build():
    from . import ch4b
    return [ch4b.ex1(), ch4b.ex2(), ch4b.ex3(), ch4b.ex4(), ex5(), ex6(), ex7(), ex8()]
