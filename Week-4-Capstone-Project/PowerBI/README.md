# Power BI Dashboard Guide – Week 4

The assignment asks for a business-metrics dashboard in Power BI or Tableau.

## Recommended visuals
1. Card: Total Sales
2. Card: Total Quantity
3. Card: Average Rating
4. Clustered column chart: Sales by Category
5. Bar chart: Top Products by Sales
6. Line chart: Sales Trend by Date
7. Slicers: Category, Product, Date

## Data
Import `data/sales_data.csv` into Power BI.

## Optional DAX measures
```DAX
Total Sales = SUM(sales_data[Sales])
Total Quantity = SUM(sales_data[Quantity])
Average Rating = AVERAGE(sales_data[Rating])
```

Save the finished Power BI report as `week4_sales_dashboard.pbix`.
The PBIX file must be created in Power BI Desktop; it cannot be generated reliably as a text file.
