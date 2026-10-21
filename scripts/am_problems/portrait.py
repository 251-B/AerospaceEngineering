"""Phase-portrait analysis text and figure registration for the results of planar.py.

(No backslash may appear inside an f-string expression in Python 3.11, so every choice of wording is computed first.)
"""
import sympy as sp

from .core import register_figure, tex, vec


def fl(m):
    return [[float(m[i, j]) for j in range(2)] for i in range(2)]


def vlabel(v):
    return f"({tex(v[0])}, {tex(v[1])})"


def _figs(doc, prefix, zs, xs):
    if zs is not None:
        register_figure(prefix + "-z", zs)
        doc.fig(prefix + "-z", zs["caption"])
    register_figure(prefix + "-x", xs)
    doc.fig(prefix + "-x", xs["caption"])


def real_portrait(doc, out, prefix):
    A, J = out["A"], out["J"]
    l1, l2, v1, v2 = out["l1"], out["l2"], out["v1"], out["v2"]
    doc.h(4, "Phase portrait")
    BS = "\\"
    if l1 == 0 or l2 == 0:
        i0 = 1 if l1 == 0 else 2
        lnz, vz, vnz = (l2, v1, v2) if l1 == 0 else (l1, v2, v1)
        nz = 2 if l1 == 0 else 1
        toward = "towards" if lnz < 0 else "away from"
        behaviour = ("approaches the line of equilibria as $t \\to +\\infty$ (the equilibria are stable but each orbit ends at a different point)"
                     if lnz < 0 else "leaves the line of equilibria as $t \\to +\\infty$ (the equilibria are unstable)")
        doc.p(f"One eigenvalue is zero and the other is $\\lambda_{nz} = {tex(lnz)} \\neq 0$. In the canonical plane $\\dot z_{i0} = 0$, so $z_{i0}$ is constant along every solution (Topic 4, case $\\lambda = 0$).")
        doc.p(f"Every point of the line through $\\mathbf v_{i0} = {vlabel(vz)}$ is an equilibrium, because $A\\mathbf v_{i0} = \\mathbf 0$. Every other solution moves on a straight line parallel to $\\mathbf v_{nz} = {vlabel(vnz)}$ with $\\mathbf x - \\mathbf x_{{eq}} \\propto e^{{{tex(lnz)}t}}$: it {behaviour}. The arrows point {toward} the line of equilibria.")
        capz = "Canonical $\\mathbf z$-plane: the line of equilibria (green) and the trajectories parallel to the other axis."
        capx = f"Original $(x, y)$-plane: equilibria on the line through ${vlabel(vz)}$ (green); trajectories parallel to ${vlabel(vnz)}$, {toward} that line."
        zs = dict(A=fl(J), lines=[[1, 0, "z_1"], [0, 1, "z_2"]], axes=["z_1", "z_2"], plane="z-plane", title=prefix + " z-plane", caption=capz)
        xs = dict(A=fl(A), lines=[[float(v1[0]), float(v1[1]), "v_1"], [float(v2[0]), float(v2[1]), "v_2"]], axes=["x", "y"], plane="x-plane", title=prefix + " x-plane", caption=capx)
        _figs(doc, prefix, zs, xs)
        return "line of equilibria"
    stable, unstable = l1 < 0 and l2 < 0, l1 > 0 and l2 > 0
    word = "stable node" if stable else ("unstable node" if unstable else "saddle")
    signs = "both negative" if stable else ("both positive" if unstable else "of opposite signs")
    ratio = sp.nsimplify(l2 / l1)
    doc.p(f"$\\lambda_1 = {tex(l1)}$ and $\\lambda_2 = {tex(l2)}$ are {signs}: the origin is a **{word}** (Robinson Ch. 28, Topic 4 Sec. 6 and 9).")
    doc.p(f"In the canonical $\\mathbf z$-plane, eliminating $t$ from $z_1 = c_1e^{{{tex(l1)}t}}$ and $z_2 = c_2e^{{{tex(l2)}t}}$ (for $c_1 \\neq 0$): $|z_1|/|c_1| = e^{{\\lambda_1t}}$, so $e^{{t}} = (|z_1|/|c_1|)^{{1/\\lambda_1}}$ and $|z_2| = |c_2|e^{{\\lambda_2t}} = |c_2|\\,(|z_1|/|c_1|)^{{\\lambda_2/\\lambda_1}}$, i.e. $z_2 = K\\,|z_1|^{{\\lambda_2/\\lambda_1}} = K\\,|z_1|^{{{tex(ratio)}}}$ with $K = c_2|c_1|^{{-\\lambda_2/\\lambda_1}}$ (equivalently, integrate the separable equation $\\frac{{dz_2}}{{dz_1}} = \\frac{{\\lambda_2z_2}}{{\\lambda_1z_1}}$ by the chain rule, as in Exercise 10). The axes $z_1 = 0$ and $z_2 = 0$ are invariant: a solution that starts on an axis stays on it.")
    if l1 * l2 < 0:
        vs, vu = (v1, v2) if l1 < 0 else (v2, v1)
        doc.p(f"The exponent $\\lambda_2/\\lambda_1 = {tex(ratio)}$ is negative, so the orbits are hyperbola-like. Only solutions starting on the eigenline of the negative eigenvalue, the line through ${vlabel(vs)}$ (the **stable manifold**), reach the origin as $t \\to +\\infty$; the line through ${vlabel(vu)}$ (positive eigenvalue) is the **unstable manifold**. All other orbits come in close to the stable line, then leave along the unstable one.")
    else:
        slow, sl = (v1, l1) if abs(l1) < abs(l2) else (v2, l2)
        when = "they arrive there as $t \\to +\\infty$" if stable else "they leave from there (the limit $t \\to -\\infty$)"
        toward = "towards" if stable else "away from"
        doc.p(f"The exponent $\\lambda_2/\\lambda_1 = {tex(ratio)}$ is positive, so the orbits are parabola-like curves through the origin. At the origin they are tangent to the eigenvector of the eigenvalue of **smaller modulus**, $|\\lambda| = {tex(abs(sl))}$, i.e. to the line through ${vlabel(slow)}$ ({when}), and far from the origin they become parallel to the other eigenvector (the fast direction). The arrows point {toward} the origin on both eigenlines.")
    o1 = "outward" if l1 > 0 else "inward"
    o2 = "outward" if l2 > 0 else "inward"
    doc.p(f"The map $\\mathbf x = Q\\mathbf z$ sends the $z_1$-axis to the line through $\\mathbf v_1 = {vlabel(v1)}$ and the $z_2$-axis to the line through $\\mathbf v_2 = {vlabel(v2)}$. Straight lines stay straight and the origin stays fixed, so the $\\mathbf x$-portrait is the canonical one sheared onto the eigenlines. On $\\mathbf v_1$: $\\dot{{\\mathbf x}} = A\\mathbf v_1 = {tex(l1)}\\mathbf v_1$ points {o1}; on $\\mathbf v_2$: $\\dot{{\\mathbf x}} = {tex(l2)}\\mathbf v_2$ points {o2}.")
    capz = f"Canonical $\\mathbf z$-plane ({word}): invariant axes and orbits $z_2 = K|z_1|^{{{tex(ratio)}}}$."
    capx = f"Original $(x, y)$-plane ({word}): dashed lines are the eigenlines $\\mathbf v_1 = {vlabel(v1)}$ and $\\mathbf v_2 = {vlabel(v2)}$."
    zs = dict(A=fl(J), lines=[[1, 0, "z_1"], [0, 1, "z_2"]], axes=["z_1", "z_2"], plane="z-plane", title=prefix + " z-plane", caption=capz)
    xs = dict(A=fl(A), lines=[[float(v1[0]), float(v1[1]), "v_1"], [float(v2[0]), float(v2[1]), "v_2"]], axes=["x", "y"], plane="x-plane", title=prefix + " x-plane", caption=capx)
    _figs(doc, prefix, zs, xs)
    return word


def complex_portrait(doc, out, prefix):
    A, Q, J = out["A"], out["Q"], out["J"]
    rho, om = out["rho"], out["om"]
    detQ = sp.simplify(Q.det())
    doc.h(4, "Phase portrait")
    word = "centre" if rho == 0 else ("stable spiral" if rho < 0 else "unstable spiral")
    if rho == 0:
        shape = "the orbits are circles of period $T = 2\\pi/\\omega$ (closed orbits)."
    else:
        fac = tex(sp.simplify(sp.exp(2 * sp.pi * rho / om)))
        shape = f"one full turn takes $T = 2\\pi/\\omega$ while the radius is multiplied by $e^{{2\\pi\\rho/\\omega}} = {fac}$ ({'shrinking' if rho < 0 else 'growing'})."
    doc.p(f"$\\rho = {tex(rho)}$ and $\\omega = {tex(om)}$: the origin is a **{word}**. In the $\\mathbf z$-plane $r = r_0e^{{{tex(rho)}t}}$ and $\\theta = \\theta_0 - {tex(om)}t$: the motion is always **clockwise** ($\\dot\\theta = -\\omega < 0$), and {shape}")
    tx = A * sp.Matrix([0, 1])
    sense = "clockwise" if tx[0] > 0 else "counter-clockwise"
    where = "$> 0$: to the right at the top of the plane" if tx[0] > 0 else "$< 0$: to the left at the top of the plane"
    dsign = "$> 0$" if detQ > 0 else "$< 0$"
    pres = "preserves" if detQ > 0 else "reverses"
    final = "clockwise" if detQ > 0 else "counter-clockwise"
    doc.p(f"Sense of rotation in the $\\mathbf x$-plane, tested directly on the vector field (Topic 4 Sec. 7.8): at $(0, 1)^T$, $\\dot{{\\mathbf x}} = A(0, 1)^T = {vec(tx[0], tx[1])}$, so $\\dot x = {tex(tx[0])}$ is {where}: the rotation is **{sense}**. Cross-check: $\\det Q = {tex(detQ)}$ is {dsign}, so $Q$ {pres} orientation and the clockwise motion of the $\\mathbf z$-plane becomes {final} in the $\\mathbf x$-plane, in agreement.")
    assert (tx[0] > 0) == (detQ > 0), (A, detQ, tx)
    capz = f"Canonical $\\mathbf z$-plane ({word}): clockwise, $\\dot\\theta = -\\omega$."
    capx = f"Original $(x, y)$-plane ({word}), {sense}."
    zs = dict(A=fl(J), axes=["z_1", "z_2"], plane="z-plane", title=prefix + " z-plane", caption=capz)
    xs = dict(A=fl(A), axes=["x", "y"], plane="x-plane", title=prefix + " x-plane", caption=capx)
    _figs(doc, prefix, zs, xs)
    return word


def improper_portrait(doc, out, prefix):
    A, J, lam, v1, N = out["A"], out["J"], out["lam"], out["v1"], out["N"]
    doc.h(4, "Phase portrait")
    word = "stable improper node" if lam < 0 else ("unstable improper node" if lam > 0 else "line of equilibria (nilpotent shear)")
    if lam == 0:
        doc.p(f"$\\lambda = 0$: every point of the eigenline through $\\mathbf v_1 = {vlabel(v1)}$ is an equilibrium. In the $\\mathbf z$-plane $z_2 = c_2$ is constant and $z_1 = c_1 + c_2t$ moves with constant speed $c_2$: horizontal lines, to the right if $z_2 > 0$ and to the left if $z_2 < 0$. Under $\\mathbf x = Q\\mathbf z$ they become lines parallel to $\\mathbf v_1$: on the side of the eigenline where $\\mathbf v_2$ points (for $z_2 > 0$) they are traversed along $+\\mathbf v_1$, on the opposite side along $-\\mathbf v_1$.")
    else:
        away = "away from" if lam > 0 else "towards"
        doc.p(f"$\\lambda = {tex(lam)}$ is repeated with a single eigendirection and $A \\neq \\lambda I$: the origin is an **{word}** (Topic 4 Sec. 8.8 and 8.9). In the $\\mathbf z$-plane the $z_1$-axis is invariant ($z_2 \\equiv 0$, $z_1 = c_1e^{{{tex(lam)}t}}$, arrows {away} the origin); the other orbits satisfy $z_1 = z_2\\left[K + \\frac{{1}}{{\\lambda}}\\ln|z_2|\\right]$, are S-shaped, tangent to the $z_1$-axis at the origin and parallel to it far away. Since $\\dot z_1 = \\lambda z_1 + z_2 = z_2$ on the $z_2$-axis, orbits cross it moving to the right in the upper half-plane and to the left in the lower one.")
    Np = N * sp.Matrix([0, 1])
    k = sp.simplify(Np[0] / v1[0]) if v1[0] != 0 else sp.simplify(Np[1] / v1[1])
    drift = "+" if k > 0 else "-"
    tail = "The orbits are tangent to the eigenline at the origin and bend into an S around it." if lam != 0 else "The orbits are the straight lines parallel to $\\mathbf v_1$."
    doc.p(f"Orientation in the $\\mathbf x$-plane, from $N\\mathbf x = (A - \\lambda I)\\mathbf x = z_2\\mathbf v_1$ (Topic 4 Sec. 8.9): at $(0, 1)^T$, $N(0, 1)^T = {vec(Np[0], Np[1])} = {tex(k)}\\,\\mathbf v_1$, so there the orbit drifts along ${drift}\\mathbf v_1$. {tail}")
    capz = f"Canonical $\\mathbf z$-plane ({word})."
    capx = f"Original $(x, y)$-plane ({word}); dashed: the eigenline with $\\mathbf v_1 = {vlabel(v1)}$."
    zs = dict(A=fl(J), lines=[[1, 0, "z_1"]], axes=["z_1", "z_2"], plane="z-plane", title=prefix + " z-plane", caption=capz)
    xs = dict(A=fl(A), lines=[[float(v1[0]), float(v1[1]), "v_1"]], axes=["x", "y"], plane="x-plane", title=prefix + " x-plane", caption=capx)
    _figs(doc, prefix, zs, xs)
    return word


def star_portrait(doc, out, prefix):
    A, lam = out["A"], out["lam"]
    doc.h(4, "Phase portrait")
    word = "stable star" if lam < 0 else "unstable star"
    toward = "towards" if lam < 0 else "away from"
    doc.p(f"$A = {tex(lam)}I$: every line through the origin is invariant and every solution moves along its own ray, $\\mathbf x(t) = e^{{{tex(lam)}t}}\\mathbf x_0$, {toward} the origin (the origin is a **{word}**). The picture is the same in every basis, so there is no separate canonical plane.")
    cap = f"{word.capitalize()}: straight rays {'into' if lam < 0 else 'out of'} the origin."
    xs = dict(A=fl(A), axes=["x", "y"], plane="x-plane", title=prefix + " star", caption=cap)
    _figs(doc, prefix, None, xs)
    return word


def portrait(doc, out, prefix):
    k = out["kind"]
    fn = {"real": real_portrait, "complex": complex_portrait, "improper": improper_portrait, "star": star_portrait}[k]
    return fn(doc, out, prefix)
