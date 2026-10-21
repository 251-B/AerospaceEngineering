"""Chapter 4, part 2 (probls_ch4-ii_2627.pdf): eight exercises on complex and repeated eigenvalues."""
import sympy as sp

from . import planar, portrait
from .core import Doc, Note, register_figure, tex, vec, t
from .planar import M, par

SHEET = dict(code="Ch4-II", label="4.II", id_prefix="e",
             tema="Tema 4: Systems of First-Order ODEs and the Phase Plane",
             index_note="Problem Set - Chapter 4 Part 2",
             theory_note="Concept - Planar Systems with Complex Eigenvalues")
SOURCE = "probls_ch4-ii_2627.pdf"
CLAIMS = []


def claim_canon(tag, out):
    CLAIMS.append(dict(kind="canon", id=tag, A=out["A"], Q=out["Q"], J=out["J"], sol=out.get("sol")))


# eigen-data of Exercise 1: (rho, omega, eta_+ as (re, im) pairs per component, sign of xdot on x = 0, y > 0, statement text)
EX1 = [
    ("i", 1, 3, ((1, 0), (2, -1)), "<", r"\lambda_\pm = 1 \pm 3i \text{ with } \boldsymbol\eta_\pm = (1,\ 2 \mp i),\ \dot x < 0"),
    ("ii", 0, 3, ((1, 2), (1, -3)), "<", r"\lambda_\pm = \pm 3i \text{ with } \boldsymbol\eta_\pm = (1 \pm 2i,\ 1 \mp 3i),\ \dot x < 0"),
    ("iii", -2, 1, ((1, -1), (3, 1)), ">", r"\lambda_\pm = -2 \pm i \text{ with } \boldsymbol\eta_\pm = (1 \mp i,\ 3 \pm i),\ \dot x > 0"),
    ("iv", -1, 1, ((1, 0), (0, 1)), ">", r"\lambda_\pm = -1 \pm i \text{ with } \boldsymbol\eta_\pm = (1,\ \pm i),\ \dot x > 0"),
    ("v", 2, 2, ((0, 3), (5, -4)), "<", r"\lambda_\pm = 2 \pm 2i \text{ with } \boldsymbol\eta_\pm = (\pm 3i,\ 5 \mp 4i),\ \dot x < 0"),
    ("vi", 5, 3, ((2, 5), (0, -1)), "<", r"\lambda_\pm = 5 \pm 3i \text{ with } \boldsymbol\eta_\pm = (2 \pm 5i,\ \mp i),\ \dot x < 0"),
    ("vii", 0, 7, ((1, 1), (-1, 2)), ">", r"\lambda_\pm = \pm 7i \text{ with } \boldsymbol\eta_\pm = (1 \pm i,\ -1 \pm 2i),\ \dot x > 0"),
    ("viii", -13, 17, ((-8, 6), (4, -5)), ">", r"\lambda_\pm = -13 \pm 17i \text{ with } \boldsymbol\eta_\pm = (\pm 6i - 8,\ 4 \mp 5i),\ \dot x > 0"),
]


def uw(eta):
    u = sp.Matrix([eta[0][0], eta[1][0]])
    w = sp.Matrix([eta[0][1], eta[1][1]])
    return u, w


def cplx(re, im):
    return sp.sympify(re) + sp.I * sp.sympify(im)


def eta_tex(eta):
    return "\\begin{pmatrix} " + tex(cplx(*eta[0])) + " \\\\ " + tex(cplx(*eta[1])) + " \\end{pmatrix}"


def build_from_complex(doc, rho, om, u, w):
    """A = Q J Q^{-1} from eigen-data, with the products written out."""
    Q = sp.Matrix.hstack(u, w)
    J = sp.Matrix([[rho, om], [-om, rho]])
    A = sp.simplify(Q * J * Q.inv())
    doc.p("The matrix is not given; it is rebuilt from $A\\mathbf u = \\rho\\mathbf u - \\omega\\mathbf w$, $A\\mathbf w = \\omega\\mathbf u + \\rho\\mathbf w$ (Topic 4 Eq. 7.4), which say $AQ = QJ$ with $Q = [\\mathbf u \\mid \\mathbf w]$, so $A = QJQ^{-1}$:")
    doc.m(f"Q = {M(Q)}, \\quad J = {M(J)}, \\quad \\det Q = {tex(Q.det())}, \\quad Q^{{-1}} = {M(Q.inv())}")
    QJ = planar.matmul_steps(doc, Q, J, "Q", "J", "QJ")
    doc.m(f"QJ = {M(QJ)}")
    A2 = planar.matmul_steps(doc, QJ, Q.inv(), "(QJ)", "Q^{-1}", "A")
    assert A2 == A
    doc.m(f"A = QJQ^{{-1}} = {M(A)}")
    return A


def ex1():
    n = Note(SHEET, 1, "Eight Spiral and Centre Portraits from Complex Eigen-data", "Complex Eigenvalues • Spirals and Centres • Eight Portraits",
             ["problema-resuelto", "autovalores-complejos", "espirales", "centros", "retrato-de-fase"], SOURCE)
    st = n.statement
    st.p("Draw the phase portrait for the equation $d\\mathbf x/dt = A\\mathbf x$, when the eigenvalues ($\\lambda_\\pm$) and eigenvectors ($\\boldsymbol\\eta_\\pm$) of $A$ are as given. The sign of $\\dot x$ is indicated when $x = 0$ and $y > 0$.")
    st.ul([f"({l}) ${txt}$;" if l != "viii" else f"({l}) ${txt}$." for l, _, _, _, _, txt in EX1])
    p1 = n.phase(1, "Setup and classification")
    p1.p("In each item $\\lambda_\\pm = \\rho \\pm i\\omega$ with $\\omega > 0$ and $\\boldsymbol\\eta_+ = \\mathbf u + i\\mathbf w$ is the eigenvector of $\\lambda_+ = \\rho + i\\omega$ (the second eigenvector $\\boldsymbol\\eta_- = \\bar{\\boldsymbol\\eta}_+$ carries no new information). The type is fixed by $\\rho$: $\\rho < 0$ stable spiral, $\\rho > 0$ unstable spiral, $\\rho = 0$ centre (Topic 4 Sec. 7.6). The sense of rotation follows from the vector field at $(0, 1)^T$: $\\dot{\\mathbf x} = A(0, 1)^T = (a_{12}, a_{22})^T$, and $\\dot x = a_{12} > 0$ means clockwise, $\\dot x < 0$ counter-clockwise (Topic 4 Sec. 7.8). The sign of $\\dot x$ given in the statement is therefore the sense of rotation:")
    p1.table(["Item", "$\\rho$", "$\\omega$", "Type", "Given sign of $\\dot x$ at $(0, 1)$", "Sense"],
             [[f"({l})", f"${r}$", f"${o}$", "centre" if r == 0 else ("stable spiral" if r < 0 else "unstable spiral"), f"${s}\\ 0$", "counter-clockwise" if s == "<" else "clockwise"]
              for l, r, o, e, s, _ in EX1])
    p2 = n.phase(2, "Formulation")
    p2.p("For each item the eigenvector gives $\\mathbf u = \\operatorname{Re}\\boldsymbol\\eta_+$ and $\\mathbf w = \\operatorname{Im}\\boldsymbol\\eta_+$, hence $Q = [\\mathbf u \\mid \\mathbf w]$ and the canonical form $J = \\begin{pmatrix} \\rho & \\omega \\\\ -\\omega & \\rho \\end{pmatrix}$ (rotation clockwise in the $\\mathbf z$-plane). The matrix $A = QJQ^{-1}$ is rebuilt, the given sign of $\\dot x$ is checked against $a_{12}$, and the portrait is drawn in the $\\mathbf z$-plane and in the $(x, y)$-plane ($\\mathbf x = Q\\mathbf z$).")
    p3 = n.phase(3, "Derivation of the eight portraits")
    for l, rho, om, eta, sgn, txt in EX1:
        p3.h(3, f"({l}) ${txt}$")
        u, w = uw(eta)
        p3.p(f"Split the eigenvector of $\\lambda_+ = {tex(cplx(rho, om))}$ into real and imaginary parts, $\\boldsymbol\\eta_+ = {eta_tex(eta)} = \\mathbf u + i\\mathbf w$, so $\\rho = {tex(rho)}$, $\\omega = {tex(om)}$ and")
        p3.m(f"\\mathbf u = {vec(u[0], u[1])}, \\qquad \\mathbf w = {vec(w[0], w[1])}")
        A = build_from_complex(p3, sp.Integer(rho), sp.Integer(om), u, w)
        a12 = A[0, 1]
        ok = (a12 < 0) == (sgn == "<")
        assert ok, (l, a12, sgn)
        p3.p(f"Check of the given sign: $\\dot x$ at $(0, 1)$ equals $a_{{12}} = {tex(a12)}$, which is {'negative' if a12 < 0 else 'positive'}, in agreement with the statement ($\\dot x {sgn} 0$).")
        out = planar.complex_pair(p3, A, "t", given=(sp.Integer(rho), sp.Integer(om), u, w))
        claim_canon(f"4II-E1-{l}", out)
        portrait.portrait(p3, out, f"ch4b-e1-{l}")
    p4 = n.phase(4, "Interpretation and checks")
    p4.table(["Item", "$A$", "Type", "Sense of rotation"],
             [[f"({l})", f"${M(sp.simplify(sp.Matrix.hstack(*uw(eta)) * sp.Matrix([[r, o], [-o, r]]) * sp.Matrix.hstack(*uw(eta)).inv()))}$",
               "centre" if r == 0 else ("stable spiral" if r < 0 else "unstable spiral"), "counter-clockwise" if s == "<" else "clockwise"] for l, r, o, eta, s, _ in EX1])
    p4.ul(["In every item $\\det Q$ and the sign of $a_{12}$ agree (the code asserts $\\det Q > 0 \\Leftrightarrow a_{12} > 0$), which is the Topic 4 rule: the $\\mathbf z$-plane turns clockwise, and $Q$ reverses the sense exactly when $\\det Q < 0$.",
           "Centres (ii) and (vii) ($\\rho = 0$): $\\operatorname{tr}A = 0$ and $\\det A = \\omega^2 > 0$; the orbits are closed ellipses with period $2\\pi/\\omega$ ($2\\pi/3$ and $2\\pi/7$).",
           "Spirals: (i), (v), (vi) unstable; (iii), (iv), (viii) stable. The growth/decay factor per turn is $e^{2\\pi\\rho/\\omega}$, stated in each item; (viii) decays extremely fast ($e^{-26\\pi/17} \\approx 0.008$ per turn), so its spiral is nearly invisible after one turn.",
           "The eigen-data are consistent: $A\\boldsymbol\\eta_+ = \\lambda_+\\boldsymbol\\eta_+$ holds in each item by construction of $A$ (Eq. 7.4 verified entry by entry)."])
    return n


def ex2():
    n = Note(SHEET, 2, "General Solutions for the Eight Complex Eigen-data", "Real General Solution • Euler's Formula",
             ["problema-resuelto", "solucion-general", "autovalores-complejos", "formula-de-euler"], SOURCE)
    st = n.statement
    st.p("Write down the general solution of the equation $d\\mathbf x/dt = A\\mathbf x$, when the eigenvalues ($\\lambda_\\pm$) and eigenvectors ($\\boldsymbol\\eta_\\pm$) of $A$ are those in the previous exercise.")
    p1 = n.phase(1, "Setup")
    p1.p("The eight eigen-data are those of Exercise 1 (listed there). For each, $\\boldsymbol\\eta_+ = \\mathbf u + i\\mathbf w$ is the eigenvector of $\\lambda_+ = \\rho + i\\omega$.")
    p2 = n.phase(2, "Formulation: the real general solution")
    p2.p("Complex solutions $e^{\\lambda_+t}\\boldsymbol\\eta_+$ and $e^{\\lambda_-t}\\bar{\\boldsymbol\\eta}_+$ combine into real ones: choose conjugate coefficients, $\\mathbf x = 2\\operatorname{Re}\\left[Ce^{(\\rho + i\\omega)t}(\\mathbf u + i\\mathbf w)\\right]$ with $C = \\alpha + i\\beta$. Expanding $e^{i\\omega t} = \\cos\\omega t + i\\sin\\omega t$ (Euler) and keeping the real part, with $c_1 = 2\\alpha$, $c_2 = -2\\beta$ (Topic 4 Eq. 7.3, Robinson Eq. 29.2):")
    p2.m(r"\mathbf x(t) = e^{\rho t}\Big[\left(c_1\cos\omega t + c_2\sin\omega t\right)\mathbf u + \left(c_2\cos\omega t - c_1\sin\omega t\right)\mathbf w\Big]")
    p2.p("Check of the derivation of the real part: $(a + ib)(\\mathbf u + i\\mathbf w)$ has real part $a\\mathbf u - b\\mathbf w$ because $i\\cdot i = -1$; with $a = \\alpha\\cos\\omega t - \\beta\\sin\\omega t$ and $b = \\beta\\cos\\omega t + \\alpha\\sin\\omega t$ this is $\\frac12[(c_1\\cos\\omega t + c_2\\sin\\omega t)\\mathbf u + (c_2\\cos\\omega t - c_1\\sin\\omega t)\\mathbf w]$ after substituting $\\alpha = c_1/2$, $\\beta = -c_2/2$.")
    p3 = n.phase(3, "Derivation: the eight solutions")
    c1, c2 = sp.symbols("c_1 c_2")
    for l, rho, om, eta, sgn, txt in EX1:
        u, w = uw(eta)
        p3.h(3, f"({l}) ${txt}$")
        p3.p(f"$\\rho = {tex(rho)}$, $\\omega = {tex(om)}$, $\\mathbf u = {vec(u[0], u[1])}$, $\\mathbf w = {vec(w[0], w[1])}$. Substituting in the general formula,")
        p3.m(f"\\mathbf x(t) = e^{{{tex(rho)}t}}\\left[\\left(c_1\\cos {tex(om)}t + c_2\\sin {tex(om)}t\\right){vec(u[0], u[1])} + \\left(c_2\\cos {tex(om)}t - c_1\\sin {tex(om)}t\\right){vec(w[0], w[1])}\\right]")
        a1 = c1 * sp.cos(om * t) + c2 * sp.sin(om * t)
        b1 = c2 * sp.cos(om * t) - c1 * sp.sin(om * t)
        pref = sp.exp(rho * t)
        x1 = sp.expand(pref * (a1 * u[0] + b1 * w[0]))
        x2 = sp.expand(pref * (a1 * u[1] + b1 * w[1]))
        p3.p("Component by component:")
        p3.m(f"x(t) = {tex(x1)}, \\qquad y(t) = {tex(x2)}")
        # verification against A
        Q = sp.Matrix.hstack(u, w)
        A = sp.simplify(Q * sp.Matrix([[rho, om], [-om, rho]]) * Q.inv())
        res = sp.simplify(sp.Matrix([sp.diff(x1, t), sp.diff(x2, t)]) - A * sp.Matrix([x1, x2]))
        assert res == sp.zeros(2, 1), (l, res)
        p3.p(f"Check: with $A = {M(A)}$ (Exercise 1), $\\dot{{\\mathbf x}} - A\\mathbf x = \\mathbf 0$ identically (verified symbolically).")
        CLAIMS.append(dict(kind="sol", id=f"4II-E2-{l}", A=A, sol=(x1, x2)))
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["The two constants are real and are the initial coordinates in the $(\\mathbf u, \\mathbf w)$ basis: $(c_1, c_2)^T = Q^{-1}\\mathbf x_0$.",
           "Centres $(\\rho = 0)$: (ii) and (vii) give purely periodic $\\mathbf x(t)$ with period $2\\pi/3$ and $2\\pi/7$; spirals have an envelope $e^{\\rho t}$.",
           "Linear independence: $e^{\\rho t}(\\cos\\omega t\\,\\mathbf u - \\sin\\omega t\\,\\mathbf w)$ and $e^{\\rho t}(\\sin\\omega t\\,\\mathbf u + \\cos\\omega t\\,\\mathbf w)$ have Wronskian $e^{2\\rho t}\\det[\\mathbf u\\ \\mathbf w] \\neq 0$ since $\\mathbf u, \\mathbf w$ are independent (Exercise 4).",
           "Dimensional check: the exponent $\\rho t$ and the phase $\\omega t$ are dimensionless when $\\rho$ and $\\omega$ are rates in s$^{-1}$ and $t$ in s."])
    return n


EX3 = [("i", [[0, -1], [1, -1]]), ("ii", [[-2, 3], [-6, 4]]), ("iii", [[-11, -2], [13, -9]]), ("iv", [[7, -5], [10, -3]])]


def ex3():
    n = Note(SHEET, 3, "Canonical Form of Four Systems with Complex Eigenvalues", "Canonical Form • Q = [u | w] • Four Matrices",
             ["problema-resuelto", "forma-canonica", "autovalores-complejos", "cambio-de-base"], SOURCE)
    st = n.statement
    st.p("For the following equations find the eigenvalues and eigenvectors of the matrix on the right-hand side, and hence find the coordinate transformation that will put the equations into their standard simple (canonical) form. Show that this transformation has the desired effect.")
    st.ul([f"({l}) $\\dfrac{{d\\mathbf x}}{{dt}} = {M(sp.Matrix(A))}\\mathbf x$;" if l != "iv" else f"({l}) $\\dfrac{{d\\mathbf x}}{{dt}} = {M(sp.Matrix(A))}\\mathbf x$." for l, A in EX3])
    p1 = n.phase(1, "Setup")
    p1.p("The standard (canonical) form for a complex pair $\\rho \\pm i\\omega$ is $\\dot{\\mathbf z} = J\\mathbf z$ with $J = \\begin{pmatrix} \\rho & \\omega \\\\ -\\omega & \\rho \\end{pmatrix}$, reached by $\\mathbf z = Q^{-1}\\mathbf x$ with $Q = [\\mathbf u \\mid \\mathbf w]$, $\\mathbf u + i\\mathbf w$ the eigenvector of $\\rho + i\\omega$ (Topic 4 Sec. 7.4). For every matrix $\\Delta = (\\operatorname{tr}A)^2 - 4\\det A < 0$ (checked in each item), so the eigenvalues are complex conjugate.")
    p2 = n.phase(2, "Formulation")
    p2.p("Steps for each matrix: characteristic equation, eigenvalue $\\rho + i\\omega$, eigenvector via the first row, $\\mathbf u, \\mathbf w$, relations (7.4), $Q$ and $Q^{-1}$, and the explicit product $Q^{-1}AQ = J$.")
    p3 = n.phase(3, "Derivation")
    for l, A in EX3:
        A = sp.Matrix(A)
        p3.h(3, f"({l}) $A = {M(A)}$")
        out = planar.complex_pair(p3, A, "t")
        claim_canon(f"4II-E3-{l}", out)
        p3.p(f"The canonical system is $\\dot z_1 = {tex(out['rho'])}z_1 + ({tex(out['om'])})z_2$, $\\dot z_2 = -({tex(out['om'])})z_1 + {tex(out['rho'])}z_2$: a rotation clockwise with angular speed $\\omega = {tex(out['om'])}$ combined with a radial factor $e^{{{tex(out['rho'])}t}}$.")
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["In each item the explicit product $Q^{-1}AQ$ reproduces $J$ exactly (entry-by-entry arithmetic above).",
           "(i) has an irrational $\\omega = \\sqrt3/2$ (eigenvalues $-\\tfrac12 \\pm \\tfrac{\\sqrt3}{2}i$, with the surds carried exactly): stable spiral. (ii) $1 \\pm 3i$, unstable spiral; (iii) $-10 \\pm 5i$, stable spiral (fast decay, ratio $|\\rho|/\\omega = 2$); (iv) $2 \\pm 5i$, unstable spiral.",
           "The orientation of $Q$ ($\\det Q$ sign) decides whether the clockwise rotation of the $\\mathbf z$-plane stays clockwise in the $\\mathbf x$-plane; it is $b\\omega$ here (positive iff $b > 0$).",
           "The eigenvalues of each matrix satisfy $\\lambda_+ + \\lambda_- = \\operatorname{tr}A$ and $\\lambda_+\\lambda_- = \\det A$ (checked in the text)."])
    return n


def ex4():
    n = Note(SHEET, 4, "Real and Imaginary Parts of a Complex Eigenvector Are Independent", "Linear Independence • Complex Eigenvectors",
             ["problema-resuelto", "independencia-lineal", "autovectores-complejos", "demostracion"], SOURCE)
    st = n.statement
    st.p("In the previous chapter we used the result that eigenvectors which correspond to distinct eigenvalues are linearly independent. Use this result to show that the real and imaginary parts of complex eigenvectors are linearly independent.")
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("Let $A$ be a real $2\\times 2$ matrix with a non-real eigenvalue $\\lambda = \\rho + i\\omega$ ($\\omega \\neq 0$) and eigenvector $\\mathbf v = \\mathbf u + i\\mathbf w \\in \\mathbb C^2$, $\\mathbf u, \\mathbf w \\in \\mathbb R^2$. To show: $\\mathbf u$ and $\\mathbf w$ are linearly independent over $\\mathbb R$, i.e. $\\alpha\\mathbf u + \\beta\\mathbf w = \\mathbf 0$ with $\\alpha, \\beta \\in \\mathbb R$ implies $\\alpha = \\beta = 0$.")
    p2 = n.phase(2, "Formulation")
    p2.p("Ingredients: (a) $\\bar{\\mathbf v} = \\mathbf u - i\\mathbf w$ is an eigenvector for $\\bar\\lambda$ (conjugate $A\\mathbf v = \\lambda\\mathbf v$ and use $\\bar A = A$ since $A$ is real); (b) $\\lambda \\neq \\bar\\lambda$ because $\\omega \\neq 0$; (c) eigenvectors of distinct eigenvalues are linearly independent (over $\\mathbb C$) (Topic 4, Appendix B argument).")
    p3 = n.phase(3, "Derivation")
    p3.h(4, "Step 1: $\\mathbf v$ and $\\bar{\\mathbf v}$ are independent")
    p3.p("By (a), (b) and the quoted result, $\\mathbf v$ and $\\bar{\\mathbf v}$ are linearly independent in $\\mathbb C^2$: $\\gamma\\mathbf v + \\delta\\bar{\\mathbf v} = \\mathbf 0$ with $\\gamma, \\delta \\in \\mathbb C$ forces $\\gamma = \\delta = 0$.")
    p3.h(4, "Step 2: express $\\mathbf u, \\mathbf w$ through $\\mathbf v, \\bar{\\mathbf v}$")
    p3.m(r"\mathbf u = \frac{\mathbf v + \bar{\mathbf v}}{2}, \qquad \mathbf w = \frac{\mathbf v - \bar{\mathbf v}}{2i}")
    p3.h(4, "Step 3: a real relation must be trivial")
    p3.p("Suppose $\\alpha\\mathbf u + \\beta\\mathbf w = \\mathbf 0$ with $\\alpha, \\beta \\in \\mathbb R$. Substitute Step 2 and collect the coefficients of $\\mathbf v$ and $\\bar{\\mathbf v}$:")
    p3.m(r"\alpha\frac{\mathbf v + \bar{\mathbf v}}{2} + \beta\frac{\mathbf v - \bar{\mathbf v}}{2i} = \underbrace{\left(\frac{\alpha}{2} + \frac{\beta}{2i}\right)}_{\gamma}\mathbf v + \underbrace{\left(\frac{\alpha}{2} - \frac{\beta}{2i}\right)}_{\delta}\bar{\mathbf v} = \mathbf 0")
    p3.p("By Step 1, $\\gamma = \\delta = 0$. Using $\\frac1i = -i$: $\\gamma = \\frac{\\alpha - i\\beta}{2}$ and $\\delta = \\frac{\\alpha + i\\beta}{2}$. Then $\\gamma = 0$ means $\\alpha - i\\beta = 0$; with $\\alpha, \\beta$ real, real and imaginary parts give $\\alpha = 0$ and $\\beta = 0$. $\\blacksquare$")
    p3.h(4, "Check against the direct argument")
    p3.p("Alternative (Topic 4 Sec. 7.3): if $\\mathbf w = k\\mathbf u$ (or $\\mathbf u = \\mathbf 0$), $\\mathbf v$ would be a complex multiple of one real vector $\\mathbf r$, forcing $A\\mathbf r = \\lambda\\mathbf r$ with $A\\mathbf r$ real, so $\\lambda$ would be real: contradiction. The two proofs agree; the one above only uses the independence of eigenvectors of distinct eigenvalues, as the exercise requests.")
    p4 = n.phase(4, "Interpretation and checks")
    p4.ul(["Consequence: $Q = [\\mathbf u \\mid \\mathbf w]$ is invertible, which is what makes the change of coordinates $\\mathbf z = Q^{-1}\\mathbf x$ possible for complex eigenvalues (Exercises 3 and 1).",
           "Numerical check with the eigenvector of Topic 4 Example 7.1, $\\mathbf v = (5, -1 + 3i)^T$: $\\mathbf u = (5, -1)^T$, $\\mathbf w = (0, 3)^T$, $\\det[\\mathbf u\\ \\mathbf w] = 15 \\neq 0$.",
           "The argument fails for a real eigenvalue ($\\lambda = \\bar\\lambda$): then $\\mathbf w = \\mathbf 0$ can occur, consistent with Step 1 breaking down.",
           "In dimension $n$ the same idea shows that the real and imaginary parts of eigenvectors of different conjugate pairs together with real eigenvectors remain independent."])
    return n


EX5 = [("i", 3, 3, (2, 1), (1, -1), ((2, 1), (1, -1))), ("ii", 0, 3, (0, 3), (1, 2), ((0, 1), (3, 2))), ("iii", -2, 1, (1, 1), (1, -1), ((1, 1), (1, -1)))]
EX5TXT = {"i": r"\lambda_\pm = 3 \pm 3i,\ \boldsymbol\eta_\pm = (2 \pm i,\ 1 \mp i)", "ii": r"\lambda_\pm = \pm 3i,\ \boldsymbol\eta_\pm = (\pm i,\ 3 \pm 2i)", "iii": r"\lambda_\pm = -2 \pm i,\ \boldsymbol\eta_\pm = (1 \pm i,\ 1 \mp i)"}
