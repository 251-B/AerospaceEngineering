---
materia: "Aerospace Materials I"
tema: "Topic 9: Polymers"
origen: "Problems T9_Polymers.pdf, Problem 7"
dificultad: medium
badge: "Weight average · polydispersity · repeat unit"
tags:
  - official-problem
  - solved
  - molecular-weight
  - polydispersity
  - degree-of-polymerization
  - crystallinity
---

# ✏️ Problem: T9-07 — Weight Average, Polydispersity and Repeat Unit of a Polyalkene

## 📄 Official Statement
> 7. A thermoplastic polymer has been analyzed, obtaining the following fractions of weight wᵢ shown in the table for the following ranges of molecular weight in the table:
> a) Calculate the weight-average molecular weight
> b) Calculate de polydispersity assuming that the number average molecular weight is 12880 g/mol.
> c) If the polymerization degree is 230 and assuming that the polymer is an alkene (CₙH₂ₙ) with the general formula shown below, determine the value of X in the structural formula below. (Atomic mass: H = 1, C = 12).
> d) Explain if the crystallinity of the polymer should be higher or lower than the crystallinity of polyethylene.
>
> ![[attachments/T9/t9-p7-molecular-weight-table.png]]
>
> ![[attachments/T9/t9-p7-repeat-unit.png]]
>
> *(Solution: a) Mw = 15500 g/mol; b) PDI = 1.2; c) X = 1, polybutadiene; d) lower)*

The sheet prints "Calculate de polydispersity". The structural formula is a repeat unit $\mathrm{-CH_2{-}CH-}$ with the side chain $\mathrm{(CH_2)_X{-}CH_3}$ hanging from the CH, in brackets with subscript $n$.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Mean of each range.** Each range is represented by its midpoint $M_i$, as in the example of Session 19 Slides 14-15.
2. **Averages.** $M_w = \sum w_i M_i$ and the index of polydispersion $I = M_w/M_n$ [Session 19 Slide 13]; the sheet calls it PDI.
3. **Degree of polymerization.** The polymerization degree 230 is the number average $X_n = M_n/M_0$ [Session 19 Slide 12], with $M_n = 12\,880$ g/mol from part b).
4. **Repeat unit.** Counting the atoms of the drawn unit: $\mathrm{CH_2}$, $\mathrm{CH}$, $X$ groups $\mathrm{CH_2}$ and $\mathrm{CH_3}$.

### Data
| Range (g/mol) | Midpoint $M_i$ (g/mol) | $w_i$ |
| :--- | ---: | ---: |
| 0 – 5 000 | 2 500 | 0.02 |
| 5 000 – 10 000 | 7 500 | 0.12 |
| 10 000 – 15 000 | 12 500 | 0.32 |
| 15 000 – 20 000 | 17 500 | 0.32 |
| 20 000 – 25 000 | 22 500 | 0.22 |

$\sum w_i = 0.02 + 0.12 + 0.32 + 0.32 + 0.22 = 1.00$. Also $M_n = 12\,880$ g/mol, $X_n = 230$, C = 12 g/mol, H = 1 g/mol.

**Unknowns:** (a) $M_w$; (b) the polydispersity; (c) $X$; (d) crystallinity compared with polyethylene.

---

## 🧠 2. Model and Strategy

[Session 19 Slides 12-13]:

$$M_w = \sum w_i M_i \qquad I = \frac{M_w}{M_n} \qquad M_0 = \frac{M_n}{X_n}$$

**Strategy.**
1. Weight each midpoint by its weight fraction and add.
2. Divide by the given $M_n$.
3. Get $M_0$ from $M_n$ and $X_n$, write $M_0$ of the drawn unit as a function of $X$ and solve.
4. Compare the chain with polyethylene using the factors of crystallinity of Slides 26-27.

---

## 🔢 3. Step-by-Step Derivation

### 1. a) Weight-average molecular weight [Session 19 Slide 13]
| $M_i$ (g/mol) | $w_i$ | $w_i M_i$ (g/mol) |
| ---: | ---: | ---: |
| 2 500 | 0.02 | 50 |
| 7 500 | 0.12 | 900 |
| 12 500 | 0.32 | 4 000 |
| 17 500 | 0.32 | 5 600 |
| 22 500 | 0.22 | 4 950 |

$$M_w = 50 + 900 + 4000 + 5600 + 4950 = \mathbf{15\,500\ g/mol}$$

### 2. b) Polydispersity [Session 19 Slide 13]
$$I = \frac{M_w}{M_n} = \frac{15\,500\ \text{g/mol}}{12\,880\ \text{g/mol}} = \mathbf{1.203}$$

### 3. c) Value of X [Session 19 Slide 12]
Molecular weight of the repeat unit from the degree of polymerization:

$$M_0 = \frac{M_n}{X_n} = \frac{12\,880\ \text{g/mol}}{230} = 56.0\ \text{g/mol}$$

Atoms of the drawn unit: carbon, $1\ (\mathrm{CH_2}) + 1\ (\mathrm{CH}) + X\ (\mathrm{CH_2}\ \text{groups}) + 1\ (\mathrm{CH_3}) = X + 3$; hydrogen, $2 + 1 + 2X + 3 = 2X + 6$. The unit is $\mathrm{C}_{X+3}\mathrm{H}_{2X+6}$, that is $\mathrm{C}_n\mathrm{H}_{2n}$ with $n = X + 3$, an alkene formula as the statement says. Its molecular weight:

$$M_0 = 12(X + 3) + 1(2X + 6) = 14X + 42\ \text{g/mol}$$

Setting it equal to 56.0 g/mol:

$$14X + 42 = 56 \ \Rightarrow\ 14X = 14 \ \Rightarrow\ \mathbf{X = 1}$$

The repeat unit is $\mathrm{-CH_2{-}CH(CH_2CH_3)-}$, $\mathrm{C_4H_8}$ (56 g/mol): a vinyl polymer with an ethyl side group, the polymer of 1-butene, usually called poly(1-butene) or polybutene (the name is an extension; it is not on the slides).

### 4. d) Crystallinity compared with polyethylene [Session 19 Slides 26-27]
Polyethylene, $\mathrm{-[CH_2{-}CH_2]_n-}$, is the example of a simple, symmetric monomer that crystallizes easily (Slide 27). This polymer has an ethyl side group on every second carbon:
- the side group is bulkier and makes the unit more complex, and complex monomeric structures lower the degree of crystallinity (Slide 26);
- the CH carbon carries two different groups, so the polymer can be atactic, and atactic polymers are amorphous (Slide 26); only an isotactic or syndiotactic grade could crystallize, and still with more difficulty than PE.

**Answer: lower than polyethylene.**

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $w_i$ is dimensionless, so $M_w$ is in g/mol; $I$ and $X_n$ are pure numbers; $M_0 = M_n/X_n$ is in g/mol.
- **$M_w \ge M_n$.** $15\,500 > 12\,880$ g/mol, so $I = 1.203 > 1$, as it must be for a polymer with a distribution of lengths.
- **Back-substitution.** $230\times56\ \text{g/mol} = 12\,880$ g/mol, exactly the given $M_n$.
- **Limit.** $X = 0$ would give $\mathrm{C_3H_6}$ (42 g/mol), polypropylene; each extra $\mathrm{CH_2}$ adds 14 g/mol, so only $X = 1$ matches 56 g/mol.

### Interpretation
The data describe a moderately polydisperse polymer ($I = 1.2$) of about 230 units per chain, whose unit is polypropylene with one more $\mathrm{CH_2}$ in the side group. The longer side group makes the chain less regular than polyethylene and polypropylene, so it packs less well and is less crystalline, which also means a lower density, stiffness and melting point than polyethylene of similar chain length.

> [!warning] Discrepancy with the official solution
> The key gives "X = 1, polybutadiene". The value $X = 1$ agrees, but the drawn unit with $X = 1$ is $\mathrm{C_4H_8}$, a saturated unit with an ethyl side group (the polymer of 1-butene), not polybutadiene. Polybutadiene is made from 1,3-butadiene, $\mathrm{CH_2{=}CH{-}CH{=}CH_2}$ [Session 20 Slide 15]; its repeat unit keeps one double bond, $\mathrm{C_4H_6}$ = 54 g/mol, does not follow the $\mathrm{C}_n\mathrm{H}_{2n}$ formula of the statement, and $230\times54 = 12\,420$ g/mol does not give the stated $M_n = 12\,880$ g/mol. The name in the key is therefore not consistent with the statement; the computed polymer is the polymer of 1-butene.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) $M_w$ | 15 500 g/mol | 15 500 g/mol | agrees |
| b) PDI | 1.2 | 1.203 | agrees |
| c) $X$ | 1, polybutadiene | 1, unit $\mathrm{C_4H_8}$ (polymer of 1-butene) | $X$ agrees; the name does not (see the warning) |
| d) Crystallinity | lower | lower than PE | agrees |

## 🔗 Related Links
* [[Topic 9 - Polymers]]
* [[Problem - T9-08 Number and Weight Averages and Monomer of an Unknown Polymer|Problem T9-08]]
