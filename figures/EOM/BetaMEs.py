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
y1 = [1.414213562, 1.490711985, 1.33333333, 0.471404521, 1.673320053, 1.788854382, 0.894427191, 1.85164020, 2.138089935, 0.377964473, 2.018433569]
y2 = [1.411292188, 1.490407468, 1.32469010, 0.471285798, 1.672493520, 1.162231505, 0.893847422, 1.85084078, 0.849276004, 1.195003360, 2.017977110]
y3 = [1.412833676, 1.490441392, 1.33020284, 0.471064008, 1.673113051, 1.777396654, 0.637893830, 1.84894488, 2.118227040, 0.439264608, 2.017514765]

labels = [r'$\mathrm{s_{1/2},s_{1/2}}$',
          r'$\mathrm{p_{3/2},p_{3/2}}$',
          r'$\mathrm{p_{1/2},p_{3/2}}$',
          r'$\mathrm{p_{1/2},p_{1/2}}$',
          r'$\mathrm{d_{5/2},d_{5/2}}$',
          r'$\mathrm{d_{3/2},d_{5/2}}$',
          r'$\mathrm{d_{3/2},d_{3/2}}$',
          r'$\mathrm{f_{7/2},f_{7/2}}$',
          r'$\mathrm{f_{5/2},f_{7/2}}$',
          r'$\mathrm{f_{5/2},f_{5/2}}$',
          r'$\mathrm{g_{9/2},g_{9/2}}$']

for num in [0,1,2,3,4,5,6,7,8,9,10]:
    y2[num] = abs(y1[num] - y2[num])
    y3[num] = abs(y1[num] - y3[num])

plt.rc('font', family='serif')

fig = plt.figure(figsize=(10, 5))
gs = gridspec.GridSpec(1, 1)

ax1 = plt.subplot(gs[0])
ax1.scatter(x1, y2, color='b', marker='o', s=60, label=r'$\mathrm{{}^{16}O}$')
ax1.scatter(x1, y3, color='r', marker='o', s=60, label=r'$\mathrm{{}^{22}O}$')

plt.xticks(x1, labels, rotation=40)
ax1.tick_params(axis='x',labelsize=16)
ax1.tick_params(axis='y',labelsize=16)
ax1.set_ylabel(r'$\mathrm{|\bar{O}_{GT} - \hat{O}_{GT}|}$', fontsize=20)
annotation_string = r'$*\mathrm{Preliminary}$'
plt.annotate(annotation_string, fontsize=16, xy=(0.03, 0.9), xycoords='axes fraction')

ax1.legend(bbox_to_anchor=(0.98,0.975), frameon=False, fontsize=14)

plt.tight_layout()
plt.savefig('BetaMEs.pdf', format='pdf', bbox_inches='tight')
plt.show()
