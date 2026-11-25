/*!
 * Aerospace Engineering Study Portal: unified "Study session" panel
 * (Pomodoro timer, evidence-based study modes, step guide, session planner and synced study sound).
 *
 * Loaded on every study page by assets/js/theme.js, right after focus-lab.js (no page carries its
 * own <script> tag for it); injects assets/css/pomodoro.css?v=20261125d. Skipped in ?print=.
 *
 * One floating planet button (#pomodoroButton) opens one minimalist panel (#pomodoroPanel):
 *   - Subject auto-mode: picks the evidence-based mode for the current subject page unless pinned;
 *   - Mode & Plan drawer (collapsed behind the top selector pill): 4 study modes + Classic + Custom +
 *     total-time session planner;
 *   - Core focus zone: 172 px SVG ring, Start/Pause + Reset + Skip, and a 2-line step guide (or
 *     wakeful rest on breaks);
 *   - Unified Sound bar + collapsible Tune drawer: drives AEFocusLab (opt-in masking in focus,
 *     optional binaural tones, 8 s fade to silence or soft alpha/masking on breaks, volume,
 *     isochronic speakers, phase chime, auto-start, and advanced Hz).
 *
 * Storage: 'ae_pomodoro' (JSON).
 * API: window.AEPomodoro = { KEY, STYLES, planSessions, guideFor, suggest, parseDuration,
 *      formatMinutes, open, openSound, close, start, pause, reset, skip, startPlan, endPlan, state }
 */
(function () {
  'use strict';

  if (window.AEPomodoro) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var SCRIPT = document.currentScript;
  var KEY = 'ae_pomodoro';
  var MINUTE = 60000;
  var LIMITS = { total: [10, 720], focus: [1, 180], short: [1, 60], long: [1, 90], longEvery: [2, 8] };

  var STYLES = {
    standard: { id: 'standard', label: 'Standard', shortLabel: 'Classic', focus: 25, short: 5, long: 15, longEvery: 4,
      minFocus: 10, stretch: 10, group: 'classic', note: '25 min focus · 5 min break · 15 min long break every 4 blocks' },
    deep: { id: 'deep', label: 'Deep focus', shortLabel: 'Classic', focus: 50, short: 10, long: 25, longEvery: 3,
      minFocus: 20, stretch: 20, group: 'classic', note: '50 min focus · 10 min break · 25 min long break every 3 blocks' },
    theory: { id: 'theory', label: 'Theory & cases', shortLabel: 'Theory', focus: 45, short: 8, long: 25, longEvery: 2,
      minFocus: 20, stretch: 5, group: 'study', note: '45 min focus · 8 min break · 25 min long break every 2 blocks',
      steps: [
        { min: 5, title: 'Pre-test', tag: 'Pre-test', text: 'Answer 3–5 questions before opening notes.' },
        { min: 15, title: 'Read one sub-block', tag: 'Read', text: 'Skeleton and a contrast table only.' },
        { min: 15, title: 'Blurt', tag: 'Blurt', text: 'Notes closed. Write all you remember.' },
        { min: 10, title: 'Colour check', tag: 'Check', text: 'Fix gaps in another colour, then 10 T/F with reasons.' }
      ],
      audio: { base: { preset: 'isolation', noise: 0.25, tone: 0, text: 'Brown mask' },
        tones: { preset: 'smr', noise: 0.25, tone: 0.15, text: 'SMR 14 Hz' } } },
    visual: { id: 'visual', label: 'Diagrams & mechanisms', shortLabel: 'Diagrams', focus: 40, short: 8, long: 20, longEvery: 3,
      minFocus: 20, stretch: 5, group: 'study', note: '40 min focus · 8 min break · 20 min long break every 3 blocks',
      steps: [
        { min: 8, title: 'Draw from memory', tag: 'Draw', text: 'Blank page: axes, phases, labels.' },
        { min: 14, title: 'Causal chain', tag: 'Chain', text: 'Processing -> microstructure -> property -> failure.' },
        { min: 10, title: 'Contrast', tag: 'Contrast', text: 'Two opposite mechanisms side by side.' },
        { min: 8, title: 'Test yourself', tag: 'Test', text: 'MCQ: say why each wrong option is wrong.' }
      ],
      audio: { base: { preset: 'isolation', noise: 0.30, tone: 0, text: 'Brown mask' },
        tones: { preset: 'alpha', noise: 0.15, tone: 0.18, text: 'Alpha 10 Hz' } } },
    worked: { id: 'worked', label: 'New topic · worked', shortLabel: 'New topic', focus: 30, short: 5, long: 15, longEvery: 3,
      minFocus: 15, stretch: 5, group: 'study', note: '30 min focus · 5 min break · 15 min long break every 3 blocks',
      steps: [
        { min: 5, title: 'Micro-theory', tag: 'Theory', text: 'Read only the rule and its hypotheses.' },
        { min: 10, title: 'Worked example', tag: 'Example', text: 'Explain why each step and hypothesis holds.' },
        { min: 15, title: 'Guided problems', tag: 'Guided', text: 'Solve 1–2 similar ones; peek only when stuck.' }
      ],
      audio: { base: { preset: 'isolation', noise: 0.30, tone: 0, text: 'Brown mask' },
        tones: { preset: 'beta', noise: 0.20, tone: 0.20, text: 'Beta 20 Hz' } } },
    problems: { id: 'problems', label: 'Problems & exam', shortLabel: 'Problems', focus: 90, short: 15, long: 25, longEvery: 2,
      minFocus: 30, stretch: 10, group: 'study', note: '90 min focus · 15 min break · 25 min long break every 2 blocks',
      steps: [
        { min: 5, title: 'Mix topics', tag: 'Mix', text: 'Pick interleaved problems. Notes and formula sheet closed.' },
        { min: 70, title: 'Solve closed-book', tag: 'Solve', text: 'Name the governing law and hypotheses first.' },
        { min: 15, title: 'Colour review', tag: 'Review', text: 'Check key. Write why each mistake happened.' }
      ],
      audio: { base: { preset: 'isolation', noise: 0.30, tone: 0, text: 'Brown mask' },
        tones: { preset: 'gamma', noise: 0.25, tone: 0.20, text: 'Gamma 40 Hz' } } }
  };
  var STUDY_MODES = ['theory', 'visual', 'worked', 'problems'];

  var REST = {
    silence: { label: 'Silence (best)', short: 'Silence on break', cue: { preset: null, fade: 8 } },
    alpha: { label: 'Alpha 10Hz', short: 'Alpha 10 Hz on break', cue: { preset: 'alpha', tone: 0.10, noise: 0.15, fade: 1.5 } },
    mask: { label: 'Mask', short: 'Masking on break', cue: { preset: 'isolation', tone: 0, noise: 0.20, fade: 1.5 } }
  };
  var REST_TEXT = 'Phone away. Water, look far away, or close eyes.';

  var SUBJECT_MODES = {
    'business-management': { mode: 'theory', tag: 'AUTO · BUSINESS' },
    'aerospace-materials-1': { mode: 'visual', tag: 'AUTO · MATERIALS' },
    'fluid-mechanics': { mode: 'problems', tag: 'AUTO · FLUIDS' },
    'engineering-mechanics': { mode: 'problems', tag: 'AUTO · MECHANICS' },
    'advanced-maths': { mode: 'problems', tag: 'AUTO · MATHS' }
  };
  var SUBJECT_ONLY = {
    'business-management': 'theory', 'aerospace-materials-1': 'visual',
    'fluid-mechanics': 'problems', 'engineering-mechanics': 'problems', 'advanced-maths': 'problems'
  };

  function suggestMeta(path) {
    var m = /\/subjects\/([^\/]+)\//.exec(path || '');
    var info = m && SUBJECT_MODES[m[1]];
    if (!info) return null;
    var mode = info.mode === 'problems' && /\/(teoria|theory)\//.test(path) ? 'worked' : info.mode;
    return { mode: mode, tag: info.tag };
  }
  function suggest(path) {
    var meta = suggestMeta(path);
    return meta ? meta.mode : null;
  }

  var PHASES = {
    focus: { label: 'Focus', title: 'Focus' },
    short: { label: 'Short break', title: 'Break' },
    long: { label: 'Long break', title: 'Long break' }
  };

  function clamp(x, lo, hi) { return Math.min(hi, Math.max(lo, x)); }
  function style(id) { return STYLES[id] || STYLES.standard; }

  /* ================================================================== planner (no DOM) */
  function breakAfter(k, s) {
    return k % s.longEvery === 0 ? { kind: 'long', min: s.long } : { kind: 'short', min: s.short };
  }

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
      else if (unit === '') total += sawHours ? v : NaN;
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

  function guideFor(styleId, phase, elapsedMin) {
    var s = STYLES[styleId], steps = s && s.steps;
    if (!phase) return null;
    if (phase.kind !== 'focus') {
      return { kind: phase.kind, title: phase.kind === 'long' ? 'Long break · wakeful rest' : 'Short break · wakeful rest',
        text: REST_TEXT, next: steps ? steps[0].title : null };
    }
    if (!steps) return null;
    var k = phase.min / s.focus, at = 0, t = clamp(+elapsedMin || 0, 0, phase.min), index = steps.length - 1;
    var bounds = steps.map(function (st) {
      var b = { start: at * k, end: (at + st.min) * k };
      at += st.min;
      return b;
    });
    for (var i = 0; i < bounds.length; i++) if (t < bounds[i].end) { index = i; break; }
    var step = steps[index], b = bounds[index];
    return {
      kind: 'focus', index: index, count: steps.length, title: step.title, text: step.text,
      tags: steps.map(function (st) { return st.tag; }), bounds: bounds,
      range: Math.round(b.start) + '–' + Math.round(b.end) + ' min',
      part: b.end > b.start ? clamp((t - b.start) / (b.end - b.start), 0, 1) : 1,
      nextIn: index < steps.length - 1 ? b.end - t : null,
      next: index < steps.length - 1 ? steps[index + 1].title : null
    };
  }

  /* ================================================================== state */
  function defaults() {
    var s = STYLES.standard;
    return {
      v: 1,
      mode: 'free',
      tab: 'free',
      preset: 'standard',
      durations: { focus: s.focus, short: s.short, long: s.long, longEvery: s.longEvery },
      freeDone: 0,
      phase: { kind: 'focus', min: s.focus },
      plan: null,
      draft: { input: '2h', style: 'standard' },
      running: false,
      started: false,
      endAt: 0,
      remaining: s.focus * MINUTE,
      auto: true,
      sound: true,
      study: 'standard',
      pinned: false,
      audio: { on: false, tones: false, rest: 'silence' }
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
    if (raw && typeof raw === 'object') {
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
      if (STYLES[raw.study]) s.study = raw.study;
      // Preserve legacy saved presets without `pinned` when `preset` was explicitly chosen (e.g. account.js -> 'deep').
      s.pinned = raw.pinned === true || (raw.pinned === undefined && raw.preset !== undefined && raw.preset !== 'standard');
      var a = raw.audio && typeof raw.audio === 'object' ? raw.audio : {};
      s.audio = { on: a.on === true, tones: a.tones === true, rest: REST[a.rest] ? a.rest : 'silence' };
    }
    var sug = suggest(location.pathname);
    var active = s.running || (s.started && !(s.mode === 'plan' && s.plan && s.plan.done));
    if (sug && !s.pinned && s.mode === 'free' && !active && STYLES[sug]) {
      var sm = STYLES[sug];
      s.preset = sug;
      s.study = sug;
      s.draft.style = sug;
      s.durations = { focus: sm.focus, short: sm.short, long: sm.long, longEvery: sm.longEvery };
      s.phase = { kind: 'focus', min: sm.focus };
      s.remaining = sm.focus * MINUTE;
    }
    return s;
  }

  var state = load();

  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* storage blocked */ }
  }

  function current(s) {
    s = s || state;
    return s.mode === 'plan' && s.plan ? s.plan.phases[s.plan.index] : s.phase;
  }

  function duration() { return current().min * MINUTE; }
  function remaining(now) { return state.running ? Math.max(0, state.endAt - (now || Date.now())) : state.remaining; }
  function planFinished() { return state.mode === 'plan' && state.plan && state.plan.done; }
  function inProgress() { return state.running || (state.started && !planFinished()); }
  function studyId() {
    if (state.mode === 'plan' && state.plan) return state.plan.style;
    return STYLES[state.preset] ? state.preset : state.study;
  }

  /* ================================================================== timer logic */
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
      completePhase(now - state.endAt > 3000);
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
    var sug = suggest(location.pathname);
    state.preset = id;
    state.study = id;
    state.draft.style = id;
    state.pinned = !(sug && id === sug);
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
    state.pinned = true;
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

  /* ================================================================== study sound (Focus Lab) */
  var lastCue = '';

  function soundKey() {
    if (!state.audio.on) return 'off';
    if (!state.running) return 'stop';
    var kind = current().kind;
    return kind === 'focus' ? 'focus:' + studyId() + ':' + (state.audio.tones ? 'tones' : 'base') : 'rest:' + state.audio.rest;
  }

  function soundCue(key) {
    var s = style(studyId()), label = (STYLES[studyId()] ? s.label : 'Custom') + ' · ';
    if (key === 'off' || key === 'stop') return { preset: null, fade: 1, label: key === 'off' ? '' : label + 'paused' };
    if (key.indexOf('rest:') === 0) {
      var r = REST[state.audio.rest].cue;
      return { preset: r.preset, tone: r.tone, noise: r.noise, fade: r.fade, label: label + 'break' };
    }
    var a = STYLES[studyId()] && STYLES[studyId()].audio;
    var c = a ? a[state.audio.tones ? 'tones' : 'base'] : { preset: 'keep' };
    return { preset: c.preset, tone: c.tone, noise: c.noise, fade: 1.5, label: label + 'focus' };
  }

  function syncSound() {
    var key = soundKey(), lab = window.AEFocusLab;
    if (key === lastCue) return;
    var was = lastCue;
    lastCue = key;
    if ((was === '' || was === 'off') && (key === 'off' || key === 'stop')) return;
    if (lab && typeof lab.cue === 'function') lab.cue(soundCue(key));
  }

  function setAudio(name, value) {
    state.audio[name] = value;
    commit();
  }

  /* ================================================================== chime (Web Audio) */
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
    setTimeout(function () { try { master.disconnect(); } catch (e) { /* gone */ } }, (notes.length * 0.16 + 1.6) * 1000);
  }

  /* ================================================================== UI */
  var ui = {};
  var modeDrawerOpen = false;
  var tuneDrawerOpen = false;
  var customOpen = false;
  var lastGuide = '';
  var baseTitle = '';
  var RING = 2 * Math.PI * 52;
  var MINI = 2 * Math.PI * 9;
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
    close: ['M6 6l12 12', 'M18 6L6 18'],
    phones: ['M4 14v-2a8 8 0 0 1 16 0v2', 'M4 14h3v6H5a1 1 0 0 1-1-1z', 'M20 14h-3v6h2a1 1 0 0 0 1-1z'],
    chevron: ['M6 9l6 6 6-6']
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

  function toggleRow(id, title, text, onChange, compact) {
    var row = el('label', compact ? 'pm-switch pm-switch--compact' : 'pm-switch');
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
    box.appendChild(el('span', 'pm-field__unit', name === 'longEvery' ? 'blk' : 'min'));
    wrap.appendChild(lab);
    wrap.appendChild(box);
    input.addEventListener('change', function () { setDuration(name, input.value); });
    return { wrap: wrap, input: input };
  }

  function slider(id, label, min, max, step, value, onInput) {
    var row = el('div', 'pm-slider');
    var head = el('div', 'pm-slider__head');
    var name = el('label', 'pm-slider__label', label);
    name.htmlFor = id;
    var out = el('output', 'pm-slider__value');
    out.htmlFor = id;
    head.appendChild(name);
    head.appendChild(out);
    var input = el('input', 'pm-range');
    input.type = 'range';
    input.id = id;
    input.min = min;
    input.max = max;
    input.step = step;
    input.value = value;
    input.addEventListener('input', function () { onInput(+input.value); });
    row.appendChild(head);
    row.appendChild(input);
    return { row: row, input: input, out: out };
  }

  function build() {
    if (document.getElementById('pomodoroButton') || !document.body) return;
    baseTitle = document.title;

    // single floating planet launcher
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
    var launcherText = el('span', 'pm-launcher__label', 'Study');
    launcher.appendChild(launcherText);

    var panel = el('section', 'pm-panel');
    panel.id = 'pomodoroPanel';
    panel.hidden = true;
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-modal', 'false');
    panel.setAttribute('aria-labelledby', 'pomodoroTitle');

    // header
    var head = el('header', 'pm-head');
    var brand = el('div', 'pm-head__brand');
    if (window.AESite && typeof window.AESite.mark === 'function') {
      var seal = el('span', 'pm-brand-seal');
      seal.setAttribute('aria-hidden', 'true');
      seal.appendChild(window.AESite.mark(22));
      brand.appendChild(seal);
    }
    var title = el('h2', 'pm-title', 'Study session');
    title.id = 'pomodoroTitle';
    brand.appendChild(title);
    var close = button('pm-icon-btn', '', 'Close study session');
    close.appendChild(svgIcon(ICONS.close, 16));
    head.appendChild(brand);
    head.appendChild(close);

    // single mode selector pill
    var meta = suggestMeta(location.pathname);
    var sug = meta ? meta.mode : null;
    var picker = button('pm-picker');
    picker.setAttribute('aria-expanded', 'false');
    var pickerMain = el('span', 'pm-picker__main');
    var pickerRight = el('span', 'pm-picker__right');
    var pickerAuto = el('span', 'pm-picker__auto', meta ? meta.tag : '');
    var pickerChev = el('span', 'pm-picker__chev');
    pickerChev.appendChild(svgIcon(ICONS.chevron, 14));
    pickerRight.appendChild(pickerAuto);
    pickerRight.appendChild(pickerChev);
    picker.appendChild(pickerMain);
    picker.appendChild(pickerRight);

    // collapsible Mode & Plan drawer
    var modeDrawer = el('div', 'pm-drawer pm-drawer--mode');
    modeDrawer.hidden = true;
    var modeList = el('div', 'pm-mode-list');
    modeList.setAttribute('role', 'group');
    modeList.setAttribute('aria-label', 'Study type');
    var modeRows = STUDY_MODES.map(function (id) {
      var s = STYLES[id];
      var row = button('pm-mode-row');
      row.setAttribute('data-preset', id);
      row.appendChild(el('span', 'pm-mode-row__name', s.label));
      var right = el('span', 'pm-mode-row__meta');
      right.appendChild(el('span', 'pm-mode-row__times', s.focus + ' / ' + s.short));
      if (id === sug) right.appendChild(el('span', 'pm-mode-row__auto', 'AUTO'));
      row.appendChild(right);
      row.addEventListener('click', function () {
        setPreset(id);
        modeDrawerOpen = false;
        render();
      });
      modeList.appendChild(row);
      return row;
    });
    modeDrawer.appendChild(modeList);

    var classicRow = el('div', 'pm-classic');
    classicRow.setAttribute('role', 'group');
    classicRow.setAttribute('aria-label', 'Classic and custom durations');
    classicRow.appendChild(el('span', 'pm-classic__label', 'Classic'));
    var classicChips = ['standard', 'deep'].map(function (id) {
      var chip = button('pm-chip', STYLES[id].focus + ' / ' + STYLES[id].short, 'Classic ' + STYLES[id].label);
      chip.setAttribute('data-preset', id);
      chip.addEventListener('click', function () {
        setPreset(id);
        modeDrawerOpen = false;
        render();
      });
      classicRow.appendChild(chip);
      return chip;
    });
    var customChip = button('pm-chip pm-chip--ghost', 'Custom…');
    classicRow.appendChild(customChip);
    modeDrawer.appendChild(classicRow);

    var customBox = el('div', 'pm-custom');
    customBox.hidden = true;
    var fields = el('div', 'pm-fields');
    var inputs = {
      focus: numberField('pmFocus', 'Focus', 'focus'),
      short: numberField('pmShort', 'Short', 'short'),
      long: numberField('pmLong', 'Long', 'long'),
      longEvery: numberField('pmEvery', 'Every', 'longEvery')
    };
    Object.keys(inputs).forEach(function (k) { fields.appendChild(inputs[k].wrap); });
    customBox.appendChild(fields);
    modeDrawer.appendChild(customBox);

    var modeLock = el('p', 'pm-note', 'A plan is running. End it to switch mode.');
    modeDrawer.appendChild(modeLock);

    // compact planner inside Mode & Plan drawer
    var planner = el('div', 'pm-planner');
    planner.appendChild(el('p', 'pm-section', 'Plan by total time'));
    var chips = el('div', 'pm-chips');
    chips.setAttribute('role', 'group');
    chips.setAttribute('aria-label', 'Quick total time picks');
    [['1h', '1 h'], ['1h 30', '1 h 30'], ['2h', '2 h'], ['3h', '3 h']].forEach(function (v) {
      var chip = button('pm-chip', v[1]);
      chip.setAttribute('data-total', v[0]);
      chip.addEventListener('click', function () {
        state.draft.input = v[0];
        totalInput.value = v[0];
        save();
        renderPlanner();
      });
      chips.appendChild(chip);
    });
    var totalInput = el('input', 'pm-input pm-input--compact');
    totalInput.type = 'text';
    totalInput.id = 'pmTotal';
    totalInput.autocomplete = 'off';
    totalInput.spellcheck = false;
    totalInput.placeholder = 'e.g. 2:30, 180m';
    totalInput.setAttribute('aria-label', 'Total time available');
    var draftRow = el('div', 'pm-draft-row');
    draftRow.appendChild(chips);
    draftRow.appendChild(totalInput);
    var summary = el('p', 'pm-plan-line');
    summary.setAttribute('aria-live', 'polite');
    var steps = el('ol', 'pm-steps');
    var planActions = el('div', 'pm-actions');
    var startPlanBtn = button('pm-btn pm-btn--primary pm-btn--full', 'Start plan');
    var endPlanBtn = button('pm-btn pm-btn--full', 'End plan');
    var newPlanBtn = button('pm-btn pm-btn--primary pm-btn--full', 'New plan');
    planActions.appendChild(startPlanBtn);
    planActions.appendChild(newPlanBtn);
    planActions.appendChild(endPlanBtn);
    planner.appendChild(draftRow);
    planner.appendChild(summary);
    planner.appendChild(steps);
    planner.appendChild(planActions);
    modeDrawer.appendChild(planner);

    // core dial + controls
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

    var controls = el('div', 'pm-controls');
    var play = button('pm-play');
    var playIcon = el('span', 'pm-play__icon');
    var playText = el('span', 'pm-play__text');
    play.appendChild(playIcon);
    play.appendChild(playText);
    var resetBtn = button('pm-ctrl', '', 'Reset this phase');
    resetBtn.appendChild(svgIcon(ICONS.reset, 15));
    resetBtn.appendChild(el('span', '', 'Reset'));
    var skipBtn = button('pm-ctrl', '', 'Skip to next phase');
    skipBtn.appendChild(svgIcon(ICONS.skip, 15));
    skipBtn.appendChild(el('span', '', 'Skip'));
    controls.appendChild(play);
    controls.appendChild(resetBtn);
    controls.appendChild(skipBtn);
    timer.appendChild(controls);

    var live = el('p', 'pm-sr');
    live.setAttribute('aria-live', 'polite');

    // active plan progress (only shown when a plan is active)
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

    // compact 2-line step guide
    var guide = el('div', 'pm-guide');
    var guideHead = el('div', 'pm-guide__head');
    var guideStep = el('span', 'pm-guide__step');
    var guideNext = el('span', 'pm-guide__next');
    guideHead.appendChild(guideStep);
    guideHead.appendChild(guideNext);
    var guideTitle = el('p', 'pm-guide__title');
    var guideText = el('p', 'pm-guide__text');
    var guideBar = el('ol', 'pm-guide__bar');
    guideBar.setAttribute('aria-hidden', 'true');
    [guideHead, guideTitle, guideText, guideBar].forEach(function (n) { guide.appendChild(n); });

    // unified bottom Sound bar + collapsible Tune drawer
    var soundCard = el('div', 'pm-sound');
    var soundBar = el('div', 'pm-sound__row');
    var soundLeft = el('div', 'pm-sound__left');
    var phones = el('span', 'pm-sound__icon');
    phones.appendChild(svgIcon(ICONS.phones, 17));
    var audioToggle = toggleRow('pmAudio', 'Sound', '', function (on) { setAudio('on', on); }, true);
    var soundSub = el('span', 'pm-sound__sub');
    audioToggle.row.querySelector('.pm-switch__text').appendChild(soundSub);
    soundLeft.appendChild(phones);
    soundLeft.appendChild(audioToggle.row);
    var tuneBtn = button('pm-tune-btn', 'Tune');
    var tuneChev = el('span', 'pm-tune-btn__chev');
    tuneChev.appendChild(svgIcon(ICONS.chevron, 13));
    tuneBtn.appendChild(tuneChev);
    tuneBtn.setAttribute('aria-expanded', 'false');
    soundBar.appendChild(soundLeft);
    soundBar.appendChild(tuneBtn);

    var tuneDrawer = el('div', 'pm-drawer pm-drawer--tune');
    tuneDrawer.hidden = true;

    tuneDrawer.appendChild(el('p', 'pm-section', 'Focus audio'));
    var focusAudioSeg = seg('Focus audio', [['base', 'Masking (best)'], ['tones', 'Binaural']], function (v) {
      setAudio('tones', v === 'tones');
    });
    focusAudioSeg.group.className += ' pm-seg--full';
    tuneDrawer.appendChild(focusAudioSeg.group);

    tuneDrawer.appendChild(el('p', 'pm-section', 'On breaks'));
    var restSeg = seg('Sound on breaks', Object.keys(REST).map(function (k) { return [k, REST[k].label]; }), function (v) {
      setAudio('rest', v);
    });
    restSeg.group.className += ' pm-seg--full';
    tuneDrawer.appendChild(restSeg.group);

    var labState = window.AEFocusLab ? window.AEFocusLab.state() : { volume: 0.75, iso: false, carrier: 200, beat: 40 };
    var volSlider = slider('pmVol', 'Volume', 0, 100, 1, Math.round((labState.volume == null ? 0.75 : labState.volume) * 100), function (v) {
      if (window.AEFocusLab && window.AEFocusLab.setVolume) window.AEFocusLab.setVolume(v / 100);
    });
    tuneDrawer.appendChild(volSlider.row);

    var toggles = el('div', 'pm-toggles');
    var isoToggle = toggleRow('pmIso', 'Speakers (isochronic)', '', function (on) {
      if (window.AEFocusLab && window.AEFocusLab.setIsochronic) window.AEFocusLab.setIsochronic(on);
    }, true);
    var chimeToggle = toggleRow('pmSound', 'Phase chime', '', function (on) {
      state.sound = on;
      if (on) { unlockAudio(); chime('focus'); }
      commit();
    }, true);
    var autoToggle = toggleRow('pmAuto', 'Auto-start', '', function (on) {
      state.auto = on;
      commit();
    }, true);
    toggles.appendChild(isoToggle.row);
    toggles.appendChild(chimeToggle.row);
    toggles.appendChild(autoToggle.row);
    tuneDrawer.appendChild(toggles);

    var adv = el('details', 'pm-adv');
    adv.appendChild(el('summary', '', 'Advanced Hz'));
    var carrierSlider = slider('pmCarrier', 'Carrier', 100, 432, 1, labState.carrier || 200, function (v) {
      if (window.AEFocusLab && window.AEFocusLab.setCustomHz) window.AEFocusLab.setCustomHz(v, window.AEFocusLab.state().beat);
    });
    var beatSlider = slider('pmBeat', 'Beat', 1, 45, 1, labState.beat || 40, function (v) {
      if (window.AEFocusLab && window.AEFocusLab.setCustomHz) window.AEFocusLab.setCustomHz(window.AEFocusLab.state().carrier, v);
    });
    adv.appendChild(carrierSlider.row);
    adv.appendChild(beatSlider.row);
    tuneDrawer.appendChild(adv);
    tuneDrawer.appendChild(el('p', 'pm-hint', 'Entrainment evidence is mixed; treat audio as a low-volume masking routine. Resumes on first click across pages.'));

    soundCard.appendChild(soundBar);
    soundCard.appendChild(tuneDrawer);

    [head, picker, modeDrawer, timer, progress, guide, live, soundCard].forEach(function (node) { panel.appendChild(node); });
    document.body.appendChild(launcher);
    document.body.appendChild(panel);

    ui = {
      launcher: launcher, launcherText: launcherText, miniArc: miniArc, panel: panel, close: close,
      picker: picker, pickerMain: pickerMain, pickerAuto: pickerAuto, modeDrawer: modeDrawer,
      modeRows: modeRows, classicChips: classicChips, customChip: customChip, customBox: customBox,
      inputs: inputs, modeLock: modeLock, planner: planner, totalInput: totalInput, summary: summary,
      steps: steps, startPlanBtn: startPlanBtn, endPlanBtn: endPlanBtn, newPlanBtn: newPlanBtn,
      chips: chips, arc: arc, phaseLabel: phaseLabel, time: time, sub: sub, play: play, playIcon: playIcon,
      playText: playText, resetBtn: resetBtn, skipBtn: skipBtn, live: live, progress: progress,
      progressText: progressText, progressLeft: progressLeft, track: track,
      guide: guide, guideStep: guideStep, guideNext: guideNext, guideTitle: guideTitle, guideText: guideText, guideBar: guideBar,
      audioOn: audioToggle.input, soundSub: soundSub, tuneBtn: tuneBtn, tuneDrawer: tuneDrawer,
      focusAudioSeg: focusAudioSeg, restSeg: restSeg, volSlider: volSlider, iso: isoToggle.input,
      sound: chimeToggle.input, auto: autoToggle.input, carrierSlider: carrierSlider, beatSlider: beatSlider
    };

    picker.addEventListener('click', function () {
      modeDrawerOpen = !modeDrawerOpen;
      if (modeDrawerOpen) tuneDrawerOpen = false;
      render();
    });
    customChip.addEventListener('click', function () {
      customOpen = !customOpen;
      render();
    });
    tuneBtn.addEventListener('click', function () {
      tuneDrawerOpen = !tuneDrawerOpen;
      if (tuneDrawerOpen) modeDrawerOpen = false;
      render();
    });
    window.addEventListener('aefocuslab:change', function () { if (!ui.panel.hidden) renderSoundControls(); });

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
      modeDrawerOpen = false;
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
    document.addEventListener('pointerdown', function first() {
      if (state.running) unlockAudio();
      document.removeEventListener('pointerdown', first, true);
    }, true);
    window.addEventListener('storage', function (event) {
      if (event.key !== KEY) return;
      state = load();
      render();
    });

    if (catchUp(Date.now())) save();
    render();
    setInterval(tick, 250);
    document.addEventListener('visibilitychange', tick);

    var pending = null;
    try { pending = JSON.parse(sessionStorage.getItem('ae_pomodoro_pending') || 'null'); sessionStorage.removeItem('ae_pomodoro_pending'); } catch (e) { pending = null; }
    if (pending && pending.minutes > 0) {
      var pStyle = SUBJECT_ONLY[pending.subject] || 'standard';
      state.pinned = true;
      startPlan(pending.minutes, pStyle);
      openPanel();
    }
  }

  function tick() {
    if (!state.running) return;
    var now = Date.now();
    if (now >= state.endAt) {
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
    if (window.AESideris && typeof window.AESideris.close === 'function') window.AESideris.close();
    ui.panel.hidden = false;
    ui.launcher.setAttribute('aria-expanded', 'true');
    ui.panel.scrollTop = 0;
    render();
    requestAnimationFrame(function () { ui.panel.classList.add('is-open'); });
    ui.play.focus({ preventScroll: true });
  }

  function openSound() {
    modeDrawerOpen = false;
    tuneDrawerOpen = true;
    openPanel();
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
    var g = done ? null : guideFor(studyId(), phase, (full - left) / MINUTE);
    syncSound();

    var gkey = g && active ? g.kind + (g.kind === 'focus' ? g.index : '') : '';
    if (gkey !== lastGuide) {
      if (state.running && g && g.kind === 'focus' && g.index > 0 && lastGuide.indexOf('focus') === 0) {
        announce('Step ' + (g.index + 1) + ': ' + g.title);
      }
      lastGuide = gkey;
    }

    // single planet launcher
    ui.launcher.classList.toggle('is-running', state.running);
    ui.launcher.classList.toggle('is-paused', !state.running && active);
    ui.launcher.classList.toggle('is-break', isBreak && active);
    ui.launcher.classList.toggle('is-compact', active);
    ui.launcher.classList.toggle('is-audio', state.audio.on && state.running);
    ui.launcherText.textContent = active ? clock(left) : done ? 'Done' : 'Study';
    ui.miniArc.setAttribute('stroke-dashoffset', (MINI * (1 - (active ? frac : 0))).toFixed(2));
    var where = PHASES[phase.kind].label + ', ' + clock(left) + ' left' + (state.running ? '' : ', paused') +
      (g && g.kind === 'focus' ? ', ' + g.title : '');
    ui.launcher.setAttribute('aria-label', active ? 'Study session: ' + where : done ? 'Study session: plan complete' : 'Study session');
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
    ui.playIcon.appendChild(svgIcon(state.running ? ICONS.pause : ICONS.play, 16));
    ui.playText.textContent = state.running ? 'Pause' : active ? 'Resume' : 'Start';

    // plan progress
    var plan = state.mode === 'plan' ? state.plan : null;
    ui.progress.hidden = !plan;
    if (plan) renderProgress(plan, now, left);

    renderModePicker(plan, now);
    renderGuide(g, active);
    renderSoundControls();
  }

  function renderModePicker(plan, now) {
    var meta = suggestMeta(location.pathname);
    var s = style(studyId()), d = state.durations;
    var shortName = plan ? s.shortLabel : (STYLES[state.preset] ? s.shortLabel : 'Custom');
    var times = plan ? (s.focus + '/' + s.short) : (d.focus + '/' + d.short);
    ui.pickerMain.textContent = shortName + ' · ' + times;
    var showAuto = !!(meta && !plan && !state.pinned && state.preset === meta.mode);
    ui.pickerAuto.hidden = !showAuto;
    ui.picker.setAttribute('aria-expanded', modeDrawerOpen ? 'true' : 'false');
    ui.picker.classList.toggle('is-open', modeDrawerOpen);
    ui.modeDrawer.hidden = !modeDrawerOpen;

    if (!modeDrawerOpen) return;
    var chosen = plan ? state.plan.style : state.preset;
    ui.modeRows.concat(ui.classicChips).forEach(function (b) {
      b.setAttribute('aria-pressed', b.getAttribute('data-preset') === chosen ? 'true' : 'false');
      b.disabled = !!plan;
    });
    ui.customChip.setAttribute('aria-pressed', (customOpen || state.preset === 'custom') ? 'true' : 'false');
    ui.customChip.disabled = !!plan;
    ui.customBox.hidden = !(customOpen || state.preset === 'custom') || !!plan;
    Object.keys(ui.inputs).forEach(function (k) {
      var input = ui.inputs[k].input;
      if (document.activeElement !== input) input.value = state.durations[k];
      input.disabled = !!plan;
    });
    ui.modeLock.hidden = !plan;
    renderPlanner(now);
  }

  function renderGuide(g, active) {
    ui.guide.hidden = !g;
    if (!g) return;
    ui.guide.classList.toggle('is-break', g.kind !== 'focus');
    if (g.kind !== 'focus') {
      ui.guideStep.textContent = g.kind === 'long' ? 'Wakeful rest · long break' : 'Wakeful rest · short break';
      ui.guideNext.textContent = g.next ? 'Next: ' + g.next : '';
      ui.guideNext.hidden = !g.next;
      ui.guideTitle.textContent = 'Wakeful rest';
      ui.guideText.textContent = g.text;
      ui.guideBar.hidden = true;
      return;
    }
    ui.guideStep.textContent = 'STEP ' + (g.index + 1) + ' / ' + g.count;
    ui.guideNext.hidden = false;
    ui.guideNext.textContent = g.nextIn !== null
      ? (active ? 'NEXT IN ' + clock(g.nextIn * MINUTE) : g.range)
      : g.range;
    ui.guideTitle.textContent = g.title;
    ui.guideText.textContent = g.text;
    ui.guideBar.hidden = false;
    var bar = ui.guideBar;
    if (bar.getAttribute('data-tags') !== g.tags.join('|')) {
      bar.setAttribute('data-tags', g.tags.join('|'));
      bar.textContent = '';
      g.tags.forEach(function (tag) {
        var li = el('li', 'pm-guide__seg');
        var tr = el('span', 'pm-guide__track');
        tr.appendChild(el('span', 'pm-guide__fill'));
        li.appendChild(tr);
        li.appendChild(el('span', 'pm-guide__tag', tag));
        bar.appendChild(li);
      });
    }
    var total = g.bounds[g.bounds.length - 1].end || 1;
    g.bounds.forEach(function (b, i) {
      var li = bar.children[i];
      li.style.flexGrow = String((b.end - b.start) / total);
      li.className = 'pm-guide__seg' + (i < g.index ? ' is-done' : i === g.index ? ' is-current' : '');
      li.firstChild.firstChild.style.width = (i < g.index ? 100 : i === g.index && active ? Math.round(g.part * 1000) / 10 : 0) + '%';
    });
  }

  function renderSoundControls() {
    ui.audioOn.checked = state.audio.on;
    var s = STYLES[studyId()];
    var focusLabel = s && s.audio ? s.audio[state.audio.tones ? 'tones' : 'base'].text : 'Mixer preset';
    var breakLabel = REST[state.audio.rest].short;
    if (!state.audio.on) {
      ui.soundSub.textContent = 'Off';
    } else if (current().kind !== 'focus' && state.running) {
      ui.soundSub.textContent = breakLabel;
    } else {
      ui.soundSub.textContent = focusLabel + ' · ' + breakLabel;
    }
    ui.tuneBtn.setAttribute('aria-expanded', tuneDrawerOpen ? 'true' : 'false');
    ui.tuneBtn.classList.toggle('is-open', tuneDrawerOpen);
    ui.tuneDrawer.hidden = !tuneDrawerOpen;

    if (!tuneDrawerOpen) return;
    pressed(ui.focusAudioSeg.buttons, state.audio.tones ? 'tones' : 'base');
    pressed(ui.restSeg.buttons, state.audio.rest);
    ui.auto.checked = state.auto;
    ui.sound.checked = state.sound;
    if (window.AEFocusLab) {
      var ls = window.AEFocusLab.state();
      var volPct = Math.round((ls.volume == null ? 0.75 : ls.volume) * 100);
      ui.volSlider.input.value = volPct;
      ui.volSlider.out.textContent = volPct + '%';
      ui.iso.checked = !!ls.iso;
      ui.carrierSlider.input.value = ls.carrier;
      ui.carrierSlider.out.textContent = ls.carrier + ' Hz';
      ui.beatSlider.input.value = ls.beat;
      ui.beatSlider.out.textContent = ls.beat + ' Hz';
    }
  }

  function subline(phase) {
    if (state.mode === 'plan') {
      var p = state.plan, n = 0, total = p.summary.blocks;
      for (var i = 0; i <= p.index; i++) if (p.phases[i].kind === 'focus') n++;
      return phase.kind === 'focus' ? 'Session ' + n + ' of ' + total : 'Next: session ' + (n + 1) + ' of ' + total;
    }
    var d = state.durations, k = state.freeDone + (phase.kind === 'focus' ? 1 : 0);
    if (phase.kind !== 'focus') return 'Next: Block ' + (state.freeDone + 1);
    return 'Block ' + k + ' · long break every ' + d.longEvery;
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

  function renderPlanner() {
    if (!ui.planner) return;
    var plan = state.mode === 'plan' ? state.plan : null;
    ui.startPlanBtn.hidden = !!plan;
    ui.endPlanBtn.hidden = !plan || plan.done;
    ui.newPlanBtn.hidden = !plan || !plan.done;
    [].forEach.call(ui.chips.children, function (c) {
      c.setAttribute('aria-pressed', !plan && c.getAttribute('data-total') === state.draft.input ? 'true' : 'false');
      c.disabled = !!plan;
    });
    ui.totalInput.disabled = !!plan;

    var shown = plan;
    if (!plan) {
      if (document.activeElement !== ui.totalInput) ui.totalInput.value = state.draft.input;
      var total = parseDuration(state.draft.input);
      var valid = total && total >= LIMITS.total[0] && total <= LIMITS.total[1];
      ui.totalInput.setAttribute('aria-invalid', valid ? 'false' : 'true');
      ui.startPlanBtn.disabled = !valid;
      shown = valid ? planSessions(total, state.draft.style) : null;
      if (!shown) {
        ui.summary.textContent = total ? 'Choose 10 min to 12 h.' : 'Write a time such as 2h, 1:30 or 90m.';
        ui.steps.hidden = true;
        return;
      }
      ui.summary.textContent = summaryCompact(shown.summary);
      ui.steps.hidden = true;
      return;
    }

    ui.summary.textContent = formatMinutes(shown.summary.focus) + ' focus · ' + shown.summary.blocks +
      (shown.summary.blocks === 1 ? ' block' : ' blocks');
    ui.steps.hidden = false;
    ui.steps.textContent = '';
    var at = 0, block = 0;
    shown.phases.forEach(function (p, i) {
      if (p.kind === 'focus') block++;
      var li = el('li', 'pm-step is-' + p.kind);
      if (plan.done || i < plan.index) li.className += ' is-done';
      else if (i === plan.index) { li.className += ' is-current'; li.setAttribute('aria-current', 'step'); }
      li.appendChild(el('span', 'pm-step__at', offsetLabel(at)));
      li.appendChild(el('span', 'pm-step__name', p.kind === 'focus' ? 'Focus ' + block : PHASES[p.kind].label));
      li.appendChild(el('span', 'pm-step__min', p.min + ' min'));
      ui.steps.appendChild(li);
      at += p.min;
    });
  }

  function summaryCompact(s) {
    var sizes = [];
    Object.keys(s.sizes).map(Number).sort(function (a, b) { return b - a; }).forEach(function (sz) {
      for (var k = 0; k < s.sizes[sz]; k++) sizes.push(sz + 'm');
    });
    var br = [];
    if (s.short) br.push(s.shortMin + 'm break');
    if (s.long) br.push(s.longMin + 'm long');
    return s.blocks + (s.blocks === 1 ? ' block' : ' blocks') + ' (' + sizes.join(' + ') + ')' +
      (br.length ? ' · ' + br.join(' · ') : '');
  }

  function offsetLabel(min) {
    var h = Math.floor(min / 60), m = min % 60;
    return h + ':' + (m < 10 ? '0' : '') + m;
  }

  /* ---------------------------------------------------------------- boot */
  function addStylesheet() {
    if (!SCRIPT || !SCRIPT.src || document.querySelector('link[href*="pomodoro.css"]')) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = SCRIPT.src.replace(/js\/pomodoro\.js(\?.*)?$/, 'css/pomodoro.css?v=20261125d');
    document.head.appendChild(link);
  }

  addStylesheet();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();

  window.AEPomodoro = {
    KEY: KEY,
    STYLES: STYLES,
    planSessions: planSessions,
    guideFor: guideFor,
    suggest: suggest,
    parseDuration: parseDuration,
    formatMinutes: formatMinutes,
    open: function () { if (ui.panel) openPanel(); },
    openSound: function () { if (ui.panel) openSound(); },
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
