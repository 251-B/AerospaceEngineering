---
name: Sideris
description: A night observatory for studying 2nd-year Aerospace Engineering at UC3M.
colors:
  night-sky: "#070b14"
  night-sky-deep: "#0d1321"
  starlight: "#f8fafc"
  nebula-grey: "#94a3b8"
  dust-grey: "#64748b"
  daylight-paper: "#f8fafc"
  daylight-ink: "#0f172a"
  study-night: "#0a0e17"
  study-night-surface: "#131b2b"
  study-day: "#f6f8fa"
  study-day-surface: "#ffffff"
  fluid-cyan: "#06b6d4"
  materials-amber: "#f59e0b"
  mechanics-green: "#10b981"
  maths-indigo: "#6366f1"
  business-red: "#ef4444"
  fluid-neon: "#00f0ff"
  materials-neon: "#ffb703"
  mechanics-neon: "#00f59b"
  maths-neon: "#a78bfa"
  business-neon: "#ff0055"
  star-fluid: "#62d6ee"
  star-materials: "#efbf5a"
  star-mechanics: "#5fdcae"
  star-maths: "#b6a2f2"
  star-business: "#ee7aa6"
typography:
  display:
    fontFamily: "'Abril Fatface', cursive, Georgia, serif"
    fontSize: "clamp(2rem, 4.2vw, 3.2rem)"
    fontWeight: 400
    lineHeight: 1.2
  body:
    fontFamily: "'Newsreader', Georgia, 'Times New Roman', serif"
    fontSize: "1.02rem"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "'JetBrains Mono', 'Cascadia Code', monospace"
    fontSize: "0.76rem"
    fontWeight: 500
    letterSpacing: "0.05em"
rounded:
  sm: "8px"
  md: "14px"
  lg: "20px"
  xl: "26px"
spacing:
  max-width: "1280px"
components:
  card-dark:
    backgroundColor: "{colors.study-night-surface}"
    textColor: "{colors.starlight}"
    rounded: "{rounded.lg}"
  card-light:
    backgroundColor: "{colors.study-day-surface}"
    textColor: "{colors.daylight-ink}"
    rounded: "{rounded.lg}"
  badge:
    textColor: "{colors.nebula-grey}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
---

# Design System: Sideris

## Overview

**Creative North Star: "Night Observatory"**

Sideris is an observatory used at night. The visit starts at the telescope (an optional intro: "Ready to ignite?", with Skip intro), then the dome opens onto the sky: each subject is a constellation in its own colour, drawn over a nebula background in one of five sky palettes, with a "Classic view" of subject cards for whoever just wants to go fast. Once a student enters a subject, the dome closes and the room becomes a quiet reading desk: flat, opaque, matte surfaces with no stars, no blur and no movement under the text, so long derivations can be read for an hour without fatigue.

Two densities live side by side. The hub is atmospheric and spacious; the study pages are dense, calm and functional, where the content (equations, figures, step-by-step solutions) carries the page. Colour identifies the subject, never decorates the reading. Every text meets AAA contrast on all six reading palettes, because the portal is used mostly in the morning and late at night on phone, tablet and laptop.

**Key Characteristics:**
- Animated sky on the home page only; flat matte surfaces everywhere else.
- One accent colour per subject, with a brighter neon twin on dark surfaces.
- Serif reading voice (Newsreader), poster display (Abril Fatface), mono for numbers and labels.
- Six reading palettes (Default, Cream, Sepia, Slate paper, Sage, Charcoal), each bound to one polarity.
- No emojis; icons are inline SVG.

## Colors

A night-sky neutral base with five subject accents that act as wayfinding lights.

### Primary
- **Night Sky** (`night-sky`): the background of the home page and of the dark theme; deepened to Night Sky Deep for secondary bands.
- **Study Night / Study Night Surface** (`study-night`, `study-night-surface`): the flat page and card colours of dark study pages.
- **Study Day / Study Day Surface** (`study-day`, `study-day-surface`): the same roles in light mode.

### Secondary (subject accents)
- **Fluid Cyan**, **Materials Amber**, **Mechanics Green**, **Maths Indigo**, **Business Red**: mark the subject on its card, headings, borders and links. On dark surfaces each switches to its neon twin (`*-neon`).

### Neutral
- **Starlight** (`starlight`): primary text on dark. **Daylight Ink** (`daylight-ink`): primary text on light.
- **Nebula Grey** and **Dust Grey**: secondary and muted text, badges and "Soon" labels.
- Borders and glass layers are white or black at 4-10% opacity (`--border-subtle`, `--border-card`, `--bg-glass`).

### Constellation stars
On the constellation home each subject is drawn in a softened star colour (`star-*`), with a lighter tint for its label; in light mode they switch to deeper shades (`assets/css/constellations.css`).

### Sky palettes (home)
`html[data-sky-palette]` sets the home background: Deep Cosmos (default, cyan/violet/pink nebula over blue-black), Observatory Charcoal, Nebula Indigo, Stratospheric Light (the only light one) and Blueprint Cyan (with a grid). Each re-points the `--sk-*` variables (background, text, line, panel, border).

### Reading palettes
The study pages re-point the `--study-*` variables in `assets/css/study-surface.css`: Cream (#f5f2eb), Sepia (#efe8d8), Slate paper (#eceff2) and Sage (#ebf0ea) are light; Charcoal (#111620) is dark. They only restyle; content never changes for a palette.

### Named Rules
**The Instrument Light Rule.** A subject accent marks where you are (card, heading, border, active link); it never fills large reading areas and never colours body text.
**The AAA Rule.** Every text reaches 7:1 (large text 4.5:1) on every reading palette; `tools/tests/test_surface.py` enforces it.

## Typography

**Display Font:** Abril Fatface (with Georgia, serif)
**Body Font:** Newsreader (with Georgia, Times New Roman)
**Label/Mono Font:** JetBrains Mono (with Cascadia Code, monospace)

**Character:** A high-contrast poster face for the big titles over a warm, bookish serif for reading; the mono face is the instrument readout for numbers, timers and labels.

### Hierarchy
- **Display** (400, clamp(2rem, 4.2vw, 3.2rem), 1.2): portal and page titles.
- **Headline / Title** (Newsreader or Abril Fatface, 1.15-1.35rem): section and card headings.
- **Body** (400, about 1.02rem, 1.65): theory and solutions; maths in KaTeX.
- **Label** (JetBrains Mono, 0.74-0.76rem, letter-spacing 0.05em): badges, counters, timers, metadata.

### Named Rules
**The Three Voices Rule.** Exactly three families: Abril Fatface for display, Newsreader for reading, JetBrains Mono for figures. No fourth font.

## Layout

Centered content up to 1280px. The hub uses a grid of subject cards that collapses to one column on phones; study pages are a single reading column with problem cards stacked vertically. Breakpoints at 768px, 640px (`assets/css/responsive.css`, the phone safety net) and 480px. Wide tables scroll inside `.table-wrapper` / `.table-container`. Navigation lives in the left drawer (side menu, `min(85vw, 320px)`); the header carries only the menu button, the home link and the tools (updates bell, palette picker).

## Elevation & Depth

Hybrid. On the hub, cards float over the sky with soft ambient shadows and translucent fills. On study pages surfaces are opaque and nearly flat: depth comes from one tonal step between page, card and inset (statement boxes, tables).

### Shadow Vocabulary
- **Card at rest** (`--shadow-card`: 0 4px 24px, black 45% dark / 6% light).
- **Card on hover** (`--shadow-card-hover`: 0 16px 44px, black 60% dark / 10% light): navigation cards only; long reading cards stay still under the cursor.

### Named Rules
**The Closed Dome Rule.** The sky, constellations, gradients and blur belong to the home page; study pages are flat and opaque.

## Shapes

Generously rounded, never sharp: 8px for badges and small controls, 14px for buttons and inputs, 20px for cards, 26px for large hero panels. Borders are hairlines at low opacity.

## Components

### Telescope intro
- Line-art telescope over a perspective grid, the Sideris emblem and title, "Ready to ignite?" and an Ignite button; Skip intro below. Shown on demand (`?intro=1`).

### Constellation home
- Five constellations (Stella Fluidorum, Materiae, Mechanicae, Matheseos, Oeconomiae), one per subject, joined by faint guide lines; choosing one opens its subject. Keyboard: Tab and Enter. Header controls: menu, view switch, sound, sky palette select, Classic view, updates bell, theme switch, Sign in.

### Subject cards (hub, Classic view)
- **Character:** an instrument panel per subject.
- **Shape:** 20px radius, translucent card fill, hairline border, subject accent on the icon and edge.
- **States:** lift with the hover shadow; unbuilt areas shown as `aria-disabled` with a "Soon" badge.

### Problem and theory cards (study pages)
- **Shape:** 20px radius, opaque `--study-surface`, statement box one tonal step apart.
- **Behaviour:** collapsible solutions (`details`), a "Close solution" bar at the end, Ask AI bar and PDF buttons.

### Badges
- JetBrains Mono, small caps-like spacing, muted text on a faint fill; counts must match the pages on disk.

### Navigation
- Left drawer over the page, closed by default, current subject/area/page marked with `aria-current="page"` and scroll-spy inside the page. Subject tab strip inside `<main>` on the hand-written index pages.

### Floating tools
- "Focus" and "Timer" buttons bottom right, "What's new" bell in the header; only one panel open at a time; hidden in print.

## Do's and Don'ts

### Do:
- **Do** keep the existing logo, the three fonts and the space aesthetic.
- **Do** use the tokens in `assets/css/tokens.css` and the `--study-*` variables; never hard-code a page colour.
- **Do** check every new text colour against all six palettes (AAA).
- **Do** keep transitions short (0.2s / 0.35s, cubic-bezier(0.4, 0, 0.2, 1)).
- **Do** keep every study page printable as an A4 black-and-white PDF.

### Don't:
- **Don't** use emojis anywhere.
- **Don't** put the animated sky, canvas or blur on study pages.
- **Don't** colour body text with a subject accent.
- **Don't** add header navigation buttons or jump-pill bars; the side menu does that job.
- **Don't** add theme code to a page; `assets/js/theme.js` owns it.
