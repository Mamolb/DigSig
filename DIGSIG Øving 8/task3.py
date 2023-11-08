#Going to make a vovel recognition program
#The program should take your voice as input and then transform it into a dirfferent vovel

import numpy as np
import scipy.io
import scipy.signal
import soundfile as sf

#First we get the data from the file
data = scipy.io.loadmat('vowels.mat')
norwegian_vowels = data['v'][0]
fs = int(data['fs'][0][0])
#We now need a desiered vovel
desired_vowel_index = 0
desired_norwegian_vowel = norwegian_vowels[desired_vowel_index]
#We now need to get the coefficents of the vovel
#Function the get teh coefficents
def ar_coefficients(signal, order=10):
    a = np.zeros(order + 1)
    e = np.zeros(order + 1)
    r = np.zeros(order + 1)
    
    for m in range(order + 1):
        r[m] = np.dot(signal[m:], signal[:-m] if m != 0 else signal)
    
    a[0] = 1.0
    e[0] = r[0]
    for k in range(1, order + 1):
        lambda_val = -np.dot(a[:k], r[k:0:-1]) / e[k-1]
        a[1:k+1] = a[1:k+1] + lambda_val * np.flip(a[:k])
        a[k] = lambda_val
        e[k] = (1 - lambda_val**2) * e[k-1]
    
    return a[1:]

coeff_desired_vowel = ar_coefficients(desired_norwegian_vowel.ravel())

#We need to get the coefficents of the input vovel
input_vowel, input_fs = sf.read('vowel2.wav')
coeff_input_vowel = ar_coefficients(input_vowel.ravel())
#To get the noice we need to use the recording of the wovel in my voice through the inverse filer 
#With coefficents of the input vowel

#We now need to get the noice from the inverse-filter
inverseFilterOfOwnNoice = coeff_input_vowel
#We need to get the noice
noice = scipy.signal.lfilter(inverseFilterOfOwnNoice, [1], input_vowel)
#the final part is to take this noice and filter it with the coefficents of the desired vowel
#This will give us the transformed vowel
desiredNorwegianVowelSound = scipy.signal.lfilter([1],coeff_desired_vowel, noice)
#We need to normalize the sound
desiredNorwegianVowelSound = desiredNorwegianVowelSound / np.abs(desiredNorwegianVowelSound).max()
#We then need to play the sound
sf.write('transformed_vowel.wav', desiredNorwegianVowelSound, fs)




