import React from 'react';
import { OffthreadVideo, staticFile, useCurrentFrame, interpolate, Easing } from 'remotion';
import { C } from './theme';

// Zoom keyframes, in frames local to the enclosing Sequence. x/y: focus point as a fraction of the screen.
export type ZoomKey = { f: number; z: number; x?: number; y?: number };

const ez = Easing.bezier(0.65, 0, 0.35, 1);

const sampleZoom = (keys: ZoomKey[] | undefined, frame: number) => {
  if (!keys || keys.length === 0) return { z: 1, x: 0.5, y: 0.5 };
  const k = keys.map((q) => ({ f: q.f, z: q.z, x: q.x ?? 0.5, y: q.y ?? 0.5 }));
  if (frame <= k[0].f) return k[0];
  for (let i = 0; i < k.length - 1; i++) {
    const a = k[i], b = k[i + 1];
    if (frame <= b.f) {
      const t = ez((frame - a.f) / Math.max(1, b.f - a.f));
      return { z: a.z + (b.z - a.z) * t, x: a.x + (b.x - a.x) * t, y: a.y + (b.y - a.y) * t };
    }
  }
  return k[k.length - 1];
};

export const Screen: React.FC<{
  clip: string;
  w: number;
  h: number;
  startFrom?: number;
  rate?: number;
  zoom?: ZoomKey[];
  radius?: number;
}> = ({ clip, w, h, startFrom = 0, rate = 1, zoom, radius = 0 }) => {
  const frame = useCurrentFrame();
  const { z, x, y } = sampleZoom(zoom, frame);
  // keep the focus point centred, but never reveal the edge of the recording
  const maxX = ((z - 1) * w) / 2, maxY = ((z - 1) * h) / 2;
  const tx = Math.max(-maxX, Math.min(maxX, -(x - 0.5) * w * z));
  const ty = Math.max(-maxY, Math.min(maxY, -(y - 0.5) * h * z));
  return (
    <div style={{ width: w, height: h, overflow: 'hidden', borderRadius: radius, position: 'relative', background: '#000' }}>
      <div style={{ width: w, height: h, transform: `translate(${tx}px, ${ty}px) scale(${z})`, transformOrigin: '50% 50%' }}>
        <OffthreadVideo src={staticFile(`clips/${clip}.mp4`)} startFrom={startFrom} playbackRate={rate} muted style={{ width: w, height: h, display: 'block' }} />
      </div>
      {/* glass reflection */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: 'linear-gradient(115deg, rgba(255,255,255,0.07) 0%, rgba(255,255,255,0.02) 28%, transparent 42%)',
          pointerEvents: 'none',
        }}
      />
    </div>
  );
};

type DevProps = { clip: string; width: number; startFrom?: number; rate?: number; zoom?: ZoomKey[]; glow?: string };

const glowShadow = (glow = C.blue) => `0 40px 90px rgba(0,0,0,0.65), 0 0 0 1px rgba(255,255,255,0.08), 0 0 120px ${glow}33`;

export const Monitor: React.FC<DevProps> = ({ clip, width, startFrom, rate, zoom, glow }) => {
  const bezel = Math.round(width * 0.012);
  const sw = width - bezel * 2;
  const sh = Math.round((sw * 9) / 16);
  return (
    <div style={{ width, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <div
        style={{
          padding: bezel,
          paddingBottom: bezel * 1.6,
          borderRadius: bezel * 1.4,
          background: 'linear-gradient(180deg, #1c2130 0%, #0c0f17 100%)',
          boxShadow: glowShadow(glow),
          position: 'relative',
        }}
      >
        <Screen clip={clip} w={sw} h={sh} startFrom={startFrom} rate={rate} zoom={zoom} radius={4} />
        <div style={{ position: 'absolute', bottom: bezel * 0.45, left: '50%', width: 6, height: 6, marginLeft: -3, borderRadius: 3, background: '#2c3346' }} />
      </div>
      <div style={{ width: width * 0.11, height: width * 0.07, background: 'linear-gradient(90deg, #121620, #2a3142 50%, #121620)', clipPath: 'polygon(18% 0, 82% 0, 100% 100%, 0 100%)' }} />
      <div style={{ width: width * 0.3, height: Math.max(6, width * 0.008), borderRadius: 8, background: 'linear-gradient(90deg, #121620, #343c50 50%, #121620)', boxShadow: '0 18px 40px rgba(0,0,0,0.6)' }} />
    </div>
  );
};

export const Tablet: React.FC<DevProps> = ({ clip, width, startFrom, rate, zoom, glow }) => {
  const bezel = Math.round(width * 0.04);
  const sw = width - bezel * 2;
  const sh = Math.round((sw * 1180) / 820);
  return (
    <div
      style={{
        padding: bezel,
        borderRadius: bezel * 2.2,
        background: 'linear-gradient(145deg, #2a3040 0%, #0d1018 60%, #1b2030 100%)',
        boxShadow: glowShadow(glow ?? C.violet),
        position: 'relative',
        width,
      }}
    >
      <Screen clip={clip} w={sw} h={sh} startFrom={startFrom} rate={rate} zoom={zoom} radius={bezel * 0.9} />
      <div style={{ position: 'absolute', top: bezel / 2 - 3, left: '50%', width: 6, height: 6, marginLeft: -3, borderRadius: 3, background: '#323a4e' }} />
    </div>
  );
};

export const Phone: React.FC<DevProps> = ({ clip, width, startFrom, rate, zoom, glow }) => {
  const bezel = Math.round(width * 0.035);
  const sw = width - bezel * 2;
  const sh = Math.round((sw * 844) / 390);
  return (
    <div
      style={{
        padding: bezel,
        borderRadius: width * 0.17,
        background: 'linear-gradient(145deg, #3a4256 0%, #0b0e15 45%, #262c3c 100%)',
        boxShadow: glowShadow(glow ?? C.cyan),
        position: 'relative',
        width,
      }}
    >
      <Screen clip={clip} w={sw} h={sh} startFrom={startFrom} rate={rate} zoom={zoom} radius={width * 0.14} />
      <div
        style={{
          position: 'absolute',
          top: bezel + sw * 0.03,
          left: '50%',
          width: sw * 0.3,
          height: sw * 0.085,
          marginLeft: -sw * 0.15,
          borderRadius: sw,
          background: '#000',
        }}
      />
    </div>
  );
};

// Spring-in wrapper for devices: rise + slight 3D tilt settling to flat.
export const useEnter = (delay = 0, dur = 50) => {
  const f = useCurrentFrame();
  const t = interpolate(f - delay, [0, dur], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.bezier(0.16, 1, 0.3, 1) });
  return t;
};
