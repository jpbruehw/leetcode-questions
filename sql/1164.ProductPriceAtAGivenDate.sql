-- Table: Products

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | product_id    | int     |
-- | new_price     | int     |
-- | change_date   | date    |
-- +---------------+---------+
-- (product_id, change_date) is the primary key (combination of columns with unique values) of this table.
-- Each row of this table indicates that the price of some product was changed to a new price at some date.
 

-- Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Products table:
-- +------------+-----------+-------------+
-- | product_id | new_price | change_date |
-- +------------+-----------+-------------+
-- | 1          | 20        | 2019-08-14  |
-- | 2          | 50        | 2019-08-14  |
-- | 1          | 30        | 2019-08-15  |
-- | 1          | 35        | 2019-08-16  |
-- | 2          | 65        | 2019-08-17  |
-- | 3          | 20        | 2019-08-18  |
-- +------------+-----------+-------------+
-- Output: 
-- +------------+-------+
-- | product_id | price |
-- +------------+-------+
-- | 2          | 50    |
-- | 1          | 35    |
-- | 3          | 10    |
-- +------------+-------+

-- CTE -> use rank function to give rank
-- to each product id based on the date
WITH cte AS
(
    SELECT *, RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS rnk
    FROM Products
    WHERE change_date <= '2019-08-16'
)
-- select the product id and price where
-- rank is 1
-- this gives us the most RECENT change
-- to a given product since we don't need
-- any changes prior to that, we want the price
-- closest to 2019-08-16
SELECT product_id, new_price AS price
FROM cte
WHERE rnk = 1

UNION

-- select the remaining ids not in the cte
-- this means that their changes where
-- made AFTER 2019-08-16, in this case
-- we know that the price is 10
SELECT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM cte);