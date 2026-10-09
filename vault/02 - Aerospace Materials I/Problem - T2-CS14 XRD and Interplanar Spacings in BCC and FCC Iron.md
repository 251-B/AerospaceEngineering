---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 14"
dificultad: low
tags:
  - official-problem
  - solved
  - xrd
  - bragg-spacing
  - iron-allotropy
  - bcc
  - fcc
---

# ✏️ Problem: T2-CS14 — XRD Diffraction and Interplanar Spacings in BCC and FCC Iron

## 📄 Official Statement
> **14. Fe has a BCC or an FCC structure, depending on the temperature. The X-ray diffraction (XRD) technique allows determining the spacing or distances between crystalline planes, from which the lattice parameters are deduced. For the BCC structure, the lattice parameter is $a = 0.2864\text{ \AA}$, while for the FCC $a = 0.3592\text{ \AA}$.**  
> *(Note: the official text labels these values in angstroms, but $0.2864\text{ \AA}$ would be smaller than an atom. They are nanometres: $a_{\alpha\text{-Fe}} = 0.2864\text{ nm} = 2.864\text{ \AA}$ and $a_{\gamma\text{-Fe}} = 0.3592\text{ nm} = 3.592\text{ \AA}$. The official answers below carry the same unit slip, i.e. they read $0.143\text{ nm}$, $0.179\text{ nm}$, $0.2025\text{ nm}$, $0.207\text{ nm}$. This solution works in nm.)*  
> **a)** What distance can be expected between the planes $(020)$ for both structures?  
> **b)** Calculate the distance between the most compact planes of both structures.  
> *(Solution: a) $d_{020}(\text{BCC}) = 0.143\text{ \AA}$; $d_{020}(\text{FCC}) = 0.179\text{ \AA}$; b) $\text{BCC } (110) = 0.2025\text{ \AA}$; $\text{FCC } (111) = 0.207\text{ \AA}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Lattice parameter of the BCC phase ($\alpha\text{-Fe}$): $a_{\text{BCC}} = 0.2864\text{ nm}$.
* Lattice parameter of the FCC phase ($\gamma\text{-Fe}$): $a_{\text{FCC}} = 0.3592\text{ nm}$.
* Planes of Maximum Packing [Session 4 Slide 9]:
  * In the BCC structure: densest planes $\{110\}$.
  * In the FCC structure: densest planes $\{111\}$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

For any crystal with cubic symmetry, the interplanar spacing $d_{hkl}$ separating two parallel planes of the same Miller family is given by the fundamental relation [Session 3 Slide 53]:

$$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$

* For the $(020)$ plane:
  $$d_{020} = \frac{a}{\sqrt{0^2 + 2^2 + 0^2}} = \frac{a}{2}$$
* For the most densely packed plane of BCC $(110)$:
  $$d_{110}^{\text{BCC}} = \frac{a_{\text{BCC}}}{\sqrt{1^2 + 1^2 + 0^2}} = \frac{a_{\text{BCC}}}{\sqrt{2}}$$
* For the most densely packed plane of FCC $(111)$:
  $$d_{111}^{\text{FCC}} = \frac{a_{\text{FCC}}}{\sqrt{1^2 + 1^2 + 1^2}} = \frac{a_{\text{FCC}}}{\sqrt{3}}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Part a: Distance between $(020)$ Planes
* **For the BCC Structure:**
  $$d_{020}(\text{BCC}) = \frac{a_{\text{BCC}}}{2} = \frac{0.2864\text{ nm}}{2} = \mathbf{0.1432\text{ nm}} \approx \mathbf{0.143\text{ nm}}$$

* **For the FCC Structure:**
  $$d_{020}(\text{FCC}) = \frac{a_{\text{FCC}}}{2} = \frac{0.3592\text{ nm}}{2} = \mathbf{0.1796\text{ nm}} \approx \mathbf{0.180\text{ nm}}$$

---

### 2. Part b: Distance between the Most Densely Packed Planes
* **BCC Structure ($(110)$ plane):**
  $$d_{110}(\text{BCC}) = \frac{a_{\text{BCC}}}{\sqrt{2}} = \frac{0.2864\text{ nm}}{1.4142136} = \mathbf{0.20252\text{ nm}} \approx \mathbf{0.2025\text{ nm}}$$

* **FCC Structure ($(111)$ plane):**
  $$d_{111}(\text{FCC}) = \frac{a_{\text{FCC}}}{\sqrt{3}} = \frac{0.3592\text{ nm}}{1.7320508} = \mathbf{0.20738\text{ nm}} \approx \mathbf{0.207\text{ nm}}$$

---

## 🎯 4. Phase 4: Units and Limits

1. **Correlation with Bragg's Law:** In an X-ray diffraction test with copper $K\alpha$ radiation ($\lambda = 1.5418\text{ \AA} = 0.15418\text{ nm}$), the diffraction angle $\theta$ is inversely related to $d_{hkl}$:
   $$\sin\theta = \frac{\lambda}{2 d_{hkl}}$$
   Since the most densely packed planes have the **largest interplanar spacing $d_{hkl}$** ($d_{110}^{\text{BCC}} = 0.2025\text{ nm}$, $d_{111}^{\text{FCC}} = 0.207\text{ nm}$), they produce the **first diffraction peak at the smallest angle $2\theta$** and with the highest intensity in the XRD spectrum.
   Bragg angles (Cu $K\alpha$, $\lambda = 0.15418\text{ nm}$, first order; $\lambda$ and $d$ must be in the same unit):
   $$\sin\theta_{110}^{\text{BCC}} = \frac{0.15418\text{ nm}}{2 \times 0.20252\text{ nm}} = 0.3807 \implies \theta = 22.4^\circ \;(2\theta = 44.7^\circ)$$
   $$\sin\theta_{111}^{\text{FCC}} = \frac{0.15418\text{ nm}}{2 \times 0.20738\text{ nm}} = 0.3717 \implies \theta = 21.8^\circ \;(2\theta = 43.6^\circ)$$
   Mixing $\lambda = 1.5418\text{ \AA}$ with $d$ in nm (or the official mislabelled $\text{\AA}$ values) would give the impossible $\sin\theta = 1.5418/(2\times0.2025) = 3.8$.
2. **Very similar spacings:** It is notable that $d_{110}^{\text{BCC}} \approx 0.203\text{ nm}$ and $d_{111}^{\text{FCC}} \approx 0.207\text{ nm}$ are practically identical (difference $\approx 2.4\%$), which confirms that the distances between the densest layers of iron atoms hardly change on crossing the allotropic transformation temperature of $910^\circ\text{C}$.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
