import matplotlib.pyplot as plt
x=[10, 20, 30, 40]
y=[34, 40, 10, 46]
y1=['c', 'c++', 'java', 'python']

plt.pie(x, labels=y1, radius=1.5, autopct="%f%%")
plt.pie([1], colors='white')
plt.show()