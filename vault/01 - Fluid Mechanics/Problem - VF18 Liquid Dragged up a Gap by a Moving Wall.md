---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - flujo-casi-estacionario
  - columna-de-liquido
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF18.pdf"
id: "vf18"
pill: "VF18: Dragged column"
sheets:
  - 18
tags_html:
  - "Couette + Poiseuille"
  - "Rising column"
  - "Critical velocity"
---

# Problem VF18: Liquid Dragged up a Gap by a Moving Wall

> Official viscous-flow sheet of the course (prefinal exam of Dec 16, 2013), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: Couette plus Poiseuille flow in a thin gap (Notes.pdf, Eqs. 7.12 and 7.69-7.71) with the reduced pressure $P = p + \rho gz$ fixed at both ends of the column, and mass conservation for the rising column.

## Statement

A liquid of density $\rho$ and viscosity $\mu$ is contained in an open vessel limited laterally by a vertical wall. A thin flat plate is placed parallel to the wall with its lower end at a depth $H$, forming a gap of thickness $d$, as shown in the figure. At the initial instant of time, the vertical wall begins to move upwards with a constant velocity $V$, dragging the liquid into the gap, where a liquid column of height $h(t)$ rises. To solve the problem, assume that the flow in the gap is dominated by viscosity. Address the following questions in order:

1. Obtain the velocity profile across the gap $v_z(y)$.

2. Calculate the volume flow rate that enters the gap $Q(t) = \int_0^dv_z\,dy$ as well as the distribution of reduced pressure $P = p + \rho gz$ along the liquid column and its associated gradient $P_l = -\partial P/\partial z$. In particular, write expressions for the instantaneous values of $Q(t)$ and $P_l(t)$ in terms of $h(t)$.

3. Write the differential equation with initial condition that determines the variation with time of $h(t)$ and compute $h(t)$ by integration.

4. Investigate the solution that appears for large times. In particular, show that for values of the wall velocity $V$ below a critical value $V_c$ the liquid column settles at a constant height $h_\infty$, whereas for $V>V_c$ the column keeps rising, with a rate $dh/dt$ that approaches a constant value $dh/dt = \dot{h}_\infty$ for large times. Give the values of $V_c$, $h_\infty$, and $\dot{h}_\infty$.

5. For $V<V_c$, compute the power needed to keep the wall in motion when the steady solution is reached.

![[attachments/FM-T7/vf18-statement.svg]]
*Statement figure (redrawn from VF18.pdf, panel t > 0): a vertical wall that moves up with velocity V and a fixed plate at the distance d, with its lower end at the depth H below the free surface; the gap is filled with liquid up to the height h(t) above the free surface; p_a acts on the free surface and on the top of the column*

Source: VF18.pdf (page 1, prefinal exam of Dec 16, 2013; statement and handwritten key). Notes.pdf, Chapter 7: Couette and Poiseuille flows, Eqs. 7.9-7.12; wedge effect, Eqs. 7.69-7.75.

## Hypotheses, Data and Unknowns

- The wall ($y = 0$) moves up with $V$; the plate ($y = d$) is at rest. $z$ is measured upwards from the free surface of the vessel; the gap extends from the lower end of the plate, $z = -H$, up to the top of the column, $z = h(t)$, with $h(0) = 0$.
- The free surface of the vessel and the top of the column are at $p_a$. The hydrostatic pressure at the lower end of the plate: $p = p_a + \rho gH$.
- The flow is slender and quasi-steady (viscosity dominates), so the profile is Couette plus Poiseuille at each instant, with the reduced pressure uniform across the gap and a uniform gradient $P_l(t)$ along it.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $V$ | velocity of the wall | m/s |
| $d$, $H$ | width of the gap, depth of the lower end of the plate | m |
| $h(t)$ | height of the column above the free surface | m |
| $Q(t)$ | volume flux entering the gap (per unit width) | m$^2$/s |

## Velocity Profile

Equation (7.69) with $P_l = -\partial P/\partial z$, the wall at $y = 0$ moving with $V$ and the plate at $y = d$ at rest (Eq. 7.12):

$$ v_z = V\left(1 - \frac{y}{d}\right) + \frac{P_l}{2\mu}\,d^2\,\frac{y}{d}\left(1 - \frac{y}{d}\right) $$

## Flux and Pressure

$$ Q = \int_0^dv_z\,dy = \frac{Vd}{2} + \frac{P_ld^3}{12\mu}, \qquad \frac{\partial P}{\partial z} = \frac{12\mu}{d^3}\left(\frac{Vd}{2} - Q\right) $$

The reduced pressure at the lower end of the plate ($z = -H$, $p = p_a + \rho gH$) is $p_a + \rho gH - \rho gH = p_a$, and at the top of the column ($z = h$, $p = p_a$) it is $p_a + \rho gh$. Since $\partial P/\partial z$ is uniform in the gap, integrating:

$$ P - p_a = \frac{12\mu}{d^3}\left(\frac{Vd}{2} - Q\right)(z + H), \qquad P_l = -\frac{p_a + \rho gh - p_a}{h + H} = -\frac{\rho gh}{h + H} $$

Equating the two expressions of $P_l$ ($P_l$ from the integral and from the flux):

$$ Q = \frac{Vd}{2} - \frac{\rho gh}{h + H}\,\frac{d^3}{12\mu} $$

(the key writes the three results without the intermediate step: with $z = h$, $P - p_a = \rho gh$ gives $\frac{12\mu}{d^3}\left(\frac{Vd}{2} - Q\right) = \frac{\rho gh}{h + H}$, and $P_l = -\partial P/\partial z$).

## Evolution of the Column

The column is a liquid of cross-section $d$ (per unit width), so its top rises with the mean velocity $Q/d$: $d\,\dot{h} = Q$, that is

$$ \frac{dh}{dt} = \frac{V}{2} - \frac{\rho gd^2}{12\mu}\,\frac{h}{h + H} = \frac{1}{2}\left[V - V_c\,\frac{h}{h + H}\right], \qquad V_c = \frac{\rho gd^2}{6\mu}, \quad h(0) = 0 $$

Writing $A = V - V_c$, $\frac{dh}{dt} = \frac{1}{2}\,\frac{Ah + VH}{h + H}$ and $dt = \frac{2(h + H)}{Ah + VH}\,dh$. Since $h + H = \frac{1}{A}(Ah + VH) - \frac{HV_c}{A}$ (as $H - \frac{VH}{A} = -\frac{HV_c}{A}$), the integral from $0$ to $h$ (Barrow's rule) is

$$ \frac{t}{2} = \frac{h}{A} - \frac{HV_c}{A^2}\ln\frac{Ah + VH}{VH} \;\Longrightarrow\; h - \frac{V_cH}{V - V_c}\ln\frac{(V - V_c)h + VH}{VH} = (V - V_c)\frac{t}{2} $$

(for $V\neq V_c$; for $V = V_c$ the equation is $dh/dt = \frac{V}{2}\frac{H}{h + H}$ and $h + \frac{h^2}{2H} = \frac{Vt}{2}$).

## Large Times

- **$V>V_c$.** $A>0$ and the logarithm grows slower than $h$: $h\to\infty$ as $t\to\infty$ and $dh/dt\to\frac{1}{2}\left(V - V_c\right)$, since $h/(h + H)\to 1$:
$$ \dot{h}_\infty = \frac{V - V_c}{2} $$
- **$V<V_c$.** $A<0$: $dh/dt$ goes to zero when $Ah + VH = 0$, so $Q\to 0$ and the column settles at
$$ h_\infty = \frac{HV}{V_c - V} $$
(the argument of the logarithm tends to zero, the column approaches $h_\infty$ asymptotically).
- **Critical velocity:** $V_c = \dfrac{\rho gd^2}{6\mu}$: the wall velocity for which the Couette flux $Vd/2$ equals the maximum backflow that the weight of an infinitely long column can drive, $\rho gd^3/(12\mu)$.

## Power in the Steady State, $V<V_c$

At the end $Q = 0$, so $P_l = -6\mu V/d^2$ (from $Q = 0$: $\frac{Vd}{2} + \frac{P_ld^3}{12\mu} = 0$), and the profile is $v_z = V\left(1 - \frac{y}{d}\right) - \frac{3V}{d^2}\,y\,(d - y)$. The shear on the moving wall ($\bar{n} = +\bar{e}_y$ from the wall into the liquid):

$$ \tau_w = \mu\frac{\partial v_z}{\partial y}\Big|_{y=0} = -\frac{\mu V}{d} + \frac{P_ld}{2} = -\frac{\mu V}{d} - \frac{3\mu V}{d} = -\frac{4\mu V}{d} $$

(the key writes the same, $\left(-\frac{V}{d} - \frac{\rho gh}{h + H}\frac{d}{2\mu}\right)\mu = -\frac{4\mu V}{d}$ at $h = h_\infty$, where $\frac{\rho gh_\infty}{h_\infty + H} = \frac{6\mu V}{d^2}$). This is in $-z$, resisting the motion. The wall is in contact with the liquid of the gap over the whole filled length from $z = -H$ to $z = h_\infty$, that is $h_\infty + H = \frac{HV_c}{V_c - V}$. The power that must be applied is the force times the velocity:

$$ \dot{W} = \frac{4\mu V}{d}\,\left(h_\infty + H\right)V = \frac{4\mu V^2H}{d}\,\frac{V_c}{V_c - V} $$

(per unit width). **Energy check:** with $Q = 0$ the liquid does not gain potential energy nor receive any net pressure work, so the whole power is dissipated: $\mu\int_0^d(\partial v_z/\partial y)^2dy = \frac{\mu V^2}{d}\int_0^1(4 - 6s)^2ds = \frac{4\mu V^2}{d}$ per unit length, times the length $h_\infty + H$, the same.

> [!warning] Discrepancy with the official solution
> The key boxes $\dot{W} = \frac{4\mu V^3}{d}\frac{H}{V_c - V}$, which is $\frac{4\mu V}{d}\,V\,h_\infty$: the wetted length it uses is $h_\infty$, the height of the column above the free surface. The gap, and so the wall in contact with the liquid of the film, extends from the lower end of the plate, $z = -H$, to the top of the column, $z = h_\infty$, a length $h_\infty + H$, and the profile (with the same shear) is the same in the part below the free surface. The correct length is $h_\infty + H = HV_c/(V_c - V)$, and $\dot{W} = 4\mu V^2H\,V_c/\left[d\,(V_c - V)\right]$, larger than the key's by the factor $V_c/V$. The dissipation check above confirms it. (If the part of the wall below the free surface is not counted, because the liquid there is in the open vessel, the key's value would follow; the statement does not say so, and the gap is filled from the lower end of the plate.)

## Answers and Checks

- Velocity: $v_z = V\left(1 - \frac{y}{d}\right) + \frac{P_l}{2\mu}d^2\frac{y}{d}\left(1 - \frac{y}{d}\right)$; $Q = \frac{Vd}{2} - \frac{\rho gh}{h + H}\frac{d^3}{12\mu}$; $P_l = -\frac{\rho gh}{h + H}$.
- Equation: $\frac{dh}{dt} = \frac{V}{2} - \frac{\rho gd^2}{12\mu}\frac{h}{h + H}$, $h(0) = 0$; solution $h - \frac{V_cH}{V - V_c}\ln\frac{(V - V_c)h + VH}{VH} = (V - V_c)\frac{t}{2}$.
- $V_c = \rho gd^2/(6\mu)$; for $V>V_c$, $\dot{h}_\infty = (V - V_c)/2$; for $V<V_c$, $h_\infty = HV/(V_c - V)$.
- Power: $\dot{W} = \frac{4\mu V^2}{d}\left(h_\infty + H\right) = \frac{4\mu V^2HV_c}{d(V_c - V)}$.
- Dimensions: $\rho gd^2/\mu$ is $ML^{-3}\cdot LT^{-2}\cdot L^2/(ML^{-1}T^{-1}) = LT^{-1}$, a velocity; $\mu V^2H/d$ is $ML^{-1}T^{-1}\cdot L^2T^{-2} = MLT^{-3}$ per unit width, a power per unit width.
- Limits: for $H\to 0$, $h_\infty\to 0$ and $\dot{W}\to 0$; for $V\to V_c^-$, $h_\infty\to\infty$ and $\dot{W}\to\infty$.
- Check against the official key: VF18.pdf gives the same profile, $Q$, $P_l$, differential equation, implicit solution, $V_c$, $\dot{h}_\infty$, $h_\infty$ and the wall shear; its power differs by the length used, as noted.
