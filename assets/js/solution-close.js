/*!
 * Aerospace Engineering Study Portal: "Close" button at the end of a worked solution.
 *
 * Loaded on every page by assets/js/theme.js (no page carries its own <script> tag for it); the script
 * adds its own stylesheet (assets/css/solution-close.css). Skipped in the PDF print mode (?print=...),
 * and hidden by @media print.
 *
 * Worked solutions are collapsible: <details class="solution-details"> (Engineering Mechanics, Fluid
 * Mechanics) or a whole problem card, <details class="problem-card"> (Aerospace Materials I). Once one is
 * open and read to the end, the only way to fold it was to scroll back to its summary. This adds a bar
 * with a "Close" button as the last child of each of them. Pressing it folds the <details>, scrolls back
 * to its summary when that is above the visible area (below the sticky page header) and moves the focus
 * to the summary.
 *
 * The bar goes after the content block, not inside it, so the pages' own `.phase-block:last-child` rule
 * keeps matching. No storage. API: window.AESolutionClose = { init }
 */
(function () {
  'use strict';

  if (window.AESolutionClose) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var SCRIPT = document.currentScript;
  var SVG_NS = 'http://www.w3.org/2000/svg';
  var KINDS = [
    { sel: 'details.solution-details', summary: 'summary.solution-summary', label: 'Close solution' },
    { sel: 'details.problem-card', summary: 'summary.problem-summary', label: 'Close problem' }
  ];

  function icon() {
    var svg = document.createElementNS(SVG_NS, 'svg');
    svg.setAttribute('viewBox', '0 0 24 24');
    svg.setAttribute('width', '14');   // sized without the stylesheet too
    svg.setAttribute('height', '14');
    svg.setAttribute('aria-hidden', 'true');
    svg.setAttribute('focusable', 'false');
    var path = document.createElementNS(SVG_NS, 'path');
    path.setAttribute('d', 'M6 6l12 12M18 6L6 18');
    svg.appendChild(path);
    return svg;
  }

  /* Height of the sticky page header, so the summary is not scrolled under it. */
  function headerHeight() {
    var header = document.querySelector('body > .site-header, body > header.site-header');
    return header && getComputedStyle(header).position === 'sticky' ? header.offsetHeight : 0;
  }

  function closeAndReturn(details, summary) {
    details.open = false;
    if (!summary) return;
    var gap = headerHeight() + 12;
    var top = summary.getBoundingClientRect().top;
    // An instant jump, not a smooth scroll: the way back can be thousands of pixels and a long animation
    // lands off target when the layout above the summary shifts on the way (lazy images). 'instant' also
    // overrides a page's own `scroll-behavior: smooth`, and keeps prefers-reduced-motion users unanimated.
    if (top < gap) window.scrollTo({ top: Math.max(0, top + window.pageYOffset - gap), behavior: 'instant' });
    try { summary.focus({ preventScroll: true }); } catch (e) { summary.focus(); }
  }

  function addBar(details, kind) {
    if (details.querySelector(':scope > .sol-close-bar')) return;
    var summary = details.querySelector(':scope > ' + kind.summary);
    var bar = document.createElement('div');
    bar.className = 'sol-close-bar';
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'sol-close';
    button.appendChild(icon());
    button.appendChild(document.createTextNode(kind.label));
    button.addEventListener('click', function () { closeAndReturn(details, summary); });
    bar.appendChild(button);
    details.appendChild(bar);
  }

  function init() {
    KINDS.forEach(function (kind) {
      [].forEach.call(document.querySelectorAll(kind.sel), function (details) { addBar(details, kind); });
    });
  }

  function addStylesheet() {
    if (!SCRIPT || !SCRIPT.src || document.querySelector('link[href*="solution-close.css"]')) return;
    var linkEl = document.createElement('link');
    linkEl.rel = 'stylesheet';
    linkEl.href = SCRIPT.src.replace(/js\/solution-close\.js(\?.*)?$/, 'css/solution-close.css');
    document.head.appendChild(linkEl);
  }

  addStylesheet();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();

  window.AESolutionClose = { init: init };
})();
