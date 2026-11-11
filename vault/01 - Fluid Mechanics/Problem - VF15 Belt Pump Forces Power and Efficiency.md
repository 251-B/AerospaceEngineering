---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - bomba-viscosa
  - eficiencia
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF15.pdf"
id: "vf15"
pill: "VF15: Belt pump efficiency"
sheets:
  - 15
tags_html:
  - "Couette + Poiseuille"
  - "Forces on the belts"
  - "Efficiency"
---

# Problem VF15: Belt Pump: Forces, Power and Efficiency

> Official viscous-flow sheet of the course (exam of Dec 18, 2012), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: Couette plus Poiseuille flow between two moving walls (Notes.pdf, Eqs. 7.9-7.12), forces from the wall shear (Eq. 7.16 convention) and the energy balance of the pump. It is the continuation of [[Problem - DA10 Two-Belt Viscous Pump]], Problem 3 of the same exam.

## Statement

**PROBLEM 4 (1 hour)** The system sketched in the figure is designed to steadily pump fluid of constant density $\rho$ and constant viscosity $\mu$ from a reservoir, where the modified pressure has a constant value $P_0$, to another one at pressure $P_0 + \Delta P$ ($\Delta P > 0$). To that end, a pair of parallel belts of length $L$, separated by a distance $h\ll L$, are driven at constant velocities $V_l$ and $V_u$, dragging the liquid towards the large pressure reservoir.

The liquid flow can be assumed steady, two-dimensional (spanwise length much larger than $h$), and dominated by viscous forces in the gap. It proves convenient to introduce a cartersian coordinate system $(x, y)$, where $x$ and $y$ are the directions parallel and perpendicular to the belts, respectively. The **only** known parameters are $(\rho, \mu, P_0, \Delta P, L, h, V_l, V_u)$.

1. (1 point). Under the assumption of dominant viscous forces, obtain the characteristic velocity, $V_{\Delta P}$, induced in the liquid by the overpressure $\Delta P$. Show that the pump will only work if the dimensionless parameter $\Lambda = (h^2\Delta P)/[\mu L(V_l + V_u)]$, is sufficiently small.

2. (1 point). Provide the condition(s) that must be satisfied for the flow to be dominated by viscous forces.

3. (2 points). Determine the streamwise velocity profile in the gap between both belts, $v_x(x, y)$, as well as the volume flux per unit spanwise length, $q$. The results must be expressed as a function of known data, and of the reduced pressure gradient, $P_l$.

4. (2 points). Determine $P_l$, as well as the pressure distribution inside the channel, $P(x)$.

5. (2 points). Find the external forces per unit spanwise length in the $x$-direction, $F^{EXT}_{l,x}$ and $F^{EXT}_{u,x}$, that must be exerted on the lower and upper belts to keep the motion, as well as the power per unit spanwise length that needs to be supplied to drive the system, $\dot{W}$.

6. (2 points). Knowing that the net mechanical energy gained by the liquid per unit time and per unit spanwise length during the pumping process is $\dot{W}_{useful} = q\Delta P$, determine the efficiency of the pumping system, $\eta = \dot{W}_{useful}/\dot{W}$, as a function of the governing parameters. Study the particular cases a) $V_l = V_u$, and b) $V_l = 0$, demonstrating that in both cases the result can be expressed as a function of the single parameter $\Lambda$ defined above. In case b), find the maximum efficiency, $\eta_{max}$ as well as the corresponding value of $\Lambda_{max}$.

7. (1 additional point). Discuss the solution of Problem 3 in the light of the results obtained in Problem 4.

The sheet prints "cartersian". In the key the efficiency is item (5), the statement's item 6; the key has no text for item 7.

![[attachments/FM-T7/vf15-statement.svg]]
*Statement figure (redrawn from VF15.pdf): two parallel belts of length L, a distance h apart, whose facing strands move at V_u and V_l and drag liquid of density ρ and viscosity μ from a reservoir at P_0 to one at P_0 + ΔP*

Source: VF15.pdf (page 1: statement; pages 2 and 3: handwritten key; exam of Dec 18, 2012). Notes.pdf, Chapter 7: Couette and Poiseuille flows, Eqs. 7.8-7.12; slender flows, Eqs. 7.40-7.46.

## Hypotheses, Data and Unknowns

- The belts are the walls $y = 0$ (lower, velocity $V_l$) and $y = h$ (upper, velocity $V_u$), both moving along $+x$ towards the high-pressure reservoir, $x = 0$ at $P_0$ and $x = L$ at $P_0 + \Delta P$; the pressure is reduced pressure and the flow is steady, slender and two-dimensional.
- Everything is per unit spanwise length.

## Characteristic Velocity and Criterion for Pumping

The balance of the pressure and viscous forces in the gap, $\Delta P/L\sim\mu V_{\Delta P}/h^2$, gives the velocity induced by the overpressure (which pushes the liquid **backward**, from high to low pressure):

$$ V_{\Delta P}\sim\frac{h^2\Delta P}{\mu L}, \qquad \Lambda = \frac{V_{\Delta P}}{V_l + V_u} = \frac{h^2\Delta P}{\mu L\left(V_l + V_u\right)} $$

The belts drag the liquid forward with a velocity of order $V_l + V_u$: the pump only works if this velocity beats the backflow, $V_{\Delta P}$ sufficiently smaller than $V_l + V_u$, that is, $\Lambda$ small enough (Part 6 shows that the flux vanishes for a finite value of $\Lambda$).

## Criterion for Viscous Dominance

The slender-flow condition (Eq. 7.41) is $(\rho V h/\mu)(h/L)\ll 1$ with the largest velocity of the problem. Depending on which one dominates:

$$ \Lambda\ll 1\ (V\sim V_l + V_u):\quad\frac{\rho\left(V_l + V_u\right)h^2}{\mu L}\ll 1; \qquad\Lambda\gg 1\ (V\sim V_{\Delta P}):\quad\frac{\rho\,\Delta P\,h^4}{\mu^2L^2}\ll 1 $$

The pump only works for $\Lambda$ small, so the first condition is the one that matters. The flow is steady, so the unsteady condition holds.

## Velocity Profile and Flux

With $P_l = -\partial P/\partial x$ and Eq. (7.12) extended to two moving walls:

$$ 0 = P_l + \mu\frac{\partial^2v_x}{\partial y^2}; \qquad y = 0:\; v_x = V_l, \qquad y = h:\; v_x = V_u $$

$v_x = -\frac{P_ly^2}{2\mu} + Ay + B$ with $B = V_l$ and $A = \frac{V_u - V_l}{h} + \frac{P_lh}{2\mu}$:

$$ v_x = V_l + \frac{V_u - V_l}{h}\,y + \frac{P_l}{2\mu}\,y\,(h - y), \qquad q = \int_0^hv_x\,dy = \frac{(V_l + V_u)h}{2} + \frac{P_lh^3}{12\mu} $$

## Pressure Gradient and Pressure

Integrating the continuity equation across the gap: $\partial q/\partial x = v_y(0) - v_y(h) = 0$ (the belts do not move normally to themselves), so $q$ is uniform and so is $P_l$:

$$ \frac{\partial^2P}{\partial x^2} = 0,\quad P(0) = P_0,\quad P(L) = P_0 + \Delta P \;\Longrightarrow\; P = P_0 + \Delta P\,\frac{x}{L}, \qquad P_l = -\frac{\Delta P}{L} $$

## Forces on the Belts and Power

The shear stress is $\tau'_{xy} = \mu\,\partial v_x/\partial y = \mu\frac{V_u - V_l}{h} - \frac{\Delta P}{2L}(h - 2y)$ (with $P_l = -\Delta P/L$). The force of the liquid on a belt is $\bar{\tau}'\cdot\bar{n}$ with $\bar{n}$ from the belt into the liquid ($+\bar{e}_y$ on the lower belt, $-\bar{e}_y$ on the upper belt); only the $x$ components are considered (the pressure is normal to the belts):

$$ F_{lx} = \int_0^L\tau'_{xy}\big|_{y=0}dx = \frac{\mu\left(V_u - V_l\right)L}{h} - \frac{\Delta P\,h}{2}, \qquad F_{ux} = -\int_0^L\tau'_{xy}\big|_{y=h}dx = -\frac{\mu\left(V_u - V_l\right)L}{h} - \frac{\Delta P\,h}{2} $$

The external forces that keep the belts at constant velocity are the opposite:

$$ F^{EXT}_{u,x} = \frac{\Delta P\,h}{2} + \frac{\mu\left(V_u - V_l\right)L}{h}, \qquad F^{EXT}_{l,x} = \frac{\Delta P\,h}{2} - \frac{\mu\left(V_u - V_l\right)L}{h} $$

and the power per unit spanwise length is the sum of force times velocity:

$$ \dot{W} = F^{EXT}_{l,x}V_l + F^{EXT}_{u,x}V_u = \frac{\left(V_l + V_u\right)h\,\Delta P}{2} + \frac{\left(V_u - V_l\right)^2\mu L}{h} $$

The first term is the work against the pressure difference (the force $\Delta P\,h/2$ on each belt), the second is the viscous dissipation of the Couette part.

## Efficiency

$$ \eta = \frac{q\,\Delta P}{\dot{W}} = \frac{\dfrac{(V_l + V_u)h\,\Delta P}{2} - \dfrac{h^3\Delta P^2}{12\mu L}}{\dfrac{(V_l + V_u)h\,\Delta P}{2} + \dfrac{(V_u - V_l)^2\mu L}{h}} $$

Dividing numerator and denominator by $(V_l + V_u)h\,\Delta P/2$, with $\frac{h^2\Delta P}{6\mu L(V_l + V_u)} = \frac{\Lambda}{6}$ and $\frac{2\mu L(V_u - V_l)^2}{h^2\Delta P(V_u + V_l)} = \frac{2}{\Lambda}\left(\frac{V_u - V_l}{V_u + V_l}\right)^2$:

$$ \eta = \frac{1 - \Lambda/6}{1 + \dfrac{2}{\Lambda}\left(\dfrac{V_u - V_l}{V_u + V_l}\right)^2} $$

The flux $q = \frac{(V_l + V_u)h}{2}\left(1 - \frac{\Lambda}{6}\right)$ vanishes at $\Lambda = 6$: the pump works for $\Lambda<6$.

**a) $V_l = V_u$.** The ratio of velocities is zero and $\eta = 1 - \Lambda/6$ (no shear dissipation: the walls move together).

**b) $V_l = 0$.** The ratio is 1, so $\eta = \dfrac{1 - \Lambda/6}{1 + 2/\Lambda} = \dfrac{\Lambda(6 - \Lambda)}{6(\Lambda + 2)}$, which is zero at $\Lambda = 0$ and at $\Lambda = 6$. The maximum: $\frac{d}{d\Lambda}\frac{6\Lambda - \Lambda^2}{6\Lambda + 12} = 0$ gives $(6 - 2\Lambda)(\Lambda + 2) - (6\Lambda - \Lambda^2) = 0$, that is $\Lambda^2 + 4\Lambda - 12 = 0$, $(\Lambda + 6)(\Lambda - 2) = 0$:

$$ \Lambda_{max} = 2, \qquad \eta_{max} = \frac{2\cdot 4}{6\cdot 4} = \frac{1}{3} $$

## Discussion of Problem 3 (Item 7)

The key has no text for this item; the following is computed here. Problem 3 of the exam ([[Problem - DA10 Two-Belt Viscous Pump]]) is this pump with $V_l = 0$, calibrated with glycerol ($h = 1$ cm, $L = 20$ cm, $\mu = 1.41$ kg/(m s), $\Delta P = 1$ kPa) at $V_u = 0.10$ to $0.35$ m/s, so $\Lambda = h^2\Delta P/(\mu LV_u) = 0.355/V_u$ (with $V_u$ in m/s) goes from $3.55$ to $1.01$. The formula of case b) gives $\eta = 0.26$, $0.33$, $0.33$, $0.32$, $0.30$, $0.28$ for $V_u = 10, 15, 20, 25, 30, 35$ cm/s, the values of the efficiency column of the calibration table; the flux $q = \frac{V_uh}{2}(1 - \Lambda/6)$ gives $2.04$ cm$^2$/s at $V_u = 10$ cm/s (the table has 2), and the power $\dot{W} = \frac{V_uh\Delta P}{2} + \frac{V_u^2\mu L}{h}$ gives $0.5 + 0.28 = 0.78$ W/m at the same speed (the table: 0.8). The calibration points are around the optimum $\Lambda = 2$ ($V_u = 17.7$ cm/s), where $\eta$ is highest; and since $\eta$ depends only on $\Lambda$, the oil, with $\Delta P_{oil}/\Delta P_g = 2$ and $\mu_{oil}/\mu_g = 3.55$, works at the same $\Lambda$ and the same efficiency for the speed $V_{u,oil} = 0.564\,V_{u,g}$, the similarity condition of Problem 3.

## Answers and Checks

- $V_{\Delta P}\sim h^2\Delta P/(\mu L)$; the pump works for $\Lambda\ll 1$ (in fact $\Lambda<6$). Viscous dominance: $\rho(V_l + V_u)h^2/(\mu L)\ll 1$.
- Velocity: $v_x = V_l + \frac{V_u - V_l}{h}y + \frac{P_l}{2\mu}y(h - y)$; flux: $q = \frac{(V_l + V_u)h}{2} + \frac{P_lh^3}{12\mu}$; $P_l = -\Delta P/L$, $P = P_0 + \Delta Px/L$.
- Forces: $F^{EXT}_{u,x} = \frac{\Delta Ph}{2} + \frac{\mu(V_u - V_l)L}{h}$, $F^{EXT}_{l,x} = \frac{\Delta Ph}{2} - \frac{\mu(V_u - V_l)L}{h}$; power: $\dot{W} = \frac{(V_l + V_u)h\Delta P}{2} + \frac{(V_u - V_l)^2\mu L}{h}$.
- Efficiency: $\eta = \frac{1 - \Lambda/6}{1 + (2/\Lambda)\left[(V_u - V_l)/(V_u + V_l)\right]^2}$; a) $\eta = 1 - \Lambda/6$; b) $\Lambda_{max} = 2$, $\eta_{max} = 1/3$.
- Dimensions: $\Delta P\,h$ is $ML^{-1}T^{-2}\cdot L = MT^{-2}$, a force per unit width; $\Lambda$ is $L^2\cdot ML^{-1}T^{-2}/(ML^{-1}T^{-1}\cdot L\cdot LT^{-1}) = 1$.
- Energy check: $\dot{W} - q\Delta P$ must be the viscous dissipation per unit span, $L\int_0^h\mu\left(\partial v_x/\partial y\right)^2dy$. With $\partial v_x/\partial y = \frac{V_u - V_l}{h} + \frac{P_l}{2\mu}(h - 2y)$ the cross term integrates to zero and the integral is $\mu\frac{(V_u - V_l)^2}{h}L + \frac{P_l^2h^3}{12\mu}L$; and $\dot{W} - q\Delta P = \frac{(V_u - V_l)^2\mu L}{h} + \frac{h^3\Delta P^2}{12\mu L}$, the same (with $P_l^2L = \Delta P^2/L$).
- Check against the official key: VF15.pdf gives the same criterion, profile, flux, pressure, forces, power, efficiency, both cases and $\Lambda_{max} = 2$, $\eta_{max} = 1/3$.
