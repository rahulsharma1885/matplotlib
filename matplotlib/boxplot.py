import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

x = [2, 4, 5, 7, 9]
x1 = [5, 7, 9, 6, 3]


# plt.boxplot([x, x1], labels=['python', 'c++'])
plt.boxplot([x, x1], labels=['python', 'c++'], notch=False, vert=True, widths=0.05, whis=True, sym='g+', boxprops=dict(color='r'),whiskerprops=dict(color='g'), capprops=dict(color='y'))

pylab.boxplot([x, x1], labels=['python', 'c++'], notch=False, vert=True, widths=0.05, whis=True, sym='g+', boxprops=dict(color='r'),whiskerprops=dict(color='g'), capprops=dict(color='y'))
# plt.grid() 
plt.show()


