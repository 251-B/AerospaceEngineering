import React from 'react';
import { AbsoluteFill, Audio, staticFile, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { TransitionSeries, linearTiming, TransitionPresentation, TransitionPresentationComponentProps } from '@remotion/transitions';
import { slide } from '@remotion/transitions/slide';
import { SpaceBackground } from './Background';
import { C, mono } from './theme';
import timing from './scenes.json';
import { Intro, HubScene, SearchScene, TheoryScene, ProblemsScene, AskAIScene, PaletteScene, FocusScene, TimerScene, SourcesScene, TrioScene, Outro } from './Scenes';

// Custom CSS transition: the outgoing scene flies past the camera, the incoming one resolves out of blur.
type WarpProps = Record<string, never>;
const Warp: React.FC<TransitionPresentationComponentProps<WarpProps>> = ({ children, presentationDirection, presentationProgress: p }) => {
  const entering = presentationDirection === 'entering';
  const scale = entering ? 0.9 + 0.1 * p : 1 + 0.18 * p;
  const blur = entering ? (1 - p) * 14 : p * 14;
  const opacity = entering ? p : 1 - p;
  return <AbsoluteFill style={{ transform: `scale(${scale})`, filter: `blur(${blur}px)`, opacity }}>{children}</AbsoluteFill>;
};
const warp = (): TransitionPresentation<WarpProps> => ({ component: Warp, props: {} });

const T = timing.transition; // transition length (frames)
export const SCENES: { c: React.FC; d: number; name: string }[] = [
  { c: Intro, d: timing.durations[0], name: 'Intro' },
  { c: HubScene, d: timing.durations[1], name: 'Study hub' },
  { c: SearchScene, d: timing.durations[2], name: 'Search' },
  { c: TheoryScene, d: timing.durations[3], name: 'Theory' },
  { c: ProblemsScene, d: timing.durations[4], name: 'Solved problems' },
  { c: AskAIScene, d: timing.durations[5], name: 'Ask AI' },
  { c: PaletteScene, d: timing.durations[6], name: 'Reading palettes' },
  { c: FocusScene, d: timing.durations[7], name: 'Focus Lab' },
  { c: TimerScene, d: timing.durations[8], name: 'Study timer' },
  { c: SourcesScene, d: timing.durations[9], name: 'Official material' },
  { c: TrioScene, d: timing.durations[10], name: 'Responsive' },
  { c: Outro, d: timing.durations[11], name: 'Outro' },
];
export const TOTAL = SCENES.reduce((a, s) => a + s.d, 0) - T * (SCENES.length - 1);

const presentations = [warp(), slide({ direction: 'from-right' }), warp(), slide({ direction: 'from-bottom' }), warp(), slide({ direction: 'from-left' }), warp(), slide({ direction: 'from-right' }), warp(), warp(), warp()];

const Hud: React.FC = () => {
  const f = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  let acc = 0, idx = 0;
  for (let i = 0; i < SCENES.length; i++) { if (f >= acc - T / 2) idx = i; acc += SCENES[i].d - T; }
  const show = interpolate(f, [260, 320, durationInFrames - 400, durationInFrames - 340], [0, 1, 1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const prog = f / durationInFrames;
  return (
    <AbsoluteFill style={{ pointerEvents: 'none', opacity: show }}>
      <div style={{ position: 'absolute', top: 38, left: 80, fontFamily: mono, fontSize: 16, letterSpacing: 3, color: C.dim }}>
        <span style={{ color: C.cyan }}>●</span>&nbsp; AEROSPACE ENGINEERING · STUDY PORTAL
      </div>
      <div style={{ position: 'absolute', top: 38, right: 80, fontFamily: mono, fontSize: 16, letterSpacing: 3, color: C.dim, textTransform: 'uppercase' }}>
        {SCENES[idx].name}
      </div>
      <div style={{ position: 'absolute', left: 80, right: 80, bottom: 30, height: 2, background: 'rgba(255,255,255,0.08)', borderRadius: 2 }}>
        <div style={{ width: `${prog * 100}%`, height: '100%', background: `linear-gradient(90deg, ${C.cyan}, ${C.violet})`, boxShadow: `0 0 12px ${C.cyan}` }} />
      </div>
    </AbsoluteFill>
  );
};

export const Promo: React.FC = () => (
  <AbsoluteFill style={{ background: C.bg0 }}>
    <SpaceBackground />
    <TransitionSeries>
      {SCENES.flatMap((s, i) => {
        const Comp = s.c;
        const items = [
          <TransitionSeries.Sequence key={`s${i}`} durationInFrames={s.d}>
            <Comp />
          </TransitionSeries.Sequence>,
        ];
        if (i < SCENES.length - 1)
          items.push(<TransitionSeries.Transition key={`t${i}`} presentation={presentations[i] as TransitionPresentation<any>} timing={linearTiming({ durationInFrames: T })} />);
        return items;
      })}
    </TransitionSeries>
    <Hud />
    <Audio src={staticFile('soundtrack.wav')} volume={(f) => interpolate(f, [0, 20], [0, 1], { extrapolateRight: 'clamp' })} />
  </AbsoluteFill>
);
