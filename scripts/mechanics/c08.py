"""C08: Kepler orbit with e = 1/3, apsidal speeds, areal velocity, tangential impulse at perigee (bank item C08).

Independent route for (b): the apse radii of the new orbit are the roots of the radial energy equation
E = h^2/(2 r^2) - mu/r (zero radial velocity), with E and h computed from the state just after the impulse.
"""
import sympy as sp


def verify(chk):
    mu, rp = sp.symbols("mu r_p", positive=True)
    r = sp.symbols("r", positive=True)
    e = sp.Rational(1, 3)
    a = rp / (1 - e)
    ra = a * (1 + e)
    chk("a = 3 r_p / 2", a, 3 * rp / 2)
    chk("r_a = 2 r_p", ra, 2 * rp)
    vp = sp.sqrt(mu * (2 / rp - 1 / a))
    va = sp.sqrt(mu * (2 / ra - 1 / a))
    chk("v_p^2 = 4 mu / (3 r_p) = 2 mu / a", vp**2, 2 * mu / a)
    chk("v_a^2 = mu / (3 r_p)", va**2, mu / (3 * rp))
    chk("v_p / v_a = (1+e)/(1-e) = 2", vp / va, 2)
    chk("angular momentum r_p v_p = r_a v_a (vis-viva consistent)", rp * vp, ra * va)
    # areal velocity is h/2 at both apsides (constant)
    chk("areal velocity at perigee = areal velocity at apogee", rp * vp / 2, ra * va / 2)
    # radial-energy check of the original orbit: roots of E = h^2/(2r^2) - mu/r are r_p and r_a
    E0 = vp**2 / 2 - mu / rp
    h0 = rp * vp
    roots0 = sp.solve(sp.Eq(h0**2 / (2 * r**2) - mu / r, E0), r)
    chk.true("apse radii of the original orbit = {r_p, 2 r_p}", set(sp.simplify(x) for x in roots0) == {rp, 2 * rp})

    # (b) tangential impulse at perigee: speed v_p' = sqrt(9/8) v_p
    vpn = sp.sqrt(sp.Rational(9, 8)) * vp
    chk("v_p'^2 = 3 mu / (2 r_p)", vpn**2, 3 * mu / (2 * rp))
    chk.value("dv / v_p = sqrt(9/8) - 1 = 6.07 %", sp.sqrt(sp.Rational(9, 8)) - 1, 0.06066, tol=5e-5)
    En = vpn**2 / 2 - mu / rp
    hn = rp * vpn
    roots = sp.solve(sp.Eq(hn**2 / (2 * r**2) - mu / r, En), r)
    chk.true("apse radii after the impulse = {r_p, 3 r_p}", set(sp.simplify(x) for x in roots) == {rp, 3 * rp})
    chk("eps' = -mu/(4 r_p)", En, -mu / (4 * rp))
    chk("h'^2 = 3/2 mu r_p", hn**2, sp.Rational(3, 2) * mu * rp)
    chk("r^2 (h'^2/(2r^2) - mu/r - eps') = (mu/(4 r_p)) (r - r_p)(r - 3 r_p)",
        sp.expand(r**2 * (hn**2 / (2 * r**2) - mu / r - En)), sp.expand((mu / (4 * rp)) * (r - rp) * (r - 3 * rp)))
    chk("escape: v^2 = 2 mu/r_p gives eps = 0", (2 * mu / rp) / 2 - mu / rp, 0)
    an = -mu / (2 * En)
    chk("new semi-major axis a' = 2 r_p", an, 2 * rp)
    chk("new eccentricity e' = 1/2", (3 * rp - rp) / (3 * rp + rp), sp.Rational(1, 2))
    chk("vis-viva on the new orbit at r_p", vpn**2, mu * (2 / rp - 1 / an))
    chk.true("v_p' > circular speed sqrt(mu/r_p): r_p stays the perigee", sp.simplify(vpn**2 - mu / rp) > 0)
    # velocity at the new apogee
    van = hn / (3 * rp)
    chk("v_a' = h'/(3 r_p): v_a'^2 = mu/(6 r_p)", van**2, mu / (6 * rp))
