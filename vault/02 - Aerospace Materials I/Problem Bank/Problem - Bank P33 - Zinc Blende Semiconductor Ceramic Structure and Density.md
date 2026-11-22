---
materia: Aerospace Materials I
tema: "Unit 8: ceramic crystal structures"
bank_id: P33
title: "Zinc blende semiconductor ceramic structure and density"
category: mt3_problem
archetype: ceramic-structure
level: standard
unit: 8
difficulty: 2
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of Problems T8 (problem 1) and the final of June 2014 (question 1); not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - ceramic-structure
  - zinc-blende
  - semiconductor
  - density
---

# Bank P33 — Zinc blende semiconductor ceramic structure and density

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Problems T8 (problem 1) and the final of June 2014 (question 1). Method: Session 16, Slides 6 and 9 (cell-geometry relations and density formula marked as extension from Topic 2). Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

Zinc selenide ($\text{ZnSe}$) is an II–VI semiconductor ceramic used in infrared optical windows and laser optics. Using the effective tetrahedral radii $r(\text{Zn}^{2+}) = 0.060\ \text{nm}$ and $r(\text{Se}^{2-}) = 0.184\ \text{nm}$, atomic masses $M(\text{Zn}) = 65.38\ \text{g/mol}$ and $M(\text{Se}) = 78.96\ \text{g/mol}$, and Avogadro's constant $N_A = 6.022\times10^{23}\ \text{mol}^{-1}$:

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Cation radius ($\text{Zn}^{2+}$) | $r_C$ | 0.060 nm | $6.0\times10^{-11}$ m |
| Anion radius ($\text{Se}^{2-}$) | $r_A$ | 0.184 nm | $1.84\times10^{-10}$ m |
| Atomic mass of Zn | $M_{\text{Zn}}$ | 65.38 g/mol | $65.38\times10^{-3}$ kg/mol |
| Atomic mass of Se | $M_{\text{Se}}$ | 78.96 g/mol | $78.96\times10^{-3}$ kg/mol |
| Avogadro's constant | $N_A$ | $6.022\times10^{23}\ \text{mol}^{-1}$ | $6.022\times10^{23}\ \text{mol}^{-1}$ |

Unit conversions: $1\ \text{nm} = 10^{-6}\ \text{mm}$; $1\ \text{nm}^2 = 10^{-12}\ \text{mm}^2$; $1\ \text{nm}^3 = 10^{-21}\ \text{cm}^3 = 10^{-27}\ \text{m}^3$; $1\ \text{g/cm}^3 = 1000\ \text{kg/m}^3$.

#### Model

- **Radius-ratio rule:** $0.225 \le r_C/r_A \le 0.414$ predicts tetrahedral coordination ($\text{C.I.} = 4$) and the zinc blende ($\text{ZnS}$) structure [Session 16, Slide 6].
- **Zinc blende ($\text{ZnS}$) unit cell:** anions form an FCC lattice and cations fill **half** of the tetrahedral interstitial sites, giving $4\ \text{Zn}^{2+}$ and $4\ \text{Se}^{2-}$ per unit cell and $\text{C.I.} = 4$ for both ions [Session 16, Slide 9].
- **Tetrahedral contact (extension):** the occupied tetrahedral site at $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ touches the corner anion at $(0,0,0)$ along the body diagonal, so $\frac{\sqrt{3}}{4}a = r_C + r_A$.
- **APF, density, and directional/planar densities (extension from Topic 2):** $\text{APF} = 4(V_C + V_A)/V$, $\rho = 4(M_{\text{Zn}} + M_{\text{Se}})/(V N_A)$, $\rho_L[111] = N_{[111]}/L_{[111]}$, and $\rho_P(111) = N_{(111)}/A_{(111)}$.

## (a) Predict the coordination index from $r_C/r_A$, identify the crystal structure and lattice sites, and justify the stoichiometry. [1.0 pts]

### Hint

Compute $r(\text{Zn}^{2+})/r(\text{Se}^{2-})$ and check the tetrahedral window $0.225\text{–}0.414$ in Session 16, Slide 6. Recall that only half of the eight tetrahedral holes of the FCC anion sublattice are occupied in zinc blende.

### Checkpoint

- $r_C/r_A = 0.3261 \in [0.225, 0.414]$: tetrahedral coordination, $\text{C.I.} = 4$ for both ions
- **Structure:** zinc blende ($\text{ZnS}$ type); $\text{Se}^{2-}$ on FCC ($4\ \text{ions/cell}$), $\text{Zn}^{2+}$ in half of the 8 tetrahedral sites ($4\ \text{ions/cell}$)
- **Stoichiometry:** $\text{Zn}_4\text{Se}_4 \to \text{ZnSe}$ ($1:1$, $4$ formula units per cell)

### Solution

#### Radius ratio and coordination index

Dividing the cation radius by the anion radius [Session 16, Slide 6]:

$$\frac{r_C}{r_A} = \frac{r(\text{Zn}^{2+})}{r(\text{Se}^{2-})} = \frac{0.060\ \text{nm}}{0.184\ \text{nm}} = 0.3261$$

Because $0.225 \le 0.3261 \le 0.414$, each $\text{Zn}^{2+}$ cation sits inside a regular tetrahedron of 4 $\text{Se}^{2-}$ anions ($\text{C.I.} = 4$), which gives the **zinc blende ($\text{ZnS}$) structure** [Session 16, Slides 6 and 9]. By $1:1$ stoichiometry, each $\text{Se}^{2-}$ anion is likewise tetrahedrally coordinated to 4 $\text{Zn}^{2+}$ cations ($\text{C.I.} = 4$).

#### Ion positions and unit cell stoichiometry

In the zinc blende unit cell [Session 16, Slide 9]:
- **$\text{Se}^{2-}$ anions** occupy the **FCC lattice points** (8 corners and 6 face centres):

$$n_{\text{Se}^{2-}} = 8\times\frac{1}{8} + 6\times\frac{1}{2} = 1 + 3 = 4\ \text{anions/cell}$$

- **$\text{Zn}^{2+}$ cations** occupy **half (4 out of 8) of the tetrahedral interstitial sites** (specifically, the four non-adjacent sites $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$, $(\frac{1}{4},\frac{3}{4},\frac{3}{4})$, $(\frac{3}{4},\frac{1}{4},\frac{3}{4})$, and $(\frac{3}{4},\frac{3}{4},\frac{1}{4})$, all completely inside the cell):

$$n_{\text{Zn}^{2+}} = 4\times 1 = 4\ \text{cations/cell}$$

Therefore the cell holds $4\ \text{Zn}^{2+}$ and $4\ \text{Se}^{2-}$ ions, i.e. **4 $\text{ZnSe}$ formula units** ($1:1$ stoichiometry) with net charge $4(+2) + 4(-2) = 0$.

## (b) Derive the lattice parameter $a$, check anion–anion non-overlap, and calculate the cell volume $V$ and the atomic packing factor (APF). [1.5 pts]

### Hint

The occupied tetrahedral site at $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ touches the anion at $(0,0,0)$ along the body diagonal, so $\frac{\sqrt{3}}{4}a = r_C + r_A$. Check that nearest anions along the face diagonal satisfy $a\sqrt{2}/2 > 2r_A$.

### Checkpoint

- $a = 0.5635\ \text{nm}$ ($a\sqrt{2}/2 = 0.3985\ \text{nm} > 2r_A = 0.3680\ \text{nm}$, no overlap)
- $V = 0.1789\ \text{nm}^3 = 1.789\times10^{-22}\ \text{cm}^3 = 1.789\times10^{-28}\ \text{m}^3$
- $\text{APF} = 0.6036$ ($60.4\%$)

### Solution

#### Lattice parameter from tetrahedral contact

The tetrahedral site $(\frac{1}{4}a,\frac{1}{4}a,\frac{1}{4}a)$ lies one quarter of the body diagonal from $(0,0,0)$ (**extension** of Session 16, Slide 9):

$$\frac{\sqrt{3}}{4}\,a = r_C + r_A$$

Multiplying both sides by $4$ and dividing by $\sqrt{3}$ gives:

$$a = \frac{4(r_C + r_A)}{\sqrt{3}} = \frac{4\times(0.060\ \text{nm} + 0.184\ \text{nm})}{1.73205} = \frac{0.976\ \text{nm}}{1.73205} = 0.5635\ \text{nm}$$

#### Anion–anion non-overlap check

The closest $\text{Se}^{2-}$ ions sit half a face diagonal apart:

$$d_{\text{Se–Se}} = \frac{a\sqrt{2}}{2} = \frac{0.5635\ \text{nm}\times 1.4142}{2} = 0.3985\ \text{nm}$$

Because $0.3985\ \text{nm} > 2r_A = 2\times 0.184\ \text{nm} = 0.3680\ \text{nm}$, the anions do not touch or overlap.

#### Unit cell volume

$$V = a^3 = (0.56349\ \text{nm})^3 = 0.17892\ \text{nm}^3 \approx 0.1789\ \text{nm}^3$$

Converting to $\text{cm}^3$ ($1\ \text{nm}^3 = 10^{-21}\ \text{cm}^3$) and $\text{m}^3$ ($1\ \text{nm}^3 = 10^{-27}\ \text{m}^3$):

$$V = 1.789\times10^{-22}\ \text{cm}^3 = 1.789\times10^{-28}\ \text{m}^3$$

#### Atomic packing factor (APF)

Volume of one $\text{Zn}^{2+}$ sphere and one $\text{Se}^{2-}$ sphere:

$$V_{\text{Zn}^{2+}} = \frac{4}{3}\pi(0.060\ \text{nm})^3 = 9.048\times10^{-4}\ \text{nm}^3$$

$$V_{\text{Se}^{2-}} = \frac{4}{3}\pi(0.184\ \text{nm})^3 = 2.6096\times10^{-2}\ \text{nm}^3$$

Summing the 4 cations and 4 anions per cell and dividing by $V$:

$$V_{\text{ions}} = 4\,(9.0478\times10^{-4} + 2.6096\times10^{-2})\ \text{nm}^3 = 4\times 0.027001\ \text{nm}^3 = 0.10800\ \text{nm}^3$$

$$\text{APF} = \frac{V_{\text{ions}}}{V} = \frac{0.10800\ \text{nm}^3}{0.17892\ \text{nm}^3} = 0.6036$$

## (c) Calculate the theoretical volumetric density $\rho$ in $\text{g/cm}^3$ and $\text{kg/m}^3$. [1.0 pts]

### Hint

Compute the mass of the 4 $\text{ZnSe}$ formula units in one cell using $M_{\text{ZnSe}} = M_{\text{Zn}} + M_{\text{Se}}$ and divide by $V$ in $\text{cm}^3$.

### Checkpoint

- $M_{\text{ZnSe}} = 144.34\ \text{g/mol}$, $m_{\text{cell}} = 9.588\times10^{-22}\ \text{g}$
- $\rho = 5.358\ \text{g/cm}^3 = 5358\ \text{kg/m}^3$

### Solution

#### Mass of one unit cell

With $M_{\text{ZnSe}} = 65.38 + 78.96 = 144.34\ \text{g/mol}$ and $n_{\text{cell}} = 4$ formula units per cell:

$$m_{\text{cell}} = \frac{4\,(M_{\text{Zn}} + M_{\text{Se}})}{N_A} = \frac{4\times 144.34\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = \frac{577.36\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = 9.5875\times10^{-22}\ \text{g} \approx 9.588\times10^{-22}\ \text{g}$$

#### Theoretical volumetric density

$$\rho = \frac{m_{\text{cell}}}{V} = \frac{9.5875\times10^{-22}\ \text{g}}{1.7892\times10^{-22}\ \text{cm}^3} = 5.358\ \text{g/cm}^3 = 5358\ \text{kg/m}^3$$

## (d) Determine the linear ionic density along $[111]$ and the planar ionic density on $(111)$, stating the exact ion counts by species. [1.5 pts]

### Hint

In zinc blende, only ONE of the two sites $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ and $(\frac{3}{4},\frac{3}{4},\frac{3}{4})$ along the $[111]$ body diagonal is occupied by $\text{Zn}^{2+}$! On the $(111)$ triangle $x + y + z = 1$, check whether any $\text{Zn}^{2+}$ tetrahedral coordinates satisfy $x + y + z = 1$.

### Checkpoint

- $[111]$: length $a\sqrt{3} = 0.9760\ \text{nm}$; $1\ \text{Se}^{2-} + 1\ \text{Zn}^{2+} = 2$ ions; $\rho_L[111] = 2.049\ \text{ions/nm} = 2.049\times10^{6}\ \text{ions/mm}$
- $(111)$: triangle area $\frac{\sqrt{3}}{2}a^2 = 0.2750\ \text{nm}^2$; $2\ \text{Se}^{2-} + 0\ \text{Zn}^{2+} = 2$ ions; $\rho_P(111) = 7.273\ \text{ions/nm}^2 = 7.273\times10^{12}\ \text{ions/mm}^2$

### Solution

#### Linear ionic density along $[111]$

The $[111]$ body diagonal runs from $(0,0,0)$ to $(1,1,1)$ with length

$$L_{[111]} = a\sqrt{3} = 0.56349\ \text{nm}\times 1.73205 = 0.9760\ \text{nm}$$

Along the line $x = y = z$ with $0 \le x \le 1$:
- **$\text{Se}^{2-}$ anions:** occupy both corners $(0,0,0)$ and $(1,1,1)$, each shared between two collinear cells ($2\times\frac{1}{2} = 1\ \text{Se}^{2-}$ ion).
- **$\text{Zn}^{2+}$ cations:** of the two tetrahedral positions on the body diagonal, $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ is occupied ($1\ \text{Zn}^{2+}$ ion), while $(\frac{3}{4},\frac{3}{4},\frac{3}{4})$ belongs to the empty half of the tetrahedral sites!

Hence $N_{[111]} = 1\ \text{Se}^{2-} + 1\ \text{Zn}^{2+} = 2\ \text{ions}$, and

$$\rho_L[111] = \frac{N_{[111]}}{L_{[111]}} = \frac{2\ \text{ions}}{0.9760\ \text{nm}} = 2.0492\ \text{ions/nm} \approx 2.049\ \text{ions/nm}$$

Converting with $1\ \text{mm} = 10^{6}\ \text{nm}$:

$$\rho_L[111] = 2.0492\times10^{6}\ \text{ions/mm} \approx 2.049\times10^{6}\ \text{ions/mm}$$

#### Planar ionic density on $(111)$

The $(111)$ plane $x + y + z = 1$ cuts the cube in an equilateral triangle with vertices $(1,0,0)$, $(0,1,0)$, and $(0,0,1)$ of side $s = a\sqrt{2}$ and area:

$$A_{(111)} = \frac{\sqrt{3}}{4}(a\sqrt{2})^2 = \frac{\sqrt{3}}{2}a^2 = 0.86603\times(0.56349\ \text{nm})^2 = 0.27499\ \text{nm}^2 \approx 0.2750\ \text{nm}^2$$

Counting the ions satisfying $x + y + z = 1$:
- **$\text{Se}^{2-}$ anions:** 3 corners ($3\times\frac{1}{6} = \frac{1}{2}$) plus 3 face centres on the triangle edges ($3\times\frac{1}{2} = \frac{3}{2}$), giving $n_{\text{Se}^{2-}} = 2\ \text{Se}^{2-}$ ions.
- **$\text{Zn}^{2+}$ cations:** the four occupied tetrahedral sites have coordinate sums $x + y + z = \frac{3}{4}$ (at $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$) or $\frac{7}{4}$ (at $(\frac{1}{4},\frac{3}{4},\frac{3}{4})$, $(\frac{3}{4},\frac{1}{4},\frac{3}{4})$, and $(\frac{3}{4},\frac{3}{4},\frac{1}{4})$), never $1$. So **0 $\text{Zn}^{2+}$ ions** lie on this $(111)$ plane.

Thus $N_{(111)} = 2\ \text{Se}^{2-} + 0\ \text{Zn}^{2+} = 2\ \text{ions}$, and

$$\rho_P(111) = \frac{N_{(111)}}{A_{(111)}} = \frac{2\ \text{ions}}{0.27499\ \text{nm}^2} = 7.273\ \text{ions/nm}^2 = 7.273\times10^{12}\ \text{ions/mm}^2$$

## Interpretation

- **Physical check:** the calculated parameter $a = 0.5635\ \text{nm}$ and density $\rho = 5.358\ \text{g/cm}^3$ are very close to the measured values of zinc-blende $\text{ZnSe}$ ($a = 0.5668\ \text{nm}$, $\rho = 5.27\ \text{g/cm}^3$; **extension**).
- **Open structure and low APF:** $\text{APF} = 0.604$ is substantially lower than the $0.74$ of a close-packed FCC metal because the four small $\text{Zn}^{2+}$ ions fill only half of the tetrahedral holes, leaving the other four tetrahedral sites and all octahedral sites empty.
- **SI dimensional check:** $[a] = \text{m}$; $[V] = \text{m}^3$; $[\rho] = \text{kg/m}^3$; $[\rho_L] = \text{m}^{-1}$; $[\rho_P] = \text{m}^{-2}$; $[\text{APF}]$ dimensionless.
- **Common mistake:** putting $\text{Zn}^{2+}$ at both $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ and $(\frac{3}{4},\frac{3}{4},\frac{3}{4})$ along $[111]$ (counting 3 ions instead of 2 — only half of the tetrahedral sites are occupied in zinc blende!), or taking $a\sqrt{2} = 4r_{\text{Se}}$ instead of $\frac{\sqrt{3}}{4}a = r_C + r_A$.

## Verification

- r_C / r_A | 0.060/0.184 | 0.3261
- a (nm) | 4*(0.060+0.184)/sqrt(3) | 0.5635
- d_Se-Se (nm) | 4*(0.060+0.184)/sqrt(3)*sqrt(2)/2 | 0.3985
- 2*r_A (nm) | 2*0.184 | 0.3680
- V (nm^3) | (4*(0.060+0.184)/sqrt(3))**3 | 0.1789
- V (cm^3) | (4*(0.060+0.184)/sqrt(3))**3*1e-21 | 1.789e-22
- V (m^3) | (4*(0.060+0.184)/sqrt(3))**3*1e-27 | 1.789e-28
- V_Zn (nm^3) | 4/3*pi*0.060**3 | 9.048e-4
- V_Se (nm^3) | 4/3*pi*0.184**3 | 2.6096e-2
- V_ions (nm^3) | 4*(4/3*pi*(0.060**3+0.184**3)) | 0.10800
- APF | 4*(4/3*pi*(0.060**3+0.184**3))/((4*(0.060+0.184)/sqrt(3))**3) | 0.6036
- m_cell (g) | 4*(65.38+78.96)/N_A | 9.588e-22
- rho (g/cm^3) | (4*(65.38+78.96)/N_A)/((4*(0.060+0.184)/sqrt(3))**3*1e-21) | 5.358
- rho (kg/m^3) | (4*(65.38+78.96)/N_A)/((4*(0.060+0.184)/sqrt(3))**3*1e-21)*1000 | 5358
- L_111 (nm) | 4*(0.060+0.184) | 0.9760
- rho_L[111] (ions/nm) | 2/(4*(0.060+0.184)) | 2.049
- rho_L[111] (ions/mm) | 2/(4*(0.060+0.184))*1e6 | 2.049e6
- A_111 (nm^2) | sqrt(3)/2*(4*(0.060+0.184)/sqrt(3))**2 | 0.2750
- rho_P(111) (ions/nm^2) | 2/(sqrt(3)/2*(4*(0.060+0.184)/sqrt(3))**2) | 7.273
- rho_P(111) (ions/mm^2) | 2/(sqrt(3)/2*(4*(0.060+0.184)/sqrt(3))**2)*1e12 | 7.273e12

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
