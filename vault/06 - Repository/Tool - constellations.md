---
subject: "Repository"
tags:
  - repository
  - tool
  - web
source: "assets/js/constellations.js"
---

# Tool - constellations

## Purpose

Stellar view of the landing page: `assets/js/constellations.js` and `assets/css/constellations.css`, used by the root `index.html` only. Each of the five subjects is a constellation with the silhouette of its icon (Stella Fluidorum, Stella Materiae, Stella Mechanicae, Stella Matheseos, Stella Oeconomiae); its stars are the main areas of the subject (Theory, Solved Problems, Extra Problems, Formula Sheet, Exam Simulator, PDFs, Exams), read from `window.AE_NAV` ([[Tool - build_nav]]), with the counters of the classic cards. Related: [[Rules - AGENTS.md]], [[Tool - audit_portal]].

## Behaviour

- One SVG with a camera (the `viewBox`). Panorama: five constellations joined by guide lines. Click or Enter on a constellation: the camera glides to it (instant under `prefers-reduced-motion`). `Esc`, the back button or empty sky return to the panorama.
- Views, key `ae_home_view` (`constellations` default, `classic`). The classic cards stay in the DOM (class `classic-only`), so `audit_portal` still checks their badges.
- Look: stars with a shape of their own per area and a matching line icon of each page, no discs behind the figures (lines and stars glow on hover and when open), names shown only when a constellation is opened, in the display font of the hero heading, a nebula backdrop and a seeded twinkling sky. Sky palettes, key `ae_sky_palette`: Deep Cosmos, Observatory Charcoal, Nebula Indigo, Stratospheric Light, Blueprint Cyan. Each has a polarity and sets the portal theme through `AETheme`; text tokens are AAA on every palette (`tools/tests/test_constellations.py`).
- Hook for a future entrance animation: `playIntro()` (returns a Promise, plays nothing today). The `ae-constellations-ready` event fires after it.

## Editing

Silhouettes and Latin titles are in `META` of the script; the two panorama layouts (landscape and portrait) in `LAND` and `PORT`. A new subject needs a `META` entry and a slot.
