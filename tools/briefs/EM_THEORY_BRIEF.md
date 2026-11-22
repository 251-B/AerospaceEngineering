# Brief: writing an Engineering Mechanics theory note (Topics 1 to 5, flavor `mechanics`)

Working brief for the agent that writes (or rewrites) one theory note of Engineering Mechanics, Topics 1 to 5 (point
particle). It is deleted when the mission closes. The orchestrator names the topic and the part (sections) of the
batch; everything else is here. Read `AGENTS.md`, sections "Problem-solving standard" and "Engineering Mechanics:
derivation boxes, first principles and the rigid body order", before you start.

## What you write

One note, `vault/03 - Engineering Mechanics/Topic N - <name>.md` (the file already exists with an older text without
derivation boxes: you REPLACE its body; keep the file name). The page `subjects/engineering-mechanics/teoria/topic-N.html`
is generated from it later by `tools/build_topic_pages.py`; you never edit HTML. You also write the figure briefs of the
note, `tools/figures/em_th/briefs/tN.md` (format below). You write no Python.

| Topic | Note | Sources (printed chapters of `Notes.pdf`; PDF page = printed page + 1) | Decks |
| :--- | :--- | :--- | :--- |
| 1 | `Topic 1 - Kinematics of a Point Particle.md` | Ch. 1 Getting started (printed 9-26) and Ch. 2 Kinematics of point particles (27-35) | Lecture 1 |
| 2 | `Topic 2 - Dynamics of a Point Particle, Equilibrium and Oscillations.md` | Ch. 4, Secs. 4.1 to 4.7 (printed 41-~49) and Ch. 5 The harmonic oscillator (54-60) | Lectures 2 and 6 |
| 3 | `Topic 3 - Constraints and Reaction Forces.md` | Ch. 6 Constraints and reaction forces (61-65) and Ch. 7 The Newtonian mechanics approach I (66-70) | Lecture 3 |
| 4 | `Topic 4 - Angular Momentum and Central Forces.md` | Ch. 4, Sec. 4.8 Angular momentum and torque with 4.8.1 Central force motion, and Ch. 8 Kepler's problem (71-74) | Lecture 4 |
| 5 | `Topic 5 - Relative Motion.md` | Ch. 3 Relative motion (36-40) and Ch. 4, Sec. 4.9 Dynamics of relative motion | Lecture 5 |

Decks (under `sources/cuatrimestre-1/03-engineering-mechanics/`). Their lecture number is the number printed on their
title slide: Lecture 1 `unit-01-particle-kinematics/slides/01_-_Point_particle_kinematics.pdf`; Lecture 2
`unit-02-dynamics-point-particle/slides/02.PointParticleDynamics.pdf`; Lecture 3
`unit-03-constraints-reactions/slides/03_-_Constraints.pdf`; Lecture 4
`unit-04-angular-momentum-central-forces/slides/04_-_Angular_momentum.pdf`; Lecture 5
`unit-05-relative-motion/slides/05_-_Relative_motion.pdf`; Lecture 6
`unit-02-dynamics-point-particle/slides/06-oscillations-and-linearization.pdf`. (`unit-01-.../00.pdf` is the course
presentation and is not cited.)

Topic 2 must cover Lecture 6 completely: free oscillator, forced oscillator, resonance, beats, damped oscillator with
damping ratio below, equal to and above one, the amplification factor as a function of the frequency ratio and the
phase lag, Taylor linearisation about an equilibrium, and the bead on a rotating hoop with its effective potential and
the bifurcation at the critical rotation rate. Topic 4 takes from Ch. 4 only Sec. 4.8; Topic 5 takes Sec. 4.9.

## Read first

1. The model of the format, exactly: `Topic 6 - Kinematics of Rigid Bodies and Inertia Properties.md` (same folder):
   read its first 300 lines and one worked example completely. Copy its structure: YAML frontmatter (title, subject,
   course, source, type, language, tags), `# Topic N - ...`, ONE first blockquote line `> ...` with the central idea of
   the topic (prose, atomic maths only), a paragraph saying which chapters, equations and slides the note follows, a
   table of symbols, then sections `## 1. Title`, `## 2. Title`, ... with `###` sub-headings.
2. The sources, page by page, BEFORE writing a section: `pdftotext -layout -f A -l B <pdf> -` on the pages of that
   section of `Notes.pdf` and the matching slides. Follow the notes equation by equation, in their order, and the
   slides slide by slide. Never invent an equation, a number or a figure.
3. The current note and the current hand-written page `subjects/engineering-mechanics/teoria/topic-N.html` (and
   `git show HEAD:<path>` if needed): they hold earlier explanations and examples. Keep every correct and useful piece of
   content (rewritten into the new format); content that is not in the sources is either removed or marked extension.
   The `Concept - ...` notes of the same folder may be linked with `See also [[...]]` lines (that line is not rendered).

## The five laws (the build fails, or the audit rejects the note, if one is broken)

1. **No calculation in prose (`no-inline-calc`).** Outside a derivation box, paragraphs and list items carry only
   atomic identifiers in maths (`$m$`, `$\theta$`, `$\mathbf r_0^P$`, `$S_1$`): no `=`, `\dot`, `\ddot`, `\times`,
   `\frac`, `\dfrac`, `\tfrac`, `\int` inside `$...$`, and no `$$` at all. This also holds inside `[!key]`, `[!info]`,
   `[!warning]` and `[!example]` callouts and in list items. Definitions of symbols and data go in tables (table cells
   are not checked). Every development goes in a box:

   ```
   > [!derivation] Title of the step
   > **Law:** the principle invoked
   > **Source:** Notes.pdf, Eq. 2.6; [Lecture 1, Slide 14]
   >
   > (optional sentences, lists and a figure embed)
   >
   > $$\begin{aligned}
   > \mathbf v_0^P &= \frac{d}{dt}\mathbf r_0^P \quad &\text{(definition of velocity)} \\
   > &= \dot x\,\mathbf i_0 + \dot y\,\mathbf j_0 \quad &\text{(the basis of $S_0$ is fixed)}
   > \end{aligned}$$
   >
   > $$\boxed{\mathbf v_0^P = \dot x\,\mathbf i_0 + \dot y\,\mathbf j_0}$$
   >
   > **Units:** $[\mathrm{L\,T^{-1}}]$, each term written out
   > **Meaning:** the physical reading of the result (true to first order, every number recomputed)
   ```
   ONE operation per aligned row, each row with its reason `\quad &\text{(...)}`. Matrix and determinant rows inside a
   box use `\cr` (not `\\`) inside `\begin{pmatrix}...\end{pmatrix}`/`\begin{vmatrix}`, because `\\` ends the aligned row.
   Write citations OUTSIDE `$...$` so that they become links. Accepted citation forms: `Notes.pdf, Eq. X.Y`,
   `Notes.pdf, Sec. X.Y`, `Notes.pdf, Ch. N`, `Notes.pdf, p. N`, `[Lecture N, Slide M]`, `[Lecture N, Slides M-K]`.
   Other callouts: `> [!key] Title` (a summary), `> [!info] Extension: ...` (beyond the course; the title must start
   with "Extension"), `> [!warning] Title` (pitfalls, discrepancies with the sources), `> [!example] Title` (the
   statement of a worked example: prose and a data table only; its solution follows as derivation boxes right after
   it). A derivation box whose title starts with "Extension" is shown as an extension.
2. **Always from first principles.** Nothing starts from a memorised formula (polar, cylindrical or spherical
   acceleration components, the centrifugal shortcut instead of the double vector product written out, a tabulated
   result). The chain is: position vector → change of basis matrices (with the determinant and at least one diagonal
   and one off-diagonal entry of R Rᵀ = I written out) and the derivatives of the unit vectors → velocity →
   acceleration → Newton. Every integral: antiderivative, substitution with its differential, Barrow's rule with both
   limits substituted. Every chain rule written as such; every derivative written before it is used; every vector
   product expanded (distributive row, then the products of unit vectors) before its result. In a theory note you may
   cite an earlier equation of the same or an earlier chapter instead of re-deriving it, but the equation that the
   section of the notes derives is derived in the box, in the order the notes derive it.
3. **Deductive figures** wherever there are vectors, projections, triangles or a change of basis: one 2D view per
   rotation (axis out of the paper ⊙ or into it ⊗, fixed axes grey, rotated axes coloured, the angle marked between
   both pairs of axes, the 3×3 matrix in the box beside it); the main plane with the right triangles shaded and the
   hypotenuse, the adjacent leg (cosine) and the opposite leg (sine) labelled; free-body diagrams with every applied
   force and reaction (and the inertia forces in a moving frame). Redraw the key figures of the notes and slides (cite
   them: "Notes.pdf Fig. 2.3", "[Lecture 1, Slide 12]"). Embed each one on its own line as
   `![[attachments/EM-T/tN-<slug>.svg]]` (lower case, hyphens; N = topic number) where it is needed, inside a box or
   between boxes.
4. **Nothing is "obvious".** Every sine or cosine names its right triangle (adjacent, opposite, hypotenuse); every
   minus sign of a change of basis is explained with the right-hand rule and the view (which axis points out of the
   paper); an angle measured from a vertical is related to the standard polar angle with its proof; every derivative,
   product of matrices and vector product is written out before its result.
5. **Integrity.** SI units and a dimensional check in every box. Anything beyond `Notes.pdf` and the decks is marked
   extension (Lagrangian mechanics is NOT a tool of the course). If a source looks wrong, do not adjust anything: write
   a `> [!warning] Discrepancy with Notes.pdf` (or `Erratum to ...`) callout with the check that proves it, and report
   it. The words "Phase 1", "first phase", "four phases" never appear (the physical "phase" of an oscillation is fine).

## Citations

- `Notes.pdf, Eq. X.Y`: only equations you have seen on the page with `pdftotext` (the equation number printed at the
  right of the equation). Sections as printed (`Sec. 2.4`). Figures as printed (`Notes.pdf Fig. 2.3`, plain text).
- Slides: Lecture 1 has its own numbering (some slides are missing from the PDF): cite the slide number printed on the
  slide; the map printed number → PDF page is `"slide_map"` of `em-s1` in `tools/source_links.json`. For Lectures 2 to 6
  the slide number is the PDF page index. Check the page with `pdftotext -f M -l M` before citing it.
- The links to the PDF pages are added after the build by the orchestrator (`tools/source_links.py`); do not edit
  `tools/source_anchors.json` or `tools/source_links.json`.

## Lessons of earlier audits (avoid all of them from the first draft)

1. Definite integrals without the antiderivative or without Barrow's rule, even for $\cos^2$.
2. An initial condition on the velocity used without writing the first derivative first.
3. Numbers or percentages in a **Meaning** line that were not recomputed; a Meaning sentence false to first order.
4. "Conserved about a moving axis" without both reasons (zero moment and zero extra term).
5. "Moves towards / lies on the side of" sentences not checked against the signed formulas; physical claims ("this
   variable controls ...") not derived.
6. Parameters named that do not exist in the topic; one symbol used for two quantities in one note.
7. Equations and unknowns miscounted; a relation used before it is defined.
8. "Checked symbolically / with Lagrange" written without showing it.
9. Minus signs of a change of basis without explanation; R Rᵀ = I with a single entry written.
10. Claims of stability, holonomy or finite times without an argument (a box).
11. A row of an aligned block doing two operations (product rule, substitution and grouping are three rows; an
    expansion and the use of $\cos^2+\sin^2=1$ are two rows).
12. A general solution of an ODE without its characteristic equation; a first integral whose last row is not the boxed
    expression; a citation whose page does not show the claimed content; a property of the notes quoted where your own
    result contradicts it (write the erratum instead); a modelling hypothesis presented as a theorem.

Recompute every symbolic result and every number privately (sympy or plain arithmetic) before writing it; never cite
that check in the note.

## Figure briefs

For every embed write a block in `tools/figures/em_th/briefs/tN.md` (replace the file if it exists), in the format of
`tools/figures/em_th/briefs/t6.md`:

```
## tN-<slug>
View: ... (which plane, which axis out of / into the paper, which figure of the notes or slide it redraws)
Draw: ... (every point, vector, angle, triangle and label, with colours by role: fixed axes grey, moving basis blue,
      auxiliary vectors orange, angles green, forces pink)
Values to draw: ... (numbers used for the drawing, or "none")
Alt: one sentence
Caption: one sentence (may use $...$)
```
Be exact: the figure agent draws only what the brief says.

## Checking your work

```bash
python3 tools/briefs/check_theory_note.py subjects/engineering-mechanics/teoria/topic-N.html --katex <KATEX>/katex.js
```
(`<KATEX>` is given by the orchestrator.) It builds the page as the real builder does, with placeholders for the figures
not drawn yet. The only lines allowed to remain are `figure not drawn yet: ...`; fix every `error:` and every KaTeX
failure. Then re-read each section once as a student: any step skipped, any sign unexplained, any number unverified?

## Report back (short)

The sections written (numbers and titles) and the equations and slides they follow; the figures briefed; every
discrepancy or erratum found in the sources; content of the old note or page that you
dropped and why; the final output of the check command. You do not commit, push, spawn agents or run builders in write
mode; you edit only the note and the figure brief file.
