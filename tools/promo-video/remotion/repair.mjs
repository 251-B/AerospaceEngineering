// Re-render individual frames of an image-sequence render, reusing one browser.
// usage: node repair.mjs <framesDir> <frame> [frame ...]
import { openBrowser, renderStill, selectComposition } from '@remotion/renderer';
import fs from 'node:fs';
import path from 'node:path';

const [dir, ...frames] = process.argv.slice(2);
const serveUrl = path.resolve('build');
const browserExecutable = process.env.REMOTION_BROWSER || null;
const chromiumOptions = { gl: 'angle' };

const files = fs.readdirSync(dir).filter((f) => f.endsWith('.jpeg')).sort();
const pad = files[0].match(/(\d+)\.jpeg$/)[1].length;
const prefix = files[0].replace(/\d+\.jpeg$/, '');

const browser = await openBrowser('chrome', { browserExecutable, chromiumOptions });
const composition = await selectComposition({ serveUrl, id: 'Promo', puppeteerInstance: browser, browserExecutable, chromiumOptions });
for (const f of frames.map(Number)) {
  const output = path.join(dir, `${prefix}${String(f).padStart(pad, '0')}.jpeg`);
  await renderStill({ composition, serveUrl, frame: f, output, imageFormat: 'jpeg', jpegQuality: 95, overwrite: true, puppeteerInstance: browser, browserExecutable, chromiumOptions });
  process.stdout.write(`${f} `);
}
await browser.close({ silent: true });
console.log('\nrepaired', frames.length);
