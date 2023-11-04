import numpy as np
from scipy import signal
from scipy.signal import lfilter
import matplotlib.pyplot as plt
import scipy.io
from scipy.signal import lfilter, unit_impulse
from scipy.signal import freqz
from scipy.signal import lti, impulse, freqz

R = 8
alpha = 0.7
# Define the coefficients of the filter H(z)
b = [1]   # Numerator coefficients
a = [1, 0, 0, 0, 0, 0, 0, 0, 0.7]   # Denominator coefficients

# Create a unit sample input signal
n = np.arange(0, 50)  # Number of samples
x = unit_impulse(len(n))

# Compute the unit sample response using lfilter
y = lfilter(b, a, x)
#compute the frequency respons:
w, h = freqz(b, a)
w2 = np.linspace(0,20,len(w))
magnitude = np.abs(h)

#New Filter

# Filter coefficients

newAlpha = 0.8
newN = 6
newR = 16

b1 = np.zeros(newN*newR+1)#Numerator
#putting in values
b1[0] = 1
b1[newN*newR] = -(newAlpha**newN)
a1 = np.zeros(newR+1)#Denominator
a1[0] = 1
a1[newR] = -newAlpha
n2 = np.linspace(0,400)
x2 = unit_impulse(len(n2))
y1 = lfilter(b1, a1, x2)


w2, h2 = freqz(b, a)
magnitude2 = np.abs(h2)
# Plot the unit sample response
plt.stem(n2, y1, basefmt='b')
plt.xlabel('n (Sample Index)')
plt.ylabel('h[n] (Unit Sample Response)')
plt.title('Unit Sample Response of the second filter)')
plt.grid(True)
plt.show()

#Plot the new filter
# plt.figure(figsize=(10, 6))
# plt.plot(w2, (magnitude2))
# plt.title('Frequency Response')
# plt.ylabel('Magnitude (dB)')
# plt.grid(True)
# plt.show()

#plot the frequency respons:
# Plot the magnitude response
# plt.figure(figsize=(10, 6))
# plt.plot(w, 20 * np.log10(magnitude))
# plt.title('Frequency Response')
# plt.ylabel('Magnitude (dB)')
# plt.grid(True)
# plt.show()

