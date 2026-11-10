---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - lubricacion
  - pelicula-comprimida
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF14.pdf"
id: "vf14"
pill: "VF14: Arm approaching a wall"
sheets:
  - 14
tags_html:
  - "Squeeze film"
  - "Closed end"
  - "Force and torque"
---

# Problem VF14: Arm Approaching a Wall

> Official viscous-flow sheet of the course (exam of Jan 10, 2012), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: slender film (Notes.pdf, Eqs. 7.67-7.71), continuity across the film with a moving boundary (Eq. 7.72) and the force and moment of the pressure and the shear (Eq. 7.76).

## Statement

The L-shaped arm of length $L$ depicted in the figure moves vertically approaching the horizontal wall, forming a thin channel of decreasing uniform thickness $h(t)\ll L$. A liquid of density $\rho$ and viscosity $\mu$ fills the channel. Due to the arm displacement, the liquid is forced to move out, discharging to the surrounding atmosphere, where the reduced pressure is $P_\infty$. For a known value of $h(t)$,

1. Give the conditions for the motion in the channel to be dominated by viscosity.

2. Determine the velocity profile across the channel $v_x(x,y,t)$, the associated volume flux $Q = \int_0^hv_x\,dy$, and the reduced pressure distribution $P(x,t)$, including the value $P_0(t)$ at $x = 0$.

3. Calculate the force acting on the arm $\bar{F} = (F_x, F_y)$.

4. Obtain the torque exerted on the arm with respect to its end point $A$.

The sheet writes the pressure at $x = 0$ as $P_o$ in the figure and $P_0$ in the statement.

![[attachments/FM-T7/vf14-statement.svg]]
*Statement figure (redrawn from VF14.pdf): an L-shaped arm whose horizontal bar of length L is at the height h(t) above a wall and whose vertical leg closes the channel at x = 0; A is the end of the bar and P_∞ the pressure outside; P_o is the pressure at x = 0*

Source: VF14.pdf (page 1, exam of Jan 10, 2012, statement and handwritten key). Notes.pdf, Chapter 7: slender films, Eqs. 7.67-7.71; the wedge effect, Eq. 7.72; forces and moments, Eq. 7.76.

## Hypotheses, Data and Unknowns

- The arm moves vertically with the velocity $\dot{h} = dh/dt$ (negative when it approaches the wall); the channel, $0 < x < L$, $0 < y < h(t)$, is closed at $x = 0$ by the vertical leg and open at $x = L$, where the pressure is $P_\infty$.
- Slender film ($h\ll L$), pressure uniform across it; gravity is absorbed in the reduced pressure.

## Criterion for Viscous Dominance

By continuity $V_L\sim L\dot{h}/h$ and $t_0\sim h/|\dot{h}|$. The convective and local accelerations against the viscous force (Eqs. 7.67-7.68):

$$ \frac{\rho V_Lh}{\mu}\frac{h}{L}\sim\frac{L\dot{h}}{h}\frac{h}{\nu}\frac{h}{L} = \frac{h\dot{h}}{\nu}\ll 1, \qquad \frac{h^2/\nu}{t_0}\sim\frac{h\dot{h}}{\nu}\ll 1 $$

So $h\,|\dot{h}|/\nu\ll 1$.

## Velocity, Flux and Pressure

Equation (7.69) with no slip on the wall and on the arm ($v_x = 0$ at $y = 0$ and $y = h$) gives the Poiseuille profile (7.11):

$$ 0 = P_l + \mu\frac{\partial^2v_x}{\partial y^2} \;\Longrightarrow\; v_x = \frac{P_l}{2\mu}\,y\,(h - y), \qquad Q = \frac{P_lh^3}{12\mu} = -\frac{\partial P}{\partial x}\frac{h^3}{12\mu} $$

Integrating the continuity equation across the channel, with $v_x(h) = 0$, $v_y(0) = 0$ and $v_y(h) = \dot{h}$ (the arm moves with $\dot{h}$):

$$ \int_0^{h}\left(\frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y}\right)dy = 0 \;\Longrightarrow\; \frac{\partial Q}{\partial x} + \dot{h} = 0 $$

so $Q = -\dot{h}x$ (zero at the closed end $x = 0$; positive for an approaching arm). Then $-\frac{\partial P}{\partial x}\frac{h^3}{12\mu} = -\dot{h}x$, that is, the first integration of the key, $\frac{\partial P}{\partial x}\frac{h^3}{12\mu} = \dot{h}x$ (the key's boxed line carries a sign that is the opposite of its next line, which is the one used):

$$ \frac{\partial P}{\partial x} = \frac{12\mu\dot{h}}{h^3}\,x \;\Longrightarrow\; P = \frac{6\mu\dot{h}}{h^3}\,x^2 + C_2 $$

With $P(L) = P_\infty$:

$$ P(x, t) = P_\infty + \frac{6\mu\dot{h}}{h^3}\left(x^2 - L^2\right), \qquad P_0(t) = P_\infty - \frac{6\mu\dot{h}L^2}{h^3} $$

For an approaching arm ($\dot{h}<0$) there is an overpressure, largest at the closed end.

## Force on the Arm

**Vertical force.** The liquid below the arm pushes it upward with the excess pressure (the pressure $P_\infty$ acts on the whole surface of the arm and gives no net force):

$$ F_y = \int_0^L(P - P_\infty)\,dx = \frac{6\mu\dot{h}}{h^3}\left[\frac{x^3}{3} - L^2x\right]_0^L = \frac{6\mu\dot{h}}{h^3}\left(-\frac{2L^3}{3}\right) = -\frac{4\mu\dot{h}L^3}{h^3} $$

positive for $\dot{h}<0$: the liquid resists the approach (it is a force of the order of $\mu|\dot{h}|L^3/h^3$, very large for a thin film).

**Horizontal force.** Two contributions: the pressure on the inner face of the vertical leg (area $h$, normal $+\bar{e}_x$ from the arm into the liquid; the force of the liquid is $-(P_0 - P_\infty)h$) and the shear on the underside of the arm ($\bar{n} = -\bar{e}_y$, force $-\mu\,\partial v_x/\partial y$ per unit area):

$$ F_x = -(P_0 - P_\infty)\,h - \int_0^L\mu\left.\frac{\partial v_x}{\partial y}\right|_{y=h}dx, \qquad -(P_0 - P_\infty)h = \frac{6\mu\dot{h}L^2}{h^2} $$

With $\partial v_x/\partial y = \frac{P_l}{2\mu}(h - 2y)$, $P_l = -\partial P/\partial x = -12\mu\dot{h}x/h^3$: at $y = h$, $\mu\,\partial v_x/\partial y = -\frac{P_lh}{2} = \frac{6\mu\dot{h}x}{h^2}$, and

$$ -\int_0^L\frac{6\mu\dot{h}x}{h^2}\,dx = -\frac{3\mu\dot{h}L^2}{h^2}, \qquad F_x = \frac{6\mu\dot{h}L^2}{h^2} - \frac{3\mu\dot{h}L^2}{h^2} = \frac{3\mu\dot{h}L^2}{h^2} $$

$$ \bar{F} = \left(\frac{3\mu\dot{h}L^2}{h^2},\; -\frac{4\mu\dot{h}L^3}{h^3}\right), \qquad |F_x|/|F_y|\sim h/L\ll 1 $$

## Torque about the End Point $A$

The pressure on the underside of the arm gives the moment about $A$ ($x = L$) of a vertical force at the distance $x - L$ (arm positive along $\bar{e}_x\times\bar{e}_y = \bar{e}_z$):

$$ \bar{M} = -\int_0^L(P - P_\infty)(L - x)\,dx\;\bar{e}_z = -\frac{6\mu\dot{h}}{h^3}\int_0^L\left(x^2 - L^2\right)(L - x)\,dx\;\bar{e}_z $$

$$ \int_0^L\left(x^2 - L^2\right)(L - x)\,dx = \int_0^L\left(Lx^2 - x^3 - L^3 + L^2x\right)dx = L\frac{L^3}{3} - \frac{L^4}{4} - L^4 + \frac{L^4}{2} = L^4\left(\frac{1}{3} - \frac{1}{4} - 1 + \frac{1}{2}\right) = -\frac{5}{12}L^4 $$

$$ \bar{M} = \frac{5}{2}\,\frac{\mu\dot{h}}{h^3}\,L^4\;\bar{e}_z $$

The moment of the pressure on the leg is of order $\mu\dot{h}L^2/h$ (the pressure $\sim\mu\dot{h}L^2/h^3$ acting on the area $h$ with the arm $\sim h$) and the moment of the shear on the arm is $\sim\mu\dot{h}L^2/h$: a factor $(h/L)^2$ smaller than the one above and neglected, as the key does.

## Answers and Checks

- Viscous dominance: $h|\dot{h}|/\nu\ll 1$.
- Profile and flux: $v_x = \frac{P_l}{2\mu}y(h - y)$, $Q = -\dot{h}x$; pressure: $P = P_\infty + \frac{6\mu\dot{h}}{h^3}(x^2 - L^2)$, $P_0 = P_\infty - \frac{6\mu\dot{h}L^2}{h^3}$.
- Force: $\bar{F} = \left(\frac{3\mu\dot{h}L^2}{h^2}, -\frac{4\mu\dot{h}L^3}{h^3}\right)$; torque about $A$: $\bar{M} = \frac{5}{2}\frac{\mu\dot{h}L^4}{h^3}\bar{e}_z$.
- Dimensions: $\mu\dot{h}L^3/h^3$ is $ML^{-1}T^{-1}\cdot LT^{-1}\cdot L^3/L^3 = MLT^{-2}\cdot L^{-1}$, a force per unit width.
- Limits: $\dot{h}\to 0$ gives zero force, torque and overpressure; $h\to 0$ makes them grow as $h^{-3}$ (and the film does not drain in finite time at a constant $\dot{h}$ without infinite force).
- Check against the official key: VF14.pdf gives the same criterion, profile, flux, pressure, force and torque; its boxed continuity line has the opposite sign of the next one (only the second is consistent with $\partial Q/\partial x = -\dot{h}$).
