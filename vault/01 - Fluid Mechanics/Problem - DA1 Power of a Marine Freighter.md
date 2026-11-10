---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - semejanza-fisica
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA1.pdf"
id: "da1"
pill: "DA1: Marine freighter"
sheets:
  - 1
tags_html:
  - "Π theorem"
  - "Froude similarity"
  - "Re ≫ 1"
---

# Problem DA1: Power of a Marine Freighter

> Official dimensional-analysis sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem (Notes.pdf, Eq. 6.25), the limit of negligible viscosity (Eq. 6.55) and physical similarity (Eqs. 6.57-6.59).

## Statement

We want to estimate the driving power $W$ necessary to move at a peak velocity $V = 10$ m/s a marine freighter of length $l = 100$ m and total mass at full load $m = 1000$ Tm. For that purpose, a small model of length $l_e = 1$ m, geometrically similar to the real ship, is to be tested on a hydraulic channel. To guide the design of the experiment, follow these steps:

1. Use the dimensional analysis to reduce the parametric dependence of the required power $W$.

2. Write the three equations that need to be satisfied to guarantee physical similarity between the experiment and the full-scale prototype. Verify that it is not possible to find the values of the mass $m_e$ and velocity $V_e$ of the experiment that satisfy simultaneously all three equations, so that complete physical similarity cannot be attained.

3. Assuming that the effect of viscosity on the fluid motion is negligible, determine the values of $m_e$ and $V_e$. Check that the corresponding values of the Reynolds number for both the real prototype and the experiment are indeed sufficiently large for the assumption of negligible viscosity to be a reasonable approximation.

4. If the experimental measurement of the power obtained with the experimental model is $W_e = 10$ W, obtain the value of the driving power $W$ needed to operate the real prototype at the required conditions.

Source: DA1.pdf (page 1, statement and handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; physical similarity, Eqs. 6.57-6.59.

## Hypotheses, Data and Dimensional Table

- The ship moves at constant velocity on the free surface of water, which is the same liquid in the channel and in the sea: $\rho_e = \rho$, $\mu_e = \mu$, so $\nu_e = \nu = \mu/\rho \simeq 10^{-6}$ m$^2$/s.
- The power goes into the waves made at the free surface (gravity $g$ matters, since the free surface is not flat; Notes.pdf, p. 66) and into the viscous drag ($\mu$ matters, a priori).
- The mass $m$ fixes how deep the hull floats: by Archimedes, the submerged volume is $m/\rho$.
- "Tm" is the metric ton: $m = 1000\ \text{t} = 10^6$ kg.

| Parameter | Meaning | Dimensions | Value (prototype) |
| :--- | :--- | :--- | :--- |
| $W$ | driving power (unknown) | $ML^2T^{-3}$ | ? |
| $V$ | ship velocity | $LT^{-1}$ | 10 m/s |
| $g$ | gravity | $LT^{-2}$ | 9.81 m/s$^2$ |
| $m$ | mass at full load | $M$ | $10^6$ kg |
| $l$ | ship length | $L$ | 100 m |
| $\rho$ | water density | $ML^{-3}$ | 1000 kg/m$^3$ |
| $\mu$ | water viscosity | $ML^{-1}T^{-1}$ | $10^{-3}$ kg/(m s) |

## Application of the Π Theorem

$$ W = W(V, g, m, l, \rho, \mu) $$

There are $n = 6$ governing parameters. Exponent matrix, rows $V$, $l$, $\rho$; columns $L$, $M$, $T$:

$$ \begin{pmatrix} 1 & 0 & -1 \\ 1 & 0 & 0 \\ -3 & 1 & 0 \end{pmatrix}, \qquad \det = 1\,(0\cdot 0 - 0\cdot 1) - 0 + (-1)\,(1\cdot 1 - 0\cdot(-3)) = -1 \neq 0 $$

so $(V, l, \rho)$ have independent dimensions and $k = 3$: there are $n - k = 3$ dimensionless parameters. $(V, l, \rho)$ is chosen because velocity, size and the inertia of the water clearly matter (Notes.pdf, p. 68).

**Power.** $[W] = [\rho]^a[V]^b[l]^c$:

$$ M:\; 1 = a, \qquad T:\; -3 = -b, \qquad L:\; 2 = -3a + b + c $$

so $a = 1$, $b = 3$ and $c = 2 + 3 - 3 = 2$: $\Pi_0 = W/(\rho V^3 l^2)$.

**Gravity.** $[g] = [V]^b[l]^c$ (no mass, so no $\rho$): $T:\; -2 = -b$, $L:\; 1 = b + c$, so $b = 2$, $c = -1$ and $g/(V^2/l)$ is dimensionless; its inverse is the square of the Froude number, $V^2/(gl)$.

**Mass.** $[m] = [\rho]^a[V]^b[l]^c$: $M:\; 1 = a$, $T:\; 0 = -b$, $L:\; 0 = -3a + b + c$, so $a = 1$, $b = 0$, $c = 3$: $m/(\rho l^3)$.

**Viscosity.** $[\mu] = [\rho]^a[V]^b[l]^c$: $M:\; 1 = a$, $T:\; -1 = -b$, $L:\; -1 = -3a + b + c$, so $a = 1$, $b = 1$, $c = 1$: $\mu/(\rho V l)$, the inverse of the Reynolds number.

$$ \frac{W}{\rho V^3 l^2} = f\left(\frac{V^2}{g l}, \frac{m}{\rho l^3}, \frac{\rho V l}{\mu}\right) $$

- $V^2/(gl)$ (Froude number squared): inertia against gravity, that is the waves at the free surface.
- $m/(\rho l^3)$: by Archimedes $m/\rho$ is the submerged volume, so this group is proportional to the ratio of the submerged volume to the total volume of the ship.
- $\rho V l/\mu$: the Reynolds number.

## Physical Similarity

Model (subscript $e$) and prototype are physically similar when the three governing groups are equal. With the same liquid and the same $g$:

$$ \frac{V^2}{g l} = \frac{V_e^2}{g l_e} \;\Longrightarrow\; V_e = \left(\frac{l_e}{l}\right)^{1/2} V $$

$$ \frac{V l}{\nu} = \frac{V_e l_e}{\nu} \;\Longrightarrow\; V_e = \frac{l}{l_e}\,V $$

$$ \frac{m}{\rho l^3} = \frac{m_e}{\rho l_e^3} \;\Longrightarrow\; m_e = \left(\frac{l_e}{l}\right)^3 m $$

The third equation fixes $m_e$. The first two ask for two different velocities: with $l_e/l = 10^{-2}$, Froude asks for $V_e = 10^{-1}V$ and Reynolds for $V_e = 10^{2}V$. Both hold only if $(l_e/l)^{1/2} = l/l_e$, that is $(l_e/l)^{3/2} = 1$, $l_e = l$: **with the same liquid, no scaled model can be fully similar** (Notes.pdf, p. 71: partial similarity).

## Negligible Viscosity

If viscosity has a negligible effect ($\mathrm{Re}\gg 1$), the group $\rho V l/\mu$ drops out of the law (Notes.pdf, Eq. 6.55):

$$ \frac{W}{\rho V^3 l^2} = f\left(\frac{V^2}{g l}, \frac{m}{\rho l^3}\right) $$

and only the Froude and mass conditions remain:

$$ V_e = \left(\frac{l_e}{l}\right)^{1/2} V = \left(\frac{1}{100}\right)^{1/2}\times 10 = 1\ \text{m/s}, \qquad m_e = \left(\frac{l_e}{l}\right)^3 m = 10^{-6}\times 10^{6} = 1\ \text{kg} $$

Check of the assumption, with $\nu = 10^{-6}$ m$^2$/s:

$$ \mathrm{Re} = \frac{V l}{\nu} = \frac{10\times 100}{10^{-6}} = 10^{9} \gg 1, \qquad \mathrm{Re}_e = \frac{V_e l_e}{\nu} = \frac{1\times 1}{10^{-6}} = 10^{6} \gg 1 $$

Both are very large, so neglecting viscosity is reasonable in the model and in the ship, even though the two Reynolds numbers differ by a factor $10^3$.

## Power of the Prototype

With the two remaining groups equal, $\Pi_0$ is equal too (Notes.pdf, Eq. 6.58):

$$ \frac{W}{\rho V^3 l^2} = \frac{W_e}{\rho V_e^3 l_e^2} \;\Longrightarrow\; W = \left(\frac{V}{V_e}\right)^3\left(\frac{l}{l_e}\right)^2 W_e $$

$$ W = (10)^3\,(100)^2 \times 10\ \text{W} = 10^{3}\times 10^{4}\times 10 = 10^{8}\ \text{W} = 100\ \text{MW} $$

## Answers and Checks

- Reduced law: $W/(\rho V^3 l^2) = f\left(V^2/(gl),\, m/(\rho l^3),\, \rho V l/\mu\right)$.
- Full similarity needs $V_e = (l_e/l)^{1/2}V$ and $V_e = (l/l_e)V$ at once: impossible for $l_e \neq l$.
- With negligible viscosity: $V_e = 1$ m/s, $m_e = 1$ kg; $\mathrm{Re} = 10^9$, $\mathrm{Re}_e = 10^6$.
- Prototype power: $W = 100$ MW.
- Dimensions: $\rho V^3 l^2$ has $ML^{-3}\cdot L^3T^{-3}\cdot L^2 = ML^2T^{-3}$, a power.
- Scaling check: under Froude similarity $V \propto l^{1/2}$, so $W \propto V^3 l^2 \propto l^{7/2}$, and $100^{7/2} = 10^7$ times 10 W is $10^8$ W, the same.
- Check against the official key: DA1.pdf gives $V_e = 1$ m/s, $m_e = 1$ kg, $\mathrm{Re}\simeq 10^9$, $\mathrm{Re}_e = 10^6$ and $W = 100$ MW, the same results.
