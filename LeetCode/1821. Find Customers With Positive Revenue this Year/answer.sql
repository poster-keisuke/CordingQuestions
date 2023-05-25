-- 1821. Find Customers With Positive Revenue this Year
-- https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/

-- Write your MySQL query statement below
SELECT customer_id FROM Customers WHERE year = '2021' AND revenue > 0 GROUP BY customer_id, year;