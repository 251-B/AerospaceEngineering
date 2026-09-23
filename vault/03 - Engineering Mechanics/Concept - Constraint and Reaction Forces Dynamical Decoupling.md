---
title: "Concept: Constraint and Reaction Forces Dynamical Decoupling"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/03_-_Constraints (1).pdf (Slides 13–15) & teoria/Notes.pdf (Sections 6.4–6.5)"
tier: "Atomic Concept Note"
language: "English"
---

# ⚖️ Concept: Constraint and Reaction Forces Dynamical Decoupling

## 1. Nature of Constraint (Reaction) Forces

In Newtonian mechanics, the physical mechanism compelling a particle to remain on a constraint manifold is a **constraint (or reaction) force $\mathbf{N}$** (Slide 13):
1. For smooth constraints, the reaction force **acts strictly within the normal subspace $V_N$**:
   $$ \mathbf{N} \in V_N $$
2. The scalar components of $\mathbf{N}$ are **not known a priori**. They take whatever values are required to enforce the constraint:
   * **Surface ($\dim(V_N) = 1$):** $\mathbf{N} = N_1\,\mathbf{n}$ (1 unknown scalar $N_1(t)$).
   * **Curve ($\dim(V_N) = 2$):** $\mathbf{N} = N_1\,\mathbf{n}_f + N_2\,\mathbf{n}_g$ (2 unknown scalars $N_1(t), N_2(t)$).

---

## 2. Closure of the Constrained Dynamical System

Newton's Second Law yields 3 scalar equations in 3D:
$$ m_P\,\mathbf{a}_0^P = \mathbf{F}_{\text{applied}} + \mathbf{N} $$

Let $n = \text{CDOF}$ and $k = \dim(V_N)$ be the number of unknown reaction components:
* **Curve:** $n = 1$ CDOF, $k = 2$ reaction unknowns $\implies n + k = 1 + 2 = 3$ unknowns.
* **Surface:** $n = 2$ CDOFs, $k = 1$ reaction unknown $\implies n + k = 2 + 1 = 3$ unknowns.

Because there are exactly 3 equations for 3 unknowns, the dynamic system is **mathematically closed and well-posed**.

---

## 3. The Dynamical Decoupling Method (Slide 14)

Rather than solving a coupled system of algebraic and differential equations simultaneously, we exploit the orthogonality of $V_T$ and $V_N$ to decouple the problem into two sequential steps:

```
               NEWTON'S SECOND LAW: m a = F_app + N
                                 |
        +------------------------+------------------------+
        |                                                 |
  Project onto V_T                                  Project onto V_N
  (N . t = 0)                                       (Solves for reactions)
        |                                                 |
  v                                                 v
PURE EQUATIONS OF MOTION:                         ALGEBRAIC REACTION EQUATIONS:
Solve generalized coordinates q_i(t)              N_1(q, \dot{q}), N_2(q, \dot{q})
```

### 3.1 Step 1: Solving Generalized Coordinates (Tangent Projection)
Projecting Newton's second law onto the basis of the tangent subspace $V_T$:
* **Curve Case (Project along $\mathbf{t}$):**
  $$ m_P\,\mathbf{a}_0^P \cdot \mathbf{t} = \mathbf{F}_{\text{applied}} \cdot \mathbf{t} + \underbrace{\mathbf{N} \cdot \mathbf{t}}_{=0} \implies m_P\,\mathbf{a}_0^P \cdot \mathbf{t} = \mathbf{F}_{\text{applied}} \cdot \mathbf{t} $$
* **Surface Case (Project along $\mathbf{t}_\alpha, \mathbf{t}_\beta$):**
  $$ m_P\,\mathbf{a}_0^P \cdot \mathbf{t}_\alpha = \mathbf{F}_{\text{applied}} \cdot \mathbf{t}_\alpha, \quad m_P\,\mathbf{a}_0^P \cdot \mathbf{t}_\beta = \mathbf{F}_{\text{applied}} \cdot \mathbf{t}_\beta $$

Because $\mathbf{N} \in V_N \perp V_T$, all reaction forces vanish identically! This yields an isolated system of $n$ second-order ODEs for the generalized coordinates $q_i(t)$.

### 3.2 Step 2: Determining Constraint Forces (Normal Projection)
Once the motion $q_i(t), \dot{q}_i(t), \ddot{q}_i(t)$ is known, project Newton's second law onto the basis of $V_N$:
* **Surface Case (Project along $\mathbf{n}$):**
  $$ m_P\,\mathbf{a}_0^P \cdot \mathbf{n} = \mathbf{F}_{\text{applied}} \cdot \mathbf{n} + N_1\,\|\mathbf{n}\|^2 \implies N_1 = \frac{(m_P\,\mathbf{a}_0^P - \mathbf{F}_{\text{applied}}) \cdot \mathbf{n}}{\|\mathbf{n}\|^2} $$
* **Curve Case (Project along $\mathbf{n}_f, \mathbf{n}_g$):**
  Yields a $2 \times 2$ linear system for $N_1$ and $N_2$.

---

## 4. Benchmark Summary: Vertical Circular Wire (Slide 15)
For a particle of mass $m$ sliding along a vertical circular wire of radius $a$ in $Oxy$:
* Tangent projection ($\mathbf{e}_\theta$):
  $$ m a\ddot{\theta} = -mg\cos\theta \implies \ddot{\theta} + \frac{g}{a}\cos\theta = 0 $$
* Normal projection ($\mathbf{e}_R$):
  $$ -m a\dot{\theta}^2 = N_R - mg\sin\theta \implies N_R(\theta, \dot{\theta}) = mg\sin\theta - ma\dot{\theta}^2 $$

---

## 🔗 Related Notes
* [[Topic 3 - Constraints and Reaction Forces|Topic 3 Master Guide]]
* [[Concept - Normal and Tangent Subspaces for Surfaces and Curves|Normal and Tangent Subspaces]]
* [[Concept - Work and Power of Constraint Forces and Energy Preservation|Work & Power of Constraints]]
