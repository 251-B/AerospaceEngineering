---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 14"
dificultad: hard
tags:
  - official-problem
  - solved
  - invariant-reactions
  - congruent-melting
  - phase-diagram-reading
---

# ✏️ Problem: T4-PD14 — Reading a Hypothetical Diagram with Several Compounds

## 📄 Official Statement
> **14. In the following graph, a hypothetical phase diagram is represented, identify and explain the following: a) The existing phases in each phase field of the diagram. b) The invariant reactions writing the temperature and the reaction's equation, the composition of each phase inside the reaction and its name. c) The congruent and incongruent fusion phases.**
>
> ![[attachments/T4/pd-p14-diagram.png]]
>
> *(Solution, from the annotated diagram of Solution problems Phase diagrams I.pdf, p. 37; the sheet prints none: β incongruent melting; γ congruent melting; δ incongruent melting; ε incongruent melting)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium**; the diagram has no printed values except the axes (wt% B; temperature assumed in °C, since the axis prints no unit), so every number below is a **reading of the figure**, to about ±1 wt% and ±10 °C.
2. Phases are named as in the official solution (p. 37): terminal solid solutions α (A side) and ζ (B side), intermediate phases β, γ (a vertical line: a compound of fixed composition at about 62 % B), δ and ε, and the liquid L.
3. Each horizontal line is an invariant reaction, named by its shape [Session 8 Slide 6]; melting is congruent at a maximum of the liquidus and incongruent at a peritectic line [Session 8 Slide 17].

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: composition (wt% B) against temperature. The diagram is read on horizontal lines, from the top down and from left to right; no change of basis is involved.

**Method.** (a) Single-phase fields are the regions bounded by curved lines that touch the axis or a dome; each two-phase field takes the phases on its two sides along a horizontal tie line [Session 7 Slide 15]. (b) For each horizontal line: the three phases at its ends and middle point, and the shape. (c) Where each intermediate phase ends at the top.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Phase fields
| Field | Phases |
| :--- | :--- |
| top | L |
| A side, below the liquidus | α + L, then α |
| around 20 % B | β; α + β on its left; β + L above the 700 °C line on its right |
| 23-62 % B, below 700 °C | β + γ |
| 43-62 % B, above 700 °C | γ + L |
| 62 % B | γ (vertical line) |
| 62-72 % B, above 660 °C | γ + L |
| closed field near 68 % B, 430-660 °C | δ, with γ + δ, δ + L and δ + ε around it |
| 62-80 % B, below 430 °C | γ + ε |
| around 80 % B | ε, with ε + L above it |
| 81-94 % B, below 495 °C | ε + ζ |
| B side | ζ + L, then ζ |

### b) Invariant reactions (on cooling, wt% B)
| T (°C) | Reaction | Name |
| :--- | :--- | :--- |
| ≈ 895 | $\alpha\,(8) + L\,(28) \rightarrow \beta\,(19)$ | peritectic |
| ≈ 700 | $L\,(43) \rightarrow \beta\,(23) + \gamma\,(62)$ | eutectic |
| ≈ 660 | $\gamma\,(62) + L\,(72) \rightarrow \delta\,(68)$ | peritectic |
| ≈ 595 | $\delta\,(71) + L\,(84) \rightarrow \varepsilon\,(80)$ | peritectic |
| ≈ 495 | $L\,(90) \rightarrow \varepsilon\,(81) + \zeta\,(94)$ | eutectic |
| ≈ 430 | $\delta\,(68) \rightarrow \gamma\,(62) + \varepsilon\,(76)$ | eutectoid |

### c) Melting
- **γ melts congruently** at about 865 °C: it is at the maximum of its liquidus dome, and the liquid formed has its composition.
- **β, δ and ε melt incongruently**: each ends at a peritectic line (895, 660 and 595 °C), where on heating it gives a liquid plus a different solid (β → α + L, δ → γ + L, ε → δ + L).
- The pure components A (≈ 1200 °C) and B (≈ 695 °C) also melt congruently, like any pure metal [Session 8 Slide 17].

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- On every eutectic and eutectoid line the parent phase (L or δ) lies **between** the two products; on every peritectic line the product lies between the two reactants, with the liquid at one end [Session 8 Slide 6].
- Phase rule: three phases on each horizontal line, $F = 2 - 3 + 1 = 0$ [Session 7 Slide 13].
- δ is a closed field: it is created by a peritectic at 660 °C and destroyed by a eutectoid at 430 °C, so it exists only between those temperatures.
- **Limiting case**: an alloy with exactly the composition of a line compound (γ) is a single phase, with fractions 1 or 0 and no tie line; every two-phase reading above lies strictly between its tie-line ends.

### Interpretation
The diagram is a chain of simple diagrams joined at the compounds. A phase that touches the liquid only at a horizontal line cannot exist as a liquid of its own composition, which is the meaning of incongruent melting.

## ✅ Check against the official solution
Part (c) agrees with the key (β, δ, ε incongruent; γ congruent). The key gives no temperatures or compositions for part (b); they are readings of the figure here. The field labels agree with the annotated diagram of Solution problems Phase diagrams I.pdf, p. 37.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Invariant Reactions in Binary Systems]]
* [[Concept - Intermetallic Compounds and Congruent Melting]]
