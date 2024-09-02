import matplotlib.pyplot as plt

data = [45, 55, 60, 70, 80, 85, 90, 95, 100, 60, 70, 80, 90, 100, 100]
plt.hist(data, bins=15, edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.title('Histogram of Test Scores')
plt.show()
