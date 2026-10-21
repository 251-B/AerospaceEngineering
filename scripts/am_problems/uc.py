"""Constant-coefficient linear ODEs with forcing, solved by the method of the course with every step written out.

Method (Robinson Ch. 12, 14, 16.1; Topic 3 of the portal):
  1. characteristic polynomial and its roots, complementary function;
  2. guess for the particular integral (multiplied by t^s when the forcing resonates with a root of multiplicity s);
  3. derivatives, substitution, matching of coefficients;
  4. general solution and, when asked, the initial conditions.
"""
import re

import sympy as sp

from .core import tex, solve_steps, t

k = sp.Symbol("k")
PRIME = {0: "", 1: "'", 2: "''"}


# --------------------------------------------------------------------------- forcing pieces
class Piece:
    """c * t**deg * exp(sigma t) * trig(omega t), trig in {None, 'sin', 'cos'}."""

    def __init__(self, c=1, deg=0, sigma=0, omega=0, trig=None, cs=None):
        self.c, self.deg, self.sigma, self.omega, self.trig = sp.sympify(c), deg, sp.sympify(sigma), sp.sympify(omega), trig
        self.cs = cs                    # (cos coefficient, sin coefficient) when trig == "mix"

    @property
    def expr(self):
        e = self.c * t ** self.deg * sp.exp(self.sigma * t)
        if self.trig == "sin":
            e *= sp.sin(self.omega * t)
        elif self.trig == "cos":
            e *= sp.cos(self.omega * t)
        elif self.trig == "mix":
            e *= self.cs[0] * sp.cos(self.omega * t) + self.cs[1] * sp.sin(self.omega * t)
        return e

    @property
    def root(self):
        """The exponent s = sigma + i omega that the forcing 'is' for the resonance test."""
        return self.sigma + (sp.I * self.omega if self.trig else 0)


def Poly(deg, c=1):
    return Piece(c=c, deg=deg)


def Exp(kappa, c=1):
    return Piece(c=c, sigma=kappa)


def Sin(alpha, c=1, sigma=0):
    return Piece(c=c, sigma=sigma, omega=alpha, trig="sin")


def Cos(alpha, c=1, sigma=0):
    return Piece(c=c, sigma=sigma, omega=alpha, trig="cos")


# --------------------------------------------------------------------------- helpers
def poly_char(coeffs):
    n = len(coeffs) - 1
    return sum(sp.sympify(c) * k ** (n - i) for i, c in enumerate(coeffs))


def lop(coeffs, f):
    n = len(coeffs) - 1
    return sum(sp.sympify(c) * sp.diff(f, t, n - i) for i, c in enumerate(coeffs))


def dname(var, order):
    """x, x', x'', x^{(3)} ..."""
    return var + (PRIME[order] if order < 3 else f"^{{({order})}}")


def ode_tex(coeffs, var="x", rhs=None, dots=True):
    """a_n x^{(n)} + ... + a_0 x (= rhs).  dots=True uses Newton's dots up to the second derivative."""
    n = len(coeffs) - 1
    parts = []
    for i, c in enumerate(coeffs):
        c = sp.sympify(c)
        if c == 0:
            continue
        order = n - i
        if dots and order <= 2:
            d = {0: var, 1: f"\\dot{{{var}}}", 2: f"\\ddot{{{var}}}"}[order]
        elif dots and order == 3:
            d = f"\\dddot{{{var}}}"
        else:
            d = dname(var, order)
        neg = c.could_extract_minus_sign()
        mag = -c if neg else c
        term = ("" if mag == 1 else tex(mag)) + d
        parts.append(("-" if neg else "") + term if not parts else (" - " if neg else " + ") + term)
    s = "".join(parts)
    return s if rhs is None else s + " = " + tex(rhs)


def root_table(coeffs):
    P = poly_char(coeffs)
    return P, sp.roots(sp.Poly(P, k))


def complementary(rts, cs):
    """Basis functions of the complementary function and the general expression with constants cs."""
    basis = []
    for r, m in sorted(rts.items(), key=lambda kv: (sp.re(kv[0]), sp.im(kv[0]))):
        if sp.im(r) == 0:
            for j in range(m):
                basis.append(("real", r, j, t ** j * sp.exp(r * t)))
        elif sp.im(r) > 0:
            rho, om = sp.re(r), sp.im(r)
            for j in range(m):
                basis.append(("cos", r, j, t ** j * sp.exp(rho * t) * sp.cos(om * t)))
                basis.append(("sin", r, j, t ** j * sp.exp(rho * t) * sp.sin(om * t)))
    return basis, sum(c * b[3] for c, b in zip(cs, basis))


def mult_of(rts, s):
    for r, m in rts.items():
        if sp.simplify(r - s) == 0:
            return m
    return 0


def guess_for(piece, s_mult, ks):
    """The guess for a particular integral: (expression, unknowns used, basis functions)."""
    basis = []
    for j in range(piece.deg + 1):
        if piece.trig:
            basis.append(t ** (j + s_mult) * sp.exp(piece.sigma * t) * sp.cos(piece.omega * t))
            basis.append(t ** (j + s_mult) * sp.exp(piece.sigma * t) * sp.sin(piece.omega * t))
        else:
            basis.append(t ** (j + s_mult) * sp.exp(piece.sigma * t))
    ks = list(ks)[: len(basis)]
    return sum(kk * b for kk, b in zip(ks, basis)), ks, basis


def _gap(om):
    """A thin space before t when the frequency is a symbol (\\alpha t would be an undefined macro)."""
    return "" if sp.sympify(om).is_number else "\\,"


# Display settings used by callers that need another wording (set and restored around a call).
DOTS = True          # Newton dots for derivatives up to order 3 (False: primes, for an independent variable x)
FNAME = "f"          # name of the right-hand side in the sentences ("F" for the eliminated equation of a system)


def label_of(mon, piece):
    """Label of a monomial (i, jc, js) of Poly in (t, cos, sin), with the exponential factor of the piece."""
    i, jc, js = mon
    parts = []
    if i:
        parts.append("t" if i == 1 else f"t^{{{i}}}")
    if piece.sigma != 0:
        parts.append(tex(sp.exp(piece.sigma * t)))
    if jc:
        parts.append(rf"\cos {tex(piece.omega)}{_gap(piece.omega)}t" if piece.omega != 1 else r"\cos t")
    if js:
        parts.append(rf"\sin {tex(piece.omega)}{_gap(piece.omega)}t" if piece.omega != 1 else r"\sin t")
    return " ".join(parts) if parts else "1"


def split_basis(expr, piece):
    """Coefficients of expr on the monomials t^i cos^j sin^l (times e^{sigma t}) as a dict."""
    Cc, Ss = sp.symbols("Cc Ss")
    e = sp.expand(sp.expand(expr) * sp.exp(-piece.sigma * t))
    e = sp.expand(sp.powsimp(e))
    if piece.trig:
        e = e.subs({sp.cos(piece.omega * t): Cc, sp.sin(piece.omega * t): Ss})
    P = sp.Poly(sp.expand(e), t, Cc, Ss, domain="EX")
    return {mon: c for mon, c in P.terms()}


def coeff_tex(c):
    c = sp.expand(c)
    if len(sp.Add.make_args(c)) > 1:
        return f"\\left({tex(c)}\\right)"
    return "" if c == 1 else ("-" if c == -1 else tex(c))


def lop_tex(coeffs, name):
    """L[x_p] written out: x_p'' + 2x_p' + 10x_p."""
    n = len(coeffs) - 1
    parts = []
    for i, c in enumerate(coeffs):
        c = sp.sympify(c)
        if c == 0:
            continue
        d = dname(name, n - i)
        neg = c.could_extract_minus_sign()
        mag = -c if neg else c
        term = ("" if mag == 1 else tex(mag)) + d
        parts.append(("-" if neg else "") + term if not parts else (" - " if neg else " + ") + term)
    return "".join(parts)


# --------------------------------------------------------------------------- the particular integral, step by step
def particular(doc, coeffs, piece, rts, var="x", subhead=None, ks=None):
    """Write the undetermined-coefficients computation for one forcing piece; return x_p (SymPy)."""
    n = len(coeffs) - 1
    P = poly_char(coeffs)
    f = piece.expr
    s = piece.root
    m = mult_of(rts, s)
    if subhead:
        doc.h(4, subhead)
    if piece.trig:
        kind_txt = "sinusoidal term" + (" times an exponential" if piece.sigma != 0 else "")
    elif piece.deg and piece.sigma == 0:
        kind_txt = f"polynomial of degree {piece.deg}"
    else:
        kind_txt = "exponential"
    ps = sp.simplify(P.subs(k, s))
    if piece.trig:
        doc.p(f"The forcing ${tex(f)}$ is a {kind_txt}: it is the real or imaginary part of $e^{{({tex(s)})t}}$, so we test $s = {tex(s)}$ in the characteristic polynomial: $P({tex(s)}) = {tex(ps)}$.")
    elif piece.deg and piece.sigma == 0:
        doc.p(f"The forcing ${tex(f)}$ is a {kind_txt}; a polynomial is $e^{{0t}}$ times a polynomial, so the exponent to test is $s = 0$: $P(0) = {tex(ps)}$.")
    else:
        doc.p(f"The forcing ${tex(f)}$ is an exponential with exponent $s = {tex(s)}$; we test it in the characteristic polynomial: $P({tex(s)}) = {tex(ps)}$.")
    if m == 0:
        doc.p("Since $P(s) \\neq 0$, no term of the standard guess solves the homogeneous equation, so the standard guess is used as it stands.")
    else:
        doc.p(f"Since $P(s) = 0$ and $s$ is a root of multiplicity ${m}$, the standard guess would contain terms of the complementary function. By the rule of thumb (Robinson Sec. 14.5, p. 139) the guess is multiplied by $t^{{{m}}}$.")
    ks = ks or sp.symbols("K_1:12")
    guess, ksu, basis = guess_for(piece, m, ks)
    doc.p("Guess for the particular integral, with undetermined coefficients:")
    doc.m(f"{var}_p(t) = {tex(guess)}")
    derivs = [guess] + [sp.diff(guess, t, j) for j in range(1, n + 1)]
    doc.p("Differentiate term by term (product rule on $t^j e^{\\sigma t}$, chain rule on $\\cos\\omega t$ and $\\sin\\omega t$):")
    doc.m(r"\begin{aligned} " + r" \\ ".join(f"{dname(var + '_p', j)}(t) &= {tex(sp.expand(derivs[j]))}" for j in range(1, n + 1)) + r" \end{aligned}")
    Lxp = sp.expand(lop(coeffs, guess))
    doc.p(f"Substitute into $L[{var}_p] = {lop_tex(coeffs, var + '_p')}$ and collect the terms that multiply the same function:")
    coll = split_basis(Lxp, piece)
    order = lambda mm: (mm[0], mm[1], mm[2])
    terms = []
    for mon in sorted(coll, key=order, reverse=True):
        lab = label_of(mon, piece)
        c = coeff_tex(coll[mon])
        sep = "\\," if (c and c != "-" and lab != "1") else ""
        terms.append(f"{c}{sep}{lab}" if lab != "1" else (c or "1"))
    doc.m(f"L[{var}_p] = " + re.sub(r"\+\s*-\s*", "- ", " + ".join(terms)))
    rhs = split_basis(f, piece)
    doc.p(f"This must equal the forcing ${FNAME}(t) = {tex(f)}$ for every $t$. The functions on the left are linearly independent, so the coefficient of each must match the coefficient of the same function in ${FNAME}$:")
    eqs, lines = [], []
    for mon in sorted(set(coll) | set(rhs), key=order, reverse=True):
        lhs_c, rhs_c = sp.expand(coll.get(mon, 0)), sp.expand(rhs.get(mon, 0))
        eqs.append(sp.Eq(lhs_c, rhs_c))
        lines.append(f"{label_of(mon, piece)}: &\\quad {tex(lhs_c)} = {tex(rhs_c)}")
    doc.m(r"\begin{aligned} " + r" \\ ".join(lines) + r" \end{aligned}")
    sol = solve_steps(doc, eqs, ksu)
    xp = sp.expand(guess.subs(sol))
    doc.p("Therefore")
    doc.m(f"{var}_p(t) = {tex(xp)}")
    assert sp.simplify(lop(coeffs, xp) - f) == 0, (coeffs, piece.expr, xp)
    return xp


# --------------------------------------------------------------------------- complete solution
def complementary_steps(doc, coeffs, var="x", cs=None):
    """Characteristic equation, roots and complementary function; returns (rts, expr, basis, cs)."""
    n = len(coeffs) - 1
    P, rts = root_table(coeffs)
    cs = cs or sp.symbols("c_1:%d" % (n + 1))
    doc.p(f"The homogeneous equation ${ode_tex(coeffs, var, 0, dots=DOTS)}$ has constant coefficients, so we try ${var} = e^{{kt}}$ (Robinson Sec. 12.1 and 16.1): by the chain rule each derivative multiplies by $k$, and dividing by $e^{{kt}} \\neq 0$ leaves the characteristic equation")
    doc.m(f"P(k) = {tex(P)} = 0")
    if n == 2:
        a, b, c = [sp.sympify(x) for x in coeffs]
        doc.p(f"Its discriminant is $\\Delta = b^2 - 4ac = ({tex(b)})^2 - 4({tex(a)})({tex(c)}) = {tex(sp.simplify(b ** 2 - 4 * a * c))}$.")
    fac = sp.factor(P, extension=[sp.I])
    doc.p(f"Factorising, $P(k) = {tex(fac)}$, so the roots are")
    items = sorted(rts.items(), key=lambda kv: (sp.re(kv[0]), sp.im(kv[0])))
    doc.m(r", \qquad ".join(f"k = {tex(r)}" + (f" \\ \\text{{(multiplicity {m})}}" if m > 1 else "") for r, m in items))
    basis, expr = complementary(rts, cs)
    doc.p("A real root $k$ of multiplicity $m$ gives $t^j e^{kt}$ for $j = 0, \\dots, m - 1$; a complex pair $\\rho \\pm i\\omega$ gives $t^j e^{\\rho t}\\cos\\omega t$ and $t^j e^{\\rho t}\\sin\\omega t$ (Euler's formula, Robinson Sec. 12.3). The fundamental set is " + ", ".join(f"${tex(b[3])}$" for b in basis) + ", so the complementary function is")
    doc.m(f"{var}_h(t) = {tex(expr)}")
    return rts, expr, basis, cs


def solve_ivp(doc, coeffs, pieces, ics, var="x"):
    """General solution of L[x] = sum(pieces) and, if ics is not None, the solution of x^{(j)}(0) = ics[j].

    Returns (general, particular_solution_or_None, xp)."""
    n = len(coeffs) - 1
    rts, xh, basis, cs = complementary_steps(doc, coeffs, var)
    xp_total = 0
    if len(pieces) > 1:
        doc.p("The forcing is a sum of terms. By linearity (Robinson Eq. 14.7) a particular integral is the sum of particular integrals of the separate terms, each found in turn.")
    for pc in pieces:
        head = f"Particular integral for the term ${tex(pc.expr)}$" if len(pieces) > 1 else None
        xp_total += particular(doc, coeffs, pc, rts, var, subhead=head)
    if len(pieces) > 1:
        doc.p("Adding the particular integrals,")
        doc.m(f"{var}_p(t) = {tex(sp.expand(xp_total))}")
    general = xh + xp_total
    if pieces:
        doc.p("The general solution is the complementary function plus the particular integral:")
        doc.m(f"{var}(t) = {var}_h(t) + {var}_p(t) = {tex(general)}")
    else:
        doc.p("The equation is homogeneous, so there is no particular integral and the general solution is the complementary function:")
        doc.m(f"{var}(t) = {var}_h(t) = {tex(general)}")
    if ics is None:
        return general, None, xp_total
    ders = [general] + [sp.diff(general, t, j) for j in range(1, n)]
    doc.p("Initial conditions. Differentiate the general solution (product and chain rules):")
    doc.m(r"\begin{aligned} " + r" \\ ".join(f"{dname(var, j)}(t) &= {tex(sp.expand(ders[j]))}" for j in range(1, n)) + r" \end{aligned}")
    doc.p("Evaluate at $t = 0$, using $e^{0} = 1$, $\\cos 0 = 1$ and $\\sin 0 = 0$:")
    eqs, lines = [], []
    for j, (d, val) in enumerate(zip(ders, ics)):
        at0 = sp.expand(d.subs(t, 0))
        eqs.append(sp.Eq(at0, sp.sympify(val)))
        lines.append(f"{dname(var, j)}(0) &= {tex(at0)} = {tex(sp.sympify(val))}")
    doc.m(r"\begin{aligned} " + r" \\ ".join(lines) + r" \end{aligned}")
    sol = solve_steps(doc, eqs, cs)
    final = sp.expand(general.subs(sol))
    doc.p("Substituting the constants into the general solution,")
    doc.m(f"\\boxed{{{var}(t) = {tex(final)}}}")
    for j, val in enumerate(ics):
        assert sp.simplify(sp.diff(final, t, j).subs(t, 0) - sp.sympify(val)) == 0, (coeffs, ics, final)
    assert sp.simplify(lop(coeffs, final) - sum(p.expr for p in pieces)) == 0, (coeffs, final)
    return general, final, xp_total
