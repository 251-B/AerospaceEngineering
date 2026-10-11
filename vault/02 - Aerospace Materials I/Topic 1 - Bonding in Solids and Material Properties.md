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

> **Central idea:** how the atoms of a material are bonded decides its properties; the properties decide what kind of material it is, and that in turn decides how it can be processed and what it can be used for.

The topic covers the three primary bonds (ionic, covalent and metallic), the weak secondary bonds between molecules, and how each type of bond shows up in the properties of a material.

---

## 1. Introduction [Slide 2]

Materials science links four ideas: **structure**, **properties**, **processing** and **applications**. They are often drawn as the four corners of a tetrahedron, because each one is connected to the other three: change the processing and the structure changes, change the structure and the properties change, and so on.

At the root of this chain is the **nature of the bonding** between atoms:

$$\text{Nature of bonding} \;\leftrightarrow\; \text{properties} \;\leftrightarrow\; \text{type of material} \;\leftrightarrow\; \text{processing and applications}$$

![[attachments/T1/tetrahedron.svg]]

---

## 2. Ionic bonding [Slides 4-15]

See also [[Concept - Ionic Bonding and Lattice Energy]].

### 2.1 What an ionic bond is [Slide 4]

An **ionic bond** forms when one or more valence electrons are **completely transferred** from one atom to another. The result is two ions with opposite charges that attract each other.

- It forms between a **metal** and a **nonmetal**.
- The electron goes from the **less electronegative** atom (the metal) to the **more electronegative** one (the nonmetal). The first becomes a positive **cation**, the second a negative **anion**.
- What holds the ions together is the **electrostatic attraction** between opposite charges.
- This attraction acts equally in all directions: the ionic bond is **non-directional**.

### 2.2 Example: sodium chloride [Slide 5]

Sodium and chlorine have very different electronegativities. Sodium gives its single valence electron to chlorine; sodium becomes Na⁺ and chlorine becomes Cl⁻, and the two ions attract each other.

Forming ions also changes their size:
- a metal that becomes a **cation** gets **smaller**;
- a nonmetal that becomes an **anion** gets **larger**.

A perfectly ionic bond is an ideal case. Real ionic bonds always have **some covalent character**.

### 2.3 How ions are modelled [Slide 6]

To describe ionic solids, ions are treated as:
1. **charged spheres**,
2. **elastic spheres**,
3. **polarizable spheres**: the electron cloud of an ion can be distorted by the ions around it.

The difference with a covalent bond is clear in the electron density: in a covalent bond (such as N₂) the electrons are shared in the region between the two atoms, while in an ionic bond (such as LiF) each ion keeps its own separate electron cloud.

### 2.4 Force between two ions [Slide 7]

How strongly two ions pull on each other depends on how far apart they are:
- when they are **very far apart**, they do not interact;
- at **large distances**, the Coulomb **attraction** between opposite charges dominates;
- at **short distances**, the electron clouds overlap and **repel**.

The net force is the sum of the two effects:

$$F_{net} = F_{attractive} + F_{repulsive}$$

$$F_{net} = -\frac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 a^2} - \frac{n b}{a^{n+1}}$$

| Symbol | Meaning |
| :--- | :--- |
| $Z_1, Z_2$ | number of electrons removed or added to each ion (its charge number) |
| $e$ | electron charge, $1.6\times10^{-19}\ \text{C}$ |
| $\varepsilon_0$ | permittivity of free space, $8.85\times10^{-12}\ \text{C}^2/(\text{N}\cdot\text{m}^2)$ |
| $b$ | a constant |
| $n$ | Born exponent, between 5 and 9 |
| $a$ | distance between the ions |

If attraction is counted as positive and repulsion as negative, the net force is zero at one particular distance, $a_0$. Just beyond $a_0$ the attraction reaches a **maximum**: the largest force the pair can withstand before being pulled apart. When the two ions touch, $a_0$ equals the cation radius plus the anion radius, $r + R$.

### 2.5 Energy of an ion pair [Slide 8]

Force and energy describe the same interaction: the force is the derivative of the energy with respect to distance, $F = \partial E/\partial a$. The net energy of the pair is

$$E_{net} = \underbrace{\frac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 a_0}}_{\text{attraction: energy released}} + \underbrace{\frac{b}{a_0^{\,n}}}_{\text{repulsion: energy absorbed}}$$

Because the two ions have charges of opposite sign, $Z_1 Z_2$ is negative and the attraction term lowers the energy; the repulsion term raises it.

The energy is **lowest** at the **equilibrium distance $a_0$**, where attraction and repulsion balance. This minimum is the same point where the net force is zero.

![[attachments/T1/force-energy.svg]]

> [!info] Checking the link between force and energy
> Differentiating each term of $E_{net}$ with respect to $a$ gives back the two terms of the force:
> $\dfrac{\partial}{\partial a}\left(\dfrac{Z_1Z_2e^2}{4\pi\varepsilon_0}\,a^{-1}\right) = -\dfrac{Z_1Z_2e^2}{4\pi\varepsilon_0 a^2}$ and $\dfrac{\partial}{\partial a}\left(b\,a^{-n}\right) = -\dfrac{n b}{a^{n+1}}$.

### 2.6 Lattice energy [Slide 9]

The **lattice energy U** is the energy involved in bringing one mole of ions from infinitely far apart to their fixed positions in a crystal. An equivalent way to see it: the energy **released** when one mole of ionic solid forms from its ions in the gas state.

It follows from the energy of one pair at equilibrium:

$$E_{r=a_0} = \frac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 a_0} + \frac{b}{a_0^{\,n}} \quad\Longrightarrow\quad U = -\frac{Z_1 Z_2 e^2 N_A A}{4\pi\varepsilon_0 a_0}\left(1-\frac{1}{n}\right)$$

where $N_A$ is Avogadro's number (one mole of ion pairs) and $A$ is a constant that depends on the crystal.

> [!info] Where the factor $(1 - 1/n)$ comes from
> 1. At $a_0$ the force is zero: $-\dfrac{Z_1Z_2e^2}{4\pi\varepsilon_0 a_0^2} - \dfrac{n b}{a_0^{n+1}} = 0$.
> 2. Multiplying by $a_0^{n+1}$ and solving for $b$: $b = -\dfrac{Z_1Z_2e^2 a_0^{n-1}}{4\pi\varepsilon_0\, n}$.
> 3. The repulsion term then becomes $\dfrac{b}{a_0^n} = -\dfrac{Z_1Z_2e^2}{4\pi\varepsilon_0 a_0}\cdot\dfrac{1}{n}$.
> 4. Adding the attraction term: $E_{r=a_0} = \dfrac{Z_1Z_2e^2}{4\pi\varepsilon_0 a_0}\left(1-\dfrac{1}{n}\right)$.
> 5. Multiplying by $N_A A$ gives $U$. In the expression for $U$ the charge numbers are taken as positive and the minus sign is written in front, so that $U$ is negative.
>
> With $n$ between 5 and 9, repulsion only takes away between 11 % and 20 % of the attraction energy.

The lattice energy cannot be measured directly, but it can be obtained from steps that can be measured, arranged in a closed loop called the **Born-Haber cycle**. For KCl:

| Step | ΔH (kJ/mol) |
| :--- | ---: |
| Sublimation of K | +89 |
| Ionization of K(g) | +425 |
| Dissociation of Cl₂(g) | +244 |
| Ionization of Cl(g) | −355 |
| Formation of KCl | −438 |

> [!info] Closing the cycle
> Only half a mole of Cl₂ is needed per mole of KCl, so the dissociation step counts 244/2 = 122 kJ/mol. Going from K(s) + ½Cl₂(g) to the gas ions and then down to KCl(s), the lattice energy is what closes the loop:
> $$U = -438 - (89 + 425 + 122 - 355) = -438 - 281 = -719\ \text{kJ/mol}$$

### 2.7 Properties that depend on the lattice energy [Slides 10-13]

The stronger the bond (the larger the lattice energy), the more energy it takes to separate the ions. Four properties follow from this.

#### Melting point [Slide 10]

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

(All the energies are negative; the table gives their size.)

- **Same valence (+1):** larger ions → lower lattice energy → lower melting point.
- **Higher valence (+2):** more charge → much higher lattice energy → much higher melting point. MgO melts at 2800 °C, NaCl at 801 °C.

LiCl does not follow the first trend (it melts lower than NaCl although its U is larger); the trend holds from NaCl to CsCl.

#### Hardness [Slide 11]

**Hardness** measures how well a material resists **localized plastic deformation**, caused by pressing into it (indentation) or by scratching (abrasion). Mineralogists use the Mohs scale.

| | BeO | MgO | CaO | SrO | BaO |
| :--- | ---: | ---: | ---: | ---: | ---: |
| d (Å) | 1.65 | 2.10 | 2.40 | 2.57 | 2.77 |
| Mohs hardness | 9.0 | 6.5 | 4.5 | 3.5 | 3.3 |

For comparison: hydroxyapatite 5, keratin (fingernail) 2.5.

$$\text{smaller cation } (r_{c^+}\downarrow) \;\Rightarrow\; U \uparrow \;\Rightarrow\; \text{harder}$$

The **binding (potential) energy** is the energy needed to create or break the bond; on the energy-distance curve it is the depth of the minimum. Materials with a high binding energy have **high melting temperatures** and are **hard**.

#### Thermal expansion [Slide 12]

**Thermal expansion** is the tendency of matter to change volume when its temperature changes. The **coefficient of thermal expansion** is the change in a linear dimension per degree of temperature, and it is related to the **strength of the bonds**.

When a material is heated, its atoms gain energy and move up inside the energy well:
- in a **deep, narrow** well (strong bonding) the average spacing between atoms barely changes → **low** thermal expansion;
- in a **shallow, wide** well (weak bonding) the spacing grows a lot → **high** thermal expansion.

| | NaF | NaCl | NaBr | NaI |
| :--- | ---: | ---: | ---: | ---: |
| $\alpha_V$ (10⁻⁶ °C⁻¹) | 39 | 40 | 43 | 48 |

For comparison: hydroxyapatite 12·10⁻⁶ °C⁻¹.

$$\text{larger anion } (r_{a^-}\uparrow) \;\Rightarrow\; U \downarrow \;\Rightarrow\; \alpha \uparrow$$

#### Young's modulus [Slide 13]

A high binding energy goes with a **steep** energy curve: a larger force is needed to stretch the bonds, so the **elastic (Young's) modulus is higher**. On a force-distance curve this is the slope $dF/da$ where the curve crosses zero: steeper for strong bonds, gentler for weak ones.

### 2.8 General properties of ionic compounds [Slide 14]

1. The strong electrostatic attraction gives **high melting and boiling points**.
2. They are **hard and brittle** at room temperature.
3. They are **electrical insulators**, except when molten or dissolved in water. To carry a current, whole ions have to move, and ions move slowly, so the conductivity is poor.
4. They are **soluble in water**.

### 2.9 How ions are arranged [Slide 15]

- Since the ionic bond is **non-directional**, each ion simply surrounds itself with ions of the opposite charge.
- The arrangement always keeps the solid **electrically neutral** (NaCl and CsCl are typical examples).
- The **smaller the cation compared with the anion**, the **fewer anions** fit around it.
- Ionic compounds are **crystalline solids**.

---

## 3. Covalent bonding [Slides 17-21]

See also [[Concept - Covalent Bonding and Polar Character]].

### 3.1 What a covalent bond is [Slide 17]

- It usually forms between **nonmetals**.
- The atoms **share electrons** instead of transferring them.
- It is **highly directional**, and it leaves **no free electrons**.
- It appears between elements with a **small electronegativity difference**, close to each other in the periodic table.
- The outer **s and p electrons** are shared so that each atom reaches the electron configuration of a **noble gas**.

Simple examples: two H atoms share one pair of electrons to form H–H; two Cl atoms share one pair to form Cl–Cl, and each Cl keeps three lone pairs.

### 3.2 Silicon and silica [Slide 18]

- **Silicon** has a valence of four, so each atom must form **four covalent bonds**. Because these bonds are directional, they point to the corners of a **tetrahedron**, at **109.5°** from each other.
- **Silica (SiO₂)** has the same tetrahedral structure, with covalent bonds between silicon and oxygen.

### 3.3 Properties of covalent materials [Slide 19]

**Covalent solids** are built from a **continuous network** of covalent bonds (diamond, boron nitride, quartz SiO₂, silicon carbide SiC). They are:
- **electrical insulators**, both solid and molten;
- **hard and incompressible**;
- of **high melting point** and non-volatile;
- **insoluble**.

Covalent bonds also hold together individual molecules and polymer chains, which are **substances with covalent bonds** rather than covalent networks.

### 3.4 Polar covalent bonds [Slide 20]

- In a **nonpolar** bond the shared electrons are split **equally** between the two atoms (H–H, Cl–Cl).
- In a **polar** covalent bond the two atoms have **different electronegativities**, so the shared electrons spend more time near one of them (H–Cl). The centres of positive and negative charge no longer coincide.

The size of this separation of charge is the **dipole moment**:

$$\mu = Q \times d$$

with $Q$ the charge and $d$ the distance between the atoms. It is measured in debye: $1\ \text{D} = 3.33\times10^{-30}\ \text{C}\cdot\text{m}$.

How ionic a bond between atoms A and B is depends on their electronegativities $X_A$ and $X_B$:

$$\%\ \text{ionic character} = \left(1 - e^{-0.25\,(X_A - X_B)^2}\right)\times 100\%$$

If $X_A = X_B$, the exponential is 1 and the bond is 0 % ionic (purely covalent). As the difference grows, the exponential goes to 0 and the ionic character approaches 100 %, without ever reaching it: a purely ionic bond is an ideal. HI and HBr are nearly covalent, HF is in between, and KCl or LiF are mostly ionic.

### 3.5 Bond length, bond order and bond energy [Slide 21]

For a given pair of atoms, a **higher bond order** (single → double → triple) makes the bond **shorter**, and a shorter bond is **stronger** (higher bond energy). H₂, F₂ and N₂ follow this rule.

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

(The energies are released when the bond forms, so they are negative.)

---

## 4. Metallic bonding [Slides 23-27]

See also [[Concept - Metallic Bonding and Energy Band Theory]].

### 4.1 What a metallic bond is [Slide 23]

In a metal, the atoms give up their valence electrons, which form a shared **"sea" of electrons**. What remains of each atom is a positive core, and the cores are held together by their attraction to the negative electron sea. In short: the metallic bond is the **electrostatic attraction between metal cations and delocalized electrons**.

- The atoms are **closely packed** in a crystal structure.
- The electrons are spread among all the atoms as an **electron cloud**.
- Since each outer electron is shared by many atoms, the bond is **non-directional**.

### 4.2 Bonding energy and valence electrons [Slide 24]

- Forming metallic bonds **lowers the energy** of the atoms.
- As for any bond, the energy is lowest at the **equilibrium distance $a_0$**.
- **Fewer valence electrons → weaker bond.** Potassium (valence +1): bonding energy 89.6 kJ/mol, melting point 63.5 °C.
- **More valence electrons → stronger bond.** Calcium (valence +2): bonding energy 177 kJ/mol, melting point 851 °C.

Bonding energies and melting points of the fourth-period metals:

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

### 4.3 What metallic bonding means for properties [Slide 25]

- Pure metals are much more **malleable** than ionic or covalent networks. Their strength can be raised considerably by **alloying**.
- Pure metals are **excellent conductors of heat and electricity**: under a voltage, the electrons of the electron sea move freely and carry the current.

### 4.4 Band theory [Slides 26-27]

**Band theory** describes the electrons of a solid, which can only have energies inside certain ranges.

When atoms join into a metallic crystal, the orbitals of the separate atoms combine into a set of orbitals that belong to the whole crystal. Each new atom adds more levels, and with a huge number of atoms the levels are so close together that they form an almost continuous range of energies: a **band**. A piece of metal behaves like a single giant molecule. Lithium shows it: Li, Li₂, Li₃, …, Li_N, with the 2s levels multiplying into a band.

The band structure depends on the **distance between atoms**: the bands form because the outermost orbitals of neighbouring atoms overlap. In lithium and in magnesium this gives a valence band and a conduction band.

> [!warning] Note on the official material
> The magnesium example is labelled "Z = 4, 1s² 2s²". That is the configuration of beryllium; magnesium has Z = 12.

---

## 5. Secondary bonding: intermolecular forces [Slides 29-35]

See also [[Concept - Intermolecular Forces and Secondary Bonds]].

### 5.1 Primary bonds are strong [Slide 29]

| Primary bond | Energy (kcal/mol) | Mechanism |
| :--- | :--- | :--- |
| Ionic | 150-370 | electrons transferred → cations and anions → Coulomb force (non-directional) |
| Covalent | 125-300 | electrons shared (directional) |
| Metallic | 25-200 | electrons shared by all the atoms, held only loosely by the nuclei (non-directional) |

### 5.2 Secondary bonds are weak [Slide 30]

**Secondary (van der Waals) bonds** are attractions between **electric dipoles** in atoms or molecules. A dipole appears when the electron charge is spread **unevenly**, so that the centre of positive charge and the centre of negative charge are in different places.

There are two kinds of dipole:
- **permanent dipoles**, which do not change with time;
- **fluctuating dipoles**, which appear and disappear as the electron cloud changes with time.

### 5.3 Permanent dipoles (1-10 kcal/mol) [Slide 31]

They form in molecules that:
- have a **constant dipole moment μ**, and
- are made of atoms of **different electronegativity** joined by **covalent** bonds.

Whether a molecule has a dipole depends on its shape:
- **CH₄:** the four C–H bonds are arranged **symmetrically**; their effects cancel and there is **no dipole moment**.
- **CH₃Cl:** replacing one H by Cl makes the tetrahedron **asymmetrical**, and the molecule **has a dipole**.

### 5.4 Example: PVC [Slide 32]

In polyvinyl chloride (PVC) the chlorine atoms along the chain carry a negative charge and the hydrogen atoms a positive one. Neighbouring chains therefore attract each other through van der Waals bonds, and this extra bonding makes PVC **stiffer**. When a force is applied, these weak bonds break and the chains **slide past one another**.

### 5.5 The hydrogen bond (≈ 7 kcal/mol in water) [Slide 33]

The **hydrogen bond** is a strong case of permanent dipole. When hydrogen is bonded to a very **electronegative atom** (O–H, N–H, F–H), the charge is distributed very unevenly: the bond is polar and forms a permanent dipole. A hydrogen bond is the **dipole-dipole attraction between polar bonds that contain hydrogen**.

In **water**, the two hydrogens are not in a straight line with the oxygen (the H–O–H angle is about 105°), so the molecule is a dipole. The **oxygen** is the **negative** end and the **hydrogens** the **positive** end, and the hydrogen of one molecule is attracted to the oxygen of the next.

> [!warning] Note on the official material
> The official text writes "positive oxygen pole and negative hydrogen pole". The signs are swapped: oxygen, being more electronegative, pulls the shared electrons and is the negative pole.

### 5.6 Fluctuating dipoles (< 2 kcal/mol) [Slide 34]

Even **nonpolar** molecules attract each other weakly. At any instant the electron cloud may be slightly lopsided, creating a short-lived dipole; a moment later it is symmetrical again or lopsided the other way. These **fluctuating dipoles** are the weakest of the secondary bonds.

### 5.7 Example: boiling points of the hydrides [Slide 35]

Going down a group (to higher periods), the boiling points of the hydrides generally rise, because larger atoms with more electrons give stronger forces between the molecules (CH₄ → SiH₄ → GeH₄ → SnH₄).

Water, HF and NH₃ break this trend: their **hydrogen bonds** are much stronger than ordinary van der Waals forces, and so their boiling points are **far higher** than the trend would predict.

---

## 6. Bonding and properties in materials [Slides 37-38]

See also [[Concept - Interatomic Potential Energy Curves and Macroscopic Properties]].

The type of bond largely defines the family of material:

| Type of material | Character of bonding | Examples |
| :--- | :--- | :--- |
| Metals | Metallic | Fe, steels |
| Ceramics and glasses | Ionic / covalent | Silica (SiO₂) |
| Polymers | Covalent and secondary | Polyethylene –(CH₂)– |

Summary of properties by type of bond:

| Bond | Type of substance | Melting and boiling points | Mechanical properties | Solubility |
| :--- | :--- | :--- | :--- | :--- |
| Covalent | Molecular | Low | Soft in the solid state | Depends on the polarity of the molecules |
| Covalent | Atomic network (lattice) | Very high | Very hard, brittle | Insoluble in all solvents |
| Ionic | Ionic | High | Hard and brittle | Soluble in polar solvents |
| Metallic | Metallic | High | Ductile and workable | Insoluble in all solvents |

---

## 7. Questions [Slide 39]

1. Compare metallic and covalent primary bonds: nature of the bond, valence of the atoms involved, and ductility of the materials → [[Problem - T1 Exam Question 1 Metallic vs Covalent Bonding]]
2. Titanium is stiffer than aluminium, has a lower thermal expansion coefficient and a higher melting temperature. Sketch both potential-well curves on the same graph and show how these properties appear in them → [[Problem - T1 Exam Question 2 Potential Curves Titanium vs Aluminium]]
3. Would MgO or magnesium have the higher modulus of elasticity? → [[Problem - T1 Exam Question 3 Elastic Modulus MgO vs Mg]]
4. Aluminium and silicon are neighbours in the periodic table. Which would have the higher modulus of elasticity? → [[Problem - T1 Exam Question 4 Elastic Modulus Aluminium vs Silicon]]

---

**Back to:** [[Aerospace Materials I MOC]]
