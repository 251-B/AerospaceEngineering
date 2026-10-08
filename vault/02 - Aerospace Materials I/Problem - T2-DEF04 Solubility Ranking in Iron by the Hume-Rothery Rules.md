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
> | Element | Atomic radius (nm) | Crystalline Structure | Electronegativity | Valence |
> | :--- | :---: | :---: | :---: | :---: |
> | **Iron (Fe)** | $0.124$ | **BCC** | $1.7$ | $+2, +3$ |
> | **Nickel (Ni)** | $0.125$ | **FCC** | $1.8$ | $+2$ |
> | **Molybdenum (Mo)** | $0.136$ | **BCC** | $1.3$ | $+3, +4, +6$ |
> | **Manganese (Mn)** | $0.112$ | **Simple cubic** | $1.6$ | $+2, +3, +6, +7$ |

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

---

## 🧠 2. Phase 2: Frames and Change of Basis

Solid solubility in substitutional solutions is governed by the **4 Hume-Rothery rules** [Session 4 Slide 22]:

1. **Atomic radius difference ($\Delta R$):** It must be below $15\%$ for appreciable solubility:
   $$\Delta R = \frac{|R_{\text{soluto}} - R_{\text{Fe}}|}{R_{\text{Fe}}} \times 100\%$$
2. **Crystal structure:** Solute and matrix must share the **same lattice structure**. If they differ (e.g. BCC vs FCC or SC), complete solubility is physically impossible.
3. **Electronegativity:** The difference $|\Delta \chi|$ must be minimal. Large differences favour intermetallic compounds instead of a solid solution.
4. **Valence:** Same valence, or a solute valence compatible with the oxidation states of the matrix.

---

## 🔢 3. Phase 3: Step-by-Step Comparative Evaluation of the Criteria

### 1. Evaluation of Molybdenum ($\text{Mo}$):
* **Atomic radius difference:**
  $$\Delta R_{\text{Mo}} = \frac{|0.136 - 0.124|}{0.124} \times 100\% = \frac{0.012}{0.124} \times 100\% = \mathbf{9.68\%} < 15\% \quad \checkmark$$
* **Crystal structure:** **BCC** $\implies$ **Identical to that of Iron ($\alpha\text{-Fe}$)** $\checkmark$ (Determining factor for wide solubility in ferrite).
* **Electronegativity:** $\Delta \chi = |1.3 - 1.7| = 0.4$ (moderate).
* **Valence:** Shares the common valence $+3$.
* **Conclusion:** Having the **same BCC lattice** and comfortably meeting the size criterion ($\approx 9.7\%$), $\text{Mo}$ is a ferrite stabiliser with very high solid solubility in $\alpha\text{-Fe}$.

---

### 2. Evaluation of Nickel ($\text{Ni}$):
* **Atomic radius difference:**
  $$\Delta R_{\text{Ni}} = \frac{|0.125 - 0.124|}{0.124} \times 100\% = \frac{0.001}{0.124} \times 100\% = \mathbf{0.81\%} \ll 15\% \quad \checkmark$$
  *(Almost identical atomic size).*
* **Crystal structure:** **FCC** $\neq$ **BCC** $\times$ (Different crystal structure).
* **Electronegativity:** $\Delta \chi = |1.8 - 1.7| = 0.1$ (optimal similarity).
* **Valence:** Shares the valence $+2$.
* **Conclusion:** Although it meets the size ($0.8\%$) and electronegativity criteria unsurpassably well, its crystal structure is **FCC** (it is an austenite $\gamma$ stabiliser). Because the lattice does not match, its solubility in $\alpha\text{-Fe}$ (BCC) is lower than that of Molybdenum, but higher than that of Manganese.

---

### 3. Evaluation of Manganese ($\text{Mn}$):
* **Atomic radius difference:**
  $$\Delta R_{\text{Mn}} = \frac{|0.112 - 0.124|}{0.124} \times 100\% = \frac{0.012}{0.124} \times 100\% = \mathbf{9.68\%} < 15\% \quad \checkmark$$
* **Crystal structure:** **Simple Cubic (SC)** $\neq$ **BCC** $\times$. The simple cubic lattice has a very low packing ($\text{APF} = 0.52$) and coordination $6$, completely incompatible with the BCC lattice ($\text{NC}=8$, $\text{APF}=0.68$).
* **Electronegativity:** $\Delta \chi = |1.6 - 1.7| = 0.1$.
* **Conclusion:** Owing to the radical crystal-structure mismatch with an atypical simple cubic lattice, it shows the lowest relative solubility in the BCC iron lattice.

---

## 🎯 4. Phase 4: Units and Limits, with Conclusion

### Definitive Solubility Hierarchy in $\alpha\text{-Fe}$:
$$\mathbf{Mo > Ni > Mn}$$

1. **Molybdenum ($\text{Mo}$):** It is the most soluble because it **shares the same BCC crystal structure** as iron and comfortably satisfies the Hume-Rothery size criterion ($\Delta R < 15\%$).
2. **Nickel ($\text{Ni}$):** It occupies the intermediate position: its radii are practically equal ($\Delta R < 1\%$), but its **FCC** structure limits its solubility in BCC ferrite.
3. **Manganese ($\text{Mn}$):** It shows the lowest solubility in the iron lattice because of its simple cubic crystal structure.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
