# Copied from internet   ===   ===   ===  == = = = ===

import wave
import numpy as np

wr = wave.open('1.wav', 'r')
sz = 44100 # Read and process 1 second at a time.
da = np.fromstring(wr.readframes(sz), dtype=np.int16)
left, right = da[0::2], da[1::2]

lf, rf = abs(np.fft.rfft(left)), abs(np.fft.rfft(right))

import matplotlib.pyplot as plt

plt.figure(1)
a = plt.subplot(211)
r = 2**16/2
a.set_ylim([-r, r])
a.set_xlabel('time [s]')
a.set_ylabel('sample value [-]')
x = np.arange(44100)/44100
plt.plot(x, left)
b = plt.subplot(212)
b.set_xscale('log')
b.set_xlabel('frequency [Hz]')
b.set_ylabel('|amplitude|')
plt.plot(lf)
plt.savefig('sample-graph.png')