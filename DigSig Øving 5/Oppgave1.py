import numpy as np
from scipy import signal
from scipy.signal import lfilter
import matplotlib.pyplot as plt

a1 = 0.4
a2 = 0.95
a3 = (-0.95)

n = np.linspace(0,50,51)
l = np.linspace(-50,50,101)
f = np.linspace(-0.5,0.5,101)

#We get diffrent x values
x1 = a1**n
x2 = a2**n
x3 = a3**n
#We now need to get the autocorrelation values
r_xx1 = a1**(np.abs(l))/(1-a1**2)
r_xx2 = a2**(np.abs(l))/(1-a2**2)
r_xx3 = a3**(np.abs(l))/(1-a3**2)
#Get diffrent Sxx(f)

s_xx1 = 1/(1-2*a1*np.cos(2*np.pi*f)+a1**2)
s_xx2 = 1/(1-2*a2*np.cos(2*np.pi*f)+a2**2)
s_xx3 = 1/(1-2*a3*np.cos(2*np.pi*f)+a3**2)

plt.plot(f, s_xx1, label='s_xx[f] plotted with a = 0.4')
plt.plot(f, s_xx2, label='s_xx[f] plotted with a = 0.95')
plt.plot(f, s_xx3, label='s_xx[f] plotted with a = -0.95')

# Add labels, legend, and title
plt.xlabel('f')
plt.ylabel('Diffrent s_xx[f]s')
plt.legend()
plt.title('Plot of s_xx[f] with diffrent a values')

# Show the plot
plt.show()
