"""Remove one-frame paint defects from an image-sequence render.

A frame is suspect when some block differs from both neighbours while the neighbours agree
(check_frames.py). Real motion is reproducible, a paint defect is not: each suspect frame is
re-rendered until two consecutive renders agree, then the sequence is checked again.
usage: python3 settle.py <framesDir> [threshold]
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
frames_dir = Path(sys.argv[1])
THR = float(sys.argv[2]) if len(sys.argv) > 2 else 25.0
W, H, B = 320, 180, 20
CHECK = HERE / "check_frames.py"


def img(i):
    return frames_dir / f"element-{i:04d}.jpeg"


def small(path):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(path), "-vf", f"scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(H, W).astype(np.float32)


def block_diff(x, y):
    return float(np.abs(x - y).reshape(H // B, B, W // B, B).mean((1, 3)).max())


def detect():
    out = subprocess.run([sys.executable, str(CHECK), str(frames_dir / "element-%04d.jpeg"), str(THR)], capture_output=True, text=True).stdout
    return set(json.loads(out)["bad"])


def rerender(frames):
    subprocess.run(["node", str(HERE / "repair.mjs"), str(frames_dir), *map(str, sorted(frames))], check=True, cwd=HERE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


stable = set()
fixed = 0
for rnd in range(1, 9):
    suspects = detect() - stable
    print(f"check {rnd}: {len(suspects)} suspect frames", flush=True)
    if not suspects:
        break
    pending = set(suspects)
    for attempt in range(1, 7):
        before = {i: small(img(i)) for i in pending}
        rerender(pending)
        agreed = {i for i in pending if block_diff(before[i], small(img(i))) < 6}
        stable |= agreed
        changed = pending - agreed
        if attempt == 1:
            fixed += len(changed)
        print(f"  pass {attempt}: {len(agreed)} reproducible, {len(changed)} changed (defects fixed or re-rendered again)", flush=True)
        pending = changed
        if not pending:
            break
else:
    sys.exit("sequence did not settle")
print(f"settled: {len(stable)} suspect frames now render reproducibly ({fixed} of them were paint defects)", flush=True)
