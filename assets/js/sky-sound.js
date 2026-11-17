/*!
 * Home page, stellar view: celestial sound (root index.html only).
 *
 * Synthesised with the Web Audio API, no audio files: a slow pad of open chords through a soft low-pass
 * filter and a generated reverb, random glass-like chimes on a pentatonic scale, a rising "whoosh" for
 * the ignition and small chimes when the pointer rests on a constellation.
 *
 * Browsers only allow sound after a gesture, so the sound starts from the intro's "ignite" button (or from
 * the first click or key press when the visitor had it on). Storage: key ae_sky_sound ('on' | 'off'),
 * never a key with "theme" in it, always in try/catch. The speaker button (#soundToggle) mutes and
 * unmutes; the sound stops while the tab is hidden and while the classic view is shown.
 *
 * API: window.AESkySound = { start(), whoosh(), chime(i), setOn(bool), isOn(), supported }
 */
(function () {
  'use strict';

  var KEY = 'ae_sky_sound';
  var AC = window.AudioContext || window.webkitAudioContext;
  var supported = !!AC;

  function read(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function write(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* storage blocked: keep it in memory */ } }

  var ctx = null, master = null, reverbIn = null, padBus = null, running = false;
  var chimeTimer = 0, chordTimer = 0, chordIndex = 0, padVoices = [];
  var wanted = read(KEY) !== 'off';          // the visitor's choice; default on after the first ignite
  var VOLUME = 0.5;
  var PENTATONIC = [587.33, 659.25, 739.99, 880.0, 987.77, 1174.66, 1318.51];   // D major pentatonic, D5 to E6
  var CHORDS = [
    [146.83, 220.0, 329.63, 369.99, 493.88],   // D add9
    [123.47, 185.0, 293.66, 329.63, 440.0],    // B minor 9
    [98.0, 146.83, 246.94, 293.66, 440.0],     // G add9
    [110.0, 164.81, 277.18, 329.63, 493.88]    // A sus
  ];

  function impulse(seconds, decay) {
    var rate = ctx.sampleRate, length = Math.floor(rate * seconds), buffer = ctx.createBuffer(2, length, rate);
    for (var c = 0; c < 2; c++) {
      var data = buffer.getChannelData(c);
      for (var i = 0; i < length; i++) data[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / length, decay);
    }
    return buffer;
  }

  function build() {
    if (ctx || !supported) return;
    ctx = new AC();
    master = ctx.createGain(); master.gain.value = 0;
    var comp = ctx.createDynamicsCompressor();
    master.connect(comp); comp.connect(ctx.destination);
    var reverb = ctx.createConvolver(); reverb.buffer = impulse(5.5, 2.6);
    reverbIn = ctx.createGain(); reverbIn.gain.value = 0.9;
    reverbIn.connect(reverb); reverb.connect(master);
    padBus = ctx.createGain(); padBus.gain.value = 0;
    var filter = ctx.createBiquadFilter(); filter.type = 'lowpass'; filter.frequency.value = 1100; filter.Q.value = 0.6;
    padBus.connect(filter); filter.connect(master); filter.connect(reverbIn);
    // the filter breathes
    var lfo = ctx.createOscillator(), lfoGain = ctx.createGain();
    lfo.frequency.value = 0.07; lfoGain.gain.value = 420; lfo.connect(lfoGain); lfoGain.connect(filter.frequency); lfo.start();
    // the pad: five notes, each two slightly detuned oscillators
    CHORDS[0].forEach(function (f, i) {
      var pair = [];
      ['sine', 'triangle'].forEach(function (type, j) {
        var osc = ctx.createOscillator(), g = ctx.createGain();
        osc.type = type; osc.frequency.value = f; osc.detune.value = (j ? 7 : -6) + i;
        g.gain.value = type === 'sine' ? 0.05 : 0.022;
        osc.connect(g); g.connect(padBus); osc.start(); pair.push(osc);
      });
      padVoices.push(pair);
    });
  }

  function glideChord() {
    chordIndex = (chordIndex + 1) % CHORDS.length;
    var chord = CHORDS[chordIndex], t = ctx.currentTime;
    padVoices.forEach(function (pair, i) {
      pair.forEach(function (osc) {
        osc.frequency.cancelScheduledValues(t);
        osc.frequency.setValueAtTime(osc.frequency.value, t);
        osc.frequency.exponentialRampToValueAtTime(chord[i], t + 7);
      });
    });
  }

  function chime(index, quiet) {
    if (!ctx || !running) return;
    var f = PENTATONIC[(index === undefined ? Math.floor(Math.random() * PENTATONIC.length) : index) % PENTATONIC.length];
    var t = ctx.currentTime, pan = ctx.createStereoPanner ? ctx.createStereoPanner() : null;
    var vol = quiet ? 0.045 : 0.085;
    [[1, 1], [2.01, 0.28], [3.98, 0.1]].forEach(function (part) {
      var osc = ctx.createOscillator(), g = ctx.createGain();
      osc.type = 'sine'; osc.frequency.value = f * part[0];
      g.gain.setValueAtTime(0.0001, t);
      g.gain.exponentialRampToValueAtTime(vol * part[1], t + 0.012);
      g.gain.exponentialRampToValueAtTime(0.0001, t + (quiet ? 2.4 : 4.2) / part[0] + 0.6);
      osc.connect(g);
      if (pan) { pan.pan.value = Math.random() * 1.6 - 0.8; g.connect(pan); pan.connect(master); pan.connect(reverbIn); }
      else { g.connect(master); g.connect(reverbIn); }
      osc.start(t); osc.stop(t + 5);
    });
  }

  function scheduleChime() {
    clearTimeout(chimeTimer);
    chimeTimer = setTimeout(function () { chime(); scheduleChime(); }, 2200 + Math.random() * 4200);
  }

  function whoosh() {
    if (!ctx || !running) return;
    var t = ctx.currentTime, len = Math.floor(ctx.sampleRate * 3), buf = ctx.createBuffer(1, len, ctx.sampleRate), d = buf.getChannelData(0);
    for (var i = 0; i < len; i++) d[i] = Math.random() * 2 - 1;
    var src = ctx.createBufferSource(); src.buffer = buf;
    var band = ctx.createBiquadFilter(); band.type = 'bandpass'; band.Q.value = 1.2;
    band.frequency.setValueAtTime(180, t); band.frequency.exponentialRampToValueAtTime(5200, t + 1.9);
    var g = ctx.createGain();
    g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.32, t + 1.4); g.gain.exponentialRampToValueAtTime(0.0001, t + 2.8);
    src.connect(band); band.connect(g); g.connect(master); g.connect(reverbIn); src.start(t); src.stop(t + 3);
    var sub = ctx.createOscillator(), sg = ctx.createGain();
    sub.type = 'sine'; sub.frequency.setValueAtTime(70, t + 1.1); sub.frequency.exponentialRampToValueAtTime(28, t + 2.6);
    sg.gain.setValueAtTime(0.0001, t + 1.1); sg.gain.exponentialRampToValueAtTime(0.5, t + 1.25); sg.gain.exponentialRampToValueAtTime(0.0001, t + 2.8);
    sub.connect(sg); sg.connect(master); sub.start(t + 1.1); sub.stop(t + 3);
    [0, 2, 4].forEach(function (n, k) { setTimeout(function () { chime(n + 2, false); }, 1500 + k * 260); });   // an arpeggio as the sky opens
  }

  function fadeIn() {
    var t = ctx.currentTime;
    master.gain.cancelScheduledValues(t); master.gain.setValueAtTime(master.gain.value, t); master.gain.linearRampToValueAtTime(VOLUME, t + 3);
    padBus.gain.cancelScheduledValues(t); padBus.gain.setValueAtTime(padBus.gain.value, t); padBus.gain.linearRampToValueAtTime(1, t + 6);
  }

  function fadeOut(done) {
    if (!ctx) return;
    var t = ctx.currentTime;
    master.gain.cancelScheduledValues(t); master.gain.setValueAtTime(master.gain.value, t); master.gain.linearRampToValueAtTime(0, t + 0.7);
    setTimeout(function () { if (!running && ctx && ctx.state === 'running') ctx.suspend(); if (done) done(); }, 800);
  }

  function engage() {
    if (!supported) return false;
    build();
    running = true;
    var go = function () { fadeIn(); scheduleChime(); clearInterval(chordTimer); chordTimer = setInterval(glideChord, 21000); };
    if (ctx.state === 'suspended') ctx.resume().then(go); else go();
    return true;
  }

  function disengage() {
    running = false; clearTimeout(chimeTimer); clearInterval(chordTimer);
    fadeOut();
  }

  var toggle = null;
  function renderToggle() {
    if (!toggle) return;
    var on = running;
    toggle.setAttribute('aria-pressed', on ? 'true' : 'false');
    toggle.title = on ? 'Mute the sky' : 'Play the sound of the sky';
    toggle.setAttribute('aria-label', toggle.title);
    toggle.classList.toggle('is-on', on);
  }

  function setOn(on) {
    wanted = !!on;
    write(KEY, wanted ? 'on' : 'off');
    if (wanted) engage(); else disengage();
    renderToggle();
  }

  function start() {   // called from a click: the intro's ignite button
    if (read(KEY) === 'off') { wanted = false; renderToggle(); return false; }
    wanted = true; write(KEY, 'on');
    var ok = engage(); renderToggle(); return ok;
  }

  document.addEventListener('visibilitychange', function () {
    if (!ctx) return;
    if (document.hidden) { if (ctx.state === 'running') ctx.suspend(); }
    else if (running && ctx.state === 'suspended') ctx.resume();
  });

  document.addEventListener('DOMContentLoaded', function () {
    toggle = document.getElementById('soundToggle');
    if (toggle) {
      if (!supported) toggle.hidden = true;
      toggle.addEventListener('click', function () { setOn(!running); });
      renderToggle();
    }
    // sound already chosen "on" but the intro was skipped: start at the first gesture
    if (supported && wanted && read(KEY) === 'on' && document.documentElement.getAttribute('data-intro') !== 'on') {
      var arm = function () { document.removeEventListener('pointerdown', arm, true); document.removeEventListener('keydown', arm, true); if (!running) { engage(); renderToggle(); } };
      document.addEventListener('pointerdown', arm, true); document.addEventListener('keydown', arm, true);
    }
  });

  // the classic view is quiet
  document.addEventListener('ae-home-view', function (event) {
    if (event.detail && event.detail.view === 'classic') { if (running) { disengage(); renderToggle(); } }
    else if (wanted && read(KEY) === 'on' && ctx) { engage(); renderToggle(); }
  });

  window.AESkySound = { start: start, whoosh: whoosh, chime: chime, setOn: setOn, isOn: function () { return running; }, supported: supported };
})();
