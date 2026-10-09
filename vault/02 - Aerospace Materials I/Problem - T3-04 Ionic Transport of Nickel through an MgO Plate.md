---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
origen: "Problems T3_Diffusion.pdf, Problem 4"
dificultad: high
tags:
  - official-problem
  - solved
  - ficks-first-law
  - ceramic-diffusion
  - steady-state
  - ionic-transport
  - mgo
  - fcc-nickel
---

# ✏️ Problem: T3-04 — Ionic Transport of Nickel through a Ceramic MgO Plate

## 📄 Official Statement
> **4.- A plate of magnesium oxide of $0.1\text{ cm}$ thickness separates two metallic blocks, one of $\text{Ni}$ and one of $\text{Ta}$. At $1400^\circ\text{C}$ $\text{Ni}$ ions diffuse through the $\text{MgO}$ plate. The diffusion coefficient of $\text{Ni}$ in $\text{MgO}$ is $9 \times 10^{-12}\text{ cm}^2/\text{s}$ and the lattice parameter of (fcc) $\text{Ni}$ at $1400^\circ\text{C}$ is $3.6 \times 10^{-8}\text{ cm}$. Determine the time necessary for sufficient $\text{Ni}^{2+}$ ions to pass through the ceramic material so that the thickness of the block of $\text{Ni}$ is reduced by one micron.**  
> *(Solution: $t = 309\text{ h}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Physical Hypotheses:
1. **Quasi-Steady-State Regime:** Because of the relatively large thickness of the magnesium oxide ceramic plate ($\Delta x = 0.1\text{ cm} = 1000\ \mu\text{m}$) compared with the microscopic reduction of the nickel block ($\Delta h = 1\ \mu\text{m}$), the transport of $\text{Ni}^{2+}$ cations through the ceramic takes place under **steady-state** conditions according to Fick's First Law [Session 5 Slides 16-17].
2. **Boundary Conditions at the Interfaces:**
   * At the left interface ($\text{Ni}/\text{MgO}$ at $x = 0$): the magnesium oxide is in intimate contact with the pure metallic nickel block, so the volumetric concentration of nickel available at the interface equals the atomic density of metallic nickel: $C_1 = \rho_{\text{at, Ni}}$.
   * At the right interface ($\text{MgO}/\text{Ta}$ at $x = \Delta x$): tantalum acts as a perfect sink, instantly consuming or reacting with the emerging nickel ions to form intermetallics or dissolve, fixing a practically zero concentration: $C_2 \approx 0$ [Slide 16].
3. **Crystal Structure of Nickel:** At $1400^\circ\text{C}$, metallic nickel crystallises in a Face-Centred Cubic (FCC) lattice, with $n = 4$ atoms per unit cell and lattice parameter $a = 3.6 \times 10^{-8}\text{ cm}$ [Session 3 Slide 15; Session 5 Slide 23].

### Input Parameters:
* Thickness of the $\text{MgO}$ plate: $\Delta x = 0.1\text{ cm} = 1.0 \times 10^{-3}\text{ m}$
* System temperature: $T = 1400^\circ\text{C} = 1673.15\text{ K}$
* Diffusion coefficient of $\text{Ni}$ in $\text{MgO}$: $D = 9 \times 10^{-12}\text{ cm}^2/\text{s} = 9 \times 10^{-16}\text{ m}^2/\text{s}$
* Lattice parameter of FCC nickel: $a = 3.6 \times 10^{-8}\text{ cm} = 3.6 \times 10^{-10}\text{ m}$
* Required reduction of the nickel thickness: $\Delta h = 1\ \mu\text{m} = 10^{-4}\text{ cm} = 10^{-6}\text{ m}$

---

## 🧠 2. Phase 2: Frames and Change of Basis

### 1. Atomic Density of the Nickel Block ($\rho_{\text{at, Ni}}$):
In an FCC crystal lattice, the number of atoms per unit cell is $n = 4$, and the cell volume is $V_C = a^3$. The atomic volumetric density of nickel in the metallic block is given by [Session 3 Slide 15]:

$$\rho_{\text{at, Ni}} = \frac{n}{a^3} = \frac{4}{a^3} \quad \left[\frac{\text{átomos}}{\text{cm}^3}\right]$$

### 2. Number of Atoms to Transfer per Unit Area ($N/A$):
To reduce the thickness of the metallic block of area $A$ by an amount $\Delta h$, the volume of nickel that must dissolve and diffuse is:
$$V_{\text{perdido}} = A \cdot \Delta h$$

The total number of nickel atoms required per unit transverse area is:
$$\frac{N}{A} = \rho_{\text{at, Ni}} \cdot \Delta h = \frac{4 \cdot \Delta h}{a^3} \quad \left[\frac{\text{átomos}}{\text{cm}^2}\right]$$

### 3. Steady Diffusive Flux through the Ceramic (Fick's First Law):
According to Fick's First Law [Session 5 Slide 16]:
$$J = -D \frac{\Delta C}{\Delta x} = D \frac{C_1 - C_2}{\Delta x} = D \frac{\rho_{\text{at, Ni}} - 0}{\Delta x} = D \frac{\rho_{\text{at, Ni}}}{\Delta x} \quad \left[\frac{\text{átomos}}{\text{cm}^2\cdot\text{s}}\right]$$

### 4. Fundamental Relation and Cancellation of the Atomic Density:
The constant diffusive flux $J$ represents precisely the rate of atoms crossing the unit area per unit time:
$$J = \frac{N / A}{t}$$

Equating both expressions for the flux:
$$\frac{\rho_{\text{at, Ni}} \cdot \Delta h}{t} = D \frac{\rho_{\text{at, Ni}}}{\Delta x}$$

Note the remarkable analytical result: **the atomic density $\rho_{\text{at, Ni}}$ cancels formally on both sides of the equation**:

$$\frac{\Delta h}{t} = \frac{D}{\Delta x} \implies t = \frac{\Delta x \cdot \Delta h}{D}$$

The surface recession rate of the nickel sheet depends exclusively on the diffusivity in the ceramic barrier and on its thickness.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Explicit Calculation of the Atomic Density of Nickel:
* FCC unit cell volume:
  $$V_C = a^3 = (3.6 \times 10^{-8}\text{ cm})^3 = 4.6656 \times 10^{-23}\text{ cm}^3$$
* Atomic density:
  $$\rho_{\text{at, Ni}} = \frac{4\text{ átomos}}{4.6656 \times 10^{-23}\text{ cm}^3} \approx \mathbf{8.5734 \times 10^{22}\text{ átomos/cm}^3}$$

---

### 2. Number of Atoms per Unit Area for $\Delta h = 1\ \mu\text{m} = 10^{-4}\text{ cm}$:
$$\frac{N}{A} = (8.5734 \times 10^{22}\text{ átomos/cm}^3) \times (10^{-4}\text{ cm}) = \mathbf{8.5734 \times 10^{18}\text{ átomos/cm}^2}$$

---

### 3. Steady Diffusive Flux ($J$):
With $C_1 = 8.5734 \times 10^{22}\text{ átomos/cm}^3$, $C_2 = 0$, $D = 9 \times 10^{-12}\text{ cm}^2/\text{s}$ and $\Delta x = 0.1\text{ cm}$:
$$J = D \frac{C_1}{\Delta x} = (9 \times 10^{-12}\text{ cm}^2/\text{s}) \times \frac{8.5734 \times 10^{22}\text{ átomos/cm}^3}{0.1\text{ cm}}$$
$$J = (9 \times 10^{-12}) \times (8.5734 \times 10^{23}) \approx \mathbf{7.71605 \times 10^{12}\text{ átomos/cm}^2\cdot\text{s}}$$

---

### 4. Required Time ($t$):
$$t = \frac{N / A}{J} = \frac{8.5734 \times 10^{18}\text{ átomos/cm}^2}{7.71605 \times 10^{12}\text{ átomos/cm}^2\cdot\text{s}} \approx \mathbf{1.1111 \times 10^6\text{ s}}$$

Or through the compact expression derived above:
$$t = \frac{\Delta x \cdot \Delta h}{D} = \frac{(0.1\text{ cm}) \times (10^{-4}\text{ cm})}{9 \times 10^{-12}\text{ cm}^2/\text{s}} = \frac{10^{-5}\text{ cm}^2}{9 \times 10^{-12}\text{ cm}^2/\text{s}} = \frac{1}{9} \times 10^7\text{ s} \approx \mathbf{1.1111 \times 10^6\text{ s}}$$

### Conversion to Hours:
$$t = \frac{1.1111 \times 10^6\text{ s}}{3600\text{ s/h}} \approx \mathbf{308.64\text{ h}} \approx \mathbf{309\text{ h}}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Dimensional Analysis:
$$[t] = \frac{[\Delta x] \cdot [\Delta h]}{[D]} = \frac{\text{cm} \cdot \text{cm}}{\text{cm}^2/\text{s}} = \text{s} \quad \checkmark$$

### Physical-Ceramic Interpretation:
1. **Ceramic Diffusion Barrier:** Refractory ceramic oxides such as $\text{MgO}$ (rock-salt $\text{NaCl}$-type crystal structure) have very high lattice energies and strong $\text{Mg}^{2+}\text{--}\text{O}^{2-}$ ionic bonds. For this reason, even though the system is subjected to an extreme temperature of $1400^\circ\text{C}$ (close to the melting of nickel, $T_m = 1452^\circ\text{C}$), the diffusion coefficient of nickel is extremely low ($9 \times 10^{-12}\text{ cm}^2/\text{s}$).
2. **Time Durability:** **$309\text{ hours}$** (almost 13 continuous days) are required to wear away barely one surface micron ($1\ \mu\text{m}$) of nickel. This shows how slow ionic transport is in a dense oxide: diffusion is slower for charged species and in materials with high $T_m$ [Session 5 Slide 27], so the MgO plate acts as an effective diffusion barrier between the two metal blocks.

---

## 🔗 Related Links
* [[Topic 3 - Diffusion in Solids and Mass Transport]] (Master MOC for Topic 3)
* [[Concept - Fick's First Law, Steady-State Diffusion]]
* [[Concept - Diffusion Mechanisms, Vacancies and Interstitials]]
* [[Problem - T3-06 Hydrogen Purification with a Palladium Membrane]]
