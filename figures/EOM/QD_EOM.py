import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import re
from matplotlib.ticker import MultipleLocator
from matplotlib import gridspec

#majorLocatorX = MultipleLocator(2)
#minorLocatorX = MultipleLocator(1)
#majorLocatorY = MultipleLocator(0.05)
#minorLocatorY = MultipleLocator(0.025)

filename = '/home/sam/Documents/thesis/data/QDot_thesis.dat'

x1 = []
y1 = []

x2 = []
y2 = []

with open(filename) as f:
    data = f.read()
data = data.split('\n')

for num in range(len(data)):
    line = data[num].split()

    print(line)
    
    if( num < 24 ):
        x1.append(float(line[5]))
        y1.append(abs((float(line[3]) - float(line[4]))/float(line[4])))
    else:
        x2.append(float(line[5]))
        y2.append(abs((float(line[3]) - float(line[4]))/float(line[4])))

plt.rc('font', family='serif')

fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(1, 1)

ax1 = plt.subplot(gs[0])
ax1.scatter(x1, y1, color='b', marker='o', s=40, label='PA-EOM')
ax1.scatter(x2, y2, color='r', marker='s', s=40, label='PR-EOM')

ax1.axis([-0.02, 0.8, 0.0, 0.05], fontsize=22)
ax1.tick_params(axis='x',labelsize=16)
ax1.tick_params(axis='y',labelsize=16)
ax1.set_ylabel(r'$\mathrm{\Delta E/E}$', fontsize=20)
ax1.set_xlabel(r'$\mathrm{n_{1-particle},\ n_{1-hole}}$', fontsize=20)

ax1.legend(loc='upper right', frameon=False, fontsize=18, labelspacing=0.0)

plt.tight_layout()
plt.savefig('QD_EOM.pdf', format='pdf', bbox_inches='tight')
plt.show()
