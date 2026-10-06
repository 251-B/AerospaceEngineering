---
title: "Formula Sheet - Topic 4: Angular Momentum and Central Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/04_-_Angular_momentum.pdf & teoria/Notes.pdf (Ch. 4.8 & 8)"
tier: "Formula Cheat Sheet"
language: "English"
---

# 📑 Formula Sheet: Topic 4 — Angular Momentum & Kepler's Problem

## 1. Vectorial Definitions & Units

| Quantity | Vector Formula | SI Units | Dimensions | Notes |
| :--- | :--- | :---: | :---: | :--- |
| **Linear Momentum** | $\mathbf{p}_0^P = m^P \mathbf{v}_0^P$ | $\text{kg}\cdot\text{m/s}$ | $[M][L][T]^{-1}$ | Reference frame dependent |
| **Angular Momentum** | $\mathbf{H}_{A0}^P = \mathbf{AP} \times m^P \mathbf{v}_0^P = (\mathbf{r}_0^P - \mathbf{r}_0^A) \times m^P \mathbf{v}_0^P$ | $\text{kg}\cdot\text{m}^2/\text{s}$ | $[M][L]^2[T]^{-1}$ | Depends on origin $A$ and frame $S_0$ |
| **Torque (Moment)** | $\mathbf{M}_A = \mathbf{AP} \times \mathbf{F} = (\mathbf{r}_0^P - \mathbf{r}_0^A) \times \mathbf{F}$ | $\text{N}\cdot\text{m}$ | $[M][L]^2[T]^{-2}$ | Independent of point along line of action |
| **Internal Torques** | $\sum \mathbf{M}_A^{\text{internal}} \equiv \mathbf{0}$ | $\text{N}\cdot\text{m}$ | $[M][L]^2[T]^{-2}$ | Collinear action-reaction forces |
| **Specific Angular Momentum** | $\mathbf{h} = \frac{\mathbf{H}_{O0}^P}{m^P} = \mathbf{r} \times \mathbf{v}$ | $\text{m}^2/\text{s}$ | $[L]^2[T]^{-1}$ | Mass-independent parameter |

---

## 2. Differential Evolution Equations for $\mathbf{H}_{A0}^P$

* **Arbitrary Moving Point $A$ (General Form):**
  $$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \mathbf{M}_A - \mathbf{v}_0^A \times m^P \mathbf{v}_0^P $$

* **Fixed Point in $S_0$ ($\mathbf{v}_0^A = \mathbf{0}$):**
  $$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \mathbf{M}_A $$

* **Point Moving Parallel to Particle ($\mathbf{v}_0^A \parallel \mathbf{v}_0^P$):**
  $$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \mathbf{M}_A $$

* **Origin Moving at Constant Velocity ($\mathbf{a}_0^A = \mathbf{0}$):**
  $$ \frac{d\mathbf{H}_{AA}}{dt}\Bigg|_A = \mathbf{M}_A $$

* **Conservation Condition:**
  $$ \mathbf{M}_A = \mathbf{0} \implies \mathbf{H}_{A0}^P = \text{constant vector} \quad \text{(3 scalar conservation laws)} $$

---

## 3. Central Force Dynamics & Polar Coordinates

* **Central Force Field:**
  $$ \mathbf{F} = F(r)\,\mathbf{e}_r = F(r)\,\frac{\mathbf{r}}{r} \implies \mathbf{M}_O = \mathbf{r} \times \mathbf{F} = \mathbf{0} $$
* **Invariant Angular Momentum:**
  $$ \mathbf{H}_{O0}^P = \text{const} \implies \mathbf{r}(t) \perp \mathbf{H}_O, \quad \mathbf{v}(t) \perp \mathbf{H}_O \quad \implies \text{\textbf{Planar Motion}} $$
* **Kinematics in Orbital Plane ($z = 0$):**
  $$ \mathbf{r} = r\,\mathbf{e}_r, \qquad \mathbf{v} = \dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta $$
  $$ \mathbf{a} = \left(\ddot{r} - r\dot{\theta}^2\right)\mathbf{e}_r + \left(r\ddot{\theta} + 2\dot{r}\dot{\theta}\right)\mathbf{e}_\theta $$
* **Conserved Specific Angular Momentum:**
  $$ h = r^2\dot{\theta} = \text{constant} \implies \dot{\theta} = \frac{h}{r^2} $$
* **Kepler's 2nd Law (Areal Velocity):**
  $$ \frac{dA}{dt} = \frac{1}{2}r^2\dot{\theta} = \frac{h}{2} = \text{constant} $$

---

## 4. Binet Equation & Orbital Trajectories

* **Binet Variable Substitution:**
  $$ u \equiv \frac{1}{r}, \qquad \dot{r} = -h\frac{du}{d\theta}, \qquad \ddot{r} = -h^2 u^2 \frac{d^2u}{d\theta^2} $$
* **General Binet Equation:**
  $$ \frac{d^2u}{d\theta^2} + u = -\frac{F(1/u)}{m h^2 u^2} $$
* **Gravitational Inverse-Square Field ($F = -\mu m / r^2 = -\mu m u^2$):**
  $$ \frac{d^2u}{d\theta^2} + u = \frac{\mu}{h^2} $$
* **Conic Orbit Solution:**
  $$ r(\theta) = \frac{p}{1 + e\cos\theta} = \frac{h^2/\mu}{1 + e\cos\theta} $$
  where $p = h^2/\mu$ is the semi-latus rectum and $e$ is the orbit eccentricity.

---

## 5. Conic Section Orbital Geometry

| Orbit Type | Eccentricity $e$ | Semi-Major Axis $a$ | Specific Energy $\xi$ | Turning Points |
| :--- | :---: | :---: | :---: | :--- |
| **Circle** | $e = 0$ | $a = p > 0$ | $\xi < 0$ | $r = a = \text{const}$ |
| **Ellipse** | $0 < e < 1$ | $a > 0$ | $\xi < 0$ | Periapsis $r_p$ and Apoapsis $r_a$ |
| **Parabola** | $e = 1$ | $a \to \infty$ | $\xi = 0$ | Periapsis $r_p = p/2$, escape to $\infty$ |
| **Hyperbola** | $e > 1$ | $a < 0$ | $\xi > 0$ | Periapsis $r_p$, asymptote angle $\theta_\infty$ |

### Fundamental Conic Relations (Ellipses):
* **Semi-Major Axis:** $2a = r_p + r_a \implies a = \frac{p}{1 - e^2}$
* **Periapsis Distance:** $r_p = a(1 - e) = \frac{p}{1 + e}$
* **Apoapsis Distance:** $r_a = a(1 + e) = \frac{p}{1 - e}$
* **Semi-Minor Axis:** $b = a\sqrt{1 - e^2} = \sqrt{a p}$
* **Semi-Latus Rectum:** $p = a(1 - e^2) = \frac{b^2}{a} = \frac{h^2}{\mu}$
* **Specific Angular Momentum:** $h = \sqrt{\mu p} = \sqrt{\mu a(1 - e^2)}$

---

## 6. Kepler's 3rd Law & Orbital Timing

* **Orbital Period:**
  $$ \tau = \frac{2\pi a b}{h} = \frac{2\pi a (a\sqrt{1 - e^2})}{\sqrt{\mu a (1 - e^2)}} = 2\pi\sqrt{\frac{a^3}{\mu}} $$
* **Kepler's Third Law:**
  $$ \tau^2 = \frac{4\pi^2}{\mu} a^3 $$
* **Mean Motion:**
  $$ n \equiv \frac{2\pi}{\tau} = \sqrt{\frac{\mu}{a^3}} $$

---

## 7. Energy Conservation & Characteristic Velocities

* **Mass-Specific Mechanical Energy (Vis-Viva Equation):**
  $$ \xi = \frac{1}{2}v^2 - \frac{\mu}{r} = -\frac{\mu}{2a} = \text{constant} $$
* **Vis-Viva Speed Formula:**
  $$ v^2 = \mu\left(\frac{2}{r} - \frac{1}{a}\right) $$
* **Circular Orbit Velocity ($r = a$):**
  $$ v_c = \sqrt{\frac{\mu}{r}} = \sqrt{\frac{\mu}{a}} $$
* **Parabolic Escape Velocity ($a \to \infty$):**
  $$ v_e = \sqrt{\frac{2\mu}{r}} = \sqrt{2}\,v_c $$
* **Periapsis Velocity ($r = r_p = a(1-e)$):**
  $$ v_p = \sqrt{\frac{\mu}{a}\left(\frac{1 + e}{1 - e}\right)} $$
* **Apoapsis Velocity ($r = r_a = a(1+e)$):**
  $$ v_a = \sqrt{\frac{\mu}{a}\left(\frac{1 - e}{1 + e}\right)} $$
* **Apsidal Velocity Ratio:**
  $$ \frac{v_p}{v_a} = \frac{1 + e}{1 - e} = \frac{r_a}{r_p} $$
