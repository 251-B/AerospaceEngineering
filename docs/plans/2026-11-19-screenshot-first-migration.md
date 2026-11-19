# Plan: Screenshot-First figures in every subject (2026-11-19)

The rule is in `AGENTS.md`, "Web page rules", bullet **Figures from the official PDFs (Screenshot-First, every subject)**. This file says how to migrate the pages built before the rule, one subject and one topic at a time. Aerospace Materials I is the reference: Topics 1 to 11 already use only crops (`tools/figures/materials_t*.py`, `REG.raster`).

## 1. Inventory (2026-11-19)

Generated SVGs (`REG.put`) and crops (`REG.raster` or PNG) per vault attachment folder:

| Subject | Figure modules | `vault/attachments/` | Likely class |
| :--- | :--- | :--- | :--- |
| Business Management | `bm_t1.py` to `bm_t7.py` (48 `put`) | `BM-T1` to `BM-T7`: 48 SVG | Mostly slide diagrams: **migrate** to crops |
| Fluid Mechanics theory | `fluids_t3.py` (40), `fluids_t4.py` (8), `fluids_t5.py` (6), `fluids_t6.py` (3), `fluids_t7.py` (7) | `FM-T3` 40 SVG + 4 PNG, `FM-T4` 8 + 8, `FM-T5` 28, `FM-T6` 13 + 1, `FM-T7` 25 | Figures of `Notes.pdf`: **migrate**; plots of formulas not in the notes are EXTRA |
| Fluid Mechanics problems | `fluids_t5p.py`, `fluids_t6p.py`, `fluids_t7p.py`; `RASTER` in `tools/fluids_ns/` | in the same `FM-T*` folders | Statement figures: **migrate**; deduction and free-body figures are EXTRA |
| Engineering Mechanics | `em_theory.py`, `em_solutions.py`, `em_midterm1.py` | `EM` 68 PNG (statements, already crops), `EM-T` 49 SVG, `EM-SOL` 217 SVG, `EM-M1` 20 SVG | `EM-SOL` and most `EM-T` are deduction figures (EXTRA, required by the problem-solving standard); only `EM-T` figures copied from `Notes.pdf` or the slides **migrate** |
| Advanced Maths | `am_phase.py`, `am_portraits.py` | `AM-PS` 76 SVG | Computed phase portraits: EXTRA unless the notes print that same figure |
| Aerospace Materials I bank | `materials_mt2.py`, `mat_mt2/` | `MAT-MT2` 116 SVG, `T2-problems` 10 SVG | Items written for the bank, not in any PDF: EXTRA (no change) |

Recount before starting a subject (counts change as other sessions work):

```bash
for f in tools/figures/*.py tools/figures/*/*.py; do echo "$f put=$(grep -c '\.put(' $f) raster=$(grep -cE '\.raster\(|^\s+R\(' $f)"; done
```

## 2. Procedure per topic

One topic per commit. Models as in `CLAUDE.md` (Model routing).

1. **Classify (Haiku, read-only).** For every `REG.put` figure of the topic's module, find whether the same drawing is printed in the topic's PDFs (`sources/cuatrimestre-1/<subject>/unit-*/`). Output a table in the scratchpad: figure name, where it is embedded (note and line), class `MIGRATE` (with PDF file, page and a clip rectangle in PDF points) or `EXTRA` / `INVIABLE` (with the reason). No edits.
2. **Decide (main session).** Review the doubtful rows; a figure that adds labels or steps the PDF does not have stays EXTRA. Engineering Mechanics deduction figures and free-body diagrams are always EXTRA.
3. **Crop (Haiku, plan given).** For each `MIGRATE` row: render the clip at 200 DPI with `pymupdf`, save `vault/attachments/<folder>/<name>.png`, open it with Read and re-crop until there is no title, footer, page number, cut label or neighbouring figure. Report the files.
4. **Wire (Sonnet).** In the figure module replace `REG.put(name, ...)` by `REG.raster(name, title, caption, width)` with the caption "Copied from <PDF>, <slide/page>"; delete the drawing code that is no longer used and the old `.svg` of `vault/attachments/` (git rm). Keep the same `name` so the notes' embeds still resolve; if the embed in the note says `.svg`, change it to `.png`. Add a one-line comment next to every `REG.put` that stays, `# EXTRA: ...` or `# INVIABLE: ...`. Do not touch the study text, except a sentence that described the drawing ("the figure redrawn from ...").
5. **Build and gates.** Run the builder of the topic (`build_topic_pages.py`, `build_problem_pages.py`, `build_mech_problems.py`, `fluids_*/build.py`, ...), then `source_links.py`, `build_nav.py`, `build_source_notes.py`, `build_pdfs.py`; gates: `vault_lint`, `audit_portal`, every `--check`, `render_check` on the changed pages, and the test suite once at the end. Look at the page in the browser (figures visible, sizes sensible, Charcoal palette shows crops on their light mat).
6. **Commit and push.** Stage only the topic's files; `assets/pdf/manifest.json` and `assets/data/updates.js` are shared, so stage only your own hunks (build the staged blob from HEAD). One "What's new" entry per subject when its migration is complete. Message `refactor(<subject>): figures of Topic N cropped from the official PDFs`.

## 3. Done when

Every `REG.put` left in the subject's modules has an `# EXTRA` or `# INVIABLE` comment, every crop has been inspected, and the gates pass. Then update the inventory table above and the line "Aerospace Materials I already follows this rule" in `AGENTS.md`.

## 4. Startup prompt for a new session

```
Lee AGENTS.md (regla "Figures from the official PDFs (Screenshot-First, every subject)") y docs/plans/2026-11-19-screenshot-first-migration.md: quiero migrar las figuras del portal a recortes de los PDFs oficiales siguiendo ese plan, igual que ya está hecho en Aerospace Materials I. Antes de tocar nada, recuenta el inventario (comando del §1), enséñame la tabla por asignatura y pregúntame con qué asignatura empezamos. Después trabaja tema a tema con el procedimiento del §2 (Haiku clasifica y recorta, tú decides los dudosos, Sonnet cablea y construye), con commit y push por tema. No pases el humanizer. Para si llegas al 70 % del límite de 5 horas y dime qué queda.
```
