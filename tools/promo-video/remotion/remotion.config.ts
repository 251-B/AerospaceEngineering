import { Config } from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setJpegQuality(95);
// 'angle' is ~7x faster than 'swangle' on a CPU-only machine.
Config.setChromiumOpenGlRenderer('angle');
// Optional: point at a local Chrome headless shell instead of letting Remotion download one.
if (process.env.REMOTION_BROWSER) Config.setBrowserExecutable(process.env.REMOTION_BROWSER);
