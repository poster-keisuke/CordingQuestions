-- 2084. Drop Type 1 Orders for Customers With Type 0 Orders
-- https://leetcode.com/problems/drop-type-1-orders-for-customers-with-type-0-orders/

SELECT * FROM Orders
WHERE (customer_id, order_type)
IN (SELECT customer_id, MIN(order_type)
    FROM Orders
    GROUP BY customer_id)