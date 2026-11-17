/*!
 * Home page, welcome screen (root index.html only): a night sky seen through a telescope, the name,
 * "Ready to ignite?" and a button. Pressing it starts the celestial sound, throws the stars into a
 * warp, flashes and drops the visitor into the constellation map ("entering space").
 *
 * Shown once per browser session (sessionStorage key ae_intro) and only in the stellar view; the head part of
 * constellations.js sets <html data-intro="on"> before the first paint. ?intro=1 shows it again, ?intro=0 never.
 * With prefers-reduced-motion the warp is replaced by a short fade. No audio files: the sound is
 * assets/js/sky-sound.js. The map underneath is inert while the welcome screen is up.
 *
 * Events: document 'ae-intro-done' when the welcome screen has gone.
 */
(function () {
  'use strict';

  var root = document.documentElement;
  if (root.getAttribute('data-intro') !== 'on') return;

  function ready(fn) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn); else fn(); }

  ready(function () {
    var intro = document.getElementById('skyIntro');
    var canvas = document.getElementById('introCanvas');
    var button = document.getElementById('introIgnite');
    var skip = document.getElementById('introSkip');
    var app = document.querySelector('.app-wrapper');
    if (!intro || !canvas || !button) { root.removeAttribute('data-intro'); return; }

    var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var ctx = canvas.getContext('2d');
    var W = 0, H = 0, dpr = 1, running = true;
    var stars = [];
    var phase = 'idle', t0 = 0;           // idle | warp | decel
    var speed = 0.012;                    // depth units per second

    if (app) app.setAttribute('inert', '');
    try { document.activeElement && document.activeElement.blur(); } catch (e) { /* nothing focused */ }

    function resize() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = canvas.width = Math.round(window.innerWidth * dpr);
      H = canvas.height = Math.round(window.innerHeight * dpr);
      canvas.style.width = window.innerWidth + 'px'; canvas.style.height = window.innerHeight + 'px';
    }
    resize();
    window.addEventListener('resize', resize);

    var TINTS = ['255,255,255', '255,255,255', '200,225,255', '255,235,205', '190,170,255', '150,230,255'];
    function seed(star, anywhere) {
      star.x = (Math.random() * 2 - 1) * 1.15;
      star.y = (Math.random() * 2 - 1) * 1.15;
      star.z = anywhere ? Math.random() * 0.98 + 0.02 : 1;
      star.tint = TINTS[Math.floor(Math.random() * TINTS.length)];
      star.tw = Math.random() * 6.28;
      star.size = 0.6 + Math.random() * 1.5;
    }
    var COUNT = Math.round(Math.min(620, Math.max(260, window.innerWidth * window.innerHeight / 3600)));
    for (var i = 0; i < COUNT; i++) { var s0 = {}; seed(s0, true); stars.push(s0); }

    var last = 0;
    function frame(now) {
      if (!running) return;
      var dt = Math.min(0.05, (now - (last || now)) / 1000); last = now;
      var el = phase === 'idle' ? 0 : (now - t0) / 1000;
      if (phase === 'warp') {
        var k = Math.min(1, el / 1.7);
        speed = 0.012 + 4.2 * k * k * k;
        if (el > 2.0) { phase = 'decel'; t0 = now; }
      } else if (phase === 'decel') {
        speed = Math.max(0.2, speed * Math.pow(0.02, dt));
      }
      var cx = W / 2, cy = H / 2, scale = Math.max(W, H) * 0.55;
      ctx.clearRect(0, 0, W, H);
      var warping = phase !== 'idle' && speed > 0.06;
      var warmth = phase === 'warp' ? Math.min(1, el / 1.5) : 0;
      for (var n = 0; n < stars.length; n++) {
        var st = stars[n], pz = st.z;
        st.z -= speed * dt;
        if (st.z <= 0.015) { seed(st, false); st.z = 1; pz = 1; }
        var sx = cx + st.x / st.z * scale * 0.5, sy = cy + st.y / st.z * scale * 0.5;
        var px = cx + st.x / pz * scale * 0.5, py = cy + st.y / pz * scale * 0.5;
        var depth = 1 - st.z;
        var alpha = Math.min(1, 0.45 + depth * 0.9);
        if (phase === 'idle') {
          st.tw += dt * (0.8 + st.size);
          alpha *= 0.6 + 0.4 * Math.sin(st.tw);
          ctx.fillStyle = 'rgba(' + st.tint + ',' + alpha.toFixed(3) + ')';
          ctx.beginPath(); ctx.arc(sx, sy, st.size * dpr * (0.7 + depth * 1.1), 0, 6.283); ctx.fill();
        } else {
          ctx.strokeStyle = 'rgba(' + (warmth > 0.6 && n % 5 === 0 ? '170,200,255' : st.tint) + ',' + alpha.toFixed(3) + ')';
          ctx.lineWidth = Math.max(0.6, st.size * dpr * (0.5 + depth * 1.4));
          ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(sx, sy); ctx.stroke();
        }
      }
      requestAnimationFrame(frame);
    }
    if (!reduced) requestAnimationFrame(frame);
    else {   // one still frame
      for (var m = 0; m < stars.length; m++) {
        var q = stars[m], x = W / 2 + q.x / q.z * Math.max(W, H) * 0.275, y = H / 2 + q.y / q.z * Math.max(W, H) * 0.275;
        ctx.fillStyle = 'rgba(' + q.tint + ',0.7)'; ctx.beginPath(); ctx.arc(x, y, q.size * dpr, 0, 6.283); ctx.fill();
      }
    }

    function finish() {
      running = false;
      window.removeEventListener('resize', resize);
      if (app) app.removeAttribute('inert');
      root.removeAttribute('data-intro');
      intro.classList.remove('is-igniting', 'is-leaving');
      document.dispatchEvent(new CustomEvent('ae-intro-done'));
      var sv = document.getElementById('skyView');
      if (sv && sv.focus) { try { sv.setAttribute('tabindex', '-1'); sv.focus({ preventScroll: true }); } catch (e) { /* focus not possible */ } }
    }

    function enter(withSound) {
      if (intro.classList.contains('is-igniting')) return;
      try { sessionStorage.setItem('ae_intro', 'seen'); } catch (e) { /* storage blocked */ }
      var sv = document.getElementById('skyView');
      intro.classList.add('is-igniting');
      button.disabled = true;
      if (withSound && window.AESkySound) { window.AESkySound.start(); window.AESkySound.whoosh(); }
      if (reduced) {
        setTimeout(function () { intro.classList.add('is-leaving'); if (sv) sv.classList.add('is-entering'); }, 150);
        setTimeout(function () { finish(); }, 750);
        setTimeout(function () { if (sv) sv.classList.remove('is-entering'); }, 2200);
        return;
      }
      phase = 'warp'; t0 = performance.now();
      setTimeout(function () { intro.classList.add('is-flash'); }, 1150);
      setTimeout(function () { intro.classList.add('is-leaving'); if (sv) sv.classList.add('is-entering'); }, 1750);
      setTimeout(function () { finish(); }, 3050);
      setTimeout(function () { if (sv) sv.classList.remove('is-entering'); }, 5200);
    }

    button.addEventListener('click', function () { enter(true); });
    if (skip) skip.addEventListener('click', function () { enter(false); });
    document.addEventListener('keydown', function (event) {
      if (root.getAttribute('data-intro') !== 'on') return;
      if (event.key === 'Escape') { event.preventDefault(); enter(false); }
    });
    setTimeout(function () { try { button.focus({ preventScroll: true }); } catch (e) { /* focus not possible */ } }, 400);
  });
})();
