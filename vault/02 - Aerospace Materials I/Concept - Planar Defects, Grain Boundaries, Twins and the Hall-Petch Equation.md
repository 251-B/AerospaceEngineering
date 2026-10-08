---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 4 T2 Structure of Materials II_2025.pdf, Slides 38-46"
tags:
  - theory
  - fundamental-concept
  - planar-defects
  - grain-boundaries
  - hall-petch
  - twins
  - stacking-faults
  - surface-energy
dificultad: medium
prerrequisitos:
  - "[[Concept - Dislocations, Burgers Vector and Slip in Metals]]"
---

# 🧱 Concept: Planar Defects, Grain Boundaries, Twins and the Hall-Petch Equation

> **Definition:** **Planar or two-dimensional defects** are interfaces or boundaries that separate a crystalline material into different domains that have the same crystal structure but a different spatial orientation, or that represent discontinuities in the atomic stacking sequence [Slide 38].

---

## 🌾 1. Grain Boundaries

A conventional structural metallic material is not a single crystal but a **polycrystal** made up of millions of individual crystallites called **grains**, formed during simultaneous solidification from multiple independent nuclei [Slide 39-40].

### Structural and Thermodynamic Characteristics [Slide 41]:
* **Boundary width:** It is only **2 to 5 interatomic distances** thick ($0.5\text{--}1.5\text{ nm}$).
* **Atomic mismatch:** In this narrow region, the atoms cannot reach the equilibrium spacing or full coordination.
* **High interfacial energy ($\gamma_{\text{gb}}$):** Because of the lower atomic packing density and distorted bonds, grain boundaries are highly energetic zones:
  * They are preferential paths for **fast atomic diffusion in the solid state** ($D_{\text{gb}} \gg D_{\text{lattice}}$).
  * They are preferred sites for **second-phase precipitation** and impurity segregation.
  * They are chemically reactive (susceptible to **intergranular corrosion** in 2000 and 7000 series aeronautical aluminum alloys).

---

## 📈 2. Slip Barrier Effect and the Hall-Petch Equation

When a dislocation moves under an applied stress along its slip plane, it propagates easily through the interior of the grain until it meets a grain boundary [Slide 41]:
1. The slip plane and direction change orientation abruptly on crossing the boundary.
2. The atomic disorder at the boundary destroys the periodic continuity of the slip plane.
3. Dislocations pile up at the grain boundary (**dislocation pile-up**), accumulating a repulsive back-stress that slows the advance of the following dislocations.

### Hall-Petch Equation [Slide 41]:
The smaller the grain size $d$, the larger the total grain-boundary area per unit volume and the shorter the mean free path of dislocations before they are blocked. This increases the yield strength of the material exponentially according to the **Hall-Petch relation**:

$$\sigma_y = \sigma_0 + k_y \cdot d^{-1/2}$$

where:
* $\sigma_y$: apparent yield strength of the polycrystal ($\text{MPa}$).
* $\sigma_0$: lattice friction stress (intrinsic resistance to the motion of an isolated dislocation inside the grain).
* $k_y$: blocking coefficient or Hall-Petch hardening constant ($\text{MPa}\cdot\mu\text{m}^{1/2}$).
* $d$: mean grain diameter (obtained by optical metallography or SEM).

> [!TIP]
> **The Only Mechanism Without a Trade-off:**
> Grain refinement is the only metallurgical hardening mechanism that **simultaneously increases the yield strength ($\sigma_y$) and the fracture toughness / ductility**, while also lowering the ductile-brittle transition temperature (DBTT) in aerospace steels and titanium alloys.

---

## 🪞 2. Twins (Twin Boundaries)

A **twin** is a special planar boundary that separates two crystalline regions whose lattice orientation has a **mirror-symmetry (mirror image)** relationship with respect to a common crystal plane called the *twin plane* [Slide 42].

* **Deformation Twins (Mechanical Twinning):** Produced by severe shear stress or dynamic impact at low temperatures. They are decisive in providing plastic deformability to HCP metals (such as $\text{Ti}$ and $\text{Mg}$) and BCC metals that lack enough active slip systems at low temperature.
* **Annealing Twins:** They are generated during recrystallization heat treatments in FCC metals with low stacking-fault energy (e.g., AISI 304/316 austenitic stainless steels, $\text{Cu-Zn}$ brasses [Slide 43]).

---

## 📑 3. Stacking Faults

A stacking fault is a local interruption of one or two atomic layers in the regular periodic close-packed stacking sequence [Slide 44]:

* **Perfect sequence in FCC:** $\dots ABC\, ABC\, ABC \dots$
* **Intrinsic stacking fault in FCC:**
  $$\dots ABC\, AB\, ABC \dots$$
  Note that in the central region the local sequence is $AB\, AB$, which coincides exactly with the sequence of an **HCP** structure. Therefore, a stacking fault in an FCC crystal is an ultrathin atomic sheet of HCP symmetry.
* **Stacking-Fault Energy (SFE):** Metals with low SFE (such as brass or stainless steel) dissociate their full dislocations into **Shockley partial dislocations**, preventing cross-slip and giving a high strain-hardening rate.

---

## 🌐 4. External Surfaces and Surface Energy ($\gamma_s$)

The external surface that confines any crystalline solid is the terminal planar defect [Slide 45]:
* Surface atoms lack their outer neighbors: their **coordination number is lower** than in the bulk ($\text{NC}_{\text{surf}} < \text{NC}_{\text{bulk}}$).
* These broken or unsatisfied atomic bonds accumulate an excess of elastic and electrostatic energy called the **surface free energy ($\gamma_s$)**:
  $$E_{\text{surface}} > E_{\text{bulk}}$$
* Thermodynamically, materials tend to minimize their exposed surface area to reduce their total free energy (driving force of the sintering of ceramic and metal powders in aerospace powder metallurgy).

---
*Bidirectional Links:*
* [[Concept - Dislocations, Burgers Vector and Slip in Metals|⬅️ Previous: Dislocations and Slip]]
* [[Concept - Polymorphism and Allotropy in Metals and Ceramics|Next: Polymorphism and Allotropy ➡️]]
