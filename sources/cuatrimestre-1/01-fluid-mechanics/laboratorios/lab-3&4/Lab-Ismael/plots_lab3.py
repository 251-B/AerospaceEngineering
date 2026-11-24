"""Plots 5 and 6 of the Lab 3-4 report (NACA 2410, Fluent, Spalart-Allmaras).

fig5_cp_aoa3_6_9.pdf : Cp along the airfoil for AoA = 3, 6, 9 deg (pcoeff_aoaN.txt written by Fluent)
fig6_cl_vs_aoa.pdf   : CL from Fluent vs AoA (3, 6, 9, 10, 12 deg), with thin-airfoil theory
"""
from pathlib import Path
import math
import re
import numpy as np
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3})


def read_cp_loop(a: int) -> np.ndarray:
    """Read Fluent XY-plot node data and stitch the 4 MPI wall partitions into one closed loop."""
    with open(BASE / f"pcoeff_aoa{a}.txt", encoding="utf-8") as fh:
        pts = [tuple(map(float, ln.split())) for ln in fh if re.match(r"^\s*-?\d", ln)]
    chunks, cur = [], [pts[0]]
    for pt in pts[1:]:
        if abs(pt[0] - cur[-1][0]) > 0.05:
            chunks.append(cur)
            cur = [pt]
        else:
            cur.append(pt)
    chunks.append(cur)

    ordered = list(chunks.pop(0))
    while chunks:
        head, tail = ordered[0], ordered[-1]
        for i, ch in enumerate(chunks):
            if math.hypot(ch[0][0] - tail[0], ch[0][1] - tail[1]) < 1e-4:
                ordered.extend(ch[1:])
                chunks.pop(i)
                break
            if math.hypot(ch[-1][0] - tail[0], ch[-1][1] - tail[1]) < 1e-4:
                ordered.extend(reversed(ch[:-1]))
                chunks.pop(i)
                break
            if math.hypot(ch[-1][0] - head[0], ch[-1][1] - head[1]) < 1e-4:
                ordered = list(ch[:-1]) + ordered
                chunks.pop(i)
                break
            if math.hypot(ch[0][0] - head[0], ch[0][1] - head[1]) < 1e-4:
                ordered = list(reversed(ch[1:])) + ordered
                chunks.pop(i)
                break
        else:
            raise ValueError(f"Unconnected partition chunk in pcoeff_aoa{a}.txt")

    if math.hypot(ordered[0][0] - ordered[-1][0], ordered[0][1] - ordered[-1][1]) < 1e-4:
        ordered.pop()
    assert len(ordered) == 971, f"Expected 971 unique wall nodes, got {len(ordered)}"
    arr = np.array(ordered)
    arr = np.roll(arr, -int(np.argmax(arr[:, 0])), axis=0)
    return np.vstack([arr, arr[0]])


def read_cl(a: int) -> float:
    """Extract total lift coefficient on 'wing' from Fluent's wall-forces transcript."""
    fname = "fluent_check6_saved.txt" if a == 6 else f"fluent_aoa{a}.txt"
    with open(BASE / fname, encoding="utf-8", errors="replace") as fh:
        lines = [ln for ln in fh if ln.strip().startswith("wing ")]
    return float(lines[-1].split()[-1])


CL = {a: read_cl(a) for a in (3, 6, 9, 10, 12)}
CL_16 = read_cl(16)
assert CL[12] > CL_16, "Expected stall drop at 16 deg"

# --- Plot 5: Cp(x/c), suction side and pressure side together, -Cp up as usual for airfoils
fig, ax = plt.subplots(figsize=(7.5, 4.5))
ax.axhline(0.0, color="0.55", lw=0.8, ls=":")
for a, col in ((3, "tab:blue"), (6, "tab:orange"), (9, "tab:green")):
    loop = read_cp_loop(a)
    ax.plot(loop[:, 0], loop[:, 1], "-", lw=1.5, color=col, label=fr"$\alpha = {a}^\circ$")
ax.invert_yaxis()
ax.set_xlim(-0.02, 1.02)
ax.set_xlabel(r"$x/c$ [-]")
ax.set_ylabel(r"$C_p$ [-]")
ax.legend(framealpha=0.95)
fig.tight_layout()
fig.savefig(BASE / "fig5_cp_aoa3_6_9.pdf", metadata={"CreationDate": None})
fig.savefig(BASE / "fig5_cp_aoa3_6_9.png", dpi=200)
plt.close(fig)

# --- Thin-airfoil theory for the NACA 2410 camber line (m = 0.02, p = 0.4):
# Exact closed-form integral: alpha_L0 = -(1/pi) * int_0^pi (dz/dx) (cos th - 1) dth
m, p = 0.02, 0.4
th_p = math.acos(1.0 - 2.0 * p)


def _camber_prim(th: float) -> float:
    a_c, b_c = p - 0.5, 0.5
    return -a_c * th + (a_c - b_c) * math.sin(th) + b_c * (0.5 * th + 0.25 * math.sin(2.0 * th))


aL0 = -((2.0 * m / p**2) * (_camber_prim(th_p) - _camber_prim(0.0))
        + (2.0 * m / (1.0 - p) ** 2) * (_camber_prim(math.pi) - _camber_prim(th_p))) / math.pi
assert abs(math.degrees(aL0) + 2.0772) < 1e-3, aL0

A = sorted(CL)
fig, ax = plt.subplots(figsize=(7.5, 4.5))
aa = np.linspace(0.0, 13.0, 100)
ax.plot(aa, 2.0 * math.pi * (np.radians(aa) - aL0), "--", color="k", lw=1.4,
        label=fr"Thin-airfoil theory, $2\pi(\alpha-\alpha_{{L0}})$, $\alpha_{{L0}}={math.degrees(aL0):.2f}^\circ$")
ax.plot(A, [CL[a] for a in A], "o-", color="tab:red", lw=1.6, ms=5.5,
        label="Fluent (Spalart-Allmaras)")
ax.set_xlim(-0.3, 13.0)
ax.set_xlabel(r"$\alpha$ (deg)")
ax.set_ylabel(r"$C_L$ [-]")
ax.legend(framealpha=0.95)
fig.tight_layout()
fig.savefig(BASE / "fig6_cl_vs_aoa.pdf", metadata={"CreationDate": None})
fig.savefig(BASE / "fig6_cl_vs_aoa.png", dpi=200)
plt.close(fig)

for a in A:
    cl_th = 2.0 * math.pi * (math.radians(a) - aL0)
    diff_pct = (CL[a] - cl_th) / cl_th * 100.0
    print(f"{a:>3} deg  CL = {CL[a]:.4f}   theory = {cl_th:.4f}   ({diff_pct:+.1f}%)")
print(f" 16 deg  CL = {CL_16:.4f}   (extra, 1000 iter max)")
print(f"alpha_L0 = {math.degrees(aL0):.3f} deg")
