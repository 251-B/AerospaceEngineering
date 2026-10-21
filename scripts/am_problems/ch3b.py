"""Chapter 3, part 2 (probls_ch3-ii_2627.pdf): nine exercises on inhomogeneous equations, resonance and variation of constants."""
import sympy as sp

from . import uc
from .core import Doc, Note, register_figure, rename_ivar, tex, solve_steps, t

SHEET = dict(code="Ch3-II", label="3.II", id_prefix="e",
             tema="Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients",
             index_note="Problem Set - Chapter 3 Part 2",
             theory_note="Topic 3 - Second-Order Linear ODEs General Theory and Constant Coefficients")
SOURCE = "probls_ch3-ii_2627.pdf"
w, al, lam, amp = sp.symbols("omega alpha lambda a", positive=True)
K = sp.symbols("K_1:6")
CLAIMS = []          # structured claims for scripts/verify_topic3_topic4.py


def claim_ode(tag, coeffs, rhs, ics, solution, ivar=t):
    CLAIMS.append(dict(kind="ode", id=tag, coeffs=coeffs, rhs=rhs, ics=ics, solution=solution, ivar=ivar))


def ode_line(coeffs, rhs, var="x", dots=True):
    return uc.ode_tex(coeffs, var, rhs, dots=dots)


# =============================================================================================== Exercise 1
EX1 = [
    ("i", [1, 0, -4], [uc.Poly(2)], t ** 2),
    ("ii", [1, -4, 0], [uc.Poly(2)], t ** 2),
    ("iii", [1, 1, -2], [uc.Exp(-1, 3)], 3 * sp.exp(-t)),
    ("iv", [1, 1, -2], [uc.Exp(1)], sp.exp(t)),
    ("v", [1, 2, 1], [uc.Exp(-1)], sp.exp(-t)),
    ("vi", [1, 0, w ** 2], [uc.Sin(al)], sp.sin(al * t)),
    ("vii", [1, 0, w ** 2], [uc.Sin(w)], sp.sin(w * t)),
    ("viii", [1, 2, 10], [uc.Exp(-1)], sp.exp(-t)),
    ("ix", [1, 2, 10], [uc.Cos(3, sigma=-1)], sp.exp(-t) * sp.cos(3 * t)),
    ("x", [1, 6, 10], [uc.Cos(1, sigma=-3)], sp.exp(-3 * t) * sp.cos(t)),
    ("xi", [1, 4, 4], [uc.Exp(2)], sp.exp(2 * t)),
]
EX1_TAIL = {
    "i": "all terms of the complementary function except the growing one are small: $x \\sim \\tfrac{9}{16}e^{2t}$, unbounded",
    "ii": "the term $\\tfrac{1}{128}e^{4t}$ is tiny at first but eventually dominates the cubic polynomial: unbounded",
    "iii": "$x \\sim \\tfrac52 e^{t}$ (the forcing $3e^{-t}$ and the mode $e^{-2t}$ decay): unbounded",
    "iv": "resonance with the root $k = 1$: $x \\sim (\\tfrac{t}{3} + \\tfrac{23}{9})e^{t}$, faster than a pure exponential",
    "v": "every term carries $e^{-t}$: $x \\to 0$, although the resonant term $\\tfrac12t^2e^{-t}$ first grows (critical damping, resonant forcing)",
    "vi": "bounded for all $t$ (a sum of two sinusoids, periodic exactly when $\\alpha/\\omega$ is rational); no decay; beat-like modulation appears when $\\alpha \\approx \\omega$",
    "vii": "resonance: the amplitude of $-\\dfrac{t\\cos\\omega t}{2\\omega}$ grows linearly without bound",
    "viii": "all terms decay like $e^{-t}$: $x \\to 0$; the non-oscillatory forced part $\\tfrac19e^{-t}$ is not resonant",
    "ix": "resonance with the damped oscillation: the envelope $\\tfrac{t}{6}e^{-t}$ peaks at $t = 1$ (value $\\tfrac{1}{6e} \\approx 0.061$) and then decays; $x \\to 0$",
    "x": "resonance with $e^{-3t}\\cos t$: the envelope $\\tfrac{t}{2}e^{-3t}$ peaks at $t = \\tfrac13$ and decays; $x \\to 0$",
    "xi": "$x \\sim \\tfrac1{16}e^{2t}$: the forced exponential beats the decaying modes $e^{-2t}$, $te^{-2t}$: unbounded",
}


def ex1():
    n = Note(SHEET, 1, "Constant-Coefficient Equations with Forcing (Eleven IVPs)", "Undetermined Coefficients • 11 IVPs • Resonance",
             ["problema-resuelto", "coeficientes-indeterminados", "resonancia", "pvi-segundo-orden", "oscilaciones"], SOURCE)
    st = n.statement
    st.p("Find the general solution of the following differential equations. You will find it useful to look up Exercise 4 of Chapter 3, part 1. For each item $(n)$, find the unique solution such that $x(0) = n$ and $\\dot x(0) = 0$. E.g. for item (iii), $x(0) = 3$, etc.")
    labels = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi"]
    stmt = {
        "i": r"\ddot x - 4x = t^2", "ii": r"\ddot x - 4\dot x = t^2", "iii": r"\ddot x + \dot x - 2x = 3e^{-t}", "iv": r"\ddot x + \dot x - 2x = e^{t}",
        "v": r"\ddot x + 2\dot x + x = e^{-t}", "vi": r"\ddot x + \omega^2 x = \sin(\alpha t)\ \text{ for } \alpha \neq \omega", "vii": r"\ddot x + \omega^2 x = \sin(\alpha t)\ \text{ for } \alpha = \omega",
        "viii": r"\ddot x + 2\dot x + 10x = e^{-t}", "ix": r"\ddot x + 2\dot x + 10x = e^{-t}\cos(3t)", "x": r"\ddot x + 6\dot x + 10x = e^{-3t}\cos t", "xi": r"\ddot x + 4\dot x + 4x = e^{2t}"}
    st.ul([f"({l}) ${stmt[l]}$;" if l != "x" else f"({l}) ${stmt[l]}$," for l in labels])

    p1 = n.phase(1, "Setup, classification and data")
    p1.p("All eleven equations are **linear, second-order, inhomogeneous equations with constant coefficients**, $L[x] = \\ddot x + b\\dot x + cx = f(t)$ (the coefficient of $\\ddot x$ is $1$). The forcing $f$ is built from polynomials, exponentials and sinusoids, so the method of undetermined coefficients applies (Robinson Ch. 14). Hypotheses: for (vi) and (vii) the parameters $\\omega > 0$ and $\\alpha$ are real, with $\\alpha \\neq \\omega$ in (vi) and $\\alpha = \\omega$ in (vii).")
    p1.p("The coefficients are continuous on all of $\\mathbb R$, so for every pair of initial data there is exactly one solution, defined for all $t$ (existence and uniqueness, Robinson Thm 11.1 and Thm 16.1). The data of item $(n)$ are $x(0) = n$, $\\dot x(0) = 0$, with $n$ the position of the item in the list:")
    p1.table(["Item", "Equation $L[x] = f$", "$x(0)$", "$\\dot x(0)$"],
             [[f"({l})", f"${stmt[l]}$", str(k), "0"] for k, l in enumerate(labels, 1)])
    p1.p("Strategy (Robinson Sec. 14.1, Lemma): the general solution of $L[x] = f$ is $x = x_h + x_p$, with $x_h$ the general solution of $L[x] = 0$ (two arbitrary constants $c_1, c_2$) and $x_p$ any one particular solution. The constants are then fixed by the two initial conditions.")

    p2 = n.phase(2, "Method, notation and the guess for each item")
    p2.p("Write $P(k) = k^2 + bk + c$ for the characteristic polynomial. A forcing $c_0\\,t^m e^{\\sigma t}\\{\\cos\\omega t, \\sin\\omega t\\}$ is, for the purpose of the guess, the exponent $s = \\sigma + i\\omega$ (and $s = \\sigma$ when there is no sinusoid; $s = 0$ for a polynomial). Rule of thumb (Robinson Sec. 14.5, p. 139): take the standard guess of the same form as $f$ with undetermined coefficients, and multiply it by $t^{m_s}$ where $m_s$ is the multiplicity of $s$ as a root of $P$ ($m_s = 0$ when $P(s) \\neq 0$).")
    p2.table(["Forcing", "Standard guess $x_p$", "If $s$ is a root of $P$ of multiplicity $m_s$"],
             [["polynomial of degree $m$", "$K_0 + K_1t + \\dots + K_mt^m$", "multiply by $t^{m_s}$"],
              ["$e^{\\sigma t}$", "$Ke^{\\sigma t}$", "$Kt^{m_s}e^{\\sigma t}$"],
              ["$\\sin\\omega t$ or $\\cos\\omega t$", "$K_1\\cos\\omega t + K_2\\sin\\omega t$ (both, always)", "$t^{m_s}(K_1\\cos\\omega t + K_2\\sin\\omega t)$"],
              ["$e^{\\sigma t}\\cos\\omega t$", "$e^{\\sigma t}(K_1\\cos\\omega t + K_2\\sin\\omega t)$", "$t^{m_s}e^{\\sigma t}(K_1\\cos\\omega t + K_2\\sin\\omega t)$"]])
    rows = []
    for (l, coeffs, pieces, rhs), k in zip(EX1, range(1, 12)):
        P, rts = uc.root_table(coeffs)
        pc = pieces[0]
        m = uc.mult_of(rts, pc.root)
        rt = ", ".join(tex(r) + (f"\\ (\\text{{double}})" if mm == 2 else (f"\\ (\\text{{multiplicity }}{mm})" if mm > 2 else "")) for r, mm in sorted(rts.items(), key=lambda kv: (sp.re(kv[0]), sp.im(kv[0]))))
        rows.append([f"({l})", f"${tex(P)}$", f"${rt}$", f"${tex(pc.root)}$", str(m)])
    p2.p("Applying the rule item by item (the roots of $P$ were found in Exercise 4 of part 1 for the homogeneous equations; the last column is $m_s$):")
    p2.table(["Item", "$P(k)$", "Roots of $P$", "Exponent $s$ of $f$", "$m_s$"], rows)
    p2.p("Items with $m_s \\geq 1$ (resonant forcing, marked by a non-zero last column) need the extra factor $t^{m_s}$: (ii), (iv), (v), (vii), (ix), (x).")

    p3 = n.phase(3, "Step-by-step derivation of the eleven solutions")
    finals = {}
    for k, (l, coeffs, pieces, rhs) in enumerate(EX1, 1):
        p3.h(3, f"({l}) ${ode_line(coeffs, rhs)}$, with $x(0) = {k}$, $\\dot x(0) = 0$")
        g, final, xp = uc.solve_ivp(p3, coeffs, pieces, [k, 0])
        finals[l] = (final, xp, g)
        claim_ode(f"3II-E1-{l}", coeffs, rhs, [k, 0], final)
        if l == "vi":
            tidy = 6 * sp.cos(w * t) + (sp.sin(al * t) - al / w * sp.sin(w * t)) / (w ** 2 - al ** 2)
            assert sp.simplify(tidy - final) == 0
            p3.p("Writing the same solution with the denominator $\\omega^2 - \\alpha^2$ that appears naturally in the guess (check: $-\\frac{1}{\\alpha^2 - \\omega^2} = \\frac{1}{\\omega^2 - \\alpha^2}$ and $\\frac{\\alpha}{\\alpha^2\\omega - \\omega^3} = -\\frac{\\alpha}{\\omega(\\omega^2 - \\alpha^2)}$):")
            p3.m(f"\\boxed{{x(t) = 6\\cos\\omega t + \\frac{{\\sin\\alpha t - \\dfrac{{\\alpha}}{{\\omega}}\\sin\\omega t}}{{\\omega^2 - \\alpha^2}}}}")
            p3.p("The first term carries the initial displacement $x(0) = 6$; the fraction vanishes at $t = 0$ and has zero slope there ($\\alpha\\cos 0 - \\alpha\\cos 0 = 0$ after dividing by $\\omega^2 - \\alpha^2$), so the initial conditions hold.")
        if l == "vii":
            p3.p("Check of the resonant solution by the limit $\\alpha \\to \\omega$ of the forced part of item (vi), the fraction, which does not depend on the initial data (L'Hopital's rule, differentiating numerator and denominator with respect to $\\alpha$):")
            p3.m(r"\lim_{\alpha\to\omega}\frac{\sin\alpha t - \frac{\alpha}{\omega}\sin\omega t}{\omega^2 - \alpha^2} = \lim_{\alpha\to\omega}\frac{t\cos\alpha t - \frac{1}{\omega}\sin\omega t}{-2\alpha} = \frac{t\cos\omega t - \frac{1}{\omega}\sin\omega t}{-2\omega} = -\frac{t\cos\omega t}{2\omega} + \frac{\sin\omega t}{2\omega^2}")
            p3.p("which is exactly the zero-data (forced) part of the resonant solution just found, i.e. everything except $7\\cos\\omega t$: the resonant solution is the limit of the non-resonant ones.")

    p4 = n.phase(4, "Interpretation, long-time behaviour and checks")
    p4.p("Summary of the eleven solutions of the IVPs (item $(n)$ has $x(0) = n$, $\\dot x(0) = 0$):")
    rows = []
    for k, (l, coeffs, pieces, rhs) in enumerate(EX1, 1):
        final = finals[l][0]
        if l == "vi":
            fin_tex = r"6\cos\omega t + \dfrac{\sin\alpha t - (\alpha/\omega)\sin\omega t}{\omega^2 - \alpha^2}"
        else:
            fin_tex = tex(final)
        rows.append([f"({l})", f"${fin_tex}$"])
    p4.table(["Item", "Solution $x(t)$"], rows)
    p4.h(4, "Behaviour as $t \\to \\infty$")
    p4.ul([f"({l}): {EX1_TAIL[l]}." for l, *_ in EX1])
    p4.h(4, "Checks")
    p4.ul(["Every solution was substituted back into its equation and into both initial conditions symbolically (script `scripts/verify_topic3_topic4.py`): the residual $L[x] - f$ is identically zero and $x(0) = n$, $\\dot x(0) = 0$.",
           "Dimensions: if $x$ is a length and $t$ a time, every term of $\\ddot x + b\\dot x + cx = f$ has units of length/time$^2$, so $b$ has units s$^{-1}$, $c$ and $\\omega^2$ units s$^{-2}$ and $f$ units m/s$^2$ if the equation is read dimensionally. The sheet itself uses dimensionless variables (forcings such as $t^2$ or $e^{-t}$ carry no units), so these units only serve to check the structure of the formulas. In (vi) the combination $\\alpha/\\omega$ is dimensionless and $1/(\\omega^2 - \\alpha^2)$ has units s$^2$, so $x$ comes out in metres.",
           "Resonance diagnostic: the items with a factor $t$ in the particular integral are exactly those where the exponent of $f$ is a root of $P$ (listed in Phase 2).",
           "Beats versus resonance: as $\\alpha \\to \\omega$, (vi) tends to (vii) (L'Hopital check above); the beat amplitude $\\propto 1/(\\omega^2 - \\alpha^2)$ blows up exactly where the resonant solution replaces it."])
    return n


# =============================================================================================== Exercise 2
def ex2():
    n = Note(SHEET, 2, "A Particular Integral by Superposition", "Superposition • Exponential Forcing",
             ["problema-resuelto", "superposicion", "coeficientes-indeterminados", "resonancia"], SOURCE)
    n.statement.p("Find a particular solution for $\\ddot x + \\dot x - 2x = 12e^{-t} - 6e^{t}$. You may find useful parts (iii) and (iv) of the previous exercise.")
    p1 = n.phase(1, "Setup")
    p1.p("The equation is $L[x] = \\ddot x + \\dot x - 2x = f$ with $f = 12e^{-t} - 6e^{t}$, the same operator $L$ as items (iii) and (iv) of Exercise 1. $L$ is linear (Robinson Eq. 11.11), so if $L[x_a] = f_a$ and $L[x_b] = f_b$ then $L[\\alpha x_a + \\beta x_b] = \\alpha f_a + \\beta f_b$ (Robinson Eq. 14.7). Hypothesis: nothing more is needed, since any single solution of $L[x] = f$ is a particular integral.")
    p2 = n.phase(2, "Formulation")
    p2.p("Rewrite the forcing in terms of the two forcings of Exercise 1:")
    p2.m(r"f = 12e^{-t} - 6e^{t} = 4\,\underbrace{\left(3e^{-t}\right)}_{f_a\ \text{(item iii)}} - 6\,\underbrace{\left(e^{t}\right)}_{f_b\ \text{(item iv)}}")
    p2.p("Item (iii) found $x_a$ with $L[x_a] = 3e^{-t}$ and item (iv) found $x_b$ with $L[x_b] = e^{t}$. Then $x_p = 4x_a - 6x_b$.")
    p3 = n.phase(3, "Derivation")
    p3.h(4, "The two particular integrals of Exercise 1")
    P, rts = uc.root_table([1, 1, -2])
    p3.p(f"$P(k) = k^2 + k - 2 = (k - 1)(k + 2)$ has roots $1$ and $-2$. For $3e^{{-t}}$ the exponent is $s = -1$, $P(-1) = 1 - 1 - 2 = -2 \\neq 0$, so $x_a = K e^{{-t}}$ and, since $\\dot x_a = -Ke^{{-t}}$, $\\ddot x_a = Ke^{{-t}}$: $L[x_a] = (K - K - 2K)e^{{-t}} = -2Ke^{{-t}} = 3e^{{-t}}$, hence $K = -\\tfrac32$:")
    p3.m(r"x_a(t) = -\tfrac32 e^{-t}")
    p3.p("For $e^{t}$ the exponent is $s = 1$, a simple root ($P(1) = 1 + 1 - 2 = 0$), so the guess is $x_b = Kte^{t}$. By the product rule $\\dot x_b = K(1 + t)e^{t}$ and $\\ddot x_b = K(2 + t)e^{t}$, so")
    p3.m(r"L[x_b] = K\left[(2 + t) + (1 + t) - 2t\right]e^{t} = 3Ke^{t} = e^{t} \;\Longrightarrow\; K = \tfrac13,\qquad x_b(t) = \tfrac13\,t\,e^{t}")
    p3.h(4, "Superposition")
    xa, xb = -sp.Rational(3, 2) * sp.exp(-t), t * sp.exp(t) / 3
    xp = sp.expand(4 * xa - 6 * xb)
    p3.m(f"x_p = 4x_a - 6x_b = 4\\left(-\\tfrac32 e^{{-t}}\\right) - 6\\left(\\tfrac13 te^{{t}}\\right) = {tex(xp)}")
    p3.h(4, "Direct verification by substitution")
    d1, d2 = sp.expand(sp.diff(xp, t)), sp.expand(sp.diff(xp, t, 2))
    p3.m(r"\begin{aligned} " + f"\\dot x_p &= {tex(d1)} \\\\ \\ddot x_p &= {tex(d2)}" + r" \end{aligned}")
    lx = sp.expand(d2 + d1 - 2 * xp)
    p3.m(f"\\ddot x_p + \\dot x_p - 2x_p = \\left({tex(d2)}\\right) + \\left({tex(d1)}\\right) - 2\\left({tex(xp)}\\right) = {tex(lx)}")
    assert sp.simplify(lx - (12 * sp.exp(-t) - 6 * sp.exp(t))) == 0
    p3.p("This is $12e^{-t} - 6e^{t}$, as required.")
    p4 = n.phase(4, "Interpretation and checks")
    p4.callout("result", "Result", [f"A particular solution is $x_p(t) = {tex(xp)}$.", "The general solution is $x(t) = c_1e^{t} + c_2e^{-2t} - 6e^{-t} - 2te^{t}$ (the roots $1$ and $-2$ of $P$ give the complementary function)."])
    p4.ul(["The term $-2te^{t}$ carries the extra factor $t$ because $e^{t}$ solves the homogeneous equation (resonance); the term $-6e^{-t}$ does not.",
           "Particular integrals are not unique: adding any multiple of $e^{t}$ or $e^{-2t}$ gives another one; the answer above is the one with no such terms.",
           "Dimensions: with $[t] = $ s, each term of $L[x]$ has the units of $f$; both sides are exponentials of a dimensionless argument $t/(1\\ \\mathrm{s})$, so the check is purely numerical."])
    CLAIMS.append(dict(kind="ode", id="3II-E2", coeffs=[1, 1, -2], rhs=12 * sp.exp(-t) - 6 * sp.exp(t), ics=None, solution=xp, ivar=t))
    return n


# =============================================================================================== Exercise 3
def ex3():
    n = Note(SHEET, 3, "Harmonic Oscillator under Periodic Forcing: Beats and Resonance", "Forced Oscillations • Resonance • Beats",
             ["problema-resuelto", "oscilaciones-forzadas", "resonancia", "pulsaciones"], SOURCE)
    st = n.statement
    st.p("Suppose that $x(t)$ denotes the distance of some system from its equilibrium position, such that it satisfies the differential equation")
    st.m(r"\ddot x + \omega^2 x = a\cos\alpha t,")
    st.p("where the second term on the left hand side accounts for harmonic oscillations and the right hand side is an external forcing that is periodic in time. Discuss the form of the general solution in terms of the natural frequency of oscillation $\\omega$ and the frequency $\\alpha$ of the external force.")
    p1 = n.phase(1, "Setup and classification")
    p1.p("Hypotheses: $\\omega > 0$ is the natural angular frequency (rad/s), $\\alpha \\geq 0$ the forcing frequency and $a$ the forcing amplitude per unit mass (m/s$^2$). The equation is linear, second-order, with constant coefficients and a sinusoidal forcing. Its characteristic polynomial $P(k) = k^2 + \\omega^2$ has the imaginary roots $k = \\pm i\\omega$, so the complementary function is the simple harmonic motion $x_h = c_1\\cos\\omega t + c_2\\sin\\omega t$ (Topic 3, Sec. 4.2).")
    p1.p("The forcing $a\\cos\\alpha t$ has exponent $s = \\pm i\\alpha$. The whole discussion hinges on whether $s$ is a root of $P$, that is, on whether $\\alpha = \\omega$ (**resonance**) or $\\alpha \\neq \\omega$. Both cases are solved below with the method of undetermined coefficients, then compared.")
    p2 = n.phase(2, "Method")
    p2.p("General solution $x = x_h + x_p$ (Robinson Sec. 14.1). For $x_p$ use the guess table of Topic 3, Sec. 5: $K_1\\cos\\alpha t + K_2\\sin\\alpha t$ when $P(i\\alpha) \\neq 0$ and $t(K_1\\cos\\omega t + K_2\\sin\\omega t)$ when $\\alpha = \\omega$.")
    p3 = n.phase(3, "Derivation")
    p3.h(3, "Case A: $\\alpha \\neq \\omega$ (non-resonant forcing)")
    start = len(p3.out)
    g, _, xpA = uc.solve_ivp(p3, [1, 0, w ** 2], [uc.Piece(c=amp, trig="cos", omega=al)], None)
    p3.p("Remarks on this case. The guess contained a sine term, but matching showed $K_2 = 0$: with no $\\dot x$ term in the equation, cosines are only turned into cosines. The general solution is")
    p3.m(r"x(t) = c_1\cos\omega t + c_2\sin\omega t + \frac{a}{\omega^2 - \alpha^2}\cos\alpha t = M\cos(\omega t - \phi) + \frac{a}{\omega^2 - \alpha^2}\cos\alpha t")
    p3.p("(the last form uses the amplitude-phase rewriting $c_1\\cos\\omega t + c_2\\sin\\omega t = M\\cos(\\omega t - \\phi)$ with $M = \\sqrt{c_1^2 + c_2^2}$, Topic 3, Eq. 13.3). The solution is a superposition of two sinusoids with different frequencies, so it is **bounded** for every $t$; it is periodic only if $\\omega/\\alpha$ is rational. The forced amplitude $|a/(\\omega^2 - \\alpha^2)|$ is large when $\\alpha \\approx \\omega$.")
    p3.h(4, "Starting from rest: beats")
    p3.p("With $x(0) = 0$, $\\dot x(0) = 0$: $x(0) = c_1 + \\frac{a}{\\omega^2 - \\alpha^2} = 0$ gives $c_1 = -\\frac{a}{\\omega^2 - \\alpha^2}$, and $\\dot x(0) = \\omega c_2 = 0$ gives $c_2 = 0$ (the forced term $\\propto \\cos\\alpha t$ has zero slope at $0$). Hence")
    p3.m(r"x(t) = \frac{a}{\omega^2 - \alpha^2}\left(\cos\alpha t - \cos\omega t\right)")
    p3.p("Use $\\cos A - \\cos B = -2\\sin\\frac{A + B}{2}\\sin\\frac{A - B}{2}$ with $A = \\alpha t$, $B = \\omega t$, noting that $\\sin\\frac{\\alpha - \\omega}{2}t = -\\sin\\frac{\\omega - \\alpha}{2}t$:")
    p3.m(r"x(t) = \frac{2a}{\omega^2 - \alpha^2}\,\sin\frac{(\omega + \alpha)t}{2}\;\sin\frac{(\omega - \alpha)t}{2}")
    p3.p("This is a fast oscillation at the mean frequency $(\\omega + \\alpha)/2$ whose amplitude is modulated by the slow envelope $\\pm\\frac{2a}{|\\omega^2 - \\alpha^2|}\\sin\\frac{|\\omega - \\alpha|t}{2}$: **beats**. The envelope vanishes every $2\\pi/|\\omega - \\alpha|$ (the beat period; the signed factor $\\sin\\frac{(\\omega - \\alpha)t}{2}$ itself has period $4\\pi/|\\omega - \\alpha|$), long when $\\alpha \\approx \\omega$, and its peak value $\\frac{2a}{|\\omega^2 - \\alpha^2|}$ grows without bound as $\\alpha \\to \\omega$.")
    p3.h(3, "Case B: $\\alpha = \\omega$ (resonance)")
    g2, _, xpB = uc.solve_ivp(p3, [1, 0, w ** 2], [uc.Piece(c=amp, trig="cos", omega=w)], None)
    p3.p("Remarks on this case. Now $s = i\\omega$ is a simple root of $P$, so the guess is multiplied by $t$ and matching gives $K_1 = 0$, $K_2 = \\frac{a}{2\\omega}$:")
    p3.m(r"x(t) = c_1\cos\omega t + c_2\sin\omega t + \frac{a}{2\omega}\,t\sin\omega t")
    p3.p("The last term oscillates at the natural frequency with an amplitude $\\frac{a}{2\\omega}t$ that **grows linearly in time**: the response is unbounded (Robinson Sec. 15.1.2). For zero initial data, $c_1 = c_2 = 0$ (the particular integral and its derivative $\\frac{a}{2\\omega}(\\sin\\omega t + \\omega t\\cos\\omega t)$ vanish at $t = 0$), so $x(t) = \\frac{a}{2\\omega}\\,t\\sin\\omega t$.")
    p3.h(3, "Case C: resonance as the limit of beats")
    p3.p("Let $\\alpha \\to \\omega$ in the beat solution of Case A, which is $0/0$ at $\\alpha = \\omega$. L'Hopital's rule (differentiate numerator and denominator with respect to $\\alpha$, at fixed $t$):")
    p3.m(r"\lim_{\alpha\to\omega}\frac{a(\cos\alpha t - \cos\omega t)}{\omega^2 - \alpha^2} = \lim_{\alpha\to\omega}\frac{-at\sin\alpha t}{-2\alpha} = \frac{a\,t\sin\omega t}{2\omega}")
    p3.p("which is exactly the resonant solution of Case B: the linear growth is the limit of beats whose period and peak both tend to infinity.")
    register_figure("ch3b-e3-beats", dict(kind="series", title="Beats and resonance", caption="Response of $\\ddot x + x = \\cos\\alpha t$ from rest ($\\omega = 1$): beats for $\\alpha = 0.85$ (blue, bounded, envelope dashed) and resonance for $\\alpha = 1$ (pink, amplitude $t/2$).",
                   t1=90, ymax=24, xlabel="t", ylabel="x", curves=[
                       dict(fn="beats", w=1.0, al=0.85, a=1.0, col="BLUE"), dict(fn="beats_env", w=1.0, al=0.85, a=1.0, col="BLUE"),
                       dict(fn="resonance", w=1.0, a=1.0, col="PINK"), dict(fn="resonance_env", w=1.0, a=1.0, col="PINK")]))
    p3.fig("ch3b-e3-beats", "Response of $\\ddot x + x = \\cos\\alpha t$ from rest ($\\omega = 1$): beats for $\\alpha = 0.85$ (blue, bounded, envelope dashed) and resonance for $\\alpha = 1$ (pink, amplitude $t/2$).")
    p4 = n.phase(4, "Interpretation and checks")
    p4.table(["Frequency ratio", "Particular integral", "Behaviour of the general solution"],
             [["$\\alpha \\neq \\omega$", "$\\dfrac{a}{\\omega^2 - \\alpha^2}\\cos\\alpha t$", "bounded superposition of two sinusoids; beats if the data are those of rest; large amplitude near $\\alpha \\approx \\omega$"],
              ["$\\alpha = \\omega$", "$\\dfrac{a}{2\\omega}t\\sin\\omega t$", "amplitude grows linearly: resonance"],
              ["$\\alpha \\to 0$", "$\\dfrac{a}{\\omega^2}$", "static deflection $a/\\omega^2$ under a constant force (Hooke's law)"],
              ["$\\alpha \\to \\infty$", "$\\approx -\\dfrac{a}{\\alpha^2}\\cos\\alpha t$", "response tends to $0$: inertia dominates"]])
    p4.ul(["There is no damping in this model, so the transient $x_h$ never dies: unlike Exercise 4, the steady state is not isolated from the initial data.",
           "Dimensions: $[a] = \\mathrm{m/s^2}$, $[\\omega^2 - \\alpha^2] = \\mathrm{s^{-2}}$, so $[a/(\\omega^2 - \\alpha^2)] = \\mathrm m$ and for the resonant term $[a\\,t/(2\\omega)] = (\\mathrm{m/s^2})(\\mathrm s)/(\\mathrm{s^{-1}}) = \\mathrm m$ (radians are dimensionless).",
           "Engineering reading: a structure with natural frequency $\\omega$ must not be forced at (or near) $\\omega$ for long; real systems have damping, which keeps the amplitude finite (Exercise 4)."])
    CLAIMS.append(dict(kind="ode", id="3II-E3-A", coeffs=[1, 0, w ** 2], rhs=amp * sp.cos(al * t), ics=None, solution=xpA, ivar=t, particular=True))
    CLAIMS.append(dict(kind="ode", id="3II-E3-B", coeffs=[1, 0, w ** 2], rhs=amp * sp.cos(w * t), ics=None, solution=xpB, ivar=t, particular=True))
    return n


# =============================================================================================== Exercise 4
def ex4():
    n = Note(SHEET, 4, "Damped Forced Oscillator: Amplitude and Phase of the Steady State", "Frequency Response • Amplitude M • Phase φ",
             ["problema-resuelto", "oscilaciones-forzadas", "amortiguamiento", "respuesta-en-frecuencia"], SOURCE)
    st = n.statement
    st.p("Consider the oscillating system of the previous exercise, but now in the presence of a non-negligible viscous drag so that Newton's second law reads")
    st.m(r"\ddot x + \lambda\dot x + \omega^2 x = a\cos\alpha t,")
    st.p("in the underdamped case in which $\\lambda^2 < 4\\omega^2$. Show that $x_p(t) = M\\cos(\\alpha t - \\phi)$ is a particular solution, finding its amplitude $M$ and phase $\\phi$ in terms of the system parameters. Discuss how the relative ratio between the system response and the external forcing, $M/a$, behaves with the external frequency $\\alpha$ and compare with the zero-drag ($\\lambda = 0$) case.")
    p1 = n.phase(1, "Setup and hypotheses")
    p1.p("Parameters: $\\lambda > 0$ (damping rate, s$^{-1}$), $\\omega > 0$ (natural frequency), $\\alpha > 0$ (forcing frequency), $a > 0$ (forcing amplitude per unit mass). Underdamped: $\\lambda^2 < 4\\omega^2$, so the characteristic roots are $-\\frac{\\lambda}{2} \\pm i\\sigma$ with $\\sigma = \\frac12\\sqrt{4\\omega^2 - \\lambda^2} > 0$ (Topic 3, Sec. 4.3) and the complementary function is $x_h = e^{-\\lambda t/2}(c_1\\cos\\sigma t + c_2\\sin\\sigma t)$, which decays. Only $x_p$ survives at long times.")
    p2 = n.phase(2, "Formulation: what has to be shown")
    p2.p("We must find constants $M$ and $\\phi$ such that $x_p = M\\cos(\\alpha t - \\phi)$ satisfies $L[x_p] = a\\cos\\alpha t$. Because $\\cos(\\alpha t - \\phi)$ is a shifted cosine, the cosine and sine terms of the guess of Topic 3, Sec. 6.1 are packed in one amplitude and one phase. The subtraction formulas $\\cos(\\alpha t - \\phi) = \\cos\\alpha t\\cos\\phi + \\sin\\alpha t\\sin\\phi$ and $\\sin(\\alpha t - \\phi) = \\sin\\alpha t\\cos\\phi - \\cos\\alpha t\\sin\\phi$ will be used.")
    p3 = n.phase(3, "Derivation")
    p3.h(4, "Substitution")
    p3.p("Differentiate with the chain rule ($\\frac{d}{dt}(\\alpha t - \\phi) = \\alpha$):")
    p3.m(r"\dot x_p = -M\alpha\sin(\alpha t - \phi), \qquad \ddot x_p = -M\alpha^2\cos(\alpha t - \phi)")
    p3.p("Therefore")
    p3.m(r"L[x_p] = \ddot x_p + \lambda\dot x_p + \omega^2x_p = M\left[(\omega^2 - \alpha^2)\cos(\alpha t - \phi) - \lambda\alpha\sin(\alpha t - \phi)\right]")
    p3.p("Expand the shifted functions and collect cosines and sines of $\\alpha t$:")
    p3.m(r"L[x_p] = M\left[(\omega^2 - \alpha^2)\cos\phi + \lambda\alpha\sin\phi\right]\cos\alpha t + M\left[(\omega^2 - \alpha^2)\sin\phi - \lambda\alpha\cos\phi\right]\sin\alpha t")
    p3.p("This must equal $a\\cos\\alpha t + 0\\cdot\\sin\\alpha t$ for every $t$; $\\cos\\alpha t$ and $\\sin\\alpha t$ are linearly independent, so both coefficients must match:")
    p3.m(r"\begin{aligned} M\left[(\omega^2 - \alpha^2)\cos\phi + \lambda\alpha\sin\phi\right] &= a \quad (1) \\ M\left[(\omega^2 - \alpha^2)\sin\phi - \lambda\alpha\cos\phi\right] &= 0 \quad (2) \end{aligned}")
    p3.h(4, "Phase")
    p3.p("$M \\neq 0$, because $M = 0$ would turn equation (1) into $0 = a > 0$. Hence equation (2) gives $(\\omega^2 - \\alpha^2)\\sin\\phi = \\lambda\\alpha\\cos\\phi$, i.e.")
    p3.m(r"\tan\phi = \frac{\lambda\alpha}{\omega^2 - \alpha^2}")
    p3.p("To fix the quadrant, introduce $R = \\sqrt{(\\omega^2 - \\alpha^2)^2 + \\lambda^2\\alpha^2} > 0$ and the angle $\\phi$ defined by")
    p3.m(r"\cos\phi = \frac{\omega^2 - \alpha^2}{R}, \qquad \sin\phi = \frac{\lambda\alpha}{R}")
    p3.p("(these satisfy $\\cos^2\\phi + \\sin^2\\phi = \\frac{(\\omega^2 - \\alpha^2)^2 + \\lambda^2\\alpha^2}{R^2} = 1$ and equation (2): $(\\omega^2 - \\alpha^2)\\frac{\\lambda\\alpha}{R} - \\lambda\\alpha\\frac{\\omega^2 - \\alpha^2}{R} = 0$). Because $\\sin\\phi = \\lambda\\alpha/R > 0$, $\\phi \\in (0, \\pi)$: $\\phi = \\operatorname{arccot}\\frac{\\omega^2 - \\alpha^2}{\\lambda\\alpha}$, i.e. $\\phi = \\arctan\\frac{\\lambda\\alpha}{\\omega^2 - \\alpha^2}$ for $\\alpha < \\omega$ and $\\phi = \\pi + \\arctan\\frac{\\lambda\\alpha}{\\omega^2 - \\alpha^2}$ for $\\alpha > \\omega$.")
    p3.h(4, "Amplitude")
    p3.p("Substitute $\\cos\\phi$ and $\\sin\\phi$ in equation (1):")
    p3.m(r"M\left[(\omega^2 - \alpha^2)\frac{\omega^2 - \alpha^2}{R} + \lambda\alpha\frac{\lambda\alpha}{R}\right] = M\,\frac{(\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2}{R} = M\,R = a")
    p3.m(r"\boxed{M = \frac{a}{\sqrt{(\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2}}, \qquad \phi = \operatorname{atan2}\!\left(\lambda\alpha,\ \omega^2 - \alpha^2\right)}")
    p3.p("so $x_p = M\\cos(\\alpha t - \\phi)$ is indeed a particular solution. It agrees with the sine-cosine form of Topic 3, Eq. 15.5: $M\\cos\\phi = \\frac{a(\\omega^2 - \\alpha^2)}{R^2}$ and $M\\sin\\phi = \\frac{a\\lambda\\alpha}{R^2}$ are exactly the coefficients $D$ and $C$ found there.")
    p3.h(4, "Ratio of response to forcing")
    p3.m(r"\frac{M}{a} = \frac{1}{\sqrt{(\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2}} =: F(\alpha)")
    p3.p("Differentiate the radicand $D(\\alpha) = (\\omega^2 - \\alpha^2)^2 + \\lambda^2\\alpha^2$ with the chain rule: $D'(\\alpha) = -4\\alpha(\\omega^2 - \\alpha^2) + 2\\lambda^2\\alpha = 2\\alpha\\left(2\\alpha^2 - 2\\omega^2 + \\lambda^2\\right)$. The critical points are $\\alpha = 0$ and $\\alpha_r^2 = \\omega^2 - \\frac{\\lambda^2}{2}$, which is real only if $\\lambda^2 < 2\\omega^2$.")
    p3.ul(["**Case $\\lambda^2 < 2\\omega^2$ (light damping).** $D$ has a minimum at $\\alpha_r = \\sqrt{\\omega^2 - \\lambda^2/2} < \\omega$ and $F$ a maximum. There $\\omega^2 - \\alpha_r^2 = \\frac{\\lambda^2}{2}$, so $D(\\alpha_r) = \\frac{\\lambda^4}{4} + \\lambda^2\\left(\\omega^2 - \\frac{\\lambda^2}{2}\\right) = \\lambda^2\\left(\\omega^2 - \\frac{\\lambda^2}{4}\\right)$ and $\\left(\\frac{M}{a}\\right)_{\\max} = \\frac{1}{\\lambda\\sqrt{\\omega^2 - \\lambda^2/4}} = \\frac{1}{\\lambda\\sigma}$: finite, large for small $\\lambda$, and attained slightly below $\\omega$ (pseudo-resonance).",
            "**Case $2\\omega^2 \\leq \\lambda^2 < 4\\omega^2$.** $D'(\\alpha) \\geq 0$ for $\\alpha > 0$: no peak, and $M/a$ decreases monotonically from its value at $\\alpha = 0$.",
            "**Limits.** $\\alpha \\to 0$: $M/a \\to 1/\\omega^2$ (static deflection under a constant force); $\\alpha = \\omega$: $M/a = 1/(\\lambda\\omega)$; $\\alpha \\to \\infty$: $M/a \\approx 1/\\alpha^2 \\to 0$.",
            "**Phase.** $\\phi$ increases continuously from $0$ at $\\alpha = 0$ through $\\pi/2$ at $\\alpha = \\omega$ (there $\\cos\\phi = 0$) to $\\pi$ as $\\alpha \\to \\infty$: the response lags the forcing by a quarter period exactly at the natural frequency."])
    p3.h(4, "Comparison with the undamped case")
    p3.p("For $\\lambda = 0$, $M/a = \\frac{1}{|\\omega^2 - \\alpha^2|}$, which tends to $+\\infty$ as $\\alpha \\to \\omega$ (resonance, Exercise 3), and $\\phi$ jumps discontinuously from $0$ (for $\\alpha < \\omega$) to $\\pi$ (for $\\alpha > \\omega$): the response is in phase below $\\omega$ and in antiphase above. Any $\\lambda > 0$ regularises this: the peak becomes finite, $1/(\\lambda\\sigma)$, and the phase jump is smoothed over a band of width $\\sim\\lambda$ around $\\omega$. As $\\lambda \\to 0$, $\\alpha_r \\to \\omega$ and the peak height $1/(\\lambda\\sigma) \\to \\infty$, recovering resonance.")
    register_figure("ch3b-e4-response", dict(kind="response", title="Frequency response", caption="Amplitude ratio $\\omega^2M/a$ against $\\alpha/\\omega$ for $\\lambda/\\omega = 0.2, 0.5, 1, 1.5$ (blue to pink) and the undamped limit (dashed, $\\lambda = 0$).",
                   lams=[0.2, 0.5, 1.0, 1.5], ymax=5.0))
    p3.fig("ch3b-e4-response", "Amplitude ratio $\\omega^2M/a$ against $\\alpha/\\omega$ for $\\lambda/\\omega = 0.2, 0.5, 1, 1.5$ (blue to pink) and the undamped limit (dashed, $\\lambda = 0$).")
    p4 = n.phase(4, "Interpretation and checks")
    p4.callout("result", "Result", ["$x_p(t) = M\\cos(\\alpha t - \\phi)$ with $M = \\dfrac{a}{\\sqrt{(\\omega^2 - \\alpha^2)^2 + \\lambda^2\\alpha^2}}$ and $\\phi = \\operatorname{atan2}(\\lambda\\alpha, \\omega^2 - \\alpha^2) \\in (0, \\pi)$.",
                                    "The general solution is $x = e^{-\\lambda t/2}(c_1\\cos\\sigma t + c_2\\sin\\sigma t) + M\\cos(\\alpha t - \\phi)$: the transient decays and the steady state at the forcing frequency remains, independent of the initial data."])
    p4.ul(["Numerical check of (1) and (2) at $\\omega = 2$, $\\lambda = 1$, $\\alpha = 1$, $a = 1$: $R = \\sqrt{9 + 1} = \\sqrt{10}$, $M = 1/\\sqrt{10}$, $\\cos\\phi = 3/\\sqrt{10}$, $\\sin\\phi = 1/\\sqrt{10}$, and $M[3\\cos\\phi + 1\\cdot\\sin\\phi] = \\frac{1}{\\sqrt{10}}\\cdot\\frac{9 + 1}{\\sqrt{10}} = 1 = a$ (checked symbolically in `scripts/verify_topic3_topic4.py`).",
           "Dimensions: $[\\omega^2 - \\alpha^2] = [\\lambda\\alpha] = \\mathrm{s^{-2}}$, so $[R] = \\mathrm{s^{-2}}$ and $[M] = [a]/[R] = \\mathrm{m/s^2\\cdot s^2} = \\mathrm m$; $\\phi$ is dimensionless.",
           "Condition $\\lambda^2 < 4\\omega^2$ is only needed for the form of $x_h$; the formulas for $M$ and $\\phi$ hold for every $\\lambda > 0$."])
    Mexp = amp / sp.sqrt((w ** 2 - al ** 2) ** 2 + lam ** 2 * al ** 2)
    phi = sp.atan2(lam * al, w ** 2 - al ** 2)
    xp = Mexp * sp.cos(al * t - phi)
    CLAIMS.append(dict(kind="ode", id="3II-E4", coeffs=[1, lam, w ** 2], rhs=amp * sp.cos(al * t), ics=None, solution=xp, ivar=t, particular=True))
    return n


# =============================================================================================== Exercise 5
def ex5():
    n = Note(SHEET, 5, "Higher-Order Inhomogeneous Equations with Constant Coefficients", "Third and Fourth Order • Repeated Roots • Undetermined Coefficients",
             ["problema-resuelto", "orden-superior", "coeficientes-indeterminados", "raices-repetidas"], SOURCE)
    st = n.statement
    st.p("Working by analogy with the second order case, find the general solution of the following inhomogeneous higher-order linear equations with constant coefficients:")
    st.ul([r"(i) $\dfrac{d^3x}{dt^3} - 6\dfrac{d^2x}{dt^2} + 11\dfrac{dx}{dt} - 6x = e^{-t}$,",
           r"(ii) $y''' - 3y' + 2 = \sin x$,",
           r"(iii) $\dfrac{d^4x}{dt^4} - 4\dfrac{d^3x}{dt^3} + 8\dfrac{d^2x}{dt^2} - 8\dfrac{dx}{dt} + 4x = \sin t$."])
    p1 = n.phase(1, "Setup, classification and a remark on the statement")
    p1.p("All three are linear, constant-coefficient, inhomogeneous equations of order $3$, $3$ and $4$. By the higher-order theory (Robinson Sec. 16.1, Topic 3 Sec. 3 box), the general solution of $a_nx^{(n)} + \\dots + a_0x = f$ is $x = x_h + x_p$, where $x_h$ contains $n$ arbitrary constants (the solution space of the homogeneous equation has dimension $n$) and the method of undetermined coefficients gives $x_p$ exactly as for $n = 2$. Hypotheses: coefficients constant, $f$ continuous.")
    p1.callout("warning", "Remark on the statement of (ii)", [
        "The sheet prints $y''' - 3y' + 2 = \\sin x$. Read literally this is the linear equation $y''' - 3y' = \\sin x - 2$ (the constant $2$ moves to the right-hand side), which is perfectly solvable. The other two items and the form $L[y] = \\dots$ suggest that the term $2y$ may have been intended, but that is only a guess from the pattern of the sheet. We therefore solve **both readings in full**: $y''' - 3y' + 2y = \\sin x$ (the guessed one) and the literal $y''' - 3y' = \\sin x - 2$, each with its own general solution, so that the answer is complete whichever the author meant."])
    p2 = n.phase(2, "Method")
    p2.p("Characteristic polynomial $P(k) = a_nk^n + \\dots + a_0$. A root $k$ of multiplicity $m$ gives $t^je^{kt}$ for $j = 0, \\dots, m - 1$; a complex pair $\\rho \\pm i\\omega$ of multiplicity $m$ gives $t^je^{\\rho t}\\cos\\omega t$ and $t^je^{\\rho t}\\sin\\omega t$ for $j = 0, \\dots, m - 1$ (Topic 3, Sec. 3 box, Robinson Sec. 16.1). The particular integral uses the guess table of Topic 3, Sec. 5, with the factor $t^{m_s}$ when the exponent $s$ of the forcing is a root of $P$ of multiplicity $m_s$. The derivatives needed are now up to order $n$.")
    p3 = n.phase(3, "Derivation")
    p3.h(3, "(i) $x''' - 6x'' + 11x' - 6x = e^{-t}$")
    g1, _, xp1 = uc.solve_ivp(p3, [1, -6, 11, -6], [uc.Exp(-1)], None)
    claim_ode("3II-E5-i", [1, -6, 11, -6], sp.exp(-t), None, xp1)
    CLAIMS[-1]["particular"] = True
    p3.h(3, "(ii) $y''' - 3y' + 2y = \\sin x$ (independent variable $x$)")
    X = sp.Symbol("x", real=True)
    old_t = uc.t
    uc.t = X
    uc.DOTS = False
    start = len(p3.out)
    g2, _, xp2 = uc.solve_ivp(p3, [1, 0, -3, 2], [uc.Sin(1)], None, var="y")
    uc.t = old_t
    uc.DOTS = True
    rename_ivar(p3, start, "x")
    CLAIMS.append(dict(kind="ode", id="3II-E5-ii", coeffs=[1, 0, -3, 2], rhs=sp.sin(X), ics=None, solution=xp2.subs(X, X), ivar=X, particular=True))
    p3.h(4, "Literal reading of the sheet: $y''' - 3y' = \\sin x - 2$")
    uc.t = X
    uc.DOTS = False
    start = len(p3.out)
    g2b, _, xp2b = uc.solve_ivp(p3, [1, 0, -3, 0], [uc.Sin(1), uc.Poly(0, c=-2)], None, var="y")
    uc.t = old_t
    uc.DOTS = True
    rename_ivar(p3, start, "x")
    CLAIMS.append(dict(kind="ode", id="3II-E5-ii-literal", coeffs=[1, 0, -3, 0], rhs=sp.sin(X) - 2, ics=None, solution=xp2b, ivar=X, particular=True))
    p3.h(3, "(iii) $x^{(4)} - 4x''' + 8x'' - 8x' + 4x = \\sin t$")
    g3, _, xp3 = uc.solve_ivp(p3, [1, -4, 8, -8, 4], [uc.Sin(1)], None)
    claim_ode("3II-E5-iii", [1, -4, 8, -8, 4], sp.sin(t), None, xp3)
    CLAIMS[-1]["particular"] = True
    p4 = n.phase(4, "Interpretation and checks")
    p4.table(["Item", "General solution"], [["(i)", f"${tex(g1)}$"], ["(ii), intended", "$y(x) = " + tex(g2) + "$"], ["(ii), literal reading", "$y(x) = " + tex(g2b.subs(t, X)) + "$"], ["(iii)", f"${tex(g3)}$"]])
    p4.ul(["The number of arbitrary constants equals the order ($3$, $3$, $4$), as the dimension of the solution space requires (Robinson Sec. 16.2).",
           "(i): three distinct real roots $1, 2, 3$, none equal to the exponent $s = -1$ of the forcing, hence no factor $t$.",
           "(ii): $P(k) = k^3 - 3k + 2 = (k - 1)^2(k + 2)$ has the **double** root $1$, giving $e^x$ and $xe^x$; the forcing exponent is $s = \\pm i$, not a root.",
           "(iii): $P(k) = k^4 - 4k^3 + 8k^2 - 8k + 4 = (k^2 - 2k + 2)^2 = ((k - 1)^2 + 1)^2$ has the **double** complex pair $1 \\pm i$, giving $e^t\\cos t, e^t\\sin t, te^t\\cos t, te^t\\sin t$; the forcing exponent is $\\pm i$, not a root.",
           "Each particular integral was substituted back into its equation symbolically (script `scripts/verify_topic3_topic4.py`); the residual vanishes identically."])
    return n
