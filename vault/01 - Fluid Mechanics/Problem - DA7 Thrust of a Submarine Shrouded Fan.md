---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - semejanza-fisica
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA7.pdf"
id: "da7"
pill: "DA7: Submarine fan"
sheets:
  - 7
tags_html:
  - "Π theorem"
  - "Fractional exponents"
  - "Re ≫ 1"
---

# Problem DA7: Thrust of a Submarine Shrouded Fan

> Official dimensional-analysis sheet of the course (exam of 17-05-2010), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem with a power among the independent parameters (Notes.pdf, Eq. 6.25), the limit of negligible viscosity (Eq. 6.55) and physical similarity (Eqs. 6.57-6.59).

## Statement

The submarine propulsion device schematically represented in the figure consists of a nozzle, with inlet and outlet crosssection area $A_e$ and $A_s$, and a fan located inside, which imparts a rate of work per unit time (power) $\dot{W}$ to the circulating water stream, whose density and viscosity are $\rho$ and $\mu$, respectively. To characterize the thrust $E$ produced when the submarine is at rest and at sufficient depth for gravity to have a negligible effect, please follow these steps:

1. By application of the Π theorem, reduce the parametric dependence of the thrust $E$.

2. Simplify the result assuming that the viscosity has a negligible effect, **justifying** the simplification. Maintain this assumption in addressing the next question.

3. An experimental test is conducted with a geometrically similar model with scale 1/10. It is found that, for a fan power $\dot{W}_e = 100$ Watts the resulting thrust is $E_e = 125$ N. If a thrust $E_p = 12500$ N is needed for the real prototype, determine the power $W$ necessary to drive the fan.

The subscript of the prototype thrust is blurred in the scan; it reads as $E_p$ (prototype).

![[attachments/FM-T6/da7-statement.svg]]
*Statement figure (redrawn from DA7.pdf): a nozzle of inlet area A_e and outlet area A_s with a fan inside that gives the power Ẇ to water of density ρ and viscosity μ; E is the thrust*

Source: DA7.pdf (page 1, exam of 17-05-2010, statement and handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; limits, Eq. 6.55; physical similarity, Eqs. 6.57-6.59.

## Hypotheses, Data and Dimensional Table

- The submarine is at rest, so there is no free-stream velocity: the only "motor" of the flow is the power $\dot{W}$. Gravity is negligible (deep water, no free surface).
- The nozzle is defined by its two areas (the rest of the shape by geometric similarity). Same water in the model and in the prototype.

| Parameter | Meaning | Dimensions |
| :--- | :--- | :--- |
| $E$ | thrust (unknown) | $MLT^{-2}$ |
| $\dot{W}$ | fan power | $ML^2T^{-3}$ |
| $\rho$ | water density | $ML^{-3}$ |
| $\mu$ | water viscosity | $ML^{-1}T^{-1}$ |
| $A_e$, $A_s$ | inlet and outlet areas | $L^2$ |

## Application of the Π Theorem

$$ E = E(\dot{W}, \rho, \mu, A_e, A_s) $$

$n = 5$. Since no velocity is given, the independent set must use the power: $(\rho, \dot{W}, A_s)$. Rows in $(L, M, T)$: $\rho(-3, 1, 0)$, $\dot{W}(2, 1, -3)$, $A_s(2, 0, 0)$. Expanding along the third row, $\det = 2\cdot(1\cdot(-3) - 0\cdot 1) = -6 \neq 0$, so $k = 3$ and two groups remain.

**Thrust.** $[E] = [\rho]^a[\dot{W}]^b[A_s]^c$:

$$ M:\; 1 = a + b, \qquad T:\; -2 = -3b, \qquad L:\; 1 = -3a + 2b + 2c $$

so $b = 2/3$, $a = 1/3$ and $2c = 1 + 1 - \tfrac{4}{3} = \tfrac{2}{3}$, $c = 1/3$: the scale $\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}$.

**Viscosity.** $[\mu] = [\rho]^a[\dot{W}]^b[A_s]^c$:

$$ M:\; 1 = a + b, \qquad T:\; -1 = -3b, \qquad L:\; -1 = -3a + 2b + 2c $$

so $b = 1/3$, $a = 2/3$ and $2c = -1 + 2 - \tfrac{2}{3} = \tfrac{1}{3}$, $c = 1/6$. The group is $\mu/(\rho^{2/3}\dot{W}^{1/3}A_s^{1/6})$; its inverse plays the role of a Reynolds number.

**Areas.** $A_e/A_s$.

$$ \frac{E}{\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}} = f\left(\frac{A_e}{A_s}, \frac{\rho^{2/3}A_s^{1/6}\dot{W}^{1/3}}{\mu}\right) $$

Check that the last group is a Reynolds number: a velocity scale built from the power is $U_s = (\dot{W}/(\rho A_s))^{1/3}$ (kinetic-energy flux $\rho U^3 A \sim \dot{W}$), and $\rho U_s A_s^{1/2}/\mu = \rho^{2/3}\dot{W}^{1/3}A_s^{1/2 - 1/3}/\mu = \rho^{2/3}\dot{W}^{1/3}A_s^{1/6}/\mu$, the same group.

## Negligible Viscosity

If

$$ \frac{\rho^{2/3}A_s^{1/6}\dot{W}^{1/3}}{\mu} \gg 1 $$

viscosity is negligible and the group drops out (Notes.pdf, Eq. 6.55):

$$ \frac{E}{\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}} = f\left(\frac{A_e}{A_s}\right) $$

Justification with the test data (water, $\rho = 10^3$ kg/m$^3$, $\mu = 10^{-3}$ kg/(m s)): the model area is not given, but any reasonable outlet, e.g. $A_s \sim 10^{-2}$ m$^2$, with $\dot{W} = 100$ W gives $\rho^{2/3}A_s^{1/6}\dot{W}^{1/3}/\mu = 100\times 0.46\times 4.64/10^{-3} \simeq 2\times 10^{5} \gg 1$ (an estimate, since the size is assumed).

## Physical Similarity and Prototype Power

Geometric similarity gives the same $A_e/A_s$, so the dimensionless thrust is the same; with the same water:

$$ \frac{E_p}{\rho^{1/3}\dot{W}^{2/3}A_{s}^{1/3}} = \frac{E_e}{\rho^{1/3}\dot{W}_e^{2/3}A_{se}^{1/3}} \;\Longrightarrow\; \dot{W}^{2/3} = \frac{E_p}{E_e}\left(\frac{A_{se}}{A_s}\right)^{1/3}\dot{W}_e^{2/3} $$

and raising to $3/2$:

$$ \dot{W} = \left(\frac{E_p}{E_e}\right)^{3/2}\left(\frac{A_{se}}{A_s}\right)^{1/2}\dot{W}_e $$

Scale 1/10 in length means $A_{se}/A_s = 1/100$:

$$ \dot{W} = \left(\frac{12500}{125}\right)^{3/2}\left(\frac{1}{100}\right)^{1/2}\times 100\ \text{W} = 100^{3/2}\times\frac{1}{10}\times 100 = 1000\times\frac{1}{10}\times 100 = 10^{4}\ \text{W} $$

## Answers and Checks

- Reduced law: $E/(\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}) = f\left(A_e/A_s,\, \rho^{2/3}A_s^{1/6}\dot{W}^{1/3}/\mu\right)$.
- With $\rho^{2/3}A_s^{1/6}\dot{W}^{1/3}/\mu \gg 1$: $E/(\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}) = f(A_e/A_s)$.
- Prototype power: $\dot{W} = 10^4$ W = 10 kW.
- Dimensions: $\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}$ is $M^{1/3}L^{-1}\cdot M^{2/3}L^{4/3}T^{-2}\cdot L^{2/3} = MLT^{-2}$, a force.
- Physical sense: at fixed geometry $E \propto \dot{W}^{2/3}$; a hundred times the thrust with a hundred times the area needs $(100)^{3/2}/(100)^{1/2} = 100$ times the power.
- Check against the official key: DA7.pdf gives $\dot{W} = (E/E_e)^{3/2}(A_{se}/A_s)^{1/2}\dot{W}_e = 10^4$ W, the same result.
