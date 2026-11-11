---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - flujo-periodico
  - womersley
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF10.pdf"
id: "vf10"
pill: "VF10: Pulsatile pipe flow"
sheets:
  - 10
tags_html:
  - "Oscillatory pressure gradient"
  - "Womersley parameter"
  - "Quasi-steady and Stokes layer"
---

# Problem VF10: Pulsatile Flow in a Pipe

> Official viscous-flow sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 7 - Viscous Flows]].
> Method: unidirectional flow in a pipe (Notes.pdf, Eq. 7.7), complex function for a periodic forcing (Eqs. 7.28-7.30) and the limits of small and large $a^2\omega/\nu$ (Eqs. 7.33-7.35 and 7.31).

## Statement

Consider the unidirectional periodic motion induced in an infinitely long circular pipe of radius $a$ by an oscillatory pressure gradient $P_l = A\cos(\omega t)$. Write the conservation equation with boundary conditions that determine the axial velocity $v_x(r,t)$ and show how the problem can be solved exactly by separation of variables. Study separately the limits $a^2\omega/\nu\gg 1$ and $a^2\omega/\nu\ll 1$ and obtain the corresponding limiting solutions. In biofluid mechanics the square root $a(\omega/\nu)^{1/2}$ is called the Womersley parameter, which takes fairly large values for blood flow in large arteries, as you can see by using the values corresponding to the human aorta ($\mu/\rho\simeq 4\times 10^{-2}$ cm$^2$/s, $a\simeq 1.2$ cm, and $\omega = 2\pi$ s$^{-1}$), but that decreases for flow is smaller arteries. Find how small the artery radius needs to be for Poiseuille flow to be approximately applicable.

The sheet prints "but that decreases for flow is smaller arteries" and has no figure.

Source: VF10.pdf (page 1, statement and handwritten key; no date printed). Notes.pdf, Chapter 7: unidirectional flow, Eqs. 7.6-7.7; Stokes flow near a wall, Eqs. 7.26-7.31; the limits of an oscillating channel, Eqs. 7.33-7.35.

## Hypotheses, Data and Equation

- Incompressible liquid of constant $\rho$ and $\mu$ ($\nu = \mu/\rho$) in a pipe of constant section, so the flow is strictly unidirectional, $v_x(r, t)$ (Eq. 7.1), and the reduced pressure gradient $P_l(t) = A\cos\omega t$ is uniform along the pipe (Eq. 7.4).
- The solution sought is the periodic one, so no initial condition is needed.
- Aorta: $\omega\simeq 2\pi$ s$^{-1}$ (heart rate 1 Hz), $\nu\simeq 4\times 10^{-2}$ cm$^2$/s, $a\simeq 1.2$ cm.

Equation (7.7) with the forcing and its conditions (symmetry on the axis and no slip at the wall), with the scale of each term below it:

$$ \underbrace{\rho\frac{\partial v_x}{\partial t}}_{\rho V_L\omega} = A\cos\omega t + \underbrace{\frac{\mu}{r}\frac{\partial}{\partial r}\left(r\frac{\partial v_x}{\partial r}\right)}_{\mu V_L/a^2}; \qquad r = 0:\; \frac{\partial v_x}{\partial r} = 0, \qquad r = a:\; v_x = 0 $$

The ratio of the local acceleration to the viscous term is $\rho V_L\omega\big/(\mu V_L/a^2) = a^2\omega/\nu$, the square of the Womersley parameter.

## Exact Solution by Separation of Variables

With $A\cos\omega t = \operatorname{Re}\left(Ae^{\imath\omega t}\right)$, solve for a complex $v^*$ with $v_x = \operatorname{Re}(v^*)$:

$$ \rho\frac{\partial v^*}{\partial t} = Ae^{\imath\omega t} + \frac{\mu}{r}\frac{\partial}{\partial r}\left(r\frac{\partial v^*}{\partial r}\right), \qquad v^* = Ae^{\imath\omega t}f(r) $$

Substituting (the factor $e^{\imath\omega t}$ cancels, the variables separate):

$$ \imath\omega\rho f = 1 + \frac{\mu}{r}\frac{d}{dr}\left(r\frac{df}{dr}\right); \qquad f'(0) = 0, \qquad f(a) = 0 $$

This is a linear ordinary equation with a constant forcing. A particular solution is the constant $f_p = 1/(\imath\omega\rho)$ (the pressure gradient balances the acceleration). The homogeneous equation $f'' + f'/r - \kappa^2f = 0$ with $\kappa^2 = \imath\omega/\nu$, $\kappa = (1 + \imath)\sqrt{\omega/(2\nu)}$, is the modified Bessel equation of order zero (outside the notes, an **extension**), whose solution regular on the axis is $I_0(\kappa r)$. The wall condition fixes its coefficient:

$$ f = \frac{1}{\imath\omega\rho}\left[1 - \frac{I_0(\kappa r)}{I_0(\kappa a)}\right], \qquad v_x = \operatorname{Re}\left\{\frac{A}{\imath\omega\rho}\left[1 - \frac{I_0(\kappa r)}{I_0(\kappa a)}\right]e^{\imath\omega t}\right\} $$

Check: since $I_0'' + I_0'/x = I_0$, $f'' + f'/r = -\frac{\kappa^2}{\imath\omega\rho}\frac{I_0(\kappa r)}{I_0(\kappa a)}$, and $\imath\omega\rho f - 1 = -\frac{I_0(\kappa r)}{I_0(\kappa a)}$ while $\frac{\mu}{r}\left(rf'\right)' = \mu\left(f'' + \frac{f'}{r}\right) = -\frac{\mu\kappa^2}{\imath\omega\rho}\frac{I_0(\kappa r)}{I_0(\kappa a)} = -\frac{I_0(\kappa r)}{I_0(\kappa a)}$, so the equation holds; $f(a) = 0$ and $f'(0) = 0$ because $I_0'(0) = 0$.

## Limit $a^2\omega/\nu\ll 1$: Quasi-steady Poiseuille Flow

The viscous time $a^2/\nu$ is much shorter than $\omega^{-1}$, so the unsteady term is negligible and the profile adjusts at every instant:

$$ 0 = A\cos\omega t + \frac{\mu}{r}\frac{\partial}{\partial r}\left(r\frac{\partial v_x}{\partial r}\right) \;\Longrightarrow\; v_x = \frac{A\cos\omega t}{4\mu}\left(a^2 - r^2\right) $$

(the integration of (7.13) with $P_l = A\cos\omega t$). From the exact solution: $I_0(x)\simeq 1 + x^2/4$, so $1 - I_0(\kappa r)/I_0(\kappa a)\simeq\kappa^2(a^2 - r^2)/4$, and $f\simeq\frac{1}{\imath\omega\rho}\frac{\imath\omega}{4\nu}\left(a^2 - r^2\right) = \frac{a^2 - r^2}{4\mu}$.

## Limit $a^2\omega/\nu\gg 1$: Uniform Flow and Stokes Layer

Viscosity is negligible in most of the section, and the equation reduces to the balance of acceleration and pressure force, $\rho\,\partial v_x/\partial t = A\cos\omega t$. Integrating in time (the mean value is zero for the periodic solution):

$$ v_x = \frac{A}{\rho\omega}\sin\omega t $$

a **uniform flow** (the same velocity at every radius) that lags the pressure gradient by a quarter of a period. It does not satisfy the no-slip condition: near the wall there is a thin layer where viscosity matters. The balance $\rho V_L/\omega^{-1}\sim\mu V_L/\delta^2$ gives $\delta\sim\sqrt{\nu/\omega}\ll a$. In it let $\eta = (a - r)/\sqrt{\nu/\omega}$ (the distance to the wall), $\tau = \omega t$ and $\tilde{v} = \frac{A}{\rho\omega}\sin\omega t - v_x$:

$$ \frac{\partial\tilde{v}}{\partial\tau} = \frac{\partial^2\tilde{v}}{\partial\eta^2}; \qquad \eta = 0:\; \tilde{v} = \frac{A}{\rho\omega}\sin\omega t, \qquad \eta\to\infty:\; \tilde{v}\to 0 $$

(the curvature of the pipe is negligible in a layer of thickness $\delta\ll a$). It is the Stokes problem (7.26) for the wall velocity $\frac{A}{\rho\omega}\sin\omega t$, whose solution (7.31), with $\sin$ in place of $\cos$, gives (computed here)

$$ v_x = \frac{A}{\rho\omega}\left[\sin\omega t - e^{-\zeta}\sin(\omega t - \zeta)\right], \qquad \zeta = \frac{a - r}{\sqrt{2\nu/\omega}} $$

which is zero at the wall ($\zeta = 0$) and tends to the uniform flow away from it.

## Blood Flow in the Aorta

$$ \frac{a^2\omega}{\nu} = \frac{(1.2\ \text{cm})^2\,2\pi\ \text{s}^{-1}}{4\times 10^{-2}\ \text{cm}^2/\text{s}} = \frac{1.44\times 6.283}{0.04} = 226, \qquad a\sqrt{\frac{\omega}{\nu}} = \sqrt{226} = 15 $$

The Womersley parameter is about 15, so the flow in the aorta is in the limit $a^2\omega/\nu\gg 1$: a uniform core with a thin viscous layer of thickness $\sqrt{\nu/\omega} = \sqrt{0.04/6.283}\ \text{cm} = 0.0798\ \text{cm}\simeq 0.8$ mm.

**Radius for Poiseuille flow.** Viscosity dominates the whole section, and the profile is the quasi-steady Poiseuille one, when $a^2\omega/\nu\lesssim 1$, that is

$$ a\lesssim\sqrt{\frac{\nu}{\omega}}\simeq 0.8\ \text{mm}, \qquad a\ll 0.8\ \text{mm for a good approximation} $$

(about the size of the smallest arteries and arterioles).

## Answers and Checks

- Problem: $\rho\,\partial v_x/\partial t = A\cos\omega t + \frac{\mu}{r}\partial_r\left(r\,\partial_rv_x\right)$, $\partial_rv_x(0) = 0$, $v_x(a) = 0$; exact solution with $I_0$ (extension).
- $a^2\omega/\nu\ll 1$: $v_x = \frac{A\cos\omega t}{4\mu}(a^2 - r^2)$. $a^2\omega/\nu\gg 1$: $v_x = \frac{A}{\rho\omega}\sin\omega t$, with a Stokes layer of thickness $\sqrt{\nu/\omega}$.
- Aorta: $a^2\omega/\nu\simeq 226$, Womersley parameter $\simeq 15$; Poiseuille flow needs $a\lesssim 0.8$ mm.
- Dimensions: $A/(\rho\omega)$ is $ML^{-2}T^{-2}/(ML^{-3}T^{-1}) = LT^{-1}$; $A a^2/\mu$ is also a velocity.
- Check against the official key: VF10.pdf gives the same equation, the complex-function problem for the separation of variables (left as the ordinary equation), both limits, the layer thickness $\sqrt{\nu/\omega}$, the Stokes problem in $\eta$ and the aorta numbers (226, 15, 0.8 mm).
