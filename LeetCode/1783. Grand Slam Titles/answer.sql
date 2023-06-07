-- 1783. Grand Slam Titles
-- https://leetcode.com/problems/grand-slam-titles/

-- Write your MySQL query statement below
SELECT player_id, player_name, SUM(player_id=Wimbledon) + SUM(player_id=Fr_open) + SUM(player_id=US_open) + SUM(player_id=Au_open) AS grand_slams_count FROM Players JOIN Championships ON Players.player_id = Championships.Wimbledon OR Players.player_id = Championships.Fr_open OR Players.player_id = Championships.US_open OR Players.player_id = Championships.Au_open GROUP BY player_name ORDER BY player_name;