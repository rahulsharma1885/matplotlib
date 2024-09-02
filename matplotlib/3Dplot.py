import matplotlib.pyplot as plt

x = [0, 1, 5, 25]
y = [0, 10, 13, 0]
z = [0, 13, 20, 9]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, s=[100, 100, 100, 100])
ax.plot(x, y, z)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()