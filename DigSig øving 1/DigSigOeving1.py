import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Parameters
A = 1             # Amplitude
f1 = 0.3           # Normalized frequency
Fs = 12000         # Sampling frequency
duration = 4      # Duration in seconds

# Time vector
t = np.linspace(0, duration, int(Fs * duration), endpoint=False)

# Generate the discrete harmonic sequence
x = A * np.cos(2*np.pi*f1*t)

# Plot the sequence 
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Discrete Harmonic Sequence')
plt.show() 

sd.play(x,Fs)
sd.wait()

