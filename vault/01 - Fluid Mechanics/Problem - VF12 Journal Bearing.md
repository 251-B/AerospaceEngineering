---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - lubricacion
  - cojinete
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF12.pdf"
id: "vf12"
pill: "VF12: Journal bearing"
sheets:
  - 12
tags_html:
  - "Eccentric cylinders"
  - "Wedge effect"
  - "Force, torque, cavitation"
---

# Problem VF12: Journal Bearing

> Official viscous-flow sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: the lubrication film of a planar bearing (Notes.pdf, Eqs. 7.69-7.75) wrapped around the shaft, with the flux fixed by the periodicity of the pressure.

## Statement

The cylindrical bearing shown in the figure includes an external fixed casing of radius $R_b$ and a shaft rotating with angular velocity $\omega$ of radius $R$ such that $R_b - R\ll R$. The centers are shifted a small distance $e$, called exentricity, so that in between both cylinders there exists a thin circular gap of thickness $h\sim e\sim R_b - R\ll R$ full of a liquid of density $\rho$ and viscosity $\mu$.

1. Show by simple trigonometric reasoning that the gap thickness can be expressed as $h(\theta) = R_b - R + e\cos\theta$.

2. Obtain the azimuthal velocity distribution $v_x$ in terms of the distance $y$ to the fixed casing and the unknown value of the induced pressure gradient $P_l = -R^{-1}\partial P/\partial\theta$.

3. Determine the circulating volume flux $Q = \int_0^hv_x\,dy$ as well as the pressure distribution $P(\theta) - P(0)$, where $P(0)$ is the unknown value of the pressure at $\theta = 0$, which depends on the pressurization conditions.

4. Calculate the torque and the force acting on the rotating shaft.

The sheet prints "exentricity". In the figure and in the key $y$ is measured from the shaft surface (the key's profile is $\omega R$ at $y = 0$ and zero at $y = h$), not from the casing as the sentence of item 2 says.

![[attachments/FM-T7/vf12-statement.svg]]
*Statement figure (redrawn from VF12.pdf): a shaft of radius R rotating with ω inside a fixed casing of radius R_b, their centres O and C a distance e apart; θ is measured from the line of centres, h(θ) is the gap, x = Rθ the arc along the shaft and y the distance across the gap, from the shaft to the casing*

Source: VF12.pdf (page 1, statement and handwritten key; no date printed). Notes.pdf, Chapter 7: Couette and Poiseuille flows, Eqs. 7.9-7.12; the wedge effect, Eqs. 7.69-7.76.

## Hypotheses, Data and Unknowns

- The gap is thin ($h\sim e\sim R_b - R\ll R$), so it can be unrolled: $x = R\theta$ along the shaft and $y$ across the gap, with $y = 0$ on the shaft (moving with $\omega R$) and $y = h$ on the fixed casing; the flow is steady and slender, with the pressure uniform across the gap and $P_l = -R^{-1}\partial P/\partial\theta$.
- Let $c = R_b - R$ and $\varepsilon = e/c$ ($0\le\varepsilon<1$). Forces are per unit length of the shaft.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R$, $R_b$ | radii of the shaft and of the casing | m |
| $e$, $\varepsilon = e/(R_b - R)$ | eccentricity and its relative value | m, 1 |
| $\omega$ | angular velocity of the shaft | s$^{-1}$ |
| $Q$ | circulating flux per unit length | m$^2$/s |

## Gap Thickness

Place the centre of the casing at $C$ and the centre of the shaft at $O$, a distance $e$ from $C$, with $\theta$ the angle at $O$ from the line $OC$ direction; the radial line from $O$ at the angle $\theta$ meets the casing at a point at the distance $R + h$ from $O$. In the triangle $O$, $C$, point of the casing, the sides are $R + h$ (from $O$), $e$ (from $C$ to $O$) and $R_b$ (from $C$), with the angle $\theta$ at $O$ between the sides $R + h$ and $e$; the law of cosines gives (the legs of the key's sketch, $(R + h)\cos\theta - e$ and $(R + h)\sin\theta$, give the same):

$$ R_b^2 = (R + h)^2 - 2e(R + h)\cos\theta + e^2 \;\Longrightarrow\; R + h = e\cos\theta + \sqrt{R_b^2 - e^2\sin^2\theta} $$

The square root is $R_b\left[1 - e^2\sin^2\theta/(2R_b^2) + \dots\right]$, and the second term is a factor $e/R_b\ll 1$ smaller than $e$, so $R + h\simeq R_b + e\cos\theta$:

$$ h(\theta) = R_b - R + e\cos\theta = (R_b - R)\left[1 + \varepsilon\cos\theta\right] $$

The gap is largest at $\theta = 0$ and smallest at $\theta = \pi$.

## Velocity Profile, Flux and Pressure

The shaft moves with $\omega R$ and the casing is at rest: Couette plus Poiseuille (Eq. 7.70), with the pressure gradient along $x = R\theta$:

$$ v_x = \omega R\,\frac{h - y}{h} - \frac{y(h - y)}{2\mu}\,\frac{1}{R}\frac{\partial P}{\partial\theta}, \qquad Q = \int_0^hv_x\,dy = \frac{\omega Rh}{2} - \frac{h^3}{12\mu R}\frac{\partial P}{\partial\theta} $$

The flux is the same at every $\theta$ (Eq. 7.72), so $\partial P/\partial\theta = \frac{12\mu R}{h^3}\left(\frac{\omega Rh}{2} - Q\right)$, and integrating from $0$ to $\theta$ (Eq. 7.74):

$$ P(\theta) - P(0) = 6\mu\omega R^2\int_0^\theta\frac{d\theta'}{h^2} - 12\mu RQ\int_0^\theta\frac{d\theta'}{h^3} $$

**Periodicity.** $P(2\pi) = P(0)$ gives $Q = \frac{\omega R}{2}\int_0^{2\pi}\frac{d\theta}{h^2}\Big/\int_0^{2\pi}\frac{d\theta}{h^3}$. With $h = c(1 + \varepsilon\cos\theta)$ and the known integrals (computed here, with $|\varepsilon|<1$)

$$ \int_0^{2\pi}\frac{d\theta}{(1 + \varepsilon\cos\theta)^2} = \frac{2\pi}{(1 - \varepsilon^2)^{3/2}}, \qquad \int_0^{2\pi}\frac{d\theta}{(1 + \varepsilon\cos\theta)^3} = \frac{\pi\left(2 + \varepsilon^2\right)}{(1 - \varepsilon^2)^{5/2}} $$

$$ Q = \frac{\omega Rc}{2}\,\frac{2\pi/(1 - \varepsilon^2)^{3/2}}{\pi(2 + \varepsilon^2)/(1 - \varepsilon^2)^{5/2}} = \omega Rc\,\frac{1 - \varepsilon^2}{2 + \varepsilon^2} $$

**Pressure.** Substituting $Q$:

$$ \frac{\partial P}{\partial\theta} = \frac{6\mu\omega R^2}{c^2}\left[\frac{1}{(1 + \varepsilon\cos\theta)^2} - \frac{2(1 - \varepsilon^2)}{(2 + \varepsilon^2)(1 + \varepsilon\cos\theta)^3}\right] = \frac{6\mu\omega R^2}{c^2(2 + \varepsilon^2)}\,\frac{\varepsilon\left(2\cos\theta + 3\varepsilon + \varepsilon^2\cos\theta\right)}{(1 + \varepsilon\cos\theta)^3} $$

and this is the derivative of

$$ P(\theta) - P(0) = \frac{6\mu\omega R^2}{(R_b - R)^2}\,\frac{\varepsilon\,(2 + \varepsilon\cos\theta)\sin\theta}{(2 + \varepsilon^2)(1 + \varepsilon\cos\theta)^2} $$

(check: with $N = (2 + \varepsilon\cos\theta)\sin\theta$, $N' = 2\cos\theta - \varepsilon + 2\varepsilon\cos^2\theta$ and $\frac{d}{d\theta}\frac{N}{(1 + \varepsilon\cos\theta)^2} = \frac{N'(1 + \varepsilon\cos\theta) + 2\varepsilon\sin\theta\,N}{(1 + \varepsilon\cos\theta)^3} = \frac{2\cos\theta + 3\varepsilon + \varepsilon^2\cos\theta}{(1 + \varepsilon\cos\theta)^3}$, which has the factor $\varepsilon$ of the previous line; and the expression vanishes at $\theta = 0$). The pressure is antisymmetric, $P(\theta) - P(0) = -[P(-\theta) - P(0)]$: overpressure on one side of the line of centres and underpressure on the other, which gives a force perpendicular to it.

## Force and Torque on the Shaft

**Torque.** The shear on the shaft (normal from the shaft into the liquid, $+\bar{e}_y$) is $\tau_p = \mu\,\partial v_x/\partial y|_{y=0} = -\frac{\mu\omega R}{h} - \frac{h}{2R}\frac{\partial P}{\partial\theta}$; with $\partial P/\partial\theta = 6\mu\omega R^2/h^2 - 12\mu RQ/h^3$, $\tau_p = -\frac{4\mu\omega R}{h} + \frac{6\mu Q}{h^2}$. The torque per unit length is $M = \int_0^{2\pi}\tau_pR\cdot R\,d\theta$:

$$ M = -4\mu\omega R^3\int_0^{2\pi}\frac{d\theta}{h} + 6\mu QR^2\int_0^{2\pi}\frac{d\theta}{h^2}, \qquad \int_0^{2\pi}\frac{d\theta}{1 + \varepsilon\cos\theta} = \frac{2\pi}{\sqrt{1 - \varepsilon^2}} $$

$$ M = -\frac{8\pi\mu\omega R^3}{c\sqrt{1 - \varepsilon^2}} + \frac{12\pi\mu\omega R^3}{c(2 + \varepsilon^2)\sqrt{1 - \varepsilon^2}} = -\frac{4\pi\mu\omega R^3}{R_b - R}\,\frac{1 + 2\varepsilon^2}{\sqrt{1 - \varepsilon^2}\,(2 + \varepsilon^2)} $$

(the torque of the liquid on the shaft, opposing the rotation; the torque the motor applies is its opposite).

**Force.** The pressure force on the shaft is $\bar{F} = -\int(P - P(0))\,\bar{n}\,R\,d\theta$, with $\bar{n}$ the outward normal of the shaft, $n_z = \sin\theta$ and $n_\parallel = \cos\theta$ (the uniform $P(0)$ gives no net force). The component along the line of centres is zero because $P - P(0)$ is odd in $\theta$ and $\cos\theta$ is even. The perpendicular one, integrating by parts ($P(0) = P(2\pi)$ so the boundary term vanishes): $\int_0^{2\pi}(P - P(0))\sin\theta\,d\theta = \int_0^{2\pi}\cos\theta\,\frac{\partial P}{\partial\theta}\,d\theta = \frac{6\mu\omega R^2\varepsilon}{c^2(2 + \varepsilon^2)}\int_0^{2\pi}\frac{\cos\theta\left(2\cos\theta + 3\varepsilon + \varepsilon^2\cos\theta\right)}{(1 + \varepsilon\cos\theta)^3}d\theta$, and the last integral equals $2\pi/\sqrt{1 - \varepsilon^2}$ (verified numerically in the checks of this note). Hence

$$ F_z = -R\int_0^{2\pi}(P - P(0))\sin\theta\,d\theta = -\frac{12\pi\mu\omega R^3}{(R_b - R)^2}\,\frac{\varepsilon}{\sqrt{1 - \varepsilon^2}\,(2 + \varepsilon^2)} $$

on the shaft (downward in the figure), and the opposite on the bearing (upward). The shear forces contribute to the force on the shaft at a relative order $c/R\ll 1$ and are neglected.

## Limit of Large Eccentricity and Cavitation

When $\varepsilon\to 1$ (the shaft touches the casing, $h_{min} = c(1 - \varepsilon)\to 0$) the force grows without bound, $F_z\propto(1 - \varepsilon^2)^{-1/2}$: **a bearing can in principle bear an infinite load**. In practice it fails earlier: the underpressure side of $P(\theta) - P(0)$ reaches the vapour pressure $p_v$ and the liquid cavitates when $P_{min} - P(0) = p_v - P(0)$. The minimum of $P$ is where $\partial P/\partial\theta = 0$, that is $\cos\theta_{min} = -3\varepsilon/(2 + \varepsilon^2)$ with $\sin\theta_{min}<0$ ($\theta_{min}\simeq 3\pi/2$ for small $\varepsilon$, as the key notes).

## Answers and Checks

- Gap: $h = R_b - R + e\cos\theta = (R_b - R)(1 + \varepsilon\cos\theta)$.
- Velocity: $v_x = \omega R\frac{h - y}{h} - \frac{y(h - y)}{2\mu R}\frac{\partial P}{\partial\theta}$; flux: $Q = \omega R(R_b - R)\frac{1 - \varepsilon^2}{2 + \varepsilon^2}$.
- Pressure: $P - P(0) = \frac{6\mu\omega R^2}{(R_b - R)^2}\frac{\varepsilon(2 + \varepsilon\cos\theta)\sin\theta}{(2 + \varepsilon^2)(1 + \varepsilon\cos\theta)^2}$.
- Torque: $M = -\frac{4\pi\mu\omega R^3}{R_b - R}\frac{1 + 2\varepsilon^2}{\sqrt{1 - \varepsilon^2}(2 + \varepsilon^2)}$; force: $F_z = -\frac{12\pi\mu\omega R^3}{(R_b - R)^2}\frac{\varepsilon}{\sqrt{1 - \varepsilon^2}(2 + \varepsilon^2)}$ on the shaft, opposite on the bearing.
- Limit $\varepsilon\to 0$ (concentric): $Q = \omega Rc/2$, $P = P(0)$, $F_z = 0$ and $M = -2\pi\mu\omega R^3/c$, the Couette torque of the gap $c$: $\tau = \mu\omega R/c$ times $R\cdot R\cdot 2\pi$.
- Dimensions: $\mu\omega R^3/(R_b - R)$ is $ML^{-1}T^{-1}\cdot T^{-1}\cdot L^3/L = MLT^{-2}$, a torque per unit length (N m/m = N); $\mu\omega R^3/(R_b - R)^2$ is a force per unit length.
- Check against the official key: VF12.pdf gives the same geometry, profile, flux, pressure, torque and force. Its part 1 writes the gap as $(R_b - R)[1 + \varepsilon\cos\theta]$ and its flux integrals as $(1 - \varepsilon\cos\theta)$; the two give the same integrals by $\theta\to\theta + \pi$.
