#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
"""The test tone of the sample link tests, computed here so that no audio file is kept in the tree:
0.9 s, 44.1 kHz, 16-bit mono, a decaying 330 Hz with its octave (tests/host_link.c compares the decoded
sample with the same formula).   gen_tone.py OUT.wav"""
import math, struct, sys, wave

RATE, N = 44100, 39690
out = bytearray()
for i in range(N):
    t = i / RATE
    v = 0.6 * math.sin(2 * math.pi * 330 * t) * math.exp(-t * 2) + 0.2 * math.sin(2 * math.pi * 660 * t) * math.exp(-t * 4)
    out += struct.pack("<h", int(30000 * v))
with wave.open(sys.argv[1], "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE)
    w.writeframes(bytes(out))
