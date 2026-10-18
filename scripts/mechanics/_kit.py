"""Shared helpers for the SymPy checks of the Engineering Mechanics Midterm 1 bank.

Every problem module `pNN.py` defines `verify(chk)`; `chk(name, left, right, numeric=None)` records that
`left - right` simplifies to zero (or, when `numeric` is a dict of substitutions, that it is zero there).
`chk.true(name, condition)` records a plain boolean check (inequalities, signs, numeric values).
The runner `scripts/verify_mechanics_problems.py` imports every module and prints the table.
"""
import sympy as sp


class Checker:
    def __init__(self, tag):
        self.tag = tag
        self.rows = []

    def __call__(self, name, left, right=0, numeric=None):
        diff = sp.simplify(sp.sympify(left) - sp.sympify(right))
        if diff != 0 and numeric is not None:
            diff = sp.simplify(diff.subs(numeric))
        if diff != 0:
            diff = sp.nsimplify(sp.simplify(sp.trigsimp(diff)))
        ok = diff == 0
        self.rows.append((name, bool(ok), "" if ok else f"residual {diff}"))
        return ok

    def true(self, name, cond, detail=""):
        self.rows.append((name, bool(cond), detail))
        return bool(cond)

    def value(self, name, expr, expected, tol=1e-9):
        got = sp.N(expr, 15)
        ok = abs(got - sp.N(expected, 15)) < tol
        self.rows.append((name, bool(ok), f"{got}" if not ok else f"= {sp.N(got, 8)}"))
        return ok


def unit(angle, kind="r"):
    """Planar polar unit vectors in the inertial basis: kind 'r' -> (cos, sin), 'th' -> (-sin, cos)."""
    return sp.Matrix([sp.cos(angle), sp.sin(angle)]) if kind == "r" else sp.Matrix([-sp.sin(angle), sp.cos(angle)])
