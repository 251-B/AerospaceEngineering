---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - esferas-concentricas
  - analisis-dimensional
  - flujo-viscoso
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS12.pdf"
id: "ns12"
pill: "NS12: Spheres"
tags_html:
  - "Dimensional analysis"
  - "Spherical coordinates"
  - "Separation of variables"
  - "Volume flux"
---

# Problem NS12: Flow between Concentric Spheres

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

A very viscous liquid (of constant density $\rho$ and viscosity $\mu$) flows steadily through the gap between two concentric spheres, as shown in the figure. The flow is driven by a given pressure difference between the entrance and exit section, $\Delta p = p_i - p_o$, and gravity effects are negligible. We wish to determine the resulting volume flux $Q$ as a function of the known geometry data, fluid properties and pressure difference, $Q(R, \kappa, \epsilon, \rho, \mu, \Delta p)$.

1. Apply the dimensional analysis technique to write the parametric dependence of $Q$ as a function of the minimum number of parameters.

2. Simplify the non-dimensional relation for the case of flow dominated by viscous forces, for which the liquid inertia is negligible.

3. Disregarding end effects in the entrance and exit regions, we can assume that the flow is unidirectional and symmetric, $\bar{v} = v_\theta(r, \theta)\bar{e}_\theta$ (note that $v_r = v_\phi = 0$ and $\partial/\partial\phi = 0$). With this assumption, write the simplified continuity and momentum equations in spherical coordinates, as well as the necessary boundary conditions to solve the system. Write the expression to evaluate the volume flux $Q$ and then check that the parametric dependence stated earlier, that is $Q(R, \kappa, \epsilon, \rho, \mu, \Delta p)$, is correct.

4. Simplify the $\theta$-momentum equation with the assumption that the velocity is small enough for the viscous terms to be dominant over the convective terms. Under this conditions, the radial pressure variations are negligible compared with $\Delta p$ and we can consider that the pressure is a function of $\theta$ alone, $p(\theta)$.

5. Write the mathematical formulation (equations and boundary conditions) in non-dimensional form. Use the non-dimensional variables $\tilde{r} = r/R$, $\tilde{v}_\theta = v_\theta/V_\theta$ and $\tilde{p} = (p - p_o)/\Delta p$, where you can define $V_\theta$ such that there are no parameters in the non-dimensional equation.

6. Using the continuity equation, show that $\tilde{v}_\theta\sin\theta = \tilde{u}(\tilde{r})$, where $\tilde{u}(\tilde{r})$ is a function of $\tilde{r}$ to be determined.

7. Rewrite the $\theta$-momentum equation in terms of the function $\tilde{u}(\tilde{r})$ instead of $\tilde{v}_\theta$ and separate variables to show that
$$ \operatorname{sen}\theta\,\frac{d\tilde{p}}{d\theta} = C $$
$$ \frac{1}{\tilde{r}}\frac{d}{d\tilde{r}}\left(\tilde{r}^2\frac{d\tilde{u}}{d\tilde{r}}\right) = C $$
where $C$ is a constant.

8. Integrate the ODE for the pressure and determine the value of the constant $C$ Note that the boundary conditions for the pressure are to be applied at $\theta = \epsilon$ and $\theta = \pi - \epsilon$.

9. With the known value of $C$, integrate the ode for $\tilde{u}(\tilde{r})$ obtained in item and thus obtain the velocity profile $\tilde{v}_\theta(\tilde{r}, \theta)$.

10. Define a proper non-dimensional form for the volume flux $\tilde{Q}$ and obtain it by integration of the velocity profile.

Transcribed as printed (exam of June 27, 2013, "PROBLEM 1 (90 minutes)"), including "Under this conditions", the missing full stop after "constant $C$" in item 8 the missing item number and the lower-case "ode" in item 9.

![[attachments/FM-T4/ns12-statement.png]]
*Statement figure (crop of NS12.pdf, p. 1): gap between two concentric spheres of radii $\kappa R$ and $R$, entrance and exit sections of half-angle $\epsilon$ and the radial coordinate $r$*

Source: NS12.pdf (page 1 of 4: statement; pages 2 to 4: handwritten solution). Notes.pdf, Chapter 4: continuity Eq. 4.40 and momentum Eq. 4.41 in spherical coordinates; dimensional analysis of Unit 6 is used for item 1.

## Phase 1: Hypotheses, Data and Unknowns

- Steady flow of a very viscous incompressible liquid (constant $\rho$, $\mu$), gravity neglected. The liquid flows through the gap $\kappa R \leq r \leq R$ between two concentric spheres, from an entrance section (polar angle $0 \leq \theta \leq \epsilon$ of the outer sphere, pressure $p_i$) to an exit section ($\pi - \epsilon \leq \theta \leq \pi$, pressure $p_o$).
- Away from the end regions the flow is unidirectional and symmetric: $\bar{v} = v_\theta(r,\theta)\,\bar{e}_\theta$, $v_r = v_\phi = 0$, $\partial/\partial\phi = 0$; the model domain is $\kappa R \leq r \leq R$, $\epsilon \leq \theta \leq \pi - \epsilon$.
- Data: $[R,\ \kappa,\ \epsilon,\ \rho,\ \mu,\ \Delta p]$ with $0 < \kappa < 1$. Unknowns: $Q$, $v_\theta(r,\theta)$, $p(\theta)$.
- The "viscous" regime is the limit in which the dimensionless group $\rho\,\Delta p\,R^2/\mu^2$ is small.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R$, $\kappa R$ | outer and inner sphere radii | m |
| $\epsilon$ | half-angle of the entrance and exit sections | rad |
| $\Delta p = p_i - p_o$ | driving pressure difference | Pa |
| $Q$ | volume flux through the gap | m$^3$/s |
| $V_\theta$ | velocity scale, defined in item 5 | m/s |
| $\rho$, $\mu$ | density and viscosity | kg/m$^3$, Pa s |

## Phase 2: Frames, Field Form and Boundary Conditions

- Spherical frame $(r,\theta,\phi)$ centred on the common centre of the spheres, with the axis through the entrance and exit; the basis $\{\bar{e}_r,\bar{e}_\theta,\bar{e}_\phi\}$ is orthonormal and right-handed.
- Field form: $\bar{v} = v_\theta(r,\theta)\,\bar{e}_\theta$, $p = p(r,\theta)$ (reduced to $p(\theta)$ in item 4).

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $r = \kappa R$ | $v_\theta = 0$ | no-slip on the inner sphere |
| $r = R$ | $v_\theta = 0$ | no-slip on the outer sphere |
| $\theta = \epsilon$ | $p = p_i$ | entrance section |
| $\theta = \pi - \epsilon$ | $p = p_o$ | exit section |

## Phase 3: Step-by-Step Derivation

### 3.1 Dimensional analysis (items 1 and 2)

The variables of the problem are $Q$, $R$, $\kappa$, $\epsilon$, $\rho$, $\mu$, $\Delta p$. The dimensional ones, $Q\ [\mathrm{L^3T^{-1}}]$, $R\ [\mathrm{L}]$, $\rho\ [\mathrm{ML^{-3}}]$, $\mu\ [\mathrm{ML^{-1}T^{-1}}]$ and $\Delta p\ [\mathrm{ML^{-1}T^{-2}}]$, are five and involve three fundamental dimensions (M, L, T), so by the Vaschy-Buckingham theorem there are $5 - 3 = 2$ dimensionless groups from them; $\kappa$ and $\epsilon$ are already dimensionless. Choosing $R$, $\mu$ and $\Delta p$ as repeated variables:

$$ \Pi_1 = \frac{Q\,\mu}{\Delta p\,R^3}, \qquad \Pi_2 = \frac{\rho\,\Delta p\,R^2}{\mu^2} $$

Check: $\Pi_1 = (\mathrm{L^3T^{-1}})(\mathrm{ML^{-1}T^{-1}})/[(\mathrm{ML^{-1}T^{-2}})\,\mathrm{L^3}] = 1$ and $\Pi_2 = (\mathrm{ML^{-3}})(\mathrm{ML^{-1}T^{-2}})\,\mathrm{L^2}/(\mathrm{M^2L^{-2}T^{-2}}) = 1$. The minimum parametric dependence is

$$ \boxed{\,\frac{Q\,\mu}{\Delta p\,R^3} = f\left(\kappa,\ \epsilon,\ \frac{\rho\,\Delta p\,R^2}{\mu^2}\right)\,} \tag{1} $$

The group $\Pi_2$ is a Reynolds number: with the viscous velocity $V = \Delta p\,R/\mu$, $\rho VR/\mu = \rho\Delta pR^2/\mu^2$. When viscous forces dominate and the inertia of the liquid is negligible, the density disappears from the problem and the dependence on $\Pi_2$ is lost:

$$ \boxed{\,\frac{Q\,\mu}{\Delta p\,R^3} = f(\kappa,\ \epsilon)\,} \tag{2} $$

### 3.2 Equations and boundary conditions (item 3)

*Continuity* in spherical coordinates with $v_r = v_\phi = 0$ and $\partial_\phi = 0$:

$$ \frac{1}{r\sin\theta}\frac{\partial(v_\theta\sin\theta)}{\partial\theta} = 0 \;\Longrightarrow\; \frac{\partial(v_\theta\sin\theta)}{\partial\theta} = 0 \tag{3} $$

*Momentum* (steady, no mass force), the three components of (4.41) with $v_r = v_\phi = 0$. In the viscous terms of the $\theta$ component, $\dfrac{1}{r^2}\dfrac{\partial}{\partial\theta}\left[\dfrac{1}{\sin\theta}\dfrac{\partial(v_\theta\sin\theta)}{\partial\theta}\right]$ contains the left side of (3), so it vanishes; the terms with $v_r$, $v_\phi$ and $\partial_\phi$ vanish too. The $r$ component keeps the centrifugal term and the $\phi$ component only the pressure derivative:

$$ -\rho\frac{v_\theta^2}{r} = -\frac{\partial p}{\partial r} \tag{4} $$

$$ \rho\frac{v_\theta}{r}\frac{\partial v_\theta}{\partial\theta} = -\frac{1}{r}\frac{\partial p}{\partial\theta} + \mu\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial v_\theta}{\partial r}\right) \tag{5} $$

$$ 0 = -\frac{1}{r\sin\theta}\frac{\partial p}{\partial\phi} \;\Longrightarrow\; \frac{\partial p}{\partial\phi} = 0 \tag{6} $$

*Boundary conditions* (table of Phase 2): $v_\theta(\kappa R,\theta) = 0$, $v_\theta(R,\theta) = 0$, $p = p_i$ at $\theta = \epsilon$ and $p = p_o$ at $\theta = \pi - \epsilon$. Writing $p' = p - p_o$ (so $dp' = dp$), these are $p'(\theta = \epsilon) = \Delta p$ and $p'(\theta = \pi - \epsilon) = 0$.

*Volume flux.* Through the equatorial section $\theta = \pi/2$, the annulus $\kappa R \leq r \leq R$ with area element $2\pi r\,dr$:

$$ Q = \int_{\kappa R}^R v_\theta\left(r,\tfrac{\pi}{2}\right)2\pi r\,dr \tag{7} $$

*Check of the parametric dependence.* The system (3)-(5) with its boundary conditions contains only $\rho$, $\mu$, $R$, $\kappa$, $\epsilon$ and $\Delta p$, so $Q = Q(R,\kappa,\epsilon,\rho,\mu,\Delta p)$, as stated.

### 3.3 Viscous-dominated flow (item 4)

Estimate the sizes of the terms of (5): the pressure term is $\Delta p/R$, the viscous term is $\mu V_\theta/R^2$ and the convective term is $\rho V_\theta^2/R$. The first two balance if $V_\theta \sim \Delta p\,R/\mu$, and the ratio of the convective term to the pressure term is then $\rho V_\theta^2/\Delta p \sim \rho\Delta pR^2/\mu^2 = \Pi_2 \ll 1$. The convective term is dropped. In (4) the radial pressure variation is of order $\rho V_\theta^2$, also small against $\Delta p$ by the same factor, so $p = p(\theta)$ and (5) becomes

$$ 0 = -\frac{1}{r}\frac{dp}{d\theta} + \frac{\mu}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial v_\theta}{\partial r}\right) \tag{8} $$

### 3.4 Non-dimensional formulation (item 5)

With $\tilde{r} = r/R$, $\tilde{v}_\theta = v_\theta/V_\theta$ and $\tilde{p} = (p - p_o)/\Delta p$, the pressure term of (8) is $(\Delta p/(R\tilde{r}))\,d\tilde{p}/d\theta$ and the viscous term is $(\mu V_\theta/R^2)(1/\tilde{r}^2)\,\partial(\tilde{r}^2\partial\tilde{v}_\theta/\partial\tilde{r})/\partial\tilde{r}$. Choosing $V_\theta = \Delta p\,R/\mu$ makes the two coefficients equal, and multiplying by $\tilde{r}$:

$$ 0 = -\frac{d\tilde{p}}{d\theta} + \frac{1}{\tilde{r}}\frac{\partial}{\partial\tilde{r}}\left(\tilde{r}^2\frac{\partial\tilde{v}_\theta}{\partial\tilde{r}}\right), \qquad \frac{\partial(\tilde{v}_\theta\sin\theta)}{\partial\theta} = 0 \tag{9} $$

with the boundary conditions

$$ \tilde{v}_\theta(\kappa,\theta) = \tilde{v}_\theta(1,\theta) = 0, \qquad \tilde{p}(\epsilon) = 1, \qquad \tilde{p}(\pi - \epsilon) = 0 \tag{10} $$

and the flux

$$ \tilde{Q} = \frac{Q\,\mu}{\Delta p\,R^3} = 2\pi\int_\kappa^1\tilde{v}_\theta\left(\tilde{r},\tfrac{\pi}{2}\right)\tilde{r}\,d\tilde{r} \tag{11} $$

The problem has no parameters except $\kappa$ and $\epsilon$ (through the boundary conditions and the integration limits), so $\tilde{Q} = \tilde{Q}(\kappa,\epsilon)$, in agreement with (2).

### 3.5 Continuity and separation of variables (items 6 and 7)

From (9), $\partial(\tilde{v}_\theta\sin\theta)/\partial\theta = 0$, so $\tilde{v}_\theta\sin\theta$ does not depend on $\theta$:

$$ \tilde{v}_\theta\,\sin\theta = \tilde{u}(\tilde{r}) \tag{12} $$

Substituting $\tilde{v}_\theta = \tilde{u}/\sin\theta$ in the momentum equation of (9):

$$ \frac{d\tilde{p}}{d\theta} = \frac{1}{\tilde{r}\sin\theta}\frac{d}{d\tilde{r}}\left(\tilde{r}^2\frac{d\tilde{u}}{d\tilde{r}}\right) \;\Longrightarrow\; \sin\theta\,\frac{d\tilde{p}}{d\theta} = \frac{1}{\tilde{r}}\frac{d}{d\tilde{r}}\left(\tilde{r}^2\frac{d\tilde{u}}{d\tilde{r}}\right) \tag{13} $$

The left side depends only on $\theta$ and the right side only on $\tilde{r}$, so both are equal to a constant $C$ (which may depend on $\kappa$ and $\epsilon$):

$$ \boxed{\,\sin\theta\,\frac{d\tilde{p}}{d\theta} = C, \qquad \frac{1}{\tilde{r}}\frac{d}{d\tilde{r}}\left(\tilde{r}^2\frac{d\tilde{u}}{d\tilde{r}}\right) = C\,} \tag{14} $$

### 3.6 Pressure and the constant $C$ (item 8)

From (14), $d\tilde{p}/d\theta = C/\sin\theta$. Integrating from $\theta = \epsilon$ (where $\tilde{p} = 1$) to $\theta = \pi - \epsilon$ (where $\tilde{p} = 0$):

$$ 0 - 1 = C\int_\epsilon^{\pi-\epsilon}\frac{d\theta}{\sin\theta} \equiv C\,E(\epsilon) \;\Longrightarrow\; \boxed{\,C = -\frac{1}{E(\epsilon)}\,} \tag{15} $$

The antiderivative of $1/\sin\theta$ is $\ln\tan(\theta/2)$ (its derivative is $\dfrac{1}{2\sin(\theta/2)\cos(\theta/2)} = \dfrac{1}{\sin\theta}$), and Barrow's rule with $\tan\left(\frac{\pi - \epsilon}{2}\right) = \cot(\epsilon/2)$ gives

$$ E(\epsilon) = \left[\ln\tan\frac{\theta}{2}\right]_\epsilon^{\pi-\epsilon} = \ln\cot\frac{\epsilon}{2} - \ln\tan\frac{\epsilon}{2} = -2\ln\tan\frac{\epsilon}{2} = \ln\frac{1 + \cos\epsilon}{1 - \cos\epsilon} \tag{16} $$

(using $\tan^2(\epsilon/2) = (1 - \cos\epsilon)/(1 + \cos\epsilon)$). The pressure is $\tilde{p}(\theta) = 1 - \left[\ln\tan(\theta/2) - \ln\tan(\epsilon/2)\right]/E(\epsilon)$.

### 3.7 Velocity profile (item 9)

The second equation of (14): $\dfrac{d}{d\tilde{r}}\left(\tilde{r}^2\tilde{u}'\right) = C\tilde{r}$. Integrating, $\tilde{r}^2\tilde{u}' = C\tilde{r}^2/2 + A$, so $\tilde{u}' = C/2 + A/\tilde{r}^2$, and again $\tilde{u} = C\tilde{r}/2 - A/\tilde{r} + B$. The conditions $\tilde{u}(1) = 0$ and $\tilde{u}(\kappa) = 0$ (from $\tilde{v}_\theta = 0$ at both spheres) give

$$ \frac{C}{2} - A + B = 0, \qquad \frac{C\kappa}{2} - \frac{A}{\kappa} + B = 0 $$

Subtracting, $\frac{C}{2}(1 - \kappa) - A\left(1 - \frac{1}{\kappa}\right) = 0$, hence $A = -C\kappa/2$ and $B = A - C/2 = -C(1 + \kappa)/2$:

$$ \tilde{u}(\tilde{r}) = -\frac{C}{2}\left[1 - \tilde{r} + \kappa\left(1 - \frac{1}{\tilde{r}}\right)\right] = -\frac{C}{2}\,\frac{(1 - \tilde{r})(\tilde{r} - \kappa)}{\tilde{r}} \tag{17} $$

and, with (15) and $\tilde{v}_\theta = \tilde{u}/\sin\theta$,

$$ \boxed{\,\tilde{v}_\theta(\tilde{r},\theta) = \frac{1}{2E(\epsilon)\,\sin\theta}\left[1 - \tilde{r} + \kappa\left(1 - \frac{1}{\tilde{r}}\right)\right]\,} \tag{18} $$

The bracket equals $(1 - \tilde{r})(\tilde{r} - \kappa)/\tilde{r}$, which is positive in $\kappa < \tilde{r} < 1$: the flow goes from the entrance to the exit, with the largest velocity at the equator ($\sin\theta = 1$).

### 3.8 Volume flux (item 10)

The non-dimensional flux is $\tilde{Q} = Q\mu/(\Delta pR^3)$, (11). At $\theta = \pi/2$, $\sin\theta = 1$ and $\tilde{v}_\theta = \tilde{u}$:

$$ \tilde{Q} = 2\pi\int_\kappa^1\tilde{u}\,\tilde{r}\,d\tilde{r} = \frac{\pi}{E(\epsilon)}\int_\kappa^1\left(1 - \tilde{r}\right)\left(\tilde{r} - \kappa\right)d\tilde{r} \tag{19} $$

The integrand is $-\tilde{r}^2 + (1 + \kappa)\tilde{r} - \kappa$, with antiderivative $-\tilde{r}^3/3 + (1 + \kappa)\tilde{r}^2/2 - \kappa\tilde{r}$; Barrow's rule between $\kappa$ and $1$ gives $\dfrac{(1 - \kappa)^3}{6}$ (check: $\int_a^b(b - r)(r - a)\,dr = (b - a)^3/6$). Therefore

$$ \boxed{\,\tilde{Q} = \frac{\pi\,(1 - \kappa)^3}{6\,E(\epsilon)}, \qquad Q = \frac{\pi\,\Delta p\,R^3\,(1 - \kappa)^3}{6\,\mu\,E(\epsilon)}\,}, \qquad E(\epsilon) = \ln\frac{1 + \cos\epsilon}{1 - \cos\epsilon} \tag{20} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** The flow in the gap is a Poiseuille-like flow along the meridians: the pressure drop $\Delta p$ is distributed as $\ln\tan(\theta/2)$ along $\theta$, and across the gap the velocity has the parabola-like shape (17) that vanishes at both spheres. The flux is proportional to $\Delta p/\mu$, as every Stokes flow, and to the cube of the gap, $(1 - \kappa)^3R^3$.
- **Limits.** For $\kappa \to 1$ the gap closes and $Q \to 0$ as $(1 - \kappa)^3$. For $\epsilon \to 0$ the end sections shrink and $E(\epsilon) \simeq 2\ln(2/\epsilon) \to \infty$, so $Q$ vanishes only logarithmically. For $\epsilon \to \pi/2$ the sections cover the whole hemispheres and $E \to 0$ makes $Q \to \infty$, which is the breakdown of the unidirectional model (the end effects it neglects then control the flow).
- **Validity.** The result requires $\rho\Delta pR^2/\mu^2 \ll 1$ (item 4).
- **Dimensional check.** $\Delta pR^3/\mu$ has units $(\mathrm{N/m^2})\,\mathrm{m^3}/(\mathrm{Pa\,s}) = \mathrm{m^3/s}$, the units of $Q$. $V_\theta = \Delta pR/\mu$ has units m/s. $E(\epsilon)$ and $\tilde{Q}$ are dimensionless.
- **Consistency of the profile.** The flux through the cone $\theta = \text{const}$ (area element $2\pi\tilde{r}\sin\theta\,d\tilde{r}$, normal velocity $\tilde{v}_\theta$) is $2\pi\int_\kappa^1\tilde{v}_\theta\sin\theta\,\tilde{r}\,d\tilde{r} = 2\pi\int_\kappa^1\tilde{u}\,\tilde{r}\,d\tilde{r}$, independent of $\theta$ as continuity requires; item 10 evaluates it at $\theta = \pi/2$, where the cone is the equatorial plane.
