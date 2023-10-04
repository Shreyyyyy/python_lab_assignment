import pandas as pd

# 1. Import the dataset and interpret the results
hospital_data = pd.read_csv('airlines.csv')
print("First few rows of the dataset:")
print(hospital_data.head())

# 2. Understand the data frame
print("Data frame description:")
print(hospital_data.describe())
print("Data frame shape:", hospital_data.shape)
print("Data frame info:")
print(hospital_data.info())

# 3. Handling missing values
missing_values = hospital_data.isnull().sum()
hospital_data_delete = hospital_data.dropna()
hospital_data_replace = hospital_data.fillna(-1)
hospital_data_fill_forward = hospital_data.ffill()
hospital_data_fill_backward = hospital_data.bfill()

print("Data frame after deleting rows with missing values:")
print(hospital_data_delete)
print("Data frame after replacing missing values:")
print(hospital_data_replace)
print("Data frame after forward filling missing values:")
print(hospital_data_fill_forward)
print("Data frame after backward filling missing values:")
print(hospital_data_fill_backward)

# 4. Filter based on a column using groupby
department_counts = hospital_data.groupby('Department')['Patient_ID'].count()
print("Department-wise patient counts:")
print(department_counts)

# 5. Select 20 samples randomly and create a data frame with hierarchical indexing
random_samples = hospital_data.sample(n=20)
hierarchical_indexed_df = random_samples.set_index(['Department', 'Doctor_ID'])
print("Data frame with hierarchical indexing:")
print(hierarchical_indexed_df)
