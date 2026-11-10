---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - couette-poiseuille
  - balance-de-energia
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF17.pdf"
id: "vf17"
pill: "VF17: Plate in a channel"
sheets:
  - 17
tags_html:
  - "Two channels in parallel"
  - "Forces and power"
  - "Energy balance"
---

# Problem VF17: Thin Plate in a Couette Channel

> Official viscous-flow sheet of the course (exam of June 27, 2013), statement transcribed from the sheet. The sheet has **no handwritten key**: the solution below is worked here. Part of [[Topic 7 - Viscous Flows]].
> Method: Couette plus Poiseuille flow in each half of the channel (Notes.pdf, Eqs. 7.9-7.12), conservation of the flux, the force from the wall shear (Eq. 7.16 convention) and the integral energy balance.

## Statement

**PROBLEM 3 (1 hour)** A perfect liquid of constant density $\rho$ and constant viscosity $\mu$ fills the space between two infinite parallel walls separated by a distance $2h$, that move parallel to themselves in the same direction with a constant velocity $U$. As shown in the figure, a very thin solid plate of length $L\gg h$ is placed at the center of the channel. In the regions far upstream and far downstream from the plate the liquid moves with uniform velocity $U$ due to the motion of the confining walls, and the modified pressure takes uniform values $P(x\to-\infty)\to P_{-\infty}$ and $P(x\to\infty)\to P_\infty$, respectively.

1. Provide the criterion that must be accomplished for the flow to be dominated by viscous forces. (**1 point**)

2. Obtain the velocity field in the region occupied by the plate, in terms of the unknown pressure gradient $P_l = -\partial P/\partial x$. (**3 points**)

3. Obtain the pressure drop $P_{-\infty} - P_\infty$, as well as the pressure gradient $P_l$. (**3 points**)

4. Determine the forces (per unit spanwise length) that the liquid exerts on the confining walls, $F_w$, and on the inner plate, $F_p$, as well as the power that must be applied to drive the walls. (**3 points**)

5. If all the inner walls are thermally isolated, determine the temperature increase in the liquid between two points situated far downstream and far upstream, $T_\infty - T_{-\infty}$. To that end, apply the energy equation in integral form to an appropriately defined control volume (**1 extra point**).

![[attachments/FM-T7/vf17-statement.svg]]
*Statement figure (redrawn from VF17.pdf): a channel between two walls at y = ±h moving with velocity U, with a thin plate of length L on the centre line from x = 0 to x = L; the liquid far upstream and downstream moves with U at the pressures and temperatures P_{−∞}, T_{−∞} and P_∞, T_∞; the sketched profiles are those found in the solution*

Source: VF17.pdf (page 1, exam of June 27, 2013; statement only, no key). Notes.pdf, Chapter 7: Couette and Poiseuille flows, Eqs. 7.8-7.12; slender flows, Eqs. 7.40-7.46.

## Hypotheses, Data and Unknowns

- The walls are at $y = \pm h$ and move with $U$; the plate lies on $y = 0$ for $0 < x < L$ and is at rest. Over the plate the channel is divided into two identical half-channels of height $h$, symmetric with respect to $y = 0$.
- Steady flow, slender ($L\gg h$) and two-dimensional; the entrance and exit regions, of length of order $h$, are neglected: the pressure losses in them are small against the loss along the plate (Notes.pdf, Eq. 7.63).
- The liquid has constant $c$ (specific heat), and the inner walls are insulated, so there is no heat flux across the boundaries. Per unit spanwise length.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $h$, $L$ | half-height of the channel, length of the plate | m |
| $U$ | velocity of the walls and of the far flow | m/s |
| $P_{-\infty}$, $P_\infty$ | reduced pressures far upstream and downstream | Pa |
| $T_{-\infty}$, $T_\infty$, $c$ | temperatures far away, specific heat | K, J/(kg K) |

## Criterion for Viscous Dominance

In the half-channel of height $h$ and length $L$ with the velocity scale $U$ (Eq. 7.41):

$$ \frac{\rho Uh}{\mu}\,\frac{h}{L}\ll 1 $$

The flow is steady. (If the pressure-driven velocity, computed below, is of the order of $U$ the same criterion holds.)

## Velocity Field in the Plate Region

In the upper half-channel, $0 < y < h$, with the plate at rest ($y = 0$) and the wall moving with $U$ ($y = h$), the profile is Couette plus Poiseuille (Eq. 7.12):

$$ v_x = U\,\frac{y}{h} + \frac{P_l}{2\mu}\,y\,(h - y), \qquad q_{half} = \int_0^hv_x\,dy = \frac{Uh}{2} + \frac{P_lh^3}{12\mu} $$

The lower half is the mirror image, $v_x(-y) = v_x(y)$.

## Pressure Drop and Pressure Gradient

The flux is conserved along the channel. Far from the plate it is $2h\,U$ (uniform velocity). Over the plate it is the sum of the two halves:

$$ 2hU = 2\left[\frac{Uh}{2} + \frac{P_lh^3}{12\mu}\right] = Uh + \frac{P_lh^3}{6\mu} \;\Longrightarrow\; P_l = \frac{6\mu U}{h^2} $$

The couette flux alone ($Uh$) is only half of what must pass, so the pressure must push: $P_l>0$, the pressure falls in the direction of the flow. The gradient is uniform (the section is constant), so

$$ P_{-\infty} - P_\infty = P_lL = \frac{6\mu UL}{h^2} $$

(the losses at the ends of the plate are of order $\mu U/h$, a factor $h/L$ smaller). With this value the velocity is

$$ v_x = U\frac{y}{h} + \frac{3U}{h^2}\,y\,(h - y) = \frac{U\,y}{h^2}\,(4h - 3y), \qquad 0\le y\le h $$

which is $U$ at the wall, zero at the plate and has a maximum $\frac{4}{3}U$ at $y = \frac{2}{3}h$ (the jet seen in the sketch of the sheet).

## Forces and Power

The shear stress is $\mu\,\partial v_x/\partial y = \mu\left[\frac{U}{h} + \frac{P_l}{2\mu}(h - 2y)\right] = \frac{\mu U}{h^2}\left(4h - 6y\right)$. The force of the liquid on a surface is $\bar{\tau}'\cdot\bar{n}$ with $\bar{n}$ pointing from the surface into the liquid.

**Walls.** On the upper wall ($y = h$, $\bar{n} = -\bar{e}_y$): $\tau = -\mu\frac{\partial v_x}{\partial y}\Big|_h = -\frac{\mu U}{h^2}(4h - 6h) = \frac{2\mu U}{h}$ in $+x$: the liquid in the gap moves faster than the wall and drags it forward. Over the length $L$, for each wall (the walls outside the plate region are in uniform flow, with no shear):

$$ F_w = \frac{2\mu UL}{h} \;\text{ on each wall},\quad\text{in the direction of its motion}; \qquad\text{both walls: }\frac{4\mu UL}{h} $$

**Plate.** On each face ($y = 0^{\pm}$, $\bar{n} = \pm\bar{e}_y$): $\tau = \mu\frac{\partial v_x}{\partial y}\Big|_0 = \frac{4\mu U}{h}$ along $+x$. Two faces and the length $L$:

$$ F_p = 2\cdot\frac{4\mu U}{h}\,L = \frac{8\mu UL}{h} $$

(the drag on the plate, in the direction of the flow).

**Check by momentum.** For the liquid in the plate region (no change of momentum flux, uniform $U$ in and out), the forces on it add to zero: the pressure difference on the section $2h$, $2h(P_{-\infty} - P_\infty) = 12\mu UL/h$, minus the reactions on the two walls, $4\mu UL/h$, minus the reaction on the plate, $8\mu UL/h$: $12 - 4 - 8 = 0$.

**Power.** The liquid pushes the walls forward with the total force $4\mu UL/h$, so to keep them at the constant velocity $U$ an external force $-F_w$ must hold each one back. The power that the external agent supplies to the walls is

$$ \dot{W}_{walls} = -2F_wU = -\frac{4\mu U^2L}{h} $$

negative: the walls do not have to be driven, they **receive** the power $4\mu U^2L/h$ from the liquid (which is being pushed through the plate region by the imposed pressure drop); a brake has to absorb it. Its magnitude is $2F_wU$.

## Temperature Increase

Control volume: the liquid between two sections far upstream and far downstream, bounded by the walls and the plate (all insulated: no heat). Steady energy balance in integral form: net outflow of $\rho(e + v^2/2)$ plus the work of the pressure at the two sections equals the work of the viscous forces on the moving boundaries (the plate is at rest, the walls move with $U$). The kinetic energy flux is the same in and out (uniform $U$); with $e = cT$:

$$ \rho c\,(2hU)\left(T_\infty - T_{-\infty}\right) = \underbrace{2hU\left(P_{-\infty} - P_\infty\right)}_{\text{work of the pressure}} - \underbrace{2F_wU}_{\text{work done on the walls}} = \frac{12\mu U^2L}{h} - \frac{4\mu U^2L}{h} = \frac{8\mu U^2L}{h} $$

(the work of the force that the walls exert on the liquid is $-F_w U$ per wall; the reduced pressure is used, since the flow is horizontal and the heights are the same). Hence

$$ T_\infty - T_{-\infty} = \frac{8\mu U^2L/h}{2\rho c\,hU} = \frac{4\mu UL}{\rho c\,h^2} $$

**Check with the dissipation:** $\Phi = \mu(\partial v_x/\partial y)^2 = \mu U^2(4h - 6y)^2/h^4$, and $\int_0^h\Phi\,dy = \frac{\mu U^2}{h^4}\left[-\frac{(4h - 6y)^3}{18}\right]_0^h = \frac{\mu U^2}{h^4}\,\frac{64h^3 + 8h^3}{18} = \frac{4\mu U^2}{h}$; two halves and the length $L$: $\frac{8\mu U^2L}{h}$, the same, as it must be (all the mechanical power that is not stored becomes heat).

## Answers and Checks

- Viscous dominance: $(\rho Uh/\mu)(h/L)\ll 1$.
- Velocity over the plate: $v_x = \frac{U\,y}{h^2}(4h - 3y)$ for $0\le y\le h$ (symmetric in $y$); $P_l = 6\mu U/h^2$; $P_{-\infty} - P_\infty = 6\mu UL/h^2$.
- Forces: $F_w = 2\mu UL/h$ on each wall (forward), $F_p = 8\mu UL/h$ on the plate (forward). Power at the walls: $2F_wU = 4\mu U^2L/h$, received from the liquid.
- Temperature: $T_\infty - T_{-\infty} = 4\mu UL/(\rho ch^2)$.
- Dimensions: $\mu UL/h$ per unit width is $MT^{-2}$, a force per unit width; $\mu UL/(\rho ch^2)$ is $ML^{-1}T^{-1}\cdot LT^{-1}\cdot L/(ML^{-3}\cdot L^2T^{-2}\Theta^{-1}\cdot L^2) = \Theta$.
- Limit $L\to 0$: all the quantities vanish, as they should without a plate.
- Check against the official key: none; the sheet has no solution, so all the results of this note are computed here and checked by the momentum, flux and energy balances above.
