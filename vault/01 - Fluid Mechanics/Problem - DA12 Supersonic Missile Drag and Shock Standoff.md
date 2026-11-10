---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - semejanza-fisica
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA12.pdf"
id: "da12"
pill: "DA12: Supersonic missile"
sheets:
  - 12
tags_html:
  - "Π theorem"
  - "Mach similarity"
  - "Order of magnitude"
  - "Hypersonic limit"
---

# Problem DA12: Supersonic Missile Drag and Shock Standoff

> Official dimensional-analysis sheet of the course (prefinal exam of Dec 16, 2013), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem (Notes.pdf, Eq. 6.25), order-of-magnitude analysis of the momentum equation (Eqs. 6.45-6.46), Mach similarity (Eqs. 6.57-6.59) and the limit $U/c \gg 1$ (Eq. 6.55).

## Statement

A nuclear missile is designed to fly at supersonic speeds (velocities $U$ larger than the sound velocity $c$) at high altitudes. In the solution that appears, a bow shock is present at a standoff distance $d$ from the missile tip. To characterize the solution and determine the drag force $F$ acting on the missile, a series of experiments is conducted in a supersonic wind tunnel using a small experimental model geometrically similar to the real prototype. Analyze the results following these steps:

1. Use the Π theorem to reduce the parametric dependence of the drag $F$ and standoff distance $d$. To set up the problem, note that the compressibility of the gas is characterized by the ambient sound speed $c$, which should be considered at the start of the analysis, along with the ambient values of the density and viscosity of the gas $\rho$ and $\mu$. Since the density changes across the shock, gravity might also influence the solution through the resulting buoyant force.

2. Derive the conditions under which both gravity and viscosity do not influence the solution. The reasoning should be substantiated with an order-of-magnitude analysis of the momentum equation to show clearly which dimensionless parameters measure the relative importance of buoyant and viscous forces (relative to the convective acceleration).

3. The experimental tests are carried out at normal ambient conditions ($\rho_e = 1.22$ kg/m$^3$, $\mu_e = 1.98\times 10^{-5}$ kg/(m s), $c_e = 340$ m/s) with a model of diameter $D_e = 0.01$ m, significantly smaller than that of the real missile ($D_m = 1$ m), giving the results shown in the table. Use the results, together with the assumption that $g$ and $\mu$ have a negligible influence, to deduce the variation with flight speed $U_m$ of the drag force $F_m$ and standoff distance $d_m$ corresponding to the missile flying at cruise altitude, where $\rho_m = 0.36$ kg/m$^3$, $\mu_m = 1.44\times 10^{-5}$ kg/(m s), and $c_m = 295$ m/s.

4. Check that the criteria needed to neglect $g$ and $\mu$ are satisfied both in the experiment and for the real missile conditions.

5. Determine a simplified expression for the drag force when the Mach number is very large (i.e., $U/c \gg 1$).

| $U_e$ (m/s) | $F_e$ (N) | $d_e$ (m) |
| ---: | ---: | ---: |
| 400 | 9.2 | 0.012 |
| 700 | 37.50 | 0.01 |
| 1,000 | 86.00 | 0.005 |
| 2,000 | 383 | 0 |
| 4,000 | 1532 | 0 |

![[attachments/FM-T6/da12-statement.svg]]
*Statement figure (redrawn from DA12.pdf, frame of the missile): a gas of density ρ, viscosity μ and sound speed c meets the missile of diameter D at a speed U > c; a bow shock stands at a distance d ahead of the tip*

Source: DA12.pdf (page 1, prefinal exam of Dec 16, 2013, statement and handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; order of magnitude, Eqs. 6.45-6.46; limits, Eq. 6.55; physical similarity, Eqs. 6.57-6.59.

## Hypotheses, Data and Dimensional Table

- In the frame of the missile the gas arrives at $U$ with its ambient $\rho$, $\mu$, $c$; gravity is kept at first, as the statement asks, because the density jump across the shock creates a buoyant force.
- The model is geometrically similar; the subscript $m$ is the missile (prototype), $e$ the experiment.

| Parameter | Dimensions |
| :--- | :--- |
| $F$ (unknown) | $MLT^{-2}$ |
| $d$ (unknown) | $L$ |
| $D$ | $L$ |
| $U$, $c$ | $LT^{-1}$ |
| $\rho$ | $ML^{-3}$ |
| $\mu$ | $ML^{-1}T^{-1}$ |
| $g$ | $LT^{-2}$ |

## Application of the Π Theorem

$$ F = F(D, U, \rho, \mu, c, g), \qquad d = d(D, U, \rho, \mu, c, g) $$

$n = 6$; $(\rho, U, D)$ have independent dimensions ($\det = -1$, as in DA1), so three groups remain.

- **Drag:** $[F] = [\rho][U]^2[D]^2$ (exponents as for the sphere, Notes.pdf, Eq. 6.32): $F/(\rho U^2D^2)$.
- **Standoff:** $d/D$.
- **Viscosity:** $\rho UD/\mu$ (Reynolds). **Gravity:** $[g] = [U]^2[D]^{-1}$ (as in DA1): $U^2/(gD)$ (Froude squared). **Compressibility:** $U/c$ (Mach).

$$ \frac{F}{\rho U^2D^2} = f_1\left(\frac{\rho UD}{\mu}, \frac{U^2}{gD}, \frac{U}{c}\right), \qquad \frac{d}{D} = f_2\left(\frac{\rho UD}{\mu}, \frac{U^2}{gD}, \frac{U}{c}\right) $$

## Order of Magnitude: When Gravity and Viscosity Do Not Matter

Velocities are of order $U$ and change by $O(U)$ over distances $O(D)$, as in Notes.pdf, Eq. 6.45. The convective acceleration, the viscous force and the buoyant force per unit volume are then

$$ O(\rho\,\bar{v}\cdot\nabla\bar{v}) \sim \frac{\rho U^2}{D}, \qquad O(\mu\nabla^2\bar{v}) \sim \frac{\mu U}{D^2}, \qquad O(\Delta\rho\,g) \sim \rho g $$

where the density change across a strong shock is of the order of $\rho$ itself. The two ratios to the convective term are

$$ \frac{O(\rho\,\bar{v}\cdot\nabla\bar{v})}{O(\mu\nabla^2\bar{v})} = \frac{\rho U^2/D}{\mu U/D^2} = \frac{\rho UD}{\mu}, \qquad \frac{O(\rho\,\bar{v}\cdot\nabla\bar{v})}{O(\rho g)} = \frac{\rho U^2/D}{\rho g} = \frac{U^2}{gD} $$

So viscosity is negligible if $\rho UD/\mu \gg 1$, and gravity if $U^2/(gD) \gg 1$. Then (Notes.pdf, Eq. 6.55)

$$ \frac{F}{\rho U^2D^2} = f_1\left(\frac{U}{c}\right), \qquad \frac{d}{D} = f_2\left(\frac{U}{c}\right) $$

## Mach Similarity: from the Tunnel to the Missile

Each tunnel point is similar to the flight state with the same Mach number:

$$ \frac{U_m}{c_m} = \frac{U_e}{c_e} \;\Longrightarrow\; U_m = \frac{c_m}{c_e}\,U_e = \frac{295}{340}\,U_e = 0.8676\,U_e $$

and then

$$ \frac{F_m}{\rho_mU_m^2D_m^2} = \frac{F_e}{\rho_eU_e^2D_e^2} \;\Longrightarrow\; F_m = \frac{\rho_m}{\rho_e}\left(\frac{U_m}{U_e}\right)^2\left(\frac{D_m}{D_e}\right)^2F_e = \frac{0.36}{1.22}\times 0.7528\times 10^{4}\,F_e = 2221\,F_e $$

$$ \frac{d_m}{D_m} = \frac{d_e}{D_e} \;\Longrightarrow\; d_m = \frac{D_m}{D_e}\,d_e = 100\,d_e $$

| $U_e$ (m/s) | $U_m$ (m/s) | $F_m$ (N) | $d_m$ (m) |
| ---: | ---: | ---: | ---: |
| 400 | 347 | $2.04\times 10^{4}$ | 1.2 |
| 700 | 607 | $8.33\times 10^{4}$ | 1.0 |
| 1000 | 868 | $1.91\times 10^{5}$ | 0.5 |
| 2000 | 1735 | $8.51\times 10^{5}$ | 0 |
| 4000 | 3471 | $3.40\times 10^{6}$ | 0 |

> [!warning] Discrepancy with the official solution
> The key writes $F_m = 1.91\times 10^{4}$ N in the third row; $2221\times 86 = 1.91\times 10^{5}$ N, and the drag must grow between the second row ($8.33\times 10^{4}$ N) and the fourth ($8.5\times 10^{5}$ N), so the exponent of the key is a slip: the value is $1.91\times 10^{5}$ N.

## Check of the Criteria

The groups are smallest at the lowest speed of each series:

$$ \left(\frac{\rho_eU_eD_e}{\mu_e}\right)_{min} = \frac{1.22\times 400\times 0.01}{1.98\times 10^{-5}} = 2.46\times 10^{5} \gg 1, \qquad \left(\frac{\rho_mU_mD_m}{\mu_m}\right)_{min} = \frac{0.36\times 347\times 1}{1.44\times 10^{-5}} = 8.68\times 10^{6} \gg 1 $$

$$ \left(\frac{U_e^2}{gD_e}\right)_{min} = \frac{400^2}{9.81\times 0.01} = 1.63\times 10^{6} \gg 1, \qquad \left(\frac{U_m^2}{gD_m}\right)_{min} = \frac{347^2}{9.81\times 1} = 1.23\times 10^{4} \gg 1 $$

All four are very large: gravity and viscosity can be neglected in the tunnel and in flight.

## Hypersonic Limit

For $U/c \gg 1$ the Mach number stops influencing the drag coefficient (Notes.pdf, Eq. 6.55):

$$ \frac{F}{\rho U^2D^2} = C $$

The tunnel data give $C$:

| $U_e/c_e$ | $F_e/(\rho_eU_e^2D_e^2)$ |
| ---: | ---: |
| 1.18 | $9.2/(1.22\times 1.6\times 10^{5}\times 10^{-4}) = 0.471$ |
| 2.06 | $37.5/(1.22\times 4.9\times 10^{5}\times 10^{-4}) = 0.627$ |
| 2.94 | $86/(1.22\times 10^{6}\times 10^{-4}) = 0.705$ |
| 5.88 | $383/(1.22\times 4\times 10^{6}\times 10^{-4}) = 0.785$ |
| 11.8 | $1532/(1.22\times 1.6\times 10^{7}\times 10^{-4}) = 0.785$ |

The last two Mach numbers give the same value, so $C \simeq 0.785$ and

$$ F \simeq 0.785\,\rho U^2D^2 \qquad (U/c \gg 1) $$

## Answers and Checks

- Reduced laws: $F/(\rho U^2D^2)$ and $d/D$ are functions of $\rho UD/\mu$, $U^2/(gD)$ and $U/c$.
- Viscosity and gravity are negligible for $\rho UD/\mu \gg 1$ and $U^2/(gD) \gg 1$; then both depend on $U/c$ only.
- Missile: $U_m = 0.868\,U_e$, $F_m = 2221\,F_e$, $d_m = 100\,d_e$ (table above).
- Criteria: Reynolds $\ge 2.4\times 10^5$ and Froude squared $\ge 1.2\times 10^4$ in both systems.
- Hypersonic drag: $F \simeq 0.785\,\rho U^2D^2$.
- Dimensions: $\rho U^2D^2$ is $ML^{-3}\cdot L^2T^{-2}\cdot L^2 = MLT^{-2}$, a force.
- Physical sense: as the Mach number grows the shock moves closer to the tip ($d \to 0$ from $U_e = 2000$ m/s on) and the drag coefficient levels off, the behaviour predicted by (6.55).
- Check against the official key: DA12.pdf gives the same groups, $U_m = (c_m/c_e)U_e$, the same table (with the slip of the third force corrected above), the criteria $2.46\times 10^5$, $8.67\times 10^6$, $1.63\times 10^6$, $1.23\times 10^4$ and $C \simeq 0.785$.
