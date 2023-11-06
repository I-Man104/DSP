import math
from signal_processing import get_datasets
from tests.task_3_test import QuantizationTest1, QuantizationTest2

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
        QuantizationTest1("./test_cases (output)/task3/Quan1_Out.txt",binary_rep,xQs)
    elif v.get() == "levels":
        QuantizationTest2("./test_cases (output)/task3/Quan2_Out.txt",interval_index,binary_rep,xQs,error)
