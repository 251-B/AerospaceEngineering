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
      if (e.children.length === 0 && /^\W*(click to (expand|collapse)|expand\s*\/\s*collapse|show|hide)\W*$|^\W*click to (expand|collapse)\b/i.test(clean(e.textContent))) e.setAttribute('data-pdf-hidden', '');
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

  /* Tables with displayed equations would grow past the page: fix their layout, 60 % for the maths. */
  function fitTables() {
    [].forEach.call(document.querySelectorAll('table'), function (t) {
      if (!t.querySelector('.katex-display') || t.closest('.katex')) return;
      var rows = t.rows, n = 0, math = {}, text = [];
      for (var r = 0; r < rows.length; r++) {
        n = Math.max(n, rows[r].cells.length);
        for (var c = 0; c < rows[r].cells.length; c++) {
          var cell = rows[r].cells[c];
          if (cell.querySelector('.katex-display')) math[c] = 1;
          text[c] = (text[c] || 0) + clean(cell.textContent).length;
        }
      }
      var longest = [];
      for (var r2 = 0; r2 < rows.length; r2++) for (var c2 = 0; c2 < rows[r2].cells.length; c2++) {
        var cell2 = rows[r2].cells[c2];
        if (cell2.querySelector('.katex-display')) continue;
        clean(cell2.textContent).split(' ').forEach(function (w) { longest[c2] = Math.max(longest[c2] || 0, w.length); });
      }
      var tw = t.parentElement.getBoundingClientRect().width || 670;
      var m = Object.keys(math).length, others = n - m, total = 0;
      if (!m || !n) return;
      for (var i = 0; i < n; i++) if (!math[i]) total += Math.max(text[i] || 0, 1);
      var colgroup = el('colgroup');
      for (var j = 0; j < n; j++) {
        var col = el('col');
        /* maths columns share 60 %; the others share 40 % by their amount of text (at least 7 % each) */
        var minW = Math.min(30, ((longest[j] || 2) * 7.2 + 14) / tw * 100);     /* never split a word */
        var w = math[j] ? (others ? 60 / m : 100 / m) : Math.max(7, minW, 40 * Math.max(text[j] || 0, 1) / total);
        col.style.width = w.toFixed(1) + '%';
        colgroup.appendChild(col);
      }
      [].forEach.call(t.querySelectorAll('colgroup'), function (g) { g.remove(); });
      t.insertBefore(colgroup, t.firstChild);
      [].forEach.call(t.querySelectorAll('th, td'), function (cell) { cell.style.width = 'auto'; });
      t.style.tableLayout = 'fixed';
      t.style.width = '100%';
    });
  }

  /* Displayed equations wider than the printed line are scaled down to fit (not below 70 %, 55 % in tables). */
  function fitEquations() {
    [].forEach.call(document.querySelectorAll('.katex-display'), function (d) {
      var k = d.querySelector('.katex');
      if (!k) return;
      k.style.fontSize = '';
      /* the width the equation needs: its rows plus the equation number KaTeX places at the right */
      var need = 0, tag = k.querySelector('.tag');
      [].forEach.call(k.querySelectorAll('.katex-html > .base'), function (b) { need += b.getBoundingClientRect().width; });
      if (tag) need += 2 * (tag.getBoundingClientRect().width + 14);   /* centred: the number needs its width on both sides */
      need = Math.max(need, k.scrollWidth);
      var avail = d.clientWidth;
      var floor = d.closest('td, th') ? 0.55 : 0.7;
      if (avail > 0 && need > avail) k.style.fontSize = Math.max(floor, avail / need * 0.98).toFixed(3) + 'em';
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

  /* Keep a label or heading on the same page as the start of what it introduces: wrap it with the
     next ~120 px of content in one unbreakable block (break-after: avoid alone is not reliable). */
  var KEEP_SEL = 'h2, h3, h4, h5, [class*="phase-badge"], .phase-title, .phase-heading, .section-label, .section-tag, .pdf-summary, ' +
    '.article-category, .callout-title, .result-callout-title, .strategy-title, .step-heading, .step-subheading, ' +
    '.result-label, .result-title, .result-header, .result-box-title, .box-label, .box-title, summary';
  /* PDF only: open collapsible blocks become plain blocks, so their title can be kept with the content. */
  function flattenDetails() {
    [].forEach.call(document.querySelectorAll('details'), function (d) {
      if (d.closest('[data-pdf-hidden]') || d.matches(CARD_SEL)) return;
      var div = el('div', d.className + ' pdf-details');
      while (d.firstChild) {
        var n = d.firstChild;
        if (n.tagName === 'SUMMARY') {
          var s = el('div', (n.className ? n.className + ' ' : '') + 'pdf-summary');
          while (n.firstChild) s.appendChild(n.firstChild);
          d.removeChild(n);
          div.appendChild(s);
        } else div.appendChild(n);
      }
      d.parentNode.replaceChild(div, d);
    });
  }

  function hasLooseText(e) {
    for (var c = e.firstChild; c; c = c.nextSibling) if (c.nodeType === 3 && /\S/.test(c.nodeValue)) return true;
    return false;
  }

  function isBlock(e) {
    return /^(block|flex|grid|table|list-item|flow-root)$/.test(getComputedStyle(e).display);
  }

  var NO_DESCEND = 'table, ul, ol, p, li, pre, .katex-display, .math-block, svg, figure, .figure, ' +
    '.diagram-card, [class*="diagram"], [class*="figure"], [class*="table-"], .table-container, .table-wrapper';

  function keepWithNext() {
    [].forEach.call(document.querySelectorAll(KEEP_SEL), function (label) {
      if (label.closest('.pdf-keep, .katex, .pdf-print-head, [data-pdf-hidden]') || label.tagName === 'SUMMARY') return;
      var parent = label.parentElement;
      /* only blocks are regrouped, and never inside running text (that would pull words out of sentences) */
      if (!parent || hasLooseText(parent) || !(isBlock(label) || getComputedStyle(label).display === 'inline-block')) return;
      /* a heading that ends a small header block (tag + title) carries the whole block with it */
      while (!label.nextElementSibling && label.parentElement && label.parentElement.parentElement &&
             label.parentElement.getBoundingClientRect().height < 160 && !hasLooseText(label.parentElement.parentElement) &&
             !label.parentElement.matches(CARD_SEL + ', main, article, section, body')) {
        label = label.parentElement;
      }
      if (label.closest('.pdf-keep')) return;
      var group = [label], h = label.getBoundingClientRect().height, n = label.nextElementSibling, depth = 0;
      while (n && h < 120) {
        if (n.matches(KEEP_SEL) && !hasLooseText(n.parentElement)) { group.push(n); h += n.getBoundingClientRect().height; n = n.nextElementSibling; continue; }
        if (!isBlock(n) || n.tagName === 'SCRIPT') break;
        if (n.matches(KEEP_SEL)) { group.push(n); h += n.getBoundingClientRect().height; n = n.nextElementSibling; continue; }
        var nh = n.getBoundingClientRect().height;
        if (nh > 200) {
          /* too tall to move with the label: put the label at the top of it and keep it with its first block */
          var first = n.firstElementChild;
          if (first && depth < 3 && !n.matches(NO_DESCEND) && !hasLooseText(n) &&
              (isBlock(first) || getComputedStyle(first).display === 'inline-block') &&
              !n.querySelector(':scope > table, :scope > svg, :scope > figure, :scope > img')) {
            group.forEach(function (g) { n.insertBefore(g, first); });
            n = first; depth++;
            continue;
          }
          break;                                   /* leave the break to the browser */
        }
        group.push(n); h += nh; n = n.nextElementSibling;
      }
      if (group.length < 2 || h > 480) return;
      var box = el('div', 'pdf-keep');
      group[0].parentNode.insertBefore(box, group[0]);
      group.forEach(function (g) { box.appendChild(g); });
    });
  }

  /* The closing source line of a problem stays on the page of the last lines of its solution: it is
     moved next to the deepest last block of what precedes it, and both are kept together. */
  function keepWithPrevious() {
    [].forEach.call(document.querySelectorAll('.problem-footer'), function (foot) {
      if (foot.closest('[data-pdf-hidden]')) return;
      var prev = foot.previousElementSibling, depth = 0;
      while (prev && prev.getBoundingClientRect().height > 200 && prev.lastElementChild && depth < 4 &&
             !prev.matches('table, ul, ol, p, .katex-display, svg, figure') && !hasLooseText(prev)) {
        prev = prev.lastElementChild; depth++;
      }
      /* a tall list: its last item continues in a list of its own, kept with the footer */
      if (prev && prev.matches('ul, ol') && prev.children.length > 1 && prev.getBoundingClientRect().height > 260) {
        var tail = document.createElement(prev.tagName);
        tail.className = prev.className;
        if (prev.tagName === 'OL') tail.setAttribute('start', String((parseInt(prev.getAttribute('start') || '1', 10)) + prev.children.length - 1));
        tail.appendChild(prev.lastElementChild);
        tail.style.marginTop = '0';
        prev.style.marginBottom = '0';
        prev.parentNode.insertBefore(tail, prev.nextSibling);
        prev = tail;
      }
      if (!prev || prev.getBoundingClientRect().height > 260 || !isBlock(prev)) return;
      var box = el('div', 'pdf-keep');
      prev.parentNode.insertBefore(box, prev);
      box.appendChild(prev);
      box.appendChild(foot);
    });
  }

  /* A phase box that holds only its label (no content yet on the web page) is left out of the PDF. */
  function hideEmptyPhases() {
    [].forEach.call(document.querySelectorAll('[class*="phase-badge"], .phase-title'), function (label) {
      var box = label.parentElement;
      if (box && box !== document.body && clean(box.textContent) === clean(label.textContent)) box.setAttribute('data-pdf-hidden', '');
    });
  }

  /* Hand-drawn diagrams use light screen colours: on paper they get a grey-ink filter (colours to greys,
     light greys darkened, white kept white). Figures from tools/figures carry .fig-kit and print as drawn. */
  function inkFilter() {
    if (document.getElementById('pdf-ink-defs')) return;
    var ns = 'http://www.w3.org/2000/svg';
    var defs = document.createElementNS(ns, 'svg');
    defs.setAttribute('id', 'pdf-ink-defs');
    defs.setAttribute('width', '0'); defs.setAttribute('height', '0');
    defs.setAttribute('style', 'position:absolute');
    defs.innerHTML = '<filter id="pdf-ink" color-interpolation-filters="sRGB">' +
      '<feColorMatrix type="saturate" values="0"/>' +
      '<feComponentTransfer><feFuncR type="gamma" exponent="2.4"/><feFuncG type="gamma" exponent="2.4"/>' +
      '<feFuncB type="gamma" exponent="2.4"/></feComponentTransfer></filter>';
    document.body.appendChild(defs);
  }

  function prepare() {
    inkFilter();
    hidePinned();
    hideEmptyPhases();
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
          fitTables();
          fitEquations();
          flattenDetails();
          keepWithNext();
          keepWithPrevious();
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
