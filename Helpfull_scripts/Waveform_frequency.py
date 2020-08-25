import wave
import numpy as np
import matplotlib.pyplot as plt

signal_wave = wave.open('signal_files\wav\LTEsample.wav', 'r')
sample_rate = 160000
sig = np.frombuffer(signal_wave.readframes(sample_rate), dtype=np.int16)
# For the whole segment of the wave file
sig = sig[:]

# For partial segment of the wave file
#sig = sig[25000:32000]

# Separating stereo channels
#left, right = data[0::2], data[1::2]

# Plot the waveform (plot_a) and the frequency spectrum (plot_b)
plt.figure(1)

plot_a = plt.subplot(211)
plot_a.plot(sig)
plot_a.set_xlabel('sample rate * time')
plot_a.set_ylabel('energy')

plot_b = plt.subplot(212)
plot_b.specgram(sig, NFFT=1024, Fs=sample_rate, noverlap=900)
plot_b.set_xlabel('Time')
plot_b.set_ylabel('Frequency')

plt.show()