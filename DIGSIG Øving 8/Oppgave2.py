##Solving the Yule-Walker equations to get the coefficients of the AR model
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.linalg import solve

#Defining the AR model

#AN np.array with 1.16 as 0 value and -0.4 as 1 and -1 value, and 0 for the rest
#NOTE: For values that is zero in the array I will just type in zero
Yxx = np.array([1.16, -0.4,-0.4])
#Add zeroes to Yxx

##Fist order Yu-Walker equation

#Equation on form Ax = B
B1 = -Yxx[1]
A1 = Yxx[0]

X1 = solve(A1,B1)
#print with line
print("First order Yu-Walker equation: \n")
print("The coefficent of a1 is " + str(X1)+"\n")

#Second order Yu-Walker equation

#Creating a 2x2 matrix with values from Yxx
A2 = np.array([[Yxx[0],Yxx[1]], [Yxx[-1],Yxx[0]]])
#Create a 1x2 matrix with values from B2
B2 = np.array([[-Yxx[-1]],[0]])
X2 = solve (A2,B2)
#print with line
print("Second order Yu-Walker equation: \n")
print("The coefficient of a1 is " + str(X2[0]) + ". The coefficient of a2 is " + str(X2[1]) + "\n")

#Third order Yu-Walker equation
#Creating a 3x3 matrix with values from Yxx
A3 = np.array([[Yxx[0],Yxx[1],0], [Yxx[-1],Yxx[0],Yxx[1]], [0,Yxx[-1],Yxx[0]]])
#Create a 1x3 matrix with values from B3
B3 = np.array([[-Yxx[-1]],[0],[0]])
X3 = solve (A3,B3)
#print with line
print("Third order Yu-Walker equation: \n")
print("The coefficient of a1 is " + str(X3[0]) + ". The coefficient of a2 is " + str(X3[1]) + ". The coefficient of a3 is " + str(X3[2]) + "\n")
#We need to find the corresponding variance for each of the coefficients
#First order
Of1 = np.sum([X1+1]*Yxx[:2])
#Second order
Of2 = 1*Yxx[0]+X2[0]*Yxx[1]+X2[1]*0
#Third order
Of3 = 1*Yxx[0]+X3[0]*Yxx[1]+X3[1]*0+X3[2]*0
print("The variance of the first order is " + str(Of1) + ". The variance of the second order is " + str(Of2) + ". The variance of the theird order is " + str(Of3) +  "\n")

#Oppgave 2d)
#Find the expression of the PSD of the AR model

#First order
f = np.linspace(0,0.5,100)
denominatorOfRff1 = np.zeros(len(f))
for i in range(len(f)):
    sum = (X1) * np.e**(-1j*2*np.pi*f[i])
    denominatorOfRff1[i] = np.abs((1+sum))**2
Rff1 = Of1 / denominatorOfRff1
#Second order
denominatorOfRff2 = np.zeros(len(f))
for i in range(len(f)):
    sum = (X2[0]) * np.e**(-1j*2*np.pi*f[i])+ (X2[1]) * np.e**(-1j*2*np.pi*f[i]*2)
    denominatorOfRff2[i] = np.abs((1+sum))**2
Rff2 = Of2 / denominatorOfRff2
#Third order
denominatorOfRff3 = np.zeros(len(f))
for i in range(len(f)):
    sum = (X3[0]) * np.e**(-1j*2*np.pi*f[i]) + (X3[1]) * np.e**(-1j*2*np.pi*f[i]*2) + (X3[2]) * np.e**(-1j*2*np.pi*f[i]*3)
    denominatorOfRff3[i] = np.abs((1+sum))**2
Rff3 = Of3 / denominatorOfRff3

#The actual PSD found in task 2b)
TrueRff = -0.8*np.cos(2*np.pi*f)+1.16
#Plotting the PSD
# Create a single figure with three subplots
fig, axes = plt.subplots(3, 1, figsize=(6, 12))

# Plot each data in a separate subplot
axes[0].plot(f, Rff1, label="First order")
axes[0].plot(f, np.abs(TrueRff), color='red', label="True PSD")
axes[0].set_xlabel("Frequency")
axes[0].set_ylabel("PSD")
axes[0].legend()

axes[1].plot(f, Rff2, label="Second order")
axes[1].plot(f, TrueRff, color='red', label="True PSD")
axes[1].set_xlabel("Frequency")
axes[1].set_ylabel("PSD")
axes[1].legend()

axes[2].plot(f, Rff3, label="Third order")
axes[2].plot(f, TrueRff, color='red', label="True PSD")
axes[2].set_xlabel("Frequency")
axes[2].set_ylabel("PSD")
axes[2].legend()

plt.tight_layout()  # Ensures subplots don't overlap
plt.show()