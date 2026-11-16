---
subject: "Repository"
tags:
  - repository
  - rules
  - engineering-mechanics
source: "Mission brief of 2026-11-14 (Engineering Mechanics complete)"
status: "in progress"
---

# Rules - EM Mission Progress

Progress log of the mission "Engineering Mechanics complete": theory for Topics 1 to 8, the 93 official problems (51 point particle, 42 rigid body) and the SVG geometry simulator. A new session starts by reading this note and `git log`; work marked as done is not repeated.

Related: [[Repository MOC]], [[Rules - AGENTS.md]], [[Rules - CLAUDE.md]], [[Tool - build_mech_problems]], [[Tool - build_topic_pages]].

## Milestones

| Milestone | Scope | State | Commit |
| :--- | :--- | :--- | :--- |
| Start-up | Skills read, rules read, inventory, this log | done | see `git log` (`docs(mechanics): open the EM mission progress log`) |
| Sources | Copy Lectures 6 to 10 into `sources/`, regenerate inventory, manifest, source notes and PDF pages | done (decks received 2026-11-14) | `feat(mechanics): add Lectures 6 to 10 to the sources` |
| Simulator engine | `assets/js/mechanics-3d-sim.js`, `assets/css/mechanics-3d-sim.css`, eight archetypes, `tools/tests/test_mechanics_sim.py` (19 tests), guide in [[Tool - mechanics-3d-sim]] | done | `7a177a1`, `43a8cd9` |
| H1 | Theory Topics 1 to 8, flavor `mechanics` in `build_topic_pages.py` | in progress: flavor and lecture citations being implemented (agent `tool-theory`); notes not started | |
| H2 | `no-inline-calc` gate, migration of the structure 2 problems, badges, extra-problems bank | in progress: contract in `tools/derivation.py` and `assets/css/derivation-box.css` done (`7a177a1`); builder upgrade in progress (agent `tool-problems`); solutions not started | |
| H3 | 42 rigid body problems (`rb-01` to `rb-42`, structure 4) | in progress: statements and keys being extracted (six agents, output in the session scratchpad `rb/`, figure crops in `vault/attachments/EM/T{6,7,8}-RB*.png`) | |
| H4 | `sim` block in the 93 notes, one commit per topic | not started | |
| H5 | Indexes, links, PDFs, updates, ultrareview | not started | |

## Starting inventory (2026-11-14)

- `tools/mech_problems.json`: 51 problems, 31 with `"structure": 2` and 20 with `"structure": 3`.
- Vault, `03 - Engineering Mechanics/`: 54 notes; theory notes Topic 1 to Topic 5, `Problem Set` and `Solution Set` for Topics 1 to 5, formula sheets. No note for Topics 6, 7 or 8.
- Portal, `subjects/engineering-mechanics/`: theory and problem pages `topic-1` to `topic-5`, the indexes, `extra-problems/`, `formula-sheet/`, `simulator/` (exam simulator), `sources/` and `exams/`.
- Sources: `teoria/Notes.pdf` (130 pages), `problemas/Problems.pdf` (81 pages), `schedule/weekly-planning-mechanics_G46.pdf`, and six decks in `unit-01` to `unit-05` (`00.pdf`, `01_-_Point_particle_kinematics.pdf`, `02.PointParticleDynamics.pdf`, `03_-_Constraints.pdf`, `04_-_Angular_momentum.pdf`, `05_-_Relative_motion.pdf`). The folders `unit-06-particle-systems`, `unit-07-rigid-body-kinematics` and `unit-08-rigid-body-dynamics` are empty.
- **The five new decks (Lectures 6 to 10) are not in the repository (working tree, `origin/main`, the session branch) and no file was uploaded to the session.** The mission stops here, as the brief orders, until they are provided.

## Blockers and open questions

1. Lectures 6 to 10 (oscillations and linearization, rigid body kinematics, inertia properties, momentum and energy, rigid body dynamics): the PDF files are needed.
2. The brief refers twice to "the previous version of this assignment" (the content breakdown of each theory topic; the split of the 42 rigid body problems into groups A to G and their badges). That text is not in the repository or in this session.
3. Target folders: see conflict 1 below.

## Conflicts between the brief and the repository (not resolved silently)

1. **Unit folder names.** The brief copies the decks to `unit-02-dynamics-point-particle/`, `unit-06-kinematics-rigid-bodies-inertia/` and `unit-07-dynamics-rigid-bodies/`. The repository has `unit-02-dynamics-point-particle/`, `unit-06-particle-systems/` (empty), `unit-07-rigid-body-kinematics/` (empty) and `unit-08-rigid-body-dynamics/` (empty). Options: reuse the existing folders, or rename them to the names of the brief (which regenerates the inventory, the manifest and the source notes). Waiting for the decision.
2. **Deck numbering.** The brief cites "deck 07-relative-motion" and calls angular momentum "Lecture 5"; on disk the decks are `04_-_Angular_momentum.pdf` and `05_-_Relative_motion.pdf`. Citations will follow the numbering printed on the slides once the new decks can be read.
3. **Theory note names.** The brief names `Topic 1 - Kinematics of a Point Particle` and `Topic 2 - Dynamics of a Point Particle, Equilibrium and Oscillations`; the vault has `Topic 1 - Fundamentals and Particle Kinematics` and `Topic 2 - Point Particle Dynamics`. They will be renamed with `tools/vault_rename.py` (wikilinks rewritten), which is consistent with `AGENTS.md`.
4. **Model routing.** `CLAUDE.md` has three tiers; the brief adds a fourth (orchestration and highest-risk code in the main session) and asks to pass `model` on every spawn even where the agent frontmatter differs. This is an explicit addition of the brief and will be written into `CLAUDE.md`.
5. **Structure 4 and `.derivation-box`.** `AGENTS.md` knows structures 2 and 3 and the `phase-block` class. The brief adds structure 4 (rigid body order) and the `no-inline-calc` rule; both are explicit additions and will be written into `AGENTS.md` with the tool change.
6. **task-observer workspace.** The skill wants a stable path outside the checkout; this cloud container is ephemeral and has none. Observations of this mission are kept in this note until a stable path is pinned.

## Checks against `weekly-planning-mechanics_G46.pdf` (done)

- Point particle in-class sessions: Session 2 (Problem 1), Session 4 (11, 16, 17), Session 6 (29, 32), Session 8 (19, 43), Session 10 (7, 27), Session 12 (34, 38), Session 13 (35, 49). The fourteen problems of the brief match the schedule.
- Rigid body in-class sessions: Session 17 (1, 3, 4 only the letter T, 5 only the cone), Session 19 (6, 8), Session 20 (20), Session 21 (17, 24), Session 22 (13), Session 23 (11, 15), Session 25 (28, 32), Session 26 (41).
- The schedule does not list the problems of the badge `Oscillations - Lecture 6` (12, 24, 34f, 35f, 45, 46, 50f); it only places "Equilibrium and oscillations" in Session 11. That list has to be checked against the Lecture 6 deck.

## Update 2026-11-14: decks and earlier brief received

- The five decks were uploaded and copied to the paths of the brief. The folders were renamed to the names of the brief (conflict 1 closed): `unit-02-particle-dynamics` to `unit-02-dynamics-point-particle`, the empty `unit-06-particle-systems` to `unit-06-kinematics-rigid-bodies-inertia` and the empty `unit-07-rigid-body-kinematics` to `unit-07-dynamics-rigid-bodies`. `unit-08-rigid-body-dynamics` stays empty (Topic 8 has no deck). The decks print their own numbers on the title slide ("6. Oscillations" to "10. Rigid body dynamics"), so citations use `[Lecture N, Slide M]` with those numbers.
- `update_inventory.py` also rewrote the README of the other four subjects (drift from before this mission); those changes were left out of the commit.
- The earlier brief was provided. Its split of the 42 rigid body problems (to be verified page by page against `Problems.pdf`):

| Page | Group | Problems (`rb-NN` = number in `Problems.pdf` section 2) |
| :--- | :--- | :--- |
| `topic-6.html` (8) | A, rigid body kinematics, Euler angles, instantaneous axis (Lecture 7, Ch. 9) | 01, 02, 03, 11, 34, 35 |
| | B, mass geometry, Steiner, principal axes (Lecture 8, Ch. 10) | 04, 05 |
| `topic-7.html` (8) | C, linear and angular momentum, kinetic energy (Lecture 9, Ch. 11) | 06, 07 |
| | D, planar and 3D dynamics, equilibrium, linearized oscillations (Lectures 10 and 6, Ch. 5 and 12) | 08, 09, 10, 24, 25, 38 |
| `topic-8.html` (26) | E, rolling with and without slip, unilateral constraints (Ch. 13.1 to 13.3) | 12, 13, 14, 15, 16, 18, 19, 22, 23, 28, 33, 37, 39, 40, 41 |
| | F, multibody systems and exploded views (Ch. 13.4) | 17, 20, 21, 26, 27, 29, 31, 36, 42 |
| | G, torque-free motion, Poinsot, gyroscopes (Ch. 15) | 30, 32 |

- In-class badges of the rigid body problems, as checked against the schedule: Session 17 (01, 03, 04 letter T, 05 cone), 19 (06, 08), 20 (20), 21 (17, 24), 22 (13), 23 (11, 15), 25 (28, 32), 26 (41). They match the earlier brief.
- Theory breakdown per topic: as listed in the earlier brief (Topic 6: orthogonal matrices, Euler angles 3-1-3 and 3-2-1, additivity of the angular velocity, velocity and acceleration fields, helical motion, instantaneous axis, centre of mass, inertia tensor, change of basis of the tensor, Steiner, principal values and directions, the three symmetry theorems, flat plate. Topic 7: linear momentum, angular momentum about an arbitrary point, change of pole, kinetic energy, Koenig, moment equation, Euler equations, gravity reduced at G, work and energy, planar dynamics. Topic 8: rigid body constraints, rolling with and without slip, indeterminate reactions, exploded views, the ten-step recipe of Ch. 14, torque-free motion of Ch. 15).

## Update 2026-11-14 (evening): decisions taken while building

- **Scope of the derivation-box rule.** The 20 Topic 5 solutions already in structure 3 are full of calculations in prose, so the rule means rewriting all 51 particle solutions, not only the 31 in structure 2. Until each is rewritten it carries `"boxed": false` in `tools/mech_problems.json`, which exempts it from the gate; the mission ends with no such flag.
- **Gate, as implemented** (`derivation.gate`): outside a box, inline maths in a paragraph or list item may not contain `=`, `\dot`, `\ddot`, `\times`, `\frac` or `\int`, and no display formula stands outside a box. Table cells are not checked (definitions go in tables). Statements are not checked (they are verbatim).
- **Simulator configuration.** The brief puts `sim` in the note frontmatter; the Solution Set notes hold many problems each, so the configuration is a callout inside each problem (`> [!example] Interactive simulator` and a `> sim: {...}` line). Readouts are arithmetic expressions evaluated by the script (no `eval`), so each problem shows the formulas of its own solution.
- **Matrix notation.** The brief writes the matrix as [B1B0]; `Notes.pdf` (chapter 1) writes it with a left and a right subscript, 0 and 1 around R, columns being the rotated unit vectors in the fixed basis. The simulator and the solutions follow `Notes.pdf`.
- **Page numbers of `Problems.pdf`.** The brief gives printed footer numbers; the repository cites the PDF page index (footer plus one), which is what the deep links open. Rigid body statements are on PDF pages 37 to 71 and the keys on 77 to 81.
- **Unit folders.** All three renames of the brief were done (see the first update).
- **Browser in cloud sessions.** `/usr/bin/google-chrome` hangs in the cloud container; the tools find a browser by name, so a wrapper named `msedge` on the PATH that runs the preinstalled `chrome-headless-shell` with `--no-sandbox` makes `build_pdfs`, `render_check` and the browser tests work (full suite: 367 tests in about two minutes). KaTeX for the PDFs comes from the npm package (`npm pack katex@0.16.8`), passed with `--katex`.
- **Usage limits.** The subagents stopped once on the account's five-hour usage limit and were resumed after the reset. The mission needs several such windows; this log and `git log` are the resume points.

## Work plan from here (per batch of 4 to 6 problems)

1. A solver (Opus) writes each solution as a part file with derivation boxes, the figure briefs and the simulator line.
2. A figure agent (Sonnet) writes one module per problem under `tools/figures/em_sol/`, renders and inspects every figure.
3. The auditor (`problem-step-mentor`, Opus) reads the batch; findings are verified by the orchestrator before they are fixed.
4. The orchestrator assembles the part files into the Solution Set note, runs the builders and gates, prints the PDFs and commits (one commit per topic).

## Update 2026-11-15: tools ready, rigid body statements in the vault

- Done and committed: `tools/build_mech_problems.py` (derivation boxes, gate, structure 4, topics 6 to 8 and `rb-NN` cards, group headings, extra badges, simulator callout), `tools/build_topic_pages.py` flavor `mechanics`, lecture citations `[Lecture N, Slide M]` in `tools/source_links.py`, the three rigid body Problem Set notes (42 statements, 39 figure crops) and [[Problem Set - Rigid Body Official Key]] (20 problems have a printed answer, 22 have none).
- Class badges of the particle problems are on the pages (checked against the schedule). The theory notes of Topics 1 and 2 were renamed to the names of the brief.
- **Conflict: chapter numbers of `Notes.pdf`.** The brief maps Topic 2 to chapters 3 to 5, Topic 3 to chapter 6, Topic 4 to chapter 7 and Topic 5 to chapter 8. The printed chapters are: 1 getting started, 2 kinematics of point particles, 3 relative motion, 4 dynamics of the point particle, 5 the harmonic oscillator, 6 constraints and reaction forces, 7 the Newtonian approach I, 8 Kepler's problem, 9 to 15 as the brief says. The notes are written against the printed chapters: Topic 1 chapters 1 and 2; Topic 2 chapters 4 and 5; Topic 3 chapters 6 and 7; Topic 4 the angular momentum part of chapter 4 and chapter 8; Topic 5 chapter 3. In `Notes.pdf` the PDF page is the printed page plus one.
- In progress: pilot batch of solutions (Topic 1, problems 1 to 6) and the theory notes of Topics 6, 7 and 8. Part files and briefs live in the session scratchpad (`sol/`, `theory/`, `SOLVER_BRIEF.md`, `THEORY_BRIEF.md`, `check_part.py`, `check_theory.py`); they are lost if the container is recycled, the committed notes are not.

## Update 2026-11-15 (second session, branch `claude/loving-hypatia-fddsfv`)

- The work of `claude/practical-newton-p5p22y` was fast-forwarded into this branch. The container was recycled, so the scratchpad drafts (pilot solutions of Topic 1 problems 1 to 6, drafts of Topic 2, the agent briefs) are lost and will be rewritten. To avoid a second loss, the solver brief is now in the repository (`tools/briefs/RB_SOLVER_BRIEF.md`) and the figure briefs in `tools/figures/em_sol/briefs/rbNN.md`; both folders are deleted when the mission closes.
- **Order changed by the user:** rigid body first (theory pages 6 to 8, then the 42 problems), particle afterwards; and **one agent at a time**, no parallel teams.
- Rigid body theory: the three pages are registered in `tools/topic_pages.json` (flavor `mechanics`). Topic 7 builds and renders clean (458 formulas, 0 KaTeX errors, local KaTeX). Topics 6 and 8 wait for their figure modules (`tools/figures/em_th/t6.py`, `t8.py`, in progress).
- Rigid body solutions: the note `Solution Set - Topic 6 Rigid Body Kinematics and Inertia` exists with RB-34 (the model of the format), RB-35 and RB-01 (matches the key). Their figures are briefed, not drawn yet. The simulator line of each problem is left for milestone H4.
- Rendering in the cloud: `render_check` is run through a wrapper that swaps the KaTeX CDN for the npm copy (the CDN answers 403 here); the browser is the wrapper `msedge` described above.
- **Rigid body theory done** (`971d2ba`): pages `teoria/topic-6.html`, `topic-7.html`, `topic-8.html`, figure modules `em_th/t6.py` and `t8.py` (28 figures), anchors of `Notes.pdf` chapters 9 to 15 added to `tools/source_anchors.json` (only the `em-notes` block was refreshed: a full `--refresh-anchors` in this container also moved anchors of other subjects and was discarded), theory index, portal badge (8 of 8 units), side menu, PDFs, What's new entry. Gates: `build_topic_pages`, `source_links`, `build_nav`, `build_pdfs`, `audit_portal`, `build_source_notes`, `sources_manifest`, `build_sources_pages` all clean; `render_check` clean on the edited pages (local KaTeX).
- Fixed on the way: mechanics theory pages did not define `--text-faint`, so the grey axes of every figure were invisible on screen (now set in `MECH_CSS`); seven `\text{...}` reasons of the Topic 8 note had a bare underscore.
- **Open, to restore later:** the practice link of the three theory pages points to `../problemas/index.html` until `problemas/topic-6..8.html` exist; then set it back to the topic page in `tools/topic_pages.json`.
- **Open, small:** labels touching a line in `t8-disk-slip` (the angular velocity label on the rim), `t8-poinsot` ("polhode") and `t8-disk-rolling`; to fix in the figure pass of the rigid body problems.
- **Known red gate while Topic 6 solutions are incomplete:** `build_mech_problems --check` (missing solutions and figures not drawn yet) and its test `test_pages_are_up_to_date_with_their_notes`; the other 406 tests pass. `vault_lint` reports only the five figure embeds of RB-01, RB-34 and RB-35 that are not drawn yet.
- Test suite command: `python -m unittest discover -s tools/tests` (the `-t .` of the brief fails: `tools/tests` is not a package).
- **Topic 6 solutions written** (`8a3f56f`): RB-01, 02, 03, 04, 05, 11, 34, 35 in the Solution Set note. Against the key: RB-01, 02, 03, 11 match; RB-04 matches for the T (I and C have no key); RB-05 matches for (a) to (g), (h) to (j) have no key; RB-34 and RB-35 have no key. Figures (29) are being drawn (`tools/figures/em_sol/rbNN.py`).
- **Gap found in the theory:** the note `Topic 6 - Kinematics of Rigid Bodies and Inertia Properties` ends with chapter 9 (degrees of freedom). Chapter 10 of `Notes.pdf` and Lecture 8 (centre of mass, tensor of inertia, change of basis of the tensor, Steiner, principal axes, symmetry theorems, flat plate) are not written yet. To do before Topic 6 is closed: write those sections (Opus), draw their figures, rebuild the page and the PDF, and correct the card of the theory index if needed.
- **Simulator callouts:** the solvers were told to add none; they are added for all problems in milestone H4.

## Update 2026-11-16: particle problems, branch `claude/practical-newton-p5p22y-particle`

- This branch holds the rewrite of the particle solutions with derivation boxes (brief: `tools/briefs/P_SOLVER_BRIEF.md`; per batch: solver, figure agent, read-only auditor, fixes verified one by one; one agent at a time). It started from `ebc5575` of the mission branch, so the rigid body pages and solutions written afterwards on other branches are not here.
- **Topic 1** (problems 1 to 9) and **Topic 2** (10 to 17, 45, 46): done, pages and PDFs built (`a3c486a` for Topic 2).
- **Topic 3 done** (18, 19, 23, 24, 29, 31, 32, 35, 38, 39, 48, 50): twelve solutions in structure 3, 37 deduction figures, page `problemas/topic-3.html` and its 13 PDFs rebuilt. Against the key: 18 to 31 as recorded in their audit; 32, 35, 38 and 39 match; 48 and 50 print no answer and carry independent checks. No discrepancy callout was needed. The audit of the second batch gave 21 findings (one wrong sentence on the first-order frequency shift in 35, one wrong description of the starting point in 38, merged rows, incomplete orthogonality checks, two misplaced citations, eight figure defects); all were verified and applied.
- **Tool change:** `build_mech_problems.py` now holds a page back only for errors of its own problems (before, any error anywhere blocked every page, so the unfinished rigid body figures of this branch blocked Topic 3). The exit code still fails on any error.
- **Topic 4 done** (42, 43, 44, the whole topic): three solutions in structure 3, 13 figures (the effective potentials, the radial band and the orbit are computed from the formulas), page `problemas/topic-4.html` and its PDFs rebuilt. `Problems.pdf` prints no answer for any of the three (verified on PDF p. 76); each carries independent checks. The audit gave 15 findings, all verified and applied. Erratum recorded in Problem 42: property 5 of `Notes.pdf`, Sec. 4.8.1 (the particle never reaches O unless the angular momentum is zero) fails for the attractive power law with exponent 3 (strength at or above the square of the areal constant) and exponent 4; the proof is in a box. Two phrases of the statement of Problem 42 that had been edited were restored word for word. No problem is left in structure 2.
- **Remaining particle work:** Topic 5 (20 problems with `"boxed": false`), then the simulator callouts (milestone H4; each `tools/figures/em_sol/briefs/pNN.md` ends with the proposed `sim` line).
- **Known red on this branch, not from the particle work:** `build_mech_problems --check` reports the Topic 6 rigid body figures not drawn here (`rb-04`, `rb-05`, `rb-34`, `rb-35`), label overlaps in `rb11-*` and a stale `topic-6.html`; they are solved on the rigid body branch and disappear at the merge.
- Cloud set-up used again: wrapper `msedge` for `chrome-headless-shell --no-sandbox`, KaTeX from `npm pack katex@0.16.8` passed with `--katex`, portal fonts downloaded from Google Fonts into `~/.fonts`; `render_check` run on a mirror made with `build_pdfs._mirror`.
