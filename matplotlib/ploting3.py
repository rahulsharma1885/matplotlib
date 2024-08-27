import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df= pd.read_csv('d.csv')
# result= plt.plot(df['fran_id'], df['date_game'], color='red', linestyle='solid', linewidth=3, marker='o', label='rahul')
# result= plt.plot(df['seasongame'], df['opp_id'], color='green', linestyle='solid', linewidth=3, marker='o', label='seasongame')

result= plt.bar(df['fran_id'], df['date_game'], color='red', linestyle='solid', linewidth=3, label='rahul')
result= plt.bar(df['seasongame'], df['opp_id'], color='green', linestyle='solid', linewidth=3, label='seasongame')

plt.xlabel('fan id')
plt.ylabel('date_game')
plt.legend(loc='best')
plt.show()

# print(df)