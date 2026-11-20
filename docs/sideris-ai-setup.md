# Sideris Instant AI Setup (Cloudflare Worker)

This guide covers the Cloudflare Worker that powers **Sideris Lux**, **Sideris Aether**,
**Sideris Orion** and **Sideris Titan** with **0 MB download** inside every study page (desktop and
mobile), grounded in the portal's `vault/` RAG shards.

- **Cloud inference:** the Worker runs every profile on Cloudflare Workers AI (`[ai] binding = "AI"`
  in `tools/cloudflare/wrangler.sideris.toml`); each profile tries its models in order
  (`PROFILE_DEFAULTS` in `tools/cloudflare/sideris-worker.js`). No other provider is used.
- **Answer length:** Orion and Titan are reasoning models and get up to 6144 tokens
  (`maxTokensCap` in the worker, `maxTokens` in `assets/data/ai-models.js`); Lux and Aether keep 2048.
- **Daily allowance per student:** each question costs points by model (Lux 1, Aether 2, Orion and
  Titan 5); a student gets 40 a day, an IP 400 (campus wifi), and an optional cap for the whole portal
  (`PORTAL_DAILY_POINTS`). Counters live in the `SiderisQuota` Durable Object (SQLite, created by the
  deploy) and reset at 00:00 UTC; the student is an anonymous id kept in their browser
  (`ae_sideris_client`). Change the numbers with the commented `[vars]` of the wrangler config.
- **Cloud only:** every model answers from the Worker; nothing is downloaded to the device. Models
  used to install themselves on computers (Transformers.js + WebGPU); that was dropped on 2026-11-20
  because integrated GPUs took tens of seconds to read a question, browsers evicted the 1.3-2.5 GB
  files and few devices could run the mid-size models. `AESiderisEngine.cleanupLocal()` removes the
  old files (`sideris-models`, `transformers-cache`) and keys (`ae_sideris_local`, `ae_sideris_files`).
- **Nothing to set up for students:** no run mode, no model links or keys.

---

## 1. Deploy the Worker to your Cloudflare account

From the repository root:

```bash
npx wrangler login
npx wrangler deploy --config tools/cloudflare/wrangler.sideris.toml
```

Wrangler prints your public Worker URL, e.g.:
`https://sideris-ai.<your-subdomain>.workers.dev`

Test the health endpoint in your browser:
`https://sideris-ai.<your-subdomain>.workers.dev/health`
You should see `{"ok":true,"providers":["cloudflare-ai"],...}`.

---

## 2. Connect the portal

Edit `assets/data/sideris-config.js` and paste your public Worker URL:

```js
window.AE_SIDERIS_CONFIG = window.AE_SIDERIS_CONFIG || {
  workerUrl: 'https://sideris-ai.<your-subdomain>.workers.dev'
};
```

Commit and push. Every student now gets instant Sideris answers with zero downloads.
