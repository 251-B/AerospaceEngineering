---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - semejanza-fisica
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA5.pdf"
id: "da5"
pill: "DA5: Wind turbine"
sheets:
  - 5
tags_html:
  - "Π theorem"
  - "Re ≫ 1"
  - "Experimental curve"
---

# Problem DA5: Power of a Wind Turbine

> Official dimensional-analysis sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem (Notes.pdf, Eq. 6.25), the limit of negligible viscosity (Eq. 6.55) and the conversion of a measured curve between similar states (Eqs. 6.57-6.59).

## Statement

We want to investigate the performance of a wind turbine of given geometrical shape and diameter $D$ rotating with angular velocity $n$ subject to a wind stream of velocity $U$. Assume in the development that the velocity is sufficiently small compared with that of sound that air effectively behaves as an incompressible fluid of constant density and kinematic viscosity $\rho$ and $\nu$.

- Use the dimensional analysis to reduce the parametric dependence of the power produced by the wind turbine $W$.
- Simplify the results by assuming that the effect of viscosity $\mu$ is negligible. Justify the simplification.

We have measured the variation with $n$ of the power delivered by a given turbine of diameter $D = 5$ m on a day when the wind was blowing at $U = 10$ m/s, given the results shown in the plot below.

![[attachments/FM-T6/da5-statement.svg]]
*Statement figure (redrawn from DA5.pdf): power W_1 delivered by the turbine of diameter D = 5 m against its angular velocity n_1 for a wind of U = 10 m/s; the dots are the values read in the official key (4, 5.5, 6.5, 7, 6 and 4.5 kW at 125 to 250 rpm), a reading of the plot*

Based on these results, address the following three questions:

- If the wind velocity on a different day is $U = 15$ m/s, determine the angular velocity required for the turbine to deliver maximum power as well as the resulting power.
- If we fix the angular velocity at $n = 200$ rpm, obtain the power response as a function of the wind velocity $W(U)$.
- Consider a geometrically similar turbine of diameter $D = 10$ m. Obtain the power that it would deliver if placed rotating at $n = 175$ rpm in a wind stream of velocity $U = 20$ m/s.

The sheet prints the last diameter as "10.$^m$" (the unit slipped into a superscript); it is $D = 10$ m.

Source: DA5.pdf (page 1, statement and handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; limits, Eq. 6.55; physical similarity, Eqs. 6.57-6.59.

## Hypotheses, Data and Dimensional Table

- Incompressible air (low Mach number, as the statement says): no speed of sound in the list. No free surface: no gravity.
- Measured state, subscript 1: $D_1 = 5$ m, $U_1 = 10$ m/s, and the curve $W_1(n_1)$, read at the points of the key (a reading of the plot).

| Parameter | Meaning | Dimensions |
| :--- | :--- | :--- |
| $W$ | power delivered (unknown) | $ML^2T^{-3}$ |
| $U$ | wind velocity | $LT^{-1}$ |
| $n$ | angular velocity | $T^{-1}$ |
| $D$ | rotor diameter | $L$ |
| $\rho$ | air density | $ML^{-3}$ |
| $\mu$ | air viscosity | $ML^{-1}T^{-1}$ |

## Application of the Π Theorem

$$ W = W(U, n, D, \rho, \mu) $$

$n = 5$ parameters; $(U, D, \rho)$ have independent dimensions (rows $U(1,0,-1)$, $D(1,0,0)$, $\rho(-3,1,0)$, $\det = -1$, as in DA1), so two groups remain.

**Power.** $[W] = [\rho]^a[U]^b[D]^c$: $M:\; 1 = a$; $T:\; -3 = -b$; $L:\; 2 = -3 + 3 + c$; so $W/(\rho U^3 D^2)$.

**Rotation.** $[n] = [U]^b[D]^c$: $T:\; -1 = -b$; $L:\; 0 = b + c$; so $b = 1$, $c = -1$ and the group is $n/(U/D) = nD/U$, the ratio of the blade-tip speed to the wind speed.

**Viscosity.** As in DA1, $\mu/(\rho U D)$, the inverse of the Reynolds number.

$$ \frac{W}{\rho U^3 D^2} = f\left(\frac{n D}{U}, \frac{\rho U D}{\mu}\right) $$

## Negligible Viscosity

In typical applications $\rho U D/\mu \gg 1$: with $U = 10$ m/s, $D = 5$ m and $\nu \simeq 1.5\times 10^{-5}$ m$^2$/s for air (a standard value, not given in the statement), $\mathrm{Re} = UD/\nu \simeq 3\times 10^{6}$. Viscosity then does not influence the flow through the rotor, and with $\rho$ in the independent set the Reynolds number drops out (Notes.pdf, Eq. 6.55):

$$ \frac{W}{\rho U^3 D^2} = f\left(\frac{n D}{U}\right) $$

Two states with the same $nD/U$ are physically similar, and their powers are related by equal $W/(\rho U^3 D^2)$. The air density is the same in all the cases below, so it cancels.

## Maximum Power at U = 15 m/s

On the measured curve, the maximum is $W_1 = 7$ kW at $n_1 = 200$ rpm. The state at $U_2 = 15$ m/s similar to it (same $D$) has

$$ \frac{n_1}{U_1/D} = \frac{n_2}{U_2/D} \;\Longrightarrow\; n_2 = \frac{U_2}{U_1}\,n_1 = \frac{15}{10}\times 200 = 300\ \text{rpm} $$

$$ \frac{W_1}{\rho U_1^3 D^2} = \frac{W_2}{\rho U_2^3 D^2} \;\Longrightarrow\; W_2 = \left(\frac{U_2}{U_1}\right)^3 W_1 = 1.5^3\times 7 = 3.375\times 7 = 23.625\ \text{kW} $$

Since $f$ has a single maximum, the maximum of $W$ at fixed $U$ is reached at the same $nD/U$ as in the test.

## Power Curve at n = 200 rpm

Each measured point $(n_1, W_1)$ is similar to the state at $n = 200$ rpm with the wind that keeps $nD/U$:

$$ U = \frac{n}{n_1}\,U_1 = \frac{200}{n_1}\times 10\ \text{m/s}, \qquad W = \left(\frac{U}{U_1}\right)^3 W_1 $$

| $n_1$ (rpm) | $W_1$ (kW) | $U$ (m/s) | $(U/U_1)^3$ | $W$ (kW) |
| ---: | ---: | ---: | ---: | ---: |
| 125 | 4 | 16 | 4.096 | 16.38 |
| 150 | 5.5 | 13.33 | 2.370 | 13.04 |
| 175 | 6.5 | 11.43 | 1.493 | 9.70 |
| 200 | 7 | 10 | 1 | 7 |
| 225 | 6 | 8.89 | 0.702 | 4.21 |
| 250 | 4.5 | 8 | 0.512 | 2.30 |

## Larger Turbine

For $D = 10$ m, $n = 175$ rpm and $U = 20$ m/s, the similar measured point has the same $nD/U$:

$$ n_1 = n\,\frac{D}{D_1}\,\frac{U_1}{U} = 175\times\frac{10}{5}\times\frac{10}{20} = 175\ \text{rpm} \;\Longrightarrow\; W_1 = 6.5\ \text{kW} $$

$$ W = \left(\frac{U}{U_1}\right)^3\left(\frac{D}{D_1}\right)^2 W_1 = 2^3\times 2^2\times 6.5 = 8\times 4\times 6.5 = 208\ \text{kW} $$

## Answers and Checks

- Reduced law: $W/(\rho U^3D^2) = f(nD/U, \rho UD/\mu)$, and $f(nD/U)$ for $\mathrm{Re}\gg 1$.
- At $U = 15$ m/s: maximum power at $n = 300$ rpm, $W = 23.6$ kW.
- At $n = 200$ rpm: the table above, from 16.4 kW at 16 m/s to 2.3 kW at 8 m/s.
- Turbine of 10 m at 175 rpm and 20 m/s: $W = 208$ kW.
- Dimensions: $\rho U^3D^2$ is $ML^{-3}\cdot L^3T^{-3}\cdot L^2 = ML^2T^{-3}$; $nD/U$ is $T^{-1}L/(LT^{-1}) = 1$, so rpm can be used on both sides without conversion.
- Check against the official key: DA5.pdf gives $n = 300$ rpm and $W = 23.625$ kW, the table $U$ = 16, 13.3, 11.43, 10, 8.89, 8 m/s with $W$ = 16.38, 13.03, 9.7, 7, 4.2, 2.3 kW, and $W = 208$ kW for the 10 m turbine, the same results (the key truncates $2.370\times 5.5 = 13.037$ to 13.03; rounded, 13.04).
