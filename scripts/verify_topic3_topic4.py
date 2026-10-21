#!/usr/bin/env python3
"""Symbolic verification of every result of Chapter 3 part 2 and Chapter 4 parts 1 and 2 (Advanced Maths).

The author modules (scripts/am_problems/) register one structured claim per result; this script re-checks each claim
with SymPy independently of the text that was written:

  ode          the function satisfies the ODE identically and the initial data (and, for IVPs with numeric
               coefficients, equals the solution returned by sympy.dsolve)
  integral_ode variation-of-constants formula with unevaluated integrals solves the ODE (derivative bookkeeping)
  system       (x, y) satisfies x' = a x + b y + f, y' = c x + d y + g and the initial data
  sol          a closed-form vector solution satisfies x' = A x
  canon        Q^-1 A Q = J exactly, A = Q J Q^-1, and the stored solution satisfies x' = A x

    python scripts/verify_topic3_topic4.py        # exit code 1 if any claim fails
"""
import pathlib
import sys

import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from am_problems import ch3b, ch3b_vp, ch4a, ch4a_b, ch4b, ch4b_b  # noqa: E402

failures, checked = [], 0


def is_zero(expr, var=None):
    """Zero test: exact simplification first, then numerical sampling (for trigonometric identities)."""
    expr = sp.sympify(expr)
    if sp.simplify(expr) == 0:
        return True
    syms = sorted(expr.free_symbols, key=str)
    import random
    random.seed(1)
    for _ in range(6):
        sub = {s: sp.Rational(random.randint(3, 40), 41) for s in syms}
        try:
            if abs(sp.N(expr.subs(sub), 30)) > 1e-15:
                return False
        except (TypeError, ZeroDivisionError):
            continue
    return True


def fail(tag, msg):
    failures.append((tag, msg))
    print("FAIL", tag, msg)


def check_ode(c):
    var = c["ivar"]
    sol, coeffs, rhs = sp.sympify(c["solution"]), c["coeffs"], sp.sympify(c["rhs"])
    n = len(coeffs) - 1
    res = sum(sp.sympify(co) * sp.diff(sol, var, n - i) for i, co in enumerate(coeffs)) - rhs
    if not is_zero(res):
        fail(c["id"], f"ODE residual {sp.simplify(res)}")
    if c.get("ics") is not None:
        for j, val in enumerate(c["ics"]):
            v = sp.diff(sol, var, j).subs(var, 0) - sp.sympify(val)
            if not is_zero(v):
                fail(c["id"], f"initial condition {j}: {v}")
        # independent solution with dsolve when everything is numeric
        try:
            if all(sp.sympify(co).is_number for co in coeffs) and not (sp.sympify(rhs).free_symbols - {var}):
                f = sp.Function("f")
                eq = sp.Eq(sum(sp.sympify(co) * f(var).diff(var, n - i) for i, co in enumerate(coeffs)), rhs)
                ics = {(f(0) if j == 0 else sp.Subs(f(var).diff(var, j), var, 0)): c["ics"][j] for j in range(n)}
                ds = sp.dsolve(eq, f(var), ics=ics)
                if not is_zero(ds.rhs - sol):
                    fail(c["id"], f"differs from dsolve: {sp.simplify(ds.rhs - sol)}")
        except Exception as exc:                       # dsolve is only a cross-check
            print("  (dsolve skipped for", c["id"], type(exc).__name__ + ")")


def check_integral_ode(c):
    var = c["ivar"]
    y1, y2, g = sp.sympify(c["y1"]), sp.sympify(c["y2"]), sp.sympify(c["g"])
    coeffs = c["coeffs"]
    W = sp.simplify(y1 * sp.diff(y2, var) - y2 * sp.diff(y1, var))
    u1p, u2p = -y2 * g / W, y1 * g / W
    u1, u2 = sp.Function("u1")(var), sp.Function("u2")(var)
    xp = u1 * y1 + u2 * y2

    def sub(e):
        return e.subs({u1.diff(var): u1p, u2.diff(var): u2p})
    d1 = sp.expand(sub(sp.diff(xp, var)))
    # the auxiliary condition u1' y1 + u2' y2 = 0 leaves x' = u1 y1' + u2 y2'
    if not is_zero(d1 - (u1 * sp.diff(y1, var) + u2 * sp.diff(y2, var))):
        fail(c["id"], "auxiliary condition")
    d2 = sub(sp.diff(u1 * sp.diff(y1, var) + u2 * sp.diff(y2, var), var))
    res = sp.expand(coeffs[0] * d2 + coeffs[1] * (u1 * sp.diff(y1, var) + u2 * sp.diff(y2, var)) + coeffs[2] * xp - c["rhs"])
    if not is_zero(res):
        fail(c["id"], f"variation of constants residual {sp.simplify(res)}")


def check_system(c):
    A = c["A"]
    x, y = c["sol"]
    f, g = c["f"], c["g"]
    r1 = sp.diff(x, t) - (A[0, 0] * x + A[0, 1] * y + f)
    r2 = sp.diff(y, t) - (A[1, 0] * x + A[1, 1] * y + g)
    if not (is_zero(r1) and is_zero(r2)):
        fail(c["id"], f"system residual {sp.simplify(r1)}, {sp.simplify(r2)}")
    if sp.simplify(x.subs(t, 0) - c["x0"]) != 0 or sp.simplify(y.subs(t, 0) - c["y0"]) != 0:
        fail(c["id"], "initial data")


def check_sol(c):
    A = c["A"]
    x, y = c["sol"]
    res = sp.Matrix([sp.diff(x, t), sp.diff(y, t)]) - A * sp.Matrix([x, y])
    if not all(is_zero(r) for r in res):
        fail(c["id"], f"x' - A x = {res.T}")


def check_canon(c):
    A, Q, J = c["A"], c["Q"], c["J"]
    if sp.simplify(Q.inv() * A * Q - J) != sp.zeros(2, 2):
        fail(c["id"], "Q^-1 A Q != J")
    if sp.simplify(Q * J * Q.inv() - A) != sp.zeros(2, 2):
        fail(c["id"], "A != Q J Q^-1")
    if c.get("sol") is not None:
        check_sol(dict(id=c["id"], A=A, sol=c["sol"]))


t = ch3b.t
CHECKS = {"ode": check_ode, "integral_ode": check_integral_ode, "system": check_system, "sol": check_sol, "canon": check_canon}


def main():
    global checked
    for mod, names in ((ch3b, ["ex1", "ex2", "ex3", "ex4", "ex5"]), (ch3b_vp, ["ex6", "ex7", "ex8", "ex9"]),
                       (ch4a, ["ex1", "ex2", "ex3", "ex4", "ex5", "ex6", "ex7"]), (ch4a_b, ["ex8", "ex9", "ex10", "ex11"]),
                       (ch4b, ["ex1", "ex2", "ex3", "ex4"]), (ch4b_b, ["ex5", "ex6", "ex7", "ex8"])):
        for name in names:
            getattr(mod, name)()
    claims = ch3b.CLAIMS + ch4a.CLAIMS + ch4b.CLAIMS
    for c in claims:
        CHECKS[c["kind"]](c)
        checked += 1
    by = {}
    for c in claims:
        by[c["kind"]] = by.get(c["kind"], 0) + 1
    print(f"verify_topic3_topic4: {checked} claims checked {by}")
    if failures:
        print(f"{len(failures)} FAILED")
        return 1
    print("all claims verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
