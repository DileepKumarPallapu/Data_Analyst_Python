# Week 2 – Python for Data Analysis
# Requirements: pandas, numpy

import pandas as pd

# 1. Load a CSV file using Pandas and display basic info.
df = pd.read_csv("data/sales_data.csv")

print("=== First 5 Rows ===")
print(df.head())

print("\n=== Basic Info ===")
df.info()

print("\n=== Statistical Summary ===")
print(df.describe())

# 2. Handle missing values and duplicates using Pandas.
print("\n=== Missing Values Before Cleaning ===")
print(df.isnull().sum())

df["Rating"] = df["Rating"].fillna(df["Rating"].median())
df = df.drop_duplicates()

print("\n=== Missing Values After Cleaning ===")
print(df.isnull().sum())

print("\n=== Duplicate Rows After Cleaning ===")
print(df.duplicated().sum())

# 3. Group data by category and find total revenue.
category_revenue = (
    df.groupby("Category", as_index=False)["Revenue"]
      .sum()
      .sort_values("Revenue", ascending=False)
)

print("\n=== Total Revenue by Category ===")
print(category_revenue)

# 4. Sort data by multiple columns using Python.
sorted_df = df.sort_values(
    by=["Category", "Revenue"],
    ascending=[True, False]
)

print("\n=== Sorted by Category and Revenue ===")
print(sorted_df)

# 5. Create a correlation matrix for numerical columns.
correlation_matrix = df.select_dtypes(include="number").corr()

print("\n=== Correlation Matrix ===")
print(correlation_matrix.round(2))
