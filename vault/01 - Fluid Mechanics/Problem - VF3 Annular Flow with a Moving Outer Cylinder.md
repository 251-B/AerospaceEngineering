---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - flujo-anular
  - poiseuille-couette
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF3.pdf"
id: "vf3"
pill: "VF3: Annular flow"
sheets:
  - 3
tags_html:
  - "Annulus"
  - "Poiseuille + Couette"
  - "Zero flux"
---

# Problem VF3: Annular Flow with a Moving Outer Cylinder

> Official viscous-flow sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: steady unidirectional flow in cylindrical coordinates (Notes.pdf, Eqs. 7.7 and 7.13), with the two integration constants fixed by the no-slip conditions on both walls.

## Statement

A fluid of density $\rho$ and viscosity $\mu$ is confined between two infinitely long coaxial cylinders of radii $a$ and $\alpha a$, with $\alpha < 1$, aligned in the $x$ direction. The fluid is forced to move steadily due to the presence of a known reduced pressure gradient $P_l = -\partial P/\partial x$ and also due to the backward motion of the outer cylinder, with velocity $V$.

1. Determine the fluid velocity $v_x(r)$.

2. Obtain the power needed to move the outer cylinder.

3. Calculate the value of $V$ for which the volume flux in the pipe is identically zero.

![[attachments/FM-T7/vf3-statement.svg]]
*Statement figure (redrawn from VF3.pdf): liquid of density ρ and viscosity μ between a rod of radius αa and a cylinder of radius a, along x, driven by the pressure gradient P_l; the outer cylinder moves backward with velocity V*

Source: VF3.pdf (page 1, statement and handwritten key). Notes.pdf, Chapter 7: unidirectional flow, Eq. 7.7; steady flow in a circular pipe, Eqs. 7.13-7.16.

## Hypotheses, Data and Unknowns

- Steady, fully developed flow of a liquid with constant $\mu$: $\bar{v} = v_x(r)\bar{e}_x$ (Notes.pdf, Eq. 7.1, with axial symmetry); $P_l$ is a known constant (Notes.pdf, p. 74).
- The inner body, a rod of radius $\alpha a$, is at rest; the outer cylinder of radius $a$ moves backward, that is, with velocity $-V\bar{e}_x$.
- "Backward" means against the pressure-driven flow: $P_l > 0$ drives the liquid towards $+x$.
- The power is taken per unit length of cylinder, since the cylinders are infinitely long.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $a$, $\alpha a$ | outer and inner radius ($\alpha < 1$) | m |
| $P_l$ | reduced pressure gradient, $-\partial P/\partial x$ | Pa/m |
| $V$ | speed of the outer cylinder (towards $-x$) | m/s |
| $\mu$ | viscosity | kg/(m s) |

## Velocity Profile

Equation (7.7) in steady state, with the conditions at the two walls:

$$ 0 = P_l + \frac{\mu}{r}\frac{d}{dr}\left(r\frac{dv_x}{dr}\right); \qquad r = \alpha a:\; v_x = 0, \qquad r = a:\; v_x = -V $$

Multiplying by $r/\mu$ and integrating once: $r\,dv_x/dr = -P_l r^2/(2\mu) + C_1$. Dividing by $r$ and integrating again:

$$ v_x = -\frac{P_l}{4\mu}r^2 + C_1\ln r + C_2 $$

The term $C_1\ln r$ cannot be dropped: the axis is not part of the domain, so there is no regularity condition. It is convenient to write the solution with the inner wall as origin of the logarithm, $v_x = -\frac{P_l}{4\mu}\left(r^2 - \alpha^2a^2\right) + C\ln\frac{r}{\alpha a}$, which satisfies $v_x(\alpha a) = 0$ for any $C$. The outer wall fixes $C$:

$$ -V = -\frac{P_l}{4\mu}a^2\left(1 - \alpha^2\right) + C\ln\frac{1}{\alpha} \;\Longrightarrow\; C = \frac{-V + \dfrac{P_l}{4\mu}a^2\left(1 - \alpha^2\right)}{\ln\left(\alpha^{-1}\right)} $$

$$ v_x = -\frac{P_l}{4\mu}\left[r^2 - (\alpha a)^2\right] + \left[-V + \frac{P_l}{\mu}\frac{\left(1 - \alpha^2\right)a^2}{4}\right]\frac{\ln\left(r/\alpha a\right)}{\ln\left(\alpha^{-1}\right)} $$

Check: at $r = \alpha a$ the logarithm is zero and the bracket $r^2 - (\alpha a)^2$ vanishes; at $r = a$ the first term is $-P_la^2(1 - \alpha^2)/(4\mu)$ and the second is $-V + P_la^2(1 - \alpha^2)/(4\mu)$, whose sum is $-V$.

## Power Needed to Move the Outer Cylinder

The force per unit area of the liquid on the outer wall is $\tau_p = \bar{\bar{\tau}}'\cdot\bar{n}$ with $\bar{n}$ pointing from the wall into the liquid, $\bar{n} = -\bar{e}_r$, so $\tau_p = -\mu\left(\partial v_x/\partial r\right)_{r=a}$ (the convention of (7.16)). Differentiating,

$$ \frac{dv_x}{dr} = -\frac{P_l}{2\mu}r + \frac{C}{r} \;\Longrightarrow\; \tau_p = \frac{P_la}{2} - \frac{\mu C}{a} = \frac{P_la}{2} - \frac{\mu}{a}\,\frac{-V + \dfrac{P_l}{4\mu}a^2\left(1 - \alpha^2\right)}{\ln\left(\alpha^{-1}\right)} $$

$$ \tau_p = \frac{P_la}{2}\left[1 - \frac{1 - \alpha^2}{2\ln\left(\alpha^{-1}\right)}\right] + \frac{\mu V}{a\ln\left(\alpha^{-1}\right)} $$

The liquid pushes the cylinder with the force $2\pi a\,\tau_p$ per unit length, in the direction $+x$. The external agent that moves the cylinder at velocity $-V\bar{e}_x$ must balance it, with the force $-2\pi a\,\tau_p\,\bar{e}_x$, so the power it supplies per unit length is force times velocity:

$$ W = \left(-2\pi a\tau_p\right)(-V) = \tau_p\,V\,2\pi a $$

(power per unit length of cylinder, in W/m).

## Zero Volume Flux

The flux through the annulus is $Q = \int_{\alpha a}^{a}2\pi r\,v_x\,dr$. With $G = P_l/(4\mu)$, $b = \alpha a$, $\mathcal{L} = \ln(\alpha^{-1})$ and the two integrals (Barrow's rule):

$$ \int_b^a r\left(r^2 - b^2\right)dr = \left[\frac{r^4}{4} - \frac{b^2r^2}{2}\right]_b^a = \frac{\left(a^2 - b^2\right)^2}{4} $$

$$ \int_b^a r\ln\frac{r}{b}\,dr = \left[\frac{r^2}{2}\ln\frac{r}{b} - \frac{r^2}{4}\right]_b^a = \frac{a^2}{2}\mathcal{L} - \frac{a^2 - b^2}{4} $$

(the second uses $\int r\ln r\,dr = \frac{r^2}{2}\ln r - \frac{r^2}{4}$, checked by differentiating). With $D_a = a^2 - b^2 = a^2(1 - \alpha^2)$ and $C = (-V + G D_a)/\mathcal{L}$:

$$ \frac{Q}{2\pi} = -G\frac{D_a^2}{4} + C\left(\frac{a^2}{2}\mathcal{L} - \frac{D_a}{4}\right) = 0 $$

The key stops at the equivalent integral equation, boxed, $\frac{V}{\ln(\alpha^{-1})}\int_{\alpha a}^{a}r\ln\frac{r}{\alpha a}\,dr = \frac{P_l}{4\mu}\int_{\alpha a}^{a}\left[\frac{(1 - \alpha^2)a^2\ln(r/\alpha a)}{\ln(\alpha^{-1})} - r^2 + (\alpha a)^2\right]r\,dr$, and does not evaluate it. Evaluating it (computed here) and solving for $V$:

$$ \left(-V + GD_a\right)\left(\frac{a^2}{2} - \frac{D_a}{4\mathcal{L}}\right) = G\frac{D_a^2}{4} \;\Longrightarrow\; V = GD_a\,\frac{\dfrac{a^2}{2} - \dfrac{D_a}{4} - \dfrac{D_a}{4\mathcal{L}}}{\dfrac{a^2}{2} - \dfrac{D_a}{4\mathcal{L}}} $$

and, using $\frac{a^2}{2} - \frac{D_a}{4} = \frac{a^2(1 + \alpha^2)}{4}$ and multiplying numerator and denominator by $4\mathcal{L}/a^2$:

$$ V = \frac{P_la^2}{4\mu}\left(1 - \alpha^2\right)\frac{\left(1 + \alpha^2\right)\ln\left(\alpha^{-1}\right) - \left(1 - \alpha^2\right)}{2\ln\left(\alpha^{-1}\right) - \left(1 - \alpha^2\right)} $$

## Answers and Checks

- Velocity: $v_x = -\frac{P_l}{4\mu}\left[r^2 - (\alpha a)^2\right] + \left[-V + \frac{P_l}{4\mu}(1 - \alpha^2)a^2\right]\ln(r/\alpha a)/\ln(\alpha^{-1})$.
- Power per unit length: $W = 2\pi a\,V\left\{\frac{P_la}{2}\left[1 - \frac{1 - \alpha^2}{2\ln(\alpha^{-1})}\right] + \frac{\mu V}{a\ln(\alpha^{-1})}\right\}$.
- Zero flux: $V = \frac{P_la^2}{4\mu}(1 - \alpha^2)\frac{(1 + \alpha^2)\ln(\alpha^{-1}) - (1 - \alpha^2)}{2\ln(\alpha^{-1}) - (1 - \alpha^2)}$.
- Limit $\alpha\to 0$ (no rod): $\ln(\alpha^{-1})\to\infty$ and $V\to\frac{P_la^2}{4\mu}\cdot\frac{1}{2} = \frac{P_la^2}{8\mu}$; directly, a pipe with a wall moving at $-V$ has $Q = \pi a^4P_l/(8\mu) - V\pi a^2 = 0$, the same $V$.
- Limit $\alpha\to 1$ (thin gap $h = a(1 - \alpha)$): with $\epsilon = 1 - \alpha$, $\ln(\alpha^{-1})\simeq\epsilon + \epsilon^2/2 + \epsilon^3/3$, the numerator of the last fraction is $\simeq 2\epsilon^3/3$ and its denominator $\simeq 2\epsilon^2$, so $V\to\frac{P_la^2}{4\mu}\,2\epsilon\,\frac{\epsilon}{3} = \frac{P_lh^2}{6\mu}$, which is the plane result: $Q = P_lh^3/(12\mu) - Vh/2 = 0$.
- Dimensions: $P_la^2/\mu$ is $ML^{-2}T^{-2}\cdot L^2/(ML^{-1}T^{-1}) = LT^{-1}$, a velocity; $\tau_pV$ per unit length is $(\text{N/m}^2)(\text{m/s})(\text{m}) = \text{W/m}$.
- Check against the official key: VF3.pdf gives the same velocity profile, the same $\tau_p$ and $W = \tau_pV\,2\pi a$, and, for the zero flux, the integral condition (not evaluated).
