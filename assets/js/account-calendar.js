/*!
 * Sideris portal: account calendar page (account/calendar.html)
 *
 * Renders the student's term calendar from assets/js/calendar-core.js: week, month and list
 * views, a sheet per class (what you will do, prepare links, I missed it, class not held, edit
 * time or room, notes), the group and timetable editor, and the side column (next class, to
 * catch up, coming up). Everything is built inside one container by AECalendarUI.mount(), so
 * the test harness can mount it with a stub account. No storage of its own: the record lives
 * under 'ae_calendar' through AECalendar.load()/save().
 */
(function () {
  'use strict';

  var self = document.currentScript;
  var BASE = self && self.src ? self.src.replace(/assets\/js\/account-calendar\.js(\?.*)?$/, '') : '../';
  var DAY_NAMES = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
  var DAY_LONG = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var FALLBACK_SUBJECTS = [
    { id: 'fluid-mechanics', name: 'Fluid Mechanics', short: 'Fluids' },
    { id: 'aerospace-materials-1', name: 'Aerospace Materials I', short: 'Materials' },
    { id: 'engineering-mechanics', name: 'Engineering Mechanics', short: 'Mechanics' },
    { id: 'advanced-maths', name: 'Advanced Maths', short: 'Maths' },
    { id: 'business-management', name: 'Business Management', short: 'Management' }
  ];
  var MARK = { 'fluid-mechanics': '#008bbc', 'aerospace-materials-1': '#bc7b04', 'engineering-mechanics': '#36ac73', 'advanced-maths': '#6651a9', 'business-management': '#b14955' };
  var HOUR_PX = 48;

  function C() { return window.AECalendar; }
  function subjects() { return (window.AEAccount && window.AEAccount.SUBJECTS) || FALLBACK_SUBJECTS; }
  function subjectOf(id) { var l = subjects(); for (var i = 0; i < l.length; i++) if (l[i].id === id) return l[i]; return null; }
  function shortName(id) { var s = subjectOf(id); return s ? s.short : 'Personal'; }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function minutes(t) { var p = t.split(':'); return +p[0] * 60 + +p[1]; }
  function dateLabel(iso, long) {
    var d = C().dow(iso) - 1, p = iso.split('-');
    return (long ? DAY_LONG[d] : DAY_NAMES[d]) + ' ' + (+p[2]) + ' ' + MONTHS[+p[1] - 1];
  }
  function monday(iso) { return C().addDays(iso, 1 - C().dow(iso)); }
  function uid() { return 'ev-' + Date.now().toString(36) + Math.random().toString(36).slice(2, 7); }

  function kindLabel(o) {
    if (o.isExam && o.kind === 'exam') return 'Exam';
    return C().KIND_LABEL[o.kind] || 'Class';
  }

  function sourceLine(o, tt) {
    if (o.isEvent) return 'Added by you.';
    if (o.basis === 'log') return 'Covered in class (lecture log, Aula Global).';
    if (o.official) {
      var g = o.group && o.group !== 'custom' ? ' (' + o.group + ')' : '';
      return (o.fromSlot ? 'From the official plan, given to your own timetable in order' : 'From the official weekly planning' + g) +
        '. Your changes override it.';
    }
    if (o.kind === 'exam') return 'Exam date from your settings.';
    return 'Your own slot. No official plan has been published for it.';
  }

  // ======================================================================== group editor
  // Builds the per-subject group, lab group and weekly slot editor into `container`. Mutates
  // rec.groups and rec.daysOff; calls onChange() after every edit.
  function groupPicker(container, slugs, rec, onChange, tt) {
    tt = tt || window.AE_TIMETABLE || { subjects: {} };
    container.innerHTML = '';
    slugs.forEach(function (slug) {
      var subj = tt.subjects[slug];
      var meta = subjectOf(slug) || { name: slug };
      var g = rec.groups[slug] || null;
      var box = el('fieldset', 'cal-grp');
      box.style.setProperty('--cal-mark', MARK[slug] || 'currentColor');
      box.appendChild(el('legend', 'cal-grp__name', meta.name));

      var row = el('div', 'cal-grp__row');
      var lab = el('label', 'cal-field');
      lab.appendChild(el('span', 'cal-field__label', 'Group'));
      var sel = el('select', 'cal-input');
      sel.setAttribute('data-grp', slug);
      [['', 'Choose your group']].concat(Object.keys((subj && subj.groups) || {}).map(function (k) { return [k, k + ' (official timetable)']; }))
        .concat([['custom', 'My own timetable']]).forEach(function (o) {
          var opt = el('option', '', o[1]); opt.value = o[0]; sel.appendChild(opt);
        });
      sel.value = g ? g.group : '';
      lab.appendChild(sel);
      row.appendChild(lab);

      if (subj && subj.labGroups && subj.labGroups.length) {
        var lab2 = el('label', 'cal-field');
        lab2.appendChild(el('span', 'cal-field__label', 'Lab group'));
        var sel2 = el('select', 'cal-input');
        sel2.setAttribute('data-lab', slug);
        [['', 'Not sure']].concat(subj.labGroups.map(function (x) { return [x, 'Group ' + x]; })).forEach(function (o) {
          var opt = el('option', '', o[1]); opt.value = o[0]; sel2.appendChild(opt);
        });
        sel2.value = g && g.labGroup ? g.labGroup : '';
        sel2.addEventListener('change', function () {
          ensure().labGroup = sel2.value || null; touch();
        });
        lab2.appendChild(sel2);
        row.appendChild(lab2);
      }
      box.appendChild(row);

      var note = el('p', 'cal-grp__hint');
      box.appendChild(note);
      var slotsBox = el('div', 'cal-slots');
      box.appendChild(slotsBox);

      function ensure() {
        if (!rec.groups[slug]) rec.groups[slug] = { group: sel.value || 'custom', labGroup: null, slots: [], at: Date.now() };
        return rec.groups[slug];
      }
      function touch() { ensure().at = Date.now(); onChange(); }

      function drawSlots() {
        slotsBox.innerHTML = '';
        var cur = rec.groups[slug];
        if (!cur) { note.textContent = subj && subj.basis === 'plan' ? 'Your classes and what is done in each come from the official plan of your group.' : 'Choose a group, or build your own timetable.'; return; }
        if (cur.group !== 'custom') {
          var og = subj && subj.groups[cur.group];
          note.textContent = og ? 'Official timetable: ' + og.slots.map(function (s) { return DAY_NAMES[s.dow - 1] + ' ' + s.start + '-' + s.end + (s.room ? ' ' + s.room : ''); }).join(', ') + '.' : '';
          return;
        }
        note.textContent = subj && subj.basis === 'plan'
          ? 'Add your weekly classes. The official plan is given to them in order: problem slots take the problem sessions, lecture slots the lectures.'
          : subj && subj.basis === 'log' ? 'Add your weekly classes. Lectures that appear in the lecture log show what was covered on that day.'
            : 'Add your weekly classes. There is no official plan for this subject yet: you can note what was covered after each class.';
        (cur.slots || []).forEach(function (s, i) {
          var r = el('div', 'cal-slot');
          r.setAttribute('data-slot', slug + ':' + i);
          var day = el('select', 'cal-input cal-input--day');
          day.setAttribute('aria-label', 'Day');
          DAY_LONG.forEach(function (n, k) { var o = el('option', '', n); o.value = String(k + 1); day.appendChild(o); });
          day.value = String(s.dow);
          var st = el('input', 'cal-input cal-input--time'); st.type = 'time'; st.value = s.start || ''; st.setAttribute('aria-label', 'Start');
          var en = el('input', 'cal-input cal-input--time'); en.type = 'time'; en.value = s.end || ''; en.setAttribute('aria-label', 'End');
          var room = el('input', 'cal-input cal-input--room'); room.value = s.room || ''; room.placeholder = 'Room'; room.setAttribute('aria-label', 'Room');
          var kind = el('select', 'cal-input');
          kind.setAttribute('aria-label', 'Kind of class');
          [['lecture', 'Lecture'], ['problems', 'Problem class']].forEach(function (o) { var op = el('option', '', o[1]); op.value = o[0]; kind.appendChild(op); });
          kind.value = s.kind || 'lecture';
          var del = el('button', 'cal-btn cal-btn--quiet', 'Remove'); del.type = 'button';
          function upd() {
            s.dow = +day.value; s.start = st.value; s.end = en.value; s.room = room.value; s.kind = kind.value; touch();
          }
          [day, st, en, room, kind].forEach(function (x) { x.addEventListener('change', upd); });
          del.addEventListener('click', function () { cur.slots.splice(i, 1); touch(); drawSlots(); });
          [day, st, en, room, kind, del].forEach(function (x) { r.appendChild(x); });
          slotsBox.appendChild(r);
        });
        var add = el('button', 'cal-btn', 'Add a weekly class'); add.type = 'button';
        add.setAttribute('data-add-slot', slug);
        add.addEventListener('click', function () {
          cur.slots = cur.slots || [];
          cur.slots.push({ id: uid(), dow: 1, start: '09:00', end: '10:30', room: '', kind: 'lecture' });
          touch(); drawSlots();
        });
        slotsBox.appendChild(add);
      }

      sel.addEventListener('change', function () {
        if (!sel.value) { delete rec.groups[slug]; onChange(); drawSlots(); return; }
        var cur = ensure();
        cur.group = sel.value;
        if (sel.value === 'custom' && !(cur.slots && cur.slots.length)) {
          // Start the own timetable from the official slots of the first group, when there is one.
          var first = subj && Object.keys(subj.groups)[0];
          cur.slots = first ? subj.groups[first].slots.map(function (s) { return { id: uid(), dow: s.dow, start: s.start, end: s.end, room: '', kind: s.kind }; }) : [];
        }
        touch(); drawSlots();
      });
      drawSlots();
      container.appendChild(box);
    });
  }

  // ======================================================================== the page
  function mount(root, opts) {
    opts = opts || {};
    var account = opts.account || window.AEAccount;
    var tt = opts.tt || window.AE_TIMETABLE || { term: { start: '2026-09-07', end: '2026-12-18', daysOff: [] }, subjects: {} };
    var base = opts.base != null ? opts.base : BASE;
    var params = new URLSearchParams(location.search);
    var today = opts.today || params.get('today') || new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().slice(0, 10);
    var nowTime = opts.now || params.get('now') || new Date().toTimeString().slice(0, 5);
    var width = opts.width || window.innerWidth;
    var state = { view: params.get('view') || (width < 640 ? 'list' : 'week'), anchor: params.get('date') || today };
    var rec = C().load();
    root.innerHTML = '';

    var user = account && account.current ? account.current() : null;
    if (!user) {
      var gate = el('section', 'acc-card acc-gate');
      gate.id = 'calGate';
      gate.appendChild(el('h1', '', 'Calendar'));
      gate.appendChild(el('p', '', 'Sign in to see your classes, labs and exams, and what will be done in each class.'));
      var inl = el('div', 'acc-inline');
      var a1 = el('a', 'acc-btn acc-btn--ghost', 'Sign in'); a1.href = 'login.html?next=calendar.html';
      var a2 = el('a', 'acc-btn acc-btn--primary', 'Create an account'); a2.href = 'signup.html';
      inl.appendChild(a1); inl.appendChild(a2); gate.appendChild(inl);
      root.appendChild(gate);
      return null;
    }
    function prefs() { var u = account.current(); return (u && u.prefs) || { subjects: [], exams: {} }; }
    function slugs() { var p = prefs(); return p.subjects && p.subjects.length ? p.subjects : subjects().map(function (s) { return s.id; }); }

    var app = el('div', 'cal');
    app.id = 'calApp';
    root.appendChild(app);
    var live = el('p', 'cal-sr'); live.id = 'calLive'; live.setAttribute('aria-live', 'polite');
    app.appendChild(live);

    // ---- toolbar
    var head = el('header', 'cal-head');
    head.appendChild(el('h1', 'cal-title', 'Calendar'));
    var bar = el('div', 'cal-bar');
    var nav = el('div', 'cal-bar__group');
    function btn(text, attr, val, cls) { var b = el('button', 'cal-btn' + (cls ? ' ' + cls : ''), text); b.type = 'button'; if (attr) b.setAttribute(attr, val); return b; }
    var prev = btn('Previous', 'data-cal-nav', 'prev'); prev.setAttribute('aria-label', 'Previous period');
    var nextB = btn('Next', 'data-cal-nav', 'next'); nextB.setAttribute('aria-label', 'Next period');
    var todayB = btn('Today', 'data-cal-nav', 'today');
    var period = el('strong', 'cal-period'); period.id = 'calPeriod';
    [prev, nextB, todayB, period].forEach(function (x) { nav.appendChild(x); });
    var views = el('div', 'cal-bar__group'); views.setAttribute('role', 'group'); views.setAttribute('aria-label', 'View');
    ['week', 'month', 'list'].forEach(function (v) { views.appendChild(btn(v.charAt(0).toUpperCase() + v.slice(1), 'data-cal-view', v)); });
    var acts = el('div', 'cal-bar__group');
    var addB = btn('Add', null, null, 'cal-btn--primary'); addB.id = 'calAdd';
    var grpB = btn('My groups', null, null); grpB.id = 'calGroups';
    var expB = btn('Export .ics', null, null); expB.id = 'calExport';
    expB.title = 'Download your term as a calendar file for Google Calendar or Outlook (a one-off copy)';
    acts.appendChild(addB); acts.appendChild(grpB); acts.appendChild(expB);
    bar.appendChild(nav); bar.appendChild(views); bar.appendChild(acts);
    head.appendChild(bar);
    app.appendChild(head);

    var layout = el('div', 'cal-layout');
    var mainCol = el('div', 'cal-main');
    var grid = el('div', 'cal-grid'); grid.id = 'calGrid';
    mainCol.appendChild(grid);
    var legend = el('p', 'cal-legend', 'Dashed border: lab. Striped: missed, to catch up. Faded: class not held. Labs never link to lab material.');
    mainCol.appendChild(legend);
    var side = el('aside', 'cal-side');
    function sideCard(id, title) {
      var s = el('section', 'acc-card cal-card');
      s.appendChild(el('h2', 'cal-card__title', title));
      var body = el('div', 'cal-card__body'); body.id = id;
      s.appendChild(body); side.appendChild(s);
      return body;
    }
    var nextBox = sideCard('calNext', 'Next class');
    var catchBox = sideCard('calCatchup', 'To catch up');
    var comingBox = sideCard('calComing', 'Coming up');
    var attBox = sideCard('calAttendance', 'Attendance');
    layout.appendChild(mainCol); layout.appendChild(side);
    app.appendChild(layout);

    // ---- dialogs
    var sheet = el('dialog', 'cal-dialog'); sheet.id = 'calSheet'; sheet.setAttribute('aria-labelledby', 'calSheetTitle');
    var groupsDlg = el('dialog', 'cal-dialog cal-dialog--wide'); groupsDlg.id = 'calGroupsDlg'; groupsDlg.setAttribute('aria-labelledby', 'calGroupsTitle');
    var addDlg = el('dialog', 'cal-dialog'); addDlg.id = 'calAddDlg'; addDlg.setAttribute('aria-labelledby', 'calAddTitle');
    [sheet, groupsDlg, addDlg].forEach(function (d) { app.appendChild(d); });

    function announce(text) { live.textContent = ''; setTimeout(function () { live.textContent = text; }, 30); }
    function persist(msg) {
      C().save(rec);
      if (account.changed) account.changed();
      render();
      if (msg) announce(msg);
    }
    function openDialog(d) { if (d.showModal) { if (!d.open) d.showModal(); } else d.setAttribute('open', ''); }
    function closeDialog(d) { if (d.close && d.open) d.close(); else d.removeAttribute('open'); }

    function all() { return C().build(tt, rec, prefs(), tt.term.start, '2027-07-31'); }
    function range() {
      if (state.view === 'week') { var m = monday(state.anchor); return [m, C().addDays(m, 6)]; }
      if (state.view === 'month') {
        var first = state.anchor.slice(0, 8) + '01';
        var start = monday(first);
        return [start, C().addDays(start, 41)];
      }
      var s = monday(state.anchor); return [s, C().addDays(s, 27)];
    }

    // ---- an event chip
    function chip(o, compact) {
      var b = el('button', 'cal-ev');
      b.type = 'button';
      b.setAttribute('data-key', o.key);
      b.style.setProperty('--cal-mark', MARK[o.subject] || 'var(--acc-text-2)');
      if (o.status === 'missed') b.classList.add('cal-ev--missed');
      if (o.status === 'notheld') b.classList.add('cal-ev--notheld');
      if (o.status === 'done') b.classList.add('cal-ev--done');
      if (o.kind === 'lab') b.classList.add('cal-ev--lab');
      if (o.isExam) b.classList.add('cal-ev--exam');
      if (o.manual && !o.official) b.classList.add('cal-ev--manual');
      var k = el('span', 'cal-ev__kind', shortName(o.subject) + ' / ' + kindLabel(o));
      var t = el('span', 'cal-ev__title', o.manual && !o.official ? (o.note ? o.note.split('\n')[0] : 'Your slot') : o.title);
      b.appendChild(k); b.appendChild(t);
      if (!compact) {
        var meta = [o.start ? o.start + (o.end ? '-' + o.end : '') : 'All day', o.room].filter(Boolean).join(' ');
        b.appendChild(el('span', 'cal-ev__meta', meta));
        if (o.status === 'missed') b.appendChild(el('span', 'cal-ev__tag', 'Missed, catch up'));
        if (o.status === 'notheld') b.appendChild(el('span', 'cal-ev__tag', o.fromSlot ? 'Not held, plan moved' : 'Not held'));
        if (o.status === 'done') b.appendChild(el('span', 'cal-ev__tag', 'Caught up'));
        if (o.movedFrom) b.appendChild(el('span', 'cal-ev__tag', 'Moved from ' + dateLabel(o.movedFrom)));
      }
      var label = shortName(o.subject) + ', ' + kindLabel(o) + ', ' + (o.title || '') + ', ' + dateLabel(o.date, true) + (o.start ? ' ' + o.start : '');
      b.setAttribute('aria-label', label + (o.status ? ', ' + o.status : ''));
      b.addEventListener('click', function () { openSheet(o); });
      return b;
    }

    // ---- views
    function renderWeek(list) {
      var m = monday(state.anchor);
      var days = [];
      for (var i = 0; i < 7; i++) days.push(C().addDays(m, i));
      days = days.filter(function (d, i) { return i < 5 || list.some(function (o) { return o.date === d; }); });
      var timed = list.filter(function (o) { return o.start; });
      var lo = 8 * 60, hi = 20 * 60;
      timed.forEach(function (o) { lo = Math.min(lo, Math.floor(minutes(o.start) / 60) * 60); hi = Math.max(hi, Math.ceil(minutes(o.end || o.start) / 60) * 60 + (o.end ? 0 : 60)); });
      var wrap = el('div', 'cal-week');
      wrap.style.setProperty('--cal-cols', days.length);
      wrap.appendChild(el('div', 'cal-week__corner'));
      days.forEach(function (d) {
        var h = el('div', 'cal-week__day' + (d === today ? ' is-today' : ''));
        h.appendChild(el('span', '', DAY_NAMES[C().dow(d) - 1]));
        h.appendChild(el('strong', '', String(+d.slice(8))));
        if (d === today) h.appendChild(el('span', 'cal-week__today', 'today'));
        wrap.appendChild(h);
      });
      wrap.appendChild(el('div', 'cal-week__corner cal-week__allday-label', 'All day'));
      days.forEach(function (d) {
        var cell = el('div', 'cal-week__allday');
        list.filter(function (o) { return o.date === d && !o.start; }).forEach(function (o) { cell.appendChild(chip(o, true)); });
        wrap.appendChild(cell);
      });
      var gutter = el('div', 'cal-week__hours');
      gutter.style.height = ((hi - lo) / 60 * HOUR_PX) + 'px';
      for (var t = lo; t < hi; t += 60) {
        var s = el('span', '', (t / 60 < 10 ? '0' : '') + (t / 60) + ':00');
        s.style.top = ((t - lo) / 60 * HOUR_PX) + 'px';
        gutter.appendChild(s);
      }
      wrap.appendChild(gutter);
      days.forEach(function (d) {
        var col = el('div', 'cal-week__col' + (d === today ? ' is-today' : ''));
        col.style.height = ((hi - lo) / 60 * HOUR_PX) + 'px';
        var items = timed.filter(function (o) { return o.date === d; });
        var lanes = [];
        items.forEach(function (o) {
          var s0 = minutes(o.start), e0 = o.end ? minutes(o.end) : s0 + 60;
          var lane = 0;
          while (lanes[lane] && lanes[lane] > s0) lane++;
          lanes[lane] = e0; o._lane = lane; o._s = s0; o._e = e0;
        });
        items.forEach(function (o) {
          var c = chip(o, false);
          c.classList.add('cal-ev--abs');
          c.style.top = ((o._s - lo) / 60 * HOUR_PX) + 'px';
          c.style.height = Math.max(28, (o._e - o._s) / 60 * HOUR_PX - 3) + 'px';
          var n = lanes.length;
          c.style.left = 'calc(' + (o._lane * 100 / n) + '% + 3px)';
          c.style.width = 'calc(' + (100 / n) + '% - 6px)';
          col.appendChild(c);
        });
        wrap.appendChild(col);
      });
      grid.appendChild(wrap);
      period.textContent = dateLabel(days[0]) + ' - ' + dateLabel(C().addDays(m, 6));
    }

    function renderMonth(list, r) {
      var month = state.anchor.slice(0, 7);
      var wrap = el('div', 'cal-month');
      DAY_NAMES.forEach(function (n) { wrap.appendChild(el('div', 'cal-month__head', n)); });
      for (var i = 0; i < 42; i++) {
        var d = C().addDays(r[0], i);
        var cell = el('div', 'cal-month__cell' + (d.slice(0, 7) !== month ? ' is-out' : '') + (d === today ? ' is-today' : ''));
        cell.appendChild(el('span', 'cal-month__num', String(+d.slice(8))));
        var items = list.filter(function (o) { return o.date === d; });
        items.slice(0, 3).forEach(function (o) { cell.appendChild(chip(o, true)); });
        if (items.length > 3) {
          var more = el('button', 'cal-month__more', '+' + (items.length - 3) + ' more');
          more.type = 'button';
          (function (day) { more.addEventListener('click', function () { state.view = 'week'; state.anchor = day; render(); }); })(d);
          cell.appendChild(more);
        }
        wrap.appendChild(cell);
      }
      grid.appendChild(wrap);
      var p = state.anchor.split('-');
      period.textContent = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][+p[1] - 1] + ' ' + p[0];
    }

    function renderList(list, r) {
      var wrap = el('div', 'cal-list');
      var days = {};
      list.forEach(function (o) { (days[o.date] = days[o.date] || []).push(o); });
      var keys = Object.keys(days).sort();
      if (!keys.length) wrap.appendChild(el('p', 'cal-empty', 'Nothing in these four weeks.'));
      keys.forEach(function (d) {
        var g = el('section', 'cal-list__day' + (d === today ? ' is-today' : ''));
        g.appendChild(el('h3', 'cal-list__date', dateLabel(d, true) + (d === today ? ' (today)' : '')));
        days[d].forEach(function (o) { g.appendChild(chip(o, false)); });
        wrap.appendChild(g);
      });
      grid.appendChild(wrap);
      period.textContent = dateLabel(r[0]) + ' - ' + dateLabel(r[1]);
    }

    function renderSide(occ) {
      nextBox.innerHTML = ''; catchBox.innerHTML = ''; comingBox.innerHTML = '';
      var hasGroups = Object.keys(rec.groups).length > 0;
      var n = C().next(occ, today + 'T' + nowTime);
      if (!hasGroups) {
        nextBox.appendChild(el('p', 'cal-muted', 'Choose your groups to see your classes.'));
      } else if (n) {
        nextBox.appendChild(el('p', 'cal-kicker', dateLabel(n.date) + (n.start ? ' / ' + n.start : '') + (n.room ? ' / ' + n.room : '')));
        nextBox.appendChild(chip(n, true));
        if (n.text) nextBox.appendChild(el('p', 'cal-muted', n.text));
      } else nextBox.appendChild(el('p', 'cal-muted', 'No more classes this term.'));

      var pend = C().pending(occ, today);
      if (!pend.length) catchBox.appendChild(el('p', 'cal-muted', 'Nothing to catch up. Mark a class as missed and it appears here with its material.'));
      var ul = el('ul', 'cal-items');
      pend.forEach(function (o) {
        var li = el('li', 'cal-item');
        li.style.setProperty('--cal-mark', MARK[o.subject] || 'var(--acc-text-2)');
        li.appendChild(el('span', 'cal-item__when', dateLabel(o.date) + ' / ' + shortName(o.subject)));
        li.appendChild(el('span', 'cal-item__title', o.title));
        var row = el('span', 'cal-item__links');
        o.links.slice(0, 2).forEach(function (l) { var a = el('a', '', l.label); a.href = base + l.href; row.appendChild(a); });
        var done = el('button', 'cal-link-btn', 'Mark as caught up'); done.type = 'button';
        done.setAttribute('data-done', o.key);
        done.addEventListener('click', function () { setMark(o, { status: 'done' }); persist('Marked as caught up'); });
        row.appendChild(done);
        li.appendChild(row);
        ul.appendChild(li);
      });
      if (pend.length) catchBox.appendChild(ul);

      var limit = C().addDays(today, 28);
      var coming = occ.filter(function (o) { return o.date >= today && o.date <= limit && (o.isExam || o.kind === 'lab') && o.status !== 'notheld'; });
      if (!coming.length) comingBox.appendChild(el('p', 'cal-muted', 'No exams or labs in the next four weeks.'));
      var ul2 = el('ul', 'cal-items');
      coming.forEach(function (o) {
        var li = el('li', 'cal-item');
        li.style.setProperty('--cal-mark', MARK[o.subject] || 'var(--acc-text-2)');
        li.appendChild(el('span', 'cal-item__when', dateLabel(o.date) + (o.start ? ' / ' + o.start : '')));
        var b = el('button', 'cal-link-btn cal-item__title', shortName(o.subject) + ': ' + o.title); b.type = 'button';
        b.addEventListener('click', function () { openSheet(o); });
        li.appendChild(b);
        ul2.appendChild(li);
      });
      if (coming.length) comingBox.appendChild(ul2);

      attBox.innerHTML = '';
      var att = C().attendance(occ, today);
      var keys = Object.keys(att).filter(function (k) { return att[k].held; });
      if (!keys.length) attBox.appendChild(el('p', 'cal-muted', 'Your attendance appears here once classes have been held.'));
      var ul3 = el('ul', 'cal-items');
      keys.forEach(function (k) {
        var a = att[k];
        var li = el('li', 'cal-item');
        li.style.setProperty('--cal-mark', MARK[k] || 'var(--acc-text-2)');
        li.appendChild(el('span', 'cal-item__title', shortName(k) + ': ' + a.attended + ' of ' + a.held + ' classes'));
        li.appendChild(el('span', 'cal-item__when', a.missed ? a.missed + ' missed, ' + a.caughtUp + ' caught up' : 'none missed'));
        ul3.appendChild(li);
      });
      if (keys.length) attBox.appendChild(ul3);
    }

    function exportICS() {
      var text = C().toICS(all(), today + 'T' + nowTime);
      var url = URL.createObjectURL(new Blob([text], { type: 'text/calendar;charset=utf-8' }));
      var a = el('a'); a.href = url; a.download = 'sideris-calendar.ics';
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(url); }, 2000);
      announce('Calendar file downloaded');
    }

    function render() {
      grid.innerHTML = '';
      Array.prototype.forEach.call(views.children, function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-cal-view') === state.view)); });
      grid.setAttribute('data-view', state.view);
      var occ = all();
      var r = range();
      var list = occ.filter(function (o) { return o.date >= r[0] && o.date <= r[1]; });
      if (state.view === 'week') renderWeek(list);
      else if (state.view === 'month') renderMonth(list, r);
      else renderList(list, r);
      renderSide(occ);
      api.occurrences = occ;
    }

    // ---- marks
      function setMark(o, patch) {
      var k = o.isEvent ? o.key : (o.sessionId || o.key);
      var m = rec.marks[k] || {};
      Object.keys(patch).forEach(function (p) { m[p] = patch[p]; });
      m.at = Date.now();
      rec.marks[k] = m;
    }
    function classKey(o) { return C().occKey(o.subject, o.date, o.start); }

    // ---- the sheet of one class
    function openSheet(o) {
      sheet.innerHTML = '';
      var form = el('form', 'cal-sheet');
      form.method = 'dialog';
      form.appendChild(el('p', 'cal-kicker', [dateLabel(o.date, true), o.start ? o.start + (o.end ? '-' + o.end : '') : 'All day', o.room, o.group && o.group !== 'custom' ? o.group : null].filter(Boolean).join(' / ')));
      var h = el('h2', 'cal-sheet__title', shortName(o.subject) + ' / ' + kindLabel(o) + (o.title ? ': ' + o.title : ''));
      h.id = 'calSheetTitle';
      form.appendChild(h);
      if (o.text) {
        form.appendChild(el('h3', 'cal-sheet__sub', o.basis === 'log' ? 'Covered in class' : 'What you will do'));
        form.appendChild(el('p', 'cal-sheet__text', o.text));
      }
      if (o.links.length) {
        var p = el('p', 'cal-sheet__links');
        p.appendChild(el('span', 'cal-sheet__sub', 'Prepare: '));
        o.links.forEach(function (l, i) { if (i) p.appendChild(document.createTextNode(' / ')); var a = el('a', '', l.label); a.href = base + l.href; p.appendChild(a); });
        form.appendChild(p);
      }
      if (o.movedFrom) form.appendChild(el('p', 'cal-muted', 'Moved from ' + dateLabel(o.movedFrom, true) + '.'));
      form.appendChild(el('p', 'cal-sheet__source', sourceLine(o, tt)));

      var actions = el('div', 'cal-sheet__actions');
      function act(name, text, fn) { var b = btn(text, 'data-act', name); b.addEventListener('click', fn); actions.appendChild(b); return b; }
      var isClass = !o.isEvent && !o.isExam;
      if (isClass && o.date <= today || (isClass && o.kind === 'lab')) {
        act('missed', o.status === 'missed' ? 'Undo: I missed it' : 'I missed it', function () {
          setMark(o, { status: o.status === 'missed' ? null : 'missed' }); closeDialog(sheet);
          persist(o.status === 'missed' ? 'Class no longer marked as missed' : 'Marked as missed. It is in To catch up.');
        });
      } else if (isClass) {
        act('missed', o.status === 'missed' ? 'Undo: I will miss it' : 'I will miss it', function () {
          setMark(o, { status: o.status === 'missed' ? null : 'missed' }); closeDialog(sheet); persist('Saved');
        });
      }
      if (o.status === 'missed') act('done', 'Caught up', function () { setMark(o, { status: 'done' }); closeDialog(sheet); persist('Marked as caught up'); });

      var moveBox = null;
      if (isClass && o.kind !== 'lab') {
        act('notheld', o.status === 'notheld' || o.movedFrom ? 'Undo: class not held' : 'Class not held', function () {
          if (o.status === 'notheld' || o.movedFrom) {
            var k = o.fromSlot ? classKey(o) : o.sessionId;
            if (o.fromSlot) { if (rec.marks[k]) { rec.marks[k].status = null; rec.marks[k].at = Date.now(); } }
            else setMark(o, { status: null, moveTo: null });
            closeDialog(sheet); persist('Class restored'); return;
          }
          if (o.fromSlot) {
            var k2 = classKey(o);
            rec.marks[k2] = { status: 'notheld', at: Date.now() };
            closeDialog(sheet); persist('Class not held. The plan moves to your next class.');
          } else {
            moveBox.hidden = false;
            moveBox.querySelector('input').focus();
          }
        });
        if (!o.fromSlot) {
          moveBox = el('div', 'cal-sheet__move'); moveBox.hidden = true;
          var lab = el('label', 'cal-field');
          lab.appendChild(el('span', 'cal-field__label', 'When will this session be given?'));
          var inp = el('input', 'cal-input'); inp.type = 'date';
          var later = all().filter(function (x) { return x.subject === o.subject && x.date > o.date && !x.isExam && x.kind !== 'lab'; })[0];
          inp.value = later ? later.date : C().addDays(o.date, 7);
          lab.appendChild(inp); moveBox.appendChild(lab);
          var ok = btn('Move it', 'data-act', 'move');
          var none = btn('Not given at all', 'data-act', 'drop', 'cal-btn--quiet');
          ok.addEventListener('click', function () { setMark(o, { status: null, moveTo: inp.value }); closeDialog(sheet); persist('Session moved to ' + dateLabel(inp.value, true)); });
          none.addEventListener('click', function () { setMark(o, { status: 'notheld', moveTo: null }); closeDialog(sheet); persist('Class marked as not held'); });
          moveBox.appendChild(ok); moveBox.appendChild(none);
        }
      }
      if ((isClass && o.kind !== 'lab') || o.kind === 'study') {
        act('study', 'Study this', function () { location.href = studyRequest(o, base); });
      }
      if (o.status === 'missed' && o.kind !== 'lab') {
        act('explain', 'Explain what I missed', function () { location.href = explainRequest(o, base); });
      }
      var reviseBox = null;
      if (o.isExam && o.date > today) {
        act('revise', 'Plan my revision', function () { reviseBox.hidden = false; reviseBox.querySelector('input').focus(); });
        reviseBox = el('div', 'cal-sheet__move'); reviseBox.hidden = true;
        var rl = el('label', 'cal-field');
        rl.appendChild(el('span', 'cal-field__label', 'Hours a day'));
        var hours = el('input', 'cal-input cal-input--time'); hours.type = 'number'; hours.min = '0.5'; hours.max = '4'; hours.step = '0.5'; hours.value = '1';
        rl.appendChild(hours); reviseBox.appendChild(rl);
        var go = btn('Add study blocks', 'data-act', 'revise-go', 'cal-btn--primary');
        go.addEventListener('click', function () {
          rec.events.forEach(function (e) { if (e.exam === o.key && !e.deleted) { e.deleted = true; e.at = Date.now(); } });
          var blocks = C().revisionPlan(tt, rec, prefs(), o, today, +hours.value || 1);
          blocks.forEach(function (b) { rec.events.push(b); });
          closeDialog(sheet);
          persist(blocks.length ? blocks.length + ' study blocks added before the exam' : 'No free days left before this exam');
        });
        reviseBox.appendChild(go);
        reviseBox.appendChild(el('p', 'cal-muted', 'Blocks go on your free hours, one topic each, the topics of missed classes first. Delete or move any block later.'));
      }
      if (o.isEvent) act('delete', 'Delete', function () {
        rec.events.forEach(function (e) { if (e.id === o.key) { e.deleted = true; e.at = Date.now(); } });
        closeDialog(sheet); persist('Deleted');
      });
      else if (o.official || o.isExam) act('hide', 'Hide from my calendar', function () {
        rec.hidden.push({ id: o.key, at: Date.now() }); closeDialog(sheet); persist('Hidden from your calendar');
      });
      form.appendChild(actions);
      if (moveBox) form.appendChild(moveBox);
      if (reviseBox) form.appendChild(reviseBox);

      // edit time / room and note
      var det = el('details', 'cal-sheet__edit');
      det.appendChild(el('summary', '', 'Edit time, room or note'));
      var row = el('div', 'cal-grp__row');
      function field(label, type, value) {
        var l = el('label', 'cal-field'); l.appendChild(el('span', 'cal-field__label', label));
        var i = el(type === 'textarea' ? 'textarea' : 'input', 'cal-input'); if (type !== 'textarea') i.type = type; i.value = value || '';
        l.appendChild(i); row.appendChild(l); return i;
      }
      var fs = field('Start', 'time', o.start), fe = field('End', 'time', o.end), fr = field('Room', 'text', o.room);
      det.appendChild(row);
      var scope = null;
      var g = rec.groups[o.subject];
      if (o.fromSlot && g && g.group === 'custom') {
        scope = el('label', 'cal-check');
        var cb = el('input'); cb.type = 'checkbox'; scope.appendChild(cb);
        scope.appendChild(document.createTextNode(' Every ' + DAY_LONG[C().dow(o.date) - 1] + ' class (change the weekly slot)'));
        det.appendChild(scope);
      }
      var nl = el('label', 'cal-field cal-field--wide');
      nl.appendChild(el('span', 'cal-field__label', o.manual && !o.official ? 'What was covered (your note)' : 'Your note'));
      var nt = el('textarea', 'cal-input'); nt.rows = 3; nt.value = o.note || '';
      nl.appendChild(nt); det.appendChild(nl);
      var save = btn('Save changes', 'data-act', 'edit', 'cal-btn--primary');
      save.addEventListener('click', function () {
        if (scope && scope.querySelector('input').checked) {
          (g.slots || []).forEach(function (s) {
            if (s.dow === C().dow(o.date) && s.start === o.start) { s.start = fs.value; s.end = fe.value; s.room = fr.value; }
          });
          g.at = Date.now();
          if (nt.value !== (o.note || '')) setMark(o, { note: nt.value });
        } else if (o.isEvent) {
          rec.events.forEach(function (e) { if (e.id === o.key) { e.start = fs.value || null; e.end = fe.value || null; e.room = fr.value; e.note = nt.value; e.at = Date.now(); } });
        } else {
          var patch = { note: nt.value };
          if (fs.value && fs.value !== o.start || fe.value && fe.value !== o.end) patch.time = { start: fs.value, end: fe.value };
          if (fr.value !== (o.room || '')) patch.room = fr.value;
          setMark(o, patch);
        }
        closeDialog(sheet); persist('Changes saved');
      });
      det.appendChild(save);
      form.appendChild(det);
      var close = btn('Close', 'data-act', 'close', 'cal-btn--quiet cal-sheet__close');
      close.addEventListener('click', function () { closeDialog(sheet); });
      form.appendChild(close);
      if (api.extendSheet) api.extendSheet(o, form, actions);
      sheet.appendChild(form);
      openDialog(sheet);
    }

    // ---- groups dialog
    function openGroups() {
      groupsDlg.innerHTML = '';
      var form = el('div', 'cal-sheet');
      var h = el('h2', 'cal-sheet__title', 'My groups and timetable'); h.id = 'calGroupsTitle';
      form.appendChild(h);
      form.appendChild(el('p', 'cal-muted', 'Choose your group in each subject. With an official timetable your classes, labs and tests are filled in for you; with your own timetable you add your weekly classes. You can change anything later.'));
      var box = el('div', 'cal-grps');
      var draft = JSON.parse(JSON.stringify(rec));
      groupPicker(box, slugs(), draft, function () {}, tt);
      form.appendChild(box);
      // days off
      var off = el('fieldset', 'cal-grp');
      off.appendChild(el('legend', 'cal-grp__name', 'Days with no classes'));
      var offList = el('p', 'cal-muted');
      function drawOff() { offList.textContent = draft.daysOff.length ? draft.daysOff.map(function (d) { return dateLabel(d); }).join(', ') : 'None added. Official holidays are already left out.'; }
      drawOff();
      var oi = el('input', 'cal-input'); oi.type = 'date'; oi.setAttribute('aria-label', 'Day with no classes');
      var ob = btn('Add day');
      ob.addEventListener('click', function () { if (oi.value && draft.daysOff.indexOf(oi.value) < 0) { draft.daysOff.push(oi.value); draft.daysOff.sort(); drawOff(); } });
      var oc = btn('Clear', null, null, 'cal-btn--quiet');
      oc.addEventListener('click', function () { draft.daysOff = []; drawOff(); });
      off.appendChild(offList); off.appendChild(oi); off.appendChild(ob); off.appendChild(oc);
      form.appendChild(off);
      var row = el('div', 'cal-sheet__actions');
      var ok = btn('Save', 'data-act', 'save-groups', 'cal-btn--primary');
      var cancel = btn('Cancel', 'data-act', 'close', 'cal-btn--quiet');
      ok.addEventListener('click', function () { rec.groups = draft.groups; rec.daysOff = draft.daysOff; closeDialog(groupsDlg); persist('Groups saved'); });
      cancel.addEventListener('click', function () { closeDialog(groupsDlg); });
      row.appendChild(ok); row.appendChild(cancel);
      form.appendChild(row);
      groupsDlg.appendChild(form);
      openDialog(groupsDlg);
    }

    // ---- add dialog
    function openAdd() {
      addDlg.innerHTML = '';
      var form = el('div', 'cal-sheet');
      var h = el('h2', 'cal-sheet__title', 'Add to your calendar'); h.id = 'calAddTitle';
      form.appendChild(h);
      var row = el('div', 'cal-grp__row cal-grp__row--wrap');
      function field(label, node) { var l = el('label', 'cal-field'); l.appendChild(el('span', 'cal-field__label', label)); l.appendChild(node); row.appendChild(l); return node; }
      var kind = el('select', 'cal-input');
      [['lecture', 'Class'], ['problems', 'Problem class'], ['lab', 'Lab'], ['exam', 'Exam'], ['other', 'Other']].forEach(function (o) { var op = el('option', '', o[1]); op.value = o[0]; kind.appendChild(op); });
      field('What', kind);
      var subj = el('select', 'cal-input');
      var none = el('option', '', 'No subject'); none.value = ''; subj.appendChild(none);
      slugs().forEach(function (s) { var op = el('option', '', (subjectOf(s) || { name: s }).name); op.value = s; subj.appendChild(op); });
      field('Subject', subj);
      var title = el('input', 'cal-input'); title.placeholder = 'Title';
      field('Title', title);
      var date = el('input', 'cal-input'); date.type = 'date'; date.value = state.anchor;
      field('Date', date);
      var st = el('input', 'cal-input'); st.type = 'time'; field('Start (empty: all day)', st);
      var en = el('input', 'cal-input'); en.type = 'time'; field('End', en);
      var room = el('input', 'cal-input'); field('Room', room);
      form.appendChild(row);
      var err = el('p', 'cal-error'); err.setAttribute('role', 'alert'); form.appendChild(err);
      var acts2 = el('div', 'cal-sheet__actions');
      var ok = btn('Add', 'data-act', 'add', 'cal-btn--primary');
      var cancel = btn('Cancel', 'data-act', 'close', 'cal-btn--quiet');
      ok.addEventListener('click', function () {
        if (!date.value) { err.textContent = 'Choose a date.'; return; }
        rec.events.push({ id: uid(), subject: subj.value || null, kind: kind.value, title: title.value || (kind.options[kind.selectedIndex].text),
          date: date.value, start: st.value || null, end: en.value || null, room: room.value, note: '', links: [], at: Date.now() });
        closeDialog(addDlg); state.anchor = date.value; persist('Added to your calendar');
      });
      cancel.addEventListener('click', function () { closeDialog(addDlg); });
      acts2.appendChild(ok); acts2.appendChild(cancel);
      form.appendChild(acts2);
      addDlg.appendChild(form);
      openDialog(addDlg);
      title.focus();
    }

    // ---- wiring
    nav.addEventListener('click', function (e) {
      var b = e.target.closest('[data-cal-nav]'); if (!b) return;
      var w = b.getAttribute('data-cal-nav');
      if (w === 'today') state.anchor = today;
      else {
        var sign = w === 'next' ? 1 : -1;
        if (state.view === 'month') {
          var p = state.anchor.split('-'), m = +p[1] - 1 + sign, y = +p[0] + Math.floor(m / 12);
          m = ((m % 12) + 12) % 12;
          state.anchor = y + '-' + (m < 9 ? '0' : '') + (m + 1) + '-01';
        } else state.anchor = C().addDays(state.anchor, sign * (state.view === 'week' ? 7 : 28));
      }
      render();
    });
    views.addEventListener('click', function (e) {
      var b = e.target.closest('[data-cal-view]'); if (!b) return;
      state.view = b.getAttribute('data-cal-view'); render(); announce(b.textContent + ' view');
    });
    addB.addEventListener('click', openAdd);
    grpB.addEventListener('click', openGroups);
    expB.addEventListener('click', exportICS);
    document.addEventListener('keydown', function (e) {
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      if (sheet.open || groupsDlg.open || addDlg.open) return;
      var t = e.target;
      if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
      if (e.key === 'ArrowLeft') { prev.click(); e.preventDefault(); }
      else if (e.key === 'ArrowRight') { nextB.click(); e.preventDefault(); }
    });

    var api = { render: render, openSheet: openSheet, openGroups: openGroups, openAdd: openAdd, record: function () { return rec; }, state: state, occurrences: [], today: today, base: base, persist: persist, setMark: setMark };
    render();
    if (!Object.keys(rec.groups).length && !opts.noFirstVisit) openGroups();
    return api;
  }

  // The study timer and Sideris run on study pages only, so the calendar leaves the request in
  // sessionStorage and opens the class's first page; pomodoro.js / ai-chat.js pick it up there.
  function studyPage(o, base) {
    var l = (o.links || [])[0];
    if (l) return base + l.href;
    return base + 'subjects/' + (o.subject || 'engineering-mechanics') + '/teoria/index.html';
  }
  function put(key, value) { try { sessionStorage.setItem(key, JSON.stringify(value)); } catch (e) { /* blocked */ } }

  function explainRequest(o, base) {
    base = base != null ? base : BASE;
    var name = (subjectOf(o.subject) || { name: '' }).name;
    put('ae_sideris_pending', {
      visibleText: 'I missed this class. Explain what was covered and how to catch up.',
      taskLabel: 'Catch up on a missed class',
      location: name + ', ' + dateLabel(o.date, true),
      hiddenContext: 'The student missed a class of ' + name + ' on ' + dateLabel(o.date, true) + '. Session: ' + (o.title || '') +
        '. What was done: ' + (o.text || 'not stated') + '. Portal pages for it: ' + (o.links || []).map(function (l) { return l.label + ' (' + l.href + ')'; }).join('; ') +
        '. Explain the essential ideas step by step, then suggest which problems to try first.'
    });
    return studyPage(o, base);
  }

  function studyRequest(o, base) {
    base = base != null ? base : BASE;
    var len = o.start && o.end ? minutes(o.end) - minutes(o.start) : 50;
    put('ae_pomodoro_pending', { minutes: Math.max(25, len), label: shortName(o.subject) + ': ' + (o.title || ''), subject: o.subject || null });
    return studyPage(o, base);
  }

  // Sign-up wizard, step "Your classes": the group editor on a draft of the record. save()
  // stores it; skip() leaves the stored record untouched (the calendar asks on the first visit).
  function signupClasses(container, slugs, tt) {
    var draft = C().load();
    groupPicker(container, slugs, draft, function () {}, tt);
    return {
      draft: draft,
      save: function () {
        C().save(draft);
        if (window.AEAccount && window.AEAccount.changed) window.AEAccount.changed();
      },
      skip: function () {}
    };
  }

  // Sign-up wizard, step "Your exams": the official tests and quizzes of the chosen groups,
  // read-only, above the midterm and final date inputs.
  function officialExams(list, rec, prefs, tt) {
    tt = tt || window.AE_TIMETABLE;
    list.innerHTML = '';
    if (!tt) return 0;
    var occ = C().build(tt, rec, prefs, tt.term.start, tt.term.end).filter(function (o) { return o.isExam && o.official; });
    occ.forEach(function (o) {
      var li = el('li', 'cal-item');
      li.style.setProperty('--cal-mark', MARK[o.subject] || 'var(--acc-text-2)');
      li.appendChild(el('span', 'cal-item__when', dateLabel(o.date, true) + (o.start ? ' / ' + o.start : '')));
      li.appendChild(el('span', 'cal-item__title', shortName(o.subject) + ': ' + o.title));
      li.appendChild(el('span', 'cal-muted', 'From the official plan of your group.'));
      list.appendChild(li);
    });
    return occ.length;
  }

  // Dashboard card: the next class with what will be done in it, and a link to the calendar.
  function nextCard(container, o) {
    var tt = o.tt || window.AE_TIMETABLE;
    var base = o.base != null ? o.base : BASE;
    container.innerHTML = '';
    var link = el('a', 'acc-panel__link', 'Open the calendar');
    link.href = base + 'account/calendar.html';
    if (!tt || !Object.keys((o.rec && o.rec.groups) || {}).length) {
      container.appendChild(el('p', 'cal-muted', 'Choose your groups in the calendar to see your next class and what will be done in it.'));
      container.appendChild(link);
      return null;
    }
    var occ = C().build(tt, o.rec, o.prefs, o.today, C().addDays(o.today, 60));
    var n = C().next(occ, o.today + 'T' + o.now);
    if (!n) { container.appendChild(el('p', 'cal-muted', 'No more classes this term.')); container.appendChild(link); return null; }
    var box = el('div', 'cal-next');
    box.style.setProperty('--cal-mark', MARK[n.subject] || 'currentColor');
    box.appendChild(el('p', 'cal-kicker', dateLabel(n.date, true) + (n.start ? ' / ' + n.start + (n.end ? '-' + n.end : '') : '') + (n.room ? ' / ' + n.room : '')));
    box.appendChild(el('p', 'cal-next__title', (subjectOf(n.subject) || { name: '' }).name + ': ' + n.title));
    if (n.text) box.appendChild(el('p', 'cal-muted', n.text));
    if (n.links.length) {
      var p = el('p', 'cal-sheet__links');
      n.links.forEach(function (l, i) { if (i) p.appendChild(document.createTextNode(' / ')); var a = el('a', '', l.label); a.href = base + l.href; p.appendChild(a); });
      box.appendChild(p);
    }
    var pend = C().pending(C().build(tt, o.rec, o.prefs, tt.term.start, o.today), o.today).length;
    if (pend) box.appendChild(el('p', 'cal-muted', pend + (pend === 1 ? ' class' : ' classes') + ' to catch up.'));
    container.appendChild(box);
    container.appendChild(link);
    return n;
  }

  window.AECalendarUI = { mount: mount, groupPicker: groupPicker, nextCard: nextCard, signupClasses: signupClasses, officialExams: officialExams,
    explainRequest: explainRequest, studyRequest: studyRequest, MARK: MARK, dateLabel: function (iso, long) { return dateLabel(iso, long); } };

  function start() {
    if (document.body.getAttribute('data-page') !== 'calendar') return;
    if (!window.AEAccount || !window.AECalendar) { setTimeout(start, 30); return; }
    var root = document.getElementById('calRoot');
    window.AECalendarUI.page = mount(root, {});
    document.addEventListener('ae-account-change', function () { window.AECalendarUI.page = mount(root, { noFirstVisit: true }); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
