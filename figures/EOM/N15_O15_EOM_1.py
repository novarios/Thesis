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

filename1 = '/home/sam/Documents/thesis/data/PR_final2_7_8.dat'
filename2 = '/home/sam/Documents/thesis/data/PR_final2_8_7.dat'

e1 = [[] for num in range(2)]
jp1 = [[] for num in range(2)]
j1 = [[] for num in range(2)]
p1 = [[] for num in range(2)]
n1 = [[] for num in range(2)]

e2 = [[] for num in range(2)]
jp2 = [[] for num in range(2)]
j2 = [[] for num in range(2)]
p2 = [[] for num in range(2)]
n2 = [[] for num in range(2)]

with open(filename1) as f1:
    data1 = f1.read()
data1 = data1.split('\n')

with open(filename2) as f2:
    data2 = f2.read()
data2 = data2.split('\n')

for num in range(12):
    line = data2[num].split()
    index = (num - num%6)/6

    e1[index].append([float(line[11]),float(line[11])])
    n1[index].append(float(line[13]))

    if( index == 0 ):
        p1[index].append('--')
        j1[index].append('b')
        if( num == 5 ):
            jp1[index].append('1/2-')
        else:
            jp1[index].append('')

    if( index == 1 ):
        p1[index].append('--')
        j1[index].append('r')
        if( num == 11 ):
            jp1[index].append('3/2-')
        else:
            jp1[index].append('')


for num in range(12):
    line = data2[num].split()
    index = (num - num%6)/6
    
    e2[index].append([float(line[11]),float(line[11])])
    n2[index].append(float(line[13]))
    
    if( index == 0 ):
        p2[index].append('--')
        j2[index].append('b')
        if( num == 5 ):
            jp2[index].append('1/2-')
        else:
            jp2[index].append('')
            
    if( index == 1 ):
        p2[index].append('--')
        j2[index].append('r')
        if( num == 11 ):
            jp2[index].append('3/2-')
        else:
            jp2[index].append('')


xa = [-10.0, -6.0, -2.0, 2.0, 6.0, 10.0]

plt.rc('font', family='serif')

fig = plt.figure(figsize=(16, 6))
gs = gridspec.GridSpec(1, 2)

ax1 = plt.subplot(gs[0])
for index in range(2):
    for num in range(len(e1[index])):
        if( jp1[index][num] == '' ):
            labelstring = ""
        else:
            labelstring = r'$\mathrm{' + jp1[index][num] + '}$'

        if(p1[index][num] == '--'):
            ax1.plot([xa[num]-1.5*n1[index][num], xa[num]+1.5*n1[index][num]], e1[index][num], linestyle=p1[index][num], dashes=(7,1), color=j1[index][num], linewidth=2.25, label=labelstring)
        else:
            ax1.plot([xa[num]-1.5*n1[index][num], xa[num]+1.5*n1[index][num]], e1[index][num], linestyle=p1[index][num], color=j1[index][num], linewidth=2.25, label=labelstring)

ax1.axis([-13.0, 15.0, 15.0, 30.0], fontsize=18)
ax1.tick_params(axis='x',labelsize=16)
ax1.set_ylabel(r'$\mathrm{E\ (MeV)}$', fontsize=18)
annotation_string = r'$\mathrm{^{15}N}$'
ax1.annotate(annotation_string, fontsize=22, xy=(0.915, 0.1), xycoords='axes fraction')
plt.setp(ax1, xticks=[-9.0,0.0,9.0], xticklabels=[r'$\beta=0$',r'$\beta=1$',r'$\mathrm{Exp.}$'])

ax1.legend(loc='upper right', frameon=False, fontsize=15, labelspacing=0.0)



ax2 = plt.subplot(gs[1])
for index in range(2):
    for num in range(len(e2[index])):
        print(e2[index][num])
        print([xa[num]-n2[index][num], xa[num]+n2[index][num]])
        if( jp2[index][num] == '' ):
            labelstring = ""
        else:
            labelstring = r'$\mathrm{' + jp2[index][num] + '}$'

        if(p2[index][num] == '--'):
            ax2.plot([xa[num]-1.5*n2[index][num], xa[num]+1.5*n2[index][num]], e2[index][num], linestyle=p2[index][num], dashes=(7,1), color=j2[index][num], linewidth=2.25, label=labelstring)
        else:
            ax2.plot([xa[num]-1.5*n2[index][num], xa[num]+1.5*n2[index][num]], e2[index][num], linestyle=p2[index][num], color=j2[index][num], linewidth=2.25, label=labelstring)

ax2.axis([-13.0, 15.0, 15.0, 30.0], fontsize=18)
ax2.tick_params(axis='x',labelsize=16)
ax2.set_ylabel(r'$\mathrm{E\ (MeV)}$', fontsize=18)
annotation_string = r'$\mathrm{^{15}N}$'
ax2.annotate(annotation_string, fontsize=22, xy=(0.915, 0.1), xycoords='axes fraction')
plt.setp(ax1, xticks=[-9.0,0.0,9.0], xticklabels=[r'$\beta=0$',r'$\beta=1$',r'$\mathrm{Exp.}$'])

ax2.legend(loc='upper right', frameon=False, fontsize=15, labelspacing=0.0)



plt.tight_layout()
plt.savefig('N15_O15_EOM_2.pdf', format='pdf', bbox_inches='tight')
plt.show()
