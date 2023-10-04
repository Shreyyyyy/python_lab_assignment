import pandas as pd
import numpy as np

# Step 1: Import the dataset
data = pd.read_csv("airlines.csv")

# Step 2: Explore the data frame
print("Data Frame Description:")
print(data.describe())
print("\nData Frame Shape:")
print(data.shape)
print("\nData Frame Info:")
print(data.info())

# Step 3: Handle missing values
# Method 1: Delete rows with missing data
data_delete = data.dropna()

# Method 2: Replace missing values with a specific value (e.g., 'N/A')
data_replace = data.fillna('N/A')

# Method 3: Fill missing values with mean for numerical columns
data_fill_mean = data.copy()
data_fill_mean['Airline ID'].fillna(data_fill_mean['Airline ID'].mean(), inplace=True)

# Method 4: Backfill missing values
data_backfill = data.fillna(method='bfill')

# Step 4: Filter based on a column using groupby
grouped_data = data.groupby('Country').size().reset_index(name='Counts')

# Step 5: Select 20 random samples and create a hierarchical index
sample_data = data.sample(n=20).reset_index(drop=True)

# Print the results
print("\nData Frame after Deleting Rows with Missing Data:")
print(data_delete)

print("\nData Frame after Replacing Missing Values:")
print(data_replace)

print("\nData Frame after Filling Missing Values with Mean (Airline ID):")
print(data_fill_mean)

print("\nData Frame after Backfilling Missing Values:")
print(data_backfill)

print("\nFiltered Data Based on 'Country' Column:")
print(grouped_data)

print("\nRandom 20 Samples with Hierarchical Index:")
print(sample_data)