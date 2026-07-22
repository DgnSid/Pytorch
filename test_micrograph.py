import math
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as inline
def f(x):
    return 3*x**2 - 4*x +5

#print(f(3.0))

xs= np.arange(-5, 5, 0.25)
#print(xs)
ys= f(xs)
#print(ys)
plt.plot(xs, ys)
#plt.show()

h=0.0001
x=3  
print((f(x+h) - f(x)) / h)