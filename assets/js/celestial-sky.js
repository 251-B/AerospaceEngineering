/**
 * CELESTIAL SKY & DYNAMIC STARRY SKIES ENGINE
 * Bachelor in Aerospace Engineering — Universidad Carlos III de Madrid (UC3M)
 * High-Performance HTML5 Canvas Engine with Subject-Themed Atmospheric Motifs
 * 
 * Features:
 * - 3-Tier Star System (Micro-stardust, Mid-field Twinkle, Foreground Luminous Flares)
 * - Aerospace Ballistic Meteors (Shooting Stars)
 * - Subject-Specific Motifs (Laminar Streamlines, FCC Lattice, Keplerian Orbits, Fourier Harmonics, Satellite Mesh)
 * - Stratospheric Cartography Light Mode (Astrolabe Arcs, Solar Gold & Sapphire Navigation Stars)
 * - Full Dark/Light Theme Sync, HiDPI Retina support, Battery Optimization & prefers-reduced-motion
 */

(function () {
  'use strict';

  // ========================================================
  // 1. CONFIGURATION & COLOR PALETTES
  // ========================================================

  const PALETTES = {
    'portal': {
      dark: {
        bgSpace: '#050811',
        stardust: ['#ffffff', '#e0f2fe', '#e0e7ff', '#fef3c7', '#fce7f3'],
        twinkleStars: ['#38bdf8', '#818cf8', '#34d399', '#fbbf24', '#f43f5e'],
        luminousStars: ['#00f0ff', '#a78bfa', '#00f59b', '#ffb703', '#ff0055'],
        meteorColor: '#38bdf8',
        motifColor: 'rgba(56, 189, 248, 0.22)',
        motifAccent: '#00f0ff'
      },
      light: {
        bgSpace: '#f8fafc',
        stardust: ['#64748b', '#94a3b8', '#cbd5e1'],
        twinkleStars: ['#0284c7', '#4f46e5', '#059669', '#d97706', '#e11d48'],
        luminousStars: ['#0369a1', '#4338ca', '#d97706'],
        meteorColor: '#d97706',
        motifColor: 'rgba(79, 70, 229, 0.15)',
        motifAccent: '#4f46e5'
      }
    },
    'fluid-mechanics': {
      dark: {
        bgSpace: '#040914',
        stardust: ['#ffffff', '#cffafe', '#e0f2fe', '#bae6fd'],
        twinkleStars: ['#00f0ff', '#38bdf8', '#06b6d4', '#2dd4bf', '#67e8f9'],
        luminousStars: ['#00f0ff', '#38bdf8', '#22d3ee'],
        meteorColor: '#00f0ff',
        motifColor: 'rgba(0, 240, 255, 0.25)',
        motifAccent: '#00f0ff'
      },
      light: {
        bgSpace: '#f8fafc',
        stardust: ['#64748b', '#94a3b8', '#0284c7'],
        twinkleStars: ['#0891b2', '#0284c7', '#0369a1', '#0d9488', '#d97706'],
        luminousStars: ['#0284c7', '#0e7490', '#d97706'],
        meteorColor: '#0284c7',
        motifColor: 'rgba(6, 182, 212, 0.18)',
        motifAccent: '#0891b2'
      }
    },
    'aerospace-materials-1': {
      dark: {
        bgSpace: '#0c0804',
        stardust: ['#ffffff', '#fef3c7', '#ffedd5', '#fde68a'],
        twinkleStars: ['#ffb703', '#fbbf24', '#f59e0b', '#f97316', '#fef08a'],
        luminousStars: ['#ffb703', '#f59e0b', '#fbbf24'],
        meteorColor: '#ffb703',
        motifColor: 'rgba(255, 183, 3, 0.24)',
        motifAccent: '#ffb703'
      },
      light: {
        bgSpace: '#fbfaf8',
        stardust: ['#78716c', '#a8a29e', '#d97706'],
        twinkleStars: ['#d97706', '#b45309', '#92400e', '#c2410c', '#475569'],
        luminousStars: ['#b45309', '#d97706', '#1e293b'],
        meteorColor: '#b45309',
        motifColor: 'rgba(217, 119, 6, 0.18)',
        motifAccent: '#b45309'
      }
    },
    'engineering-mechanics': {
      dark: {
        bgSpace: '#040c09',
        stardust: ['#ffffff', '#d1fae5', '#a7f3d0', '#ecfdf5'],
        twinkleStars: ['#00f59b', '#10b981', '#34d399', '#059669', '#6ee7b7'],
        luminousStars: ['#00f59b', '#10b981', '#34d399'],
        meteorColor: '#00f59b',
        motifColor: 'rgba(0, 245, 155, 0.25)',
        motifAccent: '#00f59b'
      },
      light: {
        bgSpace: '#f8faf9',
        stardust: ['#64748b', '#94a3b8', '#059669'],
        twinkleStars: ['#059669', '#047857', '#065f46', '#0d9488', '#d97706'],
        luminousStars: ['#047857', '#059669', '#d97706'],
        meteorColor: '#059669',
        motifColor: 'rgba(16, 185, 129, 0.18)',
        motifAccent: '#059669'
      }
    },
    'advanced-maths': {
      dark: {
        bgSpace: '#070614',
        stardust: ['#ffffff', '#ede9fe', '#e0e7ff', '#ddd6fe'],
        twinkleStars: ['#a78bfa', '#818cf8', '#6366f1', '#c084fc', '#e0e7ff'],
        luminousStars: ['#a78bfa', '#818cf8', '#c084fc'],
        meteorColor: '#a78bfa',
        motifColor: 'rgba(167, 139, 250, 0.25)',
        motifAccent: '#a78bfa'
      },
      light: {
        bgSpace: '#faf8fc',
        stardust: ['#64748b', '#94a3b8', '#6366f1'],
        twinkleStars: ['#4f46e5', '#4338ca', '#6d28d9', '#7c3aed', '#d97706'],
        luminousStars: ['#4338ca', '#6d28d9', '#d97706'],
        meteorColor: '#4f46e5',
        motifColor: 'rgba(99, 102, 241, 0.18)',
        motifAccent: '#4f46e5'
      }
    },
    'business-management': {
      dark: {
        bgSpace: '#100609',
        stardust: ['#ffffff', '#ffe4e6', '#fecdd3', '#fee2e2'],
        twinkleStars: ['#ff0055', '#fb7185', '#ef4444', '#f43f5e', '#fcd34d'],
        luminousStars: ['#ff0055', '#ef4444', '#fb7185'],
        meteorColor: '#ff0055',
        motifColor: 'rgba(255, 0, 85, 0.24)',
        motifAccent: '#ff0055'
      },
      light: {
        bgSpace: '#fcf8f9',
        stardust: ['#64748b', '#94a3b8', '#ef4444'],
        twinkleStars: ['#e11d48', '#be123c', '#9f1239', '#dc2626', '#1d4ed8'],
        luminousStars: ['#be123c', '#e11d48', '#d97706'],
        meteorColor: '#e11d48',
        motifColor: 'rgba(239, 68, 68, 0.18)',
        motifAccent: '#e11d48'
      }
    }
  };

  // ========================================================
  // 2. DETECTION HELPERS
  // ========================================================

  function detectSubject() {
    const htmlSubject = document.documentElement.getAttribute('data-celestial-subject');
    if (htmlSubject && PALETTES[htmlSubject]) return htmlSubject;

    if (document.body) {
      const bodySubject = document.body.getAttribute('data-celestial-subject');
      if (bodySubject && PALETTES[bodySubject]) return bodySubject;
    }

    const path = (window.location.pathname || '').toLowerCase();
    if (path.includes('fluid-mechanics')) return 'fluid-mechanics';
    if (path.includes('aerospace-materials-1')) return 'aerospace-materials-1';
    if (path.includes('engineering-mechanics')) return 'engineering-mechanics';
    if (path.includes('advanced-maths')) return 'advanced-maths';
    if (path.includes('business-management')) return 'business-management';

    return 'portal';
  }

  function detectTheme() {
    const attr = document.documentElement.getAttribute('data-theme');
    if (attr === 'light' || attr === 'dark') return attr;
    try {
      const stored = localStorage.getItem('ae_theme') || 
                     localStorage.getItem('aero-portal-theme') || 
                     localStorage.getItem('theme');
      if (stored === 'light' || stored === 'dark') return stored;
    } catch (e) {}
    return 'dark';
  }

  // ========================================================
  // 3. ENGINE STATE & SETUP
  // ========================================================

  let canvas = null;
  let ctx = null;
  let width = 0;
  let height = 0;
  let dpr = 1;
  let animId = null;
  let lastTime = performance.now();
  let isPaused = false;
  let reducedMotion = false;

  let currentSubject = 'portal';
  let currentTheme = 'dark';
  let currentPalette = PALETTES['portal']['dark'];

  // Entity stores
  let microStars = [];
  let midStars = [];
  let luminousStars = [];
  let meteors = [];
  let motifEntities = [];
  let meteorTimer = 0;
  let nextMeteorInterval = 5;

  function ensureCanvas() {
    canvas = document.getElementById('celestial-canvas');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'celestial-canvas';
      canvas.className = 'celestial-canvas';
      canvas.setAttribute('aria-hidden', 'true');
      document.body.prepend(canvas);
    }
    ctx = canvas.getContext('2d', { alpha: true });
  }

  // ========================================================
  // 4. ENTITY GENERATION
  // ========================================================

  function initEntities() {
    microStars = [];
    midStars = [];
    luminousStars = [];
    meteors = [];
    motifEntities = [];

    const area = width * height;
    const isDark = currentTheme === 'dark';

    // --- Tier 1: Distant Micro-stardust ---
    const microCount = Math.min(220, Math.max(70, Math.floor(area / 9500)));
    for (let i = 0; i < microCount; i++) {
      microStars.push({
        x: Math.random() * width,
        y: Math.random() * height,
        r: 0.35 + Math.random() * 0.55,
        alpha: isDark ? (0.2 + Math.random() * 0.35) : (0.12 + Math.random() * 0.22),
        color: currentPalette.stardust[Math.floor(Math.random() * currentPalette.stardust.length)],
        twinkleSpeed: 0.6 + Math.random() * 1.4,
        twinklePhase: Math.random() * Math.PI * 2
      });
    }

    // --- Tier 2: Mid-field Twinkling Stars ---
    const midCount = Math.min(80, Math.max(30, Math.floor(area / 19000)));
    for (let i = 0; i < midCount; i++) {
      midStars.push({
        x: Math.random() * width,
        y: Math.random() * height,
        r: 0.9 + Math.random() * 0.85,
        baseAlpha: isDark ? (0.35 + Math.random() * 0.25) : (0.25 + Math.random() * 0.25),
        amp: isDark ? (0.25 + Math.random() * 0.35) : (0.2 + Math.random() * 0.25),
        color: currentPalette.twinkleStars[Math.floor(Math.random() * currentPalette.twinkleStars.length)],
        freq: 1.2 + Math.random() * 2.2,
        phase: Math.random() * Math.PI * 2,
        harmonicRatio: (i % 3) + 1 // 1x, 2x, 3x for maths harmonic modulation
      });
    }

    // --- Tier 3: Foreground Luminous Stars ---
    const lumCount = Math.min(22, Math.max(10, Math.floor(area / 52000)));
    for (let i = 0; i < lumCount; i++) {
      luminousStars.push({
        x: Math.random() * width,
        y: Math.random() * height,
        r: 1.8 + Math.random() * 1.0,
        color: currentPalette.luminousStars[Math.floor(Math.random() * currentPalette.luminousStars.length)],
        pulseFreq: 0.8 + Math.random() * 1.2,
        phase: Math.random() * Math.PI * 2,
        hasCrossSpike: i < 6
      });
    }

    // --- Subject-Specific Atmospheric Motifs Setup ---
    initSubjectMotifs();
  }

  function initSubjectMotifs() {
    motifEntities = [];

    if (currentSubject === 'fluid-mechanics') {
      // Streamline flow tracers
      const streamlineCount = 5;
      for (let i = 0; i < streamlineCount; i++) {
        const yBase = (height / (streamlineCount + 1)) * (i + 1);
        motifEntities.push({
          type: 'streamline',
          yBase: yBase,
          amplitude: 25 + Math.random() * 35,
          wavelength: 380 + Math.random() * 220,
          phase: Math.random() * Math.PI * 2,
          speed: 0.6 + Math.random() * 0.5,
          particles: Array.from({ length: 4 }, (_, pIdx) => ({
            progress: (pIdx / 4) + Math.random() * 0.2,
            speed: 0.08 + Math.random() * 0.06
          }))
        });
      }
    } else if (currentSubject === 'aerospace-materials-1') {
      // Rotating unit cell wireframe glyph (FCC / Hexagonal)
      motifEntities.push({
        type: 'lattice-glyph',
        x: width - Math.min(180, width * 0.2),
        y: Math.min(180, height * 0.22),
        rotation: 0,
        radius: Math.min(75, width * 0.12),
        nodes: [
          [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
          [-1, -1,  1], [1, -1,  1], [1, 1,  1], [-1, 1,  1],
          // Face centers
          [0, 0, -1], [0, 0, 1], [-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0]
        ]
      });
    } else if (currentSubject === 'engineering-mechanics') {
      // Keplerian orbital tracks
      const cx = width * 0.78;
      const cy = height * 0.32;
      motifEntities.push({
        type: 'kepler-system',
        cx: cx,
        cy: cy,
        orbits: [
          { a: Math.min(180, width * 0.22), b: Math.min(110, width * 0.14), tilt: -0.28, anomaly: 0.2, speed: 0.28 },
          { a: Math.min(270, width * 0.34), b: Math.min(170, width * 0.21), tilt: 0.18, anomaly: 2.1, speed: 0.16 },
          { a: Math.min(360, width * 0.44), b: Math.min(230, width * 0.28), tilt: -0.12, anomaly: 4.4, speed: 0.10 }
        ]
      });
    } else if (currentSubject === 'advanced-maths') {
      // Fourier harmonic standing waves
      motifEntities.push({
        type: 'harmonic-waves',
        yCenter: height * 0.74,
        time: 0,
        waves: [
          { k: 0.008, omega: 1.2, amp: 28, phase: 0 },
          { k: 0.016, omega: 2.4, amp: 14, phase: 1.1 },
          { k: 0.024, omega: 3.6, amp: 8, phase: 2.3 }
        ]
      });
    } else if (currentSubject === 'business-management') {
      // Orbital satellite constellation mesh nodes
      const satCount = 8;
      for (let i = 0; i < satCount; i++) {
        const angle = (i / satCount) * Math.PI * 2;
        const radius = Math.min(width, height) * (0.28 + (i % 3) * 0.08);
        motifEntities.push({
          type: 'sat-node',
          angle: angle,
          orbitRadius: radius,
          cx: width * 0.5,
          cy: height * 0.52,
          speed: (0.12 + (i % 3) * 0.06) * ((i % 2 === 0) ? 1 : -1),
          pingPhase: Math.random() * Math.PI * 2
        });
      }
    } else if (currentSubject === 'portal') {
      // Grand Cosmic Harmony (faint orbital arc + subtle constellation bonds)
      motifEntities.push({
        type: 'portal-harmony',
        cx: width * 0.82,
        cy: height * 0.28,
        a: Math.min(280, width * 0.32),
        b: Math.min(180, width * 0.20),
        tilt: -0.22,
        anomaly: 1.2,
        speed: 0.2
      });
    }
  }

  // ========================================================
  // 5. UPDATE ENGINE
  // ========================================================

  function update(dt) {
    if (reducedMotion) return;

    // Meteors spawn & ballistic trajectory update
    meteorTimer += dt;
    if (meteorTimer >= nextMeteorInterval && meteors.length < 2) {
      spawnMeteor();
      meteorTimer = 0;
      nextMeteorInterval = 4.5 + Math.random() * 5.0;
    }

    for (let i = meteors.length - 1; i >= 0; i--) {
      const m = meteors[i];
      m.x += m.vx * dt;
      m.y += m.vy * dt;
      m.life -= dt;
      if (m.life <= 0 || m.x < -100 || m.x > width + 100 || m.y > height + 100) {
        meteors.splice(i, 1);
      }
    }

    // Update subject motifs
    if (currentSubject === 'fluid-mechanics') {
      motifEntities.forEach(item => {
        if (item.type === 'streamline') {
          item.phase += dt * item.speed;
          item.particles.forEach(p => {
            p.progress += dt * p.speed;
            if (p.progress > 1.0) p.progress -= 1.0;
          });
        }
      });
    } else if (currentSubject === 'aerospace-materials-1') {
      motifEntities.forEach(item => {
        if (item.type === 'lattice-glyph') {
          item.rotation += dt * 0.25;
        }
      });
    } else if (currentSubject === 'engineering-mechanics') {
      motifEntities.forEach(item => {
        if (item.type === 'kepler-system') {
          item.orbits.forEach(orb => {
            orb.anomaly += dt * orb.speed;
            if (orb.anomaly > Math.PI * 2) orb.anomaly -= Math.PI * 2;
          });
        }
      });
    } else if (currentSubject === 'advanced-maths') {
      motifEntities.forEach(item => {
        if (item.type === 'harmonic-waves') {
          item.time += dt;
        }
      });
    } else if (currentSubject === 'business-management') {
      motifEntities.forEach(item => {
        if (item.type === 'sat-node') {
          item.angle += dt * item.speed;
          item.pingPhase += dt * 2.2;
        }
      });
    } else if (currentSubject === 'portal') {
      motifEntities.forEach(item => {
        if (item.type === 'portal-harmony') {
          item.anomaly += dt * item.speed;
          if (item.anomaly > Math.PI * 2) item.anomaly -= Math.PI * 2;
        }
      });
    }
  }

  function spawnMeteor() {
    const angle = (28 + Math.random() * 24) * (Math.PI / 180);
    const speed = 750 + Math.random() * 450;
    const startX = Math.random() * (width * 0.85);
    const startY = Math.random() * (height * 0.35);
    const maxLife = 0.7 + Math.random() * 0.55;

    meteors.push({
      x: startX,
      y: startY,
      vx: Math.cos(angle) * speed,
      vy: Math.sin(angle) * speed,
      length: 120 + Math.random() * 100,
      life: maxLife,
      maxLife: maxLife,
      color: currentPalette.meteorColor
    });
  }

  // ========================================================
  // 6. RENDER ENGINE
  // ========================================================

  function draw() {
    ctx.clearRect(0, 0, width, height);

    const isLight = currentTheme === 'light';
    const now = performance.now() * 0.001;

    // If Light Mode, draw Stratospheric Cartography first
    if (isLight) {
      drawStratosphericCartography(now);
    }

    // 1. Draw Subject Motifs (Background Layer)
    drawSubjectMotifs(now, isLight);

    // 2. Draw Tier 1 Micro-stardust
    drawMicroStars(now, isLight);

    // 3. Draw Tier 2 Mid-field Twinkling Stars
    drawMidStars(now, isLight);

    // 4. Draw Tier 3 Foreground Luminous Stars
    drawLuminousStars(now, isLight);

    // 5. Draw Aerospace Meteors (Dark Mode & Reduced Motion Safe)
    if (!isLight && !reducedMotion) {
      drawMeteors();
    }
  }

  // --- Stratospheric Cartography (Light Mode) ---
  function drawStratosphericCartography(t) {
    ctx.save();
    const cx = width * 0.52;
    const cy = height * 0.44;
    const maxR = Math.max(width, height) * 0.65;

    ctx.strokeStyle = 'rgba(148, 163, 184, 0.16)';
    ctx.lineWidth = 1;

    // Concentric celestial navigation coordinate rings
    const ringRadii = [80, 160, 260, 390, 540, 720];
    ringRadii.forEach(r => {
      if (r <= maxR) {
        ctx.beginPath();
        ctx.arc(cx, cy, r, 0, Math.PI * 2);
        ctx.stroke();
      }
    });

    // Subtle meridian azimuth lines
    ctx.strokeStyle = 'rgba(148, 163, 184, 0.12)';
    for (let deg = 0; deg < 360; deg += 45) {
      const rad = deg * (Math.PI / 180);
      ctx.beginPath();
      ctx.moveTo(cx + Math.cos(rad) * 60, cy + Math.sin(rad) * 60);
      ctx.lineTo(cx + Math.cos(rad) * Math.min(maxR, 420), cy + Math.sin(rad) * Math.min(maxR, 420));
      ctx.stroke();
    }

    // Central astrolabe reticle
    ctx.strokeStyle = currentPalette.motifStroke || 'rgba(99, 102, 241, 0.22)';
    ctx.beginPath();
    ctx.arc(cx, cy, 28, 0, Math.PI * 2);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(cx - 36, cy);
    ctx.lineTo(cx + 36, cy);
    ctx.moveTo(cx, cy - 36);
    ctx.lineTo(cx, cy + 36);
    ctx.stroke();

    ctx.restore();
  }

  // --- Tier 1: Micro-stardust ---
  function drawMicroStars(t, isLight) {
    ctx.save();
    for (let i = 0; i < microStars.length; i++) {
      const s = microStars[i];
      let a = s.alpha;
      if (!reducedMotion) {
        a += Math.sin(t * s.twinkleSpeed + s.twinklePhase) * 0.08;
      }
      a = Math.max(0.04, Math.min(1.0, a));

      ctx.fillStyle = s.color;
      ctx.globalAlpha = a;
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();
  }

  // --- Tier 2: Mid-field Twinkle ---
  function drawMidStars(t, isLight) {
    ctx.save();
    for (let i = 0; i < midStars.length; i++) {
      const s = midStars[i];
      let a = s.baseAlpha;
      if (!reducedMotion) {
        const modFreq = currentSubject === 'advanced-maths' ? s.freq * s.harmonicRatio : s.freq;
        a += Math.sin(t * modFreq + s.phase) * s.amp;
      }
      a = Math.max(0.08, Math.min(1.0, a));

      ctx.fillStyle = s.color;
      ctx.globalAlpha = a;
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fill();

      // In Light Mode, add navigation diamond ticks to some stars
      if (isLight && i % 4 === 0) {
        ctx.strokeStyle = s.color;
        ctx.globalAlpha = a * 0.6;
        ctx.lineWidth = 0.8;
        ctx.beginPath();
        ctx.moveTo(s.x - 3.5, s.y);
        ctx.lineTo(s.x + 3.5, s.y);
        ctx.moveTo(s.x, s.y - 3.5);
        ctx.lineTo(s.x, s.y + 3.5);
        ctx.stroke();
      }
    }
    ctx.restore();
  }

  // --- Tier 3: Foreground Luminous Stars ---
  function drawLuminousStars(t, isLight) {
    ctx.save();
    for (let i = 0; i < luminousStars.length; i++) {
      const s = luminousStars[i];
      const pulse = reducedMotion ? 1.0 : 1.0 + Math.sin(t * s.pulseFreq + s.phase) * 0.18;
      const coreR = s.r * pulse;
      const haloR = coreR * 3.6;

      // Soft radial glow halo
      const grad = ctx.createRadialGradient(s.x, s.y, coreR * 0.4, s.x, s.y, haloR);
      grad.addColorStop(0, s.color);
      grad.addColorStop(0.35, isLight ? 'rgba(30, 58, 138, 0.18)' : 'rgba(255, 255, 255, 0.22)');
      grad.addColorStop(1, 'rgba(0, 0, 0, 0)');

      ctx.globalAlpha = isLight ? 0.65 : 0.85;
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(s.x, s.y, haloR, 0, Math.PI * 2);
      ctx.fill();

      // Sharp central star core
      ctx.globalAlpha = 1.0;
      ctx.fillStyle = isLight ? s.color : '#ffffff';
      ctx.beginPath();
      ctx.arc(s.x, s.y, coreR, 0, Math.PI * 2);
      ctx.fill();

      // 4-point astronomical diffraction spikes on prominent stars
      if (s.hasCrossSpike && !isLight) {
        ctx.strokeStyle = s.color;
        ctx.lineWidth = 0.8;
        ctx.globalAlpha = 0.45 * pulse;
        const spikeLen = coreR * 5.2;

        ctx.beginPath();
        ctx.moveTo(s.x - spikeLen, s.y);
        ctx.lineTo(s.x + spikeLen, s.y);
        ctx.moveTo(s.x, s.y - spikeLen);
        ctx.lineTo(s.x, s.y + spikeLen);
        ctx.stroke();
      }
    }
    ctx.restore();
  }

  // --- Meteors (Aerospace Ballistic Trajectory) ---
  function drawMeteors() {
    ctx.save();
    for (let i = 0; i < meteors.length; i++) {
      const m = meteors[i];
      const normLife = m.life / m.maxLife; // 1 to 0
      const alpha = Math.sin(normLife * Math.PI); // Smooth fade in and out

      const tailAngle = Math.atan2(m.vy, m.vx) + Math.PI;
      const tailX = m.x + Math.cos(tailAngle) * m.length;
      const tailY = m.y + Math.sin(tailAngle) * m.length;

      const grad = ctx.createLinearGradient(m.x, m.y, tailX, tailY);
      grad.addColorStop(0, m.color);
      grad.addColorStop(0.35, 'rgba(255, 255, 255, 0.7)');
      grad.addColorStop(1, 'rgba(255, 255, 255, 0)');

      ctx.strokeStyle = grad;
      ctx.lineWidth = 1.8;
      ctx.globalAlpha = alpha;
      ctx.beginPath();
      ctx.moveTo(m.x, m.y);
      ctx.lineTo(tailX, tailY);
      ctx.stroke();

      // Radiant meteor head flare
      ctx.fillStyle = '#ffffff';
      ctx.beginPath();
      ctx.arc(m.x, m.y, 2.2, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();
  }

  // --- Subject-Specific Motifs Rendering ---
  function drawSubjectMotifs(t, isLight) {
    if (currentSubject === 'fluid-mechanics') {
      drawFluidStreamlines(t, isLight);
    } else if (currentSubject === 'aerospace-materials-1') {
      drawMaterialsLattice(t, isLight);
    } else if (currentSubject === 'engineering-mechanics') {
      drawKeplerianOrbits(t, isLight);
    } else if (currentSubject === 'advanced-maths') {
      drawHarmonicWaves(t, isLight);
    } else if (currentSubject === 'business-management') {
      drawConstellationMesh(t, isLight);
    } else if (currentSubject === 'portal') {
      drawPortalHarmony(t, isLight);
    }
  }

  // Motifs 1: Fluid Mechanics Streamlines
  function drawFluidStreamlines(t, isLight) {
    ctx.save();
    ctx.strokeStyle = isLight ? 'rgba(6, 182, 212, 0.16)' : 'rgba(0, 240, 255, 0.14)';
    ctx.lineWidth = 1;

    motifEntities.forEach(line => {
      if (line.type !== 'streamline') return;

      ctx.beginPath();
      const step = 20;
      for (let x = 0; x <= width + step; x += step) {
        const y = line.yBase + Math.sin((x / line.wavelength) + line.phase) * line.amplitude;
        if (x === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Fluid tracer particles
      line.particles.forEach(p => {
        const px = p.progress * width;
        const py = line.yBase + Math.sin((px / line.wavelength) + line.phase) * line.amplitude;
        const pAlpha = Math.sin(p.progress * Math.PI) * (isLight ? 0.6 : 0.85);

        ctx.fillStyle = isLight ? '#0891b2' : '#00f0ff';
        ctx.globalAlpha = pAlpha;
        ctx.beginPath();
        ctx.arc(px, py, 2.0, 0, Math.PI * 2);
        ctx.fill();
      });
    });
    ctx.restore();
  }

  // Motifs 2: Aerospace Materials Crystalline Constellations & 3D Lattice
  function drawMaterialsLattice(t, isLight) {
    ctx.save();
    // Connect proximate stars with crystalline lattice bonds
    const stars = luminousStars.concat(midStars.slice(0, 22));
    const maxDist = 115;
    ctx.strokeStyle = isLight ? 'rgba(217, 119, 6, 0.16)' : 'rgba(255, 183, 3, 0.18)';
    ctx.lineWidth = 0.85;

    for (let i = 0; i < stars.length; i++) {
      for (let j = i + 1; j < stars.length; j++) {
        const dx = stars[i].x - stars[j].x;
        const dy = stars[i].y - stars[j].y;
        const dist = Math.hypot(dx, dy);
        if (dist < maxDist) {
          const alpha = (1 - dist / maxDist) * (isLight ? 0.45 : 0.65);
          ctx.globalAlpha = alpha;
          ctx.beginPath();
          ctx.moveTo(stars[i].x, stars[i].y);
          ctx.lineTo(stars[j].x, stars[j].y);
          ctx.stroke();
        }
      }
    }

    // Rotating isometric FCC unit cell glyph
    motifEntities.forEach(glyph => {
      if (glyph.type !== 'lattice-glyph') return;
      ctx.globalAlpha = isLight ? 0.35 : 0.55;
      ctx.strokeStyle = isLight ? '#d97706' : '#ffb703';
      ctx.lineWidth = 1;

      const cosR = Math.cos(glyph.rotation);
      const sinR = Math.sin(glyph.rotation);

      // Project 3D nodes
      const projected = glyph.nodes.map(([x3, y3, z3]) => {
        // Rotate around Y and X axis
        const rx = x3 * cosR - z3 * sinR;
        const rz = x3 * sinR + z3 * cosR;
        const ry = y3 * 0.85 - rz * 0.35;
        return {
          px: glyph.x + rx * glyph.radius * 0.55,
          py: glyph.y + ry * glyph.radius * 0.55
        };
      });

      // Draw cube edges
      const edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
      ];
      edges.forEach(([i1, i2]) => {
        ctx.beginPath();
        ctx.moveTo(projected[i1].px, projected[i1].py);
        ctx.lineTo(projected[i2].px, projected[i2].py);
        ctx.stroke();
      });

      // Draw atomic vertex spheres
      projected.forEach(p => {
        ctx.fillStyle = isLight ? '#b45309' : '#fbbf24';
        ctx.beginPath();
        ctx.arc(p.px, p.py, 2.2, 0, Math.PI * 2);
        ctx.fill();
      });
    });
    ctx.restore();
  }

  // Motifs 3: Engineering Mechanics Keplerian Orbits
  function drawKeplerianOrbits(t, isLight) {
    ctx.save();
    motifEntities.forEach(sys => {
      if (sys.type !== 'kepler-system') return;

      sys.orbits.forEach(orb => {
        ctx.save();
        ctx.translate(sys.cx, sys.cy);
        ctx.rotate(orb.tilt);

        // Orbit path
        ctx.strokeStyle = isLight ? 'rgba(5, 150, 105, 0.18)' : 'rgba(0, 245, 155, 0.20)';
        ctx.lineWidth = 1;
        ctx.setLineDash([5, 7]);
        ctx.beginPath();
        ctx.ellipse(0, 0, orb.a, orb.b, 0, 0, Math.PI * 2);
        ctx.stroke();

        // Orbiting state vector / satellite
        const satX = orb.a * Math.cos(orb.anomaly);
        const satY = orb.b * Math.sin(orb.anomaly);

        ctx.setLineDash([]);
        ctx.fillStyle = isLight ? '#059669' : '#00f59b';
        ctx.globalAlpha = 0.9;
        ctx.beginPath();
        ctx.arc(satX, satY, 3.2, 0, Math.PI * 2);
        ctx.fill();

        // Orbit velocity vector indicator
        const vx = -orb.a * Math.sin(orb.anomaly) * 0.12;
        const vy = orb.b * Math.cos(orb.anomaly) * 0.12;
        ctx.strokeStyle = isLight ? 'rgba(5, 150, 105, 0.45)' : 'rgba(0, 245, 155, 0.6)';
        ctx.lineWidth = 1.2;
        ctx.beginPath();
        ctx.moveTo(satX, satY);
        ctx.lineTo(satX + vx, satY + vy);
        ctx.stroke();

        ctx.restore();
      });

      // Inertial reference frame triad {X_I, Y_I}
      const triadX = Math.min(80, width * 0.08);
      const triadY = height - Math.min(80, height * 0.1);
      ctx.strokeStyle = isLight ? 'rgba(5, 150, 105, 0.45)' : 'rgba(0, 245, 155, 0.45)';
      ctx.lineWidth = 1.2;

      ctx.beginPath();
      ctx.moveTo(triadX, triadY);
      ctx.lineTo(triadX + 38, triadY); // X-axis
      ctx.moveTo(triadX, triadY);
      ctx.lineTo(triadX, triadY - 38); // Y-axis
      ctx.stroke();

      ctx.fillStyle = isLight ? '#047857' : '#00f59b';
      ctx.font = '10px monospace';
      ctx.fillText('X_I', triadX + 42, triadY + 4);
      ctx.fillText('Y_I', triadX - 4, triadY - 42);
    });
    ctx.restore();
  }

  // Motifs 4: Advanced Mathematics Harmonic Waves
  function drawHarmonicWaves(t, isLight) {
    ctx.save();
    motifEntities.forEach(item => {
      if (item.type !== 'harmonic-waves') return;

      item.waves.forEach((w, idx) => {
        ctx.strokeStyle = isLight ? 'rgba(79, 70, 229, 0.18)' : 'rgba(167, 139, 250, 0.20)';
        ctx.lineWidth = 1.1;
        ctx.beginPath();

        const step = 16;
        for (let x = 0; x <= width + step; x += step) {
          const y = item.yCenter + Math.sin(x * w.k - item.time * w.omega + w.phase) * w.amp;
          if (x === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();
      });
    });
    ctx.restore();
  }

  // Motifs 5: Business Management Constellation Mesh
  function drawConstellationMesh(t, isLight) {
    ctx.save();
    const sats = [];
    motifEntities.forEach(node => {
      if (node.type !== 'sat-node') return;
      const x = node.cx + Math.cos(node.angle) * node.orbitRadius;
      const y = node.cy + Math.sin(node.angle) * (node.orbitRadius * 0.58);
      sats.push({ x, y, ping: node.pingPhase });
    });

    // Dynamic Inter-Satellite Laser Links (ISL)
    const maxLinkDist = 180;
    ctx.lineWidth = 1;
    for (let i = 0; i < sats.length; i++) {
      for (let j = i + 1; j < sats.length; j++) {
        const dx = sats[i].x - sats[j].x;
        const dy = sats[i].y - sats[j].y;
        const dist = Math.hypot(dx, dy);
        if (dist < maxLinkDist) {
          const alpha = (1 - dist / maxLinkDist) * (isLight ? 0.45 : 0.65);
          ctx.strokeStyle = isLight ? 'rgba(225, 29, 72, 0.35)' : 'rgba(255, 0, 85, 0.45)';
          ctx.globalAlpha = alpha;
          ctx.beginPath();
          ctx.moveTo(sats[i].x, sats[i].y);
          ctx.lineTo(sats[j].x, sats[j].y);
          ctx.stroke();
        }
      }
    }

    // Satellite nodes & telemetry rings
    sats.forEach(s => {
      ctx.globalAlpha = 0.9;
      ctx.fillStyle = isLight ? '#e11d48' : '#ff0055';
      ctx.beginPath();
      ctx.arc(s.x, s.y, 2.8, 0, Math.PI * 2);
      ctx.fill();

      // Telemetry pulse ring
      const ringR = 4 + (Math.sin(s.ping) + 1) * 4;
      ctx.strokeStyle = isLight ? 'rgba(225, 29, 72, 0.45)' : 'rgba(255, 0, 85, 0.45)';
      ctx.lineWidth = 0.8;
      ctx.beginPath();
      ctx.arc(s.x, s.y, ringR, 0, Math.PI * 2);
      ctx.stroke();
    });

    ctx.restore();
  }

  // Motifs 6: Portal Grand Cosmic Harmony
  function drawPortalHarmony(t, isLight) {
    ctx.save();
    // Constellation bonds between nearby luminous stars
    ctx.strokeStyle = isLight ? 'rgba(79, 70, 229, 0.14)' : 'rgba(56, 189, 248, 0.16)';
    ctx.lineWidth = 0.8;
    for (let i = 0; i < luminousStars.length; i++) {
      for (let j = i + 1; j < luminousStars.length; j++) {
        const dx = luminousStars[i].x - luminousStars[j].x;
        const dy = luminousStars[i].y - luminousStars[j].y;
        const dist = Math.hypot(dx, dy);
        if (dist < 140) {
          ctx.globalAlpha = (1 - dist / 140) * 0.45;
          ctx.beginPath();
          ctx.moveTo(luminousStars[i].x, luminousStars[i].y);
          ctx.lineTo(luminousStars[j].x, luminousStars[j].y);
          ctx.stroke();
        }
      }
    }

    // Gentle orbital track
    motifEntities.forEach(orb => {
      if (orb.type !== 'portal-harmony') return;
      ctx.save();
      ctx.translate(orb.cx, orb.cy);
      ctx.rotate(orb.tilt);
      ctx.strokeStyle = isLight ? 'rgba(2, 132, 199, 0.15)' : 'rgba(0, 240, 255, 0.16)';
      ctx.lineWidth = 1;
      ctx.setLineDash([4, 6]);
      ctx.beginPath();
      ctx.ellipse(0, 0, orb.a, orb.b, 0, 0, Math.PI * 2);
      ctx.stroke();

      const satX = orb.a * Math.cos(orb.anomaly);
      const satY = orb.b * Math.sin(orb.anomaly);
      ctx.setLineDash([]);
      ctx.fillStyle = isLight ? '#0284c7' : '#00f0ff';
      ctx.globalAlpha = 0.85;
      ctx.beginPath();
      ctx.arc(satX, satY, 2.8, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    });
    ctx.restore();
  }

  // ========================================================
  // 7. ANIMATION LOOP & LIFECYCLE
  // ========================================================

  function animate(currentTime) {
    if (isPaused) return;

    const dt = Math.min((currentTime - lastTime) / 1000, 0.1);
    lastTime = currentTime;

    update(dt);
    draw();

    if (!reducedMotion) {
      animId = requestAnimationFrame(animate);
    }
  }

  function startAnimation() {
    if (animId) cancelAnimationFrame(animId);
    if (reducedMotion) {
      draw();
      return;
    }
    lastTime = performance.now();
    animId = requestAnimationFrame(animate);
  }

  function handleResize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = window.innerWidth;
    height = window.innerHeight;

    canvas.width = Math.floor(width * dpr);
    canvas.height = Math.floor(height * dpr);
    canvas.style.width = width + 'px';
    canvas.style.height = height + 'px';

    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.scale(dpr, dpr);

    initEntities();
    draw();
  }

  let resizeTimeout = null;
  function debouncedResize() {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(handleResize, 150);
  }

  function rebuildStars() {
    currentPalette = PALETTES[currentSubject][currentTheme] || PALETTES['portal'][currentTheme];
    initEntities();
    draw();
  }

  function setupObservers() {
    // Visibility change (Battery Saver)
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        isPaused = true;
        if (animId) cancelAnimationFrame(animId);
      } else {
        isPaused = false;
        lastTime = performance.now();
        startAnimation();
      }
    });

    // prefers-reduced-motion media query
    const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    reducedMotion = motionQuery.matches;
    motionQuery.addEventListener('change', (e) => {
      reducedMotion = e.matches;
      if (reducedMotion) {
        if (animId) cancelAnimationFrame(animId);
        draw();
      } else {
        startAnimation();
      }
    });

    // Theme & Subject Mutation Observer
    const observer = new MutationObserver(mutations => {
      for (const m of mutations) {
        if (m.attributeName === 'data-theme') {
          const newTheme = detectTheme();
          if (newTheme !== currentTheme) {
            currentTheme = newTheme;
            rebuildStars();
          }
        } else if (m.attributeName === 'data-celestial-subject') {
          const newSub = detectSubject();
          if (newSub !== currentSubject) {
            currentSubject = newSub;
            rebuildStars();
          }
        }
      }
    });
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['data-theme', 'data-celestial-subject']
    });

    // Storage event for multi-tab sync
    window.addEventListener('storage', e => {
      if (e.key === 'ae_theme' || e.key === 'aero-portal-theme' || e.key === 'theme') {
        const newTheme = detectTheme();
        if (newTheme !== currentTheme) {
          currentTheme = newTheme;
          rebuildStars();
        }
      }
    });

    // Window resize
    window.addEventListener('resize', debouncedResize, { passive: true });
  }

  // ========================================================
  // 8. INITIALIZATION
  // ========================================================

  function init() {
    currentSubject = detectSubject();
    currentTheme = detectTheme();

    // Ensure documentElement has the subject attribute set
    if (!document.documentElement.getAttribute('data-celestial-subject')) {
      document.documentElement.setAttribute('data-celestial-subject', currentSubject);
    }

    currentPalette = PALETTES[currentSubject][currentTheme] || PALETTES['portal'][currentTheme];

    ensureCanvas();
    handleResize();
    setupObservers();
    startAnimation();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Export engine handle for debugging or external controls if needed
  window.CelestialSkyEngine = {
    getSubject: () => currentSubject,
    getTheme: () => currentTheme,
    rebuild: rebuildStars
  };
})();
