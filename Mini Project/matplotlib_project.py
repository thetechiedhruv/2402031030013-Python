import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data/covid_data.csv')

# Filter data for one country (e.g., India)
india_df = df[df['country'] == 'India']

# Convert date column to datetime
india_df['date'] = pd.to_datetime(india_df['date'])

# Plot
plt.figure(figsize=(10, 5))
plt.plot(india_df['date'], india_df['new_cases'], label='New Cases', color='blue')
plt.plot(india_df['date'], india_df['new_deaths'], label='New Deaths', color='red')
plt.title('COVID-19 Daily Cases and Deaths in India')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
