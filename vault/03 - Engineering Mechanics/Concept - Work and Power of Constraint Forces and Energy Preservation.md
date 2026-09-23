---
title: "Concept: Work and Power of Constraint Forces and Energy Preservation"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/03_-_Constraints (1).pdf (Slide 16) & teoria/Notes.pdf (Section 6.4)"
tier: "Atomic Concept Note"
language: "English"
---

# ⚡ Concept: Work and Power of Constraint Forces and Energy Preservation

## 1. Power of a Constraint Force

The instantaneous power developed by a constraint reaction force $\mathbf{N}$ on a moving particle $P$ is given by the scalar product:
$$ P_N = \mathbf{N} \cdot \mathbf{v}_0^P \quad [\text{W} = \text{J/s}] $$

---

## 2. Stationary (Scleronomic) Constraint Theorem

> [!IMPORTANT]
> **Cardinal Theorem of Smooth Scleronomic Constraints (Slide 16):**
> If a smooth constraint is **stationary** (independent of explicit time $t$), the constraint force performs **identically zero power and zero work**:
> $$ P_N \equiv 0 \quad \text{and} \quad W_N = \int_{t_1}^{t_2} P_N\,dt \equiv 0 $$

### 2.1 Geometric Proof
1. By definition of a smooth constraint, the reaction force resides in the normal subspace:
   $$ \mathbf{N} \in V_N $$
2. For a stationary constraint manifold, the trajectory $\mathbf{r}_0^P(t)$ is confined to the surface or curve for all time. Thus, the velocity vector is strictly tangent:
   $$ \mathbf{v}_0^P = \frac{d\mathbf{r}_0^P}{dt} \in V_T $$
3. Since $V_N$ and $V_T$ are mutually orthogonal subspaces ($V_N \perp V_T$):
   $$ P_N = \mathbf{N} \cdot \mathbf{v}_0^P = 0 \quad \forall t $$

### 2.2 Differential Form Proof (Notes Sec. 6.4)
For a surface $f(x, y, z) = 0$, the normal reaction is $\mathbf{N} = \lambda\,\nabla f$. The differential work is:
$$ \delta W_N = \mathbf{N} \cdot d\mathbf{r} = (\lambda\,\nabla f) \cdot d\mathbf{r} = \lambda\left( \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz \right) = \lambda\,df $$
Since the particle is constrained to $f(x, y, z) = 0$ for all time, its total differential along the motion vanishes:
$$ df \equiv 0 \implies \delta W_N \equiv 0 $$

---

## 3. Conservation of Mechanical Energy

Because stationary constraint reaction forces do zero work:
$$ \frac{dT_0}{dt} = \mathbf{F}_{\text{net}} \cdot \mathbf{v}_0^P = (\mathbf{F}_{\text{applied}} + \mathbf{N}) \cdot \mathbf{v}_0^P = \mathbf{F}_{\text{applied}} \cdot \mathbf{v}_0^P + 0 $$
If all active applied forces are conservative ($\mathbf{F}_{\text{applied}} = -\nabla V_0$):
$$ \frac{dT_0}{dt} = -\nabla V_0 \cdot \mathbf{v}_0^P = -\frac{dV_0}{dt} \implies \frac{d(T_0 + V_0)}{dt} = 0 $$
$$ E_0 = T_0 + V_0 = \text{constant} $$

**Conclusion:** The presence of smooth, stationary constraint forces does not alter the applicability of the **Law of Conservation of Mechanical Energy**.

---

## 4. When Do Constraint Forces Perform Work?

Constraint forces perform non-zero work under two specific conditions:
1. **Rheonomic (Moving) Constraints:** If the constraint evolves explicitly with time ($f(x, y, z, t) = 0$), then:
   $$ \frac{df}{dt} = \nabla f \cdot \mathbf{v}_0^P + \frac{\partial f}{\partial t} = 0 \implies \mathbf{v}_0^P \cdot \nabla f = -\frac{\partial f}{\partial t} \neq 0 $$
   The velocity has a normal component, so $\mathbf{N} \cdot \mathbf{v}_0^P = -\lambda \frac{\partial f}{\partial t} \neq 0$. Energy is transferred between the driving mechanism and the particle.
2. **Rough Contacts (Friction):** If friction is present, the tangential contact force dissipates mechanical energy into heat ($P_R = -\mu N v_P^* < 0$).

---

## 🔗 Related Notes
* [[Topic 3 - Constraints and Reaction Forces|Topic 3 Master Guide]]
* [[Concept - Classification of Constraints Holonomic Rheonomic and Unilateral|Classification of Constraints]]
* [[Concept - Constraint and Reaction Forces Dynamical Decoupling|Dynamical Decoupling]]
