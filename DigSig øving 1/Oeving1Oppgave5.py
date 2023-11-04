import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

y_1 = np.array([1.0, 3.0, 6.0, 5.0, 3.0], dtype=float)

h_2 = []

for x in range(11):
    h_2.append(0.9**x)

y_2 = np.convolve(y_1,h_2)
n = np.linspace(0,len(y_2)-1,15)
plt.stem(n,y_2)
plt.title("Oppgave 5b)")
plt.xlabel("Sample[n]")
plt.ylabel("Verdi av y_2")
plt.show()
