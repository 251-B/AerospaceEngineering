---
materia: Aerospace Materials I
tema: "Unit 8: ceramic crystal structures"
bank_id: P32
title: "Fluorite oxide unit cell from crystallographic planes"
category: mt3_problem
archetype: ceramic-structure
level: trap
unit: 8
difficulty: 3
points: 5.0
time_minutes: 35
official: false
origen: "Problem written for the bank in the style of the final of January 2016 (question 8) in MATERIALS_FINALEXAM_2016_ORD_SOL.pdf and Problems T8 (problem 4); not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - ceramic-structure
  - fluorite
  - planes
  - density
  - packing-factor
---

# Bank P32 — Fluorite oxide unit cell from crystallographic planes

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the final of January 2016 (question 8) and Problems T8 (problem 4). Method: Session 16, Slides 6 and 10 (contact, overlap, and density relations marked as extension from Topic 2). Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

A refractory ceramic oxide with general formula $A_x B_y$ (where $A$ is a tetravalent cation $A^{4+}$ and $B$ is the oxide anion $\text{O}^{2-}$) crystallizes in a cubic unit cell whose ion positions on two crystallographic planes are listed below:

- **$(100)$ plane** (a square of side $a$): $A^{4+}$ ions sit at the four corners $(0,0,0)$, $(0,1,0)$, $(0,0,1)$, and $(0,1,1)$ and at the face centre $(0,\frac{1}{2},\frac{1}{2})$; no $B^{2-}$ ions lie on this plane.
- **$(110)$ plane** ($x + y = 1$, a rectangle of width $a\sqrt{2}$ and height $a$): $A^{4+}$ ions sit at the four corners $(1,0,0)$, $(0,1,0)$, $(0,1,1)$, and $(1,0,1)$ and at the midpoints of the top and bottom long edges $(\frac{1}{2},\frac{1}{2},1)$ and $(\frac{1}{2},\frac{1}{2},0)$, while four $B^{2-}$ ions lie strictly inside the rectangle at $(\frac{1}{4},\frac{3}{4},\frac{1}{4})$, $(\frac{1}{4},\frac{3}{4},\frac{3}{4})$, $(\frac{3}{4},\frac{1}{4},\frac{1}{4})$, and $(\frac{3}{4},\frac{1}{4},\frac{3}{4})$ (the intersecting $(1\bar{1}0)$ plane $x = y$ carries the four symmetric interior $B^{2-}$ ions at $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$, $(\frac{1}{4},\frac{1}{4},\frac{3}{4})$, $(\frac{3}{4},\frac{3}{4},\frac{1}{4})$, and $(\frac{3}{4},\frac{3}{4},\frac{3}{4})$).

Given $r(A^{4+}) = 0.105\ \text{nm}$, $r(B^{2-}) = 0.138\ \text{nm}$, $M(A) = 232.04\ \text{g/mol}$ (thorium), $M(B) = 16.00\ \text{g/mol}$ (oxygen), and $N_A = 6.022\times10^{23}\ \text{mol}^{-1}$:

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Cation radius ($A^{4+}$) | $r_A$ | 0.105 nm | $1.05\times10^{-10}$ m |
| Anion radius ($B^{2-}$) | $r_B$ | 0.138 nm | $1.38\times10^{-10}$ m |
| Atomic mass of $A$ (Th) | $M_A$ | 232.04 g/mol | $232.04\times10^{-3}$ kg/mol |
| Atomic mass of $B$ (O) | $M_B$ | 16.00 g/mol | $16.00\times10^{-3}$ kg/mol |
| Avogadro's constant | $N_A$ | $6.022\times10^{23}\ \text{mol}^{-1}$ | $6.022\times10^{23}\ \text{mol}^{-1}$ |

Unit conversions: $1\ \text{nm} = 10^{-6}\ \text{mm}$; $1\ \text{nm}^2 = 10^{-12}\ \text{mm}^2$; $1\ \text{nm}^3 = 10^{-21}\ \text{cm}^3 = 10^{-27}\ \text{m}^3$; $1\ \text{g/cm}^3 = 1000\ \text{kg/m}^3$.

#### Model

- **Radius-ratio rule:** $0.732 \le r_C/r_A \le 1.0$ predicts $\text{C.I.} = 8$ (cubic coordination around the cation) [Session 16, Slide 6].
- **Fluorite ($\text{CaF}_2$) structure:** cations ($A$) sit on the FCC lattice points ($4\ \text{ions/cell}$) and anions ($B$) fill **all** 8 tetrahedral interstitial sites ($8\ \text{ions/cell}$), with $\text{C.I.}(A) = 8$ and $\text{C.I.}(B) = 4$ [Session 16, Slide 10].
- **Tetrahedral contact (extension):** a tetrahedral site at $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ touches the nearest FCC corner at $(0,0,0)$ along the body diagonal, so $\frac{\sqrt{3}}{4}a = r_A + r_B$.
- **Non-overlap checks (extension):** adjacent tetrahedral anions at $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ and $(\frac{3}{4},\frac{1}{4},\frac{1}{4})$ are separated by $a/2$ (requiring $2r_B < a/2$, i.e. $r_B < a/4$), while adjacent FCC cations are separated by $a\sqrt{2}/2$ (requiring $2r_A < a\sqrt{2}/2$).
- **APF, density, and directional/planar densities (extension from Topic 2):** $\text{APF} = (4V_A + 8V_B)/V$, $\rho = (4M_A + 8M_B)/(V N_A)$, $\rho_L[110] = N_{[110]}/L_{[110]}$, and $\rho_P(110) = N_{(110)}/A_{(110)}$.

## (a) Identify the crystal structure type, describe the lattice sites of $A^{4+}$ and $B^{2-}$, and determine the stoichiometry and coordination indices. [1.2 pts]

### Hint

Convert the $(100)$ positions into 3D cubic lattice points, recognize the $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ family as tetrahedral sites, and check the radius ratio $r_A/r_B$. Remember that in fluorite the cations, not the anions, form the FCC sublattice.

### Checkpoint

- **Structure:** fluorite ($\text{CaF}_2$ type); $A^{4+}$ on FCC ($4\ \text{ions/cell}$), $B^{2-}$ in all 8 tetrahedral sites ($8\ \text{ions/cell}$)
- **Stoichiometry:** $A_4 B_8 \to AB_2$ ($\text{ThO}_2$, thorium dioxide)
- **Coordination indices:** $r_A/r_B = 0.7609 \in [0.732, 1.0] \implies \text{C.I.}(A^{4+}) = 8$ and $\text{C.I.}(B^{2-}) = 4$

### Solution

#### Identify the 3D sublattices from the two planes

- **$A^{4+}$ sublattice:** on the cubic $(100)$ face, $A^{4+}$ occupies the four corners and the face centre $(0,\frac{1}{2},\frac{1}{2})$. By cubic symmetry, every face carries a face-centred ion, and the $(110)$ plane confirms $A^{4+}$ at the top and bottom face centres $(\frac{1}{2},\frac{1}{2},1)$ and $(\frac{1}{2},\frac{1}{2},0)$. Therefore, **$A^{4+}$ occupies the FCC lattice points**:

$$n_A = 8\times\frac{1}{8} + 6\times\frac{1}{2} = 1 + 3 = 4\ \text{cations/cell}$$

- **$B^{2-}$ sublattice:** the coordinates $(\frac{1}{4},\frac{3}{4},\frac{1}{4})$, $(\frac{1}{4},\frac{3}{4},\frac{3}{4})$, $(\frac{3}{4},\frac{1}{4},\frac{1}{4})$, and $(\frac{3}{4},\frac{1}{4},\frac{3}{4})$ on $(110)$, together with the four symmetric sites on $(1\bar{1}0)$, are the eight $(\pm\frac{1}{4},\pm\frac{1}{4},\pm\frac{1}{4})$ centres of the eight sub-cubes of edge $a/2$ inside the FCC cell — that is, **all 8 tetrahedral interstitial sites**, each completely inside the unit cell:

$$n_B = 8\times 1 = 8\ \text{anions/cell}$$

#### Structure type, stoichiometry, and coordination indices

An FCC sublattice of cations with anions occupying **all** tetrahedral sites is the **fluorite ($\text{CaF}_2$) structure** [Session 16, Slide 10].

![[attachments/T8/s16-fluorite-structure.png]]

*(Reference prototype of the fluorite structure from Session 16, Slide 10: $A^{4+}$ occupies the $\text{Ca}^{2+}$ FCC sites and $B^{2-}$ occupies all eight $\text{F}^-$ tetrahedral sites.)*

Dividing the cell counts by 4 gives the empirical stoichiometry:

$$A_4 B_8 \quad\Longrightarrow\quad AB_2$$

With $M_A = 232.04\ \text{g/mol}$ ($\text{Th}$) and $M_B = 16.00\ \text{g/mol}$ ($\text{O}$), the compound is **$\text{ThO}_2$** (thorium dioxide, listed on Session 16, Slide 10), and charge balance is verified by $4(+4) + 8(-2) = 0$.

Checking the radius ratio [Session 16, Slide 6]:

$$\frac{r_A}{r_B} = \frac{0.105\ \text{nm}}{0.138\ \text{nm}} = 0.7609$$

Since $0.732 \le 0.7609 \le 1.0$, each $A^{4+}$ cation is coordinated to 8 $B^{2-}$ anions forming a cube around it: **$\text{C.I.}(A^{4+}) = 8$**. Conversely, each $B^{2-}$ anion sits inside a tetrahedron of 4 $A^{4+}$ cations (one corner and three adjacent face centres), so **$\text{C.I.}(B^{2-}) = 4$** [Session 16, Slide 10]. Notice the bond-count identity $n_A\cdot\text{C.I.}(A) = 4\times 8 = 32 = 8\times 4 = n_B\cdot\text{C.I.}(B)$.

## (b) Find the lattice parameter $a$, verify that neither anions nor cations overlap, and calculate the cell volume $V$. [1.3 pts]

### Hint

The vector from the corner $(0,0,0)$ to the nearest tetrahedral site $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ has length $\frac{\sqrt{3}}{4}a$. Isolate $a$, then check both the $B$–$B$ edge spacing ($a/2$) and the $A$–$A$ face-diagonal spacing ($a\sqrt{2}/2$).

### Checkpoint

- $a = 0.5612\ \text{nm}$
- Anion check: $a/2 = 0.2806\ \text{nm} > 2r_B = 0.2760\ \text{nm}$ (equivalently $r_B = 0.138\ \text{nm} < a/4 = 0.1403\ \text{nm}$); cation check: $a\sqrt{2}/2 = 0.3968\ \text{nm} > 2r_A = 0.2100\ \text{nm}$
- $V = 0.1767\ \text{nm}^3 = 1.767\times10^{-22}\ \text{cm}^3 = 1.767\times10^{-28}\ \text{m}^3$

### Solution

#### Lattice parameter from tetrahedral contact

The tetrahedral site at $(\frac{1}{4}a,\frac{1}{4}a,\frac{1}{4}a)$ lies at distance

$$d_{\text{tet}} = \sqrt{\left(\frac{a}{4}\right)^2 + \left(\frac{a}{4}\right)^2 + \left(\frac{a}{4}\right)^2} = \frac{\sqrt{3}}{4}\,a$$

from the corner cation at $(0,0,0)$. Setting this centre-to-centre distance equal to $r_A + r_B$ (**extension**):

$$\frac{\sqrt{3}}{4}\,a = r_A + r_B$$

Multiplying both sides by $4$ and dividing by $\sqrt{3}$ isolates $a$:

$$a = \frac{4(r_A + r_B)}{\sqrt{3}} = \frac{4\times(0.105\ \text{nm} + 0.138\ \text{nm})}{1.73205} = \frac{0.972\ \text{nm}}{1.73205} = 0.5612\ \text{nm}$$

#### Non-overlap checks for anions and cations

1. **Anion–anion check:** the eight tetrahedral $B^{2-}$ ions form a simple-cubic sub-array of spacing $a/2$ (e.g., between $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ and $(\frac{3}{4},\frac{1}{4},\frac{1}{4})$). The spacing is

$$d_{B\text{–}B} = \frac{a}{2} = \frac{0.5612\ \text{nm}}{2} = 0.2806\ \text{nm}$$

and twice the anion radius is $2r_B = 2\times 0.138\ \text{nm} = 0.2760\ \text{nm}$ (equivalently $r_B = 0.138\ \text{nm} < a/4 = 0.1403\ \text{nm}$). Because $0.2806\ \text{nm} > 0.2760\ \text{nm}$, **the anions do not overlap**.
2. **Cation–cation check:** the nearest $A^{4+}$ ions lie along half a face diagonal:

$$d_{A\text{–}A} = \frac{a\sqrt{2}}{2} = \frac{0.5612\ \text{nm}\times 1.4142}{2} = 0.3968\ \text{nm} > 2r_A = 2\times 0.105\ \text{nm} = 0.2100\ \text{nm}$$

Thus **the cations do not overlap either**, confirming that the $A$–$B$ tetrahedral contact governs $a$.

#### Unit cell volume

$$V = a^3 = (0.5612\ \text{nm})^3 = 0.17673\ \text{nm}^3 \approx 0.1767\ \text{nm}^3$$

Converting to $\text{cm}^3$ ($1\ \text{nm}^3 = 10^{-21}\ \text{cm}^3$) and $\text{m}^3$ ($1\ \text{nm}^3 = 10^{-27}\ \text{m}^3$):

$$V = 1.767\times10^{-22}\ \text{cm}^3 = 1.767\times10^{-28}\ \text{m}^3$$

## (c) Calculate the atomic packing factor (APF) and the theoretical volumetric density $\rho$ in $\text{g/cm}^3$ and $\text{kg/m}^3$. [1.2 pts]

### Hint

Include 4 $A^{4+}$ spheres and **all 8** $B^{2-}$ spheres in both the ionic volume and the unit-cell mass (forgetting half the tetrahedral anions is a classic mistake).

### Checkpoint

- $V_A = 4.849\times10^{-3}\ \text{nm}^3$, $V_B = 1.1008\times10^{-2}\ \text{nm}^3$, $\text{APF} = 0.6081$ ($60.8\%$)
- $m_{\text{cell}} = 1.7538\times10^{-21}\ \text{g}$, $\rho = 9.924\ \text{g/cm}^3 = 9924\ \text{kg/m}^3$

### Solution

#### Atomic packing factor (APF)

Volume of one $A^{4+}$ sphere and one $B^{2-}$ sphere:

$$V_A = \frac{4}{3}\pi(0.105\ \text{nm})^3 = 4.8490\times10^{-3}\ \text{nm}^3 \approx 4.849\times10^{-3}\ \text{nm}^3$$

$$V_B = \frac{4}{3}\pi(0.138\ \text{nm})^3 = 1.1008\times10^{-2}\ \text{nm}^3$$

With $4\ A^{4+}$ and $8\ B^{2-}$ ions in the cell:

$$V_{\text{ions}} = 4V_A + 8V_B = 4(4.8490\times10^{-3}) + 8(1.1008\times10^{-2}) = 0.019396 + 0.088067 = 0.10746\ \text{nm}^3$$

$$\text{APF} = \frac{V_{\text{ions}}}{V} = \frac{0.10746\ \text{nm}^3}{0.17673\ \text{nm}^3} = 0.6081$$

#### Theoretical volumetric density

Mass of the 4 $AB_2$ formula units ($4A + 8B$) in the unit cell:

$$m_{\text{cell}} = \frac{4(M_A + 2M_B)}{N_A} = \frac{4\times(232.04 + 2\times 16.00)\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = \frac{4\times 264.04\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = \frac{1056.16\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = 1.7538\times10^{-21}\ \text{g}$$

Dividing by $V = 1.7673\times10^{-22}\ \text{cm}^3$:

$$\rho = \frac{m_{\text{cell}}}{V} = \frac{1.7538\times10^{-21}\ \text{g}}{1.7673\times10^{-22}\ \text{cm}^3} = 9.924\ \text{g/cm}^3 = 9924\ \text{kg/m}^3$$

## (d) Determine the linear ionic density along $[110]$ and the planar ionic density on $(110)$, detailing the ion counts by species. [1.3 pts]

### Hint

Watch the two traps here: (1) the $[110]$ face diagonal on $z = 0$ cuts **zero** tetrahedral anions; (2) the $(110)$ rectangle contains both the FCC cations on its corners and top/bottom edges **and** four whole $B^{2-}$ anions strictly inside it.

### Checkpoint

- $[110]$: length $a\sqrt{2} = 0.7936\ \text{nm}$; $2\ A^{4+} + 0\ B^{2-} = 2$ ions; $\rho_L[110] = 2.520\ \text{ions/nm} = 2.520\times10^{6}\ \text{ions/mm}$
- $(110)$: area $a^2\sqrt{2} = 0.4454\ \text{nm}^2$; $2\ A^{4+} + 4\ B^{2-} = 6$ ions; $\rho_P(110) = 13.47\ \text{ions/nm}^2 = 1.347\times10^{13}\ \text{ions/mm}^2$

### Solution

#### Linear ionic density along $[110]$

The $[110]$ segment across one unit cell is the face diagonal on $z = 0$ from $(0,0,0)$ to $(1,1,0)$, of length

$$L_{[110]} = a\sqrt{2} = 0.5612\ \text{nm}\times 1.41421 = 0.7936\ \text{nm}$$

Along the line $x = y$, $z = 0$:
- **$A^{4+}$ ions:** two corners at $(0,0,0)$ and $(1,1,0)$ (each shared between two collinear cells, $2\times\frac{1}{2} = 1$) plus the face centre at $(\frac{1}{2},\frac{1}{2},0)$ ($1$ ion), giving $n_A = 2\ A^{4+}$ ions.
- **$B^{2-}$ ions:** all tetrahedral anions sit at $z = \frac{1}{4}$ or $z = \frac{3}{4}$, never $z = 0$, so **0 $B^{2-}$ ions** lie on $[110]$.

Thus $N_{[110]} = 2\ \text{ions}$, and

$$\rho_L[110] = \frac{N_{[110]}}{L_{[110]}} = \frac{2\ \text{ions}}{0.7936\ \text{nm}} = 2.520\ \text{ions/nm} = 2.520\times10^{6}\ \text{ions/mm}$$

#### Planar ionic density on $(110)$

The $(110)$ plane $x + y = 1$ cuts the cell in a rectangle of width $a\sqrt{2}$ and height $a$:

$$A_{(110)} = (a\sqrt{2})\,a = a^2\sqrt{2} = (0.5612\ \text{nm})^2\times 1.41421 = 0.44538\ \text{nm}^2 \approx 0.4454\ \text{nm}^2$$

Counting every ion on the $(110)$ rectangle from the statement:
- **$A^{4+}$ ions:** four corners $(1,0,0)$, $(0,1,0)$, $(0,1,1)$, and $(1,0,1)$ (each shared by 4 coplanar cells, $4\times\frac{1}{4} = 1$) plus two edge midpoints $(\frac{1}{2},\frac{1}{2},0)$ and $(\frac{1}{2},\frac{1}{2},1)$ (each shared by 2 coplanar cells, $2\times\frac{1}{2} = 1$), giving $n_A = 1 + 1 = 2\ A^{4+}$ ions.
- **$B^{2-}$ ions:** all four anions $(\frac{1}{4},\frac{3}{4},\frac{1}{4})$, $(\frac{1}{4},\frac{3}{4},\frac{3}{4})$, $(\frac{3}{4},\frac{1}{4},\frac{1}{4})$, and $(\frac{3}{4},\frac{1}{4},\frac{3}{4})$ lie strictly inside the rectangle boundaries ($0 < z < 1$), so each contributes $1$: $n_B = 4\times 1 = 4\ B^{2-}$ ions.

Notice the $2:4 = 1:2$ ratio on $(110)$, making the plane electrically neutral ($2(+4) + 4(-2) = 0$). The total ion count is $N_{(110)} = 2 + 4 = 6\ \text{ions}$, so

$$\rho_P(110) = \frac{N_{(110)}}{A_{(110)}} = \frac{6\ \text{ions}}{0.44538\ \text{nm}^2} = 13.472\ \text{ions/nm}^2 \approx 13.47\ \text{ions/nm}^2 = 1.347\times10^{13}\ \text{ions/mm}^2$$

## Interpretation

- **Why the cation forms the FCC sublattice despite $r_A < r_B$:** in $\text{ThO}_2$ the cation radius ($0.105\ \text{nm}$) is smaller than the oxygen radius ($0.138\ \text{nm}$), which often tricks students into placing $\text{O}^{2-}$ on FCC. However, the $1:2$ stoichiometry and $\text{C.I.}(A) = 8$ require the cations to sit at the 4 FCC sites so that the 8 smaller-coordination ($\text{C.I.} = 4$) anions can occupy all 8 tetrahedral holes (forming a simple-cubic anion array of side $a/2$ with $a/2 > 2r_B$).
- **Physical check:** the calculated density $9.924\ \text{g/cm}^3$ agrees closely with the experimental density of thoria ($\text{ThO}_2$, $\approx 10.00\ \text{g/cm}^3$, $a_{\text{exp}} = 0.5597\ \text{nm}$; **extension**).
- **SI dimensional check:** $[a] = \text{m}$; $[V] = \text{m}^3$; $[\rho] = \text{kg/m}^3$; $[\rho_L] = \text{m}^{-1}$; $[\rho_P] = \text{m}^{-2}$; $[\text{APF}]$ dimensionless.
- **Common mistakes (the three traps):** (1) using $a\sqrt{2} = 4r_A$ as in an FCC metal, which ignores the $\text{O}^{2-}$ anions and gives severe overlap; (2) counting only 4 $B^{2-}$ ions per unit cell because only four appear on $(110)$, forgetting the four on $(1\bar{1}0)$; (3) omitting the 4 interior $B^{2-}$ ions from $\rho_P(110)$ (which would wrongly give $2/A_{(110)} = 4.49\ \text{ions/nm}^2$).

## Verification

- r_A / r_B | 0.105/0.138 | 0.7609
- a (nm) | 4*(0.105+0.138)/sqrt(3) | 0.5612
- d_B-B (nm) | 4*(0.105+0.138)/sqrt(3)/2 | 0.2806
- 2*r_B (nm) | 2*0.138 | 0.2760
- a/4 (nm) | 4*(0.105+0.138)/sqrt(3)/4 | 0.1403
- d_A-A (nm) | 4*(0.105+0.138)/sqrt(3)*sqrt(2)/2 | 0.3968
- 2*r_A (nm) | 2*0.105 | 0.2100
- V (nm^3) | (4*(0.105+0.138)/sqrt(3))**3 | 0.1767
- V (cm^3) | (4*(0.105+0.138)/sqrt(3))**3*1e-21 | 1.767e-22
- V (m^3) | (4*(0.105+0.138)/sqrt(3))**3*1e-27 | 1.767e-28
- V_A (nm^3) | 4/3*pi*0.105**3 | 4.849e-3
- V_B (nm^3) | 4/3*pi*0.138**3 | 1.1008e-2
- V_ions (nm^3) | 4*(4/3*pi*0.105**3)+8*(4/3*pi*0.138**3) | 0.10746
- APF | (4*(4/3*pi*0.105**3)+8*(4/3*pi*0.138**3))/((4*(0.105+0.138)/sqrt(3))**3) | 0.6081
- m_cell (g) | 4*(232.04+2*16.00)/N_A | 1.7538e-21
- rho (g/cm^3) | (4*(232.04+2*16.00)/N_A)/((4*(0.105+0.138)/sqrt(3))**3*1e-21) | 9.924
- rho (kg/m^3) | (4*(232.04+2*16.00)/N_A)/((4*(0.105+0.138)/sqrt(3))**3*1e-21)*1000 | 9924
- L_110 (nm) | 4*(0.105+0.138)/sqrt(3)*sqrt(2) | 0.7936
- rho_L[110] (ions/nm) | 2/(4*(0.105+0.138)/sqrt(3)*sqrt(2)) | 2.520
- rho_L[110] (ions/mm) | 2/(4*(0.105+0.138)/sqrt(3)*sqrt(2))*1e6 | 2.520e6
- A_110 (nm^2) | (4*(0.105+0.138)/sqrt(3))**2*sqrt(2) | 0.4454
- rho_P(110) (ions/nm^2) | 6/((4*(0.105+0.138)/sqrt(3))**2*sqrt(2)) | 13.47
- rho_P(110) (ions/mm^2) | 6/((4*(0.105+0.138)/sqrt(3))**2*sqrt(2))*1e12 | 1.347e13

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
