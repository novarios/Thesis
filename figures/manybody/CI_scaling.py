import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial
from matplotlib.ticker import MultipleLocator

## degeneracy at level n for spin +- 1/2
def degen (n):
    return (n + 1) * (n + 2)

## total number of states for N shells
def num_states (N):
    num = 0
    for x in range(0,N+1):
        num = num + degen(x)
    return num

## ln(n!)
def logfac (n):
    if( n == 0 ):
        return 0.0
    fac = 0.0
    for x in range(1,n+1):
        fac = fac + np.log(x)
    return fac

## choose n from N objects
def choose (N, n):
    return np.exp(logfac(N) - logfac(N - n) - logfac(n))

x = np.zeros(10)
y1 = np.zeros(10)
y2 = np.zeros(10)
y3 = np.zeros(10)
y4 = np.zeros(10)

for i in range(5,15):
    x[i-5] = i
    y1[i-5] = (choose(num_states(i),2)/2)**4
    y2[i-5] = (choose(num_states(i),8)/2)**4
    y3[i-5] = (choose(num_states(i),20)/2)**4
    y4[i-5] = (choose(num_states(i),28)/2)**4

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.yscale('log')

plt.savefig('CI_scaling.pdf', format='pdf', bbox_inches='tight')
plt.show()
