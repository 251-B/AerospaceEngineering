---
materia: "Aerospace Materials I"
tema: "Topic 9: Polymers"
origen: "Problems T9_Polymers.pdf, Problem 1"
dificultad: easy
badge: "Degree of polymerization · chains per gram"
tags:
  - official-problem
  - solved
  - molecular-weight
  - degree-of-polymerization
  - pmma
---

# ✏️ Problem: T9-01 — Degree of Polymerization and Number of Chains of PMMA

## 📄 Official Statement
> 1. The molecular weight of PMMA is 250 000 g/mol. If all the chains have the same size, calculate (a) the degree of polymerization and (b) number of chains in 1 g of polymer.
>
> Data: Atomic mass (g/mol): O = 16, H = 1, C = 12.
>
> *(Solution: (a) 2500; (b) 2.408 x10¹⁸ chains)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Monodisperse polymer.** All the chains have the same size, as the statement says, so every average molecular weight equals the molecular weight of one chain: $M_n = M_w = M = 250\,000$ g/mol and the index of polydispersion is $I = 1$ [Session 19 Slide 13].
2. **Repeat unit of PMMA.** Polymethyl methacrylate is $\mathrm{-[CH_2{-}C(CH_3)(COOCH_3)]_n-}$ [Session 19 Slide 50; Session 20 Slide 8]. Counting the atoms of the unit: C in $\mathrm{CH_2}$, the backbone C, $\mathrm{CH_3}$, $\mathrm{C{=}O}$ and $\mathrm{OCH_3}$ gives 5 C; H in $\mathrm{CH_2}$, $\mathrm{CH_3}$ and $\mathrm{OCH_3}$ gives $2 + 3 + 3 = 8$ H; and the ester group has 2 O. The repeat unit is $\mathrm{C_5H_8O_2}$.
3. **Avogadro's number.** $N_A = 6.022\times10^{23}$ mol⁻¹ (not given on the sheet; standard constant).

### Data
| Quantity | Symbol | Value |
| :--- | :--- | ---: |
| Molecular weight of the polymer | $M$ | 250 000 g/mol |
| Atomic masses | C, H, O | 12, 1, 16 g/mol |
| Mass of polymer | $m$ | 1 g |
| Avogadro's number | $N_A$ | $6.022\times10^{23}$ mol⁻¹ |

**Unknowns:** (a) the degree of polymerization $X_n$; (b) the number of chains $N$ in 1 g.

---

## 🧠 2. Model and Strategy

The degree of polymerization is the average number of monomer units in a chain [Session 19 Slide 12]:

$$X_n = \frac{M_n}{M_0}$$

with $M_0$ the molecular weight of the repeat unit. A mole of chains contains $N_A$ chains, so the number of chains in a mass $m$ is the number of moles of chains, $m/M$, times $N_A$.

**Strategy.**
1. Compute $M_0$ of the PMMA repeat unit from the atomic masses.
2. Divide the chain molecular weight by $M_0$.
3. Convert 1 g into moles of chains and then into chains.

---

## 🔢 3. Step-by-Step Derivation

### 1. Molecular weight of the repeat unit
$$M_0 = 5\,M_C + 8\,M_H + 2\,M_O = 5(12\ \text{g/mol}) + 8(1\ \text{g/mol}) + 2(16\ \text{g/mol})$$

$$M_0 = 60 + 8 + 32 = 100\ \text{g/mol}$$

### 2. (a) Degree of polymerization [Session 19 Slide 12]
$$X_n = \frac{M_n}{M_0} = \frac{250\,000\ \text{g/mol}}{100\ \text{g/mol}} = \mathbf{2500}$$

### 3. (b) Number of chains in 1 g
Moles of chains in 1 g:

$$n = \frac{m}{M} = \frac{1\ \text{g}}{250\,000\ \text{g/mol}} = 4.000\times10^{-6}\ \text{mol}$$

Number of chains:

$$N = n\,N_A = 4.000\times10^{-6}\ \text{mol}\times6.022\times10^{23}\ \text{mol}^{-1} = \mathbf{2.409\times10^{18}\ chains}$$

(more digits: $2.4088\times10^{18}$).

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $X_n = (\text{g/mol})/(\text{g/mol})$ is a pure number, as a count of units must be. $N = (\text{g})/(\text{g/mol})\times\text{mol}^{-1}$ is a pure number of chains.
- **Mass of one chain.** $M/N_A = 250\,000\ \text{g/mol}/6.022\times10^{23}\ \text{mol}^{-1} = 4.15\times10^{-19}$ g, and $1\ \text{g}/4.15\times10^{-19}\ \text{g} = 2.41\times10^{18}$ chains, the same result.
- **Second route.** 1 g holds $1/100 = 0.01$ mol of repeat units, that is $6.022\times10^{21}$ units; divided by 2500 units per chain this again gives $2.409\times10^{18}$ chains.
- **Limit.** If the chains were shorter (smaller $X_n$), the same gram would contain more chains: $N$ is inversely proportional to $M$.

### Interpretation
Each PMMA chain is a molecule of 2500 repeat units, about four hundred thousand times smaller in mass than a microgram, so even one gram of plastic holds a few $10^{18}$ macromolecules. In a real PMMA the chains are not all the same size; then $M$ in the statement would be the number average $M_n$, and the same two formulas would give the average degree of polymerization and the number of chains.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| (a) Degree of polymerization | 2500 | 2500 | agrees |
| (b) Chains in 1 g | $2.408\times10^{18}$ | $2.4088\times10^{18}$ | agrees; the key truncates the last digit |

## 🔗 Related Links
* [[Topic 9 - Polymers]]
