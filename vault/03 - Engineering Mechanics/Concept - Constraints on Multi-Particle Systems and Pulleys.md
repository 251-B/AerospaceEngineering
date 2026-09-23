---
title: "Concept: Constraints on Multi-Particle Systems and Pulleys"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/03_-_Constraints (1).pdf (Slide 17)"
tier: "Atomic Concept Note"
language: "English"
---

# 🪢 Concept: Constraints on Multi-Particle Systems and Pulleys

## 1. Multi-Particle Kinematic Constraints

In multi-body engineering systems, constraints frequently couple the positions and velocities of several point particles $\{P_1, P_2, \dots, P_N\}$ (Slide 17):
* Masses connected by massless, taut, inextensible cables.
* Pulley blocks and hoisting mechanisms (Atwood machines).
* Articulated linkages and guide rods.

---

## 2. Geometric Formulation and Minimal Coordinates

Consider two masses $m_1$ and $m_2$ connected by a light inextensible cable of fixed length $L$ routed around stationary and moving pulleys:

1. **Holonomic Constraint Relation:**
   Expressing the geometric lengths of all cable segments in terms of coordinate positions $s_1(t)$ and $s_2(t)$:
   $$ L = c_1\,s_1(t) + c_2\,s_2(t) + \text{constant} $$
   where $c_1, c_2$ are integer coefficients determined by the pulley routing.
2. **Velocity and Acceleration Constraints:**
   Differentiating the cable length equation with respect to time:
   $$ \frac{dL}{dt} = 0 \implies c_1\,\dot{s}_1 + c_2\,\dot{s}_2 = 0 \implies \dot{s}_2 = -\frac{c_1}{c_2}\dot{s}_1 $$
   $$ c_1\,\ddot{s}_1 + c_2\,\ddot{s}_2 = 0 \implies \ddot{s}_2 = -\frac{c_1}{c_2}\ddot{s}_1 $$
3. **Degree of Freedom Reduction:**
   Although the system comprises two moving masses ($2 \times 1 = 2$ initial coordinates), the single constraint reduces the configuration space to:
   $$ \text{CDOF} = 2 - 1 = 1 $$
   A single generalized coordinate $q = s_1$ completely describes the kinematics of the entire system.

---

## 3. Internal Reaction Forces and Energy Transmission

In a multi-particle constraint:
1. **Coupled Tension Forces:**
   For a massless, frictionless cable, the tension magnitude $T$ is uniform throughout its entire length. The cable pulls on particle 1 with tension $\mathbf{T}_1$ and on particle 2 with tension $\mathbf{T}_2$.
2. **Individual vs. Total Work:**
   The constraint force performs non-zero work on each individual particle:
   $$ W_1 = \int \mathbf{T}_1 \cdot d\mathbf{r}_1 \neq 0, \quad W_2 = \int \mathbf{T}_2 \cdot d\mathbf{r}_2 \neq 0 $$
   However, calculating the net work done by the internal constraint forces:
   $$ W_{\text{internal}} = W_1 + W_2 = \int T(c_1\,ds_1 + c_2\,ds_2) = \int T\,d(c_1 s_1 + c_2 s_2) = \int T\,dL = 0 $$
   Because $dL \equiv 0$, **the net internal work performed by an ideal inextensible cable vanishes identically**.

### 3.1 Conservation of Total Mechanical Energy
Ideal cables and pulleys act as **conservative energy transmitters**:
* They do not generate or dissipate mechanical energy.
* They transfer kinetic and potential energy between interconnected bodies.
* The total mechanical energy of the whole multi-particle system is strictly conserved:
  $$ E_{\text{total}} = T_1 + T_2 + V_1 + V_2 = \text{constant} $$

---

## 🔗 Related Notes
* [[Topic 3 - Constraints and Reaction Forces|Topic 3 Master Guide]]
* [[Concept - Work and Power of Constraint Forces and Energy Preservation|Work & Power of Constraints]]
* [[Concept - Classification of Constraints Holonomic Rheonomic and Unilateral|Classification of Constraints]]
