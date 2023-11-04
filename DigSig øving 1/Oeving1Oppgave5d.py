import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

x_1 = np.array([1.0, 2.0, 3.0], dtype=float)
h_1 = np.array([1.0, 1.0, 1.0], dtype=float)

h_2 = []

for x in range(11):
    h_2.append(0.9**x)

#Tar nå h_2 først
y_1 = np.convolve(x_1,h_2)
y_2 = np.convolve(y_1,h_1)

n_1 = np.linspace(0,len(y_1)-1,13)


plt.subplot(2, 1, 1)
plt.stem(n_1, y_1)
plt.title("Oppgave 5d) y_1")
plt.xlabel("Sample[n]")
plt.ylabel("Verdi av y_1")

plt.subplot(2, 1, 2)
n_2 = np.linspace(0, len(y_2)-1, 15)
plt.stem(n_2, y_2)
plt.title("Oppgave 5d) y_2")
plt.xlabel("Sample[n]")
plt.ylabel("Verdi av y_2")

plt.tight_layout()  # Helps in avoiding overlap of subplots
plt.show()
