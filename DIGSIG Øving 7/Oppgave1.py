import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.signal
from scipy.signal import lfilter
from scipy.signal import welch
from scipy.signal import periodogram

K_values = [10, 100]  # Segment sizes
N = 20000  # Replace with your desired value of N

g = np.random.randn(N)
u = np.sqrt(3) * (2 * np.random.rand(1, N) - 1)
b = 2 * (np.random.rand(1, N) > 0.5) - 1

# Create an array for x-axis values
x = np.arange(1, N + 1)
# Compute autocorrelation for g
autocorr_g = np.correlate(g, g, mode='full') / (N * np.var(g))

# Compute autocorrelation for u
autocorr_u = np.correlate(u[0], u[0], mode='full') / (N * np.var(u))

# Compute autocorrelation for b
autocorr_b = np.correlate(b[0], b[0], mode='full') / (N * np.var(b))

# Theoretical autocorrelation values
theoretical_autocorr_g = np.zeros(2 * N - 1)  # For Gaussian white noise
theoretical_autocorr_u = np.zeros(2 * N - 1)  # For u
theoretical_autocorr_b = np.zeros(2 * N - 1)  # For b
#Task 2c)

H_ZTOP = [1.0]
H_ZDOWN = [1.0,0.5]

n = np.zeros(39999)
#White noice:
# Generate white Gaussian noise
sigma = np.sqrt(3/4)
w = np.random.normal(0, sigma, N)

autocorr_w = np.correlate(w, w, mode='full') / (N * np.var(w))

#I fill filter the randome gaussan correleted white noice
x = lfilter([1], H_ZDOWN, w)

#Task3a)
K = 20

# Initialize an array to store the mean estimates
mean_estimates = []

# Repeat the mean calculation for 200 segments
for i in range(200):
    # Extract a segment of length K from the signal x
    segment = x[i * K: (i + 1) * K]
    
    # Calculate the mean of the segment
    segment_mean = np.mean(segment)
    
    # Append the mean estimate to the list
    mean_estimates.append(segment_mean)


num_bins = 20
# Create a histogram of the mean estimates

# Estimate the mean of the mean estimates
estimated_mean = np.mean(mean_estimates)

# Estimate the variance of the mean estimates
estimated_variance = np.var(mean_estimates)

# Display the results
# print(f'Estimated Mean: {estimated_mean}')
# print(f'Estimated Variance: {estimated_variance}')


#Task 3d)
# Define the segment lengths
K_values = [20, 40, 100]

for K in K_values:
    # Extract the mean estimates for the specific segment length K
    segment_mean_estimates = mean_estimates[K // 20 - 1 :: K // 20]

    # Estimate the mean of the mean estimates
    estimated_mean = np.mean(segment_mean_estimates)

    # Estimate the variance of the mean estimates
    estimated_variance = np.var(segment_mean_estimates)

    # Display the results for the current segment length
    print(f'For K = {K}:')
    print(f'Estimated Mean: {estimated_mean}')
    print(f'Estimated Variance: {estimated_variance}')
    print()
# plt.hist(mean_estimates, bins=num_bins, edgecolor='k')

# # Label the axes and add a title
# plt.xlabel('Mean Estimate')
# plt.ylabel('Frequency')
# plt.title('Histogram of Mean Estimates')

# # Display the histogram
# plt.grid(True)  # Add grid lines

# # Show the plot
# plt.show()




# # Plot the autocorrelation function
# plt.figure(figsize=(10, 5))
# plt.subplot(121)
# plt.title('Autocorrelation Function (Theoretical and Estimated)')
# plt.stem(lags, autocorr_estimated[N-11:N+10], 'ro--', label='Estimated')
# plt.stem(lags,autocorr_w[N-11:N+10],label = "Theory")
# plt.xlabel('Lag')
# plt.ylabel('Autocorrelation')
# plt.legend()

# # Plot the power density spectrum
# plt.subplot(122)
# plt.title('Power Density Spectrum')
# plt.semilogy(frequencies, power_density, 'b')
# plt.xlabel('Frequency')
# plt.ylabel('Power Density')
# plt.tight_layout()

# plt.show()



# # Plot the autocorrelation functions
# # plt.figure(figsize=(12, 6))

# # plt.subplot(131)
# # plt.plot(np.arange(-N + 1, N), autocorr_g)
# # plt.title("Autocorrelation for g")

# # plt.subplot(132)
# # plt.plot(np.arange(-N + 1, N), autocorr_u)
# # plt.title("Autocorrelation for u")

# # plt.subplot(133)
# # plt.plot(np.arange(-N + 1, N), autocorr_b)
# # plt.title("Autocorrelation for b")

# # plt.show()



# #Task 1c)
# # Compute sample mean for g
# mean_g = np.mean(g)

# # Compute sample mean for u
# mean_u = np.mean(u)

# # Compute sample mean for b
# mean_b = np.mean(b)

# # Theoretical means
# theoretical_mean_g = 0  # For Gaussian white noise
# theoretical_mean_u = 0  # For u
# theoretical_mean_b = 0  # For b

# # Print and compare the means
# print("Sample Mean for g:", mean_g)
# print("Theoretical Mean for g:", theoretical_mean_g)

# print("Sample Mean for u:", mean_u)
# print("Theoretical Mean for u:", theoretical_mean_u)

# print("Sample Mean for b:", mean_b)
# print("Theoretical Mean for b:", theoretical_mean_b)

# # Plot g, u, and b as discrete points using plt.stem
# plt.stem(x, g, linefmt='C0-', markerfmt='C0o', label='g', basefmt='C0-')
# plt.stem(x, u[0], linefmt='C1-', markerfmt='C1o', label='u', basefmt='C1-')
# plt.stem(x, b[0], linefmt='C2-', markerfmt='C2o', label='b', basefmt='C2-')

# # Add labels and legend
# plt.xlabel('N')
# plt.ylabel('Values')
# plt.legend()

# # Show the plot
# plt.show()
