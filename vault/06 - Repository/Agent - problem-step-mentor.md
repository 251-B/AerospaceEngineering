---
subject: "Repository"
tags:
  - repository
  - agent
source: ".claude/agents/problem-step-mentor.md"
---

# Agent - problem-step-mentor

## Role

Pedagogical problem mentor and analytical rigour auditor. It enforces the problem-solving standard (the lecturer's order of each subject, with no visible "Phase" labels) on problem solutions and leads the mathematical dimension of an ultrareview.

## Tools granted

`Read`, `Grep`, `Glob`. It is read-only at the tool level. The frontmatter also sets model and effort options, which this note does not reproduce.

## Scope

The body asks it to write solutions into `vault/` and to store the core result in claude-mem. No write tool is granted, so those steps need another agent or the main session. [[Rules - AGENTS.md]] lists the role as read-only, which matches the granted tools, so the body and the tool list conflict.

## Rule it enforces

The problem-solving standard of [[Rules - AGENTS.md]]. A solution is shown in the lecturer's order (in Engineering Mechanics: frames, bases and coordinates; change of basis and position vector, with figures; kinematics; forces and equations of motion; answers and checks). Behind it runs a silent checklist that is never written into the solution:

1. Setup: hypotheses, degrees of freedom and an SI parameter table.
2. Frames: coordinate systems and the change-of-basis matrix `[{}_0 R_1]`, with `det R = 1` and `R R^T = I`.
3. Derivation: each law is justified before use; every sine, cosine and sign is explained. Chain rule, differentials and Barrow limits are explicit, with no algebraic jumps.
4. Interpretation: SI units, limiting cases and physical meaning.

## Related

[[Repository MOC]] · [[Rules - AGENTS.md]] · [[Agent - aerospace-pedagogue]] · [[Agent - web-qa-reviewer]] · [[Tool - build_problem_pages]]
