from matplotlib.widgets import Button
import matplotlib.pyplot as plt
import sys
import pylab

import numpy as np
fig = plt.figure()

def callback(event):
    print "clicked:", event
    sys.stdout.flush()

ax1 = plt.axes([0.2, 0.5, 0.1, 0.075])
ax2 = plt.axes([0.7, 0.5, 0.1, 0.075])

b1 = Button(ax1, 'Button 1')
b1.on_clicked(callback)

b2 = Button(ax2, 'Button 2')
b2.on_clicked(callback)