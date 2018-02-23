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

filename1 = '/home/sam/Documents/thesis/data/PR_new_final_7_8.dat'
filename2 = '/home/sam/Documents/thesis/data/PR_new_final_8_7.dat'
filename3 = '/home/sam/Documents/thesis/data/PR_new_final_7_14.dat'
filename4 = '/home/sam/Documents/thesis/data/PR_new_final_8_13.dat'

x1 = [[] for i in range(3)]
y1 = [[] for i in range(3)]
x2 = [[] for i in range(3)]
y2 = [[] for i in range(3)]
x3 = [[] for i in range(3)]
y3 = [[] for i in range(3)]
x4 = [[] for i in range(3)]
y4 = [[] for i in range(3)]

with open(filename1) as f1:
    data1 = f1.read()
data1 = data1.split('\n')

with open(filename2) as f2:
    data2 = f2.read()
data2 = data2.split('\n')

with open(filename3) as f3:
    data3 = f3.read()
data3 = data3.split('\n')

with open(filename4) as f4:
    data4 = f4.read()
data4 = data4.split('\n')

for num in range(len(data1)-1):
    line = data1[num].split()
    if( int(line[3]) == 8 ):
        x1[0].append(float(line[0]))
        y1[0].append(float(line[12]))
    elif( int(line[3]) == 10 ):
        x1[1].append(float(line[0]))
        y1[1].append(float(line[12]))
    elif( int(line[3]) == 12 ):
        x1[2].append(float(line[0]))
        y1[2].append(float(line[12]))

for num in range(len(data2)-1):
    line = data2[num].split()
    if( int(line[3]) == 8 ):
        x2[0].append(float(line[0]))
        y2[0].append(float(line[12]))
    elif( int(line[3]) == 10 ):
        x2[1].append(float(line[0]))
        y2[1].append(float(line[12]))
    elif( int(line[3]) == 12 ):
        x2[2].append(float(line[0]))
        y2[2].append(float(line[12]))

for num in range(len(data3)-1):
    line = data3[num].split()
    if( int(line[3]) == 8 ):
        x3[0].append(float(line[0]))
        y3[0].append(float(line[12]))
    elif( int(line[3]) == 10 ):
        x3[1].append(float(line[0]))
        y3[1].append(float(line[12]))
    elif( int(line[3]) == 12 ):
        x3[2].append(float(line[0]))
        y3[2].append(float(line[12]))

for num in range(len(data4)-1):
    line = data4[num].split()
    if( int(line[3]) == 8 ):
        x4[0].append(float(line[0]))
        y4[0].append(float(line[12]))
    elif( int(line[3]) == 10 ):
        x4[1].append(float(line[0]))
        y4[1].append(float(line[12]))
    elif( int(line[3]) == 12 ):
        x4[2].append(float(line[0]))
        y4[2].append(float(line[12]))
        
plt.rc('font', family='serif')

fig = plt.figure(figsize=(8, 7))
gs = gridspec.GridSpec(2, 2)

ax1 = plt.subplot(gs[0])
ax1.plot(x1[0], y1[0], '-', marker='o', color='k')
ax1.plot(x1[1], y1[1], '--', marker='s', color='r')
ax1.plot(x1[2], y1[2], ':', marker='^', color='b')
ax1.plot([0, 30], [-115.4919, -115.4919], '--', color='grey')
ax1.axis([6.0, 30.0, -118.0, -100.0])
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_ylabel(r'$\mathrm{E\ (MeV)}$', fontsize=15)
# 115.4919
annotation_string = r'$\mathrm{^{15}N}$'
ax1.annotate(annotation_string, fontsize=15, xy=(0.15, 0.85), xycoords='axes fraction')

ax2 = plt.subplot(gs[1])
ax2.plot(x2[0], y2[0], '-', marker='o', color='k', label='$\mathrm{8}$')
ax2.plot(x2[1], y2[1], '--', marker='s', color='r', label='$\mathrm{10}$')
ax2.plot(x2[2], y2[2], ':', marker='^', color='b', label='$\mathrm{12}$')
ax2.plot([0, 30], [-111.95538, -111.95538], '--', color='grey')
ax2.axis([6.0, 30.0, -115.0, -95.0])
plt.setp(ax2.get_xticklabels(), visible=False)
# 111.95538
annotation_string = r'$\mathrm{^{15}O}$'
ax2.annotate(annotation_string, fontsize=15, xy=(0.15, 0.85), xycoords='axes fraction')

ax3 = plt.subplot(gs[2])
ax3.plot(x3[0], y3[0], '-', marker='o', color='k')
ax3.plot(x3[1], y3[1], '--', marker='s', color='r')
ax3.plot(x3[2], y3[2], ':', marker='^', color='b')
ax3.plot([0, 30], [-138.789315, -138.789315], '--', color='grey')
ax3.axis([6.0, 30.0, -140.0, -110.0])
ax3.set_xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=15)
ax3.set_ylabel(r'$\mathrm{E\ (MeV)}$', fontsize=15)
# 138.789315
annotation_string = r'$\mathrm{^{21}N}$'
ax3.annotate(annotation_string, fontsize=15, xy=(0.15, 0.85), xycoords='axes fraction')

ax4 = plt.subplot(gs[3])
ax4.plot(x4[0], y4[0], '-', marker='o', color='k')
ax4.plot(x4[1], y4[1], '--', marker='s', color='r')
ax4.plot(x4[2], y4[2], ':', marker='^', color='b')
ax4.plot([0, 30], [-155.176854, -155.176854], '--', color='grey')
ax4.axis([6.0, 30.0, -160.0, -130.0])
ax4.set_xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=15)
# 155.176854
annotation_string = r'$\mathrm{^{21}O}$'
ax4.annotate(annotation_string, fontsize=15, xy=(0.15, 0.85), xycoords='axes fraction')


ax2.legend(loc='upper right', title='$\mathbf{e_{max}}$', frameon=False, fontsize='small')

#ax.xaxis.set_major_locator(majorLocatorX)
#ax.xaxis.set_minor_locator(minorLocatorX)
#ax.yaxis.set_major_locator(majorLocatorY)
#ax.yaxis.set_minor_locator(minorLocatorY)

plt.tight_layout()
plt.savefig('PR-EOM.pdf', format='pdf', bbox_inches='tight')
plt.show()
