-- 1571. Warehouse Manager
-- https://leetcode.com/problems/warehouse-manager/

-- Write your MySQL query statement below
SELECT name AS warehouse_name, SUM(Width * Length * Height * units) AS volume FROM Warehouse
    JOIN Products on Warehouse.product_id = Products.product_id
    GROUP BY name
