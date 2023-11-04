import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft


f1 = 7/40
f2 = 9/40
n = np.linspace(0,99,100)
x_n = np.sin(2*np.pi*f1*n) + np.sin(2*np.pi*f2*n)

#Find the FFT with diffrent lengths
#Length 1024
n2 = np.linspace(0,999,1000)
n3 = np.linspace(0,29,30)
n4 = np.linspace(0,9,10)
x_n1 = np.sin(2*np.pi*f1*n2) + np.sin(2*np.pi*f2*n2)
x_n2 = np.sin(2*np.pi*f1*n3) + np.sin(2*np.pi*f2*n3)
x_n3 = np.sin(2*np.pi*f1*n4) + np.sin(2*np.pi*f2*n4)

#100
X1 = fft(x_n,1024)
#1000
X2 = fft(x_n1,1024)
#30
X3 = fft(x_n2,1024)
#10
X4 = fft(x_n3,1024)
#I just want to plot half of the plot, (Aliasing)
f1 = np.linspace(0,0.5,int(len(X1)/2))
f2 = np.linspace(0,0.5,int(len(X2)/2))
f3 = np.linspace(0,0.5,int(len(X3)/2))
f4 = np.linspace(0,0.5,int(len(X4)/2))
#Plots
fig, axs = plt.subplots(2)
#only want to plot half of X1 osv to avoid aliasing

#Task 2c)

X5 = fft(x_n,256)
X6 = fft(x_n,128)
f5 = np.linspace(0,0.5,int(len(X5)/2))
f6 = np.linspace(0,0.5,int(len(X6)/2))
axs[0].plot(f5, np.abs(X5)[:len(X5)//2])
axs[0].set_title('Plot with N =256')
axs[1].plot(f6, np.abs(X6)[:len(X6)//2])
axs[1].set_title('Plot with N = 128')
# axs[1, 0].plot(f3, np.abs(X3)[:len(X3)//2])
# axs[1, 0].set_title('Plot with N = 30')
# axs[1, 1].plot(f4, np.abs(X4)[:len(X4)//2])
# axs[1, 1].set_title("Plot with N = 10")
plt.show()
