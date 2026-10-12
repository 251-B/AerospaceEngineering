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
  $$A_{\text{atom}} = \pi R^2$$

---

### Parameters:
| Quantity | Symbol | Value | SI unit |
| :--- | :--- | :--- | :--- |
| Lattice parameter | $a$ | not given (results are ratios) | m |
| Atomic radius | $R$ | $a\sqrt{2}/4$ | m |
| Atoms per cell | $n$ | $8 \cdot \tfrac18 + 6 \cdot \tfrac12 = 4$ | dimensionless |
| FCC sites (units of $a$) | | corners $(0/1, 0/1, 0/1)$; face centres $(\tfrac12,\tfrac12,0/1)$, $(\tfrac12,0/1,\tfrac12)$, $(0/1,\tfrac12,\tfrac12)$ | dimensionless |

Hypotheses: hard spheres of radius $R$; an atom counts for a plane only if its centre lies on the plane, and it then contributes a circle of radius $R$; each plane is evaluated over its section with one unit cell, with the usual sharing fractions for atoms on the boundary of the section (corner of a triangle $60^\circ/360^\circ = \tfrac16$, corner of a rectangle $\tfrac14$, side $\tfrac12$).

---

## 🧠 2. Phase 2: Frames and Change of Basis

The **Fraction of Area Occupied by Atoms (Planar Packing Fraction, PPF)** on a crystallographic plane $(h\, k\, l)$ is defined as the ratio between the total area of the circular sections of the atoms whose centres fall exactly on that plane and the total geometric area of the plane inside the unit cell [Session 4 Slide 9]:

$$\text{PPF}_{(hkl)} = \frac{N_{\text{atoms}} \cdot (\pi R^2)}{A_{(hkl)}}$$

* If a plane passes between atomic planes and **does not cut the centre of any atom**, the number of atoms contained is zero and $\text{PPF} = 0$.

---

## 🔢 3. Phase 3: Step-by-Step Derivation for Each Plane

Each plane is written from its intercepts $1/h,\ 1/k,\ 1/l$ (in units of $a$) as $hx + ky + lz = 1$ [Session 3 Slides 44, 48], and the FCC sites that satisfy that equation are the atoms of the plane. Throughout, $a^2 = (2\sqrt{2}R)^2 = 8R^2$.

### 1. $(111)$ Plane: $x + y + z = 1$
* **Geometry:** the section is the equilateral triangle with vertices $(1,0,0)$, $(0,1,0)$, $(0,0,1)$ and edge equal to a face diagonal, $L = a\sqrt{2} = 2\sqrt{2}R\cdot\sqrt{2} = 4R$.
* **Area:**
  $$A_{(111)} = \frac{\sqrt{3}}{4} L^2 = \frac{\sqrt{3}}{4}(4R)^2 = \frac{\sqrt{3}}{4}\cdot 16R^2 = 4\sqrt{3}\, R^2$$
* **Atoms:** the 3 corners (sum of coordinates $1$) at the vertices, each $\tfrac16$, and the 3 face centres $(\tfrac12,\tfrac12,0)$, $(\tfrac12,0,\tfrac12)$, $(0,\tfrac12,\tfrac12)$ (sum $\tfrac12 + \tfrac12 = 1$) at the midpoints of the sides, each $\tfrac12$:
  $$N = 3 \cdot \tfrac16 + 3 \cdot \tfrac12 = \tfrac12 + \tfrac32 = 2 \text{ atoms}$$
* **Fraction:**
  $$\text{PPF}_{(111)} = \frac{2\pi R^2}{4\sqrt{3}R^2} = \frac{\pi}{2\sqrt{3}} = \frac{3.14159}{3.46410} = 0.9069 \quad (90.7\%)$$

---

### 2. $(200)$ Plane: $2x = 1$, i.e. $x = \tfrac12$
* **Geometry:** intercepts $x = \tfrac12$, $y = z = \infty$: the square section of side $a$ through the middle of the cell, parallel to the $(100)$ faces.
* **Area:** $A_{(200)} = a^2 = 8R^2$.
* **Atoms:** sites with $x = \tfrac12$ are the face centres $(\tfrac12,0,\tfrac12)$, $(\tfrac12,1,\tfrac12)$, $(\tfrac12,\tfrac12,0)$, $(\tfrac12,\tfrac12,1)$. Each lies at the midpoint of a side of the square and is shared with the neighbouring cell, so it counts $\tfrac12$:
  $$N = 4 \cdot \tfrac12 = 2 \text{ atoms}$$
* **Fraction:**
  $$\text{PPF}_{(200)} = \frac{2\pi R^2}{8R^2} = \frac{\pi}{4} = 0.7854 \quad (78.5\%)$$

---

### 3. $(220)$ Plane: $2x + 2y = 1$, i.e. $x + y = \tfrac12$
* **Geometry:** intercepts $x = \tfrac12$, $y = \tfrac12$, $z = \infty$: a vertical rectangle from $(\tfrac12, 0, z)$ to $(0, \tfrac12, z)$, $0 \le z \le 1$.
* **Area:** base $\sqrt{(a/2)^2 + (a/2)^2} = \sqrt{a^2/2} = \frac{a}{\sqrt{2}}$, height $a$:
  $$A_{(220)} = \frac{a}{\sqrt{2}}\cdot a = \frac{a^2}{\sqrt{2}} = \frac{8R^2}{\sqrt{2}} = 4\sqrt{2}\, R^2$$
* **Atoms:** testing $x + y$ on every site: corners give $0, 1, 2$; face centres give $1$ for $(\tfrac12,\tfrac12,0/1)$, $\tfrac12$ for $(\tfrac12,0,\tfrac12)$ and $(0,\tfrac12,\tfrac12)$, and $\tfrac32$ for $(\tfrac12,1,\tfrac12)$ and $(1,\tfrac12,\tfrac12)$. Only $(\tfrac12,0,\tfrac12)$ and $(0,\tfrac12,\tfrac12)$ lie on the plane, at mid-height of the two vertical sides of the rectangle, each shared with the neighbouring cell:
  $$N = 2 \cdot \tfrac12 = 1 \text{ atom}$$
* **Fraction:**
  $$\text{PPF}_{(220)} = \frac{\pi R^2}{4\sqrt{2}R^2} = \frac{\pi}{4\sqrt{2}} = \frac{\pi\sqrt{2}}{8} = \frac{4.44288}{8} = 0.5554 \quad (55.5\%)$$

---

### 4. $(222)$ Plane: $2x + 2y + 2z = 1$, i.e. $x + y + z = \tfrac12$
* **Geometry:** intercepts $x = y = z = \tfrac12$: an equilateral triangle parallel to $(111)$, halfway between the origin corner and the $(111)$ plane.
* **Atoms:** the sum of the coordinates is an integer for every FCC site: $0, 1, 2, 3$ for corners and $\tfrac12 + \tfrac12 + 0 = 1$ or $\tfrac12 + \tfrac12 + 1 = 2$ for face centres. It is never $\tfrac12$, so no atom centre lies on the plane: $N = 0$.
  $$\text{PPF}_{(222)} = \frac{0 \cdot \pi R^2}{A_{(222)}} = 0$$

---

### 5. $(400)$ Plane: $4x = 1$, i.e. $x = \tfrac14$
* **Geometry:** a square section of side $a$ parallel to the $(100)$ faces at $x = \tfrac14$.
* **Atoms:** the FCC sites have $x = 0$, $\tfrac12$ or $1$ only, so none has $x = \tfrac14$: $N = 0$.
  $$\text{PPF}_{(400)} = \frac{0}{a^2} = 0$$

---

### 6. $(420)$ Plane: $4x + 2y = 1$
* **Geometry:** intercepts $x = \tfrac14$, $y = \tfrac12$, $z = \infty$: a vertical rectangle from $(\tfrac14, 0, z)$ to $(0, \tfrac12, z)$, $0 \le z \le 1$.
* **Area:** base $\sqrt{(a/4)^2 + (a/2)^2} = \sqrt{\tfrac{a^2}{16} + \tfrac{4a^2}{16}} = \frac{a\sqrt{5}}{4}$, height $a$:
  $$A_{(420)} = \frac{\sqrt{5}}{4}a^2 = \frac{\sqrt{5}}{4}\cdot 8R^2 = 2\sqrt{5}\, R^2$$
* **Atoms:** testing $4x + 2y$ on every site: corners give $0, 2, 4, 6$; face centres give $3$ for $(\tfrac12,\tfrac12,0/1)$, $2$ for $(\tfrac12,0,\tfrac12)$, $4$ for $(\tfrac12,1,\tfrac12)$, $5$ for $(1,\tfrac12,\tfrac12)$ and $1$ for $(0,\tfrac12,\tfrac12)$. Only the face centre $(0,\tfrac12,\tfrac12)$ lies on the plane, at mid-height of the side $x = 0$ of the rectangle, shared with the neighbouring cell:
  $$N = 1 \cdot \tfrac12 = \tfrac12 \text{ atom}$$
* **Fraction:**
  $$\text{PPF}_{(420)} = \frac{\tfrac12\pi R^2}{2\sqrt{5}R^2} = \frac{\pi}{4\sqrt{5}} = \frac{3.14159}{8.94427} = 0.3512 \quad (35.1\%)$$

---

## 🎯 4. Phase 4: Interpretation and Verification

### 1. Summary
| Plane $(hkl)$ | Atoms in the section | Section area | PPF | Percentage | Official |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $(111)$ | $2$ | $4\sqrt{3}R^2$ | $\frac{\pi}{2\sqrt{3}}$ | 90.7% | $\pi/(2\sqrt{3})$ ✓ |
| $(200)$ | $2$ | $8R^2$ | $\frac{\pi}{4}$ | 78.5% | $\pi/4$ ✓ |
| $(220)$ | $1$ | $4\sqrt{2}R^2$ | $\frac{\pi\sqrt{2}}{8}$ | 55.5% | $\pi\sqrt{2}/8$ ✓ |
| $(222)$ | $0$ | $\sqrt{3}R^2$ | $0$ | 0% | $0$ ✓ |
| $(400)$ | $0$ | $8R^2$ | $0$ | 0% | $0$ ✓ |
| $(420)$ | $\tfrac12$ | $2\sqrt{5}R^2$ | $\frac{\pi}{4\sqrt{5}}$ | 35.1% | $\pi/(4\sqrt{5})$ ✓ |

The $(222)$ triangle has edge $\tfrac12 a\sqrt{2}$, so its area is $\frac{\sqrt{3}}{4}\cdot\frac{2a^2}{4} = \frac{\sqrt{3}}{8}a^2 = \sqrt{3}R^2$. All six results agree with the official solution.

### 2. Physical meaning
* $(111)$ is the close-packed plane of FCC: $\pi/(2\sqrt{3})$ is the largest fraction of a plane that equal circles can cover (hexagonal arrangement; extension), which is why FCC slips on $\{111\}$ [Session 4 Slide 37].
* The packing falls as $h^2 + k^2 + l^2$ grows: $3 \to 4 \to 8 \to 20$ for $(111)$, $(200)$, $(220)$, $(420)$, i.e. $90.7\% > 78.5\% > 55.5\% > 35.1\%$. Higher indices mean closer layers, $d = a/\sqrt{h^2+k^2+l^2}$, and since all layers share the same $\rho_v$, closer layers hold fewer atoms per unit area.
* $(222)$ and $(400)$ are not empty "by accident": $x + y + z = \tfrac12$ lies halfway between the atomic layers $x + y + z = 0$ and $1$, and $x = \tfrac14$ halfway between the layers $x = 0$ and $\tfrac12$. Their PPF is zero because they cut the cell between two layers of atoms.

### 3. Cross-check with the volume density (extension)
For a plane that does contain atoms, $\text{PPF} = \rho_{(hkl)}\,\pi R^2$ with $\rho_{(hkl)} = \rho_v\, d$, where $\rho_v = 4/a^3$ and $d = a/\sqrt{h^2+k^2+l^2}$ is the spacing of the layers [Session 3 Slide 53]:
* $(111)$: $\rho = \frac{4}{a^3}\cdot\frac{a}{\sqrt{3}} = \frac{4}{\sqrt{3}a^2}$, $\text{PPF} = \frac{4\pi R^2}{\sqrt{3}\cdot 8R^2} = \frac{\pi}{2\sqrt{3}}$ ✓
* $(200)$: $\rho = \frac{4}{a^3}\cdot\frac{a}{2} = \frac{2}{a^2}$, $\text{PPF} = \frac{2\pi R^2}{8R^2} = \frac{\pi}{4}$ ✓
* $(220)$: $\rho = \frac{4}{a^3}\cdot\frac{a}{2\sqrt{2}} = \frac{\sqrt{2}}{a^2}$, $\text{PPF} = \frac{\sqrt{2}\pi R^2}{8R^2} = \frac{\pi\sqrt{2}}{8}$ ✓
* $(420)$: $\rho = \frac{4}{a^3}\cdot\frac{a}{2\sqrt{5}} = \frac{2}{\sqrt{5}a^2}$, $\text{PPF} = \frac{2\pi R^2}{\sqrt{5}\cdot 8R^2} = \frac{\pi}{4\sqrt{5}}$ ✓

The section-by-section counts and the layer method give the same four values.

### 4. Dimensional check
$[\text{PPF}] = \frac{[N][\pi R^2]}{[A]} = \frac{1 \cdot \text{m}^2}{\text{m}^2} = 1$: a pure number, and every value lies between $0$ and $1$ ✓.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
