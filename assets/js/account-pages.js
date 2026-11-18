/*!
 * Sideris portal: behaviour of the account pages (account/login.html, signup.html, settings.html).
 * Needs window.AEAccount (assets/js/account.js, loaded by theme.js) and window.AESurface (theme.js).
 * The page says which one it is with <body data-page="login|signup|settings">.
 */
(function () {
  'use strict';

  var ICONS = {
    'fluid-mechanics': '<path d="M3 13.2c3-3.2 8-4.3 12.5-3.1 2.4.6 4.3 1.7 5.5 3.1-2 .8-5 1.2-8.5 1.2-4 0-7.5-.4-9.5-1.2z" fill="currentColor" fill-opacity="0.18"/><path d="M2 7.6c4-2.2 9-2.6 13.5-1.2 2.5.8 4.6 2 6.5 3.5"/><path d="M2 18.4c4 .9 9 1 13.5.4 2.4-.3 4.6-.9 6.5-1.6"/>',
    'aerospace-materials-1': '<path d="M12 3l7.5 4.3v8.6L12 20.2l-7.5-4.3V7.3z"/><path d="M12 11.6l7.5-4.3M12 11.6L4.5 7.3M12 11.6v8.6"/><circle cx="12" cy="3" r="1.3" fill="currentColor"/><circle cx="19.5" cy="7.3" r="1.3" fill="currentColor"/><circle cx="4.5" cy="7.3" r="1.3" fill="currentColor"/><circle cx="12" cy="11.6" r="1.3" fill="currentColor"/><circle cx="12" cy="20.2" r="1.3" fill="currentColor"/>',
    'engineering-mechanics': '<path d="M10.26 5.01L10.42 2.53L13.58 2.53L13.74 5.01L15.71 5.83L17.58 4.19L19.81 6.42L18.17 8.29L18.99 10.26L21.47 10.42L21.47 13.58L18.99 13.74L18.17 15.71L19.81 17.58L17.58 19.81L15.71 18.17L13.74 18.99L13.58 21.47L10.42 21.47L10.26 18.99L8.29 18.17L6.42 19.81L4.19 17.58L5.83 15.71L5.01 13.74L2.53 13.58L2.53 10.42L5.01 10.26L5.83 8.29L4.19 6.42L6.42 4.19L8.29 5.83z"/><circle cx="12" cy="12" r="3"/>',
    'advanced-maths': '<path d="M15.6 4.3c-2-.9-3.3.2-3.5 2.3l-.5 10.8c-.2 2.1-1.5 3.2-3.5 2.3"/><path d="M15.8 13.2c.9-1.3 2.2-1.3 2.9 0l.6 1.6c.6 1.3 1.6 1.3 2.2.2"/><path d="M21.2 12.4l-5.2 5.2"/><path d="M3 9.5h4.2M5.1 7.4v4.2"/>',
    'business-management': '<path d="M4 20.5h16"/><path d="M6.5 20.5v-4.5M11 20.5v-7.5M15.5 20.5v-10.5"/><path d="M4.5 10l5-3.6 3.5 2L19 3.8"/><path d="M15.6 3.6h3.6v3.6"/>'
  };

  var META = {
    'fluid-mechanics': '7 topics · Navier-Stokes, hydrostatics',
    'aerospace-materials-1': 'Midterm 2 test bank',
    'engineering-mechanics': 'Kinematics to rigid bodies',
    'advanced-maths': 'ODEs and planar systems',
    'business-management': 'Financial statements'
  };

  // Mini previews of the reading palettes (the colours of assets/css/study-surface.css).
  var PALETTES = [
    { id: 'default', label: 'Default', mode: 'Portal', split: true },
    { id: 'cream', label: 'Cream', mode: 'Light', bg: '#f5f2eb', card: '#ffffff', inset: '#ece8df', text: '#23272f', text2: '#474b56', border: 'rgba(43,45,49,0.12)' },
    { id: 'sepia', label: 'Sepia', mode: 'Light', bg: '#efe8d8', card: '#f7f2e4', inset: '#e5dcb7', text: '#342a22', text2: '#4d4137', border: 'rgba(60,48,38,0.14)' },
    { id: 'slate-paper', label: 'Slate paper', mode: 'Light', bg: '#eceff2', card: '#f6f8fa', inset: '#e2e6eb', text: '#1a222d', text2: '#414a58', border: 'rgba(26,34,45,0.12)' },
    { id: 'sage', label: 'Sage', mode: 'Light', bg: '#ebf0ea', card: '#f4f7f3', inset: '#e1e8e0', text: '#1f2922', text2: '#404d43', border: 'rgba(31,41,34,0.12)' },
    { id: 'charcoal', label: 'Charcoal', mode: 'Dark', bg: '#111620', card: '#18202f', inset: '#141a26', text: '#dde4ec', text2: '#9fadc0', border: 'rgba(255,255,255,0.08)' }
  ];

  var TICK = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>';

  function $(sel, scope) { return (scope || document).querySelector(sel); }
  function $$(sel, scope) { return Array.prototype.slice.call((scope || document).querySelectorAll(sel)); }

  function esc(text) {
    return String(text).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function showError(box, error) {
    if (!box) return;
    box.textContent = error ? (error.message || String(error)) : '';
    box.classList.toggle('is-shown', !!error);
  }

  var toastTimer = null;
  function toast(text) {
    var node = $('#accToast');
    if (!node) return;
    node.innerHTML = '<b>Saved</b>' + esc(text || '');
    node.classList.add('is-shown');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { node.classList.remove('is-shown'); }, 1800);
  }

  function nextUrl() {
    var match = /[?&]next=([^&]+)/.exec(location.search);
    if (!match) return '../index.html';
    var target = decodeURIComponent(match[1]);
    // only paths inside the portal
    return /^(\.\.\/|[a-z0-9_-]+\/)[^:]*$/i.test(target) && target.indexOf('//') === -1 ? target : '../index.html';
  }

  // ---- shared pieces ----------------------------------------------------------------------
  function wirePasswordToggles() {
    $$('.acc-pw__toggle').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var input = btn.parentNode.querySelector('input');
        var show = input.type === 'password';
        input.type = show ? 'text' : 'password';
        btn.textContent = show ? 'Hide' : 'Show';
        btn.setAttribute('aria-pressed', String(show));
      });
    });
  }

  function strength(pw) {
    var score = 0;
    if (pw.length >= 8) score++;
    if (pw.length >= 12) score++;
    if (/[A-Z]/.test(pw) && /[a-z]/.test(pw)) score++;
    if (/\d/.test(pw) && /[^A-Za-z0-9]/.test(pw)) score++;
    return pw ? Math.max(1, score) : 0;
  }

  function renderSubjects(container, selected, onChange) {
    container.innerHTML = '';
    AEAccount.SUBJECTS.forEach(function (s) {
      var label = document.createElement('label');
      label.className = 'acc-subject' + (selected.indexOf(s.id) !== -1 ? ' is-on' : '');
      label.style.setProperty('--dot', s.accent);
      label.innerHTML =
        '<input type="checkbox" value="' + s.id + '"' + (selected.indexOf(s.id) !== -1 ? ' checked' : '') + '>' +
        '<span class="acc-subject__icon" aria-hidden="true"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">' + ICONS[s.id] + '</svg></span>' +
        '<span><span class="acc-subject__name">' + esc(s.name) + '</span><span class="acc-subject__meta">' + esc(META[s.id]) + '</span></span>' +
        '<span class="acc-subject__tick" aria-hidden="true">' + TICK + '</span>';
      var input = label.querySelector('input');
      input.addEventListener('change', function () {
        label.classList.toggle('is-on', input.checked);
        onChange($$('input:checked', container).map(function (i) { return i.value; }));
      });
      container.appendChild(label);
    });
  }

  function renderSwatches(container, current, onPick) {
    container.innerHTML = '';
    container.setAttribute('role', 'radiogroup');
    PALETTES.forEach(function (p) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'acc-swatch-card';
      btn.setAttribute('role', 'radio');
      btn.setAttribute('data-surface', p.id);
      btn.setAttribute('aria-checked', String(p.id === current));
      btn.setAttribute('aria-label', p.label + ' palette');
      var style = p.split ? '' : ' style="--m-bg:' + p.bg + ';--m-card:' + p.card + ';--m-inset:' + p.inset + ';--m-text:' + p.text + ';--m-text-2:' + p.text2 + ';--m-border:' + p.border + '"';
      btn.innerHTML =
        '<span class="acc-mini' + (p.split ? ' acc-mini--split' : '') + '"' + style + ' aria-hidden="true">' +
          '<span class="acc-mini__card"><span class="acc-mini__title"></span><span class="acc-mini__line"></span><span class="acc-mini__line"></span><span class="acc-mini__line"></span>' +
          (p.split ? '' : '<span class="acc-mini__eq">F = ma</span>') + '</span></span>' +
        '<span class="acc-swatch-card__name">' + esc(p.label) + '<small>' + esc(p.mode) + '</small></span>';
      btn.addEventListener('click', function () {
        $$('.acc-swatch-card', container).forEach(function (b) { b.setAttribute('aria-checked', String(b === btn)); });
        onPick(p.id);
      });
      container.appendChild(btn);
    });
    container.addEventListener('keydown', function (event) {
      var step = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[event.key];
      var cards = $$('.acc-swatch-card', container);
      var index = cards.indexOf(document.activeElement);
      if (!step || index < 0) return;
      event.preventDefault();
      cards[(index + step + cards.length) % cards.length].focus();
    });
  }

  function renderDates(container, subjects, exams, onChange) {
    container.innerHTML = '';
    if (!subjects.length) {
      container.innerHTML = '<p class="acc-hint">Choose your subjects first; their exam dates go here.</p>';
      return;
    }
    subjects.forEach(function (id) {
      var s = null;
      AEAccount.SUBJECTS.forEach(function (x) { if (x.id === id) s = x; });
      if (!s) return;
      var e = exams[id] || { midterm: '', final: '' };
      var row = document.createElement('div');
      row.className = 'acc-date-row';
      row.style.setProperty('--dot', s.accent);
      row.innerHTML =
        '<div class="acc-date-row__name"><i aria-hidden="true"></i>' + esc(s.name) + '</div>' +
        '<div><label class="acc-label" for="mid-' + id + '">Midterm</label><input class="acc-input" type="date" id="mid-' + id + '" value="' + esc(e.midterm || '') + '"></div>' +
        '<div><label class="acc-label" for="fin-' + id + '">Final exam</label><input class="acc-input" type="date" id="fin-' + id + '" value="' + esc(e.final || '') + '"></div>';
      $$('input', row).forEach(function (input) {
        input.addEventListener('change', function () {
          exams[id] = { midterm: $('#mid-' + id).value, final: $('#fin-' + id).value };
          onChange(exams);
        });
      });
      container.appendChild(row);
    });
  }

  function seg(container, value, onPick) {
    $$('button', container).forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-value') === value));
      b.addEventListener('click', function () {
        $$('button', container).forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        onPick(b.getAttribute('data-value'));
      });
    });
  }

  // ---- login ----------------------------------------------------------------------------------
  function initLogin() {
    var form = $('#loginForm');
    var error = $('#loginError');
    wirePasswordToggles();
    var user = AEAccount.current();
    if (user) $('#alreadyIn').hidden = false, $('#alreadyName').textContent = user.name;
    $('#forgotBtn').addEventListener('click', function () { $('#forgotNote').hidden = !$('#forgotNote').hidden; });
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      showError(error, null);
      var submit = $('button[type="submit"]', form);
      submit.disabled = true;
      AEAccount.signIn({ email: form.email.value, password: form.password.value }).then(function () {
        location.href = nextUrl();
      }, function (err) {
        submit.disabled = false;
        showError(error, err);
        form.password.setAttribute('aria-invalid', 'true');
        form.password.focus();
      });
    });
  }

  // ---- signup + onboarding -------------------------------------------------------------------
  function initSignup() {
    var form = $('#signupForm');
    var error = $('#signupError');
    var meter = $('#pwMeter');
    wirePasswordToggles();
    form.password.addEventListener('input', function () {
      meter.setAttribute('data-level', String(strength(form.password.value)));
    });

    var draft = { subjects: [], exams: {}, surface: AESurface.get() };
    var step = 0;
    var panes = ['#stepAccount', '#stepSubjects', '#stepLook', '#stepDates', '#stepDone'];

    function go(n) {
      step = n;
      panes.forEach(function (sel, i) { $(sel).hidden = i !== n; });
      $$('.acc-steps__bar span').forEach(function (bar, i) { bar.classList.toggle('is-done', i < n); });
      $('#stepCount').textContent = n >= 1 && n <= 3 ? 'Step ' + n + ' of 3' : '';
      $('#wizardSteps').hidden = n < 1 || n > 3;
      var heading = $(panes[n] + ' h2');
      if (heading) { heading.setAttribute('tabindex', '-1'); heading.focus({ preventScroll: true }); }
      window.scrollTo({ top: 0, behavior: 'smooth' });
      if (n === 3) renderDates($('#datesList'), draft.subjects, draft.exams, function (exams) { draft.exams = exams; });
      if (n === 4) summary();
    }

    function save() {
      return AEAccount.updatePrefs({
        subjects: draft.subjects,
        primary: draft.subjects[0] || null,
        exams: draft.exams,
        surface: draft.surface
      });
    }

    function summary() {
      var user = AEAccount.current();
      $('#doneName').textContent = user ? user.name.split(' ')[0] : '';
      var names = AEAccount.SUBJECTS.filter(function (s) { return draft.subjects.indexOf(s.id) !== -1; }).map(function (s) { return s.short; });
      $('#doneSubjects').textContent = names.length ? names.join(', ') : 'none yet';
      var pal = PALETTES.filter(function (p) { return p.id === draft.surface; })[0];
      $('#donePalette').textContent = pal ? pal.label : 'Default';
    }

    // Keep the order of the clicks: the first subject picked becomes the main one.
    function onSubjects(list) {
      draft.subjects = draft.subjects.filter(function (id) { return list.indexOf(id) !== -1; })
        .concat(list.filter(function (id) { return draft.subjects.indexOf(id) === -1; }));
      $('#subjectsNext').textContent = list.length ? 'Continue with ' + list.length + (list.length === 1 ? ' subject' : ' subjects') : 'Continue';
    }
    renderSubjects($('#subjectList'), draft.subjects, onSubjects);
    renderSwatches($('#swatchList'), draft.surface, function (id) {
      draft.surface = id;
      AESurface.set(id);
    });

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      showError(error, null);
      $$('.acc-input', form).forEach(function (i) { i.removeAttribute('aria-invalid'); });
      if (!form.terms.checked) { showError(error, new Error('Please accept how your data is kept to continue.')); return; }
      var submit = $('button[type="submit"]', form);
      submit.disabled = true;
      AEAccount.signUp({ name: form.elements['name'].value, email: form.email.value, password: form.password.value }).then(function () {
        go(1);
      }, function (err) {
        submit.disabled = false;
        showError(error, err);
        var field = /email/i.test(err.message) ? form.email : /password/i.test(err.message) ? form.password : /name/i.test(err.message) ? form.elements['name'] : null;
        if (field) { field.setAttribute('aria-invalid', 'true'); field.focus(); }
      });
    });

    $$('[data-go]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var target = Number(btn.getAttribute('data-go'));
        if (target > step && step >= 1) save();
        go(target);
      });
    });

    // Signed in already: straight to the set-up steps (useful to redo them).
    if (AEAccount.current()) {
      var prefs = AEAccount.current().prefs;
      draft.subjects = prefs.subjects.slice();
      draft.exams = prefs.exams;
      renderSubjects($('#subjectList'), draft.subjects, onSubjects);
      go(/[?&]step=(\d)/.test(location.search) ? Number(RegExp.$1) : 1);
    }
  }

  // ---- settings --------------------------------------------------------------------------------
  function initSettings() {
    var user = AEAccount.current();
    if (!user) {
      $('#settingsGate').hidden = false;
      $('#settingsApp').hidden = true;
      return;
    }
    $('#settingsGate').hidden = true;
    $('#settingsApp').hidden = false;
    wirePasswordToggles();

    function prefs() { return AEAccount.current().prefs; }
    function savePrefs(patch, label) {
      return AEAccount.updatePrefs(patch).then(function () { toast(label); refreshChip(); });
    }

    // profile chip + avatar
    function refreshChip() {
      var u = AEAccount.current();
      if (!u) return;
      var primary = AEAccount.SUBJECTS.filter(function (s) { return s.id === u.prefs.primary; })[0];
      $$('.acc-big-avatar').forEach(function (a) {
        a.textContent = AEAccount.initials(u.name);
        if (primary) a.style.setProperty('--acc-ring', primary.accent); else a.style.removeProperty('--acc-ring');
      });
      $('#chipName').textContent = u.name;
      $('#chipEmail').textContent = u.email;
    }
    refreshChip();

    // Profile
    var nameForm = $('#nameForm');
    nameForm.elements['name'].value = user.name;
    $('#emailField').value = user.email;
    $('#memberSince').textContent = new Date(user.created).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' });
    nameForm.addEventListener('submit', function (event) {
      event.preventDefault();
      AEAccount.update({ name: nameForm.elements['name'].value }).then(function () { toast('Name updated'); refreshChip(); }, function (err) { showError($('#nameError'), err); });
    });
    var pwForm = $('#passwordForm');
    pwForm.addEventListener('submit', function (event) {
      event.preventDefault();
      showError($('#passwordError'), null);
      AEAccount.changePassword(pwForm.current.value, pwForm.next.value).then(function () {
        pwForm.reset();
        toast('Password changed');
      }, function (err) { showError($('#passwordError'), err); });
    });
    $('#signOutBtn').addEventListener('click', function () { AEAccount.signOut(); location.href = '../index.html'; });

    // Subjects
    var primarySelect = $('#primarySelect');
    function fillPrimary() {
      var p = prefs();
      primarySelect.innerHTML = '';
      if (!p.subjects.length) {
        primarySelect.innerHTML = '<option value="">Choose a subject above first</option>';
        primarySelect.disabled = true;
        return;
      }
      primarySelect.disabled = false;
      AEAccount.SUBJECTS.forEach(function (s) {
        if (p.subjects.indexOf(s.id) === -1) return;
        var o = document.createElement('option');
        o.value = s.id;
        o.textContent = s.name;
        o.selected = s.id === p.primary;
        primarySelect.appendChild(o);
      });
    }
    function fillDates() {
      var p = prefs();
      renderDates($('#datesList'), p.subjects, p.exams, function (exams) { savePrefs({ exams: exams }, 'Exam dates'); });
    }
    renderSubjects($('#subjectList'), prefs().subjects, function (list) {
      var p = prefs();
      var primary = list.indexOf(p.primary) !== -1 ? p.primary : (list[0] || null);
      savePrefs({ subjects: list, primary: primary }, 'Subjects').then(function () { fillPrimary(); fillDates(); });
    });
    primarySelect.addEventListener('change', function () { savePrefs({ primary: primarySelect.value }, 'Main subject'); });
    fillPrimary();
    fillDates();

    // Appearance
    var swatches = $('#swatchList');
    renderSwatches(swatches, AESurface.get(), function (id) {
      AESurface.set(id);
      var auto = prefs().autoSurface;
      if (auto.on) { auto.on = false; $('#autoToggle').checked = false; syncAuto(); }
      savePrefs({ surface: id, autoSurface: auto }, 'Reading palette');
    });
    document.addEventListener('ae-surface-change', function (event) {
      $$('.acc-swatch-card', swatches).forEach(function (b) { b.setAttribute('aria-checked', String(b.getAttribute('data-surface') === event.detail.surface)); });
    });

    var autoToggle = $('#autoToggle');
    var autoBox = $('#autoOptions');
    function syncAuto() { autoBox.hidden = !autoToggle.checked; }
    var a = prefs().autoSurface;
    autoToggle.checked = a.on;
    $('#daySelect').value = a.day;
    $('#nightSelect').value = a.night;
    syncAuto();
    function saveAuto() {
      var next = { on: autoToggle.checked, by: $('#autoBy [aria-pressed="true"]').getAttribute('data-value'), day: $('#daySelect').value, night: $('#nightSelect').value };
      syncAuto();
      savePrefs({ autoSurface: next }, next.on ? 'Automatic palette on' : 'Automatic palette off');
    }
    autoToggle.addEventListener('change', saveAuto);
    seg($('#autoBy'), a.by, saveAuto);
    $('#daySelect').addEventListener('change', saveAuto);
    $('#nightSelect').addEventListener('change', saveAuto);

    var range = $('#fontRange');
    var out = $('#fontOut');
    range.value = prefs().fontScale;
    out.textContent = range.value + '%';
    range.addEventListener('input', function () {
      out.textContent = range.value + '%';
      document.documentElement.style.fontSize = range.value + '%';
    });
    range.addEventListener('change', function () { savePrefs({ fontScale: Number(range.value) }, 'Text size'); });
    $('#fontReset').addEventListener('click', function () {
      range.value = 100;
      out.textContent = '100%';
      savePrefs({ fontScale: 100 }, 'Text size');
    });

    // Study
    seg($('#formulaSeg'), prefs().formulaMode, function (v) {
      AEAccount.writeFormulaMode(v);
      savePrefs({ formulaMode: v }, 'Formula sheet mode');
    });
    seg($('#pomodoroSeg'), prefs().pomodoro, function (v) {
      var applied = AEAccount.writePomodoroStyle(v);
      savePrefs({ pomodoro: v }, applied ? 'Timer style' : 'Timer style (after the running block)');
    });

    // Privacy and data
    function fillData() {
      var list = $('#dataList');
      var rows = AEAccount.deviceData();
      list.innerHTML = rows.length ? '' : '<li>Nothing stored yet on this device.</li>';
      rows.forEach(function (r) {
        var li = document.createElement('li');
        var detail = r.count !== null ? r.count + (r.count === 1 ? ' entry' : ' entries') : (r.size < 1024 ? r.size + ' B' : (r.size / 1024).toFixed(1) + ' kB');
        li.innerHTML = '<span>' + esc(r.label) + ' <code>' + esc(r.key) + '</code></span><code>' + esc(detail) + '</code>';
        list.appendChild(li);
      });
    }
    fillData();
    $('#exportBtn').addEventListener('click', function () {
      var blob = new Blob([JSON.stringify(AEAccount.exportData(), null, 2)], { type: 'application/json' });
      var link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'sideris-my-data.json';
      document.body.appendChild(link);
      link.click();
      setTimeout(function () { URL.revokeObjectURL(link.href); link.remove(); }, 0);
      toast('Export ready');
    });
    var dialog = $('#deleteDialog');
    $('#deleteBtn').addEventListener('click', function () {
      showError($('#deleteError'), null);
      if (dialog.showModal) dialog.showModal(); else dialog.setAttribute('open', '');
      $('#deletePassword').focus();
    });
    $('#deleteCancel').addEventListener('click', function () { dialog.close(); });
    $('#deleteForm').addEventListener('submit', function (event) {
      event.preventDefault();
      AEAccount.deleteAccount($('#deletePassword').value).then(function () {
        location.href = '../index.html';
      }, function (err) { showError($('#deleteError'), err); });
    });

    // Side navigation: scroll-spy
    var links = $$('.acc-nav a');
    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          links.forEach(function (l) { l.setAttribute('aria-current', String(l.getAttribute('href') === '#' + entry.target.id)); });
        });
      }, { rootMargin: '-30% 0px -60% 0px' });
      $$('.acc-section').forEach(function (s) { observer.observe(s); });
    }
  }

  function start() {
    if (!window.AEAccount || !window.AESurface) { setTimeout(start, 30); return; }
    var page = document.body.getAttribute('data-page');
    if (page === 'login') initLogin();
    else if (page === 'signup') initSignup();
    else if (page === 'settings') initSettings();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
