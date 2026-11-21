# Plan: Screenshot-First figures in every subject (2026-11-19)

The rule is in `AGENTS.md`, "Web page rules", bullet **Figures from the official PDFs (Screenshot-First, every subject)**. This file says how to migrate the pages built before the rule, one subject and one topic at a time. Aerospace Materials I is the reference: Topics 1 to 11 already use only crops (`tools/figures/materials_t*.py`, `REG.raster`).

## 1. Inventory (2026-11-19)

Generated SVGs (`REG.put`) and crops (`REG.raster` or PNG) per vault attachment folder:

| Subject | Figure modules | `vault/attachments/` | Likely class |
| :--- | :--- | :--- | :--- |
| Business Management | `bm_t1.py` to `bm_t7.py` (48 `put`) | `BM-T1` to `BM-T7`: 4 SVG left (EXTRA) + 46 PNG | **Done 2026-11-19**: 46 crops; EXTRA: T3 balance, T4 p2-profit and p3-profit, T5 p1-demand |
| Fluid Mechanics theory | `fluids_t3.py` (40), `fluids_t4.py` (8), `fluids_t5.py` (6), `fluids_t6.py` (3), `fluids_t7.py` (7) | `FM-T3` 40 SVG + 4 PNG, `FM-T4` 8 + 8, `FM-T5` 28, `FM-T6` 13 + 1, `FM-T7` 25 | **Done 2026-11-21** (theory and problems together): 45 crops (T3 10, T4 2, T5 9, T6 11, T7 13); the rest commented EXTRA or INVIABLE (most problem-statement scans carry handwriting), plus the EXTRA `t5-metacentre` sketch |
| Fluid Mechanics problems | `fluids_t5p.py`, `fluids_t6p.py`, `fluids_t7p.py`; `RASTER` in `tools/fluids_ns/` | in the same `FM-T*` folders | **Done 2026-11-21**: counted with the theory row above; deduction and free-body figures are EXTRA |
| Engineering Mechanics | `em_theory.py`, `em_solutions.py`, `em_midterm1.py` | `EM` 68 PNG (statements, already crops), `EM-T` 49 SVG, `EM-SOL` 217 SVG, `EM-M1` 20 SVG | **Done 2026-11-21** (theory): `EM-T` 26 crops (T6 12, T7 3, T8 11), 22 EXTRA (including `t6-half-wire`) and 1 INVIABLE (`t7-spring-pair`); `EM-SOL` and `EM-M1` stay EXTRA as deduction figures; the statements (`EM`) were already crops |
| Advanced Maths | `am_phase.py`, `am_portraits.py` | `AM-PS` 76 SVG | **Done 2026-11-21**: all EXTRA (computed answers to "sketch the phase portrait" and solution plots; the Ch3/Ch4 problem sheets print no figure), no crops |
| Aerospace Materials I bank | `materials_mt2.py`, `mat_mt2/` | `MAT-MT2` 116 SVG, `T2-problems` 10 SVG | Items written for the bank, not in any PDF: EXTRA (no change) |

Recount before starting a subject (counts change as other sessions work):

```bash
for f in tools/figures/*.py tools/figures/*/*.py; do echo "$f put=$(grep -c '\.put(' $f) raster=$(grep -cE '\.raster\(|^\s+R\(' $f)"; done
```

## 2. Procedure per topic

One topic per commit. Models as in `CLAUDE.md` (Model routing), organised as a fan-out:

- **Opus 5.5 (main session) orchestrates and decides; it does not read PDFs or crop.** It recounts the inventory, splits the subject into small jobs (one PDF, deck or topic per job, never a whole subject in one agent), writes one complete brief per job (files, figure names, output paths, what to report) and resolves every doubtful case the agents send back.
- **Haiku 5.5 does the reading and cropping, many agents in parallel.** Launch every independent job of a step in a single message, in the background (`run_in_background`), so they run at the same time; each agent gets its own PDF and its own output folder in the scratchpad, so no two agents write the same file. They follow the brief literally and report in at most 10 lines; anything not covered by the brief comes back to Opus.
- **Sonnet 5.5 reviews and wires.** A reviewer checks the Haiku output before anything is wired (opens a contact sheet of the crops and the classification table: cut labels, wrong figure, a crop that should be EXTRA) and returns only the rows to redo; a wiring agent then edits the modules, builds, runs the gates and commits. Wiring runs one topic at a time, because topics share `nav.json`, `source_links.json`, the manifest and `updates.js`.
- Keep the main session lean: read agent reports, never their transcripts or the PDFs.

Steps:

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
Lee AGENTS.md (regla "Figures from the official PDFs (Screenshot-First, every subject)") y docs/plans/2026-11-19-screenshot-first-migration.md: quiero migrar las figuras del portal a recortes de los PDFs oficiales siguiendo ese plan, igual que ya está hecho en Aerospace Materials I. Antes de tocar nada, recuenta el inventario (comando del §1), enséñame la tabla por asignatura y pregúntame con qué asignatura empezamos. Después trabaja tema a tema con el procedimiento del §2 (tú, Opus, organizas y decides; lanzas en paralelo muchos agentes Haiku 5.5, uno por PDF o tema, para clasificar y recortar; un Sonnet 5.5 revisa los recortes antes de cablear y otro Sonnet cablea, construye y pasa los gates), con commit y push por tema. No pases el humanizer. Para si llegas al 70 % del límite de 5 horas y dime qué queda.
```
