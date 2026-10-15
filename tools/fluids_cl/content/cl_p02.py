# CL6 to CL10 in the class style.
import math
from clcommon import *

ENERGY_COLS = [r"\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma", r"-\int p\,\bar{v}\cdot\bar{n}\,d\sigma",
               r"\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma", r"-\int\bar{q}\cdot\bar{n}\,d\sigma"]


def energy_eq(volume_heat=True, moving=False):
    vc = r"(\bar{v} - \bar{v}_c)" if moving else r"(\bar{v} - " + crossed(r"\bar{v}_c", "0") + ")"
    s = (crossed(r"\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV", r"0\ (\text{steady})")
         + r" + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[" + vc + r"\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + "
         + crossed(r"\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV", r"\text{neglect } \bar{g}") + r" - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + ")
    s += (r"\int_{V_c}Q_R\,dV" if volume_heat else crossed(r"\int_{V_c}Q_R\,dV", "0"))
    return s


def mom_eq(moving=False, pref="p_a"):
    vc = r"(\bar{v} - \bar{v}_c)" if moving else r"(\bar{v} - " + crossed(r"\bar{v}_c", "0") + ")"
    return (crossed(r"\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV", r"0\ (\text{steady})")
            + r" + \int_{\Sigma_c}\rho\bar{v}\,[" + vc + r"\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - " + pref + r")\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + "
            + crossed(r"\int_{V_c}\rho\bar{g}\,dV", r"\text{neglect } \bar{g}"))


def mass_eq(moving=False):
    vc = r"(\bar{v} - \bar{v}_c)" if moving else r"(\bar{v} - " + crossed(r"\bar{v}_c", "0") + ")"
    return crossed(r"\frac{d}{dt}\int_{V_c}\rho\,dV", r"0\ (\text{steady})") + r" + \int_{\Sigma_c}\rho\," + vc + r"\cdot\bar{n}\,d\sigma = 0"


# ---------------------------------------------------------------- CL6
_rho, _c, _Ai, _Ao, _vo, _pi, _pa, _Ti, _To = 1000., 4186., 0.01, 0.004, 6., 1.6e5, 101325., 293., 293.5
_vi = _vo * _Ao / _Ai
_Fx6 = (_rho * _vi ** 2 + _pi - _pa) * _Ai
_Fz6 = _rho * _vo ** 2 * _Ao
_Q6 = _rho * _vo * _Ao * (_c * (_To - _Ti) + (_vo ** 2 - _vi ** 2) / 2) + (_pa - _pi) * _vo * _Ao
CL6 = dict(
    id="cl6", pill="CL6: Elbow",
    title="Elbow Discharging a Vertical Jet: Velocity, Force and Heat",
    note_title="Problem - CL6 Elbow with Vertical Jet",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "energia", "codo"],
    tags_html=["Elbow", "Linear momentum", "Energy", "Heat through the walls"],
    statement=[
        ("p", r"A liquid of density $\rho$ and specific heat $c$ flows through the elbow-shaped pipe shown in CL6.pdf, discharging to the atmosphere as a vertical jet through an outlet section of surface area $A_o$, different from the value $A_i$ at the inlet. Gravity is assumed to have a negligible effect on the fluid motion. Besides, uniform flow properties are assumed at the inlet and outlet sections, where readings from a thermometer give different values $T_i$ and $T_o$ for the temperature. The velocity at the outlet section is measured to be $v_o$ and a manometer is used to determine the value $p_i$ for the pressure at the inlet section. In terms of all of these quantities, determine:"),
        ("ul", [r"The value of the velocity at the inlet $v_i$.", r"The two components of the force $(F_x, F_z)$ exerted on the pipe.", r"The amount of heat $Q$ transferred per unit time to the liquid by heat conduction through the pipe walls."]),
    ],
    source_line=r"Source: CL6.pdf (page 1), also solved in class (class notes, CL6). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady, incompressible liquid, $e = cT$; neglect $\bar{g}$; uniform properties at inlet and outlet (no viscous stresses or conduction across them).",
                r"Free jet: $p = p_a$ over the outlet section. The outer face of the pipe is in contact with the ambient air at $p_a$, so the force on the pipe is computed with gauge pressure $p - p_a$.",
                r"Geometry (figure): the liquid enters horizontally along $+\bar{e}_x$ and leaves as a vertical jet along $-\bar{e}_z$ ($\bar{e}_z$ upwards).",
                r"Data: $[\rho,\ c,\ A_i,\ A_o,\ v_o,\ p_i,\ p_a,\ T_i,\ T_o]$. Unknowns: $[v_i,\ F_x,\ F_z,\ \dot{Q}]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$A_i$, $A_o$", "inlet and outlet areas", r"m$^2$"],
                [r"$v_i$, $v_o$", "inlet and outlet velocities", "m/s"],
                [r"$p_i$, $p_a$", "inlet and ambient pressures", "Pa"],
                [r"$T_i$, $T_o$", "inlet and outlet temperatures", "K"],
                [r"$c$", "specific heat of the liquid", r"J/(kg$\cdot$K)"],
                [r"$\dot{Q}$", "heat per unit time into the liquid", "W"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the pipe, $\bar{e}_x$ horizontal (inlet flow direction), $\bar{e}_z$ vertical upwards. Fixed control volume: the liquid inside the pipe, $\bar{v}_c = 0$.",
                r"Surfaces: $\Sigma_i$ (inlet, $\bar{n} = -\bar{e}_x$, $\bar{v} = v_i\bar{e}_x$), $\Sigma_o$ (outlet, $\bar{n} = -\bar{e}_z$, $\bar{v} = -v_o\bar{e}_z$), $\Sigma_w$ (pipe wall, $\bar{v} = 0$).",
            ]),
            ("p", r"Force of the liquid and the ambient air on the pipe, and heat through the walls, written on $\Sigma_w$:"),
            ("m", r"\boxed{\,\bar{F} = F_x\bar{e}_x + F_z\bar{e}_z = \int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma - \int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma\,}"),
            ("m", r"\boxed{\,\dot{Q} = -\int_{\Sigma_w}\bar{q}\cdot\bar{n}\,d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="Mass (Notes Eq. 3.11)", eq=mass_eq(), cols=[COL_MASS],
                rows=[(r"\Sigma_i", [r"$\rho\,v_i\bar{e}_x\cdot(-\bar{e}_x)A_i = -\rho v_iA_i$"], False),
                      (r"\Sigma_o", [r"$\rho\,(-v_o\bar{e}_z)\cdot(-\bar{e}_z)A_o = +\rho v_oA_o$"], False),
                      (r"\Sigma_w", [r"$0$"], False)],
                result=r"\boxed{\,v_i = \frac{A_o}{A_i}\,v_o\,},\qquad \dot{m} = \rho v_iA_i = \rho v_oA_o \tag{1}")),
            ("bal", dict(
                label="Linear momentum (Notes Eq. 3.36)", eq=mom_eq(), cols=[COL_MFLUX, COL_P, COL_TAU],
                rows=[(r"\Sigma_i", [r"$\rho v_i\bar{e}_x\,(-v_i)A_i = -\rho v_i^2A_i\,\bar{e}_x$", r"$-(p_i - p_a)(-\bar{e}_x)A_i = (p_i - p_a)A_i\,\bar{e}_x$", r"$0$"], False),
                      (r"\Sigma_o", [r"$\rho(-v_o\bar{e}_z)\,(v_o)A_o = -\rho v_o^2A_o\,\bar{e}_z$", r"$0$ (free jet)", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$", r"$\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed $\Sigma_w$ terms: $-\bar{F}$.",
                result=r"-\rho v_i^2A_i\,\bar{e}_x - \rho v_o^2A_o\,\bar{e}_z = (p_i - p_a)A_i\,\bar{e}_x - \bar{F} \;\Longrightarrow\; \boxed{\,F_x = \left[\rho v_i^2 + (p_i - p_a)\right]A_i,\qquad F_z = \rho v_o^2A_o\,} \tag{2}")),
            ("bal", dict(
                label="Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False), cols=ENERGY_COLS,
                rows=[(r"\Sigma_i", [r"$-\dot{m}\left(cT_i + \tfrac{v_i^2}{2}\right)$", r"$+p_iv_iA_i$", r"$0$", r"$0$ (uniform $T$)"], False),
                      (r"\Sigma_o", [r"$+\dot{m}\left(cT_o + \tfrac{v_o^2}{2}\right)$", r"$-p_av_oA_o$", r"$0$", r"$0$ (uniform $T$)"], False),
                      (r"\Sigma_w", [r"$0$", r"$0$ ($\bar{v} = 0$)", r"$0$ ($\bar{v} = 0$)", r"$-\int_{\Sigma_w}\bar{q}\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed $\Sigma_w$ term: $\dot{Q}$. Using (1), $p_iv_iA_i - p_av_oA_o = (p_i - p_a)\,v_oA_o$.",
                result=r"\dot{m}\left[c(T_o - T_i) + \frac{v_o^2 - v_i^2}{2}\right] = (p_i - p_a)\,v_oA_o + \dot{Q} \;\Longrightarrow\; \boxed{\,\dot{Q} = \rho v_oA_o\left[c(T_o - T_i) + \frac{v_o^2 - v_i^2}{2}\right] + (p_a - p_i)\,v_oA_o\,} \tag{3}")),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"$F_x > 0$: the pipe is pushed along the incoming flow by the momentum flux and the gauge pressure at the inlet. $F_z > 0$: the jet leaves downwards, so the pipe is pushed upwards.",
                r"(3) splits the heat into the rise of internal energy, the change of kinetic energy and the flow work. If no heat were exchanged and there were no losses, (3) with $\dot{Q} = 0$ and $T_o = T_i$ would reduce to Bernoulli's equation $p_i + \tfrac{1}{2}\rho v_i^2 = p_a + \tfrac{1}{2}\rho v_o^2$.",
                r"Dimensions (SI): $[\rho v_i^2A_i] = [(p_i - p_a)A_i] = \text{N}$; $[\rho v_oA_o\,c\,\Delta T] = (\text{kg/s})(\text{J/(kg K)})\,\text{K} = \text{W}$; $[(p_a - p_i)v_oA_o] = \text{Pa}\cdot\text{m}^3/\text{s} = \text{W}$.",
                rf"Numerical illustration (hypothetical data): water, $c = 4186$ J/(kg K), $A_i = 0.01$ m$^2$, $A_o = 0.004$ m$^2$, $v_o = 6$ m/s, $p_i = 1.6\times10^5$ Pa, $p_a = 101325$ Pa, $T_o - T_i = 0.5$ K give $v_i = {f(_vi)}$ m/s, $F_x = {f(_Fx6)}$ N, $F_z = {f(_Fz6)}$ N and $\dot{{Q}} = {f(_Q6)}$ W.",
                r"Agreement with the official and class solutions: (1), (2) and (3) are the results of CL6.pdf (which labels the vertical axis $y$: $F_y = \rho v_o^2A_o$) and of the class notes.",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL7
_G, _Ts, _Ta, _pa7, _A7, _R7, _Rg, _cp, _tb = 0.5, 350., 293., 101325., 0.05, 0.05, 287., 1005., 0.5
_rhoa, _rhos = _pa7 / (_Rg * _Ta), _pa7 / (_Rg * _Ts)
_vr = _G / (_rhoa * _A7)
_vz = _G / (_rhos * math.pi * _R7 ** 2)
_vt = _vz * _tb
_F7 = _G * _vz
_M7 = 2 / 3 * _R7 * _G * _vt
_P7 = _G * ((_cp * _Ts + (_vt ** 2 + _vz ** 2) / 2) - (_cp * _Ta + _vr ** 2 / 2))
CL7 = dict(
    id="cl7", pill="CL7: Dryer",
    title="Industrial Dryer: Velocities, Force, Power and Torque",
    note_title="Problem - CL7 Industrial Dryer",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-angular", "energia", "secador"],
    tags_html=["Axisymmetric", "Angular momentum", "Energy", "Ideal gas"],
    statement=[
        ("p", r"The axisymmetric industrial dryer of the figure in CL7.pdf is designed to provide a steady hot jet of radius $R$, mass flux $G$, and temperature $T_s$. Air enters the dryer from the ambient, at temperature and pressure $T_a$ and $p_a$, through a radial inlet of surface $A$. Inside the dryer there exists an electric resistance that releases an amount of heat $Q$ per unit time, as well as a fan of power $W$ (work per unit time). Because of the presence of the fan, the air velocity at the exit has both azimuthal and axial components, $v_\theta$ and $v_z$, such that $v_\theta/v_z = \tan(\beta)$. In the analysis, assume that the fan and the inner walls of the dryer are thermally insulated, that the air behaves as an ideal gas with constant $R_g$ and specific heat at constant pressure $c_p$, that gravity has a negligible effect on the fluid motion, and that the flow properties are uniform at the inlet and outlet sections. For given values of $G$, $T_s$, $T_a$, $p_a$, $A$, $R$, $R_g$, $c_p$ and $\tan(\beta)$, determine:"),
        ("ul", [r"The velocity at the entrance section $v_r$ as well as the two velocity components at the exit $v_\theta$ and $v_z$.", r"The force acting on the dryer, indicating clearly its magnitude and direction.", r"The total power required to run the dryer $Q + W$.", r"The torque acting on the dryer."]),
    ],
    source_line=r"Source: CL7.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.35, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady (on average) axisymmetric flow; ideal gas $p = \rho R_gT$, so $h = e + p/\rho = c_pT$; neglect $\bar{g}$; uniform properties at inlet and outlet.",
                r"Inlet: air taken from the ambient, with $p = p_a$, $T = T_a$, $\rho_a = p_a/(R_gT_a)$ and radial velocity $v_r$ pointing inwards (as in the official solution). Exit: free jet, $p = p_a$, $T = T_s$, $\rho_s = p_a/(R_gT_s)$, velocity $v_z\bar{e}_z + v_\theta\bar{e}_\theta$ uniform over the disc of radius $R$.",
                r"$G$ is the mass flow rate of the jet (kg/s), as used in the official solution ($G = \rho_av_rA$). Fan and inner walls insulated; the resistance releases $\dot{Q}$; the fan delivers the power $\dot{W}$ to the air.",
                r"Data: $[G,\ T_s,\ T_a,\ p_a,\ A,\ R,\ R_g,\ c_p,\ \tan\beta]$. Unknowns: $[v_r,\ v_z,\ v_\theta,\ \bar{F},\ \dot{Q} + \dot{W},\ \bar{M}]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$G$", "mass flow rate", "kg/s"],
                [r"$A$, $R$", "inlet area, jet radius", r"m$^2$, m"],
                [r"$v_r$, $v_z$, $v_\theta$", "inlet and exit velocities", "m/s"],
                [r"$R_g$, $c_p$", r"gas constant, specific heat", r"J/(kg$\cdot$K)"],
                [r"$\bar{F}$, $\bar{M}$", "force and torque on the dryer", r"N, N$\cdot$m"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the dryer; cylindrical basis $(\bar{e}_r, \bar{e}_\theta, \bar{e}_z)$ with $\bar{e}_z$ along the axis in the jet direction; origin on the axis. By axisymmetry $\int\bar{e}_r\,d\theta = \int\bar{e}_\theta\,d\theta = 0$ over a full turn.",
                r"Surfaces: $\Sigma_1$ (radial inlet, area $A$, $\bar{n} = \bar{e}_r$, $\bar{v} = -v_r\bar{e}_r$), $\Sigma_2$ (exit disc, $\bar{n} = \bar{e}_z$), $\Sigma_w$ (fixed casing and resistance, $\bar{v} = 0$) and $\Sigma_m$ (fan blades, $\bar{v} = \bar{v}_c$).",
            ]),
            ("p", r"Force and torque of the air (inside, and ambient outside) on the dryer, and the heat and work exchanged:"),
            ("m", r"\boxed{\,\bar{F} = \int_{\Sigma_w,\Sigma_m}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
            ("m", r"\boxed{\,\bar{M} = \int_{\Sigma_w,\Sigma_m}\bar{x}\wedge\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="Mass (Notes Eq. 3.11)", eq=mass_eq(moving=True), cols=[r"\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma"],
                rows=[(r"\Sigma_1", [r"$\rho_a(-v_r)A = -\rho_av_rA$"], False),
                      (r"\Sigma_2", [r"$\rho_sv_z\pi R^2$"], False),
                      (r"\Sigma_w,\ \Sigma_m", [r"$0$"], False)],
                result=r"G = \frac{p_a}{R_gT_a}\,v_rA = \frac{p_a}{R_gT_s}\,v_z\pi R^2 \;\Longrightarrow\; \boxed{\,v_r = \frac{GR_gT_a}{p_aA},\qquad v_z = \frac{GR_gT_s}{p_a\pi R^2},\qquad v_\theta = v_z\tan\beta\,} \tag{1}")),
            ("bal", dict(
                label="Linear momentum (Notes Eq. 3.35)", eq=mom_eq(moving=True), cols=[r"\int\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma", COL_P, COL_TAU],
                rows=[(r"\Sigma_1", [r"$\rho_av_r^2\int_{\Sigma_1}\bar{e}_r\,d\sigma = 0$ (axisymmetric)", r"$0$ ($p = p_a$)", r"$0$"], False),
                      (r"\Sigma_2", [r"$\rho_sv_z\int_{\Sigma_2}(v_z\bar{e}_z + v_\theta\bar{e}_\theta)\,d\sigma = \rho_sv_z^2\pi R^2\,\bar{e}_z$", r"$0$ (free jet)", r"$0$"], False),
                      (r"\Sigma_w,\ \Sigma_m", [r"$0$", r"$-\int(p - p_a)\,\bar{n}\,d\sigma$", r"$\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed terms: $-\bar{F}$. On $\Sigma_2$, $\int_{\Sigma_2}\bar{e}_\theta\,d\sigma = 0$, so the swirl gives no force.",
                result=r"\rho_sv_z^2\pi R^2\,\bar{e}_z = -\bar{F} \;\Longrightarrow\; \boxed{\,\bar{F} = -\frac{p_a}{R_gT_s}\,v_z^2\,\pi R^2\,\bar{e}_z = -G\,v_z\,\bar{e}_z\,} \tag{2}")),
            ("bal", dict(
                label="Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False, moving=True), cols=ENERGY_COLS,
                rows=[(r"\Sigma_1", [r"$-G\left(e_a + \tfrac{v_r^2}{2}\right)$", r"$+p_av_rA$", r"$0$", r"$0$"], False),
                      (r"\Sigma_2", [r"$+G\left(e_s + \tfrac{v_\theta^2 + v_z^2}{2}\right)$", r"$-p_av_z\pi R^2$", r"$0$", r"$0$"], False),
                      (r"\Sigma_m", [r"$0$", r"$-\int_{\Sigma_m}p\,\bar{v}\cdot\bar{n}\,d\sigma$", r"$\int_{\Sigma_m}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$", r"$0$ (insulated)"], True),
                      (r"\Sigma_w", [r"$0$", r"$0$", r"$0$", r"$-\int_{\Sigma_w}\bar{q}\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed terms: the work on $\Sigma_m$ is the fan power $\dot{W}$; the heat through $\Sigma_w$ (only the resistance, the walls are insulated) is $\dot{Q}$. With $p_av_rA = G\,p_a/\rho_a$ and $p_av_z\pi R^2 = G\,p_a/\rho_s$, $e + p/\rho = c_pT$:",
                result=r"\boxed{\,\dot{Q} + \dot{W} = G\left[\left(c_pT_s + \frac{v_\theta^2 + v_z^2}{2}\right) - \left(c_pT_a + \frac{v_r^2}{2}\right)\right]\,} \tag{3}")),
            ("bal", dict(
                label="Angular momentum about the origin, z component (Notes Eq. 3.38)",
                eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho\,\bar{x}\wedge\bar{v}\,dV", "0") + r" + \int_{\Sigma_c}\rho\,(\bar{x}\wedge\bar{v})[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma",
                cols=[r"\int\rho\,(\bar{x}\wedge\bar{v})_z\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma", r"\text{pressure and viscous moments}"],
                rows=[(r"\Sigma_1", [r"$0$ ($\bar{x}\wedge(-v_r\bar{e}_r) = -zv_r\,\bar{e}_\theta$, no $z$ component)", r"$0$"], False),
                      (r"\Sigma_2", [r"$\int_0^R\rho_sv_z\,(rv_\theta)\,2\pi r\,dr = \rho_sv_zv_\theta\,\frac{2\pi R^3}{3}$", r"$0$"], False),
                      (r"\Sigma_w,\ \Sigma_m", [r"$0$", r"$-\bar{M}\cdot\bar{e}_z$"], True)],
                wall=r"On $\Sigma_2$, $\bar{x} = r\bar{e}_r + z_2\bar{e}_z$ and $\bar{x}\wedge(v_z\bar{e}_z + v_\theta\bar{e}_\theta) = -rv_z\bar{e}_\theta + rv_\theta\bar{e}_z - z_2v_\theta\bar{e}_r$; only $rv_\theta\bar{e}_z$ survives the integral. The antiderivative of $r^2$ is $r^3/3$, and Barrow's rule between $0$ and $R$ gives $R^3/3$.",
                result=r"\boxed{\,\bar{M} = -\rho_sv_zv_\theta\,\frac{2\pi R^3}{3}\,\bar{e}_z = -\frac{2}{3}\,R\,G\,v_\theta\,\bar{e}_z\,} \tag{4}")),
            ("note", "Erratum in the official solution (slip in the boxed result)", r"CL7.pdf writes the momentum balance as $\frac{p_a}{R_gT_s}v_z^2\pi R^2\bar{e}_z = -\bar{F}$ but boxes $\bar{F} = -\frac{p_a}{R_gT_s}v_z^2\bar{e}_z$, without the area $\pi R^2$. That expression has units of pressure, not force; the correct result is (2)."),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"The radial inflow gives no net momentum (axisymmetry), so the force is the reaction to the jet: magnitude $Gv_z$, direction $-\bar{e}_z$ (opposite to the jet).",
                r"The swirl gives no force but gives a torque: the fan sets the air rotating, and the air reacts on the dryer with $\bar{M}$ opposite to the swirl. For $\beta = 0$, $v_\theta = 0$ and $\bar{M} = 0$.",
                r"(3): the electric and mechanical power go into heating the air from $T_a$ to $T_s$ and into its kinetic energy.",
                r"Dimensions (SI): $[Gv_z] = \text{N}$; $[RGv_\theta] = \text{m}\cdot(\text{kg/s})(\text{m/s}) = \text{N}\cdot\text{m}$; $[Gc_pT] = \text{W}$.",
                rf"Numerical illustration (hypothetical data): $G = 0.5$ kg/s, $T_s = 350$ K, $T_a = 293$ K, $p_a = 101325$ Pa, $A = 0.05$ m$^2$, $R = 0.05$ m, $R_g = 287$ J/(kg K), $c_p = 1005$ J/(kg K), $\tan\beta = 0.5$ give $v_r = {f(_vr)}$ m/s, $v_z = {f(_vz)}$ m/s, $v_\theta = {f(_vt)}$ m/s, $|\bar{{F}}| = {f(_F7)}$ N, $\dot{{Q}} + \dot{{W}} = {f(_P7)}$ W and $|\bar{{M}}| = {f(_M7)}$ N$\cdot$m (a midpoint quadrature of the torque integral gives the same value).",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL8
_r8, _Vj, _Dj, _Ds = 1000., 10., 0.05, 0.02
_F8 = _r8 * _Vj ** 2 * math.pi / 4 * (_Dj ** 2 - _Ds ** 2)
_h8 = (_Dj ** 2 - _Ds ** 2) / (8 * 0.1)
CL8 = dict(
    id="cl8", pill="CL8: Jet on Orifice",
    title="Jet Impinging on a Wall with an Orifice",
    note_title="Problem - CL8 Jet on a Wall with an Orifice",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "chorro", "bernoulli"],
    tags_html=["Free jets", "Bernoulli", "Mass", "Force on a wall"],
    statement=[
        ("p", r"A circular water jet of diameter $D_j$ and velocity $V_j$ impinges perpendicularly to a wall, where there exists an orifice centered at the jet axis, as shown in the figure of CL8.pdf, so that part of the water flows through the orifice and part is deflected to flow next to the wall. Assuming that the flow velocity is sufficiently large for the effects of viscosity and gravity to be negligible:"),
        ("ul", [r"Determine the values of the velocities $V_s$ and $V_r$ for the secondary jet that emerges from the orifice and for the radial wall jet.", r"Obtain the thickness $h(r)$ of the radial wall jet.", r"Compute the force that the jet exerts on the wall as a function of $\rho$, $V_j$, $D_j$ and $D_s$."]),
    ],
    source_line=r"Source: CL8.pdf (page 1). Notes.pdf: Bernoulli's equation Eq. 4.17 (Chapter 4), integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady, incompressible, frictionless (viscosity negligible); neglect $\bar{g}$ (buoyancy-free).",
                r"Free jets surrounded by the ambient air at $p_a$. In each jet away from the wall the streamlines are straight and parallel (aligned), so the pressure does not vary across them: $p = p_a$ inside the incoming jet, the secondary jet and the wall jet (official solution).",
                r"Data: $[\rho,\ V_j,\ D_j,\ D_s]$. Unknowns: $[V_s,\ V_r,\ h(r),\ \bar{F}_w]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$V_j$, $D_j$", "velocity and diameter of the jet", "m/s, m"],
                [r"$V_s$, $D_s$", "secondary jet velocity, orifice diameter", "m/s, m"],
                [r"$V_r$, $h(r)$", "wall-jet velocity and thickness", "m/s, m"],
                [r"$\bar{F}_w$", "force of the jet on the wall", "N"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the wall; $\bar{e}_x$ along the jet axis (towards the wall); cylindrical coordinate $r$ on the wall, with $\int\bar{e}_r\,d\theta = 0$.",
                r"Fixed control volume around the water: $\Sigma_j$ (section of the incoming jet, $\bar{n} = -\bar{e}_x$), $\Sigma_s$ (section of the secondary jet beyond the orifice, $\bar{n} = +\bar{e}_x$), $\Sigma_r$ (cylinder of radius $r$ across the wall jet, $\bar{n} = \bar{e}_r$, height $h$), $\Sigma_a$ (free surfaces, $p = p_a$, $\bar{v}\cdot\bar{n} = 0$) and $\Sigma_w$ (wetted wall).",
            ]),
            ("p", r"Force of the water (and of the ambient air on the dry side) on the wall:"),
            ("m", r"\boxed{\,\bar{F}_w = \int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma - \int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma\,}"),
        ]),
        ("Phase 3", "Bernoulli and Balances, Surface by Surface", [
            ("h4", "3.1 Velocities: Bernoulli along a streamline"),
            ("p", r"Why this tool: for steady, frictionless, incompressible flow without mass forces, $p + \tfrac{1}{2}\rho|\bar{v}|^2$ is constant along a streamline (Notes Eq. 4.17 with $U = 0$, as used in the official solution). Take a streamline from the incoming jet to the wall jet, and another one to the secondary jet; at both ends $p = p_a$:"),
            ("m", r"p_a + \tfrac{1}{2}\rho V_j^2 = p_a + \tfrac{1}{2}\rho V_r^2 \;\Longrightarrow\; \boxed{\,V_r = V_j\,},\qquad p_a + \tfrac{1}{2}\rho V_j^2 = p_a + \tfrac{1}{2}\rho V_s^2 \;\Longrightarrow\; \boxed{\,V_s = V_j\,} \tag{1}"),
            ("bal", dict(
                label="Mass (Notes Eq. 3.11)", eq=mass_eq(), cols=[COL_MASS],
                rows=[(r"\Sigma_j", [r"$-\rho V_j\frac{\pi D_j^2}{4}$"], False),
                      (r"\Sigma_s", [r"$+\rho V_s\frac{\pi D_s^2}{4}$"], False),
                      (r"\Sigma_r", [r"$+\rho V_r\,2\pi r\,h$"], False),
                      (r"\Sigma_a,\ \Sigma_w", [r"$0$"], False)],
                wall=r"With (1), $V_s = V_r = V_j$ and the velocity cancels.",
                result=r"-\frac{\pi D_j^2}{4} + \frac{\pi D_s^2}{4} + 2\pi rh = 0 \;\Longrightarrow\; \boxed{\,h(r) = \frac{D_j^2 - D_s^2}{8\,r}\,} \tag{2}")),
            ("bal", dict(
                label="Linear momentum (Notes Eq. 3.36)", eq=mom_eq(), cols=[COL_MFLUX, COL_P, COL_TAU],
                rows=[(r"\Sigma_j", [r"$\rho V_j\bar{e}_x(-V_j)\frac{\pi D_j^2}{4} = -\rho V_j^2\frac{\pi D_j^2}{4}\bar{e}_x$", r"$0$ ($p = p_a$)", r"$0$"], False),
                      (r"\Sigma_s", [r"$+\rho V_s^2\frac{\pi D_s^2}{4}\bar{e}_x$", r"$0$ ($p = p_a$)", r"$0$"], False),
                      (r"\Sigma_r", [r"$\rho V_r^2h\,r\int_0^{2\pi}\bar{e}_r\,d\theta = 0$", r"$0$ ($p = p_a$)", r"$0$"], False),
                      (r"\Sigma_a", [r"$0$", r"$0$ ($p = p_a$)", r"$0$"], False),
                      (r"\Sigma_w", [r"$0$", r"$-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$", r"$\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed $\Sigma_w$ terms: $-\bar{F}_w$. With (1), $V_s = V_j$.",
                result=r"\left(\rho V_j^2\frac{\pi D_s^2}{4} - \rho V_j^2\frac{\pi D_j^2}{4}\right)\bar{e}_x = -\bar{F}_w \;\Longrightarrow\; \boxed{\,\bar{F}_w = \rho V_j^2\,\frac{\pi}{4}\left(D_j^2 - D_s^2\right)\bar{e}_x\,} \tag{3}")),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"Only the part of the jet stopped by the wall (the annulus between $D_s$ and $D_j$) pushes on it; the secondary jet keeps its momentum. For $D_s \to 0$, $\bar{F}_w \to \rho V_j^2\pi D_j^2/4$, the force of a jet on a flat plate; for $D_s \to D_j$ the jet passes through and $\bar{F}_w \to 0$, $h \to 0$.",
                r"$h \propto 1/r$: the wall jet thins as it spreads, keeping the flow rate $2\pi rhV_j$ constant.",
                r"Dimensions (SI): $[h] = \text{m}^2/\text{m} = \text{m}$; $[\rho V_j^2D^2] = \text{N}$.",
                rf"Numerical illustration (hypothetical data): $\rho = 1000$ kg/m$^3$, $V_j = 10$ m/s, $D_j = 0.05$ m, $D_s = 0.02$ m give $|\bar{{F}}_w| = {f(_F8)}$ N and $h(0.1\ \text{{m}}) = {f(_h8*1000,4)}$ mm.",
                r"Agreement with the official solution: CL8.pdf obtains (1), (2) and (3).",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL9
_r9, _As, _Ae, _W9 = 1000., 0.05, 0.1, 5e4
_Us = (2 * _W9 / (_r9 * _As)) ** (1 / 3)
_Ue = _Us * _As / _Ae
_T9 = _r9 * _As * _Us ** 2 * (1 - 0.5 * _As / _Ae)
CL9 = dict(
    id="cl9", pill="CL9: Submarine Thruster",
    title="Submarine Propulsion Device: Thrust from the Propeller Power",
    note_title="Problem - CL9 Submarine Propulsion Device",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "energia", "propulsion"],
    tags_html=["Thrust", "Bernoulli", "Energy", "Similarity"],
    statement=[
        ("p", r"The submarine propulsion device schematically represented in the figure of CL9.pdf consists of a nozzle, with inlet and outlet cross-section area $A_e$ and $A_s$, and a propeller (printed as 'fan', corrected by hand to 'propeller') located inside, which imparts a rate of work per unit time (power) $\dot{W}$ to the circulating water stream, whose density and viscosity are $\rho$ and $\mu$, respectively. To determine the thrust $T$ produced when the submarine is at rest and at sufficient depth for gravity to have a negligible effect, please follow these steps:"),
        ("ul", [
            r"By application of the continuity equation determine a relationship between the uniform velocities $U_e$ and $U_s$ at the inlet and outlet sections.",
            r"Use the momentum conservation equation to obtain an expression for the thrust (axial force) that the fluid exerts on the propulsion device as a function of the flow conditions at the inlet and outlet. Assume that the pressure surrounding the device is equal to the ambient pressure $p_\infty$.",
            r"Assuming that the flow upstream from the entrance is steady and inviscid, use Bernoulli's equation along a given streamline to find a relationship between the flow conditions in the stagnant atmosphere (1) and at the entrance $e$.",
            r"Use the energy equation to relate the work per unit time $\dot{W}$ with the different fluid variables appearing in the problem. Assume that the variation of internal energy between the inlet and outlet sections is negligible ($e_e = e_s$) and that all of the device walls, including those of the fan, are thermally insulated.",
            r"Combine the above equations to show that the thrust can be expressed in the form $T/(\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}) = f(A_e/A_s)$, obtaining the function $f$.",
        ]),
    ],
    source_line=r"Source: CL9.pdf (page 1). Notes.pdf: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.35, integral total energy balance Eq. 3.46, Bernoulli's equation Eq. 4.17.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady (on average), incompressible water; gravity negligible at depth (it is absorbed in the reduced pressure $p + \rho gz$, as the official solution notes); uniform properties at $e$ and $s$.",
                r"Viscous stresses negligible on the sections ($\rho UD/\mu \gg 1$); the exit jet discharges at the ambient pressure, $p_s = p_\infty$; walls and propeller insulated; $e_e = e_s$.",
                r"Data: $[\rho,\ A_e,\ A_s,\ \dot{W},\ p_\infty]$. Unknowns: $[U_e,\ U_s,\ p_e,\ T]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$A_e$, $A_s$", "inlet and outlet areas", r"m$^2$"],
                [r"$U_e$, $U_s$", "inlet and outlet velocities", "m/s"],
                [r"$p_e$, $p_\infty$", "inlet and ambient pressures", "Pa"],
                [r"$\dot{W}$", "power given by the propeller to the water", "W"],
                [r"$T$", "thrust", "N"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the submarine (at rest), $\bar{e}_x$ along the axis in the direction of the exit jet. The thrust pushes the device towards $-\bar{e}_x$: $\bar{F} = -T\bar{e}_x$ is the force of the water (inside and outside, at $p_\infty$) on the device.",
                r"Surfaces: $\Sigma_e$ (inlet, $\bar{n} = -\bar{e}_x$), $\Sigma_s$ (outlet, $\bar{n} = +\bar{e}_x$), $\Sigma_w$ (nozzle walls, fixed) and $\Sigma_p$ (propeller, moving).",
            ]),
            ("m", r"\boxed{\,\bar{F} = -T\,\bar{e}_x = \int_{\Sigma_w,\Sigma_p}\left[(p - p_\infty)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="(1) Mass (Notes Eq. 3.11)", eq=mass_eq(moving=True), cols=[r"\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma"],
                rows=[(r"\Sigma_e", [r"$-\rho U_eA_e$"], False), (r"\Sigma_s", [r"$+\rho U_sA_s$"], False), (r"\Sigma_w,\ \Sigma_p", [r"$0$"], False)],
                result=r"\boxed{\,U_eA_e = U_sA_s\,} \tag{1}")),
            ("bal", dict(
                label="(2) Linear momentum (Notes Eq. 3.35)", eq=mom_eq(moving=True, pref=r"p_\infty"), cols=[r"\int\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma", COL_P.replace("p_a", r"p_\infty"), COL_TAU],
                rows=[(r"\Sigma_e", [r"$-\rho U_e^2A_e\,\bar{e}_x$", r"$(p_e - p_\infty)A_e\,\bar{e}_x$", r"$0$"], False),
                      (r"\Sigma_s", [r"$+\rho U_s^2A_s\,\bar{e}_x$", r"$0$ ($p_s = p_\infty$)", r"$0$"], False),
                      (r"\Sigma_w,\ \Sigma_p", [r"$0$", r"$-\int(p - p_\infty)\,\bar{n}\,d\sigma$", r"$\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed terms: $-\bar{F} = T\bar{e}_x$. With (1), $\rho U_s^2A_s - \rho U_e^2A_e = \rho U_eA_e(U_s - U_e)$.",
                result=r"\rho U_eA_e(U_s - U_e) = (p_e - p_\infty)A_e + T \;\Longrightarrow\; \boxed{\,T = \rho U_eA_e\,(U_s - U_e) - (p_e - p_\infty)A_e\,} \tag{2}")),
            ("h4", "(3) Bernoulli upstream of the inlet"),
            ("p", r"Steady inviscid flow from the stagnant water far ahead (1), where $v = 0$ and $p = p_\infty$, to the inlet $e$ (Notes Eq. 4.17 with the reduced pressure):"),
            ("m", r"p_\infty = p_e + \tfrac{1}{2}\rho U_e^2 \;\Longrightarrow\; \boxed{\,p_e - p_\infty = -\tfrac{1}{2}\rho U_e^2\,} \tag{3}"),
            ("bal", dict(
                label="(4) Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False, moving=True), cols=ENERGY_COLS,
                rows=[(r"\Sigma_e", [r"$-\rho U_eA_e\left(e_e + \tfrac{U_e^2}{2}\right)$", r"$+p_eU_eA_e$", r"$0$", r"$0$"], False),
                      (r"\Sigma_s", [r"$+\rho U_sA_s\left(e_s + \tfrac{U_s^2}{2}\right)$", r"$-p_\infty U_sA_s$", r"$0$", r"$0$"], False),
                      (r"\Sigma_p", [r"$0$", r"$-\int_{\Sigma_p}p\,\bar{v}\cdot\bar{n}\,d\sigma$", r"$\int_{\Sigma_p}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$", r"$0$ (insulated)"], True),
                      (r"\Sigma_w", [r"$0$", r"$0$", r"$0$", r"$0$ (insulated)"], False)],
                wall=r"Boxed $\Sigma_p$ terms: the propeller power $\dot{W}$. With $e_e = e_s$, $\rho U_eA_e = \rho U_sA_s = \dot{m}$ and (3):",
                result=r"\dot{W} = \dot{m}\left[\frac{p_\infty - p_e}{\rho} + \frac{U_s^2 - U_e^2}{2}\right] = \dot{m}\left[\frac{U_e^2}{2} + \frac{U_s^2 - U_e^2}{2}\right] \;\Longrightarrow\; \boxed{\,\dot{W} = \tfrac{1}{2}\rho A_sU_s^3,\qquad U_s = \left(\frac{2\dot{W}}{\rho A_s}\right)^{1/3}\,} \tag{4}")),
            ("h4", "(5) Thrust in similarity form"),
            ("p", r"Substituting (3) into (2) and using (1), $U_eA_e = U_sA_s$ and $U_e = U_sA_s/A_e$:"),
            ("m", r"T = \rho U_eA_e(U_s - U_e) + \tfrac{1}{2}\rho U_e^2A_e = \rho U_eA_e\left(U_s - \frac{U_e}{2}\right) = \rho A_sU_s\left(U_s - \frac{U_s}{2}\frac{A_s}{A_e}\right) = \rho A_sU_s^2\left(1 - \frac{1}{2}\frac{A_s}{A_e}\right)."),
            ("p", r"With (4), $\rho A_sU_s^2 = \rho A_s\left(\frac{2\dot{W}}{\rho A_s}\right)^{2/3} = 2^{2/3}\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}$, so"),
            ("m", r"\boxed{\,\frac{T}{\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}} = f\!\left(\frac{A_e}{A_s}\right) = 2^{2/3}\left(1 - \frac{1}{2\,A_e/A_s}\right)\,} \tag{5}"),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"$f$ grows with $A_e/A_s$: a large intake (slow inflow, small suction depression at the inlet) gives the most thrust for a given power, tending to $f \to 2^{2/3} \approx 1.587$ as $A_e/A_s \to \infty$. For $A_e = A_s$, $f = 2^{2/3}/2 \approx 0.794$.",
                r"Thrust grows only as $\dot{W}^{2/3}$: doubling the power gives $2^{2/3} \approx 1.59$ times the thrust, because the extra power goes into a faster jet whose kinetic energy is wasted.",
                r"Dimensions (SI): $[\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}] = (\text{kg/m}^3)^{1/3}(\text{kg m}^2/\text{s}^3)^{2/3}(\text{m}^2)^{1/3} = \text{kg}\cdot\text{m/s}^2 = \text{N}$, so $f$ is dimensionless.",
                rf"Numerical check (hypothetical data): $\rho = 1000$ kg/m$^3$, $A_s = 0.05$ m$^2$, $A_e = 0.1$ m$^2$, $\dot{{W}} = 50$ kW give $U_s = {f(_Us)}$ m/s, $U_e = {f(_Ue)}$ m/s, $T = {f(_T9)}$ N, and $T/(\rho^{{1/3}}\dot{{W}}^{{2/3}}A_s^{{1/3}}) = {f(2**(2/3)*(1-0.5*_As/_Ae))} = f(2)$; the energy balance (4) gives back $\dot{{W}} = 50$ kW.",
                r"Agreement with the official solution: CL9.pdf obtains (1) to (5), $f = 2^{2/3}\left(1 - \tfrac{1}{2}A_s/A_e\right)$.",
            ]),
        ]),
    ],
)

# ---------------------------------------------------------------- CL10
_De, _Ds10, _r10, _mu, _W10, _pa10 = 2.0, 0.1, 1.2, 1.8e-5, 1000.0, 101300.0
_Us10 = (8 * _W10 / (_r10 * math.pi * _Ds10 ** 2)) ** (1 / 3)
_Ue10 = _Us10 * (_Ds10 / _De) ** 2
_pe10 = _pa10 - 0.5 * _r10 * _Ue10 ** 2
_Fx10 = -_r10 * _Us10 ** 2 * math.pi * _Ds10 ** 2 / 4
_Fy10 = _r10 * _Ue10 ** 2 * math.pi * _De ** 2 / 8
CL10 = dict(
    id="cl10", pill="CL10: Ventilator",
    title="Ventilation Device: Velocities, Force and Fan Power",
    note_title="Problem - CL10 Ventilation Device",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "energia", "ventilador"],
    tags_html=["Fan", "Bernoulli", "Linear momentum", "Numerical values"],
    statement=[
        ("p", r"The ventilation device shown in the figure of CL10.pdf takes air out of a room at pressure $p_a$ through a circular nozzle of diameter $D_e$. The air is discharged to the open atmosphere, also at pressure $p_a$, through a pipe of diameter $D_s < D_e$. To force the air motion the device includes a fan, which exerts a rate of work per unit time $\dot{W}$ on the air stream. To simplify the solution you may assume that the air density $\rho$ and viscosity $\mu$ are constant and that gravity has a negligible effect."),
        ("ul", [
            r"Using the continuity equation, obtain a relationship between the values of the velocity at the entrance and exit sections $U_e$ and $U_s$, assumed to be uniform.",
            r"Make use of Bernoulli's equation upstream from the entrance section (i.e., along a stream line between (0) and (e)) to obtain an equation for the pressure and velocity at the entrance section $p_e$ and $U_e$.",
            r"Determine the two components of the force $F_x$ and $F_y$ acting on the device. Include in the computation the contribution of the stagnant surrounding air.",
            r"Use the energy equation to compute the value of $U_s$ as a function of the power $\dot{W}$. Assume that the air temperature has the same values at the entrance and exit sections and that the device is thermally insulated.",
            r"Obtain the numerical values of $U_s$, $U_e$, $p_e$, $F_x$ and $F_y$ for $D_e = 2$ m, $D_s = 0.1$ m, $\rho = 1.2$ kg/m$^3$, $\mu = 1.8\times10^{-5}$ kg/(m$\cdot$s), $\dot{W} = 1000$ W, $p_a = 101300$ Pa. Note: the following quantities are known: $D_e$, $D_s$, $\rho$, $\mu$, $\dot{W}$, $p_a$.",
        ]),
    ],
    source_line=r"Source: CL10.pdf (page 1). Notes.pdf: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.35, integral total energy balance Eq. 3.46, Bernoulli's equation Eq. 4.17.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady, constant $\rho$ and $\mu$; neglect $\bar{g}$; uniform properties at $e$ and $s$; same temperature at $e$ and $s$ ($e_e = e_s$); device insulated.",
                r"The air in the room far from the inlet is at rest at $p_a$ (point 0); the exit is a free jet at $p_a$; the outer surface of the device is surrounded by stagnant air at $p_a$ (included through the gauge pressure).",
                r"Geometry (figure): the inlet faces downwards, air enters along $+\bar{e}_y$; the exit pipe points along $+\bar{e}_x$.",
                r"Data: $[D_e,\ D_s,\ \rho,\ \mu,\ \dot{W},\ p_a]$. Unknowns: $[U_e,\ U_s,\ p_e,\ F_x,\ F_y]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$D_e$, $D_s$", "inlet and exit diameters", "m"],
                [r"$U_e$, $U_s$", "inlet and exit velocities", "m/s"],
                [r"$p_e$, $p_a$", "inlet and ambient pressures", "Pa"],
                [r"$\dot{W}$", "fan power given to the air", "W"],
                [r"$F_x$, $F_y$", "force on the device", "N"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the device: $\bar{e}_x$ horizontal (exit direction), $\bar{e}_y$ vertical upwards (inlet flow direction).",
                r"Surfaces: $\Sigma_e$ (inlet, $\bar{n} = -\bar{e}_y$, $\bar{v} = U_e\bar{e}_y$), $\Sigma_s$ (exit, $\bar{n} = +\bar{e}_x$, $\bar{v} = U_s\bar{e}_x$), $\Sigma_w$ (fixed walls) and $\Sigma_m$ (fan).",
            ]),
            ("m", r"\boxed{\,\bar{F} = F_x\bar{e}_x + F_y\bar{e}_y = \int_{\Sigma_w,\Sigma_m}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="(1) Mass (Notes Eq. 3.11)", eq=mass_eq(moving=True), cols=[r"\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma"],
                rows=[(r"\Sigma_e", [r"$-\rho U_e\frac{\pi D_e^2}{4}$"], False), (r"\Sigma_s", [r"$+\rho U_s\frac{\pi D_s^2}{4}$"], False), (r"\Sigma_w,\ \Sigma_m", [r"$0$"], False)],
                result=r"\boxed{\,U_e\,D_e^2 = U_s\,D_s^2\,} \tag{1}")),
            ("h4", "(2) Bernoulli from the room (0) to the inlet (e)"),
            ("m", r"p_a + 0 = p_e + \tfrac{1}{2}\rho U_e^2 \;\Longrightarrow\; \boxed{\,p_e = p_a - \tfrac{1}{2}\rho U_e^2\,} \tag{2}"),
            ("bal", dict(
                label="(3) Linear momentum (Notes Eq. 3.35)", eq=mom_eq(moving=True), cols=[r"\int\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma", COL_P, COL_TAU],
                rows=[(r"\Sigma_e", [r"$\rho U_e\bar{e}_y(-U_e)\frac{\pi D_e^2}{4} = -\rho U_e^2\frac{\pi D_e^2}{4}\bar{e}_y$", r"$-(p_e - p_a)(-\bar{e}_y)\frac{\pi D_e^2}{4} = (p_e - p_a)\frac{\pi D_e^2}{4}\bar{e}_y$", r"$0$"], False),
                      (r"\Sigma_s", [r"$+\rho U_s^2\frac{\pi D_s^2}{4}\bar{e}_x$", r"$0$ (free jet)", r"$0$"], False),
                      (r"\Sigma_w,\ \Sigma_m", [r"$0$", r"$-\int(p - p_a)\,\bar{n}\,d\sigma$", r"$\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True)],
                wall=r"Boxed terms: $-\bar{F}$.",
                result=r"\boxed{\,F_x = -\rho U_s^2\frac{\pi D_s^2}{4},\qquad F_y = \rho U_e^2\frac{\pi D_e^2}{4} + (p_e - p_a)\frac{\pi D_e^2}{4} = \rho U_e^2\frac{\pi D_e^2}{8}\,} \tag{3}")),
            ("p", r"The last form of $F_y$ uses (2): $(p_e - p_a) = -\tfrac{1}{2}\rho U_e^2$."),
            ("bal", dict(
                label="(4) Total energy (Notes Eq. 3.46)", eq=energy_eq(volume_heat=False, moving=True), cols=ENERGY_COLS,
                rows=[(r"\Sigma_e", [r"$-\dot{m}\left(e_e + \tfrac{U_e^2}{2}\right)$", r"$+p_eU_e\frac{\pi D_e^2}{4}$", r"$0$", r"$0$"], False),
                      (r"\Sigma_s", [r"$+\dot{m}\left(e_s + \tfrac{U_s^2}{2}\right)$", r"$-p_aU_s\frac{\pi D_s^2}{4}$", r"$0$", r"$0$"], False),
                      (r"\Sigma_m", [r"$0$", r"$-\int_{\Sigma_m}p\,\bar{v}\cdot\bar{n}\,d\sigma$", r"$\int_{\Sigma_m}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$", r"$0$"], True),
                      (r"\Sigma_w", [r"$0$", r"$0$", r"$0$", r"$0$ (insulated)"], False)],
                wall=r"Boxed $\Sigma_m$ terms: the fan power $\dot{W}$. With $e_e = e_s$, $\dot{m} = \rho U_s\pi D_s^2/4$ and (2), $\frac{p_a - p_e}{\rho} = \frac{U_e^2}{2}$:",
                result=r"\dot{W} = \dot{m}\left[\frac{p_a - p_e}{\rho} + \frac{U_s^2 - U_e^2}{2}\right] = \dot{m}\,\frac{U_s^2}{2} \;\Longrightarrow\; \boxed{\,\dot{W} = \rho\,\frac{\pi D_s^2}{8}\,U_s^3,\qquad U_s = \left(\frac{8\dot{W}}{\rho\pi D_s^2}\right)^{1/3}\,} \tag{4}")),
            ("h4", "(5) Numerical values"),
            ("table", ["Quantity", "Expression", "Value"], [
                [r"$U_s$", r"$\left(8\dot{W}/(\rho\pi D_s^2)\right)^{1/3}$", rf"${f(_Us10)}$ m/s"],
                [r"$U_e$", r"$U_s\,(D_s/D_e)^2$", rf"${f(_Ue10)}$ m/s"],
                [r"$p_e$", r"$p_a - \tfrac{1}{2}\rho U_e^2$", rf"${f(_pe10,9)}$ Pa ($p_a - p_e = {f(_pa10-_pe10,3)}$ Pa)"],
                [r"$F_x$", r"$-\rho U_s^2\pi D_s^2/4$", rf"${f(_Fx10)}$ N"],
                [r"$F_y$", r"$\rho U_e^2\pi D_e^2/8$", rf"${f(_Fy10,4)}$ N"],
            ]),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"The large intake makes the inlet velocity tiny ($U_e \approx 0.15$ m/s), so the suction depression $p_a - p_e$ and $F_y$ are negligible; the force is the reaction to the exit jet, $F_x < 0$ (opposite to the jet).",
                r"The Reynolds numbers, $\rho U_sD_s/\mu \approx 4\times10^5$ and $\rho U_eD_e/\mu \approx 2\times10^4$, are large, which supports neglecting viscous stresses on the sections and using Bernoulli upstream of the inlet (this is where $\mu$ enters).",
                r"Dimensions (SI): $[\rho D_s^2U_s^3] = (\text{kg/m}^3)\,\text{m}^2(\text{m/s})^3 = \text{W}$; $[\rho U^2D^2] = \text{N}$.",
                r"Agreement with the official solution: CL10.pdf obtains (1) to (4), with $F_x = -\rho U_s^2\pi D_s^2/4$, $F_y = \rho U_e^2\pi D_e^2/4 + (p_e - p_a)\pi D_e^2/4$ and $\dot{W} = \rho\pi D_s^2U_s^3/8$; it does not write out the numbers of part 5.",
            ]),
        ]),
    ],
)

PROBLEMS = [CL6, CL7, CL8, CL9, CL10]
