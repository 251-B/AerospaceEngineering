---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams II.pdf, Problem 9"
dificultad: hard
tags:
  - official-problem
  - solved
  - fe-c-system
  - cast-iron
  - ledeburite
---

# ✏️ Problem: T4-FC09 — A 3 % C Cast Iron from 1146 to 800 °C

## 📄 Official Statement
> **9. Examine closely the phase diagram Fe-C answer the following questions. a) Calculate the percentage of C in an alloy that has 64.7 % of austenite and 35.5 % of cementite at 800 ºC. What kind of alloy is it? b) What microconstituents does it have at 1146ºC? Calculate the quantity of each one. c) How do microconstituents change when cooling down from 1146 ºC to 800 ºC?**
>
> *(Solutions: a) $C_0$ = 3%; hypoeutectic cast iron; b) $w_{\gamma primary}$ = 60.2%; $w_{ledeburite}$ = 39.8%; $w_{Fe_3C\,ledeburite}$ = 18.8%; $w_{\gamma ledeburite}$ = 21%; $w_{\gamma total}$ = 81.2%; c) Fe₃C precipitates (secondary Fe₃C); $w_{Fe_3C\,secondary}$ = 16.3%)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

1. Equilibrium, Fe-Fe₃C diagram [Session 9 Slide 4].
2. **Reading of the figure:** at 800 °C the $A_{cm}$ line is at about 1.0 % C (a straight line from (0.76, 727) to (2.14, 1147) gives 0.99).
3. The data of the statement add up to 100.2 %; each fraction is used on its own to get $C_0$, and the two results are compared.

---

## 🧠 2. Phase 2: Frames and Change of Basis

Tie lines: 800 °C (γ 1.0 / Fe₃C 6.67), 1147 + ΔT (γ 2.14 / L 4.30), 1146 °C (γ 2.14 / Fe₃C 6.67). The lever rule is solved for $C_0$ in (a) and applied in (b) and (c); microconstituents as in Session 7 Slide 32.

![[attachments/T4/fc-p9.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Composition
From the austenite: $W_\gamma = \dfrac{6.67 - C_0}{6.67 - 1.0} = 0.647 \Rightarrow C_0 = 6.67 - 0.647 \times 5.67 = 6.67 - 3.668 = 3.00$ % C.

From the cementite: $W_{\text{Fe}_3\text{C}} = \dfrac{C_0 - 1.0}{5.67} = 0.355 \Rightarrow C_0 = 1.0 + 0.355 \times 5.67 = 1.0 + 2.013 = 3.01$ % C.

Both give **$C_0$ ≈ 3.0 % C**: $2.14 < 3.0 < 4.30$, a **hypoeutectic cast iron**.

### b) Microconstituents at 1146 °C
Just above 1147 °C (γ 2.14 / L 4.30; length 2.16):
$$W_{\gamma,p} = \frac{4.30 - 3.0}{2.16} = \frac{1.30}{2.16} = 0.602 \qquad W_L = \frac{3.0 - 2.14}{2.16} = \frac{0.86}{2.16} = 0.398$$
At 1146 °C the liquid has become **ledeburite** (0.398) and the **primary austenite** remains (0.602). Phases at 1146 °C (γ 2.14 / Fe₃C 6.67; length 4.53):
$$W_{\text{Fe}_3\text{C}} = \frac{3.0 - 2.14}{4.53} = \frac{0.86}{4.53} = 0.190 \qquad W_{\gamma,\text{total}} = 1 - 0.190 = 0.810$$
All the cementite is in the ledeburite (0.190), so the austenite of the ledeburite is $0.398 - 0.190 = 0.208$.

![[attachments/T4/fc-micro-p9.svg]]

### c) From 1146 to 800 °C
The austenite (primary and eutectic) loses carbon along $A_{cm}$, from 2.14 to 1.0 % C, and the excess precipitates as **secondary cementite** [Session 9 Slide 11]. At 800 °C:
$$W_{\text{Fe}_3\text{C}}(800) = \frac{3.0 - 1.0}{5.67} = \frac{2.0}{5.67} = 0.353 \qquad W_{\text{Fe}_3\text{C},\text{sec}} = 0.353 - 0.190 = 0.163$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

- Ledeburite make-up: $0.190/0.398 = 0.477$ Fe₃C, as in Worked example 14 ✓.
- At 800 °C: γ $1 - 0.353 = 0.647$ — exactly the 64.7 % of the statement ✓.

## ✅ Check against the official solution
Agrees with the key: 3 %, hypoeutectic cast iron, 60.2 %, 39.8 % and 16.3 %. With 6.67 % C the cementite of the ledeburite is 19.0 % (key 18.8 %, from 6.7 % C), its austenite 20.8 % (key 21 %) and the total austenite 81.0 % (key 81.2 %): differences of rounding only.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - The Fe-Fe3C Diagram and Steel Microstructures]]
* [[Problem - T4-FC10 Fe-Cementite Questions and Pearlite Limits]]
