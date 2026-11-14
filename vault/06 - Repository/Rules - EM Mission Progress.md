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
