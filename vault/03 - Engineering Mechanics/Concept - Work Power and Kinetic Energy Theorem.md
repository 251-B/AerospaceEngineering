---
subject: Mechanics Applied to Aerospace Engineering
topic: 2 - Point Particle Dynamics
concept: Work, Power, and the Kinetic Energy Theorem
tags:
  - concept
  - work
  - power
  - kinetic-energy
  - work-energy-theorem
---

# Concept: Work, Power, and the Kinetic Energy Theorem

## 1. Context and Physical Significance
Forces alter both the speed and the direction of moving bodies. The Work-Energy Theorem states that only the tangential component of a force alters the particle's speed (and thus its kinetic energy).

---

## 2. Mathematical Definitions

### 2.1 Instantaneous Power
$$ P = \mathbf{F} \cdot \mathbf{v}_0^P \quad [\text{W} = \text{J/s}] $$
where $\mathbf{F}$ is the applied force and $\mathbf{v}_0^P$ is the particle's absolute velocity vector.

### 2.2 Kinetic Energy
$$ T_0 = \frac{1}{2}m_P\,\|\mathbf{v}_0^P\|^2 = \frac{1}{2}m_P\,v_0^2 \ge 0 \quad [\text{J}] $$

### 2.3 The Kinetic Energy Theorem
Taking the time derivative of kinetic energy:
$$ \frac{dT_0}{dt} = m_P\,\mathbf{v}_0^P \cdot \mathbf{a}_0^P = \mathbf{F} \cdot \mathbf{v}_0^P = P $$
The time rate of change of kinetic energy equals the instantaneous power exerted by all applied forces.

### 2.4 Work of a Force
Integrating over time from $t_1$ to $t_2$:
$$ W_{12} = \int_{t_1}^{t_2} P\,dt = \int_{t_1}^{t_2} (\mathbf{F}\cdot\mathbf{v}_0^P)\,dt = \int_{\mathbf{r}_1}^{\mathbf{r}_2} \mathbf{F} \cdot d\mathbf{r} = \Delta T_0 = T_{0,2} - T_{0,1} $$

---

## 3. Geometric Rationale: Tangential vs. Normal Forces
Because $\mathbf{v}_0^P = v_0\,\mathbf{e}_t$ in the intrinsic Frenet-Serret frame:
$$ P = \mathbf{F} \cdot (v_0\,\mathbf{e}_t) = F_t\,v_0 $$
* Forces with non-zero tangential component ($F_t \neq 0$) perform non-zero work and change particle speed.
* Forces orthogonal to velocity ($F_t = 0$, such as normal reactions on frictionless constraints, string tension, or magnetic Lorentz forces) do **zero work** ($W \equiv 0$).
