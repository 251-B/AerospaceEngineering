/*!
 * Aerospace Engineering Study Portal: "Ask Claude" on selected text.
 *
 * Load once per theory or problem page, after theme.js:
 *     <script defer src="../../../assets/js/ask-claude.js"></script>
 * The script adds its own stylesheet (assets/css/ask-claude.css, found next to this file).
 *
 * Select a sentence, a formula or a step and an "Ask Claude" pill appears next to it. The panel
 * builds a prompt with the fragment (formulas as their LaTeX source, read from KaTeX), the
 * subject, page, section and nearest citation of the official material, then opens
 * claude.ai/new?q=... in a new tab. Each student uses their own claude.ai account; this page
 * sends nothing anywhere. "Copy prompt" is the fallback when the prefill does not arrive.
 *
 * Storage: 'ae_ask_lang' ('es' | 'en'), the language Claude is asked to answer in.
 */
(function () {
  'use strict';

  var SCRIPT = document.currentScript;
  var LANG_KEY = 'ae_ask_lang';
  var MAX_FRAGMENT = 3500;
  var CLAUDE_URL = 'https://claude.ai/new?q=';

  var SUBJECTS = {
    'fluid-mechanics': 'Fluid Mechanics',
    'aerospace-materials-1': 'Aerospace Materials I',
    'engineering-mechanics': 'Engineering Mechanics',
    'advanced-maths': 'Advanced Mathematics',
    'business-management': 'Business Management'
  };

  var THEORY_ACTIONS = [
    { id: 'simple', label: 'Explain simply',
      task: 'Explain this fragment in simple terms, as to a classmate who sees it for the first time. Say what every symbol means.' },
    { id: 'steps', label: 'Step by step',
      task: 'Go through it step by step with no algebraic jumps: show every derivative, substitution and simplification, and say why each step is allowed.' },
    { id: 'why', label: 'Why does it hold?',
      task: 'Explain where it comes from and why it holds: the physical idea behind it, its assumptions and when it stops being valid.' },
    { id: 'example', label: 'Worked example',
      task: 'Give me a short worked numerical example that uses it, in SI units, with a dimensional check.' },
    { id: 'quiz', label: 'Quiz me',
      task: 'Ask me 3 short questions, one at a time, to check that I understand it. Wait for each answer before correcting it.' }
  ];

  var PROBLEM_ACTIONS = [
    { id: 'step', label: 'Explain this step',
      task: 'Explain this step of the solution: what is done, why it is allowed and where each number comes from. Show any algebra that is skipped.' },
    { id: 'method', label: 'Why this method?',
      task: 'Explain why this equation or method is the right one here, what the alternatives would be and why they do not fit.' },
    { id: 'concept', label: 'Underlying theory',
      task: 'Explain the theory this relies on, in simple terms, with every symbol defined.' },
    { id: 'similar', label: 'Similar exercise',
      task: 'Write a similar exercise with different numbers for me to practise. Do not give the solution until I ask for it.' },
    { id: 'check', label: 'Check my reasoning',
      task: 'I will tell you how I would solve it. Check my reasoning and point out any mistake, without giving the full answer straight away.' }
  ];

  var state = { pill: null, panel: null, backdrop: null, range: null, action: null, lastFocus: null };

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

  function contentRoot() {
    return document.querySelector('main') || document.body;
  }

  function isProblemPage() {
    return /\/problemas\//.test(location.pathname);
  }

  function subjectName() {
    var m = location.pathname.match(/\/subjects\/([^/]+)\//);
    return m && SUBJECTS[m[1]] ? SUBJECTS[m[1]] : '';
  }

  function insideUi(node) {
    var e = node && (node.nodeType === 1 ? node : node.parentElement);
    return !!(e && e.closest('.ask-claude-pill, .ask-claude-panel, input, textarea, header.site-header, .site-header'));
  }

  /* ------------------------------------------------------------------ selection -> text with LaTeX */
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
      var c = node.classList;
      if (c.contains('katex-display')) { out.push('\n$$' + texOf(node) + '$$\n'); return; }
      if (c.contains('katex')) { out.push('$' + texOf(node) + '$'); return; }
      if (c.contains('katex-mathml') || node.tagName === 'SCRIPT' || node.tagName === 'STYLE' || node.tagName === 'svg') return;
      if (node.tagName === 'BR') { out.push('\n'); return; }
      if (node.tagName === 'TD' || node.tagName === 'TH') { out.push(' | '); }
      if (node.tagName === 'LI') out.push('\n- ');
    }
    for (var ch = node.firstChild; ch; ch = ch.nextSibling) serialize(ch, out);
    if (node.nodeType === 1 && BLOCK.test(node.tagName)) out.push('\n');
  }

  function fragmentText(range) {
    var out = [];
    serialize(range.cloneContents(), out);
    var s = out.join('').replace(/[ \t]+\n/g, '\n').replace(/\n[ \t]+/g, '\n').replace(/\n{3,}/g, '\n\n').replace(/ {2,}/g, ' ').trim();
    if (s.length > MAX_FRAGMENT) s = s.slice(0, MAX_FRAGMENT) + ' […]';
    return s;
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

  function context(range) {
    var start = startNode(range);
    var h1 = document.querySelector('h1');
    var section = nearestBefore('h2, h3', start);
    var card = (start.nodeType === 1 ? start : start.parentElement).closest('.problem-card, .problem-box');
    var cardTitle = card ? card.querySelector('h2, h3, h4, .problem-title') : null;
    var cites = [], seen = {};
    function addCite(a) {
      var href = a.getAttribute('href') || '', page = href.match(/#page=(\d+)/);
      var file = '';
      try { file = decodeURIComponent(href.split('#')[0].split('/').pop()); } catch (e) { file = ''; }
      var t = file ? file + (page ? ', page ' + page[1] : '') : clean(a.textContent);
      if (a.classList.contains('src-link') && /statement/i.test(a.textContent)) t += ' (problem statement)';
      if (t && !seen[t]) { seen[t] = 1; cites.push(t); }
    }
    var inside = range.cloneContents().querySelectorAll('a.src-cite, a.src-link');
    for (var i = 0; i < inside.length; i++) addCite(inside[i]);
    if (!cites.length) {
      var near = card ? card.querySelector('a.src-link') : nearestBefore('a.src-cite, a.src-link', start);
      if (near) addCite(near);
    }
    var docs = [];
    var panel = document.querySelectorAll('.src-panel a');
    for (var j = 0; j < panel.length && j < 4; j++) docs.push(clean(panel[j].textContent));
    var title = clean(h1 ? h1.textContent : document.title.split(/\s[—|-]\s/)[0]);
    return {
      subject: subjectName(),
      page: title,
      section: section ? clean(section.textContent) : '',
      problem: cardTitle && cardTitle !== section ? clean(cardTitle.textContent) : '',
      docs: docs,
      cites: cites
    };
  }

  function buildPrompt(text, ctx, action, question, lang) {
    var L = [];
    L.push('I am a 2nd-year Aerospace Engineering student at UC3M' + (ctx.subject ? ', studying ' + ctx.subject : '') + '.');
    if (ctx.page) L.push('Page: ' + ctx.page + (isProblemPage() ? ' (solved problems)' : ' (theory notes)'));
    if (ctx.section) L.push('Section: ' + ctx.section);
    if (ctx.problem) L.push('Problem: ' + ctx.problem);
    if (ctx.docs.length) L.push('Official course material: ' + ctx.docs.join('; '));
    if (ctx.cites.length) L.push('Source of this fragment: ' + ctx.cites.join('; '));
    L.push('', 'Fragment from my notes (formulas in LaTeX):', '"""', text, '"""', '');
    if (action) L.push(action.task);
    if (question) L.push((action ? 'Also: ' : '') + question);
    L.push('', 'Stay within what this course covers and say clearly when you go beyond it. Use SI units and write formulas in LaTeX.');
    L.push(lang === 'es' ? 'Answer in Spanish, keeping the technical terms in English in brackets the first time they appear.' : 'Answer in English.');
    return L.join('\n');
  }

  /* ------------------------------------------------------------------ UI */
  function ensureStyles() {
    if (document.querySelector('link[data-ask-claude]')) return;
    var href = SCRIPT && SCRIPT.src ? SCRIPT.src.replace(/js\/ask-claude\.js(\?.*)?$/, 'css/ask-claude.css') : '';
    if (!href) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet'; link.href = href; link.setAttribute('data-ask-claude', '');
    document.head.appendChild(link);
  }

  var SPARK = '<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false">' +
    '<path fill="currentColor" d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"/>' +
    '<path fill="currentColor" opacity=".7" d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/></svg>';

  function buildPill() {
    var b = el('button', 'ask-claude-pill');
    b.type = 'button';
    b.innerHTML = SPARK + '<span>Ask Claude</span>';
    b.setAttribute('aria-label', 'Ask Claude about the selected text');
    b.addEventListener('mousedown', function (e) { e.preventDefault(); });   /* keep the selection */
    b.addEventListener('click', openPanel);
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

  function placePill() {
    if (state.panel && state.panel.classList.contains('is-open')) return;
    var r = currentRange();
    if (!r) { hidePill(); return; }
    state.range = widenOverMath(r);
    if (!state.pill) state.pill = buildPill();
    var last = endRect(r);
    var coarse = window.matchMedia && window.matchMedia('(pointer: coarse)').matches;
    var pw = state.pill.offsetWidth || 120, ph = state.pill.offsetHeight || 32;
    var x = Math.min(Math.max(8, last.right - pw / 2), document.documentElement.clientWidth - pw - 8);
    var y = coarse ? last.bottom + 14 : last.top - ph - 10;
    if (!coarse && y < 64) y = last.bottom + 10;
    state.pill.style.left = (x + window.scrollX) + 'px';
    state.pill.style.top = (y + window.scrollY) + 'px';
    state.pill.classList.add('is-visible');
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

  var timer = null;
  function schedule() {
    clearTimeout(timer);
    timer = setTimeout(placePill, 180);
  }

  function chip(action, group) {
    var b = el('button', 'ask-claude-chip', action.label);
    b.type = 'button';
    b.setAttribute('aria-pressed', 'false');
    b.addEventListener('click', function () {
      var on = state.action !== action;
      state.action = on ? action : null;
      var all = group.querySelectorAll('.ask-claude-chip');
      for (var i = 0; i < all.length; i++) all[i].setAttribute('aria-pressed', 'false');
      if (on) b.setAttribute('aria-pressed', 'true');
      refresh();
    });
    return b;
  }

  function buildPanel() {
    var back = el('div', 'ask-claude-backdrop');
    back.addEventListener('click', closePanel);
    var p = el('div', 'ask-claude-panel');
    p.setAttribute('role', 'dialog');
    p.setAttribute('aria-modal', 'true');
    p.setAttribute('aria-labelledby', 'ask-claude-title');

    var head = el('div', 'ask-claude-head');
    var title = el('h2', 'ask-claude-title');
    title.id = 'ask-claude-title';
    title.innerHTML = SPARK + '<span>Ask Claude</span>';
    var close = el('button', 'ask-claude-close', '×');
    close.type = 'button';
    close.setAttribute('aria-label', 'Close');
    close.addEventListener('click', closePanel);
    head.appendChild(title); head.appendChild(close);

    var where = el('p', 'ask-claude-context');
    var quote = el('blockquote', 'ask-claude-quote');
    var label1 = el('p', 'ask-claude-label', 'What do you need?');
    var chips = el('div', 'ask-claude-chips');
    (isProblemPage() ? PROBLEM_ACTIONS : THEORY_ACTIONS).forEach(function (a) { chips.appendChild(chip(a, chips)); });
    var ta = el('textarea', 'ask-claude-question');
    ta.rows = 2;
    ta.placeholder = 'Your own question (optional)';
    ta.setAttribute('aria-label', 'Your own question (optional)');
    ta.addEventListener('input', refresh);

    var langRow = el('div', 'ask-claude-lang');
    langRow.appendChild(el('span', 'ask-claude-label', 'Answer in'));
    var seg = el('div', 'ask-claude-seg');
    seg.setAttribute('role', 'group');
    seg.setAttribute('aria-label', 'Answer language');
    [['es', 'Español'], ['en', 'English']].forEach(function (o) {
      var b = el('button', '', o[1]);
      b.type = 'button';
      b.dataset.lang = o[0];
      b.addEventListener('click', function () { writeLang(o[0]); syncLang(); refresh(); });
      seg.appendChild(b);
    });
    langRow.appendChild(seg);

    var actions = el('div', 'ask-claude-actions');
    var copy = el('button', 'ask-claude-btn ask-claude-btn-ghost', 'Copy prompt');
    copy.type = 'button';
    copy.addEventListener('click', copyPrompt);
    var go = el('a', 'ask-claude-btn ask-claude-btn-primary');
    go.target = '_blank';
    go.rel = 'noopener noreferrer';
    go.innerHTML = '<span>Open in Claude</span> <span aria-hidden="true">↗</span>';
    go.addEventListener('click', function () { setTimeout(closePanel, 50); });
    actions.appendChild(copy); actions.appendChild(go);

    var note = el('p', 'ask-claude-note',
      'Opens claude.ai in a new tab with your own account. Nothing is sent from this page.');

    [head, where, quote, label1, chips, ta, langRow, actions, note].forEach(function (n) { p.appendChild(n); });
    p.addEventListener('keydown', trapKeys);
    document.body.appendChild(back);
    document.body.appendChild(p);
    state.backdrop = back;
    state.panel = p;
    state.ui = { where: where, quote: quote, chips: chips, ta: ta, seg: seg, go: go, copy: copy };
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
    var accent = getComputedStyle(state.panel).getPropertyValue('--ac-accent').trim();
    var L = luminance(accent);
    /* pick the text colour with the higher contrast ratio against the accent */
    var dark = (L + 0.05) / 0.0545, light = 1.05 / (L + 0.05);
    state.panel.style.setProperty('--ac-on-accent', dark >= light ? '#0b0d12' : '#ffffff');
  }

  function syncLang() {
    var lang = readLang(), bs = state.ui.seg.querySelectorAll('button');
    for (var i = 0; i < bs.length; i++) bs[i].setAttribute('aria-pressed', bs[i].dataset.lang === lang ? 'true' : 'false');
  }

  function prompt() {
    return buildPrompt(state.text, state.ctx, state.action, clean(state.ui.ta.value), readLang());
  }

  function refresh() {
    state.ui.go.href = CLAUDE_URL + encodeURIComponent(prompt());
  }

  function openPanel() {
    if (!state.range) return;
    if (!state.panel) buildPanel();
    state.lastFocus = document.activeElement;
    state.text = fragmentText(state.range);
    state.ctx = context(state.range);
    var bits = [state.ctx.subject, state.ctx.page, state.ctx.problem || state.ctx.section].filter(Boolean);
    state.ui.where.textContent = bits.join(' · ');
    state.ui.quote.textContent = '';
    var frag = state.range.cloneContents();
    var ids = frag.querySelectorAll('[id]');
    for (var i = 0; i < ids.length; i++) ids[i].removeAttribute('id');
    state.ui.quote.appendChild(frag);
    state.action = null;
    var cs = state.ui.chips.querySelectorAll('.ask-claude-chip');
    for (var j = 0; j < cs.length; j++) cs[j].setAttribute('aria-pressed', 'false');
    cs[0].click();
    state.ui.ta.value = '';
    state.ui.copy.textContent = 'Copy prompt';
    syncLang();
    inkOnAccent();
    refresh();
    hidePill();
    document.documentElement.classList.add('ask-claude-lock');
    state.backdrop.classList.add('is-open');
    state.panel.classList.add('is-open');
    cs[0].focus();
  }

  function closePanel() {
    if (!state.panel || !state.panel.classList.contains('is-open')) return;
    state.panel.classList.remove('is-open');
    state.backdrop.classList.remove('is-open');
    document.documentElement.classList.remove('ask-claude-lock');
    if (state.lastFocus && state.lastFocus.focus) state.lastFocus.focus();
  }

  function trapKeys(e) {
    if (e.key === 'Escape') { e.preventDefault(); closePanel(); return; }
    if (e.key !== 'Tab') return;
    var f = state.panel.querySelectorAll('button, a[href], textarea');
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }

  function copyPrompt() {
    var text = prompt(), btn = state.ui.copy;
    function done(ok) { btn.textContent = ok ? 'Copied ✓' : 'Copy failed'; }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { done(true); }, function () { done(fallbackCopy(text)); });
    } else {
      done(fallbackCopy(text));
    }
  }

  function fallbackCopy(text) {
    var t = el('textarea');
    t.value = text;
    t.setAttribute('readonly', '');
    t.style.position = 'fixed'; t.style.opacity = '0';
    document.body.appendChild(t);
    t.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(t);
    return ok;
  }

  /* ------------------------------------------------------------------ wiring */
  function init() {
    ensureStyles();
    document.addEventListener('selectionchange', schedule);
    document.addEventListener('mouseup', schedule);
    document.addEventListener('keyup', function (e) { if (e.key !== 'Escape') schedule(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') hidePill(); });
    window.addEventListener('resize', schedule);
  }

  window.AEAskClaude = { buildPrompt: buildPrompt, fragmentText: fragmentText, context: context, open: openPanel };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
