-- 1303. Find the Team Size
-- https://leetcode.com/problems/find-the-team-size/

SELECT employee_id, COUNT(team_id) OVER(PARTITION BY team_id) AS team_size
FROM Employee;