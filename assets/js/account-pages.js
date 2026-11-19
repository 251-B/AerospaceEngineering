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

  // The constellation of the sign-in pages: a subject's star (and the line between two lit
  // stars) lights up when the subject is chosen.
  function lightStars(list) {
    $$('.acc-star').forEach(function (g) { g.classList.toggle('is-lit', list.indexOf(g.getAttribute('data-star')) !== -1); });
    $$('.acc-sky__lines line').forEach(function (l) {
      l.classList.toggle('is-lit', list.indexOf(l.getAttribute('data-a')) !== -1 && list.indexOf(l.getAttribute('data-b')) !== -1);
    });
  }

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
  // ---- the sky of the sign-in pages ---------------------------------------------------------
  var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function initSky() {
    var clock = $('#accClock');
    function tick() {
      var d = new Date();
      if (clock) clock.textContent = (d.getHours() < 10 ? '0' : '') + d.getHours() + ':' + (d.getMinutes() < 10 ? '0' : '') + d.getMinutes();
    }
    tick();
    setInterval(tick, 20000);
    // Gentle parallax: far dust, near dust and the map drift at three depths with the pointer.
    var sky = $('.acc-sky');
    if (!sky || REDUCED || !window.matchMedia('(pointer: fine)').matches) return;
    var layers = [['.acc-sky__layer--far', 6], ['.acc-sky__layer--near', 14], ['.acc-sky__stage', 9]].map(function (l) {
      return [$(l[0]), l[1]];
    });
    var frame = 0;
    document.addEventListener('pointermove', function (event) {
      if (frame) return;
      frame = requestAnimationFrame(function () {
        frame = 0;
        var dx = event.clientX / window.innerWidth - 0.5, dy = event.clientY / window.innerHeight - 0.5;
        layers.forEach(function (l) {
          if (l[0]) l[0].style.transform = 'translate3d(' + (-dx * l[1]).toFixed(2) + 'px,' + (-dy * l[1]).toFixed(2) + 'px,0)';
        });
      });
    });
  }

  // Lock the telescope onto the star of an email (or let it go when the email is not valid).
  var lockedId = null;
  function lockStar(email) {
    var me = $('#accMe'), pos = $('#accMePos'), target = $('#accTarget');
    if (!me || !pos) return null;
    var valid = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(email || '').trim());
    var star = valid ? AEAccount.starFor(email) : null;
    if (!star) {
      me.classList.remove('is-locked');
      lockedId = null;
      if (target) target.textContent = 'Scanning';
      return null;
    }
    if (star.id === lockedId) return star;
    lockedId = star.id;
    pos.setAttribute('transform', 'translate(' + star.x + ' ' + star.y + ')');
    me.classList.remove('is-locked');
    void me.getBoundingClientRect();   // restart the lock animation
    me.classList.add('is-locked');
    if (target) target.textContent = star.id;
    return star;
  }

  function watchEmail(input) {
    var timer = 0;
    input.addEventListener('input', function () {
      clearTimeout(timer);
      timer = setTimeout(function () { lockStar(input.value); }, 260);
    });
  }

  function launch(then) {
    var main = $('.acc-auth');
    if (main) main.classList.add('is-launch');
    setTimeout(then, REDUCED ? 0 : 850);
  }

  function initLogin() {
    initSky();
    lightStars(AEAccount.SUBJECTS.map(function (x) { return x.id; }));
    var form = $('#loginForm');
    var error = $('#loginError');
    wirePasswordToggles();
    watchEmail(form.email);
    var user = AEAccount.current();
    if (user) $('#alreadyIn').hidden = false, $('#alreadyName').textContent = user.name;
    // The browser remembers the last account: greet it by name and find its star at once.
    var last = AEAccount.lastAccount();
    if (last && !user) {
      form.email.value = last.email;
      $('#loginTitle').textContent = 'Welcome back, ' + last.name.split(' ')[0] + '.';
      $('#loginSub').hidden = true;
      $('#loginKnown').hidden = false;
      lockStar(last.email);
      setTimeout(function () { form.password.focus(); }, 60);
    }
    $('#notYou').addEventListener('click', function () {
      AEAccount.forgetLast();
      form.reset();
      lockStar('');
      $('#loginTitle').textContent = 'Sign in';
      $('#loginSub').hidden = false;
      $('#loginKnown').hidden = true;
      form.email.focus();
    });
    $('#forgotBtn').addEventListener('click', function () {
      if (AEAccount.backend === 'supabase') {
        var note = $('#forgotNote');
        note.hidden = false;
        if (!form.email.value) { note.textContent = 'Write your email above, then press "Forgot it?" again.'; form.email.focus(); return; }
        note.textContent = 'Sending...';
        AEAccount.recoverPassword(form.email.value).then(function () {
          note.textContent = 'If that email has an account, a link to set a new password is on its way.';
        }, function (err) { note.textContent = err.message; });
        return;
      }
      $('#forgotNote').hidden = !$('#forgotNote').hidden;
    });
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      showError(error, null);
      var submit = $('button[type="submit"]', form);
      submit.disabled = true;
      AEAccount.signIn({ email: form.email.value, password: form.password.value }).then(function () {
        lockStar(form.email.value);
        launch(function () { location.href = nextUrl(); });
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
    initSky();
    wirePasswordToggles();
    watchEmail(form.email);
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
      $('#doneSubjects').textContent = names.length ? names.join(', ') : 'No subjects yet';
      var pal = PALETTES.filter(function (p) { return p.id === draft.surface; })[0];
      $('#donePalette').textContent = (pal ? pal.label : 'Default') + ' palette';
    }

    // Keep the order of the clicks: the first subject picked becomes the main one.
    function onSubjects(list) {
      draft.subjects = draft.subjects.filter(function (id) { return list.indexOf(id) !== -1; })
        .concat(list.filter(function (id) { return draft.subjects.indexOf(id) === -1; }));
      lightStars(draft.subjects);
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
      AEAccount.signUp({ name: form.elements['name'].value, email: form.email.value, password: form.password.value,
                         invite: form.invite ? form.invite.value : '' }).then(function (res) {
        if (res && res.pending) {
          submit.disabled = false;
          showError(error, null);
          $('#signupDone').hidden = false;
          $('#signupDone').textContent = 'Almost there: open the email we sent to ' + res.email + ' to confirm it, then sign in.';
          return;
        }
        go(1);
      }, function (err) {
        submit.disabled = false;
        showError(error, err);
        var field = /invite/i.test(err.message) ? form.invite : /email/i.test(err.message) ? form.email : /password/i.test(err.message) ? form.password : /name/i.test(err.message) ? form.elements['name'] : null;
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
      lightStars(draft.subjects);
      renderSubjects($('#subjectList'), draft.subjects, onSubjects);
      lockStar(AEAccount.current().email);
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
    var goalRange = $('#goalRange'), goalOut = $('#goalOut');
    function goalText(v) { return +v ? v + ' h' : 'Off'; }
    goalRange.value = prefs().weeklyGoal;
    goalOut.textContent = goalText(goalRange.value);
    goalRange.addEventListener('input', function () { goalOut.textContent = goalText(goalRange.value); });
    goalRange.addEventListener('change', function () { savePrefs({ weeklyGoal: Number(goalRange.value) }, 'Weekly goal'); });

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

  // ---- My study (account/dashboard.html) ------------------------------------------------------
  // Subject colours for the marks of the charts (validated for colour-vision deficiency on the
  // dark and the light card); text never takes them.
  // One family: the same chroma (OKLCH C 0.135) and staggered lightness, so the five hues sit
  // together; every pair separates for colour-vision deficiency (worst all-pairs dE 9.2) and for
  // normal vision (15.6) on the dark card and on every light palette.
  var MARK_SET = { 'fluid-mechanics': '#008bbc', 'aerospace-materials-1': '#bc7b04', 'engineering-mechanics': '#36ac73', 'advanced-maths': '#6651a9', 'business-management': '#b14955' };
  var MARK = { dark: MARK_SET, light: MARK_SET };
  var SIM_KEYS = { 'business-management': 'ae_bm_exams', 'aerospace-materials-1': 'ae_mat_exams', 'advanced-maths': 'ae_am_exams', 'engineering-mechanics': 'ae_em_exams' };

  function markColour(id) {
    return MARK[document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark'][id];
  }

  function duration(sec) {
    var min = Math.round(sec / 60);
    if (min < 60) return min + ' min';
    var h = Math.floor(min / 60), m = min % 60;
    return h + ' h' + (m ? ' ' + m + ' min' : '');
  }

  function ago(ms) {
    var min = Math.round((Date.now() - ms) / 60000);
    if (min < 1) return 'just now';
    if (min < 60) return min + ' min ago';
    var h = Math.round(min / 60);
    if (h < 24) return h + ' h ago';
    var d = Math.round(h / 24);
    return d === 1 ? 'yesterday' : d + ' days ago';
  }

  function readStore(key) {
    try { return JSON.parse(localStorage.getItem(key) || 'null'); } catch (e) { return null; }
  }

  function lastDays(n) {
    var out = [];
    for (var i = n - 1; i >= 0; i--) {
      var d = new Date();
      d.setHours(12, 0, 0, 0);
      d.setDate(d.getDate() - i);
      out.push(d);
    }
    return out;
  }

  function initDashboard() {
    var user = AEAccount.current();
    if (!user) { $('#studyGate').hidden = false; return; }
    $('#studyApp').hidden = false;
    var prefs = user.prefs;
    var nextBox = $('#nextClass');
    if (nextBox && window.AECalendarUI && window.AECalendar) {
      var now = new Date();
      var localNow = new Date(now.getTime() - now.getTimezoneOffset() * 60000).toISOString();
      AECalendarUI.nextCard(nextBox, { rec: AECalendar.load(), prefs: prefs, today: localNow.slice(0, 10), now: localNow.slice(11, 16), base: '../' });
    }
    var subjects = AEAccount.SUBJECTS.slice().sort(function (a, b) {
      var ia = prefs.subjects.indexOf(a.id), ib = prefs.subjects.indexOf(b.id);
      return (ia < 0 ? 99 : ia) - (ib < 0 ? 99 : ib);
    });
    var byId = {};
    AEAccount.SUBJECTS.forEach(function (s) { byId[s.id] = s; });
    var log = AEAccount.studyLog();
    var days = lastDays(7);
    var week = days.map(function (d) { return log.days[AEAccount.dayKey(d)] || {}; });
    var weekTotal = week.reduce(function (sum, day) {
      return sum + Object.keys(day).reduce(function (s, k) { return s + day[k]; }, 0);
    }, 0);

    // streak: consecutive days with at least 10 minutes, ending today (or yesterday)
    var streak = 0;
    for (var i = 0; i < 70; i++) {
      var d = new Date(); d.setDate(d.getDate() - i);
      var rec = log.days[AEAccount.dayKey(d)] || {};
      var sec = Object.keys(rec).reduce(function (s, k) { return s + rec[k]; }, 0);
      if (sec >= 600) streak++;
      else if (i > 0) break;
    }

    // hero
    var now = new Date();
    var hour = now.getHours();
    var greet = hour < 6 ? 'Good night' : hour < 12 ? 'Good morning' : hour < 20 ? 'Good afternoon' : 'Good evening';
    $('#studyDate').textContent = now.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' });
    $('#studyTitle').textContent = greet + ', ' + user.name.split(' ')[0] + '.';
    var next = AEAccount.nextExam(prefs);
    $('#studyLine').textContent = next
      ? AEAccount.examPhrase(next) + '. ' + (weekTotal ? 'Keep the rhythm.' : 'A good week to start.')
      : 'Add your exam dates and the countdowns appear here.';
    $('#statWeek').textContent = duration(weekTotal) + (prefs.weeklyGoal ? ' / ' + prefs.weeklyGoal + ' h' : '');
    $('#statStreak').textContent = streak + (streak === 1 ? ' day' : ' days');
    $('#statNext').textContent = next ? (next.days === 0 ? 'Today' : next.days + (next.days === 1 ? ' day' : ' days')) : '-';
    $('#statNextLabel').textContent = next ? 'to ' + next.subject.short + ' ' + next.kind : 'next exam';

    // continue where you left off
    var recent = AEAccount.recentPages();
    var list = $('#continueList');
    var rows = Object.keys(recent).filter(function (k) { return byId[k] && recent[k].path; })
      .sort(function (a, b) { return recent[b].at - recent[a].at; });
    if (!rows.length) {
      list.innerHTML = '<li class="acc-empty">Open a theory or problem page and it will wait for you here.</li>';
    } else {
      rows.forEach(function (k) {
        var r = recent[k], s = byId[k];
        var li = document.createElement('li');
        li.innerHTML = '<a href="../' + esc(r.path) + '" style="--dot:' + s.accent + '">' +
          '<span class="acc-continue__dot" aria-hidden="true"></span>' +
          '<span class="acc-continue__body"><span class="acc-continue__meta">' + esc(s.short) + (r.area ? ' &middot; ' + esc(r.area) : '') + '</span>' +
          '<span class="acc-continue__title">' + esc(r.title || s.name) + '</span></span>' +
          '<span class="acc-continue__ago">' + esc(ago(r.at)) + '</span>' +
          '<svg class="acc-continue__arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>';
        list.appendChild(li);
      });
    }

    // upcoming exams
    var exams = [];
    var today = new Date(); today.setHours(0, 0, 0, 0);
    prefs.subjects.forEach(function (id) {
      var e = prefs.exams[id] || {};
      [['midterm', 'Midterm'], ['final', 'Final exam']].forEach(function (kind) {
        if (!e[kind[0]]) return;
        var p = e[kind[0]].split('-');
        var date = new Date(+p[0], +p[1] - 1, +p[2]);
        var left = Math.round((date - today) / 86400000);
        if (left >= 0) exams.push({ s: byId[id], kind: kind[1], date: date, left: left });
      });
    });
    exams.sort(function (a, b) { return a.left - b.left; });
    var examList = $('#examList');
    if (!exams.length) {
      examList.innerHTML = '<li class="acc-empty">No dates yet. <a href="settings.html#subjects">Add your exams</a> and they count down here.</li>';
    } else {
      exams.slice(0, 6).forEach(function (x) {
        var li = document.createElement('li');
        li.className = x.left <= 7 ? 'is-soon' : '';
        li.style.setProperty('--dot', x.s.accent);
        li.innerHTML = '<span class="acc-exams__days"><strong>' + (x.left === 0 ? 'Today' : x.left) + '</strong>' +
          (x.left === 0 ? '' : '<span>' + (x.left === 1 ? 'day' : 'days') + '</span>') + '</span>' +
          '<span class="acc-exams__body"><span class="acc-exams__name">' + esc(x.s.name) + '</span>' +
          '<span class="acc-exams__meta">' + esc(x.kind) + ' &middot; ' + esc(x.date.toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' })) + '</span></span>';
        examList.appendChild(li);
      });
    }

    // this week: stacked bars, one per day, one segment per subject
    var used = subjects.filter(function (s) { return week.some(function (day) { return day[s.id]; }); });
    var chartSubjects = used.length ? used : subjects.filter(function (s) { return prefs.subjects.indexOf(s.id) !== -1; });
    $('#weekTotal').textContent = weekTotal ? duration(weekTotal) + ' in the last 7 days' : 'No study time yet';
    renderGoal(weekTotal, prefs.weeklyGoal);
    renderWeek(days, week, chartSubjects);
    renderHeatmap(log);
    renderSky(log, prefs, byId);
    wireMarks(byId);
    var resizeTimer = 0;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(function () { renderWeek(days, week, chartSubjects); }, 150);
    });

    // exam simulator
    var sims = $('#simList');
    var any = false;
    subjects.forEach(function (s) {
      var key = SIM_KEYS[s.id];
      if (!key) return;
      var store = readStore(key);
      var hist = store && Array.isArray(store.history) ? store.history.filter(function (h) { return h.max > 0; }) : [];
      if (!hist.length) return;
      any = true;
      var grades = hist.map(function (h) { return h.total / h.max * 10; });
      var last = hist[hist.length - 1];
      var mistakes = openMistakes(hist);
      var review = mistakes.length;
      var avg = grades.reduce(function (a, b) { return a + b; }, 0) / grades.length;
      var best = Math.max.apply(null, grades);
      var card = document.createElement('article');
      card.className = 'acc-sim';
      card.style.setProperty('--dot', s.accent);
      card.innerHTML = '<header><span class="acc-continue__dot" aria-hidden="true"></span><h3>' + esc(s.name) + '</h3></header>' +
        '<div class="acc-sim__main"><div class="acc-sim__grade"><strong>' + grades[grades.length - 1].toFixed(1) + '</strong><span>last, out of 10</span></div>' +
        spark(grades.slice(-10), markColour(s.id)) + '</div>' +
        '<dl class="acc-sim__facts"><div><dt>Attempts</dt><dd>' + hist.length + '</dd></div><div><dt>Average</dt><dd>' + avg.toFixed(1) +
        '</dd></div><div><dt>Best</dt><dd>' + best.toFixed(1) + '</dd></div></dl>' +
        '<div class="acc-sim__links"><a href="../subjects/' + s.id + '/simulator/index.html">New simulation</a>' +
        (review ? '<button type="button" class="acc-sim__review" aria-expanded="false">' + review + (review === 1 ? ' mistake' : ' mistakes') + ' to practise</button>' : '<span>Nothing to review</span>') + '</div>' +
        (review ? '<div class="acc-sim__list" hidden></div>' : '');
      sims.appendChild(card);
      if (review) wireMistakes(card, s, mistakes);
    });
    if (!any) {
      sims.innerHTML = '<p class="acc-empty">No simulations yet. Try one: ' + subjects.filter(function (s) { return SIM_KEYS[s.id]; })
        .map(function (s) { return '<a href="../subjects/' + s.id + '/simulator/index.html">' + esc(s.short) + '</a>'; }).join(' &middot; ') + '.</p>';
    }
  }

  // Favourites and notes, newest first, filterable; each row links back to its problem card.
  var AREA_OF = { problemas: 'Problems', 'extra-problems': 'Extra problems' };
  function renderMarks(byId) {
    var list = $('#marksList');
    if (!list) return;
    var items = AEAccount.marks().items;
    var rows = Object.keys(items).map(function (k) { return items[k]; })
      .filter(function (m) { return byId[m.subject] && m.path; })
      .sort(function (a, b) { return (b.updated || 0) - (a.updated || 0); });
    var counts = { all: rows.length, fav: rows.filter(function (m) { return m.fav; }).length, note: rows.filter(function (m) { return m.note; }).length };
    $('#cntAll').textContent = counts.all;
    $('#cntFav').textContent = counts.fav;
    $('#cntNote').textContent = counts.note;
    var filter = (list.getAttribute('data-filter') || 'all');
    var shown = rows.filter(function (m) { return filter === 'all' || (filter === 'fav' ? m.fav : m.note); });
    if (!rows.length) {
      list.innerHTML = '<li class="acc-empty">Star a problem or write a note on it (the buttons beside its arrow) and it is kept here.</li>';
      return;
    }
    if (!shown.length) {
      list.innerHTML = '<li class="acc-empty">' + (filter === 'fav' ? 'No favourites yet.' : 'No notes yet.') + '</li>';
      return;
    }
    list.innerHTML = '';
    shown.forEach(function (m) {
      var s = byId[m.subject];
      var area = (/subjects\/[^\/]+\/([^\/]+)\//.exec(m.path) || [])[1];
      var li = document.createElement('li');
      li.innerHTML = '<a href="../' + esc(m.path) + '#' + esc(m.card) + '" style="--dot:' + s.accent + '">' +
        '<span class="acc-marks__icon' + (m.fav ? ' is-fav' : '') + '" aria-hidden="true">' +
        (m.fav ? '<svg width="16" height="16" viewBox="0 0 24 24"><path d="M12 3.3l2.6 5.4 5.9.8-4.3 4.1 1 5.9L12 16.7l-5.2 2.8 1-5.9-4.3-4.1 5.9-.8z"/></svg>'
               : '<svg width="16" height="16" viewBox="0 0 24 24"><path d="M5 4h10l4 4v12H5zM15 4v4h4M8.5 12h7M8.5 15.5h5"/></svg>') + '</span>' +
        '<span class="acc-marks__body"><span class="acc-continue__meta"><i class="acc-marks__dot"></i>' + esc(s.short) + ' &middot; ' + esc(AREA_OF[area] || 'Problems') +
        (m.fav ? ' &middot; <b>Favourite</b>' : '') + '</span>' +
        '<span class="acc-marks__title">' + esc(m.title || m.card) + '</span>' +
        (m.note ? '<span class="acc-marks__note">' + esc(m.note) + '</span>' : '') + '</span>' +
        '<span class="acc-continue__ago">' + esc(ago(m.updated || Date.now())) + '</span></a>';
      list.appendChild(li);
    });
  }

  function wireMarks(byId) {
    $$('.acc-chip[data-filter]').forEach(function (chip) {
      chip.addEventListener('click', function () {
        $$('.acc-chip[data-filter]').forEach(function (c) { c.setAttribute('aria-pressed', String(c === chip)); });
        $('#marksList').setAttribute('data-filter', chip.getAttribute('data-filter'));
        renderMarks(byId);
      });
    });
    renderMarks(byId);
    window.addEventListener('storage', function (e) { if (e.key === 'ae_marks') renderMarks(byId); });
  }

  // ---- Your sky: one star per day of study, constellations of consecutive days ---------------------
  // A day with at least 10 minutes in ae_study_log is a star: its size grows with the minutes, its
  // colour is the subject studied most that day. Consecutive days are joined into a constellation; a
  // day without study closes it. Positions come from the dates (a seeded random walk per
  // constellation, constellations laid on a golden-angle spiral), so the sky never reshuffles and
  // only grows.
  function seeded(text) {
    var h = 2166136261;
    for (var i = 0; i < text.length; i++) { h ^= text.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; }
    return function () { h = Math.imul(h ^ (h >>> 15), 2246822507) >>> 0; h = Math.imul(h ^ (h >>> 13), 3266489909) >>> 0; return ((h ^= h >>> 16) >>> 0) / 4294967296; };
  }

  function skyDays(log) {
    return Object.keys(log.days).sort().map(function (k) {
      var rec = log.days[k];
      var sec = 0, top = null, topSec = 0;
      Object.keys(rec).forEach(function (s) { sec += rec[s]; if (rec[s] > topSec) { topSec = rec[s]; top = s; } });
      return { key: k, sec: sec, top: top, subjects: Object.keys(rec).filter(function (s) { return rec[s] >= 300; }) };
    }).filter(function (d) { return d.sec >= 600; });
  }

  function dayDiff(a, b) {
    var pa = a.split('-'), pb = b.split('-');
    return Math.round((new Date(+pb[0], pb[1] - 1, +pb[2]) - new Date(+pa[0], pa[1] - 1, +pa[2])) / 86400000);
  }

  function renderSky(log, prefs, byId) {
    var map = $('#skyMap');
    if (!map) return;
    var days = skyDays(log);
    var groups = [];
    days.forEach(function (d, i) {
      if (!i || dayDiff(days[i - 1].key, d.key) > 1) groups.push([]);
      groups[groups.length - 1].push(d);
    });
    var narrow = (map.clientWidth || 1000) < 600;   // phones: a taller sky, so the stars keep their size
    var W = narrow ? 600 : 1000, H = narrow ? 560 : 360;
    var stars = [], lines = [];
    // Each constellation gets its own cell of the sky, in date order (left to right, top to bottom);
    // inside it, a seeded random walk that stays within the cell, so groups never overlap.
    var n = Math.max(1, groups.length);
    var cols = Math.max(1, Math.ceil(Math.sqrt(n * W / H))), rows = Math.ceil(n / cols);
    var cw = W / cols, ch = H / rows;
    groups.forEach(function (g, gi) {
      var col = gi % cols, row = Math.floor(gi / cols);
      var rnd = seeded(g[0].key);
      var x0 = col * cw + 22, x1 = (col + 1) * cw - 22, y0 = row * ch + 22, y1 = (row + 1) * ch - 22;
      var x = x0 + (x1 - x0) * (0.3 + rnd() * 0.4), y = y0 + (y1 - y0) * (0.3 + rnd() * 0.4);
      var dir = rnd() * Math.PI * 2, step0 = Math.min(cw, ch) / (2.2 + Math.sqrt(g.length));
      g.forEach(function (d, di) {
        if (di) {
          dir += (rnd() - 0.5) * 2.2;
          var step = step0 * (0.75 + rnd() * 0.6);
          var nx = x + Math.cos(dir) * step, ny = y + Math.sin(dir) * step;
          if (nx < x0 || nx > x1) { dir = Math.PI - dir; nx = x + Math.cos(dir) * step; }
          if (ny < y0 || ny > y1) { dir = -dir; ny = y + Math.sin(dir) * step; }
          x = Math.max(x0, Math.min(x1, nx)); y = Math.max(y0, Math.min(y1, ny));
          lines.push([stars[stars.length - 1].x, stars[stars.length - 1].y, x, y]);
        }
        stars.push({ x: x, y: y, d: d, size: 2.2 + Math.min(5, Math.sqrt(d.sec / 60) / 2.6) });
      });
    });
    var best = days.reduce(function (b, d) { return !b || d.sec > b.sec ? d : b; }, null);
    $('#skyStars').textContent = stars.length;
    $('#skyConsts').textContent = groups.filter(function (g) { return g.length >= 2; }).length;
    $('#skyBest').textContent = best ? duration(best.sec) : '-';

    var rnd0 = seeded('dust');
    var dust = '';
    for (var i = 0; i < 140; i++) dust += '<circle cx="' + (rnd0() * W).toFixed(1) + '" cy="' + (rnd0() * H).toFixed(1) + '" r="' + (0.4 + rnd0() * 0.8).toFixed(2) + '" opacity="' + (0.15 + rnd0() * 0.5).toFixed(2) + '"/>';
    var newest = stars.length ? stars[stars.length - 1] : null;
    var svg = '<svg viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="Your sky: ' + stars.length + ' study days as stars, in ' +
      groups.length + ' groups of consecutive days">' +
      '<g class="acc-skymap__dust">' + dust + '</g>' +
      '<g class="acc-skymap__lines">' + lines.map(function (l) {
        return '<line x1="' + l[0].toFixed(1) + '" y1="' + l[1].toFixed(1) + '" x2="' + l[2].toFixed(1) + '" y2="' + l[3].toFixed(1) + '"/>';
      }).join('') + '</g>' +
      stars.map(function (st, i) {
        var c = markColour(st.d.top) || '#e2e8f0';
        return '<g class="acc-skymap__star' + (st === newest ? ' is-new' : '') + '" style="--c:' + c + ';--i:' + (i % 9) + '" data-tip="' +
          esc(dateLabel(st.d.key) + ' · ' + duration(st.d.sec) + (byId[st.d.top] ? ' · mostly ' + byId[st.d.top].short : '')) + '" tabindex="0">' +
          '<circle class="acc-skymap__halo" cx="' + st.x.toFixed(1) + '" cy="' + st.y.toFixed(1) + '" r="' + (st.size * 3.2).toFixed(1) + '"/>' +
          '<circle class="acc-skymap__core" cx="' + st.x.toFixed(1) + '" cy="' + st.y.toFixed(1) + '" r="' + st.size.toFixed(1) + '"/></g>';
      }).join('') +
      (stars.length ? '' : '<text x="' + W / 2 + '" y="' + H / 2 + '" text-anchor="middle" class="acc-skymap__empty">Study for 10 minutes today and your first star appears here.</text>') +
      '</svg>';
    map.innerHTML = svg;
    var used = {};
    days.forEach(function (d) { if (d.top) used[d.top] = true; });
    $('#skyLegend').innerHTML = Object.keys(used).length
      ? Object.keys(used).map(function (id) { return '<span><i style="background:' + markColour(id) + '"></i>' + esc(byId[id] ? byId[id].short : id) + '</span>'; }).join('') +
        '<span class="acc-sky-panel__hint">Size: minutes studied that day</span>'
      : '';
    var tip = $('#weekTip');
    $$('.acc-skymap__star', map).forEach(function (g) {
      function show() { tip.innerHTML = '<strong>' + g.getAttribute('data-tip') + '</strong>'; placeTip(tip, g.querySelector('.acc-skymap__core')); }
      function hide() { tip.hidden = true; }
      g.addEventListener('mouseenter', show); g.addEventListener('focus', show);
      g.addEventListener('mouseleave', hide); g.addEventListener('blur', hide);
    });
    renderBadges(days, groups, prefs);
  }

  function dateLabel(key) {
    var p = key.split('-');
    return new Date(+p[0], p[1] - 1, +p[2]).toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' });
  }

  // Achievements, all computed from what is already stored; locked ones show how far along they are.
  function renderBadges(days, groups, prefs) {
    var box = $('#skyBadges');
    if (!box) return;
    var longest = groups.reduce(function (m, g) { return Math.max(m, g.length); }, 0);
    // best 7-day window and subjects covered in one
    var bestWeek = 0, fullWeek = false;
    var mine = prefs.subjects || [];
    days.forEach(function (d, i) {
      var sum = 0, seen = {};
      for (var j = i; j >= 0 && dayDiff(days[j].key, d.key) < 7; j--) {
        sum += days[j].sec;
        days[j].subjects.forEach(function (s) { seen[s] = true; });
      }
      bestWeek = Math.max(bestWeek, sum);
      if (mine.length >= 2 && mine.every(function (s) { return seen[s]; })) fullWeek = true;
    });
    // a simulator item missed once and right in a later attempt
    var corrected = 0;
    Object.keys(SIM_KEYS).forEach(function (slug) {
      var st = readStore(SIM_KEYS[slug]);
      var hist = st && Array.isArray(st.history) ? st.history.slice().sort(function (a, b) { return (a.finishedAt || 0) - (b.finishedAt || 0); }) : [];
      var missed = {};
      hist.forEach(function (h) {
        (h.items || []).forEach(function (it) {
          var low = it.score < it.points / 2;
          if (low) missed[it.id] = true;
          else if (missed[it.id]) { corrected++; delete missed[it.id]; }
        });
      });
    });
    var goal = prefs.weeklyGoal || 0;
    var list = [
      { name: 'First light', text: 'Your first star', done: days.length >= 1, prog: Math.min(1, days.length) + ' / 1' },
      { name: 'Constellation', text: '5 days in a row', done: longest >= 5, prog: Math.min(longest, 5) + ' / 5' },
      { name: 'A week of nights', text: '7 days in a row', done: longest >= 7, prog: Math.min(longest, 7) + ' / 7' },
      { name: 'Ten hours', text: '10 h in 7 days', done: bestWeek >= 36000, prog: Math.floor(Math.min(bestWeek, 36000) / 3600) + ' / 10 h' },
      { name: 'On target', text: goal ? 'Your ' + goal + ' h weekly goal' : 'Set a weekly goal', done: !!goal && bestWeek >= goal * 3600,
        prog: goal ? Math.floor(Math.min(bestWeek, goal * 3600) / 3600) + ' / ' + goal + ' h' : 'no goal yet' },
      { name: 'Full sky', text: 'Every subject in one week', done: fullWeek, prog: mine.length >= 2 ? 'not yet' : 'choose 2+ subjects' },
      { name: 'Second chance', text: 'Right on a question you missed', done: corrected >= 1, prog: corrected + ' / 1' },
      { name: 'Fifty stars', text: '50 days of study', done: days.length >= 50, prog: Math.min(days.length, 50) + ' / 50' }
    ];
    box.innerHTML = list.map(function (b) {
      return '<li class="acc-badge' + (b.done ? ' is-done' : '') + '"><span class="acc-badge__icon" aria-hidden="true">' +
        '<svg viewBox="0 0 24 24" width="22" height="22"><path d="M12 2.5l2.4 6.6 7 .3-5.5 4.3 1.9 6.8L12 16.6l-5.8 3.9 1.9-6.8-5.5-4.3 7-.3z"/></svg></span>' +
        '<span class="acc-badge__body"><strong>' + esc(b.name) + '</strong><span>' + esc(b.text) + '</span>' +
        '<em>' + (b.done ? 'Unlocked' : esc(b.prog)) + '</em></span></li>';
    }).join('');
    var n = list.filter(function (b) { return b.done; }).length;
    box.setAttribute('aria-label', n + ' of ' + list.length + ' achievements unlocked');
  }

  // ---- "Practise my mistakes" -----------------------------------------------------------------
  // An item is still open when its latest attempt in any simulation scored below half of its
  // points (a wrong or blank test question, a problem below half). Getting it right later closes it.
  var BANKS = { 'business-management': 'AE_BM_BANK', 'aerospace-materials-1': 'AE_MAT_BANK', 'advanced-maths': 'AE_AM_BANK', 'engineering-mechanics': 'AE_EM_BANK' };
  var bankLoads = {};

  function openMistakes(hist) {
    var latest = {};
    hist.slice().sort(function (a, b) { return (a.finishedAt || 0) - (b.finishedAt || 0); }).forEach(function (h) {
      (h.items || []).forEach(function (it) { latest[it.id] = { low: it.score < it.points / 2, at: h.finishedAt || 0 }; });
    });
    return Object.keys(latest).filter(function (id) { return latest[id].low; })
      .sort(function (a, b) { return latest[b].at - latest[a].at; });
  }

  // The subject's bank (titles, units, pages) is loaded only when the list is opened.
  function loadBank(slug) {
    if (!bankLoads[slug]) {
      bankLoads[slug] = new Promise(function (resolve) {
        if (window[BANKS[slug]]) { resolve(window[BANKS[slug]]); return; }
        var tag = document.createElement('script');
        tag.src = '../subjects/' + slug + '/data/problems.js';
        tag.onload = function () { resolve(window[BANKS[slug]] || null); };
        tag.onerror = function () { resolve(null); };
        document.head.appendChild(tag);
      });
    }
    return bankLoads[slug];
  }

  function mistakeHref(slug, bank, item, id) {
    var pages = (bank && bank.pages) || {};
    var page = (item && pages[item.category]) ||
      (item && item.category === 'short_theory_case' ? 'midterm-1-theory.html' : 'midterm-1-problems.html');
    return '../subjects/' + slug + '/extra-problems/' + page + '#' + encodeURIComponent(id);
  }

  function wireMistakes(card, subject, ids) {
    var btn = card.querySelector('.acc-sim__review');
    var box = card.querySelector('.acc-sim__list');
    var listId = 'mistakes-' + subject.id;
    box.id = listId;
    btn.setAttribute('aria-controls', listId);
    var filled = false;
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', String(open));
      box.hidden = !open;
      if (!open || filled) return;
      box.innerHTML = '<p class="acc-sim__loading">Loading your mistakes...</p>';
      loadBank(subject.id).then(function (bank) {
        filled = true;
        var byId = {};
        ((bank && bank.items) || []).forEach(function (it) { byId[it.id] = it; });
        var shown = ids.slice(0, 12);
        box.innerHTML = '<ol class="acc-mistakes">' + shown.map(function (id) {
          var it = byId[id];
          return '<li><a href="' + esc(mistakeHref(subject.id, bank, it, id)) + '">' +
            '<span class="acc-mistakes__id">' + esc(id) + (it && it.unit ? ' &middot; Unit ' + esc(it.unit) : '') + '</span>' +
            '<span class="acc-mistakes__title">' + esc(it ? it.title : 'Item ' + id) + '</span></a></li>';
        }).join('') + '</ol>' +
          (ids.length > shown.length ? '<p class="acc-sim__more">and ' + (ids.length - shown.length) + ' more</p>' : '') +
          '<a class="acc-btn acc-btn--ghost acc-sim__practise" href="../subjects/' + subject.id + '/simulator/index.html">Start a new simulation</a>';
      });
    });
  }

  // Weekly goal: a ring with the share of the goal reached in the last 7 days.
  function renderGoal(weekSec, goalH) {
    var box = $('#weekGoal');
    if (!box) return;
    if (!goalH) {
      box.innerHTML = '<a class="acc-goal__set" href="settings.html#study">Set a weekly goal</a>';
      return;
    }
    var share = Math.min(1, weekSec / 3600 / goalH);
    var r = 22, c = 2 * Math.PI * r;
    var done = share >= 1;
    box.innerHTML = '<svg class="acc-goal__ring" viewBox="0 0 56 56" width="56" height="56" aria-hidden="true">' +
      '<circle cx="28" cy="28" r="' + r + '" class="acc-goal__track"/>' +
      '<circle cx="28" cy="28" r="' + r + '" class="acc-goal__arc' + (done ? ' is-done' : '') + '" stroke-dasharray="' + c.toFixed(1) + '" stroke-dashoffset="' +
      (c * (1 - share)).toFixed(1) + '" transform="rotate(-90 28 28)"/></svg>' +
      '<span class="acc-goal__pct">' + Math.round(share * 100) + '%</span>' +
      '<span class="acc-goal__text"><strong>' + (done ? 'Goal reached' : duration(Math.max(0, goalH * 3600 - weekSec)) + ' to go') + '</strong>' +
      '<span>of your ' + goalH + ' h weekly goal</span></span>';
  }

  // Sparkline of the grades out of 10: filled area, a point per attempt, the pass line at 5.
  var sparkId = 0;
  function spark(values, colour) {
    var w = 190, h = 64, pl = 16, pr = 8, pt = 8, pb = 8;
    var x = function (i) { return values.length < 2 ? (pl + w - pr) / 2 : pl + i * (w - pl - pr) / (values.length - 1); };
    var y = function (v) { return pt + (10 - v) / 10 * (h - pt - pb); };
    var id = 'spk' + (++sparkId);
    var pts = values.map(function (v, i) { return [x(i), y(v)]; });
    var line = pts.map(function (p) { return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' ');
    var area = values.length > 1
      ? 'M' + pts[0][0].toFixed(1) + ',' + (h - pb) + ' L' + line.split(' ').join(' L') + ' L' + pts[pts.length - 1][0].toFixed(1) + ',' + (h - pb) + ' Z'
      : '';
    var out = ['<svg class="acc-sim__spark" viewBox="0 0 ' + w + ' ' + h + '" role="img" aria-label="Grades of the last ' + values.length +
      (values.length === 1 ? ' attempt: ' : ' attempts: ') + values.map(function (v) { return v.toFixed(1); }).join(', ') + ' out of 10">',
      '<defs><linearGradient id="' + id + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="' + colour + '" stop-opacity="0.35"/>' +
      '<stop offset="1" stop-color="' + colour + '" stop-opacity="0"/></linearGradient></defs>',
      '<line class="acc-sim__mid" x1="' + pl + '" x2="' + (w - pr) + '" y1="' + y(5).toFixed(1) + '" y2="' + y(5).toFixed(1) + '"/>',
      '<text class="acc-sim__axis" x="0" y="' + (y(5) + 3).toFixed(1) + '">5</text>'];
    if (area) out.push('<path d="' + area + '" fill="url(#' + id + ')"/>',
      '<polyline points="' + line + '" fill="none" stroke="' + colour + '" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>');
    pts.forEach(function (p, i) {
      var lastOne = i === pts.length - 1;
      out.push('<circle cx="' + p[0].toFixed(1) + '" cy="' + p[1].toFixed(1) + '" r="' + (lastOne ? 4.5 : 2.6) + '" fill="' + colour +
        '" class="acc-sim__pt' + (lastOne ? ' is-last' : '') + '"/>');
    });
    out.push('</svg>');
    return out.join('');
  }

  function fmtMin(m) {
    m = Math.round(m);
    if (m < 60) return m + 'm';
    return Math.floor(m / 60) + 'h' + (m % 60 ? (m % 60 < 10 ? '0' : '') + (m % 60) : '');
  }

  // This week: stacked bars, one per day, with rounded tops, a soft gradient per subject, the daily
  // average as a dashed rule, and direct totals on today and on the best day only.
  function renderWeek(days, week, subjects) {
    var box = $('#weekChart');
    var W = Math.max(300, Math.round(box.clientWidth || 640)), H = 250, left = 40, right = 62, top = 26, bottom = 30;
    var totals = week.map(function (day) { return subjects.reduce(function (s, x) { return s + (day[x.id] || 0); }, 0) / 60; });
    var maxMin = Math.max.apply(null, totals.concat([30]));
    var step = maxMin <= 60 ? 15 : maxMin <= 180 ? 30 : maxMin <= 360 ? 60 : 120;
    var yMax = Math.ceil(maxMin * 1.08 / step) * step;
    var plotH = H - top - bottom, plotW = W - left - right;
    var slot = plotW / days.length, barW = Math.min(38, slot * 0.5);
    var y = function (m) { return top + plotH - m / yMax * plotH; };
    var avg = totals.reduce(function (a, b) { return a + b; }, 0) / days.length;
    var best = totals.indexOf(Math.max.apply(null, totals));
    var svg = ['<svg viewBox="0 0 ' + W + ' ' + H + '" width="' + W + '" height="' + H + '" role="img" aria-label="Minutes studied per day in the last 7 days, by subject"><defs>'];
    subjects.forEach(function (s) {
      var c = markColour(s.id);
      svg.push('<linearGradient id="wk-' + s.id + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="color-mix(in srgb, ' + c + ' 86%, #ffffff)"/>' +
        '<stop offset="1" stop-color="' + c + '"/></linearGradient>');
    });
    svg.push('</defs>');
    // today's column
    var tx = left + slot * (days.length - 1);
    svg.push('<rect class="acc-week__today" x="' + (tx + 4).toFixed(1) + '" y="' + (top - 18) + '" width="' + (slot - 8).toFixed(1) + '" height="' + (plotH + 18 + bottom - 4) + '" rx="10"/>');
    for (var g = 0; g <= yMax; g += step) {
      svg.push('<line class="acc-week__grid" x1="' + left + '" x2="' + (W - right) + '" y1="' + y(g).toFixed(1) + '" y2="' + y(g).toFixed(1) + '"/>');
      svg.push('<text class="acc-week__axis" x="' + (left - 8) + '" y="' + (y(g) + 4).toFixed(1) + '" text-anchor="end">' + fmtMin(g) + '</text>');
    }
    days.forEach(function (d, i) {
      var cx = left + slot * i + slot / 2, x0 = cx - barW / 2;
      var segs = subjects.filter(function (s) { return week[i][s.id]; });
      svg.push('<g class="acc-week__bar" data-i="' + i + '">');
      svg.push('<rect class="acc-week__hit" x="' + (cx - slot / 2) + '" y="' + (top - 18) + '" width="' + slot + '" height="' + (plotH + 18) + '"/>');
      if (segs.length) {
        var stackTop = y(totals[i]);
        // one clip per bar: rounded top, square bottom on the baseline
        svg.push('<clipPath id="wkc' + i + '"><rect x="' + x0.toFixed(1) + '" y="' + stackTop.toFixed(1) + '" width="' + barW.toFixed(1) + '" height="' + (y(0) - stackTop + 8).toFixed(1) + '" rx="7"/></clipPath>');
        svg.push('<g clip-path="url(#wkc' + i + ')">');
        var base = 0;
        segs.forEach(function (s, k) {
          var m = week[i][s.id] / 60;
          var y0 = y(base), y1 = y(base + m);
          var hgt = Math.max(1, y0 - y1 - (k ? 2 : 0));   // 2 px surface gap between segments
          svg.push('<rect x="' + x0.toFixed(1) + '" y="' + y1.toFixed(1) + '" width="' + barW.toFixed(1) + '" height="' + hgt.toFixed(1) + '" fill="url(#wk-' + s.id + ')"/>');
          base += m;
        });
        svg.push('</g>');
        if (i === days.length - 1 || i === best) {
          svg.push('<text class="acc-week__value" x="' + cx.toFixed(1) + '" y="' + (stackTop - 7).toFixed(1) + '" text-anchor="middle">' + fmtMin(totals[i]) + '</text>');
        }
      } else {
        svg.push('<rect class="acc-week__zero" x="' + x0.toFixed(1) + '" y="' + (y(0) - 3) + '" width="' + barW.toFixed(1) + '" height="3" rx="1.5"/>');
      }
      svg.push('</g>');
      var label = i === days.length - 1 ? 'Today' : d.toLocaleDateString('en-GB', { weekday: 'short' });
      svg.push('<text class="acc-week__axis' + (i === days.length - 1 ? ' is-today' : '') + '" x="' + cx.toFixed(1) + '" y="' + (H - 9) + '" text-anchor="middle">' + label + '</text>');
    });
    if (avg > 0) {
      svg.push('<line class="acc-week__avg" x1="' + left + '" x2="' + (W - right + 4) + '" y1="' + y(avg).toFixed(1) + '" y2="' + y(avg).toFixed(1) + '"/>');
      // the label sits in the right margin, outside the bars
      svg.push('<text class="acc-week__avglabel" x="' + (W - right + 8) + '" y="' + (y(avg) - 2).toFixed(1) + '">avg</text>');
      svg.push('<text class="acc-week__avglabel acc-week__avglabel--value" x="' + (W - right + 8) + '" y="' + (y(avg) + 11).toFixed(1) + '">' + fmtMin(avg) + '/day</text>');
    }
    svg.push('<line class="acc-week__base" x1="' + left + '" x2="' + (W - right) + '" y1="' + y(0) + '" y2="' + y(0) + '"/></svg>');
    box.innerHTML = svg.join('');

    $('#weekLegend').innerHTML = subjects.map(function (s) {
      return '<span><i style="background:' + markColour(s.id) + '"></i>' + esc(s.short) + '</span>';
    }).join('');

    // by subject: share of the week, sorted
    var sums = subjects.map(function (s) {
      return { s: s, sec: week.reduce(function (a, day) { return a + (day[s.id] || 0); }, 0) };
    }).filter(function (r) { return r.sec; }).sort(function (a, b) { return b.sec - a.sec; });
    var all = sums.reduce(function (a, r) { return a + r.sec; }, 0);
    $('#weekShare').innerHTML = '<h3 class="acc-sub">By subject</h3>' + (sums.length ? sums.map(function (r) {
      var pct = Math.round(r.sec / all * 100);
      return '<div class="acc-share__row"><div class="acc-share__top"><span>' + esc(r.s.short) + '</span><span class="acc-share__val">' + duration(r.sec) +
        '<em>' + pct + '%</em></span></div><div class="acc-share__track"><i style="width:' + (r.sec / sums[0].sec * 100).toFixed(1) + '%;background:linear-gradient(90deg, ' +
        markColour(r.s.id) + ', color-mix(in srgb, ' + markColour(r.s.id) + ' 72%, #ffffff))"></i></div></div>';
    }).join('') : '<p class="acc-empty">No study time this week yet.</p>');

    // table view (identity is never colour alone)
    var head = '<tr><th>Day</th>' + subjects.map(function (s) { return '<th>' + esc(s.short) + '</th>'; }).join('') + '<th>Total</th></tr>';
    var body = days.map(function (d, i) {
      return '<tr><td>' + esc(d.toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' })) + '</td>' +
        subjects.map(function (s) { return '<td>' + (week[i][s.id] ? Math.round(week[i][s.id] / 60) : 0) + '</td>'; }).join('') +
        '<td>' + Math.round(totals[i]) + '</td></tr>';
    }).join('');
    $('#weekTable').innerHTML = '<table class="acc-table"><caption>Minutes per day</caption><thead>' + head + '</thead><tbody>' + body + '</tbody></table>';

    // hover / focus: tooltip, and the other days step back
    var tip = $('#weekTip');
    var bars = $$('.acc-week__bar', box);
    bars.forEach(function (g) {
      var i = +g.getAttribute('data-i');
      g.setAttribute('tabindex', '0');
      function show() {
        var rows = subjects.filter(function (s) { return week[i][s.id]; }).map(function (s) {
          return '<span><i style="background:' + markColour(s.id) + '"></i>' + esc(s.short) + '<b>' + duration(week[i][s.id]) + '</b></span>';
        }).join('');
        tip.innerHTML = '<strong>' + esc(days[i].toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'short' })) + '</strong>' +
          (rows || '<span>No study time</span>') + (totals[i] ? '<em>' + duration(totals[i] * 60) + ' in total</em>' : '');
        placeTip(tip, g.querySelector('.acc-week__hit'));
        box.classList.add('is-focus');
        g.classList.add('is-hover');
      }
      function hide() { tip.hidden = true; box.classList.remove('is-focus'); g.classList.remove('is-hover'); }
      g.addEventListener('mouseenter', show);
      g.addEventListener('focus', show);
      g.addEventListener('mouseleave', hide);
      g.addEventListener('blur', hide);
    });
  }

  function placeTip(tip, el) {
    tip.hidden = false;
    var r = el.getBoundingClientRect();
    var tw = tip.offsetWidth;
    tip.style.left = Math.round(Math.max(8, Math.min(r.left + r.width / 2 - tw / 2, window.innerWidth - tw - 8))) + 'px';
    tip.style.top = Math.round(r.top + window.scrollY + 4) + 'px';   // the CSS lifts it by its own height
  }

  // Last 10 weeks: one cell per day, Monday to Sunday, in five steps of a single hue.
  function renderHeatmap(log) {
    var box = $('#heatmap');
    if (!box) return;
    var today = new Date(); today.setHours(12, 0, 0, 0);
    var dow = (today.getDay() + 6) % 7;            // Monday = 0
    var start = new Date(today); start.setDate(today.getDate() - dow - 9 * 7);
    var cells = [], weeks = 10, total = 0, active = 0;
    var levels = [0, 15, 45, 90, 150];
    for (var w = 0; w < weeks; w++) {
      for (var d = 0; d < 7; d++) {
        var date = new Date(start); date.setDate(start.getDate() + w * 7 + d);
        var future = date > today;
        var rec = log.days[AEAccount.dayKey(date)] || {};
        var min = Object.keys(rec).reduce(function (s, k) { return s + rec[k]; }, 0) / 60;
        if (!future) { total += min; if (min >= 10) active++; }
        var lvl = future ? -1 : min <= 0 ? 0 : levels.filter(function (t) { return min >= t; }).length;
        cells.push('<span class="acc-heat__cell" data-l="' + lvl + '" style="grid-column:' + (w + 2) + ';grid-row:' + (d + 2) + '"' +
          (future ? '' : ' tabindex="0" data-tip="' + esc(date.toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' })) + ' · ' + (min ? duration(min * 60) : 'no study') + '"') +
          ' aria-label="' + esc(date.toDateString()) + ': ' + Math.round(min) + ' minutes"></span>');
      }
      var monday = new Date(start); monday.setDate(start.getDate() + w * 7);
      if (w === 0 || monday.getDate() <= 7) {
        cells.push('<span class="acc-heat__month" style="grid-column:' + (w + 2) + ';grid-row:1">' + monday.toLocaleDateString('en-GB', { month: 'short' }) + '</span>');
      }
    }
    ['Mon', '', 'Wed', '', 'Fri', '', 'Sun'].forEach(function (n, i) {
      if (n) cells.push('<span class="acc-heat__day" style="grid-column:1;grid-row:' + (i + 2) + '">' + n + '</span>');
    });
    box.innerHTML = '<div class="acc-heat__grid">' + cells.join('') + '</div>' +
      '<div class="acc-heat__side"><p><strong>' + duration(total * 60) + '</strong><span>in 10 weeks</span></p><p><strong>' + active + '</strong><span>active days</span></p>' +
      '<div class="acc-heat__legend"><span>Less</span>' + [0, 1, 2, 3, 4].map(function (l) { return '<i class="acc-heat__cell" data-l="' + l + '"></i>'; }).join('') + '<span>More</span></div></div>';
    var tip = $('#weekTip');
    $$('.acc-heat__cell[data-tip]', box).forEach(function (c) {
      function show() { tip.innerHTML = '<strong>' + c.getAttribute('data-tip') + '</strong>'; placeTip(tip, c); }
      function hide() { tip.hidden = true; }
      c.addEventListener('mouseenter', show); c.addEventListener('focus', show);
      c.addEventListener('mouseleave', hide); c.addEventListener('blur', hide);
    });
  }

  // Cloud mode: say where the account lives, and on the sign-up page ask for the invite code.
  function initCloudBits() {
    if (AEAccount.backend !== 'supabase') return;
    $$('[data-local-line]').forEach(function (p) {
      p.lastChild.textContent = 'Synced to your account on every device';
    });
    var field = $('#inviteField');
    if (!field || !AEAccount.requiresInvite) return;
    field.hidden = false;
    var input = $('#suInvite'), status = $('#inviteStatus');
    var m = /[?&]invite=([^&#]+)/.exec(location.search);
    if (m) input.value = decodeURIComponent(m[1]).toUpperCase();
    var timer = 0, asked = '';
    function check() {
      var code = input.value.replace(/\s/g, '').toUpperCase();
      input.removeAttribute('aria-invalid');
      if (code.length < 12) { status.textContent = ''; status.className = 'acc-invite__status'; return; }
      if (code === asked) return;
      asked = code;
      status.textContent = 'Checking...';
      status.className = 'acc-invite__status';
      AEAccount.inviteStatus(code).then(function (st) {
        if (code !== asked) return;
        var text = { valid: 'Valid code', used: 'Already used', unknown: 'Not a Sideris code' }[st] || '';
        status.textContent = text;
        status.className = 'acc-invite__status is-' + (st === 'valid' ? 'ok' : 'bad');
        if (st !== 'valid') input.setAttribute('aria-invalid', 'true');
      }, function () { status.textContent = ''; asked = ''; });
    }
    input.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(check, 350); });
    if (input.value) check();
  }

  function start() {
    if (!window.AEAccount || !window.AESurface) { setTimeout(start, 30); return; }
    initCloudBits();
    var page = document.body.getAttribute('data-page');
    if (page === 'login') initLogin();
    else if (page === 'signup') initSignup();
    else if (page === 'settings') initSettings();
    else if (page === 'dashboard') initDashboard();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
