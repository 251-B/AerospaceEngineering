---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - energia
  - turborreactor
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL5.pdf"
---

# Problem CL5: Turbojet on a Testbench: Exit State

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].

## Statement

The entrance and exit sections of the turboreactor sketched in the figure of CL5.pdf have areas $A_1$ and $A_2$. Besides the outer fixed frame, the machine has mobile parts in its interior that extract an amount of work $W$ per unit time from the fluid stream. The combined effects of chemical reaction in the combustion chamber and heat transfer through the walls give a heat transfer per unit time $Q$ to the fluid stream. The axial force on the turboreactor measured on the testbench is $\mathbf{F} = -F\,\mathbf{e}_x$. For given values of $W$, $Q$ and $F$ and assuming that at the entrance and exit sections the flow properties are uniform, obtain the values of the density $\rho_2$, pressure $p_2$ and velocity $v_2$ in terms of their values $p_1$, $\rho_1$ and $v_1$ at the entrance. (Handwritten addition: no gravity.)

Source: CL5.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eq. 3.10, integral momentum balance Eq. 3.35, integral total energy balance Eq. 3.46, force on a body Eq. 3.32.

## Phase 1: Hypotheses, Degrees of Freedom and Data

- The gas is a perfect gas with specific heat ratio $\gamma$ ($h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$), as used in the official solution. Flow properties are uniform over the entrance and exit sections; viscous stresses and conduction are negligible there. No gravity (handwritten addition).
- The flow is steady on average: the rotating parts make it periodic in time at fixed points inside the engine, but through the sections it is steady, so the net accumulation inside the control volume is zero.
- The fuel mass flow is not given and is neglected, so the mass flow at the exit equals that at the entrance (as in the official solution). The ambient pressure $p_a$ acts on the outer surface of the engine and is part of the measured force; $p_a$ is therefore needed as data in addition to those listed.
- The scan prints the direction of the force as $-F\,\mathbf{e}_x$ with $F > 0$ (thrust acts against the exhaust direction). Three unknowns, $\rho_2$, $p_2$, $v_2$, and three equations (mass, axial momentum, energy).

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $A_1$, $A_2$ | entrance and exit areas | m$^2$ |
| $p_1$, $\rho_1$, $v_1$ | entrance state (data) | Pa, kg/m$^3$, m/s |
| $p_2$, $\rho_2$, $v_2$ | exit state (unknowns) | Pa, kg/m$^3$, m/s |
| $F$ | magnitude of the thrust measured on the bench | N |
| $W$ | power extracted from the fluid by the mobile parts | W |
| $Q$ | heat per unit time added to the fluid | W |
| $\dot m = \rho_1 v_1 A_1$ | mass flow | kg/s |

## Phase 2: Coordinates, Frames and Changes of Variable

- Inertial frame fixed to the testbench, with the engine at rest and the axis $\mathbf{e}_x$ along its axis in the direction of the flow.
- Control volume: the gas inside the engine, with boundary $\Sigma_1$ (entrance, $\mathbf{n} = -\mathbf{e}_x$, area $A_1$), $\Sigma_2$ (exit, $\mathbf{n} = +\mathbf{e}_x$, area $A_2$), $\Sigma_3$ (inner surface of the fixed casing) and $\Sigma_4$ (surface of the mobile parts, moving with velocity $\mathbf{v}_w$). The boundary $\Sigma_4$ moves with the blades, so $\mathbf{v}_c = \mathbf{v}_w$ on it. Since the fluid sticks to the walls, $\mathbf{v} = \mathbf{v}_w$ there and $(\mathbf{v} - \mathbf{v}_c)\cdot\mathbf{n} = 0$ on $\Sigma_3 \cup \Sigma_4$. The universal balances (Eqs. 3.10, 3.35, 3.46) are used.
- Since $\int_{\Sigma_c}p_a\,\mathbf{n}\,d\sigma = 0$ on a closed surface, $p$ is replaced by $p - p_a$ in the momentum balance. The measured force $\mathbf{F}$ is the net force of the gas and the atmosphere on the engine, so the force of the engine on the gas is $-\mathbf{F} = +F\,\mathbf{e}_x$ (gauge form, thin casing).
- The power taken from the gas by the mobile parts is defined with the normal $\mathbf{n}$ pointing out of the solid (into the gas), as in CL5.pdf: $W = -\int_{\Sigma_4}p\,\mathbf{v}_w\cdot\mathbf{n}\,d\sigma + \int_{\Sigma_4}\mathbf{v}_w\cdot\bar{\bar{\tau}}'\cdot\mathbf{n}\,d\sigma$, the power of the traction of the gas on the moving solid.

## Phase 3: Step-by-Step Derivation

### 3.1 Mass

Why this tool: Notes Eq. 3.10 with zero net accumulation. On $\Sigma_3$ and $\Sigma_4$, $(\mathbf{v} - \mathbf{v}_c)\cdot\mathbf{n} = 0$:

$$ -\rho_1 v_1 A_1 + \rho_2 v_2 A_2 = 0 \;\Longrightarrow\; \boxed{\,\rho_2\,v_2\,A_2 = \rho_1\,v_1\,A_1 = \dot m\,}. \tag{M} $$

### 3.2 Axial momentum

Why this tool: the thrust is the force on the engine, which enters the balance of Notes Eq. 3.35 through the unknown wall term. Left-hand side, using (M):

$$ \int_{\Sigma_c}\rho\,v_x\,[(\mathbf{v} - \mathbf{v}_c)\cdot\mathbf{n}]\,d\sigma = -\rho_1 v_1^2 A_1 + \rho_2 v_2^2 A_2 = \dot m\,(v_2 - v_1). $$

Right-hand side: $\Sigma_1$ gives $+(p_1 - p_a)A_1$ and $\Sigma_2$ gives $-(p_2 - p_a)A_2$; viscous stresses are negligible there; the walls give $-\mathbf{F}\cdot\mathbf{e}_x = +F$. Hence

$$ \dot m\,(v_2 - v_1) = (p_1 - p_a)A_1 - (p_2 - p_a)A_2 + F \;\Longrightarrow\; \boxed{\,F = \rho_1 v_1 A_1\,(v_2 - v_1) - (p_1 - p_a)A_1 + (p_2 - p_a)A_2\,} \tag{P} $$

### 3.3 Total energy

Why this tool: $p_2$ and $\rho_2$ are linked by the heat and work exchanged, which only the energy balance (Notes Eq. 3.46) contains. On $\Sigma_3$ the casing is at rest, so no work is done; on $\Sigma_4$ the terms $-\int p\,\mathbf{v}\cdot\mathbf{n}\,d\sigma + \int\mathbf{v}\cdot\bar{\bar{\tau}}'\cdot\mathbf{n}\,d\sigma$ of Eq. 3.46 (normal out of the gas) are the power done on the gas by the blades, which is $-W$ by the definition of $W$ in Phase 2; the heat through the walls plus the heat release in the volume is $Q$. On $\Sigma_1$ and $\Sigma_2$ the pressure work $p\,\mathbf{v}\cdot\mathbf{n}$ joins the convective flux and turns $e$ into $h$:

$$ \rho_1 v_1 A_1\left[\left(e_2 + \frac{v_2^2}{2}\right) - \left(e_1 + \frac{v_1^2}{2}\right)\right] = p_1 v_1 A_1 - p_2 v_2 A_2 - W + Q, $$

$$ \boxed{\,\dot m\left[\left(\frac{\gamma}{\gamma - 1}\frac{p_2}{\rho_2} + \frac{v_2^2}{2}\right) - \left(\frac{\gamma}{\gamma - 1}\frac{p_1}{\rho_1} + \frac{v_1^2}{2}\right)\right] = Q - W\,} \tag{E} $$

Equations (M), (P) and (E) determine $\rho_2$, $p_2$ and $v_2$.

## Phase 4: Interpretation, Limits and Dimensional Check

- Equation (P) is the classical thrust balance: the thrust is the change of momentum flux plus the pressure imbalance on the two sections. For $p_1 = p_2 = p_a$ it reduces to $F = \dot m\,(v_2 - v_1)$.
- Equation (E) says that the stagnation enthalpy of the stream rises by the heat added per unit mass flow and falls by the work extracted per unit mass flow: $Q - W$ is the net energy input.
- Dimensions (SI): $[\dot m\,(v_2 - v_1)] = (\text{kg/s})(\text{m/s}) = \text{N}$; $[(Q - W)/\dot m] = \text{W}/(\text{kg/s}) = \text{J/kg} = \text{m}^2/\text{s}^2 = [h] = [v^2]$.
- Numerical illustration (hypothetical data, not a real engine): $A_1 = 0.5$ m$^2$, $A_2 = 0.3$ m$^2$, $v_1 = 150$ m/s, $p_1 = 0.9\times10^5$ Pa, $\rho_1 = 1.1$ kg/m$^3$ ($M_1 = 0.443$), $p_a = 10^5$ Pa, $F = 30$ kN, $W = 2$ MW, $Q = 30$ MW, $\gamma = 1.4$ give $\dot m = 82.5$ kg/s and the two roots of the extension below: $v_2 = 355.515$ m/s, $p_2 = 126817$ Pa, $\rho_2 = 0.77353$ kg/m$^3$ ($M_2 = 0.742$) and $v_2 = 597.263$ m/s, $p_2 = 60336$ Pa, $\rho_2 = 0.46043$ kg/m$^3$ ($M_2 = 1.39$); the residuals of (M), (P) and (E) are below $10^{-6}$ in SI units.
- Agreement with the official solution: CL5.pdf obtains (M) as $\rho_1 v_1 A_1 = \rho_2 v_2 A_2$, (P) as $F = \rho_1 v_1 A_1(v_2 - v_1) - (p_1 - p_a)A_1 + (p_2 - p_a)A_2$ and (E) as above, the same equations (reading of the handwriting).

> [!info] Extension (beyond the official solution): explicit solution
> With $K \equiv p_a A_2 + F + (p_1 - p_a)A_1 + \dot m\,v_1$, (P) gives $p_2 A_2 = K - \dot m\,v_2$ and, with (M), $p_2/\rho_2 = (K - \dot m\,v_2)\,v_2/\dot m$. Substituting into (E) and using $\frac{1}{2} - \frac{\gamma}{\gamma-1} = -\frac{\gamma+1}{2(\gamma-1)}$ gives the quadratic $(\gamma + 1)\,v_2^2 - 2\gamma\,\frac{K}{\dot m}\,v_2 + 2(\gamma - 1)\,H_0 = 0$ with $H_0 \equiv \frac{\gamma}{\gamma-1}\frac{p_1}{\rho_1} + \frac{v_1^2}{2} + \frac{Q - W}{\dot m}$. It has two roots, a subsonic and a supersonic exit state; for a subsonic entrance and heat addition the physical exit state is the subsonic root (the smaller one), since reaching the supersonic root would need a passage through the sonic condition inside the engine, which this overall balance does not describe. For $F = 0$, $Q = W = 0$ and $A_1 = A_2$ one root is $v_2 = v_1$ and the product of the roots is $2(\gamma-1)H_0/(\gamma+1)$, the Prandtl relation of a normal shock.
