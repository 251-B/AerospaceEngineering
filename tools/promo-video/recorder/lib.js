// Deterministic 60 fps recorder: Playwright fake clock + per-frame screenshots piped to ffmpeg.
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const { routeCdn, BASE } = require('./common');

const FPS = 60;
const DT = 1000 / FPS;
const OUT = path.join(__dirname, 'clips');
fs.mkdirSync(OUT, { recursive: true });

const DEVICES = {
  desktop: { viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1, touch: false },
  tablet: { viewport: { width: 820, height: 1180 }, deviceScaleFactor: 1.5, touch: true, isMobile: true },
  mobile: { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, touch: true, isMobile: true },
};

const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2); // easeInOutCubic
const lerp = (a, b, t) => a + (b - a) * t;

const CURSOR_JS = (touch) => `
(() => {
  if (document.getElementById('__promoCursor')) return;
  const c = document.createElement('div');
  c.id = '__promoCursor';
  c.style.cssText = 'position:fixed;left:0;top:0;z-index:2147483647;pointer-events:none;will-change:transform;transition:none;';
  c.innerHTML = ${touch}
    ? '<div style="width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;background:rgba(255,255,255,.35);border:2px solid rgba(255,255,255,.9);box-shadow:0 0 0 1px rgba(0,0,0,.35),0 4px 14px rgba(0,0,0,.35);"></div>'
    : '<svg width="30" height="30" viewBox="0 0 24 24" style="filter:drop-shadow(0 2px 4px rgba(0,0,0,.5))"><path d="M4 2 L4 19 L8.5 14.8 L11.6 21.6 L14.6 20.3 L11.6 13.6 L17.8 13.4 Z" fill="#fff" stroke="#111" stroke-width="1.3" stroke-linejoin="round"/></svg>';
  const r = document.createElement('div');
  r.id = '__promoRipple';
  r.style.cssText = 'position:fixed;left:0;top:0;width:60px;height:60px;margin:-30px 0 0 -30px;border-radius:50%;border:3px solid rgba(96,200,255,.95);z-index:2147483646;pointer-events:none;opacity:0;transition:none;';
  document.documentElement.appendChild(r);
  document.documentElement.appendChild(c);
  window.__promoSet = (x, y, show) => { c.style.transform = 'translate(' + x + 'px,' + y + 'px)'; c.style.opacity = show ? 1 : 0; };
  window.__promoRip = (x, y, k) => { r.style.left = x + 'px'; r.style.top = y + 'px'; r.style.opacity = k <= 0 || k >= 1 ? 0 : (1 - k); r.style.transform = 'scale(' + (0.3 + k * 1.2) + ')'; };
  window.__promoSet(-100, -100, false);
})();`;

class Recorder {
  constructor(browser, device) {
    this.browser = browser;
    this.deviceName = device;
    this.dev = DEVICES[device];
    this.cursor = { x: this.dev.viewport.width * 0.6, y: this.dev.viewport.height * 0.6, show: !this.dev.touch };
  }

  async open(url, { theme = 'dark', storage = {} } = {}) {
    const d = this.dev;
    this.ctx = await this.browser.newContext({
      viewport: d.viewport, deviceScaleFactor: d.deviceScaleFactor, hasTouch: d.touch, isMobile: !!d.isMobile,
      colorScheme: theme, reducedMotion: 'no-preference',
    });
    await routeCdn(this.ctx);
    const init = { ae_theme: theme, ...storage };
    await this.ctx.addInitScript((kv) => {
      try { if (!sessionStorage.getItem('__promoInit')) { for (const k in kv) localStorage.setItem(k, kv[k]); sessionStorage.setItem('__promoInit', '1'); } } catch (e) {}
    }, init);
    this.page = await this.ctx.newPage();
    this.page.on('pageerror', (e) => console.log('  [pageerror]', e.message));
    await this.page.clock.install({ time: new Date('2026-10-14T10:00:00') });
    await this.goto(url);
    this.cdp = await this.ctx.newCDPSession(this.page);
    await this.cdp.send('Animation.enable');
  }

  async goto(url) {
    await this.page.goto(BASE + url, { waitUntil: 'load' });
    await this.page.evaluate(() => document.fonts.ready);
    await this.page.clock.runFor(1500);
    await this.page.waitForTimeout(300);
    await this.page.evaluate(CURSOR_JS(this.dev.touch));
    await this.page.evaluate(() => { document.documentElement.style.scrollBehavior = 'auto'; });
    await this.syncCursor();
  }

  async syncCursor() {
    const { x, y, show } = this.cursor;
    await this.page.evaluate(([x, y, s]) => window.__promoSet && window.__promoSet(x, y, s), [x, y, show]);
  }

  // Start a clip: frames go to clips/<name>.mp4
  async start(name) {
    const file = path.join(OUT, `${this.deviceName}-${name}.mp4`);
    this.ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
      '-c:v', 'libx264', '-preset', 'medium', '-crf', '15', '-pix_fmt', 'yuv420p', '-r', String(FPS), file], { stdio: ['pipe', 'inherit', 'inherit'] });
    this.frames = 0;
    this.file = file;
    await this.calibrate();
    console.log(`  ● ${this.deviceName}-${name}`);
  }

  // Make CSS transitions advance ~1/60 s of animation time per captured frame.
  async calibrate() {
    const t0 = Date.now();
    for (let i = 0; i < 4; i++) await this.page.screenshot({ type: 'jpeg', quality: 50 });
    const ms = (Date.now() - t0) / 4;
    this.rate = Math.min(1, DT / ms);
    await this.cdp.send('Animation.setPlaybackRate', { playbackRate: this.rate });
  }

  async frame() {
    await this.page.clock.runFor(DT);
    const buf = await this.page.screenshot({ type: 'jpeg', quality: 93, animations: 'allow', caret: 'initial' });
    if (!this.ff.stdin.write(buf)) await new Promise((r) => this.ff.stdin.once('drain', r));
    this.frames++;
  }

  async wait(sec) { for (let i = 0, n = Math.round(sec * FPS); i < n; i++) await this.frame(); }

  async stop() {
    this.ff.stdin.end();
    await new Promise((r) => this.ff.on('close', r));
    console.log(`    ${this.frames} frames (${(this.frames / FPS).toFixed(2)} s) -> ${path.basename(this.file)}`);
    await this.cdp.send('Animation.setPlaybackRate', { playbackRate: 1 });
  }

  // Smoothly scroll the window (or an element) to an absolute Y over `sec`.
  async scrollTo(y, sec, sel = null) {
    const from = await this.page.evaluate((s) => (s ? document.querySelector(s).scrollTop : window.scrollY), sel);
    const max = await this.page.evaluate((s) => (s ? document.querySelector(s).scrollHeight - document.querySelector(s).clientHeight : document.documentElement.scrollHeight - innerHeight), sel);
    const to = Math.max(0, Math.min(max, y));
    const n = Math.round(sec * FPS);
    for (let i = 1; i <= n; i++) {
      const v = lerp(from, to, ease(i / n));
      await this.page.evaluate(([v, s]) => { if (s) document.querySelector(s).scrollTop = v; else window.scrollTo(0, v); }, [v, sel]);
      await this.frame();
    }
  }

  async scrollToEl(selector, sec, offset = 120, nth = 0) {
    const y = await this.page.evaluate(([s, o, n]) => {
      const el = document.querySelectorAll(s)[n];
      return el.getBoundingClientRect().top + window.scrollY - o;
    }, [selector, offset, nth]);
    await this.scrollTo(y, sec);
  }

  async box(selector, nth = 0) {
    return this.page.evaluate(([s, n]) => {
      const el = typeof s === 'string' ? document.querySelectorAll(s)[n] : null;
      if (!el) return null;
      const r = el.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2, w: r.width, h: r.height, top: r.top, left: r.left };
    }, [selector, nth]);
  }

  async moveTo(x, y, sec = 0.7) {
    const fx = this.cursor.x, fy = this.cursor.y;
    if (this.dev.touch) { this.cursor = { x, y, show: false }; return; }
    const n = Math.max(1, Math.round(sec * FPS));
    for (let i = 1; i <= n; i++) {
      const k = ease(i / n);
      this.cursor = { x: lerp(fx, x, k), y: lerp(fy, y, k) - Math.sin(Math.PI * k) * 30, show: true };
      await this.page.mouse.move(this.cursor.x, this.cursor.y);
      await this.syncCursor();
      await this.frame();
    }
  }

  async moveToEl(selector, sec = 0.7, nth = 0, dx = 0, dy = 0) {
    const b = await this.box(selector, nth);
    if (!b) throw new Error('missing ' + selector);
    await this.moveTo(b.x + dx, b.y + dy, sec);
    return b;
  }

  async ripple(x, y, frames = 24, touch = this.dev.touch) {
    for (let i = 0; i <= frames; i++) {
      const k = i / frames;
      if (touch) await this.page.evaluate(([x, y, s]) => window.__promoSet(x, y, s), [x, y, k < 0.6]);
      await this.page.evaluate(([x, y, k]) => window.__promoRip(x, y, k), [x, y, k]);
      if (i < frames) await this.frame();
    }
    if (touch) await this.page.evaluate(() => window.__promoSet(-100, -100, false));
  }

  // Click/tap an element with a visible pointer and ripple.
  async click(selector, { nth = 0, sec = 0.7, dx = 0, dy = 0, after = 0.4 } = {}) {
    const b = await this.moveToEl(selector, sec, nth, dx, dy);
    const x = b.x + dx, y = b.y + dy;
    if (this.dev.touch) {
      for (let i = 0; i < 8; i++) { await this.page.evaluate(([x, y]) => window.__promoSet(x, y, true), [x, y]); await this.frame(); }
      await this.page.touchscreen.tap(x, y);
    } else {
      await this.page.mouse.click(x, y);
    }
    await this.ripple(x, y);
    await this.syncCursor();
    await this.wait(after);
  }

  async type(text, cps = 14) {
    for (const ch of text) {
      await this.page.keyboard.type(ch);
      await this.wait(1 / cps);
    }
  }

  async close() { await this.ctx.close(); }
}

async function launch() {
  return chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required', '--hide-scrollbars', '--force-color-profile=srgb'] });
}

module.exports = { Recorder, launch, FPS };
