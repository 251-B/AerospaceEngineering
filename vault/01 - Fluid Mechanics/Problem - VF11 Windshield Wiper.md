---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - lubricacion
  - fuerza-y-momento
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF11.pdf"
id: "vf11"
pill: "VF11: Windshield wiper"
sheets:
  - 11
tags_html:
  - "Couette + Poiseuille"
  - "Closed end"
  - "Force and moment"
---

# Problem VF11: Windshield Wiper

> Official viscous-flow sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: Couette plus Poiseuille flow in a thin channel (Notes.pdf, Eqs. 7.69-7.71) with zero flux because of the closed end, and the force and the moment of the pressure and the shear on the arm (Eq. 7.76).

## Statement

To investigate the performance of windshield wipers consider as a simplified model the L-shaped arm of the figure moving with velocity $V$ with respect to a horizontal surface. The wiper is pulled from the end point $A$ with a force $F_x$ parallel to the wall, dragging in its motion the fluid located between the arm and the wall. To study the problem, we shall use a reference frame moving with the arm, as indicated in the figure. The outer pressure is $p_a$.

1. Determine the velocity $v_x$ across the channel formed between the wiper and the wall.

2. Find the pressure distribution $p(x)$ including the value found at the end wall $x = 0$.

3. Compute the force $F_x$ necessary to move the wiper.

4. Obtain the moment exerted with respect to the end point $A$.

5. If $W$ is the weight of the wiper, determine the critical value of $V$ beyond which the end $x = 0$ rises, letting the liquid flow out.

![[attachments/FM-T7/vf11-statement.svg]]
*Statement figure (redrawn from VF11.pdf): an L-shaped arm whose horizontal bar of length L is at a height h above the wall and whose vertical leg closes the channel at x = 0; the wall moves with velocity V towards −x in the frame of the arm, F_x acts at A and p_o is the pressure at x = 0*

Source: VF11.pdf (page 1, statement and handwritten key; no date printed). Notes.pdf, Chapter 7: Couette and Poiseuille flows, Eqs. 7.9-7.12; wedge effect, Eqs. 7.69-7.76.

## Hypotheses, Data and Unknowns

- In the frame of the arm the wall moves with velocity $-V\bar{e}_x$ (the arm moves with $+V$ with respect to the wall) and the arm is at rest. The channel is closed at $x = 0$ by the vertical leg and open at $x = L$, where the pressure is $p_a$.
- The channel is slender ($h\ll L$), the flow is steady in this frame and the pressure is uniform across the gap; $P_l = -dp/dx$ is constant.
- Pressures are gauge pressures with respect to $p_a$ on the outer faces of the wiper; gravity is not considered.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $L$, $h$ | length of the arm, height of the channel | m |
| $V$ | velocity of the wiper with respect to the wall | m/s |
| $p_0$, $p_a$ | pressure at $x = 0$, outer pressure | Pa |
| $W$ | weight of the wiper (per unit width) | N/m |

## Velocity Profile

The wall at $y = 0$ moves with $-V$ and the arm at $y = h$ is at rest, so the Couette and Poiseuille flows of Eqs. (7.9) and (7.11) add (Eq. 7.12):

$$ v_x = -V\,\frac{h - y}{h} + \frac{P_l}{2\mu}\,y\,(h - y) $$

The channel is closed at $x = 0$ and the flux is uniform along it (Eq. 7.72), so **the flux is zero**:

$$ Q = \int_0^hv_x\,dy = -\frac{Vh}{2} + \frac{P_lh^3}{12\mu} = 0 \;\Longrightarrow\; P_l = \frac{6\mu V}{h^2} $$

and the profile is $v_x = -V\frac{h - y}{h} + \frac{3V}{h^2}\,y\,(h - y)$: the liquid is dragged to the left near the wall and returns to the right near the arm.

## Pressure Distribution

$P_l = -dp/dx = (p_0 - p_a)/L$ is constant with $p(L) = p_a$:

$$ p_0 = p_a + \frac{6\mu VL}{h^2}, \qquad p - p_a = \frac{6\mu V}{h^2}\,(L - x) $$

an overpressure, largest at the closed end.

## Force Needed to Move the Wiper

Take the wiper as the arm plus the vertical leg. The force of the liquid on it (normal pointing from the wiper into the liquid) has two parts in the $x$ direction.

**Pressure on the leg** (area $h$ per unit width, normal $+\bar{e}_x$ on its inner face, force $-(p - p_a)\bar{n}$): $-(p_0 - p_a)h = -6\mu VL/h$. The pressure on the underside of the arm is vertical.

**Shear on the underside of the arm** ($y = h$, $\bar{n} = -\bar{e}_y$): $\bar{\tau}\cdot\bar{n} = -\mu\,\partial v_x/\partial y$, and $\partial v_x/\partial y = V/h + \frac{P_l}{2\mu}(h - 2y)$ gives at $y = h$: $V/h - \frac{P_lh}{2\mu} = V/h - 3V/h = -2V/h$. So the force per unit area is $+2\mu V/h$ and, over the length $L$, $+2\mu VL/h$.

$$ F_{liquid,x} = -\frac{6\mu VL}{h} + \frac{2\mu VL}{h} = -\frac{4\mu VL}{h} $$

The liquid opposes the motion. The force that must be applied at $A$ is the opposite:

$$ F_x = \frac{4\mu VL}{h} $$

(the key writes the sum of both contributions on one line, "$-\mu(\partial v_x/\partial y)_{y=h}L\,\bar{e}_x = -4\mu VL/h\,\bar{e}_x$", which is the total and not the viscous term alone; it then boxes $F_x = 4\mu VL/h$).

## Moment about the End Point $A$

The pressure on the underside of the arm acts upward, $+(p - p_a)\,dx\,\bar{e}_y$, at the point $x$, whose position with respect to $A$ is $(x - L)\bar{e}_x$:

$$ \bar{M}_A = \int_0^L(x - L)\,(p - p_a)\,dx\;\bar{e}_z = -\frac{6\mu V}{h^2}\int_0^L(L - x)^2dx\;\bar{e}_z = -\frac{6\mu V}{h^2}\,\frac{L^3}{3}\,\bar{e}_z = -\frac{2\mu VL^3}{h^2}\,\bar{e}_z $$

(since $\bar{e}_x\times\bar{e}_y = \bar{e}_z$ and $\int_0^L(L - x)^2dx = \left[-(L - x)^3/3\right]_0^L = L^3/3$). The shear forces on the arm act at the level of $A$ and give no moment; the pressure on the leg and the shear on it give a moment of order $\mu VL/h$, a factor $(h/L)^2$ smaller than the one above, and are neglected (the key strikes out the viscous integral).

## Critical Velocity

The wiper is subjected to its weight $W$ (at the middle, $x = L/2$), the pressure load of the film on the arm, the force at $A$ and the reaction $R$ of the wall on its end $x = 0$ (upward). Moments about $A$, with $\bar{M}_A$ the moment of the liquid:

$$ 0 = -\frac{2\mu VL^3}{h^2} + W\frac{L}{2} - RL \;\Longrightarrow\; R = \frac{W}{2} - \frac{2\mu VL^2}{h^2} $$

The end $x = 0$ rises when $R = 0$ (the film lifts it):

$$ V_c = \frac{Wh^2}{4\mu L^2} $$

For $V < V_c$ the end rests on the wall and the liquid is retained; for $V > V_c$ it rises and lets the liquid flow out.

## Answers and Checks

- Velocity: $v_x = -V\frac{h - y}{h} + \frac{P_l}{2\mu}y(h - y)$ with $P_l = 6\mu V/h^2$ (zero flux).
- Pressure: $p - p_a = \frac{6\mu V}{h^2}(L - x)$, $p_0 = p_a + \frac{6\mu VL}{h^2}$.
- Force: $F_x = 4\mu VL/h$. Moment about $A$: $\bar{M}_A = -\frac{2\mu VL^3}{h^2}\bar{e}_z$. Critical velocity: $V_c = Wh^2/(4\mu L^2)$.
- Dimensions: $\mu VL/h$ per unit width is $ML^{-1}T^{-1}\cdot LT^{-1}\cdot L/L = MT^{-2}$, a force per unit width; $Wh^2/(\mu L^2)$ is a velocity ($W$ per unit width $\sim MT^{-2}$).
- Check of the force: the horizontal momentum balance of the liquid in the channel is $0 = (p_0 - p_a)h - \tau_{arm}L - \tau_{wall}L$ per unit width, with $\tau_{wall} = \mu|v'(0)| = 4\mu V/h$ ($v'(0) = V/h + P_lh/(2\mu) = V/h + 3V/h = 4V/h$ directed along $+x$) and $\tau_{arm} = 2\mu V/h$: $6\mu VL/h = 2\mu VL/h + 4\mu VL/h$.
- Check against the official key: VF11.pdf gives the same profile, pressure, $F_x = 4\mu VL/h$, $\bar{M} = -2\mu VL^3/h^2\,\bar{e}_z$ and $V = Wh^2/(4\mu L^2)$.
