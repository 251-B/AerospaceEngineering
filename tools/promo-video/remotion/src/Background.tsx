import React, { useMemo } from 'react';
import { AbsoluteFill, random, useCurrentFrame, interpolate } from 'remotion';
import { C, W, H } from './theme';

const STARS = 420;

export const SpaceBackground: React.FC = () => {
  const f = useCurrentFrame();
  const stars = useMemo(
    () =>
      new Array(STARS).fill(0).map((_, i) => ({
        x: random(`x${i}`) * W,
        y: random(`y${i}`) * H,
        z: 0.2 + random(`z${i}`) * 0.8, // depth: parallax + size
        tw: random(`t${i}`) * Math.PI * 2,
        hue: random(`h${i}`),
      })),
    [],
  );

  return (
    <AbsoluteFill style={{ background: `radial-gradient(ellipse 120% 90% at 50% 40%, ${C.bg1} 0%, ${C.bg0} 70%)`, overflow: 'hidden' }}>
      {/* nebula glows drifting slowly */}
      {[
        { x: 0.18, y: 0.25, r: 900, c: 'rgba(79,124,255,0.20)', s: 0.7 },
        { x: 0.85, y: 0.75, r: 1000, c: 'rgba(155,107,255,0.17)', s: 0.5 },
        { x: 0.6, y: 0.1, r: 700, c: 'rgba(56,214,255,0.10)', s: 0.9 },
      ].map((n, i) => (
        <div
          key={i}
          style={{
            position: 'absolute',
            left: n.x * W - n.r / 2 + Math.sin(f / 300 + i) * 60 * n.s,
            top: n.y * H - n.r / 2 + Math.cos(f / 360 + i * 2) * 40 * n.s,
            width: n.r,
            height: n.r,
            borderRadius: '50%',
            background: `radial-gradient(circle, ${n.c} 0%, transparent 65%)`,
          }}
        />
      ))}

      <svg width={W} height={H} style={{ position: 'absolute', inset: 0 }}>
        {stars.map((s, i) => {
          const x = (((s.x - f * 0.35 * s.z) % W) + W) % W;
          const tw = 0.55 + 0.45 * Math.sin(f / 22 + s.tw);
          const r = 0.5 + s.z * 1.5;
          const fill = s.hue > 0.92 ? '#ffd8a8' : s.hue > 0.82 ? '#a8d8ff' : '#ffffff';
          return <circle key={i} cx={x} cy={s.y} r={r} fill={fill} opacity={(0.25 + 0.75 * s.z) * tw} />;
        })}
      </svg>

      {/* orbital rings */}
      <svg width={W} height={H} style={{ position: 'absolute', inset: 0, opacity: 0.55 }}>
        <defs>
          <linearGradient id="ring" x1="0" x2="1">
            <stop offset="0" stopColor={C.cyan} stopOpacity="0" />
            <stop offset="0.5" stopColor={C.cyan} stopOpacity="0.35" />
            <stop offset="1" stopColor={C.violet} stopOpacity="0" />
          </linearGradient>
        </defs>
        {[0, 1, 2].map((i) => (
          <g key={i} transform={`translate(${W * 0.5} ${H * 1.05}) rotate(${-8 + i * 6 + f * 0.01 * (i + 1)})`}>
            <ellipse rx={1100 + i * 260} ry={260 + i * 70} fill="none" stroke="url(#ring)" strokeWidth={1.2} />
            <circle
              cx={(1100 + i * 260) * Math.cos(f / (260 + i * 90) + i)}
              cy={(260 + i * 70) * Math.sin(f / (260 + i * 90) + i)}
              r={3}
              fill={i === 1 ? C.violet : C.cyan}
              opacity={0.9}
            />
          </g>
        ))}
      </svg>

      {/* fine HUD grid with vignette */}
      <AbsoluteFill
        style={{
          backgroundImage: `linear-gradient(${C.line} 1px, transparent 1px), linear-gradient(90deg, ${C.line} 1px, transparent 1px)`,
          backgroundSize: '120px 120px',
          backgroundPosition: `${-f * 0.2}px 0px`,
          opacity: 0.18,
          maskImage: 'radial-gradient(ellipse 70% 60% at 50% 50%, black 10%, transparent 75%)',
          WebkitMaskImage: 'radial-gradient(ellipse 70% 60% at 50% 50%, black 10%, transparent 75%)',
        }}
      />
      <AbsoluteFill style={{ background: 'radial-gradient(ellipse 85% 80% at 50% 50%, transparent 55%, rgba(0,0,0,0.65) 100%)' }} />
      <AbsoluteFill style={{ opacity: interpolate(f, [0, 30], [1, 0], { extrapolateRight: 'clamp' }), background: '#000' }} />
    </AbsoluteFill>
  );
};
