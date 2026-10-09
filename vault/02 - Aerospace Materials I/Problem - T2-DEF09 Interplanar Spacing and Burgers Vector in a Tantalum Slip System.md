---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 9"
dificultad: medium
tags:
  - official-problem
  - solved
  - tantalum
  - bcc
  - slip-systems
  - burgers-vector
  - interplanar-spacing
---

# ✏️ Problem: T2-DEF09 — Interplanar Spacing and Burgers Vector Magnitude in a Tantalum Slip System

## 📄 Official Statement
> **9. a) Determine the interplanar spacing and the length of the Burgers vector for slipping in the slip system $(110) / [1\,\bar{1}\,1]$ in BCC tantalum.**  
> **b) Repeat assuming that the slip system is $(111) / [1\,\bar{1}\,0]$.**  
> **Data: $a = 3.3026\text{ \AA}$.**  
> *(Solution: a) $b = 2.860\text{ \AA}$, $d_{(110)} = 2.335\text{ \AA}$; b) $b = 4.671\text{ \AA}$, $d_{(111)} = 1.907\text{ \AA}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Material and Lattice Parameter:
* Element: Pure tantalum ($\text{Ta}$), a high-density refractory metal.
* Structure: Body-Centred Cubic (BCC).
* Lattice parameter: $a = 3.3026\text{ \AA} = 0.33026\text{ nm}$.

### Slip Systems Evaluated:
1. **Real System (Part a):** Plane $(110)$ and direction $[1\,\bar{1}\,1]$.
2. **Hypothetical System (Part b):** Plane $(111)$ and direction $[1\,\bar{1}\,0]$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

1. **Interplanar Spacing in Cubic Crystals [Session 3 Slide 53]:**
   $$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$
2. **Magnitude of the Burgers Vector ($\vec{b}$) in Cubic Lattices [Session 4 Slide 35]:**
   * Along the slip direction $[1\,\bar{1}\,1]$ (direction of maximum packing in BCC), the minimum lattice translation vector joins a vertex with the cube centre:
     $$\vec{b}_a = \frac{a}{2}[1\, -1\, 1] \implies |\vec{b}_a| = \frac{a\sqrt{1^2 + (-1)^2 + 1^2}}{2} = \frac{a\sqrt{3}}{2}$$
   * Along the hypothetical slip direction $[1\,\bar{1}\,0]$ (face diagonal in BCC), the cell centre does not interrupt the diagonal; the full elementary translation vector joins two opposite vertices of a square face:
     $$\vec{b}_b = a[1\, -1\, 0] \implies |\vec{b}_b| = a\sqrt{1^2 + (-1)^2 + 0^2} = a\sqrt{2}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Part a: Real System $(110) / [1\,\bar{1}\,1]$
* **Interplanar Spacing $d_{(110)}$:**
  $$d_{(110)} = \frac{a}{\sqrt{1^2 + 1^2 + 0^2}} = \frac{a}{\sqrt{2}} = \frac{3.3026\text{ \AA}}{\sqrt{2}} = \frac{3.3026}{1.4142136} = \mathbf{2.3353\text{ \AA}} \approx \mathbf{2.335\text{ \AA}}$$

* **Burgers Vector Length $|\vec{b}|$:**
  $$|\vec{b}| = \frac{a\sqrt{3}}{2} = \frac{3.3026\text{ \AA} \times 1.7320508}{2} = \frac{5.72027}{2} = \mathbf{2.8601\text{ \AA}} \approx \mathbf{2.860\text{ \AA}}$$

---

### 2. Part b: Hypothetical System $(111) / [1\,\bar{1}\,0]$
* **Interplanar Spacing $d_{(111)}$:**
  $$d_{(111)} = \frac{a}{\sqrt{1^2 + 1^2 + 1^2}} = \frac{a}{\sqrt{3}} = \frac{3.3026\text{ \AA}}{1.7320508} = \mathbf{1.90676\text{ \AA}} \approx \mathbf{1.907\text{ \AA}}$$
  *(Note that in the official solutions sheet the typographical error appears labelled as $d_{(110)} = 1.907\text{ \AA}$, when it corresponds to the $(111)$ plane).*

* **Burgers Vector Length $|\vec{b}|$:**
  $$|\vec{b}| = a\sqrt{2} = 3.3026\text{ \AA} \times 1.4142136 = \mathbf{4.67058\text{ \AA}} \approx \mathbf{4.671\text{ \AA}}$$

---

## 🎯 4. Phase 4: Units and Limits

Comparison of the two systems analysed:

| Physical Parameter | Real System: $(110)/[1\bar{1}1]$ | Hypothetical System: $(111)/[1\bar{1}0]$ | Comparison |
| :--- | :--- | :--- | :--- |
| **Interplanar Spacing $d_{hkl}$** | $\mathbf{2.335\text{ \AA}}$ (Larger) | $1.907\text{ \AA}$ (Smaller) | $d_{(110)} > d_{(111)}$ |
| **Burgers Vector Magnitude $|\vec{b}|$** | $\mathbf{2.860\text{ \AA}}$ (Smaller) | $4.671\text{ \AA}$ (Larger) | $|\vec{b}_{\text{real}}| \ll |\vec{b}_{\text{hipotético}}|$ |
| **Dislocation Energy ($E \propto |\vec{b}|^2$)** | $k \times (2.860)^2 = \mathbf{8.18\, k}$ | $k \times (4.671)^2 = \mathbf{21.82\, k}$ | **2.67 times lower energy** |

### Metallurgical Conclusion:
The Peierls-Nabarro stress $\tau_{\text{PN}}$ (the intrinsic resistance of the lattice to dislocation motion) decreases exponentially with the interplanar spacing $d$ and increases with the magnitude of the Burgers vector:
$$\tau_{\text{PN}} \approx 2G \exp\left(-\frac{2\pi d}{|\vec{b}|}\right)$$
The real system $(110)/[1\bar{1}1]$ simultaneously has the **largest interplanar spacing** ($2.335\text{ \AA}$) and the **smallest Burgers vector** ($2.860\text{ \AA}$), making the strain energy almost three times lower and the resistance to motion minimal. For this reason, tantalum and all BCC refractory metals invariably slip in the $\{110\}\langle 111 \rangle$ family.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
