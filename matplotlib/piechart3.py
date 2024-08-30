import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('d.csv')

explode = [0.1 if i == 0 else 0 for i in range(len(data['fran_id']))]

plt.pie(data['forecast'], labels=data['fran_id'], autopct="%0.1f%%", explode=explode, shadow=True)
plt.savefig('sample.png')
plt.show()
