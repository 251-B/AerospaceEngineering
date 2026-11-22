"""Plots 5 and 6 of the Lab 3-4 report (NACA 2410, Fluent, Spalart-Allmaras).

fig5_cp_aoa3_6_9.pdf : Cp along the airfoil for AoA = 3, 6, 9 deg (pcoeff_aoaN.txt written by Fluent)
fig6_cl_vs_aoa.pdf   : CL from Fluent vs AoA, with thin-airfoil theory for the same camber line
"""
import math, re
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3})

def read_cp(a):
    pts = [tuple(map(float, l.split())) for l in open(f"pcoeff_aoa{a}.txt") if re.match(r"^-?\d", l)]
    return np.array(pts)

# CL printed by Reports > Forces (Direction Vector = (-sin a, cos a)), see fluent_aoaN.txt / fluent_transcript2.txt
CL = {}
for a in (3, 9, 10, 12):  # the 16 deg extra is not part of plot 6
    lines = [l for l in open(f"fluent_aoa{a}.txt") if l.startswith("wing ")]
    CL[a] = float(lines[-1].split()[-1])  # last 'wing' row = direction-vector table, last column = total coefficient
CL[6] = 0.82458338  # fluent_transcript2.txt (6 deg run)

# --- Plot 5: Cp(x/c), suction side and pressure side together, -Cp up as usual for airfoils
fig, ax = plt.subplots(figsize=(7.5, 4.6))
for a, c in ((3, "tab:blue"), (6, "tab:orange"), (9, "tab:green")):
    d = read_cp(a)
    ax.plot(d[:, 0], d[:, 1], ".", ms=2.5, color=c, label=fr"$\alpha = {a}^\circ$")
ax.invert_yaxis()
ax.set_xlabel(r"$x/c$")
ax.set_ylabel(r"$C_p$")
ax.legend()
fig.tight_layout(); fig.savefig("fig5_cp_aoa3_6_9.pdf"); fig.savefig("fig5_cp_aoa3_6_9.png", dpi=200)

# --- Thin-airfoil theory for the NACA 2410 camber line (m = 0.02, p = 0.4):
# alpha_L0 = -(1/pi) * int_0^pi dz/dx (cos th - 1) dth,  CL = 2 pi (alpha - alpha_L0)
m, p = 0.02, 0.4
th = np.linspace(1e-6, math.pi - 1e-6, 200001)
x = 0.5 * (1 - np.cos(th))
dzdx = np.where(x < p, 2 * m / p**2 * (p - x), 2 * m / (1 - p) ** 2 * (p - x))
aL0 = -np.trapezoid(dzdx * (np.cos(th) - 1), th) / math.pi
assert abs(math.degrees(aL0) + 2.08) < 0.05, aL0  # known value for NACA 24xx, about -2.1 deg

A = sorted(CL)
fig, ax = plt.subplots(figsize=(7.5, 4.6))
ax.plot(A, [CL[a] for a in A], "o-", color="tab:red", label="Fluent (Spalart-Allmaras)")
aa = np.linspace(0, 16, 50)
ax.plot(aa, 2 * math.pi * (np.radians(aa) - aL0), "--", color="k",
        label=fr"Thin-airfoil theory, $2\pi(\alpha-\alpha_{{L0}})$, $\alpha_{{L0}}={math.degrees(aL0):.2f}^\circ$")
ax.set_xlabel(r"$\alpha$ (deg)")
ax.set_ylabel(r"$C_L$")
ax.legend()
fig.tight_layout(); fig.savefig("fig6_cl_vs_aoa.pdf"); fig.savefig("fig6_cl_vs_aoa.png", dpi=200)

for a in A:
    print(f"{a:>3} deg  CL = {CL[a]:.4f}   theory = {2*math.pi*(math.radians(a)-aL0):.4f}")
print(f"alpha_L0 = {math.degrees(aL0):.3f} deg")
