---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - semejanza-fisica
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA10.pdf"
id: "da10"
pill: "DA10: Belt pump"
sheets:
  - 10
tags_html:
  - "Π theorem"
  - "Re ≪ 1"
  - "Calibration table"
---

# Problem DA10: Two-Belt Viscous Pump

> Official dimensional-analysis sheet of the course (exam of Dec 18, 2012), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem with $\mu$ in the independent set (Notes.pdf, p. 68), the limit of negligible inertia (Eq. 6.55) and similarity between two liquids in the same pump (Eqs. 6.57-6.59).

## Statement

**PROBLEM 3 (50 minutes)** The system sketched in the figure is designed to steadily pump fluid of constant density $\rho$ and constant viscosity $\mu$ from a reservoir, where the modified pressure has a constant value $P_0$, to another one at pressure $P_0 + \Delta P$ ($\Delta P > 0$). To that end, a pair of parallel belts of length $L$, separated by a distance $h \ll L$, are driven at constant velocities $V_l$ and $V_u$, dragging the liquid towards the large pressure reservoir.

In the forthcoming analysis, the liquid flow can be assumed steady and two-dimensional (spanwise length much larger than $h$). The most important parameters of the system are the liquid volume flux **per unit spanwise length**, $q$, the power needed to drive the system **per unit spanwise length**, $\dot{W}$, and the pump efficiency, $\eta = q\Delta P/\dot{W}$.

![[attachments/FM-T6/da10-statement.svg]]
*Statement figure (redrawn from DA10.pdf): two parallel belts of length L, a distance h ≪ L apart, driven at V_u and V_l, drag liquid of density ρ and viscosity μ from a reservoir at reduced pressure P_0 to one at P_0 + ΔP*

1. (*3 points*). Use dimensional analysis to simplify the dependence of $q$, $\dot{W}$ and $\eta$, as functions of an appropriately chosen set of parameters governing the operation of the pump.

2. (*2 points*). Simplify the resulting dimensionless functions when the inertia of the fluid can be neglected compared to the viscous forces. Note that, in this limit, the fluid density plays a negligible role. In the remainder of the problem, assume that these conditions are satisfied.

A pump with $h = 1$ cm and $L = 20$ cm is calibrated using glycerol, of density $\rho_g = 1260$ kg/m$^3$ and viscosity $\mu_g = 1.41$ kg/(m s), using an overpressure $\Delta P_g = 1$ kPa. During the calibration process, the lower belt is kept at rest, $V_{l,g} = 0$, while the upper belt is driven at several velocities $V_{u,g}$, as indicated in the table below, where the corresponding values of $q_g$, $\dot{W}_g$ and $\eta_g$ are also shown.

| $V_{u,g}$ (cm/s) | $q_g$ (cm$^2$/s) | $\dot{W}_g$ (Watt/m) | $\eta_g$ |
| ---: | ---: | ---: | ---: |
| 10 | 2 | 0.8 | 0.26 |
| 15 | 4.5 | 1.4 | 0.33 |
| 20 | 7 | 2.1 | 0.33 |
| 25 | 9.5 | 3 | 0.32 |
| 30 | 12 | 4 | 0.3 |
| 35 | 14.5 | 5.2 | 0.28 |

The **same pump** is used to deliver a silicone oil, of density $\rho_{oil} = 1100$ kg m$^{-3}$ and viscosity $\mu_{oil} = 5$ kg/(m s), with an overpressure $\Delta P_{oil} = 2$ kPa.

3. (*2 points*). Determine the velocities $V_{l,oil}$ and $V_{u,oil}$ for which the results obtained in the calibration tests can be used to predict the pumping behavior with the silicone oil.

4. (*2 points*). Calculate the corresponding values of $q_{oil}$, $\dot{W}_{oil}$ and $\eta_{oil}$.

5. (*1 point*). Discuss the hypothesis of negligible fluid inertia.

Source: DA10.pdf (page 1: statement; page 2: handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; selection of parameters, p. 68; limits, Eq. 6.55; physical similarity, Eqs. 6.57-6.59.

## Hypotheses, Data and Dimensional Table

- Steady, two-dimensional flow of a liquid with constant $\rho$ and $\mu$; gravity is absorbed in the modified pressure, so only the difference $\Delta P$ enters (Notes.pdf, p. 66).
- All quantities are per unit spanwise length: $[q] = L^2T^{-1}$, $[\dot{W}] = ML^2T^{-3}/L = MLT^{-3}$.
- Recomputing $\eta = q\Delta P/\dot{W}$ from the table: row 1 gives $2\times 10^{-4}\times 10^{3}/0.8 = 0.25$ (printed 0.26) and row 2 gives $4.5\times 10^{-4}\times 10^{3}/1.4 = 0.32$ (printed 0.33); rows 3 to 6 agree with the printed values (0.333, 0.317, 0.300, 0.279).

| Parameter | Dimensions |
| :--- | :--- |
| $q$ | $L^2T^{-1}$ |
| $\dot{W}$ | $MLT^{-3}$ |
| $\eta$ | 1 |
| $\rho$ | $ML^{-3}$ |
| $\mu$ | $ML^{-1}T^{-1}$ |
| $\Delta P$ | $ML^{-1}T^{-2}$ |
| $V_u$, $V_l$ | $LT^{-1}$ |
| $L$, $h$ | $L$ |

## Application of the Π Theorem

$$ q = f_1(\rho, \mu, \Delta P, V_u, V_l, L, h), \qquad \dot{W} = f_2(\dots), \qquad \eta = f_3(\dots) $$

$n = 7$. The key takes $(\mu, V_u, h)$, natural for a viscous pump. Rows $\mu(-1, 1, -1)$, $V_u(1, 0, -1)$, $h(1, 0, 0)$ in $(L, M, T)$; only $\mu$ has mass, so expanding along the $M$ column, $\det = -1\cdot\left(1\cdot 0 - (-1)\cdot 1\right) = -1 \neq 0$: $k = 3$, and $n - k = 4$ groups remain.

**Flux.** $[q] = [\mu]^a[V_u]^b[h]^c$: $M:\; 0 = a$; $T:\; -1 = -b$; $L:\; 2 = b + c$; so the scale is $V_u h$.

**Power.** $[\dot{W}] = [\mu]^a[V_u]^b[h]^c$: $M:\; 1 = a$; $T:\; -3 = -a - b$, $b = 2$; $L:\; 1 = -a + b + c$, $c = 0$; so the scale is $\mu V_u^2$.

**Density.** $[\rho] = [\mu]^a[V_u]^b[h]^c$: $M:\; 1 = a$; $T:\; 0 = -1 - b$, $b = -1$; $L:\; -3 = -1 - 1 + c$, $c = -1$: the group $\rho V_u h/\mu$, a Reynolds number.

**Pressure.** $[\Delta P] = [\mu]^a[V_u]^b[h]^c$: $M:\; 1 = a$; $T:\; -2 = -1 - b$, $b = 1$; $L:\; -1 = -1 + 1 + c$, $c = -1$: the group $h\Delta P/(\mu V_u)$.

**Belts and geometry.** $V_l/V_u$ and $L/h$.

$$ \frac{q}{V_u h} = \Pi_q\left(\frac{\rho V_u h}{\mu}, \frac{h\Delta P}{\mu V_u}, \frac{V_l}{V_u}, \frac{L}{h}\right), \quad \frac{\dot{W}}{\mu V_u^2} = \Pi_W(\dots), \quad \eta = \eta(\dots) $$

with the same four arguments.

## Negligible Inertia

When inertia is negligible against viscous forces, the density drops out ($\rho V_u h/\mu \to 0$; Notes.pdf, Eq. 6.55):

$$ \frac{q}{V_u h} = \Pi_q\left(\frac{h\Delta P}{\mu V_u}, \frac{V_l}{V_u}, \frac{L}{h}\right), \quad \frac{\dot{W}}{\mu V_u^2} = \Pi_W\left(\frac{h\Delta P}{\mu V_u}, \frac{V_l}{V_u}, \frac{L}{h}\right), \quad \eta = \eta\left(\frac{h\Delta P}{\mu V_u}, \frac{V_l}{V_u}, \frac{L}{h}\right) $$

## Physical Similarity: from Glycerol to Silicone Oil

The pump is the same, so $L/h$ is the same. The other two groups must be equal.

**Lower belt.**

$$ \frac{V_{l,oil}}{V_{u,oil}} = \frac{V_{l,g}}{V_{u,g}} = 0 \;\Longrightarrow\; V_{l,oil} = 0 $$

**Upper belt.** The same $h$ cancels:

$$ \frac{h\Delta P_{oil}}{\mu_{oil}V_{u,oil}} = \frac{h\Delta P_g}{\mu_g V_{u,g}} \;\Longrightarrow\; \frac{V_{u,oil}}{V_{u,g}} = \frac{\mu_g}{\mu_{oil}}\,\frac{\Delta P_{oil}}{\Delta P_g} = \frac{1.41}{5}\times\frac{2}{1} = 0.564 $$

## Oil Performance

With all groups equal, the dimensionless outputs are equal:

$$ \frac{q_{oil}}{V_{u,oil}h} = \frac{q_g}{V_{u,g}h} \;\Longrightarrow\; \frac{q_{oil}}{q_g} = \frac{V_{u,oil}}{V_{u,g}} = 0.564 $$

$$ \frac{\dot{W}_{oil}}{\mu_{oil}V_{u,oil}^2} = \frac{\dot{W}_g}{\mu_g V_{u,g}^2} \;\Longrightarrow\; \frac{\dot{W}_{oil}}{\dot{W}_g} = \frac{\mu_{oil}}{\mu_g}\left(\frac{V_{u,oil}}{V_{u,g}}\right)^2 = \frac{5}{1.41}\times 0.564^2 = 3.546\times 0.3181 = 1.128 $$

$$ \eta_{oil} = \eta_g $$

Check: $\eta_{oil}/\eta_g = (q_{oil}/q_g)(\Delta P_{oil}/\Delta P_g)/(\dot{W}_{oil}/\dot{W}_g) = 0.564\times 2/1.128 = 1$. The $\eta_{oil}$ column copies the printed $\eta_g$, as the key does; from $q\Delta P/\dot{W}$ the first two rows would read 0.25 and 0.32.

| $V_{u,g}$ (cm/s) | $V_{u,oil}$ (cm/s) | $q_{oil}$ (cm$^2$/s) | $\dot{W}_{oil}$ (W/m) | $\eta_{oil}$ |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 5.64 | 1.128 | 0.902 | 0.26 |
| 15 | 8.46 | 2.538 | 1.579 | 0.33 |
| 20 | 11.28 | 3.948 | 2.369 | 0.33 |
| 25 | 14.10 | 5.358 | 3.384 | 0.32 |
| 30 | 16.92 | 6.768 | 4.512 | 0.30 |
| 35 | 19.74 | 8.178 | 5.866 | 0.28 |

## Negligible Inertia: Discussion

The plain Reynolds number of the calibration is not small: $\rho_g V_{u,g}h/\mu_g = 1260\times 0.10\times 0.01/1.41 = 0.89$ at the lowest speed and $3.1$ at the highest. The key compares inertia and viscosity in the **slender** channel ($h \ll L$), where the convective term is smaller than the viscous one by the extra factor $h/L$, so the relevant number is the reduced Reynolds number $(\rho V_u h/\mu)(h/L)$. This criterion belongs to the slender viscous flows of Chapter 7 of the notes (an **extension** here). With $h/L = 1/20$:

$$ \text{glycerol: } 0.89\times\frac{1}{20} = 0.045 \;\le\; \frac{\rho_g V_{u,g}h}{\mu_g}\,\frac{h}{L} \;\le\; 3.13\times\frac{1}{20} = 0.156 $$

$$ \text{oil: } \frac{1100\times 0.0564\times 0.01}{5}\times\frac{1}{20} = 0.0062 \;\le\; \frac{\rho_{oil}V_{u,oil}h}{\mu_{oil}}\,\frac{h}{L} \;\le\; \frac{1100\times 0.1974\times 0.01}{5}\times\frac{1}{20} = 0.022 $$

Both are small, more so for the oil, so neglecting inertia is a good approximation, and the calibration can be transferred to the oil.

## Answers and Checks

- Reduced laws: $q/(V_uh)$, $\dot{W}/(\mu V_u^2)$ and $\eta$ are functions of $\rho V_uh/\mu$, $h\Delta P/(\mu V_u)$, $V_l/V_u$, $L/h$; without inertia, of the last three only.
- Similar operation with oil: $V_{l,oil} = 0$, $V_{u,oil} = 0.564\,V_{u,g}$.
- Oil performance: $q_{oil} = 0.564\,q_g$, $\dot{W}_{oil} = 1.128\,\dot{W}_g$, $\eta_{oil} = \eta_g$ (table above).
- Inertia: reduced Reynolds number 0.045-0.156 (glycerol) and 0.006-0.022 (oil).
- Dimensions: $\mu V_u^2$ is $ML^{-1}T^{-1}\cdot L^2T^{-2} = MLT^{-3}$, a power per unit length; $h\Delta P/(\mu V_u)$ is $L\cdot ML^{-1}T^{-2}/(ML^{-1}T^{-1}\cdot LT^{-1}) = 1$.
- Check against the official key: DA10.pdf gives $V_{l,oil} = 0$, $V_{u,oil}/V_{u,g} = 0.564$, $q_{oil}/q_g = 0.564$, $\dot{W}_{oil}/\dot{W}_g = 1.128$ and the same table, with the inertia ranges 0.045-0.156 and 0.0062-0.022.
