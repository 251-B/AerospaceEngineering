---
materia: "Advanced Maths"
tema: "Exam pattern analysis: structure, themes and archetypes of the official papers"
tags:
  - exam-analysis
  - problem-bank
  - advanced-maths
---

# Exam Analysis - Official Papers 2011-2025

> Phase 1 of the Advanced Maths problem bank. Source: the 67 files of `sources/cuatrimestre-1/04-advanced-maths/examenes/` (`MATHS_FIRSTPARTIAL_*`, `MATHS_SECONDPARTIAL_*`, `MATHS_FINALEXAM_*`, one other-university paper). The text layer of 52 papers could be read with PyMuPDF; the rest are photographs or scans (`.jpg`, `.jpeg`, `.docx`, empty-text PDFs), duplicates (`HIGHLIGHTED`) or the other-university paper, and were not counted. Hub: [[Advanced Maths MOC]]. Bank index: [[Problem Set - Advanced Maths Problem Bank]].

## 1. Structure of the three cohorts

| Cohort | Papers read | Duration printed | Marks | Typical shape |
| :--- | :--- | :--- | :--- | :--- |
| First partial (MT1/MT2) | 19 | 1 h (2019, 2020 G46/G47), 1.5 h (2021 G45); 2024 and 2025 print none | 10: 4+6, 5+5, 3+4, 2+5+3 | 2 or 3 problems; one is always a linear system with its phase portrait |
| Second partial (MT3) | 12 | 1 h (2019), 1.5 h (2021), 2 h (2020) | 10: 4+6, 5+5 | A nonlinear system or a Fourier series, plus a PDE by separation of variables |
| Final exam | 21 | 3 h (2022), 3.5 h (2020, 2021), 4 h (2019) | 10: 2.5 x 4, or 2+3+3+2 | Four problems, one per block: ODE, system, Fourier/Sturm-Liouville, PDE |

The 2011-2016 papers print neither marks nor duration in the text layer; the bank does not guess them.

## 2. Frequency matrix of themes

Counts are the number of papers (text layer) whose text matches the theme; keyword based, so they bound the true frequency from below for scanned or terse papers.

| Theme | Final (21) | First partial (19) | Second partial (12) |
| :--- | :---: | :---: | :---: |
| First-order modelling (cooling, mixing, population, decay) | 7 | 9 | 4 |
| Exact equations and integrating factors | 6 | 5 | 1 |
| Separable, Bernoulli, change of variable | 3 | 6 | 0 |
| Phase line and stationary solutions | 0 | 2 | 2 |
| Reduction of order with a known solution | 2 | 4 | 0 |
| Euler / Cauchy-Euler equations | 5 | 5 | 1 |
| Undetermined coefficients, variation of parameters | 7 | 6 | 0 |
| Resonance, damping, forced oscillators | 4 | 0 | 0 |
| Power series solutions | 0 | 2 | 0 |
| Linear systems: eigenvalues and eigenvectors | 13 | 16 | 8 |
| Phase portraits | 12 | 11 | 7 |
| System with a real parameter $a$ or $\alpha$ | 9 | 5 | 0 |
| Inhomogeneous systems | 4 | 4 | 0 |
| Nonlinear systems: Jacobian, species, SIR | 9 | 6 | 7 |
| Energy, first integrals, conservative systems | 2 | 0 | 1 |
| Fourier series | 9 | 2 | 7 |
| Dirichlet convergence and numerical sums | 1 | 0 | 3 |
| Heat equation | 11 | 0 | 3 |
| Wave equation | 12 | 0 | 0 |
| Laplace equation (disc, annulus, half disc, ring) | 9 | 0 | 4 |
| Sturm-Liouville | 7 | 1 | 1 |
| Numerical methods (Euler, truncation error) | 8 | 4 | 0 |

Reading: the first partial is linear ODEs and linear systems (16 of 19 papers); the second partial moves to nonlinear systems, Fourier series and Laplace/heat (never wave); the finals add the wave equation, Sturm-Liouville and the integrated problems. Numerical methods appear in the 2011-2016 papers only and are outside the bank.

## 3. How the questions are posed

- **Action verbs:** "Find the solution of the IVP", "Sketch the phase portrait", "Classify the origin / the fixed points", "Show that", "Verify that $y_1$ and $y_2$ are solutions", "Discuss the evolution for $t\to\infty$", "Describe the interaction between the species for $\alpha<0$, $=0$, $>0$", "Justify why", "Explain in your own words" (2024 papers), "Calculate a power series solution" (2025).
- **Theory demanded inside problems:** the definition of an exact equation and what to do if it is not (2024), the meaning of the constants of the logistic law (2024), why eigenvalues matter (2024), uniqueness of the Laplace problem by the divergence theorem (2022), why the zero mode plays no role in a ring (2019), the energy of a heat solution (2024).
- **Forms of the same block:** direct problem (given $A$, find the portrait) versus inverse (given eigen-data, build $A$: sheet Ch4-II P5); parametric systems $A(a)$ whose type changes with $a$ (2025 G47: $\begin{pmatrix}a&1\\1&a\end{pmatrix}$); modelling narratives (cooling with a linearly growing ambient temperature, 2019) versus bare equations; piecewise data for Fourier problems (2019: $5x/2$ then $3-2x$); non-homogeneous boundary data reduced by a shift or a steady state (2020, 2024).
- **Marking:** parts carry explicit marks (3, 7, 5, 6, 15 in 2024); the answer must cite the theory of the course; the final answer is to be boxed.

## 4. Archetypes of the bank

| Archetype | Cohort | Bank items |
| :--- | :--- | :--- |
| `ode-first-order-modeling` | MT1 | P01 |
| `ode-first-order-qualitative` | MT1 | P02 |
| `ode-second-order-reduction` | MT1, Final | P03, P15 |
| `ode-second-order-undetermined-params` | MT1, Final | P04, P16 |
| `linear-systems-phase-portrait` | MT1, Final | P05, P06, P07, P18 |
| `nonlinear-systems-stability` | MT2, Final | P08, P09, P17 |
| `fourier-series-convergence` | MT2, Final | P10, P11, P20 |
| `pde-separation-laplace` | MT2, Final | P13, P21 |
| `pde-separation-heat-wave` | MT2, Final | P12, P14, P22 |
| `sturm-liouville-eigenproblems` | Final | P19 |

Each archetype is realised with different data layouts (direct and inverse statements, parametric cases, narratives, piecewise data), not with renumbered official exercises. Blueprints: `subjects/advanced-maths/data/exam-blueprint*.json`; builder: `tools/build_maths_bank.py`.

## 5. Limits of this analysis

- Papers that are images (2018 MT1/MT2 photographs, 2024 solutions) and `.docx` files were not read.
- The 2011-2016 papers have no readable marks; their structure is inferred from the problem count only.
- Keyword counts can double-count a paper that mentions several themes; they are frequencies of presence, not of weight.
