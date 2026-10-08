# 📚 Advanced Mathematics (Matemáticas Avanzadas)

> **Course Code:** `251-15331` | **Degree:** BSc in Aerospace Engineering (UC3M) | **Term:** 2nd Year, 1st Term  
> **NotebookLM ID:** `c27033c3-5a64-403f-a517-5847831aabcb`  
> **Portal Web:** `subjects/04-advanced-maths/` | **Obsidian Vault:** `vault/04-advanced-maths/`  
> **Last Synchronized:** `2026-10-08 14:32` | **Total Official Files:** `8` (11.3 MB)

---

## 📊 Summary of Resources

| Category | File Count | Status | Notes |
| :--- | :---: | :---: | :--- |
| 📖 **Theory & Slides** | `3` | 🟢 Active | Consolidated Notes & Session Slides |
| ✏️ **Problem Sheets & Solutions** | `4` | 🟢 Active | Official problem sets & step-by-step solutions |
| 📝 **Official Exams** | `0` | 🟡 Incomplete | Partial midterms & final exams |
| 📅 **Course Schedule** | `1` | 🟢 Available | Weekly lecture & evaluation calendar |

---

## 📦 Detailed Resource Inventory (Present Files)

| # | File Name | Category / Subfolder | Size | File Path |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `view.htm` | 📅 Schedule | 174.0 KB | `schedule/view.htm` |
| 2 | `ProblemsCh1.pdf` | ✏️ Problems | 38.8 KB | `unit-01-introduction-ode-modeling/problemas/ProblemsCh1.pdf` |
| 3 | `BookODE's.pdf` | 📖 Theory | 4.6 MB | `unit-01-introduction-ode-modeling/teoria/BookODE's.pdf` |
| 4 | `ProblemsCh2.pdf` | ✏️ Problems | 43.3 KB | `unit-02-first-order-odes/problemas/ProblemsCh2.pdf` |
| 5 | `ProblemsCh3.pdf` | ✏️ Problems | 41.3 KB | `unit-03-second-order-linear-odes/problemas/ProblemsCh3.pdf` |
| 6 | `probls_ch3_2627.pdf` | ✏️ Problems | 41.3 KB | `unit-03-second-order-linear-odes/problemas/probls_ch3_2627.pdf` |
| 7 | `definition_linear_ODE.pdf` | 📖 Theory | 98.4 KB | `unit-04-systems-of-odes/teoria/definition_linear_ODE.pdf` |
| 8 | `BookPDE's.pdf` | 📖 Theory | 6.2 MB | `unit-05-fourier-series-pdes/teoria/BookPDE's.pdf` |

---

## 📋 Gap Analysis & Missing Materials Tracker ("Lo que Falta")

This checklist tracks all academic materials required according to the official UC3M syllabus. It identifies existing items and highlights missing documents that should be uploaded when published.

### 1. Course Schedule & Organization
- [x] **Official Syllabus & Calendar (`schedule/`):** Present (`view.htm`)

### 2. Syllabus Units & Weekly Topics

#### Unit 1: Introduction to ODEs & Mathematical Modeling (`unit-01-introduction-ode-modeling/`)
  * **Theory / Slides:**
    - [x] BookODE's.pdf (Ch 1)
  * **Problems & Solutions:**
    - [x] ProblemsCh1.pdf

#### Unit 2: First-Order ODEs & Qualitative Dynamics (`unit-02-first-order-odes/`)
  * **Theory / Slides:**
    - [x] BookODE's.pdf (Ch 2)
    - [ ] Lecture notes on integrating factors & exact equations
  * **Problems & Solutions:**
    - [x] ProblemsCh2.pdf

#### Unit 3: Second-Order Linear ODEs & Vibrations (`unit-03-second-order-linear-odes/`)
  * **Theory / Slides:**
    - [x] BookODE's.pdf (Ch 3)
    - [ ] Lecture notes on Wronskian & variation of parameters
  * **Problems & Solutions:**
    - [x] ProblemsCh3.pdf
    - [x] probls_ch3_2627.pdf

#### Unit 4: Linear Systems of ODEs & Phase Plane (`unit-04-systems-of-odes/`)
  * **Theory / Slides:**
    - [x] definition_linear_ODE.pdf
    - [x] BookODE's.pdf (Ch 4)
  * **Problems & Solutions:**
    - [ ] Systems of ODEs Problem Sheet (Ch 4)

#### Unit 5: Fourier Series & Boundary Value Problems (`unit-05-fourier-series-pdes/`)
  * **Theory / Slides:**
    - [x] BookPDE's.pdf (Ch 1-2)
  * **Problems & Solutions:**
    - [ ] Fourier Series Problem Sheet (Ch 5)

#### Unit 6: Classical PDEs (Heat, Wave & Laplace Equations) (`unit-06-classical-pdes/`)
  * **Theory / Slides:**
    - [x] BookPDE's.pdf (Ch 3-5)
  * **Problems & Solutions:**
    - [ ] PDE Separation of Variables Problem Sheet (Ch 6)

### 4. Official Exams & Tests (`examenes/`)
- [ ] First Midterm (ODEs Ch 1-3) past exams and solutions
- [ ] Second Midterm (Systems & Fourier) past exams and solutions
- [ ] Final Exam past papers and solutions

---

## 🔄 Automated Update Protocol ("Cómo Actualizar")

Whenever you upload new files to this subject or to `sources/`, follow this simple process to keep the inventory and checklists synchronized:

1. **Drop New Files into the Correct Subfolder:**
   - **Theory / Lecture Slides:** Place in `unit-XX-<topic>/teoria/` (or `slides/` for consolidated subjects).
   - **Problem Sheets / Solutions:** Place in `unit-XX-<topic>/problemas/`.
   - **Exams:** Place in `examenes/<first-partial | second-partial | third-partial | final-exam>/`.
   - **Schedule / Calendar:** Place in `schedule/`.

2. **Run the Automatic Synchronizer:**
   Execute the update script from the project root in PowerShell or terminal:
   ```bash
   python sources/update_inventory.py
   ```
   *This will automatically scan all files, update the inventory tables, recalculate file sizes, and refresh the "Lo que Falta" checklists across all subjects.*

3. **Downstream Propagation (Obsidian & Web):**
   After updating sources, the pedagogical subagents (`aerospace_pedagogue` and `problem_step_mentor`) reference this README to ingest new topics into the Obsidian vault (`vault/`) and develop corresponding web study modules (`subjects/`).

