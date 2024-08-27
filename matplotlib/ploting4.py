import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from colorama import Fore, Style, init
init()

# Load your CSV data
df = pd.read_csv('d.csv')

# Plot the data
plt.plot(df['game_id'], df['is_playoffs'], color='green', label='rahul', linestyle='solid', linewidth=3, marker='+')
plt.title('demo')
plt.xlabel('game id')
plt.ylabel('score')
plt.legend(loc='best')
plt.show()

# Print in red text
print(Fore.YELLOW + 'RAHUL SHARMA' + Style.RESET_ALL)
