import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('d.csv')
plt.plot(df['game_id'], df['date_game'], marker='o', linewidth=3, linestyle= 'dotted', color='green', label='rahul')
plt.plot(df['elo_i'], df['team_id'], marker='o', linewidth=3, linestyle= 'solid', color='red', label='mohit')
# plt.ylim('0', '194611020PRO')
# plt.xlim('11/1/1946', '11/2/1946')
plt.title('DEMO')
plt.xlabel('Total')
plt.ylabel('date predection')
plt.legend(loc='best')
plt.grid()
plt.show()
print(df)