---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - energia
  - mezcla
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL19.pdf"
---

# Problem CL19: Elbow Mixing Two Air Streams: Outlet Velocity, Force and Heat

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The elbow-shaped tube of circular cross section shown in the figure of CL19.pdf serves to mix two different air streams. The pipe discharges to the open atmosphere after mixing is completed. At the inlet, where the pressure $p_i = 2p_a$ and velocity $U_i$ are uniform, the inner stream, with diameter $D/\sqrt{2}$, has temperature $T_1$, and the outer coflow stream has temperature $T_2$. The temperature measurement at the outlet reveals that $T_o = T_1T_2/(T_1 + T_2)$.

- Determine the uniform gas velocity at the outlet $U_o$.
- Compute the force $\bar{F} = F_x\bar{e}_x + F_y\bar{e}_y$ acting on the pipe. In the computation, neglect the effect of gravity.
- Obtain the amount of heat transferred per unit time through the pipe wall.

Note: for a perfect gas, $p = \rho R_gT$, where $R_g$ is the gas constant.

Source: CL19.pdf (page 1, prefinal of Dec 16, 2013). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46.

## Phase 1: Hypotheses, Data and Unknowns

- Steady; perfect gas, $\rho = p/(R_gT)$, $h = c_pT$; neglect $\bar{g}$; uniform velocity and pressure at the inlet; uniform state at the outlet (mixing completed); no moving parts.
- Inlet (diameter $D$, flow along $+\bar{e}_x$): inner stream of area $\pi D^2/8$ at $T_1$, outer annulus of area $\pi D^2/4 - \pi D^2/8 = \pi D^2/8$ at $T_2$, both at $U_i$ and $p_i = 2p_a$. Outlet (diameter $D$, flow along $+\bar{e}_y$): free jet at $p_a$, $T_o$.
- Data: $[p_a,\ U_i,\ T_1,\ T_2,\ D,\ R_g,\ c_p]$. Unknowns: $[U_o,\ F_x,\ F_y,\ \dot{Q}]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $U_i$, $U_o$ | inlet and outlet velocities | m/s |
| $T_1$, $T_2$, $T_o$ | temperatures | K |
| $D$ | pipe diameter | m |
| $\dot{Q}$ | heat from the wall to the gas | W |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the pipe, $\bar{e}_x$ horizontal (inlet flow), $\bar{e}_y$ vertical upwards (outlet flow). Fixed control volume. $A \equiv \pi D^2/4$.
- Surfaces: $\Sigma_i$ (inlet, $\bar{n} = -\bar{e}_x$), $\Sigma_o$ (outlet, $\bar{n} = +\bar{e}_y$), $\Sigma_\ell$ (pipe wall).

$$ \boxed{\,\bar{F} = \int_{\Sigma_\ell}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

$$ \boxed{\,\dot{Q} = -\int_{\Sigma_\ell}\bar{q}\cdot\bar{n}\,d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**1. Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_i\ (T_1)$ | $-\frac{p_i}{R_gT_1}U_i\frac{\pi D^2}{8}$ |
| $\Sigma_i\ (T_2)$ | $-\frac{p_i}{R_gT_2}U_i\frac{\pi D^2}{8}$ |
| $\Sigma_o$ | $+\frac{p_a}{R_gT_o}U_o\frac{\pi D^2}{4}$ |
| $\Sigma_\ell$ | $0$ |

With $p_i = 2p_a$: $\frac{p_a}{R_g}U_i\frac{\pi D^2}{4}\left(\frac{1}{T_1} + \frac{1}{T_2}\right) = \frac{p_a}{R_gT_o}U_o\frac{\pi D^2}{4}$, and $\frac{1}{T_1} + \frac{1}{T_2} = \frac{T_1 + T_2}{T_1T_2} = \frac{1}{T_o}$.

$$ \boxed{\,U_o = U_i\,} \tag{1} $$

**2. Linear momentum (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_i$ | $-\frac{p_i}{R_g}\left(\frac{1}{T_1} + \frac{1}{T_2}\right)U_i^2\frac{\pi D^2}{8}\bar{e}_x = -\frac{p_a}{R_gT_o}U_i^2A\,\bar{e}_x$ | $(p_i - p_a)A\,\bar{e}_x = p_aA\,\bar{e}_x$ | $0$ |
| $\Sigma_o$ | $+\frac{p_a}{R_gT_o}U_o^2A\,\bar{e}_y$ | $0$ (free jet) | $0$ |
| **$\Sigma_\ell$** (boxed) | $0$ | $-\int_{\Sigma_\ell}(p - p_a)\,\bar{n}\,d\sigma$ | $\int_{\Sigma_\ell}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed $\Sigma_\ell$ terms: $-\bar{F}$. With (1), $U_o = U_i$.

$$ \boxed{\,\bar{F} = \frac{\pi D^2}{4}\,p_a\left(1 + \frac{U_i^2}{R_gT_o}\right)\bar{e}_x - \frac{\pi D^2}{4}\,\frac{p_aU_i^2}{R_gT_o}\,\bar{e}_y\,} \tag{2} $$

> [!warning] Erratum in the official solution (sign of F_y)
> CL19.pdf writes the momentum balance with $+\frac{p_a}{R_gT_o}U_oU_o\bar{e}_y\frac{\pi D^2}{4}$ on the left-hand side and $-\bar{F}$ on the right, but boxes $\bar{F}$ with $+\frac{\pi D^2}{4}p_a\frac{U_i^2}{R_gT_o}\bar{e}_y$. Moving the outlet flux to the other side gives the minus sign of (2): the jet leaves upwards, so its reaction on the pipe points downwards. The computed sign is kept.

**3. Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_i\ (T_1)$ | $-\dot{m}_1\left(e_1 + \tfrac{U_i^2}{2}\right)$ | $+p_iU_i\frac{\pi D^2}{8}$ | $0$ | $0$ |
| $\Sigma_i\ (T_2)$ | $-\dot{m}_2\left(e_2 + \tfrac{U_i^2}{2}\right)$ | $+p_iU_i\frac{\pi D^2}{8}$ | $0$ | $0$ |
| $\Sigma_o$ | $+\dot{m}\left(e_o + \tfrac{U_o^2}{2}\right)$ | $-p_aU_oA$ | $0$ | $0$ |
| **$\Sigma_\ell$** (boxed) | $0$ | $0$ | $0$ | $-\int_{\Sigma_\ell}\bar{q}\cdot\bar{n}\,d\sigma$ |

Boxed term: $\dot{Q}$. Combining with the pressure work, $h = c_pT$; the kinetic terms cancel ($U_o = U_i$, $\dot{m}_1 + \dot{m}_2 = \dot{m}$). Enthalpy fluxes: $\dot{m}_kc_pT_k = c_p\frac{p_i}{R_g}U_i\frac{\pi D^2}{8}$ for each inlet stream, so their sum is $c_p\frac{2p_a}{R_g}U_iA$; at the outlet $\dot{m}c_pT_o = c_p\frac{p_a}{R_g}U_iA$.

$$ \dot{Q} = c_p\frac{p_a}{R_g}U_iA - c_p\frac{2p_a}{R_g}U_iA \;\Longrightarrow\; \boxed{\,\dot{Q} = -\frac{c_p}{R_g}\,p_aU_i\,\frac{\pi D^2}{4}\,} \tag{3} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- $\dot{Q} < 0$: heat leaves the gas through the wall. This is consistent with the data: $T_o = T_1T_2/(T_1 + T_2)$ is lower than both inlet temperatures, so the gas must be cooled (the official solution notes that the fluid is cooled down as it flows through the pipe).
- The outlet velocity equals the inlet one because the density halves with the pressure ($p_a$ vs $2p_a$) while the temperature effect is exactly offset by the chosen $T_o$.
- Dimensions (SI): $[p_aA] = \text{N}$; $[p_aU_i^2A/(R_gT)] = \text{N}$; $[c_pp_aU_iA/R_g] = \text{W}$.
- Numerical illustration (hypothetical data): $p_a = 101325$ Pa, $U_i = 20$ m/s, $T_1 = 300$ K, $T_2 = 400$ K ($T_o = 171.43$ K), $D = 0.1$ m, $R_g = 287$ J/(kg K), $c_p = 1005$ J/(kg K) give $F_x = 802.27$ N, $F_y = -6.47$ N and $\dot{Q} = -55734$ W.
