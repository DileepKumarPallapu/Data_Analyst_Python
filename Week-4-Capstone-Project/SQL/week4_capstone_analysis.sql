-- Week 4 – Capstone SQL Analysis
-- Import data/sales_data.csv into a table named sales_data before running.

-- 1. Overall business metrics
SELECT
    SUM(Sales) AS total_sales,
    SUM(Quantity) AS total_quantity,
    AVG(Rating) AS average_rating
FROM sales_data;

-- 2. Sales by category
SELECT
    Category,
    SUM(Sales) AS total_sales,
    SUM(Quantity) AS total_quantity,
    AVG(Rating) AS average_rating
FROM sales_data
GROUP BY Category
ORDER BY total_sales DESC;

-- 3. Top products by sales
SELECT
    Product,
    SUM(Sales) AS total_sales,
    SUM(Quantity) AS total_quantity,
    AVG(Rating) AS average_rating
FROM sales_data
GROUP BY Product
ORDER BY total_sales DESC;

-- 4. Monthly sales trend
SELECT
    MONTH(Date) AS month_number,
    SUM(Sales) AS total_sales
FROM sales_data
GROUP BY MONTH(Date)
ORDER BY month_number;
