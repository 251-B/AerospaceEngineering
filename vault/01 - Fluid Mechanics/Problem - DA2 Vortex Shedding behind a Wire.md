---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - semejanza-fisica
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA2.pdf"
id: "da2"
pill: "DA2: Vortex shedding"
sheets:
  - 2
tags_html:
  - "Π theorem"
  - "Reynolds similarity"
  - "Re ≫ 1"
  - "Experimental table"
---

# Problem DA2: Vortex Shedding behind a Wire

> Official dimensional-analysis sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem with $k = n$ for the critical velocity (Notes.pdf, Eqs. 6.6-6.7), Reynolds similarity between two wires (Eqs. 6.57-6.59) and the limit $\mathrm{Re}\gg 1$ (Eq. 6.51).

## Statement

A wind stream of velocity $U$ flows over a circular wire of radius $R$. It is observed that, when the velocity increases above a critical value $U_c$, the steady flow becomes unstable and it is replaced by a periodic solution characterized by the appearance of vortices of opposite circulation that come off the bottom and top of the cylinder in an alternative fashion, as shown in the figure below.

1. Use the dimensional analysis to reduce the parametric dependence of $U_c$.

![[attachments/FM-T6/da2-statement.svg]]
*Statement figure (redrawn from DA2.pdf): a wind stream of velocity U, density ρ and viscosity μ over a wire of radius R; above the critical velocity the wake becomes a periodic street of vortices of opposite circulation*

The periodic flow that appears for $U > U_c$ causes a periodic force on the cylinder perpendicular to the incident wind stream.

2. Use again the Π theorem to simplify the parametric dependence of the period of the motion $T$ that emerges for $U > U_c$ and of the mean value of the force per unit length acting on the wire, given by its quadratic average value $\bar{F} = \sqrt{\int_0^T F^2(t)\,dt/T}$.

3. Explain how the resulting expressions are simplified for large values of $U$ such that $U \gg \nu/R$, where $\nu$ is the kinematic viscosity of air.

Experiments in a wind tunnel with a wire of radius $R = 1$ mm give $U_c = 0.2$ m/s along with the following values of $T$ and $\bar{F}$ for $U > U_c$:

| $U$ (m/s) | $T$ (ms) | $\bar{F}$ (mN/m) |
| ---: | ---: | ---: |
| 0.2 | 100 | 0 |
| 0.5 | 25 | 0.01 |
| 1 | 10 | 0.12 |
| 2 | 5 | 0.48 |
| 4 | 2.5 | 1.92 |
| 10 | 1 | 12 |
| 20 | 0.5 | 48 |

Use this experimental information to determine, for a wire of radius $R = 2$ mm,

4. The value of $U_c$.

5. The variation of $T$ and $\bar{F}$ with $U$ for $U > U_c$.

6. Obtain the simplified expressions for $T$ and $\bar{F}$ that apply for sufficiently large values of $U$.

Source: DA2.pdf (page 1, statement and handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; limits, Eqs. 6.51 and 6.55; physical similarity, Eqs. 6.57-6.59.

## Hypotheses, Data and Dimensional Table

- Incompressible air of density $\rho$ and viscosity $\mu$; gravity plays no role (no free surface, Notes.pdf, p. 66); the wire is long, so the problem is two-dimensional and the force is taken per unit length.
- The onset of shedding cannot depend on $U$ itself: $U_c$ is the value of $U$ at which it happens, so it depends only on the air and the wire.
- $\bar{F}$ is a root-mean-square force per unit length: $[\bar{F}] = MLT^{-2}/L = MT^{-2}$.

| Quantity | Dimensions |
| :--- | :--- |
| $U$, $U_c$ | $LT^{-1}$ |
| $R$ | $L$ |
| $\rho$ | $ML^{-3}$ |
| $\mu$ | $ML^{-1}T^{-1}$ |
| $T$ (period) | $T$ |
| $\bar{F}$ (per unit length) | $MT^{-2}$ |

## Application of the Π Theorem

### Critical velocity

$$ U_c = U_c(\rho, \mu, R) $$

Rows $\rho$, $\mu$, $R$; columns $L$, $M$, $T$:

$$ \begin{pmatrix} -3 & 1 & 0 \\ -1 & 1 & -1 \\ 1 & 0 & 0 \end{pmatrix}, \qquad \det = 1\cdot\left(1\cdot(-1) - 0\cdot 1\right) = -1 \neq 0 $$

(expanding along the third row). So $k = n = 3$ and no dimensionless parameter is left: $U_c$ divided by the combination with its dimensions is a constant (Notes.pdf, Eqs. 6.6-6.7). With $[U_c] = [\rho]^a[\mu]^b[R]^c$:

$$ M:\; 0 = a + b, \qquad T:\; -1 = -b, \qquad L:\; 1 = -3a - b + c $$

so $b = 1$, $a = -1$ and $c = 1 + 3(-1) + 1 = -1$:

$$ \frac{U_c}{\mu/(\rho R)} = \frac{U_c R}{\nu} = C_1 $$

Shedding starts at a fixed critical Reynolds number.

### Period and force

$$ T = T(\rho, U, \mu, R), \qquad \bar{F} = \bar{F}(\rho, U, \mu, R) $$

$n = 4$; $(\rho, U, R)$ have independent dimensions ($\det$ of rows $U(1,0,-1)$, $R(1,0,0)$, $\rho(-3,1,0)$ is $-1$, as in DA1), so $k = 3$ and one group is left, which is $\mu/(\rho U R) = 1/\mathrm{Re}$ (exponents as for the sphere, Notes.pdf, Eq. 6.33).

**Period.** $[T] = [\rho]^a[U]^b[R]^c$: $M:\; 0 = a$; $T:\; 1 = -b$; $L:\; 0 = -3a + b + c$; so $a = 0$, $b = -1$, $c = 1$, the time scale $R/U$.

**Force.** $[\bar{F}] = MT^{-2} = [\rho]^a[U]^b[R]^c$: $M:\; 1 = a$; $T:\; -2 = -b$; $L:\; 0 = -3a + b + c$; so $a = 1$, $b = 2$, $c = 3 - 2 = 1$, the scale $\rho U^2 R$.

$$ \frac{T}{R/U} = f_T\left(\frac{\rho U R}{\mu}\right), \qquad \frac{\bar{F}}{\rho U^2 R} = f_F\left(\frac{\rho U R}{\mu}\right) $$

### Large velocities

$U \gg \nu/R$ means $\mathrm{Re} = UR/\nu \gg 1$. With $(\rho, U, R)$ as the independent set (the natural choice when viscosity is not dominant, Notes.pdf, p. 68), the dependence on $\mathrm{Re}$ disappears (Notes.pdf, Eq. 6.55):

$$ \frac{T}{R/U} = C_T, \qquad \frac{\bar{F}}{\rho U^2 R} = C_F $$

## Physical Similarity: from the 1 mm Wire to the 2 mm Wire

Both wires are in air (same $\rho$, $\mu$, $\nu$). Subscript 1 is the tested wire ($R_1 = 1$ mm), subscript 2 the new one ($R_2 = 2$ mm).

**Critical velocity.** $U_c R/\nu$ is the same constant for both:

$$ \frac{U_{c1}}{\nu/R_1} = \frac{U_{c2}}{\nu/R_2} \;\Longrightarrow\; U_{c2} = \frac{R_1}{R_2}\,U_{c1} = \frac{1}{2}\times 0.2 = 0.1\ \text{m/s} $$

**Each measured point.** A point of the table describes the 2 mm wire when the Reynolds numbers are equal:

$$ \frac{\rho U_1 R_1}{\mu} = \frac{\rho U_2 R_2}{\mu} \;\Longrightarrow\; U_2 = \frac{R_1}{R_2}\,U_1 = \frac{U_1}{2} $$

Then $T/(R/U)$ and $\bar{F}/(\rho U^2 R)$ are equal:

$$ \frac{T_1}{R_1/U_1} = \frac{T_2}{R_2/U_2} \;\Longrightarrow\; T_2 = \frac{R_2}{R_1}\,\frac{U_1}{U_2}\,T_1 = 2\times 2\times T_1 = 4\,T_1 $$

$$ \frac{\bar{F}_1}{\rho U_1^2 R_1} = \frac{\bar{F}_2}{\rho U_2^2 R_2} \;\Longrightarrow\; \bar{F}_2 = \left(\frac{U_2}{U_1}\right)^2\frac{R_2}{R_1}\,\bar{F}_1 = \frac{1}{4}\times 2\times\bar{F}_1 = \frac{\bar{F}_1}{2} $$

| $U_2$ (m/s) | $T_2$ (ms) | $\bar{F}_2$ (mN/m) |
| ---: | ---: | ---: |
| 0.1 | 400 | 0 |
| 0.25 | 100 | 0.005 |
| 0.5 | 40 | 0.06 |
| 1 | 20 | 0.24 |
| 2 | 10 | 0.96 |
| 5 | 4 | 6 |
| 10 | 2 | 24 |

## Simplified Laws for Large Velocities

The constants come from the measurements in the range where the dimensionless values stop changing. For the 1 mm wire:

| $U$ (m/s) | $T U/R$ | $\bar{F}/(\rho U^2 R)$ |
| ---: | ---: | ---: |
| 0.5 | $25\times 10^{-3}\times 0.5/10^{-3} = 12.5$ | $10^{-5}/(1.2\times 0.25\times 10^{-3}) = 0.033$ |
| 1 | $10\times 10^{-3}\times 1/10^{-3} = 10$ | $1.2\times 10^{-4}/(1.2\times 1\times 10^{-3}) = 0.10$ |
| 4 | $2.5\times 10^{-3}\times 4/10^{-3} = 10$ | $1.92\times 10^{-3}/(1.2\times 16\times 10^{-3}) = 0.10$ |
| 20 | $0.5\times 10^{-3}\times 20/10^{-3} = 10$ | $4.8\times 10^{-2}/(1.2\times 400\times 10^{-3}) = 0.10$ |

(air density $\rho = 1.2$ kg/m$^3$, the value that reproduces the key; the statement does not give it). From $U = 1$ m/s on, both groups are constant:

$$ C_T = \frac{T U}{R} = 10, \qquad C_F = \frac{\bar{F}}{\rho U^2 R} = 0.1 $$

so, for any wire at large $U$:

$$ T = 10\,\frac{R}{U}, \qquad \bar{F} = 0.1\,\rho U^2 R $$

For $R = 2$ mm: $T = 0.02/U$ (s, with $U$ in m/s) and $\bar{F} = 0.1\times 1.2\times 0.002\,U^2 = 2.4\times 10^{-4}\,U^2$ N/m. Check at $U = 10$ m/s: $T = 2$ ms and $\bar{F} = 0.024$ N/m $= 24$ mN/m, the last row of the table above.

## Answers and Checks

- Critical velocity: $U_c R/\nu = C_1$; for $R = 2$ mm, $U_c = 0.1$ m/s.
- Period and force: $T U/R = f_T(\mathrm{Re})$ and $\bar{F}/(\rho U^2 R) = f_F(\mathrm{Re})$; for $R = 2$ mm, $U_2 = U_1/2$, $T_2 = 4T_1$, $\bar{F}_2 = \bar{F}_1/2$ (table above).
- Large $U$: $T = 10\,R/U$, $\bar{F} = 0.1\,\rho U^2 R$.
- Dimensions: $R/U$ is a time; $\rho U^2 R$ is $ML^{-3}\cdot L^2T^{-2}\cdot L = MT^{-2}$, a force per unit length.
- Extension: the group $f/(U/R) = 1/C_T = 0.1$ (frequency $f = 1/T$) is the Strouhal number based on the radius; with the diameter it is $2R/(UT) = 0.2$, the classical value for a circular cylinder.
- Check against the official key: DA2.pdf gives $U_c = 0.1$ m/s, $U_2 = U_1/2$, $T_2 = 4T_1$, $\bar{F}_2 = \bar{F}_1/2$ with the same table, and $C_T = 10$, $C_F = 0.1$.
