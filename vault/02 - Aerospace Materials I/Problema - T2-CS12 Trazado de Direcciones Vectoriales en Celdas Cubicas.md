---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 12"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - crystallographic-directions
  - cubic-lattice
  - miller-indices
  - vector-drawing
---

# ✏️ Problema: T2-CS12 — Trazado de Direcciones Vectoriales en Celdas Cúbicas

## 📄 Enunciado Oficial
> **12. Draw direction vectors in unit cells for the following cubic directions:**  
> **a)** $[1\, 1\, 2]$  
> **b)** $[\bar{3}\, 3\, 1]$  
> **c)** $[2\, 1\, 2]$  
> **d)** $[\bar{1}\, 0\, 1]$  
> **e)** $[3\, 2\, 1]$  
> **f)** $[1\, 2\, 2]$  
> **g)** $[\bar{1}\, 2\, 3]$  
> **h)** $[0\, \bar{2}\, 1]$  
> **i)** $[2\, \bar{3}\, 3]$  
> **j)** $[1\, 2\, \bar{1}]$  
> **k)** $[2\, 2\, 3]$  
> **l)** $[\bar{1}\, 0\, 3]$

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Contexto Geométrico:
Se representan doce vectores cristalográficos dentro de una celda cúbica estándar unitaria de dimensiones normalizadas $1 \times 1 \times 1$.

### Reglas de Normalización y Traslación de Origen [Session 3 Slides 37-40]:
1. Las componentes del vector director deben reducirse dividiendo por la componente de mayor valor absoluto ($u_{\text{max}}$) para que el vector quepa estrictamente dentro del volumen de una única celda unitaria:
   $$\vec{r} = \left(\frac{u}{u_{\text{max}}}, \frac{v}{u_{\text{max}}}, \frac{w}{u_{\text{max}}}\right)$$
2. Si alguna componente es negativa (barra superior $\bar{u}$), el **origen del vector debe trasladarse** a la posición $+1$ a lo largo de dicho eje para que el vector apunte hacia el interior de la celda.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

Citando el procedimiento sistemático [Session 3 Slide 38]:
1. Identificar si hay índices negativos y fijar el origen local:
   * $\bar{u} \implies$ origen en $x = 1$.
   * $\bar{v} \implies$ origen en $y = 1$.
   * $\bar{w} \implies$ origen en $z = 1$.
2. Trazar el vector desde el origen $(x_0, y_0, z_0)$ hasta el punto final $(x_0 + \Delta x, y_0 + \Delta y, z_0 + \Delta z)$.
3. Unir ambos puntos con una flecha orientada.

---

## 🔢 3. Fase 3: Determinación Detallada de las 12 Direcciones

| Letra | Dirección $[u\,v\,w]$ | Normalización $(\Delta x, \Delta y, \Delta z)$ | Origen Local $(x_0, y_0, z_0)$ | Extremo del Vector $(x_f, y_f, z_f)$ | Descripción Geométrica del Vector |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **a** | $[1\, 1\, 2]$ | $(1/2,\, 1/2,\, 1)$ | $(0, 0, 0)$ | $(1/2, 1/2, 1)$ | Desde el origen hasta el centro de la cara superior $z=1$ |
| **b** | $[\bar{3}\, 3\, 1]$ | $(-1,\, 1,\, 1/3)$ | $(1, 0, 0)$ | $(0, 1, 1/3)$ | Desde el vértice $(1,0,0)$ hasta la cara izquierda a $z=1/3$ |
| **c** | $[2\, 1\, 2]$ | $(1,\, 1/2,\, 1)$ | $(0, 0, 0)$ | $(1, 1/2, 1)$ | Desde el origen hasta el punto medio de arista superior derecha |
| **d** | $[\bar{1}\, 0\, 1]$ | $(-1,\, 0,\, 1)$ | $(1, 0, 0)$ | $(0, 0, 1)$ | Diagonal de cara en el plano $x-z$, desde $(1,0,0)$ a $(0,0,1)$ |
| **e** | $[3\, 2\, 1]$ | $(1,\, 2/3,\, 1/3)$ | $(0, 0, 0)$ | $(1, 2/3, 1/3)$ | Cruza el interior de la celda hacia la cara derecha $x=1$ |
| **f** | $[1\, 2\, 2]$ | $(1/2,\, 1,\, 1)$ | $(0, 0, 0)$ | $(1/2, 1, 1)$ | Hacia la arista superior frontal |
| **g** | $[\bar{1}\, 2\, 3]$ | $(-1/3,\, 2/3,\, 1)$ | $(1, 0, 0)$ | $(2/3, 2/3, 1)$ | Asciende hacia la cara superior saliendo desde $x=1$ |
| **h** | $[0\, \bar{2}\, 1]$ | $(0,\, -1,\, 1/2)$ | $(0, 1, 0)$ | $(0, 0, 1/2)$ | Paralelo al plano $y-z$, desde $(0,1,0)$ hasta la arista $z$ a media altura |
| **i** | $[2\, \bar{3}\, 3]$ | $(2/3,\, -1,\, 1)$ | $(0, 1, 0)$ | $(2/3, 0, 1)$ | Desde $(0,1,0)$ hacia la cara superior $z=1$ |
| **j** | $[1\, 2\, \bar{1}]$ | $(1/2,\, 1,\, -1/2)$ | $(0, 0, 1)$ | $(1/2, 1, 1/2)$ | Desde la cara superior $(0,0,1)$ hacia abajo en la cara $y=1$ |
| **k** | $[2\, 2\, 3]$ | $(2/3,\, 2/3,\, 1)$ | $(0, 0, 0)$ | $(2/3, 2/3, 1)$ | Vector simétrico en $x$ e $y$ hacia la cara superior $z=1$ |
| **l** | $[\bar{1}\, 0\, 3]$ | $(-1/3,\, 0,\, 1)$ | $(1, 0, 0)$ | $(2/3, 0, 1)$ | Contenido en el plano $x-z$, desde $(1,0,0)$ a $(2/3, 0, 1)$ |

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

1. **Paralelismo:** Si multiplicamos un vector por una constante positiva escalar, la dirección no cambia: $[1\, 1\, 2]$ y $[2\, 2\, 4]$ representan exactamente la **misma dirección cristalográfica**.
2. **Equivalencia de Familias $\langle u\, v\, w \rangle$:** Direcciones como $[1\, 2\, 2]$ y $[2\, 1\, 2]$ son miembros simétricos de la familia $\langle 221 \rangle$ en la red cúbica, lo que implica que poseen idéntica longitud de repetición traslacional y las mismas propiedades físicas de conductividad o módulo de elasticidad.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
