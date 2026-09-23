---
title: "Concept: Coulomb Friction as Applied Force and Tangent Reaction"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/03_-_Constraints (1).pdf (Slides 18–20) & teoria/Notes.pdf (Section 6.6)"
tier: "Atomic Concept Note"
language: "English"
---

# 🛑 Concept: Coulomb Friction as Applied Force and Tangent Reaction

## 1. Classical Coulomb Friction Model

When surfaces or guides are not perfectly smooth, tangential contact forces arise between the body and the constraint manifold. In this course, friction is modeled via the **Coulomb Friction Law** using a single friction coefficient $\mu > 0$ (Slides 18–19 & Notes Sec. 6.6).

Depending on whether there is relative motion between particle $P$ and the constraint, friction behaves according to two completely different mathematical categories:

```
                            FRICTION FORCE F_R
                                     |
         +---------------------------+---------------------------+
         |                                                       |
  RELATIVE REST: v_P* = 0                                 RELATIVE SLIP: v_P* != 0
  - Constraint Reaction Force                             - Applied Force
  - Unknown magnitude in V_T                              - Known magnitude: |F_R| = mu * N
  - Zero power / work                                     - Direction opposes velocity
  - Bounded: |F_R| <= mu * N                              - Strictly dissipative: P < 0
```

---

## 2. The Two Physical Regimes

### 2.1 Dynamic Friction Regime (Relative Slip: $\mathbf{v}_P^* \neq \mathbf{0}$)
When the particle slides relative to the constraint at relative velocity $\mathbf{v}_P^* \neq \mathbf{0}$:
* **Classification:** Friction acts as an **applied external force** with known direction and magnitude.
* **Mathematical Form:**
  $$ \mathbf{F}_R = -\mu N\,\frac{\mathbf{v}_P^*}{\|\mathbf{v}_P^*\|} $$
  where $N = \|\mathbf{N}\|$ is the magnitude of the normal constraint force.
* **Power & Dissipation:** The instantaneous power is strictly negative:
  $$ P_R = \mathbf{F}_R \cdot \mathbf{v}_P^* = -\mu N\,\frac{\mathbf{v}_P^* \cdot \mathbf{v}_P^*}{\|\mathbf{v}_P^*\|} = -\mu N\,\|\mathbf{v}_P^*\| < 0 $$
  Dynamic friction **always dissipates mechanical energy** into heat.

### 2.2 Static Friction Regime (Relative Rest: $\mathbf{v}_P^* = \mathbf{0}$)
When the particle remains stationary relative to the constraint ($\mathbf{v}_P^* = \mathbf{0}$):
* **Classification:** Friction behaves as an **unknown constraint reaction force** in the tangent subspace $V_T$:
  $$ \mathbf{F}_R \in V_T $$
  * For a curve: $\mathbf{F}_R = R_1\,\mathbf{t}$ (1 new unknown scalar $R_1$).
  * For a surface: $\mathbf{F}_R = R_1\,\mathbf{t}_\alpha + R_2\,\mathbf{t}_\beta$ (2 new unknown scalars $R_1, R_2$).
* **Power & Work:** Because the relative velocity is zero, static friction exerts **identically zero power and zero work**:
  $$ P_R = \mathbf{F}_R \cdot \mathbf{0} \equiv 0 \implies W_R \equiv 0 $$

---

## 3. Switching Criteria Between Regimes (Slide 19)

Solving a friction problem requires continuously monitoring the transition conditions:

1. **Static $\to$ Dynamic (Breakaway / Slip):**
   The particle remains stuck as long as the tangential reaction force required for equilibrium satisfies:
   $$ \|\mathbf{F}_R\| \le \mu N $$
   If external forces demand a tangential force exceeding the Coulomb threshold:
   $$ \|\mathbf{F}_R\| > \mu N $$
   the static grip fails, slip initiates immediately, and the formulation switches to the dynamic case:
   $$ \mathbf{F}_R = -\mu N\,\frac{\mathbf{v}_P^*}{\|\mathbf{v}_P^*\|} $$

2. **Dynamic $\to$ Static (Arrest / Sticking):**
   The particle decelerates under dynamic friction until its relative speed reaches zero:
   $$ \mathbf{v}_P^* = \mathbf{0} $$
   At that exact instant, we re-evaluate whether the required equilibrium tangential force satisfies $\|\mathbf{F}_{\text{tangential}}\| \le \mu N$. If satisfied, the particle locks in place.

---

## 4. Benchmark Summary: Rough Cylinder (Slide 20)
For a particle of mass $m$ on a cylinder of radius $a$:
* Dynamic Slip ($\dot{\theta} \neq 0, \dot{z} \neq 0$):
  $$ \mathbf{F}_R = -\mu N \left( \frac{a\dot{\theta}}{v}\mathbf{e}_\theta + \frac{\dot{z}}{v}\mathbf{e}_z \right), \quad v = \sqrt{(a\dot{\theta})^2 + \dot{z}^2} $$
* Static Rest ($\dot{\theta} = 0, \dot{z} = 0$):
  $$ \mathbf{F}_R = R_\theta\,\mathbf{e}_\theta + R_z\,\mathbf{e}_z \quad \text{with} \quad \sqrt{R_\theta^2 + R_z^2} \le \mu N $$

---

## 🔗 Related Notes
* [[Topic 3 - Constraints and Reaction Forces|Topic 3 Master Guide]]
* [[Concept - Constraint and Reaction Forces Dynamical Decoupling|Dynamical Decoupling]]
* [[Concept - Work and Power of Constraint Forces and Energy Preservation|Work & Power of Constraints]]
