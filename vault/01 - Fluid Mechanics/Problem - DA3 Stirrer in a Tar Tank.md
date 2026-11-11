---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - semejanza-fisica
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA3.pdf"
id: "da3"
pill: "DA3: Tar stirrer"
sheets:
  - 3
tags_html:
  - "Π theorem"
  - "Froude and Reynolds"
  - "Change of fluid"
---

# Problem DA3: Stirrer in a Tar Tank

> Official dimensional-analysis sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem (Notes.pdf, Eq. 6.25) and full physical similarity (Eqs. 6.57-6.59), made possible by changing the working fluid.

## Statement

A large container of diameter $D = 10$ m contains a volume $V = 1000$ m$^3$ of tar ($\nu_t = 10^{-3}$ m$^2$/s, $\rho_t = 2\times 10^3$ kg/m$^3$). To avoid solidification, the tar is continuously moved with a 3-blade stirrer of height $h = 1$ m placed at its bottom, which rotates with angular velocity $\Omega = 1$ s$^{-1}$, as shown in the figure. Design a small experiment with a geometrically similar model to determine the power $W$ needed to operate the stirrer. In particular,

- Use the Π theorem to reduce the parametric dependence of $W$.
- By using water in the experiment as working fluid, obtain the values of $D_e$, $h_e$, $V_e$ y $\Omega_e$ required to guarantee that the experiment is physically similar to the prototype.
- Obtain the ratio $W/W_e$ between the power measured in the experiment $W_e$ and that required to move the stirrer of the real prototype.

The sheet writes "y", Spanish for "and", in the second question.

![[attachments/FM-T6/da3-statement.svg]]
*Statement figure (redrawn from DA3.pdf, section view): a container of diameter D holding a volume V of tar, free surface at p_a, with a 3-blade stirrer of height h at its bottom rotating at Ω; gravity g downward*

Source: DA3.pdf (page 1, statement and handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; physical similarity, Eqs. 6.57-6.59.

## Hypotheses, Data and Dimensional Table

- The tar has a free surface at $p = p_a$ that the stirrer deforms, so gravity enters through that boundary condition (Notes.pdf, p. 66); the viscosity of tar is large, so viscosity enters too.
- Geometry: the tank diameter $D$, the stirrer height $h$ and the volume $V$ (which fixes the depth of tar); the blade shape is fixed by geometric similarity.
- Water in the model: $\nu_w = 10^{-6}$ m$^2$/s, $\rho_w = 10^3$ kg/m$^3$, so $\mu_w = 10^{-3}$ kg/(m s). Tar: $\mu_t = \rho_t\nu_t = 2\times 10^3\times 10^{-3} = 2$ kg/(m s).

| Parameter | Dimensions | Prototype |
| :--- | :--- | :--- |
| $W$ (unknown) | $ML^2T^{-3}$ | ? |
| $\Omega$ | $T^{-1}$ | 1 s$^{-1}$ |
| $g$ | $LT^{-2}$ | 9.81 m/s$^2$ |
| $h$ | $L$ | 1 m |
| $D$ | $L$ | 10 m |
| $V$ | $L^3$ | 1000 m$^3$ |
| $\rho$ | $ML^{-3}$ | $2\times 10^3$ kg/m$^3$ |
| $\mu$ | $ML^{-1}T^{-1}$ | 2 kg/(m s) |

## Application of the Π Theorem

$$ W = W(\Omega, g, h, D, V, \rho, \mu) $$

$n = 7$. The key takes $(\mu, \Omega, h)$ as the independent set, natural for a very viscous liquid (Notes.pdf, p. 68). Rows $\Omega$, $h$, $\mu$; columns $L$, $M$, $T$:

$$ \begin{pmatrix} 0 & 0 & -1 \\ 1 & 0 & 0 \\ -1 & 1 & -1 \end{pmatrix}, \qquad \det = (-1)\cdot\left(1\cdot 1 - 0\cdot(-1)\right) = -1 \neq 0 $$

(expanding along the first row), so $k = 3$ and $n - k = 4$ groups remain.

**Power.** $[W] = [\mu]^a[\Omega]^b[h]^c$: $M:\; 1 = a$; $T:\; -3 = -a - b$; $L:\; 2 = -a + c$; so $a = 1$, $b = 2$, $c = 3$: $\Pi_0 = W/(\mu\Omega^2 h^3)$.

**Gravity.** $[g] = [\Omega]^b[h]^c$: $T:\; -2 = -b$; $L:\; 1 = c$: the group $g/(\Omega^2 h)$, an inverse Froude number squared.

**Geometry.** $D/h$ and $V/h^3$.

**Density.** $[\rho] = [\mu]^a[\Omega]^b[h]^c$: $M:\; 1 = a$; $T:\; 0 = -a - b$, so $b = -1$; $L:\; -3 = -a + c$, so $c = -2$: $\rho/(\mu\Omega^{-1}h^{-2}) = \rho\Omega h^2/\mu$, a Reynolds number.

$$ \frac{W}{\mu\Omega^2 h^3} = f\left(\frac{g}{\Omega^2 h}, \frac{D}{h}, \frac{V}{h^3}, \frac{\rho\Omega h^2}{\mu}\right) $$

## Physical Similarity with Water

All four groups must be equal in model ($e$, water) and prototype ($t$, tar), with the same $g$:

$$ \frac{g}{\Omega^2 h} = \frac{g}{\Omega_e^2 h_e} \;\Longrightarrow\; \frac{h_e}{h} = \left(\frac{\Omega}{\Omega_e}\right)^2 $$

$$ \frac{\Omega h^2}{\nu_t} = \frac{\Omega_e h_e^2}{\nu_w} \;\Longrightarrow\; \left(\frac{h_e}{h}\right)^2 = \frac{\Omega}{\Omega_e}\,\frac{\nu_w}{\nu_t} $$

$$ \frac{D}{h} = \frac{D_e}{h_e}, \qquad \frac{V}{h^3} = \frac{V_e}{h_e^3} $$

The first two fix the scale and the speed. From the first, $\Omega/\Omega_e = (h_e/h)^{1/2}$; into the second:

$$ \left(\frac{h_e}{h}\right)^2 = \left(\frac{h_e}{h}\right)^{1/2}\frac{\nu_w}{\nu_t} \;\Longrightarrow\; \left(\frac{h_e}{h}\right)^{3/2} = \frac{\nu_w}{\nu_t} \;\Longrightarrow\; \frac{h_e}{h} = \left(\frac{\nu_t}{\nu_w}\right)^{-2/3} = \left(10^{3}\right)^{-2/3} = 10^{-2} $$

$$ h_e = 10^{-2}\times 1 = 1\ \text{cm}, \qquad \frac{\Omega_e}{\Omega} = \left(\frac{h}{h_e}\right)^{1/2} = \left(\frac{\nu_t}{\nu_w}\right)^{1/3} = 10 \;\Longrightarrow\; \Omega_e = 10\ \text{s}^{-1} $$

$$ D_e = \frac{h_e}{h}\,D = 10^{-2}\times 10 = 10\ \text{cm}, \qquad V_e = \left(\frac{h_e}{h}\right)^3 V = 10^{-6}\times 1000 = 10^{-3}\ \text{m}^3 = 1\ \text{litre} $$

This is the way out of the Reynolds-Froude incompatibility of DA1: the model fluid must satisfy $\nu_w/\nu_t = (h_e/h)^{3/2}$, and water does it for a 1:100 model of a tank of tar.

Check of both groups: prototype $\Omega h^2/\nu_t = 1\times 1/10^{-3} = 10^3$, model $\Omega_e h_e^2/\nu_w = 10\times 10^{-4}/10^{-6} = 10^3$; prototype $g/(\Omega^2 h) = 9.81$, model $9.81/(100\times 0.01) = 9.81$.

## Power Ratio

With all groups equal, $\Pi_0$ is equal:

$$ \frac{W}{\mu_t\Omega^2 h^3} = \frac{W_e}{\mu_w\Omega_e^2 h_e^3} \;\Longrightarrow\; \frac{W}{W_e} = \frac{\mu_t}{\mu_w}\left(\frac{\Omega}{\Omega_e}\right)^2\left(\frac{h}{h_e}\right)^3 = \frac{\rho_t}{\rho_w}\,\frac{\nu_t}{\nu_w}\left(\frac{\Omega}{\Omega_e}\right)^2\left(\frac{h}{h_e}\right)^3 $$

$$ \frac{W}{W_e} = 2\times 10^{3}\times\left(10^{-1}\right)^2\times\left(10^{2}\right)^3 = 2\times 10^{3}\times 10^{-2}\times 10^{6} = 2\times 10^{7} $$

## Answers and Checks

- Reduced law: $W/(\mu\Omega^2 h^3) = f\left(g/(\Omega^2 h),\, D/h,\, V/h^3,\, \rho\Omega h^2/\mu\right)$.
- Model in water: $h_e = 1$ cm, $D_e = 10$ cm, $V_e = 1$ litre, $\Omega_e = 10$ s$^{-1}$.
- Power ratio: $W/W_e = 2\times 10^7$.
- Dimensions: $\mu\Omega^2h^3$ is $ML^{-1}T^{-1}\cdot T^{-2}\cdot L^3 = ML^2T^{-3}$, a power.
- Consistency: the same ratio follows from $\rho\Omega^3h^5$ as power scale (the other choice of the independent set): $(\rho_t/\rho_w)(\Omega/\Omega_e)^3(h/h_e)^5 = 2\times 10^{-3}\times 10^{10} = 2\times 10^7$.
- Check against the official key: DA3.pdf gives $h_e = 1$ cm, $\Omega_e = 10$ s$^{-1}$, $D_e = 10$ cm, $V_e = 1$ litre and $W/W_e = 2\times 10^7$.
