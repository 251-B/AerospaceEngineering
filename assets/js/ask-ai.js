/*!
 * Aerospace Engineering Study Portal: "Ask AI" (Claude or Gemini) on the study material.
 *
 * Load once per theory or problem page, after theme.js:
 *     <script defer src="../../../assets/js/ask-ai.js"></script>
 * The script adds its own stylesheet (assets/css/ask-ai.css, found next to this file).
 *
 * Two entry points:
 *   - Select a sentence, a formula or a step: an "Ask AI" pill appears next to the selection.
 *   - Problem pages: under each statement, a bar offers a Socratic tutor and a full explanation of
 *     the solution. The prompt carries the statement and the page's solution (as a reference the
 *     tutor must not reveal in Socratic mode).
 * The panel builds a structured prompt (role, context, material, task, answer rules) with formulas
 * as their LaTeX source read from KaTeX, then:
 *   - Claude: opens claude.ai/new?q=<prompt> (or copies it and opens claude.ai when it is too long);
 *   - Gemini: copies the prompt and opens gemini.google.com (Gemini has no prefill link).
 * Each student uses their own account; this page calls no API and sends nothing by itself.
 *
 * Storage: 'ae_ask_lang' ('es' | 'en'), the language the assistant is asked to answer in.
 */
(function () {
  'use strict';

  var SCRIPT = document.currentScript;
  var LANG_KEY = 'ae_ask_lang';
  var MAX_FRAGMENT = 4000;
  var MAX_SOLUTION = 14000;
  var MAX_URL = 7500;
  var PROVIDERS = {
    claude: { name: 'Claude', open: 'https://claude.ai/new', prefill: 'https://claude.ai/new?q=' },
    gemini: { name: 'Gemini', open: 'https://gemini.google.com/app', prefill: null }
  };

  var SUBJECTS = {
    'fluid-mechanics': 'Fluid Mechanics',
    'aerospace-materials-1': 'Aerospace Materials I',
    'engineering-mechanics': 'Engineering Mechanics (Mechanics Applied to Aerospace Engineering)',
    'advanced-maths': 'Advanced Mathematics (ordinary differential equations)',
    'business-management': 'Business Management'
  };

  var SOLUTION_SEL = '.phase-block, .phase-section, .solution-box, .solution-details, .phases-grid, ' +
    '.strategy-callout, .phase-title, .result-box, .result-callout';
  var STATEMENT_SEL = '.problem-statement-box, .statement-box, .problem-statement';
  var CARD_SEL = '.problem-card, .problem-box';

  /* ------------------------------------------------------------------ tasks
     needs: 'fragment' (selected text) | 'statement' | 'solution' (reference solution in the prompt)
     hidden: the reference solution is for checking only and must not be revealed */
  var SOCRATIC_RULES = [
    'If the statement already quotes the official final answer, treat it only as the target: what I must learn is the method.',
    'Work as a Socratic tutor. Do NOT give me the solution, the next step or the final result.',
    'Ask ONE short question per message, then stop and wait for my reply.',
    'Start from what I already know: first ask me what is asked, which data and unknowns there are, and which principle or equation of the course I would use.',
    'When I answer, say clearly whether it is right. If it is wrong, do not correct it: ask a question or give a check (units, a limiting case, a sign, a special value) that lets me find the mistake myself.',
    'If I am stuck, give graded hints, one at a time: (1) the principle to use, (2) the equation, (3) the first line of the step. Never jump to the full step.',
    'Every few steps, ask me to summarise what we have done in one sentence.',
    'When I reach the result, check it against the reference, ask me for a dimensional check and a physical interpretation, and finish with a short list of the mistakes I made and how to avoid them.',
    'Reveal the reference solution only if I write "show solution".'
  ].map(function (r) { return '- ' + r; });

  var TASKS = {
    /* theory: selection */
    simple: { label: 'Explain simply', needs: ['fragment'],
      task: ['Explain this fragment so that I understand it completely, in simple words, as a good teacher would at the blackboard.',
        'Start with the idea in one or two plain sentences, then go through it line by line. Define every symbol and quantity (with its SI unit) the first time it appears.',
        'If it contains an equation or a derivation, show every step with nothing skipped. End with a short summary of what I must remember.'] },
    derive: { label: 'Step-by-step derivation', needs: ['fragment'],
      task: ['Derive or justify this result step by step, from the starting principles of the course, with no algebraic jumps.',
        'For each step write the operation you do and why it is allowed (which law, assumption or theorem).'] },
    why: { label: 'Why does it hold?', needs: ['fragment'],
      task: ['Explain where this comes from and why it holds: the physical (or economic) idea behind it, the assumptions it needs, and when it stops being valid.',
        'Give one limiting case or special case that makes it intuitive.'] },
    example: { label: 'Worked example', needs: ['fragment'],
      task: ['Give me one short worked numerical example that uses this, with realistic data, solved completely with every step shown, ending with a dimensional check.'] },
    socraticTheory: { label: 'Socratic: let me work it out', needs: ['fragment'], socratic: true,
      task: ['Help me understand this fragment by working it out myself.',
        '- Work as a Socratic tutor: do NOT explain it to me directly.',
        '- Ask ONE short question per message, then stop and wait for my reply.',
        '- Start from what I already know (definitions, earlier results of the course) and lead me, question by question, to each idea or step of the fragment.',
        '- When I answer, say clearly whether it is right. If it is wrong, do not correct it: ask a question or give a check (units, a limiting case, a special value) that lets me find the mistake myself.',
        '- If I am stuck, give graded hints, one at a time, never the full answer.',
        '- When I can explain it in my own words, give me a two-line summary and one question to check it stuck.',
        'Begin now with your first question only.'] },
    quiz: { label: 'Quiz me', needs: ['fragment'],
      task: ['Test whether I understand this. Ask me 4 questions, one at a time, from easy to harder (concept, meaning of a symbol, a small calculation, a "what happens if" question).',
        'Wait for each answer, correct it with a short explanation, then ask the next one. Finish with a score and what I should review.'] },

    /* problems: selection inside a solution */
    step: { label: 'Explain this step', needs: ['fragment', 'statement'],
      task: ['Explain this part of the solution in full detail: what is done, why it is done here, and why it is allowed.',
        'Rewrite it with every intermediate step that is skipped, and say where every number comes from.'] },
    method: { label: 'Why this method?', needs: ['fragment', 'statement'],
      task: ['Explain why this equation or method is the right choice at this point of the problem, what the alternatives would be and why they fit worse.'] },
    concept: { label: 'Theory behind it', needs: ['fragment', 'statement'],
      task: ['Explain the theory this relies on, simply and completely, with every symbol defined, and then show how it is applied in this step.'] },
    socraticStep: { label: 'Socratic: guide me', needs: ['fragment', 'statement', 'solution'], hidden: true, socratic: true,
      task: ['I want to reach this step of the solution by myself.'].concat(SOCRATIC_RULES).concat(['Begin now with your first question only.']) },

    /* problems: whole problem (bar under the statement) */
    solveSocratic: { label: 'Socratic tutor', needs: ['statement', 'solution'], hidden: true, socratic: true, card: true,
      task: ['Help me solve this problem by myself, from the start.'].concat(SOCRATIC_RULES).concat(['Begin now with your first question only.']) },
    explainSolution: { label: 'Explain the full solution', needs: ['statement', 'solution'], card: true,
      task: ['Explain the reference solution of this problem from start to finish so that I understand every detail, as a teacher would at the blackboard. Structure the answer as:',
        '1. **What is asked**: the statement in plain words; a table of the data (value and SI unit) and of the unknowns.',
        '2. **Strategy**: the principles and equations used, why they are the right ones here, and what the alternatives would be.',
        '3. **Step-by-step solution**: every step of the reference solution, with all the intermediate algebra and arithmetic that it skips, and the reason for each step.',
        '4. **Result and checks**: the final result with units, a dimensional check, and its physical meaning or limiting cases.',
        '5. **Typical mistakes** in this kind of problem and how to avoid them.'] },
    explainStatement: { label: 'Understand the statement', needs: ['statement'], card: true,
      task: ['Help me understand the statement WITHOUT solving it: rewrite it in simple words, describe the situation (what a sketch would show), list the data with SI units and the unknowns,',
        'and say which theory and equations of the course are involved and why. Do not compute anything.'] },
    checkAttempt: { label: 'Check my attempt', needs: ['statement', 'solution'], hidden: true, card: true, attempt: true,
      task: ['Below is my attempt. Compare it with the reference solution step by step.',
        'Tell me which steps are right. For the FIRST mistake, explain what is wrong and why, and give me a hint to fix it, but do not write the corrected step or the final result.',
        'Wait for my corrected version before checking the rest.'] },
    similar: { label: 'Similar exercise', needs: ['statement'], card: true,
      task: ['Write ONE new exercise of the same type and difficulty, with different data, for me to practise. Give only the statement.',
        'When I send my answer, correct it step by step, and solve it in full only if I ask for it.'] }
  };

  var THEORY_ACTIONS = ['simple', 'derive', 'why', 'example', 'socraticTheory', 'quiz'];
  var PROBLEM_SELECTION_ACTIONS = ['step', 'method', 'concept', 'socraticStep'];
  var CARD_ACTIONS = ['explainSolution', 'solveSocratic', 'explainStatement', 'checkAttempt', 'similar'];

  var state = { pill: null, panel: null, ui: null, range: null, req: null, action: null, lastFocus: null };

  /* ------------------------------------------------------------------ helpers */
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  function readLang() {
    try { var v = localStorage.getItem(LANG_KEY); if (v === 'es' || v === 'en') return v; } catch (e) { /* blocked */ }
    return 'es';
  }

  function writeLang(v) {
    try { localStorage.setItem(LANG_KEY, v); } catch (e) { /* blocked: keep in memory */ }
  }

  function clean(s) {
    return (s || '').replace(/\s+/g, ' ').trim();
  }

  function cap(s, n) {
    return s.length > n ? s.slice(0, n) + '\n[… truncated]' : s;
  }

  function contentRoot() {
    return document.querySelector('main') || document.body;
  }

  function isProblemPage() {
    return /\/problemas\//.test(location.pathname);
  }

  function subjectSlug() {
    var m = location.pathname.match(/\/subjects\/([^/]+)\//);
    return m ? m[1] : '';
  }

  function insideUi(node) {
    var e = node && (node.nodeType === 1 ? node : node.parentElement);
    return !!(e && e.closest('.ask-ai-pill, .ask-ai-panel, .ask-ai-bar, input, textarea, .site-header'));
  }

  /* ------------------------------------------------------------------ DOM -> text with LaTeX */
  function katexAncestor(node) {
    var e = node && (node.nodeType === 1 ? node : node.parentElement);
    return e ? e.closest('.katex-display, .katex') : null;
  }

  function widenOverMath(range) {
    var r = range.cloneRange();
    var a = katexAncestor(r.startContainer);
    if (a) r.setStartBefore(a.closest('.katex-display') || a);
    var b = katexAncestor(r.endContainer);
    if (b) r.setEndAfter(b.closest('.katex-display') || b);
    return r;
  }

  function texOf(k) {
    var ann = k.querySelector('annotation[encoding="application/x-tex"]');
    return ann ? ann.textContent.trim() : clean(k.textContent);
  }

  var BLOCK = /^(P|DIV|LI|UL|OL|H[1-6]|TR|TABLE|SECTION|ARTICLE|BLOCKQUOTE|FIGURE|FIGCAPTION|DETAILS|SUMMARY)$/;

  function serialize(node, out) {
    if (node.nodeType === 3) { out.push(node.nodeValue.replace(/\s+/g, ' ')); return; }
    if (node.nodeType !== 1 && node.nodeType !== 11) return;
    if (node.nodeType === 1) {
      var c = node.classList, tag = node.tagName;
      if (c.contains('katex-display')) { out.push('\n$$' + texOf(node) + '$$\n'); return; }
      if (c.contains('katex')) { out.push('$' + texOf(node) + '$'); return; }
      if (c.contains('katex-mathml') || c.contains('ask-ai-bar') || c.contains('src-link') ||
          tag === 'SCRIPT' || tag === 'STYLE' || tag === 'BUTTON' || tag === 'svg' || tag === 'SVG') return;
      if (tag === 'BR') { out.push('\n'); return; }
      if (tag === 'TD' || tag === 'TH') out.push(' | ');
      if (tag === 'LI') out.push('\n- ');
      if (/^H[1-6]$/.test(tag)) out.push('\n\n');
    }
    for (var ch = node.firstChild; ch; ch = ch.nextSibling) serialize(ch, out);
    if (node.nodeType === 1 && BLOCK.test(node.tagName)) out.push('\n');
  }

  function tidy(s) {
    return s.replace(/[ \t]+\n/g, '\n').replace(/\n[ \t]+/g, '\n').replace(/\n{3,}/g, '\n\n').replace(/ {2,}/g, ' ').trim();
  }

  function textOfRange(range, max) {
    var out = [];
    serialize(range.cloneContents(), out);
    return cap(tidy(out.join('')), max);
  }

  /* ------------------------------------------------------------------ problem cards */
  function cardOf(node) {
    var e = node && (node.nodeType === 1 ? node : node.parentElement);
    return e ? e.closest(CARD_SEL) : null;
  }

  function cardTitle(card) {
    var t = card.querySelector('.problem-title') || card.querySelector('h2, h3');
    var n = card.querySelector('.problem-num, .problem-num-badge, .prob-num-badge, .problem-id, .problem-tag');
    return clean((n ? n.textContent + ' · ' : '') + (t ? t.textContent : ''));
  }

  function statementBlock(card) {
    var s = card.querySelector(STATEMENT_SEL);
    if (s) return s;
    var hs = card.querySelectorAll('h3, h4, h5');
    for (var i = 0; i < hs.length; i++) {
      if (/statement/i.test(hs[i].textContent)) return hs[i].parentElement !== card ? hs[i].parentElement : hs[i];
    }
    return null;
  }

  function isSolutionPart(n) {
    return n.matches(SOLUTION_SEL) || !!n.querySelector(SOLUTION_SEL);
  }

  /* Split a card into its statement and its solution (two ranges), whatever the page's markup. */
  function splitCard(card) {
    if (card._askAiSplit) return card._askAiSplit;
    var head = card.querySelector(':scope > summary') || card.querySelector('.problem-header');
    var st = statementBlock(card), end = st;
    var stmt = document.createRange(), sol = document.createRange();
    if (head) stmt.setStartAfter(head); else stmt.setStart(card, 0);
    if (st) {
      for (var n = st.nextElementSibling; n && !isSolutionPart(n) && !n.classList.contains('ask-ai-bar'); n = n.nextElementSibling) end = n;
      stmt.setEndAfter(end);
      sol.setStartAfter(end);
    } else {
      var first = card.querySelector(SOLUTION_SEL);
      if (first) { stmt.setEndBefore(first); sol.setStartBefore(first); end = first.previousElementSibling; }
      else { stmt.setEnd(card, card.childNodes.length); sol.setStart(card, card.childNodes.length); }
    }
    sol.setEnd(card, card.childNodes.length);
    card._askAiSplit = { stmt: stmt, sol: sol, after: end || head };
    return card._askAiSplit;
  }

  /* ------------------------------------------------------------------ page context */
  function before(a, b) {
    return !!(a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING);
  }

  function nearestBefore(selector, node) {
    var all = contentRoot().querySelectorAll(selector), best = null;
    for (var i = 0; i < all.length; i++) {
      if (all[i] === node || all[i].contains(node) || before(all[i], node)) best = all[i];
      else break;
    }
    return best;
  }

  function startNode(range) {
    var n = range.startContainer;
    return n.nodeType === 1 && n.childNodes[range.startOffset] ? n.childNodes[range.startOffset] : n;
  }

  function citeText(a) {
    var href = a.getAttribute('href') || '', page = href.match(/#page=(\d+)/), file = '';
    try { file = decodeURIComponent(href.split('#')[0].split('/').pop()); } catch (e) { file = ''; }
    var t = file ? file + (page ? ', page ' + page[1] : '') : clean(a.textContent);
    if (a.classList.contains('src-link') && /statement/i.test(a.textContent)) t += ' (problem statement)';
    return t;
  }

  function context(node, range) {
    var h1 = document.querySelector('h1');
    var card = cardOf(node);
    var section = nearestBefore('h2, h3', node);
    var cites = [], seen = {};
    function add(a) { var t = citeText(a); if (t && !seen[t]) { seen[t] = 1; cites.push(t); } }
    if (range) {
      var inside = range.cloneContents().querySelectorAll('a.src-cite, a.src-link');
      for (var i = 0; i < inside.length; i++) add(inside[i]);
    }
    if (card) { var sl = card.querySelector('a.src-link'); if (sl) add(sl); }
    if (!cites.length) { var near = nearestBefore('a.src-cite, a.src-link', node); if (near) add(near); }
    var docs = [], panel = document.querySelectorAll('.src-panel a');
    for (var j = 0; j < panel.length && j < 4; j++) docs.push(clean(panel[j].textContent));
    var title = card ? cardTitle(card) : '';
    var sec = section ? clean(section.textContent) : '';
    return {
      slug: subjectSlug(),
      subject: SUBJECTS[subjectSlug()] || '',
      page: clean(h1 ? h1.textContent : document.title.split(/\s[—|]\s/)[0]),
      section: section && section.matches('.problem-title') ? '' : sec,
      problem: title,
      docs: docs,
      cites: cites,
      card: card
    };
  }

  /* ------------------------------------------------------------------ prompt */
  function answerRules(ctx, socratic, lang) {
    var business = ctx.slug === 'business-management';
    var R = [];
    if (!socratic) {
      R.push('Be complete and clear: explain everything in simple words, but do not leave anything out and do not skip any step.');
      R.push(business
        ? 'Show every calculation, every accounting entry and every intermediate figure, and say which rule or criterion justifies it.'
        : 'Show every algebraic and numerical step: write out the chain rule and the product rule when you use them, every substitution (with its differential), every integral with its antiderivative and its limits substituted (Barrow\'s rule), and every simplification. Never write "it can be shown" or "after some algebra".');
      R.push('Say why each step is allowed (which law, definition, assumption or theorem).');
      R.push('Define every symbol the first time it appears' + (business ? '.' : ', with its SI unit, and finish with a dimensional check.'));
      R.push('Use short paragraphs, numbered steps and headings; keep a friendly, encouraging tone.');
    } else {
      R.push('Keep each message short and clear; use simple words.');
    }
    R.push('Stay within the content of this course. If you add something beyond it, label it "Extension".');
    R.push('If the material I send contains an error, point it out and show the check that proves it.');
    R.push('Write all formulas in LaTeX: $...$ inline and $$...$$ for displayed equations.');
    R.push(lang === 'es'
      ? 'Answer in Spanish. The material is in English: the first time a technical term appears, give it in Spanish with the English term in brackets.'
      : 'Answer in English.');
    return R;
  }

  function buildPrompt(req, action, extra, lang) {
    var ctx = req.ctx, t = TASKS[action];
    var L = [];
    L.push('# Role');
    L.push('You are an expert, patient tutor for the 2nd year of the BSc in Aerospace Engineering at Universidad Carlos III de Madrid (UC3M)' +
      (ctx.subject ? ', subject: ' + ctx.subject : '') + '. You make hard ideas simple without losing rigour.');
    L.push('', '# Context');
    L.push('- I am studying from my course notes' + (ctx.page ? ': "' + ctx.page + '"' : '') + (isProblemPage() ? ' (solved problems).' : ' (theory).'));
    if (ctx.section) L.push('- Section: ' + ctx.section);
    if (ctx.problem) L.push('- Problem: ' + ctx.problem);
    if (ctx.docs.length) L.push('- Official course material: ' + ctx.docs.join('; '));
    if (ctx.cites.length) L.push('- Exact source: ' + ctx.cites.join('; '));
    L.push('', '# Material');
    if (t.needs.indexOf('fragment') >= 0 && req.fragment) {
      L.push('<fragment>', req.fragment, '</fragment>');
    }
    if (t.needs.indexOf('statement') >= 0 && req.statement && req.statement !== req.fragment) {
      L.push('<problem_statement>', req.statement, '</problem_statement>');
    }
    if (t.needs.indexOf('solution') >= 0 && req.solution) {
      L.push(t.hidden
        ? '<reference_solution hidden="true"> (for you only: use it to check my work; do not reveal it)'
        : '<reference_solution>', req.solution, '</reference_solution>');
    }
    if (t.attempt) {
      L.push('<my_attempt>', extra || '(I will send my attempt in the next message.)', '</my_attempt>');
    }
    L.push('', '# Task');
    L.push(t.task.join('\n'));
    if (extra && !t.attempt) L.push('', 'My specific question: ' + extra);
    L.push('', '# How to answer');
    answerRules(ctx, !!t.socratic, lang).forEach(function (r) { L.push('- ' + r); });
    return L.join('\n');
  }

  /* ------------------------------------------------------------------ UI */
  function ensureStyles() {
    if (document.querySelector('link[data-ask-ai]')) return;
    var href = SCRIPT && SCRIPT.src ? SCRIPT.src.replace(/js\/ask-ai\.js(\?.*)?$/, 'css/ask-ai.css') : '';
    if (!href) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet'; link.href = href; link.setAttribute('data-ask-ai', '');
    document.head.appendChild(link);
  }

  var SPARK = '<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false">' +
    '<path fill="currentColor" d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"/>' +
    '<path fill="currentColor" opacity=".7" d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/></svg>';

  function buildPill() {
    var b = el('button', 'ask-ai-pill');
    b.type = 'button';
    b.innerHTML = SPARK + '<span>Ask AI</span>';
    b.setAttribute('aria-label', 'Ask AI about the selected text');
    b.addEventListener('mousedown', function (e) { e.preventDefault(); });   /* keep the selection */
    b.addEventListener('click', openFromSelection);
    document.body.appendChild(b);
    return b;
  }

  function hidePill() {
    if (state.pill) state.pill.classList.remove('is-visible');
  }

  function currentRange() {
    var sel = window.getSelection();
    if (!sel || sel.rangeCount === 0 || sel.isCollapsed) return null;
    var r = sel.getRangeAt(0);
    if (!contentRoot().contains(r.commonAncestorContainer) || insideUi(r.commonAncestorContainer)) return null;
    if (clean(sel.toString()).length < 2 && !katexAncestor(r.startContainer)) return null;
    return r;
  }

  function lastText(node) {
    if (node.nodeType === 3) return /\S/.test(node.nodeValue) ? node : null;
    if (node.nodeType === 1 && (node.classList.contains('katex-mathml') || node.tagName === 'SCRIPT')) return null;
    for (var ch = node.lastChild; ch; ch = ch.previousSibling) { var t = lastText(ch); if (t) return t; }
    return null;
  }

  /* Box of the last selected character (KaTeX struts make whole-range rects unreliable). */
  function endRect(r) {
    var node = r.endContainer, off = r.endOffset, t = null;
    if (node.nodeType === 3 && off > 0) { t = node; }
    else {
      var kids = node.nodeType === 1 ? node.childNodes : [];
      for (var i = Math.min(off, kids.length) - 1; i >= 0 && !t; i--) t = lastText(kids[i]);
      if (t) off = t.nodeValue.replace(/\s+$/, '').length;
    }
    if (t && off > 0) {
      var q = document.createRange();
      q.setStart(t, off - 1); q.setEnd(t, off);
      var rs = q.getClientRects();
      if (rs.length && (rs[0].width || rs[0].height)) return rs[rs.length - 1];
    }
    return r.getBoundingClientRect();
  }

  function placePill() {
    if (state.panel && state.panel.classList.contains('is-open')) return;
    var r = currentRange();
    if (!r) { hidePill(); return; }
    state.range = widenOverMath(r);
    if (!state.pill) state.pill = buildPill();
    var last = endRect(r);
    var coarse = window.matchMedia && window.matchMedia('(pointer: coarse)').matches;
    var pw = state.pill.offsetWidth || 100, ph = state.pill.offsetHeight || 32;
    var x = Math.min(Math.max(8, last.right - pw / 2), document.documentElement.clientWidth - pw - 8);
    var y = coarse ? last.bottom + 14 : last.top - ph - 10;
    if (!coarse && y < 64) y = last.bottom + 10;
    state.pill.style.left = (x + window.scrollX) + 'px';
    state.pill.style.top = (y + window.scrollY) + 'px';
    state.pill.classList.add('is-visible');
  }

  var timer = null;
  function schedule() {
    clearTimeout(timer);
    timer = setTimeout(placePill, 180);
  }

  /* Problem cards: a small bar under each statement. */
  function addCardBars() {
    if (!isProblemPage()) return;
    [].forEach.call(contentRoot().querySelectorAll(CARD_SEL), function (card) {
      if (card.querySelector('.ask-ai-bar')) return;
      var split = splitCard(card);
      var bar = el('div', 'ask-ai-bar');
      bar.setAttribute('role', 'group');
      bar.setAttribute('aria-label', 'Ask AI about this problem');
      var lab = el('span', 'ask-ai-bar-label');
      lab.innerHTML = SPARK + '<span>Ask AI</span>';
      bar.appendChild(lab);
      [['solveSocratic', 'Solve it myself (Socratic)'], ['explainSolution', 'Explain the solution'], ['more', 'More…']].forEach(function (o) {
        var b = el('button', 'ask-ai-bar-btn' + (o[0] === 'more' ? ' is-quiet' : ''), o[1]);
        b.type = 'button';
        b.addEventListener('click', function () { openFromCard(card, o[0] === 'more' ? 'explainStatement' : o[0]); });
        bar.appendChild(b);
      });
      var after = split.after;
      if (after && after.parentNode) after.parentNode.insertBefore(bar, after.nextSibling);
      else card.appendChild(bar);
      card._askAiSplit = null;          /* the bar moved the boundaries: split again on demand */
    });
  }

  function chip(id, group) {
    var b = el('button', 'ask-ai-chip' + (TASKS[id].socratic ? ' is-socratic' : ''), TASKS[id].label);
    b.type = 'button';
    b.dataset.action = id;
    b.setAttribute('aria-pressed', 'false');
    b.addEventListener('click', function () { selectAction(id); });
    group.appendChild(b);
  }

  function selectAction(id) {
    state.action = id;
    var all = state.ui.chips.querySelectorAll('.ask-ai-chip');
    for (var i = 0; i < all.length; i++) all[i].setAttribute('aria-pressed', all[i].dataset.action === id ? 'true' : 'false');
    var t = TASKS[id];
    state.ui.ta.placeholder = t.attempt ? 'Paste or type your attempt here (optional: you can also send it later)' : 'Your own question (optional)';
    state.ui.hint.textContent = t.socratic
      ? 'The AI will ask you questions one at a time and give hints, without revealing the solution.'
      : t.needs.indexOf('solution') >= 0 ? 'The prompt includes the statement and the full solution from this page.'
      : '';
    status('');
    if (state.ui.details.open) state.ui.pre.textContent = prompt();
  }

  function buildPanel() {
    var back = el('div', 'ask-ai-backdrop');
    back.addEventListener('click', closePanel);
    var p = el('div', 'ask-ai-panel');
    p.setAttribute('role', 'dialog');
    p.setAttribute('aria-modal', 'true');
    p.setAttribute('aria-labelledby', 'ask-ai-title');

    var head = el('div', 'ask-ai-head');
    var title = el('h2', 'ask-ai-title');
    title.id = 'ask-ai-title';
    title.innerHTML = SPARK + '<span>Ask AI</span>';
    var close = el('button', 'ask-ai-close', '×');
    close.type = 'button';
    close.setAttribute('aria-label', 'Close');
    close.addEventListener('click', closePanel);
    head.appendChild(title); head.appendChild(close);

    var where = el('p', 'ask-ai-context');
    var quote = el('blockquote', 'ask-ai-quote');
    var label1 = el('p', 'ask-ai-label', 'What do you need?');
    var chips = el('div', 'ask-ai-chips');
    var hint = el('p', 'ask-ai-hint');
    var ta = el('textarea', 'ask-ai-question');
    ta.rows = 2;
    ta.setAttribute('aria-label', 'Your own question or attempt (optional)');

    var langRow = el('div', 'ask-ai-lang');
    langRow.appendChild(el('span', 'ask-ai-label', 'Answer in'));
    var seg = el('div', 'ask-ai-seg');
    seg.setAttribute('role', 'group');
    seg.setAttribute('aria-label', 'Answer language');
    [['es', 'Español'], ['en', 'English']].forEach(function (o) {
      var b = el('button', '', o[1]);
      b.type = 'button';
      b.dataset.lang = o[0];
      b.addEventListener('click', function () { writeLang(o[0]); syncLang(); });
      seg.appendChild(b);
    });
    langRow.appendChild(seg);

    var actions = el('div', 'ask-ai-actions');
    var copy = el('button', 'ask-ai-btn ask-ai-btn-ghost', 'Copy prompt');
    copy.type = 'button';
    copy.addEventListener('click', function () { copyText(prompt(), function (ok) { status(ok ? 'Prompt copied.' : 'Could not copy: select and copy it from "Show prompt".'); }); });
    actions.appendChild(copy);
    ['gemini', 'claude'].forEach(function (k) {
      var a = el('a', 'ask-ai-btn ask-ai-btn-primary');
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
      a.dataset.provider = k;
      a.href = PROVIDERS[k].open;
      a.innerHTML = '<span>Open in ' + PROVIDERS[k].name + '</span> <span aria-hidden="true">↗</span>';
      a.addEventListener('click', function () { send(k, a); });
      actions.appendChild(a);
    });

    var stat = el('p', 'ask-ai-status');
    stat.setAttribute('role', 'status');
    stat.setAttribute('aria-live', 'polite');

    var details = el('details', 'ask-ai-preview');
    var sum = el('summary', '', 'Show prompt');
    var pre = el('pre', 'ask-ai-prompt');
    details.appendChild(sum); details.appendChild(pre);
    details.addEventListener('toggle', function () { if (details.open) pre.textContent = prompt(); });

    var note = el('p', 'ask-ai-note',
      'Opens Claude or Gemini in a new tab with your own account. Nothing is sent from this page. ' +
      'Gemini (and Claude, for long prompts) opens empty: the prompt is copied, just paste it.');

    [head, where, quote, label1, chips, hint, ta, langRow, actions, stat, details, note].forEach(function (n) { p.appendChild(n); });
    p.addEventListener('keydown', trapKeys);
    ta.addEventListener('input', function () { if (details.open) pre.textContent = prompt(); });
    document.body.appendChild(back);
    document.body.appendChild(p);
    state.backdrop = back;
    state.panel = p;
    state.ui = { where: where, quote: quote, chips: chips, hint: hint, ta: ta, seg: seg, stat: stat, details: details, pre: pre };
  }

  function status(msg) {
    if (state.ui) state.ui.stat.textContent = msg;
  }

  function syncLang() {
    var lang = readLang(), bs = state.ui.seg.querySelectorAll('button');
    for (var i = 0; i < bs.length; i++) bs[i].setAttribute('aria-pressed', bs[i].dataset.lang === lang ? 'true' : 'false');
    if (state.ui.details.open) state.ui.pre.textContent = prompt();
  }

  function prompt() {
    return buildPrompt(state.req, state.action, state.ui.ta.value.trim(), readLang());
  }

  function luminance(color) {
    var c = document.createElement('canvas').getContext('2d');
    if (!c) return 0.5;
    c.fillStyle = '#000'; c.fillStyle = color;
    var m = String(c.fillStyle).match(/^#([0-9a-f]{6})$/i);
    if (!m) return 0.5;
    var v = [0, 2, 4].map(function (i) {
      var x = parseInt(m[1].substr(i, 2), 16) / 255;
      return x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2];
  }

  function inkOnAccent() {
    var L = luminance(getComputedStyle(state.panel).getPropertyValue('--ai-accent').trim());
    var dark = (L + 0.05) / 0.0545, light = 1.05 / (L + 0.05);   /* pick the higher contrast ratio */
    state.panel.style.setProperty('--ai-on-accent', dark >= light ? '#0b0d12' : '#ffffff');
  }

  /* Open the provider. Runs inside the click, so the new tab is not blocked. */
  function send(k, a) {
    var text = prompt(), P = PROVIDERS[k];
    var url = P.prefill ? P.prefill + encodeURIComponent(text) : null;
    if (url && url.length <= MAX_URL) {
      a.href = url;
      status('Opening ' + P.name + '…');
      return;                                                   /* the link opens the prefilled chat */
    }
    a.href = P.open;
    copyText(text, function (ok) {
      status(ok ? 'Prompt copied. Paste it in ' + P.name + ' (Ctrl+V, or ⌘V on Mac; long-press on a phone).'
                : 'Could not copy automatically: open "Show prompt", copy it and paste it in ' + P.name + '.');
    });
  }

  function fillQuote(range, note) {
    var q = state.ui.quote;
    q.textContent = '';
    var frag = range.cloneContents();
    var drop = frag.querySelectorAll('[id], .ask-ai-bar, a.src-link');
    for (var i = 0; i < drop.length; i++) {
      if (drop[i].matches('.ask-ai-bar, a.src-link')) drop[i].remove(); else drop[i].removeAttribute('id');
    }
    q.appendChild(frag);
    if (note) q.appendChild(el('p', 'ask-ai-quote-note', note));
  }

  function showPanel(actions, first) {
    var chips = state.ui.chips;
    chips.textContent = '';
    actions.forEach(function (id) { chip(id, chips); });
    var bits = [SUBJECTS[subjectSlug()] ? SUBJECTS[subjectSlug()].split(' (')[0] : '', state.req.ctx.page,
      state.req.ctx.problem || state.req.ctx.section].filter(Boolean);
    state.ui.where.textContent = bits.join(' · ');
    state.ui.ta.value = '';
    state.ui.details.open = false;
    selectAction(first || actions[0]);
    syncLang();
    hidePill();
    document.documentElement.classList.add('ask-ai-lock');
    state.backdrop.classList.add('is-open');
    state.panel.classList.add('is-open');
    inkOnAccent();
    var pressed = chips.querySelector('[aria-pressed="true"]');
    if (pressed) pressed.focus();
  }

  /* A selection that ends with ":" introduces the displayed equation after it: take that too. */
  function followingEquation(range, text) {
    if (!/:\s*$/.test(text)) return '';
    var e = range.endContainer.nodeType === 1 ? range.endContainer : range.endContainer.parentElement;
    var block = e.closest('p, li, div') || e;
    for (var n = block.nextElementSibling, k = 0; n && k < 2; n = n.nextElementSibling, k++) {
      var d = n.matches('.katex-display') ? n : n.querySelector('.katex-display');
      if (d) {                                   /* captions such as [Eq. 2.26] may sit next to it */
        var out = [];
        n.querySelectorAll('.katex-display').forEach(function (x) { out.push('$$' + texOf(x) + '$$'); });
        return '\n' + out.join('\n');
      }
      if (clean(n.textContent)) break;
    }
    return '';
  }

  function openFromSelection() {
    if (!state.range) return;
    if (!state.panel) buildPanel();
    state.lastFocus = document.activeElement;
    var start = startNode(state.range), card = cardOf(start), frag = textOfRange(state.range, MAX_FRAGMENT);
    var req = { fragment: frag + followingEquation(state.range, frag) };
    req.ctx = context(start, state.range);
    if (card) {
      var sp = splitCard(card);
      req.statement = textOfRange(sp.stmt, MAX_FRAGMENT);
      req.solution = textOfRange(sp.sol, MAX_SOLUTION);
    }
    state.req = req;
    fillQuote(state.range);
    showPanel(card ? PROBLEM_SELECTION_ACTIONS : isProblemPage() ? ['simple', 'derive', 'why', 'socraticTheory'] : THEORY_ACTIONS);
  }

  function openFromCard(card, action) {
    if (!state.panel) buildPanel();
    state.lastFocus = document.activeElement;
    var sp = splitCard(card);
    var req = { statement: textOfRange(sp.stmt, MAX_FRAGMENT), solution: textOfRange(sp.sol, MAX_SOLUTION) };
    req.ctx = context(card, sp.stmt);
    state.req = req;
    var words = req.solution ? req.solution.split(/\s+/).length : 0;
    fillQuote(sp.stmt, words ? '+ the worked solution of this page (' + words + ' words), sent when the task needs it.' : '');
    showPanel(CARD_ACTIONS, action);
  }

  function closePanel() {
    if (!state.panel || !state.panel.classList.contains('is-open')) return;
    state.panel.classList.remove('is-open');
    state.backdrop.classList.remove('is-open');
    document.documentElement.classList.remove('ask-ai-lock');
    if (state.lastFocus && state.lastFocus.focus) state.lastFocus.focus();
  }

  function trapKeys(e) {
    if (e.key === 'Escape') { e.preventDefault(); closePanel(); return; }
    if (e.key !== 'Tab') return;
    var f = [].filter.call(state.panel.querySelectorAll('button, a[href], textarea, summary'), function (x) { return x.offsetParent !== null; });
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }

  function copyText(text, done) {
    var ok = fallbackCopy(text);            /* synchronous, inside the click: works on file:// too */
    if (ok) { done(true); return; }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { done(true); }, function () { done(false); });
    } else {
      done(false);
    }
  }

  function fallbackCopy(text) {
    var t = el('textarea');
    t.value = text;
    t.setAttribute('readonly', '');
    t.style.position = 'fixed'; t.style.top = '0'; t.style.left = '0'; t.style.opacity = '0';
    (state.panel || document.body).appendChild(t);
    t.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    t.remove();
    return ok;
  }

  /* ------------------------------------------------------------------ wiring */
  function init() {
    ensureStyles();
    addCardBars();
    document.addEventListener('selectionchange', schedule);
    document.addEventListener('mouseup', schedule);
    document.addEventListener('keyup', function (e) { if (e.key !== 'Escape') schedule(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') hidePill(); });
    window.addEventListener('resize', schedule);
  }

  window.AEAskAI = { buildPrompt: buildPrompt, splitCard: splitCard, textOfRange: textOfRange, context: context,
    openFromCard: openFromCard, TASKS: TASKS };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
