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
    "id": "2026-10-14-updates-panel",
    "date": "2026-10-14",
    "tag": "Portal",
    "title": "New \"What's new\" panel",
    "text": "The bell in the header now lists every recent change to the portal. A dot shows when there is something you have not read yet."
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
    "link": "subjects/engineering-mechanics/teoria/topic-5.html"
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
    "text": "The colour dots in the header change the page to cream, sepia, grey, sage or charcoal, so you can pick the one that is easiest on your eyes."
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
    "text": "Each subject has an Exams page with first, second and third partials and finals, newest first. Exams from other universities are listed apart.",
    "link": "subjects/fluid-mechanics/exams/index.html"
  },
  {
    "id": "2026-10-11-ask-ai",
    "date": "2026-10-11",
    "tag": "Portal",
    "title": "Ask AI on selected text and problems",
    "text": "Select any text, or use the bar under a problem statement, to ask Claude or Gemini for help with a ready-made prompt."
  }
]
;
