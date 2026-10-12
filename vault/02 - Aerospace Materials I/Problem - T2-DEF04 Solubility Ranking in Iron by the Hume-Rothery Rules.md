---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 4"
dificultad: medium
tags:
  - official-problem
  - solved
  - hume-rothery
  - iron-alloys
  - solubility
  - solid-solutions
---

# ✏️ Problem: T2-DEF04 — Ranking of Solubility in Iron by the Hume-Rothery Rules

## 📄 Official Statement
> **4. Using data in the table below, order the elements according to their solubility in iron, from higher to lower solubility. Justify your answer.**  
> *(Solution: $\text{Mo} > \text{Ni} > \text{Mn}$)*
> 
> | Element | Atomic radius (nm) | Crystalline Structure | *Electronegativity* | Valence |
> | :---: | :---: | :---: | :---: | :---: |
> | Iron | 0.124 | BCC | 1.7 | +2, +3 |
> | Nickel | 0.125 | FCC | 1.8 | +2 |
> | Molybdenum | 0.136 | BCC | 1.3 | +3, +4, +6 |
> | Manganese | 0.112 | Simple cubic | 1.6 | +2, +3,+6, +7 |

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Solvent Matrix:
* **Iron ($\alpha\text{-Fe}$):**
  * Atomic radius: $R_{\text{Fe}} = 0.124\text{ nm}$.
  * Crystal lattice: **BCC**.
  * Pauling electronegativity: $\chi_{\text{Fe}} = 1.7$.
  * Stable valences: $+2, +3$.

### Solutes to Evaluate:
1. **Nickel ($\text{Ni}$):** $R = 0.125\text{ nm}$, FCC, $\chi = 1.8$, Val = $+2$.
2. **Molybdenum ($\text{Mo}$):** $R = 0.136\text{ nm}$, BCC, $\chi = 1.3$, Val = $+3, +4, +6$.
3. **Manganese ($\text{Mn}$):** $R = 0.112\text{ nm}$, Simple Cubic, $\chi = 1.6$, Val = $+2, +3, +6, +7$.

In SI units the radii are $R_{\text{Fe}} = 1.24\times10^{-10}\text{ m}$, $R_{\text{Ni}} = 1.25\times10^{-10}\text{ m}$, $R_{\text{Mo}} = 1.36\times10^{-10}\text{ m}$, $R_{\text{Mn}} = 1.12\times10^{-10}\text{ m}$ ($1\text{ nm} = 10^{-9}\text{ m}$); the electronegativities are dimensionless (Pauling scale).

Hypotheses: substitutional solid solution of each element in iron with the BCC structure given in the table; the four Hume-Rothery conditions are qualitative [Session 4 Slide 23], so the ranking is obtained by comparing how many conditions each solute fulfils and by how much, giving priority to the crystal structure (the first condition on the slide: a solute that crystallises in a different lattice cannot replace solvent atoms over the whole composition range) and then to the size mismatch.

---

## 🧠 2. Phase 2: Frames and Change of Basis

Solid solubility in substitutional solutions is governed by the **4 Hume-Rothery rules** [Session 4 Slide 23]:

1. **Atomic radius difference ($\Delta R$):** It must be below $15\%$ for appreciable solubility:
   $$\Delta R = \frac{|R_{\text{solute}} - R_{\text{Fe}}|}{R_{\text{Fe}}} \times 100\%$$
2. **Crystal structure:** Solute and matrix must share the **same lattice structure**. If they differ (e.g. BCC vs FCC or SC), complete solubility is physically impossible.
3. **Electronegativity:** The difference $|\Delta \chi|$ must be minimal. Large differences favour intermetallic compounds instead of a solid solution.
4. **Valence:** Same valence, or a solute valence compatible with the oxidation states of the matrix.

---

## 🔢 3. Phase 3: Step-by-Step Comparative Evaluation of the Criteria

### 1. Size criterion (radius mismatch)
With $\Delta R = \dfrac{|R_{\text{solute}} - R_{\text{Fe}}|}{R_{\text{Fe}}}\times 100\%$ and $R_{\text{Fe}} = 0.124\text{ nm}$ [Session 4 Slide 23]:

$$\Delta R_{\text{Ni}} = \frac{|0.125 - 0.124|}{0.124}\times 100\% = \frac{0.001}{0.124}\times 100\% = 0.00806\times 100\% = 0.81\% < 15\% \quad \checkmark$$

$$\Delta R_{\text{Mo}} = \frac{|0.136 - 0.124|}{0.124}\times 100\% = \frac{0.012}{0.124}\times 100\% = 0.0968\times 100\% = 9.68\% < 15\% \quad \checkmark$$

$$\Delta R_{\text{Mn}} = \frac{|0.112 - 0.124|}{0.124}\times 100\% = \frac{0.012}{0.124}\times 100\% = 0.0968\times 100\% = 9.68\% < 15\% \quad \checkmark$$

All three are below the $15\%$ limit for metals, so none is restricted to the "limited solubility ($<1\%$)" case of the slide; Ni is by far the closest in size.

### 2. Crystal-structure criterion
* Mo: BCC, the same as Fe $\Rightarrow$ fulfilled $\checkmark$.
* Ni: FCC $\neq$ BCC $\Rightarrow$ not fulfilled $\times$.
* Mn: simple cubic $\neq$ BCC $\Rightarrow$ not fulfilled $\times$.

### 3. Electronegativity criterion
$$|\Delta\chi_{\text{Ni}}| = |1.8 - 1.7| = 0.1, \qquad |\Delta\chi_{\text{Mo}}| = |1.3 - 1.7| = 0.4, \qquad |\Delta\chi_{\text{Mn}}| = |1.6 - 1.7| = 0.1$$
Ni and Mn are equally close to Fe; Mo has the largest difference of the three.

### 4. Valence criterion
* Ni ($+2$) shares $+2$ with Fe ($+2, +3$).
* Mo ($+3, +4, +6$) shares $+3$.
* Mn ($+2, +3, +6, +7$) shares both $+2$ and $+3$.

No solute is excluded by valence.

### 5. Summary and ranking

| Solute | $\Delta R$ | Same structure as Fe (BCC) | $\lvert\Delta\chi\rvert$ | Common valence | Conditions fulfilled |
| :---: | :---: | :---: | :---: | :---: | :--- |
| Mo | $9.68\%$ ✓ | yes (BCC) ✓ | $0.4$ | $+3$ ✓ | structure, size, valence |
| Ni | $0.81\%$ ✓ | no (FCC) ✗ | $0.1$ | $+2$ ✓ | size (best), electronegativity, valence |
| Mn | $9.68\%$ ✓ | no (SC) ✗ | $0.1$ | $+2, +3$ ✓ | size, electronegativity, valence |

1. **Mo first.** It is the only solute with the same BCC lattice as iron, and its size mismatch ($9.68\%$) is within the $15\%$ limit. Its larger electronegativity difference ($0.4$) is the only weak point, and it does not outweigh the structural match.
2. **Ni versus Mn.** Both fail the structure condition, have the same $|\Delta\chi| = 0.1$ and share a valence with iron. The criterion that separates them is size: $0.81\%$ for Ni against $9.68\%$ for Mn, i.e. $9.68/0.81 \approx 12$ times larger mismatch for Mn. Hence Ni is more soluble than Mn.

$$\boxed{\text{Mo} > \text{Ni} > \text{Mn}}$$

This agrees with the official solution ($\text{Mo} > \text{Ni} > \text{Mn}$).

---

## 🎯 4. Phase 4: Units and Limits, with Conclusion

1. **Dimensional check:** $\Delta R$ is a ratio of two lengths, $[\Delta R] = \text{m}/\text{m} = 1$, so it can be computed in nm without converting to m: $\frac{1.2\times10^{-11}\text{ m}}{1.24\times10^{-10}\text{ m}} = 0.0968$, the same as $\frac{0.012\text{ nm}}{0.124\text{ nm}}$. Electronegativity differences are dimensionless (Pauling scale).
2. **Weighting of the rules:** the Hume-Rothery rules give conditions, not a formula [Session 4 Slide 23]: when one or more conditions fail the solubility is partial, and even when all are met total solubility is not guaranteed. The ranking above therefore rests on the order of importance used here (structure first, then size); with that order the result is unique, because Mo is the only solute that matches the lattice and the Ni/Mn tie in electronegativity and valence is broken by size.
3. **Limiting cases:** a solute with $\Delta R > 15\%$ would drop to the bottom regardless of the other rules (solubility $<1\%$ on the slide); a solute meeting all four conditions with a very small $\Delta R$ would be the candidate for complete solubility. None of the three solutes is a clear case of all four conditions: Mo has the largest electronegativity difference ($0.4$), while Ni and Mn fail the structure condition.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
