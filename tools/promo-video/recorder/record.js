// Shot list. Usage: node record.js <desktop|tablet|mobile> [clipName ...]
const { Recorder, launch } = require('./lib');

const EM_T3 = '/subjects/engineering-mechanics/teoria/topic-3.html';
const EM_P1 = '/subjects/engineering-mechanics/problemas/topic-1.html';
const AM_T2 = '/subjects/aerospace-materials-1/teoria/topic-2-structure.html';
const FM_EX = '/subjects/fluid-mechanics/exams/index.html';
const FM_SRC = '/subjects/fluid-mechanics/sources/index.html';

// Select a text range by dragging the mouse across it (desktop) frame by frame.
async function dragSelect(r, selector, frac = 0.9, sec = 1.0) {
  const pts = await r.page.evaluate(([s, f]) => {
    const el = document.querySelector(s);
    const range = document.createRange();
    const tn = [...el.childNodes].find((n) => n.nodeType === 3 && n.textContent.trim().length > 40) || el.firstChild;
    range.setStart(tn, 0); range.setEnd(tn, Math.floor(tn.textContent.length * f));
    const rects = range.getClientRects();
    const a = rects[0], b = rects[rects.length - 1];
    return { x0: a.left + 1, y0: a.top + a.height / 2, x1: b.right - 1, y1: b.top + b.height / 2 };
  }, [selector, frac]);
  await r.moveTo(pts.x0, pts.y0, 0.6);
  await r.page.mouse.down();
  const n = Math.round(sec * 60);
  for (let i = 1; i <= n; i++) {
    const k = i / n;
    const x = pts.x0 + (pts.x1 - pts.x0) * k, y = pts.y0 + (pts.y1 - pts.y0) * k;
    r.cursor = { x, y, show: true };
    await r.page.mouse.move(x, y);
    await r.syncCursor();
    await r.frame();
  }
  await r.page.mouse.up();
}

// Touch devices: select programmatically, the pill reacts to selectionchange.
async function rangeSelect(r, selector, frac = 0.9) {
  await r.page.evaluate(([s, f]) => {
    const el = document.querySelector(s);
    const tn = [...el.childNodes].find((n) => n.nodeType === 3 && n.textContent.trim().length > 40) || el.firstChild;
    const range = document.createRange();
    range.setStart(tn, 0); range.setEnd(tn, Math.floor(tn.textContent.length * f));
    const sel = getSelection(); sel.removeAllRanges(); sel.addRange(range);
  }, [selector, frac]);
}

const CLIPS = {
  desktop: {
    async hub(r) {
      await r.open('/index.html');
      await r.start('hub');
      await r.wait(1.6);
      await r.moveTo(1100, 360, 0.8);
      await r.scrollTo(470, 2.4);
      await r.moveToEl('.subject-card, .subjects-grid > *', 0.8, 2);
      await r.wait(0.6);
      await r.moveToEl('.subjects-grid > * a, .subjects-grid > * li', 0.6, 0);
      await r.wait(0.8);
      await r.stop();
      await r.close();
    },
    async search(r) {
      await r.open('/index.html');
      await r.page.evaluate(() => scrollTo(0, 300));
      await r.start('search');
      await r.wait(0.5);
      await r.click('#searchInput', { sec: 0.8, dx: -120, after: 0.2 });
      await r.type('Kepler', 9);
      await r.wait(1.4);
      for (let i = 0; i < 6; i++) { await r.page.keyboard.press('Backspace'); await r.wait(0.05); }
      await r.type('Fick', 9);
      await r.wait(1.2);
      await r.page.keyboard.press('Escape');
      await r.wait(0.4);
      await r.click('.semester-tab', { nth: 2, sec: 0.8, after: 1.2 });
      await r.click('.semester-tab', { nth: 0, sec: 0.6, after: 0.6 });
      await r.stop();
      await r.close();
    },
    async theory(r) {
      await r.open(EM_T3);
      await r.page.evaluate(() => scrollTo(0, 4930));
      await r.start('theory');
      await r.wait(0.8);
      await r.moveTo(1180, 560, 0.8);
      await r.scrollTo(5560, 2.6);
      await r.wait(0.6);
      await r.scrollTo(6280, 2.6);
      await r.wait(0.8);
      await r.stop();
      await r.close();
    },
    async problems(r) {
      await r.open(EM_P1);
      await r.start('problems');
      await r.wait(0.5);
      await r.moveToEl('.src-link', 0.9, 1);
      await r.wait(0.6);
      await r.moveToEl('.problem-card .pdf-link', 0.6, 0);
      await r.wait(0.4);
      await r.scrollToEl('.solution-summary', 1.8, 640, 0);
      await r.click('.solution-summary', { nth: 0, sec: 0.7, dx: -200, after: 0.5 });
      await r.scrollToEl('.phase-block', 1.6, 110, 0);
      await r.wait(0.5);
      await r.scrollToEl('.phase-block', 1.8, 110, 1);
      await r.wait(0.5);
      await r.scrollToEl('.phase-block', 1.8, 110, 2);
      await r.wait(0.5);
      await r.scrollTo(await r.page.evaluate(() => scrollY + 800), 1.8);
      await r.wait(0.4);
      await r.stop();
      await r.close();
    },
    async askai(r) {
      await r.open(EM_P1);
      await r.page.evaluate(() => { const c = document.querySelectorAll('.problem-card')[0]; scrollTo(0, c.getBoundingClientRect().top + scrollY - 100); });
      await r.start('askai');
      await r.wait(0.5);
      await r.moveToEl('.ask-ai-bar-btn', 0.8, 0);
      await r.wait(0.6);
      await dragSelect(r, '.problem-card .problem-statement p', 0.95, 1.1);
      await r.wait(0.9);
      await r.click('.ask-ai-pill', { sec: 0.6, after: 1.0 });
      await r.wait(1.4);
      const chip = await r.box('.ask-ai-panel .ask-ai-chip', 1);
      if (chip) { await r.click('.ask-ai-panel .ask-ai-chip', { nth: 1, sec: 0.7, after: 0.8 }); }
      await r.moveToEl('.ask-ai-panel .ask-ai-preview, .ask-ai-panel .ask-ai-prompt', 0.8);
      await r.wait(1.2);
      await r.stop();
      await r.close();
    },
    async palettes(r) {
      await r.open(EM_T3);
      await r.page.evaluate(() => scrollTo(0, 5000));
      await r.start('palettes');
      await r.wait(0.4);
      await r.click('#surfaceButton', { sec: 0.9, after: 0.6 });
      for (const i of [1, 2, 4, 5, 0]) await r.click('.surface-swatch', { nth: i + 1, sec: 0.45, after: 0.85 });
      await r.page.keyboard.press('Escape');
      await r.wait(0.3);
      await r.click('#themeToggle', { sec: 0.6, after: 1.3 });
      await r.stop();
      await r.close();
    },
    async focus(r) {
      await r.open('/index.html');
      await r.page.evaluate(() => scrollTo(0, 260));
      await r.start('focus');
      await r.wait(0.4);
      await r.click('#focusLabButton', { sec: 0.9, after: 0.8 });
      await r.click('.fl-card', { nth: 3, sec: 0.7, after: 0.5 });
      await r.click('.fl-play', { sec: 0.7, after: 2.0 });
      await r.click('.fl-seg__btn', { nth: 1, sec: 0.6, after: 1.8 });
      await r.stop();
      await r.close();
    },
    async timer(r) {
      await r.open('/index.html');
      await r.page.evaluate(() => scrollTo(0, 260));
      await r.start('timer');
      await r.wait(0.3);
      await r.click('#pomodoroButton', { sec: 0.9, after: 0.7 });
      await r.click('.pm-card', { nth: 1, sec: 0.6, after: 0.6 });
      await r.click('.pm-seg__btn', { nth: 1, sec: 0.6, after: 0.6 });
      await r.click('.pm-chip', { nth: 3, sec: 0.6, after: 1.4 });
      await r.scrollTo(400, 1.0, '#pomodoroPanel');
      await r.wait(0.8);
      await r.stop();
      await r.close();
    },
    async sources(r) {
      await r.open(FM_SRC);
      await r.start('sources');
      await r.wait(0.5);
      await r.scrollTo(700, 2.0);
      await r.wait(0.3);
      await r.goto(FM_EX);
      await r.wait(0.5);
      await r.moveToEl('a[href*="SECONDPARTIAL"], .chip, nav a', 0.7, 1);
      await r.scrollTo(900, 2.2);
      await r.wait(0.5);
      await r.stop();
      await r.close();
    },
    async trio(r) {
      await r.open('/index.html');
      await r.start('trio');
      await r.wait(1.0);
      await r.scrollTo(1500, 4.0);
      await r.wait(0.5);
      await r.scrollTo(0, 3.0);
      await r.wait(0.5);
      await r.stop();
      await r.close();
    },
  },
  tablet: {
    async trio(r) {
      await r.open('/index.html');
      await r.start('trio');
      await r.wait(1.0);
      await r.scrollTo(2000, 4.0);
      await r.wait(0.5);
      await r.scrollTo(0, 3.0);
      await r.wait(0.5);
      await r.stop();
      await r.close();
    },
    async materials(r) {
      await r.open(AM_T2);
      await r.page.evaluate(() => scrollTo(0, 5300));
      await r.start('materials');
      await r.wait(0.5);
      await r.scrollTo(6600, 3.0);
      await r.wait(0.4);
      await r.scrollTo(8400, 2.6);
      await r.wait(0.5);
      await r.stop();
      await r.close();
    },
    async askai(r) {
      await r.open(EM_P1);
      await r.page.evaluate(() => { const c = document.querySelectorAll('.problem-card')[1]; scrollTo(0, c.getBoundingClientRect().top + scrollY - 80); });
      await r.start('askai');
      await r.wait(0.6);
      await r.click('.ask-ai-bar-btn', { nth: 4, after: 1.2 });
      await r.wait(1.0);
      await r.click('.ask-ai-panel .ask-ai-chip', { nth: 2, after: 1.2 });
      await r.stop();
      await r.close();
    },
  },
  mobile: {
    async trio(r) {
      await r.open('/index.html');
      await r.start('trio');
      await r.wait(1.0);
      await r.scrollTo(2400, 4.0);
      await r.wait(0.5);
      await r.scrollTo(0, 3.0);
      await r.wait(0.5);
      await r.stop();
      await r.close();
    },
    async problems(r) {
      await r.open(EM_P1);
      await r.page.evaluate(() => { const e = document.querySelector('.solution-summary'); scrollTo(0, e.getBoundingClientRect().top + scrollY - 700); });
      await r.start('problems');
      await r.wait(0.4);
      await r.scrollToEl('.solution-summary', 1.4, 420, 0);
      await r.click('.solution-summary', { nth: 0, after: 0.4 });
      await r.scrollToEl('.phase-block', 1.6, 70, 0);
      await r.wait(0.3);
      await r.scrollToEl('.phase-block', 1.8, 70, 2);
      await r.wait(0.4);
      await r.stop();
      await r.close();
    },
    async timer(r) {
      await r.open('/index.html');
      await r.start('timer');
      await r.wait(0.4);
      await r.click('#pomodoroButton', { after: 0.7 });
      await r.click('.pm-seg__btn', { nth: 1, after: 0.6 });
      await r.click('.pm-chip', { nth: 2, after: 1.4 });
      await r.wait(0.6);
      await r.stop();
      await r.close();
    },
    async theme(r) {
      await r.open(EM_T3);
      await r.page.evaluate(() => scrollTo(0, 4400));
      await r.start('theme');
      await r.wait(0.6);
      await r.click('#themeToggle', { after: 1.4 });
      await r.scrollTo(5200, 2.0);
      await r.wait(0.5);
      await r.stop();
      await r.close();
    },
  },
};

(async () => {
  const [device, ...names] = process.argv.slice(2);
  const list = names.length ? names : Object.keys(CLIPS[device]);
  const b = await launch();
  for (const n of list) {
    const t = Date.now();
    try { await CLIPS[device][n](new Recorder(b, device)); }
    catch (e) { console.log(`  ✗ ${device}-${n}:`, e.message.split('\n')[0]); }
    console.log(`    (${((Date.now() - t) / 1000).toFixed(0)} s)`);
  }
  await b.close();
})();
