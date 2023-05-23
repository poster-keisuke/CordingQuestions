# 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_money = 0
        for account in accounts:
            sum_money = 0
            for money in account:
                sum_money += money

            if max_money < sum_money:
                max_money = sum_money

        return max_money
