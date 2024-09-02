import matplotlib.pylab as pt
import matplotlib.pyplot as plt


x = [1,2,3,4]
area1= [1,2,3,4]
area2 = [2,3,4,5]
area3 = [1,3,2,4]

l=['area1', 'area2', 'area3']
plt.stackplot(x,area1, area2, area3, labels=l)
plt.title('demo')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc=2)
pt.show()
