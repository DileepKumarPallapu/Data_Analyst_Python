"""
Week 4 – End-to-End Data Analysis Capstone
EDA + Regression + Business Insights
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sales_data.csv"
OUT = ROOT / "PowerBI"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Date"])

# EDA
print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nDescriptive statistics:\n", df.describe(numeric_only=True))

# Business metrics
category_summary = (
    df.groupby("Category", as_index=False)
      .agg(Total_Sales=("Sales","sum"),
           Total_Quantity=("Quantity","sum"),
           Average_Rating=("Rating","mean"))
      .sort_values("Total_Sales", ascending=False)
)
product_summary = (
    df.groupby("Product", as_index=False)
      .agg(Total_Sales=("Sales","sum"),
           Total_Quantity=("Quantity","sum"),
           Average_Rating=("Rating","mean"))
      .sort_values("Total_Sales", ascending=False)
)

print("\nCategory summary:\n", category_summary)
print("\nTop products:\n", product_summary.head(5))

# Export summaries for Power BI
category_summary.to_csv(OUT / "category_summary.csv", index=False)
product_summary.to_csv(OUT / "product_summary.csv", index=False)
df.to_csv(OUT / "sales_data_for_powerbi.csv", index=False)

# Charts
plt.figure(figsize=(8,5))
category_summary.plot.bar(x="Category", y="Total_Sales", legend=False)
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(OUT / "sales_by_category.png")
plt.close()

plt.figure(figsize=(8,5))
df.groupby("Date", as_index=False)["Sales"].sum().plot(x="Date", y="Sales", marker="o")
plt.title("Sales Trend")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(OUT / "sales_trend.png")
plt.close()

# Regression: predict Sales using Revenue, Quantity, Rating and Category.
X = df[["Revenue", "Quantity", "Rating", "Category"]]
y = df["Sales"]

preprocess = ColumnTransformer(
    transformers=[("category", OneHotEncoder(handle_unknown="ignore"), ["Category"])],
    remainder="passthrough"
)
model = Pipeline([
    ("preprocess", preprocess),
    ("regressor", LinearRegression())
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("\nRegression Results")
print("MAE:", round(mean_absolute_error(y_test, pred), 2))
print("R2:", round(r2_score(y_test, pred), 4))

predictions = pd.DataFrame({"Actual_Sales": y_test.values, "Predicted_Sales": pred})
predictions.to_csv(OUT / "regression_predictions.csv", index=False)

print("\nAnalysis complete. Power BI-ready files are in:", OUT)
