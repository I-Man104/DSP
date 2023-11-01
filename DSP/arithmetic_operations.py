from tkinter import messagebox, filedialog
from signal_processing import get_datasets, plot_signals
from scipy.interpolate import interp1d
import numpy as np
import math

from task_2_test import AddSignalSamplesAreEqual, SubSignalSamplesAreEqual, MultiplySignalByConst, ShiftSignalByConst, NormalizeSignal, SignalSamplesAreEqual
from task_3_test import QuantizationTest1, QuantizationTest2
# Addition
def add_signals(signal1, signal2):
    x_values1, y_values1 = signal1
    x_values2, y_values2 = signal2

    # Find the common range for x values
    min_x = max(min(x_values1), min(x_values2))
    max_x = min(max(x_values1), max(x_values2))

    # Interpolate the shorter signal to match the length of the longer one
    f1 = interp1d(x_values1, y_values1, kind='linear', fill_value=0, bounds_error=False)
    f2 = interp1d(x_values2, y_values2, kind='linear', fill_value=0, bounds_error=False)

    x_values = np.linspace(min_x, max_x, num=max(len(x_values1), len(x_values2)), endpoint=True)
    y_values_sum = f1(x_values) + f2(x_values)

    return (x_values, y_values_sum)

def addition():
    datasets = get_datasets()
    
    if len(datasets) != 2:
        print("Please select exactly two signals.")
        return

    # Add the first two signals
    sum_signal = add_signals(datasets[0], datasets[1])
    
    # test Addition
    # AddSignalSamplesAreEqual('Signal1.txt','Signal2.txt',sum_signal[0],sum_signal[1])
    AddSignalSamplesAreEqual('Signal1.txt','Signal3.txt',sum_signal[0],sum_signal[1])
    
    # Plot the original signals and the sum
    plot_signals(datasets + [sum_signal])

# Subtraction
def subtract_signals(signal1, signal2):
    x_values1, y_values1 = signal1
    x_values2, y_values2 = signal2

    # Find the common range for x values
    min_x = max(min(x_values1), min(x_values2))
    max_x = min(max(x_values1), max(x_values2))

    # Interpolate the shorter signal to match the length of the longer one
    f1 = interp1d(x_values1, y_values1, kind='linear', fill_value=0, bounds_error=False)
    f2 = interp1d(x_values2, y_values2, kind='linear', fill_value=0, bounds_error=False)

    x_values = np.linspace(min_x, max_x, num=max(len(x_values1), len(x_values2)), endpoint=True)
    y_values_diff = f1(x_values) - f2(x_values)

    return (x_values, y_values_diff)

def subtraction():
    datasets = get_datasets()

    if len(datasets) != 2:
        print("Please select exactly two signals.")
        return

    # Subtract the first signal from the second signal
    diff_signal = subtract_signals(datasets[1], datasets[0])
    
    # test Subtraction
    # SubSignalSamplesAreEqual('Signal1.txt','Signal2.txt',diff_signal[0],diff_signal[1])
    SubSignalSamplesAreEqual('Signal1.txt','Signal3.txt',diff_signal[0],diff_signal[1])

    # Plot the original signals and the difference
    plot_signals(datasets + [diff_signal])

# Multiplication
def multiplication(factor):
    datasets = get_datasets()

    if len(datasets) != 1:
        print("Please select exactly one signal.")
        return

    original_signal = datasets[0]
    multiplied_signal = (original_signal[0], original_signal[1] * factor)
    
    # test Multiplication
    MultiplySignalByConst(factor, multiplied_signal[0], multiplied_signal[1])

    # Plot the original signal and the multiplied signal
    plot_signals([original_signal, multiplied_signal])

# Squaring
def squaring():
    datasets = get_datasets()

    if len(datasets) != 1:
        print("Please select exactly one signal.")
        return

    original_signal = datasets[0]
    squared_signal = (original_signal[0], [y ** 2 for y in original_signal[1]])

    # test Squaring
    SignalSamplesAreEqual('SQU', './test_cases/task2/output squaring signal 1.txt', squared_signal[0], squared_signal[1])

    # Plot the original signal and the squared signal
    plot_signals([original_signal, squared_signal])

# Shifting
def shifting(shift_value):
    datasets = get_datasets()

    if len(datasets) != 1:
        print("Please select exactly one signal.")
        return

    original_signal = datasets[0]
    shifted_signal = (original_signal[0] - shift_value, original_signal[1])

    # test Shifting
    ShiftSignalByConst(shift_value, shifted_signal[0], shifted_signal[1])

    # Plot the original signal and the shifted signal
    plot_signals([original_signal, shifted_signal])

# Normalization
def normalization(normalize_option):
    MinRange = 0
    MaxRange = 1
    
    datasets = get_datasets()

    if len(datasets) != 1:
        print("Please select exactly one signal.")
        return

    original_signal = datasets[0]

    if normalize_option == "0 to 1":
        min_y = min(original_signal[1])
        max_y = max(original_signal[1])
        normalized_signal_y = [(y - min_y) / (max_y - min_y) for y in original_signal[1]]

    elif normalize_option == "-1 to 1":
        MinRange = -1
        max_abs_y = max(abs(y) for y in original_signal[1])
        normalized_signal_y = [(2 * (y / max_abs_y) - 1) for y in original_signal[1]]
    else:
        print("Invalid normalization option.")
        return

    normalized_signal = (original_signal[0], normalized_signal_y)
    
    # test normalization
    NormalizeSignal(MinRange, MaxRange, normalized_signal[0], normalized_signal[1])

    # Plot the original signal and the normalized signal
    plot_signals([original_signal, normalized_signal])
# Accumulation
def accumulation():
    datasets = get_datasets()

    if len(datasets) != 1:
        print("Please select exactly one signal.")
        return

    original_signal = datasets[0]

    accumulated_values = np.cumsum(original_signal[1])
    accumulated_signal = (original_signal[0], accumulated_values)

    # test accumulation
    SignalSamplesAreEqual('ACC', './test_cases/task2/output accumulation for signal1.txt', accumulated_signal[0], accumulated_signal[1])

    # Plot the original signal and the accumulated signal
    plot_signals([original_signal, accumulated_signal])
    
    
def quantization_signal(signal,lvls):
    sig_min = min(signal)
    sig_max = max(signal)
    sig_delta = round((sig_max - sig_min)/lvls,3)
    ranges = []
    mid_points=[]
    interval_index=[]
    xQs=[]
    binary_rep=[]
    error = []
    num_bits = int(math.log(lvls,2))
    x= sig_min
    for i in range(lvls):
        ranges.append((x,x+sig_delta))
        x = x +sig_delta
    
    ranges = [(round(a,3), round(b, 3)) for a, b in ranges]
    for start, end in ranges:
        mid_points.append(round((start + end)/2,3))
    y=0
    
    for i,(point) in enumerate(signal):
        for index,(start, end) in enumerate(ranges):
            if point >= start and point <= end:
                xQs.append(mid_points[index])
                interval_index.append(index+1)
                y = index
                break
        binary_rep.append(format(y, f'0{num_bits}b'))
        error.append(round(xQs[i]-point,3))
    return binary_rep,error,xQs,interval_index

def quantization_signal_tst(qunt_entry,v):
    lvls = int(qunt_entry.get())
    if v.get() == "bits":
        lvls = pow(2,int(qunt_entry.get()))    
    indices,signals=get_datasets()
    binary_rep,error,xQs,interval_index = quantization_signal(signals,lvls)
    if v.get() == "bits":
        QuantizationTest1("./test_cases/task3/Quan1_Out.txt",binary_rep,xQs)
    elif v.get() == "levels":
        QuantizationTest2("./test_cases/task3/Quan2_Out.txt",interval_index,binary_rep,xQs,error)
