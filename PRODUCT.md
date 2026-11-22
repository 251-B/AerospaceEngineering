# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

The author and their classmates in the 2nd year of the BSc in Aerospace Engineering at UC3M. They use the portal often, on phone, tablet and laptop, mostly in the morning and at night (so low-light reading matters).

## Product Purpose

Sideris is a study portal for the five first-semester subjects (Fluid Mechanics, Aerospace Materials I, Engineering Mechanics, Advanced Maths, Business Management): theory explained in full detail and every problem of each topic solved step by step. Success means a student can learn a topic and prepare an exam from the portal alone, trusting that it matches the course.

## Positioning

- Problems solved step by step in each lecturer's own order and notation, with no algebraic skips.
- Everything comes from the official course PDFs, with deep links to the exact page of the source.
- Study tools built in: Ask AI prompts, study timer (Pomodoro), Focus sound, exam simulator and downloadable A4 PDFs.

## Operating Context

Pages are generated from the Obsidian vault (`vault/`), which follows the official material in `sources/`. Static site served from GitHub Pages; locally `python -m http.server 8765`. Navigation is the side menu; the header carries only the link back to the portal home.

## Capabilities and Constraints

- No emojis anywhere.
- All study content in academic English, SI units.
- No laboratory material on the web.
- Every text AAA contrast (7:1) on all six reading palettes.
- Maths rendered with KaTeX; every study page prints well as an A4 black-and-white PDF.
- Generated pages are never edited by hand; change the vault note or the generator.
- One header link (back to `index.html`); everything else through the side menu.

## Brand Commitments

Binding, confirmed by the user:
- Keep the name and logo: **Sideris** (the S-orbit emblem) and the brand title in the header.
- Keep the fonts: Newsreader (body), Abril Fatface (display headings), JetBrains Mono (figures, code).
- Keep the space aesthetic: the telescope intro, the constellation home (one constellation per subject) and the night-sky palettes.

## Evidence on Hand

Real content only: theory pages, solved problems and official PDFs under `subjects/`, `vault/` and `sources/`. No testimonials, usage numbers or external claims exist; do not invent them.

## Product Principles

1. Faithful to the official sources before anything else.
2. Reading and working through derivations comes first; tools must not get in the way.
3. Comfortable on every device and in low light.
4. One consistent portal across the five subjects.
