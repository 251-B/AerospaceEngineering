/*!
 * Aerospace Engineering Study Portal: "What's new" (bell, updates panel and toast).
 *
 * Loaded on every page by assets/js/theme.js, after assets/data/updates.js (no page carries its own
 * <script> tag for it); the script adds its own stylesheet (assets/css/updates.css). Skipped in the
 * PDF print mode (?print=...), and hidden by @media print.
 *
 *   - bell: a button in the page header, in front of the reading-palette picker and the theme
 *     toggle, with a badge that counts the entries the visitor has not read yet;
 *   - panel: the list of entries (date, subject tag, title, short text, optional link), newest first.
 *     Opening it marks everything as read, but the entries that were new stay highlighted until it
 *     closes. Only one of this panel, the study timer and Focus Lab is open at a time;
 *   - toast: a small notice at the bottom left, shown once per newest unread entry (and never when
 *     the browser blocks storage, since it could not be remembered). A visually hidden live region
 *     announces it to screen readers.
 *
 * Entries live in assets/data/updates.js (window.AE_UPDATES), written by hand when a change that
 * users can see is closed. Links are paths from the portal root; they are resolved against this
 * script's own URL, so they work from any page depth and over file://.
 *
 * Storage: 'ae_updates' (JSON: { seen: [ids], toast: id }). The very first visit counts the three
 * newest entries as unread and everything older as read.
 * API: window.AEUpdates = { KEY, list, unread, open, close, markAllRead }
 */
(function () {
  'use strict';

  if (window.AEUpdates) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var SCRIPT = document.currentScript;
  var KEY = 'ae_updates';
  var FIRST_VISIT_UNREAD = 3;
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var ROOT = SCRIPT && SCRIPT.src ? SCRIPT.src.replace(/assets\/js\/updates\.js(\?.*)?$/, '') : '';

  var entries = (Array.isArray(window.AE_UPDATES) ? window.AE_UPDATES : []).filter(function (e) {
    return e && typeof e.id === 'string' && typeof e.title === 'string';
  });

  /* ---------------------------------------------------------------- state */
  var memory = null;   // used when localStorage is blocked

  // A write that is not read back means a toast could not be remembered, so it would come back on every page.
  var storageOk = (function () {
    try {
      var probe = KEY + '_probe';
      localStorage.setItem(probe, '1');
      var ok = localStorage.getItem(probe) === '1';
      localStorage.removeItem(probe);
      return ok;
    } catch (e) { return false; }
  })();

  function readState() {
    var raw = null;
    try { raw = localStorage.getItem(KEY); } catch (e) { return memory; }
    if (!raw) return null;
    try {
      var s = JSON.parse(raw);
      if (s && Array.isArray(s.seen)) return { seen: s.seen.filter(function (x) { return typeof x === 'string'; }), toast: typeof s.toast === 'string' ? s.toast : '' };
    } catch (e) { /* corrupted value: start again */ }
    return null;
  }

  function writeState(s) {
    memory = s;
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* storage blocked: keep it in memory only */ }
  }

  var state = readState();
  if (!state) {
    state = { seen: entries.slice(FIRST_VISIT_UNREAD).map(function (e) { return e.id; }), toast: '' };
    // A data file that failed to load must not leave an empty "seen" list: every entry would be unread next time.
    if (entries.length) writeState(state);
  }

  function unread() {
    return entries.filter(function (e) { return state.seen.indexOf(e.id) < 0; });
  }

  function markAllRead() {
    if (!entries.length) return;
    state.seen = entries.map(function (e) { return e.id; });
    writeState(state);
    refresh();
  }

  /* ---------------------------------------------------------------- helpers */
  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function svg(inner, size) {
    var s = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    s.setAttribute('viewBox', '0 0 24 24');
    s.setAttribute('width', size);   // sized without the stylesheet too, so a slow or missing CSS never draws a 300 x 150 icon
    s.setAttribute('height', size);
    s.setAttribute('aria-hidden', 'true');
    s.innerHTML = inner;
    return s;
  }

  function formatDate(iso) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(iso || '');
    return m ? (+m[3]) + ' ' + MONTHS[+m[2] - 1] + ' ' + m[1] : '';
  }

  // Only paths inside the portal: no scheme, no protocol-relative URL, no way out of the root.
  function resolveLink(path) {
    if (typeof path !== 'string' || !path || /^[a-z][a-z0-9+.-]*:/i.test(path) || path.charAt(0) === '/' || path.indexOf('..') >= 0) return '';
    return ROOT + encodeURI(path);
  }

  /* ---------------------------------------------------------------- UI */
  var ui = {};
  var fresh = [];   // ids that were unread when the panel opened

  function build() {
    if (document.getElementById('updatesButton') || !entries.length) return;
    var toggle = document.getElementById('themeToggle');
    var anchor = document.getElementById('surfacePicker') || toggle;
    if (!anchor || !anchor.parentNode) return;

    var bell = el('button', 'upd-bell');
    bell.type = 'button';
    bell.id = 'updatesButton';
    bell.setAttribute('aria-haspopup', 'dialog');
    bell.setAttribute('aria-expanded', 'false');
    bell.setAttribute('aria-controls', 'updatesPanel');
    bell.title = 'What’s new';
    bell.appendChild(svg('<path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/>', 17));
    var badge = el('span', 'upd-badge');
    badge.setAttribute('aria-hidden', 'true');
    bell.appendChild(badge);
    anchor.parentNode.insertBefore(bell, anchor);

    var panel = el('div', 'upd-panel');
    panel.id = 'updatesPanel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-modal', 'false');
    panel.setAttribute('aria-label', 'What’s new');
    panel.tabIndex = -1;
    panel.hidden = true;   // hidden without the stylesheet too
    var head = el('div', 'upd-panel__head');
    head.appendChild(el('h2', 'upd-panel__title', 'What’s new'));
    var list = el('ol', 'upd-list');
    panel.appendChild(head);
    panel.appendChild(list);
    document.body.appendChild(panel);

    var toast = el('div', 'upd-toast');
    toast.id = 'updatesToast';
    toast.hidden = true;
    var toastBody = el('div', 'upd-toast__body');
    var toastKicker = el('span', 'upd-toast__kicker', 'New on the portal');
    var toastTitle = el('strong', 'upd-toast__title');
    toastBody.appendChild(toastKicker);
    toastBody.appendChild(toastTitle);
    var toastOpen = el('button', 'upd-toast__open', 'See what’s new');
    toastOpen.type = 'button';
    var toastClose = el('button', 'upd-toast__close');
    toastClose.type = 'button';
    toastClose.setAttribute('aria-label', 'Dismiss');
    toastClose.appendChild(svg('<path d="M6 6l12 12M18 6L6 18"/>', 16));
    toast.appendChild(toastBody);
    toast.appendChild(toastOpen);
    toast.appendChild(toastClose);
    document.body.appendChild(toast);

    // A live region only announces text added after it is rendered, so the toast card (display: none
    // until it shows) cannot be one: this empty, visually hidden region carries the announcement.
    var live = el('div', 'upd-sr');
    live.id = 'updatesLive';
    live.setAttribute('role', 'status');
    live.setAttribute('aria-live', 'polite');
    document.body.appendChild(live);

    ui = { bell: bell, badge: badge, panel: panel, list: list, toast: toast, toastTitle: toastTitle, live: live };

    bell.addEventListener('click', function () { if (isOpen()) closePanel(false); else openPanel(); });
    toastOpen.addEventListener('click', function () { hideToast(); openPanel(); });
    toastClose.addEventListener('click', hideToast);
    document.addEventListener('keydown', onKeydown);   // Escape closes from anywhere; Tab is handled inside the panel
    document.addEventListener('click', function (event) {
      if (isOpen() && !panel.contains(event.target) && !bell.contains(event.target) && !toast.contains(event.target)) closePanel(false);
    });
    window.addEventListener('resize', function () { if (isOpen()) place(); });
    window.addEventListener('scroll', function () { if (isOpen()) place(); }, true);
    // Another tab read the entries (or a new one arrived): mirror it here.
    window.addEventListener('storage', function (event) {
      if (event.key !== KEY) return;
      state = readState() || state;
      refresh();
      if (!unread().length) hideToast();
    });

    render();
    refresh();
    maybeToast();
  }

  function render() {
    ui.list.textContent = '';
    entries.forEach(function (entry) {
      var item = el('li', 'upd-item');
      if (fresh.indexOf(entry.id) >= 0) item.classList.add('is-new');
      var meta = el('div', 'upd-item__meta');
      if (fresh.indexOf(entry.id) >= 0) {
        var dot = el('span', 'upd-item__new', 'New');
        meta.appendChild(dot);
      }
      if (entry.tag) meta.appendChild(el('span', 'upd-item__tag', entry.tag));
      var date = formatDate(entry.date);
      if (date) {
        var time = el('time', 'upd-item__date', date);
        time.setAttribute('datetime', entry.date);
        meta.appendChild(time);
      }
      item.appendChild(meta);
      item.appendChild(el('h3', 'upd-item__title', entry.title));
      if (entry.text) item.appendChild(el('p', 'upd-item__text', entry.text));
      var href = resolveLink(entry.link);
      if (href) {
        var a = el('a', 'upd-item__link', 'Open →');
        a.href = href;
        item.appendChild(a);
      }
      ui.list.appendChild(item);
    });
  }

  function refresh() {
    if (!ui.bell) return;
    var n = unread().length;
    ui.badge.textContent = n > 9 ? '9+' : String(n);
    ui.badge.hidden = n === 0;
    ui.bell.classList.toggle('has-unread', n > 0);
    ui.bell.setAttribute('aria-label', 'What’s new' + (n ? ' (' + n + ' unread)' : ''));
  }

  /* ---------------------------------------------------------------- toast */
  function maybeToast() {
    var news = unread();
    if (!storageOk || !news.length || state.toast === news[0].id) return;
    state.toast = news[0].id;
    writeState(state);
    var title = news.length > 1 ? news[0].title + ' (+' + (news.length - 1) + ' more)' : news[0].title;
    ui.toastTitle.textContent = title;
    ui.toast.hidden = false;
    setTimeout(function () { if (!ui.toast.hidden) ui.live.textContent = 'New on the portal: ' + title; }, 50);
  }

  function hideToast() {
    if (!ui.toast) return;
    ui.toast.hidden = true;
    ui.live.textContent = '';
  }

  /* ---------------------------------------------------------------- panel */
  function isOpen() { return !!ui.panel && !ui.panel.hidden; }

  // Desktop: under the bell, kept inside the viewport. Phone widths: CSS bottom sheet.
  function place() {
    if (window.matchMedia('(max-width: 600px)').matches) {
      ui.panel.style.top = '';
      ui.panel.style.left = '';
      return;
    }
    var box = ui.bell.getBoundingClientRect();
    var width = ui.panel.offsetWidth;
    var left = Math.max(12, Math.min(box.right - width, window.innerWidth - width - 12));
    // A header that has scrolled away (the exams and sources pages have no sticky one) must not take the panel with it.
    var top = Math.max(12, Math.min(box.bottom + 10, window.innerHeight - 160));
    ui.panel.style.top = Math.round(top) + 'px';
    ui.panel.style.left = Math.round(left) + 'px';
  }

  function openPanel() {
    if (!ui.panel || isOpen()) return;
    // One floating panel at a time, like the study timer and Focus Lab.
    if (window.AEPomodoro && typeof window.AEPomodoro.close === 'function') window.AEPomodoro.close();
    if (window.AEFocusLab && typeof window.AEFocusLab.close === 'function') window.AEFocusLab.close();
    hideToast();
    fresh = unread().map(function (e) { return e.id; });
    render();
    markAllRead();
    ui.panel.hidden = false;
    place();   // measures the unhidden panel, which also lets the fade-in start from its closed state
    ui.panel.classList.add('is-open');
    ui.bell.setAttribute('aria-expanded', 'true');
    ui.panel.scrollTop = 0;
    ui.panel.focus({ preventScroll: true });
  }

  function closePanel(returnFocus) {
    if (!isOpen()) return;
    ui.panel.classList.remove('is-open');
    ui.panel.hidden = true;
    ui.bell.setAttribute('aria-expanded', 'false');
    fresh = [];
    render();
    if (returnFocus) ui.bell.focus();
  }

  function onKeydown(event) {
    if (!isOpen()) return;
    if (event.key === 'Escape') {
      event.stopPropagation();
      closePanel(true);
      return;
    }
    if (event.key !== 'Tab' || !ui.panel.contains(event.target)) return;
    // The panel sits at the end of <body>: leaving it either way hands focus back to the bell.
    // Focus starts on the panel itself, so Tab goes on to the first link and Shift+Tab leaves.
    var links = ui.panel.querySelectorAll('a[href]');
    var first = links[0];
    var last = links[links.length - 1];
    var atStart = event.target === ui.panel || event.target === first;
    var atEnd = links.length ? event.target === last : event.target === ui.panel;
    if ((event.shiftKey && atStart) || (!event.shiftKey && atEnd)) {
      event.preventDefault();
      closePanel(true);
    }
  }

  /* ---------------------------------------------------------------- boot */
  function addStylesheet() {
    if (!SCRIPT || !SCRIPT.src || document.querySelector('link[href*="updates.css"]')) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = SCRIPT.src.replace(/js\/updates\.js(\?.*)?$/, 'css/updates.css');
    document.head.appendChild(link);
  }

  addStylesheet();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();

  window.AEUpdates = {
    KEY: KEY,
    list: function () { return entries.map(function (e) { return JSON.parse(JSON.stringify(e)); }); },
    unread: function () { return unread().map(function (e) { return e.id; }); },
    open: openPanel,
    close: function () { closePanel(false); },
    markAllRead: markAllRead
  };
})();
