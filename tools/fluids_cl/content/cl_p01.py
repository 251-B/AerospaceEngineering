# CL1 to CL5 in the class style.
import math
from clcommon import *

# ---------------------------------------------------------------- CL1
CL1 = dict(
    id="cl1", pill="CL1: Airfoil Wake",
    title="Airfoil Wake: Streamline Displacement and Drag",
    note_title="Problem - CL1 Airfoil Wake and Drag",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "estela", "resistencia"],
    tags_html=["Control volume", "Linear momentum", "Wake", "Drag"],
    statement=[("p", r"The experimental tests of an airfoil in a wind tunnel indicate that the velocity profile upstream remains uniform, whereas behind the airfoil there exists a wake region with significant velocity deficit whose thickness increases downstream, resulting in the flow field sketched in the figure of CL1.pdf. For the airfoil tested, the velocity measurements at a given downstream section reveal that the velocity in the wake varies linearly from the value $u = U/2$ at the centerline to reach the value $u = U$ at the edge of the wake, located at $y = y_0$. To analyze the problem, consider a control volume limited laterally by the streamlines that extend from $x \to -\infty$, $y = \pm y_{-\infty}$ ($y_{-\infty} < y_0$) to $x = x_0$, $y = \pm y_0$ and internally by the surface of the airfoil. Assuming that the air behaves as an incompressible fluid with density $\rho$ and that viscous stresses are negligible both in the wake and along the bounding streamlines, obtain the value of $y_{-\infty}$ as a function of $y_0$, as well as the value of the drag on the airfoil as a function of $\rho$, $y_0$ and $U$. In the analysis, assume that on the outer boundary of the control volume the pressure differences from the ambient value $p_\infty$ are negligible, and so is the effect of gravity on the air flow.")],
    source_line=r"Source: CL1.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eqs. 3.10-3.11, integral momentum balance Eqs. 3.35-3.36, force of the fluid on a body Eq. 3.32.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady, planar (everything per unit span), incompressible ($\rho$ constant); neglect $\bar{g}$.",
                r"Viscous stresses negligible in the wake and on the bounding streamlines; $p - p_\infty \simeq 0$ on the whole outer boundary of the control volume (given). On the airfoil surface pressure and viscous stresses are **not** neglected: they make the drag.",
                r"Wake profile at $x = x_0$ (symmetric about $y = 0$): $v_x = \tfrac{U}{2}\left(1 + \tfrac{|y|}{y_0}\right)$ for $|y| \le y_0$, and $v_x = U$ outside.",
                r"Data: $[\rho,\ U,\ y_0]$. Unknowns: $[y_{-\infty},\ D]$, with $D$ the drag per unit span.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$U$", "uniform upstream velocity", "m/s"],
                [r"$y_0$", "half-width of the wake at $x = x_0$", "m"],
                [r"$y_{-\infty}$", "half-width of the stream tube far upstream", "m"],
                [r"$\rho$", "air density", r"kg/m$^3$"],
                [r"$D$", "drag per unit span", "N/m"],
            ]),
            ("p", r"Dimensional check of the unknown: $[\rho U^2 y_0] = (\text{kg/m}^3)(\text{m}^2/\text{s}^2)\,\text{m} = \text{N/m}$, a force per unit length, as required for a planar problem."),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Inertial frame fixed to the airfoil and the tunnel; basis $(\bar{e}_x, \bar{e}_y, \bar{e}_z)$ with $\bar{e}_x$ along the stream. The control volume is fixed: $\bar{v}_c = 0$.",
                r"Surfaces of $\Sigma_c$ (outward normal $\bar{n}$): $\Sigma_1$, far upstream, $|y| < y_{-\infty}$, $\bar{n} = -\bar{e}_x$; $\Sigma_2$, the section $x = x_0$, $|y| < y_0$, $\bar{n} = +\bar{e}_x$; $\Sigma_l$, the two bounding streamlines ($\bar{v}\cdot\bar{n} = 0$); $\Sigma_w$, the airfoil surface ($\bar{n}$ pointing into the airfoil).",
                r"Change of variable for the wake integrals: $s = 1 + y/y_0$, $dy = y_0\,ds$; $y \in [0, y_0]$ maps to $s \in [1, 2]$.",
            ]),
            ("p", r"Force of the air on the airfoil (Notes Eq. 3.32), written on the wetted surface with the normal $\bar{n}$ of the control volume:"),
            ("m", r"\boxed{\,\bar{F} = \int_{\Sigma_w}(p - p_\infty)\,\bar{n}\,d\sigma - \int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma\,}"),
            ("p", r"Hence the $\Sigma_w$ terms of the momentum balance add up to $-\bar{F}$."),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="Mass (Notes Eq. 3.11)",
                eq=MASS_FIXED,
                cols=[COL_MASS],
                rows=[
                    (r"\Sigma_1", [r"$\rho\,U\,(-1)\,2y_{-\infty} = -2\rho U y_{-\infty}$"], False),
                    (r"\Sigma_2", [r"$2\rho\int_0^{y_0}\tfrac{U}{2}\left(1 + \tfrac{y}{y_0}\right)dy = \tfrac{3}{2}\rho U y_0$"], False),
                    (r"\Sigma_l", [r"$0$ (streamlines, $\bar{v}\cdot\bar{n} = 0$)"], False),
                    (r"\Sigma_w", [r"$0$ (impermeable wall)"], False),
                ],
                result=r"-2\rho U y_{-\infty} + \frac{3}{2}\rho U y_0 = 0 \;\Longrightarrow\; \boxed{\,y_{-\infty} = \frac{3}{4}\,y_0\,} \tag{1}",
            )),
            ("p", r"The $\Sigma_2$ entry in detail: the antiderivative of $1 + y/y_0$ is $y + y^2/(2y_0)$, and by Barrow's rule between $y = 0$ and $y = y_0$, $\rho U\left[y + \frac{y^2}{2y_0}\right]_0^{y_0} = \rho U\left(y_0 + \frac{y_0}{2}\right) = \frac{3}{2}\rho U y_0$ (the factor 2 of the table counts both halves of the wake)."),
            ("bal", dict(
                label="Linear momentum (Notes Eq. 3.36, with $p_a = p_\\infty$)",
                eq=MOM_FIXED_NOG.replace("p_a", r"p_\infty"),
                cols=[COL_MFLUX, COL_P.replace("p_a", r"p_\infty"), COL_TAU],
                rows=[
                    (r"\Sigma_1", [r"$\rho U\,(-U)\,2y_{-\infty}\,\bar{e}_x = -2\rho U^2y_{-\infty}\,\bar{e}_x$", r"$0$ ($p \simeq p_\infty$)", r"$0$ (uniform flow)"], False),
                    (r"\Sigma_2", [r"$2\rho\int_0^{y_0}v_x^2\,dy\;\bar{e}_x = \tfrac{7}{6}\rho U^2 y_0\,\bar{e}_x$", r"$0$ ($p \simeq p_\infty$)", r"$0$ (given)"], False),
                    (r"\Sigma_l", [r"$0$ ($\bar{v}\cdot\bar{n} = 0$)", r"$0$ ($p \simeq p_\infty$)", r"$0$ (given)"], False),
                    (r"\Sigma_w", [r"$0$ (impermeable)", r"$-\int_{\Sigma_w}(p - p_\infty)\,\bar{n}\,d\sigma$", r"$\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True),
                ],
                wall=r"Boxed $\Sigma_w$ terms: the force of the airfoil on the air, $-\bar{F}$. The $\Sigma_1$ entry uses (1): $-2\rho U^2y_{-\infty} = -\tfrac{3}{2}\rho U^2 y_0$.",
                result=r"-\frac{3}{2}\rho U^2y_0\,\bar{e}_x + \frac{7}{6}\rho U^2y_0\,\bar{e}_x = -\bar{F} \;\Longrightarrow\; \boxed{\,\bar{F} = D\,\bar{e}_x,\qquad D = \frac{1}{3}\,\rho\,U^2\,y_0\,} \tag{2}",
            )),
            ("p", r"The $\Sigma_2$ momentum entry in detail, with $s = 1 + y/y_0$, $dy = y_0\,ds$ and Barrow's rule between $s = 1$ and $s = 2$: $2\rho\frac{U^2}{4}\int_0^{y_0}\left(1 + \frac{y}{y_0}\right)^2dy = \frac{\rho U^2y_0}{2}\int_1^2 s^2\,ds = \frac{\rho U^2y_0}{2}\left[\frac{s^3}{3}\right]_1^2 = \frac{\rho U^2y_0}{2}\cdot\frac{8 - 1}{3} = \frac{7}{6}\rho U^2y_0$. The sum of the flux column is $\left(-\frac{9}{6} + \frac{7}{6}\right)\rho U^2y_0 = -\frac{1}{3}\rho U^2 y_0$."),
            ("p", r"For a wake symmetric about $y = 0$ (a symmetric airfoil at zero incidence, as the symmetric profile implies) the $y$ component of the momentum flux through $\Sigma_2$ cancels between the two halves, so $F_y = 0$: no lift."),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"The wake carries less mass flux ($\tfrac{3}{2}\rho U y_0$) than the undisturbed stream through the same width ($2\rho U y_0$): the bounding streamlines are pushed outwards, from $y_{-\infty} = \tfrac{3}{4}y_0$ to $y_0$. The momentum deficit left in the wake is the drag.",
                r"Limit $y_0 \to 0$: no wake, $y_{-\infty} \to 0$ and $D \to 0$ (d'Alembert's paradox for a frictionless attached flow).",
                r"Dimensions (SI): $[y_{-\infty}] = \text{m}$; $[D] = [\rho U^2 y_0] = \text{N/m}$.",
                r"Numerical cross-check (midpoint quadrature of the defining integrals with $2\times10^5$ cells, $U = 1$ m/s, $\rho = 1.2$ kg/m$^3$, $y_0 = 0.35$ m): $y_{-\infty}/y_0 = 0.75000$ and $D = 0.140000$ N/m $= \rho U^2y_0/3$.",
                r"Agreement with the official solution: CL1.pdf obtains $y_{-\infty} = \tfrac{3}{4}y_0$ and $\bar{F}_{\text{airfoil}} = \tfrac{1}{3}\rho U^2 y_0\,\bar{e}_x$.",
            ]),
            ("note", "Extension (beyond the official solution)", r"With the momentum thickness $\theta = \int_{-y_0}^{y_0}\frac{v_x}{U}\left(1 - \frac{v_x}{U}\right)dy = 2y_0\int_0^1\frac{1 - \sigma^2}{4}\,d\sigma = \frac{y_0}{3}$ ($\sigma = y/y_0$), the result reads $D = \rho U^2\theta$, the classical momentum-deficit formula for the drag from a wake survey."),
        ]),
    ],
)

# ---------------------------------------------------------------- CL2
_g, _h0, _F = 9.81, 0.5, 4.0
_s = math.sqrt(1 + 8 * _F)
_r = (_s - 1) / 2
_Uu = math.sqrt(_F * _g * _h0)
_U1 = _Uu * (1 - 1 / _r)
CL2 = dict(
    id="cl2", pill="CL2: Bore",
    title="Bore over a Stagnant Water Layer",
    note_title="Problem - CL2 Hydraulic Bore",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "resalto", "bore"],
    tags_html=["Moving frame", "Mass and momentum", "Hydrostatic pressure", "Froude number"],
    statement=[("p", r"The bore sketched in the figure of CL2.pdf moves under the action of gravity with constant velocity $U$ over an initially stagnant water layer of thickness $h_0$, leaving behind a layer of thickness $h_1$ moving with velocity $U_1$. Assuming that in the air both viscous stresses and pressure variations with respect to the ambient value $p_a$ are negligible, and so are viscous stresses on the bottom wall, find the values of $U_1$ and $h_1$ as a function of $U$, $h_0$ and $g$. As a preliminary computation, obtain the pressure distributions both upstream and downstream from the bore, verifying that they can be expressed in the form $p = p_a + \rho g(h_0 - z)$ and $p = p_a + \rho g(h_1 - z)$, respectively, where $z$ represents the vertical distance to the bottom wall.")],
    source_line=r"Source: CL2.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eqs. 3.10-3.11, integral momentum balance Eqs. 3.35-3.36.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Planar flow (per unit width) of an incompressible liquid of density $\rho$, with gravity $\bar{g} = -g\,\bar{e}_z$ (here gravity is **not** neglected: it drives the bore).",
                r"The bore advances towards $-\bar{e}_x$ with constant velocity $U$ over the stagnant layer $h_0$; behind it the layer $h_1$ moves with $-U_1\bar{e}_x$. Far from the front the velocity is uniform and horizontal and the free surface is flat at $p = p_a$.",
                r"Viscous stresses negligible in the water sections and on the bottom wall (given); $\mu/(\rho U h) \ll 1$.",
                r"Data: $[U,\ h_0,\ g,\ \rho]$. Unknowns: $[h_1,\ U_1]$ and the pressure distributions.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$U$", "velocity of the bore", "m/s"],
                [r"$U_1$", "velocity of the water behind the bore", "m/s"],
                [r"$h_0$, $h_1$", "layer thickness ahead of and behind the bore", "m"],
                [r"$F = U^2/(gh_0)$", "Froude number of the bore", "1"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Laboratory frame $L$, with $z$ measured from the bottom: unsteady flow, because the front moves.",
                r"Frame of the bore $B$, moving with $-U\bar{e}_x$ relative to $L$. It is inertial (constant velocity), so the balances keep their form, and the flow is steady in it. Velocities: $\bar{v}_B = \bar{v}_L + U\bar{e}_x$, so the water ahead has $U\bar{e}_x$ and the water behind $(U - U_1)\bar{e}_x$.",
                r"Control volume fixed in $B$ ($\bar{v}_c = 0$). Surfaces: $\Sigma_0$, vertical section ahead ($\bar{n} = -\bar{e}_x$, height $h_0$); $\Sigma_1$, vertical section behind ($\bar{n} = +\bar{e}_x$, height $h_1$); $\Sigma_b$, bottom wall ($\bar{n} = -\bar{e}_z$); $\Sigma_s$, free surface (steady material surface in $B$, $p = p_a$).",
            ]),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("h4", "3.1 Preliminary: hydrostatic pressure in the uniform regions"),
            ("p", r"Control volume: a column of width $\Delta x$ in the uniform region ahead, from height $z$ up to the free surface $z = h_0$. Surfaces: $\Sigma_{\text{bot}}$ (at height $z$, $\bar{n} = -\bar{e}_z$), $\Sigma_{\text{top}}$ (free surface, $\bar{n} = +\bar{e}_z$) and two vertical faces $\Sigma_{\text{side}}$ ($\bar{n} = \mp\bar{e}_x$). Only the $z$ component is needed."),
            ("bal", dict(
                label="Momentum, z component, on the column (Notes Eq. 3.36)",
                eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho v_z\,dV", r"0") + r" + \int_{\Sigma_c}\rho v_z\,(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}p\,n_z\,d\sigma + " + crossed(r"\int_{\Sigma_c}(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma", r"\text{negligible}") + r" - \int_{V_c}\rho g\,dV",
                cols=[r"\int\rho v_z\,(\bar{v}\cdot\bar{n})\,d\sigma", r"-\int p\,n_z\,d\sigma"],
                rows=[
                    (r"\Sigma_{\text{bot}}", [r"$0$ ($v_z = 0$)", r"$+p(z)\,\Delta x$"], False),
                    (r"\Sigma_{\text{top}}", [r"$0$ ($v_z = 0$)", r"$-p_a\,\Delta x$"], False),
                    (r"\Sigma_{\text{side}}", [r"$0$ ($v_z = 0$)", r"$0$ ($n_z = 0$)"], False),
                ],
                wall=r"Volume term: $-\int_{V_c}\rho g\,dV = -\rho g\,(h_0 - z)\,\Delta x$ (weight of the column).",
                result=r"0 = p(z)\,\Delta x - p_a\,\Delta x - \rho g\,(h_0 - z)\,\Delta x \;\Longrightarrow\; \boxed{\,p = p_a + \rho g\,(h_0 - z)\,} \tag{1}",
            )),
            ("p", r"The same column taken behind the bore gives $p = p_a + \rho g\,(h_1 - z)$ (1')."),
            ("h4", "3.2 Mass and momentum in the frame of the bore"),
            ("bal", dict(
                label="Mass (Notes Eq. 3.11), frame B",
                eq=MASS_FIXED,
                cols=[COL_MASS],
                rows=[
                    (r"\Sigma_0", [r"$\rho\,U\,(-1)\,h_0 = -\rho U h_0$"], False),
                    (r"\Sigma_1", [r"$\rho\,(U - U_1)\,h_1$"], False),
                    (r"\Sigma_b", [r"$0$ (wall)"], False),
                    (r"\Sigma_s", [r"$0$ (material surface)"], False),
                ],
                result=r"\boxed{\,U\,h_0 = (U - U_1)\,h_1\,} \tag{2}",
            )),
            ("p", r"In the momentum balance $p$ may be replaced by $p - p_a$ because $\int_{\Sigma_c}p_a\bar{n}\,d\sigma = 0$ on a closed surface. The $x$ component is taken (gravity has no $x$ component). On $\Sigma_0$ and $\Sigma_1$ the pressure is (1) and (1'); the antiderivative of $\rho g(h - z)$ is $\rho g(hz - z^2/2)$, and Barrow's rule between $z = 0$ and $z = h$ gives $\rho g h^2/2$."),
            ("bal", dict(
                label="Momentum, x component (Notes Eq. 3.36), frame B",
                eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho v_x\,dV", r"0\ (\text{steady in } B)") + r" + \int_{\Sigma_c}\rho v_x\,(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,n_x\,d\sigma + \int_{\Sigma_c}(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma + " + crossed(r"\int_{V_c}\rho g_x\,dV", r"g_x = 0"),
                cols=[r"\int\rho v_x\,(\bar{v}\cdot\bar{n})\,d\sigma", r"-\int(p - p_a)\,n_x\,d\sigma", r"\int(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma"],
                rows=[
                    (r"\Sigma_0", [r"$\rho U\,(-U)\,h_0 = -\rho U^2h_0$", r"$+\int_0^{h_0}\rho g(h_0 - z)\,dz = \frac{\rho g h_0^2}{2}$", r"$0$"], False),
                    (r"\Sigma_1", [r"$\rho\,(U - U_1)^2\,h_1$", r"$-\int_0^{h_1}\rho g(h_1 - z)\,dz = -\frac{\rho g h_1^2}{2}$", r"$0$"], False),
                    (r"\Sigma_b", [r"$0$", r"$0$ ($n_x = 0$)", r"$0$ (given)"], False),
                    (r"\Sigma_s", [r"$0$", r"$0$ ($p = p_a$)", r"$0$ (air)"], False),
                ],
                result=r"\boxed{\,-\rho U^2 h_0 + \rho\,(U - U_1)^2\,h_1 = \frac{\rho g}{2}\left(h_0^2 - h_1^2\right)\,} \tag{3}",
            )),
            ("h4", "3.3 Solution for $h_1/h_0$ and $U_1/U$"),
            ("p", r"From (2), $U - U_1 = Uh_0/h_1$, so $(U - U_1)^2h_1 = U^2h_0^2/h_1$. Substituting into (3) and dividing by $\rho$:"),
            ("m", r"U^2h_0\left(\frac{h_0}{h_1} - 1\right) = \frac{g}{2}(h_0 - h_1)(h_0 + h_1) \;\Longrightarrow\; U^2h_0\,\frac{h_0 - h_1}{h_1} = \frac{g}{2}(h_0 - h_1)(h_0 + h_1)."),
            ("p", r"For a bore $h_1 \ne h_0$, so $h_0 - h_1$ cancels. With $r = h_1/h_0$ and $F = U^2/(gh_0)$, dividing by $gh_0^2$ gives $F/r = (1 + r)/2$:"),
            ("m", r"r^2 + r - 2F = 0 \;\Longrightarrow\; \boxed{\,\frac{h_1}{h_0} = \frac{1}{2}\left(\sqrt{1 + 8F} - 1\right)\,} \tag{4}"),
            ("p", r"(the negative root is rejected, $h_1 > 0$). From (2), $U_1/U = 1 - h_0/h_1 = (r - 1)/r$; with $s = \sqrt{1 + 8F}$, $r = (s - 1)/2$ and"),
            ("m", r"\boxed{\,\frac{U_1}{U} = 1 - \frac{2}{s - 1} = \frac{\sqrt{1 + 8F} - 3}{\sqrt{1 + 8F} - 1}\,},\qquad F = \frac{U^2}{gh_0}. \tag{5}"),
            ("note", "Erratum in the official solution (reading of the handwriting)", r"CL2.pdf gives $h_1/h_0 = \tfrac{1}{2}(\sqrt{1+8F} - 1)$, as in (4). For the velocity it gives, as legible in the scan, $U_1/U = \tfrac{3}{2}\left(\tfrac{1}{3}\sqrt{1+8F} - 1\right) = (\sqrt{1+8F} - 3)/2 = r - 1$. This contradicts its own continuity equation (2), which requires $U_1/U = (r - 1)/r$; the two coincide only for $r = 1$. Check: (2) gives $(U - U_1)h_1 = Uh_0 > 0$, hence $U_1 < U$, whereas $r - 1 > 1$ for $F > 3$ (for $F = 4$, $r - 1 = 1.3723$ against $U_1/U = 0.5785$ from (5)). The computed value is kept."),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"A bore exists only for $F > 1$: $r > 1 \iff s > 3 \iff F > 1$. $F$ compares the speed of the front with the shallow-water wave speed $\sqrt{gh_0}$.",
                r"Weak bore, $F = 1 + \epsilon$: $r \approx 1 + \tfrac{2}{3}\epsilon$ and $U_1/U \approx \tfrac{2}{3}\epsilon \to 0$ (an infinitesimal gravity wave travelling at $\sqrt{gh_0}$).",
                r"Strong bore, $F \gg 1$: $r \approx \sqrt{2F}$ and $U_1 \to U$.",
                r"Dimensions (SI): both sides of (3) are forces per unit width, $[\rho U^2h_0] = [\rho gh^2] = \text{N/m}$; $F$, $r$ and $U_1/U$ are dimensionless.",
                rf"Numerical cross-check: $F = 4$, $h_0 = 0.5$ m, $g = 9.81$ m/s$^2$ give $U = {f(_Uu)}$ m/s, $h_1/h_0 = {f(_r)}$ ($h_1 = {f(_r*_h0)}$ m), $U_1/U = {f(1-1/_r)}$ ($U_1 = {f(_U1)}$ m/s); the residuals of (2) and (3) are below $10^{{-14}}$ in SI units.",
            ]),
            ("note", "Extension (beyond the official solution)", r"Mechanical energy is not conserved across the bore, so Bernoulli's equation cannot be used between both sections. The head lost is the classical hydraulic-jump value $\Delta H = (h_1 - h_0)^3/(4h_0h_1)$, positive for $h_1 > h_0$."),
        ]),
    ],
)

# ---------------------------------------------------------------- CL3
_rho3, _Ap, _Ao, _Up, _pp, _pa, _H = 1000.0, 0.02, 0.008, 3.0, 2.5e5, 101325.0, 1.5
_Uo = _Ap / _Ao * _Up
_Fx = (_pp - _pa) * _Ap + _rho3 * _Up * (_Up - _Uo) * _Ap
_Mz = -_rho3 * _Uo ** 2 * _H * _Ao
CL3 = dict(
    id="cl3", pill="CL3: Mouthpiece",
    title="Double-Elbow Mouthpiece: Exit Velocity, Force and Moment",
    note_title="Problem - CL3 Double-Elbow Mouthpiece",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "momento-angular", "tobera"],
    tags_html=["Control volume", "Linear momentum", "Angular momentum", "Gauge pressure"],
    statement=[("p", r"The double-elbow mouth piece of exit cross section $A_o$ shown in the figure of CL3.pdf is to be installed at the end of a circular pipe of cross section $A_p$ to redirect the outflow of water into the open atmosphere. Once the mouth piece is installed, the uniform values $U_p$ and $p_p$ are measured for the flow velocity and the pressure at the end of the pipe (i.e., just at the entrance of the mouth piece). Find the value of the uniform velocity at the exit section, $U_o$, as well as the force exerted on the mouth piece and its corresponding moment with respect to the entrance section. (Handwritten addition: neglect the effect of gravity.)")],
    source_line=r"Source: CL3.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eqs. 3.37-3.38, force and moment on a body Eqs. 3.32-3.33.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady, incompressible (water); neglect $\bar{g}$ (handwritten addition); uniform properties at inlet and outlet; viscous stresses negligible on both sections.",
                r"Free jet at the exit: $p = p_a$ over $\Sigma_o$. The thin wall of the mouth piece has the atmosphere $p_a$ on its outer face; the force asked for is the net force of the water inside plus the atmosphere outside, as in the official solution. Ignoring the atmosphere would add $p_a(A_p - A_o)\,\bar{e}_x$.",
                r"Geometry (figure): S-shaped piece; the exit axis is a vertical distance $H$ below the entrance axis; both the entrance and the exit flows are along $+\bar{e}_x$.",
                r"Data: $[\rho,\ A_p,\ A_o,\ U_p,\ p_p,\ p_a,\ H]$. Unknowns: $[U_o,\ \bar{F}_{MP},\ \bar{M}_{MP}]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$A_p$, $A_o$", "entrance and exit areas", r"m$^2$"],
                [r"$U_p$, $p_p$", "velocity and pressure at the entrance", "m/s, Pa"],
                [r"$U_o$", "exit velocity", "m/s"],
                [r"$H$", "vertical offset between the axes", "m"],
                [r"$\bar{F}_{MP}$, $\bar{M}_{MP}$", "force and moment on the mouth piece", r"N, N$\cdot$m"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Inertial frame fixed to the pipe: $\bar{e}_x$ along the pipe axis (flow direction), $\bar{e}_y$ vertical upwards, $\bar{e}_z = \bar{e}_x\wedge\bar{e}_y$ towards the reader. Origin $O$ at the centre of the entrance section (moments about $O$).",
                r"Centre of the exit section: $\bar{x}_o = X\bar{e}_x - H\bar{e}_y$ relative to $O$ ($X$ drops out). Position within a circular section relative to its centre: $\bar{\eta}$, with $\int\bar{\eta}\,d\sigma = 0$.",
                r"Control volume: the water inside the mouth piece, fixed ($\bar{v}_c = 0$). Surfaces: $\Sigma_p$ (entrance, $\bar{n} = -\bar{e}_x$), $\Sigma_o$ (exit, $\bar{n} = +\bar{e}_x$), $\Sigma_w$ (inner wall).",
            ]),
            ("p", r"Force and moment of the water and the atmosphere on the mouth piece, with $\bar{n}$ the outward normal of the control volume:"),
            ("m", r"\boxed{\,\bar{F}_{MP} = \int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma - \int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma\,}"),
            ("m", r"\boxed{\,\bar{M}_{MP} = \int_{\Sigma_w}\bar{x}\wedge\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="Mass (Notes Eq. 3.11)",
                eq=MASS_FIXED,
                cols=[COL_MASS],
                rows=[
                    (r"\Sigma_p", [r"$\rho\,U_p\bar{e}_x\cdot(-\bar{e}_x)\,A_p = -\rho U_pA_p$"], False),
                    (r"\Sigma_o", [r"$\rho\,U_o\bar{e}_x\cdot\bar{e}_x\,A_o = +\rho U_oA_o$"], False),
                    (r"\Sigma_w", [r"$0$ (wall)"], False),
                ],
                result=r"\rho U_pA_p = \rho U_oA_o \;\Longrightarrow\; \boxed{\,U_o = \frac{A_p}{A_o}\,U_p\,},\qquad \dot{m} \equiv \rho U_pA_p = \rho U_oA_o \tag{1}",
            )),
            ("bal", dict(
                label="Linear momentum (Notes Eq. 3.36)",
                eq=MOM_FIXED_NOG,
                cols=[COL_MFLUX, COL_P, COL_TAU],
                rows=[
                    (r"\Sigma_p", [r"$\rho U_p\bar{e}_x\,(-U_p)\,A_p = -\dot{m}\,U_p\bar{e}_x$", r"$-(p_p - p_a)(-\bar{e}_x)A_p = (p_p - p_a)A_p\bar{e}_x$", r"$0$ (uniform)"], False),
                    (r"\Sigma_o", [r"$\rho U_o\bar{e}_x\,(U_o)\,A_o = \dot{m}\,U_o\bar{e}_x$", r"$0$ (free jet, $p = p_a$)", r"$0$ (uniform)"], False),
                    (r"\Sigma_w", [r"$0$", r"$-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$", r"$\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True),
                ],
                wall=r"Boxed $\Sigma_w$ terms: $-\bar{F}_{MP}$.",
                result=r"\dot{m}\,(U_o - U_p)\,\bar{e}_x = (p_p - p_a)A_p\,\bar{e}_x - \bar{F}_{MP} \;\Longrightarrow\; \boxed{\,\bar{F}_{MP} = \left[(p_p - p_a)A_p + \rho U_p\,(U_p - U_o)\,A_p\right]\bar{e}_x\,} \tag{2}",
            )),
            ("p", r"No entry of the table has a component along $\bar{e}_y$ or $\bar{e}_z$, so $F_{MP,y} = F_{MP,z} = 0$."),
            ("bal", dict(
                label="Angular momentum about O (Notes Eq. 3.38)",
                eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho\,\bar{x}\wedge\bar{v}\,dV", r"0") + r" + \int_{\Sigma_c}\rho\,(\bar{x}\wedge\bar{v})(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + " + crossed(r"\int_{V_c}\rho\,\bar{x}\wedge\bar{g}\,dV", r"\text{neglect } \bar{g}"),
                cols=[r"\int\rho\,(\bar{x}\wedge\bar{v})(\bar{v}\cdot\bar{n})\,d\sigma", r"-\int\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma", r"\int\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma"],
                rows=[
                    (r"\Sigma_p", [r"$-\rho U_p^2\left(\int\bar{\eta}\,d\sigma\right)\wedge\bar{e}_x = 0$", r"$(p_p - p_a)\left(\int\bar{\eta}\,d\sigma\right)\wedge\bar{e}_x = 0$", r"$0$"], False),
                    (r"\Sigma_o", [r"$\rho U_o^2A_o\,(\bar{x}_o\wedge\bar{e}_x) = \rho U_o^2HA_o\,\bar{e}_z$", r"$0$ ($p = p_a$)", r"$0$"], False),
                    (r"\Sigma_w", [r"$0$", r"$-\int_{\Sigma_w}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma$", r"$\int_{\Sigma_w}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$"], True),
                ],
                wall=r"Boxed $\Sigma_w$ terms: $-\bar{M}_{MP}$. In the $\Sigma_o$ entry, $\bar{x} = \bar{x}_o + \bar{\eta}$ and $\bar{x}_o\wedge\bar{e}_x = (X\bar{e}_x - H\bar{e}_y)\wedge\bar{e}_x = -H\,\bar{e}_y\wedge\bar{e}_x = +H\,\bar{e}_z$.",
                result=r"\rho U_o^2HA_o\,\bar{e}_z = -\bar{M}_{MP} \;\Longrightarrow\; \boxed{\,\bar{M}_{MP} = -\rho U_o^2HA_o\,\bar{e}_z = -\rho\,\frac{A_p^2}{A_o}\,U_p^2\,H\,\bar{e}_z\,} \tag{3}",
            )),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"$A_o < A_p$ gives $U_o > U_p$: the piece accelerates the water, and the wall supplies the momentum change.",
                r"The moment exists only because the exit axis is offset by $H$: for $H \to 0$, $\bar{M}_{MP} \to 0$. With the exit below the entrance, the moment is clockwise as seen in the figure ($\bar{e}_z$ towards the reader).",
                r"Limit $A_o \to A_p$: $U_o = U_p$ and $\bar{F}_{MP} \to (p_p - p_a)A_p\bar{e}_x$, the pure pressure force.",
                r"Dimensions (SI): $[\rho U_pA_p(U_p - U_o)] = \text{N}$; $[\rho U_o^2HA_o] = \text{N}\cdot\text{m}$.",
                rf"Numerical illustration (hypothetical data): $\rho = 1000$ kg/m$^3$, $A_p = 0.02$ m$^2$, $A_o = 0.008$ m$^2$, $U_p = 3$ m/s, $p_p = 2.5\times10^5$ Pa, $p_a = 101325$ Pa, $H = 1.5$ m give $U_o = {f(_Uo)}$ m/s, $F_{{MP,x}} = {f(_Fx,6)}$ N and $M_{{MP,z}} = {f(_Mz,4)}$ N$\cdot$m.",
                r"Agreement with the official solution: CL3.pdf obtains (1), (2) and (3).",
            ]),
            ("note", "Extension (beyond the official solution)", r"If the flow inside were lossless (not stated), Bernoulli's equation $p_p - p_a = \tfrac{1}{2}\rho(U_o^2 - U_p^2)$ would give $F_{MP,x} = \tfrac{1}{2}\rho A_p(U_o - U_p)^2 \ge 0$. With losses, the measured $p_p$ must be used, as in (2)."),
        ]),
    ],
)

# ---------------------------------------------------------------- CL4
_p1, _rho1, _v1, _L, _Fx4, _Fy4 = 101325.0, 1.2, 100.0, 0.2, 30.0, -80.0
_m = _rho1 * _v1
_P = _p1 + _m * _v1 - _Fx4 / _L
_E = GAM / (GAM - 1) * _p1 / _rho1 + _v1 ** 2 / 2
_v2y = -(_Fy4 / _L) / _m
_a, _b, _c = GAM + 1, -2 * GAM * _P / _m, 2 * (GAM - 1) * (_E - _v2y ** 2 / 2)
_d = math.sqrt(_b * _b - 4 * _a * _c)
_u_lo, _u_hi = (-_b - _d) / (2 * _a), (-_b + _d) / (2 * _a)
_rho2, _p2, _p2_hi = _m / _u_lo, _P - _m * _u_lo, _P - _m * _u_hi
CL4 = dict(
    id="cl4", pill="CL4: Cascade",
    title="Cascade of Aerofoils: Downstream State",
    note_title="Problem - CL4 Cascade of Aerofoils",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "energia", "cascada"],
    tags_html=["Periodicity", "Mass, momentum, energy", "Perfect gas", "Cascade"],
    statement=[("p", r"A planar uniform stream of air with pressure $p_1$, density $\rho_1$ and velocity $\bar{v}_1 = v_{1x}\bar{e}_x$ flows past an array of aerofoils with vertical separation $L$, exerting on each one a force (per unit length) given by $\bar{F} = F_x\bar{e}_x + F_y\bar{e}_y$. Assuming that the aerofoils are thermally insulated and neglecting the effect of gravity, write the equations that determine the values of the pressure $p_2$, density $\rho_2$ and velocity $\bar{v}_2 = v_{2x}\bar{e}_x + v_{2y}\bar{e}_y$ for the uniform stream found sufficiently far downstream.")],
    source_line=r"Source: CL4.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46, force on a body Eq. 3.32.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Steady planar flow through an infinite array of identical aerofoils (pitch $L$), so the flow is periodic in $y$; uniform far upstream (1) and far downstream (2).",
                r"Neglect $\bar{g}$; aerofoils thermally insulated; compressible fluid. Viscous stresses and heat conduction negligible in the uniform sections.",
                r"Perfect gas: $h = e + \frac{p}{\rho} = c_pT = \frac{c_p}{R_g}\frac{p}{\rho} = \frac{\gamma}{\gamma - 1}\frac{p}{\rho}$ (with $p = \rho R_gT$ and $\gamma = c_p/c_v$), as in the class solution.",
                r"Data: $[p_1,\ \rho_1,\ v_{1x},\ L,\ F_x,\ F_y,\ \gamma]$. Unknowns: $[p_2,\ \rho_2,\ v_{2x},\ v_{2y}]$: four equations are needed.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$p_1$, $\rho_1$, $v_{1x}$", "upstream state", r"Pa, kg/m$^3$, m/s"],
                [r"$p_2$, $\rho_2$, $v_{2x}$, $v_{2y}$", "downstream state", r"Pa, kg/m$^3$, m/s"],
                [r"$L$", "pitch of the array", "m"],
                [r"$F_x$, $F_y$", "force on each aerofoil per unit length", "N/m"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the array; $\bar{e}_x$ along the incoming stream, $\bar{e}_y$ along the array. Fixed control volume, $\bar{v}_c = 0$, one period high.",
                r"Surfaces: $\Sigma_1$ (far upstream, height $L$, $\bar{n} = -\bar{e}_x$), $\Sigma_2$ (far downstream, height $L$, $\bar{n} = +\bar{e}_x$), $\Sigma_{l1}$ and $\Sigma_{l2}$ (upper and lower stream surfaces, $\bar{v}\cdot\bar{n} = 0$), $\Sigma_w$ (aerofoil surface, $\bar{v} = 0$, insulated).",
                r"Periodicity: $\Sigma_{l2}$ is $\Sigma_{l1}$ shifted by $-L\bar{e}_y$ with opposite normals, so the integrals of any periodic quantity over $\Sigma_{l1}$ and $\Sigma_{l2}$ cancel each other out.",
            ]),
            ("p", r"Force on each aerofoil (per unit length), with $\bar{n}$ the outward normal of the control volume:"),
            ("m", r"\boxed{\,\bar{F} = F_x\bar{e}_x + F_y\bar{e}_y = \int_{\Sigma_w}p\,\bar{n}\,d\sigma - \int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma\,}"),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="Mass (Notes Eq. 3.11)",
                eq=MASS_FIXED,
                cols=[COL_MASS],
                rows=[
                    (r"\Sigma_1", [r"$\rho_1(-v_{1x})\,L$"], False),
                    (r"\Sigma_2", [r"$\rho_2\,v_{2x}\,L$"], False),
                    (r"\Sigma_{l1},\ \Sigma_{l2}", [r"$0$ (stream surfaces)"], False),
                    (r"\Sigma_w", [r"$0$ (wall)"], False),
                ],
                result=r"\boxed{\,\rho_1v_{1x} = \rho_2v_{2x}\,} \tag{1}",
            )),
            ("bal", dict(
                label="Linear momentum (Notes Eq. 3.36)",
                eq=MOM_FIXED_NOG.replace(r"(p - p_a)", "p"),
                cols=[COL_MFLUX, r"-\int p\,\bar{n}\,d\sigma", COL_TAU],
                rows=[
                    (r"\Sigma_1", [r"$\rho_1v_{1x}\bar{e}_x(-v_{1x})L$", r"$+p_1L\,\bar{e}_x$", r"$0$"], False),
                    (r"\Sigma_2", [r"$\rho_2(v_{2x}\bar{e}_x + v_{2y}\bar{e}_y)\,v_{2x}L$", r"$-p_2L\,\bar{e}_x$", r"$0$"], False),
                    (r"\Sigma_{l1} + \Sigma_{l2}", [r"$0$", r"$0$ (cancel each other out)", r"$0$ (cancel each other out)"], False),
                    (r"\Sigma_w", [r"$0$", r"$-\int_{\Sigma_w}p\,\bar{n}\,d\sigma$", r"$\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True),
                ],
                wall=r"Boxed $\Sigma_w$ terms: $-\bar{F} = -F_x\bar{e}_x - F_y\bar{e}_y$. With (1), $\rho_2v_{2x}L = \rho_1v_{1x}L$ in the $\Sigma_2$ flux.",
                result=r"\boxed{\,F_x = \rho_1v_{1x}L\,(v_{1x} - v_{2x}) + (p_1 - p_2)\,L\,}\ \ \text{(2)}\qquad \boxed{\,F_y = -\rho_1v_{1x}L\,v_{2y}\,}\ \ \text{(3)}",
            )),
            ("bal", dict(
                label="Total energy (Notes Eq. 3.46)",
                eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV", r"0") + r" + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + " + crossed(r"\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV", r"\text{neglect}") + r" - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + " + crossed(r"\int_{V_c}(Q_c + Q_r)\,dV", r"0"),
                cols=[r"\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma", r"-\int p\,\bar{v}\cdot\bar{n}\,d\sigma", r"\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma", r"-\int\bar{q}\cdot\bar{n}\,d\sigma"],
                rows=[
                    (r"\Sigma_1", [r"$\rho_1\left(e_1 + \tfrac{v_{1x}^2}{2}\right)(-v_{1x})L$", r"$+p_1v_{1x}L$", r"$0$", r"$0$"], False),
                    (r"\Sigma_2", [r"$\rho_2\left(e_2 + \tfrac{v_{2x}^2 + v_{2y}^2}{2}\right)v_{2x}L$", r"$-p_2v_{2x}L$", r"$0$", r"$0$"], False),
                    (r"\Sigma_{l1} + \Sigma_{l2}", [r"$0$", r"$0$", r"$0$ (cancel each other out)", r"$0$ (cancel each other out)"], False),
                    (r"\Sigma_w", [r"$0$", r"$0$ ($\bar{v} = 0$)", r"$0$ ($\bar{v} = 0$)", r"$0$ (insulated)"], False),
                ],
                wall=r"Moving the pressure work to the left turns $e$ into $h = e + p/\rho$; dividing by $\rho_1v_{1x}L = \rho_2v_{2x}L$ and using $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$:",
                result=r"\boxed{\,\frac{\gamma}{\gamma - 1}\left(\frac{p_2}{\rho_2} - \frac{p_1}{\rho_1}\right) + \frac{v_{2x}^2 + v_{2y}^2}{2} - \frac{v_{1x}^2}{2} = 0\,} \tag{4}",
            )),
            ("p", r"(1) to (4) are four equations for the four unknowns $p_2$, $\rho_2$, $v_{2x}$, $v_{2y}$, which answers the question."),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"(3): the transverse force on an aerofoil equals minus the $y$ momentum given to the stream; the flow is deflected opposite to the force. (2) splits the streamwise force into a pressure drop and a momentum change.",
                r"$\bar{F} = 0$: (1) to (4) are satisfied by state 2 = state 1. Incompressible limit ($\rho_2 = \rho_1$): $v_{2x} = v_{1x}$ and $p_1 - p_2 = F_x/L$.",
                r"Dimensions (SI): $[F_x/L] = \text{Pa} = [\rho_1v_{1x}^2]$; $[\rho_1v_{1x}Lv_{2y}] = \text{N/m}$; $[\gamma p/((\gamma-1)\rho)] = \text{m}^2/\text{s}^2 = [v^2]$.",
                r"Agreement with the official solution and the class solution: the same four equations (1) to (4).",
            ]),
            ("note", "Extension (beyond the official solution): closed solution", r"With $m = \rho_1v_{1x}$: $\rho_2 = m/v_{2x}$, $v_{2y} = -F_y/(mL)$ and $p_2 = P - m\,v_{2x}$ with $P = p_1 + mv_{1x} - F_x/L$. Substituting into (4), with $E = \frac{\gamma}{\gamma-1}\frac{p_1}{\rho_1} + \frac{v_{1x}^2}{2}$ and the coefficient $\frac{1}{2} - \frac{\gamma}{\gamma-1} = -\frac{\gamma+1}{2(\gamma-1)}$ of $v_{2x}^2$: $(\gamma + 1)v_{2x}^2 - 2\gamma\frac{P}{m}v_{2x} + 2(\gamma - 1)\left(E - \frac{v_{2y}^2}{2}\right) = 0$. For $\bar{F} = 0$ one root is $v_{2x} = v_{1x}$; the root continuous with it is the physical one. " + rf"Check: $p_1 = 101325$ Pa, $\rho_1 = 1.2$ kg/m$^3$, $v_{{1x}} = 100$ m/s, $L = 0.2$ m, $F_x = 30$ N/m, $F_y = -80$ N/m, $\gamma = 1.4$ give $v_{{2x}} = {f(_u_lo,7)}$ m/s, $v_{{2y}} = {f(_v2y,5)}$ m/s, $\rho_2 = {f(_rho2,6)}$ kg/m$^3$, $p_2 = {f(_p2,7)}$ Pa, residuals of (1) to (4) below $10^{{-9}}$; the other root gives $p_2 = {f(_p2_hi,5)}$ Pa $< 0$ and is discarded."),
        ]),
    ],
)

# ---------------------------------------------------------------- CL5
_A1, _A2, _v15, _p15, _rho15, _pa5, _F5, _W5, _Q5 = 0.5, 0.3, 150.0, 0.9e5, 1.1, 1.0e5, 3.0e4, 2.0e6, 3.0e7
_md = _rho15 * _v15 * _A1
_K = _pa5 * _A2 + _F5 + (_p15 - _pa5) * _A1 + _md * _v15
_H0 = GAM / (GAM - 1) * _p15 / _rho15 + _v15 ** 2 / 2 + (_Q5 - _W5) / _md
_qa, _qb, _qc = GAM + 1, -2 * GAM * _K / _md, 2 * (GAM - 1) * _H0
_qd = math.sqrt(_qb * _qb - 4 * _qa * _qc)
_v2s, _v2h = (-_qb - _qd) / (2 * _qa), (-_qb + _qd) / (2 * _qa)
_p2s, _p2h = (_K - _md * _v2s) / _A2, (_K - _md * _v2h) / _A2
_r2s, _r2h = _md / (_v2s * _A2), _md / (_v2h * _A2)
_M1 = _v15 / math.sqrt(GAM * _p15 / _rho15)
_M2s = _v2s / math.sqrt(GAM * _p2s / _r2s)
_M2h = _v2h / math.sqrt(GAM * _p2h / _r2h)
CL5 = dict(
    id="cl5", pill="CL5: Turbojet",
    title="Turbojet on a Testbench: Exit State",
    note_title="Problem - CL5 Turbojet on a Testbench",
    tags_md=["problema-examen", "leyes-de-conservacion", "momento-lineal", "energia", "turborreactor"],
    tags_html=["Moving boundaries", "Mass, momentum, energy", "Heat and work", "Thrust"],
    statement=[("p", r"The entrance and exit sections of the turboreactor sketched in the figure of CL5.pdf have areas $A_1$ and $A_2$. Besides the outer fixed frame, the machine has mobile parts in its interior that extract an amount of work $W$ per unit time from the fluid stream. The combined effects of chemical reaction in the combustion chamber and heat transfer through the walls give a heat transfer per unit time $Q$ to the fluid stream. The axial force on the turboreactor measured on the testbench is $\bar{F} = -F\,\bar{e}_x$. For given values of $W$, $Q$ and $F$ and assuming that at the entrance and exit sections the flow properties are uniform, obtain the values of the density $\rho_2$, pressure $p_2$ and velocity $v_2$ in terms of their values $p_1$, $\rho_1$ and $v_1$ at the entrance. (Handwritten addition: no gravity.)")],
    source_line=r"Source: CL5.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eq. 3.10, integral momentum balance Eq. 3.35, integral total energy balance Eq. 3.46, force on a body Eq. 3.32.",
    phases=[
        ("Phase 1", "Hypotheses, Data and Unknowns", [
            ("ul", [
                r"Compressible flow; neglect gravity; uniform properties at inlet and outlet; steady on average (the rotating parts make the flow periodic inside, but there is no net accumulation).",
                r"Perfect gas, $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$, as in the class solution. Fuel mass flow neglected (not given), so the same mass flow crosses both sections.",
                r"$\dot{W}$: work per unit time extracted from the fluid by the mobile parts; $\dot{Q}$: heat per unit time transferred to the fluid; $\bar{F} = -F\bar{e}_x$: force on the device measured on the testbench (fluid inside plus ambient air outside, at $p_a$).",
                r"Data: $[\rho_1,\ p_1,\ \bar{v}_1 = v_1\bar{e}_x,\ A_1,\ A_2,\ p_a,\ F,\ \dot{W},\ \dot{Q},\ \gamma]$. Unknowns: $[\rho_2,\ p_2,\ \bar{v}_2 = v_2\bar{e}_x]$.",
            ]),
            ("table", ["Symbol", "Meaning", "SI unit"], [
                [r"$A_1$, $A_2$", "entrance and exit areas", r"m$^2$"],
                [r"$p_1$, $\rho_1$, $v_1$", "entrance state", r"Pa, kg/m$^3$, m/s"],
                [r"$p_2$, $\rho_2$, $v_2$", "exit state", r"Pa, kg/m$^3$, m/s"],
                [r"$F$", "thrust measured on the bench", "N"],
                [r"$\dot{W}$, $\dot{Q}$", "power extracted and heat added", "W"],
                [r"$\dot{m} = \rho_1v_1A_1$", "mass flow", "kg/s"],
            ]),
        ]),
        ("Phase 2", "Frames, Control Volume and Surfaces", [
            ("ul", [
                r"Frame fixed to the testbench; $\bar{e}_x$ along the engine axis in the flow direction.",
                r"Surfaces: $\Sigma_1$ (entrance, $\bar{n} = -\bar{e}_x$), $\Sigma_2$ (exit, $\bar{n} = +\bar{e}_x$), $\Sigma_w$ (fixed walls, $\bar{v} = \bar{v}_c = 0$) and $\Sigma_m$ (surface of the mobile parts, moving with them: $\bar{v} = \bar{v}_c \ne 0$). On $\Sigma_w$ and $\Sigma_m$, $(\bar{v} - \bar{v}_c)\cdot\bar{n} = 0$.",
                r"$\bar{n}$ is the outward normal of the control volume; $\bar{n}_{\text{in}} = -\bar{n}$ points into the fluid.",
            ]),
            ("p", r"Definitions written on the surfaces, as in class:"),
            ("m", r"\boxed{\,\bar{F} = \int_{\Sigma_m,\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma - \int_{\Sigma_m,\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma = -F\,\bar{e}_x\,}"),
            ("m", r"\boxed{\,\dot{Q} = \int_{\Sigma_w,\Sigma_m}\bar{q}\cdot\bar{n}_{\text{in}}\,d\sigma + \int_{V_c}Q_R\,dV\,}"),
            ("m", r"\boxed{\,\dot{W} = -\int_{\Sigma_m}p\,\bar{n}_{\text{in}}\cdot\bar{v}\,d\sigma + \int_{\Sigma_m}(\bar{\bar{\tau}}'\cdot\bar{n}_{\text{in}})\cdot\bar{v}\,d\sigma\,}"),
            ("p", r"Only $\Sigma_m$ enters $\dot{W}$: $\Sigma_w$ is a fixed surface and does no work. $\dot{W}$ is the power of the gas on the moving solid, so the power done on the gas there is $-\dot{W}$."),
        ]),
        ("Phase 3", "Balances, Surface by Surface", [
            ("bal", dict(
                label="Mass (Notes Eq. 3.10)",
                eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho\,dV", r"0\ (\text{on average})") + r" + \int_{\Sigma_c}\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma = 0",
                cols=[r"\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma"],
                rows=[
                    (r"\Sigma_1", [r"$-\rho_1v_1A_1$"], False),
                    (r"\Sigma_2", [r"$+\rho_2v_2A_2$"], False),
                    (r"\Sigma_m", [r"$0$ ($\bar{v} = \bar{v}_c$)"], False),
                    (r"\Sigma_w", [r"$0$"], False),
                ],
                result=r"\boxed{\,\rho_1v_1A_1 = \rho_2v_2A_2 = \dot{m}\,} \tag{1}",
            )),
            ("bal", dict(
                label="Linear momentum (Notes Eq. 3.35)",
                eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV", r"0") + r" + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + " + crossed(r"\int_{V_c}\rho\bar{g}\,dV", r"\text{neglect}"),
                cols=[r"\int\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma", COL_P, COL_TAU],
                rows=[
                    (r"\Sigma_1", [r"$\rho_1v_1\bar{e}_x(-v_1)A_1 = -\dot{m}v_1\bar{e}_x$", r"$(p_1 - p_a)A_1\bar{e}_x$", r"$0$"], False),
                    (r"\Sigma_2", [r"$\rho_2v_2\bar{e}_x(v_2)A_2 = \dot{m}v_2\bar{e}_x$", r"$-(p_2 - p_a)A_2\bar{e}_x$", r"$0$"], False),
                    (r"\Sigma_m,\ \Sigma_w", [r"$0$", r"$-\int_{\Sigma_m,\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$", r"$\int_{\Sigma_m,\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$"], True),
                ],
                wall=r"Boxed $\Sigma_m$, $\Sigma_w$ terms: $-\bar{F} = F\bar{e}_x$ (uniform velocity vectors give no viscous stress on $\Sigma_1$, $\Sigma_2$).",
                result=r"\boxed{\,\dot{m}\,(v_2 - v_1) = (p_1 - p_a)A_1 - (p_2 - p_a)A_2 + F\,} \tag{2}",
            )),
            ("bal", dict(
                label="Total energy (Notes Eq. 3.46)",
                eq=crossed(r"\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV", r"0") + r" + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}(\bar{\bar{\tau}}'\cdot\bar{n})\cdot\bar{v}\,d\sigma + " + crossed(r"\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV", r"\text{neglect}") + r" - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \int_{V_c}Q_R\,dV",
                cols=[r"\int\rho\left(e + \tfrac{v^2}{2}\right)[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma", r"-\int p\,\bar{v}\cdot\bar{n}\,d\sigma", r"\int(\bar{\bar{\tau}}'\cdot\bar{n})\cdot\bar{v}\,d\sigma", r"-\int\bar{q}\cdot\bar{n}\,d\sigma"],
                rows=[
                    (r"\Sigma_1", [r"$-\dot{m}\left(e_1 + \tfrac{v_1^2}{2}\right)$", r"$+p_1v_1A_1$", r"$0$", r"$0$ ($\nabla T = 0$)"], False),
                    (r"\Sigma_2", [r"$+\dot{m}\left(e_2 + \tfrac{v_2^2}{2}\right)$", r"$-p_2v_2A_2$", r"$0$", r"$0$ ($\nabla T = 0$)"], False),
                    (r"\Sigma_m", [r"$0$", r"$-\int_{\Sigma_m}p\,\bar{v}\cdot\bar{n}\,d\sigma$", r"$\int_{\Sigma_m}(\bar{\bar{\tau}}'\cdot\bar{n})\cdot\bar{v}\,d\sigma$", r"$-\int_{\Sigma_m}\bar{q}\cdot\bar{n}\,d\sigma$"], True),
                    (r"\Sigma_w", [r"$0$", r"$0$ ($\bar{v} = 0$)", r"$0$ ($\bar{v} = 0$)", r"$-\int_{\Sigma_w}\bar{q}\cdot\bar{n}\,d\sigma$"], True),
                ],
                wall=r"Boxed terms: the pressure and viscous work on $\Sigma_m$ add up to $-\dot{W}$; the conduction through $\Sigma_m$, $\Sigma_w$ plus the volume term $\int_{V_c}Q_R\,dV$ add up to $\dot{Q}$. Moving the pressure work on $\Sigma_1$, $\Sigma_2$ to the left gives $h = e + p/\rho$; with (1) and $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$:",
                result=r"\boxed{\,\dot{m}\left[\left(\frac{\gamma}{\gamma - 1}\frac{p_2}{\rho_2} + \frac{v_2^2}{2}\right) - \left(\frac{\gamma}{\gamma - 1}\frac{p_1}{\rho_1} + \frac{v_1^2}{2}\right)\right] = -\dot{W} + \dot{Q}\,} \tag{3}",
            )),
            ("p", r"(1), (2) and (3) determine $\rho_2$, $p_2$ and $v_2$."),
        ]),
        ("Phase 4", "Interpretation, Limits and Dimensional Check", [
            ("ul", [
                r"(2) is the thrust balance: thrust = change of momentum flux + pressure imbalance on the sections. For $p_1 = p_2 = p_a$, $F = \dot{m}(v_2 - v_1)$.",
                r"(3): the stagnation enthalpy of the stream rises by the heat added and falls by the work extracted, per unit mass flow.",
                r"Dimensions (SI): $[\dot{m}(v_2 - v_1)] = \text{N}$; $[(\dot{Q} - \dot{W})/\dot{m}] = \text{J/kg} = \text{m}^2/\text{s}^2 = [h] = [v^2]$.",
                rf"Numerical illustration (hypothetical data): $A_1 = 0.5$ m$^2$, $A_2 = 0.3$ m$^2$, $v_1 = 150$ m/s, $p_1 = 0.9\times10^5$ Pa, $\rho_1 = 1.1$ kg/m$^3$ ($M_1 = {f(_M1,3)}$), $p_a = 10^5$ Pa, $F = 30$ kN, $\dot{{W}} = 2$ MW, $\dot{{Q}} = 30$ MW, $\gamma = 1.4$: $\dot{{m}} = {f(_md,4)}$ kg/s and the two roots of the extension below, $v_2 = {f(_v2s,6)}$ m/s, $p_2 = {f(_p2s,6)}$ Pa, $\rho_2 = {f(_r2s,5)}$ kg/m$^3$ ($M_2 = {f(_M2s,3)}$), and $v_2 = {f(_v2h,6)}$ m/s, $p_2 = {f(_p2h,6)}$ Pa, $\rho_2 = {f(_r2h,5)}$ kg/m$^3$ ($M_2 = {f(_M2h,3)}$); residuals of (1) to (3) below $10^{{-6}}$ in SI units.",
                r"Agreement with the official and class solutions: the same equations (1), (2), (3) (CL5.pdf writes (2) as $F = \rho_1v_1A_1(v_2 - v_1) - (p_1 - p_a)A_1 + (p_2 - p_a)A_2$).",
            ]),
            ("note", "Extension (beyond the official solution): explicit solution", r"With $K = p_aA_2 + F + (p_1 - p_a)A_1 + \dot{m}v_1$, (2) gives $p_2A_2 = K - \dot{m}v_2$ and, with (1), $p_2/\rho_2 = (K - \dot{m}v_2)v_2/\dot{m}$. Substituting into (3) and using $\frac{1}{2} - \frac{\gamma}{\gamma-1} = -\frac{\gamma+1}{2(\gamma-1)}$: $(\gamma + 1)v_2^2 - 2\gamma\frac{K}{\dot{m}}v_2 + 2(\gamma - 1)H_0 = 0$, with $H_0 = \frac{\gamma}{\gamma-1}\frac{p_1}{\rho_1} + \frac{v_1^2}{2} + \frac{\dot{Q} - \dot{W}}{\dot{m}}$. The two roots are a subsonic and a supersonic exit state; for a subsonic entrance with heat addition the physical one is the subsonic (smaller) root, since reaching the other would require passing through sonic conditions inside the engine, which this overall balance cannot describe. For $F = 0$, $\dot{Q} = \dot{W} = 0$ and $A_1 = A_2$ one root is $v_2 = v_1$ and the product of the roots is $2(\gamma - 1)H_0/(\gamma + 1)$, the Prandtl relation of a normal shock."),
        ]),
    ],
)

PROBLEMS = [CL1, CL2, CL3, CL4, CL5]
