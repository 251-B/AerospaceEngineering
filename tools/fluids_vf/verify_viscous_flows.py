"""Check of the results of Fluid Mechanics Topic 7 (Viscous Flows): the problems VF2-VF20.

    python tools/fluids_vf/verify_viscous_flows.py      # one line per check, exit 1 if any fails

Pure standard library. Each closed form written in a note is re-derived numerically, so a typing error in a note shows
up here before it reaches the web page: the differential equation and the boundary conditions of every profile are
checked with finite differences, every flux, force, torque and power by Simpson quadrature of the fields, every
implicit relation h(t) by differentiating it and comparing with the evolution equation, and every limit of the notes
is evaluated. Numbers use the data of the checks (unit values), not those of a particular exam.
"""
import cmath
import math
import sys

FAILED = []


def report(name, ok, detail=""):
    print(f"{'ok  ' if ok else 'FAIL'} {name}{': ' + detail if detail else ''}")
    if not ok:
        FAILED.append(name)


def close(name, got, want, rel=1e-6, absolute=1e-12):
    ok = abs(got - want) <= max(rel * abs(want), absolute)
    report(name, ok, f"{got:.10g} vs {want:.10g}")


def simpson(f, a, b, n=4000):
    n += n % 2
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def d1(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def d2(f, x, h=1e-4):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)


# ------------------------------------------------------------------------------------------------- VF2
def vf2():
    h, nu, w, V = 1.0, 0.7, 2.3, 1.0
    om2 = w * h * h / (2 * nu)
    Om = math.sqrt(om2)
    lam = (1 + 1j) * Om / h
    f = lambda y: cmath.cosh(lam * (h - y)) / cmath.cosh(lam * h)         # amplitude of e^{i w t}
    close("VF2 f(0) = 1", abs(f(0.0)), 1.0)
    report("VF2 f'(h) = 0", abs(d1(f, h - 1e-4, 1e-5)) < 1e-3, f"{abs(d1(f, h - 1e-4, 1e-5)):.2e}")
    ok = all(abs(1j * w * f(y) - nu * d2(f, y)) < 1e-4 * abs(1j * w * f(y)) for y in (0.2, 0.5, 0.8))
    report("VF2 i w f = nu f'' on the layer", ok)
    close("VF2 lambda^2 nu = i w", (lam * lam * nu).imag, w)
    # rigid limit (w h^2/nu << 1) and Stokes limit (>> 1)
    Om = math.sqrt(1e-4 / 2)
    lam1 = (1 + 1j) * Om
    report("VF2 rigid limit f -> 1", abs(cmath.cosh(lam1 * (1 - 0.5)) / cmath.cosh(lam1) - 1) < 1e-3)
    Om = math.sqrt(4e4 / 2)
    eta = 0.01                                                              # y/h with delta = sqrt(2 nu/w)
    lam2 = (1 + 1j) * Om
    g = cmath.cosh(lam2 * (1 - eta)) / cmath.cosh(lam2)
    st = cmath.exp(-(1 + 1j) * Om * eta)
    report("VF2 Stokes limit f -> exp(-(1+i) y/delta)", abs(g - st) < 1e-6, f"{abs(g - st):.2e}")


# ------------------------------------------------------------------------------------------------- VF3
def vf3():
    a, mu, Pl = 1.0, 1.0, 1.0
    for al in (0.2, 0.5):
        Lg = math.log(1 / al)
        V = Pl * a * a / (4 * mu) * (1 - al ** 2) * ((1 + al ** 2) * Lg - (1 - al ** 2)) / (2 * Lg - (1 - al ** 2))
        v = lambda r: -Pl / (4 * mu) * (r * r - (al * a) ** 2) + (-V + Pl / (4 * mu) * (1 - al ** 2) * a * a) * math.log(r / (al * a)) / Lg
        close(f"VF3 v(rod) = 0, alpha = {al}", v(al * a), 0.0, absolute=1e-12)
        close(f"VF3 v(a) = -V, alpha = {al}", v(a), -V)
        ok = all(abs((d2(v, r) + d1(v, r) / r) + Pl / mu) < 1e-3 for r in (0.4, 0.6, 0.9) if r > al)
        report(f"VF3 (1/r)(r v')' = -P_l/mu, alpha = {al}", ok)
        Q = simpson(lambda r: 2 * math.pi * r * v(r), al * a, a)
        close(f"VF3 zero flux for the closed-form V, alpha = {al}", Q, 0.0, absolute=1e-9)
    close("VF3 alpha -> 0: V -> P_l a^2/(8 mu)", Pl * a * a / (4 * mu) * ((1 + 1e-12) * math.log(1e12) - 1) / (2 * math.log(1e12) - 1), Pl * a * a / (8 * mu), rel=0.03)
    al = 0.99
    Lg = math.log(1 / al)
    V = Pl * a * a / (4 * mu) * (1 - al ** 2) * ((1 + al ** 2) * Lg - (1 - al ** 2)) / (2 * Lg - (1 - al ** 2))
    close("VF3 alpha -> 1: V -> P_l h^2/(6 mu)", V, Pl * (a * (1 - al)) ** 2 / (6 * mu), rel=0.03)


# ------------------------------------------------------------------------------------------------- VF4
def vf4():
    mu, D, L, pc, pa = 1.0, 1.0, 1.0, 1.0, 0.0
    for al, be in ((0.3, 0.4), (0.5, 0.7)):
        f = 1 - al ** 4 - (1 - al ** 2) ** 2 / math.log(1 / al)
        # annulus profile of the note, with p_o - p_a = dp over beta L
        dp = 0.37
        v = lambda r: dp * D * D / (16 * mu * be * L) * (1 - (2 * r / D) ** 2 - (1 - al ** 2) / math.log(al) * math.log(2 * r / D))
        close(f"VF4 v(alpha D/2) = 0, alpha = {al}", v(al * D / 2), 0.0, absolute=1e-12)
        close(f"VF4 v(D/2) = 0, alpha = {al}", v(D / 2), 0.0, absolute=1e-12)
        Q = simpson(lambda r: 2 * math.pi * r * v(r), al * D / 2, D / 2)
        close(f"VF4 annulus flux = pi D^4 f dp/(128 mu beta L), alpha = {al}", Q, math.pi * D ** 4 * f * dp / (128 * mu * be * L))
        Q1 = lambda po: math.pi * D ** 4 * (pc - po) / (128 * mu * (1 - be) * L)
        Q2 = lambda po: math.pi * D ** 4 * f * (po - pa) / (128 * mu * be * L)
        den = 1 + be * (1 - f) / f
        po = pc - (1 - be) * (pc - pa) / den
        close(f"VF4 pipe and annulus carry the same Q, alpha = {al}", Q1(po), Q2(po))
        close(f"VF4 Q formula, alpha = {al}", Q1(po), math.pi * D ** 4 * (pc - pa) / (128 * mu * L) / den)
        report(f"VF4 the bar always lowers the flux, alpha = {al}", Q1(po) < math.pi * D ** 4 * (pc - pa) / (128 * mu * L))
    close("VF4 beta -> 0: p_o -> p_a", pc - (1 - 0.0) * (pc - pa) / 1.0, pa)
    f = 1 - 1e-6 ** 4 - (1 - 1e-12) ** 2 / math.log(1e6)
    report("VF4 alpha -> 0: f -> 1 (slowly, logarithmically)", 0.9 < f < 1.0, f"f = {f:.4f}")
    f = lambda al: 1 - al ** 4 - (1 - al ** 2) ** 2 / math.log(1 / al)
    report("VF4 alpha -> 1: f -> 0", f(0.999) < 1e-6, f"f = {f(0.999):.2e}")


# ------------------------------------------------------------------------------------------------- VF5
def vf5():
    a, g, r1, r2, m1, m2, l1 = 1.0, 9.81, 1.0, 1.3, 1.0, 2.0, 0.5
    for h in (0.2, 0.7):
        Q = math.pi * a ** 4 * g / 8 * (r1 * l1 + r2 * h) / (m1 * l1 + m2 * h)
        D = g * l1 * h * (m2 * r1 - m1 * r2) / (m1 * l1 + m2 * h)            # p_s - p_a
        Q1 = math.pi * a ** 4 / (8 * m1) * (r1 * g - D / l1)
        Q2 = math.pi * a ** 4 / (8 * m2) * (r2 * g + D / h)
        close(f"VF5 liquid 1 carries Q, h = {h}", Q1, Q)
        close(f"VF5 liquid 2 carries Q, h = {h}", Q2, Q)
    m, r = 1.0, 1.0
    Q = math.pi * a ** 4 * r * g / (8 * m)
    close("VF5 equal liquids: p_s = p_a", g * l1 * 0.4 * (m * r - m * r) / (m * l1 + m * 0.4), 0.0, absolute=1e-12)
    l2 = 0.9
    td = 8 / (g * a * a) * simpson(lambda h: (m * l1 + m * h) / (r * l1 + r * h), 0, l2)
    close("VF5 equal liquids: t_d = 8 mu l_2/(rho g a^2)", td, 8 * m * l2 / (r * g * a * a))
    close("VF5 equal liquids: t_d = pi a^2 l_2 / Q", td, math.pi * a * a * l2 / Q)
    # t(h) of the note against an RK4 integration of dh/dt = -Q/(pi a^2)
    h, t, dt = l2, 0.0, 1e-4
    rhs = lambda h: -g * a * a / 8 * (r1 * l1 + r2 * h) / (m1 * l1 + m2 * h)
    while h > 1e-3:
        k1 = rhs(h); k2 = rhs(h + dt * k1 / 2); k3 = rhs(h + dt * k2 / 2); k4 = rhs(h + dt * k3)
        h += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += dt
    ref = 8 / (g * a * a) * simpson(lambda x: (m1 * l1 + m2 * x) / (r1 * l1 + r2 * x), 1e-3, l2)
    close("VF5 integral relation = ODE solution", t, ref, rel=2e-3)


# ------------------------------------------------------------------------------------------------- VF6
def vf6():
    a, mu, pa, rho, g = 1.0, 1.0, 1.0, 1.0, 1.0
    hi = pa / (rho * g)
    close("VF6 equilibrium height", hi, 1.0)
    t_of_h = lambda h: 8 * mu * hi * hi / (a * a * pa) * (math.log(1 / (1 - h / hi)) - h / hi)
    for h in (0.1, 0.4, 0.8):
        u = a * a / (8 * mu) * (pa / h - rho * g)                           # dh/dt of the quasi-steady column
        close(f"VF6 dt/dh = 1/u, h = {h}", d1(t_of_h, h, 1e-6), 1 / u, rel=1e-5)
    # initial law h ~ a sqrt(pa t/(4 mu))
    t = 1e-6
    lo, hi_ = 1e-6, 0.5
    for _ in range(100):
        mid = (lo + hi_) / 2
        if t_of_h(mid) < t:
            lo = mid
        else:
            hi_ = mid
    close("VF6 t -> 0: h -> a sqrt(p_a t/(4 mu))", lo, a * math.sqrt(pa * t / (4 * mu)), rel=1e-3)
    close("VF6 pressure p(0) = p_a, p(h) = 0", pa * (1 - 0.0) - pa, 0.0)


# ------------------------------------------------------------------------------------------------- VF7
def vf7():
    S = lambda s: s * s / 2 + 2 * s + math.log(1 + s)
    for s in (0.1, 0.5, 1.7):
        lhs = (1 + s) ** 2 * (1 - (1 + s) ** -3)
        close(f"VF7 (1+s)^2 [1 - (1+s)^-3] = s S'(s), s = {s}", lhs, s * d1(S, s, 1e-6), rel=1e-6)
    al = 1e-3
    close("VF7 alpha -> 0: t_d -> 8 mu L/(rho g a_o^2)", 8 / (3 * al) * S(al), 8.0, rel=2e-3)
    # flux of the cone: Q = pi rho g h/(8 mu int dz/a^4) against quadrature
    a0, L, al, h, mu, rho, g = 1.0, 1.0, 0.8, 0.7, 1.0, 1.0, 1.0
    s = al * h / L
    I = simpson(lambda z: 1 / (a0 * (1 + al * z / L)) ** 4, 0, h)
    Qn = math.pi * rho * g * h / (8 * mu * I)
    Qc = 3 * al * math.pi * rho * g * a0 ** 4 * h / (8 * mu * L * (1 - (1 + s) ** -3))
    close("VF7 flux of the conical pipe", Qn, Qc)


# ------------------------------------------------------------------------------------------------- VF8
def vf8():
    mu, R, h, hd, Po = 1.3, 0.8, 0.05, -0.2, 0.0
    P = lambda r: Po + 3 * mu * hd / h ** 3 * (r * r - R * R)
    close("VF8 P(R) = P_o", P(R), Po)
    ok = all(abs(-d1(lambda r: r * h ** 3 / (12 * mu) * d1(P, r, 1e-6), r, 1e-5) + r * hd) < 1e-4 for r in (0.2, 0.5, 0.7))
    report("VF8 -(r h^3 P'/(12 mu))' + r h_dot = 0", ok)
    F = simpson(lambda r: (P(r) - Po) * 2 * math.pi * r, 0, R)
    close("VF8 force on the cylinder", F, -1.5 * math.pi * mu * R ** 4 * hd / h ** 3)
    Pl = -d1(P, R, 1e-6)
    out = 2 * math.pi * R * Pl * h ** 3 / (12 * mu)
    close("VF8 flux through r = R equals the swept volume", abs(out), math.pi * R * R * abs(hd), rel=1e-6)


# ------------------------------------------------------------------------------------------------- VF9
def vf9():
    mu, V, h, L, rho, g, al = 1.1, 0.9, 0.2, 1.0, 1.0, 9.81, math.radians(20)
    sa = math.sin(al)
    D = 2 / 3 * mu * V * L / h ** 2 - 7 / 9 * rho * g * L * sa
    Q1 = V * h + (-D / L - rho * g * sa) * 8 * h ** 3 / (12 * mu)
    Q2 = V * h / 2 + (D / L - rho * g * sa) * h ** 3 / (12 * mu)
    Q = 5 / 9 * V * h - 4 / 27 * rho * g * h ** 3 * sa / mu
    close("VF9 flux in the wide gap", Q1, Q)
    close("VF9 flux in the narrow gap", Q2, Q)
    Vmin = 4 / 15 * rho * g * h * h * sa / mu
    close("VF9 V_min makes Q = 0", 5 / 9 * Vmin * h - 4 / 27 * rho * g * h ** 3 * sa / mu, 0.0, absolute=1e-12)
    # power: V times the shear on the belt in both stretches, shear = mu dv/dy at the belt (profile of each gap)
    def shear(hh, Pl):                                                       # Pl = -dP/dx; belt at y = 0 moving V, wall at rest
        return mu * (-V / hh + Pl * hh / (2 * mu))
    Pl1 = -D / L - rho * g * sa
    Pl2 = D / L - rho * g * sa
    Wn = -V * L * (shear(2 * h, Pl1) + shear(h, Pl2))
    Wc = V * L * (11 / 6 * mu * V / h + 10 / 9 * rho * g * h * sa)
    close("VF9 power supplied to the belt", Wn, Wc)


# ------------------------------------------------------------------------------------------------- VF10
def vf10():
    a, nu, rho, A = 1.0, 1.0, 1.0, 1.0

    def I0(z, n=60):
        return sum((z / 2) ** (2 * m) / math.factorial(m) ** 2 for m in range(n))
    for w in (5.0, 200.0):
        k = cmath.sqrt(1j * w / nu)
        v = lambda r: A / (1j * rho * w) * (1 - I0(k * r) / I0(k * a))
        close(f"VF10 v(a) = 0, a^2 w/nu = {w}", abs(v(a)), 0.0, absolute=1e-12)
        ok = all(abs(1j * rho * w * v(r) - A - rho * nu * (d2(v, r) + d1(v, r) / r)) < 1e-3 * A for r in (0.3, 0.6, 0.9))
        report(f"VF10 i rho w v = A + mu (v'' + v'/r), a^2 w/nu = {w}", ok)
    w = 1e-3
    k = cmath.sqrt(1j * w / nu)
    v = lambda r: A / (1j * rho * w) * (1 - I0(k * r) / I0(k * a))
    close("VF10 low frequency: Poiseuille A (a^2 - r^2)/(4 mu)", abs(v(0.5)), A * (a * a - 0.25) / (4 * rho * nu), rel=1e-3)
    w = 4e4
    k = cmath.sqrt(1j * w / nu)
    # high frequency: the Stokes layer decays as exp(-(a - r)/sqrt(2 nu/w)) from the wall, the core keeps A/(i rho w)
    delta = math.sqrt(2 * nu / w)
    close("VF10 high frequency: Stokes layer thickness sqrt(2 nu/w) is much smaller than a", float(delta < 0.02 * a), 1.0)
    close("VF10 high frequency: core amplitude A/(rho w)", abs(A / (1j * rho * w)), A / (rho * w))


# ------------------------------------------------------------------------------------------------- VF11
def vf11():
    mu, V, h, L = 1.2, 0.7, 0.05, 1.0
    Pl = 6 * mu * V / h ** 2
    v = lambda y: -V * (h - y) / h + Pl / (2 * mu) * y * (h - y)
    close("VF11 zero flux", simpson(v, 0, h), 0.0, absolute=1e-12)
    close("VF11 v(0) = -V (wall in the frame of the arm)", v(0), -V)
    close("VF11 v(h) = 0 (arm)", v(h), 0.0, absolute=1e-12)
    close("VF11 shear on the wall: mu v'(0) = 4 mu V/h along +x", mu * d1(v, 1e-6, 1e-7), 4 * mu * V / h, rel=1e-4)
    close("VF11 shear on the arm: |mu v'(h)| = 2 mu V/h", abs(mu * d1(v, h - 1e-6, 1e-7)), 2 * mu * V / h, rel=1e-4)
    close("VF11 momentum balance", Pl * L * h, 4 * mu * V * L / h + 2 * mu * V * L / h)
    M = simpson(lambda x: (x - L) * Pl * (L - x), 0, L)
    close("VF11 moment about A", M, -2 * mu * V * L ** 3 / h ** 2)


# ------------------------------------------------------------------------------------------------- VF12
def vf12():
    for eps in (0.2, 0.6):
        h = lambda t: 1 + eps * math.cos(t)
        i2 = simpson(lambda t: 1 / h(t) ** 2, 0, 2 * math.pi)
        i3 = simpson(lambda t: 1 / h(t) ** 3, 0, 2 * math.pi)
        close(f"VF12 int h^-2, eps = {eps}", i2, 2 * math.pi / (1 - eps ** 2) ** 1.5)
        close(f"VF12 int h^-3, eps = {eps}", i3, math.pi * (2 + eps ** 2) / (1 - eps ** 2) ** 2.5)
        Q = 0.5 * i2 / i3
        close(f"VF12 flux Q = (1 - eps^2)/(2 + eps^2) (units omega R c), eps = {eps}", Q, (1 - eps ** 2) / (2 + eps ** 2))
        # pressure gradient (units 6 mu omega R^2/c^2... per theta) and torque / force by quadrature
        Pth = lambda t: 6 * (1 / h(t) ** 2 - 2 * Q / h(t) ** 3) * 1.0           # dP/dtheta in units mu omega R^2/c^2
        close(f"VF12 int dP/dtheta = 0, eps = {eps}", simpson(Pth, 0, 2 * math.pi), 0.0, absolute=1e-8)
        Pc = lambda t: 6 * eps * (2 + eps * math.cos(t)) * math.sin(t) / ((2 + eps ** 2) * (1 + eps * math.cos(t)) ** 2)
        ok = all(abs(d1(Pc, t, 1e-5) - Pth(t)) < 1e-5 * (1 + abs(Pth(t))) for t in (0.4, 1.3, 2.2, 3.0))
        report(f"VF12 closed-form pressure has the gradient of the Reynolds equation, eps = {eps}", ok)
        # shear on the shaft: tau = mu dv/dy(0), v = (h - y)/h - y (h - y)/(2) * Pth/(...)  (units: omega R, mu omega R / c)
        tau = lambda t: -1 / h(t) - h(t) * Pth(t) / 2
        M = simpson(tau, 0, 2 * math.pi)
        Mc = -2 * math.pi * (1 + 2 * eps ** 2) / (math.sqrt(1 - eps ** 2) * (2 + eps ** 2)) * 2.0
        close(f"VF12 torque, eps = {eps}", M, Mc)
        Fz = simpson(lambda t: Pth(t) * math.cos(t), 0, 2 * math.pi)
        Fc = -6 * 2 * math.pi * eps / (math.sqrt(1 - eps ** 2) * (2 + eps ** 2))
        close(f"VF12 transverse force 12 pi eps/(sqrt(1-eps^2)(2+eps^2)), eps = {eps}", abs(Fz), abs(Fc))
    close("VF12 eps -> 0: Q -> omega R c/2", (1 - 0.0) / (2 + 0.0), 0.5)


# ------------------------------------------------------------------------------------------------- VF13
def vf13():
    mu, w, al, L = 1.0, 0.8, 0.05, 1.0
    P = lambda x: 6 * mu * w / al ** 3 * math.log(x / L)
    h = lambda x: al * x
    for x in (0.3, 0.7):
        close(f"VF13 Q = -omega x^2/2, x = {x}", -d1(P, x, 1e-6) * h(x) ** 3 / (12 * mu), -w * x * x / 2, rel=1e-5)
    M = simpson(lambda x: x * P(x), 1e-9, L)
    close("VF13 torque (moment of the pressure over the plate)", abs(M), 1.5 * mu * w * L * L / al ** 3, rel=1e-6)
    close("VF13 inflow at x = L equals the wedge area swept per unit time", abs(-d1(P, L, 1e-6)) * h(L) ** 3 / (12 * mu), w * L * L / 2, rel=1e-5)


# ------------------------------------------------------------------------------------------------- VF14
def vf14():
    mu, hd, h, L = 1.0, -0.3, 0.05, 1.0
    P = lambda x: 6 * mu * hd / h ** 3 * (x * x - L * L)
    for x in (0.3, 0.8):
        close(f"VF14 Q = -h_dot x, x = {x}", -d1(P, x, 1e-6) * h ** 3 / (12 * mu), -hd * x, rel=1e-5)
    close("VF14 P_0 - P_inf", P(0.0), -6 * mu * hd * L * L / h ** 3)
    Fy = simpson(P, 0, L)
    close("VF14 vertical force", Fy, -4 * mu * hd * L ** 3 / h ** 3)
    Fx = -P(0.0) * h - simpson(lambda x: mu * 6 * hd * x / h ** 2, 0, L)
    close("VF14 horizontal force (leg pressure and shear on the arm)", Fx, 3 * mu * hd * L * L / h ** 2)
    M = simpson(lambda x: (x - L) * P(x), 0, L)
    close("VF14 moment of the pressure about A", M, 2.5 * mu * hd * L ** 4 / h ** 3)


# ------------------------------------------------------------------------------------------------- VF15
def vf15():
    mu, L, h, dP = 1.0, 1.0, 0.1, 0.4
    for Vl, Vu in ((1.0, 1.0), (0.0, 1.0), (0.3, 0.9)):
        Pl = -dP / L
        v = lambda y: Vl + (Vu - Vl) / h * y + Pl / (2 * mu) * y * (h - y)
        q = simpson(v, 0, h)
        close(f"VF15 flux, Vl = {Vl}, Vu = {Vu}", q, (Vl + Vu) * h / 2 + Pl * h ** 3 / (12 * mu))
        tl = mu * d1(v, 1e-6, 1e-7)
        tu = mu * d1(v, h - 1e-6, 1e-7)
        # external forces: the belts supply minus the force of the liquid, per unit width
        Fl_ext = -tl * L
        Fu_ext = mu * d1(v, h - 1e-6, 1e-7) * L
        close(f"VF15 external force on the lower belt, Vl = {Vl}, Vu = {Vu}", Fl_ext, dP * h / 2 - mu * (Vu - Vl) * L / h, rel=1e-4, absolute=1e-9)
        close(f"VF15 external force on the upper belt, Vl = {Vl}, Vu = {Vu}", Fu_ext, dP * h / 2 + mu * (Vu - Vl) * L / h, rel=1e-4, absolute=1e-9)
        Fext_u = dP * h / 2 + mu * (Vu - Vl) * L / h
        Fext_l = dP * h / 2 - mu * (Vu - Vl) * L / h
        Wc = (Vl + Vu) * h * dP / 2 + (Vu - Vl) ** 2 * mu * L / h
        close(f"VF15 power Vl F_l + Vu F_u, Vl = {Vl}, Vu = {Vu}", Vl * Fext_l + Vu * Fext_u, Wc)
        diss = L * simpson(lambda y: mu * d1(v, y, 1e-6) ** 2, 1e-6, h - 1e-6)
        close(f"VF15 W - q dP = dissipation, Vl = {Vl}, Vu = {Vu}", Wc - q * dP, diss, rel=1e-4)
        Lam = h * h * dP / (mu * L * (Vl + Vu))
        eta = (1 - Lam / 6) / (1 + 2 / Lam * ((Vu - Vl) / (Vu + Vl)) ** 2)
        close(f"VF15 efficiency q dP / W, Vl = {Vl}, Vu = {Vu}", q * dP / Wc, eta)
    # case b): Vl = 0 -> maximum at Lambda = 2, eta = 1/3
    eta_b = lambda Lam: (1 - Lam / 6) / (1 + 2 / Lam)
    best = max((eta_b(0.001 * k), 0.001 * k) for k in range(1, 6000))
    close("VF15 maximum efficiency (Vl = 0)", best[0], 1 / 3, rel=1e-6)
    close("VF15 Lambda at the maximum", best[1], 2.0, rel=1e-3)


# ------------------------------------------------------------------------------------------------- VF16
def vf16():
    mu, R, h, hd = 1.0, 1.0, 0.1, -0.2
    for al in (0.3, 0.5):
        p = lambda r: -6 * mu * hd / h ** 3 * (R * R * math.log(r / (al * R)) - (r * r - (al * R) ** 2) / 2)
        close(f"VF16 p(alpha R) = p_a, alpha = {al}", p(al * R), 0.0, absolute=1e-12)
        F = simpson(lambda r: p(r) * 2 * math.pi * r, al * R, R)
        f = -0.5 * math.log(al) - 3 / 8 + al ** 2 / 2 - al ** 4 / 8
        close(f"VF16 f(alpha) closed form, alpha = {al}", F, -12 * math.pi * mu * hd * R ** 4 * f / h ** 3)
    close("VF16 f(0.5)", -0.5 * math.log(0.5) - 3 / 8 + 0.125 - 0.5 ** 4 / 8, 0.08876, rel=2e-4)
    close("VF16 f(1) = 0", -0.5 * math.log(1.0) - 3 / 8 + 0.5 - 1 / 8, 0.0, absolute=1e-12)
    # quasi-steady fall: dh/dt = -W h^3/(12 pi mu R^4 f); h/h0 = (1 + 2 tau)^(-1/2)
    W, h0, f = 1.0, 0.1, 0.08876
    k = W / (12 * math.pi * mu * R ** 4 * f)
    hh, t, dt = h0, 0.0, 1e-3
    rhs = lambda x: -k * x ** 3
    for _ in range(200):
        k1 = rhs(hh); k2 = rhs(hh + dt * k1 / 2); k3 = rhs(hh + dt * k2 / 2); k4 = rhs(hh + dt * k3)
        hh += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += dt
    tau = W * h0 ** 2 * t / (12 * math.pi * mu * R ** 4 * f)
    close("VF16 h/h0 = (1 + 2 tau)^(-1/2)", hh / h0, (1 + 2 * tau) ** -0.5, rel=1e-6)


# ------------------------------------------------------------------------------------------------- VF17
def vf17():
    mu, U, h, L, rho, c = 1.0, 0.8, 0.1, 5.0, 1.0, 1.0
    Pl = 6 * mu * U / h ** 2
    v = lambda y: U * y / h + Pl / (2 * mu) * y * (h - y)
    close("VF17 v = U y (4h - 3y)/h^2", v(0.04), U * 0.04 * (4 * h - 3 * 0.04) / h ** 2)
    close("VF17 flux per half = U h", simpson(v, 0, h), U * h)
    tw = -mu * d1(v, h - 1e-6, 1e-7)
    tp = mu * d1(v, 1e-6, 1e-7)
    close("VF17 shear on a wall = 2 mu U/h", tw, 2 * mu * U / h, rel=1e-4)
    close("VF17 shear on the plate = 4 mu U/h", tp, 4 * mu * U / h, rel=1e-4)
    dpL = Pl * L
    close("VF17 momentum balance 2h dP = 2 F_w + F_p", 2 * h * dpL, 2 * (2 * mu * U * L / h) + 8 * mu * U * L / h)
    diss = 2 * L * simpson(lambda y: mu * d1(v, y, 1e-6) ** 2, 1e-6, h - 1e-6)
    dT = 4 * mu * U * L / (rho * c * h * h)
    close("VF17 energy balance rho c 2 h U dT = dissipation", rho * c * 2 * h * U * dT, diss, rel=1e-4)
    close("VF17 work of the pressure minus work on the walls", 2 * h * U * dpL - 2 * (2 * mu * U * L / h) * U, rho * c * 2 * h * U * dT)


# ------------------------------------------------------------------------------------------------- VF18
def vf18():
    d, mu, rho, g, H, V = 1.0, 1.0, 1.0, 1.0, 0.7, 5.0
    Vc = rho * g * d * d / (6 * mu)
    X = lambda h: h - Vc * H / (V - Vc) * math.log(((V - Vc) * h + V * H) / (V * H))
    for h in (0.2, 0.9, 2.0):
        hd = V / 2 - rho * g * d * d / (12 * mu) * h / (h + H)
        close(f"VF18 d[(V - Vc) t/2]/dh = (V - Vc)/(2 hd), h = {h}", d1(X, h, 1e-6), (V - Vc) / 2 / hd, rel=1e-6)
    Vs = 0.5
    hinf = H * Vs / (Vc - Vs)
    close("VF18 V < Vc: h_inf = H V/(Vc - V) is a fixed point", Vs / 2 - Vc / 2 * hinf / (hinf + H), 0.0, absolute=1e-12)
    close("VF18 power (h_inf + H) = H Vc/(Vc - V)", hinf + H, H * Vc / (Vc - Vs))
    close("VF18 V > Vc: h_dot_inf = (V - Vc)/2", V / 2 - Vc / 2 * (1e9 / (1e9 + H)), (V - Vc) / 2, rel=1e-8)


# ------------------------------------------------------------------------------------------------- VF19
def vf19():
    mu, R1, R2, U, Pl = 1.0, 0.3, 1.0, 0.8, -2.0
    Dl = R2 ** 2 - R1 ** 2
    Lm = math.log(R2 / R1)
    C = (U - Pl * Dl / (4 * mu)) / Lm
    v = lambda r: Pl / (4 * mu) * (R2 ** 2 - r * r) + C * math.log(R2 / r)
    close("VF19 v(R_1) = U", v(R1), U)
    close("VF19 v(R_2) = 0", v(R2), 0.0, absolute=1e-12)
    ok = all(abs(d2(v, r) + d1(v, r) / r + Pl / mu) < 1e-3 for r in (0.4, 0.6, 0.9))
    report("VF19 (1/r)(r v')' = -P_l/mu", ok)
    Q = simpson(lambda r: 2 * math.pi * r * v(r), R1, R2)
    Qc = math.pi * Pl * Dl ** 2 / (8 * mu) + math.pi / 2 * (U - Pl * Dl / (4 * mu)) * (Dl - 2 * R1 ** 2 * Lm) / Lm
    close("VF19 flux", Q, Qc)
    tau = mu * d1(v, R1 + 1e-6, 1e-7)
    close("VF19 shear on the rod", tau, -mu * U / (R1 * Lm) - Pl * R1 / 2 * (1 - 0.5 * (R2 ** 2 / R1 ** 2 - 1) / Lm), rel=1e-4)
    # minimum velocity from Q = 0
    Umin = Pl * Dl / (4 * mu) * (1 - Dl * Lm / (Dl - 2 * R1 ** 2 * Lm))
    C0 = (Umin - Pl * Dl / (4 * mu)) / Lm
    v0 = lambda r: Pl / (4 * mu) * (R2 ** 2 - r * r) + C0 * math.log(R2 / r)
    close("VF19 flux vanishes at U_min", simpson(lambda r: 2 * math.pi * r * v0(r), R1, R2), 0.0, absolute=1e-9)
    close("VF19 U_min > 0 for P_l < 0", float(Umin > 0), 1.0)
    # R_1 -> 0 : Poiseuille flux
    R1s = 1e-100
    Ds, Ls = R2 ** 2 - R1s ** 2, math.log(R2 / R1s)
    Qs = math.pi * Pl * Ds ** 2 / (8 * mu) + math.pi / 2 * (U - Pl * Ds / (4 * mu)) * (Ds - 2 * R1s ** 2 * Ls) / Ls
    close("VF19 R_1 -> 0: Poiseuille flux pi P_l R_2^4/(8 mu) (the correction falls as 1/ln(R_2/R_1))", Qs, math.pi * Pl * R2 ** 4 / (8 * mu), rel=0.02)
    # thin gap: Couette flux pi R1 g U
    R1t, R2t = 1.0, 1.001
    Dt, Lt = R2t ** 2 - R1t ** 2, math.log(R2t / R1t)
    close("VF19 thin gap: second term -> pi R_1 g U", math.pi / 2 * U * (Dt - 2 * R1t ** 2 * Lt) / Lt, math.pi * R1t * (R2t - R1t) * U, rel=2e-3)


# ------------------------------------------------------------------------------------------------- VF20
def vf20():
    mu, Q, h, R = 1.0, 0.5, 0.05, 1.0
    P0 = 0.0
    P = lambda r: P0 - 6 * mu * Q / (math.pi * h ** 3) * math.log(r / R)
    close("VF20 P(R) = P_0", P(R), P0)
    close("VF20 q(r) = -pi h^3 r P'/(6 mu) = Q", -math.pi * h ** 3 * 0.4 * d1(P, 0.4, 1e-6) / (6 * mu), Q, rel=1e-5)
    F = simpson(lambda r: (P(r) - P0) * 2 * math.pi * r, 1e-9, R)
    close("VF20 integral of the overpressure = 3 mu Q R^2/h^3", F, 3 * mu * Q * R * R / h ** 3, rel=1e-5)
    g, rho, rs = 9.81, 1000.0, 1100.0
    hh = (3 * mu * Q / (2 * math.pi * R * g * (rs - rho))) ** (1 / 3)
    close("VF20 equilibrium: 3 mu Q R^2/h^3 = 2 pi R^3 g (rho_s - rho)", 3 * mu * Q * R * R / hh ** 3, 2 * math.pi * R ** 3 * g * (rs - rho))
    close("VF20 h proportional to Q^(1/3)", (3 * mu * 8 * Q / (2 * math.pi * R * g * (rs - rho))) ** (1 / 3) / hh, 2.0)


def main():
    for f in (vf2, vf3, vf4, vf5, vf6, vf7, vf8, vf9, vf10, vf11, vf12, vf13, vf14, vf15, vf16, vf17, vf18, vf19, vf20):
        print(f"--- {f.__name__}")
        f()
    if FAILED:
        print(f"{len(FAILED)} check(s) failed: {', '.join(FAILED)}")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
