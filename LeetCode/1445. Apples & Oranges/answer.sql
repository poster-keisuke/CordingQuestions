-- 1445. Apples & Oranges
-- https://leetcode.com/problems/apples-oranges/

--  Write your MySQL query statement below
SELECT sale_date, SUM(CASE WHEN fruit = 'apples' THEN sold_num END) -  SUM(CASE WHEN fruit = 'oranges' THEN sold_num END) AS diff FROM Sales GROUP BY sale_date ORDER BY sale_date;