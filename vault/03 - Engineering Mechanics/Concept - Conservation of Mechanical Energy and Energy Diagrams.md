---
subject: Mechanics Applied to Aerospace Engineering
topic: 2 - Point Particle Dynamics
concept: Conservation of Mechanical Energy and Energy Diagrams
tags:
  - concept
  - mechanical-energy
  - conservation-laws
  - energy-landscapes
  - turning-points
---

# Concept: Conservation of Mechanical Energy and Energy Diagrams

## 1. Principle of Conservation of Mechanical Energy
Let total forces decompose into conservative forces $\mathbf{F}_C = -\nabla V_0$ and non-conservative forces $\mathbf{F}_N$.
Total Mechanical Energy:
$$ E_0 = T_0 + V_0 $$
Differentiating with respect to time:
$$ \frac{dE_0}{dt} = \frac{dT_0}{dt} + \frac{dV_0}{dt} = (\mathbf{F}_C + \mathbf{F}_N)\cdot\mathbf{v}_0^P - (\mathbf{F}_C\cdot\mathbf{v}_0^P) = \mathbf{F}_N \cdot \mathbf{v}_0^P $$
* If $\mathbf{F}_N = \mathbf{0}$, or if non-conservative forces are always normal to the velocity ($\mathbf{F}_N \perp \mathbf{v}_0^P$), then:
  $$ \frac{dE_0}{dt} = 0 \iff E_0 = T_0 + V_0 = \text{constant} $$
  This provides a **first integral of motion**.

---

## 2. Qualitative Motion Analysis in 1D Energy Diagrams
In a 1D system with potential curve $V_0(x)$:
$$ T_0(x) = \frac{1}{2}m v^2 = E_0 - V_0(x) \ge 0 $$

1. **Allowed Regions ($E_0 \ge V_0(x)$):** Domains where physical motion can occur.
2. **Forbidden Regions ($E_0 < V_0(x)$):** Domains where kinetic energy would be negative (physically inaccessible).
3. **Turning Points ($x_{\text{turn}}$):** Where $E_0 = V_0(x_{\text{turn}}) \implies T_0 = 0 \implies v = 0$. The particle stops and reverses its direction of motion.
4. **Speed at position $x$:**
   $$ v(x) = \sqrt{\frac{2(E_0 - V_0(x))}{m_P}} $$
