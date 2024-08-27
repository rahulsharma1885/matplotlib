import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df= pd.read_csv('d.csv')
df=df.head(5)
plt.scatter(df['game_id'], df['year_id'])
plt.grid()
plt.show()
print(df)

# import seaborn as sns
# df = sns.load_dataset('tips')
# # plt.scatter(df['total_bill'], df['tip'])   # slow
# plt.plot(df['total_bill'], df['tip'] , 'o')  # Fast
# plt.show()
# print(df)
