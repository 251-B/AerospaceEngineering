---
materia: Aerospace Materials I
tema: "Unit 8: ceramic crystal structures"
bank_id: P31
title: "MgO rock salt unit cell, APF and ionic densities"
category: mt3_problem
archetype: ceramic-structure
level: standard
unit: 8
difficulty: 2
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of Problems T8 (problem 7) and the final of January 2013 (question 6); not an official exercise. Radii and atomic masses are standard crystallographic values. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - ceramic-structure
  - rock-salt
  - density
  - packing-factor
---

# Bank P31 — MgO rock salt unit cell, APF and ionic densities

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Problems T8 (problem 7) and the final of January 2013 (question 6). Method: Session 16, Slides 6 and 8 (cell-geometry relations and density formula marked as extension from Topic 2). Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

Magnesium oxide ($\text{MgO}$) is a refractory ionic ceramic used in high-temperature furnace linings and thermal insulation. Take the ionic radii as $r(\text{Mg}^{2+}) = 0.072\ \text{nm}$ and $r(\text{O}^{2-}) = 0.140\ \text{nm}$, the atomic masses as $M(\text{Mg}) = 24.31\ \text{g/mol}$ and $M(\text{O}) = 16.00\ \text{g/mol}$, and Avogadro's constant as $N_A = 6.022\times10^{23}\ \text{mol}^{-1}$.

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Cation radius ($\text{Mg}^{2+}$) | $r_C$ | 0.072 nm | $7.2\times10^{-11}$ m |
| Anion radius ($\text{O}^{2-}$) | $r_A$ | 0.140 nm | $1.40\times10^{-10}$ m |
| Atomic mass of Mg | $M_{\text{Mg}}$ | 24.31 g/mol | $24.31\times10^{-3}$ kg/mol |
| Atomic mass of O | $M_{\text{O}}$ | 16.00 g/mol | $16.00\times10^{-3}$ kg/mol |
| Avogadro's constant | $N_A$ | $6.022\times10^{23}\ \text{mol}^{-1}$ | $6.022\times10^{23}\ \text{mol}^{-1}$ |

Unit conversions: $1\ \text{nm} = 10^{-9}\ \text{m} = 10^{-7}\ \text{cm} = 10^{-6}\ \text{mm}$; $1\ \text{nm}^2 = 10^{-12}\ \text{mm}^2$; $1\ \text{nm}^3 = 10^{-21}\ \text{cm}^3 = 10^{-27}\ \text{m}^3$; $1\ \text{g/cm}^3 = 1000\ \text{kg/m}^3$.

#### Model

- **Radius-ratio stability rule:** for $0.414 \le r_C/r_A \le 0.732$, each cation is coordinated to 6 anions at the corners of an octahedron ($\text{C.I.} = 6$), corresponding to the rock salt ($\text{NaCl}$) structure [Session 16, Slide 6].
- **Rock salt ($\text{NaCl}$) unit cell:** anions form an FCC lattice and cations fill all octahedral interstitial sites, giving $4\ \text{Mg}^{2+}$ and $4\ \text{O}^{2-}$ per cubic unit cell [Session 16, Slide 8].
- **Hard-sphere contact along the cube edge (extension):** cation and anion touch along the $[100]$ edge, $a = 2(r_C + r_A)$, provided the anions do not overlap along the face diagonal ($a\sqrt{2}/2 > 2r_A$).
- **Atomic packing factor and density (extension from Topic 2):** $\text{APF} = V_{\text{ions}}/V_{\text{cell}}$ and $\rho = n_{\text{cell}} M_{\text{MgO}}/(V_{\text{cell}} N_A)$.
- **Linear and planar ionic densities (extension from Topic 2):** $\rho_L[111] = N_{[111]}/L_{[111]}$ and $\rho_P(111) = N_{(111)}/A_{(111)}$, counting only ions whose centres lie on the line or plane.

## (a) Predict the coordination index from $r_C/r_A$, identify the crystal structure and ion positions, and justify the stoichiometry per unit cell. [1.0 pts]

### Hint

Compute $r(\text{Mg}^{2+})/r(\text{O}^{2-})$ and locate it in the radius-ratio table of Session 16, Slide 6. Then count the lattice points and octahedral sites belonging to one cubic cell.

### Checkpoint

- $r_C/r_A = 0.5143 \in [0.414, 0.732]$: octahedral coordination, $\text{C.I.} = 6$ for both ions
- Crystal structure: rock salt ($\text{NaCl}$ type)
- Counts per cell: $4\ \text{O}^{2-}$ (FCC) and $4\ \text{Mg}^{2+}$ (all octahedral sites), giving $4\ \text{MgO}$ formula units ($1:1$)

### Solution

#### Radius ratio and coordination index

Dividing the cation radius by the anion radius [Session 16, Slide 6]:

$$\frac{r_C}{r_A} = \frac{r(\text{Mg}^{2+})}{r(\text{O}^{2-})} = \frac{0.072\ \text{nm}}{0.140\ \text{nm}} = 0.5143$$

Because $0.414 \le 0.5143 \le 0.732$, each $\text{Mg}^{2+}$ ion is surrounded by **6** $\text{O}^{2-}$ anions at the corners of a regular octahedron ($\text{C.I.} = 6$), which stabilizes the **rock salt ($\text{NaCl}$) structure** [Session 16, Slides 6 and 8]. By $1:1$ stoichiometry and electroneutrality, each $\text{O}^{2-}$ is likewise surrounded by 6 $\text{Mg}^{2+}$ cations ($\text{C.I.} = 6$).

#### Lattice sites and stoichiometry per unit cell

In the rock salt unit cell [Session 16, Slide 8]:
- **$\text{O}^{2-}$ anions** occupy the **FCC lattice points** (8 corners, each shared by 8 cells, plus 6 face centres, each shared by 2 cells):

$$n_{\text{O}^{2-}} = 8\times\frac{1}{8} + 6\times\frac{1}{2} = 1 + 3 = 4\ \text{anions/cell}$$

- **$\text{Mg}^{2+}$ cations** occupy **all octahedral interstitial sites** (12 edge midpoints, each shared by 4 cells, plus 1 body centre fully inside the cell):

$$n_{\text{Mg}^{2+}} = 12\times\frac{1}{4} + 1\times 1 = 3 + 1 = 4\ \text{cations/cell}$$

Thus the unit cell contains $4\ \text{Mg}^{2+}$ and $4\ \text{O}^{2-}$ ions, i.e. **4 formula units of $\text{MgO}$** ($1:1$ stoichiometry), and total charge $4(+2) + 4(-2) = 0$ (electroneutrality satisfied).

## (b) Determine the lattice parameter $a$, verify that anions do not overlap, and compute the unit cell volume $V$ and the atomic packing factor (APF). [1.5 pts]

### Hint

Along a cube edge of rock salt, a corner anion touches an edge-centre cation, which touches the next corner anion. Check that the nearest $\text{O}^{2-}$–$\text{O}^{2-}$ spacing along the face diagonal exceeds $2r_A$.

### Checkpoint

- $a = 0.4240\ \text{nm}$ ($a\sqrt{2}/2 = 0.2998\ \text{nm} > 2r_A = 0.2800\ \text{nm}$, no overlap)
- $V = 0.07623\ \text{nm}^3 = 7.623\times10^{-23}\ \text{cm}^3 = 7.623\times10^{-29}\ \text{m}^3$
- $\text{APF} = 0.6852$ ($68.5\%$)

### Solution

#### Lattice parameter from edge contact

Along any $\langle 100\rangle$ cube edge, the sequence is $\text{O}^{2-}$ (corner) – $\text{Mg}^{2+}$ (edge midpoint) – $\text{O}^{2-}$ (corner). Because cation and anion touch along the edge (**extension** of Session 16, Slide 8):

$$a = 2(r_C + r_A) = 2\times(0.072\ \text{nm} + 0.140\ \text{nm}) = 2\times 0.212\ \text{nm} = 0.4240\ \text{nm}$$

#### Anion–anion non-overlap check

The closest $\text{O}^{2-}$ neighbours sit at a corner and an adjacent face centre, separated by half a face diagonal:

$$d_{\text{O–O}} = \frac{a\sqrt{2}}{2} = \frac{0.4240\ \text{nm}\times 1.4142}{2} = 0.2998\ \text{nm}$$

Comparing with twice the anion radius, $2r_A = 2\times 0.140\ \text{nm} = 0.2800\ \text{nm}$: since $0.2998\ \text{nm} > 0.2800\ \text{nm}$, the anions do not touch or overlap, confirming that the cation–anion contact sets $a$.

#### Unit cell volume

Cubing the lattice parameter $a$:

$$V = a^3 = (0.4240\ \text{nm})^3 = 0.076225\ \text{nm}^3 \approx 0.07623\ \text{nm}^3$$

Converting to $\text{cm}^3$ ($1\ \text{nm}^3 = 10^{-21}\ \text{cm}^3$) and to SI $\text{m}^3$ ($1\ \text{nm}^3 = 10^{-27}\ \text{m}^3$):

$$V = 0.076225\times10^{-21}\ \text{cm}^3 = 7.623\times10^{-23}\ \text{cm}^3 = 7.623\times10^{-29}\ \text{m}^3$$

#### Atomic packing factor (APF)

Modelling the 4 $\text{Mg}^{2+}$ and 4 $\text{O}^{2-}$ ions as spheres of volume $V_{\text{sphere}} = \frac{4}{3}\pi r^3$:

$$V_{\text{Mg}^{2+}} = \frac{4}{3}\pi(0.072\ \text{nm})^3 = \frac{4}{3}\pi(3.7325\times10^{-4}\ \text{nm}^3) = 1.563\times10^{-3}\ \text{nm}^3$$

$$V_{\text{O}^{2-}} = \frac{4}{3}\pi(0.140\ \text{nm})^3 = \frac{4}{3}\pi(2.7440\times10^{-3}\ \text{nm}^3) = 1.1494\times10^{-2}\ \text{nm}^3$$

Summing over the 4 cations and 4 anions in the cell:

$$V_{\text{ions}} = 4\left(1.5635\times10^{-3} + 1.1494\times10^{-2}\right)\ \text{nm}^3 = 4\times 0.013058\ \text{nm}^3 = 0.05223\ \text{nm}^3$$

Dividing by the cell volume $V$:

$$\text{APF} = \frac{V_{\text{ions}}}{V} = \frac{0.05223\ \text{nm}^3}{0.076225\ \text{nm}^3} = 0.6852$$

So $68.5\%$ of the unit cell volume is occupied by ionic spheres.

## (c) Calculate the theoretical volumetric density $\rho$ in $\text{g/cm}^3$ and $\text{kg/m}^3$. [1.0 pts]

### Hint

Compute the mass of the 4 $\text{MgO}$ formula units inside one unit cell by dividing $4(M_{\text{Mg}} + M_{\text{O}})$ by $N_A$, then divide by $V$.

### Checkpoint

- $M_{\text{MgO}} = 40.31\ \text{g/mol}$, $m_{\text{cell}} = 2.678\times10^{-22}\ \text{g}$
- $\rho = 3.513\ \text{g/cm}^3 = 3513\ \text{kg/m}^3$

### Solution

#### Mass of one unit cell

The molar mass of one formula unit of $\text{MgO}$ is $M_{\text{MgO}} = 24.31 + 16.00 = 40.31\ \text{g/mol}$. With $n_{\text{cell}} = 4$ formula units per cell:

$$m_{\text{cell}} = \frac{4\,(M_{\text{Mg}} + M_{\text{O}})}{N_A} = \frac{4\times 40.31\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = \frac{161.24\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = 2.6775\times10^{-22}\ \text{g} \approx 2.678\times10^{-22}\ \text{g}$$

#### Theoretical volumetric density

Dividing the cell mass by the cell volume $V = 7.6225\times10^{-23}\ \text{cm}^3$:

$$\rho = \frac{m_{\text{cell}}}{V} = \frac{2.6775\times10^{-22}\ \text{g}}{7.6225\times10^{-23}\ \text{cm}^3} = 3.5126\ \text{g/cm}^3 \approx 3.513\ \text{g/cm}^3$$

Converting to SI units ($1\ \text{g/cm}^3 = 10^{-3}\ \text{kg} / 10^{-6}\ \text{m}^3 = 1000\ \text{kg/m}^3$):

$$\rho = 3.5126\times1000\ \text{kg/m}^3 = 3513\ \text{kg/m}^3$$

## (d) Determine the linear ionic density along $[111]$ and the planar ionic density on $(111)$, stating the exact ion counts by species. [1.5 pts]

### Hint

The $[111]$ direction runs along the body diagonal from $(0,0,0)$ to $(1,1,1)$. The $(111)$ plane passes through $(1,0,0)$, $(0,1,0)$, and $(0,0,1)$ with equation $x + y + z = 1$; check which ions satisfy $x = y = z$ and $x + y + z = 1$.

### Checkpoint

- $[111]$: length $a\sqrt{3} = 0.7344\ \text{nm}$; $1\ \text{O}^{2-} + 1\ \text{Mg}^{2+} = 2$ ions; $\rho_L[111] = 2.723\ \text{ions/nm} = 2.723\times10^{6}\ \text{ions/mm}$
- $(111)$: triangle area $\frac{\sqrt{3}}{2}a^2 = 0.1557\ \text{nm}^2$; $2\ \text{O}^{2-} + 0\ \text{Mg}^{2+} = 2$ ions; $\rho_P(111) = 12.85\ \text{ions/nm}^2 = 1.285\times10^{13}\ \text{ions/mm}^2$

### Solution

#### Linear ionic density along $[111]$

The $[111]$ vector across one unit cell is the body diagonal joining $(0,0,0)$ to $(1,1,1)$, whose length is

$$L_{[111]} = a\sqrt{3} = 0.4240\ \text{nm}\times 1.73205 = 0.7344\ \text{nm}$$

Along the line $x = y = z$ with $0 \le x \le 1$:
- **$\text{O}^{2-}$ ions:** sit at the two corners $(0,0,0)$ and $(1,1,1)$, each shared equally with the adjacent segment along $[111]$, contributing $2\times\frac{1}{2} = 1\ \text{O}^{2-}$ ion. None of the FCC face centres lie on $x = y = z$ (each has one coordinate equal to $0$ or $1$ and two equal to $\frac{1}{2}$).
- **$\text{Mg}^{2+}$ ions:** the body-centre cation at $(\frac{1}{2},\frac{1}{2},\frac{1}{2})$ lies strictly inside the segment, contributing $1\ \text{Mg}^{2+}$ ion. None of the edge midpoints lie on $x = y = z$ (each has two coordinates in $\{0,1\}$ and one equal to $\frac{1}{2}$).

Total ions on the $[111]$ cell diagonal: $N_{[111]} = 1\ \text{O}^{2-} + 1\ \text{Mg}^{2+} = 2\ \text{ions}$. Therefore:

$$\rho_L[111] = \frac{N_{[111]}}{L_{[111]}} = \frac{2\ \text{ions}}{0.7344\ \text{nm}} = 2.723\ \text{ions/nm}$$

Converting with $1\ \text{mm} = 10^{6}\ \text{nm}$:

$$\rho_L[111] = 2.723\ \frac{\text{ions}}{\text{nm}}\times\frac{10^{6}\ \text{nm}}{1\ \text{mm}} = 2.723\times10^{6}\ \text{ions/mm}$$

#### Planar ionic density on $(111)$

The $(111)$ plane inside the unit cell has intercepts $(1,0,0)$, $(0,1,0)$, and $(0,0,1)$ (plane equation $x + y + z = 1$). Its intersection with the cube is an equilateral triangle whose side is the face diagonal $s = a\sqrt{2}$:

$$A_{(111)} = \frac{\sqrt{3}}{4}s^2 = \frac{\sqrt{3}}{4}(a\sqrt{2})^2 = \frac{\sqrt{3}}{2}a^2 = 0.86603\times(0.4240\ \text{nm})^2 = 0.15569\ \text{nm}^2 \approx 0.1557\ \text{nm}^2$$

Testing every ion position against $x + y + z = 1$:
- **$\text{O}^{2-}$ ions:** the three corners $(1,0,0), (0,1,0), (0,0,1)$ satisfy $x + y + z = 1$, and because the internal angle of an equilateral triangle is $60^\circ = \frac{1}{6}(360^\circ)$, each corner contributes $\frac{1}{6}$ ($3\times\frac{1}{6} = \frac{1}{2}$). The three face centres $(\frac{1}{2},\frac{1}{2},0), (\frac{1}{2},0,\frac{1}{2}), (0,\frac{1}{2},\frac{1}{2})$ lie at the midpoints of the triangle sides, each contributing $\frac{1}{2}$ ($3\times\frac{1}{2} = \frac{3}{2}$). Thus $n_{\text{O}^{2-}} = \frac{1}{2} + \frac{3}{2} = 2\ \text{O}^{2-}$ ions.
- **$\text{Mg}^{2+}$ ions:** edge midpoints have sums $x+y+z \in \{\frac{1}{2}, \frac{3}{2}, \frac{5}{2}\}$ and the body centre has $x+y+z = \frac{3}{2}$, so **0 $\text{Mg}^{2+}$ ions** lie on this $(111)$ plane (the cations form parallel sheets halfway between adjacent $(111)$ anion layers).

Total ions on the $(111)$ triangle: $N_{(111)} = 2\ \text{O}^{2-} + 0\ \text{Mg}^{2+} = 2\ \text{ions}$. Therefore:

$$\rho_P(111) = \frac{N_{(111)}}{A_{(111)}} = \frac{2\ \text{ions}}{0.15569\ \text{nm}^2} = 12.846\ \text{ions/nm}^2 \approx 12.85\ \text{ions/nm}^2$$

Converting with $1\ \text{mm}^2 = (10^{6}\ \text{nm})^2 = 10^{12}\ \text{nm}^2$:

$$\rho_P(111) = 12.846\ \frac{\text{ions}}{\text{nm}^2}\times\frac{10^{12}\ \text{nm}^2}{1\ \text{mm}^2} = 1.285\times10^{13}\ \text{ions/mm}^2$$

## Interpretation

- **Physical check:** the calculated density $3.513\ \text{g/cm}^3$ is within $2\%$ of the experimental density of periclase ($\text{MgO}$, $\approx 3.58\ \text{g/cm}^3$); the slight difference reflects the slight contraction of actual interionic distances from ideal hard-sphere radii.
- **Comparison with $(100)$:** unlike $(111)$, which holds only $\text{O}^{2-}$ ions ($2$ anions on $0.1557\ \text{nm}^2$), a $(100)$ cube face of area $a^2 = 0.1798\ \text{nm}^2$ holds $4\times\frac{1}{4} + 1 = 2\ \text{O}^{2-}$ and $4\times\frac{1}{2} = 2\ \text{Mg}^{2+}$ ($4$ ions total, $\rho_P(100) = 22.25\ \text{ions/nm}^2$) and is electrically neutral ($1:1$ charge balance), explaining why rock-salt crystals cleave preferentially along $\{100\}$ planes rather than polar $\{111\}$ sheets (**extension**).
- **SI dimensional check:** $[a] = \text{m}$; $[V] = \text{m}^3$; $[\rho] = (\text{kg/mol})/(\text{m}^3\cdot\text{mol}^{-1}) = \text{kg/m}^3$; $[\rho_L] = \text{m}^{-1}$; $[\rho_P] = \text{m}^{-2}$; $[\text{APF}] = \text{m}^3/\text{m}^3$ (dimensionless).
- **Common mistake:** using $a\sqrt{2} = 4r_A$ (the FCC metal relation) instead of $a = 2(r_C + r_A)$ for rock salt, which underestimates $a$ ($0.396\ \text{nm}$) and causes the cations and anions to overlap, or counting $\text{Mg}^{2+}$ edge centres on the $x+y+z=1$ $(111)$ plane.

## Verification

- r_C / r_A | 0.072/0.140 | 0.5143
- a (nm) | 2*(0.072+0.140) | 0.4240
- d_O-O face diag (nm) | 2*(0.072+0.140)*sqrt(2)/2 | 0.2998
- 2*r_A (nm) | 2*0.140 | 0.2800
- V (nm^3) | (2*(0.072+0.140))**3 | 0.07623
- V (cm^3) | (2*(0.072+0.140))**3*1e-21 | 7.623e-23
- V (m^3) | (2*(0.072+0.140))**3*1e-27 | 7.623e-29
- V_Mg (nm^3) | 4/3*pi*0.072**3 | 1.563e-3
- V_O (nm^3) | 4/3*pi*0.140**3 | 1.1494e-2
- V_ions (nm^3) | 4*(4/3*pi*(0.072**3+0.140**3)) | 0.05223
- APF | 4*(4/3*pi*(0.072**3+0.140**3))/((2*(0.072+0.140))**3) | 0.6852
- m_cell (g) | 4*(24.31+16.00)/N_A | 2.678e-22
- rho (g/cm^3) | (4*(24.31+16.00)/N_A)/((2*(0.072+0.140))**3*1e-21) | 3.513
- rho (kg/m^3) | (4*(24.31+16.00)/N_A)/((2*(0.072+0.140))**3*1e-21)*1000 | 3513
- L_111 (nm) | 2*(0.072+0.140)*sqrt(3) | 0.7344
- rho_L[111] (ions/nm) | 2/(2*(0.072+0.140)*sqrt(3)) | 2.723
- rho_L[111] (ions/mm) | 2/(2*(0.072+0.140)*sqrt(3))*1e6 | 2.723e6
- A_111 (nm^2) | sqrt(3)/2*(2*(0.072+0.140))**2 | 0.1557
- rho_P(111) (ions/nm^2) | 2/(sqrt(3)/2*(2*(0.072+0.140))**2) | 12.85
- rho_P(111) (ions/mm^2) | 2/(sqrt(3)/2*(2*(0.072+0.140))**2)*1e12 | 1.285e13
- rho_P(100) (ions/nm^2) | 4/(2*(0.072+0.140))**2 | 22.25

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
