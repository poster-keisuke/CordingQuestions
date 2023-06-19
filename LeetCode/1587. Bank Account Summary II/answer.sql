-- 1587. Bank Account Summary II
-- https://leetcode.com/problems/bank-account-summary-ii/

-- Write your MySQL query statement below
SELECT Users.name, SUM(amount) as BALANCE FROM Users JOIN Transactions ON Users.account = Transactions.account GROUP BY Users.account HAVING BALANCE > 10000;