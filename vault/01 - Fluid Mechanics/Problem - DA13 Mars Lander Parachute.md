---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - semejanza-fisica
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA13.pdf"
id: "da13"
pill: "DA13: Mars parachute"
sheets:
  - 13
tags_html:
  - "Π theorem"
  - "Froude similarity"
  - "Different planet"
---

# Problem DA13: Mars Lander Parachute

> Official dimensional-analysis sheet of the course (final exam of Jan 21, 2014), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem (Notes.pdf, Eq. 6.25), the limit of negligible viscosity (Eq. 6.55) and physical similarity between two planets (Eqs. 6.57-6.59).

## Statement

**Problem 3**: We want to deposit a module of mass $m$ over the surface of Mars ($\mu_M = 1.2\times 10^{-5}$ kg/(m s), $\rho_M = 0.02$ kg/m$^3$, and $g_M = 3.73$ m/s$^2$) using a parachute of diameter $D_M = 5$ m. To assess the potential damage on landing, we need to know the terminal velocity of parachute descent over Mars $V_M$. For its determination, a series of experiments is carried out in a vertical wind tunnel on Earth ($\mu_E = 1.7\times 10^{-5}$ kg/(m s), $\rho_E = 1.2$ kg/m$^3$, and $g_E = 9.81$ m/s$^2$), using the mission module attached to a model parachute, geometrically similar to that to be used in the Mars mission, but with a different diameter $D_E$. Use dimensional analysis to guide the design of the experiment and the analysis of the results, following the steps given below:

1. Use the Π theorem to express the dependence of $V$ in terms of the minimum number of parameters.

2. Indicate the condition that needs to be satisfied for the effect of viscosity to be negligible. Adopt this simplification in the following.

3. Determine the diameter $D_E$ needed to maintain physical similarity.

4. A terminal velocity $V_E = 2$ m/s is measured in the wind tunnel. Obtain the terminal velocity expected in the Mars mission $V_M$.

5. Verify that the viscosity is actually negligible for the experimental and mission conditions.

![[attachments/FM-T6/da13-statement.svg]]
*Statement figure (redrawn from DA13.pdf): a module of mass m hangs from a parachute of diameter D and falls at its terminal velocity V under gravity g*

Source: DA13.pdf (page 1, final exam of Jan 21, 2014, statement and handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; limits, Eq. 6.55; physical similarity, Eqs. 6.57-6.59.

## Hypotheses, Data and Dimensional Table

- At terminal velocity the weight $mg$ balances the aerodynamic drag of parachute and module; the parachute shape is fixed by geometric similarity, so it is described by $D$.
- The **same module** is used in the tunnel: $m$ is the same in both systems.
- The gas is treated as incompressible (descent speeds of a few m/s).

| Parameter | Meaning | Dimensions |
| :--- | :--- | :--- |
| $V$ | terminal velocity (unknown) | $LT^{-1}$ |
| $\rho$ | atmosphere density | $ML^{-3}$ |
| $\mu$ | atmosphere viscosity | $ML^{-1}T^{-1}$ |
| $g$ | gravity | $LT^{-2}$ |
| $m$ | module mass | $M$ |
| $D$ | parachute diameter | $L$ |

## Application of the Π Theorem

$$ V = V(\rho, \mu, g, m, D) $$

$n = 5$; the key takes $(\rho, g, D)$, with $\det = 2 \neq 0$ (rows $D(1,0,0)$, $g(1,0,-2)$, $\rho(-3,1,0)$, as in DA4), so $k = 3$ and two groups remain. The exponents are those of DA4 with $D$ in place of the particle diameter:

- **Velocity:** $\sqrt{gD}$, a Froude number $V/\sqrt{gD}$.
- **Viscosity:** $\mu/(g^{1/2}D^{3/2}\rho)$.
- **Mass:** $m/(\rho D^3)$, the module mass against the mass of air in a volume $D^3$.

$$ \frac{V}{\sqrt{gD}} = f\left(\frac{\mu}{g^{1/2}D^{3/2}\rho}, \frac{m}{\rho D^3}\right) $$

## Negligible Viscosity

The viscosity group is the inverse of a Reynolds number built with $\sqrt{gD}$; equivalently, viscosity is negligible when the Reynolds number of the descent is large,

$$ \frac{\rho VD}{\mu} \gg 1 $$

and then (Notes.pdf, Eq. 6.55)

$$ \frac{V}{\sqrt{gD}} = f\left(\frac{m}{\rho D^3}\right) $$

## Diameter of the Model Parachute

Only $m/(\rho D^3)$ must be matched, with the same $m$:

$$ \frac{m}{\rho_E D_E^3} = \frac{m}{\rho_M D_M^3} \;\Longrightarrow\; D_E = D_M\left(\frac{\rho_M}{\rho_E}\right)^{1/3} = 5\times\left(\frac{0.02}{1.2}\right)^{1/3} = 5\times 0.2554 = 1.28\ \text{m} $$

The thin Martian air needs a parachute $(\rho_E/\rho_M)^{1/3} = 60^{1/3} = 3.9$ times wider than on Earth for the same module.

## Terminal Velocity on Mars

With $m/(\rho D^3)$ equal, the Froude numbers are equal:

$$ \frac{V_E}{\sqrt{g_ED_E}} = \frac{V_M}{\sqrt{g_MD_M}} \;\Longrightarrow\; V_M = \sqrt{\frac{g_MD_M}{g_ED_E}}\,V_E = \left(\frac{g_M}{g_E}\right)^{1/2}\left(\frac{\rho_E}{\rho_M}\right)^{1/6}V_E $$

using $D_M/D_E = (\rho_E/\rho_M)^{1/3}$, whose square root is $(\rho_E/\rho_M)^{1/6}$. Numbers: $(3.73/9.81)^{1/2} = 0.3802^{1/2} = 0.6166$ and $60^{1/6} = 1.979$:

$$ V_M = 0.6166\times 1.979\times 2 = 2.44\ \text{m/s} $$

## Check of Negligible Viscosity

$$ \text{Earth: } \frac{\rho_EV_ED_E}{\mu_E} = \frac{1.2\times 2\times 1.28}{1.7\times 10^{-5}} = 1.81\times 10^{5} \gg 1, \qquad \text{Mars: } \frac{\rho_MV_MD_M}{\mu_M} = \frac{0.02\times 2.44\times 5}{1.2\times 10^{-5}} = 2.03\times 10^{4} \gg 1 $$

Viscosity is negligible in both.

## Answers and Checks

- Reduced law: $V/\sqrt{gD} = f\left(\mu/(g^{1/2}D^{3/2}\rho),\, m/(\rho D^3)\right)$.
- Viscosity negligible if $\rho VD/\mu \gg 1$; then $V/\sqrt{gD} = f\left(m/(\rho D^3)\right)$.
- Model parachute: $D_E = 1.28$ m.
- Mars terminal velocity: $V_M = 2.44$ m/s.
- Reynolds numbers: $1.8\times 10^5$ (Earth) and $2.0\times 10^4$ (Mars).
- Dimensions: $\sqrt{gD}$ is $(LT^{-2}\cdot L)^{1/2} = LT^{-1}$; $m/(\rho D^3)$ is $M/(ML^{-3}L^3) = 1$.
- Physical check: in the limit $\mathrm{Re}\gg 1$ the drag is $\propto \rho V^2D^2$ (Notes.pdf, Eq. 6.51), and the balance $mg \propto \rho V^2D^2$ gives $V \propto (mg/\rho)^{1/2}/D$; with $\rho D^3$ fixed, $V_M/V_E = (g_M/g_E)^{1/2}(\rho_E/\rho_M)^{1/2}(D_E/D_M) = 0.6166\times 7.746/3.915 = 1.22$, the same factor $2.44/2$.
- Check against the official key: DA13.pdf gives $D_E = 1.28$ m, $V_M = 2.44$ m/s and the Reynolds numbers 180 705 and 20 333 (computed with $D_E = 1.28$ m and $V_M = 2.44$ m/s), the same results.
