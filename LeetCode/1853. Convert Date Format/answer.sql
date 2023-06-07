-- 1853. Convert Date Format
-- https://leetcode.com/problems/convert-date-format/

-- Write your MySQL query statement below
SELECT DATE_FORMAT(day, "%W, %M %e, %Y") AS day FROM Days;