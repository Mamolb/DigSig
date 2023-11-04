import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Define your filter coefficients (numerator and denominator)
ha_up = [1.9, -1.9]  # Numerator coefficients
hb_up = [2, -1.8]  # Denominator coefficients
#Define lower filter
ha_low = [0.1,0.1]
hb_low = [2,-1.8]

# Compute the frequency response
w, h = signal.freqz(ha_up, hb_up)
w2, h2 = signal.freqz(ha_low,hb_low)


# Plot the magnitude and phase of the frequency response
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(w,abs(h))
plt.title('Frequency Response of higer')
plt.ylabel('Magnitude')
plt.xlabel("Angular frequency")

plt.subplot(2, 1, 2)
plt.plot(w2,abs(h2))
plt.title('Frequency Response of lower')
plt.ylabel('Magnitude')
plt.xlabel("Angular frequency")
plt.show()
