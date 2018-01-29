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

filename = '/home/sam/Documents/thesis/data/Ground_State_8_8_SRG.dat'

x1 = [[] for i in range(2)]
y1 = [[] for i in range(2)]
x2 = [[] for i in range(2)]
y2 = [[] for i in range(2)]
x3 = [[] for i in range(2)]
y3 = [[] for i in range(2)]
x4 = [[] for i in range(2)]
y4 = [[] for i in range(2)]

with open(filename) as f:
    data = f.read()
data = data.split('\n')

for num in range(len(data)-1):
    line = data[num].split()
    if( num - num%3 == 0 ):
        x1[0].append(float(line[0]))
        y1[0].append(float(line[6]))
    elif( num - num%3 == 3 ):
        x1[1].append(float(line[0]))
        y1[1].append(float(line[6]))
    elif( num - num%3 == 6 ):
        x2[0].append(float(line[0]))
        y2[0].append(float(line[6]))
    elif( num - num%3 == 9 ):
        x2[1].append(float(line[0]))
        y2[1].append(float(line[6]))
    elif( num - num%3 == 12 ):
        x3[0].append(float(line[0]))
        y3[0].append(float(line[6]))
    elif( num - num%3 == 15 ):
        x3[1].append(float(line[0]))
        y3[1].append(float(line[6]))
    elif( num - num%3 == 18 ):
        x4[0].append(float(line[0]))
        y4[0].append(float(line[6]))
    elif( num - num%3 == 21 ):
        x4[1].append(float(line[0]))
        y4[1].append(float(line[6]))
        
plt.rc('font', family='serif')

fig = plt.figure(figsize=(8, 7))
gs = gridspec.GridSpec(2, 2)

ax1 = plt.subplot(gs[0])
ax1.plot(x1[0], y1[0], '--', marker='s', color='r')
ax1.plot(x1[1], y1[1], ':', marker='^', color='b')
ax1.plot([0, 30], [-127.619, -127.619], '--', color='grey')
ax1.axis([14.0, 26.0, -155.5, -153.0])
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_ylabel(r'$\mathrm{E\ (MeV)}$', fontsize=15)
annotation_string = r'$\mathrm{NN}$'
annotation_string += "\n"
annotation_string += r'$\lambda_{\mathrm{SRG}}=1.88\ \mathrm{fm}^{-1}$'
ax1.annotate(annotation_string, fontsize=12, xy=(0.1, 0.8), xycoords='axes fraction')

ax2 = plt.subplot(gs[1])
ax2.plot(x2[0], y2[0], '--', marker='s', color='r', label='$\mathrm{10}$')
ax2.plot(x2[1], y2[1], ':', marker='^', color='b', label='$\mathrm{12}$')
ax2.plot([0, 30], [-127.619, -127.619], '--', color='grey')
ax2.axis([14.0, 26.0, -169.4, -169.0])
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2, yticks=[-169.0,-169.1,-169.2,-169.3,-169.4], yticklabels=['-169.0','-169.1','-169.2','-169.3','-169.4'])
annotation_string = r'$\mathrm{NN}$'
annotation_string += "\n"
annotation_string += r'$\lambda_{\mathrm{SRG}}=2.24\ \mathrm{fm}^{-1}$'
ax2.annotate(annotation_string, fontsize=12, xy=(0.1, 0.8), xycoords='axes fraction')

ax3 = plt.subplot(gs[2])
ax3.plot(x3[0], y3[0], '--', marker='s', color='r')
ax3.plot(x3[1], y3[1], ':', marker='^', color='b')
ax3.plot([0, 30], [-127.619, -127.619], '--', color='grey')
ax3.axis([14.0, 26.0, -128.0, -126.0])
ax3.set_xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=15)
ax3.set_ylabel(r'$\mathrm{E\ (MeV)}$', fontsize=15)
annotation_string = r'$\mathrm{NN+3N}$'
annotation_string += "\n"
annotation_string += r'$\lambda_{\mathrm{SRG}}=1.88\ \mathrm{fm}^{-1}$'
ax3.annotate(annotation_string, fontsize=12, xy=(0.1, 0.8), xycoords='axes fraction')

ax4 = plt.subplot(gs[3])
ax4.plot(x4[0], y4[0], '--', marker='s', color='r')
ax4.plot(x4[1], y4[1], ':', marker='^', color='b')
ax4.plot([0, 30], [-127.619, -127.619], '--', color='grey')
ax4.axis([14.0, 26.0, -129.3, -128.7])
ax4.set_xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=15)
plt.setp(ax4, yticks=[-128.7,-128.9,-129.1,-129.3], yticklabels=['-128.7','-128.9','-129.1','-129.3'])
annotation_string = r'$\mathrm{NN+3N}$'
annotation_string += "\n"
annotation_string += r'$\lambda_{\mathrm{SRG}}=2.24\ \mathrm{fm}^{-1}$'
ax4.annotate(annotation_string, fontsize=12, xy=(0.1, 0.8), xycoords='axes fraction')


ax2.legend(loc='upper right', title='$\mathbf{e_{max}}$', frameon=False, fontsize='small')

#ax.xaxis.set_major_locator(majorLocatorX)
#ax.xaxis.set_minor_locator(minorLocatorX)
#ax.yaxis.set_major_locator(majorLocatorY)
#ax.yaxis.set_minor_locator(minorLocatorY)

plt.tight_layout()
plt.savefig('ground_state_srg.pdf', format='pdf', bbox_inches='tight')
plt.show()
