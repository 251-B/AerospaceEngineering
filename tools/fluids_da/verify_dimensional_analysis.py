"""Check of every exponent system and every number of Fluid Mechanics Topic 6 (Dimensional Analysis): the theory note
(Notes.pdf, Chapter 6) and the problems DA1-DA14.

    python tools/fluids_da/verify_dimensional_analysis.py      # one line per check, exit 1 if any fails

Pure standard library: each exponent system "[a0] = [a1]^x [a2]^y [a3]^z" is solved exactly with fractions, each group
written in the notes is checked to be dimensionless, and each number of the notes is recomputed from the data, so a
typing error in a note shows up here before it reaches the web page.
"""
import math
import sys
from fractions import Fraction as Fr

# dimensions as exponents of (L, M, T, Theta)
D = {
    "1": (0, 0, 0, 0), "L": (1, 0, 0, 0), "A": (2, 0, 0, 0), "Vol": (3, 0, 0, 0), "t": (0, 0, 1, 0), "m": (0, 1, 0, 0),
    "U": (1, 0, -1, 0), "g": (1, 0, -2, 0), "Om": (0, 0, -1, 0), "rho": (-3, 1, 0, 0), "mu": (-1, 1, -1, 0),
    "nu": (2, 0, -1, 0), "p": (-1, 1, -2, 0), "Pl": (-2, 1, -2, 0), "F": (1, 1, -2, 0), "F1": (0, 1, -2, 0),
    "E": (2, 1, -2, 0), "E1": (1, 1, -2, 0), "W": (2, 1, -3, 0), "W1": (1, 1, -3, 0), "Q": (3, 0, -1, 0),
    "q": (2, 0, -1, 0), "T": (0, 0, 0, 1), "c_p": (2, 0, -2, -1), "k": (1, 1, -3, -1),
}
FAILED = []


def report(name, ok, detail=""):
    print(f"{'ok  ' if ok else 'FAIL'} {name}{': ' + detail if detail else ''}")
    if not ok:
        FAILED.append(name)


def dims(**powers):
    """Dimensions of a product of quantities raised to powers, e.g. dims(rho=1, U=3, L=2)."""
    out = [Fr(0)] * 4
    for q, e in powers.items():
        for i in range(4):
            out[i] += Fr(e) * D[q][i]
    return tuple(out)


def solve(target, basis):
    """Exponents x with [target] = prod [basis_i]^x_i (exact; None if the basis does not fit)."""
    rows = [[Fr(D[b][j]) for b in basis] + [Fr(D[target][j])] for j in range(4)]
    n, r, piv = len(basis), 0, []
    for c in range(n):
        p = next((i for i in range(r, 4) if rows[i][c] != 0), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        rows[r] = [x / rows[r][c] for x in rows[r]]
        for i in range(4):
            if i != r and rows[i][c] != 0:
                rows[i] = [a - rows[i][c] * b for a, b in zip(rows[i], rows[r])]
        piv.append(c)
        r += 1
    if any(all(x == 0 for x in row[:n]) and row[n] != 0 for row in rows):
        return None
    x = [Fr(0)] * n
    for i, c in enumerate(piv):
        x[c] = rows[i][n]
    return tuple(x)


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def independent(name, basis, want_det, cols=(0, 1, 2)):
    """Rows of the basis with the columns in the order of the note, (L, M, T) unless `cols` says otherwise;
    the determinant as written in the note."""
    d = det3([[D[b][j] for j in cols] for b in basis])
    report(f"{name}: det{basis} = {want_det}", d == want_det, f"det = {d}")


def exps(name, target, basis, want):
    got = solve(target, basis)
    report(f"{name}: [{target}] = {basis}^{tuple(str(Fr(w)) for w in want)}", got == tuple(Fr(w) for w in want),
           f"got {tuple(str(x) for x in got) if got else None}")


def num(name, got, want, rel=5e-3):
    report(f"{name} = {want}", abs(got - want) <= rel * abs(want), f"computed {got:.6g}")


# --------------------------------------------------------------------------------------------- theory, Chapter 6
def theory():
    report("Eq. 6.9: no x, y with [rho] = [U]^x [mu]^y", solve("rho", ("U", "mu")) is None)
    independent("Eq. 6.11 (rho, U, mu)", ("rho", "U", "mu"), -1)
    independent("Eq. 6.12 (rho, U, p)", ("rho", "U", "p"), 0)
    exps("Eq. 6.20", "mu", ("Q", "L", "rho"), (1, -1, 1))
    exps("Eq. 6.21", "Pl", ("Q", "L", "rho"), (2, -5, 1))
    independent("Eq. 6.27 (E, rho, t)", ("E", "rho", "t"), 5)
    exps("Eq. 6.28 radius", "L", ("E", "rho", "t"), ("1/5", "-1/5", "2/5"))
    exps("Eq. 6.28 pressure", "p", ("E", "rho", "t"), ("2/5", "3/5", "-6/5"))
    # end of validity: E^(2/5) rho^(3/5) t^(-6/5) ~ p_a  =>  t ~ E^(1/3) rho^(1/2) p_a^(-5/6)
    report("Taylor validity time", dims(E=Fr(1, 3), rho=Fr(1, 2), p=Fr(-5, 6)) == dims(t=1))
    independent("Eq. 6.31 first rows (R, U, rho)", ("L", "U", "rho"), 1)
    exps("Eq. 6.32", "F", ("rho", "U", "L"), (1, 2, 2))
    for q, w in (("mu", (1, 1, 1)), ("p", (1, 2, 0)), ("g", (0, 2, -1))):
        exps(f"Eq. 6.33 {q}", q, ("rho", "U", "L"), w)
    report("Eq. 6.53 from 6.52: F/(rho U^2 R^2) = (F/(mu U R)) / Re",
           dims(F=1, rho=-1, U=-2, L=-2) == dims(F=1, mu=-1, U=-1, L=-1) == (0, 0, 0, 0))
    # Re-Fr incompatibility: nu_m/nu_p = lambda^(3/2)
    lam = 0.01
    report("Section 8: Fr and Re both matched need nu_m/nu_p = lambda^(3/2)",
           math.isclose(lam ** 0.5, (lam ** 1.5) / lam), f"lambda = {lam}")


# --------------------------------------------------------------------------------------------- problems
def da1():
    independent("DA1 (V, l, rho)", ("U", "L", "rho"), -1)
    exps("DA1 W", "W", ("rho", "U", "L"), (1, 3, 2))
    exps("DA1 g", "g", ("U", "L"), (2, -1))
    exps("DA1 m", "m", ("rho", "U", "L"), (1, 0, 3))
    num("DA1 V_e (m/s)", (1 / 100) ** 0.5 * 10, 1)
    num("DA1 m_e (kg)", (1 / 100) ** 3 * 1e6, 1)
    num("DA1 W (W)", 10 ** 3 * 100 ** 2 * 10, 1e8)


def da2():
    independent("DA2 (rho, mu, R)", ("rho", "mu", "L"), -1)
    exps("DA2 U_c", "U", ("rho", "mu", "L"), (-1, 1, -1))
    exps("DA2 T", "t", ("rho", "U", "L"), (0, -1, 1))
    exps("DA2 F per length", "F1", ("rho", "U", "L"), (1, 2, 1))
    num("DA2 U_c (R = 2 mm)", 0.2 / 2, 0.1)
    for U, T, F in ((1, 10e-3, 0.12e-3), (4, 2.5e-3, 1.92e-3), (20, 0.5e-3, 48e-3)):
        num(f"DA2 C_T at U = {U}", T * U / 1e-3, 10)
        num(f"DA2 C_F at U = {U}", F / (1.2 * U ** 2 * 1e-3), 0.1)
    num("DA2 F at U = 10 m/s, R = 2 mm (N/m)", 0.1 * 1.2 * 100 * 0.002, 0.024)


def da3():
    independent("DA3 (Omega, h, mu)", ("Om", "L", "mu"), -1)
    exps("DA3 W", "W", ("mu", "Om", "L"), (1, 2, 3))
    exps("DA3 g", "g", ("Om", "L"), (2, 1))
    exps("DA3 rho", "rho", ("mu", "Om", "L"), (1, -1, -2))
    he = (1e-3 / 1e-6) ** (-2 / 3)
    num("DA3 h_e/h", he, 0.01)
    num("DA3 Omega_e", (1 / he) ** 0.5, 10)
    num("DA3 V_e (m^3)", he ** 3 * 1000, 1e-3)
    num("DA3 W/W_e", (2.0 / 1e-3) * 0.1 ** 2 * 100 ** 3, 2e7)
    num("DA3 W/W_e with rho Omega^3 h^5", 2 * 0.1 ** 3 * 100 ** 5, 2e7)


def da4():
    independent("DA4 (D, g, rho)", ("L", "g", "rho"), 2)
    exps("DA4 u_t", "U", ("L", "g"), ("1/2", "1/2"))
    exps("DA4 mu", "mu", ("rho", "g", "L"), (1, "1/2", "3/2"))
    r = 680 ** (2 / 3)
    num("DA4 680^(2/3)", r, 77.33)
    num("DA4 D_e (mm)", r * 30e-3, 2.32)
    num("DA4 m_e (g)", 1.25 * r ** 3 * 0.2e-6, 0.1156)
    num("DA4 u_t (mm/s)", (1 / r) ** 0.5 * 1.0, 0.1137)


def da5():
    exps("DA5 n", "Om", ("U", "L"), (1, -1))
    num("DA5 n at U = 15", 200 * 1.5, 300)
    num("DA5 W at U = 15 (kW)", 1.5 ** 3 * 7, 23.625)
    for n1, W1, W in ((125, 4, 16.38), (150, 5.5, 13.04), (175, 6.5, 9.70), (225, 6, 4.21), (250, 4.5, 2.30)):
        U = 200 / n1 * 10
        num(f"DA5 W(n=200) from n1 = {n1}", (U / 10) ** 3 * W1, W)
    num("DA5 n1 for D = 10 m", 175 * 2 * 0.5, 175)
    num("DA5 W for D = 10 m (kW)", 2 ** 3 * 2 ** 2 * 6.5, 208)


def da6():
    independent("DA6 (rho, g, h)", ("rho", "g", "L"), -2)
    exps("DA6 F per width", "F1", ("rho", "g", "L"), (1, 1, 2))
    exps("DA6 mu", "mu", ("rho", "g", "L"), (1, "1/2", "3/2"))
    num("DA6 h' (m)", 0.3 / 3 * 2, 0.2)
    num("DA6 U (m/s)", 10 ** 0.5 * 2, 6.32)
    num("DA6 F (N/m)", 100 * 1500, 1.5e5)
    num("DA6 real viscosity group", 1e-6 / (9.81 ** 0.5 * 2 ** 1.5), 1.1e-7, rel=0.05)
    num("DA6 model viscosity group", 1e-6 / (9.81 ** 0.5 * 0.2 ** 1.5), 3.6e-6, rel=0.02)


def da7():
    independent("DA7 (rho, W, A_s)", ("rho", "W", "A"), -6)
    exps("DA7 E", "F", ("rho", "W", "A"), ("1/3", "2/3", "1/3"))
    exps("DA7 mu", "mu", ("rho", "W", "A"), ("2/3", "1/3", "1/6"))
    num("DA7 W (W)", 100 ** 1.5 * (1 / 100) ** 0.5 * 100, 1e4)
    num("DA7 Reynolds estimate", 1e3 ** (2 / 3) * 1e-2 ** (1 / 6) * 100 ** (1 / 3) / 1e-3, 2.15e5, rel=0.01)


def da8():
    independent("DA8 (f, L, rho)", ("Om", "L", "rho"), -1)
    exps("DA8 F", "F", ("rho", "Om", "L"), (1, 2, 4))
    exps("DA8 mu", "mu", ("rho", "Om", "L"), (1, 1, 2))
    mue = 1.8e-5 * 800 / 1.2 * 100 ** 2 * 0.2 / 200
    num("DA8 mu_e", mue, 0.12)
    num("DA8 f/f_e", 800 / 1.2 * 100 ** 2 * 1.8e-5 / mue, 1000)
    num("DA8 F/F_e", 1.2 / 800 * 0.01 ** 4 * 1000 ** 2, 1.5e-5)
    num("DA8 F/F_e (key form)", 800 / 1.2 * (1.8e-5 / mue) ** 2, 1.5e-5)
    for Fe, F in ((1.33, 2.0e-5), (7.13, 1.07e-4), (8.00, 1.2e-4), (4.53, 6.8e-5)):
        num(f"DA8 F from F_e = {Fe}", 1.5e-5 * Fe, F, rel=0.01)


def da9():
    De = 1.775 / 1.630 * 0.736 / 1.225 * 320.5 / 340.3 * 1.5
    num("DA9 D_e (m)", De, 0.924)
    Ve = 340.3 / 320.5 * 300
    num("DA9 V_e (km/h)", Ve, 318.5)
    num("DA9 Omega_e (rpm)", 1.5 / De * Ve / 300 * 2500, 4308)
    num("DA9 W (W)", 0.736 / 1.225 * (300 / Ve) ** 3 * (1.5 / De) ** 2 * 6e7, 7.93e7)


def da10():
    independent("DA10 (mu, V_u, h)", ("mu", "U", "L"), -1)
    exps("DA10 q", "q", ("mu", "U", "L"), (0, 1, 1))
    exps("DA10 W per length", "W1", ("mu", "U", "L"), (1, 2, 0))
    exps("DA10 rho", "rho", ("mu", "U", "L"), (1, -1, -1))
    exps("DA10 Delta P", "p", ("mu", "U", "L"), (1, 1, -1))
    r = 1.41 / 5 * 2 / 1
    num("DA10 V_u ratio", r, 0.564)
    num("DA10 W ratio", 5 / 1.41 * r ** 2, 1.128)
    num("DA10 eta ratio", r * 2 / (5 / 1.41 * r ** 2), 1)
    num("DA10 glycerol low", 1260 * 0.10 * 0.01 / 1.41 / 20, 0.0447)
    num("DA10 glycerol high", 1260 * 0.35 * 0.01 / 1.41 / 20, 0.156)
    num("DA10 oil low", 1100 * 0.0564 * 0.01 / 5 / 20, 0.0062, rel=0.01)
    num("DA10 oil high", 1100 * 0.1974 * 0.01 / 5 / 20, 0.0217)
    for Vg, q, W in ((10, 2, 0.8), (35, 14.5, 5.2)):
        num(f"DA10 oil row V = {Vg}: q", r * q, {10: 1.128, 35: 8.178}[Vg])
        num(f"DA10 oil row V = {Vg}: W", 1.128 * W, {10: 0.902, 35: 5.866}[Vg], rel=1e-3)


def da11():
    independent("DA11 (rho, A, omega)", ("rho", "L", "Om"), 1)
    exps("DA11 W", "W", ("rho", "Om", "L"), (1, 3, 5))
    exps("DA11 mu", "mu", ("rho", "Om", "L"), (1, 1, 2))
    exps("DA11 g", "g", ("Om", "L"), (2, 1))
    num("DA11 omega_m", 20 ** 0.5 / 6, 5 ** 0.5 / 3)
    num("DA11 W_p (W)", 20 ** 3.5, 35777)


def da12():
    k = 0.36 / 1.22 * (295 / 340) ** 2 * 100 ** 2
    num("DA12 F_m/F_e", k, 2221)
    for Fe, Fm in ((9.2, 2.04e4), (37.5, 8.33e4), (86, 1.91e5), (383, 8.51e5), (1532, 3.40e6)):
        num(f"DA12 F_m from F_e = {Fe}", k * Fe, Fm)
    num("DA12 Re_e min", 1.22 * 400 * 0.01 / 1.98e-5, 2.46e5)
    num("DA12 Re_m min", 0.36 * 400 * 295 / 340 / 1.44e-5, 8.68e6)
    num("DA12 Fr_e^2 min", 400 ** 2 / (9.81 * 0.01), 1.63e6)
    num("DA12 Fr_m^2 min", (400 * 295 / 340) ** 2 / 9.81, 1.23e4, rel=0.01)
    num("DA12 C (U_e = 2000)", 383 / (1.22 * 2000 ** 2 * 1e-4), 0.785)
    num("DA12 C (U_e = 4000)", 1532 / (1.22 * 4000 ** 2 * 1e-4), 0.785)


def da13():
    De = 5 * (0.02 / 1.2) ** (1 / 3)
    num("DA13 D_E (m)", De, 1.277)
    VM = (3.73 / 9.81) ** 0.5 * (1.2 / 0.02) ** (1 / 6) * 2
    num("DA13 V_M (m/s)", VM, 2.44)
    num("DA13 V_M from the Froude ratio", (3.73 * 5 / (9.81 * De)) ** 0.5 * 2, 2.44)
    num("DA13 Re_E", 1.2 * 2 * 1.28 / 1.7e-5, 1.81e5)
    num("DA13 Re_M", 0.02 * 2.44 * 5 / 1.2e-5, 2.03e4)


def da14():
    independent("DA14 (mu, Omega, R), columns (M, L, T)", ("mu", "Om", "L"), 1, cols=(1, 0, 2))
    exps("DA14 M per length", "F", ("mu", "Om", "L"), (1, 1, 2))
    exps("DA14 rho", "rho", ("mu", "Om", "L"), (1, -1, -2))
    report("DA14 tau = Pi1/Pi2 = t nu/R^2 is dimensionless", dims(t=1, nu=1, L=-2) == (0, 0, 0, 0))
    report("DA14 Prandtl mu c/k is dimensionless", dims(mu=1, c_p=1, k=-1) == (0, 0, 0, 0))
    report("DA14 Omega^2 R^2/(c T0) is dimensionless", dims(Om=2, L=2, c_p=-1, T=-1) == (0, 0, 0, 0))
    report("DA14 conduction coefficient k/(rho c nu) = 1/Pr", dims(k=1, rho=-1, c_p=-1, nu=-1) == (0, 0, 0, 0))
    # steady state: v = Omega r solves d/dr[(1/r) d(r v)/dr] = 0 (checked on a grid with finite differences)
    h, ok = 1e-4, True
    for r in (0.2, 0.5, 0.9):
        inner = lambda x: (((x + h) * (x + h) - (x - h) * (x - h)) / (2 * h)) / x        # (1/r) d(r * r)/dr, Omega = 1
        ok &= abs((inner(r + h) - inner(r - h)) / (2 * h)) < 1e-6
    report("DA14 rigid rotation solves the steady equation", ok)


def main():
    for f in (theory, da1, da2, da3, da4, da5, da6, da7, da8, da9, da10, da11, da12, da13, da14):
        print(f"--- {f.__name__}")
        f()
    if FAILED:
        print(f"{len(FAILED)} check(s) failed: {', '.join(FAILED)}")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
