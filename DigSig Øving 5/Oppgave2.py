import numpy as np
from scipy import signal
from scipy.signal import lfilter
import matplotlib.pyplot as plt
import scipy.io

# Load the .mat file
mat = scipy.io.loadmat('signals.mat')

# Access the 'x' and 'y' vectors from the loaded .mat file
x = mat['x'].flatten()  # 'x' vector
y = mat['y'].flatten()  # 'y' vector

n = np.linspace(0,300,len(x))

#We now want to find the crosscorrelation r_yx(l)

#We fint the crosscorrelation of r_yx
r_yx = np.correlate(y, x, mode='full')
L = (len(r_yx) + 1)/2
print(L)
l = np.linspace(-L+1,L-1,len(r_yx))

#We now find the crosscorrelation r_yx[l]

r_yx2 = np.convolve(y, x[::-1], mode='full')
#Plot code
plt.stem(l, r_yx2)
# plt.plot(l, y, label='y values plotted')

# Add labels, legend, and title
plt.xlabel('l')
plt.ylabel('Value of r_yx[l]')
plt.legend()
plt.title('Crosscorrelation of r_yx[l]')

# Show the plot
plt.show()
