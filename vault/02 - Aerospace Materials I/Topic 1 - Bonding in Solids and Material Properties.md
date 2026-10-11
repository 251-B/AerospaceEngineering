---
materia: "Aerospace Materials I"
tema: "Topic 1: Bonding in Solids"
fuentes: "Session 2 T1 Bonding_2025.pdf, Slides 1-39"
tags:
  - theory
  - topic-moc
  - bonding
  - ionic-bonding
  - covalent-bonding
  - metallic-bonding
  - secondary-bonding
dificultad: medium
prerrequisitos: []
---

# 🌐 Topic 1: Bonding in Solids

> **Central idea:** the way atoms are bonded decides the properties of a material, the properties decide what type of material it is, and that decides how it is processed and where it is used [Slide 2].

This note follows the slides of `Session 2 T1 Bonding_2025.pdf` in their order and uses only what they contain. Every statement carries the slide it comes from. Short "Reading the slide" boxes explain a figure or join two formulas that are on the same slide; they add no new content.

**Contents of the topic** [Slide 1]:
1. Introduction
2. Bonding in solids: ionic bonding, covalent bonding, metallic bonding, secondary bonding (intermolecular forces)
3. Bonding and properties in materials

---

## 1. Introduction [Slide 2]

The slide links four ideas in a chain:

$$\text{Nature of bonding} \;\leftrightarrow\; \text{properties} \;\leftrightarrow\; \text{type of materials} \;\leftrightarrow\; \text{processing and applications}$$

It draws them as a tetrahedron whose four corners are **Structure**, **Properties**, **Processing** and **Applications**. Each corner is connected to the other three: changing one of them changes the others.

---

## 2. Ionic bonding [Slides 4-15]

See also [[Concept - Ionic Bonding and Lattice Energy]].

### 2.1 Definition and basic properties [Slide 4]

**Ionic bonding** is the complete transfer of valence electron(s) between atoms. It is a type of chemical bond that generates two oppositely charged ions.

Properties listed on the slide:
- It forms between **metal and nonmetallic** elements.
- Electrons are transferred **from the less electronegative atom to the more electronegative** one.
- Bonding force: **electrostatic attraction** between the oppositely charged ions.
- It is **non-directional**.

The slide diagram: the electropositive element gives an electron to the electronegative atom; the first becomes a **cation** (positive charge), the second an **anion** (negative charge); the electrostatic attraction between them is the **ionic bond**. A periodic table shows how electronegativity varies.

### 2.2 How the bond forms: NaCl [Slide 5]

An ionic bond is created between two unlike atoms with different electronegativities. When sodium gives its valence electron to chlorine, each becomes an ion (Na⁺ and Cl⁻), they attract each other, and the ionic bond is formed.

- When a metal forms a **cation**, its radius is **reduced**.
- When a nonmetal forms an **anion**, its radius **increases**.
- A **pure** ionic bond is an ideal case: there is **always some covalent participation**.

### 2.3 Fundamental principles of ionic structures [Slide 6]

Ions are treated as:
1. **Charged spheres**,
2. **Elastic spheres**,
3. **Polarizable** spheres: the electron cloud is distorted by the presence of other ions.

The slide compares electron-density maps: in a covalent bond (N₂) the electron density is shared between the two atoms; in an ionic bond (LiF) each ion keeps its own, separate cloud. A table gives the sizes of atoms and of their ions (in pm): cations are smaller than their atoms, anions are larger.

### 2.4 Interionic force for an ionic pair [Slide 7]

How the force between two ions depends on their distance:
- **Too far:** they neither attract nor repel.
- **Larger distances:** Coulombic **attraction** dominates.
- **Smaller distances:** the electron clouds **repel**.

The net force is the sum of both:

$$F_{net} = F_{attractive} + F_{repulsive}$$

$$F_{net} = -\frac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 a^2} - \frac{n b}{a^{n+1}}$$

| Symbol | Meaning (as on the slide) |
| :--- | :--- |
| $Z_1, Z_2$ | number of electrons removed or added (the charge numbers of the ions) |
| $e$ | electron charge, $1.6\times10^{-19}\ \text{C}$ |
| $\varepsilon_0$ | permittivity of space, $8.85\times10^{-12}\ \text{C}^2/(\text{N}\cdot\text{m}^2)$ |
| $b$ | constant |
| $n$ | Born exponent, between 5 and 9 |
| $a$ | interionic distance ($a_0$ at equilibrium) |

> [!info] Reading the slide
> The graph on the slide plots attraction above the axis and repulsion below it. The two ions are drawn touching: the cation radius $r$ plus the anion radius $R$ gives the distance $r + R = a$. The net force is zero at $a_0$; at slightly larger distances it reaches a **maximum force** (the maximum attraction the pair can resist).

### 2.5 Net potential energy for an ionic pair [Slide 8]

The energy of the pair is lowest (**minimum**) when the ions sit at one specific distance $a_0$. This is the **equilibrium distance**, where attractive and repulsive energies are balanced.

The slide relates force and energy by $F = \left(\dfrac{\partial E}{\partial a}\right)$ and writes the net energy as:

$$E_{net} = \underbrace{\frac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 a_0}}_{\text{attraction energy (released)}} + \underbrace{\frac{b}{a_0^{\,n}}}_{\text{repulsion energy (absorbed)}}$$

> [!info] Reading the slide
> - $Z_1$ and $Z_2$ have opposite signs (one ion is positive, the other negative), so the attraction term is negative: energy is **released**. The repulsion term is positive: energy is **absorbed**.
> - Differentiating $E_{net}$ with respect to $a$ gives back the force of Slide 7, term by term:
>   $\dfrac{\partial}{\partial a}\left(\dfrac{Z_1Z_2e^2}{4\pi\varepsilon_0}\,a^{-1}\right) = -\dfrac{Z_1Z_2e^2}{4\pi\varepsilon_0 a^2}$ and $\dfrac{\partial}{\partial a}\left(b\,a^{-n}\right) = -\dfrac{n b}{a^{n+1}}$.
> - The graphs on the slide show the energy curve with its minimum at $a_0$, where $\dfrac{dU}{dr} = 0$, exactly where the net force crosses zero.

### 2.6 Lattice energy U [Slide 9]

**Lattice energy (U):** the energy needed to bring one mole of ions from an infinite distance to their fixed positions in a crystal.

Starting from the energy of one pair at equilibrium, the slide arrives at the lattice energy of one mole:

$$E_{r=a_0} = \frac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 a_0} + \frac{b}{a_0^{\,n}} \quad\Longrightarrow\quad U = -\frac{Z_1 Z_2 e^2 N_A A}{4\pi\varepsilon_0 a_0}\left(1-\frac{1}{n}\right)$$

$N_A$ is Avogadro's number (one mole of pairs). $A$ is a constant of the crystal; the slide does not detail it further.

> [!info] Reading the slide: where the factor $(1 - 1/n)$ comes from
> 1. At $a_0$ the force is zero, so the derivative of $E$ is zero: $-\dfrac{Z_1Z_2e^2}{4\pi\varepsilon_0 a_0^2} - \dfrac{n b}{a_0^{n+1}} = 0$.
> 2. Solve for $b$: multiply by $a_0^{n+1}$ to get $-\dfrac{Z_1Z_2e^2 a_0^{n-1}}{4\pi\varepsilon_0} = n b$, so $b = -\dfrac{Z_1Z_2e^2 a_0^{n-1}}{4\pi\varepsilon_0\, n}$.
> 3. Substitute $b$ in the repulsion term: $\dfrac{b}{a_0^n} = -\dfrac{Z_1Z_2e^2}{4\pi\varepsilon_0 a_0}\cdot\dfrac{1}{n}$.
> 4. Add the attraction term: $E_{r=a_0} = \dfrac{Z_1Z_2e^2}{4\pi\varepsilon_0 a_0}\left(1-\dfrac{1}{n}\right)$.
> 5. Multiplying by $N_A A$ gives the bracket of $U$. In $U$ the slide writes $Z_1Z_2$ as positive charge numbers and puts the sign in front, so that $U$ comes out negative (Slide 10: "All energy values are negative").
>
> Since $n$ is between 5 and 9, the repulsion only removes $1/n$ (between 11 % and 20 %) of the attraction energy.

**Lattice energy, alternative view:** the energy **released** when one mole of ionic solid is formed from its ions in the gas state.

The slide shows this with the **Born-Haber cycle for KCl**:

| Step | ΔH (kJ/mol) |
| :--- | ---: |
| K sublimation | +89 |
| K(g) ionization | +425 |
| Cl₂(g) dissociation | +244 |
| Cl(g) ionization | −355 |
| KCl formation | −438 |

> [!info] Reading the slide: the cycle
> The diagram climbs from K(s) + ½Cl₂(g) to K⁺(g) + e⁻(g) + Cl(g), then falls to KCl(s). Only half a mole of Cl₂ is needed, so the dissociation step drawn in the cycle is 244/2 = 122 kJ/mol. The cycle is closed by $U$, the step from K⁺(g) + Cl⁻(g) down to KCl(s). Going round the cycle with the slide's numbers:
> $$U = -438 - (89 + 425 + 122 - 355) = -438 - 281 = -719\ \text{kJ/mol}$$
> (This value is worked out from the slide's numbers; the slide itself does not print it.)

### 2.7 Properties associated with the lattice energy [Slides 10-13]

#### 1. Melting point [Slide 10]

| Ionic solid | U (kJ/mol) | U (kcal/mol) | Melting point (°C) |
| :--- | ---: | ---: | ---: |
| LiCl | 829 | 198 | 613 |
| NaCl | 766 | 183 | 801 |
| KCl | 686 | 164 | 776 |
| RbCl | 670 | 160 | 715 |
| CsCl | 649 | 155 | 646 |
| MgO | 3932 | 940 | 2800 |
| CaO | 3583 | 846 | 2580 |
| SrO | 3311 | 791 | 2430 |
| BaO | 3127 | 747 | 1923 |

All energy values are negative (the table gives their size).

- **Valence +1:** when the ion size increases ↑, the lattice energy decreases ↓ and $T_m$ decreases ↓.
- **Valence +2:** a higher valence number ↑ gives a higher lattice energy ↑ and a higher $T_m$ ↑ (compare MgO, 2800 °C, with NaCl, 801 °C).

> [!warning] Small exception in the slide's own data
> In the valence +1 group, $T_m$ does not fall all the way: LiCl (613 °C) melts lower than NaCl (801 °C) even though its U is larger. The trend holds from NaCl to CsCl. This is only a reading of the table; the slide states the general trend.

#### 2. Hardness [Slide 11]

**Hardness** is a measure of the resistance to localized plastic deformation caused by mechanical indentation or abrasion. Several scales exist, e.g. the Mohs scale (used by mineralogists).

| | BeO | MgO | CaO | SrO | BaO |
| :--- | ---: | ---: | ---: | ---: | ---: |
| d (Å) | 1.65 | 2.10 | 2.40 | 2.57 | 2.77 |
| Mohs hardness | 9.0 | 6.5 | 4.5 | 3.5 | 3.3 |

For reference: hydroxyapatite 5, keratin (fingernail) 2.5. (1 Å = 0.1 nm.)

$$r_{c^+} \downarrow \;\Rightarrow\; U \uparrow \;\Rightarrow\; \text{hardness} \uparrow$$

The **binding (potential) energy** is the energy needed to create or break the bond. Materials with a high binding energy have high melting temperatures and high hardness. The slide's figure shows the binding energy as the depth of the energy curve at the interatomic spacing.

#### 3. Thermal expansion [Slide 12]

**Thermal expansion** is the tendency of matter to change its volume in response to a change in temperature.

The **coefficient of thermal expansion** (the change in linear dimension of a material per degree of temperature) is related to the strength of the atomic bonds. Materials whose energy curve is steep, with a **deep interatomic energy (IAE) trough** caused by strong bonding, have **low** linear coefficients of thermal expansion.

| | NaF | NaCl | NaBr | NaI |
| :--- | ---: | ---: | ---: | ---: |
| $\alpha_V$ (10⁻⁶ °C⁻¹) | 39 | 40 | 43 | 48 |

For reference: hydroxyapatite 12·10⁻⁶ °C⁻¹.

$$r_{a^-} \uparrow \;\Rightarrow\; U \downarrow \;\Rightarrow\; \text{thermal expansion } (\alpha) \uparrow$$

> [!info] Reading the slide figure
> Heating adds the same energy ΔIAE to two curves. In the **weak-bonding** curve (shallow, wide) the spacing between atoms grows a lot; in the **strong-bonding** curve (deep, narrow) it grows little. A larger separation after heating means a higher thermal expansion.

#### 4. Young's modulus [Slide 13]

(The slide numbers this property "2", but it is the fourth property of the list.)

A high binding energy (steep slope) means a greater force is needed to stretch the bonds, and so a **higher elastic (Young's) modulus**. The slide's figure shows the force-distance curves for strong and weak bonding: the slope $dF/da$ where the curve crosses the distance axis is steeper for strong bonding.

### 2.8 General properties of ionic compounds [Slide 14]

1. Strong electrostatic attraction → **high melting and evaporation points**.
2. **Hard and brittle** solids at room temperature.
3. They **do not conduct electricity**, except when molten or dissolved in water. When a voltage is applied, whole ions must move to carry a current; ions move slowly, so the electrical conductivity is poor.
4. **Water soluble.**

### 2.9 Ion arrangements in ionic solids [Slide 15]

- Ionic bonds are **non-directional**.
- The ions take geometric arrangements in the solid that **keep the solid electrically neutral** (examples on the slide: the ionic packing of CsCl and NaCl).
- As the ratio of **cation radius to anion radius decreases**, **fewer anions** surround the central cation.
- Ionic compounds are **crystalline solids**.

---

## 3. Covalent bonding [Slides 17-21]

See also [[Concept - Covalent Bonding and Polar Character]].

### 3.1 Definition [Slide 17]

- It usually forms between the **non-metallic** elements of the periodic table.
- It forms by **sharing electrons**.
- It is **highly directional**, and there are **no free electrons**.
- It takes place between elements with **small differences in electronegativity** that are close to each other in the periodic table.
- The outer **s and p electrons** are shared between two atoms so that each one reaches a **noble-gas configuration**.

Examples on the slide: H• + •H → H:H (H–H, one bond pair); two Cl atoms form Cl–Cl, with one bond pair and lone pairs on each Cl.

### 3.2 Examples: silicon and silica [Slide 18]

- **Silicon** has a valence of four, so it must form **four covalent bonds**. Because covalent bonds are **directional**, silicon forms a **tetrahedral structure** with **109.5°** between bonds.
- **Silica (SiO₂)** has the same tetrahedral structure, with covalent bonds between silicon and oxygen atoms.

### 3.3 Properties of compounds with covalent bonds [Slide 19]

**Covalent solids:**
- Formed by a system of **continuous covalent bonds**.
- **Non-conductive** lattices, both solid and molten.
- Examples: diamond, boron nitride, quartz (SiO₂), silicon carbide (SiC).
- **Hard and incompressible**; **high $T_m$**, non-volatile; **insoluble**.
- The slide shows the structures of graphite and diamond.

**Substances with covalent bonds:** the slide shows a polymer chain (–C–C–C– with H and R side groups) as an example.

### 3.4 Polar covalent bond [Slide 20]

- A **polar covalent bond** exists when atoms with **different electronegativities** share electrons in a covalent bond.
- In **nonpolar bonds** the bonding electrons are shared **equally** between the atoms.

The slide's figure: in H–H and Cl–Cl the centres of positive and negative charge coincide (nonpolar); in H–Cl they are separated (polar).

**Dipole moment:**

$$\mu = Q \times d$$

$d$ = distance between atoms; $Q$ = charge. Unit: Debye, $1\ \text{D} = 3.33\times10^{-30}\ \text{C}\cdot\text{m}$.

**Percentage of ionic character** of a bond between atoms A and B:

$$\%\ \text{ionic character} = \left(1 - e^{-0.25\,(X_A - X_B)^2}\right)\times 100\%$$

$X_i$ is the electronegativity of element $i$. The slide's graph plots this curve: the larger the electronegativity difference, the larger the ionic character (HI, HBr near the bottom; HF in the middle; KCl, LiF near the top).

> [!info] Reading the formula
> If $X_A = X_B$ the exponent is zero, $e^0 = 1$, and the ionic character is 0 % (a pure covalent, nonpolar bond). As the difference grows, $e^{-0.25(X_A-X_B)^2}$ tends to 0 and the ionic character tends to 100 %. This matches Slide 5: a pure ionic bond is an ideal that is never fully reached.

### 3.5 Bond length, bond order and bond energy [Slide 21]

For a given pair of atoms, a **higher bond order** gives a **shorter bond**, and a shorter bond has a **higher bond energy** (examples H₂, F₂, N₂).

Selected values from the slide's table (all values are negative for bond formation, because energy is released):

| Bond | Bond energy (kJ/mol) | Bond length (nm) |
| :--- | ---: | ---: |
| C–C | 370 | 0.154 |
| C=C | 680 | 0.13 |
| C≡C | 890 | 0.12 |
| C–H | 435 | 0.11 |
| O–H | 500 | 0.10 |
| O–Si | 375 | 0.16 |
| F–F | 160 | 0.14 |
| H–H | 435 | 0.074 |

---

## 4. Metallic bonding [Slides 23-27]

See also [[Concept - Metallic Bonding and Energy Band Theory]].

### 4.1 Definition [Slide 23]

The **metallic bond** forms when atoms give up their valence electrons, which then form an **electron sea**. The positively charged atom cores are bonded by their mutual attraction to the negatively charged electrons. In short, metallic bonds come from the **electrostatic attraction between metal cations and delocalized electrons**.

- Atoms in metals are **closely packed** in a crystal structure.
- The electrons spread out among the atoms, forming **electron clouds**.
- Because the outer electrons are shared by many atoms, metallic bonds are **non-directional**.

### 4.2 Bonding energy and valence electrons [Slide 24]

- Metallic bonds **lower the overall energy** of the individual atoms.
- The energy between atoms is **minimum at the equilibrium distance $a_0$**.
- **Fewer** valence electrons → **lower** bonding energy. Example: K, valence +1 → bonding energy 89.6 kJ/mol, melting temperature 63.5 °C.
- **More** valence electrons → **higher** bonding energy. Example: Ca, valence +2 → bonding energy 177 kJ/mol, melting temperature 851 °C.

The slide's table for the fourth-period metals:

| Element | Electron configuration | Bonding energy (kJ/mol) | Melting point (°C) |
| :--- | :--- | ---: | ---: |
| K | 4s¹ | 89.6 | 63.5 |
| Ca | 4s² | 177 | 851 |
| Sc | 3d¹4s² | 342 | 1397 |
| Ti | 3d²4s² | 473 | 1660 |
| V | 3d³4s² | 515 | 1730 |
| Cr | 3d⁵4s¹ | 398 | 1903 |
| Mn | 3d⁵4s² | 279 | 1244 |
| Fe | 3d⁶4s² | 418 | 1535 |
| Co | 3d⁷4s² | 383 | 1490 |
| Ni | 3d⁸4s² | 423 | 1455 |
| Cu | 3d¹⁰4s¹ | 339 | 1083 |
| Zn | 4s² | 131 | 419 |
| Ga | 4s²4p¹ | 272 | 29.8 |
| Ge | 4s²4p² | 377 | 960 |

### 4.3 Metallic bonds and material properties [Slide 25]

- Pure metals are much more **malleable** than ionic or covalent networked materials. The strength of a pure metal can be increased a lot by **alloying**.
- Pure metals are **excellent conductors of heat and electricity**. When a voltage is applied, the electrons of the electron sea move easily and carry a current.

### 4.4 Band theory [Slides 26-27]

**Band theory** is a model that describes the states of electrons in solids, which can only have energies within certain specific ranges [Slide 26].

- In a metallic crystal, all the molecular orbitals (MO) of the free atoms turn into a group of **non-localized orbitals** called a **band**. The energy difference between neighbouring MOs is so small that the energy is almost a **continuum**.
- A metal can be seen as a **giant molecule** formed by a giant number of MOs.
- The slide's example is Li [1s² 2s¹]: going from Li to Li₂, Li₃, …, Li_N, the 2s levels multiply until they form an **energy band**.

The **band structure depends on the interatomic distance**: the outermost atomic orbitals overlap and form an energy band [Slide 27]. The slide draws it for Li (Z = 3, 1s² 2s¹) and Mg (1s² 2s²), with a valence band and a conduction band for each.

> [!warning] Discrepancy in the slide
> Slide 27 labels magnesium "Mg (Z=4) 1s² 2s²". That configuration (four electrons) is beryllium; magnesium has Z = 12. The diagram itself is read as written.

---

## 5. Secondary bonding: intermolecular forces [Slides 29-35]

See also [[Concept - Intermolecular Forces and Secondary Bonds]].

### 5.1 Recap: primary bonds are strong [Slide 29]

| Primary bond | Energy (kcal/mol) | Mechanism |
| :--- | :--- | :--- |
| Ionic | 150-370 | transfer of e⁻ → cations and anions → Coulomb force (non-directional) |
| Covalent | 125-300 | sharing of e⁻ (directional) |
| Metallic | 25-200 | e⁻ shared externally and held very loosely by the nucleus (non-directional) |

The slide illustrates the three with diagrams: Na giving an electron to Cl (ionic), two Cl atoms sharing a pair (covalent), and Cu²⁺ ion cores in an electron cloud of valence electrons (metallic).

### 5.2 Secondary bonds: weak (van der Waals) [Slide 30]

Secondary bonds come from the **attraction between electric dipoles** in atoms or molecules. A dipole appears when the electron charge is distributed **asymmetrically**, so the centres of positive and negative charge are in different places.

There are two types of dipoles:
- **Permanent dipoles:** do not fluctuate with time.
- **Fluctuating dipoles:** the charge of the electron cloud changes with time.

### 5.3 Permanent dipole (1-10 kcal/mol) [Slide 31]

It forms in molecules that:
- have a **constant dipole moment μ**, and
- are made of atoms with **different electronegativity** joined by **covalent** bonds.

Example:
- **CH₄:** the four C–H bonds are arranged **symmetrically** → **no dipole moment**.
- **CH₃Cl:** the tetrahedral arrangement is **asymmetrical** → it **creates a dipole**.

### 5.4 Example: PVC [Slide 32]

- (a) In polyvinyl chloride (PVC), the chlorine atoms on the polymer chain carry a negative charge and the hydrogen atoms a positive charge. The chains are weakly bonded to each other by van der Waals bonds. This extra bonding makes PVC **stiffer**.
- (b) When a force is applied, the van der Waals bonds break and the chains **slide past one another**.

### 5.5 Hydrogen bond (permanent dipole, 7 kcal/mol in H₂O) [Slide 33]

In molecules with H and **electronegative atoms** (O–H, N–H, F–H) the charge is distributed asymmetrically → polar covalent bond → permanent dipole.

- **Hydrogen bonds** are **dipole-dipole interactions** between polar bonds that contain a hydrogen atom.
- Example: in water the dipole comes from the asymmetrical arrangement of the hydrogen atoms (the slide draws the H–O–H angle as 105°). Neighbouring molecules attract: the hydrogen of one molecule is attracted by the oxygen of the next.

> [!warning] Erratum in the slide
> Slide 33 says "attraction between positive oxygen pole and negative hydrogen pole". The signs are swapped. Oxygen is the more electronegative atom, so it pulls the shared electrons and becomes the **negative** pole; hydrogen becomes the **positive** pole. This follows from the slide's own definitions: electrons move towards the more electronegative atom (Slide 4) and a polar bond forms between atoms of different electronegativity (Slide 20).

### 5.6 Fluctuating dipole (< 2 kcal/mol) [Slide 34]

It forms in **non-polar** molecules in a crystalline lattice. The electron charge distribution fluctuates instantaneously: at one instant it is symmetrical, at the next asymmetrical. Those changing asymmetries are **fluctuating dipoles**.

### 5.7 Example: boiling points of molecular hydrides [Slide 35]

- Elements in higher periods generally have higher melting points: their atoms share more electrons, which gives stronger forces holding the molecules together.
- However, **strong hydrogen bonding** gives H₂O, HF and NH₃ a **much higher boiling point** than the trend predicts.

The slide's graph (groups 14 to 17, periods 2 to 5) shows it: CH₄, SiH₄, GeH₄, SnH₄ rise steadily with the period, while H₂O, HF and NH₃ break the trend at period 2.

> [!note] Label of the graph
> The caption reads "Variation of melting points of molecular hydrides", but the vertical axis of the graph is the **boiling point** (°C), as the text of the slide says.

---

## 6. Bonding and properties in materials [Slides 37-38]

See also [[Concept - Interatomic Potential Energy Curves and Macroscopic Properties]].

**Nature of bonding → properties → type of material** [Slide 37]:

| Type of material | Character of bonding | Examples |
| :--- | :--- | :--- |
| Metal | Metallic | Fe, steels |
| Ceramics and glasses | Ionic / covalent | Silica (SiO₂) |
| Polymers | Covalent and secondary | Polyethylene –(CH₂)– |

**Summary of properties by bond** [Slide 38]:

| Bond | Type of substance | Melting and boiling points | Mechanical properties | Solubility |
| :--- | :--- | :--- | :--- | :--- |
| Covalent | Molecular | Low | Soft in the solid state | Depends on the polarity of the molecules |
| Covalent | Atomic, covalent or lattice | Very high | Very hard, brittle | Insoluble in all solvents |
| Ionic | Ionic | High | Hard and brittle | Soluble in polar solvents |
| Metallic | Metallic | High | Ductile and workable | Insoluble in all solvents |

---

## 7. Questions [Slide 39]

The slide closes with four questions, solved in their own notes:
1. Compare metallic and covalent primary bonds: nature of the bond, valence of the atoms, ductility → [[Problem - T1 Exam Question 1 Metallic vs Covalent Bonding]]
2. Titanium is stiffer than aluminium, has a lower thermal expansion coefficient and a higher melting temperature: draw both potential-well curves → [[Problem - T1 Exam Question 2 Potential Curves Titanium vs Aluminium]]
3. MgO or magnesium: which has the higher modulus of elasticity? → [[Problem - T1 Exam Question 3 Elastic Modulus MgO vs Mg]]
4. Aluminium or silicon: which has the higher modulus of elasticity? → [[Problem - T1 Exam Question 4 Elastic Modulus Aluminium vs Silicon]]

---

**Back to:** [[Aerospace Materials I MOC]]
