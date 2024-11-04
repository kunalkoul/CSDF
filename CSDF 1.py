#!/usr/bin/env python
# coding: utf-8

# In[9]:


import wave
import numpy as np
import matplotlib.pyplot as plt

# Function to read audio file and extract data
def read_audio_file(file_path):  # Corrected argument
    with wave.open(file_path, 'rb') as wave_file:
        num_channels = wave_file.getnchannels()
        sample_width = wave_file.getsampwidth()
        frame_rate = wave_file.getframerate()
        num_frames = wave_file.getnframes()
        raw_data = wave_file.readframes(num_frames)
        audio_data = np.frombuffer(raw_data, dtype=np.int16)
    return audio_data, frame_rate

# Function to plot audio waveform
def plot_audio_waveform(audio_data, frame_rate):
    time = np.arange(0, len(audio_data)) / frame_rate
    plt.plot(time, audio_data)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Audio Waveform')
    plt.show()

# Function to plot audio spectrum
def plot_audio_spectrum(audio_data, frame_rate):
    n = len(audio_data)
    p = np.fft.fft(audio_data)
    n_unique_pts = int(np.ceil((n + 1) / 2.0))
    p = p[:n_unique_pts]
    p = np.abs(p)
    p = p / float(n)
    p = p**2
    if n % 2 > 0:
        p[1:] = p[1:] * 2
    else:
        p[1:-1] = p[1:-1] * 2
    freq_array = np.arange(0, n_unique_pts) * (frame_rate / n)
    plt.plot(freq_array/1000, 10 * np.log10(p))
    plt.xlabel('Frequency (kHz)')
    plt.ylabel('Power (dB)')
    plt.title('Audio Spectrum')
    plt.show()

if __name__ == '__main__':
    audio_data, frame_rate = read_audio_file(r"sample-9s.wav")  # Correct file path

    plot_audio_waveform(audio_data, frame_rate)
    plot_audio_spectrum(audio_data, frame_rate)


# In[ ]:




