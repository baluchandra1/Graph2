# This is a sample Python script.

'''Graph plotting code for trignometric functions.
XY plot
X axis range in divisions of pi/4'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


#################SAMPLE SPACE#######################
fig, ax = plt.subplots()
######Function Range############
#xrange = 2*np.pi     #X axis in terms of pi/4
xrange = [-2*np.pi, 2*np.pi]

yrange = [-1.2, 1.2]

x = np.linspace(xrange[0], xrange[1], 200000)
plt.axhline(y = 0, color = 'k', linestyle = '-')
plt.axvline(x = 0, color = 'k', linestyle = '-')


##########Function###########
function = [[np.sin(x),'$y=Sin(x)$'],[np.cos(x),'$y=Cos(x)$'] ]
#function_label = ['$y=x^2$', '$y=x^3$']

def fctn(function, xrange):
    i = len(function)
    #x = np.linspace(xrange[0], xrange[1], 200000)
    for y in function:
        x = np.linspace(xrange[0], xrange[1], 200000)
        ax.plot(x, y[0],label = y[1])

        plt.legend()

        #print(y)
    return plt.show()
#plt.grid()
#fctn(function,xrange)

############################################################
q = ax.xaxis.set_major_locator(MultipleLocator(np.pi/4))
def frac3(num,d0):
    gcd = np.gcd(num, d0)
    n1 = num/gcd
    d1 = d0/gcd

    if n1 == d1:
        wh_num = 'nil'
        deno = 'nil'
        numer = 'nil'
    elif n1>d1:
        wh_num = n1//d1
        st = n1%d1
        if st == 0:
            deno = 'nil'
            numer = 'nil'
        else:
            deno = d1
            numer = st
    elif n1<d1:
        wh_num = 'nil'
        deno = d1
        numer = n1
    else:
        wh_num = 0
        deno = 'nil'
        numer = 'nil'


    return(wh_num, numer, deno)

def format_func(value, tick_number):
    """Formatter for setting the xticks to multiples of \pi/4."""
    k = int(np.round(4*value/np.pi))
    if k<0:
        sign = "-"
    else:
        sign = ""
#####################################
    f = frac3(abs(k), 4)
    wh_num = f[0]
    numer = f[1]
    denom = f[2]

    if wh_num == 'nil' and numer == 'nil' and denom == 'nil':
        return '$' + sign + '\pi' + '$'
    elif wh_num == 'nil' and numer == 0:
        return '0'
    elif wh_num == 'nil':
        return '$' + sign + r'\frac{' + str(int(numer)) + '}{' + str(int(denom)) + '}' + '\pi' + '$'
    elif numer == 'nil' and denom == 'nil':
        return '$' + sign + str(int(wh_num)) + '\pi' + '$'
    else:
        return '$' + sign + str(int(wh_num)) + r'\frac{' + str(int(numer)) + '}{' + str(int(denom)) + '}' + '\pi' + '$'
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
############################################################



ax.set(xlabel='x-axis', ylabel='y-axis',
       title='Function')
plt.legend()
plt.ylim(yrange[0], yrange[1])
plt.grid()
fctn(function,xrange)
