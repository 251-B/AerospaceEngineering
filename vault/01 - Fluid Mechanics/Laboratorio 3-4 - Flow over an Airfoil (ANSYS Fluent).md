---
materia: Fluid Mechanics
tipo: laboratorio
tema: Laboratory 3-4 - 2D flow around a NACA 2410 airfoil (ANSYS Fluent)
tags:
  - fluid-mechanics
  - laboratory
  - cfd
  - airfoil
  - spalart-allmaras
dificultad: intermedia
fuentes:
  - sources/cuatrimestre-1/01-fluid-mechanics/laboratorios/lab-3&4/wing2d_fluent_tutorial_updated6.pdf
  - sources/cuatrimestre-1/01-fluid-mechanics/laboratorios/lab-3&4/NACA2410_commas.txt
---

# Laboratory 3–4: 2D Flow around an Airfoil (ANSYS Fluent)

> **Navigation:** [[Fluid Mechanics MOC]]. Report deliverables and Fluent data: `sources/cuatrimestre-1/01-fluid-mechanics/laboratorios/lab-3&4/Lab-Ismael/`. Laboratory material is not published on the web.

## Setup and Governing Model (`wing2d_fluent_tutorial_updated6.pdf`, pp. 3–13)

Steady, incompressible 2D RANS flow around a fixed **NACA 2410** airfoil ($c = 1\text{ m}$, maximum camber $m = 0.02$ at $p = 0.4$, thickness $0.10c$) inside a rectangular control volume $x \in [-10, 30]\text{ m}$, $y \in [-10, 10]\text{ m}$ ($26\,902$ cells; $971$ airfoil wall edges of median length $2.08\times 10^{-3}\text{ m}$; 14-layer boundary-layer inflation with first-layer height $2.0\times 10^{-4}\text{ m}$, growth rate $1.2$).

Fluid properties (standard air in Fluent): $\rho = 1.225\text{ kg/m}^3$, $\mu = 1.7894\times 10^{-5}\text{ kg/(m\cdot s)}$, free-stream speed $U = 10\text{ m/s}$ ($M \approx 0.03 < 0.3$), giving dynamic pressure $q_\infty = \tfrac{1}{2}\rho U^2 = 61.25\text{ Pa}$ and chord Reynolds number:

$$Re_c = \frac{\rho U c}{\mu} = \frac{1.225 \times 10 \times 1}{1.7894\times 10^{-5}} \approx 6.85\times 10^5$$

- **Boundary conditions:** `inlet` (left, top and bottom boundaries) with velocity components $u = U\cos\alpha$, $v = U\sin\alpha$ and turbulent viscosity ratio $\mu_t/\mu = 10$; `outlet` (right boundary) at $p_{\text{gauge}} = 0\text{ Pa}$; `wing` as stationary no-slip wall.
- **Solver:** double-precision pressure-based coupled RANS with the **Spalart-Allmaras** one-equation turbulence model, Second-Order Upwind momentum discretisation, hybrid initialisation, and residual tolerances $10^{-6}$ (`continuity`, `x-velocity`, `y-velocity`) and $10^{-3}$ (`nut`).
- **Force projection (pp. 3–4, 13, 19):** net surface force $\mathbf{F} = \oint_{\Sigma_{\text{wing}}} (\boldsymbol{\tau}'\cdot\hat{\mathbf{n}} - p\hat{\mathbf{n}})\,ds = F_x\mathbf{e}_x + F_y\mathbf{e}_y$ projected onto lift and drag directions ($A_p = b c = 1\text{ m}^2$ per unit span):

$$F_L = -F_x\sin\alpha + F_y\cos\alpha, \qquad F_D = F_x\cos\alpha + F_y\sin\alpha, \qquad C_L = \frac{F_L}{\tfrac{1}{2}\rho U^2 A_p}, \qquad C_D = \frac{F_D}{\tfrac{1}{2}\rho U^2 A_p}$$

## Inviscid Thin-Airfoil Reference (Extension: Anderson, Ch. 4)

With the Glauert substitution $x/c = \tfrac{1}{2}(1 - \cos\theta)$ and the piecewise parabolic NACA 2410 camber slope $dz_c/dx = (2m/p^2)(p - x/c)$ for $x/c < p$ and $(2m/(1-p)^2)(p - x/c)$ for $x/c \ge p$:

$$\alpha_{L0} = -\frac{1}{\pi}\int_0^\pi \frac{dz_c}{dx}(\cos\theta - 1)\,d\theta = -2.077^\circ \approx -2.08^\circ, \qquad C_{L,\text{thin}}(\alpha) = 2\pi(\alpha - \alpha_{L0})$$

## Numerical Results (`plots_lab3.py`, `fluent_aoa*.txt`, `pcoeff_aoa*.txt`)

| $\alpha$ ($^\circ$) | Iterations | $C_L$ (Fluent) | $C_{L,\text{thin}}$ | $(C_L - C_{L,\text{thin}})/C_{L,\text{thin}}$ | $C_D$ (Fluent) | $C_{p,\min}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $3$ | $73$ | $0.5210$ | $0.5568$ | $-6.4\%$ | $0.0129$ | $-0.931$ |
| $6$ | $75$ | $0.8246$ | $0.8858$ | $-6.9\%$ | $0.0150$ | $-2.379$ |
| $9$ | $82$ | $1.1025$ | $1.2148$ | $-9.2\%$ | $0.0201$ | $-4.762$ |
| $10$ | $87$ | $1.1850$ | $1.3244$ | $-10.5\%$ | $0.0225$ | $-5.685$ |
| $12$ | $104$ | $1.3206$ | $1.5437$ | $-14.5\%$ | $0.0292$ | $-7.614$ |
| $16$ *(extra, 1000 max)* | $258$ | $1.3016$ | $1.9823$ | $-34.3\%$ | $0.0765$ | $-9.430$ |

- At $\alpha = 6^\circ$, stagnation sits just under the leading edge ($x/c \simeq 0.0076$, $p_{\max} = 60.8\text{ Pa}$, $C_{p,\max} = 0.993$) and the upper-nose suction peak reaches $-145.7\text{ Pa}$ ($U_e \approx 18.4\text{ m/s}$).
- Over $3^\circ\text{--}9^\circ$, the RANS lift-curve slope is $0.097\text{ deg}^{-1}$ against $2\pi\text{ rad}^{-1} = 0.110\text{ deg}^{-1}$; although finite thickness ($10\%$) slightly raises the inviscid slope above $2\pi$, viscous boundary-layer thickening on the suction side (together with finite-domain and mesh discretisation effects) outweighs it and bends $C_L(\alpha)$ downward.
- At $\alpha = 16^\circ$, $C_L$ falls to $1.3016$ (below the highest sampled value $1.3206$ at $12^\circ$), total $C_D$ rises $\times 2.6$ from $0.0292$ to $0.0765$ (pressure drag $C_{D,p}$ jumps from $0.0224$ to $0.0718$ while viscous drag $C_{D,v}$ drops from $0.0068$ to $0.0047$ in `fluent_aoa12.txt` vs `fluent_aoa16.txt`), and the upper-surface $C_p$ flattens near $-0.38$ over $x/c \in [0.6, 0.95]$, indicating trailing-edge boundary-layer separation and stall between $12^\circ$ and $16^\circ$.
