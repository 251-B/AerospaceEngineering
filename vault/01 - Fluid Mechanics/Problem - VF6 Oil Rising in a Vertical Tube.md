---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - flujo-casi-estacionario
  - ascenso-capilar
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF6.pdf"
id: "vf6"
pill: "VF6: Oil rising in a tube"
sheets:
  - 6
tags_html:
  - "Quasi-steady Poiseuille flow"
  - "Rising column"
  - "Force on the pipe"
---

# Problem VF6: Oil Rising in a Vertical Tube

> Official viscous-flow sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: quasi-steady Poiseuille flow in the column (Notes.pdf, Eqs. 7.13-7.15 and 7.48-7.51), hydrostatic equilibrium for the final height, and the force on the pipe from the wall shear and the pressure on the closed end.

## Statement

The bottom end of an empty vertical tube of radius $a$, closed at the top, is put in contact with a pool of oil. Because of the ambient overpressure, the liquid begins to flow into the tube, forming a column of increasing height $h(t)$ whose evolution in time is to be investigated assuming that the motion is dominated by viscosity. In particular:

- Obtain the value of the height $h_\infty$ corresponding to the equilibrium position, reached asymptotically for large times.
- Give the condition that determines whether the motion is dominated by viscosity.
- Obtain the evolution of $h(t)$ as well as the pressure distribution along the pipe $p(x,t)$ for $0 < x < h$.
- Compute the force acting on the pipe as a function of time $\bar{F} = F_z(t)\bar{e}_z$.

![[attachments/FM-T7/vf6-statement.svg]]
*Statement figure (redrawn from VF6.pdf): a vertical tube of radius a, closed at the top, with its lower end in a pool at p_a; the oil column of height h(t) has p = 0 above it; z is the vertical axis from the pool*

Source: VF6.pdf (page 1, statement and handwritten key; no date printed). Notes.pdf, Chapter 7: steady flow in a circular pipe, Eqs. 7.13-7.16; slender flows, Eqs. 7.40-7.41; pipe flow, Eqs. 7.47-7.51. The sheet answers the four bullets in the margin order 1) to 4).

## Hypotheses, Data and Unknowns

- The tube is evacuated above the liquid (the figure marks $p = 0$ there), so the free surface of the column is at pressure zero; the pool is at the atmospheric pressure $p_a$ at the level of the lower end, which is the origin of the vertical axis $z$ (the sheet writes $x\equiv z$ for the axial coordinate).
- The liquid is incompressible with constant $\rho$ and $\mu$; the column is slender, $h\gg a$ for most of the process.
- Reduced pressure: $P = p + \rho g z$.
- The atmosphere also acts on the outer face of the closed top end of the tube (this is what the sheet's force balance includes).

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $a$ | radius of the tube | m |
| $\rho$, $\mu$ | density, viscosity of the oil | kg/m$^3$, kg/(m s) |
| $p_a$ | ambient pressure | Pa |
| $h(t)$, $h_\infty$ | height of the column and its final value | m |

## Equilibrium Height

When $t\to\infty$ the liquid is at rest and the reduced pressure is uniform, $P = p + \rho g z = \text{constant}$. At the bottom ($z = 0$) it equals $p_a$ and at the free surface ($z = h_\infty$, $p = 0$) it equals $\rho g h_\infty$:

$$ p_a = \rho g h_\infty \;\Longrightarrow\; h_\infty = \frac{p_a}{\rho g} $$

## Criterion for Viscous Dominance

The viscous force dominates the convective acceleration (and the local acceleration, since $t_0\sim L/V_L$) when, Eq. (7.41),

$$ \frac{\rho V_L a}{\mu}\,\frac{a}{L}\ll 1 $$

with the characteristic length $L\sim h_\infty$ and the velocity estimated by assuming that viscosity dominates, Eq. (7.44), $V_L\sim\frac{a^2}{L}\frac{p_a}{\mu}$ (the pressure difference that drives the flow is $p_a$):

$$ \frac{\rho a^4p_a}{\mu^2h_\infty^2} = \frac{\rho a^4p_a}{\mu^2}\,\frac{\rho^2g^2}{p_a^2} = \frac{\rho^3g^2a^4}{\mu^2p_a}\ll 1 $$

(the key writes the characteristic transverse length as $D$; here it is the radius $a$, which only changes a numerical factor).

## Evolution of the Column

Poiseuille flow in the column (Eqs. 7.13-7.15), with $P_l = -\partial P/\partial z$ uniform along the column at each instant:

$$ v_z = \frac{P_l}{4\mu}\left(a^2 - r^2\right), \qquad Q = \frac{\pi a^4}{8\mu}P_l $$

The reduced pressure falls from $P(0) = p_a$ to $P(h) = \rho g h$ over the length $h$, so $P_l = (p_a - \rho g h)/h$. The mean velocity of the column is the velocity of its free surface, $Q = \pi a^2\,dh/dt$ (the column grows, so the flux into the tube is positive upward; the key writes $-\pi a^2dh/dt$ and corrects the sign by hand). Hence

$$ \frac{dh}{dt} = \frac{a^2}{8\mu}\,\frac{p_a - \rho g h}{h} = \frac{a^2p_a}{8\mu}\,\frac{1 - h/h_\infty}{h} $$

Separating variables, with $h(0) = 0$ and $u = h/h_\infty$ ($h\,dh = h_\infty^2\,u\,du$):

$$ \int_0^h\frac{h'\,dh'}{1 - h'/h_\infty} = h_\infty^2\int_0^{h/h_\infty}\frac{u\,du}{1 - u} = \frac{a^2p_a}{8\mu}\,t, \qquad \int\frac{u\,du}{1 - u} = \int\left(-1 + \frac{1}{1 - u}\right)du = -u - \ln(1 - u) $$

$$ \frac{a^2p_a}{8\mu h_\infty^2}\,t = \ln\frac{1}{1 - h/h_\infty} - \frac{h}{h_\infty} $$

> [!warning] Discrepancy with the official solution
> The key writes this relation, and the equation of $dh/dt$ before it, without the factor $a^2$: $\frac{P_a}{8\mu h_\infty^2}t = \ln\frac{1}{1 - h/h_\infty} - \frac{h}{h_\infty}$. That cannot be right dimensionally: $p_at/\mu$ is dimensionless, so the left side has the dimensions $L^{-2}$ while the right side is dimensionless; and $dh/dt = (p_a/8\mu)(1 - h/h_\infty)/h$ has the dimensions $T^{-1}L^{-1}$ instead of $LT^{-1}$. The factor $a^2$ comes from $Q = \pi a^2dh/dt$ and $Q = \pi a^4P_l/(8\mu)$, whose ratio is $a^2$ (the key strikes out the $\pi a^2$ in that step). The same slip appears in the pressure-gradient lines of the key, written $8\mu Q/(\pi a^2)$, where the Poiseuille flux gives $8\mu Q/(\pi a^4)$. The results above keep the factor.

As $t\to\infty$, $\ln\frac{1}{1 - h/h_\infty}\to\infty$ and $h\to h_\infty$. For short times $\ln\frac{1}{1 - u} - u\simeq\frac{u^2}{2}$, so $h\simeq a\sqrt{p_at/(4\mu)}$: the column grows as $\sqrt{t}$ (the laminar, slender-flow law), independent of gravity.

## Pressure Distribution

The reduced pressure is linear, $P = p_a - P_lz$, with $P_l = (p_a - \rho gh)/h$. The actual pressure $p = P - \rho gz$:

$$ p(z, t) = p_a - \frac{p_a - \rho gh}{h}\,z - \rho gz = p_a - \frac{p_a}{h}\,z = p_a\left(1 - \frac{z}{h(t)}\right), \qquad 0 < z < h $$

linear from $p_a$ at the pool to zero at the top of the column; the weight terms cancel (the key writes the equivalent $P + \rho gz = p_a - \frac{8\mu Q}{\pi a^4}x$, boxed, with the same slip in the power of $a$).

## Force on the Pipe

The liquid acts on the pipe through the shear stress of the wall. With the normal from the wall into the liquid, $\bar{n} = -\bar{e}_r$, $\tau_p = -\mu\left(\partial v_z/\partial r\right)_{r=a} = P_la/2$ (Eq. 7.16), along $+\bar{e}_z$ (the rising liquid drags the wall upward). Over the lateral area $2\pi ah$:

$$ F_{visc} = 2\pi ah\cdot\frac{a}{2}\,\frac{p_a - \rho gh}{h} = \pi a^2\left(p_a - \rho gh\right) $$

The pressure inside the tube above the liquid is zero, and the atmosphere acts on the outer face of the closed top end with the force $-p_a\pi a^2\bar{e}_z$ (the closed end is a disc of area $\pi a^2$). The total force:

$$ \bar{F} = \pi a^2\left(p_a - \rho gh\right)\bar{e}_z - p_a\pi a^2\bar{e}_z = -\rho gh\,\pi a^2\,\bar{e}_z $$

i.e. $F_z(t) = -\rho g\pi a^2h(t)$: the weight of the column (downward), which is a good check: the force on the pipe equals the weight of the liquid it holds, since the liquid is quasi-static in the vertical momentum balance of the whole column ($\pi a^2p_a$ at the bottom, minus the weight, equals the shear transmitted to the wall).

## Answers and Checks

- Equilibrium height: $h_\infty = p_a/(\rho g)$.
- Viscous dominance: $\rho^3g^2a^4/(\mu^2p_a)\ll 1$.
- Height: $\frac{a^2p_a}{8\mu h_\infty^2}t = \ln\frac{1}{1 - h/h_\infty} - \frac{h}{h_\infty}$; pressure: $p = p_a(1 - z/h)$.
- Force on the pipe: $\bar{F} = -\rho g\pi a^2h(t)\,\bar{e}_z$.
- Dimensions: $a^2p_at/(\mu h_\infty^2)$ is $L^2\cdot ML^{-1}T^{-2}\cdot T/(ML^{-1}T^{-1}L^2) = 1$.
- Limits: at $t\to 0$, $h\to a\sqrt{p_at/(4\mu)}$; at $t\to\infty$, $h\to h_\infty$ and $F_z\to-\pi a^2p_a$ (the atmosphere on the top end, with the shear zero).
- Check against the official key: VF6.pdf gives $h_\infty = p_a/(\rho g)$, the criterion $\rho^3g^2D^4/(\mu^2p_a)\ll 1$, the integral for $h(t)$ and $\bar{F} = -\rho gh\pi a^2\bar{e}_z$; the key's $h(t)$ relation lacks the factor $a^2$, as noted above.
