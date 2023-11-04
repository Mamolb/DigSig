import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

#Frequency where I want to plot
f = np.linspace(0,1,100)
#Here is the filter
H_f = (1-(0.9*np.e**(-1j*2*np.pi*f))**27)/(1-0.9*np.e**(-1j*2*np.pi*f))
# 1 a)
#plot
# plt.figure()
# plt.title("Plot of magnituderespons for filter task 1")
# plt.plot(f, 20 * np.log10(np.abs(H_f)))
# plt.xlabel("Frequency]")
# plt.ylabel("Magnitude [dB]")
# plt.margins(0, 0.1)
# plt.grid(True)
# plt.show()

#Task 1 b)
Nx = 28
k = np.linspace(0,Nx-1,Nx)
n = np.linspace(0,Nx-1,Nx)
x_n = 0.9**n
#Takse 1b) result
X_k1 = fft(x_n,int(Nx/4))
X_k2 = fft(x_n,int(Nx/2))
X_k3 = fft(x_n,int(Nx))
X_k4 = fft(x_n,int(2*Nx))
#Task 1 d)
f1 = np.linspace(0,1,7)
f2 = np.linspace(0,1,14)
f3 = np.linspace(0,1,28)
f4 = np.linspace(0,1,56)

# Plot the magnitude response

#Task 2 a)

#New filter
N_h = 9
N_y = 28+9-1
h_n = [1]*(N_h)
#calculate y_n
y_n = np.convolve(x_n,h_n)
n1 = np.linspace(0,len(y_n)-1,len(y_n))

#Task 2 b)
#Calculate DFT
NyValue = (Nx+N_h-1)
X = fft(x_n,int(NyValue/4))
H = fft(h_n,int(NyValue/4))
Y = X*H
newy_value1 = ifft(Y,int(NyValue/4))
n2 = np.linspace(0,len(newy_value1)-1,len(newy_value1))
#second value
X = fft(x_n,int(NyValue/2))
H = fft(h_n,int(NyValue/2))
Y = X*H
newy_value2 = ifft(Y,int(NyValue/2))
n3 = np.linspace(0,len(newy_value2)-1,len(newy_value2))
#theird value
X = fft(x_n,int(NyValue))
H = fft(h_n,int(NyValue))
Y = X*H
newy_value3 = ifft(Y,int(NyValue))
n4 = np.linspace(0,len(newy_value3)-1,len(newy_value3))
#Fourth value
X = fft(x_n,int(NyValue*2))
H = fft(h_n,int(NyValue*2))
Y = X*H
newy_value4 = ifft(Y,int(2*NyValue))
n5 = np.linspace(0,len(newy_value4)-1,len(newy_value4))


# yk1 = np.linspace(0,len(Y_k1)-1,len(Y_k1))
# yk2 = np.linspace(0,len(Y_k2)-1,len(Y_k2))
# yk3 = np.linspace(0,len(Y_k3)-1,len(Y_k3))
# yk4 = np.linspace(0,len(Y_k4)-1,len(Y_k4))
fig, axs = plt.subplots(2, 2)

axs[0, 0].stem(n2, newy_value1,linefmt='r-')
axs[0, 0].stem(n1, y_n,linefmt='g-')
axs[0, 0].set_title('Plot with N_y/4')
axs[0, 1].stem(n3, newy_value2, 'tab:orange')
axs[0, 1].stem(n1, y_n,linefmt='g-')
axs[0, 1].set_title('Plot with N_y/2')
axs[1, 0].stem(n4, newy_value3, 'tab:green')
axs[1, 0].stem(n1, y_n,linefmt='r-')
axs[1, 0].set_title('Plot with N_y')
axs[1, 1].stem(n5, newy_value4, 'tab:red')
axs[1, 0].stem(n1, y_n,linefmt='b-')
axs[1, 1].set_title("Plot with 2*N_y")
plt.show()




