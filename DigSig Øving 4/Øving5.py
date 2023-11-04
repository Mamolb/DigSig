import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

Ax = 0.25
Ay = 0.25

fx = 0.04
fy = 0.10

L = 500

n = np.linspace(0,L-1,L)
d = Ax*np.cos(2*np.pi*fx*n) + Ay*np.cos(2*np.pi*fy*n)

#Error
e = np.random.randn(L)

#We need to calculate the D(f)
#Using FFT with lengt N = 2048
FFT_d = np.fft.fft(d)

g = d + e

FFT_g = np.fft.fft(g)

#plots
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(n, d)
plt.title('Plot of sequence d')
plt.ylabel('d[n]')
plt.xlabel('n')

plt.subplot(2, 2, 2)
plt.plot(n, np.abs(FFT_d))
plt.title('Plot of magnitude response of D')
plt.ylabel('D(f)')
plt.xlabel('f')

# Second set of plots
plt.subplot(2, 2, 3)
plt.plot(n, g)
plt.title('Plot of sequence g')
plt.ylabel('g[n]')
plt.xlabel('n')

plt.subplot(2, 2, 4)
plt.plot(n, np.abs(FFT_g))
plt.title('Plot of magnitude response of G')
plt.ylabel('G(f)')
plt.xlabel('f')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()
