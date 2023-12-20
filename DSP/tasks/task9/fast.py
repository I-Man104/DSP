from tests.conv_test import ConvTest
from tests.CompareSignal_corr import Compare_Signals
from signal_processing import get_datasets
from tasks.task4.DFT_IDFT import DFT,IDFT
import matplotlib.pyplot as plt
import cmath
import numpy as np
def plot_signal(x, y, title='Signal'):
    plt.figure()  # Create a new figure

    plt.subplot(2, 1, 2)  # Plot the continuous signal
    plt.plot(x, y)
    plt.title('Continuous Signal')
    plt.subplot(2, 1, 1)  # Plot the discrete signal
    plt.stem(x, y)
    plt.title('Discrete Signal')

    plt.show()


def fastConvolution():
    indecies_1 = []
    indecies_2 = []
    sample_1 = []
    sample_2 = []
    
    datasets,domain = get_datasets()
    indecies_1[:] = datasets[0][0]
    indecies_2[:] = datasets[1][0]
    sample_1[:]= datasets[0][1]
    sample_2[:] = datasets[1][1]
    
    result_indices, result_samples = conv(indecies_1, sample_1, indecies_2, sample_2)
    
    print(result_indices, result_samples)
    
    ConvTest(result_indices, result_samples)
    plot_signal(result_indices, result_samples)

def conv(indecies_1, sample_1, indecies_2, sample_2):
    # Apply zero paddings for each signal
    l1 = len(indecies_1)
    l2 = len(indecies_2)
    last1 = indecies_1[l1 - 1] + 1
    last2 = indecies_2[l2 - 1] + 1

    for i in range(l2 - 1):
        indecies_1.append(last1 + i)
        sample_1.append(0)
    for i in range(l1 - 1):
        indecies_2.append(last2 + i)
        sample_2.append(0)

    for i in range(l1 + l2 - 1):
        indecies_1[i] = i
        indecies_2[i] = i

    # Compute the Discrete Fourier Transform (DFT) of signal1 and signal2
    A1,phase1,N1 = DFT(sample_1)
    A2,phase2,N2 = DFT(sample_2)

    # Convert amplitude and phase to rectangular form for signal1
    for i in range(N1):
        A = A1[i]
        phase = phase1[i]
        sample_1[i] = [cmath.rect(A, phase)]

    # Convert amplitude and phase to rectangular form for signal2
    for i in range(N2):
        A = A2[i]
        phase = phase2[i]
        sample_2[i] = [cmath.rect(A, phase)]

    # Compute the cross-correlation in the frequency domain
    cross_correlation_freq = np.multiply([val for val in sample_1], [val for val in sample_2])
    
    # Convert the cross-correlation to amplitude and phase
    amps = []
    phases = []
    for s in cross_correlation_freq:
        amps.append(abs(s))
        phases.append(cmath.phase(s))

    # Compute the Inverse Discrete Fourier Transform (IDFT) to get the cross-correlation in time domain
    cross_correlation_time = IDFT(amps,phases)

    start_index = -(l1 - 1)
    output_index = np.arange(start_index, start_index + len(cross_correlation_time)) + 1

    # Return the indices and correlated signal
    return output_index, cross_correlation_time

def fastCorrelation():
    indecies_1 = []
    indecies_2 = []
    sample_1 = []
    sample_2 = []
    datasets,domain = get_datasets()
    indecies_1[:] = datasets[0][0]
    indecies_2[:] = datasets[1][0]
    sample_1[:]= datasets[0][1]
    sample_2[:] = datasets[1][1]
    
    result_indecies, result_samples = corr(sample_1, sample_2)
    
    Compare_Signals("test_cases (output)/task9/Corr_Output.txt",result_indecies,result_samples)
    plot_signal(indecies_1, result_samples)
    
def corr(sample_1, sample_2):
    # Compute the Discrete Fourier Transform (DFT) of signal1 and signal2
    A1,phase1,N1 = DFT(sample_1)
    A2,phase2,N2 = DFT(sample_2)
    
        # Convert amplitude and phase to rectangular form for signal1
    for i in range(N1):
        A = A1[i]
        phase = phase1[i]
        sample_1[i] = [i, cmath.rect(A, phase)]

    # Convert amplitude and phase to rectangular form for signal2
    for i in range(N2):
        A = A2[i]
        phase = phase2[i]
        sample_2[i] = [i, cmath.rect(A, phase)]

    # Compute the cross-correlation in the frequency domain
    cross_correlation_freq = np.conjugate([val[1] for val in sample_1]) * [val[1] for val in sample_2]

    # Convert the cross-correlation to amplitude and phase
    amps = []
    phases = []
    for s in cross_correlation_freq:
        amps.append(abs(s))
        phases.append(cmath.phase(s))

    # Compute the Inverse Discrete Fourier Transform (IDFT) to get the cross-correlation in time domain
    cross_correlation_time = IDFT(amps,phases)

    # Normalize
    normalizedSignal = [(1 / len(cross_correlation_time)) * s for s in cross_correlation_time]

    indecies = []
    for i in range(len(normalizedSignal)):
        indecies.append(i)
    
    # Return the indices and the normalized cross-correlation signal
    return indecies, normalizedSignal