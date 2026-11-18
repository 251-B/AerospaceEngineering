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
 * No storage. API: window.AETheoryReader = { init, sections }
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
      m.button.classList.toggle('tr-bar--read', k < i);
      if (k === i) m.button.setAttribute('aria-current', 'location');
      else m.button.removeAttribute('aria-current');
    });
  }

  function update() {
    var line = headerHeight() + window.innerHeight * 0.25;
    var i = -1;
    for (var k = 0; k < marks.length; k++) {
      if (marks[k].target.getBoundingClientRect().top <= line) i = k; else break;
    }
    if (window.innerHeight + window.pageYOffset >= document.documentElement.scrollHeight - 4) i = marks.length - 1;
    setActive(i);
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
    marks = collect(scope);
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
