from tests.CompareSignal_corr import Compare_Signals
from signal_processing import get_datasets
import matplotlib.pyplot as plt

def plot_signal(x, y, title='Signal'):
    plt.figure()  # Create a new figure

    plt.subplot(2, 1, 2)  # Plot the continuous signal
    plt.plot(x, y)
    plt.title('Continuous Signal')
    plt.subplot(2, 1, 1)  # Plot the discrete signal
    plt.stem(x, y)
    plt.title('Discrete Signal')

    plt.show()


def normalizedCrossCorrelation():
    indecies_1 = []
    indecies_2 = []
    sample_1 = []
    sample_2 = []
    datasets,domain = get_datasets()
    indecies_1[:] = datasets[0][0]
    indecies_2[:] = datasets[1][0]
    sample_1[:]= datasets[0][1]
    sample_2[:] = datasets[1][1]
    
    result_samples = corr(sample_1, sample_2)
    
    Compare_Signals("test_cases (output)/task8/CorrOutput.txt",indecies_1,result_samples)
    plot_signal(indecies_1, result_samples)
    

def corr(sample_1, sample_2):
    result_samples = []
    
    x1=sample_1
    x2=sample_2
    N=len(x1)
    sum_samle_1=0
    sum_samle_2=0
    for i in range(len(x1)):
        sum_samle_1+=x1[i]**2
    for i in range(len(x2)):
        sum_samle_2+=x2[i]**2
    bottom_num=((sum_samle_1*sum_samle_2)**0.5)/N
    for _ in range(N):
        Cur_Res=0
        for i in range(N):   
            Cur_Res+=(x1[i]*x2[i])
        tem=x2[0]
        x2.pop(0)    
        x2.append(tem)
        result_samples.append(((Cur_Res)/N)/bottom_num)
        
    return result_samples


