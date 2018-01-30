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

filename1 = '/home/sam/Documents/thesis/data/PA_EOM_COM.dat'
filename2 = '/home/sam/Documents/thesis/data/PR_EOM_COM.dat'

hw0_1 = []
e0_1 = []
hw1_1 = []
e1_1 = []
hwa_1 = []

hw0_2 = []
e0_2 = []
hw1_2 = []
e1_2 = []
hwa_2 = []

hw0_3 = []
e0_3 = []
hw1_3 = []
e1_3 = []
hwa_3 = []

hw0_4 = []
e0_4 = []
hw1_4 = []
e1_4 = []
hwa_4 = []

hw0_5 = []
e0_5 = []
hw1_5 = []
e1_5 = []
hwa_5 = []

hw0_6 = []
e0_6 = []
hw1_6 = []
e1_6 = []
hwa_6 = []

hw0_7 = []
e0_7 = []
hw1_7 = []
e1_7 = []
hwa_7 = []

hw0_8 = []
e0_8 = []
hw1_8 = []
e1_8 = []
hwa_8 = []

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
        e0_1.append(float(line[6]))
    elif( num - num%6 == 6 ):
        hw0_2.append(float(line[0]))
        e0_2.append(float(line[6]))
    elif( num - num%6 == 12 ):
        hw0_3.append(float(line[0]))
        e0_3.append(float(line[6]))
    elif( num - num%6 == 18 ):
        hw0_4.append(float(line[0]))
        e0_4.append(float(line[6]))

    if( num >= 24 and num%2 == 0 ):
        line2 = data1[num+1].split()
        if( num >= 24 and num < 36 ):
            if( float(line[7]) < float(line2[7]) ):
                hw1_1.append(float(line[0]))
                e1_1.append(float(line[7]))
                hwa_1.append(float(line[1]))
            else:
                hw1_1.append(float(line2[0]))
                e1_1.append(float(line2[7]))
                hwa_1.append(float(line2[1]))
        if( num >= 36 and num < 48 ):
            if( float(line[7]) < float(line2[7]) ):
                hw1_2.append(float(line[0]))
                e1_2.append(float(line[7]))
                hwa_2.append(float(line[1]))
            else:
                hw1_2.append(float(line2[0]))
                e1_2.append(float(line2[7]))
                hwa_2.append(float(line2[1]))
        if( num >= 48 and num < 60 ):
            if( float(line[7]) < float(line2[7]) ):
                hw1_3.append(float(line[0]))
                e1_3.append(float(line[7]))
                hwa_3.append(float(line[1]))
            else:
                hw1_3.append(float(line2[0]))
                e1_3.append(float(line2[7]))
                hwa_3.append(float(line2[1]))
        if( num >= 60 and num < 72 ):
            if( float(line[7]) < float(line2[7]) ):
                hw1_4.append(float(line[0]))
                e1_4.append(float(line[7]))
                hwa_4.append(float(line[1]))
            else:
                hw1_4.append(float(line2[0]))
                e1_4.append(float(line2[7]))
                hwa_4.append(float(line2[1]))

for num in range(len(data2)):
    line = data2[num].split()
    if( num - num%6 == 0 ):
        hw0_5.append(float(line[0]))
        e0_5.append(float(line[6]))
    elif( num - num%6 == 6 ):
        hw0_6.append(float(line[0]))
        e0_6.append(float(line[6]))
    elif( num - num%6 == 12 ):
        hw0_7.append(float(line[0]))
        e0_7.append(float(line[6]))
    elif( num - num%6 == 18 ):
        hw0_8.append(float(line[0]))
        e0_8.append(float(line[6]))

    if( num >= 24 and num%2 == 0 ):
        line2 = data2[num+1].split()
        if( num >= 24 and num < 36 ):
            if( float(line[7]) < float(line2[7]) ):
                hw1_5.append(float(line[0]))
                e1_5.append(float(line[7]))
                hwa_5.append(float(line[1]))
            else:
                hw1_5.append(float(line2[0]))
                e1_5.append(float(line2[7]))
                hwa_5.append(float(line2[1]))
        if( num >= 36 and num < 48 ):
            if( float(line[7]) < float(line2[7]) ):
                hw1_6.append(float(line[0]))
                e1_6.append(float(line[7]))
                hwa_6.append(float(line[1]))
            else:
                hw1_6.append(float(line2[0]))
                e1_6.append(float(line2[7]))
                hwa_6.append(float(line2[1]))
        if( num >= 48 and num < 60 ):
            if( float(line[7]) < float(line2[7]) ):
                hw1_7.append(float(line[0]))
                e1_7.append(float(line[7]))
                hwa_7.append(float(line[1]))
            else:
                hw1_7.append(float(line2[0]))
                e1_7.append(float(line2[7]))
                hwa_7.append(float(line2[1]))
        if( num >= 60 and num < 72 ):
            if( float(line[7]) < float(line2[7]) ):
                hw1_8.append(float(line[0]))
                e1_8.append(float(line[7]))
                hwa_8.append(float(line[1]))
            else:
                hw1_8.append(float(line2[0]))
                e1_8.append(float(line2[7]))
                hwa_8.append(float(line2[1]))

print(e0_1)
print(hw0_1)
print(e1_1)
print(hw1_1)
print(hwa_1)

print(e0_2)
print(hw0_2)
print(e1_2)
print(hw1_2)
print(hwa_2)

print(e0_3)
print(hw0_3)
print(e1_3)
print(hw1_3)
print(hwa_3)

print(e0_4)
print(hw0_4)
print(e1_4)
print(hw1_4)
print(hwa_4)

#hw0_1_1 = hw0_1[:-1]
#e0_1_1 = e0_1[:-1]
#hw0_2_1 = hw0_2[:-1]
#e0_2_1 = e0_2[:-1]

plt.rc('font', family='serif')

fig = plt.figure(figsize=(11, 11))
gs = gridspec.GridSpec(2, 2)


ax1 = plt.subplot(gs[0])
plt.plot(hw0_1, e0_1, '-', marker='o', color='k', label=r'$\mathrm{{}^{17}O(5/2^{+})}$')
plt.plot(hw0_2, e0_2, '--', marker='s', color='r', label=r'$\mathrm{{}^{17}F(5/2^{+})}$')
plt.plot(hw0_3, e0_3, ':', marker='^', color='b', label=r'$\mathrm{{}^{23}O(1/2^{+})}$')
plt.plot(hw0_4, e0_4, '-.', marker='v', color='g', label=r'$\mathrm{{}^{23}F(5/2^{+})}$')
plt.axis([6.0, 30.0, -0.5, 9.0])
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_ylabel(r'$\mathrm{E_{cm}(\omega)\ (MeV)}$', fontsize=15)

ax1.legend(bbox_to_anchor=(0.325,0.975), frameon=False, fontsize=11)


ax2 = plt.subplot(gs[1])
plt.plot(hw1_1, e1_1, '-', marker='o', color='k', label=r'$\mathrm{{}^{17}O(5/2^{+})}$')
plt.plot(hw1_2, e1_2, '--', marker='s', color='r', label=r'$\mathrm{{}^{17}F(5/2^{+})}$')
plt.plot(hw1_3, e1_3, ':', marker='^', color='b', label=r'$\mathrm{{}^{23}O(1/2^{+})}$')
plt.plot(hw1_4, e1_4, '-.', marker='v', color='g', label=r'$\mathrm{{}^{23}F(5/2^{+})}$')
plt.axis([6.0, 30.0, 0.0, 1.0])
plt.setp(ax2.get_xticklabels(), visible=False)
ax2.set_ylabel(r'$\mathrm{E_{cm}(\widetilde{\omega})\ (MeV)}$', fontsize=15)

inset_axes2 = inset_axes(ax2,width="50%",height=1.5,loc=1)
plt.plot(hw0_1, hwa_1, '-', marker='o', color='r')
plt.plot(hw0_3, hwa_3, '-.', marker='v', color='b')
plt.xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=14)
plt.ylabel(r'$\mathrm{\hbar\widetilde{\omega}\ (MeV)}$', fontsize=14)
annotation_string = r'$\mathrm{^{17}O,^{17}F}$'
plt.annotate(annotation_string, fontsize=12, xy=(0.25, 0.75), xycoords='axes fraction')
annotation_string = r'$\mathrm{^{23}O,^{23}F}$'
plt.annotate(annotation_string, fontsize=12, xy=(0.50, 0.25), xycoords='axes fraction')

ax2.legend(bbox_to_anchor=(0.325,0.975), frameon=False, fontsize=11)



ax3 = plt.subplot(gs[2])
plt.plot(hw0_5, e0_5, '-', marker='o', color='k', label=r'$\mathrm{{}^{15}N(1/2^{-})}$')
plt.plot(hw0_6, e0_6, '--', marker='s', color='r', label=r'$\mathrm{{}^{15}O(1/2^{-})}$')
plt.plot(hw0_7, e0_7, ':', marker='^', color='b', label=r'$\mathrm{{}^{21}N(1/2^{-})}$')
plt.plot(hw0_8, e0_8, '-.', marker='v', color='g', label=r'$\mathrm{{}^{21}O(5/2^{+})}$')
plt.axis([6.0, 30.0, -0.5, 10.0])
ax3.set_xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=15)
ax3.set_ylabel(r'$\mathrm{E_{cm}(\omega)\ (MeV)}$', fontsize=15)

ax3.legend(bbox_to_anchor=(0.325,0.975), frameon=False, fontsize=11)


ax4 = plt.subplot(gs[3])
plt.plot(hw1_5, e1_5, '-', marker='o', color='k', label=r'$\mathrm{{}^{15}N(1/2^{-})}$')
plt.plot(hw1_6, e1_6, '--', marker='s', color='r', label=r'$\mathrm{{}^{15}O(1/2^{-})}$')
plt.plot(hw1_7, e1_7, ':', marker='^', color='b', label=r'$\mathrm{{}^{21}N(1/2^{-})}$')
plt.plot(hw1_8, e1_8, '-.', marker='v', color='g', label=r'$\mathrm{{}^{21}O(5/2^{+})}$')
plt.axis([6.0, 30.0, -0.1, 1.0])
ax4.set_xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=15)
ax4.set_ylabel(r'$\mathrm{E_{cm}(\widetilde{\omega})\ (MeV)}$', fontsize=15)

inset_axes4 = inset_axes(ax4,width="50%",height=1.5,loc=1)
plt.plot(hw0_5, hwa_5, '-', marker='o', color='r')
plt.plot(hw0_7, hwa_7, '-.', marker='v', color='b')
plt.xlabel(r'$\mathrm{\hbar\omega\ (MeV)}$', fontsize=14)
plt.ylabel(r'$\mathrm{\hbar\widetilde{\omega}\ (MeV)}$', fontsize=14)
annotation_string = r'$\mathrm{^{15}N,^{15}O}$'
plt.annotate(annotation_string, fontsize=12, xy=(0.25, 0.75), xycoords='axes fraction')
annotation_string = r'$\mathrm{^{21}N,^{21}O}$'
plt.annotate(annotation_string, fontsize=12, xy=(0.50, 0.25), xycoords='axes fraction')

ax4.legend(bbox_to_anchor=(0.325,0.975), frameon=False, fontsize=11)


#ax.xaxis.set_major_locator(majorLocatorX)
#ax.xaxis.set_minor_locator(minorLocatorX)
#ax.yaxis.set_major_locator(majorLocatorY)
#ax.yaxis.set_minor_locator(minorLocatorY)

plt.tight_layout()
plt.savefig('EOM-CoM.pdf', format='pdf', bbox_inches='tight')
plt.show()
