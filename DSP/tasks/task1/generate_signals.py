from tkinter import messagebox
from signal_processing import get_datasets, generate_signal, plot_signals
global var_signal_type, entry_amplitude, entry_phase_shift, entry_analog_frequency, entry_sampling_frequency

def on_open_file():
    data_sets = get_datasets()
    plot_signals(data_sets)

def on_generate():
    signal_type = var_signal_type.get()
    amplitude = float(entry_amplitude.get())
    phase_shift = float(entry_phase_shift.get())
    analog_frequency = float(entry_analog_frequency.get())
    sampling_frequency = float(entry_sampling_frequency.get())

    if sampling_frequency < 2 * analog_frequency:
        messagebox.showwarning("Warning", "Sampling frequency should be at least twice the analog frequency")
        return
    
    if sampling_frequency == 0:
        messagebox.showwarning("Warning", "Sampling frequency should be bigger than 0")
        return
    
    time, signal1 = generate_signal(signal_type, amplitude, phase_shift, analog_frequency, sampling_frequency)
    
    plot_signals([(time, signal1)])
