---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 8"
dificultad: high
tags:
  - official-problem
  - solved
  - planar-packing-fraction
  - fcc
  - miller-indices
---

# ✏️ Problem: T2-CS08 — Planar Packing Fraction on FCC Planes

## 📄 Official Statement
> **8. Calculate the fraction of area occupied by atoms for the $(111)$, $(200)$, $(220)$, $(222)$, $(400)$ and $(420)$ planes, in the FCC structure.**  
> *(Solution: $(111): \pi/(2\sqrt{3})$; $(200): \pi/4$; $(220): \pi\sqrt{2}/8$; $(222): 0$; $(400): 0$; $(420): \pi/(4\sqrt{5})$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Lattice Model:
* Structure: Face-Centred Cubic (FCC).
* Fundamental contact relation along $\langle 110 \rangle$:
  $$a = 2\sqrt{2} R \implies R = \frac{a}{2\sqrt{2}} = \frac{a\sqrt{2}}{4}$$
* Cross-sectional area of each spherical atom of radius $R$:
  $$A_{\text{átomo}} = \pi R^2$$

---

## 🧠 2. Phase 2: Frames and Change of Basis

The **Fraction of Area Occupied by Atoms (Planar Packing Fraction, PPF)** on a crystallographic plane $(h\, k\, l)$ is defined as the ratio between the total area of the circular sections of the atoms whose centres fall exactly on that plane and the total geometric area of the plane inside the unit cell [Session 4 Slide 8]:

$$\text{PPF}_{(hkl)} = \frac{N_{\text{átomos}} \cdot (\pi R^2)}{A_{(hkl)}}$$

* If a plane passes between atomic planes and **does not cut the centre of any atom**, the number of atoms contained is zero and $\text{PPF} = 0$.

---

## 🔢 3. Phase 3: Step-by-Step Derivation for Each Plane

### 1. $(111)$ Plane:
* **Geometry:** Equilateral triangle with edge $L = a\sqrt{2} = 4R$.
* **Area:** $A_{(111)} = \frac{\sqrt{3}}{4} L^2 = \frac{\sqrt{3}}{4}(4R)^2 = 4\sqrt{3} R^2$.
* **Atoms contained:** 3 vertices $\times \frac{1}{6} + 3$ side centres $\times \frac{1}{2} = 2\text{ átomos}$.
* **Atomic area:** $2 \times (\pi R^2) = 2\pi R^2$.
$$\text{PPF}_{(111)} = \frac{2\pi R^2}{4\sqrt{3} R^2} = \mathbf{\frac{\pi}{2\sqrt{3}}} \approx \mathbf{0.9069} \quad (90.7\%)$$

---

### 2. $(200)$ Plane:
* **Position:** Plane parallel to $(100)$ located at mid-edge: $x = a/2$.
* **Area:** Square cross-section of the cell: $A_{(200)} = a^2$.
* **Atoms contained at $x = a/2$:**
  In an FCC lattice, the central plane perpendicular to the $x$ axis contains the atoms at the centres of the 4 surrounding faces (positions $(a/2, 1/2, 0)$, $(a/2, 0, 1/2)$, $(a/2, 1, 1/2)$, $(a/2, 1/2, 1)$).
  Each one lies at the midpoint of an edge of this square of side $a$, contributing $\frac{1}{2}$:
  $$N_{\text{átomos}} = 4 \times \frac{1}{2} = 2\text{ átomos}$$
* Knowing that $a = 2\sqrt{2} R \implies a^2 = 8R^2$:
$$\text{PPF}_{(200)} = \frac{2 \cdot \pi R^2}{a^2} = \frac{2\pi R^2}{8R^2} = \mathbf{\frac{\pi}{4}} \approx \mathbf{0.7854} \quad (78.5\%)$$

---

### 3. $(220)$ Plane:
* **Position:** Plane perpendicular to the face diagonal $[110]$ that intersects the axes at $x = a/2, y = a/2$.
* **Area:** Rectangle of base $\frac{a\sqrt{2}}{2} = \frac{a}{\sqrt{2}}$ and height $a \implies A_{(220)} = \frac{a^2}{\sqrt{2}} = \frac{a^2\sqrt{2}}{2}$.
* **Atoms contained:** It contains 2 face centres of the top and bottom faces $\implies 1\text{ átomo}$ net.
* Knowing that $a^2 = 8R^2 \implies A_{(220)} = \frac{8R^2}{\sqrt{2}} = 4\sqrt{2} R^2$:
$$\text{PPF}_{(220)} = \frac{1 \cdot \pi R^2}{4\sqrt{2} R^2} = \frac{\pi}{4\sqrt{2}} = \mathbf{\frac{\pi\sqrt{2}}{8}} \approx \mathbf{0.5554} \quad (55.5\%)$$

---

### 4. $(222)$ Plane:
* **Position:** Plane parallel to $(111)$ with intercepts at $x = a/2, y = a/2, z = a/2$.
* **Atoms contained:** In a perfect FCC lattice, the plane $x+y+z = a/2$ **does not pass through any atomic centre** (atoms sit at whole vertices and face centres $(1/2, 1/2, 0)$, whose sum of fractional coordinates is $0$, $1$ or $2$, never $1/2$).
* Therefore, $N_{\text{átomos}} = 0$:
$$\text{PPF}_{(222)} = \mathbf{0}$$

---

### 5. $(400)$ Plane:
* **Position:** Plane parallel to $(100)$ located at $x = a/4$.
* **Atoms contained:** At $x = a/4$ there is no FCC lattice site (atoms are only at $x = 0, a/2, a$).
* Therefore, $N_{\text{átomos}} = 0$:
$$\text{PPF}_{(400)} = \mathbf{0}$$

---

### 6. $(420)$ Plane:
* **Position:** It intersects the axes at $x = a/4, y = a/2, z = \infty$.
* **Plane area:** Rectangle of base length $\sqrt{(a/4)^2 + (a/2)^2} = \sqrt{\frac{5}{16}}a = \frac{a\sqrt{5}}{4}$ and height $a$:
  $$A_{(420)} = \frac{\sqrt{5}}{4}a^2$$
* **Atoms contained:** It contains the face centre $(a/2, 0, a/2)$, contributing $1/2$ atom inside the cut:
  $$N_{\text{átomos}} = \frac{1}{2}\text{ átomo}$$
* Knowing that $a^2 = 8R^2 \implies A_{(420)} = \frac{\sqrt{5}}{4}(8R^2) = 2\sqrt{5} R^2$:
$$\text{PPF}_{(420)} = \frac{\frac{1}{2}\pi R^2}{2\sqrt{5} R^2} = \mathbf{\frac{\pi}{4\sqrt{5}}} \approx \mathbf{0.3512} \quad (35.1\%)$$

---

## 🎯 4. Phase 4: Units and Limits, with Comparative Summary

| Plane $(hkl)$ | Atoms in the Plane | Plane Area in the Cell | Analytical PPF | Percentage PPF | Physical Meaning |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **$(111)$** | 2 | $4\sqrt{3}R^2$ | $\mathbf{\frac{\pi}{2\sqrt{3}}}$ | **90.7%** | Closest-packed possible plane of rigid spheres |
| **$(200)$** | 2 | $8R^2$ | $\mathbf{\frac{\pi}{4}}$ | **78.5%** | Dense atomic plane parallel to the faces |
| **$(220)$** | 1 | $4\sqrt{2}R^2$ | $\mathbf{\frac{\pi\sqrt{2}}{8}}$ | **55.5%** | Mid-diagonal plane |
| **$(222)$** | 0 | — | $\mathbf{0}$ | **0%** | Passes between close-packed $\{111\}$ planes |
| **$(400)$** | 0 | — | $\mathbf{0}$ | **0%** | Plane in the empty interatomic spacing |
| **$(420)$** | 1/2 | $2\sqrt{5}R^2$ | $\mathbf{\frac{\pi}{4\sqrt{5}}}$ | **35.1%** | Oblique low-density plane |

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
