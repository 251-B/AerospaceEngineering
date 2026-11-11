---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - flujo-anular
  - bomba-viscosa
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF19.pdf"
id: "vf19"
pill: "VF19: Rod pump"
sheets:
  - 19
tags_html:
  - "Annulus"
  - "Moving rod"
  - "Flux and minimum velocity"
---

# Problem VF19: Viscous Pump with a Moving Rod

> Official viscous-flow sheet of the course (final exam of Jan 21, 2014), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: steady flow in an annulus in cylindrical coordinates (Notes.pdf, Eqs. 7.7 and 7.13, with both constants fixed by no slip, as in [[Problem - VF3 Annular Flow with a Moving Outer Cylinder]]), reduced pressure fixed at both ends of the pipe, and the force from the wall shear.

## Statement

**Problem 4:** To fill an open container of depth $H$ located at a height $L$ above the surface of a reservoir we use the viscous pumping system sketched in the figure, including a pipe or radius $R_2$ connecting the surface of the reservoir with the bottom of the container and an infinitely long, inner, coaxial rod of radius $R_1$ that moves vertically with velocity $U$, dragging the water into the inter-cylinder gap.

1. Give the condition for the flow in the gap to be dominated by viscosity.

2. Obtain the velocity profile $v_z(r)$ across the gap.

3. Determine the loss of reduced pressure per unit length $P_l = -\partial P/\partial z$.

4. Compute the force acting on the moving shaft and the power needed to move it.

5. Determine the volume flow rate $Q$ of the pumping system, including the minimum velocity $U_{min}$ required for $Q>0$.

The sheet prints "a pipe or radius $R_2$" ("or" for "of").

![[attachments/FM-T7/vf19-statement.svg]]
*Statement figure (redrawn from VF19.pdf): a reservoir at p_a, a vertical pipe of radius R_2 and length L up to the bottom of an open container of depth H, and a coaxial rod of radius R_1 moving up with velocity U inside the pipe; z is vertical and r radial*

Source: VF19.pdf (page 1, final exam of Jan 21, 2014; statement and handwritten key). Notes.pdf, Chapter 7: steady flow in a circular pipe, Eqs. 7.13-7.16; slender flows, Eqs. 7.40-7.46.

## Hypotheses, Data and Unknowns

- The gap between the rod ($r = R_1$, moving with $+U\bar{e}_z$) and the pipe ($r = R_2$, at rest) has the length $L$ and is slender, $R_2 - R_1\ll L$; the flow is steady and axisymmetric, $v_z(r)$.
- $z$ is the height above the reservoir surface. At the entrance of the pipe ($z = 0$) $p = p_a$; at its exit ($z = L$, the bottom of the container, under a depth $H$ of water at $p_a$ on top) $p = p_a + \rho gH$. The reduced pressure is $P = p + \rho gz$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R_1$, $R_2$ | radii of the rod and of the pipe | m |
| $L$, $H$ | length of the pipe, depth of the container | m |
| $U$ | velocity of the rod (upward) | m/s |
| $\Delta = R_2^2 - R_1^2$, $\Lambda = \ln(R_2/R_1)$ | abbreviations | m$^2$, 1 |

## Criterion for Viscous Dominance

The slender-flow condition (Eq. 7.41), with the width $R_2 - R_1$ of the gap, the velocity $U$ and the length $L$:

$$ \frac{\rho U\left(R_2 - R_1\right)}{\mu}\,\frac{R_2 - R_1}{L} = \frac{\rho U\left(R_2 - R_1\right)^2}{\mu L}\ll 1 $$

(the same with the velocity driven by the pressure, of order $P_l(R_2 - R_1)^2/\mu$, if it is larger than $U$).

## Velocity Profile

Equation (7.7) in steady state with no slip on both walls:

$$ 0 = P_l + \frac{\mu}{r}\frac{d}{dr}\left(r\frac{dv_z}{dr}\right); \qquad r = R_1:\; v_z = U, \qquad r = R_2:\; v_z = 0 $$

As in VF3, the solution is $v_z = \frac{P_l}{4\mu}\left(R_2^2 - r^2\right) + C\ln\frac{R_2}{r}$, which is zero at $r = R_2$; the rod condition gives $U = \frac{P_l}{4\mu}\Delta + C\Lambda$:

$$ v_z = \frac{P_l}{4\mu}\left(R_2^2 - r^2\right) + \left[U - \frac{P_l}{4\mu}\left(R_2^2 - R_1^2\right)\right]\frac{\ln(R_2/r)}{\ln(R_2/R_1)} $$

## Pressure Loss per Unit Length

The gap has constant section, so $P_l$ is uniform. The reduced pressure at the entrance is $p_a$ and at the exit $p_a + \rho gH + \rho gL$:

$$ P_l = -\frac{\partial P}{\partial z} = \frac{p_a - \left[p_a + \rho g(H + L)\right]}{L} = -\frac{\rho g(H + L)}{L} $$

negative: the pressure (reduced) increases along the flow, opposing it; the rod has to push the water against the weight of the whole column from the reservoir to the top of the container.

## Force on the Rod and Power

The force of the liquid on the rod (normal from the rod into the liquid, $\bar{n} = +\bar{e}_r$) per unit area is $\tau_w = \mu\,\partial v_z/\partial r|_{r=R_1}$. With $\frac{dv_z}{dr} = -\frac{P_l}{2\mu}r - \frac{C}{r}$:

$$ \tau_w = -\frac{P_lR_1}{2} - \frac{\mu C}{R_1} = -\frac{\mu U}{R_1\Lambda} - \frac{P_lR_1}{2}\left[1 - \frac{1}{2}\,\frac{R_2^2/R_1^2 - 1}{\ln(R_2/R_1)}\right] $$

(using $C = \left(U - P_l\Delta/(4\mu)\right)/\Lambda$). With $P_l = -\rho g(H + L)/L$ both terms are negative: the liquid resists the motion of the rod, because $\frac{\Delta}{2R_1^2\Lambda} = \frac{x^2 - 1}{2\ln x}>1$ for $x = R_2/R_1>1$. The force on the rod over the length $L$ is $F_z = 2\pi R_1L\,\tau_w\,\bar{e}_z$, downward, and the power that must be supplied to move it is minus the power of that force (the key writes $W = U\,2\pi R_1L\,\tau_w$, the power of the force of the liquid, negative):

$$ W = -2\pi R_1LU\tau_w = 2\pi R_1LU\left[\frac{\mu U}{R_1\ln(R_2/R_1)} + \frac{\rho g(H + L)R_1}{2L}\left(\frac{R_2^2 - R_1^2}{2R_1^2\ln(R_2/R_1)} - 1\right)\right] $$

The key's lines end at the expression of $\tau_w$ without writing the final value.

## Volume Flux and Minimum Velocity

$Q = \int_{R_1}^{R_2}2\pi r\,v_z\,dr$. Barrow's rule for the two terms:

$$ \int_{R_1}^{R_2}r\left(R_2^2 - r^2\right)dr = \left[\frac{R_2^2r^2}{2} - \frac{r^4}{4}\right]_{R_1}^{R_2} = \frac{\left(R_2^2 - R_1^2\right)^2}{4}, \qquad \int_{R_1}^{R_2}r\ln\frac{R_2}{r}\,dr = \left[\frac{r^2}{2}\ln\frac{R_2}{r} + \frac{r^2}{4}\right]_{R_1}^{R_2} = \frac{R_2^2 - R_1^2}{4} - \frac{R_1^2}{2}\ln\frac{R_2}{R_1} $$

$$ Q = \frac{\pi P_l\Delta^2}{8\mu} + \frac{\pi}{2}\left(U - \frac{P_l\Delta}{4\mu}\right)\frac{\Delta - 2R_1^2\Lambda}{\Lambda} $$

> [!warning] Discrepancy with the official solution
> The key gives $Q = -2\pi\left\{\frac{P_l}{16\mu}\left(R_2^4 - R_1^4\right) + \frac{U - P_l\Delta/(4\mu)}{4\ln(R_2/R_1)}\left[R_2^2\left(2\ln R_2 - 1\right) - R_1^2\left(2\ln R_1 - 1\right)\right]\right\}$, which is not the integral of its own velocity profile. The first term should have $\left(R_2^2 - R_1^2\right)^2$ (the integral of $r(R_2^2 - r^2)$, as above), not $R_2^4 - R_1^4$; and the second keeps only the antiderivative of $r\ln r$ and drops the constant term that comes from $\ln R_2$ (a logarithm of a dimensional length appears, which is dimensionally meaningless); the overall sign is also the opposite. As a consequence the key's minimum velocity, solved from its own $Q = 0$, is not the one of the integral. The results above are used.

Checks of $Q$: for $R_1\to 0$, $\Delta\to R_2^2$, $R_1^2\Lambda\to 0$, $\Lambda\to\infty$ and the second term vanishes: $Q\to\frac{\pi P_lR_2^4}{8\mu}$, the Poiseuille flux (7.15). For a thin gap $g = R_2 - R_1\ll R_1$, $(\Delta - 2R_1^2\Lambda)/\Lambda\simeq 2R_1^2\epsilon = 2R_1g$ to first order in $\epsilon = g/R_1$, so the second term is $\pi R_1^2\epsilon U = \pi R_1gU$, the Couette flux $\frac{Ug}{2}\cdot2\pi R_1$.

**Minimum velocity.** Setting $Q = 0$: $\left(U - \frac{P_l\Delta}{4\mu}\right) = -\frac{P_l\Delta^2}{4\mu}\frac{\Lambda}{\Delta - 2R_1^2\Lambda}$, so

$$ U_{min} = \frac{P_l\Delta}{4\mu}\left[1 - \frac{\Delta\,\Lambda}{\Delta - 2R_1^2\Lambda}\right] = \frac{\rho g(H + L)\left(R_2^2 - R_1^2\right)}{4\mu L}\left[\frac{\left(R_2^2 - R_1^2\right)\ln(R_2/R_1)}{R_2^2 - R_1^2 - 2R_1^2\ln(R_2/R_1)} - 1\right] $$

positive, since $\frac{\Delta\Lambda}{\Delta - 2R_1^2\Lambda}>1$. For $U>U_{min}$ the rod pumps water to the container ($Q>0$).

## Answers and Checks

- Viscous dominance: $\rho U(R_2 - R_1)^2/(\mu L)\ll 1$.
- Velocity: $v_z = \frac{P_l}{4\mu}(R_2^2 - r^2) + \left[U - \frac{P_l}{4\mu}(R_2^2 - R_1^2)\right]\frac{\ln(R_2/r)}{\ln(R_2/R_1)}$; $P_l = -\rho g(H + L)/L$.
- Force on the rod: $F_z = 2\pi R_1L\tau_w$ with $\tau_w$ above; power supplied: $W = -2\pi R_1LU\tau_w>0$.
- Flux: $Q = \frac{\pi P_l\Delta^2}{8\mu} + \frac{\pi}{2}\left(U - \frac{P_l\Delta}{4\mu}\right)\frac{\Delta - 2R_1^2\Lambda}{\Lambda}$; $U_{min}$ as above.
- Dimensions: $\rho g(H + L)\Delta/(\mu L)$ is $ML^{-3}\cdot LT^{-2}\cdot L^2/(ML^{-1}T^{-1}) = LT^{-1}$, a velocity; $\Delta^2P_l/\mu$ is $L^4\cdot ML^{-2}T^{-2}/(ML^{-1}T^{-1}) = L^3T^{-1}$, a volume flux (as in (7.15)).
- Check against the official key: VF19.pdf gives the same criterion, profile, $P_l$ and shear; its $Q$ and $U_{min}$ differ, as noted, and it does not write the final value of the power.
