# CL17 to CL22 in the class style.
import math
from clcommon import *
from cl_p02 import ENERGY_COLS, energy_eq, mom_eq, mass_eq

# ---------------------------------------------------------------- CL17
_ai, _ao, _b, _Vi, _ri, _pi, _po, _pa, _Q = 0.3, 0.25, 1.0, 150., 1.0, 0.9e5, 1.0e5, 1.0e5, 2.0e7
_md17 = _ri * _Vi * _ai * _b
_H17 = GAM / (GAM - 1) * _pi / _ri + _Vi ** 2 / 2 + _Q / _md17
_B17 = GAM * _po * _ao * _b / ((GAM - 1) * _md17)
_Vo17 = -_B17 + math.sqrt(_B17 ** 2 + 2 * _H17)
_ro17 = _md17 / (_Vo17 * _ao * _b)
_T17 = _md17 * (_Vo17 - _Vi) + (_po - _pa) * _ao * _b - (_pi - _pa) * _ai * _b
_M17 = _b / 2 * ((_ri * _Vi ** 2 + _pi - _pa) * _ai ** 2 + (_ro17 * _Vo17 ** 2 + _po - _pa) * _ao ** 2)
_L17 = _M17 / 5e3
CL17 = dict(
    id="cl17", pill="CL17: Ramjet Airplane",
    title="Airplane with an Engine without Moving Parts: Exit State, Thrust, Torque and Canard",
    note_title="Problem - CL17 Airplane Engine Torque and Canard",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-angular", "energia", "empuje"],
    tags_html=["Thrust", "Angular momentum", "Energy", "Trim"],
    statement=[
        ("p", r"An experimental airplane is powered by an engine without moving parts that delivers a heat $\dot{Q}$ per unit time. The entrance and exit sections of the engine are, respectively, below and above the airplane's center of gravity (CoG), which is placed at the origin of the coordinate system shown in the figure of CL17.pdf. Both sections are rectangular with the same spanwise length $b$ (along the $z$-direction), and heights $a_i$ and $a_o$, as indicated in the figure. The flow at the engine's inlet has velocity $V_i$, pressure $p_i$ and density $\rho_i$, while the outlet jet discharges at pressure $p_o$. The flow is steady; gravitational forces are negligible; the conditions at the engine's inlet and outlet sections are uniform; the air behaves as a perfect gas of constant $R_g$ and specific heat ratio $\gamma$; the known data are $(a_i, V_i, \rho_i, p_i, a_o, p_o, p_a, \dot{Q})$."),
        ("ul", [
            r"Applying the mass and energy conservation equations to an appropriately defined control volume, obtain the pair of equations that determine the jet exhaust velocity, $V_o$, and the corresponding density, $\rho_o$. In the remainder of the problem, assume that $V_o$ and $\rho_o$ are already known.",
            r"Use the momentum equation to obtain the thrust provided by the engine, $\bar{T}$.",
            r"Use the angular momentum equation to obtain the net torque $\bar{M}$ acting on the airplane with respect to its CoG. Assume that the surrounding air is at uniform pressure $p_a$, except at the engine's inlet and outlet.",
            r"To compensate the torque obtained in the previous question, the engineers decide that the main wing's CoG coincides with that of the full airplane, so that it doesn't contribute to the torque, and to place a control surface (canard) at a distance $L$ from the CoG (see figure). Knowing that this control surface provides a lift force $F$, determine the distance $L$.",
        ]),
    ],
    source_line=r"Source: CL17.pdf (page 1, exam of June 27, 2013; statement only, no official solution in the source). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady; neglect $\bar{g}$; uniform properties at the inlet and outlet; perfect gas, $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$; no moving parts (no shaft work); the heat $\dot{Q}$ is the only energy input.",
                r"Surrounding air at $p_a$ everywhere except at the two sections; viscous stresses negligible on the sections.",
                r"Geometry (reading of the figure): the inlet section spans $-a_i < y < 0$ and the outlet section $0 < y < a_o$, both normal to $\bar{e}_x$, with the flow along $+\bar{e}_x$ (from the nose side to the tail). The nose points towards $-\bar{e}_x$; the canard is at $x = -L$.",
                r"Data: $[a_i,\ V_i,\ \rho_i,\ p_i,\ a_o,\ p_o,\ p_a,\ \dot{Q},\ b,\ \gamma,\ F]$. Unknowns: $[V_o,\ \rho_o,\ \bar{T},\ \bar{M},\ L]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$a_i$, $a_o$, $b$", "section heights and span", "m"],
                [r"$V_i$, $\rho_i$, $p_i$", "inlet state", r"m/s, kg/m$^3$, Pa"],
                [r"$V_o$, $\rho_o$, $p_o$", "outlet state", r"m/s, kg/m$^3$, Pa"],
                [r"$\dot{Q}$", "heat added per unit time", "W"],
                [r"$\bar{T}$, $\bar{M}$", "thrust and torque on the airplane", r"N, N$\cdot$m"],
            ]),
            ("note", "No official solution", r"CL17.pdf contains only the statement. The solution below is derived independently and checked numerically; there is no official key to compare with."),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the airplane (steady flight or test bench), origin at the CoG, $\bar{e}_x$ towards the tail, $\bar{e}_y$ upwards, $\bar{e}_z$ towards the reader. Fixed control volume: the air inside the engine.",
                r"Surfaces: $\Sigma_i$ (inlet, $\bar{n} = -\bar{e}_x$, area $a_ib$), $\Sigma_o$ (outlet, $\bar{n} = +\bar{e}_x$, area $a_ob$), $\Sigma_w$ (engine walls, at rest).",
            ]),
            ("m", r"\boxed{\,\bar{T} = \int_{\Sigma_w}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
            ("m", r"\boxed{\,\bar{M} = \int_{\Sigma_w}\bar{x}\wedge\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="1. Mass (Notes Eq. 3.11)", eq=mass_eq(), cols=[COL_MASS],
                rows=[(r"\Sigma_i", [r"$-\rho_iV_ia_ib$"], False), (r"\Sigma_o", [r"$+\rho_oV_oa_ob$"], False), (r"\Sigma_w", [r"$0$"], False)],
                result=r"\boxed{\,\rho_iV_ia_i = \rho_oV_oa_o\,},\qquad \dot{m} = \rho_iV_ia_ib \tag{1}")),
            ("bal", dict(
                label="1. Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=True), cols=ENERGY_COLS,
                rows=[(r"\Sigma_i", [r"$-\dot{m}\left(e_i + \tfrac{V_i^2}{2}\right)$", r"$+p_iV_ia_ib$", r"$0$", r"$0$"], False),
                      (r"\Sigma_o", [r"$+\dot{m}\left(e_o + \tfrac{V_o^2}{2}\right)$", r"$-p_oV_oa_ob$", r"$0$", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$0$ ($\bar{v} = 0$)", r"$0$", r"$-\int_{\Sigma_w}\bar{q}\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed term plus the volume heat release: $\dot{Q}$.",
                result=r"\boxed{\,\dot{m}\left[\left(\frac{\gamma}{\gamma - 1}\frac{p_o}{\rho_o} + \frac{V_o^2}{2}\right) - \left(\frac{\gamma}{\gamma - 1}\frac{p_i}{\rho_i} + \frac{V_i^2}{2}\right)\right] = \dot{Q}\,} \tag{2}")),
            ("p", r"(1) and (2) are the pair of equations for $V_o$ and $\rho_o$. Explicitly (extension): with (1), $\frac{p_o}{\rho_o} = \frac{p_oV_oa_ob}{\dot{m}}$, and (2) becomes $\frac{V_o^2}{2} + BV_o - H = 0$ with $B = \frac{\gamma}{\gamma-1}\frac{p_oa_ob}{\dot{m}}$ and $H = \frac{\gamma}{\gamma-1}\frac{p_i}{\rho_i} + \frac{V_i^2}{2} + \frac{\dot{Q}}{\dot{m}}$, whose positive root is $V_o = -B + \sqrt{B^2 + 2H}$."),
            ("bal", dict(
                label="2. Linear momentum (Notes Eq. 3.36)", eq=MOM_FIXED_NOG, cols=[COL_MFLUX, COL_P, COL_TAU],
                rows=[(r"\Sigma_i", [r"$-\dot{m}V_i\,\bar{e}_x$", r"$+(p_i - p_a)a_ib\,\bar{e}_x$", r"$0$"], False),
                      (r"\Sigma_o", [r"$+\dot{m}V_o\,\bar{e}_x$", r"$-(p_o - p_a)a_ob\,\bar{e}_x$", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$", r"$\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed terms: $-\bar{T}$.",
                result=r"\boxed{\,\bar{T} = -\left[\dot{m}\,(V_o - V_i) + (p_o - p_a)a_ob - (p_i - p_a)a_ib\right]\bar{e}_x\,} \tag{3}")),
            ("bal", dict(
                label="3. Angular momentum about the CoG, z component (Notes Eq. 3.38)", eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho\,\bar{x}\wedge\bar{v}\,dV", "0") + r" + \int_{\Sigma_c}\rho\,(\bar{x}\wedge\bar{v})(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma",
                cols=[r"\int\rho\,(\bar{x}\wedge\bar{v})_z(\bar{v}\cdot\bar{n})\,d\sigma", r"-\int\left[\bar{x}\wedge(p - p_a)\bar{n}\right]_z d\sigma", r"\text{viscous}"],
                rows=[(r"\Sigma_i", [r"$\int_{-a_i}^0\rho_i(-yV_i)(-V_i)\,b\,dy = -\rho_iV_i^2\frac{a_i^2}{2}b$", r"$-\int_{-a_i}^0(p_i - p_a)\,y\,b\,dy = +(p_i - p_a)\frac{a_i^2}{2}b$", r"$0$"], False),
                      (r"\Sigma_o", [r"$\int_0^{a_o}\rho_o(-yV_o)(V_o)\,b\,dy = -\rho_oV_o^2\frac{a_o^2}{2}b$", r"$-\int_0^{a_o}(p_o - p_a)(-y)\,b\,dy = +(p_o - p_a)\frac{a_o^2}{2}b$", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$-\int_{\Sigma_w}\left[\bar{x}\wedge(p - p_a)\bar{n}\right]_z d\sigma$", r"$\int_{\Sigma_w}\left[\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\right]_z d\sigma$"], True)],
                wall=r"Boxed terms: $-M_z$. On a section normal to $\bar{e}_x$, $(\bar{x}\wedge\bar{v})_z = xv_y - yv_x = -yV$ and $(\bar{x}\wedge\bar{n})_z = -yn_x$. Antiderivative of $y$: $y^2/2$; Barrow's rule gives $\left[\frac{y^2}{2}\right]_{-a_i}^0 = -\frac{a_i^2}{2}$ and $\left[\frac{y^2}{2}\right]_0^{a_o} = \frac{a_o^2}{2}$.",
                result=r"\boxed{\,\bar{M} = \frac{b}{2}\left[\left(\rho_iV_i^2 + p_i - p_a\right)a_i^2 + \left(\rho_oV_o^2 + p_o - p_a\right)a_o^2\right]\bar{e}_z\,} \tag{4}")),
            ("h4", "4. Canard position"),
            ("p", r"The lift $F\bar{e}_y$ of the canard, applied at $x = -L$, has moment $(-L\bar{e}_x)\wedge(F\bar{e}_y) = -LF\,\bar{e}_z$ about the CoG. The wing gives no moment (its CoG is the airplane's). Trim requires $\bar{M} - LF\bar{e}_z = 0$:"),
            ("m", r"\boxed{\,L = \frac{M_z}{F} = \frac{b}{2F}\left[\left(\rho_iV_i^2 + p_i - p_a\right)a_i^2 + \left(\rho_oV_o^2 + p_o - p_a\right)a_o^2\right]\,} \tag{5}"),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"The airflow enters below the CoG and leaves above it, so both the intake (pushed backwards) and the exhaust reaction (pushed forwards) create a positive $M_z$, which pitches the nose down (the nose is at $-x$). The canard ahead of the CoG with an upward lift balances it, which is why $L > 0$.",
                r"Heating raises the stagnation enthalpy (2): the gas leaves faster ($V_o > V_i$), giving the thrust (3) along $-\bar{e}_x$ (forwards).",
                r"Dimensions (SI): $[\dot{m}V] = \text{N}$; $[(\rho V^2 + p)a^2b] = \text{N}\cdot\text{m}$; $[M_z/F] = \text{m}$.",
                rf"Numerical illustration (hypothetical data): $a_i = 0.3$ m, $a_o = 0.25$ m, $b = 1$ m, $V_i = 150$ m/s, $\rho_i = 1$ kg/m$^3$, $p_i = 0.9\times10^5$ Pa, $p_o = p_a = 10^5$ Pa, $\dot{{Q}} = 20$ MW, $\gamma = 1.4$, $F = 5$ kN give $V_o = {f(_Vo17)}$ m/s, $\rho_o = {f(_ro17)}$ kg/m$^3$, $|\bar{{T}}| = {f(_T17)}$ N, $M_z = {f(_M17)}$ N$\cdot$m, $L = {f(_L17,4)}$ m (energy residual below $10^{{-7}}$).",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL18
_A18, _Aj, _Uj, _c18 = 1.0, 0.1, 10., 4186.
_s18 = math.sqrt(2 * _Aj * (_A18 - _Aj))
_Ue18 = _Uj * _s18 / (_s18 + _A18)
_Uo18 = _Uj * (_Aj + _s18) / (_A18 + _s18)
_dT18 = (_Uj * _Aj / (2 * _Uo18 * _A18) * (1 - (_Ue18 / _Uj) ** 2) - 0.5 * (_Uo18 / _Uj) ** 2) * _Uj ** 2 / _c18
CL18 = dict(
    id="cl18", pill="CL18: Ejector",
    title="Liquid Ejector: Entrained Flow Rate, Outlet Velocity and Heating",
    note_title="Problem - CL18 Liquid Ejector",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "energia", "eyector"],
    tags_html=["Ejector", "Bernoulli", "Mixing", "Dissipation"],
    statement=[
        ("p", r"The ejector shown in the figure of CL18.pdf is used to discharge a container filled with a perfect liquid of density $\rho$ and constant specific heat $c$ into the atmosphere, also at pressure $p_a$. A high-velocity jet of the same liquid, with velocity $U_j$ and cross section $A_j$, is injected along the axis of the discharge pipe, whose cross section is $A$. The jet entrains fluid as it develops, producing an underpressure at the injection section and drawing the fluid from the container. Mixing of the jet with the surrounding liquid is completed downstream, so that at the outlet the liquid discharges as a uniform jet with velocity $U_o$. For a given the geometry (i.e., given values of $A_j$ and $A$), we want to compute the characteristics of the flow in terms of the injection velocity $U_j$. In the computation, assume that the effect of gravity is negligible. Address in order the following questions:"),
        ("ul", [
            r"Assuming that the acceleration of the fluid upstream from the injector is steady and inviscid, write down the equation that relates the ambient pressure $p_a$ with the velocity and pressure at the entrance of the pipe, $U_e$ and $p_e$.",
            r"Apply the continuity and momentum balance equations to the control volume indicated in the figure. Simplify the result by assuming that the effect of friction on the wall surface is negligibly small.",
            r"Use the previous equations to show that the volumetric discharge flow rate is given by $Q = U_e(A - A_j) = \dfrac{U_j(A - A_j)}{1 + A/\sqrt{2A_j(A - A_j)}}$ and that the velocity at the outlet satisfies $\dfrac{U_o}{U_j} = \dfrac{A_j + \sqrt{2A_j(A - A_j)}}{A + \sqrt{2A_j(A - A_j)}}$.",
            r"Assuming that the values of the temperatures $T_e$ and $T_j$ at the entrance section are equal to the ambient value $T_a$, obtain the temperature $T_o$ at the outlet section when the pipe walls are adiabatic.",
        ]),
    ],
    source_line=r"Source: CL18.pdf (page 1, midterm of Nov 11, 2013). Notes.pdf: Bernoulli's equation Eq. 4.17, integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady, incompressible liquid, $e = cT$; neglect $\bar{g}$; friction on the pipe wall negligible; adiabatic walls.",
                r"Entrance section (area $A$): the jet ($A_j$, $U_j$) and the entrained liquid (annulus $A - A_j$, $U_e$) are both at the pressure $p_e$ (parallel streams). Outlet: uniform $U_o$ at $p_a$ (complete mixing).",
                r"Data: $[\rho,\ c,\ A,\ A_j,\ U_j,\ p_a,\ T_a]$. Unknowns: $[U_e,\ p_e,\ U_o,\ Q,\ T_o]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$A$, $A_j$", "pipe and jet areas", r"m$^2$"],
                [r"$U_j$, $U_e$, $U_o$", "jet, entrained and outlet velocities", "m/s"],
                [r"$p_e$", "pressure at the entrance section", "Pa"],
                [r"$Q$", "entrained volume flow rate", r"m$^3$/s"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the pipe; $\bar{e}_x$ along the pipe axis in the flow direction. Fixed control volume between the entrance and the outlet sections.",
                r"Surfaces: $\Sigma_e$ (entrance, $\bar{n} = -\bar{e}_x$, split into the jet $A_j$ and the annulus $A - A_j$), $\Sigma_o$ (outlet, $\bar{n} = +\bar{e}_x$), $\Sigma_w$ (straight pipe wall, $\bar{n}\perp\bar{e}_x$).",
            ]),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("h4", "1. Bernoulli upstream of the entrance"),
            ("p", r"From the still liquid of the container (at $p_a$) to the entrance (Notes Eq. 4.17):"),
            ("m", r"\boxed{\,p_a = p_e + \tfrac{1}{2}\rho U_e^2\,} \tag{1}"),
            ("bal", dict(
                label="2. Mass (Notes Eq. 3.11)", eq=mass_eq(), cols=[COL_MASS],
                rows=[(r"\Sigma_e\ (\text{annulus})", [r"$-\rho U_e(A - A_j)$"], False), (r"\Sigma_e\ (\text{jet})", [r"$-\rho U_jA_j$"], False), (r"\Sigma_o", [r"$+\rho U_oA$"], False), (r"\Sigma_w", [r"$0$"], False)],
                result=r"\boxed{\,U_oA = U_e(A - A_j) + U_jA_j\,} \tag{2}")),
            ("bal", dict(
                label="2. Linear momentum, x component (Notes Eq. 3.36)", eq=MOM_FIXED_NOG, cols=[r"\int\rho v_x\,(\bar{v}\cdot\bar{n})\,d\sigma", r"-\int(p - p_a)\,n_x\,d\sigma", r"\int(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma"],
                rows=[(r"\Sigma_e\ (\text{annulus})", [r"$-\rho U_e^2(A - A_j)$", r"$(p_e - p_a)(A - A_j)$", r"$0$"], False),
                      (r"\Sigma_e\ (\text{jet})", [r"$-\rho U_j^2A_j$", r"$(p_e - p_a)A_j$", r"$0$"], False),
                      (r"\Sigma_o", [r"$+\rho U_o^2A$", r"$0$ ($p = p_a$)", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$0$ ($n_x = 0$)", r"$0$ (friction neglected)"], False)],
                wall=r"With (1), $(p_e - p_a)A = -\tfrac{1}{2}\rho U_e^2A$.",
                result=r"\boxed{\,U_o^2A = U_e^2\left(\frac{A}{2} - A_j\right) + U_j^2A_j\,} \tag{3}")),
            ("h4", "3. Flow rate and outlet velocity"),
            ("p", r"Squaring (2) and dividing by $A$, then equating to (3):"),
            ("m", r"\left[U_e(A - A_j) + U_jA_j\right]^2 = A\left[U_e^2\left(\frac{A}{2} - A_j\right) + U_j^2A_j\right]."),
            ("p", r"Expanding, $U_e^2\left[(A - A_j)^2 - \frac{A^2}{2} + AA_j\right] + 2U_eU_jA_j(A - A_j) + U_j^2(A_j^2 - AA_j) = 0$. With $k = A_j(A - A_j)$ and $x = U_e/U_j$, the bracket is $\frac{A^2}{2} - k$ and the equation reads"),
            ("m", r"\left(\frac{A^2}{2} - k\right)x^2 + 2kx - k = 0 \;\Longrightarrow\; x = \frac{-k \pm \sqrt{k^2 + k\left(\frac{A^2}{2} - k\right)}}{\frac{A^2}{2} - k} = \frac{-k \pm \frac{As}{2}}{\frac{(A - s)(A + s)}{2}},\qquad s \equiv \sqrt{2k} = \sqrt{2A_j(A - A_j)}."),
            ("p", r"The $+$ sign gives $x = \frac{s(A - s)}{(A - s)(A + s)} = \frac{s}{A + s}$; the $-$ sign gives $x = -\frac{s}{A - s} < 0$ (liquid flowing back into the container, rejected). Hence"),
            ("m", r"\frac{U_e}{U_j} = \frac{1}{1 + A/\sqrt{2A_j(A - A_j)}},\qquad \boxed{\,Q = U_e(A - A_j) = \frac{U_j(A - A_j)}{1 + A/\sqrt{2A_j(A - A_j)}}\,} \tag{4}"),
            ("p", r"and from (2), $\frac{U_o}{U_j} = \frac{x(A - A_j) + A_j}{A} = \frac{s(A - A_j) + A_j(s + A)}{A(A + s)} = \frac{sA + A_jA}{A(A + s)}$:"),
            ("m", r"\boxed{\,\frac{U_o}{U_j} = \frac{A_j + \sqrt{2A_j(A - A_j)}}{A + \sqrt{2A_j(A - A_j)}}\,} \tag{5}"),
            ("bal", dict(
                label="4. Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False), cols=ENERGY_COLS,
                rows=[(r"\Sigma_e\ (\text{annulus})", [r"$-\rho U_e(A - A_j)\left(cT_e + \tfrac{U_e^2}{2}\right)$", r"$+p_eU_e(A - A_j)$", r"$0$", r"$0$"], False),
                      (r"\Sigma_e\ (\text{jet})", [r"$-\rho U_jA_j\left(cT_j + \tfrac{U_j^2}{2}\right)$", r"$+p_eU_jA_j$", r"$0$", r"$0$"], False),
                      (r"\Sigma_o", [r"$+\rho U_oA\left(cT_o + \tfrac{U_o^2}{2}\right)$", r"$-p_aU_oA$", r"$0$", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$0$", r"$0$", r"$0$ (adiabatic)"], False)],
                wall=r"Pressure work: by (2) and (1), $p_e[U_e(A - A_j) + U_jA_j] - p_aU_oA = (p_e - p_a)U_oA = -\tfrac{1}{2}\rho U_e^2U_oA$. With $T_e = T_j = T_a$ the internal-energy terms give $\rho cU_oA(T_o - T_a)$; using $U_e(A - A_j) = U_oA - U_jA_j$ and dividing by $\rho U_oAU_j^2$:",
                result=r"\boxed{\,\frac{c\,(T_o - T_a)}{U_j^2} = \frac{U_jA_j}{2U_oA}\left[1 - \left(\frac{U_e}{U_j}\right)^2\right] - \frac{1}{2}\left(\frac{U_o}{U_j}\right)^2\,} \tag{6}")),
            ("note", "Erratum in the official solution", r"CL18.pdf writes the energy balance as in the table but boxes $\frac{c(T_o - T_a)}{U_j^2} = \frac{U_jA_j}{U_oA}\left[1 - \left(\frac{U_e}{U_j}\right)^2\right] - \left(\frac{U_o}{U_j}\right)^2$, without the two factors $\tfrac{1}{2}$ (all kinetic energies are $U^2/2$), i.e. twice the value of (6). Check: for $A = 1$ m$^2$, $A_j = 0.1$ m$^2$, $U_j = 10$ m/s, $c = 4186$ J/(kg K), the residual of the energy balance (per unit density) is $0$ with (6) and $20.6$ W/(kg/m$^3$) with the boxed expression. The computed value is kept."),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"$T_o > T_a$: the mixing of the fast jet with the slow entrained liquid dissipates kinetic energy, which appears as heat. The rise is tiny for a liquid ($c$ is large).",
                r"Limit $A_j \to 0$: $s \to 0$, $Q \to 0$ and $U_o \to 0$ (no jet, no pumping). Limit $A_j \to A$: $s \to 0$, $Q \to 0$ and $U_o \to U_j$ (the jet fills the pipe).",
                r"Dimensions (SI): $[Q] = (\text{m/s})\,\text{m}^2 = \text{m}^3/\text{s}$; $[cT/U^2] = 1$.",
                rf"Numerical illustration (hypothetical data): $A = 1$ m$^2$, $A_j = 0.1$ m$^2$, $U_j = 10$ m/s, water ($c = 4186$ J/(kg K)) give $U_e = {f(_Ue18)}$ m/s, $Q = {f(_Ue18*(_A18-_Aj))}$ m$^3$/s, $U_o = {f(_Uo18)}$ m/s and $T_o - T_a = {f(_dT18*1000,4)}$ mK; the residuals of (2) and (3) are below $10^{{-14}}$.",
                r"Agreement with the official solution: (1) to (5) as in CL18.pdf; (6) differs by the factors $\tfrac{1}{2}$ discussed above.",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL19
_pa19, _Ui19, _T119, _T219, _D19, _Rg, _cp = 101325., 20., 300., 400., 0.1, 287., 1005.
_A19 = math.pi * _D19 ** 2 / 4
_To19 = _T119 * _T219 / (_T119 + _T219)
_Fx19 = _A19 * _pa19 * (1 + _Ui19 ** 2 / (_Rg * _To19))
_Fy19 = -_A19 * _pa19 * _Ui19 ** 2 / (_Rg * _To19)
_Q19 = -_cp * _pa19 * _Ui19 * _A19 / _Rg
CL19 = dict(
    id="cl19", pill="CL19: Two-Stream Elbow",
    title="Elbow Mixing Two Air Streams: Outlet Velocity, Force and Heat",
    note_title="Problem - CL19 Elbow Mixing Two Air Streams",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "energia", "mezcla"],
    tags_html=["Coflow", "Perfect gas", "Linear momentum", "Heat"],
    statement=[
        ("p", r"The elbow-shaped tube of circular cross section shown in the figure of CL19.pdf serves to mix two different air streams. The pipe discharges to the open atmosphere after mixing is completed. At the inlet, where the pressure $p_i = 2p_a$ and velocity $U_i$ are uniform, the inner stream, with diameter $D/\sqrt{2}$, has temperature $T_1$, and the outer coflow stream has temperature $T_2$. The temperature measurement at the outlet reveals that $T_o = T_1T_2/(T_1 + T_2)$."),
        ("ul", [r"Determine the uniform gas velocity at the outlet $U_o$.", r"Compute the force $\bar{F} = F_x\bar{e}_x + F_y\bar{e}_y$ acting on the pipe. In the computation, neglect the effect of gravity.", r"Obtain the amount of heat transferred per unit time through the pipe wall."]),
        ("p", r"Note: for a perfect gas, $p = \rho R_gT$, where $R_g$ is the gas constant."),
    ],
    source_line=r"Source: CL19.pdf (page 1, prefinal of Dec 16, 2013). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady; perfect gas, $\rho = p/(R_gT)$, $h = c_pT$; neglect $\bar{g}$; uniform velocity and pressure at the inlet; uniform state at the outlet (mixing completed); no moving parts.",
                r"Inlet (diameter $D$, flow along $+\bar{e}_x$): inner stream of area $\pi D^2/8$ at $T_1$, outer annulus of area $\pi D^2/4 - \pi D^2/8 = \pi D^2/8$ at $T_2$, both at $U_i$ and $p_i = 2p_a$. Outlet (diameter $D$, flow along $+\bar{e}_y$): free jet at $p_a$, $T_o$.",
                r"Data: $[p_a,\ U_i,\ T_1,\ T_2,\ D,\ R_g,\ c_p]$. Unknowns: $[U_o,\ F_x,\ F_y,\ \dot{Q}]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$U_i$, $U_o$", "inlet and outlet velocities", "m/s"],
                [r"$T_1$, $T_2$, $T_o$", "temperatures", "K"],
                [r"$D$", "pipe diameter", "m"],
                [r"$\dot{Q}$", "heat from the wall to the gas", "W"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the pipe, $\bar{e}_x$ horizontal (inlet flow), $\bar{e}_y$ vertical upwards (outlet flow). Fixed control volume. $A \equiv \pi D^2/4$.",
                r"Surfaces: $\Sigma_i$ (inlet, $\bar{n} = -\bar{e}_x$), $\Sigma_o$ (outlet, $\bar{n} = +\bar{e}_y$), $\Sigma_\ell$ (pipe wall).",
            ]),
            ("m", r"\boxed{\,\bar{F} = \int_{\Sigma_\ell}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
            ("m", r"\boxed{\,\dot{Q} = -\int_{\Sigma_\ell}\bar{q}\cdot\bar{n}\,d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="1. Mass (Notes Eq. 3.11)", eq=mass_eq(), cols=[COL_MASS],
                rows=[(r"\Sigma_i\ (T_1)", [r"$-\frac{p_i}{R_gT_1}U_i\frac{\pi D^2}{8}$"], False), (r"\Sigma_i\ (T_2)", [r"$-\frac{p_i}{R_gT_2}U_i\frac{\pi D^2}{8}$"], False), (r"\Sigma_o", [r"$+\frac{p_a}{R_gT_o}U_o\frac{\pi D^2}{4}$"], False), (r"\Sigma_\ell", [r"$0$"], False)],
                wall=r"With $p_i = 2p_a$: $\frac{p_a}{R_g}U_i\frac{\pi D^2}{4}\left(\frac{1}{T_1} + \frac{1}{T_2}\right) = \frac{p_a}{R_gT_o}U_o\frac{\pi D^2}{4}$, and $\frac{1}{T_1} + \frac{1}{T_2} = \frac{T_1 + T_2}{T_1T_2} = \frac{1}{T_o}$.",
                result=r"\boxed{\,U_o = U_i\,} \tag{1}")),
            ("bal", dict(
                label="2. Linear momentum (Notes Eq. 3.36)", eq=MOM_FIXED_NOG, cols=[COL_MFLUX, COL_P, COL_TAU],
                rows=[(r"\Sigma_i", [r"$-\frac{p_i}{R_g}\left(\frac{1}{T_1} + \frac{1}{T_2}\right)U_i^2\frac{\pi D^2}{8}\bar{e}_x = -\frac{p_a}{R_gT_o}U_i^2A\,\bar{e}_x$", r"$(p_i - p_a)A\,\bar{e}_x = p_aA\,\bar{e}_x$", r"$0$"], False),
                      (r"\Sigma_o", [r"$+\frac{p_a}{R_gT_o}U_o^2A\,\bar{e}_y$", r"$0$ (free jet)", r"$0$"], False),
                      (r"\Sigma_\ell", [r"$0$", r"$-\int_{\Sigma_\ell}(p - p_a)\,\bar{n}\,d\sigma$", r"$\int_{\Sigma_\ell}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed $\Sigma_\ell$ terms: $-\bar{F}$. With (1), $U_o = U_i$.",
                result=r"\boxed{\,\bar{F} = \frac{\pi D^2}{4}\,p_a\left(1 + \frac{U_i^2}{R_gT_o}\right)\bar{e}_x - \frac{\pi D^2}{4}\,\frac{p_aU_i^2}{R_gT_o}\,\bar{e}_y\,} \tag{2}")),
            ("note", "Erratum in the official solution (sign of F_y)", r"CL19.pdf writes the momentum balance with $+\frac{p_a}{R_gT_o}U_oU_o\bar{e}_y\frac{\pi D^2}{4}$ on the left-hand side and $-\bar{F}$ on the right, but boxes $\bar{F}$ with $+\frac{\pi D^2}{4}p_a\frac{U_i^2}{R_gT_o}\bar{e}_y$. Moving the outlet flux to the other side gives the minus sign of (2): the jet leaves upwards, so its reaction on the pipe points downwards. The computed sign is kept."),
            ("bal", dict(
                label="3. Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False), cols=ENERGY_COLS,
                rows=[(r"\Sigma_i\ (T_1)", [r"$-\dot{m}_1\left(e_1 + \tfrac{U_i^2}{2}\right)$", r"$+p_iU_i\frac{\pi D^2}{8}$", r"$0$", r"$0$"], False),
                      (r"\Sigma_i\ (T_2)", [r"$-\dot{m}_2\left(e_2 + \tfrac{U_i^2}{2}\right)$", r"$+p_iU_i\frac{\pi D^2}{8}$", r"$0$", r"$0$"], False),
                      (r"\Sigma_o", [r"$+\dot{m}\left(e_o + \tfrac{U_o^2}{2}\right)$", r"$-p_aU_oA$", r"$0$", r"$0$"], False),
                      (r"\Sigma_\ell", [r"$0$", r"$0$", r"$0$", r"$-\int_{\Sigma_\ell}\bar{q}\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed term: $\dot{Q}$. Combining with the pressure work, $h = c_pT$; the kinetic terms cancel ($U_o = U_i$, $\dot{m}_1 + \dot{m}_2 = \dot{m}$). Enthalpy fluxes: $\dot{m}_kc_pT_k = c_p\frac{p_i}{R_g}U_i\frac{\pi D^2}{8}$ for each inlet stream, so their sum is $c_p\frac{2p_a}{R_g}U_iA$; at the outlet $\dot{m}c_pT_o = c_p\frac{p_a}{R_g}U_iA$.",
                result=r"\dot{Q} = c_p\frac{p_a}{R_g}U_iA - c_p\frac{2p_a}{R_g}U_iA \;\Longrightarrow\; \boxed{\,\dot{Q} = -\frac{c_p}{R_g}\,p_aU_i\,\frac{\pi D^2}{4}\,} \tag{3}")),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"$\dot{Q} < 0$: heat leaves the gas through the wall. This is consistent with the data: $T_o = T_1T_2/(T_1 + T_2)$ is lower than both inlet temperatures, so the gas must be cooled (the official solution notes that the fluid is cooled down as it flows through the pipe).",
                r"The outlet velocity equals the inlet one because the density halves with the pressure ($p_a$ vs $2p_a$) while the temperature effect is exactly offset by the chosen $T_o$.",
                r"Dimensions (SI): $[p_aA] = \text{N}$; $[p_aU_i^2A/(R_gT)] = \text{N}$; $[c_pp_aU_iA/R_g] = \text{W}$.",
                rf"Numerical illustration (hypothetical data): $p_a = 101325$ Pa, $U_i = 20$ m/s, $T_1 = 300$ K, $T_2 = 400$ K ($T_o = {f(_To19,5)}$ K), $D = 0.1$ m, $R_g = 287$ J/(kg K), $c_p = 1005$ J/(kg K) give $F_x = {f(_Fx19)}$ N, $F_y = {f(_Fy19,4)}$ N and $\dot{{Q}} = {f(_Q19)}$ W.",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL20
_r20, _c20, _D20, _d20, _vu20, _pu20, _pa20 = 1000., 4186., 0.1, 0.04, 1.0, 1.21e5, 101325.
_vd20 = (_D20 / _d20) ** 2 * _vu20
_F20 = math.pi * _D20 ** 2 / 4 * (_pu20 - _pa20 - _r20 * _vu20 ** 2 * ((_D20 / _d20) ** 2 - 1))
_dT20 = ((_pu20 / _r20 + _vu20 ** 2 / 2) - (_pa20 / _r20 + _vd20 ** 2 / 2)) / _c20
_Fb20 = math.pi * _D20 ** 2 / 8 * _r20 * _vu20 ** 2 * ((_D20 / _d20) ** 2 - 1) ** 2
CL20 = dict(
    id="cl20", pill="CL20: Contraction",
    title="Pipe Contraction Discharging to the Atmosphere: Velocity, Force and Heating",
    note_title="Problem - CL20 Pipe Contraction",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "energia", "contraccion"],
    tags_html=["Nozzle", "Linear momentum", "Energy", "Bernoulli limit"],
    statement=[
        ("p", r"A liquid of density $\rho$ and specific heat $c$ flows steadily along a circular pipe of diameter $D$, discharging to the atmosphere, at pressure $p_a$, through a coaxial contraction that ends with a circular orifice of diameter $d$. Upstream from the contraction, the velocity, pressure, and temperature have known uniform values $v_u$, $p_u$, and $T_u$. As a function of these data ($\rho$, $c$, $D$, $d$, $p_a$, $v_u$, $p_u$, $T_u$), obtain explicit expressions for:"),
        ("ul", [r"The value of the discharge velocity $v_d$.", r"The force acting on the contraction $F$, neglecting in the calculation the effect of gravity.", r"The temperature increment $T_d - T_u$. Assume in the calculation that the contraction wall is adiabatic."]),
        ("p", r"Simplify these last two results by further assuming that the effect of viscosity is entirely negligible, so that for this incompressible steady flow Bernoulli's equation can be used to relate the variation of the fluid properties along a given stream line."),
    ],
    source_line=r"Source: CL20.pdf (page 1, final of Jan 21, 2014). Notes.pdf: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46, Bernoulli's equation Eq. 4.17.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady, incompressible liquid, $e = cT$; neglect $\bar{g}$; uniform properties at the upstream section $u$ and at the orifice $d$; adiabatic contraction; free jet at $p_a$.",
                r"Data: $[\rho,\ c,\ D,\ d,\ p_a,\ v_u,\ p_u,\ T_u]$. Unknowns: $[v_d,\ \bar{F},\ T_d - T_u]$, first in general and then in the inviscid (Bernoulli) limit.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$D$, $d$", "pipe and orifice diameters", "m"],
                [r"$v_u$, $p_u$, $T_u$", "upstream state", "m/s, Pa, K"],
                [r"$v_d$, $T_d$", "discharge velocity and temperature", "m/s, K"],
                [r"$\bar{F}$", "force on the contraction", "N"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the contraction, $\bar{e}_x$ along the axis. Fixed control volume: the liquid inside the contraction.",
                r"Surfaces: $\Sigma_u$ (upstream section, $\bar{n} = -\bar{e}_x$, area $\pi D^2/4$), $\Sigma_d$ (orifice, $\bar{n} = +\bar{e}_x$, area $\pi d^2/4$), $\Sigma_w$ (contraction wall, outer face at $p_a$).",
            ]),
            ("m", r"\boxed{\,\bar{F} = \int_{\Sigma_w}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="1. Mass (Notes Eq. 3.11)", eq=mass_eq(), cols=[COL_MASS],
                rows=[(r"\Sigma_u", [r"$-\rho v_u\frac{\pi D^2}{4}$"], False), (r"\Sigma_d", [r"$+\rho v_d\frac{\pi d^2}{4}$"], False), (r"\Sigma_w", [r"$0$"], False)],
                result=r"\boxed{\,v_d = \left(\frac{D}{d}\right)^2v_u\,} \tag{1}")),
            ("bal", dict(
                label="2. Linear momentum (Notes Eq. 3.36)", eq=MOM_FIXED_NOG, cols=[COL_MFLUX, COL_P, COL_TAU],
                rows=[(r"\Sigma_u", [r"$-\rho v_u^2\frac{\pi D^2}{4}\bar{e}_x$", r"$(p_u - p_a)\frac{\pi D^2}{4}\bar{e}_x$", r"$0$"], False),
                      (r"\Sigma_d", [r"$+\rho v_d^2\frac{\pi d^2}{4}\bar{e}_x = \rho v_uv_d\frac{\pi D^2}{4}\bar{e}_x$", r"$0$ (free jet)", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$", r"$\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed terms: $-\bar{F}$. The $\Sigma_d$ flux uses (1).",
                result=r"\rho\frac{\pi D^2}{4}v_u(v_d - v_u)\,\bar{e}_x = (p_u - p_a)\frac{\pi D^2}{4}\bar{e}_x - \bar{F} \;\Longrightarrow\; \boxed{\,\bar{F} = \frac{\pi D^2}{4}\left\{p_u - p_a - \rho v_u^2\left[\left(\frac{D}{d}\right)^2 - 1\right]\right\}\bar{e}_x\,} \tag{2}")),
            ("bal", dict(
                label="3. Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False), cols=ENERGY_COLS,
                rows=[(r"\Sigma_u", [r"$-\dot{m}\left(cT_u + \tfrac{v_u^2}{2}\right)$", r"$+p_uv_u\frac{\pi D^2}{4}$", r"$0$", r"$0$"], False),
                      (r"\Sigma_d", [r"$+\dot{m}\left(cT_d + \tfrac{v_d^2}{2}\right)$", r"$-p_av_d\frac{\pi d^2}{4}$", r"$0$", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$0$", r"$0$", r"$0$ (adiabatic)"], False)],
                wall=r"With $\dot{m} = \rho v_u\pi D^2/4 = \rho v_d\pi d^2/4$, dividing by $\dot{m}c$:",
                result=r"\boxed{\,T_d - T_u = \frac{1}{c}\left[\left(\frac{p_u}{\rho} + \frac{v_u^2}{2}\right) - \left(\frac{p_a}{\rho} + \frac{v_d^2}{2}\right)\right]\,} \tag{3}")),
            ("h4", "4. Inviscid limit (Bernoulli)"),
            ("p", r"Without viscosity, Bernoulli (Notes Eq. 4.17) along a streamline from $u$ to $d$ gives $\frac{p_u}{\rho} + \frac{v_u^2}{2} = \frac{p_a}{\rho} + \frac{v_d^2}{2}$, i.e. $p_u - p_a = \tfrac{1}{2}\rho v_u^2\left[\left(\frac{D}{d}\right)^4 - 1\right]$. Substituting into (2), with $\left(\frac{D}{d}\right)^4 - 2\left(\frac{D}{d}\right)^2 + 1 = \left[\left(\frac{D}{d}\right)^2 - 1\right]^2$, and into (3):"),
            ("m", r"\boxed{\,\bar{F} = \frac{\pi D^2}{8}\,\rho v_u^2\left[\left(\frac{D}{d}\right)^2 - 1\right]^2\bar{e}_x,\qquad T_d - T_u = 0\,} \tag{4}"),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"(3): the temperature rise measures the loss of mechanical energy (total pressure) by viscous dissipation; without viscosity it is zero, (4).",
                r"In the inviscid limit $\bar{F}$ points downstream and is always positive: the contraction is pulled along the flow. For $d \to D$, $\bar{F} \to 0$.",
                r"Dimensions (SI): $[\rho v^2D^2] = \text{N}$; $[(p/\rho + v^2/2)/c] = \text{K}$.",
                rf"Numerical illustration (hypothetical data): water, $D = 0.1$ m, $d = 0.04$ m, $v_u = 1$ m/s, $p_u = 1.21\times10^5$ Pa, $p_a = 101325$ Pa: $v_d = {f(_vd20)}$ m/s, $F = {f(_F20)}$ N and $T_d - T_u = {f(_dT20*1000,3)}$ mK (some loss); the inviscid value is $F = {f(_Fb20)}$ N (it needs $p_u - p_a = 19031$ Pa).",
                r"Agreement with the official solution: CL20.pdf obtains (1) to (4).",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL21
_r121, _U121, _p121, _U221, _p221, _R21 = 1.2, 30., 101325., 31., 101000., 0.01
_r221 = _r121 * _U121 / _U221
_F21 = (_p121 - _p221 + _r121 * _U121 * (_U121 - _U221)) * 3 * _R21
_Q21 = _r121 * _U121 * 3 * _R21 * (GAM / (GAM - 1) * (_p221 * _U221 / (_r121 * _U121) - _p121 / _r121) + 0.5 * (_U221 ** 2 - _U121 ** 2))
CL21 = dict(
    id="cl21", pill="CL21: Hot Cylinders",
    title="Array of Hot Cylinders in a Gas Stream: Density, Force and Heat",
    note_title="Problem - CL21 Array of Hot Cylinders",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "energia", "cilindros"],
    tags_html=["Periodicity", "Drag", "Heat release", "Perfect gas"],
    statement=[
        ("p", r"A linear array of parallel hot cylinders of radius $R$, whose centers are separated a distance $3R$, is placed perpendicular to a gas stream with velocity $U_1$, density $\rho_1$, and pressure $p_1$, as indicated in the figure of CL21.pdf. Sufficiently far downstream the gas properties recover uniform values, including a velocity $U_2$ and a pressure $p_2$. Assume that the effect of gravity is negligible. In terms of the quantities indicated in the figure, determine:"),
        ("ul", [r"The value of the density downstream from the array of cylinders.", r"The force acting on each cylinder (per unit length).", r"The heat transferred from each cylinder to the gas stream per unit time (per unit length). Express the result with use made of the ratio of specific heats $\gamma$."]),
        ("p", r"NOTE: Explain clearly the simplifications and assumptions employed in the derivation."),
    ],
    source_line=r"Source: CL21.pdf (page 1, retake of Jun 13, 2014). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady, planar (per unit length of cylinder); neglect $\bar{g}$; perfect gas, $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$; uniform states far upstream (1) and far downstream (2), where viscous stresses and conduction vanish.",
                r"Infinite array: the flow is periodic in $y$ with period $3R$ and symmetric about each cylinder axis, so the downstream velocity stays along $\bar{e}_x$ (no lift).",
                r"Cylinders at rest (no work); they release heat to the gas.",
                r"Data: $[\rho_1,\ U_1,\ p_1,\ U_2,\ p_2,\ R,\ \gamma]$. Unknowns: $[\rho_2,\ \bar{F},\ \dot{Q}]$ per unit length.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$U_1$, $\rho_1$, $p_1$", "upstream state", r"m/s, kg/m$^3$, Pa"],
                [r"$U_2$, $\rho_2$, $p_2$", "downstream state", r"m/s, kg/m$^3$, Pa"],
                [r"$R$", "cylinder radius (spacing $3R$)", "m"],
                [r"$\bar{F}$, $\dot{Q}$", "force and heat per unit length", "N/m, W/m"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the array; $\bar{e}_x$ along the stream. Fixed control volume of height $3R$ around one cylinder (as in the official figure).",
                r"Surfaces: $\Sigma_1$ (far upstream, $\bar{n} = -\bar{e}_x$), $\Sigma_2$ (far downstream, $\bar{n} = +\bar{e}_x$), $\Sigma_{top}$ and $\Sigma_{bot}$ (lines midway between cylinders, $\bar{n} = \pm\bar{e}_y$) and $\Sigma_{cyl}$ (cylinder surface). By periodicity every flux through $\Sigma_{top}$ equals minus the one through $\Sigma_{bot}$: they cancel each other out.",
            ]),
            ("m", r"\boxed{\,\bar{F} = \int_{\Sigma_{cyl}}\left[p\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
            ("m", r"\boxed{\,\dot{Q} = -\int_{\Sigma_{cyl}}\bar{q}\cdot\bar{n}\,d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="1. Mass (Notes Eq. 3.11)", eq=mass_eq(), cols=[COL_MASS],
                rows=[(r"\Sigma_1", [r"$-\rho_1U_1\,3R$"], False), (r"\Sigma_2", [r"$+\rho_2U_2\,3R$"], False), (r"\Sigma_{top} + \Sigma_{bot}", [r"$0$ (cancel each other out)"], False), (r"\Sigma_{cyl}", [r"$0$"], False)],
                result=r"\boxed{\,\rho_2 = \frac{U_1}{U_2}\,\rho_1\,} \tag{1}")),
            ("bal", dict(
                label="2. Linear momentum (Notes Eq. 3.36)", eq=MOM_FIXED_NOG.replace("(p - p_a)", "p"), cols=[COL_MFLUX, r"-\int p\,\bar{n}\,d\sigma", COL_TAU],
                rows=[(r"\Sigma_1", [r"$-\rho_1U_1^2\,3R\,\bar{e}_x$", r"$+p_1\,3R\,\bar{e}_x$", r"$0$"], False),
                      (r"\Sigma_2", [r"$+\rho_2U_2^2\,3R\,\bar{e}_x$", r"$-p_2\,3R\,\bar{e}_x$", r"$0$"], False),
                      (r"\Sigma_{top} + \Sigma_{bot}", [r"$0$", r"$0$", r"$0$ (cancel each other out)"], False),
                      (r"\Sigma_{cyl}", [r"$0$", r"$-\int_{\Sigma_{cyl}}p\,\bar{n}\,d\sigma$", r"$\int_{\Sigma_{cyl}}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed terms: $-\bar{F}$. With (1), $\rho_2U_2^2 = \rho_1U_1U_2$.",
                result=r"\boxed{\,\frac{\bar{F}}{3R} = \left[p_1 - p_2 + \rho_1U_1^2\left(1 - \frac{U_2}{U_1}\right)\right]\bar{e}_x\,} \tag{2}")),
            ("bal", dict(
                label="3. Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False), cols=ENERGY_COLS,
                rows=[(r"\Sigma_1", [r"$-\rho_1U_1\,3R\left(e_1 + \tfrac{U_1^2}{2}\right)$", r"$+p_1U_1\,3R$", r"$0$", r"$0$"], False),
                      (r"\Sigma_2", [r"$+\rho_2U_2\,3R\left(e_2 + \tfrac{U_2^2}{2}\right)$", r"$-p_2U_2\,3R$", r"$0$", r"$0$"], False),
                      (r"\Sigma_{top} + \Sigma_{bot}", [r"$0$", r"$0$", r"$0$", r"$0$ (cancel each other out)"], False),
                      (r"\Sigma_{cyl}", [r"$0$", r"$0$ ($\bar{v} = 0$)", r"$0$", r"$-\int_{\Sigma_{cyl}}\bar{q}\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed term: $\dot{Q}$. With $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$ and $\frac{p_2}{\rho_2} = \frac{p_2U_2}{\rho_1U_1}$ from (1):",
                result=r"\boxed{\,\dot{Q} = \rho_1U_1\,3R\left[\frac{\gamma}{\gamma - 1}\left(\frac{p_2U_2}{\rho_1U_1} - \frac{p_1}{\rho_1}\right) + \frac{1}{2}\left(U_2^2 - U_1^2\right)\right]\,} \tag{3}")),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"Heating expands the gas: $\rho_2 < \rho_1$ requires $U_2 > U_1$ (1). The drag (2) combines the pressure drop across the array with the momentum change.",
                r"Without heat ($\dot{Q} = 0$) and without drag, (1) to (3) are satisfied by state 2 = state 1.",
                r"Dimensions (SI, per unit length): $[(p + \rho U^2)R] = \text{N/m}$; $[\rho UR\,p/\rho] = \text{W/m}$.",
                rf"Numerical illustration (hypothetical data): $\rho_1 = 1.2$ kg/m$^3$, $U_1 = 30$ m/s, $p_1 = 101325$ Pa, $U_2 = 31$ m/s, $p_2 = 101000$ Pa, $R = 0.01$ m, $\gamma = 1.4$ give $\rho_2 = {f(_r221)}$ kg/m$^3$, $F/L = {f(_F21)}$ N/m and $\dot{{Q}}/L = {f(_Q21)}$ W/m.",
                r"Agreement with the official solution: CL21.pdf obtains (1), (2) and (3) (the handwritten correction in (3) replaces $1/\rho_2$ by $U_2/(\rho_1U_1)$, as here).",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL22
CL22 = dict(
    id="cl22", pill="CL22: Shrinking Cylinder",
    title="Water in a Shrinking Cylinder: Level, Velocity, Force and Power",
    note_title="Problem - CL22 Water in a Shrinking Cylinder",
    difficulty="alta",
    tags_md=["problema-examen", "leyes-de-conservacion", "volumen-de-control-movil", "energia-cinetica", "no-estacionario"],
    tags_html=["Unsteady", "Deforming CV", "Kinetic energy", "Power"],
    statement=[
        ("p", r"Figure (a) of CL22.pdf shows a cylinder of radius $a_0$ closed at the bottom that contains a volume $\pi a_0^2h_0$ of water. The water is in contact with the stagnant atmosphere at a pressure $p_a$. At time $t = 0$ the cylinder radius $a(t)$ starts decreasing and the level of water rises, as shown in figure (b) for a generic instant of time $t$. If $a(t)$ is known,"),
        ("ul", [
            r"Define clearly a control volume and use the mass conservation principle to determine the level of water $h(t)$ and the velocity of the free surface $\dot{h}(t)$ for a generic instant of time $t$.",
            r"Using control volume $V_2$, as shown in the figure (b), use the continuity equation to obtain the $z$-component of the velocity $v_z(z,t)$ in the liquid at an arbitrary level $z$, as sketched in figure b.",
            r"Using the previous results, and specifying the control volume used in the analysis, determine separately the force exerted by both the liquid and the atmosphere on the cylinder. Calculate the net force exerted by both fluids on the cylinder.",
            r"Using the kinetic energy equation, and neglecting $v_r^2$ in the kinetic energy, obtain the mechanical power exerted on the solid walls by both the liquid and the atmosphere. Determine the net power exerted by both fluids on the liquid.",
        ]),
        ("p", r"Note: Neglect viscous dissipation within the liquid, viscous stresses at the free surface and take the pressure in the air as a constant $p_a$."),
    ],
    source_line=r"Source: CL22.pdf (pages 1-3, exam of 28-10-2018, with handwritten solution). Notes.pdf, Chapter 3: Reynolds transport theorem for a moving control volume Eqs. 3.7-3.8, integral mass balance Eq. 3.10, integral momentum balance Eq. 3.35, energy balance Eq. 3.46.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Unsteady flow of an incompressible liquid (water, $\rho$ constant) with gravity $\bar{g} = -g\bar{e}_z$ (here gravity is kept); viscous dissipation and stresses at the free surface neglected; air at constant $p_a$.",
                r"The radius $a(t)$ is a known function with $a(0) = a_0$, $\dot{a} < 0$; the bottom is fixed at $z = 0$; the free surface stays flat at $z = h(t)$.",
                r"The axial velocity is assumed uniform over each horizontal section, $v_z(z,t)$, and the kinetic energy of the radial motion ($v_r^2$) is neglected (statement).",
                r"Data: $[a(t),\ a_0,\ h_0,\ \rho,\ g,\ p_a]$. Unknowns: $[h,\ \dot{h},\ v_z,\ F_{L\to W},\ F_{A\to W},\ \dot{W}_{L\to W},\ \dot{W}_{A\to W}]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$a(t)$, $a_0$", "cylinder radius, initial radius", "m"],
                [r"$h(t)$, $h_0$", "water level, initial level", "m"],
                [r"$v_z(z,t)$", "axial velocity of the water", "m/s"],
                [r"$F$", "axial force on the cylinder", "N"],
                [r"$\dot{W}$", "mechanical power on the walls", "W"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volumes and Surfaces", [
            ("ul", [
                r"Inertial frame fixed to the bottom; cylindrical coordinates $(r, \theta, z)$, $\bar{e}_z$ upwards.",
                r"Control volume 1 (the water itself, a material volume): $\Sigma_s$ (free surface, $\bar{v} = \bar{v}_c = \dot{h}\bar{e}_z$, $\bar{n} = \bar{e}_z$), $\Sigma_L$ (lateral wall, $\bar{v} = \bar{v}_c = \dot{a}\bar{e}_r$, $\bar{n} = \bar{e}_r$) and $\Sigma_b$ (bottom, $\bar{v} = \bar{v}_c = 0$, $\bar{n} = -\bar{e}_z$). Everywhere $\bar{v} = \bar{v}_c$, so no flux crosses $\Sigma_c$.",
                r"Control volume $V_2$: from the bottom to a fixed level $z$: $\Sigma_b$, $\Sigma_{L2}$ (lateral wall, moving with $\dot{a}\bar{e}_r$) and $\Sigma_z$ (fixed horizontal section, $\bar{v}_c = 0$, $\bar{n} = \bar{e}_z$).",
                r"Axial forces on the cylinder: $F_{L\to W}$ (liquid on $\Sigma_L$, $\Sigma_b$) and $F_{A\to W}$ (atmosphere on the outer surface: radial on the lateral wall, $+p_a\pi a^2$ on the outer face of the bottom; the air inside above the water also pushes only radially).",
            ]),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="1. Mass on control volume 1 (Notes Eq. 3.10)", eq=r"\frac{d}{dt}\int_{V_c(t)}\rho\,dV + \int_{\Sigma_c(t)}\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma = 0",
                cols=[r"\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma"],
                rows=[(r"\Sigma_s", [r"$0$ ($\bar{v} = \bar{v}_c = \dot{h}\bar{e}_z$)"], False), (r"\Sigma_L", [r"$0$ ($\bar{v} = \bar{v}_c = \dot{a}\bar{e}_r$)"], False), (r"\Sigma_b", [r"$0$ ($\bar{v} = \bar{v}_c = 0$)"], False)],
                wall=r"Therefore $\frac{d}{dt}\left[\rho\pi a^2h\right] = 0$ and $\rho\pi a^2(t)h(t) = \rho\pi a_0^2h_0$. Differentiating $h = a_0^2h_0a^{-2}$ with the chain rule, $\frac{dh}{dt} = a_0^2h_0\,(-2)a^{-3}\dot{a}$:",
                result=r"\boxed{\,h(t) = \frac{a_0^2}{a^2(t)}\,h_0\,}\ \ \text{(1)}\qquad \boxed{\,\dot{h} = -\frac{2a_0^2h_0\,\dot{a}}{a^3} = -2h\,\frac{\dot{a}}{a}\,}\ \ \text{(2)}")),
            ("bal", dict(
                label="2. Mass on V₂ (Notes Eq. 3.10)", eq=r"\frac{d}{dt}\int_{V_2(t)}\rho\,dV + \int_{\Sigma_2(t)}\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma = 0",
                cols=[r"\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma"],
                rows=[(r"\Sigma_z", [r"$\rho\,v_z\,\pi a^2$ ($\bar{v}_c = 0$)"], False), (r"\Sigma_{L2}", [r"$0$ ($\bar{v} = \bar{v}_c$)"], False), (r"\Sigma_b", [r"$0$"], False)],
                wall=r"Volume term: $\frac{d}{dt}(\rho\pi a^2z) = \rho\pi z\frac{d(a^2)}{dt} = 2\rho\pi za\dot{a}$ ($z$ fixed).",
                result=r"2\rho\pi za\dot{a} + \rho v_z\pi a^2 = 0 \;\Longrightarrow\; \boxed{\,v_z(z,t) = -\frac{1}{a^2}\frac{d(a^2)}{dt}\,z = -\frac{2\dot{a}(t)}{a(t)}\,z\,} \tag{3}")),
            ("p", r"Check: at $z = h$, $v_z = -2\dot{a}h/a = \dot{h}$, the velocity of the free surface (2). It is also consistent with the differential continuity equation: with $v_r = \dot{a}r/a$ (so that $v_r = \dot{a}$ at the wall), $\frac{1}{r}\frac{\partial(rv_r)}{\partial r} + \frac{\partial v_z}{\partial z} = \frac{2\dot{a}}{a} - \frac{2\dot{a}}{a} = 0$ (extension)."),
            ("bal", dict(
                label="3. Momentum, z component, on control volume 1 (Notes Eq. 3.35)",
                eq=r"\frac{d}{dt}\int_{V_c}\rho v_z\,dV + " + crossed(r"\int_{\Sigma_c}\rho v_z\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma", "0") + r" = -\int_{\Sigma_c}p\,n_z\,d\sigma + \int_{\Sigma_c}(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma - \int_{V_c}\rho g\,dV",
                cols=[r"-\int p\,n_z\,d\sigma", r"\int(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma"],
                rows=[(r"\Sigma_s", [r"$-p_a\pi a^2$", r"$0$ (neglected)"], False),
                      (r"\Sigma_L", [r"$-\int_{\Sigma_L}p\,n_z\,d\sigma$", r"$\int_{\Sigma_L}(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma$"], True),
                      (r"\Sigma_b", [r"$-\int_{\Sigma_b}p\,n_z\,d\sigma$", r"$\int_{\Sigma_b}(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma$"], True)],
                wall=r"Boxed $\Sigma_L$, $\Sigma_b$ terms: the force of the walls on the liquid, $-F_{L\to W}$. Volume terms: $\int_{V_c}\rho v_z\,dV = \int_0^h\rho\left(-\frac{2\dot{a}}{a}z\right)\pi a^2\,dz = -2\rho\pi a\dot{a}\left[\frac{z^2}{2}\right]_0^h = -\rho\pi a\dot{a}h^2$, and the weight $\rho g\pi a_0^2h_0$.",
                result=r"\frac{d}{dt}\left(-\rho\pi a\dot{a}h^2\right) = -F_{L\to W} - p_a\pi a^2 - \rho g\pi a_0^2h_0 \tag{4}")),
            ("p", r"Product rule: $\frac{d}{dt}(a\dot{a}h^2) = \dot{a}^2h^2 + a\ddot{a}h^2 + 2a\dot{a}h\dot{h}$, and with (2), $2a\dot{a}h\dot{h} = 2a\dot{a}h\left(-2h\frac{\dot{a}}{a}\right) = -4\dot{a}^2h^2$, so $\frac{d}{dt}(a\dot{a}h^2) = h^2\left(a\ddot{a} - 3\dot{a}^2\right)$ with $h^2 = \frac{a_0^4h_0^2}{a^4}$ from (1). From (4):"),
            ("m", r"\boxed{\,F_{L\to W} = \rho\pi\,\frac{a_0^4h_0^2}{a^4}\left(a\ddot{a} - 3\dot{a}^2\right) - p_a\pi a^2 - \rho g\pi a_0^2h_0\,} \tag{5}"),
            ("m", r"\boxed{\,F_{A\to W} = p_a\pi a^2\,}"),
            ("m", r"\boxed{\,F = F_{L\to W} + F_{A\to W} = \rho\pi a_0^2\left[\frac{a_0^2h_0^2}{a^4}\left(a\ddot{a} - 3\dot{a}^2\right) - gh_0\right]\,} \tag{6}"),
            ("bal", dict(
                label="4. Kinetic energy on control volume 1",
                eq=r"\frac{d}{dt}\int_{V_c}\rho\frac{v_z^2}{2}\,dV + " + crossed(r"\int_{\Sigma_c}\rho\frac{v^2}{2}(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma", "0") + r" = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV + " + crossed(r"\int_{V_c}p\,\nabla\cdot\bar{v}\,dV", r"0\ (\text{incompressible})") + r" - " + crossed(r"\int_{V_c}\Phi_v\,dV", r"\text{neglect}"),
                cols=[r"-\int p\,\bar{v}\cdot\bar{n}\,d\sigma", r"\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma"],
                rows=[(r"\Sigma_s", [r"$-p_a\dot{h}\,\pi a^2$", r"$0$ (neglected)"], False),
                      (r"\Sigma_L", [r"$-\int_{\Sigma_L}p\,\dot{a}\,d\sigma$", r"$\int_{\Sigma_L}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$"], True),
                      (r"\Sigma_b", [r"$0$ ($\bar{v} = 0$)", r"$0$ ($\bar{v} = 0$)"], False)],
                wall=r"Boxed $\Sigma_L$ terms: the power of the walls on the liquid, $-\dot{W}_{L\to W}$. Volume terms: $\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV = -\rho g\int_0^hv_z\pi a^2\,dz = \rho g\pi a\dot{a}h^2$ and $\int_{V_c}\rho\frac{v_z^2}{2}dV = \frac{\rho\pi a^2}{2}\frac{4\dot{a}^2}{a^2}\left[\frac{z^3}{3}\right]_0^h = \frac{2}{3}\rho\pi\dot{a}^2h^3$.",
                result=r"\frac{d}{dt}\left(\frac{2}{3}\rho\pi\dot{a}^2h^3\right) = -\dot{W}_{L\to W} - p_a\pi a^2\dot{h} + \rho g\pi a\dot{a}h^2 \tag{7}")),
            ("p", r"Chain and product rule with (2): $\frac{d}{dt}(\dot{a}^2h^3) = 2\dot{a}\ddot{a}h^3 + 3\dot{a}^2h^2\dot{h} = 2\dot{a}\ddot{a}h^3 - 6\dot{a}^3\frac{h^3}{a} = 2h^3\dot{a}\left(\ddot{a} - 3\frac{\dot{a}^2}{a}\right)$, with $h^3 = \frac{a_0^6h_0^3}{a^6}$; and $-p_a\pi a^2\dot{h} = 2p_a\pi\frac{a_0^2}{a}h_0\dot{a}$. From (7):"),
            ("m", r"\boxed{\,\dot{W}_{L\to W} = -\frac{4}{3}\rho\pi\left(\frac{a_0}{a}\right)^6h_0^3\,\dot{a}\left(\ddot{a} - \frac{3\dot{a}^2}{a}\right) + 2p_a\pi\frac{a_0^2}{a}h_0\,\dot{a} + \rho g\pi a\dot{a}h^2\,} \tag{8}"),
            ("p", r"Atmosphere on the walls: only the outer lateral surface below the water level moves against an unbalanced $p_a$ (above the level, the air acts on both faces), and the bottom does not move: $\dot{W}_{A\to W} = -\int p_a\,\bar{v}\cdot\bar{n}_{out}\,d\sigma = -p_a\dot{a}\,2\pi ah$:"),
            ("m", r"\boxed{\,\dot{W}_{A\to W} = -2p_a\pi\frac{a_0^2}{a}h_0\,\dot{a}\,}"),
            ("m", r"\boxed{\,\dot{W} = \dot{W}_{L\to W} + \dot{W}_{A\to W} = -\frac{4}{3}\rho\pi\left(\frac{a_0}{a}\right)^6h_0^3\,\dot{a}\left(\ddot{a} - \frac{3\dot{a}^2}{a}\right) + \rho g\pi a\dot{a}h^2\,} \tag{9}"),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"At rest ($\dot{a} = \ddot{a} = 0$): $F_{L\to W} = -p_a\pi a^2 - \rho g\pi a_0^2h_0$ (the water and the air above it push the bottom down with $p_a$ and the weight), the atmosphere pushes the bottom up with $p_a\pi a^2$, and the net force is the weight. The ambient pressure cancels in the net force (6) and in the net power (9).",
                r"The term $\rho\pi\frac{a_0^4h_0^2}{a^4}(a\ddot{a} - 3\dot{a}^2)$ is minus the rate of change of the momentum of the water: the walls must accelerate the rising column.",
                r"The statement asks finally for 'the net power exerted by both fluids on the liquid'; from the context (and the official solution) the intended quantity is the net power of both fluids on the walls, (9).",
                r"Dimensions (SI): $[\rho a_0^4h_0^2\dot{a}^2/a^4] = \text{N}$; $[\rho(a_0/a)^6h_0^3\dot{a}\ddot{a}] = \text{W}$; $[p_aa_0^2h_0\dot{a}/a] = \text{W}$.",
                r"Numerical cross-check (hypothetical data): $a(t) = a_0(1 - 0.15t + 0.04t^2)$, $a_0 = 0.1$ m, $h_0 = 0.3$ m, $\rho = 1000$ kg/m$^3$ at $t = 0.7$ s: differentiating numerically the momentum and the kinetic energy of the water (quadrature of the integrals of 3 and 4) reproduces $F_{L\to W} = -2755.01$ N and $\dot{W}_{L\to W} = -199.696$ W from (5) and (8) to 12 digits; the net values are $F = -92.27$ N and $\dot{W} = -3.399$ W.",
                r"Agreement with the official solution: CL22.pdf obtains (1) to (9).",
            ]),
        ]),
    ],
)

PROBLEMS = [CL17, CL18, CL19, CL20, CL21, CL22]
