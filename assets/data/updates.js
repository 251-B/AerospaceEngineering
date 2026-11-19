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
    "id": "2026-11-19-sideris-downloads-across-pages",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Sideris keeps installing while you move between pages",
    "text": "Model downloads now carry on from where they stopped when you change page, and a model already installed keeps answering while another downloads. No settings to touch."
  },
  {
    "id": "2026-11-19-guided-tour",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "A short guided tour of everything the portal does",
    "text": "New accounts are offered a two-minute tour of the portal. You can skip it and take it any time from your account menu.",
    "link": "account/dashboard.html"
  },
  {
    "id": "2026-11-19-calendar-revision-plans",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Revision plans, attendance and calendar export",
    "text": "Plan your revision before each exam, see your attendance per subject, export your term to Google Calendar, and ask Sideris to explain a class you missed.",
    "link": "account/calendar.html"
  },
  {
    "id": "2026-11-19-account-calendar",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "A calendar of your classes and exams",
    "text": "Choose your group and see each class with what will be done in it and the pages to prepare it. Mark the classes you missed and catch up from one list.",
    "link": "account/calendar.html"
  },
  {
    "id": "2026-11-19-business-figures-from-slides",
    "date": "2026-11-19",
    "tag": "Business Management",
    "title": "Business figures now come straight from the slides",
    "text": "The diagrams of Topics 1 to 7 are now crops of the official slides instead of redrawn versions. Two that had drifted from the slides were corrected.",
    "link": "subjects/business-management/teoria/topic-1.html"
  },
  {
    "id": "2026-11-19-sideris-on-your-computer",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Sideris installs itself on computers that can run it",
    "text": "On a capable computer Sideris quietly downloads its models and then answers there, with no daily limit. Phones and tablets keep using the cloud."
  },
  {
    "id": "2026-11-19-sideris-daily-allowance",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "A fair daily allowance of Sideris questions for everyone",
    "text": "Each student now has a daily allowance of Sideris questions, so nobody can use up the service for the rest. Lux uses the least of it, Orion and Titan the most."
  },
  {
    "id": "2026-11-19-sideris-deep-models-on-request",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Orion and Titan only when you choose them",
    "text": "Sideris answers with Lux or Aether by default. Orion and Titan think step by step first, so they are used only for the conversation where you pick them."
  },
  {
    "id": "2026-11-19-sideris-own-cloud",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Sideris runs only on its own cloud",
    "text": "Sideris no longer asks for personal API keys. Orion and Titan can now write longer step-by-step answers."
  },
  {
    "id": "2026-11-19-sideris-steadier",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Sideris keeps your place and answers in your language",
    "text": "Opening Sideris no longer moves the page you are reading. It answers in the language you write in, and long answers no longer come back empty or vanish if the connection drops."
  },
  {
    "id": "2026-11-19-sideris-hints-and-spanish",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Sideris: hints only, Ask Sideris on selected text, Spanish questions",
    "text": "On problem pages Sideris can guide you without revealing the solution. Select text to ask Sideris about it. Spanish questions now find the English course notes."
  },
  {
    "id": "2026-11-19-sideris-reads-the-page",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Sideris now sees the section or problem you are reading",
    "text": "Sideris answers about your selected text, the open problem or the section on screen, picks closer course notes, and no longer freezes on long answers."
  },
  {
    "id": "2026-11-19-problem-steps-everywhere",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Every worked problem, step by step",
    "text": "All problem pages now show solutions one step at a time, or only the answer, with a bar per problem on the right and the arrow keys to move between problems."
  },
  {
    "id": "2026-11-19-problem-steps-pilot",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Worked problems step by step (trial on two pages)",
    "text": "Solutions now show one step at a time, or only the answer, with a bar per problem on the right. Trying it on Hydrostatics and Rigid Body Kinematics first.",
    "link": "subjects/fluid-mechanics/problemas/topic-5-hydrostatics.html"
  },
  {
    "id": "2026-11-19-home-sky-on-phones",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Subject names on the sky, and all five subjects on one phone screen",
    "text": "On phones and tablets each constellation now shows its subject name. On a phone the five fit one screen and the top bar fits in one row.",
    "link": "index.html"
  },
  {
    "id": "2026-11-19-index-solar-systems",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Subject indexes as solar systems, Sideris models as planets",
    "text": "On a computer, the topics of each subject index now orbit a star as numbered planets. In Sideris, the size of each planet shows how deep its model goes.",
    "link": "subjects/engineering-mechanics/teoria/index.html"
  },
  {
    "id": "2026-11-19-sideris-studio-workspace",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Sideris AI Studio: split workspace, left history and crisp KaTeX",
    "text": "Sideris now opens as a full-height AI studio with history on the left, your study page docked live beside it, modern sans-serif typography, and reliable KaTeX equations.",
    "link": "index.html"
  },
  {
    "id": "2026-11-19-sideris-ai-chat",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Sideris AI tutor: Lux, Aether, Orion and Titan (zero download)",
    "text": "Chat right inside every study page with Sideris Lux, Aether, Orion and Titan using Ask AI and your course notes, ready instantly with zero download or offline in the browser.",
    "link": "index.html"
  },
  {
    "id": "2026-11-19-theory-slides-key-ideas",
    "date": "2026-11-19",
    "tag": "Portal",
    "title": "Clearer figures in Charcoal, slide panels and key ideas",
    "text": "Figures keep their colours and outlines in the Charcoal palette. Short text beside a tall figure becomes a slide, and folded sections list their key ideas.",
    "link": "subjects/aerospace-materials-1/teoria/topic-4-phase-diagrams.html"
  },
  {
    "id": "2026-11-18-mechanics-t6-essential",
    "date": "2026-11-18",
    "tag": "Engineering Mechanics",
    "title": "Topic 6 in Essential mode: what you need to know, section by section",
    "text": "Rigid bodies and inertia now open each section with a short plain summary and its key result. Switch to Essential to read only those, like a slide deck.",
    "link": "subjects/engineering-mechanics/teoria/topic-6.html"
  },
  {
    "id": "2026-11-18-theory-folding",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "Theory pages fold: sections, derivations and figures beside the text",
    "text": "Each section opens on demand, derivations show their result first, and a counter shows how much reading is left. On wide screens figures sit beside the text that explains them.",
    "link": "subjects/engineering-mechanics/teoria/topic-6.html"
  },
  {
    "id": "2026-11-18-theory-section-rail",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "Theory pages: section bars, wider text and shorter captions",
    "text": "Bars at the right edge jump to each section of a theory page. The text uses more of the screen, and long figure notes and source remarks now fold away.",
    "link": "subjects/engineering-mechanics/teoria/topic-6.html"
  },
  {
    "id": "2026-11-18-invite-accounts",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "Invite-only accounts that follow you to every device",
    "text": "Sideris accounts can now be opened with a personal invite code that works once. Sign in anywhere and your subjects, notes and study time come with you.",
    "link": "account/signup.html"
  },
  {
    "id": "2026-11-18-your-sky",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "Your sky: every day you study lights a star",
    "text": "My study now draws your own sky: a star for each day of study, joined into constellations on days in a row, plus eight achievements to unlock.",
    "link": "account/dashboard.html"
  },
  {
    "id": "2026-11-18-practise-mistakes",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "My study lists the simulator questions you still get wrong",
    "text": "Each simulator card in My study opens the list of questions you missed and have not got right since, with a link straight to each one.",
    "link": "account/dashboard.html"
  },
  {
    "id": "2026-11-18-weekly-goal",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "Set a weekly study goal and follow it in My study",
    "text": "Choose how many hours you want to study each week in Settings. My study shows a ring with how close you are over the last 7 days.",
    "link": "account/settings.html"
  },
  {
    "id": "2026-11-18-your-subjects-first",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "The portal now puts your subjects first",
    "text": "Signed in, the side menu lists your subjects first, What's new only shows their news and the portal's, and the home page brings their constellations forward.",
    "link": "account/settings.html"
  },
  {
    "id": "2026-11-18-favourites-and-notes",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "Star problems and keep your own notes on them",
    "text": "Signed in, every problem card has a star and a note button. Your notes show under the title even when the card is folded, and My study lists them all.",
    "link": "account/dashboard.html"
  },
  {
    "id": "2026-11-18-my-study-panel",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "My study: your exams, study time and where you left off",
    "text": "Signed-in students get a personal panel with exam countdowns, minutes studied per subject this week, the last page of each subject and their simulator grades.",
    "link": "account/dashboard.html"
  },
  {
    "id": "2026-11-18-planet-study-tools",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "Timer and Focus are now planets in each subject's colour",
    "text": "The study timer and Focus Lab buttons are drawn as small planets that take the colour of the subject you are reading. They now appear only on study pages.",
    "link": "subjects/fluid-mechanics/teoria/index.html"
  },
  {
    "id": "2026-11-18-accounts-and-settings",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "Create an account and set up the portal your way",
    "text": "Sign in from the top right, pick the subjects you take and your exam dates, and choose your reading palette, text size and study timer style in Settings.",
    "link": "account/signup.html"
  },
  {
    "id": "2026-11-18-business-topics-4-7",
    "date": "2026-11-18",
    "tag": "Business Management",
    "title": "Business Management Topics 4 to 7, with 23 more solved problems",
    "text": "New theory on production, marketing, management and innovation, plus solved sheets on break-even and leverage, price elasticity, and NPV and IRR.",
    "link": "subjects/business-management/teoria/index.html"
  },
  {
    "id": "2026-11-18-constellation-phone-fit",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "The star map fits phones better",
    "text": "On a phone the header buttons now fit the screen, the subject name sits above the Focus and Timer planets, and star labels never run off the edge.",
    "link": "index.html"
  },
  {
    "id": "2026-11-18-telescope-welcome",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "The welcome screen is now a telescope you fly into",
    "text": "A telescope on its stand greets you. Press Ignite and the camera dives into its lens, with music that turns from mystery to a stellar journey and then a calm sky.",
    "link": "index.html"
  },
  {
    "id": "2026-11-18-sideris-intro",
    "date": "2026-11-18",
    "tag": "Portal",
    "title": "A welcome screen and the sound of the sky",
    "text": "The home page opens on a telescope view of the night sky. Press Ignite to fly into the constellations, with celestial sound you can mute from the speaker button.",
    "link": "index.html"
  },
  {
    "id": "2026-11-17-materials-midterm-2-problems",
    "date": "2026-11-17",
    "tag": "Aerospace Materials I",
    "title": "Materials: 20 solved Midterm 2 problems in the simulator",
    "text": "Part II now has a longer phase-diagram problem (3 points) and a shorter Unit 5 problem (2 points), each solved step by step and drawn in every simulated exam.",
    "link": "subjects/aerospace-materials-1/extra-problems/midterm-2-problems.html"
  },
  {
    "id": "2026-11-17-materials-formula-sheet",
    "date": "2026-11-17",
    "tag": "Aerospace Materials I",
    "title": "Formula sheet for Units 4 to 7",
    "text": "A new formula sheet covers phase diagrams, mechanical, electrical, magnetic and thermal properties, with linear interpolation, the 0.2 % offset, solving steps and exam traps.",
    "link": "subjects/aerospace-materials-1/formula-sheet/index.html"
  },
  {
    "id": "2026-11-17-constellation-labels",
    "date": "2026-11-17",
    "tag": "Portal",
    "title": "Open a constellation and every star is labelled",
    "text": "Each star of an open constellation now points to a small badge with its icon, name and count, so you can see at once which star is Theory, Problems or PDFs.",
    "link": "index.html"
  },
  {
    "id": "2026-11-17-sideris-emblem",
    "date": "2026-11-17",
    "tag": "Portal",
    "title": "New Sideris constellation favicon and gold emblem",
    "text": "The browser tab now shows the subject-gradient constellation icon, while the gold orbital emblem marks the portal, Focus Lab, study timer and PDF library.",
    "link": "index.html"
  },
  {
    "id": "2026-11-17-materials-topics-8-11-review",
    "date": "2026-11-17",
    "tag": "Aerospace Materials I",
    "title": "Materials Topics 8-11: corrections and phone layout",
    "text": "Small corrections after checking Topics 8 to 11 against the slides and the solutions, and section titles that now wrap on phones instead of running off the screen.",
    "link": "subjects/aerospace-materials-1/teoria/topic-9-polymers.html"
  },
  {
    "id": "2026-11-17-living-sky",
    "date": "2026-11-17",
    "tag": "Portal",
    "title": "The star map now has a life of its own",
    "text": "Stars twinkle, the constellations drift, small lights run along their lines and shooting stars cross the sky. Everything calms down if your device asks for reduced motion.",
    "link": "index.html"
  },
  {
    "id": "2026-11-17-materials-topic-10",
    "date": "2026-11-17",
    "tag": "Aerospace Materials I",
    "title": "Composite materials: theory and 12 solved problems",
    "text": "Topic 10 of Aerospace Materials I: fibres, matrices, laminates, the rule of mixtures and how composites are made, with the 12 problems of the sheet solved step by step.",
    "link": "subjects/aerospace-materials-1/teoria/topic-10-composites.html"
  },
  {
    "id": "2026-11-17-materials-topic-9",
    "date": "2026-11-17",
    "tag": "Aerospace Materials I",
    "title": "Materials Topic 9: polymers, theory and nine solved problems",
    "text": "New theory page on polymers (structure, crystallinity, Tg and Tm, mechanical behaviour, families and processing) and the nine problems of the Topic 9 sheet solved step by step.",
    "link": "subjects/aerospace-materials-1/teoria/topic-9-polymers.html"
  },
  {
    "id": "2026-11-16-materials-topic-8",
    "date": "2026-11-16",
    "tag": "Aerospace Materials I",
    "title": "Aerospace Materials I: Topic 8, ceramic materials",
    "text": "New theory page on ceramics and glasses, from crystal structures to processing and the Shuttle tiles, with the seven problems of the sheet solved step by step.",
    "link": "subjects/aerospace-materials-1/teoria/topic-8-ceramics.html"
  },
  {
    "id": "2026-11-16-materials-topic-11",
    "date": "2026-11-16",
    "tag": "Aerospace Materials I",
    "title": "Aerospace Materials I: Topic 11 Adhesives theory",
    "text": "New theory page on adhesives: how adhesion works, the main adhesive families, how to design and prepare a bonded joint, and how joints fail and degrade.",
    "link": "subjects/aerospace-materials-1/teoria/topic-11-adhesives.html"
  },
  {
    "id": "2026-11-16-subject-skies",
    "date": "2026-11-16",
    "tag": "Portal",
    "title": "A starry sky on every subject index",
    "text": "The index pages of Theory, Problems, Extra problems, PDFs and Exams now sit on a slowly drifting night sky tinted with the colour of the subject. Cards and text are unchanged.",
    "link": "subjects/fluid-mechanics/teoria/index.html"
  },
  {
    "id": "2026-11-16-sideris-name",
    "date": "2026-11-16",
    "tag": "Portal",
    "title": "The portal is now called Sideris",
    "text": "New name, shown in the star map and in the browser tab, for example Sideris Fluids. The title uses the same colours as the old hub heading.",
    "link": "index.html"
  },
  {
    "id": "2026-11-16-stellar-home",
    "date": "2026-11-16",
    "tag": "Portal",
    "title": "New star map on the home page",
    "text": "Each subject is now a constellation. Click one to zoom in and pick Theory, Problems, PDFs and more. A button brings back the classic cards, and there are five sky palettes.",
    "link": "index.html"
  },
  {
    "id": "2026-11-16-materials-unit-6-7-practice",
    "date": "2026-11-16",
    "tag": "Aerospace Materials I",
    "title": "Materials: 100 more test questions and practice by unit",
    "text": "Units 6 and 7 now have 150 test questions each. The simulator can mix the real paper, focus on Units 6 and 7, or train one unit at a time.",
    "link": "subjects/aerospace-materials-1/simulator/index.html"
  },
  {
    "id": "2026-11-16-materials-midterm-2-simulator",
    "date": "2026-11-16",
    "tag": "Aerospace Materials I",
    "title": "Materials: Midterm 2 test bank and exam simulator",
    "text": "Test questions on Units 4 to 7 in blocks of ten, every answer explained, and a timed test marked with the real penalty. The solved problems come next.",
    "link": "subjects/aerospace-materials-1/simulator/index.html"
  },
  {
    "id": "2026-11-16-mechanics-simulators",
    "date": "2026-11-16",
    "tag": "Engineering Mechanics",
    "title": "Interactive 3D simulators in the rigid body problems",
    "text": "All 42 rigid body problems now have a simulator: turn the view, move the angles and watch the axes, the rotation matrix and the values of the solution update.",
    "link": "subjects/engineering-mechanics/problemas/topic-6.html"
  },
  {
    "id": "2026-11-16-mechanics-problems-8",
    "date": "2026-11-16",
    "tag": "Engineering Mechanics",
    "title": "Topic 8 problems: rolling, multibody and torque-free motion",
    "text": "26 official rigid body problems solved step by step: rolling, a yo-yo, Euler's disk, multibody systems with exploded views, and a free spinning asteroid.",
    "link": "subjects/engineering-mechanics/problemas/topic-8.html"
  },
  {
    "id": "2026-11-16-mechanics-rigid-body-problems-7",
    "date": "2026-11-16",
    "tag": "Engineering Mechanics",
    "title": "Rigid body problems: Topic 7 solved step by step",
    "text": "Eight official dynamics problems, from a spinner and Lagrange's top to a firedoor and a cylinder on two strings, each with free-body diagrams.",
    "link": "subjects/engineering-mechanics/problemas/topic-7.html"
  },
  {
    "id": "2026-11-15-mechanics-inertia-theory",
    "date": "2026-11-15",
    "tag": "Engineering Mechanics",
    "title": "Topic 6 theory now covers inertia properties",
    "text": "Centre of mass, moments and products of inertia, the inertia tensor, principal axes and Steiner's theorem, with four worked examples.",
    "link": "subjects/engineering-mechanics/teoria/topic-6.html"
  },
  {
    "id": "2026-11-15-mechanics-rigid-body-problems-6",
    "date": "2026-11-15",
    "tag": "Engineering Mechanics",
    "title": "Rigid body problems: Topic 6 solved step by step",
    "text": "Eight official problems on rigid body kinematics and moments of inertia, each worked from first principles with its own figures.",
    "link": "subjects/engineering-mechanics/problemas/topic-6.html"
  },
  {
    "id": "2026-11-15-mechanics-rigid-body-theory",
    "date": "2026-11-15",
    "tag": "Engineering Mechanics",
    "title": "Rigid body theory: Topics 6, 7 and 8",
    "text": "Three new theory pages cover rigid body kinematics and inertia, momentum, energy and dynamics, and rolling, multibody systems and torque-free motion.",
    "link": "subjects/engineering-mechanics/teoria/topic-6.html"
  },
  {
    "id": "2026-11-15-card-watermarks",
    "date": "2026-11-15",
    "tag": "Portal",
    "title": "Subject cards show the new icons in the background",
    "text": "The faint drawing behind each subject card on the home page is now the new icon of that subject.",
    "link": "index.html"
  },
  {
    "id": "2026-11-15-folded-problems",
    "date": "2026-11-15",
    "tag": "Portal",
    "title": "Problems start folded, shorter page headers",
    "text": "Every problem page now lists its problems folded: click one to open it, or use Open all. Page titles share one colour and the long intro texts are gone.",
    "link": "subjects/engineering-mechanics/problemas/topic-5.html"
  },
  {
    "id": "2026-11-15-exam-simulator-look",
    "date": "2026-11-15",
    "tag": "Portal",
    "title": "Cleaner exam simulator",
    "text": "The exam simulator now uses the same fonts and icons as the rest of the portal, with less text. The exam structure and the options fit on one screen.",
    "link": "subjects/advanced-maths/simulator/index.html"
  },
  {
    "id": "2026-11-15-pdf-library",
    "date": "2026-11-15",
    "tag": "Portal",
    "title": "One PDF page per subject, with search and filters",
    "text": "Course PDFs and past exams are now on the same page. Search by name, or filter by type, unit, exam and year. The Exams page will hold solved exams soon.",
    "link": "subjects/fluid-mechanics/sources/index.html"
  },
  {
    "id": "2026-11-15-delta-v-name",
    "date": "2026-11-15",
    "tag": "Portal",
    "title": "The portal is now called Delta V",
    "text": "New name and a new icon. The browser tab now shows the name and the subject you are in, for example Delta V Fluids."
  },
  {
    "id": "2026-11-15-tabs-extra-index-flat-pages",
    "date": "2026-11-15",
    "tag": "Portal",
    "title": "Clearer tab icons, short Extra problems index, no glow",
    "text": "New icons for Extra problems, Exam simulator and PDFs. The Extra problems index shows one short button per item. Topic pages no longer glow on hover.",
    "link": "subjects/advanced-maths/extra-problems/index.html"
  },
  {
    "id": "2026-11-15-section-tabs-icons",
    "date": "2026-11-15",
    "tag": "Portal",
    "title": "Section tabs with icons and tidier subject indexes",
    "text": "The tabs to move between theory, problems, exams and PDFs now have icons. Index cards are larger and centred, with more room under the title and no glow."
  },
  {
    "id": "2026-11-15-compact-subject-indexes",
    "date": "2026-11-15",
    "tag": "Portal",
    "title": "Subject indexes fit on one screen",
    "text": "The theory and problem indexes of every subject are now short cards in a grid, with the new subject icons. The site is now called Orbit and has a simpler icon."
  },
  {
    "id": "2026-11-15-timer-focus-look",
    "date": "2026-11-15",
    "tag": "Portal",
    "title": "Timer and Focus: clearer buttons in each page's colours",
    "text": "The Timer and Focus buttons and panels use the colour of the subject you are in, the home page gradient on the home page, and the same fonts as the rest of the site."
  },
  {
    "id": "2026-11-15-portal-new-home",
    "date": "2026-11-15",
    "tag": "Portal",
    "title": "A cleaner home page",
    "text": "The home page is simpler: compact subject cards with direct buttons to theory, problems, PDFs and exams, new icons and a working dark and light switch.",
    "link": "index.html"
  },
  {
    "id": "2026-11-14-mechanics-class-badges",
    "date": "2026-11-14",
    "tag": "Engineering Mechanics",
    "title": "Problems solved in class are now marked",
    "text": "Each mechanics problem done in a class session shows its session number, and the oscillation problems of Lecture 6 are marked too.",
    "link": "subjects/engineering-mechanics/problemas/index.html"
  },
  {
    "id": "2026-11-14-mechanics-lectures-6-10",
    "date": "2026-11-14",
    "tag": "Engineering Mechanics",
    "title": "Five new lecture decks: oscillations and rigid bodies",
    "text": "Lectures 6 to 10 (oscillations, rigid body kinematics, inertia, momentum and energy, rigid body dynamics) are now on the PDFs page.",
    "link": "subjects/engineering-mechanics/sources/index.html"
  },
  {
    "id": "2026-11-11-materials-slide-figures",
    "date": "2026-11-11",
    "tag": "Aerospace Materials I",
    "title": "Materials Topics 1 to 7: figures now copied from the slides",
    "text": "Theory figures that appear on the official slides are now exact copies of them instead of redrawings. Drawings made for the page, such as worked examples, stay as they were.",
    "link": "subjects/aerospace-materials-1/teoria/index.html"
  },
  {
    "id": "2026-11-10-fluids-t7-problems",
    "date": "2026-11-10",
    "tag": "Fluid Mechanics",
    "title": "Fluid Mechanics Topic 7: 19 solved problems",
    "text": "The viscous-flow sheets VF2 to VF20 are solved step by step: annular flows, belt pumps, a journal bearing, squeeze films and a levitated cylinder. Slips of the keys are flagged.",
    "link": "subjects/fluid-mechanics/problemas/topic-7-viscous-flow.html"
  },
  {
    "id": "2026-11-10-fluids-t7-theory",
    "date": "2026-11-10",
    "tag": "Fluid Mechanics",
    "title": "Fluid Mechanics Topic 7: viscous flows",
    "text": "New theory page for Chapter 7: Couette and Poiseuille flows, Stokes layers, slender films, the wedge effect and the criteria for viscous dominance, with a practical formulary.",
    "link": "subjects/fluid-mechanics/teoria/topic-7.html"
  },
  {
    "id": "2026-11-10-fluids-t6-problems",
    "date": "2026-11-10",
    "tag": "Fluid Mechanics",
    "title": "Fluid Mechanics Topic 6: 14 solved problems",
    "text": "The dimensional-analysis sheets DA1 to DA14 are solved step by step after their keys: ships, turbines, wings, propellers, a missile and a Mars parachute.",
    "link": "subjects/fluid-mechanics/problemas/topic-6-dimensional-analysis.html"
  },
  {
    "id": "2026-11-10-fluids-t6-theory",
    "date": "2026-11-10",
    "tag": "Fluid Mechanics",
    "title": "Fluid Mechanics Topic 6: dimensional analysis",
    "text": "New theory page for Chapter 6: the Pi theorem, Taylor's explosion, the nondimensional Navier-Stokes equations, the limits of large and small Reynolds number and scale models.",
    "link": "subjects/fluid-mechanics/teoria/topic-6.html"
  },
  {
    "id": "2026-11-08-materials-audit-fixes",
    "date": "2026-11-08",
    "tag": "Aerospace Materials I",
    "title": "Materials Topics 4 to 7: audit corrections",
    "text": "Fixed slide links in Topic 4, two formula slips in Topic 5, drawings in Topics 4, 6 and 7 and plain-text links, and added missing slide figures and problem counts.",
    "link": "subjects/aerospace-materials-1/teoria/index.html"
  },
  {
    "id": "2026-11-07-materials-topic-7-problems",
    "date": "2026-11-07",
    "tag": "Aerospace Materials I",
    "title": "Materials Topic 7: 2 solved problems",
    "text": "The two magnetic problems of the Topic 6 and 7 sheet are solved step by step: the loops of soft and hard magnets, and how grain size, impurities and pores change a ferromagnet.",
    "link": "subjects/aerospace-materials-1/problemas/topic-7-magnetic-thermal.html"
  },
  {
    "id": "2026-11-07-materials-topic-5-wording",
    "date": "2026-11-07",
    "tag": "Aerospace Materials I",
    "title": "Materials Topic 5: clearer problem page and wire note",
    "text": "The Topic 5 problems page no longer describes its solutions as phases, and the thermal stress wire problem now explains where the 5.86 mm of the official key comes from.",
    "link": "subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html"
  },
  {
    "id": "2026-11-07-materials-topic-7-review",
    "date": "2026-11-07",
    "tag": "Aerospace Materials I",
    "title": "Materials Topic 7: corrected drawings and notes",
    "text": "A full review fixed the thermal shock and magnetic domain drawings and the wire example, and added notes where the slides disagree. Long links no longer widen the page on phones.",
    "link": "subjects/aerospace-materials-1/teoria/topic-7-magnetic-thermal.html"
  },
  {
    "id": "2026-11-07-materials-topic-7",
    "date": "2026-11-07",
    "tag": "Aerospace Materials I",
    "title": "Materials Topic 7: magnetic and thermal properties",
    "text": "New theory page on magnetism, domains and hysteresis, superconductors, heat capacity, thermal expansion and conductivity, and thermal stress and shock, with drawings.",
    "link": "subjects/aerospace-materials-1/teoria/topic-7-magnetic-thermal.html"
  },
  {
    "id": "2026-11-06-materials-topic-6",
    "date": "2026-11-06",
    "tag": "Aerospace Materials I",
    "title": "Materials Topic 6: electrical properties and 10 solved problems",
    "text": "New theory page on energy bands, metals, semiconductors, dielectrics and piezoelectrics, with 10 official problems solved step by step and drawings for every slide.",
    "link": "subjects/aerospace-materials-1/teoria/topic-6-electrical-properties.html"
  },
  {
    "id": "2026-11-03-fluids-hydrostatics",
    "date": "2026-11-03",
    "tag": "Fluid Mechanics",
    "title": "Topic 5: hydrostatics theory and 9 solved problems",
    "text": "New theory page on fluids at rest, gates, Archimedes and the standard atmosphere, plus the official sheets solved step by step. Three solutions have an interactive simulator.",
    "link": "subjects/fluid-mechanics/problemas/topic-5-hydrostatics.html"
  },
  {
    "id": "2026-10-24-mechanics-formula-sheet",
    "date": "2026-10-24",
    "tag": "Engineering Mechanics",
    "title": "Formula sheet: kinematics to relative motion, step by step",
    "text": "A new formula sheet covers Topics 1 to 5 with the reason for each step, the solving order of the course and exam traps. A compact view prints it in a few A4 pages.",
    "link": "subjects/engineering-mechanics/formula-sheet/index.html"
  },
  {
    "id": "2026-10-24-maths-formula-sheet",
    "date": "2026-10-24",
    "tag": "Advanced Maths",
    "title": "Formula sheet: every formula with its derivation and recipe",
    "text": "A new formula sheet covers all units, with the reason for each step, exam traps and solving recipes. A compact view prints the whole sheet in six A4 pages.",
    "link": "subjects/advanced-maths/formula-sheet/index.html"
  },
  {
    "id": "2026-10-23-mechanics-topic5-figures",
    "date": "2026-10-23",
    "tag": "Engineering Mechanics",
    "title": "Topic 5 problems rebuilt in the course order, with 47 drawings",
    "text": "All 20 relative-motion problems now go frames, change of basis, kinematics, forces, answers. New drawings show each rotation and the triangle behind every sine and cosine.",
    "link": "subjects/engineering-mechanics/problemas/topic-5.html"
  },
  {
    "id": "2026-10-22-solutions-without-phase-labels",
    "date": "2026-10-22",
    "tag": "Portal",
    "title": "Worked solutions drop the Phase 1 to 4 labels",
    "text": "Generated solutions no longer show the Phase 1 to 4 labels. Each block keeps its own heading, so the solutions read as one continuous derivation.",
    "link": "subjects/engineering-mechanics/problemas/topic-5.html"
  },
  {
    "id": "2026-10-22-mechanics-bank-figure-lines",
    "date": "2026-10-22",
    "tag": "Engineering Mechanics",
    "title": "Construction lines back in the extra problem figures",
    "text": "The dashed guide lines, hatching and dimension lines of the Mechanics extra problem figures were invisible on the default palette. They now show in grey.",
    "link": "subjects/engineering-mechanics/extra-problems/midterm-1-problems.html"
  },
  {
    "id": "2026-10-22-maths-extra-problems-simulator",
    "date": "2026-10-22",
    "tag": "Advanced Maths",
    "title": "Maths extra problems and exam simulator",
    "text": "22 solved exam-style problems for the two midterms and the final, plus a timed exam simulator for each of them that you grade yourself.",
    "link": "subjects/advanced-maths/extra-problems/index.html"
  },
  {
    "id": "2026-10-22-maths-ch4-problems-class-method",
    "date": "2026-10-22",
    "tag": "Advanced Maths",
    "title": "Maths Chapter 4 problems linked to the class notes method",
    "text": "All 19 Chapter 4 problems now show the class-notes route: elimination, diagonalisation z = P^-1 x, the zero eigenvalue, Q = PM for complex pairs and the repeated-eigenvalue cases.",
    "link": "subjects/advanced-maths/problemas/topic-4-part-1.html"
  },
  {
    "id": "2026-10-22-maths-ch3-problems-class-method",
    "date": "2026-10-22",
    "tag": "Advanced Maths",
    "title": "Maths Chapter 3 problems linked to the class notes method",
    "text": "All 20 Chapter 3 problems now show the class-notes route: Cases 01 to 03, the Wronskian matrix, x = xH + xN with the educated guess, reduction of order and variation of constants.",
    "link": "subjects/advanced-maths/problemas/topic-3-problems.html"
  },
  {
    "id": "2026-10-22-maths-ch2-problems-class-method",
    "date": "2026-10-22",
    "tag": "Advanced Maths",
    "title": "Maths Chapter 2 problems linked to the class notes method",
    "text": "Each of the 17 Chapter 2 problems now shows the class-notes route: separation, the three-step integrating factor, exact equations, Picard and the f' stability test.",
    "link": "subjects/advanced-maths/problemas/topic-2-problems.html"
  },
  {
    "id": "2026-10-22-maths-ch1-problems-class-method",
    "date": "2026-10-22",
    "tag": "Advanced Maths",
    "title": "Maths Chapter 1 problems solved the way of the class notes",
    "text": "The ten Chapter 1 problems now use the methods of the class notes: integration from 0 to t, the three-step integrating factor and the superposition test.",
    "link": "subjects/advanced-maths/problemas/topic-1-problems.html"
  },
  {
    "id": "2026-10-22-maths-topic-4-class-notes",
    "date": "2026-10-22",
    "tag": "Advanced Maths",
    "title": "Maths Topic 4 now follows the class notes",
    "text": "Systems in the order of the notes, with new phase portraits for two real eigenvalues and a zero eigenvalue, and the notes' route for complex and repeated eigenvalues.",
    "link": "subjects/advanced-maths/teoria/topic-4.html"
  },
  {
    "id": "2026-10-22-maths-topic-3-class-notes",
    "date": "2026-10-22",
    "tag": "Advanced Maths",
    "title": "Maths Topic 3 now follows the class notes",
    "text": "Second-order equations in the order of the notes: the Wronskian, the three cases, x'' + x' - 6x for three forcings, and variation of constants with the sign of u1' corrected.",
    "link": "subjects/advanced-maths/teoria/topic-3.html"
  },
  {
    "id": "2026-10-22-maths-topic-2-class-notes",
    "date": "2026-10-22",
    "tag": "Advanced Maths",
    "title": "Maths Topic 2 now follows the class notes",
    "text": "Picard's theorem, stability, separable, linear and exact equations in the order of the notes, with the logistic equation and both exact examples solved step by step.",
    "link": "subjects/advanced-maths/teoria/topic-2.html"
  },
  {
    "id": "2026-10-22-maths-topic-1-class-notes",
    "date": "2026-10-22",
    "tag": "Advanced Maths",
    "title": "Maths Topic 1 now follows the class notes",
    "text": "Sections 1 to 6 now follow page 2 of the class notes: the linearity test step by step, and the population and free-fall examples solved in full.",
    "link": "subjects/advanced-maths/teoria/topic-1.html"
  },
  {
    "id": "2026-10-21-maths-chapter-3-4-new-sheets",
    "date": "2026-10-21",
    "tag": "Advanced Maths",
    "title": "Maths: 28 new solved exercises (Chapter 3 part 2, Chapter 4)",
    "text": "Three new problem pages with every step written out: forced oscillations and resonance, systems of ODEs, eigenvalues, phase portraits and canonical forms.",
    "link": "subjects/advanced-maths/problemas/topic-4-part-1.html"
  },
  {
    "id": "2026-10-21-mechanics-final-review",
    "date": "2026-10-21",
    "tag": "Engineering Mechanics",
    "title": "Mechanics problems: final review of all 51 solutions",
    "text": "A last check of every solved problem filled in missing steps and fixed a few answers and remarks, such as the top equilibrium in problem 23 and a wrong limit in problem 17.",
    "link": "subjects/engineering-mechanics/problemas/index.html"
  },
  {
    "id": "2026-10-21-maths-complex-and-repeated-eigenvalues",
    "date": "2026-10-21",
    "tag": "Advanced Maths",
    "title": "Maths Topic 4: complex and repeated eigenvalues, step by step",
    "text": "Spirals, centres, stars and improper nodes are rewritten with every change of basis worked out and phase portraits drawn in both the canonical and the original plane.",
    "link": "subjects/advanced-maths/teoria/topic-4.html"
  },
  {
    "id": "2026-10-21-mechanics-topic-5-course-order",
    "date": "2026-10-21",
    "tag": "Engineering Mechanics",
    "title": "Mechanics Topic 5: solutions in the course order",
    "text": "The twenty relative-motion problems now follow the course method step by step: kinematics, forces, equations of motion, then results and checks against the official keys.",
    "link": "subjects/engineering-mechanics/problemas/topic-5.html"
  },
  {
    "id": "2026-10-21-mechanics-topic-3-course-order",
    "date": "2026-10-21",
    "tag": "Engineering Mechanics",
    "title": "Mechanics Topic 3: solutions in the course order",
    "text": "The twelve constraint and reaction problems follow the course method step by step. Problem 24 now matches its statement and problem 31 notes an error in the official key.",
    "link": "subjects/engineering-mechanics/problemas/topic-3.html"
  },
  {
    "id": "2026-10-21-mechanics-topic-2-course-order",
    "date": "2026-10-21",
    "tag": "Engineering Mechanics",
    "title": "Mechanics Topic 2: solutions in the course order",
    "text": "The ten dynamics problems follow the course method step by step. A force formula in problem 13 and several damping values in problem 46 were corrected.",
    "link": "subjects/engineering-mechanics/problemas/topic-2.html"
  },
  {
    "id": "2026-10-21-mechanics-topic-1-course-order",
    "date": "2026-10-21",
    "tag": "Engineering Mechanics",
    "title": "Mechanics Topic 1: solutions in the course order",
    "text": "The six kinematics problems now follow the course method step by step, with the missing validity limits added and the normal vector defined as in the notes.",
    "link": "subjects/engineering-mechanics/problemas/topic-1.html"
  },
  {
    "id": "2026-10-21-mechanics-topic-4-course-order",
    "date": "2026-10-21",
    "tag": "Engineering Mechanics",
    "title": "Mechanics Topic 4: solutions in the course order",
    "text": "Problems 42 to 44 now follow the course method: constraints, kinematics, forces, equations of motion, answers. Some missing cases were added and a few values were corrected.",
    "link": "subjects/engineering-mechanics/problemas/topic-4.html"
  },
  {
    "id": "2026-10-19-materials-topic-5-problems-3",
    "date": "2026-10-19",
    "tag": "Aerospace Materials I",
    "title": "Materials Topic 5: all 15 problems solved",
    "text": "True stress and strain, plus Vickers and Brinell hardness: the last four problems complete the sheet, each checked against the key.",
    "link": "subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html"
  },
  {
    "id": "2026-10-19-materials-topic-5-problems-2",
    "date": "2026-10-19",
    "tag": "Aerospace Materials I",
    "title": "Materials Topic 5: problems 5 to 11 solved",
    "text": "Thermal stress, elastic limits, cable design with Poisson's ratio, and unloading of a copper wire, each with the sheet key checked.",
    "link": "subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html"
  },
  {
    "id": "2026-10-19-materials-topic-5-problems-1",
    "date": "2026-10-19",
    "tag": "Aerospace Materials I",
    "title": "Materials Topic 5: first four solved problems",
    "text": "Problems 1 to 4 of the mechanical properties sheet: full analyses of tensile tests, with the curves drawn from the sheet data and the key checked.",
    "link": "subjects/aerospace-materials-1/problemas/topic-5-mechanical-properties.html"
  },
  {
    "id": "2026-10-19-materials-topic-5-theory",
    "date": "2026-10-19",
    "tag": "Aerospace Materials I",
    "title": "Materials Topic 5: mechanical properties theory",
    "text": "The tensile test, stress-strain curve, toughness, strengthening mechanisms and hardness tests, from Sessions 11 and 12, with 27 figures.",
    "link": "subjects/aerospace-materials-1/teoria/topic-5-mechanical-properties.html"
  },
  {
    "id": "2026-10-19-close-solution-button",
    "date": "2026-10-19",
    "tag": "Portal",
    "title": "Close button at the end of every worked solution",
    "text": "Long solutions can now be folded from their last line. The button takes you back to the problem, so you no longer scroll up to the top of the solution to close it.",
    "link": "subjects/engineering-mechanics/problemas/topic-1.html"
  },
  {
    "id": "2026-10-19-mechanics-problems-audit",
    "date": "2026-10-19",
    "tag": "Engineering Mechanics",
    "title": "Mechanics problems reorganised: 51 problems, each in its unit",
    "text": "Repeated problems were removed and each one now sits in the unit that teaches its tools. Problems 45 and 46 were added, and missing figures were restored.",
    "link": "subjects/engineering-mechanics/problemas/index.html"
  },
  {
    "id": "2026-10-18-mechanics-extra-problems-simulator",
    "date": "2026-10-18",
    "tag": "Engineering Mechanics",
    "title": "Midterm 1 extra problems and exam simulator",
    "text": "16 new problems of 10 points with technical sketches and 8 conceptual questions for the first partial, plus a timed exam simulator that grades you part by part.",
    "link": "subjects/engineering-mechanics/extra-problems/index.html"
  },
  {
    "id": "2026-10-17-business-extra-problems-pages",
    "date": "2026-10-17",
    "tag": "Business Management",
    "title": "Extra problems split into theory cases and practice problems",
    "text": "The Extra problems page is now a hub with two pages for the 1st Midterm, one for the theory cases and one for the six practice problems. Both can be downloaded as PDF.",
    "link": "subjects/business-management/extra-problems/index.html"
  },
  {
    "id": "2026-10-17-business-extra-problems-midterm",
    "date": "2026-10-17",
    "tag": "Business Management",
    "title": "Extra problems now laid out like the other problem pages",
    "text": "One 1st Midterm block with 24 theory cases and 6 exam-style problems, each with its statement and full solution. The official exercises stay on the Problems page.",
    "link": "subjects/business-management/extra-problems/index.html"
  },
  {
    "id": "2026-10-16-fluids-navier-stokes-problems",
    "date": "2026-10-16",
    "tag": "Fluid Mechanics",
    "title": "Fluid Mechanics: solved Navier-Stokes problems (Topic 4)",
    "text": "The 17 official Navier-Stokes problems are solved, each with the statement word for word, its figure and a four-phase solution.",
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
