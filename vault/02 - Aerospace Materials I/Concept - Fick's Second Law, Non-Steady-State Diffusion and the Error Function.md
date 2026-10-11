---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Slides 18-21"
tags:
  - theory
  - key-concept
  - ficks-second-law
  - error-function
dificultad: medium
prerrequisitos: []
---

# 📖 Concept: Fick's Second Law, Non-Steady-State Diffusion and the Error Function

> **Key idea in one sentence:** when the concentration changes with time, Fick's second law gives its evolution; for a semi-infinite solid with constant surface concentration the solution is an error function.

Full explanation: [[Topic 3 - Diffusion in Solids and Mass Transport]].

## Law [Session 5 Slides 18-19]
$$\frac{\partial C_x}{\partial t} = \frac{\partial}{\partial x}\left(D\frac{\partial C}{\partial x}\right) \;\xrightarrow{\;D \neq f(C)\;}\; \frac{\partial C_x}{\partial t} = D\,\frac{\partial^2 C}{\partial x^2}$$
Boundary conditions must match the experiment.

## Semi-infinite solid [Session 5 Slides 20-21]
Conditions: $C = C_0$ for all $x$ at $t = 0$; $C = C_s$ at $x = 0$ and $C = C_0$ at $x = \infty$ for $t > 0$.
$$\frac{C_x - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$
Examples: carbon into steel, a metal absorbing atmospheric gases. erf values are tabulated (e.g. erf(0.5) = 0.5205, erf(1.0) = 0.8427).

![[attachments/T3/fick2.svg]]

**Back to:** [[Topic 3 - Diffusion in Solids and Mass Transport]] · [[Aerospace Materials I MOC]]
