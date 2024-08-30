import pandas as pd
import matplotlib.pyplot as plt

data= [32, 25, 35, 45, 10, 15]

plt.hist(data)
# plt.hist(data, bins=[10, 25, 40, 55, 70])
plt.grid()
plt.show()