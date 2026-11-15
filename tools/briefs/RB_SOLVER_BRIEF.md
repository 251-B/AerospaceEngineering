# Brief: solving a batch of rigid body problems (Engineering Mechanics, structure 4)

Working brief for the agent that writes the worked solutions of the rigid body problems `rb-NN`. It is deleted when the
mission closes. The orchestrator names the problems of the batch; everything else is here.

## What you write

For each problem of your batch, one section appended to the solution note of its topic (never reorder or edit the
sections of other problems):

| Topic | Solution note in `vault/03 - Engineering Mechanics/` |
| :--- | :--- |
| 6 | `Solution Set - Topic 6 Rigid Body Kinematics and Inertia.md` |
| 7 | `Solution Set - Topic 7 Rigid Body Momentum, Energy and Dynamics.md` |
| 8 | `Solution Set - Topic 8 Constraints, Rolling, Multibody and Torque-Free Motion.md` |

If the note of topic 7 or 8 does not exist, create it with the same frontmatter and intro shape as the topic 6 note
(change title, tags and wikilinks to that topic's Problem Set and theory note).

For each figure you embed, one brief appended to `tools/figures/em_sol/briefs/rbNN.md` (see "Figures").

You do not write Python, do not run the page builder in write mode, do not commit, do not push, do not spawn agents.

## Read first

1. The statement, word for word, in `Problem Set - Topic N ...md` (same folder), with its figure
   (`vault/attachments/EM/T?-RBNN-figure*.png`: open it with the Read tool and look at it).
2. The official answer, if any, in `Problem Set - Rigid Body Official Key.md` (section `## RB-NN`).
3. The model solution: section `## Problem RB-34` of the topic 6 solution note. Copy its form exactly.
4. The theory note of the topic (`Topic 6 - ...`, `Topic 7 - ...`, `Topic 8 - ...`): it holds the equation numbers of
   `Notes.pdf` and the lecture slides you may cite, and the notation. Cite only equations and slides that exist there
   or that you verified in `sources/cuatrimestre-1/03-engineering-mechanics/teoria/Notes.pdf` with `pdftotext`
   (PDF page = printed page + 1).

## Form of a solution (checked by `tools/build_mech_problems.py`)

```
## Problem RB-NN: <title exactly as in the Problem Set note>

### Reference Frames, Bases and Degrees of Freedom
### Change of Basis, Position Vectors and Constraint Kinematics
### Center of Mass and Inertia Tensor
### Linear Momentum, Angular Momentum and Kinetic Energy
### Free-Body Diagram and Equations of Motion
### Answers and Checks
```

All six headings, in this order, spelled exactly. A section that the problem does not need is one sentence saying why
it does not apply. `### Answers and Checks` holds a table with the explicit answer to every part of the statement and
then either the bold line `**Check against the official key:**` (when the key prints an answer) or
`**Limiting cases and consistency:**` (when it does not); with a key, limiting cases are still welcome.
Sub-headings inside a section are `####`. Separate problems with a line `---`. The word "Phase" never appears.

### Derivation boxes: every calculation lives in one

```
> [!derivation] Title of the step
> **Law:** the principle invoked
> **Source:** Notes.pdf, Eq. 9.3; [Lecture 7, Slide 6]
>
> Optional sentences (may contain maths).
>
> $$\begin{aligned}
> a &= b \quad &\text{(one operation, with its reason)} \\
> &= c \quad &\text{(the next operation)}
> \end{aligned}$$
>
> $$\boxed{a = c}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$, the check written out
> **Meaning:** the physical reading of the result
```

Rules enforced by the gate:
- Title, `**Law:**`, `**Source:**` (at least one citation of the forms `Notes.pdf, Eq. X.Y`, `Notes.pdf, Sec. X.Y`,
  `[Lecture N, Slide M]`, `Problems.pdf, p. N`; written outside `$...$`), `**Units:**`, `**Meaning:**`.
- At least one `$$` block with `\boxed{...}`.
- Every row of every `aligned` block ends with its reason `\quad &\text{(...)}`. One operation per row.
- Inside matrices and determinants use `\cr` for the row break (not `\\`), as the model does.
- Outside the boxes, a paragraph, bullet or table cell of prose may contain only atomic identifiers in maths
  (`$m$`, `$\theta$`, `$\mathbf r_0^G$`, `$\{\mathbf i_1, \mathbf j_1, \mathbf k_1\}$`): no `=`, `\dot`, `\ddot`, `\times`,
  `\frac`, `\int` in inline maths outside a box, and no `$$` block outside a box. Table cells are not gated, so data,
  definitions and the answer table may hold formulas. Numbers with units in plain text are fine ("3 rad/s").
- A figure embed may stand inside a box or between boxes, on its own line.
- KaTeX only: no `\euro`, no `\label`, no `align` environments other than `aligned`; `\lt` and `\gt` for inequalities
  in inline maths.

### First principles, no shortcuts

- Start from the position vector, the change-of-basis matrices (each one checked: determinant 1 and
  $R R^T = I$ written out once per rotation), the derivative of the unit vectors
  ($\dot{\mathbf u}_i = \boldsymbol\omega\times\mathbf u_i$), then velocity, acceleration, then
  $\sum\mathbf F = m\,\mathbf a_0^G$ and $\mathbf M_Q = \dot{\mathbf H}_{Q,0} + \mathbf v_0^Q\times\mathbf p_0$
  (or its form at $G$ or at a fixed point, saying why that pole is allowed).
- Never quote a memorised result: no polar acceleration formulas, no $m\omega^2 r$ without expanding
  $\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r)$, no moment of inertia without its integral (mass element,
  jacobian, limits, antiderivative, Barrow's rule with both limits substituted) and Steiner written term by term.
  Never refer to another problem for a result; a result of the theory note may be cited by its equation number only
  when it is a law (the velocity field, Koenig, Euler's equations), not a formula for a particular shape.
- Every sine and cosine names its right triangle (hypotenuse, adjacent leg, opposite leg). Every minus sign of a change
  of basis is explained with the right-hand rule and the view used (axis out of the paper ⊙ or into it ⊗). Every chain
  rule, product rule, vector product (determinant, expanded along the first row) and matrix product is written before
  its result.
- Only the tools of the problem's own unit or earlier units (topic 6 problems use no dynamics; topic 7 problems may use
  everything up to chapter 12; topic 8 everything).
- SI units throughout; a dimensional check in every box.

### Integrity

- Never bend a step to reach the official answer. Solve first, compare afterwards. If your result differs, keep it and
  add, in `### Answers and Checks`:
  ```
  > [!warning] Discrepancy with the official solution
  > what the key prints, what this solution obtains, and the check that supports it
  ```
  If the two are the same thing written differently (other sign convention, other basis, other choice of angle), show
  the conversion in a box.
- Mark anything beyond `Notes.pdf` and the lectures as **extension**.
- A reading of an unclear figure is stated as such ("read from the figure: ...").
- Notation of `Notes.pdf`: $S_0\{O; \mathcal B_0\}$, $\boldsymbol\omega_{B0}$, $[{}_0R_1]$ (columns: the rotated unit
  vectors in the fixed basis), $\mathbf r_0^P$, $\mathbf v_0^P$, $\mathbf H_{G}$, $\bar{\bar I}_G$.

## Figures

Each problem needs its own deduction figures (not the statement figure): one 2D view per rotation (axis ⊙/⊗, fixed
axes grey, rotated axes coloured, the angle marked between both pairs of axes), the main plane or meridian section with
the shaded right triangles used for each sine and cosine, and, when there are forces, the free-body diagram with applied
forces, reactions and (if used) inertia forces; multibody problems get an exploded view with the action-reaction pairs.

Embed each one where it is used: `![[attachments/EM-SOL/rbNN-<slug>.svg]]` (lowercase slug, hyphens). You do not draw
it. For each embed append to `tools/figures/em_sol/briefs/rbNN.md`:

```
## rbNN-<slug>
View: which plane, which axis points out of / into the paper, where the origin is.
Draw: every point, axis, vector, angle arc (with its sense), triangle (legs and hypotenuse labels), dimension.
Values to draw: the angles and lengths to use for the drawing (e.g. theta = 35 deg).
Alt: one sentence.
Caption: one or two sentences (may use $...$).
```

Be exact: the figure agent draws only what the brief says.

## Checking your work

Run from the repository root (read-only check; it writes nothing):

```bash
python3 tools/build_mech_problems.py --check 2>&1 | grep -E "rb-(NN|MM)" 
```

for your problem numbers. The only messages allowed to remain for your problems are `unknown figure rbNN-...` (the
figures are drawn after you). Fix every other message. Then re-read each solution once as a student: is any step
skipped, any sign unexplained, any number unverified? Recompute every numeric result independently
(`python3 -c ...` with sympy or plain arithmetic is fine) before you finish.

## Report back (short)

Per problem: result versus the official key (match / match after conversion / discrepancy / no key), the figures
briefed, anything in the statement or key you had to interpret, and the final output of the check command.
