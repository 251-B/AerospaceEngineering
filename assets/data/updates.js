/*!
 * Aerospace Engineering Study Portal: "What's new" entries (hand-edited).
 *
 * Read by assets/js/updates.js (bell + panel + toast on every page, loaded by theme.js).
 * Keep everything between the brackets pure JSON (tools/tests/test_updates.py parses it).
 *
 * One entry per change that users can see. Newest first. English, plain words, no jargon.
 *   id    unique slug, "YYYY-MM-DD-short-name"
 *   date  ISO date, YYYY-MM-DD
 *   tag   Fluid Mechanics | Engineering Mechanics | Aerospace Materials I | Advanced Maths |
 *         Business Management | Portal
 *   title at most 70 characters
 *   text  at most 180 characters, one or two short sentences
 *   link  optional, path from the repository root to an existing page (never laboratory material)
 */
window.AE_UPDATES = [
  {
    "id": "2026-10-16-fluids-navier-stokes-problems",
    "date": "2026-10-16",
    "tag": "Fluid Mechanics",
    "title": "Fluid Mechanics: solved Navier-Stokes problems (Topic 4)",
    "text": "The official Navier-Stokes problems are being added with the statement word for word, its figure and a four-phase solution. The first twelve are online.",
    "link": "subjects/fluid-mechanics/problemas/topic-4-navier-stokes.html"
  },
  {
    "id": "2026-10-15-fluids-navier-stokes-theory",
    "date": "2026-10-15",
    "tag": "Fluid Mechanics",
    "title": "Fluid Mechanics: Navier-Stokes equations (Topic 4)",
    "text": "The full theory of Chapter 4 is online: differential conservation laws, boundary conditions, the equations in three coordinate systems, and a practical formulary.",
    "link": "subjects/fluid-mechanics/teoria/topic-4.html"
  },
  {
    "id": "2026-10-15-quote-card-plain-text",
    "date": "2026-10-15",
    "tag": "Portal",
    "title": "Quote card without emojis",
    "text": "The motivational quote at the bottom of the pages now shows its labels as plain text."
  },
  {
    "id": "2026-10-15-business-separate-pages",
    "date": "2026-10-15",
    "tag": "Business Management",
    "title": "Problems, Extra problems and the Exam simulator on separate pages",
    "text": "Business Management now has one page each for theory, the official problems, the extra problems and the exam simulator, linked by a row of tabs.",
    "link": "subjects/business-management/extra-problems/index.html"
  },
  {
    "id": "2026-10-15-ask-ai-links",
    "date": "2026-10-15",
    "tag": "Portal",
    "title": "Ask AI now points the assistant to the exact page",
    "text": "The prompt now carries links to this page and the subject, plus the exact problem, part or section you selected, so answers follow the portal's own notation."
  },
  {
    "id": "2026-10-15-business-exam-simulator",
    "date": "2026-10-15",
    "tag": "Business Management",
    "title": "Exam Simulator for the first partial (Midterm 1)",
    "text": "Generate a timed exam of three theory cases and one problem, write your drafts, then grade yourself out of 10. Missed items go to Review in Extra problems.",
    "link": "subjects/business-management/simulator/index.html"
  },
  {
    "id": "2026-10-15-business-problem-bank",
    "date": "2026-10-15",
    "tag": "Business Management",
    "title": "New Extra problems: 24 theory cases and 16 exam problems",
    "text": "Filter by exam part, type and unit, open a hint, the key result or the full solution only when you want it, and mark what you have mastered. Press ? for shortcuts.",
    "link": "subjects/business-management/extra-problems/index.html"
  },
  {
    "id": "2026-10-15-materials-t4-review",
    "date": "2026-10-15",
    "tag": "Aerospace Materials I",
    "title": "Topic 4 checked again against the slides and the keys",
    "text": "Phase diagram notes and problems were checked line by line. Problem 12 now uses atomic %, a Fe-C figure was fixed, and every gap with the official keys is explained.",
    "link": "subjects/aerospace-materials-1/problemas/topic-4-phase-diagrams.html"
  },
  {
    "id": "2026-10-15-end-links-buttons",
    "date": "2026-10-15",
    "tag": "Portal",
    "title": "Tidier links at the end of pages",
    "text": "The portal button no longer has an emoji, and the closing links to the problems and back to the portal are now proper buttons."
  },
  {
    "id": "2026-10-15-fluids-t3-steps",
    "date": "2026-10-15",
    "tag": "Fluid Mechanics",
    "title": "Topic 3 solutions: missing steps added",
    "text": "Skipped algebra steps are now written out, data that come only from the official solutions are marked, and one numerical example was corrected.",
    "link": "subjects/fluid-mechanics/problemas/topic-3-conservation-laws.html"
  },
  {
    "id": "2026-10-15-fluids-t3-figures",
    "date": "2026-10-15",
    "tag": "Fluid Mechanics",
    "title": "Topic 3 problems now have their figures",
    "text": "Each conservation-law problem shows its statement figure and the control volume of its solution. Some figures are cropped from the official sheets.",
    "link": "subjects/fluid-mechanics/problemas/topic-3-conservation-laws.html"
  },
  {
    "id": "2026-10-14-palette-only",
    "date": "2026-10-14",
    "tag": "Portal",
    "title": "One colour control: the reading palette picker",
    "text": "The light/dark button is gone. Pick a reading palette instead: Charcoal is the dark one, the others are light, and Default is the portal's dark theme."
  },
  {
    "id": "2026-10-14-materials-t4-complete",
    "date": "2026-10-14",
    "tag": "Aerospace Materials I",
    "title": "Topic 4 complete: ceramic and ternary diagrams",
    "text": "Session 10 is on the Topic 4 page, with ceramic and ternary phase diagrams, and the last problem of the sheets is solved: all 26 are done.",
    "link": "subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html"
  },
  {
    "id": "2026-10-14-materials-t4-fe-c-problems",
    "date": "2026-10-14",
    "tag": "Aerospace Materials I",
    "title": "Topic 4: ten Fe-C problems solved",
    "text": "The second phase-diagram sheet is solved step by step: phases and microconstituents of steels and cast irons on the Fe-C diagram.",
    "link": "subjects/aerospace-materials-1/problemas/topic-4-phase-diagrams.html"
  },
  {
    "id": "2026-10-14-materials-t4-theory-part-3",
    "date": "2026-10-14",
    "tag": "Aerospace Materials I",
    "title": "New theory: the Fe-C system",
    "text": "Session 9 is now on the Topic 4 page: the Fe-C diagram, pearlite, steels and cast irons, cooling rate and alloying elements.",
    "link": "subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html"
  },
  {
    "id": "2026-10-14-hero-solved-problem-count",
    "date": "2026-10-14",
    "tag": "Portal",
    "title": "Solved-problem count on the home page corrected",
    "text": "The home page now shows the real number of solved problems across the five subjects: 185.",
    "link": "index.html"
  },
  {
    "id": "2026-10-14-materials-t4-problems-9-15",
    "date": "2026-10-14",
    "tag": "Aerospace Materials I",
    "title": "Topic 4 problems 9 to 15 solved",
    "text": "Seven more phase-diagram problems: reactions and compounds in Al-Ni, Cu-Sn, Ni-Mo, Ti-Si and Ti-B, and two diagrams drawn from data.",
    "link": "subjects/aerospace-materials-1/problemas/topic-4-phase-diagrams.html"
  },
  {
    "id": "2026-10-14-materials-t4-theory-part-2",
    "date": "2026-10-14",
    "tag": "Aerospace Materials I",
    "title": "New theory: phase diagrams, part II",
    "text": "Session 8 is now on the Topic 4 page: precipitation in the solid state, the five invariant reactions and intermetallic compounds.",
    "link": "subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html"
  },
  {
    "id": "2026-10-14-cleaner-headers",
    "date": "2026-10-14",
    "tag": "Portal",
    "title": "Cleaner page headers",
    "text": "The Index, Problems and Topic buttons and the jump bars are gone from every page. Open the side menu to reach any topic, problem set or section."
  },
  {
    "id": "2026-10-14-side-menu",
    "date": "2026-10-14",
    "tag": "Portal",
    "title": "New side menu to move around the portal",
    "text": "The menu button at the top left opens a side menu with every subject, topic and problem set. On a page it also lists that page's sections and follows you as you scroll."
  },
  {
    "id": "2026-10-14-materials-t4-problems-1-8",
    "date": "2026-10-14",
    "tag": "Aerospace Materials I",
    "title": "Topic 4 problems 1 to 8 solved",
    "text": "The first eight phase-diagram problems are solved step by step with the lever rule, with diagrams and checks against the official answers.",
    "link": "subjects/aerospace-materials-1/problemas/topic-4-phase-diagrams.html"
  },
  {
    "id": "2026-10-14-materials-t4-theory-part-1",
    "date": "2026-10-14",
    "tag": "Aerospace Materials I",
    "title": "New theory: phase diagrams, part I",
    "text": "Topic 4 starts with Session 7: phases, the phase rule, the lever rule and eutectic alloys, with the slide figures and worked examples.",
    "link": "subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html"
  },
  {
    "id": "2026-10-14-updates-panel",
    "date": "2026-10-14",
    "tag": "Portal",
    "title": "New \"What's new\" panel",
    "text": "The bell in the header now lists every recent change to the portal. A number on the bell shows how many changes you have not read yet."
  },
  {
    "id": "2026-10-14-fluids-t3-problems",
    "date": "2026-10-14",
    "tag": "Fluid Mechanics",
    "title": "Topic 3 problems solved: CL1 to CL22",
    "text": "All 22 conservation-law problems are now solved step by step in the class method, surface by surface.",
    "link": "subjects/fluid-mechanics/problemas/topic-3-conservation-laws.html"
  },
  {
    "id": "2026-10-14-study-timer",
    "date": "2026-10-14",
    "tag": "Portal",
    "title": "Study timer on every page",
    "text": "A Timer button (above Focus) runs Pomodoro blocks, or plans a whole study session from the time you have available."
  },
  {
    "id": "2026-10-13-focus-lab",
    "date": "2026-10-13",
    "tag": "Portal",
    "title": "Focus Lab: study sound",
    "text": "A Focus button on every page plays binaural beats or brown and pink noise to help you concentrate. Nothing is downloaded."
  },
  {
    "id": "2026-10-13-mechanics-t5",
    "date": "2026-10-13",
    "tag": "Engineering Mechanics",
    "title": "Topic 5: Relative Motion, theory and all 18 problems",
    "text": "The Relative Motion theory page is up, together with its 18 solved problems.",
    "link": "subjects/engineering-mechanics/problemas/topic-5.html"
  },
  {
    "id": "2026-10-13-business-t3-key",
    "date": "2026-10-13",
    "tag": "Business Management",
    "title": "Topic 3 solutions checked against the official key",
    "text": "Each Topic 3 problem now ends with a comparison against the official solutions.",
    "link": "subjects/business-management/problemas/topic-3-financial-statements.html"
  },
  {
    "id": "2026-10-12-reading-palettes",
    "date": "2026-10-12",
    "tag": "Portal",
    "title": "Reading backgrounds",
    "text": "The colour dots in the header change the page to cream, sepia, slate grey, sage or charcoal, so you can pick the one that is easiest on your eyes."
  },
  {
    "id": "2026-10-12-pdf-download",
    "date": "2026-10-12",
    "tag": "Portal",
    "title": "Download any page or problem as PDF",
    "text": "Every theory and problem page has a Download PDF button, and each problem card has its own, in black and white A4."
  },
  {
    "id": "2026-10-12-exams-pages",
    "date": "2026-10-12",
    "tag": "Portal",
    "title": "Past exams sorted by partial and year",
    "text": "Fluids, Mechanics, Materials and Maths now have an Exams page, sorted by partial and final, newest first. Exams from other universities are listed apart.",
    "link": "subjects/fluid-mechanics/exams/index.html"
  },
  {
    "id": "2026-10-12-business-theory",
    "date": "2026-10-12",
    "tag": "Business Management",
    "title": "Business theory rewritten in plain words",
    "text": "Topics 1 to 3 now explain the official slides in plain words, with the diagrams redrawn.",
    "link": "subjects/business-management/teoria/topic-1.html"
  },
  {
    "id": "2026-10-11-ask-ai",
    "date": "2026-10-11",
    "tag": "Portal",
    "title": "Ask AI on selected text and problems",
    "text": "On theory and problem pages, select any text, or use the bar under a problem statement, to ask Claude or Gemini for help with a ready-made prompt."
  },
  {
    "id": "2026-10-11-materials-topics",
    "date": "2026-10-11",
    "tag": "Aerospace Materials I",
    "title": "Materials Topics 1 to 3 rewritten from the slides",
    "text": "Bonding, structure and diffusion now follow the official slides, with worked examples of crystal directions and planes.",
    "link": "subjects/aerospace-materials-1/teoria/topic-1-bonding.html"
  },
  {
    "id": "2026-10-10-pdf-deep-links",
    "date": "2026-10-10",
    "tag": "Portal",
    "title": "Citations open the official PDF at the right page",
    "text": "Each problem has an \"Original statement\" link, and citations such as [Slide 14] open the course PDF at that exact page."
  }
]
;
