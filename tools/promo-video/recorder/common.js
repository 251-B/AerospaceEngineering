const path = require('path');
const fs = require('fs');
const KATEX = path.join(__dirname, 'node_modules/katex/dist');
async function routeCdn(ctx) {
  await ctx.route(/cdn\.jsdelivr\.net\/npm\/katex@[^/]+\/dist\/(.*)$/, (route) => {
    const rel = route.request().url().match(/dist\/(.*)$/)[1].split('?')[0];
    const f = path.join(KATEX, rel);
    if (!fs.existsSync(f)) return route.fulfill({ status: 404, body: '' });
    const type = f.endsWith('.js') ? 'application/javascript' : f.endsWith('.css') ? 'text/css' : f.endsWith('.woff2') ? 'font/woff2' : f.endsWith('.woff') ? 'font/woff' : 'font/ttf';
    route.fulfill({ status: 200, contentType: type, body: fs.readFileSync(f) });
  });
}
module.exports = { routeCdn, BASE: 'http://localhost:8765' };
