import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib import gridspec
from mpl_toolkits.axes_grid.inset_locator import inset_axes

#majorLocatorX = MultipleLocator(2)
#minorLocatorX = MultipleLocator(1)
#majorLocatorY = MultipleLocator(0.05)
#minorLocatorY = MultipleLocator(0.025)

filename1 = '/home/sam/Documents/thesis/data/O16_CoM.dat'
filename2 = '/home/sam/Documents/thesis/data/Ca40_CoM.dat'

hw0_1 = []
e0_1 = []
hw1_1 = []
e1_1 = []
hw2_1 = []
e2_1 = []
hwa_1 = []
hwb_1 = []

hw0_2 = []
e0_2 = []
hw1_2 = []
e1_2 = []
hw2_2 = []
e2_2 = []
hwa_2 = []
hwb_2 = []

with open(filename1) as f1:
    data1 = f1.read()
data1 = data1.split('\n')

with open(filename2) as f2:
    data2 = f2.read()
data2 = data2.split('\n')

for num in range(len(data1)):
    line = data1[num].split()
    if( num - num%6 == 0 ):
        hw0_1.append(float(line[0]))
        e0_1.append(float(line[5]))
    elif( num - num%6 == 6 ):
        if( num%6 <= 2 ):
            hw1_1.append(float(line[0]))
            e1_1.append(float(line[5]))
        if( num%6 >= 2 ):
            hw2_1.append(float(line[0]))
            e2_1.append(float(line[5]))
    elif( num - num%6 == 12 ):
        hwa_1.append(float(line[1]))
        hwb_1.append(float(line[2]))

for num in range(len(data2)):
    line = data2[num].split()
    if( num - num%6 == 0 ):
        hw0_2.append(float(line[0]))
        e0_2.append(float(line[5]))
    elif( num - num%6 == 6 ):
        if( num%6 <= 2 ):
            hw1_2.append(float(line[0]))
            e1_2.append(float(line[5]))
        if( num%6 >= 2 ):
            hw2_2.append(float(line[0]))
            e2_2.append(float(line[5]))
    elif( num - num%6 == 12 ):
        hwa_2.append(float(line[1]))
        hwb_2.append(float(line[2]))

hw0_1_1 = hw0_1[:-1]
e0_1_1 = e0_1[:-1]
hw0_2_1 = hw0_2[:-1]
e0_2_1 = e0_2[:-1]

plt.rc('font', family='serif')

fig = plt.figure(figsize=(7, 8))
gs = gridspec.GridSpec(2, 1)

ax1 = plt.subplot(gs[0])
plt.plot(hw0_1_1, e0_1_1, '-', marker='o', color='k', label=r'$\mathrm{\hbar\omega}$')
plt.plot(hw1_1, e1_1, '--', marker='s', color='r', label=r'$\mathrm{\hbar\widetilde{\omega}_{+}}$')
plt.plot(hw2_1, e2_1, ':', marker='^', color='b', label=r'$\mathrm{\hbar\widetilde{\omega}_{-}}$')
plt.axis([6.0, 30.0, -0.5, 4.0])
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_ylabel(r'$\mathrm{E_{CoM}\ (MeV)}$', fontsize=15)
annotation_string = r'$\mathrm{^{16}O}$'
plt.annotate(annotation_string, fontsize=15, xy=(0.05, 0.85), xycoords='axes fraction')

inset_axes1 = inset_axes(ax1,width="50%",height=1.25,loc=1)
plt.plot(hw0_1, hwa_1, '--', marker='s', color='r')
plt.plot(hw0_1, hwb_1, ':', marker='^', color='b')
plt.xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=14)
plt.ylabel(r'$\mathrm{\hbar\widetilde{\omega}\ (MeV)}$', fontsize=14)

ax1.legend(bbox_to_anchor=(1.0,0.45), frameon=False, fontsize='small')

ax2 = plt.subplot(gs[1])
plt.plot(hw0_2_1, e0_2_1, '-', marker='o', color='k', label=r'$\mathrm{\hbar\omega}$')
plt.plot(hw1_2, e1_2, '--', marker='s', color='r', label=r'$\mathrm{\hbar\widetilde{\omega}_{+}}$')
plt.plot(hw2_2, e2_2, ':', marker='^', color='b', label=r'$\mathrm{\hbar\widetilde{\omega}_{-}}$')
plt.axis([6.0, 30.0, -0.5, 4.0])
ax2.set_xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=15)
ax2.set_ylabel(r'$\mathrm{E_{CoM}\ (MeV)}$', fontsize=15)
annotation_string = r'$\mathrm{^{40}Ca}$'
plt.annotate(annotation_string, fontsize=15, xy=(0.05, 0.85), xycoords='axes fraction')

inset_axes2 = inset_axes(ax2,width="50%",height=1.25,loc=1)
plt.plot(hw0_2, hwa_2, '--', marker='s', color='r')
plt.plot(hw0_2, hwb_2, ':', marker='^', color='b')
plt.xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=14)
plt.ylabel(r'$\mathrm{\hbar\widetilde{\omega}\ (MeV)}$', fontsize=14)

ax2.legend(bbox_to_anchor=(1.0,0.45), frameon=False, fontsize='small')

#ax.xaxis.set_major_locator(majorLocatorX)
#ax.xaxis.set_minor_locator(minorLocatorX)
#ax.yaxis.set_major_locator(majorLocatorY)
#ax.yaxis.set_minor_locator(minorLocatorY)

plt.tight_layout()
plt.savefig('CoM1.pdf', format='pdf', bbox_inches='tight')
plt.show()
