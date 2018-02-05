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

x1 = [1,2,3,4,5,6,7,8,9,10,11]
y1 = [1.414213562, 1.490711985, 1.333333, 0.471404521, 1.673320053, 1.788854382, 0.894427191, 1.8516402, 2.138089935, 0.377964473, 2.018433569]
y2 = [1.411292, 1.49041, 1.32469, 0.47129, 1.67249, 1.39137, 0.89385, 1.85084, 1.5066, 1.195, 2.018]

labels = [r'$\mathrm{s_{1/2},s_{1/2}}$', r'$\mathrm{p_{3/2},p_{3/2}}$', r'$\mathrm{p_{1/2},p_{3/2}}$', r'$\mathrm{p_{1/2},p_{1/2}}$', r'$\mathrm{d_{5/2},d_{5/2}}$', r'$\mathrm{d_{3/2},d_{5/2}}$', r'$\mathrm{d_{3/2},d_{3/2}}$', r'$\mathrm{f_{7/2},f_{7/2}}$', r'$\mathrm{f_{5/2},f_{7/2}}$', r'$\mathrm{f_{5/2},f_{5/2}}$', r'$\mathrm{g_{9/2},g_{9/2}}$']

for num in range(10):
    y1[num] = abs(y1[num] - y2[num])

plt.rc('font', family='serif')

fig = plt.figure(figsize=(10, 5))
gs = gridspec.GridSpec(1, 1)

ax1 = plt.subplot(gs[0])
ax1.scatter(x1, y1, color='b', marker='o', s=60)

plt.xticks(x1, labels, rotation=40)
ax1.tick_params(axis='x',labelsize=16)
ax1.tick_params(axis='y',labelsize=16)
ax1.set_ylabel(r'$\mathrm{|\bar{O}_{GT} - \hat{O}_{GT}|}$', fontsize=20)

plt.tight_layout()
plt.savefig('BetaMEs.pdf', format='pdf', bbox_inches='tight')
plt.show()
