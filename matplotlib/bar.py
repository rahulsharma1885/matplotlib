import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

children= [10, 39, 40, 50, 20]
color= ['red', 'yellow', 'green', 'pink', 'purple']
# result= plt.bar(color, children, color='pink', label='rahul', linestyle='dotted', linewidth=3)  # by default vertical
result= plt.bar(color, children, color='pink', label='rahul', linestyle='dotted', linewidth=3)  #horizontal
# result= plt.xticks(rotation='vertical')  
plt.title('demo')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc='best')
plt.grid()
plt.show()