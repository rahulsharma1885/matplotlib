import pandas as pd

# Example dataset URL from GitHub
# url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv'
data = pd.read_csv('data.csv')

# Display the first few rows
print(data)
