# Week 3 - Python & Data Wrangling
# Topics covered from the Week 3 course material:
# Python basics, Pandas data manipulation, Matplotlib & Seaborn basics
# Assignment: clean a messy dataset, handle missing values,
# filter rows, and create new columns.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Read the CSV file
df = pd.read_csv("data/messy_sales_data.csv")

print("=== ORIGINAL DATA ===")
print(df)
print("\n=== DATA INFO ===")
print(df.info())
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Handle missing Rating values using the median
df["Rating"] = df["Rating"].fillna(df["Rating"].median())

# 4. Create a new column: Revenue_per_Unit
df["Revenue_per_Unit"] = df["Revenue"] / df["Quantity"]

# 5. Create a new column: Rating_Category
def rating_category(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    return "Average"

df["Rating_Category"] = df["Rating"].apply(rating_category)

# 6. Filter rows
high_revenue = df[df["Revenue"] >= 20000]

print("\n=== CLEANED DATA ===")
print(df)

print("\n=== HIGH REVENUE PRODUCTS (Revenue >= 20000) ===")
print(high_revenue)

# 7. Basic grouping
category_summary = (
    df.groupby("Category", as_index=False)["Revenue"]
      .sum()
      .sort_values("Revenue", ascending=False)
)

print("\n=== CATEGORY REVENUE SUMMARY ===")
print(category_summary)

# 8. Save cleaned dataset
df.to_csv("data/cleaned_sales_data.csv", index=False)

# 9. Matplotlib visualization
plt.figure(figsize=(8, 5))
plt.bar(category_summary["Category"], category_summary["Revenue"])
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("revenue_by_category.png")
plt.show()

# 10. Seaborn visualization
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Category", y="Rating")
plt.title("Product Ratings by Category")
plt.xlabel("Category")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("ratings_by_category.png")
plt.show()

print("\nWeek 3 data wrangling completed successfully.")
