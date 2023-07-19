-- 1393. Capital Gain/Loss
-- https://leetcode.com/problems/capital-gainloss/


-- Write your MySQL query statement below
WITH Results as (
  SELECT stock_name, -SUM(price) as capital_gain_loss FROM Stocks WHERE operation = "Buy" GROUP BY stock_name
  UNION ALL
  SELECT stock_name, SUM(price) as capital_gain_loss FROM Stocks WHERE operation = "Sell" GROUP BY stock_name
)

SELECT stock_name, SUM(capital_gain_loss) as capital_gain_loss FROM Results GROUP BY stock_name
