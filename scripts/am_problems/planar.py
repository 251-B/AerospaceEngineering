"""Planar linear systems x' = A x solved by the method of Topic 4, every step written out.

Conventions of the portal (Topic 4, Sections 5, 7 and 8):
  distinct real eigenvalues   Q = [v1 | v2],  J = diag(l1, l2)
  complex pair rho +- i omega Q = [u | w] with v = u + i w the eigenvector of rho + i omega,  J = [[rho, omega], [-omega, rho]]
  repeated eigenvalue         Q = [v1 | v2] with (A - l I) v2 = v1,  J = [[l, 1], [0, l]]
  z = Q^{-1} x,  z' = J z,  x = Q z.
"""
import math

import sympy as sp

from .core import tex, mat, vec, register_figure, t

I2 = sp.eye(2)


def lin(a, sa, b, sb):
    """a*sa + b*sb as LaTeX with clean signs (zero terms dropped)."""
    out = ""
    for coef, sym in ((a, sa), (b, sb)):
        coef = sp.sympify(coef)
        if coef == 0:
            continue
        neg = coef.could_extract_minus_sign()
        mag = -coef if neg else coef
        term = ("" if mag == 1 else tex(mag) + (" " if False else "")) + sym
        if len(sp.Add.make_args(mag)) > 1:
            term = f"({tex(mag)})" + sym
        out += ("-" if neg else "") + term if not out else (" - " if neg else " + ") + term
    return out or "0"


def par(x):
    """tex of x, in parentheses when it is negative or a sum (for products written out)."""
    x = sp.sympify(x)
    s = tex(x)
    if x.could_extract_minus_sign() or len(sp.Add.make_args(x)) > 1 or isinstance(x, sp.Mul) and False:
        return f"({s})"
    return s


def M(m):
    return mat([[m[i, j] for j in range(m.cols)] for i in range(m.rows)])


def prim(v):
    """Primitive integer direction of a 2-vector with rational entries (first non-zero entry positive)."""
    den = sp.ilcm(*[sp.fraction(sp.nsimplify(x))[1] for x in v])
    w = [sp.nsimplify(x) * den for x in v]
    g = sp.igcd(*[int(x) for x in w]) or 1
    w = [x / g for x in w]
    for x in w:
        if x != 0:
            if x < 0:
                w = [-y for y in w]
            break
    return sp.Matrix(w)


# --------------------------------------------------------------------------- products written out entry by entry
def matmul_steps(doc, X, Y, nx, ny, nxy=None):
    """Write X*Y entry by entry (X, Y SymPy matrices); returns X*Y."""
    P = X * Y
    lines = []
    for i in range(X.rows):
        for j in range(Y.cols):
            terms = " + ".join(f"{par(X[i, k])}\\cdot{par(Y[k, j])}" for k in range(X.cols))
            lines.append(f"({nxy or nx + ny})_{{{i + 1}{j + 1}}} &= {terms} = {tex(P[i, j])}")
    doc.m(r"\begin{aligned} " + r" \\ ".join(lines) + r" \end{aligned}")
    return P


def inverse_steps(doc, Q, name="Q"):
    a, b, c, d = Q[0, 0], Q[0, 1], Q[1, 0], Q[1, 1]
    det = sp.simplify(Q.det())
    Qi = Q.inv()
    doc.p(f"$\\det {name} = ({tex(a)})({tex(d)}) - ({tex(b)})({tex(c)}) = {tex(det)}$, which is not zero, so ${name}$ is invertible. For a $2\\times 2$ matrix $\\begin{{pmatrix}} a & b \\\\ c & d \\end{{pmatrix}}^{{-1}} = \\frac{{1}}{{ad - bc}}\\begin{{pmatrix}} d & -b \\\\ -c & a \\end{{pmatrix}}$ (Robinson, Appendix B):")
    doc.m(f"{name}^{{-1}} = \\frac{{1}}{{{tex(det)}}}{mat([[d, -b], [-c, a]])} = {M(Qi)}")
    return Qi, det


# --------------------------------------------------------------------------- characteristic polynomial and eigenvalues
def charpoly_steps(doc, A):
    a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
    lam = sp.Symbol("lambda")
    tr, det = a + d, A.det()
    doc.p("Characteristic equation $\\det(A - \\lambda I) = 0$ (Topic 4, Eq. 27.8):")
    doc.m(r"\det(A - \lambda I) = \begin{vmatrix} " + f"{tex(a)} - \\lambda & {tex(b)} \\\\ {tex(c)} & {tex(d)} - \\lambda" + r" \end{vmatrix} = "
          f"({tex(a)} - \\lambda)({tex(d)} - \\lambda) - ({tex(b)})({tex(c)})")
    expanded = sp.expand((a - lam) * (d - lam) - b * c)
    doc.m(f"= \\lambda^2 - ({tex(a)} + {par(d)})\\lambda + ({tex(a)}\\cdot{par(d)} - {par(b)}\\cdot{par(c)}) = \\lambda^2 - ({tex(tr)})\\lambda + ({tex(det)}) = {tex(expanded)}")
    disc = sp.expand(tr ** 2 - 4 * det)
    doc.p(f"$\\operatorname{{tr}}A = {tex(tr)}$, $\\det A = {tex(det)}$, discriminant $\\Delta = (\\operatorname{{tr}}A)^2 - 4\\det A = {tex(tr ** 2)} - {par(4 * det)} = {tex(disc)}$.")
    roots = sp.roots(sp.Poly(expanded, lam))
    return expanded, tr, det, disc, roots


def real_roots_text(doc, tr, det, disc, roots):
    lam = sp.Symbol("lambda")
    r = sorted(roots, key=lambda z: sp.N(z))
    sq = sp.sqrt(disc)
    doc.m(f"\\lambda = \\frac{{{tex(tr)} \\pm \\sqrt{{{tex(disc)}}}}}{{2}} = \\frac{{{tex(tr)} \\pm {tex(sq)}}}{{2}} \\quad\\Longrightarrow\\quad \\lambda_1 = {tex(r[-1])},\\ \\lambda_2 = {tex(r[0])}" if len(r) == 2 else f"\\lambda = {tex(r[0])}")
    return r


# --------------------------------------------------------------------------- eigenvectors
def kernel_steps(doc, A, lam, name="v"):
    """Solve (A - lam I) v = 0 for real lam; returns the primitive integer eigenvector."""
    B = A - lam * I2
    doc.p(f"For $\\lambda = {tex(lam)}$: ${'(A - (' + tex(lam) + ')I)'}\\mathbf{{{name}}} = \\mathbf 0$, that is")
    doc.m(f"{M(B)}\\begin{{pmatrix}} v_1 \\\\ v_2 \\end{{pmatrix}} = \\begin{{pmatrix}} 0 \\\\ 0 \\end{{pmatrix}}")
    rows = [(B[0, 0], B[0, 1]), (B[1, 0], B[1, 1])]
    eqs = [f"{tex(r[0])}v_1 {'+' if (r[1] >= 0) else '-'} {tex(abs(r[1]))}v_2 = 0" for r in rows]
    doc.m(r"\begin{aligned} " + r" \\ ".join(f"{e}\\quad (\\text{{row {i + 1}}})" for i, e in enumerate(eqs)) + r" \end{aligned}")
    ns = B.nullspace()
    v = prim(ns[0])
    use = 0 if (rows[0] != (0, 0)) else 1
    p, q = rows[use]
    other = rows[1 - use]
    if other == (0, 0):
        rel = f"row {2 - use} is identically zero"
    else:
        ratio = sp.simplify(other[0] / p) if p != 0 else sp.simplify(other[1] / q)
        src, dst = (use + 1, 2 - use)
        rel = f"row {dst} is identical to row {src}" if ratio == 1 else f"row {dst} equals ${tex(ratio)}$ times row {src}"
    if p != 0 and q != 0:
        ratio_v = sp.nsimplify(-q / p)
        rv = {1: "", -1: "-"}.get(ratio_v, tex(ratio_v) + "\\,")
        how = f"so $v_1 = {rv}v_2$: every eigenvector is a multiple of $({tex(ratio_v)}, 1)^T$. The smallest integer representative is"
    elif q == 0:
        how = "so $v_1 = 0$ and $v_2$ is free; the simplest choice is"
    else:
        how = "so $v_2 = 0$ and $v_1$ is free; the simplest choice is"
    doc.p(f"The coefficient matrix is singular ($\\det(A - \\lambda I) = 0$), so the rows are proportional ({rel}) and express a single condition. Row {use + 1} reads ${tex(p)}v_1 + {par(q)}v_2 = 0$, {how}")
    doc.m(f"\\mathbf{{{name}}} = {vec(v[0], v[1])}")
    r = A * v
    assert r == lam * v, (A, lam, v)
    doc.p(f"Check: $A\\mathbf{{{name}}} = {vec(r[0], r[1])} = {tex(lam)}\\mathbf{{{name}}}$.")
    return v


# --------------------------------------------------------------------------- real distinct eigenvalues (nodes, saddles, line of equilibria)
def real_distinct(doc, A, tag, x0=None, first_eig=None, label_pairs=True, plane_labels=True, given=None):
    """Full treatment of x' = A x with two distinct real eigenvalues.

    given: optional ((l1, v1), (l2, v2)) when the exercise supplies the eigen-data (no characteristic polynomial then).
    Returns a dict with Q, J, lambdas, vectors."""
    if given is None:
        expanded, tr, det, disc, roots = charpoly_steps(doc, A)
        r = real_roots_text(doc, tr, det, disc, roots)
        l1, l2 = r[-1], r[0]
        doc.p(f"Check: $\\lambda_1 + \\lambda_2 = {tex(l1 + l2)} = \\operatorname{{tr}}A$ and $\\lambda_1\\lambda_2 = {tex(l1 * l2)} = \\det A$.")
        doc.h(4, "Eigenvectors")
        v1 = kernel_steps(doc, A, l1, "v_1")
        v2 = kernel_steps(doc, A, l2, "v_2")
    else:
        (l1, v1), (l2, v2) = given
        v1, v2 = sp.Matrix(v1), sp.Matrix(v2)
    Q = sp.Matrix.hstack(v1, v2)
    Lam = sp.diag(l1, l2)
    doc.h(4, "Change of coordinates")
    doc.p("The eigenvectors of distinct eigenvalues are linearly independent (Topic 4, Appendix B argument), so they form a basis. Put them as columns, $Q = [\\mathbf v_1 \\mid \\mathbf v_2]$, and define the new coordinates by $\\mathbf z = Q^{-1}\\mathbf x$, i.e. $\\mathbf x = Q\\mathbf z$:")
    doc.m(f"Q = {M(Q)}")
    Qi, detQ = inverse_steps(doc, Q)
    doc.p("Since $Q$ is constant, $\\dot{\\mathbf z} = Q^{-1}\\dot{\\mathbf x} = Q^{-1}A\\mathbf x = (Q^{-1}AQ)\\mathbf z$. Compute $AQ$ one column at a time, with $A\\mathbf v_j = \\lambda_j\\mathbf v_j$:")
    r1 = A * v1
    r2 = A * v2
    doc.m(f"A\\mathbf v_1 = {M(A)}{vec(v1[0], v1[1])} = {vec(r1[0], r1[1])} = {par(l1)}\\mathbf v_1, \\qquad A\\mathbf v_2 = {M(A)}{vec(v2[0], v2[1])} = {vec(r2[0], r2[1])} = {par(l2)}\\mathbf v_2")
    AQ = sp.Matrix.hstack(r1, r2)
    doc.m(f"AQ = [A\\mathbf v_1 \\mid A\\mathbf v_2] = {M(AQ)}")
    doc.p("Now multiply by $Q^{-1}$ on the left, entry by entry:")
    prod = matmul_steps(doc, Qi, AQ, "Q^{-1}", "(AQ)", "Q^{-1}AQ")
    assert prod == Lam, (prod, Lam)
    doc.m(f"Q^{{-1}}AQ = {M(prod)} = \\Lambda = {M(Lam)}")
    doc.p("The transformation has decoupled the system (the matrix is diagonal), as claimed.")
    doc.h(4, "Solution in the canonical plane")
    doc.m(f"\\dot z_1 = {lin(l1, 'z_1', 0, '')}, \\qquad \\dot z_2 = {lin(l2, 'z_2', 0, '')}")
    doc.p("Each equation is separable. If $z_i \\neq 0$, $\\frac{dz_i}{z_i} = \\lambda_i\\,dt$ and integrating, $\\ln|z_i| = \\lambda_i t + C_i$, so $z_i = c_i e^{\\lambda_i t}$ with $c_i = \\pm e^{C_i}$ (the solution $z_i \\equiv 0$ corresponds to $c_i = 0$). Equivalently, $\\frac{d}{dt}(e^{-\\lambda_i t}z_i) = 0$.")
    doc.m(f"z_1(t) = c_1 e^{{{tex(l1)}t}}, \\qquad z_2(t) = c_2 e^{{{tex(l2)}t}}")
    doc.h(4, "Back to the original coordinates")
    doc.p("$\\mathbf x = Q\\mathbf z = z_1\\mathbf v_1 + z_2\\mathbf v_2$, so the general solution is")
    e1, e2 = f"e^{{{tex(l1)}t}}", f"e^{{{tex(l2)}t}}"
    doc.m(f"\\mathbf x(t) = c_1 {e1}{vec(v1[0], v1[1])} + c_2 {e2}{vec(v2[0], v2[1])}")
    comp1 = sp.Add(sp.Symbol("c_1") * v1[0] * sp.exp(l1 * t), sp.Symbol("c_2") * v2[0] * sp.exp(l2 * t))
    comp2 = sp.Add(sp.Symbol("c_1") * v1[1] * sp.exp(l1 * t), sp.Symbol("c_2") * v2[1] * sp.exp(l2 * t))
    doc.m(f"x(t) = {tex(comp1)}, \\qquad y(t) = {tex(comp2)}")
    out = dict(Q=Q, Qi=Qi, J=Lam, l1=l1, l2=l2, v1=v1, v2=v2, A=A, kind="real", sol=(comp1, comp2))
    if x0 is not None:
        c = Qi * sp.Matrix(x0)
        doc.p(f"Initial condition $\\mathbf x(0) = {vec(*x0)}$: at $t = 0$, $\\mathbf z(0) = Q^{{-1}}\\mathbf x(0)$:")
        doc.m(f"{vec('c_1', 'c_2')} = {M(Qi)}{vec(*x0)} = {vec(c[0], c[1])}")
        out["c"] = c
        final = (comp1.subs({sp.Symbol('c_1'): c[0], sp.Symbol('c_2'): c[1]}), comp2.subs({sp.Symbol('c_1'): c[0], sp.Symbol('c_2'): c[1]}))
        doc.m(f"x(t) = {tex(sp.expand(final[0]))}, \\qquad y(t) = {tex(sp.expand(final[1]))}")
        out["final"] = final
    return out


# --------------------------------------------------------------------------- complex eigenvalues (spirals, centres)
def complex_pair(doc, A, tag, x0=None, given=None):
    """Full treatment for a complex pair; `given` = (rho, omega, u, w) when the exercise supplies the eigenvectors."""
    a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
    lam = sp.Symbol("lambda")
    if given is None:
        expanded, tr, det, disc, roots = charpoly_steps(doc, A)
        sq = sp.sqrt(disc)
        rho = sp.nsimplify(tr / 2)
        om = sp.simplify(sp.sqrt(-disc) / 2)
        doc.p(f"$\\Delta < 0$: a complex-conjugate pair. $\\lambda = \\dfrac{{{tex(tr)} \\pm \\sqrt{{{tex(disc)}}}}}{{2}} = \\dfrac{{{tex(tr)} \\pm {tex(sq)}}}{{2}}$, so")
        doc.m(f"\\lambda_\\pm = {tex(rho)} \\pm {tex(om)}\\,i \\qquad (\\rho = {tex(rho)},\\ \\omega = {tex(om)} > 0)")
        L = rho + sp.I * om
        doc.h(4, "Eigenvector of the eigenvalue with positive imaginary part")
        doc.p(f"For $\\lambda = \\rho + i\\omega = {tex(L)}$ the first row of $(A - \\lambda I)\\mathbf v = \\mathbf 0$ reads $({tex(sp.expand(a - L))})\\,v_1 + {par(b)}\\,v_2 = 0$ (the coefficient of $v_2$ is non-zero because $\\Delta < 0$ forces $bc < 0$). Choose $v_1 = {tex(b)}$; then $v_2 = -({tex(sp.expand(a - L))}) = {tex(sp.expand(L - a))}$:")
        v = sp.Matrix([b, sp.expand(L - a)])
        u = sp.Matrix([b, sp.re(sp.expand(L - a))])
        w = sp.Matrix([0, sp.im(sp.expand(L - a))])
        doc.m(f"\\mathbf v = {vec(v[0], v[1])} = \\underbrace{{{vec(u[0], u[1])}}}_{{\\mathbf u}} + i\\,\\underbrace{{{vec(w[0], w[1])}}}_{{\\mathbf w}}")
        row2 = sp.simplify(sp.expand(c * v[0] + (d - L) * v[1]))
        assert row2 == 0, row2
        doc.p(f"Check with the second row: ${tex(c)}\\cdot{par(v[0])} + ({tex(sp.expand(d - L))})({tex(v[1])}) = {tex(sp.expand(c * v[0]))} + {par(sp.expand((d - L) * v[1]))} = 0$ (using $i^2 = -1$).")
    else:
        rho, om, u, w = given
        u, w = sp.Matrix(u), sp.Matrix(w)
    # relations (7.4)
    doc.h(4, "How $A$ acts on $\\mathbf u$ and $\\mathbf w$")
    Au, Aw = A * u, A * w
    doc.p("Separating the real and imaginary parts of $A\\mathbf v = \\lambda\\mathbf v$ gives (Topic 4, Eq. 7.4) $A\\mathbf u = \\rho\\mathbf u - \\omega\\mathbf w$ and $A\\mathbf w = \\omega\\mathbf u + \\rho\\mathbf w$. Verification with the numbers:")
    doc.m(f"A\\mathbf u = {vec(Au[0], Au[1])}, \\qquad \\rho\\mathbf u - \\omega\\mathbf w = {par(rho)}{vec(u[0], u[1])} - {par(om)}{vec(w[0], w[1])} = {vec(*(rho * u - om * w))}")
    doc.m(f"A\\mathbf w = {vec(Aw[0], Aw[1])}, \\qquad \\omega\\mathbf u + \\rho\\mathbf w = {par(om)}{vec(u[0], u[1])} + {par(rho)}{vec(w[0], w[1])} = {vec(*(om * u + rho * w))}")
    assert sp.simplify(Au - (rho * u - om * w)) == sp.zeros(2, 1) and sp.simplify(Aw - (om * u + rho * w)) == sp.zeros(2, 1)
    doc.h(4, "Change of coordinates")
    Q = sp.Matrix.hstack(u, w)
    J = sp.Matrix([[rho, om], [-om, rho]])
    doc.p("$\\mathbf u$ and $\\mathbf w$ are linearly independent (they are not parallel when $\\omega \\neq 0$; Topic 4, Lemma of Sec. 7.3). With the columns in the order $\\mathbf u, \\mathbf w$,")
    doc.m(f"Q = [\\mathbf u \\mid \\mathbf w] = {M(Q)}")
    Qi, detQ = inverse_steps(doc, Q)
    doc.p("Compute $AQ = [A\\mathbf u \\mid A\\mathbf w]$ and multiply by $Q^{-1}$ on the left, entry by entry:")
    AQ = sp.Matrix.hstack(Au, Aw)
    doc.m(f"AQ = {M(AQ)}")
    prod = matmul_steps(doc, Qi, AQ, "Q^{-1}", "(AQ)", "Q^{-1}AQ")
    assert sp.simplify(prod - J) == sp.zeros(2, 2), (prod, J)
    doc.m(f"Q^{{-1}}AQ = {M(prod)} = J = \\begin{{pmatrix}} \\rho & \\omega \\\\ -\\omega & \\rho \\end{{pmatrix}}")
    doc.h(4, "Solution in the canonical plane")
    doc.m(f"\\dot z_1 = {lin(rho, 'z_1', om, 'z_2')}, \\qquad \\dot z_2 = {lin(-om, 'z_1', rho, 'z_2')}")
    doc.p("The two equations are coupled, but they say \"scale and rotate\", which polar coordinates express directly: $z_1 = r\\cos\\theta$, $z_2 = r\\sin\\theta$ (Topic 4, Sec. 7.5).")
    doc.p("**The radius.** From $r^2 = z_1^2 + z_2^2$ the chain rule gives $2r\\dot r = 2z_1\\dot z_1 + 2z_2\\dot z_2$. Substituting $\\dot z_1 = \\rho z_1 + \\omega z_2$ and $\\dot z_2 = -\\omega z_1 + \\rho z_2$:")
    doc.m(r"r\dot r = z_1(\rho z_1 + \omega z_2) + z_2(-\omega z_1 + \rho z_2) = \rho z_1^2 + \omega z_1z_2 - \omega z_1z_2 + \rho z_2^2 = \rho r^2")
    doc.p("The terms in $\\omega$ cancel. Dividing by $r \\neq 0$ (the origin is the equilibrium): $\\dot r = \\rho r$.")
    doc.p("**The angle.** Differentiate $\\tan\\theta = z_2/z_1$ with the chain rule on the left and the quotient rule on the right: $\\sec^2\\theta\\,\\dot\\theta = (z_1\\dot z_2 - z_2\\dot z_1)/z_1^2$. Since $\\sec^2\\theta = r^2/z_1^2$, $\\dot\\theta = (z_1\\dot z_2 - z_2\\dot z_1)/r^2$, and")
    doc.m(r"z_1\dot z_2 - z_2\dot z_1 = z_1(-\omega z_1 + \rho z_2) - z_2(\rho z_1 + \omega z_2) = -\omega z_1^2 + \rho z_1z_2 - \rho z_1z_2 - \omega z_2^2 = -\omega r^2 \;\Longrightarrow\; \dot\theta = -\omega")
    doc.p("**Integration.** $\\frac{d}{dt}\\left(e^{-\\rho t}r\\right) = e^{-\\rho t}(\\dot r - \\rho r) = 0$, and Barrow's rule between $0$ and $t$, $\\left[e^{-\\rho s}r(s)\\right]_{0}^{t} = 0$, gives $r(t) = r_0e^{\\rho t}$. For the angle, $\\theta(t) - \\theta_0 = \\int_0^t(-\\omega)\\,ds = -\\omega t$. Back to Cartesian coordinates, with $c_1 = r_0\\cos\\theta_0 = z_1(0)$, $c_2 = r_0\\sin\\theta_0 = z_2(0)$ and the subtraction formulas $\\cos(\\theta_0 - \\omega t) = \\cos\\theta_0\\cos\\omega t + \\sin\\theta_0\\sin\\omega t$, $\\sin(\\theta_0 - \\omega t) = \\sin\\theta_0\\cos\\omega t - \\cos\\theta_0\\sin\\omega t$:")
    doc.m(f"z_1(t) = e^{{{tex(rho)}t}}\\left(c_1\\cos {tex(om)}t + c_2\\sin {tex(om)}t\\right), \\qquad z_2(t) = e^{{{tex(rho)}t}}\\left(c_2\\cos {tex(om)}t - c_1\\sin {tex(om)}t\\right)")
    c1s, c2s = sp.symbols("c_1 c_2")
    z1 = sp.exp(rho * t) * (c1s * sp.cos(om * t) + c2s * sp.sin(om * t))
    z2 = sp.exp(rho * t) * (c2s * sp.cos(om * t) - c1s * sp.sin(om * t))
    assert sp.simplify(sp.diff(z1, t) - (rho * z1 + om * z2)) == 0 and sp.simplify(sp.diff(z2, t) - (-om * z1 + rho * z2)) == 0
    doc.p("Check by substitution (product rule and chain rule): $\\dot z_1 = \\rho z_1 + e^{\\rho t}\\omega\\left(-c_1\\sin\\omega t + c_2\\cos\\omega t\\right) = \\rho z_1 + \\omega z_2$ and $\\dot z_2 = \\rho z_2 + e^{\\rho t}\\omega\\left(-c_2\\sin\\omega t - c_1\\cos\\omega t\\right) = \\rho z_2 - \\omega z_1$, as required.")
    doc.h(4, "Back to the original coordinates")
    doc.p("$\\mathbf x = Q\\mathbf z = z_1\\mathbf u + z_2\\mathbf w$, so")
    x1 = sp.expand(z1 * u[0] + z2 * w[0])
    x2 = sp.expand(z1 * u[1] + z2 * w[1])
    doc.m(f"\\mathbf x(t) = e^{{{tex(rho)}t}}\\left[\\left(c_1\\cos {tex(om)}t + c_2\\sin {tex(om)}t\\right){vec(u[0], u[1])} + \\left(c_2\\cos {tex(om)}t - c_1\\sin {tex(om)}t\\right){vec(w[0], w[1])}\\right]")
    doc.m(f"x(t) = {tex(x1)}, \\qquad y(t) = {tex(x2)}")
    out = dict(Q=Q, Qi=Qi, J=J, rho=rho, om=om, u=u, w=w, A=A, kind="complex", sol=(x1, x2), detQ=detQ)
    if x0 is not None:
        cc = Qi * sp.Matrix(x0)
        doc.p(f"At $t = 0$: $\\mathbf z(0) = Q^{{-1}}\\mathbf x(0) = {M(Qi)}{vec(*x0)} = {vec(cc[0], cc[1])}$, so $c_1 = {tex(cc[0])}$, $c_2 = {tex(cc[1])}$.")
        sub = {c1s: cc[0], c2s: cc[1]}
        out["final"] = (sp.expand(x1.subs(sub)), sp.expand(x2.subs(sub)))
        doc.m(f"x(t) = {tex(out['final'][0])}, \\qquad y(t) = {tex(out['final'][1])}")
    return out


# --------------------------------------------------------------------------- repeated eigenvalue
def repeated(doc, A, tag, x0=None, given=None):
    """Repeated real eigenvalue: star (A = lambda I) or improper node with the Jordan chain."""
    a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
    lam_s = sp.Symbol("lambda")
    expanded, tr, det, disc, roots = charpoly_steps(doc, A)
    lam = sp.nsimplify(tr / 2)
    assert disc == 0, disc
    shifted = "\\lambda - " + par(lam) if lam >= 0 else "\\lambda + " + tex(-lam)
    doc.p(f"$\\Delta = 0$: the characteristic polynomial is a perfect square, $({shifted})^2 = {tex(sp.expand((lam_s - lam) ** 2))}$, so")
    doc.m(f"\\lambda_1 = \\lambda_2 = \\lambda = \\tfrac12\\operatorname{{tr}}A = {tex(lam)} \\quad (m_a = 2)")
    N = A - lam * I2
    doc.p(f"Geometric multiplicity: $N = A - \\lambda I = {M(N)}$.")
    if N == sp.zeros(2, 2):
        doc.p("$N = O$: every vector is an eigenvector ($m_g = 2$) and $A = \\lambda I$ (Topic 4, Sec. 8.3). The system is already uncoupled in every basis.")
        doc.m(f"\\dot x = {par(lam)}x, \\qquad \\dot y = {par(lam)}y")
        doc.p(f"Each equation is separable, $\\frac{{d}}{{dt}}(e^{{-\\lambda t}}x_i) = 0$, so $x_i = c_i e^{{{tex(lam)}t}}$ and")
        doc.m(f"\\mathbf x(t) = e^{{{tex(lam)}t}}\\mathbf x_0 = c_1 e^{{{tex(lam)}t}}{vec(1, 0)} + c_2 e^{{{tex(lam)}t}}{vec(0, 1)}")
        x1, x2 = sp.Symbol("c_1") * sp.exp(lam * t), sp.Symbol("c_2") * sp.exp(lam * t)
        out = dict(A=A, kind="star", lam=lam, sol=(x1, x2), Q=I2, J=A, Qi=I2)
        if x0 is not None:
            out["final"] = (x0[0] * sp.exp(lam * t), x0[1] * sp.exp(lam * t))
        return out
    doc.p(f"$N \\neq O$ and $\\det N = ({tex(N[0, 0])})({tex(N[1, 1])}) - ({tex(N[0, 1])})({tex(N[1, 0])}) = 0$, so $N$ has rank 1: $m_g = 1$ and there is a single eigendirection (improper node). By Cayley-Hamilton $N^2 = O$ (Topic 4, Sec. 8.4):")
    N2 = N * N
    matmul_steps(doc, N, N, "N", "N", "N^2")
    assert N2 == sp.zeros(2, 2)
    doc.h(4, "Eigenvector")
    v1 = kernel_steps(doc, A, lam, "v_1")
    doc.h(4, "Generalised eigenvector")
    doc.p("Solve $(A - \\lambda I)\\mathbf v_2 = \\mathbf v_1$, i.e. $N\\mathbf v_2 = \\mathbf v_1$ (Eq. 8.2). The system is solvable because $\\operatorname{im}N = \\ker N$ (Sec. 8.4):")
    doc.m(f"{M(N)}\\begin{{pmatrix}} p \\\\ q \\end{{pmatrix}} = {vec(v1[0], v1[1])}")
    rows = [(N[0, 0], N[0, 1], v1[0]), (N[1, 0], N[1, 1], v1[1])]
    doc.m(r"\begin{aligned} " + r" \\ ".join(f"{tex(r[0])}p {'+' if r[1] >= 0 else '-'} {tex(abs(r[1]))}q &= {tex(r[2])}" for r in rows) + r" \end{aligned}")
    doc.p("The two equations are proportional (the right-hand sides are in the same ratio as the rows, because $\\mathbf v_1 \\in \\operatorname{im}N$), so one is enough. The solution is not unique: $\\mathbf v_2 + s\\mathbf v_1$ also works for every $s$, because $N\\mathbf v_1 = \\mathbf 0$.")
    use = 0 if rows[0][:2] != (0, 0) else 1
    n1, n2, rhs = rows[use]
    # the two simplest particular solutions: p = 0 or q = 0
    opts = []
    if n2 != 0:
        opts.append(("p", sp.Matrix([0, sp.nsimplify(rhs / n2)])))
    if n1 != 0:
        opts.append(("q", sp.Matrix([sp.nsimplify(rhs / n1), 0])))
    opts.sort(key=lambda o: (sp.ilcm(*[sp.fraction(x)[1] for x in o[1]]), sum(abs(x) for x in o[1])))
    which, v2 = opts[0]
    other = "q" if which == "p" else "p"
    coef = n2 if which == "p" else n1
    doc.p(f"Take ${which} = 0$. Row {use + 1} gives ${tex(coef)}{other} = {tex(rhs)}$, so ${other} = {tex(v2[1] if which == 'p' else v2[0])}$:")
    doc.m(f"\\mathbf v_2 = {vec(v2[0], v2[1])}")
    chk = N * v2
    doc.p(f"Check: $N\\mathbf v_2 = {vec(chk[0], chk[1])} = \\mathbf v_1$, equivalently $A\\mathbf v_2 = \\lambda\\mathbf v_2 + \\mathbf v_1 = {vec(*(lam * v2 + v1))}$ (Eq. 8.2).")
    assert chk == v1
    Q = sp.Matrix.hstack(v1, v2)
    J = sp.Matrix([[lam, 1], [0, lam]])
    doc.h(4, "Change of coordinates")
    doc.m(f"Q = [\\mathbf v_1 \\mid \\mathbf v_2] = {M(Q)}")
    Qi, detQ = inverse_steps(doc, Q)
    r1, r2 = A * v1, A * v2
    doc.m(f"A\\mathbf v_1 = {vec(r1[0], r1[1])} = {par(lam)}\\mathbf v_1, \\qquad A\\mathbf v_2 = {vec(r2[0], r2[1])} = \\mathbf v_1 + {par(lam)}\\mathbf v_2")
    AQ = sp.Matrix.hstack(r1, r2)
    doc.m(f"AQ = {M(AQ)}")
    prod = matmul_steps(doc, Qi, AQ, "Q^{-1}", "(AQ)", "Q^{-1}AQ")
    assert prod == J
    doc.m(f"Q^{{-1}}AQ = {M(prod)} = J = \\begin{{pmatrix}} \\lambda & 1 \\\\ 0 & \\lambda \\end{{pmatrix}}")
    doc.h(4, "Solution in the canonical plane")
    doc.m(f"\\dot z_1 = {lin(lam, 'z_1', 1, 'z_2')}, \\qquad \\dot z_2 = {lin(lam, 'z_2', 0, '')}")
    doc.p(f"Second equation: $\\frac{{d}}{{dt}}(e^{{-\\lambda t}}z_2) = e^{{-\\lambda t}}(\\dot z_2 - \\lambda z_2) = 0$, so $e^{{-\\lambda t}}z_2$ is constant: $z_2 = c_2 e^{{{tex(lam)}t}}$. First equation with this $z_2$: $\\dot z_1 - \\lambda z_1 = c_2 e^{{{tex(lam)}t}}$. The integrating factor is $e^{{-\\lambda t}}$: by the product rule $\\frac{{d}}{{dt}}(e^{{-\\lambda t}}z_1) = e^{{-\\lambda t}}(\\dot z_1 - \\lambda z_1) = c_2$. Barrow's rule between $0$ and $t$:")
    doc.m(f"\\left[e^{{-\\lambda s}}z_1(s)\\right]_{{s=0}}^{{s=t}} = \\int_0^t c_2\\,ds = c_2 t \\;\\Longrightarrow\\; e^{{-\\lambda t}}z_1(t) - z_1(0) = c_2 t")
    doc.m(f"z_1(t) = (c_1 + c_2 t)e^{{{tex(lam)}t}}, \\qquad z_2(t) = c_2 e^{{{tex(lam)}t}} \\qquad (c_1 = z_1(0),\\ c_2 = z_2(0))")
    doc.h(4, "Back to the original coordinates")
    doc.p("$\\mathbf x = Q\\mathbf z = z_1\\mathbf v_1 + z_2\\mathbf v_2$, hence (Topic 4, Eq. 8.5)")
    doc.m(f"\\mathbf x(t) = e^{{{tex(lam)}t}}\\left[c_1{vec(v1[0], v1[1])} + c_2\\left(t{vec(v1[0], v1[1])} + {vec(v2[0], v2[1])}\\right)\\right]")
    c1s, c2s = sp.symbols("c_1 c_2")
    x1 = sp.expand(sp.exp(lam * t) * (c1s * v1[0] + c2s * (t * v1[0] + v2[0])))
    x2 = sp.expand(sp.exp(lam * t) * (c1s * v1[1] + c2s * (t * v1[1] + v2[1])))
    doc.m(f"x(t) = {tex(x1)}, \\qquad y(t) = {tex(x2)}")
    out = dict(Q=Q, Qi=Qi, J=J, lam=lam, v1=v1, v2=v2, A=A, kind="improper", sol=(x1, x2), N=N)
    if x0 is not None:
        cc = Qi * sp.Matrix(x0)
        doc.p(f"At $t = 0$: $\\mathbf z(0) = Q^{{-1}}\\mathbf x(0) = {M(Qi)}{vec(*x0)} = {vec(cc[0], cc[1])}$.")
        sub = {c1s: cc[0], c2s: cc[1]}
        out["final"] = (sp.expand(x1.subs(sub)), sp.expand(x2.subs(sub)))
        doc.m(f"x(t) = {tex(out['final'][0])}, \\qquad y(t) = {tex(out['final'][1])}")
    return out
