---
materia: Fluid Mechanics
tipo: laboratorio
tema: Laboratory 2 - 1D advection-diffusion equation (CFD)
tags:
  - fluid-mechanics
  - laboratory
  - cfd
  - advection-diffusion
  - finite-differences
dificultad: intermedia
fuentes:
  - sources/cuatrimestre-1/01-fluid-mechanics/laboratorios/lab-2/Guidelines.pdf
  - sources/cuatrimestre-1/01-fluid-mechanics/laboratorios/lab-2/MatlabCodeReference.m
---

# Laboratory 2: 1D Advection-Diffusion Equation (FTCS)

> **Navigation:** [[Fluid Mechanics MOC]]. Individual report (one A4 page): `sources/cuatrimestre-1/01-fluid-mechanics/laboratorios/lab-2/Lab-Ismael/`. Laboratory material is not published on the web.

## Problem (Guidelines.pdf, Eqs. 1-6)

$$\frac{\partial f}{\partial t}+U\frac{\partial f}{\partial x}=\alpha\frac{\partial^2 f}{\partial x^2},\qquad f(x,0)=\operatorname{sech}^2[k(x+2)],\quad x\in[-10,10],\ 0\le t\le 20$$

All quantities are dimensionless. Boundary conditions: Dirichlet $f(\pm10,t)=0$, Neumann $\partial_x f(\pm10,t)=0$, periodic. FTCS scheme, stable under Eq. (6): $U\Delta t/\Delta x\le 1/2$ and $\alpha\Delta t/\Delta x^2\le 1/2$.

## Discrete scheme (Eqs. 10-12)

Interior nodes, with $C=U\Delta t/\Delta x$ and $D=\alpha\Delta t/\Delta x^2$:

$$f_i^{n+1}=f_i^n-\frac{C}{2}\left(f_{i+1}^n-f_{i-1}^n\right)+D\left(f_{i+1}^n-2f_i^n+f_{i-1}^n\right)$$

- Neumann (ghost nodes $f_0=f_2$, $f_{N_x+1}=f_{N_x-1}$): the centred advective difference vanishes, so $f_1^{n+1}=f_1^n+2D(f_2^n-f_1^n)$ and $f_{N_x}^{n+1}=f_{N_x}^n+2D(f_{N_x-1}^n-f_{N_x}^n)$.
- Periodic (ghost nodes $f_0=f_{N_x-1}$, $f_{N_x+1}=f_2$): nodes $1$ and $N_x$ use the neighbours $f_2$ and $f_{N_x-1}$ in the same stencil.

## Stability extension (not in the guidelines)

Modified equation of FTCS: $f_t+Uf_x=(\alpha-U^2\Delta t/2)f_{xx}$. Von Neumann analysis gives $D\le1/2$ and $C^2\le2D$, that is $\Delta t\le 2\alpha/U^2$. With $\Delta t=\Delta x/(2U)$ this fails for $U/\alpha>4/\Delta x=40$, so Eq. (6) alone is not enough for $U\gg\alpha$.

## Results (script `Lab2AdvDiffEq.m`, $k=0.5$, $N_x=201$)

- Report case $U=1$, $\alpha=0.1$: $\Delta t=0.05$, $C=D=0.5$. Peak at $x\simeq-1$ ($t=1$) and $x\simeq3$ ($t=5$). At $t=15$ the periodic pulse is at $x\simeq-7$ ($13-20$), and the Neumann pulse leaves through $x=10$ ($M$ drops from 3.9987 to 0.034). Periodic mass is conserved ($M=3.9987$).
- Item 4 sweep (periodic, $t=5$): $U=10$, $\alpha=0.1$ gives $\max f=0.99$, peak transported; $U=0.1$, $\alpha=10$ gives an almost flat profile ($\max f=0.20$). Advection displaces the pulse by $Ut$, diffusion spreads it by $\sqrt{2\alpha t}$.
