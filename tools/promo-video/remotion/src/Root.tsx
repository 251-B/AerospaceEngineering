import React from 'react';
import { Composition } from 'remotion';
import { Promo, TOTAL } from './Promo';
import { FPS, W, H } from './theme';

export const RemotionRoot: React.FC = () => (
  <Composition id="Promo" component={Promo} durationInFrames={TOTAL} fps={FPS} width={W} height={H} />
);
