# -*- coding: utf-8 -*-
"""
@author: Dan Koskiranta
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

# Read in original audio
# 'Nightingales' audio
rate, audio = wavfile.read('2025-02-27 0832.wav')
# 'Song Thrush' is xeno-canto sourced audio, originally .mp3 & converted to .wav using Audacity
#rate, audio = wavfile.read('../Audio/xenocanto/XC255239 - Song Thrush - Turdus philomelos.wav')
# 'blackbird-in-the-morning' is a mono track
#rate, audio = wavfile.read('../Audio/Birdsong/431911__sesom42__blackbird-in-the-morning.wav') 

 # Average the stereo channels
 # NOTE: comment this out for mono audio files
#audio = np.mean(audio, axis=1)

 # Total number of audio samples   
N = audio.shape[0]       
 # Length of audio track in seconds 
L = N / rate        
# Add code                 
print(f'Audio length: {L:.2f} seconds')

# Spectrogram calculation using scipy
# Add code
freqs_sp, times_sp, spec_sp= signal.spectrogram(audio, fs=rate, window=('tukey', 0.25),
                     nperseg=1024, noverlap= 1024-100,
                     detrend=False, scaling= 'spectrum')
# Calculate the magnitude of the spectrum in decibels
# Add code
spec_db_sp = 10*np.log10(spec_sp)

# Function to plot the original audio in the time-domain
def plot_time_domain():
    fig = plt.figure(figsize=(14,10))
    ax = fig.add_subplot(111)
    ax.plot(np.arange(N) / rate, audio)
    ax.set_title('Birdsong', fontsize=26, pad=10, color='sienna');
    ax.set_xlabel('Time (s)', fontsize=20, labelpad=10)
    ax.set_ylabel('Amplitude', fontsize=20, labelpad=10);

# Function to plot the spectrogram, parameters may require tuning depending on the audio file
def plot_spec_scipy():
    fig, ax = plt.subplots(figsize=(18,14))
    im = ax.pcolormesh(times_sp, freqs_sp/1000, spec_db_sp, vmax=spec_db_sp.max(), vmin=0, cmap=plt.cm.gist_yarg, linewidth=10, shading='auto')
    cb = fig.colorbar(im, ax=ax, orientation="horizontal")
    ax.set_ylabel('Frequency (kHz)', fontsize=26, labelpad=10)
    ax.set_xlabel('Time (s)', fontsize=26, labelpad=10);
    ax.set_title('Birdsong Spectrogram', fontsize=26, pad=10, color='sienna');
    ax.set_title('Birdsong', fontsize=26, pad=10, color='sienna');
    ax.set_ylim(0, 8)
    ax.set_xlim(0, 5)
    ax.tick_params(axis='both', which='both', labelsize=22, length=0)
    cb.set_label('Power (dB)', fontsize=26, labelpad=10)
    cb.ax.tick_params(labelsize=22)
    
plot_time_domain();
plot_spec_scipy();