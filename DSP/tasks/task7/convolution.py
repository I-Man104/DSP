from tests.conv_test import ConvTest
from signal_processing import get_datasets
import matplotlib.pyplot as plt

        

def plot_signal(x, y, title='Signal'):
    plt.figure()  # Create a new figure

    plt.subplot(2, 1, 2)  # Plot the continuous signal
    plt.plot(x, y)
    plt.title('Continuous Signal')
    plt.subplot(2, 1, 1)  # Plot the discrete signal
    plt.stem(x, y)
    plt.title('Discrete Signal')

    plt.show()

def convolution_time_domain():
    indecies_1 = []
    indecies_2 = []
    sample_1 = []
    sample_2 = []
    
    datasets,domain = get_datasets()
    indecies_1[:] = datasets[0][0]
    indecies_2[:] = datasets[1][0]
    sample_1[:]= datasets[0][1]
    sample_2[:] = datasets[1][1]
    
    result_indices, result_samples = convolve_signals(indecies_1,sample_1,indecies_2, sample_2)
    ConvTest(result_indices, result_samples)
    print(result_indices, result_samples)

    plot_signal(result_indices, result_samples)
    
def convolve_signals(signal1_indices, signal1_samples, signal2_indices, signal2_samples):
    m = len(signal1_samples)
    n = len(signal2_samples)
    result = [0] * (m + n - 1)  # Initialize the result array with zeros
    result_indices = [0] * (m + n - 1)  # Initialize the result indices array

    for i in range(m):
        for j in range(n):
            result[i + j] += signal1_samples[i] * signal2_samples[j]
            result_indices[i + j] = signal1_indices[i] + signal2_indices[j]

    return result_indices, result
    
    