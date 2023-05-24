-- 1350. Students With Invalid Departments
-- https://leetcode.com/problems/students-with-invalid-departments/

-- Write your MySQL query statement below
# SELECT Students.id, Students.name FROM Departments LEFT OUTER JOIN Students on Departments.id = Students.department_id
SELECT Students.id, Students.name FROM Students LEFT OUTER JOIN Departments on Departments.id = Students.department_id WHERE NOT EXISTS (SELECT * FROM Departments WHERE Departments.id = Students.department_id)