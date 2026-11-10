---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - tuberia-variable
  - descarga
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF7.pdf"
id: "vf7"
pill: "VF7: Conical pipe"
sheets:
  - 7
tags_html:
  - "Pipe of variable section"
  - "Quasi-steady discharge"
  - "Discharge time"
---

# Problem VF7: Discharge from a Conical Pipe

> Official viscous-flow sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: slender flow in a pipe of slowly varying section (Notes.pdf, Eqs. 7.47-7.51), with the flux tied to the speed of the free surface by mass conservation.

## Statement

The vertical conical pipe of length $L$ shown in the figure has a radius that increases linearly from the lower end according to $a(z) = a_o(1 + \alpha z/L)$, with $a_o\ll 1$ and $\alpha\sim O(1)$. The pipe, open at the top, is initially full of a liquid of viscosity $\mu$ and density $\rho$. At a given time, the lower end opens up and the liquid discharges to the atmosphere under the action of gravity. Give the condition for the motion to be dominated by viscosity and, in that case, obtain the evolution of $h(t)$ as well as the time needed to complete the discharge.

The sheet writes $a_o\ll 1$; the condition is $a_o\ll L$ (a slender pipe), since $a_o$ is a length.

![[attachments/FM-T7/vf7-statement.svg]]
*Statement figure (redrawn from VF7.pdf): a vertical conical pipe of length L, radius a_0 at the lower end and increasing linearly upward, open at both ends, with the free surface at the height h(t) above the lower end*

Source: VF7.pdf (page 1, statement and handwritten key; no date printed). Notes.pdf, Chapter 7: slender flows, Eqs. 7.40-7.46; pipe of variable section, Eqs. 7.47-7.51.

## Hypotheses, Data and Unknowns

- The pipe is slender and its radius changes slowly ($\alpha\sim O(1)$ and $a_o\ll L$), so the flow is a local Poiseuille flow (Eq. 7.48) and the flux $Q$ does not depend on $z$ (Eq. 7.49).
- $z$ is measured upwards from the lower end. The free surface is at $z = h(t)$, with $h(0) = L$ (the pipe is full); the lower end is open to the atmosphere, $p = p_a$, and so is the free surface.
- Reduced pressure $P = p + \rho g z$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $a(z) = a_o(1 + \alpha z/L)$ | local radius | m |
| $L$ | length of the pipe | m |
| $h(t)$ | height of the free surface above the lower end | m |
| $Q$ | volume flux (downward) | m$^3$/s |

## Criterion for Viscous Dominance

As in VF5, the convective and local accelerations are negligible against the viscous force (Eqs. 7.40-7.41) when

$$ \frac{\rho V_La_o}{\mu}\,\frac{a_o}{L}\ll 1, \qquad V_L\sim\frac{\rho g a_o^2}{\mu} \;\Longrightarrow\; \frac{\rho^2g\,a_o^4}{\mu^2L}\ll 1 $$

($V_L$ is the velocity that the weight of the column gives with the viscous resistance, Eq. 7.44; the largest radius is of order $a_o$ since $\alpha\sim O(1)$).

## Flux and Pressure

The pressure gradient along the pipe follows from the local Poiseuille law (7.49), $Q = \frac{\pi a^4}{8\mu}P_l$ with the flow downwards, so that the reduced pressure grows upwards: $dP/dz = 8\mu Q/(\pi a^4)$. Between the open lower end ($z = 0$, $p = p_a$, $P = p_a$) and the free surface ($z = h$, $p = p_a$, $P = p_a + \rho gh$), integrating (Eq. 7.50):

$$ \rho gh = \frac{8\mu Q}{\pi}\int_0^h\frac{dz}{a^4(z)} = \frac{8\mu Q}{\pi a_o^4}\int_0^h\frac{dz}{(1 + \alpha z/L)^4} $$

With $w = 1 + \alpha z/L$, $dz = (L/\alpha)\,dw$, and Barrow's rule:

$$ \int_0^h\frac{dz}{(1 + \alpha z/L)^4} = \frac{L}{\alpha}\left[-\frac{1}{3w^3}\right]_1^{1 + \alpha h/L} = \frac{L}{3\alpha}\left[1 - \frac{1}{(1 + \alpha h/L)^3}\right] $$

$$ \rho gh = \frac{8\mu QL}{3\pi\alpha a_o^4}\left[1 - \frac{1}{(1 + \alpha h/L)^3}\right] $$

(the factor $\alpha$ in the denominator is in the next line of the key: the boxed line of the sheet is partly struck out in the scan).

## Evolution of the Free Surface

The volume that leaves in $dt$ is the one lost by the column, $dV = -\pi a^2(h)\,dh$, so $Q = -\pi a^2(h)\,dh/dt$ with $a(h) = a_o(1 + \alpha h/L)$. Substituting, with $w = 1 + \alpha h/L$:

$$ \rho gh = -\frac{8\mu L}{3\alpha a_o^2}\left[1 - \frac{1}{w^3}\right]w^2\frac{dh}{dt} = -\frac{8\mu L}{3\alpha a_o^2}\,\frac{w^3 - 1}{w}\,\frac{dh}{dt} $$

(since $\left(1 - w^{-3}\right)w^2 = w^2 - w^{-1} = (w^3 - 1)/w$). Separating variables, with $h = L$ at $t = 0$:

$$ \frac{3\alpha}{8}\,\frac{\rho ga_o^2}{\mu L}\,t = -\int_L^h\frac{w^3 - 1}{h'\,w}\,dh' $$

To evaluate the integral (computed here) set $s = \alpha h'/L$, so $dh'/h' = ds/s$ and $w = 1 + s$; as $(1 + s)^3 - 1 = s\left(s^2 + 3s + 3\right)$ and $s^2 + 3s + 3 = (s + 2)(s + 1) + 1$:

$$ \frac{(1 + s)^3 - 1}{s(1 + s)} = \frac{s^2 + 3s + 3}{1 + s} = s + 2 + \frac{1}{1 + s}, \qquad \int\left(s + 2 + \frac{1}{1 + s}\right)ds = S(s) = \frac{s^2}{2} + 2s + \ln(1 + s) $$

$$ \frac{3\alpha\rho ga_o^2}{8\mu L}\,t = S(\alpha) - S\!\left(\frac{\alpha h}{L}\right), \qquad S(s) = \frac{s^2}{2} + 2s + \ln(1 + s) $$

which gives $t(h)$ explicitly, and $h(t)$ implicitly.

## Time to Complete the Discharge

At $h = 0$, $S(0) = 0$:

$$ t_d = \frac{8}{3\alpha}\,\frac{\mu L}{\rho ga_o^2}\left[\frac{\alpha^2}{2} + 2\alpha + \ln(1 + \alpha)\right] $$

The key stops at $t_d = \frac{8}{3\alpha}\frac{\mu L}{\rho ga_o^2}\int_0^L\frac{(1 + \alpha h/L)^3 - 1}{h(1 + \alpha h/L)}\,dh$; the value of the integral is $\alpha^2/2 + 2\alpha + \ln(1 + \alpha)$, as computed.

## Answers and Checks

- Viscous dominance: $\rho^2ga_o^4/(\mu^2L)\ll 1$.
- Evolution: $\frac{3\alpha\rho ga_o^2}{8\mu L}t = S(\alpha) - S(\alpha h/L)$, $S(s) = s^2/2 + 2s + \ln(1 + s)$; the flux is $Q = -\pi a_o^2(1 + \alpha h/L)^2\,dh/dt$.
- Discharge time: $t_d = \frac{8\mu L}{3\alpha\rho ga_o^2}\left[\frac{\alpha^2}{2} + 2\alpha + \ln(1 + \alpha)\right]$.
- Limit $\alpha\to 0$ (cylindrical pipe): $\frac{\alpha^2}{2} + 2\alpha + \ln(1 + \alpha) = 3\alpha + \alpha^3/3 + \dots$, so $t_d\to\frac{8\mu L}{\rho ga_o^2}$; directly, the column of constant length $h$ has $P_l = \rho g$ and $Q = \pi a_o^4\rho g/(8\mu)$, a constant mean velocity $a_o^2\rho g/(8\mu)$, and $L$ divided by it is the same.
- Dimensions: $\mu L/(\rho ga_o^2)$ is $ML^{-1}T^{-1}\cdot L/(ML^{-3}\cdot LT^{-2}\cdot L^2) = T$; $\alpha$ and $S$ are dimensionless.
- Check against the official key: VF7.pdf gives the same criterion, pressure relation (with $\alpha$ in its denominator after the factor the scan strikes), differential equation and integral relations for $h(t)$ and $t_d$, without evaluating the integral.
