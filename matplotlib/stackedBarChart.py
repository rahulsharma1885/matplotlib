import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df= sns.load_dataset('tips')

sns.barplot(df, x='sex', y='total_bill', hue='smoker', estimator=np.max, ci=None)
# data = {
#     'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
#     'Subcategory': ['Subcat 1', 'Subcat 2', 'Subcat 3', 
#                     'Subcat 1', 'Subcat 2', 'Subcat 3', 
#                     'Subcat 1', 'Subcat 2', 'Subcat 3'],
#     'Value': [5, 10, 15, 15, 20, 5, 25, 30, 10]
# }

# df = pd.DataFrame(data)

 
# sns.barplot(x='Category', y='Value', hue='Subcategory', data=df)


# plt.title('Simple Stacked Bar Chart with Seaborn')
# plt.xlabel('Categories')
# plt.ylabel('Values')

plt.show()
