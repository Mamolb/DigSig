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
print("The variance of the first order is " + str(Of1) + ". The variance of the second order is " + str(Of2) + ". The variance of the theird order is " + str(Of3)+ "\n")
