import numpy as np
import matplotlib.pyplot as plt
import random

# length= random.randint(1, 20)
# print(length)
# x= np.arange(length)
# y= np.arange(length)

# plt.fill_between(x,y, color='green', where=(x>=2)&(x<=20))
# plt.show()

x=np.array([1,2,3,4])
y=np.array([1,2,3,4])


plt.fill_between(x,y, color='green', where=(x>=2)&(x<=4))
plt.show()