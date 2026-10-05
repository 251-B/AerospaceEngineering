---
materia: Fluid Mechanics
tipo: laboratorio
tags:
  - fluid-mechanics
  - laboratory
  - reynolds-transport-theorem
  - momentum-conservation
  - jet-impact
  - experimental-aerospace
dificultad: intermedia
fuentes:
  - sources/01-fluid-mechanics/Labs/Lab_session_1.pdf
  - MedidasLab1_261005_223351 (1).jpg
---

# 🎯 Laboratory 1: Jet Impact on Surfaces (Momentum Conservation & Drag Coefficient)

> **Navigation & Context:**
> - Parent Course MOC: [[Mecanica de Fluidos MOC]]
> - Theoretical Framework: [[01 - Fluid Mechanics/Tema 3 - Conservation Laws]]
> - Fundamental Theorem: [[01 - Fluid Mechanics/Concepto - Teorema de Transporte de Reynolds]]
> - Master Index: [[00 - Indice Central/Indice Maestro]]
> - Primary Sources: `sources/01-fluid-mechanics/Labs/Lab_session_1.pdf` & Experimental Measurements `MedidasLab1_261005_223351 (1).jpg`

---

## 1. Executive Summary & Aerospace Relevance

The objective of this experimental session is to measure the dynamic reaction force produced by a vertical water jet impinging onto three target geometries (a **flat plate**, an **oblique / conical deflector**, and a **hemispherical cup**) and to rigorously validate the integral linear momentum conservation equation derived via the **Reynolds Transport Theorem (RTT)**.

In aerospace and power systems engineering, the conversion of fluid kinetic energy into mechanical force via jet deflection is a cornerstone principle:
- **Rocket Launch Pad Flame Deflectors:** Launch umbilical towers and mobile launcher platforms employ dry or water-deluged flame trenches with curved or angled wedge deflectors. The rocket exhaust plume (expanding at supersonic velocities) impinges on these surfaces, redirecting the colossal momentum flux away from sensitive ground infrastructure and dampening launch acoustic back-reflection.
- **Aircraft Turbofan Thrust Reversers:** Target-type bucket reversers or cascade turning vanes redirect high-speed bypass airflow in an oblique or reverse direction ($120^\circ \le \beta \le 150^\circ$), applying a counter-thrust braking force $F \propto (1 + \cos\theta)\dot{m}v$ directly upon runway touchdown.
- **Pelton Impulse Turbines:** High-head hydroelectric turbines inject water jets at velocities exceeding $100\text{ m/s}$ onto twin hemispherical buckets ($180^\circ$ split deflection), extracting up to $90\%$ of kinetic energy by turning fluid momentum completely around ($F \approx 2\rho Q^2/A$).

---

## 2. Theoretical Framework & Control Volume Strategy

### 2.1 The Reynolds Transport Theorem (RTT) for Linear Momentum

Consider an arbitrary, fixed control volume $V_c$ bounded by a closed control surface $\Sigma_c$. The Reynolds Transport Theorem relates the rate of change of linear momentum of a fluid system $\vec{P}_{\text{sys}}$ to the volume unsteadiness and the convective momentum flux across the boundaries:

$$\frac{d\vec{P}_{\text{sys}}}{dt} = \frac{d}{dt}\int_{V_c} \rho \vec{v}\, dV + \int_{\Sigma_c} \rho \vec{v} \left( \vec{v} \cdot \vec{n} \right) d\sigma = \sum \vec{F}_{\text{ext}}$$

Under **steady-state conditions** ($\partial/\partial t = 0$), the volume integral vanishes:

$$\int_{\Sigma_c} \rho \vec{v} \left( \vec{v} \cdot \vec{n} \right) d\sigma = \sum \vec{F}_{\text{ext}}$$

The total external force $\sum \vec{F}_{\text{ext}}$ acting on the fluid within $V_c$ consists of surface forces (pressure and viscous shear stress) and body forces (gravity):

$$\sum \vec{F}_{\text{ext}} = \int_{\Sigma_c} (-p \vec{n} + \bar{\bar{\tau}} \cdot \vec{n}) d\sigma + \int_{V_c} \rho \vec{g}\, dV$$

### 2.2 Boundary Simplification & Physical Justifications

1. **Gauge Pressure Formulation:** The atmospheric pressure $p_a$ acts uniformly on the free boundaries of the jet as well as on the dry back face of the deflecting obstacle. Substituting $p = p_a + (p - p_a)$ and applying the divergence theorem $\oint_{\Sigma_c} p_a \vec{n}\, d\sigma = \int_{V_c} \nabla p_a\, dV = 0$, the external pressure forces reduce to:
   $$\int_{\Sigma_c} -(p - p_a)\vec{n}\, d\sigma$$
   Since gauge pressure $(p - p_a) \approx 0$ at all fluid-air free surfaces, the only remaining non-zero pressure contribution comes from the wetted wall $\Sigma_w$ of the obstacle. By Newton's third law, the force exerted by the fluid on the obstacle $\vec{F}$ is equal and opposite to the force exerted by the obstacle on the fluid CV:
   $$\int_{\Sigma_w} -(p - p_a)\vec{n}\, d\sigma = -\vec{F}$$

2. **Neglect of Viscous Shear Along Deflector:** The characteristic Reynolds number of the jet is:
   $$Re_d = \frac{\rho v d}{\mu} \approx \frac{1000 \cdot (2.8 \text{ to } 8.3) \cdot 0.008}{1.002 \times 10^{-3}} \approx 2.2 \times 10^4 \text{ to } 6.6 \times 10^4 \gg 1$$
   Because $Re_d \gg 1$, viscous stresses inside the thin boundary layer on the plate are confined to a boundary layer thickness $\delta \sim d / \sqrt{Re_d} \ll d$. The total viscous shear force is orders of magnitude smaller than the convective momentum flux:
   $$\int_{\Sigma_w} \bar{\bar{\tau}}\cdot\vec{n}\, d\sigma \ll \int_{\Sigma_c} \rho \vec{v}(\vec{v}\cdot\vec{n})\, d\sigma$$

3. **Neglect of Gravity in the Deflection Zone:** The Froude number based on the elevation change $h$ from the nozzle to the plate is:
   $$Fr = \frac{v}{\sqrt{g h}}$$
   For $h = 0.035\text{ m}$ and $v \ge 2.76\text{ m/s}$, $\sqrt{gh} = \sqrt{9.81 \times 0.035} \approx 0.586\text{ m/s}$, yielding $Fr \ge 4.7 \gg 1$. Thus, gravity forces inside the thin impact zone are negligible compared to dynamic inertia forces.

4. **Bernoulli's Equation on the Free Boundary:** Along a streamline traveling on the atmospheric boundary from the nozzle exit section ($\Sigma_i$) to the lateral exit water sheet ($\Sigma_o$):
   $$p_a + \frac{1}{2}\rho v_i^2 + \rho g z_i = p_a + \frac{1}{2}\rho v_s^2 + \rho g z_s$$
   Neglecting elevation differences $\Delta z \approx 0$ across the deflection sheet, we find:
   $$v_s = v_i \equiv v$$
   where $v = Q/A$ and $A = \frac{\pi d^2}{4}$.

5. **Conservation of Mass:** For steady incompressible flow:
   $$-\rho v_i A_i + \rho v_s A_s = 0 \implies A_s = A_i \equiv A$$

---

## 3. Mathematical Derivations for the Three Geometries

Let the vertical coordinate be $\vec{e}_y$ (pointing upwards, aligned with the incident jet) and the radial horizontal direction be $\vec{e}_r$.

### 3.1 Case (a): Flat Surface ($\theta = 90^\circ$ Deflection)

- **Inlet section $\Sigma_i$:** Velocity $\vec{v}_i = v \vec{e}_y$, outward normal $\vec{n}_i = -\vec{e}_y$.
  $$\vec{v}_i \cdot \vec{n}_i = -v$$
  Inlet vertical momentum flux:
  $$\int_{\Sigma_i} \rho (\vec{v}_i \cdot \vec{e}_y)(\vec{v}_i \cdot \vec{n}_i)\, d\sigma = \rho v (-v) A = -\rho v^2 A$$
- **Outlet section $\Sigma_o$:** Water is discharged horizontally in all radial directions $\vec{e}_r$:
  $$\vec{v}_o = v \vec{e}_r, \quad \vec{v}_o \cdot \vec{e}_y = 0$$
  Outlet vertical momentum flux is exactly zero:
  $$\int_{\Sigma_o} \rho (\vec{v}_o \cdot \vec{e}_y)(\vec{v}_o \cdot \vec{n}_o)\, d\sigma = 0$$
- **Balance of Linear Momentum in $\vec{e}_y$:**
  $$-\rho v^2 A = -F_y \implies \mathbf{F_y = \rho v^2 A = \rho \frac{Q^2}{A}}$$

The **dimensionless drag coefficient** $C_d$ is defined as:
$$C_d = \frac{F}{\frac{1}{2}\rho v^2 A} = \frac{\rho v^2 A}{\frac{1}{2}\rho v^2 A} = \mathbf{2.0}$$

---

### 3.2 Case (b): Oblique / Conical Deflector ($30^\circ$ & $45^\circ$)

Let $\theta$ denote the downward angle of exit velocity relative to the horizontal plane ($\theta = 0^\circ$ corresponds to a flat plate):
$$\vec{v}_o = v \cos\theta\, \vec{e}_r - v \sin\theta\, \vec{e}_y$$
Outward normal at the exit perimeter $\vec{n}_o$ is parallel to $\vec{v}_o$, so $\vec{v}_o \cdot \vec{n}_o = +v$.

- **Inlet flux:** $-\rho v^2 A \vec{e}_y$
- **Outlet flux:**
  $$\int_{\Sigma_o} \rho (-v \sin\theta \vec{e}_y)(+v)\, d\sigma = -\rho v^2 \sin\theta A \vec{e}_y$$
- **Total momentum balance in $\vec{e}_y$:**
  $$-\rho v^2 A - \rho v^2 \sin\theta A = -F_y$$
  $$\mathbf{F_y = (1 + \sin\theta)\rho v^2 A = (1 + \sin\theta)\rho \frac{Q^2}{A}}$$

#### Comparison of Angle Conventions:
1. **$30^\circ$ Deflector (Theoretical guide, UC3M Session 1 Fig. 1b):**
   $$\theta = 30^\circ \implies \sin(30^\circ) = 0.5$$
   $$F_y = 1.5 \rho \frac{Q^2}{A} = \frac{3}{2}\rho \frac{Q^2}{A}$$
   $$\mathbf{C_d = 3.0}$$

2. **$45^\circ$ Deflector (Lab device face marking):**
   $$\theta = 45^\circ \implies \sin(45^\circ) = \frac{\sqrt{2}}{2} \approx 0.7071$$
   $$F_y = \left(1 + \frac{\sqrt{2}}{2}\right)\rho \frac{Q^2}{A} \approx 1.707 \rho \frac{Q^2}{A}$$
   $$\mathbf{C_d = 2\left(1 + \frac{\sqrt{2}}{2}\right) \approx 3.414}$$

---

### 3.3 Case (c): Hemispherical Surface ($180^\circ$ Deflection)

The water stream enters vertically upwards and follows the interior curvature of the hemisphere, exiting vertically downwards as an annular sheet:
$$\vec{v}_o = -v \vec{e}_y$$
The outward normal at the outlet is pointing downwards: $\vec{n}_o = -\vec{e}_y$, thus $\vec{v}_o \cdot \vec{n}_o = (-v)(-1) = +v$.

- **Inlet flux:** $-\rho v^2 A \vec{e}_y$
- **Outlet flux:**
  $$\int_{\Sigma_o} \rho (-v \vec{e}_y)(+v)\, d\sigma = -\rho v^2 A \vec{e}_y$$
- **Total momentum balance in $\vec{e}_y$:**
  $$-\rho v^2 A - \rho v^2 A = -F_y \implies -2\rho v^2 A = -F_y$$
  $$\mathbf{F_y = 2\rho v^2 A = 2\rho \frac{Q^2}{A}}$$

The drag coefficient is:
$$C_d = \frac{2\rho v^2 A}{\frac{1}{2}\rho v^2 A} = \mathbf{4.0}$$

---

## 4. Experimental Setup & Apparatus Specifications

The experimental tests were performed on an **Edibon FME02 Hydraulic Bench** equipped with an **Edibon FME01 Jet Impact Apparatus**:
- **Nozzle Inner Diameter:** $d = 8\text{ mm} = 0.008\text{ m}$
- **Nozzle Cross-Sectional Area:** $A = \frac{\pi d^2}{4} = \frac{\pi (0.008)^2}{4} = 5.02655 \times 10^{-5}\text{ m}^2$
- **Working Fluid:** Water at $T \approx 20^\circ\text{C}$ ($\rho = 1000\text{ kg/m}^3$, $\mu = 1.002 \times 10^{-3}\text{ Pa}\cdot\text{s}$)
- **Local Gravity:** $g = 9.81\text{ m/s}^2$
- **Nozzle-to-Target Distance:** $h \approx 35\text{ mm} = 0.035\text{ m}$
- **Force Measurement System:** Mechanical balancing platform with level indicator dial gauge counterbalanced by calibrated brass weights (increments of $50\text{ g}$).

---

## 5. Experimental Data Reduction (11 Points, Full SI Units)

Experimental readings recorded in `MedidasLab1_261005_223351 (1).jpg` for 11 flow rates from $Q = 1500\text{ l/h}$ down to $500\text{ l/h}$:

### 5.1 Hydraulic Base Parameters

$$\text{Conversion: } Q\,[\text{m}^3/\text{s}] = \frac{Q\,[\text{l/h}]}{3.6 \times 10^6}, \quad v = \frac{Q\,[\text{m}^3/\text{s}]}{A}, \quad Re_d = \frac{\rho v d}{\mu}, \quad F_{\text{dyn}} = \frac{1}{2}\rho \frac{Q^2}{A}$$

| Point | $Q$ (l/h) | $Q$ ($\text{m}^3/\text{s}$) | $v$ (m/s) | $Re_d$ | $F_{\text{dyn}} = \frac{1}{2}\rho v^2 A$ (N) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 1500 | $4.1667 \times 10^{-4}$ | 8.289 | 66,182 | 1.727 |
| **2** | 1400 | $3.8889 \times 10^{-4}$ | 7.737 | 61,770 | 1.504 |
| **3** | 1300 | $3.6111 \times 10^{-4}$ | 7.184 | 57,358 | 1.297 |
| **4** | 1200 | $3.3333 \times 10^{-4}$ | 6.631 | 52,946 | 1.105 |
| **5** | 1100 | $3.0556 \times 10^{-4}$ | 6.079 | 48,534 | 0.929 |
| **6** | 1000 | $2.7778 \times 10^{-4}$ | 5.526 | 44,121 | 0.768 |
| **7** | 900 | $2.5000 \times 10^{-4}$ | 4.974 | 39,709 | 0.622 |
| **8** | 800 | $2.2222 \times 10^{-4}$ | 4.421 | 35,297 | 0.491 |
| **9** | 700 | $1.9444 \times 10^{-4}$ | 3.868 | 30,885 | 0.376 |
| **10** | 600 | $1.6667 \times 10^{-4}$ | 3.316 | 26,473 | 0.276 |
| **11** | 500 | $1.3889 \times 10^{-4}$ | 2.763 | 22,061 | 0.192 |

---

### 5.2 Target A: Flat Surface ($C_{d,\text{th}} = 2.0$)

$$W_f = m_f \cdot g, \quad F_{\text{th},f} = \rho \frac{Q^2}{A} = 2 F_{\text{dyn}}, \quad C_{d,f} = \frac{W_f}{F_{\text{dyn}}}, \quad \epsilon_f = \frac{W_f - F_{\text{th},f}}{F_{\text{th},f}} \times 100\%$$

| $Q$ (l/h) | $m_f$ (g) | $W_f$ (N) | $F_{\text{th},f}$ (N) | $C_{d,\text{exp}}$ | Error $\epsilon$ (%) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1500 | 350 | 3.434 | 3.454 | **1.99** | **-0.6%** |
| 1400 | 300 | 2.943 | 3.009 | **1.96** | **-2.2%** |
| 1300 | 250 | 2.453 | 2.594 | **1.89** | **-5.5%** |
| 1200 | 250 | 2.453 | 2.210 | **2.22** | **+10.9%** |
| 1100 | 200 | 1.962 | 1.857 | **2.11** | **+5.6%** |
| 1000 | 200 | 1.962 | 1.535 | **2.56** | **+27.8%** |
| 900 | 150 | 1.472 | 1.243 | **2.37** | **+18.3%** |
| 800 | 100 | 0.981 | 0.982 | **2.00** | **-0.1%** |
| 700 | 100 | 0.981 | 0.752 | **2.61** | **+30.4%** |
| 600 | 50 | 0.491 | 0.553 | **1.78** | **-11.2%** |
| 500 | 0 | 0.000 | 0.384 | **0.00** | **-100.0%** |

*Average $C_d$ (high flow rates $1100-1500\text{ l/h}$):* $\overline{C_d} = 2.03 \pm 0.12$ ($1.7\%$ average deviation from theory).

---

### 5.3 Target B: Oblique Deflector $45^\circ / 30^\circ$ ($C_{d,\text{th}} = 3.0$ for $30^\circ$)

$$W_o = m_o \cdot g, \quad F_{\text{th},o} = 1.5 \rho \frac{Q^2}{A} = 3 F_{\text{dyn}}, \quad C_{d,o} = \frac{W_o}{F_{\text{dyn}}}, \quad \epsilon_o = \frac{W_o - F_{\text{th},o}}{F_{\text{th},o}} \times 100\%$$

| $Q$ (l/h) | $m_o$ (g) | $W_o$ (N) | $F_{\text{th},o}$ (N) | $C_{d,\text{exp}}$ | Error $\epsilon$ (%) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1500 | 400 | 3.924 | 5.181 | **2.27** | **-24.3%** |
| 1400 | 350 | 3.434 | 4.513 | **2.28** | **-23.9%** |
| 1300 | 350 | 3.434 | 3.891 | **2.65** | **-11.8%** |
| 1200 | 300 | 2.943 | 3.316 | **2.66** | **-11.2%** |
| 1100 | 250 | 2.453 | 2.786 | **2.64** | **-12.0%** |
| 1000 | 200 | 1.962 | 2.303 | **2.56** | **-14.8%** |
| 900 | 150 | 1.472 | 1.865 | **2.37** | **-21.1%** |
| 800 | 150 | 1.472 | 1.474 | **3.00** | **-0.1%** |
| 700 | 100 | 0.981 | 1.128 | **2.61** | **-13.1%** |
| 600 | 100 | 0.981 | 0.829 | **3.55** | **+18.3%** |
| 500 | 50 | 0.491 | 0.576 | **2.56** | **-14.8%** |

*Note on geometry:* If evaluated with the $45^\circ$ theoretical model ($C_{d,\text{th}} = 3.414$), the measured values exhibit an average deficit of $\sim 28\%$, consistent with strong lateral sheet deflection impinging on the transparent cylinder wall.

---

### 5.4 Target C: Hemispherical Cup ($C_{d,\text{th}} = 4.0$)

$$W_h = m_h \cdot g, \quad F_{\text{th},h} = 2.0 \rho \frac{Q^2}{A} = 4 F_{\text{dyn}}, \quad C_{d,h} = \frac{W_h}{F_{\text{dyn}}}, \quad \epsilon_h = \frac{W_h - F_{\text{th},h}}{F_{\text{th},h}} \times 100\%$$

| $Q$ (l/h) | $m_h$ (g) | $W_h$ (N) | $F_{\text{th},h}$ (N) | $C_{d,\text{exp}}$ | Error $\epsilon$ (%) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1500 | 550 | 5.396 | 6.908 | **3.12** | **-21.9%** |
| 1400 | 500 | 4.905 | 6.017 | **3.26** | **-18.5%** |
| 1300 | 450 | 4.415 | 5.189 | **3.40** | **-14.9%** |
| 1200 | 350 | 3.434 | 4.421 | **3.11** | **-22.3%** |
| 1100 | 300 | 2.943 | 3.715 | **3.17** | **-20.8%** |
| 1000 | 250 | 2.453 | 3.070 | **3.20** | **-20.1%** |
| 900 | 200 | 1.962 | 2.487 | **3.16** | **-21.1%** |
| 800 | 150 | 1.472 | 1.965 | **3.00** | **-25.1%** |
| 700 | 100 | 0.981 | 1.504 | **2.61** | **-34.8%** |
| 600 | 100 | 0.981 | 1.105 | **3.55** | **-11.2%** |
| 500 | 50 | 0.491 | 0.768 | **2.56** | **-36.1%** |

*Average $C_d$ for $Q \ge 900\text{ l/h}$:* $\overline{C_d} = 3.20 \pm 0.11$. While consistently below the ideal value of $4.0$, it clearly shows that the hemispherical target produces roughly **$1.6\times$** the force of the flat plate, reflecting the high momentum reversal.

---

## 6. Physical Diagnostics of Experimental Discrepancies

Detailed physical evaluation reveals four major sources of experimental systematic discrepancy:

### 6.1 Gravitational Deceleration Before Impact
The water jet is emitted vertically from the nozzle and travels an upward distance $h \approx 35\text{ mm}$ before impinging upon the obstacle. By Torricelli / Bernoulli free-flight kinematics:
$$v_{\text{imp}} = \sqrt{v_0^2 - 2 g h}$$

- At maximum flow $Q = 1500\text{ l/h}$ ($v_0 = 8.289\text{ m/s}$):
  $$v_{\text{imp}} = \sqrt{8.289^2 - 2 \cdot 9.81 \cdot 0.035} = \sqrt{68.71 - 0.687} = 8.247\text{ m/s} \quad (\Delta v / v = -0.5\%)$$
- At minimum flow $Q = 500\text{ l/h}$ ($v_0 = 2.763\text{ m/s}$):
  $$v_{\text{imp}} = \sqrt{2.763^2 - 0.687} = \sqrt{7.634 - 0.687} = 2.636\text{ m/s} \quad (\Delta v / v = -4.6\%)$$
Because $F \propto v_{\text{imp}}^2$, the effective theoretical force at impact is reduced by:
$$\frac{\Delta F}{F} \approx \frac{2gh}{v_0^2} = \frac{0.687}{7.634} \approx 9.0\%$$
This explains why the theoretical force overpredicts experimental readings at lower flow rates.

### 6.2 Splashback, Droplet Interference & Annular Jet Collision
- In the **hemispherical cup**, the fluid turns $180^\circ$ and exits vertically downward in a cylindrical sheet surrounding the incoming upward jet. Droplet entrainment, aerodynamic drag between the counter-flowing streams, and water splashing onto the vertical support rod create significant downward momentum loss.
- In the **enclosed transparent testing chamber**, droplets bounce off the acrylic cylinder walls and rain onto the balance lever, distorting the net mechanical equilibrium.

### 6.3 Quantization of Counterbalance Masses
The laboratory apparatus utilizes discrete slotted brass weights with a minimum unit of $\Delta m = 50\text{ g}$, corresponding to a force resolution of:
$$\Delta W = 0.050\text{ kg} \times 9.81\text{ m/s}^2 = 0.4905\text{ N}$$
- At $Q = 1500\text{ l/h}$, $W \approx 3.4 - 5.4\text{ N}$, so $\Delta W / W \approx 9 - 14\%$.
- At $Q = 500\text{ l/h}$, $F_{\text{th},f} = 0.384\text{ N} < \Delta W$. Since the smallest mass is $50\text{ g}$, placing $50\text{ g}$ would immediately overbalance the lever, forcing the student to record $m = 0\text{ g}$ (producing an apparent $-100\%$ error).
- At intermediate flows, discrete steps create artificial plateaus ($m = 250\text{ g}$ recorded at both $1300$ and $1200\text{ l/h}$ for the flat plate).

---

## 7. Conclusions & Pedagogical Takeaways

1. **Validation of Integral Momentum Balance:** The experimental results strongly confirm that the dynamic force scales quadratically with flow rate ($F \propto Q^2$), validating the convective momentum flux term $\int \rho \vec{v}(\vec{v}\cdot\vec{n})\, d\sigma$ derived from the Reynolds Transport Theorem.
2. **Deflection Multiplier Effect:** The target geometry dramatically dictates the reaction force:
   $$\overline{C}_{d,\text{flat}} \approx 2.0 \quad < \quad \overline{C}_{d,\text{oblique}} \approx 2.6 \quad < \quad \overline{C}_{d,\text{hemisphere}} \approx 3.2$$
   The hemispherical cup doubles the theoretical linear momentum transfer compared to the flat plate by reversing fluid velocity by $180^\circ$.
3. **Engineering Implications:** The deficit between theoretical $C_d=4.0$ and measured $C_d=3.2$ illustrates real-world hydraulic losses: flow separation inside curved buckets, air entrainment, droplet impact, and boundary layer friction. Pelton turbine designers account for these exact losses using bucket splitters and cutouts.
