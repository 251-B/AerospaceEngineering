// Renders tools/account_art/galaxy.html (written by galaxy.py) to a PNG with a transparent
// background. Usage, from the repository root:
//   python tools/account_art/galaxy.py
//   node tools/account_art/render.js tools/account_art/galaxy.html galaxy.png 0.85
//   python -c "from PIL import Image; Image.open('galaxy.png').save('assets/img/sky/account-galaxy.webp', 'WEBP', quality=74, method=6)"
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [src, out, scale] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1200 }, deviceScaleFactor: Number(scale || 0.85) });
  await p.goto('file://' + path.resolve(src));
  await p.waitForTimeout(800);
  await p.screenshot({ path: out, omitBackground: true });
  await b.close();
})();
