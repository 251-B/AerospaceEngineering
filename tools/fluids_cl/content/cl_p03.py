# CL11 to CL16 in the class style.
import math
from clcommon import *
from cl_p02 import ENERGY_COLS, energy_eq, mom_eq, mass_eq


# ---------------------------------------------------------------- CL11
def _cl11(rhoa, pa, Ai, Ae, Mg, WQ, g=GAM):
    def resid(Ue, al):
        Ui = 2 * Ue * math.sin(al); pi = pa - 0.5 * rhoa * Ui ** 2
        rhoe = rhoa * Ui * Ai / (Ue * Ae); md = rhoa * Ui * Ai
        return md * Ue * math.cos(al) - Mg, md * (g / (g - 1) * (pa / rhoe - pi / rhoa) + (Ue ** 2 - Ui ** 2) / 2) - WQ
    x = [100., 0.6]
    for _ in range(200):
        r = resid(*x)
        J = [[0, 0], [0, 0]]
        for j in range(2):
            d = [0, 0]; d[j] = 1e-6 * max(1, abs(x[j]))
            rp = resid(x[0] + d[0], x[1] + d[1])
            J[0][j] = (rp[0] - r[0]) / d[j]; J[1][j] = (rp[1] - r[1]) / d[j]
        det = J[0][0] * J[1][1] - J[0][1] * J[1][0]
        x = [x[0] - (J[1][1] * r[0] - J[0][1] * r[1]) / det, x[1] - (-J[1][0] * r[0] + J[0][0] * r[1]) / det]
    Ue, al = x
    Ui = 2 * Ue * math.sin(al)
    return Ue, math.degrees(al), Ui, pa - 0.5 * rhoa * Ui ** 2, rhoa * Ui * Ai / (Ue * Ae), resid(*x)


_Ue11, _al11, _Ui11, _pi11, _rhoe11, _res11 = _cl11(1.2, 101325., 2.5, 1.2, 8.0e4, 6.0e6)
CL11 = dict(
    id="cl11", pill="CL11: VTOL Engine",
    title="VTOL Propulsion Device in Hover: Nozzle Angle and Flow State",
    note_title="Problem - CL11 VTOL Propulsion Device",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "energia", "vtol"],
    tags_html=["Thrust vectoring", "Bernoulli", "Linear momentum", "Energy"],
    statement=[
        ("p", r"The propulsion device of a VTOL (vertical take-off and landing) aircraft includes a horizontal intake of cross section $A_i$ and a thrust vectoring nozzle of variable angle $\alpha$ and exit cross section $A_e$. When the aircraft is hovering (suspended at a fixed point), the engine must provide a force $\bar{F} = F_x\bar{e}_x + F_y\bar{e}_y$, such that the lift $F_y$ equals the weight of the aircraft ($Mg$), while the thrust $F_x$ is identically zero. The work per unit time on the air stream through the mobile blades is $W$ and the amount of heat added per unit time is $Q$ (including heat losses through the walls). For the analysis of the problem, one may introduce the following assumptions regarding the air motion:"),
        ("ul", [r"The effect of gravity is entirely negligible.", r"Flow properties at the entrance and exit sections are uniform.", r"The air around the engine casing is at rest with uniform pressure $p_a$.", r"Upstream from the inlet the flow is inviscid and with constant density, such that $\rho_i = \rho_a$ and one may use Bernoulli's equation along any streamline to relate the ambient pressure $p_a$ with that found at the entrance $p_i$."]),
        ("p", r"With the above simplifications, write the equations that determine the values of $U_i$, $U_e$, $p_i$, $\rho_e$ and $\alpha$ in terms of the known quantities ($p_a$, $Mg$, $\rho_a$, $A_i$, $A_e$, $\gamma$, $W$, and $Q$)."),
    ],
    source_line=r"Source: CL11.pdf (page 1). Notes.pdf: integral mass balance Eq. 3.10, integral momentum balance Eq. 3.35, integral total energy balance Eq. 3.46, Bernoulli's equation Eq. 4.17.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady (on average); neglect $\bar{g}$; uniform properties at $i$ and $e$; perfect gas, $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$; ambient air at rest at $p_a$ around the casing.",
                r"Inlet: $\rho_i = \rho_a$ (constant density upstream) and Bernoulli from the still air to the inlet. Exit: free jet at $p_a$, density $\rho_e$.",
                r"Geometry (figure): air enters along $-\bar{e}_x$ through the horizontal intake; the jet leaves downwards and backwards, $\bar{v}_e = -U_e(\sin\alpha\,\bar{e}_x + \cos\alpha\,\bar{e}_y)$, with $\alpha$ measured from the vertical.",
                r"Hover: $F_x = 0$, $F_y = Mg$. Data: $[p_a,\ \rho_a,\ Mg,\ A_i,\ A_e,\ \gamma,\ \dot{W},\ \dot{Q}]$. Unknowns: $[U_i,\ U_e,\ p_i,\ \rho_e,\ \alpha]$: five equations are needed.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$A_i$, $A_e$", "intake and exit areas", r"m$^2$"],
                [r"$U_i$, $U_e$", "intake and exit velocities", "m/s"],
                [r"$p_i$, $\rho_e$", "intake pressure, exit density", r"Pa, kg/m$^3$"],
                [r"$\alpha$", "nozzle angle from the vertical", "rad"],
                [r"$\dot{W}$, $\dot{Q}$", "power and heat given to the air", "W"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the hovering aircraft (inertial while hovering); $\bar{e}_x$ horizontal, $\bar{e}_y$ vertical upwards.",
                r"Surfaces: $\Sigma_i$ (intake, $\bar{n} = +\bar{e}_x$, $\bar{v} = -U_i\bar{e}_x$), $\Sigma_e$ (exit, $\bar{n} = \bar{v}_e/U_e$), $\Sigma_w$ (fixed walls) and $\Sigma_m$ (mobile blades).",
            ]),
            ("m", r"\boxed{\,\bar{F} = F_x\bar{e}_x + F_y\bar{e}_y = \int_{\Sigma_w,\Sigma_m}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}\qquad(\text{force of the air on the engine})"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="Mass (Notes Eq. 3.10)", eq=mass_eq(moving=True), cols=[r"\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma"],
                rows=[(r"\Sigma_i", [r"$\rho_a(-U_i)A_i$"], False), (r"\Sigma_e", [r"$+\rho_eU_eA_e$"], False), (r"\Sigma_w,\ \Sigma_m", [r"$0$"], False)],
                result=r"\boxed{\,\rho_aU_iA_i = \rho_eU_eA_e = \dot{m}\,} \tag{1}")),
            ("p", r"Entrance region (Notes Eq. 4.17, from the still ambient air to the inlet):"),
            ("m", r"\boxed{\,p_a = p_i + \tfrac{1}{2}\rho_aU_i^2\,} \tag{2}"),
            ("bal", dict(
                label="Linear momentum (Notes Eq. 3.35)", eq=mom_eq(moving=True), cols=[r"\int\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma", COL_P, COL_TAU],
                rows=[(r"\Sigma_i", [r"$\rho_a(-U_i\bar{e}_x)(-U_i)A_i = \rho_aU_i^2A_i\,\bar{e}_x$", r"$-(p_i - p_a)A_i\,\bar{e}_x$", r"$0$"], False),
                      (r"\Sigma_e", [r"$-\rho_eU_e^2A_e(\sin\alpha\,\bar{e}_x + \cos\alpha\,\bar{e}_y)$", r"$0$ (free jet)", r"$0$"], False),
                      (r"\Sigma_w,\ \Sigma_m", [r"$0$", r"$-\int(p - p_a)\,\bar{n}\,d\sigma$", r"$\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed terms: $-\bar{F} = -F_x\bar{e}_x - F_y\bar{e}_y$. $x$ component with $F_x = 0$, (2) and (1): $\rho_aU_i^2A_i - \rho_eU_e^2A_e\sin\alpha = \tfrac{1}{2}\rho_aU_i^2A_i$, i.e. $\tfrac{1}{2}\rho_aU_i^2A_i = \rho_aU_iA_i\,U_e\sin\alpha$. $y$ component with $F_y = Mg$: $-\rho_eU_e^2A_e\cos\alpha = -Mg$.",
                result=r"\boxed{\,U_i = 2\,U_e\sin\alpha\,}\ \ \text{(3)}\qquad \boxed{\,Mg = \rho_eU_e^2A_e\cos\alpha = \rho_aU_i^2A_i\,\frac{\cos\alpha}{2\sin\alpha}\,}\ \ \text{(4)}")),
            ("bal", dict(
                label="Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=True, moving=True), cols=ENERGY_COLS,
                rows=[(r"\Sigma_i", [r"$-\dot{m}\left(e_i + \tfrac{U_i^2}{2}\right)$", r"$+p_iU_iA_i$", r"$0$", r"$0$"], False),
                      (r"\Sigma_e", [r"$+\dot{m}\left(e_e + \tfrac{U_e^2}{2}\right)$", r"$-p_aU_eA_e$", r"$0$", r"$0$"], False),
                      (r"\Sigma_m", [r"$0$", r"$-\int_{\Sigma_m}p\,\bar{v}\cdot\bar{n}\,d\sigma$", r"$\int_{\Sigma_m}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$", r"$-\int_{\Sigma_m}\bar{q}\cdot\bar{n}\,d\sigma$"], True),
                      (r"\Sigma_w", [r"$0$", r"$0$", r"$0$", r"$-\int_{\Sigma_w}\bar{q}\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed terms: the work on $\Sigma_m$ is $\dot{W}$; the heat through the walls plus the volume term $\int_{V_c}Q_R\,dV$ is $\dot{Q}$ (net, including the losses). With $h = e + p/\rho = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$:",
                result=r"\boxed{\,\rho_aU_iA_i\left[\left(\frac{\gamma}{\gamma - 1}\frac{p_a}{\rho_e} + \frac{U_e^2}{2}\right) - \left(\frac{\gamma}{\gamma - 1}\frac{p_i}{\rho_a} + \frac{U_i^2}{2}\right)\right] = \dot{W} + \dot{Q}\,} \tag{5}")),
            ("p", r"(1) to (5) are five equations for $U_i$, $U_e$, $p_i$, $\rho_e$ and $\alpha$, which answers the question."),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"(3) says that the backward component of the jet momentum must cancel the intake momentum plus the suction force at the intake: because the intake is at a lower pressure than ambient (2), only half of $\rho_aU_i^2A_i$ has to be balanced.",
                r"(4): the lift is the vertical momentum flux of the jet. For $\alpha \to 0$ (vertical jet), (3) would require $U_i \to 0$: the intake momentum could not be balanced, so a hovering engine with a horizontal intake needs $\alpha > 0$.",
                r"Dimensions (SI): $[\rho_eU_e^2A_e] = \text{N} = [Mg]$; $[\dot{m}\,\gamma p/((\gamma-1)\rho)] = \text{W}$.",
                rf"Numerical illustration (hypothetical data, solved by Newton's method on the two equations left after eliminating $U_i$, $p_i$, $\rho_e$): $\rho_a = 1.2$ kg/m$^3$, $p_a = 101325$ Pa, $A_i = 2.5$ m$^2$, $A_e = 1.2$ m$^2$, $Mg = 80$ kN, $\dot{{W}} + \dot{{Q}} = 6$ MW, $\gamma = 1.4$ give $U_e = {f(_Ue11)}$ m/s, $\alpha = {f(_al11,4)}^\circ$, $U_i = {f(_Ui11)}$ m/s, $p_i = {f(_pi11,6)}$ Pa, $\rho_e = {f(_rhoe11)}$ kg/m$^3$ (residuals below $10^{{-6}}$).",
                r"Agreement with the official solution: CL11.pdf obtains (1) to (5).",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL12
_Vu, _pu, _Tu, _pa12, _Rg, _A12, _L12 = 50., 1.5e5, 400., 101325., 287., 0.01, 1.0
_c12 = _pu * _Vu / (_pa12 * _Tu)
_b12 = GAM * _Rg / (GAM - 1)
_H12 = _b12 * _Tu + 0.5 * _Vu ** 2
_To12 = (-_b12 + math.sqrt(_b12 ** 2 + 2 * _c12 ** 2 * _H12)) / _c12 ** 2
_Vo12 = _c12 * _To12
_rhou = _pu / (_Rg * _Tu)
_F12 = _rhou * _Vu * _A12 * (_Vu + _Vo12) + (_pu - _pa12) * _A12
_M12 = _rhou * _Vu * _A12 * _L12 * _Vo12
CL12 = dict(
    id="cl12", pill="CL12: Gas in a U-Pipe",
    title="Gas Discharging through an Inverted U-Pipe: Outlet State, Force and Moment",
    note_title="Problem - CL12 Gas through an Inverted U-Pipe",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "momento-angular", "gas"],
    tags_html=["Compressible", "Energy", "Linear momentum", "Angular momentum"],
    statement=[
        ("p", r"The gas circulating along the pipe of cross section $A$ depicted in the figure of CL12.pdf discharges to the atmosphere, where the pressure is $p_a$. Measurements at a given upstream location give $V_u$, $p_u$, and $T_u$ for the velocity, pressure and temperature, all uniform across the section. In the analysis that follows, it is assumed that the pipe is thermally insulated and that buoyancy forces have a negligible effect on the gas motion. The gas properties are defined by its gas constant $R_g$ together with the ratio of specific heats $\gamma = c_p/c_v$."),
        ("ul", [r"Obtain the values of the gas temperature and velocity at the outlet section $T_o$ and $V_o$ in terms of $V_u$, $p_u$, $T_u$, $p_a$, $R_g$ and $\gamma$.", r"Compute the two components of the force $F_x$ and $F_y$ acting on the stretch of pipe considered.", r"Calculate the momentum on the pipe with respect to the origin of the coordinate system indicated in the figure."]),
    ],
    source_line=r"Source: CL12.pdf (page 1, exam of Dec 16, 2011). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady compressible flow of a perfect gas ($p = \rho R_gT$, $h = c_pT = \frac{\gamma}{\gamma-1}R_gT$); neglect $\bar{g}$; pipe insulated and at rest (no heat, no work); uniform properties at both sections.",
                r"Geometry (figure): inverted U of constant section $A$; the gas goes up the left leg ($\bar{v} = V_u\bar{e}_y$ at the measuring section) and down the right leg, discharging as a free jet ($p = p_a$, $\bar{v} = -V_o\bar{e}_y$) at a horizontal distance $L$ from the left leg; the origin $O$ is on the axis of the left leg.",
                r"Data: $[V_u,\ p_u,\ T_u,\ p_a,\ R_g,\ \gamma,\ A,\ L]$. Unknowns: $[T_o,\ V_o,\ F_x,\ F_y,\ \bar{M}]$. The 'momentum on the pipe' of the statement is the moment of the forces on the pipe about $O$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$V_u$, $p_u$, $T_u$", "upstream state", "m/s, Pa, K"],
                [r"$V_o$, $T_o$", "outlet velocity and temperature", "m/s, K"],
                [r"$A$, $L$", "pipe section, distance between legs", r"m$^2$, m"],
                [r"$\bar{F}$, $\bar{M}$", "force and moment on the pipe", r"N, N$\cdot$m"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the pipe; $\bar{e}_x$ horizontal (from the left leg to the right leg), $\bar{e}_y$ vertical upwards, $\bar{e}_z = \bar{e}_x\wedge\bar{e}_y$ towards the reader. Fixed control volume.",
                r"Surfaces: $\Sigma_u$ (measuring section, $\bar{n} = -\bar{e}_y$), $\Sigma_o$ (outlet, $\bar{n} = -\bar{e}_y$), $\Sigma_w$ (inner wall). Positions: $\bar{x} = y\bar{e}_y + \bar{\eta}$ on $\Sigma_u$ and $\bar{x} = L\bar{e}_x + y\bar{e}_y + \bar{\eta}$ on $\Sigma_o$, with $\int\bar{\eta}\,d\sigma = 0$.",
            ]),
            ("m", r"\boxed{\,\bar{F} = \int_{\Sigma_w}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
            ("m", r"\boxed{\,\bar{M} = \int_{\Sigma_w}\bar{x}\wedge\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="Mass (Notes Eq. 3.11)", eq=mass_eq(), cols=[COL_MASS],
                rows=[(r"\Sigma_u", [r"$-\rho_uV_uA$, with $\rho_u = \frac{p_u}{R_gT_u}$"], False), (r"\Sigma_o", [r"$+\rho_oV_oA$, with $\rho_o = \frac{p_a}{R_gT_o}$"], False), (r"\Sigma_w", [r"$0$"], False)],
                result=r"\rho_uV_uA = \rho_oV_oA \;\Longrightarrow\; \boxed{\,\frac{p_uV_u}{T_u} = \frac{p_aV_o}{T_o}\,} \tag{1}")),
            ("bal", dict(
                label="Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False), cols=ENERGY_COLS,
                rows=[(r"\Sigma_u", [r"$-\dot{m}\left(e_u + \tfrac{V_u^2}{2}\right)$", r"$+p_uV_uA$", r"$0$", r"$0$"], False),
                      (r"\Sigma_o", [r"$+\dot{m}\left(e_o + \tfrac{V_o^2}{2}\right)$", r"$-p_aV_oA$", r"$0$", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$0$ ($\bar{v} = 0$)", r"$0$ ($\bar{v} = 0$)", r"$0$ (insulated)"], False)],
                result=r"\boxed{\,\frac{\gamma}{\gamma - 1}R_gT_u + \frac{1}{2}V_u^2 = \frac{\gamma}{\gamma - 1}R_gT_o + \frac{1}{2}V_o^2\,} \tag{2}")),
            ("p", r"Solving (1) and (2): with $C \equiv \frac{p_uV_u}{p_aT_u}$, (1) gives $V_o = C\,T_o$; substituting into (2), $\frac{C^2}{2}T_o^2 + \frac{\gamma R_g}{\gamma - 1}T_o - H = 0$ with $H = \frac{\gamma R_g}{\gamma - 1}T_u + \frac{V_u^2}{2}$, whose positive root is"),
            ("m", r"\boxed{\,T_o = \frac{-\frac{\gamma R_g}{\gamma - 1} + \sqrt{\left(\frac{\gamma R_g}{\gamma - 1}\right)^2 + 2C^2H}}{C^2},\qquad V_o = C\,T_o\,} \tag{3}"),
            ("bal", dict(
                label="Linear momentum (Notes Eq. 3.36)", eq=MOM_FIXED_NOG, cols=[COL_MFLUX, COL_P, COL_TAU],
                rows=[(r"\Sigma_u", [r"$\rho_uV_u\bar{e}_y(-V_u)A = -\rho_uV_u^2A\,\bar{e}_y$", r"$-(p_u - p_a)(-\bar{e}_y)A = (p_u - p_a)A\,\bar{e}_y$", r"$0$"], False),
                      (r"\Sigma_o", [r"$\rho_o(-V_o\bar{e}_y)(V_o)A = -\rho_uV_uA\,V_o\,\bar{e}_y$", r"$0$ (free jet)", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$", r"$\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed $\Sigma_w$ terms: $-\bar{F}$. The $\Sigma_o$ entry uses (1).",
                result=r"-\rho_uV_uA\,(V_u + V_o)\,\bar{e}_y = (p_u - p_a)A\,\bar{e}_y - \bar{F} \;\Longrightarrow\; \boxed{\,F_x = 0,\qquad F_y = \rho_uV_uA\,(V_u + V_o) + (p_u - p_a)A\,} \tag{4}")),
            ("bal", dict(
                label="Angular momentum about O (Notes Eq. 3.38)", eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho\,\bar{x}\wedge\bar{v}\,dV", "0") + r" + \int_{\Sigma_c}\rho\,(\bar{x}\wedge\bar{v})(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma",
                cols=[r"\int\rho\,(\bar{x}\wedge\bar{v})(\bar{v}\cdot\bar{n})\,d\sigma", r"-\int\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma", r"\int\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma"],
                rows=[(r"\Sigma_u", [r"$0$ ($y\bar{e}_y\wedge\bar{e}_y = 0$, $\int\bar{\eta}\,d\sigma = 0$)", r"$0$ (same reason)", r"$0$"], False),
                      (r"\Sigma_o", [r"$\rho_oV_oA\,(L\bar{e}_x\wedge(-V_o\bar{e}_y)) = -\rho_uV_uA\,LV_o\,\bar{e}_z$", r"$0$ (free jet)", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$-\int_{\Sigma_w}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma$", r"$\int_{\Sigma_w}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$"], True)],
                wall=r"Boxed $\Sigma_w$ terms: $-\bar{M}$.",
                result=r"-\rho_uV_uA\,LV_o\,\bar{e}_z = -\bar{M} \;\Longrightarrow\; \boxed{\,\bar{M} = \rho_uV_uA\,L\,V_o\,\bar{e}_z = \frac{p_u}{R_gT_u}V_uA\,L\,V_o\,\bar{e}_z\,} \tag{5}")),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"Adiabatic, workless flow keeps the stagnation enthalpy (2); the pressure drop to $p_a$ lowers the density, so the gas accelerates ($V_o > V_u$) and cools slightly ($T_o < T_u$).",
                r"Both legs push the pipe upwards: the gas turning down in the right leg and the gauge pressure at the measuring section. The moment comes only from the outlet jet, offset by $L$ from $O$.",
                r"Incompressible-like limit ($p_u \to p_a$, small $V$): $T_o \to T_u$, $V_o \to V_u$, $F_y \to 2\rho_uV_u^2A$.",
                r"Dimensions (SI): $[\rho_uV_u^2A] = \text{N}$; $[\rho_uV_uALV_o] = \text{N}\cdot\text{m}$; $[R_gT] = [V^2] = \text{m}^2/\text{s}^2$.",
                rf"Numerical illustration (hypothetical data, air): $V_u = 50$ m/s, $p_u = 1.5\times10^5$ Pa, $T_u = 400$ K, $p_a = 101325$ Pa, $R_g = 287$ J/(kg K), $\gamma = 1.4$, $A = 0.01$ m$^2$, $L = 1$ m give $T_o = {f(_To12,6)}$ K, $V_o = {f(_Vo12)}$ m/s, $F_y = {f(_F12)}$ N, $M_z = {f(_M12)}$ N$\cdot$m (residuals of (1), (2) below $10^{{-8}}$).",
                r"Agreement with the official solution: CL12.pdf obtains (1), (2), (4) and (5); it does not solve (1)-(2) explicitly.",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL13
_r13, _D13, _Do13, _h13, _a13, _Vo13, _po13, _ps13, _pa13 = 1000., 0.3, 0.1, 0.02, math.radians(30), 3., 1.2e5, 2.5e5, 101325.
_Vn13 = _Do13 ** 2 * _Vo13 / (4 * _D13 * _h13)
_Vs13 = _Vn13 / math.sin(_a13)
_md13 = _r13 * _Vo13 * math.pi * _Do13 ** 2 / 4
_F13 = math.pi * _Do13 ** 2 / 4 * (_r13 * _Vo13 ** 2 + _po13 - _pa13)
_M13 = _md13 * _D13 / 2 * _Vs13 * math.cos(_a13)
_W13 = _md13 * ((_ps13 - _po13) / _r13 + (_Vs13 ** 2 - _Vo13 ** 2) / 2)
CL13 = dict(
    id="cl13", pill="CL13: Centrifugal Pump",
    title="Centrifugal Pump: Exit Velocity, Axial Force, Torque and Power",
    note_title="Problem - CL13 Centrifugal Pump",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-angular", "energia", "bomba"],
    tags_html=["Turbomachine", "Angular momentum", "Euler torque", "Pump power"],
    statement=[
        ("p", r"The figure of CL13.pdf shows a sketch of a centrifugal pump. Water enters the pump with uniform axial velocity $V_o$ and pressure $p_o$ through a circular pipe of diameter $D_o$. The internal geometry of the pump includes rotating blades that redirect the flow, so that the water leaves the pump with zero axial velocity through a lateral exit of width $h$ and diameter $D$. At the exit section, the pressure is $p_s \ne p_a$ and the velocity vector, of magnitude $V_s$, forms an angle $\alpha$ with the lateral surface, as indicated in the figure, i.e., the corresponding normal and tangential velocity components are $V_s\sin\alpha$ and $V_s\cos\alpha$, respectively. Assuming that the effect of gravity is negligible and that the water temperature at the exit is equal to that found at the entrance (handwritten addition: and that the pump walls are insulated), determine the values of the:"),
        ("ul", [r"Radial velocity component at the exit section $V_s\sin\alpha$.", r"Axial force exerted on the pump.", r"Torque exerted on the pump.", r"Power of the pump, assumed to be ideal (i.e., work per unit time exerted on the water stream by the rotating parts)."]),
        ("p", r"Note: besides the water density $\rho$ and the ambient pressure $p_a$, the following quantities can be assumed to be known in solving the problem: $D$, $D_o$, $h$, $\alpha$, $V_o$, $p_o$, and $p_s$."),
    ],
    source_line=r"Source: CL13.pdf (page 1, exam of Jan 10, 2012). Notes.pdf, Chapter 3: integral mass balance Eq. 3.10, integral momentum balance Eq. 3.35, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady (on average), incompressible water; neglect $\bar{g}$; equal temperature at entrance and exit ($e_s = e_o$); insulated walls; uniform properties at both sections.",
                r"The outer casing is surrounded by air at $p_a$ (gauge pressure $p - p_a$ in the force).",
                r"Data: $[\rho,\ p_a,\ D,\ D_o,\ h,\ \alpha,\ V_o,\ p_o,\ p_s]$. Unknowns: $[V_s\sin\alpha,\ F_x,\ \bar{M},\ \dot{W}]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$D_o$, $V_o$, $p_o$", "inlet diameter, velocity, pressure", "m, m/s, Pa"],
                [r"$D$, $h$", "exit diameter and width", "m"],
                [r"$V_s$, $\alpha$, $p_s$", "exit velocity, angle, pressure", "m/s, rad, Pa"],
                [r"$\dot{W}$", "power given to the water by the blades", "W"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the casing; $\bar{e}_x$ along the axis (inlet flow direction); cylindrical basis $(\bar{e}_r, \bar{e}_\theta)$ around $\bar{e}_x$ with $\bar{e}_r\wedge\bar{e}_\theta = \bar{e}_x$; origin on the axis in the exit plane. Over a full turn, $\int\bar{e}_r\,d\theta = \int\bar{e}_\theta\,d\theta = 0$.",
                r"Surfaces: $\Sigma_o$ (inlet disc, $\bar{n} = -\bar{e}_x$), $\Sigma_s$ (lateral exit cylinder, radius $D/2$, width $h$, $\bar{n} = \bar{e}_r$, $\bar{v} = V_s\sin\alpha\,\bar{e}_r + V_s\cos\alpha\,\bar{e}_\theta$), $\Sigma_w$ (fixed casing) and $\Sigma_b$ (rotating blades).",
            ]),
            ("m", r"\boxed{\,\bar{F} = \int_{\Sigma_w,\Sigma_b}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
            ("m", r"\boxed{\bar{M} = \int_{\Sigma_w,\Sigma_b}\bar{x}\wedge\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="Mass (Notes Eq. 3.10)", eq=mass_eq(moving=True), cols=[r"\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma"],
                rows=[(r"\Sigma_o", [r"$-\rho V_o\frac{\pi D_o^2}{4}$"], False), (r"\Sigma_s", [r"$+\rho V_s\sin\alpha\,\pi Dh$"], False), (r"\Sigma_w,\ \Sigma_b", [r"$0$"], False)],
                result=r"\boxed{\,V_s\sin\alpha = \frac{D_o^2}{4Dh}\,V_o\,},\qquad \dot{m} = \rho V_o\frac{\pi D_o^2}{4} \tag{1}")),
            ("bal", dict(
                label="Linear momentum, axial component (Notes Eq. 3.35)", eq=mom_eq(moving=True), cols=[r"\int\rho v_x\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma", r"-\int(p - p_a)\,n_x\,d\sigma", r"\int(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma"],
                rows=[(r"\Sigma_o", [r"$-\rho V_o^2\frac{\pi D_o^2}{4}$", r"$+(p_o - p_a)\frac{\pi D_o^2}{4}$", r"$0$"], False),
                      (r"\Sigma_s", [r"$0$ ($v_x = 0$)", r"$0$ ($n_x = 0$)", r"$0$"], False),
                      (r"\Sigma_w,\ \Sigma_b", [r"$0$", r"$-\int(p - p_a)\,n_x\,d\sigma$", r"$\int(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma$"], True)],
                wall=r"Boxed terms: $-F_x$. The radial and azimuthal components vanish because $\int\bar{e}_r\,d\theta = \int\bar{e}_\theta\,d\theta = 0$.",
                result=r"\boxed{\,\bar{F} = \frac{\pi D_o^2}{4}\left[\rho V_o^2 + (p_o - p_a)\right]\bar{e}_x\,} \tag{2}")),
            ("bal", dict(
                label="Angular momentum about the axis (Notes Eq. 3.38)", eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho\,\bar{x}\wedge\bar{v}\,dV", r"0") + r" + \int_{\Sigma_c}\rho\,(\bar{x}\wedge\bar{v})[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma",
                cols=[r"\int\rho\,(\bar{x}\wedge\bar{v})_x\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma", r"\text{pressure and viscous moments}"],
                rows=[(r"\Sigma_o", [r"$0$ ($\bar{v} \parallel \bar{e}_x$, no swirl)", r"$0$"], False),
                      (r"\Sigma_s", [r"$\rho V_s\sin\alpha\,\pi Dh\,\frac{D}{2}V_s\cos\alpha = \dot{m}\,\frac{D}{2}\,V_s\cos\alpha$", r"$0$ ($\bar{x}\wedge\bar{e}_r$ has no $x$ component)"], False),
                      (r"\Sigma_w,\ \Sigma_b", [r"$0$", r"$-\bar{M}\cdot\bar{e}_x$"], True)],
                wall=r"On $\Sigma_s$, $\bar{x} = \frac{D}{2}\bar{e}_r + x\bar{e}_x$, and the $x$ component of $\bar{x}\wedge\bar{v}$ is $\frac{D}{2}V_s\cos\alpha$ (from $\bar{e}_r\wedge\bar{e}_\theta = \bar{e}_x$). The mass flux in front of it is (1).",
                result=r"\boxed{\,\bar{M} = -\rho V_o\frac{\pi D_o^2}{4}\,V_s\cos\alpha\,\frac{D}{2}\,\bar{e}_x\,} \tag{3}")),
            ("bal", dict(
                label="Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False, moving=True), cols=ENERGY_COLS,
                rows=[(r"\Sigma_o", [r"$-\dot{m}\left(e_o + \tfrac{V_o^2}{2}\right)$", r"$+p_oV_o\frac{\pi D_o^2}{4}$", r"$0$", r"$0$"], False),
                      (r"\Sigma_s", [r"$+\dot{m}\left(e_s + \tfrac{V_s^2}{2}\right)$", r"$-p_sV_s\sin\alpha\,\pi Dh$", r"$0$", r"$0$"], False),
                      (r"\Sigma_b", [r"$0$", r"$-\int_{\Sigma_b}p\,\bar{v}\cdot\bar{n}\,d\sigma$", r"$\int_{\Sigma_b}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$", r"$0$"], True),
                      (r"\Sigma_w", [r"$0$", r"$0$", r"$0$", r"$0$ (insulated)"], False)],
                wall=r"Boxed $\Sigma_b$ terms: the power $\dot{W}$ of the blades. With $e_s = e_o$ and (1):",
                result=r"\boxed{\,\dot{W} = \rho V_o\frac{\pi D_o^2}{4}\left[\left(\frac{p_s}{\rho} + \frac{V_s^2}{2}\right) - \left(\frac{p_o}{\rho} + \frac{V_o^2}{2}\right)\right]\,} \tag{4}")),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"(3) is the reaction to the angular momentum given to the water: the blades give the water the swirl $V_s\cos\alpha$ at radius $D/2$, and the water acts on the pump with the opposite torque (Euler's turbomachinery relation; the motor must supply it).",
                r"(4): the ideal power raises the total pressure $p + \tfrac{1}{2}\rho V^2$ of the water flow rate $\dot{m}/\rho$.",
                r"Dimensions (SI): $[\dot{m}\,D\,V_s] = \text{N}\cdot\text{m}$; $[\dot{m}\,p/\rho] = \text{W}$; $[D_o^2V_o/(Dh)] = \text{m/s}$.",
                rf"Numerical illustration (hypothetical data): $\rho = 1000$ kg/m$^3$, $D = 0.3$ m, $D_o = 0.1$ m, $h = 0.02$ m, $\alpha = 30^\circ$, $V_o = 3$ m/s, $p_o = 1.2\times10^5$ Pa, $p_s = 2.5\times10^5$ Pa, $p_a = 101325$ Pa give $V_s\sin\alpha = {f(_Vn13)}$ m/s ($V_s = {f(_Vs13)}$ m/s), $F_x = {f(_F13)}$ N, $|\bar{{M}}| = {f(_M13)}$ N$\cdot$m, $\dot{{W}} = {f(_W13)}$ W.",
                r"Agreement with the official solution: CL13.pdf obtains (1) to (4).",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL14
_p1, _r1, _u1, _ut, _p2, _Ri, _Ro = 1.2e5, 1.1, 150., 80., 1.3e5, 0.2, 0.5
_A1, _A2 = math.pi * (_Ro ** 2 - _Ri ** 2), math.pi * _Ro ** 2
_m14 = _r1 * _u1 * _A1 / _A2
_H14 = GAM / (GAM - 1) * _p1 / _r1 + (_u1 ** 2 + _ut ** 2) / 2
_bb = GAM * _p2 / ((GAM - 1) * _m14)
_u2 = -_bb + math.sqrt(_bb ** 2 + 2 * _H14)
_r2 = _m14 / _u2
_F14 = (_p1 + _r1 * _u1 ** 2) * _A1 - (_p2 + _r2 * _u2 ** 2) * _A2
_M14 = 2 * math.pi / 3 * _r1 * _u1 * _ut * (_Ro ** 3 - _Ri ** 3)
CL14 = dict(
    id="cl14", pill="CL14: Diffuser Module",
    title="Gas-Turbine Diffuser Module: Exit State, Force and Torque",
    note_title="Problem - CL14 Gas Turbine Diffuser Module",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-angular", "energia", "difusor"],
    tags_html=["Stator", "Swirl removal", "Angular momentum", "Perfect gas"],
    statement=[
        ("p", r"The diffuser module at the exit of a gas turbine consists of a **fixed** aerofoil cascade (stator), of inner and outer radii $R_i$ and $R_o$, respectively, together with a conical diffuser, as depicted in the figure of CL14.pdf. The gas enters the module with velocity field $\bar{v}_1 = u_1\bar{e}_z + u_\theta\bar{e}_\theta$, having both axial and azimuthal components, pressure $p_1$ and density $\rho_1$, and leaves the module with a purely axial velocity field $\bar{v}_2 = u_2\bar{e}_z$, pressure $p_2$ and density $\rho_2$. For the analysis of the problem, one may introduce the following assumptions:"),
        ("ul", [r"The effect of gravity is entirely negligible.", r"Flow properties at the entrance and exit sections are uniform.", r"The air around the casing is at rest with uniform pressure $p_a$.", r"The working gas behaves as a perfect gas (gas constant $R_g$, specific heat ratio $\gamma$).", r"All the inner walls are adiabatic."]),
        ("p", r"With the above simplifications, write the equations that determine the values of $\rho_2$ and $u_2$, as well as the net force, $F$, and torque, $M$, acting on the diffuser module, in terms of the known quantities ($p_a$, $p_1$, $\rho_1$, $p_2$, $u_1$, $u_\theta$, $R_i$, $R_o$, $\gamma$ and $R_g$)."),
    ],
    source_line=r"Source: CL14.pdf (pages 1-4, quiz of Nov 5, 2012, with typed solution). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady, axisymmetric; neglect $\bar{g}$; uniform properties at both sections; perfect gas, $h = c_pT = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$; adiabatic walls; the module is fixed (no work).",
                r"Inlet: annulus $R_i < r < R_o$ (area $A_1 = \pi(R_o^2 - R_i^2)$). Exit: full disc $r < R_o$ (area $A_2 = \pi R_o^2$).",
                r"The ambient air at $p_a$ touches only the outer cylindrical casing, whose normal is radial: by axisymmetry it gives no axial force and no axial torque ($\bar{F}_{ext} = 0$, $\bar{M}_{ext} = 0$). Absolute pressures are therefore used, as in the official solution (the gauge form would wrongly add $p_a\pi R_i^2$ on the hub face, which is not in contact with the ambient air).",
                r"Data: $[p_a,\ p_1,\ \rho_1,\ p_2,\ u_1,\ u_\theta,\ R_i,\ R_o,\ \gamma,\ R_g]$. Unknowns: $[\rho_2,\ u_2,\ F,\ M]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$u_1$, $u_\theta$", "axial and azimuthal inlet velocity", "m/s"],
                [r"$p_1$, $\rho_1$; $p_2$, $\rho_2$", "inlet and exit states", r"Pa, kg/m$^3$"],
                [r"$u_2$", "exit axial velocity", "m/s"],
                [r"$R_i$, $R_o$", "inner and outer radii", "m"],
                [r"$F$, $M$", "axial force and torque on the module", r"N, N$\cdot$m"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the module; right-handed cylindrical basis $(\bar{e}_r, \bar{e}_\theta, \bar{e}_z)$, $\bar{e}_r\wedge\bar{e}_\theta = \bar{e}_z$, with $\bar{e}_z$ along the flow; origin on the axis.",
                r"Surfaces (as in the official solution): $\Sigma_{in}$ (inlet annulus, $\bar{n} = -\bar{e}_z$), $\Sigma_{out}$ (exit disc, $\bar{n} = +\bar{e}_z$), $\Sigma_w$ (inner wall of the casing and outer wall of the cone) and $\Sigma_a$ (surfaces around the stator aerofoils). All are fixed.",
            ]),
            ("m", r"\boxed{\,F\,\bar{e}_z = \int_{\Sigma_w,\Sigma_a}\left[p\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma + \underbrace{\bar{F}_{ext}}_{0}\,}"),
            ("m", r"\boxed{M\,\bar{e}_z = \int_{\Sigma_w,\Sigma_a}\bar{x}\wedge\left[p\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma + \underbrace{\bar{M}_{ext}}_{0}\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="Mass (Notes Eq. 3.11)", eq=mass_eq(), cols=[COL_MASS],
                rows=[(r"\Sigma_{in}", [r"$-\rho_1u_1\pi(R_o^2 - R_i^2)$"], False), (r"\Sigma_{out}", [r"$+\rho_2u_2\pi R_o^2$"], False), (r"\Sigma_w,\ \Sigma_a", [r"$0$"], False)],
                result=r"\boxed{\,\rho_1u_1\pi(R_o^2 - R_i^2) = \rho_2u_2\pi R_o^2 = G\,} \tag{1}")),
            ("bal", dict(
                label="Linear momentum, axial component (Notes Eq. 3.36)", eq=MOM_FIXED_NOG.replace("(p - p_a)", "p"), cols=[r"\int\rho v_z\,(\bar{v}\cdot\bar{n})\,d\sigma", r"-\int p\,n_z\,d\sigma", r"\int(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma"],
                rows=[(r"\Sigma_{in}", [r"$-\rho_1u_1^2\pi(R_o^2 - R_i^2)$", r"$+p_1\pi(R_o^2 - R_i^2)$", r"$0$ (uniform)"], False),
                      (r"\Sigma_{out}", [r"$+\rho_2u_2^2\pi R_o^2$", r"$-p_2\pi R_o^2$", r"$0$ (uniform)"], False),
                      (r"\Sigma_w,\ \Sigma_a", [r"$0$", r"$-\int p\,n_z\,d\sigma$", r"$\int(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma$"], True)],
                wall=r"Boxed terms: the force of the walls on the gas, $-F$ (with $\bar{F}_{ext} = 0$). The swirl gives no axial momentum flux.",
                result=r"\boxed{\,F = \pi(R_o^2 - R_i^2)\left(p_1 + \rho_1u_1^2\right) - \pi R_o^2\left(p_2 + \rho_2u_2^2\right)\,} \tag{2}")),
            ("bal", dict(
                label="Angular momentum, axial component (Notes Eq. 3.38)", eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho\,\bar{x}\wedge\bar{v}\,dV", "0") + r" + \int_{\Sigma_c}\rho\,(\bar{x}\wedge\bar{v})(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}\bar{x}\wedge p\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma",
                cols=[r"\int\rho\,(\bar{x}\wedge\bar{v})_z\,(\bar{v}\cdot\bar{n})\,d\sigma", r"\text{pressure and viscous moments}"],
                rows=[(r"\Sigma_{in}", [r"$\int_{R_i}^{R_o}\rho_1\,(ru_\theta)(-u_1)\,2\pi r\,dr = -\frac{2\pi}{3}\rho_1u_1u_\theta(R_o^3 - R_i^3)$", r"$0$ ($\bar{x}\wedge\bar{e}_z$ has no $z$ component)"], False),
                      (r"\Sigma_{out}", [r"$0$ (no swirl)", r"$0$"], False),
                      (r"\Sigma_w,\ \Sigma_a", [r"$0$", r"$-M$"], True)],
                wall=r"On $\Sigma_{in}$, $\bar{x} = r\bar{e}_r + z\bar{e}_z$ and the $z$ component of $\bar{x}\wedge(u_1\bar{e}_z + u_\theta\bar{e}_\theta)$ is $ru_\theta$ (from $\bar{e}_r\wedge\bar{e}_\theta = \bar{e}_z$). The antiderivative of $r^2$ is $r^3/3$; Barrow's rule between $R_i$ and $R_o$ gives $(R_o^3 - R_i^3)/3$.",
                result=r"\boxed{\,M = \frac{2\pi}{3}\,\rho_1u_1u_\theta\left(R_o^3 - R_i^3\right)\,} \tag{3}")),
            ("bal", dict(
                label="Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False), cols=ENERGY_COLS,
                rows=[(r"\Sigma_{in}", [r"$-G\left(e_1 + \tfrac{u_1^2 + u_\theta^2}{2}\right)$", r"$+p_1u_1\pi(R_o^2 - R_i^2)$", r"$0$", r"$0$"], False),
                      (r"\Sigma_{out}", [r"$+G\left(e_2 + \tfrac{u_2^2}{2}\right)$", r"$-p_2u_2\pi R_o^2$", r"$0$", r"$0$"], False),
                      (r"\Sigma_w,\ \Sigma_a", [r"$0$", r"$0$ ($\bar{v} = 0$)", r"$0$ ($\bar{v} = 0$)", r"$0$ (adiabatic)"], False)],
                result=r"\boxed{\,\frac{\gamma}{\gamma - 1}\frac{p_1}{\rho_1} + \frac{u_1^2 + u_\theta^2}{2} = \frac{\gamma}{\gamma - 1}\frac{p_2}{\rho_2} + \frac{u_2^2}{2}\,} \tag{4}")),
            ("p", r"(1) and (4) give $\rho_2$ and $u_2$; then (2) gives $F$ and (3) gives $M$ directly; $T_2 = p_2/(\rho_2R_g)$ from the equation of state."),
            ("note", "Discrepancy with the official solution (sign of the torque)", r"CL14.pdf uses $\bar{x}\wedge\bar{e}_\theta = -r\bar{e}_z$ and obtains $M = -\frac{2\pi}{3}\rho_1u_1u_\theta(R_e^3 - R_i^3)$ (it calls the outer radius $R_e$). With the right-handed basis $(\bar{e}_r, \bar{e}_\theta, \bar{e}_z)$ one has $\bar{e}_r\wedge\bar{e}_\theta = +\bar{e}_z$, so $\bar{x}\wedge\bar{e}_\theta = +r\bar{e}_z$ and the sign is the one in (3). The magnitude is the same; physically, the torque of the gas on the stator has the sense of the incoming swirl, since the stator removes it. The computed sign is kept."),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"(4): the stagnation enthalpy is conserved; the kinetic energy of the swirl, $u_\theta^2/2$, is recovered as enthalpy (pressure and temperature) downstream.",
                r"For $u_\theta = 0$ there is nothing to remove and $M = 0$. $M$ is the torque that the mounting of the stator must withstand.",
                r"Dimensions (SI): $[(p + \rho u^2)R^2] = \text{N}$; $[\rho u_1u_\theta R^3] = \text{N}\cdot\text{m}$.",
                rf"Numerical illustration (hypothetical data, extension): $p_1 = 1.2\times10^5$ Pa, $\rho_1 = 1.1$ kg/m$^3$, $u_1 = 150$ m/s, $u_\theta = 80$ m/s, $p_2 = 1.3\times10^5$ Pa, $R_i = 0.2$ m, $R_o = 0.5$ m, $\gamma = 1.4$: eliminating $\rho_2 = G/(\pi R_o^2u_2)$ in (4) gives a quadratic in $u_2$ with positive root $u_2 = {f(_u2)}$ m/s, $\rho_2 = {f(_r2)}$ kg/m$^3$; then $F = {f(_F14)}$ N (the module is pushed upstream by the pressure rise) and $M = {f(_M14)}$ N$\cdot$m.",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL15
_v1, _v2, _r15, _T1, _T2, _dp1, _dp2, _D1, _D2, _L1, _c15 = 0.4, 1.2, 1000., 20., 40., 50., 200., 0.1, 0.025, 0.2, 4216.
_A115, _A215 = math.pi * _D1 ** 2 / 4, math.pi * _D2 ** 2 / 4
_vs15 = _v1 + _v2 * (_D2 / _D1) ** 2
_Ts15 = (_T1 + _dp1 / (_r15 * _c15) + _v1 ** 2 / (2 * _c15)) * _v1 / _vs15 + (_T2 + _dp2 / (_r15 * _c15) + _v2 ** 2 / (2 * _c15)) * _v2 * _A215 / (_vs15 * _A115) - _vs15 ** 2 / (2 * _c15)
_Fx15 = (_r15 * _v1 ** 2 + _dp1) * _A115
_Fy15 = (_r15 * _v2 ** 2 + _dp2) * _A215 - _r15 * _vs15 ** 2 * _A115
_M15 = _Fy15 * (_L1 + 1.5 * _D1)
CL15 = dict(
    id="cl15", pill="CL15: Mixing Elbow",
    title="Mixing Elbow: Exit Velocity and Temperature, Force and Torque",
    note_title="Problem - CL15 Mixing Elbow",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-angular", "energia", "mezcla"],
    tags_html=["Two inlets", "Mixing", "Energy", "Angular momentum"],
    statement=[
        ("p", r"Consider the mixing elbow shown schematically in the figure of CL15.pdf. Cold water flows through the main pipe and mixes with warmer water that enters through a smaller inlet located at the elbow. The liquid properties can be considered independent of the temperature and gravity effects can be neglected. All pipe walls are adiabatic. The known pipe dimensions, fluid properties and boundary conditions are given in the figure (density $\rho$, viscosity $\mu$, conductivity $k$, specific heat $c$; main inlet $v_1$, $p_1$, $T_1$, diameter $D_1$; secondary inlet $v_2$, $p_2$, $T_2$, diameter $D_2$; exit at $p_a$). Assume that the two streams mix completely and that the velocity and temperature are uniform at the exit section."),
        ("ul", [
            r"Find the velocity $v_s$ and temperature $T_s$ of the mixed stream emerging from the pipe at ambient pressure.",
            r"Obtain the net force $\bar{F}$ exerted on the mixing elbow by the water flowing inside and the ambient air.",
            r"Obtain the torque $\bar{M}_1$ about the point $\bar{x}_1$ located at the center of the larger inlet.",
            r"Compute the above results numerically, given the following data: $v_1 = 0.4$ m/s; $v_2 = 1.2$ m/s; $\rho = 1000$ kg/m$^3$; $T_1 = 20^\circ$C; $T_2 = 40^\circ$C; $\mu = 8\times10^{-4}$ Pa s; $p_1 - p_a = 50$ Pa; $p_2 - p_a = 200$ Pa; $k = 0.677$ W/(m s); $D_1 = 10$ cm; $D_2 = 2.5$ cm; $c = 4216$ J/(kg K); $L_1 = 20$ cm; $L_2 = 7$ cm.",
        ]),
    ],
    source_line=r"Source: CL15.pdf (pages 1-2, exam of Dec 18, 2012, with solution). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady, incompressible liquid with constant properties, $e = e_0 + cT$; neglect $\bar{g}$; adiabatic walls; uniform properties at the three sections; complete mixing.",
                r"Geometry (figure): main inlet along $+\bar{e}_x$ (section $A_1 = \pi D_1^2/4$), secondary inlet along $+\bar{e}_y$ ($A_2 = \pi D_2^2/4$), exit along $+\bar{e}_y$ (section $A_1$) at $p_a$. The secondary inlet and the exit share the same vertical axis, at a horizontal distance $L_1 + D_1 + D_1/2 = L_1 + \tfrac{3}{2}D_1$ from $\bar{x}_1$ (bend of inner radius $D_1$; reading of the figure, as in the official solution).",
                r"Data: as listed. Unknowns: $[v_s,\ T_s,\ \bar{F},\ \bar{M}_1]$. $\mu$, $k$ and $L_2$ are not needed.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$v_1$, $v_2$, $v_s$", "inlet and exit velocities", "m/s"],
                [r"$T_1$, $T_2$, $T_s$", "temperatures", r"$^\circ$C"],
                [r"$p_1 - p_a$, $p_2 - p_a$", "inlet gauge pressures", "Pa"],
                [r"$D_1$, $D_2$, $L_1$", "diameters and length", "m"],
                [r"$\bar{F}$, $\bar{M}_1$", "force and torque on the elbow", r"N, N$\cdot$m"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the elbow: $\bar{e}_x$ horizontal (main inlet flow), $\bar{e}_y$ vertical upwards, $\bar{e}_z$ towards the reader; moments about $\bar{x}_1$.",
                r"Surfaces (fixed CV, as in the official solution): $\Sigma_1$ (main inlet, $\bar{n} = -\bar{e}_x$), $\Sigma_2$ (secondary inlet, $\bar{n} = -\bar{e}_y$), $\Sigma_{out}$ (exit, $\bar{n} = +\bar{e}_y$), $\Sigma_{wall}$.",
            ]),
            ("m", r"\boxed{\,\bar{F} = -\int_{\Sigma_{wall}}\left[-(p - p_a)\,\bar{n} + \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
            ("m", r"\boxed{\bar{M}_1 = -\int_{\Sigma_{wall}}(\bar{x} - \bar{x}_1)\wedge\left[-(p - p_a)\,\bar{n} + \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="Mass (Notes Eq. 3.11)", eq=mass_eq(), cols=[COL_MASS],
                rows=[(r"\Sigma_1", [r"$-\rho v_1A_1$"], False), (r"\Sigma_2", [r"$-\rho v_2A_2$"], False), (r"\Sigma_{out}", [r"$+\rho v_sA_1$"], False), (r"\Sigma_{wall}", [r"$0$"], False)],
                result=r"v_1A_1 + v_2A_2 = v_sA_1 \;\Longrightarrow\; \boxed{\,v_s = v_1 + v_2\left(\frac{D_2}{D_1}\right)^2\,} \tag{1}")),
            ("bal", dict(
                label="Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False), cols=ENERGY_COLS,
                rows=[(r"\Sigma_1", [r"$-\rho\left(e_1 + \tfrac{v_1^2}{2}\right)v_1A_1$", r"$+p_1v_1A_1$", r"$0$", r"$0$"], False),
                      (r"\Sigma_2", [r"$-\rho\left(e_2 + \tfrac{v_2^2}{2}\right)v_2A_2$", r"$+p_2v_2A_2$", r"$0$", r"$0$"], False),
                      (r"\Sigma_{out}", [r"$+\rho\left(e_s + \tfrac{v_s^2}{2}\right)v_sA_1$", r"$-p_av_sA_1$", r"$0$", r"$0$"], False),
                      (r"\Sigma_{wall}", [r"$0$", r"$0$", r"$0$", r"$0$ (adiabatic)"], False)],
                wall=r"With $e = e_0 + cT$, dividing by $\rho c\,v_sA_1$ ($e_0$ cancels by (1)) and writing $p_a$ as $p_a(v_1A_1 + v_2A_2)/(v_sA_1)$:",
                result=r"\boxed{\,T_s = \left(T_1 + \frac{p_1 - p_a}{\rho c} + \frac{v_1^2}{2c}\right)\frac{v_1}{v_s} + \left(T_2 + \frac{p_2 - p_a}{\rho c} + \frac{v_2^2}{2c}\right)\frac{v_2A_2}{v_sA_1} - \frac{v_s^2}{2c}\,} \tag{2}")),
            ("bal", dict(
                label="Linear momentum (Notes Eq. 3.36)", eq=MOM_FIXED_NOG, cols=[COL_MFLUX, COL_P, COL_TAU],
                rows=[(r"\Sigma_1", [r"$-\rho v_1^2A_1\,\bar{e}_x$", r"$(p_1 - p_a)A_1\,\bar{e}_x$", r"$0$"], False),
                      (r"\Sigma_2", [r"$-\rho v_2^2A_2\,\bar{e}_y$", r"$(p_2 - p_a)A_2\,\bar{e}_y$", r"$0$"], False),
                      (r"\Sigma_{out}", [r"$+\rho v_s^2A_1\,\bar{e}_y$", r"$0$ ($p = p_a$)", r"$0$"], False),
                      (r"\Sigma_{wall}", [r"$0$", r"$-\int(p - p_a)\,\bar{n}\,d\sigma$", r"$\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed terms: $-\bar{F}$.",
                result=r"\boxed{\,\bar{F} = \left(\rho v_1^2 + p_1 - p_a\right)A_1\,\bar{e}_x + \left[\left(\rho v_2^2 + p_2 - p_a\right)A_2 - \rho v_s^2A_1\right]\bar{e}_y\,} \tag{3}")),
            ("bal", dict(
                label="Angular momentum about x̄₁ (Notes Eq. 3.38)", eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho\,(\bar{x} - \bar{x}_1)\wedge\bar{v}\,dV", "0") + r" + \int_{\Sigma_c}\rho\,[(\bar{x} - \bar{x}_1)\wedge\bar{v}](\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}(\bar{x} - \bar{x}_1)\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}(\bar{x} - \bar{x}_1)\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma",
                cols=[r"\int\rho\,[(\bar{x} - \bar{x}_1)\wedge\bar{v}](\bar{v}\cdot\bar{n})\,d\sigma", r"-\int(\bar{x} - \bar{x}_1)\wedge(p - p_a)\bar{n}\,d\sigma", r"\int(\bar{x} - \bar{x}_1)\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma"],
                rows=[(r"\Sigma_1", [r"$0$ (centred at $\bar{x}_1$)", r"$0$", r"$0$"], False),
                      (r"\Sigma_2", [r"$-\rho v_2^2A_2\,d\,\bar{e}_z$", r"$(p_2 - p_a)A_2\,d\,\bar{e}_z$", r"$0$"], False),
                      (r"\Sigma_{out}", [r"$+\rho v_s^2A_1\,d\,\bar{e}_z$", r"$0$", r"$0$"], False),
                      (r"\Sigma_{wall}", [r"$0$", r"$-\int(\bar{x} - \bar{x}_1)\wedge(p - p_a)\bar{n}\,d\sigma$", r"$\int(\bar{x} - \bar{x}_1)\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$"], True)],
                wall=r"Boxed terms: $-\bar{M}_1$. With $d = L_1 + \tfrac{3}{2}D_1$ the horizontal distance to the common vertical axis, $(\bar{x} - \bar{x}_1)\wedge\bar{e}_y = d\,\bar{e}_x\wedge\bar{e}_y = d\,\bar{e}_z$ for the centres of $\Sigma_2$ and $\Sigma_{out}$ (the vertical offsets are parallel to $\bar{e}_y$ and drop out).",
                result=r"\boxed{\,\bar{M}_1 = \left[\left(\rho v_2^2 + p_2 - p_a\right)A_2 - \rho v_s^2A_1\right]\left(L_1 + \frac{3}{2}D_1\right)\bar{e}_z\,} \tag{4}")),
            ("h4", "Numerical values (part 4)"),
            ("table", ["Quantity", "Value"], [
                [r"$v_s$", rf"${f(_vs15,3)}$ m/s"],
                [r"$T_s$", rf"${f(_Ts15,4)}\ ^\circ$C"],
                [r"$\bar{F}$", rf"${f(_Fx15,3)}\,\bar{{e}}_x {f(_Fy15,3)}\,\bar{{e}}_y$ N"],
                [r"$\bar{M}_1$", rf"${f(_M15,3)}\,\bar{{e}}_z$ N$\cdot$m"],
            ]),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"(2) is a mass-weighted average of the inlet temperatures, corrected by the tiny flow-work and kinetic-energy terms ($\Delta p/(\rho c) \sim 10^{-5}$ K here): $T_s \approx (v_1A_1T_1 + v_2A_2T_2)/(v_sA_1)$.",
                r"$F_y < 0$: the exit momentum flux exceeds the momentum and gauge pressure brought in by the small inlet, so the elbow is pulled downwards; $\bar{M}_1$ follows from the same vertical imbalance acting at the arm $d$.",
                r"Dimensions (SI): $[(p - p_a)/(\rho c)] = \text{K}$, $[v^2/c] = \text{K}$; $[\rho v^2A] = \text{N}$; $[\rho v^2Ad] = \text{N}\cdot\text{m}$.",
                r"Agreement with the official solution: CL15.pdf obtains (1) to (4) and $v_s = 0.475$ m/s, $T_s = 23^\circ$C, $\bar{F} = 1.65\,\bar{e}_x - 0.967\,\bar{e}_y$ N, $\bar{M}_1 = -0.338\,\bar{e}_z$ N$\cdot$m, the same values.",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL16
_r16, _v16, _h16, _al16, _th16 = 1000., 10., 0.02, 0.3, math.radians(25)
CL16 = dict(
    id="cl16", pill="CL16: Jet on a Wedge",
    title="Plane Jet Split by a Non-Symmetric Wedge: Force, Moment and Heat",
    note_title="Problem - CL16 Plane Jet on a Non-Symmetric Wedge",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-angular", "energia", "chorro"],
    tags_html=["Free jets", "Bernoulli", "Moment of a jet", "Heat transfer"],
    statement=[
        ("p", r"A plane liquid jet of constant density $\rho$, thickness $h$ and uniform velocity $v$, impinges on a non-symmetric wedge of geometry and dimensions shown in the figure of CL16.pdf. The wedge splits the jet into two layers of unequal flux, such that a portion $\alpha$ of the volume flux is deflected an angle $\theta$, and the rest of the fluid is deflected an angle $2\theta$. The flow is steady; viscous and gravitational forces are negligible; the known data are $(\rho, c, v, h, \alpha, \theta, L, p_a, T_0, T_1, T_2)$."),
        ("ul", [
            r"Noting that the conditions for the use of Bernoulli's theorem are met, determine the (uniform) velocity of the fluid on each deflected layer.",
            r"Determine the thickness $h_1$ and $h_2$ of each layer.",
            r"Determine the force $\bar{F}$ (per unit length in the $z$-direction) that the liquid jet and the ambient air exert on the wedge.",
            r"Determine the moment $\bar{M}_0$ due to the force $\bar{F}$ about the corner $\bar{x}_0$ of the wedge. Find the value of the fraction $\alpha$ that would produce a null moment, $\bar{M}_0 = 0$.",
            r"Knowing the uniform temperature $T_0$ of the incoming jet, the uniform temperatures $T_1$ and $T_2$ of the two liquid layers when they lose contact with the wedge, and the constant specific heat $c$ of the liquid, determine the heat $q$ transferred per unit surface from the liquid to the wedge. Assume that the heat flux is uniform on the wedge surface and that there is no heat transfer by conduction between the liquid and the ambient air.",
        ]),
    ],
    source_line=r"Source: CL16.pdf (pages 1-2, exam of Jan 14, 2013, with handwritten results). Notes.pdf: Bernoulli's equation Eq. 4.17, integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady, planar (per unit length in $z$), incompressible, frictionless; neglect $\bar{g}$; free jets at $p_a$ (straight parallel streamlines in the layers away from the corner, so $p = p_a$ inside them).",
                r"Geometry (figure): the incoming jet is centred on the $x$ axis, which passes through the corner $\bar{x}_0$; layer 1 leaves along $\bar{t}_1 = \cos\theta\,\bar{e}_x + \sin\theta\,\bar{e}_y$ on the upper face, layer 2 along $\bar{t}_2 = \cos2\theta\,\bar{e}_x - \sin2\theta\,\bar{e}_y$ on the lower face. The faces have horizontal length $L$, i.e. lengths $L/\cos\theta$ and $L/\cos2\theta$.",
                r"Heat: uniform flux $q$ from the liquid to the wedge on both faces; no conduction to the air; $e = cT$.",
                r"Data: $[\rho,\ c,\ v,\ h,\ \alpha,\ \theta,\ L,\ p_a,\ T_0,\ T_1,\ T_2]$. Unknowns: $[v_1,\ v_2,\ h_1,\ h_2,\ \bar{F},\ \bar{M}_0,\ q]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$v$, $h$", "jet velocity and thickness", "m/s, m"],
                [r"$\alpha$, $\theta$", "flux fraction and deflection angle", "1, rad"],
                [r"$h_1$, $h_2$", "layer thicknesses", "m"],
                [r"$\bar{F}$, $\bar{M}_0$", "force and moment per unit length", r"N/m, N$\cdot$m/m"],
                [r"$q$", "heat flux to the wedge", r"W/m$^2$"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the wedge; origin at the corner $\bar{x}_0$; $\bar{e}_z$ towards the reader.",
                r"Surfaces: $\Sigma_0$ (incoming jet section, $\bar{n} = -\bar{e}_x$), $\Sigma_1$, $\Sigma_2$ (layer sections normal to $\bar{t}_1$, $\bar{t}_2$, $\bar{n} = \bar{t}_1, \bar{t}_2$), $\Sigma_a$ (free surfaces, $p = p_a$) and $\Sigma_w$ (wetted faces). On layer $k$, $\bar{x} - \bar{x}_0 = s\,\bar{t}_k + \eta\,\bar{m}_k$, with $\bar{m}_1 = -\sin\theta\,\bar{e}_x + \cos\theta\,\bar{e}_y$, $\bar{m}_2 = -\sin2\theta\,\bar{e}_x - \cos2\theta\,\bar{e}_y$ the unit normals pointing away from the wedge and $0 \le \eta \le h_k$.",
            ]),
            ("m", r"\boxed{\,\bar{F} = \int_{\Sigma_w}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
            ("m", r"\boxed{\bar{M}_0 = \int_{\Sigma_w}(\bar{x} - \bar{x}_0)\wedge\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
            ("m", r"\boxed{q = -\frac{1}{L/\cos\theta + L/\cos2\theta}\int_{\Sigma_w}\bar{q}\cdot\bar{n}_{\text{in}}\,d\sigma\,}"),
        ]),
        ("Phase 3", "Bernoulli and Balances, Surface by Surface", [
            ("h4", "1. Velocities"),
            ("p", r"Bernoulli (Notes Eq. 4.17, $U = 0$) along a free streamline from the incoming jet to each layer, with $p = p_a$ at both ends: $p_a + \tfrac{1}{2}\rho v^2 = p_a + \tfrac{1}{2}\rho v_k^2$, so"),
            ("m", r"\boxed{\,v_1 = v_2 = v\,} \tag{1}"),
            ("bal", dict(
                label="2. Mass (Notes Eq. 3.11): thicknesses", eq=mass_eq(), cols=[COL_MASS],
                rows=[(r"\Sigma_0", [r"$-\rho vh = -\rho Q$"], False), (r"\Sigma_1", [r"$+\rho vh_1 = \rho\alpha Q$"], False), (r"\Sigma_2", [r"$+\rho vh_2 = \rho(1 - \alpha)Q$"], False), (r"\Sigma_a,\ \Sigma_w", [r"$0$"], False)],
                result=r"\boxed{\,h_1 = \alpha h,\qquad h_2 = (1 - \alpha)h\,} \tag{2}")),
            ("bal", dict(
                label="3. Linear momentum (Notes Eq. 3.36)", eq=MOM_FIXED_NOG, cols=[COL_MFLUX, COL_P, COL_TAU],
                rows=[(r"\Sigma_0", [r"$-\rho v^2h\,\bar{e}_x$", r"$0$", r"$0$"], False),
                      (r"\Sigma_1", [r"$\rho v^2\alpha h\,(\cos\theta\,\bar{e}_x + \sin\theta\,\bar{e}_y)$", r"$0$", r"$0$"], False),
                      (r"\Sigma_2", [r"$\rho v^2(1 - \alpha)h\,(\cos2\theta\,\bar{e}_x - \sin2\theta\,\bar{e}_y)$", r"$0$", r"$0$"], False),
                      (r"\Sigma_a", [r"$0$", r"$0$ ($p = p_a$)", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$", r"$\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed $\Sigma_w$ terms: $-\bar{F}$.",
                result=r"\boxed{\,\bar{F} = \rho v^2h\left\{\left[1 - \alpha\cos\theta - (1 - \alpha)\cos2\theta\right]\bar{e}_x - \left[\alpha\sin\theta - (1 - \alpha)\sin2\theta\right]\bar{e}_y\right\}\,} \tag{3}")),
            ("bal", dict(
                label="4. Angular momentum about x̄₀ (Notes Eq. 3.38)", eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho\,(\bar{x} - \bar{x}_0)\wedge\bar{v}\,dV", "0") + r" + \int_{\Sigma_c}\rho\,[(\bar{x} - \bar{x}_0)\wedge\bar{v}](\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}(\bar{x} - \bar{x}_0)\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}(\bar{x} - \bar{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma",
                cols=[r"\int\rho\,[(\bar{x} - \bar{x}_0)\wedge\bar{v}](\bar{v}\cdot\bar{n})\,d\sigma", r"\text{pressure and viscous moments}"],
                rows=[(r"\Sigma_0", [r"$\int_{-h/2}^{h/2}\rho v\,(-yv)(-1)\,dy\;\bar{e}_z = 0$ (odd in $y$)", r"$0$"], False),
                      (r"\Sigma_1", [r"$\int_0^{h_1}\rho v^2\,\eta\,(\bar{m}_1\wedge\bar{t}_1)\,d\eta = -\rho v^2\frac{h_1^2}{2}\,\bar{e}_z$", r"$0$"], False),
                      (r"\Sigma_2", [r"$\int_0^{h_2}\rho v^2\,\eta\,(\bar{m}_2\wedge\bar{t}_2)\,d\eta = +\rho v^2\frac{h_2^2}{2}\,\bar{e}_z$", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$-\bar{M}_0$"], True)],
                wall=r"Here $\bar{m}_1\wedge\bar{t}_1 = (-\sin^2\theta - \cos^2\theta)\,\bar{e}_z = -\bar{e}_z$ and $\bar{m}_2\wedge\bar{t}_2 = (\sin^22\theta + \cos^22\theta)\,\bar{e}_z = +\bar{e}_z$; the part $s\,\bar{t}_k\wedge\bar{t}_k$ vanishes. The antiderivative of $\eta$ is $\eta^2/2$; Barrow's rule between $0$ and $h_k$ gives $h_k^2/2$. With (2): $-\frac{\rho v^2h^2}{2}\left[\alpha^2 - (1 - \alpha)^2\right] = -\frac{\rho v^2h^2}{2}(2\alpha - 1)$.",
                result=r"-\frac{\rho v^2h^2}{2}(2\alpha - 1)\,\bar{e}_z = -\bar{M}_0 \;\Longrightarrow\; \boxed{\,\bar{M}_0 = \rho v^2\,\frac{h^2}{2}\,(2\alpha - 1)\,\bar{e}_z,\qquad \bar{M}_0 = 0 \iff \alpha = \frac{1}{2}\,} \tag{4}")),
            ("bal", dict(
                label="5. Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False), cols=ENERGY_COLS,
                rows=[(r"\Sigma_0", [r"$-\rho vh\left(cT_0 + \tfrac{v^2}{2}\right)$", r"$+p_avh$", r"$0$", r"$0$"], False),
                      (r"\Sigma_1", [r"$+\rho v\alpha h\left(cT_1 + \tfrac{v^2}{2}\right)$", r"$-p_av\alpha h$", r"$0$", r"$0$"], False),
                      (r"\Sigma_2", [r"$+\rho v(1 - \alpha)h\left(cT_2 + \tfrac{v^2}{2}\right)$", r"$-p_av(1 - \alpha)h$", r"$0$", r"$0$"], False),
                      (r"\Sigma_a", [r"$0$", r"$0$", r"$0$", r"$0$ (no conduction to the air)"], False),
                      (r"\Sigma_w", [r"$0$", r"$0$ ($\bar{v} = 0$)", r"$0$", r"$-q\left(\frac{L}{\cos\theta} + \frac{L}{\cos2\theta}\right)$"], True)],
                wall=r"Boxed $\Sigma_w$ term: the heat leaves the liquid towards the wedge. The kinetic-energy and pressure-work terms cancel because $\alpha + (1 - \alpha) = 1$.",
                result=r"\rho vhc\left[\alpha T_1 + (1 - \alpha)T_2 - T_0\right] = -q\left(\frac{L}{\cos\theta} + \frac{L}{\cos2\theta}\right) \;\Longrightarrow\; \boxed{\,q = \frac{\rho cvh}{\frac{L}{\cos\theta} + \frac{L}{\cos2\theta}}\left[T_0 - \alpha T_1 - (1 - \alpha)T_2\right]\,} \tag{5}")),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"Symmetric-split check: with $\alpha = 1/2$ the two layers carry equal flux and their moments about the corner cancel, (4). The force (3) is still not symmetric because the deflections $\theta$ and $2\theta$ differ.",
                r"Limit $\theta \to 0$: no deflection, $\bar{F} \to 0$ in (3) (both brackets vanish).",
                r"(5): $q > 0$ (liquid heats the wedge) when the liquid leaves colder than it arrived on average.",
                r"Dimensions (SI, per unit length): $[\rho v^2h] = \text{N/m}$; $[\rho v^2h^2] = \text{N}\cdot\text{m}/\text{m}$; $[\rho cvh\,\Delta T/L] = \text{W/m}^2$.",
                r"Numerical cross-check of (4) (hypothetical data): $\rho = 1000$ kg/m$^3$, $v = 10$ m/s, $h = 0.02$ m, $\alpha = 0.3$, $\theta = 25^\circ$: midpoint quadrature of the two layer integrals gives an angular-momentum flux of $8.000$ N$\cdot$m/m, equal to $-\rho v^2h^2(2\alpha - 1)/2 = 8$, i.e. $M_{0,z} = -8$ N$\cdot$m/m.",
                r"Agreement with the official solution: CL16.pdf obtains (1) to (5).",
            ]),
        ]),
    ],
)

PROBLEMS = [CL11, CL12, CL13, CL14, CL15, CL16]
