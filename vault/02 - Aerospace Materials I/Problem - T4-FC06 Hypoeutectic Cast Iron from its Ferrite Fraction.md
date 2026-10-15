---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams II.pdf, Problem 6"
dificultad: medium
tags:
  - official-problem
  - solved
  - fe-c-system
  - cast-iron
  - ledeburite
---

# ✏️ Problem: T4-FC06 — Hypoeutectic Cast Iron from its Ferrite Fraction

## 📄 Official Statement
> **6.- Consider a steel with a content of C < 4.3% at (727−ΔT)ºC. In these conditions, $\chi_\alpha$ = 0.47. Indicate the mass fraction of the phases at (1147+ΔT)ºC and (1147−ΔT)ºC.**
>
> *(Solution: T1: $w_\gamma$ = 0.32, $\chi_L$ = 0.68; T2: $w_\gamma$ = 0.68, $\chi_{Fe_3C}$ = 0.32, $w_E$ = 0.68, $\chi_{\gamma E}$ = 0.36, $w_{Fe_3C}$ = 0.32)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

1. Equilibrium, Fe-Fe₃C diagram [Session 9 Slide 4]: α 0.022, γ 2.14 (at 1147 °C), eutectic 4.30, Fe₃C 6.67 % C.
2. Unknown first: $C_0$, from the ferrite fraction just below 727 °C.
3. The statement says "steel", but the result is above 2.14 % C, so the alloy is a **hypoeutectic cast iron** (it has ledeburite).

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Fe-Fe₃C diagram (wt% C, °C), with tie lines at 727 − ΔT (α-Fe₃C), 1147 + ΔT (γ-L) and 1147 − ΔT (γ-Fe₃C). Step 1 solves the lever rule for $C_0$; steps 2-3 apply it at 1147 ± ΔT; microconstituents as in Session 7 Slide 32.

![[attachments/T4/fc-p6.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Composition
$$W_\alpha = \frac{C_{\text{Fe}_3\text{C}} - C_0}{C_{\text{Fe}_3\text{C}} - C_\alpha} \;\Rightarrow\; C_0 = C_{\text{Fe}_3\text{C}} - W_\alpha\,(C_{\text{Fe}_3\text{C}} - C_\alpha) = 6.67 - 0.47 \times 6.648 = 6.67 - 3.125 = 3.545 \approx 3.55\ \%\,\text{C}$$

### 2. $T_1$ = 1147 + ΔT (γ 2.14 / L 4.30; length 2.16)
$$W_L = \frac{C_0 - C_\gamma}{C_L - C_\gamma} = \frac{3.545 - 2.14}{2.16} = \frac{1.405}{2.16} = 0.650 \qquad W_\gamma = \frac{4.30 - 3.545}{2.16} = \frac{0.755}{2.16} = 0.350$$

### 3. $T_2$ = 1147 − ΔT (γ 2.14 / Fe₃C 6.67; length 4.53)
$$W_{\text{Fe}_3\text{C}} = \frac{3.545 - 2.14}{4.53} = \frac{1.405}{4.53} = 0.310 \qquad W_\gamma = \frac{6.67 - 3.545}{4.53} = \frac{3.125}{4.53} = 0.690$$

**Microconstituents at $T_2$:** primary austenite = γ at $T_1$ = 0.350; ledeburite = L at $T_1$ = 0.650, made of γ $0.690 - 0.350 = 0.340$ and Fe₃C 0.310.

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

- Ledeburite make-up: $0.340/0.650 = 0.523$ γ, as in Worked example 14 ✓.
- Mass balance at $T_2$: $0.690 \times 2.14 + 0.310 \times 6.67 = 1.48 + 2.07 = 3.55$ % C ✓.
- **Limiting cases** (fractions dimensionless, compositions in wt% C): the ferrite fraction $(6.67 - C_0)/6.648$ is 1 at $C_0 = 0.022$ and 0 at $C_0 = 6.67$; 0.47 lies between, so $C_0$ lies between those limits, here inside the cast-iron range.

## ✅ Check against the official solution
The method matches the worked page of Solution problems Phase diagrams II.pdf, p. 12.

> [!warning] Discrepancy with the official solution
> The worked page rounds the composition to $C_0 = 3.6$ % C before going on (with 6.7 % C it is 3.56) and so gives 0.68/0.32 at $T_1$, 0.32/0.68 at $T_2$, primary γ 0.32 and eutectic γ 0.36. With the unrounded $C_0 = 3.545$ % C the values are 0.650/0.350, 0.310/0.690, primary γ 0.350 and eutectic γ 0.340; the computed values are kept. The page also writes the formula for $\chi_L$ with the labels of the α-Fe₃C tie line; its numbers, $(3.6 - 2.14)/(4.3 - 2.14)$, are those of the γ-L tie line used here.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - The Fe-Fe3C Diagram and Steel Microstructures]]
* [[Problem - T4-FC07 Hypereutectic Cast Iron from its Cementite Fraction]]
