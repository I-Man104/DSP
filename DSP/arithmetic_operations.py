from tkinter import filedialog
from signal_processing import get_datasets, plot_signals
from scipy.interpolate import interp1d
import numpy as np

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
    
    # Plot the original signals and the sum
    plot_signals(datasets + [sum_signal])

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
    diff_signal = subtract_signals(datasets[1], datasets[0])  # Note the order of signals

    # Plot the original signals and the difference
    plot_signals(datasets + [diff_signal])
    
def multiplication():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if not file_path:
        return

    constant = simpledialog.askfloat("Multiplication", "Enter a constant value:")
    if constant is None:
        return

    points = read_file(file_path)

    result_points = [(x, y * constant) for (x, y) in points]

def squaring():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if not file_path:
        return

    points = read_file(file_path)

    result_points = [(x, y ** 2) for (x, y) in points]

def shifting():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if not file_path:
        return

    shift = simpledialog.askfloat("Shifting", "Enter a shift value:")
    if shift is None:
        return

    points = read_file(file_path)

    result_points = [(x + shift, y) for (x, y) in points]

def normalization():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if not file_path:
        return

    normalize_option = simpledialog.askstring("Normalization", "Choose normalization (0-1 or -1-1):")
    if normalize_option not in ("0-1", "-1-1"):
        print("Invalid normalization option.")
        return

    points = read_file(file_path)

    if normalize_option == "0-1":
        min_y = min(y for (_, y) in points)
        max_y = max(y for (_, y) in points)
        result_points = [(x, (y - min_y) / (max_y - min_y)) for (x, y) in points]
    else:  # -1-1 normalization
        min_y = min(y for (_, y) in points)
        max_y = max(y for (_, y) in points)
        max_abs_y = max(abs(y) for (_, y) in points)
        result_points = [(x, (2 * (y / max_abs_y) - 1)) for (x, y) in points]

   

def accumulation():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if not file_path:
        return

    points = read_file(file_path)

    accumulated_signal = [(x, 0) for x, _ in points]

    for i, (_, y) in enumerate(points):
        accumulated_signal[i] = (points[i][0], sum(y for _, y in points[:i+1]))