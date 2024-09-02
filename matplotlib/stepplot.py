import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.array([2, 4, 6,5, 8])
y = np.array([1, 3, 5,5, 7])

plt.step(x,y, marker='o', color='r',label='python', mfc='g', ms=10 )
plt.legend(loc='best')
plt.grid()
plt.show()
