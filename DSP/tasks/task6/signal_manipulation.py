from signal_processing import get_datasets
from tests.comparesignals import SignalSamplesAreEqual
from tests.Shift_Fold_Signal import Shift_Fold_Signal
from tasks.task4.DFT_IDFT import DFT,IDFT
import numpy as np
import matplotlib.pyplot as plt

def plot_signal(x, y, title='Signal'):
    plt.figure()  # Create a new figure

    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.show()


def shift_tsk6(idx,numm,bol=True):
    if bol:
        x = [item - numm for item in idx]
    else:
        x = [item + numm for item in idx]
    return x

def smoothing(window_size):
    x = []
    y = []
    dataset,domain = get_datasets()
    x[:],y[:] = dataset
    j = window_size
    new_y = []
    for i in range(len(y)):
        if j > len(y):
            break
        window = np.sum(y[i:j])/window_size
        new_y.append(window)
        j+=1
    # first test case: window size = 3, input_signal1.txt
    SignalSamplesAreEqual("./test_cases (output)/task6/MovingAverage/OutMovAvgTest1.txt",x,new_y)
    # second test case: window size = 5, input_signal2.txt
    SignalSamplesAreEqual("./test_cases (output)/task6/MovingAverage/OutMovAvgTest2.txt",x,new_y)

def folding(fold_only = True):
    x = []
    y = []
    dataset,domain = get_datasets()
    x[:],y[:] = dataset
    y.reverse()
    if fold_only == True:
        Shift_Fold_Signal("test_cases (output)/task6/ShiftingAndFolding/Output_fold.txt", x, y)
    plot_signal(x,y)
    return x,y

def shift_and_fold(shift_value):
    x,y = folding(False)
    x = shift_tsk6(x,shift_value,False)
    Shift_Fold_Signal("test_cases (output)/task6/ShiftingAndFolding/Output_ShifFoldedby500.txt", x, y)
    Shift_Fold_Signal("test_cases (output)/task6/ShiftingAndFolding/Output_ShiftFoldedby-500.txt", x, y)
    plot_signal(x,y)

def remove_dc_component_time_domain():
    x = []
    y = []
    dataset,domain = get_datasets()
    x[:],y[:] = dataset
    A,phase,N = DFT(y)
    A[0] = 0
    phase[0] = 0
    y = IDFT(A,phase)
    SignalSamplesAreEqual("./test_cases (output)/task5/DC_component_output.txt", x, y)