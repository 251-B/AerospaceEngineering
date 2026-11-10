---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - lubricacion
  - cuña-giratoria
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF13.pdf"
id: "vf13"
pill: "VF13: Rotating plate"
sheets:
  - 13
tags_html:
  - "Opening wedge"
  - "Unsteady film"
  - "Torque"
---

# Problem VF13: Rotating Plate over a Wall

> Official viscous-flow sheet of the course (exam of Dec 16, 2011), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: slender film between a plate and a wall (Notes.pdf, Eqs. 7.64-7.71), continuity across the film with a moving boundary (Eq. 7.72), and the moment of the pressure on the plate (Eq. 7.76).

## Statement

A plate of length $L$ is initially sitting on a horizontal plane in the presence of a stagnant liquid atmosphere with reduced pressure $P_\infty$. At a given instant, we begin to rotate the plate with constant angular velocity $\omega = d\alpha/dt$ by applying a given torque $M$ at its left end, as sketched in the figure. For the analysis, use the approximation $h(x,t) = x\tan(\alpha)\simeq x\alpha$, valid for $\alpha\ll 1$.

1. Demonstrate that for values of $\alpha$ sufficiently smaller than a critical value, to be determined, the fluid motion in the gap formed between the plate and the wall is dominated by viscosity.

2. Obtain the velocity profile $v_x$ in the gap as a function of the unknwon value of $P_l(x,t) = -\partial P/\partial x$ as well as the associated volume flux at a given section $Q = \int_0^{\alpha x}v_x\,dy$.

3. Using continuity, write an equation linking $Q$ and $\omega$, and integrate it to compute the pressure distribution $P(x,t)$ (in the integration, you may anticipate that $x^3P_l\to 0$ as $x\to 0$).

4. Determine the torque $M(t)$ needed to provide a constant angular velocity $\omega$.

The sheet prints "unknwon" and, in item 3, a stray character before "it".

![[attachments/FM-T7/vf13-statement.svg]]
*Statement figure (redrawn from VF13.pdf): a plate of length L hinged at O on a horizontal wall, rotating with ω = dα/dt under the torque M; the gap is h(x, t) = αx and the surrounding liquid is at P_∞*

Source: VF13.pdf (page 1, exam of Dec 16, 2011, statement and handwritten key). Notes.pdf, Chapter 7: slender films, Eqs. 7.67-7.71; the wedge effect, Eq. 7.72; forces and moments, Eq. 7.76.

## Hypotheses, Data and Unknowns

- The plate is hinged at the origin $O$ and rises with the angle $\alpha(t)$ ($\alpha\ll 1$): $x$ runs along the wall from $O$, $y$ is vertical and the gap is $h = \alpha x$, increasing with time, so liquid has to flow **in** from the surroundings to fill the wedge that opens.
- The gap is slender ($h\ll x$) and the pressure is uniform across it; at the outer end $x = L$ the pressure is $P_\infty$; at the hinge no flux ($Q = 0$ at $x = 0$).
- The plate surface moves with the velocity $v_y = \partial h/\partial t = \omega x$ (to the first order in $\alpha$).

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $L$, $\alpha(t)$ | length of the plate and its angle | m, rad |
| $\omega = d\alpha/dt$ | constant angular velocity | s$^{-1}$ |
| $P_\infty$ | reduced pressure of the surrounding liquid | Pa |
| $M$ | torque at $O$ (per unit width) | N |

## Criterion for Viscous Dominance

The scales are $h_c\sim L\alpha$ (largest gap) and $t_0 = \alpha/\omega$ (time to change the angle by its own value). The continuity equation $\partial v_x/\partial x + \partial v_y/\partial y = 0$ with $v_y\sim\omega L$ gives $V_L\sim\omega L^2/h_c = \omega L/\alpha$. Local acceleration and convective acceleration against the viscous force (Eqs. 7.67-7.68):

$$ \frac{h_c^2/\nu}{t_0}\sim\frac{L^2\alpha^2\omega}{\nu\alpha} = \frac{\omega L^2\alpha}{\nu}, \qquad \frac{V_Lh_c}{\nu}\frac{h_c}{L}\sim\frac{\omega L}{\alpha}\frac{L\alpha}{\nu}\,\alpha = \frac{\omega L^2\alpha}{\nu} $$

Both are the same number, and viscosity dominates if it is much smaller than one:

$$ \alpha\ll\alpha_c = \frac{\nu}{\omega L^2} $$

(and of course $\alpha\ll 1$).

## Velocity Profile and Flux

Equation (7.69) with the no-slip conditions at the wall ($y = 0$) and at the plate ($y = h$), both at rest in this approximation (the normal motion of the plate is the continuity term), integrated as for (7.11):

$$ v_x = \frac{P_l}{2\mu}\,y\,(h - y), \qquad Q = \frac{P_lh^3}{12\mu} = -\frac{\alpha^3x^3}{12\mu}\frac{\partial P}{\partial x} $$

## Continuity and Pressure

Integrate $\partial v_x/\partial x + \partial v_y/\partial y = 0$ across the gap:

$$ \int_0^h\frac{\partial v_x}{\partial x}\,dy + \int_0^h\frac{\partial v_y}{\partial y}\,dy = \frac{\partial Q}{\partial x} - \frac{dh}{dx}\,v_x(y = h) + v_y(h) - v_y(0) = 0 $$

The term $\frac{dh}{dx}v_x(y = h)$ vanishes because $v_x(h) = 0$ (no slip on the plate), $v_y(0) = 0$ on the wall and $v_y(h) = \partial h/\partial t = \omega x$:

$$ \frac{\partial Q}{\partial x} + \omega x = 0 $$

Integrating with $Q = 0$ at $x = 0$: $Q = -\omega x^2/2$ (negative: inflow towards the hinge). Equating with the flux of the profile:

$$ -\frac{\alpha^3x^3}{12\mu}\frac{\partial P}{\partial x} = -\frac{\omega x^2}{2} \;\Longrightarrow\; \frac{\partial P}{\partial x} = \frac{6\mu\omega}{\alpha^3}\,\frac{1}{x} $$

(the constant of integration of the first step is zero because $x^3P_l\to 0$ as $x\to 0$). Integrating from $L$ to $x$ with $P(L) = P_\infty$:

$$ P - P_\infty = \frac{6\mu\omega}{\alpha^3}\,\ln\frac{x}{L} $$

negative for $x < L$: an underpressure that grows without bound near the hinge (logarithmically) and tends to hold the plate down.

## Torque

The moment of the pressure on the plate about the hinge, per unit width, with the pressure acting on its underside (the force is vertical to this order, at the position $x$):

$$ M_{liquid} = \int_0^L(P - P_\infty)\,x\,dx\;\bar{e}_z = \frac{6\mu\omega}{\alpha^3}\int_0^Lx\ln\frac{x}{L}\,dx\;\bar{e}_z, \qquad \int_0^Lx\ln\frac{x}{L}dx = L^2\int_0^1u\ln u\,du = L^2\left[\frac{u^2}{2}\ln u - \frac{u^2}{4}\right]_0^1 = -\frac{L^2}{4} $$

$$ M_{liquid} = -\frac{3}{2}\,\frac{\mu\omega L^2}{\alpha^3}\,\bar{e}_z $$

The liquid opposes the rotation (the rotation is counterclockwise, $+\bar{e}_z$), so the torque that must be applied is the opposite, positive:

$$ \bar{M} = \frac{3}{2}\,\frac{\mu\,\omega\,L^2}{\alpha^3}\,\bar{e}_z $$

It grows as $\alpha^{-3}$ at the start of the motion (small $\alpha$). The shear on the plate gives a moment smaller by a factor $\alpha$.

## Answers and Checks

- Viscous dominance: $\alpha\ll\nu/(\omega L^2)$.
- Profile and flux: $v_x = \frac{P_l}{2\mu}y(h - y)$, $Q = \frac{P_lh^3}{12\mu} = -\frac{\omega x^2}{2}$.
- Pressure: $P - P_\infty = \frac{6\mu\omega}{\alpha^3}\ln(x/L)$. Torque: $M = \frac{3}{2}\mu\omega L^2/\alpha^3$.
- Dimensions: $\mu\omega L^2/\alpha^3$ is $ML^{-1}T^{-1}\cdot T^{-1}\cdot L^2 = MT^{-2}\cdot L$, a torque per unit width (N); $\nu/(\omega L^2)$ is dimensionless.
- Consistency: the volume flowing in through $x = L$ is $|Q(L)| = \omega L^2/2$ per unit width, equal to the area of the wedge swept per unit time, $\frac{d}{dt}\left(\frac{1}{2}L\cdot\alpha L\right) = \omega L^2/2$.
- Check against the official key: VF13.pdf gives the same criterion, profile, flux, pressure (with $P(L) = P_\infty$) and torque; the key does not write the kinematic condition $v_y(h) = \omega x$, the constant of integration or the boundary condition, which are stated above.
