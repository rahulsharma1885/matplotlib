import matplotlib.pyplot as plt
import pandas as pd

# data= pd.read_csv('d.csv')

# plt.stem(data['elo_n'], data['win_equiv'])
# plt.legend()
# plt.show()

x=[1,2,3,4,5,6]
y=[2,2,5,6,4,3]
plt.stem(x,y, linefmt=':',bottom=0, markerfmt='r+',basefmt='y',use_line_collection=False, label='python')
# plt.stem(x,y, linefmt=':',bottom=9, markerfmt='r+',basefmt='y',use_line_collection=False, label='python')
# plt.stem(x,y, linefmt=':', markerfmt='r+',basefmt='y',use_line_collection=False, label='python', orientation='horizontal')
plt.legend()
plt.show()