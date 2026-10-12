---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 3"
dificultad: medium
tags:
  - official-problem
  - solved
  - miller-indices
  - crystal-planes
  - cubic-lattice
  - origin-translation
---

# ✏️ Problem: T2-CS03 — Drawing Crystal Planes in a Cubic Lattice

## 📄 Official Statement
> **3. Draw the crystalline planes in a cubic lattice that present the following Miller indices:**  
> **a)** $(1\, 0\, \bar{1})$  
> **b)** $(1\, \bar{2}\, 1)$  
> **c)** $(\bar{2}\, 1\, 3)$  
> **d)** $(1\, \bar{3}\, 3)$  
> **e)** $(1\, \bar{2}\, \bar{2})$  
> **f)** $(\bar{3}\, 1\, 2)$  
> **g)** $(1\, 2\, \bar{3})$  
> **h)** $(\bar{1}\, \bar{4}\, 3)$  
> **i)** $(\bar{3}\, 1\, \bar{3})$  
> **j)** $(3\, \bar{1}\, 3)$

> [!note] Reading of the statement
> The text layer of the PDF loses the overbars, so they were read on the rendered page (page 1): in f) only the $3$ is barred, $(\bar{3}\,1\,2)$, and in i) only the two $3$ are barred, $(\bar{3}\,1\,\bar{3})$.

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Geometric Context:
Ten families of crystallographic planes are analysed in a cubic lattice with orthogonal edges of length $a$.

### Parameters:
| Quantity | Symbol | Value | SI unit |
| :--- | :--- | :--- | :--- |
| Lattice parameter (cube edge) | $a$ | not given (drawings in units of $a$) | m |
| Miller indices | $h, k, l$ | integers of each part | dimensionless |
| Intercepts from the origin | $1/h,\ 1/k,\ 1/l$ | fractions of $a$ | dimensionless (times $a$ in m) |

Hypotheses: ideal cubic cell ($a = b = c$, $\alpha = \beta = \gamma = 90^\circ$); each plane is drawn as its section with one unit cell; coordinates are written in units of $a$.

### Origin Selection Criterion [Session 3 Slides 45, 49]:
* If all indices $h, k, l$ are positive, the origin is the corner $O = (0, 0, 0)$.
* If any index is negative (overbar notation $\bar{u}$), the origin must be translated by $+1$ unit along the corresponding axis so that the intercept falls inside the standard unit cell:
  * $\bar{h} \implies$ translate origin to $x = 1$.
  * $\bar{k} \implies$ translate origin to $y = 1$.
  * $\bar{l} \implies$ translate origin to $z = 1$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

According to Miller's systematic inverse procedure [Session 3 Slides 44, 48]:
1. Take the **reciprocals of the Miller indices** to find the relative axial intercepts:
   $$x_{\text{int}} = \frac{1}{h}, \quad y_{\text{int}} = \frac{1}{k}, \quad z_{\text{int}} = \frac{1}{l}$$
   (with the rule $1/0 = \infty$, indicating parallelism to the axis).
2. Determine the required origin translation from the sign of the intercepts.
3. Mark the cut points on the unit cell edges relative to the chosen origin and join them with straight lines to form the polygon of the planar section.

---

## 🔢 3. Phase 3: Step-by-Step Construction of the 10 Planes

Summary of the construction (coordinates in units of $a$):

| Part | Plane $(h\,k\,l)$ | Reciprocals $(1/h, 1/k, 1/l)$ | Origin $O'$ | Cut points | Section |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **a** | $(1\,0\,\bar{1})$ | $(1,\ \infty,\ -1)$ | $(0,0,1)$ | $(1,0,1)$, $(0,0,0)$; parallel to $y$ | rectangle $a \times a\sqrt{2}$ |
| **b** | $(1\,\bar{2}\,1)$ | $(1,\ -\tfrac12,\ 1)$ | $(0,1,0)$ | $(1,1,0)$, $(0,\tfrac12,0)$, $(0,1,1)$ | triangle |
| **c** | $(\bar{2}\,1\,3)$ | $(-\tfrac12,\ 1,\ \tfrac13)$ | $(1,0,0)$ | $(\tfrac12,0,0)$, $(1,1,0)$, $(1,0,\tfrac13)$ | triangle |
| **d** | $(1\,\bar{3}\,3)$ | $(1,\ -\tfrac13,\ \tfrac13)$ | $(0,1,0)$ | $(1,1,0)$, $(0,\tfrac23,0)$, $(0,1,\tfrac13)$ | triangle |
| **e** | $(1\,\bar{2}\,\bar{2})$ | $(1,\ -\tfrac12,\ -\tfrac12)$ | $(0,1,1)$ | $(1,1,1)$, $(0,\tfrac12,1)$, $(0,1,\tfrac12)$ | triangle |
| **f** | $(\bar{3}\,1\,2)$ | $(-\tfrac13,\ 1,\ \tfrac12)$ | $(1,0,0)$ | $(\tfrac23,0,0)$, $(1,1,0)$, $(1,0,\tfrac12)$ | triangle |
| **g** | $(1\,2\,\bar{3})$ | $(1,\ \tfrac12,\ -\tfrac13)$ | $(0,0,1)$ | $(1,0,1)$, $(0,\tfrac12,1)$, $(0,0,\tfrac23)$ | triangle |
| **h** | $(\bar{1}\,\bar{4}\,3)$ | $(-1,\ -\tfrac14,\ \tfrac13)$ | $(1,1,0)$ | $(0,1,0)$, $(1,\tfrac34,0)$, $(1,1,\tfrac13)$ | triangle |
| **i** | $(\bar{3}\,1\,\bar{3})$ | $(-\tfrac13,\ 1,\ -\tfrac13)$ | $(1,0,1)$ | $(\tfrac23,0,1)$, $(1,1,1)$, $(1,0,\tfrac23)$ | triangle |
| **j** | $(3\,\bar{1}\,3)$ | $(\tfrac13,\ -1,\ \tfrac13)$ | $(0,1,0)$ | $(\tfrac13,1,0)$, $(0,0,0)$, $(0,1,\tfrac13)$ | triangle |

In every drawing the shaded polygon is the plane, the dots are the cut points (labelled with the intercept measured from $O'$, in units of $a$) and the open circle is the new origin $O'$.

### a) $(1\,0\,\bar{1})$

* **Origin:** negative index on $z$, so the origin moves one edge along that axis: $O' = (0,\ 0,\ 1)$ [Session 3 Slide 49].
* **Reciprocals:**
  $$\frac{1}{1} = 1,\quad \frac{1}{0} = \infty,\quad \frac{1}{-1} = -1$$
* **Intercepts from $O'$:**
  * $x$: $x_{O'} + 1/1 = 0 + (1) = 1$, cut point $(1,\ 0,\ 1)$
  * $y$: none, the plane is parallel to the $y$ axis
  * $z$: $z_{O'} + 1/(-1) = 1 + (-1) = 0$, cut point $(0,\ 0,\ 0)$
* **Plane equation (analytic check, extension):** intercept form of the plane in units of $a$, $h(x-x_{O'}) + k(y-y_{O'}) + l(z-z_{O'}) = 1$ gives
  $$x - (z-1) = 1 \;\Longrightarrow\; x - z = 0$$
* **Check of the vertices:**
  * $(0,\ 0,\ 0)$: $(1)(0) + (-1)(0) = 0$ ✓
  * $(1,\ 0,\ 1)$: $(1)(1) + (-1)(1) = 0$ ✓
  * $(1,\ 1,\ 1)$: $(1)(1) + (-1)(1) = 0$ ✓
  * $(0,\ 1,\ 0)$: $(1)(0) + (-1)(0) = 0$ ✓
* **Section:** the plane contains the whole edges $(0,y,0)$ and $(1,y,1)$, $0 \le y \le 1$, so the section is the rectangle $(0,0,0)$, $(1,0,1)$, $(1,1,1)$, $(0,1,0)$ with sides $a$ (along $y$) and $\sqrt{1^2+1^2}\,a = a\sqrt{2}$ (face diagonal).

![[attachments/T2-problems/cs03-a.svg]]

### b) $(1\,\bar{2}\,1)$

* **Origin:** negative index on $y$, so the origin moves one edge along that axis: $O' = (0,\ 1,\ 0)$ [Session 3 Slide 49].
* **Reciprocals:**
  $$\frac{1}{1} = 1,\quad \frac{1}{-2} = -\tfrac{1}{2},\quad \frac{1}{1} = 1$$
* **Intercepts from $O'$:**
  * $x$: $x_{O'} + 1/1 = 0 + (1) = 1$, cut point $(1,\ 1,\ 0)$
  * $y$: $y_{O'} + 1/(-2) = 1 + (-\tfrac{1}{2}) = \tfrac{1}{2}$, cut point $(0,\ \tfrac{1}{2},\ 0)$
  * $z$: $z_{O'} + 1/1 = 0 + (1) = 1$, cut point $(0,\ 1,\ 1)$
* **Plane equation (analytic check, extension):** intercept form of the plane in units of $a$, $h(x-x_{O'}) + k(y-y_{O'}) + l(z-z_{O'}) = 1$ gives
  $$x - 2(y-1) + z = 1 \;\Longrightarrow\; x - 2y + z = -1$$
* **Check of the vertices:**
  * $(1,\ 1,\ 0)$: $(1)(1) + (-2)(1) + (1)(0) = -1$ ✓
  * $(0,\ \tfrac{1}{2},\ 0)$: $(1)(0) + (-2)(\tfrac{1}{2}) + (1)(0) = -1$ ✓
  * $(0,\ 1,\ 1)$: $(1)(0) + (-2)(1) + (1)(1) = -1$ ✓
* **Section:** the three cut points lie on edges of the cell, so the section is the triangle that joins them [Session 3 Slide 48]: $(1,\ 1,\ 0)$, $(0,\ \tfrac{1}{2},\ 0)$, $(0,\ 1,\ 1)$.

![[attachments/T2-problems/cs03-b.svg]]

### c) $(\bar{2}\,1\,3)$

* **Origin:** negative index on $x$, so the origin moves one edge along that axis: $O' = (1,\ 0,\ 0)$ [Session 3 Slide 49].
* **Reciprocals:**
  $$\frac{1}{-2} = -\tfrac{1}{2},\quad \frac{1}{1} = 1,\quad \frac{1}{3} = \tfrac{1}{3}$$
* **Intercepts from $O'$:**
  * $x$: $x_{O'} + 1/(-2) = 1 + (-\tfrac{1}{2}) = \tfrac{1}{2}$, cut point $(\tfrac{1}{2},\ 0,\ 0)$
  * $y$: $y_{O'} + 1/1 = 0 + (1) = 1$, cut point $(1,\ 1,\ 0)$
  * $z$: $z_{O'} + 1/3 = 0 + (\tfrac{1}{3}) = \tfrac{1}{3}$, cut point $(1,\ 0,\ \tfrac{1}{3})$
* **Plane equation (analytic check, extension):** intercept form of the plane in units of $a$, $h(x-x_{O'}) + k(y-y_{O'}) + l(z-z_{O'}) = 1$ gives
  $$-2(x-1) + y + 3z = 1 \;\Longrightarrow\; -2x + y + 3z = -1$$
* **Check of the vertices:**
  * $(\tfrac{1}{2},\ 0,\ 0)$: $(-2)(\tfrac{1}{2}) + (1)(0) + (3)(0) = -1$ ✓
  * $(1,\ 1,\ 0)$: $(-2)(1) + (1)(1) + (3)(0) = -1$ ✓
  * $(1,\ 0,\ \tfrac{1}{3})$: $(-2)(1) + (1)(0) + (3)(\tfrac{1}{3}) = -1$ ✓
* **Section:** the three cut points lie on edges of the cell, so the section is the triangle that joins them [Session 3 Slide 48]: $(\tfrac{1}{2},\ 0,\ 0)$, $(1,\ 1,\ 0)$, $(1,\ 0,\ \tfrac{1}{3})$.

![[attachments/T2-problems/cs03-c.svg]]

### d) $(1\,\bar{3}\,3)$

* **Origin:** negative index on $y$, so the origin moves one edge along that axis: $O' = (0,\ 1,\ 0)$ [Session 3 Slide 49].
* **Reciprocals:**
  $$\frac{1}{1} = 1,\quad \frac{1}{-3} = -\tfrac{1}{3},\quad \frac{1}{3} = \tfrac{1}{3}$$
* **Intercepts from $O'$:**
  * $x$: $x_{O'} + 1/1 = 0 + (1) = 1$, cut point $(1,\ 1,\ 0)$
  * $y$: $y_{O'} + 1/(-3) = 1 + (-\tfrac{1}{3}) = \tfrac{2}{3}$, cut point $(0,\ \tfrac{2}{3},\ 0)$
  * $z$: $z_{O'} + 1/3 = 0 + (\tfrac{1}{3}) = \tfrac{1}{3}$, cut point $(0,\ 1,\ \tfrac{1}{3})$
* **Plane equation (analytic check, extension):** intercept form of the plane in units of $a$, $h(x-x_{O'}) + k(y-y_{O'}) + l(z-z_{O'}) = 1$ gives
  $$x - 3(y-1) + 3z = 1 \;\Longrightarrow\; x - 3y + 3z = -2$$
* **Check of the vertices:**
  * $(1,\ 1,\ 0)$: $(1)(1) + (-3)(1) + (3)(0) = -2$ ✓
  * $(0,\ \tfrac{2}{3},\ 0)$: $(1)(0) + (-3)(\tfrac{2}{3}) + (3)(0) = -2$ ✓
  * $(0,\ 1,\ \tfrac{1}{3})$: $(1)(0) + (-3)(1) + (3)(\tfrac{1}{3}) = -2$ ✓
* **Section:** the three cut points lie on edges of the cell, so the section is the triangle that joins them [Session 3 Slide 48]: $(1,\ 1,\ 0)$, $(0,\ \tfrac{2}{3},\ 0)$, $(0,\ 1,\ \tfrac{1}{3})$.

![[attachments/T2-problems/cs03-d.svg]]

### e) $(1\,\bar{2}\,\bar{2})$

* **Origin:** negative index on $y, z$, so the origin moves one edge along that axis: $O' = (0,\ 1,\ 1)$ [Session 3 Slide 49].
* **Reciprocals:**
  $$\frac{1}{1} = 1,\quad \frac{1}{-2} = -\tfrac{1}{2},\quad \frac{1}{-2} = -\tfrac{1}{2}$$
* **Intercepts from $O'$:**
  * $x$: $x_{O'} + 1/1 = 0 + (1) = 1$, cut point $(1,\ 1,\ 1)$
  * $y$: $y_{O'} + 1/(-2) = 1 + (-\tfrac{1}{2}) = \tfrac{1}{2}$, cut point $(0,\ \tfrac{1}{2},\ 1)$
  * $z$: $z_{O'} + 1/(-2) = 1 + (-\tfrac{1}{2}) = \tfrac{1}{2}$, cut point $(0,\ 1,\ \tfrac{1}{2})$
* **Plane equation (analytic check, extension):** intercept form of the plane in units of $a$, $h(x-x_{O'}) + k(y-y_{O'}) + l(z-z_{O'}) = 1$ gives
  $$x - 2(y-1) - 2(z-1) = 1 \;\Longrightarrow\; x - 2y - 2z = -3$$
* **Check of the vertices:**
  * $(1,\ 1,\ 1)$: $(1)(1) + (-2)(1) + (-2)(1) = -3$ ✓
  * $(0,\ \tfrac{1}{2},\ 1)$: $(1)(0) + (-2)(\tfrac{1}{2}) + (-2)(1) = -3$ ✓
  * $(0,\ 1,\ \tfrac{1}{2})$: $(1)(0) + (-2)(1) + (-2)(\tfrac{1}{2}) = -3$ ✓
* **Section:** the three cut points lie on edges of the cell, so the section is the triangle that joins them [Session 3 Slide 48]: $(1,\ 1,\ 1)$, $(0,\ \tfrac{1}{2},\ 1)$, $(0,\ 1,\ \tfrac{1}{2})$.

![[attachments/T2-problems/cs03-e.svg]]

### f) $(\bar{3}\,1\,2)$

* **Origin:** negative index on $x$, so the origin moves one edge along that axis: $O' = (1,\ 0,\ 0)$ [Session 3 Slide 49].
* **Reciprocals:**
  $$\frac{1}{-3} = -\tfrac{1}{3},\quad \frac{1}{1} = 1,\quad \frac{1}{2} = \tfrac{1}{2}$$
* **Intercepts from $O'$:**
  * $x$: $x_{O'} + 1/(-3) = 1 + (-\tfrac{1}{3}) = \tfrac{2}{3}$, cut point $(\tfrac{2}{3},\ 0,\ 0)$
  * $y$: $y_{O'} + 1/1 = 0 + (1) = 1$, cut point $(1,\ 1,\ 0)$
  * $z$: $z_{O'} + 1/2 = 0 + (\tfrac{1}{2}) = \tfrac{1}{2}$, cut point $(1,\ 0,\ \tfrac{1}{2})$
* **Plane equation (analytic check, extension):** intercept form of the plane in units of $a$, $h(x-x_{O'}) + k(y-y_{O'}) + l(z-z_{O'}) = 1$ gives
  $$-3(x-1) + y + 2z = 1 \;\Longrightarrow\; -3x + y + 2z = -2$$
* **Check of the vertices:**
  * $(\tfrac{2}{3},\ 0,\ 0)$: $(-3)(\tfrac{2}{3}) + (1)(0) + (2)(0) = -2$ ✓
  * $(1,\ 1,\ 0)$: $(-3)(1) + (1)(1) + (2)(0) = -2$ ✓
  * $(1,\ 0,\ \tfrac{1}{2})$: $(-3)(1) + (1)(0) + (2)(\tfrac{1}{2}) = -2$ ✓
* **Section:** the three cut points lie on edges of the cell, so the section is the triangle that joins them [Session 3 Slide 48]: $(\tfrac{2}{3},\ 0,\ 0)$, $(1,\ 1,\ 0)$, $(1,\ 0,\ \tfrac{1}{2})$.

![[attachments/T2-problems/cs03-f.svg]]

### g) $(1\,2\,\bar{3})$

* **Origin:** negative index on $z$, so the origin moves one edge along that axis: $O' = (0,\ 0,\ 1)$ [Session 3 Slide 49].
* **Reciprocals:**
  $$\frac{1}{1} = 1,\quad \frac{1}{2} = \tfrac{1}{2},\quad \frac{1}{-3} = -\tfrac{1}{3}$$
* **Intercepts from $O'$:**
  * $x$: $x_{O'} + 1/1 = 0 + (1) = 1$, cut point $(1,\ 0,\ 1)$
  * $y$: $y_{O'} + 1/2 = 0 + (\tfrac{1}{2}) = \tfrac{1}{2}$, cut point $(0,\ \tfrac{1}{2},\ 1)$
  * $z$: $z_{O'} + 1/(-3) = 1 + (-\tfrac{1}{3}) = \tfrac{2}{3}$, cut point $(0,\ 0,\ \tfrac{2}{3})$
* **Plane equation (analytic check, extension):** intercept form of the plane in units of $a$, $h(x-x_{O'}) + k(y-y_{O'}) + l(z-z_{O'}) = 1$ gives
  $$x + 2y - 3(z-1) = 1 \;\Longrightarrow\; x + 2y - 3z = -2$$
* **Check of the vertices:**
  * $(1,\ 0,\ 1)$: $(1)(1) + (2)(0) + (-3)(1) = -2$ ✓
  * $(0,\ \tfrac{1}{2},\ 1)$: $(1)(0) + (2)(\tfrac{1}{2}) + (-3)(1) = -2$ ✓
  * $(0,\ 0,\ \tfrac{2}{3})$: $(1)(0) + (2)(0) + (-3)(\tfrac{2}{3}) = -2$ ✓
* **Section:** the three cut points lie on edges of the cell, so the section is the triangle that joins them [Session 3 Slide 48]: $(1,\ 0,\ 1)$, $(0,\ \tfrac{1}{2},\ 1)$, $(0,\ 0,\ \tfrac{2}{3})$.

![[attachments/T2-problems/cs03-g.svg]]

### h) $(\bar{1}\,\bar{4}\,3)$

* **Origin:** negative index on $x, y$, so the origin moves one edge along that axis: $O' = (1,\ 1,\ 0)$ [Session 3 Slide 49].
* **Reciprocals:**
  $$\frac{1}{-1} = -1,\quad \frac{1}{-4} = -\tfrac{1}{4},\quad \frac{1}{3} = \tfrac{1}{3}$$
* **Intercepts from $O'$:**
  * $x$: $x_{O'} + 1/(-1) = 1 + (-1) = 0$, cut point $(0,\ 1,\ 0)$
  * $y$: $y_{O'} + 1/(-4) = 1 + (-\tfrac{1}{4}) = \tfrac{3}{4}$, cut point $(1,\ \tfrac{3}{4},\ 0)$
  * $z$: $z_{O'} + 1/3 = 0 + (\tfrac{1}{3}) = \tfrac{1}{3}$, cut point $(1,\ 1,\ \tfrac{1}{3})$
* **Plane equation (analytic check, extension):** intercept form of the plane in units of $a$, $h(x-x_{O'}) + k(y-y_{O'}) + l(z-z_{O'}) = 1$ gives
  $$-(x-1) - 4(y-1) + 3z = 1 \;\Longrightarrow\; -x - 4y + 3z = -4$$
* **Check of the vertices:**
  * $(0,\ 1,\ 0)$: $(-1)(0) + (-4)(1) + (3)(0) = -4$ ✓
  * $(1,\ \tfrac{3}{4},\ 0)$: $(-1)(1) + (-4)(\tfrac{3}{4}) + (3)(0) = -4$ ✓
  * $(1,\ 1,\ \tfrac{1}{3})$: $(-1)(1) + (-4)(1) + (3)(\tfrac{1}{3}) = -4$ ✓
* **Section:** the three cut points lie on edges of the cell, so the section is the triangle that joins them [Session 3 Slide 48]: $(0,\ 1,\ 0)$, $(1,\ \tfrac{3}{4},\ 0)$, $(1,\ 1,\ \tfrac{1}{3})$.

![[attachments/T2-problems/cs03-h.svg]]

### i) $(\bar{3}\,1\,\bar{3})$

* **Origin:** negative index on $x, z$, so the origin moves one edge along that axis: $O' = (1,\ 0,\ 1)$ [Session 3 Slide 49].
* **Reciprocals:**
  $$\frac{1}{-3} = -\tfrac{1}{3},\quad \frac{1}{1} = 1,\quad \frac{1}{-3} = -\tfrac{1}{3}$$
* **Intercepts from $O'$:**
  * $x$: $x_{O'} + 1/(-3) = 1 + (-\tfrac{1}{3}) = \tfrac{2}{3}$, cut point $(\tfrac{2}{3},\ 0,\ 1)$
  * $y$: $y_{O'} + 1/1 = 0 + (1) = 1$, cut point $(1,\ 1,\ 1)$
  * $z$: $z_{O'} + 1/(-3) = 1 + (-\tfrac{1}{3}) = \tfrac{2}{3}$, cut point $(1,\ 0,\ \tfrac{2}{3})$
* **Plane equation (analytic check, extension):** intercept form of the plane in units of $a$, $h(x-x_{O'}) + k(y-y_{O'}) + l(z-z_{O'}) = 1$ gives
  $$-3(x-1) + y - 3(z-1) = 1 \;\Longrightarrow\; -3x + y - 3z = -5$$
* **Check of the vertices:**
  * $(\tfrac{2}{3},\ 0,\ 1)$: $(-3)(\tfrac{2}{3}) + (1)(0) + (-3)(1) = -5$ ✓
  * $(1,\ 1,\ 1)$: $(-3)(1) + (1)(1) + (-3)(1) = -5$ ✓
  * $(1,\ 0,\ \tfrac{2}{3})$: $(-3)(1) + (1)(0) + (-3)(\tfrac{2}{3}) = -5$ ✓
* **Section:** the three cut points lie on edges of the cell, so the section is the triangle that joins them [Session 3 Slide 48]: $(\tfrac{2}{3},\ 0,\ 1)$, $(1,\ 1,\ 1)$, $(1,\ 0,\ \tfrac{2}{3})$.

![[attachments/T2-problems/cs03-i.svg]]

### j) $(3\,\bar{1}\,3)$

* **Origin:** negative index on $y$, so the origin moves one edge along that axis: $O' = (0,\ 1,\ 0)$ [Session 3 Slide 49].
* **Reciprocals:**
  $$\frac{1}{3} = \tfrac{1}{3},\quad \frac{1}{-1} = -1,\quad \frac{1}{3} = \tfrac{1}{3}$$
* **Intercepts from $O'$:**
  * $x$: $x_{O'} + 1/3 = 0 + (\tfrac{1}{3}) = \tfrac{1}{3}$, cut point $(\tfrac{1}{3},\ 1,\ 0)$
  * $y$: $y_{O'} + 1/(-1) = 1 + (-1) = 0$, cut point $(0,\ 0,\ 0)$
  * $z$: $z_{O'} + 1/3 = 0 + (\tfrac{1}{3}) = \tfrac{1}{3}$, cut point $(0,\ 1,\ \tfrac{1}{3})$
* **Plane equation (analytic check, extension):** intercept form of the plane in units of $a$, $h(x-x_{O'}) + k(y-y_{O'}) + l(z-z_{O'}) = 1$ gives
  $$3x - (y-1) + 3z = 1 \;\Longrightarrow\; 3x - y + 3z = 0$$
* **Check of the vertices:**
  * $(\tfrac{1}{3},\ 1,\ 0)$: $(3)(\tfrac{1}{3}) + (-1)(1) + (3)(0) = 0$ ✓
  * $(0,\ 0,\ 0)$: $(3)(0) + (-1)(0) + (3)(0) = 0$ ✓
  * $(0,\ 1,\ \tfrac{1}{3})$: $(3)(0) + (-1)(1) + (3)(\tfrac{1}{3}) = 0$ ✓
* **Section:** the three cut points lie on edges of the cell, so the section is the triangle that joins them [Session 3 Slide 48]: $(\tfrac{1}{3},\ 1,\ 0)$, $(0,\ 0,\ 0)$, $(0,\ 1,\ \tfrac{1}{3})$.

![[attachments/T2-problems/cs03-j.svg]]

---

## 🎯 4. Phase 4: Interpretation and Verification

### 1. The normal $[h\,k\,l]$ is perpendicular to every drawn plane
In cubic lattices the direction $[h\,k\,l]$ is perpendicular to the plane $(h\,k\,l)$ [Session 3 Slide 45]. Two edges of each section, taken from its first vertex, must therefore give a zero dot product with $(h, k, l)$:

| Part | $(h,k,l)$ | Edge $\vec{u}_1$ | $\vec{u}_1 \cdot (h,k,l)$ | Edge $\vec{u}_2$ | $\vec{u}_2 \cdot (h,k,l)$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| a | $(1,0,-1)$ | $(1,0,1)$ | $1 + 0 - 1 = 0$ | $(0,1,0)$ | $0$ |
| b | $(1,-2,1)$ | $(1,\tfrac12,0)$ | $1 - 1 + 0 = 0$ | $(0,\tfrac12,1)$ | $0 - 1 + 1 = 0$ |
| c | $(-2,1,3)$ | $(\tfrac12,1,0)$ | $-1 + 1 + 0 = 0$ | $(\tfrac12,0,\tfrac13)$ | $-1 + 0 + 1 = 0$ |
| d | $(1,-3,3)$ | $(1,\tfrac13,0)$ | $1 - 1 + 0 = 0$ | $(0,\tfrac13,\tfrac13)$ | $0 - 1 + 1 = 0$ |
| e | $(1,-2,-2)$ | $(1,\tfrac12,0)$ | $1 - 1 + 0 = 0$ | $(0,\tfrac12,-\tfrac12)$ | $0 - 1 + 1 = 0$ |
| f | $(-3,1,2)$ | $(\tfrac13,1,0)$ | $-1 + 1 + 0 = 0$ | $(\tfrac13,0,\tfrac12)$ | $-1 + 0 + 1 = 0$ |
| g | $(1,2,-3)$ | $(1,0,\tfrac13)$ | $1 + 0 - 1 = 0$ | $(0,\tfrac12,\tfrac13)$ | $0 + 1 - 1 = 0$ |
| h | $(-1,-4,3)$ | $(-1,\tfrac14,0)$ | $1 - 1 + 0 = 0$ | $(0,\tfrac14,\tfrac13)$ | $0 - 1 + 1 = 0$ |
| i | $(-3,1,-3)$ | $(\tfrac13,1,0)$ | $-1 + 1 + 0 = 0$ | $(\tfrac13,0,-\tfrac13)$ | $-1 + 0 + 1 = 0$ |
| j | $(3,-1,3)$ | $(\tfrac13,1,0)$ | $1 - 1 + 0 = 0$ | $(0,1,\tfrac13)$ | $0 - 1 + 1 = 0$ |

All twenty products vanish, so every polygon is a correct section of its plane.

### 2. Families and interplanar spacing
Planes with the same set of indices, in any order and with any signs, belong to one family $\{h\,k\,l\}$ [Session 3 Slide 50]. The spacing between parallel planes of a cubic crystal is [Session 3 Slide 53]
$$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$

| Family | Parts | $h^2 + k^2 + l^2$ | $d_{hkl}$ |
| :---: | :---: | :---: | :---: |
| $\{1\,0\,1\}$ | a | $1 + 0 + 1 = 2$ | $a/\sqrt{2} = 0.7071\,a$ |
| $\{1\,1\,2\}$ | b | $1 + 4 + 1 = 6$ | $a/\sqrt{6} = 0.4082\,a$ |
| $\{1\,2\,2\}$ | e | $1 + 4 + 4 = 9$ | $a/3 = 0.3333\,a$ |
| $\{1\,2\,3\}$ | c, f, g | $4 + 1 + 9 = 14$ | $a/\sqrt{14} = 0.2673\,a$ |
| $\{1\,3\,3\}$ | d, i, j | $1 + 9 + 9 = 19$ | $a/\sqrt{19} = 0.2294\,a$ |
| $\{1\,3\,4\}$ | h | $1 + 16 + 9 = 26$ | $a/\sqrt{26} = 0.1961\,a$ |

Planes c, f and g are drawn in different orientations but belong to the same family $\{123\}$, and d, i and j to $\{133\}$: inside each family the planes have the same spacing and the same atomic arrangement, so they only differ by a symmetry operation of the cube.

### 3. Limiting cases
* A zero index gives an infinite intercept: plane a never meets the $y$ axis and is parallel to it, so its section is a rectangle that runs through the whole cell instead of a triangle.
* The larger an index, the closer its cut point is to $O'$ (intercept $1/h$): the $\bar{4}$ of plane h cuts at only $\tfrac14 a$ from $O'$, and the family with the largest $h^2+k^2+l^2$ has the smallest spacing $d_{hkl}$.
* Moving the origin to $O'$ only selects another member of the same set of parallel, equidistant planes [Session 3 Slide 50]: the orientation, fixed by the normal $[h\,k\,l]$, is unchanged, and changing every sign, $(h\,k\,l) \to (\bar{h}\,\bar{k}\,\bar{l})$, describes the same set of planes.

### 4. Dimensional check
The intercepts $1/h$, $1/k$, $1/l$ are pure numbers that multiply $a$; the cut points therefore have units of length ($\text{m}$), and $[d_{hkl}] = [a] / [\sqrt{h^2+k^2+l^2}] = \text{m}/1 = \text{m}$.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
