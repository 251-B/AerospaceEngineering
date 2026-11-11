---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - bomba-viscosa
  - lubricacion
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF9.pdf"
id: "vf9"
pill: "VF9: Conveyor belt pump"
sheets:
  - 9
tags_html:
  - "Couette + Poiseuille"
  - "Two stretches in series"
  - "Power and energy balance"
---

# Problem VF9: Conveyor Belt Pumping on an Incline

> Official viscous-flow sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: Couette plus Poiseuille flow in each stretch (Notes.pdf, Eqs. 7.12 and 7.70-7.71), equal flux in both stretches (Eq. 7.72) and the reduced pressure $P = p + \rho gZ$ (Eq. 7.2).

## Statement

The conveyor belt of velocity $V$ shown in the figure is used to pump a liquid of density $\rho$ and viscosity $\mu$ along a straight inclined channel of angle $\alpha$ including two stretches of equal length $L$ with different heights $2h$ and $h$, respectively.

- Give the conditions for the liquid-film motion to be dominated by viscosity.
- Compute the pressure distribution along the channel $p(x)$.
- Determine the volume flux $Q$ as well as the minimum value of $V$ for which $Q > 0$.
- Obtain the power needed to drive the conveyor belt.

![[attachments/FM-T7/vf9-statement.svg]]
*Statement figure (redrawn from VF9.pdf): an inclined channel at the angle α between the conveyor belt, which moves up the slope with velocity V, and a fixed wall with a step (gap 2h over a length L, then h over a length L); both ends are at p_a and p_0 is the pressure at the step*

Source: VF9.pdf (page 1, statement and handwritten key; no date printed). Notes.pdf, Chapter 7: Couette and Poiseuille flows, Eqs. 7.8-7.12; wedge effect, Eqs. 7.69-7.75.

## Hypotheses, Data and Unknowns

- The belt is the lower wall of the channel (the line between the two rollers in the figure) and moves up the slope, along $+x$, with velocity $V$; the upper wall is fixed. $x$ runs along the belt and $y$ is normal to it, from the belt towards the fixed wall.
- Gap: $2h$ for $0 < x < L$ and $h$ for $L < x < 2L$. Both ends of the channel are at the atmospheric pressure $p_a$ (the inlet at the bottom reservoir, the outlet at the top).
- The flow is steady and slender, so in each stretch the pressure is uniform across the gap and the reduced pressure $P = p + \rho gx\sin\alpha$ (with $Z = x\sin\alpha$ at $y\to 0$) has a constant gradient.
- Let $p_0$ be the pressure at the step, $x = L$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $V$ | velocity of the belt | m/s |
| $h$, $2h$ | gaps of the two stretches | m |
| $L$, $\alpha$ | length of each stretch, angle of the channel | m, rad |
| $p_a$, $p_0$ | pressure at the ends and at the step | Pa |
| $Q$ | volume flux per unit width | m$^2$/s |

## Criterion for Viscous Dominance

For a slender film (Eqs. 7.67-7.68) with the velocity scale $V$, the largest gap $2h\sim h$ and the length $L$:

$$ \frac{\rho Vh}{\mu}\,\frac{h}{L}\ll 1 $$

The flow is steady, so the unsteady condition (7.67) holds.

## Velocity and Flux in Each Stretch

The reduced pressure at the ends: $P(0) = p_a$ and $P(2L) = p_a + \rho g\,2L\sin\alpha$; at the step $P(L) = p_0 + \rho gL\sin\alpha$. With $P_l = -dP/dx$:

$$ P_{l1} = \frac{p_a - p_0 - \rho gL\sin\alpha}{L}, \qquad P_{l2} = \frac{p_0 + \rho gL\sin\alpha - p_a - 2\rho gL\sin\alpha}{L} = \frac{p_0 - p_a - \rho gL\sin\alpha}{L} $$

The profile of a gap $H$ with the lower wall at velocity $V$ and the upper wall at rest is the sum of Couette and Poiseuille flows (Eqs. 7.9 and 7.11, 7.70):

$$ v_x = V\,\frac{H - y}{H} + \frac{P_l}{2\mu}\,y\,(H - y), \qquad Q = \int_0^Hv_x\,dy = \frac{VH}{2} + \frac{P_lH^3}{12\mu} $$

$$ H = 2h:\quad Q = Vh + \frac{2h^3}{3\mu}\,P_{l1}, \qquad H = h:\quad Q = \frac{Vh}{2} + \frac{h^3}{12\mu}\,P_{l2} $$

## Pressure Distribution and Flux

The flux is the same in both stretches. With $\Delta = (p_0 - p_a)/L$ and $G = \rho g\sin\alpha$, $P_{l1} = -\Delta - G$ and $P_{l2} = \Delta - G$:

$$ Vh - \frac{2h^3}{3\mu}\left(\Delta + G\right) = \frac{Vh}{2} + \frac{h^3}{12\mu}\left(\Delta - G\right) $$

Multiplying by $12\mu/h^3$: $6\mu V/h^2 - 8\Delta - 8G = \Delta - G$, so $9\Delta = 6\mu V/h^2 - 7G$:

$$ p_0 - p_a = \frac{2}{3}\,\frac{\mu VL}{h^2} - \frac{7}{9}\,\rho gL\sin\alpha $$

The pressure $p = P - \rho gx\sin\alpha$ is linear in each stretch, because the weight term cancels (as in VF5):

$$ 0 < x < L:\quad p = p_a + \left(p_0 - p_a\right)\frac{x}{L}, \qquad L < x < 2L:\quad p = p_0 - \left(p_0 - p_a\right)\frac{x - L}{L} $$

(the second from $P(x) = P(L) + P_{l2}\cdot(-(x - L))$ and $p = P - \rho gx\sin\alpha$).

**Volume flux.** Using the second stretch with $P_{l2} = \Delta - G$:

$$ Q = \frac{Vh}{2} + \frac{h^3}{12\mu}\left(\frac{2}{3}\frac{\mu V}{h^2} - \frac{16}{9}G\right) = \frac{Vh}{2} + \frac{Vh}{18} - \frac{4}{27}\frac{h^3G}{\mu} = \frac{5}{9}Vh - \frac{4}{27}\,\frac{\rho gh^3\sin\alpha}{\mu} $$

**Minimum velocity.** $Q > 0$ requires $\frac{5}{9}Vh > \frac{4}{27}\frac{\rho gh^3\sin\alpha}{\mu}$:

$$ V > V_{min} = \frac{4}{15}\,\frac{\rho gh^2\sin\alpha}{\mu} $$

## Power Needed to Drive the Belt

The liquid acts on the belt with the shear $\tau = \mu\,\partial v_x/\partial y$ at $y = 0$ (normal $+\bar{e}_y$, from the belt into the liquid):

$$ \tau_1 = \mu\left(-\frac{V}{2h} + \frac{P_{l1}}{2\mu}\,2h\right) = -\frac{\mu V}{2h} + P_{l1}h, \qquad \tau_2 = -\frac{\mu V}{h} + \frac{P_{l2}h}{2} $$

$$ \tau_1 + \tau_2 = -\frac{3}{2}\frac{\mu V}{h} + h\left(P_{l1} + \frac{P_{l2}}{2}\right) = -\frac{3}{2}\frac{\mu V}{h} - h\left(\frac{\Delta}{2} + \frac{3G}{2}\right) $$

The force of the liquid on the belt (per unit width) is $L(\tau_1 + \tau_2)\bar{e}_x$, negative: the liquid resists. The key's boxed $W = VL(\tau_1 + \tau_2)$ is the power of this force (negative); **the power that the drive must supply is its opposite**:

$$ W_{drive} = -VL\left(\tau_1 + \tau_2\right) = VL\left[\frac{3}{2}\frac{\mu V}{h} + \frac{3}{2}\rho gh\sin\alpha + \frac{h}{2}\,\frac{p_0 - p_a}{L}\right] $$

and with $\Delta = \frac{2}{3}\frac{\mu V}{h^2} - \frac{7}{9}G$ ($\frac{h\Delta}{2} = \frac{1}{3}\frac{\mu V}{h} - \frac{7}{18}Gh$):

$$ W_{drive} = VL\left[\frac{11}{6}\,\frac{\mu V}{h} + \frac{10}{9}\,\rho gh\sin\alpha\right] $$

**Energy check** (computed here, horizontal case $G = 0$): the viscous dissipation of a gap $H$ per unit length is $\int_0^H\mu\,(\partial v_x/\partial y)^2dy = \mu V^2/H + P_l^2H^3/(12\mu)$ (the cross term integrates to zero). With $P_{l1} = -\Delta = -\frac{2}{3}\mu V/h^2$ and $P_{l2} = \Delta$: stretch 1 gives $\frac{43}{54}\mu V^2/h$ and stretch 2 gives $\frac{28}{27}\mu V^2/h = \frac{56}{54}\mu V^2/h$; adding them and multiplying by $L$ gives $\frac{99}{54}\mu V^2L/h = \frac{11}{6}\mu V^2L/h$, which is $W_{drive}$ for $G = 0$.

## Answers and Checks

- Viscous dominance: $(\rho Vh/\mu)(h/L)\ll 1$.
- Pressure: $p = p_a + (p_0 - p_a)x/L$ for $0 < x < L$ and $p = p_0 - (p_0 - p_a)(x - L)/L$ for $L < x < 2L$, with $p_0 - p_a = \frac{2}{3}\mu VL/h^2 - \frac{7}{9}\rho gL\sin\alpha$.
- Flux: $Q = \frac{5}{9}Vh - \frac{4}{27}\rho gh^3\sin\alpha/\mu$; $V_{min} = \frac{4}{15}\rho gh^2\sin\alpha/\mu$.
- Power supplied: $W = VL\left[\frac{3}{2}\frac{\mu V}{h} + \frac{3}{2}\rho gh\sin\alpha + \frac{h}{2}\frac{p_0 - p_a}{L}\right] = VL\left[\frac{11}{6}\frac{\mu V}{h} + \frac{10}{9}\rho gh\sin\alpha\right]$.
- Dimensions: $\mu V^2L/h$ per unit width is $ML^{-1}T^{-1}\cdot L^2T^{-2}\cdot L/L = MLT^{-3}$, a power per unit width; $\rho gh^2/\mu$ is a velocity.
- Limits: for $\alpha = 0$ and $L\to$ any, $V_{min} = 0$ and $Q = \frac{5}{9}Vh$ (the pump works for any $V > 0$); for $h$ fixed and large $\alpha$ the weight of the column stops the pumping when $V < V_{min}$.
- Check against the official key: VF9.pdf gives the same profiles, fluxes, $p_0 - p_a$, $Q$, $V_{min}$ and pressure distribution (its $p$ is the pressure, in which the weight cancels), and $W = VL(\tau_1 + \tau_2)$, which has the sign of the force on the belt, as explained above.
