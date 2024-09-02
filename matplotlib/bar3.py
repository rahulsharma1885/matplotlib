import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D']
values1 = [10, 24, 36, 18]
values2 = [15, 20, 30, 25]

x= np.arange(len(categories))

bar_width=0.35

plt.bar(x-bar_width / 2 , values1, bar_width, color='red', label='Dataset 1')
plt.bar(x+bar_width / 2 , values2,  bar_width, color='lightblue', label='Dataset 1')

plt.title('demo')
plt.xlabel('r')
plt.ylabel('y')
plt.legend(loc='best')
plt.show()