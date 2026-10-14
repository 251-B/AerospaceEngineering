"""Synthesise an original ambient soundtrack synced to the scene cuts (public/soundtrack.wav)."""
import json
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
SR = 48000
FPS = 60
cfg = json.loads((ROOT / "src/scenes.json").read_text())
T, D = cfg["transition"], cfg["durations"]
total_frames = sum(D) - T * (len(D) - 1)
dur = total_frames / FPS
N = int(dur * SR)
t = np.arange(N) / SR
rng = np.random.default_rng(7)

# transition centres (s)
cuts, acc = [], 0
for d in D[:-1]:
    acc += d - T
    cuts.append((acc + T / 2) / FPS)

L = np.zeros(N)
R = np.zeros(N)


def note(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def env_adsr(n, a, r):
    e = np.ones(n)
    na, nr = min(int(a * SR), n // 2), min(int(r * SR), n // 2)
    e[:na] = np.linspace(0, 1, na) ** 2
    if nr:
        e[-nr:] *= np.linspace(1, 0, nr) ** 2
    return e


# ---- chord progression (D minor, cinematic): 5 s per chord ----
BPM = 96
beat = 60 / BPM
bar = 4 * beat
chord_len = 2 * bar  # 5 s
prog = [
    [50, 57, 62, 65, 69, 76],  # Dm(add9)
    [46, 53, 58, 62, 65, 72],  # Bbmaj7-ish
    [41, 53, 57, 60, 65, 69],  # F
    [48, 55, 60, 64, 67, 74],  # C(add9)
]

# ---- pad: detuned additive saw-ish voices, slow swell, chord crossfades ----
pad = np.zeros((2, N))
k = 0
start = 0.0
while start < dur:
    ch = prog[k % 4]
    s0 = int(max(0, start - 0.6) * SR)
    s1 = min(N, int((start + chord_len + 0.8) * SR))
    n = s1 - s0
    if n <= 0:
        break
    tt = np.arange(n) / SR
    e = env_adsr(n, 1.2, 1.4)
    for vi, m in enumerate(ch[1:]):
        for ci, det in enumerate((-0.08, 0.0, 0.07)):
            f0 = note(m + det)
            ph = rng.uniform(0, 2 * np.pi)
            w = sum(np.sin(2 * np.pi * f0 * h * tt + ph * h) / h ** 1.6 for h in (1, 2, 3, 4))
            pan = 0.5 + 0.35 * np.sin(vi * 1.3 + ci * 2.1)
            pad[0, s0:s1] += w * e * (1 - pan) * 0.018
            pad[1, s0:s1] += w * e * pan * 0.018
    # sub bass on the root
    sub = np.sin(2 * np.pi * note(ch[0] - 12) * tt) * env_adsr(n, 0.4, 1.0) * 0.10
    pad[0, s0:s1] += sub
    pad[1, s0:s1] += sub
    start += chord_len
    k += 1
# slow filter-like movement: amplitude shimmer
pad = 0.6 * pad + 0.4 * pad.mean(axis=0, keepdims=True)
pad *= 0.85 + 0.15 * np.sin(2 * np.pi * t / 7.0)

# ---- arpeggio plucks (start after intro) ----
arp = np.zeros((2, N))
step = beat / 2
i = 0
tk = 5.0
while tk < dur - 3.5:
    ch = prog[int(tk // chord_len) % 4]
    pattern = [ch[2] + 12, ch[3] + 12, ch[4] + 12, ch[3] + 12, ch[5], ch[4] + 12, ch[3] + 12, ch[2] + 12]
    m = pattern[i % 8]
    n = int(0.9 * SR)
    s0 = int(tk * SR)
    s1 = min(N, s0 + n)
    tt = np.arange(s1 - s0) / SR
    f0 = note(m)
    w = (np.sin(2 * np.pi * f0 * tt) + 0.25 * np.sin(2 * np.pi * 2 * f0 * tt) * np.exp(-tt * 9)) * np.exp(-tt * 5.5)
    vel = 0.05 * (1.0 if i % 4 == 0 else 0.7)
    pan = 0.25 if i % 2 else 0.75
    arp[0, s0:s1] += w * vel * (1 - pan)
    arp[1, s0:s1] += w * vel * pan
    tk += step
    i += 1
arp *= np.clip((t - 5) / 2.5, 0, 1)

# ---- soft pulse: kick on 1 & 3, airy hats on off-beats ----
perc = np.zeros(N)
tk = 10.0
bi = 0
while tk < dur - 5:
    s0 = int(tk * SR)
    if bi % 2 == 0:
        n = int(0.35 * SR)
        tt = np.arange(min(n, N - s0)) / SR
        f = 48 + 70 * np.exp(-tt * 28)
        kick = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 9) * 0.28
        perc[s0:s0 + len(tt)] += kick
    hs = int((tk + beat / 2) * SR)
    n = int(0.06 * SR)
    if hs + n < N:
        hat = rng.standard_normal(n)
        hat = np.diff(np.concatenate([[0], hat])) * np.exp(-np.arange(n) / SR * 70) * 0.025
        perc[hs:hs + n] += hat
    tk += beat
    bi += 1
perc_st = np.vstack([perc, perc])

# ---- whooshes at every cut + intro impact ----
fx = np.zeros((2, N))
for c in cuts:
    n = int(1.4 * SR)
    s0 = int((c - 0.9) * SR)
    if s0 < 0:
        continue
    noise = rng.standard_normal((2, n))
    # band-ish: difference of two smoothings
    tt = np.arange(n) / SR
    shape = np.sin(np.pi * np.clip(tt / 1.4, 0, 1)) ** 3
    k1 = np.ones(18) / 18
    b = np.vstack([np.convolve(noise[j], k1, "same") for j in range(2)])
    fx[:, s0:s0 + n] += b * shape * 0.22
# intro: riser into impact at 0.55 s (logo) and a low boom
n = int(3.0 * SR)
tt = np.arange(n) / SR
boom = np.sin(2 * np.pi * (36 + 30 * np.exp(-tt * 6)) * tt) * np.exp(-tt * 1.8) * 0.45
s0 = int(0.55 * SR)
fx[:, s0:s0 + n] += boom
shimmer = np.zeros(n)
for m in (74, 81, 86):
    shimmer += np.sin(2 * np.pi * note(m) * tt) * np.exp(-tt * 1.2) * 0.03
s1 = int(1.0 * SR)
fx[0, s1:s1 + n] += shimmer
fx[1, s1:s1 + n] += shimmer

mix = pad + arp + perc_st * 0.9 + fx

# ---- reverb: FFT convolution with decaying stereo noise ----
ir_n = int(2.6 * SR)
irt = np.arange(ir_n) / SR
irs = []
for j in range(2):
    ir = rng.standard_normal(ir_n) * np.exp(-irt * 2.6)
    ir = np.convolve(ir, np.ones(6) / 6, "same")  # darken
    ir[0] = 0
    irs.append(ir / np.sqrt(np.sum(ir ** 2)))
wet = np.zeros_like(mix)
nfft = 1 << int(np.ceil(np.log2(N + ir_n)))
for j in range(2):
    src = pad[j] + arp[j] + fx[j] * 0.6
    wet[j] = np.fft.irfft(np.fft.rfft(src, nfft) * np.fft.rfft(irs[j], nfft), nfft)[:N]
mix = mix + wet * 0.32

# fades and master
fade_in = np.clip(t / 0.4, 0, 1)
fade_out = np.clip((dur - t) / 4.0, 0, 1) ** 1.5
mix *= fade_in * fade_out
peak = np.max(np.abs(mix))
mix = np.tanh(mix / peak * 1.3) * 0.86

out = (np.clip(mix.T, -1, 1) * 32767).astype("<i2")
with wave.open(str(ROOT / "public/soundtrack.wav"), "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(out.tobytes())
print(f"soundtrack: {dur:.2f} s, cuts at {[round(c, 2) for c in cuts]}")
