import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the range of values for w
w = np.linspace(0, np.pi, 1000)  # Creating an array of 1000 points from 0 to 2*pi

# Step 2: Calculate the values of the function
H_1 = (2 * np.cos(w) + 2)
H_2 = 1 / np.sqrt(1 + 1.8 * np.cos(w) + 0.81)

#Same shit but for phase respons:

O_1 = -w
O_2 = np.arctan(0.9*np.sin(w)/(1+0.9*np.cos(w)))

# Step 3: Create the plot
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
plt.plot(w, O_1, label='2*cos(w) + 2', color='blue')
plt.plot(w,O_2,label="1/(1+1.8cos(w)+0.81)^1/2",color="red")
plt.xlabel('w')
plt.ylabel('Phase respons')
plt.title('Phase respons of the two systems')
plt.grid(True)
plt.legend()
plt.show()

