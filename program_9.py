import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Step 1: Read the datasetv

data = pd.read_csv("airlines.csv")

# Step 2: Create basic plots

# Histogram of Airline IDs
plt.figure(figsize=(8, 6))
plt.hist(data['Airline ID'], bins=20, color='skyblue')
plt.xlabel('Airline ID')
plt.ylabel('Frequency')
plt.title('Histogram of Airline IDs')
plt.show()

# Scatter plot of Airline IDs vs. Active
plt.figure(figsize=(8, 6))
plt.scatter(data['Airline ID'], data['Active'], alpha=0.5, color='green')
plt.xlabel('Airline ID')
plt.ylabel('Active')
plt.title('Scatter Plot of Airline IDs vs. Active')
plt.show()

# Line plot of Airlines Count by Country
country_counts = data['Country'].value_counts()
plt.figure(figsize=(12, 6))
plt.plot(country_counts.index, country_counts.values, marker='o', linestyle='-', color='blue')
plt.xticks(rotation=90)
plt.xlabel('Country')
plt.ylabel('Count')
plt.title('Line Plot of Airlines Count by Country')
plt.show()

# Bar graph of the top 10 countries with the most airlines
top_10_countries = country_counts.head(10)
plt.figure(figsize=(10, 6))
plt.bar(top_10_countries.index, top_10_countries.values, color='purple')
plt.xticks(rotation=45)
plt.xlabel('Country')
plt.ylabel('Count')
plt.title('Top 10 Countries with the Most Airlines')
plt.show()

# Pie chart showing the distribution of Active/Inactive airlines
active_counts = data['Active'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(active_counts, labels=active_counts.index, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'])
plt.title('Distribution of Active/Inactive Airlines')
plt.show()

# Area plot showing cumulative counts by Country
cumulative_country_counts = country_counts.cumsum()
plt.figure(figsize=(12, 6))
plt.fill_between(cumulative_country_counts.index, cumulative_country_counts.values, color='orange', alpha=0.5)
plt.xticks(rotation=90)
plt.xlabel('Country')
plt.ylabel('Cumulative Count')
plt.title('Cumulative Count of Airlines by Country')
plt.show()

# Box plot of Airline IDs
plt.figure(figsize=(8, 6))
plt.boxplot(data['Airline ID'].dropna(), vert=False, widths=0.7)
plt.xlabel('Airline ID')
plt.title('Box Plot of Airline IDs')
plt.show()

# Pair plot (scatter matrix) of Airline ID vs. Active
sns.pairplot(data[['Airline ID', 'Active']], hue='Active', markers=['o', 's'], palette={"Y": "g", "N": "r"})
plt.title('Pair Plot of Airline ID vs. Active')
plt.show()

# Step 3: Draw two advanced graphs (example: Violin plot and Heatmap)

# Violin plot showing the distribution of Airline ID by Active status
plt.figure(figsize=(10, 6))
sns.violinplot(x='Active', y='Airline ID', data=data, palette={"Y": "g", "N": "r"})
plt.xlabel('Active')
plt.ylabel('Airline ID')
plt.title('Violin Plot of Airline ID by Active Status')
plt.show()

# Heatmap of correlation matrix between numerical columns
numerical_columns = data.select_dtypes(include=[np.number])
correlation_matrix = numerical_columns.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap of Correlation Matrix')
plt.show()