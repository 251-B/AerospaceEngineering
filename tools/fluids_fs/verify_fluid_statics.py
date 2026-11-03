"""SymPy check of every result of Fluid Mechanics Topic 5 (Hydrostatics): theory formulas and problems FS1-FS10.

    python tools/fluids_fs/verify_fluid_statics.py      # prints one line per check, exit 1 on the first failure

Each check integrates the pressure field from first principles (dF = -p n dA, dM = (x - x_o) x dF) and compares the
result with the closed form written in the vault notes, so a typing error in a note shows up here before it reaches
the web page. FS8 is a second scan of FS2 and is not checked twice.
"""
import sys

import sympy as sp

rho, g, pa, L, h, H, R, W, b = sp.symbols("rho g p_a L h H R W b", positive=True)
z, y, s, th, ph, al = sp.symbols("z y s theta phi alpha", real=True)
FAILED = []


def check(name, got, want):
    ok = sp.simplify(sp.expand(got - want)) == 0
    print(f"{'ok  ' if ok else 'FAIL'} {name}: {sp.simplify(got)}")
    if not ok:
        FAILED.append(name)
        print(f"     expected {sp.simplify(want)}")


def theory():
    # plane surface inclined at theta, strip dA = w(s) ds at distance s from the free-surface line, depth s sin(theta)
    s1, s2, w = sp.symbols("s_1 s_2 w", positive=True)
    th0 = sp.Symbol("theta_0", positive=True)
    F = sp.integrate(rho * g * s * sp.sin(th0) * w, (s, s1, s2))
    A = w * (s2 - s1)
    sC = (s1 + s2) / 2
    check("plane rectangle: F = rho g sin(theta) s_C A", F, rho * g * sp.sin(th0) * sC * A)
    M = sp.integrate(rho * g * s * sp.sin(th0) * w * s, (s, s1, s2))
    I = w * (s2 - s1) ** 3 / 12
    check("plane rectangle: s_CP = s_C + I/(s_C A)", M / F, sC + I / (sC * A))
    # moment about the centroidal axis is rho g sin(theta) I, independent of the depth
    check("plane rectangle: M_C = rho g sin(theta) I", sp.integrate(rho * g * s * sp.sin(th0) * w * (s - sC), (s, s1, s2)),
          rho * g * sp.sin(th0) * I)
    # second moments used by the plane-gate simulator
    check("I_C square", sp.integrate(L * (s - L / 2) ** 2, (s, 0, L)), L ** 4 / 12)
    check("I_C triangle (base L at the bottom, height L)", sp.integrate(L * (1 - s / L) * (s - L / 3) ** 2, (s, 0, L)), L ** 4 / 36)
    check("I_C circle of diameter L", sp.integrate(2 * sp.sqrt((L / 2) ** 2 - y ** 2) * y ** 2, (y, -L / 2, L / 2)), sp.pi * L ** 4 / 64)
    # area of the half disc (x < 0) below the level y = h of a cylinder of radius R standing on the floor
    beta = sp.Symbol("beta", positive=True)
    hb = R - R * sp.cos(beta)
    want = R ** 2 * beta / 2 - (R - hb) * R * sp.sin(beta) / 2
    for v in (sp.pi / 6, sp.pi / 3, sp.pi / 2, 2 * sp.pi / 3, sp.pi):
        u = sp.Symbol("u", positive=True)                # y = R - R cos u, width R sin u, dy = R sin u du
        A = sp.integrate((R * sp.sin(u)) * (R * sp.sin(u)), (u, 0, v))
        check(f"curved: sector - triangle at beta = {v}", A, want.subs(beta, v))
    # standard atmosphere exponent and isothermal layer
    Rg, lam, T0, z0 = sp.symbols("R_g lambda T_0 z_0", positive=True)
    zz = sp.Symbol("z", positive=True)
    p = pa * (1 - lam * zz / T0) ** (g / (Rg * lam))
    check("troposphere solves dp/dz = -p g/(R_g T)", sp.diff(p, zz) + p * g / (Rg * (T0 - lam * zz)), 0)
    print(f"     g/(R_g lambda) = {9.81 / (287 * 6.5e-3):.4f}, p_11/p_a = {(216.66 / 288.16) ** (9.81 / (287 * 6.5e-3)):.4f}")


def fs1():
    rf, rh, ra, Vh = sp.symbols("rho_f rho_h rho_a V_h", positive=True)
    Vs = sp.solve(sp.Eq(rf * g * sp.Symbol("V"), rh * g * Vh), sp.Symbol("V"))[0]
    check("FS1 V_s", Vs, rh / rf * Vh)
    Va = rh * Vh / ra
    check("FS1 V_d = V_a - V_s", Va - Vs, rh / ra * Vh * (1 - ra / rf))
    check("FS1 rho_f = rho_a", (Va - Vs).subs(rf, ra), 0)


def fs2():
    # hemisphere of radius R on the sea floor, outward normal e_r, z = R sin(phi) (phi = elevation)
    n_z = sp.sin(ph)
    dS = R ** 2 * sp.cos(ph)
    Fz = -sp.integrate(sp.integrate(rho * g * (H - R * sp.sin(ph)) * n_z * dS, (th, 0, 2 * sp.pi)), (ph, 0, sp.pi / 2))
    check("FS2 F_z (integration)", Fz, -sp.pi * R ** 2 * rho * g * (H - 2 * R / 3))
    check("FS2 F_z (weight of the virtual column)", Fz, -rho * g * (sp.pi * R ** 2 * H - sp.Rational(2, 3) * sp.pi * R ** 3))
    Fx = -sp.integrate(sp.integrate(rho * g * (H - R * sp.sin(ph)) * sp.cos(ph) * sp.cos(th) * dS, (th, 0, 2 * sp.pi)), (ph, 0, sp.pi / 2))
    check("FS2 F_x = 0", Fx, 0)


def fs3():
    H1, H2, pc = sp.symbols("H_1 H_2 p_c", positive=True)
    sol = sp.solve([sp.Eq((pc - pa) * L ** 2, W), sp.Eq(pc, pa + rho * g * H1), sp.Eq(pa * L ** 3, pc * L ** 2 * (L - H2))],
                   [H1, H2, pc], dict=True)[0]
    check("FS3 H1/L", sol[H1] / L, W / (rho * g * L ** 3))
    check("FS3 H2/L", sol[H2] / L, W / (pa * L ** 2 + W))
    check("FS3 p_c", sol[pc], pa + W / L ** 2)
    check("FS3 Archimedes: displaced volume L^2 H1", rho * g * L ** 2 * sol[H1], W)


def fs4():
    F = sp.integrate(rho * g * (h - z) * L, (z, 0, L))
    check("FS4 F", F, rho * g * L ** 2 * (h - L / 2))
    M = sp.integrate((L / 2 - z) * rho * g * (h - z) * L, (z, 0, L))
    check("FS4 moment about the centre", M, rho * g * L ** 4 / 12)
    check("FS4 F_A", M / (L / 2), rho * g * L ** 3 / 6)
    e = (L ** 4 / 12) / ((h - L / 2) * L ** 2)
    check("FS4 F times (z_C - z_CP)", F * e, rho * g * L ** 4 / 12)


def fs5():
    r1, r2, H1, H2 = sp.symbols("rho_1 rho_2 H_1 H_2", positive=True)
    M1 = sp.integrate(r1 * g * (H1 - z) * b * z, (z, 0, H1))
    M2 = sp.integrate(r2 * g * (H2 - z) * b * z, (z, 0, H2))
    check("FS5 M1", M1, r1 * g * b * H1 ** 3 / 6)
    check("FS5 M2", M2, r2 * g * b * H2 ** 3 / 6)
    Hc = sp.solve(sp.Eq(M1, M2.subs(H2, sp.Symbol("x", positive=True))), sp.Symbol("x", positive=True))[0]
    check("FS5 H_c", Hc, H1 * (r1 / r2) ** sp.Rational(1, 3))
    check("FS5 stop reaction", (M1 - M2) / H1, g * b * (r1 * H1 ** 3 - r2 * H2 ** 3) / (6 * H1))


def fs6():
    Hs, hs = sp.symbols("H h", positive=True)
    a = L * sp.sqrt(3) / 2 + hs - Hs                       # height of the air triangle
    A0 = sp.sqrt(3) * L ** 2 / 4
    A = a ** 2 / sp.sqrt(3)
    check("FS6 area of a similar triangle of height a (h=0, H=0 gives A0)", A.subs({hs: 0, Hs: 0}), A0)
    check("FS6 p/p_a (isothermal)", A0 / A, sp.Rational(3, 4) * L ** 2 / a ** 2)
    At = (L * sp.sqrt(3) / 2 - Hs) ** 2 / sp.sqrt(3)
    check("FS6 W/(rho g L^2)", (A - At) / L ** 2,
          ((sp.sqrt(3) / 2 + hs / L - Hs / L) ** 2 - (sp.sqrt(3) / 2 - Hs / L) ** 2) / sp.sqrt(3))
    # numerical example used in the note: rho g L/p_a = 0.1, W/(rho g L^2) = 0.2
    X, Y, P = sp.symbols("X Y P", positive=True)
    eqs = [P - sp.Rational(3, 4) / (sp.sqrt(3) / 2 + Y - X) ** 2, P - (1 + sp.Rational(1, 10) * Y),
           sp.Rational(1, 5) - ((sp.sqrt(3) / 2 + Y - X) ** 2 - (sp.sqrt(3) / 2 - X) ** 2) / sp.sqrt(3)]
    sol = sp.nsolve(eqs, [X, Y, P], [0.5, 0.05, 1.0])
    print(f"     FS6 example: H/L = {float(sol[0]):.4f}, h/L = {float(sol[1]):.4f}, p/p_a = {float(sol[2]):.4f}")


def fs7():
    r1, r2, h1, h2 = sp.symbols("rho_1 rho_2 h_1 h_2", positive=True)
    # left face: force -p n dl with n towards the liquid = (-cos a, -sin a), dl = dy/cos a
    F1 = [sp.integrate(r1 * g * (h1 - y) * c / sp.cos(al), (y, 0, h1)) for c in (sp.cos(al), sp.sin(al))]
    check("FS7 F1x", F1[0], r1 * g * h1 ** 2 / 2)
    check("FS7 F1y", F1[1], r1 * g * h1 ** 2 / 2 * sp.tan(al))
    F2 = [sp.integrate(r2 * g * (h2 - y) * c / sp.cos(al), (y, 0, h2)) for c in (-sp.cos(al), sp.sin(al))]
    check("FS7 F2x", F2[0], -r2 * g * h2 ** 2 / 2)
    check("FS7 Ry", -(F1[1] + F2[1]) + W, W - (r1 * h1 ** 2 + r2 * h2 ** 2) * g * sp.tan(al) / 2)
    M1 = sp.integrate(r1 * g * (h1 - y) * (y / sp.cos(al)) / sp.cos(al), (y, 0, h1))
    check("FS7 M1 about O", M1, r1 * g * h1 ** 3 / (6 * sp.cos(al) ** 2))
    # cross product check: r = (-y tan a, y), dF = p (cos a, sin a) dy/cos a, M_z = x dF_y - y dF_x
    Mz = sp.integrate(((-y * sp.tan(al)) * sp.sin(al) - y * sp.cos(al)) * r1 * g * (h1 - y) / sp.cos(al), (y, 0, h1))
    check("FS7 M1 from r x dF (clockwise)", -Mz, r1 * g * h1 ** 3 / (6 * sp.cos(al) ** 2))


def fs9():
    l = sp.Symbol("l", positive=True)
    M = sp.integrate(rho * g * (H + l - z) * z, (z, -h, l))
    check("FS9 M about the hinge", M, rho * g * ((H + l) * (l ** 2 - h ** 2) / 2 - (l ** 3 + h ** 3) / 3))
    Hc = sp.solve(sp.Eq(M, 0), H)[0]
    check("FS9 H", Hc, sp.Rational(2, 3) * (l ** 3 + h ** 3) / (l ** 2 - h ** 2) - l)
    check("FS9 H factored", Hc, (l + h) * (2 * h - l) / (3 * (l - h)))
    zcp = sp.integrate(rho * g * (H + l - z) * z, (z, -h, l)) / sp.integrate(rho * g * (H + l - z), (z, -h, l))
    check("FS9 centre of pressure at the hinge when H = H_c", sp.simplify(zcp.subs(H, Hc)), 0)


def fs10():
    Ls = sp.Symbol("L", positive=True)
    # left half fully wetted to 2R: theta from the top, y = R + R cos(theta), n_x = -sin(theta)
    F1 = sp.integrate(rho * g * (2 * R - (R + R * sp.cos(th))) * sp.sin(th) * Ls * R, (th, 0, sp.pi))
    check("FS10 F1 (integration)", F1, 2 * rho * g * R ** 2 * Ls)
    check("FS10 F1 (projection)", rho * g * R * (2 * R * Ls), 2 * rho * g * R ** 2 * Ls)
    F2 = sp.integrate(rho * g * (R - (R + R * sp.cos(th))) * sp.sin(th) * Ls * R, (th, sp.pi / 2, sp.pi))
    check("FS10 F2 (integration)", F2, rho * g * R ** 2 * Ls / 2)
    net = F1 - F2
    check("FS10 net", net, sp.Rational(3, 2) * rho * g * R ** 2 * Ls)
    print(f"     FS10 numbers: {float(net.subs({rho: 1000, g: 9.81, R: 0.5, Ls: 5})):.2f} N")


def main():
    for f in (theory, fs1, fs2, fs3, fs4, fs5, fs6, fs7, fs9, fs10):
        print(f"--- {f.__name__}")
        f()
    if FAILED:
        print(f"{len(FAILED)} check(s) failed: {', '.join(FAILED)}")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
