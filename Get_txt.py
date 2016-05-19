#! usr/bin/env python
import sys
import numpy as np
import pylab
import matplotlib.pyplot as plt

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

fig = plt.figure()
fig.suptitle('N K-edge', fontsize=20, fontweight='bold')
ax = fig.add_subplot(111)

ax.set_xlabel('Energy (eV)', fontsize=14)
ax.set_ylabel('X-ray Absorption Intensity (arb. units)', fontsize=14)

ax.plot(energy_col, XMCD_col)

ax.axis([390, 413, -0.02, 0.07])

pylab.savefig('XAS_test.pdf')

plt.show()


