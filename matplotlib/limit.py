import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

year=[2022, 2023, 2024, 2025]
price= [20000, 30000, 50000, 60000]

result= plt.scatter(year, price)
plt.xlim(2022,2024)
plt.ylim(20000, 50000)
plt.show()