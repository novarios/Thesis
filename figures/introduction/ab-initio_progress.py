import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

majorLocatorX = MultipleLocator(5)
minorLocatorX = MultipleLocator(5)
majorLocatorY = MultipleLocator(20)
minorLocatorY = MultipleLocator(10)

a1985 = [2]
a1987 = [3]
a1995 = [4, 5]
a1996 = [6]
a1997 = [7]
a2000 = [8, 16]
a2002 = [9, 10]
a2003 = [11, 13]
a2005 = [12]
a2009 = [17]
a2010 = [18, 20, 21, 22, 23, 24]
a2011 = [15, 39, 40, 41, 42, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 60, 61, 62]
a2012 = [26, 28, 36, 68, 78, 88, 90, 100, 106, 114, 116, 118, 120, 132]
a2013 = [19, 25, 27, 34, 37, 38, 43, 44, 45, 46, 58, 64, 66, 70, 72, 74, 76, 80, 82, 84, 86, 92, 94, 96, 98, 102, 104, 108, 110]
a2014 = [29, 30, 31, 32, 33, 35, 57, 59, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 112, 122, 124, 126, 128, 130, 134, 136, 138, 140, 142, 144, 146]

y1985 = [1985] * len(a1985)
y1987 = [1987] * len(a1987)
y1995 = [1995] * len(a1995)
y1997 = [1997] * len(a1997)
y2000 = [2000] * len(a2000)
y2002 = [2002] * len(a2002)
y2003 = [2003] * len(a2003)
y2005 = [2005] * len(a2005)
y2009 = [2009] * len(a2009)
y2010 = [2010] * len(a2010)
y2011 = [2011] * len(a2011)
y2012 = [2012] * len(a2012)
y2013 = [2013] * len(a2013)
y2014 = [2014] * len(a2014)

years = y1985 + y1987 + y1995 + y1997 + y2000 + y2002 + y2003 + y2005 + y2009 + y2010 + y2011 + y2012 + y2013 + y2014
masses = a1985 + a1987 + a1995 + a1997 + a2000 + a2002 + a2003 + a2005 + a2009 + a2010 + a2011 + a2012 + a2013 + a2014

x1 = np.linspace(1985, 2020, 100)
y1 = 0.01 * np.exp(0.34657 * (x1 - 1985))

plt.rc('font', family='serif')

fig, ax = plt.subplots()
#ax.scatter(years, masses, 75, marker='o', color=(1.0,0.4,0), edgecolor='black', linewidth = 0.9)

plt.scatter(years, masses, 75, marker='o', color=(1.0,0.4,0), edgecolor='black', linewidth = 0.9)
#plt.plot(x1, y1)
plt.xlabel(r'$\mathrm{Year}$', fontsize=16)
plt.ylabel(r'$\mathrm{Mass\ Number\ (A)}$', fontsize=16)
plt.axis([1984, 2015, 0, 150])

ax.xaxis.set_major_locator(majorLocatorX)
ax.xaxis.set_minor_locator(minorLocatorX)
ax.yaxis.set_major_locator(majorLocatorY)
ax.yaxis.set_minor_locator(minorLocatorY)

#plt.xaxis.set_major_locator(majorLocatorX)
#plt.xaxis.set_minor_locator(minorLocatorX)
#plt.yaxis.set_major_locator(majorLocatorY)
#plt.yaxis.set_minor_locator(minorLocatorY)

plt.savefig('ab-initio_progress.pdf', format='pdf', bbox_inches='tight')
plt.show()
