import React from 'react';
import { spring, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { C, GRAD, grotesk, mono } from './theme';

export const useSpring = (delay = 0, config = { damping: 16, stiffness: 120, mass: 0.9 }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  return spring({ frame: f - delay, fps, config });
};

export const Kicker: React.FC<{ n?: string; children: React.ReactNode; delay?: number; color?: string }> = ({ n, children, delay = 0, color = C.cyan }) => {
  const s = useSpring(delay);
  const f = useCurrentFrame();
  const lineW = interpolate(f - delay, [0, 30], [0, 56], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 16, opacity: s, transform: `translateX(${(1 - s) * -30}px)`, fontFamily: mono, fontSize: 21, letterSpacing: 4, color, textTransform: 'uppercase' }}>
      {n && <span style={{ color: C.text, opacity: 0.55 }}>{n}</span>}
      <span style={{ width: lineW, height: 2, background: color, display: 'inline-block' }} />
      <span>{children}</span>
    </div>
  );
};

// Words spring up one after another. Wrap a word in *asterisks* to paint it with the gradient.
export const Headline: React.FC<{ text: string; delay?: number; size?: number; stagger?: number; align?: 'left' | 'center'; font?: string }> = ({
  text,
  delay = 0,
  size = 76,
  stagger = 4,
  align = 'left',
  font = grotesk,
}) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const lines = text.split('\n');
  let wi = 0;
  let inHl = false;
  return (
    <div style={{ fontFamily: font, fontWeight: 700, fontSize: size, lineHeight: 1.06, letterSpacing: -1.5, color: C.text, textAlign: align }}>
      {lines.map((line, li) => (
        <div key={li} style={{ display: 'flex', flexWrap: 'wrap', gap: `0 ${size * 0.26}px`, justifyContent: align === 'center' ? 'center' : 'flex-start' }}>
          {line.split(' ').map((w, i) => {
            const d = delay + wi++ * stagger;
            const s = spring({ frame: f - d, fps, config: { damping: 14, stiffness: 140, mass: 0.8 } });
            if (w.startsWith('*')) inHl = true;
            const hl = inHl;
            if (w.endsWith('*') || w.endsWith('*.')) inHl = false;
            const word = w.replace(/\*/g, '');
            return (
              <span key={i} style={{ display: 'inline-block', overflow: 'hidden', paddingBottom: size * 0.12, marginBottom: -size * 0.12 }}>
                <span
                  style={{
                    display: 'inline-block',
                    transform: `translateY(${(1 - s) * 105}%) rotate(${(1 - s) * 4}deg)`,
                    opacity: Math.min(1, s * 1.4),
                    ...(hl ? { backgroundImage: GRAD, WebkitBackgroundClip: 'text', backgroundClip: 'text', color: 'transparent' } : {}),
                  }}
                >
                  {word}
                </span>
              </span>
            );
          })}
        </div>
      ))}
    </div>
  );
};

export const Body: React.FC<{ children: React.ReactNode; delay?: number; size?: number; width?: number }> = ({ children, delay = 0, size = 28, width = 640 }) => {
  const s = useSpring(delay);
  return (
    <div style={{ fontFamily: grotesk, fontSize: size, lineHeight: 1.45, color: C.dim, maxWidth: width, opacity: s, transform: `translateY(${(1 - s) * 24}px)`, filter: `blur(${(1 - s) * 6}px)` }}>
      {children}
    </div>
  );
};

export const Bullets: React.FC<{ items: { icon?: string; text: string; color?: string }[]; delay?: number; stagger?: number }> = ({ items, delay = 0, stagger = 10 }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
      {items.map((it, i) => {
        const s = spring({ frame: f - delay - i * stagger, fps, config: { damping: 15, stiffness: 130 } });
        const col = it.color ?? C.cyan;
        return (
          <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 18, opacity: s, transform: `translateX(${(1 - s) * -40}px)` }}>
            <div
              style={{
                width: 46,
                height: 46,
                borderRadius: 12,
                display: 'grid',
                placeItems: 'center',
                background: `${col}1f`,
                border: `1px solid ${col}66`,
                color: col,
                fontFamily: mono,
                fontSize: 20,
                fontWeight: 600,
                flex: 'none',
                transform: `scale(${0.6 + 0.4 * s})`,
              }}
            >
              {it.icon ?? '✓'}
            </div>
            <div style={{ fontFamily: grotesk, fontSize: 27, color: C.text, fontWeight: 500 }}>{it.text}</div>
          </div>
        );
      })}
    </div>
  );
};

export const Chip: React.FC<{ children: React.ReactNode; color?: string; delay?: number }> = ({ children, color = C.cyan, delay = 0 }) => {
  const s = useSpring(delay, { damping: 12, stiffness: 160, mass: 0.7 });
  return (
    <span
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: 10,
        padding: '10px 20px',
        borderRadius: 999,
        border: `1px solid ${color}88`,
        background: `${color}18`,
        color,
        fontFamily: mono,
        fontSize: 20,
        letterSpacing: 1,
        transform: `scale(${s})`,
        opacity: s,
        boxShadow: `0 0 24px ${color}33`,
      }}
    >
      {children}
    </span>
  );
};

export const Counter: React.FC<{ to: number; label: string; color: string; delay?: number }> = ({ to, label, color, delay = 0 }) => {
  const f = useCurrentFrame();
  const t = interpolate(f - delay, [0, 70], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const eased = 1 - Math.pow(1 - t, 3);
  const s = useSpring(delay);
  return (
    <div style={{ opacity: s, transform: `translateY(${(1 - s) * 30}px)` }}>
      <div style={{ fontFamily: mono, fontWeight: 600, fontSize: 68, color, textShadow: `0 0 30px ${color}66` }}>{Math.round(to * eased)}</div>
      <div style={{ fontFamily: mono, fontSize: 17, letterSpacing: 3, color: C.dim, textTransform: 'uppercase', marginTop: 4 }}>{label}</div>
    </div>
  );
};
