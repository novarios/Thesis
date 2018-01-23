import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib import gridspec

#majorLocatorX = MultipleLocator(2)
#minorLocatorX = MultipleLocator(1)
#majorLocatorY = MultipleLocator(0.05)
#minorLocatorY = MultipleLocator(0.025)

filename1 = '/home/sam/Documents/thesis/data/Ground_State_6_8.dat'
filename2 = '/home/sam/Documents/thesis/data/Ground_State_8_14.dat'
filename3 = '/home/sam/Documents/thesis/data/Ground_State_14_20.dat'

x1 = [[] for i in range(3)]
y1 = [[] for i in range(3)]
x2 = [[] for i in range(3)]
y2 = [[] for i in range(3)]
x3 = [[] for i in range(3)]
y3 = [[] for i in range(3)]

with open(filename1) as f1:
    data1 = f1.read()
data1 = data1.split('\n')

with open(filename2) as f2:
    data2 = f2.read()
data2 = data2.split('\n')

with open(filename3) as f3:
    data3 = f3.read()
data3 = data3.split('\n')

for num in range(len(data1)-1):
    line = data1[num].split()
    if( int(line[1]) == 8 ):
        x1[0].append(float(line[0]))
        y1[0].append(float(line[6]))
    elif( int(line[1]) == 10 ):
        x1[1].append(float(line[0]))
        y1[1].append(float(line[6]))
    elif( int(line[1]) == 12 ):
        x1[2].append(float(line[0]))
        y1[2].append(float(line[6]))

for num in range(len(data2)-1):
    line = data2[num].split()
    if( int(line[1]) == 8 ):
        x2[0].append(float(line[0]))
        y2[0].append(float(line[6]))
    elif( int(line[1]) == 10 ):
        x2[1].append(float(line[0]))
        y2[1].append(float(line[6]))
    elif( int(line[1]) == 12 ):
        x2[2].append(float(line[0]))
        y2[2].append(float(line[6]))

for num in range(len(data3)-1):
    line = data3[num].split()
    if( int(line[1]) == 8 ):
        x3[0].append(float(line[0]))
        y3[0].append(float(line[6]))
    elif( int(line[1]) == 10 ):
        x3[1].append(float(line[0]))
        y3[1].append(float(line[6]))
    elif( int(line[1]) == 12 ):
        x3[2].append(float(line[0]))
        y3[2].append(float(line[6]))
        
plt.rc('font', family='serif')

fig = plt.figure(figsize=(12,4))
gs = gridspec.GridSpec(1, 3)

ax1 = plt.subplot(gs[0])
ax1.plot(x1[0], y1[0], '-', marker='o', color='k')
ax1.plot(x1[1], y1[1], '--', marker='s', color='r')
ax1.plot(x1[2], y1[2], ':', marker='^', color='b')
ax1.plot([0, 30], [-105.284, -105.284], '--', color='grey')
ax1.axis([6.0, 30.0, -106.0, -87.0])
ax1.set_xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=15)
ax1.set_ylabel(r'$\mathrm{E\ (MeV)}$', fontsize=15)
# 105.284
annotation_string = r'$\mathrm{^{14}C}$'
ax1.annotate(annotation_string, fontsize=15, xy=(0.15, 0.85), xycoords='axes fraction')

ax2 = plt.subplot(gs[1])
ax2.plot(x2[0], y2[0], '-', marker='o', color='k')
ax2.plot(x2[1], y2[1], '--', marker='s', color='r')
ax2.plot(x2[2], y2[2], ':', marker='^', color='b')
ax2.plot([0, 30], [-162.027, -162.027], '--', color='grey')
ax2.axis([6.0, 30.0, -163.0, -135.0])
ax2.set_xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=15)
# 162.027
annotation_string = r'$\mathrm{^{22}O}$'
ax2.annotate(annotation_string, fontsize=15, xy=(0.15, 0.85), xycoords='axes fraction')

ax3 = plt.subplot(gs[2])
ax3.plot(x3[0], y3[0], '-', marker='o', color='k', label='$\mathrm{8}$')
ax3.plot(x3[1], y3[1], '--', marker='s', color='r', label='$\mathrm{10}$')
ax3.plot(x3[2], y3[2], ':', marker='^', color='b', label='$\mathrm{12}$')
ax3.plot([0, 30], [-283.429, -283.429], '--', color='grey')
ax3.axis([6.0, 30.0, -302.0, -260.0])
ax3.set_xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=15)
# 283.429
annotation_string = r'$\mathrm{^{34}Si}$'
ax3.annotate(annotation_string, fontsize=15, xy=(0.15, 0.85), xycoords='axes fraction')


ax3.legend(loc='upper right', title='$\mathbf{e_{max}}$', frameon=False, fontsize='small')

#ax.xaxis.set_major_locator(majorLocatorX)
#ax.xaxis.set_minor_locator(minorLocatorX)
#ax.yaxis.set_major_locator(majorLocatorY)
#ax.yaxis.set_minor_locator(minorLocatorY)

plt.tight_layout()
plt.savefig('ground_state2.pdf', format='pdf', bbox_inches='tight')
plt.show()
