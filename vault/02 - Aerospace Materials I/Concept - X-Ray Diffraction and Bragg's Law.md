---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Slide 53"
tags:
  - theory
  - fundamental-concept
  - x-ray-diffraction
  - bragg-law
  - interplanar-spacing
  - materials-characterization
dificultad: medium
prerrequisitos:
  - "[[Concept - Miller Notation for Cubic and Hexagonal Directions and Planes]]"
---

# ⚡ Concept: X-Ray Diffraction and Bragg's Law

> **Diffraction Principle:** X-rays have wavelengths of the order of interatomic distances ($\lambda \sim 0.05\text{--}0.25\text{ nm} \sim 0.5\text{--}2.5\text{ \AA}$). When a monochromatic beam strikes a periodic crystal, the waves elastically scattered by the electrons of parallel atomic planes interfere constructively if the optical path difference is an integer multiple of the wavelength [Slide 53].

---

## 📐 1. Interplanar Spacing Equations ($d_{hkl}$)

The interplanar spacing $d_{hkl}$ is the shortest perpendicular distance separating two adjacent crystallographic planes belonging to the same Miller family $(h\, k\, l)$ [Slide 53]:

### 1. Cubic System ($a = b = c$, $\alpha = \beta = \gamma = 90^\circ$):
$$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$

### 2. General Orthorhombic System ($a \neq b \neq c$, $\alpha = \beta = \gamma = 90^\circ$):
$$\frac{1}{d_{hkl}^2} = \frac{h^2}{a^2} + \frac{k^2}{b^2} + \frac{l^2}{c^2} \implies d_{hkl} = \frac{1}{\sqrt{\frac{h^2}{a^2} + \frac{k^2}{b^2} + \frac{l^2}{c^2}}}$$

### 3. Tetragonal System ($a = b \neq c$, $\alpha = \beta = \gamma = 90^\circ$):
$$\frac{1}{d_{hkl}^2} = \frac{h^2 + k^2}{a^2} + \frac{l^2}{c^2}$$

### 4. Hexagonal System ($a = b \neq c$, $\gamma = 120^\circ$):
$$\frac{1}{d_{hkl}^2} = \frac{4}{3}\left(\frac{h^2 + hk + k^2}{a^2}\right) + \frac{l^2}{c^2}$$

### 1.1 Derivation of $d_{hkl}$ for the Cubic System (added)
The plane $(h\,k\,l)$ nearest to the origin (not through it) cuts the axes at $x = a/h$, $y = a/k$, $z = a/l$. The vector $\vec{g} = (h, k, l)$ is normal to the family, since for any two points $P_1, P_2$ of the plane, $\vec{g}\cdot(P_1 - P_2) = h(x_1-x_2)+k(y_1-y_2)+l(z_1-z_2)$ vanishes (each intercept satisfies $\vec{g}\cdot P = a$). The unit normal is $\hat{n} = \vec{g}/\sqrt{h^2+k^2+l^2}$, and the distance from the origin plane to the next one is the projection of the intercept point $(a/h, 0, 0)$ on $\hat{n}$:

$$d_{hkl} = \hat{n}\cdot\left(\frac{a}{h},0,0\right) = \frac{h}{\sqrt{h^2+k^2+l^2}}\cdot\frac{a}{h} = \frac{a}{\sqrt{h^2+k^2+l^2}}$$

Combining with Bragg's law for a cubic crystal: $\sin\theta = \frac{\lambda}{2a}\sqrt{h^2+k^2+l^2}$, so $\sin^2\theta \propto N \equiv h^2+k^2+l^2$ and the peak positions identify the lattice (Section 3). Numerical check: $\alpha\text{-Fe}$ ($a = 2.866\ \text{\AA}$, Cu $K\alpha$, $\lambda = 1.5406\ \text{\AA}$): $d_{110} = 2.866/\sqrt2 = 2.027\ \text{\AA}$ and $2\theta = 44.68^\circ$.

---

## 🌊 2. Derivation of Bragg's Law

Consider two parallel incident rays with grazing angle $\theta$ (Bragg angle) reflected from two adjacent parallel atomic planes $(hkl)$ separated by a distance $d_{hkl}$:

```
     Ray 1 \          / Diffracted ray 1
            \   θ    /
 Plane 1 ─────●─────●───── (hkl)
            /|     |\
           / | d   | \
          /  |     |  \
     Ray 2 \ |     | / Diffracted ray 2
            \|  θ  |/
 Plane 2 ─────●─────●───── (hkl)
              A     B
```

* Ray 2 travels an additional distance before reflection equal to $d_{hkl}\sin\theta$.
* After reflection, it travels another identical additional distance equal to $d_{hkl}\sin\theta$.
* **Total optical path difference:**
  $$\Delta = 2\, d_{hkl}\sin\theta$$
* **Condition for Maximum Constructive Interference (Bragg's Law) [Slide 53]:**
  $$n\lambda = 2\, d_{hkl}\sin\theta$$
  where $n$ is the diffraction order ($n = 1$ for first-order diffraction, higher orders being absorbed into the Miller indices: $d_{nh, nk, nl} = d_{hkl}/n$).

---

## 🔍 3. Systematic Extinction Rules (Structure Factor $F_{hkl}$)

Because of destructive interference from intermediate atomic planes in centered cells, certain reflections $(hkl)$ do not appear in the diffractogram:

| Crystal Structure | Allowed Reflection Condition | Typical Observed Reflections | Forbidden (Extinct) Reflections |
| :--- | :--- | :--- | :--- |
| **Simple Cubic (SC)** | Any combination $(hkl)$ | $(100), (110), (111), (200), (210), (211)$ | None |
| **Body-Centered Cubic (BCC)** | $h + k + l = \text{even}$ | $(110), (200), (211), (220), (310), (222)$ | $(100), (111), (210), (300)$ |
| **Face-Centered Cubic (FCC)** | $h, k, l$ all even or all odd | $(111), (200), (220), (311), (222), (400)$ | $(100), (110), (210), (211)$ |

### 3.1 Why the Extinction Rules Hold (added derivation, beyond Slide 53)
For a monatomic cell with atoms at fractional positions $(x_j, y_j, z_j)$, the scattered amplitude of reflection $(hkl)$ is $F_{hkl} = f\sum_j e^{2\pi i(hx_j + ky_j + lz_j)}$, with $f$ the atomic scattering factor. Use $e^{i\pi m} = (-1)^m$.
* **BCC**, atoms at $(0,0,0)$ and $\left(\frac12,\frac12,\frac12\right)$: $F = f\left[1 + e^{i\pi(h+k+l)}\right] = f\left[1 + (-1)^{h+k+l}\right]$, which is $2f$ for $h+k+l$ even and $0$ for odd.
* **FCC**, atoms at $(0,0,0)$, $\left(\frac12,\frac12,0\right)$, $\left(\frac12,0,\frac12\right)$, $\left(0,\frac12,\frac12\right)$: $F = f\left[1 + (-1)^{h+k} + (-1)^{h+l} + (-1)^{k+l}\right]$. If $h, k, l$ have the same parity all three signs are $+$ and $F = 4f$; for mixed parity exactly two of the sums are odd, so $F = f(1 + 1 - 1 - 1) = 0$ (or $1 - 1 - 1 + 1 = 0$), e.g. $(100)$: $1 - 1 - 1 + 1 = 0$.

Consequence for the order of the peaks: the allowed values of $N = h^2+k^2+l^2$ are $2, 4, 6, 8, 10, 12, \dots$ for BCC (ratios $1:2:3:4:5:6$) and $3, 4, 8, 11, 12, 16, \dots$ for FCC (ratios $3:4:8:11:12:16$); the first two peak ratios $\sin^2\theta_2/\sin^2\theta_1$ are $2$ for BCC and $4/3$ for FCC. Check: Al (FCC, $a = 4.05\ \text{\AA}$, Cu $K\alpha$): the $(111)$ peak is at $2\theta = 38.47^\circ$.

---

## 🔬 4. Applications in Aerospace Engineering

1. **Precise Determination of Lattice Parameters ($a, c$):**
   By accurately measuring the $2\theta$ peak angles, $d_{hkl}$ is calculated and the lattice parameter $a$ is solved for:
   $$a = \frac{\lambda \sqrt{h^2 + k^2 + l^2}}{2\sin\theta}$$
2. **Phase Identification and Polymorphism:**
   It allows allotropic phases to be distinguished instantly (e.g., BCC ferrite $\alpha\text{-Fe}$ vs FCC austenite $\gamma\text{-Fe}$; HCP $\alpha$-titanium vs BCC $\beta$-titanium).
3. **Analysis of Macroscopic Residual Stresses:**
   The presence of tensile or compressive residual stresses (due to shot peening, friction stir welding or machining) alters the interplanar spacing $\Delta d$, angularly shifting the diffraction peaks ($\Delta \theta$).

---
*Bidirectional Links:*
* [[Concept - Volumetric, Linear and Planar Density in Crystal Lattices|⬅️ Previous: Crystallographic Densities]]
* [[Concept - Point Defects, Thermal Vacancies, Schottky and Frenkel|Next: Point Defects ➡️]]
