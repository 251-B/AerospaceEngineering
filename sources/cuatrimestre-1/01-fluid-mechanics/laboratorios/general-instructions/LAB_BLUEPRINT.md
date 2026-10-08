# 🚀 Fluid Mechanics — Laboratory Practical Master Blueprint & SOP
**Standard Operating Procedure (SOP) for UC3M 2nd Year Aerospace Engineering Labs**

This document establishes the exact, validated blueprint used in **Lab 1 (Jet Impact on Surfaces)** to develop, solve, and document future laboratory sessions (Lab 2, Lab 3, etc.) with maximum speed, technical rigor, and zero hallucinations.

---

## 👥 Official Authors Metadata
Always use these exact names and affiliations for all generated reports and templates:
- **Institution:** Universidad Carlos III de Madrid (UC3M)
- **Department:** Departamento de Ingeniería Térmica y de Fluidos
- **Degree:** Bachelor's Degree in Aerospace Engineering (2nd Year)
- **Course:** Engineering Fluid Mechanics
- **Authors:**
  1. Marcos Guijarro Ruano
  2. Alejandro Ranz Remartínez
  3. Aimar Álvarez Iglesias
  4. Héctor González Rodríguez
  5. Ismael Martín Díez

---

## 🔄 5-Stage Multi-Agent Lifecycle

When a new laboratory session is initiated:

### Stage 1: Protocol Initialization (`AGENTS.md`)
- Ensure the 5 specialized subagents are defined (`manage_subagents(list)`):
  1. `source_researcher`: Local data ingestion from `sources/01-fluid-mechanics/Labs/` (PDF guide + raw measurement photos).
  2. `aerospace_pedagogue`: Theoretical framework from first principles in academic English.
  3. `problem_step_mentor`: 4-Phase analytical derivation without algebraic jumps & uncertainty propagation.
  4. `subject_web_builder`: Dual architecture implementation (Web Portal + Obsidian Vault).
  5. `web_qa_reviewer`: Quality audit (relative links, KaTeX delimiters, no heavy canvas, git status).

### Stage 2: Data Extraction & SI Normalization (`source_researcher`)
1. Ingest official guide `Lab_session_X.pdf` (geometry, nozzles, fluids, governing formulas).
2. Transcribe raw measurements sheet (flow rates, pressures, manometer levels, masses, times).
3. Compute complete SI conversion tables:
   - All flows to $\text{m}^3/\text{s}$, pressures to $\text{Pa}$, forces to $\text{N}$.
   - Reynolds numbers ($Re$), Froude numbers ($Fr$), loss coefficients, or drag coefficients ($C_d$).
   - Uncertainty propagation formulas ($\delta X = X \cdot \sqrt{\dots}$ or worst-case linear bound $\delta X = X \sum |\delta x_i / x_i|$).
   - Ensure all uncertainty values in final tables maintain homogeneous 2-decimal precision.

### Stage 3: Analytical Derivation (`problem_step_mentor` & `aerospace_pedagogue`)
1. **Phase 1 (Setup & Hypotheses):** Control volume definition ($\Sigma_c = \Sigma_i \cup \Sigma_o \cup \Sigma_{\text{free}} \cup \Sigma_w$), uniform gauge pressures ($p - p_{\text{atm}} = 0$).
2. **Phase 2 (Formulation):** Reynolds Transport Theorem (RTT) or differential Navier-Stokes justification.
3. **Phase 3 (Derivations):** Integral evaluation without algebraic jumps.
4. **Phase 4 (Physical Diagnostics):** Real-world discrepancies:
   - Ballistic Torricelli deceleration / hydrostatic height drops ($v = \sqrt{v_0^2 \pm 2gh}$).
   - Boundary layer skin friction ($c_v < 1$).
   - Measurement quantization thresholds (e.g. discrete weights $\Delta m$, rotameter graduations $\Delta Q$).
   - Human/procedural factors (parallax error, differences between lab guide protocol and actual execution).

### Stage 4: Dual Frontend & Obsidian Deployment (`subject_web_builder`)
1. **Web Portal (`subjects/fluid-mechanics/laboratorio/`):**
   - File: `lab-X-[name].html`.
   - Layout: Sticky breadcrumbs with back-link to `../../../index.html`, theme toggle (dark/light with `localStorage('theme')` & `localStorage('ae_theme')`).
   - Quick-nav pills: `[Overview, Theoretical Framework, Experimental Setup, Data Reduction, Graphical Analysis, Physical Diagnostics, Conclusions]`.
   - Data visualization: Clean responsive tables + **crisp static vector SVG plots** (prohibition of heavy Three.js/Canvas interactive simulators).
   - Celestial background: `celestial-sky.js` & `celestial-sky.css`.
   - Catalog index: Update `subjects/fluid-mechanics/laboratorio/index.html` and badge in `index.html`.
2. **Obsidian Vault (`vault/01 - Fluid Mechanics/`):**
   - File: `Laboratorio X - [Name].md` with YAML frontmatter, bidirectional `[[Wikilinks]]`, and update `Mecanica de Fluidos MOC.md`.

### Stage 5: Overleaf / Claude Pro & MATLAB Packaging
Generate the prompt for teammate's Claude Pro requesting:
1. **MATLAB Script (`process_labX_data.m`):**
   - Hardcoded experimental vectors.
   - SI data reduction and least-squares fits ($R^2$ evaluation).
   - Publication-quality vector plots (300 DPI, LaTeX interpreter, export as `.pdf` and `.png`).
   - Console output formatted in LaTeX `tabular` syntax.
2. **LaTeX Report (`main.tex`):**
   - 12–14 page standard aerospace report.
   - Front cover with UC3M and *Department of Thermal and Fluid Engineering*.
   - Sections matching academic rubric.
   - Appendix with scan of the **signed lab measurements sheet** with TA signature.

---

## ⚡ Quick-Start Prompt for New Labs

To run this entire pipeline in a single turn for future labs, copy and paste this prompt into a fresh conversation:

```text
Hola. Vamos a desarrollar el [Laboratorio X: Nombre de la Práctica] de Fluid Mechanics siguiendo el Blueprint oficial guardado en:
'sources/01-fluid-mechanics/Labs/LAB_BLUEPRINT.md'

1. Lee y asimila las directrices de 'sources/01-fluid-mechanics/Labs/LAB_BLUEPRINT.md' y 'AGENTS.md'.
2. Comprueba y define los 5 subagentes especializados.
3. Ingesta los nuevos archivos en 'sources/01-fluid-mechanics/Labs/' (guía PDF y foto/datos de medidas).
4. Ejecuta el pipeline completo:
   - Reducción de datos SI con incertidumbres a 2 decimales y diagnóstico físico maduro.
   - Creación de la página web en 'subjects/fluid-mechanics/laboratorio/lab-X-...html' y nota en Obsidian.
   - Generación del Master Prompt para Claude Pro / Overleaf con script de MATLAB incluido para nuestro equipo (Marcos, Alejandro, Aimar, Héctor, Ismael).
¡Dale caña!
```
