---
materia: Fluid Mechanics
tema: "Topic 7: Viscous Flows"
tags:
  - problema-examen
  - flujo-viscoso
  - flujo-periodico
  - stokes
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-07-viscous-flow/problemas/VF2_w_solution.pdf"
id: "vf2"
pill: "VF2: Oscillating wall"
sheets:
  - 2
tags_html:
  - "Unsteady unidirectional flow"
  - "Complex solution"
  - "Quasi-steady and Stokes limits"
---

# Problem VF2: Oscillating Wall under a Liquid Layer

> Official viscous-flow sheet of the course, statement transcribed from the sheet, solution after its handwritten key (five pages). Part of [[Topic 7 - Viscous Flows]].
> Method: unidirectional flow (Notes.pdf, Eq. 7.6), complex function for a periodic forcing (Eqs. 7.28-7.30) and the limits $h^2\omega/\nu\ll 1$ and $\gg 1$ (Eqs. 7.31-7.35).

## Statement

Consider the periodic motion induced in a liquid layer of thickness $h$ when the bottom wall moves with velocity $V\cos(\omega t)$. Write the equation with boundary conditions that determines $v_x(y,t)$. Consider separately the cases $\omega h^2/\nu\gg 1$ and $\omega h^2/\nu\ll 1$. Obtain the general solution and show how it reduces to the limiting solutions studied earlier in the appriate limits.

The sheet prints "appriate"; it is kept. The top of the layer is a free surface at the pressure $p_a$, as the figure of the sheet shows.

![[attachments/FM-T7/vf2-statement.svg]]
*Statement figure (redrawn from VF2_w_solution.pdf, p. 1): a liquid layer of thickness h with a free surface at p_a on a wall that oscillates with velocity V cos(ωt); y is normal to the wall and x along it*

Source: VF2_w_solution.pdf (page 1: statement and first solution; pages 2 to 5: handwritten derivation). Notes.pdf, Chapter 7: unidirectional flow, Eq. 7.6; Stokes flow near a wall, Eqs. 7.26-7.31; oscillating wall of a channel, Eqs. 7.32-7.35.

## Hypotheses, Data and Equation

- The liquid has constant $\rho$ and $\mu$. The flow is parallel to the wall: $\bar{v} = v_x(y, t)\,\bar{e}_x$, because continuity gives $\partial v_x/\partial x = 0$ (Notes.pdf, Eq. 7.1).
- **Pressure.** The $y$ component of the momentum equation gives $0 = -\partial P/\partial y$ with $P = p + \rho g y$, so $P$ is the same at every height. At the free surface $p = p_a$ and $y = h$, hence $P = p_a + \rho g h$, a constant: $\partial P/\partial x = 0$ and $P_l = 0$ (the free surface stays flat).
- **Free surface.** The air above exerts a negligible shear stress (its viscosity is neglected), so the shear stress of the liquid vanishes at $y = h$: $\partial v_x/\partial y = 0$.
- **Periodic solution.** The wall velocity is periodic and the sought solution is the permanent one, so no initial condition is needed (Notes.pdf, p. 78). With a forcing $V\sin\omega t$ one could impose $v_x = 0$ at $t = 0$, which is compatible.

Equation (7.6) with $P_l = 0$ and $\nu = \mu/\rho$, and its boundary conditions:

$$ \frac{\partial v_x}{\partial t} = \nu\frac{\partial^2 v_x}{\partial y^2}; \qquad y = 0:\; v_x = V\cos\omega t, \qquad y = h:\; \frac{\partial v_x}{\partial y} = 0 $$

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $h$ | thickness of the layer | m |
| $V$, $\omega$ | amplitude and frequency of the wall velocity | m/s, s$^{-1}$ |
| $\nu$ | kinematic viscosity | m$^2$/s |
| $\omega h^2/\nu$ | ratio of the viscous time $h^2/\nu$ to $\omega^{-1}$ | 1 |

## General Solution with a Complex Function

Since $V\cos\omega t = \operatorname{Re}\left(V e^{\imath\omega t}\right)$, the linear problem is solved for a complex $v^*$ with $v_x = \operatorname{Re}(v^*)$:

$$ \frac{\partial v^*}{\partial t} = \nu\frac{\partial^2 v^*}{\partial y^2}; \qquad y = 0:\; v^* = V e^{\imath\omega t}, \qquad y = h:\; \frac{\partial v^*}{\partial y} = 0 $$

Look for $v^* = V e^{\imath\omega t}f(y)$. Substituting, $\imath\omega f = \nu f''$, that is

$$ f'' - \frac{\imath\omega}{\nu}f = 0; \qquad f(0) = 1, \qquad f'(h) = 0 $$

(in the key's non-dimensional form, $z = y/h$ and $2\Omega^2 = \omega h^2/\nu$, the problem has **one parameter**: $f'' - 2\imath\Omega^2 f = 0$ with $f(0) = 1$, $f'(1) = 0$).

**Characteristic equation.** $\lambda^2 = \imath\omega/\nu$. With $\imath = e^{\imath\pi/4}\cdot e^{\imath\pi/4}$, $\sqrt{\imath} = (1 + \imath)/\sqrt{2}$, so the two roots are $\pm\lambda$ with

$$ \lambda = (1 + \imath)\sqrt{\frac{\omega}{2\nu}}, \qquad \lambda h = (1 + \imath)\,\Omega \quad\text{with}\quad \Omega = \sqrt{\frac{\omega h^2}{2\nu}} $$

(check: $\lambda^2 = (1 + \imath)^2\,\omega/(2\nu) = 2\imath\,\omega/(2\nu) = \imath\omega/\nu$).

**Constants.** $f = C_1e^{\lambda y} + C_2e^{-\lambda y}$. The wall condition gives $C_1 + C_2 = 1$. The condition at the free surface, $f'(h) = \lambda\left(C_1e^{\lambda h} - C_2e^{-\lambda h}\right) = 0$, gives $C_1e^{\lambda h} = C_2e^{-\lambda h}$. Substituting $C_2 = 1 - C_1$:

$$ C_1\left(e^{\lambda h} + e^{-\lambda h}\right) = e^{-\lambda h} \;\Longrightarrow\; C_1 = \frac{e^{-\lambda h}}{e^{\lambda h} + e^{-\lambda h}}, \qquad C_2 = 1 - C_1 = \frac{e^{\lambda h}}{e^{\lambda h} + e^{-\lambda h}} $$

Putting them in $f$:

$$ f = \frac{e^{-\lambda h}e^{\lambda y} + e^{\lambda h}e^{-\lambda y}}{e^{\lambda h} + e^{-\lambda h}} = \frac{e^{\lambda(h - y)} + e^{-\lambda(h - y)}}{e^{\lambda h} + e^{-\lambda h}} = \frac{\cosh\left[\lambda(h - y)\right]}{\cosh(\lambda h)} $$

and the complex solution is

$$ v^* = V e^{\imath\omega t}\,\frac{\cosh\left[(1 + \imath)\Omega(1 - y/h)\right]}{\cosh\left[(1 + \imath)\Omega\right]}, \qquad v_x = \operatorname{Re}(v^*) $$

> [!warning] Discrepancy with the official solution
> The second boundary-condition equation of the key, boxed on page 1, reads $C_1e^{(1+\imath)\sqrt{\omega/2\nu}\,h} - C_2e^{-(1+\imath)\sqrt{\omega/2\nu}\,h} = 1$. The condition $f'(h) = 0$ gives $0$ on the right-hand side, as derived above, and the coefficients $C_1$, $C_2$ that the key writes just below are the ones that follow from $0$, not from $1$. It is a slip in the key; the final solution is not affected.

## The Real Solution

With $s = \Omega(1 - y/h)$ and $\cosh(s + \imath s) = \cosh s\cos s + \imath\sinh s\sin s$:

$$ f = \frac{A + \imath B}{C + \imath D}, \qquad A = \cosh s\cos s,\; B = \sinh s\sin s,\; C = \cosh\Omega\cos\Omega,\; D = \sinh\Omega\sin\Omega $$

Multiplying numerator and denominator by $C - \imath D$ gives $f = \left[(AC + BD) + \imath(BC - AD)\right]/(C^2 + D^2)$. The real part of $e^{\imath\omega t}f$ is $\left[(AC + BD)\cos\omega t - (BC - AD)\sin\omega t\right]/(C^2 + D^2)$ (since $\operatorname{Re}[(\cos\omega t + \imath\sin\omega t)(a + \imath b)] = a\cos\omega t - b\sin\omega t$). Also $C^2 + D^2 = \left(\cosh 2\Omega + \cos 2\Omega\right)/2$, which is the denominator $e^{2\Omega} + e^{-2\Omega} + 2\cos 2\Omega$ of the key up to the factor 4. Then

$$ \frac{v_x}{V} = \frac{(AC + BD)\cos\omega t - (BC - AD)\sin\omega t}{C^2 + D^2} $$

At $y = 0$, $s = \Omega$, so $A = C$ and $B = D$ and $v_x/V = \cos\omega t$, as the wall condition requires. The key obtains the same function as a sum of four terms of the form $e^{\pm\Omega z}\cos(\Omega z \pm \omega t + \dots)$, multiplying by the conjugate of the denominator.

## Limit $\omega h^2/\nu\ll 1$: Quasi-steady Solution

Here $|\lambda h| = \sqrt{2}\,\Omega\ll 1$, so the viscous time $h^2/\nu$ is much shorter than $\omega^{-1}$ and the unsteady term is negligible. The equation reduces to $\partial^2 v_x/\partial y^2 = 0$ with $v_x = V\cos\omega t$ at $y = 0$ and $\partial v_x/\partial y = 0$ at $y = h$. Integrating twice, $v_x = A(t)y + B(t)$; the condition at $y = h$ gives $A = 0$ and the wall gives $B = V\cos\omega t$:

$$ v_x = V\cos\omega t $$

**The liquid layer moves like a solid**: with no shear stress at the free surface, nothing opposes the motion. The exact solution gives the same: $\cosh(x)\simeq 1 + x^2/2$ for small $x$, so $f \simeq 1 + \frac{\lambda^2}{2}\left[(h - y)^2 - h^2\right] = 1 - \frac{\imath\omega}{2\nu}\,y\,(2h - y)\to 1$. The first correction (computed here, an **extension**) is $v_x \simeq V\left[\cos\omega t + \frac{\omega}{2\nu}\,y\,(2h - y)\sin\omega t\right]$, of relative size $\omega h^2/\nu\ll 1$ (it uses $\operatorname{Re}\left[\imath e^{\imath\omega t}\right] = -\sin\omega t$).

## Limit $\omega h^2/\nu\gg 1$: Stokes Layer

Here $\Omega\gg 1$: the thickness $h$ is much larger than the penetration length $\delta = \sqrt{\nu/\omega}$. The sheet first writes $\partial v_x/\partial t = 0$ with two question marks: the right argument is not that the layer is at rest, but that the motion is confined to a thin layer. Balancing $\omega V\sim\nu V/\delta^2$ gives $\delta\sim\sqrt{\nu/\omega}\ll h$, and the problem becomes the one of Stokes (Notes.pdf, Eq. 7.26):

$$ \frac{\partial v_x}{\partial t} = \nu\frac{\partial^2 v_x}{\partial y^2}; \qquad y = 0:\; v_x = V\cos\omega t, \qquad y\gg\sqrt{\nu/\omega}:\; v_x\to 0 $$

whose solution (7.31) is

$$ v_x = V\,e^{-y/\sqrt{2\nu/\omega}}\,\cos\left(\omega t - \frac{y}{\sqrt{2\nu/\omega}}\right) $$

It follows from the exact solution: $\cosh[\lambda(h - y)]/\cosh(\lambda h) = \left[e^{-\lambda y} + e^{-\lambda(2h - y)}\right]/\left[1 + e^{-2\lambda h}\right]$, and $\left|e^{-2\lambda h}\right| = e^{-2\Omega}\to 0$, $\left|e^{-\lambda(2h - y)}\right|\le e^{-\Omega}$ for $y\le h$, so $f\simeq e^{-\lambda y}$ with $\lambda = (1 + \imath)/\sqrt{2\nu/\omega}$, and the real part of $V e^{\imath\omega t}e^{-\lambda y}$ is the expression above. The thickness $h$ **disappears** from the result.

The key solves the same limit in the non-dimensional variable $\eta = y/\delta$ with $\delta^2\omega/\nu = 1$: $f'' - \imath f = 0$, $f(0) = 1$, $f(\infty)$ bounded, so the root with growing exponential has a zero coefficient ($A = 0$, $B = 1$) and $f = e^{-(1 + \imath)\eta/\sqrt{2}}$.

## Answers and Checks

- Problem: $\partial v_x/\partial t = \nu\,\partial^2v_x/\partial y^2$, $v_x(0, t) = V\cos\omega t$, $\partial v_x/\partial y(h, t) = 0$.
- General solution: $v_x = \operatorname{Re}\left\{V e^{\imath\omega t}\cosh\left[(1 + \imath)\Omega(1 - y/h)\right]/\cosh\left[(1 + \imath)\Omega\right]\right\}$ with $\Omega^2 = \omega h^2/(2\nu)$.
- $\omega h^2/\nu\ll 1$: $v_x = V\cos\omega t$ (rigid motion). $\omega h^2/\nu\gg 1$: Stokes solution, independent of $h$.
- Boundary conditions of the general solution: at $y = 0$, $f = 1$; at $y = h$, $\sinh[\lambda(h - y)] = 0$, so $f' = 0$.
- Dimensions: $\omega h^2/\nu$ is $T^{-1}L^2/(L^2T^{-1}) = 1$; $\sqrt{2\nu/\omega}$ is a length.
- Check against the official key: VF2_w_solution.pdf gives the same equation, complex solution, real part, rigid limit and Stokes limit, with the slip in the second boundary-condition equation noted above; the minus sign that the key writes before $e^{-\eta/\sqrt{2}}e^{\imath(\omega t - \eta/\sqrt{2})}$ on page 4 (a reading of the handwriting) also disappears in the real part it boxes.
