import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

majorLocatorX = MultipleLocator(2)
minorLocatorX = MultipleLocator(1)
majorLocatorY = MultipleLocator(0.05)
minorLocatorY = MultipleLocator(0.025)

filename = '/home/sam/Documents/thesis/data/Electron_Gas.dat'
filename1 = '/home/sam/Documents/thesis/data/Electron_Gas_QMC.dat'

x = [[] for i in range(5)]
y = [[] for i in range(5)]

x1 = []
y1 = []

with open(filename) as f:
    data = f.read()
data = data.split('\n')

for num in range(len(data)):
    line = data[num].split()
    ind = (num - num%15)/15
    #print(ind, float(line[0]), float(line[6]))
    if(float(line[0]) == 1.0):
        continue
    x[ind].append(float(line[0]))
    y[ind].append(float(line[6]))

with open(filename1) as f1:
    data1 = f1.read()
data1 = data1.split('\n')

for num in range(1,len(data1)):
    line1 = data1[num].split()
    x1.append(float(line1[0]))
    y1.append(float(line1[1]))

plt.rc('font', family='serif')

fig, ax = plt.subplots()
ax.plot(x[0], y[0], ':', marker='o', color='r', label='$\mathrm{N=14}$')
ax.plot(x[1], y[1], '-.', marker='s', color='b', label='$\mathrm{N=54}$')
#ax.plot(x[2], y[2], '--', marker='v', color='g', label='$\mathrm{N=114}$')
#ax.plot(x[3], y[3], '-', marker='o', color='r', label='$\mathrm{N=162}$')
ax.plot(x[4], y[4], '-', marker='^', color='k', label='$\mathrm{N=246}$')
ax.plot(x1, y1, '--', marker='v', color='g', label='$\mathrm{QMC}$')
ax.legend(loc='upper right')

plt.xlabel(r'$\mathrm{Wigner-Seitz\ Radius\ (r_{s})}$', fontsize=15)
plt.ylabel(r'$\mathrm{E/A\ (Ha)}$', fontsize=15)
plt.axis([1.0, 16.0, -0.1, 0.2])

#annotation_string = r'$\mathrm{25\ Shells}$'
#annotation_string += '\n'
#annotation_string += r'$\mathrm{1030\ Total\ States}$'
#ax.annotate(annotation_string, fontsize=15, xy=(2.5, 0.16))

ax.xaxis.set_major_locator(majorLocatorX)
ax.xaxis.set_minor_locator(minorLocatorX)
ax.yaxis.set_major_locator(majorLocatorY)
ax.yaxis.set_minor_locator(minorLocatorY)

plt.savefig('Electronic_Gas.pdf', format='pdf', bbox_inches='tight')
plt.show()
