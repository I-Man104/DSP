import numpy as np
from signal_processing import get_datasets
from tests.comparesignals import SignalSamplesAreEqual

def plot_freq(x, y, x_lable, y_lable, fig, canv, flg=False):
    fig.clear()
    fig.supxlabel(x_lable)
    fig.supylabel(y_lable)
    ax=fig.add_subplot(111)
    if flg:
        fig.supxlabel("Time")
        ax.plot(x,y)
    else:
        ax.stem(x, y)
    canv.draw()

def write_file(indecies,samples):
  with open('dct_output.txt', 'w') as f:
    f.write('0\n')
    f.write('1\n')
    f.write(str(len(indecies))+'\n')
    for index,line in enumerate(indecies):
      if(index==(len(indecies)-1)):
        f.write(str(line)+' '+str(samples[index]))
      else:
        f.write(str(line)+' '+str(samples[index])+'\n')
  f.close()

def compute_dct(m_first_coefficients, figures, canvass):
    indecies = []
    samples = []
    data , domain = get_datasets()
    indecies[:] = data[0]
    samples[:] = data[1]

    # Ensure samples is a NumPy array
    samples = np.array(samples, dtype=float)
    
    N = len(samples)
    Yk = []

    for k in range(N):
        summation = 0

        for n in range(N):
            summation += samples[n] * np.cos((np.pi / (4 * N)) * (2 * n - 1) * (2 * k - 1))

        Y_current = np.sqrt(2/N) * summation
        Yk.append(Y_current)

    SignalSamplesAreEqual("./test_cases (output)/task5/DCT_output.txt", indecies, Yk)
    plot_freq(indecies, Yk, "indecies", "samples", figures[0], canvass[0], True)
    write_file(indecies[:m_first_coefficients], samples[:m_first_coefficients])
    
def remove_dc_component():
    indecies = []
    samples = []
    data, domain = get_datasets()
    indecies[:] = data[0]
    samples[:] = data[1]

    mean_sample=np.mean(samples)
    N=len(samples)
    after_remove=[]
    for k in range(N):
        after_remove.append(samples[k]-mean_sample)

    SignalSamplesAreEqual("./test_cases (output)/task5/DC_component_output.txt", indecies, after_remove)