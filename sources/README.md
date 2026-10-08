# 📚 Repositorio de Fuentes Originales (Ground Truth)

Este directorio alberga los materiales oficiales, diapositivas, boletines de problemas, exámenes de la cátedra, guiones de laboratorio y calendarios académicos de 2º curso del Grado en Ingeniería Aeroespacial (UC3M). Sirve como la **única fuente de verdad** autorizada para nutrir la bóveda de Obsidian (`vault/`) y el portal de estudio (`subjects/`).

---

## 📁 Estructura Jerárquica por Cuatrimestre y Asignatura

```text
sources/
└── cuatrimestre-1/
    ├── 01-fluid-mechanics/
    │   ├── schedule/
    │   ├── laboratorios/          # general-instructions/ y lab-1/ .. lab-4/
    │   ├── examenes/              # final-exam / first-midterm / second-midterm
    │   ├── teoria/                # Manual integral (Notes.pdf)
    │   ├── slides/                # Diapositivas (Ch1-2)
    │   └── unit-01..07/
    │       ├── slides/            # Diapositivas específicas
    │       └── problemas/         # Boletines temáticos (K1-K10, CL1-CL22, NS1-NS17, Statics, DA1-DA14, VF2-VF20)
    │
    ├── 02-aerospace-materials-1/
    │   ├── schedule/              # Cronograma oficial (Schedule_MAT AERO I)
    │   ├── laboratorios/          # general-instructions/ y lab-1/ .. lab-4/
    │   ├── examenes/              # first-partial / second-partial / third-partial / final-exam
    │   └── unit-01..11/
    │       ├── teoria/            # Diapositivas por sesión (T1 a T11)
    │       └── problemas/         # Problemas y soluciones oficiales (T2 a T10)
    │
    ├── 03-engineering-mechanics/
    │   ├── schedule/
    │   ├── laboratorios/          # general-instructions/ y lab-1/ .. lab-4/
    │   ├── examenes/              # final-exam / first-midterm / second-midterm
    │   ├── teoria/                # Manual integral (Notes.pdf)
    │   ├── problemas/             # Volumen integral con los 51 problemas (Problems.pdf)
    │   └── unit-01..08/
    │       └── slides/            # Diapositivas temáticas
    │
    ├── 04-advanced-maths/
    │   ├── schedule/              # Cronograma de Aula Global (view.htm)
    │   ├── examenes/              # final-exam / first-midterm / second-midterm
    │   └── unit-01..06/
    │       ├── teoria/            # Libros y notas de EDOs / EDPs
    │       └── problemas/         # Boletines por capítulo (Ch1, Ch2, Ch3...)
    │
    └── 05-business-management/
        ├── schedule/
        ├── examenes/              # final-exam / first-midterm / second-midterm
        └── unit-01..06/
            ├── teoria/            # Presentaciones por tema
            └── problemas/         # Ejercicios contables y casos prácticos
```

---

## 📌 Especificaciones Pedagógicas y Estructurales de las Asignaturas

1. **Mecánica y Fluidos (Teoría Consolidada):**
   - Disponen de un único manual integral en su carpeta raíz `teoria/Notes.pdf` que abarca todo el programa.
2. **Mecánica (Problemas y Slides Integrales):**
   - Los ejercicios están centralizados en un único volumen completo en `03-engineering-mechanics/problemas/Problems.pdf` (51 problemas integrados).
   - Cada unidad temática cuenta con su subcarpeta `slides/` con las diapositivas oficiales de clase.
3. **Fluidos (Boletines Temáticos y Slides):**
   - Cuenta con 6 boletines completos organizados por unidades: Cinemática (`K1–K10`), Conservación (`CL1–CL22`), Navier-Stokes (`NS1–NS17`), Hidrostática (`fluid_statics_1–10`), Análisis Dimensional (`DA1–DA14`) y Flujos Viscosos (`VF2–VF20`).
4. **Materiales Aeroespaciales I (Temas 1 a 11 y Evaluación):**
   - 11 unidades temáticas oficiales con diapositivas de cada sesión y problemas resueltos.
   - Evaluación en 3 parciales (`first-partial/`, `second-partial/`, `third-partial/`) más examen final (`final-exam/`).
5. **Laboratorios Estandarizados (`laboratorios/`):**
   - Habilitados para Fluidos, Materiales y Mecánica de Estructuras.
   - Cada carpeta de laboratorios se divide estrictamente en:
     - `general-instructions/`: Normas generales, guías maestras de laboratorio (`mechanics_labs.pdf`, `LabGuide_AerospaceMaterialsI.pdf`, `LAB_BLUEPRINT.md`).
     - `lab-1/`, `lab-2/`, `lab-3/`, `lab-4/`: Carpetas dedicadas para los guiones, códigos MATLAB, medidas experimentales e informes de cada sesión.
6. **Carpeta de Schedule:**
   - Presente en las 5 asignaturas de forma estandarizada para alojar cronogramas y calendarios de entregas.
7. **Control de Inventario y Tracking de Faltantes (`README.md` por Asignatura):**
   - Cada una de las 5 asignaturas cuenta con un `README.md` dedicado que detalla los archivos disponibles, tabla con tamaños y ubicaciones, y una lista de verificación ("Lo que falta") contra el temario oficial.
   - Para sincronizar automáticamente todos los READMEs tras subir nuevos archivos, ejecutar:
     ```powershell
     powershell -File sources/update_inventory.ps1
     ```
     o bien:
     ```bash
     python sources/update_inventory.py
     ```
