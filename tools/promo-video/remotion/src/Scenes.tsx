import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame, Easing, Sequence, useVideoConfig, spring } from 'remotion';
import { C, GRAD, display, grotesk, mono, serif } from './theme';
import { Kicker, Headline, Body, Bullets, Chip, Counter, useSpring } from './Text';
import { Monitor, Tablet, Phone, ZoomKey } from './Devices';
import clips from './clips.json';

type ClipName = keyof typeof clips;
// Fit a clip of N frames into `frames` of screen time (mild speed-up or slow-down).
export const fit = (clip: ClipName, frames: number, startFrom = 0) => Math.max(0.8, Math.min(1.6, (clips[clip] - startFrom) / frames));

const clamp = { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' } as const;
const outExpo = Easing.bezier(0.16, 1, 0.3, 1);

// ---------- Logo mark (matches the portal's orbit icon) ----------
export const LogoMark: React.FC<{ size: number; delay?: number }> = ({ size, delay = 0 }) => {
  const f = useCurrentFrame();
  const s = useSpring(delay, { damping: 11, stiffness: 110, mass: 0.9 });
  return (
    <div
      style={{
        width: size,
        height: size,
        borderRadius: size * 0.26,
        background: `linear-gradient(135deg, ${C.cyan}, ${C.blue} 55%, ${C.violet})`,
        display: 'grid',
        placeItems: 'center',
        transform: `scale(${s}) rotate(${(1 - s) * -40}deg)`,
        boxShadow: `0 0 ${size * 0.6}px ${C.blue}88, inset 0 1px 0 rgba(255,255,255,0.4)`,
      }}
    >
      <svg width={size * 0.62} height={size * 0.62} viewBox="0 0 24 24">
        <ellipse cx="12" cy="12" rx="10" ry="4.2" fill="none" stroke="#fff" strokeWidth="2" transform={`rotate(${-30 + f * 0.4} 12 12)`} />
        <circle cx="12" cy="12" r="3.4" fill="#fff" />
      </svg>
    </div>
  );
};

// ---------- Intro ----------
export const Intro: React.FC = () => {
  const f = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const ring = (i: number) => interpolate(f, [10 + i * 8, 90 + i * 8], [0, 1], { ...clamp, easing: outExpo });
  const sweep = interpolate(f, [70, 190], [0, 100], { ...clamp, easing: Easing.inOut(Easing.cubic) });
  const push = interpolate(f, [0, durationInFrames], [1, 1.06]);
  const titleS = useSpring(34, { damping: 18, stiffness: 90, mass: 1 });
  return (
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center', transform: `scale(${push})` }}>
      <svg width={1920} height={1080} style={{ position: 'absolute', inset: 0 }}>
        {[0, 1, 2, 3].map((i) => {
          const r = 180 + i * 120;
          const c = 2 * Math.PI * r;
          return (
            <g key={i} transform={`translate(960 470) rotate(${f * (0.15 + i * 0.05) * (i % 2 ? -1 : 1)}) scale(1 0.34)`}>
              <circle r={r} fill="none" stroke={i % 2 ? C.violet : C.cyan} strokeOpacity={0.35 - i * 0.05} strokeWidth={2} strokeDasharray={c} strokeDashoffset={c * (1 - ring(i))} />
              <circle cx={r} cy={0} r={6} fill={i % 2 ? C.violet : C.cyan} opacity={ring(i)} />
            </g>
          );
        })}
      </svg>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 34, marginTop: -40 }}>
        <LogoMark size={128} delay={6} />
        <Kicker delay={22}>UC3M · BSc Aerospace Engineering · 2nd Year</Kicker>
        <div
          style={{
            fontFamily: display,
            fontSize: 140,
            lineHeight: 1.1,
            padding: '0 20px 10px',
            color: 'transparent',
            backgroundImage: 'linear-gradient(100deg, #dfe7ff 0%, #c8d6ff 35%, #ffffff 45%, #9fd8ff 50%, #ffffff 55%, #c8d6ff 65%, #dfe7ff 100%)',
            backgroundSize: '300% 100%',
            backgroundPosition: `${100 - sweep}% 0`,
            WebkitBackgroundClip: 'text',
            backgroundClip: 'text',
            transform: `translateY(${(1 - titleS) * 80}px) scale(${0.9 + 0.1 * titleS})`,
            opacity: titleS,
            letterSpacing: 1,
          }}
        >
          Aerospace Engineering
        </div>
        <Headline text="The *study portal* for the second year" size={52} delay={60} align="center" stagger={5} />
      </div>
    </AbsoluteFill>
  );
};

// ---------- Generic feature layout ----------
type Side = 'left' | 'right';
export const FeatureLayout: React.FC<{ side?: Side; text: React.ReactNode; children: React.ReactNode; textWidth?: number; deviceShift?: number }> = ({
  side = 'left',
  text,
  children,
  textWidth = 660,
  deviceShift = 0,
}) => {
  const f = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const enter = interpolate(f, [0, 55], [0, 1], { ...clamp, easing: outExpo });
  const drift = interpolate(f, [0, durationInFrames], [0, 1]);
  const dir = side === 'left' ? 1 : -1;
  return (
    <AbsoluteFill style={{ flexDirection: side === 'left' ? 'row' : 'row-reverse', alignItems: 'center', padding: '0 80px', gap: 60 }}>
      <div style={{ width: textWidth, flex: 'none', display: 'flex', flexDirection: 'column', gap: 30 }}>{text}</div>
      <div
        style={{
          flex: 1,
          position: 'relative',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <div
          style={{
            // 2D only: 3D transforms (rotateY + perspective) left devices half-painted on some frames.
            transform: `translateX(${(1 - enter) * 260 * dir + deviceShift}px) translateY(${(1 - enter) * 40}px) scale(${0.92 + 0.08 * enter + drift * 0.03})`,
            opacity: enter,
            position: 'relative',
          }}
        >
          {children}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// A secondary device that springs in over the main one.
export const Overlay: React.FC<{ delay: number; x: number; y: number; children: React.ReactNode; from?: 'bottom' | 'right' | 'left' }> = ({ delay, x, y, children, from = 'bottom' }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: f - delay, fps, config: { damping: 15, stiffness: 90, mass: 1.1 } });
  const off = from === 'bottom' ? `translateY(${(1 - s) * 700}px)` : `translateX(${(1 - s) * (from === 'right' ? 900 : -900)}px)`;
  return (
    <div style={{ position: 'absolute', left: x, top: y, transform: `${off} rotate(${(1 - s) * 8}deg)`, opacity: Math.min(1, s * 2) }}>
      {children}
    </div>
  );
};

// ---------- 02 Hub ----------
export const HubScene: React.FC = () => (
  <FeatureLayout
    text={
      <>
        <Kicker n="01" delay={8}>Study hub</Kicker>
        <Headline text={'Five subjects.\n*One* portal.'} delay={14} />
        <Body delay={36}>Theory notes, step-by-step solved problems and the original course PDFs for every subject of the first semester.</Body>
        <div style={{ display: 'flex', gap: 54, marginTop: 10 }}>
          <Counter to={5} label="Subjects" color={C.cyan} delay={50} />
          <Counter to={130} label="Solved problems" color={C.blue} delay={60} />
          <Counter to={327} label="Official PDFs" color={C.green} delay={70} />
        </div>
      </>
    }
  >
    <Monitor clip="desktop-hub" width={1040} rate={fit('desktop-hub', 420)} zoom={[{ f: 0, z: 1 }, { f: 300, z: 1 }, { f: 400, z: 1.25, x: 0.5, y: 0.6 }]} />
  </FeatureLayout>
);

// ---------- 03 Search ----------
export const SearchScene: React.FC = () => (
  <FeatureLayout
    side="right"
    textWidth={600}
    text={
      <>
        <Kicker n="02" delay={8}>Instant search</Kicker>
        <Headline text={'Find any topic\nin a *keystroke.*'} delay={14} />
        <Body delay={36}>Live filtering across subjects, topics and concepts, plus semester tabs and keyboard shortcuts.</Body>
        <div style={{ display: 'flex', gap: 14, flexWrap: 'wrap' }}>
          <Chip delay={60}>/ search</Chip>
          <Chip delay={68} color={C.violet}>T theme</Chip>
          <Chip delay={76} color={C.amber}>Esc clear</Chip>
        </div>
      </>
    }
  >
    <Monitor
      clip="desktop-search"
      width={1040}
      startFrom={10}
      rate={fit('desktop-search', 560, 10)}
      zoom={[
        { f: 0, z: 1 },
        { f: 60, z: 1.75, x: 0.28, y: 0.3 },
        { f: 300, z: 1.75, x: 0.28, y: 0.36 },
        { f: 370, z: 1, x: 0.5, y: 0.5 },
        { f: 420, z: 1.45, x: 0.68, y: 0.3 },
        { f: 540, z: 1.2, x: 0.5, y: 0.45 },
      ]}
    />
  </FeatureLayout>
);

// ---------- 04 Theory (+ tablet) ----------
export const TheoryScene: React.FC = () => (
  <FeatureLayout
    textWidth={600}
    text={
      <>
        <Kicker n="03" delay={8} color={C.violet}>Theory</Kicker>
        <Headline text={'Derived from\n*first principles.*'} delay={14} />
        <Bullets
          delay={40}
          items={[
            { icon: '∑', text: 'Every equation typeset with KaTeX' },
            { icon: '◭', text: 'Original vector figures', color: C.violet },
            { icon: '§', text: 'Cited to the official slides', color: C.amber },
          ]}
        />
      </>
    }
  >
    <Monitor
      clip="desktop-theory"
      width={1040}
      rate={fit('desktop-theory', 500)}
      zoom={[{ f: 0, z: 1.15, x: 0.5, y: 0.4 }, { f: 160, z: 1.65, x: 0.5, y: 0.45 }, { f: 330, z: 1.65, x: 0.5, y: 0.55 }, { f: 470, z: 1.3, x: 0.5, y: 0.5 }]}
    />
    <Overlay delay={150} x={760} y={150}>
      <Tablet clip="tablet-materials" width={360} rate={fit('tablet-materials', 370)} />
    </Overlay>
  </FeatureLayout>
);

// ---------- 05 Problems (+ phone) ----------
const PHASES = ['Setup', 'Frames', 'Derivation', 'Interpretation'];
export const ProblemsScene: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <FeatureLayout
      side="right"
      textWidth={610}
      text={
        <>
          <Kicker n="04" delay={8} color={C.green}>Solved problems</Kicker>
          <Headline text={'Every step.\n*No algebraic skips.*'} delay={14} />
          <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            {PHASES.map((p, i) => {
              const on = interpolate(f, [60 + i * 45, 80 + i * 45], [0, 1], clamp);
              return (
                <div key={p} style={{ display: 'flex', alignItems: 'center', gap: 16, opacity: 0.25 + 0.75 * on, transform: `translateX(${(1 - on) * -20}px)` }}>
                  <span style={{ fontFamily: mono, fontSize: 20, color: C.green, width: 46 }}>0{i + 1}</span>
                  <span style={{ height: 2, width: 40 * on, background: C.green }} />
                  <span style={{ fontFamily: grotesk, fontSize: 30, color: C.text, fontWeight: 500 }}>{p}</span>
                </div>
              );
            })}
          </div>
          <Body delay={250} size={24}>Deep links open the official PDF at the exact page. One-click A4 PDFs for every problem.</Body>
        </>
      }
    >
      <Monitor
        clip="desktop-problems"
        width={1040}
        rate={fit('desktop-problems', 660)}
        zoom={[{ f: 0, z: 1 }, { f: 40, z: 2.1, x: 0.42, y: 0.62 }, { f: 120, z: 2.1, x: 0.5, y: 0.62 }, { f: 190, z: 1.25, x: 0.5, y: 0.5 }, { f: 230, z: 1.6, x: 0.5, y: 0.45 }, { f: 660, z: 1.6, x: 0.5, y: 0.5 }]}
      />
      <Overlay delay={290} x={-110} y={190}>
        <Phone clip="mobile-problems" width={270} rate={fit('mobile-problems', 370)} />
      </Overlay>
    </FeatureLayout>
  );
};

// ---------- 06 Ask AI (+ tablet) ----------
export const AskAIScene: React.FC = () => (
  <FeatureLayout
    textWidth={600}
    text={
      <>
        <Kicker n="05" delay={8} color={C.cyan}>Ask AI</Kicker>
        <Headline text={'Select any line.\n*Ask* about it.'} delay={14} />
        <Body delay={36}>A structured prompt with the context and formulas in LaTeX, sent to Claude or Gemini. Socratic tutor, full explanation or check my attempt.</Body>
        <div style={{ display: 'flex', gap: 14, flexWrap: 'wrap' }}>
          <Chip delay={70}>Socratic</Chip>
          <Chip delay={78} color={C.violet}>Explain</Chip>
          <Chip delay={86} color={C.green}>Check my attempt</Chip>
        </div>
      </>
    }
  >
    <Monitor
      clip="desktop-askai"
      width={1040}
      rate={fit('desktop-askai', 620)}
      zoom={[
        { f: 0, z: 1.2, x: 0.5, y: 0.35 },
        { f: 90, z: 1.9, x: 0.42, y: 0.24 },
        { f: 250, z: 1.9, x: 0.45, y: 0.26 },
        { f: 320, z: 1.55, x: 0.5, y: 0.45 },
        { f: 620, z: 1.55, x: 0.5, y: 0.5 },
      ]}
    />
    <Overlay delay={380} x={800} y={250} from="right">
      <Tablet clip="tablet-askai" width={300} startFrom={20} rate={fit('tablet-askai', 240, 20)} glow={C.cyan} />
    </Overlay>
  </FeatureLayout>
);

// ---------- 07 Palettes & theme (+ phone) ----------
const SW = [
  { n: 'Default', c: '#101828' },
  { n: 'Cream', c: '#f6efe0' },
  { n: 'Sepia', c: '#efe0c2' },
  { n: 'Slate paper', c: '#e3e5e8' },
  { n: 'Sage', c: '#dfe8d9' },
  { n: 'Charcoal', c: '#2a2e35' },
];
export const PaletteScene: React.FC = () => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <FeatureLayout
      side="right"
      textWidth={600}
      text={
        <>
          <Kicker n="06" delay={8} color={C.amber}>Reading comfort</Kicker>
          <Headline text={'Dark, light and\n*six reading palettes.*'} delay={14} />
          <div style={{ display: 'flex', gap: 18 }}>
            {SW.map((s, i) => {
              const k = spring({ frame: f - 50 - i * 6, fps, config: { damping: 10, stiffness: 160 } });
              return (
                <div key={s.n} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 8, transform: `scale(${k})` }}>
                  <div style={{ width: 62, height: 62, borderRadius: 31, background: s.c, border: '2px solid rgba(255,255,255,0.35)', boxShadow: `0 0 20px ${s.c}55` }} />
                  <span style={{ fontFamily: mono, fontSize: 14, color: C.dim }}>{s.n}</span>
                </div>
              );
            })}
          </div>
          <Body delay={90}>Every palette keeps text at AAA contrast. Your choice follows you across pages.</Body>
        </>
      }
    >
      <Monitor
        clip="desktop-palettes"
        width={1040}
        rate={fit('desktop-palettes', 560)}
        zoom={[{ f: 0, z: 1 }, { f: 50, z: 1.8, x: 0.62, y: 0.2 }, { f: 380, z: 1.8, x: 0.62, y: 0.25 }, { f: 450, z: 1.15, x: 0.5, y: 0.5 }]}
      />
      <Overlay delay={240} x={850} y={230}>
        <Phone clip="mobile-theme" width={250} rate={fit('mobile-theme', 320)} glow={C.amber} />
      </Overlay>
    </FeatureLayout>
  );
};

// ---------- 08 Focus Lab ----------
export const FocusScene: React.FC = () => (
  <FeatureLayout
    textWidth={600}
    text={
      <>
        <Kicker n="07" delay={8} color={C.violet}>Focus Lab</Kicker>
        <Headline text={'Study sound,\n*synthesised live.*'} delay={14} />
        <Bullets
          delay={40}
          items={[
            { icon: 'γ', text: 'Binaural presets from 10 to 40 Hz', color: C.violet },
            { icon: '~', text: 'Brown and pink noise, or noise only' },
            { icon: '▮', text: 'Live wave and spectrum view', color: C.green },
          ]}
        />
      </>
    }
  >
    <Monitor
      clip="desktop-focus"
      width={1040}
      rate={fit('desktop-focus', 500)}
      glow={C.violet}
      zoom={[{ f: 0, z: 1 }, { f: 70, z: 1.7, x: 0.85, y: 0.4 }, { f: 230, z: 1.7, x: 0.85, y: 0.5 }, { f: 300, z: 2.2, x: 0.86, y: 0.82 }, { f: 500, z: 2.2, x: 0.86, y: 0.82 }]}
    />
  </FeatureLayout>
);

// ---------- 09 Timer (+ phone) ----------
export const TimerScene: React.FC = () => (
  <FeatureLayout
    side="right"
    textWidth={600}
    text={
      <>
        <Kicker n="08" delay={8} color={C.green}>Study timer</Kicker>
        <Headline text={'Plan the session.\n*Then focus.*'} delay={14} />
        <Body delay={36}>Pomodoro (25/5) or deep focus (50/10). Type “3h” and the planner builds the full block-and-break timeline.</Body>
        <div style={{ display: 'flex', gap: 14 }}>
          <Chip delay={70} color={C.green}>25 / 5</Chip>
          <Chip delay={78} color={C.cyan}>50 / 10</Chip>
          <Chip delay={86} color={C.amber}>Planner</Chip>
        </div>
      </>
    }
  >
    <Monitor
      clip="desktop-timer"
      width={1040}
      rate={fit('desktop-timer', 520)}
      zoom={[{ f: 0, z: 1 }, { f: 80, z: 1.8, x: 0.88, y: 0.35 }, { f: 300, z: 1.8, x: 0.88, y: 0.55 }, { f: 520, z: 1.8, x: 0.88, y: 0.6 }]}
    />
    <Overlay delay={200} x={-90} y={210}>
      <Phone clip="mobile-timer" width={250} rate={fit('mobile-timer', 300)} glow={C.green} />
    </Overlay>
  </FeatureLayout>
);

// ---------- 10 Sources & exams ----------
export const SourcesScene: React.FC = () => (
  <FeatureLayout
    textWidth={600}
    text={
      <>
        <Kicker n="09" delay={8} color={C.amber}>Official material</Kicker>
        <Headline text={'327 PDFs.\nExams *by year.*'} delay={14} />
        <Body delay={36}>Theory, slides and problem sheets by unit. Partials and finals sorted by year, newest first, with solutions.</Body>
      </>
    }
  >
    <Monitor clip="desktop-sources" width={1040} rate={fit('desktop-sources', 380)} glow={C.amber} zoom={[{ f: 0, z: 1.25, x: 0.5, y: 0.4 }, { f: 380, z: 1.4, x: 0.5, y: 0.45 }]} />
  </FeatureLayout>
);

// ---------- 11 Responsive trio ----------
export const TrioScene: React.FC = () => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const sp = (d: number) => spring({ frame: f - d, fps, config: { damping: 14, stiffness: 80, mass: 1.1 } });
  const a = sp(10), b = sp(28), c = sp(46);
  const labels = ['Desktop · 1920×1080', 'Tablet · 820×1180', 'Mobile · 390×844'];
  const label = (t: string, k: number, col: string) => (
    <div style={{ marginTop: 26, textAlign: 'center', fontFamily: mono, fontSize: 19, letterSpacing: 2, color: col, opacity: k }}>{t}</div>
  );
  return (
    <AbsoluteFill>
      <div style={{ position: 'absolute', top: 70, width: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 18 }}>
        <Kicker n="10" delay={4}>Responsive by design</Kicker>
        <Headline text="One portal. *Every screen.*" align="center" size={68} delay={10} />
      </div>
      <div style={{ position: 'absolute', left: 0, right: 0, bottom: 70, display: 'flex', alignItems: 'flex-end', justifyContent: 'center', gap: 70 }}>
        <div style={{ transform: `translateY(${(1 - a) * 500}px)`, opacity: a }}>
          <Monitor clip="desktop-trio" width={900} rate={fit('desktop-trio', 500)} />
          {label(labels[0], a, C.blue)}
        </div>
        <div style={{ transform: `translateY(${(1 - b) * 600}px)`, opacity: b }}>
          <Tablet clip="tablet-trio" width={400} rate={fit('tablet-trio', 490)} />
          {label(labels[1], b, C.violet)}
        </div>
        <div style={{ transform: `translateY(${(1 - c) * 700}px)`, opacity: c }}>
          <Phone clip="mobile-trio" width={250} rate={fit('mobile-trio', 480)} />
          {label(labels[2], c, C.cyan)}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ---------- 12 Outro ----------
const TAGS = ['Theory', 'Solved problems', 'Official PDFs', 'Past exams', 'Ask AI', 'Focus Lab', 'Study timer', 'Reading palettes', 'Dark / Light', 'PDF export', 'Responsive'];
export const Outro: React.FC = () => {
  const f = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const fadeOut = interpolate(f, [durationInFrames - 40, durationInFrames], [1, 0], clamp);
  const urlS = useSpring(70);
  return (
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center', opacity: fadeOut }}>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 36 }}>
        <LogoMark size={104} delay={4} />
        <div style={{ fontFamily: display, fontSize: 112, color: C.text, opacity: useSpring(14), transform: `translateY(${(1 - useSpring(14)) * 50}px)`, filter: `drop-shadow(0 0 36px ${C.blue}55)` }}>
          Aerospace Engineering
        </div>
        <div style={{ fontFamily: serif, fontStyle: 'italic', fontSize: 40, color: C.dim, opacity: useSpring(30) }}>Theory, solved problems and official material, in one place.</div>
        <div
          style={{
            marginTop: 8,
            padding: '18px 38px',
            borderRadius: 999,
            fontFamily: mono,
            fontSize: 32,
            color: '#fff',
            background: 'rgba(79,124,255,0.14)',
            border: `1.5px solid transparent`,
            backgroundImage: `linear-gradient(rgba(10,16,48,0.92), rgba(10,16,48,0.92)), ${GRAD}`,
            backgroundOrigin: 'border-box',
            backgroundClip: 'padding-box, border-box',
            boxShadow: `0 0 60px ${C.blue}55`,
            transform: `scale(${urlS})`,
            opacity: urlS,
          }}
        >
          251-b.github.io/AerospaceEngineering
        </div>
        <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: 12, maxWidth: 1400, marginTop: 10 }}>
          {TAGS.map((t, i) => {
            const k = spring({ frame: f - 100 - i * 4, fps, config: { damping: 14, stiffness: 150 } });
            return (
              <span key={t} style={{ fontFamily: grotesk, fontSize: 22, color: C.text, padding: '8px 18px', borderRadius: 999, border: `1px solid ${C.line}`, background: 'rgba(255,255,255,0.04)', opacity: k, transform: `translateY(${(1 - k) * 20}px)` }}>
                {t}
              </span>
            );
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};

export { Sequence };
