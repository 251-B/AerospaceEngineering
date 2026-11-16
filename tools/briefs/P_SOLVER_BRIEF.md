# Brief: rewriting a batch of particle problems (Engineering Mechanics, structure 3)

Working brief for the agent that rewrites the worked solutions of the particle problems `NN` (01 to 51). It is deleted
when the mission closes. The orchestrator names the problems of the batch; everything else is here.

**First read `tools/briefs/RB_SOLVER_BRIEF.md` completely**: the derivation-box syntax, the gate `no-inline-calc`, the
first-principles rules, the explanation standard, the integrity rules and the figure rules are the same. Only the
differences below change. Model of the style: the six finished solutions of
`vault/03 - Engineering Mechanics/Solution Set - Topic 1 Particle Kinematics.md` (read two of them) and, for the
rigid body form, `## Problem RB-34` of `Solution Set - Topic 6 ...md`.

## What you write

For each problem of the batch, REPLACE its section in the solution note of its topic (the section starts with
`## Problem NN: ...` or `## 📌 Problem NN: ...` and ends before the next `## ` heading; write the new one as
`## Problem NN: <title exactly as in the Problem Set note>`; never touch the sections of other problems):

| Topic | Solution note in `vault/03 - Engineering Mechanics/` | Tools you may use (printed chapters of `Notes.pdf`; PDF page = printed + 1) |
| :--- | :--- | :--- |
| 1 | `Solution Set - Topic 1 Particle Kinematics.md` | ch. 1-2 (PDF 10-36); Lecture 1 |
| 2 | `Solution Set - Topic 2 Point Particle Dynamics.md` | ch. 1-2, 4 (dynamics, PDF 42-54), 5 (harmonic oscillator, PDF 55-61); Lectures 1, 2, 6 |
| 3 | `Solution Set - Topic 3 Constraints and Reaction Forces.md` | ch. 1-2, 4-7 (constraints PDF 62-66; Newtonian approach I PDF 67-71); Lectures 1-3, 6 |
| 4 | `Solution Set - Topic 4 Angular Momentum and Central Forces.md` | ch. 1-2, 4-8 (Kepler PDF 72-75); Lectures 1-4, 6 |
| 5 | `Solution Set - Topic 5 Relative Motion.md` | ch. 1-8 (relative motion, ch. 3, PDF 37-41); Lectures 1-6 |

In `tools/mech_problems.json` set, for each of your problems, `"structure": 3` and DELETE the key `"boxed"` (an entry
without `"boxed": false` is gated). Change no other key and no other entry.

Sections of a solution (structure 3), all headings spelled exactly, in this order:

```
## Problem NN: <title>
### Reference Frames, Bases and Coordinates
### Change of Basis and Position Vector
### Kinematics
### Forces and Equations of Motion        (omit only when the problem has no dynamics)
### Answers and Checks
```
`### Answers and Checks` holds a table with the explicit answer to every part of the statement, then either the bold
line `**Check against the official key:**` (always present: when the PDF prints no answer for the problem, say so in that
line and give an independent check instead) and limiting cases (each in a box). Separate problems with `---`.

## Sources

- Statement, verbatim: `Problem Set - Topic N ...md`, section `## 📌 Problem NN` (figure in `vault/attachments/EM/`,
  open it with the Read tool).
- Official key of the particle problems: `sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf`,
  PDF pages 72-77 (numbered like the problems; a number with nothing after it means no key). Cite statements as
  `Problems.pdf, p. N` with the PDF page index.
- Current solution in the note: legacy text with calculations in prose (some in "Phase" layout). Reuse its mathematics
  where correct, but re-derive and verify every step yourself, and keep its confirmed discrepancy or erratum findings.
- Unfinished drafts of earlier attempts may exist in the session scratchpad (`.../scratchpad/sol/pNN.md`, with a
  `pNN.figs.md`): if present, read them as drafts, verify every line, and reuse what is right.
- Theory notes (`Topic N - ...md`) are written after the solutions: do not rely on them. Cite equations of `Notes.pdf`
  that you have seen on the page (`pdftotext -f P -l P`), never invent a number.
- Slides: cite `[Lecture N, Slide M]` only when the number M is the PDF page index of the deck AND that page shows the
  content (the links open the PDF page M). Lecture 1 has a slide map in `tools/source_links.json`; for the other decks
  verify. When in doubt cite `Notes.pdf` only.
- Decks: Lecture 1 `unit-01-particle-kinematics/slides/01_-_Point_particle_kinematics.pdf`; 2 `unit-02-dynamics-point-particle/slides/02.PointParticleDynamics.pdf`;
  3 `unit-03-constraints-reactions/slides/03_-_Constraints.pdf`; 4 `unit-04-angular-momentum-central-forces/slides/04_-_Angular_momentum.pdf`;
  5 `unit-05-relative-motion/slides/05_-_Relative_motion.pdf`; 6 `unit-02-dynamics-point-particle/slides/06-oscillations-and-linearization.pdf`
  (all under `sources/cuatrimestre-1/03-engineering-mechanics/`).

## Figures and the simulator

Figure names: `![[attachments/EM-SOL/pNN-<slug>.svg]]` (lower case, hyphens). For each problem write
`tools/figures/em_sol/briefs/pNN.md` (replace it if it exists) with, per embed, the block of the RB brief (View, Draw,
Values to draw, Alt, Caption) under `## pNN-<slug>`. Some problems already have a figure module
`tools/figures/em_sol/pNN.py` from an earlier session: look at it; where a figure still fits the new solution keep its
name and say "exists, unchanged" in the brief; where the solution changed, write the full brief of the new version; figures
of the old module that the new text no longer embeds are listed under `## to remove`. You write no Python.

Required per problem: one 2D view per rotation (axis out of the paper or into it, fixed axes grey, rotated axes
coloured, the angle marked between both pairs of axes); the main plane or meridian section with the shaded right
triangles that justify each sine and cosine and the position vector built step by step; and, for every problem with
forces, the free-body diagram with the applied forces, the reactions and (moving frames) the inertia forces.

The simulator is not connected yet: do NOT write a `> [!example] Interactive simulator` callout. Instead end each
`pNN.md` brief with
```
## simulator configuration (to connect in milestone H4)
```
a fenced block holding ONE line `sim: {"archetype": ..., "params": {...}, "defaults": {...}, "readouts": [...]}` as
described in `vault/06 - Repository/Tool - mechanics-3d-sim.md` (default state = the data of the statement; readouts =
2 to 5 key formulas of your solution as arithmetic expressions). If no archetype can draw the geometry, write one line
saying so and name the closest one.

## Checking your work

```bash
python3 tools/build_mech_problems.py --check 2>&1 | grep -E "problem (NN|MM)"
```
The only messages allowed to remain for your problems are `unknown figure pNN-...` (the figures are drawn after you).
Fix every other message, including `no-inline-calc` findings. Messages about `rb-NN` problems are not yours. Then
re-read each solution once as a student: any step skipped, any sign unexplained, any number unverified? Recompute every
numeric result independently (`python3 -c ...`, sympy or plain arithmetic) before you finish.

## Report back (short)

Per problem: result versus the official key (match / match after conversion / discrepancy / no key), the figures
briefed, anything in the statement or key you had to interpret (hypotheses taken), and the final output of the check
command. You do not commit, do not push, do not spawn agents, do not run the page builder in write mode.
