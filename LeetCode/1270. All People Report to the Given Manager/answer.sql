-- 1270. All People Report to the Given Manager
-- https://leetcode.com/problems/all-people-report-to-the-given-manager/

-- Write your MySQL query statement below
WITH RECURSIVE Leaders AS (
    SELECT employee_id FROM Employees WHERE employee_id != 1 AND manager_id = 1
    UNION ALL
    SELECT Members.employee_id FROM Leaders JOIN Employees AS Members ON Leaders.employee_id = Members.manager_id
)

SELECT employee_id FROM Leaders ORDER BY employee_id
