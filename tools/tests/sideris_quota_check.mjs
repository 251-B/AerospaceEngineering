// Daily allowance of tools/cloudflare/sideris-worker.js (SiderisQuota), with an in-memory Durable Object.
// Run by test_sideris_quota.py; exits non-zero on the first failed assert.
import worker, { SiderisQuota } from './worker.mjs';  // copied there by test_sideris_quota.py
import assert from 'node:assert';
function makeNs() {
  const objs = new Map();
  return { objs, idFromName: (n) => n, get: (id) => {
    if (!objs.has(id)) { const mem = new Map(); objs.set(id, new SiderisQuota({ storage: { get: async (k) => mem.get(k), put: async (k, v) => { mem.set(k, v); } } })); }
    const o = objs.get(id); return { fetch: (url, init) => o.fetch(new Request(url, init)) };
  } };
}
const AI = { run: async () => ({ response: 'ok' }) };
async function ask(env, profile, client, ip = '9.9.9.9') {
  const h = { 'Content-Type': 'application/json', Origin: 'https://251-b.github.io', 'CF-Connecting-IP': ip };

  const res = await worker.fetch(new Request('https://x/v1/chat/completions', { method: 'POST', headers: h,
    body: JSON.stringify({ profile, client, stream: false, messages: [{ role: 'user', content: 'hi' }] }) }), env, {});
  return { status: res.status, remaining: res.headers.get('X-Sideris-Remaining'), body: await res.json() };
}
// 1. student: 40 points = 20 Aether questions, then blocked; another student still fine
let env = { AI, QUOTA: makeNs() };
let r; for (let i = 0; i < 20; i++) { r = await ask(env, 'sideris-aether', 'student-aaaaaaaa', '1.1.1.' + i); assert.equal(r.status, 200); }
assert.equal(r.remaining, '0');
r = await ask(env, 'sideris-lux', 'student-aaaaaaaa', '1.1.1.99'); assert.equal(r.status, 429); assert.equal(r.body.limit, 'student');
r = await ask(env, 'sideris-titan', 'student-bbbbbbbb', '1.1.1.98'); assert.equal(r.status, 200); assert.equal(r.remaining, '35');
console.log('student limit ok');
// 2. IP cap: refused at the IP counter gives the student their points back
env = { AI, QUOTA: makeNs(), IP_DAILY_POINTS: '4' };
assert.equal((await ask(env, 'sideris-aether', 'student-cccccccc', '5.5.5.5')).status, 200);
assert.equal((await ask(env, 'sideris-aether', 'student-dddddddd', '5.5.5.5')).status, 200);
r = await ask(env, 'sideris-aether', 'student-eeeeeeee', '5.5.5.5'); assert.equal(r.status, 429); assert.equal(r.body.limit, 'ip');
r = await ask(env, 'sideris-aether', 'student-eeeeeeee', '6.6.6.6'); assert.equal(r.remaining, '38', 'refund after IP refusal');
console.log('ip cap + refund ok');
// 3. portal cap
env = { AI, QUOTA: makeNs(), PORTAL_DAILY_POINTS: '3' };
assert.equal((await ask(env, 'sideris-aether', 'student-ffffffff', '7.7.7.1')).status, 200);
r = await ask(env, 'sideris-aether', 'student-gggggggg', '7.7.7.2'); assert.equal(r.status, 429); assert.equal(r.body.limit, 'portal');
console.log('portal cap ok');
// 4. no client id -> counted by IP as the student; bad id ignored
env = { AI, QUOTA: makeNs() };
await ask(env, 'sideris-aether', null, '8.8.8.8'); await ask(env, 'sideris-aether', 'bad id!', '8.8.8.8');
assert.ok(env.QUOTA.objs.has('student-ip:8.8.8.8')); assert.equal([...env.QUOTA.objs.keys()].filter(k => k.startsWith('student:')).length, 0);
console.log('fallback id ok');
// 5. next day resets; no binding / broken counter keep Sideris up
env = { AI, QUOTA: makeNs() };
for (let i = 0; i < 20; i++) await ask(env, 'sideris-aether', 'student-hhhhhhhh', '2.2.2.' + i);
assert.equal((await ask(env, 'sideris-aether', 'student-hhhhhhhh', '2.2.3.1')).status, 429);
const RealDate = Date; globalThis.Date = class extends RealDate { constructor(...a) { super(...(a.length ? a : [RealDate.now() + 86400000])); } };
assert.equal((await ask(env, 'sideris-aether', 'student-hhhhhhhh', '2.2.3.2')).status, 200); globalThis.Date = RealDate;
assert.equal((await ask({ AI }, 'sideris-titan', 'student-iiiiiiii')).status, 200);
assert.equal((await ask({ AI, QUOTA: { idFromName: (n) => n, get: () => ({ fetch: async () => { throw new Error('boom'); } }) } }, 'sideris-titan', 'student-jjjjjjjj')).status, 200);
console.log('day reset + fail-open ok');
