import pandas as pd

df = pd.read_csv('matplotlib/testfaildata.csv')
result= df['appData']
result.to_csv('mydata.csv', index=False)
# print(df)
