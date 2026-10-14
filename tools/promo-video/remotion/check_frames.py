"""Find frames with paint defects: a block that differs from both neighbours while the neighbours agree.
usage: check_frames.py <video | 'dir/%05d.jpeg'> [threshold]  -> prints JSON list of 0-based bad frame indices"""
import subprocess, sys, json, numpy as np
src = sys.argv[1]; thr = float(sys.argv[2]) if len(sys.argv) > 2 else 12.0
W, H, B = 320, 180, 20
args = ['ffmpeg', '-loglevel', 'error']
if '%' in src: args += ['-framerate', '60', '-i', src]
else: args += ['-i', src]
raw = subprocess.run(args + ['-vf', f'scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True).stdout
v = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)
def blocks(x):  # mean abs diff per BxB block
    return x.reshape(x.shape[0], H // B, B, W // B, B).mean((2, 4))
a, b, c = v[:-2], v[1:-1], v[2:]
s = (blocks(np.abs(b - a)) + blocks(np.abs(b - c)) - blocks(np.abs(c - a))) / 2
score = s.reshape(len(s), -1).max(1)
bad = [int(i + 1) for i in np.where(score > thr)[0]]
print(json.dumps({'frames': int(len(v)), 'bad': bad, 'top': sorted([[round(float(x), 1), int(i + 1)] for i, x in enumerate(score)], reverse=True)[:12]}))
