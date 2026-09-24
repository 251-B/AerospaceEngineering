---
materia: Fluid Mechanics
tema: "Tema 3: Conservation Laws"
tags:
  - teoria
  - concepto-clave
  - fourier
  - conduccion-termica
  - prandtl
dificultad: media
prerrequisitos:
  - "[[01 - Fluid Mechanics/Tema 1 - Introductory Remarks and Starting Assumptions|Tema 1: Introductory Remarks]]"
---

# 🔬 Concepto: Ley de Fourier, Conducción Térmica y Número de Prandtl

> **Idea clave en una frase:** La transferencia de calor molecular por conducción se rige por la Ley de Fourier $\vec{q} = -k\nabla T$, donde el vector flujo de calor $\vec{q}$ proyectado sobre la normal exterior determina el intercambio térmico superficial ($q_n = \vec{q}\cdot\vec{n}$); la difusión molecular de momento frente a la de calor queda unívocamente caracterizada por el número adimensional de Prandtl $\mathrm{Pr} = \nu/\alpha$.

---

## ☀️ 1. Flujo de Calor Conductivo y Principio de Cauchy Térmico (Notes.pdf, Ecs. 3.39–3.43)

El calor transferido por conducción a través de un elemento de superficie diferencial $d\sigma$ orientado según el vector normal unitario $\vec{n}$ es proporcional al área del elemento:

$$ d\dot{Q}_{\text{cond}} = q_n(\vec{n}, \vec{x}, t) \, d\sigma \qquad \text{[Ec. 3.39]} $$

* **Convenio de signos oficial (Notes.pdf):** $q_n$ se define como positivo si la energía térmica se transfiere hacia el elemento de fluido hacia el cual apunta $\vec{n}$ (es decir, calor que sale del volumen delimitado si $\vec{n}$ es la normal exterior).

### Deducción del Vector Flujo Térmico con el Tetraedro de Cauchy
Al igual que en el caso de los esfuerzos mecánicos, consideremos el tetraedro diferencial de fluido de aristas coordenadas infinitesimales. En el límite $h \to 0$, el balance de energía en el tetraedro se reduce en primer orden al equilibrio entre los flujos térmicos de las cuatro caras (el término de almacenamiento volumétrico $\sim \mathcal{O}(h^3)$ es despreciable frente a las superficies $\sim \mathcal{O}(h^2)$):

$$ q_n dA = q_1 dA_1 + q_2 dA_2 + q_3 dA_3 \qquad \text{[Ec. 3.40]} $$

Donde $q_i$ representa el flujo de calor por unidad de superficie a través de un plano perpendicular al vector de la base $\vec{e}_i$. Empleando la relación trigonométrica $dA_i = n_i dA$ y dividiendo por el área de la cara oblicua $dA$:

$$ \mathbf{q_n = n_1 q_1 + n_2 q_2 + n_3 q_3 = \vec{q} \cdot \vec{n}} \qquad \text{[Ec. 3.41]} $$

Donde $\vec{q}(\vec{x}, t) = (q_1, q_2, q_3)$ es el **vector densidad de flujo de calor** (unidades $\text{W/m}^2$).

### Flujo Térmico Total y Divergencia
El calor total transmitido por conducción hacia el exterior a través de una superficie cerrada $\Sigma$ que delimita un volumen $V$ viene dado por:
$$ \dot{Q}_{\text{cond, neto}} = \int_\Sigma \vec{q} \cdot \vec{n} \, d\sigma \qquad \text{[Ec. 3.42]} $$
Aplicando el teorema de Gauss:
$$ \mathbf{\int_\Sigma \vec{q} \cdot \vec{n} \, d\sigma = \int_V (\nabla \cdot \vec{q}) \, dV} \qquad \text{[Ec. 3.43]} $$
Por tanto, $\mathbf{\nabla \cdot \vec{q}}$ representa físicamente la **tasa de pérdida neta de calor por conducción por unidad de volumen** (potencia calorífica neta que escapa de la unidad de volumen).

---

## 🔥 2. La Ley de Fourier (Notes.pdf, Ec. 3.44)

El vector flujo de calor por conducción molecular sigue la ley fenomenológica de Joseph Fourier (1822):

$$ \mathbf{\vec{q} = -k \nabla T} \qquad \text{[Ec. 3.44]} $$

* $\nabla T$: Gradiente espacial de la temperatura absoluta.
* El signo negativo garantiza la compatibilidad con el Segundo Principio de la Termodinámica: el calor fluye espontáneamente desde regiones de mayor temperatura hacia regiones de menor temperatura ($\vec{q}$ apunta en sentido contrario a $\nabla T$).
* $k$: **Conductividad térmica** del fluido, unidades $\text{W}/(\text{m}\cdot\text{K})$. Es una propiedad termodinámica de estado que depende de la temperatura y prácticamente nada de la presión.

---

## 📊 3. Comportamiento Físico de la Conductividad Térmica $k(T)$

| Fluido | Mecanismo Físico Predominante | Evolución con Temperatura $T$ | Valores de Referencia |
| :--- | :--- | :--- | :--- |
| **Gases (Aire)** | Colisiones y agitación molecular al azar ($v_{\text{th}} \propto \sqrt{T}$) | **Aumenta con $T$** ($\propto T^{1/2}$ o Sutherland térmico) | $k_a(288\text{ K}) = 0.025\text{ W/(m K)}$<br>$k_a(368\text{ K}) = 0.030\text{ W/(m K)}$ |
| **Líquidos Comunes** | Transporte por interacción molecular intermolecular | **Disminuye ligeramente con $T$** (la dilatación separa moléculas) | Aceites lubricantes: $k \approx 0.14\text{ W/(m K)}$ |
| **Agua Líquida (Anomalía)** | Red de puentes de hidrógeno que se reorganizan térmicamente | **Aumenta con $T$** en el rango líquido habitual | $k_w(288\text{ K}) = 0.59\text{ W/(m K)}$<br>$k_w(368\text{ K}) = 0.68\text{ W/(m K)}$ |

---

## ⚡ 4. Difusividad Térmica ($\alpha$) y Número de Prandtl ($\mathrm{Pr}$)

Para comparar la velocidad a la que un medio transporta energía por conducción frente a su inercia térmica, se define la **difusividad térmica** $\alpha$:

$$ \mathbf{\alpha = \frac{k}{\rho c_p}} \quad \text{(para gases o líquidos generales, o } \alpha = \frac{k}{\rho c} \text{ para líquidos incompresibles)} $$

* Unidades de $\alpha$: $\text{m}^2/\text{s}$ (idénticas dimensiones cinemáticas que la viscosidad cinemática $\nu = \mu/\rho$).

El cociente adimensional entre ambas difusividades moleculares define el **Número de Prandtl** ($\mathrm{Pr}$):

$$ \mathbf{\mathrm{Pr} = \frac{\nu}{\alpha} = \frac{\mu c_p}{k} = \frac{\text{Tasa de Difusión Molecular de Cantidad de Movimiento}}{\text{Tasa de Difusión Molecular de Calor}}} $$

### Comparación de Regímenes Físicos en Ingeniería Aeroespacial

```
Pr << 1 (Metales Líquidos: Hg, Na) ─── Pr ≈ 0.72 (Aire y Gases) ─── Pr ≈ 2 a 8 (Agua) ─── Pr >> 1 (Aceites Aeroespaciales)
    [Calor difunde mucho más              [Capa límite viscosa y           [Momento difunde mucho
      rápido que el momento]              térmica de espesor similar]        más rápido que el calor]
```

1. **Gases en Aviación ($\mathrm{Pr} \sim 0.7$ a $0.8$):**
   Para el aire en un amplísimo rango termodinámico ($150\text{ K} - 1500\text{ K}$), $\mathbf{\mathrm{Pr} \approx 0.72}$. Esto implica que en los perfiles alares y toberas, el espesor de la capa límite viscosa $\delta_v$ y el espesor de la capa límite térmica $\delta_T$ son prácticamente iguales:
   $$ \frac{\delta_v}{\delta_T} \sim \mathrm{Pr}^{1/3} \approx (0.72)^{1/3} \approx 0.90 $$
2. **Aceites de Lubricación de Turbinas ($\mathrm{Pr} \gg 1$, de 100 a 10.000):**
   La difusión viscosa de momento es miles de veces más rápida que la disipación térmica. El calor generado por fricción viscosa queda confinado en capas térmicas sumamente delgadas, requiriendo circuitos de refrigeración activa forzada en los cojinetes.
3. **Metales Líquidos de Refrigeración Nuclear / Espacial ($\mathrm{Pr} \ll 1$, $\sim 0.01 - 0.03$):**
   En reactores nucleares espaciales refrigerados por sodio o mercurio, los electrones libres transfieren energía térmica a velocidades colosales, superando por órdenes de magnitud el transporte viscoso.
4. **Agua Líquida ($\mathrm{Pr} = 8.14$ a $288\text{ K} \to 1.82$ a $368\text{ K}$):**
   Muestra una acusada sensibilidad térmica debida al desplome exponencial de la viscosidad $\mu_w(T)$.
