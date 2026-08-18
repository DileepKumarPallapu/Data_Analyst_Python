-- Week 2: SQL for Data Analysis
-- Compatible with MySQL 8+

CREATE DATABASE IF NOT EXISTS week2_data_analysis;
USE week2_data_analysis;

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    city VARCHAR(50),
    category VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers VALUES
(1, 'Arun Kumar', 'Chennai', 'Premium'),
(2, 'Priya Sharma', 'Bengaluru', 'Regular'),
(3, 'Rahul Verma', 'Hyderabad', 'Premium'),
(4, 'Sneha Reddy', 'Chennai', 'Regular'),
(5, 'Kiran Patel', 'Mumbai', 'Regular'),
(6, 'Anjali Rao', 'Pune', 'Premium');

INSERT INTO orders VALUES
(101, 1, '2026-08-01', 2500.00, 'Completed'),
(102, 2, '2026-08-02', 1800.00, 'Completed'),
(103, 1, '2026-08-03', 3200.00, 'Completed'),
(104, 3, '2026-08-04', 4500.00, 'Completed'),
(105, 4, '2026-08-05', 1200.00, 'Pending'),
(106, 5, '2026-08-06', 2750.00, 'Completed'),
(107, 3, '2026-08-07', 3900.00, 'Completed'),
(108, 2, '2026-08-08', 2100.00, 'Cancelled'),
(109, 6, '2026-08-09', 5000.00, 'Completed'),
(110, 4, '2026-08-10', 1600.00, 'Completed');

-- 1. SELECT: View all customers
SELECT * FROM customers;

-- 2. WHERE: Find completed orders
SELECT *
FROM orders
WHERE status = 'Completed';

-- 3. ORDER BY: Highest order amounts first
SELECT order_id, customer_id, amount
FROM orders
ORDER BY amount DESC;

-- 4. GROUP BY + SUM: Total revenue by customer
SELECT
    c.customer_id,
    c.customer_name,
    SUM(o.amount) AS total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'Completed'
GROUP BY c.customer_id, c.customer_name
ORDER BY total_revenue DESC;

-- 5. AVG: Average order value
SELECT ROUND(AVG(amount), 2) AS average_order_value
FROM orders
WHERE status = 'Completed';

-- 6. COUNT: Number of completed orders
SELECT COUNT(*) AS completed_orders
FROM orders
WHERE status = 'Completed';

-- 7. GROUP BY: Revenue by city
SELECT
    c.city,
    SUM(o.amount) AS total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'Completed'
GROUP BY c.city
ORDER BY total_revenue DESC;

-- 8. JOIN: Customer and order details
SELECT
    o.order_id,
    c.customer_name,
    c.city,
    o.order_date,
    o.amount,
    o.status
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
ORDER BY o.order_date;

-- 9. Subquery: Customers whose total completed spending is above average
SELECT
    c.customer_id,
    c.customer_name,
    SUM(o.amount) AS total_spending
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'Completed'
GROUP BY c.customer_id, c.customer_name
HAVING SUM(o.amount) > (
    SELECT AVG(customer_total)
    FROM (
        SELECT SUM(amount) AS customer_total
        FROM orders
        WHERE status = 'Completed'
        GROUP BY customer_id
    ) AS totals
)
ORDER BY total_spending DESC;

-- 10. CASE: Classify completed orders by value
SELECT
    order_id,
    amount,
    CASE
        WHEN amount >= 4000 THEN 'High Value'
        WHEN amount >= 2000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS order_category
FROM orders
WHERE status = 'Completed'
ORDER BY amount DESC;

-- 11. Top customers by total completed revenue
SELECT
    c.customer_name,
    SUM(o.amount) AS total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'Completed'
GROUP BY c.customer_id, c.customer_name
ORDER BY total_revenue DESC
LIMIT 3;

-- 12. Average order value by customer
SELECT
    c.customer_name,
    ROUND(AVG(o.amount), 2) AS average_order_value,
    COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'Completed'
GROUP BY c.customer_id, c.customer_name
ORDER BY average_order_value DESC;
