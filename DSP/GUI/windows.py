from tkinter import ttk
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tasks.task2.arithmetic_operations import addition, subtraction, multiplication, squaring, shifting, normalization, accumulation
from tasks.task3.quantization import quantization_signal_tst
from tasks.task4.DFT_IDFT import change_time_sig, apply_dft, apply_idft, apply_comp, mod_sig
from tasks.task5.DCT import compute_dct, remove_dc_component
from tasks.task6.signal_manipulation import smoothing, folding, shift_and_fold, remove_dc_component_time_domain
from tasks.task6.DerivativeSignal import DerivativeSignal
from tasks.task7.convolution import convolution_time_domain
from tasks.task8.Correlation import normalizedCrossCorrelation
from tasks.task9.fast import fastConvolution, fastCorrelation
global entry_multiplication_factor,entry_shift_value,combo_normalization_range, entry_shift_value_task6, entry_window_size

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
    
def open_Quantize_window(root):
    Quantize_window = tk.Toplevel(root)
    Quantize_window.title("Quantize Operations")
    Quantize_window.geometry("400x250")

    # Create labels and entry field
    label_bits_levels_number = tk.Label(Quantize_window, text="Number of (bits/levels):")
    label_bits_levels_number.pack()
    entry_bits_levels_number = tk.Entry(Quantize_window)
    entry_bits_levels_number.pack()

    # Type selection
    type_var = tk.StringVar()
    bits_option = ttk.Radiobutton(Quantize_window, text="Bits", variable=type_var, value="bits")
    bits_option.pack()
    levels_option = ttk.Radiobutton(Quantize_window, text="Levels", variable=type_var, value="levels")
    levels_option.pack()

    # test1 button
    btn_test_1 = tk.Button(Quantize_window, text="test1", command=lambda: quantization_signal_tst(entry_bits_levels_number, type_var))
    btn_test_1.pack(pady=10)
    # test2 button
    btn_test_2 = tk.Button(Quantize_window, text="test2", command=lambda: quantization_signal_tst(entry_bits_levels_number, type_var))
    btn_test_2.pack(pady=10)

def open_IDF_IDFT_window(root):
    # initializing the window
    IDF_IDFT_window = tk.Toplevel(root)
    IDF_IDFT_window.title("IDF_IDFT Operations")
    IDF_IDFT_window.geometry("1000x530")
    
    # frequency entry
    freq_lable = ttk.Label(IDF_IDFT_window, text="Frequency :", font=15)
    freq_lable.grid(column=0, row=0,sticky='e')
    freq_entry = tk.Entry(IDF_IDFT_window)
    freq_entry.grid(column=1, row=0,sticky='w')
    
    tORf_sig= []
    x=[]

    def change_time_sig_button(x, tORf_sig, figures, canvass):
        x, tORf_sig = change_time_sig(x, tORf_sig, figures, canvass)
    
    get_time_sig = tk.Button(IDF_IDFT_window, text="Get Signal",command=lambda: change_time_sig_button(x, tORf_sig, figures, canvass))
    get_time_sig.grid(row=1, column=0)
    apply_fur = tk.Button(IDF_IDFT_window, text="Apply DFT",command=lambda: apply_dft(tORf_sig,freq_entry,figures,canvass))
    apply_fur.grid(row=1, column=1)
    apply_fur_idft = tk.Button(IDF_IDFT_window, text="Apply IDFT",command=lambda: apply_idft(x,tORf_sig,figures,canvass))
    apply_fur_idft.grid(row=1, column=2)
    apply_fur_idft = tk.Button(IDF_IDFT_window, text="Compare",command=lambda: apply_comp())
    apply_fur_idft.grid(row=0, column=2)
    
    figures = [Figure(figsize=(5, 4), dpi=65) for _ in range(3)]
    for fig in figures:
        a = fig.add_subplot(111)
        a.plot(0, 0)
    canvass = [FigureCanvasTkAgg(figure, IDF_IDFT_window) for figure in figures]
    for idx,canvas in enumerate(canvass):
        canvas.get_tk_widget().grid(row=4,column=idx)
    
    mod_amp = ttk.Label(IDF_IDFT_window, text="Amplitude :", font=15)
    mod_amp.grid(column=0, row=5,sticky='e')
    mod_amp_entry = tk.Entry(IDF_IDFT_window)
    mod_amp_entry.grid(column=1, row=5,sticky='w')
    mod_phase = ttk.Label(IDF_IDFT_window, text="Phase Shift :", font=15)
    mod_phase.grid(column=0, row=6,sticky='e')
    mod_phase_entry = tk.Entry(IDF_IDFT_window)
    mod_phase_entry.grid(column=1, row=6,sticky='w')
    mod_idx = ttk.Label(IDF_IDFT_window, text="Number :", font=15)
    mod_idx.grid(column=0, row=7,sticky='e')
    mod_idx_entry = tk.Entry(IDF_IDFT_window)
    mod_idx_entry.grid(column=1, row=7,sticky='w')
    apply_mod = tk.Button(IDF_IDFT_window, text="Apply Modification"
                        ,command=lambda: mod_sig(mod_amp_entry,mod_phase_entry,mod_idx_entry,x,tORf_sig,freq_entry,figures,canvass))
    apply_mod.grid(row=6, column=2,sticky='w')
    
    # Text field for DCT result
    dct_result_entry = tk.Entry(IDF_IDFT_window)
    dct_result_entry.grid(row=8, column=1, pady=10)
    
    # Add "Compute DCT" button and text field in the same row
    compute_dct_button = tk.Button(IDF_IDFT_window, text="Compute DCT", command=lambda: compute_dct(int(dct_result_entry.get()), figures, canvass))
    compute_dct_button.grid(row=8, column=0, pady=10)
    
    # Add "Remove DC component" button
    remove_dc_button = tk.Button(IDF_IDFT_window, text="Remove DC component", command=lambda: remove_dc_component())
    remove_dc_button.grid(row=10, column=0, columnspan=3, pady=10)
    
def open_Time_Domain_window(root):
    # initializing the window
    Time_Domain_window = tk.Toplevel(root)
    Time_Domain_window.title("Time Domain Operations")
    Time_Domain_window.geometry("400x600")
    
    # Smoothing
    frame_smoothing = tk.Frame(Time_Domain_window)
    frame_smoothing.pack(pady=10)
    entry_window_size = tk.Entry(frame_smoothing)
    entry_window_size.pack(side=tk.LEFT, padx=5)
    smoothing_btn = tk.Button(frame_smoothing, text="smoothing", command=lambda: smoothing(int(entry_window_size.get())))
    smoothing_btn.pack(side=tk.LEFT, padx=5, pady=10)
    
    # Sharpening
    frame_sharpening = tk.Frame(Time_Domain_window)
    frame_sharpening.pack(pady=10)
    sharpening_btn = tk.Button(frame_sharpening, text="Sharpening", command=DerivativeSignal)
    sharpening_btn.pack()
    
    # Shifting
    frame_shifting = tk.Frame(Time_Domain_window)
    frame_shifting.pack(pady=10)
    btn_shift = tk.Button(frame_shifting, text="Shift", command=lambda: shifting(float(entry_shift_value_task6.get())))
    btn_shift.pack(side=tk.LEFT, padx=5)
    label_shift_factor = tk.Label(frame_shifting, text="Shift by:")
    label_shift_factor.pack(side=tk.LEFT, padx=5)
    entry_shift_value_task6 = tk.Entry(frame_shifting)
    entry_shift_value_task6.pack(side=tk.LEFT, padx=5)
    
    # Folding
    frame_folding = tk.Frame(Time_Domain_window)
    frame_folding.pack(pady=10)
    btn_folding = tk.Button(frame_folding, text="Folding", command=folding)
    btn_folding.pack(side=tk.LEFT, padx=5)
    
    # Shift and Fold
    frame_shifting_folding = tk.Frame(Time_Domain_window)
    frame_shifting_folding.pack(pady=10)
    btn_shift = tk.Button(frame_shifting_folding, text="Shift and Fold", command=lambda: shift_and_fold(int(entry_shift_fold_value_task6.get())))
    btn_shift.pack(side=tk.LEFT, padx=5)
    label_shift_factor = tk.Label(frame_shifting_folding, text="Shift by:")
    label_shift_factor.pack(side=tk.LEFT, padx=5)
    entry_shift_fold_value_task6 = tk.Entry(frame_shifting_folding)
    entry_shift_fold_value_task6.pack(side=tk.LEFT, padx=5)
    
    # Add "Remove DC component" button
    frame_remove_dc = tk.Frame(Time_Domain_window)
    frame_remove_dc.pack(pady=10)
    remove_dc_button = tk.Button(frame_remove_dc, text="Remove DC component", command=lambda: remove_dc_component_time_domain())
    remove_dc_button.grid(row=10, column=0, columnspan=3, pady=10)
    
    # Add "Convolution" button
    frame_convolution = tk.Frame(Time_Domain_window)
    frame_convolution.pack(pady=10)
    convolution_button = tk.Button(frame_convolution, text="Convolute", command=lambda: convolution_time_domain())
    convolution_button.pack()
    
    # Add "Correlation" button
    frame_correlation = tk.Frame(Time_Domain_window)
    frame_correlation.pack(pady=10)
    correlation_button = tk.Button(frame_correlation, text="Correlation", command=lambda: normalizedCrossCorrelation())
    correlation_button.pack()
    
    # Add "Fast Convolution" button
    frame_fast_Convolution = tk.Frame(Time_Domain_window)
    frame_fast_Convolution.pack(pady=10)
    fast_Convolution_button = tk.Button(frame_fast_Convolution, text="Fast Convolution", command=lambda: fastConvolution())
    fast_Convolution_button.pack()
    
    # Add "Fast Correlation" button
    frame_fast_correlation = tk.Frame(Time_Domain_window)
    frame_fast_correlation.pack(pady=10)
    fast_correlation_button = tk.Button(frame_fast_correlation, text="Fast Correlation", command=lambda: fastCorrelation())
    fast_correlation_button.pack()
