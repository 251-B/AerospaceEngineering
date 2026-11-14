---
subject: "Repository"
tags:
  - repository
  - rules
  - engineering-mechanics
source: "Mission brief of 2026-11-14 (Engineering Mechanics complete)"
status: "blocked"
---

# Rules - EM Mission Progress

Progress log of the mission "Engineering Mechanics complete": theory for Topics 1 to 8, the 93 official problems (51 point particle, 42 rigid body) and the SVG geometry simulator. A new session starts by reading this note and `git log`; work marked as done is not repeated.

Related: [[Repository MOC]], [[Rules - AGENTS.md]], [[Rules - CLAUDE.md]], [[Tool - build_mech_problems]], [[Tool - build_topic_pages]].

## Milestones

| Milestone | Scope | State | Commit |
| :--- | :--- | :--- | :--- |
| Start-up | Skills read, rules read, inventory, this log | done | see `git log` (`docs(mechanics): open the EM mission progress log`) |
| Sources | Copy Lectures 6 to 10 into `sources/`, regenerate inventory, manifest, source notes and PDF pages | **blocked** (decks not available) | |
| Simulator engine | `assets/js/mechanics-3d-sim.js`, `assets/css/mechanics-3d-sim.css`, eight archetypes, `tools/tests/test_mechanics_sim.py` | not started | |
| H1 | Theory Topics 1 to 8, flavor `mechanics` in `build_topic_pages.py` | not started (Topics 2, 6, 7 need the decks) | |
| H2 | `no-inline-calc` gate, migration of the structure 2 problems, badges, extra-problems bank | not started | |
| H3 | 42 rigid body problems (`rb-01` to `rb-42`, structure 4) | not started | |
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

1. **Unit folder names.** The brief copies the decks to `unit-02-dynamics-point-particle/`, `unit-06-kinematics-rigid-bodies-inertia/` and `unit-07-dynamics-rigid-bodies/`. The repository has `unit-02-particle-dynamics/`, `unit-06-particle-systems/` (empty), `unit-07-rigid-body-kinematics/` (empty) and `unit-08-rigid-body-dynamics/` (empty). Options: reuse the existing folders, or rename them to the names of the brief (which regenerates the inventory, the manifest and the source notes). Waiting for the decision.
2. **Deck numbering.** The brief cites "deck 07-relative-motion" and calls angular momentum "Lecture 5"; on disk the decks are `04_-_Angular_momentum.pdf` and `05_-_Relative_motion.pdf`. Citations will follow the numbering printed on the slides once the new decks can be read.
3. **Theory note names.** The brief names `Topic 1 - Kinematics of a Point Particle` and `Topic 2 - Dynamics of a Point Particle, Equilibrium and Oscillations`; the vault has `Topic 1 - Fundamentals and Particle Kinematics` and `Topic 2 - Point Particle Dynamics`. They will be renamed with `tools/vault_rename.py` (wikilinks rewritten), which is consistent with `AGENTS.md`.
4. **Model routing.** `CLAUDE.md` has three tiers; the brief adds a fourth (orchestration and highest-risk code in the main session) and asks to pass `model` on every spawn even where the agent frontmatter differs. This is an explicit addition of the brief and will be written into `CLAUDE.md`.
5. **Structure 4 and `.derivation-box`.** `AGENTS.md` knows structures 2 and 3 and the `phase-block` class. The brief adds structure 4 (rigid body order) and the `no-inline-calc` rule; both are explicit additions and will be written into `AGENTS.md` with the tool change.
6. **task-observer workspace.** The skill wants a stable path outside the checkout; this cloud container is ephemeral and has none. Observations of this mission are kept in this note until a stable path is pinned.

## Checks against `weekly-planning-mechanics_G46.pdf` (done)

- Point particle in-class sessions: Session 2 (Problem 1), Session 4 (11, 16, 17), Session 6 (29, 32), Session 8 (19, 43), Session 10 (7, 27), Session 12 (34, 38), Session 13 (35, 49). The fourteen problems of the brief match the schedule.
- Rigid body in-class sessions: Session 17 (1, 3, 4 only the letter T, 5 only the cone), Session 19 (6, 8), Session 20 (20), Session 21 (17, 24), Session 22 (13), Session 23 (11, 15), Session 25 (28, 32), Session 26 (41).
- The schedule does not list the problems of the badge `Oscillations - Lecture 6` (12, 24, 34f, 35f, 45, 46, 50f); it only places "Equilibrium and oscillations" in Session 11. That list has to be checked against the Lecture 6 deck.
