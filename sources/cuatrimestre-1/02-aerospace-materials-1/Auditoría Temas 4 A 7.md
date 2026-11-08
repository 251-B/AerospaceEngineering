# Auditoría Exhaustiva de Aerospace Materials I (Temas 4 a 7)

Se han auditado línea por línea los 8 archivos HTML de **Teoría** y **Problemas** de los **Temas 4, 5, 6 y 7** del portal de estudio contrastándolos con todas las diapositivas oficiales (`Session 7` a `Session 15`), las hojas oficiales de problemas y los PDFs de soluciones de la UC3M.

> [!NOTE]
> **Balance general de calidad matemática y física:**
> - La fidelidad del contenido teórico y de la resolución matemática de los **53 problemas** (26 en T4, 15 en T5, 10 en T6 y 2 en T7) respecto a los PDFs oficiales de la UC3M es **excelente**. Incluso donde las hojas oficiales de la UC3M contienen erratas o redondeos intermedios (como la reducción de área del $7.3\%$ vs. $31.1\%$ en T5-P2, la inversión del brazo de palanca en T4-II.2, o la suma $103\%$ en el ternario T4-II.11), el portal lo calcula bien y documenta en bloques `callout` por qué difiere la clave oficial.
> - **Sin embargo, existen errores concretos de enlaces a PDFs, errores de transcripción de fórmulas/datos en tablas, bugs visuales en diagramas SVG, restos de sintaxis Markdown/Obsidian sin convertir y elementos de interfaz omitidos**, detallados a continuación con sus líneas exactas.

---

## 1. Tema 4 — Phase Diagrams

**Archivos auditados:**
- Teoría: [topic-4-phase-diagrams.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html) (3.300 líneas)
- Problemas: [topic-4-phase-diagrams.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-4-phase-diagrams.html) (4.813 líneas)

### 🔴 1.1. 30 enlaces de citas (`href`) apuntan al PDF equivocado (`Session 7` en lugar de `Session 8, 9 o 10`)
Cuando en el texto original se escribió `[Slide X]` sin poner delante `Session N`, el generador de enlaces vinculó por defecto `Session 7 T4 Phase diagrams I_2025.pdf#page=X`:

* **En [teoria/topic-4-phase-diagrams.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html) — Parte II (deben apuntar a `Session 8 T4 Phase diagrams II.pdf`):**
  - [Línea 1959](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L1959) y [Línea 1965](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L1965): `Slide 4` (precipitación en $\text{Pb–16 wt\% Sn}$) apunta a `Session 7#page=4` $\rightarrow$ debe ser `Session 8#page=4`.
  - [Línea 2321](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L2321): `Slide 9` (errata regla de la palanca en peritéctico $\text{Cu–Zn}$) apunta a `Session 7#page=9` $\rightarrow$ debe ser `Session 8#page=9`.
  - [Línea 2436](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L2436) (2 enlaces) y [Línea 2506](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L2506): `Slide 15` (diagrama $\text{Ti–B}$) apuntan a `Session 7#page=15` $\rightarrow$ deben ser `Session 8#page=15`.
* **En [teoria/topic-4-phase-diagrams.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html) — Parte III (deben apuntar a `Session 9 T4 Phase diagrams III.pdf`):**
  - [Línea 2543](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L2543) (2 enlaces): `Slide 3` y `Slide 4` $\rightarrow$ deben ser `Session 9`.
  - [Línea 2660](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L2660) (4 enlaces): `Slide 5`, `6`, `7`, `8` (fases ferrita, austenita, cementita) $\rightarrow$ deben ser `Session 9`.
  - [Líneas 2674, 2680, 2691, 2766, 2775, 2869](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L2674-L2869): `Slide 9`, `11`, `12`, `14`, `17` $\rightarrow$ deben ser `Session 9`.
  - [Líneas 2959 (2 enlaces) y 2964](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L2959-L2964): `Slide 20` y `Slide 4` $\rightarrow$ deben ser `Session 9`.
* **En [teoria/topic-4-phase-diagrams.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html) — Parte IV (deben apuntar a `Session 10 T4 Phase diagrams IV.pdf`):**
  - [Líneas 3116 (4 enlaces) y 3117 (2 enlaces)](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L3116-L3117): `Slide 3` y `Slide 4` ($\text{Al}_2\text{O}_3\text{–SiO}_2$) $\rightarrow$ deben ser `Session 10`.
  - [Líneas 3206 y 3211](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L3206-L3211): `Slide 6` y `Slide 7` (ternarios) $\rightarrow$ deben ser `Session 10`.
* **En [problemas/topic-4-phase-diagrams.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-4-phase-diagrams.html#L2950) (Problema 15):**
  - [Línea 2950](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-4-phase-diagrams.html#L2950): El texto dice `"Slide 15 of Session 8"`, pero el `href` apunta a `Session 7 T4 Phase diagrams I_2025.pdf#page=15` en lugar de `Session 8`.

### 🟡 1.2. Fallos en Diagramas SVG de Teoría y Problemas (Tema 4)
1. **Figura 54 — Diagrama $\text{Fe–Fe}_3\text{C}$ ([teoria/topic-4-phase-diagrams.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L2547-L2655)):**
   - **Etiqueta `6.67` vacía en el eje X ([línea 2592](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L2592)):** El elemento `<text x="597.7" y="379.0" ...></text>` en el borde derecho de la cementita está vacío (falta el texto `6.67`).
   - **Solapamiento de texto `eutectoid` con la barra `steels` ([líneas 2632 y 2653](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L2632-L2653)):** Las etiquetas `hypo-` (`y="438.0"`) y `eutectoid` (`y="452.0"`) están colocadas debajo de las flechas verdes (`y="422.0"`), haciendo que `eutectoid` pise la barra azul `steels` (`y="462.0"`).
2. **Figura 75 — Triángulo de Gibbs Ternario ([teoria/topic-4-phase-diagrams.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L3133-L3196)):**
   - **Falta el título del tercer eje `% C` ([líneas 3194–3195](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L3194-L3195)):** Están etiquetados `% A` y `% B`, pero se omitió `% C`. Además, tanto el lado izquierdo como el derecho están numerados de `10` a `90` subiendo hacia el vértice superior `A`, dejando sin escala propia el componente `C`.
3. **Figura 79 — Lectura del Punto 1 en el isoterma $\text{Fe–Cr–Ni}$ a $650\text{ }^\circ\text{C}$ ([teoria/topic-4-phase-diagrams.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L3218-L3263)):**
   - En las [líneas 3261–3262](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L3261-L3262), la etiqueta `20 % Fe` está colocada en el lado izquierdo (`Fe–Cr`, donde la escala de la diapositiva 7 marca `80 % Cr`) en lugar de en la base (`Ni–Fe`), y la etiqueta `20 % Ni` está colocada en la base en lugar de en el lado derecho (`Cr–Ni`).
4. **Figura 36 — Esquemas de las 5 reacciones invariantes ([teoria/topic-4-phase-diagrams.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L1976-L2049)):**
   - Al esquema **peritéctico** ([líneas 1995–1999](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L1995-L1999)) le falta la línea de contorno inferior derecha desde `(622, 146)` que separa $\alpha+L$ de $\beta+L$, y al esquema **monotéctico** ([líneas 2005–2009](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html#L2005-L2009)) le falta la línea inferior izquierda desde `(418, 236)` que separa $L_2$ de $\alpha+L_2$.
5. **Problema I.2b ([problemas/topic-4-phase-diagrams.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-4-phase-diagrams.html#L629-L746)):**
   - El enunciado pide dibujar la **curva de enfriamiento ($T$ vs. tiempo)** además de las microestructuras. La Figura 4 dibuja el diagrama de fases y los 4 círculos de microestructura, pero solo describe la curva $T\text{–}t$ en texto sin dibujarla (a diferencia de la pág. 4 de `Solution problems Phase diagrams I.pdf`).

---

## 2. Tema 5 — Mechanical Properties

**Archivos auditados:**
- Teoría: [topic-5-mechanical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-5-mechanical-properties.html) (1.879 líneas)
- Problemas: [topic-5-mechanical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html) (2.381 líneas)

### 🔴 2.1. Errores de Transcripción de Fórmulas y Datos en Teoría (Tema 5)
1. **Fórmula de Dureza Rockwell transcrita como `"to"` en lugar de signo menos `−` ([teoria/topic-5-mechanical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-5-mechanical-properties.html#L1831)):**
   - En la tabla resumen de la Sección 18 ([línea 1831](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-5-mechanical-properties.html#L1831)), en la columna "Hardness number" de Rockwell pone:
     - `$R_A$, $R_C$, $R_D$ (100 to 500 t)`
     - `$R_B$, $R_F$, $R_G$ (130 to 500 t)`
   - **Error:** En [Session 12 Slide 29](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/sources/cuatrimestre-1/02-aerospace-materials-1/unit-05-mechanical-properties/teoria/Session%2012%20T5%20Mechanical%20properties%20II.pdf), la expresión es la fórmula **`100 - 500t`** y **`130 - 500t`** (donde $t$ es la penetración en mm bajo la carga principal, equivalente a $\text{HR} = N - h/0.002$). Se confundió el guion de resta con `"to"`.
2. **Diámetro de probeta estándar ASTM mal leído como `$0.505 \cdot D$` ([teoria/topic-5-mechanical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-5-mechanical-properties.html#L568-L588)):**
   - En la [línea 568](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-5-mechanical-properties.html#L568) y en el SVG de la Figura 1 ([línea 588](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-5-mechanical-properties.html#L588)) escribe `$0.505 \cdot D$` (`0.505 D`). En [Session 11 Slide 4](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/sources/cuatrimestre-1/02-aerospace-materials-1/unit-05-mechanical-properties/teoria/Session%2011%20T5%20Mechanical%20properties%20I.pdf) pone **`0.505" Diameter`** (es decir, $0.505\text{ pulgadas} \approx 12.8\text{ mm}$, el mismo diámetro estándar del Problema 1), no $0.505$ multiplicado por $D$.
3. **Referencia huérfana a `"Slide 46 of Session 15"` en el Problema 5c ([problemas/topic-5-mechanical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html#L1399)):**
   - La [línea 1399](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html#L1399) cita `"Slide 46 of Session 15"` sin aclarar que `Session 15` pertenece al **Tema 7 (Magnetic and Thermal Properties)** (donde se vuelve a proyectar este mismo Problema 5 del Tema 5).

### 🟡 2.2. Sintaxis Markdown Cruda, XML/SVG Inválido y UI en Tema 5
1. **Encabezado Markdown crudo `##` dentro de un `<p>` ([teoria/topic-5-mechanical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-5-mechanical-properties.html#L1850)):**
   - La [línea 1850](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-5-mechanical-properties.html#L1850) muestra literalmente `<p>## Videos linked in the slides</p>`.
2. **Blockquotes Markdown crudos `&gt;` en los enunciados de los Problemas 5 y 8 ([problemas/topic-5-mechanical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html#L1305-L1306)):**
   - [Líneas 1305–1306](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html#L1305-L1306) (Problema 5): `<p>&gt;</p><p>&gt; Data: E = 207 GPa...</p>`.
   - [Líneas 1591–1594](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html#L1591-L1594) (Problema 8): `<p>&gt;</p><p>&gt; - a. What is the value of the yield stress?</p>...` en lugar de una lista HTML `<ul><li>`.
3. **Carácter `<` sin escapar dentro de `<text>` en dos SVGs ([problemas/topic-5-mechanical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html#L1705)):**
   - En las [líneas 1705 y 1920](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html#L1705): `<text ...>Δd < 0: |Δd| = ν ε d0</text>` (debe ser `&lt;`).
4. **Falta la barra superior de navegación rápida (`<nav class="pills-bar">`) en [problemas/topic-5-mechanical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html#L725-L769):**
   - El CSS la tiene definida ([líneas 247–297](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html#L247-L297)), pero no se incluyó el elemento `<nav class="pills-bar">` en el `<body>`.
5. **Omisiones menores respecto a [Session 11](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/sources/cuatrimestre-1/02-aerospace-materials-1/unit-05-mechanical-properties/teoria/Session%2011%20T5%20Mechanical%20properties%20I.pdf):**
   - Falta la tabla comparativa de **Módulo Específico ($E/\rho$)** de la diapositiva 13 (aceros, aleaciones de Al, alúmina, sílice, cemento) y las curvas de fuerza/energía interatómica de la diapositiva 14.
   - En la Figura 16 ([líneas 1179–1220](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-5-mechanical-properties.html#L1179-L1220), curva Real vs. Ingenieril, diapositiva 37), falta la tercera curva discontinua **`Corrected`** tras la estricción.

---

## 3. Tema 6 — Electrical Properties

**Archivos auditados:**
- Teoría: [topic-6-electrical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-6-electrical-properties.html) (2.350 líneas)
- Problemas: [topic-6-electrical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-6-electrical-properties.html) (2.060 líneas)

### 🔴 3.1. Restos de Markdown/Obsidian, Subíndices sin Formatear y Barra de Navegación
1. **Encabezado Markdown crudo `##` y nombres de archivos de Obsidian volcados en texto plano ([teoria/topic-6-electrical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-6-electrical-properties.html#L2320-L2323)):**
   - [Línea 2320](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-6-electrical-properties.html#L2320): `<p>## Videos linked in the slides</p>`.
   - [Línea 2323](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-6-electrical-properties.html#L2323): Vuelca los nombres internos de los archivos del vault (`Problem - T6-01 Silver and Aluminium Wires...`, etc.) como texto corrido en lugar de enlaces a `../problemas/topic-6-electrical-properties.html#problem-1`.
   - También en [problemas/topic-6-electrical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-6-electrical-properties.html#L1022) aparecen nombres crudos de notas del vault en la [línea 1022](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-6-electrical-properties.html#L1022) (`Problem - T2-DEF03 Cationic Vacancies in MgO...`) y en la [línea 1071](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-6-electrical-properties.html#L1071) (`Problem - T6-07 Conductivity of Intrinsic Germanium at 75 C`).
2. **Subíndices con guion bajo literal (`v_d`, `n_i`) y notación `e-04` en SVGs y pies de figura ([problemas/topic-6-electrical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-6-electrical-properties.html#L1395)):**
   - [Línea 1395](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-6-electrical-properties.html#L1395) (SVG Fig. 6): muestra `v_d (electrons)` con guion bajo.
   - [Líneas 1641, 1656 y 1798](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-6-electrical-properties.html#L1641-L1798) (SVGs y pie de Fig. 8 y 9): muestran `n_i` literal sin subíndice.
   - [Líneas 1652–1653](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-6-electrical-properties.html#L1652-L1653) (SVG Fig. 8): muestran `2.979e-04` y `1.021e-04` en lugar de `×10⁻⁴`.
   - En [teoria/topic-6-electrical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-6-electrical-properties.html#L1511) ([líneas 1511 y 1561](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-6-electrical-properties.html#L1511-L1561)): los pies de las Figuras 22 y 23 escriben `Ed` y `Ea` sin subíndice.
3. **Falta la barra `<nav class="pills-bar">` en [problemas/topic-6-electrical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-6-electrical-properties.html#L594-L597):**
   - Igual que en el Tema 5, el CSS define `.pills-bar` pero no está insertada en el HTML.

### 🟡 3.2. Simplificaciones u Omisiones Menores respecto a [Session 13](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/sources/cuatrimestre-1/02-aerospace-materials-1/unit-06-electrical-properties/teoria/Session%2013%20T6%20Electrical%20properties.pdf)
- **Diapositiva 45 (Unión p-n — Zona de deplexión y diagrama de bandas):** En la Sección 15.1 ([líneas 1629–1676](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-6-electrical-properties.html#L1629-L1676)), la Figura 28 solo dibuja los bloques `p` y `n` estáticos, omitiendo los otros dos subdiagramas de la diapositiva 45 (la **zona de deplexión / depletion layer** con el campo eléctrico interno y el **diagrama de doblamiento de bandas de energía** con el potencial de difusión).
- **Diapositiva 56 (Dimensiones de la celda de $\text{BaTiO}_3$):** En la Sección 17.2 ([líneas 2195–2247](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-6-electrical-properties.html#L2195-L2247)), la Figura 36 no incluye las dimensiones de red ($c = 0.403\text{ nm}, a = 0.398\text{ nm}$) ni los desplazamientos iónicos ($0.006\text{ nm}$ para $\text{Ti}^{4+}$ y $0.009/0.006\text{ nm}$ para $\text{O}^{2-}$) de la diapositiva 56.
- **Diapositiva 43 (Pendiente en la gráfica $\ln\sigma$ vs. $1/T$):** El `callout` de la [línea 1597](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-6-electrical-properties.html#L1597) señala acertadamente la errata $E_a - E_c$ de la diapositiva 43, pero convendría añadir también que en el gráfico derecho de esa misma diapositiva la etiqueta dice `Slope = -(Ec - Ed)/k` (sin el factor $2$), mientras que la ecuación de la izquierda en la diapositiva lleva $2kT$.

---

## 4. Tema 7 — Magnetic and Thermal Properties

**Archivos auditados:**
- Teoría: [topic-7-magnetic-thermal.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-7-magnetic-thermal.html) (1.272 líneas)
- Problemas: [topic-7-magnetic-thermal.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-7-magnetic-thermal.html) (799 líneas)

### 🔴 4.1. Fallos en SVGs de Ciclos de Histéresis y Dominios Magnéticos (Tema 7)
1. **Problema 11 ([problemas/topic-7-magnetic-thermal.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-7-magnetic-thermal.html#L648-L711)) — Contradicción entre la tabla de verificación y el SVG de la Figura 1:**
   - En la [línea 711](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-7-magnetic-thermal.html#L711), la tabla afirma haber marcado `$B_s$, $B_r$, $H_c$, $\mu_i$, $\mu_{max}$ on both loops`.
   - Sin embargo, en el SVG de la Figura 1 ([líneas 648–673](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-7-magnetic-thermal.html#L648-L673)):
     - **No aparece la curva de imanación inicial** desde $(0,0)$ ni están dibujadas ni etiquetadas $\mu_i$ ni $\mu_{\max}$ en ninguno de los dos ciclos.
     - En el ciclo blando (azul) solo se etiquetó `Hc (soft)`, faltando $B_s$ y $B_r$.
     - **El ciclo duro (rosa) no se cierra en los extremos de saturación** ([líneas 656–657](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-7-magnetic-thermal.html#L656-L657) y también en la Figura 8 de Teoría, [líneas 886–887](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-7-magnetic-thermal.html#L886-L887)): en $x=50$ las ramas terminan en `y=320.4` y `y=330.0` (hueco vertical de `9.6 px`), y en $x=650$ terminan en `y=50.0` y `y=59.6`.
2. **Figura 6 de Teoría — Línea de campo magnético exterior degenerada ([teoria/topic-7-magnetic-thermal.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-7-magnetic-thermal.html#L770)):**
   - En la [línea 770](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-7-magnetic-thermal.html#L770), la curva Bézier `<path d="M95,60 C95,30 95,200 95,170" .../>` tiene todos sus puntos en `x=95`, por lo que dibuja una línea recta vertical a través del centro del imán en lugar de un bucle exterior cerrado, y a los bloques B y C les faltan los bucles de campo exterior que sí aparecen en la diapositiva 15.

### 🟡 4.2. Restos del Vault de Obsidian, Rutas de PDF y Navegación (Tema 7)
1. **Nombres crudos de notas de Obsidian en el texto:**
   - [teoria/topic-7-magnetic-thermal.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-7-magnetic-thermal.html):
     - [Línea 1031](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-7-magnetic-thermal.html#L1031): `Concept - Interatomic Potential Energy Curves and Macroscopic Properties`.
     - [Línea 1107](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-7-magnetic-thermal.html#L1107): `Concept - Fick's First Law, Steady-State Diffusion`.
     - [Línea 1197](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-7-magnetic-thermal.html#L1197): `Problem - T5-05 Thermal Stress in a Constrained Steel Wire`.
   - [problemas/topic-7-magnetic-thermal.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-7-magnetic-thermal.html):
     - [Línea 745](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-7-magnetic-thermal.html#L745): `Problem - T7-11 Hysteresis Loops of Soft and Hard Magnetic Materials`.
     - [Línea 781](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-7-magnetic-thermal.html#L781): dice `table of Section 3` (referencia huérfana a la numeración del Markdown original).
2. **Enlaces al PDF de problemas apuntan a la carpeta `unit-06` en lugar de `unit-07` ([problemas/topic-7-magnetic-thermal.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-7-magnetic-thermal.html#L607)):**
   - En las [líneas 607, 626 y 732](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-7-magnetic-thermal.html#L607-L732), el enlace apunta a `unit-06-electrical-properties/problemas/...` en vez de `unit-07-magnetic-thermal-properties/problemas/...`.
3. **Falta la barra `<nav class="pills-bar">` y el botón de retorno a Teoría en [problemas/topic-7-magnetic-thermal.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/problemas/topic-7-magnetic-thermal.html#L594-L598).**
4. **URLs de YouTube en texto plano sin enlace `<a>` ([teoria/topic-7-magnetic-thermal.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-7-magnetic-thermal.html#L995)).**

---

## 5. Desajustes en el Índice General de Teoría ([teoria/index.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/index.html))

En [teoria/index.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/index.html#L416-L474):
1. **Falta la insignia verde de problemas (`<span class="cbadge problems">`) en las tarjetas de los Temas 5, 6 y 7:**
   - Los Temas 1 a 4 muestran la insignia verde con el número de problemas (`4 exam questions`, `26 solved problems`, `6 solved problems`, `26 solved problems`), pero en las tarjetas de los **Temas 5, 6 y 7** ([líneas 422, 442 y 462](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/index.html#L422-L462)) se omitió (`15 solved problems`, `10 solved problems`, `2 solved problems`).
2. **Conteo de secciones en las tarjetas:**
   - **Topic 6 ([línea 443](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/index.html#L443)):** La tarjeta dice `19 sections`, pero [topic-6-electrical-properties.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-6-electrical-properties.html) está numerado del `§ 1` al `§ 17` (17 secciones principales).
   - **Topic 7 ([línea 463](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/index.html#L463)):** La tarjeta dice `17 sections`, pero [topic-7-magnetic-thermal.html](file:///C:/Users/Ismael/Documents/GitHub/AerospaceEngineering/subjects/aerospace-materials-1/teoria/topic-7-magnetic-thermal.html) está numerado del `§ 1` al `§ 15` (15 secciones principales).
