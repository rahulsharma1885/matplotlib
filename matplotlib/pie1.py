import matplotlib.pyplot as plt
x=[10, 20, 30, 40]
y=['c', 'c++', 'java', 'python']

exp=[0.05, 0,0,0]
col=['r', 'b', 'g', 'y']

plt.pie(x, labels=y, autopct="%0.1f%%", explode=exp, colors=col,radius=1.5, startangle=90, labeldistance=1.1, rotatelabels=False, counterclock=False)
plt.show()
