-- 1693. Daily Leads and Partners
-- https://leetcode.com/problems/daily-leads-and-partners/

-- Write your MySQL query statement below
SELECT date_id, make_name, COUNT(DISTINCT lead_id) as unique_leads, COUNT(DISTINCT partner_id) as unique_partners FROM DailySales GROUP BY make_name, date_id