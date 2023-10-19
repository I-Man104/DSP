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

def plot_signals(signal1):
    import matplotlib.pyplot as plt
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    ax1.plot(signal1[0], signal1[1])
    ax1.set_title("Signal 1 (Continuous)")

    ax2.stem(signal1[0], signal1[1])
    ax2.set_title("Signal 1 (Discrete)")

    plt.tight_layout()
    plt.show()
