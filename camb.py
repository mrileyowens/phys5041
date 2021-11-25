# Author: Riley Owens (GitHub: mrileyowens)

# This file plots CMB scalar data created
# by CAMB.

from matplotlib import pyplot as plt

import os
import glob

import numpy as np

from scipy.signal import find_peaks

# Establishing filepaths and directories
home='C:/Users/15136/OneDrive - University of Cincinnati/Documents/Courses/PHYS 5041'
data=home+'/data'
figs=home+'/figs'

# Retrieving files for varying spatial curvatures
files=glob.glob(data+'/Om_k*.dat')

# Plot labels
labels=['$\Omega_k$=-0.1','$\Omega_k$=0.0','$\Omega_k$=0.1']

# Figure of CMB scalar spectra for different spatial curvatures
fig,ax=plt.subplots(1,1)

for i in [0,1,2]:

    # Extracting data from files
    arr=np.loadtxt(files[i])

    # Plotting data in semilog space
    ax.semilogx(arr[:,0],arr[:,1],label=labels[i])

ax.set_xlim(np.min(arr[:,0]),np.max(arr[:,0]))
ax.set_ylim(0.0)
ax.set_xlabel('Multipole Moment ($\ell$)')
ax.set_ylabel('Anisotropy Power ($\mu$K$^2$)')
ax.legend(loc='upper left')

fig.tight_layout()
fig.savefig(figs+'/cmbps.png',dpi=100,bbox_inches='tight')

# Retrieving files for varying baryon contents
files=glob.glob(data+'/Om_b*.dat')

# Plot labels
labels=['$\Omega_bh^2$=0.01264','$\Omega_bh^2$=0.02260','$\Omega_bh^2$=0.04520']

# Figure of CMB scalar spectra for different baryon contents
fig,ax=plt.subplots(1,1)

peakArr=np.array([])

for i in [0,1,2]:

    # Extracting data from files
    arr=np.loadtxt(files[i])

    # Plotting data in semilog space
    ax.semilogx(arr[:,0],arr[:,1],label=labels[i])

    # Determining index locations of peaks in spectrum
    ind=find_peaks(arr[:,1])

    # Taking multipole moments of peak locations
    moments=np.take(arr[:,0],ind[0])

    # Taking anisotropy power of peaks
    peaks=np.take(arr[:,1],ind[0])

    # Creating array with height of first two peaks for display
    # to compute ratio
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
