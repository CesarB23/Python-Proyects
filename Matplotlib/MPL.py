import numpy as np
import matplotlib.pyplot as plt
import math
plt.grid()
x = np.arange(0,10,0.1)
y = np.sin(x/2)
y2 = np.cos(x/2)
x2 = np.linspace(0,5,10)
y3 = x2**2
plt.plot(x,y,"--r")
plt.plot(x,y2,"g")
#   plt.plot(x2,y3)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Sin-Cos")
plt.show()

