# [TRASPASO TEORÍA -> CLAUDE: BLOQUE 1]

## 1. Resumen de Fórmulas y Conceptos Dominados de Notes.pdf (Capítulos 1 y 2)

### Sub-parte 1.1: Hipótesis del Continuo, Propiedades y Aceleración Fluida
* **Continuum Hypothesis & Local Thermodynamic Equilibrium (LTE):**
  * Double-bounding criterion: $d \ll (\delta V)^{1/3} \ll L \implies \frac{d}{L} \ll 1$ (Notes.pdf, Eq. 1.2)[cite: 4].
  * Microscopic scale: $d = (W/\rho N_A)^{1/3}$, $d_{\text{water}} \approx 0.31\text{ nm} \sim d_0$, $d_{\text{air}} \approx 3.4\text{ nm} \sim 10 d_0$[cite: 4].
  * LTE and Knudsen criterion: $Kn = \frac{\lambda}{L} \ll 1$ and $T_{\text{macro}} \gg \tau$ (Eq. 1.7)[cite: 4].
  * In gases, $\lambda \sim 400\text{ nm} \gg d \sim 3.4\text{ nm}$; LTE is more restrictive than the continuum criterion[cite: 4]. When $Kn \sim 1$, the continuum breaks down, LTE is lost, and velocity slip appears at the wall[cite: 4].
* **Viscosity & Shear Stress:**
  * Cauchy stress decomposition: $\bar{\bar{\tau}} = -p\bar{\bar{I}} + \bar{\bar{\tau}}'$ (Eq. 3.16)[cite: 4, 10].
  * Newton’s law of viscosity (simple shear): $\tau = \mu \frac{\partial u}{\partial y}$[cite: 10]. Dynamic viscosity $\mu$ $[\text{Pa}\cdot\text{s}]$, kinematic viscosity $\nu = \frac{\mu}{\rho}$ $[\text{m}^2/\text{s}]$.
  * Temperature dependence: $\mu_{\text{gas}} \propto \sqrt{T}$ (molecular momentum transfer increases with $T$); $\mu_{\text{liquid}}$ decreases sharply with $T$ (intermolecular cohesion weakens)[cite: 4, 10].
  * Air vs Water: $\mu_{\text{water}} \approx 64\,\mu_{\text{air}}$, but $\nu_{\text{air}} \approx 13\,\nu_{\text{water}}$ due to the density ratio ($\rho_{\text{water}} \approx 800\,\rho_{\text{air}}$).
* **Material Derivative & Fluid Acceleration:**
  * Material derivative operator: $\frac{D\varphi}{Dt} = \frac{\partial \varphi}{\partial t} + \bar{v}\cdot\nabla\varphi$ (Eq. 2.24)[cite: 4, 10].
  * Fluid particle acceleration: $\bar{a} = \frac{D\bar{v}}{Dt} = \frac{\partial \bar{v}}{\partial t} + \bar{v}\cdot(\nabla\bar{v})$ (Eq. 2.25)[cite: 4, 10].
  * Intrinsic (Lamb) formulation (valid in all coordinate systems):
    $$\bar{a} = \frac{\partial \bar{v}}{\partial t} + \nabla\left(\frac{|\bar{v}|^2}{2}\right) - \bar{v}\wedge(\nabla\wedge\bar{v}) \qquad \text{[Eq. 2.26]}$$[cite: 4, 10]
  * Cartesian component form (prohibited in curvilinear coordinates): $a_i = \frac{\partial v_i}{\partial t} + v_j\frac{\partial v_i}{\partial x_j}$ (Eq. 2.27)[cite: 4].
  * Non-inertial frame of reference: $\bar{a}_{\text{abs}} = \bar{a}_{\text{rel}} + \bar{a}_0 + \dot{\bar{\Omega}}\wedge\bar{x} + \bar{\Omega}\wedge(\bar{\Omega}\wedge\bar{x}) + 2\bar{\Omega}\wedge\bar{v}$ (Eq. 2.28)[cite: 4].

---

### Sub-parte 1.2: Líneas del Flujo (Streamlines, Pathlines, Streaklines, Fluid Lines)
* **Streamlines (Líneas de corriente):**
  * Instantaneous curves tangent to $\bar{v}$ at a frozen time $t$:
    $$\frac{h_1 dx_1}{v_1(\bar{x}, t)} = \frac{h_2 dx_2}{v_2(\bar{x}, t)} = \frac{h_3 dx_3}{v_3(\bar{x}, t)} \qquad \text{[Eq. 2.21]}$$[cite: 4, 10]
  * Stagnation point: $\bar{v} = \bar{0}$ (Eq. 2.11)[cite: 4, 10, 12]. Streamlines can only intersect at stagnation points[cite: 4].
  * Stream tubes: boundaries are stream surfaces; no convective mass flux crosses lateral walls ($\bar{v}\cdot\bar{n} = 0$)[cite: 4, 10].
* **Trajectories & Pathlines:**
  * Lagrangian trajectory: $\frac{d\bar{x}}{dt} = \bar{v}(\bar{x}, t)$ with $\bar{x}(t_0) = \bar{x}_0$ (Eq. 2.12)[cite: 4, 12].
  * Pathline: geometric curve obtained by eliminating time $t$ from the trajectory components (Eq. 2.15)[cite: 4, 12].
* **Fluid Lines & Material Surfaces:**
  * Material curve tracking: $\bar{x} = \bar{x}_T(\bar{x}_l(\lambda), t)$ (Eq. 2.17)[cite: 4, 14].
  * Recipe: express initial shape $f(\bar{x}_0) = 0$ in terms of initial positions $\bar{x}_0$, invert trajectory relations to obtain $\bar{x}_0 = \bar{X}_0(\bar{x}, t)$, and substitute back[cite: 14].
* **Coincidence Theorems:**
  * In steady flows ($\partial\bar{v}/\partial t = \bar{0}$): Streamlines $\equiv$ Pathlines $\equiv$ Streaklines[cite: 4, 10].
  * In unsteady flows with fixed spatial direction ($\bar{v} = f(t)\bar{V}(\bar{x})$): Streamlines $\equiv$ Pathlines (e.g., Problems K8, K9, K10)[cite: 10, 12].

---

### Sub-parte 1.3: Cinemática Diferencial, Deformación, Vorticidad y Circulación
* **Helmholtz Decomposition of the Velocity Gradient Tensor:**
  * Relative motion: $d\bar{v} = d\bar{x}\cdot\nabla\bar{v}$ with $(\nabla\bar{v})_{ij} = \frac{\partial v_j}{\partial x_i}$ (Eq. 2.46)[cite: 4, 15].
  * Decomposition: $\nabla\bar{v} = \bar{\bar{T}}_d + \bar{\bar{T}}_r$ (Eq. 2.47)[cite: 4, 15].
  * Rate-of-strain tensor (symmetric, causes deformation and viscous stress):
    $$\bar{\bar{T}}_d = \frac{1}{2}(\nabla\bar{v} + \nabla\bar{v}^T) \qquad \text{[Eq. 2.48]}$$[cite: 4, 15]
    * Diagonal terms ($T_{d,ii}$): linear rate of extension (stretching) along axis $i$.
    * Off-diagonal terms ($T_{d,ij}, i\neq j$): half the shear strain rate ($\frac{1}{2}\dot{\gamma}_{ij}$).
  * Rate-of-rotation tensor (skew-symmetric, causes pure rigid-body rotation):
    $$\bar{\bar{T}}_r = \frac{1}{2}(\nabla\bar{v} - \nabla\bar{v}^T), \qquad d\bar{v}_r = d\bar{x}\cdot\bar{\bar{T}}_r = \frac{1}{2}\bar{\omega}\wedge d\bar{x} = \bar{\Omega}_{\text{fluid}}\wedge d\bar{x} \qquad \text{[Eq. 2.49, 2.52]}$$[cite: 4, 15]
    * Local fluid angular velocity: $\bar{\Omega}_{\text{fluid}} = \frac{1}{2}\bar{\omega}$[cite: 4, 10].
* **Volumetric Dilatation & Principal Directions:**
  * Volumetric expansion rate: $\frac{1}{V}\frac{dV}{dt} = \text{tr}(\nabla\bar{v}) = \text{tr}(\bar{\bar{T}}_d) = \nabla\cdot\bar{v}$ (Eq. 2.62)[cite: 4, 10].
  * Incompressible flow: $\nabla\cdot\bar{v} = 0 \implies \text{tr}(\bar{\bar{T}}_d) = 0$[cite: 4, 10].
  * Principal strain rates and axes: $|\bar{\bar{T}}_d - \lambda\bar{\bar{I}}| = 0$; zero shear strain in the principal frame[cite: 4, 10].
* **Vorticity, Circulation & Stokes' Theorem:**
  * Vorticity vector: $\bar{\omega} = \nabla\wedge\bar{v}$ (Eq. 2.6)[cite: 4, 10, 14]. Irrotational flow: $\bar{\omega} \equiv \bar{0}$[cite: 4, 10, 14].
  * Circulation: $\Gamma = \oint_C \bar{v}\cdot d\bar{l}$ (Eq. 2.29)[cite: 4, 10].
  * Stokes' Theorem: $\Gamma = \oint_C \bar{v}\cdot d\bar{l} = \int_\Sigma \bar{\omega}\cdot\bar{n}\,d\sigma$ (Eq. 2.32)[cite: 4, 10].
  * Topology caveat: Stokes holds if $\Sigma$ is completely contained within the fluid. In multiply connected domains (airfoils, free vortex with core singularity), $\bar{\omega} = \bar{0}$ everywhere in the fluid but $\Gamma \neq 0$[cite: 4, 10].
  * Aerodynamic Lift (Kutta-Joukowski): $L' = \rho_\infty V_\infty \Gamma$[cite: 4, 10].

---

### Sub-parte 1.4: Potencial de Velocidades, Función de Corriente y Flujos Convectivos
* **Velocity Potential ($\phi$):**
  * Condition of existence: Irrotational flow ($\bar{\omega} = \nabla\wedge\bar{v} \equiv \bar{0}$)[cite: 4, 10, 14].
  * Relation: $\bar{v} = \nabla\phi$ (Eq. 2.34)[cite: 4, 10, 14].
  * Governing equation: $\nabla^2\phi = 0$ (Laplace equation) when the flow is also incompressible ($\nabla\cdot\bar{v} = 0$)[cite: 4, 10].
* **Stream Function ($\psi$):**
  * Condition of existence: 2D Incompressible flow ($\nabla\cdot\bar{v} = 0$)[cite: 4, 10].
  * Cartesian: $v_x = \frac{\partial\psi}{\partial y}, \; v_y = -\frac{\partial\psi}{\partial x}$ (Eq. 2.41)[cite: 4, 10].
  * Polar: $v_r = \frac{1}{r}\frac{\partial\psi}{\partial\theta}, \; v_\theta = -\frac{\partial\psi}{\partial r}$ (Eq. 2.44–2.45)[cite: 4, 10].
  * Physical properties: isolines $\psi = \text{const}$ are streamlines; volumetric flow rate per unit span between two streamlines is $Q' = \psi_2 - \psi_1$ (Eq. 2.45)[cite: 4, 10].
  * Equipotential lines and streamlines form an orthogonal net: $\nabla\phi \cdot \nabla\psi = 0$[cite: 10].
* **Convective Fluxes:**
  * Rate of transport of property $\varphi$ (per unit mass) through control surface $\Sigma$:
    $$\Phi_\varphi = \int_\Sigma \rho\,\varphi\,(\bar{v}\cdot\bar{n})\,d\sigma$$[cite: 4, 10, 14]
  * Mass flux: $\dot{m} = \int_\Sigma \rho(\bar{v}\cdot\bar{n})\,d\sigma$[cite: 4, 10, 14].
  * Momentum flux vector: $\bar{\Phi}_{\text{mom}} = \int_\Sigma \rho\bar{v}(\bar{v}\cdot\bar{n})\,d\sigma$[cite: 4, 10, 14].
  * Kinetic energy flux: $\dot{E}_k = \int_\Sigma \frac{1}{2}\rho|\bar{v}|^2(\bar{v}\cdot\bar{n})\,d\sigma$[cite: 4, 10, 14].
  * Momentum correction coefficient: $\beta = \frac{1}{A\bar{u}^2}\int_A u^2\,dA \ge 1$. Non-uniform profiles (e.g., Poiseuille) carry more momentum than uniform profiles with equal mass flow rate due to quadratic velocity weighting ($\beta_{\text{uniform}} = 1$ vs. $\beta_{\text{Poiseuille}} = 1.2$)[cite: 1, 9].

---

## 2. Registro de Dudas y Puntos Críticos Durante la Sesión

1. **Aceleración en coordenadas polares/cilíndricas:**
   * *Trampa detectada:* Intentar derivar componente a componente con $a_i = Dv_i/Dt$ olvidando los términos de curvatura (aceleración centrípeta $-v_\theta^2/r$ en $\bar{e}_r$ y aceleración de Coriolis $+v_r v_\theta/r$ en $\bar{e}_\theta$)[cite: 10].
   * *Regla mnemotécnica para problemas:* Usar siempre la ecuación intrínseca de Lamb (Notes.pdf, Eq. 2.26) $\bar{a} = \frac{\partial\bar{v}}{\partial t} + \nabla\left(\frac{|\bar{v}|^2}{2}\right) - \bar{v}\wedge\bar{\omega}$. Si el flujo es irrotacional, el rotacional se anula directamente[cite: 4, 10].
2. **Corte y coincidencia de líneas de flujo:**
   * Dos *streamlines* del mismo instante jamás se cortan en un punto regular ($V \neq 0$), solo pueden cruzarse en un *stagnation point* ($\bar{v} = \bar{0}$)[cite: 4, 10].
   * *Streamlines* (instantáneas, $t$ congelado) y *pathlines* (históricas, integrando en $t$) solo coinciden si el flujo es estacionario ($\partial\bar{v}/\partial t = \bar{0}$) o si la dirección espacial está congelada ($\bar{v} = f(t)\bar{V}(\bar{x})$)[cite: 4, 10].
3. **Descomposición del tensor gradiente de velocidad ($\nabla\bar{v}$):**
   * El tensor de rotación $\bar{\bar{T}}_r$ es antisimétrico y representa rotación pura de sólido rígido a velocidad angular $\bar{\Omega}_{\text{fluid}} = \frac{1}{2}\bar{\omega}$ sin cambiar distancias ni ángulos relativos[cite: 4, 10, 15].
   * El tensor velocidad de deformación $\bar{\bar{T}}_d$ es simétrico y contiene toda la distorsión geométrica real del fluido (origen de las tensiones viscosas $\bar{\bar{\tau}}'$)[cite: 4, 10, 15].
4. **Condiciones de existencia independientes para $\phi$ y $\psi$:**
   * No confundir: la existencia de $\phi$ depende exclusivamente de la irrotacionalidad ($\bar{\omega} = \bar{0}$); la de $\psi$ depende exclusivamente de la incompresibilidad en 2D ($\nabla\cdot\bar{v} = 0$)[cite: 4, 10].
   * En flujo de Couette ($v_x = \dot{\gamma}y, v_y = 0$): $\nabla\cdot\bar{v} = 0 \implies$ existe $\psi(x,y)$, pero $\bar{\omega} = -\dot{\gamma}\bar{e}_z \neq \bar{0} \implies$ NO existe $\phi$[cite: 10].
5. **Teorema de Stokes en dominios múltiplemente conexos:**
   * En un vórtice libre puntual ($v_\theta \propto 1/r$), $\bar{\omega} = \bar{0}$ para todo $r > 0$, pero la circulación alrededor del origen es $\Gamma = \Gamma_0 \neq 0$ debido a la singularidad en $r=0$[cite: 4, 10].

---

## 3. Checklist de Verificación: Listo para Problemas K1 a K10

- [x] **K1 / K2:** Dominado el cálculo de $\bar{\bar{T}}_d$, $\bar{\bar{T}}_r$, $\nabla\cdot\bar{v}$, vorticidad constante $\omega_z = -U/H$ y circulación rectangular mediante integral de línea y Stokes[cite: 10].
- [x] **K3:** Dominada la deformación de líneas fluidas y circunferencias en flujos de cizalla lineal y evolución de superficies materiales[cite: 4].
- [x] **K4:** Dominado el semicuerpo de Rankine (superposición de corriente uniforme + fuente puntual), cálculo de puntos de remanso, isolínea $\psi = \text{cte}$ del cuerpo y flujo volumétrico a través de superficies abiertas/cerradas con Gauss[cite: 10, 12].
- [x] **K5:** Dominada la cinemática en coordenadas polares con dependencia temporal armónica: gradiente de velocidad, $\nabla\cdot\bar{v}$, vorticidad, aceleración por la fórmula de Lamb (Eq. 2.26) y circulación[cite: 10].
- [x] **K6:** Dominada la cinemática de esferas y líneas fluidas tridimensionales bajo flujos axisimétricos[cite: 4].
- [x] **K7:** Dominado el punto de estancamiento hiperbólico planar ($v_x = ax, v_y = by$): condición de incompresibilidad ($b = -a$), integración de $\phi$ y $\psi$, autovalores/autovectores de deformación y deformación de un elemento cuadrado[cite: 10].
- [x] **K8:** Dominado el campo 3D con factor temporal exponencial: coincidencia de streamlines y pathlines por dirección constante, integración de trayectorias y deformación de una esfera material fluida en un elipsoide[cite: 4, 12].
- [x] **K9:** Dominado el dipolo oscilante polar ($v_r \propto -\sin\theta/r^2, v_\theta \propto \cos\theta/r^2$): irrotacionalidad, incompresibilidad, integración de $\phi$ y $\psi$, aceleración en la línea $\theta = 0$ y evolución de la línea fluida inicial[cite: 10, 12].
- [x] **K10:** Dominado el flujo de corte con dependencia exponencial en $x$, tasa de estiramiento y rotación de lados de un elemento cuadrado mediante $d\bar{l}\cdot\nabla\bar{v}$[cite: 12, 15].

**Veredicto:** Base teórica, física y mapa de ecuaciones de `Notes.pdf` consolidada al 100%. Listo para resolución práctica de problemas en Claude.

---

## Nota de Claude al guardar (2026-10-31)

Comprobado contra los enunciados de K1-K10. K5, K7 y K9 están bien descritos. Descripciones que no cuadran con los enunciados reales:
- **K1** no es Couette: es la pared porosa oscilante (no estacionario; trayectoria, línea fluida, Q(t), circulación en un cuadrado con Stokes). Lo de $\omega_z = -U/H$ es solo K2.
- **K3** es una fuente 3D $v_r = Q(t)/(4\pi r^2)$: superficie fluida inicial $r = R$, línea fluida, tubo de corriente y cambio a un observador móvil. No es cizalla lineal.
- **K6** es el vórtice de Burgers 3D en cilíndricas: condición de incompresibilidad, líneas de corriente y trayectorias. No trata esferas.
- **K8** el factor temporal es $\cos\Omega t$ (potencial pulsante), no exponencial.
- **K10** la exponencial es en el tiempo, $e^{\Omega t}$, no en $x$; el campo es lineal en $x, y$.
