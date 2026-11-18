/*!
 * Aerospace Engineering Study Portal: theory reader (section rail, wide view, quieter text).
 *
 * Loaded on every page by assets/js/theme.js (no page carries its own <script> tag for it); it acts
 * only on theory topic pages (teoria/topic-*.html, not the index) and is skipped in the PDF print
 * mode (?print=...). Its styles are assets/css/theory-reader.css, linked by this script. Everything it
 * changes is screen-only: the browser's own print and the PDFs show the page as written.
 *
 *  - Section rail: a column of short bars at the right edge of the window, one per h2 (longer bar)
 *    and per h3 (shorter bar, only while the page has at most MAX_MARKS headings in all). A bar is a
 *    button: clicking it jumps to that heading; hovering or focusing it shows the heading's title.
 *    The bar of the section in view is marked (aria-current), the ones above it count as read.
 *  - Wide view: the article column of the page grows to the width of the window (html.tr-wide).
 *  - Quieter text: citations of the official material inside a heading ("[Session 21 Slides 3-4]")
 *    are hidden on screen (the "Official material" strip and the in-text citations still link the
 *    PDFs); citations in running text are set smaller in the secondary text colour; a figure caption
 *    keeps its first sentence, and the rest (long explanations, "Copied from Slide 3") folds behind a
 *    "More" button; a paragraph that only says how the page follows the official material ("This page
 *    follows ...") folds behind "About this page".
 *  - Sections, derivations and progress: every h2 section folds to its title ("Open all / Fold all"),
 *    derivation boxes show their result until "Show derivation", a pill above the rail gives the
 *    section in view and the minutes left; the arrow keys move between sections.
 *  - Reading modes: pages with summary boxes (> [!summary] in the vault note, .essential-box) get an
 *    Essential / Full switch (Essential shows each section's summary and first figure only), stored
 *    under ae_theory_mode (try/catch: the page works without storage).
 * API: window.AETheoryReader = { init, sections }
 */
(function () {
  'use strict';

  if (window.AETheoryReader) return;
  if (/[?&]print=/.test(location.search)) return;
  if (!/\/teoria\/topic-[^\/]+\.html$/.test(location.pathname)) {
    window.AETheoryReader = { init: function () {}, sections: function () { return []; } };
    return;
  }

  var MAX_MARKS = 60;          // above this, the rail lists the h2 headings only
  var MIN_MARKS = 3;           // a page with fewer headings gets no rail
  var CAPTION_KEEP = 140;      // a caption longer than this folds after its first sentence
  var SKIP = '.toc-card, .src-panel, .ae-nav, nav, aside, .exam-box, .derivation-box, .callout, ' +
    '[class*="ask-ai"], [class*="upd-"], [class*="fl-"], [class*="pm-"], [class*="surface-"], .tr-rail';
  var SOURCE_RE = /(,\s*)?\b([Cc]opied from|[Rr]edrawn (from|after)|[Aa]dapted from|[Rr]eproduced from|[Tt]aken from|Sources?: |Session \d+, Slides? [\d\u2013-]+\.*\s*$)/;
  var META_RE = /^This (page|note) (follows|reproduces|transcribes|is built)/;
  var META_TITLE_RE = /^(Erratum|Errata|Note on the official material|Spellings? of the slides?|Printed (words|on|ions)|(Two )?typing slips? in|Topic number printed|Rounding on the slide|Two [\w\s$\\{}_]+ on Slide|.*the slides disagree)/i;
  var CITE_START_RE = /\[[^\[\]]*$/;
  var marks = [];

  function linkStyles() {
    var self = document.querySelector('script[src*="theory-reader.js"]');
    if (!self || document.querySelector('link[href*="theory-reader.css"]')) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = self.src.replace(/js\/theory-reader\.js(\?.*)?$/, 'css/theory-reader.css');
    document.head.appendChild(link);
  }

  /* -------------------------------------------------------------- headings */
  function headingText(h) {
    var clone = h.cloneNode(true);
    [].forEach.call(clone.querySelectorAll('.katex-mathml, .tr-cite, .src-cite, .section-number, .section-tag, .anchor, .ae-ask'), function (n) {
      n.remove();
    });
    return clone.textContent.replace(/\[[^\]]*\]/g, '').replace(/^\s*(§\s*)?\d+(\.\d+)*\s*[.)\-–—:]?\s*/, '')
      .replace(/\s+/g, ' ').trim();
  }

  function slug(text) {
    return 'sec-' + text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 40);
  }

  function collect(scope) {
    var all = [].filter.call(scope.querySelectorAll('h2, h3'), function (h) {
      return !h.closest(SKIP) && headingText(h);
    });
    var h2 = all.filter(function (h) { return h.tagName === 'H2'; });
    var list = all.length > MAX_MARKS || h2.length < 2 ? h2 : all;
    if (list.length < MIN_MARKS && all.length >= MIN_MARKS) list = all;
    var used = {};
    return list.map(function (h) {
      if (!h.id) {   // same scheme as the side menu, so both point to the same anchor
        var base = slug(headingText(h)), id = base, n = 2;
        while (used[id] || document.getElementById(id)) id = base + '-' + n++;
        h.id = id;
      }
      used[h.id] = true;
      return { id: h.id, text: headingText(h), level: h.tagName === 'H2' ? 2 : 3, target: h };
    });
  }

  /* ------------------------------------------------------------- citations */
  /* Wraps "[Session 21 Slides <a>3</a>-<a>4</a>]" (brackets in the text nodes around one or more
     .src-cite links) in <span class="tr-cite">. Only when both brackets share the links' parent. */
  function wrapCitations(scope) {
    [].forEach.call(scope.querySelectorAll('span.cite'), function (span) {   // pages that mark them already
      if (/^\s*\[/.test(span.textContent)) span.classList.add('tr-cite');
    });
    [].forEach.call(scope.querySelectorAll('.src-cite'), function (a) {
      if (a.closest('.tr-cite')) return;
      var prev = a.previousSibling;
      while (prev && prev.nodeType !== 3) {
        if (prev.nodeType === 1 && !prev.classList.contains('src-cite')) return;
        prev = prev.previousSibling;
      }
      if (!prev) return;
      var m = CITE_START_RE.exec(prev.nodeValue);
      if (!m) return;
      var next = a.nextSibling;
      while (next && !(next.nodeType === 3 && next.nodeValue.indexOf(']') >= 0)) {
        if (next.nodeType === 1 && !next.classList.contains('src-cite')) return;
        if (next.nodeType === 3 && next.nodeValue.indexOf('[') >= 0) return;
        next = next.nextSibling;
      }
      if (!next) return;
      var startNode = prev.splitText(m.index);
      next.splitText(next.nodeValue.indexOf(']') + 1);
      var span = document.createElement('span');
      span.className = 'tr-cite';
      a.parentNode.insertBefore(span, startNode);
      var node = startNode;
      while (node) {
        var after = node.nextSibling;
        span.appendChild(node);
        if (node === next) break;
        node = after;
      }
      // the space before a hidden heading citation would trail the title
      var before = span.previousSibling;
      if (before && before.nodeType === 3) {
        var trimmed = before.nodeValue.replace(/\s+$/, '');
        if (trimmed !== before.nodeValue) {
          before.nodeValue = trimmed;
          span.insertBefore(document.createTextNode(' '), span.firstChild);
        }
      }
    });
  }

  /* ---------------------------------------------------------------- folds */
  var foldCount = 0;

  function makeFold(label, extraClass, tag) {
    var id = 'tr-fold-' + (++foldCount);
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'tr-more';
    button.setAttribute('aria-expanded', 'false');
    button.setAttribute('aria-controls', id);
    button.textContent = label;
    var body = document.createElement(tag || 'span');
    body.className = 'tr-fold' + (extraClass ? ' ' + extraClass : '');
    body.id = id;
    button.addEventListener('click', function () {
      var open = button.getAttribute('aria-expanded') !== 'true';
      button.setAttribute('aria-expanded', String(open));
      body.classList.toggle('tr-fold--open', open);
    });
    return { button: button, body: body };
  }

  /* Index (into the caption's text) of the end of its first sentence, outside formulas and links. */
  function firstSentenceEnd(text) {
    var re = /\.(?=\s+[A-Z(\[$])/g, m;
    while ((m = re.exec(text))) {
      var head = text.slice(0, m.index);
      if (/\b(Fig|Figs|Eq|Eqs|Sec|p|pp|e\.g|i\.e|vs|cf|approx|No|[A-Z])$/.test(head)) continue;
      // "Figure 3." or "Figure 1. Fig. 13.1." is a label, not a sentence
      if (/^Figure\s+[\dA-Z.\-]+(\.\s*Fig\.\s*[\d.()a-z]+)?$/i.test(head.trim())) continue;
      if ((head.match(/\$/g) || []).length % 2) continue;                       // inside a formula
      if ((head.match(/\(/g) || []).length !== (head.match(/\)/g) || []).length) continue;   // inside brackets
      return m.index + 1;
    }
    return -1;
  }

  /* Splits the caption's children at a text offset: everything after it goes into the fold. */
  function foldCaption(caption) {
    if (caption.querySelector('.tr-fold')) return;
    var text = caption.textContent;
    var sourceAt = text.search(SOURCE_RE);
    var cut = text.length > CAPTION_KEEP ? firstSentenceEnd(text) : -1;
    if (sourceAt > 0 && (cut < 0 || sourceAt < cut)) cut = sourceAt;
    if (cut <= 0 || text.slice(cut).trim().length < 12) return;

    // find the text node holding the offset; the cut never falls inside an element other than text
    var walker = document.createTreeWalker(caption, NodeFilter.SHOW_TEXT), node, seen = 0;
    while ((node = walker.nextNode())) {
      if (seen + node.nodeValue.length >= cut) break;
      seen += node.nodeValue.length;
    }
    if (!node || node.parentNode !== caption) return;   // inside a link or formula: leave it whole
    var rest = node.splitText(cut - seen);
    var fold = makeFold('More', 'tr-fold--caption');
    var item = rest;
    while (item) {
      var after = item.nextSibling;
      fold.body.appendChild(item);
      item = after;
    }
    caption.appendChild(document.createTextNode(' '));
    caption.appendChild(fold.button);
    caption.appendChild(fold.body);
    caption.classList.add('tr-caption');
  }

  function foldMeta(p) {
    if (p.closest('.tr-meta, .callout, .derivation-box')) return;
    var fold = makeFold('About this page', 'tr-fold--block', 'div');
    var wrap = document.createElement('div');
    wrap.className = 'tr-meta';
    p.parentNode.insertBefore(wrap, p);
    wrap.appendChild(fold.button);
    wrap.appendChild(fold.body);
    fold.body.appendChild(p);
  }

  function foldCallout(title) {
    var box = title.parentNode;
    if (!box || box.classList.contains('tr-folded') || box.closest('.derivation-box')) return;
    box.classList.add('tr-folded');
    title.classList.add('tr-folded-title');
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'tr-more';
    button.setAttribute('aria-expanded', 'false');
    button.textContent = 'Show';
    button.addEventListener('click', function () {
      var open = box.classList.toggle('tr-folded');
      button.setAttribute('aria-expanded', String(!open));
      button.textContent = open ? 'Show' : 'Hide';
    });
    title.appendChild(button);
  }

  /* ----------------------------------------------------------------- rail */
  function headerHeight() {
    var header = document.querySelector('body > .site-header, body > header');
    if (!header) return 0;
    var pos = getComputedStyle(header).position;
    return pos === 'sticky' || pos === 'fixed' ? header.offsetHeight : 0;
  }

  /* Images above the heading load lazily and change the height of the page after the jump, so the
     heading is held in place for a moment, until the reader scrolls on their own. */
  var holdUntil = 0, holdTarget = null;
  function stopHold() { holdUntil = 0; holdTarget = null; }
  ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function (type) {
    window.addEventListener(type, stopHold, { passive: true, capture: true });
  });

  function place(target) {
    var top = target.getBoundingClientRect().top + window.pageYOffset - headerHeight() - 12;
    window.scrollTo({ top: Math.max(0, top), behavior: 'instant' });
  }

  function hold() {
    if (!holdTarget || Date.now() > holdUntil) { stopHold(); return; }
    var off = holdTarget.getBoundingClientRect().top - headerHeight() - 12;
    if (Math.abs(off) > 2) place(holdTarget);
    requestAnimationFrame(hold);
  }

  function jump(mark) {
    openSectionOf(mark.target);
    place(mark.target);
    if (history.replaceState) history.replaceState(null, '', '#' + mark.id);
    try { mark.target.setAttribute('tabindex', '-1'); mark.target.focus({ preventScroll: true }); } catch (e) {}
    setActive(marks.indexOf(mark));
    holdTarget = mark.target;
    holdUntil = Date.now() + 1500;
    requestAnimationFrame(hold);
  }

  var activeIndex = -1;
  function setActive(i) {
    if (i === activeIndex) return;
    activeIndex = i;
    marks.forEach(function (m, k) {
      if (!m.button) return;
      m.button.classList.toggle('tr-bar--read', k < i);
      if (k === i) m.button.setAttribute('aria-current', 'location');
      else m.button.removeAttribute('aria-current');
    });
  }

  function isHidden(el) { return !!el.closest('.tr-hidden'); }

  function update() {
    var line = headerHeight() + window.innerHeight * 0.25;
    var i = -1;
    for (var k = 0; k < marks.length; k++) {
      if (isHidden(marks[k].target)) continue;   // a heading inside a folded section is never "current"
      if (marks[k].target.getBoundingClientRect().top <= line) i = k; else break;
    }
    if (window.innerHeight + window.pageYOffset >= document.documentElement.scrollHeight - 4) {
      for (var j = marks.length - 1; j >= 0; j--) if (!isHidden(marks[j].target)) { i = j; break; }
    }
    setActive(i);
    updateProgress(i);
  }

  /* ------------------------------------------------------------ derivations */
  /* A derivation box shows its title, the boxed result and its meaning; the steps, units, law and
     source open with "Show derivation". */
  function foldDerivation(box) {
    if (box.classList.contains('tr-dbox')) return;
    var head = box.querySelector(':scope > .derivation-head');
    if (!head || !box.querySelector('.derivation-steps')) return;
    box.classList.add('tr-dbox', 'tr-dfolded');
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'tr-more tr-dbtn';
    button.setAttribute('aria-expanded', 'false');
    button.textContent = 'Show derivation';
    button.addEventListener('click', function () {
      var folded = box.classList.toggle('tr-dfolded');
      button.setAttribute('aria-expanded', String(!folded));
      button.textContent = folded ? 'Show derivation' : 'Hide derivation';
    });
    head.appendChild(button);
  }

  /* --------------------------------------------------------------- sections */
  /* Each h2 folds to its title. The body of a section is the run of elements after its heading (or
     after the heading's wrapper) up to the element that holds the next h2; nothing is moved, the
     elements only get the class tr-hidden while the section is folded. */
  var sections = [];

  function bodyOf(head, heads) {
    function holdsHead(el) { return heads.some(function (h) { return el === h || el.contains(h); }); }
    var node = head, items = [];
    while (node && node.parentElement) {
      var sib = node.nextElementSibling;
      while (sib && !holdsHead(sib)) {
        if (!sib.matches('script, style, .tr-rail, .essential-recap')) items.push(sib);
        sib = sib.nextElementSibling;
      }
      if (items.length || sib) break;
      if (node.parentElement.matches('main, body')) break;
      node = node.parentElement;
    }
    return items;
  }

  function chevron() {
    var ns = 'http://www.w3.org/2000/svg';
    var svg = document.createElementNS(ns, 'svg');
    svg.setAttribute('viewBox', '0 0 24 24');
    svg.setAttribute('width', '18');
    svg.setAttribute('height', '18');
    svg.setAttribute('aria-hidden', 'true');
    svg.setAttribute('focusable', 'false');
    var path = document.createElementNS(ns, 'path');
    path.setAttribute('d', 'M6 9l6 6 6-6');
    svg.appendChild(path);
    return svg;
  }

  function setSection(sec, open) {
    sec.open = open;
    sec.items.forEach(function (el) { el.classList.toggle('tr-hidden', !open); });
    sec.head.classList.toggle('tr-sec-closed', !open);
    // the wrapper of a section (<section>, .theory-section) loses its own spacing while folded
    var host = sec.head.parentElement;
    if (host && !host.matches('main, body, article') && sec.items.every(function (el) { return el.parentElement === host; }))
      host.classList.toggle('tr-sec-host-closed', !open);
    sec.toggle.setAttribute('aria-expanded', String(open));
    sec.toggle.setAttribute('aria-label', (open ? 'Fold' : 'Open') + ' section: ' + sec.title);
  }

  function openSectionOf(target) {
    sections.forEach(function (sec) {
      if (!sec.open && (sec.items.some(function (el) { return el === target || el.contains(target); }) ||
          sec.head === target || sec.head.contains(target))) setSection(sec, true);
    });
  }

  function countWords(el) {
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT), node, words = 0;
    while ((node = walker.nextNode())) {
      var parent = node.parentElement;
      if (!parent || parent.closest('script, style, .tr-rail, .tr-more')) continue;
      if (parent.closest('.katex')) continue;
      var text = node.nodeValue;
      var formulas = (text.match(/\$\$[\s\S]*?\$\$|\$[^$]+\$/g) || []).length;
      text = text.replace(/\$\$[\s\S]*?\$\$|\$[^$]+\$/g, ' ');
      words += (text.match(/\S+/g) || []).length + 3 * formulas;
    }
    return words + 3 * el.querySelectorAll('.katex').length;
  }

  var WPM = 180;
  function minutes(words) { return Math.max(1, Math.round(words / WPM)); }

  function buildSections(scope, heads) {
    heads.forEach(function (h2) {
      var head = h2.closest('.section-header') || h2;
      if (!scope.contains(head)) head = h2;
      var items = bodyOf(head, heads);
      if (!items.length) return;
      var toggle = document.createElement('button');
      toggle.type = 'button';
      toggle.className = 'tr-sec-toggle';
      toggle.appendChild(chevron());
      var sec = { h2: h2, head: head, items: items, toggle: toggle, open: true, title: headingText(h2),
        words: countWords(head) + items.reduce(function (n, el) { return n + countWords(el); }, 0) };
      items.forEach(function (el) { el.classList.add('tr-sec-item'); });
      sec.essential = items.filter(function (el) { return el.matches('.essential-box'); });
      sec.ewords = sec.essential.reduce(function (n, el) { return n + countWords(el); }, 0);
      if (sec.essential.length) {   // the first figure of the section goes with its summary
        var fig = items.filter(function (el) { return el.matches(FIGURE); })[0];
        if (fig) { fig.classList.add('tr-key-fig'); sec.ewords += 40; }
      }
      head.classList.add('tr-sec-head');
      head.appendChild(toggle);
      head.addEventListener('click', function (event) {
        if (event.target.closest('a, input, select, textarea') ||
            (event.target.closest('button') && event.target.closest('button') !== toggle)) return;
        if (String(window.getSelection && window.getSelection()) !== '') return;
        if (mode === 'essential') return;   // every summary is already shown
        setSection(sec, !sec.open);
        update();
      });
      sections.push(sec);
    });
    if (sections.length < 2) {   // nothing worth folding: undo
      sections.forEach(function (sec) { sec.head.classList.remove('tr-sec-head'); sec.toggle.remove(); });
      sections = [];
      return;
    }
    sections.forEach(function (sec) { setSection(sec, false); });

    var bar = document.createElement('div');
    bar.className = 'tr-secbar';
    secInfo = document.createElement('span');
    secInfo.className = 'tr-secbar__info';
    bar.appendChild(secInfo);
    if (hasEssential()) bar.appendChild(modeSwitch());
    [['Open all', true], ['Fold all', false]].forEach(function (pair) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'tr-secbar__btn';
      b.textContent = pair[0];
      b.addEventListener('click', function () {
        sections.forEach(function (sec) { setSection(sec, pair[1]); });
        update();
      });
      bar.appendChild(b);
    });
    var hint = document.createElement('span');
    hint.className = 'tr-secbar__hint';
    hint.textContent = 'Keys \u2190 \u2192 move between sections';
    bar.appendChild(hint);
    sections[0].head.parentNode.insertBefore(bar, sections[0].head);
    setMode(initialMode());
    document.addEventListener('keydown', onKey);

    // a link to anything inside a folded section (side menu, #hash, citations) opens that section first
    function openHash() {
      var id = decodeURIComponent(location.hash.slice(1));
      var target = id && document.getElementById(id);
      if (target) { openSectionOf(target); update(); }
    }
    document.addEventListener('click', function (event) {
      var a = event.target.closest && event.target.closest('a[href*="#"]');
      if (!a || a.pathname !== location.pathname) return;
      var target = document.getElementById(decodeURIComponent(a.hash.slice(1)));
      if (target) openSectionOf(target);
    }, true);
    window.addEventListener('hashchange', openHash);
    if (location.hash) {
      openHash();
      var t = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (t) requestAnimationFrame(function () { place(t); });
    }
  }

  /* ------------------------------------------------------- reading modes */
  /* Essential: every section shows only its "What you need to know" box and its first figure (the
     page reads like a deck). Full: the whole page, sections folded as usual. Pages without summaries
     have no switch. The choice is remembered under ae_theory_mode; ?mode=essential|full overrides it. */
  var FIGURE = '.diagram-card, .diagram-container, figure.fig, .fig';
  var MODE_KEY = 'ae_theory_mode';
  var mode = 'full', secInfo = null, modeButtons = [];

  function hasEssential() { return sections.some(function (sec) { return sec.essential.length; }); }
  function wordsOf(sec) { return mode === 'essential' && sec.essential.length ? sec.ewords : sec.words; }

  function initialMode() {
    if (!hasEssential()) return 'full';
    var q = /[?&]mode=(essential|full)\b/.exec(location.search);
    if (q) return q[1];
    try { return localStorage.getItem(MODE_KEY) === 'essential' ? 'essential' : 'full'; } catch (e) { return 'full'; }
  }

  function setMode(m, remember) {
    mode = m === 'essential' && hasEssential() ? 'essential' : 'full';
    document.documentElement.classList.toggle('tr-essential', mode === 'essential');
    modeButtons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-mode') === mode)); });
    if (remember) { try { localStorage.setItem(MODE_KEY, mode); } catch (e) {} }
    var total = sections.reduce(function (n, s) { return n + wordsOf(s); }, 0);
    if (secInfo) secInfo.textContent = sections.length + ' sections \u00b7 about ' + minutes(total) + ' min of reading';
    update();
  }

  function modeSwitch() {
    var group = document.createElement('div');
    group.className = 'tr-mode';
    group.setAttribute('role', 'group');
    group.setAttribute('aria-label', 'Reading mode');
    [['essential', 'Essential'], ['full', 'Full']].forEach(function (pair) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'tr-mode__btn';
      b.setAttribute('data-mode', pair[0]);
      b.textContent = pair[1];
      b.addEventListener('click', function () { setMode(pair[0], true); });
      modeButtons.push(b);
      group.appendChild(b);
    });
    return group;
  }

  /* Left and right arrows move to the previous or next section, like turning a slide: in Full mode
     that section opens and the others fold. Ignored while typing and with a modifier key held. */
  function onKey(event) {
    if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return;
    if (event.ctrlKey || event.altKey || event.metaKey || event.shiftKey) return;
    var t = event.target;
    if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
    if (document.querySelector('[role="dialog"][aria-modal="true"]:not([hidden])')) return;
    var cur = activeIndex >= 0 && marks[activeIndex] ? sectionIndexOf(marks[activeIndex].target) : -1;
    var next = Math.max(0, Math.min(sections.length - 1, cur + (event.key === 'ArrowRight' ? 1 : -1)));
    if (next === cur && cur >= 0) return;
    event.preventDefault();
    var sec = sections[next];
    if (mode === 'full') sections.forEach(function (s) { setSection(s, s === sec); });
    var mark = marks.filter(function (m) { return m.target === sec.h2; })[0];
    if (mark) jump(mark); else place(sec.head);
  }

  /* --------------------------------------------------------------- progress */
  var progress = null;
  function sectionIndexOf(el) {
    var found = -1;
    sections.forEach(function (sec, i) {
      if (sec.h2.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING || sec.h2 === el) found = i;
    });
    return found;
  }

  function updateProgress(markIndex) {
    if (!progress || !sections.length) return;
    var i = markIndex >= 0 ? sectionIndexOf(marks[markIndex].target) : -1;
    var left = sections.slice(Math.max(0, i)).reduce(function (n, s) { return n + wordsOf(s); }, 0);
    progress.textContent = (i < 0 ? sections.length + ' sections' : (i + 1) + ' / ' + sections.length) +
      ' \u00b7 ~' + minutes(left) + ' min';
    progress.title = i < 0
      ? sections.length + ' sections, about ' + minutes(left) + ' min of reading'
      : 'Section ' + (i + 1) + ' of ' + sections.length + ', about ' + minutes(left) + ' min left';
  }

  /* ---------------------------------------------------------- figure layout */
  /* On a wide screen a narrow figure followed by text floats to the right of that text, like a slide
     with the picture beside the words (CSS, at least 1100 px). */
  function mediaWidth(card) {
    var media = card.querySelector('img, svg');
    if (!media) return 0;
    var w = 0;
    var mw = /max-width:\s*(?:min\(100%,\s*)?(\d+)px/.exec(media.getAttribute('style') || '');
    if (mw) w = +mw[1];
    if (!w && media.tagName.toLowerCase() === 'svg') {
      var vb = (media.getAttribute('viewBox') || '').split(/[\s,]+/);
      w = +media.getAttribute('width') || +vb[2] || 0;
    }
    if (!w && media.naturalWidth) w = media.naturalWidth;
    return w;
  }

  function sideFigures(scope) {
    [].forEach.call(scope.querySelectorAll('.diagram-card, .diagram-container, figure.fig'), function (card) {
      if (card.closest('.callout, .derivation-box, table, .tr-side') || card.classList.contains('pair')) return;
      if (card.querySelectorAll('img, svg').length !== 1) return;
      var w = mediaWidth(card);
      if (!w || w > 620) return;
      var next = card.nextElementSibling, prev = card.previousElementSibling;
      var textAfter = next && next.matches('p, ul, ol');
      if (!textAfter) {
        // the paragraph that introduces the figure comes first: the figure goes up beside it
        if (!prev || !prev.matches('p') || prev.classList.contains('tr-side') || countWords(prev) < 30) return;
        prev.parentNode.insertBefore(card, prev);
      }
      card.classList.add('tr-side');
      card.style.setProperty('--tr-fig-w', Math.max(280, w + 40) + 'px');
      card.parentElement.classList.add('tr-side-host');
    });
  }

  function buildRail() {
    var nav = document.createElement('nav');
    nav.className = 'tr-rail';
    nav.setAttribute('aria-label', 'Sections of this page');
    var list = document.createElement('ol');
    list.className = 'tr-rail__list';
    list.style.setProperty('--tr-n', String(marks.length));
    nav.appendChild(list);
    marks.forEach(function (mark, i) {
      var li = document.createElement('li');
      var button = document.createElement('button');
      button.type = 'button';
      button.className = 'tr-bar tr-bar--h' + mark.level;
      button.setAttribute('aria-label', mark.text);
      var line = document.createElement('span');
      line.className = 'tr-bar__line';
      line.setAttribute('aria-hidden', 'true');
      var tip = document.createElement('span');
      tip.className = 'tr-bar__tip';
      tip.setAttribute('aria-hidden', 'true');
      tip.textContent = mark.text;
      button.appendChild(line);
      button.appendChild(tip);
      button.addEventListener('click', function () { jump(mark); });
      li.appendChild(button);
      list.appendChild(li);
      mark.button = button;
      mark.index = i;
    });
    if (sections.length) {
      progress = document.createElement('p');
      progress.className = 'tr-progress';
      progress.setAttribute('aria-live', 'off');
      nav.insertBefore(progress, list);
    }
    document.body.appendChild(nav);
    document.documentElement.classList.add('tr-has-rail');
    var queued = false;
    window.addEventListener('scroll', function () {
      if (queued) return;
      queued = true;
      requestAnimationFrame(function () { queued = false; update(); });
    }, { passive: true });
    window.addEventListener('resize', update);
    update();
  }

  /* ----------------------------------------------------------------- init */
  function init() {
    if (document.documentElement.classList.contains('tr-on')) return;
    var scope = document.querySelector('main') || document.body;
    document.documentElement.classList.add('tr-on', 'tr-wide');
    wrapCitations(scope);
    [].forEach.call(scope.querySelectorAll('.diagram-caption, figcaption'), foldCaption);
    [].forEach.call(scope.querySelectorAll('p'), function (p) {
      if (META_RE.test(p.textContent.trim())) foldMeta(p);
    });
    [].forEach.call(scope.querySelectorAll('.callout-title, .note-title'), function (title) {
      if (META_TITLE_RE.test(title.textContent.trim())) foldCallout(title);
    });
    [].forEach.call(scope.querySelectorAll('.derivation-box'), foldDerivation);
    sideFigures(scope);
    marks = collect(scope);
    var heads = marks.filter(function (m) { return m.level === 2; }).map(function (m) { return m.target; });
    if (heads.length < 2) heads = collect(scope).filter(function (m) { return m.level === 2; }).map(function (m) { return m.target; });
    buildSections(scope, heads);
    if (marks.length >= MIN_MARKS) buildRail();
  }

  linkStyles();
  window.AETheoryReader = {
    init: init,
    sections: function () { return marks.map(function (m) { return { id: m.id, text: m.text, level: m.level }; }); }
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
