import numpy as np
from tkinter import messagebox, filedialog
from tests.comparesignals import SignalSamplesAreEqual

def load_signal(file_path):
    with open(file_path, 'r') as file:
        print("File selected:", file_path)
        # the domain is a time domain by default
        domain = 'time'
        iteration = 0
        lines = file.readlines()
        data = []
        for line in lines:
            # check second row
            if iteration == 1 and float(line) == 1:
                domain = 'frequency'
            
            # check the signal
            elif iteration > 2:
                values = []
                if domain == 'time':
                    values = line.strip().split()
                elif domain == 'frequency':
                    if line.__contains__(' '):
                        values = line.strip().replace('f', '').split(' ')
                    elif line.__contains__(','):
                        values = line.strip().replace('f', '').split(',')
                data.append([float(value) for value in values])
            iteration = iteration + 1
    
    return np.array(data), domain

def get_datasets():
    file_paths = filedialog.askopenfilenames()
    if not file_paths:
        return
    if len(file_paths) == 1:
        data, domain = load_signal(file_paths[0])
        return [data[:, 0], data[:, 1]],domain
    data_sets = []
    for file_path in file_paths:
        data, domain = load_signal(file_path)
        x_values = data[:, 0]
        y_values = data[:, 1]
        data_sets.append((x_values, y_values))
    return data_sets, domain

def generate_signal(signal_type, amplitude, phase_shift, analog_frequency, sampling_frequency):
    indecies = np.arange(1, sampling_frequency+1) 
    time = np.arange(sampling_frequency) / sampling_frequency
    omega = 2 * np.pi * analog_frequency
    if signal_type == "Sine Wave":
        signal = amplitude * np.sin(omega * time + phase_shift)
        SignalSamplesAreEqual('./test_cases/task1/SinOutput.txt', time, signal)
    elif signal_type == "Cosine Wave":
        signal = amplitude * np.cos(omega * time + phase_shift)
        SignalSamplesAreEqual('./test_cases/task1/CosOutput.txt', time, signal)
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
    