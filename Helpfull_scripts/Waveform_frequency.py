import wave
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog

# Selects file from storage\
filename = filedialog.askopenfilename(filetypes = (("signal files", "*.wav;*.mp3")
                                                             ,("All files", "*.*") ))
# read audio samples 
# input_data = read(filename)
# audio = input_data[1]

signal_wave = wave.open(filename)
sample_rate = 16000
sig = np.frombuffer(signal_wave.readframes(sample_rate), dtype=np.int16)

sig = sig[:]

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
