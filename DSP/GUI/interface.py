from tkinter import messagebox, ttk
import tkinter as tk
from GUI.windows import open_arithmetic_window, open_Quantize_window, open_IDF_IDFT_window, open_Time_Domain_window
from tasks.task1.generate_signals import on_open_file, on_generate
def create_interface(root):
    global var_signal_type, entry_amplitude, entry_phase_shift, entry_analog_frequency, entry_sampling_frequency

    root.geometry("400x550")
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
    btn_arithmetic.pack()
    
    # Add the Quantize Operations button that opens a new window
    btn_quantization = tk.Button(root, text="Quantization", command=lambda: open_Quantize_window(root))
    btn_quantization.pack()
    
    # Add the Frequency Domain button that opens a new window
    btn_frequency_domain = tk.Button(root, text="Frequency Domain", command=lambda: open_IDF_IDFT_window(root))
    btn_frequency_domain.pack()
    
    # Add the IDF_IDFT button that opens a new window
    btn_time_domain = tk.Button(root, text="Time Domain", command=lambda: open_Time_Domain_window(root))
    btn_time_domain.pack()
