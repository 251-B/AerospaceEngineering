---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 9"
dificultad: high
tags:
  - official-problem
  - solved
  - polymorphism
  - allotropy
  - iron
  - volume-change
  - bragg-spacing
  - planar-density
---

# ✏️ Problem: T2-CS09 — Volume Change in the BCC to FCC Polymorphic Transformation

## 📄 Official Statement
> **9. A pure metal undergoes a polymorphic change from BCC to FCC when it reaches $910^\circ\text{C}$. Calculate the volume change associated with the change in structure given that the interplanar spacing $d_{321}$ for the BCC structure is $0.07565\text{ nm}$, and the planar density in the FCC lattice in the plane $(002)$ is $15.18 \times 10^{18}\text{ at/m}^2$.**  
> *(Solution: $5.7\text{ \%}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Physical Context:
The problem models the classic allotropic transformation of pure iron at the $A_3$ austenitisation point at $910^\circ\text{C}$ [Session 4 Slide 49]:
$$\alpha\text{-Fe (BCC)} \xrightarrow{910^\circ\text{C}} \gamma\text{-Fe (FCC)}$$

### Input Data:
* **BCC phase (low temperature):**
  * Interplanar spacing of the $(321)$ family: $d_{321}^{\text{BCC}} = 0.07565\text{ nm} = 0.7565\text{ \AA}$.
  * Number of atoms per unit cell: $n_{\text{BCC}} = 2$.
* **FCC phase (high temperature):**
  * Planar density on the $(002)$ plane: $\rho_{(002)}^{\text{FCC}} = 15.18 \times 10^{18}\text{ at/m}^2 = 15.18\text{ at/nm}^2$.
  * Number of atoms per unit cell: $n_{\text{FCC}} = 4$.

### Definition of the Volume Change:
The volume change is defined by the percentage variation of the **volume per atom ($V_{\text{at}}$)**, or mean atomic volume, between the two phases:
$$\frac{\Delta V}{V_{\text{BCC}}} = \frac{V_{\text{at}}^{\text{FCC}} - V_{\text{at}}^{\text{BCC}}}{V_{\text{at}}^{\text{BCC}}} \times 100\%$$

---

## 🧠 2. Phase 2: Frames and Change of Basis

1. **Lattice Parameter of the BCC Phase ($a_{\text{BCC}}$):**
   From the interplanar spacing formula for cubic lattices [Session 3 Slide 53]:
   $$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}} \implies a_{\text{BCC}} = d_{321} \cdot \sqrt{3^2 + 2^2 + 1^2} = d_{321} \cdot \sqrt{14}$$
   The volume per atom in BCC is:
   $$V_{\text{at}}^{\text{BCC}} = \frac{V_C^{\text{BCC}}}{n_{\text{BCC}}} = \frac{a_{\text{BCC}}^3}{2}$$

2. **Lattice Parameter of the FCC Phase ($a_{\text{FCC}}$):**
   The $(002)$ plane is perpendicular to the $z$ axis, located at mid-height $z = a/2$. In an FCC cell, it contains the centres of the 4 surrounding faces (each shared by two cells $\implies 4 \times 1/2 = 2$ net atoms) over an area $A = a_{\text{FCC}}^2$ [Session 4 Slide 8]:
   $$\rho_{(002)} = \frac{2}{a_{\text{FCC}}^2} \implies a_{\text{FCC}} = \sqrt{\frac{2}{\rho_{(002)}}}$$
   The volume per atom in FCC is:
   $$V_{\text{at}}^{\text{FCC}} = \frac{V_C^{\text{FCC}}}{n_{\text{FCC}}} = \frac{a_{\text{FCC}}^3}{4}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Calculation in the BCC Structure:
* Calculation of $a_{\text{BCC}}$:
  $$\sqrt{14} \approx 3.741657$$
  $$a_{\text{BCC}} = 0.07565\text{ nm} \times 3.741657 = 0.2830565\text{ nm} = 2.8306\text{ \AA}$$
* BCC unit cell volume:
  $$V_C^{\text{BCC}} = a_{\text{BCC}}^3 = (0.2830565\text{ nm})^3 = 0.0226787\text{ nm}^3$$
* Volume per atom in BCC:
  $$V_{\text{at}}^{\text{BCC}} = \frac{0.0226787\text{ nm}^3}{2} = \mathbf{0.0113394\text{ nm}^3/\text{átomo}}$$

---

### 2. Calculation in the FCC Structure:
* Given planar density: $\rho_{(002)} = 15.18 \times 10^{18}\text{ at/m}^2 = 15.18\text{ at/nm}^2$.
* Area of the FCC cell face:
  $$a_{\text{FCC}}^2 = \frac{2}{\rho_{(002)}} = \frac{2}{15.18\text{ nm}^{-2}} = 0.131752\text{ nm}^2$$
* Lattice parameter $a_{\text{FCC}}$:
  $$a_{\text{FCC}} = \sqrt{0.131752\text{ nm}^2} \approx 0.362977\text{ nm} = 3.6298\text{ \AA}$$
* FCC unit cell volume:
  $$V_C^{\text{FCC}} = a_{\text{FCC}}^3 = (0.362977\text{ nm})^3 = 0.047823\text{ nm}^3$$
* Volume per atom in FCC:
  $$V_{\text{at}}^{\text{FCC}} = \frac{0.047823\text{ nm}^3}{4} = \mathbf{0.0119558\text{ nm}^3/\text{átomo}}$$

---

### 3. Relative Volume Change:
$$\Delta V_{\text{rel}} = \frac{V_{\text{at}}^{\text{FCC}} - V_{\text{at}}^{\text{BCC}}}{V_{\text{at}}^{\text{BCC}}} = \frac{0.0119558 - 0.0113394}{0.0113394}$$
$$\Delta V_{\text{rel}} = \frac{0.0006164}{0.0113394} = +0.05436 \implies \mathbf{+5.4\%}$$

Cross-check without intermediate rounding: $\dfrac{a_{\text{FCC}}^3 / 4}{a_{\text{BCC}}^3 / 2} - 1 = \dfrac{0.047823 / 4}{0.022679 / 2} - 1 = 1.0544 - 1 = +5.4\%$.

> [!warning] Discrepancy with the official solution
> The official key states $5.7\%$. With the data as given ($d_{321}^{\text{BCC}} = 0.07565\text{ nm}$ and $\rho_{(002)}^{\text{FCC}} = 15.18\times10^{18}\text{ at/m}^2$, using $\rho_{(002)} = 2/a_{\text{FCC}}^2$) the result is $+5.4\%$. Rounding the intermediate values to 3-5 significant figures gives $5.4$-$5.5\%$ and never $5.7\%$; no input was altered to force a match.

---

## 🎯 4. Phase 4: Units and Limits

* **Interpretation of the sign and size of the result:** Both phases are compared at the same temperature ($910^\circ\text{C}$), so thermal vibration cannot explain the difference. The positive sign follows only from the data supplied: they give $a_{\text{BCC}} = 0.2831\text{ nm}$ and $a_{\text{FCC}} = 0.3630\text{ nm}$, hence $V_{\text{at}}^{\text{FCC}} > V_{\text{at}}^{\text{BCC}}$. These numbers are those of a hypothetical metal, not of real iron: real iron contracts by roughly $1\%$ in the $\alpha \to \gamma$ transformation, so a close-packed FCC phase is not expected to have a larger atomic volume than BCC. The packing factors ($\text{APF} = 0.74$ for FCC vs $0.68$ for BCC) only apply at equal atomic radius.
* **Dimensional Control in Heat Treatments:** A macroscopic volume jump of this order ($\approx 5.4\%$ with the given data) generates high internal stresses during the cooling of thick aerospace parts made of carbon or alloy steel, and is the primary cause of possible warping or cracking during quenching.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
