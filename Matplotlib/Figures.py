import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(0,20,0.05)
print(x)
y = x**2
y1 = np.sin(x)
fig_1, axes_1 = plt.subplots(figsize=(8,4),nrows=1,ncols=3)
plt.tight_layout()
axes_1[1].set_title("Plot 2")
axes_1[1].set_xlabel("X")
axes_1[1].set_ylabel("Y")
axes_1[1].plot(x,y)
axes_1[2].plot(x,y1)
plt.show()