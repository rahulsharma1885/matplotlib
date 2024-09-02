import matplotlib.pyplot as plt
import pandas as pd

df= pd.read_csv('d.csv')

plt.subplot(2,2,1)
plt.plot(df['opp_fran'], df['team_id'])

plt.subplot(2,2,4)
plt.pie(df['year_id'], df['pts'])

plt.subplot(2,2,2)
plt.bar(df['opp_fran'], df['pts'])

plt.subplot(2,2,3)
plt.stem(df['opp_fran'], df['team_id'])

plt.show()