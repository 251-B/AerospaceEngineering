---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - flujo-lento
  - tuberia
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF4.pdf"
id: "vf4"
pill: "VF4: Pipe and bar"
sheets:
  - 4
tags_html:
  - "Slender flow criterion"
  - "Pipe and annulus in series"
  - "Matching the pressure"
---

# Problem VF4: Pipe with a Partly Inserted Bar

> Official viscous-flow sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: the criterion of a slender flow dominated by viscosity (Notes.pdf, Eqs. 7.40-7.41), Poiseuille flow in the pipe (Eqs. 7.13-7.15) and in the annulus (as in VF3), with the pressure at the junction fixed by equal flux (Eq. 7.49, $Q$ uniform).

## Statement

The liquid located in a container at pressure $p_c$ discharges to the atmosphere, where the pressure is $p_a < p_c$, through a cylindrical pipe of diameter $D$ and length $L\gg D$. To control the volume flux $Q$ that circulates, a cylindrical bar of diameter $\alpha D$ is inserted coaxially from the exit, as shown in the figure, to partially block the liquid flow in the final stretch of the pipe.

1. Give the criterion for the motion in the tube to be dominated by viscosity.

2. Determine, in terms of the value of the pressure at the end of the tube $p_o$, the velocity field found for $0 < x/L < (1 - \beta)$ and for $(1 - \beta) < x/L < L$, where $\beta L$ is the insertion length.

3. Obtain the volume flux $Q$ and the value of $p_o$ as a function of $\beta$.

On the sheet, "contained in a deposit" is struck out by hand and replaced by "located in a container", and the printed second range is written $(1 - \beta) < x/L < L$, a typing slip for $(1 - \beta) < x/L < 1$.

![[attachments/FM-T7/vf4-statement.svg]]
*Statement figure (redrawn from VF4.pdf): a container at p_c discharging through a pipe of diameter D and length L; a coaxial bar of diameter αD enters from the exit along the last stretch βL; p_o is the pressure where the bar starts and p_a the exit pressure*

Source: VF4.pdf (page 1, statement and handwritten key). Notes.pdf, Chapter 7: slender flows dominated by viscosity, Eqs. 7.40-7.46; pipe of variable section, Eqs. 7.47-7.51; entrance region, Eqs. 7.55-7.63.

## Hypotheses, Data and Unknowns

- The liquid has constant $\rho$ and $\mu$; the flow is steady and axisymmetric.
- If the criterion of Part 1 holds, the flow is fully developed (Poiseuille) everywhere except in short regions of length of order $D$ at the entrance and at the junction $x = (1 - \beta)L$, and the pressure variations in them are small compared with the loss along the pipe (Notes.pdf, Eqs. 7.56 and 7.63). So $P(0) = p_c$ and the pressure at the end of the first stretch equals the one at the beginning of the second, $p_o$.
- Gravity is absorbed in the reduced pressure $P$; the gravity of a horizontal pipe does not matter, and the symbols $p_c$, $p_o$, $p_a$ are used for the reduced pressures (as in the key).
- Let $a = D/2$, $\Delta p = p_c - p_a$ and $\mathcal{G} = \pi D^4/(128\mu)$, so that $\mathcal{G} = \pi a^4/(8\mu)$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $D$, $\alpha D$ | diameters of the pipe and of the bar | m |
| $L$, $\beta L$ | length of the pipe and of the inserted bar | m |
| $p_c$, $p_o$, $p_a$ | pressure in the container, at the bar tip, at the exit | Pa |
| $Q$ | volume flux | m$^3$/s |

## Criterion for Viscous Dominance

The flow is dominated by viscosity when the convective acceleration is much smaller than the viscous force, Eq. (7.41), and the flow is steady here, so (7.40) is satisfied:

$$ \frac{\rho v_L D}{\mu}\,\frac{D}{L}\ll 1 $$

The velocity $v_L$ is not known, so assume that viscosity dominates and estimate it from the balance of pressure and viscous forces, Eq. (7.44), $\Delta_LP\sim\mu v_LL/D^2$ with $\Delta_LP\sim p_c - p_a$:

$$ v_L\sim\frac{D^2}{L}\,\frac{p_c - p_a}{\mu} $$

Substituting in the criterion:

$$ \frac{\rho D}{\mu}\,\frac{D}{L}\,\frac{D^2}{L}\,\frac{p_c - p_a}{\mu} = \frac{\rho D^4\left(p_c - p_a\right)}{\mu^2L^2}\ll 1 $$

which only contains known data.

## Velocity Fields

**First stretch, $0 < x < (1 - \beta)L$: circular pipe.** As in (7.13)-(7.14), with a constant reduced pressure gradient $dP/dx = -P_{l1}$ and radius $a = D/2$:

$$ v_x = \frac{P_{l1}}{4\mu}\left(a^2 - r^2\right) = \frac{P_{l1}}{16\mu}\left(D^2 - 4r^2\right) $$

The gradient is constant because the section is constant and $Q$ is uniform, so $P_{l1} = (p_c - p_o)/\left[(1 - \beta)L\right]$. In terms of the key's notation, $dP/dx = -(p_c - p_o)/\left[(1 - \beta)L\right]$.

**Second stretch, $(1 - \beta)L < x < L$: annulus.** The liquid is between the bar ($r = \alpha a$) and the pipe wall ($r = a$), both at rest, with $P_{l2} = (p_o - p_a)/(\beta L)$. Integrating (7.47) twice as in VF3, with $v_x(\alpha a) = v_x(a) = 0$:

$$ v_x = \frac{P_{l2}}{4\mu}\left(a^2 - r^2\right) + C\ln\frac{r}{a}; \qquad 0 = \frac{P_{l2}}{4\mu}a^2\left(1 - \alpha^2\right) + C\ln\alpha \;\Longrightarrow\; C = -\frac{P_{l2}a^2\left(1 - \alpha^2\right)}{4\mu\ln\alpha} $$

$$ v_x = \frac{P_{l2}D^2}{16\mu}\left[1 - \left(\frac{2r}{D}\right)^2 - \frac{1 - \alpha^2}{\ln\alpha}\ln\frac{2r}{D}\right], \qquad P_{l2} = \frac{p_o - p_a}{\beta L} $$

Check: at $r = D/2$ the bracket is $1 - 1 - 0 = 0$; at $r = \alpha D/2$ it is $1 - \alpha^2 - \frac{1 - \alpha^2}{\ln\alpha}\ln\alpha = 0$.

## Volume Flux

**Pipe.** From (7.15), $Q = \frac{\pi a^4}{8\mu}P_{l1}$, so

$$ Q = \mathcal{G}\,\frac{p_c - p_o}{(1 - \beta)L} \tag{1} $$

**Annulus.** With $s = r/a$, $Q = \int_{\alpha a}^{a}2\pi r\,v_x\,dr = 2\pi a^2\,\frac{P_{l2}a^2}{4\mu}\,I$ with $I = \int_\alpha^1 s\left[1 - s^2 - k\ln s\right]ds$ and $k = (1 - \alpha^2)/\ln\alpha$. Barrow's rule for each term:

$$ \int_\alpha^1 s\,ds = \frac{1 - \alpha^2}{2}, \qquad \int_\alpha^1 s^3ds = \frac{1 - \alpha^4}{4}, \qquad \int_\alpha^1 s\ln s\,ds = \left[\frac{s^2}{2}\ln s - \frac{s^2}{4}\right]_\alpha^1 = -\frac{1 - \alpha^2}{4} - \frac{\alpha^2}{2}\ln\alpha $$

$$ I = \frac{1 - \alpha^2}{2} - \frac{1 - \alpha^4}{4} + k\left[\frac{1 - \alpha^2}{4} + \frac{\alpha^2}{2}\ln\alpha\right] = \frac{1 - \alpha^2}{2} - \frac{1 - \alpha^4}{4} + \frac{\left(1 - \alpha^2\right)^2}{4\ln\alpha} + \frac{\alpha^2\left(1 - \alpha^2\right)}{2} $$

and since $\frac{1 - \alpha^2}{2} + \frac{\alpha^2(1 - \alpha^2)}{2} = \frac{1 - \alpha^4}{2}$, $I = \frac{1}{4}\left[\left(1 - \alpha^4\right) - \frac{(1 - \alpha^2)^2}{\ln(\alpha^{-1})}\right]$. Therefore

$$ Q = \frac{\pi a^4P_{l2}}{8\mu}\,f(\alpha) = \mathcal{G}\,\frac{p_o - p_a}{\beta L}\,f(\alpha), \qquad f(\alpha) = 1 - \alpha^4 - \frac{\left(1 - \alpha^2\right)^2}{\ln\left(\alpha^{-1}\right)} \tag{2} $$

($f$ is the ratio of the flux of the annulus to that of the empty pipe for the same $P_l$: $f\to 1$ for $\alpha\to 0$ and $f\to 0$ for $\alpha\to 1$.) The key writes the same function as $f(\alpha) = 1 - \alpha^2(2 - \alpha^2) - \frac{(1 - \alpha^2)\left[1 - \alpha^2 - 2\alpha^2\ln(\alpha^{-1})\right]}{\ln(\alpha^{-1})}$; expanding, $1 - 2\alpha^2 + \alpha^4 + 2\alpha^2(1 - \alpha^2) - (1 - \alpha^2)^2/\ln(\alpha^{-1}) = 1 - \alpha^4 - (1 - \alpha^2)^2/\ln(\alpha^{-1})$, the same.

## Flux and Pressure at the Junction

The flux is the same in both stretches (Notes.pdf, Eq. 7.72 and the discussion of (7.49)). Equating (1) and (2):

$$ \frac{p_c - p_o}{1 - \beta} = f\,\frac{p_o - p_a}{\beta} $$

With $u = p_o - p_a$ and $p_c - p_o = \Delta p - u$: $\beta(\Delta p - u) = f(1 - \beta)u$, so $u = \dfrac{\beta\,\Delta p}{\beta + f(1 - \beta)}$. Then

$$ Q = \mathcal{G}\,\frac{f\,u}{\beta L} = \frac{\pi D^4}{128\mu L}\,\frac{p_c - p_a}{1 + \beta\left(1 - f\right)/f}, \qquad p_o = p_c - \frac{(1 - \beta)\left(p_c - p_a\right)}{1 + \beta\left(1 - f\right)/f} $$

(the second from $p_c - p_o = \Delta p - u = \dfrac{f(1 - \beta)\Delta p}{\beta + f(1 - \beta)}$, dividing numerator and denominator by $f$).

> [!warning] Discrepancy with the official solution
> The two boxed results of the key have $1 + \dfrac{\beta f}{1 - f}$ in the denominator, with $f = f(\alpha)$ of its own equation (2). That combination is not the one that follows from (1) and (2). Two limits prove it. For $\alpha\to 0$ (no bar) $f\to 1$, and the key's denominator $1 + \beta f/(1 - f)$ tends to infinity, so $Q\to 0$, when the flow must be that of the empty pipe; the corrected denominator $1 + \beta(1 - f)/f$ tends to 1 and gives $Q = \pi D^4\Delta p/(128\mu L)$. For $\alpha\to 1$ (the bar fills the pipe) $f\to 0$ and the key gives the empty-pipe flux, the corrected formula $Q\to 0$. The calculation above is kept.
>
> A second slip: the key writes $dP/dx = (p_c - p_o)/\left[(1 - \beta)L\right]$ for the first stretch, a positive gradient, while the pressure falls along $x$; the boxed flux (1) uses the correct magnitude.

## Answers and Checks

- Viscous dominance: $\rho D^4(p_c - p_a)/(\mu^2L^2)\ll 1$.
- Velocities: $v_x = \frac{(p_c - p_o)}{16\mu(1 - \beta)L}\left(D^2 - 4r^2\right)$ for $0 < x < (1 - \beta)L$ and $v_x = \frac{(p_o - p_a)D^2}{16\mu\beta L}\left[1 - (2r/D)^2 - \frac{1 - \alpha^2}{\ln\alpha}\ln(2r/D)\right]$ for $(1 - \beta)L < x < L$.
- Flux: $Q = \frac{\pi D^4}{128\mu L}\frac{p_c - p_a}{1 + \beta(1 - f)/f}$; pressure at the junction: $p_o = p_c - \frac{(1 - \beta)(p_c - p_a)}{1 + \beta(1 - f)/f}$.
- Limits: $\beta\to 0$ (no bar) gives $Q = \pi D^4\Delta p/(128\mu L)$ and $p_o\to p_c - \Delta p = p_a$; $\beta\to 1$ (bar over the whole pipe) gives $Q = \mathcal{G}f\,\Delta p/L$ and $p_o\to p_c$, all the loss in the annulus; $f\to 1$ gives the empty pipe whatever $\beta$.
- Dimensions: $\pi D^4\Delta p/(\mu L)$ is $L^4\cdot ML^{-1}T^{-2}/(ML^{-1}T^{-1}\cdot L) = L^3T^{-1}$, a volume flux; $\rho D^4\Delta p/(\mu^2L^2)$ is $ML^{-3}L^4\,ML^{-1}T^{-2}/(M^2L^{-2}T^{-2}L^2) = 1$.
- Check against the official key: VF4.pdf gives the same criterion, the same fields, the same flux in each stretch (1) and (2) and the same $f(\alpha)$; its last two boxed results differ from the corrected ones, as explained in the discrepancy above.
