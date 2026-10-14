import { continueRender, delayRender, staticFile } from 'remotion';

// Fonts are bundled locally (public/fonts): the render browser cannot reach Google Fonts directly.
const FACES: [string, string, string, string][] = [
  ['PromoGrotesk', 'grotesk-400', '400', 'normal'],
  ['PromoGrotesk', 'grotesk-500', '500', 'normal'],
  ['PromoGrotesk', 'grotesk-700', '700', 'normal'],
  ['PromoMono', 'mono-400', '400', 'normal'],
  ['PromoMono', 'mono-600', '600', 'normal'],
  ['PromoDisplay', 'abril', '400', 'normal'],
  ['PromoSerif', 'news-italic', '400', 'italic'],
];
if (typeof document !== 'undefined') {
  const handle = delayRender('fonts');
  Promise.all(
    FACES.map(([family, file, weight, style]) => {
      const face = new FontFace(family, `url(${staticFile(`fonts/${file}.woff2`)}) format('woff2')`, { weight, style });
      return face.load().then((f) => document.fonts.add(f));
    }),
  ).then(() => continueRender(handle));
}

export const grotesk = 'PromoGrotesk, sans-serif';
export const mono = 'PromoMono, monospace';
export const display = 'PromoDisplay, serif';
export const serif = 'PromoSerif, serif';

export const FPS = 60;
export const W = 1920;
export const H = 1080;

export const C = {
  bg0: '#03050c',
  bg1: '#0a1030',
  text: '#eef3ff',
  dim: '#9aa8c7',
  cyan: '#38d6ff',
  blue: '#4f7cff',
  violet: '#9b6bff',
  amber: '#ffb547',
  green: '#3ee6a8',
  line: 'rgba(160,190,255,0.16)',
};

export const GRAD = `linear-gradient(100deg, ${C.cyan} 0%, ${C.blue} 45%, ${C.violet} 100%)`;
