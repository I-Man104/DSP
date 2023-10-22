from tkinter import filedialog, messagebox, ttk
import tkinter as tk
from signal_processing import load_signal, generate_signal, plot_signals

global var_signal_type, entry_amplitude, entry_phase_shift, entry_analog_frequency, entry_sampling_frequency

def on_open_file():
    file_paths = filedialog.askopenfilenames()
    if not file_paths:
        return

    data_sets = []
    for file_path in file_paths:
        data = load_signal(file_path)
        data_sets.append((data[:, 0], data[:, 1]))
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
    
    plot_signals((time, signal1))

def create_interface(root):
    global var_signal_type, entry_amplitude, entry_phase_shift, entry_analog_frequency, entry_sampling_frequency

    root.geometry("400x400")
    root.title("Signal Processing Framework")
    frame = tk.Frame(root)
    frame.pack(pady=20)

    # Create open button
    btn_open = tk.Button(root, text="Open Signal", command=on_open_file)
    btn_open.pack(pady=10)

    # Add items to the Signal Generation menu
    var_signal_type = tk.StringVar()
    var_signal_type.set("Sine Wave")  # Default signal type
    
    # Create a combo box for signal type selection
    combo_signal_type = ttk.Combobox(root, textvariable=var_signal_type, values=["Sine Wave", "Cosine Wave"], state="readonly")
    combo_signal_type.pack()
    
    # Create labels and entry fields for signal parameters
    label_amplitude = tk.Label(root, text="Amplitude:")
    label_amplitude.pack()
    entry_amplitude = tk.Entry(root)
    entry_amplitude.pack()

    label_phase_shift = tk.Label(root, text="Phase Shift:")
    label_phase_shift.pack()
    entry_phase_shift = tk.Entry(root)
    entry_phase_shift.pack()

    label_analog_frequency = tk.Label(root, text="Analog Frequency:")
    label_analog_frequency.pack()
    entry_analog_frequency = tk.Entry(root)
    entry_analog_frequency.pack()

    label_sampling_frequency = tk.Label(root, text="Sampling Frequency:")
    label_sampling_frequency.pack()
    entry_sampling_frequency = tk.Entry(root)
    entry_sampling_frequency.pack()

    # Create the Generate button
    btn_generate = tk.Button(root, text="Generate Signal", command=on_generate)
    btn_generate.pack(pady=20)

    # Create a menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
