---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - pelicula-delgada
  - chorro
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF20.pdf"
id: "vf20"
pill: "VF20: Jet-supported cylinder"
sheets:
  - 20
tags_html:
  - "Radial Poiseuille flow"
  - "Thin film"
  - "Force balance"
---

# Problem VF20: Cylinder Levitated by a Jet

> Official viscous-flow sheet of the course (exam of 16-01-2019), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: radial Poiseuille flow in a thin gap (Notes.pdf, Eqs. 7.69-7.71 in cylindrical coordinates) with the flux fixed by the jet, and the equilibrium of the cylinder.

## Statement

**FLUID MECHANICS I. PROBLEM 2 (10 POINTS). 16-01-2019. Time: 75 minutes.** The cylinder of radius $R$ and height $2R$ shown in the figure is submerged in an infinite tank of liquid of density $\rho$ and viscosity $\mu$. The cylinder, of density $\rho_s>\rho$, is sustained at a constant height $h\ll R$ by the effect of a narrow jet of volumetric flow rate $Q$ and radius of the order of $h$, injected at the center of the base of the cylinder (see the sketch). Assuming the fluid movement is negligible in the bulk of the tank ($P_0$ = const.) and the flow below the cylinder is dominated by viscosity, we want to determine the dependence of $h$ as a function of $Q$. To this end, the following sequence is suggested:

1. Give the criterion, as a function of the known parameters, for the flow in the gap of width $h$ between the cylinder and the bottom of the tank to be dominated by viscosity.

2. Determine the velocity profile as a function of the local reduced pressure gradient $\partial P/\partial r$.

3. Obtain the local flow rate $q(r)$ at a generic radial position $r$

4. Use the continuity equation to derive an equation for the reduced pressure $P$, with all needed boundary conditions. Obtain $P$.

5. Determine $h$

![[attachments/FM-T7/vf20-statement.svg]]
*Statement figure (redrawn from VF20.pdf): a cylinder of radius R, height 2R and density ρ_s hovering at the height h above the bottom of a tank of liquid (ρ, μ, pressure P_0 far away) on a jet of flow rate Q injected at the centre of its base; z is vertical and r radial*

Source: VF20.pdf (page 1: statement; pages 2 and 3: handwritten key; exam of 16-01-2019). Notes.pdf, Chapter 7: slender films, Eqs. 7.67-7.71; the wedge effect, Eq. 7.72.

## Hypotheses, Data and Unknowns

- The gap between the base of the cylinder ($z = h$) and the bottom of the tank ($z = 0$) is slender, axisymmetric and steady; the liquid enters it through the jet at the centre ($r\lesssim h$) and leaves at $r = R$ to the tank, where the reduced pressure is $P_0$ (the liquid is at rest there).
- Reduced pressure $P = p + \rho gz$. The cylinder is in equilibrium: its weight $W = 2\pi R^3\rho_sg$ (volume $2\pi R^3$) balances the force of the liquid.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R$, $2R$ | radius and height of the cylinder | m |
| $\rho_s$, $\rho$, $\mu$ | density of the cylinder, of the liquid, viscosity | kg/m$^3$, kg/m$^3$, kg/(m s) |
| $h$, $Q$ | height of the gap, flux of the jet | m, m$^3$/s |

## Criterion for Viscous Dominance

The convective acceleration is negligible against the viscous force (Eq. 7.41) when $\frac{\rho V_{zc}h}{\mu}\frac{h}{R}\ll 1$, with $V_{zc}$ the velocity scale of the jet, of radius $\sim h$, so $V_{zc}\sim Q/h^2$. The radial velocity in the gap follows from the flux, $v_r = Q/(2\pi rh)$, which is $\sim Q/h^2\sim V_{zc}$ at the entrance $r\sim h$. Then

$$ \frac{\rho V_{zc}h}{\mu}\,\frac{h}{R}\sim\frac{\rho Q}{\mu h}\,\frac{h}{R} = \frac{\rho Q}{\mu R}\ll 1 $$

(the key states $V_r\sim Q/h^2$ for $r\sim h$ and boxes the result). This is the estimate of the key, with the global slenderness $h/R$. More locally, at a radius $r$ the ratio of convective to viscous terms is $\rho v_rh^2/(\mu r) = \rho Qh/(2\pi\mu r^2)$, which decreases with $r$: it is largest near the entrance, where it is of order $\rho Q/(\mu h)$ (stricter than the boxed $\rho Q/(\mu R)$ by $R/h$), and the slender-film solution below is valid for $r\gg h$ when $\rho Qh/(\mu r^2)\ll 1$ there.

## Velocity Profile and Flux

Radial momentum in the gap (Eq. 7.69 in cylindrical coordinates), with no slip at the bottom of the tank ($z = 0$) and at the base of the cylinder ($z = h$):

$$ 0 = -\frac{\partial P}{\partial r} + \mu\frac{\partial^2v_r}{\partial z^2}; \qquad z = 0:\; v_r = 0, \qquad z = h:\; v_r = 0 $$

Integrating twice, $v_r = \frac{1}{2\mu}\frac{\partial P}{\partial r}z^2 + Az$ ($B = 0$ by the condition at $z = 0$), and $0 = \frac{1}{2\mu}\frac{\partial P}{\partial r}h^2 + Ah$ gives $A$:

$$ v_r = -\frac{1}{2\mu}\,\frac{\partial P}{\partial r}\left(hz - z^2\right) $$

The local flux through the cylinder of radius $r$ and height $h$ is

$$ q(r) = \int_0^h2\pi r\,v_r\,dz = -\frac{2\pi r}{2\mu}\frac{\partial P}{\partial r}\left[\frac{hz^2}{2} - \frac{z^3}{3}\right]_0^h = -\frac{\pi h^3r}{6\mu}\frac{\partial P}{\partial r} $$

## Pressure

Continuity in the gap: no liquid enters or leaves through the bottom or the base (both are walls), so $q(r) = Q$ for every $r$:

$$ Q = -\frac{\pi h^3r}{6\mu}\frac{\partial P}{\partial r} \;\Longrightarrow\; \frac{\partial P}{\partial r} = -\frac{6\mu Q}{\pi h^3r} $$

Integrating in $r$ with the boundary condition $P = P_0$ at $r = R$:

$$ P = P_0 - \frac{6\mu Q}{\pi h^3}\,\ln\frac{r}{R} $$

an overpressure for $r<R$, which grows (logarithmically) towards the centre, where the slender approximation stops being valid (at $r\sim h$).

## Height of the Cylinder

The force of the liquid on the cylinder is the difference of the pressures on its base and on its top, over the area $\pi R^2$ (the lateral pressure is horizontal). At the top, $z = h + 2R$, the liquid is at rest with the reduced pressure $P_0$, so $p_t = P_0 - \rho g(h + 2R)$; at the base, $p_b = P - \rho gh$:

$$ F = \int_0^R2\pi r\left(p_b - p_t\right)dr = \int_0^R2\pi r\left[2\rho gR + (P - P_0)\right]dr = 2\pi\rho gR^3 - \frac{12\mu Q}{h^3}\int_0^Rr\ln\frac{r}{R}\,dr $$

With $r = Rs$, $\int_0^Rr\ln\frac{r}{R}dr = R^2\int_0^1s\ln s\,ds = R^2\left[\frac{s^2}{2}\ln s - \frac{s^2}{4}\right]_0^1 = -\frac{R^2}{4}$:

$$ F = 2\pi\rho gR^3 + \frac{3\mu QR^2}{h^3} $$

The first term is the buoyancy (the weight of the displaced liquid, $\rho g\cdot2\pi R^3$) and the second is the lift of the jet. The cylinder floats at the height $h$ when $F = W = 2\pi R^3\rho_sg$:

$$ \frac{3\mu QR^2}{h^3} = 2\pi R^3g\left(\rho_s - \rho\right) \;\Longrightarrow\; h = \left[\frac{3\mu QR^2}{2\pi R^3g\left(\rho_s - \rho\right)}\right]^{1/3} = \left[\frac{3\mu Q}{2\pi Rg\left(\rho_s - \rho\right)}\right]^{1/3} $$

## Answers and Checks

- Viscous dominance: $\rho Q/(\mu R)\ll 1$ (and $h\ll R$).
- Profile: $v_r = -\frac{1}{2\mu}\frac{\partial P}{\partial r}(hz - z^2)$; flux: $q = -\frac{\pi h^3r}{6\mu}\frac{\partial P}{\partial r} = Q$; pressure: $P = P_0 - \frac{6\mu Q}{\pi h^3}\ln\frac{r}{R}$.
- Height: $h = \left[\frac{3\mu Q}{2\pi Rg(\rho_s - \rho)}\right]^{1/3}$.
- Dimensions: $\mu Q/(Rg\Delta\rho)$ is $ML^{-1}T^{-1}\cdot L^3T^{-1}/(L\cdot LT^{-2}\cdot ML^{-3}) = L^3$, so $h$ is a length; $\rho Q/(\mu R)$ is $ML^{-3}L^3T^{-1}/(ML^{-1}T^{-1}L) = 1$.
- Limits: $Q\to 0$ gives $h\to 0$ (the cylinder rests on the bottom) and $h\propto Q^{1/3}$; $\rho_s\to\rho$ makes the cylinder neutrally buoyant and $h\to\infty$ (it floats with any $Q$).
- Check against the official key: VF20.pdf gives the same criterion (stated without the step $V_{zc}\sim Q/h^2$), profile, $q$, $P$, force ($2\pi\rho gR^3 + 3\mu QR^2/h^3$) and $h$ (left as $\left[3\mu QR^2/(2\pi R^3g(\rho_s - \rho))\right]^{1/3}$).
