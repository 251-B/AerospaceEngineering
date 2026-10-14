---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams II.pdf, Problem 11"
dificultad: easy
tags:
  - official-problem
  - solved
  - ternary-diagrams
---

# ✏️ Problem: T4-FC11 — Composition of a Ternary Alloy

## 📄 Official Statement
> **11.- Determine the composition in wt% of the ternary alloy H marked in the diagram below:**
>
> ![[attachments/T4/fc-p11-sheet.png]]
>
> *(Solution: 40% C + 33% A + 30%B)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

1. The diagram is a ternary composition triangle in weight percent: corners A (top), B (bottom left) and C (bottom right); the grid lines are every 10 % [Session 10 Slide 5].
2. The axes, as labelled on the sheet: "porcentaje en peso de A" on the right side, "de B" on the left side, "de C" on the bottom.
3. H is drawn on a node of the grid (a reading of the figure).
4. Unknowns: $w_A$, $w_B$, $w_C$, with $w_A + w_B + w_C = 100$ %.

---

## 🧠 2. Phase 2: Frames and Change of Basis

**Frame:** the triangle itself. Each component is read along the lines parallel to the side opposite its corner: constant A is parallel to B-C, constant B parallel to A-C, constant C parallel to A-B [Session 10 Slides 5, 7]. The three readings are independent, so the condition that they add up to 100 % is a check of the reading, not an extra equation.

![[attachments/T4/fc-p11.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

1. **% A.** The horizontal line through H (parallel to B-C) is the third line above the base B-C: it meets the A axis (right side) at **30 % A**.
2. **% B.** The line through H parallel to the A-C side meets the B axis (left side) at **30 % B**.
3. **% C.** The line through H parallel to the A-B side meets the C axis (bottom) at **40 % C**.

**Composition of H: 30 wt% A, 30 wt% B, 40 wt% C.**

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

- Sum: $30 + 30 + 40 = 100$ % ✓.
- Position check: on the 30 % A line, the remaining 70 % is shared between B and C; H is at $40/70 = 0.57$ of the way from the B side to the C side of that line, which agrees with its place on the drawing.
- Limits: a point on a side has 0 % of the opposite component; a corner is 100 % of its component.

## ✅ Check against the official solution

> [!warning] Discrepancy with the official solution
> The key gives "40% C + 33% A + 30% B", which adds up to 103 %, so it cannot be right. H lies on the 30 % A line of the grid (the third line above B-C), and with 30 % B and 40 % C the sum is 100 %. The value 33 % A is a typo for 30 %; the reading 30/30/40 is kept.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Ceramic and Ternary Phase Diagrams]]
