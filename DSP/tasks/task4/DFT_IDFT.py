from signal_processing import get_datasets
import numpy as np
import math
from tests.task_4_test import SignalComapreAmplitude, SignalComaprePhaseShift

def generate_omega(freq,N):
  omg=2*np.pi*freq/N
  omegas=[]
  for i in range(N):
    omegas.append(omg*(i+1))
  return omegas


def plot_freq(x,y,ylable,fig,canv,flg=False):
  fig.clear()
  fig.supxlabel("Fundamental Frequency")
  fig.supylabel(ylable)
  ax=fig.add_subplot(111)
  if flg:
    fig.supxlabel("Time")
    ax.plot(x,y)
  else:
    ax.stem(x, y)
  canv.draw()

# check if it's time signal or frequency signal
def change_time_sig(x, tORf_sig, figures, canvass):
  data_set,domain=get_datasets()
  x[:] = data_set[0]
  tORf_sig[:] = data_set[1]
  if domain == 'time':
    plot_freq(np.arange(len(tORf_sig)),tORf_sig,"Amplitude",figures[0],canvass[0],True)
  else:
    omega=generate_omega(4,len(tORf_sig))
    plot_freq(omega,x,"Amplitude",figures[1],canvass[1])
    plot_freq(omega,tORf_sig,"Phase Shift",figures[2],canvass[2])
  return x, tORf_sig

def DFT(sig):
    A=[]
    phase=[]
    N =len(sig)
    n=np.arange(N)
    xK=np.zeros(N,dtype=complex)

    for i in range(N):
        xK[i]+=np.sum(sig*np.exp(-2j*np.pi*i*n/N))

    for x in xK:
        A.append(np.sqrt((x.real**2) + (x.imag**2)))
        phase.append( math.atan2(x.imag,x.real))

    write_file(True,A,phase)
    return A,phase,N

def IDFT(amp,phase):
    N =len(amp)
    xknew = np.zeros(N,dtype=np.complex128)
    for i in range(N):
        xknew[i] += complex(amp[i]*np.cos(phase[i]),amp[i]*np.sin(phase[i]))

    xN=np.zeros(N,dtype=np.complex128)
    N =len(xknew)
    n=np.arange(N)
    for i in range(N):
        xN[i]+=np.sum(xknew*np.exp(2j*np.pi*i*n/N))/N
    write_file(False,np.round(xN.real,0))
    return xN.real


def apply_dft(sig,freq_entry,figures,canvass):
    amp,phase_shift,sample_num=DFT(sig)
    omg=generate_omega(int(freq_entry.get()),sample_num)
    plot_freq(omg,amp,"Amplitude",figures[1],canvass[1])
    plot_freq(omg,phase_shift,"Phase Shift",figures[2],canvass[2])

def apply_idft(amp,phase,figures,canvass):
    sig=IDFT(amp,phase)
    plot_freq(np.arange(len(sig)),sig,"Amplitude",figures[0],canvass[0],True)

def write_file(type,amp_or_sig,x=0):
    if type:
        with open('frequency_output.txt', 'w') as f:
            f.write('0\n')
            f.write('1\n')
            f.write(str(len(amp_or_sig))+'\n')
            for index,line in enumerate(amp_or_sig):
                if(index==(len(amp_or_sig)-1)):
                    f.write(str(line)+' '+str(x[index]))
                else:
                    f.write(str(line)+' '+str(x[index])+'\n')
        f.close()
    else:
        with open('time_output.txt', 'w') as f:
            f.write('0\n')
            f.write('0\n')
            f.write(str(len(amp_or_sig))+'\n')
            for index,line in enumerate(amp_or_sig):
                if(index==(len(amp_or_sig)-1)):
                    f.write(str(index)+' '+str(line))
                else:
                    f.write(str(index)+' '+str(line)+'\n')
        f.close()

def mod_sig(mod_amp_entry,mod_phase_entry,mod_idx_entry,amp_or_idx,sig_or_phase,freq_entry,figures,canvass):
    mod_amp = float(mod_amp_entry.get())
    mod_phase = float(mod_phase_entry.get())
    mod_idx = int(mod_idx_entry.get())-1
    amp,phase_shift,sample_num=DFT(sig_or_phase)
    amp[mod_idx]=mod_amp
    phase_shift[mod_idx]=mod_phase

    omg=generate_omega(int(freq_entry.get()),sample_num)
    plot_freq(omg,amp,"Amplitude",figures[1],canvass[1])
    plot_freq(omg,phase_shift,"Phase Shift",figures[2],canvass[2])
    apply_idft(amp,phase_shift,figures,canvass)

def apply_comp():
    data_me,domain_me=get_datasets()
    idx_or_amp_me,sig_or_phase_me = data_me
    data_u,isfreq_u=get_datasets()
    idx_or_amp_u,sig_or_phase_u = data_u
    if domain_me == 'frequency':
        new_amp_me=[float(format(x,'.12f')) for x in idx_or_amp_me]
        new_amp_u=[float(format(x,'.12f')) for x in idx_or_amp_u]
        ans=SignalComapreAmplitude(new_amp_me,new_amp_u)
        print(f'The amplitude compare = {ans}')
        new_phase_me=[float(format(x,'.12f')) for x in sig_or_phase_me]
        new_phase_u=[float(format(x,'.12f')) for x in sig_or_phase_u]
        anss=SignalComaprePhaseShift(new_phase_me,new_phase_u)
        print(f'The phase shift compare = {anss}')
    else:
        new_amp_me=[float(format(x,'.12f')) for x in idx_or_amp_me]
        new_amp_u=[float(format(x,'.12f')) for x in idx_or_amp_u]
        ans=SignalComapreAmplitude(new_amp_me,new_amp_u)
        print(f'The amplitude compare = {ans}')
