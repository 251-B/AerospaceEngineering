---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - energia
  - eyector
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL18.pdf"
---

# Problem CL18: Liquid Ejector: Entrained Flow Rate, Outlet Velocity and Heating

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The ejector shown in the figure of CL18.pdf is used to discharge a container filled with a perfect liquid of density $\rho$ and constant specific heat $c$ into the atmosphere, also at pressure $p_a$. A high-velocity jet of the same liquid, with velocity $U_j$ and cross section $A_j$, is injected along the axis of the discharge pipe, whose cross section is $A$. The jet entrains fluid as it develops, producing an underpressure at the injection section and drawing the fluid from the container. Mixing of the jet with the surrounding liquid is completed downstream, so that at the outlet the liquid discharges as a uniform jet with velocity $U_o$. For a given the geometry (i.e., given values of $A_j$ and $A$), we want to compute the characteristics of the flow in terms of the injection velocity $U_j$. In the computation, assume that the effect of gravity is negligible. Address in order the following questions:

- Assuming that the acceleration of the fluid upstream from the injector is steady and inviscid, write down the equation that relates the ambient pressure $p_a$ with the velocity and pressure at the entrance of the pipe, $U_e$ and $p_e$.
- Apply the continuity and momentum balance equations to the control volume indicated in the figure. Simplify the result by assuming that the effect of friction on the wall surface is negligibly small.
- Use the previous equations to show that the volumetric discharge flow rate is given by $Q = U_e(A - A_j) = \dfrac{U_j(A - A_j)}{1 + A/\sqrt{2A_j(A - A_j)}}$ and that the velocity at the outlet satisfies $\dfrac{U_o}{U_j} = \dfrac{A_j + \sqrt{2A_j(A - A_j)}}{A + \sqrt{2A_j(A - A_j)}}$.
- Assuming that the values of the temperatures $T_e$ and $T_j$ at the entrance section are equal to the ambient value $T_a$, obtain the temperature $T_o$ at the outlet section when the pipe walls are adiabatic.

![[attachments/FM-T3/cl18-statement.svg]]
*Statement figure (redrawn from CL18.pdf, p. 1): container at $p_a$, pipe of section $A$; jet $A_j$, $U_j$ injected on the axis; entrance section with $U_e$, $p_e$ around the jet; control volume $V_c$ with outward normals; uniform outlet jet $U_o$ into $p_a$*

Source: CL18.pdf (page 1, midterm of Nov 11, 2013). Notes.pdf: Bernoulli's equation Eq. 4.17, integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, incompressible liquid, $e = cT$; neglect $\bar{g}$; friction on the pipe wall negligible; adiabatic walls.
- Entrance section (area $A$): the jet ($A_j$, $U_j$) and the entrained liquid (annulus $A - A_j$, $U_e$) are both at the pressure $p_e$ (parallel streams). Outlet: uniform $U_o$ at $p_a$ (complete mixing).
- Data: $[\rho,\ c,\ A,\ A_j,\ U_j,\ p_a,\ T_a]$. Unknowns: $[U_e,\ p_e,\ U_o,\ Q,\ T_o]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $A$, $A_j$ | pipe and jet areas | m$^2$ |
| $U_j$, $U_e$, $U_o$ | jet, entrained and outlet velocities | m/s |
| $p_e$ | pressure at the entrance section | Pa |
| $Q$ | entrained volume flow rate | m$^3$/s |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the pipe; $\bar{e}_x$ along the pipe axis in the flow direction. Fixed control volume between the entrance and the outlet sections.
- Surfaces: $\Sigma_e$ (entrance, $\bar{n} = -\bar{e}_x$, split into the jet $A_j$ and the annulus $A - A_j$), $\Sigma_o$ (outlet, $\bar{n} = +\bar{e}_x$), $\Sigma_w$ (straight pipe wall, $\bar{n}\perp\bar{e}_x$).

![[attachments/FM-T3/cl18-cv.svg]]
*Control volume of the solution: $\Sigma_e$ (entrance, $\bar{n} = -\bar{e}_x$, made of the jet $A_j$ and the annulus $A - A_j$), $\Sigma_o$ (outlet, $\bar{n} = +\bar{e}_x$) and the straight wall $\Sigma_w$ ($\bar{n}\perp\bar{e}_x$); $\bar{e}_x$ points along the flow*

## Phase 3: Balances, Surface by Surface

### 1. Bernoulli upstream of the entrance

From the still liquid of the container (at $p_a$) to the entrance (Notes Eq. 4.17):

$$ \boxed{\,p_a = p_e + \tfrac{1}{2}\rho U_e^2\,} \tag{1} $$

**2. Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_e\ (\text{annulus})$ | $-\rho U_e(A - A_j)$ |
| $\Sigma_e\ (\text{jet})$ | $-\rho U_jA_j$ |
| $\Sigma_o$ | $+\rho U_oA$ |
| $\Sigma_w$ | $0$ |

$$ \boxed{\,U_oA = U_e(A - A_j) + U_jA_j\,} \tag{2} $$

**2. Linear momentum, x component (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho v_x\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(p - p_a)\,n_x\,d\sigma$ | $\int(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_e\ (\text{annulus})$ | $-\rho U_e^2(A - A_j)$ | $(p_e - p_a)(A - A_j)$ | $0$ |
| $\Sigma_e\ (\text{jet})$ | $-\rho U_j^2A_j$ | $(p_e - p_a)A_j$ | $0$ |
| $\Sigma_o$ | $+\rho U_o^2A$ | $0$ ($p = p_a$) | $0$ |
| $\Sigma_w$ | $0$ | $0$ ($n_x = 0$) | $0$ (friction neglected) |

With (1), $(p_e - p_a)A = -\tfrac{1}{2}\rho U_e^2A$.

$$ \boxed{\,U_o^2A = U_e^2\left(\frac{A}{2} - A_j\right) + U_j^2A_j\,} \tag{3} $$

### 3. Flow rate and outlet velocity

Squaring (2) and dividing by $A$, then equating to (3):

$$ \left[U_e(A - A_j) + U_jA_j\right]^2 = A\left[U_e^2\left(\frac{A}{2} - A_j\right) + U_j^2A_j\right]. $$

Expanding, $U_e^2\left[(A - A_j)^2 - \frac{A^2}{2} + AA_j\right] + 2U_eU_jA_j(A - A_j) + U_j^2(A_j^2 - AA_j) = 0$. With $k = A_j(A - A_j)$ and $x = U_e/U_j$, the bracket is $\frac{A^2}{2} - k$ and the equation reads

$$ \left(\frac{A^2}{2} - k\right)x^2 + 2kx - k = 0 \;\Longrightarrow\; x = \frac{-k \pm \sqrt{k^2 + k\left(\frac{A^2}{2} - k\right)}}{\frac{A^2}{2} - k} = \frac{-k \pm \frac{As}{2}}{\frac{(A - s)(A + s)}{2}},\qquad s \equiv \sqrt{2k} = \sqrt{2A_j(A - A_j)}. $$

The $+$ sign gives $x = \frac{s(A - s)}{(A - s)(A + s)} = \frac{s}{A + s}$; the $-$ sign gives $x = -\frac{s}{A - s} < 0$ (liquid flowing back into the container, rejected). Hence

$$ \frac{U_e}{U_j} = \frac{1}{1 + A/\sqrt{2A_j(A - A_j)}},\qquad \boxed{\,Q = U_e(A - A_j) = \frac{U_j(A - A_j)}{1 + A/\sqrt{2A_j(A - A_j)}}\,} \tag{4} $$

and from (2), $\frac{U_o}{U_j} = \frac{x(A - A_j) + A_j}{A} = \frac{s(A - A_j) + A_j(s + A)}{A(A + s)} = \frac{sA + A_jA}{A(A + s)}$:

$$ \boxed{\,\frac{U_o}{U_j} = \frac{A_j + \sqrt{2A_j(A - A_j)}}{A + \sqrt{2A_j(A - A_j)}}\,} \tag{5} $$

**4. Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_e\ (\text{annulus})$ | $-\rho U_e(A - A_j)\left(cT_e + \tfrac{U_e^2}{2}\right)$ | $+p_eU_e(A - A_j)$ | $0$ | $0$ |
| $\Sigma_e\ (\text{jet})$ | $-\rho U_jA_j\left(cT_j + \tfrac{U_j^2}{2}\right)$ | $+p_eU_jA_j$ | $0$ | $0$ |
| $\Sigma_o$ | $+\rho U_oA\left(cT_o + \tfrac{U_o^2}{2}\right)$ | $-p_aU_oA$ | $0$ | $0$ |
| $\Sigma_w$ | $0$ | $0$ | $0$ | $0$ (adiabatic) |

Pressure work: by (2) and (1), $p_e[U_e(A - A_j) + U_jA_j] - p_aU_oA = (p_e - p_a)U_oA = -\tfrac{1}{2}\rho U_e^2U_oA$. With $T_e = T_j = T_a$ the internal-energy terms give $\rho cU_oA(T_o - T_a)$; using $U_e(A - A_j) = U_oA - U_jA_j$ and dividing by $\rho U_oAU_j^2$:

$$ \boxed{\,\frac{c\,(T_o - T_a)}{U_j^2} = \frac{U_jA_j}{2U_oA}\left[1 - \left(\frac{U_e}{U_j}\right)^2\right] - \frac{1}{2}\left(\frac{U_o}{U_j}\right)^2\,} \tag{6} $$

> [!warning] Erratum in the official solution
> CL18.pdf writes the energy balance as in the table but boxes $\frac{c(T_o - T_a)}{U_j^2} = \frac{U_jA_j}{U_oA}\left[1 - \left(\frac{U_e}{U_j}\right)^2\right] - \left(\frac{U_o}{U_j}\right)^2$, without the two factors $\tfrac{1}{2}$ (all kinetic energies are $U^2/2$), i.e. twice the value of (6). Check: for $A = 1$ m$^2$, $A_j = 0.1$ m$^2$, $U_j = 10$ m/s, $c = 4186$ J/(kg K), the residual of the energy balance (per unit density) is $0$ with (6) and $20.6$ W/(kg/m$^3$) with the boxed expression. The computed value is kept.

## Phase 4: Interpretation, Limits and Dimensional Check

- $T_o > T_a$: the mixing of the fast jet with the slow entrained liquid dissipates kinetic energy, which appears as heat. The rise is tiny for a liquid ($c$ is large).
- Limit $A_j \to 0$: $s \to 0$, $Q \to 0$ and $U_o \to 0$ (no jet, no pumping). Limit $A_j \to A$: $s \to 0$, $Q \to 0$ and $U_o \to U_j$ (the jet fills the pipe).
- Dimensions (SI): $[Q] = (\text{m/s})\,\text{m}^2 = \text{m}^3/\text{s}$; $[cT/U^2] = 1$.
- Numerical illustration (hypothetical data): $A = 1$ m$^2$, $A_j = 0.1$ m$^2$, $U_j = 10$ m/s, water ($c = 4186$ J/(kg K)) give $U_e = 2.9788$ m/s, $Q = 2.6809$ m$^3$/s, $U_o = 3.6809$ m/s and $T_o - T_a = 1.339$ mK; the residuals of (2) and (3) are below $10^{-14}$.
- Agreement with the official solution: (1) to (5) as in CL18.pdf; (6) differs by the factors $\tfrac{1}{2}$ discussed above.
