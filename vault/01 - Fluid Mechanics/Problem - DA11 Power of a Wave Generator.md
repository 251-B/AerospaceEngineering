---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - semejanza-fisica
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA11.pdf"
id: "da11"
pill: "DA11: Wave generator"
sheets:
  - 11
tags_html:
  - "Π theorem"
  - "Froude similarity"
  - "Re ≫ 1"
---

# Problem DA11: Power of a Wave Generator

> Official dimensional-analysis sheet of the course (exam of Jan 14, 2013), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem (Notes.pdf, Eq. 6.25), the limit of negligible viscosity (Eq. 6.55) and Froude similarity (Eqs. 6.57-6.59).

## Statement

**PROBLEM 3 (45 minutes)** The figure below illustrates a simple mechanism to generate periodic gravity waves in a pool of liquid (density $\rho$ and viscosity $\mu$), with undisturbed height $H$. The waves are driven by the harmonic motion of the lateral confining wall perpendicular to itself, with amplitude $A$ and frequency $\omega$.

![[attachments/FM-T6/da11-statement.svg]]
*Statement figure (redrawn from DA11.pdf): above, the pool of liquid (ρ, μ) of undisturbed depth H; below, the lateral wall moved harmonically, x = A cos(2πωt), by the power Ẇ, generating gravity waves*

1. (*4 points*). Use dimensional analysis to simplify the dependence of the power needed to drive the generator, $\dot{W}$, as a function of the governing parameters $(\rho, \mu, A, \omega, H, g)$.

2. (*1 point*). Simplify the resulting dimensionless function for the case of negligible viscous forces. In the remainder of the problem, assume that this condition is satisfied.

To characterize the requirements of a new wave generator to be installed in a large water channel (subindex p), a scale model (subindex m) with $H_m/H_p = 1/20$ is tested in the lab using water as working fluid. Knowing that the wave frequency required in the water channel is $\omega_p = 1/6$ s$^{-1}$,

3. (*2 points*). Determine the value of the frequency, $\omega_m$, that must be used in the experiments to guarantee physical similarity.

4. (*2 points*). If the power used in the model is $\dot{W}_m = 1$ Watt, obtain the power needed to drive the wave generator in the water channel, $\dot{W}_p$.

5. (*1 point*). Justify the hypothesis of negligible viscous forces. If needed, make a reasonable guess for the values of the involved variables.

Source: DA11.pdf (page 1: statement; page 2: handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; limits, Eq. 6.55; physical similarity, Eqs. 6.57-6.59.

## Hypotheses, Data and Dimensional Table

- Gravity waves at a free surface: $g$ is essential (Notes.pdf, p. 66). The wall motion $x = A\cos(2\pi\omega t)$ shows that $\omega$ is a frequency in cycles per second, $[\omega] = T^{-1}$.
- The model is geometrically similar (all lengths, the channel width included, scaled by $1/20$) and uses water, as the channel: same $\rho$, $\mu$, $g$.

| Parameter | Dimensions |
| :--- | :--- |
| $\dot{W}$ (unknown) | $ML^2T^{-3}$ |
| $\rho$ | $ML^{-3}$ |
| $\mu$ | $ML^{-1}T^{-1}$ |
| $A$, $H$ | $L$ |
| $\omega$ | $T^{-1}$ |
| $g$ | $LT^{-2}$ |

## Application of the Π Theorem

$$ \dot{W} = f(\rho, \mu, A, \omega, H, g) $$

$n = 6$. The key takes $(\rho, A, \omega)$: rows $\rho(-3, 1, 0)$, $A(1, 0, 0)$, $\omega(0, 0, -1)$ in $(L, M, T)$; expanding along the $\omega$ row, $\det = (-1)\cdot\left((-3)\cdot 0 - 1\cdot 1\right) = 1 \neq 0$, so $k = 3$ and three groups remain.

**Power.** $[\dot{W}] = [\rho]^a[\omega]^b[A]^c$: $M:\; 1 = a$; $T:\; -3 = -b$; $L:\; 2 = -3 + c$; so $\Pi_{\dot{W}} = \dot{W}/(\rho\omega^3A^5)$.

**Viscosity.** $[\mu] = [\rho]^a[\omega]^b[A]^c$: $M:\; 1 = a$; $T:\; -1 = -b$; $L:\; -1 = -3 + c$; so $\Pi_\mu = \mu/(\rho\omega A^2)$, the inverse of a Reynolds number with the wall velocity $\omega A$.

**Depth.** $\Pi_H = H/A$.

**Gravity.** $[g] = [\omega]^b[A]^c$: $T:\; -2 = -b$; $L:\; 1 = c$; so $\Pi_g = g/(\omega^2A)$.

$$ \Pi_{\dot{W}} = \Pi_{\dot{W}}(\Pi_\mu, \Pi_H, \Pi_g): \qquad \frac{\dot{W}}{\rho\omega^3A^5} = \Pi_{\dot{W}}\left(\frac{\mu}{\rho\omega A^2}, \frac{H}{A}, \frac{g}{\omega^2 A}\right) $$

## Negligible Viscous Forces

For $\Pi_\mu \to 0$ the group drops out (Notes.pdf, Eq. 6.55):

$$ \frac{\dot{W}}{\rho\omega^3A^5} = \Pi_{\dot{W}}\left(\frac{H}{A}, \frac{g}{\omega^2 A}\right) $$

## Physical Similarity

**Depth group.** Geometric similarity of the whole setup, amplitude included:

$$ \frac{H_p}{A_p} = \frac{H_m}{A_m} \;\Longrightarrow\; \frac{A_p}{A_m} = \frac{H_p}{H_m} = 20 $$

**Gravity group.** Same $g$:

$$ \frac{g}{\omega_p^2A_p} = \frac{g}{\omega_m^2A_m} \;\Longrightarrow\; \frac{\omega_m}{\omega_p} = \sqrt{\frac{A_p}{A_m}} = \sqrt{20} $$

$$ \omega_m = \sqrt{20}\times\frac{1}{6} = \frac{2\sqrt{5}}{6} = \frac{\sqrt{5}}{3}\ \text{s}^{-1} = 0.745\ \text{s}^{-1} $$

## Power of the Prototype

With $\Pi_H$ and $\Pi_g$ equal, $\Pi_{\dot{W}}$ is equal (same $\rho$):

$$ \frac{\dot{W}_p}{\rho\omega_p^3A_p^5} = \frac{\dot{W}_m}{\rho\omega_m^3A_m^5} \;\Longrightarrow\; \frac{\dot{W}_p}{\dot{W}_m} = \left(\frac{\omega_p}{\omega_m}\right)^3\left(\frac{A_p}{A_m}\right)^5 = \left(\frac{A_p}{A_m}\right)^{-3/2}\left(\frac{A_p}{A_m}\right)^5 = \left(\frac{A_p}{A_m}\right)^{7/2} $$

$$ \dot{W}_p = 20^{7/2}\times 1\ \text{W} = 20^3\times\sqrt{20}\ \text{W} = 8000\times 4.472 = 35\,777\ \text{W} = 35.78\ \text{kW} $$

## Negligible Viscosity: Justification

For water, $\rho = 10^3$ kg/m$^3$ and $\mu = 10^{-3}$ kg/(m s), so $\Pi_\mu = 10^{-6}/(\omega A^2)$ with $\omega$ in s$^{-1}$ and $A$ in m. The amplitudes are not given; reasonable guesses, as the key suggests:

- channel: $A_p \sim 1$ m, $\omega_p = 1/6$ s$^{-1}$, so $\Pi_\mu \sim 10^{-6}/(0.17\times 1) = 6\times 10^{-6} \ll 1$;
- model: $A_m = A_p/20 \sim 0.05$ m, $\omega_m = 0.745$ s$^{-1}$, so $\Pi_\mu \sim 10^{-6}/(0.745\times 0.0025) = 5\times 10^{-4} \ll 1$.

Viscous forces are negligible in both (large Reynolds numbers).

## Answers and Checks

- Reduced law: $\dot{W}/(\rho\omega^3A^5) = \Pi_{\dot{W}}\left(\mu/(\rho\omega A^2),\, H/A,\, g/(\omega^2A)\right)$; without viscosity, $\Pi_{\dot{W}}(H/A, g/(\omega^2A))$.
- Model frequency: $\omega_m = \sqrt{5}/3 = 0.745$ s$^{-1}$.
- Channel power: $\dot{W}_p = 20^{7/2}\,\dot{W}_m = 35.78$ kW.
- Dimensions: $\rho\omega^3A^5$ is $ML^{-3}\cdot T^{-3}\cdot L^5 = ML^2T^{-3}$, a power.
- Froude scaling: times scale as $\lambda^{1/2}$ and powers as $\lambda^{7/2}$ with $\lambda = 20$, as for the ship of DA1.
- Check against the official key: DA11.pdf gives $\omega_m = \sqrt{5}/3$ s$^{-1}$ and $\dot{W}_p = 20^{7/2}\dot{W}_m = 35.78$ kW, and justifies $\Pi_\mu \ll 1$ with $A \sim 1$ m, $\omega \sim 1$ s$^{-1}$.
