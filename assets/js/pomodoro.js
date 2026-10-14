/*!
 * Aerospace Engineering Study Portal: "Study timer" (Pomodoro timer and session planner).
 *
 * Loaded on every page by assets/js/theme.js, next to focus-lab.js (no page carries its own
 * <script> tag for it); the script adds its own stylesheet (assets/css/pomodoro.css). Skipped in
 * the PDF print mode (?print=...), and hidden by @media print.
 *
 * A floating "Timer" button sits right above the "Focus" button and opens a non-modal panel:
 *   - timer: SVG progress ring, Start/Pause, Reset, Skip phase, auto-start and chime switches;
 *   - free timer: Standard (25/5, long 15 every 4) or Deep focus (50/10, long 25 every 3), with
 *     every duration editable;
 *   - session planner: total time available ("3h", "2:30", "180 min") + block style -> a queue of
 *     focus blocks and breaks that fills the time exactly (see planSessions), run end to end.
 * While the timer runs, the button shows the time left and a small progress ring, and
 * document.title shows the time left and the phase.
 *
 * The clock is wall-clock based (endAt timestamp), so a throttled tab, a reload or a closed page
 * never drifts: on load the timer catches up through every phase that ended meanwhile.
 * The chime is synthesised with the Web Audio API (no audio files).
 *
 * Storage: 'ae_pomodoro' (JSON: mode, durations, plan and its position, running state, endAt).
 * API: window.AEPomodoro = { KEY, STYLES, planSessions, parseDuration, formatMinutes, open, close,
 *      start, pause, reset, skip, startPlan, endPlan, state }
 */
(function () {
  'use strict';

  if (window.AEPomodoro) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var SCRIPT = document.currentScript;
  var KEY = 'ae_pomodoro';
  var MINUTE = 60000;
  var LIMITS = { total: [10, 720], focus: [1, 180], short: [1, 60], long: [1, 90], longEvery: [2, 8] };

  // minFocus: shortest closing block worth starting; stretch: most the last block may grow by.
  var STYLES = {
    standard: { id: 'standard', label: 'Standard', focus: 25, short: 5, long: 15, longEvery: 4, minFocus: 10, stretch: 10,
      note: '25 min focus · 5 min break · 15 min long break every 4 blocks' },
    deep: { id: 'deep', label: 'Deep focus', focus: 50, short: 10, long: 25, longEvery: 3, minFocus: 20, stretch: 20,
      note: '50 min focus · 10 min break · 25 min long break every 3 blocks' }
  };

  var PHASES = {
    focus: { label: 'Focus', title: 'Focus' },
    short: { label: 'Short break', title: 'Break' },
    long: { label: 'Long break', title: 'Long break' }
  };

  function clamp(x, lo, hi) { return Math.min(hi, Math.max(lo, x)); }
  function style(id) { return STYLES[id] || STYLES.standard; }

  /* ================================================================== planner (no DOM)
     Break after the k-th focus block (k = 1, 2, ...): long when k is a multiple of longEvery. */
  function breakAfter(k, s) {
    return k % s.longEvery === 0 ? { kind: 'long', min: s.long } : { kind: 'short', min: s.short };
  }

  /* Fill `total` minutes with focus blocks and breaks; the plan starts and ends with focus.
     1. Greedy: keep adding [break, full block] while it fits.
     2. Rest R = total - used. If R minus the next break still leaves a block of at least minFocus,
        add that break and a shorter closing block (the plan then fills the time exactly).
     3. Otherwise lengthen the last block by min(R, stretch); anything left is free buffer.
     A total shorter than one block becomes a single block of that length. */
  function planSessions(total, styleId) {
    var s = style(styleId);
    total = Math.round(clamp(+total || 0, LIMITS.total[0], LIMITS.total[1]));
    var phases = [], used, n;
    if (total <= s.focus) {
      phases.push({ kind: 'focus', min: total });
      used = total;
    } else {
      phases.push({ kind: 'focus', min: s.focus });
      used = s.focus;
      n = 1;
      for (;;) {
        var b = breakAfter(n, s);
        if (used + b.min + s.focus > total) break;
        phases.push(b, { kind: 'focus', min: s.focus });
        used += b.min + s.focus;
        n++;
      }
      var rest = total - used, next = breakAfter(n, s);
      if (rest - next.min >= s.minFocus) {
        phases.push(next, { kind: 'focus', min: rest - next.min });
        used = total;
      } else if (rest > 0) {
        var add = Math.min(rest, s.stretch);
        phases[phases.length - 1].min += add;
        used += add;
      }
    }
    return summarise({ total: total, style: s.id, phases: phases, index: 0, done: false });
  }

  function summarise(plan) {
    var sum = { focus: 0, breaks: 0, blocks: 0, short: 0, long: 0, shortMin: 0, longMin: 0, sizes: {} };
    plan.phases.forEach(function (p) {
      if (p.kind === 'focus') {
        sum.focus += p.min;
        sum.blocks++;
        sum.sizes[p.min] = (sum.sizes[p.min] || 0) + 1;
      } else {
        sum.breaks += p.min;
        sum[p.kind]++;
        sum[p.kind + 'Min'] = p.min;
      }
    });
    sum.buffer = plan.total - sum.focus - sum.breaks;
    plan.summary = sum;
    return plan;
  }

  /* "3h", "3 h 30", "3h30m", "2:30", "2.5 h", "180", "180 min", "1 hora 20 minutos" -> minutes.
     A bare number up to 12 is read as hours, a larger one as minutes. Returns null if unreadable. */
  function parseDuration(text) {
    var str = String(text == null ? '' : text).toLowerCase().replace(/,/g, '.').trim();
    if (!str) return null;
    var m = /^(\d{1,2}):([0-5]\d)$/.exec(str);
    if (m) return +m[1] * 60 + +m[2];
    var re = /(\d+(?:\.\d+)?)\s*([a-zñ]*)/g, total = 0, tokens = 0, sawHours = false, t;
    var rest = str.replace(re, function (all, num, unit) {
      var v = +num;
      tokens++;
      if (/^(h|hr|hrs|hour|hours|hora|horas)$/.test(unit)) { total += v * 60; sawHours = true; }
      else if (/^(m|min|mins|minute|minutes|minuto|minutos)$/.test(unit)) total += v;
      else if (unit === '') total += sawHours ? v : NaN;   // "3h 30" -> minutes; a bare number is handled below
      else total = NaN;
      return ' ';
    });
    if (!tokens || !/^[\s+&]*(?:(?:and|y)[\s+&]*)*$/.test(rest)) return null;
    if (tokens === 1 && (t = /^(\d+(?:\.\d+)?)$/.exec(str))) total = +t[1] <= 12 ? +t[1] * 60 : +t[1];
    if (!isFinite(total) || total <= 0) return null;
    return Math.round(total);
  }

  function formatMinutes(min) {
    min = Math.round(min);
    var h = Math.floor(min / 60), m = min % 60;
    if (!h) return m + ' min';
    return m ? h + ' h ' + m + ' min' : h + ' h';
  }

  function clock(ms) {
    var s = Math.max(0, Math.ceil(ms / 1000)), h = Math.floor(s / 3600), m = Math.floor(s / 60) % 60, sec = s % 60;
    var mm = (h ? (m < 10 ? '0' : '') : '') + m, ss = (sec < 10 ? '0' : '') + sec;
    return (h ? h + ':' : '') + mm + ':' + ss;
  }

  function timeOfDay(date) {
    return (date.getHours() < 10 ? '0' : '') + date.getHours() + ':' + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes();
  }

  /* ================================================================== state */
  function defaults() {
    var s = STYLES.standard;
    return {
      v: 1,
      mode: 'free',                        // 'free' | 'plan'
      tab: 'free',                         // panel tab: 'free' | 'plan'
      preset: 'standard',                  // free timer preset ('custom' after editing)
      durations: { focus: s.focus, short: s.short, long: s.long, longEvery: s.longEvery },
      freeDone: 0,                         // focus blocks finished in the free cycle
      phase: { kind: 'focus', min: s.focus },
      plan: null,                          // { total, style, phases, index, done }
      draft: { input: '3h', style: 'standard' },
      running: false,
      started: false,                      // the current phase has been started (running or paused)
      endAt: 0,                            // wall-clock end of the running phase (ms)
      remaining: s.focus * MINUTE,         // time left while paused (ms)
      auto: true,                          // start the next phase on its own
      sound: true
    };
  }

  function int(x, range, fallback) {
    return isFinite(x) && x !== null && x !== '' ? Math.round(clamp(+x, range[0], range[1])) : fallback;
  }

  function cleanPhase(p, fallback) {
    if (!p || !PHASES[p.kind]) return fallback;
    var min = int(p.min, [1, LIMITS.total[1]], 0);
    return min ? { kind: p.kind, min: min } : fallback;
  }

  function load() {
    var s = defaults(), raw = null;
    try { raw = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { raw = null; }
    if (!raw || typeof raw !== 'object') return s;
    if (raw.mode === 'plan' || raw.mode === 'free') s.mode = raw.mode;
    if (raw.tab === 'plan' || raw.tab === 'free') s.tab = raw.tab;
    if (raw.preset === 'custom' || STYLES[raw.preset]) s.preset = raw.preset;
    var d = raw.durations || {};
    s.durations = {
      focus: int(d.focus, LIMITS.focus, s.durations.focus),
      short: int(d.short, LIMITS.short, s.durations.short),
      long: int(d.long, LIMITS.long, s.durations.long),
      longEvery: int(d.longEvery, LIMITS.longEvery, s.durations.longEvery)
    };
    s.freeDone = int(raw.freeDone, [0, 1e6], 0);
    s.phase = cleanPhase(raw.phase, { kind: 'focus', min: s.durations.focus });
    if (raw.plan && Array.isArray(raw.plan.phases) && raw.plan.phases.length) {
      var phases = raw.plan.phases.map(function (p) { return cleanPhase(p, null); }).filter(Boolean);
      if (phases.length) {
        s.plan = summarise({
          total: int(raw.plan.total, LIMITS.total, 0) || phases.reduce(function (a, p) { return a + p.min; }, 0),
          style: style(raw.plan.style).id,
          phases: phases,
          index: int(raw.plan.index, [0, phases.length - 1], 0),
          done: raw.plan.done === true
        });
      }
    }
    if (s.mode === 'plan' && !s.plan) s.mode = 'free';
    if (raw.draft) {
      s.draft.input = String(raw.draft.input == null ? s.draft.input : raw.draft.input).slice(0, 40);
      s.draft.style = style(raw.draft.style).id;
    }
    s.running = raw.running === true && isFinite(raw.endAt) && raw.endAt > 0;
    s.endAt = s.running ? +raw.endAt : 0;
    s.started = s.running || raw.started === true;
    var full = current(s).min * MINUTE;
    s.remaining = isFinite(raw.remaining) ? clamp(+raw.remaining, 0, full) : full;
    if (s.mode === 'plan' && s.plan.done) s.running = false;
    s.auto = raw.auto !== false;
    s.sound = raw.sound !== false;
    return s;
  }

  var state = load();

  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* storage blocked: keep it in memory */ }
  }

  function current(s) {
    s = s || state;
    return s.mode === 'plan' && s.plan ? s.plan.phases[s.plan.index] : s.phase;
  }

  function duration() { return current().min * MINUTE; }
  function remaining(now) { return state.running ? Math.max(0, state.endAt - (now || Date.now())) : state.remaining; }
  function planFinished() { return state.mode === 'plan' && state.plan && state.plan.done; }
  // A phase is "in progress" once started: it runs, or it is paused part-way.
  function inProgress() { return state.running || (state.started && !planFinished()); }

  /* ================================================================== timer logic */
  // Move to the next phase. Returns false when a plan has just ended.
  function nextPhase() {
    if (state.mode === 'plan') {
      if (state.plan.index >= state.plan.phases.length - 1) {
        state.plan.done = true;
        state.running = false;
        state.endAt = 0;
        state.remaining = 0;
        return false;
      }
      state.plan.index++;
    } else if (state.phase.kind === 'focus') {
      state.freeDone++;
      var d = state.durations;
      state.phase = state.freeDone % d.longEvery === 0 ? { kind: 'long', min: d.long } : { kind: 'short', min: d.short };
    } else {
      state.phase = { kind: 'focus', min: state.durations.focus };
    }
    return true;
  }

  // The running phase reached endAt: chain into the next one from that exact instant.
  function completePhase(silent) {
    var endedAt = state.endAt;
    var more = nextPhase();
    state.started = !!(more && state.auto);
    if (more && state.auto) {
      state.endAt = endedAt + duration();
      state.running = true;
    } else {
      state.running = false;
      state.endAt = 0;
      if (more) state.remaining = duration();
    }
    if (!silent && state.sound) chime(more ? current().kind : 'done');
    announce(more ? PHASES[current().kind].label + ' started' + (state.running ? '' : ' (paused)') : 'Plan complete');
  }

  function catchUp(now) {
    var guard = 0, changed = false;
    while (state.running && now >= state.endAt && guard++ < 500) {
      completePhase(now - state.endAt > 3000);   // phases that ended while the page was closed stay quiet
      changed = true;
    }
    return changed;
  }

  function start() {
    if (planFinished()) return;
    unlockAudio();
    if (state.remaining <= 0) state.remaining = duration();
    state.endAt = Date.now() + state.remaining;
    state.running = true;
    state.started = true;
    commit();
  }

  function pause() {
    if (!state.running) return;
    state.remaining = remaining();
    state.running = false;
    state.endAt = 0;
    commit();
  }

  function reset() {
    if (planFinished()) return;
    state.running = false;
    state.started = false;
    state.endAt = 0;
    state.remaining = duration();
    commit();
  }

  function skip() {
    if (planFinished()) return;
    var wasRunning = state.running;
    var more = nextPhase();
    if (more) {
      state.remaining = duration();
      state.running = wasRunning;
      state.started = wasRunning;
      state.endAt = wasRunning ? Date.now() + state.remaining : 0;
      announce(PHASES[current().kind].label + (wasRunning ? ' started' : ' ready'));
    } else {
      announce('Plan complete');
    }
    commit();
  }

  function startPlan(total, styleId) {
    state.plan = planSessions(total, styleId);
    state.mode = 'plan';
    state.tab = 'plan';
    state.remaining = duration();
    state.running = false;
    start();
  }

  function endPlan() {
    state.plan = null;
    state.mode = 'free';
    state.freeDone = 0;
    state.phase = { kind: 'focus', min: state.durations.focus };
    state.running = false;
    state.started = false;
    state.endAt = 0;
    state.remaining = duration();
    commit();
  }

  function setPreset(id) {
    var s = STYLES[id];
    if (!s) return;
    state.preset = id;
    state.durations = { focus: s.focus, short: s.short, long: s.long, longEvery: s.longEvery };
    if (state.mode === 'free') {
      state.freeDone = 0;
      state.phase = { kind: 'focus', min: s.focus };
      state.running = false;
      state.started = false;
      state.endAt = 0;
      state.remaining = duration();
    }
    commit();
  }

  function setDuration(name, value) {
    var v = int(value, LIMITS[name], state.durations[name]);
    state.durations[name] = v;
    state.preset = 'custom';
    // An idle free phase of that kind takes the new length at once; a started one keeps its own.
    if (state.mode === 'free' && !inProgress() && state.phase.kind === name) {
      state.phase.min = v;
      state.remaining = duration();
    }
    commit();
  }

  function commit() {
    save();
    render();
  }

  /* ================================================================== sound (Web Audio, no files) */
  var AudioCtx = window.AudioContext || window.webkitAudioContext;
  var audioCtx = null;

  function unlockAudio() {
    if (!AudioCtx) return null;
    try {
      if (!audioCtx) audioCtx = new AudioCtx();
      if (audioCtx.state === 'suspended') audioCtx.resume();
    } catch (e) { audioCtx = null; }
    return audioCtx;
  }

  // Soft bell: rising triad when focus starts, falling when a break starts, a fifth when the plan ends.
  var CHIMES = { focus: [523.25, 659.25, 783.99], short: [783.99, 659.25, 523.25], long: [783.99, 659.25, 523.25, 392], done: [523.25, 783.99, 1046.5] };

  function chime(kind) {
    var ctx = audioCtx;
    if (!ctx || ctx.state !== 'running') return;
    var notes = CHIMES[kind] || CHIMES.focus;
    var master = ctx.createGain();
    master.gain.value = 0.5;
    master.connect(ctx.destination);
    var t0 = ctx.currentTime + 0.03;
    notes.forEach(function (f, i) {
      var t = t0 + i * 0.16;
      [[f, 0.10], [2 * f, 0.018]].forEach(function (partial) {
        var osc = ctx.createOscillator(), g = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.value = partial[0];
        g.gain.setValueAtTime(0.0001, t);
        g.gain.exponentialRampToValueAtTime(partial[1], t + 0.015);
        g.gain.exponentialRampToValueAtTime(0.0001, t + 1.3);
        osc.connect(g);
        g.connect(master);
        osc.start(t);
        osc.stop(t + 1.35);
      });
    });
    setTimeout(function () { try { master.disconnect(); } catch (e) { /* already gone */ } }, (notes.length * 0.16 + 1.6) * 1000);
  }

  /* ================================================================== UI */
  var ui = {};
  var baseTitle = '';
  var RING = 2 * Math.PI * 52;   // circumference of the panel ring (r = 52 in a 120 viewBox)
  var MINI = 2 * Math.PI * 9;    // circumference of the launcher ring (r = 9 in a 24 viewBox)
  var NS = 'http://www.w3.org/2000/svg';

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function svg(tag, attrs) {
    var node = document.createElementNS(NS, tag);
    for (var k in attrs) node.setAttribute(k, attrs[k]);
    return node;
  }

  function svgIcon(paths, size) {
    var root = svg('svg', { viewBox: '0 0 24 24', width: size || 18, height: size || 18, 'aria-hidden': 'true', focusable: 'false' });
    paths.forEach(function (d) { root.appendChild(svg('path', { d: d })); });
    return root;
  }

  var ICONS = {
    play: ['M8 5.5v13l11-6.5z'],
    pause: ['M7.5 5.5h3v13h-3z', 'M13.5 5.5h3v13h-3z'],
    reset: ['M4.5 12a7.5 7.5 0 1 0 2.2-5.3', 'M4.5 4.5v4h4'],
    skip: ['M6 6l8 6-8 6z', 'M17.5 6v12'],
    close: ['M6 6l12 12', 'M18 6L6 18']
  };

  function button(className, text, label) {
    var b = el('button', className, text);
    b.type = 'button';
    if (label) b.setAttribute('aria-label', label);
    return b;
  }

  function seg(label, items, onPick) {
    var group = el('div', 'pm-seg');
    group.setAttribute('role', 'group');
    group.setAttribute('aria-label', label);
    var buttons = items.map(function (item) {
      var b = button('pm-seg__btn', item[1]);
      b.setAttribute('data-value', item[0]);
      b.addEventListener('click', function () { onPick(item[0]); });
      group.appendChild(b);
      return b;
    });
    return { group: group, buttons: buttons };
  }

  function toggleRow(id, title, text, onChange) {
    var row = el('label', 'pm-switch');
    var input = el('input', 'pm-switch__input');
    input.type = 'checkbox';
    input.id = id;
    var copy = el('span', 'pm-switch__text');
    copy.appendChild(el('strong', '', title));
    if (text) copy.appendChild(el('span', '', text));
    row.appendChild(input);
    row.appendChild(el('span', 'pm-switch__track'));
    row.appendChild(copy);
    input.addEventListener('change', function () { onChange(input.checked); });
    return { row: row, input: input };
  }

  function numberField(id, label, name) {
    var wrap = el('div', 'pm-field');
    var lab = el('label', 'pm-field__label', label);
    lab.htmlFor = id;
    var box = el('div', 'pm-field__box');
    var input = el('input', 'pm-input');
    input.type = 'number';
    input.id = id;
    input.inputMode = 'numeric';
    input.min = LIMITS[name][0];
    input.max = LIMITS[name][1];
    input.step = 1;
    box.appendChild(input);
    box.appendChild(el('span', 'pm-field__unit', name === 'longEvery' ? 'blocks' : 'min'));
    wrap.appendChild(lab);
    wrap.appendChild(box);
    input.addEventListener('change', function () { setDuration(name, input.value); });
    return { wrap: wrap, input: input };
  }

  function build() {
    if (document.getElementById('pomodoroButton') || !document.body) return;
    baseTitle = document.title;

    // launcher: mini ring + label (or the time left)
    var launcher = button('pm-launcher');
    launcher.id = 'pomodoroButton';
    launcher.setAttribute('aria-expanded', 'false');
    launcher.setAttribute('aria-controls', 'pomodoroPanel');
    var mini = svg('svg', { viewBox: '0 0 24 24', width: 18, height: 18, 'aria-hidden': 'true', focusable: 'false', 'class': 'pm-mini' });
    mini.appendChild(svg('circle', { cx: 12, cy: 12, r: 9, 'class': 'pm-mini__track' }));
    var miniArc = svg('circle', { cx: 12, cy: 12, r: 9, 'class': 'pm-mini__arc', 'stroke-dasharray': MINI.toFixed(2), transform: 'rotate(-90 12 12)' });
    mini.appendChild(miniArc);
    mini.appendChild(svg('path', { d: 'M12 7.5V12l3 2', 'class': 'pm-mini__hands' }));
    launcher.appendChild(mini);
    var launcherText = el('span', 'pm-launcher__label', 'Timer');
    launcher.appendChild(launcherText);

    var panel = el('section', 'pm-panel');
    panel.id = 'pomodoroPanel';
    panel.hidden = true;
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-modal', 'false');
    panel.setAttribute('aria-labelledby', 'pomodoroTitle');

    // header
    var head = el('header', 'pm-head');
    var titles = el('div');
    titles.appendChild(el('p', 'pm-kicker', 'Pomodoro · session planner'));
    var title = el('h2', 'pm-title', 'Study timer');
    title.id = 'pomodoroTitle';
    titles.appendChild(title);
    var close = button('pm-icon-btn', '', 'Close study timer');
    close.appendChild(svgIcon(ICONS.close, 18));
    head.appendChild(titles);
    head.appendChild(close);

    // timer: ring + readout
    var timer = el('div', 'pm-timer');
    var ring = svg('svg', { viewBox: '0 0 120 120', 'class': 'pm-ring', 'aria-hidden': 'true', focusable: 'false' });
    ring.appendChild(svg('circle', { cx: 60, cy: 60, r: 52, 'class': 'pm-ring__track' }));
    var arc = svg('circle', { cx: 60, cy: 60, r: 52, 'class': 'pm-ring__arc', 'stroke-dasharray': RING.toFixed(2), transform: 'rotate(-90 60 60)' });
    ring.appendChild(arc);
    var face = el('div', 'pm-face');
    var phaseLabel = el('p', 'pm-phase');
    var time = el('p', 'pm-time');
    time.setAttribute('role', 'timer');
    var sub = el('p', 'pm-sub');
    face.appendChild(phaseLabel);
    face.appendChild(time);
    face.appendChild(sub);
    var dial = el('div', 'pm-dial');
    dial.appendChild(ring);
    dial.appendChild(face);
    timer.appendChild(dial);

    // controls
    var controls = el('div', 'pm-controls');
    var play = button('pm-play');
    var playIcon = el('span', 'pm-play__icon');
    var playText = el('span', 'pm-play__text');
    play.appendChild(playIcon);
    play.appendChild(playText);
    var resetBtn = button('pm-icon-btn', '', 'Reset this phase');
    resetBtn.title = 'Reset this phase';
    resetBtn.appendChild(svgIcon(ICONS.reset, 18));
    var skipBtn = button('pm-icon-btn', '', 'Skip to the next phase');
    skipBtn.title = 'Skip to the next phase';
    skipBtn.appendChild(svgIcon(ICONS.skip, 18));
    controls.appendChild(play);
    controls.appendChild(resetBtn);
    controls.appendChild(skipBtn);
    timer.appendChild(controls);

    var live = el('p', 'pm-sr');
    live.setAttribute('aria-live', 'polite');

    // plan progress (visible while a plan is active)
    var progress = el('div', 'pm-progress');
    var progressHead = el('div', 'pm-progress__head');
    var progressText = el('span', 'pm-progress__text');
    var progressLeft = el('span', 'pm-progress__left');
    progressHead.appendChild(progressText);
    progressHead.appendChild(progressLeft);
    var track = el('div', 'pm-track');
    track.setAttribute('role', 'progressbar');
    track.setAttribute('aria-valuemin', '0');
    track.setAttribute('aria-valuemax', '100');
    progress.appendChild(progressHead);
    progress.appendChild(track);

    // tabs
    var tabs = seg('Timer mode', [['free', 'Free timer'], ['plan', 'Plan session']], function (v) {
      state.tab = v;
      commit();
    });
    tabs.group.className += ' pm-tabs';

    // free timer pane
    var free = el('div', 'pm-pane');
    var presets = el('div', 'pm-presets');
    presets.setAttribute('role', 'group');
    presets.setAttribute('aria-label', 'Block presets');
    var presetCards = Object.keys(STYLES).map(function (id) {
      var s = STYLES[id];
      var card = button('pm-card');
      card.setAttribute('data-preset', id);
      card.appendChild(el('span', 'pm-card__badge', s.focus + ' / ' + s.short));
      card.appendChild(el('span', 'pm-card__name', s.label));
      card.appendChild(el('span', 'pm-card__note', s.note));
      card.addEventListener('click', function () { setPreset(id); });
      presets.appendChild(card);
      return card;
    });
    var fields = el('div', 'pm-fields');
    var inputs = {
      focus: numberField('pmFocus', 'Focus', 'focus'),
      short: numberField('pmShort', 'Short break', 'short'),
      long: numberField('pmLong', 'Long break', 'long'),
      longEvery: numberField('pmEvery', 'Long break every', 'longEvery')
    };
    Object.keys(inputs).forEach(function (k) { fields.appendChild(inputs[k].wrap); });
    var freeNote = el('p', 'pm-note');
    var freeLock = el('div', 'pm-lock');
    var freeLockText = el('p', 'pm-note', 'A planned session is running. End it to use the free timer.');
    var freeLockBtn = button('pm-btn', 'End plan');
    freeLockBtn.addEventListener('click', endPlan);
    freeLock.appendChild(freeLockText);
    freeLock.appendChild(freeLockBtn);
    free.appendChild(freeLock);
    free.appendChild(presets);
    free.appendChild(fields);
    free.appendChild(freeNote);

    // planner pane
    var planner = el('div', 'pm-pane');
    var draftBox = el('div', 'pm-draft');
    var totalField = el('div', 'pm-field pm-field--wide');
    var totalLabel = el('label', 'pm-field__label', 'Time available');
    totalLabel.htmlFor = 'pmTotal';
    var totalInput = el('input', 'pm-input pm-input--wide');
    totalInput.type = 'text';
    totalInput.id = 'pmTotal';
    totalInput.autocomplete = 'off';
    totalInput.spellcheck = false;
    totalInput.placeholder = 'e.g. 3h, 2:30, 180 min';
    totalInput.setAttribute('aria-describedby', 'pmTotalHint');
    var totalHint = el('p', 'pm-hint');
    totalHint.id = 'pmTotalHint';
    totalField.appendChild(totalLabel);
    totalField.appendChild(totalInput);
    totalField.appendChild(totalHint);
    var chips = el('div', 'pm-chips');
    chips.setAttribute('role', 'group');
    chips.setAttribute('aria-label', 'Quick picks');
    [['1h', '1 h'], ['1h 30', '1 h 30'], ['2h', '2 h'], ['3h', '3 h'], ['4h', '4 h']].forEach(function (v) {
      var chip = button('pm-chip', v[1]);
      chip.addEventListener('click', function () {
        state.draft.input = v[0];
        totalInput.value = v[0];
        commit();
      });
      chips.appendChild(chip);
    });
    var styleSeg = seg('Block style', [['standard', 'Standard · 25 min'], ['deep', 'Deep focus · 50 min']], function (v) {
      state.draft.style = v;
      commit();
    });
    var styleNote = el('p', 'pm-hint');
    draftBox.appendChild(totalField);
    draftBox.appendChild(chips);
    draftBox.appendChild(el('p', 'pm-section', 'Block style'));
    draftBox.appendChild(styleSeg.group);
    draftBox.appendChild(styleNote);

    var summary = el('div', 'pm-summary');
    summary.setAttribute('aria-live', 'polite');
    var timeline = el('div', 'pm-timeline');
    timeline.setAttribute('aria-hidden', 'true');
    var steps = el('ol', 'pm-steps');
    var planActions = el('div', 'pm-actions');
    var startPlanBtn = button('pm-btn pm-btn--primary', 'Start plan');
    var endPlanBtn = button('pm-btn', 'End plan');
    var newPlanBtn = button('pm-btn pm-btn--primary', 'New plan');
    planActions.appendChild(startPlanBtn);
    planActions.appendChild(newPlanBtn);
    planActions.appendChild(endPlanBtn);
    planner.appendChild(draftBox);
    planner.appendChild(summary);
    planner.appendChild(timeline);
    planner.appendChild(steps);
    planner.appendChild(planActions);

    // options
    var options = el('div', 'pm-options');
    var auto = toggleRow('pmAuto', 'Auto-start next phase', 'Breaks and blocks follow on without a click.', function (on) {
      state.auto = on;
      commit();
    });
    var sound = toggleRow('pmSound', 'Chime at the end of each phase', 'A soft bell synthesised in the browser.', function (on) {
      state.sound = on;
      if (on) { unlockAudio(); chime('focus'); }
      commit();
    });
    options.appendChild(auto.row);
    options.appendChild(sound.row);

    var foot = el('p', 'pm-foot', 'The timer keeps running across pages and reloads; it is saved in this browser only.');

    [head, timer, live, progress, tabs.group, free, planner, options, foot].forEach(function (node) { panel.appendChild(node); });
    document.body.appendChild(launcher);
    document.body.appendChild(panel);

    ui = {
      launcher: launcher, launcherText: launcherText, miniArc: miniArc, panel: panel, close: close,
      arc: arc, phaseLabel: phaseLabel, time: time, sub: sub, play: play, playIcon: playIcon, playText: playText,
      resetBtn: resetBtn, skipBtn: skipBtn, live: live, progress: progress, progressText: progressText,
      progressLeft: progressLeft, track: track, tabs: tabs, free: free, presets: presetCards, inputs: inputs,
      freeNote: freeNote, freeLock: freeLock, planner: planner, draftBox: draftBox, totalInput: totalInput,
      totalHint: totalHint, styleSeg: styleSeg, styleNote: styleNote, summary: summary, timeline: timeline,
      steps: steps, startPlanBtn: startPlanBtn, endPlanBtn: endPlanBtn, newPlanBtn: newPlanBtn,
      auto: auto.input, sound: sound.input
    };

    launcher.addEventListener('click', function () {
      if (panel.hidden) openPanel(); else closePanel(false);
    });
    close.addEventListener('click', function () { closePanel(true); });
    play.addEventListener('click', function () { if (state.running) pause(); else start(); });
    resetBtn.addEventListener('click', reset);
    skipBtn.addEventListener('click', skip);
    totalInput.addEventListener('input', function () {
      state.draft.input = totalInput.value;
      save();
      renderPlanner();
    });
    totalInput.addEventListener('keydown', function (event) {
      if (event.key === 'Enter') startPlanBtn.click();
    });
    startPlanBtn.addEventListener('click', function () {
      var total = parseDuration(state.draft.input);
      if (!total || total < LIMITS.total[0] || total > LIMITS.total[1]) { totalInput.focus(); return; }
      startPlan(total, state.draft.style);
      panel.scrollTop = 0;
    });
    endPlanBtn.addEventListener('click', endPlan);
    newPlanBtn.addEventListener('click', endPlan);
    panel.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        event.stopPropagation();
        closePanel(true);
      }
    });
    // One panel at a time: opening Focus Lab closes this one (and openPanel closes Focus Lab).
    document.addEventListener('click', function (event) {
      if (event.target.closest && event.target.closest('#focusLabButton') && !panel.hidden) closePanel(false);
    }, true);
    // Audio may only start after a gesture: a reloaded running timer unlocks it on the first click.
    document.addEventListener('pointerdown', function first() {
      if (state.running) unlockAudio();
      document.removeEventListener('pointerdown', first, true);
    }, true);
    window.addEventListener('storage', function (event) {
      if (event.key !== KEY) return;
      state = load();
      render();
    });

    if (catchUp(Date.now())) save();   // write only on a change, never a blind overwrite at load
    render();
    setInterval(tick, 250);
    document.addEventListener('visibilitychange', tick);
  }

  function tick() {
    if (!state.running) return;
    var now = Date.now();
    if (now >= state.endAt) {
      // Another tab may already have moved on: adopt its state instead of chiming twice.
      var raw = null;
      try { raw = localStorage.getItem(KEY); } catch (e) { raw = null; }
      var stored = raw ? load() : state;
      if (stored.running !== state.running || stored.endAt !== state.endAt || stored.mode !== state.mode) {
        state = stored;
        render();
        return;
      }
      if (catchUp(now)) save();
    }
    render(now);
  }

  function openPanel() {
    if (window.AEFocusLab && typeof window.AEFocusLab.close === 'function') window.AEFocusLab.close();
    ui.panel.hidden = false;
    ui.launcher.setAttribute('aria-expanded', 'true');
    ui.panel.scrollTop = 0;
    render();
    requestAnimationFrame(function () { ui.panel.classList.add('is-open'); });
    ui.play.focus({ preventScroll: true });
  }

  function closePanel(returnFocus) {
    ui.panel.classList.remove('is-open');
    ui.panel.hidden = true;
    ui.launcher.setAttribute('aria-expanded', 'false');
    if (returnFocus) ui.launcher.focus();
  }

  function announce(text) { if (ui.live) ui.live.textContent = text; }

  function pressed(buttons, value) {
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-value') === value ? 'true' : 'false'); });
  }

  /* ---------------------------------------------------------------- render */
  function render(now) {
    if (!ui.panel) return;
    now = now || Date.now();
    var phase = current(), left = remaining(now), full = phase.min * MINUTE;
    var done = planFinished();
    var frac = done ? 1 : clamp(1 - left / full, 0, 1);
    var active = inProgress();
    var isBreak = phase.kind !== 'focus';

    // launcher
    ui.launcher.classList.toggle('is-running', state.running);
    ui.launcher.classList.toggle('is-paused', !state.running && active);
    ui.launcher.classList.toggle('is-break', isBreak && active);
    ui.launcher.classList.toggle('is-compact', active);
    ui.launcherText.textContent = active ? clock(left) : done ? 'Done' : 'Timer';
    ui.miniArc.setAttribute('stroke-dashoffset', (MINI * (1 - (active ? frac : 0))).toFixed(2));
    var where = PHASES[phase.kind].label + ', ' + clock(left) + ' left' + (state.running ? '' : ', paused');
    ui.launcher.setAttribute('aria-label', active ? 'Study timer: ' + where : done ? 'Study timer: plan complete' : 'Study timer');
    ui.launcher.title = ui.launcher.getAttribute('aria-label');

    // tab title
    var t = active ? (state.running ? '' : '⏸ ') + clock(left) + ' · ' + PHASES[phase.kind].title + ' — ' + baseTitle : baseTitle;
    if (document.title !== t) document.title = t;

    if (ui.panel.hidden) return;

    // dial
    ui.panel.classList.toggle('is-break', isBreak && !done);
    ui.arc.setAttribute('stroke-dashoffset', (RING * (1 - frac)).toFixed(2));
    ui.phaseLabel.textContent = done ? 'Plan complete' : PHASES[phase.kind].label;
    ui.time.textContent = done ? formatMinutes(state.plan.summary.focus) : clock(left);
    ui.time.setAttribute('aria-label', done ? 'Plan complete' : clock(left) + ' left');
    ui.sub.textContent = done ? 'of focused study' : subline(phase);
    ui.play.disabled = done;
    ui.resetBtn.disabled = done;
    ui.skipBtn.disabled = done;
    ui.play.setAttribute('aria-pressed', state.running ? 'true' : 'false');
    ui.playIcon.textContent = '';
    ui.playIcon.appendChild(svgIcon(state.running ? ICONS.pause : ICONS.play, 18));
    ui.playText.textContent = state.running ? 'Pause' : active ? 'Resume' : 'Start';

    // plan progress
    var plan = state.mode === 'plan' ? state.plan : null;
    ui.progress.hidden = !plan;
    if (plan) renderProgress(plan, now, left);

    // tabs and panes
    pressed(ui.tabs.buttons, state.tab);
    ui.free.hidden = state.tab !== 'free';
    ui.planner.hidden = state.tab !== 'plan';
    ui.auto.checked = state.auto;
    ui.sound.checked = state.sound;
    if (state.tab === 'free') renderFree();
    else renderPlanner(now);
  }

  function subline(phase) {
    if (state.mode === 'plan') {
      var p = state.plan, n = 0, total = p.summary.blocks;
      for (var i = 0; i <= p.index; i++) if (p.phases[i].kind === 'focus') n++;
      return phase.kind === 'focus' ? 'Session ' + n + ' of ' + total : 'Next: session ' + (n + 1) + ' of ' + total;
    }
    var d = state.durations, k = state.freeDone + (phase.kind === 'focus' ? 1 : 0);
    if (phase.kind !== 'focus') return 'After block ' + state.freeDone;
    var untilLong = d.longEvery - ((k - 1) % d.longEvery) - 1;
    return 'Block ' + k + ' · ' + (untilLong ? 'long break in ' + (untilLong + 1) : 'long break next');
  }

  function renderProgress(plan, now, left) {
    var doneMin = 0, totalMin = 0;
    plan.phases.forEach(function (p, i) {
      totalMin += p.min;
      if (i < plan.index) doneMin += p.min;
    });
    var cur = plan.phases[plan.index];
    var elapsed = plan.done ? totalMin : doneMin + (cur.min * MINUTE - left) / MINUTE;
    var n = 0;
    for (var i = 0; i <= plan.index; i++) if (plan.phases[i].kind === 'focus') n++;
    ui.progressText.textContent = plan.done ? 'All ' + plan.summary.blocks + ' sessions done'
      : 'Session ' + n + ' of ' + plan.summary.blocks;
    var remainingMin = Math.max(0, totalMin - elapsed);
    ui.progressLeft.textContent = plan.done ? formatMinutes(totalMin) : formatMinutes(Math.ceil(remainingMin)) + ' left' +
      (state.running ? ' · ends ' + timeOfDay(new Date(now + remainingMin * MINUTE)) : '');
    var pct = Math.round(100 * elapsed / totalMin);
    ui.track.setAttribute('aria-valuenow', String(pct));
    ui.track.setAttribute('aria-label', 'Plan progress: ' + pct + '%');
    fillTrack(ui.track, plan, plan.done ? plan.phases.length : plan.index, plan.done ? 0 : (cur.min * MINUTE - left) / (cur.min * MINUTE));
  }

  // Segments proportional to each phase; phases before `upto` are full, phase `upto` is `part` full.
  function fillTrack(track, plan, upto, part) {
    var total = plan.phases.reduce(function (a, p) { return a + p.min; }, 0);
    if (track.children.length !== plan.phases.length) {
      track.textContent = '';
      plan.phases.forEach(function (p) {
        var s = el('span', 'pm-track__seg is-' + p.kind);
        s.appendChild(el('span', 'pm-track__fill'));
        track.appendChild(s);
      });
    }
    plan.phases.forEach(function (p, i) {
      var s = track.children[i];
      s.style.flexGrow = String(p.min / total);
      s.firstChild.style.width = (i < upto ? 100 : i === upto ? Math.round(clamp(part, 0, 1) * 1000) / 10 : 0) + '%';
    });
  }

  function renderFree() {
    var locked = state.mode === 'plan';
    ui.freeLock.hidden = !locked;
    ui.presets.forEach(function (card) {
      card.setAttribute('aria-pressed', card.getAttribute('data-preset') === state.preset ? 'true' : 'false');
      card.disabled = locked;
    });
    Object.keys(ui.inputs).forEach(function (k) {
      var input = ui.inputs[k].input;
      if (document.activeElement !== input) input.value = state.durations[k];
      input.disabled = locked;
    });
    var d = state.durations;
    ui.freeNote.textContent = locked ? '' : 'Cycle: ' + d.focus + ' min focus, ' + d.short + ' min break; every ' + d.longEvery +
      ' blocks a ' + d.long + ' min long break. A change applies to the next phase that has not started.';
  }

  function renderPlanner(now) {
    if (!ui.planner) return;
    now = now || Date.now();
    var plan = state.mode === 'plan' ? state.plan : null;
    ui.draftBox.hidden = !!plan;
    ui.startPlanBtn.hidden = !!plan;
    ui.endPlanBtn.hidden = !plan || plan.done;
    ui.newPlanBtn.hidden = !plan || !plan.done;
    var shown = plan;
    if (!plan) {
      if (document.activeElement !== ui.totalInput) ui.totalInput.value = state.draft.input;
      pressed(ui.styleSeg.buttons, state.draft.style);
      ui.styleNote.textContent = style(state.draft.style).note + '.';
      var total = parseDuration(state.draft.input);
      var valid = total && total >= LIMITS.total[0] && total <= LIMITS.total[1];
      ui.totalInput.setAttribute('aria-invalid', valid ? 'false' : 'true');
      ui.totalHint.textContent = valid ? '= ' + formatMinutes(total) + ' · ends at ' + timeOfDay(new Date(now + total * MINUTE)) + ' if you start now'
        : total ? 'Choose between 10 min and 12 h.' : 'Write a time such as 3h, 2:30 or 180 min.';
      ui.startPlanBtn.disabled = !valid;
      shown = valid ? planSessions(total, state.draft.style) : null;
    }
    ui.summary.textContent = '';
    ui.timeline.textContent = '';
    ui.steps.textContent = '';
    ui.summary.hidden = ui.steps.hidden = !shown;
    ui.timeline.hidden = !shown || !!plan;   // an active plan already shows its track at the top
    if (!shown) return;

    var s = shown.summary;
    var head = el('p', 'pm-summary__lead');
    head.appendChild(document.createTextNode('For your '));
    head.appendChild(el('strong', '', formatMinutes(shown.total)));
    head.appendChild(document.createTextNode(': '));
    head.appendChild(document.createTextNode(summaryParts(s).join(' + ') + ' = '));
    head.appendChild(el('strong', '', formatMinutes(s.focus) + ' of real study'));
    head.appendChild(document.createTextNode('.'));
    ui.summary.appendChild(head);
    var stats = el('div', 'pm-stats');
    [[s.blocks, s.blocks === 1 ? 'block' : 'blocks'], [formatMinutes(s.focus), 'focus'], [formatMinutes(s.breaks), 'breaks']]
      .concat(s.buffer ? [[formatMinutes(s.buffer), 'buffer']] : [])
      .forEach(function (item) {
        var box = el('div', 'pm-stat');
        box.appendChild(el('span', 'pm-stat__value', String(item[0])));
        box.appendChild(el('span', 'pm-stat__label', item[1]));
        stats.appendChild(box);
      });
    ui.summary.appendChild(stats);

    // timeline of the draft (proportional segments, nothing filled yet)
    if (!plan) {
      var track = el('div', 'pm-track pm-track--tall');
      ui.timeline.appendChild(track);
      fillTrack(track, shown, -1, 0);
    }

    // step list with start offsets
    var at = 0, block = 0;
    shown.phases.forEach(function (p, i) {
      if (p.kind === 'focus') block++;
      var li = el('li', 'pm-step is-' + p.kind);
      if (plan) {
        if (plan.done || i < plan.index) li.className += ' is-done';
        else if (i === plan.index) { li.className += ' is-current'; li.setAttribute('aria-current', 'step'); }
      }
      li.appendChild(el('span', 'pm-step__at', offsetLabel(at)));
      li.appendChild(el('span', 'pm-step__name', p.kind === 'focus' ? 'Focus ' + block : PHASES[p.kind].label));
      li.appendChild(el('span', 'pm-step__min', p.min + ' min'));
      ui.steps.appendChild(li);
      at += p.min;
    });
  }

  function offsetLabel(min) {
    var h = Math.floor(min / 60), m = min % 60;
    return h + ':' + (m < 10 ? '0' : '') + m;
  }

  function summaryParts(s) {
    var parts = [], sizes = Object.keys(s.sizes).map(Number).sort(function (a, b) { return b - a; });
    sizes.forEach(function (size) {
      var n = s.sizes[size];
      parts.push(n + ' ' + (n === 1 ? 'block' : 'blocks') + ' of ' + size + ' min');
    });
    if (s.short) parts.push(s.short + ' short ' + (s.short === 1 ? 'break' : 'breaks') + ' of ' + s.shortMin + ' min');
    if (s.long) parts.push(s.long + ' long ' + (s.long === 1 ? 'break' : 'breaks') + ' of ' + s.longMin + ' min');
    return parts;
  }

  /* ---------------------------------------------------------------- boot */
  function addStylesheet() {
    if (!SCRIPT || !SCRIPT.src || document.querySelector('link[href*="pomodoro.css"]')) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = SCRIPT.src.replace(/js\/pomodoro\.js(\?.*)?$/, 'css/pomodoro.css');
    document.head.appendChild(link);
  }

  addStylesheet();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();

  window.AEPomodoro = {
    KEY: KEY,
    STYLES: STYLES,
    planSessions: planSessions,
    parseDuration: parseDuration,
    formatMinutes: formatMinutes,
    open: function () { if (ui.panel) openPanel(); },
    close: function () { if (ui.panel) closePanel(false); },
    start: start,
    pause: pause,
    reset: reset,
    skip: skip,
    startPlan: startPlan,
    endPlan: endPlan,
    state: function () { return JSON.parse(JSON.stringify(state)); }
  };
})();
