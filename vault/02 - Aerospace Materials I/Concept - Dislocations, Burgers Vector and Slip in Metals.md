---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 4 T2 Structure of Materials II_2025.pdf, Slides 25-37"
tags:
  - theory
  - fundamental-concept
  - dislocations
  - burgers-vector
  - slip
  - slip-systems
  - ductility
dificultad: high
prerrequisitos:
  - "[[Concept - FCC, BCC and HCP Metallic Structures and Packing Factor]]"
---

# 🌀 Concept: Dislocations, Burgers Vector and Slip in Metals

> **The Theoretical Strength Paradox:** The theoretical calculation of the shear stress required to slip one plane of atoms simultaneously over another predicts $\tau_{\text{theoretical}} \approx \frac{G}{2\pi} \sim \frac{G}{10}$ (of the order of thousands of megapascals). However, real pure metals deform plastically at experimental stresses 100 to 1000 times lower ($\tau_{\text{exp}} \sim 10^{-4}\text{--}10^{-3}G$) [Slide 25]. This discrepancy is explained by the existence and sequential motion of **linear defects called dislocations** (proposed theoretically by Taylor, Orowan and Polanyi in 1934).

---

## 📐 1. Types of Dislocations and the Burgers Circuit

A dislocation is a one-dimensional linear imperfection that separates a region that has undergone slip from one that remains intact [Slides 25, 28].

```
Dislocation type        Dislocation line (\vec{t}) vs Burgers vector (\vec{b})           Displacement vs \vec{b}
─────────────────────────────────────────────────────────────────────────────────────────────────
Edge dislocation        \vec{b} \perp \vec{t}                                           \vec{b} || Direction of motion
Screw dislocation       \vec{b} \parallel \vec{t}                                       \vec{b} \perp Direction of motion
Mixed dislocation       Generic angle 0 < \theta < 90^\circ                            Combined behavior
```

### 1. Edge or Taylor Dislocation [Slide 28-29]:
* It is created conceptually by inserting an **extra half-plane of atoms** into the upper half of the crystal.
* The dislocation line ($\vec{t}$) is the lower terminating edge of that extra half-plane.
* It generates an asymmetric elastic stress field: **compression** above the slip plane and **tension** below.

### 2. Screw or Burgers Dislocation [Slide 30]:
* Produced by a shear stress that distorts the crystal so that the atomic planes become a continuous helical ramp around the dislocation axis.
* It generates only a **pure shear** elastic field (with no volume change or hydrostatic dilatation).

### 3. Mixed Dislocation [Slide 31]:
* In a real crystal, dislocation lines are continuous curved loops. Regions with pure edge or screw orientation are limiting cases of a mixed dislocation whose Burgers vector $\vec{b}$ is identical along its entire path [Slide 31].

---

## 🔄 2. Formal Definition of the Burgers Vector ($\vec{b}$)

The **Burgers vector $\vec{b}$** defines the exact magnitude and crystallographic direction of the lattice distortion caused by the dislocation [Slide 28].

### Burgers Circuit Procedure:
1. In a perfect reference crystal, a closed loop is drawn by traveling $m$ atomic spacings to the right, $n$ downward, $m$ to the left and $n$ upward ($S \to E = 0$).
2. The same closed path is drawn around the dislocation line in the real crystal.
3. The circuit does not close; the vector needed to close the path (from the end to the start) is the **Burgers vector $\vec{b}$** [Slide 28].

---

## ⚡ 3. Stored Elastic Energy and the Minimum-Energy Criterion

The presence of a dislocation introduces elastic distortions in the lattice that store elastic energy per unit length ($E$) [Slides 29, 35]:

$$E \propto |\vec{b}|^2$$

Specifically, for an edge dislocation $E_{\text{edge}} = \frac{G |\vec{b}|^2}{4\pi(1-\nu)} \ln\left(\frac{r_1}{r_0}\right)$ and for a screw dislocation $E_{\text{screw}} = \frac{G |\vec{b}|^2}{4\pi} \ln\left(\frac{r_1}{r_0}\right)$.

### Why does slip occur along directions of maximum packing? [Slide 35]
The energy required to move a dislocation is directly proportional to the elastic energy it introduces:
$$E_{\text{mov}} \propto |\vec{b}|^2$$

To minimize this energy, the crystal **always selects the shortest possible lattice translation vectors**, which correspond rigorously to the **crystallographic directions of maximum packing**:
* In **FCC**:
  * Vector along the close-packed direction $\langle 110 \rangle$: $\vec{b} = \frac{a}{2}\langle 110 \rangle$.
    $$|\vec{b}|^2 = \left(\frac{a}{2}\right)^2 (1^2 + 1^2 + 0) = \frac{a^2}{2} = \frac{(2\sqrt{2}R)^2}{2} = 4R^2 \implies E_b \propto 4R^2$$
  * If slip occurred along a non-close-packed direction such as $[100]$: $\vec{b} = a[100]$.
    $$|\vec{b}|^2 = a^2 = (2\sqrt{2}R)^2 = 8R^2 \implies E_b \propto 8R^2$$
  * Energy ratio:
    $$\frac{E_{[100]}}{E_{[110]}} = \frac{8R^2}{4R^2} = \mathbf{2}$$
    *(Proof required in Problem DEF07: moving a dislocation along $[100]$ costs twice the energy of moving it along $[110]$, so nature always opts for $[110]$).*

---

## ✈️ 4. Slip Systems and the Origin of Ductility

A **slip system** consists of the combination of a **slip plane** (plane of maximum planar density) and a **slip direction** (direction of maximum linear density) contained in that plane [Slide 34, 36].

| Crystal Structure | Slip Plane | Slip Direction | Number of Active Systems | Macroscopic Ductility |
| :--- | :--- | :--- | :--- | :--- |
| **FCC ($\text{Al, Cu, Ni, Au}$)** | $\{111\}$ (4 planes) | $\langle 1\bar{1}0 \rangle$ (3 directions/plane) | $4 \times 3 = \mathbf{12\text{ systems}}$ | **Exceptional at any temperature** (even cryogenic) |
| **BCC ($\alpha\text{-Fe, Mo, W, Ta}$)** | $\{110\}$ (6 planes) | $\langle \bar{1}11 \rangle$ (2 directions/plane) | $6 \times 2 = \mathbf{12\text{ systems}}$ | Good at high $T$, but suffers a **ductile-brittle transition (DBTT)** |
| **HCP ($\text{Ti, Mg, Zn, Be}$)** | $(0001)$ basal (1 plane) | $\langle 11\bar{2}0 \rangle$ (3 directions) | $1 \times 3 = \mathbf{3\text{ systems}}$ | **Low at room temperature** (requires twinning to form) |

### von Mises Criterion for Generalized Plasticity:
For a polycrystal to undergo uniform plastic deformation without cracking at the grain boundaries, at least **5 independent slip systems** are required.
* **FCC:** It has 12 very dense, intersecting systems in 3D space $\implies$ maximum ductility and fracture toughness (basis of aerospace Al alloys and Ni superalloys).
* **BCC:** Although it has 12 systems, the $\{110\}$ planes are not atomically close-packed, requiring thermal activation to overcome the Peierls barrier $\implies$ brittleness at low temperatures.
* **HCP:** At ambient temperature it has only the 3 coplanar basal systems, of which just 2 are independent, fewer than the 5 required $\implies$ intrinsic brittleness unless prismatic/pyramidal slip is activated at high temperature or mechanical twinning occurs.

---
*Bidirectional Links:*
* [[Concept - Substitutional and Interstitial Solid Solutions, Hume-Rothery Rules|⬅️ Previous: Solid Solutions]]
* [[Concept - Planar Defects, Grain Boundaries, Twins and the Hall-Petch Equation|Next: Planar Defects and Hall-Petch ➡️]]
