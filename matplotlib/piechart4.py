import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data= pd.read_csv('d.csv')
# exp= [0.1 if i==0 else 0 for i in range(len(data))]
exp= [0.1 if i==0 else 0 for i in range(len(data['fran_id']))]
plt.pie(data['forecast'], labels=data['fran_id'],autopct="%0.1f%%" ,explode=exp, shadow=False)
plt.show()
