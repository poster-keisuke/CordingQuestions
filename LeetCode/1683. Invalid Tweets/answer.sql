-- 1683. Invalid Tweets
-- https://leetcode.com/problems/invalid-tweets/

-- Write your MySQL query statement below
SELECT tweet_id FROM Tweets WHERE CHARACTER_LENGTH(content) > 15;