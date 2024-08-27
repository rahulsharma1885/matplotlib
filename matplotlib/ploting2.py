import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv('d.csv')
result= plt.bar(df['fran_id'], df['date_game'])
plt.show()

# print(df)