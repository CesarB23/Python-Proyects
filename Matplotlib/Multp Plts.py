import numpy as np
import matplotlib.pyplot as plt

plt.subplot(1,3,1)
x = np.arange(0,10,0.1)
y = np.sin(x)
y2 = np.cos(x)
x2 = np.linspace(0,5,10)
y3 = x2**2
plt.plot(x,y,"--r")
plt.subplot(1,3,2)
plt.plot(x,y2,"g")
plt.subplot(1,3,3)
plt.plot(x2,y3,"b")
plt.show()