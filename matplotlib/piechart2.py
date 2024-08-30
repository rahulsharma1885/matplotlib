import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('d.csv')
plt.pie(data['elo_n'], labels=data['team_id'], autopct="%0.1f%%")

plt.show()
