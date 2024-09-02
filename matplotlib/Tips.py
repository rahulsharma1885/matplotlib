import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset and modify the 'size' column
tips = sns.load_dataset('tips')
tips['size'] = tips['size'] * 100

# Plot using matplotlib
plt.figure(figsize=(10, 6))
scatter = plt.scatter(x=tips['total_bill'], y=tips['tip'], 
                      c=tips['sex'].apply(lambda x: 0 if x == 'Male' else 1), 
                      s=tips['size'], cmap='viridis')
plt.title('Cost Analysis')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.colorbar(scatter, label='Sex')
plt.show()
