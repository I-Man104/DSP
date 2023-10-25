from tkinter import filedialog, messagebox, ttk
import tkinter as tk
from signal_processing import get_datasets, generate_signal, plot_signals
from arithmetic_operations import addition, subtraction, multiplication, squaring, shifting, normalization, accumulation
global var_signal_type, entry_amplitude, entry_phase_shift, entry_analog_frequency, entry_sampling_frequency,entry_multiplication_factor,entry_shift_value,combo_normalization_range

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

def open_arithmetic_window(root):
    arithmetic_window = tk.Toplevel(root)
    arithmetic_window.title("Arithmetic Operations")
    arithmetic_window.geometry("500x450")
    
    # Addition
    frame_addition = tk.Frame(arithmetic_window)
    frame_addition.pack(pady=10)
    btn_addition = tk.Button(frame_addition, text="Addition", command=addition)
    btn_addition.pack(side=tk.LEFT, padx=5)
    
    # Subtraction
    frame_subtraction = tk.Frame(arithmetic_window)
    frame_subtraction.pack(pady=10)
    btn_subtraction = tk.Button(frame_subtraction, text="Subtraction", command=subtraction)
    btn_subtraction.pack(side=tk.LEFT, padx=5)

    # Multiplication
    frame_multiplication = tk.Frame(arithmetic_window)
    frame_multiplication.pack(pady=10)
    entry_multiplication_factor = tk.Entry(frame_multiplication)
    entry_multiplication_factor.pack(side=tk.LEFT, padx=5)
    btn_multiplication = tk.Button(frame_multiplication, text="Multiply", command=lambda: multiplication(float(entry_multiplication_factor.get())))
    btn_multiplication.pack(side=tk.LEFT, padx=5)

    # Squaring
    frame_squaring = tk.Frame(arithmetic_window)
    frame_squaring.pack(pady=10)
    btn_squaring = tk.Button(frame_squaring, text="Squaring", command=squaring)
    btn_squaring.pack(side=tk.LEFT, padx=5)
    
    # Shifting
    frame_shifting = tk.Frame(arithmetic_window)
    frame_shifting.pack(pady=10)
    btn_shift = tk.Button(frame_shifting, text="Shift", command=lambda: shifting(float(entry_shift_value.get())))
    btn_shift.pack(side=tk.LEFT, padx=5)

    frame_shifting.pack(pady=10)
    label_shift_factor = tk.Label(frame_shifting, text="Shift by:")
    label_shift_factor.pack(side=tk.LEFT, padx=5)
    entry_shift_value = tk.Entry(frame_shifting)
    entry_shift_value.pack(side=tk.LEFT, padx=5)

    # Normalization
    frame_normalization = tk.Frame(arithmetic_window)
    frame_normalization.pack(pady=10)
    btn_normalization = tk.Button(frame_normalization, text="Normalization", command=lambda: normalization(combo_normalization_range.get()))
    btn_normalization.pack(side=tk.LEFT, padx=5)
    normalization_options = ["0 to 1", "-1 to 1"]
    combo_normalization_range = ttk.Combobox(frame_normalization, values=normalization_options, state="readonly")
    combo_normalization_range.set(normalization_options[0])  # Setting default value to "0 to 1"
    combo_normalization_range.pack(side=tk.LEFT, padx=5)

    # Accumulation
    frame_accumulation = tk.Frame(arithmetic_window)
    frame_accumulation.pack(pady=10)
    btn_accumulation = tk.Button(frame_accumulation, text="Accumulation", command=accumulation)
    btn_accumulation.pack(side=tk.LEFT, padx=5)

def create_interface(root):
    global var_signal_type, entry_amplitude, entry_phase_shift, entry_analog_frequency, entry_sampling_frequency

    root.geometry("400x450")
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
    
    # Add the Arithmetic Operations button that opens a new window
    btn_arithmetic = tk.Button(root, text="Arithmetic Operations", command=lambda: open_arithmetic_window(root))
    btn_arithmetic.pack(pady=20)
