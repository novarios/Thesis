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

filename1 = '/home/sam/Documents/thesis/data/21N_levels.dat'
filename2 = '/home/sam/Documents/thesis/data/PR_final_7_14.dat'

e1 = []
jp1 = []
j1 = []
p1 = []

e2 = [[] for num in range(3)]
jp2 = [[] for num in range(3)]
j2 = [[] for num in range(3)]
p2 = [[] for num in range(3)]

with open(filename1) as f1:
    data1 = f1.read()
data1 = data1.split('\n')

with open(filename2) as f2:
    data2 = f2.read()
data2 = data2.split('\n')

num_states = 25
num = 1
#while(num < num_states and num < len(data1)-1):
for num in [1,2]:
    line = data1[num].split("\t")
    e1.append([float(line[4])/1000.0,float(line[4])/1000.0])
    jp = str(line[6])
    jp = jp.replace('(','').replace(')','').replace(' ','')

    if( len(jp) != 0 ):
        if( len(jp) > 4 ):
            jp = ''
        if(jp not in jp1):
            jp1.append(jp)
        else:
            jp1.append('')
    else:
        if('J^{\pi}' not in jp1):
            jp1.append('J^{\pi}')
        else:
            jp1.append('')            

    if( len(jp) == 0 ):
        p1.append('-')
    elif( jp[-1] == '-' ):
        p1.append('--')
    else:
        p1.append('-')

    if( len(jp) == 0 ):
        j1.append('k')
    else:
        jp = jp[:-1]

    if( jp == '1/2' ):
        j1.append('b')
    elif( jp == '3/2' ):
        j1.append('r')
    elif( jp == '5/2' ):
        j1.append('g')
    elif( jp == '7/2' ):
        j1.append('m')
    elif( jp == '9/2' ):
        j1.append('c')

    num = num + 1

indices = {0:0, 1:1, 4:2}

num1 = [1, 1, 1]
num2 = 1
while((num1[0] < num_states or num1[1] < num_states or num1[2] < num_states) and num2 < len(data2)-1):
    line = data2[num2].split()
    if(  float(line[0]) != 16.0 ):
        num2 = num2 + 1
        continue
    index = indices[int(line[2])]
    e2[index].append([float(line[11]),float(line[11])])
    jp = str(line[6])[1:-1]

    if( jp[0] == 'p' or jp[0] == 'f'):
        p2[index].append('--')
        jp = jp + '-'
    else:
        p2[index].append('-')
        jp = jp + '+'

    jp = jp[1:]

    if(jp not in jp2[0] and jp not in jp2[1] and jp not in jp2[2] and jp not in jp1):
        jp2[index].append(jp)
    else:
        jp2[index].append('')

    if( jp[:-1] == '1/2' ):
        j2[index].append('b')
    elif( jp[:-1] == '3/2' ):
        j2[index].append('r')
    elif( jp[:-1] == '5/2' ):
        j2[index].append('g')
    elif( jp[:-1] == '7/2' ):
        j2[index].append('m')
    elif( jp[:-1] == '9/2' ):
        j2[index].append('c')

    num1[index] = num1[index] + 1
    num2 = num2 + 1


filename3 = '/home/sam/Documents/thesis/data/21O_levels.dat'
filename4 = '/home/sam/Documents/thesis/data/PR_final_8_13.dat'

e3 = []
jp3 = []
j3 = []
p3 = []

e4 = [[] for num in range(3)]
jp4 = [[] for num in range(3)]
j4 = [[] for num in range(3)]
p4 = [[] for num in range(3)]

with open(filename3) as f3:
    data3 = f3.read()
data3 = data3.split('\n')

with open(filename4) as f4:
    data4 = f4.read()
data4 = data4.split('\n')

num_states = 25
num = 1
#while(num < num_states and num < len(data3)-1):
for num in [1,2]:
    line = data3[num].split("\t")
    e3.append([float(line[4])/1000.0,float(line[4])/1000.0])
    jp = str(line[6])
    jp = jp.replace('(','').replace(')','').replace(' ','')

    if( len(jp) != 0 ):
        if( len(jp) > 4 ):
            jp = ''
        if(jp not in jp3):
            jp3.append(jp)
        else:
            jp3.append('')
    else:
        if('J^{\pi}' not in jp3):
            jp3.append('J^{\pi}')
        else:
            jp3.append('')            

    if( len(jp) == 0 ):
        p3.append('-')
    elif( jp[-1] == '-' ):
        p3.append('--')
    else:
        p3.append('-')

    if( len(jp) == 0 ):
        j3.append('k')
    else:
        jp = jp[:-1]

    if( jp == '1/2' ):
        j3.append('b')
    elif( jp == '3/2' ):
        j3.append('r')
    elif( jp == '5/2' ):
        j3.append('g')
    elif( jp == '7/2' ):
        j3.append('m')
    elif( jp == '9/2' ):
        j3.append('c')

    num = num + 1

indices = {0:0, 1:1, 4:2}

num1 = [1, 1, 1]
num2 = 1
while((num1[0] < num_states or num1[1] < num_states or num1[2] < num_states) and num2 < len(data4)-1):
    line = data4[num2].split()
    if(  float(line[0]) != 16.0 ):
        num2 = num2 + 1
        continue
    index = indices[int(line[2])]
    e4[index].append([float(line[11]),float(line[11])])
    jp = str(line[6])[1:-1]

    if( jp[0] == 'p' or jp[0] == 'f'):
        p4[index].append('--')
        jp = jp + '-'
    else:
        p4[index].append('-')
        jp = jp + '+'

    jp = jp[1:]

    if(jp not in jp4[0] and jp not in jp4[1] and jp not in jp4[2] and jp not in jp3):
        jp4[index].append(jp)
    else:
        jp4[index].append('')

    if( jp[:-1] == '1/2' ):
        j4[index].append('b')
    elif( jp[:-1] == '3/2' ):
        j4[index].append('r')
    elif( jp[:-1] == '5/2' ):
        j4[index].append('g')
    elif( jp[:-1] == '7/2' ):
        j4[index].append('m')
    elif( jp[:-1] == '9/2' ):
        j4[index].append('c')

    num1[index] = num1[index] + 1
    num2 = num2 + 1
    
#xa = [[-14.0,-10.0], [-6.0,-2.0], [2.0,6.0], [10.0,14.0]]
xa = [[-12.0,-6.0], [-3.0,3.0], [2.0,6.0], [6.0,12.0]]

plt.rc('font', family='serif')

fig = plt.figure(figsize=(16, 6))
gs = gridspec.GridSpec(1, 2)

ax1 = plt.subplot(gs[0])
for num in range(len(e1)):
    if( jp1[num] == '' ):
        labelstring = ""
    else:
        labelstring = r'$\mathrm{' + jp1[num] + '}$'

    if(p1[num] == '--'):
        ax1.plot(xa[3], e1[num], linestyle=p1[num], dashes=(7,1), color=j1[num], linewidth=2.5, label=labelstring)
    else:
        ax1.plot(xa[3], e1[num], linestyle=p1[num], color=j1[num], linewidth=2.5, label=labelstring)

for index in range(3):
    offset = e2[index][0][0]
    for num in range(len(e2[index])):
        e2[index][num][0] -= offset
        e2[index][num][1] -= offset
        
for index in [0,1]:
    for num in range(len(e2[index])):
        if( jp2[index][num] == '' ):
            labelstring = ""
        else:
            labelstring = r'$\mathrm{' + jp2[index][num] + '}$'

        if(p2[index][num] == '--'):
            ax1.plot(xa[index], e2[index][num], linestyle=p2[index][num], dashes=(7,1), color=j2[index][num], linewidth=2.5, label=labelstring)
        else:
            ax1.plot(xa[index], e2[index][num], linestyle=p2[index][num], color=j2[index][num], linewidth=2.5, label=labelstring)

ax1.plot([xa[0][1], xa[1][0]], [e2[0][0], e2[1][0]], linestyle=':', color='b', linewidth=2.5)
ax1.plot([xa[1][1], xa[3][0]], [e2[1][0], e1[0]], linestyle=':', color='b', linewidth=2.5)

ax1.plot([xa[0][1], xa[1][0]], [e2[0][1], e2[1][1]], linestyle=':', color='r', linewidth=2.5)
ax1.plot([xa[1][1], xa[3][0]], [e2[1][1], e1[1]], linestyle=':', color='r', linewidth=2.5)

#ax1.plot([xa[0][1], xa[1][0]], [e2[0][4], e2[1][2]], linestyle=':', color='r', linewidth=2.5)
#ax1.plot([xa[1][1], xa[3][0]], [e2[1][2], e1[2]], linestyle=':', color='r', linewidth=2.5)

ax1.axis([-13.0, 15.0, -0.5, 10.5], fontsize=22)
ax1.tick_params(axis='x',labelsize=20)
ax1.tick_params(axis='y',labelsize=16)
ax1.set_ylabel(r'$\mathrm{E\ (MeV)}$', fontsize=20)
annotation_string = r'$\mathrm{^{21}N}$'
ax1.annotate(annotation_string, fontsize=24, xy=(0.9, 0.05), xycoords='axes fraction')
plt.setp(ax1, xticks=[-9.0,0.0,9.0], xticklabels=[r'$\beta=0$',r'$\beta=1$',r'$\mathrm{Exp.}$'])

ax1.legend(loc='upper right', frameon=False, fontsize=18, labelspacing=0.0)



ax2 = plt.subplot(gs[1])
for num in range(len(e3)):
    if( jp3[num] == '' ):
        labelstring = ""
    else:
        labelstring = r'$\mathrm{' + jp3[num] + '}$'

    if(p3[num] == '--'):
        ax2.plot(xa[3], e3[num], linestyle=p3[num], dashes=(7,1), color=j3[num], linewidth=2.5, label=labelstring)
    else:
        ax2.plot(xa[3], e3[num], linestyle=p3[num], color=j3[num], linewidth=2.5, label=labelstring)

for index in range(3):
    offset = e4[index][0][0]
    for num in range(len(e4[index])):
        e4[index][num][0] -= offset
        e4[index][num][1] -= offset
        
for index in [0,1]:
    for num in range(len(e4[index])):
        if( jp4[index][num] == '' ):
            labelstring = ""
        else:
            labelstring = r'$\mathrm{' + jp4[index][num] + '}$'

        if(p4[index][num] == '--'):
            ax2.plot(xa[index], e4[index][num], linestyle=p4[index][num], dashes=(7,1), color=j4[index][num], linewidth=2.5, label=labelstring)
        else:
            ax2.plot(xa[index], e4[index][num], linestyle=p4[index][num], color=j4[index][num], linewidth=2.5, label=labelstring)

ax2.plot([xa[0][1], xa[1][0]], [e4[0][0], e4[1][0]], linestyle=':', color='g', linewidth=2.5)
ax2.plot([xa[1][1], xa[3][0]], [e4[1][0], e3[0]], linestyle=':', color='g', linewidth=2.5)

ax2.plot([xa[0][1], xa[1][0]], [e4[0][2], e4[1][1]], linestyle=':', color='b', linewidth=2.5)
ax2.plot([xa[1][1], xa[3][0]], [e4[1][1], e3[1]], linestyle=':', color='b', linewidth=2.5)

#ax2.plot([xa[0][1], xa[1][0]], [e4[0][3], e4[1][2]], linestyle=':', color='g', linewidth=2.5)
#ax2.plot([xa[1][1], xa[3][0]], [e4[1][2], e3[2]], linestyle=':', color='g', linewidth=2.5)


ax2.axis([-13.0, 15.0, -0.5, 10.5], fontsize=22)
ax2.tick_params(axis='x',labelsize=20)
plt.setp(ax2.get_yticklabels(), visible=False)
annotation_string = r'$\mathrm{^{21}O}$'
ax2.annotate(annotation_string, fontsize=24, xy=(0.9, 0.05), xycoords='axes fraction')
plt.setp(ax2, xticks=[-9.0,0.0,9.0], xticklabels=[r'$\beta=0$',r'$\beta=1$',r'$\mathrm{Exp.}$'])

ax2.legend(loc='upper right', frameon=False, fontsize=18, labelspacing=0.0)


plt.tight_layout()
plt.savefig('N21_O21_EOM_2.pdf', format='pdf', bbox_inches='tight')
plt.show()
