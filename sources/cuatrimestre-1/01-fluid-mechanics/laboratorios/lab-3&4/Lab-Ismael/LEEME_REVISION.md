# Lab 3-4 Mecánica de Fluidos (UC3M) — paquete para revisión desde cero

Flujo 2D alrededor de un perfil NACA 2410 (c = 1 m, dominio 40 x 20 m) en ANSYS Fluent 2026 R1 Student.
Este paquete contiene todo lo necesario para que otra persona o IA (Claude, Antigravity) revise el trabajo
de cero, paso a paso, contra la guía oficial, y encuentre cualquier error.

## Contenido del .zip

| Ruta | Qué es |
|---|---|
| `wing2d_fluent_tutorial_updated6.pdf` | **Guía oficial del lab** (la fuente de verdad). Mallado pp. 8-9, Fluent pp. 10-19, entregables p. 20. |
| `Lab3Geometry.wbpj` + `Lab3Geometry_files/` | Proyecto de ANSYS Workbench (geometría, malla y caso de Fluent guardado a 6°). Abrir el `.wbpj` con Workbench 2026 R1. |
| `NACA2410_commas.txt`, `naca0012coords_dots.txt` | Coordenadas del perfil usadas para la geometría. |
| `Lab-Ismael/Lab3_Martin_Diez.pdf` | **Report final** (lo que se entrega). |
| `Lab-Ismael/main.tex` + `lab3_overleaf.zip` | Fuente LaTeX del report y paquete para Overleaf. |
| `Lab-Ismael/fig1..fig4_*.png` | Capturas directas de Fluent a 6° (presión, líneas de corriente, quiver estela, quiver borde de ataque). |
| `Lab-Ismael/fig5_*.pdf/png`, `fig6_*.pdf/png` + `plots_lab3.py` | Gráficas 5 (Cp a 3/6/9°) y 6 (CL vs α) y el script de Python que las genera. |
| `Lab-Ismael/pcoeff_aoaN.txt` | Cp exportado de Fluent para α = 3, 6, 9, 10, 12, 16°. |
| `Lab-Ismael/fluent_aoaN.txt`, `fluent_transcript2.txt`, `fluent_check6_saved.txt` | Transcripts de la consola de Fluent: historial de iteraciones y el informe de fuerzas con el CL de cada ángulo (`fluent_transcript2.txt` = caso de 6°). |
| `Lab-Ismael/j/*.jou` | Journals de Fluent usados (`aoaN.jou` = un ángulo completo; `setup6.jou` = configuración de 6°). Sirven para reproducir cada caso. |

## REGLA PRINCIPAL para la revisión: valores de las imágenes de la guía

En la guía, el texto y las capturas de pantalla a veces dan valores distintos. **Por decisión del equipo, se siguen casi siempre los valores que aparecen en las IMÁGENES de la guía**, salvo cuando no es posible o no tiene sentido. Las excepciones aplicadas son:

| Paso | Texto de la guía | Imagen de la guía | Usado | Por qué |
|---|---|---|---|---|
| Fluent Launcher (p. 10) | "your number of cores" | 2 procesos | **4 procesos** | La licencia Student permite como máximo 4; más da error de licencia (HPC_PARALLEL). Decisión del equipo. |
| Residuos (p. 13) | todos 1e-6 | continuity, x, y = 1e-6; **nut = 0.001** | Imagen | Regla de la imagen. |
| Vectores, escala (p. 15) | Scale 0.2, flechas negras | **Scale 10**, Auto Scale, color por Velocity Magnitude | Auto Scale + color por magnitud (imagen), **escala 0.5** | Con esta malla, 10 da flechas gigantes que tapan todo y 0.2 las deja diminutas; 0.5 es lo mínimo legible. Única excepción de escala. |
| Streamlines (p. 16) | rango 150-170 | sin Filled, Banded, Clip to Range, Draw Mesh, `surface_body`, 150-170 | Imagen | Regla de la imagen. |
| Cp (p. 17) | Direction Vector | Node Values, Position on X Axis, dirección (1, 0) | Imagen | Regla de la imagen. |

Al revisar, **no marcar como error** una diferencia con el TEXTO de la guía si coincide con la IMAGEN o con una excepción de esta tabla. Sí marcar cualquier valor que no coincida con ninguna de las dos.

## Otras desviaciones conocidas (decididas, no son errores)
- La Named Selection `wing` no existía en la malla del compañero: la zona del perfil (`wall-surface_body`) se renombró a `wing` dentro de Fluent. Si se hace *Update* de la malla, el nombre vuelve a `wall-surface_body` (habría que crear la Named Selection `wing` en Meshing).
- La malla tiene 26 902 celdas; la guía habla de "aproximadamente 29 000".
- El extra de MATLAB (p. 20, segundo EXTRA) no está hecho: el código "provided" no está disponible.
- El report lleva por ahora un solo autor; los otros cuatro integrantes se añadirán antes de entregar.

## Resultados obtenidos
| α | 3° | 6° | 9° | 10° | 12° | 16° (extra, 1000 it.) |
|---|---|---|---|---|---|---|
| CL | 0.5210 | 0.8246 | 1.1025 | 1.1850 | 1.3206 | 1.3016 |
| Iteraciones hasta converger | 73 | 75 | 82 | 87 | 104 | 258 |

Re = ρUc/μ = 1.225·10·1/1.7894e-5 ≈ 6.85·10^5. Teoría de perfil delgado: α_L0 = −2.08° (NACA 2410), dCL/dα = 2π rad⁻¹ = 0.1097/°.

## Checklist de revisión paso a paso (hacerla en este orden)

1. **Entregables (guía p. 20):** el PDF contiene exactamente las 6 figuras pedidas, cada una con pie de 1-2 frases, sin texto extra salvo el EXTRA de 16°.
   - Fig. 1 contorno de presión estática a 6°; Fig. 2 líneas de corriente; Fig. 3 quiver en x = 1.0, 1.025, 1.05, 1.075, 1.1, 1.2; Fig. 4 quiver en x = −0.05, 0, 0.025, 0.05, 0.1, 0.15, 0.2; Fig. 5 Cp a 3, 6, 9° en una gráfica (Python/MATLAB); Fig. 6 CL vs α (3, 6, 9, 10, 12°) comparado con bibliografía.
   - Los Cp se guardaron en archivos de texto (3, 6, 9° como mínimo).
2. **Configuración de Fluent** (abrir el proyecto, Setup) contra la guía pp. 10-13 y la tabla de la regla principal: pressure-based; Spalart-Allmaras; materiales por defecto; inlet por componentes con Vx = 10 cos α, Vy = 10 sin α y turbulent viscosity ratio 10; outlet presión manométrica 0; `wing` = wall; Reference Values desde inlet; Momentum Second Order Upwind; criterios de residuo; report definition `lift_coeff` sobre `wing` con vector (−sin α, cos α); inicialización Hybrid; 5000 iteraciones.
3. **Vectores por ángulo** (journals `j/aoaN.jou`): comprobar Vx, Vy y el vector de lift de cada ángulo (p. ej. 3°: 9.9863, 0.5234 y (−0.0523, 0.9986)).
4. **Convergencia** (transcripts `fluent_aoaN.txt`): continuidad < 1e-6 al final y CL estable en las últimas iteraciones.
5. **CL:** el valor del informe de fuerzas (fila `wing`, última columna, tabla "Direction Vector") coincide con la tabla de resultados y con el pie de la Fig. 6.
6. **Verosimilitud física:**
   - Presión de remanso = ½ρU² = 61.25 Pa (Fig. 1 muestra 61 Pa) y Cp(remanso) ≈ 1 en los `pcoeff`.
   - Cp mínimo de 6° = −146/61.25 = −2.38 (coincide con `pcoeff_aoa6.txt`).
   - CL casi lineal en α a ángulos bajos, por debajo de la teoría y cada vez más con α; a 16° CL baja respecto a 12° (pérdida).
7. **Gráficas 5 y 6:** ejecutar `python plots_lab3.py` dentro de `Lab-Ismael/` y comprobar que regenera las figuras y los números (incluido α_L0 = −2.08°).
8. **Pies de figura:** cada número citado en un pie se puede comprobar en las figuras, en los `pcoeff` o en los transcripts.
9. **Formato del report:** título, autor, asignatura y fecha; figuras numeradas y legibles; ejes con magnitud y unidades.

Anotar cada hallazgo con: archivo, qué está mal, valor esperado según la guía (o su imagen) y valor encontrado.
