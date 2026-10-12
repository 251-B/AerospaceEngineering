/*!
 * Aerospace Engineering Study Portal: "Download PDF" / "Open as PDF" on theory and problem pages.
 *
 * Load once per topic page, after theme.js:
 *     <script defer src="../../../assets/js/pdf-export.js"></script>
 * The script adds its stylesheet (assets/css/print.css, the A4 black-and-white layout) and:
 *   - theory pages: a bar under the title with "Download PDF" and "Open as PDF";
 *   - problem pages: the same bar for all problems together, and both links on every problem card.
 * The PDFs are generated ahead of time by tools/build_pdfs.py into assets/pdf/<subject>/<area>/:
 *   <page>.pdf for the whole page and <page>/<card id>.pdf for each problem.
 * The generator opens the page with ?print=all or ?print=<card id>; this script then prepares the
 * printed layout (all solutions expanded, only the chosen problem, dark diagrams inverted). The same
 * preparation runs before the browser's own print dialog, so Ctrl+P gives the same document.
 */
(function () {
  'use strict';

  var SCRIPT = document.currentScript;
  var CARD_SEL = '.problem-card, .problem-box';
  var SUBJECTS = {
    'fluid-mechanics': 'Fluid Mechanics',
    'aerospace-materials-1': 'Aerospace Materials I',
    'engineering-mechanics': 'Engineering Mechanics',
    'advanced-maths': 'Advanced Mathematics',
    'business-management': 'Business Management'
  };

  var where = location.pathname.match(/\/subjects\/([^/]+)\/(teoria|problemas)\/([^/]+)\.html$/);
  if (!where) return;
  var slug = where[1], area = where[2], stem = where[3];
  var mode = new URLSearchParams(location.search).get('print');

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  function clean(s) { return (s || '').replace(/\s+/g, ' ').trim(); }

  function slugify(s) {
    return clean(s).normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^A-Za-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '').slice(0, 90);
  }

  function pdfHref(cardId) {
    return '../../../assets/pdf/' + slug + '/' + area + '/' + stem + (cardId ? '/' + cardId : '') + '.pdf';
  }

  function pageTitle() {
    var h1 = document.querySelector('h1');
    return clean(h1 ? h1.textContent : document.title.split(/\s[—|]\s/)[0]);
  }

  function cardTitle(card) {
    var t = card.querySelector('.problem-title') || card.querySelector('h2, h3');
    var n = card.querySelector('.problem-num, .problem-num-badge, .prob-num-badge, .problem-id, .problem-tag');
    return clean((n ? n.textContent + ' ' : '') + (t ? t.textContent : card.id));
  }

  function cards() {
    return [].filter.call(document.querySelectorAll(CARD_SEL), function (c) { return c.id; });
  }

  function ensureStyles() {
    if (document.querySelector('link[data-pdf-export]')) return;
    var href = SCRIPT && SCRIPT.src ? SCRIPT.src.replace(/js\/pdf-export\.js(\?.*)?$/, 'css/print.css') : '';
    if (!href) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet'; link.href = href; link.setAttribute('data-pdf-export', '');
    document.head.appendChild(link);
  }

  /* ------------------------------------------------------------------ buttons */
  var ICON_DOWN = '<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11"/><path d="M7 10l5 5 5-5"/><path d="M5 20h14"/></svg>';
  var ICON_OPEN = '<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4h6v6"/><path d="M20 4l-9 9"/><path d="M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>';

  function links(container, href, fileName, what) {
    var d = el('a', 'pdf-link');
    d.href = href;
    d.setAttribute('download', fileName);
    d.innerHTML = ICON_DOWN + '<span>Download PDF</span>';
    d.setAttribute('aria-label', 'Download ' + what + ' as an A4 PDF');
    var o = el('a', 'pdf-link');
    o.href = href;
    o.target = '_blank';
    o.rel = 'noopener';
    o.innerHTML = ICON_OPEN + '<span>Open as PDF</span>';
    o.setAttribute('aria-label', 'Open ' + what + ' as a PDF in a new tab');
    container.appendChild(d);
    container.appendChild(o);
  }

  function addButtons() {
    var h1 = document.querySelector('h1');
    if (!h1) return;
    var head = h1.closest('.article-header, .page-intro, .page-hero, .page-title-box, header') || h1.parentElement;
    var subject = SUBJECTS[slug] || '';
    var list = area === 'problemas' ? cards() : [];
    var bar = el('div', 'pdf-bar');
    bar.setAttribute('role', 'group');
    bar.setAttribute('aria-label', 'PDF of this page');
    bar.appendChild(el('span', 'pdf-bar-label', list.length ? 'All ' + list.length + ' problems' : 'Notes as PDF'));
    links(bar, pdfHref(''), slugify(subject + ' ' + pageTitle()) + '.pdf', list.length ? 'all the problems of this page' : 'these notes');
    head.appendChild(bar);

    list.forEach(function (card) {
      var chips = el('span', 'pdf-chips');
      chips.setAttribute('role', 'group');
      chips.setAttribute('aria-label', 'PDF of this problem');
      links(chips, pdfHref(card.id), slugify(subject + ' ' + cardTitle(card)) + '.pdf', 'this problem');
      var anchor = card.querySelector('a.src-link');
      if (anchor) anchor.insertAdjacentElement('afterend', chips);
      else {
        var t = card.querySelector('.problem-title') || card.querySelector('h2, h3');
        (t || card.firstElementChild || card).insertAdjacentElement(t ? 'afterend' : 'afterbegin', chips);
      }
    });
  }

  /* ------------------------------------------------------------------ printed layout */
  function luminance(rgb) {
    var m = String(rgb).match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?/);
    if (!m || (m[4] !== undefined && +m[4] < 0.5)) return 1;
    return (0.2126 * m[1] + 0.7152 * m[2] + 0.0722 * m[3]) / 255;
  }

  /* Diagrams drawn on a dark panel (light strokes) are inverted so they print dark on white. */
  function invertDarkDiagrams() {
    [].forEach.call(document.querySelectorAll('main svg, article svg'), function (svg) {
      if (svg.classList.contains('pdf-invert') || svg.closest('.katex, .pdf-bar, .pdf-chips, .ask-ai-bar')) return;
      var box = svg.getBoundingClientRect();
      if (box.width < 120 || box.height < 60) return;
      var dark = false;
      [].some.call(svg.querySelectorAll('rect'), function (r) {
        var b = r.getBoundingClientRect();
        if (b.width * b.height < 0.6 * box.width * box.height) return false;
        dark = luminance(getComputedStyle(r).fill) < 0.35;
        return true;
      });
      if (!dark) dark = luminance(getComputedStyle(svg).backgroundColor) < 0.35 ||
        luminance(getComputedStyle(svg.parentElement).backgroundColor) < 0.35;
      if (dark) svg.classList.add('pdf-invert');
    });
  }

  var opened = [];
  function openDetails() {
    [].forEach.call(document.querySelectorAll('details'), function (d) {
      if (!d.open) { d.open = true; opened.push(d); }
    });
  }

  function closeDetails() {
    opened.forEach(function (d) { d.open = false; });
    opened = [];
  }

  function printFrame(card) {
    if (document.querySelector('.pdf-print-head')) return;
    var root = document.querySelector('main') || document.querySelector('article') || document.body;
    var head = el('div', 'pdf-print-head');
    ['UC3M · BSc Aerospace Engineering', SUBJECTS[slug] || '', card ? pageTitle() : ''].forEach(function (t) {
      if (t) head.appendChild(el('span', '', t));
    });
    root.insertBefore(head, root.firstChild);
    var docs = [].map.call(document.querySelectorAll('.src-panel a'), function (a) { return clean(a.textContent); });
    var foot = el('div', 'pdf-print-foot',
      'Study notes written from the official course material' + (docs.length ? ' (' + docs.join('; ') + ')' : '') +
      '. Online version: subjects/' + slug + '/' + area + '/' + stem + '.html');
    root.appendChild(foot);
  }

  /* Keep only one problem: hide every sibling along the path from the card up to <body>. */
  function isolate(card) {
    for (var node = card; node && node !== document.body; node = node.parentElement) {
      [].forEach.call(node.parentElement ? node.parentElement.children : [], function (sib) {
        if (sib !== node && !sib.classList.contains('pdf-print-head') && !sib.classList.contains('pdf-print-foot') &&
            sib.tagName !== 'SCRIPT' && sib.tagName !== 'STYLE') sib.setAttribute('data-pdf-hidden', '');
      });
    }
  }

  /* The print layout lives under data-theme="print", so no dark/light rule of the page applies while
     printing. Only the attribute changes; the stored theme (ae_theme) is left alone. */
  var savedTheme = null;
  function printTheme(on) {
    var root = document.documentElement;
    if (on && root.getAttribute('data-theme') !== 'print') {
      savedTheme = root.getAttribute('data-theme');
      root.setAttribute('data-theme', 'print');
    } else if (!on && savedTheme !== null) {
      root.setAttribute('data-theme', savedTheme);
      savedTheme = null;
    }
  }

  /* Screen-only hints such as "Click to Expand" have no class: find them by their text. */
  function hideScreenHints() {
    [].forEach.call(document.querySelectorAll('summary *, .solution-toggle, .toggle-hint, [class*="expand"]'), function (e) {
      if (e.children.length === 0 && /^\W*click to (expand|collapse)\b/i.test(clean(e.textContent))) e.setAttribute('data-pdf-hidden', '');
    });
  }

  /* PDF output only: colour emoji (📄, 📖, ⚡ …) would embed a bitmap font; drop them. */
  function stripEmoji() {
    var re = /[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}\u{FE0F}\u{200D}]/gu;
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    for (var n = walker.nextNode(); n; n = walker.nextNode()) {
      if (re.test(n.nodeValue) && !(n.parentElement && n.parentElement.closest('.katex'))) {
        re.lastIndex = 0;
        n.nodeValue = n.nodeValue.replace(re, '');
      }
      re.lastIndex = 0;
    }
  }

  /* Displayed equations wider than the printed line are scaled down to fit (not below 70 %). */
  function fitEquations() {
    [].forEach.call(document.querySelectorAll('.katex-display'), function (d) {
      var k = d.querySelector('.katex');
      if (!k) return;
      k.style.fontSize = '';
      var avail = d.clientWidth, need = k.scrollWidth;
      if (avail > 0 && need > avail) k.style.fontSize = Math.max(0.7, avail / need * 0.98).toFixed(3) + 'em';
    });
  }

  /* Sticky or fixed bars (sub-chapter tabs, floating buttons) would print over the text. */
  function hidePinned() {
    [].forEach.call(document.querySelectorAll('body *'), function (e) {
      if (e.classList.contains('pdf-print-head') || e.closest('.katex')) return;
      var pos = getComputedStyle(e).position;
      if (pos === 'fixed' || pos === 'sticky') e.setAttribute('data-pdf-hidden', '');
    });
  }

  function prepare() {
    hidePinned();
    printTheme(true);
    hideScreenHints();
    openDetails();
    invertDarkDiagrams();
    var list = cards();
    list.forEach(function (c, i) { if (i) c.classList.add('pdf-break'); });
  }

  function init() {
    ensureStyles();
    if (mode) {
      document.documentElement.classList.add('pdf-render');
      var card = mode !== 'all' ? document.getElementById(mode) : null;
      printFrame(card);
      if (card) isolate(card);
      /* KaTeX renders on DOMContentLoaded, after this deferred script: wait for the page to settle. */
      window.addEventListener('load', function () {
        setTimeout(function () {
          stripEmoji();
          prepare();
          if (card) card.classList.remove('pdf-break');
          fitEquations();
          document.documentElement.setAttribute('data-pdf-ready', '');
        }, 300);
      });
      return;
    }
    printFrame(null);
    addButtons();
    window.addEventListener('beforeprint', prepare);
    window.addEventListener('afterprint', function () { closeDetails(); printTheme(false); });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
