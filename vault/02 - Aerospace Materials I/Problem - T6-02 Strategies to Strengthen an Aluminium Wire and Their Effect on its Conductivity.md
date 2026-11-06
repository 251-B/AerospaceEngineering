---
materia: "Aerospace Materials I"
tema: "Topic 6: Electrical Properties"
origen: "Problems T6andT7_Electric and Magnetic Properties.pdf, Problem 2"
dificultad: medium
badge: "Conductivity · strengthening · Matthiessen"
tags:
  - official-problem
  - solved
  - matthiessen
  - strengthening
  - residual-resistivity
---

# ✏️ Problem: T6-02 — Strategies to Strengthen an Aluminium Wire and Their Effect on its Conductivity

## 📄 Official Statement
> 2. Reason what effect the following strategies would have on the conductivity and tensile strength of an aluminum alloy wire:
>
> - a) Alloying with a more conductive metal as copper.
> - b) Decrease on its working temperature.
> - c) Thermal treatment that increases the grain size of the alloy.
> - d) Treatment that causes intermetallic precipitation.
> - e) Metal drawing (forming) that involves a high % of cold work.
>
> Indicate which would be the best strategy to reduce the weight of the wire while maintaining its tensile strength and conductivity.
>
> *(Solution: a) conductivity: decrease; strength: increase; b) conductivity: increase; strength: more increase; c) conductivity: increase; strength: decrease; d) conductivity: decrease; strength: increase; e) conductivity: decrease; strength: increase)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Matthiessen's rule.** The total resistivity of a metal is the thermal part plus the residual part, and the residual part is the sum of an impurity part and a deformation part [Session 13 Slides 14, 16]. Conductivity is the inverse of resistivity [Session 13 Slide 13].
2. **Scattering lowers conductivity.** Anything that distorts the metal lattice scatters the conduction electrons, reduces their mobility and therefore the conductivity [Session 13 Slides 16-17].
3. **All hardening methods lower the conductivity** to a greater or lesser extent [Session 13 Slide 18], and they raise the strength by making dislocation glide harder (Topic 5).
4. **Notation.** The sheet uses "σ" for conductivity in this topic and for stress in Topic 5; here the electrical conductivity is $\gamma$ and the tensile strength is $\sigma_{ts}$, to keep both in the same equation without confusion.
5. **Same alloy density and length.** For the weight comparison the density and the length of the wire do not change with the strategy; only the section $A$ does.

### Data
| Quantity | Symbol | Meaning |
| :--- | :--- | :--- |
| Electrical conductivity | $\gamma=1/\rho$ | property to keep or improve |
| Tensile strength | $\sigma_{ts}$ | property to keep or improve |
| Wire section | $A$ | unknown to reduce (mass $\propto A$) |

**Unknown:** the direction of change of $\gamma$ and $\sigma_{ts}$ for each strategy, and the strategy that allows the lightest wire.

---

## 🧠 2. Model and Strategy

Each strategy acts on one term of Matthiessen's rule and, at the same time, on dislocation motion. The figure collects the directions of the key: only strategy b moves into the quadrant in which both properties improve.

![[attachments/T6/t6-p2-strategies.svg]]

**Strategy.**
1. Write Matthiessen's rule and decide, for each strategy, which resistivity term changes and in which direction.
2. Read the effect on the strength from Topic 5 (strengthening mechanisms) and from the chart of Slide 18.
3. For the weight question, write the three conditions of a wire of section $A'$ (load capacity, conductance, mass) and find when $A'<A$ is allowed.

---

## 🔢 3. Step-by-Step Derivation

### 1. The law that governs the conductivity [Session 13 Slides 13, 14, 16]
Total resistivity as the sum of the thermal, impurity and deformation parts, and its inverse:

$$\rho_{\text{total}}=\rho_T+\rho_r=\rho_T+\rho_i+\rho_d$$

$$\gamma=\frac{1}{\rho_{\text{total}}}=\frac{1}{\rho_T+\rho_i+\rho_d}$$

A larger sum in the denominator means a smaller conductivity; a smaller sum means a larger one.

### 2. Strategy a: alloying with copper
The solute atoms are foreign atoms in the aluminium lattice and scatter the electrons whatever their own conductivity (Slide 16 shows that every addition raises the resistivity of copper); copper dissolved in aluminium therefore adds to $\rho_i$ (Topic 5: solid solution strengthening):

$$\rho_i\uparrow\ \Rightarrow\ \rho_{\text{total}}\uparrow\ \Rightarrow\ \gamma=\frac{1}{\rho_{\text{total}}}\downarrow\qquad\sigma_{ts}\uparrow$$

### 3. Strategy b: lower working temperature
The thermal term is $\rho_T=\rho_0(1+\alpha_T T)$ [Session 13 Slide 14], which falls when $T$ falls:

$$T\downarrow\ \Rightarrow\ \rho_T\downarrow\ \Rightarrow\ \rho_{\text{total}}\downarrow\ \Rightarrow\ \gamma\uparrow$$

The key also gives a strength increase, larger than the others. This is the reading of the key, not a derivation from the slides; the usual reason is that at lower temperature the atoms vibrate less and thermally assisted dislocation motion is weaker, so a higher stress is needed to move dislocations (a gloss, not content of Session 13):

$$T\downarrow\ \Rightarrow\ \sigma_{ts}\uparrow\uparrow$$

### 4. Strategy c: grain growth
A larger grain has fewer grain boundaries per unit volume, and the boundaries are part of the deformation term [Session 13 Slide 16]; at the same time the Hall-Petch effect of Topic 5 (grain size strengthening) weakens the metal:

$$d_{\text{grain}}\uparrow\ \Rightarrow\ \text{boundaries}\downarrow\ \Rightarrow\ \rho_d\downarrow\ \Rightarrow\ \gamma\uparrow\qquad\sigma_{ts}\downarrow$$

### 5. Strategy d: intermetallic precipitation
The precipitates are second-phase particles that scatter electrons and block dislocations (Topic 5: precipitation strengthening), and the matrix keeps a part of the solute that raises its impurity term [Session 13 Slide 16]:

$$\text{precipitates}\ \Rightarrow\ \rho_{\text{total}}\uparrow\ \Rightarrow\ \gamma\downarrow\qquad\sigma_{ts}\uparrow$$

### 6. Strategy e: heavy cold work
Drawing multiplies dislocations, which are structural imperfections of the deformation term [Session 13 Slide 16] (Topic 5: strain hardening). The chart of Slide 18 shows the yield strength rising strongly with the cold work while the conductivity falls only slightly:

$$\text{cold work}\uparrow\ \Rightarrow\ \rho_d\uparrow\ \Rightarrow\ \gamma\downarrow\ (\text{slightly})\qquad\sigma_{ts}\uparrow$$

### 7. The lightest wire that keeps strength and conductivity
Load capacity, conductance and mass of the original wire, of length $l$ and density $\rho_m$, and of the new wire of section $A'$ with properties $\gamma'$ and $\sigma_{ts}'$:

$$F_{\max}=\sigma_{ts}\,A\qquad G=\frac{\gamma\,A}{l}\qquad m=\rho_m\,A\,l$$

$$F'_{\max}=\sigma_{ts}'\,A'\qquad G'=\frac{\gamma'\,A'}{l}\qquad m'=\rho_m\,A'\,l$$

The new wire must carry at least the same load and conduct at least as well:

$$\sigma_{ts}'\,A'\ge\sigma_{ts}\,A\ \Rightarrow\ \frac{A'}{A}\ge\frac{\sigma_{ts}}{\sigma_{ts}'}$$

$$\frac{\gamma'\,A'}{l}\ge\frac{\gamma\,A}{l}\ \Rightarrow\ \frac{A'}{A}\ge\frac{\gamma}{\gamma'}$$

Both conditions together give a lower bound for the section, and the mass ratio equals the section ratio because $\rho_m$ and $l$ are unchanged:

$$\frac{m'}{m}=\frac{A'}{A}\ge\max\!\left(\frac{\sigma_{ts}}{\sigma_{ts}'},\ \frac{\gamma}{\gamma'}\right)$$

A lighter wire means $m'/m<1$, which is possible only if the larger of the two ratios on the right is below 1, that is, if both $\sigma_{ts}'>\sigma_{ts}$ and $\gamma'>\gamma$:

$$m'<m\ \Longleftrightarrow\ \sigma_{ts}'>\sigma_{ts}\ \text{and}\ \gamma'>\gamma$$

Applied to the five strategies of the key:

| Strategy | $\gamma'/\gamma$ | $\sigma_{ts}'/\sigma_{ts}$ | Lighter wire possible? |
| :--- | :---: | :---: | :--- |
| a alloying with Cu | $<1$ | $>1$ | no: conductance fixes $A'/A\ge\gamma/\gamma'>1$ |
| b lower temperature | $>1$ | $>1$ | yes |
| c grain growth | $>1$ | $<1$ | no: load capacity fixes $A'/A\ge\sigma_{ts}/\sigma_{ts}'>1$ |
| d precipitates | $<1$ | $>1$ | no: conductance |
| e cold work | $<1$ | $>1$ | no: conductance |

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Key.** The directions of a to e reproduce the key of the sheet term by term.
- **Units of the weight argument.** Each ratio is dimensionless, and the three conditions are homogeneous:

$$[F_{\max}]=\text{Pa}\cdot\text{m}^2=\text{N}\qquad[G]=\frac{\Omega^{-1}\text{m}^{-1}\cdot\text{m}^2}{\text{m}}=\Omega^{-1}\qquad[m]=\frac{\text{kg}}{\text{m}^3}\cdot\text{m}^2\cdot\text{m}=\text{kg}$$

- **Limit.** If $\gamma'=\gamma$ and $\sigma_{ts}'=\sigma_{ts}$ the bound is $A'/A\ge1$: no strategy, no saving.

### Interpretation
Strategies a, d and e buy strength with conductivity and strategy c does the opposite, so none of them can shrink the wire when both properties are required. Only a lower working temperature improves both, so it is the strategy that permits a lighter wire. This choice of "best" is the reasoning of this note from the conditions above; the key of the sheet lists only the directions of change. A lower working temperature needs cooling in service, which has its own cost and mass; a material change is the alternative route.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) alloying with Cu | γ decreases; strength increases | γ decreases; strength increases | agrees |
| b) lower temperature | γ increases; strength more increase | γ increases; strength increases most | agrees |
| c) larger grains | γ increases; strength decreases | γ increases; strength decreases | agrees |
| d) precipitates | γ decreases; strength increases | γ decreases; strength increases | agrees |
| e) cold work | γ decreases; strength increases | γ decreases; strength increases | agrees |
| Best strategy for a lighter wire | not printed | b | reasoning of this note (both properties must rise) |

## 🔗 Related Links
* [[Topic 6 - Electrical Properties]]
* [[Concept - Solid Solution Strengthening]]
* [[Concept - Grain Size Strengthening]]
* [[Concept - Precipitation Strengthening]]
* [[Concept - Strain Hardening and Percent Cold Work]]
