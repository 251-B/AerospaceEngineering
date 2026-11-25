/*!
 * Aerospace Engineering Study Portal: "Focus Lab" (headless Web Audio study-sound engine).
 *
 * Loaded on every study page by assets/js/theme.js, right before assets/js/pomodoro.js.
 * Controlled from the unified "Study session" panel (no separate floating button or panel).
 * Skipped in the PDF print mode (?print=...).
 *
 * Audio graph (Web Audio API only, no audio files):
 *   oscL (sine, carrier)        -> panL (pan -1) ----------------\
 *   oscR (sine, carrier + beat) -> gateR -> panR (pan +1) --------> toneBus -> pulse -> master
 *   lfo (sine, beat) -> soft-square shaper -> depth ----------------------------^ (pulse.gain)
 *   loop of brown or pink noise (AudioBuffer) -> fade -> noiseBus -----------------> master
 *   master -> destination, master -> analyser
 * Binaural mode: panL = -1, gateR = 1, pulse = 1, depth = 0 (each ear hears its own tone).
 * Isochronic mode: panL = 0 (both ears), gateR = 0, pulse = 0.5*sqrt2 + 0.5*sqrt2*square(beat).
 * Every gain, pan and frequency change is a linear or exponential ramp, so nothing clicks.
 *
 * Study timer sync: AEFocusLab.cue(spec) lets assets/js/pomodoro.js drive the sound phase by phase
 * ({ preset, noise, tone, fade, label }; preset null fades to silence, 'keep' keeps the engine's
 * current sound). A cue that cannot start (hidden tab, or a new page before any gesture) waits for
 * the tab to be visible and the first click or key.
 *
 * Storage: 'ae_focus_lab' (JSON: preset, frequencies, levels, volume, noise colour, iso, playing).
 * API: window.AEFocusLab = { PRESETS, KEY, LIMITS, noiseBuffer, createEngine, cue, applyPreset,
 *      setVolume, setIsochronic, setCustomHz, start, stop, toggle, open, close, state }
 */
(function () {
  'use strict';

  if (window.AEFocusLab) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var KEY = 'ae_focus_lab';
  var LIMITS = { carrier: [100, 432], beat: [1, 45] };
  var TONE_MAX = 0.3;     // gain of the tone bus at 100 %
  var NOISE_MAX = 0.75;   // gain of the noise bus at 100 %
  var NOISE_RMS = 0.2;    // RMS of the generated noise loops
  var NOISE_SECONDS = 12; // length of each noise loop
  var TIME = { fadeIn: 0.6, fadeOut: 0.35, glide: 0.25, level: 0.08, swap: 0.5 };

  // Wording kept to what the evidence supports: behavioural effects of binaural beats are modest and
  // their EEG entrainment is unproven (Garcia-Argibay 2019; Ingendoh 2023); low-level masking is the
  // best-supported use (Awada 2022), and rhythmic sound can hurt reading and verbal memory (Kampfe 2011).
  var PRESETS = [
    { id: 'gamma', name: 'Calculation & Debugging', band: 'gamma', carrier: 200, beat: 40, tones: true,
      noise: 'brown', level: 0.25, use: 'Problem solving · derivations · debugging',
      text: 'A 40 Hz beat over brown noise. Some studies report small gains in attention; the brain-wave mechanism is unproven, so use it as a focus cue.' },
    { id: 'beta', name: 'Active Programming', band: 'beta', carrier: 250, beat: 20, tones: true,
      noise: 'pink', level: 0.20, use: 'Practice problems · writing code',
      text: 'A 20 Hz beat over pink noise: a steady cue for step-by-step work. Measured effects are modest and not specific to the band.' },
    { id: 'smr', name: 'Technical Reading & Papers', band: 'smr', carrier: 200, beat: 14, tones: true,
      noise: 'brown', level: 0.30, use: 'Reading notes · papers · documentation',
      text: 'A 14 Hz beat over brown noise. For reading, quiet masking matters more than the beat: keep the tones low, rhythmic sound can disturb verbal memory.' },
    { id: 'alpha', name: 'Assimilation & Flow', band: 'alpha', carrier: 220, beat: 10, tones: true,
      noise: 'pink', level: 0.15, use: 'Light review · noisy breaks',
      text: 'A 10 Hz beat over soft pink noise, for light review or a break in a noisy room. Evidence for relaxation or memory gains is mixed.' },
    { id: 'isolation', name: 'Pure Isolation', band: 'none', carrier: 200, beat: 40, tones: false,
      noise: 'brown', level: 0.50, use: 'Masking a noisy room',
      text: 'Brown noise only (1/f²), no tones: masks background chatter. The best-supported option; keep it barely above the room.' }
  ];

  function clamp(x, lo, hi) { return Math.min(hi, Math.max(lo, x)); }
  function num(x, fallback) { return typeof x === 'number' && isFinite(x) ? clamp(x, 0, 1) : fallback; }
  function findPreset(id) {
    for (var i = 0; i < PRESETS.length; i++) if (PRESETS[i].id === id) return PRESETS[i];
    return null;
  }

  /* ================================================================== noise synthesis
     Each channel is generated independently (decorrelated stereo), the mean is removed, the
     level is set to NOISE_RMS, and the last 0.5 s are cross-faded (equal power) into the start,
     so the loop has no seam: the sample after the last one is the continuation of the noise. */
  function brownSamples(count, rate) {
    var leak = 1 - 2 * Math.PI * 8 / rate;   // integrator pole: 1/f^2 above about 8 Hz, flat below
    var out = new Float32Array(count), y = 0;
    for (var i = 0; i < count; i++) {
      y = leak * y + (Math.random() * 2 - 1);
      out[i] = y;
    }
    return out;
  }

  function pinkSamples(count) {
    // Paul Kellet's refined pink filter (within 0.05 dB of 1/f above 9 Hz at 44.1 kHz).
    var out = new Float32Array(count), b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0;
    for (var i = 0; i < count; i++) {
      var w = Math.random() * 2 - 1;
      b0 = 0.99886 * b0 + w * 0.0555179;
      b1 = 0.99332 * b1 + w * 0.0750759;
      b2 = 0.96900 * b2 + w * 0.1538520;
      b3 = 0.86650 * b3 + w * 0.3104856;
      b4 = 0.55000 * b4 + w * 0.5329522;
      b5 = -0.7616 * b5 - w * 0.0168980;
      out[i] = b0 + b1 + b2 + b3 + b4 + b5 + b6 + w * 0.5362;
      b6 = w * 0.115926;
    }
    return out;
  }

  function noiseBuffer(ctx, type, seconds) {
    var rate = ctx.sampleRate;
    var n = Math.round(rate * (seconds || NOISE_SECONDS));
    var m = Math.round(rate * 0.5);
    var buffer = ctx.createBuffer(2, n, rate);
    for (var ch = 0; ch < 2; ch++) {
      var raw = type === 'pink' ? pinkSamples(n + m) : brownSamples(n + m, rate);
      var data = buffer.getChannelData(ch);
      var i, mean = 0, power = 0;
      for (i = 0; i < n; i++) {
        if (i < m) {
          var a = (i / m) * Math.PI / 2;
          data[i] = raw[i] * Math.sin(a) + raw[n + i] * Math.cos(a);
        } else {
          data[i] = raw[i];
        }
        mean += data[i];
      }
      mean /= n;
      for (i = 0; i < n; i++) { data[i] -= mean; power += data[i] * data[i]; }
      var scale = NOISE_RMS / Math.sqrt(power / n || 1);
      for (i = 0; i < n; i++) data[i] *= scale;
    }
    return buffer;
  }

  /* ================================================================== engine (no DOM)
     Works on any BaseAudioContext, so the test harness can render it offline. */
  function createEngine(ctx, output) {
    var dest = output || ctx.destination;
    var buffers = {};

    function glide(param, value, seconds, exponential) {
      var now = ctx.currentTime;
      if (param.cancelAndHoldAtTime) {
        param.cancelAndHoldAtTime(now);
      } else {
        var held = param.value;
        param.cancelScheduledValues(now);
        param.setValueAtTime(held, now);
      }
      if (exponential && value > 0 && param.value > 0) param.exponentialRampToValueAtTime(value, now + seconds);
      else param.linearRampToValueAtTime(value, now + seconds);
    }

    function softSquare() {
      var curve = new Float32Array(1025), k = 4;
      for (var i = 0; i < curve.length; i++) {
        var x = i / 512 - 1;
        curve[i] = Math.tanh(k * x) / Math.tanh(k);
      }
      return curve;
    }

    var master = ctx.createGain();
    master.gain.setValueAtTime(0, 0);
    var analyser = ctx.createAnalyser();
    analyser.fftSize = 16384;
    analyser.smoothingTimeConstant = 0.55;
    master.connect(dest);
    master.connect(analyser);

    var toneBus = ctx.createGain();
    toneBus.gain.setValueAtTime(0, 0);
    var pulse = ctx.createGain();
    pulse.gain.setValueAtTime(1, 0);
    toneBus.connect(pulse);
    pulse.connect(master);

    var oscL = ctx.createOscillator();
    var oscR = ctx.createOscillator();
    oscL.type = oscR.type = 'sine';
    var panL = ctx.createStereoPanner();
    var panR = ctx.createStereoPanner();
    panL.pan.setValueAtTime(-1, 0);
    panR.pan.setValueAtTime(1, 0);
    var gateR = ctx.createGain();
    oscL.connect(panL);
    panL.connect(toneBus);
    oscR.connect(gateR);
    gateR.connect(panR);
    panR.connect(toneBus);

    var lfo = ctx.createOscillator();
    lfo.type = 'sine';
    var shaper = ctx.createWaveShaper();
    shaper.curve = softSquare();
    var depth = ctx.createGain();
    depth.gain.setValueAtTime(0, 0);
    lfo.connect(shaper);
    shaper.connect(depth);
    depth.connect(pulse.gain);

    var noiseBus = ctx.createGain();
    noiseBus.gain.setValueAtTime(0, 0);
    noiseBus.connect(master);
    var noise = null;   // { type, source, fade }

    var current = { carrier: 200, beat: 40, iso: false, master: 1 };
    oscL.frequency.setValueAtTime(current.carrier, 0);
    oscR.frequency.setValueAtTime(current.carrier + current.beat, 0);
    lfo.frequency.setValueAtTime(current.beat, 0);
    oscL.start(0);
    oscR.start(0);
    lfo.start(0);

    function setFrequencies(carrier, beat, seconds) {
      var t = seconds === undefined ? TIME.glide : seconds;
      current.carrier = carrier;
      current.beat = beat;
      glide(oscL.frequency, carrier, t, true);
      glide(oscR.frequency, carrier + beat, t, true);
      glide(lfo.frequency, beat, t, true);
    }

    function setIsochronic(on, seconds) {
      var t = seconds === undefined ? TIME.glide : seconds;
      var h = Math.SQRT2 / 2;   // pulse peaks at 2h = sqrt2: makes up the -3 dB of pan 0
      current.iso = !!on;
      glide(panL.pan, on ? 0 : -1, t);
      glide(gateR.gain, on ? 0 : 1, t);
      glide(pulse.gain, on ? h : 1, t);
      glide(depth.gain, on ? h : 0, t);
    }

    function setToneLevel(level, seconds) {
      glide(toneBus.gain, TONE_MAX * level * level, seconds === undefined ? TIME.level : seconds);
    }

    function setNoiseLevel(level, seconds) {
      glide(noiseBus.gain, NOISE_MAX * level * level, seconds === undefined ? TIME.level : seconds);
    }

    function setNoiseType(type, seconds) {
      var t = seconds === undefined ? TIME.swap : seconds;
      if (noise && noise.type === type) return;
      if (noise) {
        var old = noise;
        glide(old.fade.gain, 0, t);
        old.source.stop(ctx.currentTime + t + 0.05);
        old.source.onended = function () { old.fade.disconnect(); };
        noise = null;
      }
      if (type !== 'brown' && type !== 'pink') return;
      if (!buffers[type]) buffers[type] = noiseBuffer(ctx, type);
      var source = ctx.createBufferSource();
      source.buffer = buffers[type];
      source.loop = true;
      var fade = ctx.createGain();
      fade.gain.setValueAtTime(0, ctx.currentTime);
      source.connect(fade);
      fade.connect(noiseBus);
      source.start(ctx.currentTime, Math.random() * buffers[type].duration);
      glide(fade.gain, 1, t);
      noise = { type: type, source: source, fade: fade };
    }

    function setMaster(level, seconds) {
      current.master = clamp(level, 0, 1);
      glide(master.gain, current.master, seconds === undefined ? TIME.level : seconds);
    }

    function fadeIn(seconds, level) {
      if (typeof level === 'number' && isFinite(level)) current.master = clamp(level, 0, 1);
      glide(master.gain, current.master, seconds === undefined ? TIME.fadeIn : seconds);
    }
    function fadeOut(seconds) { glide(master.gain, 0, seconds === undefined ? TIME.fadeOut : seconds); }

    return {
      context: ctx,
      analyser: analyser,
      current: current,
      setFrequencies: setFrequencies,
      setIsochronic: setIsochronic,
      setToneLevel: setToneLevel,
      setNoiseLevel: setNoiseLevel,
      setNoiseType: setNoiseType,
      setMaster: setMaster,
      fadeIn: fadeIn,
      fadeOut: fadeOut
    };
  }

  /* ================================================================== state */
  var DEFAULTS = { preset: 'gamma', carrier: 200, beat: 40, tone: 0.5, lastTone: 0.5, noise: 0.25,
    volume: 0.75, noiseType: 'brown', iso: false, view: 'wave', playing: false };

  function load() {
    var s = {}, raw = null, k;
    for (k in DEFAULTS) s[k] = DEFAULTS[k];
    try { raw = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { raw = null; }
    if (!raw || typeof raw !== 'object') return s;
    if (raw.preset === 'custom' || findPreset(raw.preset)) s.preset = raw.preset;
    if (isFinite(raw.carrier)) s.carrier = clamp(Math.round(+raw.carrier), LIMITS.carrier[0], LIMITS.carrier[1]);
    if (isFinite(raw.beat)) s.beat = clamp(Math.round(+raw.beat), LIMITS.beat[0], LIMITS.beat[1]);
    if (isFinite(raw.tone)) s.tone = clamp(+raw.tone, 0, 1);
    if (isFinite(raw.lastTone)) s.lastTone = clamp(+raw.lastTone, 0.05, 1);
    if (isFinite(raw.noise)) s.noise = clamp(+raw.noise, 0, 1);
    if (isFinite(raw.volume)) s.volume = clamp(+raw.volume, 0, 1);
    if (raw.noiseType === 'brown' || raw.noiseType === 'pink' || raw.noiseType === 'off') s.noiseType = raw.noiseType;
    s.iso = raw.iso === true;
    if (raw.view === 'wave' || raw.view === 'spectrum') s.view = raw.view;
    s.playing = raw.playing === true;
    return s;
  }

  var state = load();

  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* storage blocked: keep it in memory */ }
  }

  /* ================================================================== transport & API */
  var engine = null;
  var playing = false;
  var suspendTimer = 0;
  var following = '';
  var pendingFade = null;
  var AudioCtx = window.AudioContext || window.webkitAudioContext;

  function emitChange() {
    try { window.dispatchEvent(new CustomEvent('aefocuslab:change')); } catch (e) { /* ignore */ }
  }

  function ensureEngine() {
    if (engine || !AudioCtx) return engine;
    var ctx = new AudioCtx({ latencyHint: 'playback' });
    engine = createEngine(ctx);
    engine.setFrequencies(state.carrier, state.beat, 0.01);
    engine.setIsochronic(state.iso, 0.01);
    return engine;
  }

  function start(seconds) {
    if (!ensureEngine()) return;
    clearTimeout(suspendTimer);
    pendingFade = null;
    var ctx = engine.context;
    var go = function () {
      engine.setFrequencies(state.carrier, state.beat, 0.05);
      engine.setIsochronic(state.iso, 0.05);
      engine.setToneLevel(state.tone, 0.05);
      engine.setNoiseType(state.noiseType, 0.05);
      engine.setNoiseLevel(state.noise, 0.05);
      engine.fadeIn(seconds, state.volume);
    };
    playing = true;
    state.playing = true;
    save();
    emitChange();
    if (ctx.state === 'suspended') ctx.resume().then(go, go); else go();
  }

  function stop(seconds) {
    playing = false;
    state.playing = false;
    save();
    emitChange();
    if (!engine) return;
    engine.fadeOut(seconds);
    var ctx = engine.context;
    clearTimeout(suspendTimer);
    suspendTimer = setTimeout(function () {
      if (!playing && ctx.state === 'running') ctx.suspend();
    }, ((seconds === undefined ? TIME.fadeOut : seconds) + 0.15) * 1000);
  }

  function canPlay() {
    if (document.hidden) return false;
    if (engine && engine.context.state === 'running') return true;
    return !navigator.userActivation || navigator.userActivation.hasBeenActive;
  }

  function resumePending() {
    if (pendingFade === null || document.hidden) return;
    var fade = pendingFade;
    pendingFade = null;
    start(fade);
  }

  document.addEventListener('pointerdown', resumePending, true);
  document.addEventListener('keydown', resumePending, true);
  document.addEventListener('visibilitychange', function () { if (canPlay()) resumePending(); });
  window.addEventListener('storage', function (event) {
    if (event.key !== KEY || playing) return;
    state = load();
    emitChange();
  });

  function applyPreset(id) {
    var p = findPreset(id);
    if (!p) return;
    state.preset = p.id;
    state.carrier = p.carrier;
    state.beat = p.beat;
    state.noiseType = p.noise;
    state.noise = p.level;
    state.tone = p.tones ? (state.tone > 0 ? state.tone : state.lastTone) : 0;
    if (engine) {
      engine.setFrequencies(state.carrier, state.beat);
      engine.setToneLevel(state.tone, TIME.glide);
      engine.setNoiseType(state.noiseType);
      engine.setNoiseLevel(state.noise, TIME.glide);
    }
    save();
    emitChange();
  }

  function setVolume(v) {
    state.volume = clamp(+v || 0, 0, 1);
    if (engine && playing) engine.setMaster(state.volume, TIME.level);
    save();
    emitChange();
  }

  function setIsochronic(on) {
    state.iso = !!on;
    if (engine) engine.setIsochronic(state.iso);
    save();
    emitChange();
  }

  function setCustomHz(carrier, beat) {
    state.carrier = clamp(Math.round(carrier), LIMITS.carrier[0], LIMITS.carrier[1]);
    state.beat = clamp(Math.round(beat), LIMITS.beat[0], LIMITS.beat[1]);
    state.preset = 'custom';
    if (state.tone === 0) state.tone = state.lastTone;
    if (engine) {
      engine.setFrequencies(state.carrier, state.beat);
      engine.setToneLevel(state.tone, TIME.glide);
    }
    save();
    emitChange();
  }

  function cue(spec) {
    spec = spec || { preset: null };
    following = spec.label ? String(spec.label) : '';
    if (!spec.preset) {
      pendingFade = null;
      if (playing) stop(typeof spec.fade === 'number' ? spec.fade : undefined); else emitChange();
      return;
    }
    var p = findPreset(spec.preset);
    if (p) {
      state.preset = p.id;
      state.carrier = p.carrier;
      state.beat = p.beat;
      state.noiseType = p.noise;
      state.noise = num(spec.noise, p.level);
      state.tone = p.tones ? num(spec.tone, state.tone > 0 ? state.tone : state.lastTone) : 0;
      if (engine) {
        engine.setFrequencies(state.carrier, state.beat);
        engine.setToneLevel(state.tone, TIME.glide);
        engine.setNoiseType(state.noiseType);
        engine.setNoiseLevel(state.noise, TIME.glide);
      }
      save();
    }
    var fade = typeof spec.fade === 'number' ? spec.fade : undefined;
    if (!AudioCtx || playing) { emitChange(); return; }
    if (!canPlay()) {
      pendingFade = fade === undefined ? TIME.fadeIn : fade;
      emitChange();
      return;
    }
    start(fade);
  }

  window.AEFocusLab = {
    PRESETS: PRESETS,
    KEY: KEY,
    LIMITS: LIMITS,
    noiseBuffer: noiseBuffer,
    createEngine: createEngine,
    open: function () { if (window.AEPomodoro && typeof window.AEPomodoro.openSound === 'function') window.AEPomodoro.openSound(); },
    close: function () { if (window.AEPomodoro && typeof window.AEPomodoro.close === 'function') window.AEPomodoro.close(); },
    start: start,
    stop: stop,
    toggle: function () { if (playing) stop(); else start(); },
    applyPreset: applyPreset,
    setVolume: setVolume,
    setIsochronic: setIsochronic,
    setCustomHz: setCustomHz,
    cue: cue,
    state: function () { var copy = {}; for (var k in state) copy[k] = state[k]; copy.active = playing; copy.following = following; return copy; }
  };
})();
