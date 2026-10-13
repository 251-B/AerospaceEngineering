/*!
 * Aerospace Engineering Study Portal: "Focus Lab" (study sound, synthesised in the browser).
 *
 * Loaded on every page by assets/js/theme.js (no page carries its own <script> tag for it); the
 * script adds its own stylesheet (assets/css/focus-lab.css, found next to this file). Skipped in
 * the PDF print mode (?print=...), and hidden by @media print.
 *
 * A floating "Focus" button opens a non-modal panel:
 *   - presets (gamma 40 Hz, beta 20 Hz, SMR 14 Hz, alpha 10 Hz, brown noise only);
 *   - live mixer: binaural level, background noise (brown / pink / off) and its level, isochronic
 *     toggle for speakers, fine tuning of the carrier (100-432 Hz) and beat (1-45 Hz);
 *   - a small real-time visualiser (waveform envelope or spectrum, AnalyserNode + <canvas>).
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
 * Storage: 'ae_focus_lab' (JSON: preset, frequencies, levels, noise colour, mode, view).
 * API: window.AEFocusLab = { PRESETS, KEY, LIMITS, noiseBuffer, createEngine, open, close, toggle,
 *      applyPreset, state }
 */
(function () {
  'use strict';

  if (window.AEFocusLab) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var SCRIPT = document.currentScript;
  var KEY = 'ae_focus_lab';
  var LIMITS = { carrier: [100, 432], beat: [1, 45] };
  var TONE_MAX = 0.3;     // gain of the tone bus at 100 %
  var NOISE_MAX = 0.75;   // gain of the noise bus at 100 %
  var NOISE_RMS = 0.2;    // RMS of the generated noise loops
  var NOISE_SECONDS = 12; // length of each noise loop
  var TIME = { fadeIn: 0.6, fadeOut: 0.35, glide: 0.25, level: 0.08, swap: 0.5 };

  var BANDS = {
    gamma: { symbol: 'γ', name: 'Gamma' },
    beta: { symbol: 'β', name: 'Beta' },
    smr: { symbol: 'β', name: 'SMR' },
    alpha: { symbol: 'α', name: 'Alpha' },
    none: { symbol: '1/f²', name: 'Noise only' }
  };

  var PRESETS = [
    { id: 'gamma', name: 'Calculation & Debugging', band: 'gamma', carrier: 200, beat: 40, tones: true,
      noise: 'brown', level: 0.25, use: 'Problem solving · advanced maths · system architecture',
      text: 'High-speed neural synchronisation for complex problem solving, advanced mathematics and systems architecture.' },
    { id: 'beta', name: 'Active Programming', band: 'beta', carrier: 250, beat: 20, tones: true,
      noise: 'pink', level: 0.20, use: 'Writing code · implementing logic · practice problems',
      text: 'Sustained analytical focus for writing code, implementing logic and solving practical exercises.' },
    { id: 'smr', name: 'Technical Reading & Papers', band: 'smr', carrier: 200, beat: 14, tones: true,
      noise: 'brown', level: 0.30, use: 'Documentation · technical standards · papers',
      text: 'Sensorimotor rhythm (14 Hz) for deep reading of documentation and technical standards, and study without mental fatigue.' },
    { id: 'alpha', name: 'Assimilation & Flow', band: 'alpha', carrier: 220, beat: 10, tones: true,
      noise: 'pink', level: 0.15, use: 'New theory · conceptual physics · mind maps',
      text: 'Relaxed alertness, suited to understanding new theoretical concepts, conceptual physics and mind maps.' },
    { id: 'isolation', name: 'Pure Isolation', band: 'none', carrier: 200, beat: 40, tones: false,
      noise: 'brown', level: 0.50, use: 'Ambient-noise masking · sensory overload',
      text: 'Low-frequency acoustic masking (1/f²) to block ambient noise and reduce sensory overload.' }
  ];

  var NOISES = [
    { id: 'brown', label: 'Brown', note: 'Brown noise: −6 dB per octave (1/f²)' },
    { id: 'pink', label: 'Pink', note: 'Pink noise: −3 dB per octave (1/f)' },
    { id: 'off', label: 'Off', note: 'No background noise' }
  ];

  function clamp(x, lo, hi) { return Math.min(hi, Math.max(lo, x)); }
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

    var current = { carrier: 200, beat: 40, iso: false };
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

    function fadeIn(seconds) { glide(master.gain, 1, seconds === undefined ? TIME.fadeIn : seconds); }
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
      fadeIn: fadeIn,
      fadeOut: fadeOut
    };
  }

  /* ================================================================== state */
  var DEFAULTS = { preset: 'gamma', carrier: 200, beat: 40, tone: 0.5, lastTone: 0.5, noise: 0.25,
    noiseType: 'brown', iso: false, view: 'wave', playing: false };

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

  /* ================================================================== UI */
  var ui = {};
  var engine = null;
  var playing = false;
  var frame = 0;
  var suspendTimer = 0;
  var AudioCtx = window.AudioContext || window.webkitAudioContext;

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function svgIcon(paths, size) {
    var ns = 'http://www.w3.org/2000/svg';
    var svg = document.createElementNS(ns, 'svg');
    svg.setAttribute('viewBox', '0 0 24 24');
    svg.setAttribute('width', size || 18);
    svg.setAttribute('height', size || 18);
    svg.setAttribute('aria-hidden', 'true');
    svg.setAttribute('focusable', 'false');
    paths.forEach(function (d) {
      var p = document.createElementNS(ns, 'path');
      p.setAttribute('d', d);
      svg.appendChild(p);
    });
    return svg;
  }

  var ICONS = {
    phones: ['M4 14v-2a8 8 0 0 1 16 0v2', 'M4 14h3v6H5a1 1 0 0 1-1-1z', 'M20 14h-3v6h2a1 1 0 0 0 1-1z'],
    play: ['M8 5.5v13l11-6.5z'],
    pause: ['M7.5 5.5h3v13h-3z', 'M13.5 5.5h3v13h-3z'],
    close: ['M6 6l12 12', 'M18 6L6 18']
  };

  function hz(x) { return Math.round(x) + ' Hz'; }
  function pct(x) { return Math.round(x * 100) + '%'; }

  function bandLabel(preset) {
    var band = BANDS[preset.band];
    return preset.tones ? band.symbol + ' ' + band.name + ' · ' + hz(preset.beat) : band.symbol + ' · ' + band.name;
  }

  function slider(id, label, min, max, step, value) {
    var row = el('div', 'fl-slider');
    var head = el('div', 'fl-slider__head');
    var name = el('label', 'fl-slider__label', label);
    name.htmlFor = id;
    var out = el('output', 'fl-slider__value');
    out.htmlFor = id;
    head.appendChild(name);
    head.appendChild(out);
    var input = el('input', 'fl-range');
    input.type = 'range';
    input.id = id;
    input.min = min;
    input.max = max;
    input.step = step;
    input.value = value;
    row.appendChild(head);
    row.appendChild(input);
    return { row: row, input: input, out: out };
  }

  function build() {
    if (document.getElementById('focusLabButton') || !document.body) return;

    var launcher = el('button', 'fl-launcher');
    launcher.type = 'button';
    launcher.id = 'focusLabButton';
    launcher.setAttribute('aria-expanded', 'false');
    launcher.setAttribute('aria-controls', 'focusLabPanel');
    launcher.appendChild(svgIcon(ICONS.phones, 18));
    launcher.appendChild(el('span', 'fl-launcher__label', 'Focus'));
    var dot = el('span', 'fl-launcher__dot');
    dot.setAttribute('aria-hidden', 'true');
    launcher.appendChild(dot);

    var panel = el('section', 'fl-panel');
    panel.id = 'focusLabPanel';
    panel.hidden = true;
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-modal', 'false');
    panel.setAttribute('aria-labelledby', 'focusLabTitle');

    // header
    var head = el('header', 'fl-head');
    var titles = el('div', 'fl-head__titles');
    titles.appendChild(el('p', 'fl-kicker', 'Neuro-Audio Focus Lab'));
    var title = el('h2', 'fl-title', 'Study frequencies');
    title.id = 'focusLabTitle';
    titles.appendChild(title);
    var close = el('button', 'fl-icon-btn');
    close.type = 'button';
    close.setAttribute('aria-label', 'Close Focus Lab');
    close.appendChild(svgIcon(ICONS.close, 18));
    head.appendChild(titles);
    head.appendChild(close);

    // transport
    var transport = el('div', 'fl-transport');
    var play = el('button', 'fl-play');
    play.type = 'button';
    var playIcon = el('span', 'fl-play__icon');
    var playText = el('span', 'fl-play__text');
    play.appendChild(playIcon);
    play.appendChild(playText);
    var readout = el('p', 'fl-readout');
    readout.setAttribute('aria-live', 'polite');
    transport.appendChild(play);
    transport.appendChild(readout);

    // headphones notice
    var notice = el('p', 'fl-notice');
    notice.setAttribute('role', 'note');

    // presets
    var presetTitle = el('h3', 'fl-section', 'Presets');
    var presetList = el('div', 'fl-presets');
    presetList.setAttribute('role', 'group');
    presetList.setAttribute('aria-label', 'Study presets');
    var cards = PRESETS.map(function (p) {
      var card = el('button', 'fl-card');
      card.type = 'button';
      card.setAttribute('data-preset', p.id);
      if (!p.tones) card.className += ' is-wide';
      card.appendChild(el('span', 'fl-card__band', bandLabel(p)));
      card.appendChild(el('span', 'fl-card__name', p.name));
      var freqs = el('span', 'fl-card__hz');
      (p.tones ? ['Carrier ' + hz(p.carrier), 'L ' + hz(p.carrier) + ' · R ' + hz(p.carrier + p.beat)] : ['Oscillators off'])
        .forEach(function (part, i) {
          if (i) freqs.appendChild(document.createTextNode(' · '));
          freqs.appendChild(el('span', '', part));
        });
      card.appendChild(freqs);
      card.appendChild(el('span', 'fl-card__use', p.use));
      card.appendChild(el('span', 'fl-card__noise', (p.noise === 'brown' ? 'Brown' : 'Pink') + ' noise ' + pct(p.level)));
      card.addEventListener('click', function () { applyPreset(p.id); });
      presetList.appendChild(card);
      return card;
    });
    var explain = el('p', 'fl-explain');
    explain.setAttribute('aria-live', 'polite');

    // visualiser
    var vizHead = el('div', 'fl-viz__head');
    vizHead.appendChild(el('h3', 'fl-section', 'Signal'));
    var views = el('div', 'fl-seg');
    views.setAttribute('role', 'group');
    views.setAttribute('aria-label', 'Visualiser view');
    var viewButtons = [['wave', 'Wave'], ['spectrum', 'Spectrum']].map(function (v) {
      var b = el('button', 'fl-seg__btn', v[1]);
      b.type = 'button';
      b.setAttribute('data-view', v[0]);
      b.addEventListener('click', function () {
        state.view = v[0];
        save();
        sync();
        draw();
      });
      views.appendChild(b);
      return b;
    });
    vizHead.appendChild(views);
    var canvas = el('canvas', 'fl-canvas');
    canvas.setAttribute('role', 'img');

    // mixer
    var mixTitle = el('h3', 'fl-section', 'Live mixer');
    var tone = slider('flTone', 'Binaural tones', 0, 100, 1, Math.round(state.tone * 100));
    var noiseRow = el('div', 'fl-noise');
    var noiseHead = el('div', 'fl-slider__head');
    noiseHead.appendChild(el('span', 'fl-slider__label', 'Background noise'));
    var noiseSeg = el('div', 'fl-seg');
    noiseSeg.setAttribute('role', 'group');
    noiseSeg.setAttribute('aria-label', 'Background noise colour');
    var noiseButtons = NOISES.map(function (n) {
      var b = el('button', 'fl-seg__btn', n.label);
      b.type = 'button';
      b.title = n.note;
      b.setAttribute('data-noise', n.id);
      b.addEventListener('click', function () { setNoiseType(n.id); });
      noiseSeg.appendChild(b);
      return b;
    });
    noiseHead.appendChild(noiseSeg);
    noiseRow.appendChild(noiseHead);
    var noiseLevel = slider('flNoise', 'Noise level', 0, 100, 1, Math.round(state.noise * 100));
    noiseRow.appendChild(noiseLevel.row);

    var isoRow = el('label', 'fl-switch');
    var iso = el('input', 'fl-switch__input');
    iso.type = 'checkbox';
    iso.id = 'flIso';
    var isoText = el('span', 'fl-switch__text');
    isoText.appendChild(el('strong', '', 'Isochronic tones'));
    isoText.appendChild(el('span', '', 'Amplitude pulses at the beat frequency: works on speakers.'));
    isoRow.appendChild(iso);
    isoRow.appendChild(el('span', 'fl-switch__track'));
    isoRow.appendChild(isoText);

    var fine = el('details', 'fl-fine');
    fine.appendChild(el('summary', '', 'Fine tuning'));
    var carrier = slider('flCarrier', 'Carrier frequency', LIMITS.carrier[0], LIMITS.carrier[1], 1, state.carrier);
    var beat = slider('flBeat', 'Beat frequency', LIMITS.beat[0], LIMITS.beat[1], 1, state.beat);
    fine.appendChild(carrier.row);
    fine.appendChild(beat.row);

    var foot = el('p', 'fl-foot', 'Keep the volume low. Evidence on brainwave entrainment by binaural beats is mixed: ' +
      'treat the presets as a focus routine, not as a treatment. Sound stops when you leave the page; ' +
      'the Focus button resumes it on the next one.');

    [head, transport, notice, presetTitle, presetList, explain, vizHead, canvas, mixTitle, tone.row, noiseRow,
      isoRow, fine, foot].forEach(function (node) { panel.appendChild(node); });

    document.body.appendChild(launcher);
    document.body.appendChild(panel);

    ui = { launcher: launcher, panel: panel, close: close, play: play, playIcon: playIcon, playText: playText,
      readout: readout, notice: notice, cards: cards, explain: explain, viewButtons: viewButtons, canvas: canvas,
      tone: tone, noiseButtons: noiseButtons, noiseLevel: noiseLevel, iso: iso, carrier: carrier, beat: beat };

    launcher.addEventListener('click', function () {
      if (!panel.hidden) { closePanel(false); return; }
      openPanel();
      if (state.playing && !playing) start();   // resume what was playing on the previous page
    });
    close.addEventListener('click', function () { closePanel(true); });
    play.addEventListener('click', function () { if (playing) stop(); else start(); });

    tone.input.addEventListener('input', function () {
      state.tone = tone.input.value / 100;
      if (state.tone > 0) state.lastTone = state.tone;
      if (engine) engine.setToneLevel(state.tone);
      save();
      sync();
    });
    noiseLevel.input.addEventListener('input', function () {
      state.noise = noiseLevel.input.value / 100;
      if (engine) engine.setNoiseLevel(state.noise);
      save();
      sync();
    });
    iso.addEventListener('change', function () {
      state.iso = iso.checked;
      if (engine) engine.setIsochronic(state.iso);
      save();
      sync();
    });
    carrier.input.addEventListener('input', function () { tune(+carrier.input.value, state.beat); });
    beat.input.addEventListener('input', function () { tune(state.carrier, +beat.input.value); });

    panel.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        event.stopPropagation();
        closePanel(true);
      }
    });
    document.addEventListener('ae-theme-change', draw);
    document.addEventListener('ae-surface-change', draw);
    window.addEventListener('resize', draw);
    window.addEventListener('storage', function (event) {
      if (event.key !== KEY || playing) return;
      state = load();
      sync();
    });

    if (!AudioCtx) {
      play.disabled = true;
      ui.readout.textContent = 'This browser has no Web Audio API.';
    }
    sync();
  }

  function tune(carrier, beat) {
    state.carrier = clamp(Math.round(carrier), LIMITS.carrier[0], LIMITS.carrier[1]);
    state.beat = clamp(Math.round(beat), LIMITS.beat[0], LIMITS.beat[1]);
    state.preset = 'custom';
    if (state.tone === 0) state.tone = state.lastTone;
    if (engine) {
      engine.setFrequencies(state.carrier, state.beat);
      engine.setToneLevel(state.tone);
    }
    save();
    sync();
  }

  function setNoiseType(type) {
    state.noiseType = type;
    if (engine) engine.setNoiseType(type);
    save();
    sync();
  }

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
    sync();
  }

  function sync() {
    if (!ui.panel) return;
    var p = findPreset(state.preset);
    var tonesOn = state.tone > 0;

    ui.launcher.classList.toggle('is-playing', playing);
    ui.launcher.classList.toggle('is-resumable', !playing && state.playing);
    ui.launcher.title = playing ? 'Focus Lab: playing' : state.playing ? 'Focus Lab: click to resume' : 'Focus Lab: study frequencies';
    ui.launcher.setAttribute('aria-label', ui.launcher.title);

    ui.play.setAttribute('aria-pressed', playing ? 'true' : 'false');
    ui.playIcon.textContent = '';
    ui.playIcon.appendChild(svgIcon(playing ? ICONS.pause : ICONS.play, 20));
    ui.playText.textContent = playing ? 'Pause' : 'Start';

    var parts = [];
    if (tonesOn && state.iso) parts.push(hz(state.carrier) + ' pulsed at ' + hz(state.beat));
    else if (tonesOn) parts.push('L ' + hz(state.carrier) + ' · R ' + hz(state.carrier + state.beat) + ' · beat ' + hz(state.beat));
    else parts.push('Tones off');
    parts.push(state.noiseType === 'off' ? 'no noise' : state.noiseType + ' noise ' + pct(state.noise));
    if (AudioCtx) ui.readout.textContent = parts.join(' · ');

    ui.notice.className = 'fl-notice' + (state.iso ? ' is-iso' : '');
    ui.notice.textContent = state.iso
      ? 'Isochronic mode: one tone pulsed in both ears. Works on speakers or headphones.'
      : 'Binaural beats need stereo headphones: each ear must hear only its own tone. On speakers, switch on Isochronic tones below.';

    ui.cards.forEach(function (card) {
      card.setAttribute('aria-pressed', card.getAttribute('data-preset') === state.preset ? 'true' : 'false');
    });
    ui.explain.textContent = '';
    if (p) {
      ui.explain.appendChild(el('strong', '', p.name + '. '));
      ui.explain.appendChild(document.createTextNode(p.text));
    } else {
      ui.explain.appendChild(el('strong', '', 'Custom. '));
      ui.explain.appendChild(document.createTextNode('Carrier ' + hz(state.carrier) + ', beat ' + hz(state.beat) +
        ' (fine tuning). Pick a preset to return to a tested setting.'));
    }

    ui.viewButtons.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-view') === state.view ? 'true' : 'false'); });
    ui.noiseButtons.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-noise') === state.noiseType ? 'true' : 'false'); });
    ui.canvas.setAttribute('aria-label', state.view === 'wave'
      ? 'Waveform of the mixed signal; the envelope beats at the beat frequency'
      : 'Spectrum of the mixed signal from 30 Hz to 2 kHz');

    ui.tone.input.value = Math.round(state.tone * 100);
    ui.tone.out.textContent = pct(state.tone);
    ui.noiseLevel.input.value = Math.round(state.noise * 100);
    ui.noiseLevel.out.textContent = pct(state.noise);
    ui.noiseLevel.input.disabled = state.noiseType === 'off';
    ui.iso.checked = state.iso;
    ui.carrier.input.value = state.carrier;
    ui.carrier.out.textContent = hz(state.carrier);
    ui.beat.input.value = state.beat;
    ui.beat.out.textContent = hz(state.beat);
  }

  /* ---------------------------------------------------------------- transport */
  function ensureEngine() {
    if (engine || !AudioCtx) return engine;
    var ctx = new AudioCtx({ latencyHint: 'playback' });
    engine = createEngine(ctx);
    engine.setFrequencies(state.carrier, state.beat, 0.01);
    engine.setIsochronic(state.iso, 0.01);
    return engine;
  }

  function start() {
    if (!ensureEngine()) return;
    clearTimeout(suspendTimer);
    var ctx = engine.context;
    var go = function () {
      engine.setFrequencies(state.carrier, state.beat, 0.05);
      engine.setIsochronic(state.iso, 0.05);
      engine.setToneLevel(state.tone, 0.05);
      engine.setNoiseType(state.noiseType, 0.05);
      engine.setNoiseLevel(state.noise, 0.05);
      engine.fadeIn();
    };
    playing = true;
    state.playing = true;
    save();
    sync();
    loop();
    if (ctx.state === 'suspended') ctx.resume().then(go, go); else go();
  }

  function stop() {
    playing = false;
    state.playing = false;
    save();
    sync();
    if (!engine) return;
    engine.fadeOut();
    var ctx = engine.context;
    clearTimeout(suspendTimer);
    suspendTimer = setTimeout(function () {
      if (!playing && ctx.state === 'running') ctx.suspend();
    }, (TIME.fadeOut + 0.15) * 1000);
  }

  function openPanel() {
    ui.panel.hidden = false;
    ui.launcher.setAttribute('aria-expanded', 'true');
    ui.panel.scrollTop = 0;
    requestAnimationFrame(function () { ui.panel.classList.add('is-open'); });
    ui.play.focus({ preventScroll: true });
    draw();
    loop();
  }

  function closePanel(returnFocus) {
    ui.panel.classList.remove('is-open');
    ui.panel.hidden = true;
    ui.launcher.setAttribute('aria-expanded', 'false');
    cancelAnimationFrame(frame);
    frame = 0;
    if (returnFocus) ui.launcher.focus();
  }

  /* ---------------------------------------------------------------- visualiser */
  var timeData = null;
  var freqData = null;
  var waveScale = 1;
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var lastDraw = 0;

  function loop() {
    if (frame || !ui.panel || ui.panel.hidden) return;
    frame = requestAnimationFrame(function tick(t) {
      frame = 0;
      if (ui.panel.hidden) return;
      if (!reduceMotion || t - lastDraw > 200) {
        lastDraw = t;
        draw();
      }
      if (playing || (engine && engine.context.state === 'running')) frame = requestAnimationFrame(tick);
    });
  }

  function draw() {
    var canvas = ui.canvas;
    if (!canvas || !ui.panel || ui.panel.hidden) return;
    var dpr = window.devicePixelRatio || 1;
    var w = canvas.clientWidth, h = canvas.clientHeight;
    if (!w || !h) return;
    if (canvas.width !== Math.round(w * dpr) || canvas.height !== Math.round(h * dpr)) {
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
    }
    var g = canvas.getContext('2d');
    g.setTransform(dpr, 0, 0, dpr, 0, 0);
    g.clearRect(0, 0, w, h);
    var css = getComputedStyle(ui.panel);
    var accent = css.getPropertyValue('--fl-wave').trim() || '#f59e0b';
    var grid = css.getPropertyValue('--fl-grid').trim() || 'rgba(127,127,127,.25)';
    var muted = css.getPropertyValue('--fl-muted').trim() || '#888';

    g.strokeStyle = grid;
    g.lineWidth = 1;
    g.beginPath();
    g.moveTo(0, Math.round(h / 2) + 0.5);
    g.lineTo(w, Math.round(h / 2) + 0.5);
    g.stroke();

    var live = engine && playing;
    if (state.view === 'spectrum') drawSpectrum(g, w, h, accent, grid, muted, live);
    else drawWave(g, w, h, accent, live);
  }

  function drawWave(g, w, h, accent, live) {
    if (!live) return;
    var an = engine.analyser;
    if (!timeData || timeData.length !== an.fftSize) timeData = new Float32Array(an.fftSize);
    an.getFloatTimeDomainData(timeData);
    var span = Math.min(timeData.length, Math.round(engine.context.sampleRate * 0.25));
    var startAt = timeData.length - span;
    var peak = 0, i;
    for (i = startAt; i < timeData.length; i++) peak = Math.max(peak, Math.abs(timeData[i]));
    var target = peak > 1e-4 ? 0.85 / peak : waveScale;
    waveScale += (target - waveScale) * 0.15;
    var mid = h / 2, per = span / w;
    g.fillStyle = accent;
    g.globalAlpha = 0.28;
    g.beginPath();
    var tops = [];
    for (var x = 0; x < w; x++) {
      var a = startAt + Math.floor(x * per), b = Math.min(timeData.length, startAt + Math.floor((x + 1) * per));
      var lo = 0, hi = 0;
      for (i = a; i < b; i++) { if (timeData[i] < lo) lo = timeData[i]; if (timeData[i] > hi) hi = timeData[i]; }
      tops.push([mid - hi * waveScale * mid, mid - lo * waveScale * mid]);
      if (x === 0) g.moveTo(x, tops[x][0]); else g.lineTo(x, tops[x][0]);
    }
    for (x = w - 1; x >= 0; x--) g.lineTo(x, tops[x][1]);
    g.closePath();
    g.fill();
    g.globalAlpha = 1;
    g.strokeStyle = accent;
    g.lineWidth = 1.25;
    g.beginPath();
    for (x = 0; x < w; x++) { if (x === 0) g.moveTo(x, tops[x][0]); else g.lineTo(x, tops[x][0]); }
    g.stroke();
    g.beginPath();
    for (x = 0; x < w; x++) { if (x === 0) g.moveTo(x, tops[x][1]); else g.lineTo(x, tops[x][1]); }
    g.stroke();
  }

  function drawSpectrum(g, w, h, accent, grid, muted, live) {
    var fMin = 30, fMax = 2000, dbMin = -120, dbMax = -8;
    var lx = function (f) { return Math.log(f / fMin) / Math.log(fMax / fMin) * w; };
    g.font = '10px ' + (getComputedStyle(ui.panel).getPropertyValue('--fl-mono').trim() || 'monospace');
    g.fillStyle = muted;
    g.strokeStyle = grid;
    [50, 100, 200, 500, 1000].forEach(function (f) {
      var x = Math.round(lx(f)) + 0.5;
      g.beginPath();
      g.moveTo(x, 0);
      g.lineTo(x, h);
      g.stroke();
      g.fillText(f >= 1000 ? f / 1000 + 'k' : String(f), x + 3, h - 4);
    });
    if (!live) return;
    var an = engine.analyser;
    if (!freqData || freqData.length !== an.frequencyBinCount) freqData = new Float32Array(an.frequencyBinCount);
    an.getFloatFrequencyData(freqData);
    var binHz = engine.context.sampleRate / an.fftSize;
    g.beginPath();
    g.moveTo(0, h);
    for (var x = 0; x < w; x++) {
      var f0 = fMin * Math.pow(fMax / fMin, x / w), f1 = fMin * Math.pow(fMax / fMin, (x + 1) / w);
      var a = Math.floor(f0 / binHz), b = Math.max(a + 1, Math.ceil(f1 / binHz)), db = -Infinity;
      for (var i = a; i < b && i < freqData.length; i++) db = Math.max(db, freqData[i]);
      var y = h - clamp((db - dbMin) / (dbMax - dbMin), 0, 1) * h;
      g.lineTo(x, y);
    }
    g.lineTo(w, h);
    g.closePath();
    g.fillStyle = accent;
    g.globalAlpha = 0.22;
    g.fill();
    g.globalAlpha = 1;
    g.strokeStyle = accent;
    g.lineWidth = 1.25;
    g.stroke();
  }

  /* ---------------------------------------------------------------- boot */
  function addStylesheet() {
    if (!SCRIPT || !SCRIPT.src || document.querySelector('link[href*="focus-lab.css"]')) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = SCRIPT.src.replace(/js\/focus-lab\.js(\?.*)?$/, 'css/focus-lab.css');
    document.head.appendChild(link);
  }

  addStylesheet();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();

  window.AEFocusLab = {
    PRESETS: PRESETS,
    KEY: KEY,
    LIMITS: LIMITS,
    noiseBuffer: noiseBuffer,
    createEngine: createEngine,
    open: function () { if (ui.panel) openPanel(); },
    close: function () { if (ui.panel) closePanel(false); },
    toggle: function () { if (playing) stop(); else start(); },
    applyPreset: applyPreset,
    state: function () { var copy = {}; for (var k in state) copy[k] = state[k]; copy.active = playing; return copy; }
  };
})();
