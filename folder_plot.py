import os
import numpy as np
import pylab
import matplotlib.pyplot as plt

list = os.listdir('/Users/SeanFackler/PycharmProjects/Plotting/files')

split = os.path.splitext(list[1])

print split

parsed = split[0].split("_")

print parsed

data = np.genfromtxt('Overview N_XMCD.txt')

# print data

energy = data[0, :]
XMCD = data[1, :]

energy_col = energy.reshape(-1, 1)
XMCD_col = XMCD.reshape(-1, 1)
spectra = np.concatenate((energy_col, XMCD_col), axis=1)

print spectra
np.savetxt('spectra.txt', spectra, delimiter=",")

# Make Figure

print parsed[2]

fig = plt.figure()
#title = 'spectra of %(material)s' % {"material": parsed[2]}
title = 'spectra of %(material)s taken at %(technique)s on %(date)s' % {"material":parsed[0], "technique":parsed[2], "date":parsed[3]}

#print title

fig.suptitle(title, fontsize=20, fontweight='bold')
ax = fig.add_subplot(111)

ax.set_xlabel('Energy (eV)', fontsize=14)
ax.set_ylabel('X-ray Absorption Intensity (arb. units)', fontsize=14)

ax.plot(energy_col, XMCD_col)

ax.axis([390, 413, -0.02, 0.07])

pylab.savefig('XAS_test.pdf')

plt.show()
