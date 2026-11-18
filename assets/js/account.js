/*!
 * Sideris portal: user accounts (profile, preferences, header button)
 *
 * Loaded by assets/js/theme.js on every page (no page carries its own tag); the account pages
 * (account/login.html, account/signup.html, account/settings.html) use its API.
 *
 * Backend: this first version runs in LOCAL mode. The account and its preferences are kept in
 * this browser only (localStorage 'ae_account' for the accounts, 'ae_session' for the signed-in
 * one; neither key contains "theme"). Passwords are never stored: only a salted SHA-256 digest.
 * A cloud backend (sign-in from any device, Google / Microsoft) plugs in behind the same API
 * later; window.AE_ACCOUNT_CONFIG = { backend: 'local' } is the only mode for now.
 *
 * API: window.AEAccount = {
 *   SUBJECTS, SURFACES, backend,
 *   current()                       -> { name, email, created, prefs } | null
 *   signUp({ name, email, password }) -> Promise<user>      (rejects with Error(message))
 *   signIn({ email, password })       -> Promise<user>
 *   signOut()
 *   update({ name }) / updatePrefs(patch) / changePassword(old, next) -> Promise
 *   deleteAccount(password)          -> Promise
 *   exportData()                     -> plain object (account without the digest + device data)
 *   deviceData()                     -> [{ key, label, size }]
 *   apply()                          -> re-applies the preferences to this page
 *   url(page)                        -> path to account/<page> from the current page
 * }
 * Event: document 'ae-account-change' with detail { user }.
 * Skipped in the PDF print mode (theme.js does not load it there).
 */
(function () {
  'use strict';

  var ACCOUNTS_KEY = 'ae_account';
  var SESSION_KEY = 'ae_session';
  var FORMULA_KEY = 'ae_formula_mode';
  var POMODORO_KEY = 'ae_pomodoro';
  var root = document.documentElement;
  var self = document.currentScript;
  var BASE = self && self.src ? self.src.replace(/assets\/js\/account\.js(\?.*)?$/, '') : '';

  var SUBJECTS = [
    { id: 'fluid-mechanics', name: 'Fluid Mechanics', short: 'Fluids', accent: '#06b6d4' },
    { id: 'aerospace-materials-1', name: 'Aerospace Materials I', short: 'Materials', accent: '#f59e0b' },
    { id: 'engineering-mechanics', name: 'Engineering Mechanics', short: 'Mechanics', accent: '#10b981' },
    { id: 'advanced-maths', name: 'Advanced Maths', short: 'Maths', accent: '#6366f1' },
    { id: 'business-management', name: 'Business Management', short: 'Management', accent: '#ef4444' }
  ];

  var SURFACE_IDS = ['default', 'cream', 'sepia', 'slate-paper', 'sage', 'charcoal'];

  function defaultPrefs() {
    return {
      subjects: [],
      primary: null,
      exams: {},
      surface: 'default',
      autoSurface: { on: false, by: 'time', day: 'cream', night: 'charcoal' },
      fontScale: 100,
      formulaMode: 'deep',
      pomodoro: 'standard'
    };
  }

  // ---- storage --------------------------------------------------------------------------
  function readJSON(key) {
    try {
      var raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : null;
    } catch (e) { return null; }
  }

  function writeJSON(key, value) {
    try {
      if (value === null) localStorage.removeItem(key);
      else localStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch (e) { return false; }
  }

  function accounts() {
    var all = readJSON(ACCOUNTS_KEY);
    return all && typeof all === 'object' && !Array.isArray(all) ? all : {};
  }

  function normEmail(email) { return String(email || '').trim().toLowerCase(); }

  function mergePrefs(prefs) {
    var out = defaultPrefs();
    if (!prefs || typeof prefs !== 'object') return out;
    if (Array.isArray(prefs.subjects)) {
      out.subjects = prefs.subjects.filter(function (id) { return findSubject(id); });
    }
    if (findSubject(prefs.primary) && out.subjects.indexOf(prefs.primary) !== -1) out.primary = prefs.primary;
    if (prefs.exams && typeof prefs.exams === 'object') {
      SUBJECTS.forEach(function (s) {
        var e = prefs.exams[s.id];
        if (e && typeof e === 'object') {
          out.exams[s.id] = { midterm: validDate(e.midterm), final: validDate(e.final) };
        }
      });
    }
    if (SURFACE_IDS.indexOf(prefs.surface) !== -1) out.surface = prefs.surface;
    var a = prefs.autoSurface;
    if (a && typeof a === 'object') {
      out.autoSurface.on = !!a.on;
      out.autoSurface.by = a.by === 'system' ? 'system' : 'time';
      if (SURFACE_IDS.indexOf(a.day) !== -1 && a.day !== 'charcoal') out.autoSurface.day = a.day;
      if (a.night === 'charcoal' || a.night === 'default') out.autoSurface.night = a.night;
    }
    var scale = Number(prefs.fontScale);
    if (scale >= 90 && scale <= 125) out.fontScale = Math.round(scale / 5) * 5;
    if (prefs.formulaMode === 'compact') out.formulaMode = 'compact';
    if (prefs.pomodoro === 'deep') out.pomodoro = 'deep';
    return out;
  }

  function validDate(v) { return /^\d{4}-\d{2}-\d{2}$/.test(v || '') ? v : ''; }

  function findSubject(id) {
    for (var i = 0; i < SUBJECTS.length; i++) if (SUBJECTS[i].id === id) return SUBJECTS[i];
    return null;
  }

  function publicUser(record) {
    if (!record) return null;
    return {
      name: record.name,
      email: record.email,
      created: record.created,
      backend: 'local',
      prefs: mergePrefs(record.prefs)
    };
  }

  function sessionRecord() {
    var session = readJSON(SESSION_KEY);
    if (!session || !session.email) return null;
    return accounts()[normEmail(session.email)] || null;
  }

  function current() { return publicUser(sessionRecord()); }

  function saveRecord(record) {
    var all = accounts();
    all[normEmail(record.email)] = record;
    if (!writeJSON(ACCOUNTS_KEY, all)) throw new Error('This browser blocks storage, so the account cannot be saved.');
  }

  function emit() {
    document.dispatchEvent(new CustomEvent('ae-account-change', { detail: { user: current() } }));
  }

  // ---- password digest (salted SHA-256; FNV-1a fallback where Web Crypto is missing) -------
  function hex(buffer) {
    var bytes = new Uint8Array(buffer), out = '';
    for (var i = 0; i < bytes.length; i++) out += (bytes[i] < 16 ? '0' : '') + bytes[i].toString(16);
    return out;
  }

  function newSalt() {
    var bytes = new Uint8Array(16);
    if (window.crypto && crypto.getRandomValues) crypto.getRandomValues(bytes);
    else for (var i = 0; i < bytes.length; i++) bytes[i] = Math.floor(Math.random() * 256);
    return hex(bytes.buffer);
  }

  function digest(password, salt) {
    var text = salt + ':' + password;
    if (window.crypto && crypto.subtle && window.TextEncoder) {
      return crypto.subtle.digest('SHA-256', new TextEncoder().encode(text)).then(function (b) { return 'sha256:' + hex(b); });
    }
    var h = 0x811c9dc5;
    for (var i = 0; i < text.length; i++) { h ^= text.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0; }
    return Promise.resolve('fnv:' + h.toString(16));
  }

  // ---- validation ---------------------------------------------------------------------------
  function checkEmail(email) {
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) throw new Error('Enter a valid email address.');
  }

  function checkPassword(password) {
    if (String(password || '').length < 8) throw new Error('The password needs at least 8 characters.');
  }

  function attempt(fn) {
    try { return Promise.resolve(fn()); } catch (e) { return Promise.reject(e); }
  }

  // ---- account operations ------------------------------------------------------------------
  function signUp(data) {
    return attempt(function () {
      var name = String(data.name || '').trim();
      var email = normEmail(data.email);
      if (!name) throw new Error('Enter the name you want to be shown.');
      checkEmail(email);
      checkPassword(data.password);
      if (accounts()[email]) throw new Error('This browser already has an account with that email. Sign in instead.');
      var salt = newSalt();
      return digest(data.password, salt).then(function (hash) {
        var prefs = defaultPrefs();
        try {
          var surface = localStorage.getItem('ae_surface');
          if (SURFACE_IDS.indexOf(surface) !== -1) prefs.surface = surface;
          var formula = localStorage.getItem(FORMULA_KEY);
          if (formula === 'compact') prefs.formulaMode = 'compact';
        } catch (e) { /* storage blocked */ }
        saveRecord({ name: name, email: email, salt: salt, hash: hash, created: new Date().toISOString(), prefs: prefs });
        writeJSON(SESSION_KEY, { email: email, since: new Date().toISOString() });
        emit();
        return current();
      });
    });
  }

  function signIn(data) {
    return attempt(function () {
      var email = normEmail(data.email);
      var record = accounts()[email];
      var fail = new Error('The email or the password is not right.');
      if (!record) throw fail;
      return digest(data.password || '', record.salt).then(function (hash) {
        if (hash !== record.hash) throw fail;
        writeJSON(SESSION_KEY, { email: email, since: new Date().toISOString() });
        emit();
        apply();
        return current();
      });
    });
  }

  function signOut() {
    writeJSON(SESSION_KEY, null);
    emit();
  }

  function update(fields) {
    return attempt(function () {
      var record = sessionRecord();
      if (!record) throw new Error('You are not signed in.');
      if (fields.name !== undefined) {
        var name = String(fields.name).trim();
        if (!name) throw new Error('The name cannot be empty.');
        record.name = name;
      }
      saveRecord(record);
      emit();
      return current();
    });
  }

  function updatePrefs(patch) {
    return attempt(function () {
      var record = sessionRecord();
      if (!record) throw new Error('You are not signed in.');
      var prefs = mergePrefs(record.prefs);
      Object.keys(patch || {}).forEach(function (k) { prefs[k] = patch[k]; });
      record.prefs = mergePrefs(prefs);
      saveRecord(record);
      apply();
      emit();
      return current();
    });
  }

  function changePassword(oldPassword, nextPassword) {
    return attempt(function () {
      var record = sessionRecord();
      if (!record) throw new Error('You are not signed in.');
      checkPassword(nextPassword);
      return digest(oldPassword || '', record.salt).then(function (hash) {
        if (hash !== record.hash) throw new Error('The current password is not right.');
        var salt = newSalt();
        return digest(nextPassword, salt).then(function (nextHash) {
          record.salt = salt;
          record.hash = nextHash;
          saveRecord(record);
          return true;
        });
      });
    });
  }

  function deleteAccount(password) {
    return attempt(function () {
      var record = sessionRecord();
      if (!record) throw new Error('You are not signed in.');
      return digest(password || '', record.salt).then(function (hash) {
        if (hash !== record.hash) throw new Error('The password is not right.');
        var all = accounts();
        delete all[normEmail(record.email)];
        writeJSON(ACCOUNTS_KEY, Object.keys(all).length ? all : null);
        writeJSON(SESSION_KEY, null);
        emit();
        return true;
      });
    });
  }

  // ---- data on this device -----------------------------------------------------------------
  var DEVICE_KEYS = [
    ['ae_bm_exams', 'Business Management simulator history'],
    ['ae_mat_exams', 'Aerospace Materials I simulator history'],
    ['ae_surface', 'Reading palette'],
    ['ae_theme', 'Light or dark mode'],
    ['ae_formula_mode', 'Formula sheet mode'],
    ['ae_pomodoro', 'Study timer'],
    ['ae_focus_lab', 'Focus Lab settings'],
    ['ae_updates', 'What’s new read state'],
    ['ae_nav', 'Side menu groups']
  ];

  function deviceData() {
    var out = [];
    DEVICE_KEYS.forEach(function (pair) {
      var raw = null;
      try { raw = localStorage.getItem(pair[0]); } catch (e) { raw = null; }
      if (raw === null) return;
      var count = null;
      try {
        var parsed = JSON.parse(raw);
        if (Array.isArray(parsed)) count = parsed.length;
      } catch (e) { /* plain string value */ }
      out.push({ key: pair[0], label: pair[1], size: raw.length, count: count });
    });
    return out;
  }

  function exportData() {
    var user = current();
    var device = {};
    DEVICE_KEYS.forEach(function (pair) {
      try {
        var raw = localStorage.getItem(pair[0]);
        if (raw === null) return;
        try { device[pair[0]] = JSON.parse(raw); } catch (e) { device[pair[0]] = raw; }
      } catch (e) { /* storage blocked */ }
    });
    return { exported: new Date().toISOString(), portal: 'Sideris', account: user, device: device };
  }

  // ---- applying the preferences to the page ------------------------------------------------
  function isNight(by) {
    if (by === 'system') return !!(window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
    var hour = new Date().getHours();
    return hour < 7 || hour >= 20;
  }

  function surfaceFor(prefs) {
    if (!prefs.autoSurface.on) return null;
    return isNight(prefs.autoSurface.by) ? prefs.autoSurface.night : prefs.autoSurface.day;
  }

  function apply() {
    var user = current();
    if (!user) {
      root.style.removeProperty('font-size');
      root.removeAttribute('data-account');
      return;
    }
    root.setAttribute('data-account', 'signed-in');
    var prefs = user.prefs;
    var target = surfaceFor(prefs);
    if (target && window.AESurface && document.querySelector('link[href*="study-surface.css"]') &&
        window.AESurface.get() !== target) {
      window.AESurface.set(target);
    }
    if (prefs.fontScale !== 100) root.style.fontSize = prefs.fontScale + '%';
    else root.style.removeProperty('font-size');
  }

  // Study preferences live in the widgets' own keys, so the timer and the formula sheets need
  // no change: the settings page writes them through these helpers.
  function writeFormulaMode(mode) {
    try { localStorage.setItem(FORMULA_KEY, mode === 'compact' ? 'compact' : 'deep'); } catch (e) { /* blocked */ }
  }

  var POMODORO_STYLES = {
    standard: { focus: 25, short: 5, long: 15, longEvery: 4 },
    deep: { focus: 50, short: 10, long: 25, longEvery: 3 }
  };

  function writePomodoroStyle(id) {
    var style = POMODORO_STYLES[id] ? id : 'standard';
    var s = POMODORO_STYLES[style];
    var state = readJSON(POMODORO_KEY);
    if (state && (state.running || state.started)) return false;   // never touch a running timer
    state = state && typeof state === 'object' ? state : { v: 1, mode: 'free', tab: 'free' };
    state.preset = style;
    state.durations = { focus: s.focus, short: s.short, long: s.long, longEvery: s.longEvery };
    state.phase = { kind: 'focus', min: s.focus };
    state.remaining = s.focus * 60000;
    state.draft = state.draft && typeof state.draft === 'object' ? state.draft : { input: '3h' };
    state.draft.style = style;
    return writeJSON(POMODORO_KEY, state);
  }

  // ---- header button -----------------------------------------------------------------------
  function url(page) { return BASE + 'account/' + (page || 'settings.html'); }

  function initials(name) {
    var parts = String(name || '').trim().split(/\s+/).filter(Boolean);
    if (!parts.length) return '?';
    var first = parts[0].charAt(0);
    var last = parts.length > 1 ? parts[parts.length - 1].charAt(0) : '';
    return (first + last).toUpperCase();
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function injectStyles() {
    if (document.querySelector('link[data-account-css]') || !BASE) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = BASE + 'assets/css/account-widget.css';
    link.setAttribute('data-account-css', '');
    document.head.appendChild(link);
  }

  var widget = null;
  var menu = null;

  function closeMenu(returnFocus) {
    if (!menu || !widget) return;
    menu.classList.remove('is-open');
    var trigger = widget.querySelector('button');
    if (trigger) trigger.setAttribute('aria-expanded', 'false');
    if (returnFocus && trigger) trigger.focus();
  }

  function buildWidget() {
    var anchor = document.getElementById('themeToggle');
    if (!anchor || !anchor.parentNode) return;
    if (widget && widget.parentNode) widget.parentNode.removeChild(widget);
    if (menu && menu.parentNode) menu.parentNode.removeChild(menu);
    widget = null;
    menu = null;

    var user = current();
    widget = el('div', 'acc-widget');
    widget.id = 'accountWidget';

    if (!user) {
      var link = el('a', 'acc-signin', 'Sign in');
      link.href = url('login.html');
      widget.appendChild(link);
    } else {
      var subject = findSubject(user.prefs.primary);
      var trigger = el('button', 'acc-avatar');
      trigger.type = 'button';
      trigger.id = 'accountButton';
      trigger.setAttribute('aria-haspopup', 'true');
      trigger.setAttribute('aria-expanded', 'false');
      trigger.setAttribute('aria-controls', 'accountMenu');
      trigger.setAttribute('aria-label', 'Account: ' + user.name);
      trigger.title = user.name;
      if (subject) trigger.style.setProperty('--acc-ring', subject.accent);
      trigger.appendChild(el('span', 'acc-avatar__initials', initials(user.name)));
      widget.appendChild(trigger);

      menu = el('div', 'acc-menu');
      menu.id = 'accountMenu';
      menu.setAttribute('role', 'menu');
      menu.setAttribute('aria-label', 'Account');
      var head = el('div', 'acc-menu__head');
      head.appendChild(el('strong', '', user.name));
      head.appendChild(el('span', '', user.email));
      menu.appendChild(head);
      [['Settings', 'settings.html'], ['Appearance', 'settings.html#appearance'], ['Subjects', 'settings.html#subjects']].forEach(function (item) {
        var a = el('a', 'acc-menu__item', item[0]);
        a.href = url(item[1]);
        a.setAttribute('role', 'menuitem');
        menu.appendChild(a);
      });
      var out = el('button', 'acc-menu__item acc-menu__item--quiet', 'Sign out');
      out.type = 'button';
      out.setAttribute('role', 'menuitem');
      out.addEventListener('click', function () { signOut(); closeMenu(false); });
      menu.appendChild(out);
      document.body.appendChild(menu);

      trigger.addEventListener('click', function () {
        if (menu.classList.contains('is-open')) { closeMenu(false); return; }
        var box = trigger.getBoundingClientRect();
        menu.classList.add('is-open');
        var width = menu.offsetWidth;
        menu.style.top = Math.round(box.bottom + 10) + 'px';
        menu.style.left = Math.round(Math.max(12, Math.min(box.right - width, window.innerWidth - width - 12))) + 'px';
        trigger.setAttribute('aria-expanded', 'true');
        var first = menu.querySelector('.acc-menu__item');
        if (first) first.focus();
      });
      menu.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') { event.stopPropagation(); closeMenu(true); }
      });
    }
    // Rightmost item of the header actions. Where the reading-palette picker is built, the button
    // goes inside its wrapper, right after the swatch: headers that spread their items
    // (space-between) keep one block of controls, and the order bell, picker, #themeToggle stays.
    var picker = document.getElementById('surfacePicker');
    if (picker) picker.appendChild(widget);
    else anchor.parentNode.insertBefore(widget, anchor.nextSibling);
  }

  document.addEventListener('click', function (event) {
    if (!menu || !menu.classList.contains('is-open')) return;
    if (!menu.contains(event.target) && !(widget && widget.contains(event.target))) closeMenu(false);
  });
  window.addEventListener('resize', function () { closeMenu(false); });

  // On palette pages the button goes inside the picker, which theme.js builds on DOMContentLoaded:
  // wait for it (some pages load theme.js late) instead of falling back to another place.
  function start(tries) {
    tries = tries || 0;
    var wantsPicker = !!document.querySelector('link[href*="study-surface.css"]') && !!document.getElementById('themeToggle');
    if (wantsPicker && !document.getElementById('surfacePicker') && tries < 40) {
      setTimeout(function () { start(tries + 1); }, 25);
      return;
    }
    injectStyles();
    buildWidget();
    apply();
  }

  document.addEventListener('ae-account-change', function () { buildWidget(); });
  // Another tab signed in or out, or changed the preferences.
  window.addEventListener('storage', function (event) {
    if (event.key === SESSION_KEY || event.key === ACCOUNTS_KEY) { buildWidget(); apply(); }
  });

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { start(0); });
  else start(0);

  window.AEAccount = {
    SUBJECTS: SUBJECTS,
    SURFACES: SURFACE_IDS,
    backend: 'local',
    current: current,
    signUp: signUp,
    signIn: signIn,
    signOut: signOut,
    update: update,
    updatePrefs: updatePrefs,
    changePassword: changePassword,
    deleteAccount: deleteAccount,
    exportData: exportData,
    deviceData: deviceData,
    apply: apply,
    url: url,
    initials: initials,
    writeFormulaMode: writeFormulaMode,
    writePomodoroStyle: writePomodoroStyle
  };
})();
