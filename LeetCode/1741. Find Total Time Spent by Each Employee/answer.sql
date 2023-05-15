-- 1741. Find Total Time Spent by Each Employee
-- https://leetcode.com/problems/find-total-time-spent-by-each-employee/

-- Write your MySQL query statement below

SELECT event_day AS day, emp_id, SUM(out_time) - SUM(in_time) AS total_time FROM Employees GROUP BY emp_id, event_day;