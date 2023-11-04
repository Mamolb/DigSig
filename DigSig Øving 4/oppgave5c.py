import numpy as np
from scipy import signal
from scipy.signal import lfilter
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

#Hplots


#plots for zeroes and poles

z = 1,-1

zeros = -1,1

polesx = [0.99*np.exp(2j*np.pi*fx),0.99*np.exp(-2j*np.pi*fx)]
polesy = [0.99*np.e**(2j*np.pi*fy),0.99*np.e**(-2j*np.pi*fy)]

Hw,w = signal.freqz(np.poly(z),np.poly(polesx))
Hy,w = signal.freqz(np.poly(z),np.poly(polesy))
f = w/(2*np.pi)

# plt.figure(figsize=(10, 8))
# plt.subplot(1, 1, 1)
# plt.plot(f, abs(Hy))
# plt.title('Plot of Hy(f)')
# plt.ylabel('Hy(f)')
# plt.xlabel('f')
# plt.show()

#We now do task 5 c)

#We want to see what the filter does with the input signal.

gx = lfilter(np.poly(z),np.poly(polesx),g)
gy = lfilter(np.poly(z),np.poly(polesy),g)
#We also want the frequency of the two outputs we fastfouriertransform it
FFT_gx = np.fft.fft(gx)
FFT_gy = np.fft.fft(gy)

F = np.linspace(0,1,500)

# plt.figure(figsize=(10, 8))
# plt.subplot(1, 1, 1)
# plt.plot(F, FFT_gy)
# plt.title('Plot of FFT_gy(f)')
# plt.ylabel('Gy(f)')
# plt.xlabel('f')
# plt.show()


#Task 5 d)

#We want to first find the coeffisients of the numerator and denominator

#Find the new roots of the nomenator
z2 = np.roots(np.poly(polesx)+np.poly(polesy))
newz = np.concatenate([z, z2])
newPolesH = np.concatenate([polesx, polesy])
#Plots zeroes and poles
# plt.scatter(np.real(newz), np.imag(newz), marker='o', color='b', label='Zeros')
# plt.scatter(np.real(newPolesH), np.imag(newPolesH), marker='x', color='r', label='Poles')

# # Plot the unit circle
# unit_circle = plt.Circle((0, 0), 1, fill=False, color='g', linestyle='dotted', label='Unit Circle')
# plt.gca().add_patch(unit_circle)
#Plot for complexplot
# plt.xlabel('Real')
# plt.ylabel('Imaginary')
# plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
# plt.axvline(0, color='black', linestyle='--', linewidth=0.5)
# plt.grid()
# plt.legend()
# plt.show()

#We want now to plot the magnitude respons
w,Finalg,= signal.freqz(np.poly(newz),np.poly(newPolesH))
finalResult = lfilter(np.poly(newz),np.poly(newPolesH),g)
FFT_Final = np.fft.fft(finalResult)
plt.figure(figsize=(10, 8))
plt.subplot(1, 1, 1)
F2 = np.linspace(0,1,500)
plt.plot(F2,FFT_Final)
plt.title('Plot FFT_Q(f)')
plt.ylabel('Q(f)')
plt.xlabel('f')
plt.show()


# plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Zeros')
# plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Poles')
# plt.xlabel('Real')
# plt.ylabel('Imaginary')
# plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
# plt.axvline(0, color='black', linestyle='--', linewidth=0.5)
# plt.grid()
# plt.legend()
# plt.show()





#Old Plot
# plt.figure(figsize=(10, 8))
# plt.subplot(2, 2, 1)
# plt.plot(n, d)
# plt.title('Plot of sequence d')
# plt.ylabel('d[n]')
# plt.xlabel('n')

# plt.subplot(2, 2, 2)
# plt.plot(n, np.abs(FFT_d))
# plt.title('Plot of magnitude response of D')
# plt.ylabel('D(f)')
# plt.xlabel('f')

# # Second set of plots
# plt.subplot(2, 2, 3)
# plt.plot(n, g)
# plt.title('Plot of sequence g')
# plt.ylabel('g[n]')
# plt.xlabel('n')

# plt.subplot(2, 2, 4)
# plt.plot(n, np.abs(FFT_g))
# plt.title('Plot of magnitude response of G')
# plt.ylabel('G(f)')
# plt.xlabel('f')

# # Adjust layout to prevent overlap
# plt.tight_layout()

# # Show the plots
# plt.show()
