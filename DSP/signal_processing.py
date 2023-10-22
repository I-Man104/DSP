import numpy as np
from tkinter import messagebox
from comparesignals import SignalSamplesAreEqual

def load_signal(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            if line.__contains__(' '):
                values = line.strip().split()
                data.append([float(value) for value in values])
    return np.array(data)

def generate_signal(signal_type, amplitude, phase_shift, analog_frequency, sampling_frequency):
    indecies = np.arange(1, sampling_frequency+1) 
    time = np.arange(sampling_frequency) / sampling_frequency
    omega = 2 * np.pi * analog_frequency
    if signal_type == "Sine Wave":
        signal = amplitude * np.sin(omega * time + phase_shift)
        SignalSamplesAreEqual('./test_cases/SinOutput.txt', time, signal)
    elif signal_type == "Cosine Wave":
        signal = amplitude * np.cos(omega * time + phase_shift)
        SignalSamplesAreEqual('./test_cases/CosOutput.txt', time, signal)
    else:
        messagebox.showerror("Error", "Invalid signal type selected!")
        return

    return indecies, signal

def plot_signals(data_sets):
    import matplotlib.pyplot as plt
    for i, data_set in enumerate(data_sets):
        plt.figure(i+1)  # Create a new figure for each signal
        
        plt.subplot(2, 1, 2)  # Plot the continuous signal
        plt.plot(data_set[0], data_set[1])
        plt.title('Continuous Signal')

        plt.subplot(2, 1, 1)  # Plot the discrete signal
        plt.stem(data_set[0], data_set[1])
        plt.title('Discrete Signal')
        
    plt.tight_layout()
    plt.show()
    