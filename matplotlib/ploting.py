import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# price= [1000, 3000, 4000, 20000]
# date=  [2021, 2022, 2023, 2024]

# result= plt.plot(date, price)

df = pd.read_csv('matplotlib/data.csv')
result= plt.scatter(df['Duration'], df['Pulse'])
result= plt.bar(df['Duration'], df['Pulse'])
result= plt.plot(df['Duration'], df['Pulse'])
plt.show()