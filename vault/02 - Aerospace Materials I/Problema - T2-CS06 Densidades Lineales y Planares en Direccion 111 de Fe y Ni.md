---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 6"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - iron-bcc
  - nickel-fcc
  - linear-density
  - planar-density
  - slip-systems
---

# ✏️ Problema: T2-CS06 — Densidades Lineales y Planares en Dirección [111] y Plano (111) de Fe (BCC) y Ni (FCC)

## 📄 Enunciado Oficial
> **6. Calculate the linear density in the $[111]$ direction and the planar density in the $(111)$ plane for:**  
> **a)** Iron BCC *(Solution: $\rho_{[111]} = 2/(\sqrt{3}a)$, $\rho_{(111)} = 1/(a^2\sqrt{3})$)*  
> **b)** Nickel FCC *(Solution: $\rho_{[111]} = 1/(a\sqrt{3})$, $\rho_{(111)} = 4/(a^2\sqrt{3})$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Modelos Estructurales:
1. **Hierro Ferrítico ($\alpha\text{-Fe}$):** Red Cúbica Centrada en el Cuerpo (BCC), parámetro $a_{\text{Fe}}$, $n = 2$ átomos/celda.
2. **Níquel ($\text{Ni}$):** Red Cúbica Centrada en las Caras (FCC), parámetro $a_{\text{Ni}}$, $n = 4$ átomos/celda.

### Parámetros de Comparación:
* Dirección evaluada: $[111]$ (diagonal principal del cubo, longitud $L_{[111]} = a\sqrt{3}$).
* Plano evaluado: $(111)$ (plano que intersecta los ejes en $x=a, y=a, z=a$, delimitando un triángulo equilátero de aristas $a\sqrt{2}$).

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

Citando la teoría de empaquetamiento reticular [Session 4 Slides 7-9]:
* **Densidad Lineal:**
  $$\rho_{[111]} = \frac{N_{\text{átomos centrados en la diagonal}}}{a\sqrt{3}}$$
* **Densidad Planar:**
  $$\rho_{(111)} = \frac{N_{\text{átomos contenidos en el triángulo}}}{A_{\text{triángulo}}}$$
  donde el triángulo sobre la celda tiene arista $L = a\sqrt{2}$ y área:
  $$A_{\text{triángulo}} = \frac{\sqrt{3}}{4} L^2 = \frac{\sqrt{3}}{4}(2a^2) = \frac{\sqrt{3}}{2}a^2$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### Apartado a: Hierro BCC ($\alpha\text{-Fe}$)

1. **Densidad Lineal en $[111]$:**
   * En BCC, los átomos están en contacto a lo largo de la diagonal principal $[111]$.
   * La diagonal pasa por los dos vértices opuestos y atraviesa el átomo central del cuerpo.
   * Átomos cortados: $2 \times \frac{1}{2} (\text{vértices}) + 1 (\text{centro}) = 2\text{ átomos}$.
   * Longitud del segmento: $L = a\sqrt{3}$.
   $$\rho_{[111]} = \frac{2}{a\sqrt{3}} = \mathbf{\frac{2}{\sqrt{3}a}}$$

2. **Densidad Planar en $(111)$:**
   * El plano $(111)$ contiene únicamente los 3 vértices $(a,0,0), (0,a,0), (0,0,a)$. Cada vértice aporta un ángulo de $60^\circ$ dentro del triángulo equilátero ($\frac{60^\circ}{360^\circ} = \frac{1}{6}$):
     $$N_{\text{átomos}} = 3 \times \frac{1}{6} = \frac{1}{2}\text{ átomo}$$
   * El átomo central $(a/2, a/2, a/2)$ **no está contenido en el plano $(111)$**, sino a una distancia perpendicular $d = \frac{a}{2\sqrt{3}}$ por detrás.
   * Área del triángulo: $A = \frac{\sqrt{3}}{2}a^2$.
   $$\rho_{(111)} = \frac{1/2}{\frac{\sqrt{3}}{2}a^2} = \mathbf{\frac{1}{a^2\sqrt{3}}}$$

---

### Apartado b: Níquel FCC ($\text{Ni}$)

1. **Densidad Lineal en $[111]$:**
   * En FCC, los átomos no se tocan a lo largo de $[111]$; la diagonal del cubo está vacía en su centro.
   * La diagonal corta únicamente los dos átomos de los vértices opuestos por sus centros:
     $$N_{\text{átomos}} = 2 \times \frac{1}{2} = 1\text{ átomo}$$
   * Longitud: $L = a\sqrt{3}$.
   $$\rho_{[111]} = \mathbf{\frac{1}{a\sqrt{3}}}$$

2. **Densidad Planar en $(111)$:**
   * En FCC, el plano $(111)$ es el plano de máxima compacidad (plano compacto).
   * Contiene los 3 vértices del triángulo (cada uno aporta $\frac{1}{6}$) más los 3 centros de cara situados en los puntos medios de los lados del triángulo (cada uno aporta $\frac{1}{2}$ al pertenecer a dos celdas adyacentes):
     $$N_{\text{átomos}} = 3 \times \left(\frac{1}{6}\right) + 3 \times \left(\frac{1}{2}\right) = \frac{1}{2} + \frac{3}{2} = 2\text{ átomos}$$
   * Área del triángulo: $A = \frac{\sqrt{3}}{2}a^2$.
   $$\rho_{(111)} = \frac{2}{\frac{\sqrt{3}}{2}a^2} = \mathbf{\frac{4}{a^2\sqrt{3}}}$$

---

## 🎯 4. Fase 4: Interpretación Física y Consecuencias Mecánicas

| Parámetro Cristalográfico | Hierro BCC ($\alpha\text{-Fe}$) | Níquel FCC ($\text{Ni}$) | Conclusión Física |
| :--- | :--- | :--- | :--- |
| **Densidad lineal $\rho_{[111]}$** | $\mathbf{\frac{2}{\sqrt{3}a}}$ (Máxima compacidad) | $\frac{1}{\sqrt{3}a}$ | $[111]$ es la dirección de deslizamiento en BCC |
| **Densidad planar $\rho_{(111)}$** | $\frac{1}{\sqrt{3}a^2}$ | $\mathbf{\frac{4}{\sqrt{3}a^2}}$ (Máxima compacidad) | $(111)$ es el plano de deslizamiento en FCC |

* En **Hierro BCC**, $[111]$ es la dirección compacta más densa (el vector de Burgers es $\vec{b} = \frac{a}{2}\langle 111 \rangle$), pero su plano $(111)$ es muy poco denso ($\frac{1}{a^2\sqrt{3}}$), lo que explica por qué el deslizamiento en BCC ocurre en los planos $\{110\}$, cuya densidad es $\frac{\sqrt{2}}{a^2} \approx \frac{1.414}{a^2}$.
* En **Níquel FCC**, el plano $(111)$ tiene una densidad planar cuatro veces mayor ($\frac{4}{a^2\sqrt{3}} \approx \frac{2.309}{a^2}$), constituyendo el plano compacto canónico de las superaleaciones de base níquel utilizadas en álabes de turbinas monocristalinos.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
