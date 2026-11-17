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
- Look: stars with a small shape of their own per area (no icons), no discs behind the figures (lines and stars glow on hover and when open), names shown only when a constellation is opened, in the display font of the hero heading, a nebula backdrop and a seeded twinkling sky. Sky palettes, key `ae_sky_palette`: Deep Cosmos, Observatory Charcoal, Nebula Indigo, Stratospheric Light, Blueprint Cyan. Each has a polarity and sets the portal theme through `AETheme`; text tokens are AAA on every palette (`tools/tests/test_constellations.py`).
- Hook for a future entrance animation: `playIntro()` (returns a Promise, plays nothing today). The `ae-constellations-ready` event fires after it.

## Editing

Silhouettes and Latin titles are in `META` of the script; the two panorama layouts (landscape and portrait) in `LAND` and `PORT`. A new subject needs a `META` entry and a slot.

## Phones and tablets

Below 900 px (and on phones held on their side) the map is a taller sky that scrolls: `PORT_S` (one column, phones) and `PORT_T` (zigzag, tablets), with the title in the first screen. Opening a constellation fixes the map to the window, grows the stars (`--ks`, icon at least 20 px) and keeps every text at 13 px or more; going back restores the scroll position. The far sky is redrawn for the layout in use.

## Motion

Everything moves slowly and stops with `prefers-reduced-motion`: each figure drifts on its own loop (`.const-float`), stars twinkle and their halos breathe, a small light runs along every lit line (`.const-flow`), three shooting stars cross the far sky, the far sky follows the pointer a little (parallax) and the nebula and the title breathe. Animations are CSS only; the open constellation stops drifting so its stars stay easy to hit.

## The figures

Each subject is a real constellation: Delphinus (Fluid Mechanics), Cygnus (Aerospace Materials I), Ursa Major (Engineering Mechanics), Orion (Advanced Maths) and Leo (Business Management). Coordinates, `sc` (scale), `rot`, `use` (which anchors carry a star) and the faint `extra` companion stars are in `META` of the script. When a constellation is opened, the camera box follows the figure's own size.

## Welcome screen and sound

`assets/js/sky-intro.js` + `assets/css/sky-intro.css` show a night sky through a telescope lens with the name, "Ready to ignite?" and an Ignite button (once per browser session, key `ae_intro` in `sessionStorage`; `?intro=1` forces it, `?intro=0` skips it; the head part of `constellations.js` sets `<html data-intro="on">`). Pressing Ignite starts the sound, throws the stars into a warp, flashes and drops the visitor into the map (`.is-entering`: the map rises out of the warp and each constellation lights in turn). `assets/js/sky-sound.js` synthesises the sound with the Web Audio API (no audio files): a slow pad of open chords, pentatonic chimes, a whoosh, and a soft chime when the pointer reaches a constellation; key `ae_sky_sound`, speaker button `#soundToggle`. The map has no name in the middle: the heading stays for screen readers and the five figures fill the whole sky. On the map the blinking, the flashes and the light running along the lines are slow on purpose. With reduced motion the warp becomes a short fade.

The welcome screen does not show again in the same tab (`ae_intro`) nor when the classic view is stored; the replay button in the header (`#introReplay`) reloads the page with `?intro=1`, which also brings the stellar view back.

### Welcome screen, second pass

The lens is gold (`#E1C170`, the colour of the emblem) and carries the emblem (`#i-sideris`), "Sideris", "Aerospace" and "Engineering · 2nd Year"; it is built in stages on load (ring drawn, emblem rises, title wiped in, then the phrase and the button). The button is a round gold ring with a rippling star and the label "Ignite". Stars follow the pointer a little and a shooting star crosses now and then. Sound: a dark, mysterious drone with a whisper, a distant heartbeat and bells starts at the first click, key press or touch (or at once when the browser allows it); pressing Ignite melts it into the celestial sound. The speaker button of the welcome screen (`#introSound`) mutes both. Enter or Space ignites.

### Welcome screen, third pass

The lens is now the front of a telescope: concentric rings (barrel, knurled focus ring, inner rings) round a curved piece of glass with soft reflections, and the name sits on the glass as if it were the end of the tube. The logo (an inline copy of the emblem, `#emblemGrad`), the letters, the rings and the Ignite button share one gradient (cyan, indigo, violet). Every size is a multiple of the lens diameter (`--L`), so the logo, the name and the lines never overlap; the old side view of the telescope is gone.

## Welcome screen, fourth pass: the whole telescope

The welcome screen shows a viewpoint telescope seen end-on, after the user's reference photos, against the Milky Way and a mountain horizon. Drawn in one-point perspective (every ring is scaled by its depth): from the far end, a long rear tube receding towards the objective (dew-shield bands), a bolted collar flange where it steps down to the narrow front tube (ribbed bands, a focus knob), the near end with a tilted elliptical face and the small lens. A fork holds the trunnions on the collar and stands on a pedestal. The gradient emblem, "Sideris", "Aerospace" and the course line sit above "Ready to ignite?" in the call to action, beside the telescope (wide screens) or under it (tall screens). Igniting dollies the camera into the lens (`transform-origin` at the lens centre; `--cx/--cy` for the flash set by `sky-intro.js` from `#introDisc`) before the unchanged warp.

Igniting dives the camera into the lens: the telescope scales about 22 times around the lens centre while the warp canvas moves its vanishing point onto the lens (`lensX/lensY` from `#introDisc`), so the stars stream out of it. The sound has three moods in `sky-sound.js`: mystery on the welcome screen, a one-off stellar journey on ignite (`journey()`: sawtooth stack through a rising filter, an accelerating D major arpeggio, a bright shimmer) and the calm celestial pad with a low open fifth, which rises as the journey fades.
