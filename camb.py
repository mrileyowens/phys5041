from matplotlib import pyplot as plt

import os
import glob

import numpy as np

from scipy.signal import find_peaks

home='C:/Users/15136/OneDrive - University of Cincinnati/Documents/Courses/PHYS 5041'

data=home+'/data'
figs=home+'/figs'

cwd=os.getcwd()

files=glob.glob(data+'/Om_k*.dat')

labels=['$\Omega_k$=-0.1','$\Omega_k$=0.0','$\Omega_k$=0.1']

fig,ax=plt.subplots(1,1)

for i in [0,1,2]:

    arr=np.loadtxt(files[i])

    ax.semilogx(arr[:,0],arr[:,1],label=labels[i])

ax.set_xlim(np.min(arr[:,0]),np.max(arr[:,0]))
ax.set_ylim(0.0)
ax.set_xlabel('Multipole Moment ($\ell$)')
ax.set_ylabel('Anisotropy Power ($\mu$K$^2$)')
ax.legend(loc='upper left')

fig.tight_layout()
fig.savefig(figs+'/cmbps.png',dpi=100,bbox_inches='tight')

files=glob.glob(data+'/Om_b*.dat')
print(files)

labels=['$\Omega_bh^2$=0.01264','$\Omega_bh^2$=0.02260','$\Omega_bh^2$=0.04520']

fig,ax=plt.subplots(1,1)

peakArr=np.array([])

for i in [0,1,2]:

    arr=np.loadtxt(files[i])

    ax.semilogx(arr[:,0],arr[:,1],label=labels[i])

    ind=find_peaks(arr[:,1])
    moments=np.take(arr[:,0],ind[0])
    print(moments)
    peaks=np.take(arr[:,1],ind[0])
    firstpeak=peaks[0]
    secondpeak=peaks[1]
    peakArr=np.append(peakArr,np.array([firstpeak,secondpeak]))

ax.set_xlim(np.min(arr[:,0]),np.max(arr[:,0]))
ax.set_ylim(0.0)
ax.set_xlabel('Multipole Moment ($\ell$)')
ax.set_ylabel('Anisotropy Power ($\mu$K$^2$)')
ax.legend(loc='upper left')

fig.tight_layout()
fig.savefig(figs+'/cmbpsb.png',dpi=100,bbox_inches='tight')

print(peakArr)
