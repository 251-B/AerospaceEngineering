---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 12"
dificultad: medium
tags:
  - official-problem
  - solved
  - crystallographic-directions
  - cubic-lattice
  - miller-indices
  - vector-drawing
---

# ✏️ Problem: T2-CS12 — Drawing Direction Vectors in Cubic Cells

## 📄 Official Statement
> **12. Draw direction vectors in unit cells for the following cubic directions:**  
> **a)** $[1\, \bar{1}\, \bar{2}]$  
> **b)** $[\bar{3}\, 3\, 1]$  
> **c)** $[2\, \bar{1}\, 2]$  
> **d)** $[\bar{1}\, 0\, 1]$  
> **e)** $[3\, 2\, 1]$  
> **f)** $[1\, \bar{2}\, \bar{2}]$  
> **g)** $[1\, \bar{2}\, 3]$  
> **h)** $[0\, \bar{2}\, 1]$  
> **i)** $[2\, \bar{3}\, 3]$  
> **j)** $[1\, 2\, \bar{1}]$  
> **k)** $[\bar{2}\, \bar{2}\, 3]$  
> **l)** $[1\, 0\, \bar{3}]$
>
> *(No numerical solution is given in the official sheet. The overbars were read from the rendered page of the PDF; in the sheet item k) is printed on a second line after l).)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Geometric Context:
Twelve crystallographic vectors are drawn inside a standard cubic unit cell of normalised dimensions $1 \times 1 \times 1$.

| Quantity | Symbol | Value / unit |
| :--- | :---: | :--- |
| Lattice parameter (cube edge) | $a$ | arbitrary, in m; not needed, because every coordinate is a fraction of $a$ |
| Direction indices | $[u\,v\,w]$ | integers, dimensionless |
| Tail (new origin $O'$) | $(x_0, y_0, z_0)$ | fractions of $a$, each $0$ or $1$ |
| Head (arrow tip) | $(x_f, y_f, z_f)$ | fractions of $a$, each in $[0, 1]$ |

Hypotheses: cubic cell ($a = b = c$, $\alpha = \beta = \gamma = 90^\circ$), right-handed axes $x$, $y$, $z$ along the cell edges [Session 3 Slide 37]; each direction is drawn as one vector inside one cell, which is always possible because parallel vectors share the same indices [Session 3 Slide 41].

### Normalisation and Origin Translation Rules [Session 3 Slides 37-40]:
1. The components of the direction vector must be reduced by dividing by the component of largest absolute value ($u_{\text{max}}$) so that the vector fits strictly inside the volume of a single unit cell:
   $$\vec{r} = \left(\frac{u}{u_{\text{max}}}, \frac{v}{u_{\text{max}}}, \frac{w}{u_{\text{max}}}\right)$$
2. If any component is negative (overbar $\bar{u}$), the **origin of the vector must be translated** to the position $+1$ along that axis so that the vector points towards the interior of the cell.

---

## 🧠 2. Phase 2: Frames and Change of Basis

Citing the systematic procedure [Session 3 Slides 39-40]:
1. Identify whether there are negative indices and fix the local origin:
   * $\bar{u} \implies$ origin at $x = 1$.
   * $\bar{v} \implies$ origin at $y = 1$.
   * $\bar{w} \implies$ origin at $z = 1$.
2. Draw the vector from the origin $(x_0, y_0, z_0)$ to the end point $(x_0 + \Delta x, y_0 + \Delta y, z_0 + \Delta z)$.
3. Join both points with an oriented arrow.

---

## 🔢 3. Phase 3: Step-by-Step Construction of the 12 Directions

For every direction the same four operations are applied [Session 3 Slides 39-40]:
1. $m = \max(|u|, |v|, |w|)$ and reduced vector $\vec{r} = \frac{1}{m}(u, v, w)$, so that the largest component is $\pm 1$;
2. new origin $O'$: a $1$ in the position of each negative index, a $0$ elsewhere;
3. head $= O' + \vec{r}$, component by component;
4. check: head $-$ tail $= \vec{r}$ and $m\,\vec{r} = (u, v, w)$, and every coordinate of the head lies in $[0, 1]$ (the arrow stays inside the cell).

**a) $[1\,\bar{1}\,\bar{2}]$.** $m = 2$, $\vec{r} = \tfrac{1}{2}(1, -1, -2) = (\tfrac12, -\tfrac12, -1)$. Negative $v$ and $w$, so $O' = (0, 1, 1)$. Head $= (0 + \tfrac12,\ 1 - \tfrac12,\ 1 - 1) = (\tfrac12, \tfrac12, 0)$, the centre of the bottom face. Check: $2(\tfrac12, -\tfrac12, -1) = (1, -1, -2)$.

**b) $[\bar{3}\,3\,1]$.** $m = 3$, $\vec{r} = \tfrac{1}{3}(-3, 3, 1) = (-1, 1, \tfrac13)$. Negative $u$, so $O' = (1, 0, 0)$. Head $= (1 - 1,\ 0 + 1,\ 0 + \tfrac13) = (0, 1, \tfrac13)$, one third of the way up the back vertical edge $x = 0$, $y = 1$. Check: $3(-1, 1, \tfrac13) = (-3, 3, 1)$.

**c) $[2\,\bar{1}\,2]$.** $m = 2$, $\vec{r} = \tfrac{1}{2}(2, -1, 2) = (1, -\tfrac12, 1)$. Negative $v$, so $O' = (0, 1, 0)$. Head $= (0 + 1,\ 1 - \tfrac12,\ 0 + 1) = (1, \tfrac12, 1)$, the midpoint of the top edge of the front face $x = 1$. Check: $2(1, -\tfrac12, 1) = (2, -1, 2)$.

**d) $[\bar{1}\,0\,1]$.** $m = 1$, $\vec{r} = (-1, 0, 1)$. Negative $u$, so $O' = (1, 0, 0)$. Head $= (1 - 1,\ 0 + 0,\ 0 + 1) = (0, 0, 1)$: the diagonal of the face $y = 0$. Check: $m = 1$, no scaling.

**e) $[3\,2\,1]$.** $m = 3$, $\vec{r} = \tfrac{1}{3}(3, 2, 1) = (1, \tfrac23, \tfrac13)$. No negative index, so $O' = (0, 0, 0)$. Head $= (1, \tfrac23, \tfrac13)$, a point of the front face $x = 1$. Check: $3(1, \tfrac23, \tfrac13) = (3, 2, 1)$.

**f) $[1\,\bar{2}\,\bar{2}]$.** $m = 2$, $\vec{r} = \tfrac{1}{2}(1, -2, -2) = (\tfrac12, -1, -1)$. Negative $v$ and $w$, so $O' = (0, 1, 1)$. Head $= (0 + \tfrac12,\ 1 - 1,\ 1 - 1) = (\tfrac12, 0, 0)$, the midpoint of the $x$ edge. Check: $2(\tfrac12, -1, -1) = (1, -2, -2)$.

**g) $[1\,\bar{2}\,3]$.** $m = 3$, $\vec{r} = \tfrac{1}{3}(1, -2, 3) = (\tfrac13, -\tfrac23, 1)$. Negative $v$, so $O' = (0, 1, 0)$. Head $= (0 + \tfrac13,\ 1 - \tfrac23,\ 0 + 1) = (\tfrac13, \tfrac13, 1)$, a point of the top face. Check: $3(\tfrac13, -\tfrac23, 1) = (1, -2, 3)$.

**h) $[0\,\bar{2}\,1]$.** $m = 2$, $\vec{r} = \tfrac{1}{2}(0, -2, 1) = (0, -1, \tfrac12)$. Negative $v$, so $O' = (0, 1, 0)$. Head $= (0,\ 1 - 1,\ 0 + \tfrac12) = (0, 0, \tfrac12)$, the midpoint of the $z$ edge; the vector lies in the face $x = 0$. Check: $2(0, -1, \tfrac12) = (0, -2, 1)$.

**i) $[2\,\bar{3}\,3]$.** $m = 3$, $\vec{r} = \tfrac{1}{3}(2, -3, 3) = (\tfrac23, -1, 1)$. Negative $v$, so $O' = (0, 1, 0)$. Head $= (0 + \tfrac23,\ 1 - 1,\ 0 + 1) = (\tfrac23, 0, 1)$, a point of the top edge of the face $y = 0$. Check: $3(\tfrac23, -1, 1) = (2, -3, 3)$.

**j) $[1\,2\,\bar{1}]$.** $m = 2$, $\vec{r} = \tfrac{1}{2}(1, 2, -1) = (\tfrac12, 1, -\tfrac12)$. Negative $w$, so $O' = (0, 0, 1)$. Head $= (0 + \tfrac12,\ 0 + 1,\ 1 - \tfrac12) = (\tfrac12, 1, \tfrac12)$, the centre of the right face $y = 1$. Check: $2(\tfrac12, 1, -\tfrac12) = (1, 2, -1)$.

**k) $[\bar{2}\,\bar{2}\,3]$.** $m = 3$, $\vec{r} = \tfrac{1}{3}(-2, -2, 3) = (-\tfrac23, -\tfrac23, 1)$. Negative $u$ and $v$, so $O' = (1, 1, 0)$. Head $= (1 - \tfrac23,\ 1 - \tfrac23,\ 0 + 1) = (\tfrac13, \tfrac13, 1)$, a point of the top face. Check: $3(-\tfrac23, -\tfrac23, 1) = (-2, -2, 3)$.

**l) $[1\,0\,\bar{3}]$.** $m = 3$, $\vec{r} = \tfrac{1}{3}(1, 0, -3) = (\tfrac13, 0, -1)$. Negative $w$, so $O' = (0, 0, 1)$. Head $= (0 + \tfrac13,\ 0,\ 1 - 1) = (\tfrac13, 0, 0)$, a point of the $x$ edge; the vector lies in the face $y = 0$. Check: $3(\tfrac13, 0, -1) = (1, 0, -3)$.

### Summary

| Item | Direction | $m$ | Reduced $\vec{r}$ | Tail $O'$ | Head | Where the head lies |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| a | $[1\,\bar{1}\,\bar{2}]$ | 2 | $(\tfrac12, -\tfrac12, -1)$ | $(0, 1, 1)$ | $(\tfrac12, \tfrac12, 0)$ | centre of the bottom face |
| b | $[\bar{3}\,3\,1]$ | 3 | $(-1, 1, \tfrac13)$ | $(1, 0, 0)$ | $(0, 1, \tfrac13)$ | edge $x = 0$, $y = 1$ |
| c | $[2\,\bar{1}\,2]$ | 2 | $(1, -\tfrac12, 1)$ | $(0, 1, 0)$ | $(1, \tfrac12, 1)$ | midpoint of edge $x = 1$, $z = 1$ |
| d | $[\bar{1}\,0\,1]$ | 1 | $(-1, 0, 1)$ | $(1, 0, 0)$ | $(0, 0, 1)$ | corner (face diagonal of $y = 0$) |
| e | $[3\,2\,1]$ | 3 | $(1, \tfrac23, \tfrac13)$ | $(0, 0, 0)$ | $(1, \tfrac23, \tfrac13)$ | face $x = 1$ |
| f | $[1\,\bar{2}\,\bar{2}]$ | 2 | $(\tfrac12, -1, -1)$ | $(0, 1, 1)$ | $(\tfrac12, 0, 0)$ | midpoint of the $x$ edge |
| g | $[1\,\bar{2}\,3]$ | 3 | $(\tfrac13, -\tfrac23, 1)$ | $(0, 1, 0)$ | $(\tfrac13, \tfrac13, 1)$ | top face $z = 1$ |
| h | $[0\,\bar{2}\,1]$ | 2 | $(0, -1, \tfrac12)$ | $(0, 1, 0)$ | $(0, 0, \tfrac12)$ | midpoint of the $z$ edge |
| i | $[2\,\bar{3}\,3]$ | 3 | $(\tfrac23, -1, 1)$ | $(0, 1, 0)$ | $(\tfrac23, 0, 1)$ | edge $y = 0$, $z = 1$ |
| j | $[1\,2\,\bar{1}]$ | 2 | $(\tfrac12, 1, -\tfrac12)$ | $(0, 0, 1)$ | $(\tfrac12, 1, \tfrac12)$ | centre of the face $y = 1$ |
| k | $[\bar{2}\,\bar{2}\,3]$ | 3 | $(-\tfrac23, -\tfrac23, 1)$ | $(1, 1, 0)$ | $(\tfrac13, \tfrac13, 1)$ | top face $z = 1$ |
| l | $[1\,0\,\bar{3}]$ | 3 | $(\tfrac13, 0, -1)$ | $(0, 0, 1)$ | $(\tfrac13, 0, 0)$ | $x$ edge |

### Drawings

Each panel shows the cell with the axes $x$ (towards the reader), $y$ (right) and $z$ (up); the filled dot is the tail $O'$, the open dot the head, and a dotted line drops from a head that is not on the base or on a vertical edge to its foot on the plane $z = 0$.

![[attachments/T2/p12-dirs-1.svg]]

![[attachments/T2/p12-dirs-2.svg]]

![[attachments/T2/p12-dirs-3.svg]]

![[attachments/T2/p12-dirs-4.svg]]

---

## 🎯 4. Phase 4: Units and Limits

1. **Dimensions:** the indices are pure numbers and every coordinate is a fraction of the lattice parameter, $x = X/a$ with $[X] = \text{m}$ and $[a] = \text{m}$, so $[x] = \text{m}/\text{m} = 1$. The drawings are therefore valid for any cubic metal; only the real length of each vector scales with $a$.
2. **Containment check:** all twelve heads have coordinates in $[0, 1]$ (table above), so every arrow stays inside one cell, as the construction requires [Session 3 Slide 39].
3. **Parallelism:** multiplying a vector by a positive scalar does not change the direction: $[1\,\bar{1}\,\bar{2}]$ and $[2\,\bar{2}\,\bar{4}]$ are the **same crystallographic direction** [Session 3 Slide 41]. Reversing the arrow changes every sign: the opposite of $[1\,2\,\bar{1}]$ is $[\bar{1}\,\bar{2}\,1]$.
4. **Families:** in a cubic cell, directions whose indices are permutations of the same numbers, with any signs, belong to the same family. Here $[2\,\bar{1}\,2]$ and $[1\,\bar{2}\,\bar{2}]$ are both members of $\langle 1\,2\,2 \rangle$, and $[2\,\bar{3}\,3]$ belongs to $\langle 2\,3\,3 \rangle$; members of one family have the same repeat length along the line.
5. **Limiting case:** when $m = 1$ (item d) no scaling is needed and the head is a lattice corner; for $m > 1$ at least one component is a fraction, so the head falls on an edge, a face or (in general) inside the cell.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
