---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - lubricacion
  - fuerza-de-adhesion
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF8.pdf"
id: "vf8"
pill: "VF8: Lifting from an oil film"
sheets:
  - 8
tags_html:
  - "Squeeze film"
  - "Radial Poiseuille flow"
  - "Adhesion force"
---

# Problem VF8: Lifting a Cylinder from an Oil Film

> Official viscous-flow sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: slender film flow (Notes.pdf, Eqs. 7.64-7.71) in cylindrical coordinates, with the flux fixed by continuity and the moving boundary $y = h(t)$ (as in the wedge effect, Eq. 7.72).

## Statement

We want to lift the cylindrical body shown in the figure. A layer of oil exists between the body and the horizontal solid surface. The radial inflow caused by the lifting motion of the body is associated with the existence of underpressures in the liquid film, inducing an adhesion force to be computed here for the case of constant velocity $\dot{h} = dh/dt$.

- Show that the liquid motion in the liquid film between the body and the solid surface is dominated by viscosity for values of $h$ much smaller than $\nu/\dot{h}$.
- Obtain the radial velocity profile $v_r$ as a function of the radial pressure gradiente $P_l = -\partial P/\partial r$.
- Using continuity, derive an equation for the pressure distribution $P(r,t)$.
- Compute the pressure distribution as well as the adhesion force acting on the body.

The sheet prints "gradiente" and "pressuse".

![[attachments/FM-T7/vf8-statement.svg]]
*Statement figure (redrawn from VF8.pdf): a cylindrical body of radius R lifted with velocity ḣ from a horizontal surface; the oil film of thickness h(t) between them is fed by a radial inflow from the outer pressure P_o*

Source: VF8.pdf (page 1, statement and handwritten key; no date printed). Notes.pdf, Chapter 7: slender films, Eqs. 7.64-7.71; the wedge effect, Eq. 7.72; forces, Eq. 7.76.

## Hypotheses, Data and Unknowns

- Axisymmetric film: $\bar{v} = (v_r, v_y)$ with $y$ the distance to the solid surface and $r$ the radial coordinate from the axis; the film is slender, $h\ll R$.
- The body moves up with the constant velocity $\dot{h} = dh/dt$ and its lower face stays flat, so $v_y = \dot{h}$ there; the oil is in contact with the surface at $y = 0$ ($v_y = 0$). At the edge $r = R$ the pressure is the outer one, $P_o$ (the key writes $P_0$).
- Gravity is absorbed in the reduced pressure $P$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R$ | radius of the body | m |
| $h(t)$, $\dot{h}$ | thickness of the film and its rate | m, m/s |
| $\mu$, $\nu$ | viscosity of the oil | kg/(m s), m$^2$/s |

## Criterion for Viscous Dominance

By continuity in the film, $\partial(rv_r)/\partial r + r\,\partial v_y/\partial y = 0$ gives $v_r/R\sim v_y/h\sim\dot{h}/h$, so the radial velocity scale is $V_L\sim R\dot{h}/h$ and the time scale of the process is $t_0\sim h/\dot{h}$. Local acceleration against viscous force (Eq. 7.67) and convective acceleration against viscous force (Eq. 7.68):

$$ \frac{O(\rho\,\partial v_r/\partial t)}{O(\mu\nabla^2\bar{v})} = \frac{h^2/\nu}{t_0}\sim\frac{h\dot{h}}{\nu}, \qquad \frac{O(\rho\bar{v}\cdot\nabla\bar{v})}{O(\mu\nabla^2\bar{v})} = \frac{V_Lh}{\nu}\,\frac{h}{R}\sim\frac{R\dot{h}}{h}\,\frac{h}{\nu}\,\frac{h}{R} = \frac{h\dot{h}}{\nu} $$

Both are small when $h\dot{h}/\nu\ll 1$, that is

$$ h\ll\frac{\nu}{\dot{h}} $$

## Radial Velocity Profile

With negligible inertia and uniform pressure across the film, the radial momentum equation is (Eq. 7.69)

$$ 0 = -\frac{\partial P}{\partial r} + \mu\frac{\partial^2v_r}{\partial y^2}; \qquad y = 0:\; v_r = 0, \qquad y = h:\; v_r = 0 $$

Integrating twice, with $P_l = -\partial P/\partial r$ independent of $y$: $\mu v_r = -P_ly^2/2 + C_1y + C_2$, $C_2 = 0$, $C_1 = P_lh/2$:

$$ v_r = \frac{P_l}{2\mu}\,y\,(h - y) = -\frac{h^2}{2\mu}\frac{\partial P}{\partial r}\,\frac{y}{h}\left(1 - \frac{y}{h}\right) $$

The flux per unit length of circumference is $\int_0^hv_r\,dy = P_lh^3/(12\mu)$ (as in Eq. 7.11).

## Equation for the Pressure

Integrate the continuity equation $\frac{\partial(rv_r)}{\partial r} + \frac{\partial(rv_y)}{\partial y} = 0$ across the film:

$$ \int_0^h\left[\frac{\partial(rv_r)}{\partial r} + \frac{\partial(rv_y)}{\partial y}\right]dy = \frac{\partial}{\partial r}\left(r\int_0^hv_r\,dy\right) + r\left[v_y(h) - v_y(0)\right] = 0 $$

(the Leibniz term with $dh/dr$ is zero because $h$ does not depend on $r$). With $v_y(0) = 0$ and $v_y(h) = \dot{h}$ (kinematic condition on the moving body):

$$ -\frac{\partial}{\partial r}\left(r\,\frac{h^3}{12\mu}\,\frac{\partial P}{\partial r}\right) + r\dot{h} = 0; \qquad r = 0:\; \frac{\partial P}{\partial r} = 0, \qquad r = R:\; P = P_o $$

## Pressure Distribution and Adhesion Force

Integrating from the axis (Barrow, with $r\,\partial P/\partial r = 0$ at $r = 0$): $-r\frac{h^3}{12\mu}\frac{\partial P}{\partial r} + \dot{h}\frac{r^2}{2} = 0$, so $\frac{\partial P}{\partial r} = \frac{6\mu\dot{h}}{h^3}\,r$, and integrating from $R$ to $r$ with $P(R) = P_o$:

$$ P - P_o = \frac{6\mu\dot{h}}{h^3}\,\frac{r^2 - R^2}{2} = \frac{3\mu}{h^3}\,\dot{h}\left(r^2 - R^2\right) $$

For $\dot{h} > 0$ (lifting), $P < P_o$ in the whole film: an **underpressure**, largest on the axis, $P(0) - P_o = -3\mu\dot{h}R^2/h^3$.

The oil acts on the base of the body with the normal pointing from the body into the liquid, $\bar{n} = -\bar{e}_y$, so the force is $-\int(P - P_o)\bar{n}\,d\sigma = \int(P - P_o)\,d\sigma\,\bar{e}_y$ (the uniform $P_o$ gives no net force on the closed body):

$$ \bar{F} = \int_0^R2\pi r\,(P - P_o)\,dr\,\bar{e}_y = \frac{6\pi\mu\dot{h}}{h^3}\left[\frac{r^4}{4} - \frac{R^2r^2}{2}\right]_0^R\bar{e}_y = -\frac{3\pi}{2}\,\mu\,\frac{R^4}{h^3}\,\dot{h}\,\bar{e}_y $$

The force is downward: the underpressure **holds the body back** (adhesion), and grows as $h^{-3}$ when the film is thin and with the velocity of lifting.

## Answers and Checks

- Viscous dominance: $h\ll\nu/\dot{h}$ (and $h\ll R$).
- Radial profile: $v_r = -\frac{h^2}{2\mu}\frac{\partial P}{\partial r}\frac{y}{h}\left(1 - \frac{y}{h}\right)$; equation: $-\frac{\partial}{\partial r}\left(r\frac{h^3}{12\mu}\frac{\partial P}{\partial r}\right) + r\dot{h} = 0$.
- Pressure: $P - P_o = \frac{3\mu\dot{h}}{h^3}(r^2 - R^2)$; force: $\bar{F} = -\frac{3\pi}{2}\mu\frac{R^4}{h^3}\dot{h}\,\bar{e}_y$.
- Dimensions: $\mu R^4\dot{h}/h^3$ is $ML^{-1}T^{-1}\cdot L^4\cdot LT^{-1}/L^3 = MLT^{-2}$, a force.
- Consistency: the total volume flux leaving through $r = R$ is $2\pi R\cdot\left(-P_l h^3/(12\mu)\right)$ at $R$, with $P_l = -6\mu\dot{h}R/h^3$ there: $2\pi R\cdot\frac{6\mu\dot{h}R}{h^3}\cdot\frac{h^3}{12\mu} = \pi R^2\dot{h}$, the volume swept by the body (negative sign: inflow), as continuity requires.
- Check against the official key: VF8.pdf gives the same scale analysis, profile, pressure equation, $P - P_o = 3\mu\dot{h}(r^2 - R^2)/h^3$ and $F = -\frac{3\pi}{2}\mu R^4\dot{h}/h^3$.
